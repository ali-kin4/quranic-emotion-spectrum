# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

This is a **research-paper repository**, not a software product. It contains:

- Two manuscripts (Persian primary, English journal version) under `paper/`.
- A reproducible Python pipeline under `analysis/` that derives every empirical claim, table, and figure in the paper from the Quranic Arabic Corpus (Dukes 2011, GPL).
- Pre-computed CSV outputs (`data/concordance/`) and rendered figures (`figures/`, `figures_fa/`) committed to the repo so reviewers can inspect results without re-running.

The paper argues that fourteen Arabic roots in the Qur'an form a graded **anger** spectrum across **six stages** (pre-anger displeasure → inner pressure → evaluative aversion → active anger → compressed rage → behavioural outcomes). Background on the thesis lives in `README.md` and `paper/{english,persian}/manuscript.md`.

## Running the analysis pipeline

The pipeline is **strictly sequential** — `advanced_metrics.py` and the visualizers read CSVs that `extract_concordance.py` writes. Run from the repo root:

```bash
pip install -r analysis/requirements.txt
python analysis/extract_concordance.py    # writes data/concordance/master_concordance.csv + summary_counts.csv + by_root/*.csv
python analysis/advanced_metrics.py        # writes morphology/statistical_tests/network_centrality/umbrella_cooccurrence CSVs
python analysis/visualize_spectrum.py      # writes figures/fig{1..4}.{pdf,png}
python analysis/visualize_advanced.py      # writes figures/fig{5..7}.{pdf,png}
python analysis/visualize_spectrum_fa.py   # Persian-labelled equivalents → figures_fa/
python analysis/visualize_advanced_fa.py
```

The pipeline is deterministic: identical inputs produce byte-identical CSVs and figure pixels. No tests, no linter, no build system — just these scripts.

## Architecture you must understand before editing

### `analysis/spectrum_roots.py` is the single source of truth

Every other script imports `SPECTRUM`, `EXPANSION`, and the stage labels from here. Three categories exist intentionally:

- **`SPECTRUM`** — the 14 core roots that define the anger spectrum and drive every published statistic and figure.
- **`EXPANSION`** — 5 "umbrella" moral-evaluation roots (ẓlm, jrm, fsq, ʿdw, šnʾ) used only for cross-field robustness checks (`umbrella_cooccurrence.csv`).
- **`DIAGNOSTIC_TAMAYYUZ`** — kept as a separate row purely so `extract_concordance.py` can still emit a per-root CSV for legacy comparison. **Do not** add it to figures or stats: the paper folds tamayyuz into ghayẓ as a manifestation of compressed rage at peak (per reviewer Round 1).

Selectors exist via `all_roots(include_expansion=..., include_diagnostic=...)`. Adding a root means editing this file and re-running the entire pipeline.

### QAC parsing flow

`qac_parser.py` parses the Buckwalter-encoded QAC v0.4 morphology file (one row per *segment*, where a token like وَيَغْضَبُونَ = prefix + stem + suffix segments). `collapse_to_words()` re-aggregates segments back into surface words by `(sura, aya, word)` — concordances and statistics operate on words, never on raw segments.

`buckwalter.py` provides the Buckwalter↔Arabic Unicode mapping. The QAC stores roots as `gDb`, `sxT`, `gyZ`, etc.; user-facing CSVs and figures contain Arabic. Always go through `bw_to_arabic()` for display.

### No scipy / no scikit dependency by design

`advanced_metrics.py` re-implements the binomial PMF, chi-squared statistic, and a hard-coded critical-value table (Wilson–Hilferty fallback for df > 10) so the pipeline runs on a vanilla `pip install -r requirements.txt`. **Do not** introduce `scipy` to "clean this up" — it's a deliberate dependency-budget choice. Eigenvector centrality uses NetworkX power iteration with NaN fallback for the same reason.

### Statistical tests are recomputed dynamically

`statistical_tests()` in `advanced_metrics.py` reads `summary_counts.csv` and `quran_check.json` at runtime — it does **not** hard-code stage totals or the Meccan baseline. The Meccan-rate prior is the proportion of total ayat (not suras) classified Meccan, weighted by `total_verses` per sura. Changing `SPECTRUM` membership reflows every test result automatically; do not paste values from old paper drafts into the code.

### Visualization scripts come in parallel English/Persian pairs

`visualize_spectrum.py` → `figures/`, `visualize_spectrum_fa.py` → `figures_fa/` (same for `_advanced`). The Persian variants reshape and bidi-reorder strings via `arabic_reshaper` + `python-bidi` for correct matplotlib rendering. When changing a figure, update both variants together.

## Building the manuscripts

Both manuscripts are written in Markdown (`paper/{english,persian}/manuscript.md`) and rendered to LaTeX via Pandoc, then compiled with **XeLaTeX** (MiKTeX 25.4 was used for the committed PDFs). The committed `manuscript.tex` and `manuscript_body.tex` are pandoc output; the hand-maintained file is `template.tex`.

- Fonts are bundled under `paper/fonts/` (Amiri for Arabic, Vazirmatn for Persian, EB Garamond for Latin) and referenced with relative `Path = ../fonts/`. **Don't change the font configuration** — both templates depend on these exact filenames.
- Persian template uses **xepersian** for RTL; English template avoids polyglossia/bidi (only short Arabic insertions via `\arb{...}`).
- `\graphicspath{{../../figures/}}` (English) — figures must already exist before TeX compile.

There is no Makefile or build script. Re-rendering PDFs is a manual `pandoc → xelatex` step the authors run locally.

## Reviewer-driven structure (avoid regressing)

The current six-stage / 14-root structure replaced the original four-stage / 10-root design after a major reviewer revision (commit `367ddaa`, then Rounds 1–3 in `15ccb09` / `998e729` / `a2d9748`). Three things are *easy to accidentally undo*:

1. **Tamayyuz is not a separate stage.** It's a manifestation of ghayẓ at peak (Q. 67:8: *takādu tamayyazu min al-ġayẓ* = container collapse).
2. **Stage 6 lexemes carry caveats** (baghy/ṭughyān/ʿutuww often arise from supremacism rather than directly from anger). The `note=` fields on each `SpectrumRoot` record this and are quoted in the manuscript.
3. **The phenomenology-vs-outcomes split test** is meant to *fail to reject* the equal-split null after the reviewer revision — that's not a bug, it's the result the manuscript reports as supporting the caveat.

Read the docstring at the top of `spectrum_roots.py` and the `note=` fields before suggesting changes to the spectrum.
