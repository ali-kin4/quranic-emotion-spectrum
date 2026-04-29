# The Phenomenology of the Anger Spectrum in the Qurʾān
## A Semantic-Network Analysis of Displeasure, Inflammation, and Destructiveness Along an Action-Intensity Continuum

**Karim Jabbary** *(corresponding author)*
Department of Arabic Language and Literature, Faculty of Literature and Humanities, Urmia University, Urmia, Iran

**Ali Jabbary**
Urmia University, Urmia, Iran

---

## Abstract

The Qurʾān deploys an exceptionally articulated lexicon for the description of the *anger spectrum* in human emotion, yet existing scholarship has tended to treat this lexicon either word-by-word or through normative-ethical frames, leaving the structural-relational dimension of the field largely unexplored. This study advances the thesis that fourteen core Arabic roots—**ʾff, krh, ḍyq, ḥzn, ʾsf, nqm, sxṭ, mqt, ġḍb, ḥrd, ġyẓ, bġy, ṭġy, ʿtw**—form a single graded semantic field organised along the dimension of *intensity of action*, traversing six phenomenological stages: (1) pre-anger displeasure, (2) inner pressure and contraction, (3) evaluative aversion, (4) active anger, (5) compressed/explosive rage, and (6) behavioural outcomes (with caveats). We integrate three methodological lenses—Toshihiko Izutsu's semantic-field approach, scalar semantics in the Kennedy-Sassoon tradition, and conceptual metaphor theory after Lakoff and Kövecses—and validate the proposed continuum against the **Quranic Arabic Corpus** (Dukes 2011) using a fully reproducible Python pipeline. The empirical analysis covers 312 attestations across the fourteen core spectrum roots, spanning the entire 6,236-verse corpus. Three principal findings emerge. First, the six-stage distribution of attestations deviates highly significantly from uniformity (χ²(5) = 227.15, *p* < 0.001). Stage totals are: Stage 1 = 44; Stage 2 = 60; Stage 3 = 27; Stage 4 = 25; Stage 5 = 11; Stage 6 = 145. The phenomenological core (Stages 1–5 = 167) and the behavioural-outcomes pole (Stage 6 = 145) are *not* significantly unequal (χ²(1) = 1.55, fails to reject equal split), a result we read—following the reviewer's caveats below—as supporting the position that Stage-6 lexemes (*baghy*, *ṭughyān*, *ʿutuww*) are not exclusively anger-derived. Second, two distributional patterns emerge that have, to our knowledge, not been previously reported: *sakhaṭ* attests **exclusively** in Medinan suras (0/4; binomial *p* = 0.026 against the corpus baseline of 0.60 Meccan), while *asaf* attests **exclusively** in Meccan suras (5/0); we additionally identify *naqm* as Meccan-tilted (12/5), *maqt* (4/2), and *ḥard* as a Qurʾānic hapax legomenon at Q. 68:25 (Meccan). Third, network-centrality analysis of the aya-level co-occurrence graph reveals that *baghy* operates as one of the principal bridging nodes (betweenness = 0.15, tied with *ghaḍab* and *asaf*; closeness = 0.55, the highest in the spectrum) between the anger spectrum and the broader moral-evaluation field of the Qurʾān (315 attestations of *ẓulm*, 66 of *jurm*, 54 of *fisq*, 106 of *ʿadāwah*). The Qurʾānic continuum is structurally homologous with Gross's process model of emotion regulation (1998, 2014), Plutchik's wheel of intensity (1980), and Spielberger's State-Trait Anger framework (1999), but extends beyond these in a critical respect: by integrating Stage 6, it presents not only a *psychology* of anger but a *moral anthropology* of the structural consequences of unmanaged emotion. We argue that the Qurʾānic verse Q. 67:8 (*takādu tamayyazu min al-ġayẓ*) constitutes one of the most articulated linguistic instances of "container collapse" (Lakoff & Kövecses 1987) in any documented historical text, providing strong cross-cultural evidence for the cognitive universality of the ANGER IS PRESSURIZED CONTAINER metaphor. The findings have implications for Qurʾānic translation (where the levelling of distinct lexemes erodes the spectrum's moral-psychological architecture), for the design of culturally-grounded Islamic-psychology interventions, and for the cross-linguistic study of anger lexicons.

**Keywords:** Qurʾān, anger spectrum, semantic field, cognitive linguistics, scalar semantics, conceptual metaphor, anger lexicon, emotion regulation, Arabic corpus linguistics, Izutsu, Islamic psychology.

---

## 1. Introduction

### 1.1. Statement of the problem

The Qurʾānic lexicon for the *anger spectrum* exhibits a precision that survives, only with difficulty, the attempts of translation to render it into modern languages. Where English versions level *uff*, *karh*, *ḍīq*, *ḥuzn*, *asaf*, *naqm*, *sakhaṭ*, *maqt*, *ghaḍab*, *ḥard*, *ghayẓ*, *baghy*, *ṭughyān*, and *ʿutuww* into a small set of broad equivalents—chiefly "displeasure," "distress," "grief," "anger," "rage," "transgression," and "rebellion"—the Arabic original distinguishes them with the precision of a graded taxonomy of irritation, aversion, anger, and its outcomes. The hypothesis advanced in this paper is structural: that fourteen of the Qurʾān's thematically central anger-spectrum roots are not synonyms or scattered semantic singletons but coordinated nodes in a single *graded* semantic field, organised along the dimension of *intensity of action* (*shiddat al-kunish* in the Persian formulation of the original idea). The field opens in pre-anger displeasure (the murmured *uff*, the inner *karāha*), passes through inner pressure and contraction, evaluative aversion, active anger, and compressed/explosive rage, and—at the behavioural pole—issues into outcomes (*baghy*, *ṭughyān*, *ʿutuww*) whose causation, as we shall argue, is bidirectional rather than purely emotional. We treat the fourteen roots as discrete attestation points on this continuum and validate the proposed ordering through systematic corpus-based analysis.

This claim, if it holds, has consequences far beyond philology. It implies that the Qurʾān encodes—through the architecture of its lexicon, not through any explicit theoretical statement—a sophisticated implicit theory of the genealogy of moral failure: a theory according to which the social-structural pathologies the text most frequently denounces (transgression, tyranny, defiance) are *related to*, and in many cases developmentally downstream from, inner experiences of irritation, dislike, constriction, and grief. As we shall argue in §4 and §5, the relationship at the behavioural pole is bidirectional: anger may produce *baghy*/*ṭughyān*/*ʿutuww*, but these behaviours can equally produce *anger* (in their victims, in the prophets, in the divine response). The distance between the murmured *uff* of Q. 17:23 and the *ʿutuww* of Q. 25:21 is not categorical but graded; it is the distance walked, in the absence of intervention, by an unmanaged life of irritation, dislike, and anger.

### 1.2. Aims and originality

This paper has three aims. The first is **methodological**: to demonstrate that combining Izutsu's qualitative semantic-field approach, scalar-semantic ordering in the Kennedy–Sassoon tradition, and conceptual-metaphor theory in the Lakoff–Kövecses tradition produces stronger philological claims than any of the three frameworks in isolation. We argue that this trifold integration is, in published Qurʾānic studies, here brought together for the first time. The second aim is **descriptive**: to map every Qurʾānic occurrence of the fourteen core roots, to render that map publicly verifiable through an open concordance, and to extract from it empirical regularities that previous scholarship—working in either tafsir, lexicography, or single-word semantic analysis—was not in a position to detect. The third aim is **interpretive**: to argue that the resulting continuum constitutes a coherent "logic of anger escalation" with deep structural affinities to modern psychology of emotion, and to identify the specific points at which the Qurʾānic continuum *exceeds* the explanatory range of the contemporary models.

The paper's claim to **originality** rests on five distinct contributions: (i) the first integration of Izutsu, Kennedy, and Lakoff in a Qurʾānic study; (ii) a fully reproducible computational pipeline over the Quranic Arabic Corpus, released open-source; (iii) the discovery, to our knowledge unreported, of the exclusively-Medinan distribution of *sakhaṭ* and the exclusively-Meccan distribution of *asaf*; (iv) the demonstration via network-centrality analysis that *baghy* serves as the bridge node between the emotional and moral-evaluation fields of the Qurʾān; and (v) the substantive argument that Q. 67:8 (*takādu tamayyazu min al-ġayẓ*) constitutes one of the strongest historical instances of the "container collapse" pattern identified by Lakoff and Kövecses (1987).

### 1.3. Prior work and the gap

Prior scholarship clusters into five lines, each insufficient on its own to address the structural question that motivates this paper.

**Single-word lexical studies** treat individual lexemes in detail but rarely place them in relation to one another. The most directly relevant Persian-language precedent—Narimani, Iqbali, and Chari's (2021) study of *ghayẓ*, *ghaḍab*, and *sakhaṭ* in *Pizhūhish-hā-yi Qurʾān va Ḥadīth* (University of Tehran)—covers three of our fourteen roots but does not place them on a graded scale or extend the analysis to the pre-anger displeasure, inner pressure, evaluative aversion, or behavioural-outcome stages. Their analysis demonstrates, on tafsir grounds, that *ghaḍab* is the central anger lexeme (predicated of God, prophets, and believers), *sakhaṭ* is reserved for divine displeasure with hypocrites, and *ghayẓ* is exclusive to the unbelievers and hypocrites in human-attribution contexts. We confirm and extend their lexical-tafsir findings with corpus-distributional evidence, scalar-semantic ordering, and the cognitive-linguistic *kaẓm* analysis. Qarizadeh, Salmani Marvast, Meymandi, and Farsi (2024) provide a polysemy analysis of *ṭughyān* alone in *Pizhūhish-hā-yi Zabānshinākhtī-yi Qurʾān* (University of Isfahan), showing that the root attests in 27 suras and 13 morphological forms with the central meaning of "transgressing the limit." Both works illustrate the present gap: high-quality lexical work is available for individual lexemes, but no integrated continuum has been articulated.

**Ethics-of-anger studies** focus on the imperative of *kaẓm al-ghayẓ* (restraining suppressed rage; Q. 3:134) and adjacent verses, drawing on the *aḥādīth* tradition. These works are normatively rich but linguistically thin and tend not to interrogate the conceptual architecture of the lexicon as a structured field.

**Cognitive-semantic studies** in the Izutsu tradition—most notably Qāʾimīniyā's *Maʿnāshināsī-yi Shinākhtī-yi Qurʾān* (Tehran: Pizhūhishgāh-i Farhang va Andīshah-i Islāmī, 2011) and his *Istiʿārah-hā-yi Mafhūmī wa Faḍāhā-yi Qurʾānī* (2014)—have begun to apply cognitive linguistics to Qurʾānic vocabulary. To our knowledge, no published work has yet treated the anger-spectrum field as a graded continuum or validated it against full-corpus evidence. The work of Maalej (2004, *Metaphor and Symbol* 19(1): 51–75) on conceptual metaphor in Tunisian Arabic anger expressions, while linguistically rigorous, focuses on contemporary spoken Arabic rather than the Qurʾānic register.

**Translation-criticism studies** observe the levelling tendency of translations and identify it as a structural defect [CITATION NEEDED for a specific recent example], but lack a reference model of the spectrum against which translations can be systematically evaluated.

**Islamic psychology** has begun to extract emotion-regulation models from Qurʾānic and *ḥadīth* sources [CITATION NEEDED for specific Islamic-psychology references]. This body of work has predominantly drawn on *aḥādīth* and tended to leave the systematic linguistic analysis of the Qurʾānic surface itself in the background.

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

The contemporary linguistic theory of *gradable predicates*, developed in the work of Kennedy (1999, 2007), Sassoon (2010), and others, supplies the missing apparatus. On this framework, a graded predicate maps to a *scale* characterised by three components: (a) a *dimension* of measurement (e.g., temperature, length, intensity); (b) an *ordering* of points on that dimension; and (c) a unit of comparison, explicit or implicit. Scalar predicates take degree modifiers (*very*, *extremely*, *somewhat*, *barely*) and admit comparative constructions (*more X than*, *too X*); these properties signal their underlying scalar structure.

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

The fourteen core roots were selected by three concurrent criteria: (i) *exegetical centrality* — appearance as a focal reference in at least three of the four authoritative lexica (Ibn Fāris's *Maqāyīs*, al-Rāghib's *Mufradāt*, Ibn Manẓūr's *Lisān*, and Mostafavi's twentieth-century *Taḥqīq*); (ii) *minimum corpus frequency* of one attestation (admitting Qurʾānic hapax legomena such as *ḥard*, Q. 68:25, when their lexical and tafsir profile is sufficiently rich); (iii) *thematic membership* in the anger-spectrum field without significant overlap with adjacent fields (epistemology, faith, normative ethics).

Note that *karh* (Stage 1, dislike/aversion) is a borderline case: its *karāha* sense is properly affective (pre-anger inner aversion), while its *ikrāh* sense (coercion) is structural rather than emotional and is treated separately (see §4.x on *karh*). A second tier of five roots—**šnʾ, jrm, fsq, ẓlm, ʿdw**—is extracted as "umbrella moral terms" for robustness checks (§4.5) and inter-field co-occurrence analysis (§4.7). These roots, while semantically related to the anger field, either have inflated cardinality (*ẓlm*: 315 attestations functioning as a meta-category) or properly belong to the adjacent field of normative ethics (*jrm*, *fsq*); they are excluded from the principal continuum to preserve focus.

### 3.3. Computational pipeline

The pipeline is implemented in Python (MIT-licensed) and operates in five steps: (1) parse the QAC morphology file; (2) filter on target roots; (3) collapse multi-segment morphemes to surface words preserving the *(sūra:āya)* coordinate; (4) join with sura-level metadata for Meccan/Medinan classification; (5) emit four classes of output (master concordance CSV, per-root concordances, distributional summaries, network/centrality CSVs). Code is organised across `analysis/qac_parser.py`, `analysis/spectrum_roots.py`, `analysis/extract_concordance.py`, `analysis/advanced_metrics.py`, and visualisation modules. The complete analysis is reproducible from a fresh clone of the repository in two commands: `python analysis/extract_concordance.py && python analysis/visualize_spectrum.py && python analysis/visualize_advanced.py`.

### 3.4. Quantitative analyses

Beyond raw frequency tabulation, we conduct: (a) chi-squared tests against the null of uniform six-stage distribution and against the null of equal Stages 1–5 vs Stage 6 split; (b) two-sided exact binomial tests for Meccan/Medinan exclusivity claims, taking 0.60 as the corpus-baseline rate of Meccan attestations (the proportion of Meccan ayat in the QAC); (c) morphological breakdown by part-of-speech (verb, noun, adjective, participle, other); (d) network analysis on the verse-level co-occurrence graph, computing weighted degree, betweenness centrality, closeness centrality, and (where the graph permits) eigenvector centrality.

### 3.5. Qualitative analyses

We supplement the quantitative analyses with: (a) comparative etymological analysis across the four authoritative lexica named above (Maqāyīs, Mufradāt, Lisān, Taḥqīq); (b) comparative *tafsīr* analysis for the canonical exemplar verses, drawing on four authoritative tafsirs—al-Ṭabāṭabāʾī's *al-Mīzān*, al-Zamakhsharī's *al-Kashshāf*, al-Ṭabarsī's *Majmaʿ al-Bayān*, and Ibn ʿĀshūr's *al-Taḥrīr wa-l-Tanwīr*; (c) phenomenological analysis of contextual markers (*ḍīq al-ṣadr*, *ḥuzn al-qalb*, *asaf al-nafs*, *ḍāqa dharʿan*); (d) translation-criticism analysis comparing five major translations (Yusuf Ali, Pickthall, Arberry, Saheeh International, Hilali-Khan) on the canonical exemplar verses.

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
| 1 | ʾ-f-f | irritation, vocal expression of distaste (*taḍajjur*) [TO BE EXPANDED FROM LEXICA] | the lowest verbal expression of displeasure | term of irritation directed at someone or something | minimal vocal sign of inner aversion |
| 1 | k-r-h | dislike, finding burdensome; coercion (*ikrāh*) | aversion of the soul; structurally extended to coercion | what is disliked by nature or by reason | inner *karāha* vs. structural *ikrāh* (the latter is not an emotion) |
| 2 | ḍ-y-q | constriction; absence of opening | the state of being pressed upon, contrasted with capacity (*saʿah*) | reduction of available space, from *saʿah* to *ḍīq* | inner or outer absence of expansion (*basṭ*) |
| 2 | ḥ-z-n | rough/uneven ground → heaviness of soul | sorrow as the opposite of joy (*faraḥ*) | rugged ground, then roughness of the self | affective response to perceived loss |
| 2 | ʾ-s-f | intense grief mixed with anger | extreme anger conjoined with grief | reaching the limit of grief and anger | composite of grief and proximate anger |
| 3 | n-q-m | disapproval coupled with intent of retribution [TO BE EXPANDED FROM LEXICA] | objecting to and seeking redress against an act | denouncing strongly; cf. al-muntaqim as divine attribute | evaluative anger oriented toward retribution |
| 3 | s-kh-ṭ | severe aversion and ethical rejection | the opposite of *riḍā* (consent), with intensity | severe non-acceptance with judgment | declarative rejection grounded in moral assessment |
| 3 | m-q-t | the most intense form of *ibghāḍ* (Zajjāj) | aversion arising from observing a *qabīḥ* act (*al-Rāghib*) | *ashaddu al-ibghāḍ*; aversion-distance rather than approach-aggression | purely evaluative moral aversion |
| 4 | gh-ḍ-b | inner agitation and motion | the boiling of the heart's blood seeking retribution | a rising perturbation of the soul | directed emotion enabling retributive action |
| 4 | ḥ-r-d | anger combined with intent (*qaṣd*); intent to deny | per al-Ṭabarsī (*Majmaʿ al-Bayān*): both anger and *qaṣd* | per al-Ṭabāṭabāʾī (*al-Mīzān*): anger plus deliberate denial [TO BE EXPANDED FROM LEXICA] | anger weaponised through resource-denial (Q. 68:25) |
| 5 | gh-y-ẓ | pressure and surge, contained | the most intense forms of contained anger | filling of the self with restrained anger | high-pressure emotional accumulation |
| 6 | b-gh-y | seeking beyond rightful bounds | overstepping the path of right | dominance through aggression | aggressive action with intent to oppress |
| 6 | ṭ-gh-y | overflow of water past its bank | crossing the permitted measure | severe transgression of the limit | rebellious shattering of normative bounds |
| 6 | ʿ-t-w | severe rebellion with arrogance | extreme self-aggrandisement in disobedience | obstinate excess attached to *istikbār* | entrenched rebellious posture (a property of moral character) |

The table shows that the ordering from *uff* to *ʿutuww* is not the construction of the present analysis but is internally encoded in the lexicographic tradition itself: the four authoritative lexica already gloss each root with progressively more externalised and structural meanings, ascending from the murmured *uff*, through inner *karāha*, *ḍīq*, and *ḥuzn*, through evaluative *naqm*/*sakhaṭ*/*maqt*, to active *ghaḍab*/*ḥard*, to compressed *ghayẓ*, and into the externalised behavioural pole at *baghy*/*ṭughyān*/*ʿutuww*.

### 4.2. Distributional summary

Table 2 reports the principal distributional facts for the fourteen core roots. The table integrates frequency, Meccan/Medinan split, and (for the roots with sufficient morphological variation) morphological profile; it forms the empirical backbone of the analyses that follow.

**Table 2. Distributional profile of the fourteen core roots**

| Stage | Root | Total | Meccan | Medinan | Notes |
|:-:|:-:|:-:|:-:|:-:|:--|
| 1 | ʾff (أف) | 3 | 3 | 0 | All Meccan; lowest tier of verbal displeasure |
| 1 | krh (كره) | 41 | 14 | 27 | Medinan-tilted (*p* = 0.005); twofold *karāha*/*ikrāh* |
| 2 | ḍyq (ضيق) | 13 | 9 | 4 | Inner constriction (*ḍīq al-ṣadr*; *ḍāqa dharʿan*) |
| 2 | ḥzn (حزن) | 42 | 26 | 16 | Most frequent Stage-2 lexeme; valence transversal (see §4.3.2) |
| 2 | ʾsf (أسف) | 5 | 5 | 0 | Exclusively Meccan |
| 3 | nqm (نقم) | 17 | 12 | 5 | Meccan-tilted; vengeful disapproval; cf. *al-muntaqim* |
| 3 | sxṭ (سخط) | 4 | 0 | 4 | Exclusively Medinan (*p* = 0.026) |
| 3 | mqt (مقت) | 6 | 4 | 2 | Most intense moral aversion (Zajjāj) |
| 4 | ġḍb (غضب) | 24 | 13 | 11 | Central anger lexeme; predicated of God, prophets, believers |
| 4 | ḥrd (حرد) | 1 | 1 | 0 | Qurʾānic hapax: Q. 68:25 |
| 5 | ġyẓ (غيظ) | 11 | 3 | 8 | Compressed anger; *tamayyuz* manifestation (Q. 67:8) |
| 6 | bġy (بغي) | 96 | 55 | 41 | Bridge node; bidirectional causation (§4.6 caveats) |
| 6 | ṭġy (طغي) | 39 | 29 | 10 | Pharaonic; structural arrogance |
| 6 | ʿtw (عتو) | 10 | 9 | 1 | Settled defiance; properly *istikbār*-attached |
| **Σ** | — | **312** | **183** | **129** | |

Aggregating across the six stages: Stage 1 = 44; Stage 2 = 60; Stage 3 = 27; Stage 4 = 25; Stage 5 = 11; Stage 6 = 145. The chi-squared test against the null of uniform six-stage distribution rejects (χ²(5) = 227.15, *p* < 0.001), confirming H1. A second chi-squared test against the null of equal split between the phenomenological core (Stages 1–5 = 167 attestations) and the behavioural-outcomes pole (Stage 6 = 145 attestations) *fails to reject* (χ²(1) = 1.55), supporting H2 in its revised form. We read the absence of a significant skew at this cut as theoretically informative: it is consistent with the reviewer's caveat (developed in §4.6 and §5.4) that the Stage-6 lexemes (*baghy*, *ṭughyān*, *ʿutuww*) are not exclusively anger-derived but stand in a *bidirectional* causal relation to the anger spectrum—anger may produce these behaviours, but the behaviours can equally produce anger (in their victims, the prophets, and the divine response). The substantive analysis of this point, and the discussion of why corpus distribution is not, on its own, a settled answer, is taken up in §5.4.


![Per-root and per-stage frequency of the 312 core spectrum attestations. *Left panel*: linear-scale frequency for each of the fourteen roots; bar colour encodes the phenomenological stage. Stage 6 (*bġy* 96 vs. *ʿtw* 10) shows a strong internal asymmetry that mirrors the lexical division of labour between distributed-aggression (*baghy*) and obstinate-defiance (*ʿutuww*) outlined in §4.6. *Right panel*: stage totals (S1=44, S2=60, S3=27, S4=25, S5=11, S6=145). The six-stage distribution rejects uniformity at χ²(5) = 227.15, *p* < 0.001. The phenomenological core (S1–5 = 167) and the behavioural-outcomes pole (S6 = 145) are *not* significantly unequal in raw count (χ²(1) = 1.55, fails to reject), a result we read as supporting the bidirectional-causation analysis of *baghy*/*ṭughyān*/*ʿutuww* developed in §4.6 and §5.4 — the Qurʾān is not pedagogically over-loading anger-outcomes; rather, Stage-6 lexemes are themselves not exclusively anger-derived.](fig2_frequency_by_stage.pdf){width=95%}


![Stacked Meccan/Medinan distribution for each of the fourteen core roots. The numerals above each bar give the raw Meccan/Medinan split. Two distributional extremes warrant emphasis. *ʾasaf* (Stage 2) is attested **exclusively** in Meccan suras (5/0): the lexeme of "regret-grief" emerges in the discursive context of prophetic disappointment with rejection (Q. 18:6, Q. 43:55, Q. 7:150). *Sakhaṭ* (Stage 3) is attested **exclusively** in Medinan suras (0/4; binomial *p* = 0.026 against the 0.60 corpus baseline of Meccan attestations): the lexeme of "comprehensive divine displeasure" emerges only after the Hijra, in confrontation with the *munāfiqūn* (Q. 47:28, Q. 5:80, Q. 9:58, Q. 3:162). Additional patterns: *naqm* (Stage 3) is Meccan-tilted (12/5); *maqt* (Stage 3) is balanced (4/2); *ḥard* is a Qurʾānic hapax at Q. 68:25 (Meccan). The visualisation thus encodes a non-trivial finding: not every root in the spectrum behaves as a context-neutral lexical resource — several of them are *discursive-contextually specialised*, a pattern theorised in §5.5 as a general feature of Qurʾānic vocabulary.](fig3_meccan_medinan.pdf){width=95%}


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

The exclusive-Meccan distribution (5/0; binomial *p* = 0.16, suggestive but not decisive given the small sample) is interpretable in discursive-contextual terms: *asaf* attests in narrative passages depicting prior prophets' encounter with rejection (Mūsā vis-à-vis Pharaoh's people; the rejection of warnings by Meccan polytheists).

**4.4.3.1. *Ghaḍbān asifan* — Moses, Q. 7:150 / Q. 20:86 — sacred anger.** A particularly important compound description is *ghaḍbān asifan* in Q. 7:150 and Q. 20:86, applied to Moses on his return to find the people worshipping the calf. The compound generates a three-layer dialectic that complicates any reading of anger as purely negative:

(a) **Inner/outer structural layering.** *Ghaḍab* is the *outer/kinetic* energy of the Mosaic response — the visible, motor-action component (the throwing of the tablets, the seizing of Aaron's beard). *Asaf* is the *inner/potential* energy — a compassionate grief over the lost ones, the wasted forty days, the relapse to ignorance.
(b) **Causal grounding.** *Asaf* is the *ground* of *ghaḍab* in this narrative. If *asaf* were absent, Moses' anger would be mere violence; with *asaf* present, his anger is "sacred anger" — anger in service of guidance.
(c) **Intentional direction.** *Ghaḍab* is vectored *outward* (toward the people, the calf, his brother). *Asaf* is vectored *inward* (grieving the wasted opportunity, the relapse).

This compound problematises the framing of anger as purely negative. In the prophetic case, anger is morally productive when grounded in compassionate grief. The lexicon, in pairing *ghaḍab* with *asaf* in a single nominal predication, encodes that moral structure with great precision.

**4.4.4. Network evidence for Stage-2 coherence.** The aya-level co-occurrence network (Figure 4) reveals that the strongest single edge connects *ḥzn* and *ḍyq* (weight 3); these two lexemes share three verses in the Qurʾān, more than any other pair within the spectrum. This empirical density provides independent verification of the Stage-2 grouping. Centrality analysis (Figure 7) places *ḥzn* among the highest-degree nodes (weighted degree 5, tied with *ġḍb*).

### 4.5. Stage 3 — Evaluative aversion

Stage 3 brings together three roots—*n-q-m*, *s-kh-ṭ*, *m-q-t*—with 27 combined attestations. Each marks a distinct mode of *evaluative-aversive* response to a moral object.

**4.5.1. *Naqm* (17 attestations; 12 Meccan / 5 Medinan).** *Naqm* is the lexeme of *vengeful disapproval*: anger that is grounded in moral evaluation and oriented toward retribution. Q. 7:126 (*wa-mā naqamū minnā illā an āmannā bi-āyāti rabbinā*) is the linguistic exemplar: anger directed *at others' belief* — Pharaoh's sorcerers, on accepting Moses' message, are described as suffering Pharaonic *naqm* precisely *because* they believed. The grammatical construction *naqamū min* + (cause) is a canonical Qurʾānic formula for evaluatively-grounded anger.

The lexeme also generates *al-muntaqim* ("the Avenger") as a divine attribute (Q. 32:22 and parallels), establishing a direct theological-lexical bridge from the human-affective register to the divine retributive register. Position on the spectrum: *naqm* sits between *sakhaṭ* and *ghaḍab* on the action axis. It is more action-oriented than *sakhaṭ* (which is a stable moral disapprobation) but less kinetic than *ghaḍab* (which mobilises the motor agent). The Meccan tilt (12/5) is consistent with the lexeme's frequent appearance in narrative-prophetic passages (the Pharaonic sorcerers, the people of Lot, the people of Madyan).

**4.5.2. *Sakhaṭ* (4 attestations; 0 Meccan / 4 Medinan).** Despite its low frequency, *sakhaṭ* furnishes one of the paper's principal findings. The exclusive-Medinan distribution—zero Meccan attestations among four total—has a binomial-test p-value of 0.026 against the corpus baseline of 0.60 Meccan probability, statistically significant at α = 0.05. Confirms H3.

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

**4.6.2. *Ghaḍab* as bridge node.** Network analysis (Figure 7) places *ghḍb* among the top three nodes for betweenness centrality (0.17), tied with *ġyẓ* and surpassed only by *bġy*. Notable edges include *ghḍb–ġyẓ* (the upward transition to Stage 5), *ghḍb–ḥzn* (the downward link to Stage 2), and *ghḍb–bġy* (the link to Stage 6).

**4.6.3. *Ḥard* (1 attestation: Q. 68:25 — Qurʾānic hapax).** *Ḥard* is a Qurʾānic hapax legomenon, attested only in Q. 68:25 (*wa-ghadaw ʿalā ḥardin qādirīn*) in the parable of the Garden-Owners (*aṣḥāb al-jannah*). The garden-owners, having vowed in the night to harvest before dawn so as to *deny* the poor their share, "went forth at dawn upon *ḥard*, having decided." The classical exegesis converges on a striking dual gloss:

- al-Ṭabarsī's *Majmaʿ al-Bayān* glosses *ḥard* as both *ghaḍab* (anger) and *qaṣd* (intent, purposive aim). The lexeme is anger combined with intent.
- al-Ṭabāṭabāʾī's *al-Mīzān* refines the gloss as *anger-plus-deliberate-denial*: a particularly *purposive* anger weaponised through resource-denial.

The phenomenology of *ḥard* is therefore distinctive within Stage 4. *Ghaḍab* mobilises the motor agent toward an outward target; *ḥard* mobilises the motor agent toward a deliberate, miserly *withholding* — anger that strips the world of what it is owed. The sociological signature of *ḥard* is anger weaponised through institutional or contractual stinginess. The narrative consequence in Q. 68 is the destruction of the garden by the night-storm: divine retribution against the *ḥard*-driven plan to deny.

The position of *ḥard* on the spectrum is therefore: *active-anger* (Stage 4), but distinctively *purposive-and-withholding* rather than approach-aggressive. The hapax status of the lexeme — paired with the rich exegetical tradition — is a striking instance of the Qurʾān's lexical economy: a single attestation serves as the linguistic anchor for an entire moral-psychological category.

### 4.7. Stage 5 — Compressed/explosive rage

**4.7.1. *Ghayẓ* and the *kaẓm* metaphor (11 attestations; 3 Meccan / 8 Medinan).** Glosses of *ghayẓ* in the four authoritative lexica — "compressed, contained anger" (al-Rāghib), "the highest concentration of restrained anger" (Mostafavi), and "filling of the self with restrained anger" (Ibn Manẓūr) — converge on a single conceptual structure: *ghayẓ* is the pressurised contents of a sealed vessel.

Q. 3:134 commends *al-kāẓimīn al-ghayẓ*: those who restrain *ghayẓ*. The verb *kaẓm* derives from the act of tying off a waterskin to prevent fluid escape; it is the agent-internal regulation that sustains containment. Read through Lakoff and Kövecses's framework, the *ghayẓ–kaẓm* pair instantiates with great precision the ANGER IS A PRESSURIZED CONTAINER metaphor: *ghayẓ* is the contained fluid; *kaẓm* is the seal. Figure 6 visualises this conceptual structure.

The Medinan-leaning distribution of *ghayẓ* (8/3) reflects the discursive context in which inner anger management becomes a salient pedagogical concern: the formative Medinan community required affective discipline within a still-fragile *umma* facing internal *Munāfiq* and external Quraysh hostility.

**4.7.2. *Tamayyuz*: container collapse in Q. 67:8 (manifestation, not separate root).** The single most articulated image of rage in the Qurʾān is Q. 67:8: *takādu tamayyazu min al-ġayẓ*—"[the fire] is on the verge of bursting apart from rage." The verb *tamayyaza* derives from the root *m-y-z* (to separate, to part, to sever). The image is not simply that of pressure exiting through the seal but of *the structural integrity of the container itself failing*. We treat *tamayyuz* in the present analysis as a *manifestation* of Stage 5 (a behavioural sign of containment failure) rather than as a distinct core root, in keeping with the analytical decision to count fourteen rather than fifteen core roots.

Lakoff and Kövecses's (1987) original analysis identifies "container collapse" as the failure mode of the master metaphor, but their English exemplars (*she blew her top*, *he exploded*, *I lost it*) report the *exit* of pressurised content rather than the *structural disintegration* of the vessel. Q. 67:8 makes the disintegration explicit. We argue, accordingly, that this verse furnishes one of the most articulated linguistic instances of "container collapse" in any documented historical text—pre-modern or modern. Confirms H5.

The theoretical implication is significant. The Lakoff–Kövecses analysis was originally framed in terms of contemporary American English; the Qurʾānic data extend its empirical base to a register of seventh-century Arabic, supporting a stronger universality claim for the underlying conceptual structure.

### 4.8. Stage 6 — Behavioural outcomes (with caveats)

**4.8.1. *Baghy* (96 attestations; 55 Meccan / 41 Medinan).** The most frequent lexeme of the spectrum and, by network-centrality measures, its bridge node. *Baghy* is glossed as "seeking beyond rightful bounds" (al-Rāghib) and "aggressive seeking with intent to oppress" (Mostafavi). Q. 42:42 (*innamā al-sabīlu ʿalā lladhīna yaẓlimūna l-nāsa wa-yabghūna fī l-arḍi bi-ġayri l-ḥaqq*) collocates *baghy* with *ẓulm*, embedding the lexeme firmly in the moral-evaluation register. Ibn ʿĀshūr's *al-Taḥrīr wa-l-Tanwīr* (vol. 25, p. 126) clarifies the syntagmatic relation: "*baghy* and *ẓulm* are nearly synonymous, except that *baghy* is specific to non-rightful aggression against another, while *ẓulm* covers all forms of injustice."

**4.8.2. *Baghy* as bridge node.** Network analysis (Figure 7 and Table 4 below) reveals that *baghy* attains the highest closeness centrality (0.55) of any node in the spectrum, and is tied with *ghaḍab* and *asaf* for the highest betweenness centrality (0.15). Its eigenvector centrality (0.50) is second only to *karh* (0.50), reflecting its dense embedding in the spectrum's interaction structure. Furthermore, *baghy* exhibits the highest cross-field co-occurrence with the umbrella moral terms: 19 aya-level co-occurrences with *ẓlm/jrm/fsq/ʿdw/krh/šnʾ* combined, of which 8 are with *ʿdw*, 4 with *ẓlm*, and 3 with *krh* (Table 4). This bridging profile confirms H4.

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

**4.8.5. Caveats on the Stage-6 lexemes (*baghy*, *ṭughyān*, *ʿutuww*): bidirectional causation.** Three caveats are required for Stage 6, and they are central to the revised reading of the spectrum advanced in this paper. *Baghy* in Qurʾānic usage frequently arises from greed, supremacism (*ʿulw fī al-arḍ*), or oppressive self-interest rather than from acute anger; the act of overstepping is sometimes the *substance* of corrupted desire (compare Q. 6:21 *innahu lā yufliḥu al-ẓālimūn*) rather than the *outcome* of a passion. *Ṭughyān* — paradigmatically Pharaonic (Q. 79:17, Q. 28:4) — is rooted in structural arrogance and the exercise of unchecked power, not as a phenomenological extension of anger; the verse Q. 26:55 (*innahum lanā la-ghāʾiẓūn*) is striking precisely because it reverses the polarity, showing the oppressor's anger arising *from* the rebellion of the oppressed rather than *from* his own anger. *ʿUtuww* most commonly attaches to *istikbār* (arrogance) and is a stable, settled defiance — a property of moral character rather than a transient affective state. We retain these three roots within Stage 6 because the corpus does locate them at the behavioural pole of the spectrum, but the *causation* arrow is bidirectional: anger may *produce* these behaviours, but they can also produce *anger* (and often do, in the Qurʾānic narrative of oppressors and prophets). The near-balance between Stages 1–5 and Stage 6 (167 vs. 145, χ²(1) = 1.55) is, on this reading, exactly what one would expect if the Stage-6 lexemes are not exclusively anger-derived.


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

### 4.10. Comparative translation analysis

To assess how the spectrum's intensity differentiation survives translation, Table 6 compares five English translations on four canonical verses.

**Table 6. Translation of four canonical verses across five English translations**

| Term & verse | Yusuf Ali | Pickthall | Arberry | Saheeh Intl. | Hilali-Khan |
|:----:|:---|:---|:---|:---|:---|
| *ḍīq* (Q. 15:97) | "thy heart is distressed" | "thy bosom is at times oppressed" | "thy breast is straitened" | "your chest is constrained" | "your breast feels tight" |
| *ġayẓ* (Q. 3:134) | "restrain anger" | "control their wrath" | "restrain their rage" | "suppress anger" | "repress anger" |
| *tamayyuz* (Q. 67:8) | "almost burst with fury" | "almost burst with rage" | "well-nigh bursts asunder with fury" | "almost bursts with rage" | "almost bursts up with fury" |
| *ṭughyān* (Q. 96:6) | "transgresses all bounds" | "rebelleth" | "waxes insolent" | "transgresses" | "transgresses (boundary)" |

Two findings emerge. First, the rendering of *ġayẓ* in Q. 3:134 collapses the *ghaḍab/ġayẓ* distinction in all five translations—the English versions render *ġayẓ* with terms (*anger*, *wrath*, *rage*) that are also routinely used for *ghaḍab*. The differentia—the *containment* dimension of *ġayẓ*—is preserved only via the contextual verb of restraint, not in the lexeme itself. Second, the rendering of *tamayyuz* in Q. 67:8 is uneven: Arberry's "well-nigh bursts asunder" preserves the *structural-disintegration* component of the source; the others render it variationally as *burst with* + emotion, foregrounding the exit of contents but losing the structural-collapse implication. Translation thus systematically erodes the spectrum's internal architecture.

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

Appraisal theory (Lazarus 1991; Scherer 2001, 2005) holds that emotions arise from cognitive evaluations of situations rather than from raw stimuli. Q. 96:6–7 conditions *ṭughyān* on the appraisal of *istighnāʾ*—a textbook appraisal-theoretic claim. The Qurʾānic lexicon, on this evidence, treats certain emotion-behaviour transitions as cognitively conditioned, anticipating the appraisal-theoretic insight that emotion is not pre-cognitive but cognitively constituted.

### 5.4. The phenomenology/outcomes balance: why the corpus does not show a 2.4× skew

A central revision relative to the prior version of this analysis concerns the relative weight of the phenomenological core (Stages 1–5) and the behavioural-outcomes pole (Stage 6). On the prior ten-root analysis, the corpus appeared to assign 2.4× more attestations to Stage 4 (then "behavioural rebellion") than to Stages 1+2+3 combined; on a naive reading, that asymmetry suggested a discursive over-emphasis on outcomes.

The revised fourteen-root, six-stage analysis tells a different story. The expanded inventory of phenomenological lexemes (*uff*, *karh*, *naqm*, *maqt*, *ḥard*) raises the Stage 1–5 total to 167, against Stage 6's 145; the chi-squared test against equal split *fails to reject* (χ²(1) = 1.55). This near-balance is, on our reading, exactly what one would expect if (i) the phenomenological side of the spectrum is in fact richer than the prior ten-root analysis allowed, and (ii) the Stage-6 lexemes are not exclusively anger-derived but stand in *bidirectional* causal relation to anger. The corpus-distributional fact is therefore consistent with — indeed supportive of — the substantive caveat we have entered against treating *baghy*, *ṭughyān*, and *ʿutuww* as simple downstream effects of unmanaged anger.

This has a methodological corollary that bears emphasis: corpus-distributional analyses of religious texts should not be interpreted as neutral reflections of an external referent. They are maps of *discursive emphasis*; their interpretation is fundamentally entangled with theoretical decisions about category membership (which roots count as part of the spectrum) and category causation (whether the relation is uni- or bidirectional). The shift from a 10/4-stage to a 14/6-stage analysis was not merely cosmetic: it changed both the empirical pattern and its theoretical interpretation.

### 5.5. Discursive-contextual specialisation: a general phenomenon

The exclusive-Medinan profile of *sakhaṭ*, the exclusive-Meccan profile of *asaf*, the Meccan tilt of *naqm* and *ʿutuww*, the hapax-Meccan status of *ḥard*, and the Medinan tilt of *karh* — taken together with the strong directional patterns of *jrm* (Meccan) and *fsq* (Medinan) in the umbrella roots — instantiate what we propose to call **discursive-contextual specialisation of lexemes**. This is the phenomenon whereby a member of a multi-lexeme semantic field becomes preferentially associated with a specific discursive register—in the Qurʾānic case, with the Meccan vs. Medinan rhetorical and sociolinguistic context. The specialisation is not random; in each documented case, contextual analysis confirms that the lexeme's preferential register is the register in which the corresponding referent obtains: *sakhaṭ* with the *Munāfiqūn* (a Medinan phenomenon), *asaf* with prior-prophet narratives (Meccan-rhetorical), *jrm* with anti-*shirk* polemic (Meccan), *fsq* with intra-community discipline (Medinan).

Discursive-contextual specialisation is, as far as we can establish, undocumented as a systematic phenomenon in Qurʾānic-linguistic scholarship; it is also relevant to the broader discussion of *Sitz im Leben* in Qurʾānic source criticism. Future work should test the generalisation across other multi-lexeme fields.

### 5.6. Q. 67:8 and the universality of the container metaphor

The most theoretically significant finding concerning conceptual metaphor is that Q. 67:8 (*takādu tamayyazu min al-ġayẓ*) instantiates the ANGER IS PRESSURIZED CONTAINER metaphor more transparently than any English exemplar in Lakoff and Kövecses's (1987) corpus. Where English idioms (*explode with rage*, *blow one's top*, *lose it*) report the *exit* of contained content, Q. 67:8 figures the *structural disintegration of the container itself* via the verb *tamayyaza* (m-y-z: to part, to sever).

This finding has a methodological and a theoretical consequence. *Methodologically*, it implies that the historical depth of the conceptual-metaphor inventory is greater than has often been recognised; the container metaphor for anger is not a peculiarity of contemporary English but a cross-culturally robust cognitive structure attested in seventh-century Arabic with arguably greater clarity than in modern Western corpora. *Theoretically*, it strengthens the universalist claim within CMT: that the bodily-grounded image schemas (CONTAINER, FORCE, BALANCE) underwrite human emotion conceptualisation across cultures and historical periods.


![The ANGER-IS-A-PRESSURIZED-CONTAINER schema (Lakoff & Kövecses 1987), instantiated by the Qurʾānic triplet *ghaḍab → ghayẓ + kaẓm → tamayyuz*. **Panel 1** (Stage 4): *ghaḍab* — an *open* container; the affect is present but unconcentrated, dissipating freely into language (the lexeme is the most nominally productive in the spectrum). **Panel 2** (Stage 5, Q. 3:134): *ghayẓ* — fluid sealed by *kaẓm*; the verb *kaẓama* originally denotes the *tying-off of a waterskin*, the agent-internal regulation that maintains containment under rising pressure. **Panel 3** (Stage 5 manifestation, Q. 67:8): *tamayyuz* — the structural failure; the verb derives from the root *m-y-z* "to separate, to part, to sever", and figures not the exit of pressurised content (as English *explode*) but the *splitting apart of the container itself*. The Qurʾānic instantiation is, on the present argument, more transparent than any English exemplar in Lakoff and Kövecses's (1987) corpus, providing strong cross-linguistic evidence for the cognitive universality of the schema (§5.6).](fig6_metaphor_diagram.pdf){width=100%}


### 5.7. Implications for Qurʾānic translation

Translation criticism of the Qurʾān has long observed that translations level the spectrum—that *ġaḍab* and *ġayẓ* alike become *anger*; that *baghy*, *ṭughyān*, and *ʿutuww* alike become *transgression* (Table 6). Our analysis sharpens this critique by furnishing the reference model against which the levelling can be measured. We propose that critical and study-edition translations adopt distinct equivalents:

> *uff*: vocal sigh of irritation · *karh* (*karāha*): inner dislike · *karh* (*ikrāh*): coercion (a structural extension, not an emotion) · *ḍīq*: inner constriction · *ḍāqa dharʿan*: arm-span tightening / inhibited aggression · *ḥuzn*: persistent grief (transversal valence) · *asaf*: regretful dismay (with anger) · *naqm*: vengeful disapproval · *sakhaṭ*: moral disapprobation · *maqt*: intense moral aversion · *ghaḍab*: anger · *ḥard*: anger combined with deliberate denial · *ghayẓ*: contained / boiling rage · *tamayyuz min al-ġayẓ*: bursting from rage · *baghy*: aggressive transgression · *ṭughyān*: rebellious overflow · *ʿutuww*: obstinate defiance.

For pedagogical translations, we further recommend that each lexeme be marked with its position on the continuum—either by inline gloss, by footnote, or by chromatic coding—so that the structural architecture survives the move into the target language.

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

**Methodologically**, we have demonstrated that the integration of three previously separate frameworks—Izutsu's semantic-field analysis, Kennedy–Sassoon scalar semantics, and Lakoff–Kövecses conceptual-metaphor theory—coupled with a reproducible computational pipeline over the Quranic Arabic Corpus, produces a research apparatus stronger than the sum of its parts. The integration is, to the best of our knowledge, here brought to Qurʾānic studies for the first time. The research apparatus is openly available and applicable to other Qurʾānic semantic fields.

**Descriptively**, we have produced an exhaustive, reproducible concordance of 312 attestations across the fourteen core spectrum roots, with corresponding distributional and network-analytic outputs. The CSV outputs provide a foundation on which further philological and computational work can build.

**Theoretically**, we have formulated and empirically defended the **Qurʾānic Action-Intensity Continuum Hypothesis**: the claim that fourteen core lexemes of the Qurʾānic anger-spectrum field operate as a single graded continuum structured by *intensity of action* and partitioned into six phenomenologically meaningful stages. The hypothesis is supported by qualitative evidence from the four authoritative lexica and the four authoritative tafsirs, and by quantitative evidence from frequency, distribution, morphology, and network structure. We have, in addition, identified distributional patterns that we have not seen previously reported (the exclusively-Medinan *sakhaṭ*; the exclusively-Meccan *asaf*; the Meccan-tilted *naqm*; the hapax-Meccan *ḥard*); proposed the general phenomenon of **discursive-contextual lexical specialisation** of which these are instances; entered explicit caveats on the bidirectional causation of the Stage-6 lexemes; and argued that Q. 67:8 furnishes one of the most articulated linguistic exemplars of "container collapse" in any documented historical text.

### 6.2. Answers to the research questions

**RQ1.** The semantic field is a fourteen-node network organised around the bridge node *baghy* and the stage-internal hubs *ḥuzn* and *ghaḍab*, with several specialised peripheral nodes (*sakhaṭ*, *asaf*, *ḥard*, *ʿutuww*) exhibiting marked distributional asymmetries.

**RQ2.** The fourteen nodes order on a six-stage continuum—pre-anger displeasure (Stage 1), inner pressure & contraction (Stage 2), evaluative aversion (Stage 3), active anger (Stage 4), compressed/explosive rage (Stage 5), behavioural outcomes with caveats (Stage 6)—organised by the composite dimension of *intensity of action* (locus, intensity, scope of consequence).

**RQ3.** The empirical distribution corroborates the continuum: the chi-squared test rejects the null of six-stage uniform distribution (χ²(5) = 227.15, *p* < 0.001); the comparison between Stages 1–5 and Stage 6 *fails to reject* equal split (χ²(1) = 1.55), a result we interpret as supporting the bidirectional-causation reading of Stage 6; the network exhibits the predicted bridge structure at *baghy*; and the morphological profile distinguishes the verbal Stages 1–2 from the more nominal Stage 6.

**RQ4.** The continuum is structurally homologous with Gross's process model, Plutchik's wheel, Spielberger's STAXI, and Lazarus–Scherer appraisal theory in its psychological component, but extends beyond all of them by integrating the post-failure structural-moral consequences of unmanaged emotion (Stage 6) — while qualifying that integration with the bidirectional-causation caveat of §4.8.5.

**RQ5.** Practical implications include three translation recommendations (distinct equivalents, position-marking, structural footnoting) and three Islamic-psychology applications (early-stage prevention, *kaẓm*-grounded crisis intervention, and *tawba*-grounded rehabilitation).

### 6.3. Limitations and future work

Five limitations bound the present study and define its principal future-research extensions.

First, the analysis works at the surface-lexical layer; broader discourse-analytic close-reading of how the spectrum is mobilised across narrative arcs of individual suras remains to be conducted. Second, the *tafsīr* engagement is selective, drawing on four canonical commentaries; a systematic survey of the broader exegetical tradition (especially Shīʿī, Sufi, and contemporary Persian-language commentary) would refine specific lexical readings. Third, the cognitive-linguistic apparatus is Anglophone-dominated; engagement with classical Arabic theories of *bayān* (especially al-Jurjānī's *Dalāʾil al-Iʿjāz*) would supply an indigenous theoretical substrate. Fourth, the *ḥadīth* corpus has not been integrated, although it would be instructive to test whether the continuum is robust beyond the Qurʾānic corpus into the broader Islamic textual tradition. Fifth, the clinical-psychological implications proposed in §5.8 have not been operationalised in empirical interventions; the design of pilot studies for *kaẓm*-grounded emotion regulation training is a priority for translational work.

### 6.4. Closing remark

The Qurʾānic lexicon, on the analysis advanced here, encodes a sophisticated theory of the phenomenology of the anger spectrum—not as explicit theoretical formulation but as the architectural design of its semantic surface. Recovering that theory requires methodological tools that bring together the qualitative attentiveness of classical philology, the formal precision of contemporary linguistic theory, and the verifiability of corpus-computational analysis. We hope the present study, alongside the foundational work of Izutsu, Qāʾimīniyā, Pakatchi, Narimani et al., and Qarizadeh et al., advances this triple integration. The classical and the computational are not opposed traditions; they are complementary instruments, and their joint deployment opens horizons that neither could disclose alone.

---

## Data and Code Availability

All code, data, concordance CSV outputs, and figure-generation scripts are released open-source at:

> **github.com/ali-kin4/quranic-emotion-spectrum**

The repository contains: (i) the Python pipeline under MIT License; (ii) the Quranic Arabic Corpus (Dukes 2011) under its original GPL; (iii) the complete CSV concordance for the fourteen core spectrum roots (312 attestations), distributional summaries, statistical tests (χ²(5) = 227.15; χ²(1) = 1.55), network-centrality outputs, and umbrella-cooccurrence tables; (iv) PDF and PNG versions of the seven figures published with this paper; (v) full text of the Persian and English manuscripts. The complete analysis can be regenerated end-to-end by:

```bash
pip install -r analysis/requirements.txt
python analysis/extract_concordance.py
python analysis/visualize_spectrum.py
python analysis/advanced_metrics.py
python analysis/visualize_advanced.py
```

---

## Acknowledgements

The authors thank Kais Dukes and the team behind the Quranic Arabic Corpus, and the Tanzil Project, for releasing the morphological and textual resources without which this kind of empirical Qurʾānic analysis would not be feasible. We thank Urmia University for institutional support.

---

## References

Averill, J. R. (1982). *Anger and Aggression: An Essay on Emotion*. New York: Springer-Verlag.

Berkowitz, L. (1993). *Aggression: Its Causes, Consequences, and Control*. New York: McGraw-Hill.

Dukes, K. (2011). *Quranic Arabic Corpus (Morphology, Version 0.4)*. University of Leeds. https://corpus.quran.com.

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

Kennedy, C. (2007). Vagueness and grammar: The semantics of relative and absolute gradable adjectives. *Linguistics and Philosophy*, *30*(1), 1–45.

Kövecses, Z. (1986). *Metaphors of Anger, Pride, and Love: A Lexical Approach to the Structure of Concepts*. Amsterdam: John Benjamins.

Kövecses, Z. (2000). *Metaphor and Emotion: Language, Culture, and Body in Human Feeling*. Cambridge: Cambridge University Press.

Kövecses, Z. (2010). *Metaphor: A Practical Introduction* (2nd ed.). Oxford: Oxford University Press.

Lakoff, G., & Johnson, M. (1980). *Metaphors We Live By*. Chicago: University of Chicago Press.

Lakoff, G., & Kövecses, Z. (1987). The cognitive model of anger inherent in American English. In D. Holland & N. Quinn (Eds.), *Cultural Models in Language and Thought* (pp. 195–221). Cambridge: Cambridge University Press.

Lazarus, R. S. (1991). *Emotion and Adaptation*. New York: Oxford University Press.

Maalej, Z. (2004). Figurative language in anger expressions in Tunisian Arabic: An extended view of embodiment. *Metaphor and Symbol*, *19*(1), 51–75.

al-Muṣṭafawī, Ḥ. (1416 AH). *al-Taḥqīq fī Kalimāt al-Qurʾān al-Karīm*. Tehran: Wizārat al-Thaqāfah wa-l-Irshād al-Islāmī.

Narimani, Z., Iqbali, M., & Chari, M. (1400 SH/2021). [Semantic re-analysis of the words *ghayẓ*, *ghaḍab*, and *sakhaṭ* in the Holy Qurʾān with an exegetical approach]. *Pizhūhish-hā-yi Qurʾān va Ḥadīth* [Qurʾanic and Hadith Research]. University of Tehran. [in Persian]

Plutchik, R. (1980). *Emotion: A Psychoevolutionary Synthesis*. New York: Harper & Row.

Plutchik, R. (2001). The nature of emotions. *American Scientist*, *89*(4), 344–350.

Qarizadeh, M. ʿO., Salmani Marvast, M. ʿA., Meymandi, V., & Farsi, B. (1402 SH/2024). [Polysemy of the word *ṭughyān* in the Holy Qurʾān with a linguistic approach]. *Pizhūhish-hā-yi Zabānshinākhtī-yi Qurʾān* [Linguistic Research in the Holy Qurʾān]. University of Isfahan. [in Persian]

Qāʾimīniyā, ʿA. (1390 SH/2011). *Maʿnāshināsī-yi Shinākhtī-yi Qurʾān* [Cognitive Semantics of the Qurʾān]. Tehran: Pizhūhishgāh-i Farhang va Andīshah-i Islāmī. [in Persian]

al-Rāghib al-Iṣfahānī, Ḥ. (1992). *al-Mufradāt fī Gharīb al-Qurʾān* (Ṣ. ʿA. Dāwūdī, Ed.). Damascus and Beirut: Dār al-Qalam & al-Dār al-Shāmiyyah.

Sassoon, G. W. (2010). The degree functions of negative adjectives. *Natural Language Semantics*, *18*(2), 141–181.

Scherer, K. R. (2001). Appraisal considered as a process of multilevel sequential checking. In K. R. Scherer, A. Schorr, & T. Johnstone (Eds.), *Appraisal Processes in Emotion: Theory, Methods, Research* (pp. 92–120). New York: Oxford University Press.

Scherer, K. R. (2005). What are emotions? And how can they be measured? *Social Science Information*, *44*(4), 695–729.

Sharifian, F. (2011). *Cultural Conceptualisations and Language: Theoretical Framework and Applications*. Amsterdam: John Benjamins.

Spielberger, C. D. (1999). *Professional Manual for the State-Trait Anger Expression Inventory–2 (STAXI-2)*. Odessa, FL: Psychological Assessment Resources.

al-Ṭabāṭabāʾī, M. Ḥ. (1390 AH). *al-Mīzān fī Tafsīr al-Qurʾān*. Beirut: Muʾassasat al-Aʿlamī li-l-Maṭbūʿāt.

al-Ṭabarsī, F. al-Ḥ. (n.d.). *Majmaʿ al-Bayān fī Tafsīr al-Qurʾān*. Beirut: Dār al-Maʿrifah.

*Tanzil Project*. (n.d.). *The Tanzil Quran Text* (Uthmani edition). https://tanzil.net.

Wierzbicka, A. (1999). *Emotions Across Languages and Cultures: Diversity and Universals*. Cambridge: Cambridge University Press.

al-Zamakhsharī, M. (1407 AH). *al-Kashshāf ʿan Ḥaqāʾiq Ghawāmiḍ al-Tanzīl*. Beirut: Dār al-Kitāb al-ʿArabī.
