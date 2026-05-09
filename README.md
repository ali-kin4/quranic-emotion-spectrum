# Quranic Emotion Spectrum
### A Phenomenological–Computational Study of the Anger Spectrum in the Qurʾān

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ali-kin4/quranic-emotion-spectrum/blob/master/notebooks/quranic_emotion_spectrum.ipynb)

> **One-click reproducibility.** The notebook above clones this repo into a Colab runtime, verifies the corpus SHA-256, runs the entire pipeline (concordance → statistics → network → figures), regenerates all seven figures in English- and Persian-labelled variants, runs sparse-count robustness diagnostics, and can optionally commit the regenerated outputs back to a feature branch on GitHub. See [`notebooks/quranic_emotion_spectrum.ipynb`](notebooks/quranic_emotion_spectrum.ipynb).

A research-paper repository accompanying a **dual-track scholarly project** (May 2026 revision):

- **English (international target — JQS / Cognitive Linguistics / DSH)**: *The Phenomenology of the Anger Spectrum in the Qurʾān: A Semantic-Network Analysis of Displeasure, Inflammation, and Destructiveness Along an Action-Intensity Continuum* (~14,300 words; full 14-root × 6-stage continuum with state-of-art uncertainty-aware quantitative methodology).
- **Persian (Iranian target — NRGS Isfahan / QHS Imam Sadiq)**: «اوجِ طیفِ خشم در قرآن کریم: قرائتی تطبیقی-تفسیری از مرحله‌های فعّال، متراکم، و پیامدی» (~10,500 words; tafsir-comparative companion paper focused on Stages 4–6, with deep nine-tafsir engagement).

The two papers share data infrastructure but answer different scholarly questions — fully COPE/ICMJE-compliant via substantive differentiation rather than translated republication.

The paper argues that **fourteen** core Arabic roots in the Qurʾān—
**ʾff, krh, ḍyq, ḥzn, ʾsf, nqm, sxṭ, mqt, ġḍb, ḥrd, ġyẓ, bġy, ṭġy, ʿtw**—form
a single graded semantic field organised by *intensity of action*. The
continuum traverses **six** phenomenological stages:

| Stage | Theme | Roots |
|-------|-------|-------|
| 1 | Pre-anger displeasure | أُفّ, كره |
| 2 | Inner pressure / contraction | ضيق, حزن, أسف |
| 3 | Evaluative aversion | نقم, سخط, مقت |
| 4 | Active anger | غضب, حرد |
| 5 | Compressed / explosive rage | غيظ (with *tamayyuz* as manifestation) |
| 6 | Behavioural outcomes (with caveats: bidirectional causation) | بغي, طغيان, عتوّ |

The paper combines three methodological lenses—Izutsu-style semantic-field
analysis, scalar semantics in the Kennedy–Sassoon tradition, and conceptual
metaphor theory after Lakoff and Kövecses—and validates the proposed continuum
against the **Quranic Arabic Corpus** (Dukes 2011) using a fully reproducible
Python pipeline.

Two empirical findings emerge as novel:

1. **سخط** is attested *exclusively* in Medinan suras (0 Meccan / 4 Medinan).
2. **أسف** is attested *exclusively* in Meccan suras (5 Meccan / 0 Medinan).

The Stage-4 (behavioural rebellion) vocabulary is approximately **2.4× more
frequent** than the combined first three stages, suggesting that the Qur'an
foregrounds the *behavioural outcomes* of unmanaged emotion as warning rather
than describing inner phenomenology for its own sake.

---

## Repository structure

```
quranic-emotion-spectrum/
├── paper/
│   ├── english/manuscript.{md,tex,pdf}  English JQS-target version (~14,300 words, 35pp)
│   └── persian/manuscript.{md,tex,pdf}  Persian NRGS-target tafsir-companion (~10,500 words, 33pp)
├── analysis/
│   ├── buckwalter.py              Arabic ↔ Buckwalter transliteration
│   ├── qac_parser.py              Parses Quranic Arabic Corpus v0.4
│   ├── spectrum_roots.py          14 core + 5 umbrella roots; 6-stage definition
│   ├── extract_concordance.py     Extraction pipeline → CSV concordances
│   ├── advanced_metrics.py        χ², monotonic-trend, permutation null,
│   │                              Cramér's V / Cohen's w, FDR (Holm-Bonferroni),
│   │                              bootstrap CIs (1000 resamples), centrality
│   ├── visualize_spectrum.py      Generates figures 1–4
│   └── visualize_advanced.py      Generates figures 5–7
├── data/
│   ├── quran/
│   │   ├── qac_morphology.txt     QAC v0.4 (Dukes 2011, GPL); SHA-256 pinned
│   │   └── quran_check.json       Verse text + Meccan/Medinan metadata
│   └── concordance/
│       ├── master_concordance.csv         312 spectrum + 544 umbrella attestations
│       ├── summary_counts.csv             Per-root frequency table
│       ├── sura_distribution.csv          Per-sura per-root counts
│       ├── morphology_by_root.csv         POS / form breakdown per root
│       ├── statistical_tests.csv          χ², trend tests, FDR, sensitivity table
│       ├── network_centrality.csv         Centrality + bootstrap 95% CIs
│       ├── umbrella_cooccurrence.csv      Cross-field co-occurrence
│       ├── stage6_causation_coding.csv    κ=0.79 anger-derived/structural audit
│       ├── validation_audit.md            14/14 + 50/50 manual validation
│       └── by_root/*.csv                  Per-root concordances
├── figures/ (and figures_fa/)
│   ├── fig1_continuum.{pdf,png}              6-stage spectrum diagram
│   ├── fig2_frequency_by_stage.{pdf,png}     Frequency bars
│   ├── fig3_meccan_medinan.{pdf,png}         Revelation-context distribution
│   ├── fig4_cooccurrence.{pdf,png}           Aya-level co-occurrence network
│   ├── fig5_morphology_stack.{pdf,png}       POS breakdown per root
│   ├── fig6_metaphor_diagram.{pdf,png}       Container-collapse schema
│   └── fig7_centrality.{pdf,png}             Network centrality (with CI panel)
├── references/
│   ├── english.bib                BibTeX bibliography (incl. Kövecses 2025,
│   │                              Gaanoun & Alsuhaibani 2025, Khan 2025, etc.)
│   ├── persian.bib                BibTeX bibliography for Persian version
│   └── classical_sources.md       Annotated edition info for classical works
└── docs/
    ├── original_idea.docx         Original idea document (Persian)
    └── extracted_idea.txt         Plain-text extraction
```

---

## Reproducing the analysis

The analysis is fully reproducible end-to-end:

```bash
# 1. Install Python dependencies
pip install -r analysis/requirements.txt

# 2. (Optional) Re-download the corpus if absent
#    qac_morphology.txt is from https://corpus.quran.com (GPL, Dukes 2011)
#    quran_check.json is JSON-formatted Tanzil text + metadata.

# 3. Run the extraction pipeline (writes to data/concordance/)
python analysis/extract_concordance.py

# 4. Run the advanced metrics (morphology, statistical tests, network centrality)
python analysis/advanced_metrics.py

# 5. Generate figures 1–4 (writes to figures/)
python analysis/visualize_spectrum.py

# 6. Generate figures 5–7 (writes to figures/)
python analysis/visualize_advanced.py
```

The pipeline is deterministic; identical inputs produce byte-identical CSVs
and figure pixels.

### Headline empirical results (May 2026 revision — research-grade methodology)

**Statistical findings, reported with full uncertainty awareness:**

- **Asymptotic χ²(5) = 227.15** against uniform six-stage distribution; Cohen's *w* = 0.85 (large effect). However, **marginal-preserving permutation null** *p* = 0.24 indicates the asymptotic *p*-value over-states evidence on this sparse, marginally-imbalanced design — the substantive case for the six-stage architecture rests on qualitative lexicographic, exegetical, and metaphorical evidence rather than the omnibus *p*-value alone.
- **Three monotonic-trend tests** all fail to reject the no-trend null (Spearman ρ = −0.09, *p* = 0.85; Mann-Kendall *p* = 0.71; Cochran-Armitage-style OLS *p* = 0.40) — the *expected* result, since the continuum is an ordering of *semantic* intensity, not of attestation frequency.
- **Phenomenology-vs-outcomes split** χ²(1) = 1.55 (Cohen's *w* = 0.07, trivial effect) — fails to reject. *Consistent with* the bidirectional-causation reading of Stage 6, supported by the κ = 0.79-validated tafsir-coding audit (26% A / 49% S / 25% A+S; A-only re-analysis χ²(1) = 81.4, *p* < 0.001).
- ***sakhaṭ* exclusively Medinan** (0/4): raw binomial *p* = 0.005 (robust across baselines 0.70–0.78); **Holm-Bonferroni adjusted *p* = 0.05** over the family of 14 per-root binomials — borderline rather than emphatic post-FDR. The only spectrum root surviving FDR correction at α = 0.05.
- **Network centrality** point-estimate: *baghy* highest closeness 0.55, betweenness 0.15 (tied with *ghaḍab*, *asaf*); **bootstrap 95% percentile CIs** are wide (e.g., *baghy* betweenness ∈ [0.00, 0.31]; closeness ∈ [0.23, 0.84]), reflecting the small graph (14 nodes); bridging-role claim is *consistent with* point estimates, qualified by bootstrap.
- **Q. 67:8 container-collapse claim** softened to "an unusually transparent linguistic instance" (the verb *tamayyaza* lexicalises the disintegration of the *vessel* itself rather than the exit of *contents*); strong universalist claim reserved pending a cross-cultural philological survey commended in §5.6.

---

## Findings at a glance — full 14-root × 6-stage continuum

| Stage | Root | Arabic | n | Meccan | Medinan | Note |
|------:|:----:|:------:|--:|------:|--------:|:--|
| 1 | ʾff | أفّ | 3 | 3 | 0 | All Meccan; lowest verbal displeasure |
| 1 | krh | كره | 41 | 14 | 27 | Dual karāha/ikrāh structure |
| 2 | ḍyq | ضيق | 13 | 9 | 4 | Inner constriction (*ḍīq al-ṣadr*) |
| 2 | ḥzn | حزن | 42 | 26 | 16 | Most frequent Stage 2; 88% verbal |
| 2 | ʾsf | أسف | 5 | 5 | 0 | Suggestive Meccan-only (raw *p* = 0.34, adj. 1.00) |
| 3 | nqm | نقم | 17 | 12 | 5 | Vengeful disapproval; *al-Muntaqim* |
| 3 | sxṭ | سخط | 4 | 0 | **4** | **Holm-adj. *p* = 0.05** — borderline post-FDR |
| 3 | mqt | مقت | 6 | 4 | 2 | *Ashaddu al-ibghāḍ* (Zajjāj) |
| 4 | ġḍb | غضب | 24 | 13 | 11 | Central anger lexeme |
| 4 | ḥrd | حرد | 1 | 1 | 0 | Qurʾānic hapax (Q. 68:25) |
| 5 | ġyẓ | غيظ | 11 | 3 | 8 | Compressed rage; *kaẓm* metaphor |
| 6 | bġy | بغي | 96 | 55 | 41 | Bridge node; bidirectional |
| 6 | ṭġy | طغيان | 39 | 29 | 10 | Pharaonic; appraisal of *istighnāʾ* |
| 6 | ʿtw | عتوّ | 10 | 9 | 1 | Settled defiance; *istikbār*-attached |
| **Σ** | — | — | **312** | **183** | **129** | |

---

## Citation

If you use this work, please cite the manuscript:

```bibtex
@article{jabbary2026spectrum,
  author  = {Jabbary, Karim and Jabbary, Ali},
  title   = {The Phenomenology of the Anger Spectrum in the {Qur'\={a}n}:
             A Semantic-Network Analysis of Displeasure, Inflammation,
             and Destructiveness Along an Action-Intensity Continuum},
  year    = {2026},
  affiliation = {Urmia University, Iran},
  note    = {Manuscript draft; repository at
             github.com/ali-kin4/quranic-emotion-spectrum}
}
```

The corpus must be cited separately:

> Dukes, Kais. (2011). *Quranic Arabic Corpus, Morphology v0.4*.
> University of Leeds. https://corpus.quran.com (GPL)

---

## License

- Manuscripts (`paper/`) — Creative Commons Attribution 4.0 (CC-BY-4.0).
- Code (`analysis/`) — MIT License.
- The Quranic Arabic Corpus data (`data/quran/qac_morphology.txt`) is
  redistributed under its original GPL license; see the file's copyright
  header for terms.
- The Tanzil Quran text data (`data/quran/quran_check.json`) is derived from
  Tanzil under CC-BY-ND 3.0.

See `LICENSE` for the full text of MIT and CC-BY-4.0.

---

<div dir="rtl" lang="fa">

## معرفی پژوهش (فارسی)

این انباره، حاوی نسخه‌های پیش‌نویسِ مقاله **«پدیدارشناسی عواطف منفی در قرآن کریم: تحلیل شبکه معنایی آزردگی، پرخاشگری و عصیان بر اساس شدت کنش»** و کلِ زیرساختِ پژوهشیِ آن است.

این پژوهش با تلفیقِ سه چارچوبِ روش‌شناختی—معناشناسی میدانیِ ایزوتسو، معناشناسی طیفی، و زبان‌شناسی شناختی—نشان می‌دهد که ده ریشه عربیِ کانونی در قرآن (ضيق، حزن، أسف، سخط، غضب، غيظ، ميز، بغي، طغي، عتو) یک پیوستارِ معنایی واحدِ چهارمرحله‌ای را تشکیل می‌دهند که با متغیرِ «شدت کنش» سامان‌بندی شده است.

تحلیلِ پیکره‌ایِ ۸۳۳ بسامد در کلِ قرآن، با استفاده از پیکره ریخت‌شناختی قرآنی (دوکس، ۲۰۱۱)، دو الگوی توزیعی شایانِ توجه را آشکار می‌سازد: انحصارِ مدنیِ «سَخَط» و انحصارِ مکیِ «أَسَف». افزون بر این، مرحله چهارم (واژگانِ عصیان) تقریباً ۲٫۴ برابرِ مجموع سه مرحله نخست بسامد دارد؛ یافته‌ای که نقشِ تربیتی-هدایت‌گرایانه‌ی متن را در پیشِ چشم می‌نهد.

نسخه پیش‌نویسِ فارسی در `paper/persian/manuscript.md` و نسخه فشرده‌ی انگلیسی در `paper/english/manuscript.md` در دسترس‌اند. کلِ خط لوله تحلیلی با چهار خط فرمان قابلِ بازتولید است.

</div>
