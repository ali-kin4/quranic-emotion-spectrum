# Quranic Emotion Spectrum
### A Phenomenological–Computational Study of Negative Emotions in the Qur'an

A research-paper repository accompanying:

> *The Phenomenology of Negative Emotions in the Qur'an: A Semantic-Network
> Analysis of Distress, Aggression, and Rebellion Along an Action-Intensity
> Continuum.*

The paper proposes that ten core Arabic roots in the Qur'an—
**ḍyq, ḥzn, ʾsf, sxṭ, ġḍb, ġyẓ, myz, bġy, ṭġy, ʿtw**—form a single graded
semantic field organised by *intensity of action*. The continuum traverses
four phenomenological stages:

| Stage | Theme | Roots |
|-------|-------|-------|
| 1 | Internal distress (pre-anger) | ضيق, حزن, أسف |
| 2 | Explicit anger | سخط, غضب |
| 3 | Explosive rage | غيظ, تميّز من الغيظ |
| 4 | Behavioural rebellion | بغي, طغيان, عتوّ |

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
│   ├── persian/manuscript.md      Persian primary draft (~11,600 words)
│   └── english/manuscript.md      English journal version (~9,400 words)
├── analysis/
│   ├── buckwalter.py              Arabic ↔ Buckwalter transliteration
│   ├── qac_parser.py              Parses Quranic Arabic Corpus v0.4
│   ├── spectrum_roots.py          Defines the 10 core + 6 expansion roots
│   ├── extract_concordance.py     Extraction pipeline → CSV concordances
│   ├── advanced_metrics.py        Morphology, χ²-tests, network centrality
│   ├── visualize_spectrum.py      Generates figures 1–4
│   └── visualize_advanced.py      Generates figures 5–7
├── data/
│   ├── quran/
│   │   ├── qac_morphology.txt     Quranic Arabic Corpus (Dukes 2011, GPL)
│   │   └── quran_check.json       Verse text + Meccan/Medinan metadata
│   └── concordance/
│       ├── master_concordance.csv     833 attestations across 16 roots
│       ├── summary_counts.csv         Per-root frequency table
│       ├── sura_distribution.csv      Per-sura per-root counts
│       ├── morphology_by_root.csv     POS / form breakdown per root
│       ├── statistical_tests.csv      χ² and binomial test results
│       ├── network_centrality.csv     Degree/betweenness/closeness measures
│       ├── umbrella_cooccurrence.csv  Cross-field co-occurrence with ẓlm/jrm/fsq
│       └── by_root/*.csv              Per-root concordances
├── figures/
│   ├── fig1_continuum.{pdf,png}              4-stage spectrum diagram
│   ├── fig2_frequency_by_stage.{pdf,png}     Frequency bars
│   ├── fig3_meccan_medinan.{pdf,png}         Revelation-context distribution
│   ├── fig4_cooccurrence.{pdf,png}           Aya-level co-occurrence network
│   ├── fig5_morphology_stack.{pdf,png}       POS breakdown per root
│   ├── fig6_metaphor_diagram.{pdf,png}       ANGER IS PRESSURIZED CONTAINER
│   └── fig7_centrality.{pdf,png}             Network centrality metrics
├── references/
│   ├── english.bib                BibTeX bibliography for the English version
│   ├── persian.bib                BibTeX bibliography for the Persian version
│   └── classical_sources.md       Annotated edition info for classical works
└── docs/
    ├── original_idea.docx         The original idea document (Persian)
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

### Headline empirical results

- χ²(3) = **165.45**, *p* < 0.001 against uniform stage distribution
- χ²(1) = **7.11**, *p* = 0.008 against equal Stage 1+2+3 vs Stage 4 split
- *sakhaṭ* exclusively Medinan: binomial *p* = **0.026** under H₀ = 0.60
- *jrm* (umbrella) Meccan dominance: binomial *p* < 0.0001
- *baghy* highest betweenness centrality (**0.39**) — bridge node between the
  emotional and the moral-evaluation field
- Q. 67:8 (*takādu tamayyazu min al-ġayẓ*) instantiates Lakoff–Kövecses
  "container collapse" with greater clarity than any English exemplar in the
  CMT literature

---

## Findings at a glance

| Stage | Root | Arabic | n | Meccan | Medinan |
|------:|:----:|:------:|--:|------:|--------:|
| 1 | Dyq | ضيق | 13 | 9 | 4 |
| 1 | Hzn | حزن | 42 | 26 | 16 |
| 1 | Asf | أسف | 5 | **5** | 0 |
| 2 | sxṭ | سخط | 4 | 0 | **4** |
| 2 | ġḍb | غضب | 24 | 13 | 11 |
| 3 | ġyẓ | غيظ | 11 | 3 | 8 |
| 3 | myz | تميّز | 4 | 2 | 2 |
| 4 | bġy | بغي | 96 | 55 | 41 |
| 4 | ṭġy | طغيان | 39 | 29 | 10 |
| 4 | ʿtw | عتوّ | 10 | 9 | 1 |

---

## Citation

If you use this work, please cite the manuscript:

```bibtex
@article{jabbary2026spectrum,
  author  = {Jabbary, Karim and Jabbary, Ali},
  title   = {The Phenomenology of Negative Emotions in the {Qur'\={a}n}:
             A Semantic-Network Analysis of Distress, Aggression, and
             Rebellion Along an Action-Intensity Continuum},
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
