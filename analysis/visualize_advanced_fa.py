"""Generate the advanced (research-grade) figures — Persian-localised.

    figures_fa/fig5_morphology_stack.{pdf,png}    Per-root POS profile
    figures_fa/fig6_metaphor_diagram.{pdf,png}    Container-under-pressure metaphor
    figures_fa/fig7_centrality.{pdf,png}          Three centrality measures

All Persian/Arabic strings are reshaped + bidi-reordered. Persian numerals
are used in every annotation and tick label. Vazirmatn for Persian UI text,
Amiri for Arabic root glyphs.
"""
from __future__ import annotations

import csv
import io
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager as fm  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Rectangle  # noqa: E402
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
def ar(s: str) -> str:
    return get_display(arabic_reshaper.reshape(s)) if s else s


_PERSIAN_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")


def fa_num(value) -> str:
    s = str(value)
    return s.translate(_PERSIAN_DIGITS).replace(".", "٫")


FA_STAGE_NUM = {1: "۱", 2: "۲", 3: "۳", 4: "۴", 5: "۵", 6: "۶"}


plt.rcParams.update({
    "font.family": ["Vazirmatn", "Tahoma", "DejaVu Sans"],
    "font.size": 11,
    "axes.labelsize": 12,
    "axes.titlesize": 12,
    "legend.fontsize": 10,
    "xtick.labelsize": 11,
    "ytick.labelsize": 11,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.edgecolor": "#444444",
    "axes.linewidth": 0.8,
    "xtick.color": "#444444",
    "ytick.color": "#444444",
    "figure.dpi": 150,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.08,
    "savefig.dpi": 300,
    "pdf.fonttype": 42,
})

# Synced with visualize_spectrum_fa.py
STAGE_COLORS = {
    1: "#A8D8B9",
    2: "#5BA9C1",
    3: "#3B6C9B",
    4: "#9E5F2E",
    5: "#7C1D3F",
    6: "#3A1F47",
}

# Okabe-Ito categorical palette for morphology (CVD-safe).
MORPH_COLORS = {
    "verb":       "#0072B2",  # blue
    "noun":       "#E69F00",  # orange
    "adjective":  "#009E73",  # bluish-green
    "participle": "#CC79A7",  # reddish-purple
    "other":      "#999999",  # neutral grey
}

CANONICAL_ORDER = [r.bw for r in SPECTRUM]


def style_axes(ax, *, ygrid: bool = True) -> None:
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color("#666666")
        ax.spines[side].set_linewidth(0.7)
    if ygrid:
        ax.yaxis.grid(True, color="#DDDDDD", linewidth=0.6, zorder=0)
        ax.set_axisbelow(True)


def set_fa_yaxis(ax) -> None:
    labels = []
    for t in ax.get_yticks():
        if abs(t - int(t)) < 1e-9:
            labels.append(fa_num(int(t)))
        else:
            labels.append(fa_num(f"{t:.2f}"))
    ax.set_yticks(ax.get_yticks())
    ax.set_yticklabels(labels, fontproperties=FP_FA, fontsize=11)


# --------------------------------------------------------------------- #
#  Figure 5 — Morphological breakdown                                   #
# --------------------------------------------------------------------- #
def fig5_morphology() -> None:
    rows = []
    with (CONC_DIR / "morphology_by_root.csv").open("r", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            r["stage"] = int(r["stage"])
            for k in ("verb", "noun", "adjective", "participle", "other", "total"):
                r[k] = int(r[k])
            rows.append(r)

    core_bw = [r.bw for r in SPECTRUM]
    rows = [r for r in rows if r["root_bw"] in core_bw]
    surface_by_bw = {r.bw: r.display() for r in SPECTRUM}

    canonical = [bw for bw in CANONICAL_ORDER if bw in {r["root_bw"] for r in rows}]
    by_bw = {r["root_bw"]: r for r in rows}

    fig, ax = plt.subplots(figsize=(13.5, 5.6))
    labels = [ar(surface_by_bw[bw]) for bw in canonical]
    x = list(range(len(canonical)))
    bottoms = [0] * len(canonical)
    categories = [
        ("verb",       ar("فعل"),               MORPH_COLORS["verb"]),
        ("noun",       ar("اسم"),               MORPH_COLORS["noun"]),
        ("adjective",  ar("صفت"),               MORPH_COLORS["adjective"]),
        ("participle", ar("اسمِ فاعل/مفعول"),    MORPH_COLORS["participle"]),
        ("other",      ar("سایر"),              MORPH_COLORS["other"]),
    ]
    for key, label, color in categories:
        vals = [by_bw[bw][key] for bw in canonical]
        ax.bar(x, vals, bottom=bottoms, label=label,
               color=color, edgecolor="white", linewidth=0.6, zorder=2)
        for xi, (b, v) in enumerate(zip(bottoms, vals)):
            if v >= 4:
                # Choose text color by luminance of the underlying slice.
                ax.text(xi, b + v / 2, fa_num(v),
                        ha="center", va="center",
                        fontsize=10, fontproperties=FP_FA_BOLD,
                        color="white" if color != MORPH_COLORS["other"]
                        else "#222222")
        bottoms = [bo + v for bo, v in zip(bottoms, vals)]

    # Totals above
    for xi, bw in enumerate(canonical):
        total = by_bw[bw]["total"]
        ax.text(xi, total + 2, ar(f"n = {fa_num(total)}"),
                ha="center", va="bottom",
                fontsize=10.5, fontproperties=FP_FA_BOLD, color="#222222")

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=15, fontproperties=FP_AR_BOLD)
    ax.set_ylabel(ar("شمارِ بسامد"), fontproperties=FP_FA, fontsize=12)
    max_total = max(by_bw[bw]["total"] for bw in canonical)
    ax.set_ylim(0, max_total * 1.28)
    style_axes(ax)
    set_fa_yaxis(ax)

    # Figure title and verbal/nominal trend live in the manuscript caption.

    # Legend at the top — bigger Persian labels.
    leg = ax.legend(loc="upper center", ncol=5, fontsize=11,
                    frameon=False, prop=FP_FA,
                    bbox_to_anchor=(0.5, 1.06))
    for txt in leg.get_texts():
        txt.set_fontproperties(FP_FA)

    fig.tight_layout()
    out = FIG_DIR / "fig5_morphology_stack.pdf"
    plt.savefig(out)
    plt.savefig(out.with_suffix(".png"), dpi=200)
    plt.close()
    print(f"Wrote {out}")


# --------------------------------------------------------------------- #
#  Figure 6 — Conceptual-metaphor diagram                               #
# --------------------------------------------------------------------- #
def fig6_metaphor() -> None:
    fig, ax = plt.subplots(figsize=(13.5, 7.6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    ax.axis("off")

    # Title
    ax.text(6, 8.4, ar("خشم، ظرفی است تحت فشار"),
            ha="center", va="center",
            fontsize=15, fontproperties=FP_FA_BOLD, color="#1A1A1A")
    ax.text(6, 7.85,
            ar("استعارهٔ مفهومیِ Lakoff & Kövecses (۱۹۸۷) — "
               "اعمال‌شده بر سه‌گانهٔ غَیظ–کَظم–تَمَیُّز در قرآن کریم"),
            ha="center", va="center",
            fontsize=10, fontproperties=FP_FA, color="#666666",
            style="italic")

    # Three vessel states across the bottom row.
    # The Persian RTL convention reads from right to left, so progression
    # of pressure should also flow right→left. We place Stage 4 (open vessel)
    # on the RIGHT, then Stage 5α (sealed) in the MIDDLE, then Stage 5β
    # (rupturing) on the LEFT — escalation moves leftward.
    vessel_states = [
        # (cx, color, fluid_height_ratio, top_label, bottom_label, ar_label, lid, crack)
        (10.0, "#FFC857", 0.30,
         ar("مرحلهٔ ۴: غَضَب"),
         ar("ظرفِ باز / بدونِ مهر؛") + "\n"
         + ar("هیجان حاضر است اما تحت فشار نیست."),
         "غَضَب", False, False),
        (6.0, "#E76F51", 0.65,
         ar("مرحلهٔ ۵ (الف): غَیظ + کَظم"),
         ar("ظرفِ مهر شده؛ فشار رو به افزایش؛") + "\n"
         + ar("کنشگر با کَظم خود را مهار می‌کند") + "\n"
         + ar("(آل‌عمران ۳:۱۳۴، وَالْکاظِمِينَ الْغَيْظَ).") ,
         "غَيْظ + كَظْم", True, False),
        (2.0, "#9D2933", 0.90,
         ar("مرحلهٔ ۵ (ب): تَمَیُّز"),
         ar("گسستنِ ظرف (مُلک ۶۷:۸):") + "\n"
         + ar("تَكَادُ تَمَيَّزُ مِنَ الْغَيْظِ") + "\n"
         + ar("— خودِ ظرف از هم می‌شکافد."),
         "تَمَيُّز", True, True),
    ]

    vessel_y = 4.3   # vessel centre
    vessel_w = 1.5
    vessel_h = 1.9

    for (cx, col, fh_ratio, top, bot, arabic, lid, crack) in vessel_states:
        # Outer vessel
        ax.add_patch(FancyBboxPatch(
            (cx - vessel_w / 2, vessel_y - vessel_h / 2),
            vessel_w, vessel_h,
            boxstyle="round,pad=0.05,rounding_size=0.18",
            facecolor="white", edgecolor="#1A1A1A", linewidth=1.8,
            zorder=2,
        ))
        # Fluid level
        fluid_h = vessel_h * fh_ratio - 0.1
        ax.add_patch(Rectangle(
            (cx - vessel_w / 2 + 0.08,
             vessel_y - vessel_h / 2 + 0.08),
            vessel_w - 0.16, fluid_h,
            facecolor=col, edgecolor="none", alpha=0.78, zorder=2.5,
        ))
        # Lid
        if lid:
            ax.plot([cx - vessel_w / 2 - 0.05, cx + vessel_w / 2 + 0.05],
                    [vessel_y + vessel_h / 2, vessel_y + vessel_h / 2],
                    color="#1A1A1A", linewidth=2.4, zorder=3,
                    solid_capstyle="round")
            ax.text(cx, vessel_y + vessel_h / 2 + 0.22,
                    ar("(مهر شده)"), ha="center", va="bottom",
                    fontsize=8.5, fontproperties=FP_FA,
                    style="italic", color="#666666")
        # Crack & burst
        if crack:
            ax.plot([cx - 0.55, cx - 0.35, cx - 0.45, cx - 0.25, cx - 0.4],
                    [vessel_y + 0.30, vessel_y + 0.50, vessel_y + 0.45,
                     vessel_y + 0.65, vessel_y + 0.80],
                    color="#1A1A1A", linewidth=1.6, zorder=4)
            ax.text(cx + 0.95, vessel_y + 0.45, ar("انفجار"),
                    fontsize=9, fontproperties=FP_FA_BOLD,
                    color="#7C1D3F", zorder=4)
        # Arabic label under vessel
        ax.text(cx, vessel_y - vessel_h / 2 - 0.35, ar(arabic),
                ha="center", va="top",
                fontsize=14, fontproperties=FP_AR_BOLD, color="#1A1A1A")
        # Stage label above
        ax.text(cx, vessel_y + vessel_h / 2 + 0.65, top,
                ha="center", va="bottom",
                fontsize=10.5, fontproperties=FP_FA_BOLD, color="#1A1A1A")
        # Description well below the Arabic label
        ax.text(cx, vessel_y - vessel_h / 2 - 1.05, bot,
                ha="center", va="top",
                fontsize=8.8, fontproperties=FP_FA, color="#333333")

    # Arrows (RTL flow: right → left)
    arrow_kw = dict(arrowstyle="-|>", color="#888888", lw=2.2,
                    mutation_scale=18,
                    connectionstyle="arc3,rad=0.0")
    ax.annotate("", xy=(6.9, vessel_y), xytext=(9.1, vessel_y),
                arrowprops=arrow_kw, zorder=1)
    ax.annotate("", xy=(2.9, vessel_y), xytext=(5.1, vessel_y),
                arrowprops=arrow_kw, zorder=1)
    ax.text(8.0, vessel_y + 0.45, ar("تشدید"),
            ha="center", va="bottom",
            fontsize=9.5, fontproperties=FP_FA_BOLD,
            style="italic", color="#666666")
    ax.text(4.0, vessel_y + 0.45, ar("شکستنِ مهار"),
            ha="center", va="bottom",
            fontsize=9.5, fontproperties=FP_FA_BOLD,
            style="italic", color="#666666")

    # Source / target mapping (Persian RTL reads right-to-left; we render
    # the "source domain" on the right and "target domain" on the left,
    # joined by a graphical arrow drawn separately rather than a Unicode
    # arrow glyph Vazirmatn does not cover).
    ax.text(9.4, 0.7,
            ar("حوزهٔ مبدأ (ظرف):  ظرف · مهر · فشار · انفجار"),
            ha="center", va="center",
            fontsize=10, fontproperties=FP_FA, color="#1A1A1A",
            bbox=dict(boxstyle="round,pad=0.45", facecolor="#F5F0E1",
                      edgecolor="#9E8E5A", linewidth=0.8))
    ax.text(2.6, 0.7,
            ar("حوزهٔ مقصد (خشم):  غَیظِ مهارشده با کَظم · گسستِ تَمَیُّز"),
            ha="center", va="center",
            fontsize=10, fontproperties=FP_FA, color="#1A1A1A",
            bbox=dict(boxstyle="round,pad=0.45", facecolor="#EFE6F2",
                      edgecolor="#7C5C8E", linewidth=0.8))
    # Connecting arrow: source -> target (right-to-left)
    ax.annotate("", xy=(4.4, 0.7), xytext=(7.6, 0.7),
                arrowprops=dict(arrowstyle="-|>", color="#666666",
                                lw=1.8, mutation_scale=18))
    ax.text(6.0, 1.05, ar("نگاشت"),
            ha="center", va="bottom",
            fontsize=9, fontproperties=FP_FA, style="italic",
            color="#666666")

    fig.tight_layout()
    out = FIG_DIR / "fig6_metaphor_diagram.pdf"
    plt.savefig(out)
    plt.savefig(out.with_suffix(".png"), dpi=200)
    plt.close()
    print(f"Wrote {out}")


# --------------------------------------------------------------------- #
#  Figure 7 — Network centrality                                        #
# --------------------------------------------------------------------- #
def fig7_centrality() -> None:
    rows = []
    with (CONC_DIR / "network_centrality.csv").open("r", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            r["stage"] = int(r["stage"])
            r["degree_weighted"] = float(r["degree_weighted"])
            r["betweenness"] = float(r["betweenness"])
            r["closeness"] = float(r["closeness"])
            rows.append(r)

    canonical = [bw for bw in CANONICAL_ORDER if bw in {r["root_bw"] for r in rows}]
    by_bw = {r["root_bw"]: r for r in rows}
    surface_by_bw = {r.bw: r.display() for r in SPECTRUM}
    labels = [ar(surface_by_bw[bw]) for bw in canonical]
    x = list(range(len(canonical)))
    colors = [STAGE_COLORS[by_bw[bw]["stage"]] for bw in canonical]

    fig, axes = plt.subplots(1, 3, figsize=(17, 5.8))

    panels = [
        ("degree_weighted", ar("الف) درجهٔ وزنی"),
         ar("درجهٔ وزنی"), "{:.0f}", 0.10),
        ("betweenness",     ar("ب) مرکزیتِ بینابینی"),
         ar("مرکزیتِ بینابینی"), "{:.2f}", 0.005),
        ("closeness",       ar("ج) مرکزیتِ نزدیکی"),
         ar("مرکزیتِ نزدیکی"), "{:.2f}", 0.012),
    ]

    for ax, (key, title, ylabel, fmt, gap) in zip(axes, panels):
        vals = [by_bw[bw][key] for bw in canonical]
        ax.bar(x, vals, color=colors, edgecolor="white", linewidth=0.6,
               zorder=2)
        ax.set_xticks(x)
        ax.set_xticklabels(labels, fontsize=15,
                           fontproperties=FP_AR_BOLD,
                           rotation=45, ha="right")
        ax.set_ylabel(ylabel, fontproperties=FP_FA, fontsize=12)
        ax.set_title(title, fontproperties=FP_FA_BOLD,
                     fontsize=12, pad=10)
        style_axes(ax)
        vmax = max(vals) if vals else 1
        for xi, v in enumerate(vals):
            if v > 0:
                ax.text(xi, v + max(vmax * 0.02, gap),
                        fa_num(fmt.format(v)),
                        ha="center", va="bottom",
                        fontsize=10.5, fontproperties=FP_FA,
                        color="#222222")
        ax.set_ylim(0, vmax * 1.18 if vmax > 0 else 1)
        set_fa_yaxis(ax)

    # Figure title (and 14-core-roots banner) live in the manuscript caption.

    fig.tight_layout()

    out = FIG_DIR / "fig7_centrality.pdf"
    plt.savefig(out)
    plt.savefig(out.with_suffix(".png"), dpi=200)
    plt.close()
    print(f"Wrote {out}")


if __name__ == "__main__":
    fig5_morphology()
    fig6_metaphor()
    fig7_centrality()
