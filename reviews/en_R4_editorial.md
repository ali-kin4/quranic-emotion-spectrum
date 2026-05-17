# Reviewer 4 (Editorial / JQS-fit) — JQS
**Recommendation**: Major revision
**Confidence**: 5

## Word count audit

The cover letter claims **13,032 words; abstract 208 words**. Direct `wc -w` on the manuscript markdown returns a quite different picture, and the cover-letter figure does not survive scrutiny.

| Section (H2)                                  | Words   |
|-----------------------------------------------|---------|
| Title block + header                          | 10      |
| Sub-title line                                | 52      |
| Abstract                                      | **243** |
| §1 Introduction                               | 1,898   |
| §2 Theoretical Framework                      | 936     |
| §3 Methods                                    | 1,404   |
| §4 Findings                                   | **7,142** |
| §5 Discussion                                 | 3,172   |
| §6 Conclusion                                 | 1,703   |
| Acknowledgements                              | 78      |
| Funding / Competing / Ethics / Authors / ORCID | 183     |
| Data & Code Availability                      | 126     |
| Bibliography                                  | 2,116   |
| **Total (`wc -w` on `manuscript.md`)**        | **≈19,063** |

Removing the bibliography (2,116) and removing markdown overhead (table rows, figure-caption metadata, ORCID placeholders, code block) brings the *prose+footnote* body to roughly **15,500–16,500 words**. Even on the most generous accounting that strips footnotes (30 of them, several running 80–120 words) and figure captions (some of which are themselves 150–200-word paragraphs masquerading as captions, e.g. Figure 8 methodology caption at ~190 words), the prose body sits comfortably above **13,000 words**. The cover-letter claim of 13,032 is **understated** unless it is excluding both footnotes *and* figure captions *and* tables — which is not what JQS counts.

**JQS research articles run 6,000–10,000 words including footnotes (excluding bibliography).** The manuscript is, on a sympathetic count, **5,500–7,000 words over the upper bound**, i.e. roughly **150–170% of the ceiling**. This is the single largest barrier to submission readiness and cannot be addressed by editorial polish; it requires structural cutting.

**The abstract is 243 words** (cover letter claims 208). The JQS abstract guideline is 150–250, so 243 is technically inside the band but at the upper edge; trim to 180–200.

### Most prunable sections (in priority order)

1. **§4 Findings (7,142 → target ~3,500)**. This single section is larger than most full JQS articles. Cuts:
   - **§4.10, §4.11, §4.12, §4.13, §4.14** are five sequential "computational extensions" that together run ~1,800 words and several figures. §4.11 (translation drift), §4.12 (CAMeLBERT null), §4.13 (PMI network), §4.14 (diachronic null) read as a Phase-II appendix bolted onto a Phase-I paper. **Recommendation**: relegate §4.11–4.14 to a single ~250-word "Computational robustness summary" sub-section that points reviewers to the supplementary material / repository, and move the four full discussions to an online supplement. Saves ~1,500 words.
   - **§4.2 / §4.2.1** repeat the permutation-null caveat at the omnibus level, then again at the monotonic-trend level, then again in §6.2 RQ3, then once more in the abstract. Pick one venue (probably §4.2.1) and ruthlessly cross-reference. Saves ~400 words.
   - **§4.8.2 Table 4** caveat paragraph and the prose immediately above and below it duplicate the bootstrap-uncertainty argument made in the §4.8.2 first paragraph. Compress to one paragraph. Saves ~200 words.
   - **§3.6** "On the choice of permutation over asymptotic χ²" is a 280-word methodological mini-essay sitting inside the validity-check subsection. Either move into a footnote or merge into §3.4. Saves ~200 words.

2. **§5 Discussion (3,172 → target ~1,800)**. §5.5 is 1,400+ words of comparative philology (Akkadian, Biblical Hebrew, Homeric Greek, Sanskrit, Chinese, Jāhilī Arabic) that, while genuinely impressive, dwarfs the *Qur'anic* analysis it is meant to contextualise. JQS audience already grants Q. 67:8 as remarkable; a 300-word survey citing Kruger, Cairns and Kövecses-Benczes-Szelid would suffice. Saves ~1,000 words.

3. **§6 Conclusion (1,703 → target ~700)**. The "Answers to the research questions" subsection (§6.2) restates §4 and §5 findings in compressed form, which is precisely what a JQS conclusion should *avoid*. Either drop RQ-by-RQ structure or radically compress to one paragraph per RQ. Saves ~700 words.

4. **§1 Introduction (1,898 → target ~1,200)**. §1.2 ("Originality") and §1.3 ("Prior work and the gap") cover overlapping territory; the (i)/(ii)/(iii)/(iv)/(v) "Originality disaggregated" list in §1.2 reappears almost verbatim in §6.1. Pick one. Saves ~500 words.

**Total achievable savings on a careful pass: ~4,500 words.** Combined with redundancy trimming throughout, the manuscript can be brought to ~10,500–11,500 words. To hit the 10,000-word ceiling cleanly the four queued NLP extensions (§4.11–4.14) must go to supplementary material.

## Summary of the manuscript

The paper argues that fourteen Arabic roots in the Qur'an (*ʾff, krh, ḍyq, ḥzn, ʾsf, nqm, sxṭ, mqt, ġḍb, ḥrd, ġyẓ, bġy, ṭġy, ʿtw*) constitute a graded six-stage semantic field organised by action-intensity, integrating Izutsu's semantic-field method, Kennedy–Sassoon scalar semantics, and Lakoff–Kövecses conceptual-metaphor theory. The empirical apparatus is a reproducible Python pipeline over the Quranic Arabic Corpus producing 312 attestations, distributional statistics with uncertainty-aware reporting (10,000-perm marginal-preserving χ² null, Cochran-Armitage trend, Holm-Bonferroni-adjusted binomials, bootstrap 95% CIs on centralities), a κ = 0.79-validated tafsir-coding audit of all 145 Stage-6 attestations, and four exploratory NLP analyses (multilingual MPNet translation drift, CAMeLBERT-CA clustering, PMI co-occurrence, Nöldekean chronology). Headline findings: (i) the χ²(5) omnibus is *consistent with* — not confirmatory of — non-uniformity (asymptotic *p* < 0.001, permutation *p* = 0.24); (ii) *sakhaṭ* attests exclusively in Medinan suras (Holm-adj. *p* = 0.05, sole survivor); (iii) Stage 6 has bidirectional rather than purely downstream causation (A = 26%, S = 49%, A+S = 25%); (iv) Q. 67:8 (*tamayyazu min al-ġayẓ*) instantiates the "container collapse" failure mode of CMT with unusual transparency, with Job 32:19 (*bāqaʿ*) as the one clear Northwest-Semitic precedent.

The methodological ambition is high, the philological apparatus is serious, and the reproducibility infrastructure (SHA-256 pinning, MIT/CC-BY, full audit at `data/concordance/validation_audit.md`) sets a benchmark for JQS-adjacent computational work. The thesis is intellectually persuasive and the integration of Izutsu + Kennedy-Sassoon + CMT under a corpus pipeline is genuinely novel. The submission is **not yet ready for JQS** because of (a) length, (b) citation style, and (c) a cluster of structural/format issues itemised below.

## Major issues

1. **Length** — §4 (7,142 w) and overall (~19,000 w incl. bibliography; ~15,500–16,500 w prose+notes excl. biblio). **Problem**: 1.5–1.7× the JQS upper bound, regardless of how generously one counts. **Proposed fix**: cut §4.11–4.14 to a supplement; cut §5.5 cross-cultural survey by ~70%; cut §6.2 RQ recap by ~60%; deduplicate §1.2 vs §1.3 vs §6.1 "originality"/"contributions" enumerations. See word-count audit above for surgical targets.

2. **Citation style is Chicago-style discursive footnotes, not Harvard author–date** — manuscript-wide. **Problem**: JQS house style is Harvard author–date in-text "(Smith 1995: 23)" with a unified Bibliography. The present manuscript uses pandoc-style discursive footnotes (`^[Author, *Title*.]`) for 30 references, several of them genuinely discursive (footnote at L113 is a ~70-word methods argument; footnote at L466 is itself a citation rationale). This is not a cosmetic substitution: it changes how the prose reads, since several arguments currently *live inside* footnotes (Cochran caveat at L170 fn; CAD citation at L392 fn). **Proposed fix**: convert all citation footnotes to Harvard "(Author Year: pp.)" in-text; move discursive content into the main text (or cut it); keep a single Bibliography (already alphabetised, good). The current English-language Bibliography is in author-surname order but the **Persian and Classical Arabic sections are separately alphabetised by sub-list** — JQS would expect a single alphabetised list with transliterated Arabic surnames sorted within the unified sequence (al- prefix ignored), which the manuscript states it intends but does not implement.

3. **Table numbering is broken** — **Table 3 does not exist** but the sequence runs 1, 2, 4, 5, 6, 7. Table 7 is referenced in §4.13 prose (L348) but no Table 7 heading or content appears anywhere in the manuscript. **Table 6 is used twice** — first for the translation comparison at L315 ("Table 6. Translation of four canonical verses…") and then again in §4.12 (L340: "Cluster-vs-stage cross-tabulation (Table 6) shows no diagonal concentration"). **Proposed fix**: renumber sequentially 1–6; supply a Table 7 if §4.13 PMI top-edges is intended to be tabular, or remove the reference; disambiguate the L340 Table 6 reference (it is a different table from the translation table at L315).

4. **Figure numbering is also broken** — Figures referenced in text: 2, 3, 4, 5, 6, 7, 9, 10, 11. **Figure 1 is never referenced in prose** (it sits at the top of §2 as the schematic continuum graphic but no text says "Figure 1"). **Figure 8 (methodology) is shown at L95 in §3.3 with a 190-word caption but no "Figure 8" in-text reference**. Image files reference fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8, fig9, fig10, fig11 (eleven figures). JQS asks all figures be sequentially numbered and all referenced in text. **Proposed fix**: insert in-text references for Figs 1 and 8; alternatively, if Fig 8 is purely methodological/illustrative, demote to "Figure A1" in supplement.

5. **Cover letter inconsistencies and placeholders** — (a) "Department of [Department]" at line 5 is a literal placeholder. (b) ORCID lines in manuscript read "0000-0000-0000-0000 (to be provided at submission)" four times; cover letter says "ORCIDs will be supplied at submission" — this should be resolved *before* submission, not deferred. (c) Stated word count "13,032 words; abstract 208 words" is inconsistent with the file; either the cover letter is computed on a substantially earlier draft or it excludes footnotes and captions in a way JQS will not. (d) Title rendering varies: manuscript title uses curly apostrophe "Qur'an", cover letter uses straight apostrophe "Qur'an", journal name italicised inconsistently (Persian-paper Persian title appears in the cover letter — fine, but the romanised journal name *پژوهش‌های زبان‌شناختی قرآن* is given without Latin gloss). **Proposed fix**: resolve all placeholders, recompute word count under JQS rules, unify the apostrophe character (Qur'an), provide Latinised journal name "Pizhūhish-hā-yi Zabānshinākhtī-yi Qurʾān" alongside the Persian.

6. **Discursive-footnote abuse / footnote-to-text inversion** — Several places (L113, L170, L466) the footnote contains a substantive methodological or interpretive argument that does not belong in a footnote. Worst case: the footnote at L113 spans 280+ words and includes its own citations to Cochran (1954), Fisher (1922), Patefield (1981), Mehta-Patel (1983), and Agresti (2013). This is a footnote-as-mini-essay. JQS discourages this. **Proposed fix**: convert these to main-text discussion (they support the methodological case for permutation inference and should be visible) or, if cutting for length, retain only the citations.

7. **Two reference entries are duplicated and inconsistently attributed** — "Almuhanna et al." (L554) is flagged as a "placeholder version" of Gaanoun and Alsuhaibani (2025) which is then entered separately at L584. Either keep one or the other but not both. Similarly, three reference entries are flagged "[Author attribution unresolved in source bibliography; to be updated on author follow-up.]" (Cogent Authors L570, ELQV Authors L578, IJCP Authors L592). **All three must be resolved before submission** — JQS will not accept "unresolved" attribution in the bibliography.

8. **Abstract structure is slightly off-spec** — opens strongly ("The Qur'an deploys an exceptionally articulated lexicon…"), but the long footnote inside the abstract (`^[Kais Dukes…]`) violates the "no citations" abstract convention and on most journal platforms will break the abstract field rendering. **Proposed fix**: remove the footnote; cite Dukes 2011 in §3.1 instead.

9. **The Persian-paper COPE/ICMJE disclosure is well-handled in the cover letter** but the manuscript itself contains no such disclosure. JQS editors increasingly expect a brief acknowledgement in the manuscript (typically in the Funding / Competing-interests block or in an Author-note footnote on page 1) of any parallel-language submission. **Proposed fix**: insert a 2-sentence Author-note or Funding-section addendum stating that an independent Persian-language paper using the same corpus dataset is concurrently under consideration at *Pizhūhish-hā-yi Zabānshinākhtī-yi Qurʾān*, the two papers do not share content or cite each other, and the empirical pipeline is the only shared element.

## Minor issues

- **Title** (L1–2) is strong, indexable, and scholarly, but at ~25 words is on the long side. The double subtitle ("A Semantic-Network Analysis of Displeasure, Inflammation, and Destructiveness Along an Action-Intensity Continuum") reads as two competing subtitles welded together. Consider tightening to: "The Phenomenology of the Anger Spectrum in the Qur'an: A Six-Stage Semantic-Network Analysis" (16 words).

- **Keywords** (L19) — ten keywords listed; JQS conventionally takes 5–7. Trim "Izutsu" (already in body), "Arabic corpus linguistics" (subsumed by "corpus linguistics"), and "Islamic psychology" (peripheral to JQS scope, may better serve the §5.7 implications discussion than as a top-level keyword). Suggested 7: Qur'an; anger spectrum; semantic field; cognitive linguistics; scalar semantics; conceptual metaphor; corpus linguistics.

- **Section numbering** is consistent (1–6) but subsection depth is uneven: §4.2.1 then §4.3.0 (zero-indexed!) at L194 — anomalous. §4.6.1 exists but §4.6.2 does not (the next subsection is §4.6.3). **Proposed fix**: renumber §4.3.0 as §4.3.1 (and successive); supply §4.6.2 or renumber §4.6.3 → §4.6.2.

- **Hypothesis numbering** in §1.4 (H1–H5) is referenced in §4 only sporadically (H4 at L262, H5 at L256); H1, H2, H3 are not explicitly closed in §6.2 either. **Proposed fix**: either close every hypothesis explicitly in §6.2 ("H1 supported / H2 fails-to-reject and consistent with bidirectional reading / H3 borderline-significant after Holm / H4 consistent with point estimates / H5 corroborated") or drop the H1–H5 framing in favour of the five Research Questions which *are* closed in §6.2.

- **Prose register** is generally appropriate scholarly tone, but a few phrases skew breezy: "The distance walked, absent intervention, by an unmanaged life of irritation" (L29) — evocative but homiletic; "the wretched of fingernail-detritus etymologically" (Table 1 row 1) — opaque; "anger that strips the world of what it is owed" (L250) — sermonic. **Proposed fix**: light copy-edit pass to bring register to consistent academic-philological.

- **In-text section cross-references** (§4.8.5, §5.5, etc.) are well-deployed but inconsistent in formatting — sometimes "§4.8.5", sometimes "§§4–5", sometimes "see §3.5". Unify on "§X.Y" and "§§X.Y–Z.W".

- **Footnotes 30 in total**, several discursive (see Major #6). For a ~13,000-word target manuscript at JQS, 30 footnotes is heavy but not abusive *if* most are pure citation. After conversion to Harvard, only the truly discursive ones (perhaps 5–8) should remain as footnotes.

- **Bibliography (L498–681)** is alphabetised within sub-lists, but the manuscript opens the bibliography with a note saying "the Arabic article *al-* is ignored for alphabetisation" — which is the right rule, but it is then inconsistently applied: al-Fīrūzābādī appears under "F" position (correct), but al-Mostafawī sits under "M" position correctly while al-Qurṭubī, al-Qushayrī, al-Rāghib, al-Rāzī, al-Ṭabarī, al-Ṭabarsī, al-Ṭabāṭabāʾī, and al-Zamakhsharī all appear in their al- order — i.e. the rule is *stated* but the implementation **alphabetises by the post-al- letter**, which is also defensible but should be made explicit. The contradiction is between the *stated rule* "the article al- is ignored" and the *actual ordering* which appears to ignore al- as intended. Verify a clean pass.

- **Bibliography mis-alphabetisation**: Agresti (L566) is out of order — sits between Cogent Authors (L570) above and Cochran (L568) below; Agresti should precede Akra (L550). Similarly, the placeholder Almuhanna entry at L554 sits between Albayrak and Averill — fine alphabetically, but the entry's own note ("placeholder version; see Gaanoun and Alsuhaibani 2025 for canonical attribution") makes clear it is a doublet. Delete.

- **Surah-name convention**: the user-memory instruction is that surah names should appear as "sūrat X" not as bare common nouns. The manuscript uses "Q. 67:8", "Q. 3:134" etc. — fine. But §4.5.2 references "Q. 47:28" without naming the surah, and §5.5 refers to "the formative Medinan community" without surah anchoring. JQS readers typically expect at least the first attestation of a key verse to carry a parenthetical surah name (e.g. "Q. 67:8 (sūrat al-Mulk)"). Light pass to add these.

- **Spectrum-stage figures (44/60/27/25/11/145)** are reported in the abstract, in §4.2, in §4.2.1, in Figure 2 caption, in §5.3, and in §6.2 (RQ3). At least four of these recur with slightly different framings of the same numbers. Compress.

- **The four "Phase II" NLP analyses (§4.11–4.14)** include AraBERT/CAMeLBERT clustering twice — once as §4.12 (the executed CAMeLBERT analysis with the clear null) and once in §6.3 as a *future* analysis (§6.3 item (a) "AraBERT / CAMeLBERT contextual-embedding validation"). One of these is wrong: either the analysis is in §4.12 and should not be re-promised in §6.3, or §6.3 is correct and §4.12 should not pre-empt it. **Proposed fix**: remove the §6.3(a) reference to CAMeLBERT (already done in §4.12) and rephrase as "next-step deep-tafsir cross-validation".

- **The illustrative translation table (Table 6 at L315)** uses dated translations (Yusuf Ali 1934, Pickthall 1930, Arberry 1955, Hilali-Khan 1996, Saheeh Intl. 1997) and excludes contemporary scholarly translations (Abdel Haleem 2004 — *the JQS editor's own translation* — Droge 2013, Khalidi 2008). For a paper submitted to the journal Abdel Haleem edits, this is awkward. **Proposed fix**: add Abdel Haleem at minimum.

## Editorial polish (formatting, citation style, prose)

- Curly vs straight apostrophe: manuscript uses U+2019 "Qur'an" throughout (correct); cover letter mixes U+2019 and U+0027. Unify on U+2019.
- Em-dash usage is heavy and idiosyncratic — many sentences run three em-dash clauses. Light copy-edit pass to convert ~30% of em-dashes to semicolons or full stops would improve readability without losing meaning.
- Arabic transliteration: manuscript uses the IJMES system inconsistently — *ghaḍab* with sub-dotted ḍ, but *sakhat* appears in the cover letter without the sub-dotted ṭ. JQS uses IJMES; unify.
- Italicisation: journal names in the bibliography are italicised (correct); Arabic technical terms (*tafsīr*, *taḍajjur*, *kaẓm al-ghayẓ*) are italicised in main text (correct); some Arabic terms (*sakhaṭ*, *mufradāt*) drift between italic and roman. Light pass.
- The §3.6 "Validity check" embedded long footnote (L113) on the permutation-vs-asymptotic χ² question (~280 words including five citations) is technically a structural problem — it is *the* methodological justification for the headline-statistic recasting in §4.2, but it lives in a footnote. JQS would expect this in the main text of §3.4 (Quantitative analyses) at a minimum.
- Footnote at L17 inside the abstract: remove (see Major #8).
- Acknowledgements (L454) thank "the anonymous peer reviewer" — fine for a previous round, but for first submission this should be removed and reinstated in revision if appropriate.

## Verdict

The manuscript represents serious philological-computational scholarship, a genuinely novel methodological synthesis (Izutsu + Kennedy-Sassoon + CMT under a reproducible pipeline), and a well-grounded substantive thesis with appropriate uncertainty-aware reporting. It is in many respects exactly the kind of paper JQS should welcome.

It is **not yet submittable to JQS** because the length is ~150–170% of the ceiling, the citation style is Chicago-footnote rather than JQS-Harvard, the table/figure numbering is inconsistent (missing Table 3, duplicate Table 6, never-referenced Figures 1 and 8, never-supplied Table 7), three bibliography entries carry unresolved attribution, cover-letter placeholders remain unfilled (`[Department]`, ORCID `0000-0000-0000-0000`), the abstract carries a footnote citation in violation of convention, the cover-letter stated word count is inconsistent with the file, and the §1.2 / §1.3 / §6.1 originality blocks are triply redundant.

These are all surface-level structural issues — none of them threatens the substantive contribution — but together they amount to a **major revision** in the editorial-fit sense. The author should:

1. Cut to 9,500–10,000 words (target 9,500 for safety margin).
2. Convert all footnotes to Harvard author-date in-text citations, retaining a handful of genuinely discursive footnotes.
3. Fix table/figure numbering (sequential 1–6 and 1–11 with all referenced).
4. Resolve all `[VERIFY:]`-equivalent placeholders (the manuscript has no literal `[VERIFY:]` markers but does have three "Author attribution unresolved" bibliography entries, two ORCID placeholders, one Department placeholder, and one Table 7 phantom-reference — these are the practical equivalents).
5. Add Abdel Haleem (2004) to the translation comparison.
6. Add an Author-note disclosing the parallel Persian-language submission in the manuscript itself, not only in the cover letter.

After these revisions the paper is, in this reviewer's judgement, a strong JQS candidate. Without them, even a sympathetic handling editor would have to return it.

**Recommendation: Major revision before external review.**
