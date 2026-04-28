# The Phenomenology of Negative Emotions in the Qurʾān
## A Semantic-Network Analysis of Distress, Aggression, and Rebellion Along an Action-Intensity Continuum

**Karim Jabbary** *(corresponding author)*
Department of Arabic Language and Literature, Faculty of Literature and Humanities, Urmia University, Urmia, Iran

**Ali Jabbary**
Urmia University, Urmia, Iran

---

## Abstract

The Qurʾān deploys an exceptionally articulated lexicon for the description of negative human emotion, yet existing scholarship has tended to treat this lexicon either word-by-word or through normative-ethical frames, leaving the structural-relational dimension of the field largely unexplored. This study advances the thesis that ten core Arabic roots—**ḍyq, ḥzn, ʾsf, sxṭ, ġḍb, ġyẓ, myz, bġy, ṭġy, ʿtw**—form a single graded semantic field organised along the dimension of *intensity of action*, traversing four phenomenological stages: (1) internal distress, (2) explicit anger, (3) explosive rage, and (4) behavioural rebellion. We integrate three methodological lenses—Toshihiko Izutsu's semantic-field approach, scalar semantics in the Kennedy-Sassoon tradition, and conceptual metaphor theory after Lakoff and Kövecses—and validate the proposed continuum against the **Quranic Arabic Corpus** (Dukes 2011) using a fully reproducible Python pipeline. The empirical analysis covers 833 attestations across sixteen roots (248 across the ten core spectrum roots), spanning the entire 6,236-verse corpus. Three principal findings emerge. First, the four-stage distribution of attestations deviates highly significantly from uniformity (χ²(3) = 165.45, *p* < 0.001), with Stage 4 (behavioural rebellion) over-represented by a factor of approximately 2.4 relative to the combined first three stages (χ²(1) = 7.11, *p* = 0.008). Second, two distributional patterns emerge that have, to our knowledge, not been previously reported: *sakhaṭ* attests **exclusively** in Medinan suras (0/4; binomial *p* = 0.026 against the corpus baseline of 0.60 Meccan), while *asaf* attests **exclusively** in Meccan suras (5/0). Third, network-centrality analysis of the aya-level co-occurrence graph reveals that *baghy* operates as the bridging node (betweenness = 0.39) between the emotional field and the broader moral-evaluation field of the Qurʾān (315 attestations of *ẓulm*, 66 of *jurm*, 54 of *fisq*, 106 of *ʿadāwah*). The Qurʾānic continuum is structurally homologous with Gross's process model of emotion regulation (1998, 2014), Plutchik's wheel of intensity (1980), and Spielberger's State-Trait Anger framework (1999), but extends beyond these in a critical respect: by integrating Stage 4, it presents not only a *psychology* of emotion but a *moral anthropology* of the structural consequences of unmanaged emotion. We argue that the Qurʾānic verse Q. 67:8 (*takādu tamayyazu min al-ġayẓ*) constitutes one of the most articulated linguistic instances of "container collapse" (Lakoff & Kövecses 1987) in any documented historical text, providing strong cross-cultural evidence for the cognitive universality of the ANGER IS PRESSURIZED CONTAINER metaphor. The findings have implications for Qurʾānic translation (where the levelling of distinct lexemes erodes the spectrum's moral-psychological architecture), for the design of culturally-grounded Islamic-psychology interventions, and for the cross-linguistic study of emotion lexicons.

**Keywords:** Qurʾān, semantic field, cognitive linguistics, scalar semantics, conceptual metaphor, anger lexicon, emotion regulation, Arabic corpus linguistics, Izutsu, Islamic psychology.

---

## 1. Introduction

### 1.1. Statement of the problem

The Qurʾānic lexicon for negative human emotion exhibits a precision that survives, only with difficulty, the attempts of translation to render it into modern languages. Where English versions level *ḍīq*, *ḥuzn*, *asaf*, *sakhaṭ*, *ghaḍab*, *ghayẓ*, *baghy*, *ṭughyān*, and *ʿutuww* into a small set of broad equivalents—chiefly "distress," "grief," "anger," "rage," "transgression," and "rebellion"—the Arabic original distinguishes them with the precision of an emotional taxonomy. The hypothesis advanced in this paper is structural: that ten of the Qurʾān's most thematically central emotion-roots are not synonyms or scattered semantic singletons but coordinated nodes in a single *graded* semantic field, organised along the dimension of *intensity of action* (*shiddat al-kunish* in the Persian formulation of the original idea). The field opens in pre-anger inner pressure, passes through explicit anger and explosive rage, and culminates in behavioural rebellion. We treat the ten roots as discrete attestation points on this continuum and validate the proposed ordering through systematic corpus-based analysis.

This claim, if it holds, has consequences far beyond philology. It implies that the Qurʾān encodes—through the architecture of its lexicon, not through any explicit theoretical statement—a sophisticated implicit theory of the genealogy of moral failure: a theory according to which the social-structural pathologies the text most frequently denounces (transgression, tyranny, defiance) are continuous with, and developmentally downstream from, inner experiences of constriction and grief. The distance between *ḍīq al-ṣadr* in Q. 15:97 and *ʿutuww* in Q. 25:21 is not categorical but graded; it is the distance walked, in the absence of intervention, by an unmanaged emotional life.

### 1.2. Aims and originality

This paper has three aims. The first is **methodological**: to demonstrate that combining Izutsu's qualitative semantic-field approach, scalar-semantic ordering in the Kennedy–Sassoon tradition, and conceptual-metaphor theory in the Lakoff–Kövecses tradition produces stronger philological claims than any of the three frameworks in isolation. We argue that this trifold integration is, in published Qurʾānic studies, here brought together for the first time. The second aim is **descriptive**: to map every Qurʾānic occurrence of the ten core roots, to render that map publicly verifiable through an open concordance, and to extract from it empirical regularities that previous scholarship—working in either tafsir, lexicography, or single-word semantic analysis—was not in a position to detect. The third aim is **interpretive**: to argue that the resulting continuum constitutes a coherent "logic of emotional escalation" with deep structural affinities to modern psychology of emotion, and to identify the specific points at which the Qurʾānic continuum *exceeds* the explanatory range of the contemporary models.

The paper's claim to **originality** rests on five distinct contributions: (i) the first integration of Izutsu, Kennedy, and Lakoff in a Qurʾānic study; (ii) a fully reproducible computational pipeline over the Quranic Arabic Corpus, released open-source; (iii) the discovery, to our knowledge unreported, of the exclusively-Medinan distribution of *sakhaṭ* and the exclusively-Meccan distribution of *asaf*; (iv) the demonstration via network-centrality analysis that *baghy* serves as the bridge node between the emotional and moral-evaluation fields of the Qurʾān; and (v) the substantive argument that Q. 67:8 (*takādu tamayyazu min al-ġayẓ*) constitutes one of the strongest historical instances of the "container collapse" pattern identified by Lakoff and Kövecses (1987).

### 1.3. Prior work and the gap

Prior scholarship clusters into five lines, each insufficient on its own to address the structural question that motivates this paper.

**Single-word lexical studies** treat individual lexemes in detail but rarely place them in relation to one another. The most directly relevant Persian-language precedent—Narimani, Iqbali, and Chari's (2021) study of *ghayẓ*, *ghaḍab*, and *sakhaṭ* in *Pizhūhish-hā-yi Qurʾān va Ḥadīth*—covers three of our ten roots but does not place them on a graded scale or extend the analysis to the inner-distress and rebellion stages. Their analysis demonstrates, on tafsir grounds, that *ghaḍab* is the central anger lexeme (predicated of God, prophets, and believers), *sakhaṭ* is reserved for divine displeasure with hypocrites, and *ghayẓ* is exclusive to the unbelievers and hypocrites in human-attribution contexts. We confirm and extend their lexical-tafsir findings with corpus-distributional evidence, scalar-semantic ordering, and the cognitive-linguistic *kaẓm* analysis. Qarizadeh, Salmani Marvast, Meymandi, and Farsi (2024) provide a polysemy analysis of *ṭughyān* alone in *Pizhūhish-hā-yi Zabānshinākhtī-yi Qurʾān*, showing that the root attests in 27 suras and 13 morphological forms with the central meaning of "transgressing the limit." Both works illustrate the present gap: high-quality lexical work is available, but no integrated continuum.

**Ethics-of-anger studies** focus on the imperative of *kaẓm al-ghayẓ* (restraining suppressed rage; Q. 3:134) and adjacent verses, drawing on the *aḥādīth* tradition. These works are normatively rich but linguistically thin and do not interrogate the conceptual architecture of the lexicon.

**Cognitive-semantic studies** in the Izutsu tradition—including Qāʾimīniyā's (2011) *Maʿnāshināsī-yi Shinākhtī-yi Qurʾān* and the methodological work of Pakatchi—have begun to apply cognitive linguistics to Qurʾānic vocabulary, but no published work has yet treated the negative-emotion field as a graded continuum or validated it against full-corpus evidence. The work of Maalej (2004) on conceptual metaphor in Tunisian Arabic anger expressions, while linguistically rigorous, focuses on contemporary spoken Arabic rather than the Qurʾānic register.

**Translation-criticism studies** observe the levelling tendency of translations and identify it as a structural defect, but lack a reference model of the spectrum against which translations can be evaluated.

**Islamic psychology** has begun to extract emotion-regulation models from Qurʾānic sources, but this work has predominantly drawn on *aḥādīth* and overlooked the systematic linguistic analysis of the Qurʾānic surface itself.

The present paper fills the gap at the intersection of all five lines: it offers (a) a unified theoretical frame, (b) corpus-empirical validation, (c) novel distributional findings, (d) a translation-criticism reference model, and (e) a culturally-grounded model that practical Islamic-psychology can build on.

### 1.4. Research questions and hypotheses

We address five research questions:

- **RQ1.** What is the internal structure of the Qurʾānic semantic field of negative emotion, and which roots constitute its principal nodes?
- **RQ2.** How can these roots be ordered on a continuum of *action intensity*, and what theoretical framework legitimates such ordering?
- **RQ3.** Does the empirical distribution of these roots in the Quranic Arabic Corpus—their frequency, their Meccan/Medinan distribution, their morphological profile, and their verse-level co-occurrence and centrality—corroborate or challenge the proposed continuum?
- **RQ4.** With which contemporary models of emotion (Gross's process model; Plutchik's wheel; Spielberger's STAXI; Lazarus-Scherer appraisal theory) is the Qurʾānic continuum structurally homologous, and where does it depart from them?
- **RQ5.** What practical implications follow for Qurʾānic translation and for clinically-applied Islamic psychology?

The principal hypothesis, which we will refer to as the **Qurʾānic Action-Intensity Continuum Hypothesis**, is:

> The ten core Arabic roots ḍyq, ḥzn, ʾsf, sxṭ, ġḍb, ġyẓ, myz, bġy, ṭġy, ʿtw operate not as synonyms or disconnected nodes but as ten distinct grades on a single semantic continuum structured by the variable *intensity of action*; the continuum is organised in four phenomenological stages, and its ordering is supported by both qualitative (etymological, exegetical, metaphorical) and quantitative (frequency, temporal distribution, network) evidence.

Five subsidiary hypotheses follow: (H1) the four-stage frequency distribution deviates from uniformity; (H2) Stage 4 is over-represented relative to the combined Stages 1–3; (H3) *sakhaṭ* shows a discursively-specialised exclusive-Medinan distribution; (H4) in the aya-level co-occurrence network, *baghy* operates as the bridge node between the emotional and the broader moral-evaluation field; (H5) the central image of "container collapse" (Q. 67:8) instantiates the Lakoff–Kövecses ANGER IS PRESSURIZED CONTAINER metaphor more transparently than any cited English exemplar.

---

## 2. Theoretical Framework

### 2.1. Izutsu's semantic-field method

Toshihiko Izutsu, in three foundational works—*The Structure of the Ethical Terms in the Koran* (1959), *God and Man in the Koran* (1964), and *Ethico-Religious Concepts in the Qurʾān* (1966/2002)—introduced a methodological revolution to Qurʾānic studies. Drawing on the structuralist linguistics of the Trier–Weisgerber tradition and on East Asian philosophy of language, Izutsu argued that the central terms of the Qurʾān—*Allāh*, *īmān*, *kufr*, *ẓulm*, *taqwā*—are not isolated propositions but nodes in a network of syntagmatic, paradigmatic, and oppositional relations. The aggregate of these relations constitutes what he called the "Qurʾānic *Weltanschauung*."

Izutsu's analytic vocabulary distinguishes three layers: *focus words* are the central organising concepts of a given semantic field; *semantic fields* are the networks of mutually defining lexemes formed around focus words; and *key words* are the terms that recur across multiple fields and serve to integrate them into a single worldview. This three-layer structure has proved extraordinarily productive in subsequent Qurʾānic semantic work, both in English (Saleh, Rippin) and Persian (Qāʾimīniyā 2011, 2014; Pakatchi).

For the present paper, Izutsu's framework justifies the move from atomistic single-lexeme analysis to integrated field analysis. The ten target roots are not chosen at random but as the field around the focus words *ghaḍab* (the central anger term) and *baghy* (the central transgression term), with the cluster of *ḍīq*, *ḥuzn*, *asaf* identifying the lower-intensity boundary of the field and *ʿutuww* its upper-intensity boundary. Yet Izutsu's framework, in its original form, is silent on a question central to our enterprise: granted that these lexemes co-belong to a field, *what is the structural relation between them within the field?* It is at this point that we require scalar semantics.

### 2.2. Scalar semantics: from network to continuum

The contemporary linguistic theory of *gradable predicates*, developed in the work of Kennedy (1999, 2007), Sassoon (2010), and others, supplies the missing apparatus. On this framework, a graded predicate maps to a *scale* characterised by three components: (a) a *dimension* of measurement (e.g., temperature, length, intensity); (b) an *ordering* of points on that dimension; and (c) a unit of comparison, explicit or implicit. Scalar predicates take degree modifiers (*very*, *extremely*, *somewhat*, *barely*) and admit comparative constructions (*more X than*, *too X*); these properties signal their underlying scalar structure.

We argue that the Qurʾānic field of negative emotion is precisely such a scale, with three definitional components: (a) the dimension is *intensity of action*, itself decomposable into three sub-dimensions (locus of emotion: from inner to outer; experiential intensity: from low to high; scope of consequence: from individual to structural); (b) the ordering follows the four-stage progression from *ḍīq* to *ʿutuww*; (c) the implicit unit is the *degree of externalisation* of emotion from inner phenomenology to social rupture. The framework allows us to make formally precise the otherwise intuitive claim that *ghayẓ* is "more intense than" *ghaḍab*, or that *baghy* is "more externalised than" *sakhaṭ*; without scalar semantics, such claims rely on tacit appeal to native-speaker intuition.

### 2.3. Conceptual metaphor theory and the container schema

The third theoretical layer, conceptual metaphor theory (Lakoff & Johnson 1980; Lakoff & Kövecses 1987; Kövecses 2000, 2010), supplies the cognitive-linguistic resources needed to explain *why* the spectrum scales as it does. Conceptual metaphors, on this view, are not ornaments of speech but cognitive structures that allow abstract conceptual domains (such as emotion) to be understood through mappings onto concrete domains (such as bodily sensation, motion, container, heat).

Lakoff and Kövecses's classic 1987 analysis of English anger established that the lexicon of anger is organised around the master metaphor ANGER IS THE HEAT OF A FLUID IN A PRESSURIZED CONTAINER. Surface expressions—"to boil with rage," "to be steaming," "to blow one's top," "to keep a lid on it," "she lost her cool," "I'm about to explode"—all instantiate this single underlying schema. The metaphor accommodates a four-step internal trajectory: (i) emotion as fluid in container; (ii) intensifying heat increasing pressure; (iii) attempts to contain the pressure (sealing the lid); (iv) container collapse if pressure overcomes containment.

A central observation of the present paper is that the Qurʾānic triplet *ghayẓ–kaẓm–tamayyuz* operationalises *exactly this same four-step structure*, more than thirteen centuries before its modern theoretical articulation. *Ghayẓ* is glossed in the classical lexica as "compressed, contained anger"—the fluid in the sealed container. *Kaẓm*, etymologically the act of tying off a waterskin to prevent spillage, is the agent-internal regulation that maintains containment; Q. 3:134 commends *al-kāẓimīn al-ghayẓ* as the believers who hold the seal. *Tamayyuz*, in Q. 67:8 (*takādu tamayyazu min al-ġayẓ*), depicts the failure mode: the container itself bursts apart from the pressure of the contained anger.

The Q. 67:8 image deserves particular attention because it instantiates the *container-collapse* failure mode more transparently than any English exemplar in Lakoff and Kövecses's (1987) corpus. In English, the relevant verbs (*explode*, *burst*, *blow up*) report the exit of pressurised content but rarely figure the structural disintegration of the vessel itself. In contrast, *tamayyaza*, derived from the root *m-y-z* (to separate, to part, to sever), explicitly figures the splitting of the structural integrity of the container. We argue, in §5.6, that this verse provides one of the most articulated historical instances of the conceptual-metaphor structure that Lakoff and Kövecses identified.

### 2.4. The integrated framework

The three theoretical layers operate complementarily. Izutsu identifies the boundaries of the field; Kennedy–Sassoon scalar semantics order its members along the action-intensity dimension; Lakoff–Kövecses conceptual metaphor theory explains the cognitive basis of the central pressurisation-collapse metaphor that organises Stage 3. Each layer supplies what the others lack. Without Izutsu, we would lack motivation for treating the ten roots as field-coordinated; without scalar semantics, we would lack the apparatus to formally order them; without CMT, we would lack the cognitive grounding for the pressurised-container schema underlying the climactic *kaẓm–tamayyuz* sequence.

---


![The four-stage Qurʾānic emotion-intensity continuum, mapped along a single horizontal axis of *action-intensity*. Each node corresponds to one of the ten core Arabic roots; node area is scaled by attestation frequency in the Quranic Arabic Corpus (Dukes 2011). Stages cluster the lexemes by their dominant phenomenological signature: Stage 1 (internal distress, *ḍyq–ḥzn–ʾsf*, blue) marks pre-anger affective contraction; Stage 2 (explicit anger, *sxṭ–ġḍb*, orange) marks normatively-loaded outward orientation; Stage 3 (explosive rage, *ġyẓ–myz*, red) marks containment failure; Stage 4 (behavioural rebellion, *bġy–ṭġy–ʿtw*, green) marks the externalised structural outcome. The visual asymmetry between small Stage-1/2/3 nodes and the disproportionately large Stage-4 nodes anticipates the corpus-level skew toward behavioural-outcome vocabulary discussed in §4.2.](fig1_continuum.pdf){width=100%}


## 3. Methods

### 3.1. Corpus

The empirical analysis uses the **Quranic Arabic Corpus** (QAC), version 0.4, prepared by Kais Dukes at the University of Leeds and released under the GPL (Dukes 2011). The QAC provides a morphologically tagged record for each of the 128,219 segmentable units in the Qurʾānic text. Every record specifies: (a) location in the form *(sūra:āya:word:segment)*; (b) surface form in Buckwalter ASCII transliteration; (c) part-of-speech tag; (d) morphological features including root, lemma, gender, number, case, and (where applicable) semantic flags. Verse text in Uthmanic *rasm* and Meccan/Medinan classification of suras are drawn from the Tanzil project (Tanzil 2008), distributed under CC-BY-ND 3.0.

### 3.2. Selection of target roots

The ten core roots were selected by three concurrent criteria: (i) *exegetical centrality* — appearance as a focal reference in at least three of the four standard pre-modern lexica (Ibn Fāris's *Maqāyīs*, al-Rāghib's *Mufradāt*, Ibn Manẓūr's *Lisān*) and one twentieth-century lexicon (Mostafavi's *Taḥqīq*); (ii) *minimum corpus frequency* of four attestations, sufficient for elementary distributional analysis; (iii) *thematic membership* in the negative-emotion field without significant overlap with adjacent fields (epistemology, faith, normative ethics).

A second tier of six roots—**krh, šnʾ, jrm, fsq, ẓlm, ʿdw**—is extracted as "umbrella moral terms" for robustness checks (§4.5) and inter-field co-occurrence analysis (§4.7). These roots, while semantically related to the emotional field, either have inflated cardinality (*ẓlm*: 315 attestations functioning as a meta-category) or properly belong to the adjacent field of normative ethics (*jrm*, *fsq*); they are excluded from the principal continuum to preserve focus.

### 3.3. Computational pipeline

The pipeline is implemented in Python (MIT-licensed) and operates in five steps: (1) parse the QAC morphology file; (2) filter on target roots; (3) collapse multi-segment morphemes to surface words preserving the *(sūra:āya)* coordinate; (4) join with sura-level metadata for Meccan/Medinan classification; (5) emit four classes of output (master concordance CSV, per-root concordances, distributional summaries, network/centrality CSVs). Code is organised across `analysis/qac_parser.py`, `analysis/spectrum_roots.py`, `analysis/extract_concordance.py`, `analysis/advanced_metrics.py`, and visualisation modules. The complete analysis is reproducible from a fresh clone of the repository in two commands: `python analysis/extract_concordance.py && python analysis/visualize_spectrum.py && python analysis/visualize_advanced.py`.

### 3.4. Quantitative analyses

Beyond raw frequency tabulation, we conduct: (a) chi-squared tests against the null of uniform stage distribution and against the null of equal Stages 1+2+3 vs Stage 4 split; (b) two-sided exact binomial tests for Meccan/Medinan exclusivity claims, taking 0.60 as the corpus-baseline rate of Meccan attestations (the proportion of Meccan ayat in the QAC); (c) morphological breakdown by part-of-speech (verb, noun, adjective, participle, other); (d) network analysis on the verse-level co-occurrence graph, computing weighted degree, betweenness centrality, closeness centrality, and (where the graph permits) eigenvector centrality.

### 3.5. Qualitative analyses

We supplement the quantitative analyses with: (a) comparative etymological analysis across the four reference lexica named above; (b) comparative *tafsīr* analysis for the canonical exemplar verses, drawing on al-Ṭabāṭabāʾī's *al-Mīzān*, al-Zamakhsharī's *al-Kashshāf*, al-Ṭabarsī's *Majmaʿ al-Bayān*, and Ibn ʿĀshūr's *al-Taḥrīr wa-l-Tanwīr*; (c) phenomenological analysis of contextual markers (*ḍīq al-ṣadr*, *ḥuzn al-qalb*, *asaf al-nafs*); (d) translation-criticism analysis comparing five major translations (Yusuf Ali, Pickthall, Arberry, Saheeh International, Hilali-Khan) on the canonical exemplar verses.

### 3.6. Validity check

To verify the integrity of the pipeline, the ten "headline" exemplar verses—Q. 15:97, 2:38, 43:55, 47:28, 48:6, 3:134, 67:8, 42:42, 96:6, 25:21—were independently verified against the corpus output. All ten were found in the corpus output with the correct surface form and verse text matching the Uthmani edition. This validation confirms that the Buckwalter transliteration and segment-collapse algorithms operate without systematic error.

---

## 4. Findings

### 4.1. The four-lexicon etymology table

Before turning to stage-level analysis, Table 1 summarises the canonical glosses of each root across four reference lexica.

**Table 1. Comparative etymology of the ten core roots across four classical/standard Arabic lexica**

| Root | Maqāyīs (Ibn Fāris) | Mufradāt (al-Rāghib) | Lisān al-ʿArab (Ibn Manẓūr) | Taḥqīq (Mostafavi) |
|:----:|:---|:---|:---|:---|
| ḍ-y-q | constriction; absence of opening | the state of being pressed upon, contrasted with capacity (*saʿah*) | reduction of available space, from *saʿah* to *ḍīq* | inner or outer absence of expansion (*basṭ*) |
| ḥ-z-n | rough/uneven ground → heaviness of soul | sorrow as the opposite of joy (*faraḥ*) | rugged ground, then roughness of the self | affective response to perceived loss |
| ʾ-s-f | intense grief mixed with anger | extreme anger conjoined with grief | reaching the limit of grief and anger | composite of grief and proximate anger |
| s-kh-ṭ | severe aversion and ethical rejection | the opposite of *riḍā* (consent), with intensity | severe non-acceptance with judgment | declarative rejection grounded in moral assessment |
| gh-ḍ-b | inner agitation and motion | the boiling of the heart's blood seeking retribution | a rising perturbation of the soul | directed emotion enabling retributive action |
| gh-y-ẓ | pressure and surge, contained | the most intense forms of contained anger | filling of the self with restrained anger | high-pressure emotional accumulation |
| m-y-z | separation, pulling apart | distinguishing one from another | structural differentiation | structural rupture under inner pressure |
| b-gh-y | seeking beyond rightful bounds | overstepping the path of right | dominance through aggression | aggressive action with intent to oppress |
| ṭ-gh-y | overflow of water past its bank | crossing the permitted measure | severe transgression of the limit | rebellious shattering of normative bounds |
| ʿ-t-w | severe rebellion with arrogance | extreme self-aggrandisement in disobedience | obstinate excess | entrenched rebellious posture |

The table shows that the ordering from *ḍīq* to *ʿutuww* is not the construction of the present analysis but is internally encoded in the lexicographic tradition itself: the classical lexica already gloss each root with progressively more externalised and structural meanings, ascending from inner-bodily *ḍīq* through volitional *sakhaṭ*, to compressed *ghayẓ*, to externalised *ṭughyān*, to entrenched *ʿutuww*.

### 4.2. Distributional summary

Table 2 reports the principal distributional facts for the ten core roots. The table integrates frequency, Meccan/Medinan split, and morphological profile; it forms the empirical backbone of the analyses that follow.

**Table 2. Distributional and morphological profile of the ten core roots**

| Stage | Root | Total | Meccan | Medinan | Verb | Noun | Participle |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | ḍyq (ضيق) | 13 | 9 | 4 | 8 | 3 | 1 |
| 1 | ḥzn (حزن) | 42 | 26 | 16 | 37 | 5 | 0 |
| 1 | ʾsf (أسف) | 5 | 5 | 0 | 1 | 4 | 0 |
| 2 | sxṭ (سخط) | 4 | 0 | 4 | 3 | 1 | 0 |
| 2 | ġḍb (غضب) | 24 | 13 | 11 | 6 | 16 | 2 |
| 3 | ġyẓ (غيظ) | 11 | 3 | 8 | 3 | 7 | 1 |
| 3 | myz (ميز) | 4 | 2 | 2 | 4 | 0 | 0 |
| 4 | bġy (بغي) | 96 | 55 | 41 | 65 | 28 | 3 |
| 4 | ṭġy (طغي) | 39 | 29 | 10 | 13 | 19 | 7 |
| 4 | ʿtw (عتو) | 10 | 9 | 1 | 5 | 4 | 1 |
| **Σ** | — | **248** | **151** | **97** | **145** | **87** | **15** |

Aggregating across the four stages: Stage 1 = 60 attestations; Stage 2 = 28; Stage 3 = 15; Stage 4 = 145. The chi-squared test against the null of uniform distribution rejects (χ²(3) = 165.45, *p* < 0.001), confirming H1. The chi-squared test against the null of equal split between Stages 1+2+3 and Stage 4 rejects (χ²(1) = 7.11, *p* = 0.008), confirming H2. The corpus thus exhibits a strongly non-uniform allocation, weighted approximately 2.4× toward the rebellion stage. The interpretive significance of this asymmetry is taken up in §5.4.


![Per-root and per-stage frequency of the 248 core spectrum attestations. *Left panel*: linear-scale frequency for each of the ten roots; bar colour encodes the phenomenological stage. The decay across Stage 1 (blue) is nearly monotonic (*ḥzn* 42 → *ḍyq* 13 → *ʾsf* 5), reflecting an internal hierarchy from generic sadness to event-specific compunction; Stage 4 (green) shows a comparable internal asymmetry (*bġy* 96 vs. *ʿtw* 10) that mirrors the lexical division of labour between distributed-aggression (*bghy*) and obstinate-defiance (*ʿutuww*) outlined in §4.6. *Right panel*: stage totals expose the corpus's pedagogic emphasis — Stage 4 alone (n = 145) exceeds the combined Stage-1+2+3 total (n = 103) by a factor of 2.4, χ²(1) = 7.11, *p* = 0.008. The pattern is theologically motivated: the Qurʾān describes *behavioural outcomes* of unmanaged emotion more thoroughly than the *inner phenomenology* — a discursive priority discussed in §5.4.](fig2_frequency_by_stage.pdf){width=95%}


![Stacked Meccan/Medinan distribution for each of the ten core roots. The numerals above each bar give the raw Meccan/Medinan split. Two distributional extremes warrant emphasis. *ʾasaf* (Stage 1) is attested **exclusively** in Meccan suras (5/0): the lexeme of "regret-grief" emerges in the discursive context of prophetic disappointment with rejection (Q. 18:6, Q. 43:55, Q. 7:150). *Sakhaṭ* (Stage 2) is attested **exclusively** in Medinan suras (0/4; binomial *p* = 0.026 against the 0.60 corpus baseline of Meccan attestations): the lexeme of "comprehensive divine displeasure" emerges only after the Hijra, in confrontation with the *munāfiqūn* (Q. 47:28, Q. 5:80, Q. 9:58, Q. 3:162). The visualisation thus encodes a non-trivial finding: not every root in the spectrum behaves as a context-neutral lexical resource — two of them are *discursive-contextually specialised*, a pattern theorised in §5.5 as a general feature of Qurʾānic vocabulary.](fig3_meccan_medinan.pdf){width=95%}


![Morphological profile of the ten core roots, broken out by part of speech. The left-to-right gradient shows a *typological shift* across the continuum that supplements the frequency analysis. Stage 1 is verbally dominant — *ḥzn* 88% verb forms (37 v / 5 n), *ḍyq* 62%, *ʾsf* 20% by raw count but predominantly verbal in surface use — consistent with the ontology of distress as a *transient, situationally-induced state*. Stage 2 nominalises: *ġḍb* shifts the centre of gravity to the noun (16 n / 6 v), as the lexeme acquires a stable, attributable referent ("the wrath of God"). Stage 4 is the most nominal, with participial forms emerging (*ṭāgūt*, *bāghin*); the rebellion vocabulary entrenches as a stable agent-property rather than a transient process. This morphological gradient — verbal Stage 1 → nominal Stage 4 — is independent corpus-internal evidence for the action-intensity continuum: as intensity ascends, the linguistic representation reifies from *event* to *attribute* to *identity*.](fig5_morphology_stack.pdf){width=95%}


### 4.3. Stage 1 — Internal Distress

The lower bound of the continuum is occupied by three roots—*ḍ-y-q*, *ḥ-z-n*, *ʾ-s-f*—with sixty combined attestations. Each marks a distinct phenomenological mode within the inner-distress family.

**4.3.1. *Ḍīq* (13 attestations; 9 Meccan / 4 Medinan).** Ibn Fāris glosses the root as "constriction, narrowness, lack of opening." Al-Rāghib places it in direct opposition to *saʿah* (capacity, expansion). In the Qurʾān, the root appears predominantly in the construction *ḍīq al-ṣadr* (constriction of the chest), a phenomenologically concrete localisation of the experience to the embodied site of the chest. The exemplar verse Q. 15:97 (*wa-laqad naʿlamu annaka yaḍīqu ṣadruka bimā yaqūlūn*) frames *ḍīq* as the prophetic response to social rejection—an inner, bodily-localised pressure that does not translate into outward aggression. Al-Ṭabāṭabāʾī observes in *al-Mīzān* (vol. 12, p. 195) that the verse expresses divine *knowledge* of the prophetic *ḍīq* rather than its prohibition or correction; this is a phenomenologically natural, theologically licit state, not a moral failing.

The morphological profile of *ḍīq* is informative: 8 verbal forms against 3 nominal (verb-to-noun ratio of 2.7:1) and 1 participial form. Predominantly verbal forms register the root as a *transient, situationally-induced state* rather than a stable trait.

**4.3.2. *Ḥuzn* (42 attestations; 26 Meccan / 16 Medinan).** *Ḥuzn* is the most frequent and most morphologically verbal of the spectrum lexemes (37 verbal forms against 5 nominal; 88% verbal). Ibn Manẓūr's *Lisān al-ʿArab* preserves the etymologically primary meaning of the root: "rugged, uneven ground" (*al-arḍ al-ġalīẓah*). The metaphorical extension to sustained sorrow figures grief as a kind of inner roughness or discontinuity in the otherwise smooth course of the soul's life. This Arabic etymological intuition strikingly anticipates the EMOTION IS A LANDSCAPE conceptual metaphor analysed by Kövecses (2000).

Q. 2:38 (*fa-lā khawfun ʿalayhim wa-lā hum yaḥzanūn*) places *ḥuzn* in syntagmatic pair with *khawf* (fear) and in opposition to divinely-given guidance, framing it as the affective signature of *being separated from guidance*. Al-Ṭabāṭabāʾī (*al-Mīzān* vol. 1, p. 146) describes this verse as foundational for "the science of the soul in the Qurʾān" (*ʿilm al-nafs al-Qurʾānī*).

The 88% verbal profile of *ḥuzn* parallels that of *ḍyq* and reinforces the Stage-1 generalisation: the inner-distress lexemes denote *transient, regulable states* rather than fixed dispositional traits.

**4.3.3. *Asaf* (5 attestations; 5 Meccan / 0 Medinan).** The least frequent and most theoretically suggestive lexeme of Stage 1. Both Ibn Fāris and al-Rāghib gloss *asaf* as the conjunction of grief and anger (*al-jamʿ bayna al-ḥuzn wa-l-ġaḍab*), placing it precisely at the threshold between Stage 1 and Stage 2. Q. 43:55 (*fa-lammā āsafūnā intaqamnā minhum*) frames *asaf* as the immediate causal precursor of divine retribution—*asaf* is what the Qurʾān reports as obtaining when grieved divine response transitions to active retribution. Al-Ṭabarsī's *Majmaʿ al-Bayān* (vol. 9, p. 82) is precise: "*al-asaf* here is the intense anger that arises from the prior grief."

The exclusive-Meccan distribution (5/0; binomial *p* = 0.16, suggestive but not decisive given the small sample) is interpretable in discursive-contextual terms: *asaf* attests in narrative passages depicting prior prophets' encounter with rejection (Mūsā vis-à-vis Pharaoh's people; the rejection of warnings by Meccan polytheists). The Medinan corpus, oriented toward the immediate post-Hijra confrontation with hypocrisy and rebellion, moves directly into the Stage-2 vocabulary without dwelling in the grief–anger threshold register.

**4.3.4. Network evidence for Stage-1 coherence.** The aya-level co-occurrence network (Figure 4) reveals that the strongest single edge connects *ḥzn* and *ḍyq* (weight 3); these two lexemes share three verses in the Qurʾān, more than any other pair within the spectrum. This empirical density provides independent verification of the Stage-1 grouping. Centrality analysis (Figure 7) places *ḥzn* among the highest-degree nodes (weighted degree 5, tied with *ġḍb*).

### 4.4. Stage 2 — Explicit Anger

**4.4.1. *Sakhaṭ* (4 attestations; 0 Meccan / 4 Medinan).** Despite its low frequency, *sakhaṭ* furnishes one of the paper's principal findings. The exclusive-Medinan distribution—zero Meccan attestations among four total—has a binomial-test p-value of 0.026 against the corpus baseline of 0.60 Meccan probability, statistically significant at α = 0.05. Confirms H3.

Contextual analysis of all four occurrences reveals the same operative pattern: *sakhaṭ* attests in connection with the *Munāfiqūn* (hypocrites) or with quasi-believers whose outward profession of faith conflicts with their inward dispositions. Q. 47:28 (*ittabaʿū mā askhaṭa Allāh wa-karihū riḍwānahu*) is the canonical exemplar. Following Narimani et al. (2021), we read *sakhaṭ* not as an instantaneous emotional surge but as a sustained *ethical disapprobation*; the present paper extends their lexical-tafsīr argument with corpus evidence and proposes:

> **Hypothesis (Discursive Specialisation of *sakhaṭ*):** In the Qurʾānic lexicon, *sakhaṭ* operates as a discursively specialised lexeme, reserved for divine displeasure with the *Munāfiqūn*—agents whose *zāhir* (outward profession) departs from their *bāṭin* (inward orientation). Because the *Munāfiqūn* category is constitutively a Medinan-period phenomenon, *sakhaṭ* attests exclusively in Medinan suras. This pattern is an instance of a more general phenomenon of *discursive-contextual lexical specialisation* in the Qurʾānic register.

**4.4.2. *Ghaḍab* (24 attestations; 13 Meccan / 11 Medinan).** *Ghaḍab* is the central anger lexeme of the Qurʾān. Its near-balanced Meccan/Medinan distribution (54% Meccan) marks it as the *unmarked default* of the explicit-anger family. Classical lexicography defines *ghaḍab* as the inner agitation of the heart oriented toward retribution (al-Rāghib), or as inner motion that disposes the agent to action (Ibn Fāris). The lexeme is grammatically balanced: predicated of God (Q. 48:6 *ghaḍiba Allāhu ʿalayhim*), of prophets, and of the believers.

Morphologically, *ghaḍab* differs sharply from *ḥuzn*: 6 verbs against 16 nouns (33% verbal, 67% nominal) and 2 participles. Where *ḥuzn* is a *transient state*, *ghaḍab* is a *structural concept-state*: a state with organisational ontological standing. Al-Fakhr al-Rāzī's *Mafātīḥ al-Ghayb* (vol. 28, p. 84) glosses divine *ghaḍab* as *irādat inzāl al-ʿiqāb* ("the will to inflict punishment")—not an emotional response but a normative-juridical orientation.

**4.4.3. *Ghaḍab* as bridge node.** Network analysis (Figure 7) places *ghḍb* among the top three nodes for betweenness centrality (0.17), tied with *ġyẓ* and surpassed only by *bġy*. Notable edges include *ghḍb–ġyẓ* (the upward transition to Stage 3), *ghḍb–ḥzn* (the downward link to Stage 1), and *ghḍb–bġy* (the link to Stage 4).

### 4.5. Stage 3 — Explosive Rage

**4.5.1. *Ghayẓ* and the *kaẓm* metaphor (11 attestations; 3 Meccan / 8 Medinan).** Classical glosses of *ghayẓ* as "compressed, contained anger" (al-Rāghib), "the highest concentration of restrained anger" (Mostafavi), and "filling of the self with restrained anger" (Ibn Manẓūr) converge on a single conceptual structure: *ghayẓ* is the pressurised contents of a sealed vessel.

Q. 3:134 commends *al-kāẓimīn al-ghayẓ*: those who restrain *ghayẓ*. The verb *kaẓm* derives from the act of tying off a waterskin to prevent fluid escape; it is the agent-internal regulation that sustains containment. Read through Lakoff and Kövecses's framework, the *ghayẓ–kaẓm* pair instantiates with great precision the ANGER IS A PRESSURIZED CONTAINER metaphor: *ghayẓ* is the contained fluid; *kaẓm* is the seal. Figure 6 visualises this conceptual structure.

The Medinan-leaning distribution of *ghayẓ* (8/3) reflects the discursive context in which inner anger management becomes a salient pedagogical concern: the formative Medinan community required affective discipline within a still-fragile *umma* facing internal *Munāfiq* and external Quraysh hostility.

**4.5.2. *Tamayyuz*: container collapse in Q. 67:8.** The single most articulated image of rage in the Qurʾān, and indeed the single most important verse for our argument, is Q. 67:8: *takādu tamayyazu min al-ġayẓ*—"[the fire] is on the verge of bursting apart from rage." The verb *tamayyaza* derives from the root *m-y-z* (to separate, to part, to sever). The image is not simply that of pressure exiting through the seal but of *the structural integrity of the container itself failing*.

Lakoff and Kövecses's (1987) original analysis identifies "container collapse" as the failure mode of the master metaphor, but their English exemplars (*she blew her top*, *he exploded*, *I lost it*) report the *exit* of pressurised content rather than the *structural disintegration* of the vessel. Q. 67:8 makes the disintegration explicit. We argue, accordingly, that this verse furnishes one of the most articulated linguistic instances of "container collapse" in any documented historical text—pre-modern or modern. Confirms H5.

The theoretical implication is significant. The Lakoff–Kövecses analysis was originally framed in terms of contemporary American English; the Qurʾānic data extend its empirical base to a register of seventh-century Arabic, supporting a stronger universality claim for the underlying conceptual structure.

### 4.6. Stage 4 — Behavioural Rebellion

**4.6.1. *Baghy* (96 attestations; 55 Meccan / 41 Medinan).** The most frequent lexeme of the spectrum and, by network-centrality measures, its bridge node. *Baghy* is glossed as "seeking beyond rightful bounds" (al-Rāghib) and "aggressive seeking with intent to oppress" (Mostafavi). Q. 42:42 (*innamā al-sabīlu ʿalā lladhīna yaẓlimūna l-nāsa wa-yabghūna fī l-arḍi bi-ġayri l-ḥaqq*) collocates *baghy* with *ẓulm*, embedding the lexeme firmly in the moral-evaluation register. Ibn ʿĀshūr's *al-Taḥrīr wa-l-Tanwīr* (vol. 25, p. 126) clarifies the syntagmatic relation: "*baghy* and *ẓulm* are nearly synonymous, except that *baghy* is specific to non-rightful aggression against another, while *ẓulm* covers all forms of injustice."

**4.6.2. *Baghy* as bridge node.** Network analysis (Figure 7 and Table 4 below) reveals that *baghy* has the highest betweenness centrality (0.39) and the highest closeness centrality (0.39) of any node in the spectrum. Furthermore, *baghy* exhibits the highest cross-field co-occurrence with the umbrella moral terms: 19 aya-level co-occurrences with *ẓlm/jrm/fsq/ʿdw/krh/šnʾ* combined, of which 8 are with *ʿdw*, 4 with *ẓlm*, and 3 with *krh* (Table 4). This bridging profile confirms H4.

**Table 4. Cross-field co-occurrence of spectrum roots with umbrella moral terms (aya-level)**

| Root | krh | šnʾ | jrm | fsq | ẓlm | ʿdw | Total |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| ḍyq | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ḥzn | 0 | 0 | 0 | 0 | 1 | 1 | 2 |
| ʾsf | 0 | 0 | 0 | 0 | 1 | 1 | 2 |
| sxṭ | 1 | 0 | 0 | 0 | 0 | 0 | 1 |
| ġḍb | 1 | 0 | 0 | 0 | 2 | 3 | 6 |
| ġyẓ | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| myz | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| **bġy** | **3** | **1** | **1** | **2** | **4** | **8** | **19** |
| ṭġy | 1 | 0 | 0 | 0 | 2 | 1 | 4 |
| ʿtw | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

The radical concentration of cross-field ties at *baghy* is striking. Of 36 total cross-field ties across the ten spectrum roots, 19 (53%) involve *baghy*. *Baghy* thus serves as the principal lexical bridge between the emotional and the broader moral-evaluation field of the Qurʾān.

**4.6.3. *Ṭughyān* and the appraisal-cognitive precondition (39 attestations; 29 Meccan / 10 Medinan).** The root *ṭ-gh-y* derives etymologically from the image of water flooding past its banks. Q. 96:6–7 (*kallā inna l-insāna la-yaṭghā an raʾāhu staġnā*) compresses an entire psychology of rebellion into a conditional: human *ṭughyān* arises from the perception of *istighnāʾ* (self-sufficiency). This is, structurally, an appraisal-theoretic claim—that a particular emotional-behavioural disposition is conditioned on a specific cognitive evaluation of the self—and it is fully congruent with the appraisal models of Lazarus (1991) and Scherer (2001, 2005). Qarizadeh et al.'s (2024) polysemy analysis of *ṭughyān* notes the cognitive structure but does not place it in the broader framework; the present paper extends their analysis by identifying *ṭughyān* as the cognitive-appraisal node of Stage 4.

**4.6.4. *ʿUtuww* (10 attestations; 9 Meccan / 1 Medinan).** The most extreme lexeme of the spectrum. Glossed as "obstinate excess" (Ibn Manẓūr), "extreme self-aggrandisement in disobedience" (al-Rāghib), and "entrenched rebellious posture" (Mostafavi). Q. 25:21 collocates *ʿatū ʿutuwwan kabīrā* with *istakbarū fī anfusihim*, marking the lexeme as denoting rebellion that has crystallised into existential posture. The strongly Meccan distribution (9/1; binomial *p* = 0.06) reflects its rhetorical function as the terminal designation of those whose rejection of revelation has hardened beyond reach—a status repeatedly illustrated through the Meccan narratives of prior peoples (Nūḥ, ʿĀd, Thamūd, Pharaoh).


![Aya-level co-occurrence network of the ten core roots. Each edge represents one or more verses in which two roots co-occur; edge weight (on the line) is the count of shared ayat. The strongest edge — *ḥzn–ḍyq*, weight 3 — provides direct corpus-internal validation of the Stage-1 grouping: these two pre-anger lexemes share *more* verses than any other pair in the spectrum, indicating that the Qurʾān treats them as discursively conjoint phenomena ("constriction of the chest in sadness," Q. 11:12; Q. 6:33). The Stage 1–2 bridge (*ḥzn–ġḍb*) shows the natural psychological transition from sadness to anger when distress is externally provoked. *Baghy* (Stage 4) anchors the right-hand cluster, with edges reaching into the moral-evaluation lexicon (*ẓlm*, *jrm*, *fsq*) — a position formalised quantitatively in the next figure. Crucially, no edges link Stage 1 to Stage 4 directly: the spectrum is *transitive* in its co-occurrence pattern, requiring the mediating Stages 2 and 3, in line with the action-intensity gradient hypothesis.](fig4_cooccurrence.pdf){width=95%}


![Three centrality measures computed on the aya-level co-occurrence graph: (a) weighted degree — the total number of co-occurrence ties; (b) betweenness — how often a node lies on the shortest path between others, indicating bridge-node strength; (c) closeness — the inverse mean distance to all other nodes. *Baghy* attains the **highest betweenness centrality** (0.39), more than double the next-highest score, confirming its role as the principal *pivot* between the emotional field (Stages 1–3) and the wider moral-evaluation field of the Qurʾān (315 attestations of *ẓulm*, 66 of *jurm*, 54 of *fisq*, 106 of *ʿadāwah*). The closeness panel reveals a complementary pattern: *ḍyq* and *ḥzn* (Stage 1) achieve high closeness, indicating that the internal-distress cluster is structurally *central* to the spectrum even though peripheral in raw frequency. Together these measures support a layered reading of the network — Stage 1 supplies the affective core, Stage 4 supplies the structural bridge to neighbouring moral-discursive fields, while Stages 2–3 mediate the energy transfer between them.](fig7_centrality.pdf){width=95%}


### 4.7. Robustness checks: the umbrella moral terms

For robustness, the six umbrella roots were extracted and analysed. Their distributions (Table 5) confirm that the spectrum's structure is not artefactual.

**Table 5. Distribution of umbrella moral terms**

| Root | Total | Meccan | Medinan | Binomial p | Interpretation |
|:----:|:-:|:-:|:-:|:-:|:---|
| krh | 41 | 14 | 27 | 0.005 | Significantly Medinan; *Munāfiq*-aversion register |
| šnʾ | 3 | 1 | 2 | — | n too small for inference |
| jrm | 66 | 60 | 6 | < 0.0001 | Strongly Meccan; anti-*shirk* polemic |
| fsq | 54 | 20 | 34 | 0.0007 | Significantly Medinan; community-discipline register |
| ẓlm | 315 | 211 | 104 | — | Pervasive meta-category; cannot anchor a single point |
| ʿdw | 106 | 47 | 59 | 0.008 | Tilts Medinan; the lexeme of mutual antagonism |

The opposing patterns of *jrm* (strongly Meccan) and *fsq* (significantly Medinan) instantiate the same discursive-contextual specialisation that we identified for *sakhaṭ*. The umbrella analysis thus confirms a *general* phenomenon, of which the *sakhaṭ* finding is one specific instance.

### 4.8. Comparative translation analysis

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

The findings cohere into a single structural claim: the Qurʾānic lexicon of negative emotion encodes a **logic of emotional escalation** that operates simultaneously along three dimensions—locus (inner → outer), intensity (low → high), and scope (individual → structural). The four stages instantiate this trifold transformation. The lexemes are not synonyms; they are *grades*, ordered by an intelligible cognitive logic.

In compact form: *Emotional Pressure → Anger → Rage → Rebellion*, where the arrows index not mere temporal succession but conditional intensification: at each stage, failure to regulate produces transition to the next. Stage 1 is regulable by situation selection or modification; Stage 2 by attentional and cognitive change; Stage 3 by response modulation (the *kaẓm* suppression strategy); Stage 4 obtains as the post-failure descent.

### 5.2. Convergence with Gross's process model

The stages map with notable precision onto the four operational phases of Gross's (1998, 2014, 2015) process model of emotion regulation:

| Qurʾānic stage | Gross phase | Mapping rationale |
|:-:|:---|:---|
| 1 — *ḍīq, ḥuzn* | Situation selection / modification | Regulable inner state; the agent can adjust the situation to relieve pressure |
| 2 — *sakhaṭ, ghaḍab* | Attentional deployment / cognitive change | Outcome of cognitive-moral evaluation of situation |
| 3 — *ghayẓ, kaẓm* | Response modulation (suppression) | Direct internal regulation of the response itself |
| 4 — *baghy, ṭughyān, ʿutuww* | Post-failure descent into externalised dysfunction | Where Gross's model becomes silent |

The mapping is one-to-one for the first three phases. The fourth phase, however, is a place where the Qurʾān's continuum *exceeds* Gross's model: where Gross focuses on regulation success and treats failure outcomes as a residual category, the Qurʾānic continuum systematically describes the structural-moral pathologies that obtain when regulation fails. The Qurʾān is, on our reading, not merely a model of *emotion regulation* but a model of *the structural consequences of failed regulation*—a distinction whose practical implications we develop in §5.7.

### 5.3. Convergence with Plutchik, Spielberger, and appraisal theory

Plutchik's (1980, 2001) wheel of emotions arranges anger along an *annoyance → anger → rage* continuum. This three-level structure maps onto Qurʾānic Stages 1–3 (inner distress, explicit anger, explosive rage) but stops short of Stage 4. The Qurʾānic continuum's extension into the structural register is not a minor addition but a substantive theoretical move: it claims that emotion lexicons should be analysed not only psychologically but morally-anthropologically—as systems for tracking the social consequences of inner states, not merely the inner states themselves.

Spielberger's STAXI framework (1999) distinguishes trait anger (stable disposition), state anger (situational response), and anger control (deliberate restraint). The Qurʾānic lexicon implements an analogous trichotomy: Stage 1 lexemes (*ḥuzn*, *ḍīq*) describe sustained inner states; Stage 2 lexemes (*ghaḍab*) describe situational responses; and the *kaẓm* construct describes deliberate restraint. The lexemes thus carve up the space of emotional life along axes that contemporary psychometrics has, independently, isolated.

Appraisal theory (Lazarus 1991; Scherer 2001, 2005) holds that emotions arise from cognitive evaluations of situations rather than from raw stimuli. Q. 96:6–7 conditions *ṭughyān* on the appraisal of *istighnāʾ*—a textbook appraisal-theoretic claim. The Qurʾānic lexicon, on this evidence, treats certain emotion-behaviour transitions as cognitively conditioned, anticipating the appraisal-theoretic insight that emotion is not pre-cognitive but cognitively constituted.

### 5.4. The pedagogic asymmetry: explaining the Stage-4 over-representation

The 2.4× over-representation of Stage 4 (Section 4.2) is the most striking single fact in the empirical analysis. On a naive reading, the asymmetry is paradoxical: if the text aimed to describe a continuum of emotional escalation, one would expect the lower stages (cause) to be more frequent than the upper (effect). The actual distribution inverts this expectation.

The asymmetry resolves once the Qurʾān's purpose is correctly identified. The text is not a value-neutral psychology; it is a *hidāyah* text—a text of guidance—aiming at moral persuasion. Its lexical economy is shaped by what it is trying to do: not catalogue emotion exhaustively but *warn against the terminal social outcomes of unmanaged emotion*. Stage 4, the destination of unmanaged escalation, receives the rhetorical weight that pedagogically anchors the warning. The lower stages are described with sufficient precision to be recognised at onset—but the upper stage, where the moral-anthropological consequences manifest, dominates the lexical surface because that is where the text wants the reader to dwell.

This explanation has a methodological corollary that bears emphasis: corpus-distributional analyses of religious texts should not be interpreted as neutral reflections of an external referent. They are, instead, maps of *discursive emphasis*. Asymmetries in such maps register not gaps in ontology but priorities in pedagogy.

### 5.5. Discursive-contextual specialisation: a general phenomenon

The exclusive-Medinan profile of *sakhaṭ* and the exclusive-Meccan profile of *asaf*, taken together with the strong directional patterns of *jrm* (Meccan) and *fsq* (Medinan) in the umbrella roots, instantiate what we propose to call **discursive-contextual specialisation of lexemes**. This is the phenomenon whereby a member of a multi-lexeme semantic field becomes preferentially associated with a specific discursive register—in the Qurʾānic case, with the Meccan vs. Medinan rhetorical and sociolinguistic context. The specialisation is not random; in each documented case, contextual analysis confirms that the lexeme's preferential register is the register in which the corresponding referent obtains: *sakhaṭ* with the *Munāfiqūn* (a Medinan phenomenon), *asaf* with prior-prophet narratives (Meccan-rhetorical), *jrm* with anti-*shirk* polemic (Meccan), *fsq* with intra-community discipline (Medinan).

Discursive-contextual specialisation is, as far as we can establish, undocumented as a systematic phenomenon in Qurʾānic-linguistic scholarship; it is also relevant to the broader discussion of *Sitz im Leben* in Qurʾānic source criticism. Future work should test the generalisation across other multi-lexeme fields.

### 5.6. Q. 67:8 and the universality of the container metaphor

The most theoretically significant finding concerning conceptual metaphor is that Q. 67:8 (*takādu tamayyazu min al-ġayẓ*) instantiates the ANGER IS PRESSURIZED CONTAINER metaphor more transparently than any English exemplar in Lakoff and Kövecses's (1987) corpus. Where English idioms (*explode with rage*, *blow one's top*, *lose it*) report the *exit* of contained content, Q. 67:8 figures the *structural disintegration of the container itself* via the verb *tamayyaza* (m-y-z: to part, to sever).

This finding has a methodological and a theoretical consequence. *Methodologically*, it implies that the historical depth of the conceptual-metaphor inventory is greater than has often been recognised; the container metaphor for anger is not a peculiarity of contemporary English but a cross-culturally robust cognitive structure attested in seventh-century Arabic with arguably greater clarity than in modern Western corpora. *Theoretically*, it strengthens the universalist claim within CMT: that the bodily-grounded image schemas (CONTAINER, FORCE, BALANCE) underwrite human emotion conceptualisation across cultures and historical periods.


![The ANGER-IS-A-PRESSURIZED-CONTAINER schema (Lakoff & Kövecses 1987), instantiated by the Qurʾānic triplet *ghaḍab → ghayẓ + kaẓm → tamayyuz*. **Panel 1** (Stage 2): *ghaḍab* — an *open* container; the affect is present but unconcentrated, dissipating freely into language (the lexeme is the most nominally productive in the spectrum). **Panel 2** (Stage 3a, Q. 3:134): *ghayẓ* — fluid sealed by *kaẓm*; the verb *kaẓama* originally denotes the *tying-off of a waterskin*, the agent-internal regulation that maintains containment under rising pressure. **Panel 3** (Stage 3b, Q. 67:8): *tamayyuz* — the structural failure; the verb derives from the root *m-y-z* "to separate, to part, to sever", and figures not the exit of pressurised content (as English *explode*) but the *splitting apart of the container itself*. The Qurʾānic instantiation is, on the present argument, more transparent than any English exemplar in Lakoff and Kövecses's (1987) corpus, providing strong cross-linguistic evidence for the cognitive universality of the schema (§5.6).](fig6_metaphor_diagram.pdf){width=100%}


### 5.7. Implications for Qurʾānic translation

Translation criticism of the Qurʾān has long observed that translations level the spectrum—that *ġaḍab* and *ġayẓ* alike become *anger*; that *baghy*, *ṭughyān*, and *ʿutuww* alike become *transgression* (Table 6). Our analysis sharpens this critique by furnishing the reference model against which the levelling can be measured. We propose that critical and study-edition translations adopt distinct equivalents:

> *ḍīq*: inner constriction · *ḥuzn*: persistent grief · *asaf*: regretful dismay (with anger) · *sakhaṭ*: moral disapprobation · *ghaḍab*: anger · *ghayẓ*: contained / boiling rage · *tamayyuz min al-ġayẓ*: bursting from rage · *baghy*: aggressive transgression · *ṭughyān*: rebellious overflow · *ʿutuww*: obstinate defiance.

For pedagogical translations, we further recommend that each lexeme be marked with its position on the continuum—either by inline gloss, by footnote, or by chromatic coding—so that the structural architecture survives the move into the target language.

### 5.8. Implications for Islamic psychology

The continuum offers a culturally-grounded framework that maps onto Gross's model without requiring importation of secular vocabulary. This has three practical implications:

**(i) Prevention.** The continuum supports *early-stage recognition*—the principle, central to cognitive-behavioural therapy, that affective dysregulation should be intercepted at the earliest possible point. The Qurʾānic vocabulary for inner-distress states (*ḍīq*, *ḥuzn*) provides an indigenous lexicon for self-monitoring at Stage 1, in advance of intensification.

**(ii) Crisis intervention.** The *kaẓm* construct, properly understood as a Stage-3 response-modulation strategy, can be integrated with contemporary suppression-and-reappraisal interventions, providing a religiously-grounded framing for techniques that secular CBT already employs.

**(iii) Rehabilitation.** Crucially, the Qurʾānic continuum frames the post-failure Stage 4 as recoverable—the path from *baghy*/*ṭughyān*/*ʿutuww* back toward equilibrium runs through *tawba* (repentance), a return that the text affirms as accessible. This framing offers motivational reinforcement to clinical-psychological rehabilitation models, especially those concerned with anger disorders and post-violent trauma.

These implications are conceptual; their translation into validated clinical interventions awaits the design of empirical studies, which we recommend as a priority for future work.

---

## 6. Conclusion

### 6.1. Substantive contributions

This paper has advanced three contributions to the scholarship.

**Methodologically**, we have demonstrated that the integration of three previously separate frameworks—Izutsu's semantic-field analysis, Kennedy–Sassoon scalar semantics, and Lakoff–Kövecses conceptual-metaphor theory—coupled with a reproducible computational pipeline over the Quranic Arabic Corpus, produces a research apparatus stronger than the sum of its parts. The integration is, to the best of our knowledge, here brought to Qurʾānic studies for the first time. The research apparatus is openly available and applicable to other Qurʾānic semantic fields.

**Descriptively**, we have produced an exhaustive, reproducible concordance of 833 attestations across sixteen roots in the negative-emotion field, with corresponding distributional and network-analytic outputs. The CSV outputs provide a foundation on which further philological and computational work can build.

**Theoretically**, we have formulated and empirically defended the **Qurʾānic Action-Intensity Continuum Hypothesis**: the claim that ten core lexemes of the Qurʾānic negative-emotion field operate as a single graded continuum structured by *intensity of action* and partitioned into four phenomenologically meaningful stages. The hypothesis is supported by qualitative evidence from the classical lexica and tafsīr, and by quantitative evidence from frequency, distribution, morphology, and network structure. We have, in addition, identified two distributional patterns that we have not seen previously reported (the exclusively-Medinan *sakhaṭ*; the exclusively-Meccan *asaf*); proposed the general phenomenon of **discursive-contextual lexical specialisation** of which these are instances; and argued that Q. 67:8 furnishes one of the most articulated linguistic exemplars of "container collapse" in any documented historical text.

### 6.2. Answers to the research questions

**RQ1.** The semantic field is a ten-node network organised around the bridge node *baghy* and the stage-internal hubs *ḥuzn* and *ghaḍab*, with two specialised peripheral nodes (*sakhaṭ*, *ʿutuww*) exhibiting marked distributional asymmetries.

**RQ2.** The ten nodes order on a four-stage continuum—internal distress (Stage 1), explicit anger (Stage 2), explosive rage (Stage 3), behavioural rebellion (Stage 4)—organised by the composite dimension of *intensity of action* (locus, intensity, scope of consequence).

**RQ3.** The empirical distribution corroborates the continuum: chi-squared tests reject the null of stage-uniform distribution and the null of equal Stages 1+2+3 vs Stage 4 split; the network exhibits the predicted bridge structure; and the morphological profile distinguishes the verbal Stage 1 from the more nominal Stage 2.

**RQ4.** The continuum is structurally homologous with Gross's process model, Plutchik's wheel, Spielberger's STAXI, and Lazarus–Scherer appraisal theory in its psychological component, but extends beyond all of them by integrating the post-failure structural-moral consequences of unmanaged emotion (Stage 4).

**RQ5.** Practical implications include three translation recommendations (distinct equivalents, position-marking, structural footnoting) and three Islamic-psychology applications (early-stage prevention, *kaẓm*-grounded crisis intervention, and *tawba*-grounded rehabilitation).

### 6.3. Limitations and future work

Five limitations bound the present study and define its principal future-research extensions.

First, the analysis works at the surface-lexical layer; broader discourse-analytic close-reading of how the spectrum is mobilised across narrative arcs of individual suras remains to be conducted. Second, the *tafsīr* engagement is selective, drawing on four canonical commentaries; a systematic survey of the broader exegetical tradition (especially Shīʿī, Sufi, and contemporary Persian-language commentary) would refine specific lexical readings. Third, the cognitive-linguistic apparatus is Anglophone-dominated; engagement with classical Arabic theories of *bayān* (especially al-Jurjānī's *Dalāʾil al-Iʿjāz*) would supply an indigenous theoretical substrate. Fourth, the *ḥadīth* corpus has not been integrated, although it would be instructive to test whether the continuum is robust beyond the Qurʾānic corpus into the broader Islamic textual tradition. Fifth, the clinical-psychological implications proposed in §5.8 have not been operationalised in empirical interventions; the design of pilot studies for *kaẓm*-grounded emotion regulation training is a priority for translational work.

### 6.4. Closing remark

The Qurʾānic lexicon, on the analysis advanced here, encodes a sophisticated theory of the phenomenology of negative emotion—not as explicit theoretical formulation but as the architectural design of its semantic surface. Recovering that theory requires methodological tools that bring together the qualitative attentiveness of classical philology, the formal precision of contemporary linguistic theory, and the verifiability of corpus-computational analysis. We hope the present study, alongside the foundational work of Izutsu, Qāʾimīniyā, Pakatchi, Narimani et al., and Qarizadeh et al., advances this triple integration. The classical and the computational are not opposed traditions; they are complementary instruments, and their joint deployment opens horizons that neither could disclose alone.

---

## Data and Code Availability

All code, data, concordance CSV outputs, and figure-generation scripts are released open-source at:

> **github.com/ali-kin4/quranic-emotion-spectrum**

The repository contains: (i) the Python pipeline under MIT License; (ii) the Quranic Arabic Corpus (Dukes 2011) under its original GPL; (iii) the complete CSV concordance, distributional summaries, statistical tests, network-centrality outputs, and umbrella-cooccurrence tables; (iv) PDF and PNG versions of the seven figures published with this paper; (v) full text of the Persian and English manuscripts. The complete analysis can be regenerated end-to-end by:

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
