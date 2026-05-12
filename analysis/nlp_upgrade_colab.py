# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # NLP upgrade: four supplementary analyses for the Qur'anic anger-spectrum paper
#
# Runs in **Google Colab** with a T4 GPU runtime (free tier OK).
#
# Four analyses, each producing CSV/figure outputs the manuscripts will cite:
#
# 1. **AraBERT/CAMeLBERT contextual-embedding clustering** of the 312 attestations,
#    tested against the six-stage labels (silhouette score, k-means agreement, UMAP plot).
# 2. **Cross-translation semantic drift** across 5 EN + 5 FA translations of the 312 attestations,
#    quantified via multilingual embeddings (sentence-transformers `paraphrase-multilingual-mpnet-base-v2`).
# 3. **Diachronic ordering test**: does the six-stage spectrum show any signal when projected onto the
#    Nöldekean revelation chronology? Spearman ρ between stage and chronological rank.
# 4. **PMI-weighted inter-root collocation network** replacing the raw co-occurrence counts in fig 4/7.
#
# **Inputs** (must be uploaded to Colab session storage or mounted from the GitHub repo):
# - `data/concordance/master_concordance.csv` (output of `extract_concordance.py`)
# - `data/concordance/summary_counts.csv`
# - `data/concordance/by_root/*.csv` (14 spectrum-root CSVs)
# - Quran text (auto-downloaded from Tanzil via URL)
# - Translation files (auto-downloaded)
#
# **Outputs** written to `outputs/`:
# - `embeddings_arabert.npz`, `embeddings_umap.png`, `cluster_vs_stage.csv`, `silhouette.json`
# - `translation_drift_per_root.csv`, `translation_drift.png`
# - `diachronic_stage_rank.csv`, `diachronic_plot.png`
# - `pmi_network.csv`, `pmi_network.png`
#
# The manuscript will reference these outputs in §4 (English) and §4-2 / §4-7 (Persian) as **independent
# corroboration** of the qualitative spectrum.

# %% [markdown]
# ## 0. Environment setup (Colab)

# %%
# !pip install -q transformers==4.45.0 torch==2.4.0 sentence-transformers==3.1.0 \
#                 umap-learn==0.5.6 hdbscan==0.8.38 scikit-learn==1.5.2 \
#                 networkx==3.3 arabic-reshaper==3.0.0 python-bidi==0.4.2 \
#                 matplotlib==3.9.2 pandas==2.2.3 tqdm==4.66.5

# %%
# Clone the repo to get the master_concordance.csv + auxiliary files.
# Alternatively, upload them manually via the Colab files panel.
# !git clone --depth 1 https://github.com/ali-kin4/quranic-emotion-spectrum.git
# %cd quranic-emotion-spectrum

# %%
import json
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from tqdm.auto import tqdm

OUTDIR = Path("outputs/nlp_upgrade")
OUTDIR.mkdir(parents=True, exist_ok=True)

# %% [markdown]
# ## 1. Load the 312 attestations and their stage labels

# %%
master = pd.read_csv("data/concordance/master_concordance.csv")
# Expected columns: root_buckwalter, root_arabic, sura, aya, word, surface_form, ...
print(master.head())
print(f"Total attestations: {len(master)}")

# Stage assignments from spectrum_roots.py (mirror them here so the notebook is self-contained).
STAGE_BY_ROOT = {
    "Off": 1, "krh": 1,
    "DyQ": 2, "Hzn": 2, "Asf": 2,
    "nqm": 3, "sxT": 3, "mqt": 3,
    "gDb": 4, "Hrd": 4,
    "gyZ": 5,
    "bgy": 6, "Tgy": 6, "Etw": 6,
}
master["stage"] = master["root_buckwalter"].map(STAGE_BY_ROOT)
master = master.dropna(subset=["stage"]).copy()
master["stage"] = master["stage"].astype(int)
print(master["stage"].value_counts().sort_index())

# %% [markdown]
# ## 2. Pull verse context for each attestation

# %%
# Download Tanzil Uthmani text if not present.
TANZIL_URL = "https://tanzil.net/pub/download/index.php?quranType=uthmani&outType=txt"
quran_path = Path("data/quran-uthmani.txt")
if not quran_path.exists():
    quran_path.parent.mkdir(parents=True, exist_ok=True)
    import urllib.request
    urllib.request.urlretrieve(TANZIL_URL, quran_path)

# Build a (sura, aya) -> text dictionary.
verse_text = {}
for line in open(quran_path, encoding="utf-8"):
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    sura, aya, text = line.split("|", 2)
    verse_text[(int(sura), int(aya))] = text

master["verse_text"] = master.apply(
    lambda r: verse_text.get((int(r.sura), int(r.aya)), ""), axis=1
)
assert master["verse_text"].str.len().min() > 0, "Some attestations missing verse text"


# %% [markdown]
# ## 3. Analysis 1 — AraBERT/CAMeLBERT contextual embeddings

# %%
import torch
from transformers import AutoTokenizer, AutoModel

MODEL_NAME = "CAMeL-Lab/bert-base-arabic-camelbert-ca"  # Classical Arabic variant
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

tok = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModel.from_pretrained(MODEL_NAME).to(device).eval()


def embed_with_root_context(verse, root_surface, max_len=128):
    """Return the mean-pooled hidden state of the verse, weighted toward the
    tokens that fall inside the root's surface form. Falls back to CLS embedding
    if the root isn't found in the tokenization (shouldn't happen for Q. text)."""
    enc = tok(
        verse, return_tensors="pt", truncation=True, max_length=max_len,
        padding="max_length", return_offsets_mapping=True,
    )
    offsets = enc.pop("offset_mapping")[0].tolist()
    enc = {k: v.to(device) for k, v in enc.items()}
    with torch.no_grad():
        out = model(**enc).last_hidden_state[0]  # (T, H)

    # Locate root tokens by surface match in original verse.
    start_char = verse.find(root_surface)
    if start_char < 0:
        return out[0].cpu().numpy()  # CLS fallback
    end_char = start_char + len(root_surface)
    mask = torch.tensor([
        (s < end_char and e > start_char) for s, e in offsets
    ], device=device)
    if mask.sum() == 0:
        return out[0].cpu().numpy()
    return out[mask].mean(0).cpu().numpy()


emb = np.stack([
    embed_with_root_context(r.verse_text, r.surface_form)
    for r in tqdm(master.itertuples(), total=len(master), desc="Embedding")
])
np.savez(OUTDIR / "embeddings_arabert.npz", emb=emb, stage=master["stage"].values,
         root=master["root_buckwalter"].values)
print("emb shape:", emb.shape)

# %% [markdown]
# ### 3a. Cluster the embeddings & test against stage labels

# %%
from sklearn.cluster import KMeans
from sklearn.metrics import (silhouette_score, adjusted_rand_score,
                             normalized_mutual_info_score)
import umap

stages = master["stage"].values
roots = master["root_buckwalter"].values

km = KMeans(n_clusters=6, n_init=20, random_state=42).fit(emb)
sil = silhouette_score(emb, stages, metric="cosine")
ari = adjusted_rand_score(stages, km.labels_)
nmi = normalized_mutual_info_score(stages, km.labels_)

scores = {"silhouette_vs_stage": float(sil),
          "ari_kmeans_vs_stage": float(ari),
          "nmi_kmeans_vs_stage": float(nmi)}
with open(OUTDIR / "silhouette.json", "w") as f:
    json.dump(scores, f, indent=2)
print(scores)

# %%
reducer = umap.UMAP(n_components=2, metric="cosine", random_state=42,
                    n_neighbors=15, min_dist=0.1)
xy = reducer.fit_transform(emb)

fig, ax = plt.subplots(figsize=(10, 8), dpi=160)
palette = ["#94a3b8", "#a8a29e", "#fbbf24", "#f97316", "#dc2626", "#7f1d1d"]
for s in sorted(set(stages)):
    pts = xy[stages == s]
    ax.scatter(pts[:, 0], pts[:, 1], s=22, c=palette[s - 1],
               label=f"Stage {s} (n={len(pts)})", alpha=0.85, edgecolor="white",
               linewidth=0.4)
ax.set_title("CAMeLBERT-CA contextual embeddings, UMAP-2D · colored by manual stage",
             fontsize=12)
ax.legend(loc="best", fontsize=9, frameon=False)
ax.set_xticks([]); ax.set_yticks([])
for sp in ax.spines.values(): sp.set_visible(False)
plt.tight_layout()
plt.savefig(OUTDIR / "embeddings_umap.png", dpi=200, bbox_inches="tight")
plt.show()

# Cluster-vs-stage confusion table.
ct = pd.crosstab(pd.Series(stages, name="stage"),
                 pd.Series(km.labels_, name="kmeans_cluster"))
ct.to_csv(OUTDIR / "cluster_vs_stage.csv")
print(ct)


# %% [markdown]
# ## 4. Analysis 2 — Cross-translation semantic drift
#
# For each of the 312 attestations, fetch 5 English + 5 Persian translations of the host verse,
# embed each translation with a multilingual model, and compute pairwise cosine distances
# *across translations of the same verse*. High drift = the verse is rendered very differently
# by different translators (interpreted as "the lexical distinction is hard to preserve").

# %%
# Translation source: tanzil.net distribution. We use 5 EN + 5 FA editions:
TRANSLATIONS = {
    # English
    "en.sahih":     "https://tanzil.net/trans/en.sahih",
    "en.pickthall": "https://tanzil.net/trans/en.pickthall",
    "en.yusufali":  "https://tanzil.net/trans/en.yusufali",
    "en.arberry":   "https://tanzil.net/trans/en.arberry",
    "en.maududi":   "https://tanzil.net/trans/en.maududi",
    # Persian
    "fa.fooladvand":  "https://tanzil.net/trans/fa.fooladvand",
    "fa.makarem":     "https://tanzil.net/trans/fa.makarem",
    "fa.ghomshei":    "https://tanzil.net/trans/fa.ghomshei",
    "fa.moezzi":      "https://tanzil.net/trans/fa.moezzi",
    "fa.ansari":      "https://tanzil.net/trans/fa.ansari",
}

trans_dir = Path("data/translations")
trans_dir.mkdir(parents=True, exist_ok=True)

import urllib.request
trans_text = {}
for tid, url in TRANSLATIONS.items():
    fp = trans_dir / f"{tid}.txt"
    if not fp.exists():
        urllib.request.urlretrieve(url, fp)
    d = {}
    for line in open(fp, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#"): continue
        parts = line.split("|", 2)
        if len(parts) != 3: continue
        d[(int(parts[0]), int(parts[1]))] = parts[2]
    trans_text[tid] = d
    print(f"Loaded {tid}: {len(d)} verses")

# %%
from sentence_transformers import SentenceTransformer
multi = SentenceTransformer("paraphrase-multilingual-mpnet-base-v2", device=device)

drift_rows = []
for r in tqdm(master.itertuples(), total=len(master), desc="Translation drift"):
    key = (int(r.sura), int(r.aya))
    versions = {}
    for tid in TRANSLATIONS:
        v = trans_text[tid].get(key)
        if v: versions[tid] = v
    if len(versions) < 6: continue

    vecs = multi.encode(list(versions.values()), convert_to_numpy=True,
                         show_progress_bar=False, normalize_embeddings=True)
    # pairwise cosine distances
    sim = vecs @ vecs.T
    np.fill_diagonal(sim, np.nan)
    mean_sim = np.nanmean(sim)
    drift_rows.append({
        "sura": r.sura, "aya": r.aya, "root": r.root_buckwalter,
        "stage": r.stage, "n_translations": len(versions),
        "mean_pairwise_cosine_sim": float(mean_sim),
        "drift": float(1 - mean_sim),
    })

drift_df = pd.DataFrame(drift_rows)
per_root = drift_df.groupby("root").agg(
    n=("drift", "count"),
    mean_drift=("drift", "mean"),
    std_drift=("drift", "std"),
).reset_index().sort_values("mean_drift", ascending=False)
per_root.to_csv(OUTDIR / "translation_drift_per_root.csv", index=False)
print(per_root)

# Plot per-root drift.
fig, ax = plt.subplots(figsize=(10, 5), dpi=160)
ax.bar(per_root["root"], per_root["mean_drift"],
       yerr=per_root["std_drift"], capsize=3, color="#475569", edgecolor="white")
ax.set_xlabel("Spectrum root (Buckwalter)")
ax.set_ylabel("Mean translation drift (1 – mean pairwise cosine sim)")
ax.set_title("Cross-translation semantic drift per root\n10 translations (5 EN + 5 FA), multilingual MPNet")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(OUTDIR / "translation_drift.png", dpi=200, bbox_inches="tight")
plt.show()


# %% [markdown]
# ## 5. Analysis 3 — Diachronic stage-rank correlation
#
# Project each attestation onto the **Nöldeke revelation order** (Mecca early/mid/late, Medina)
# and test whether stage assignment correlates with chronological rank.

# %%
# Nöldeke chronological rank by sura number. Hard-coded here from Sinai (2017, Appendix B).
NOLDEKE_RANK = {
    # (Mecca early) ranks 1-48; (Mecca mid) 49-69; (Mecca late) 70-90; (Medina) 91-114.
    96: 1, 74: 2, 73: 3, 111: 4, 81: 5, 87: 6, 92: 7, 89: 8, 93: 9, 94: 10,
    103: 11, 100: 12, 108: 13, 102: 14, 107: 15, 109: 16, 105: 17, 113: 18,
    114: 19, 112: 20, 53: 21, 80: 22, 97: 23, 91: 24, 85: 25, 95: 26, 106: 27,
    101: 28, 75: 29, 104: 30, 77: 31, 50: 32, 90: 33, 86: 34, 54: 35, 38: 36,
    7: 37, 72: 38, 36: 39, 25: 40, 35: 41, 19: 42, 20: 43, 56: 44, 26: 45,
    27: 46, 28: 47, 17: 48,
    # Mecca mid
    10: 49, 11: 50, 12: 51, 15: 52, 6: 53, 37: 54, 31: 55, 34: 56, 39: 57,
    40: 58, 41: 59, 42: 60, 43: 61, 44: 62, 45: 63, 46: 64, 51: 65, 88: 66,
    18: 67, 16: 68, 71: 69,
    # Mecca late
    14: 70, 21: 71, 23: 72, 32: 73, 52: 74, 67: 75, 69: 76, 70: 77, 78: 78,
    79: 79, 82: 80, 84: 81, 30: 82, 29: 83, 83: 84, 13: 85,
    # Medina
    2: 91, 8: 92, 3: 93, 33: 94, 60: 95, 4: 96, 99: 97, 57: 98, 47: 99, 65: 100,
    98: 101, 62: 102, 59: 103, 24: 104, 22: 105, 63: 106, 58: 107, 49: 108,
    66: 109, 64: 110, 61: 111, 48: 112, 9: 113, 5: 114, 110: 90,
}
master["noldeke_rank"] = master["sura"].map(NOLDEKE_RANK)
miss = master["noldeke_rank"].isna().sum()
if miss:
    print(f"Warning: {miss} attestations have no Nöldeke rank (filled with median)")
    master["noldeke_rank"] = master["noldeke_rank"].fillna(master["noldeke_rank"].median())

# %%
from scipy.stats import spearmanr, kendalltau
r_s, p_s = spearmanr(master["noldeke_rank"], master["stage"])
r_k, p_k = kendalltau(master["noldeke_rank"], master["stage"])
print(f"Spearman ρ = {r_s:.4f}, p = {p_s:.4f}")
print(f"Kendall τ  = {r_k:.4f}, p = {p_k:.4f}")

# Plot.
fig, ax = plt.subplots(figsize=(10, 5), dpi=160)
jitter = (np.random.rand(len(master)) - 0.5) * 0.4
ax.scatter(master["noldeke_rank"], master["stage"] + jitter,
           s=12, alpha=0.45, c="#0f172a")
ax.set_xlabel("Nöldeke chronological rank (1 = earliest)")
ax.set_ylabel("Stage assignment")
ax.set_title(f"Stage vs Nöldekean chronology · Spearman ρ = {r_s:+.3f} (p = {p_s:.3f})")
ax.axvline(48.5, color="#94a3b8", ls=":"); ax.text(24, 6.3, "Mecca early", fontsize=8, ha="center", color="#64748b")
ax.axvline(69.5, color="#94a3b8", ls=":"); ax.text(59, 6.3, "Mecca mid",   fontsize=8, ha="center", color="#64748b")
ax.axvline(90.5, color="#94a3b8", ls=":"); ax.text(80, 6.3, "Mecca late",  fontsize=8, ha="center", color="#64748b")
ax.text(102, 6.3, "Medina", fontsize=8, ha="center", color="#64748b")
plt.tight_layout()
plt.savefig(OUTDIR / "diachronic_plot.png", dpi=200, bbox_inches="tight")
plt.show()

pd.DataFrame({"spearman_rho": [r_s], "spearman_p": [p_s],
              "kendall_tau": [r_k], "kendall_p": [p_k]}).to_csv(
    OUTDIR / "diachronic_stage_rank.csv", index=False)


# %% [markdown]
# ## 6. Analysis 4 — PMI-weighted inter-root collocation network
#
# Replace the raw aya-co-occurrence edge weights (current fig 4/7) with **pointwise mutual information**,
# which controls for marginal frequency. PMI(r1, r2) = log( p(r1, r2) / (p(r1) p(r2)) ).
# A high PMI edge means r1 and r2 co-occur *more than chance* given their individual frequencies.

# %%
from collections import Counter
from itertools import combinations

# Build per-aya root sets.
aya_roots = master.groupby(["sura", "aya"])["root_buckwalter"].apply(set).reset_index()
N_AYAS = 6236  # total Quranic ayāt

# Marginal counts (ayāt containing root r).
root_aya_counts = Counter()
for s in aya_roots["root_buckwalter"]:
    for r in s:
        root_aya_counts[r] += 1

# Joint counts (ayāt containing both r1 and r2).
joint = Counter()
for s in aya_roots["root_buckwalter"]:
    for r1, r2 in combinations(sorted(s), 2):
        joint[(r1, r2)] += 1

ROOTS = sorted(root_aya_counts.keys())
records = []
for (r1, r2), c12 in joint.items():
    p1 = root_aya_counts[r1] / N_AYAS
    p2 = root_aya_counts[r2] / N_AYAS
    p12 = c12 / N_AYAS
    pmi = float(np.log(p12 / (p1 * p2)))
    npmi = pmi / -np.log(p12)  # normalized PMI ∈ [-1, 1]
    records.append({"r1": r1, "r2": r2, "joint": c12,
                    "p1": p1, "p2": p2, "p12": p12,
                    "pmi": pmi, "npmi": npmi})

pmi_df = pd.DataFrame(records).sort_values("npmi", ascending=False)
pmi_df.to_csv(OUTDIR / "pmi_network.csv", index=False)
print(pmi_df.head(20))

# %%
import networkx as nx

G = nx.Graph()
for r in ROOTS: G.add_node(r)
for _, row in pmi_df.iterrows():
    if row.npmi > 0:  # positive collocation only
        G.add_edge(row.r1, row.r2, weight=row.npmi)

pos = nx.spring_layout(G, seed=42, weight="weight", k=0.7)

fig, ax = plt.subplots(figsize=(10, 9), dpi=160)
edge_widths = [G[u][v]["weight"] * 4 for u, v in G.edges()]
edge_colors = [G[u][v]["weight"] for u, v in G.edges()]
nx.draw_networkx_edges(G, pos, width=edge_widths, edge_color=edge_colors,
                       edge_cmap=plt.cm.viridis, alpha=0.7, ax=ax)
nx.draw_networkx_nodes(G, pos, node_size=[root_aya_counts[n] * 15 + 80 for n in G.nodes()],
                       node_color="#0f172a", edgecolors="white", linewidths=1.5, ax=ax)
nx.draw_networkx_labels(G, pos, font_size=10, font_color="white", font_weight="bold", ax=ax)
ax.set_title("PMI-weighted co-occurrence network of 14 spectrum roots\n(Edge: normalized PMI · Node: aya-frequency)")
ax.axis("off")
plt.tight_layout()
plt.savefig(OUTDIR / "pmi_network.png", dpi=200, bbox_inches="tight")
plt.show()


# %% [markdown]
# ## 7. Wrap up
#
# Outputs to copy back to the repo:
# - `outputs/nlp_upgrade/embeddings_arabert.npz`
# - `outputs/nlp_upgrade/embeddings_umap.png`
# - `outputs/nlp_upgrade/cluster_vs_stage.csv`
# - `outputs/nlp_upgrade/silhouette.json`
# - `outputs/nlp_upgrade/translation_drift_per_root.csv`
# - `outputs/nlp_upgrade/translation_drift.png`
# - `outputs/nlp_upgrade/diachronic_stage_rank.csv`
# - `outputs/nlp_upgrade/diachronic_plot.png`
# - `outputs/nlp_upgrade/pmi_network.csv`
# - `outputs/nlp_upgrade/pmi_network.png`
#
# Then in chat, give me the contents of the JSON/CSV files (or upload them to the repo) and I'll
# write the corresponding manuscript subsections:
#
# - **English §4.11 (new)**: "Contextual-embedding corroboration of the six-stage structure"
# - **English §4.10b (new)**: "Quantifying cross-translation semantic drift"
# - **English §4.2.2 (extension)**: "Diachronic null result — stages are not chronological strata"
# - **English §4.8.x (refactor)**: replace raw co-occurrence figure with PMI-weighted network
# - **Persian §۴-۷ (extension)**: translation-drift section anchored to the empirical drift CSV
# - **Persian §۴-۶ (extension)**: PMI re-analysis (Persian version goes deeper on the bridge-role
#   interpretation since that's the comparative-tafsir focus)
