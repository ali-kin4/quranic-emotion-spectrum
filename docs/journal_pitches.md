# Per-journal pitch memos

This document maps the four available manuscript versions to four candidate journals, with a short pitch and a length / fit check for each.

| Manuscript | Path | Words (current) | Best venue (primary) | Best venue (backup) |
|---|---|---:|---|---|
| English short (combined) | `paper/english_short/manuscript.md` | ~3,000 (under-budget; expand to 8,500–9,000 before submission) | Cognitive Linguistics | Journal of Qur'anic Studies |
| English methods/computational | `paper/papers_split/methods/manuscript.md` | ~3,000 (under-budget; expand to 8,500–9,000) | Digital Scholarship in the Humanities | Corpus Linguistics and Linguistic Theory |
| English theory/conceptual | `paper/papers_split/theory/manuscript.md` | ~2,700 (under-budget; expand to 8,500–9,000) | Cognitive Linguistics | Metaphor and Symbol |
| Persian short | `paper/persian_short/manuscript.md` | ~2,500 Persian words | فصلنامه پژوهش‌های قرآن و حدیث (دانشگاه تهران) | پژوهش‌های زبان‌شناختی قرآن (دانشگاه اصفهان) |
| English long (current TeX) | `paper/english/manuscript.tex` | ~12,000+ | (split as above; do not submit as-is) | — |
| Persian long (current TeX) | `paper/persian/manuscript.tex` | 51 pp Persian | فقط در صورتی که مجله سقف صفحاتش بالاست | — |

> **All three English short manuscripts are presently below their target lengths** (≈ 3 K words vs the 9 K target). Before submission, each needs expansion through (a) more detailed lexical/exegetical case studies in §4, (b) more substantive engagement with the secondary literature in §2, and (c) longer methods/results sections.

---

## Pitch 1 — *Cognitive Linguistics* (de Gruyter)

**Submit:** `paper/papers_split/theory/manuscript.md` (after expansion).

**Why this venue:** Cognitive Linguistics is the flagship for cognitive-semantic theory; integrates Lakoff/Kövecses, Kennedy/Sassoon, and field-semantic traditions. Reviewers will value the metaphor-theoretic argument (container collapse) and the methodological integration claim.

**Length target:** 8,000–10,000 words (research article). Current draft ≈ 2,700 → expand to ≈ 9,000.

**Strategic positioning:**
- Lead with the **trifold integration** as the methodological contribution.
- Q. 67:8's *tamayyaza* as the clearest hook — a pre-modern lexicalisation of *container collapse*, lexicalising structural disintegration rather than efflux.
- Frame the corpus-distributional results as **triangulating evidence**, not the central claim. Cognitive Linguistics' reviewers respond to philological argument first, statistics second.
- Restate the originality claim cautiously: "*to the best of our knowledge*", not "first ever".
- Defer the bidirectional Stage-6 caveat to §5 — don't lead with it, but don't bury it either.

**Likely reviewer concerns and pre-emptive responses:**
- *Why these fourteen roots?* — §3.2 documents the five inclusion/exclusion criteria; the alternative-root-set robustness check in the notebook is mentioned in §6.
- *Stage assignment is interpretive, not mechanical.* — Acknowledge in limitations; note the LLM-as-coder validation cell is a stress-test (§6).
- *Stage 6 lexemes are not anger consequences.* — Pre-empt this in §4.6 with the bidirectional reading.
- *Cross-linguistic generalisation?* — Cite Maalej 2004 (Tunisian Arabic) and Yu 1995 (Chinese); refrain from the strongest comparative-historical claim.

**Companion paper note in cover letter:** "A companion methods paper presenting the open-source pipeline, statistical-diagnostic protocol, and reproducible Colab notebook is in submission to *Digital Scholarship in the Humanities*."

---

## Pitch 2 — *Digital Scholarship in the Humanities* (Oxford)

**Submit:** `paper/papers_split/methods/manuscript.md` (after expansion).

**Why this venue:** DSH publishes methods-and-artifact papers with strong reproducibility infrastructure. Open code, open data, deterministic pipeline, and the LLM-validation protocol are all central to DSH's editorial profile.

**Length target:** ≤ 9,000 words full paper (or ≤ 5,000 short paper). Current draft ≈ 3,000 → expand toward 8,000–8,500.

**Strategic positioning:**
- Lead with the **artifact**: open Colab notebook, deterministic pipeline, validated reproducibility, license stack.
- Three methodological contributions: sparse-count diagnostics, LLM-as-coder validation (Cohen's κ), KL-divergence translation criticism.
- Treat the Qurʾānic-anger findings as a **worked example**, not the central contribution.
- Highlight cross-corpus extensibility (Hebrew Bible via Sefaria) as evidence the pipeline generalises.

**Likely reviewer concerns:**
- *What's novel beyond a concordance?* — The three diagnostic additions, the validated reproducibility, the cross-corpus check.
- *Is the pipeline genuinely usable by others?* — One-click Colab badge; SHA-verification; pinned environment; commit-and-push step.
- *LLM-as-coder is not yet established methodology.* — Frame it as a tractable inter-annotator-agreement protocol; cite Landis & Koch 1977 for κ; acknowledge it as complement, not replacement, of expert philology.

**Companion paper note:** "A companion theoretical paper presenting the philological argument and the cognitive-semantic analysis of Q. 67:8 is in submission to *Cognitive Linguistics*."

---

## Pitch 3 — *Metaphor and Symbol* (Taylor & Francis)

**Submit:** Modified version of `paper/papers_split/theory/manuscript.md` — re-cut to lead with the container-collapse argument.

**Why this venue:** Strong fit for the Q. 67:8 metaphor analysis specifically. Reviewers will engage with the Lakoff-Kövecses framing and care about cross-linguistic evidence (Yu 1995, Maalej 2004).

**Length target:** ≈ 8,000 words (APA-style; consult journal page for current figures).

**Strategic positioning:**
- Lead with **container collapse as a cross-linguistic universal** and use Q. 67:8 as the exemplar.
- Restructure §4 so the *tamayyuz* analysis is the spine, with the six-stage continuum as supporting context.
- The Izutsu/Kennedy framework can be condensed to a single section.

**Likely reviewer concerns:**
- *Is "container collapse" really distinct from "explosion"?* — §4.5 argues the lexical-morphological evidence (*m-y-z* root) is decisive.
- *Single-verse argument is thin.* — Reinforce with Hebrew/Greek/Sanskrit/Chinese comparisons (some preliminary; full survey deferred to future work).

---

## Pitch 4 — *Journal of Qur'anic Studies* (Edinburgh University Press)

**Submit:** Modified version of `paper/english_short/manuscript.md` — re-cut to lead with the philological/Qurʾānic-studies framing rather than cognitive linguistics.

**Why this venue:** JQS is the leading English-language venue for Qurʾānic studies. The audience is philologists and Islamicists, not cognitive linguists. The reproducibility infrastructure becomes a secondary asset; the primary asset is the **integrated philological argument** for the six-stage continuum.

**Length target:** typically 8,000–12,000 words (specific cap not posted publicly; consult editor).

**Strategic positioning:**
- Lead with the **lexical-tafsīr argument**: dictionary entries from the four authoritative lexica, tafsīr readings from the four canonical commentaries.
- The corpus pipeline appears as an **operationalisation aid**, not the methodological centrepiece.
- Pair the analysis with substantial engagement with the Persian-language secondary literature (Qāʾimīniyā, Pakatchi, Narimani et al., Qarizadeh et al.) — JQS readers will recognise these.
- Discuss the translation-criticism implications carefully and concretely.

**Likely reviewer concerns:**
- *This is corpus linguistics dressed up as Qurʾānic studies.* — Re-balance the prose to make tafsīr and lexicography primary; pipeline secondary.
- *The Stage 6 bidirectional caveat seems ad hoc.* — Defend with explicit Q. 26:55 analysis and historical-linguistic argument about *ʿuluww fī al-arḍ*.
- *Why include hapaxes?* — *Ḥard* (Q. 68:25) has rich tafsīr profile; defend in §3.2.

---

## Pitch 5 — *پژوهش‌های قرآن و حدیث* (Persian-language; University of Tehran) or similar

**Submit:** `paper/persian_short/manuscript.md` (after expansion to ≈ 8,000–10,000 Persian words).

**Why this venue:** Persian Qurʾānic-studies journals are typically more flexible on length (some accept 50–60 pp), but the short version is what reviewers will most welcome. The Persian audience already knows Izutsu, Qāʾimīniyā, and Pakatchi; the integration claim and the corpus pipeline are the novel hooks.

**Strategic positioning:**
- Foreground the **Iranian secondary literature** (Qāʾimīniyā 1390/1393, Pakatchi, Narimani et al. 1400, Qarizadeh et al. 1402).
- Render technical terms with both Persian and English (e.g., "معناشناسی طیفی \lr{(Scalar Semantics)}").
- Keep the open-source notebook as a prominent asset — Iranian Qurʾānic-studies journals are increasingly receptive to digital-humanities infrastructure.

---

## Submission strategy: parallel vs sequential

**Recommended sequence (parallel):**

1. **Today (concept-finalisation):** Authors review the three English short manuscripts and choose either Strategy A (split into two papers; submit Methods to DSH and Theory to Cognitive Linguistics in parallel) or Strategy B (single combined paper; submit to Cognitive Linguistics or JQS).
2. **Week 1–2:** Expand chosen manuscript(s) from 3 K → 9 K words. The notebook outputs (bootstrap CIs, KL divergences, LLM kappa, embedding plots) supply ~1,500–2,000 words of new methods-and-results content per paper.
3. **Week 3:** Final round of internal review, polish English/Persian prose. Compile to PDF.
4. **Week 4:** Submit. If parallel split, mention the companion paper in each cover letter.

**Persian submission:** parallel to the English strategy. The Persian short can be submitted to a Persian Qurʾānic-studies journal once expanded to 8 K Persian words.

---

## What needs author judgement (not the agent's call)

- **Choice between Strategy A (two papers) and Strategy B (one paper).** Two papers gets you greater publication velocity and more visibility, at the cost of more writing. One paper is faster but less impactful.
- **Whether to add the cross-corpus Hebrew Bible analysis to the Methods paper.** It strengthens the artifact contribution but requires author engagement with biblical Hebrew.
- **Whether to submit the Persian short to an Iranian journal first or after the English version is published.** Some Iranian journals welcome translations of already-published international work; others prefer original Persian-language submissions.
- **Whether to invite a third author** (e.g., a senior Qurʾānic-studies scholar at Urmia or another Iranian university) for the JQS submission — this can substantially improve acceptance odds for a more conservative venue.
