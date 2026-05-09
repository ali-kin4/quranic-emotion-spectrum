# The Phenomenology of the Anger Spectrum in the Qur’an
## A Semantic-Network Analysis of Displeasure, Inflammation, and Destructiveness Along an Action-Intensity Continuum

**Karim Jabbary** *(corresponding author)*
Department of Arabic Language and Literature, Faculty of Literature and Humanities, Urmia University, Urmia, Iran. *email:* k.jabbary@urmia.ac.ir.

**Ali Jabbary**
Faculty of Computer Engineering, Urmia University, Urmia, Iran. *email:* a.jabbary@urmia.ac.ir.

Karim Jabbary: ORCID 0000-0000-0000-0000 (to be provided at submission)
Ali Jabbary: ORCID 0000-0000-0000-0000 (to be provided at submission)

---

## Abstract

The Qur’an deploys an exceptionally articulated lexicon for the *anger spectrum*, yet existing scholarship treats it word-by-word or through normative-ethical frames. This study argues that fourteen core Arabic roots (*ʾff, krh, ḍyq, ḥzn, ʾsf, nqm, sxṭ, mqt, ġḍb, ḥrd, ġyẓ, bġy, ṭġy, ʿtw*) form a graded semantic field organised by *intensity of action* across six phenomenological stages: pre-anger displeasure, inner pressure, evaluative aversion, active anger, compressed rage, and behavioural outcomes. We integrate Izutsu's semantic-field approach, Kennedy–Sassoon scalar semantics, and Lakoff–Kövecses conceptual metaphor theory, validating the continuum against the Quranic Arabic Corpus (Dukes 2011) through a reproducible pipeline over 312 attestations. Three findings are reported under uncertainty-aware metrics. First, the asymptotic χ²(5) = 227.15 is large but a permutation null yields *p* = 0.24; the omnibus is *consistent with* rather than confirmatory of non-uniformity, the substantive case resting on qualitative evidence. Second, *sakhaṭ* attests exclusively in Medinan suras (Holm-adjusted *p* = 0.05), the sole confirmed instance of *discursive-contextual lexical specialisation*. Third, network analysis identifies *baghy* as a bridging node to the broader moral-evaluation field. Q. 67:8 (*takādu tamayyazu min al-ġayẓ*) is an unusually transparent instance of "container collapse"; a κ = 0.79-validated tafsir audit supports a *bidirectional-causation* reading of Stage 6. Implications follow for Qur’anic translation and Islamic psychology.

**Keywords:** Qur’an, anger spectrum, semantic field, cognitive linguistics, scalar semantics, conceptual metaphor, emotion regulation, Arabic corpus linguistics, Izutsu, Islamic psychology.

---

## 1. Introduction

### 1.1. Statement of the problem

The Qur’anic lexicon for the *anger spectrum* exhibits a precision that survives only with difficulty into translation. Where English versions level *uff*, *karh*, *ḍīq*, *ḥuzn*, *asaf*, *naqm*, *sakhaṭ*, *maqt*, *ghaḍab*, *ḥard*, *ghayẓ*, *baghy*, *ṭughyān*, and *ʿutuww* into a small set of broad equivalents — "displeasure," "distress," "grief," "anger," "rage," "transgression," "rebellion" — the Arabic original distinguishes them with the precision of a graded taxonomy. We advance the structural hypothesis that these fourteen Qur’anic anger-spectrum roots are not synonyms but coordinated nodes in a single *graded* semantic field, organised along *intensity of action* (*shiddat al-kunish* in the Persian original), traversing pre-anger displeasure, inner pressure and contraction, evaluative aversion, active anger, compressed/explosive rage, and — at the behavioural pole — outcomes (*baghy*, *ṭughyān*, *ʿutuww*) whose causation is bidirectional rather than purely emotional.

This claim has consequences beyond philology: it implies that the Qur’an encodes — through its lexical architecture, not by explicit theoretical statement — an implicit theory of the genealogy of moral failure, in which the social-structural pathologies the text most frequently denounces (transgression, tyranny, defiance) are *related to* and often developmentally downstream from inner experiences of irritation, dislike, constriction, and grief. As we argue in §4–§5, the relationship at the behavioural pole is *bidirectional*: anger may produce *baghy*/*ṭughyān*/*ʿutuww*, but these behaviours can equally produce anger (in their victims, the prophets, the divine response). The distance from *uff* (Q. 17:23) to *ʿutuww* (Q. 25:21) is graded rather than categorical — the distance walked, absent intervention, by an unmanaged life of irritation.

### 1.2. Aims and originality

This paper has three aims. The first is **methodological**: to demonstrate that combining Izutsu's qualitative semantic-field approach, scalar-semantic ordering in the Kennedy–Sassoon tradition, and conceptual-metaphor theory in the Lakoff–Kövecses tradition produces stronger philological claims than any of the three frameworks in isolation. To our knowledge—and we say this advisedly, given that the Persian-language Qur’anic-linguistic literature in particular is not exhaustively indexed in international databases—this trifold integration is here brought together in Qur’anic studies for the first time as a unified analytic framework over a corpus pipeline. We acknowledge that Qāʾimīniyā (1390/2011, 1393/2014) and Pakatchi already integrate Izutsu's field method with cognitive-linguistic conceptual-metaphor analysis, and that Persian-language scalar-semantic work on Qur’anic vocabulary may exist in venues we have not been able to canvass; the *novelty* of the present paper is therefore best stated as the *systematic combination* of the three frameworks within a single computational-empirical pipeline, not as the introduction of any one framework. The second aim is **descriptive**: to map every Qur’anic occurrence of the fourteen core roots, to render that map publicly verifiable through an open concordance, and to extract from it empirical regularities that previous scholarship—working in either tafsir, lexicography, or single-word semantic analysis—was not in a position to detect. The third aim is **interpretive**: to argue that the resulting continuum constitutes a coherent "logic of anger escalation" with deep structural affinities to modern psychology of emotion, and to identify the specific points at which the Qur’anic continuum *exceeds* the explanatory range of the contemporary models.

**Originality** disaggregated into three contributions with "to our knowledge" qualifications: **(i) Methodological synthesis** (moderate): the trifold integration of Izutsu's field method, Kennedy–Sassoon scalar semantics, and Lakoff–Kövecses CMT under a corpus pipeline. We acknowledge Qāʾimīniyā (1390/2011, 1393/2014) and Pakatchi-Afrashi (1399/2020) already integrate Izutsu and CMT in Persian Qur’anic scholarship; the novel element is the Kennedy–Sassoon scalar layer. **(ii) Empirical findings** (variable strength): of four distributional patterns, only the exclusively-Medinan *sakhaṭ* (raw *p* = 0.005; **Holm-Bonferroni adj. *p* = 0.05**) survives FDR — borderline rather than emphatic. *Asaf* (5/0), *naqm* (12/5), *ʿutuww* (9/1) tilts do not survive correction and are reported as contextual observations. **(iii) Interpretive contribution** (most substantive): *bidirectional-causation reading of Stage 6* via κ = 0.79-validated tafsir-coding (A = 26%, S = 49%, A+S = 25%); A-only re-analysis χ²(1) = 81.4, *p* < 0.001 with phenomenological core dominating anger-derived outcomes ~4.4×. This reconciles a puzzling distributional finding with the structurally-driven character of *baghy*/*ṭughyān*/*ʿutuww* in classical exegesis. To these add **(iv)** a fully reproducible MIT-licensed pipeline (SHA-256 pinning, permutation/bootstrap, 50/50 manual validation) and **(v)** the comparative observation that Q. 67:8 is an unusually transparent instance of "container collapse", softened in §5.5 by the absence of a cross-cultural survey.

### 1.3. Prior work and the gap

Prior scholarship clusters into five lines, each insufficient on its own to address the structural question motivating this paper. **Single-word lexical studies**: the most directly relevant Persian-language precedent — Narimani, Eghbali, and Chari (2021; *JQST* 54:1) on *ghayẓ*, *ghaḍab*, and *sakhaṭ* — establishes on tafsir grounds that *ghaḍab* is central, *sakhaṭ* reserved for divine displeasure with hypocrites, and *ghayẓ* exclusive to unbelievers/hypocrites in human-attribution contexts; we confirm and extend their findings with corpus-distributional evidence and the *kaẓm* analysis. Qarizadeh et al. (2024) on *ṭughyān* shows the root attests in 27 suras with the central meaning of transgressing the limit. Both works illustrate the present gap: high-quality lexical work for individual lexemes, no integrated continuum. **Ethics-of-anger studies** focus on *kaẓm al-ghayẓ* (Q. 3:134) and adjacent verses but are normatively rich and linguistically thin. **Cognitive-semantic studies** in the Izutsu tradition — Qāʾimīniyā (1390/2011, 1393/2014); Pakatchi-Afrashi (1399/2020); Albayrak (2020) — have applied cognitive linguistics to Qur’anic vocabulary but not treated the anger spectrum as a graded continuum. The cross-linguistic CMT literature on anger is decisively updated by *Metaphors of ANGER across Languages* (Kövecses, Benczes & Szelid eds., 2025; De Gruyter, 2 vols.); Classical Arabic is conspicuously not separately treated in Vols. 1–2, a gap this paper begins to fill. **Translation-criticism studies** are quantitative at scale in 2025: Gaanoun & Alsuhaibani (2025; *Nature HSSC*) show inconsistent sentiment polarity across seven English translations; Alsuhaibani et al.'s (2025) ELQV dataset of 2,100 emotion-labelled verses provides a coarse-Ekman reference; Khan et al. (2025; *Frontiers Signal Proc.*) survey the field; Cogent A&H 2025 catalogues flattening risks. None of these supplies a *graded reference model of the lexical spectrum* at the lexeme level. **Islamic psychology** (e.g. *IJCP* 2023 on fear/anger/sadness/shame in Qur’an-and-ḥadīth) tends to draw on *aḥādīth* and leave systematic linguistic analysis of the Qur’anic surface in the background. The present paper fills the gap at the intersection of all five lines: a unified theoretical frame, corpus-empirical validation, novel distributional findings, a translation-criticism reference model, and a culturally-grounded model for practical Islamic psychology.

### 1.4. Research questions and hypotheses

We address five research questions: (RQ1) the internal structure of the Qur’anic anger-spectrum field and its principal nodes; (RQ2) the continuum ordering by action-intensity and the theoretical framework legitimating it; (RQ3) corpus-distributional corroboration of the continuum (frequency, Meccan/Medinan, morphology, network centrality); (RQ4) structural homology with Gross, Plutchik, Spielberger, and Lazarus-Scherer appraisal theory; (RQ5) practical implications for Qur’anic translation and clinical Islamic psychology.

The principal **Qur’anic Action-Intensity Continuum Hypothesis** holds that the fourteen core roots (ʾff, krh, ḍyq, ḥzn, ʾsf, nqm, sxṭ, mqt, ġḍb, ḥrd, ġyẓ, bġy, ṭġy, ʿtw) operate as fourteen distinct grades on a single semantic continuum structured by *intensity of action*, organised in six phenomenological stages, supported by qualitative (etymological, exegetical, metaphorical) and quantitative (frequency, distribution, network) evidence. Five subsidiary hypotheses: (H1) non-uniform six-stage frequency distribution; (H2) near-equal split between phenomenological core (S1–5) and behavioural pole (S6), supporting the bidirectional Stage-6 reading; (H3) discursively-specialised exclusive-Medinan distribution of *sakhaṭ*; (H4) *baghy* as bridge node in the co-occurrence network; (H5) Q. 67:8 as transparent instance of "container collapse" CMT failure mode.

---

## 2. Theoretical Framework

### 2.1. Izutsu's semantic-field method

Toshihiko Izutsu, in three foundational works—*The Structure of the Ethical Terms in the Koran* (1959), *God and Man in the Koran* (1964), and *Ethico-Religious Concepts in the Qur’an* (1966/2002)—introduced a methodological revolution to Qur’anic studies. Drawing on the structuralist linguistics of the Trier–Weisgerber tradition and on East Asian philosophy of language, Izutsu argued that the central terms of the Qur’an—*Allāh*, *īmān*, *kufr*, *ẓulm*, *taqwā*—are not isolated propositions but nodes in a network of syntagmatic, paradigmatic, and oppositional relations. The aggregate of these relations constitutes what he called the "Qur’anic *Weltanschauung*."

Izutsu's analytic vocabulary distinguishes three layers: *focus words* are the central organising concepts of a given semantic field; *semantic fields* are the networks of mutually defining lexemes formed around focus words; and *key words* are the terms that recur across multiple fields and serve to integrate them into a single worldview. This three-layer structure has proved extraordinarily productive in subsequent Qur’anic semantic work, both in English (Saleh, Rippin) and Persian (Qāʾimīniyā 2011, 2014; Pakatchi).

For the present paper, Izutsu's framework justifies the move from atomistic single-lexeme analysis to integrated field analysis. The fourteen target roots are not chosen at random but as the field around the focus words *ghaḍab* (the central anger term) and *baghy* (the central behavioural-outcome term), with the lower-intensity cluster (*uff*, *karh*, *ḍīq*, *ḥuzn*, *asaf*) identifying the pre-anger and inner-pressure boundary of the field and *ʿutuww* its upper-intensity boundary. Yet Izutsu's framework, in its original form, is silent on a question central to our enterprise: granted that these lexemes co-belong to a field, *what is the structural relation between them within the field?* It is at this point that we require scalar semantics.

### 2.2. Scalar semantics: from network to continuum

The contemporary linguistic theory of *gradable predicates* (Kennedy 1999, 2007; Sassoon 2010) supplies the missing apparatus. A graded predicate maps to a scale characterised by three components: a *dimension* of measurement, an *ordering* on that dimension, and a unit of comparison. Scalar predicates take degree modifiers and admit comparative constructions, signalling their scalar structure. The Qur’anic anger field is precisely such a scale: the dimension is *intensity of action* (decomposable into locus, experiential intensity, scope of consequence); the ordering follows the six-stage progression; the implicit unit is the *degree of externalisation* of emotion from inner phenomenology to social rupture. Without this framework, the claim that *ghayẓ* is "more intense than" *ghaḍab* relies on tacit native-speaker intuition.

### 2.3. Conceptual metaphor theory and the container schema

Conceptual metaphor theory (Lakoff & Johnson 1980; Lakoff & Kövecses 1987; Kövecses 2000, 2010, 2025) treats metaphor as a cognitive structure that allows abstract domains (emotion) to be understood through concrete ones (container, heat). Lakoff and Kövecses (1987) established that English anger is organised around ANGER IS THE HEAT OF A FLUID IN A PRESSURIZED CONTAINER, accommodating a four-step trajectory: fluid in container → intensifying pressure → containment attempts → container collapse. Our central observation is that the Qur’anic triplet *ghayẓ–kaẓm–tamayyuz* operationalises this exact structure thirteen centuries early. *Ghayẓ* is glossed by all four authoritative lexica as "compressed contained anger" — fluid in sealed vessel. *Kaẓm*, etymologically tying off a waterskin, is the agent-internal regulation that maintains containment (Q. 3:134 *al-kāẓimīn al-ghayẓ*). *Tamayyuz* (Q. 67:8) depicts the failure mode: the container itself bursts apart. The Qur’anic verb derives from *m-y-z* (to part, sever) and figures the disintegration of the *vessel*, not (as in English *explode*, *burst*, *blow up*) the *exit* of contents — an unusually transparent instantiation of the failure-mode schema. We treat *tamayyuz* as a *manifestation* of Stage 5, not an independent core root.

### 2.4. The integrated framework

The three layers operate complementarily: Izutsu identifies field boundaries; Kennedy-Sassoon scalar semantics order members along the action-intensity dimension; CMT explains the cognitive basis of the pressurisation-collapse metaphor organising Stage 5. Each supplies what the others lack — without Izutsu, no motivation for field-coordination; without scalar semantics, no apparatus for ordering; without CMT, no cognitive grounding for the climactic *kaẓm–tamayyuz* sequence.

---


![The six-stage Qur’anic anger-spectrum continuum along the *action-intensity* axis. Node area scales with QAC attestation frequency. Stages: S1 pre-anger displeasure (*ʾff–krh*); S2 inner pressure (*ḍyq–ḥzn–ʾsf*); S3 evaluative aversion (*nqm–sxṭ–mqt*); S4 active anger (*ġḍb–ḥrd*); S5 compressed/explosive rage (*ġyẓ*; *tamayyuz* as manifestation); S6 behavioural outcomes (*bġy–ṭġy–ʿtw*) — causation *bidirectional* rather than purely downstream (§4.8.5). Mass at S6 (n=145) ≈ S1–5 (n=167); the χ²(1) = 1.55 near-balance is theoretically consistent with the bidirectional reading.](fig1_continuum.pdf){width=100%}


## 3. Methods

### 3.1. Corpus

The empirical analysis uses the **Quranic Arabic Corpus** (QAC), version 0.4, prepared by Kais Dukes at the University of Leeds and released under the GPL (Dukes 2011). The QAC provides a morphologically tagged record for each of the 128,219 segmentable units in the Qur’anic text. Every record specifies: (a) location in the form *(sūra:āya:word:segment)*; (b) surface form in Buckwalter ASCII transliteration; (c) part-of-speech tag; (d) morphological features including root, lemma, gender, number, case, and (where applicable) semantic flags. Verse text in Uthmanic *rasm* and Meccan/Medinan classification of suras are drawn from the Tanzil project (Tanzil 2008), distributed under CC-BY-ND 3.0.

### 3.2. Selection of target roots

The fourteen core roots were selected by three concurrent criteria, applied transparently and reported here so that the inventory is not vulnerable to the charge of post-hoc selection: (i) *exegetical centrality* — appearance as a focal reference in at least three of the four authoritative lexica (Ibn Fāris's *Maqāyīs*, al-Rāghib's *Mufradāt*, Ibn Manẓūr's *Lisān*, and Mostafavi's twentieth-century *Taḥqīq*); (ii) *minimum corpus frequency* of one attestation, admitting Qur’anic hapax legomena (*ḥard*, Q. 68:25) when supported by an explicit gloss in at least three of the four lexica plus consistent treatment in the four canonical tafsirs of §3.5; (iii) *thematic membership* in the anger-spectrum field without significant overlap with adjacent fields (epistemology, faith, normative ethics).

**Excluded candidate roots** (transparency): *q-h-r* (dominance/power, *al-Qahhār* divine name); *ḥ-n-q* (post-Qur’anic, ḥadīth-only); *ʿ-n-f* (adverbial harshness, not emotion); *ḍ-r-b* (polysemous, conflict-scene); *q-ṣ-w*/*q-s-y* (hardness-of-heart, epistemic-moral); *gh-l-ẓ* (adverbial harshness); *ʾ-n-f* (nominal *anf* "nose", post-Qur’anic anger sense); *š-n-ʾ* (binary loving/hating, reclassified as umbrella). *Karh* (Stage 1) is borderline — *karāha* is affective, *ikrāh* (coercion) structural; we include the affective sense and discuss the structural extension separately (§4.3.1). Five umbrella moral terms (**šnʾ, jrm, fsq, ẓlm, ʿdw**) are used for robustness (§4.9) and cross-field co-occurrence (Table 4), excluded from the principal continuum either because of inflated cardinality (*ẓlm* n=315 functions as a meta-category) or because they belong to adjacent normative-ethics fields.

### 3.3. Computational pipeline

The Python (MIT-licensed) pipeline operates in five steps: parse the QAC morphology file; filter on target roots; collapse multi-segment morphemes to surface words preserving the *(sūra:āya)* coordinate; join with sura-level metadata for Meccan/Medinan classification; emit master concordance, per-root concordances, distributional summaries, and network/centrality CSVs. The complete analysis is reproducible from a fresh clone of the repository in four commands (`pip install`, `extract_concordance.py`, `advanced_metrics.py`, `visualize_*.py`).

**Reproducibility audit (summary).** QAC v0.4 (Dukes, May 2011) is pinned by SHA-256 in the repository; minimum-version dependencies are listed in `requirements.txt`; outputs are released under MIT (code) and CC-BY 4.0 (manuscripts/figures); the 14 headline exemplar verses and a stratified 50-segment audit on the four most frequent core roots (*ḥzn*, *bġy*, *ġḍb*, *ṭġy*) returned 100% correct segment-to-root assignment against Tanzil. Full audit at `data/concordance/validation_audit.md`.

### 3.4. Quantitative analyses

Quantitative tests beyond frequency tabulation: (a) χ²(5) and χ²(1) for uniform-stage and S1–5/S6 nulls, with Cramér's *V* and Cohen's *w*, plus a marginal-preserving permutation null (10,000 perms, deterministic seed) for the omnibus; (b) three monotonic-trend tests (Spearman ρ, Mann-Kendall, Cochran-Armitage-style OLS slope); (c) two-sided exact binomials with the corpus-derived 0.74 Meccan-ayat baseline, Holm-Bonferroni step-down adjusted over the family of fourteen per-root tests, and a granular sensitivity table at baselines 0.70–0.78; (d) morphological breakdown by POS; (e) aya-level co-occurrence network (cf. Mottaghi et al. 2024) with weighted degree, betweenness, closeness, and eigenvector centrality, accompanied by non-parametric bootstrap 95% percentile CIs (1,000 ayat-resamples with replacement). The combined uncertainty-aware reporting is, to our knowledge, the most rigorous yet applied to Qur’anic computational-corpus studies; the wider 2025 cross-scripture NLP literature (e.g. Nandan et al. 2025) operates at the discourse-topic level on coarse sentiment and does not yet apply this battery at the lexeme level.

### 3.5. Qualitative analyses

Qualitative complements: (a) comparative etymology across the four authoritative lexica (Maqāyīs, Mufradāt, Lisān, Taḥqīq); (b) comparative *tafsīr* analysis on a broadened set of nine commentaries — the four primary (al-Ṭabāṭabāʾī's *al-Mīzān*, al-Zamakhsharī's *al-Kashshāf*, al-Ṭabarsī's *Majmaʿ al-Bayān*, Ibn ʿĀshūr's *al-Taḥrīr*) supplemented with al-Ṭabarī, al-Qurṭubī, Ibn Kathīr, Sayyid Quṭb, and ʿAbduh-Riḍā's *al-Manār*; for Sufi-tradition cross-checking on *kaẓm al-ghayẓ* (§4.7), al-Qushayrī's *Laṭāʾif al-Ishārāt*. Where the broader set diverges from the primary four on key claims (whether *ghayẓ* is exclusively predicated of unbelievers; whether *sakhaṭ* is exclusively directed at the *Munāfiqūn*; whether *naqm* admits a non-retributive sense), divergences are recorded in §4 and corresponding claims qualified. (c) phenomenological analysis of contextual markers (*ḍīq al-ṣadr*, *ḥuzn al-qalb*, *asaf al-nafs*, *ḍāqa dharʿan*); (d) illustrative translation-criticism on five English translations (Yusuf Ali, Pickthall, Arberry, Saheeh International, Hilali-Khan) at canonical exemplar verses (§4.10) — framed throughout as illustrative rather than systematic.

### 3.6. Validity check

To verify the integrity of the pipeline, fourteen "headline" exemplar verses—one per core root—were independently verified against the corpus output:

- Q. 17:23 (*uff*); Q. 2:216 (*karh*); Q. 15:97 (*ḍyq*); Q. 2:38 (*ḥzn*); Q. 43:55 (*asaf*); Q. 7:126 (*naqm*); Q. 47:28 (*sakhaṭ*); Q. 40:10 (*maqt*); Q. 48:6 (*ghaḍab*); Q. 68:25 (*ḥard*); Q. 3:134 (*ghayẓ*; with manifestation Q. 67:8 *tamayyuz*); Q. 42:42 (*baghy*); Q. 96:6 (*ṭughyān*); Q. 25:21 (*ʿutuww*).

All fourteen were found in the corpus output with the correct surface form and verse text matching the Uthmani edition. This validation confirms that the Buckwalter transliteration and segment-collapse algorithms operate without systematic error.

---

## 4. Findings

### 4.1. The four-lexicon etymology table

Before turning to stage-level analysis, Table 1 summarises the canonical glosses of each root across four reference lexica.

**Table 1. Comparative etymology of the fourteen core roots across the four authoritative Arabic lexica**

| Stage | Root | Maqāyīs (Ibn Fāris) | Mufradāt (al-Rāghib) | Lisān al-ʿArab (Ibn Manẓūr) | Taḥqīq (Mostafavi) |
|:-:|:----:|:---|:---|:---|:---|
| 1 | ʾ-f-f | "kalimatu taḍajjurin" (a word of vexation); the wretched of fingernail-detritus etymologically; smallest audible expression of displeasure | the lowest verbal expression of displeasure (*adnā kalimati al-taḍajjur*) | term of irritation (*taḍajjur*) directed at someone or something disliked; cf. *uffah* (sub-vocal sigh) | minimal vocal sign of inner aversion; pre-anger affective register |
| 1 | k-r-h | dislike, finding burdensome; coercion (*ikrāh*) | aversion of the soul; structurally extended to coercion | what is disliked by nature or by reason | inner *karāha* vs. structural *ikrāh* (the latter is not an emotion) |
| 2 | ḍ-y-q | constriction; absence of opening | the state of being pressed upon, contrasted with capacity (*saʿah*) | reduction of available space, from *saʿah* to *ḍīq* | inner or outer absence of expansion (*basṭ*) |
| 2 | ḥ-z-n | rough/uneven ground → heaviness of soul | sorrow as the opposite of joy (*faraḥ*) | rugged ground, then roughness of the self | affective response to perceived loss |
| 2 | ʾ-s-f | intense grief mixed with anger | extreme anger conjoined with grief | reaching the limit of grief and anger | composite of grief and proximate anger |
| 3 | n-q-m | *al-naqimah*: disapproval (*inkār*) coupled with intent to punish; cf. *intaqama min* = exact retribution from | objecting to (*ankara ʿalā*) and seeking redress (*ʿuqūbah*) against a reprehensible act | strong denunciation (*ankara ashadda al-inkār*) yoked to *ʿuqūbah*; basis of divine attribute *al-Muntaqim* | evaluative anger oriented toward retribution; cognition-grounded, action-tilted |
| 3 | s-kh-ṭ | severe aversion and ethical rejection | the opposite of *riḍā* (consent), with intensity | severe non-acceptance with judgment | declarative rejection grounded in moral assessment |
| 3 | m-q-t | the most intense form of *ibghāḍ* (Zajjāj) | aversion arising from observing a *qabīḥ* act (*al-Rāghib*) | *ashaddu al-ibghāḍ*; aversion-distance rather than approach-aggression | purely evaluative moral aversion |
| 4 | gh-ḍ-b | inner agitation and motion | the boiling of the heart's blood seeking retribution | a rising perturbation of the soul | directed emotion enabling retributive action |
| 4 | ḥ-r-d | *ḥarada*: to be angry; also the act of *qaṣd* (deliberate aim); the lexicon couples affect and intent | conjoining *ghaḍab* with *qaṣd*: anger directed by purpose, viz. denial | *ḥarada* "to act/move toward an aim with resolve while in anger"; cf. *ḥarīd* = isolated, the angry-aloof | anger weaponised through deliberate resource-denial (Q. 68:25 *aṣḥāb al-jannah*); affective + volitional + miserly composite |
| 5 | gh-y-ẓ | pressure and surge, contained | the most intense forms of contained anger | filling of the self with restrained anger | high-pressure emotional accumulation |
| 6 | b-gh-y | seeking beyond rightful bounds | overstepping the path of right | dominance through aggression | aggressive action with intent to oppress |
| 6 | ṭ-gh-y | overflow of water past its bank | crossing the permitted measure | severe transgression of the limit | rebellious shattering of normative bounds |
| 6 | ʿ-t-w | severe rebellion with arrogance | extreme self-aggrandisement in disobedience | obstinate excess attached to *istikbār* | entrenched rebellious posture (a property of moral character) |

The table shows that the ordering from *uff* to *ʿutuww* is not the construction of the present analysis but is internally encoded in the lexicographic tradition itself: the four authoritative lexica already gloss each root with progressively more externalised and structural meanings, ascending from the murmured *uff*, through inner *karāha*, *ḍīq*, and *ḥuzn*, through evaluative *naqm*/*sakhaṭ*/*maqt*, to active *ghaḍab*/*ḥard*, to compressed *ghayẓ*, and into the externalised behavioural pole at *baghy*/*ṭughyān*/*ʿutuww*.

### 4.2. Distributional summary

Table 2 reports the principal distributional facts for the fourteen core roots. The table integrates frequency, Meccan/Medinan split, and (for the roots with sufficient morphological variation) morphological profile; it forms the empirical backbone of the analyses that follow.

Figures 2 and 3 visualise the distributional profile graphically: Figure 2 reports per-root frequency and the per-stage stage-totals; Figure 3 plots the Meccan/Medinan distribution and highlights the four discursively-specialised roots (*sakhaṭ*, *asaf*, *naqm*, *ʿutuww*) discussed below. Figure 4 reports the morphological breakdown by part of speech, instantiating a verbal-to-nominal gradient across the spectrum that we develop in §4.6.1 below.

**Table 2. Distributional profile of the fourteen core roots**

| Stage | Root | Total | Meccan | Medinan | Notes |
|:-:|:-:|:-:|:-:|:-:|:--|
| 1 | ʾff (أف) | 3 | 3 | 0 | All Meccan; lowest tier of verbal displeasure |
| 1 | krh (كره) | 41 | 14 | 27 | Medinan-tilted (*p* = 0.005); twofold *karāha*/*ikrāh* |
| 2 | ḍyq (ضيق) | 13 | 9 | 4 | Inner constriction (*ḍīq al-ṣadr*; *ḍāqa dharʿan*) |
| 2 | ḥzn (حزن) | 42 | 26 | 16 | Most frequent Stage-2 lexeme; valence transversal (see §4.4.2) |
| 2 | ʾsf (أسف) | 5 | 5 | 0 | Exclusively Meccan |
| 3 | nqm (نقم) | 17 | 12 | 5 | Meccan-tilted; vengeful disapproval; cf. *al-muntaqim* |
| 3 | sxṭ (سخط) | 4 | 0 | 4 | Exclusively Medinan (*p* = 0.005); see baseline-sensitivity analysis in §4.5.2 |
| 3 | mqt (مقت) | 6 | 4 | 2 | Most intense moral aversion (Zajjāj) |
| 4 | ġḍb (غضب) | 24 | 13 | 11 | Central anger lexeme; predicated of God, prophets, believers |
| 4 | ḥrd (حرد) | 1 | 1 | 0 | Qur’anic hapax: Q. 68:25 |
| 5 | ġyẓ (غيظ) | 11 | 3 | 8 | Compressed anger; *tamayyuz* manifestation (Q. 67:8) |
| 6 | bġy (بغي) | 96 | 55 | 41 | Bridge node; bidirectional causation (see §4.8.5) |
| 6 | ṭġy (طغي) | 39 | 29 | 10 | Pharaonic; structural arrogance |
| 6 | ʿtw (عتو) | 10 | 9 | 1 | Settled defiance; properly *istikbār*-attached |
| **Σ** | — | **312** | **183** | **129** | |

Aggregating across the six stages: Stage 1 = 44; Stage 2 = 60; Stage 3 = 27; Stage 4 = 25; Stage 5 = 11; Stage 6 = 145. The asymptotic chi-squared test against the null of uniform six-stage distribution rejects (χ²(5) = 227.15, *p* < 0.001), with effect sizes Cramér's *V* = 0.38 and Cohen's *w* = 0.85 (large effect by Cohen's conventions). However, an asymptotic χ² on a six-cell distribution with one cell at *n* = 11 (Stage 5) and another at *n* = 145 (Stage 6) is not above suspicion: the chi-squared approximation requires expected counts ≥ 5 in every cell (which is met) but is *known* to be conservative under marginal imbalance (Cochran 1954). We therefore complement the asymptotic test with a **marginal-preserving permutation null**: the per-root attestation counts are held fixed and the fourteen stage labels are randomly permuted across roots (10,000 permutations, fixed RNG seed 20260509), yielding the empirical *p*-value as the fraction of permuted χ² values that meet or exceed the observed 227.15. The result is *p* = 0.24 — i.e. under random stage relabelling of the fourteen roots, a χ² statistic this extreme is not unusual, because much of the omnibus's mass derives from the fact that *baghy* alone contributes 96 attestations (versus a uniform expectation of ~52 per stage) and would inflate any single-stage cell into which it fell. We read this honestly: the asymptotic significance over-states the strength of evidence for non-uniformity on this sparse, marginally-imbalanced design, and the substantive case for the six-stage architecture rests on the qualitative lexicographic, exegetical, and metaphorical evidence developed in §4.1 and §4.3–§4.8 rather than on the omnibus *p*-value alone. We retain the asymptotic χ² as a descriptive statistic with appropriate effect-size reporting, but treat it as *consistent with* — not as *positive evidence for* — H1. A discriminating test of monotonicity, distinct from the omnibus, is reported in §4.2.1 below. A complementary chi-squared test against the null of equal split between the phenomenological core (Stages 1–5 = 167 attestations) and the behavioural-outcomes pole (Stage 6 = 145 attestations) *fails to reject* (χ²(1) = 1.55, Cohen's *w* = 0.07 — trivial effect). Because failure to reject a null is *absence of evidence of a difference* and not evidence of equality, we report this result not as positive corroboration of H2 but as a finding *consistent with* the reading developed in §4.8.5 and §5.3: the Stage-6 lexemes (*baghy*, *ṭughyān*, *ʿutuww*) are not exclusively anger-derived but stand in a *bidirectional* causal relation to the anger spectrum—anger may produce these behaviours, but the behaviours can equally produce anger (in their victims, the prophets, and the divine response). The test is, with these sample sizes, underpowered to discriminate between competing models of the Stage 1–5 ↔ Stage 6 relation; the substantive interpretation rests on the qualitative tafsir-grounded analysis of §4.8.5, not on the statistical near-balance.

#### 4.2.1. Monotonic-trend tests for the six-stage ordering

Because the χ²(5) test confirms non-uniformity but says nothing about *ordering*, we report three complementary monotonic-trend tests of stage rank against attestation frequency. (i) **Spearman rank-correlation** between stage index (1–6) and per-stage attestation count is ρ = –0.09 with two-sided asymptotic *p* = 0.85 — the count rises from S1 (44) to S2 (60), drops through S3–S5 (27, 25, 11), then jumps to S6 (145), producing a non-monotonic profile that the rank-correlation correctly identifies. (ii) **Mann-Kendall** (small-sample-robust) yields *S* = –3, *z* = –0.38, *p* = 0.71. (iii) **Cochran-Armitage-style** OLS slope of count on stage rank yields slope = 10.17, *z* = 0.85, *p* = 0.40. All three tests fail to reject the no-trend null. We read this as the expected and substantively interpretable result: the action-intensity continuum is an ordering of *semantic intensity*, not of *attestation frequency*; the Qur’an's pedagogical emphasis at the lower-intensity (S1–2) and behavioural-outcome (S6) poles is theoretically motivated rather than indexical of intensity. The non-monotonic frequency profile is precisely what one would expect if the corpus weights pre-anger and post-anger lexemes pedagogically, *because* of their hortatory function in the moral architecture of the text. The monotonicity tests are included here transparently to forestall the misreading that frequency alone validates the continuum order. The qualitative tests of ordering (lexicographic, exegetical, metaphorical) reported in §4.1 and §4.3–§4.8 are the load-bearing evidence for the continuum's structure.


![Per-root and per-stage frequency of the 312 core spectrum attestations. *Left*: per-root frequency, bar colour encoding stage. Stage 6 internal asymmetry (*bġy* 96 vs *ʿtw* 10) reflects the lexical division between distributed-aggression and obstinate-defiance (§4.8). *Right*: stage totals S1=44, S2=60, S3=27, S4=25, S5=11, S6=145. χ²(5) = 227.15 (asymptotic *p* < 0.001), but permutation null *p* = 0.24 — see §4.2. Phenomenological core (S1–5 = 167) vs Stage 6 (145): χ²(1) = 1.55, fails to reject — *consistent with* the bidirectional-causation reading of §4.8.5.](fig2_frequency_by_stage.pdf){width=95%}


![Stacked Meccan/Medinan distribution for the fourteen core roots. *Sakhaṭ* (S3) exclusively Medinan (0/4; raw *p* = 0.005, Holm-adj. 0.05) — the only root surviving FDR. *Asaf* (5/0 Meccan), *naqm* (12/5 Meccan), *ʿutuww* (9/1 Meccan) tilts contextual but not FDR-significant. *Ḥard* hapax (Q. 68:25, Meccan). The patterns instantiate *discursive-contextual specialisation* (§5.4).](fig3_meccan_medinan.pdf){width=95%}


![Morphological profile by part of speech. The left-to-right gradient shows verbal dominance at Stages 1–2 (*ḥzn* 88% verbal, *ḍyq* 62% — transient situational states), nominalisation at Stage 4 (*ghḍb* 16n/6v — stable attributable referent), and peak nominality with emerging participial forms at Stage 6 (*ṭāghūt*, *bāghin* — entrenched agent-property). The verbal→nominal gradient is independent corpus-internal evidence for the action-intensity continuum: as intensity ascends, representation reifies from *event* to *attribute* to *identity*.](fig5_morphology_stack.pdf){width=95%}


### 4.3. Stage 1 — Pre-anger displeasure

The lower bound of the continuum is occupied by two roots—*ʾ-f-f* and *k-r-h*—that mark the *pre-anger* register: vocal irritation and inner aversion respectively.

**4.3.0. *Uff* (3; all Meccan).** *Uff* (gloss: *taḍajjur*, "irritation") is the Qur’anic register's lowest verbal expression of displeasure. Its three attestations occupy paradigmatic moral positions: Q. 17:23 prohibits saying *uff* to one's parents (the *lowest* sign of displeasure morally weighted at the *highest* relational stake); Q. 21:67 places it in Abraham's mouth confronting idol-worshippers (prophetic remonstrance); Q. 46:17 ascribes it to a rebellious child reproaching believing parents (the inverse). *Uff* anchors the lower boundary of the spectrum at a register *below* anger proper but already morally accountable.

**4.3.1. *Karh* (41; 14M/27Md; raw *p* = 0.005, Holm-adj. 0.05).** *Karh* exhibits a *twofold structure*:

(a) **Inner *karāha* (dislike)** — pre-anger evaluative dislike, framed as *reformable* by Q. 2:216 (*ʿasā an takrahū shayʾan wa-huwa khayrun lakum*); the Stage-1 anger-spectrum sense. (b) **Structural *ikrāh* (coercion)** — not an emotion but a structural extension of distaste into compulsion (Q. 2:256 *lā ikrāha fī al-dīn*; Q. 16:106; Q. 24:33). We include *karh* on the strength of its *karāha* sense; *ikrāh* is a structural cognate worth noting because it shares the root and instantiates a Stage-6-like behavioural extension of distaste.

### 4.4. Stage 2 — Inner pressure and contraction

Stage 2 brings together three roots—*ḍ-y-q*, *ḥ-z-n*, *ʾ-s-f*—with 60 combined attestations. Each marks a distinct phenomenological mode within the inner-pressure family.

**4.4.1. *Ḍīq* (13; 9M/4Md).** Ibn Fāris glosses *ḍyq* as "constriction, narrowness"; al-Rāghib in opposition to *saʿah* (expansion). The root appears predominantly in the construction *ḍīq al-ṣadr* (constriction of the chest), localising the experience to the embodied site. Q. 15:97 frames it as the prophetic response to social rejection — an inner, bodily-localised pressure that does not translate into outward aggression. Al-Ṭabāṭabāʾī (*al-Mīzān* 12:195) observes the verse expresses divine *knowledge* of prophetic *ḍīq* rather than prohibition: a phenomenologically natural, theologically licit state, not a moral failing. Morphological profile: 8 verbs / 3 nouns / 1 participle — registering a transient, situationally-induced state.

**4.4.1.1. *Ḍāqa dharʿan* — inhibited aggression at Lot, Q. 11:77/80.** The compound idiom *ḍāqa bihim dharʿan* ("his arm-span tightened by them") in the Lot narrative figures *post-anger blocked aggression* — anger at action-threshold but structurally inhibited. The four-step trajectory (trigger *sīʾa bihim* → constriction *ḍyq+dharʿ* → aspirational voicing *law anna lī bikum quwwatan* → transfer of agency to the divine through the angels' arrival) shows that *ḍyq* sits at *both* poles of the spectrum: pre-anger contraction *and* upper-pressure threshold of inhibition. The Qur’anic narrative theologises inhibited aggression: when the wronged agent lacks power, divine agency completes the anger trajectory.

**4.4.2. *Ḥuzn* (42; 26M/16Md).** The most frequent and most verbal Stage-2 lexeme (37v / 5n = 88% verbal). Ibn Manẓūr preserves the etymologically primary "rugged, uneven ground" (*al-arḍ al-ġalīẓah*); the metaphorical extension figures grief as inner roughness, anticipating Kövecses's (2000) EMOTION IS A LANDSCAPE schema. Q. 2:38 places *ḥuzn* in syntagmatic pair with *khawf* and opposes both to divinely-given guidance — *ḥuzn* as the affective signature of *separation from guidance*; al-Ṭabāṭabāʾī (*al-Mīzān* 1:146) calls this foundational for *ʿilm al-nafs al-Qur’anī*. **Caveat (transversality)**: *Ḥuzn* is *not* strictly anger-derived. It has four valences — standalone grief over loss (Q. 12:84, Jacob over Joseph), externally-induced sorrow from being wronged (prophetic grief at rejection), positive moral compunction (the affective register of *tawba*), and anger turned inward when externally inhibited (closest to the Stage-2 placement here). Inclusion is justified by corpus density and proximity of (b) and (d) to the anger field, but the valence is more transversal than a single stage label admits. The 88% verbal profile reinforces the Stage-2 generalisation: inner-pressure lexemes denote transient, regulable states.

**4.4.3. *Asaf* (5; 5M/0Md).** The least frequent Stage-2 lexeme. Ibn Fāris and al-Rāghib gloss as the conjunction of grief and anger (*al-jamʿ bayna al-ḥuzn wa-l-ġaḍab*) — at the threshold between inner pressure and active anger. Q. 43:55 (*fa-lammā āsafūnā intaqamnā minhum*) frames *asaf* as the immediate causal precursor of divine retribution; al-Ṭabarsī (*Majmaʿ* 9:82) glosses *al-asaf* here as "the intense anger arising from prior grief." The exclusive-Meccan distribution (5/0; raw *p* = 0.34, adj. *p* = 1.00) is suggestive but evidentially weak — at *n* = 5 the test has very low power. Across all five attestations, *asaf* occurs in narrative passages depicting prior prophets' encounter with rejection and in the *ghaḍbān asifan* compound applied to Moses (§4.4.3.1). We register the 5/0 distribution as a *contextual observation* warranting follow-up at higher *n* (e.g. against the *ḥadīth* corpus), not as a confirmed empirical finding.

**4.4.3.1. *Ghaḍbān asifan* — sacred anger at Moses, Q. 7:150 / 20:86.** The compound *ghaḍbān asifan*, applied to Moses on his return to find the calf-worshippers, generates a three-layer dialectic: *ghaḍab* is outward/kinetic (throwing the tablets, seizing Aaron); *asaf* is inward/potential (compassionate grief over the relapse). *Asaf* grounds *ghaḍab*: absent its compassionate ground, Moses' anger would be violence; present, it is anger in service of guidance. The lexicon's pairing in a single nominal predication encodes moral-productivity-of-prophetic-anger as a structural property, not as ad-hoc apologetics.

**4.4.4. Network evidence for Stage-2 coherence.** The aya-level co-occurrence network (Figure 5) reveals that the strongest single edge connects *ḥzn* and *ḍyq* (weight 3); these two lexemes share three verses in the Qur’an, more than any other pair within the spectrum. This empirical density provides independent verification of the Stage-2 grouping. Centrality analysis (Figure 6) places *ḥzn* among the highest-degree nodes (weighted degree 5, tied with *ġḍb*).

### 4.5. Stage 3 — Evaluative aversion

Stage 3 brings together three roots—*n-q-m*, *s-kh-ṭ*, *m-q-t*—with 27 combined attestations. Each marks a distinct mode of *evaluative-aversive* response to a moral object.

**4.5.1. *Naqm* (17 attestations; 12 Meccan / 5 Medinan).** *Naqm* is the lexeme of *vengeful disapproval*: anger that is grounded in moral evaluation and oriented toward retribution. Q. 7:126 (*wa-mā naqamū minnā illā an āmannā bi-āyāti rabbinā*) is the linguistic exemplar: anger directed *at others' belief* — Pharaoh's sorcerers, on accepting Moses' message, are described as suffering Pharaonic *naqm* precisely *because* they believed. The grammatical construction *naqamū min* + (cause) is a canonical Qur’anic formula for evaluatively-grounded anger.

The lexeme also generates *al-muntaqim* ("the Avenger") as a divine attribute (Q. 32:22 and parallels), establishing a direct theological-lexical bridge from the human-affective register to the divine retributive register. Position on the spectrum: *naqm* sits between *sakhaṭ* and *ghaḍab* on the action axis. It is more action-oriented than *sakhaṭ* (which is a stable moral disapprobation) but less kinetic than *ghaḍab* (which mobilises the motor agent). The Meccan tilt (12/5) is consistent with the lexeme's frequent appearance in narrative-prophetic passages (the Pharaonic sorcerers, the people of Lot, the people of Madyan).

**4.5.2. *Sakhaṭ* (4 attestations; 0 Meccan / 4 Medinan).** Despite its low frequency, *sakhaṭ* furnishes one of the paper's principal distributional findings. The exclusive-Medinan distribution—zero Meccan attestations among four total—has a two-sided exact binomial p-value of **0.005** against the corpus-derived baseline of 0.74 Meccan probability, statistically significant at α = 0.05.

***Baseline derivation, made explicit.*** The 0.74 Meccan-rate baseline is the proportion of *ayat* (verses, not suras) classified Meccan in the QAC sura metadata, computed as `meccan_ayat ÷ total_ayat` weighted by `total_verses` per sura. We use the ayat-weighted rate rather than the sura-count rate (~0.69) because an attestation drawn at uniform random from the corpus hits an aya, not a sura; the longer Medinan suras inflate the Medinan share at the aya level. The implementation is in `analysis/advanced_metrics.py` (`_compute_meccan_baseline`).

***Granular baseline sensitivity.*** With n = 4, the inference is mildly sensitive to the baseline. We report the two-sided exact binomial p-value across the conventional range at fine resolution:

| H₀ Meccan rate | Two-sided p (k=0, n=4) | Interpretation |
|:--:|:--:|:---|
| 0.70 (lower bound; sura-count proxy) | 0.0081 | significant at α = 0.05 |
| 0.72 | 0.0061 | significant at α = 0.05 |
| **0.74 (corpus ayat-weighted; default)** | **0.0046** | **significant at α = 0.05** |
| 0.76 | 0.0033 | significant at α = 0.01 |
| 0.78 (upper bound) | 0.0023 | significant at α = 0.01 |

The conclusion is robust across the range. **Multiple-comparison adjustment** (Holm-Bonferroni over the family of 14 per-root binomials): *sakhaṭ* adjusted *p* = 0.05 (raw 0.005) — borderline rather than emphatic. *Asaf* (5/0; raw 0.34, adj. 1.00), *ʿutuww* (9/1; raw 0.47, adj. 1.00), and *karh* (raw 0.005, adj. 0.05 — tied) tilts do not survive correction. With *n* = 4 the test is underpowered; the substantive claim rests on the convergence of distributional evidence with the contextual-tafsir reading. All four *sakhaṭ* attestations are tied to the *Munāfiqūn* — Q. 47:28 (*ittabaʿū mā askhaṭa Allāh wa-karihū riḍwānahu*) is canonical. Following Narimani et al. (2021), we read *sakhaṭ* not as an instantaneous emotional surge but as sustained *ethical disapprobation*; we propose:

> **Hypothesis (Discursive Specialisation of *sakhaṭ*):** *sakhaṭ* operates as a discursively specialised lexeme, reserved for divine displeasure with the *Munāfiqūn* — agents whose *zāhir* departs from their *bāṭin*. Since the *Munāfiqūn* category is constitutively a Medinan-period phenomenon, *sakhaṭ* attests exclusively in Medinan suras. This is one instance of a general phenomenon of *discursive-contextual lexical specialisation* in the Qur’anic register.

**4.5.3. *Maqt* (6 attestations; 4 Meccan / 2 Medinan).** *Maqt* is *intense moral aversion*: the four lexica converge on *ashaddu al-ibghāḍ* (Zajjāj/al-Layth in *Tahdhīb al-Lugha*); al-Rāghib grounds it specifically in observation of a reprehensible act (*ʿan amrin qabīḥin rakibahu*), making *maqt* purely evaluative. Two contrasts with *ghaḍab*: causation (purely evaluative vs. injury/frustration-triggered); action profile (rejection-distance vs. approach-aggression). Canonical exemplars — Q. 40:10 (*maqt al-nafs* doubled), Q. 4:22 (institutional moral aversion in forbidden marriages), Q. 35:39 (rising divine *maqt* against disbelievers), Q. 61:3 (saying-without-doing) — stabilise the lexeme as the Qur’anic register's term for moral aversion as evaluative response, distinct from the kinetic-motor *ghaḍab* of Stage 4.

### 4.6. Stage 4 — Active anger

Stage 4 (25 attestations) covers active, motor-mobilising anger.

**4.6.1. *Ghaḍab* (24; 13M/11M).** The central anger lexeme of the Qur’an, with near-balanced Meccan/Medinan distribution marking it as the unmarked default. The four lexica gloss it as inner agitation of the heart oriented toward retribution (al-Rāghib) or inner motion disposing the agent to action (Ibn Fāris). Predicated balance-fully of God (Q. 48:6), prophets, and believers. Morphologically nominal (16 n / 6 v / 2 ptcp = 67% nominal vs *ḥuzn*'s 88% verbal): *ghaḍab* is a *structural concept-state* with organisational ontological standing rather than a transient affect. Al-Fakhr al-Rāzī's *Mafātīḥ al-Ghayb* glosses divine *ghaḍab* as *irādat inzāl al-ʿiqāb* — a normative-juridical orientation, not an emotional response. Network analysis places *ghḍb* among the top three for betweenness centrality (point estimate 0.17), with notable edges to *ġyẓ* (upward transition to S5), *ḥzn* (downward S2 link), and *bġy* (S6 link).

**4.6.3. *Ḥard* (Q. 68:25, hapax).** A Qur’anic hapax in the Garden-Owners parable (*wa-ghadaw ʿalā ḥardin qādirīn*): garden-owners who vow in the night to harvest before dawn so as to deny the poor their share. Classical exegesis converges on a dual gloss: al-Ṭabarsī's *Majmaʿ al-Bayān* reads *ḥard* as both *ghaḍab* (anger) and *qaṣd* (purposive intent); al-Ṭabāṭabāʾī's *al-Mīzān* refines as anger-plus-deliberate-denial — purposive anger weaponised through resource-denial. *Ghaḍab* mobilises the motor agent outward; *ḥard* mobilises toward deliberate, miserly withholding — anger that strips the world of what it is owed. The narrative consequence is the destruction of the garden by night-storm: divine retribution against the *ḥard*-driven plan to deny. A single attestation thus serves as linguistic anchor for an entire moral-psychological category.

### 4.7. Stage 5 — Compressed/explosive rage

**4.7.1. *Ghayẓ* and the *kaẓm* metaphor (11 attestations; 3M/8Md).** The four lexica converge: *ghayẓ* is "compressed contained anger" (al-Rāghib), "the highest concentration of restrained anger" (Mostafavi), "filling of the self with restrained anger" (Ibn Manẓūr) — pressurised contents of a sealed vessel. Q. 3:134 commends *al-kāẓimīn al-ghayẓ*; the verb *kaẓm* derives from the act of tying off a waterskin, the agent-internal regulation that sustains containment. Read through Lakoff & Kövecses (1987), the *ghayẓ–kaẓm* pair instantiates ANGER IS A PRESSURIZED CONTAINER with precision: *ghayẓ* the contained fluid, *kaẓm* the seal (Figure 7). The Medinan tilt (8/3) tracks the discursive context: inner anger management becomes a salient pedagogical concern in the formative Medinan community facing internal *Munāfiq* and external Quraysh hostility.

**4.7.2. *Tamayyuz*: container collapse in Q. 67:8 (manifestation, not separate root).** Q. 67:8 — *takādu tamayyazu min al-ġayẓ* ("[the fire] is on the verge of bursting apart from rage") — is the single most articulated image of rage in the Qur’an. *Tamayyaza* (root *m-y-z*: to part, sever) figures not the *exit* of pressurised content (as in English *she blew her top*, *he exploded*, *I lost it*) but the *structural integrity of the container itself failing*. We treat *tamayyuz* as a manifestation of Stage 5 rather than a distinct core root, retaining the fourteen-root inventory. H5 is corroborated in the form: Q. 67:8 instantiates the container-collapse failure mode with greater lexical transparency than the English exemplars in Lakoff and Kövecses's (1987) corpus; whether this is the strongest historical instance is left open pending the cross-cultural philological survey we commend in §5.5.

### 4.8. Stage 6 — Behavioural outcomes (with caveats)

**4.8.1. *Baghy* (96; 55M/41Md).** The most frequent lexeme of the spectrum and the principal bridge node by point-estimate centrality. Glossed as "seeking beyond rightful bounds" (al-Rāghib) and "aggressive seeking with intent to oppress" (Mostafavi). Q. 42:42 collocates *baghy* with *ẓulm*, embedding it in the moral-evaluation register. Ibn ʿĀshūr clarifies (*al-Taḥrīr* 25:126): *baghy* and *ẓulm* are near-synonymous, except *baghy* is specific to non-rightful aggression against another while *ẓulm* covers all injustice.

**4.8.2. *Baghy* as bridge node (with bootstrap uncertainty).** *Baghy* attains the highest point-estimate closeness centrality (0.55) and is tied with *ghaḍab* (0.53) and *asaf* (0.49) for the highest betweenness centrality (0.15). Bootstrap 95% percentile CIs (1,000 ayat-resamples) are wide — for *baghy*: betweenness ∈ [0.00, 0.31]; closeness ∈ [0.23, 0.84]; eigenvector ∈ [0.00, 0.68] — reflecting the small graph (14 nodes) and modest edge density. On strict non-overlap, no node's centrality is significantly greater than another's. The bridging-role claim must therefore be qualified: *baghy* leads on three of four point-estimate measures, but the bootstrap does not rule out alternatives. What is *robust* at the aggregate level is the cross-field connectivity to the umbrella moral terms (Table 4): *baghy* shows 16 aya-level co-occurrences with *ẓlm/jrm/fsq/ʿdw/šnʾ* combined (8 with *ʿdw*, 4 with *ẓlm*), an integer-count pattern independent of centrality ranking. H4 is *consistent with* point estimates, qualified by bootstrap.

**Table 4. Cross-field co-occurrence of spectrum roots with umbrella moral terms (aya-level)**

Cross-field ties for the original ten-root analysis (preserved here from the prior pipeline run; ties for the four newly-incorporated roots — *ʾff*, *naqm*, *maqt*, *ḥard* — are sparse and dominated by zeros, given their low corpus frequency, and are omitted from this summary table without affecting the overall pattern):

| Root | šnʾ | jrm | fsq | ẓlm | ʿdw | Total |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| ḍyq | 0 | 0 | 0 | 0 | 0 | 0 |
| ḥzn | 0 | 0 | 0 | 1 | 1 | 2 |
| ʾsf | 0 | 0 | 0 | 1 | 1 | 2 |
| sxṭ | 0 | 0 | 0 | 0 | 0 | 0 (krh-tie excluded since *krh* is now in the spectrum) |
| ġḍb | 0 | 0 | 0 | 2 | 3 | 5 |
| ġyẓ | 0 | 0 | 0 | 0 | 1 | 1 |
| **bġy** | **1** | **1** | **2** | **4** | **8** | **16** |
| ṭġy | 0 | 0 | 0 | 2 | 1 | 3 |
| ʿtw | 0 | 0 | 0 | 0 | 0 | 0 |

The radical concentration of cross-field ties at *baghy* is striking. Of the total cross-field ties across the fourteen spectrum roots, 19 (~53%) involve *baghy*. *Baghy* thus serves as the principal lexical bridge between the emotional and the broader moral-evaluation field of the Qur’an.

**4.8.3. *Ṭughyān* (39 attestations; 29 Meccan / 10 Medinan).** Root *ṭ-gh-y* derives from water flooding past its banks. Q. 96:6–7 (*kallā inna l-insāna la-yaṭghā an raʾāhu staġnā*) compresses a psychology of rebellion into a conditional: *ṭughyān* arises from the appraisal of *istighnāʾ* (self-sufficiency) — structurally an appraisal-theoretic claim, congruent with Lazarus (1991) and Scherer (2001, 2005), and aligning with Roseman's "agency-self / motive-inconsistent / high-control" pattern. Qarizadeh et al.'s (2024) polysemy analysis notes the cognitive structure; we identify *ṭughyān* as the cognitive-appraisal node of Stage 6.

**4.8.4. *ʿUtuww* (10 attestations; 9 Meccan / 1 Medinan).** The most extreme lexeme — "obstinate excess" (Ibn Manẓūr), "extreme self-aggrandisement in disobedience" (al-Rāghib). Q. 25:21 collocates *ʿatū ʿutuwwan kabīrā* with *istakbarū fī anfusihim*: rebellion crystallised into existential posture. Strong Meccan distribution (9/1; raw *p* = 0.06; Holm-adjusted *p* = 1.00) is consistent with its rhetorical function as terminal designation for Nūḥ-, ʿĀd-, Thamūd-, and Pharaonic-people narratives, but does not survive FDR correction.

**4.8.5. Bidirectional causation and a tafsir-grounded audit.** *Baghy* arises frequently from greed and *ʿulw fī al-arḍ* (cf. Q. 6:21); *ṭughyān* — paradigmatically Pharaonic (Q. 79:17) — is rooted in structural arrogance, with Q. 26:55 (*innahum lanā la-ghāʾiẓūn*) reversing polarity to show oppressor-anger arising *from* the rebellion of the oppressed; *ʿutuww* attaches to *istikbār* as settled character. The causation arrow is therefore *bidirectional*. To operationalise this, each of the 145 Stage-6 attestations was coded against the joint reading of *al-Mīzān*, *al-Kashshāf*, *Majmaʿ al-Bayān*, and *al-Taḥrīr wa-l-Tanwīr*: **A** (anger-derived), **S** (structurally derived: greed/*istikbār*/*ʿulw* without explicit anger antecedent), or **A+S** (joint). Coding by the corresponding author with second-coder verification on a 20% subsample (κ = 0.79; full coding at `data/concordance/stage6_causation_coding.csv`). Results: A = 38 (26%), S = 71 (49%), A+S = 36 (25%); by root, *baghy* 22A/50S/24A+S, *ṭughyān* 11A/19S/9A+S, *ʿutuww* 5A/2S/3A+S. Re-running χ²(1) on A-only (Stages 1–5 = 167 vs. anger-derived Stage-6 = 38) yields χ²(1) = 81.4, *p* < 0.001 — the phenomenological core dominates anger-derived outcomes ~4.4×. The full-Stage-6 near-balance (χ²(1) = 1.55) is therefore explained: S-attestations belong to an adjacent moral-anthropological field of *ẓulm-istikbār-ʿulw* that the corpus pervasively documents, and *baghy*/*ṭughyān*/*ʿutuww* are not coextensive with "anger outcomes" in the strict sense.


![Aya-level co-occurrence network of the fourteen core roots; edges weighted by shared-ayat count. Strongest edge *ḥzn–ḍyq* (weight 3) corpus-validates the Stage-2 grouping (Q. 11:12, Q. 6:33). *Baghy* anchors the right cluster with edges to the moral-evaluation lexicon (*ẓlm/jrm/fsq*). Transitive structure (no direct S1→S6 edges; mediation through S2–S5) is consistent with both the action-intensity gradient and the bidirectional Stage-6 reading (§4.8.5).](fig4_cooccurrence.pdf){width=95%}


![Three centrality measures with bootstrap 95% percentile CIs on the aya-level co-occurrence graph: (a) weighted degree, (b) betweenness, (c) closeness. *Baghy*: highest closeness point-estimate (0.55, CI [0.23, 0.84]) and shared-highest betweenness (0.15, CI [0.00, 0.31]) with *ghaḍab* and *asaf* — pivotal between the anger spectrum and the wider moral-evaluation field (315 *ẓulm*, 66 *jurm*, 54 *fisq*, 106 *ʿadāwah*). Wide CIs reflect the small graph; bridging-role claim consistent with point estimates, qualified by bootstrap (§4.8.2). *Ḍyq* and *ḥzn* (S2) high-closeness despite low frequency — inner-pressure cluster structurally central. Layered reading: S2 affective core, S6 structural bridge, S3–5 mediation.](fig7_centrality.pdf){width=95%}


### 4.9. Robustness checks: the umbrella moral terms

For robustness, the umbrella roots were extracted and analysed (note that *karh*, formerly an umbrella term, is now incorporated into the spectrum at Stage 1 and is reported in Table 2). Distributions of the remaining five (Table 5) confirm that the spectrum's structure is not artefactual.

**Table 5. Distribution of umbrella moral terms**

| Root | Total | Meccan | Medinan | Binomial p | Interpretation |
|:----:|:-:|:-:|:-:|:-:|:---|
| šnʾ | 3 | 1 | 2 | — | n too small for inference |
| jrm | 66 | 60 | 6 | < 0.0001 | Strongly Meccan; anti-*shirk* polemic |
| fsq | 54 | 20 | 34 | 0.0007 | Significantly Medinan; community-discipline register |
| ẓlm | 315 | 211 | 104 | — | Pervasive meta-category; cannot anchor a single point |
| ʿdw | 106 | 47 | 59 | 0.008 | Tilts Medinan; the lexeme of mutual antagonism |

The opposing patterns of *jrm* (strongly Meccan) and *fsq* (significantly Medinan) instantiate the same discursive-contextual specialisation that we identified for *sakhaṭ*. The umbrella analysis thus confirms a *general* phenomenon, of which the *sakhaṭ* finding is one specific instance.

### 4.10. Comparative translation analysis (illustrative sample)

To illustrate how the spectrum's intensity differentiation fares in translation, Table 6 compares five English translations on four canonical verses. We frame this as an *illustrative* case, not a systematic translation-criticism evaluation: a properly powered evaluation would require a stratified random sample of all 312 attestations (or, more practically, ~30 verses sampled across the six stages with inter-rater coding by trained Arabist coders). The four-verse, five-translation sample here suffices to register the *pattern* of levelling but does not, on its own, support the strong translation-recommendation set in §5.6; the recommendations there are conditional on a follow-up evaluation that we commend to future work.

**Table 6. Translation of four canonical verses across five English translations** (illustrative sample; n = 4 verses × 5 translations = 20 cells)

| Term & verse | Yusuf Ali | Pickthall | Arberry | Saheeh Intl. | Hilali-Khan |
|:----:|:---|:---|:---|:---|:---|
| *ḍīq* (Q. 15:97) | "thy heart is distressed" | "thy bosom is at times oppressed" | "thy breast is straitened" | "your chest is constrained" | "your breast feels tight" |
| *ġayẓ* (Q. 3:134) | "restrain anger" | "control their wrath" | "restrain their rage" | "suppress anger" | "repress anger" |
| *tamayyuz* (Q. 67:8) | "almost burst with fury" | "almost burst with rage" | "well-nigh bursts asunder with fury" | "almost bursts with rage" | "almost bursts up with fury" |
| *ṭughyān* (Q. 96:6) | "transgresses all bounds" | "rebelleth" | "waxes insolent" | "transgresses" | "transgresses (boundary)" |

Two illustrative observations emerge from this small sample. First, the rendering of *ġayẓ* in Q. 3:134 collapses the *ghaḍab/ġayẓ* distinction in all five translations—the English versions render *ġayẓ* with terms (*anger*, *wrath*, *rage*) that are also routinely used for *ghaḍab*. The differentia—the *containment* dimension of *ġayẓ*—is preserved only via the contextual verb of restraint, not in the lexeme itself. Second, the rendering of *tamayyuz* in Q. 67:8 is uneven: Arberry's "well-nigh bursts asunder" preserves the *structural-disintegration* component of the source; the others render it variationally as *burst with* + emotion, foregrounding the exit of contents but losing the structural-collapse implication. These observations are *suggestive of* a systematic levelling pattern but are not on their own evidentially decisive; we register them as motivating the systematic translation evaluation we commend in §6.3.

---

## 5. Discussion

### 5.1. The integrated logic of escalation

The findings cohere into a single structural claim: the Qur’anic lexicon of the anger spectrum encodes a **logic of anger escalation** that operates simultaneously along three dimensions—locus (inner → outer), intensity (low → high), and scope (individual → structural). The six stages instantiate this trifold transformation. The lexemes are not synonyms; they are *grades*, ordered by an intelligible cognitive logic.

In compact form: *Pre-anger displeasure → Inner pressure → Evaluative aversion → Active anger → Compressed rage → Behavioural outcomes (with caveats)*. The arrows index not mere temporal succession but conditional intensification at each step where regulation may succeed or fail. The Stage 6 step is, however, distinctive: the move into behavioural outcomes is *not* a deterministic escalation from anger but is influenced by independent vectors (greed, *istikbār*, structural arrogance), which is why we read the near-balance between Stages 1–5 (167) and Stage 6 (145) as theoretically informative rather than paradoxical.

### 5.2. Convergence with contemporary emotion psychology

The Qur’anic stages map onto Gross's (1998, 2014, 2015) process model of emotion regulation, with the Qur’anic spectrum partitioning more finely on the affective side and adding an explicit behavioural-outcomes register: Stage 1 (pre-anger *uff/karh*) ↔ antecedent-focused situation selection; Stage 2 (*ḍīq/ḥuzn/asaf*) ↔ situation modification; Stage 3 (*naqm/sakhaṭ/maqt*) ↔ attentional deployment / cognitive change; Stage 4 (*ghaḍab/ḥard*) ↔ response selection; Stage 5 (*ghayẓ*/*kaẓm*; *tamayyuz*) ↔ response modulation and containment failure; Stage 6 (*baghy/ṭughyān/ʿutuww*) — where Gross's model becomes silent and the Qur’an adds the moral anthropology of structural-moral pathologies that may be downstream from anger but, with bidirectional causation, may also be upstream of it.

The Qur’anic lexicon also realises an STAXI-style trichotomy (Spielberger 1999): trait-like sustained states (*ḥuzn*, *ḍīq*), state-like situational responses (*sakhaṭ*, *maqt*, *ghaḍab*), and deliberate restraint (*kaẓm*) — three axes contemporary psychometrics has independently isolated. Plutchik's (1980, 2001) annoyance → anger → rage three-level wheel maps onto Stages 1–5 but stops at the regulatory boundary; Stage 6 is the Qur’an's substantive extension into the morally-anthropological. Appraisal theory (Frijda 1986; Lazarus 1991; Roseman 1996; Scherer 2001, 2005) holds that emotions arise from cognitive evaluations rather than raw stimuli; Q. 96:6–7 conditions *ṭughyān* on the appraisal of *istighnāʾ* (perceived self-sufficiency) — a textbook appraisal-theoretic claim aligning with Roseman's "agency-self / motive-inconsistent / high-control" pattern. The Qur’anic lexicon thus encodes — as architectural design rather than explicit theoretical statement — insights contemporary emotion science has reached independently.

### 5.3. The phenomenology/outcomes balance

A naive ten-root reading once suggested 2.4× more attestations at the behavioural pole than at Stages 1–3 combined, indicating discursive over-emphasis on outcomes. The revised fourteen-root inventory (167 / 145; χ²(1) = 1.55, fail to reject) tells a different story: the expanded phenomenological vocabulary (*uff*, *karh*, *naqm*, *maqt*, *ḥard*) brings the lower stages into corpus-distributional balance with Stage 6, exactly as one would expect if (i) the phenomenological side is richer than the prior analysis allowed, and (ii) Stage-6 lexemes are not exclusively anger-derived but stand in bidirectional causal relation to anger. The methodological lesson: corpus-distributional analyses of religious texts are maps of *discursive emphasis*, fundamentally entangled with category-membership and category-causation decisions; the 10/4 → 14/6 shift changed both the empirical pattern and its interpretation.

### 5.4. Discursive-contextual specialisation

The FDR-surviving Medinan exclusivity of *sakhaṭ*, alongside the contextual-only Meccan tilts of *asaf*, *naqm*, and *ʿutuww*, the hapax-Meccan *ḥard*, the Medinan tilt of *karh*, and the strong umbrella patterns *jrm* (Meccan) and *fsq* (Medinan), instantiate **discursive-contextual specialisation**: members of multi-lexeme semantic fields preferentially attaching to specific discursive registers. The pattern is not random — *sakhaṭ* attaches to the *Munāfiqūn* (a Medinan phenomenon), *asaf* to prior-prophet narratives (Meccan-rhetorical), *jrm* to anti-*shirk* polemic (Meccan), *fsq* to intra-community discipline (Medinan). El-Awa (2006) on textual relations and Sinai (2017, 2023) on Meccan/Medinan diachrony supply the theoretical framework: specialisation is exactly the kind of pattern one would expect from the Qur’an's gradual response to evolving sociolinguistic contexts. The phenomenon is, to our knowledge, undocumented as a systematic corpus-distributional pattern in Qur’anic-linguistic scholarship; future work should test the generalisation across other multi-lexeme fields, in dialogue with QurAna/QurSim (Sharaf & Atwell 2012) and the QuranMorph (2025) and MASAQ extensions of the Dukes corpus.

### 5.5. Q. 67:8 and the container metaphor

Q. 67:8 (*takādu tamayyazu min al-ġayẓ*) instantiates the ANGER IS PRESSURIZED CONTAINER metaphor with unusual transparency: where English idioms (*explode*, *blow one's top*, *lose it*) report the *exit* of contained content, *tamayyaza* (m-y-z: to part, to sever) lexicalises *the structural disintegration of the vessel itself*. We frame this claim conservatively: assessing whether Q. 67:8 is the *most* articulated instance in the historical record requires a comparative survey of pre-modern Greek (Homeric *kholos*, *menis*), Akkadian (*ezzu*, *libbāti malû*), Sanskrit (*krodha*, *manyu*), Hebrew (*ḥēmâ*, *ʾaph*-idioms), and pre-Islamic *Jāhilī* poetry — a survey beyond the scope of the present paper that we commend to specialists. The Qur’anic data are *consistent with* CMT's universalist claim that bodily-grounded image schemas (CONTAINER, FORCE) underwrite emotion conceptualisation across cultures, while extending the empirical base to seventh-century Arabic; they do not, on their own, establish the strong cross-cultural universalism that earlier formulations of this paper risked overstating. The two-volume *Metaphors of ANGER across Languages* (Kövecses, Benczes & Szelid eds. 2025; De Gruyter), conspicuously omitting Classical Arabic from its language coverage, is the natural framework against which the present analysis should be situated.


![The ANGER-IS-A-PRESSURIZED-CONTAINER schema (Lakoff & Kövecses 1987), instantiated by *ghaḍab → ghayẓ + kaẓm → tamayyuz*. **Panel 1** (S4): *ghaḍab* — open container, affect dissipating into language. **Panel 2** (S5, Q. 3:134): *ghayẓ* — fluid sealed by *kaẓm* (etymologically the tying-off of a waterskin). **Panel 3** (S5 manifestation, Q. 67:8): *tamayyuz* — structural failure; *m-y-z* "to part, sever" figures the splitting of the container itself, not (as English *explode*) the exit of contents. The Qur’anic instantiation is, on the conservative claim of §5.5, *unusually transparent* relative to the English exemplars in Lakoff and Kövecses's corpus.](fig6_metaphor_diagram.pdf){width=100%}


### 5.6. Implications for Qur’anic translation (conditional on follow-up evaluation)

Translation criticism of the Qur’an has long observed that translations tend to level the spectrum—that *ġaḍab* and *ġayẓ* alike become *anger*; that *baghy*, *ṭughyān*, and *ʿutuww* alike become *transgression* (Table 6). Our four-verse, five-translation illustrative sample (§4.10) is consistent with this pattern but is too small (*n* = 4 verses × 5 translations = 20 cells) to support strong prescriptive claims; recent computational work — notably Gaanoun & Alsuhaibani (2025; *Nature HSSC*) on sentiment preservation across seven English translations and Alsuhaibani et al.'s (2025) ELQV emotion-labelled dataset of 2,100 Qur’anic verses — has begun to operationalise the levelling concern at scale on coarse Ekman categories, though without a graded reference model of the lexical spectrum against which the levelling could be benchmarked. We frame the present discussion as **conditional implications**: contingent on a follow-up systematic evaluation (a stratified random sample of ~30 verses across the six stages, with multi-rater coding against the spectrum reference model), the analysis would *if confirmed* support the following candidate equivalents for critical and study-edition translations:

> *uff*: vocal sigh of irritation · *karh* (*karāha*): inner dislike · *karh* (*ikrāh*): coercion (a structural extension, not an emotion) · *ḍīq*: inner constriction · *ḍāqa dharʿan*: arm-span tightening / inhibited aggression · *ḥuzn*: persistent grief (transversal valence) · *asaf*: regretful dismay (with anger) · *naqm*: vengeful disapproval · *sakhaṭ*: moral disapprobation · *maqt*: intense moral aversion · *ghaḍab*: anger · *ḥard*: anger combined with deliberate denial · *ghayẓ*: contained / boiling rage · *tamayyuz min al-ġayẓ*: bursting from rage · *baghy*: aggressive transgression · *ṭughyān*: rebellious overflow · *ʿutuww*: obstinate defiance.

A second conditional implication, which we register as a hypothesis rather than a recommendation, is that pedagogical translations may benefit from marking each lexeme's position on the continuum (by inline gloss, footnote, or chromatic coding) — but the empirical case for this rests on the comparative comprehension study we commend to future work. The 30-verse stratified evaluation, paired with an inter-rater coded comparison across the present spectrum reference model and the ELQV labels, is a natural Phase II for the present dataset.

### 5.7. Implications for Islamic psychology

The continuum offers a culturally-grounded framework mapping onto Gross's model without importation of secular vocabulary, with three conceptual implications: **(i) Prevention** — early-stage recognition through indigenous Stages 1–2 lexicon (*uff*, *karāha*, *ḍīq*, *ḥuzn*) supports CBT-style interception of affective dysregulation; **(ii) Crisis intervention** — the *kaẓm* construct integrates with contemporary suppression-and-reappraisal techniques; **(iii) Rehabilitation** — the post-failure Stage 6 is framed as recoverable through *tawba*, providing motivational reinforcement for anger-disorder and post-violent-trauma rehabilitation. These implications are conceptual; their translation into validated clinical interventions awaits empirical studies we recommend as a priority for future work.

---

## 6. Conclusion

### 6.1. Substantive contributions

This paper has advanced three contributions to the scholarship.

**Methodologically**, we have demonstrated that the integration of three previously separate frameworks—Izutsu's semantic-field analysis, Kennedy–Sassoon scalar semantics, and Lakoff–Kövecses conceptual-metaphor theory—coupled with a reproducible computational pipeline over the Quranic Arabic Corpus, produces a research apparatus stronger than the sum of its parts. To our knowledge, this trifold integration with corpus-empirical validation has not previously been deployed in Qur’anic studies as a unified analytic framework, although Qāʾimīniyā (1390/2011, 1393/2014) and Pakatchi have integrated Izutsu and conceptual-metaphor theory, and Persian-language scalar-semantic work on Qur’anic vocabulary may exist in venues we have not been able to canvass. The research apparatus is openly available and applicable to other Qur’anic semantic fields.

**Descriptively**, we have produced an exhaustive, reproducible concordance of 312 attestations across the fourteen core spectrum roots, with corresponding distributional and network-analytic outputs. The CSV outputs — including FDR-adjusted binomial tests, marginal-preserving permutation null *p*-values, and bootstrap 95% CIs on every centrality estimate — provide a foundation on which further philological and computational work can build.

**Theoretically**, we have formulated and empirically defended the **Qur’anic Action-Intensity Continuum Hypothesis**: the claim that fourteen core lexemes of the Qur’anic anger-spectrum field operate as a single graded continuum structured by *intensity of action* and partitioned into six phenomenologically meaningful stages. The hypothesis is supported by qualitative evidence from the four authoritative lexica and from a now-broadened tafsir consultation (§3.5), and by quantitative evidence from frequency, distribution, morphology, and network structure. We have, in addition, identified distributional patterns that, to our knowledge, have not been previously reported as a coordinated set, while reporting their post-FDR evidential strength transparently: the exclusively-Medinan *sakhaṭ* survives Holm-Bonferroni correction at α = 0.05 *borderline* (raw *p* = 0.005, adjusted *p* = 0.05) and is robust across baselines 0.70–0.78; the exclusively-Meccan *asaf*, the Meccan-tilted *naqm*, the hapax-Meccan *ḥard*, and the Medinan-tilted *karh* are reported as *contextual observations* warranting follow-up rather than as confirmed findings. The general phenomenon of **discursive-contextual lexical specialisation** of which we hypothesise these are instances is proposed as a research target rather than as a settled result. We have entered explicit caveats on the bidirectional causation of the Stage-6 lexemes (§4.8.5), grounded in a κ = 0.79-validated tafsir-coding audit, and argued that Q. 67:8 furnishes an *unusually transparent* linguistic exemplar of "container collapse"—a comparative claim whose strong universalist form is reserved pending the cross-cultural philological survey we commend in §5.5 and §6.3.

### 6.2. Answers to the research questions

**RQ1.** The semantic field is a fourteen-node network organised around the bridge node *baghy* and the stage-internal hubs *ḥuzn* and *ghaḍab*, with several specialised peripheral nodes (*sakhaṭ*, *asaf*, *ḥard*, *ʿutuww*) exhibiting marked distributional asymmetries.

**RQ2.** The fourteen nodes order on a six-stage continuum—pre-anger displeasure (Stage 1), inner pressure & contraction (Stage 2), evaluative aversion (Stage 3), active anger (Stage 4), compressed/explosive rage (Stage 5), behavioural outcomes with caveats (Stage 6)—organised by the composite dimension of *intensity of action* (locus, intensity, scope of consequence).

**RQ3.** The empirical distribution is *consistent with* (though not by itself confirmatory of) the continuum: the asymptotic chi-squared rejects the null of six-stage uniform distribution (χ²(5) = 227.15; large effect size at Cohen's *w* = 0.85), but a marginal-preserving permutation null on the same statistic yields *p* = 0.24, indicating that the asymptotic *p*-value over-states the evidence on this sparse, marginally-imbalanced design; the substantive case for the six-stage architecture rests on the qualitative lexicographic, exegetical, and metaphorical evidence rather than on the omnibus *p*-value alone. The comparison between Stages 1–5 and Stage 6 *fails to reject* equal split (χ²(1) = 1.55, Cohen's *w* = 0.07, trivial effect); we read this as *consistent with* — but not as positive evidence for — the bidirectional-causation reading of Stage 6, with the substantive support coming from the κ = 0.79-validated tafsir-coding audit (§4.8.5). The network exhibits a bridging-role profile at *baghy* with wide bootstrap confidence intervals reported transparently. The morphological profile distinguishes the verbal Stages 1–2 from the more nominal Stage 6.

**RQ4.** The continuum is structurally homologous with Gross's process model, Plutchik's wheel, Spielberger's STAXI, and Lazarus–Scherer appraisal theory in its psychological component, but extends beyond all of them by integrating the post-failure structural-moral consequences of unmanaged emotion (Stage 6) — while qualifying that integration with the bidirectional-causation caveat of §4.8.5.

**RQ5.** *Conditional* practical implications include candidate distinct-equivalent translations and position-marking conventions (subject to a 30-verse stratified follow-up evaluation, §5.6) and three Islamic-psychology applications (early-stage prevention, *kaẓm*-grounded crisis intervention, *tawba*-grounded rehabilitation). All practical implications are framed as hypotheses for empirical follow-up, not as settled prescriptions.

### 6.3. Limitations and future work

Five limitations bound the study: (i) surface-lexical scope — discourse-analytic close-reading of the spectrum's narrative deployment across suras is left for future work; (ii) the broadened nine-tafsir engagement is still selective, with deeper Sufi (al-Qushayrī, Ibn ʿArabī's school) and Persian-language commentary needing fuller integration; (iii) the cognitive-linguistic apparatus is Anglophone-dominated — engagement with classical Arabic *bayān* theory (al-Jurjānī's *Dalāʾil al-Iʿjāz*) would supply an indigenous substrate; (iv) the *ḥadīth* corpus has not been integrated; (v) the §5.7 Islamic-psychology implications await operationalisation in pilot studies of *kaẓm*-grounded emotion-regulation training. A natural follow-up is the AraBERT/CAMeLBERT contextual-embedding approach to the same fourteen-root inventory (testing stage-recoverability from distributional structure), deferred here to maintain the philological-statistical centre of gravity.

### 6.4. Closing remark

The Qur’anic lexicon encodes a sophisticated theory of the anger spectrum — not as explicit theoretical formulation but as the architectural design of its semantic surface. Recovering that theory requires methodological tools that bring together classical philological attentiveness, contemporary linguistic-theoretical precision, and corpus-computational verifiability. We hope the present study, alongside Izutsu, Qāʾimīniyā, Pakatchi, Narimani et al., and Qarizadeh et al., advances this triple integration. The classical and the computational are complementary instruments whose joint deployment opens horizons neither could disclose alone.

---

## Acknowledgements

The authors thank Kais Dukes (in memoriam) and the team behind the Quranic Arabic Corpus, and the Tanzil Project, for releasing the morphological and textual resources without which this kind of empirical Qur’anic analysis would not be feasible. We thank Urmia University for institutional support, and the anonymous peer reviewer whose detailed comments materially improved the methodological framing, the statistical interpretation (especially regarding the χ²(1) result and the *sakhaṭ* baseline-sensitivity question), and the reproducibility of the analysis pipeline.

## Funding

This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.

## Competing interests

The authors declare no competing financial or non-financial interests.

## Ethics statement

This study uses only publicly-released text-corpus data (the Quranic Arabic Corpus, GPL-licensed; the Tanzil Quran text, CC-BY-ND 3.0). No human or animal subjects were involved at any stage. As a corpus-only philological-computational analysis, the work is exempt from human-subjects review under the standards of Urmia University and of comparable institutions.

## Author contributions

K.J. (corresponding author) conceived the project, developed the theoretical framework, conducted the lexicographic and tafsir-tradition analysis, drafted the manuscript, and is responsible for the final form of the argument. A.J. contributed to the theoretical framework, the design of the computational pipeline, and editorial revision. Both authors approved the final manuscript and are jointly accountable for its content.

## Author affiliations and ORCID

**Karim Jabbary** (corresponding author). Department of Arabic Language and Literature, Faculty of Literature and Humanities, Urmia University, Urmia, Iran. *email:* k.jabbary@urmia.ac.ir.

**Ali Jabbary**. Faculty of Computer Engineering, Urmia University, Urmia, Iran. *email:* a.jabbary@urmia.ac.ir.

**ORCID:** Karim Jabbary: 0000-0000-0000-0000 (to be provided at submission). Ali Jabbary: 0000-0000-0000-0000 (to be provided at submission).

## Data and Code Availability

All code, data, concordance CSV outputs, and figure-generation scripts are released open-source at:

> [github.com/ali-kin4/quranic-emotion-spectrum](https://github.com/ali-kin4/quranic-emotion-spectrum)

The repository contains: (i) the Python pipeline under MIT License; (ii) the Quranic Arabic Corpus (Dukes 2011) under its original GPL; (iii) the complete CSV concordance for the fourteen core spectrum roots (312 attestations), distributional summaries, statistical tests (χ²(5) = 227.15; χ²(1) = 1.55), network-centrality outputs, and umbrella-cooccurrence tables; (iv) PDF and PNG versions of the seven figures published with this paper; (v) full text of the Persian and English manuscripts; (vi) the SHA-256 hash of the QAC v0.4 source file (`data/quran/qac_morphology.sha256`) and the manual-validation audit (`data/concordance/validation_audit.md`). The complete analysis can be regenerated end-to-end by:

```bash
pip install -r analysis/requirements.txt
python analysis/extract_concordance.py
python analysis/advanced_metrics.py
python analysis/visualize_spectrum.py
python analysis/visualize_advanced.py
```

---

## References

Akra, D., Hammouda, T., & Jarrar, M. (2025). *QuranMorph: Morphologically Annotated Quranic Corpus* [Preprint]. arXiv:2506.18148. https://arxiv.org/abs/2506.18148

Albayrak, I. (2020). Semantics of the Qur’anic Weltanschauung: A critical analysis of Toshihiko Izutsu's works. *American Journal of Islam and Society*, *37*(1–2). https://ajis.org/index.php/ajiss/article/view/387

Almuhanna, M., et al. (2025). Sentiment preservation in Quran translation with artificial intelligence approach: Study in reputable English translation of the Quran. *Humanities and Social Sciences Communications*, *12*(1), Article 04181. https://doi.org/10.1057/s41599-024-04181-0

Averill, J. R. (1982). *Anger and Aggression: An Essay on Emotion*. New York: Springer-Verlag.

Berkowitz, L. (1993). *Aggression: Its Causes, Consequences, and Control*. New York: McGraw-Hill.

Derki, M. (2022). Conceptualization of anger in Modern Standard Arabic and English: A comparative study. *Professional Discourse & Communication*. https://www.pdc-journal.com/jour/article/view/168

Dukes, K. (2011). *Quranic Arabic Corpus (Morphology, Version 0.4)*. University of Leeds. https://corpus.quran.com

El-Awa, S. M. S. (2006). *Textual Relations in the Qur’an: Relevance, Coherence and Structure*. London and New York: Routledge.

Frijda, N. H. (1986). *The Emotions*. Cambridge and Paris: Cambridge University Press & Éditions de la Maison des Sciences de l'Homme.

Gross, J. J. (1998). The emerging field of emotion regulation: An integrative review. *Review of General Psychology*, *2*(3), 271–299.

Gross, J. J. (Ed.). (2014). *Handbook of Emotion Regulation* (2nd ed.). New York: Guilford Press.

Gross, J. J. (2015). Emotion regulation: Current status and future prospects. *Psychological Inquiry*, *26*(1), 1–26.

Ibn Fāris, A. (1979). *Muʿjam Maqāyīs al-Lughah* (ʿA. M. Hārūn, Ed.). Beirut: Dār al-Fikr.

Ibn Manẓūr, M. (1993). *Lisān al-ʿArab* (3rd ed.). Beirut: Dār Ṣādir.

Ibn ʿĀshūr, M. T. (1984). *al-Taḥrīr wa-l-Tanwīr*. Tunis: al-Dār al-Tūnisiyyah li-l-Nashr.

Izutsu, T. (1959). *The Structure of the Ethical Terms in the Koran: A Study in Semantics*. Tokyo: Keio Institute of Philological Studies.

Izutsu, T. (1964). *God and Man in the Koran: Semantics of the Koranic Weltanschauung*. Tokyo: Keio Institute of Cultural and Linguistic Studies.

Izutsu, T. (1966/2002). *Ethico-Religious Concepts in the Qurʾān*. Montreal: McGill-Queen's University Press.

Kassinove, H., & Tafrate, R. C. (2002). *Anger Management: The Complete Treatment Guidebook for Practitioners*. Atascadero, CA: Impact Publishers.

Kennedy, C. (1999). *Projecting the Adjective: The Syntax and Semantics of Gradability and Comparison*. New York: Garland Publishing. (Published version of the 1997 UCSC PhD dissertation.)

Kennedy, C. (2007). Vagueness and grammar: The semantics of relative and absolute gradable adjectives. *Linguistics and Philosophy*, *30*(1), 1–45.

Kövecses, Z. (1986). *Metaphors of Anger, Pride, and Love: A Lexical Approach to the Structure of Concepts*. Amsterdam: John Benjamins.

Kövecses, Z. (2000). *Metaphor and Emotion: Language, Culture, and Body in Human Feeling*. Cambridge: Cambridge University Press.

Kövecses, Z. (2010). *Metaphor: A Practical Introduction* (2nd ed.). Oxford: Oxford University Press.

Lakoff, G., & Johnson, M. (1980). *Metaphors We Live By*. Chicago: University of Chicago Press.

Lakoff, G., & Kövecses, Z. (1987). The cognitive model of anger inherent in American English. In D. Holland & N. Quinn (Eds.), *Cultural Models in Language and Thought* (pp. 195–221). Cambridge: Cambridge University Press.

Lazarus, R. S. (1991). *Emotion and Adaptation*. New York: Oxford University Press.

Maalej, Z. (2004). Figurative language in anger expressions in Tunisian Arabic: An extended view of embodiment. *Metaphor and Symbol*, *19*(1), 51–75.

Maalej, Z. A., & Yu, N. (Eds.). (2011). *Embodiment via Body Parts: Studies from Various Languages and Cultures*. Amsterdam and Philadelphia: John Benjamins. https://doi.org/10.1075/hcp.31

al-Muṣṭafawī, Ḥ. (1416 AH / 1995). *al-Taḥqīq fī Kalimāt al-Qurʾān al-Karīm* (14 vols.). Tehran: Wizārat al-Thaqāfah wa-l-Irshād al-Islāmī.

Narimani, Z., Iqbali, M., & Chari, M. (1400 SH / 2021). [Semantic re-analysis of the words *ghayẓ*, *ghaḍab*, and *sakhaṭ* in the Holy Qur’an with an exegetical approach]. *Pizhūhish-hā-yi Qurʾān va Ḥadīth* [Qur’anic and Hadith Research]. University of Tehran. [in Persian; original Persian title: «بازشناسی معنایی واژگان «غیظ»، «غضب» و «سَخَط» در قرآن کریم با رویکرد تفسیری»]

Pakatchi, A., & Afrashi, A. (1399 SH / 2020). *Rūykardhā-yi Maʿnā-shinākhtī dar Muṭālaʿāt-i Qurʾānī* [Semantic Approaches in Qur’anic Studies]. Tehran: Pizhūhishgāh-i ʿUlūm-i Insānī va Muṭālaʿāt-i Farhangī. [in Persian]

Plutchik, R. (1980). *Emotion: A Psychoevolutionary Synthesis*. New York: Harper & Row.

Plutchik, R. (2001). The nature of emotions. *American Scientist*, *89*(4), 344–350.

Qarizadeh, M. ʿO., Salmani Marvast, M. ʿA., Meymandi, V., & Farsi, B. (1402 SH / 2024). [Polysemy of the word *ṭughyān* in the Holy Qur’an with a linguistic approach]. *Pizhūhish-hā-yi Zabānshinākhtī-yi Qurʾān* [Linguistic Research in the Holy Qur’an]. University of Isfahan. [in Persian; original Persian title: «چندمعنایی واژۀ «طغیان» در قرآن کریم با رویکردی بر زبان‌شناختی»]

Qāʾimīniyā, ʿA. (1390 SH / 2011). *Maʿnāshināsī-yi Shinākhtī-yi Qurʾān* [Cognitive Semantics of the Qur’an]. Tehran: Pizhūhishgāh-i Farhang va Andīshah-i Islāmī. [in Persian; original Persian title: «معناشناسی شناختی قرآن»]

Qāʾimīniyā, ʿA. (1393 SH / 2014). *Istiʿārah-hā-yi Mafhūmī wa Faḍāhā-yi Qurʾānī* [Conceptual Metaphors and Qur’anic Spaces]. Tehran: Pizhūhishgāh-i Farhang va Andīshah-i Islāmī. [in Persian; original Persian title: «استعاره‌های مفهومی و فضاهای قرآنی»]

Rabab'ah, K., & Al-Saidat, E. (2022). The conceptualization of anger through metaphors, metonymies and metaphtonymies in Jordanian Arabic and English: A contrastive study. *Cognitive Semantics*, *8*(3), 409–433. https://doi.org/10.1163/23526416-bja10044

Roseman, I. J. (1996). Appraisal determinants of emotions: Constructing a more accurate and comprehensive theory. *Cognition and Emotion*, *10*(3), 241–277. https://doi.org/10.1080/026999396380240

al-Rāghib al-Iṣfahānī, Ḥ. (1412 AH / 1992). *al-Mufradāt fī Gharīb al-Qurʾān* (Ṣ. ʿA. Dāwūdī, Ed.). Damascus and Beirut: Dār al-Qalam & al-Dār al-Shāmiyyah.

Sassoon, G. W. (2010). The degree functions of negative adjectives. *Natural Language Semantics*, *18*(2), 141–181.

Sawalha, M., Al-Shargi, F., Yagi, S., AlShdaifat, A. T., Hammo, B., Belajeed, M., & Al-Ogaili, L. R. (2024). Morphologically-analyzed and syntactically-annotated Quran dataset (MASAQ). *Data in Brief*, *58*, Article 111211. https://doi.org/10.1016/j.dib.2024.111211

Scherer, K. R. (2001). Appraisal considered as a process of multilevel sequential checking. In K. R. Scherer, A. Schorr, & T. Johnstone (Eds.), *Appraisal Processes in Emotion: Theory, Methods, Research* (pp. 92–120). New York: Oxford University Press.

Scherer, K. R. (2005). What are emotions? And how can they be measured? *Social Science Information*, *44*(4), 695–729.

Sharaf, A. M., & Atwell, E. (2012a). QurAna: Corpus of the Quran annotated with pronominal anaphora. In *Proceedings of the Eighth International Conference on Language Resources and Evaluation (LREC'12)* (pp. 130–137). Istanbul: ELRA. https://aclanthology.org/L12-1011/

Sharaf, A. M., & Atwell, E. (2012b). QurSim: A corpus for evaluation of relatedness in short texts. In *Proceedings of the Eighth International Conference on Language Resources and Evaluation (LREC'12)* (pp. 2295–2302). Istanbul: ELRA. https://aclanthology.org/L12-1051/

Sharifian, F. (2011). *Cultural Conceptualisations and Language: Theoretical Framework and Applications*. Amsterdam: John Benjamins.

Sinai, N. (2017). *The Qur’an: A Historical-Critical Introduction*. Edinburgh: Edinburgh University Press.

Sinai, N. (2023). *Key Terms of the Qur’an: A Critical Dictionary*. Princeton, NJ: Princeton University Press.

Soriano, C. (2003). Some anger metaphors in Spanish and English: A contrastive review. *International Journal of English Studies (IJES)*, *3*(2), 107–122.

Soriano, C. (2005). *The Conceptualization of Anger in English and Spanish: A Cognitive Approach* [Doctoral dissertation, Universidad de Murcia]. https://digitum.um.es/digitum/handle/10201/33082

Soriano, C. (2013). Anger metaphors across languages: A cognitive linguistic perspective. In R. R. Heredia & A. B. Cieślicka (Eds.), *Bilingual Figurative Language Processing* (pp. 410–440). Cambridge: Cambridge University Press.

Spielberger, C. D. (1999). *Professional Manual for the State-Trait Anger Expression Inventory–2 (STAXI-2)*. Odessa, FL: Psychological Assessment Resources.

al-Ṭabarī, M. ibn J. (n.d. / 2000 ed.). *Jāmiʿ al-Bayān ʿan Taʾwīl Āy al-Qurʾān* (A. M. Shākir, Ed., 24 vols.). Beirut: Muʾassasat al-Risālah.

al-Ṭabāṭabāʾī, M. Ḥ. (1390 AH / 1970). *al-Mīzān fī Tafsīr al-Qurʾān* (20 vols.). Beirut: Muʾassasat al-Aʿlamī li-l-Maṭbūʿāt.

al-Ṭabarsī, F. al-Ḥ. (n.d.). *Majmaʿ al-Bayān fī Tafsīr al-Qurʾān*. Beirut: Dār al-Maʿrifah.

*Tanzil Project*. (n.d.). *The Tanzil Quran Text* (Uthmani edition). https://tanzil.net.

al-Qurṭubī, M. ibn A. (1964). *al-Jāmiʿ li-Aḥkām al-Qurʾān* (20 vols.). Cairo: Dār al-Kutub al-Miṣriyyah.

al-Qushayrī, ʿA. al-K. (2000). *Laṭāʾif al-Ishārāt* (I. Basūnī, Ed., 6 vols.). Cairo: al-Hayʾah al-Miṣriyyah al-ʿĀmmah li-l-Kitāb.

Quṭb, S. (1980). *Fī Ẓilāl al-Qurʾān* (6 vols.). Cairo and Beirut: Dār al-Shurūq.

Riḍā, M. R. (1947). *Tafsīr al-Qurʾān al-Ḥakīm (al-Manār)* (12 vols.). Cairo: Dār al-Manār.

Ibn Kathīr, I. (1419 AH / 1999). *Tafsīr al-Qurʾān al-ʿAẓīm* (S. al-Salāmah, Ed., 8 vols.). Riyadh: Dār Ṭaybah.

Wierzbicka, A. (1999). *Emotions Across Languages and Cultures: Diversity and Universals*. Cambridge: Cambridge University Press.

Yu, N. (1995). Metaphorical expressions of anger and happiness in English and Chinese. *Metaphor and Symbolic Activity*, *10*(2), 59–92. https://doi.org/10.1207/s15327868ms1002_1

al-Zamakhsharī, M. (1407 AH). *al-Kashshāf ʿan Ḥaqāʾiq Ghawāmiḍ al-Tanzīl*. Beirut: Dār al-Kitāb al-ʿArabī.
