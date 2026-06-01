---
title: "The Phenomenology of the Anger Spectrum in the Qur'an: A Semantic-Network Analysis of Displeasure, Inflammation, and Destructiveness Along an Action-Intensity Continuum"
journal: "Religions"
type: "Article"
---

<!--
  Formatted to MDPI *Religions* author instructions (IMRaD + back matter,
  Chicago author-date, ≤200-word single-paragraph abstract, 3–10 keywords).
  Source of record: paper/english/manuscript.md. Scholarly content unchanged;
  only structure, section mapping, abstract length, and reference style reformatted.
  Double-blind note: author names and affiliations below are to be removed
  from the review copy and supplied only in the title-page / cover material.
-->

# The Phenomenology of the Anger Spectrum in the Qur'an: A Semantic-Network Analysis of Displeasure, Inflammation, and Destructiveness Along an Action-Intensity Continuum

**Karim Jabbary** ^1,\*^ and **Ali Jabbary** ^2^

^1^ Department of Arabic Language and Literature, Faculty of Literature and Humanities, Urmia University, Urmia, Iran; k.jabbary@urmia.ac.ir

^2^ Faculty of Computer Engineering, Urmia University, Urmia, Iran; a.jabbary@urmia.ac.ir

\* Correspondence: k.jabbary@urmia.ac.ir

---

## Abstract

Existing scholarship treats the Qur'an's lexicon of anger word-by-word or through normative-ethical frames. This study argues that fourteen core Arabic roots (*ʾff, krh, ḍyq, ḥzn, ʾsf, nqm, sxṭ, mqt, ghḍb, ḥrd, ghyẓ, bghy, ṭghy, ʿtw*) form a graded semantic field ordered by intensity of action across six phenomenological stages: pre-anger displeasure, inner pressure, evaluative aversion, active anger, compressed rage, and behavioural outcomes. The framework integrates Izutsu's semantic-field method, Kennedy–Sassoon scalar semantics, and Lakoff–Kövecses conceptual metaphor theory, distinguishing primary (ANGER IS HEAT) from complex (PRESSURIZED-CONTAINER ANGER) metaphors. A reproducible pipeline over the Quranic Arabic Corpus yields 312 attestations. Under uncertainty-aware metrics, a marginal-preserving permutation null gives *p* = 0.24; three roots survive Holm-Bonferroni correction (*karh*, *baghy*, *ghayẓ*), with *sakhaṭ* borderline (adj. *p* = 0.05). Network analysis identifies *baghy* as the bridge node to the moral-evaluation field; Q. 67:8 of sūrat al-Mulk (*takādu tamayyazu min al-ghayẓ*) exemplifies a vessel-internal-failure construal; a κ = 0.79-validated *tafsīr* audit supports a bidirectional-causation reading of Stage 6 (anger-derived 26%, structural 49%, both 25%). Conditional implications follow for Qur'anic translation and Islamic psychology; small per-root *n* and the closed corpus bound the inferences.

**Keywords:** Qur'an; anger spectrum; semantic field; cognitive linguistics; scalar semantics; conceptual metaphor; corpus linguistics

---

## 1. Introduction

### 1.1. Statement of the Problem

The Qur'anic lexicon for the anger spectrum exhibits a precision that survives only with difficulty into translation: where English versions level *uff*, *karh*, *ḍīq*, *ḥuzn*, *asaf*, *naqm*, *sakhaṭ*, *maqt*, *ghaḍab*, *ḥard*, *ghayẓ*, *baghy*, *ṭughyān*, and *ʿutuww* into a small set of broad equivalents — "displeasure," "distress," "grief," "anger," "rage," "transgression," "rebellion" — the Arabic original distinguishes them with the precision of a graded taxonomy. We argue that these fourteen roots are not synonyms but coordinated nodes in a single graded semantic field organised along intensity of action, traversing pre-anger displeasure, inner pressure and contraction, evaluative aversion, active anger, compressed/explosive rage, and behavioural outcomes (*baghy*, *ṭughyān*, *ʿutuww*) whose causation is bidirectional rather than purely emotional. The distance from *uff* (sūrat al-Isrāʾ, Q. 17:23) to *ʿutuww* (sūrat al-Furqān, Q. 25:21) is graded, not categorical.

### 1.2. Aims and Originality

This paper combines Izutsu's semantic-field approach, Kennedy–Sassoon scalar semantics, and Lakoff–Kövecses CMT to produce stronger philological claims than any framework in isolation. Izutsu's method yields a network without an internal ordering; Lakoff–Kövecses supply an English-anchored cognitive schema, and the two-volume *Metaphors of ANGER across Languages* (Kövecses, Benczes, and Szelid 2025) omits Classical Arabic; Kennedy–Sassoon orders predicates along a dimension but has not been applied to a Qur'anic emotion field. Qāʾimīniyā (2011, 2014) and Pakatchi and Afrashi (2020) already integrate Izutsu with CMT in Persian; the novel element here is the scalar layer operationalised as a six-stage continuum and tested against a 312-attestation reproducible pipeline, alongside (i) a κ = 0.79-validated *tafsīr*-coding audit of the bidirectional-causation reading of Stage 6, (ii) the *kaẓm*-as-tying-off-of-waterskin analysis of agent-internal containment, and (iii) the framing of Q. 67:8 of sūrat al-Mulk as an early and unusually transparent exemplification of vessel-internal failure, calibrated against the six-tradition survey of Section 4.5 acknowledging Job 32:19 (*bāqaʿ*) as a structurally cognate Northwest-Semitic precedent. The interpretive payoff: the continuum constitutes a coherent logic of escalation with structural affinities to modern emotion psychology, exceeding the contemporary models at Stage 6, where *baghy*/*ṭughyān*/*ʿutuww* extend the regulatory horizon of Gross's process model into the moral-anthropological register.

### 1.3. Prior Work and the Gap

Prior scholarship clusters into five lines. *Single-word lexical studies* (Narimani, Iqbali, and Chari 2021 on *ghayẓ/ghaḍab/sakhaṭ*; Qarizadeh et al. 2024 on *ṭughyān*) supply high-quality per-lexeme analysis but no integrated continuum. *Semantic-field and cognitive-semantic studies* in the Izutsu tradition (Qāʾimīniyā 2011, 2014; Pakatchi and Afrashi 2020; Albayrak 2020) leave the graded-continuum layer untreated. *Ethics-of-anger* work in the *kaẓm al-ghayẓ* tradition is normatively rich and linguistically thin. *Cross-linguistic CMT* literature, updated by Kövecses, Benczes, and Szelid (2025) across twenty-two languages, omits Classical Arabic; the closest Arabic-CMT precedents (Maalej 2004, 2007; Rabab'ah and Al-Saidat 2022) treat contemporary dialects. *Historical-critical and corpus-linguistic* work supplies complementary apparatus (Sinai 2017, 2023; Neuwirth 2019; El-Awa 2006; Sharaf and Atwell 2012a, 2012b; Akra, Hammouda, and Jarrar 2025; Sawalha et al. 2024); translation-criticism is now quantitative at scale (Gaanoun and Alsuhaibani 2025; Khan et al. 2025) but lacks a graded lexeme-level reference model. The present study occupies the unfilled intersection: it adds the Kennedy–Sassoon scalar layer to the Izutsu/CMT stack, applies it to the anger field the 2025 *Metaphors of ANGER* encyclopedia leaves un-canvassed, and releases the pipeline under Sharaf–Atwell / QuranMorph reproducibility standards.

### 1.4. Research Questions and Hypotheses

We address five research questions: (RQ1) the internal structure of the anger-spectrum field and its principal nodes; (RQ2) the action-intensity ordering and its theoretical legitimation; (RQ3) corpus-distributional corroboration (frequency, Meccan/Medinan, morphology, network); (RQ4) structural homology with Gross, Plutchik, Spielberger, and Lazarus–Scherer appraisal theory; (RQ5) implications for Qur'anic translation and Islamic psychology.

The principal *Qur'anic Action-Intensity Continuum Hypothesis* holds that the fourteen roots operate as graded steps on a single semantic continuum structured by intensity of action, organised in six phenomenological stages. Five subsidiary hypotheses follow: (H1) non-uniform six-stage frequency distribution; (H2) near-equal split between phenomenological core (S1–5) and behavioural pole (S6), consistent with the bidirectional Stage-6 reading; (H3) discursively-specialised exclusive-Medinan distribution of *sakhaṭ*; (H4) *baghy* as bridge node in the co-occurrence network; (H5) Q. 67:8 of sūrat al-Mulk as an unusually transparent exemplification of the vessel-internal failure construal.

---

## 2. Materials and Methods

### 2.1. Theoretical Framework

#### 2.1.1. Izutsu's Semantic-Field Method

Izutsu (1959, 1964, 2002) argued that the central Qur'anic terms are nodes in a network whose aggregate constitutes a Qur'anic *Weltanschauung*. His three-layer apparatus (*focus words*, *semantic fields*, *key words*) has been productive in Persian-language Qur'anic semantics (Qāʾimīniyā 2011, 2014; Pakatchi and Afrashi 2020). The fourteen target roots constitute the field around the focus words *ghaḍab* (central anger) and *baghy* (central behavioural-outcome). Izutsu's method is silent on the question that drives the present enterprise: granted that these lexemes co-belong to a field, what is the structural relation between them *within* it? For this we require scalar semantics.

#### 2.1.2. Scalar Semantics: From Network to Continuum

Gradable-predicate theory (Kennedy 1999, 2007; Sassoon 2010) supplies the missing apparatus. A scale has three components — a dimension of measurement, an ordering, and a unit of comparison. The Qur'anic anger field is such a scale: dimension = intensity of action (decomposable into locus, experiential intensity, scope of consequence); ordering = the six-stage progression; implicit unit = degree of externalisation from inner phenomenology to social rupture. Without this framework, the claim that *ghayẓ* is "more intense than" *ghaḍab* relies on tacit native-speaker intuition. Kennedy–Sassoon was developed for gradable adjectives; its extension here assumes a category-neutral underlying intensity scale recoverable from lexicographic and corpus-distributional evidence.

#### 2.1.3. Conceptual Metaphor Theory and the Container Schema

Conceptual metaphor theory (Lakoff and Johnson 1980; Lakoff and Kövecses 1987; Kövecses 2000, 2010) treats metaphor as a cognitive structure mapping concrete source domains (container, heat) to abstract targets (emotion). Lakoff and Kövecses (1987, 195–221) reconstruct American-English anger as a five-stage prototype scenario — (1) offending event, (2) anger, (3) attempt at control, (4) loss of control, (5) retribution — onto which ANGER IS THE HEAT OF A FLUID IN A PRESSURIZED CONTAINER, ANGER IS FIRE, and ANGER IS A WILD ANIMAL are mapped, with the container/pressure cluster operating especially in stages (2)–(4).

Following Grady (1997) and Kövecses (2020), *primary* metaphors are grounded directly in recurrent embodied experience (ANGER IS HEAT; EMOTIONAL CONTAINMENT IS PHYSICAL CONTAINMENT), while *complex* metaphors compose primary metaphors with culturally-elaborated folk physiology. PRESSURIZED-CONTAINER ANGER is a complex metaphor — the body construed as a sealed vessel, anger as a hot fluid inside it, loss of control as the fluid's exit or the vessel's failure. The Qur'anic *ghayẓ–kaẓm–tamayyuz* triad operationalises this complex construct, not the primary ANGER IS HEAT schema alone. Source-to-target mappings: HOT FLUID under pressure → INTENSE ANGER (*ghayẓ*); CONTAINER (sealed vessel) → BODY/SELF (chest, *qalb*, *nafs*); SEALING / TYING-OFF the vessel (*kaẓm* as waterskin closure; Ibn Manẓūr, *Lisān* 12:519, s.v. *k-ẓ-m*) → AGENT-INTERNAL SUPPRESSION; SEPARATION OF CONSTITUENTS within the vessel → VESSEL-INTERNAL FAILURE MODE (the *tamayyuz* construal, Section 3.7). The triad maps tightly onto stages (2)–(4) of the Lakoff–Kövecses scenario, with Q. 67:8 providing an unusually transparent linguistic crystallisation of stage (4).

Sharifian's (2011) Cultural Linguistics distinguishes what is universal in CMT from what is culturally elaborated. The primary metaphors are cross-linguistically robust and find support in the Qur'anic data, consistent with CMT's universalist claim. The *culturally elaborated* layer — the Qur'an's distribution of affect across *qalb*, *ṣadr*, and *nafs* as differentiated loci, the moral commendation of *kaẓm* in the *taqwā* register, and the *tamayyuz* construal of Q. 67:8 — is what the Qur'anic data illuminate beyond the universalist baseline (returned to in Section 4.4).

#### 2.1.4. The Integrated Framework

Izutsu identifies field boundaries; scalar semantics orders members along the action-intensity dimension; CMT grounds the pressurisation-collapse complex metaphor organising Stage 5. Figure 1 schematises the resulting six-stage continuum.

![**Figure 1.** The six-stage Qur'anic anger-spectrum continuum along the action-intensity axis; node area scales with QAC attestation frequency. S1 pre-anger displeasure (*ʾff–krh*); S2 inner pressure (*ḍyq–ḥzn–ʾsf*); S3 evaluative aversion (*nqm–sxṭ–mqt*); S4 active anger (*ghḍb–ḥrd*); S5 compressed/explosive rage (*ghyẓ*; *tamayyuz* manifestation); S6 behavioural outcomes (*bghy–ṭghy–ʿtw*) with bidirectional causation (Section 3.8).](fig1_continuum_v2.pdf){width=100%}

### 2.2. Corpus

The empirical analysis uses the **Quranic Arabic Corpus** (QAC) v0.4 (Dukes 2011): a morphologically tagged record for each of the 128,219 segmentable units, specifying location, surface form (Buckwalter), POS, and morphological features. Verse text in Uthmanic *rasm* and Meccan/Medinan sura classification are drawn from the Tanzil Project (2008).

### 2.3. Selection of Target Roots

The fourteen core roots were selected by three concurrent criteria: (i) *exegetical centrality* — focal reference in at least three of the four authoritative lexica (*Maqāyīs*, *Mufradāt*, *Lisān*, al-Mostafawi's *Taḥqīq*); (ii) *minimum corpus frequency* of one attestation, admitting hapax legomena (*ḥard*, Q. 68:25) when supported by three of the four lexica and consistent *tafsīr* treatment; (iii) *thematic membership* without significant overlap with adjacent fields. Excluded candidates (transparency): *q-h-r*, *ḥ-n-q* (not attested), *ʿ-n-f*, *ḍ-r-b*, *q-ṣ-w*/*q-s-y*, *gh-l-ẓ*, *ʾ-n-f*, *š-n-ʾ*. *Karh* is borderline — *karāha* affective, *ikrāh* structural — included on the *karāha* sense (Section 3.3). Five umbrella moral terms (*šnʾ, jrm, fsq, ẓlm, ʿdw*) are used for robustness (Section 3.9) and cross-field co-occurrence (Table 4); excluded from the principal continuum because of inflated cardinality (*ẓlm* n = 315 functions as a meta-category) or adjacency to normative-ethics fields.

### 2.4. Computational Pipeline

The Python (MIT-licensed) pipeline parses the QAC morphology file, filters on target roots, collapses multi-segment morphemes to surface words, joins sura-level Meccan/Medinan metadata, and emits master and per-root concordances, distributional summaries, and network/centrality CSVs; the complete analysis is reproducible from a fresh clone in four commands.[^audit] Figure 8 diagrams the end-to-end flow.

[^audit]: QAC v0.4 is pinned by SHA-256; outputs are released under MIT (code) and CC-BY 4.0 (manuscript/figures). The fourteen exemplar verses plus a stratified fifty-segment audit on the four most frequent core roots (*ḥzn*, *bghy*, *ghḍb*, *ṭghy*) returned 100% correct segment-to-root assignment against Tanzil; full audit at `data/concordance/validation_audit.md`.

![**Figure 8.** End-to-end pipeline from corpus to findings: QAC v0.4 and Tanzil sources → Buckwalter→Unicode parse → fourteen spectrum + five umbrella-moral root selection → distributional, network, *tafsīr*-coding, and translation-audit analyses → 312 attestations, figures, and Stage-6 causation breakdown. The pipeline is deterministic.](fig8_methodology.pdf){width=95%}

### 2.5. Quantitative Analyses

Quantitative tests beyond frequency tabulation: (a) χ²(5) and χ²(1) on uniform-stage and S1–5/S6 nulls, with a marginal-preserving permutation null (Cochran 1954; Patefield 1981; Mehta and Patel 1983; Agresti 2013, §3.5);[^perm-note] (b) three monotonic-trend tests (Spearman ρ, Mann–Kendall, Cochran–Armitage-style OLS slope); (c) two-sided exact binomials against the 0.74 Meccan-ayat baseline, Holm–Bonferroni-adjusted over the family of fourteen per-root tests, with sensitivity tables at baselines 0.70–0.78 and a family-size sensitivity check;[^family-size] (d) morphological breakdown by POS; (e) aya-level co-occurrence network (cf. Mottaghi et al. 2024) with weighted degree, betweenness, closeness, and eigenvector centrality, bootstrap 95% percentile CIs (10,000 ayat-resamples; fixed RNG seed).

[^perm-note]: The permutation null holds per-root counts fixed and randomly permutes the fourteen stage labels (10,000 permutations, fixed RNG seed 20260509); the empirical *p* is the fraction of permuted χ² values meeting or exceeding 227.15. This is the natural extension of Fisher-exact reasoning to a many-cell design (Patefield 1981; Mehta and Patel 1983).

[^family-size]: The reported family size of fourteen is the per-root Meccan/Medinan binomial family. A strict reading would expand the family to ≈ 20 (adding the omnibus χ²(5), S1–5/S6 χ²(1), three trend tests, and A-only re-analysis). Under the strict family, *karh* and *baghy* remain below α = 0.05; *ghayẓ* moves from adj. ≈ 0.019 to 0.027 (still significant); *sakhaṭ* moves from adj. 0.050 to 0.075 (substantively informative — see Section 3.5.2). Conclusions of Sections 3.5–3.8 are robust to the family-size choice.

### 2.6. Qualitative Analyses

Qualitative complements: (a) comparative etymology across the four lexica (Table 1); (b) comparative *tafsīr* on nine commentaries — al-Ṭabāṭabāʾī, al-Zamakhsharī, al-Ṭabarsī, Ibn ʿĀshūr, al-Ṭabarī, al-Qurṭubī, Ibn Kathīr, Sayyid Quṭb, ʿAbduh–Riḍā, with al-Qushayrī's *Laṭāʾif al-Ishārāt* for Sufi cross-checking on *kaẓm al-ghayẓ*; (c) phenomenological analysis of contextual markers (*ḍīq al-ṣadr*, *ḥuzn al-qalb*, *ḍāqa dharʿan*); (d) illustrative translation-criticism on five English translations at canonical exemplar verses (Section 3.10).

### 2.7. Validity Check

Fourteen headline exemplar verses — one per core root — were independently verified against the corpus output (Q. 17:23, 2:216, 15:97, 2:38, 43:55, 7:126, 47:28, 40:10, 48:6, 68:25, 3:134 [with Q. 67:8 *tamayyuz*], 42:42, 96:6, 25:21); all matched the Uthmani edition.

---

## 3. Results

### 3.1. The Four-Lexicon Etymology Table

Table 1 summarises the canonical glosses of each root across four reference lexica.

**Table 1.** Comparative etymology of the fourteen core roots across the four authoritative Arabic lexica.

| Stage | Root | Maqāyīs (Ibn Fāris) | Mufradāt (al-Rāghib) | Lisān al-ʿArab (Ibn Manẓūr) | Taḥqīq (al-Mostafawi) |
|:-:|:----:|:---|:---|:---|:---|
| 1 | ʾ-f-f | "*kalimatu taḍajjurin*" (a word of vexation); smallest audible expression of displeasure | the lowest verbal expression of displeasure (*adnā kalimati al-taḍajjur*) | term of irritation (*taḍajjur*) directed at someone or something disliked; cf. *uffah* (sub-vocal sigh) | minimal vocal sign of inner aversion; pre-anger affective register |
| 1 | k-r-h | dislike, finding burdensome; coercion (*ikrāh*) | aversion of the soul; structurally extended to coercion | what is disliked by nature or by reason | inner *karāha* vs. structural *ikrāh* (the latter is not an emotion) |
| 2 | ḍ-y-q | constriction; absence of opening | the state of being pressed upon, contrasted with capacity (*saʿah*) | reduction of available space, from *saʿah* to *ḍīq* | inner or outer absence of expansion (*basṭ*) |
| 2 | ḥ-z-n | rough/uneven ground → heaviness of soul | sorrow as the opposite of joy (*faraḥ*) | rugged ground, then roughness of the self | affective response to perceived loss |
| 2 | ʾ-s-f | intense grief mixed with anger | extreme anger conjoined with grief | reaching the limit of grief and anger | composite of grief and proximate anger |
| 3 | n-q-m | *al-naqimah*: disapproval (*inkār*) coupled with intent to punish; cf. *intaqama min* = exact retribution from | objecting to (*ankara ʿalā*) and seeking redress (*ʿuqūbah*) against a reprehensible act | strong denunciation (*ankara ashadda al-inkār*) yoked to *ʿuqūbah*; basis of divine attribute *al-Muntaqim* | evaluative anger oriented toward retribution; cognition-grounded, action-tilted |
| 3 | s-kh-ṭ | severe aversion and ethical rejection | the opposite of *riḍā* (consent), with intensity | severe non-acceptance with judgment | declarative rejection grounded in moral assessment |
| 3 | m-q-t | the most intense form of *ibghāḍ* (Zajjāj) | aversion arising from observing a *qabīḥ* act (al-Rāghib) | *ashaddu al-ibghāḍ*; aversion-distance rather than approach-aggression | purely evaluative moral aversion |
| 4 | gh-ḍ-b | inner agitation and motion | the boiling of the heart's blood seeking retribution | a rising perturbation of the soul | directed emotion enabling retributive action |
| 4 | ḥ-r-d | *ḥarada*: to be angry; also the act of *qaṣd* (deliberate aim) | conjoining *ghaḍab* with *qaṣd*: anger directed by purpose, viz. denial | *ḥarada* "to act/move toward an aim with resolve while in anger"; cf. *ḥarīd* = isolated, the angry-aloof | anger weaponised through deliberate resource-denial (Q. 68:25 *aṣḥāb al-jannah*); affective + volitional + miserly composite |
| 5 | gh-y-ẓ | pressure and surge, contained | the most intense forms of contained anger | filling of the self with restrained anger | high-pressure emotional accumulation |
| 6 | b-gh-y | seeking beyond rightful bounds | overstepping the path of right | dominance through aggression | aggressive action with intent to oppress |
| 6 | ṭ-gh-y | overflow of water past its bank | crossing the permitted measure | severe transgression of the limit | rebellious shattering of normative bounds |
| 6 | ʿ-t-w | severe rebellion with arrogance | extreme self-aggrandisement in disobedience | transgressing the limit, with *istikbār*-attachment as collocational feature | entrenched rebellious posture (a property of moral character) |

The table grounds two distinct claims at different evidential strengths. The *pairwise ordering relations* among many root-pairs (e.g. *uff* < *ghaḍab*; *karāha* < *maqt*; *ghaḍab* < *ghayẓ*; *naqm* < *baghy*) are internally encoded in the lexicographic tradition: the four authoritative lexica already gloss each root with progressively externalised and structural meanings. The *partition into six discrete phenomenological stages*, by contrast, is the analytical contribution of the present study, licensed jointly by the lexicographic ordering, the *tafsīr* readings of Sections 3.3–3.8, and the morphological and distributional evidence of Section 3.2.

### 3.2. Distributional Summary

Table 2 and Figures 2–5 report the principal distributional facts for the fourteen roots: per-root and per-stage frequency, Meccan/Medinan split, and morphological breakdown by POS.

**Table 2.** Distributional profile of the fourteen core roots (Wilson-score 95% CIs on the Meccan-rate point estimate; baseline = 0.74).

| Stage | Root | n | M | Md | M-rate (95% CI) | Notes |
|:-:|:-:|:-:|:-:|:-:|:-:|:--|
| 1 | ʾff | 3 | 3 | 0 | 1.00 [0.44, 1.00] | All Meccan; *n* too small for inference |
| 1 | krh | 41 | 14 | 27 | 0.34 [0.22, 0.49] | Medinan-tilted, CI excludes baseline; Holm-adj. ≈ 1.4 × 10⁻⁶ |
| 2 | ḍyq | 13 | 9 | 4 | 0.69 [0.42, 0.87] | CI includes baseline; inner constriction |
| 2 | ḥzn | 42 | 26 | 16 | 0.62 [0.47, 0.75] | CI includes baseline; valence transversal (Section 3.4.2) |
| 2 | ʾsf | 5 | 5 | 0 | 1.00 [0.57, 1.00] | Underpowered; CI excludes baseline at boundary only |
| 3 | nqm | 17 | 12 | 5 | 0.71 [0.47, 0.87] | CI includes baseline; not FDR-significant |
| 3 | sxṭ | 4 | 0 | 4 | 0.00 [0.00, 0.49] | CI excludes baseline; Holm-adj. = 0.050 |
| 3 | mqt | 6 | 4 | 2 | 0.67 [0.30, 0.90] | Wide CI; includes baseline |
| 4 | ghḍb | 24 | 13 | 11 | 0.54 [0.35, 0.72] | CI excludes 0.74 baseline; central anger lexeme |
| 4 | ḥrd | 1 | 1 | 0 | — | Hapax: sūrat al-Qalam, Q. 68:25 |
| 5 | ghyẓ | 11 | 3 | 8 | 0.27 [0.10, 0.57] | Medinan-tilted; Holm-adj. ≈ 1.9 × 10⁻² — survives FDR |
| 6 | bghy | 96 | 55 | 41 | 0.57 [0.47, 0.67] | CI excludes baseline; Holm-adj. ≈ 5.3 × 10⁻³ — survives FDR; bridge node (Section 3.8.5) |
| 6 | ṭghy | 39 | 29 | 10 | 0.74 [0.59, 0.85] | CI includes baseline; not FDR-significant |
| 6 | ʿtw | 10 | 9 | 1 | 0.90 [0.60, 0.98] | CI includes baseline; *istikbār*-attached |
| **Σ** | — | **312** | **183** | **129** | — | |

We lead the small-*n* roots (*asaf* at *n* = 5, *sakhaṭ* at *n* = 4, *mqt* at *n* = 6) with the Wilson-score CI rather than the *p*-value; the Holm-Bonferroni adjustment then carries the inferential weight across the family.

Across the six stages: S1 = 44; S2 = 60; S3 = 27; S4 = 25; S5 = 11; S6 = 145. Two distinct nulls bear on these data, answering different questions. The *uniform-six-stage null* (is the per-stage distribution uniform?) is unambiguously rejected by the asymptotic χ²(5) = 227.15, *p* < 0.001 (Cramér's *V* = 0.38, Cohen's *w* = 0.85), since *baghy* alone supplies 96 of 312 attestations. A *marginal-preserving permutation null* holding per-root counts fixed and randomly permuting the fourteen stage labels tests instead "*conditional on baghy's mass-dominance*, is our partition more skewed than a random six-binning of the same roots?" — the empirical *p* = 0.24 says no. This is not evidence that the distribution is uniform (already ruled out); it is evidence that the omnibus χ² cannot discriminate our partition from alternative six-bin partitions of the same roots. The structural case for the six-stage architecture rests on the qualitative evidence of Sections 3.1 and 3.3–3.8 together with the morphological-gradient and Meccan/Medinan-specialisation evidence below.

The S1–5/S6 χ²(1) = 1.55 (Cohen's *w* = 0.07) fails to reject equal split between the phenomenological core (167) and the behavioural pole (145) — absence of evidence of a difference, *consistent with* the bidirectional-causation reading of Section 3.8.5 and Section 4.3.

#### 3.2.1. Monotonic-Trend Tests

Three monotonic-trend tests of stage rank against attestation frequency all fail to reject the no-trend null: Spearman ρ = –0.09 (*p* = 0.85), Mann–Kendall *z* = –0.38 (*p* = 0.71), Cochran–Armitage-style OLS slope = 10.17 (*p* = 0.40). The continuum orders by *semantic intensity*, not attestation frequency. The Qur'an is a closed hortatory text whose lexical weights are pedagogically determined: density is heaviest at the two poles of moral consequence (S1–2, entry points for *kaẓm*, *taqwā*, *ḥilm*; S6, the structural pathologies most frequently denounced), with S3–5 as middle-trajectory states. A flat trend is what the theory predicts.

![**Figure 2.** Per-root and per-stage frequency of the 312 core attestations. *Left*: per-root frequency (bar colour encodes stage). *Right*: stage totals S1 = 44, S2 = 60, S3 = 27, S4 = 25, S5 = 11, S6 = 145. χ²(5) = 227.15 asymptotic, but permutation null *p* = 0.24 (Section 3.2); S1–5/S6 χ²(1) = 1.55, consistent with the bidirectional-causation reading of Section 3.8.5.](fig2_frequency_by_stage.pdf){width=95%}

![**Figure 3.** Stacked Meccan/Medinan distribution. Three roots survive Holm-Bonferroni correction (α = 0.05): *karh* (Medinan), *baghy* (Meccan), and *ghayẓ* (Medinan); *sakhaṭ* at adj. *p* = 0.050. *Asaf*, *naqm*, *ʿutuww* tilts are contextual. The patterns instantiate *discursive-contextual specialisation* (Section 4.4).](fig3_meccan_medinan.pdf){width=95%}

![**Figure 5.** Morphological profile by POS. Verbal dominance at S1–2 (*ḥzn* 88% verbal, *ḍyq* 62%), nominalisation at S4 (*ghḍb* 16n/6v), peak nominality with participial forms at S6 (*ṭāghūt*, *bāghin*). The verbal→nominal gradient is independent corpus-internal evidence for the action-intensity continuum.](fig5_morphology_stack.pdf){width=95%}

### 3.3. Stage 1 — Pre-Anger Displeasure

**3.3.1. *Uff* (3; all Meccan).** *Uff* (*taḍajjur*) is the Qur'anic register's lowest verbal expression of displeasure. Its three attestations occupy paradigmatic moral positions: sūrat al-Isrāʾ (Q. 17:23) prohibits saying *uff* to one's parents — the lowest sign of displeasure weighted at the highest relational stake; sūrat al-Anbiyāʾ (Q. 21:67) places it in Abraham's mouth confronting idol-worshippers; sūrat al-Aḥqāf (Q. 46:17) ascribes it to a rebellious child reproaching believing parents.

**3.3.2. *Karh* (41; 14M/27Md; Holm-adj. *p* ≈ 1.4 × 10⁻⁶ — survives FDR).** *Karh* exhibits a twofold structure: inner *karāha* (pre-anger evaluative dislike, framed as reformable by sūrat al-Baqara, Q. 2:216, *ʿasā an takrahū shayʾan wa-huwa khayrun lakum*; the S1 sense), and structural *ikrāh* (coercion — not an emotion but a structural extension into compulsion: Q. 2:256, *lā ikrāha fī al-dīn*; Q. 16:106; Q. 24:33). Inclusion rests on the *karāha* sense; the structural *ikrāh* in Medinan community-discipline contexts (consent in marriage, freedom in religion) accounts for the Medinan tilt.

### 3.4. Stage 2 — Inner Pressure and Contraction

Stage 2 brings together three roots (*ḍ-y-q*, *ḥ-z-n*, *ʾ-s-f*) with sixty attestations.

**3.4.1. *Ḍīq* (13; 9M/4Md).** Ibn Fāris glosses *ḍyq* as constriction/narrowness; al-Rāghib opposes it to *saʿah*. The root appears predominantly in *ḍīq al-ṣadr* (constriction of the chest), localising the experience to the embodied site (sūrat al-Ḥijr, Q. 15:97, the prophetic response to social rejection). Al-Ṭabāṭabāʾī (*al-Mīzān* 12:195, ad Q. 15:97: *wa-laqad naʿlamu annaka yaḍīqu ṣadruka bimā yaqūlūn*) reads the verse as expressing divine *knowledge of* prophetic *ḍīq* rather than prohibition. The compound *ḍāqa bihim dharʿan* in the Lot narrative (sūrat Hūd, Q. 11:77/80) figures post-anger *blocked* aggression: trigger *sīʾa bihim* → constriction → aspirational voicing *law anna lī bikum quwwatan* → transfer of agency to the divine. *Ḍyq* thus sits at both poles of the spectrum (pre-anger contraction and upper-pressure inhibition); the morphological profile (8v / 3n / 1 ptcp) registers a transient, situationally-induced state.

**3.4.2. *Ḥuzn* (42; 26M/16Md).** The most frequent and most verbal S2 lexeme (88% verbal). Ibn Manẓūr preserves the primary sense "rugged, uneven ground"; the metaphorical extension figures grief as inner roughness (anticipating Kövecses 2000 on EMOTION IS A LANDSCAPE). Sūrat al-Baqara (Q. 2:38) pairs *ḥuzn* with *khawf* and opposes both to divinely-given guidance. *Ḥuzn* has four valences: standalone grief over loss (Jacob over Joseph, sūrat Yūsuf, Q. 12:84), externally-induced sorrow from being wronged, positive moral compunction (the affective register of *tawba*), and anger turned inward when externally inhibited; inclusion at S2 is justified by corpus density and proximity of the second and fourth valences to the anger field.

**3.4.3. *Asaf* (5; 5M/0Md).** Al-Rāghib glosses *asaf* as the conjunction of grief and anger (*al-jamʿ bayna al-ḥuzn wa-l-ghaḍab*). Sūrat al-Zukhruf (Q. 43:55, *fa-lammā āsafūnā intaqamnā minhum*) frames it as the immediate causal precursor of divine retribution (al-Ṭabarsī, *Majmaʿ* 9:82). The compound *ghaḍbān asifan*, applied to Moses on his return to the calf-worshippers (Q. 7:150; Q. 20:86), generates a three-layer dialectic in which *ghaḍab* is outward-kinetic and *asaf* the inward-compassionate ground. The 5/0 distribution is power-bound (Wilson CI [0.57, 1.00]). The aya-level network (Figure 4) confirms S2 coherence: *ḥzn*–*ḍyq* is the strongest single edge (weight 3).

### 3.5. Stage 3 — Evaluative Aversion

Stage 3 brings together three roots (*n-q-m*, *s-kh-ṭ*, *m-q-t*) with twenty-seven attestations marking distinct modes of evaluative aversion. *Maqt* is the lexicographic superlative of *aversion* (Zajjāj, *ashaddu al-ibghāḍ*) but is placed between *sakhaṭ* and *ghaḍab* on the action-intensity axis because the dimension here is intensity of *action*, not intensity of *aversion*.

**3.5.1. *Naqm* (17; 12M/5Md).** *Naqm* is vengeful disapproval — anger grounded in moral evaluation and oriented toward retribution. Sūrat al-Aʿrāf (Q. 7:126, *wa-mā naqamū minnā illā an āmannā bi-āyāti rabbinā*) is the linguistic exemplar; al-Ṭabarī (*Jāmiʿ al-bayān* 13:23 ad loc.) glosses *naqamū* as *ʿābū wa-ankarū*, exposing the *taʿaṣṣub*-structure of disbelief (al-Qurṭubī, *al-Jāmiʿ* 7:262 convergent). The lexeme generates *al-muntaqim* as a divine attribute (Q. 32:22 and parallels). The Wilson CI includes the baseline.

**3.5.2. *Sakhaṭ* (4; 0M/4Md).** The exclusive-Medinan distribution is one of the paper's principal distributional findings.[^sakhat-baseline] Holm-adjusted *p* = 0.050 — borderline. All four attestations are tied to the *Munāfiqūn* in their Medinan-period exegesis: sūrat Muḥammad (Q. 47:28, *ittabaʿū mā askhaṭa Allāh wa-karihū riḍwānahu*) is canonical, though al-Ṭabarī notes that sūrat al-Māʾida (Q. 5:80) is exegetically discussed as directed at the People of the Book rather than the *Munāfiqūn* properly. Following Narimani, Iqbali, and Chari (2021), we read *sakhaṭ* as sustained *ethical disapprobation* rather than instantaneous emotional surge; we propose:

> *Hypothesis (Discursive Specialisation of sakhaṭ):* *sakhaṭ* operates as a discursively specialised lexeme reserved for divine displeasure with the *Munāfiqūn* — agents whose *ẓāhir* departs from their *bāṭin*. Since the *Munāfiqūn* category is constitutively a Medinan-period phenomenon, *sakhaṭ* attests exclusively in Medinan suras. This is one instance of a general phenomenon of *discursive-contextual lexical specialisation*, of which *karh* (Medinan-community discipline) and the umbrella patterns *jrm* (Meccan) / *fsq* (Medinan) are convergent.

[^sakhat-baseline]: The 0.74 baseline is the proportion of ayat (not suras) classified Meccan in the QAC metadata; we use the ayat-weighted rate because an attestation drawn at random from the corpus hits an aya, not a sura. A sensitivity table over baselines 0.70–0.78 yields two-sided *p* values from 0.0081 (at 0.70) to 0.0023 (at 0.78); the conclusion is robust across the range.

**3.5.3. *Maqt* (6; 4M/2Md).** *Maqt* is *intense moral aversion*: the four lexica converge on *ashaddu al-ibghāḍ* (Zajjāj); al-Rāghib grounds it in observation of a reprehensible act, making *maqt* purely evaluative. The canonical exemplar is sūrat Ghāfir (Q. 40:10, *la-maqtu Allāhi akbaru min maqtikum anfusakum*), the doubled *maqt* comparing divine moral aversion at the disbelievers with their own retrospective self-*maqt* on the Day of Resurrection (al-Ṭabarī, *Jāmiʿ al-bayān* 21:351 ad loc.; al-Qurṭubī, *al-Jāmiʿ* 15:296 convergent). Sūrat al-Nisāʾ (Q. 4:22), sūrat Fāṭir (Q. 35:39), and sūrat al-Ṣaff (Q. 61:3) stabilise the lexeme as moral aversion as evaluative response, distinct from the kinetic-motor *ghaḍab* of Stage 4.

### 3.6. Stage 4 — Active Anger

**3.6.1. *Ghaḍab* (24; 13M/11Md).** The central anger lexeme — near-balanced Meccan/Medinan distribution marks it as the unmarked default. The four lexica gloss it as inner agitation oriented toward retribution (al-Rāghib) or inner motion disposing the agent to action (Ibn Fāris); predicated balance-fully of God (sūrat al-Fatḥ, Q. 48:6), prophets, and believers. Morphologically 67% nominal (16n/6v/2 ptcp) vs *ḥuzn*'s 88% verbal: *ghaḍab* is a structural concept-state, not a transient affect. Al-Rāzī (*Mafātīḥ al-Ghayb*) glosses divine *ghaḍab* in the register of *irādat al-ʿuqūbah* — a normative-juridical orientation, not an emotional response. Network analysis places *ghḍb* among the top three for betweenness (point estimate 0.17).

**3.6.2. *Ḥard* (Q. 68:25, hapax).** A hapax in the Garden-Owners parable (*wa-ghadaw ʿalā ḥardin qādirīn*): owners vowing in the night to harvest before dawn so as to deny the poor their share. Al-Ṭabarī (*Jāmiʿ al-bayān* 23:550 ad loc.) records four classical *qawls*: (i) *qaṣd* (purposive aim — Mujāhid, Ibn Zayd, Ibn ʿAbbās ʿan ʿIkrima); (ii) *ghaḍab* (anger toward the poor — Qatāda, al-Suddī); (iii) *manʿ* (withholding — al-Ḥasan); (iv) *quwwa/sūʾ* (strength or evil intent — Sufyān al-Thawrī). The affective synthesis — *ḥard* as anger weaponised through deliberate denial — converges (i) and (ii), defended by al-Ṭabrisī (*Majmaʿ* 10:90) and al-Ṭabāṭabāʾī (*al-Mīzān* 19:380); it is not the unanimous consensus but the reading we adopt, because the narrative consequence (divine destruction of the garden) requires both an affective and an intentional component.

### 3.7. Stage 5 — Compressed/Explosive Rage

**3.7.1. *Ghayẓ* and the *kaẓm* metaphor (11; 3M/8Md; Holm-adj. ≈ 1.9 × 10⁻² — survives FDR).** The four lexica converge: *ghayẓ* is compressed contained anger (al-Rāghib), the highest concentration of restrained anger (al-Mostafawi), filling of the self with restrained anger (Ibn Manẓūr) — pressurised contents of a sealed vessel. Sūrat Āl ʿImrān (Q. 3:134) commends *al-kāẓimīn al-ghayẓ*; *kaẓm* derives from the tying-off of a waterskin (Ibn Manẓūr, *Lisān* 12:519, s.v. *k-ẓ-m*), the agent-internal regulation that sustains containment. The construction itself presupposes that the believers being commended experience the *ghayẓ* they suppress; the Narimani et al. claim that *ghayẓ* in human reference is exclusive to unbelievers must therefore be qualified — transitive *ghayẓ directed at* believers is exclusively non-believer-attributed, but intransitive/experiential *ghayẓ* (the *kāẓimīn* themselves) is attributed to believers. Read through the complex container metaphor of Section 2.1.3, *ghayẓ* is the contained fluid and *kaẓm* the agent's sealing operation (Figure 6). The Medinan tilt tracks the discursive context: inner anger management is a salient pedagogical concern in the formative Medinan community.

**3.7.2. *Tamayyuz* in sūrat al-Mulk, Q. 67:8 (manifestation, not separate root).** The verb *tamayyazu* in *takādu tamayyazu min al-ghayẓ* (Q. 67:8) walks from the *lughawī* gloss to the CMT construal in two steps. *First*, the lexicographic ground: in *Mufradāt* and *Lisān*, the dominant gloss of *m-y-z* is *al-tafrīq bayna al-mukhtaliṭ* — separating things that have been mixed; al-Ṭabarī (*Jāmiʿ al-bayān* ad loc.) glosses *yanqaṭiʿu baʿḍuhā min baʿḍ*; al-Zamakhsharī (*al-Kashshāf* ad loc.) is convergent. *Second*, the metonymic bridge: separation of contents within a sealed vessel, taken under the complex container metaphor of Section 2.1.3, is naturally construed as a vessel-internal failure mode — distinct from the English exit-typed exemplars (*she blew her top*) where the container is preserved and contents escape. Ibn ʿĀshūr (*al-Taḥrīr wa-l-Tanwīr* 29:25) reads compatibly, emphasising the violence of the inner severance and the figurative attribution of rage to the Hell-fire as an animate vessel; his is the strongest classical ally of the construal we defend. The two readings are compatible. H5 is *exemplified* rather than corroborated — Q. 67:8 is the most lexically transparent Qur'anic instance, not a deductive proof. We treat *tamayyuz* as a manifestation of Stage 5.[^qiraat-mulk-q67]

[^qiraat-mulk-q67]: The canonical *qirāʾāt* tradition records minor variation on the verb form (Ḥafṣ ʿan ʿĀṣim reads *tamayyazu*; alternative voweling in some readings), but the lexicographic and exegetical reading is stable.

### 3.8. Stage 6 — Behavioural Outcomes

**3.8.1. *Baghy* (96; 55M/41Md; Holm-adj. ≈ 5.3 × 10⁻³ — survives FDR).** The most frequent lexeme of the spectrum and principal bridge node. Glossed as "seeking beyond rightful bounds" (al-Rāghib) and "aggressive seeking with intent to oppress" (al-Mostafawi). Sūrat al-Shūrā (Q. 42:42) collocates *baghy* with *ẓulm*; al-Ṭabarī (*Jāmiʿ al-bayān* 21:548 ad loc.) glosses *yabghūna* as *yataʿaddawn*, reading the verse as juridically restricting recourse to those who combine oppression and *baghy*-style transgression (al-Qurṭubī, *al-Jāmiʿ* 16:36, convergent). Ibn ʿĀshūr (*al-Taḥrīr* 25:126) clarifies: *baghy* and *ẓulm* are near-synonymous, but *baghy* is specific to non-rightful aggression against another whereas *ẓulm* covers all injustice.

**3.8.2. *Baghy* as bridge node.** *Baghy* attains the highest point-estimate closeness centrality (0.55) and shared-highest betweenness (0.15) with *ghaḍab* and *asaf*. Bootstrap 95% percentile CIs (10,000 ayat-resamples) are wide — for *baghy*: betweenness ∈ [0.00, 0.31]; closeness ∈ [0.23, 0.84]; eigenvector ∈ [0.00, 0.68] — reflecting the small graph (14 nodes). On strict non-overlap, no node's centrality is significantly greater than another's. What is *robust* at the aggregate level is cross-field connectivity to the umbrella moral terms (Table 4): *baghy* shows sixteen aya-level co-occurrences with *ẓlm/jrm/fsq/ʿdw/šnʾ* combined, an integer-count pattern independent of centrality ranking.

**Table 4.** Cross-field co-occurrence of spectrum roots with umbrella moral terms (aya-level). Ties for the four newly-incorporated roots (*ʾff*, *naqm*, *maqt*, *ḥard*) are sparse and omitted.

| Root | šnʾ | jrm | fsq | ẓlm | ʿdw | Total |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| ḍyq | 0 | 0 | 0 | 0 | 0 | 0 |
| ḥzn | 0 | 0 | 0 | 1 | 1 | 2 |
| ʾsf | 0 | 0 | 0 | 1 | 1 | 2 |
| sxṭ | 0 | 0 | 0 | 0 | 0 | 0 |
| ghḍb | 0 | 0 | 0 | 2 | 3 | 5 |
| ghyẓ | 0 | 0 | 0 | 0 | 1 | 1 |
| **bghy** | **1** | **1** | **2** | **4** | **8** | **16** |
| ṭghy | 0 | 0 | 0 | 2 | 1 | 3 |
| ʿtw | 0 | 0 | 0 | 0 | 0 | 0 |

Of the total cross-field ties, nineteen (~53%) involve *baghy* — the principal lexical bridge between the anger field and the wider moral-evaluation field.

**3.8.3. *Ṭughyān* (39; 29M/10Md).** Root *ṭ-gh-y* derives from water flooding past its banks. Sūrat al-ʿAlaq (Q. 96:6–7, *kallā inna l-insāna la-yaṭghā an raʾāhu staghnā*) compresses a psychology of rebellion into a conditional: *ṭughyān* arises from the appraisal of *istighnāʾ* (self-sufficiency) — an appraisal-theoretic claim congruent with Roseman's (1996) other-caused / motive-inconsistent / high-control pattern for defiance. Qarizadeh et al. (2024) note the cognitive structure; we identify *ṭughyān* as the cognitive-appraisal node of Stage 6.

**3.8.4. *ʿUtuww* (10; 9M/1Md; Holm-adj. *p* = 1.00 — not FDR-significant).** The most extreme lexeme — "obstinate excess" (Ibn Manẓūr), "extreme self-aggrandisement in disobedience" (al-Rāghib). Sūrat al-Furqān (Q. 25:21) collocates *ʿatū ʿutuwwan kabīrā* with *istakbarū fī anfusihim*: rebellion crystallised into existential posture. The 9/1 split tracks the lexeme's rhetorical function as terminal designation for Nūḥ-, ʿĀd-, Thamūd-, and Pharaonic-people narratives but is not distinguishable from the baseline under the binomial.

**3.8.5. Bidirectional Causation and a *Tafsīr*-Grounded Audit.** *Baghy* arises frequently from greed and *ʿulw fī al-arḍ* (cf. sūrat al-Anʿām, Q. 6:21); *ṭughyān* — paradigmatically Pharaonic (sūrat al-Nāziʿāt, Q. 79:17) — is rooted in structural arrogance; sūrat al-Shuʿarāʾ (Q. 26:55, *innahum lanā la-ghāʾiẓūn*) reverses polarity to show oppressor-anger arising *from* the rebellion of the oppressed; *ʿutuww* attaches to *istikbār* as settled character. The causation arrow is bidirectional. Each of the 145 Stage-6 attestations was coded against the joint reading of *al-Mīzān*, *al-Kashshāf*, *Majmaʿ al-Bayān*, and *al-Taḥrīr wa-l-Tanwīr* under a three-label codebook: **A** (anger-origin: immediate exegetical antecedent is an anger-type affective state), **S** (structural-origin: antecedent is *istikbār*/*ʿulw*/greed without explicit anger antecedent), or **A+S** (both present).

*Coding protocol.* Two independent graduate-level coders (the corresponding author and an Arabic-literature graduate trained on the codebook with commentary excerpts) coded all 145 attestations: (i) not blinded to root identity (root is intrinsic to the textual context); (ii) blinded to the bidirectional-causation hypothesis at the coding stage; (iii) attestation order randomised per coder via fixed RNG seed (`np.random.default_rng(20260509)`); (iv) disagreements (n = 14) reconciled in joint session against the four commentaries, with original-pass codings used for κ. Cohen's κ = 0.79 — *substantial* agreement (Landis and Koch 1977); per-label κ (A = 0.82, S = 0.78, A+S = 0.74), per-root κ (*baghy* 0.81, *ṭughyān* 0.77, *ʿutuww* 0.70), 3 × 3 confusion matrix, and full codebook are deposited at `data/concordance/stage6_*.{csv,md}`.

*Results.* A = 38 (26%), S = 71 (49%), A+S = 36 (25%); by root, *baghy* 22A/50S/24A+S, *ṭughyān* 11A/19S/9A+S, *ʿutuww* 5A/2S/3A+S. χ²(1) on A-only (S1–5 = 167 vs. anger-derived S6 = 38) = 81.4, *p* < 0.001 — the phenomenological core dominates anger-derived outcomes ~4.4×. The full-S6 near-balance is therefore explained: S-attestations belong to an adjacent moral-anthropological field of *ẓulm-istikbār-ʿulw*; *baghy*/*ṭughyān*/*ʿutuww* are not coextensive with "anger outcomes" in the strict sense.

![**Figure 4.** Aya-level co-occurrence network; edges weighted by shared-ayat count. Strongest edge *ḥzn–ḍyq* (weight 3) corpus-validates the S2 grouping. *Baghy* anchors the right cluster with edges to *ẓlm/jrm/fsq*. Transitive structure (no direct S1→S6 edges) is consistent with both the action-intensity gradient and the bidirectional S6 reading (Section 3.8.5).](fig4_cooccurrence.pdf){width=95%}

![**Figure 7.** Three centrality measures with bootstrap 95% percentile CIs on the co-occurrence graph (weighted degree, betweenness, closeness). *Baghy* leads on closeness (0.55, CI [0.23, 0.84]) and shares highest betweenness (0.15, CI [0.00, 0.31]) with *ghaḍab* and *asaf*. Wide CIs reflect the small graph; bridging-role claim consistent with point estimates but qualified by bootstrap (Section 3.8.2).](fig7_centrality.pdf){width=95%}

### 3.9. Robustness Checks: The Umbrella Moral Terms

The five umbrella roots (Table 5) confirm that the spectrum's structure is not artefactual. The opposing patterns of *jrm* (strongly Meccan) and *fsq* (significantly Medinan) instantiate the same discursive-contextual specialisation identified for *sakhaṭ* and *karh* — the umbrella analysis confirms a general phenomenon.

**Table 5.** Distribution of umbrella moral terms.

| Root | n | M | Md | Binomial *p* | Interpretation |
|:----:|:-:|:-:|:-:|:-:|:---|
| šnʾ | 3 | 1 | 2 | — | *n* too small |
| jrm | 66 | 60 | 6 | < 0.0001 | Strongly Meccan; anti-*shirk* polemic |
| fsq | 54 | 20 | 34 | 0.0007 | Significantly Medinan; community discipline |
| ẓlm | 315 | 211 | 104 | — | Pervasive meta-category |
| ʿdw | 106 | 47 | 59 | 0.008 | Tilts Medinan; mutual antagonism |

### 3.10. Comparative Translation: An Illustrative Observation

A four-verse, five-translation sample (Table 6) illustrates the levelling pattern: *ghayẓ* (Q. 3:134) is rendered with terms (*anger*, *wrath*, *rage*) routinely used also for *ghaḍab*, with the containment differentia carried only by the contextual verb of restraint; *tamayyuz* (Q. 67:8) is rendered unevenly, with only Arberry's "well-nigh bursts asunder" preserving the structural-disintegration component. The sample is illustrative; a stratified evaluation across ~30 verses with multi-rater coding is left to future work.

**Table 6.** Translation of four canonical verses across five English translations (illustrative sample).

| Term & verse | Yusuf Ali | Pickthall | Arberry | Saheeh Intl. | Hilali-Khan |
|:----:|:---|:---|:---|:---|:---|
| *ḍīq* (Q. 15:97) | "thy heart is distressed" | "thy bosom is at times oppressed" | "thy breast is straitened" | "your chest is constrained" | "your breast feels tight" |
| *ghayẓ* (Q. 3:134) | "restrain anger" | "control their wrath" | "restrain their rage" | "suppress anger" | "repress anger" |
| *tamayyuz* (Q. 67:8) | "almost burst with fury" | "almost burst with rage" | "well-nigh bursts asunder with fury" | "almost bursts with rage" | "almost bursts up with fury" |
| *ṭughyān* (Q. 96:6) | "transgresses all bounds" | "rebelleth" | "waxes insolent" | "transgresses" | "transgresses (boundary)" |

### 3.11. Summary of Computational Corroboration (Supplementary Materials S1–S4)

Four NLP analyses extend the main pipeline over the same 312 attestations; full detail in the Supplementary Materials. **S1 (cross-translation semantic drift)** with multilingual MPNet over ten parallel renderings recovers three drift bands mapping onto the spectrum (affective-core lexemes drift < 0.20, evaluative-aversion and containment-pressure lexemes > 0.22, *ṭughyān* topping non-hapax) — convergent with Section 3.10. **S2 (CAMeLBERT-CA clustering)** yields silhouette = −0.082, NMI = 0.077 against the six-stage labelling; a Monte-Carlo baseline (10,000 random 6-partitions of the fourteen roots into stages of the observed sizes) gives mean random NMI ≈ 0.094 [0.041, 0.156]. The observed NMI sits below the random mean — this is a clear null in which the model clusters by root identity, and the spectrum adds analytical structure beyond the language model's distributional view. **S3 (PMI-weighted network)** corrects raw-count artefacts: *asaf*–*ghaḍab* (npmi = 0.59) emerges as the strongest signal and *baghy*'s raw-count dominance is shown to be partly a frequency artefact. **S4 (Nöldekean diachronic null)** finds Spearman ρ = −0.157; R² ≈ 0.025 explains < 3% of variance — a diachronic effect statistically detectable (*p* = 0.006) but substantively a null, consistent with the claim that the taxonomy organises by intensity, not chronology.

---

## 4. Discussion

### 4.1. The Integrated Logic of Escalation

The findings cohere into a single structural claim: the Qur'anic anger lexicon encodes a logic of escalation along three dimensions — locus (inner → outer), intensity (low → high), and scope (individual → structural). In compact form: *Pre-anger displeasure → Inner pressure → Evaluative aversion → Active anger → Compressed rage → Behavioural outcomes (with caveats)*. The arrows index conditional intensification at each step where regulation may succeed or fail. Stage 6 is distinctive: the move into behavioural outcomes is not a deterministic escalation from anger but is influenced by independent vectors (greed, *istikbār*, structural arrogance), which is why the near-balance between S1–5 and S6 is theoretically informative rather than paradoxical.

### 4.2. Convergence with Contemporary Emotion Psychology

The continuum maps onto four families of contemporary emotion theory at points of structural convergence, sufficient to ground the Islamic-psychology implications of Section 4.7 and to identify where the Qur'anic lexicon extends the contemporary models.

**Gross's process model.** Gross (1998, 2014, 2015) partitions emotion regulation into five sequential strategies (*situation selection*, *situation modification*, *attentional deployment*, *cognitive change*, *response modulation*). The Qur'anic continuum cross-cuts this typology rather than mapping one-to-one: situation selection is forward-looking and so does not match the S1 lexemes, which are reactions to a present trigger. **S1** (*uff*, *karāha*) is better located at cognitive change / response-tendency modulation in nuce. **S2** (*ḍīq*, *ḥuzn*, *asaf*) implicates situation modification and attentional deployment. **S3** (*naqm*, *sakhaṭ*, *maqt*) is paradigmatically cognitive change. **S4** (*ghaḍab*, *ḥard*) lies at the response-selection threshold. **S5** is response modulation with two sub-strategies: *kaẓm* (Q. 3:134) is closest to *expressive suppression*, but the Qur'anic moral commendation of *kāẓimīn al-ghayẓ* need not entail the physiological costs Gross associates with suppression, and Sufi readings (al-Qushayrī's *Laṭāʾif al-Ishārāt* ad loc.) tilt the construct toward *cognitive reappraisal* in the *taqwā* frame; we do not read *kāẓim al-ghayẓ* as unambiguously expressive-suppression. *Tamayyuz* figures the failure mode regardless. **S6** lies beyond the episode-bounded scope of Gross's model — structural-moral pathologies of personhood, with the Section 3.8.5 bidirectional-causation caveat.

**Plutchik; Spielberger.** Plutchik's (1980, 2001) three-level escalation (annoyance → anger → rage) is refined by the Qur'anic continuum, which partitions annoyance into vocal irritation (*uff*, S1), inner aversion (*karāha*, S1), and inner pressure (S2) — three stages where Plutchik has one label — and inserts compressed rage (*ghayẓ*, S5) between anger (≈ S4 *ghaḍab*) and terminal rage. Spielberger's STAXI-2 (1999) trichotomy of *trait*, *state*, and *control* is realised at the lexical surface: trait-like sustained states (*ḥuzn*, *ḍīq*, *karāha*); state-like situational responses (*sakhaṭ*, *maqt*, *ghaḍab*); and *kaẓm* (Q. 3:134) as the Qur'anic anger-control lexeme, operationally close to Spielberger's anger-in / suppression construct but with explicit moral commendation.

**Appraisal theory: Scherer's checks and Roseman's *ṭughyān*-pattern.** Appraisal theory (Frijda 1986; Lazarus 1991; Scherer 2001, 2005; Roseman 1996) holds that emotional response is determined not by stimulus alone but by cognitive *appraisal* along defined dimensions. Scherer's component-process model specifies four sequential checks; the Stage-3 lexemes operate as a lexicon for the normative-significance check at progressively higher intensities (*naqm* → *sakhaṭ* → *maqt*). Sūrat al-ʿAlaq (Q. 96:6–7) conditions *ṭughyān* on the appraisal of *istighnāʾ*: the agent perceives high coping potential, low external constraint, and self-agency. On Roseman's (1996) appraisal structure, defiance and contempt are *other-caused* and *motive-inconsistent* (the agent rebels against an other-imposed normative constraint perceived as inconsistent with the agent's self-conception). *Ṭughyān* on *istighnāʾ* fits this pattern: the divine command is the other-caused, motive-inconsistent constraint that *istighnāʾ* construes as dispensable. The Qur'anic lexicon thus encodes — as architectural design rather than theoretical statement — appraisal-theoretic insights that contemporary emotion science reached independently.

### 4.3. The Phenomenology/Outcomes Balance

A naive ten-root reading once suggested 2.4× more attestations at the behavioural pole than at S1–3 combined. The revised fourteen-root inventory (167 / 145) corrects that picture: the expanded phenomenological vocabulary brings the lower stages into balance with Stage 6, consistent with both a richer affective lexicon and the bidirectional causal relation between Stage-6 lexemes and anger. In Fauconnier and Turner's (2002, 17–57) terms, Stage 6 operates as a conceptual blend whose input spaces are wrong-doing-as-supremacism and anger-as-pressure.

### 4.4. Discursive-Contextual Specialisation and Cultural Linguistics

The FDR-surviving tilts of *karh* (Medinan), *baghy* (Meccan), *ghayẓ* (Medinan), the borderline *sakhaṭ* (Medinan), the contextual Meccan tilts of *asaf*, *naqm*, and *ʿutuww*, and the umbrella patterns *jrm* (Meccan) / *fsq* (Medinan) together instantiate *discursive-contextual specialisation* — members of multi-lexeme fields attaching to specific discursive registers. The attachments are non-random: *sakhaṭ* to the *Munāfiqūn* (a Medinan phenomenon), *karh* to the structural *ikrāh* idiom of Medinan community discipline, *ghayẓ* to the *kaẓm* pedagogy of Medinan ethics, *asaf* to prior-prophet narratives (Meccan-rhetorical), *jrm* to anti-*shirk* polemic (Meccan), *fsq* to intra-community discipline (Medinan). El-Awa (2006) and Sinai (2017, 2023) supply the framework: specialisation is the pattern one expects from the Qur'an's gradual response to evolving sociolinguistic contexts.

Read through Sharifian (2011), the same data illuminate the universal–culturally-elaborated distinction of Section 2.1.3: the primary metaphors (ANGER IS HEAT; EMOTIONAL CONTAINMENT IS PHYSICAL CONTAINMENT) are robustly attested in the Qur'anic *ghayẓ*–*kaẓm* register and support the CMT universalist claim; the *culturally elaborated* layer — the distribution of affect across *qalb* (S2 *ḍīq al-ṣadr*), *ṣadr* (S2), and *nafs* (S2 *asaf al-nafs*), the moral commendation of *kaẓm* in the *taqwā* frame, the *Munāfiqūn*-attachment of *sakhaṭ*, and the *tamayyuz* construal of Q. 67:8 — is what the Qur'anic data illuminate beyond the universalist baseline.

### 4.5. Q. 67:8 and the Container Metaphor: A Focused Comparative Survey

The Qur'anic *ghayẓ–kaẓm–tamayyuz* triad maps onto stages (2)–(4) of the Lakoff–Kövecses scenario with unusual lexical transparency at stage (4): English exemplars (*blew his top*) lexicalise the failure-mode as *exit of contents* with the container preserved, whereas Q. 67:8, under the complex container metaphor of Section 2.1.3, supports the construal of vessel-internal failure (Section 3.7.2). A six-tradition survey contextualises the claim. *Akkadian*: *libbu* and *kabattu* as filled containers (CAD L 163–164; Bodi 2018; Neo-Assyrian bodily-mapping work in Lauri et al. 2024 confirms the FILLING/HEAT-IN-CONTAINER schema). *Biblical Hebrew*: *ḥēmâ* and *ḥarôn-ʾaph* (Kruger 2000, 2015) both EXIT-typed — except Job 32:19 (*kĕ-yayin lōʾ-yippātēaḥ … yibbāqēaʿ*), where *bāqaʿ* names the structural failure of the vessel; this is the one clear pre-Qur'anic Northwest-Semitic precedent. *Homeric Greek*: *kholos* and *mēnis* in fluid-and-heat schemas with no Iliadic vessel-rupture (Muellner 1996; Cairns 2003). *Vedic and Classical Sanskrit*: *krodha* and *manyu* in FIRE and WEAPON-RELEASE schemas, not vessel-disintegration. *Classical and Modern Chinese*: *nù*, *fèn*, *qì* with HOT *QÌ* IN A CONTAINER (Yu 1995; Kövecses, Benczes, and Szelid 2025). *Pre-Islamic Jāhilī Arabic*: *ḥamiya* and *ghalā* alongside *ghayẓ* in the cognate fluid-heat register (cf. *al-Mufaḍḍaliyyāt* nos. 38, 87, ʿAntara's *Muʿallaqa* ll. 32–35; Webb 2016, 213–245). Five of the six traditions concentrate on filling, heating, exit/overflow; the Hebrew Bible alone offers a clear parallel to vessel-rupture proper. We hold our claim at "an early and unusually transparent" lexicalisation, with Job 32:19 acknowledged as a structurally cognate Northwest-Semitic precedent. The Qur'anic data strengthen the universalist hypothesis of CMT and extend the empirical base to seventh-century Arabic.

![**Figure 6.** *Illustrative* schematisation of the ANGER-IS-A-PRESSURIZED-CONTAINER complex metaphor (after Lakoff and Kövecses 1987), instantiated by *ghaḍab → ghayẓ + kaẓm → tamayyuz*. Panel 1 (S4): *ghaḍab* — open container, affect dissipating into language. Panel 2 (S5, Q. 3:134): *ghayẓ* sealed by *kaẓm*. Panel 3 (S5 manifestation, Q. 67:8): *tamayyuz* — the construal of constituent-separation as vessel-internal failure (Section 3.7.2). The figure is heuristic; evidence is borne by the lexicographic and exegetical analysis of Sections 3.7 and 4.5.](fig6_metaphor_v2.pdf){width=100%}

### 4.6. Implications for Qur'anic Translation

A graded reference model of the spectrum offers a principled corrective to the levelling pattern that Gaanoun and Alsuhaibani (2025) and Khan et al. (2025) document at the sentiment-category level. We do not, on the strength of the four-verse illustrative sample of Section 3.10, advance translation prescriptions; a systematic stratified evaluation (~30 verses across the six stages, multi-rater coded against the spectrum) is the prerequisite. Candidate equivalents for each spectrum lexeme are catalogued in the project repository for use by translators wishing to mark intensity-position lexically.

### 4.7. Implications for Islamic Psychology

The continuum offers a culturally-grounded framework mapping onto Gross's model without importing secular vocabulary, with three conceptual implications: (i) *Prevention* — early-stage recognition through the indigenous S1–2 lexicon supports CBT-style interception of affective dysregulation; (ii) *Crisis intervention* — *kaẓm* integrates with contemporary suppression-and-reappraisal techniques; (iii) *Rehabilitation* — post-failure Stage 6 is framed as recoverable through *tawba*. These are conceptual; their translation into validated clinical interventions awaits empirical studies.

### 4.8. Limitations

Five limitations bound the inferences. (i) *Surface-lexical scope*: discourse-analytic close-reading of the spectrum's narrative deployment across suras is left for future work. (ii) *Tafsīr engagement*: a deep-dive indexing the full classical/medieval/Sufi/modernist tradition with κ-validated multi-coder reading on contested verses would deepen exegetical grounding. (iii) *Cognitive-linguistic apparatus*: engagement with classical *bayān* theory (al-Jurjānī, al-Sakkākī) would supply an indigenous substrate. (iv) *Ḥadīth integration*: a parallel concordance over Ṣaḥīḥ al-Bukhārī, Ṣaḥīḥ Muslim, and al-Kāfī would supply convergent evidence on *kaẓm* and a replication test for the underpowered *asaf* distribution. (v) *Islamic-psychology operationalisation*: Section 4.7's implications await pilot studies of *kaẓm*-grounded emotion-regulation training, validated against the STAXI and DERS. Small per-root *n* and the closed-text status of the corpus bound every inference reported above; computational evidence remains a complement to, not a replacement for, the classical philological and exegetical tradition.

---

## 5. Conclusions

*Methodologically*, the integration of Izutsu's semantic-field analysis, Kennedy–Sassoon scalar semantics, and Lakoff–Kövecses CMT — coupled with a reproducible computational pipeline over the QAC — produces an apparatus stronger than the sum of its parts; to our knowledge, this trifold integration with corpus-empirical validation has not been deployed in Qur'anic studies, although Qāʾimīniyā (2011, 2014) and Pakatchi and Afrashi (2020) have integrated Izutsu and CMT.

*Descriptively*, we produce a reproducible concordance of 312 attestations with FDR-adjusted binomial tests, marginal-preserving permutation null *p*-values, and bootstrap 95% CIs on every centrality estimate.

*Theoretically*, we formulate and defend the *Qur'anic Action-Intensity Continuum Hypothesis*: the fourteen lexemes operate as a single graded continuum structured by intensity of action and partitioned into six stages, supported by qualitative evidence from the four authoritative lexica and the broadened *tafsīr* consultation, and by quantitative evidence from frequency, distribution, morphology, and network structure. The κ = 0.79-validated audit grounds the bidirectional-causation reading of Stage 6; the six-tradition survey of Section 4.5 calibrates Q. 67:8 as an early and unusually transparent — rather than uniquely transparent — exemplification of vessel-internal failure, with Job 32:19 (*bāqaʿ*) acknowledged as a structurally cognate Northwest-Semitic precedent.

In answer to the research questions: the anger-spectrum field is a fourteen-node lexical network organised by intensity of action, with *baghy* the bridge node (closeness 0.55; ~53% of cross-field ties) and stage-internal hubs *ḥuzn* (S2) and *ghaḍab* (S4) (RQ1–RQ2); the empirical distribution is *consistent with* the continuum — asymptotic χ²(5) = 227.15, permutation null *p* = 0.24, S1–5/S6 χ²(1) = 1.55, with three roots (*karh*, *baghy*, *ghayẓ*) surviving Holm-Bonferroni and *sakhaṭ* borderline (RQ3); the continuum is structurally homologous with Gross (S1–5), Plutchik, Spielberger, and Lazarus–Scherer–Roseman appraisal theory, extending beyond all four at Stage 6 (RQ4); and conditional implications follow for Qur'anic translation and Islamic psychology (RQ5). The Qur'anic lexicon encodes a sophisticated theory of the anger spectrum in the architecture of its semantic surface; recovering it requires the integration of classical philological attentiveness, contemporary linguistic-theoretical precision, and corpus-computational verifiability. Future work should pursue discourse-analytic close-reading, deeper *tafsīr* indexing, engagement with classical *bayān* theory, ḥadīth-corpus replication, and clinical operationalisation of the *kaẓm* construct.

---

## Supplementary Materials

The following are available online: four computational corroboration analyses (S1 cross-translation semantic drift; S2 CAMeLBERT-CA contextual-embedding clustering; S3 PMI-weighted co-occurrence network; S4 Nöldekean diachronic null), with Figures S1–S3, in `paper/english/supplementary.md`. All outputs are reproducible from `nlp_upgrade_colab.py` against the committed `outputs/nlp_upgrade/` directory.

## Author Contributions

Conceptualization, K.J.; methodology, K.J. and A.J.; software, A.J.; validation, K.J. and A.J.; formal analysis, K.J.; investigation, K.J.; data curation, A.J.; writing—original draft preparation, K.J.; writing—review and editing, K.J. and A.J.; visualization, A.J.; supervision, K.J.; project administration, K.J. All authors have read and agreed to the published version of the manuscript.

## Funding

This research received no external funding.

## Institutional Review Board Statement

Not applicable. This study used only publicly released text-corpus data and involved no human or animal subjects.

## Informed Consent Statement

Not applicable.

## Data Availability Statement

The data presented in this study are openly available. The complete reproducible Python pipeline (MIT License), the derived CSV concordance for the fourteen core spectrum roots (312 attestations), distributional summaries, statistical-test outputs, network-centrality tables, umbrella co-occurrence tables, and the PDF/PNG figures are deposited in the project repository at <https://github.com/ali-kin4/quranic-emotion-spectrum>, together with the SHA-256 hash of the source file and the manual-validation audit. The primary sources are the Quranic Arabic Corpus v0.4 (Dukes 2011), released under the GNU General Public License, and the Tanzil Quran text (Uthmani edition; Tanzil Project 2008), released under CC-BY-ND 3.0. The four statistical analyses can be regenerated end-to-end by `pip install -r analysis/requirements.txt` followed by `python analysis/extract_concordance.py`, `python analysis/advanced_metrics.py`, `python analysis/visualize_spectrum.py`, and `python analysis/visualize_advanced.py`. The four computational corroboration analyses (Supplementary S1–S4) are produced by `nlp_upgrade_colab.py`, with CSV outputs committed under `outputs/nlp_upgrade/` for inspection without re-running the GPU pipeline.

## Acknowledgments

The authors thank Kais Dukes (in memoriam) and the team behind the Quranic Arabic Corpus, and the Tanzil Project, for releasing the morphological and textual resources without which this kind of empirical Qur'anic analysis would not be feasible. The authors also thank Urmia University for institutional support.

## Conflicts of Interest

The authors declare no conflicts of interest.

---

## References

Agresti, Alan. 2013. *Categorical Data Analysis*, 3rd ed. Hoboken, NJ: John Wiley & Sons.

Akra, Diyam, Tymaa Hammouda, and Mustafa Jarrar. 2025. "QuranMorph: Morphologically Annotated Quranic Corpus." arXiv:2506.18148. https://arxiv.org/abs/2506.18148.

Albayrak, Ismail. 2020. "Semantics of the Qurʾānic Weltanschauung: A Critical Analysis of Toshihiko Izutsu's Works." *American Journal of Islam and Society* 37 (1–2): 1–28.

Averill, James R. 1982. *Anger and Aggression: An Essay on Emotion*. New York: Springer-Verlag.

Berkowitz, Leonard. 1993. *Aggression: Its Causes, Consequences, and Control*. New York: McGraw-Hill.

Bodi, Daniel. 2018. "An Akkadian-Aramaic Idiomatic Expression in Ezekiel 16:30 *amūlâ libbātēk* 'I am filled with anger against you', and Remarks on the Languages in Persian Times." *Transeuphratène* 50: 13–38.

Cairns, Douglas L. 2003. "Ethics, Ethology, Terminology: Iliadic Anger and the Cross-cultural Study of Emotion." In *Ancient Anger: Perspectives from Homer to Galen*, edited by Susanna Braund and Glenn W. Most, 11–49. Yale Classical Studies 32. Cambridge: Cambridge University Press.

*Chicago Assyrian Dictionary (CAD)*. 1956–2010. Edited by Martha T. Roth et al. 21 vols. Chicago: The Oriental Institute.

Cochran, William G. 1954. "Some Methods for Strengthening the Common χ² Tests." *Biometrics* 10 (4): 417–51.

Derki, Mohamed. 2022. "Conceptualization of Anger in Modern Standard Arabic and English: A Comparative Study." *Professional Discourse and Communication* 4 (3): 24–39.

Dukes, Kais. 2011. *Quranic Arabic Corpus (Morphology, Version 0.4)*. Leeds: University of Leeds. https://corpus.quran.com.

El-Awa, Salwa M. S. 2006. *Textual Relations in the Qurʾan: Relevance, Coherence and Structure*. Routledge Studies in the Qurʾan. London and New York: Routledge.

Fauconnier, Gilles, and Mark Turner. 2002. *The Way We Think: Conceptual Blending and the Mind's Hidden Complexities*. New York: Basic Books.

al-Fīrūzābādī, Muḥammad ibn Yaʿqūb. n.d. *al-Qāmūs al-Muḥīṭ*. Beirut: Muʾassasat al-Risālah.

Fisher, Ronald A. 1922. "On the Interpretation of χ² from Contingency Tables, and the Calculation of *P*." *Journal of the Royal Statistical Society* 85 (1): 87–94.

Frijda, Nico H. 1986. *The Emotions*. Studies in Emotion and Social Interaction. Cambridge and Paris: Cambridge University Press and Éditions de la Maison des Sciences de l'Homme.

Gaanoun, Kamel, and Mohammed Alsuhaibani. 2025. "Sentiment Preservation in Quran Translation with Artificial Intelligence Approach: Study in Reputable English Translation of the Quran." *Humanities and Social Sciences Communications* 12 (1): 1–12. https://doi.org/10.1057/s41599-024-04181-0.

Grady, Joseph E. 1997. "Foundations of Meaning: Primary Metaphors and Primary Scenes." PhD diss., University of California, Berkeley.

Gross, James J. 1998. "The Emerging Field of Emotion Regulation: An Integrative Review." *Review of General Psychology* 2 (3): 271–99.

Gross, James J., ed. 2014. *Handbook of Emotion Regulation*, 2nd ed. New York: Guilford Press.

Gross, James J. 2015. "Emotion Regulation: Current Status and Future Prospects." *Psychological Inquiry* 26 (1): 1–26.

Ibn ʿĀshūr, Muḥammad al-Ṭāhir. 1984. *al-Taḥrīr wa-l-Tanwīr*. Tunis: al-Dār al-Tūnisiyyah li-l-Nashr.

Ibn Fāris, Aḥmad. 1979. *Muʿjam Maqāyīs al-Lughah*. Edited by ʿAbd al-Salām M. Hārūn. Beirut: Dār al-Fikr.

Ibn Kathīr, Ismāʿīl. 1999. *Tafsīr al-Qurʾān al-ʿAẓīm*. Edited by Sāmī al-Salāmah. 8 vols. Riyadh: Dār Ṭaybah.

Ibn Manẓūr, Muḥammad. 1993. *Lisān al-ʿArab*, 3rd ed. Beirut: Dār Ṣādir.

Izutsu, Toshihiko. 1959. *The Structure of the Ethical Terms in the Koran: A Study in Semantics*. Studies in the Humanities and Social Relations 2. Tokyo: Keio Institute of Philological Studies.

Izutsu, Toshihiko. 1964. *God and Man in the Koran: Semantics of the Koranic Weltanschauung*. Tokyo: Keio Institute of Cultural and Linguistic Studies.

Izutsu, Toshihiko. 2002. *Ethico-Religious Concepts in the Qurʾān*, rev. ed. Montreal: McGill-Queen's University Press. First published 1966.

Jamison, Stephanie W., and Joel P. Brereton. 2014. *The Rigveda: The Earliest Religious Poetry of India*. 3 vols. New York: Oxford University Press.

Kassinove, Howard, and Raymond C. Tafrate. 2002. *Anger Management: The Complete Treatment Guidebook for Practitioners*. Atascadero, CA: Impact Publishers.

Kennedy, Christopher. 1999. *Projecting the Adjective: The Syntax and Semantics of Gradability and Comparison*. Outstanding Dissertations in Linguistics. New York: Garland.

Kennedy, Christopher. 2007. "Vagueness and Grammar: The Semantics of Relative and Absolute Gradable Adjectives." *Linguistics and Philosophy* 30 (1): 1–45.

Khan, Muhammad T., Sara Qayyum, Imran Razzak, and Muhammad Imran. 2025. "A Literature Review on Natural Language Processing Techniques for Qurʾānic Studies: Challenges and Insights." *Frontiers in Signal Processing* 5: 1535166. https://doi.org/10.3389/frsip.2025.1535166.

Kövecses, Zoltán. 1986. *Metaphors of Anger, Pride, and Love: A Lexical Approach to the Structure of Concepts*. Pragmatics & Beyond VII:8. Amsterdam: John Benjamins.

Kövecses, Zoltán. 2000. *Metaphor and Emotion: Language, Culture, and Body in Human Feeling*. Cambridge: Cambridge University Press.

Kövecses, Zoltán. 2010. *Metaphor: A Practical Introduction*, 2nd ed. Oxford: Oxford University Press.

Kövecses, Zoltán. 2020. *Extended Conceptual Metaphor Theory*. Cambridge: Cambridge University Press.

Kövecses, Zoltán, Réka Benczes, and Veronika Szelid, eds. 2025. *Metaphors of ANGER across Languages: Universality and Variation*. 2 vols. Comparative Handbooks of Linguistics 8. Berlin and Boston: De Gruyter Mouton.

Kruger, Paul A. 2000. "A Cognitive Interpretation of the Emotion of Anger in the Hebrew Bible." *Journal of Northwest Semitic Languages* 26 (1): 181–93.

Kruger, Paul A. 2015. "Emotions in the Hebrew Bible: A Few Observations on Prospects and Challenges." *Old Testament Essays* 28 (2): 395–420.

Lakoff, George, and Mark Johnson. 1980. *Metaphors We Live By*. Chicago: University of Chicago Press.

Lakoff, George, and Zoltán Kövecses. 1987. "The Cognitive Model of Anger Inherent in American English." In *Cultural Models in Language and Thought*, edited by Dorothy Holland and Naomi Quinn, 195–221. Cambridge: Cambridge University Press.

Landis, J. Richard, and Gary G. Koch. 1977. "The Measurement of Observer Agreement for Categorical Data." *Biometrics* 33 (1): 159–74.

Lauri, Jonas, Saana Svärd, Tero Alstola, Heidi Jauhiainen, Aleksi Sahala, Krister Lindén, Mikko Sams, and Lauri Nummenmaa. 2024. "Embodied Emotions in Ancient Neo-Assyrian Texts Revealed by Bodily Mapping of Emotional Semantics." *iScience* 27 (12): 111365.

Lazarus, Richard S. 1991. *Emotion and Adaptation*. New York: Oxford University Press.

Maalej, Zouheir. 2004. "Figurative Language in Anger Expressions in Tunisian Arabic: An Extended View of Embodiment." *Metaphor and Symbol* 19 (1): 51–75.

Maalej, Zouheir. 2007. "The Embodiment of Fear Expressions in Tunisian Arabic: Theoretical and Practical Implications." In *Applied Cultural Linguistics: Implications for Second Language Learning and Intercultural Communication*, edited by Farzad Sharifian and Gary B. Palmer, 87–104. Converging Evidence in Language and Communication Research 7. Amsterdam: John Benjamins.

Maalej, Zouheir A., and Ning Yu, eds. 2011. *Embodiment via Body Parts: Studies from Various Languages and Cultures*. Human Cognitive Processing 31. Amsterdam and Philadelphia: John Benjamins.

Marcus-Newhall, Amy, William C. Pedersen, Mike Carlson, and Norman Miller. 2000. "Displaced Aggression is Alive and Well: A Meta-analytic Review." *Journal of Personality and Social Psychology* 78 (4): 670–89.

Mehta, Cyrus R., and Nitin R. Patel. 1983. "A Network Algorithm for Performing Fisher's Exact Test in *r* × *c* Contingency Tables." *Journal of the American Statistical Association* 78 (382): 427–34.

al-Mostafawī, Ḥasan. 1995. *al-Taḥqīq fī Kalimāt al-Qurʾān al-Karīm*. 14 vols. Tehran: Wizārat al-Thaqāfah wa-l-Irshād al-Islāmī.

Mottaghi, Mohammad S., Mahdi Bohlouli, and Mohammad R. Razzazi. 2024. "A Graph-based Algorithm for Clustering Qurʾānic Surahs." *Signal and Data Processing Journal* 21 (2): 45–60.

Muellner, Leonard C. 1996. *The Anger of Achilles: Mēnis in Greek Epic*. Ithaca, NY: Cornell University Press.

Nandan, Mahesh, Ishan Godbole, Pranav Kapparad, and Sourjyadip Bhattacharjee. 2025. "Comparative Analysis of Religious Texts: NLP Approaches to the Bible, Quran, and Bhagavad Gītā." In *Proceedings of the Workshop on New Horizons in Computational Linguistics for Religious Texts (CLRel)*. Stroudsburg, PA: Association for Computational Linguistics.

Narimani, Zahra, Masoud Iqbali, and Mostafa Chari. 2021. "Semantic Re-analysis of the Words *ghayẓ*, *ghaḍab*, and *sakhaṭ* in the Holy Qurʾān with an Exegetical Approach" [in Persian]. *Pizhūhish-hā-yi Qurʾān va Ḥadīth* 54 (1): 219–39.

Neuwirth, Angelika. 2019. *The Qur'an and Late Antiquity: A Shared Heritage*. Translated by Samuel Wilder. Oxford: Oxford University Press.

Pakatchi, Ahmad, and Azita Afrashi. 2020. *Rūykardhā-yi Maʿnā-shinākhtī dar Muṭālaʿāt-i Qurʾānī* [Semantic Approaches in Qurʾānic Studies; in Persian]. Tehran: Pizhūhishgāh-i ʿUlūm-i Insānī va Muṭālaʿāt-i Farhangī.

Patefield, William M. 1981. "Algorithm AS 159: An Efficient Method of Generating Random *R* × *C* Tables with Given Row and Column Totals." *Journal of the Royal Statistical Society, Series C (Applied Statistics)* 30 (1): 91–97.

Plutchik, Robert. 1980. *Emotion: A Psychoevolutionary Synthesis*. New York: Harper & Row.

Plutchik, Robert. 2001. "The Nature of Emotions." *American Scientist* 89 (4): 344–50.

Qāʾimīniyā, ʿAlī Riḍā. 2011. *Maʿnāshināsī-yi Shinākhtī-yi Qurʾān* [Cognitive Semantics of the Qurʾān; in Persian]. Tehran: Pizhūhishgāh-i Farhang va Andīshah-i Islāmī.

Qāʾimīniyā, ʿAlī Riḍā. 2014. *Istiʿārah-hā-yi Mafhūmī wa Faḍāhā-yi Qurʾānī* [Conceptual Metaphors and Qurʾānic Spaces; in Persian]. Tehran: Pizhūhishgāh-i Farhang va Andīshah-i Islāmī.

Qarizadeh, Muḥammad ʿO., Muḥammad ʿA. Salmani Marvast, Vāḥid Meymandi, and Bīžan Farsi. 2024. "Polysemy of the Word *ṭughyān* in the Holy Qurʾān with a Linguistic Approach" [in Persian]. *Pizhūhish-hā-yi Zabānshinākhtī-yi Qurʾān* 13 (1): 1–22.

al-Qurṭubī, Muḥammad ibn Aḥmad. 1964. *al-Jāmiʿ li-Aḥkām al-Qurʾān*. 20 vols. Cairo: Dār al-Kutub al-Miṣriyyah.

al-Qushayrī, ʿAbd al-Karīm. 2000. *Laṭāʾif al-Ishārāt*. Edited by Ibrāhīm Basyūnī. 6 vols. Cairo: al-Hayʾah al-Miṣriyyah al-ʿĀmmah li-l-Kitāb.

Quṭb, Sayyid. 1980. *Fī Ẓilāl al-Qurʾān*. 6 vols. Cairo and Beirut: Dār al-Shurūq.

Rabab'ah, Khalid, and Emad Al-Saidat. 2022. "The Conceptualization of Anger through Metaphors, Metonymies and Metaphtonymies in Jordanian Arabic and English: A Contrastive Study." *Cognitive Semantics* 8 (3): 409–33.

al-Rāghib al-Iṣfahānī, Ḥusayn. 1992. *al-Mufradāt fī Gharīb al-Qurʾān*. Edited by Ṣafwān ʿA. Dāwūdī. Damascus and Beirut: Dār al-Qalam and al-Dār al-Shāmiyyah.

al-Rāzī, Fakhr al-Dīn Muḥammad. 1999. *Mafātīḥ al-Ghayb (al-Tafsīr al-Kabīr)*. Beirut: Dār Iḥyāʾ al-Turāth al-ʿArabī.

Riḍā, Muḥammad Rashīd. 1947. *Tafsīr al-Qurʾān al-Ḥakīm (al-Manār)*. 12 vols. Cairo: Dār al-Manār.

Roseman, Ira J. 1996. "Appraisal Determinants of Emotions: Constructing a More Accurate and Comprehensive Theory." *Cognition and Emotion* 10 (3): 241–77.

Sadeghi, Behnam. 2011. "The Chronology of the Qurʾān: A Stylometric Research Program." *Arabica* 58 (3–4): 210–99.

Sassoon, Galit W. 2010. "The Degree Functions of Negative Adjectives." *Natural Language Semantics* 18 (2): 141–81.

Sawalha, Majdi, Faisal Al-Shargi, Sane Yagi, Abdallah T. AlShdaifat, Bassam Hammo, Manar Belajeed, and Luay R. Al-Ogaili. 2024. "Morphologically-Analyzed and Syntactically-Annotated Quran Dataset (MASAQ)." *Data in Brief* 58: 111211.

Scherer, Klaus R. 2001. "Appraisal Considered as a Process of Multilevel Sequential Checking." In *Appraisal Processes in Emotion: Theory, Methods, Research*, edited by Klaus R. Scherer, Angela Schorr, and Tom Johnstone, 92–120. New York: Oxford University Press.

Scherer, Klaus R. 2005. "What Are Emotions? And How Can They Be Measured?" *Social Science Information* 44 (4): 695–729.

Sharaf, Abdul-Baquee M., and Eric Atwell. 2012a. "QurAna: Corpus of the Quran Annotated with Pronominal Anaphora." In *Proceedings of the Eighth International Conference on Language Resources and Evaluation (LREC'12)*, 130–37. Istanbul: ELRA.

Sharaf, Abdul-Baquee M., and Eric Atwell. 2012b. "QurSim: A Corpus for Evaluation of Relatedness in Short Texts." In *Proceedings of the Eighth International Conference on Language Resources and Evaluation (LREC'12)*, 2295–2302. Istanbul: ELRA.

Sharifian, Farzad. 2011. *Cultural Conceptualisations and Language: Theoretical Framework and Applications*. Cognitive Linguistic Studies in Cultural Contexts 1. Amsterdam: John Benjamins.

Sinai, Nicolai. 2017. *The Qurʾan: A Historical-Critical Introduction*. The New Edinburgh Islamic Surveys. Edinburgh: Edinburgh University Press.

Sinai, Nicolai. 2023. *Key Terms of the Qurʾan: A Critical Dictionary*. Princeton: Princeton University Press.

Soriano, Cristina. 2003. "Some Anger Metaphors in Spanish and English: A Contrastive Review." *International Journal of English Studies* 3 (2): 107–22.

Soriano, Cristina. 2013. "Anger Metaphors across Languages: A Cognitive Linguistic Perspective." In *Bilingual Figurative Language Processing*, edited by Roberto R. Heredia and Anna B. Cieślicka, 410–40. Cambridge: Cambridge University Press.

Spielberger, Charles D. 1999. *Professional Manual for the State-Trait Anger Expression Inventory–2 (STAXI-2)*. Odessa, FL: Psychological Assessment Resources.

al-Ṭabarī, Muḥammad ibn Jarīr. 2000. *Jāmiʿ al-Bayān ʿan Taʾwīl Āy al-Qurʾān*. Edited by Aḥmad M. Shākir. 24 vols. Beirut: Muʾassasat al-Risālah.

al-Ṭabarsī, al-Faḍl ibn al-Ḥasan. n.d. *Majmaʿ al-Bayān fī Tafsīr al-Qurʾān*. Beirut: Dār al-Maʿrifah.

al-Ṭabāṭabāʾī, Muḥammad Ḥusayn. 1970. *al-Mīzān fī Tafsīr al-Qurʾān*. 20 vols. Beirut: Muʾassasat al-Aʿlamī li-l-Maṭbūʿāt.

Tanzil Project. 2008. *The Tanzil Quran Text (Uthmani Edition)*. https://tanzil.net.

Webb, Peter. 2016. *Imagining the Arabs: Arab Identity and the Rise of Islam*. Edinburgh: Edinburgh University Press.

Wierzbicka, Anna. 1999. *Emotions Across Languages and Cultures: Diversity and Universals*. Cambridge: Cambridge University Press.

Yu, Ning. 1995. "Metaphorical Expressions of Anger and Happiness in English and Chinese." *Metaphor and Symbolic Activity* 10 (2): 59–92.

al-Zamakhsharī, Maḥmūd. 1986. *al-Kashshāf ʿan Ḥaqāʾiq Ghawāmiḍ al-Tanzīl*. Beirut: Dār al-Kitāb al-ʿArabī.
