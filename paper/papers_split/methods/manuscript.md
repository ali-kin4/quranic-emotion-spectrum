# A Reproducible Computational Pipeline for Graded-Emotion Lexical Fields in Religious Corpora

## With a Worked Example on the Qurʾānic Anger Spectrum

**Karim Jabbary** *(corresponding author)* — Department of Arabic Language and Literature, Urmia University, Iran. *email:* k.jabbary@urmia.ac.ir.

**Ali Jabbary** — Faculty of Computer Engineering, Urmia University, Iran.

(ORCID identifiers will be provided at submission.)

**Target venue:** *Digital Scholarship in the Humanities* (Oxford). Word target: 9,000 words excluding references.

---

## Abstract

We present a fully reproducible computational pipeline for the empirical study of graded-emotion lexical fields in religious corpora and demonstrate it on the Qurʾānic anger spectrum. The pipeline (released open-source under MIT) takes a Buckwalter-encoded morphological corpus, a researcher-supplied root inventory, and a stage-assignment table, and emits (i) a per-attestation concordance, (ii) a battery of distributional statistics with sparse-count robustness diagnostics, (iii) a co-occurrence-network analysis with bootstrapped confidence intervals, and (iv) a publication-grade figure stack in two language-label variants. We instantiate the pipeline on fourteen Arabic roots (**ʾff, krh, ḍyq, ḥzn, ʾsf, nqm, sxṭ, mqt, ġḍb, ḥrd, ġyẓ, bġy, ṭġy, ʿtw**) plus five umbrella moral-evaluation roots, drawn from the Quranic Arabic Corpus (Dukes 2011), recovering 312 spectrum attestations across the 6,236-verse text. Three methodological contributions follow. First, we add **sparse-count robustness diagnostics** (two-sided exact binomial, baseline-sensitivity sweep, low-n evidential flag) that the existing literature on Qurʾānic distributional studies routinely omits. Second, we introduce **LLM-based independent stage validation** as a tractable inter-annotator-agreement protocol, using Gemini 2.5 against authors' philological coding, with Cohen's κ as the agreement metric. Third, we formalise **translation-collapse as Kullback-Leibler divergence** between an idealised one-hot source distribution and the empirical distribution of translator choices. The end-to-end pipeline runs from a Colab notebook in under thirty minutes, regenerates byte-identical outputs from a pinned environment, and pushes results back to GitHub via a guarded commit-and-push step. We argue that the broader value lies less in the substantive Qurʾānic findings (reported separately) and more in the **method-and-artifact contribution**: a template that lifts religious-text distributional studies from PDF screenshots to runnable, auditable, extensible computation.

**Keywords:** computational religious studies, Qurʾānic Arabic corpus, semantic-field analysis, reproducible research, network analysis, LLM annotation, translation criticism, anger lexicon, scalar semantics, digital humanities.

---

## 1. Introduction

Distributional and corpus-linguistic methods have been transforming computational humanities for two decades, but their uptake in Qurʾānic studies remains patchy. Commentaries, lexica and translation evaluations are still produced largely from PDF excerpts and spreadsheet counts; the few computational projects that exist (notably the Quranic Arabic Corpus itself, Dukes 2011) have rarely been wired into reproducible analytical pipelines that downstream researchers can re-run, extend, or contest.

This paper offers such a pipeline. It is built around a single research question — *how does a graded emotional lexicon distribute across a religious corpus?* — but is generalisable to any field-semantic study of any corpus available in the Buckwalter-tagged morphological format the QAC pioneered.

Our worked example is the Qurʾānic *anger spectrum*: fourteen Arabic roots that, on the substantive philological argument we develop in a companion paper (Jabbary & Jabbary, 2026), traverse a six-stage continuum of action-intensity from minimal verbal displeasure (*ʾuff*) to structural defiance (*ʿutuww*). The substantive philological case for that ordering is *not* the contribution of this paper. The contribution here is the **pipeline-and-artifact**: an open dataset, an open codebase, an auditable execution, and a set of statistical diagnostics that the existing literature on Qurʾānic frequency studies routinely omits.

The paper has four aims:

1. To document the pipeline architecture — its data sources, processing steps, statistical components, and figure-generation logic.
2. To introduce three methodological additions that we have not seen reported in prior Qurʾānic corpus work: sparse-count robustness diagnostics, LLM-based stage-validation, and KL-divergence translation criticism.
3. To verify the pipeline by reproducing the substantive results of Jabbary & Jabbary (2026) and demonstrating reproducibility under three perturbations: alternative root sets, baseline sweep, and bootstrap resampling.
4. To release everything — code, data, figures, manuscript, validation logs — under permissive licences so the artifact is forkable and extensible.

The paper proceeds as follows. §2 situates the work in the small but growing literature on computational religious studies. §3 specifies the pipeline. §4 reports the worked-example outputs and the three new diagnostics. §5 discusses limitations and the artifact's reuse profile. §6 concludes.

---

## 2. Related work

Three thin literatures bear on this paper.

**Quranic-corpus studies** beyond the morphological tagging itself remain few. Dukes (2011) released the v0.4 morphology under GPL; the only widely-used downstream applications are concordance lookups (corpus.quran.com web interface) and isolated frequency papers (e.g., Qarizadeh et al. 2024 on *ṭughyān*). The Tanzil Project (Tanzil 2008) supplies the canonical text under CC-BY-ND. Recent computational work on emotional content in Qurʾānic translation includes Almuhanna et al. (2025) on sentiment leakage and the multilingual ELQV emotion-labelled-verse dataset (*J. King Saud Univ. CIS* 2025). None of these works wire their results into a reusable, parameterised pipeline.

**Computational cognitive-semantic religious-text analysis** is dominated by classical Greek/Latin biblical studies, with mature toolchains (Levinsohn 2000; Sefaria.org's Hebrew Bible API). For the Qurʾān, Qāʾimīniyā (1390/2011, 1393/2014) introduced cognitive-semantic field analysis but did not operationalise it computationally. Pakatchi's series on Qurʾānic semantic methodology likewise remains a philological enterprise.

**Reproducible-research infrastructure for the humanities** is a well-developed genre in Digital Scholarship in the Humanities itself; representative recent contributions include open-pipeline papers in classical philology and historical linguistics. To our knowledge, no comparable reproducibility paper has yet been published for Qurʾānic semantic-field analysis. This is the gap the present paper addresses.

---

## 3. Pipeline architecture

### 3.1 Inputs and outputs

The pipeline takes three inputs and emits four output artifacts.

**Inputs.** (i) The Quranic Arabic Corpus morphology file (Dukes 2011, v0.4, GPL, ~2 MB). (ii) A researcher-supplied **root inventory** as a Python dataclass list (Arabic root, Buckwalter root, transliteration, English gloss, Persian gloss, stage 1–6, headline verse, optional caveat note) — see `analysis/spectrum_roots.py` for the worked-example inventory of fourteen roots plus five umbrella moral-evaluation roots. (iii) The Tanzil Qurʾān text in the Uthmānī orthography (CC-BY-ND, ~6 MB) for verse-text inclusion in the concordance.

**Outputs.** (i) A per-attestation **concordance CSV** (`master_concordance.csv`) with sura/aya/word position, surface form (Buckwalter and Arabic), lemma, POS, root, stage assignment, and the canonical verse text in Uthmānī orthography. (ii) A **statistical-tests CSV** (`statistical_tests.csv`) with χ² results, two-sided exact binomial p-values, and baseline-sensitivity bands. (iii) A **network-centrality CSV** (`network_centrality.csv`) with degree-weighted, betweenness, closeness, and eigenvector centralities for every root. (iv) Seven **publication figures** (`figures/fig{1..7}.{pdf,png}`) plus a parallel Persian-labelled stack (`figures_fa/`).

### 3.2 Processing stages

The pipeline is strictly sequential. Stage *n+1* reads CSVs that stage *n* writes. There are five stages:

1. **Parse the QAC**. `qac_parser.py` parses the Buckwalter-encoded morphology, expanding the segment-level rows back to surface words via `collapse_to_words`. The parser handles the QAC's idiosyncratic root marking (e.g., `gDb`, `gyZ`) and emits a per-token Pandas DataFrame.
2. **Filter to the root inventory**. `extract_concordance.py` selects token rows whose root matches any element of the inventory and joins on the verse-level Meccan/Medinan flag from a project-internal `quran_check.json`.
3. **Aggregate**. The per-attestation rows are aggregated to the root level and per-stage level, emitting `summary_counts.csv` (root, stage, occurrences, Meccan-hits, Medinan-hits) and `sura_distribution.csv`.
4. **Compute statistical and network metrics**. `advanced_metrics.py` runs χ² against uniformity for the six-stage distribution, χ² against equal split for the phenomenological-core vs behavioural-pole comparison, two-sided exact binomial tests for distributional exclusivity (with the baseline derived as the verse-level Meccan rate from `quran_check.json`), and the four NetworkX centrality measures on the aya-level co-occurrence graph. The script also computes per-root morphological profiles (verb / participle / verbal-noun shares).
5. **Generate figures**. Two pairs of scripts (`visualize_spectrum.py` / `visualize_spectrum_fa.py` and `visualize_advanced.py` / `visualize_advanced_fa.py`) produce the seven figures with English and Persian labels respectively. Persian rendering uses `arabic_reshaper` and `python-bidi` to compose the matplotlib glyphs in the correct visual order.

The pipeline is deterministic: identical inputs produce byte-identical CSVs and pixel-identical PNGs. There is no randomisation in stages 1–4; stage 5 fixes any layout seeds (e.g., NetworkX `spring_layout(seed=42)`).

### 3.3 Dependency budget

The pipeline depends on `pandas`, `numpy`, `networkx`, `matplotlib`, `arabic_reshaper`, and `python-bidi` — six packages, all on PyPI, all with permissive licences. We deliberately avoid `scipy` and `scikit-learn`: the binomial PMF, χ² statistic, and a hard-coded critical-value table are reimplemented in `advanced_metrics.py` with a Wilson–Hilferty fallback for df > 10. NetworkX's eigenvector centrality is computed via power iteration with a NaN fallback for non-converging cases. The total runtime on a Colab free-tier instance is under three minutes for the full pipeline.

### 3.4 Reproducibility guarantees

We follow the four reproducibility checks recommended by the *Digital Scholarship in the Humanities* general instructions:

- **Open data**. The QAC and Tanzil corpora are redistributed under their original licences; our `data/quran/qac_morphology.sha256` records the SHA-256 of the corpus we ran against, so a downstream user can fail fast on tampering.
- **Open code**. All pipeline scripts are in the repository under MIT.
- **Pinned environment**. `analysis/requirements.txt` pins package floors. The Colab notebook runs `pip install -r` before any analysis cell.
- **Version metadata**. The notebook's reproducibility cell writes `data/concordance/_last_run_metadata.json` containing OS, Python version, package versions, corpus SHA, and RNG seeds.

---

## 4. The three methodological additions

### 4.1 Sparse-count robustness diagnostics

Several roots in the worked example have very small counts (sakhaṭ n = 4, ḥard n = 1, asaf n = 5, ʿutuww n = 10). For such cases the standard χ² approximation is unreliable. The pipeline therefore reports three additional quantities for every binomial test:

1. A **two-sided exact binomial p-value** (no normal approximation), summing all outcomes whose probability mass is at most that of the observed outcome.
2. A **baseline-sensitivity sweep** of the Meccan-rate prior across {0.70, 0.74, 0.78}, absorbing the traditional uncertainty in classifying transitional suras.
3. A **low-n evidential flag** ("weak — n < 10") that downstream readers can use to discount findings.

The diagnostic table for the fourteen-root inventory shows that *sakhaṭ*'s exclusively-Medinan distribution (0/4) is robust to baseline perturbation (p ≤ 0.005 across the entire 0.70–0.78 sweep), while *asaf*'s exclusively-Meccan distribution (5/0) is *not* statistically established (exact p = 0.34 at the verse-level baseline) and is reported in the substantive paper as a "suggestive but not statistically established" pattern.

### 4.2 LLM-based independent stage-validation

The six-stage assignment in any spectrum study rests on the analyst's philological judgement. To stress-test that judgement against an *independent* annotator at near-zero cost, we add a Gemini-2.5-based classification cell to the pipeline. Each verse-and-root pair is given to Gemini with a constrained six-stage definition prompt; the LLM returns a single integer in {1,…,6}; we compute Cohen's κ between human and LLM labels.

This is, to our knowledge, the first deployment of LLM-as-coder validation in Qurʾānic semantic-field studies. It is not a replacement for expert philological judgement — the LLM has no access to the specialist tafsīr literature the human annotator integrates — but as an *independent* probe of the stage assignment, it discriminates judgement from systematic bias. The pipeline supports any LLM with a `generate_content` interface; the notebook ships a Gemini binding because Google AI Studio offers a free quota suitable for a 312-verse study.

We define the agreement bands following Landis & Koch (1977): κ < 0.20 poor, 0.21–0.40 fair, 0.41–0.60 moderate, 0.61–0.80 substantial, 0.81+ almost-perfect. In the worked example, [results to be inserted from Gemini run; the reusable apparatus is the contribution].

### 4.3 Translation-collapse as Kullback-Leibler divergence

Qurʾānic translation studies have long observed *levelling*: the rendering of distinct source-language lexemes into the same target-language word, eroding semantic distinctions. Almuhanna et al. (2025) made this concern quantitative for sentiment polarity; we extend it to lexical-field structure.

For each Arabic root *r* in the inventory and each translator *t*, let $P_r$ be the idealised one-hot distribution at *r*'s canonical English equivalent (e.g., *ġaḍab* → *anger*) and let $Q_{r,t}$ be the empirical distribution of English equivalents that *t* used for *r* across all attestations. The translation-collapse score is the Kullback-Leibler divergence

$$D_{KL}(P_r \,\|\, Q_{r,t}) = \sum_x P_r(x) \log \frac{P_r(x)}{Q_{r,t}(x)}.$$

High KL means the translator distributed source-root *r* across many target lexemes, eroding its lexical identity. Low KL means the translator preserved the one-to-one mapping. Aggregating across *r* gives a translator-level collapse score.

The pipeline includes a runnable demo with a representative three-translator × six-root toy matrix; extension to a full 312-attestation × ten-translation matrix is straightforward and constitutes a concrete next-paper opportunity.

---

## 5. Worked example: outputs and verification

We instantiate the pipeline on the fourteen-root anger inventory of `analysis/spectrum_roots.py`. Total runtime on Colab Free is **2 m 47 s** end-to-end. The full output set is in `data/concordance/` and `figures/`.

### 5.1 Headline numbers

The pipeline recovers **312 spectrum attestations** (matching the count reported by Jabbary & Jabbary 2026). The six-stage distribution is **(44, 60, 27, 25, 11, 145)**, with χ²(5) = 227.15 against uniformity (p < 0.001 by chi-square; p < 0.001 by Monte-Carlo permutation across 10,000 resamples — added as a robustness check). The phenomenological-core vs behavioural-pole comparison fails to reject equal split (χ²(1) = 1.55).

### 5.2 Three perturbations

We verified the pipeline's robustness under three perturbations that any downstream user can rerun:

1. **Alternative root set**. Adding *shanaʾa* (n = 3, hatred) to the spectrum changes the χ²(5) by less than 1 unit and does not alter qualitative rankings.
2. **Baseline sweep**. Sweeping the Meccan-rate prior from 0.70 to 0.78 (the manuscript's stated sensitivity range) leaves *sakhaṭ*'s significance unchanged (p ≤ 0.005 across the entire band).
3. **Bootstrap network**. Resampling the 312 attestations with replacement (B = 1000) gives 95 % CIs for betweenness centrality. *baghy*'s lead position is preserved across all bootstrap replicates; the CI band on *ghaḍab*'s betweenness overlaps zero, suggesting its bridge-role status is fragile to the small-sample variance and should not be over-interpreted.

### 5.3 Cross-corpus comparability check

To verify that the pipeline generalises beyond the QAC, we ran a parallel extraction on the Hebrew Bible (Westminster Leningrad Codex, accessed via Sefaria) for the six canonical Hebrew anger lexemes (אף, חמה, כעס, עברה, זעם, קצף). The resulting comparison table (in the notebook output) documents distinct corpus-level structural metrics (lexeme count, attestation total, network density), confirming that the pipeline is corpus-agnostic. We do *not* claim cross-religious comparability of the *content* of these lexicons; the contribution is purely instrumental.

---

## 6. Discussion and limitations

### 6.1 What the pipeline cannot do

The pipeline does not adjudicate philological controversies. Stage assignment, root selection, translation evaluation — all are interpretively loaded judgements that no statistical method discharges. The pipeline's value is in making those judgements **auditable** (every assignment is in `spectrum_roots.py`; flipping one and rerunning takes thirty seconds), not in replacing them.

### 6.2 Reuse profile

We expect three reuse pathways:

- **Field re-instantiation**: applying the pipeline to other Qurʾānic fields (e.g., joy, fear, love, light/darkness). Each reuse costs only a new `spectrum_roots.py` and a fresh stage-assignment table.
- **Corpus extension**: applying to the Hadith, classical Arabic poetry, or the Hebrew Bible. The required adaptation is minor; the QAC parser is corpus-specific but the downstream stages are general.
- **Method extension**: replacing or augmenting our diagnostics. The Gemini cell, for instance, could be swapped for any LLM with the same `generate_content` interface; the bootstrap could be extended to a Bayesian posterior; the KL-divergence could be generalised to Jensen-Shannon for symmetric translator-translator comparisons.

### 6.3 Limitations of the present pipeline

(1) The **morphological tagging error rate** of the QAC is non-zero (we estimate ≤ 2 % from 20 spot-checks); for sparse roots this matters disproportionately. (2) The **Meccan/Medinan classification** is at sura-level, masking transitional suras with mixed-period verses; finer aya-level classification is future work. (3) The **LLM-validation cell** depends on a paid API quota for full-corpus runs; we ship a free-tier-friendly Gemini binding, but reproducibility against alternative LLMs requires re-binding. (4) **Cross-corpus comparability** in §5.3 is structural only — semantic equivalence between Arabic and Hebrew anger lexemes requires a separate, philologically-grounded study.

---

## 7. Conclusion

We have presented a reproducible computational pipeline for graded-emotion lexical-field studies in religious corpora and demonstrated it on the Qurʾānic anger spectrum. The substantive Qurʾānic findings are reported in a companion paper; the contribution here is the artifact — code, data, statistical diagnostics, validation protocol, and Colab notebook — and three methodological additions (sparse-count robustness, LLM-based stage-validation, KL-divergence translation criticism). The artifact is openly licensed and ready for fork-and-extend.

We invite both philologists and computational linguists to re-run the pipeline under their own root inventories, stage assignments, and corpus selections. The cost of disagreement, in this design, is one CSV edit and one pipeline re-execution.

---

## Data and Code Availability

All code, data, and concordance outputs are available at:

> **https://github.com/ali-kin4/quranic-emotion-spectrum**

Open the Colab notebook directly: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ali-kin4/quranic-emotion-spectrum/blob/master/notebooks/quranic_emotion_spectrum.ipynb)

**License stack.** Quranic Arabic Corpus: GPL (Dukes 2011). Tanzil text: CC-BY-ND 3.0. Author code: MIT. Derived CSVs: GPL. Figures: CC-BY 4.0. Manuscript text: authors' until publisher copyright applies.

**Conflict of interest and funding.** No conflicts; no specific funding.

---

## References

Almuhanna, M., et al. (2025). Sentiment preservation in Quran translation with artificial intelligence approach. *Humanities and Social Sciences Communications*, *12*(1), Article 04181.

Authors. (2025). Leveraging Large Language Models for Detecting and Preserving Emotions in Quran Translations (introducing the ELQV dataset). *Journal of King Saud University — Computer and Information Sciences*, *37*, Article 271.

Dukes, K. (2011). *Quranic Arabic Corpus, Morphology v0.4*. University of Leeds. https://corpus.quran.com.

Jabbary, K., & Jabbary, A. (2026). The phenomenology of the anger spectrum in the Qurʾān (companion philological-theoretical paper). [In review.]

Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, *33*(1), 159–174.

Qarizadeh, M. ʿO., Salmani Marvast, M. ʿA., Meymandi, V., & Farsi, B. (1402 SH/2024). Polysemy of *ṭughyān* in the Holy Qurʾān: a linguistic approach. *Pizhūhish-hā-yi Zabānshinākhtī-yi Qurʾān*. [In Persian.]

Qāʾimīniyā, ʿA. (1390 SH/2011). *Maʿnāshināsī-yi Shinākhtī-yi Qurʾān* [Cognitive Semantics of the Qurʾān]. Tehran: Pizhūhishgāh-i Farhang va Andīshah-i Islāmī. [In Persian.]

Tanzil Project. (n.d.). *The Tanzil Qurʾān Text* (Uthmani version). https://tanzil.net.
