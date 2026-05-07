# Manual validation audit — Quranic Anger-Spectrum Pipeline

This document records the manual verification of the QAC → concordance →
statistics pipeline performed in support of the empirical claims in
*The Phenomenology of the Anger Spectrum in the Qurʾān* (Jabbary &
Jabbary, 2026).

## 1. Headline-verse exemplar audit (n = 14)

For each of the fourteen core spectrum roots, the manuscript identifies
one canonical exemplar verse (§3.6). All fourteen exemplars were
checked against the corpus output (`data/concordance/master_concordance.csv`)
and against the Tanzil Uthmani text (`data/quran/quran_check.json`).

| # | Root | Buckwalter | Exemplar | In master concordance | Surface form correct | Verse text matches Tanzil |
|--:|:----:|:----------:|:--------:|:---------------------:|:--------------------:|:-------------------------:|
| 1 | ʾff | Aff | Q. 17:23 | ✓ | ✓ | ✓ |
| 2 | krh | krh | Q. 2:216 | ✓ | ✓ | ✓ |
| 3 | ḍyq | Dyq | Q. 15:97 | ✓ | ✓ | ✓ |
| 4 | ḥzn | Hzn | Q. 2:38 | ✓ | ✓ | ✓ |
| 5 | ʾsf | Asf | Q. 43:55 | ✓ | ✓ | ✓ |
| 6 | nqm | nqm | Q. 7:126 | ✓ | ✓ | ✓ |
| 7 | sxṭ | sxT | Q. 47:28 | ✓ | ✓ | ✓ |
| 8 | mqt | mqt | Q. 40:10 | ✓ | ✓ | ✓ |
| 9 | ġḍb | gDb | Q. 48:6 | ✓ | ✓ | ✓ |
| 10 | ḥrd | Hrd | Q. 68:25 | ✓ | ✓ | ✓ |
| 11 | ġyẓ | gyZ | Q. 3:134 | ✓ | ✓ | ✓ |
| 12 | bġy | bgy | Q. 42:42 | ✓ | ✓ | ✓ |
| 13 | ṭġy | Tgy | Q. 96:6 | ✓ | ✓ | ✓ |
| 14 | ʿtw | Etw | Q. 25:21 | ✓ | ✓ | ✓ |

All 14/14 (100%) exemplars verified. The Buckwalter↔Arabic round-trip
algorithm and the segment-collapse operation produce no systematic
errors at the surface level for the headline cases.

## 2. Stratified-sample audit for high-frequency roots (n = 50)

For the four roots that contribute the largest share of the corpus
(*ḥzn* 42, *bġy* 96, *ġḍb* 24, *ṭġy* 39 — covering 65 % of all spectrum
attestations), a stratified-random sample of 50 segment-to-root
mappings was drawn (≈12–13 per root, sampled without replacement) and
manually verified against the Tanzil text.

For each sampled segment we checked:
1. The segment's surface form is present in the cited verse;
2. The QAC's ROOT feature for that segment matches the lexicographic
   root identified in Lane's *Lexicon* and the four authoritative
   lexica (Maqāyīs, Mufradāt, Lisān, Taḥqīq); and
3. The segment is correctly assigned to a single word at the
   `(sūra, āya, word)` coordinate after the `collapse_to_words`
   operation.

| Root | n in sample | Correct (3/3) | Notes |
|:-:|:-:|:-:|:-:|
| ḥzn | 13 | 13 (100%) | — |
| bġy | 13 | 13 (100%) | — |
| ġḍb | 12 | 12 (100%) | — |
| ṭġy | 12 | 12 (100%) | — |
| **Total** | **50** | **50 (100%)** | — |

All 50/50 (100%) of segment-to-root assignments were verified correct.
This validates that the QAC's ROOT field aligns with the lexicographic
tradition for the high-frequency spectrum roots, and that the
`collapse_to_words` algorithm preserves morphological identity
correctly across multi-segment tokens.

## 3. What the validation does and does not verify

This validation establishes that, *for the spectrum roots and the four
high-frequency roots audited*, the QAC's ROOT field and our
segment-collapse algorithm align with the lexicographic tradition with
no detected systematic error.

It does **not**:

- audit the QAC's morphological tags exhaustively across all 128,219
  segments (this is the responsibility of the upstream QAC project; see
  Dukes 2011 and the `corpus.quran.com` web tools);
- guarantee zero error rate across the full corpus (the QAC is a
  human-curated dataset and known errata are listed at
  `corpus.quran.com/feedback.jsp`);
- validate the morphological *flag* fields (gender, number, case),
  since the present paper's analyses do not depend on them.

## 4. Reproducing the audit

The headline-verse audit is automated as part of `analysis/extract_concordance.py`
(via the `_validate_exemplars` helper). The stratified-sample audit was
conducted manually with a fixed random seed (numpy.random.seed(2026))
to ensure reproducibility; the sample list and per-segment verdicts
are recorded in `data/concordance/sampled_segments_for_audit.csv`.

---

*Last updated: 2026-04-30. Audit conducted by K. Jabbary.*
