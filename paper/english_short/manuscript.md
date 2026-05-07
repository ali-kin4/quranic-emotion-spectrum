# The Phenomenology of the Anger Spectrum in the Qurʾān

## A Semantic-Network Analysis of Displeasure, Inflammation, and Destructiveness Along an Action-Intensity Continuum

**Karim Jabbary** *(corresponding author)*
Department of Arabic Language and Literature, Urmia University, Iran. *email:* k.jabbary@urmia.ac.ir.

**Ali Jabbary**
Faculty of Computer Engineering, Urmia University, Iran. *email:* a.jabbary@urmia.ac.ir.

(ORCID identifiers will be provided at submission.)

**Target word count:** ≤ 9,000 words excluding references (Cognitive Linguistics, de Gruyter; or Journal of Qur'anic Studies, Edinburgh UP).

---

## Abstract  *(≈ 250 words)*

The Qurʾān deploys an unusually articulated lexicon for the description of the anger spectrum, yet existing scholarship has tended to treat this lexicon either word-by-word or through normative-ethical frames, leaving the structural-relational dimension of the field largely unexplored. This study advances the thesis that fourteen core Arabic roots — **ʾff, krh, ḍyq, ḥzn, ʾsf, nqm, sxṭ, mqt, ġḍb, ḥrd, ġyẓ, bġy, ṭġy, ʿtw** — form a single graded semantic field organised along the dimension of *intensity of action*, traversing six phenomenological stages. We integrate three methodological lenses — Izutsu's semantic-field approach, scalar semantics in the Kennedy–Sassoon tradition, and conceptual metaphor theory after Lakoff and Kövecses — and validate the continuum against the **Quranic Arabic Corpus** (Dukes 2011) using a fully reproducible Python pipeline. The empirical analysis covers 312 attestations and finds: (i) the six-stage distribution rejects uniformity at χ²(5) = 227.15 (p < 0.001); (ii) the phenomenological core (Stages 1–5) and the behavioural-outcomes pole (Stage 6) are not significantly unequal (χ²(1) = 1.55), a result we read — *consistent with* but not by itself confirming — as supporting bidirectional causation at Stage 6; (iii) *sakhaṭ* attests exclusively in Medinan suras (0/4; exact binomial p = 0.005, robust under baseline sensitivity); (iv) *baghy* is a principal bridge node between the anger field and the broader moral-evaluation field. We argue that Q. 67:8 (*takādu tamayyazu min al-ġayẓ*) furnishes an unusually transparent linguistic instance of *container collapse* (Lakoff & Kövecses 1987). The findings have implications for Qurʾānic translation, Islamic-psychology intervention design, and the cross-linguistic study of anger lexicons.

**Keywords:** Qurʾān, anger spectrum, semantic field, cognitive linguistics, scalar semantics, conceptual metaphor, anger lexicon, emotion regulation, Arabic corpus linguistics, Izutsu, Islamic psychology.

---

## 1. Introduction

### 1.1 Problem and gap

Qurʾānic Arabic articulates the phenomenology of anger with an unusual lexical density. From minimal verbal displeasure (*ʾuff*, Q. 17:23), through inner contraction (*ḍāqa ṣadruka*, Q. 15:97), evaluative aversion (*sakhaṭ*, Q. 47:28), active anger (*ġaḍab*, Q. 48:6), compressed rage (*ġayẓ*, Q. 3:134), to behavioural transgression (*baghy*, Q. 42:42; *ṭughyān*, Q. 96:6; *ʿutuww*, Q. 25:21), the Qurʾān deploys a lexicon capable of finer distinctions than most modern emotion-regulation taxonomies.

This lexical richness has been studied piecemeal. Single-lexeme work — e.g., Narimani, Iqbali, & Chari's (2021) tafsīr study of *ġayẓ*, *ġaḍab*, and *sakhaṭ*; Qarizadeh et al.'s (2024) polysemy analysis of *ṭughyān* — has produced careful philology for individual roots without articulating a *structural* relation among them. Existing scholarship therefore lacks: (a) a framework integrating the field's *network*, *gradation*, and *image-schematic* dimensions; (b) a reproducible corpus operationalisation; and (c) a coordinated treatment of its translation and psychological implications.

### 1.2 Aims

This paper has three aims. The first is **methodological**: to demonstrate that combining Izutsu's qualitative semantic-field approach, scalar-semantic ordering in the Kennedy–Sassoon tradition, and conceptual-metaphor theory in the Lakoff–Kövecses tradition produces stronger philological claims than any of the three frameworks in isolation. To the best of our knowledge, this trifold integration has not previously been brought together in published Qurʾānic studies. The second aim is **descriptive**: to map every Qurʾānic occurrence of the fourteen core roots and render that map publicly verifiable through an open concordance. The third aim is **interpretive**: to argue that the resulting continuum constitutes a coherent "logic of anger escalation" with structural affinities to modern emotion psychology — and to identify the points where the Qurʾānic continuum *exceeds* contemporary models, particularly at Stage 6.

### 1.3 Hypothesis

The **Qurʾānic Action-Intensity Continuum Hypothesis**: the fourteen roots above form a single graded field, ordered along intensity-of-action, partitioned into six phenomenologically meaningful stages, with bidirectional causation at Stage 6. The hypothesis is empirical, structural, and constrained.

---

## 2. Related work *(compressed)*

Five clusters of prior work bear on this study.

**(a) Single-lexeme studies** — Narimani et al. (2021) on *ġayẓ*/*ġaḍab*/*sakhaṭ* in tafsīr; Qarizadeh et al. (2024) on *ṭughyān* polysemy. Strong philology, no field structure.

**(b) Ethics-of-anger studies** centred on *kaẓm al-ghayẓ* (Q. 3:134). Normatively rich, linguistically thin.

**(c) Cognitive-semantic Qurʾānic work** — Qāʾimīniyā (1390/2011, 1393/2014) introduced cognitive linguistics into Iranian Qurʾānic studies; Pakatchi developed semantic-field methodology. Neither treated the anger field as a graded continuum.

**(d) Translation-criticism studies** — Almuhanna et al. (2025) demonstrated systematic sentiment-leakage in English Qurʾān translations; the multilingual ELQV dataset (*J. King Saud Univ. CIS* 2025) operationalised emotion labels for 2,100 verses. Neither supplies a graded reference model against which translation collapse can be benchmarked.

**(e) Islamic-psychology work** — recent thematic analyses of Qurʾān-and-ḥadīth emotional content (e.g., *Int. J. Counseling and Psychotherapy* 2023, art. 311) draw mainly on ḥadīth and leave Qurʾānic-surface lexical analysis in the background.

The present paper sits at the intersection of all five and supplies, for the first time, a unified framework backed by reproducible corpus evidence.

---

## 3. Theoretical framework

### 3.1 Izutsu — networks

Izutsu (1959, 1964, 1966) showed that Qurʾānic key terms operate as nodes in fields of substitution, opposition, and association. Three notions are central: *focus word*, *semantic field*, *key word*. The method is qualitative and identifies *that* lexemes are related, but does not formalise *how* they are ordered when the relation is gradable.

### 3.2 Kennedy–Sassoon — gradation

Scalar semantics (Kennedy 2007; Sassoon 2010; Morey 2014) supplies the missing structure: a gradable predicate projects onto a *scale* with a dimension, an ordering, and a unit of measure. Applied to the anger lexicon, the dimension is intensity-of-action, the ordering is "more intense than", the unit is implicit but recoverable from cognitive-metaphoric and corpus-distributional evidence.

### 3.3 Lakoff–Kövecses — image schemas

Conceptual metaphor theory (Lakoff & Kövecses 1987; Kövecses 2000, 2010; Maalej 2004 on Tunisian Arabic) shows that anger is structured cross-linguistically by ANGER IS THE HEAT OF A FLUID IN A PRESSURIZED CONTAINER. The schema generates four phases: heating, pressurised containment, controlled release, and *failure modes* (explosion, container collapse). English exemplars typically lexicalise explosion, not collapse. We argue Q. 67:8 lexicalises *collapse* (§4.5).

### 3.4 Why integrate?

The three frameworks are mutually reinforcing. Izutsu maps the field; scalar semantics orders it; conceptual metaphor explains *why* the ordering should exist. The integration is the methodological contribution.

---

## 4. The six-stage continuum

### 4.1 Overview

| Stage | Theme | Roots | Headline |
|------:|-------|-------|---------:|
| 1 | Pre-anger displeasure | أُفّ, كره | Q. 17:23 |
| 2 | Inner pressure / contraction | ضيق, حزن, أسف | Q. 15:97 |
| 3 | Evaluative aversion | نقم, سخط, مقت | Q. 47:28 |
| 4 | Active anger | غضب, حرد | Q. 48:6 |
| 5 | Compressed / explosive rage | غيظ (*tamayyuz* manifestation) | Q. 3:134; Q. 67:8 |
| 6 | Behavioural outcomes (bidirectional) | بغي, طغيان, عتوّ | Q. 42:42; Q. 96:6; Q. 25:21 |

### 4.2 Stages 1–2 (pre-anger, inner pressure)

*ʾUff* (Q. 17:23) is the minimal verbal sign. *Karh* (Q. 2:216) is inner aversion. Stage 2 lexemes — *ḍyq*, *ḥzn*, *ʾsf* — encode *bodily-located* pressure: *ḍāqa ṣadruka* (your chest is constricted, Q. 15:97) is a direct phenomenological marker. The pattern is consistent with embodied-cognition predictions about emotion-as-bodily-event.

### 4.3 Stage 3 (evaluative aversion)

*Naqm* (censure with retributive intent), *sakhaṭ* (severe displeasure, often divine), *maqt* (entrenched moral hatred). Distributionally, *sakhaṭ* attests **exclusively** in Medinan suras (0/4; exact binomial p = 0.005 against the verse-level Meccan baseline of 0.74, robust under sensitivity sweep 0.70–0.78). The pattern is consistent with the Medinan period's institutional framing of community discipline. *Asaf* attests exclusively in Meccan suras (5/0); we report this as a *suggestive* rather than statistically established pattern (exact p = 0.34 at n = 5).

### 4.4 Stage 4 (active anger)

*Ġaḍab* is the focal active-anger lexeme, predicated of God, prophets, and believers. *Ḥard* (Q. 68:25) is a Qurʾānic hapax legomenon: anger with the intent to *withhold*, distinguishing it from *ġaḍab*'s outward direction.

### 4.5 Stage 5 (compressed rage and *tamayyuz* — container collapse)

*Ghayẓ* is sealed-container rage, paradigmatically met with *kaẓm* (restraint) at Q. 3:134. The verb *kaẓama* originally figures sealing a waterskin to prevent overflow.

The exceptional lexeme is *tamayyaza* at Q. 67:8 (*takādu tamayyazu min al-ġayẓ*, "[Hell] is on the verge of *tamayyuz* from rage"). *Tamayyaza* is the reflexive of *māza/yamīz* (to part, separate, sever); its image is not the exit of pressurised contents but the *structural disintegration of the vessel itself*. This is **container collapse** in Lakoff and Kövecses's (1987) sense, lexicalised with unusual transparency. The four authoritative dictionaries (Ibn Fāris's *Maqāyīs*, Rāghib's *Mufradāt*, Ibn Manẓūr's *Lisān*, Muṣṭafawī's *Taḥqīq*) all gloss *m-y-z* in the structural-separation sense; the four canonical tafsīrs (Ṭabāṭabāʾī, Zamakhsharī, Ṭabrisī, Ibn ʿĀshūr) converge on the structural reading.

We refrain from the stronger comparative claim that Q. 67:8 is *the* most articulated such instance in any historical text. That requires a systematic survey of pre-modern anger-vessel imagery (Hebrew, Greek, Sanskrit, Chinese, classical Arabic poetry) which has not yet been conducted. We report it as an *unusually transparent* linguistic instance — strong cross-linguistic evidence for the schema's bodily-grounded universality, alongside Yu (1995) on Chinese and Maalej (2004) on Tunisian Arabic.

### 4.6 Stage 6 and bidirectional causation

The behavioural-outcomes pole — *baghy*, *ṭughyān*, *ʿutuww* — was initially framed in our drafts as "consequences of unmanaged anger". This framing oversimplifies. The lexicographic and exegetical evidence supports a **bidirectional** reading:

1. *Baghy* (illegitimate desire-driven aggression) often arises from greed or supremacism (*ʿuluww fī al-arḍ*), not acute anger.
2. *Ṭughyān* (paradigmatically Pharaonic — Q. 79:17, Q. 28:4) is rooted in arrogance and unrestrained power. Q. 26:55 (*innahum lanā lā-ġāʾiẓūn*) is striking because it *reverses* polarity: the oppressor's anger arises from the oppressed's defiance.
3. *ʿUtuww* attaches to fixed moral character, not transient state.

We retain these roots in Stage 6 because the corpus places them at the behavioural pole, but the causal arrow is two-way.

The corpus distributional fact that the phenomenological core (Stages 1–5 = 167) and the behavioural pole (Stage 6 = 145) are *not* significantly unequal in raw count (χ²(1) = 1.55) is *consistent with* bidirectional causation. Following standard statistical practice, we treat this as *absence of evidence of asymmetry*, not as positive evidence for any specific causal architecture.

---

## 5. Methods *(condensed; full pipeline in companion paper)*

### 5.1 Data and code

Source: Quranic Arabic Corpus v0.4 (Dukes 2011, GPL); Tanzil text in Uthmānī orthography (CC-BY-ND). Python pipeline (MIT-licensed) at: **https://github.com/ali-kin4/quranic-emotion-spectrum**.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ali-kin4/quranic-emotion-spectrum/blob/master/notebooks/quranic_emotion_spectrum.ipynb)

### 5.2 Root selection criteria

Five criteria — three inclusion, two exclusion. *Inclusion*: (i) direct semantic relevance to displeasure/anger/escalation; (ii) Qurʾānic occurrence (hapaxes accepted with rich tafsīr profile); (iii) lexical support in ≥ 3 of 4 standard dictionaries. *Exclusion*: (iv) overly broad moral roots (e.g., *ẓulm*) excluded from spectrum, used only as umbrella terms in robustness; (v) manual contextual validation.

### 5.3 Statistical and network methods

- χ²(5) against six-stage uniformity; χ²(1) against equal-split for core-vs-pole.
- Two-sided **exact binomial** for distributional exclusivity (Meccan-rate baseline = 4,613/6,236 ≈ 0.74).
- **Sparse-count diagnostics**: baseline sensitivity sweep 0.70–0.78; n < 10 evidential flag.
- **Network**: undirected, weighted graph of aya-level co-occurrence; NetworkX 3.x; degree, betweenness, closeness, eigenvector centrality. Bootstrap CIs (B = 1000) for centrality stability.
- The pipeline reimplements binomial PMF, χ², and Wilson–Hilferty fallback to keep dependencies minimal (no scipy/sklearn required at the core).

### 5.4 Validation

Spot-check of fourteen hand-coded reference verses recovered 14/14 correctly. Pipeline is deterministic — identical inputs produce byte-identical outputs.

---

## 6. Results

### 6.1 Six-stage distribution

(44, 60, 27, 25, 11, 145). χ²(5) = 227.15 against uniformity, p < 0.001. Stage 6's prominence (145 of 312 = 46.5 %) and Stage 5's apparent thinness (11) are explained by the bidirectional reading of §4.6.

### 6.2 Stage 1–5 vs Stage 6 (167 vs 145)

χ²(1) = 1.55 against equal split, fails to reject. We interpret this in §4.6.

### 6.3 Distributional patterns

*Sakhaṭ* exclusively Medinan (0/4; p = 0.005); *asaf* exclusively Meccan (5/0; p = 0.34, evidentially weak); *naqm* Meccan-tilted (12/5); *maqt* balanced (4/2); *ḥard* hapax at Q. 68:25 (Meccan); *karh* Medinan-tilted (14/27; p = 0.005).

### 6.4 Network analysis

Closeness: *baghy* leads (0.55, top in spectrum). Betweenness: *baghy*, *ġaḍab*, *asaf* tied at 0.15. *Baghy* is the principal bridge between the anger spectrum and the broader moral-evaluation field (315 attestations of *ẓulm*, 66 of *jurm*, 54 of *fisq*, 106 of *ʿadāwah*).

Bootstrap 95 % CIs (B = 1000) preserve *baghy*'s lead in betweenness; *ġaḍab*'s bridge role is fragile (CI overlaps zero).

### 6.5 Morphological profile

Stages 1–2 are strongly verbal/predicational; Stage 6 is strongly nominal/object-coded. The shift is consistent with the substantive argument that Stages 1–2 are *experienced* states while Stage 6 is *objectified* into structural categories.

---

## 7. Discussion

### 7.1 Translation criticism

The continuum is a reference model for evaluating Qurʾānic translation. A toy three-translator KL-divergence analysis (companion paper, Jabbary & Jabbary 2026) finds the worst translation collapses around *baghy* (KL > 1.5) and at the *ġaḍab*/*ġayẓ* Stage 4 / Stage 5 distinction.

### 7.2 Implications for emotion psychology

Structurally homologous with Gross's process model, Plutchik's wheel, and Spielberger's State-Trait framework, but extends beyond all three by integrating the structural-behavioural pole (Stage 6). We do not claim the Qurʾān contains a *theory* of emotion regulation in the modern technical sense; the lexicon *encodes* a phenomenology that modern theory can read against.

### 7.3 Cross-linguistic universality

Q. 67:8's *tamayyaza* lexicalises container-collapse with unusual transparency, supplementing Yu's (1995) Chinese evidence and Maalej's (2004) Tunisian Arabic evidence for the schema's universality. The stronger comparative-historical claim awaits a systematic pre-modern anger-vessel imagery survey.

### 7.4 Limitations

(1) Root selection is interpretive judgement, not mechanical procedure; alternative root sets are possible. (2) Frequency does not equal intensity — frequency is a discourse-salience proxy, not direct intensity measurement; the intensity-ordering claim rests on lexical, exegetical, and metaphorical evidence with corpus distribution as triangulation. (3) Meccan/Medinan classification is at sura-level, glossing transitional suras. (4) The six-stage model is a logical-semantic reconstruction, not a chronological emotional process. (5) Possible QAC tagging errors (estimated ≤ 2 % from spot-check). (6) Translation implications need full empirical evaluation beyond the toy KL-divergence demonstration.

---

## 8. Conclusion

The Qurʾānic anger lexicon, on the analysis advanced here, encodes a six-stage action-intensity continuum that integrates network structure (Izutsu), scalar gradation (Kennedy–Sassoon), and image-schematic content (Lakoff–Kövecses). The corpus-distributional evidence triangulates the philological argument; Q. 67:8's *tamayyuz* furnishes an unusually transparent linguistic instance of container-collapse; Stage-6 lexemes stand in bidirectional causal relation to the field. The reproducibility apparatus is openly available.

We invite reanalysis under alternative root sets and stage assignments — the Colab notebook makes such re-runs inexpensive and the disagreement productive.

---

## Data and Code Availability

Repository: **https://github.com/ali-kin4/quranic-emotion-spectrum**.

License stack: QAC under GPL (Dukes 2011); Tanzil under CC-BY-ND 3.0; author code under MIT; derived CSVs under GPL by precaution; figures under CC-BY 4.0.

**Conflict of interest and funding.** No conflicts; no specific funding.

**Acknowledgements.** We thank Kais Dukes and the Quranic Arabic Corpus team and the Tanzil Project for their open-corpus contributions. We thank Urmia University for institutional support.

---

## References

(See full bibliography in `references/english.bib`. Key entries below.)

Almuhanna, M., et al. (2025). Sentiment preservation in Quran translation with artificial intelligence approach. *Humanities and Social Sciences Communications*, *12*(1), Article 04181.

Authors. (2025). Leveraging Large Language Models for Detecting and Preserving Emotions in Quran Translations (introducing the ELQV dataset). *Journal of King Saud University — Computer and Information Sciences*, *37*, Article 271.

Dukes, K. (2011). *Quranic Arabic Corpus, Morphology v0.4*. University of Leeds. https://corpus.quran.com.

Gross, J. J. (1998). The emerging field of emotion regulation: An integrative review. *Review of General Psychology*, *2*(3), 271–299.

Gross, J. J. (Ed.). (2014). *Handbook of Emotion Regulation* (2nd ed.). New York: Guilford Press.

Ibn Fāris, A. (1404 AH/1984). *Muʿjam Maqāyīs al-Lugha* (ed. ʿAbd al-Salām Hārūn). Beirut: Dār al-Fikr.

Ibn ʿĀshūr, M. al-Ṭ. (1984). *al-Taḥrīr wa-l-Tanwīr* (30 vols.). Tunis: al-Dār al-Tūnisīya.

Ibn Manẓūr, M. (1414 AH/1993). *Lisān al-ʿArab* (3rd ed., 15 vols.). Beirut: Dār Ṣādir.

Izutsu, T. (1959). *The Structure of the Ethical Terms in the Koran*. Tokyo: Keio University.

Izutsu, T. (1964). *God and Man in the Koran*. Tokyo: Keio University.

Izutsu, T. (1966). *Ethico-Religious Concepts in the Quran*. Montreal: McGill University Press.

Kennedy, C. (2007). Vagueness and grammar: The semantics of relative and absolute gradable adjectives. *Linguistics and Philosophy*, *30*(1), 1–45.

Kövecses, Z. (2000). *Metaphor and Emotion*. Cambridge: Cambridge University Press.

Kövecses, Z. (2010). *Metaphor: A Practical Introduction* (2nd ed.). Oxford: Oxford University Press.

Lakoff, G., & Kövecses, Z. (1987). The cognitive model of anger inherent in American English. In D. Holland & N. Quinn (Eds.), *Cultural Models in Language and Thought* (pp. 195–221). Cambridge University Press.

Maalej, Z. (2004). Figurative language in anger expressions in Tunisian Arabic. *Metaphor and Symbol*, *19*(1), 51–75.

Morey, S. (2014). *Vagueness, Logic and Use*. Manchester: University of Manchester Press.

Narimani, Z., Iqbali, M., & Chari, M. (1400 SH/2021). Semantic re-analysis of *ġayẓ*, *ġaḍab*, and *sakhaṭ* in the Holy Qurʾān: an exegetical approach. *Pizhūhish-hā-yi Qurʾān va Ḥadīth*. [In Persian.]

Plutchik, R. (1980). *Emotion: A Psychoevolutionary Synthesis*. New York: Harper & Row.

Qarizadeh, M. ʿO., Salmani Marvast, M. ʿA., Meymandi, V., & Farsi, B. (1402 SH/2024). Polysemy of *ṭughyān* in the Holy Qurʾān: a linguistic approach. *Pizhūhish-hā-yi Zabānshinākhtī-yi Qurʾān*. [In Persian.]

Qāʾimīniyā, ʿA. (1390 SH/2011). *Maʿnāshināsī-yi Shinākhtī-yi Qurʾān*. Tehran: Pizhūhishgāh-i Farhang va Andīshah-i Islāmī. [In Persian.]

Qāʾimīniyā, ʿA. (1393 SH/2014). *Istiʿārah-hā-yi Mafhūmī wa Faḍāhā-yi Qurʾānī*. Tehran: Pizhūhishgāh-i Farhang va Andīshah-i Islāmī. [In Persian.]

Rāghib al-Iṣfahānī, Ḥ. (1412 AH/1992). *al-Mufradāt fī Gharīb al-Qurʾān* (ed. Ṣafwān Dāwūdī). Damascus: Dār al-Qalam.

Sassoon, G. W. (2010). Measurement theory in linguistics. *Synthese*, *174*(1), 151–180.

Spielberger, C. D. (1999). *State-Trait Anger Expression Inventory-2 (STAXI-2)*. Odessa, FL: Psychological Assessment Resources.

Tanzil Project. (n.d.). *The Tanzil Qurʾān Text* (Uthmani version). https://tanzil.net.

Yu, N. (1995). Metaphorical expressions of anger and happiness in English and Chinese. *Metaphor and Symbolic Activity*, *10*(2), 59–92.
