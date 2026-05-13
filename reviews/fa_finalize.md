# Final Submission-Prep Report — Persian Manuscript (NRGS)

**Branch**: `comprehensive-revision-may2026-v2`
**Date**: 2026-05-13 (۱۹ اردیبهشت ۱۴۰۵)
**Scope**: Cover-letter update, .tex/.docx regeneration, final QC sweep.

---

## 1. Final body word count

| Section | Words |
|---|---:|
| Body (lines 23–340; intro → final paragraph of §۶) | **7,890** |
| Persian abstract (line 19) | 198 |
| English abstract | 206 |
| Full `manuscript.md` (incl. metadata, bibliography, English mirror, appendix) | 10,009 |

Body is within NRGS safe band (6,000–8,000; the structural-fix agent's narrower 7,300–7,900 target band is also satisfied).

---

## 2. QC grep results (final, across `paper/persian/manuscript.md` and `paper/persian/cover_letter.md`)

| Pattern | Matches | Notes |
|---|---:|---|
| `ChatGPT`, `Claude`, `Anthropic`, `OpenAI`, `GPT`, `LLM`, `DALL-E`, `Midjourney`, `image gen` (case-insensitive) | **0** | Clean. (Earlier-run hits in stale `manuscript.tex`/`manuscript_body.tex` were eliminated by the .tex regeneration in §4.) |
| `هوش مصنوعی`, `مدل زبانی`, `تولیدشده توسط`, `تهیه‌شده با کمک` | **0** | Clean. |
| `[VERIFY:` | **0** | Clean (R1-flagged Marcus-Newhall citation was resolved by the content-fix agent). |
| `[Author`, `[Department]` | **0** | Clean. |
| `0000-0000-0000-0000` | **4** | Intentional ORCID placeholders (2 in Persian metadata block, 2 in English mirror author block) per structural-fix report §7 — author fills locally. |
| `TODO`, `FIXME`, `XXX`, `PLACEHOLDER` | **0** | Clean. |
| `نسخه‌ی انگلیسی`, `مقاله‌ی انگلیسی`, `JQS`, `Journal of Qur'anic Studies` in **manuscript.md** | **0** | Clean — no cross-references to the English paper in the body. |
| `JQS` in **cover_letter.md** | **1** | Single mention in the parallel-publication-disclosure paragraph, as instructed. |
| Bare `سوره X` (without izafe) | **0** | Sura references use «سورۀ X» throughout (29 izafe instances). The one `سوره` match in the bibliography (`صفوی ۱۳۸۲ ... سوره‌ی مهر`) is the publisher name, not a sura citation. |
| Figure refs resolve to real files in `figures_fa/` | **10 / 10** | fig1–fig10 all present (.pdf/.png/.jpg variants as noted in markdown). |

---

## 3. .docx regeneration

- File: `paper/persian/manuscript.docx`
- Command: `pandoc /tmp/manuscript_persian_pp.md --resource-path="C:/Users/.../figures_fa;C:/Users/.../quranic-emotion-spectrum" -o paper/persian/manuscript.docx`
- Preprocessing: piped through `sed -E 's/\(fig([0-9]+)_([a-z_0-9]+)\.pdf\)/(fig\1_\2.png)/g'` so pandoc can resolve image extensions.
- Size: **1,569,478 bytes** (~1.5 MB). Non-empty, with embedded figures (no "Could not fetch resource" warnings after `--resource-path` flag was set).

---

## 4. .tex regeneration

| File | Size | Command |
|---|---:|---|
| `paper/persian/manuscript.tex` (standalone) | 122,346 bytes | `pandoc /tmp/manuscript_persian_pp.md --template=paper/persian/template.tex --standalone -o paper/persian/manuscript.tex` |
| `paper/persian/manuscript_body.tex` (body-only) | 118,686 bytes | `pandoc /tmp/manuscript_persian_pp.md -o paper/persian/manuscript_body.tex` |

Both generated without warnings (pandoc 3.5 on Windows). Standalone uses the hand-maintained `template.tex` (xepersian, Vazirmatn + Amiri + EB Garamond, relative `Path = ../fonts/`). Per CLAUDE.md, **XeLaTeX was not run** — the user compiles locally with MiKTeX 25.4.

All 10 `\includegraphics{...}` calls in the regenerated `manuscript.tex` resolve to real files in `figures_fa/`:
- `fig1_continuum.png`, `fig2_frequency_by_stage.png`, `fig3_meccan_medinan.png`, `fig4_cooccurrence.png`, `fig5_morphology_stack.png`, `fig6_metaphor_diagram.png`, `fig7_centrality.png` (PDFs converted to PNG by preprocessor)
- `fig8_mufassir.jpg`, `fig9_bidirectional.jpg`, `fig10_genealogy.jpg` (originals)

---

## 5. Cover letter changes summary

File: `paper/persian/cover_letter.md`

**Single substantive edit**:
- Line 17: «با حجمِ متنِ اصلی حدودِ **۸٬۰۸۰** کلمه» → «با حجمِ متنِ اصلی حدودِ **۷٬۸۹۰** کلمه». Aligns with the actual post-content-polish body word count.

**Items verified, no change needed**:

- **Article title** matches `manuscript.md` line 3 verbatim: «اوجِ طیفِ خشم در قرآن کریم: قرائتی تطبیقی-تفسیری از مرحله‌های فعّال، متراکم، و پیامدی».
- **Subtitle** matches `manuscript.md` line 4 verbatim: «بازخوانیِ غضب، غیظ، بَغی، طغیان و عتوّ در پرتوِ سنّتِ تفسیریِ شیعی-سنّی و میراثِ معناشناسیِ شناختیِ ایرانی-اسلامی».
- **Parallel-publication-disclosure paragraph** (line 31) reads truthfully: explicitly states the two papers «آثاری مستقل‌اند که تنها در پشتوانه‌ی داده‌ایِ پیکره‌ای (QAC نسخه‌ی ۰٫۴، دوکس ۲۰۱۱) و خط‌لوله‌ی تحلیلیِ بازتولیدپذیر اشتراک دارند؛ به یکدیگر ارجاع نمی‌دهند و هیچ هم‌پوشانیِ محتوایی فراتر از این پایه‌ی مشترک ندارند». COPE/ICMJE compliance is named.
- **Suggested reviewers** (lines 35–38): four named, appropriate Iranian Qur'anic-linguistics scholars — Qāʾimī-niā (پژوهشگاهِ فرهنگ و اندیشه‌ی اسلامی), Pākatchī (دانشگاه امام صادق), Afrashī (پژوهشگاهِ علومِ انسانی), Rezāʾī Eṣfahānī (جامعة المصطفی).
- **Date** (line 9): ۱۹ اردیبهشت ۱۴۰۵ (۹ مه ۲۰۲۶) — matches the manuscript submission date per branch context.
- **Author affiliations and emails** (lines 47–48): «گروهِ زبان و ادبیاتِ عرب، دانشکده‌ی ادبیات و علومِ انسانی، دانشگاه ارومیه»; corresponding-author `k.jabbary@urmia.ac.ir`; second-author `a.jabbary@urmia.ac.ir`. Consistent with `manuscript.md` lines 6–13 (English mirror lines 446–448 ditto).
- **LLM/AI disclosure**: grep on cover letter for {ChatGPT, Claude, Anthropic, OpenAI, GPT, LLM, DALL-E, Midjourney, هوش مصنوعی, مدل زبانی, تولیدشده توسط, تهیه‌شده با کمک} → **0 matches**.

---

## 6. Files modified by this pass

| File | Change |
|---|---|
| `paper/persian/cover_letter.md` | Word-count update: ۸٬۰۸۰ → ۷٬۸۹۰ |
| `paper/persian/manuscript.tex` | Regenerated via pandoc (replaces 2026-05-13 15:00 version) |
| `paper/persian/manuscript_body.tex` | Regenerated via pandoc (replaces 2026-05-13 15:00 version) |
| `paper/persian/manuscript.docx` | Regenerated via pandoc (replaces 2026-05-13 15:00 version) |
| `reviews/fa_finalize.md` | This report (new) |

**Not modified**: `paper/persian/manuscript.md` (no edits in this pass — the structural- and content-fix agents had it submission-ready), `paper/persian/template.tex` (hand-maintained), `paper/persian/manuscript.pdf` (user re-compiles via XeLaTeX locally).

---

## 7. Outstanding items (deliberate)

- ORCID placeholders `0000-0000-0000-0000` in `manuscript.md` (lines 9, 13, 446, 448) — to be filled by authors before final submission. Flagged in structural-fix report §7.
- `manuscript.pdf` is **not** regenerated by this pass — the user compiles locally with MiKTeX/XeLaTeX per project convention (CLAUDE.md: "There is no Makefile or build script. Re-rendering PDFs is a manual `pandoc → xelatex` step the authors run locally.").

---

## 8. Submission-readiness summary

The Persian manuscript bundle is submission-ready for *پژوهش‌های زبان‌شناختیِ قرآن* (NRGS):

- Body within word-limit band, 7,890 / 8,000.
- All sūrah references use «سورۀ X» izafe form.
- No LLM/AI disclosure anywhere.
- No cross-references to the English JQS paper from within the manuscript body; only the cover letter's mandated COPE/ICMJE disclosure paragraph names JQS.
- All 10 figures resolved.
- .tex / .docx regenerated cleanly from the polished `manuscript.md`.
- Cover-letter word-count claim now matches actuals.

User next steps (out-of-agent-scope):
1. Fill ORCIDs in `manuscript.md` lines 9 and 13.
2. Compile `manuscript.tex` with XeLaTeX (MiKTeX 25.4) to refresh `manuscript.pdf`.
3. Submit `.docx` + cover letter to NRGS portal.
