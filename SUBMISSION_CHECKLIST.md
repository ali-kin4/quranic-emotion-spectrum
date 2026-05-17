# Submission Checklist — *Pizhuhish'hā-yi Zabānshenakhtī-yi Qur'ān*

**Journal:** پژوهش‌های زبان‌شناختیِ قرآن (Journal of Qur'anic Linguistics, NRGS)
**Publisher:** University of Isfahan, Centre for Qur'an and Hadith Research
**Portal:** <https://nrgs.ui.ac.ir>
**Corresponding author:** Karim Jabbary (`k.jabbary@urmia.ac.ir`)
**Manuscript:** `paper/persian/manuscript.md` → `submission/persian/manuscript.{pdf,docx}`
**Cover letter:** `paper/persian/cover_letter.md` → `submission/persian/cover_letter.docx`

This checklist takes the corresponding author from "manuscript is done" → "manuscript is submitted" with zero ambiguity. Tick items left-to-right in any markdown viewer.

> **Scope note.** This file covers the Persian manuscript only. The English companion paper has its own submission flow (target: *Journal of Qur'anic Studies*, EUP) and must not be cross-referenced here per project policy.

---

## A. Manuscript file integrity

Goal: the rendered Persian PDF/DOCX is internally consistent and free of authoring debris.

- [ ] **All in-text figure cross-references resolve** (شکل ۱…۱۰، جدول ۱–۲)
  ```bash
  # From repo root — count figure/table references and image insertions
  grep -oE "شکلِ?\s*۱?[۰-۹]+|fig[0-9]+_[a-z_]+\.pdf" paper/persian/manuscript.md | sort | uniq -c
  grep -oE "جدولِ?\s*۱?[۰-۹]+" paper/persian/manuscript.md | sort | uniq -c
  ```
  Why: NRGS reviewers read figure callouts in order; an orphan «شکلِ ۷» or a missing «جدولِ ۲» will be flagged at first-pass desk review.

- [ ] **All citation parentheticals match a bibliography entry**
  ```bash
  # List inline citations (Persian author-year style, e.g. «(قائمی‌نیا، ۱۳۹۰)»)
  grep -oE "\([^)]*(۱۳۹|۱۴۰|۱۹|۲۰)[۰-۹]{2,3}[^)]*\)" paper/persian/manuscript.md \
      | sort -u > /tmp/citations_in_text.txt
  # Cross-check against the bibliography block at the bottom of the manuscript
  sed -n '/## منابع\|## References\|\\begin{LTR}/,/\\end{LTR}\|englishabstract/p' \
      paper/persian/manuscript.md > /tmp/bibliography.txt
  ```
  Why: NRGS uses APA-7 (Persian-adapted) and rejects manuscripts with dangling citations on a one-shot basis.

- [ ] **بندِ X-Y cross-references all exist** (every «بندِ ۴-۵» must point at a real subheading)
  ```bash
  # Extract referenced section IDs and compare against headings
  grep -oE "بندِ?\s*[۰-۹]+-[۰-۹]+(-[۰-۹]+)?" paper/persian/manuscript.md | sort -u > /tmp/band_refs.txt
  grep -oE "^### [۰-۹]+-[۰-۹]+\.?|^#### [۰-۹]+-[۰-۹]+-[۰-۹]+\.?" paper/persian/manuscript.md > /tmp/band_targets.txt
  diff <(sort -u /tmp/band_refs.txt) <(grep -oE "[۰-۹]+-[۰-۹]+(-[۰-۹]+)?" /tmp/band_targets.txt | sort -u)
  ```
  Why: ~30 internal section cross-refs in the current draft; a single missing «بندِ ۴-۶-۴» reads as carelessness to a Persian reviewer.

- [ ] **No leftover placeholder strings**
  ```bash
  grep -rnE "TBD|XXXX|placeholder|TO BE|CITATION NEEDED|0000-0000-0000-0000" \
      paper/persian/ submission/persian/
  ```
  Expected: zero matches inside Persian artifacts. The English manuscript still carries ORCID placeholders — that is the English flow's problem, not this submission's.

- [ ] **No leftover § symbols** (Western section-mark sneaks in via copy-paste from English drafts)
  ```bash
  grep -n "§" paper/persian/manuscript.md submission/persian/manuscript.pdf 2>/dev/null
  ```
  Why: NRGS Persian house style uses «بند» / «بخش», never «§».

- [ ] **The Persian PDF compiles clean (no overfull `\hbox` on body pages)**
  ```bash
  grep -cE "Overfull \\\\hbox" paper/persian/manuscript.log
  # Inspect each line to confirm it falls in the LTR bibliography block, not in body text
  grep -nE "Overfull \\\\hbox" paper/persian/manuscript.log | head -30
  ```
  Why: 19 overfull-hbox warnings currently exist in `manuscript.log`. NRGS accepts the LTR-bibliography ones (long URLs); body-text overruns must be re-broken.

- [ ] **English abstract page renders with Latin digits and IJMES diacritics**
  Open the last page of `submission/persian/manuscript.pdf` and confirm: (1) digits are `0–9` not `۰–۹`, (2) `ġaḍab`, `ġayẓ`, `kaẓm` carry their diacritics, (3) `\textit{…}` italics did not collapse to upright.
  Why: NRGS requires an English abstract on the closing page for international indexing (ISC, DOAJ).

- [ ] **Persian half-spaces (نیم‌فاصله) are present where required**
  ```bash
  # Spot-check common compounds — should NOT show as space-separated
  grep -cE "می‌|نمی‌|بی‌|پیش‌|هم‌|کم‌" paper/persian/manuscript.md
  ```
  Why: Iranian academic readers parse half-space versus full-space as a literacy signal; missing ZWNJ is the #1 visual disqualifier in the first 30 seconds of editor review.

---

## B. Conformance to journal requirements (NRGS Isfahan)

Goal: every house-style requirement on <https://nrgs.ui.ac.ir/journal/authors.note> is satisfied.

- [ ] **Persian abstract length: 150–250 words** (current: ~198 words per `submission/README.md`)
  ```bash
  # Extract the Persian abstract block and count words
  awk '/^## چکیده/,/^---/' paper/persian/manuscript.md \
      | grep -v '^---\|^##' | wc -w
  ```
  Why: NRGS auto-rejects abstracts outside 150–250 on form validation.

- [ ] **5–7 Persian keywords** (current: 6 — «تفسیرِ تطبیقی؛ طیفِ خشمِ قرآنی؛ استعاره‌ی مفهومی؛ کَظمِ غیظ؛ علّیتِ دوسویه؛ معناشناسیِ شناختیِ قرآنی»)
  ```bash
  grep -A1 "واژگانِ کلیدی" paper/persian/manuscript.md | head -3
  ```
  Why: NRGS requires Persian keywords on the title page; fewer than 5 or more than 7 triggers a back-from-desk request.

- [ ] **English abstract length: 150–250 words** (current: ~206 per `submission/README.md`)
  ```bash
  # Count words in the englishabstract environment in the rendered .tex
  awk '/\\begin{englishabstract}/,/\\end{englishabstract}/' paper/persian/manuscript.tex \
      | wc -w
  ```
  Why: ISC indexing pipeline parses the English abstract block; out-of-range entries are silently dropped from international search.

- [ ] **Persian + English title both present and parallel**
  - Persian: «اوجِ طیفِ خشم در قرآن کریم: قرائتی تطبیقی-تفسیری از مرحله‌های فعّال، متراکم، و پیامدی»
  - English: «The Apex of the Anger Spectrum in the Holy Qur'ān: A Comparative-Exegetical Reading of the Active, Compressed, and Consequential Stages»
  ```bash
  grep -nE "^# |englishabstract|Large.*bfseries" paper/persian/manuscript.md paper/persian/manuscript.tex | head -10
  ```
  Why: NRGS title page must carry both; English title is what shows up in DOAJ / Google Scholar.

- [ ] **Author affiliations include department, faculty, university, city, country** for both authors
  Karim Jabbary — گروه زبان و ادبیات عرب، دانشکده‌ی ادبیات و علوم انسانی، دانشگاه ارومیه، ارومیه، ایران
  Ali Jabbary — گروه مهندسی کامپیوتر، دانشکده‌ی فنی و مهندسی، دانشگاه ارومیه، ارومیه، ایران
  Why: NRGS rejects partial affiliations (e.g. just "Urmia University") on form validation.

- [ ] **Corresponding-author email and ORCID present**
  - Email: `k.jabbary@urmia.ac.ir` (present)
  - ORCID: currently **absent from the Persian manuscript** — must be added before submission
  ```bash
  grep -nE "ORCID|0000-" paper/persian/manuscript.md
  ```
  Why: NRGS now requires ORCID per ICMJE / COPE compliance (mandatory since 1402 ش).

- [ ] **All Qur'anic verse references in the form (سورۀ X: آیه‌ی Y)** (or «سورۀ X: Y»)
  ```bash
  # Find any bare-noun citations — e.g. «بقره ۹۰» without «سورۀ»
  grep -nE "(^|[^ۀ])\b(بقره|آل عمران|نساء|مائده|انعام|اعراف|انفال|توبه|یونس|هود|یوسف|رعد|ابراهیم|حجر|نحل|اسراء|کهف|مریم|طه|انبیاء|حج|مؤمنون|نور|فرقان|شعراء|نمل|قصص|عنکبوت|روم|لقمان|سجده|احزاب|سبأ|فاطر|یس|صافات|ص|زمر|غافر|فصلت|شوری|زخرف|دخان|جاثیه|احقاف|محمد|فتح|حجرات|ق|ذاریات|طور|نجم|قمر|الرحمن|واقعه|حدید|مجادله|حشر|ممتحنه|صف|جمعه|منافقون|تغابن|طلاق|تحریم|ملک|قلم|حاقه|معارج|نوح|جن|مزمل|مدثر|قیامه|انسان|مرسلات|نبأ|نازعات|عبس|تکویر|انفطار|مطففین|انشقاق|بروج|طارق|اعلی|غاشیه|فجر|بلد|شمس|لیل|ضحی|شرح|تین|علق|قدر|بینه|زلزال|عادیات|قارعه|تکاثر|عصر|همزه|فیل|قریش|ماعون|کوثر|کافرون|نصر|مسد|اخلاص|فلق|ناس)\s+[۰-۹]+" paper/persian/manuscript.md | head
  ```
  Why: per project memory `feedback_surah_names.md`, surah names must always appear with the «سورۀ» honorific in this journal; bare nouns read as colloquial.

- [ ] **All hijri-shamsi years marked «ش»; hijri-qamari years marked «ق» where applicable; Gregorian years marked «م» only when ambiguous**
  ```bash
  # Heuristic: find years 1300–1410 (likely shamsi) and confirm each carries " ش"
  grep -oE "۱[۳۴][۰-۹][۰-۹]" paper/persian/manuscript.md | sort -u
  ```
  Why: a 1390 without a "ش" reads as a Gregorian 1390 CE to a careless reader; NRGS reviewers will flag.

- [ ] **Bibliography sorted by Persian/Arabic alphabet for Persian/Arabic sources, by Latin alphabet for English sources**
  ```bash
  # Persian/Arabic block then LTR Latin block — visually confirm sort order
  awk '/## منابع/,/\\begin{LTR}/' paper/persian/manuscript.md | grep -E "^- " | head -20
  awk '/\\begin{LTR}/,/\\end{LTR}/' paper/persian/manuscript.md | grep -E "^- " | head -20
  ```
  Why: NRGS reviewers physically scan the bibliography for order; mis-sorted entries are a copy-edit red flag.

- [ ] **File formats submitted: `.docx` AND `.pdf` together**
  ```bash
  ls -la submission/persian/
  ```
  Expected: `manuscript.pdf`, `manuscript.docx`, `cover_letter.docx` (already present).
  Why: NRGS portal accepts both; reviewers receive the PDF, copy-editors work from the DOCX.

---

## C. Reproducibility appendix

Goal: the public repository and archival snapshot meet open-research expectations.

- [ ] **GitHub URL works**
  ```bash
  # Document the check — actual curl may not run from this harness
  curl -I https://github.com/ali-kin4/quranic-emotion-spectrum
  ```
  Expected: `HTTP/2 200`. Why: NRGS now asks corresponding authors to include a "Data and Code Availability" statement; a 404 here voids the claim.

- [ ] **Zenodo DOI inserted into manuscript and `CITATION.cff`** (currently `10.5281/zenodo.XXXXXXX` placeholder)
  ```bash
  # Verify the placeholder is gone after Zenodo release (see ZENODO.md)
  grep -rn "zenodo.XXXXXXX" CITATION.cff paper/persian/manuscript.md
  ```
  Expected after minting: zero matches. Why: NRGS does not require a DOI, but reviewers cite it as evidence of reproducibility maturity.

- [ ] **Code license is clear: MIT in `LICENSE` file**
  ```bash
  head -3 LICENSE
  ```
  Why: NRGS encourages permissive licensing for accompanying code.

- [ ] **Data licenses are clear for QAC (GPL) and Tanzil (CC-BY-ND-3.0)**
  ```bash
  grep -nE "GPL|CC-BY|دوکس|تنزیل" paper/persian/manuscript.md ZENODO.md | head
  ```
  Why: redistribution constraints (GPL viral, CC-BY-ND no-derivatives) must be honoured downstream.

---

## D. Submission package

Goal: every file the NRGS portal asks for is in `submission/persian/`, named correctly, and opens cleanly.

- [ ] **`manuscript.pdf`** — Persian, ~34 pages, ~1.11 MB
  ```bash
  ls -la submission/persian/manuscript.pdf
  ```

- [ ] **`manuscript.docx`** — Persian, ~1.5 MB (regenerate if `.md` was edited after `2026-05-14`)
  ```bash
  # Pandoc regeneration command — XeLaTeX is the engine of record for the PDF;
  # DOCX uses pandoc's native Word writer. Use the Persian template's reference doc if available.
  cd paper/persian
  pandoc manuscript.md \
      --from=markdown+raw_tex \
      --to=docx \
      --output=manuscript.docx
  cp manuscript.docx ../../submission/persian/manuscript.docx
  ```
  Why: NRGS copy-editors prefer DOCX for typesetting; a stale DOCX (older than the PDF) silently desyncs the final printed page.

- [ ] **`cover_letter.docx`** (currently present; PDF version optional)
  ```bash
  ls -la submission/persian/cover_letter.docx
  # Optional: convert to PDF if portal demands it
  # libreoffice --headless --convert-to pdf submission/persian/cover_letter.docx \
  #     --outdir submission/persian/
  ```

- [ ] **`figures/` and `figures_fa/`** — 300 DPI PNG + vector PDF available for every figure cited
  ```bash
  # Confirm every fig*.pdf cited in the Persian manuscript has a Persian-labelled PDF
  for f in $(grep -oE 'fig[0-9]+_[a-z_]+\.pdf' paper/persian/manuscript.md | sort -u); do
      test -f "figures_fa/$f" && echo "OK  $f" || echo "MISSING figures_fa/$f"
  done
  ```
  Why: NRGS may request the original vector PDFs separately for print-quality typesetting.

- [ ] **`CITATION.cff` present at repo root with valid CFF v1.2.0 schema**
  ```bash
  pip install cffconvert && cffconvert --validate -i CITATION.cff
  ```
  Why: signals to reviewers and to Zenodo that the project ships machine-readable citation metadata.

- [ ] **Anonymised version of the manuscript** — NRGS uses double-blind peer review; an author-stripped copy is required
  ```bash
  # Produce an anonymised copy by stripping author block, affiliations, ORCID,
  # acknowledgements, and "Jabbary" self-citations
  cp paper/persian/manuscript.md /tmp/manuscript_anon.md
  sed -i -E "s/کریم جباری|علی جباری|k\.jabbary@urmia\.ac\.ir|a\.jabbary@urmia\.ac\.ir/[نویسنده]/g" /tmp/manuscript_anon.md
  sed -i -E "/## (تشکر|سپاسگزاری|Acknowledgements)/,/^## /d" /tmp/manuscript_anon.md
  # Re-render
  cd paper/persian
  pandoc /tmp/manuscript_anon.md --template=template.tex --pdf-engine=xelatex \
      -o ../../submission/persian/manuscript_anonymous.pdf --standalone
  ```
  Why: NRGS double-blind verification is enforced at desk-check; un-anonymised submissions are auto-returned.

---

## E. Ethics declarations

Goal: every statement most Iranian journals require under COPE / ICMJE alignment is present in the cover letter (or, where the portal asks, in dedicated form fields).

- [ ] **Conflict-of-interest statement** — explicit "هیچ‌گونه تعارضِ منافع وجود ندارد" in cover letter or end-matter
  Why: NRGS asks for COI on the submission form; absence stalls review.

- [ ] **Funding statement** — if no external funding, declare "این پژوهش از هیچ منبعِ مالیِ بیرونی پشتیبانی نشده است"
  Why: NRGS does not require funding but expects an affirmative statement (positive or null).

- [ ] **Original-work declaration** — confirm the manuscript is not under concurrent review at another Persian-language venue
  Note: the cover letter already discloses the parallel English submission to JQS (COPE-compliant); reconfirm this is acceptable to NRGS, as the two papers are independent and target different language/journal communities.
  Why: NRGS treats parallel-language submission as acceptable when properly disclosed; un-disclosed parallel Persian submission would be misconduct.

- [ ] **IRB / ethics-board statement** — N/A for textual / corpus analysis; state explicitly
  Suggested text: «این پژوهش بر تحلیلِ متنِ منتشرشده‌ی قرآن کریم و پیکره‌های زبانیِ آزاد و عمومی استوار است و نیازی به تأییدِ کمیته‌ی اخلاقیِ پژوهشی ندارد.»
  Why: NRGS asks IRB status on the form; "not applicable" must be affirmative, not blank.

- [ ] **AI-assistance disclosure: NONE** — per project policy in `.claude/projects/.../memory/feedback_no_llm_disclosure.md`
  Why: manuscripts, figures, cover letters, and acknowledgements must never disclose LLM or AI image-gen use. Do not add any "this manuscript was prepared with the assistance of …" sentence.

---

## F. Final visual inspection

Goal: catch what static checks miss. Budget 45 minutes.

- [ ] **Read every page of `submission/persian/manuscript.pdf` on screen**
  - Open at 100% zoom in a PDF reader with RTL support (e.g. Adobe Acrobat, SumatraPDF on Windows, or `mupdf` on Linux).
  - Why: scrolling past the table-heavy pages (جدول ۱، جدول ۲) often reveals overlapped column boundaries that grep won't catch.

- [ ] **Cross-check figure numbers in text against actual compiled order**
  Walk through the PDF and confirm: «شکل ۱» in the text matches the figure that appears first in the PDF, «شکل ۲» the second, etc.
  ```bash
  # Programmatic helper: list figure captions in source order
  grep -nE '!\[' paper/persian/manuscript.md
  ```
  Why: pandoc renumbers figures by source order, but author-supplied callouts like «شکلِ ۱۰» are static — a re-ordering during revision can silently desync.

- [ ] **Confirm no overflowing margins** in body text
  Scroll through pages 1–34; any Persian word that runs into the right margin or any Latin token that runs into the left margin must be re-broken (insert نیم‌فاصله or hyphen).
  Why: NRGS print template is A4 with ~2.5 cm margins; overruns reprint badly.

- [ ] **Confirm all Persian half-spaces (نیم‌فاصله) render correctly**
  Inspect compound words («می‌کند», «بی‌توجهی», «هم‌نشینی») — they must appear with the short connecting space, not as two separated tokens nor as fully concatenated.
  Why: NRGS reviewers will mark this as a copy-edit issue (~3 days added to revision cycle).

- [ ] **Confirm figure resolution is adequate at print size**
  ```bash
  # Spot-check PNG resolution; PDFs are vector so no need to check
  identify figures_fa/fig1_continuum.png figures_fa/fig2_frequency_by_stage.png \
            figures_fa/fig8_mufassir.png figures_fa/fig10_genealogy.png 2>/dev/null
  ```
  Expected: ≥ 300 DPI at the embed size; if PNG, vector PDF is preferred and is what the manuscript actually uses.

---

## G. After submission

Goal: clean handoff, archival, and a paper trail for revision rounds.

- [ ] **Save submission confirmation email** into a project-local archive
  ```bash
  mkdir -p submission/persian/_confirmation
  # Save the NRGS portal acknowledgement as nrgs_ack_YYYY-MM-DD.pdf
  ```
  Why: NRGS sometimes loses portal submission records; the email is the only paper trail.

- [ ] **Tag git release `v1.0.0` and push** (Zenodo will auto-archive — see `ZENODO.md`)
  ```bash
  git tag -a v1.0.0 -m "NRGS Isfahan submission — Persian manuscript v1.0.0"
  git push origin v1.0.0
  ```
  Why: locks an immutable snapshot of code+data corresponding to the submission; reviewer-2 reproducibility checks then target a stable ref.

- [ ] **Record submission date in a project log**
  ```bash
  # Append a one-line entry to a project log
  echo "$(date -I) — Persian manuscript submitted to NRGS (Isfahan), portal id: <ID>" \
      >> submission/SUBMISSION_LOG.md
  ```
  Why: with two parallel papers (NRGS + JQS) in flight, dates blur fast.

- [ ] **Set a 6-week review-reminder** in a calendar of choice
  Why: NRGS first-round decisions typically arrive in 8–12 weeks; if no acknowledgement at week 6, ping the editor politely.

- [ ] **Insert Zenodo DOI into manuscript after minting** (re-tag `v1.0.1`)
  ```bash
  sed -i 's|10.5281/zenodo.XXXXXXX|10.5281/zenodo.<CONCEPT_DOI>|g' CITATION.cff paper/persian/manuscript.md
  git commit -am "Insert Zenodo DOI into Persian manuscript and CITATION.cff"
  git tag -a v1.0.1 -m "DOI inserted into NRGS Persian submission"
  git push origin v1.0.1
  ```
  Why: the v1.0.0 release earns its own version-DOI; the manuscript that cites that DOI must be re-tagged so future readers can resolve.

---

*Last updated: 2026-05-17. Tailored to NRGS Isfahan house style; the JQS-bound English manuscript follows a separate flow.*
