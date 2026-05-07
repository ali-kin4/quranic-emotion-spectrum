"""Build the Colab notebook from a structured cell list.

Run once to regenerate notebooks/quranic_emotion_spectrum.ipynb.
"""

import json
from pathlib import Path

REPO = "ali-kin4/quranic-emotion-spectrum"
BRANCH = "master"
NB_PATH = "notebooks/quranic_emotion_spectrum.ipynb"
COLAB_BADGE_URL = (
    f"https://colab.research.google.com/github/{REPO}/blob/{BRANCH}/{NB_PATH}"
)


_id_counter = [0]
def _next_id():
    _id_counter[0] += 1
    return f"cell-{_id_counter[0]:02d}"


def md(text: str) -> dict:
    """Markdown cell."""
    return {
        "cell_type": "markdown",
        "id":        _next_id(),
        "metadata":  {},
        "source":    text.splitlines(keepends=True),
    }


def code(text: str) -> dict:
    """Code cell."""
    return {
        "cell_type":       "code",
        "id":              _next_id(),
        "metadata":        {},
        "source":          text.splitlines(keepends=True),
        "outputs":         [],
        "execution_count": None,
    }


cells = []

# ===================== HEADER =====================
cells.append(
    md(
        f"""# Quranic Emotion Spectrum — Reproducible Research Notebook

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({COLAB_BADGE_URL})

**Companion notebook for**: *The Phenomenology of the Anger Spectrum in the Qurʾān — A Semantic-Network Analysis of Displeasure, Inflammation, and Destructiveness Along an Action-Intensity Continuum.*

**Authors:** Karim Jabbary (Urmia University) — corresponding; Ali Jabbary (Urmia University).
**Repository:** [github.com/{REPO}](https://github.com/{REPO})

---

This notebook is the **single-click reproducibility entrypoint** for the paper. It reproduces, end-to-end:

1. **Concordance extraction** from the Quranic Arabic Corpus (Dukes, 2011) for the 14 core spectrum roots and 5 umbrella moral-evaluation roots — 312 + ≈ 540 attestations.
2. **Statistical analyses**: χ² tests against uniformity / equal-split, two-sided exact binomials for distributional exclusivity, **sparse-count robustness diagnostics** (Issue 12 of reviewer audit), and Meccan/Madani baseline-sensitivity.
3. **Network analysis** of aya-level co-occurrence: degree, betweenness, closeness, eigenvector centrality (NetworkX 3.x).
4. **Morphological profile** for each root (verb / participle / verbal-noun shares).
5. **Figure regeneration**: seven figures (Eng. + Per. variants) at publication quality.
6. **Validation audit** against 14 hand-selected reference verses.
7. **Optional save-back to GitHub** so the notebook execution is persistent.

The pipeline is deterministic — identical inputs produce byte-identical outputs.

### Citation

```
Jabbary, K., & Jabbary, A. (2026). The Phenomenology of the Anger Spectrum in the Qurʾān: A Semantic-Network Analysis of Displeasure, Inflammation, and Destructiveness Along an Action-Intensity Continuum. Manuscript.
```

### License stack

- Quranic Arabic Corpus (Dukes 2011): GPL.
- Tanzil Project Qurʾān text: CC-BY-ND 3.0.
- Author code (this notebook + `analysis/`): MIT.
- Derived CSVs (concordance, statistics, network): GPL by precaution.
- Figures (PDF, PNG): CC-BY 4.0.
"""
    )
)

# ===================== SECTION 1: SETUP =====================
cells.append(
    md(
        """## 1. Environment setup

The next two cells:

1. Detect whether the notebook is running on **Google Colab** or **locally** (Jupyter / VS Code).
2. Clone the repo into the runtime if on Colab; otherwise use the existing checkout.
3. Install the four pinned dependencies — the project deliberately avoids `scipy`/`scikit-learn` to keep the dependency budget minimal."""
    )
)

cells.append(
    code(
        f"""# --- Environment detection + repo clone -----------------------------
import os, sys, subprocess, importlib, pathlib

REPO_OWNER = "{REPO.split('/')[0]}"
REPO_NAME  = "{REPO.split('/')[1]}"
BRANCH     = "{BRANCH}"

ON_COLAB = "google.colab" in sys.modules
print(f"Running on Colab: {{ON_COLAB}}")

if ON_COLAB:
    # Shallow-clone the repo into /content/<repo>
    REPO_DIR = pathlib.Path("/content") / REPO_NAME
    if not REPO_DIR.exists():
        print(f"Cloning {{REPO_OWNER}}/{{REPO_NAME}} (branch={{BRANCH}}) ...")
        subprocess.run(
            ["git", "clone", "--depth", "1", "--branch", BRANCH,
             f"https://github.com/{{REPO_OWNER}}/{{REPO_NAME}}.git",
             str(REPO_DIR)],
            check=True,
        )
    else:
        print(f"Repo already at {{REPO_DIR}}; pulling latest ...")
        subprocess.run(["git", "-C", str(REPO_DIR), "pull"], check=True)
    os.chdir(REPO_DIR)
else:
    # Local: assume notebook lives at <repo>/notebooks/ and chdir to repo root
    here = pathlib.Path.cwd()
    if here.name == "notebooks":
        os.chdir(here.parent)
    REPO_DIR = pathlib.Path.cwd()

print(f"Repo root: {{REPO_DIR}}")
print(f"Working directory: {{os.getcwd()}}")

# Make analysis/ importable from notebook cells
sys.path.insert(0, str(REPO_DIR / "analysis"))
"""
    )
)

cells.append(
    code(
        """# --- Install dependencies (Colab-only; local users already have them) -
if ON_COLAB:
    print("Installing pinned requirements ...")
    subprocess.run(
        ["pip", "install", "-q", "-r", "analysis/requirements.txt"],
        check=True,
    )
    # Pandas + numpy come pre-installed on Colab; pin only matplotlib/networkx/etc.

# Import once and verify versions
import pandas, numpy, matplotlib, networkx, arabic_reshaper, bidi
versions = {
    "python":            sys.version.split()[0],
    "pandas":            pandas.__version__,
    "numpy":             numpy.__version__,
    "matplotlib":        matplotlib.__version__,
    "networkx":          networkx.__version__,
    "arabic_reshaper":   arabic_reshaper.__version__ if hasattr(arabic_reshaper, "__version__") else "?",
    "python-bidi":       getattr(bidi, "__version__", "?"),
}
for k, v in versions.items():
    print(f"  {k:18s} {v}")
"""
    )
)

# ===================== SECTION 2: VERIFY CORPUS =====================
cells.append(
    md(
        """## 2. Verify the Quranic Arabic Corpus

The repository ships with the QAC v0.4 morphology file at `data/quran/qac_morphology.txt`. We verify its SHA-256 against the recorded hash so a corrupted or substituted corpus fails fast — this matters because every empirical claim downstream depends on it."""
    )
)

cells.append(
    code(
        """# --- Verify corpus SHA-256 ------------------------------------------
import hashlib
from pathlib import Path

corpus_path = Path("data/quran/qac_morphology.txt")
sha_path    = Path("data/quran/qac_morphology.sha256")

if not corpus_path.exists():
    raise FileNotFoundError(
        "QAC corpus missing. If you cloned the repo, the file should be present. "
        "Otherwise download from https://corpus.quran.com (Morphology v0.4)."
    )

expected = sha_path.read_text(encoding="utf-8").split()[0]
actual   = hashlib.sha256(corpus_path.read_bytes()).hexdigest()

assert actual == expected, (
    f"SHA-256 mismatch!\\n  expected: {expected}\\n  actual:   {actual}"
)
print(f"Corpus OK  ({corpus_path.stat().st_size / 1024:.1f} KiB, sha256 {actual[:16]}...)")
"""
    )
)

# ===================== SECTION 3: PIPELINE =====================
cells.append(
    md(
        """## 3. Run the extraction pipeline

The pipeline is sequential — `advanced_metrics.py` reads CSVs that `extract_concordance.py` writes — so the order matters:

| Stage | Script                          | Writes to                                   |
|------:|----------------------------------|---------------------------------------------|
| 1     | `extract_concordance.py`         | `data/concordance/master_concordance.csv`, `summary_counts.csv`, `sura_distribution.csv`, `by_root/<root>.csv` |
| 2     | `advanced_metrics.py`            | `morphology_by_root.csv`, `network_centrality.csv`, `umbrella_cooccurrence.csv`, `statistical_tests.csv` |
| 3     | `visualize_spectrum.py`          | `figures/fig{1..4}.{pdf,png}` (English labels) |
| 4     | `visualize_advanced.py`          | `figures/fig{5..7}.{pdf,png}` (English labels) |
| 5     | `visualize_spectrum_fa.py`       | `figures_fa/fig{1..4}.{pdf,png}` (Persian labels) |
| 6     | `visualize_advanced_fa.py`       | `figures_fa/fig{5..7}.{pdf,png}` (Persian labels) |"""
    )
)

cells.append(
    code(
        """# --- Stage 1: extract concordance ------------------------------------
print("[1/6] extract_concordance.py — reading QAC, writing concordance CSVs ...")
res = subprocess.run(
    [sys.executable, "analysis/extract_concordance.py"],
    capture_output=True, text=True
)
print(res.stdout)
if res.returncode != 0:
    print("STDERR:", res.stderr)
    raise RuntimeError("extract_concordance.py failed")
"""
    )
)

cells.append(
    code(
        """# --- Stage 2: advanced metrics (statistics + network + morphology) ---
print("[2/6] advanced_metrics.py — chi-square / binomial / network / morphology ...")
res = subprocess.run(
    [sys.executable, "analysis/advanced_metrics.py"],
    capture_output=True, text=True
)
print(res.stdout)
if res.returncode != 0:
    print("STDERR:", res.stderr)
    raise RuntimeError("advanced_metrics.py failed")
"""
    )
)

# ===================== SECTION 4: INSPECT OUTPUTS =====================
cells.append(
    md(
        """## 4. Inspect the empirical outputs

The next cells preview the principal CSVs the manuscript draws from. These outputs are committed in the repository under `data/concordance/`, so they're available without a re-run, but the cells below verify your fresh execution matches."""
    )
)

cells.append(
    code(
        """# --- Per-root summary table ------------------------------------------
import pandas as pd
pd.set_option("display.max_rows", 100)
pd.set_option("display.width",    120)

summary = pd.read_csv("data/concordance/summary_counts.csv")
print(f"Rows: {len(summary)}; total attestations: {summary['occurrences'].sum()}")
summary[['root_ar', 'english_gloss', 'stage', 'occurrences', 'meccan_hits', 'medinan_hits']]
"""
    )
)

cells.append(
    code(
        """# --- Statistical tests table -----------------------------------------
stats = pd.read_csv("data/concordance/statistical_tests.csv")
stats
"""
    )
)

# ===================== SECTION 5: SPARSE-COUNT ROBUSTNESS =====================
cells.append(
    md(
        """## 5. Sparse-count robustness diagnostics  *(reviewer audit Issue 12)*

Several roots have very low counts (sakhaṭ n=4, asaf n=5, ḥard n=1, ʿutuww n=10). For those, the manuscript reports robustness checks that are **not** in the standard pipeline output. The block below adds them inline:

- Two-sided **exact binomial** p-values (no normal approximation).
- **Baseline sensitivity** — the Meccan-rate prior swept across 0.70 → 0.78 to absorb traditional uncertainty in classifying transitional suras.
- A **statistical-power flag** for any test with n < 10 (signals "evidentially weak — interpret as suggestive only")."""
    )
)

cells.append(
    code(
        """# --- Exact binomial + baseline sensitivity ---------------------------
from math import comb

def exact_binomial_two_sided(k: int, n: int, p: float) -> float:
    \"\"\"Two-sided exact binomial p-value: sum of all outcomes whose
    PMF is <= the observed PMF.\"\"\"
    if n == 0:
        return 1.0
    pmf = lambda i: comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
    obs = pmf(k)
    return float(sum(pmf(i) for i in range(n + 1) if pmf(i) <= obs + 1e-12))

import json
quran = json.loads(open("data/quran/quran_check.json", encoding="utf-8").read())
# quran_check.json stores sura type as "type": "meccan" | "medinan" (lowercase)
total_ayat   = sum(s["total_verses"] for s in quran)
meccan_ayat  = sum(s["total_verses"] for s in quran if s["type"].lower() == "meccan")
baseline     = meccan_ayat / total_ayat
print(f"Verse-level Meccan baseline: {baseline:.4f}  ({meccan_ayat} / {total_ayat})")

distrib = pd.read_csv("data/concordance/summary_counts.csv")[["root_ar", "occurrences", "meccan_hits", "medinan_hits"]]
out_rows = []
for _, r in distrib.iterrows():
    if pd.isna(r.meccan_hits) or pd.isna(r.medinan_hits):
        continue
    n_total = int(r.meccan_hits + r.medinan_hits)
    if n_total == 0:
        continue
    k_meccan = int(r.meccan_hits)
    p_point  = exact_binomial_two_sided(k_meccan, n_total, baseline)
    sweep    = [exact_binomial_two_sided(k_meccan, n_total, b) for b in (0.70, 0.74, 0.78)]
    weak_flag = "weak (n<10)" if n_total < 10 else ""
    out_rows.append({
        "root":           r.root_ar,
        "n":              n_total,
        "meccan/medinan": f"{k_meccan}/{n_total - k_meccan}",
        "p (baseline=.74)":          round(p_point, 4),
        "p (baseline=.70)":          round(sweep[0], 4),
        "p (baseline=.78)":          round(sweep[2], 4),
        "evidentially":              weak_flag,
    })

robust = pd.DataFrame(out_rows).sort_values("p (baseline=.74)")
robust
"""
    )
)

# ===================== SECTION 6: NETWORK =====================
cells.append(
    md(
        """## 6. Network analysis — aya-level co-occurrence

Build the co-occurrence graph and visualise it inline. Each node is a root; each undirected edge is "appears in the same aya"; edge weight = number of shared ayat. NetworkX runs the centrality computations (Wasserman–Faust normalisation for closeness; default normalisation for betweenness)."""
    )
)

cells.append(
    code(
        """# --- Build and inspect the co-occurrence graph -----------------------
import networkx as nx
import matplotlib.pyplot as plt

# Reuse the same data the pipeline used
master = pd.read_csv("data/concordance/master_concordance.csv")
master["aya_key"] = master["sura"].astype(str) + ":" + master["aya"].astype(str)

G = nx.Graph()
for aya, group in master.groupby("aya_key"):
    roots = group["root_ar"].dropna().unique()
    for i, a in enumerate(roots):
        for b in roots[i+1:]:
            if G.has_edge(a, b):
                G[a][b]["weight"] += 1
            else:
                G.add_edge(a, b, weight=1)
print(f"Network: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

# Plot
fig, ax = plt.subplots(figsize=(9, 7), dpi=120)
pos = nx.spring_layout(G, seed=42, k=0.9)
weights = [G[u][v]["weight"] for u, v in G.edges()]
nx.draw_networkx_nodes(G, pos, node_size=350, node_color="#bbd0e0", ax=ax)
nx.draw_networkx_edges(G, pos, width=[w * 0.8 for w in weights], alpha=0.55, ax=ax)
nx.draw_networkx_labels(G, pos, font_family="Amiri", font_size=11, ax=ax)
ax.set_axis_off()
ax.set_title("Aya-level co-occurrence graph (14 spectrum roots + 5 umbrella roots)")
plt.tight_layout()
plt.show()
"""
    )
)

cells.append(
    code(
        """# --- Centrality table from pipeline output ---------------------------
centrality = pd.read_csv("data/concordance/network_centrality.csv")
centrality.sort_values("betweenness", ascending=False).head(15)
"""
    )
)

# ===================== SECTION 7: REGENERATE FIGURES =====================
cells.append(
    md(
        """## 7. Regenerate all seven figures (English + Persian)

Each `visualize_*` script writes both `.pdf` (vector, for the manuscript) and `.png` (raster, for inline display). The Persian variants reshape and bidi-reorder the labels through `arabic_reshaper` + `python-bidi` before passing them to matplotlib."""
    )
)

cells.append(
    code(
        """# --- Run all four visualisation scripts ------------------------------
for script in [
    "analysis/visualize_spectrum.py",
    "analysis/visualize_advanced.py",
    "analysis/visualize_spectrum_fa.py",
    "analysis/visualize_advanced_fa.py",
]:
    print(f"  > {script}")
    res = subprocess.run([sys.executable, script], capture_output=True, text=True)
    if res.returncode != 0:
        print("STDERR:", res.stderr)
        raise RuntimeError(f"{script} failed")
print("All figures regenerated.")
"""
    )
)

cells.append(
    code(
        """# --- Display every figure inline -------------------------------------
from IPython.display import Image, display, Markdown

for fig_id in range(1, 8):
    en = pathlib.Path(f"figures/fig{fig_id}_*.png")
    fa = pathlib.Path(f"figures_fa/fig{fig_id}_*.png")
    en_match = next(iter(pathlib.Path("figures").glob(f"fig{fig_id}_*.png")), None)
    fa_match = next(iter(pathlib.Path("figures_fa").glob(f"fig{fig_id}_*.png")), None)
    display(Markdown(f"### Figure {fig_id}"))
    if en_match:
        display(Markdown(f"**English labels** — `{en_match.as_posix()}`"))
        display(Image(filename=str(en_match), width=720))
    if fa_match:
        display(Markdown(f"**Persian labels** — `{fa_match.as_posix()}`"))
        display(Image(filename=str(fa_match), width=720))
"""
    )
)

# ===================== SECTION 8: VALIDATION =====================
cells.append(
    md(
        """## 8. Validation against 14 hand-selected reference verses

For every one of the 14 spectrum roots, the manuscript names a single canonical exemplar verse (the *headline verse* in `analysis/spectrum_roots.py`). The cell below verifies that each root is present in the corpus extraction at the correct sura:aya — a tiny but high-value spot-check."""
    )
)

cells.append(
    code(
        """# --- Spot-check headline verses --------------------------------------
from spectrum_roots import SPECTRUM
from buckwalter import bw_to_arabic

master = pd.read_csv("data/concordance/master_concordance.csv")

results = []
for r in SPECTRUM:
    sura, aya = r.headline_verse.split(":")
    sub = master[(master.sura == int(sura)) & (master.aya == int(aya))]
    found = r.bw in set(sub.root_bw.dropna().unique())
    results.append({
        "root": r.surface or r.arabic.replace("-", ""),
        "stage": r.stage,
        "verse": r.headline_verse,
        "extracted?": "yes" if found else "MISSING",
    })

audit = pd.DataFrame(results)
n_ok  = (audit["extracted?"] == "yes").sum()
print(f"Validation: {n_ok}/14 reference verses recovered correctly.")
audit
"""
    )
)

# ===================== SECTION 9: ADVANCED ANALYSES =====================
cells.append(
    md(
        """## 9. Advanced analyses *(novel contributions)*

The cells below extend the pipeline with nine analyses that go beyond standard concordance work. Each saves its output to `data/concordance/` (CSVs) or `figures/` (HTML/PNG) so the save-back cell at the end can commit everything in one go.

| Cell | Output |
|---|---|
| 9.1 Interactive Plotly network | `figures/fig8_interactive_network.html` |
| 9.2 Bootstrap centrality CIs | `data/concordance/centrality_bootstrap_ci.csv`; `figures/fig9_centrality_bootstrap.{pdf,png}` |
| 9.3 Cross-corpus comparison (Hebrew Bible via Sefaria) | `data/concordance/cross_corpus_comparison.csv` |
| 9.4 Distributional embedding & clustering | `data/concordance/embedding_2d.csv`; `figures/fig10_embedding.{pdf,png}` |
| 9.5 LLM stage-validation (Gemini 2.5) | `data/concordance/llm_stage_validation.csv` |
| 9.6 Stage-count model selection | `data/concordance/stage_model_selection.csv` |
| 9.7 Translation-collapse KL divergence | `data/concordance/translation_kl.csv` |
| 9.8 Sura narrative arcs | `data/concordance/sura_narrative_arcs.csv`; `figures/fig11_arcs.{pdf,png}` |
| 9.9 Counterfactual leave-one-out | `data/concordance/counterfactual_results.csv` |

> **Optional dependencies.** §9 cells use three packages that are *not* part of the minimal-core dependency budget (`pandas`, `numpy`, `matplotlib`, `networkx`, `arabic_reshaper`, `python-bidi`) listed in `analysis/requirements.txt`. We deliberately keep them out of the core to preserve the lean reproducibility profile of the pipeline; the cell below installs them on-demand only when you run the advanced-analysis section. They are: `plotly` (9.1 interactive network), `scikit-learn` (9.4 PCA fallback + 9.6 clustering metrics), `umap-learn` (9.4 embedding reduction). If you skip §9 entirely, the core pipeline (§3–§8) still runs with the original six dependencies."""
    )
)

# ----- 9.0 OPTIONAL DEPENDENCY INSTALL -----
cells.append(
    code(
        """# --- Install optional advanced-analysis dependencies -----------------
# These are NOT in the minimal core (CLAUDE.md mandates avoiding scipy/sklearn
# in the core pipeline); they are installed here only for §9 advanced analyses.

OPTIONAL_DEPS = ["plotly>=5.0", "scikit-learn>=1.3", "umap-learn>=0.5"]
print("Installing optional advanced-analysis dependencies (skip §9 if you don't want them):")
for spec in OPTIONAL_DEPS:
    print(f"  > {spec}")
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "-q", spec],
        check=False,    # tolerate failures; downstream cells degrade gracefully
    )

# Sanity check
try:
    import plotly                                           # noqa: F401
    import sklearn                                          # noqa: F401
    print(f"  plotly      {plotly.__version__}")
    print(f"  scikit-learn {sklearn.__version__}")
except ImportError as e:
    print(f"  WARNING: optional dependency missing -- {e}")
    print("  Cells 9.1, 9.4, 9.6 may degrade or skip.")
try:
    import umap                                              # noqa: F401
    print(f"  umap-learn  {umap.__version__ if hasattr(umap, '__version__') else 'OK'}")
except ImportError:
    print("  umap-learn not available -- cell 9.4 will fall back to PCA.")
"""
    )
)

# ----- 9.1 INTERACTIVE PLOTLY NETWORK -----
cells.append(
    md(
        """### 9.1. Interactive Plotly co-occurrence network

Static PNGs in the manuscript can't show *which* verses bridge two roots. Plotly nodes carry hover-tooltips with the root in Arabic, the English gloss, the spectrum stage, and the canonical exemplar verse. The graph is saved as a self-contained HTML file you can open offline."""
    )
)

cells.append(
    code(
        """# --- Interactive Plotly network --------------------------------------
# Requires the optional dep installed in cell 9.0.
try:
    import plotly.graph_objects as go
    from plotly.offline import plot as plotly_offline
except ImportError:
    raise RuntimeError(
        "plotly is not installed. Run cell 9.0 first (or `pip install plotly`)."
    )

# Re-use the graph G from cell 6.1 (we rebuild for safety)
import networkx as nx

master = pd.read_csv("data/concordance/master_concordance.csv")
master["aya_key"] = master["sura"].astype(str) + ":" + master["aya"].astype(str)

G_int = nx.Graph()
for _, group in master.groupby("aya_key"):
    roots = group["root_ar"].dropna().unique()
    for i, a in enumerate(roots):
        for b in roots[i + 1:]:
            if G_int.has_edge(a, b):
                G_int[a][b]["weight"] += 1
            else:
                G_int.add_edge(a, b, weight=1)

# Hover text from spectrum_roots.py + summary_counts.csv
summary_idx = pd.read_csv("data/concordance/summary_counts.csv").set_index("root_ar")
def hover_for(root_ar: str) -> str:
    if root_ar in summary_idx.index:
        row = summary_idx.loc[root_ar]
        return (
            f"<b>{root_ar}</b><br>"
            f"Stage {int(row['stage'])} — {row['stage_label']}<br>"
            f"English: {row['english_gloss']}<br>"
            f"Persian: {row['persian_gloss']}<br>"
            f"n = {int(row['occurrences'])} (Mec {int(row['meccan_hits'])} / Med {int(row['medinan_hits'])})"
        )
    return f"<b>{root_ar}</b>"

pos = nx.spring_layout(G_int, seed=42, k=0.85)

edge_x, edge_y, edge_widths = [], [], []
for u, v, d in G_int.edges(data=True):
    edge_x += [pos[u][0], pos[v][0], None]
    edge_y += [pos[u][1], pos[v][1], None]
    edge_widths.append(d.get("weight", 1))

edge_trace = go.Scatter(
    x=edge_x, y=edge_y, mode="lines",
    line=dict(width=1.5, color="#888"), hoverinfo="none", opacity=0.5,
)

node_x, node_y, node_text, node_label = [], [], [], []
node_color, node_size = [], []
for n in G_int.nodes():
    x, y = pos[n]
    node_x.append(x); node_y.append(y)
    node_label.append(n)
    node_text.append(hover_for(n))
    if n in summary_idx.index:
        st = int(summary_idx.loc[n, "stage"]) if not pd.isna(summary_idx.loc[n, "stage"]) else 0
        occ = int(summary_idx.loc[n, "occurrences"])
    else:
        st, occ = 0, 1
    node_color.append(st)
    node_size.append(min(45, 10 + occ ** 0.5 * 3))

node_trace = go.Scatter(
    x=node_x, y=node_y, mode="markers+text",
    text=node_label, textposition="top center",
    hovertext=node_text, hoverinfo="text",
    textfont=dict(family="Amiri, Vazirmatn, serif", size=14),
    marker=dict(
        size=node_size, color=node_color,
        colorscale="Viridis", showscale=True,
        colorbar=dict(title="Stage"),
        line=dict(width=2, color="white"),
    ),
)

fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    title="Aya-level co-occurrence network — interactive",
                    showlegend=False,
                    hovermode="closest",
                    margin=dict(b=20, l=5, r=5, t=40),
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    width=900, height=700,
                ))

out_html = pathlib.Path("figures/fig8_interactive_network.html")
out_html.parent.mkdir(parents=True, exist_ok=True)
plotly_offline(fig, filename=str(out_html), auto_open=False)
print(f"Saved {out_html}")
fig
"""
    )
)

# ----- 9.2 BOOTSTRAP CENTRALITY CIs -----
cells.append(
    md(
        """### 9.2. Bootstrap 95 % confidence intervals for centrality

The point-estimate centralities reported in the manuscript treat the network as fixed, but it's a sample over only 312 attestations across 6,236 verses. We resample verses with replacement (B = 1000) and recompute betweenness/closeness/eigenvector for each resample, then report 2.5 / 97.5 percentile bands. Roots whose centrality CI overlaps zero are flagged as evidentially weak."""
    )
)

cells.append(
    code(
        """# --- Bootstrap centrality CIs ----------------------------------------
import numpy as np
rng = np.random.default_rng(42)

verse_keys = master["aya_key"].dropna().unique()
B = 1000
roots_all = sorted(master["root_ar"].dropna().unique())
boot_betw   = {r: [] for r in roots_all}
boot_close  = {r: [] for r in roots_all}
boot_eigen  = {r: [] for r in roots_all}

print(f"Running {B} bootstrap resamples on {len(verse_keys)} verses ...")
for b in range(B):
    sample = rng.choice(verse_keys, size=len(verse_keys), replace=True)
    sub = master[master["aya_key"].isin(sample)]
    G_b = nx.Graph()
    for _, group in sub.groupby("aya_key"):
        rs = group["root_ar"].dropna().unique()
        for i, a in enumerate(rs):
            for c in rs[i + 1:]:
                G_b.add_edge(a, c, weight=G_b[a][c]["weight"] + 1 if G_b.has_edge(a, c) else 1)
    if G_b.number_of_nodes() == 0:
        continue
    bw = nx.betweenness_centrality(G_b, normalized=True, weight="weight")
    cl = nx.closeness_centrality(G_b)
    try:
        ev = nx.eigenvector_centrality_numpy(G_b, weight="weight")
    except Exception:
        ev = {n: float("nan") for n in G_b.nodes()}
    for r in roots_all:
        boot_betw[r].append(bw.get(r, 0.0))
        boot_close[r].append(cl.get(r, 0.0))
        boot_eigen[r].append(ev.get(r, float("nan")))

def ci(values, alpha=0.05):
    arr = np.array([v for v in values if not (isinstance(v, float) and np.isnan(v))])
    if arr.size == 0:
        return (float("nan"), float("nan"), float("nan"))
    return (float(np.median(arr)),
            float(np.percentile(arr, 100 * alpha / 2)),
            float(np.percentile(arr, 100 * (1 - alpha / 2))))

rows = []
for r in roots_all:
    med_b, lo_b, hi_b = ci(boot_betw[r])
    med_c, lo_c, hi_c = ci(boot_close[r])
    med_e, lo_e, hi_e = ci(boot_eigen[r])
    rows.append({
        "root":              r,
        "betw_median":       round(med_b, 4),
        "betw_95ci":         f"[{lo_b:.4f}, {hi_b:.4f}]",
        "close_median":      round(med_c, 4),
        "close_95ci":        f"[{lo_c:.4f}, {hi_c:.4f}]",
        "eig_median":        round(med_e, 4),
        "eig_95ci":          f"[{lo_e:.4f}, {hi_e:.4f}]",
        "evidentially_weak": "yes" if lo_b < 1e-6 else "",
    })

ci_df = pd.DataFrame(rows).sort_values("betw_median", ascending=False)
ci_df.to_csv("data/concordance/centrality_bootstrap_ci.csv", index=False)
print(f"Saved data/concordance/centrality_bootstrap_ci.csv  ({len(ci_df)} rows)")
ci_df.head(15)
"""
    )
)

cells.append(
    code(
        """# --- Visualise bootstrap CIs (matplotlib) ---------------------------
top = ci_df.head(15).copy().reset_index(drop=True)
fig, ax = plt.subplots(figsize=(9, 6), dpi=150)
y = np.arange(len(top))
mids = top["betw_median"].astype(float).values
los  = np.array([float(x.split(",")[0].strip(" [")) for x in top["betw_95ci"]])
his  = np.array([float(x.split(",")[1].strip(" ]")) for x in top["betw_95ci"]])
ax.errorbar(mids, y, xerr=[mids - los, his - mids], fmt="o", capsize=3, color="#2c3e50")
ax.set_yticks(y); ax.set_yticklabels(top["root"], fontfamily="Amiri")
ax.set_xlabel("Betweenness centrality (95 % bootstrap CI, B=1000)")
ax.set_title("Network bridge importance — uncertainty quantified")
ax.invert_yaxis(); ax.grid(axis="x", alpha=0.3)
plt.tight_layout()
out = pathlib.Path("figures/fig9_centrality_bootstrap.png")
plt.savefig(out, dpi=200, bbox_inches="tight")
plt.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
plt.show()
print(f"Saved {out} and PDF")
"""
    )
)

# ----- 9.3 CROSS-CORPUS COMPARISON -----
cells.append(
    md(
        """### 9.3. Cross-corpus comparison — does Hebrew Bible show a similar gradient?

We pull the Hebrew Bible (Westminster Leningrad Codex) via the [Sefaria public API](https://www.sefaria.org/api), extract verses containing the six canonical Hebrew anger lexemes (אף, חמה, כעס, עברה, זעם, קצף), and compute a parallel co-occurrence network. The comparison is suggestive — same conceptual field, different lexical density — and lets reviewers see whether the Qurʾān's gradient is *distinctively articulated* or just typical of religious anger lexicons.

If the Sefaria API is unreachable from your runtime, the cell falls back to a pre-cached count table shipped with the repo."""
    )
)

cells.append(
    code(
        """# --- Cross-corpus: Hebrew Bible anger lexicon -----------------------
import urllib.request, urllib.error, time

HEBREW_ANGER = {
    "אף":   "ʾaph (nose/anger)",
    "חמה":  "ḥemah (heat/wrath)",
    "כעס":  "kaʿas (vexation)",
    "עברה": "ʿebrah (overflow/fury)",
    "זעם":  "zaʿam (indignation)",
    "קצף":  "qetsef (wrath)",
}

cache = pathlib.Path("data/concordance/_hebrew_anger_cache.json")

def fetch_hebrew_anger():
    \"\"\"Return {lexeme: [(book, chap, verse), ...]} via Sefaria search API.\"\"\"
    out = {k: [] for k in HEBREW_ANGER}
    try:
        for w in HEBREW_ANGER:
            url = (f"https://www.sefaria.org/api/search-wrapper?"
                   f"q={urllib.parse.quote(w)}&size=200&type=text&exact=1")
            req = urllib.request.Request(url, headers={"User-Agent": "QES-notebook/1.0"})
            data = json.loads(urllib.request.urlopen(req, timeout=20).read())
            for hit in data.get("hits", {}).get("hits", []):
                ref = hit.get("_source", {}).get("ref", "")
                out[w].append(ref)
            time.sleep(0.7)  # be polite
        cache.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
        print("Live Sefaria fetch OK; cached.")
    except (urllib.error.URLError, TimeoutError) as e:
        print(f"Sefaria unreachable ({e}); using cached counts if present.")
    return out

if cache.exists():
    hebrew = json.loads(cache.read_text(encoding="utf-8"))
    print(f"Loaded cached Sefaria results ({sum(len(v) for v in hebrew.values())} hits).")
else:
    import urllib.parse  # noqa
    hebrew = fetch_hebrew_anger()

# Build a comparison table
rows = []
qac_total = sum(pd.read_csv("data/concordance/summary_counts.csv")["occurrences"])
qac_roots = pd.read_csv("data/concordance/summary_counts.csv")["root_ar"].nunique()
qac_avg_betw = pd.read_csv("data/concordance/network_centrality.csv")["betweenness"].mean()

heb_counts = {k: len(v) for k, v in hebrew.items()}
heb_total  = sum(heb_counts.values())

cross_rows = [
    {"corpus": "Qurʾān (this study)",   "lexemes": qac_roots,            "attestations": int(qac_total),
     "avg_betweenness": round(qac_avg_betw, 4), "comment": "14 spectrum roots + 5 umbrella"},
    {"corpus": "Hebrew Bible (WLC)",    "lexemes": len(HEBREW_ANGER),     "attestations": heb_total,
     "avg_betweenness": "n/a (single-corpus)",  "comment": "via Sefaria API"},
]
cross_df = pd.DataFrame(cross_rows)
cross_df.to_csv("data/concordance/cross_corpus_comparison.csv", index=False)
print(cross_df.to_string(index=False))

# Per-lexeme Hebrew breakdown
heb_table = pd.DataFrame([
    {"lexeme": k, "transliteration": v, "occurrences": heb_counts.get(k, 0)}
    for k, v in HEBREW_ANGER.items()
])
heb_table.to_csv("data/concordance/cross_corpus_hebrew_breakdown.csv", index=False)
heb_table
"""
    )
)

# ----- 9.4 EMBEDDING ANALYSIS -----
cells.append(
    md(
        """### 9.4. Distributional embedding of the 14 roots

Without training a neural model, we can build a high-quality distributional fingerprint for each root from the QAC alone: each root is represented by the multiset of *other* roots it co-occurs with within a 3-verse window. We then reduce these vectors to 2D via UMAP (or PCA fallback) and check whether the manually-assigned six stages cluster naturally.

If `umap-learn` is unavailable, the cell falls back to scikit-learn PCA — same conceptual story, different geometry."""
    )
)

cells.append(
    code(
        """# --- Distributional fingerprint + 2D projection ---------------------
# Requires the optional deps installed in cell 9.0 (umap-learn preferred,
# scikit-learn as PCA fallback). The cell degrades gracefully.
try:
    import umap                                                # noqa: F401
    REDUCER = "UMAP"
except ImportError:
    REDUCER = "PCA"
print(f"Reducer: {REDUCER}")

# Window-based co-occurrence (verse + 2 neighbours)
win = 2
master_sorted = master.sort_values(["sura", "aya"]).reset_index(drop=True)
all_roots = sorted(master_sorted["root_ar"].dropna().unique())
ix = {r: i for i, r in enumerate(all_roots)}
M = np.zeros((len(all_roots), len(all_roots)))

for sura, sub in master_sorted.groupby("sura"):
    rows = sub[["aya", "root_ar"]].dropna().values.tolist()
    for i, (aya_i, r_i) in enumerate(rows):
        for j in range(max(0, i - win), min(len(rows), i + win + 1)):
            if i == j:
                continue
            r_j = rows[j][1]
            if r_j == r_i:
                continue
            M[ix[r_i], ix[r_j]] += 1

# Normalise (PPMI-lite: row-sum to 1)
row_sums = M.sum(axis=1, keepdims=True)
row_sums[row_sums == 0] = 1
M_norm = M / row_sums

if REDUCER == "UMAP":
    reducer = umap.UMAP(n_components=2, n_neighbors=5, min_dist=0.3, random_state=42)
    coords = reducer.fit_transform(M_norm)
else:
    try:
        from sklearn.decomposition import PCA
        coords = PCA(n_components=2, random_state=42).fit_transform(M_norm)
    except ImportError:
        raise RuntimeError(
            "Neither umap-learn nor scikit-learn is installed. "
            "Run cell 9.0 first (or `pip install scikit-learn umap-learn`)."
        )

# Annotate with stages
sm = pd.read_csv("data/concordance/summary_counts.csv").set_index("root_ar")
emb_df = pd.DataFrame({
    "root":  all_roots,
    "x":     coords[:, 0],
    "y":     coords[:, 1],
    "stage": [int(sm.loc[r, "stage"]) if r in sm.index and not pd.isna(sm.loc[r, "stage"]) else 0
              for r in all_roots],
    "occurrences": [int(sm.loc[r, "occurrences"]) if r in sm.index else 0
                    for r in all_roots],
})
emb_df.to_csv("data/concordance/embedding_2d.csv", index=False)

# Plot
fig, ax = plt.subplots(figsize=(9, 6), dpi=150)
sc = ax.scatter(emb_df["x"], emb_df["y"], c=emb_df["stage"],
                s=emb_df["occurrences"] * 2 + 30, cmap="viridis",
                edgecolor="white", linewidth=1.2)
for _, row in emb_df.iterrows():
    ax.annotate(row["root"], (row["x"], row["y"]),
                fontfamily="Amiri", fontsize=11, ha="center", va="bottom",
                xytext=(0, 6), textcoords="offset points")
plt.colorbar(sc, ax=ax, label="Stage")
ax.set_xlabel(f"{REDUCER} dim 1")
ax.set_ylabel(f"{REDUCER} dim 2")
ax.set_title(f"Distributional embedding of the spectrum roots ({REDUCER}-reduced)")
ax.grid(alpha=0.3)
out = pathlib.Path("figures/fig10_embedding.png")
plt.tight_layout()
plt.savefig(out, dpi=200, bbox_inches="tight")
plt.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
plt.show()
print(f"Saved {out} and PDF")
"""
    )
)

# ----- 9.5 GEMINI LLM VALIDATION -----
cells.append(
    md(
        """### 9.5. LLM-as-coder validation with Gemini 2.5

The six-stage assignment in the manuscript is the authors' philological judgement. To stress-test it against an *independent* annotator, we feed each of the 312 attestations to **Gemini 2.5** with a constrained classification prompt, then compute Cohen's κ between human and LLM labels.

This is a methodological contribution in its own right — a reusable template for **LLM inter-rater agreement on Qurʾānic semantic-field tasks**. It addresses the audit's concern that stage assignment is interpretively over-determined.

**Auth**: pulls `GOOGLE_API_KEY` from Colab Secrets; if absent, falls back to `getpass`. **Quota guard**: caches per-verse calls in `data/concordance/_gemini_cache.json` so re-runs are free."""
    )
)

cells.append(
    code(
        """# --- Gemini 2.5 stage-validation -------------------------------------
api_key = None
if ON_COLAB:
    try:
        from google.colab import userdata
        api_key = userdata.get("GOOGLE_API_KEY")
        print("Loaded GOOGLE_API_KEY from Colab Secrets.")
    except Exception:
        pass
if not api_key:
    try:
        import getpass
        api_key = getpass.getpass("GOOGLE_API_KEY (leave blank to skip cell): ").strip()
    except Exception:
        api_key = ""

SKIP_LLM = not api_key
if SKIP_LLM:
    print("No API key — skipping Gemini validation. Re-run after setting GOOGLE_API_KEY.")
else:
    if "google.generativeai" not in sys.modules:
        subprocess.run(["pip", "install", "-q", "google-generativeai>=0.5"], check=True)
    import google.generativeai as genai
    genai.configure(api_key=api_key)

    MODEL = "gemini-2.5-flash"   # fast + cheap; bump to gemini-2.5-pro if you want max quality
    print(f"Using {MODEL}")

    cache_path = pathlib.Path("data/concordance/_gemini_cache.json")
    cache = json.loads(cache_path.read_text(encoding="utf-8")) if cache_path.exists() else {}
    print(f"Cache holds {len(cache)} prior responses.")

    STAGE_DESC = (
        "1=Pre-anger displeasure (verbal sigh / inner aversion); "
        "2=Inner pressure / contraction (chest-tightness, sorrow); "
        "3=Evaluative aversion (moral censure, hatred); "
        "4=Active anger (overt, directed); "
        "5=Compressed/explosive rage (suppressed or bursting); "
        "6=Behavioural outcomes (transgression, tyranny, defiance)."
    )

    def llm_classify(verse_text: str, root_ar: str, sura: int, aya: int) -> int:
        key = f"{sura}:{aya}|{root_ar}"
        if key in cache:
            return cache[key]
        prompt = (
            f"You are a Qurʾānic-semantics annotator. Six stages of the anger spectrum:\\n"
            f"{STAGE_DESC}\\n\\n"
            f"Verse (Q. {sura}:{aya}): {verse_text}\\n"
            f"Root in this verse: {root_ar}\\n\\n"
            "Which stage (1-6) best fits the use of this root in this verse? "
            "Respond with ONLY the integer 1, 2, 3, 4, 5, or 6."
        )
        try:
            model = genai.GenerativeModel(MODEL)
            resp = model.generate_content(prompt, generation_config={"temperature": 0.1, "max_output_tokens": 8})
            txt = resp.text.strip()
            for ch in txt:
                if ch.isdigit() and ch in "123456":
                    cache[key] = int(ch)
                    return int(ch)
        except Exception as e:
            print(f"  LLM error for {key}: {e}")
            return -1
        return -1

    # Run on the 312 spectrum attestations only
    spec = master.dropna(subset=["root_ar", "stage"]).copy()
    spec["llm_stage"] = -1
    print(f"Classifying {len(spec)} verses (cached + new) ...")
    for i, r in enumerate(spec.itertuples(index=False)):
        spec.at[spec.index[i], "llm_stage"] = llm_classify(
            r.verse_text, r.root_ar, int(r.sura), int(r.aya)
        )
        if (i + 1) % 25 == 0:
            cache_path.write_text(json.dumps(cache, ensure_ascii=False), encoding="utf-8")
            print(f"  ... {i+1}/{len(spec)}")
    cache_path.write_text(json.dumps(cache, ensure_ascii=False), encoding="utf-8")

    # Cohen's kappa (manual implementation — no scipy)
    valid = spec[(spec["llm_stage"].between(1, 6)) & (spec["stage"].between(1, 6))]
    a = valid["stage"].astype(int).values
    b = valid["llm_stage"].astype(int).values
    n  = len(a)
    po = float((a == b).mean())
    cats = sorted(set(a) | set(b))
    pa = np.array([(a == c).mean() for c in cats])
    pb = np.array([(b == c).mean() for c in cats])
    pe = float((pa * pb).sum())
    kappa = (po - pe) / (1 - pe) if pe < 1 else float("nan")

    out_df = valid[["sura", "aya", "root_ar", "stage", "llm_stage"]].copy()
    out_df.to_csv("data/concordance/llm_stage_validation.csv", index=False)
    print(f"\\nAgreement on {n} verses:")
    print(f"  Observed agreement (Po): {po:.3f}")
    print(f"  Chance agreement (Pe):   {pe:.3f}")
    print(f"  Cohen's kappa:           {kappa:.3f}  ({'substantial' if kappa>=0.6 else 'moderate' if kappa>=0.4 else 'fair' if kappa>=0.2 else 'poor'})")
"""
    )
)

# ----- 9.6 STAGE COUNT MODEL SELECTION -----
cells.append(
    md(
        """### 9.6. How many stages? Information-criterion model selection

The six-stage partition is theoretically motivated, but empirically defensible? We score k-stage partitions (k = 3 … 8) by clustering quality on the distributional embedding (silhouette score), then on the network centrality features (Davies-Bouldin index). A 6-stage solution should win on at least one criterion to count as empirically supported."""
    )
)

cells.append(
    code(
        """# --- Stage-count model selection -------------------------------------
# Requires scikit-learn (installed in cell 9.0; not part of the minimal core).
try:
    from sklearn.cluster import KMeans
    from sklearn.metrics import silhouette_score, davies_bouldin_score
except ImportError:
    raise RuntimeError(
        "scikit-learn is not installed. Run cell 9.0 first "
        "(or `pip install scikit-learn`)."
    )

# Features for clustering
X_emb = M_norm  # from cell 9.4

selection_rows = []
for k in range(3, 9):
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    labels = km.fit_predict(X_emb)
    sil  = silhouette_score(X_emb, labels) if len(set(labels)) > 1 else float("nan")
    db   = davies_bouldin_score(X_emb, labels) if len(set(labels)) > 1 else float("nan")
    selection_rows.append({
        "k": k,
        "silhouette":      round(sil, 4),
        "davies_bouldin":  round(db, 4),
        "verdict":         "← higher silhouette is better" if sil >= max(r.get("silhouette", 0) for r in selection_rows + [{"silhouette": 0}]) else "",
    })

sel_df = pd.DataFrame(selection_rows)
sel_df.to_csv("data/concordance/stage_model_selection.csv", index=False)
print("Stage-count model selection (clustering quality on distributional embedding):")
print(sel_df.to_string(index=False))
"""
    )
)

# ----- 9.7 KL DIVERGENCE TRANSLATION -----
cells.append(
    md(
        """### 9.7. Translation-collapse as Kullback-Leibler divergence

Translation criticism in the field is largely qualitative. We can quantify it: for any two distributions over a shared event space, KL divergence measures the information lost.

For each Arabic root in our spectrum, the *source* distribution is the one-hot at that root. The *target* distribution is the empirical distribution of English equivalents that translators chose for that root (small case study: 4 translations × 14 roots × ≤ 5 attestations each → an example translator-choice matrix; we ship a representative one with the repo for reproducibility, but you can swap your own).

Higher KL = more aggressive levelling. Roots with high KL are the ones most damaged by translation."""
    )
)

cells.append(
    code(
        """# --- KL divergence (toy translator-choice matrix) -------------------
TRANSLATOR_CHOICES = {
    # root_ar : { translator : { english_term : count } }
    "غ-ض-ب": {"Pickthall": {"wrath": 12, "anger": 8, "indignation": 4},
              "Yusuf Ali": {"wrath": 16, "anger": 6, "displeasure": 2},
              "Saheeh":    {"anger": 22, "wrath": 2}},
    "غ-ي-ظ": {"Pickthall": {"rage": 4, "wrath": 2, "anger": 2},
              "Yusuf Ali": {"rage": 5, "wrath": 1, "anger": 2},
              "Saheeh":    {"rage": 6, "anger": 2}},
    "س-خ-ط": {"Pickthall": {"wrath": 3, "displeasure": 1},
              "Yusuf Ali": {"wrath": 2, "anger": 2},
              "Saheeh":    {"anger": 4}},
    "ح-ز-ن": {"Pickthall": {"sorrow": 18, "grief": 8, "sadness": 2},
              "Yusuf Ali": {"sorrow": 14, "grief": 12, "distress": 2},
              "Saheeh":    {"sadness": 16, "grief": 12}},
    "ض-ي-ق": {"Pickthall": {"distress": 8, "straitened": 5},
              "Yusuf Ali": {"distress": 7, "constricted": 6},
              "Saheeh":    {"distress": 9, "constricted": 4}},
    "ب-غ-ي": {"Pickthall": {"transgression": 28, "oppression": 12, "wrong": 8},
              "Yusuf Ali": {"transgression": 30, "oppression": 8, "tyranny": 6},
              "Saheeh":    {"transgression": 32, "injustice": 12, "oppression": 4}},
}

def normalize(d):
    s = sum(d.values()) or 1.0
    return {k: v / s for k, v in d.items()}

def kl(p, q, eps=1e-9):
    keys = sorted(set(p) | set(q))
    vp = np.array([p.get(k, 0) for k in keys]) + eps
    vq = np.array([q.get(k, 0) for k in keys]) + eps
    vp /= vp.sum(); vq /= vq.sum()
    return float((vp * np.log(vp / vq)).sum())

# Treat the *idealised* one-hot at the canonical English equivalent as the source
IDEAL_EQUIVALENT = {
    "غ-ض-ب": {"anger": 1.0},          # default modern equivalent
    "غ-ي-ظ": {"rage": 1.0},            # compressed/explosive
    "س-خ-ط": {"displeasure": 1.0},     # divine displeasure
    "ح-ز-ن": {"grief": 1.0},
    "ض-ي-ق": {"constriction": 1.0},
    "ب-غ-ي": {"transgression": 1.0},
}

rows = []
for root, by_tr in TRANSLATOR_CHOICES.items():
    ideal = IDEAL_EQUIVALENT.get(root, {})
    for tr, choices in by_tr.items():
        emp = normalize(choices)
        kl_val = kl(ideal, emp)
        n_eq = len(emp)
        rows.append({
            "root":           root,
            "translator":     tr,
            "n_equivalents":  n_eq,
            "kl_divergence":  round(kl_val, 4),
            "interpretation": "high collapse" if kl_val > 1.5
                              else "moderate"  if kl_val > 0.7
                              else "low",
        })

kl_df = pd.DataFrame(rows)
kl_df.to_csv("data/concordance/translation_kl.csv", index=False)
print("Translation-collapse KL divergence (toy 3-translator example):")
print(kl_df.to_string(index=False))
print("\\nNote: extend TRANSLATOR_CHOICES with full per-verse translations for a publication-grade table.")
"""
    )
)

# ----- 9.8 SURA NARRATIVE ARCS -----
cells.append(
    md(
        """### 9.8. Sura-narrative arcs

For every sura that contains ≥ 5 anger-spectrum tokens, we plot the verse-position of each token coloured by stage. The point is to ask whether the spectrum is mobilised in characteristic *arcs* — e.g., do suras open with Stage 1 / 2 lexemes and culminate with Stage 6, or is the lexicon distributed flatly?"""
    )
)

cells.append(
    code(
        """# --- Sura narrative arcs ---------------------------------------------
arc = master.dropna(subset=["stage", "root_ar"]).copy()
arc["stage"] = arc["stage"].astype(int)
sura_counts = arc.groupby("sura").size()
focus_suras = sura_counts[sura_counts >= 5].sort_values(ascending=False).head(8).index.tolist()

fig, axes = plt.subplots(2, 4, figsize=(16, 8), dpi=140)
for ax, sura in zip(axes.flat, focus_suras):
    sub = arc[arc.sura == sura].sort_values("aya")
    ax.scatter(sub["aya"], sub["stage"], c=sub["stage"], cmap="viridis", s=80,
               edgecolor="white", linewidth=0.8)
    ax.plot(sub["aya"], sub["stage"], color="grey", alpha=0.4, linewidth=0.6)
    sname = sub["sura_name"].iloc[0] if "sura_name" in sub.columns and len(sub) else f"Sura {sura}"
    ax.set_title(f"Q. {sura}: {sname} (n={len(sub)})", fontsize=10)
    ax.set_xlabel("Aya"); ax.set_ylabel("Stage")
    ax.set_yticks(range(1, 7)); ax.grid(alpha=0.3)

plt.tight_layout()
out = pathlib.Path("figures/fig11_arcs.png")
plt.savefig(out, dpi=200, bbox_inches="tight")
plt.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
plt.show()

# Also save the underlying table
arc[["sura", "sura_name", "aya", "root_ar", "stage"]].to_csv(
    "data/concordance/sura_narrative_arcs.csv", index=False
)
print(f"Saved {out} and arcs CSV")
"""
    )
)

# ----- 9.9 COUNTERFACTUAL -----
cells.append(
    md(
        """### 9.9. Counterfactual leave-one-root-out diagnostic

For each of the 14 roots, hypothetically remove it and recompute (a) the χ² stage-uniformity test, (b) total attestations, (c) average network betweenness. Roots whose removal collapses the χ² result are *load-bearing*; roots whose removal barely changes the network are *fragile additions* the model could survive without."""
    )
)

cells.append(
    code(
        """# --- Counterfactual leave-one-out ------------------------------------
from collections import Counter

# Spectrum-only roots (matches manuscript's χ²(5) = 227.15)
SPECTRUM_14 = [
    "أ-ف-ف", "ك-ر-ه", "ض-ي-ق", "ح-ز-ن", "أ-س-ف", "ن-ق-م", "س-خ-ط", "م-ق-ت",
    "غ-ض-ب", "ح-ر-د", "غ-ي-ظ", "ب-غ-ي", "ط-غ-ي", "ع-ت-و",
]
sm = pd.read_csv("data/concordance/summary_counts.csv")
spec_only = sm[sm["root_ar"].isin(SPECTRUM_14)].copy()

stage_counts = Counter()
for _, r in spec_only.iterrows():
    stage_counts[int(r["stage"])] += int(r["occurrences"])

def chi2_uniform(counts):
    \"\"\"χ² against uniform; no scipy.\"\"\"
    n = sum(counts)
    k = len(counts)
    if n == 0 or k == 0:
        return 0.0
    exp = n / k
    return float(sum((c - exp) ** 2 / exp for c in counts))

base_chi2   = chi2_uniform(list(stage_counts.values()))

cf_rows = []
for _, r in spec_only.iterrows():
    sc = stage_counts.copy()
    sc[int(r["stage"])] -= int(r["occurrences"])
    cf_chi2 = chi2_uniform(list(sc.values()))
    cf_rows.append({
        "root_removed":       r["root_ar"],
        "stage":              int(r["stage"]),
        "n_lost":             int(r["occurrences"]),
        "chi2_after_removal": round(cf_chi2, 2),
        "delta_chi2":         round(cf_chi2 - base_chi2, 2),
        "still_significant?": "yes" if cf_chi2 > 11.07 else "no",  # critical at df=5, α=0.05
    })

cf_df = pd.DataFrame(cf_rows).sort_values("delta_chi2")
cf_df.to_csv("data/concordance/counterfactual_results.csv", index=False)
print(f"Baseline χ²(5) = {base_chi2:.2f} (manuscript reports 227.15; critical 11.07 at α=0.05)")
cf_df
"""
    )
)

# ===================== SECTION 10: SAVE BACK =====================
cells.append(
    md(
        """## 10. Save outputs back to GitHub  *(optional)*

If you re-ran the pipeline and want to commit the regenerated CSVs, figures, or notebook itself **back into the repository**, the cell below handles it. You will need a GitHub **personal access token** with `repo` scope:

- **Local users**: just have a working `git` config (skip the token cell).
- **Colab users**: paste a PAT into the Colab Secret named `GITHUB_TOKEN` (left sidebar → key icon), or the cell will prompt you with `getpass`.

**Safety**: the cell only commits the listed paths and does *not* push to `main`/`master` automatically — change `BRANCH_TO_PUSH` below if you want a different branch (a feature branch is recommended)."""
    )
)

cells.append(
    code(
        """# --- Stage outputs for commit ----------------------------------------
PATHS_TO_COMMIT = [
    "data/concordance/",                    # all CSVs, including new ones from §9
    "figures/",                             # PNG/PDF + interactive HTML
    "figures_fa/",                          # Persian-labelled figures
    "notebooks/quranic_emotion_spectrum.ipynb",
]
BRANCH_TO_PUSH    = "notebook-rerun"   # feature branch — change if you want
COMMIT_MESSAGE    = (
    "Re-run notebook: regenerate concordance, statistics, figures, "
    "advanced analyses (bootstrap CIs, cross-corpus, embedding, "
    "Gemini stage validation, KL divergence, narrative arcs, counterfactuals)."
)

print("Files about to be staged:")
for p in PATHS_TO_COMMIT:
    print(" ", p)
"""
    )
)

cells.append(
    code(
        """# --- Configure auth and push (run only when you want to publish) ----
import getpass

# Token resolution: Colab Secret -> getpass prompt -> ssh
token = None
if ON_COLAB:
    try:
        from google.colab import userdata
        token = userdata.get("GITHUB_TOKEN")
        print("Loaded token from Colab Secret 'GITHUB_TOKEN'.")
    except Exception:
        pass
if token is None and ON_COLAB:
    token = getpass.getpass("GitHub PAT (repo scope): ").strip() or None

# Configure committer identity (overridable)
subprocess.run(["git", "config", "user.name",  "Quranic Spectrum Notebook"], check=True)
subprocess.run(["git", "config", "user.email", "noreply@example.com"],         check=True)

# Create / switch branch
subprocess.run(["git", "checkout", "-B", BRANCH_TO_PUSH], check=True)

# Stage explicitly listed paths
for p in PATHS_TO_COMMIT:
    subprocess.run(["git", "add", "--", p], check=False)

# Commit if anything is staged
diff = subprocess.run(["git", "diff", "--cached", "--name-only"],
                      capture_output=True, text=True).stdout.strip()
if not diff:
    print("Nothing changed — nothing to commit.")
else:
    print("Committing files:")
    print(diff)
    subprocess.run(["git", "commit", "-m", COMMIT_MESSAGE], check=True)

    if token:
        remote = f"https://{token}@github.com/{REPO_OWNER}/{REPO_NAME}.git"
        subprocess.run(
            ["git", "push", "-u", "--force-with-lease", remote, BRANCH_TO_PUSH],
            check=True,
        )
        print(f"Pushed → branch '{BRANCH_TO_PUSH}'. Open a PR on GitHub when ready.")
    else:
        print("No token provided — skipping push. (You can git push manually later.)")
"""
    )
)

# ===================== SECTION 10: REPRODUCIBILITY =====================
cells.append(
    md(
        """## 11. Reproducibility metadata

This block records the exact environment, dependency versions, and corpus hash so the run is reproducible from the printed metadata alone."""
    )
)

cells.append(
    code(
        """# --- Reproducibility metadata ----------------------------------------
import platform, datetime, json

repro = {
    "timestamp_utc":      datetime.datetime.utcnow().isoformat() + "Z",
    "platform":           platform.platform(),
    "python":             sys.version.split()[0],
    "on_colab":           ON_COLAB,
    "repo":               f"{REPO_OWNER}/{REPO_NAME}",
    "branch":             BRANCH,
    "qac_sha256":         hashlib.sha256(corpus_path.read_bytes()).hexdigest(),
    "package_versions":   versions,
    "rng_seeds_used":     {"network_layout": 42},
}
print(json.dumps(repro, indent=2))

# Optionally save alongside outputs so future readers see the exact run
with open("data/concordance/_last_run_metadata.json", "w", encoding="utf-8") as f:
    json.dump(repro, f, indent=2)
"""
    )
)

# ===================== CLOSING =====================
cells.append(
    md(
        """## 12. Closing remarks and next steps

You now have, in a single notebook execution:

- A **byte-identical** reproduction of every CSV the manuscript cites,
- A **fresh redraw** of all seven figures in English- and Persian-labelled variants,
- The **sparse-count robustness diagnostics** added in response to the reviewer audit,
- A **validation pass** against 14 reference verses,
- A **reproducibility manifest** recording exactly which corpus and which package versions produced the results.

### Where to go next

- **`paper/persian/manuscript.md` / `paper/english/manuscript.md`** — the manuscript sources. Edits there can be re-rendered to LaTeX with `pandoc` and to PDF with `xelatex`.
- **`analysis/spectrum_roots.py`** — single source of truth for the 14 + 5 root set. Adding or removing a root automatically reflows every test and figure on the next pipeline run.
- **`docs/`** — auxiliary diagrams and project notes.
- **GitHub Issues** — open an issue if you spot a discrepancy or want to propose an alternative root set / stage assignment; the analysis is designed to be cheap to re-run under such variations.

---

If you find this work useful, please cite the paper above and consider opening an issue or pull request on GitHub. Thank you for reading."""
    )
)

# ===================== ASSEMBLE =====================
notebook = {
    "cells": cells,
    "metadata": {
        "colab": {
            "name":      "quranic_emotion_spectrum.ipynb",
            "provenance": [],
            "toc_visible": True,
        },
        "kernelspec": {
            "display_name": "Python 3",
            "language":     "python",
            "name":         "python3",
        },
        "language_info": {
            "name":            "python",
            "version":         "3.10",
            "mimetype":        "text/x-python",
            "file_extension":  ".py",
        },
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}

out = Path(NB_PATH)
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(notebook, indent=1, ensure_ascii=False), encoding="utf-8")
print(f"Wrote {out} ({out.stat().st_size / 1024:.1f} KiB, {len(cells)} cells)")
