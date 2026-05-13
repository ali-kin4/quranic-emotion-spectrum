# Reviewer 4 (Editorial / NRGS-fit) — NRGS
**Recommendation**: Minor revision
**Confidence**: 4

## Executive summary (~200 words)

The manuscript is a serious, well-structured submission whose intellectual fit for *پژوهش‌های زبان‌شناختیِ قرآن* is unambiguous: it sits squarely in the cognitive-semantics / Iranian-Islamic tradition (Qāʾimī-niā, Pākatchī, Narīmānī, Qāriʾ-zādeh) the journal cultivates, and it cites two recent NRGS-adjacent contributions explicitly. The eight-section structure aligns cleanly with NRGS expectations (مقدمه، پیشینه، چارچوب نظری، روش، یافته‌ها، بحث، نتیجه‌گیری، منابع), heading numbering is in Persian convention, the bilingual abstract pair is present and parallel, and the reference list is cleanly tri-sectioned (Arabic / Persian / English). The cover letter is professional, COPE-compliant on the parallel English JQS submission, and lists four plausible Iranian Qurʾanic-linguistics reviewers.

The most pressing fit issues are: (1) **the manuscript is materially over the 8,000-word ceiling** — body alone is ~9,930 words once tables and figure captions are counted, and the cover letter's "~۸٬۰۸۰ کلمه" figure is therefore incorrect; (2) the sūrah-naming convention "سوره X" is used 24 times but with the bare common-noun pattern (e.g., "سوره مُلک: ۸") rather than the strict "سورۀ مُلک، آیۀ ۸" pattern preferred by NRGS; (3) author block lacks ORCID; (4) ten figures with full captions are heavy for a paper this length and worth pruning. None of these are show-stoppers — hence Minor revision.

## Word count audit

Measured with `wc -w` (counts each token between whitespace as a word, which on Persian markdown overcounts a little because of inline LaTeX such as `\lr{...}`, table-delimiter `|`, and image-link tokens, but undercounts compound `‌`-joined forms; the two errors largely cancel):

| Section | Lines | wc -w |
|---|---|---|
| Persian abstract + keywords (block at ll. 15–19) | 5 | **292** |
| English abstract + keywords (ll. 465–470) | 6 | **306** |
| Persian body (Intro § 1 through `سخنِ پایانی` § 6-3, ll. 23–351) — **includes tables and figure captions** | 329 | **9,933** |
| References block (ll. 354–443) | 90 | 1,556 |
| Cover letter (`cover_letter.md`) | – | 705 |
| Whole `manuscript.md` file | 471 | 12,306 |

**Findings**:
- The cover letter claims "حجمِ متنِ اصلی حدودِ ۸٬۰۸۰ کلمه (در محدوده‌ی مجازِ نشریه)". By any reasonable count the Persian body alone is ~9,930 words, which is **~24% over the 8,000-word ceiling** and **~66% over the 6,000-word target**. The author may be discounting the table contents and the very long figure captions (≈900–1,100 words combined), but NRGS counts both. Recommend trimming to ≤8,000.
- Both abstracts are above the 150–200-word window (292 fa / 306 en). NRGS abstracts are typically tight; please cut by ~30%.
- Trim candidates (in order of expected payoff):
  - § ۲-۲ has *two consecutive paragraphs* on "بازشناسیِ ایرانیِ نظریه‌ی استعاره‌ی مفهومی" (ll. 63 + 65) that restate the same Qāʾimī-niā / Pākatchī / Kövecses-2025 framing — merge into one.
  - § ۴-۵-۲ allots one full paragraph to each of five tafsīrs (Ṭabāṭabāʾī, Zamakhsharī, Ṭabrisī, Ibn ʿĀshūr, Qushayrī) and then a *summary* paragraph (l. 216) that re-lists all four — drop the recap or drop one of the five.
  - § ۴-۸ ("اعتبارسنجیِ پیکره‌ای-محاسباتیِ تکمیلی") is a single ~430-word paragraph reading like a methods appendix; consider relegating to a footnote or moving to the GitHub appendix with a one-line in-body pointer.
  - § ۶-۲ enumerates four future-research vectors (الف / ب / ج / د) over ~1,000 words; NRGS conclusions are normally tighter — collapse to three short bullets.
  - Figure captions average ~120 words each; the ten captions together (~1,100 words) push the count up materially. Captions should arguably be ~50 words for an Esfahan submission.

## خلاصه مقاله

نویسندگان طیفِ خشمِ قرآنیِ شش‌مرحله‌ای را بر بنیادِ پیکره‌ی ریخت‌شناختیِ قرآنیِ دوکس و در گفت‌وگو با میراثِ معناشناسیِ شناختیِ ایرانی-اسلامیِ معاصر (قائمی‌نیا، پاکتچی، نَریمانی، قاری‌زاده) صورت‌بندی می‌کنند و سپس بر اوجِ پیوستار — مرحله‌های ۴ (غضب، حَرد)، ۵ (غیظ، کَظم، تَمَیُّز) و ۶ (بَغی، طُغیان، عُتُوّ) — متمرکز می‌گردند. سهمِ نظریِ محوری، عملیاتی‌سازیِ علّیتِ دوسویه در مرحله‌ی ۶ از رهگذرِ ممیّزیِ تفسیر-بنیادِ ۱۴۵ بسامد است (با کاپای کوهنِ ۰٫۷۹): تنها ۲۶٪ خشم-خاستگاه، ۴۹٪ ساختار-خاستگاه (طمع، استکبار، عُلوّ فی الأرض) و ۲۵٪ ترکیبی. این یافته در امتدادِ تأکیدِ کلاسیکِ المیزان بر «طغیانِ فرعونی به‌منزله‌ی سابقِ خشم بر مغلوبان» قرار می‌گیرد. نویسندگان همچنین نشان می‌دهند که سه‌گانه‌ی غیظ-کَظم-تَمَیُّز چهار گامِ استعاره‌ی *خشم به‌مثابهِ ظرفِ تحتِ فشار* (لیکاف و کوچش ۱۹۸۷) را پیشاپیش عملیاتی ساخته است. تحلیل با ۱۱ شکل، ۲ جدول و چهار تحلیلِ مکمّلِ محاسباتی (تعبیه‌های CAMeLBERT، فاصله‌های ترجمه‌ای MPNet، شبکه‌ی PMI، آزمونِ نُلدِکه‌ای) پشتیبانی می‌شود.

## Major issues

1. **Word-count over-run, mis-declared in the cover letter** — `cover_letter.md` l. 17 states the manuscript is "حدودِ ۸٬۰۸۰ کلمه (در محدوده‌ی مجازِ نشریه)". The Persian body alone is **9,933 words** (Intro through Conclusion, including tables/captions, excluding references and English abstract). This is ~24% over NRGS's 8,000 ceiling and will be flagged at desk-review. Fix: trim per the candidates listed in the word-count audit (target ≤8,000) and correct the cover-letter number, or pre-empt with an explicit overrun justification.

2. **Both abstracts are over length (292 fa / 306 en vs. NRGS's 150–200)** — l. 17 (Persian) and l. 467 (English). Both are also unusually citation-laden ("گراس ۲۰۱۴، ۲۰۱۵"; "Gross's contemporary suppression-and-reappraisal construct"); NRGS abstracts should be self-contained and citation-free. Fix: cut to ~180 words each and remove explicit author-year cites from both abstracts.

3. **Author block lacks ORCID and the corresponding-author email differs between manuscript and cover letter** — manuscript l. 8 gives `kasraghanavati@icloud.com`; cover letter l. 48 gives `k.jabbary@urmia.ac.ir`. NRGS requires the institutional address and an ORCID for each author. Fix: pick one canonical email (preferably the institutional one) and add ORCIDs for both authors below the affiliation block.

4. **Sūrah-naming convention** — the user-memory note `feedback_surah_names.md` mandates "سوره X" (or "سورۀ X") with the proper-noun form throughout. The text uses *24 instances* of "سوره X: آیه" but always in the elided form ("سوره مُلک: ۸", "سوره اسراء: ۲۳", "سوره آل عمران: ۱۳۴"). NRGS preference is the fuller "سورۀ مُلک، آیۀ ۸". This is a system-wide change. Fix: a single find/replace pass to convert "سوره X: N" → "سورۀ X، آیۀ N". Also normalise the inconsistent variant on l. 4 (`سنّتِ تفسیریِ شیعی-سنّی`) — fine — vs. table entries that just say "مُلک: ۸" without "سوره" at all.

5. **Figure 8 is missing** — the caption list jumps `fig1_continuum.pdf`, `fig2_frequency_by_stage.pdf`, `fig3_meccan_medinan.pdf`, `fig4_cooccurrence.pdf`, `fig5_morphology_stack.pdf`, `fig6_metaphor_diagram.pdf`, `fig7_centrality.pdf`, then `fig9_mufassir.jpg`, `fig10_bidirectional.jpg`, `fig11_genealogy.jpg`. There is no `fig8_*` in the manuscript or in `figures_fa/`. Either the numbering reflects a deleted figure (renumber 9→8, 10→9, 11→10) or `fig8` was meant to exist and is missing. Fix: renumber for clean 1-10 sequence.

6. **Only one figure is cross-referenced in body prose** — only "شکلِ ۶" appears in running text (l. 228). The other nine figures float without an in-text "see figure N" anchor. NRGS expects every shamāra-dār figure to have at least one prose referent. Fix: add a short "(نک. شکلِ N)" anchor for each figure at its first conceptual mention (Fig 1 in § ۱-۱ or § ۴-۲; Fig 11 genealogy in § ۱-۲, etc.). Also: Persian Esfahan-style usually places figure number and title *above* the image, not embedded in the caption — verify the pandoc/xelatex rendering meets house style.

## Minor issues

- **`[VERIFY:]` marker in bibliography** — l. 420 (Marcus-Newhall et al. 2025) still contains a literal `[VERIFY: ...]` block warning that the year-string is uncertain. This must be resolved before submission. The in-body cite (l. 190: "نک. \lr{Marcus-Newhall et al. 2025}") commits to a date the bibliography flags as unverified. Recommended fix: replace with Marcus-Newhall et al. (2000), the canonical displaced-aggression meta-analysis, and update the in-body reference.

- **Reference-list alphabetisation is inconsistent in § ج (English)** — entries are not strictly A→Z: `Akra → Albayrak → Alsuhaibani → Anthropic → Gaanoun → Averill → Berkowitz → Derki → Dukes → El-Awa → Frijda → Gross → Izutsu → Kassinove → Khan → Kövecses → Kennedy → Kennedy → Kövecses (1986) → Kövecses (2000) → ...` — Gaanoun is filed under G out of order, two Kövecses-headed clusters are split by a Kennedy cluster, and the Maalej-Marcus-Maalej run on ll. 419–421 is out of order. Fix: re-sort strictly alphabetically by first author surname.

- **Reference-list orthography inconsistency in § الف (Arabic)** — some entries lead with "ال" definite article (`الراغب`, `الزمخشري`, `الطباطبائي`) and others drop it (`ابن فارس`, `ابن کثیر`, `ابن منظور`, `رشید رضا`, `سیّد قطب`). Esfahan house style normally orders Arabic surnames by the *root* (Ṭabāṭabāʾī under Ṭ, Rāghib under R), with the article ignored for alphabetisation. Recommend re-sorting and harmonising.

- **Persian APA-style — page-range presentation** — within § الف entries, volume notation is uniform ("(۸ مجلد)") but in-text citations interleave Arabic and Persian numerals: "ج۴، ص۴۲۸" (l. 180), "ج۲۸، ص۸۴" (l. 178), "ج۱۸، ص۲۸۲" (l. 178), but "ج ۱، ص ۲۰۴–۲۱۲" with spaces (l. 274). Standardise to one style.

- **Cover letter — slight word inflation** — 705 words is on the long side for a Persian submission cover letter (typical: 350–500). Two paragraphs ("سه سهمِ کلیدیِ پژوهش" enumerated as ۱، ۲، ۳, and "جایگاه‌گذاریِ روش‌شناختی") materially overlap and can be merged. The COPE-style parallel-paper disclosure paragraph, by contrast, is well-written and should stay verbatim.

- **No leftover internal cross-references to the English paper** — checked. Good; the user-memory note `feedback_papers_independent.md` is respected. The only "JQS" mention is in the cover letter's COPE-style disclosure (correct location).

- **English abstract — typographical** — l. 467 contains a stray straight double-quote inside the Arabic transliteration ("`"ḥabsu al-ġayẓi fī ṣadrin ḍayyiqin ka-l-ḥabsi al-māʾi fī al-siqāʾ"`") that may not roundtrip through pandoc → xelatex cleanly inside `\begin{LTR}`. Consider replacing with proper LaTeX `\textquotedblleft … \textquotedblright` or English curly quotes.

- **Keywords count** — Persian abstract lists 10 keywords (l. 19), English abstract lists 9 (l. 469). NRGS requires 5–7. Fix: cut to 6 each, ideally aligned 1:1 across the two languages.

- **Cover-letter date in two calendars** — l. 9 gives both the Hijrī-Shamsī and Gregorian forms (۱۹ اردیبهشت ۱۴۰۵ / ۹ مه ۲۰۲۶); good, retain.

- **Tables — captions and source attribution** — Table 1 (l. 105) and Table 2 (l. 130) have Persian captions above the table (correct). Neither carries a source-attribution line ("منبع: یافته‌های پژوهش بر پایه‌ی پیکره‌ی دوکس ۲۰۱۱") below. NRGS prefers an explicit source line even when it is "یافته‌های پژوهش".

- **Heading numbering glitch** — § ۴-۴ heading reads "مرحله ۴" without the connecting kasreh ("مرحله‌ی ۴"); § ۴-۵ heading also reads "مرحله ۵"; § ۴-۶ reads "مرحله‌ی ۶". Make uniform.

- **§ ۴-۸ vs. cover-letter framing** — cover letter touts the JQS paper as having "روش‌شناسیِ محاسباتیِ پیشرفته (آزمونِ جایگشتیِ حافظِ حاشیه‌ها، فاصله‌های اطمینانِ بوت‌استرپی، تصحیحِ هولم-بنفرونی)". § ۴-۲ of the Persian paper *also* reports the permutation test (l. 128), the Holm-Bonferroni correction, and § ۴-۸ adds CAMeLBERT/MPNet/PMI/Nöldeke trend tests. Either the cover letter overstates the methodological gap between the two papers, or § ۴-۸ duplicates JQS material. Pick one framing.

## Editorial polish (formatting, citation style, prose)

- The hyphen-vs-dash usage is mixed: en-dash for ranges ("۸۲–۹۸"), em-dash for parenthetical asides ("— ابن‌فارس در …"). Both used correctly, but a handful of cases use hyphen-minus ("ج۱۸، ص ۲۷۸-۲۸۰") inconsistently with the dominant en-dash. Run one find/replace pass.

- "QAC" / "Quranic Arabic Corpus" / "پیکره‌ی ریخت‌شناختیِ قرآنی" / "پیکره‌ی دوکس" all designate the same object. Define once at first use and stay with one Persian abbreviation.

- Some `\lr{...}` insertions render English words in LTR boxes (e.g., `\lr{ANGER IS BODILY HEAT}`, `\lr{cross-translation semantic drift}`). For NRGS, the convention is *(`English in italics inside parentheses after the Persian gloss`)* rather than naked LTR boxes. Verify the printed pages don't show ragged inline LTR runs.

- The Persian-language URLs ("[github.com/ali-kin4/quranic-emotion-spectrum](…)") in § پیوست are tucked into a markdown link the LaTeX export may break; supply both the bare URL and the markdown link for safety.

- The Anthropic Interpretability Team (2026) reference (l. 393) is a *blog post* / Transformer Circuits thread, not a peer-reviewed publication, and isn't cited in the body of the paper. Either cite it (and explain why a non-peer-reviewed source is doing load-bearing work in an Esfahan submission), or drop it from the bibliography.

- Cover letter — opening salutation is doubled ("جنابِ آقای دکتر محمدرضا حاجی‌اسماعیلی، سردبیرِ محترمِ نشریه‌ی *پژوهش‌های زبان‌شناختیِ قرآن*" in the metadata block + "جنابِ آقای دکتر سردبیرِ محترمِ نشریه‌ی پژوهش‌های زبان‌شناختی قرآن" as the first body line). Pick one. Persian-letter convention is to use a single salutation under the metadata block.

- "گرایشِ مدنی (p = ۰٫۰۰۵)" appears twice in Table 2 (rows for کره and سخط). NRGS readers will want a clarification whether this is the raw or Holm-corrected p; § ۴-۲ (l. 128) clarifies but Table 2 itself does not — add a footnote to the table.

- The phrase "هاپَکسِ قرآنی" appears (correctly) for حَرد and "هاپَکسِ مکّی" for the same root in § ۵-۳ — pick one term and use it consistently.

## Verdict

A strong, NRGS-appropriate paper with a clear methodological signature and a non-trivial empirical claim (bidirectional causation at Stage 6, with κ = 0.79 inter-coder reliability). The contribution is well-positioned against the journal's existing literature (Narīmānī 1400, Qāriʾ-zādeh 1402 are both cited and engaged). The cover letter is solid on COPE/ICMJE disclosure of the parallel JQS paper. **The blockers are entirely cosmetic/structural**: cut to the 8,000-word ceiling, trim both abstracts to ≤200 words, normalise sūrah-naming to "سورۀ X، آیۀ N", resolve the `[VERIFY:]` marker on Marcus-Newhall, renumber the figures to a clean 1–10 sequence, add ORCIDs and a single canonical corresponding-author email, and re-sort the English reference list. With these changes — none requiring substantive scholarly revision — the paper should be ready for desk-acceptance and out-of-house review.
