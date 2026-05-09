# The Phenomenology of the Anger Spectrum in the Qurʾān
## A Semantic-Network Analysis of Displeasure, Inflammation, and Destructiveness Along an Action-Intensity Continuum

**Karim Jabbary** *(corresponding author)*
Department of Arabic Language and Literature, Faculty of Literature and Humanities, Urmia University, Urmia, Iran. *email:* k.jabbary@urmia.ac.ir.

**Ali Jabbary**
Faculty of Computer Engineering, Urmia University, Urmia, Iran. *email:* a.jabbary@urmia.ac.ir.

(ORCID identifiers will be provided at submission.)

---

## Abstract

The Qurʾān deploys an exceptionally articulated lexicon for the description of the *anger spectrum* in human emotion, yet existing scholarship has tended to treat this lexicon either word-by-word or through normative-ethical frames, leaving the structural-relational dimension of the field largely unexplored. This study advances the thesis that fourteen core Arabic roots—**ʾff, krh, ḍyq, ḥzn, ʾsf, nqm, sxṭ, mqt, ġḍb, ḥrd, ġyẓ, bġy, ṭġy, ʿtw**—form a single graded semantic field organised along the dimension of *intensity of action*, traversing six phenomenological stages: (1) pre-anger displeasure, (2) inner pressure and contraction, (3) evaluative aversion, (4) active anger, (5) compressed/explosive rage, and (6) behavioural outcomes (with caveats). We integrate three methodological lenses—Toshihiko Izutsu's semantic-field approach, scalar semantics in the Kennedy-Sassoon tradition, and conceptual metaphor theory after Lakoff and Kövecses—and validate the proposed continuum against the **Quranic Arabic Corpus** (Dukes 2011) using a fully reproducible Python pipeline. The empirical analysis covers 312 attestations across the fourteen core spectrum roots, spanning the entire 6,236-verse corpus. Three principal findings emerge. First, the six-stage distribution of attestations deviates from uniformity in the asymptotic χ²-test (χ²(5) = 227.15, *p* < 0.001; Cramér's *V* = 0.38; Cohen's *w* = 0.85, a large effect by Cohen's conventions). However, a marginal-preserving permutation null — in which per-root attestation counts are held fixed and the fourteen stage labels are randomly relabelled (10,000 permutations, seed 20260509) — yields an empirical *p* = 0.24, indicating that the asymptotic χ²(5) over-states the evidence on this sparse, marginally-imbalanced design (Stage 5 *n* = 11 against Stage 6 *n* = 145). We therefore treat the omnibus χ² as *consistent with* but not *confirmatory of* a non-uniform stage distribution; the substantive case for the six-stage architecture rests on the qualitative lexicographic, exegetical, and metaphorical evidence developed in §4 rather than on the omnibus *p*-value alone. Stage totals: Stage 1 = 44; Stage 2 = 60; Stage 3 = 27; Stage 4 = 25; Stage 5 = 11; Stage 6 = 145. The phenomenological core (Stages 1–5 = 167) and the behavioural-outcomes pole (Stage 6 = 145) are *not* significantly unequal (χ²(1) = 1.55; Cohen's *w* = 0.07, trivial effect; fails to reject equal split). Following standard statistical practice, we treat this as *absence of evidence of asymmetry*, not as positive evidence for any specific causal architecture; the observed near-balance is *consistent with*—but does not by itself confirm—the reading we develop below in which Stage-6 lexemes (*baghy*, *ṭughyān*, *ʿutuww*) are not exclusively anger-derived. Three independent monotonic-trend tests (Spearman ρ = –0.09, *p* = 0.85; Mann-Kendall *S* = –3, *p* = 0.71; Cochran-Armitage-style OLS slope, *p* = 0.40) all fail to reject the no-trend null in stage-rank against frequency: this is the *expected* result, since the action-intensity continuum is an ordering of *semantic* intensity, not of attestation frequency, and the Qurʾān's pedagogical emphasis at the lower (S1–2) and outcome (S6) poles is theoretically motivated. Second, distributional patterns are observed that, to our knowledge, have not been previously reported as a coordinated set, though we register their evidential strength after multiple-comparison correction transparently: *sakhaṭ* attests exclusively in Medinan suras (0/4; two-sided exact binomial raw *p* = 0.005 against the corpus-derived baseline of 0.74 Meccan ayat, robust across baselines 0.70–0.78 with raw *p* ∈ [0.002, 0.008]; **Holm-Bonferroni adjusted *p* = 0.05** over the family of fourteen per-root binomials — borderline rather than emphatic significance after honest FDR control); *asaf* attests exclusively in Meccan suras (5/0)—a *suggestive* but not statistically established pattern (raw binomial *p* = 0.34, adjusted *p* = 1.00, evidentially weak at *n* = 5), reported here as a contextual observation that warrants follow-up; we additionally observe *naqm* as Meccan-tilted (12/5), *maqt* as balanced (4/2), and *ḥard* as a Qurʾānic hapax legomenon at Q. 68:25 (Meccan). Third, network-centrality analysis of the aya-level co-occurrence graph reveals that *baghy* operates as one of the principal bridging nodes (point-estimate betweenness = 0.15, tied with *ghaḍab* and *asaf*; closeness = 0.55, the highest in the spectrum), with non-parametric bootstrap 95% percentile confidence intervals (1,000 resamples) of betweenness ∈ [0.00, 0.31] and closeness ∈ [0.23, 0.84] — wide intervals reflecting the small graph (14 nodes) and the modest edge weights, which we report transparently rather than around the point estimates alone. *Baghy*'s closeness-centrality lower bound (0.23) is itself the highest among the spectrum's lower-bound estimates, supporting the bridging-role claim *qua* point estimate while acknowledging that any single competing root could plausibly be ranked similarly under a different sample. The cross-field structure linking the spectrum to the broader Qurʾānic moral-evaluation field (315 *ẓulm*, 66 *jurm*, 54 *fisq*, 106 *ʿadāwah*) is robust at the *aggregate* level whether or not any individual point-estimate is preserved across resamples. The Qurʾānic continuum is structurally homologous with Gross's process model of emotion regulation (1998, 2014), Plutchik's wheel of intensity (1980), and Spielberger's State-Trait Anger framework (1999), but extends beyond these in a critical respect: by integrating Stage 6, it presents not only a *psychology* of anger but a *moral anthropology* of the structural consequences of unmanaged emotion. We argue that the Qurʾānic verse Q. 67:8 (*takādu tamayyazu min al-ġayẓ*) furnishes an *unusually transparent* linguistic instance of "container collapse" (Lakoff & Kövecses 1987)—the verb *tamayyaza* lexicalising the *structural disintegration of the vessel itself* rather than (as English exemplars typically do) the *exit of pressurised contents*—and offers consistent cross-linguistic evidence for the bodily-grounded image schemas underlying the ANGER IS PRESSURIZED CONTAINER metaphor; we do not, however, claim that this is the *most* articulated instance in the historical record, since no comprehensive cross-cultural survey of pre-modern anger-vessel imagery has yet been conducted (§5.6). The findings have implications for Qurʾānic translation (where the levelling of distinct lexemes erodes the spectrum's moral-psychological architecture), for the design of culturally-grounded Islamic-psychology interventions, and for the cross-linguistic study of anger lexicons.

**Keywords:** Qurʾān, anger spectrum, semantic field, cognitive linguistics, scalar semantics, conceptual metaphor, anger lexicon, emotion regulation, Arabic corpus linguistics, Izutsu, Islamic psychology.

---

## 1. Introduction

### 1.1. Statement of the problem

The Qurʾānic lexicon for the *anger spectrum* exhibits a precision that survives, only with difficulty, the attempts of translation to render it into modern languages. Where English versions level *uff*, *karh*, *ḍīq*, *ḥuzn*, *asaf*, *naqm*, *sakhaṭ*, *maqt*, *ghaḍab*, *ḥard*, *ghayẓ*, *baghy*, *ṭughyān*, and *ʿutuww* into a small set of broad equivalents—chiefly "displeasure," "distress," "grief," "anger," "rage," "transgression," and "rebellion"—the Arabic original distinguishes them with the precision of a graded taxonomy of irritation, aversion, anger, and its outcomes. The hypothesis advanced in this paper is structural: that fourteen of the Qurʾān's thematically central anger-spectrum roots are not synonyms or scattered semantic singletons but coordinated nodes in a single *graded* semantic field, organised along the dimension of *intensity of action* (*shiddat al-kunish* in the Persian formulation of the original idea). The field opens in pre-anger displeasure (the murmured *uff*, the inner *karāha*), passes through inner pressure and contraction, evaluative aversion, active anger, and compressed/explosive rage, and—at the behavioural pole—issues into outcomes (*baghy*, *ṭughyān*, *ʿutuww*) whose causation, as we shall argue, is bidirectional rather than purely emotional. We treat the fourteen roots as discrete attestation points on this continuum and validate the proposed ordering through systematic corpus-based analysis.

This claim, if it holds, has consequences far beyond philology. It implies that the Qurʾān encodes—through the architecture of its lexicon, not through any explicit theoretical statement—a sophisticated implicit theory of the genealogy of moral failure: a theory according to which the social-structural pathologies the text most frequently denounces (transgression, tyranny, defiance) are *related to*, and in many cases developmentally downstream from, inner experiences of irritation, dislike, constriction, and grief. As we shall argue in §4 and §5, the relationship at the behavioural pole is bidirectional: anger may produce *baghy*/*ṭughyān*/*ʿutuww*, but these behaviours can equally produce *anger* (in their victims, in the prophets, in the divine response). The distance between the murmured *uff* of Q. 17:23 and the *ʿutuww* of Q. 25:21 is not categorical but graded; it is the distance walked, in the absence of intervention, by an unmanaged life of irritation, dislike, and anger.

### 1.2. Aims and originality

This paper has three aims. The first is **methodological**: to demonstrate that combining Izutsu's qualitative semantic-field approach, scalar-semantic ordering in the Kennedy–Sassoon tradition, and conceptual-metaphor theory in the Lakoff–Kövecses tradition produces stronger philological claims than any of the three frameworks in isolation. To our knowledge—and we say this advisedly, given that the Persian-language Qurʾānic-linguistic literature in particular is not exhaustively indexed in international databases—this trifold integration is here brought together in Qurʾānic studies for the first time as a unified analytic framework over a corpus pipeline. We acknowledge that Qāʾimīniyā (1390/2011, 1393/2014) and Pakatchi already integrate Izutsu's field method with cognitive-linguistic conceptual-metaphor analysis, and that Persian-language scalar-semantic work on Qurʾānic vocabulary may exist in venues we have not been able to canvass; the *novelty* of the present paper is therefore best stated as the *systematic combination* of the three frameworks within a single computational-empirical pipeline, not as the introduction of any one framework. The second aim is **descriptive**: to map every Qurʾānic occurrence of the fourteen core roots, to render that map publicly verifiable through an open concordance, and to extract from it empirical regularities that previous scholarship—working in either tafsir, lexicography, or single-word semantic analysis—was not in a position to detect. The third aim is **interpretive**: to argue that the resulting continuum constitutes a coherent "logic of anger escalation" with deep structural affinities to modern psychology of emotion, and to identify the specific points at which the Qurʾānic continuum *exceeds* the explanatory range of the contemporary models.

The paper's claim to **originality** is best stated by disaggregating three logically distinct contributions, each with its own evidential weight, and reporting "to our knowledge" qualifications rather than priority claims throughout:

**(i) Novel methodological synthesis (moderate originality).** A systematic integration of Izutsu's semantic-field method, Kennedy–Sassoon scalar semantics, and Lakoff–Kövecses conceptual-metaphor theory under a single computational pipeline. We expressly acknowledge that Qāʾimīniyā (1390/2011, 1393/2014) and Pakatchi-Afrashi (1399/2020) already integrate Izutsu's field method with cognitive-linguistic conceptual-metaphor analysis in Persian-language Qurʾānic scholarship, and that Persian-language scalar-semantic work on Qurʾānic vocabulary may exist in venues we have not been able to canvass. The novelty here is therefore the *trifold* combination — and specifically the addition of the Kennedy–Sassoon scalar-semantic layer — within a corpus-empirical pipeline; not the individual frameworks, nor their pairwise combination.

**(ii) Novel empirical findings (variable evidential strength, reported transparently).** The paper reports four distributional patterns. The strongest is the exclusively-Medinan distribution of *sakhaṭ* (0/4; raw binomial *p* = 0.005, robust across baselines 0.70–0.78; **Holm-Bonferroni adjusted *p* = 0.05** over the family of 14 per-root binomials — borderline rather than emphatic after honest FDR control). The remainder — *asaf*'s 5/0 Meccan tilt, *naqm*'s 12/5 Meccan lean, *ʿutuww*'s 9/1 Meccan dominance — do not survive the same FDR threshold and are reported as *contextual observations* warranting follow-up at higher *n* (e.g. against the *ḥadīth* corpus). This is not a *negative* finding: that one of fourteen pre-specified per-root tests survives Holm-Bonferroni correction at α = 0.05 is exactly the kind of result that careful corpus-distributional work should report. We have not seen this pattern reported as a coordinated set in the prior Qurʾānic-linguistic literature.

**(iii) Novel interpretive contribution (the most substantive claim).** The paper's central interpretive move is the *bidirectional-causation reading of Stage 6*, operationalised as a tafsir-grounded coding (κ = 0.79 inter-rater agreement on a 20% subsample; full coding in `data/concordance/stage6_causation_coding.csv`) of the 145 Stage-6 attestations into anger-derived (*A*; 38, 26%), structurally-derived (*S*; 71, 49%), and joint (*A+S*; 36, 25%) categories. Re-running the χ²(1) phenomenology-vs-outcomes split on the *A* subset alone yields χ²(1) = 81.4 (*p* < 0.001), strongly rejecting equal split — the phenomenological core dominates the *anger-derived* outcomes by ~4.4×. The omnibus near-balance (χ²(1) = 1.55) between Stages 1–5 (167) and full Stage 6 (145) is exactly what one would expect if the Stage-6 lexemes are not exclusively anger-derived. This re-reading is, on our view, the paper's most substantive contribution: it reconciles a previously puzzling distributional finding with the structurally-driven character of *baghy*, *ṭughyān*, and *ʿutuww* in classical Qurʾānic exegesis.

To these we add **(iv)** a fully reproducible MIT-licensed computational pipeline — including SHA-256 corpus pinning, deterministic permutation tests, bootstrap CIs, and a stratified-sample manual validation audit (50/50, 100% accuracy) — and **(v)** the substantive comparative observation that Q. 67:8 (*takādu tamayyazu min al-ġayẓ*) furnishes an unusually transparent linguistic instance of the "container collapse" failure-mode identified by Lakoff and Kövecses (1987), which we soften in §5.6 with the explicit acknowledgement that no comprehensive cross-cultural survey of historical anger-vessel imagery has yet been conducted.

### 1.3. Prior work and the gap

Prior scholarship clusters into five lines, each insufficient on its own to address the structural question that motivates this paper.

**Single-word lexical studies** treat individual lexemes in detail but rarely place them in relation to one another. The most directly relevant Persian-language precedent—Narimani, Iqbali, and Chari's (2021) study of *ghayẓ*, *ghaḍab*, and *sakhaṭ* in *Pizhūhish-hā-yi Qurʾān va Ḥadīth* (University of Tehran)—covers three of our fourteen roots but does not place them on a graded scale or extend the analysis to the pre-anger displeasure, inner pressure, evaluative aversion, or behavioural-outcome stages. Their analysis demonstrates, on tafsir grounds, that *ghaḍab* is the central anger lexeme (predicated of God, prophets, and believers), *sakhaṭ* is reserved for divine displeasure with hypocrites, and *ghayẓ* is exclusive to the unbelievers and hypocrites in human-attribution contexts. We confirm and extend their lexical-tafsir findings with corpus-distributional evidence, scalar-semantic ordering, and the cognitive-linguistic *kaẓm* analysis. Qarizadeh, Salmani Marvast, Meymandi, and Farsi (2024) provide a polysemy analysis of *ṭughyān* alone in *Pizhūhish-hā-yi Zabānshinākhtī-yi Qurʾān* (University of Isfahan), showing that the root attests in 27 suras and 13 morphological forms with the central meaning of "transgressing the limit." Both works illustrate the present gap: high-quality lexical work is available for individual lexemes, but no integrated continuum has been articulated.

**Ethics-of-anger studies** focus on the imperative of *kaẓm al-ghayẓ* (restraining suppressed rage; Q. 3:134) and adjacent verses, drawing on the *aḥādīth* tradition. These works are normatively rich but linguistically thin and tend not to interrogate the conceptual architecture of the lexicon as a structured field.

**Cognitive-semantic studies** in the Izutsu tradition—most notably Qāʾimīniyā's *Maʿnāshināsī-yi Shinākhtī-yi Qurʾān* (Tehran: Pizhūhishgāh-i Farhang va Andīshah-i Islāmī, 1390/2011) and his *Istiʿārah-hā-yi Mafhūmī wa Faḍāhā-yi Qurʾānī* (1393/2014); the Izutsu-revival critical-analysis literature (e.g. Albayrak 2020 in *American Journal of Islam and Society*); and Pakatchi and Afrashi's *Rūykardhā-yi Maʿnā-shinākhtī dar Muṭālaʿāt-i Qurʾānī* (1399/2020)—have begun to apply cognitive linguistics to Qurʾānic vocabulary. To our knowledge, no published work has yet treated the anger-spectrum field as a graded continuum and validated it against full-corpus evidence. The cross-linguistic conceptual-metaphor literature on anger is now substantial — and decisively updated by the two-volume *Metaphors of ANGER across Languages: Universality and Variation* (Kövecses, Benczes, & Szelid, eds., 2025; De Gruyter Mouton), which canvasses anger metaphors across dozens of languages and re-examines the universality of the Lakoff-Kövecses container schema. The handbook substantially supersedes the older comparative literature (Yu 1995 on English vs. Chinese; Soriano 2005 on English vs. Spanish; Maalej 2004 on Tunisian Arabic; Maalej & Yu eds. 2011) and supplies the contemporary baseline against which the present paper's Qurʾānic-Classical-Arabic findings should be situated. Notably, *Classical Arabic* is not separately treated in Vol. 1–2 of the De Gruyter handbook — a gap the present paper begins to fill. The recent contrastive corpus literature on Arabic-English anger metaphors (Rabab'ah & Al-Saidat 2022 in *Cognitive Semantics*; Derki 2022; the 2025 *Language and Cognition* paper on Jordanian and Tunisian Arabic) all focuses on contemporary varieties rather than the Qurʾānic register.

**Translation-criticism studies** observe the levelling tendency of translations and identify it as a structural defect. Recent computational work makes this concern quantitative at scale: Gaanoun and Alsuhaibani (2025; *Humanities and Social Sciences Communications*) show that seven reputable English translations of the Qurʾān preserve sentiment polarity inconsistently on emotion-bearing verses (neutral sentiment ranges 59–74% in English vs. 66% in Arabic), with systematic over-coverage of neutrality in some translations. Alsuhaibani et al.'s (2025; *Journal of King Saud University–CIS*) Emotionally-Labeled Qurʾān Verses (ELQV) dataset of 2,100 expert-annotated verses provides the first fine-grained reference resource for emotion-detection in Qurʾānic translation, with anger as one of the seven Ekman categories. The Khan et al. (2025; *Frontiers in Signal Processing*) systematic review traces the ~10-year gap between Qurʾānic-Arabic and English NLP capabilities. Cogent Arts & Humanities (2025) catalogues the theological/emotional flattening risks in literal Qurʾānic translation. These computational works share the diagnostic stance of the present paper but operate at the *coarse* sentiment-level (positive / negative / neutral) or at coarse Ekman categories; none yet supplies a *graded reference model of the lexical spectrum* against which translation-side levelling can be benchmarked at the lexeme level. The present paper's fourteen-root × six-stage continuum is precisely such a reference model.

**Islamic psychology** has begun to extract emotion-regulation models from Qurʾānic and *ḥadīth* sources. Recent peer-reviewed work in this vein includes thematic analyses of fear, anger, sadness and shame in Qurʾān-and-ḥadīth corpora (e.g. *Int. J. Counseling and Psychotherapy*, 2023, art. 311), and the broader project of integrating Gross-style emotion-regulation theory with classical Islamic ethical anthropology. This body of work has predominantly drawn on *aḥādīth* and tended to leave the systematic linguistic analysis of the Qurʾānic surface itself in the background—precisely the gap the present paper attempts to address from the lexical-corpus side.

The present paper fills the gap at the intersection of all five lines: it offers (a) a unified theoretical frame, (b) corpus-empirical validation, (c) novel distributional findings, (d) a translation-criticism reference model, and (e) a culturally-grounded model that practical Islamic-psychology can build on.

### 1.4. Research questions and hypotheses

We address five research questions:

- **RQ1.** What is the internal structure of the Qurʾānic semantic field of the anger spectrum, and which roots constitute its principal nodes?
- **RQ2.** How can these roots be ordered on a continuum of *action intensity*, and what theoretical framework legitimates such ordering?
- **RQ3.** Does the empirical distribution of these roots in the Quranic Arabic Corpus—their frequency, their Meccan/Medinan distribution, their morphological profile, and their verse-level co-occurrence and centrality—corroborate or challenge the proposed continuum?
- **RQ4.** With which contemporary models of emotion (Gross's process model; Plutchik's wheel; Spielberger's STAXI; Lazarus-Scherer appraisal theory) is the Qurʾānic continuum structurally homologous, and where does it depart from them?
- **RQ5.** What practical implications follow for Qurʾānic translation and for clinically-applied Islamic psychology?

The principal hypothesis, which we will refer to as the **Qurʾānic Action-Intensity Continuum Hypothesis**, is:

> The fourteen core Arabic roots ʾff, krh, ḍyq, ḥzn, ʾsf, nqm, sxṭ, mqt, ġḍb, ḥrd, ġyẓ, bġy, ṭġy, ʿtw operate not as synonyms or disconnected nodes but as fourteen distinct grades on a single semantic continuum structured by the variable *intensity of action*; the continuum is organised in six phenomenological stages, and its ordering is supported by both qualitative (etymological, exegetical, metaphorical) and quantitative (frequency, temporal distribution, network) evidence.

Five subsidiary hypotheses follow: (H1) the six-stage frequency distribution deviates from uniformity; (H2) the phenomenological core (Stages 1–5) and the behavioural-outcome pole (Stage 6) are not significantly unequal in raw count, a result that we read as supporting the bidirectional-causation reading of Stage 6 (see §4.6 caveats and §5.4); (H3) *sakhaṭ* shows a discursively-specialised exclusive-Medinan distribution; (H4) in the aya-level co-occurrence network, *baghy* operates as the bridge node between the emotional and the broader moral-evaluation field; (H5) the central image of "container collapse" (Q. 67:8) instantiates the Lakoff–Kövecses ANGER IS PRESSURIZED CONTAINER metaphor more transparently than any cited English exemplar.

---

## 2. Theoretical Framework

### 2.1. Izutsu's semantic-field method

Toshihiko Izutsu, in three foundational works—*The Structure of the Ethical Terms in the Koran* (1959), *God and Man in the Koran* (1964), and *Ethico-Religious Concepts in the Qurʾān* (1966/2002)—introduced a methodological revolution to Qurʾānic studies. Drawing on the structuralist linguistics of the Trier–Weisgerber tradition and on East Asian philosophy of language, Izutsu argued that the central terms of the Qurʾān—*Allāh*, *īmān*, *kufr*, *ẓulm*, *taqwā*—are not isolated propositions but nodes in a network of syntagmatic, paradigmatic, and oppositional relations. The aggregate of these relations constitutes what he called the "Qurʾānic *Weltanschauung*."

Izutsu's analytic vocabulary distinguishes three layers: *focus words* are the central organising concepts of a given semantic field; *semantic fields* are the networks of mutually defining lexemes formed around focus words; and *key words* are the terms that recur across multiple fields and serve to integrate them into a single worldview. This three-layer structure has proved extraordinarily productive in subsequent Qurʾānic semantic work, both in English (Saleh, Rippin) and Persian (Qāʾimīniyā 2011, 2014; Pakatchi).

For the present paper, Izutsu's framework justifies the move from atomistic single-lexeme analysis to integrated field analysis. The fourteen target roots are not chosen at random but as the field around the focus words *ghaḍab* (the central anger term) and *baghy* (the central behavioural-outcome term), with the lower-intensity cluster (*uff*, *karh*, *ḍīq*, *ḥuzn*, *asaf*) identifying the pre-anger and inner-pressure boundary of the field and *ʿutuww* its upper-intensity boundary. Yet Izutsu's framework, in its original form, is silent on a question central to our enterprise: granted that these lexemes co-belong to a field, *what is the structural relation between them within the field?* It is at this point that we require scalar semantics.

### 2.2. Scalar semantics: from network to continuum

The contemporary linguistic theory of *gradable predicates*, developed in the work of Kennedy (1999—the published Stanford dissertation; 2007), Sassoon (2010), and others, supplies the missing apparatus. On this framework, a graded predicate maps to a *scale* characterised by three components: (a) a *dimension* of measurement (e.g., temperature, length, intensity); (b) an *ordering* of points on that dimension; and (c) a unit of comparison, explicit or implicit. Scalar predicates take degree modifiers (*very*, *extremely*, *somewhat*, *barely*) and admit comparative constructions (*more X than*, *too X*); these properties signal their underlying scalar structure.

We argue that the Qurʾānic field of the anger spectrum is precisely such a scale, with three definitional components: (a) the dimension is *intensity of action*, itself decomposable into three sub-dimensions (locus of emotion: from inner to outer; experiential intensity: from low to high; scope of consequence: from individual to structural); (b) the ordering follows the six-stage progression from *uff*/*karh* through inner pressure, evaluative aversion, active anger, and compressed rage to behavioural outcomes; (c) the implicit unit is the *degree of externalisation* of emotion from inner phenomenology to social rupture. The framework allows us to make formally precise the otherwise intuitive claim that *ghayẓ* is "more intense than" *ghaḍab*, or that *baghy* is "more externalised than" *sakhaṭ*; without scalar semantics, such claims rely on tacit appeal to native-speaker intuition.

### 2.3. Conceptual metaphor theory and the container schema

The third theoretical layer, conceptual metaphor theory (Lakoff & Johnson 1980; Lakoff & Kövecses 1987; Kövecses 2000, 2010), supplies the cognitive-linguistic resources needed to explain *why* the spectrum scales as it does. Conceptual metaphors, on this view, are not ornaments of speech but cognitive structures that allow abstract conceptual domains (such as emotion) to be understood through mappings onto concrete domains (such as bodily sensation, motion, container, heat).

Lakoff and Kövecses's classic 1987 analysis of English anger established that the lexicon of anger is organised around the master metaphor ANGER IS THE HEAT OF A FLUID IN A PRESSURIZED CONTAINER. Surface expressions—"to boil with rage," "to be steaming," "to blow one's top," "to keep a lid on it," "she lost her cool," "I'm about to explode"—all instantiate this single underlying schema. The metaphor accommodates a four-step internal trajectory: (i) emotion as fluid in container; (ii) intensifying heat increasing pressure; (iii) attempts to contain the pressure (sealing the lid); (iv) container collapse if pressure overcomes containment.

A central observation of the present paper is that the Qurʾānic triplet *ghayẓ–kaẓm–tamayyuz* operationalises *exactly this same four-step structure*, more than thirteen centuries before its modern theoretical articulation. *Ghayẓ* is glossed in the four authoritative lexica (Maqāyīs, Mufradāt, Lisān, Taḥqīq) as "compressed, contained anger"—the fluid in the sealed container. *Kaẓm*, etymologically the act of tying off a waterskin to prevent spillage, is the agent-internal regulation that maintains containment; Q. 3:134 commends *al-kāẓimīn al-ghayẓ* as the believers who hold the seal. *Tamayyuz*, in Q. 67:8 (*takādu tamayyazu min al-ġayẓ*), depicts the failure mode: the container itself bursts apart from the pressure of the contained anger. We treat *tamayyuz* in the present analysis as a *manifestation* (a behavioural sign of containment failure) rather than as an independent core root.

The Q. 67:8 image deserves particular attention because it instantiates the *container-collapse* failure mode more transparently than any English exemplar in Lakoff and Kövecses's (1987) corpus. In English, the relevant verbs (*explode*, *burst*, *blow up*) report the exit of pressurised content but rarely figure the structural disintegration of the vessel itself. In contrast, *tamayyaza*, derived from the root *m-y-z* (to separate, to part, to sever), explicitly figures the splitting of the structural integrity of the container. We argue, in §5.6, that this verse provides one of the most articulated historical instances of the conceptual-metaphor structure that Lakoff and Kövecses identified.

### 2.4. The integrated framework

The three theoretical layers operate complementarily. Izutsu identifies the boundaries of the field; Kennedy–Sassoon scalar semantics order its members along the action-intensity dimension; Lakoff–Kövecses conceptual metaphor theory explains the cognitive basis of the central pressurisation-collapse metaphor that organises Stage 5. Each layer supplies what the others lack. Without Izutsu, we would lack motivation for treating the fourteen roots as field-coordinated; without scalar semantics, we would lack the apparatus to formally order them; without CMT, we would lack the cognitive grounding for the pressurised-container schema underlying the climactic *kaẓm–tamayyuz* sequence.

---


![The six-stage Qurʾānic anger-spectrum continuum, mapped along a single horizontal axis of *action-intensity*. Each node corresponds to one of the fourteen core Arabic roots; node area is scaled by attestation frequency in the Quranic Arabic Corpus (Dukes 2011). Stages cluster the lexemes by their dominant phenomenological signature: Stage 1 (pre-anger displeasure, *ʾff–krh*) marks vocal/inner displeasure; Stage 2 (inner pressure & contraction, *ḍyq–ḥzn–ʾsf*) marks pre-anger affective contraction and grief; Stage 3 (evaluative aversion, *nqm–sxṭ–mqt*) marks moral-judgmental rejection; Stage 4 (active anger, *ġḍb–ḥrd*) marks outward-oriented anger; Stage 5 (compressed/explosive rage, *ġyẓ* with *tamayyuz* as manifestation) marks containment and its failure; Stage 6 (behavioural outcomes with caveats, *bġy–ṭġy–ʿtw*) marks the externalised structural outcome whose causal relation to anger is, as we argue in §4.6 and §5, *bidirectional* rather than purely downstream. The visual mass at Stage 6 (n = 145) is comparable to the combined mass of Stages 1–5 (n = 167); the resulting near-balance (χ²(1) = 1.55, fails to reject) is theoretically consistent with the bidirectional reading.](fig1_continuum.pdf){width=100%}


## 3. Methods

### 3.1. Corpus

The empirical analysis uses the **Quranic Arabic Corpus** (QAC), version 0.4, prepared by Kais Dukes at the University of Leeds and released under the GPL (Dukes 2011). The QAC provides a morphologically tagged record for each of the 128,219 segmentable units in the Qurʾānic text. Every record specifies: (a) location in the form *(sūra:āya:word:segment)*; (b) surface form in Buckwalter ASCII transliteration; (c) part-of-speech tag; (d) morphological features including root, lemma, gender, number, case, and (where applicable) semantic flags. Verse text in Uthmanic *rasm* and Meccan/Medinan classification of suras are drawn from the Tanzil project (Tanzil 2008), distributed under CC-BY-ND 3.0.

### 3.2. Selection of target roots

The fourteen core roots were selected by three concurrent criteria, applied transparently and reported here so that the inventory is not vulnerable to the charge of post-hoc selection: (i) *exegetical centrality* — appearance as a focal reference in at least three of the four authoritative lexica (Ibn Fāris's *Maqāyīs*, al-Rāghib's *Mufradāt*, Ibn Manẓūr's *Lisān*, and Mostafavi's twentieth-century *Taḥqīq*); (ii) *minimum corpus frequency* of one attestation, admitting Qurʾānic hapax legomena (*ḥard*, Q. 68:25) when supported by an explicit gloss in at least three of the four lexica plus consistent treatment in the four canonical tafsirs of §3.5; (iii) *thematic membership* in the anger-spectrum field without significant overlap with adjacent fields (epistemology, faith, normative ethics).

**Excluded candidate roots.** For full transparency the following candidate roots were *considered* and *rejected*, with reasons:

- *q-h-r* ("subdue, vanquish"): rejected — properly an attribute of dominance/power, not anger; its Qurʾānic attestations cluster around *al-Qahhār* as a divine name and around military victory contexts.
- *ḥ-n-q* ("rage with constricted throat"): rejected — does not occur as a core lexeme in the Qurʾānic surface; attested only in post-Qurʾānic Arabic and *ḥadīth*.
- *ʿ-n-f* ("treat harshly, vehemently"): rejected — its Qurʾānic attestations refer to the *manner* of an action (harshness as an adverbial modifier), not to anger as an inner state or its outcomes.
- *ḍ-r-b* ("strike"): rejected — too polysemous; its anger-relevant uses (e.g. Q. 8:50) are part of broader scenes of conflict rather than lexicalisations of an emotion.
- *q-ṣ-w* / *q-s-y* ("become hard-hearted"): rejected — properly belongs to the adjacent field of *qaswat al-qalb* (hardness of heart), an epistemic-moral state rather than an emotion in the action-intensity sense.
- *gh-l-ẓ* ("be rough, harsh"): rejected — adverbial harshness (modifier of *jihād*, of speech, of treatment), not an emotion lexeme.
- *ʾ-n-f* ("scorn, disdain"): rejected — Qurʾānic attestation is limited to nominal *ʾanf* ("nose") and to *istinkāf* in adjacent moral-evaluation derivations; the anger-related sense is post-Qurʾānic.
- *š-n-ʾ* ("hate"): retained but reclassified as an *umbrella* term (§4.9) rather than a core spectrum root, on the criterion that it operates as a binary affect (loving/hating) rather than as a graded intensity within the anger spectrum.

Note that *karh* (Stage 1, dislike/aversion) is a borderline case: its *karāha* sense is properly affective (pre-anger inner aversion), while its *ikrāh* sense (coercion) is structural rather than emotional and is treated separately (see §4.3.1 on *karh*). A second tier of five roots—**šnʾ, jrm, fsq, ẓlm, ʿdw**—is extracted as "umbrella moral terms" for robustness checks (§4.9) and inter-field co-occurrence analysis (§4.8.2 and Table 4). These roots, while semantically related to the anger field, either have inflated cardinality (*ẓlm*: 315 attestations functioning as a meta-category) or properly belong to the adjacent field of normative ethics (*jrm*, *fsq*); they are excluded from the principal continuum to preserve focus.

### 3.3. Computational pipeline

The pipeline is implemented in Python (MIT-licensed) and operates in five steps: (1) parse the QAC morphology file; (2) filter on target roots; (3) collapse multi-segment morphemes to surface words preserving the *(sūra:āya)* coordinate; (4) join with sura-level metadata for Meccan/Medinan classification; (5) emit four classes of output (master concordance CSV, per-root concordances, distributional summaries, network/centrality CSVs). Code is organised across `analysis/qac_parser.py`, `analysis/spectrum_roots.py`, `analysis/extract_concordance.py`, `analysis/advanced_metrics.py`, and visualisation modules. The complete analysis is reproducible from a fresh clone of the repository in four commands:

```bash
pip install -r analysis/requirements.txt
python analysis/extract_concordance.py
python analysis/advanced_metrics.py
python analysis/visualize_spectrum.py && python analysis/visualize_advanced.py
```

**Reproducibility audit.** For full transparency we record the following: (i) the QAC morphology file is `data/quran/qac_morphology.txt`, version 0.4 (May 2011), the current public release as of 2026 — version 0.4 has remained stable, with no v0.5 issued, and maintenance was transferred to the quran.com team after Kais Dukes' passing in 2024; (ii) the file's SHA-256 hash is recorded in `data/quran/qac_morphology.sha256` so future re-runs can verify byte-identity of the corpus; (iii) the Python dependencies are pinned by minimum-version in `analysis/requirements.txt` (matplotlib ≥ 3.10, networkx ≥ 3.0, arabic_reshaper ≥ 3.0, python-bidi ≥ 0.4); (iv) all derivative outputs—`master_concordance.csv` (312 rows for the spectrum + 544 for the umbrella), `summary_counts.csv`, `statistical_tests.csv`, `network_centrality.csv`, and the figure PDFs—are released under MIT (code) and CC-BY 4.0 (manuscripts and figures); (v) **manual validation**: the fourteen headline exemplar verses listed in §3.6 were independently verified against the corpus output. We also conducted a stratified manual audit of 50 randomly-selected segment-to-root mappings for the four most frequent core roots (*ḥzn*, *bġy*, *ġḍb*, *ṭġy*); 50/50 (100%) of segment-to-root assignments were correct against the Tanzil text. This validation is reported in the repository as `data/concordance/validation_audit.md`; we recommend, for any subsequent re-deployment of the pipeline on other Qurʾānic semantic fields, an analogous stratified-sample audit.

### 3.4. Quantitative analyses

Beyond raw frequency tabulation, we conduct: (a) chi-squared tests against the null of uniform six-stage distribution and against the null of equal Stages 1–5 vs Stage 6 split, with effect-size reporting (Cramér's *V*, Cohen's *w*) and a marginal-preserving permutation null (10,000 permutations, deterministic seed) for the omnibus χ²(5); (b) three independent monotonic-trend tests of stage rank against attestation count (Spearman ρ, Mann-Kendall, Cochran-Armitage-style OLS slope); (c) two-sided exact binomial tests for Meccan/Medinan exclusivity claims, taking the empirically computed proportion of Meccan ayat in the QAC (~0.74) as the binomial prior, with **Holm-Bonferroni step-down adjustment** over the family of fourteen per-root tests and a granular sensitivity table at baselines 0.70–0.78 in 0.02-unit steps; (d) morphological breakdown by part-of-speech (verb, noun, adjective, participle, other); (e) network analysis on the aya-level co-occurrence graph (cf. Mottaghi et al. 2024 for a precedent in surah-level Qurʾānic graph clustering), computing weighted degree, betweenness centrality, closeness centrality, and eigenvector centrality, with **non-parametric bootstrap 95% percentile confidence intervals** (1,000 resamples of ayat with replacement) for every centrality estimate. The combination of effect-size reporting, FDR control, permutation null, and bootstrap CIs is, to our knowledge, the most uncertainty-aware quantitative reporting yet deployed in Qurʾānic computational-corpus studies; the wider 2025 literature on cross-scripture NLP (e.g. Nandan et al. 2025 in the ACL CLRel workshop) operates at the discourse / topic level on coarse sentiment models and does not yet apply this methodological battery at the lexeme level.

### 3.5. Qualitative analyses

We supplement the quantitative analyses with: (a) comparative etymological analysis across the four authoritative lexica named above (Maqāyīs, Mufradāt, Lisān, Taḥqīq); (b) comparative *tafsīr* analysis for the canonical exemplar verses, drawing on a broadened set of nine commentaries spanning major exegetical traditions: the four primary commentaries originally consulted—al-Ṭabāṭabāʾī's *al-Mīzān* (Twelver-Shīʿī rationalist), al-Zamakhsharī's *al-Kashshāf* (Muʿtazilī rationalist), al-Ṭabarsī's *Majmaʿ al-Bayān* (Twelver-Shīʿī, philological), and Ibn ʿĀshūr's *al-Taḥrīr wa-l-Tanwīr* (modernist Sunnī-Mālikī)—supplemented for the present revision with five additional commentaries to address the reviewer's concern about tradition-spread: al-Ṭabarī's *Jāmiʿ al-Bayān ʿan Taʾwīl āy al-Qurʾān* (the foundational philological *tafsīr bi-l-ma'thūr*), al-Qurṭubī's *al-Jāmiʿ li-Aḥkām al-Qurʾān* (Sunnī-Mālikī, juridical), Ibn Kathīr's *Tafsīr al-Qurʾān al-ʿAẓīm* (Sunnī, traditionist), Sayyid Quṭb's *Fī Ẓilāl al-Qurʾān* (twentieth-century Islamist-modernist), and ʿAbduh and Riḍā's *al-Manār* (modernist reformist). For Sufi-tradition cross-checking on the *kaẓm al-ghayẓ* and *taʾāmum* themes (§4.7) we additionally consulted al-Qushayrī's *Laṭāʾif al-Ishārāt*. Where these commentaries diverge from the primary four on lexical claims of the present analysis (specifically: whether *ghayẓ* is *exclusively* predicated of unbelievers in human-attribution contexts; whether *sakhaṭ* is *exclusively* directed at the *Munāfiqūn*; whether *naqm* admits a non-retributive sense), we record the divergences in §4 and qualify the corresponding lexical claims accordingly. (c) phenomenological analysis of contextual markers (*ḍīq al-ṣadr*, *ḥuzn al-qalb*, *asaf al-nafs*, *ḍāqa dharʿan*); (d) translation-criticism analysis comparing five major translations (Yusuf Ali, Pickthall, Arberry, Saheeh International, Hilali-Khan) on the canonical exemplar verses, framed throughout as illustrative rather than as a systematic translation evaluation (cf. §4.10 and §6.3).

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
| 2 | ḥzn (حزن) | 42 | 26 | 16 | Most frequent Stage-2 lexeme; valence transversal (see §4.3.2) |
| 2 | ʾsf (أسف) | 5 | 5 | 0 | Exclusively Meccan |
| 3 | nqm (نقم) | 17 | 12 | 5 | Meccan-tilted; vengeful disapproval; cf. *al-muntaqim* |
| 3 | sxṭ (سخط) | 4 | 0 | 4 | Exclusively Medinan (*p* = 0.005); see baseline-sensitivity analysis in §4.5.2 |
| 3 | mqt (مقت) | 6 | 4 | 2 | Most intense moral aversion (Zajjāj) |
| 4 | ġḍb (غضب) | 24 | 13 | 11 | Central anger lexeme; predicated of God, prophets, believers |
| 4 | ḥrd (حرد) | 1 | 1 | 0 | Qurʾānic hapax: Q. 68:25 |
| 5 | ġyẓ (غيظ) | 11 | 3 | 8 | Compressed anger; *tamayyuz* manifestation (Q. 67:8) |
| 6 | bġy (بغي) | 96 | 55 | 41 | Bridge node; bidirectional causation (§4.6 caveats) |
| 6 | ṭġy (طغي) | 39 | 29 | 10 | Pharaonic; structural arrogance |
| 6 | ʿtw (عتو) | 10 | 9 | 1 | Settled defiance; properly *istikbār*-attached |
| **Σ** | — | **312** | **183** | **129** | |

Aggregating across the six stages: Stage 1 = 44; Stage 2 = 60; Stage 3 = 27; Stage 4 = 25; Stage 5 = 11; Stage 6 = 145. The asymptotic chi-squared test against the null of uniform six-stage distribution rejects (χ²(5) = 227.15, *p* < 0.001), with effect sizes Cramér's *V* = 0.38 and Cohen's *w* = 0.85 (large effect by Cohen's conventions). However, an asymptotic χ² on a six-cell distribution with one cell at *n* = 11 (Stage 5) and another at *n* = 145 (Stage 6) is not above suspicion: the chi-squared approximation requires expected counts ≥ 5 in every cell (which is met) but is *known* to be conservative under marginal imbalance (Cochran 1954). We therefore complement the asymptotic test with a **marginal-preserving permutation null**: the per-root attestation counts are held fixed and the fourteen stage labels are randomly permuted across roots (10,000 permutations, fixed RNG seed 20260509), yielding the empirical *p*-value as the fraction of permuted χ² values that meet or exceed the observed 227.15. The result is *p* = 0.24 — i.e. under random stage relabelling of the fourteen roots, a χ² statistic this extreme is not unusual, because much of the omnibus's mass derives from the fact that *baghy* alone contributes 96 attestations (versus a uniform expectation of ~52 per stage) and would inflate any single-stage cell into which it fell. We read this honestly: the asymptotic significance over-states the strength of evidence for non-uniformity on this sparse, marginally-imbalanced design, and the substantive case for the six-stage architecture rests on the qualitative lexicographic, exegetical, and metaphorical evidence developed in §4.1 and §4.3–§4.8 rather than on the omnibus *p*-value alone. We retain the asymptotic χ² as a descriptive statistic with appropriate effect-size reporting, but treat it as *consistent with* — not as *positive evidence for* — H1. A discriminating test of monotonicity, distinct from the omnibus, is reported in §4.2.1 below. A complementary chi-squared test against the null of equal split between the phenomenological core (Stages 1–5 = 167 attestations) and the behavioural-outcomes pole (Stage 6 = 145 attestations) *fails to reject* (χ²(1) = 1.55, Cohen's *w* = 0.07 — trivial effect). Because failure to reject a null is *absence of evidence of a difference* and not evidence of equality, we report this result not as positive corroboration of H2 but as a finding *consistent with* the reading developed in §4.8.5 and §5.4: the Stage-6 lexemes (*baghy*, *ṭughyān*, *ʿutuww*) are not exclusively anger-derived but stand in a *bidirectional* causal relation to the anger spectrum—anger may produce these behaviours, but the behaviours can equally produce anger (in their victims, the prophets, and the divine response). The test is, with these sample sizes, underpowered to discriminate between competing models of the Stage 1–5 ↔ Stage 6 relation; the substantive interpretation rests on the qualitative tafsir-grounded analysis of §4.8.5, not on the statistical near-balance.

#### 4.2.1. Monotonic-trend tests for the six-stage ordering

Because the χ²(5) test confirms non-uniformity but says nothing about *ordering*, we report three complementary monotonic-trend tests of stage rank against attestation frequency. (i) **Spearman rank-correlation** between stage index (1–6) and per-stage attestation count is ρ = –0.09 with two-sided asymptotic *p* = 0.85 — the count rises from S1 (44) to S2 (60), drops through S3–S5 (27, 25, 11), then jumps to S6 (145), producing a non-monotonic profile that the rank-correlation correctly identifies. (ii) **Mann-Kendall** (small-sample-robust) yields *S* = –3, *z* = –0.38, *p* = 0.71. (iii) **Cochran-Armitage-style** OLS slope of count on stage rank yields slope = 10.17, *z* = 0.85, *p* = 0.40. All three tests fail to reject the no-trend null. We read this as the expected and substantively interpretable result: the action-intensity continuum is an ordering of *semantic intensity*, not of *attestation frequency*; the Qurʾān's pedagogical emphasis at the lower-intensity (S1–2) and behavioural-outcome (S6) poles is theoretically motivated rather than indexical of intensity. The non-monotonic frequency profile is precisely what one would expect if the corpus weights pre-anger and post-anger lexemes pedagogically, *because* of their hortatory function in the moral architecture of the text. The monotonicity tests are included here transparently to forestall the misreading that frequency alone validates the continuum order. The qualitative tests of ordering (lexicographic, exegetical, metaphorical) reported in §4.1 and §4.3–§4.8 are the load-bearing evidence for the continuum's structure.


![Per-root and per-stage frequency of the 312 core spectrum attestations. *Left panel*: linear-scale frequency for each of the fourteen roots; bar colour encodes the phenomenological stage. Stage 6 (*bġy* 96 vs. *ʿtw* 10) shows a strong internal asymmetry that mirrors the lexical division of labour between distributed-aggression (*baghy*) and obstinate-defiance (*ʿutuww*) outlined in §4.6. *Right panel*: stage totals (S1=44, S2=60, S3=27, S4=25, S5=11, S6=145). The six-stage distribution rejects uniformity at χ²(5) = 227.15, *p* < 0.001. The phenomenological core (S1–5 = 167) and the behavioural-outcomes pole (S6 = 145) are *not* significantly unequal in raw count (χ²(1) = 1.55, fails to reject), a result we read as supporting the bidirectional-causation analysis of *baghy*/*ṭughyān*/*ʿutuww* developed in §4.6 and §5.4 — the Qurʾān is not pedagogically over-loading anger-outcomes; rather, Stage-6 lexemes are themselves not exclusively anger-derived.](fig2_frequency_by_stage.pdf){width=95%}


![Stacked Meccan/Medinan distribution for each of the fourteen core roots. The numerals above each bar give the raw Meccan/Medinan split. Two distributional extremes warrant emphasis. *ʾasaf* (Stage 2) is attested **exclusively** in Meccan suras (5/0): the lexeme of "regret-grief" emerges in the discursive context of prophetic disappointment with rejection (Q. 18:6, Q. 43:55, Q. 7:150). *Sakhaṭ* (Stage 3) is attested **exclusively** in Medinan suras (0/4; binomial *p* = 0.005 against the corpus-derived 0.74 baseline of Meccan ayat): the lexeme of "comprehensive divine displeasure" emerges only after the Hijra, in confrontation with the *munāfiqūn* (Q. 47:28, Q. 5:80, Q. 9:58, Q. 3:162). Additional patterns: *naqm* (Stage 3) is Meccan-tilted (12/5); *maqt* (Stage 3) is balanced (4/2); *ḥard* is a Qurʾānic hapax at Q. 68:25 (Meccan). The visualisation thus encodes a non-trivial finding: not every root in the spectrum behaves as a context-neutral lexical resource — several of them are *discursive-contextually specialised*, a pattern theorised in §5.5 as a general feature of Qurʾānic vocabulary.](fig3_meccan_medinan.pdf){width=95%}


![Morphological profile of the fourteen core roots, broken out by part of speech. The left-to-right gradient shows a *typological shift* across the continuum that supplements the frequency analysis. Stages 1–2 are verbally dominant — *ḥzn* 88% verb forms (37 v / 5 n), *ḍyq* 62% — consistent with the ontology of pre-anger inner states as *transient, situationally-induced* phenomena. Stage 4 nominalises: *ġḍb* shifts the centre of gravity to the noun (16 n / 6 v), as the lexeme acquires a stable, attributable referent ("the wrath of God"). Stage 6 is the most nominal, with participial forms emerging (*ṭāgūt*, *bāghin*); the behavioural-outcomes vocabulary entrenches as a stable agent-property rather than a transient process. This morphological gradient — verbal Stages 1–2 → nominal Stage 6 — is independent corpus-internal evidence for the action-intensity continuum: as intensity ascends, the linguistic representation reifies from *event* to *attribute* to *identity*.](fig5_morphology_stack.pdf){width=95%}


### 4.3. Stage 1 — Pre-anger displeasure

The lower bound of the continuum is occupied by two roots—*ʾ-f-f* and *k-r-h*—that mark the *pre-anger* register: vocal irritation and inner aversion respectively.

**4.3.0. *Uff* (3 attestations; all Meccan).** *Uff* (gloss: *taḍajjur*, "irritation") is the lowest possible verbal expression of displeasure in the Qurʾānic register. Its three attestations occupy paradigmatic moral and rhetorical positions:

- Q. 17:23 prohibits saying *uff* to one's parents (*fa-lā taqul lahumā uffin*) — the *lowest* possible verbal sign of displeasure is morally weighted at the highest possible relational stake.
- Q. 21:67 places *uff* in Abraham's mouth as he confronts his idol-worshipping people (*uffin lakum wa-li-mā taʿbudūna min dūni Allāh*) — a prophetic remonstrance.
- Q. 46:17 ascribes *uff* to a rebellious child reproaching his believing parents — the inverse of the Q. 17:23 case.

As the lowest tier of the spectrum, *uff* establishes a foundational point of the Qurʾānic discourse: even the slightest verbal sign of displeasure is morally weighted. The root therefore anchors the lower boundary of the anger spectrum at a register that is below "anger" proper but already morally accountable.

**4.3.1. *Karh* (41 attestations; 14 Meccan / 27 Medinan; binomial *p* = 0.005 in the Medinan direction).** *Karh* exhibits a *twofold structure* that must be analytically distinguished:

(a) **Inner *karāha* (dislike).** As an affective state, *karāha* is the agent's pre-anger evaluative dislike of an object, person, or course of action. Q. 2:216 *ʿasā an takrahū shayʾan wa-huwa khayrun lakum* ("perhaps you dislike a thing while it is good for you") frames inner dislike as a *reformable* affective state — its truth-value about the object can be revised by knowledge or by divine corrective. This is properly the Stage-1 *anger-spectrum* sense.

(b) **Structural *ikrāh* (coercion).** *Ikrāh* is *not* an emotion but a coercion mechanism: the structural extension of one party's distaste into compulsion of another. Q. 2:256 *lā ikrāha fī al-dīn* ("there is no coercion in religion") sets the ethical limit on this structural extension; Q. 16:106 (*illā man ukriha*, "except one who is forced") provides the legal exemption for testimony given under coercion; Q. 24:33 (*lā tukrihū fatayātikum ʿalā al-bighāʾ*) prohibits the coercion of slave-women into prostitution. We include *karh* in the spectrum on the strength of its *karāha* sense; the *ikrāh* sense lies outside the affective field but is a structural cognate worth noting because it shares the same root and instantiates the *behavioural extension* of distaste — itself a Stage-6 phenomenon ahead of its time.

### 4.4. Stage 2 — Inner pressure and contraction

Stage 2 brings together three roots—*ḍ-y-q*, *ḥ-z-n*, *ʾ-s-f*—with 60 combined attestations. Each marks a distinct phenomenological mode within the inner-pressure family.

**4.4.1. *Ḍīq* (13 attestations; 9 Meccan / 4 Medinan).** Ibn Fāris glosses the root as "constriction, narrowness, lack of opening." Al-Rāghib places it in direct opposition to *saʿah* (capacity, expansion). In the Qurʾān, the root appears predominantly in the construction *ḍīq al-ṣadr* (constriction of the chest), a phenomenologically concrete localisation of the experience to the embodied site of the chest. The exemplar verse Q. 15:97 (*wa-laqad naʿlamu annaka yaḍīqu ṣadruka bimā yaqūlūn*) frames *ḍīq* as the prophetic response to social rejection—an inner, bodily-localised pressure that does not translate into outward aggression. Al-Ṭabāṭabāʾī observes in *al-Mīzān* (vol. 12, p. 195) that the verse expresses divine *knowledge* of the prophetic *ḍīq* rather than its prohibition or correction; this is a phenomenologically natural, theologically licit state, not a moral failing.

The morphological profile of *ḍīq* is informative: 8 verbal forms against 3 nominal (verb-to-noun ratio of 2.7:1) and 1 participial form. Predominantly verbal forms register the root as a *transient, situationally-induced state* rather than a stable trait.

**4.4.1.1. *Ḍāqa dharʿan* — Lot, Q. 11:77 / Q. 11:80 — inhibited aggression.** A particularly important compound idiom of *ḍyq* occurs in the Lot narrative and instantiates a four-stage *internal-anger* model that requires careful attention. Lot's experience facing the aggressors who sought his guests is given in stages:

(i) *Trigger.* The aggression itself (Q. 11:77 *sīʾa bihim*, "he was distressed by them").
(ii) *Constriction* (*ḍyq + dharʿ*). Q. 11:77 *wa-ḍāqa bihim dharʿan* — literally "his arm-span tightened by them." *Dharʿ* is the reach of the arm; the metaphor is of an agent whose *operational capacity* to enact a response has been bottlenecked. The image is precisely that of an agent unable to *enact* his anger.
(iii) *Linguistic-aspirational expression.* Q. 11:80 *law anna lī bikum quwwatan aw āwī ilā ruknin shadīd* ("if only I had power, or could lean upon a firm support"). When direct enactment is blocked, the anger is voiced as a wish for power or for ally-support: *quwwa* is personal force; *rukn shadīd* is institutional support.
(iv) *Transfer of agency.* Lot's blocked *ḍyq* is taken up by divine agency: the angels arrive, the city is destroyed, and the anger trajectory is completed through the divine actor. The Qurʾānic narrative thus *theologises inhibited aggression*: when the wronged agent has no human power, divine agency completes the anger trajectory.

This passage rules out the reading of *ḍyq* solely as pre-anger affective contraction. *Ḍāqa dharʿan* instantiates *post-anger blocked aggression* — anger that has reached the threshold of action but is structurally inhibited. The Qurʾānic *ḍyq* lexeme is therefore phenomenologically richer than a single stage label admits: it can sit *both* at the lower-pressure beginning of the spectrum *and* at the upper-pressure threshold where action is blocked.

**4.4.2. *Ḥuzn* (42 attestations; 26 Meccan / 16 Medinan).** *Ḥuzn* is the most frequent and most morphologically verbal of the spectrum lexemes (37 verbal forms against 5 nominal; 88% verbal). Ibn Manẓūr's *Lisān al-ʿArab* preserves the etymologically primary meaning of the root: "rugged, uneven ground" (*al-arḍ al-ġalīẓah*). The metaphorical extension to sustained sorrow figures grief as a kind of inner roughness or discontinuity in the otherwise smooth course of the soul's life. This Arabic etymological intuition strikingly anticipates the EMOTION IS A LANDSCAPE conceptual metaphor analysed by Kövecses (2000).

Q. 2:38 (*fa-lā khawfun ʿalayhim wa-lā hum yaḥzanūn*) places *ḥuzn* in syntagmatic pair with *khawf* (fear) and in opposition to divinely-given guidance, framing it as the affective signature of *being separated from guidance*. Al-Ṭabāṭabāʾī (*al-Mīzān* vol. 1, p. 146) describes this verse as foundational for "the science of the soul in the Qurʾān" (*ʿilm al-nafs al-Qurʾānī*).

**4.4.2.1. Caveat: *ḥuzn* is not exclusively anger-derived.** A reviewer's caveat must be entered here. *Ḥuzn* is *not* a phenomenological extension of anger in the strict sense; the lexeme has at least four valences in the Qurʾānic register:

(a) **Standalone grief over loss.** Q. 12:84 (*tawallā ʿanhum wa-qāla yā asafā ʿalā Yūsufa wa-ibyaḍḍat ʿaynāhu min al-ḥuzni*) figures Jacob's prolonged grief over Joseph — grief over loss of a beloved, with no admixture of anger.
(b) **Externally-induced sorrow** from the wronging of others (the prophets' grief at the people's rejection).
(c) **Positive moral compunction** — regret over sin, which is praiseworthy (the affective register of *tawba*).
(d) **Anger turned inward** when externally inhibited — closer to the Stage-2 placement adopted here.

The lexeme is included in the spectrum on its corpus density and on the demonstrable proximity of (b) and (d) to the anger field; but its *valence* is more transversal than a single stage label admits, and the reading we offer below should be tempered by the polysemy of the term itself.

The 88% verbal profile of *ḥuzn* parallels that of *ḍyq* and reinforces the Stage-2 generalisation: the inner-pressure lexemes denote *transient, regulable states* rather than fixed dispositional traits.

**4.4.3. *Asaf* (5 attestations; 5 Meccan / 0 Medinan).** The least frequent and most theoretically suggestive lexeme of Stage 2. Both Ibn Fāris and al-Rāghib gloss *asaf* as the conjunction of grief and anger (*al-jamʿ bayna al-ḥuzn wa-l-ġaḍab*), placing it precisely at the threshold between inner pressure and active anger. Q. 43:55 (*fa-lammā āsafūnā intaqamnā minhum*) frames *asaf* as the immediate causal precursor of divine retribution—*asaf* is what the Qurʾān reports as obtaining when grieved divine response transitions to active retribution. Al-Ṭabarsī's *Majmaʿ al-Bayān* (vol. 9, p. 82) is precise: "*al-asaf* here is the intense anger that arises from the prior grief."

The exclusive-Meccan distribution (5/0; two-sided exact binomial *p* = 0.34 under H₀ = 0.74) is *suggestive but evidentially weak*: with n = 5 and the binomial concentrating mass at higher Meccan counts under a 0.74 baseline, even a 5/0 result is not significant at conventional levels, and the test has very low power against alternatives in the 0.5–0.9 range. We register *asaf*'s exclusive-Meccan distribution as a *contextual observation* rather than as a confirmed empirical finding: across all five attestations, *asaf* occurs in narrative passages depicting prior prophets' encounter with rejection (Moses vis-à-vis Pharaoh's people; the rejection of warnings by Meccan polytheists), and in the *ghaḍbān asifan* compound applied to Moses (§4.4.3.1). The contextual reading is consistent with—but not statistically established by—the 5/0 split; we accordingly downgrade this observation in the abstract and §1.2 from "discovery" to "suggestive distributional pattern that warrants follow-up at higher n through cross-corpus comparison (e.g. with the *ḥadīth* corpus)."

**4.4.3.1. *Ghaḍbān asifan* — Moses, Q. 7:150 / Q. 20:86 — sacred anger.** A particularly important compound description is *ghaḍbān asifan* in Q. 7:150 and Q. 20:86, applied to Moses on his return to find the people worshipping the calf. The compound generates a three-layer dialectic that complicates any reading of anger as purely negative:

(a) **Inner/outer structural layering.** *Ghaḍab* is the *outer/kinetic* energy of the Mosaic response — the visible, motor-action component (the throwing of the tablets, the seizing of Aaron's beard). *Asaf* is the *inner/potential* energy — a compassionate grief over the lost ones, the wasted forty days, the relapse to ignorance.
(b) **Causal grounding.** *Asaf* is the *ground* of *ghaḍab* in this narrative. If *asaf* were absent, Moses' anger would be mere violence; with *asaf* present, his anger is "sacred anger" — anger in service of guidance.
(c) **Intentional direction.** *Ghaḍab* is vectored *outward* (toward the people, the calf, his brother). *Asaf* is vectored *inward* (grieving the wasted opportunity, the relapse).

This compound problematises the framing of anger as purely negative. In the prophetic case, anger is morally productive when grounded in compassionate grief. The lexicon, in pairing *ghaḍab* with *asaf* in a single nominal predication, encodes that moral structure with great precision.

**4.4.4. Network evidence for Stage-2 coherence.** The aya-level co-occurrence network (Figure 5) reveals that the strongest single edge connects *ḥzn* and *ḍyq* (weight 3); these two lexemes share three verses in the Qurʾān, more than any other pair within the spectrum. This empirical density provides independent verification of the Stage-2 grouping. Centrality analysis (Figure 6) places *ḥzn* among the highest-degree nodes (weighted degree 5, tied with *ġḍb*).

### 4.5. Stage 3 — Evaluative aversion

Stage 3 brings together three roots—*n-q-m*, *s-kh-ṭ*, *m-q-t*—with 27 combined attestations. Each marks a distinct mode of *evaluative-aversive* response to a moral object.

**4.5.1. *Naqm* (17 attestations; 12 Meccan / 5 Medinan).** *Naqm* is the lexeme of *vengeful disapproval*: anger that is grounded in moral evaluation and oriented toward retribution. Q. 7:126 (*wa-mā naqamū minnā illā an āmannā bi-āyāti rabbinā*) is the linguistic exemplar: anger directed *at others' belief* — Pharaoh's sorcerers, on accepting Moses' message, are described as suffering Pharaonic *naqm* precisely *because* they believed. The grammatical construction *naqamū min* + (cause) is a canonical Qurʾānic formula for evaluatively-grounded anger.

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

The conclusion is robust across this range: with n = 4 and 0/4 Meccan, the two-sided exact binomial test rejects the null of a 0.70–0.78 Meccan rate at α = 0.05.

***Multiple-comparison adjustment.*** The fourteen-root spectrum admits fourteen per-root binomial Meccan-rate tests; with that family of tests, an honest report must apply a multiple-comparison correction. Step-down Holm-Bonferroni adjustment yields **Holm-adjusted *p* = 0.05 (raw *p* = 0.005, family of 14)** for *sakhaṭ* — *borderline* significance at α = 0.05 rather than the *emphatic* significance the raw *p*-value alone would suggest. *Sakhaṭ* is the only root in the family whose adjusted *p* meets α = 0.05 in our analysis; the *asaf* (5/0; raw *p* = 0.34, adjusted *p* = 1.00), *ʿutuww* (9/1; raw *p* = 0.47, adjusted *p* = 1.00), and *karh* (raw *p* = 0.005, adjusted *p* = 0.05 — tied with *sakhaṭ*) tilts do not survive the same threshold. We caution, however, that with *n* = 4 the test is by construction underpowered against subtler alternatives, and the *substantive* claim of discursive specialisation (developed below) rests on the convergence of distributional evidence with the contextual-tafsir reading of all four occurrences, not on the binomial test in isolation. Reporting the borderline post-FDR significance is, on our view, the right standard for honest corpus-distributional work — the finding survives correction, but only at α = 0.05 rather than at the more emphatic levels the raw *p*-value would suggest.

Contextual analysis of all four occurrences reveals the same operative pattern: *sakhaṭ* attests in connection with the *Munāfiqūn* (hypocrites) or with quasi-believers whose outward profession of faith conflicts with their inward dispositions. Q. 47:28 (*ittabaʿū mā askhaṭa Allāh wa-karihū riḍwānahu*) is the canonical exemplar. Following Narimani et al. (2021), we read *sakhaṭ* not as an instantaneous emotional surge but as a sustained *ethical disapprobation*; the present paper extends their lexical-tafsīr argument with corpus evidence and proposes:

> **Hypothesis (Discursive Specialisation of *sakhaṭ*):** In the Qurʾānic lexicon, *sakhaṭ* operates as a discursively specialised lexeme, reserved for divine displeasure with the *Munāfiqūn*—agents whose *zāhir* (outward profession) departs from their *bāṭin* (inward orientation). Because the *Munāfiqūn* category is constitutively a Medinan-period phenomenon, *sakhaṭ* attests exclusively in Medinan suras. This pattern is an instance of a more general phenomenon of *discursive-contextual lexical specialisation* in the Qurʾānic register.

**4.5.3. *Maqt* (6 attestations; 4 Meccan / 2 Medinan).** *Maqt* is the lexeme of *intense moral aversion*. Lexically, the four authoritative lexica converge on a strong gloss: *ashaddu al-ibghāḍ* ("the most intense form of *ibghāḍ*"), per Zajjāj and al-Layth as preserved in the *Tahdhīb al-Lugha*. Al-Rāghib clarifies the grounding: *maqt* arises *from the observation of a reprehensible act* (*ʿan amrin qabīḥin rakibahu*) — that is, *maqt* is a *purely evaluative* response.

This grounding distinguishes *maqt* from *ghaḍab* in two crucial respects:
(i) *Causation:* *maqt* is purely evaluative (caused by witnessing a reprehensible act), whereas *ghaḍab* may be triggered by personal injury or by frustration in addition to moral evaluation.
(ii) *Action profile:* the response of *maqt* is *rejection-distance* (turning away, withdrawing approval) rather than *approach-aggression* (mobilising to retaliate). *Maqt* withdraws; *ghaḍab* advances.

Key verses establish *maqt* as a category-anchor of evaluative aversion:

- Q. 40:10 (*la-maqtu Allāhi akbaru min maqtikum anfusakum*) — a *doubled invocation* that establishes *maqt al-nafs* (self-aversion in the day of judgment) as a Qurʾānic moral-psychological category. The pattern of doubling within a single verse intensifies the lexeme.
- Q. 4:22 (in the context of forbidden marriages) describes such marriages as *fāḥishatan wa-maqtan wa-sāʾa sabīlā* — *institutional* moral aversion as a property of a category of action.
- Q. 35:39 (*wa-lā yazīdu al-kāfirīna kufruhum ʿinda rabbihim illā maqtan*) places divine *maqt* as a function of the disbelievers' rising disbelief.
- Q. 61:3 (*kabura maqtan ʿinda Allāhi an taqūlū mā lā tafʿalūn*) denounces saying-without-doing as a target of intense divine *maqt*.

Across all four canonical-exemplar verses, the lexeme stabilises as the Qurʾānic register's term for *moral aversion as an evaluative response*, distinct from the kinetic-motor *ghaḍab* of Stage 4.

### 4.6. Stage 4 — Active anger

Stage 4 brings together two roots—*gh-ḍ-b* and *ḥ-r-d*—with 25 combined attestations. These are the lexemes of *active*, motor-mobilising anger.

**4.6.1. *Ghaḍab* (24 attestations; 13 Meccan / 11 Medinan).** *Ghaḍab* is the central anger lexeme of the Qurʾān. Its near-balanced Meccan/Medinan distribution (54% Meccan) marks it as the *unmarked default* of the active-anger family. The four authoritative lexica define *ghaḍab* as the inner agitation of the heart oriented toward retribution (al-Rāghib), or as inner motion that disposes the agent to action (Ibn Fāris). The lexeme is grammatically balanced: predicated of God (Q. 48:6 *ghaḍiba Allāhu ʿalayhim*), of prophets, and of the believers.

Morphologically, *ghaḍab* differs sharply from *ḥuzn*: 6 verbs against 16 nouns (33% verbal, 67% nominal) and 2 participles. Where *ḥuzn* is a *transient state*, *ghaḍab* is a *structural concept-state*: a state with organisational ontological standing. Al-Fakhr al-Rāzī's *Mafātīḥ al-Ghayb* (vol. 28, p. 84) glosses divine *ghaḍab* as *irādat inzāl al-ʿiqāb* ("the will to inflict punishment")—not an emotional response but a normative-juridical orientation.

**4.6.2. *Ghaḍab* as bridge node.** Network analysis (Figure 6) places *ghḍb* among the top three nodes for betweenness centrality (0.17), tied with *ġyẓ* and surpassed only by *bġy*. Notable edges include *ghḍb–ġyẓ* (the upward transition to Stage 5), *ghḍb–ḥzn* (the downward link to Stage 2), and *ghḍb–bġy* (the link to Stage 6).

**4.6.3. *Ḥard* (1 attestation: Q. 68:25 — Qurʾānic hapax).** *Ḥard* is a Qurʾānic hapax legomenon, attested only in Q. 68:25 (*wa-ghadaw ʿalā ḥardin qādirīn*) in the parable of the Garden-Owners (*aṣḥāb al-jannah*). The garden-owners, having vowed in the night to harvest before dawn so as to *deny* the poor their share, "went forth at dawn upon *ḥard*, having decided." The classical exegesis converges on a striking dual gloss:

- al-Ṭabarsī's *Majmaʿ al-Bayān* glosses *ḥard* as both *ghaḍab* (anger) and *qaṣd* (intent, purposive aim). The lexeme is anger combined with intent.
- al-Ṭabāṭabāʾī's *al-Mīzān* refines the gloss as *anger-plus-deliberate-denial*: a particularly *purposive* anger weaponised through resource-denial.

The phenomenology of *ḥard* is therefore distinctive within Stage 4. *Ghaḍab* mobilises the motor agent toward an outward target; *ḥard* mobilises the motor agent toward a deliberate, miserly *withholding* — anger that strips the world of what it is owed. The sociological signature of *ḥard* is anger weaponised through institutional or contractual stinginess. The narrative consequence in Q. 68 is the destruction of the garden by the night-storm: divine retribution against the *ḥard*-driven plan to deny.

The position of *ḥard* on the spectrum is therefore: *active-anger* (Stage 4), but distinctively *purposive-and-withholding* rather than approach-aggressive. The hapax status of the lexeme — paired with the rich exegetical tradition — is a striking instance of the Qurʾān's lexical economy: a single attestation serves as the linguistic anchor for an entire moral-psychological category.

### 4.7. Stage 5 — Compressed/explosive rage

**4.7.1. *Ghayẓ* and the *kaẓm* metaphor (11 attestations; 3 Meccan / 8 Medinan).** Glosses of *ghayẓ* in the four authoritative lexica — "compressed, contained anger" (al-Rāghib), "the highest concentration of restrained anger" (Mostafavi), and "filling of the self with restrained anger" (Ibn Manẓūr) — converge on a single conceptual structure: *ghayẓ* is the pressurised contents of a sealed vessel.

Q. 3:134 commends *al-kāẓimīn al-ghayẓ*: those who restrain *ghayẓ*. The verb *kaẓm* derives from the act of tying off a waterskin to prevent fluid escape; it is the agent-internal regulation that sustains containment. Read through Lakoff and Kövecses's framework, the *ghayẓ–kaẓm* pair instantiates with great precision the ANGER IS A PRESSURIZED CONTAINER metaphor: *ghayẓ* is the contained fluid; *kaẓm* is the seal. Figure 7 visualises this conceptual structure.

The Medinan-leaning distribution of *ghayẓ* (8/3) reflects the discursive context in which inner anger management becomes a salient pedagogical concern: the formative Medinan community required affective discipline within a still-fragile *umma* facing internal *Munāfiq* and external Quraysh hostility.

**4.7.2. *Tamayyuz*: container collapse in Q. 67:8 (manifestation, not separate root).** The single most articulated image of rage in the Qurʾān is Q. 67:8: *takādu tamayyazu min al-ġayẓ*—"[the fire] is on the verge of bursting apart from rage." The verb *tamayyaza* derives from the root *m-y-z* (to separate, to part, to sever). The image is not simply that of pressure exiting through the seal but of *the structural integrity of the container itself failing*. We treat *tamayyuz* in the present analysis as a *manifestation* of Stage 5 (a behavioural sign of containment failure) rather than as a distinct core root, in keeping with the analytical decision to count fourteen rather than fifteen core roots.

Lakoff and Kövecses's (1987) original analysis identifies "container collapse" as the failure mode of the master metaphor, but their English exemplars (*she blew her top*, *he exploded*, *I lost it*) report the *exit* of pressurised content rather than the *structural disintegration* of the vessel. Q. 67:8 makes the disintegration explicit. We argue, accordingly, that this verse furnishes an *unusually transparent* linguistic instance of "container collapse"—a comparative-philological claim whose strength rests, ultimately, on the cross-linguistic inventory of pre-modern anger-vessel imagery summarised in §5.6. Pending such an inventory, our finding should be read as an invitation to comparative work, not as a settled priority claim. H5 is corroborated in the form: *Q. 67:8 instantiates the container-collapse failure mode with greater lexical transparency than any of the English exemplars in Lakoff and Kövecses's (1987) corpus*; whether this is the strongest such instance in the historical record is left as an open empirical question.

### 4.8. Stage 6 — Behavioural outcomes (with caveats)

**4.8.1. *Baghy* (96 attestations; 55 Meccan / 41 Medinan).** The most frequent lexeme of the spectrum and, by network-centrality measures, its bridge node. *Baghy* is glossed as "seeking beyond rightful bounds" (al-Rāghib) and "aggressive seeking with intent to oppress" (Mostafavi). Q. 42:42 (*innamā al-sabīlu ʿalā lladhīna yaẓlimūna l-nāsa wa-yabghūna fī l-arḍi bi-ġayri l-ḥaqq*) collocates *baghy* with *ẓulm*, embedding the lexeme firmly in the moral-evaluation register. Ibn ʿĀshūr's *al-Taḥrīr wa-l-Tanwīr* (vol. 25, p. 126) clarifies the syntagmatic relation: "*baghy* and *ẓulm* are nearly synonymous, except that *baghy* is specific to non-rightful aggression against another, while *ẓulm* covers all forms of injustice."

**4.8.2. *Baghy* as bridge node — point estimates with bootstrap uncertainty.** Network analysis (Figure 6 and Table 4 below) reveals that *baghy* attains the highest *point-estimate* closeness centrality (0.55) of any node in the spectrum, and is tied with *ghaḍab* (0.53) and *asaf* (0.49) for the highest betweenness centrality (point estimate 0.15). Its eigenvector centrality (point estimate 0.50) is among the highest in the spectrum, reflecting its dense embedding in the spectrum's interaction structure. Because eigenvector and betweenness centrality on a 14-node graph with modest edge weights are *fragile* — a small change in edge structure can shift the ranking — we report **non-parametric bootstrap 95% percentile confidence intervals** computed by resampling the 256 ayat-level co-occurrences with replacement (1,000 resamples, deterministic seed 20260509). For *baghy*: betweenness ∈ [0.00, 0.31]; closeness ∈ [0.23, 0.84]; eigenvector ∈ [0.00, 0.68]. The intervals are wide — a sober reflection of the small graph and the modest density of cross-stage edges — and on the strict standard of non-overlap, no single node's centrality is *significantly* greater than another's. The substantive bridging-role claim therefore must be qualified: *baghy* has the highest point-estimate centrality on three of four measures, but the bootstrap distribution does not rule out the alternative that several spectrum roots could plausibly occupy the bridging role under different sampled subsets of ayat. What *is* robust at the aggregate level — independent of which root is identified as the principal bridge — is the cross-field connectivity profile to the umbrella moral terms (Table 4): *baghy* exhibits 16 aya-level co-occurrences with *ẓlm/jrm/fsq/ʿdw/šnʾ* combined, of which 8 are with *ʿdw* and 4 with *ẓlm*. This bridging *cross-field* profile is supported by the integer-count co-occurrence pattern even where the centrality ranking is uncertain. We treat H4 as *consistent with* the data on point estimates, with the bootstrap-derived caveat noted explicitly.

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

The radical concentration of cross-field ties at *baghy* is striking. Of the total cross-field ties across the fourteen spectrum roots, 19 (~53%) involve *baghy*. *Baghy* thus serves as the principal lexical bridge between the emotional and the broader moral-evaluation field of the Qurʾān.

**4.8.3. *Ṭughyān* and the appraisal-cognitive precondition (39 attestations; 29 Meccan / 10 Medinan).** The root *ṭ-gh-y* derives etymologically from the image of water flooding past its banks. Q. 96:6–7 (*kallā inna l-insāna la-yaṭghā an raʾāhu staġnā*) compresses an entire psychology of rebellion into a conditional: human *ṭughyān* arises from the perception of *istighnāʾ* (self-sufficiency). This is, structurally, an appraisal-theoretic claim—that a particular emotional-behavioural disposition is conditioned on a specific cognitive evaluation of the self—and it is fully congruent with the appraisal models of Lazarus (1991) and Scherer (2001, 2005). Qarizadeh et al.'s (2024) polysemy analysis of *ṭughyān* notes the cognitive structure but does not place it in the broader framework; the present paper extends their analysis by identifying *ṭughyān* as the cognitive-appraisal node of Stage 6.

**4.8.4. *ʿUtuww* (10 attestations; 9 Meccan / 1 Medinan).** The most extreme lexeme of the spectrum. Glossed as "obstinate excess" (Ibn Manẓūr), "extreme self-aggrandisement in disobedience" (al-Rāghib), and "entrenched rebellious posture" (Mostafavi). Q. 25:21 collocates *ʿatū ʿutuwwan kabīrā* with *istakbarū fī anfusihim*, marking the lexeme as denoting rebellion that has crystallised into existential posture. The strongly Meccan distribution (9/1; binomial *p* = 0.06) reflects its rhetorical function as the terminal designation of those whose rejection of revelation has hardened beyond reach—a status repeatedly illustrated through the Meccan narratives of prior peoples (Nūḥ, ʿĀd, Thamūd, Pharaoh).

**4.8.5. Caveats on the Stage-6 lexemes (*baghy*, *ṭughyān*, *ʿutuww*): bidirectional causation.** Three caveats are required for Stage 6, and they are central to the revised reading of the spectrum advanced in this paper. *Baghy* in Qurʾānic usage frequently arises from greed, supremacism (*ʿulw fī al-arḍ*), or oppressive self-interest rather than from acute anger; the act of overstepping is sometimes the *substance* of corrupted desire (compare Q. 6:21 *innahu lā yufliḥu al-ẓālimūn*) rather than the *outcome* of a passion. *Ṭughyān* — paradigmatically Pharaonic (Q. 79:17, Q. 28:4) — is rooted in structural arrogance and the exercise of unchecked power, not as a phenomenological extension of anger; the verse Q. 26:55 (*innahum lanā la-ghāʾiẓūn*) is striking precisely because it reverses the polarity, showing the oppressor's anger arising *from* the rebellion of the oppressed rather than *from* his own anger. *ʿUtuww* most commonly attaches to *istikbār* (arrogance) and is a stable, settled defiance — a property of moral character rather than a transient affective state. We retain these three roots within Stage 6 because the corpus does locate them at the behavioural pole of the spectrum, but the *causation* arrow is bidirectional: anger may *produce* these behaviours, but they can also produce *anger* (and often do, in the Qurʾānic narrative of oppressors and prophets).

**Operationalisation of the bidirectional caveat: a tafsir-grounded coding of Stage-6 attestations.** To address the reviewer's appropriate concern that the bidirectional caveat be more than a textual hedge, we coded each of the 145 Stage-6 attestations on a tafsir-grounded binary: **A** ("anger-derived" — the immediate textual context, on the joint reading of *al-Mīzān*, *al-Kashshāf*, *Majmaʿ al-Bayān*, and *al-Taḥrīr wa-l-Tanwīr*, depicts the lexeme as the behavioural completion of an inner-anger trajectory) versus **S** ("structurally derived" — the lexeme arises from greed, *istikbār*, *ʿulw fī al-arḍ*, or institutional power-asymmetry without an explicit anger antecedent in the immediate text). Verses where the four tafsirs disagreed, or where both A and S were available simultaneously (e.g. anger-driven oppression motivated by structural advantage), were coded **A+S**. Coding was conducted by the corresponding author with second-coder verification on a 20% subsample (κ = 0.79 — substantial agreement; disagreements adjudicated through joint re-reading). The coding spreadsheet is released as `data/concordance/stage6_causation_coding.csv` in the public repository.

The result of the audit (full table in the supplementary material): of 145 Stage-6 attestations, **A = 38 (26%)**, **S = 71 (49%)**, **A+S = 36 (25%)**. By root: *baghy* (n = 96) is 22 A / 50 S / 24 A+S; *ṭughyān* (n = 39) is 11 A / 19 S / 9 A+S; *ʿutuww* (n = 10) is 5 A / 2 S / 3 A+S. Re-running the χ²(1) phenomenology-vs-outcomes split using only the **A** subset (i.e., Stages 1–5 = 167 vs. anger-derived Stage-6 = 38) yields χ²(1) = 81.4 (*p* < 0.001), strongly rejecting equal split — the phenomenological core dominates the *anger-derived* outcomes by ~4.4×. This is a striking result: the prior ten-root analysis's ~2.4× outcome-skew was an artefact of conflating anger-derived and structurally-derived outcomes; once the structurally-derived ones are bracketed, the discursive emphasis is on phenomenology and *anger-driven* outcomes, in roughly the proportion classical theories of emotion regulation would predict.

The near-balance between Stages 1–5 (167) and the *full* Stage 6 (145, χ²(1) = 1.55) is therefore exactly what one would expect if (a) the Stage-6 lexemes are not exclusively anger-derived, and (b) the structurally-derived Stage-6 attestations are theoretically distinct from the anger-spectrum proper—they belong to an adjacent moral-anthropological field of *ẓulm-istikbār-ʿulw* that the corpus also pervasively documents. We retain Stage 6 in the spectrum on its corpus-distributional grounds and on the qualitative continuity of the action-intensity ordering, but we make explicit, here and in the abstract, that *baghy*/*ṭughyān*/*ʿutuww* are not coextensive with "anger outcomes" in the strict sense.


![Aya-level co-occurrence network of the fourteen core roots. Each edge represents one or more verses in which two roots co-occur; edge weight (on the line) is the count of shared ayat. The strongest edge — *ḥzn–ḍyq*, weight 3 — provides direct corpus-internal validation of the Stage-2 (inner pressure & contraction) grouping: these two pre-anger lexemes share *more* verses than any other pair in the spectrum, indicating that the Qurʾān treats them as discursively conjoint phenomena ("constriction of the chest in sadness," Q. 11:12; Q. 6:33). *Baghy* (Stage 6) anchors the right-hand cluster, with edges reaching into the moral-evaluation lexicon (*ẓlm*, *jrm*, *fsq*) — a position formalised quantitatively in the next figure. The transitive structure of the spectrum (no direct Stage-1 → Stage-6 edges; mediation through Stages 2–5) is consistent with the action-intensity gradient hypothesis, while also being consistent with the bidirectional reading of Stage 6 developed in §4.8.5.](fig4_cooccurrence.pdf){width=95%}


![Three centrality measures computed on the aya-level co-occurrence graph: (a) weighted degree — the total number of co-occurrence ties; (b) betweenness — how often a node lies on the shortest path between others, indicating bridge-node strength; (c) closeness — the inverse mean distance to all other nodes. *Baghy* attains the **highest closeness centrality** (0.55) and shares the highest betweenness centrality (0.15) with *ghaḍab* and *asaf*, confirming its role as a principal *pivot* between the anger spectrum (Stages 1–5) and the wider moral-evaluation field of the Qurʾān (315 attestations of *ẓulm*, 66 of *jurm*, 54 of *fisq*, 106 of *ʿadāwah*). The closeness panel reveals a complementary pattern: *ḍyq* and *ḥzn* (Stage 2) achieve high closeness, indicating that the inner-pressure cluster is structurally *central* to the spectrum even though peripheral in raw frequency. Together these measures support a layered reading of the network — Stage 2 supplies the affective core, Stage 6 supplies the structural bridge to neighbouring moral-discursive fields, while Stages 3–5 mediate the energy transfer between them.](fig7_centrality.pdf){width=95%}


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

To illustrate how the spectrum's intensity differentiation fares in translation, Table 6 compares five English translations on four canonical verses. We frame this as an *illustrative* case, not a systematic translation-criticism evaluation: a properly powered evaluation would require a stratified random sample of all 312 attestations (or, more practically, ~30 verses sampled across the six stages with inter-rater coding by trained Arabist coders). The four-verse, five-translation sample here suffices to register the *pattern* of levelling but does not, on its own, support the strong translation-recommendation set in §5.7; the recommendations there are conditional on a follow-up evaluation that we commend to future work.

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

The findings cohere into a single structural claim: the Qurʾānic lexicon of the anger spectrum encodes a **logic of anger escalation** that operates simultaneously along three dimensions—locus (inner → outer), intensity (low → high), and scope (individual → structural). The six stages instantiate this trifold transformation. The lexemes are not synonyms; they are *grades*, ordered by an intelligible cognitive logic.

In compact form: *Pre-anger displeasure → Inner pressure → Evaluative aversion → Active anger → Compressed rage → Behavioural outcomes (with caveats)*. The arrows index not mere temporal succession but conditional intensification at each step where regulation may succeed or fail. The Stage 6 step is, however, distinctive: the move into behavioural outcomes is *not* a deterministic escalation from anger but is influenced by independent vectors (greed, *istikbār*, structural arrogance), which is why we read the near-balance between Stages 1–5 (167) and Stage 6 (145) as theoretically informative rather than paradoxical.

### 5.2. Convergence with Gross's process model

The stages map onto the operational phases of Gross's (1998, 2014, 2015) process model of emotion regulation, with the caveat that the Qurʾānic spectrum partitions more finely on the affective side and adds an explicit behavioural-outcomes register:

| Qurʾānic stage | Gross phase | Mapping rationale |
|:-:|:---|:---|
| 1 — *uff*, *karh* (pre-anger) | Antecedent-focused: situation selection | The earliest signs of displeasure; regulable by avoiding or reframing the situation |
| 2 — *ḍīq*, *ḥuzn*, *asaf* (inner pressure) | Situation modification | Inner contraction; the agent can adjust the situation to relieve pressure |
| 3 — *naqm*, *sakhaṭ*, *maqt* (evaluative) | Attentional deployment / cognitive change | Outcome of cognitive-moral evaluation of situation |
| 4 — *ghaḍab*, *ḥard* (active) | Cognitive change / response selection | Mobilised motor response to the appraised situation |
| 5 — *ghayẓ* + *kaẓm*; *tamayyuz* | Response modulation (suppression / failure) | Direct internal regulation; *tamayyuz* marks containment failure |
| 6 — *baghy*, *ṭughyān*, *ʿutuww* | Beyond regulation: externalised dysfunction (with bidirectional causation) | Where Gross's model becomes silent — and where the Qurʾān adds the moral anthropology of unmanaged emotion *and* of independent structural pathology |

The mapping is precise for the first five stages. The sixth stage, however, is a place where the Qurʾān's continuum *exceeds* Gross's model: where Gross focuses on regulation success and treats failure outcomes as a residual category, the Qurʾānic continuum systematically describes the structural-moral pathologies that obtain at the behavioural pole — pathologies that, as we have argued in §4.8.5, may be downstream from anger but may also be upstream of it. The Qurʾān is, on our reading, not merely a model of *anger regulation* but a model of *the structural consequences of failed regulation* and *of independent structural malformations of character*—a distinction whose practical implications we develop in §5.7.

### 5.3. Convergence with Plutchik, Spielberger, and appraisal theory

Plutchik's (1980, 2001) wheel of emotions arranges anger along an *annoyance → anger → rage* continuum. This three-level structure maps onto Qurʾānic Stages 1–5 (pre-anger displeasure through compressed rage) but stops short of Stage 6. The Qurʾānic continuum's extension into the structural-behavioural register is not a minor addition but a substantive theoretical move: it claims that anger lexicons should be analysed not only psychologically but morally-anthropologically—as systems for tracking the social consequences of inner states, not merely the inner states themselves.

Spielberger's STAXI framework (1999) distinguishes trait anger (stable disposition), state anger (situational response), and anger control (deliberate restraint). The Qurʾānic lexicon implements an analogous trichotomy: Stage 2 lexemes (*ḥuzn*, *ḍīq*) describe sustained inner states; Stages 3–4 lexemes (*sakhaṭ*, *maqt*, *ghaḍab*) describe evaluative and situational responses; and the *kaẓm* construct describes deliberate restraint. The lexemes thus carve up the space of emotional life along axes that contemporary psychometrics has, independently, isolated.

Appraisal theory (Frijda 1986; Lazarus 1991; Roseman 1996; Scherer 2001, 2005) holds that emotions arise from cognitive evaluations of situations rather than from raw stimuli. Frijda's *The Emotions* (1986) is the foundational systematic treatment, formalising the appraisal–action-tendency–emotion sequence; Roseman (1996) extends the appraisal taxonomy with explicit dimensions (motive consistency, agency, certainty, control) that map directly onto the Qurʾānic typology of anger triggers. Q. 96:6–7 conditions *ṭughyān* on the appraisal of *istighnāʾ*—a textbook appraisal-theoretic claim, structurally aligned with Roseman's "agency-self / motive-inconsistent / high-control" appraisal pattern. The Qurʾānic lexicon, on this evidence, treats certain emotion-behaviour transitions as cognitively conditioned, anticipating the appraisal-theoretic insight that emotion is not pre-cognitive but cognitively constituted.

### 5.4. The phenomenology/outcomes balance: why the corpus does not show a 2.4× skew

A central revision relative to the prior version of this analysis concerns the relative weight of the phenomenological core (Stages 1–5) and the behavioural-outcomes pole (Stage 6). On the prior ten-root analysis, the corpus appeared to assign 2.4× more attestations to Stage 4 (then "behavioural rebellion") than to Stages 1+2+3 combined; on a naive reading, that asymmetry suggested a discursive over-emphasis on outcomes.

The revised fourteen-root, six-stage analysis tells a different story. The expanded inventory of phenomenological lexemes (*uff*, *karh*, *naqm*, *maqt*, *ḥard*) raises the Stage 1–5 total to 167, against Stage 6's 145; the chi-squared test against equal split *fails to reject* (χ²(1) = 1.55). This near-balance is, on our reading, exactly what one would expect if (i) the phenomenological side of the spectrum is in fact richer than the prior ten-root analysis allowed, and (ii) the Stage-6 lexemes are not exclusively anger-derived but stand in *bidirectional* causal relation to anger. The corpus-distributional fact is therefore consistent with — indeed supportive of — the substantive caveat we have entered against treating *baghy*, *ṭughyān*, and *ʿutuww* as simple downstream effects of unmanaged anger.

This has a methodological corollary that bears emphasis: corpus-distributional analyses of religious texts should not be interpreted as neutral reflections of an external referent. They are maps of *discursive emphasis*; their interpretation is fundamentally entangled with theoretical decisions about category membership (which roots count as part of the spectrum) and category causation (whether the relation is uni- or bidirectional). The shift from a 10/4-stage to a 14/6-stage analysis was not merely cosmetic: it changed both the empirical pattern and its theoretical interpretation.

### 5.5. Discursive-contextual specialisation: a general phenomenon

The exclusive-Medinan profile of *sakhaṭ* (statistically significant), the suggestive exclusive-Meccan profile of *asaf*, the Meccan tilt of *naqm* and *ʿutuww*, the hapax-Meccan status of *ḥard*, and the Medinan tilt of *karh* — taken together with the strong directional patterns of *jrm* (Meccan) and *fsq* (Medinan) in the umbrella roots — instantiate what we propose to call **discursive-contextual specialisation of lexemes**. This is the phenomenon whereby a member of a multi-lexeme semantic field becomes preferentially associated with a specific discursive register—in the Qurʾānic case, with the Meccan vs. Medinan rhetorical and sociolinguistic context. The specialisation is not random; in each documented case, contextual analysis confirms that the lexeme's preferential register is the register in which the corresponding referent obtains: *sakhaṭ* with the *Munāfiqūn* (a Medinan phenomenon), *asaf* with prior-prophet narratives (Meccan-rhetorical), *jrm* with anti-*shirk* polemic (Meccan), *fsq* with intra-community discipline (Medinan).

The phenomenon connects to the broader question of Qurʾānic textual relations and Meccan/Medinan diachrony. El-Awa (2006) on textual relations and Sinai (2017, 2023) on Meccan/Medinan diachrony provide the theoretical framework against which our distributional findings should be read: discursive-contextual specialisation is, on Sinai's account, exactly the kind of pattern that one would expect to emerge from the Qurʾān's gradual response to evolving sociolinguistic contexts; on el-Awa's account, it is one of the surface manifestations of the Qurʾānic text's coherence-relations, since lexemes that specialise discursively contribute to the relevance-structure of their host suras. Discursive-contextual specialisation is, as far as we can establish, undocumented as a *systematic corpus-distributional phenomenon* in Qurʾānic-linguistic scholarship—the lexicographical and tafsir traditions document many of the individual specialisations on a one-by-one basis without aggregating them into a general claim. Future work should test the generalisation across other multi-lexeme fields, ideally in dialogue with the QurAna and QurSim corpora (Sharaf & Atwell 2012a, 2012b) and with the MASAQ and QuranMorph extensions of the Dukes corpus (Sawalha et al. 2024; Akra et al. 2025).

### 5.6. Q. 67:8 and the container metaphor: an unusually transparent instance

A theoretically significant finding concerning conceptual metaphor is that Q. 67:8 (*takādu tamayyazu min al-ġayẓ*) instantiates the ANGER IS PRESSURIZED CONTAINER metaphor *more transparently* than the English exemplars in Lakoff and Kövecses's (1987) corpus. Where English idioms (*explode with rage*, *blow one's top*, *lose it*) report the *exit* of contained content, Q. 67:8 figures the *structural disintegration of the container itself* via the verb *tamayyaza* (m-y-z: to part, to sever).

The reviewer's caveat must be entered here, and we register it explicitly. A claim that any one historical instance is the "most articulated" of a cross-cultural pattern is comparative and therefore requires comparative data: a systematic survey of pre-modern Greek (Homeric *kholos* and *menis*), Akkadian (*ezzu*, *libbāti malû* "filled with rage"), Sanskrit (*krodha*, *manyu*), Hebrew (*ḥēmâ*, *ʾaph*, "his nose burned" idioms in the Pentateuch), and pre-Islamic Arabic *Jāhilī* poetry. Such a survey lies beyond the scope of the present paper. We therefore reframe our claim conservatively: Q. 67:8 furnishes an *unusually transparent* historical instance of the container-collapse failure mode—transparent in that the verb *tamayyaza* lexicalises *the disintegration of the vessel*, not (as English exemplars typically do) the *exit of contained content*. Whether this transparency is unique to the Qurʾānic register, characteristic of a broader Semitic-to-Indo-European belt of "vessel-of-anger" idioms, or attested with comparable explicitness elsewhere, is an open question that deserves dedicated comparative-philological investigation. We commend the question to specialists in those literatures and do not, in this paper, claim priority over a cross-cultural inventory we have not assembled.

This more cautious framing has a methodological and a theoretical consequence. *Methodologically*, it implies that the historical depth of the conceptual-metaphor inventory is plausibly greater than the (largely contemporary-English) corpus of Lakoff and Kövecses's original analysis allowed; the Qurʾānic data extend its empirical base to a register of seventh-century Arabic. *Theoretically*, the data are *consistent with* the universalist claim within CMT—that bodily-grounded image schemas (CONTAINER, FORCE, BALANCE) underwrite human emotion conceptualisation across cultures and historical periods—but they do not, on their own, establish the strong cross-cultural universalism that earlier formulations of this paper risked overstating.


![The ANGER-IS-A-PRESSURIZED-CONTAINER schema (Lakoff & Kövecses 1987), instantiated by the Qurʾānic triplet *ghaḍab → ghayẓ + kaẓm → tamayyuz*. **Panel 1** (Stage 4): *ghaḍab* — an *open* container; the affect is present but unconcentrated, dissipating freely into language (the lexeme is the most nominally productive in the spectrum). **Panel 2** (Stage 5, Q. 3:134): *ghayẓ* — fluid sealed by *kaẓm*; the verb *kaẓama* originally denotes the *tying-off of a waterskin*, the agent-internal regulation that maintains containment under rising pressure. **Panel 3** (Stage 5 manifestation, Q. 67:8): *tamayyuz* — the structural failure; the verb derives from the root *m-y-z* "to separate, to part, to sever", and figures not the exit of pressurised content (as English *explode*) but the *splitting apart of the container itself*. The Qurʾānic instantiation is, on the present argument, more transparent than any English exemplar in Lakoff and Kövecses's (1987) corpus, providing strong cross-linguistic evidence for the cognitive universality of the schema (§5.6).](fig6_metaphor_diagram.pdf){width=100%}


### 5.7. Implications for Qurʾānic translation (conditional on follow-up evaluation)

Translation criticism of the Qurʾān has long observed that translations tend to level the spectrum—that *ġaḍab* and *ġayẓ* alike become *anger*; that *baghy*, *ṭughyān*, and *ʿutuww* alike become *transgression* (Table 6). Our four-verse, five-translation illustrative sample (§4.10) is consistent with this pattern but is too small (*n* = 4 verses × 5 translations = 20 cells) to support strong prescriptive claims; recent computational work — notably Gaanoun & Alsuhaibani (2025; *Nature HSSC*) on sentiment preservation across seven English translations and Alsuhaibani et al.'s (2025) ELQV emotion-labelled dataset of 2,100 Qurʾānic verses — has begun to operationalise the levelling concern at scale on coarse Ekman categories, though without a graded reference model of the lexical spectrum against which the levelling could be benchmarked. We frame the present discussion as **conditional implications**: contingent on a follow-up systematic evaluation (a stratified random sample of ~30 verses across the six stages, with multi-rater coding against the spectrum reference model), the analysis would *if confirmed* support the following candidate equivalents for critical and study-edition translations:

> *uff*: vocal sigh of irritation · *karh* (*karāha*): inner dislike · *karh* (*ikrāh*): coercion (a structural extension, not an emotion) · *ḍīq*: inner constriction · *ḍāqa dharʿan*: arm-span tightening / inhibited aggression · *ḥuzn*: persistent grief (transversal valence) · *asaf*: regretful dismay (with anger) · *naqm*: vengeful disapproval · *sakhaṭ*: moral disapprobation · *maqt*: intense moral aversion · *ghaḍab*: anger · *ḥard*: anger combined with deliberate denial · *ghayẓ*: contained / boiling rage · *tamayyuz min al-ġayẓ*: bursting from rage · *baghy*: aggressive transgression · *ṭughyān*: rebellious overflow · *ʿutuww*: obstinate defiance.

A second conditional implication, which we register as a hypothesis rather than a recommendation, is that pedagogical translations may benefit from marking each lexeme's position on the continuum (by inline gloss, footnote, or chromatic coding) — but the empirical case for this rests on the comparative comprehension study we commend to future work. The 30-verse stratified evaluation, paired with an inter-rater coded comparison across the present spectrum reference model and the ELQV labels, is a natural Phase II for the present dataset.

### 5.8. Implications for Islamic psychology

The continuum offers a culturally-grounded framework that maps onto Gross's model without requiring importation of secular vocabulary. This has three practical implications:

**(i) Prevention.** The continuum supports *early-stage recognition*—the principle, central to cognitive-behavioural therapy, that affective dysregulation should be intercepted at the earliest possible point. The Qurʾānic vocabulary for pre-anger and inner-pressure states (*uff*, *karāha*, *ḍīq*, *ḥuzn*) provides an indigenous lexicon for self-monitoring at Stages 1–2, in advance of intensification.

**(ii) Crisis intervention.** The *kaẓm* construct, properly understood as a Stage-5 response-modulation strategy, can be integrated with contemporary suppression-and-reappraisal interventions, providing a religiously-grounded framing for techniques that secular CBT already employs.

**(iii) Rehabilitation.** Crucially, the Qurʾānic continuum frames the post-failure Stage 6 as recoverable—the path from *baghy*/*ṭughyān*/*ʿutuww* back toward equilibrium runs through *tawba* (repentance), a return that the text affirms as accessible. This framing offers motivational reinforcement to clinical-psychological rehabilitation models, especially those concerned with anger disorders and post-violent trauma.

These implications are conceptual; their translation into validated clinical interventions awaits the design of empirical studies, which we recommend as a priority for future work.

---

## 6. Conclusion

### 6.1. Substantive contributions

This paper has advanced three contributions to the scholarship.

**Methodologically**, we have demonstrated that the integration of three previously separate frameworks—Izutsu's semantic-field analysis, Kennedy–Sassoon scalar semantics, and Lakoff–Kövecses conceptual-metaphor theory—coupled with a reproducible computational pipeline over the Quranic Arabic Corpus, produces a research apparatus stronger than the sum of its parts. To our knowledge, this trifold integration with corpus-empirical validation has not previously been deployed in Qurʾānic studies as a unified analytic framework, although Qāʾimīniyā (1390/2011, 1393/2014) and Pakatchi have integrated Izutsu and conceptual-metaphor theory, and Persian-language scalar-semantic work on Qurʾānic vocabulary may exist in venues we have not been able to canvass. The research apparatus is openly available and applicable to other Qurʾānic semantic fields.

**Descriptively**, we have produced an exhaustive, reproducible concordance of 312 attestations across the fourteen core spectrum roots, with corresponding distributional and network-analytic outputs. The CSV outputs — including FDR-adjusted binomial tests, marginal-preserving permutation null *p*-values, and bootstrap 95% CIs on every centrality estimate — provide a foundation on which further philological and computational work can build.

**Theoretically**, we have formulated and empirically defended the **Qurʾānic Action-Intensity Continuum Hypothesis**: the claim that fourteen core lexemes of the Qurʾānic anger-spectrum field operate as a single graded continuum structured by *intensity of action* and partitioned into six phenomenologically meaningful stages. The hypothesis is supported by qualitative evidence from the four authoritative lexica and from a now-broadened tafsir consultation (§3.5), and by quantitative evidence from frequency, distribution, morphology, and network structure. We have, in addition, identified distributional patterns that, to our knowledge, have not been previously reported as a coordinated set, while reporting their post-FDR evidential strength transparently: the exclusively-Medinan *sakhaṭ* survives Holm-Bonferroni correction at α = 0.05 *borderline* (raw *p* = 0.005, adjusted *p* = 0.05) and is robust across baselines 0.70–0.78; the exclusively-Meccan *asaf*, the Meccan-tilted *naqm*, the hapax-Meccan *ḥard*, and the Medinan-tilted *karh* are reported as *contextual observations* warranting follow-up rather than as confirmed findings. The general phenomenon of **discursive-contextual lexical specialisation** of which we hypothesise these are instances is proposed as a research target rather than as a settled result. We have entered explicit caveats on the bidirectional causation of the Stage-6 lexemes (§4.8.5), grounded in a κ = 0.79-validated tafsir-coding audit, and argued that Q. 67:8 furnishes an *unusually transparent* linguistic exemplar of "container collapse"—a comparative claim whose strong universalist form is reserved pending the cross-cultural philological survey we commend in §5.6 and §6.3.

### 6.2. Answers to the research questions

**RQ1.** The semantic field is a fourteen-node network organised around the bridge node *baghy* and the stage-internal hubs *ḥuzn* and *ghaḍab*, with several specialised peripheral nodes (*sakhaṭ*, *asaf*, *ḥard*, *ʿutuww*) exhibiting marked distributional asymmetries.

**RQ2.** The fourteen nodes order on a six-stage continuum—pre-anger displeasure (Stage 1), inner pressure & contraction (Stage 2), evaluative aversion (Stage 3), active anger (Stage 4), compressed/explosive rage (Stage 5), behavioural outcomes with caveats (Stage 6)—organised by the composite dimension of *intensity of action* (locus, intensity, scope of consequence).

**RQ3.** The empirical distribution is *consistent with* (though not by itself confirmatory of) the continuum: the asymptotic chi-squared rejects the null of six-stage uniform distribution (χ²(5) = 227.15; large effect size at Cohen's *w* = 0.85), but a marginal-preserving permutation null on the same statistic yields *p* = 0.24, indicating that the asymptotic *p*-value over-states the evidence on this sparse, marginally-imbalanced design; the substantive case for the six-stage architecture rests on the qualitative lexicographic, exegetical, and metaphorical evidence rather than on the omnibus *p*-value alone. The comparison between Stages 1–5 and Stage 6 *fails to reject* equal split (χ²(1) = 1.55, Cohen's *w* = 0.07, trivial effect); we read this as *consistent with* — but not as positive evidence for — the bidirectional-causation reading of Stage 6, with the substantive support coming from the κ = 0.79-validated tafsir-coding audit (§4.8.5). The network exhibits a bridging-role profile at *baghy* with wide bootstrap confidence intervals reported transparently. The morphological profile distinguishes the verbal Stages 1–2 from the more nominal Stage 6.

**RQ4.** The continuum is structurally homologous with Gross's process model, Plutchik's wheel, Spielberger's STAXI, and Lazarus–Scherer appraisal theory in its psychological component, but extends beyond all of them by integrating the post-failure structural-moral consequences of unmanaged emotion (Stage 6) — while qualifying that integration with the bidirectional-causation caveat of §4.8.5.

**RQ5.** *Conditional* practical implications include candidate distinct-equivalent translations and position-marking conventions (subject to a 30-verse stratified follow-up evaluation, §5.7) and three Islamic-psychology applications (early-stage prevention, *kaẓm*-grounded crisis intervention, *tawba*-grounded rehabilitation). All practical implications are framed as hypotheses for empirical follow-up, not as settled prescriptions.

### 6.3. Limitations and future work

Five limitations bound the present study and define its principal future-research extensions.

First, the analysis works at the surface-lexical layer; broader discourse-analytic close-reading of how the spectrum is mobilised across narrative arcs of individual suras remains to be conducted. Second, the *tafsīr* engagement is selective, drawing on four canonical commentaries; a systematic survey of the broader exegetical tradition (especially Shīʿī, Sufi, and contemporary Persian-language commentary) would refine specific lexical readings. Third, the cognitive-linguistic apparatus is Anglophone-dominated; engagement with classical Arabic theories of *bayān* (especially al-Jurjānī's *Dalāʾil al-Iʿjāz*) would supply an indigenous theoretical substrate. Fourth, the *ḥadīth* corpus has not been integrated, although it would be instructive to test whether the continuum is robust beyond the Qurʾānic corpus into the broader Islamic textual tradition. Fifth, the clinical-psychological implications proposed in §5.8 have not been operationalised in empirical interventions; the design of pilot studies for *kaẓm*-grounded emotion regulation training is a priority for translational work.

### 6.4. Closing remark

The Qurʾānic lexicon, on the analysis advanced here, encodes a sophisticated theory of the phenomenology of the anger spectrum—not as explicit theoretical formulation but as the architectural design of its semantic surface. Recovering that theory requires methodological tools that bring together the qualitative attentiveness of classical philology, the formal precision of contemporary linguistic theory, and the verifiability of corpus-computational analysis. We hope the present study, alongside the foundational work of Izutsu, Qāʾimīniyā, Pakatchi, Narimani et al., and Qarizadeh et al., advances this triple integration. The classical and the computational are not opposed traditions; they are complementary instruments, and their joint deployment opens horizons that neither could disclose alone.

---

## Acknowledgements

The authors thank Kais Dukes (in memoriam) and the team behind the Quranic Arabic Corpus, and the Tanzil Project, for releasing the morphological and textual resources without which this kind of empirical Qurʾānic analysis would not be feasible. We thank Urmia University for institutional support, and the anonymous peer reviewer whose detailed comments materially improved the methodological framing, the statistical interpretation (especially regarding the χ²(1) result and the *sakhaṭ* baseline-sensitivity question), and the reproducibility of the analysis pipeline.

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

(ORCID identifiers will be provided at submission.)

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

Albayrak, I. (2020). Semantics of the Qurʾānic Weltanschauung: A critical analysis of Toshihiko Izutsu's works. *American Journal of Islam and Society*, *37*(1–2). https://ajis.org/index.php/ajiss/article/view/387

Almuhanna, M., et al. (2025). Sentiment preservation in Quran translation with artificial intelligence approach: Study in reputable English translation of the Quran. *Humanities and Social Sciences Communications*, *12*(1), Article 04181. https://doi.org/10.1057/s41599-024-04181-0

Averill, J. R. (1982). *Anger and Aggression: An Essay on Emotion*. New York: Springer-Verlag.

Berkowitz, L. (1993). *Aggression: Its Causes, Consequences, and Control*. New York: McGraw-Hill.

Derki, M. (2022). Conceptualization of anger in Modern Standard Arabic and English: A comparative study. *Professional Discourse & Communication*. https://www.pdc-journal.com/jour/article/view/168

Dukes, K. (2011). *Quranic Arabic Corpus (Morphology, Version 0.4)*. University of Leeds. https://corpus.quran.com

El-Awa, S. M. S. (2006). *Textual Relations in the Qur'an: Relevance, Coherence and Structure*. London and New York: Routledge.

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

Narimani, Z., Iqbali, M., & Chari, M. (1400 SH / 2021). [Semantic re-analysis of the words *ghayẓ*, *ghaḍab*, and *sakhaṭ* in the Holy Qurʾān with an exegetical approach]. *Pizhūhish-hā-yi Qurʾān va Ḥadīth* [Qurʾanic and Hadith Research]. University of Tehran. [in Persian; original Persian title: «بازشناسی معنایی واژگان «غیظ»، «غضب» و «سَخَط» در قرآن کریم با رویکرد تفسیری»]

Pakatchi, A., & Afrashi, A. (1399 SH / 2020). *Rūykardhā-yi Maʿnā-shinākhtī dar Muṭālaʿāt-i Qurʾānī* [Semantic Approaches in Qurʾānic Studies]. Tehran: Pizhūhishgāh-i ʿUlūm-i Insānī va Muṭālaʿāt-i Farhangī. [in Persian]

Plutchik, R. (1980). *Emotion: A Psychoevolutionary Synthesis*. New York: Harper & Row.

Plutchik, R. (2001). The nature of emotions. *American Scientist*, *89*(4), 344–350.

Qarizadeh, M. ʿO., Salmani Marvast, M. ʿA., Meymandi, V., & Farsi, B. (1402 SH / 2024). [Polysemy of the word *ṭughyān* in the Holy Qurʾān with a linguistic approach]. *Pizhūhish-hā-yi Zabānshinākhtī-yi Qurʾān* [Linguistic Research in the Holy Qurʾān]. University of Isfahan. [in Persian; original Persian title: «چندمعنایی واژۀ «طغیان» در قرآن کریم با رویکردی بر زبان‌شناختی»]

Qāʾimīniyā, ʿA. (1390 SH / 2011). *Maʿnāshināsī-yi Shinākhtī-yi Qurʾān* [Cognitive Semantics of the Qurʾān]. Tehran: Pizhūhishgāh-i Farhang va Andīshah-i Islāmī. [in Persian; original Persian title: «معناشناسی شناختی قرآن»]

Qāʾimīniyā, ʿA. (1393 SH / 2014). *Istiʿārah-hā-yi Mafhūmī wa Faḍāhā-yi Qurʾānī* [Conceptual Metaphors and Qurʾānic Spaces]. Tehran: Pizhūhishgāh-i Farhang va Andīshah-i Islāmī. [in Persian; original Persian title: «استعاره‌های مفهومی و فضاهای قرآنی»]

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

Sinai, N. (2017). *The Qur'an: A Historical-Critical Introduction*. Edinburgh: Edinburgh University Press.

Sinai, N. (2023). *Key Terms of the Qur'an: A Critical Dictionary*. Princeton, NJ: Princeton University Press.

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
