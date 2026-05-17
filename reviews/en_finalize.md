# English manuscript — final submission-prep report

**Date.** 9 May 2026 (the joint EN/FA submission window).
**Scope.** Final trim, cover-letter update, pandoc regeneration of `.tex` / `.docx`,
QC sweep against AI-disclosure and placeholder tokens, and figure-reference verification.

## 1. Final body word count

After targeted trims, the main body sits at **9,792 words**, below the JQS 9,800 sweet
spot and the 10,000 ceiling. Per-section breakdown (computed by stripping image
captions, tables, and code-fenced blocks — i.e., what JQS counts as "main body"):

| Section | Words |
|---|---:|
| §1 Introduction | 1,201 |
| §2 Theoretical Framework | 719 |
| §3 Methods | 955 |
| §4 Findings | 4,294 |
| §5 Discussion | 1,899 |
| §6 Conclusion | 724 |
| **TOTAL** | **9,792** |

Trim was -441 words from the baseline of 10,233 (per the previous agent's count).
Reviewer-mandated content (Sinai/Neuwirth/Maalej engagement, κ-protocol, Izutsu
deepening, Fauconnier-Turner blending, Lakoff-Kövecses 5-stage correction, Q. 3:134
fix, Stage-3 internal-ordering defence) was preserved verbatim. Trim targets were
adjectival/adverbial surplus, §1.1-§1.3 cross-paragraph repetition, conclusion
restatement, and methodology / table-caption duplication — the priority order
specified in the brief.

## 2. QC sweep results (manuscript.md, supplementary.md, cover_letter.md)

| Grep pattern | Hits | Resolution |
|---|---:|---|
| `ChatGPT\|Anthropic\|OpenAI\|AI-generated\|generated with\|drafted with\|assisted by AI\|DALL-E\|Midjourney\|image gen` (case-insensitive) | 0 | clean |
| `\bClaude\b\|\bLLM\b\|\bGPT\b` | 0 | clean |
| `language model` | 3 (paper/english/supplementary.md L25; manuscript.md L323; .tex emissions) | All legitimately refer to CAMeLBERT-CA (S2 analysis) — retained per brief |
| `\[VERIFY:\|\[Author\|TODO\|FIXME\|XXX\|PLACEHOLDER` | 0 | clean |
| `\[Department\]\|\[Institution\]\|\[Date\]\|\[ORCID\]` | 0 | clean — placeholders all replaced |
| Persian-cross-references in body (`Persian manuscript\|Persian paper\|Persian version\|our other paper\|see Jabbary\|in press`) | 0 | clean. Lines 53 / 423 contain (a) Persian-tradition scholarship references (Qāʾimīniyā, Pakatchi) and (b) the parallel-publication disclosure note, both legitimate per project rules |
| Bibliography "[in Persian]" tags | several | All inside `## Bibliography` (excluded from body count) |

All eight figure references in `manuscript.md` resolve to real files in `figures/`:
`fig1_continuum_v2.jpg`, `fig2_frequency_by_stage.pdf`, `fig3_meccan_medinan.pdf`,
`fig4_cooccurrence.pdf`, `fig5_morphology_stack.pdf`, `fig6_metaphor_v2.jpg`,
`fig7_centrality.pdf`, `fig8_methodology.jpg`.

## 3. Cover-letter changes

**File.** `paper/english/cover_letter.md`

Changes applied:

- **Affiliation block.** `[Department]` placeholder → `Department of Arabic Language
  and Literature`. Added `Faculty of Letters and Humanities, Urmia University`
  as a second affiliation line.
- **Word-count claim.** "13,032 words; abstract 208 words" → "main body ~9,800
  words; abstract ~250 words" (matches actual post-trim counts: body 9,792,
  abstract 250).
- **§ 2 (novel-finding paragraph).** Updated *sakhaṭ* claim to reflect the
  current borderline-FDR status (raw *p* = 0.005; Holm-adjusted *p* = 0.050) and
  acknowledged that three other roots (*karh*, *baghy*, *ghayẓ*) survive
  emphatically. Removed the now-outdated "only spectrum root surviving Holm" line.
- **Q. 67:8 sentence.** Tightened wording from "no comprehensive cross-cultural
  philological survey has yet been conducted" to "calibrated against a focused
  six-tradition philological survey... that acknowledges Job 32:19 (*bāqaʿ*) as
  the one clear Northwest-Semitic precedent" — bringing the cover letter in
  line with the §5.5 update in the body.
- **Methodology paragraph.** Added Sinai (2017) and Neuwirth (2019) alongside
  Sinai (2023), and added Khan et al. (2025).
- **Parallel-publication disclosure.** Verified to match the project rule: the
  papers "are independent works that share only the empirical dataset (QAC v0.4,
  Dukes 2011) and the reproducible analysis pipeline. They do not cite each other
  and have no content overlap." Removed the previous slightly weaker phrasing
  "have no content overlap beyond the shared corpus." Removed the ~10,786-word
  size figure for the Persian paper (kept the title only).
- **Suggested reviewers.** Replaced Hussein Abdul-Raof (Taibah) with **Zoltán
  Kövecses** (Eötvös Loránd, Budapest) — co-editor of *Metaphors of ANGER across
  Languages* (2025) and the most directly relevant CMT/anger reviewer; the
  paper's central claim is that the encyclopedia omits Classical Arabic and the
  Qur'anic *ghayẓ–kaẓm–tamayyuz* triad. The other three names (Sinai, Bauer,
  Atwell) preserved.
- **ORCID.** Kept as `0000-0000-0000-0000 (will be supplied at submission)` per
  the brief.
- **Date.** Confirmed `9 May 2026`.
- **No LLM/AI disclosure anywhere.** Cover letter grep for ChatGPT / Anthropic /
  OpenAI / LLM / GPT returns zero hits.

## 4. Pandoc regeneration

Working from `paper/english/manuscript.md`, with `--resource-path=figures` so that
pandoc can resolve relative image paths during DOCX embedding.

| Output | Command | Size | Status |
|---|---|---:|---|
| `paper/english/manuscript.tex` | `pandoc manuscript.md --template=template.tex --resource-path=figures --standalone -o manuscript.tex` | 126 KB | OK — 8 `\includegraphics` lines emitted; the template's `\graphicspath{{../../figures/}}` handles the path during XeLaTeX compile |
| `paper/english/manuscript_body.tex` | `pandoc manuscript.md --resource-path=figures -o manuscript_body.tex` | 120 KB | OK — body-only fragment for review-by-section |
| `paper/english/manuscript.docx` | `sed -E 's/\(fig([0-9]+)_([a-z_0-9]+)\.pdf\)/(fig\1_\2.png)/g'` preprocess into `/tmp/manuscript_png.md`, then `pandoc /tmp/manuscript_png.md --resource-path=figures -o manuscript.docx` | 1,540 KB (1.5 MB) | OK — all eight figures embedded as PNG (Word cannot embed `.pdf` figures, so the `.pdf` references were rewritten to `.png` for the DOCX path only; the `.tex` versions keep `.pdf` for the XeLaTeX compile) |

Pandoc 3.5 on Windows; no errors during any of the three runs.

## 5. Outstanding items for the user

- ORCIDs: still placeholder `0000-0000-0000-0000` on the author-affiliation block
  (manuscript.md L11–L12, cover_letter.md ORCID note). The user will populate at
  submission.
- XeLaTeX compile of `manuscript.tex` to PDF is a manual step on the user's
  machine (per the brief and CLAUDE.md).
- Per the no-LLM-disclosure rule, no acknowledgement of computational-writing
  assistance appears anywhere in the manuscript, supplementary, or cover letter.
