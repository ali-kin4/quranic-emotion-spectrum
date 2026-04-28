"""Generate the advanced (research-grade) figures (Persian-localized variant).

    figures_fa/fig5_morphology_stack.{pdf,png}     Per-root morphological breakdown
    figures_fa/fig6_metaphor_diagram.{pdf,png}     خشم، ظرفی است تحت فشار
    figures_fa/fig7_centrality.{pdf,png}           Centrality measures bar chart
"""
from __future__ import annotations

import csv
import io
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch  # noqa: E402
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


def ar(s: str) -> str:
    return get_display(arabic_reshaper.reshape(s)) if s else s


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

STAGE_COLORS = {1: "#4C72B0", 2: "#DD8452", 3: "#C44E52", 4: "#55A868"}


# -------------------------------------------------------------------- #
#  Figure 5 — Morphological breakdown                                  #
# -------------------------------------------------------------------- #

def fig5_morphology() -> None:
    rows = []
    with (CONC_DIR / "morphology_by_root.csv").open("r", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            r["stage"] = int(r["stage"])
            for k in ("verb", "noun", "adjective", "participle", "other", "total"):
                r[k] = int(r[k])
            rows.append(r)
    # Core spectrum only (10 roots)
    core_bw = [r.bw for r in SPECTRUM]
    rows = [r for r in rows if r["root_bw"] in core_bw]
    surface_by_bw = {r.bw: r.display() for r in SPECTRUM}

    canonical = ["Dyq", "Hzn", "Asf", "sxT", "gDb", "gyZ", "myz",
                 "bgy", "Tgy", "Etw"]
    by_bw = {r["root_bw"]: r for r in rows}

    fig, ax = plt.subplots(figsize=(12, 5.5))
    labels = [ar(surface_by_bw[bw]) for bw in canonical]
    x = list(range(len(canonical)))
    bottoms = [0] * len(canonical)
    # Persian POS labels
    categories = [
        ("verb",       ar("فعل"),    "#4878CF"),
        ("noun",       ar("اسم"),    "#EE854A"),
        ("adjective",  ar("صفت"),    "#6ACC65"),
        ("participle", ar("اسم فاعل/مفعول"), "#956CB4"),
        ("other",      ar("سایر"),    "#D5D5D5"),
    ]
    for key, label, color in categories:
        vals = [by_bw[bw][key] for bw in canonical]
        ax.bar(x, vals, bottom=bottoms, label=label,
               color=color, edgecolor="black", linewidth=0.4)
        # In-bar text for non-trivial slices
        for xi, (b, v) in enumerate(zip(bottoms, vals)):
            if v >= 4:
                ax.text(xi, b + v / 2, str(v), ha="center", va="center",
                        fontsize=8, color="black", fontweight="bold")
        bottoms = [bo + v for bo, v in zip(bottoms, vals)]
    # Annotate totals on top
    for xi, bw in enumerate(canonical):
        total = by_bw[bw]["total"]
        ax.text(xi, total + 1.5, f"n = {total}", ha="center", va="bottom",
                fontsize=9, fontweight="bold")

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=12)
    ax.set_ylabel(ar("تعداد بسامد"))
    # Add headroom so the title and legend don't collide with tall bars / n-labels
    max_total = max(by_bw[bw]["total"] for bw in canonical)
    ax.set_ylim(0, max_total * 1.25)
    ax.set_title(ar("پروفایل ریخت‌شناختی واژگان طیف "
                    "(فعل / اسم / صفت / اسم فاعل-مفعول)") + "\n"
                 + ar("نشان‌دهندهٔ غلبه فعلی در مراحل آزردگی و خشم در "
                      "برابر غلبه اسمی در مرحله عصیان"),
                 fontsize=11, pad=14)
    ax.legend(loc="upper left", ncol=5, fontsize=9, frameon=False)

    out = FIG_DIR / "fig5_morphology_stack.pdf"
    plt.savefig(out)
    plt.savefig(out.with_suffix(".png"))
    plt.close()
    print(f"Wrote {out}")


# -------------------------------------------------------------------- #
#  Figure 6 — Conceptual metaphor diagram                              #
# -------------------------------------------------------------------- #

def fig6_metaphor() -> None:
    fig, ax = plt.subplots(figsize=(11, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")

    # Central frame title (Persian)
    ax.text(5, 7.6, ar("خشم، ظرفی است تحت فشار"),
            ha="center", va="center", fontsize=13, fontweight="bold")
    ax.text(5, 7.2,
            ar("(Lakoff & Kövecses, 1987) — اعمال‌شده بر سه‌گانهٔ غَیظ–کَظم–تَمَیُّز در قرآن"),
            ha="center", va="center", fontsize=10, color="dimgray", style="italic")

    # Three vessel states across the bottom (Persian labels)
    vessel_states = [
        # (x, y, color, fluid_height, label_top, label_bottom, ar_label)
        (1.5, 3.5, "#FFC857", 0.4,
         ar("مرحله ۲: غَضَب"),
         ar("ظرف باز / بدون مهر؛")
         + "\n" + ar("هیجان حاضر است اما تحت فشار نیست."),
         "غَضَب"),
        (5.0, 3.5, "#E76F51", 0.7,
         ar("مرحله ۳ (الف): غَیظ + کَظم"),
         ar("ظرف مهر شده؛ فشار در حال افزایش؛")
         + "\n" + ar("کنشگر با کَظم خود را مهار می‌کند (آل‌عمران ۳:۱۳۴،")
         + "\n" + ar("وَالْكَاظِمِينَ الْغَيْظَ") + ").",
         "غَيْظ + كَظْم"),
        (8.5, 3.5, "#9D2933", 0.95,
         ar("مرحله ۳ (ب): تَمَیُّز"),
         ar("گسستن ظرف (مُلک ۶۷:۸):") + "\n"
         + ar("تَكَادُ تَمَيَّزُ مِنَ الْغَيْظِ") + "\n"
         + ar("— خود ظرف از هم می‌شکافد."),
         "تَمَيُّز"),
    ]

    for (cx, cy, col, fh, top, bot, arabic) in vessel_states:
        # Vessel as rounded rectangle
        ax.add_patch(FancyBboxPatch(
            (cx - 0.7, cy - 0.9), 1.4, 1.8,
            boxstyle="round,pad=0.05,rounding_size=0.15",
            facecolor="white", edgecolor="black", linewidth=1.6
        ))
        # Fluid level
        ax.fill_between([cx - 0.65, cx + 0.65],
                        cy - 0.85, cy - 0.85 + fh * 1.7,
                        color=col, alpha=0.7, edgecolor="none")
        # Lid: only present for sealed states
        if fh > 0.5:
            ax.plot([cx - 0.7, cx + 0.7], [cy + 0.9, cy + 0.9],
                    color="black", linewidth=2)
            ax.text(cx, cy + 1.05, ar("(مهر شده)"), ha="center", va="bottom",
                    fontsize=8, style="italic", color="dimgray")
            # Steam/pressure escape arrows for tamayyuz state
            if fh > 0.9:
                # Crack
                ax.plot([cx - 0.6, cx - 0.4, cx - 0.5, cx - 0.3, cx - 0.5],
                        [cy + 0.4, cy + 0.6, cy + 0.55, cy + 0.75, cy + 0.85],
                        color="black", linewidth=1.5)
                ax.text(cx + 0.85, cy + 0.5, ar("انفجار"),
                        fontsize=8, color="darkred", fontweight="bold")
        # Arabic label inside vessel
        ax.text(cx, cy - 1.45, ar(arabic), ha="center", va="center",
                fontsize=12, fontweight="bold", color="black")
        # Stage label above
        ax.text(cx, cy + 1.55, top, ha="center", va="bottom",
                fontsize=10, fontweight="bold")
        # Description below
        ax.text(cx, cy - 2.2, bot, ha="center", va="top", fontsize=8.5,
                color="black")

    # Arrows between states
    arrow_kw = dict(arrowstyle="->", color="gray", lw=2,
                    connectionstyle="arc3,rad=0.0")
    ax.annotate("", xy=(4.2, 3.5), xytext=(2.3, 3.5), arrowprops=arrow_kw)
    ax.annotate("", xy=(7.7, 3.5), xytext=(5.8, 3.5), arrowprops=arrow_kw)
    ax.text(3.25, 3.85, ar("تشدید"), ha="center", va="bottom",
            fontsize=9, color="gray", style="italic")
    ax.text(6.75, 3.85, ar("شکستن مهار"), ha="center", va="bottom",
            fontsize=9, color="gray", style="italic")

    # Side annotation: source-domain / target-domain mapping (Persian)
    ax.text(5, 0.5,
            ar("حوزهٔ مبدأ (ظرف): ظرف · مهر · فشار · انفجار   →   "
               "حوزهٔ مقصد (خشم): غَیظِ مهارشده با کَظم · گسستِ تَمَیُّز"),
            ha="center", va="center", fontsize=9.5, color="black",
            bbox=dict(boxstyle="round,pad=0.4", fc="#F5F0E1",
                      ec="dimgray", linewidth=0.6))

    out = FIG_DIR / "fig6_metaphor_diagram.pdf"
    plt.savefig(out)
    plt.savefig(out.with_suffix(".png"))
    plt.close()
    print(f"Wrote {out}")


# -------------------------------------------------------------------- #
#  Figure 7 — Centrality metrics                                       #
# -------------------------------------------------------------------- #

def fig7_centrality() -> None:
    rows = []
    with (CONC_DIR / "network_centrality.csv").open("r", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            r["stage"] = int(r["stage"])
            r["degree_weighted"] = float(r["degree_weighted"])
            r["betweenness"] = float(r["betweenness"])
            r["closeness"] = float(r["closeness"])
            rows.append(r)

    canonical = ["Dyq", "Hzn", "Asf", "sxT", "gDb", "gyZ", "myz",
                 "bgy", "Tgy", "Etw"]
    by_bw = {r["root_bw"]: r for r in rows}
    surface_by_bw = {r.bw: r.display() for r in SPECTRUM}
    labels = [ar(surface_by_bw[bw]) for bw in canonical]
    x = list(range(len(canonical)))
    colors = [STAGE_COLORS[by_bw[bw]["stage"]] for bw in canonical]

    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

    # Panel 1: Weighted degree
    deg = [by_bw[bw]["degree_weighted"] for bw in canonical]
    axes[0].bar(x, deg, color=colors, edgecolor="black", linewidth=0.6)
    axes[0].set_xticks(x)
    axes[0].set_xticklabels(labels, fontsize=11)
    axes[0].set_ylabel(ar("درجه وزنی"))
    axes[0].set_title(ar("الف) مرکزیت درجه"))
    for xi, v in enumerate(deg):
        axes[0].text(xi, v + 0.1, f"{v:.0f}", ha="center", fontsize=8)

    # Panel 2: Betweenness
    btw = [by_bw[bw]["betweenness"] for bw in canonical]
    axes[1].bar(x, btw, color=colors, edgecolor="black", linewidth=0.6)
    axes[1].set_xticks(x)
    axes[1].set_xticklabels(labels, fontsize=11)
    axes[1].set_ylabel(ar("مرکزیت بینابینی"))
    axes[1].set_title(ar("ب) مرکزیت بینابینی"))
    for xi, v in enumerate(btw):
        axes[1].text(xi, v + 0.005, f"{v:.2f}", ha="center", fontsize=8)

    # Panel 3: Closeness
    cls = [by_bw[bw]["closeness"] for bw in canonical]
    axes[2].bar(x, cls, color=colors, edgecolor="black", linewidth=0.6)
    axes[2].set_xticks(x)
    axes[2].set_xticklabels(labels, fontsize=11)
    axes[2].set_ylabel(ar("مرکزیت نزدیکی"))
    axes[2].set_title(ar("ج) مرکزیت نزدیکی"))
    for xi, v in enumerate(cls):
        axes[2].text(xi, v + 0.01, f"{v:.2f}", ha="center", fontsize=8)

    fig.suptitle(ar("سنجه‌های مرکزیت شبکه برای ده ریشه کانونی"),
                 fontsize=11.5)
    fig.tight_layout()

    out = FIG_DIR / "fig7_centrality.pdf"
    plt.savefig(out)
    plt.savefig(out.with_suffix(".png"))
    plt.close()
    print(f"Wrote {out}")


if __name__ == "__main__":
    fig5_morphology()
    fig6_metaphor()
    fig7_centrality()
