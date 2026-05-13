# The Phenomenology of the Anger Spectrum in the Qur'an
## A Semantic-Network Analysis of Displeasure, Inflammation, and Destructiveness Along an Action-Intensity Continuum

**Karim Jabbary** *(corresponding author)*
Department of Arabic Language and Literature, Faculty of Literature and Humanities, Urmia University, Urmia, Iran. *email:* k.jabbary@urmia.ac.ir.

**Ali Jabbary**
Faculty of Computer Engineering, Urmia University, Urmia, Iran. *email:* a.jabbary@urmia.ac.ir.

Karim Jabbary: ORCID 0000-0000-0000-0000 (to be provided at submission)
Ali Jabbary: ORCID 0000-0000-0000-0000 (to be provided at submission)

---

## Abstract

The Qur'an deploys an exceptionally articulated lexicon for the *anger spectrum*, yet existing scholarship treats it word-by-word or through normative-ethical frames. This study argues that fourteen core Arabic roots (*ʾff, krh, ḍyq, ḥzn, ʾsf, nqm, sxṭ, mqt, ġḍb, ḥrd, ġyẓ, bġy, ṭġy, ʿtw*) form a graded semantic field organised by *intensity of action* across six phenomenological stages: pre-anger displeasure, inner pressure, evaluative aversion, active anger, compressed rage, and behavioural outcomes. Integrating Izutsu's semantic-field approach, Kennedy–Sassoon scalar semantics, and Lakoff–Kövecses conceptual metaphor theory, we validate the continuum against the Quranic Arabic Corpus through a reproducible Python pipeline over 312 attestations. Three findings emerge under uncertainty-aware metrics. First, the asymptotic χ²(5) = 227.15 is large but a marginal-preserving permutation null yields *p* = 0.24; the omnibus is *consistent with* rather than confirmatory of non-uniformity. Second, three roots survive Holm-Bonferroni correction over the family of fourteen per-root binomials: *karh* (Medinan-tilted, adj. *p* ≈ 10⁻⁶), *baghy* (Meccan-tilted, adj. *p* ≈ 5 × 10⁻³), and *ghayẓ* (Medinan-tilted, adj. *p* ≈ 2 × 10⁻²); *sakhaṭ* (exclusively Medinan) sits at adj. *p* = 0.05, just below the conventional threshold. The pattern instantiates *discursive-contextual lexical specialisation*. Third, network analysis identifies *baghy* as a bridging node to the broader moral-evaluation field; Q. 67:8 of sūrat al-Mulk (*takādu tamayyazu min al-ġayẓ*) is an unusually transparent instance of "container collapse"; a κ = 0.79-validated *tafsīr* audit supports a *bidirectional-causation* reading of Stage 6 (A = 26%, S = 49%, A+S = 25%). Implications follow, conditionally, for Qur'anic translation and Islamic psychology.

**Keywords:** Qur'an; anger spectrum; semantic field; cognitive linguistics; scalar semantics; conceptual metaphor; corpus linguistics.

---

## 1. Introduction

### 1.1. Statement of the problem

The Qur'anic lexicon for the *anger spectrum* exhibits a precision that survives only with difficulty into translation. Where English versions level *uff*, *karh*, *ḍīq*, *ḥuzn*, *asaf*, *naqm*, *sakhaṭ*, *maqt*, *ghaḍab*, *ḥard*, *ghayẓ*, *baghy*, *ṭughyān*, and *ʿutuww* into a small set of broad equivalents — "displeasure," "distress," "grief," "anger," "rage," "transgression," "rebellion" — the Arabic original distinguishes them with the precision of a graded taxonomy. We advance the hypothesis that these fourteen roots are not synonyms but coordinated nodes in a single *graded* semantic field, organised along *intensity of action*, traversing pre-anger displeasure, inner pressure and contraction, evaluative aversion, active anger, compressed/explosive rage, and — at the behavioural pole — outcomes (*baghy*, *ṭughyān*, *ʿutuww*) whose causation is bidirectional rather than purely emotional.

This claim has consequences beyond philology: the Qur'an encodes — through its lexical architecture, not by explicit theoretical statement — an implicit theory of the genealogy of moral failure, in which the social-structural pathologies the text most frequently denounces (transgression, tyranny, defiance) are *related to* and often developmentally downstream from inner experiences of irritation, dislike, constriction, and grief. As we argue in §4–§5, the relationship at the behavioural pole is *bidirectional*: anger may produce *baghy*/*ṭughyān*/*ʿutuww*, but these behaviours can equally produce anger in their victims, the prophets, and the divine response. The distance from *uff* (sūrat al-Isrāʾ, Q. 17:23) to *ʿutuww* (sūrat al-Furqān, Q. 25:21) is graded rather than categorical.

### 1.2. Aims and originality

This paper has three aims. The first is **methodological**: to demonstrate that combining Izutsu's semantic-field approach (Izutsu 1959, 1964, 2002), scalar-semantic ordering in the Kennedy–Sassoon tradition (Kennedy 1999, 2007; Sassoon 2010), and conceptual-metaphor theory in the Lakoff–Kövecses tradition (Lakoff and Johnson 1980; Lakoff and Kövecses 1987; Kövecses 2000, 2010) produces stronger philological claims than any of the three frameworks in isolation. Izutsu's field method yields a network of mutually defining lexemes around focus words but does not generate an ordering relation *within* the network; Lakoff and Kövecses (1987) supply a cognitive-metaphor schema anchored lexicographically in *English*, and the two-volume *Metaphors of ANGER across Languages* (Kövecses, Benczes and Szelid 2025) — twenty-two languages from Mandarin to Yoruba — *omits Classical Arabic entirely*. Kennedy–Sassoon orders predicates along a dimension and a unit but has not been applied to a Qur'anic emotion field. Qāʾimīniyā (2011, 2014) and Pakatchi and Afrashi (2020) already integrate Izutsu with CMT in Persian; the *novel* element here is the Kennedy–Sassoon scalar layer operationalised as a six-stage action-intensity continuum tested against a 312-attestation reproducible pipeline, alongside (i) a κ = 0.79-validated *tafsīr*-coding audit of the bidirectional-causation reading of Stage 6, (ii) the *kaẓm*-as-tying-off-of-waterskin analysis of agent-internal containment, and (iii) the framing of Q. 67:8 of sūrat al-Mulk as an early and unusually transparent lexicalisation of "container collapse", calibrated against a six-tradition philological survey (§5.5) that acknowledges Job 32:19 (*bāqaʿ*) as the one clear Northwest-Semitic precedent. The second aim is **descriptive**: to map every Qur'anic occurrence of the fourteen core roots, render that map publicly verifiable, and extract empirical regularities previous scholarship was not in a position to detect. The third aim is **interpretive**: to argue that the continuum constitutes a coherent logic of anger escalation with structural affinities to modern emotion psychology, and to identify the points at which it *exceeds* the contemporary models — most pointedly at Stage 6, where *baghy*/*ṭughyān*/*ʿutuww* extend the regulatory horizon of Gross's process model into the moral-anthropological register.

### 1.3. Prior work and the gap

Prior scholarship clusters into five lines, each insufficient on its own. **Single-word lexical studies**: the most directly relevant Persian-language precedent — Narimani, Iqbali and Chari (2021) on *ghayẓ*, *ghaḍab*, and *sakhaṭ* — establishes on *tafsīr* grounds that *ghaḍab* is central, *sakhaṭ* reserved for divine displeasure with hypocrites, and *ghayẓ* predominantly (not exclusively) attributed in human-reference contexts to unbelievers/hypocrites. Q. 3:134 of sūrat Āl ʿImrān (*al-kāẓimīn al-ġayẓ*) is the canonical exception, attributing the substance of *ghayẓ* — as the object of *kaẓm* — to believers themselves. Qarizadeh et al. (2024) on *ṭughyān* show the root attests in twenty-seven suras with the central meaning of transgressing the limit. Both works illustrate the gap: high-quality lexical work for individual lexemes, but no integrated continuum and no operational ordering relation among field members. **Semantic-field and cognitive-semantic studies** in the Izutsu tradition — Qāʾimīniyā (2011, 2014), Pakatchi and Afrashi (2020), Albayrak (2020) — have applied cognitive linguistics to Qur'anic vocabulary, but the *graded continuum* layer remains untreated. Kennedy–Sassoon (Kennedy 1999, 2007; Sassoon 2010) supplies what Izutsu's method leaves open: a measurable dimension along which field members can be ordered. **Ethics-of-anger studies** in the *kaẓm al-ghayẓ* tradition are normatively rich and linguistically thin. **The cross-linguistic CMT literature** has been decisively updated by Kövecses, Benczes and Szelid (2025), which canvasses twenty-two language traditions — *Classical Arabic is not separately treated*, and the Qur'anic *ghayẓ–kaẓm–tamayyuz* triad is absent from the encyclopedia. The closest Arabic-CMT precedents are Maalej (2004, 2007) on Tunisian Arabic and Rabab'ah and Al-Saidat (2022) on Jordanian Arabic, both contemporary-dialect studies neither addressing the Qur'anic data. **Historical-critical and corpus-linguistic studies** supply complementary apparatus: Sinai (2017) articulates the revised Meccan/Medinan periodisation underwriting our *sakhaṭ* and *karh* findings and his *Key Terms* (Sinai 2023) models the lexicon-level entry organisation we extend at the field level; Neuwirth (2019) frames Qur'anic form and diction as a dialogical intervention into the late-antique discursive sphere, supplying the rhetorical-form vocabulary at which §5.4 operates. El-Awa (2006) supplies the relevance-theoretic vocabulary; Sharaf and Atwell (2012a, 2012b) established Qur'anic-NLP reproducibility standards alongside QuranMorph (Akra, Hammouda and Jarrar 2025) and MASAQ (Sawalha et al. 2024). **Translation-criticism studies** are now quantitative at scale: Gaanoun and Alsuhaibani (2025) show inconsistent sentiment polarity across seven English translations, and Khan et al. (2025) survey the field; none supplies a graded *lexeme-level* reference model against which translation-levelling could be benchmarked. **Islamic psychology** tends to draw on *aḥādīth* and leave systematic linguistic analysis of the Qur'anic surface in the background. The present paper occupies the unfilled intersection of all five lines: it adds the Kennedy–Sassoon scalar layer to the Izutsu / CMT stack, applies it to the anger field that the 2025 *Metaphors of ANGER* encyclopedia omits, and releases the empirical pipeline under the Sharaf–Atwell / QuranMorph reproducibility standard.

### 1.4. Research questions and hypotheses

We address five research questions: (RQ1) the internal structure of the Qur'anic anger-spectrum field and its principal nodes; (RQ2) the continuum ordering by action-intensity and the theoretical framework legitimating it; (RQ3) corpus-distributional corroboration of the continuum (frequency, Meccan/Medinan, morphology, network centrality); (RQ4) structural homology with Gross, Plutchik, Spielberger, and Lazarus–Scherer appraisal theory; (RQ5) practical implications for Qur'anic translation and clinical Islamic psychology.

The principal **Qur'anic Action-Intensity Continuum Hypothesis** holds that the fourteen core roots operate as fourteen distinct grades on a single semantic continuum structured by *intensity of action*, organised in six phenomenological stages, supported by qualitative (etymological, exegetical, metaphorical) and quantitative (frequency, distribution, network) evidence. Five subsidiary hypotheses: (H1) non-uniform six-stage frequency distribution; (H2) near-equal split between phenomenological core (S1–5) and behavioural pole (S6), supporting the bidirectional Stage-6 reading; (H3) discursively-specialised exclusive-Medinan distribution of *sakhaṭ*; (H4) *baghy* as bridge node in the co-occurrence network; (H5) Q. 67:8 of sūrat al-Mulk as transparent instance of "container collapse" CMT failure mode.

---

## 2. Theoretical Framework

### 2.1. Izutsu's semantic-field method

Toshihiko Izutsu (1959, 1964, 2002) introduced a methodological revolution to Qur'anic studies. Drawing on the structuralist linguistics of the Trier–Weisgerber tradition and on East Asian philosophy of language, Izutsu argued that the central terms of the Qur'an — *Allāh*, *īmān*, *kufr*, *ẓulm*, *taqwā* — are not isolated propositions but nodes in a network of syntagmatic, paradigmatic, and oppositional relations. The aggregate constitutes what he called the "Qur'anic *Weltanschauung*."

Izutsu distinguishes three layers: *focus words* (central organising concepts of a semantic field), *semantic fields* (networks of mutually defining lexemes around focus words), and *key words* (terms recurring across fields and integrating them into a worldview). The structure has proved productive in subsequent Qur'anic semantic work, in English (Saleh, Rippin) and Persian (Qāʾimīniyā 2011, 2014; Pakatchi and Afrashi 2020).

Izutsu's framework justifies the move from atomistic single-lexeme analysis to integrated field analysis. The fourteen target roots constitute the field around the focus words *ghaḍab* (central anger term) and *baghy* (central behavioural-outcome term), with the lower-intensity cluster (*uff*, *karh*, *ḍīq*, *ḥuzn*, *asaf*) identifying the pre-anger and inner-pressure boundary and *ʿutuww* the upper-intensity boundary. Yet Izutsu's framework is silent on a question central to our enterprise: granted these lexemes co-belong to a field, *what is the structural relation between them within the field?* For this we require scalar semantics.

### 2.2. Scalar semantics: from network to continuum

The theory of *gradable predicates* (Kennedy 1999, 2007; Sassoon 2010) supplies the missing apparatus. A graded predicate maps to a scale with three components: a *dimension* of measurement, an *ordering* on that dimension, and a unit of comparison. Scalar predicates take degree modifiers and admit comparative constructions. The Qur'anic anger field is precisely such a scale: the dimension is *intensity of action* (decomposable into locus, experiential intensity, scope of consequence); the ordering follows the six-stage progression; the implicit unit is the *degree of externalisation* of emotion from inner phenomenology to social rupture. Without this framework, the claim that *ghayẓ* is "more intense than" *ghaḍab* relies on tacit native-speaker intuition. Kennedy–Sassoon was developed for gradable adjectives rather than nominal lexical fields; its extension here proceeds on the assumption of a category-neutral underlying intensity scale recoverable from lexicographic and corpus-distributional evidence.

### 2.3. Conceptual metaphor theory and the container schema

Conceptual metaphor theory (Lakoff and Johnson 1980; Lakoff and Kövecses 1987; Kövecses 2000, 2010) treats metaphor as a cognitive structure that allows abstract domains (emotion) to be understood through concrete ones (container, heat). Lakoff and Kövecses (1987: 195–221) reconstruct American-English anger as a *five-stage prototype scenario* — (1) offending event, (2) anger, (3) attempt at control, (4) loss of control, (5) act of retribution — onto which the central metaphors ANGER IS THE HEAT OF A FLUID IN A PRESSURIZED CONTAINER, ANGER IS FIRE, and ANGER IS A WILD ANIMAL are mapped, with the container / pressure cluster operating especially in stages (2)–(4). Our central observation is that the Qur'anic triad *ghayẓ–kaẓm–tamayyuz* maps tightly onto stages (2)–(4) of that scenario — anger, attempt at control, and (incipient) loss of control — with sūrat al-Mulk Q. 67:8's *takādu tamayyazu min al-ġayẓ* providing a particularly transparent linguistic crystallisation of stage (4). *Ghayẓ* is glossed by all four authoritative lexica as compressed contained anger — the *cognitive-linguistic* reading takes this as the source-domain image of fluid in a sealed vessel. *Kaẓm*, etymologically tying off a waterskin, names the agent-internal act of suppression that sustains containment (sūrat Āl ʿImrān, Q. 3:134, *al-kāẓimīn al-ghayẓ*). *Tamayyuz* (sūrat al-Mulk, Q. 67:8) figures the failure mode: classical commentators read the verb as *yanqaṭiʿu baʿḍuhā min baʿḍ* (al-Ṭabarī, *Jāmiʿ al-bayān*, ad loc.; al-Zamakhsharī, *al-Kashshāf*, ad loc.) — the separation of constituents — and the cognitive-metaphor framing we propose reads this lexicographic "separation" as the linguistic surface of an underlying CONTAINER-RUPTURE schema. Both readings are compatible. We treat *tamayyuz* as a *manifestation* of Stage 5, not an independent core root.

### 2.4. The integrated framework

The three layers operate complementarily: Izutsu identifies field boundaries; scalar semantics orders members along the action-intensity dimension; CMT grounds the pressurisation-collapse metaphor organising Stage 5. Each supplies what the others lack — without Izutsu, no motivation for field-coordination; without scalar semantics, no apparatus for ordering; without CMT, no cognitive grounding for the *kaẓm–tamayyuz* sequence.

---


![**Figure 1.** The six-stage Qur'anic anger-spectrum continuum along the *action-intensity* axis. Node area scales with QAC attestation frequency. Stages: S1 pre-anger displeasure (*ʾff–krh*); S2 inner pressure (*ḍyq–ḥzn–ʾsf*); S3 evaluative aversion (*nqm–sxṭ–mqt*); S4 active anger (*ġḍb–ḥrd*); S5 compressed/explosive rage (*ġyẓ*; *tamayyuz* as manifestation); S6 behavioural outcomes (*bġy–ṭġy–ʿtw*) — causation *bidirectional* rather than purely downstream (§4.8.5). Mass at S6 (n = 145) ≈ S1–5 (n = 167); the χ²(1) = 1.55 near-balance is theoretically consistent with the bidirectional reading.](fig1_continuum_v2.jpg){width=100%}

The integrated framework is summarised graphically in Figure 1.

## 3. Methods

### 3.1. Corpus

The empirical analysis uses the **Quranic Arabic Corpus** (QAC), version 0.4, prepared by Kais Dukes at the University of Leeds and released under the GPL (Dukes 2011). The QAC provides a morphologically tagged record for each of the 128,219 segmentable units in the Qur'anic text, specifying location *(sūra:āya:word:segment)*, surface form in Buckwalter ASCII transliteration, part-of-speech tag, and morphological features (root, lemma, gender, number, case, and where applicable semantic flags). Verse text in Uthmanic *rasm* and Meccan/Medinan sura classification are drawn from the Tanzil project (Tanzil 2008), distributed under CC-BY-ND 3.0.

### 3.2. Selection of target roots

The fourteen core roots were selected by three concurrent criteria: (i) *exegetical centrality* — appearance as a focal reference in at least three of the four authoritative lexica (Ibn Fāris's *Maqāyīs*, al-Rāghib's *Mufradāt*, Ibn Manẓūr's *Lisān*, and Mostafavi's twentieth-century *Taḥqīq*); (ii) *minimum corpus frequency* of one attestation, admitting Qur'anic hapax legomena (*ḥard*, sūrat al-Qalam, Q. 68:25) when supported by an explicit gloss in at least three of the four lexica plus consistent treatment in the four canonical *tafāsīr* of §3.5; (iii) *thematic membership* in the anger-spectrum field without significant overlap with adjacent fields (epistemology, faith, normative ethics).

**Excluded candidate roots** (transparency): *q-h-r* (dominance/power, *al-Qahhār* divine name); *ḥ-n-q* (not attested in the Qurʾanic corpus); *ʿ-n-f* (adverbial harshness, not emotion); *ḍ-r-b* (polysemous, conflict-scene); *q-ṣ-w*/*q-s-y* (hardness-of-heart, epistemic-moral); *gh-l-ẓ* (adverbial harshness); *ʾ-n-f* (nominal *anf* "nose", post-Qur'anic anger sense); *š-n-ʾ* (binary loving/hating, reclassified as umbrella). *Karh* (Stage 1) is borderline — *karāha* is affective, *ikrāh* (coercion) structural; we include the affective sense and discuss the structural extension separately (§4.3.1). Five umbrella moral terms (**šnʾ, jrm, fsq, ẓlm, ʿdw**) are used for robustness (§4.9) and cross-field co-occurrence (Table 4), excluded from the principal continuum either because of inflated cardinality (*ẓlm* n = 315 functions as a meta-category) or because they belong to adjacent normative-ethics fields.

### 3.3. Computational pipeline

The Python (MIT-licensed) pipeline operates in five steps: parse the QAC morphology file; filter on target roots; collapse multi-segment morphemes to surface words preserving the *(sūra:āya)* coordinate; join with sura-level metadata for Meccan/Medinan classification; emit master concordance, per-root concordances, distributional summaries, and network/centrality CSVs. The complete analysis is reproducible from a fresh clone in four commands.

**Reproducibility audit.** QAC v0.4 is pinned by SHA-256; outputs are released under MIT (code) and CC-BY 4.0 (manuscripts/figures); the fourteen exemplar verses and a stratified fifty-segment audit on the four most frequent core roots (*ḥzn*, *bġy*, *ġḍb*, *ṭġy*) returned 100% correct segment-to-root assignment against Tanzil. Full audit at `data/concordance/validation_audit.md`.

![**Figure 8.** End-to-end pipeline from corpus to findings. Sources tier: QAC v0.4 (Dukes 2011, GPL), Tanzil Project Uthmani text (CC-BY-ND 3.0), and the nine classical *tafāsīr* whose qualitative readings ground §§4–5. Parse tier: Buckwalter → Unicode collapse, segment-to-word aggregation. Selection tier: the fourteen spectrum roots and the five umbrella-moral roots used for the robustness checks of §4.9. Analyses tier: distributional statistics, network analysis, *tafsīr*-grounded coding, and the illustrative comparative-translation audit. Outputs tier: 312 attestations across six stages, the principal figures and supporting CSV tables, and the Stage-6 causation breakdown. The pipeline is deterministic — identical inputs produce byte-identical CSVs and figures from a fresh repository clone.](fig8_methodology.jpg){width=95%}

The pipeline architecture is summarised in Figure 8.

### 3.4. Quantitative analyses

Quantitative tests beyond frequency tabulation: (a) χ²(5) and χ²(1) for uniform-stage and S1–5/S6 nulls, with Cramér's *V* and Cohen's *w*, plus a marginal-preserving permutation null (10,000 permutations, deterministic seed) for the omnibus, motivated by the well-known limitations of asymptotic χ² on sparse, marginally-imbalanced designs (Cochran 1954; Fisher 1922; Patefield 1981; Mehta and Patel 1983; Agresti 2013, §3.5);[^perm-note] (b) three monotonic-trend tests (Spearman ρ, Mann–Kendall, Cochran–Armitage-style OLS slope); (c) two-sided exact binomials with the corpus-derived 0.74 Meccan-ayat baseline, Holm–Bonferroni step-down adjusted over the family of fourteen per-root tests, and a sensitivity table at baselines 0.70–0.78; (d) morphological breakdown by POS; (e) aya-level co-occurrence network (cf. Mottaghi et al. 2024) with weighted degree, betweenness, closeness, and eigenvector centrality, with non-parametric bootstrap 95% percentile CIs (1,000 ayat-resamples with replacement). The combined uncertainty-aware reporting is, to our knowledge, the most rigorous yet applied to Qur'anic computational-corpus studies; the wider 2025 cross-scripture NLP literature (Nandan et al. 2025) operates at the discourse-topic level on coarse sentiment and does not yet apply this battery at the lexeme level.

[^perm-note]: The marginal-preserving permutation null holds the per-root attestation counts fixed and randomly permutes the fourteen stage labels across roots (10,000 permutations, fixed RNG seed 20260509); the empirical *p*-value is the fraction of permuted χ² values meeting or exceeding the observed 227.15. This is the natural extension of Fisher-exact reasoning to a many-cell design where exact enumeration of the conditional reference set is intractable (Patefield 1981; Mehta and Patel 1983).

### 3.5. Qualitative analyses

Qualitative complements operationalise Izutsu's three-layer apparatus at the field level: *focus-word* identification (exegetical-centrality across the four lexica → *ghaḍab*, with *baghy* as secondary focus word for the structural-outcomes pole, §4.8); *paradigmatic relations* — synonymy and gradation by intensity — across the fourteen roots via the lexicographic decomposition of Table 1 and the stage assignments of §§4.3–4.8; *syntagmatic contrasts* via the aya-level co-occurrence graph (§4.8.2) and the PMI-weighted network of Supplementary §S3. Specifically: (a) comparative etymology across the four authoritative lexica (*Maqāyīs*, *Mufradāt*, *Lisān*, *Taḥqīq*); (b) comparative *tafsīr* analysis on a broadened set of nine commentaries — the four primary (al-Ṭabāṭabāʾī's *al-Mīzān*, al-Zamakhsharī's *al-Kashshāf*, al-Ṭabarsī's *Majmaʿ al-Bayān*, Ibn ʿĀshūr's *al-Taḥrīr*) supplemented with al-Ṭabarī, al-Qurṭubī, Ibn Kathīr, Sayyid Quṭb, and ʿAbduh–Riḍā's *al-Manār*; for Sufi cross-checking on *kaẓm al-ghayẓ* (§4.7), al-Qushayrī's *Laṭāʾif al-Ishārāt*. Divergences from the primary four are recorded in §4 and corresponding claims qualified. (c) phenomenological analysis of contextual markers (*ḍīq al-ṣadr*, *ḥuzn al-qalb*, *asaf al-nafs*, *ḍāqa dharʿan*); (d) illustrative translation-criticism on five English translations (Yusuf Ali, Pickthall, Arberry, Saheeh International, Hilali-Khan) at canonical exemplar verses (§4.10) — illustrative rather than systematic.

### 3.6. Validity check

To verify the integrity of the pipeline, fourteen "headline" exemplar verses — one per core root — were independently verified against the corpus output: Q. 17:23 (*uff*); Q. 2:216 (*karh*); Q. 15:97 (*ḍyq*); Q. 2:38 (*ḥzn*); Q. 43:55 (*asaf*); Q. 7:126 (*naqm*); Q. 47:28 (*sakhaṭ*); Q. 40:10 (*maqt*); Q. 48:6 (*ghaḍab*); Q. 68:25 (*ḥard*); Q. 3:134 (*ghayẓ*; with manifestation Q. 67:8 *tamayyuz*); Q. 42:42 (*baghy*); Q. 96:6 (*ṭughyān*); Q. 25:21 (*ʿutuww*). All fourteen were found in the corpus output with the correct surface form and verse text matching the Uthmani edition.

---

## 4. Findings

### 4.1. The four-lexicon etymology table

Before turning to stage-level analysis, Table 1 summarises the canonical glosses of each root across four reference lexica.

**Table 1. Comparative etymology of the fourteen core roots across the four authoritative Arabic lexica**

| Stage | Root | Maqāyīs (Ibn Fāris) | Mufradāt (al-Rāghib) | Lisān al-ʿArab (Ibn Manẓūr) | Taḥqīq (Mostafavi) |
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

The table shows that the ordering from *uff* to *ʿutuww* is not the construction of the present analysis but is internally encoded in the lexicographic tradition itself: the four authoritative lexica already gloss each root with progressively more externalised and structural meanings, ascending from the murmured *uff*, through inner *karāha*, *ḍīq*, and *ḥuzn*, through evaluative *naqm*/*sakhaṭ*/*maqt*, to active *ghaḍab*/*ḥard*, to compressed *ghayẓ*, and into the externalised behavioural pole at *baghy*/*ṭughyān*/*ʿutuww*.

### 4.2. Distributional summary

Table 2 reports the principal distributional facts for the fourteen core roots. The table integrates frequency, Meccan/Medinan split, and (for the roots with sufficient morphological variation) morphological profile; it forms the empirical backbone of the analyses that follow.

Figures 2 and 3 visualise the distributional profile graphically: Figure 2 reports per-root frequency and the per-stage stage-totals; Figure 3 plots the Meccan/Medinan distribution and highlights the discursively-specialised roots discussed below. Figure 4 reports the morphological breakdown by part of speech.

**Table 2. Distributional profile of the fourteen core roots**

| Stage | Root | Total | Meccan | Medinan | Notes |
|:-:|:-:|:-:|:-:|:-:|:--|
| 1 | ʾff (أف) | 3 | 3 | 0 | All Meccan; lowest tier of verbal displeasure |
| 1 | krh (كره) | 41 | 14 | 27 | Medinan-tilted (raw *p* ≈ 1.0 × 10⁻⁷, Holm-adj. ≈ 1.4 × 10⁻⁶ — survives FDR); twofold *karāha*/*ikrāh* |
| 2 | ḍyq (ضيق) | 13 | 9 | 4 | Inner constriction (*ḍīq al-ṣadr*; *ḍāqa dharʿan*) |
| 2 | ḥzn (حزن) | 42 | 26 | 16 | Most frequent Stage-2 lexeme; valence transversal (see §4.4.2) |
| 2 | ʾsf (أسف) | 5 | 5 | 0 | Exclusively Meccan; *n* too small for inference |
| 3 | nqm (نقم) | 17 | 12 | 5 | Meccan-tilted; vengeful disapproval; cf. *al-muntaqim* |
| 3 | sxṭ (سخط) | 4 | 0 | 4 | Exclusively Medinan (raw *p* = 0.005, Holm-adj. *p* = 0.050 — borderline, see §4.5.2) |
| 3 | mqt (مقت) | 6 | 4 | 2 | Most intense moral aversion (Zajjāj) |
| 4 | ġḍb (غضب) | 24 | 13 | 11 | Central anger lexeme; predicated of God, prophets, believers |
| 4 | ḥrd (حرد) | 1 | 1 | 0 | Qur'anic hapax: sūrat al-Qalam, Q. 68:25 |
| 5 | ġyẓ (غيظ) | 11 | 3 | 8 | Compressed anger (raw *p* = 1.6 × 10⁻³, Holm-adj. ≈ 1.9 × 10⁻² — survives FDR); *tamayyuz* manifestation (Q. 67:8) |
| 6 | bġy (بغي) | 96 | 55 | 41 | Meccan-tilted (raw *p* = 4.1 × 10⁻⁴, Holm-adj. ≈ 5.3 × 10⁻³ — survives FDR); bridge node; bidirectional causation (see §4.8.5) |
| 6 | ṭġy (طغي) | 39 | 29 | 10 | Pharaonic; structural arrogance |
| 6 | ʿtw (عتو) | 10 | 9 | 1 | Settled defiance (raw *p* = 0.47, Holm-adj. *p* = 1.00 — does not survive FDR); properly *istikbār*-attached |
| **Σ** | — | **312** | **183** | **129** | |

Across the six stages: S1 = 44; S2 = 60; S3 = 27; S4 = 25; S5 = 11; S6 = 145. The asymptotic χ² against the uniform-six-stage null rejects (χ²(5) = 227.15, *p* < 0.001; Cramér's *V* = 0.38, Cohen's *w* = 0.85, large by Cohen's conventions). However, while expected counts are uniform at ~52 and well above Cochran's 5-per-cell rule, the *observed* marginal imbalance (S6 = 145 vs S5 = 11) is the asymmetric structure to which asymptotic χ² is most vulnerable: *baghy* alone supplies 96 attestations, almost a third of the total. We therefore complement with a **marginal-preserving permutation null** (Cochran 1954; Patefield 1981; Mehta and Patel 1983; Agresti 2013), giving the empirical *p*-value as the fraction of permuted χ² values meeting or exceeding 227.15. The result is *p* = 0.24 — under random stage relabelling, a statistic this extreme is not unusual. We read this honestly: asymptotic significance over-states the evidence for non-uniformity, and the substantive case for the six-stage architecture rests on the qualitative lexicographic, exegetical, and metaphorical evidence of §4.1 and §4.3–§4.8 rather than the omnibus *p*-value. We retain the asymptotic χ² as a descriptive statistic but treat it as *consistent with* — not *positive evidence for* — H1. A discriminating test of monotonicity is reported in §4.2.1.

A complementary χ² against the null of equal split between the phenomenological core (S1–5 = 167) and the behavioural-outcomes pole (S6 = 145) *fails to reject* (χ²(1) = 1.55, Cohen's *w* = 0.07). Because failure to reject is *absence of evidence of a difference* rather than evidence of equality, we report this not as corroboration of H2 but as *consistent with* the reading of §4.8.5 and §5.3: Stage-6 lexemes are not exclusively anger-derived but stand in *bidirectional* causal relation to the anger spectrum.

#### 4.2.1. Monotonic-trend tests for the six-stage ordering

Because the χ²(5) test confirms non-uniformity but says nothing about *ordering*, we report three complementary monotonic-trend tests of stage rank against attestation frequency. (i) **Spearman** between stage index and per-stage count is ρ = –0.09, *p* = 0.85 — the count rises from S1 (44) to S2 (60), drops through S3–S5 (27, 25, 11), then jumps to S6 (145), producing a non-monotonic profile. (ii) **Mann–Kendall** yields *S* = –3, *z* = –0.38, *p* = 0.71. (iii) **Cochran–Armitage-style** OLS slope yields slope = 10.17, *z* = 0.85, *p* = 0.40. All three fail to reject the no-trend null.

We read this as substantively interpretable: the action-intensity continuum is an ordering of *semantic intensity*, not *attestation frequency*. The Qur'anic corpus is not a random sample but a closed hortatory text whose lexical weights are *pedagogically determined*. One expects heaviest density at the two poles of moral consequence — S1–2 (entry points for *kaẓm*, *taqwā*, *ḥilm*) and S6 (the social-structural pathologies the text most frequently denounces) — with S3–5 as middle-trajectory states of lower independent salience. A flat trend test, given this structure, is the prediction the theory generates, not an embarrassment to it.


![**Figure 2.** Per-root and per-stage frequency of the 312 core spectrum attestations. *Left*: per-root frequency, bar colour encoding stage. Stage-6 internal asymmetry (*bġy* 96 vs *ʿtw* 10) reflects the lexical division between distributed-aggression and obstinate-defiance (§4.8). *Right*: stage totals S1 = 44, S2 = 60, S3 = 27, S4 = 25, S5 = 11, S6 = 145. χ²(5) = 227.15 (asymptotic *p* < 0.001), but permutation null *p* = 0.24 — see §4.2. Phenomenological core (S1–5 = 167) vs Stage 6 (145): χ²(1) = 1.55, fails to reject — *consistent with* the bidirectional-causation reading of §4.8.5.](fig2_frequency_by_stage.pdf){width=95%}


![**Figure 3.** Stacked Meccan/Medinan distribution for the fourteen core roots. Three roots survive Holm-Bonferroni correction over the family of fourteen per-root binomials at α = 0.05: *karh* (14M/27Md, raw *p* ≈ 10⁻⁷), *baghy* (55M/41Md, raw *p* ≈ 4 × 10⁻⁴), and *ghayẓ* (3M/8Md, raw *p* ≈ 1.6 × 10⁻³). *Sakhaṭ* (0M/4Md, raw *p* = 4.6 × 10⁻³) sits at adjusted *p* = 0.0503, just below conventional FDR threshold. *Asaf* (5/0 Meccan), *naqm* (12/5 Meccan), *ʿutuww* (9/1 Meccan) tilts are contextual but not FDR-significant. *Ḥard* hapax (sūrat al-Qalam, Q. 68:25, Meccan). The patterns instantiate *discursive-contextual specialisation* (§5.4).](fig3_meccan_medinan.pdf){width=95%}


![**Figure 4.** Morphological profile by part of speech. The left-to-right gradient shows verbal dominance at Stages 1–2 (*ḥzn* 88% verbal, *ḍyq* 62% — transient situational states), nominalisation at Stage 4 (*ghḍb* 16n/6v — stable attributable referent), and peak nominality with emerging participial forms at Stage 6 (*ṭāghūt*, *bāghin* — entrenched agent-property). The verbal→nominal gradient is independent corpus-internal evidence for the action-intensity continuum: as intensity ascends, representation reifies from *event* to *attribute* to *identity*.](fig5_morphology_stack.pdf){width=95%}


### 4.3. Stage 1 — Pre-anger displeasure

The lower bound of the continuum is occupied by two roots — *ʾ-f-f* and *k-r-h* — that mark the *pre-anger* register: vocal irritation and inner aversion respectively.

**4.3.1. *Uff* (3; all Meccan).** *Uff* (gloss: *taḍajjur*, "irritation") is the Qur'anic register's lowest verbal expression of displeasure. Its three attestations occupy paradigmatic moral positions: sūrat al-Isrāʾ (Q. 17:23) prohibits saying *uff* to one's parents (the *lowest* sign of displeasure morally weighted at the *highest* relational stake); sūrat al-Anbiyāʾ (Q. 21:67) places it in Abraham's mouth confronting idol-worshippers (prophetic remonstrance); sūrat al-Aḥqāf (Q. 46:17) ascribes it to a rebellious child reproaching believing parents (the inverse). *Uff* anchors the lower boundary of the spectrum at a register *below* anger proper but already morally accountable.

**4.3.2. *Karh* (41; 14M/27Md; raw *p* ≈ 1.0 × 10⁻⁷, Holm-adj. *p* ≈ 1.4 × 10⁻⁶ — survives FDR).** *Karh* exhibits a *twofold structure*: (a) **inner *karāha* (dislike)** — pre-anger evaluative dislike, framed as *reformable* by sūrat al-Baqara (Q. 2:216, *ʿasā an takrahū shayʾan wa-huwa khayrun lakum*); the Stage-1 anger-spectrum sense. (b) **Structural *ikrāh* (coercion)** — not an emotion but a structural extension of distaste into compulsion (sūrat al-Baqara, Q. 2:256, *lā ikrāha fī al-dīn*; sūrat al-Naḥl, Q. 16:106; sūrat al-Nūr, Q. 24:33). We include *karh* on the strength of its *karāha* sense. The Medinan-tilted distribution survives Holm-Bonferroni correction emphatically — *karh* is one of three roots, alongside *baghy* and *ghayẓ*, whose distributional asymmetry is not attributable to multiple-comparison artefact; the structural *ikrāh* sense in Medinan community-discipline contexts (consent in marriage, freedom in religion) accounts for the heavy Medinan weighting.

### 4.4. Stage 2 — Inner pressure and contraction

Stage 2 brings together three roots — *ḍ-y-q*, *ḥ-z-n*, *ʾ-s-f* — with sixty combined attestations.

**4.4.1. *Ḍīq* (13; 9M/4Md).** Ibn Fāris glosses *ḍyq* as "constriction, narrowness"; al-Rāghib in opposition to *saʿah* (expansion). The root appears predominantly in the construction *ḍīq al-ṣadr* (constriction of the chest), localising the experience to the embodied site. Sūrat al-Ḥijr (Q. 15:97) frames it as the prophetic response to social rejection. Al-Ṭabāṭabāʾī (*al-Mīzān* 12:195) observes the verse expresses divine *knowledge* of prophetic *ḍīq* rather than prohibition: a phenomenologically natural, theologically licit state, not a moral failing. Morphological profile: 8 verbs / 3 nouns / 1 participle — registering a transient, situationally-induced state.

**4.4.1.1. *Ḍāqa dharʿan* — inhibited aggression at Lot, sūrat Hūd, Q. 11:77/80.** The compound idiom *ḍāqa bihim dharʿan* ("his arm-span tightened by them") in the Lot narrative figures *post-anger blocked aggression* — anger at action-threshold but structurally inhibited. The four-step trajectory (trigger *sīʾa bihim* → constriction *ḍyq+dharʿ* → aspirational voicing *law anna lī bikum quwwatan* → transfer of agency to the divine through the angels' arrival) shows that *ḍyq* sits at *both* poles of the spectrum: pre-anger contraction *and* upper-pressure threshold of inhibition. The Qur'anic narrative theologises inhibited aggression: when the wronged agent lacks power, divine agency completes the anger trajectory.

**4.4.2. *Ḥuzn* (42; 26M/16Md).** The most frequent and most verbal Stage-2 lexeme (37v / 5n = 88% verbal). Ibn Manẓūr preserves the etymologically primary "rugged, uneven ground" (*al-arḍ al-ġalīẓah*); the metaphorical extension figures grief as inner roughness (anticipating Kövecses 2000 on EMOTION IS A LANDSCAPE schemas). Sūrat al-Baqara (Q. 2:38) places *ḥuzn* in syntagmatic pair with *khawf* and opposes both to divinely-given guidance — *ḥuzn* as the affective signature of *separation from guidance*. **Caveat (transversality)**: *ḥuzn* is *not* strictly anger-derived. It has four valences — standalone grief over loss (sūrat Yūsuf, Q. 12:84, Jacob over Joseph), externally-induced sorrow from being wronged (prophetic grief at rejection), positive moral compunction (the affective register of *tawba*), and anger turned inward when externally inhibited (closest to the Stage-2 placement here). Inclusion is justified by corpus density and proximity of (b) and (d) to the anger field. The 88% verbal profile reinforces the Stage-2 generalisation: inner-pressure lexemes denote transient, regulable states.

**4.4.3. *Asaf* (5; 5M/0Md).** The least frequent Stage-2 lexeme. Al-Rāghib glosses as the conjunction of grief and anger (*al-jamʿ bayna al-ḥuzn wa-l-ġaḍab*) — at the threshold between inner pressure and active anger. Sūrat al-Zukhruf (Q. 43:55, *fa-lammā āsafūnā intaqamnā minhum*) frames *asaf* as the immediate causal precursor of divine retribution; al-Ṭabarsī (*Majmaʿ* 9:82) glosses *al-asaf* here as "the intense anger arising from prior grief." The exclusive-Meccan distribution (5/0; raw *p* = 0.34, adj. *p* = 1.00) is suggestive but evidentially weak — at *n* = 5 the test has very low power. We register the 5/0 distribution as a *contextual observation* warranting follow-up at higher *n*, not as a confirmed empirical finding.

**4.4.3.1. *Ghaḍbān asifan* — sacred anger at Moses, sūrat al-Aʿrāf, Q. 7:150 / sūrat Ṭāhā, Q. 20:86.** The compound *ghaḍbān asifan*, applied to Moses on his return to find the calf-worshippers, generates a three-layer dialectic: *ghaḍab* is outward/kinetic (throwing the tablets, seizing Aaron); *asaf* is inward/potential (compassionate grief over the relapse). *Asaf* grounds *ghaḍab*: absent its compassionate ground, Moses' anger would be violence; present, it is anger in service of guidance.

**4.4.4. Network evidence for Stage-2 coherence.** The aya-level co-occurrence network (Figure 5) reveals that the strongest single edge connects *ḥzn* and *ḍyq* (weight 3); these two lexemes share three verses in the Qur'an, more than any other pair within the spectrum. Centrality analysis (Figure 6) places *ḥzn* among the highest-degree nodes (weighted degree 5, tied with *ġḍb*).

### 4.5. Stage 3 — Evaluative aversion

Stage 3 brings together three roots — *n-q-m*, *s-kh-ṭ*, *m-q-t* — with twenty-seven combined attestations. Each marks a distinct mode of *evaluative-aversive* response to a moral object. A note on internal ordering: *maqt* is the lexicographic superlative of *aversion* (Zajjāj, *ashaddu al-ibghāḍ*) but is placed *between* *sakhaṭ* and *ghaḍab* on the *action-intensity* axis because the paper's dimension is intensity of *action*, not intensity of *aversion*. *Maqt* is purely evaluative — rejection-distance rather than approach-aggression — and on the action axis sits below the kinetic-motor *ghaḍab* of Stage 4 and above the settled *sakhaṭ* of Stage 3.

**4.5.1. *Naqm* (17 attestations; 12 Meccan / 5 Medinan).** *Naqm* is the lexeme of *vengeful disapproval*: anger that is grounded in moral evaluation and oriented toward retribution. Sūrat al-Aʿrāf (Q. 7:126, *wa-mā naqamū minnā illā an āmannā bi-āyāti rabbinā*) is the linguistic exemplar. The lexeme generates *al-muntaqim* as a divine attribute (sūrat al-Sajda, Q. 32:22 and parallels). Position: *naqm* sits between *sakhaṭ* and *ghaḍab* on the action axis. The Meccan tilt (12/5) is consistent with the lexeme's frequent appearance in narrative-prophetic passages.

**4.5.2. *Sakhaṭ* (4 attestations; 0 Meccan / 4 Medinan).** Despite its low frequency, *sakhaṭ* furnishes one of the paper's principal distributional findings. The exclusive-Medinan distribution has a two-sided exact binomial *p*-value of **0.005** against the corpus-derived baseline of 0.74 Meccan probability.

***Baseline derivation.*** The 0.74 Meccan-rate baseline is the proportion of *ayat* (verses, not suras) classified Meccan in the QAC sura metadata. We use the ayat-weighted rate rather than the sura-count rate (~0.69) because an attestation drawn at uniform random from the corpus hits an aya, not a sura.

***Granular baseline sensitivity.*** With *n* = 4, the inference is mildly sensitive to the baseline:

| H₀ Meccan rate | Two-sided *p* (k=0, n=4) | Interpretation |
|:--:|:--:|:---|
| 0.70 (lower bound; sura-count proxy) | 0.0081 | significant at α = 0.05 |
| 0.72 | 0.0061 | significant at α = 0.05 |
| **0.74 (corpus ayat-weighted; default)** | **0.0046** | **significant at α = 0.05** |
| 0.76 | 0.0033 | significant at α = 0.01 |
| 0.78 (upper bound) | 0.0023 | significant at α = 0.01 |

The conclusion is robust across the range. **Multiple-comparison adjustment** (Holm-Bonferroni over the family of fourteen per-root binomials): *sakhaṭ* adjusted *p* = 0.0503 — *borderline*, just above the conventional α = 0.05 threshold. Three other roots survive Holm correction emphatically: *karh* (14M/27Md, raw *p* ≈ 1.0 × 10⁻⁷, adj. ≈ 1.4 × 10⁻⁶), *baghy* (55M/41Md, raw *p* ≈ 4 × 10⁻⁴, adj. ≈ 5.3 × 10⁻³), and *ghayẓ* (3M/8Md, raw *p* ≈ 1.6 × 10⁻³, adj. ≈ 1.9 × 10⁻²). The *asaf* (5/0; raw 0.34, adj. 1.00) and *ʿutuww* (9/1; raw 0.47, adj. 1.00) tilts do not survive correction.

All four *sakhaṭ* attestations are tied to the *Munāfiqūn* in their Medinan-period exegesis — sūrat Muḥammad (Q. 47:28, *ittabaʿū mā askhaṭa Allāh wa-karihū riḍwānahu*) is canonical, though al-Ṭabarī notes that sūrat al-Māʾida (Q. 5:80) is exegetically discussed as directed at the People of the Book rather than the *Munāfiqūn* properly. Following Narimani, Iqbali and Chari (2021), we read *sakhaṭ* not as an instantaneous emotional surge but as sustained *ethical disapprobation*; we propose:

> **Hypothesis (Discursive Specialisation of *sakhaṭ*):** *sakhaṭ* operates as a discursively specialised lexeme, reserved for divine displeasure with the *Munāfiqūn* — agents whose *ẓāhir* departs from their *bāṭin*. Since the *Munāfiqūn* category is constitutively a Medinan-period phenomenon, *sakhaṭ* attests exclusively in Medinan suras. This is one instance of a general phenomenon of *discursive-contextual lexical specialisation* in the Qur'anic register, of which *karh* (Medinan-community discipline) and the umbrella patterns *jrm* (Meccan) / *fsq* (Medinan) are convergent instances.

**4.5.3. *Maqt* (6 attestations; 4 Meccan / 2 Medinan).** *Maqt* is *intense moral aversion*: the four lexica converge on *ashaddu al-ibghāḍ* (Zajjāj / al-Layth in *Tahdhīb al-Lugha*); al-Rāghib grounds it specifically in observation of a reprehensible act (*ʿan amrin qabīḥin rakibahu*), making *maqt* purely evaluative. Canonical exemplars — sūrat Ghāfir (Q. 40:10, *maqt al-nafs* doubled), sūrat al-Nisāʾ (Q. 4:22, institutional moral aversion in forbidden marriages), sūrat Fāṭir (Q. 35:39, rising divine *maqt* against disbelievers), sūrat al-Ṣaff (Q. 61:3, saying-without-doing) — stabilise the lexeme as the Qur'anic register's term for moral aversion as evaluative response, distinct from the kinetic-motor *ghaḍab* of Stage 4.

### 4.6. Stage 4 — Active anger

Stage 4 (25 attestations) covers active, motor-mobilising anger.

**4.6.1. *Ghaḍab* (24; 13M/11Md).** The central anger lexeme of the Qur'an, with near-balanced Meccan/Medinan distribution marking it as the unmarked default. The four lexica gloss it as inner agitation of the heart oriented toward retribution (al-Rāghib) or inner motion disposing the agent to action (Ibn Fāris). Predicated balance-fully of God (sūrat al-Fatḥ, Q. 48:6), prophets, and believers. Morphologically nominal (16n / 6v / 2 ptcp = 67% nominal vs *ḥuzn*'s 88% verbal): *ghaḍab* is a *structural concept-state* with organisational standing rather than a transient affect. Al-Rāzī's *Mafātīḥ al-Ghayb* glosses divine *ghaḍab* in the register of *irādat al-ʿuqūbah* (paraphrase) — a normative-juridical orientation, not an emotional response. Network analysis places *ghḍb* among the top three for betweenness centrality (point estimate 0.17).

**4.6.2. *Ḥard* (sūrat al-Qalam, Q. 68:25, hapax).** A Qur'anic hapax in the Garden-Owners parable (*wa-ghadaw ʿalā ḥardin qādirīn*): garden-owners who vow in the night to harvest before dawn so as to deny the poor their share. Classical exegesis converges on a dual gloss: al-Ṭabarsī's *Majmaʿ al-Bayān* reads *ḥard* as both *ghaḍab* (anger) and *qaṣd* (purposive intent); al-Ṭabāṭabāʾī's *al-Mīzān* refines as anger-plus-deliberate-denial — purposive anger weaponised through resource-denial. The narrative consequence is the destruction of the garden by night-storm: divine retribution against the *ḥard*-driven plan to deny.

### 4.7. Stage 5 — Compressed/explosive rage

**4.7.1. *Ghayẓ* and the *kaẓm* metaphor (11 attestations; 3M/8Md; raw *p* = 1.6 × 10⁻³, Holm-adj. ≈ 1.9 × 10⁻² — survives FDR).** The four lexica converge: *ghayẓ* is "compressed contained anger" (al-Rāghib), "the highest concentration of restrained anger" (Mostafavi), "filling of the self with restrained anger" (Ibn Manẓūr) — pressurised contents of a sealed vessel. Sūrat Āl ʿImrān (Q. 3:134) commends *al-kāẓimīn al-ghayẓ*; the verb *kaẓm* derives from the act of tying off a waterskin, the agent-internal regulation that sustains containment. The construction itself presupposes that the believers being commended *experience* the *ghayẓ* they suppress — the Narimani et al. claim that *ghayẓ* in human reference is exclusive to unbelievers/hypocrites must therefore be qualified: *ghayẓ* in human attribution is *predominantly* — not exclusively — negative, with Q. 3:134 (*wa-l-kāẓimīn al-ghayẓa*) the canonical exception (transitive *ghayẓ directed at* believers is exclusively non-believer-attributed; intransitive/experiential *ghayẓ* — the *kāẓimīn* themselves — is attributed to believers). Read through Lakoff and Kövecses (1987), the *ghayẓ–kaẓm* pair instantiates ANGER IS A PRESSURIZED CONTAINER with precision: *ghayẓ* the contained fluid, *kaẓm* the agent's act of sealing (Figure 7). The Medinan tilt (8/3) survives FDR and tracks the discursive context: inner anger management becomes a salient pedagogical concern in the formative Medinan community.

**4.7.2. *Tamayyuz*: container collapse in sūrat al-Mulk, Q. 67:8 (manifestation, not separate root).** Sūrat al-Mulk (Q. 67:8) — *takādu tamayyazu min al-ġayẓ* ("[the fire] is on the verge of parting asunder from rage") — is the single most articulated image of rage in the Qur'an. *Tamayyaza* (root *m-y-z*: in *Mufradāt* and *Lisān* the dominant gloss is *al-tafrīq bayna al-mukhtaliṭ*, "separating things that have been mixed"; in the present context, the parting / severing of the contents from each other or of the vessel from itself) figures not the *exit* of pressurised content (as in English *she blew her top*, *he exploded*, *I lost it*) but the *structural integrity of the container itself failing*. We read this as the authors' CMT-grounded interpretation, complementing the classical "separation of constituents" gloss attested in al-Ṭabarī and al-Zamakhsharī, rather than as the plain lexicographic sense. We treat *tamayyuz* as a manifestation of Stage 5 rather than a distinct core root, retaining the fourteen-root inventory. H5 is corroborated in the form: Q. 67:8 instantiates the container-collapse failure mode with greater lexical transparency than the English exemplars in Lakoff and Kövecses's corpus.

### 4.8. Stage 6 — Behavioural outcomes (with caveats)

**4.8.1. *Baghy* (96; 55M/41Md; raw *p* = 4.1 × 10⁻⁴, Holm-adj. ≈ 5.3 × 10⁻³ — survives FDR).** The most frequent lexeme of the spectrum and the principal bridge node by point-estimate centrality. Glossed as "seeking beyond rightful bounds" (al-Rāghib) and "aggressive seeking with intent to oppress" (Mostafavi). Sūrat al-Shūrā (Q. 42:42) collocates *baghy* with *ẓulm*, embedding it in the moral-evaluation register. Ibn ʿĀshūr clarifies (*al-Taḥrīr* 25:126): *baghy* and *ẓulm* are near-synonymous, except *baghy* is specific to non-rightful aggression against another while *ẓulm* covers all injustice.

**4.8.2. *Baghy* as bridge node (with bootstrap uncertainty).** *Baghy* attains the highest point-estimate closeness centrality (0.55) and is tied with *ghaḍab* (0.53) and *asaf* (0.49) for the highest betweenness centrality (0.15). Bootstrap 95% percentile CIs (1,000 ayat-resamples) are wide — for *baghy*: betweenness ∈ [0.00, 0.31]; closeness ∈ [0.23, 0.84]; eigenvector ∈ [0.00, 0.68] — reflecting the small graph (14 nodes) and modest edge density. (Nodes with zero in-graph degree — *ʾff*, *mqt*, *ḥrd*, *ʿtw* — are trivially placed at the centrality floor with CI [0.00, 0.00].) On strict non-overlap, no node's centrality is significantly greater than another's. The bridging-role claim must therefore be qualified: *baghy* leads on three of four point-estimate measures, but the bootstrap does not rule out alternatives. What is *robust* at the aggregate level is the cross-field connectivity to the umbrella moral terms (Table 4): *baghy* shows sixteen aya-level co-occurrences with *ẓlm/jrm/fsq/ʿdw/šnʾ* combined, an integer-count pattern independent of centrality ranking. H4 is *consistent with* point estimates, qualified by bootstrap.

**Table 4. Cross-field co-occurrence of spectrum roots with umbrella moral terms (aya-level)**

Cross-field ties for the original ten-root analysis are preserved here from the prior pipeline run; ties for the four newly-incorporated roots (*ʾff*, *naqm*, *maqt*, *ḥard*) are sparse and dominated by zeros and are omitted.

| Root | šnʾ | jrm | fsq | ẓlm | ʿdw | Total |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| ḍyq | 0 | 0 | 0 | 0 | 0 | 0 |
| ḥzn | 0 | 0 | 0 | 1 | 1 | 2 |
| ʾsf | 0 | 0 | 0 | 1 | 1 | 2 |
| sxṭ | 0 | 0 | 0 | 0 | 0 | 0 |
| ġḍb | 0 | 0 | 0 | 2 | 3 | 5 |
| ġyẓ | 0 | 0 | 0 | 0 | 1 | 1 |
| **bġy** | **1** | **1** | **2** | **4** | **8** | **16** |
| ṭġy | 0 | 0 | 0 | 2 | 1 | 3 |
| ʿtw | 0 | 0 | 0 | 0 | 0 | 0 |

Of the total cross-field ties across the fourteen spectrum roots, nineteen (~53%) involve *baghy*. *Baghy* thus serves as the principal lexical bridge between the emotional and the broader moral-evaluation field of the Qur'an.

**4.8.3. *Ṭughyān* (39 attestations; 29 Meccan / 10 Medinan).** Root *ṭ-gh-y* derives from water flooding past its banks. Sūrat al-ʿAlaq (Q. 96:6–7, *kallā inna l-insāna la-yaṭghā an raʾāhu staġnā*) compresses a psychology of rebellion into a conditional: *ṭughyān* arises from the appraisal of *istighnāʾ* (self-sufficiency) — structurally an appraisal-theoretic claim, congruent with Lazarus (1991), Scherer (2001, 2005), and Roseman's (1996) "agency-self / motive-inconsistent / high-control" pattern. Qarizadeh et al.'s (2024) polysemy analysis notes the cognitive structure; we identify *ṭughyān* as the cognitive-appraisal node of Stage 6.

**4.8.4. *ʿUtuww* (10 attestations; 9 Meccan / 1 Medinan; raw *p* = 0.47, Holm-adj. *p* = 1.00 — does not survive FDR).** The most extreme lexeme — "obstinate excess" (Ibn Manẓūr), "extreme self-aggrandisement in disobedience" (al-Rāghib). Sūrat al-Furqān (Q. 25:21) collocates *ʿatū ʿutuwwan kabīrā* with *istakbarū fī anfusihim*: rebellion crystallised into existential posture. The 9/1 Meccan distribution is consistent with the lexeme's rhetorical function as terminal designation for Nūḥ-, ʿĀd-, Thamūd-, and Pharaonic-people narratives, but the raw *p*-value of 0.47 against the 0.74 Meccan baseline indicates that the 9/1 split is *not* statistically distinguishable from chance under the binomial.

**4.8.5. Bidirectional causation and a *tafsīr*-grounded audit.** *Baghy* arises frequently from greed and *ʿulw fī al-arḍ* (cf. sūrat al-Anʿām, Q. 6:21); *ṭughyān* — paradigmatically Pharaonic (sūrat al-Nāziʿāt, Q. 79:17) — is rooted in structural arrogance, with sūrat al-Shuʿarāʾ (Q. 26:55, *innahum lanā la-ghāʾiẓūn*) reversing polarity to show oppressor-anger arising *from* the rebellion of the oppressed; *ʿutuww* attaches to *istikbār* as settled character. The causation arrow is therefore *bidirectional*. To operationalise this, each of the 145 Stage-6 attestations was coded against the joint reading of *al-Mīzān*, *al-Kashshāf*, *Majmaʿ al-Bayān*, and *al-Taḥrīr wa-l-Tanwīr* under a three-label codebook — **A** (anger-origin: the immediate exegetical antecedent is an anger-type affective state), **S** (structural-origin: the antecedent is *istikbār*/*ʿulw*/greed without explicit anger antecedent), or **A+S** (both antecedents explicitly present). Two independent graduate-level coders (the corresponding author and an Arabic-literature graduate trained on the codebook with relevant commentary excerpts supplied) coded all 145 attestations independently; disagreements (n = 14) were reconciled in a joint session against the four commentaries, with original-pass codings used for κ computation. Cohen's κ = 0.79 — *substantial* agreement (Landis and Koch 1977). Full coding at `data/concordance/stage6_causation_coding.csv`. Results: A = 38 (26%), S = 71 (49%), A+S = 36 (25%); by root, *baghy* 22A/50S/24A+S, *ṭughyān* 11A/19S/9A+S, *ʿutuww* 5A/2S/3A+S (sub-counts sum to root totals). Re-running χ²(1) on A-only (Stages 1–5 = 167 vs. anger-derived Stage-6 = 38) yields χ²(1) = 81.4, *p* < 0.001 — the phenomenological core dominates anger-derived outcomes ~4.4×. The full-Stage-6 near-balance (χ²(1) = 1.55) is therefore explained: S-attestations belong to an adjacent moral-anthropological field of *ẓulm-istikbār-ʿulw* that the corpus pervasively documents, and *baghy*/*ṭughyān*/*ʿutuww* are not coextensive with "anger outcomes" in the strict sense.


![**Figure 5.** Aya-level co-occurrence network of the fourteen core roots; edges weighted by shared-ayat count. Strongest edge *ḥzn–ḍyq* (weight 3) corpus-validates the Stage-2 grouping (sūrat Hūd, Q. 11:12; sūrat al-Anʿām, Q. 6:33). *Baghy* anchors the right cluster with edges to the moral-evaluation lexicon (*ẓlm/jrm/fsq*). Transitive structure (no direct S1→S6 edges; mediation through S2–S5) is consistent with both the action-intensity gradient and the bidirectional Stage-6 reading (§4.8.5).](fig4_cooccurrence.pdf){width=95%}


![**Figure 6.** Three centrality measures with bootstrap 95% percentile CIs on the aya-level co-occurrence graph: (a) weighted degree, (b) betweenness, (c) closeness. *Baghy*: highest closeness point-estimate (0.55, CI [0.23, 0.84]) and shared-highest betweenness (0.15, CI [0.00, 0.31]) with *ghaḍab* and *asaf* — pivotal between the anger spectrum and the wider moral-evaluation field. Wide CIs reflect the small graph; bridging-role claim consistent with point estimates, qualified by bootstrap (§4.8.2). *Ḍyq* and *ḥzn* (S2) high-closeness despite low frequency — inner-pressure cluster structurally central.](fig7_centrality.pdf){width=95%}


### 4.9. Robustness checks: the umbrella moral terms

For robustness, the umbrella roots were extracted and analysed (note that *karh*, formerly an umbrella term, is now incorporated into the spectrum at Stage 1 and is reported in Table 2). Distributions of the remaining five (Table 5) confirm that the spectrum's structure is not artefactual.

**Table 5. Distribution of umbrella moral terms**

| Root | Total | Meccan | Medinan | Binomial *p* | Interpretation |
|:----:|:-:|:-:|:-:|:-:|:---|
| šnʾ | 3 | 1 | 2 | — | *n* too small for inference |
| jrm | 66 | 60 | 6 | < 0.0001 | Strongly Meccan; anti-*shirk* polemic |
| fsq | 54 | 20 | 34 | 0.0007 | Significantly Medinan; community-discipline register |
| ẓlm | 315 | 211 | 104 | — | Pervasive meta-category; cannot anchor a single point |
| ʿdw | 106 | 47 | 59 | 0.008 | Tilts Medinan; the lexeme of mutual antagonism |

The opposing patterns of *jrm* (strongly Meccan) and *fsq* (significantly Medinan) instantiate the same discursive-contextual specialisation that we identified for *sakhaṭ* and *karh*. The umbrella analysis confirms a *general* phenomenon.

### 4.10. Comparative translation analysis (illustrative sample)

To illustrate how the spectrum's intensity differentiation fares in translation, Table 6 compares five English translations on four canonical verses. We frame this as an *illustrative* case, not a systematic translation-criticism evaluation: a properly powered evaluation would require a stratified random sample of all 312 attestations (or, more practically, ~30 verses sampled across the six stages with inter-rater coding by trained Arabist coders). The four-verse, five-translation sample here suffices to register the *pattern* of levelling but does not, on its own, support the strong translation-recommendation set in §5.6.

**Table 6. Translation of four canonical verses across five English translations** (illustrative sample; *n* = 4 verses × 5 translations = 20 cells)

| Term & verse | Yusuf Ali | Pickthall | Arberry | Saheeh Intl. | Hilali-Khan |
|:----:|:---|:---|:---|:---|:---|
| *ḍīq* (sūrat al-Ḥijr, Q. 15:97) | "thy heart is distressed" | "thy bosom is at times oppressed" | "thy breast is straitened" | "your chest is constrained" | "your breast feels tight" |
| *ġayẓ* (sūrat Āl ʿImrān, Q. 3:134) | "restrain anger" | "control their wrath" | "restrain their rage" | "suppress anger" | "repress anger" |
| *tamayyuz* (sūrat al-Mulk, Q. 67:8) | "almost burst with fury" | "almost burst with rage" | "well-nigh bursts asunder with fury" | "almost bursts with rage" | "almost bursts up with fury" |
| *ṭughyān* (sūrat al-ʿAlaq, Q. 96:6) | "transgresses all bounds" | "rebelleth" | "waxes insolent" | "transgresses" | "transgresses (boundary)" |

Two illustrative observations. First, the rendering of *ġayẓ* in sūrat Āl ʿImrān (Q. 3:134) collapses the *ghaḍab/ġayẓ* distinction in all five translations — the English versions render *ġayẓ* with terms (*anger*, *wrath*, *rage*) that are also routinely used for *ghaḍab*. The differentia — the *containment* dimension — is preserved only via the contextual verb of restraint, not in the lexeme itself. Second, the rendering of *tamayyuz* in sūrat al-Mulk (Q. 67:8) is uneven: Arberry's "well-nigh bursts asunder" preserves the *structural-disintegration* component of the source; the others render it variationally as *burst with* + emotion, foregrounding the exit of contents but losing the structural-collapse implication. These observations are *suggestive of* a systematic levelling pattern but are not on their own evidentially decisive.

### 4.11. Summary of computational corroboration analyses (full detail in Supplementary Material)

Four computational analyses — extending the main pipeline with neural-language-model and information-theoretic measurements over the same 312 attestations — are reported in full in the Supplementary Material (`paper/english/supplementary.md`, sections S1–S4) and summarised here in a single paragraph. **S1 (cross-translation semantic drift)** uses multilingual MPNet over ten parallel renderings (5 EN + 5 FA) per attestation and recovers three drift bands that map onto the spectrum: affective-core lexemes (*ghaḍab*, *ḥuzn*, *baghy*) cluster low (drift < 0.20), evaluative-aversion and containment-pressure lexemes (*sakhaṭ*, *maqt*, *ḍyq*, *ghayẓ*) cluster high (> 0.22), and *ṭughyān* tops the non-hapax distribution — convergent with the §4.10 levelling observation. **S2 (CAMeLBERT-CA contextual-embedding clustering)** finds silhouette = −0.082, ARI = 0.059, NMI = 0.077 against the six-stage labelling: a clear null in which the model clusters by root identity rather than by stage, taken as evidence that the spectrum adds analytical structure beyond the language model's distributional view. **S3 (PMI-weighted co-occurrence network)** corrects the §4.8 unweighted graph for marginal-frequency artefacts: the *asaf*–*ghaḍab* pairing (npmi = 0.59) emerges as the spectrum's strongest signal, the Stage-2 *ḍyq*–*ḥuzn* edge (0.47) is ratified, and *baghy*'s outsized raw-count centrality is shown to be partly a frequency artefact. **S4 (Nöldekean diachronic null)** finds Spearman ρ = −0.157 (95% CI via Fisher's z: [−0.265, −0.046]; *p* = 0.006) against revelation order — a small effect (< 3% of variance) and substantively a null, consistent with the claim that the six-stage taxonomy organises by *intensity*, not by *chronology*.

---

## 5. Discussion

### 5.1. The integrated logic of escalation

The findings cohere into a single structural claim: the Qur'anic lexicon of the anger spectrum encodes a **logic of anger escalation** operating along three dimensions — locus (inner → outer), intensity (low → high), and scope (individual → structural). The lexemes are not synonyms but *grades* ordered by an intelligible cognitive logic.

In compact form: *Pre-anger displeasure → Inner pressure → Evaluative aversion → Active anger → Compressed rage → Behavioural outcomes (with caveats)*. The arrows index not mere temporal succession but conditional intensification at each step where regulation may succeed or fail. Stage 6 is distinctive: the move into behavioural outcomes is *not* a deterministic escalation from anger but is influenced by independent vectors (greed, *istikbār*, structural arrogance) — which is why we read the near-balance between S1–5 (167) and S6 (145) as theoretically informative rather than paradoxical.

### 5.2. Convergence with contemporary emotion psychology

The six-stage continuum maps onto four families of contemporary emotion theory at points of structural rather than psychometric convergence, sufficient to ground the Islamic-psychology implications of §5.7 and to identify where the Qur'anic lexicon *extends* the contemporary models.

**Gross's process model.** Gross (1998, 2014, 2015) partitions emotion regulation into five sequential strategies: *situation selection*, *situation modification*, *attentional deployment*, *cognitive change*, and *response modulation*. The Qur'anic continuum partitions the trajectory more finely on the affective side: **S1** (*uff*, *karāha*) ↔ *situation selection*; **S2** (*ḍīq*, *ḥuzn*, *asaf*) ↔ *situation modification*; **S3** (*naqm*, *sakhaṭ*, *maqt*) ↔ *attentional deployment* and *cognitive change*; **S4** (*ghaḍab*, *ḥard*) ↔ *response selection*, the kinetic-motor enactment; **S5** (*ghayẓ*/*kaẓm*; *tamayyuz*) ↔ *response modulation*, with *kaẓm* operationalising agent-internal *suppression / inhibition* of expression — one strategy among several available in Gross's typology (Gross 2015) — and *tamayyuz* (Q. 67:8) its container-collapse failure mode. **S6** (*baghy*, *ṭughyān*, *ʿutuww*) lies beyond Gross's frame: process-model regulation concerns the *emotional episode*, but Stage 6 lexicalises *structural-moral pathologies of personhood* outliving any single episode — with the §4.8.5 caveat that Stage 6 has bidirectional causation with the spectrum.

**Plutchik's intensity wheel; Spielberger's STAXI architecture.** Plutchik (1980, 2001) organises anger on a three-level escalation (*annoyance → anger → rage*); the Qur'anic continuum *refines* this by partitioning *annoyance* into vocal irritation (*uff*, S1), inner aversion (*karāha*, S1), and inner pressure (*ḍīq*, *ḥuzn*, *asaf*, S2) — three Qur'anic stages where Plutchik has one label — and by inserting the *compressed-rage* register (*ghayẓ*, S5) between *anger* (≈ S4 *ghaḍab*) and the unmarked terminal *rage*. Spielberger's STAXI-2 (1999) further partitions anger into *trait*, *state*, and *control*. The Qur'anic lexicon realises this trichotomy at the lexical surface: trait-like sustained states (*ḥuzn* at 88% verbal registering recurrent affective episodes, *ḍīq*, *karāha*); state-like situational responses (*sakhaṭ*, *maqt*, *ghaḍab*); and *kaẓm* (Q. 3:134) as the Qur'anic *anger-control* lexeme, operationally close to Spielberger's *anger-in* / suppression construct with the addition of explicit moral commendation.

**Appraisal theory: Scherer's checks and Roseman's *ṭughyān*-pattern.** Appraisal theory (Frijda 1986; Lazarus 1991; Scherer 2001, 2005; Roseman 1996) holds that emotional response is determined not by stimulus alone but by cognitive *appraisal* along a defined set of dimensions. Scherer's component-process model specifies four sequential checks; the Qur'anic Stage-3 lexemes operate as a lexicon for the normative-significance check at progressively higher intensities (*naqm* → *sakhaṭ* → *maqt*). Sūrat al-ʿAlaq (Q. 96:6–7) conditions *ṭughyān* on the appraisal of *istighnāʾ*: the agent perceives high coping potential, low external constraint, and self-agency — the *agency-self / motive-consistent / high-control* pattern Roseman would predict for defiance. The Qur'anic lexicon thus encodes — as architectural design rather than theoretical statement — insights contemporary emotion science has reached independently.

### 5.3. The phenomenology/outcomes balance

A naive ten-root reading once suggested 2.4× more attestations at the behavioural pole than at Stages 1–3 combined, indicating discursive over-emphasis on outcomes. The revised fourteen-root inventory (167 / 145; χ²(1) = 1.55, fail to reject) tells a different story: the expanded phenomenological vocabulary (*uff*, *karh*, *naqm*, *maqt*, *ḥard*) brings the lower stages into balance with Stage 6, as one would expect if (i) the phenomenological side is richer than prior analysis allowed, and (ii) Stage-6 lexemes are not exclusively anger-derived but stand in bidirectional causal relation to anger. In Fauconnier and Turner's (2002: 17–57) terms, the Stage-6 lexemes operate as a conceptual blend whose input spaces are wrong-doing-as-supremacism and anger-as-pressure, with the blend inheriting causal vectors from both inputs and running them bidirectionally. The methodological lesson: corpus-distributional analyses of religious texts are maps of *discursive emphasis*, entangled with category-membership and category-causation decisions.

### 5.4. Discursive-contextual specialisation

The FDR-surviving Medinan tilt of *karh* (raw *p* ≈ 10⁻⁷, adj. ≈ 10⁻⁶), the borderline-FDR Medinan exclusivity of *sakhaṭ* (adj. *p* = 0.050), the FDR-surviving Medinan tilt of *ghayẓ* (adj. ≈ 1.9 × 10⁻²), the FDR-surviving Meccan tilt of *baghy* (adj. ≈ 5.3 × 10⁻³), alongside the contextual-only Meccan tilts of *asaf*, *naqm*, and *ʿutuww*, the hapax-Meccan *ḥard*, and the strong umbrella patterns *jrm* (Meccan) and *fsq* (Medinan), instantiate **discursive-contextual specialisation**: members of multi-lexeme semantic fields preferentially attaching to specific discursive registers. The pattern is not random — *sakhaṭ* attaches to the *Munāfiqūn* (a Medinan phenomenon), *karh* to the structural *ikrāh* idiom of Medinan community discipline, *ghayẓ* to the *kaẓm* pedagogy of Medinan ethics, *asaf* to prior-prophet narratives (Meccan-rhetorical), *jrm* to anti-*shirk* polemic (Meccan), *fsq* to intra-community discipline (Medinan). El-Awa (2006) on textual relations and Sinai (2017, 2023) on Meccan/Medinan diachrony supply the theoretical framework: specialisation is exactly the kind of pattern one would expect from the Qur'an's gradual response to evolving sociolinguistic contexts. The phenomenon is, to our knowledge, undocumented as a systematic corpus-distributional pattern in Qur'anic-linguistic scholarship; future work should test the generalisation across other multi-lexeme fields, in dialogue with QurAna/QurSim (Sharaf and Atwell 2012a, 2012b), QuranMorph (Akra, Hammouda and Jarrar 2025), and MASAQ (Sawalha et al. 2024).

### 5.5. Q. 67:8 and the container metaphor: a focused comparative survey

Lakoff and Kövecses (1987: 195–221) reconstructed American-English anger as a *five-stage prototype scenario* — (1) offending event, (2) anger, (3) attempt at control, (4) loss of control, (5) act of retribution — with the PRESSURIZED CONTAINER schema mapped onto stages (2)–(4). English exemplars lexicalise the stage-(4) failure-mode as the *exit of contents* with the container preserved (*blew his top*, *flipped his lid* — the rupturing component is peripheral, not the body of the vessel). The Qur'anic *ghayẓ–kaẓm–tamayyuz* triad maps onto the same stages (2)–(4) with a precision the English exemplars do not match at stage (4): *ghayẓ* is glossed as compressed contained anger (stage 2); *kaẓm* (Q. 3:134) names the agent-internal suppression operation (stage 3); sūrat al-Mulk (Q. 67:8, *takādu tamayyazu min al-ġayẓ*) lexicalises *the parting / severing of the vessel itself* (stage 4), figuring the fire-vessel of Jahannam parting structurally from the rage of its contents rather than the exit of contents from an intact vessel.

A focused six-tradition survey contextualises the strength of this claim. **Akkadian** anchors anger in the *libbu* and *kabattu* as filled containers (*libbāti malû*, CAD L 163–164; Bodi 2018); recent bodily-mapping work on Neo-Assyrian texts (Lauri et al. 2024) confirms a dominantly FILLING / HEAT-IN-CONTAINER schema. **Biblical Hebrew** centres on *ḥēmâ* (heat/fury, frequently the object of *šāphakh* "to pour out") and the formulaic *ḥarôn-ʾaph*; Kruger (2000, 2015) demonstrates that ANGER IS FLUID IN A CONTAINER and ANGER IS FIRE IN THE NOSE are the dominant metaphors of the Hebrew Bible, both schematically EXIT-typed. The instructive exception is Job 32:19, where Elihu declares his belly *kĕ-yayin lōʾ-yippātēaḥ … yibbāqēaʿ* — "like wine that is not opened … about to burst like new wineskins": the verb *bāqaʿ* names exactly the structural failure of the vessel that the Qur'anic *tamayyaza* names. We therefore qualify our claim — Q. 67:8 is *an early and unusually transparent* lexicalisation of container collapse, not a unique one. **Homeric Greek** uses *kholos* (bile, rising) and *mēnis* (ritualised wrath); Muellner (1996) and Cairns (2003) read both as fluid-and-heat schemas, with no Iliadic image of vessel rupture. **Vedic and Classical Sanskrit** lexicalise anger principally as *krodha* and *manyu*, the latter personified as a martial deity associated with Indra (ṚV 10.83–84); the dominant images are FIRE and WEAPON-RELEASE, not vessel-disintegration. **Classical and Modern Chinese** lexicalises anger through *nù*, *fèn*, and *qì* (Yu 1995); Kövecses, Benczes and Szelid (2025) identify ANGER IS HOT *QÌ* IN A CONTAINER as the central schema. **Pre-Islamic *Jāhilī* Arabic** already deploys *ḥamiya* "to be heated" and *ġalā* "to boil" for hostile arousal, alongside *ġayẓ* in the cognate fluid-heat register; the lexical groundwork for Q. 67:8 is genuinely Arabian.

Five of the six traditions concentrate anger-imagery around *filling*, *heating*, *fluid-rising*, and *exit / overflow*; the **Hebrew Bible alone** offers a clear pre-Qur'anic parallel to vessel-rupture proper (Job 32:19). We accordingly hold our claim at **"an early and unusually transparent"** lexicalisation of container collapse, with Job 32:19 acknowledged as a structurally cognate Northwest-Semitic precedent (though Akkadian *kabattu napāḫu* "liver bursting", Greek Iliadic *cholos* swelling imagery, and Vedic *manyu* combustion offer imperfect cognates of step-(iv) container-rupture imagery that a properly stratified cross-linguistic comparison may bring more fully into the picture). The Qur'anic data thus *strengthen* the cross-cultural universalist hypothesis of CMT (Lakoff and Kövecses 1987; Kövecses 2000); they extend the empirical base to seventh-century Arabic in a register that the 2025 *Metaphors of ANGER* encyclopedia, which omits a dedicated treatment of Classical Arabic, leaves un-canvassed.


![**Figure 7.** The ANGER-IS-A-PRESSURIZED-CONTAINER schema (after Lakoff and Kövecses 1987), instantiated by *ghaḍab → ghayẓ + kaẓm → tamayyuz*. **Panel 1** (S4): *ghaḍab* — open container, affect dissipating into language. **Panel 2** (S5, sūrat Āl ʿImrān, Q. 3:134): *ghayẓ* — fluid sealed by *kaẓm* (etymologically the tying-off of a waterskin). **Panel 3** (S5 manifestation, sūrat al-Mulk, Q. 67:8): *tamayyuz* — structural failure; *m-y-z* "to part, sever" figures the splitting of the container itself, not (as English *explode*) the exit of contents. The Qur'anic instantiation is, on the conservative claim of §5.5, *unusually transparent* relative to the English exemplars in Lakoff and Kövecses's corpus.](fig6_metaphor_v2.jpg){width=100%}


### 5.6. Implications for Qur'anic translation (conditional on follow-up evaluation)

Translation criticism has long observed that translations tend to level the spectrum — that *ġaḍab* and *ġayẓ* alike become *anger*; that *baghy*, *ṭughyān*, and *ʿutuww* alike become *transgression* (Table 6). Recent computational work — Gaanoun and Alsuhaibani (2025) on sentiment preservation across seven English translations, Khan et al. (2025) on the broader NLP-Qur'anic-studies field — has begun to operationalise the levelling concern at scale on coarse Ekman categories, though without a graded reference model of the lexical spectrum against which the levelling could be benchmarked. We frame the present discussion as **conditional implications**: contingent on a follow-up systematic evaluation (a stratified random sample of ~30 verses across the six stages, with multi-rater coding against the spectrum reference model), the analysis would *if confirmed* support the following candidate equivalents:

> *uff*: vocal sigh of irritation · *karh* (*karāha*): inner dislike · *karh* (*ikrāh*): coercion (a structural extension, not an emotion) · *ḍīq*: inner constriction · *ḍāqa dharʿan*: arm-span tightening / inhibited aggression · *ḥuzn*: persistent grief (transversal valence) · *asaf*: regretful dismay (with anger) · *naqm*: vengeful disapproval · *sakhaṭ*: moral disapprobation · *maqt*: intense moral aversion · *ghaḍab*: anger · *ḥard*: anger combined with deliberate denial · *ghayẓ*: contained / boiling rage · *tamayyuz min al-ġayẓ*: bursting from rage · *baghy*: aggressive transgression · *ṭughyān*: rebellious overflow · *ʿutuww*: obstinate defiance.

A second conditional implication is that pedagogical translations may benefit from marking each lexeme's position on the continuum, but the empirical case for this rests on the comparative comprehension study we commend to future work.

### 5.7. Implications for Islamic psychology

The continuum offers a culturally-grounded framework mapping onto Gross's model without importing secular vocabulary, with three conceptual implications: **(i) Prevention** — early-stage recognition through the indigenous S1–2 lexicon (*uff*, *karāha*, *ḍīq*, *ḥuzn*) supports CBT-style interception of affective dysregulation; **(ii) Crisis intervention** — *kaẓm* integrates with contemporary suppression-and-reappraisal techniques; **(iii) Rehabilitation** — post-failure Stage 6 is framed as recoverable through *tawba*, providing motivational reinforcement for anger-disorder and post-violent-trauma rehabilitation. These are conceptual; their translation into validated clinical interventions awaits empirical studies we recommend as a priority.

---

## 6. Conclusion

### 6.1. Substantive contributions

This paper advances three contributions. **Methodologically**, we have demonstrated that the integration of Izutsu's semantic-field analysis, Kennedy–Sassoon scalar semantics, and Lakoff–Kövecses CMT — coupled with a reproducible computational pipeline over the QAC — produces a research apparatus stronger than the sum of its parts. To our knowledge, this trifold integration with corpus-empirical validation has not previously been deployed in Qur'anic studies, although Qāʾimīniyā (2011, 2014) and Pakatchi and Afrashi (2020) have integrated Izutsu and CMT.

**Descriptively**, we have produced a reproducible concordance of 312 attestations across the fourteen core spectrum roots, with distributional and network-analytic outputs — FDR-adjusted binomial tests, marginal-preserving permutation null *p*-values, and bootstrap 95% CIs on every centrality estimate — providing a foundation on which further philological and computational work can build.

**Theoretically**, we have formulated and empirically defended the **Qur'anic Action-Intensity Continuum Hypothesis**: the fourteen core lexemes operate as a single graded continuum structured by *intensity of action* and partitioned into six phenomenologically meaningful stages. The hypothesis is supported by qualitative evidence from the four authoritative lexica and the broadened *tafsīr* consultation of §3.5, and by quantitative evidence from frequency, distribution, morphology, and network structure. The κ = 0.79-validated *tafsīr*-coding audit grounds the bidirectional-causation reading of Stage 6; the six-tradition survey of §5.5 calibrates Q. 67:8 as *early and unusually transparent* — rather than uniquely transparent — lexicalisation of "container collapse", with Job 32:19 (*bāqaʿ*) acknowledged as a structurally cognate Northwest-Semitic precedent.

### 6.2. Answers to the research questions

**RQ1–RQ2.** The anger-spectrum field is a fourteen-node lexical network organised by *intensity of action*. The bridge node is *baghy* (closeness 0.55; ~53% of cross-field ties to the umbrella moral-evaluation terms); stage-internal hubs are *ḥuzn* (S2) and *ghaḍab* (S4). The ordering is licensed by the trifold synthesis of §2 and shown by Table 1 to be internally encoded in the four authoritative lexica.

**RQ3.** The empirical distribution is *consistent with* — not by itself confirmatory of — the continuum. The asymptotic χ²(5) = 227.15 is large, but permutation null *p* = 0.24; the S1–5/S6 χ²(1) = 1.55 fails to reject, consistent with the bidirectional-causation reading supported by the κ = 0.79 audit (A = 26%, S = 49%, A+S = 25%; A-only re-analysis χ²(1) = 81.4, *p* < 0.001). Three roots survive Holm-Bonferroni emphatically (*karh*, *baghy*, *ghayẓ*); *sakhaṭ* sits at adj. *p* = 0.0503, substantively supported by the convergence with the *Munāfiqūn*-discursive reading. The morphological gradient (verbal S1–2 → nominal S6) supplies convergent corpus-internal evidence.

**RQ4.** The continuum is structurally homologous with Gross's process model (S1–5), with Plutchik's intensity wheel and Spielberger's STAXI architecture, and with Lazarus–Scherer–Roseman appraisal theory (sūrat al-ʿAlaq, Q. 96:6–7, *ṭughyān* on *istighnāʾ*). It extends beyond all four at Stage 6, qualified by the bidirectional-causation caveat.

**RQ5.** *Conditional* practical implications follow for Qur'anic translation (§5.6) and for Islamic psychology (§5.7), framed as hypotheses for empirical follow-up.

### 6.3. Limitations and future work

The analysis is bounded by five limitations, each pointing to a constructive next step. (i) **Surface-lexical scope.** Discourse-analytic close-reading of the spectrum's narrative *deployment* across suras is left for future work, in dialogue with El-Awa (2006) and Sinai (2017, 2023). (ii) ***Tafsīr* engagement.** A *tafsīr*-archive deep-dive — systematic indexing against the full classical/medieval/Sufi/modernist tradition (al-Qushayrī, the *Tafsīr* attributed to al-Kāshānī, Sulamī's *Ḥaqāʾiq*, Twelver, Muʿtazilī, and modernist materials), with κ-validated multi-coder reading on contested verses — would deepen exegetical grounding. (iii) **Cognitive-linguistic apparatus.** Engagement with classical Arabic *bayān* theory (al-Jurjānī's *Dalāʾil al-Iʿjāz*, al-Sakkākī's *Miftāḥ al-ʿUlūm*) would supply an indigenous substrate. (iv) ***Ḥadīth* integration.** A parallel concordance over Ṣaḥīḥ al-Bukhārī, Ṣaḥīḥ Muslim, and al-Kāfī would supply convergent evidence on *kaẓm* and a cross-corpus replication test for the underpowered *asaf* 5/0 distribution. (v) **Islamic-psychology operationalisation.** The §5.7 implications await translation into pilot studies of *kaẓm*-grounded emotion-regulation training, validated against the STAXI and DERS. The methodological commitment remains: computational evidence is a *complement to* — not a replacement for — the classical philological and exegetical tradition.

### 6.4. Closing remark

The Qur'anic lexicon encodes a sophisticated theory of the anger spectrum — not as explicit formulation but as the architectural design of its semantic surface. Recovering that theory requires methodological tools that bring together classical philological attentiveness, contemporary linguistic-theoretical precision, and corpus-computational verifiability. We hope the present study, alongside Izutsu, Qāʾimīniyā, Pakatchi, Narimani et al., and Qarizadeh et al., advances this triple integration.

---

## Acknowledgements

The authors thank Kais Dukes (in memoriam) and the team behind the Quranic Arabic Corpus, and the Tanzil Project, for releasing the morphological and textual resources without which this kind of empirical Qur'anic analysis would not be feasible. We thank Urmia University for institutional support.

## Funding

This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.

## Competing interests

The authors declare no competing financial or non-financial interests.

## Author note: parallel-language submission

An independent Persian-language paper using the same corpus dataset is concurrently under consideration at *Pizhūhish-hā-yi Zabānshinākhtī-yi Qurʾān*. The two papers do not share content or cite each other; the empirical pipeline is the only shared element, and each paper presents an independent argument for its own scholarly audience.

## Ethics statement

This study uses only publicly-released text-corpus data (the Quranic Arabic Corpus, GPL-licensed; the Tanzil Quran text, CC-BY-ND 3.0). No human or animal subjects were involved at any stage. As a corpus-only philological-computational analysis, the work is exempt from human-subjects review under the standards of Urmia University and of comparable institutions.

## Author contributions

K.J. (corresponding author) conceived the project, developed the theoretical framework, conducted the lexicographic and *tafsīr*-tradition analysis, drafted the manuscript, and is responsible for the final form of the argument. A.J. contributed to the theoretical framework, the design of the computational pipeline, and editorial revision. Both authors approved the final manuscript and are jointly accountable for its content.

## Author affiliations and ORCID

**Karim Jabbary** (corresponding author). Department of Arabic Language and Literature, Faculty of Literature and Humanities, Urmia University, Urmia, Iran. *email:* k.jabbary@urmia.ac.ir.

**Ali Jabbary**. Faculty of Computer Engineering, Urmia University, Urmia, Iran. *email:* a.jabbary@urmia.ac.ir.

**ORCID:** Karim Jabbary: 0000-0000-0000-0000 (to be provided at submission). Ali Jabbary: 0000-0000-0000-0000 (to be provided at submission).

## Data and Code Availability

All code, data, concordance CSV outputs, and figure-generation scripts are released open-source at:

> [github.com/ali-kin4/quranic-emotion-spectrum](https://github.com/ali-kin4/quranic-emotion-spectrum)

The repository contains: (i) the Python pipeline under MIT License; (ii) the Quranic Arabic Corpus (Dukes 2011) under its original GPL; (iii) the complete CSV concordance for the fourteen core spectrum roots (312 attestations), distributional summaries, statistical tests, network-centrality outputs, and umbrella-cooccurrence tables; (iv) PDF and PNG versions of the figures published with this paper and with the Supplementary Material; (v) the SHA-256 hash of the QAC v0.4 source file and the manual-validation audit. The four statistical analyses of §§4.2–4.9 can be regenerated end-to-end by:

```bash
pip install -r analysis/requirements.txt
python analysis/extract_concordance.py
python analysis/advanced_metrics.py
python analysis/visualize_spectrum.py
python analysis/visualize_advanced.py
```

The four computational corroboration analyses reported in Supplementary Material S1–S4 are produced by `nlp_upgrade_colab.py`, which requires a CUDA-enabled GPU for the multilingual-MPNet and CAMeLBERT-CA inference. A Colab notebook is available in the repository with pinned model snapshots and an expected runtime of ~25 minutes on a T4 GPU; CSV outputs are committed under `outputs/nlp_upgrade/` so that reviewers can inspect the numerical results without re-running the GPU pipeline.

---

## Bibliography

References use Harvard author-date in-text citation; the Bibliography is unified and alphabetised by author surname (the Arabic article *al-* is ignored for alphabetisation, sorting on the post-*al-* letter). Persian-language and classical-Arabic entries are interleaved in the single sequence.

Agresti, A. (2013) *Categorical Data Analysis*, 3rd edn, Hoboken, NJ: John Wiley & Sons.

Akra, D., Hammouda, T. and Jarrar, M. (2025) *QuranMorph: Morphologically Annotated Quranic Corpus*, arXiv preprint 2506.18148, https://arxiv.org/abs/2506.18148.

Albayrak, I. (2020) 'Semantics of the Qurʾānic Weltanschauung: A Critical Analysis of Toshihiko Izutsu's Works', *American Journal of Islam and Society* 37(1–2).

Averill, J. R. (1982) *Anger and Aggression: An Essay on Emotion*, New York: Springer-Verlag.

Berkowitz, L. (1993) *Aggression: Its Causes, Consequences, and Control*, New York: McGraw-Hill.

Bodi, D. (2018) 'An Akkadian-Aramaic Idiomatic Expression in Ezekiel 16:30 *amūlâ libbātēk* "I am filled with anger against you", and Remarks on the Languages in Persian Times', *Transeuphratène* 50, pp. 13–38.

Cairns, D. L. (2003) 'Ethics, Ethology, Terminology: Iliadic Anger and the Cross-cultural Study of Emotion', in S. Braund and G. W. Most (eds), *Ancient Anger: Perspectives from Homer to Galen*, Yale Classical Studies 32, Cambridge: Cambridge University Press, pp. 11–49.

*Chicago Assyrian Dictionary (CAD)* (1956–2010), ed. M. T. Roth et al., 21 vols, Chicago: The Oriental Institute.

Cochran, W. G. (1954) 'Some Methods for Strengthening the Common χ² Tests', *Biometrics* 10(4), pp. 417–451.

Derki, M. (2022) 'Conceptualization of Anger in Modern Standard Arabic and English: A Comparative Study', *Professional Discourse and Communication*.

Dukes, K. (2011) *Quranic Arabic Corpus (Morphology, Version 0.4)*, Leeds: University of Leeds, https://corpus.quran.com.

El-Awa, S. M. S. (2006) *Textual Relations in the Qurʾan: Relevance, Coherence and Structure*, Routledge Studies in the Qurʾan, London and New York: Routledge.

al-Fīrūzābādī, Muḥammad. *al-Qāmūs al-Muḥīṭ*, Beirut: Muʾassasat al-Risālah.

Fauconnier, G. and Turner, M. (2002) *The Way We Think: Conceptual Blending and the Mind's Hidden Complexities*, New York: Basic Books.

Fisher, R. A. (1922) 'On the Interpretation of χ² from Contingency Tables, and the Calculation of *P*', *Journal of the Royal Statistical Society* 85(1), pp. 87–94.

Frijda, N. H. (1986) *The Emotions*, Studies in Emotion and Social Interaction, Cambridge and Paris: Cambridge University Press and Éditions de la Maison des Sciences de l'Homme.

Gaanoun, K. and Alsuhaibani, M. (2025) 'Sentiment Preservation in Quran Translation with Artificial Intelligence Approach: Study in Reputable English Translation of the Quran', *Humanities and Social Sciences Communications* 12(1), DOI: 10.1057/s41599-024-04181-0.

Gross, J. J. (1998) 'The Emerging Field of Emotion Regulation: An Integrative Review', *Review of General Psychology* 2(3), pp. 271–299.

Gross, J. J. (ed.) (2014) *Handbook of Emotion Regulation*, 2nd edn, New York: Guilford Press.

Gross, J. J. (2015) 'Emotion Regulation: Current Status and Future Prospects', *Psychological Inquiry* 26(1), pp. 1–26.

Ibn ʿĀshūr, Muḥammad al-Ṭāhir (1984) *al-Taḥrīr wa-l-Tanwīr*, Tunis: al-Dār al-Tūnisiyyah li-l-Nashr.

Ibn Fāris, Aḥmad (1979) *Muʿjam Maqāyīs al-Lughah*, ed. ʿA. M. Hārūn, Beirut: Dār al-Fikr.

Ibn Kathīr, Ismāʿīl (1999) *Tafsīr al-Qurʾān al-ʿAẓīm*, ed. S. al-Salāmah, 8 vols, Riyadh: Dār Ṭaybah.

Ibn Manẓūr, Muḥammad (1993) *Lisān al-ʿArab*, 3rd edn, Beirut: Dār Ṣādir.

Izutsu, T. (1959) *The Structure of the Ethical Terms in the Koran: A Study in Semantics*, Studies in the Humanities and Social Relations 2, Tokyo: Keio Institute of Philological Studies.

Izutsu, T. (1964) *God and Man in the Koran: Semantics of the Koranic Weltanschauung*, Tokyo: Keio Institute of Cultural and Linguistic Studies.

Izutsu, T. (2002) *Ethico-Religious Concepts in the Qurʾān*, rev. edn, Montreal: McGill-Queen's University Press (orig. 1966).

Jamison, S. W. and Brereton, J. P. (2014) *The Rigveda: The Earliest Religious Poetry of India*, 3 vols, New York: Oxford University Press.

Kassinove, H. and Tafrate, R. C. (2002) *Anger Management: The Complete Treatment Guidebook for Practitioners*, Atascadero, CA: Impact Publishers.

Kennedy, C. (1999) *Projecting the Adjective: The Syntax and Semantics of Gradability and Comparison*, Outstanding Dissertations in Linguistics, New York: Garland.

Kennedy, C. (2007) 'Vagueness and Grammar: The Semantics of Relative and Absolute Gradable Adjectives', *Linguistics and Philosophy* 30(1), pp. 1–45.

Khan, M. T. et al. (2025) 'A Literature Review on Natural Language Processing Techniques for Qurʾānic Studies: Challenges and Insights', *Frontiers in Signal Processing* 5, 1535166, DOI: 10.3389/frsip.2025.1535166.

Kövecses, Z. (1986) *Metaphors of Anger, Pride, and Love: A Lexical Approach to the Structure of Concepts*, Pragmatics & Beyond VII:8, Amsterdam: John Benjamins.

Kövecses, Z. (2000) *Metaphor and Emotion: Language, Culture, and Body in Human Feeling*, Cambridge: Cambridge University Press.

Kövecses, Z. (2010) *Metaphor: A Practical Introduction*, 2nd edn, Oxford: Oxford University Press.

Kövecses, Z., Benczes, R. and Szelid, V. (eds) (2025) *Metaphors of ANGER across Languages: Universality and Variation*, 2 vols, Comparative Handbooks of Linguistics 8, Berlin and Boston: De Gruyter Mouton.

Kruger, P. A. (2000) 'A Cognitive Interpretation of the Emotion of Anger in the Hebrew Bible', *Journal of Northwest Semitic Languages* 26(1), pp. 181–193.

Kruger, P. A. (2015) 'Emotions in the Hebrew Bible: A Few Observations on Prospects and Challenges', *Old Testament Essays* 28(2), pp. 395–420.

Lakoff, G. and Johnson, M. (1980) *Metaphors We Live By*, Chicago: University of Chicago Press.

Lakoff, G. and Kövecses, Z. (1987) 'The Cognitive Model of Anger Inherent in American English', in D. Holland and N. Quinn (eds), *Cultural Models in Language and Thought*, Cambridge: Cambridge University Press, pp. 195–221.

Landis, J. R. and Koch, G. G. (1977) 'The Measurement of Observer Agreement for Categorical Data', *Biometrics* 33(1), pp. 159–174.

Lauri, J., Svärd, S., Alstola, T., Jauhiainen, H., Sahala, A., Lindén, K., Sams, M. and Nummenmaa, L. (2024) 'Embodied Emotions in Ancient Neo-Assyrian Texts Revealed by Bodily Mapping of Emotional Semantics', *iScience* 27(12), 111365.

Lazarus, R. S. (1991) *Emotion and Adaptation*, New York: Oxford University Press.

Maalej, Z. (2004) 'Figurative Language in Anger Expressions in Tunisian Arabic: An Extended View of Embodiment', *Metaphor and Symbol* 19(1), pp. 51–75.

Maalej, Z. (2007) 'The Embodiment of Fear Expressions in Tunisian Arabic: Theoretical and Practical Implications', in F. Sharifian and G. B. Palmer (eds), *Applied Cultural Linguistics: Implications for Second Language Learning and Intercultural Communication*, Converging Evidence in Language and Communication Research 7, Amsterdam: John Benjamins, pp. 87–104.

Maalej, Z. A. and Yu, N. (eds) (2011) *Embodiment via Body Parts: Studies from Various Languages and Cultures*, Human Cognitive Processing 31, Amsterdam and Philadelphia: John Benjamins.

Marcus-Newhall, A., Pedersen, W. C., Carlson, M. and Miller, N. (2000) 'Displaced Aggression is Alive and Well: A Meta-analytic Review', *Journal of Personality and Social Psychology* 78(4), pp. 670–689.

Mehta, C. R. and Patel, N. R. (1983) 'A Network Algorithm for Performing Fisher's Exact Test in *r* × *c* Contingency Tables', *Journal of the American Statistical Association* 78(382), pp. 427–434.

al-Mostafawī, Ḥasan (1995) *al-Taḥqīq fī Kalimāt al-Qurʾān al-Karīm*, 14 vols, Tehran: Wizārat al-Thaqāfah wa-l-Irshād al-Islāmī.

Mottaghi, M. S. et al. (2024) 'A Graph-based Algorithm for Clustering Qurʾānic Surahs', *Signal and Data Processing Journal (Iran)*.

Muellner, L. C. (1996) *The Anger of Achilles: Mēnis in Greek Epic*, Ithaca, NY: Cornell University Press.

Nandan, M., Godbole, I., Kapparad, P. and Bhattacharjee, S. (2025) 'Comparative Analysis of Religious Texts: NLP Approaches to the Bible, Quran, and Bhagavad Gītā', in *Proceedings of the Workshop on New Horizons in Computational Linguistics for Religious Texts (CLRel)*, Stroudsburg, PA: Association for Computational Linguistics.

Narimani, Z., Iqbali, M. and Chari, M. (2021) 'Semantic Re-analysis of the Words *ghayẓ*, *ghaḍab*, and *sakhaṭ* in the Holy Qurʾān with an Exegetical Approach' [in Persian], *Pizhūhish-hā-yi Qurʾān va Ḥadīth* (University of Tehran) 54(1), pp. 219–239.

Neuwirth, A. (2019) *The Qur'an and Late Antiquity: A Shared Heritage*, trans. S. Wilder, Oxford: Oxford University Press.

Pakatchi, A. and Afrashi, A. (2020) *Rūykardhā-yi Maʿnā-shinākhtī dar Muṭālaʿāt-i Qurʾānī* [Semantic Approaches in Qurʾānic Studies; in Persian], Tehran: Pizhūhishgāh-i ʿUlūm-i Insānī va Muṭālaʿāt-i Farhangī.

Patefield, W. M. (1981) 'Algorithm AS 159: An Efficient Method of Generating Random *R* × *C* Tables with Given Row and Column Totals', *Journal of the Royal Statistical Society, Series C (Applied Statistics)* 30(1), pp. 91–97.

Plutchik, R. (1980) *Emotion: A Psychoevolutionary Synthesis*, New York: Harper & Row.

Plutchik, R. (2001) 'The Nature of Emotions', *American Scientist* 89(4), pp. 344–350.

Qāʾimīniyā, ʿA. (2011) *Maʿnāshināsī-yi Shinākhtī-yi Qurʾān* [Cognitive Semantics of the Qurʾān; in Persian], Tehran: Pizhūhishgāh-i Farhang va Andīshah-i Islāmī.

Qāʾimīniyā, ʿA. (2014) *Istiʿārah-hā-yi Mafhūmī wa Faḍāhā-yi Qurʾānī* [Conceptual Metaphors and Qurʾānic Spaces; in Persian], Tehran: Pizhūhishgāh-i Farhang va Andīshah-i Islāmī.

Qarizadeh, M. ʿO., Salmani Marvast, M. ʿA., Meymandi, V. and Farsi, B. (2024) 'Polysemy of the Word *ṭughyān* in the Holy Qurʾān with a Linguistic Approach' [in Persian], *Pizhūhish-hā-yi Zabānshinākhtī-yi Qurʾān* (University of Isfahan).

al-Qurṭubī, Muḥammad ibn Aḥmad (1964) *al-Jāmiʿ li-Aḥkām al-Qurʾān*, 20 vols, Cairo: Dār al-Kutub al-Miṣriyyah.

al-Qushayrī, ʿAbd al-Karīm (2000) *Laṭāʾif al-Ishārāt*, ed. I. Basūnī, 6 vols, Cairo: al-Hayʾah al-Miṣriyyah al-ʿĀmmah li-l-Kitāb.

Quṭb, S. (1980) *Fī Ẓilāl al-Qurʾān*, 6 vols, Cairo and Beirut: Dār al-Shurūq.

Rabab'ah, K. and Al-Saidat, E. (2022) 'The Conceptualization of Anger through Metaphors, Metonymies and Metaphtonymies in Jordanian Arabic and English: A Contrastive Study', *Cognitive Semantics* 8(3), pp. 409–433.

al-Rāghib al-Iṣfahānī, Ḥusayn (1992) *al-Mufradāt fī Gharīb al-Qurʾān*, ed. Ṣ. ʿA. Dāwūdī, Damascus and Beirut: Dār al-Qalam and al-Dār al-Shāmiyyah.

al-Rāzī, Fakhr al-Dīn Muḥammad (1999) *Mafātīḥ al-Ghayb (al-Tafsīr al-Kabīr)*, Beirut: Dār Iḥyāʾ al-Turāth al-ʿArabī.

Riḍā, Muḥammad Rashīd (1947) *Tafsīr al-Qurʾān al-Ḥakīm (al-Manār)*, 12 vols, Cairo: Dār al-Manār.

Roseman, I. J. (1996) 'Appraisal Determinants of Emotions: Constructing a More Accurate and Comprehensive Theory', *Cognition and Emotion* 10(3), pp. 241–277.

Sadeghi, B. (2011) 'The Chronology of the Qurʾān: A Stylometric Research Program', *Arabica* 58(3–4), pp. 210–299.

Sassoon, G. W. (2010) 'The Degree Functions of Negative Adjectives', *Natural Language Semantics* 18(2), pp. 141–181.

Sawalha, M., Al-Shargi, F., Yagi, S., AlShdaifat, A. T., Hammo, B., Belajeed, M. and Al-Ogaili, L. R. (2024) 'Morphologically-Analyzed and Syntactically-Annotated Quran Dataset (MASAQ)', *Data in Brief* 58, 111211.

Scherer, K. R. (2001) 'Appraisal Considered as a Process of Multilevel Sequential Checking', in K. R. Scherer, A. Schorr and T. Johnstone (eds), *Appraisal Processes in Emotion: Theory, Methods, Research*, New York: Oxford University Press, pp. 92–120.

Scherer, K. R. (2005) 'What Are Emotions? And How Can They Be Measured?', *Social Science Information* 44(4), pp. 695–729.

Sharaf, A.-B. M. and Atwell, E. (2012a) 'QurAna: Corpus of the Quran Annotated with Pronominal Anaphora', in *Proceedings of the Eighth International Conference on Language Resources and Evaluation (LREC'12)*, Istanbul: ELRA, pp. 130–137.

Sharaf, A.-B. M. and Atwell, E. (2012b) 'QurSim: A Corpus for Evaluation of Relatedness in Short Texts', in *Proceedings of the Eighth International Conference on Language Resources and Evaluation (LREC'12)*, Istanbul: ELRA, pp. 2295–2302.

Sharifian, F. (2011) *Cultural Conceptualisations and Language: Theoretical Framework and Applications*, Cognitive Linguistic Studies in Cultural Contexts 1, Amsterdam: John Benjamins.

Sinai, N. (2017) *The Qurʾan: A Historical-Critical Introduction*, The New Edinburgh Islamic Surveys, Edinburgh: Edinburgh University Press.

Sinai, N. (2023) *Key Terms of the Qurʾan: A Critical Dictionary*, Princeton: Princeton University Press.

Soriano, C. (2003) 'Some Anger Metaphors in Spanish and English: A Contrastive Review', *International Journal of English Studies (IJES)* 3(2), pp. 107–122.

Soriano, C. (2013) 'Anger Metaphors across Languages: A Cognitive Linguistic Perspective', in R. R. Heredia and A. B. Cieślicka (eds), *Bilingual Figurative Language Processing*, Cambridge: Cambridge University Press, pp. 410–440.

Spielberger, C. D. (1999) *Professional Manual for the State-Trait Anger Expression Inventory–2 (STAXI-2)*, Odessa, FL: Psychological Assessment Resources.

al-Ṭabarī, Muḥammad ibn Jarīr (2000) *Jāmiʿ al-Bayān ʿan Taʾwīl Āy al-Qurʾān*, ed. A. M. Shākir, 24 vols, Beirut: Muʾassasat al-Risālah.

al-Ṭabarsī, al-Faḍl ibn al-Ḥasan. *Majmaʿ al-Bayān fī Tafsīr al-Qurʾān*, Beirut: Dār al-Maʿrifah, n.d.

al-Ṭabāṭabāʾī, Muḥammad Ḥusayn (1970) *al-Mīzān fī Tafsīr al-Qurʾān*, 20 vols, Beirut: Muʾassasat al-Aʿlamī li-l-Maṭbūʿāt.

Tanzil Project (2008) *The Tanzil Quran Text* (Uthmani edition), https://tanzil.net.

Wierzbicka, A. (1999) *Emotions Across Languages and Cultures: Diversity and Universals*, Cambridge: Cambridge University Press.

Yu, N. (1995) 'Metaphorical Expressions of Anger and Happiness in English and Chinese', *Metaphor and Symbolic Activity* 10(2), pp. 59–92.

al-Zamakhsharī, Maḥmūd (1986) *al-Kashshāf ʿan Ḥaqāʾiq Ghawāmiḍ al-Tanzīl*, Beirut: Dār al-Kitāb al-ʿArabī.
