"""Generate the four publication figures (English variant).

    figures/fig1_continuum.pdf            — six-stage spectrum diagram
    figures/fig2_frequency_by_stage.pdf   — frequency bars with key tests
    figures/fig3_meccan_medinan.pdf       — revelation-context distribution
    figures/fig4_cooccurrence.pdf         — proximity co-occurrence network

Publication-grade upgrade for *Journal of Qur'anic Studies*:
  * Okabe-Ito and viridis/cividis colour-blind-safe palettes.
  * Serif typography (DejaVu Serif fallback if EB Garamond absent).
  * Amiri (bundled) loaded explicitly for Arabic glyph rendering.
  * Key statistical findings embedded directly into figures.
  * Minimal spines, no gridded background noise.
"""
from __future__ import annotations

import csv
import io
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # noqa: E402

import matplotlib.pyplot as plt  # noqa: E402
import matplotlib.font_manager as fm  # noqa: E402
import networkx as nx  # noqa: E402
import arabic_reshaper  # noqa: E402
from bidi.algorithm import get_display  # noqa: E402

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR / "analysis"))
from spectrum_roots import SPECTRUM, STAGE_LABELS_EN  # noqa: E402

CONC_DIR = ROOT_DIR / "data" / "concordance"
FIG_DIR = ROOT_DIR / "figures"
FIG_DIR.mkdir(exist_ok=True)
FONT_DIR = ROOT_DIR / "paper" / "fonts"

# ------------------------------------------------------------------ #
# Font registration — bundle Amiri so figures embed Arabic without   #
# depending on system fonts.                                         #
# ------------------------------------------------------------------ #
AMIRI_REGULAR = FONT_DIR / "amiri-regular.ttf"
AMIRI_BOLD = FONT_DIR / "amiri-bold.ttf"
EBGARAMOND = FONT_DIR / "ebgaramond-regular.ttf"

for _f in (AMIRI_REGULAR, AMIRI_BOLD, EBGARAMOND):
    if _f.exists():
        fm.fontManager.addfont(str(_f))

ARABIC_FP = fm.FontProperties(fname=str(AMIRI_REGULAR)) if AMIRI_REGULAR.exists() else None
ARABIC_BOLD_FP = fm.FontProperties(fname=str(AMIRI_BOLD)) if AMIRI_BOLD.exists() else ARABIC_FP


def ar(text: str) -> str:
    """Reshape and reorder an Arabic/Persian string for matplotlib rendering."""
    if not text:
        return text
    return get_display(arabic_reshaper.reshape(text))


# Serif typography, journal-grade defaults.
_serif_stack = ["EB Garamond", "DejaVu Serif", "Times New Roman", "Times", "serif"]
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": _serif_stack,
    "font.size": 10,
    "axes.labelsize": 10.5,
    "axes.titlesize": 11.5,
    "axes.titleweight": "normal",
    "axes.labelweight": "normal",
    "legend.fontsize": 9,
    "legend.frameon": False,
    "xtick.labelsize": 9.5,
    "ytick.labelsize": 9.5,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.linewidth": 0.8,
    "xtick.major.width": 0.7,
    "ytick.major.width": 0.7,
    "xtick.major.size": 3.5,
    "ytick.major.size": 3.5,
    "figure.dpi": 150,
    "savefig.bbox": "tight",
    "savefig.dpi": 300,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})

# Okabe-Ito colour-blind-safe palette (Wong 2011, modified for the six-stage
# progression: cool blue → warm orange-red → green-outcome).
STAGE_COLORS = {
    1: "#56B4E9",  # sky blue          — pre-anger displeasure
    2: "#0072B2",  # ocean blue        — inner pressure / contraction
    3: "#E69F00",  # orange            — evaluative aversion
    4: "#D55E00",  # vermilion         — active anger
    5: "#7B1E25",  # dark vermilion    — compressed rage
    6: "#009E73",  # bluish green      — behavioural outcomes
}

CANONICAL_ORDER = [r.bw for r in SPECTRUM]


def load_summary() -> list[dict]:
    rows = []
    with (CONC_DIR / "summary_counts.csv").open("r", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            row["stage"] = int(row["stage"])
            row["occurrences"] = int(row["occurrences"])
            row["meccan_hits"] = int(row["meccan_hits"])
            row["medinan_hits"] = int(row["medinan_hits"])
            rows.append(row)
    core_bw = {r.bw for r in SPECTRUM}
    return [r for r in rows if r["root_bw"] in core_bw]


def load_meccan_baseline() -> float:
    """Read the Meccan-rate prior the same way advanced_metrics does."""
    try:
        with (ROOT_DIR / "data" / "quran" / "quran_check.json").open("r",
                                                                    encoding="utf-8") as fh:
            doc = json.load(fh)
        suras = doc.get("suras") or doc.get("sura_info") or []
        if not suras:
            return 0.74
        total_v = sum(s.get("total_verses", 0) for s in suras)
        meccan_v = sum(s.get("total_verses", 0) for s in suras
                       if str(s.get("revelation", "")).lower().startswith("mec"))
        if total_v == 0:
            return 0.74
        return meccan_v / total_v
    except Exception:
        return 0.74


def _ax_clean(ax):
    """Strip the plot to journal aesthetics: 2-spine, no grid, light ticks."""
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    ax.spines["left"].set_color("#444444")
    ax.spines["bottom"].set_color("#444444")
    ax.tick_params(colors="#444444", which="both")
    ax.grid(False)


# ------------------------------------------------------------------ #
#  Figure 1 — Six-stage continuum                                    #
# ------------------------------------------------------------------ #

def fig1_continuum(rows: list[dict]) -> None:
    fig, ax = plt.subplots(figsize=(14, 5.4))
    n = len(SPECTRUM)
    width = n + 1
    ax.set_xlim(0, width)
    ax.set_ylim(0, 6.6)
    ax.axis("off")

    by_stage: dict[int, list[int]] = defaultdict(list)
    for i, r in enumerate(SPECTRUM):
        by_stage[r.stage].append(i + 1)

    # Stage bands — very low-alpha tint, no hard edges
    for st, xs_in_stage in sorted(by_stage.items()):
        x0 = min(xs_in_stage) - 0.5
        x1 = max(xs_in_stage) + 0.5
        ax.axhspan(1.1, 4.3, xmin=(x0 / width), xmax=(x1 / width),
                   facecolor=STAGE_COLORS[st], alpha=0.075, zorder=0)
        ax.text((x0 + x1) / 2, 5.55, f"Stage {st}",
                ha="center", va="center", fontsize=10.5, fontweight="bold",
                color=STAGE_COLORS[st], family="serif")
        ax.text((x0 + x1) / 2, 5.05,
                STAGE_LABELS_EN[st].split(" — ")[1],
                ha="center", va="center", fontsize=9,
                color=STAGE_COLORS[st], style="italic", family="serif")

    by_bw = {r["root_bw"]: r for r in rows}
    surface_by_bw = {r.bw: r.display() for r in SPECTRUM}

    for i, r in enumerate(SPECTRUM, start=1):
        rec = by_bw.get(r.bw)
        if rec is None:
            continue
        st = r.stage
        size = 360 + 78 * (rec["occurrences"] ** 0.55)
        ax.scatter(i, 2.8, s=size, color=STAGE_COLORS[st],
                   edgecolor="#222222", linewidth=0.9, zorder=3)
        ax.text(i, 2.8, ar(surface_by_bw[r.bw]), ha="center", va="center",
                fontsize=12.5, color="white", zorder=4,
                fontproperties=ARABIC_BOLD_FP)
        ax.text(i, 1.83, f"n = {rec['occurrences']}", ha="center", va="center",
                fontsize=9, color="#222222", zorder=4, family="serif")
        ax.text(i, 1.42, r.translit, ha="center", va="center",
                fontsize=8.5, color="#555555", zorder=4, style="italic",
                family="serif")

    # Lightweight directional arrows with gradient alpha
    for i in range(1, n):
        ax.annotate("", xy=(i + 1 - 0.32, 2.8), xytext=(i + 0.32, 2.8),
                    arrowprops=dict(arrowstyle="-|>", color="#888888",
                                    lw=0.9, alpha=0.6,
                                    mutation_scale=10), zorder=2)

    ax.text(width / 2, 0.62,
            "Action-intensity axis  →",
            ha="center", va="center", fontsize=11.5, fontweight="bold",
            color="#222222", family="serif")

    # Embedded finding (top-right)
    ax.text(width - 0.1, 6.35,
            r"$\chi^2(1)=1.55$  (phenomenology S1–5 vs. outcomes S6) — "
            "fails to reject (bidirectional reading, §4.8.5)",
            ha="right", va="top", fontsize=8.5, color="#444444",
            style="italic", family="serif")

    out = FIG_DIR / "fig1_continuum.pdf"
    plt.savefig(out)
    plt.savefig(out.with_suffix(".png"), dpi=200)
    plt.close()
    print(f"Wrote {out}")


# ------------------------------------------------------------------ #
#  Figure 2 — Per-root and per-stage frequency                       #
# ------------------------------------------------------------------ #

def fig2_frequency_by_stage(rows: list[dict]) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.6),
                                   gridspec_kw={"width_ratios": [1.35, 1.0]})
    by_bw = {r["root_bw"]: r for r in rows}
    surface_by_bw = {r.bw: r.display() for r in SPECTRUM}

    labels_ar = [surface_by_bw[bw] for bw in CANONICAL_ORDER]
    translit = [r.translit for r in SPECTRUM]
    counts = [by_bw[bw]["occurrences"] for bw in CANONICAL_ORDER]
    colors = [STAGE_COLORS[by_bw[bw]["stage"]] for bw in CANONICAL_ORDER]
    x = list(range(len(CANONICAL_ORDER)))

    bars = ax1.bar(x, counts, color=colors, edgecolor="#222222", linewidth=0.5,
                   width=0.78)
    ax1.set_xticks(x)
    # Two-line tick labels: Arabic on top (Amiri), transliteration beneath.
    ax1.set_xticklabels([""] * len(x))
    ymax_left = max(counts) * 1.18
    ax1.set_ylim(0, ymax_left)
    for xi, (lab_ar, lab_tr) in enumerate(zip(labels_ar, translit)):
        ax1.text(xi, -ymax_left * 0.04, ar(lab_ar),
                 ha="center", va="top", fontsize=14,
                 fontproperties=ARABIC_FP)
        ax1.text(xi, -ymax_left * 0.13, lab_tr,
                 ha="center", va="top", fontsize=8, style="italic",
                 color="#555555", family="serif")

    ax1.set_ylabel("Occurrences in the Qur'an", fontsize=11, family="serif")
    ax1.set_title("(a) Per-root frequency", fontsize=11.5, loc="left",
                  family="serif")
    for b, c in zip(bars, counts):
        ax1.text(b.get_x() + b.get_width() / 2, c + max(counts) * 0.015,
                 str(c), ha="center", va="bottom", fontsize=8.5,
                 color="#222222", family="serif")
    _ax_clean(ax1)

    # Stage panel
    stage_totals: dict[int, int] = defaultdict(int)
    for r in rows:
        stage_totals[r["stage"]] += r["occurrences"]
    stages = sorted(stage_totals.keys())
    bars2 = ax2.bar(stages, [stage_totals[s] for s in stages],
                    color=[STAGE_COLORS[s] for s in stages],
                    edgecolor="#222222", linewidth=0.5, width=0.7)
    ax2.set_xticks(stages)
    short = [STAGE_LABELS_EN[s].split(" — ")[1] for s in stages]
    short = [s.replace("Behavioural Outcomes", "Beh. Outcomes")
              .replace("Inner Pressure & Contraction", "Inner Pressure")
              .replace("Evaluative Aversion", "Eval. Aversion")
              .replace("Pre-Anger Displeasure", "Pre-Anger")
              .replace("Compressed Rage", "Compr. Rage")
              .replace("Active Anger", "Active Anger") for s in short]
    ax2.set_xticklabels([f"S{s}\n{lbl}" for s, lbl in zip(stages, short)],
                        fontsize=8.6, family="serif")
    ax2.set_ylabel("Total occurrences", fontsize=11, family="serif")
    ax2.set_title("(b) Stage-level totals", fontsize=11.5, loc="left",
                  family="serif")
    ymax_right = max(stage_totals.values()) * 1.2
    ax2.set_ylim(0, ymax_right)
    for b, s in zip(bars2, stages):
        ax2.text(b.get_x() + b.get_width() / 2,
                 stage_totals[s] + ymax_right * 0.015,
                 str(stage_totals[s]),
                 ha="center", va="bottom", fontsize=10.5, fontweight="bold",
                 color="#222222", family="serif")
    _ax_clean(ax2)

    # Embedded statistical findings — drawn in panel (b)'s axes coords
    finding = (
        r"$\chi^2(5) = 227.15$,  asymptotic $p < 0.001$"
        "\n"
        r"permutation $p = 0.24$  (10 000 reshuffles, seed 20260509)"
        "\n"
        r"S1–5 vs. S6:  $\chi^2(1) = 1.55$  (fail to reject)"
    )
    ax2.text(0.98, 0.97, finding, transform=ax2.transAxes,
             ha="right", va="top", fontsize=8.6, family="serif",
             color="#222222",
             bbox=dict(boxstyle="round,pad=0.45", fc="#F5F1E8",
                       ec="#888888", lw=0.6))

    fig.tight_layout()
    out = FIG_DIR / "fig2_frequency_by_stage.pdf"
    plt.savefig(out)
    plt.savefig(out.with_suffix(".png"), dpi=200)
    plt.close()
    print(f"Wrote {out}")


# ------------------------------------------------------------------ #
#  Figure 3 — Meccan/Medinan distribution                            #
# ------------------------------------------------------------------ #

def fig3_meccan_medinan(rows: list[dict]) -> None:
    fig, ax = plt.subplots(figsize=(14, 6))
    by_bw = {r["root_bw"]: r for r in rows}
    surface_by_bw = {r.bw: r.display() for r in SPECTRUM}
    labels_ar = [surface_by_bw[bw] for bw in CANONICAL_ORDER]
    translit = [r.translit for r in SPECTRUM]
    meccan = [by_bw[bw]["meccan_hits"] for bw in CANONICAL_ORDER]
    medinan = [by_bw[bw]["medinan_hits"] for bw in CANONICAL_ORDER]
    totals = [m + md for m, md in zip(meccan, medinan)]

    x = list(range(len(CANONICAL_ORDER)))
    # Cividis-style two-tone (cb-safe blue-vs-tan).
    c_meccan = "#CABF8A"
    c_medinan = "#1F6F8B"
    ax.bar(x, meccan, color=c_meccan, edgecolor="#222222",
           linewidth=0.4, label="Meccan", width=0.78)
    ax.bar(x, medinan, bottom=meccan, color=c_medinan,
           edgecolor="#222222", linewidth=0.4, label="Medinan", width=0.78)

    ymax = max(totals) * 1.22
    ax.set_ylim(0, ymax)
    ax.set_xticks(x)
    ax.set_xticklabels([""] * len(x))
    for xi, (lab_ar, lab_tr) in enumerate(zip(labels_ar, translit)):
        ax.text(xi, -ymax * 0.04, ar(lab_ar),
                ha="center", va="top", fontsize=14,
                fontproperties=ARABIC_FP)
        ax.text(xi, -ymax * 0.10, lab_tr,
                ha="center", va="top", fontsize=8, style="italic",
                color="#555555", family="serif")
    ax.set_ylabel("Occurrences", fontsize=11, family="serif")

    # Per-bar Meccan-share annotation
    for xi, bw in enumerate(CANONICAL_ORDER):
        rec = by_bw[bw]
        tot = rec["meccan_hits"] + rec["medinan_hits"]
        if tot > 0:
            pct = 100.0 * rec["meccan_hits"] / tot
            ax.text(xi, tot + ymax * 0.015,
                    f"{rec['meccan_hits']}/{rec['medinan_hits']}",
                    ha="center", va="bottom", fontsize=8.2,
                    color="#444444", family="serif")
            ax.text(xi, tot + ymax * 0.055,
                    f"{pct:.0f}% Mec.",
                    ha="center", va="bottom", fontsize=7.6,
                    color="#777777", style="italic", family="serif")

    # Baseline Meccan-rate reference line (proportion of ayat, weighted by sura)
    baseline = load_meccan_baseline()
    # Convert proportion → reference line in *expected stacked share*: instead
    # of a single horizontal line (meaningless here), annotate as text and
    # mark the binomial-significant root in red.
    ax.legend(loc="upper left", fontsize=10, frameon=False)

    # Embedded finding box (top-right)
    finding = (
        f"Meccan baseline (verse-weighted): {baseline*100:.1f}%\n"
        r"$\bf{sakhaṭ}$: 0/4 Meccan, raw $p=0.005$, Holm $p=0.05$"
        " — sole FDR survivor"
    )
    ax.text(0.99, 0.97, finding, transform=ax.transAxes,
            ha="right", va="top", fontsize=8.6, family="serif",
            color="#222222",
            bbox=dict(boxstyle="round,pad=0.45", fc="#F5F1E8",
                      ec="#888888", lw=0.6))

    # Highlight the sakhat bar with an arrow
    if "sxT" in CANONICAL_ORDER:
        sx_i = CANONICAL_ORDER.index("sxT")
        sx_tot = totals[sx_i]
        ax.annotate("sakhaṭ — 0/4\n(only FDR-significant)",
                    xy=(sx_i, sx_tot),
                    xytext=(sx_i + 1.6, sx_tot + ymax * 0.30),
                    fontsize=8.5, color="#7B1E25", family="serif",
                    arrowprops=dict(arrowstyle="->", color="#7B1E25",
                                    lw=0.9, alpha=0.85))

    _ax_clean(ax)
    fig.tight_layout()
    out = FIG_DIR / "fig3_meccan_medinan.pdf"
    plt.savefig(out)
    plt.savefig(out.with_suffix(".png"), dpi=200)
    plt.close()
    print(f"Wrote {out}")


# ------------------------------------------------------------------ #
#  Figure 4 — Aya-level co-occurrence network                        #
# ------------------------------------------------------------------ #

def fig4_cooccurrence() -> None:
    aya_to_roots: dict[tuple[int, int], set[str]] = defaultdict(set)
    with (CONC_DIR / "master_concordance.csv").open("r", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            aya_to_roots[(int(row["sura"]), int(row["aya"]))].add(row["root_bw"])

    core = [r.bw for r in SPECTRUM]
    core_set = set(core)
    edges: Counter = Counter()
    for (_sura, _aya), roots in aya_to_roots.items():
        present = sorted(roots & core_set)
        for i, a in enumerate(present):
            for b in present[i + 1:]:
                edges[(a, b)] += 1

    G = nx.Graph()
    for r in SPECTRUM:
        G.add_node(r.bw, arabic=r.arabic, stage=r.stage)
    for (a, b), w in edges.items():
        G.add_edge(a, b, weight=w)

    connected = [n for n in G.nodes() if G.degree(n) > 0]
    isolated = [n for n in G.nodes() if G.degree(n) == 0]
    G_main = G.subgraph(connected).copy()
    if G_main.number_of_nodes() > 0:
        pos = nx.spring_layout(G_main, weight="weight", seed=42,
                               k=1.7, iterations=500)
    else:
        pos = {}
    if isolated:
        ys = ([0.0] if len(isolated) == 1
              else [1.0 - 2.0 * i / (len(isolated) - 1)
                    for i in range(len(isolated))])
        for node, y in zip(isolated, ys):
            pos[node] = (1.55, y * 0.7)

    fig, ax = plt.subplots(figsize=(10, 8.5))

    bw_to_root = {r.bw: r for r in SPECTRUM}

    if G.number_of_edges() > 0:
        max_w = max(d["weight"] for _, _, d in G.edges(data=True))
        for u, v, d in G.edges(data=True):
            w_norm = d["weight"] / max_w
            ax.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]],
                    color="#555555", alpha=0.22 + 0.55 * w_norm,
                    linewidth=0.7 + 3.4 * w_norm, zorder=1,
                    solid_capstyle="round")
            mx = (pos[u][0] + pos[v][0]) / 2
            my = (pos[u][1] + pos[v][1]) / 2
            ax.text(mx, my, str(d["weight"]), fontsize=7.5,
                    ha="center", va="center", color="#333333",
                    family="serif",
                    bbox=dict(boxstyle="round,pad=0.18", fc="white",
                              ec="#888888", lw=0.4, alpha=0.9))

    for r in SPECTRUM:
        x, y = pos[r.bw]
        ax.scatter(x, y, s=1050, color=STAGE_COLORS[r.stage],
                   edgecolor="#222222", linewidth=0.9, zorder=2)
        ax.text(x, y + 0.012, ar(r.display()), ha="center", va="center",
                fontsize=12, color="white", zorder=3,
                fontproperties=ARABIC_BOLD_FP)
        ax.text(x, y - 0.085, r.translit, ha="center", va="center",
                fontsize=7.2, color="#222222", zorder=3,
                family="serif", style="italic")

    if isolated:
        ax.text(1.55, 0.78,
                "isolated\n(no aya-level\nco-occurrence)",
                ha="center", va="bottom", fontsize=8.2, style="italic",
                color="#777777", family="serif")
        ax.axvline(x=1.30, ymin=0.04, ymax=0.94, color="#CCCCCC",
                   linestyle="--", linewidth=0.7, zorder=0)

    # Bridge-node annotation. Compute betweenness on the *main* connected
    # subgraph for a quick highlight (the precise CIs live in fig 7).
    if G_main.number_of_edges() > 0:
        btw = nx.betweenness_centrality(G_main, weight="weight")
        top_bridges = sorted(btw.items(), key=lambda kv: -kv[1])[:3]
        # Compose a small caption listing the top bridge nodes
        top_text = "Top bridge nodes (betweenness):\n" + " · ".join(
            f"{bw_to_root[bw].translit} ({v:.2f})"
            for bw, v in top_bridges if v > 0
        )
    else:
        top_text = ""

    # Legend
    legend_handles = []
    for st in sorted(set(r.stage for r in SPECTRUM)):
        legend_handles.append(plt.scatter([], [], color=STAGE_COLORS[st],
                                          s=130, edgecolor="#222222",
                                          linewidth=0.6,
                                          label=STAGE_LABELS_EN[st]))
    leg = ax.legend(handles=legend_handles, loc="upper left",
                    fontsize=8.5, framealpha=0.95, frameon=True,
                    edgecolor="#888888")
    for txt in leg.get_texts():
        txt.set_family("serif")

    # Stats banner
    n_edges = G.number_of_edges()
    total_cooc = sum(d["weight"] for _, _, d in G.edges(data=True))
    stats = (f"Nodes: {G.number_of_nodes()}   "
             f"Edges: {n_edges}   "
             f"Σ co-occurrences: {total_cooc}")
    ax.text(0.02, 0.02, stats, transform=ax.transAxes,
            ha="left", va="bottom", fontsize=8.4, color="#444444",
            family="serif",
            bbox=dict(boxstyle="round,pad=0.35", fc="white",
                      ec="#AAAAAA", lw=0.5))
    if top_text:
        ax.text(0.98, 0.02, top_text, transform=ax.transAxes,
                ha="right", va="bottom", fontsize=8.4, color="#222222",
                family="serif",
                bbox=dict(boxstyle="round,pad=0.4", fc="#F5F1E8",
                          ec="#888888", lw=0.6))

    # Embed strongest-edge / bridging finding. When multiple edges tie at the
    # maximum weight, list all of them; this avoids hiding the S2 ḥzn–ḍyq
    # corpus-validation tie that the manuscript foregrounds.
    if G.number_of_edges() > 0:
        max_w = max(d["weight"] for _, _, d in G.edges(data=True))
        top_edges = [(u, v, d) for u, v, d in G.edges(data=True)
                     if d["weight"] == max_w]
        ties = "  ·  ".join(
            f"{bw_to_root[u].translit}–{bw_to_root[v].translit}"
            for u, v, _ in top_edges
        )
        tip = (f"Strongest ties (w = {max_w}):  {ties}"
               "  — S2 corpus-validation & S1↔S6 bridge")
        ax.text(0.5, 0.97, tip, transform=ax.transAxes,
                ha="center", va="top", fontsize=8.8, color="#222222",
                family="serif", style="italic")

    ax.axis("off")
    fig.tight_layout()
    out = FIG_DIR / "fig4_cooccurrence.pdf"
    plt.savefig(out)
    plt.savefig(out.with_suffix(".png"), dpi=200)
    plt.close()
    print(f"Wrote {out}")
    print(f"Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges, "
          f"total co-occurrences = {sum(d['weight'] for _, _, d in G.edges(data=True))}")


if __name__ == "__main__":
    rows = load_summary()
    fig1_continuum(rows)
    fig2_frequency_by_stage(rows)
    fig3_meccan_medinan(rows)
    fig4_cooccurrence()
