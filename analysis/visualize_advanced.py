"""Generate the advanced (research-grade) figures — publication upgrade.

    figures/fig5_morphology_stack.{pdf,png}     Per-root morphological breakdown
    figures/fig6_metaphor_diagram.{pdf,png}     ANGER IS PRESSURIZED CONTAINER
    figures/fig7_centrality.{pdf,png}           Centrality measures with bootstrap CIs
"""
from __future__ import annotations

import csv
import io
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
import matplotlib.font_manager as fm  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Rectangle, Polygon, PathPatch  # noqa: E402
from matplotlib.path import Path as MplPath  # noqa: E402
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

AMIRI_REGULAR = FONT_DIR / "amiri-regular.ttf"
AMIRI_BOLD = FONT_DIR / "amiri-bold.ttf"
EBGARAMOND = FONT_DIR / "ebgaramond-regular.ttf"
for _f in (AMIRI_REGULAR, AMIRI_BOLD, EBGARAMOND):
    if _f.exists():
        fm.fontManager.addfont(str(_f))
ARABIC_FP = fm.FontProperties(fname=str(AMIRI_REGULAR)) if AMIRI_REGULAR.exists() else None
ARABIC_BOLD_FP = fm.FontProperties(fname=str(AMIRI_BOLD)) if AMIRI_BOLD.exists() else ARABIC_FP


def ar(s: str) -> str:
    return get_display(arabic_reshaper.reshape(s)) if s else s


_serif_stack = ["EB Garamond", "DejaVu Serif", "Times New Roman", "Times", "serif"]
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": _serif_stack,
    "font.size": 11,
    "axes.labelsize": 12,
    "axes.titlesize": 12,
    "legend.fontsize": 10,
    "legend.frameon": False,
    "xtick.labelsize": 11,
    "ytick.labelsize": 11,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.linewidth": 0.8,
    "xtick.major.width": 0.7,
    "ytick.major.width": 0.7,
    "figure.dpi": 150,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.08,
    "savefig.dpi": 300,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})

# Okabe-Ito stage palette (cb-safe, identical to visualize_spectrum.py)
STAGE_COLORS = {
    1: "#56B4E9", 2: "#0072B2", 3: "#E69F00",
    4: "#D55E00", 5: "#7B1E25", 6: "#009E73",
}
CANONICAL_ORDER = [r.bw for r in SPECTRUM]


def _ax_clean(ax):
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    ax.spines["left"].set_color("#444444")
    ax.spines["bottom"].set_color("#444444")
    ax.tick_params(colors="#444444", which="both")
    ax.grid(False)


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
    core_bw = [r.bw for r in SPECTRUM]
    rows = [r for r in rows if r["root_bw"] in core_bw]
    surface_by_bw = {r.bw: r.display() for r in SPECTRUM}
    translit_by_bw = {r.bw: r.translit for r in SPECTRUM}

    canonical = [bw for bw in CANONICAL_ORDER if bw in {r["root_bw"] for r in rows}]
    by_bw = {r["root_bw"]: r for r in rows}

    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(14, 6.2),
                                  gridspec_kw={"width_ratios": [1, 1]})
    x = list(range(len(canonical)))
    # cb-safe categorical (Okabe-Ito-derived, distinct hues)
    categories = [
        ("verb",       "VERB",  "#0072B2"),  # blue
        ("noun",       "NOUN",  "#E69F00"),  # orange
        ("adjective",  "ADJ",   "#009E73"),  # green
        ("participle", "PCPL",  "#CC79A7"),  # rose
        ("other",      "OTHER", "#999999"),  # grey
    ]

    # Panel (a): absolute counts
    bottoms = [0] * len(canonical)
    for key, label, color in categories:
        vals = [by_bw[bw][key] for bw in canonical]
        ax.bar(x, vals, bottom=bottoms, label=label,
               color=color, edgecolor="#222222", linewidth=0.3, width=0.78)
        for xi, (b, v) in enumerate(zip(bottoms, vals)):
            if v >= 4:
                ax.text(xi, b + v / 2, str(v), ha="center", va="center",
                        fontsize=9.5, color="white" if key == "verb" else "#222222",
                        fontweight="bold", family="serif")
        bottoms = [bo + v for bo, v in zip(bottoms, vals)]
    ymax_a = max(bottoms) * 1.15
    ax.set_ylim(0, ymax_a)
    for xi, bw in enumerate(canonical):
        total = by_bw[bw]["total"]
        ax.text(xi, total + ymax_a * 0.015, f"n = {total}",
                ha="center", va="bottom",
                fontsize=10, fontweight="bold", color="#222222",
                family="serif")
    ax.set_xticks(x)
    ax.set_xticklabels([""] * len(x))
    for xi, bw in enumerate(canonical):
        ax.text(xi, -ymax_a * 0.04, ar(surface_by_bw[bw]),
                ha="center", va="top", fontsize=15,
                fontproperties=ARABIC_FP)
        ax.text(xi, -ymax_a * 0.10, translit_by_bw[bw],
                ha="center", va="top", fontsize=9, style="italic",
                color="#555555", family="serif")
    ax.set_ylabel("Number of attestations", fontsize=12, family="serif")
    ax.set_title("(a) Absolute counts", fontsize=12, loc="left", family="serif")
    _ax_clean(ax)
    ax.tick_params(axis="y", labelsize=11)

    # Panel (b): percentage stack
    bottoms_pct = [0.0] * len(canonical)
    totals = [max(by_bw[bw]["total"], 1) for bw in canonical]
    for key, label, color in categories:
        vals = [by_bw[bw][key] for bw in canonical]
        pcts = [100.0 * v / t for v, t in zip(vals, totals)]
        ax2.bar(x, pcts, bottom=bottoms_pct, label=label,
                color=color, edgecolor="#222222", linewidth=0.3, width=0.78)
        for xi, (b, p) in enumerate(zip(bottoms_pct, pcts)):
            if p >= 7:
                ax2.text(xi, b + p / 2, f"{p:.0f}%",
                         ha="center", va="center",
                         fontsize=9.5,
                         color="white" if key == "verb" else "#222222",
                         fontweight="bold", family="serif")
        bottoms_pct = [bo + p for bo, p in zip(bottoms_pct, pcts)]
    ax2.set_xticks(x)
    ax2.set_xticklabels([""] * len(x))
    for xi, bw in enumerate(canonical):
        ax2.text(xi, -4, ar(surface_by_bw[bw]),
                 ha="center", va="top", fontsize=15,
                 fontproperties=ARABIC_FP)
        ax2.text(xi, -10, translit_by_bw[bw],
                 ha="center", va="top", fontsize=9, style="italic",
                 color="#555555", family="serif")
    ax2.set_ylabel("Percent of attestations (within root)",
                   fontsize=12, family="serif")
    ax2.set_ylim(0, 100)
    ax2.set_title("(b) Percentage stack", fontsize=12, loc="left",
                  family="serif")
    _ax_clean(ax2)
    ax2.tick_params(axis="y", labelsize=11)

    # Shared legend on top
    handles, labels = ax2.get_legend_handles_labels()
    leg = fig.legend(handles, labels, loc="upper center", ncol=5,
                     fontsize=11, frameon=False,
                     bbox_to_anchor=(0.5, 1.01))
    for t in leg.get_texts():
        t.set_family("serif")

    # Verbal-share-by-stage trend is documented in the manuscript caption;
    # not embedded as overlay here.

    fig.tight_layout(rect=(0, 0.0, 1, 0.97))

    out = FIG_DIR / "fig5_morphology_stack.pdf"
    plt.savefig(out)
    plt.savefig(out.with_suffix(".png"), dpi=200)
    plt.close()
    print(f"Wrote {out}")


# -------------------------------------------------------------------- #
#  Figure 6 — Conceptual metaphor diagram (pressurised container)      #
# -------------------------------------------------------------------- #

def _draw_vessel(ax, cx, cy, color, fluid_frac, sealed, burst):
    """Draw a stylised pressurised-vessel glyph at (cx, cy)."""
    w, h = 1.7, 2.1
    # Vessel outline — rounded rectangle
    ax.add_patch(FancyBboxPatch(
        (cx - w/2, cy - h/2), w, h,
        boxstyle="round,pad=0.02,rounding_size=0.22",
        facecolor="#FAFAF6", edgecolor="#222222", linewidth=1.4,
        zorder=2,
    ))
    # Fluid level
    f_bot = cy - h/2 + 0.10
    f_top = f_bot + (h - 0.20) * fluid_frac
    ax.add_patch(Rectangle((cx - w/2 + 0.06, f_bot), w - 0.12, f_top - f_bot,
                           facecolor=color, edgecolor="none", alpha=0.78,
                           zorder=3))
    # Wavy meniscus line on top of fluid
    import numpy as np
    xs = np.linspace(cx - w/2 + 0.06, cx + w/2 - 0.06, 60)
    ys = f_top + 0.025 * np.sin(np.linspace(0, 4 * np.pi, 60))
    ax.plot(xs, ys, color=color, linewidth=1.2, alpha=0.95, zorder=4)

    # Lid: only present for sealed states
    if sealed:
        lid_y = cy + h/2 + 0.02
        ax.plot([cx - w/2 - 0.05, cx + w/2 + 0.05], [lid_y, lid_y],
                color="#222222", linewidth=2.4, solid_capstyle="round",
                zorder=5)
        # Bolts
        for bx in (cx - w/2 + 0.08, cx + w/2 - 0.08):
            ax.scatter(bx, lid_y, s=22, color="#444444", zorder=6)
        ax.text(cx, lid_y + 0.18, "(sealed by kaẓm)",
                ha="center", va="bottom", fontsize=8.2, style="italic",
                color="#555555", family="serif")

    # Burst: vessel structure splitting
    if burst:
        # Crack on the side
        crack = MplPath(
            [(cx - 0.4, cy + 0.2), (cx - 0.55, cy + 0.45),
             (cx - 0.38, cy + 0.55), (cx - 0.55, cy + 0.78),
             (cx - 0.30, cy + 0.95)],
            [MplPath.MOVETO, MplPath.LINETO, MplPath.LINETO,
             MplPath.LINETO, MplPath.LINETO]
        )
        ax.add_patch(PathPatch(crack, edgecolor="#222222", facecolor="none",
                               linewidth=1.6, zorder=6))
        # Outward shards
        for dx, dy in [(-0.85, 0.45), (-0.55, 0.95), (0.55, 0.95),
                       (0.85, 0.45), (0.95, 0.05)]:
            ax.annotate("", xy=(cx + dx, cy + dy),
                        xytext=(cx + dx * 0.5, cy + dy * 0.5),
                        arrowprops=dict(arrowstyle="-|>",
                                        color="#7B1E25", lw=1.4,
                                        alpha=0.85,
                                        mutation_scale=11),
                        zorder=7)
        ax.text(cx + 1.0, cy + 0.7, "container\nsplits apart",
                fontsize=8.4, color="#7B1E25", fontweight="bold",
                family="serif", ha="left", va="center")


def fig6_metaphor() -> None:
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.set_xlim(0, 14)
    ax.set_ylim(-0.5, 8)
    ax.axis("off")

    # Title block
    ax.text(7, 7.5, "ANGER IS A PRESSURISED CONTAINER",
            ha="center", va="center", fontsize=14, fontweight="bold",
            color="#222222", family="serif")
    ax.text(7, 7.0,
            "Lakoff & Kövecses (1987), instantiated by the Qur'anic "
            "ġaḍab → ġayẓ + kaẓm → tamayyuz triplet",
            ha="center", va="center", fontsize=10, style="italic",
            color="#555555", family="serif")

    # Vessel layout
    vessel_cx = [2.4, 7.0, 11.6]
    vessel_cy = 4.0
    specs = [
        # (color, fluid_frac, sealed, burst)
        ("#FFC857", 0.35, False, False),   # ġaḍab — open
        ("#E76F51", 0.78, True,  False),   # ġayẓ + kaẓm — sealed
        ("#9D2933", 0.95, True,  True),    # tamayyuz — burst
    ]
    headers = [
        ("Stage 4", "ġaḍab",
         "Open vessel; affect dissipating\ninto language and gesture."),
        ("Stage 5a", "ġayẓ  +  kaẓm",
         "Sealed vessel; pressure rising.\nAgent restrains via kaẓm\n(Q. 3:134, al-kāẓimīn al-ġayẓ)."),
        ("Stage 5b", "tamayyuz",
         "Container collapse (Q. 67:8):\ntakādu tamayyazu min al-ġayẓ\n— m-y-z = 'to part, sever'."),
    ]
    arabic_lbl = [
        "غَضَب",
        "غَيْظ + كَظْم",
        "تَمَيُّز",
    ]
    arabic_verse = [
        "",
        "وَالْكَاظِمِينَ الْغَيْظَ",
        "تَكَادُ تَمَيَّزُ مِنَ الْغَيْظِ",
    ]

    for cx, (col, fh, sealed, burst), (st, name, desc), arabic, verse in zip(
            vessel_cx, specs, headers, arabic_lbl, arabic_verse):
        # Stage banner
        ax.text(cx, vessel_cy + 1.85, st, ha="center", va="bottom",
                fontsize=10, fontweight="bold", color=STAGE_COLORS[4 if st == "Stage 4" else 5],
                family="serif")
        ax.text(cx, vessel_cy + 1.55, name, ha="center", va="bottom",
                fontsize=11.5, color="#222222", style="italic",
                family="serif")
        _draw_vessel(ax, cx, vessel_cy, col, fh, sealed, burst)
        # Arabic label below vessel
        ax.text(cx, vessel_cy - 1.40, ar(arabic), ha="center", va="center",
                fontsize=15, color="#222222",
                fontproperties=ARABIC_BOLD_FP)
        # Q-verse below
        if verse:
            ax.text(cx, vessel_cy - 1.90, ar(verse), ha="center", va="center",
                    fontsize=11, color="#555555",
                    fontproperties=ARABIC_FP)
        # Description further below
        ax.text(cx, vessel_cy - 2.50, desc, ha="center", va="top",
                fontsize=8.6, color="#222222", family="serif")

    # Inter-vessel arrows
    arrow_kw = dict(arrowstyle="-|>", color="#777777", lw=1.8,
                    mutation_scale=14, connectionstyle="arc3,rad=0.0")
    ax.annotate("", xy=(vessel_cx[1] - 1.1, vessel_cy),
                xytext=(vessel_cx[0] + 1.1, vessel_cy),
                arrowprops=arrow_kw)
    ax.annotate("", xy=(vessel_cx[2] - 1.1, vessel_cy),
                xytext=(vessel_cx[1] + 1.1, vessel_cy),
                arrowprops=arrow_kw)
    ax.text((vessel_cx[0] + vessel_cx[1]) / 2, vessel_cy + 0.35,
            "intensifies\n+ seal applied",
            ha="center", va="bottom", fontsize=8.6, style="italic",
            color="#555555", family="serif")
    ax.text((vessel_cx[1] + vessel_cx[2]) / 2, vessel_cy + 0.35,
            "containment\nfails",
            ha="center", va="bottom", fontsize=8.6, style="italic",
            color="#555555", family="serif")

    # Source/target-domain mapping banner
    banner = ("SOURCE  (CONTAINER):  vessel · fluid · seal · pressure · burst"
              "   →   "
              "TARGET  (ANGER):  ġaḍab · ġayẓ-as-fluid · kaẓm-as-seal · tamayyuz-as-collapse")
    ax.text(7, 0.0, banner, ha="center", va="center",
            fontsize=9.5, color="#222222", family="serif",
            bbox=dict(boxstyle="round,pad=0.55", fc="#F5F1E8",
                      ec="#888888", lw=0.6))

    out = FIG_DIR / "fig6_metaphor_diagram.pdf"
    plt.savefig(out)
    plt.savefig(out.with_suffix(".png"), dpi=200)
    plt.close()
    print(f"Wrote {out}")


# -------------------------------------------------------------------- #
#  Figure 7 — Network centrality with bootstrap CIs                    #
# -------------------------------------------------------------------- #

def fig7_centrality() -> None:
    rows = []
    with (CONC_DIR / "network_centrality.csv").open("r", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            r["stage"] = int(r["stage"])
            for k in ("degree_weighted",
                       "degree_ci_lower", "degree_ci_upper",
                       "betweenness", "betweenness_ci_lower",
                       "betweenness_ci_upper",
                       "closeness", "closeness_ci_lower",
                       "closeness_ci_upper"):
                if k in r:
                    r[k] = float(r[k])
            rows.append(r)

    canonical = [bw for bw in CANONICAL_ORDER if bw in {r["root_bw"] for r in rows}]
    by_bw = {r["root_bw"]: r for r in rows}
    surface_by_bw = {r.bw: r.display() for r in SPECTRUM}
    translit_by_bw = {r.bw: r.translit for r in SPECTRUM}
    labels_ar = [surface_by_bw[bw] for bw in canonical]
    labels_tr = [translit_by_bw[bw] for bw in canonical]
    x = list(range(len(canonical)))
    colors = [STAGE_COLORS[by_bw[bw]["stage"]] for bw in canonical]

    fig, axes = plt.subplots(1, 3, figsize=(17, 6.0))

    def _panel(ax, key, ci_lo_key, ci_hi_key, ylabel, title, fmt="{:.2f}"):
        vals = [by_bw[bw][key] for bw in canonical]
        ci_lo = [by_bw[bw][ci_lo_key] for bw in canonical]
        ci_hi = [by_bw[bw][ci_hi_key] for bw in canonical]
        # Asymmetric error
        err_lo = [max(v - lo, 0) for v, lo in zip(vals, ci_lo)]
        err_hi = [max(hi - v, 0) for v, hi in zip(vals, ci_hi)]
        ax.bar(x, vals, color=colors, edgecolor="#222222", linewidth=0.5,
               width=0.72, zorder=2)
        ax.errorbar(x, vals, yerr=[err_lo, err_hi], fmt="none",
                    ecolor="#333333", elinewidth=0.9, capsize=2.6,
                    capthick=0.8, zorder=3, alpha=0.85)
        ax.set_xticks(x)
        ax.set_xticklabels([""] * len(x))
        ymax = max(max(ci_hi), max(vals)) * 1.18
        if ymax <= 0:
            ymax = 1.0
        ax.set_ylim(0, ymax)
        for xi, lab_ar in enumerate(labels_ar):
            ax.text(xi, -ymax * 0.04, ar(lab_ar),
                    ha="center", va="top", fontsize=15,
                    fontproperties=ARABIC_FP)
            ax.text(xi, -ymax * 0.105, labels_tr[xi],
                    ha="center", va="top", fontsize=9, style="italic",
                    color="#555555", family="serif", rotation=0)
        ax.set_ylabel(ylabel, fontsize=12, family="serif")
        ax.set_title(title, fontsize=12, loc="left", family="serif")
        for xi, v in enumerate(vals):
            if v > 0:
                ax.text(xi, v + ymax * 0.015, fmt.format(v),
                        ha="center", va="bottom", fontsize=10,
                        color="#222222", family="serif")
        _ax_clean(ax)
        ax.tick_params(axis="y", labelsize=11)

    _panel(axes[0], "degree_weighted", "degree_ci_lower", "degree_ci_upper",
           "Weighted degree",
           "(a) Weighted degree", fmt="{:.0f}")
    _panel(axes[1], "betweenness", "betweenness_ci_lower",
           "betweenness_ci_upper",
           "Betweenness centrality",
           "(b) Betweenness (bridge-node strength)", fmt="{:.2f}")
    _panel(axes[2], "closeness", "closeness_ci_lower", "closeness_ci_upper",
           "Closeness centrality",
           "(c) Closeness (proximity to all roots)", fmt="{:.2f}")

    # Bridge-node bootstrap CIs and baghy-as-pivot interpretation live in
    # the manuscript caption (no embedded overlay or suptitle here).

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
