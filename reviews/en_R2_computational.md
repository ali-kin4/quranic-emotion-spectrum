# Reviewer 2 (Computational / Methodological) — JQS
**Recommendation**: Minor revision
**Confidence**: 5

## Summary of the manuscript

Jabbary & Jabbary argue that fourteen Arabic roots in the Qur'anic Arabic Corpus
(QAC v0.4; Dukes 2011) form a graded "anger spectrum" along an action-intensity
axis organised into six phenomenological stages (pre-anger displeasure → inner
pressure → evaluative aversion → active anger → compressed rage → behavioural
outcomes). The paper integrates Izutsu's semantic-field method, Kennedy–Sassoon
scalar semantics, and Lakoff–Kövecses CMT, validated against 312 attestations
through a reproducible Python pipeline (`analysis/extract_concordance.py`,
`analysis/advanced_metrics.py`). Quantitative apparatus includes an asymptotic
χ²(5) omnibus, a marginal-preserving permutation null, three monotonic-trend
tests (Spearman, Mann–Kendall, Cochran–Armitage-style OLS), Holm–Bonferroni-
adjusted exact binomials for Meccan/Medinan tilts (corpus-derived 0.74
ayat-weighted baseline), bootstrap 95% CIs on four centrality measures, a
κ = 0.79-validated tafsir audit of the 145 Stage-6 attestations, and four
NLP extensions (§§4.11–4.14): cross-translation drift with multilingual
MPNet (5 EN + 5 FA), CAMeLBERT-CA contextual embeddings, PMI co-occurrence,
and a Nöldekean diachronic test. The methodological self-discipline is, by
the standards of Qur'anic computational humanities, exemplary: the asymptotic
χ²(5) result is *not* used as load-bearing evidence; failures-to-reject are
explicitly framed as such; effect sizes (Cramér's V, Cohen's w) accompany
every χ²; the permutation, monotonic-trend, and CAMeLBERT-clustering nulls
are each defended as substantively informative; and the bidirectional-
causation reading of Stage 6 is operationalised quantitatively rather than
asserted.

## Major issues

1. **Discrepancies between manuscript-reported p-values and pipeline output for
   *ʿutuww* and *karh*** — §4.8.4 (lines 284), §4.3.1 (line 196), Table 2
   (line 156, 167), abstract / §1.2 originality paragraph (line 35), §4.5.2
   (line 238) — The manuscript's numerical claims are inconsistent within
   itself and with the committed CSV outputs.
   - §4.8.4 reports "*ʿUtuww* (10 attestations; 9 Meccan / 1 Medinan) … raw
     *p* = 0.06; Holm-adjusted *p* = 1.00", but §1.2 reports the same root
     as "*ʿutuww* (9/1)" with "raw 0.47, adj. 1.00", and
     `data/concordance/statistical_tests.csv` row 10 gives raw p = 0.4703
     (which I re-derived by hand: two-sided exact binomial for k = 9, n = 10,
     p = 0.74 is 0.4702). The §4.8.4 value of 0.06 is wrong by an order of
     magnitude and cannot be reproduced by `_binomial_pvalue()` with any
     defensible baseline; the §1.2 / Table-2 number is correct. The 0.06
     figure in §4.8.4 should be replaced by 0.47.
   - Table 2 lists *karh* (line 156) as "*p* = 0.005" and §4.3.1 (line 196)
     repeats "raw *p* = 0.005, Holm-adj. 0.05", but with 14/41 Meccan against
     a 0.74 baseline the actual two-sided exact binomial is *p* ≈ 1.0 × 10⁻⁷
     (re-derived directly from `_binomial_pvalue(14, 41, 0.74)`). The raw p
     is six orders of magnitude smaller than the reported figure, and the
     Holm-adjusted value would survive at α = 0.01, not merely 0.05.
   - The committed `statistical_tests.csv` does not include a *karh*-specific
     row to cross-check, but the family Holm-Bonferroni map computed by
     `_holm_bonferroni()` over all 14 spectrum binomials necessarily
     processes *karh*'s actual raw p; given that *jrm* (raw p = 0.001 in row
     11) survives, *karh* with raw p ~ 10⁻⁷ would emphatically survive.
     The manuscript needs to (i) reconcile the numbers, (ii) state which
     direction the *karh* tilt goes (Table 2 calls it "Medinan-tilted",
     which is correct: 27/41 Medinan against 0.26 expected Medinan rate),
     and (iii) revise §4.3.1 to acknowledge that *karh* is the second root
     to survive FDR, materially upgrading the empirical findings list in
     §1.2 and §6.1.

   **Proposed fix**: Re-run the pipeline, regenerate
   `statistical_tests.csv` so every spectrum root has its own row with raw and
   Holm-adjusted p, and have every numerical claim in the manuscript body
   read off that single CSV. The abstract claim that *only* *sakhaṭ* survives
   FDR is currently inconsistent with the underlying data.

2. **The "welcomed-null" framing of §4.12 (CAMeLBERT) is plausible but
   incomplete; the alternative explanation needs an empirical control** —
   §4.12 (lines 336–344) — The paper reports silhouette = −0.082, ARI = 0.059,
   NMI = 0.077 and reads the result as evidence that the six-stage taxonomy
   adds analytical structure beyond what a pretrained language model recovers
   distributionally. This is a coherent interpretation, but as written the
   section concedes that the embeddings *do* cluster — by root identity —
   without testing it. The natural control is to compute silhouette / ARI /
   NMI against the **root-identity labels** (14 categories) on the same
   embeddings; if those scores are high while the stage scores are at chance,
   the "model captures lexical co-occurrence not phenomenological intensity"
   reading is empirically grounded; if those scores are *also* low, the
   reading is less defensible and the negative result becomes harder to
   absorb. The code is straightforward (just swap `master["stage"].values`
   for `master["root_bw"].values` in the `silhouette_score` /
   `adjusted_rand_score` calls at lines 174–176 of `nlp_upgrade_colab.py`).
   The cluster-vs-stage confusion table at `outputs/nlp_upgrade/cluster_vs_stage.csv`
   already shows the embeddings are *not* trivial — they spread S6 across
   all six clusters and concentrate S2 in cluster 2 (26 / 60 attestations)
   — but the structural claim cannot be settled from a 6×6 table alone.
   A small panel of supplementary scores (root-vs-stage silhouettes; ARI
   against a randomised stage label of the same marginals as a null floor)
   would close this gap and make the welcomed-null defensible at peer-review
   level.

   **Proposed fix**: Add a 3-line supplementary block to §4.12 reporting
   silhouette / ARI against root labels and against a randomly-shuffled
   stage-label baseline. Without these, the section's framing is honest
   but cannot fully shed the "we got a negative result and called it a
   feature" concern.

3. **Diachronic test (§4.14): the Nöldekean rank is an outdated discrete
   ordering and the effect size needs framing** — §4.14 (line 356) and
   `nlp_upgrade_colab.py` lines 313–332 — The Spearman ρ = −0.157 with
   p = 0.006 is reported correctly, but two issues need disclosure. (a)
   Nöldeke's chronology has been substantially revised by Bell, Neuwirth,
   and Sinai (the very monograph cited at lines 81 and 384); using a flat
   1985-style Nöldekean rank without a robustness check against an
   alternative chronology (e.g. Sinai's late-Meccan/early-Medinan refinement,
   or a Bell-ordering robustness column) is methodologically thin. (b)
   ρ² ≈ 2.5% of variance is a small effect, and the line "both reach
   conventional significance but with effect sizes accounting for less
   than 3% of variance" is correct but easy to miss; a confidence interval
   on ρ (Fisher's z-transform) and an explicit "this should be read as a
   null, not as a small but real chronological signal" would help, since
   the *sign* of the correlation (Stage 6 concentrating in narrative-rich
   Medinan suras) is *itself* a substantive Sinai-style observation about
   the discursive evolution of the lexicon. Currently §4.14 reads it
   ambiguously: the headline is "stages are not chronological strata"
   but the underlying ρ is significant.

   **Proposed fix**: Acknowledge Nöldeke's limitations (one sentence
   pointing to Sinai 2017 Appendix B as the canonical revised ordering),
   add a 95% CI on ρ via Fisher's z-transform, and either re-run the
   correlation against Sinai's chronology as a robustness check or
   explicitly defer that to the Phase II agenda already named in §6.3.
   The §4.14 claim is honest as it stands but slightly under-qualified.

4. **Hapax *Ḥrd* (n = 1) is folded into the cross-translation drift table
   without sufficient annotation** — §4.11 (line 330) and
   `outputs/nlp_upgrade/translation_drift_per_root.csv` (row 2) — The
   paper does annotate the *ḥard* drift value of 0.40 as an outlier
   "carrying no inferential weight", but Figure 9 plots it on the same
   axis as the n ≥ 10 roots, and the standard deviation column for *ḥard*
   in the CSV is blank (only one verse, so no within-root variance is
   defined). For figure caption faithfulness, the bar should either be
   suppressed, faded, or labelled "n = 1" in-figure; otherwise a casual
   reader interprets the 0.40 bar as the spectrum's most translation-
   volatile root, which the text correctly does not claim. The same point
   applies, less acutely, to *ʾff* (n = 3) and *asaf* (n = 5).

   **Proposed fix**: Either drop the *ḥard* bar from Figure 9 or annotate
   it inline; add a "min-n threshold for inferential interpretation" line
   to the caption.

5. **Per-aya PMI uses N_AYAS = 6236 as the denominator, which is the
   Quran-wide total, but the joint events being counted are restricted
   to ayat that contain *at least one* spectrum root** — `nlp_upgrade_colab.py`
   lines 380–404 — This is a defensible *prior-over-corpus* choice
   (estimating the marginal as P(root ∈ random ayat)), but it has the
   effect of producing very small p1 / p2 / p12 estimates that depend on
   a corpus-wide normaliser even though the network is constructed only
   over spectrum-bearing ayat. The published Figure 10 caption (line 350)
   describes the top edges (asaf–ghaḍab npmi = 0.59, ḍyq–ḥuzn = 0.47,
   krh–sakhaṭ = 0.43) without telling the reader the denominator. With
   the alternative denominator N = (# of ayat containing at least one
   spectrum root) the npmi rankings stay the same (PMI is monotonic in
   the choice of common reference frame) but the absolute values shift;
   if a reader re-runs the analysis on a per-spectrum subset they will
   see different numbers and be unable to reconcile. The interpretation
   text at line 352 ("co-occur more than chance given their individual
   frequencies") is technically accurate but the reference probability
   ("chance" against what corpus?) needs one sentence of disclosure.

   **Proposed fix**: Add a footnote to §4.13 stating the PMI denominator
   choice explicitly and confirming that the npmi *ordering* is invariant
   under denominator choice, while absolute values are not.

## Minor issues

- **§3.4 / `advanced_metrics.py` line 159–166**: The Wilson–Hilferty
  fallback for df > 10 in `_chi2_critical_005` is hard-coded with
  z₀.₉₅ = 1.6449 (one-tailed), not the two-tailed z₀.₉₇₅ = 1.96 that the
  body of the function implies (it is computing an alpha = 0.05 *upper*
  critical value of a χ² distribution, which is the right thing). No bug,
  but the variable name and the comment ("z_{0.95}") are confusing —
  consider renaming.
- **`_binomial_pvalue()` (lines 102–115)**: the tolerance `1e-12` for
  including PMF tail mass is fine in floating-point but the documentation
  should note that this implements the "doubled minimum-tail" definition
  rather than the "method of small p-values" of Fisher (1922). Both are
  defensible; reviewers from a statistics audience will want to know which.
- **Bootstrap CIs in `network_centrality.csv`**: For *ʾff*, *mqt*, *ḥrd*,
  *ʿtw* (rows 2, 9, 11, 15) every centrality measure is identically 0.00
  with CI [0.00, 0.00], reflecting that these isolates have no spectrum-
  graph edges. This is technically correct but it is awkward to interpret
  these as "centrality = 0 with zero uncertainty" — the bootstrap simply
  cannot observe an edge that doesn't exist in the source data. Worth a
  one-line caveat in §4.8.2 that nodes with zero in-graph degree are
  trivially placed at the centrality floor.
- **NaN handling for eigenvector centrality** (lines 599–605): the
  `try/except (PowerIterationFailedConvergence, Exception)` correctly
  catches non-convergence, but the catch is overly broad (`Exception`)
  and would mask any other bug in NetworkX. Tighten the except to the
  specific exception class and disclose the fallback in §3.4 ("eigenvector
  centrality falls back to NaN under non-convergence; the actually-run
  graph converged but the safeguard is preserved in code").
- **§4.2 narrative**: the phrase "the chi-squared approximation requires
  expected counts ≥ 5 in every cell (which is met)" is correct (expected =
  312 / 6 ≈ 52 per cell), but the same paragraph then justifies the
  permutation null on grounds that include cell-sparsity ("sparse cells
  (Stage 5 *n* = 11)"). The two statements are about different things
  — *expected* counts vs *observed* counts — and a careful reader will
  notice. Rephrase to "while expected counts are uniform at 52 and well
  above Cochran's 5-per-cell rule, the *observed* marginal imbalance
  (S6 = 145 vs S5 = 11) is the asymmetric structure that the asymptotic
  χ² is most vulnerable to."
- **§4.8.2 closeness CI for *baghy***: reported as [0.23, 0.84] in the
  manuscript, [0.2327, 0.8401] in `network_centrality.csv`. Consistent
  rounding, no issue, but worth a one-decimal-place audit pass to be
  certain that every number in the paper matches its source CSV to two
  decimal places.
- **§4.8.4 *ʿutuww* p-value error duplicated in figure caption (line 184)**:
  the caption to fig3 lists *ʿutuww* "(9/1 Meccan)" but the body §4.8.4
  states the same and §4.5.2 family-Holm table reports raw 0.47 — once
  the §4.8.4 number is corrected this propagates automatically.
- **Comparative-translation §4.10 vs Translation-drift §4.11 cohesion**:
  the §4.10 illustrative table (Yusuf Ali, Pickthall, Arberry, Saheeh,
  Hilali-Khan) lists Hilali-Khan, but the §4.11 quantitative drift uses
  (Sahih, Pickthall, Yusuf Ali, Arberry, Maududi) — Maududi replaces
  Hilali-Khan. A one-sentence justification of the translator-set change
  (Maududi is more widely studied; Hilali-Khan has known sectarian
  framing) would help.
- **Family Holm-Bonferroni denominator**: §4.5.2 says "family of 14
  per-root binomials"; this is correct since `_holm_bonferroni()` is
  applied over `family_p_raw` indexed by `r.bw` for all 14 SPECTRUM
  roots (lines 433–439). But §6.1 echoes "every test we *could* have
  flagged is in the family, including the headline four" — there are
  four headline tilts (*sakhaṭ*, *asaf*, *ʿutuww*, *naqm*) but the
  family is 14, not 4. Word the §6.1 statement so a hostile reader cannot
  read it as a partial-family correction.
- **§3.2 transparency on root exclusion**: the list of excluded
  candidates (*q-h-r*, *ḥ-n-q*, *ʿ-n-f*, *ḍ-r-b*, *q-ṣ-w/q-s-y*,
  *gh-l-ẓ*, *ʾ-n-f*) is admirable. Worth one sentence on whether
  *ḥ-m-y* / *ġ-l-y* (heating / boiling) were considered — they are the
  pre-Islamic-Arabic CMT-relevant precursors of *ġayẓ* and are touched
  in §5.5 paragraph (6) on Jāhilī Arabic.
- **Reproducibility statement** (§ Data and Code Availability, lines
  482–494): the four reproduction commands (`pip install`,
  `extract_concordance.py`, `advanced_metrics.py`, `visualize_*.py`) do
  *not* include the four NLP analyses of §§4.11–4.14, which require
  `nlp_upgrade_colab.py` on a GPU. A one-paragraph note on how a reviewer
  can re-derive the NLP figures (Colab notebook with model snapshots,
  expected runtime, fallback if GPU unavailable) would strengthen the
  reproducibility claim. Right now the §4.11–4.14 outputs are pinned in
  `outputs/nlp_upgrade/` (CSV + PNG) but the manuscript's reproducibility
  paragraph doesn't tell a reader how to regenerate them.
- **Random seeds**: `RNG_SEED = 20260509` is fixed in `advanced_metrics.py`,
  and UMAP uses `random_state = 42`; KMeans uses `random_state = 42`;
  Nöldekean jitter uses `np.random.rand` *without* an explicit seed at
  `nlp_upgrade_colab.py` line 348. The jitter is cosmetic only (does not
  affect ρ / p) but the reproducibility-determinism claim should not have
  a single un-seeded RNG anywhere in the public pipeline.
- **Bibliography entry for Cochran (1954)**: footnote at line 170 says
  "Bibliography entry to be added on author follow-up". The bibliography
  *does* contain Cochran 1954 (line 568) — remove the placeholder note.
  Similarly "ELQV authors" and "Cogent Authors" placeholders (lines 570,
  578) should be resolved before submission.

## Editorial polish

- **Abstract**: the closing sentence ("Implications follow for Qurʾanic
  translation and Islamic psychology") is anodyne; consider naming the
  *conditional* nature of those implications since the body is so careful
  about them.
- **Section numbering**: §4.6.2 is missing (jumps from 4.6.1 to 4.6.3
  at line 250). Either re-number or fold the *ḥard* discussion into
  a single 4.6.2.
- **Table 4 (Cross-field co-occurrence)**: the parenthetical
  "(krh-tie excluded since *krh* is now in the spectrum)" inside the
  sxṭ-row "Total" column is informative but cell-formatting awkward.
  Move to a footnote.
- **§4.13 reproduction of the npmi top edges in prose**: the figure
  caption says "*asaf*–*ghaḍab* (npmi = 0.59)" and the body §4.13 says
  "(npmi = 0.59)" — consistent. Good. But the npmi range claim in the
  caption "(npmi ∈ [−1, 1])" should note that the displayed network is
  positively-thresholded so negative-npmi edges are not visible.
- **Footnote-citation density** in §1 and §2: every sub-paragraph carries
  three to five footnotes which is unusually dense for a JQS article;
  consider consolidating to one omnibus footnote at the end of each
  sub-paragraph for ease of reading.
- **Section 4.8.5 *baghy* sub-counts** (line 286): "*baghy* 22A/50S/24A+S"
  sums to 96, matching *baghy*'s total — good. *ṭughyān* 11A/19S/9A+S
  sums to 39, also matches. *ʿutuww* 5A/2S/3A+S = 10, matches. The
  paper does not show the totals work out, which would help the reader
  trust the coding pass.

## Verdict

This is a careful, methodologically self-aware computational paper that
will hold up under serious scrutiny once the load-bearing arithmetic
errors flagged in **Major issue 1** are corrected. The honest framing
of failed-trend and CAMeLBERT-null results, the κ = 0.79 second-coder
audit, the corpus-derived Meccan baseline with full sensitivity table,
the bootstrap CIs on every centrality measure, and the explicit
acknowledgement that the asymptotic χ²(5) over-states the evidence are
all features one wishes were standard in this sub-field. The
manuscript should be returned for **minor revision** with three
concrete asks: (i) re-run the pipeline and reconcile every per-root
p-value in the manuscript body against `statistical_tests.csv`, with
particular attention to *ʿutuww* (§4.8.4) and *karh* (§4.3.1), since
*karh* most likely also survives FDR and that materially upgrades the
empirical-findings paragraph; (ii) add the root-vs-stage silhouette
control to §4.12 so the welcomed-null reading is empirically grounded;
(iii) one sentence on Nöldeke chronology limitations in §4.14 plus a
Fisher's-z CI on ρ. Subject to these revisions the paper should publish
in JQS as a substantive contribution on the conservative-claims end of
the computational-humanities spectrum — exactly the register the journal
should be encouraging.
