"""Generate the four publication figures (Persian-localised variant).

    figures_fa/fig1_continuum.{pdf,png}            six-stage anger spectrum (RTL flow)
    figures_fa/fig2_frequency_by_stage.{pdf,png}   per-root and per-stage frequencies
    figures_fa/fig3_meccan_medinan.{pdf,png}       Meccan/Medinan distribution
    figures_fa/fig4_cooccurrence.{pdf,png}         aya-level co-occurrence network

Design goals: publication-grade aesthetics for an Iranian Qur'anic-studies
journal. RTL flow respected (Stage 1 on the right, Stage 6 on the left in
fig 1). Persian numerals (۰-۹) on all tick labels and frequency annotations.
Color-blind-safe viridis-derived palette for the six stages, Okabe-Ito for
categorical fills. Vazirmatn for Persian UI text, Amiri for Arabic root
glyphs (both bundled in paper/fonts/).
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
from matplotlib import font_manager as fm  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402
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


# --------------------------------------------------------------------- #
#  Font registration                                                    #
# --------------------------------------------------------------------- #
FONT_DIR = ROOT_DIR / "paper" / "fonts"

# Register bundled fonts so matplotlib can find them by family name.
for _f in ("vazirmatn-regular.ttf", "vazirmatn-bold.ttf",
           "vazirmatn-light.ttf", "amiri-regular.ttf", "amiri-bold.ttf"):
    _path = FONT_DIR / _f
    if _path.exists():
        fm.fontManager.addfont(str(_path))

FP_FA = fm.FontProperties(fname=str(FONT_DIR / "vazirmatn-regular.ttf"))
FP_FA_BOLD = fm.FontProperties(fname=str(FONT_DIR / "vazirmatn-bold.ttf"))
FP_FA_LIGHT = fm.FontProperties(fname=str(FONT_DIR / "vazirmatn-light.ttf"))
FP_AR = fm.FontProperties(fname=str(FONT_DIR / "amiri-regular.ttf"))
FP_AR_BOLD = fm.FontProperties(fname=str(FONT_DIR / "amiri-bold.ttf"))


# --------------------------------------------------------------------- #
#  Helpers                                                              #
# --------------------------------------------------------------------- #
def ar(text: str) -> str:
    """Reshape and bidi-reorder an Arabic/Persian string for matplotlib."""
    if not text:
        return text
    return get_display(arabic_reshaper.reshape(text))


_PERSIAN_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")


def fa_num(value) -> str:
    """Render any numeric value with Persian digits and Persian decimal mark."""
    s = str(value)
    return s.translate(_PERSIAN_DIGITS).replace(".", "٫")


FA_STAGE_NUM = {1: "۱", 2: "۲", 3: "۳", 4: "۴", 5: "۵", 6: "۶"}


# --------------------------------------------------------------------- #
#  Style                                                                #
# --------------------------------------------------------------------- #
plt.rcParams.update({
    "font.family": ["Vazirmatn", "Tahoma", "DejaVu Sans"],
    "font.size": 9.5,
    "axes.labelsize": 10,
    "axes.titlesize": 11,
    "legend.fontsize": 9,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.edgecolor": "#444444",
    "axes.linewidth": 0.8,
    "xtick.color": "#444444",
    "ytick.color": "#444444",
    "xtick.major.size": 3,
    "ytick.major.size": 3,
    "figure.dpi": 150,
    "savefig.bbox": "tight",
    "savefig.dpi": 300,
    "pdf.fonttype": 42,
})

# Six-stage palette: viridis-anchored, monotonic in lightness, colour-blind
# safe (CVD-checked with Color Oracle). Stage 1 is the lightest cool tone,
# Stage 6 the warmest – mirroring the semantic intensity gradient.
STAGE_COLORS = {
    1: "#A8D8B9",  # pale green-cyan — light displeasure
    2: "#5BA9C1",  # muted teal
    3: "#3B6C9B",  # mid blue
    4: "#9E5F2E",  # ochre — active anger
    5: "#7C1D3F",  # deep wine — compressed rage
    6: "#3A1F47",  # very dark plum — behavioural outcome
}

# Persian short labels per stage (no "مرحله N — " prefix)
STAGE_SHORT_FA = {
    1: "تضجر و ناخشنودی",
    2: "فشار درونی",
    3: "انزجار ارزیابانه",
    4: "خشم فعال",
    5: "خشم متراکم",
    6: "پیامد رفتاری",
}

CANONICAL_ORDER = [r.bw for r in SPECTRUM]


# --------------------------------------------------------------------- #
#  Common helpers                                                       #
# --------------------------------------------------------------------- #
def style_axes(ax, *, ygrid: bool = True) -> None:
    """Apply consistent axis styling: only left+bottom spines, soft grid."""
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color("#666666")
        ax.spines[side].set_linewidth(0.7)
    if ygrid:
        ax.yaxis.grid(True, color="#DDDDDD", linewidth=0.6, zorder=0)
        ax.set_axisbelow(True)


def set_fa_yaxis(ax) -> None:
    """Format y-axis tick labels with Persian digits using Vazirmatn."""
    labels = []
    for t in ax.get_yticks():
        if abs(t - int(t)) < 1e-9:
            labels.append(fa_num(int(t)))
        else:
            labels.append(fa_num(f"{t:.2f}"))
    ax.set_yticks(ax.get_yticks())
    ax.set_yticklabels(labels, fontproperties=FP_FA, fontsize=9)


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


# --------------------------------------------------------------------- #
#  Figure 1 — Six-stage continuum (RTL flow)                            #
# --------------------------------------------------------------------- #
def fig1_continuum(rows: list[dict]) -> None:
    """RTL six-stage continuum. Stage 1 on the right, Stage 6 on the left."""
    # Reverse spectrum order for Persian RTL reading: position 1 on the
    # right edge of the figure corresponds to Stage 1 (mildest); position N
    # on the left edge corresponds to Stage 6 (severe behavioural outcome).
    n = len(SPECTRUM)
    spectrum_rtl = list(reversed(SPECTRUM))
    width = n + 1

    fig, ax = plt.subplots(figsize=(13.5, 5.4))
    ax.set_xlim(0, width)
    ax.set_ylim(0, 6.4)
    ax.axis("off")

    # Group consecutive same-stage roots in RTL order so the band spans the
    # correct x-range.
    by_stage_xs: dict[int, list[int]] = {}
    for i, r in enumerate(spectrum_rtl, start=1):
        by_stage_xs.setdefault(r.stage, []).append(i)

    # Stage bands (background)
    for st, xs_in_stage in sorted(by_stage_xs.items()):
        x0 = min(xs_in_stage) - 0.5
        x1 = max(xs_in_stage) + 0.5
        ax.axhspan(1.0, 4.5, xmin=(x0 / width), xmax=(x1 / width),
                   facecolor=STAGE_COLORS[st], alpha=0.10, zorder=0)
        # Soft divider between bands
        ax.plot([x0, x0], [1.0, 4.5], color="white", lw=2, zorder=0)

    # Stage headers
    for st, xs_in_stage in sorted(by_stage_xs.items()):
        cx = (min(xs_in_stage) - 0.5 + max(xs_in_stage) + 0.5) / 2
        ax.text(cx, 5.55, ar(f"مرحلهٔ {FA_STAGE_NUM[st]}"),
                ha="center", va="center", fontsize=11.5,
                fontproperties=FP_FA_BOLD, color=STAGE_COLORS[st])
        ax.text(cx, 5.05, ar(STAGE_SHORT_FA[st]),
                ha="center", va="center", fontsize=9,
                fontproperties=FP_FA, color="#333333")

    by_bw = {r["root_bw"]: r for r in rows}

    # Nodes in RTL order
    for i, root in enumerate(spectrum_rtl, start=1):
        rec = by_bw.get(root.bw)
        if rec is None:
            continue
        st = root.stage
        # Bubble radius modulated by sqrt(count) for visual mapping; cap
        # extremes so 96 (baghy) does not overwhelm 1 (ḥard).
        size = 320 + 60 * (rec["occurrences"] ** 0.55)
        ax.scatter(i, 2.85, s=size, color=STAGE_COLORS[st],
                   edgecolor="white", linewidth=1.4, zorder=3)
        # Arabic root inside the bubble (Amiri, white)
        ax.text(i, 2.85, ar(root.display()), ha="center", va="center",
                fontsize=12, fontweight="bold",
                fontproperties=FP_AR_BOLD, color="white", zorder=4)
        # Persian count "n = NN" beneath
        ax.text(i, 1.80, ar(f"n = {fa_num(rec['occurrences'])}"),
                ha="center", va="center",
                fontsize=8.5, fontproperties=FP_FA, color="#222222", zorder=4)
        # Latin-script transliteration (small, italic)
        ax.text(i, 1.40, f"({root.translit})", ha="center", va="center",
                fontsize=7.5, color="#777777", zorder=4, style="italic")

    # RTL arrows: in spectrum_rtl, increasing intensity goes from right to
    # left (toward higher x indices). Draw arrows that point leftward —
    # from higher index toward (higher index + 1).
    for i in range(1, n):
        ax.annotate("", xy=(i + 1 - 0.32, 2.85), xytext=(i + 0.32, 2.85),
                    arrowprops=dict(arrowstyle="-|>", color="#888888",
                                    lw=1.0, alpha=0.65,
                                    mutation_scale=11), zorder=2)

    # Axis label: arrow points LEFT (RTL flow). Draw the arrow as a
    # graphical annotation so the figure does not depend on font-level
    # support for U+2190 / U+27F5 (which Vazirmatn lacks).
    ax.text(width / 2 + 1.4, 0.55,
            ar("افزایش شدتِ کنش"),
            ha="center", va="center",
            fontsize=11.5, fontproperties=FP_FA_BOLD, color="#222222")
    ax.annotate("",
                xy=(width / 2 - 0.6, 0.55),
                xytext=(width / 2 + 0.2, 0.55),
                arrowprops=dict(arrowstyle="-|>", color="#222222",
                                lw=1.8, mutation_scale=18))

    # Title (two lines, Persian)
    fig.text(0.5, 0.97,
             ar("پیوستارِ شش‌مرحله‌ایِ شدتِ خشم در قرآن کریم"),
             ha="center", va="top",
             fontsize=13, fontproperties=FP_FA_BOLD, color="#1A1A1A")
    fig.text(0.5, 0.925,
             ar("از آزردگیِ درونی تا عصیانِ رفتاری — اندازهٔ گره متناسب با ریشهٔ دومِ بسامد در پیکرهٔ قرآن کریم"),
             ha="center", va="top",
             fontsize=9.5, fontproperties=FP_FA, color="#555555")

    plt.subplots_adjust(top=0.86, bottom=0.05, left=0.02, right=0.98)
    out = FIG_DIR / "fig1_continuum.pdf"
    plt.savefig(out)
    plt.savefig(out.with_suffix(".png"), dpi=200)
    plt.close()
    print(f"Wrote {out}")


# --------------------------------------------------------------------- #
#  Figure 2 — Frequency by root and by stage                            #
# --------------------------------------------------------------------- #
def fig2_frequency_by_stage(rows: list[dict]) -> None:
    """Two-panel bar chart. Panel A: per-root counts. Panel B: per-stage."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.5, 5.2),
                                   gridspec_kw=dict(width_ratios=[1.85, 1]))

    canonical = [bw for bw in CANONICAL_ORDER if bw in {r["root_bw"] for r in rows}]
    by_bw = {r["root_bw"]: r for r in rows}
    surface_by_bw = {r.bw: r.display() for r in SPECTRUM}

    labels = [ar(surface_by_bw[bw]) for bw in canonical]
    counts = [by_bw[bw]["occurrences"] for bw in canonical]
    colors = [STAGE_COLORS[by_bw[bw]["stage"]] for bw in canonical]

    # --- Panel A: per-root ----------------------------------------------
    bars = ax1.bar(range(len(canonical)), counts, color=colors,
                   edgecolor="white", linewidth=0.8, zorder=2)
    ax1.set_xticks(range(len(canonical)))
    ax1.set_xticklabels(labels, fontsize=12,
                        fontproperties=FP_AR_BOLD)
    ax1.set_ylabel(ar("بسامد در پیکرهٔ قرآن"),
                   fontproperties=FP_FA, fontsize=10.5)
    ax1.set_title(ar("الف) بسامد به تفکیکِ ریشه"),
                  fontproperties=FP_FA_BOLD, fontsize=11.5, pad=10)
    style_axes(ax1)
    for b, c in zip(bars, counts):
        ax1.text(b.get_x() + b.get_width() / 2, c + max(counts) * 0.02,
                 fa_num(c), ha="center", va="bottom",
                 fontsize=9, fontproperties=FP_FA, color="#222222")
    ax1.set_ylim(0, max(counts) * 1.18)
    set_fa_yaxis(ax1)

    # --- Panel B: per-stage totals -------------------------------------
    stage_totals: dict[int, int] = defaultdict(int)
    for r in rows:
        stage_totals[r["stage"]] += r["occurrences"]
    stages = sorted(stage_totals.keys())
    bars2 = ax2.bar(stages, [stage_totals[s] for s in stages],
                    color=[STAGE_COLORS[s] for s in stages],
                    edgecolor="white", linewidth=0.8, zorder=2)
    ax2.set_xticks(stages)
    # Use only the stage number on the x-axis to avoid label collision;
    # the full label is shown beneath each bar via a secondary annotation.
    stage_tick_labels = [ar(f"مرحلهٔ {FA_STAGE_NUM[s]}") for s in stages]
    ax2.set_xticklabels(stage_tick_labels, fontsize=10,
                        fontproperties=FP_FA_BOLD)
    ax2.set_ylabel(ar("بسامد کل"), fontproperties=FP_FA, fontsize=10.5)
    ax2.set_title(ar("ب) مجموع به تفکیکِ مرحله"),
                  fontproperties=FP_FA_BOLD, fontsize=11.5, pad=10)
    style_axes(ax2)
    max_total = max(stage_totals.values())
    for b, s in zip(bars2, stages):
        ax2.text(b.get_x() + b.get_width() / 2,
                 stage_totals[s] + max_total * 0.015,
                 fa_num(stage_totals[s]),
                 ha="center", va="bottom",
                 fontsize=10, fontproperties=FP_FA_BOLD, color="#222222")
    ax2.set_ylim(0, max_total * 1.20)
    set_fa_yaxis(ax2)

    # Statistical annotation (Persian, embedded inside Panel B):
    # χ²(5) = 227.15, p < 0.001 asymptotic; permutation p = 0.24
    # We spell out «کای-دوی» rather than the Greek χ² so the glyph stays
    # within Vazirmatn's coverage.
    stat_text = (ar("آزمونِ کای-دوی مرحله‌ای:") + "\n" +
                 ar("کای-دو(۵) = ۲۲۷٫۱۵،  p < ۰٫۰۰۱  (مجانبی)") + "\n" +
                 ar("p = ۰٫۲۴  (آزمونِ جایگشتیِ حافظِ حاشیه‌ها)"))
    ax2.text(0.02, 0.98, stat_text, transform=ax2.transAxes,
             ha="left", va="top",
             fontsize=8, fontproperties=FP_FA, color="#222222",
             bbox=dict(boxstyle="round,pad=0.5", facecolor="#FAFAFA",
                       edgecolor="#BBBBBB", linewidth=0.6, alpha=0.92))

    total_hits = sum(by_bw[bw]["occurrences"] for bw in canonical)
    fig.suptitle(
        ar("بسامدِ واژگانیِ طیفِ خشم در پیکرهٔ قرآن — "
           f"{fa_num(total_hits)} بسامد در {fa_num(len(SPECTRUM))} ریشهٔ کانونی"),
        fontproperties=FP_FA_BOLD, fontsize=12.5, y=0.99)
    fig.tight_layout(rect=[0, 0, 1, 0.94])

    out = FIG_DIR / "fig2_frequency_by_stage.pdf"
    plt.savefig(out)
    plt.savefig(out.with_suffix(".png"), dpi=200)
    plt.close()
    print(f"Wrote {out}")


# --------------------------------------------------------------------- #
#  Figure 3 — Meccan / Medinan distribution                             #
# --------------------------------------------------------------------- #
def fig3_meccan_medinan(rows: list[dict]) -> None:
    """Stacked bar: Meccan vs Medinan per root, with baseline line."""
    fig, ax = plt.subplots(figsize=(13.5, 5.4))

    canonical = [bw for bw in CANONICAL_ORDER if bw in {r["root_bw"] for r in rows}]
    by_bw = {r["root_bw"]: r for r in rows}
    surface_by_bw = {r.bw: r.display() for r in SPECTRUM}
    labels = [ar(surface_by_bw[bw]) for bw in canonical]
    meccan = [by_bw[bw]["meccan_hits"] for bw in canonical]
    medinan = [by_bw[bw]["medinan_hits"] for bw in canonical]
    totals = [m + d for m, d in zip(meccan, medinan)]

    x = list(range(len(canonical)))
    # Okabe-Ito palette: sand + sky-blue
    mec_color = "#D6A35C"      # warm sand (Meccan)
    med_color = "#1F77B4"      # blue (Medinan)
    ax.bar(x, meccan, color=mec_color, edgecolor="white",
           linewidth=0.7, label=ar("مکی"), zorder=2)
    ax.bar(x, medinan, bottom=meccan, color=med_color, edgecolor="white",
           linewidth=0.7, label=ar("مدنی"), zorder=2)

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=13, fontproperties=FP_AR_BOLD)
    ax.set_ylabel(ar("بسامد در پیکره"),
                  fontproperties=FP_FA, fontsize=10.5)
    style_axes(ax)

    max_total = max(totals) if totals else 1
    # Annotate Meccan/Medinan ratios on each bar (Persian digits)
    for xi, (m, d, t) in enumerate(zip(meccan, medinan, totals)):
        if t > 0:
            ax.text(xi, t + max_total * 0.015,
                    f"{fa_num(m)}/{fa_num(d)}",
                    ha="center", va="bottom",
                    fontsize=8.5, fontproperties=FP_FA, color="#555555")
    ax.set_ylim(0, max_total * 1.20)

    # Baseline reference: Meccan rate ≈ 74% of total ayat.
    # Show as horizontal dashed line on a secondary y-axis (rate-scale)
    # for context. We overlay a faint band rather than a separate axis to
    # keep the figure simple.
    leg = ax.legend(loc="upper right", frameon=True,
                    facecolor="white", edgecolor="#BBBBBB", framealpha=0.95,
                    prop=FP_FA, fontsize=10)
    leg.get_frame().set_linewidth(0.7)

    # Statistical annotation (Persian): sakhaṭ binomial result.
    # Subscript ₀ and ∈ are outside Vazirmatn's coverage — spell them out.
    stat_text = (ar("آزمونِ دوجمله‌ایِ سَخَط (۰/۴):  p خام = ۰٫۰۰۴۶") + "\n" +
                 ar("(فرضِ صفر: نرخِ مکی = ۰٫۷۴؛  p تعدیل‌شدهٔ Holm = ۰٫۰۵)") + "\n" +
                 ar("حساسیتِ پایه ۰٫۷۰–۰٫۷۸:  p در بازهٔ ۰٫۰۰۲ تا ۰٫۰۰۸"))
    ax.text(0.02, 0.97, stat_text, transform=ax.transAxes,
            ha="left", va="top",
            fontsize=8.5, fontproperties=FP_FA, color="#222222",
            bbox=dict(boxstyle="round,pad=0.45", facecolor="#FAFAFA",
                      edgecolor="#BBBBBB", linewidth=0.6, alpha=0.95))

    ax.set_title(
        ar("توزیعِ واژگانِ طیفِ خشم میانِ پیکرهٔ مکی و مدنی"),
        fontproperties=FP_FA_BOLD, fontsize=12.5, pad=12)
    set_fa_yaxis(ax)

    fig.tight_layout()
    out = FIG_DIR / "fig3_meccan_medinan.pdf"
    plt.savefig(out)
    plt.savefig(out.with_suffix(".png"), dpi=200)
    plt.close()
    print(f"Wrote {out}")


# --------------------------------------------------------------------- #
#  Figure 4 — Aya-level co-occurrence network                           #
# --------------------------------------------------------------------- #
def fig4_cooccurrence(window: int = 0) -> None:
    """Force-directed co-occurrence graph of the 14 core spectrum roots."""
    aya_to_roots: dict[tuple[int, int], set[str]] = defaultdict(set)
    with (CONC_DIR / "master_concordance.csv").open("r", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            aya_to_roots[(int(row["sura"]), int(row["aya"]))].add(row["root_bw"])

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
              else [1.05 - 2.1 * i / (len(isolated) - 1)
                    for i in range(len(isolated))])
        for node, y in zip(isolated, ys):
            pos[node] = (1.68, y * 0.65)

    fig, ax = plt.subplots(figsize=(13.5, 8.5))

    # Draw edges
    if G.number_of_edges() > 0:
        max_w = max(d["weight"] for _, _, d in G.edges(data=True))
        for u, v, d in G.edges(data=True):
            alpha = 0.32 + 0.6 * (d["weight"] / max_w)
            lw = 0.7 + 4.0 * (d["weight"] / max_w)
            ax.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]],
                    color="#888888", alpha=alpha, linewidth=lw,
                    solid_capstyle="round", zorder=1)
            # Edge-weight label
            mx = (pos[u][0] + pos[v][0]) / 2
            my = (pos[u][1] + pos[v][1]) / 2
            ax.text(mx, my, fa_num(d["weight"]),
                    fontsize=7.5, fontproperties=FP_FA,
                    ha="center", va="center", color="#444444",
                    bbox=dict(boxstyle="round,pad=0.18",
                              facecolor="white", edgecolor="#CCCCCC",
                              linewidth=0.5, alpha=0.92), zorder=1.5)

    # Draw nodes — labels in Amiri (Arabic), white on coloured fill.
    for r in SPECTRUM:
        x, y = pos[r.bw]
        ax.scatter(x, y, s=1100, color=STAGE_COLORS[r.stage],
                   edgecolor="white", linewidth=1.6, zorder=2)
        ax.text(x, y, ar(r.display()), ha="center", va="center",
                fontsize=12, fontproperties=FP_AR_BOLD,
                color="white", zorder=3)

    # Sidebar for isolated nodes
    if isolated:
        ax.text(1.68, 1.07, ar("بدونِ هم‌رخدادگیریِ آیه‌ای"),
                ha="center", va="bottom",
                fontsize=9.5, fontproperties=FP_FA_BOLD,
                style="italic", color="#555555")
        ax.plot([1.40, 1.40], [-0.95, 0.95],
                color="#BBBBBB", linestyle="--", linewidth=0.7, zorder=0)

    # Legend (Persian stage labels)
    for st in sorted(set(r.stage for r in SPECTRUM)):
        ax.scatter([], [], color=STAGE_COLORS[st], s=150, edgecolor="white",
                   linewidth=0.6, label=ar(STAGE_LABELS[st]))
    leg = ax.legend(loc="lower left", frameon=True,
                    facecolor="white", edgecolor="#BBBBBB",
                    framealpha=0.95, prop=FP_FA, fontsize=8.5,
                    title=ar("مراحلِ طیف"),
                    title_fontproperties=FP_FA_BOLD)
    leg.get_frame().set_linewidth(0.7)
    leg.get_title().set_fontsize(9.5)

    ax.axis("off")
    n_edges = G.number_of_edges()
    n_co = sum(d["weight"] for _, _, d in G.edges(data=True))
    ax.set_title(
        ar(f"شبکهٔ هم‌رخدادگیریِ آیه‌ایِ {fa_num(len(SPECTRUM))} ریشهٔ کانونیِ طیف") + "\n" +
        ar(f"وزنِ یال = شمارِ آیاتِ مشترک   ·   {fa_num(n_edges)} یال "
           f"·   {fa_num(n_co)} هم‌رخدادگیری"),
        fontproperties=FP_FA_BOLD, fontsize=12.5, pad=10)

    fig.tight_layout()
    out = FIG_DIR / "fig4_cooccurrence.pdf"
    plt.savefig(out)
    plt.savefig(out.with_suffix(".png"), dpi=200)
    plt.close()
    print(f"Wrote {out}")
    print(f"Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges, "
          f"total co-occurrences = {n_co}")


if __name__ == "__main__":
    rows = load_summary()
    fig1_continuum(rows)
    fig2_frequency_by_stage(rows)
    fig3_meccan_medinan(rows)
    fig4_cooccurrence()
