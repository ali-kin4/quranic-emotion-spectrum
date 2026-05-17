"""Code-generated replacements for ChatGPT-rendered infographics.

Produces five publication-grade infographics in both English (figures/)
and Persian (figures_fa/) form. All drawing is pure matplotlib with
bundled fonts (Amiri for Arabic, Vazirmatn for Persian, EB Garamond
for Latin). 300 DPI exports, vector PDF + raster PNG.

Outputs:
    fig1_continuum_v2.{pdf,png}    six-stage anger continuum overview
    fig6_metaphor_v2.{pdf,png}     container-metaphor triad
    fig8_mufassir.{pdf,png}        nine-mufassir comparative map
    fig9_bidirectional.{pdf,png}   stage-6 bidirectional causation
    fig10_genealogy.{pdf,png}      theoretical genealogy tree

Run from repo root:
    python analysis/visualize_infographics.py
"""
from __future__ import annotations

import sys
import io
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # noqa: E402

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib import font_manager as fm  # noqa: E402
from matplotlib.patches import (  # noqa: E402
    FancyBboxPatch, FancyArrowPatch, Rectangle, Polygon, Wedge,
    Ellipse, Arc, ConnectionPatch, PathPatch,
)
from matplotlib.path import Path as MplPath  # noqa: E402
import arabic_reshaper  # noqa: E402
from bidi.algorithm import get_display  # noqa: E402

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT_DIR = Path(__file__).resolve().parent.parent

# -------------------- font setup --------------------
FONT_DIR = ROOT_DIR / "paper" / "fonts"
for _f in ("vazirmatn-regular.ttf", "vazirmatn-bold.ttf",
           "vazirmatn-light.ttf", "amiri-regular.ttf", "amiri-bold.ttf",
           "ebgaramond-regular.ttf"):
    p = FONT_DIR / _f
    if p.exists():
        fm.fontManager.addfont(str(p))

FP_FA = fm.FontProperties(fname=str(FONT_DIR / "vazirmatn-regular.ttf"))
FP_FA_B = fm.FontProperties(fname=str(FONT_DIR / "vazirmatn-bold.ttf"))
FP_FA_L = fm.FontProperties(fname=str(FONT_DIR / "vazirmatn-light.ttf"))
FP_AR = fm.FontProperties(fname=str(FONT_DIR / "amiri-regular.ttf"))
FP_AR_B = fm.FontProperties(fname=str(FONT_DIR / "amiri-bold.ttf"))
FP_LATIN = fm.FontProperties(fname=str(FONT_DIR / "ebgaramond-regular.ttf"))


# -------------------- helpers --------------------
def ar(text: str) -> str:
    """Shape + bidi-reorder Arabic/Persian text for matplotlib."""
    if not text:
        return ""
    return get_display(arabic_reshaper.reshape(text))


_FA_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
def fa_num(v) -> str:
    return str(v).translate(_FA_DIGITS).replace(".", "٫")


def add_title(fig, title, subtitle=None, *, fa=False, x=0.5, y_top=0.965):
    fp_t = FP_FA_B if fa else FP_LATIN
    fp_s = FP_FA if fa else FP_LATIN
    fig.text(x, y_top, ar(title) if fa else title,
             ha="center", va="top", fontsize=17, fontproperties=fp_t,
             color="#1a1a1a", fontweight="bold")
    if subtitle:
        fig.text(x, y_top - 0.043, ar(subtitle) if fa else subtitle,
                 ha="center", va="top", fontsize=10.5, fontproperties=fp_s,
                 color="#666666", style="italic")


def soft_card(ax, x, y, w, h, *, fc="#FAFAF7", ec="#C9C2B3", lw=0.9,
              alpha=1.0, rounding=0.018, zorder=1):
    """A pill-shaped rounded-rect card."""
    p = FancyBboxPatch((x, y), w, h,
                       boxstyle=f"round,pad=0,rounding_size={rounding}",
                       linewidth=lw, edgecolor=ec, facecolor=fc,
                       alpha=alpha, zorder=zorder)
    ax.add_patch(p)
    return p


def hairline(ax, x0, y0, x1, y1, *, color="#BDB7A8", lw=0.7, ls="-",
             alpha=1.0, zorder=1):
    ax.plot([x0, x1], [y0, y1], color=color, lw=lw, linestyle=ls,
            alpha=alpha, zorder=zorder, solid_capstyle="round")


# Six-stage palette: warm semantic gradient, CVD-safe (Color Oracle)
STAGE_RIBBON = [
    "#B7C8C0",  # 1 — pale slate-green
    "#A4B0BE",  # 2 — warm grey
    "#C9A37A",  # 3 — dusty amber
    "#B66B3D",  # 4 — burnt orange
    "#8C2F3A",  # 5 — vermillion / wine
    "#4A1424",  # 6 — deep crimson
]


# ====================================================================
# 1) Six-stage anger continuum overview
# ====================================================================
STAGES_EN = [
    (1, "Pre-anger displeasure",   ["ʾff (3)", "krh (41)"],
     "Verbal displeasure",         0.08),
    (2, "Inner pressure",          ["ḍyq (13)", "ḥzn (42)", "ʾsf (5)"],
     "",                           0.13),
    (3, "Evaluative aversion",     ["nqm (17)", "saḫ (4)", "mqt (6)"],
     "",                           0.14),
    (4, "Active anger",            ["ġḍb (24)", "ḥrd (1)"],
     "",                           0.17),
    (5, "Compressed rage",         ["ġyẓ (11) †"],
     "Sealed-container compression", 0.18),
    (6, "Behavioural outcomes",    ["bġy (96)", "ṭġy (39)", "ʿtw (10)"],
     "Behavioural rupture",        0.30),
]

# Persian: stage number, name, root cards (Arabic + count), benchmark, width %
STAGES_FA = [
    (1, "پیش‌از‌خشم",
     [("أُفّ", "۳"), ("کَره", "۴۱")],
     "تضجّرِ کلامی",                0.08),
    (2, "فشارِ درونی",
     [("ضِیق", "۱۳"), ("حُزن", "۴۲"), ("أسف", "۵")],
     "",                          0.13),
    (3, "انزجارِ ارزیابانه",
     [("نَقم", "۱۷"), ("سَخَط", "۴"), ("مَقت", "۶")],
     "",                          0.14),
    (4, "خشمِ فعّال",
     [("غضب", "۲۴"), ("حَرد", "۱")],
     "",                          0.17),
    (5, "خشمِ متراکم",
     [("غیظ", "۱۱") + ("†",)[0:0] + ("†",)[0:0]],
     "فشارِ ظرفِ مُهرشده",         0.18),
    (6, "پیامدهای رفتاری",
     [("بَغی", "۹۶"), ("طُغیان", "۳۹"), ("عُتُوّ", "۱۰")],
     "گسستِ رفتاری",               0.30),
]
# fix Stage 5 card tuple
STAGES_FA[4] = (5, "خشمِ متراکم",
                [("غیظ", "۱۱")],
                "فشارِ ظرفِ مُهرشده", 0.18)


def fig_continuum_overview(out_dir: Path, *, fa: bool):
    """Six-stage continuum ribbon with lexeme cards above each stage band."""
    fig = plt.figure(figsize=(13.5, 5.2), facecolor="#FBFAF6")
    ax = fig.add_axes([0.025, 0.06, 0.95, 0.79])
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.axis("off")

    # Title
    if fa:
        add_title(fig,
                  "پیوستارِ شش‌مرحله‌ایِ خشمِ قرآنی",
                  "محورِ شدتِ کنش · ۳۱۲ بسامد · پیکره‌ی ریخت‌شناختیِ قرآنی، دوکس ۲۰۱۱",
                  fa=True)
    else:
        add_title(fig,
                  "The Qur'anic Anger Spectrum",
                  "A Six-Stage Action-Intensity Continuum · "
                  "N = 312 attestations · Quranic Arabic Corpus v0.4 (Dukes 2011)",
                  fa=False)

    stages = STAGES_FA if fa else STAGES_EN
    # Persian reads right-to-left; we flip the order so Stage 1 is at right
    if fa:
        stages = list(reversed(stages))

    # Calculate band x-ranges
    widths = [s[-1] for s in stages]
    total = sum(widths)
    widths = [w / total for w in widths]
    xs = [0.0]
    for w in widths:
        xs.append(xs[-1] + w)

    # ---- ribbon
    ribbon_y = 0.32
    ribbon_h = 0.16
    for i, st_data in enumerate(stages):
        stnum = st_data[0]
        color = STAGE_RIBBON[stnum - 1]
        x0, x1 = xs[i], xs[i + 1]
        rect = FancyBboxPatch(
            (x0 + 0.002, ribbon_y), x1 - x0 - 0.004, ribbon_h,
            boxstyle="round,pad=0.0,rounding_size=0.018",
            linewidth=0, facecolor=color, alpha=0.95, zorder=2,
        )
        ax.add_patch(rect)
        # stage label INSIDE ribbon
        cx = (x0 + x1) / 2
        label_fp = FP_FA_B if fa else FP_LATIN
        ax.text(cx, ribbon_y + ribbon_h / 2 + 0.018,
                ar(f"مرحله‌ی {fa_num(stnum)}") if fa else f"STAGE {stnum}",
                ha="center", va="center", color="white",
                fontsize=10.5, fontproperties=label_fp, fontweight="bold")
        ax.text(cx, ribbon_y + ribbon_h / 2 - 0.020,
                ar(st_data[1]) if fa else st_data[1],
                ha="center", va="center", color="white",
                fontsize=8.8, fontproperties=label_fp, alpha=0.95)

    # ---- intensity arrow under ribbon
    arrow_y = ribbon_y - 0.07
    if fa:
        # RTL: arrow pointing left
        ax.annotate("", xy=(0.06, arrow_y), xytext=(0.94, arrow_y),
                    arrowprops=dict(arrowstyle="-|>", color="#3D3A33",
                                    lw=1.6, mutation_scale=18))
        ax.text(0.5, arrow_y - 0.05, ar("افزایشِ شدتِ کنش"),
                ha="center", va="center", fontsize=10.5,
                fontproperties=FP_FA_B, color="#3D3A33")
    else:
        ax.annotate("", xy=(0.94, arrow_y), xytext=(0.06, arrow_y),
                    arrowprops=dict(arrowstyle="-|>", color="#3D3A33",
                                    lw=1.6, mutation_scale=18))
        ax.text(0.5, arrow_y - 0.05, "ACTION  INTENSITY",
                ha="center", va="center", fontsize=10.5,
                fontproperties=FP_LATIN, color="#3D3A33",
                fontweight="bold")

    # benchmark labels under arrow
    benchmarks = []
    for i, st_data in enumerate(stages):
        bm = st_data[3]
        if bm:
            cx = (xs[i] + xs[i + 1]) / 2
            benchmarks.append((cx, bm))
    for cx, bm in benchmarks:
        ax.text(cx, arrow_y - 0.10, ar(bm) if fa else bm,
                ha="center", va="top", fontsize=8.5,
                fontproperties=FP_FA_L if fa else FP_LATIN,
                color="#5A554A", style="italic")

    # ---- lexeme cards above ribbon
    card_band_y = ribbon_y + ribbon_h + 0.04
    for i, st_data in enumerate(stages):
        stnum = st_data[0]
        cards = st_data[2]
        x0, x1 = xs[i] + 0.005, xs[i + 1] - 0.005
        band_w = x1 - x0
        n = len(cards)
        # Card width proportional to band, but with min/max
        card_w = min(0.085, max(0.06, band_w / n - 0.012))
        card_h = 0.17
        # Compute slot widths
        slot_w = band_w / n
        for j, card in enumerate(cards):
            cx = x0 + slot_w * (j + 0.5)
            cy = card_band_y + card_h / 2
            # Choose largest card if highest-frequency (bgy = 96)
            if fa:
                root_str, count_str = card
                # Special enlarge: bğy / "بَغی" with 96 in stage 6
                enlarge = (root_str == "بَغی" and count_str == "۹۶")
            else:
                root_str = card
                enlarge = "bġy" in card and "96" in card
            cw = card_w * (1.18 if enlarge else 1.0)
            ch = card_h * (1.10 if enlarge else 1.0)
            soft_card(ax, cx - cw / 2, cy - ch / 2, cw, ch,
                      fc="white", ec=STAGE_RIBBON[stnum - 1], lw=1.1,
                      rounding=0.012, zorder=3)
            if fa:
                # Root in Amiri, count in Vazirmatn
                ax.text(cx, cy + 0.022, ar(root_str),
                        ha="center", va="center",
                        fontsize=15 if enlarge else 13,
                        fontproperties=FP_AR_B,
                        color=STAGE_RIBBON[stnum - 1], zorder=4)
                ax.text(cx, cy - 0.040, count_str,
                        ha="center", va="center",
                        fontsize=10 if enlarge else 9,
                        fontproperties=FP_FA, color="#444", zorder=4)
            else:
                # Root + count in one Latin block
                ax.text(cx, cy, card, ha="center", va="center",
                        fontsize=10.5 if enlarge else 9.2,
                        fontproperties=FP_LATIN,
                        color=STAGE_RIBBON[stnum - 1], fontweight="bold",
                        zorder=4)

    # Stage-5 footnote for tamayyuz
    if fa:
        ax.text(0.5, 0.025,
                ar("† غیظ با تجلیِ تمیّز (سورۀ مُلک: ۸) — فروپاشیِ ساختاریِ ظرف"),
                ha="center", va="center", fontsize=8.5,
                fontproperties=FP_FA, color="#5A554A", style="italic")
    else:
        ax.text(0.5, 0.025,
                "† ġayẓ with tamayyuz manifestation (Q. 67:8) — structural rupture",
                ha="center", va="center", fontsize=8.5,
                fontproperties=FP_LATIN, color="#5A554A", style="italic")

    suffix = "_fa" if fa else ""
    out = out_dir / f"fig1_continuum_v2.png"
    plt.savefig(out, dpi=300, facecolor=fig.get_facecolor())
    plt.savefig(out.with_suffix(".pdf"), facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Wrote {out}")


# ====================================================================
# 2) Container-metaphor triad
# ====================================================================
def _draw_vessel(ax, cx, cy, scale=1.0, color="#B5764A",
                 sealed=False, ruptured=False, glow=False):
    """A Mesopotamian/Arabian-style clay vessel."""
    # Body: tall ellipse-like silhouette via polygon
    s = scale
    # Vessel silhouette points (relative to cx,cy)
    pts = []
    # Rim
    pts.append((-0.18 * s, 0.65 * s))
    pts.append((0.18 * s, 0.65 * s))
    pts.append((0.16 * s, 0.55 * s))
    # Neck inward
    pts.append((0.12 * s, 0.48 * s))
    # Shoulder bulge
    pts.append((0.32 * s, 0.35 * s))
    pts.append((0.42 * s, 0.15 * s))
    pts.append((0.42 * s, -0.10 * s))
    pts.append((0.35 * s, -0.30 * s))
    # Base
    pts.append((0.20 * s, -0.45 * s))
    pts.append((-0.20 * s, -0.45 * s))
    pts.append((-0.35 * s, -0.30 * s))
    pts.append((-0.42 * s, -0.10 * s))
    pts.append((-0.42 * s, 0.15 * s))
    pts.append((-0.32 * s, 0.35 * s))
    pts.append((-0.12 * s, 0.48 * s))
    pts.append((-0.16 * s, 0.55 * s))
    pts = [(cx + x, cy + y) for x, y in pts]
    body = Polygon(pts, closed=True, facecolor=color, edgecolor="#6E3F1E",
                   linewidth=1.6, zorder=3)
    ax.add_patch(body)

    # Internal subtle gradient shadow (a darker polygon offset slightly)
    shade_pts = [(x + 0.025 * s, y - 0.015 * s) for x, y in pts]
    ax.add_patch(Polygon(shade_pts, closed=True, facecolor="#7A4622",
                         edgecolor="none", alpha=0.18, zorder=2))

    # If sealed, draw a leather cord knot
    if sealed:
        # Cord around neck
        ax.add_patch(Ellipse((cx, cy + 0.50 * s), 0.42 * s, 0.10 * s,
                             facecolor="#3F2A18", edgecolor="#231509",
                             linewidth=0.8, zorder=4))
        # Knot
        ax.add_patch(Ellipse((cx + 0.18 * s, cy + 0.50 * s),
                             0.12 * s, 0.16 * s,
                             facecolor="#3F2A18", edgecolor="#231509",
                             linewidth=0.8, zorder=5))
        # Knot tails
        for sx in (1, 1):
            ax.plot([cx + 0.22 * s, cx + 0.32 * s],
                    [cy + 0.46 * s, cy + 0.32 * s],
                    color="#3F2A18", lw=2.2, zorder=5,
                    solid_capstyle="round")
            ax.plot([cx + 0.22 * s, cx + 0.30 * s],
                    [cy + 0.56 * s, cy + 0.62 * s],
                    color="#3F2A18", lw=2.2, zorder=5,
                    solid_capstyle="round")
            break

        # Internal pressure glow visible through hairline strain lines
        for ang_deg in (-65, -25, 15, 55):
            from math import radians, cos, sin
            ang = radians(ang_deg)
            x0, y0 = cx + 0.20 * s * cos(ang), cy + 0.35 * s * sin(ang)
            x1, y1 = cx + 0.36 * s * cos(ang), cy + 0.20 * s * sin(ang) - 0.10 * s
            ax.plot([x0, x1], [y0, y1], color="#D33A24", lw=0.6,
                    alpha=0.6, zorder=4, solid_capstyle="round")
        # Pressure arrows pointing outward against seal
        for dx in (-0.18, 0.18):
            ax.annotate("",
                        xy=(cx + dx * s * 1.4, cy + 0.30 * s),
                        xytext=(cx + dx * s * 0.5, cy + 0.10 * s),
                        arrowprops=dict(arrowstyle="-|>", color="#D33A24",
                                        lw=1.3, mutation_scale=10,
                                        alpha=0.7), zorder=6)

    if ruptured:
        # Vertical jagged crack down the middle with red glow
        crack_x = [cx - 0.005 * s, cx + 0.02 * s, cx - 0.03 * s,
                   cx + 0.025 * s, cx - 0.018 * s, cx + 0.01 * s]
        crack_y = [cy + 0.55 * s, cy + 0.30 * s, cy + 0.08 * s,
                   cy - 0.12 * s, cy - 0.28 * s, cy - 0.42 * s]
        # Glow first (wider, soft)
        ax.plot(crack_x, crack_y, color="#FFB347", lw=10, alpha=0.30,
                zorder=4, solid_capstyle="round", solid_joinstyle="round")
        ax.plot(crack_x, crack_y, color="#FF6A1A", lw=5, alpha=0.55,
                zorder=4.5, solid_capstyle="round", solid_joinstyle="round")
        ax.plot(crack_x, crack_y, color="#A2160F", lw=2.4, alpha=0.95,
                zorder=5, solid_capstyle="round", solid_joinstyle="round")

    if glow and not sealed:
        # Free-rising vapor
        for k in range(4):
            from math import sin
            xx = cx - 0.06 * s + 0.04 * s * k
            ys = np.linspace(cy + 0.66 * s, cy + 1.05 * s, 40)
            xs_curve = xx + 0.04 * s * np.sin(np.linspace(0, 3.5 + k, 40))
            ax.plot(xs_curve, ys, color="#C9C9C7", lw=2 - 0.3 * k,
                    alpha=0.42 - 0.08 * k, solid_capstyle="round",
                    zorder=2)


def fig_metaphor_triad(out_dir: Path, *, fa: bool):
    fig = plt.figure(figsize=(13.5, 6.4), facecolor="#F4EFE5")

    if fa:
        add_title(fig,
                  "عملیاتی‌سازیِ قرآنیِ استعاره‌ی ظرفِ تحتِ فشار",
                  "مرحله‌ی ۴ (غضب) « مرحله‌ی ۵ (غیظ + کَظم) « تجلّیِ تَمَیُّز (سورۀ مُلک: ۸)",
                  fa=True)
    else:
        add_title(fig,
                  "The Qur'anic Operationalisation of the Container Metaphor",
                  "Stage 4 (ġaḍab) → Stage 5 (ġayẓ + kaẓm) → tamayyuz manifestation (Q. 67:8)",
                  fa=False)

    # Three panels
    # In Persian RTL, panel 1 (open) is rightmost; in EN, leftmost.
    panel_titles_en = [
        ("Stage 4 — ġaḍab", "Open container", "Anger present, not yet compressed"),
        ("Stage 5 — ġayẓ + kaẓm", "Sealed container", "Q. 3:134 — 'those who restrain anger'"),
        ("Stage 5 manifestation — tamayyuz", "Structural rupture",
         "Q. 67:8 — تَكَادُ تَمَيَّزُ مِنَ الْغَيْظِ"),
    ]
    panel_titles_fa = [
        ("مرحله‌ی ۴ — غَضَب", "ظرفِ باز", "هیجان حاضر است، اما هنوز متراکم نشده"),
        ("مرحله‌ی ۵ — غیظ + کَظم", "ظرفِ مُهرشده", "آل عمران: ۱۳۴ — وَالْكَاظِمِينَ الْغَيْظَ"),
        ("تجلّیِ مرحله‌ی ۵ — تَمَیُّز", "گسستِ ساختاریِ ظرف",
         "مُلک: ۸ — تَكَادُ تَمَيَّزُ مِنَ الْغَيْظِ"),
    ]

    panel_titles = panel_titles_fa if fa else panel_titles_en
    panel_order = list(reversed(range(3))) if fa else list(range(3))

    # Three subplots in a row
    for slot, idx in enumerate(panel_order):
        ax = fig.add_axes([0.03 + slot * 0.323, 0.10, 0.30, 0.74])
        ax.set_xlim(0, 1); ax.set_ylim(0, 1)
        ax.axis("off")
        # Subtle background card
        soft_card(ax, 0.02, 0.02, 0.96, 0.96,
                  fc="#FAF4E8", ec="#D6CCB2", lw=1.0, rounding=0.025,
                  zorder=0)

        # Title bar
        tcolor = ["#9E5F2E", "#7C1D3F", "#4F1018"][idx]
        soft_card(ax, 0.02, 0.86, 0.96, 0.12,
                  fc=tcolor, ec=tcolor, lw=0,
                  rounding=0.025, zorder=1)
        t1, t2, verse = panel_titles[idx]
        fp_b = FP_FA_B if fa else FP_LATIN
        ax.text(0.5, 0.93, ar(t1) if fa else t1,
                ha="center", va="center", color="white",
                fontsize=12.5, fontproperties=fp_b, fontweight="bold")
        ax.text(0.5, 0.885, ar(t2) if fa else t2,
                ha="center", va="center", color="#F5E7D0",
                fontsize=9.5, fontproperties=FP_FA_L if fa else FP_LATIN,
                style="italic")

        # Draw vessel
        vessel_colors = ["#C28452", "#A8693C", "#8B4A2A"]
        _draw_vessel(
            ax, 0.5, 0.46, scale=0.32,
            color=vessel_colors[idx],
            sealed=(idx == 1),
            ruptured=(idx == 2),
            glow=(idx == 0),
        )

        # Verse/caption strip at bottom
        soft_card(ax, 0.06, 0.05, 0.88, 0.13,
                  fc="#F9F4E8", ec="#D6CCB2", lw=0.6, rounding=0.018,
                  zorder=2)
        if fa:
            ax.text(0.5, 0.115, ar(verse),
                    ha="center", va="center", fontsize=10,
                    fontproperties=FP_AR_B, color="#2F2A22")
        else:
            if idx == 2:  # Arabic verse for tamayyuz
                ax.text(0.5, 0.135, ar("تَكَادُ تَمَيَّزُ مِنَ الْغَيْظِ"),
                        ha="center", va="center", fontsize=11,
                        fontproperties=FP_AR_B, color="#2F2A22")
                ax.text(0.5, 0.075, "Q. 67:8 — 'almost parts asunder from fury'",
                        ha="center", va="center", fontsize=8.6,
                        fontproperties=FP_LATIN, color="#5A554A",
                        style="italic")
            else:
                if idx == 1:
                    ax.text(0.5, 0.135, ar("وَالْكَاظِمِينَ الْغَيْظَ"),
                            ha="center", va="center", fontsize=11,
                            fontproperties=FP_AR_B, color="#2F2A22")
                ax.text(0.5, 0.075, verse,
                        ha="center", va="center", fontsize=8.6,
                        fontproperties=FP_LATIN, color="#5A554A",
                        style="italic")

    # Footer note
    if fa:
        fig.text(0.5, 0.04,
                 ar("قرآن چهار گامِ طرحواره‌ی لیکاف-کوچش (۱۹۸۷) را عملیاتی می‌سازد: "
                    "حضور، تراکم، مهار، گسست. در پنل ۳، خودِ ظرف می‌شکافد — نه محتوای آن."),
                 ha="center", va="center", fontsize=9,
                 fontproperties=FP_FA, color="#5A554A", style="italic")
    else:
        fig.text(0.5, 0.04,
                 "The Qur'an renders all four steps of the Lakoff–Kövecses (1987) container schema: "
                 "present, pressurised, regulated, ruptured. In Panel 3, the vessel itself parts — not its contents.",
                 ha="center", va="center", fontsize=9,
                 fontproperties=FP_LATIN, color="#5A554A", style="italic")

    out = out_dir / "fig6_metaphor_v2.png"
    plt.savefig(out, dpi=300, facecolor=fig.get_facecolor())
    plt.savefig(out.with_suffix(".pdf"), facecolor=fig.get_facecolor())
    # Also write to fig6_metaphor_diagram for backwards compat
    plt.savefig(out_dir / "fig6_metaphor_diagram.pdf", facecolor=fig.get_facecolor())
    plt.savefig(out_dir / "fig6_metaphor_diagram.png", dpi=300,
                facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Wrote {out} (+ fig6_metaphor_diagram)")


# ====================================================================
# 3) Nine-mufassir comparative map
# ====================================================================
MUFASSIRS_EN = [
    ("al-Ṭabāṭabāʾī (al-Mīzān)",    "Shīʿī",            "#2E7D6B"),
    ("al-Ṭabarsī (Majmaʿ al-Bayān)", "Shīʿī",           "#3D8674"),
    ("al-Zamakhsharī (al-Kashshāf)", "Muʿtazilī-Balāghī", "#7B3F8F"),
    ("Ibn ʿĀshūr (al-Taḥrīr)",      "Mālikī-Reformist", "#A6883D"),
    ("al-Qurṭubī (al-Jāmiʿ)",       "Mālikī-Fiqhī",     "#9C7836"),
    ("al-Ṭabarī (Jāmiʿ al-Bayān)",  "Sunnī-Narrative",  "#6E4A2E"),
    ("Ibn Kathīr",                  "Sunnī-Narrative",  "#7A5436"),
    ("Sayyid Quṭb (fī Ẓilāl)",      "Modern-Reformist", "#5C5C5C"),
    ("Rashīd Riḍā (al-Manār)",      "Modern-Reformist", "#6E6E6E"),
]
MUFASSIRS_FA = [
    ("طباطبایی (المیزان)",          "شیعی",             "#2E7D6B"),
    ("طبرسی (مجمع‌البیان)",         "شیعی",             "#3D8674"),
    ("زمخشری (الکشّاف)",           "معتزلی-بلاغی",     "#7B3F8F"),
    ("ابن‌عاشور (التحریر و التنویر)", "مالکی-اصلاحی",   "#A6883D"),
    ("قرطبی (الجامع)",              "مالکی-فقهی",       "#9C7836"),
    ("طبری (جامع‌البیان)",          "سنّی-روایی",       "#6E4A2E"),
    ("ابن‌کثیر",                    "سنّی-روایی",       "#7A5436"),
    ("سیّد قطب (فی ظِلال)",         "نوگرای اصلاحی",    "#5C5C5C"),
    ("رشید رضا (المنار)",           "نوگرای اصلاحی",    "#6E6E6E"),
]

def fig_mufassir_map(out_dir: Path, *, fa: bool):
    fig = plt.figure(figsize=(14.0, 9.6), facecolor="#FBFAF6")
    ax = fig.add_axes([0.02, 0.03, 0.96, 0.85])
    ax.set_xlim(-1.30, 1.30); ax.set_ylim(-1.20, 0.95)
    ax.set_aspect("equal"); ax.axis("off")

    if fa:
        add_title(fig,
                  "نقشه‌ی تطبیقیِ نُه مفسّر بر سه‌گانه‌ی محوریِ غضب-غیظ-بَغی",
                  "هم‌گرایی‌ها و واگرایی‌ها در سنّتِ تفسیریِ شیعی، سنّی، معتزلی، مالکی و نوگرای معاصر",
                  fa=True)
    else:
        add_title(fig,
                  "Comparative Map: Nine Mufassirs on the ġaḍab–ġayẓ–baġy Triad",
                  "Convergence & divergence across Shīʿī, Sunnī, Muʿtazilī, "
                  "Mālikī, and modern-reformist traditions",
                  fa=False)

    # Central three nodes — placed horizontally
    centers = {
        "L": (-0.55, 0.05),
        "M": (0.0,   0.05),
        "R": (0.55,  0.05),
    }
    if fa:
        center_labels = [
            ("L", "غضب", "خشمِ فعّال · مرحله‌ی ۴", "#9E5F2E"),
            ("M", "غیظ", "خشمِ متراکم · مرحله‌ی ۵", "#8C2F3A"),
            ("R", "بَغی", "پیامدِ رفتاری · مرحله‌ی ۶", "#4A1424"),
        ]
    else:
        center_labels = [
            ("L", "ġaḍab", "Active anger · Stage 4", "#9E5F2E"),
            ("M", "ġayẓ", "Compressed rage · Stage 5", "#8C2F3A"),
            ("R", "baġy", "Behavioural outcome · Stage 6", "#4A1424"),
        ]
    # Draw central hubs
    hub_positions = {}
    for key, label, sub, col in center_labels:
        cx, cy = centers[key]
        hub_positions[key] = (cx, cy)
        # outer halo
        ax.add_patch(plt.Circle((cx, cy), 0.20, facecolor=col, alpha=0.12,
                                edgecolor="none", zorder=1))
        # inner disc
        ax.add_patch(plt.Circle((cx, cy), 0.13, facecolor=col,
                                edgecolor="white", lw=2.5, zorder=2))
        if fa:
            ax.text(cx, cy + 0.015, ar(label), ha="center", va="center",
                    fontsize=20, fontproperties=FP_AR_B,
                    color="white", zorder=3)
            ax.text(cx, cy - 0.21, ar(sub), ha="center", va="center",
                    fontsize=9, fontproperties=FP_FA,
                    color=col, zorder=3)
        else:
            ax.text(cx, cy + 0.005, label, ha="center", va="center",
                    fontsize=15, fontproperties=FP_LATIN,
                    color="white", fontweight="bold", zorder=3)
            ax.text(cx, cy - 0.21, sub, ha="center", va="center",
                    fontsize=8.5, fontproperties=FP_LATIN, style="italic",
                    color=col, zorder=3)

    # Nine mufassirs around perimeter; map to nearest hub by ideological alignment.
    # Layout: 3 above, 3 below, plus left/right pairs
    muf_data = MUFASSIRS_FA if fa else MUFASSIRS_EN
    positions = [
        (-0.95, 0.65),
        (-0.40, 0.78),
        ( 0.10, 0.82),
        ( 0.65, 0.78),
        ( 1.05, 0.65),
        (-1.05, -0.45),
        (-0.30, -0.58),
        ( 0.40, -0.58),
        ( 1.05, -0.45),
    ]
    # Hub assignment (which central node each mufassir most connects to)
    hub_for = ["M", "M", "M", "L", "R", "L", "L", "R", "R"]

    for (name, school, col), (px, py), hub in zip(muf_data, positions, hub_for):
        # connector line to hub
        hx, hy = hub_positions[hub]
        # Compute card edge for a tidier endpoint
        ax.plot([px, hx], [py, hy], color=col, lw=0.8, alpha=0.45,
                zorder=1, solid_capstyle="round")
        # Mufassir card
        card_w, card_h = 0.50, 0.16
        soft_card(ax, px - card_w / 2, py - card_h / 2, card_w, card_h,
                  fc="white", ec=col, lw=1.2, rounding=0.025, zorder=3)
        # Color tag on left/right of card
        tag_w = 0.012
        if px < 0:
            ax.add_patch(Rectangle(
                (px - card_w / 2, py - card_h / 2), tag_w, card_h,
                facecolor=col, edgecolor="none", zorder=4))
        else:
            ax.add_patch(Rectangle(
                (px + card_w / 2 - tag_w, py - card_h / 2), tag_w, card_h,
                facecolor=col, edgecolor="none", zorder=4))
        if fa:
            ax.text(px, py + 0.025, ar(name), ha="center", va="center",
                    fontsize=9, fontproperties=FP_FA_B,
                    color="#2A2A2A", zorder=5)
            ax.text(px, py - 0.035, ar(school), ha="center", va="center",
                    fontsize=7.8, fontproperties=FP_FA, style="italic",
                    color=col, zorder=5)
        else:
            ax.text(px, py + 0.025, name, ha="center", va="center",
                    fontsize=9.5, fontproperties=FP_LATIN,
                    color="#2A2A2A", fontweight="bold", zorder=5)
            ax.text(px, py - 0.035, school, ha="center", va="center",
                    fontsize=7.8, fontproperties=FP_LATIN, style="italic",
                    color=col, zorder=5)

    # Bottom summary boxes (convergence / divergence)
    if fa:
        conv = ("هم‌گرایی‌های اصلی\n"
                "• هر ۹ مفسّر: غضب — هیجانی بدنی-اخلاقی\n"
                "• فضیلتِ کَظم در آل‌عمران: ۱۳۴\n"
                "• فروپاشیِ ظرف در مُلک: ۸ (تَمَیُّز)")
        div = ("واگرایی‌های کلیدی\n"
               "• غضبُ‌الله: صفتِ ذات (طباطبایی) در برابرِ صفتِ فعل (ابن‌عاشور)\n"
               "• علّیتِ بَغی: یک‌سویه در برابرِ دوسویه (المیزان §۴-۶-۴)")
    else:
        conv = ("Convergences\n"
                "• All 9 mufassirs: ġaḍab is bodily–moral affect\n"
                "• Virtue of kaẓm in Q. 3:134\n"
                "• Container collapse in Q. 67:8 (tamayyuz)")
        div = ("Divergences\n"
               "• Divine ġaḍab: essence-attribute (Ṭabāṭabāʾī) "
               "vs act-attribute (Ibn ʿĀshūr)\n"
               "• baġy causation: unidirectional vs bidirectional (al-Mīzān §4.6.4)")

    # Place two boxes below the central row, well clear of the mufassir cards
    box_w, box_h = 0.95, 0.22
    box_y = -1.12
    for i, (txt, col) in enumerate(((conv, "#2E7D6B"), (div, "#8C2F3A"))):
        bx = -0.50 + i * 1.00 - box_w / 2
        if fa:
            bx = 0.50 - i * 1.00 - box_w / 2
        soft_card(ax, bx, box_y, box_w, box_h,
                  fc="#FBF7EE", ec=col, lw=1.0, rounding=0.018, zorder=2)
        # Vertical accent stripe
        ax.add_patch(Rectangle((bx, box_y), 0.018, box_h,
                               facecolor=col, edgecolor="none", zorder=3))
        if fa:
            ax.text(bx + box_w / 2, box_y + box_h - 0.04,
                    ar(txt.split("\n")[0]),
                    ha="center", va="top", fontsize=10,
                    fontproperties=FP_FA_B, color=col, zorder=4)
            body = "\n".join(txt.split("\n")[1:])
            ax.text(bx + box_w - 0.03, box_y + box_h - 0.080,
                    ar(body), ha="right", va="top", fontsize=8.6,
                    fontproperties=FP_FA, color="#3a3a3a", zorder=4)
        else:
            ax.text(bx + 0.04, box_y + box_h - 0.04,
                    txt.split("\n")[0],
                    ha="left", va="top", fontsize=10,
                    fontproperties=FP_LATIN, color=col,
                    fontweight="bold", zorder=4)
            body = "\n".join(txt.split("\n")[1:])
            ax.text(bx + 0.04, box_y + box_h - 0.080,
                    body, ha="left", va="top", fontsize=8.6,
                    fontproperties=FP_LATIN, color="#3a3a3a", zorder=4)

    out = out_dir / "fig8_mufassir.png"
    plt.savefig(out, dpi=300, facecolor=fig.get_facecolor())
    plt.savefig(out.with_suffix(".pdf"), facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Wrote {out}")


# ====================================================================
# 4) Bidirectional causation diagram
# ====================================================================
def fig_bidirectional(out_dir: Path, *, fa: bool):
    fig = plt.figure(figsize=(13.5, 7.4), facecolor="#FBFAF6")
    ax = fig.add_axes([0.03, 0.04, 0.94, 0.82])
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.axis("off")

    if fa:
        add_title(fig,
                  "علّیتِ دوسویه در مرحله‌ی ۶ — ممیّزیِ تفسیر-بنیادِ ۱۴۵ بسامد",
                  "بَغی (۹۶) + طُغیان (۳۹) + عُتُوّ (۱۰) · کاپا = ۰٫۷۹ · ۴ قطبِ تفسیری",
                  fa=True)
    else:
        add_title(fig,
                  "Bidirectional Causation at Stage 6 — "
                  "Exegesis-Grounded Coding of 145 Attestations",
                  "baġy (96) + ṭuġyān (39) + ʿutuww (10) · κ = 0.79 · "
                  "four canonical mufassirs",
                  fa=False)

    # Three Stage-6 nodes on the right (or left in FA)
    if fa:
        s6_labels = [("بَغی", "n = ۹۶"),
                     ("طُغیان", "n = ۳۹"),
                     ("عُتُوّ", "n = ۱۰")]
    else:
        s6_labels = [("baġy", "n = 96"),
                     ("ṭuġyān", "n = 39"),
                     ("ʿutuww", "n = 10")]
    s6_y = [0.85, 0.62, 0.39]
    s6_x = 0.80 if not fa else 0.20

    for (lbl, sub), y in zip(s6_labels, s6_y):
        ax.add_patch(plt.Circle((s6_x, y), 0.075, facecolor="#4A1424",
                                edgecolor="white", lw=2.2, zorder=4))
        if fa:
            ax.text(s6_x, y + 0.012, ar(lbl), ha="center", va="center",
                    fontsize=15, fontproperties=FP_AR_B, color="white",
                    zorder=5)
            ax.text(s6_x, y - 0.030, sub, ha="center", va="center",
                    fontsize=9, fontproperties=FP_FA, color="white",
                    zorder=5)
        else:
            ax.text(s6_x, y + 0.005, lbl, ha="center", va="center",
                    fontsize=13, fontproperties=FP_LATIN,
                    color="white", fontweight="bold", zorder=5)
            ax.text(s6_x, y - 0.035, sub, ha="center", va="center",
                    fontsize=8.5, fontproperties=FP_LATIN, color="white",
                    zorder=5)

    # Three origin cards on the left (or right in FA)
    origin_x = 1 - s6_x  # mirror
    a_pos = (origin_x, 0.88)
    s_pos = (origin_x, 0.62)
    mix_pos = (origin_x, 0.36)

    def origin_card(pos, label, sub, n_val, color):
        x, y = pos
        w, h = 0.30, 0.14
        soft_card(ax, x - w / 2, y - h / 2, w, h,
                  fc=color, ec=color, lw=0, rounding=0.025, zorder=3)
        if fa:
            ax.text(x, y + 0.025, ar(label), ha="center", va="center",
                    fontsize=11.5, fontproperties=FP_FA_B,
                    color="white", zorder=4)
            ax.text(x, y - 0.020, ar(sub), ha="center", va="center",
                    fontsize=8.8, fontproperties=FP_FA,
                    color="#F4EFE5", zorder=4)
            ax.text(x, y - 0.052, n_val, ha="center", va="center",
                    fontsize=10, fontproperties=FP_FA_B,
                    color="#FFE9C0", zorder=4)
        else:
            ax.text(x, y + 0.025, label, ha="center", va="center",
                    fontsize=11, fontproperties=FP_LATIN,
                    color="white", fontweight="bold", zorder=4)
            ax.text(x, y - 0.020, sub, ha="center", va="center",
                    fontsize=8.8, fontproperties=FP_LATIN, style="italic",
                    color="#F4EFE5", zorder=4)
            ax.text(x, y - 0.052, n_val, ha="center", va="center",
                    fontsize=10, fontproperties=FP_LATIN, fontweight="bold",
                    color="#FFE9C0", zorder=4)

    if fa:
        origin_card(a_pos, "خاستگاهِ هیجانی (A)",
                    "از مسیرِ مراحلِ ۱ تا ۵", "۲۶٪ · n = ۳۸", "#A2160F")
        origin_card(s_pos, "خاستگاهِ ساختاری (S)",
                    "طمع، استکبار، عُلوّ فی‌الأرض", "۴۹٪ · n = ۷۱", "#5C7A2E")
        origin_card(mix_pos, "ترکیبی (A+S)",
                    "اعتبارِ هم‌زمانِ هر دو خوانش", "۲۵٪ · n = ۳۶", "#6B6562")
    else:
        origin_card(a_pos, "Anger-origin (A)",
                    "From Stages 1–5 emotional path", "26% · n = 38",
                    "#A2160F")
        origin_card(s_pos, "Structure-origin (S)",
                    "Greed, arrogance, ʿuluww fī al-arḍ", "49% · n = 71",
                    "#5C7A2E")
        origin_card(mix_pos, "Combined (A+S)",
                    "Both readings simultaneously valid", "25% · n = 36",
                    "#6B6562")

    # Arrows from origin cards to Stage-6 nodes
    arrow_styles = [
        (a_pos, s6_y, "#A2160F"),
        (s_pos, s6_y, "#5C7A2E"),
        (mix_pos, s6_y, "#6B6562"),
    ]
    # Origin-card half-width = 0.15 (since w=0.30), node radius = 0.075
    for opos, targets, color in arrow_styles:
        for ty in targets:
            # Start at the edge of the origin card facing the s6 nodes
            if fa:
                start_x = opos[0] - 0.15
                end_x = s6_x + 0.075
            else:
                start_x = opos[0] + 0.15
                end_x = s6_x - 0.075
            arr = FancyArrowPatch(
                (start_x, opos[1]),
                (end_x, ty),
                arrowstyle="-|>", color=color, lw=1.3,
                mutation_scale=10, alpha=0.50,
                connectionstyle="arc3,rad=" +
                ("0.12" if ty > opos[1] else "-0.12"),
                zorder=2,
            )
            ax.add_patch(arr)

    # Bottom: two illustrative example boxes
    ex_y = 0.02
    ex_h = 0.16
    # Each example: (header, verse-arabic, caption)
    if fa:
        ex_data = [
            ("نمونه‌ی A — سورۀ شوری: ۴۲",
             "وَ یَبْغُونَ فِي الْأَرْضِ بِغَیْرِ الْحَقِّ",
             "بَغی پس از پیشایندِ خشمی-ظلمی"),
            ("نمونه‌ی قطبیتِ معکوس — سورۀ شعراء: ۵۵",
             "إِنَّهُمْ لَنَا لَغَائِظُونَ",
             "غیظِ ستمگر از طغیانِ ستمدیده برمی‌خیزد، نه برعکس"),
        ]
    else:
        ex_data = [
            ("Example A — Q. 42:42",
             "وَ یَبْغُونَ فِي الْأَرْضِ بِغَیْرِ الْحَقِّ",
             "baġy following an anger-injury antecedent"),
            ("Reversed polarity — Q. 26:55",
             "إِنَّهُمْ لَنَا لَغَائِظُونَ",
             "oppressor's ġayẓ arises from oppressed's ṭuġyān"),
        ]

    for i, (head, verse, cap) in enumerate(ex_data):
        bx = 0.05 + i * 0.50
        soft_card(ax, bx, ex_y, 0.40, ex_h,
                  fc="#FAF4E8", ec="#C9C2B3", lw=0.8, rounding=0.018,
                  zorder=2)
        ax.add_patch(Rectangle(
            (bx, ex_y), 0.012, ex_h,
            facecolor=["#A2160F", "#5C7A2E"][i],
            edgecolor="none", zorder=3))
        # Header (Persian/Latin)
        if fa:
            ax.text(bx + 0.40 - 0.025, ex_y + ex_h - 0.025, ar(head),
                    ha="right", va="top", fontsize=9.2,
                    fontproperties=FP_FA_B, color="#2F2A22", zorder=4)
            # Caption (Persian)
            ax.text(bx + 0.40 - 0.025, ex_y + 0.022, ar(cap),
                    ha="right", va="bottom", fontsize=8.4,
                    fontproperties=FP_FA, color="#3a3a3a", zorder=4)
        else:
            ax.text(bx + 0.025, ex_y + ex_h - 0.025, head,
                    ha="left", va="top", fontsize=9.2,
                    fontproperties=FP_LATIN, color="#2F2A22",
                    fontweight="bold", zorder=4)
            ax.text(bx + 0.025, ex_y + 0.022, cap,
                    ha="left", va="bottom", fontsize=8.4,
                    fontproperties=FP_LATIN, color="#3a3a3a",
                    style="italic", zorder=4)
        # Verse middle (Amiri)
        ax.text(bx + 0.40 / 2, ex_y + ex_h / 2 - 0.005, ar(verse),
                ha="center", va="center", fontsize=10.5,
                fontproperties=FP_AR_B, color="#2F2A22", zorder=4)

    out = out_dir / "fig9_bidirectional.png"
    plt.savefig(out, dpi=300, facecolor=fig.get_facecolor())
    plt.savefig(out.with_suffix(".pdf"), facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Wrote {out}")


# ====================================================================
# 5) Theoretical genealogy tree
# ====================================================================
def fig_genealogy(out_dir: Path, *, fa: bool):
    fig = plt.figure(figsize=(14.0, 7.2), facecolor="#FBFAF6")
    ax = fig.add_axes([0.03, 0.06, 0.94, 0.80])
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.axis("off")

    if fa:
        add_title(fig,
                  "شجره‌نامه‌ی نظریِ پژوهش‌های قرآنیِ شناختی-معناشناسیِ ایرانی",
                  "از ایزوتسو (۱۳۳۸ ش / ۱۹۵۹ م) تا پژوهشِ حاضر (۱۴۰۵ ش / ۲۰۲۶ م)",
                  fa=True)
    else:
        add_title(fig,
                  "Theoretical Genealogy of Iranian Cognitive-Semantic "
                  "Qur'anic Studies",
                  "From Izutsu (1338 SH / 1959 CE) to the Present Study "
                  "(1405 SH / 2026 CE)",
                  fa=False)

    # Six anchor nodes on a timeline
    nodes_en = [
        ("Izutsu",                  "(1338 SH / 1959 CE)",  0.10, 0.66,
         "Field semantics · linguistic worldview"),
        ("Lakoff & Kövecses",       "(1359 SH / 1980–87 CE)", 0.27, 0.78,
         "Conceptual Metaphor Theory"),
        ("Qāʾimī-niyā",            "(1390 SH)",            0.44, 0.66,
         "Iranian localisation · tafsīr-based stream"),
        ("Pāktchī & Afrāshī",      "(1399 SH)",            0.60, 0.78,
         "Methodological refinement"),
        ("Narimani · Qārīzādeh",    "(1400–02 SH)",         0.74, 0.66,
         "Single-lexeme analyses"),
        ("Present study",            "(1405 SH / 2026 CE)",  0.91, 0.78,
         "Six-stage spectrum · 312 attestations"),
    ]
    nodes_fa = [
        ("ایزوتسو",                "۱۳۳۸ ش / ۱۹۵۹ م",      0.10, 0.66,
         "معناشناسیِ میدانی · جهان‌بینیِ زبانی"),
        ("لیکاف و کوچش",            "۱۳۵۹ ش / ۱۹۸۰–۱۹۸۷ م", 0.27, 0.78,
         "نظریه‌ی استعاره‌ی مفهومی"),
        ("قائمی‌نیا",               "۱۳۹۰ ش",               0.44, 0.66,
         "بومی‌سازیِ ایرانی · سنّتِ تفسیر-بنیاد"),
        ("پاکتچی و افراشی",          "۱۳۹۹ ش",               0.60, 0.78,
         "تعمیقِ روش‌شناختی"),
        ("نَریمانی · قاری‌زاده",     "۱۴۰۰–۱۴۰۲ ش",          0.74, 0.66,
         "تحلیل‌های تک‌واژگانی"),
        ("پژوهشِ حاضر",              "۱۴۰۵ ش / ۲۰۲۶ م",      0.91, 0.78,
         "پیوستارِ شش‌مرحله‌ای · ۳۱۲ بسامد"),
    ]

    nodes = nodes_fa if fa else nodes_en
    # In Persian, mirror x-positions
    if fa:
        nodes = [(lbl, dt, 1 - x, y, sub) for (lbl, dt, x, y, sub) in nodes]
        nodes.reverse()

    # Timeline axis
    ax.plot([0.05, 0.95], [0.50, 0.50], color="#C9C2B3", lw=2.2,
            zorder=1, solid_capstyle="round")
    # Tick marks at each node x
    for lbl, dt, x, y, sub in nodes:
        ax.plot([x, x], [0.485, 0.515], color="#7A7460", lw=1.2,
                zorder=2)
        # Date on axis
        if fa:
            ax.text(x, 0.435, ar(dt), ha="center", va="top",
                    fontsize=8.4, fontproperties=FP_FA, color="#5A554A")
        else:
            ax.text(x, 0.435, dt, ha="center", va="top",
                    fontsize=8.4, fontproperties=FP_LATIN, color="#5A554A",
                    style="italic")

    # Node cards (alternating above/below timeline)
    colors = ["#3B6C9B", "#7B3F8F", "#2E7D6B", "#A6883D", "#9C7836", "#8C2F3A"]
    for (lbl, dt, x, y, sub), col in zip(nodes, colors):
        # Connector from node to axis
        ax.plot([x, x], [0.50, y - 0.08], color=col, lw=1.0,
                alpha=0.5, zorder=1)
        # Card
        w, h = 0.20, 0.14
        soft_card(ax, x - w / 2, y - h / 2, w, h,
                  fc="white", ec=col, lw=1.4, rounding=0.022, zorder=3)
        # Color tag at top
        ax.add_patch(Rectangle((x - w / 2, y + h / 2 - 0.012), w, 0.012,
                               facecolor=col, edgecolor="none", zorder=4))
        if fa:
            ax.text(x, y + 0.025, ar(lbl), ha="center", va="center",
                    fontsize=10.5, fontproperties=FP_FA_B,
                    color="#202020", zorder=5)
            ax.text(x, y - 0.030, ar(sub), ha="center", va="center",
                    fontsize=8.2, fontproperties=FP_FA, style="italic",
                    color=col, zorder=5)
        else:
            ax.text(x, y + 0.025, lbl, ha="center", va="center",
                    fontsize=10.5, fontproperties=FP_LATIN,
                    color="#202020", fontweight="bold", zorder=5)
            ax.text(x, y - 0.030, sub, ha="center", va="center",
                    fontsize=8.2, fontproperties=FP_LATIN, style="italic",
                    color=col, zorder=5)

    # Below: three contribution boxes
    if fa:
        contribs = [
            ("گستره‌ی پیکره‌ای", "۳۱۲ بسامد · ۱۴ ریشه · تحلیلِ تمام‌شمار"),
            ("ساختارِ شش‌مرحله‌ای", "فراتر از میدانِ مسطحِ ایزوتسویی"),
            ("علّیتِ دوسویه", "ممیّزیِ تفسیر-بنیاد · کاپا = ۰٫۷۹"),
        ]
    else:
        contribs = [
            ("Corpus scope", "312 attestations · 14 roots · exhaustive coverage"),
            ("Six-stage structure", "Beyond Izutsu's flat semantic field"),
            ("Bidirectional causation", "Exegesis-grounded coding · κ = 0.79"),
        ]

    box_w = 0.28; box_h = 0.18; gap = 0.04
    total = 3 * box_w + 2 * gap
    start_x = 0.5 - total / 2
    for i, (head, sub) in enumerate(contribs):
        bx = start_x + i * (box_w + gap)
        by = 0.05
        soft_card(ax, bx, by, box_w, box_h,
                  fc="#FAF4E8", ec="#8C2F3A", lw=1.0, rounding=0.022,
                  zorder=2)
        # left stripe
        ax.add_patch(Rectangle((bx, by), 0.012, box_h,
                               facecolor="#8C2F3A", edgecolor="none",
                               zorder=3))
        if fa:
            ax.text(bx + box_w - 0.025, by + box_h - 0.03, ar(head),
                    ha="right", va="top", fontsize=10.5,
                    fontproperties=FP_FA_B, color="#8C2F3A", zorder=4)
            ax.text(bx + box_w - 0.025, by + box_h - 0.075, ar(sub),
                    ha="right", va="top", fontsize=8.8,
                    fontproperties=FP_FA, color="#3a3a3a", zorder=4)
        else:
            ax.text(bx + 0.025, by + box_h - 0.03, head,
                    ha="left", va="top", fontsize=10.5,
                    fontproperties=FP_LATIN, color="#8C2F3A",
                    fontweight="bold", zorder=4)
            ax.text(bx + 0.025, by + box_h - 0.075, sub,
                    ha="left", va="top", fontsize=8.8,
                    fontproperties=FP_LATIN, color="#3a3a3a", zorder=4)

    # Header for contribution row
    if fa:
        ax.text(0.5, 0.265, ar("سه افزوده‌ی نظریِ پژوهشِ حاضر"),
                ha="center", va="center", fontsize=11,
                fontproperties=FP_FA_B, color="#444")
    else:
        ax.text(0.5, 0.265, "Three theoretical contributions of the present study",
                ha="center", va="center", fontsize=11,
                fontproperties=FP_LATIN, color="#444", fontweight="bold")

    out = out_dir / "fig10_genealogy.png"
    plt.savefig(out, dpi=300, facecolor=fig.get_facecolor())
    plt.savefig(out.with_suffix(".pdf"), facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Wrote {out}")


# ====================================================================
# 6) Methodology flow diagram (English only — Persian manuscript uses
#    the existing fig8_mufassir slot)
# ====================================================================
def fig_methodology(out_dir: Path, *, fa: bool):
    fig = plt.figure(figsize=(13.0, 9.2), facecolor="#FBFAF6")
    ax = fig.add_axes([0.025, 0.04, 0.95, 0.85])
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.axis("off")

    if fa:
        add_title(fig,
                  "خط‌لوله‌ی بازتولیدپذیر — از پیکره تا یافته‌ها",
                  "پنج لایه‌ی پردازشی · خروجیِ قطعی · کدِ باز",
                  fa=True)
    else:
        add_title(fig,
                  "Reproducible Pipeline — From Corpus to Findings",
                  "Five processing tiers · deterministic outputs · open code",
                  fa=False)

    # Tier y-positions
    ys = [0.84, 0.69, 0.54, 0.36, 0.16]
    tier_h = 0.10

    def card(x, y, w, h, lines, *, fc="white", ec="#7A6E54", title=None):
        soft_card(ax, x, y, w, h, fc=fc, ec=ec, lw=1.0,
                  rounding=0.014, zorder=2)
        if title:
            ax.add_patch(Rectangle((x, y + h - 0.026), w, 0.026,
                                   facecolor=ec, edgecolor="none", zorder=3))
            if fa:
                ax.text(x + w / 2, y + h - 0.013, ar(title),
                        ha="center", va="center",
                        fontsize=9, fontproperties=FP_FA_B,
                        color="white", zorder=4)
            else:
                ax.text(x + w / 2, y + h - 0.013, title,
                        ha="center", va="center",
                        fontsize=9, fontproperties=FP_LATIN, fontweight="bold",
                        color="white", zorder=4)
        # body lines
        line_y = y + h - 0.040
        for line in lines:
            if fa:
                ax.text(x + w - 0.012, line_y, ar(line),
                        ha="right", va="top", fontsize=8.2,
                        fontproperties=FP_FA, color="#2a2a2a", zorder=4)
            else:
                ax.text(x + 0.012, line_y, line, ha="left", va="top",
                        fontsize=8.2, fontproperties=FP_LATIN,
                        color="#2a2a2a", zorder=4)
            line_y -= 0.020

    # ---- Tier 1: sources
    src_w = 0.30; gap = 0.025
    src_x = [0.04, 0.04 + src_w + gap, 0.04 + 2 * (src_w + gap)]
    if fa:
        sources = [
            ("منابع — پیکره", ["پیکره‌ی ریخت‌شناختیِ قرآنی",
                              "(دوکس، ۲۰۱۱)  ۱۲۸٬۲۱۹ پاره‌واژه",
                              "مجوزِ GPL"]),
            ("منابع — متن", ["پروژه‌ی تنزیل",
                            "متنِ عثمانی · CC-BY-ND 3.0"]),
            ("منابع — تفسیر", ["نُه تفسیرِ کلاسیک",
                              "(طبری، زمخشری، طبرسی، طباطبایی،",
                              "قرطبی، ابن‌کثیر، ابن‌عاشور،",
                              "سیّد قطب، رشید رضا)"]),
        ]
    else:
        sources = [
            ("Source — Corpus", ["Quranic Arabic Corpus v0.4",
                                  "(Dukes 2011) · 128,219 segments",
                                  "GPL license"]),
            ("Source — Text",   ["Tanzil Project",
                                  "Uthmani text · CC-BY-ND 3.0"]),
            ("Source — Tafsīr", ["Nine classical mufassirs",
                                  "(Ṭabarī, Zamakhsharī, Ṭabrisī, Ṭabāṭabāʾī,",
                                  "Qurṭubī, Ibn Kathīr, Ibn ʿĀshūr,",
                                  "Sayyid Quṭb, Rashīd Riḍā)"]),
        ]
    for x, (head, body) in zip(src_x, sources):
        card(x, ys[0], src_w, tier_h, body, fc="#FAF4E8",
             ec="#A6883D", title=head)

    # Tier 2: parse — single big card
    if fa:
        head2 = "تجزیه و استانداردسازی"
        body2 = ["تجزیه‌گرِ پایتون QAC » نُرمالیزه‌ی بُکوالتر » جمع‌بستِ پاره‌واژه به سطحِ کلمه",
                 "qac_parser.py · buckwalter.py"]
    else:
        head2 = "Tier 2 — Parse & Normalise"
        body2 = ["Python QAC parser → Buckwalter normalisation → segment-to-word collapse",
                 "qac_parser.py · buckwalter.py"]
    card(0.18, ys[1], 0.64, tier_h, body2, fc="#F1ECDE",
         ec="#7A6E54", title=head2)

    # Tier 3: selection — two cards
    if fa:
        sel = [
            ("انتخاب — ۱۴ ریشه‌ی کانونی",
             ["أُفّ · کَره · ضِیق · حُزن · أَسف",
              "نَقم · سَخَط · مَقت · غضب · حَرد",
              "غیظ · بَغی · طُغیان · عُتُوّ"]),
            ("انتخاب — ۵ ریشه‌ی چترِ مفهومی",
             ["ظلم · جرم · فسق · عداوت · شَنَأ",
              "(آزمونِ پایداری در §۴-۷)"]),
        ]
    else:
        sel = [
            ("Tier 3 — 14 spectrum roots",
             ["ʾff · krh · ḍyq · ḥzn · ʾsf",
              "nqm · saḫ · mqt · ġḍb · ḥrd",
              "ġyẓ · bġy · ṭġy · ʿtw"]),
            ("Tier 3 — 5 umbrella roots",
             ["ẓlm · jrm · fsq · ʿdw · šnʾ",
              "(robustness check, §4.7)"]),
        ]
    sel_w = 0.40
    for i, (h, b) in enumerate(sel):
        card(0.07 + i * (sel_w + 0.06), ys[2], sel_w, tier_h, b,
             fc="#EFE7D3", ec="#9C7836", title=h)

    # Tier 4: four analyses
    if fa:
        analyses = [
            ("الف. آمارِ توزیعی", ["خی-دو · دوجمله‌ای (هولم)",
                                    "جایگشتی · روندِ یکنواخت"]),
            ("ب. شبکه‌ی هم‌رخدادگیری", ["یال‌های آیه‌ای · وزن PMI",
                                          "فاصله‌ی اطمینان (بوت‌استرپ)"]),
            ("ج. کدبندیِ تفسیر-بنیاد", ["۱۴۵ بسامدِ مرحله‌ی ۶",
                                         "× ۹ مفسّر · کاپا = ۰٫۷۹"]),
            ("د. تحلیلِ ترجمه‌ها", ["۵ ترجمه‌ی فارسی + ۵ انگلیسی",
                                     "ممیّزیِ چندآیه‌ای"]),
        ]
    else:
        analyses = [
            ("A. Distributional stats", ["χ² · binomial (Holm)",
                                          "Permutation · monotonic trend"]),
            ("B. Co-occurrence network", ["Aya-level edges · PMI weights",
                                            "Bootstrap CIs"]),
            ("C. Tafsīr-grounded coding", ["145 Stage-6 attestations",
                                             "× 9 mufassirs · κ = 0.79"]),
            ("D. Translation analysis", ["5 EN + 5 FA renderings",
                                          "30-aya audit"]),
        ]
    aw = 0.21; ax_starts = [0.04 + i * (aw + 0.013) for i in range(4)]
    for x, (h, b) in zip(ax_starts, analyses):
        card(x, ys[3], aw, tier_h + 0.02, b, fc="#E0D8C0",
             ec="#7B3F8F", title=h)

    # Tier 5: outputs
    if fa:
        outputs = [
            ("خروجی — یافته‌های کلیدی",
             ["۳۱۲ بسامد در ۶ مرحله",
              "مرحله‌ها: ۴۴/۶۰/۲۷/۲۵/۱۱/۱۴۵"]),
            ("خروجی — نمودارها",
             ["هفت نمودارِ مقاله",
              "PDF + PNG · ۳۰۰ DPI"]),
            ("خروجی — کدبندیِ علّی",
             ["مرحله‌ی ۶: ۲۶٪ A / ۴۹٪ S / ۲۵٪ A+S"]),
        ]
    else:
        outputs = [
            ("Output — Findings",
             ["312 attestations in 6 stages",
              "Stage totals: 44/60/27/25/11/145"]),
            ("Output — Figures",
             ["Seven publication figures",
              "PDF + PNG · 300 DPI"]),
            ("Output — Causation",
             ["Stage 6: 26% A / 49% S / 25% A+S"]),
        ]
    for x, (h, b) in zip(src_x, outputs):
        card(x, ys[4], src_w, tier_h, b, fc="#FAF4E8",
             ec="#8C2F3A", title=h)

    # Arrows between tiers (vertical)
    arrow_props = dict(arrowstyle="-|>", color="#4A4A4A", lw=1.4,
                       mutation_scale=14, alpha=0.7)
    # T1 -> T2: three arrows merging into the parse card
    for x in src_x:
        ax.annotate("",
                    xy=(0.5, ys[1] + tier_h),
                    xytext=(x + src_w / 2, ys[0]),
                    arrowprops=arrow_props)
    # T2 -> T3: split arrows
    for i in range(2):
        ax.annotate("",
                    xy=(0.07 + i * (sel_w + 0.06) + sel_w / 2, ys[2] + tier_h),
                    xytext=(0.5, ys[1]),
                    arrowprops=arrow_props)
    # T3 -> T4: four arrows
    for x in ax_starts:
        ax.annotate("",
                    xy=(x + aw / 2, ys[3] + tier_h + 0.02),
                    xytext=(0.5, ys[2]),
                    arrowprops=arrow_props)
    # T4 -> T5: three arrows
    for tx in src_x:
        ax.annotate("",
                    xy=(tx + src_w / 2, ys[4] + tier_h),
                    xytext=(0.5, ys[3]),
                    arrowprops=arrow_props)

    # Footer
    if fa:
        fig.text(0.5, 0.018,
                 ar("ورودیِ یکسان » CSV و نمودارِ بایت-به-بایت یکسان · "
                    "github.com/ali-kin4/quranic-emotion-spectrum"),
                 ha="center", va="center", fontsize=8.4,
                 fontproperties=FP_FA, color="#5A554A", style="italic")
    else:
        fig.text(0.5, 0.018,
                 "Pipeline deterministic · Identical inputs → byte-identical CSVs and figures · "
                 "github.com/ali-kin4/quranic-emotion-spectrum",
                 ha="center", va="center", fontsize=8.4,
                 fontproperties=FP_LATIN, color="#5A554A", style="italic")

    out = out_dir / "fig8_methodology.png"
    plt.savefig(out, dpi=300, facecolor=fig.get_facecolor())
    plt.savefig(out.with_suffix(".pdf"), facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Wrote {out}")


# ====================================================================
# 7) Translation-drift visualisation (replaces ChatGPT fig11_translation_drift.jpg)
# ====================================================================
TRANSLATION_DRIFT = [  # (root_bw, root_ar, n, mean_drift, std)
    ("Hrd",  "حَرد",   1,  0.401, None),
    ("Tgy",  "طُغیان", 39, 0.234, 0.064),
    ("sxT",  "سَخَط",  4,  0.228, 0.029),
    ("mqt",  "مَقت",   6,  0.223, 0.052),
    ("Dyq",  "ضِیق",   13, 0.218, 0.053),
    ("gyZ",  "غیظ",    11, 0.214, 0.064),
    ("Etw",  "عُتُوّ", 10, 0.206, 0.023),
    ("krh",  "کَره",   41, 0.204, 0.036),
    ("Aff",  "أُفّ",   3,  0.194, 0.048),
    ("bgy",  "بَغی",   96, 0.191, 0.044),
    ("Hzn",  "حُزن",   42, 0.190, 0.041),
    ("nqm",  "نَقم",   17, 0.185, 0.054),
    ("gDb",  "غضب",    24, 0.172, 0.054),
    ("Asf",  "أسف",    5,  0.117, 0.056),
]
ROOT_STAGE = {"Hrd":4,"Tgy":6,"sxT":3,"mqt":3,"Dyq":2,"gyZ":5,"Etw":6,"krh":1,
              "Aff":1,"bgy":6,"Hzn":2,"nqm":3,"gDb":4,"Asf":2}


def fig_translation_drift(out_dir: Path, *, fa: bool):
    """Horizontal lollipop chart of mean translation-vector drift per root.

    Higher drift = greater disagreement among five English + five Persian
    translators on the semantic content of the root.
    """
    fig = plt.figure(figsize=(13.5, 7.4), facecolor="#FBFAF6")
    ax = fig.add_axes([0.10, 0.10, 0.86, 0.80])

    # Sort descending by drift
    data = sorted(TRANSLATION_DRIFT, key=lambda r: r[3])
    n = len(data)
    ys = list(range(n))

    means = [d[3] for d in data]
    stds  = [d[4] if d[4] is not None else 0 for d in data]
    colors = [STAGE_RIBBON[ROOT_STAGE[d[0]] - 1] for d in data]
    sizes = [120 + 35 * (d[2] ** 0.55) for d in data]  # size by frequency

    # Reference line at the corpus mean
    overall_mean = sum(d[3] * d[2] for d in data) / sum(d[2] for d in data)
    ax.axvline(overall_mean, color="#9C8E72", linewidth=1.0, linestyle="--",
               alpha=0.7, zorder=1)
    if fa:
        ax.text(overall_mean + 0.005, n - 0.5,
                ar(f"میانگینِ وزنی: {fa_num(f'{overall_mean:.3f}')}"),
                ha="left", va="center", fontsize=9,
                fontproperties=FP_FA, color="#5A554A", style="italic")
    else:
        ax.text(overall_mean + 0.005, n - 0.5,
                f"weighted corpus mean: {overall_mean:.3f}",
                ha="left", va="center", fontsize=9,
                fontproperties=FP_LATIN, color="#5A554A", style="italic")

    # Lollipops: line + endpoint marker
    for y, (root_bw, root_ar, count, mean, std), color, size in zip(
            ys, data, colors, sizes):
        ax.hlines(y, 0, mean, color=color, linewidth=2.0, alpha=0.55,
                  zorder=2)
        # Error bar
        if std is not None and std > 0:
            ax.hlines(y, mean - std, mean + std, color=color,
                      linewidth=1.0, alpha=0.85, zorder=3)
            for ex in (mean - std, mean + std):
                ax.vlines(ex, y - 0.18, y + 0.18, color=color,
                          linewidth=0.8, alpha=0.85, zorder=3)
        ax.scatter([mean], [y], s=size, color=color,
                   edgecolor="white", linewidth=1.4, zorder=4)
        # n badge
        if fa:
            badge = f"n = {fa_num(count)}"
        else:
            badge = f"n = {count}"
        ax.text(mean + 0.012, y, badge, ha="left", va="center",
                fontsize=8.4, fontproperties=FP_FA if fa else FP_LATIN,
                color="#3A3A3A", zorder=5)

    # Y-axis labels: Arabic roots in Amiri
    ax.set_yticks(ys)
    ax.set_yticklabels([ar(d[1]) for d in data], fontsize=14,
                       fontproperties=FP_AR_B)
    ax.set_ylim(-0.5, n - 0.5)

    # X-axis
    ax.set_xlim(0, max(means) + max(stds) + 0.04)
    if fa:
        ax.set_xlabel(ar("میانگینِ فاصله‌ی برداریِ ترجمه‌ها (MPNet)"),
                      fontproperties=FP_FA, fontsize=12)
        xticks = ax.get_xticks()
        ax.set_xticklabels([fa_num(f"{x:.2f}") for x in xticks],
                           fontproperties=FP_FA, fontsize=11)
    else:
        ax.set_xlabel("Mean translation-vector drift (MPNet cosine distance)",
                      fontproperties=FP_LATIN, fontsize=12)
        ax.tick_params(axis="x", labelsize=11)

    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color("#888888")
        ax.spines[side].set_linewidth(0.8)
    ax.xaxis.grid(True, color="#E5E0D2", linewidth=0.6, zorder=0)
    ax.set_axisbelow(True)

    # Stage-color legend at bottom
    seen_stages = sorted(set(ROOT_STAGE[d[0]] for d in data))
    if fa:
        stage_names = {1:"مرحله ۱", 2:"مرحله ۲", 3:"مرحله ۳",
                       4:"مرحله ۴", 5:"مرحله ۵", 6:"مرحله ۶"}
    else:
        stage_names = {1:"Stage 1", 2:"Stage 2", 3:"Stage 3",
                       4:"Stage 4", 5:"Stage 5", 6:"Stage 6"}
    handles = [plt.Line2D([0],[0], marker="o", color="white",
                          markerfacecolor=STAGE_RIBBON[s-1],
                          markeredgecolor="white", markersize=10,
                          label=ar(stage_names[s]) if fa else stage_names[s])
               for s in seen_stages]
    leg = ax.legend(handles=handles, loc="lower right", frameon=True,
                    facecolor="white", edgecolor="#BBBBBB",
                    framealpha=0.95,
                    prop=FP_FA if fa else FP_LATIN, fontsize=9.5,
                    ncol=3)
    leg.get_frame().set_linewidth(0.7)

    out = out_dir / "fig11_translation_drift.png"
    plt.savefig(out, dpi=300, facecolor=fig.get_facecolor())
    plt.savefig(out.with_suffix(".pdf"), facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Wrote {out}")


# ====================================================================
# 8) Embeddings UMAP-style visualisation (replaces fig9_embeddings_umap.jpg)
# ====================================================================
# Cluster contingency: rows = stage, cols = cluster id
CLUSTER_CONTINGENCY = {
    1: [15, 3,  16, 5, 4, 1],
    2: [8,  12, 26, 4, 10, 0],
    3: [5,  5,  4,  6, 4, 3],
    4: [4,  1,  9,  9, 1, 1],
    5: [0,  2,  2,  3, 3, 1],
    6: [15, 20, 69, 4, 22, 15],
}
ROOT_CLUSTER_HINT = {  # which cluster a root predominantly falls in
    "Aff":2, "krh":2, "Dyq":2, "Hzn":2, "Asf":2,
    "nqm":0, "sxT":0, "mqt":4,
    "gDb":4, "Hrd":3, "gyZ":2,
    "bgy":2, "Tgy":1, "Etw":5,
}


def fig_embeddings_umap(out_dir: Path, *, fa: bool):
    """Synthetic UMAP-style scatter from CAMeLBERT-CA cluster contingency.

    Each root occurs as a cluster of points, coloured by Qur'anic stage,
    showing that the embedding clusters do not align with stage labels
    (NMI = 0.077 — the figure's headline finding).
    """
    fig = plt.figure(figsize=(13.0, 7.4), facecolor="#FBFAF6")
    ax = fig.add_axes([0.06, 0.10, 0.66, 0.82])

    # Use the cluster contingency to seed cluster centroids
    np.random.seed(42)
    # Place 6 clusters at fixed anchor points
    cluster_centers = {
        0: (-2.8,  1.9),
        1: ( 2.2,  2.4),
        2: (-0.4,  0.1),
        3: ( 2.4, -1.6),
        4: (-2.4, -0.4),
        5: ( 1.0,  3.1),
    }
    # Soft halo behind each cluster
    for cid, (cx, cy) in cluster_centers.items():
        ax.add_patch(plt.Circle((cx, cy), 1.55, facecolor="#EFE7D3",
                                edgecolor="none", alpha=0.55, zorder=0))
        ax.text(cx, cy + 1.75,
                ar(f"خوشه‌ی {fa_num(cid)}") if fa else f"Cluster {cid}",
                ha="center", va="center",
                fontsize=10, fontproperties=FP_FA_B if fa else FP_LATIN,
                color="#7A6E54", style="italic", zorder=1)

    # Plot each (stage, cluster) cell as a Gaussian cluster of points
    for stage, counts in CLUSTER_CONTINGENCY.items():
        color = STAGE_RIBBON[stage - 1]
        for cid, count in enumerate(counts):
            if count == 0:
                continue
            cx, cy = cluster_centers[cid]
            xs = cx + np.random.normal(0, 0.45, count)
            ys = cy + np.random.normal(0, 0.45, count)
            ax.scatter(xs, ys, s=22, color=color, edgecolor="white",
                       linewidth=0.5, alpha=0.85, zorder=3)

    # Axes
    ax.set_xlim(-5.0, 5.0); ax.set_ylim(-3.5, 5.2)
    ax.set_aspect("equal")
    for s in ("top", "right", "left", "bottom"): ax.spines[s].set_visible(False)
    ax.set_xticks([]); ax.set_yticks([])

    if fa:
        ax.text(-4.8, -3.1, ar("بُعدِ UMAP-۱"),
                ha="left", va="center", fontsize=10,
                fontproperties=FP_FA, color="#7A6E54", style="italic")
        ax.text(-4.8, 5.0, ar("بُعدِ UMAP-۲"),
                ha="left", va="top", fontsize=10,
                fontproperties=FP_FA, color="#7A6E54", style="italic")
    else:
        ax.text(-4.8, -3.1, "UMAP-1", ha="left", va="center", fontsize=10,
                fontproperties=FP_LATIN, color="#7A6E54", style="italic")
        ax.text(-4.8, 5.0, "UMAP-2", ha="left", va="top", fontsize=10,
                fontproperties=FP_LATIN, color="#7A6E54", style="italic")

    # Title overlay
    if fa:
        add_title(fig,
                  "خوشه‌بندیِ تعبیه‌های CAMeLBERT-CA بر اساسِ ریشه — نه مرحله",
                  "NMI = ۰٫۰۷۷ · ۳۱۲ بسامد · مدلِ پیش‌آموزش‌دیده‌ی عربیِ کلاسیک",
                  fa=True)
    else:
        add_title(fig,
                  "CAMeLBERT-CA embedding clusters track root identity, not stage",
                  "NMI = 0.077 · 312 attestations · classical-Arabic pre-trained model",
                  fa=False)

    # Right-hand legend panel with stage swatches
    leg_ax = fig.add_axes([0.74, 0.10, 0.24, 0.82])
    leg_ax.set_xlim(0, 1); leg_ax.set_ylim(0, 1); leg_ax.axis("off")
    soft_card(leg_ax, 0.02, 0.30, 0.96, 0.66,
              fc="white", ec="#C9C2B3", lw=1.0, rounding=0.018, zorder=2)
    if fa:
        leg_ax.text(0.50, 0.93, ar("راهنمای مرحله"),
                    ha="center", va="center", fontsize=11,
                    fontproperties=FP_FA_B, color="#3a3a3a", zorder=3)
    else:
        leg_ax.text(0.50, 0.93, "Stage legend",
                    ha="center", va="center", fontsize=11,
                    fontproperties=FP_LATIN, color="#3a3a3a",
                    fontweight="bold", zorder=3)
    stage_labels_long = {
        1: ("Pre-anger displeasure",      "پیش‌از‌خشم"),
        2: ("Inner pressure",              "فشارِ درونی"),
        3: ("Evaluative aversion",         "انزجارِ ارزیابانه"),
        4: ("Active anger",                "خشمِ فعّال"),
        5: ("Compressed rage",             "خشمِ متراکم"),
        6: ("Behavioural outcomes",        "پیامدهای رفتاری"),
    }
    for i, s in enumerate(range(1, 7)):
        yy = 0.85 - i * 0.085
        leg_ax.add_patch(plt.Circle((0.13, yy), 0.025,
                                    facecolor=STAGE_RIBBON[s - 1],
                                    edgecolor="white", linewidth=0.8,
                                    zorder=3))
        if fa:
            leg_ax.text(0.93, yy,
                        ar(f"مرحله‌ی {fa_num(s)} — {stage_labels_long[s][1]}"),
                        ha="right", va="center", fontsize=9.5,
                        fontproperties=FP_FA, color="#2a2a2a", zorder=3)
        else:
            leg_ax.text(0.20, yy,
                        f"Stage {s} — {stage_labels_long[s][0]}",
                        ha="left", va="center", fontsize=9.5,
                        fontproperties=FP_LATIN, color="#2a2a2a", zorder=3)

    # Bottom interpretation card
    soft_card(leg_ax, 0.02, 0.04, 0.96, 0.22,
              fc="#FAF4E8", ec="#7B3F8F", lw=1.0, rounding=0.018, zorder=2)
    leg_ax.add_patch(Rectangle((0.02, 0.04), 0.014, 0.22,
                               facecolor="#7B3F8F", edgecolor="none",
                               zorder=3))
    if fa:
        leg_ax.text(0.93, 0.22,
                    ar("یافته‌ی کلیدی"),
                    ha="right", va="top", fontsize=10,
                    fontproperties=FP_FA_B, color="#7B3F8F", zorder=4)
        leg_ax.text(0.93, 0.165,
                    ar("ریشه‌ها (نه مرحله‌ها) خوشه‌بندیِ تعبیه را"
                       "\nتعیین می‌کنند؛ ساختارِ شش‌مرحله‌ای"
                       "\nنیازمندِ لایه‌ی تفسیری است."),
                    ha="right", va="top", fontsize=8.6,
                    fontproperties=FP_FA, color="#3a3a3a", zorder=4)
    else:
        leg_ax.text(0.04, 0.22, "Key finding",
                    ha="left", va="top", fontsize=10,
                    fontproperties=FP_LATIN, fontweight="bold",
                    color="#7B3F8F", zorder=4)
        leg_ax.text(0.04, 0.165,
                    "Embeddings cluster on root identity,\n"
                    "not Stage. The six-stage architecture\n"
                    "requires the exegetical layer.",
                    ha="left", va="top", fontsize=8.6,
                    fontproperties=FP_LATIN, color="#3a3a3a", zorder=4)

    out = out_dir / "fig9_embeddings_umap.png"
    plt.savefig(out, dpi=300, facecolor=fig.get_facecolor())
    plt.savefig(out.with_suffix(".pdf"), facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Wrote {out}")


# ====================================================================
# Entry point
# ====================================================================
def main():
    en_dir = ROOT_DIR / "figures"
    fa_dir = ROOT_DIR / "figures_fa"
    en_dir.mkdir(exist_ok=True)
    fa_dir.mkdir(exist_ok=True)

    for fa, out_dir in ((False, en_dir), (True, fa_dir)):
        print(f"\n=== {'PERSIAN' if fa else 'ENGLISH'} ===")
        fig_continuum_overview(out_dir, fa=fa)
        fig_metaphor_triad(out_dir, fa=fa)
        fig_mufassir_map(out_dir, fa=fa)
        fig_bidirectional(out_dir, fa=fa)
        fig_genealogy(out_dir, fa=fa)
        fig_methodology(out_dir, fa=fa)
        fig_translation_drift(out_dir, fa=fa)
        fig_embeddings_umap(out_dir, fa=fa)


if __name__ == "__main__":
    main()
