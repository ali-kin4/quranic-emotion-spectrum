# A Six-Stage Action-Intensity Continuum for Anger in the Qurʾān

## Integrating Izutsu's Semantic-Field Approach, Kennedy–Sassoon Scalar Semantics, and Lakoff–Kövecses Conceptual Metaphor

**Karim Jabbary** *(corresponding author)* — Department of Arabic Language and Literature, Urmia University, Iran. *email:* k.jabbary@urmia.ac.ir.

**Ali Jabbary** — Faculty of Computer Engineering, Urmia University, Iran.

(ORCID identifiers will be provided at submission.)

**Target venue:** *Cognitive Linguistics* (de Gruyter) or *Metaphor and Symbol* (Taylor & Francis). Word target: 9,000 words excluding references.

---

## Abstract

This paper advances a unified cognitive-semantic analysis of the Qurʾānic anger lexicon, arguing that **fourteen** core Arabic roots — **ʾff, krh, ḍyq, ḥzn, ʾsf, nqm, sxṭ, mqt, ġḍb, ḥrd, ġyẓ, bġy, ṭġy, ʿtw** — operate as a single graded semantic field organised by *intensity of action* and partitioned into **six** phenomenological stages: pre-anger displeasure, inner pressure / contraction, evaluative aversion, active anger, compressed/explosive rage, and behavioural outcomes (with caveats). The analysis integrates three frameworks rarely combined in Qurʾānic studies: Izutsu's semantic-field approach for network mapping, Kennedy–Sassoon scalar semantics for intensity ordering, and Lakoff–Kövecses conceptual-metaphor theory for image-schematic structure. The integration is, to the best of our knowledge, here brought to Qurʾānic studies in this combined form for the first time. We support the proposed continuum with four converging lines of evidence: (i) etymological and lexical analysis across four authoritative dictionaries; (ii) tafsīr-based contextual reading across four canonical commentaries; (iii) a corpus-distributional analysis (308+ attestations across the 6,236-verse Qurʾānic corpus) released as an open-source pipeline; and (iv) a network-centrality analysis identifying *baghy* as a principal bridge node between the anger spectrum and the broader moral-evaluation field. We argue that Q. 67:8 (*takādu tamayyazu min al-ġayẓ*) furnishes an *unusually transparent* linguistic instance of the **container-collapse** failure mode of the ANGER IS PRESSURIZED CONTAINER metaphor — the verb *tamayyaza* lexicalising the structural disintegration of the vessel rather than the exit of contents — and that Stage-6 lexemes stand in *bidirectional* causal relation with the anger field rather than being its one-way consequence. We refrain from the stronger comparative claim that Q. 67:8 is the most articulated such instance in the historical record.

**Keywords:** Qurʾān, anger, semantic field, scalar semantics, conceptual metaphor, container collapse, cognitive linguistics, Izutsu, lexical gradation, emotion regulation.

---

## 1. Introduction

### 1.1 Problem and gap

Reflection on Qurʾānic Arabic shows that the lexicon for anger is unusually finely articulated. Single-lexeme studies in both classical lexicography and recent cognitive-semantic work (Qāʾimīniyā 1390/2011, 1393/2014; Pakatchi; Narimani et al. 2021; Qarizadeh et al. 2024) have analysed individual roots — *ġaḍab*, *ġayẓ*, *sakhaṭ*, *ṭughyān* — with philological care. But none has placed the **entire field** on a single graded continuum and tested that ordering against the corpus.

This is the gap. The literature has the lexical microscope but not the structural map. We argue that without the structural map, two methodological pathologies recur:

1. **Translation collapse**: distinct source lexemes (e.g., *ġaḍab*, *ġayẓ*, *sakhaṭ*) collapse into a single English word ("anger"), eroding the field's moral-psychological architecture (Almuhanna et al. 2025).
2. **Tafsīr fragmentation**: each lexeme is read against its own exegetical tradition without confrontation with the *relational* facts of the field — what the lexeme *contrasts* with, what it *escalates from*, what it *de-escalates into*.

Our claim is that the field is in fact graded — that the fourteen roots traverse a six-stage continuum in *intensity of action* — and that this gradient can be argued from converging cognitive-linguistic and corpus-distributional evidence.

### 1.2 Three theoretical lenses

Three frameworks, each independently mature, jointly underwrite the analysis:

- **Izutsu's semantic-field approach** (1959, 1964, 1966) — the *network* dimension. Lexemes are nodes; meaning emerges from relations of substitution, opposition, and association.
- **Scalar semantics in the Kennedy–Sassoon tradition** (Kennedy 2007; Sassoon 2010; Morey 2014) — the *gradation* dimension. Gradable predicates project onto a dimension with an ordering and a unit of measure.
- **Conceptual metaphor theory after Lakoff and Kövecses** (Lakoff & Kövecses 1987; Kövecses 2000, 2010; Maalej 2004) — the *image-schematic* dimension. Embodied source domains (containers, fluids, fire) structure abstract target domains (anger, fear, love).

In Qurʾānic studies, Izutsu's framework has been influential since the 1980s, scalar semantics has been almost untouched, and conceptual metaphor has been applied piecemeal to single lexemes. We argue the three are mutually reinforcing: the network supplies the candidate field, scalar semantics supplies the ordering criterion, and conceptual metaphor supplies the cognitive mechanism for *why* the gradation should exist at all. We are not aware of prior Qurʾānic work that has integrated all three.

### 1.3 The Qurʾānic Action-Intensity Continuum Hypothesis

Our central hypothesis (the **Qurʾānic Action-Intensity Continuum Hypothesis**) is:

> The fourteen roots **ʾff, krh, ḍyq, ḥzn, ʾsf, nqm, sxṭ, mqt, ġḍb, ḥrd, ġyẓ, bġy, ṭġy, ʿtw** form a single graded semantic field in the Qurʾānic Arabic lexicon, ordered along a dimension of *intensity of action* and partitioned into six phenomenologically meaningful stages, with bidirectional rather than strictly unidirectional causation at the behavioural-outcomes pole (Stage 6).

The hypothesis is empirical (testable against the corpus), structural (about field architecture, not single lexemes), and constrained (the Stage-6 caveat addresses a specific philological problem about *baghy*, *ṭughyān*, *ʿutuww*).

---

## 2. Background

### 2.1 Izutsu and Qurʾānic semantic-field analysis

Izutsu's three foundational works — *Structure of the Ethical Terms in the Koran* (1959), *God and Man in the Koran* (1964), *Ethico-Religious Concepts in the Quran* (1966) — established that Qurʾānic key terms (*Allāh*, *īmān*, *kufr*, *ẓulm*, *taqwā*) function as nodes in fields of substitution, opposition, and association. Three notions are central: the *focus word* of a field, the *semantic field* itself, and the *key word* that bridges multiple fields.

Izutsu's method, however, has a known limitation: it identifies *that* lexemes are related but does not formalise *how* they are ordered when the relation is gradable. Strikes of intensity are not captured.

### 2.2 Kennedy–Sassoon scalar semantics

Scalar semantics (Kennedy 1999, 2007; Sassoon 2010; Morey 2014) supplies the missing structure. A gradable predicate projects onto a *scale* with three components:

- A **dimension** (e.g., temperature, length, intensity);
- An **ordering** (e.g., < on the dimension);
- A **unit of measure** (explicit or implicit).

Applying this to anger lexemes: the dimension is intensity-of-action, the ordering is "more intense than", the unit is implicit but recoverable from cognitive-metaphoric and corpus-distributional evidence.

### 2.3 Conceptual metaphor and the container schema

Lakoff and Kövecses (1987) showed that English anger is structured by ANGER IS THE HEAT OF A FLUID IN A PRESSURIZED CONTAINER. The schema generates four expected phases: heating, pressurised containment, controlled release, and *failure modes* — explosion, container collapse. English exemplars typically lexicalise the explosion (*she blew her top*, *he exploded*) but not the structural disintegration. We argue that Q. 67:8 (*takādu tamayyazu min al-ġayẓ*) lexicalises **container collapse** with unusual transparency: *tamayyaza* derives from *m-y-z* (to part, separate, sever) and figures the structural disintegration of the vessel itself. We argue this in §4 against the four authoritative dictionaries and four authoritative tafsīrs.

---

## 3. The continuum: six stages

The proposed six-stage gradient is summarised below. Detailed lexical, etymological, exegetical, and metaphorical analysis follows in §4.

| Stage | Theme | Roots | Headline verse | Image schema |
|------:|-------|-------|---------------:|--------------|
| 1 | Pre-anger displeasure | أُفّ, كره | Q. 17:23 (*ʾuff*) | Sigh / aversion |
| 2 | Inner pressure / contraction | ضيق, حزن, أسف | Q. 15:97 (*ḍāqa ṣadruka*) | Container narrowing |
| 3 | Evaluative aversion | نقم, سخط, مقت | Q. 47:28 (*sakhaṭ Allāh*) | Moral censure |
| 4 | Active anger | غضب, حرد | Q. 48:6 (*ġaḍiba Allāhu ʿalayhim*) | Heated container, lid open |
| 5 | Compressed / explosive rage | غيظ (with *tamayyuz* manifestation) | Q. 3:134 (*kāẓimīna l-ġayẓ*); Q. 67:8 (*takādu tamayyazu min al-ġayẓ*) | Sealed container; container collapse |
| 6 | Behavioural outcomes (bidirectional) | بغي, طغيان, عتوّ | Q. 42:42 (*baghy*); Q. 96:6 (*ṭaghā*); Q. 25:21 (*ʿutuww*) | Eruption into action |

The Stage-6 caveat is critical and developed in §5: these lexemes are not exclusively anger-derived but stand in bidirectional causal relation to the field — anger may produce them, but they also (and more often, on the Qurʾānic record) arise from supremacism, power-seeking, and ethical defiance, and may themselves *generate* anger in their victims and in the divine response.

---

## 4. The container-collapse argument

### 4.1 Q. 67:8 in context

Sūrat al-Mulk verse 8 describes Hell at the moment new occupants are cast into it: *takādu tamayyazu min al-ġayẓ* — "[the fire] is on the verge of *tamayyuz* from rage". Modern translations render the verb variationally: Pickthall ("almost bursts asunder"), Yusuf Ali ("almost bursts with fury"), Saheeh ("almost bursts with rage"), Arberry ("well-nigh bursts asunder").

The verb's morphological route is significant. *Tamayyaza* is the reflexive (*mā-tafaʿʿala*) of *māza/yamīz* (to separate, to sort out, to distinguish). The image is not of pressure escaping through a seal — that would require a verb of efflux (e.g., *ṣabba*, *fāʿa*) — but of the vessel itself coming apart. The five-fold sense network of *m-y-z* (separation, distinction, sorting, severance, partition) makes this a verb of *structural disintegration*, not of contained eruption.

### 4.2 The lexicographic argument

The four authoritative dictionaries we consulted — Ibn Fāris's *Maqāyīs al-Lugha*, Rāghib al-Iṣfahānī's *al-Mufradāt*, Ibn Manẓūr's *Lisān al-ʿArab*, and Muṣṭafawī's *al-Taḥqīq fī Kalimāt al-Qurʾān* — all gloss *m-y-z* in the structural-separation sense. None glosses it as efflux or eruption. The container-collapse reading is therefore not idiosyncratic; it follows directly from the standard etymology.

### 4.3 The tafsīr argument

The four canonical tafsīrs — Ṭabāṭabāʾī's *al-Mīzān*, Zamakhsharī's *al-Kashshāf*, Ṭabrisī's *Majmaʿ al-Bayān*, and Ibn ʿĀshūr's *al-Taḥrīr wa-l-Tanwīr* — each comment on Q. 67:8 with varying philological emphasis but converge on the structural reading of *tamayyuz*. Ibn ʿĀshūr is most explicit: *yatamayyaz baʿḍuhā ʿan baʿḍ*, "its parts come apart from each other", which is precisely the container-collapse image. Zamakhsharī compares the verb to *taqaṭṭuʿ* (rending), which is also a structural verb.

### 4.4 The cross-linguistic comparison

In the Lakoff–Kövecses (1987) corpus of English exemplars, container collapse is *implicit* — readable into the master metaphor — but rarely *lexicalised*. *She blew her top*, *he exploded*, *I lost it*: each is a verb of efflux or scattered explosion, not of vessel-disintegration. Maalej's (2004) Tunisian Arabic corpus likewise centres on heat-and-pressure exemplars without a transparent container-collapse verb. Q. 67:8 is unusual because *tamayyaza* directly lexicalises the disintegration. We claim this provides cross-linguistic evidence — alongside Yu (1995) on Chinese and Kövecses (2000, 2010) on cross-cultural comparison — for the bodily-grounded universality of the schema.

We refrain from the stronger comparative claim that Q. 67:8 is *the* most articulated such instance in any historical text. That would require a systematic survey of pre-modern anger-vessel imagery (Hebrew, Greek, Sanskrit, Chinese, classical Arabic poetry) which has not yet been conducted; we leave that as an explicit open question.

---

## 5. Stage 6 and bidirectional causation

The most reviewer-fragile part of any spectrum analysis is the *behavioural-outcomes pole*. Three Stage-6 roots — *baghy*, *ṭughyān*, *ʿutuww* — were initially presented in our preparatory drafts as "the consequences of unmanaged anger". Reviewer pressure (and our own re-reading) has led us to a more cautious framing.

The lexicographic and exegetical evidence, alongside our corpus-distributional findings, supports a **bidirectional** rather than unidirectional reading:

1. *Baghy* (transgression, illegitimate desire-driven aggression) often arises from *greed* or *supremacism* (*ʿuluww fī al-arḍ*), not from acute anger. Cf. Q. 6:21 (*innahu lā yufliḥu l-ẓālimūn*).
2. *Ṭughyān* (structural defiance, paradigmatically Pharaonic — Q. 79:17, Q. 28:4) is rooted in arrogance and unrestrained power, not in the phenomenology of acute emotional escalation. Q. 26:55 (*innahum lanā lā-ġāʾiẓūn*) is a striking instance of *reverse* polarity: the oppressor's anger arises from the *defiance* of the oppressed, not the other way around.
3. *ʿUtuww* attaches primarily to fixed moral character (*sustained obstinate defiance*) rather than to a transient emotional state.

We retain these three roots in Stage 6 because the corpus places them at the behavioural pole of the spectrum, but the causal arrow is **two-way**: anger may produce these behaviours, but the behaviours can equally produce anger (in their victims, in the prophets confronting them, and in the divine response).

The corpus distributional fact that the phenomenological-core (Stages 1–5, n = 167) and the behavioural-pole (Stage 6, n = 145) are *not* significantly unequal in raw count (χ²(1) = 1.55, fails to reject equal split) is *consistent with* this bidirectional reading. Following standard statistical practice, however, we treat the χ² result as *absence of evidence of asymmetry*, not as positive evidence for the bidirectional architecture itself.

---

## 6. Corpus-distributional support

A full computational pipeline is reported separately (Jabbary & Jabbary 2026, *DSH*); the headline numbers that bear on the present argument are:

- **312 spectrum attestations** across the 6,236-verse Qurʾān, validated against fourteen hand-coded reference verses (14/14 recovered).
- **Six-stage distribution**: (44, 60, 27, 25, 11, 145), χ²(5) = 227.15 against uniformity (p < 0.001).
- **Sakhaṭ exclusively Medinan** (0/4; two-sided exact binomial p = 0.005 against verse-level Meccan baseline 0.74; robust under sensitivity sweep 0.70–0.78).
- **Asaf** exclusively Meccan (5/0) — *suggestive* but not statistically established (exact p = 0.34 at n = 5).
- **Baghy** identified as a principal bridge node by network-centrality analysis (closeness = 0.55, top in spectrum; betweenness = 0.15, tied with *ghaḍab* and *asaf*).
- **Bootstrap CIs** on betweenness preserve *baghy*'s lead but show *ghaḍab*'s bridge role is fragile (CI overlaps zero).

These distributional results corroborate but do not constitute the central philological argument. They function as a triangulating check.

---

## 7. Discussion

### 7.1 Translation implications

The continuum is a reference model for evaluating Qurʾānic translation. Our toy three-translator KL-divergence analysis (in the companion methods paper) shows that the worst translation collapses are around *baghy* (KL > 1.5; "transgression", "oppression", "tyranny", "wrong" used near-interchangeably) and around the ġaḍab/ġayẓ pair (Stage-4/Stage-5 distinction routinely lost). Reformist Qurʾān translation projects could prioritise these high-collapse loci.

### 7.2 Implications for emotion psychology

The Qurʾānic continuum is structurally homologous with Gross's (1998, 2014) process model of emotion regulation, Plutchik's (1980) wheel of intensity, and Spielberger's (1999) State-Trait Anger framework, but extends beyond all three by integrating a structural-behavioural pole (Stage 6) that modern emotion-regulation models do not explicitly map. We do not claim the Qurʾān contains a *theory* of emotion regulation in the modern technical sense; we claim its lexicon *encodes* a phenomenology that modern theory can fruitfully read against.

### 7.3 Limitations

- **Root selection is interpretive judgement**, not a mechanical procedure. Other readers might add *shanaʾa* or treat *ḥard* as too peripheral.
- **Frequency does not directly equal intensity**. Corpus frequency is a proxy for discourse salience; the intensity-ordering claim is supported by lexical-exegetical-metaphorical evidence, with corpus distribution as triangulation.
- **The Meccan/Medinan classification** is at sura-level, glossing transitional suras.
- **The six-stage model is a logical-semantic reconstruction**, not a chronological emotional process. No claim that any individual experiences *ʾuff* before *ġaḍab*.
- **Translation implications need independent empirical evaluation** — the toy KL analysis is suggestive, not definitive.

---

## 8. Conclusion

Three theoretical lenses — Izutsu's semantic-field analysis, Kennedy–Sassoon scalar semantics, and Lakoff–Kövecses conceptual-metaphor theory — when integrated, support a six-stage action-intensity continuum for the Qurʾānic anger lexicon. The integration, in this combined form, has not previously been brought to Qurʾānic studies. Q. 67:8's *tamayyaza* furnishes an unusually transparent linguistic instance of container-collapse. Stage-6 lexemes stand in bidirectional rather than unidirectional causal relation to the field. The continuum supplies a reference model for translation evaluation and a phenomenology that contemporary emotion psychology can read against.

The substantive findings are corroborated by an open, fully reproducible computational pipeline reported separately (Jabbary & Jabbary 2026, *DSH*).

---

## Data and Code Availability

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ali-kin4/quranic-emotion-spectrum/blob/master/notebooks/quranic_emotion_spectrum.ipynb)

Repository: **https://github.com/ali-kin4/quranic-emotion-spectrum**

---

## References

(See full bibliography in the master `references/english.bib`. Key entries: Almuhanna et al. 2025, Dukes 2011, Gross 1998, Ibn Fāris 1404 AH, Ibn Manẓūr 1414 AH, Ibn ʿĀshūr 1984, Izutsu 1959 / 1964 / 1966, Kennedy 2007, Kövecses 2000 / 2010, Lakoff & Kövecses 1987, Maalej 2004, Morey 2014, Narimani et al. 2021, Plutchik 1980, Pakatchi, Qarizadeh et al. 2024, Qāʾimīniyā 1390 / 1393, Rāghib al-Iṣfahānī 1412, Sassoon 2010, Spielberger 1999, Ṭabāṭabāʾī, Ṭabrisī, Tanzil 2008, Yu 1995, Zamakhsharī.)
