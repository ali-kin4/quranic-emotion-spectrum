"""Generate the four publication figures.

    figures/fig1_continuum.pdf       — six-stage spectrum diagram
    figures/fig2_frequency_by_stage.pdf — frequency bars (linear & stage totals)
    figures/fig3_meccan_medinan.pdf  — revelation-context distribution
    figures/fig4_cooccurrence.pdf    — proximity co-occurrence network

All figures use a clean academic style with Arabic text rendering.
Revised 2026-04-29 for the six-stage anger spectrum (14 core roots).
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

STAGE_COLORS = {
    1: "#7FB3D5",  # light blue   — pre-anger displeasure
    2: "#4C72B0",  # blue         — inner pressure / contraction
    3: "#DD8452",  # orange       — evaluative aversion
    4: "#C44E52",  # red          — active anger
    5: "#8E0E25",  # dark red     — compressed rage
    6: "#55A868",  # green        — behavioural outcomes
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


def fig1_continuum(rows: list[dict]) -> None:
    fig, ax = plt.subplots(figsize=(16, 6.0))
    n = len(SPECTRUM)
    width = n + 1
    ax.set_xlim(0, width)
    ax.set_ylim(0, 6.4)
    ax.axis("off")

    by_stage: dict[int, list[int]] = defaultdict(list)
    for i, r in enumerate(SPECTRUM):
        by_stage[r.stage].append(i + 1)

    for st, xs_in_stage in sorted(by_stage.items()):
        x0 = min(xs_in_stage) - 0.5
        x1 = max(xs_in_stage) + 0.5
        ax.axhspan(1.2, 4.4, xmin=(x0 / width), xmax=(x1 / width),
                   facecolor=STAGE_COLORS[st], alpha=0.08, zorder=0)
        ax.text((x0 + x1) / 2, 5.4, f"Stage {st}",
                ha="center", va="center", fontsize=10, fontweight="bold",
                color=STAGE_COLORS[st])
        ax.text((x0 + x1) / 2, 4.95,
                STAGE_LABELS_EN[st].split(" — ")[1],
                ha="center", va="center", fontsize=8.5,
                color=STAGE_COLORS[st], style="italic")

    by_bw = {r["root_bw"]: r for r in rows}
    surface_by_bw = {r.bw: r.display() for r in SPECTRUM}

    for i, r in enumerate(SPECTRUM, start=1):
        rec = by_bw.get(r.bw)
        if rec is None:
            continue
        st = r.stage
        size = 320 + 70 * (rec["occurrences"] ** 0.55)
        ax.scatter(i, 2.8, s=size, color=STAGE_COLORS[st],
                   edgecolor="black", linewidth=0.8, zorder=3)
        ax.text(i, 2.8, ar(surface_by_bw[r.bw]), ha="center", va="center",
                fontsize=10.5, fontweight="bold", color="white", zorder=4)
        ax.text(i, 1.85, f"n = {rec['occurrences']}", ha="center", va="center",
                fontsize=8.5, color="black", zorder=4)
        # Use scientific transliteration (e.g. ʾff, ḥzn, ġḍb), not Buckwalter
        # codes (Aff, Hzn, gDb), so non-Arabist readers can decode the labels.
        ax.text(i, 1.45, f"({r.translit})", ha="center", va="center",
                fontsize=7.5, color="dimgray", zorder=4, style="italic")

    for i in range(1, n):
        ax.annotate("", xy=(i + 1 - 0.3, 2.8), xytext=(i + 0.3, 2.8),
                    arrowprops=dict(arrowstyle="->", color="gray", lw=1.0,
                                    alpha=0.55), zorder=2)

    ax.text(width / 2, 0.55,
            f"Intensity of Action  →  ({ar('شدت کنش')})",
            ha="center", va="center", fontsize=11, fontweight="bold")

    out = FIG_DIR / "fig1_continuum.pdf"
    plt.savefig(out)
    plt.savefig(out.with_suffix(".png"))
    plt.close()
    print(f"Wrote {out}")


def fig2_frequency_by_stage(rows: list[dict]) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    by_bw = {r["root_bw"]: r for r in rows}
    surface_by_bw = {r.bw: r.display() for r in SPECTRUM}

    labels = [ar(surface_by_bw[bw]) for bw in CANONICAL_ORDER]
    counts = [by_bw[bw]["occurrences"] for bw in CANONICAL_ORDER]
    colors = [STAGE_COLORS[by_bw[bw]["stage"]] for bw in CANONICAL_ORDER]

    bars = ax1.bar(range(len(CANONICAL_ORDER)), counts, color=colors,
                   edgecolor="black", linewidth=0.6)
    ax1.set_xticks(range(len(CANONICAL_ORDER)))
    ax1.set_xticklabels(labels, fontsize=10.5)
    ax1.set_ylabel("Occurrences in the Qur'an")
    ax1.set_title("Per-root frequency (linear scale)")
    for b, c in zip(bars, counts):
        ax1.text(b.get_x() + b.get_width() / 2, c + max(counts) * 0.02, str(c),
                 ha="center", va="bottom", fontsize=8.5)

    stage_totals: dict[int, int] = defaultdict(int)
    for r in rows:
        stage_totals[r["stage"]] += r["occurrences"]
    stages = sorted(stage_totals.keys())
    bars2 = ax2.bar(stages, [stage_totals[s] for s in stages],
                    color=[STAGE_COLORS[s] for s in stages],
                    edgecolor="black", linewidth=0.6)
    ax2.set_xticks(stages)
    ax2.set_xticklabels([f"S{s}: {STAGE_LABELS_EN[s].split(' — ')[1]}"
                         for s in stages], fontsize=8.5,
                        rotation=20, ha="right", rotation_mode="anchor")
    ax2.set_ylabel("Total occurrences")
    ax2.set_title("Stage-level totals")
    for b, s in zip(bars2, stages):
        ax2.text(b.get_x() + b.get_width() / 2,
                 stage_totals[s] + max(stage_totals.values()) * 0.02,
                 str(stage_totals[s]),
                 ha="center", va="bottom", fontsize=10, fontweight="bold")

    fig.tight_layout()
    out = FIG_DIR / "fig2_frequency_by_stage.pdf"
    plt.savefig(out)
    plt.savefig(out.with_suffix(".png"))
    plt.close()
    print(f"Wrote {out}")


def fig3_meccan_medinan(rows: list[dict]) -> None:
    fig, ax = plt.subplots(figsize=(13, 5))
    by_bw = {r["root_bw"]: r for r in rows}
    surface_by_bw = {r.bw: r.display() for r in SPECTRUM}
    labels = [ar(surface_by_bw[bw]) for bw in CANONICAL_ORDER]
    meccan = [by_bw[bw]["meccan_hits"] for bw in CANONICAL_ORDER]
    medinan = [by_bw[bw]["medinan_hits"] for bw in CANONICAL_ORDER]

    x = range(len(CANONICAL_ORDER))
    ax.bar(x, meccan, color="#8C7853", edgecolor="black",
           linewidth=0.5, label=f"Meccan ({ar('مکی')})")
    ax.bar(x, medinan, bottom=meccan, color="#2E86AB",
           edgecolor="black", linewidth=0.5, label=f"Medinan ({ar('مدنی')})")

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=10.5)
    ax.set_ylabel("Occurrences")
    ax.legend(loc="upper left")

    for xi, bw in enumerate(CANONICAL_ORDER):
        rec = by_bw[bw]
        total = rec["meccan_hits"] + rec["medinan_hits"]
        if total > 0:
            ax.text(xi, total + max(meccan) * 0.03,
                    f"{rec['meccan_hits']}/{rec['medinan_hits']}",
                    ha="center", va="bottom", fontsize=8, color="gray")

    fig.tight_layout()
    out = FIG_DIR / "fig3_meccan_medinan.pdf"
    plt.savefig(out)
    plt.savefig(out.with_suffix(".png"))
    plt.close()
    print(f"Wrote {out}")


def fig4_cooccurrence() -> None:
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

    # Lay out the connected component(s) with a force-directed (spring)
    # layout, then place isolated nodes (those that share no aya with any
    # other spectrum root in the QAC) in a clearly-labelled sidebar so they
    # aren't visually floating in the layout and misread as broken edges.
    connected = [n for n in G.nodes() if G.degree(n) > 0]
    isolated = [n for n in G.nodes() if G.degree(n) == 0]
    G_main = G.subgraph(connected).copy()
    if G_main.number_of_nodes() > 0:
        pos = nx.spring_layout(G_main, weight="weight", seed=42,
                               k=1.6, iterations=400)
    else:
        pos = {}
    # Stack isolated nodes on the right at fixed x, evenly distributed in y
    if isolated:
        ys = ([0.0] if len(isolated) == 1
              else [1.0 - 2.0 * i / (len(isolated) - 1)
                    for i in range(len(isolated))])
        for node, y in zip(isolated, ys):
            pos[node] = (1.55, y * 0.7)

    fig, ax = plt.subplots(figsize=(13, 9))

    if G.number_of_edges() > 0:
        max_w = max(d["weight"] for _, _, d in G.edges(data=True))
        for u, v, d in G.edges(data=True):
            ax.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]],
                    color="gray", alpha=0.25 + 0.7 * (d["weight"] / max_w),
                    linewidth=0.5 + 3.0 * (d["weight"] / max_w), zorder=1)
            mx = (pos[u][0] + pos[v][0]) / 2
            my = (pos[u][1] + pos[v][1]) / 2
            ax.text(mx, my, str(d["weight"]), fontsize=7,
                    ha="center", va="center", color="dimgray",
                    bbox=dict(boxstyle="round,pad=0.15", fc="white",
                              ec="none", alpha=0.85))

    for r in SPECTRUM:
        x, y = pos[r.bw]
        ax.scatter(x, y, s=900, color=STAGE_COLORS[r.stage],
                   edgecolor="black", linewidth=0.8, zorder=2)
        ax.text(x, y, ar(r.display()), ha="center", va="center",
                fontsize=9.5, fontweight="bold", color="white", zorder=3)

    # Label the sidebar of isolated (no co-occurrence) nodes so the visual
    # placement reads correctly rather than as a layout failure.
    if isolated:
        ax.text(1.55, 0.95,
                "no aya-level\nco-occurrence",
                ha="center", va="bottom", fontsize=8.5, style="italic",
                color="dimgray")
        ax.axvline(x=1.30, ymin=0.05, ymax=0.95, color="lightgray",
                   linestyle="--", linewidth=0.7, zorder=0)

    for st in sorted(set(r.stage for r in SPECTRUM)):
        ax.scatter([], [], color=STAGE_COLORS[st], s=120, edgecolor="black",
                   linewidth=0.5, label=STAGE_LABELS_EN[st])
    ax.legend(loc="upper left", fontsize=8, framealpha=0.92)
    ax.axis("off")

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
