"""Generate the four publication figures (Persian-localized variant).

    figures_fa/fig1_continuum.pdf       — canonical four-stage spectrum
    figures_fa/fig2_frequency_by_stage.pdf — frequency bars (linear & log)
    figures_fa/fig3_meccan_medinan.pdf  — revelation-context distribution
    figures_fa/fig4_cooccurrence.pdf    — proximity co-occurrence network

All figures use a clean academic style with Arabic/Persian text rendering.
"""
from __future__ import annotations

import csv
import io
import sys
from collections import Counter, defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # noqa: E402

import matplotlib.pyplot as plt  # noqa: E402
import networkx as nx  # noqa: E402
import arabic_reshaper  # noqa: E402
from bidi.algorithm import get_display  # noqa: E402

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR / "analysis"))
from spectrum_roots import SPECTRUM, STAGE_LABELS_FA as STAGE_LABELS  # noqa: E402

CONC_DIR = ROOT_DIR / "data" / "concordance"
FIG_DIR = ROOT_DIR / "figures_fa"
FIG_DIR.mkdir(exist_ok=True)


def ar(text: str) -> str:
    """Reshape and reorder an Arabic/Persian string for matplotlib rendering."""
    if not text:
        return text
    return get_display(arabic_reshaper.reshape(text))


_PERSIAN_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")


def _to_persian_digits(n: int) -> str:
    return str(n).translate(_PERSIAN_DIGITS)


# Academic style. Tahoma supports Arabic/Persian shaping on Windows.
plt.rcParams.update({
    "font.family": ["Tahoma", "DejaVu Sans"],
    "font.size": 10,
    "axes.labelsize": 11,
    "axes.titlesize": 12,
    "legend.fontsize": 9,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 150,
    "savefig.bbox": "tight",
    "savefig.dpi": 300,
})

# Six-stage colour-blind-safe palette
STAGE_COLORS = {
    1: "#7FB3D5", 2: "#4C72B0", 3: "#DD8452",
    4: "#C44E52", 5: "#8E0E25", 6: "#55A868",
}

# Persian short labels (no "مرحله N — " prefix) per stage
STAGE_SHORT_FA = {
    1: "تضجر و ناخشنودی",
    2: "فشار درونی",
    3: "انزجار ارزیابانه",
    4: "خشم فعال",
    5: "خشم متراکم",
    6: "پیامد رفتاری",
}

CANONICAL_ORDER = [r.bw for r in SPECTRUM]

# Persian numerals for figure titles
FA_NUM = {1: "۱", 2: "۲", 3: "۳", 4: "۴", 5: "۵", 6: "۶", 7: "۷"}


def load_summary() -> list[dict]:
    rows = []
    with (CONC_DIR / "summary_counts.csv").open("r", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            row["stage"] = int(row["stage"])
            row["occurrences"] = int(row["occurrences"])
            row["meccan_hits"] = int(row["meccan_hits"])
            row["medinan_hits"] = int(row["medinan_hits"])
            rows.append(row)
    # Keep core spectrum only (10 roots) for headline figures
    core_bw = {r.bw for r in SPECTRUM}
    return [r for r in rows if r["root_bw"] in core_bw]


def fig1_continuum(rows: list[dict]) -> None:
    """Six-stage continuum diagram with 14 core roots, Persian labels."""
    n = len(SPECTRUM)
    width = n + 1
    fig, ax = plt.subplots(figsize=(16, 6.0))
    ax.set_xlim(0, width)
    ax.set_ylim(0, 6.4)
    ax.axis("off")

    by_stage_xs: dict[int, list[int]] = {}
    for i, r in enumerate(SPECTRUM):
        by_stage_xs.setdefault(r.stage, []).append(i + 1)

    for st, xs_in_stage in sorted(by_stage_xs.items()):
        x0 = min(xs_in_stage) - 0.5
        x1 = max(xs_in_stage) + 0.5
        ax.axhspan(1.2, 4.4, xmin=(x0 / width), xmax=(x1 / width),
                   facecolor=STAGE_COLORS[st], alpha=0.08, zorder=0)
        ax.text((x0 + x1) / 2, 5.4, ar(f"مرحله {FA_NUM[st]}"),
                ha="center", va="center", fontsize=10, fontweight="bold",
                color=STAGE_COLORS[st])
        ax.text((x0 + x1) / 2, 4.95, ar(STAGE_SHORT_FA[st]),
                ha="center", va="center", fontsize=8.5,
                color=STAGE_COLORS[st], style="italic")

    by_bw = {r["root_bw"]: r for r in rows}
    for i, root in enumerate(SPECTRUM, start=1):
        rec = by_bw.get(root.bw)
        if rec is None:
            continue
        st = root.stage
        size = 320 + 70 * (rec["occurrences"] ** 0.55)
        ax.scatter(i, 2.8, s=size, color=STAGE_COLORS[st],
                   edgecolor="black", linewidth=0.8, zorder=3)
        ax.text(i, 2.8, ar(root.display()), ha="center", va="center",
                fontsize=10.5, fontweight="bold", color="white", zorder=4)
        ax.text(i, 1.85, f"n = {rec['occurrences']}", ha="center", va="center",
                fontsize=8.5, color="black", zorder=4)
        ax.text(i, 1.45, f"({root.bw})", ha="center", va="center",
                fontsize=7.5, color="dimgray", zorder=4, style="italic")

    for i in range(1, n):
        ax.annotate("", xy=(i + 1 - 0.3, 2.8), xytext=(i + 0.3, 2.8),
                    arrowprops=dict(arrowstyle="->", color="gray", lw=1.0,
                                    alpha=0.55), zorder=2)

    # Axis label (Persian) — center on the dynamic figure width
    ax.text(width / 2, 0.55,
            ar("شدت کنش  ←"),
            ha="center", va="center", fontsize=12, fontweight="bold",
            color="black")

    ax.set_title(ar("پیوستار شش-مرحله‌ای شدت خشم در قرآن کریم — "
                    "از آزردگی درونی تا عصیان رفتاری") + "\n"
                 + ar("گره = ریشهٔ عربی؛ اندازه ∝ بسامد در پیکره (Dukes 2011)"),
                 fontsize=11, pad=12)

    out = FIG_DIR / "fig1_continuum.pdf"
    plt.savefig(out)
    plt.savefig(out.with_suffix(".png"))
    plt.close()
    print(f"Wrote {out}")


def fig2_frequency_by_stage(rows: list[dict]) -> None:
    """Bar chart of per-root frequencies grouped by stage."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

    canonical = [bw for bw in CANONICAL_ORDER if bw in {r["root_bw"] for r in rows}]
    by_bw = {r["root_bw"]: r for r in rows}

    surface_by_bw = {r.bw: r.display() for r in SPECTRUM}
    labels = [ar(surface_by_bw[bw]) for bw in canonical]
    counts = [by_bw[bw]["occurrences"] for bw in canonical]
    colors = [STAGE_COLORS[by_bw[bw]["stage"]] for bw in canonical]

    bars = ax1.bar(range(len(canonical)), counts, color=colors,
                   edgecolor="black", linewidth=0.6)
    ax1.set_xticks(range(len(canonical)))
    ax1.set_xticklabels(labels, fontsize=12)
    ax1.set_ylabel(ar("بسامد در قرآن"))
    ax1.set_title(ar("بسامد به تفکیک ریشه"))
    for b, c in zip(bars, counts):
        ax1.text(b.get_x() + b.get_width() / 2, c + 1.5, str(c),
                 ha="center", va="bottom", fontsize=9)

    # Stage totals (right panel)
    stage_totals: dict[int, int] = defaultdict(int)
    for r in rows:
        stage_totals[r["stage"]] += r["occurrences"]
    stages = sorted(stage_totals.keys())
    bars2 = ax2.bar(stages, [stage_totals[s] for s in stages],
                    color=[STAGE_COLORS[s] for s in stages],
                    edgecolor="black", linewidth=0.6)
    ax2.set_xticks(stages)
    ax2.set_xticklabels([ar(f"مرحله {FA_NUM[s]}") + "\n" + ar(STAGE_SHORT_FA[s])
                         for s in stages], fontsize=9)
    ax2.set_ylabel(ar("بسامد کل"))
    ax2.set_title(ar("مجموع به تفکیک مرحله"))
    for b, s in zip(bars2, stages):
        ax2.text(b.get_x() + b.get_width() / 2,
                 stage_totals[s] + 2, str(stage_totals[s]),
                 ha="center", va="bottom", fontsize=10, fontweight="bold")

    total_hits = sum(by_bw[bw]["occurrences"] for bw in canonical)
    fig.suptitle(ar(
        "بسامد واژگانی طیف در پیکرهٔ قرآن "
        f"({_to_persian_digits(total_hits)} بسامد در "
        f"{_to_persian_digits(len(SPECTRUM))} ریشهٔ کانونی)"),
        fontsize=11)
    fig.tight_layout()

    out = FIG_DIR / "fig2_frequency_by_stage.pdf"
    plt.savefig(out)
    plt.savefig(out.with_suffix(".png"))
    plt.close()
    print(f"Wrote {out}")


def fig3_meccan_medinan(rows: list[dict]) -> None:
    """Stacked bar: Meccan vs Medinan distribution per root."""
    fig, ax = plt.subplots(figsize=(11, 5))

    canonical = [bw for bw in CANONICAL_ORDER if bw in {r["root_bw"] for r in rows}]
    by_bw = {r["root_bw"]: r for r in rows}
    surface_by_bw = {r.bw: r.display() for r in SPECTRUM}
    labels = [ar(surface_by_bw[bw]) for bw in canonical]
    meccan = [by_bw[bw]["meccan_hits"] for bw in canonical]
    medinan = [by_bw[bw]["medinan_hits"] for bw in canonical]

    x = range(len(canonical))
    ax.bar(x, meccan, color="#8C7853", edgecolor="black",
           linewidth=0.5, label=ar("مکی"))
    ax.bar(x, medinan, bottom=meccan, color="#2E86AB",
           edgecolor="black", linewidth=0.5, label=ar("مدنی"))

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=12)
    ax.set_ylabel(ar("بسامد"))
    ax.set_title(ar("توزیع واژگان طیف میان پیکرهٔ مکی و مدنی"))
    ax.legend(loc="upper left")

    # Annotate proportions for the small-n suras
    for xi, bw in enumerate(canonical):
        rec = by_bw[bw]
        total = rec["meccan_hits"] + rec["medinan_hits"]
        if total > 0:
            ax.text(xi, total + 1.5,
                    f"{rec['meccan_hits']}/{rec['medinan_hits']}",
                    ha="center", va="bottom", fontsize=8, color="gray")

    fig.tight_layout()
    out = FIG_DIR / "fig3_meccan_medinan.pdf"
    plt.savefig(out)
    plt.savefig(out.with_suffix(".png"))
    plt.close()
    print(f"Wrote {out}")


def fig4_cooccurrence(window: int = 0) -> None:
    """Build a co-occurrence graph: edge between two roots if they
    appear in the same aya (window=0) or within ±window ayat."""
    # Read master concordance
    aya_to_roots: dict[tuple[int, int], set[str]] = defaultdict(set)
    with (CONC_DIR / "master_concordance.csv").open("r", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            aya_to_roots[(int(row["sura"]), int(row["aya"]))].add(row["root_bw"])

    # Build edge weights (only among the 10 core spectrum roots)
    core = [r.bw for r in SPECTRUM]
    core_set = set(core)
    edges: Counter = Counter()
    for (sura, aya), roots in aya_to_roots.items():
        present = sorted(roots & core_set)
        for i, a in enumerate(present):
            for b in present[i + 1:]:
                edges[(a, b)] += 1

    G = nx.Graph()
    for r in SPECTRUM:
        G.add_node(r.bw, arabic=r.arabic, stage=r.stage)
    for (a, b), w in edges.items():
        G.add_edge(a, b, weight=w)

    fig, ax = plt.subplots(figsize=(12, 9))
    pos = nx.spring_layout(G, weight="weight", seed=42, k=1.5, iterations=300)

    # Draw edges with thickness ∝ weight
    if G.number_of_edges() > 0:
        max_w = max(d["weight"] for _, _, d in G.edges(data=True))
        for u, v, d in G.edges(data=True):
            ax.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]],
                    color="gray", alpha=0.3 + 0.7 * (d["weight"] / max_w),
                    linewidth=0.6 + 3.0 * (d["weight"] / max_w), zorder=1)
            mx = (pos[u][0] + pos[v][0]) / 2
            my = (pos[u][1] + pos[v][1]) / 2
            ax.text(mx, my, str(d["weight"]), fontsize=7,
                    ha="center", va="center", color="dimgray",
                    bbox=dict(boxstyle="round,pad=0.15", fc="white",
                              ec="none", alpha=0.85))

    # Nodes
    for r in SPECTRUM:
        x, y = pos[r.bw]
        ax.scatter(x, y, s=900, color=STAGE_COLORS[r.stage],
                   edgecolor="black", linewidth=0.8, zorder=2)
        ax.text(x, y, ar(r.display()), ha="center", va="center",
                fontsize=10, fontweight="bold", color="white", zorder=3)

    # Legend (Persian stage labels) — iterate over every stage actually
    # present in SPECTRUM so the legend stays in sync if the spectrum is
    # extended.
    for st in sorted(set(r.stage for r in SPECTRUM)):
        ax.scatter([], [], color=STAGE_COLORS[st], s=120, edgecolor="black",
                   linewidth=0.5, label=ar(STAGE_LABELS[st]))
    ax.legend(loc="lower right", fontsize=8)

    ax.axis("off")
    ax.set_title(ar(
        f"شبکه هم‌رخدادگیری آیه‌ای {_to_persian_digits(len(SPECTRUM))} ریشه کانونی") + "\n"
                 + ar("وزن یال = تعداد آیات مشترک"),
                 fontsize=11)

    out = FIG_DIR / "fig4_cooccurrence.pdf"
    plt.savefig(out)
    plt.savefig(out.with_suffix(".png"))
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
