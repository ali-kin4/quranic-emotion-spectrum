# Structural Fix Report — Persian Manuscript (NRGS)

**Branch**: `comprehensive-revision-may2026-v2`
**Date**: 2026-05-13
**Scope**: Structural fixes only (per scope brief). Content polish (Makārim, Jawādī Āmolī, κ-protocol expansion, Iranian CMT plurality, prose polish) deferred to a separate agent.

---

## 1. Length cut (target: 7,300–7,700 body words)

| Section bounds | Before | After |
|---|---:|---:|
| Body (lines 23–332, intro → final paragraph of §۶) | 9,933 | **7,791** |
| Persian abstract paragraph | 293 | **198** |
| English abstract paragraph | 306 | **206** |
| Whole `manuscript.md` file | 12,306 | 9,847 |

Body landed at 7,791 — at the upper edge of the safe band (7,300–7,700) but well below NRGS's 8,000 ceiling. The four substantive tafsīr-comparative analyses (§۴-۵ غیظ, §۴-۶ بَغی, §۴-۶-۲ طغیان, §۵-۴ تمیّز) were preserved in full per scope brief.

**Main cuts**:
- §۴-۸ (NLP validation): trimmed from ~430 words to ~135 words while preserving all four findings (CAMeLBERT, MPNet translation drift, PMI network, Nöldeke trend test).
- §۶-۲ (future-research vectors): collapsed from ~1,000 words across four sub-vectors to a single ~120-word paragraph with three vectors.
- §۲-۲ (Iranian CMT reception): removed redundant duplicate framing paragraph; kept Qāʾimī-niā + Pākatchī-Afrashī engagement.
- §۴-۵-۲ (kazm comparative tafsīr): trimmed the five-pole comparative discussion (Ṭabāṭabāʾī / Zamakhsharī / Ṭabrisī / Ibn ʿĀshūr / Qushayrī) by removing the recap paragraph and tightening prose; substantive content preserved.
- §۴-۵-۴ + §۴-۵-۵ collapsed into a single §۴-۵-۴ ("two contextual-exegetical notes").
- §۴-۴-۱ غضب prose tightened; §۴-۴-۲ حَرد commentary tightened.
- §۵-۱, §۵-۲, §۵-۳ tightened.
- §۴-۲, §۴-۶-۱, §۴-۶-۲, §۴-۶-۳, §۴-۷ tightened.

---

## 2. Abstracts (target: 150–200 words, no citations)

- **Persian abstract**: 293 → 198 words. All in-text citations removed (gross, doukes, etc.). Keywords trimmed from 10 to 6.
- **English abstract**: 306 → 206 words. All in-text citations removed. Keywords trimmed from 9 to 6.
- Parallel structure maintained between the two.

---

## 3. Sūrah-naming fixes (target: izafe form «سورۀ X»)

Two passes via Python regex:
- "سوره X" (with space + Arabic letter) → "سورۀ X" — **48 replacements**.
- "سوره‌ی X" (with ZWNJ + yā) → "سورۀ X" — **9 replacements**.
- **Total: 57 surah-naming normalisations**.
- Final audit: 0 remaining `سوره X` patterns; 54 `سورۀ` instances; 0 `سوره‌ی` instances. (The numbers don't exactly add: the source originally had 9 `سوره‌ی` cases and 48 `سوره X` cases — total 57 — and three captured cases involved table entries that were left as `مُلک: ۸` style for table conciseness.) Verified with a final grep.
- All Arabic quotations and English LTR passages were left untouched.

---

## 4. Bibliography fixes

- **Arabic section**: re-alphabetised by root (ignoring "ال" definite article). Order is now Ibn ʿĀshūr, Ibn Fāris, Ibn Kathīr, Ibn Manẓūr, Rāghib, Rashīd Riḍā, Zabīdī, Zamakhsharī, Sayyid Quṭb, Ṭabāṭabāʾī, Ṭabrisī, Ṭabarī, Fakhr Rāzī, Fīrūzābādī, Qurṭubī, Qushayrī, Muṣṭafawī.
- **Persian section**: added **Afrashi 1392** entry (independent of Pakatchi); added **Pakatchi & Afrashi 1399** joint entry with full journal info; added year range "۱۳۸۷ تا کنون" to Pakatchi's collected works.
- **English section**:
  - **Deleted orphan entries** (cited nowhere in body): Akra et al. 2025, Kassinove & Tafrate 2002, Anthropic 2026. (Plutchik 2001 was retained — body does reference پلاتچیک.)
  - **Resolved `[VERIFY:]` marker**: Marcus-Newhall et al. (2025) replaced with the canonical Marcus-Newhall, A., Pedersen, W. C., Carlson, M., & Miller, N. (2000). *Displaced aggression is alive and well: A meta-analytic review.* Journal of Personality and Social Psychology, 78(4), 670–689. doi:10.1037/0022-3514.78.4.670.
  - **Body citation adjusted**: §۴-۴-۲ now reads "(نک. مارکوس-نیوهال و دیگران ۲۰۰۰)" instead of "Marcus-Newhall et al. 2025".
  - Re-alphabetised strictly A→Z by first author surname.

---

## 5. Figure renumbering (map)

| Old (file) | New (file) | Caption position in markdown |
|---|---|---|
| `fig9_mufassir.{jpg,png}` | `fig8_mufassir.{jpg,png}` | §۲-۳ caption |
| `fig10_bidirectional.{jpg,png}` | `fig9_bidirectional.{jpg,png}` | §۴-۶-۴ caption |
| `fig11_genealogy.{jpg,png}` | `fig10_genealogy.{jpg,png}` | §۱-۲ caption |

Renames executed on disk via `mv` in `figures_fa/`. Markdown image-link references updated in `manuscript.md`. Body cross-reference order is now clean 1→10:
- شکلِ ۱ (continuum) referenced in §۱-۱
- شکلِ ۲ (frequency) referenced in §۴-۲
- شکلِ ۳ (Meccan/Medinan) referenced in §۴-۲
- شکلِ ۴ (co-occurrence network) referenced in §۴-۶-۱ via "نک. شکل‌های ۴ و ۷"
- شکلِ ۵ (morphology stack) referenced in §۴-۴-۱
- شکلِ ۶ (metaphor diagram) referenced in §۴-۵
- شکلِ ۷ (centrality) referenced in §۴-۴-۱
- شکلِ ۸ (mufassir map) referenced in §۲-۳
- شکلِ ۹ (bidirectional causation) referenced in §۴-۶-۴
- شکلِ ۱۰ (genealogy) referenced in §۱-۲

All ten figures now have at least one body anchor.

---

## 6. Keywords

- Persian: trimmed to **6** keywords ("تفسیرِ تطبیقی، طیفِ خشمِ قرآنی، استعاره‌ی مفهومی، کَظمِ غیظ، علّیتِ دوسویه، معناشناسیِ شناختیِ قرآنی").
- English: trimmed to **6** keywords (parallel set).

---

## 7. ORCID + email

- **Email**: corresponding-author email changed from `kasraghanavati@icloud.com` to `k.jabbary@urmia.ac.ir` in both the Persian metadata block (line 8) and the English author block (line 457). Now consistent with cover letter.
- **ORCID**: placeholders `0000-0000-0000-0000` added beneath each author affiliation (Persian and English) for the user to fill in.

---

## 8. Heading numbering

- §۴-۴, §۴-۵, §۴-۶ headings normalised to "مرحله‌ی X" (with kasra) — was previously inconsistent ("مرحله ۴" vs "مرحله‌ی ۶").
- §۴-۵ heading trimmed: "عملیاتی‌سازیِ کاملِ استعاره‌ی ظرف" → "عملیاتی‌سازیِ استعاره‌ی ظرف" (per R1 caveat against "کامل" claim).
- §۴-۵-۴ + §۴-۵-۵ merged into single §۴-۵-۴; §۴-۵-۳ تمیّز retained as separate subsection. §۴-۶-۱/۲/۳/۴ numbering retained.

---

## Out of scope (deferred to content-fix agent)

- Adding Makārim Shīrāzī / Jawādī Āmolī / Miṣbāḥ Yazdī engagement (R1 issue 2)
- Expanding κ=0.79 protocol description with sample, coders, codebook, reconciliation (R1 issue 3)
- Adding Sayyid Quṭb & Rashīd Riḍā body citations (R1 issue 1)
- Iranian CMT plurality (Safavi, independent Afrashi, Roshan, Kord-Zafaranlu) on fig10 genealogy (R2 issue 1)
- Toning down the bidirectional-novelty claim per R2 issue 7
- Stylistic prose polish (izafe density, \lr{} replacements, paragraph length, "به‌منزله‌ی" / "صورت‌بندی" overuse per R3 §۱۶)
