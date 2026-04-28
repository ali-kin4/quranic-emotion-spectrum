"""Generate the four publication figures.

    figures/fig1_continuum.pdf       — canonical four-stage spectrum
    figures/fig2_frequency_by_stage.pdf — frequency bars (linear & log)
    figures/fig3_meccan_medinan.pdf  — revelation-context distribution
    figures/fig4_cooccurrence.pdf    — proximity co-occurrence network

All figures use a clean academic style with Arabic text rendering.
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
from spectrum_roots import SPECTRUM, STAGE_LABELS_EN  # noqa: E402

CONC_DIR = ROOT_DIR / "data" / "concordance"
FIG_DIR = ROOT_DIR / "figures"
FIG_DIR.mkdir(exist_ok=True)


def ar(text: str) -> str:
    """Reshape and reorder an Arabic/Persian string for matplotlib rendering."""
    if not text:
        return text
    return get_display(arabic_reshaper.reshape(text))


# Academic style. Tahoma supports Arabic shaping on Windows; falls back gracefully.
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

# Colour-blind-safe stage palette
STAGE_COLORS = {
    1: "#4C72B0",  # blue   — internal distress
    2: "#DD8452",  # orange — explicit anger
    3: "#C44E52",  # red    — explosive rage
    4: "#55A868",  # green  — rebellion (deliberately distinct from anger)
}


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
    """Horizontal four-stage continuum diagram with all 10 roots."""
    fig, ax = plt.subplots(figsize=(14, 5.5))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 6.0)
    ax.axis("off")

    # Stage bands as background rectangles. Each stage gets its own header row.
    bands = [(0.5, 3.5, 1), (3.5, 5.5, 2), (5.5, 7.5, 3), (7.5, 10.5, 4)]
    for (x0, x1, st) in bands:
        ax.axhspan(1.2, 4.4, xmin=(x0 / 11), xmax=(x1 / 11),
                   facecolor=STAGE_COLORS[st], alpha=0.08, zorder=0)
        # Two-line stage label (number on top, name below)
        ax.text((x0 + x1) / 2, 5.3, f"Stage {st}",
                ha="center", va="center", fontsize=11, fontweight="bold",
                color=STAGE_COLORS[st])
        ax.text((x0 + x1) / 2, 4.85,
                STAGE_LABELS_EN[st].split(" — ")[1],
                ha="center", va="center", fontsize=9.5,
                color=STAGE_COLORS[st], style="italic")

    canonical_order = ["Dyq", "Hzn", "Asf", "sxT", "gDb", "gyZ", "myz",
                       "bgy", "Tgy", "Etw"]
    by_bw = {r["root_bw"]: r for r in rows}
    xs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for x, bw in zip(xs, canonical_order):
        rec = by_bw.get(bw)
        if not rec:
            continue
        st = rec["stage"]
        size = 380 + 90 * (rec["occurrences"] ** 0.55)
        ax.scatter(x, 2.8, s=size, color=STAGE_COLORS[st],
                   edgecolor="black", linewidth=0.8, zorder=3)
        # Surface form (Arabic) inside node
        surface = next((s.display() for s in SPECTRUM if s.bw == bw), rec["root_ar"])
        ax.text(x, 2.8, ar(surface), ha="center", va="center",
                fontsize=11.5, fontweight="bold", color="white", zorder=4)
        # Frequency below
        ax.text(x, 1.85, f"n = {rec['occurrences']}", ha="center", va="center",
                fontsize=9, color="black", zorder=4)
        # Buckwalter ID below
        ax.text(x, 1.45, f"({bw})", ha="center", va="center",
                fontsize=8, color="dimgray", zorder=4, style="italic")

    # Arrow connecting all nodes (intensification axis)
    for x0, x1 in zip(xs[:-1], xs[1:]):
        ax.annotate("", xy=(x1 - 0.3, 2.8), xytext=(x0 + 0.3, 2.8),
                    arrowprops=dict(arrowstyle="->", color="gray", lw=1.2,
                                    alpha=0.6), zorder=2)

    # Axis label
    ax.text(5.5, 0.55,
            f"Intensity of Action  →  ({ar('شدت کنش')})",
            ha="center", va="center", fontsize=11.5, fontweight="bold",
            color="black")

    ax.set_title("Figure 1.  The Quranic Spectrum of Negative Emotions — "
                 "from Internal Distress to Behavioural Rebellion\n"
                 "Node = Arabic root, size ∝ corpus frequency in the "
                 "Quranic Arabic Corpus (Dukes 2011)",
                 fontsize=11, pad=12)

    out = FIG_DIR / "fig1_continuum.pdf"
    plt.savefig(out)
    plt.savefig(out.with_suffix(".png"))
    plt.close()
    print(f"Wrote {out}")


def fig2_frequency_by_stage(rows: list[dict]) -> None:
    """Bar chart of per-root frequencies grouped by stage."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

    canonical = ["Dyq", "Hzn", "Asf", "sxT", "gDb", "gyZ", "myz",
                 "bgy", "Tgy", "Etw"]
    by_bw = {r["root_bw"]: r for r in rows}

    surface_by_bw = {r.bw: r.display() for r in SPECTRUM}
    labels = [ar(surface_by_bw[bw]) for bw in canonical]
    counts = [by_bw[bw]["occurrences"] for bw in canonical]
    colors = [STAGE_COLORS[by_bw[bw]["stage"]] for bw in canonical]

    bars = ax1.bar(range(len(canonical)), counts, color=colors,
                   edgecolor="black", linewidth=0.6)
    ax1.set_xticks(range(len(canonical)))
    ax1.set_xticklabels(labels, fontsize=12)
    ax1.set_ylabel("Occurrences in the Qur'an")
    ax1.set_title("Per-root frequency (linear scale)")
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
    ax2.set_xticklabels([f"Stage {s}\n{STAGE_LABELS_EN[s].split(' — ')[1]}"
                         for s in stages], fontsize=9)
    ax2.set_ylabel("Total occurrences")
    ax2.set_title("Stage-level totals")
    for b, s in zip(bars2, stages):
        ax2.text(b.get_x() + b.get_width() / 2,
                 stage_totals[s] + 2, str(stage_totals[s]),
                 ha="center", va="bottom", fontsize=10, fontweight="bold")

    fig.suptitle("Figure 2.  Lexical frequency of the spectrum across "
                 "the Qur'anic corpus (n = 248 hits across 10 core roots)",
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

    canonical = ["Dyq", "Hzn", "Asf", "sxT", "gDb", "gyZ", "myz",
                 "bgy", "Tgy", "Etw"]
    by_bw = {r["root_bw"]: r for r in rows}
    surface_by_bw = {r.bw: r.display() for r in SPECTRUM}
    labels = [ar(surface_by_bw[bw]) for bw in canonical]
    meccan = [by_bw[bw]["meccan_hits"] for bw in canonical]
    medinan = [by_bw[bw]["medinan_hits"] for bw in canonical]

    x = range(len(canonical))
    ax.bar(x, meccan, color="#8C7853", edgecolor="black",
           linewidth=0.5, label=f"Meccan ({ar('مکی')})")
    ax.bar(x, medinan, bottom=meccan, color="#2E86AB",
           edgecolor="black", linewidth=0.5, label=f"Medinan ({ar('مدنی')})")

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=12)
    ax.set_ylabel("Occurrences")
    ax.set_title("Figure 3.  Distribution of spectrum vocabulary across "
                 "the Meccan and Medinan corpus")
    ax.legend(loc="upper left")

    # Annotate proportions for the small-n suras
    for xi, bw in enumerate(canonical):
        rec = by_bw[bw]
        total = rec["meccan_hits"] + rec["medinan_hits"]
        if total > 0:
            mec_pct = 100 * rec["meccan_hits"] / total
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

    fig, ax = plt.subplots(figsize=(9, 8))
    pos = {
        # Hand-laid ring positions to keep stage clusters visually grouped
        "Dyq": (-2, 1.5),
        "Hzn": (-2.5, 0.5),
        "Asf": (-2, -0.5),
        "sxT": (-1, -1.7),
        "gDb": (0, -2),
        "gyZ": (1.5, -1),
        "myz": (2, 0),
        "bgy": (2.2, 1.2),
        "Tgy": (1.2, 2),
        "Etw": (-0.5, 2),
    }

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

    # Legend
    for st in (1, 2, 3, 4):
        ax.scatter([], [], color=STAGE_COLORS[st], s=120, edgecolor="black",
                   linewidth=0.5, label=STAGE_LABELS_EN[st])
    ax.legend(loc="lower right", fontsize=8)

    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-3, 3)
    ax.axis("off")
    ax.set_title("Figure 4.  Aya-level co-occurrence network of the spectrum.\n"
                 "Edge weight = number of ayat in which both roots co-occur.",
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
