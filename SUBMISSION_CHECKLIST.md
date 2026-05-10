# Submission Checklist

Practical, ordered checklist for the corresponding author (Karim Jabbary) before clicking "submit" on either journal portal. Items grouped by what's *blocking* vs. *recommended*.

---

## A. Blocking items (must be done before submission)

### A1. ORCID identifiers

Both manuscripts and both cover letters currently carry the placeholder `0000-0000-0000-0000`.

- [ ] Karim Jabbary: register / locate ORCID at https://orcid.org → replace placeholder in:
  - `paper/english/manuscript.md` line 10
  - `paper/english/cover_letter.md` (if mentioned)
  - `paper/english/manuscript.md` "Author affiliations and ORCID" section (~line 424)
  - `paper/persian/manuscript.md` author block
- [ ] Ali Jabbary: same.
- [ ] After replacing, regenerate `.tex` and `.pdf` (instructions in §C below).

### A2. Author confirmation of all May 2026 revisions

The manuscripts have been substantially revised since the last author review:
- 14-root × 6-stage continuum (was 10/4)
- Permutation null, Holm-Bonferroni FDR, bootstrap CIs
- κ = 0.79 Stage-6 tafsir-coding audit
- Persian re-scoped as tafsir-comparative companion
- 10+ new 2024–2026 citations
- Cross-cultural philological survey (§5.5)
- JQS-style numbered short-title endnotes

- [ ] Karim Jabbary: read both manuscripts cover-to-cover and approve
- [ ] Ali Jabbary: read and approve
- [ ] Address any disagreements before submission

### A3. Editor names verified

Cover letters address:
- **JQS**: Professor M.A.S. Abdel Haleem (verified by Agent C; reverify on submission day)
- **NRGS**: Dr. Mohammad Reza Haji Esmaili (verified by Agent D; reverify on submission day)

- [ ] Confirm at https://www.euppublishing.com/journal/jqs (editorial board)
- [ ] Confirm at https://nrgs.ui.ac.ir/journal/editorial.staff?lang=fa
- [ ] If editor has changed, update salutation in both cover letters

### A4. Reviewer COI

Eight names suggested across the two cover letters (4 international + 4 Iranian). Agent G ran a public COI check; final author confirmation required:

- [ ] No co-authorship with Karim or Ali Jabbary
- [ ] No supervisory relationship (PhD, post-doc, examiner)
- [ ] No same-institution affiliation with Urmia University (Iran)
- [ ] No personal/family ties

Persian cover letter has a placeholder for the fourth reviewer — please supply or remove.

### A5. Postal address and department in cover letters

- [ ] Replace `[Department]` placeholder in `paper/english/cover_letter.md` with full department + faculty designation
- [ ] Confirm postal address for Urmia University formal header (currently only email is provided)

---

## B. Recommended items (raise quality / acceptance chances)

### B1. Code/data archival to Zenodo

JQS and DSH both encourage (DSH requires) a permanent archival snapshot with DOI:

- [ ] Visit https://zenodo.org and log in via GitHub OAuth
- [ ] Connect the repository `ali-kin4/quranic-emotion-spectrum` to Zenodo (one-click)
- [ ] Create a release (e.g. `v1.0-jqs-submission`) on GitHub — Zenodo will auto-archive and assign a DOI
- [ ] Insert the DOI into both manuscripts' "Data and Code Availability" sections
- [ ] Insert the DOI into both cover letters

### B2. Persian-native academic editor pass

Agent H performed a final polish pass; for a top-tier outcome, a 2–3 hour review by a Persian-native academic editor (ideally with Quranic-linguistic expertise) is recommended before NRGS submission.

- [ ] Engage editor (e.g., a Persian-fluent colleague at Urmia or another Iranian university)
- [ ] Review §۴-۴ غضب, §۴-۵ غیظ-کظم-تمیّز, §۴-۶ بَغی-طغیان-عتوّ in particular

### B3. JQS citation system

Agent E converted parenthetical (Author Year) citations to numbered short-title endnotes per JQS house style. Verify on the rendered PDF that:

- [ ] Footnote numbering is sequential
- [ ] First-occurrence footnotes carry full publication details
- [ ] Subsequent occurrences use short-title form (no *ibid*, no *op. cit.*)
- [ ] Bibliography is in JQS-Chicago style

### B4. Final visual proof of both PDFs

- [ ] `paper/english/manuscript.pdf` — proof for typography, figure rendering, cross-reference resolution
- [ ] `paper/persian/manuscript.pdf` — proof for BiDi, Persian numerals, ezafe consistency, Latin-block rendering

### B5. Pre-submission spell/grammar check

- [ ] Run Grammarly or similar tool on the English manuscript (final pass, accept conservatively — do not let auto-correct change Arabic transliteration)
- [ ] Run a Persian spell-check (e.g., Vafa, Virastman) on the Persian manuscript

---

## C. How to regenerate `.tex` and `.pdf` after edits

```bash
# Run from repository root
cd paper/english
pandoc manuscript.md --template=template.tex --pdf-engine=xelatex \
    -o manuscript.tex --standalone
pandoc manuscript.md -o manuscript_body.tex
xelatex -interaction=nonstopmode manuscript.tex
xelatex -interaction=nonstopmode manuscript.tex   # second pass for cross-refs

cd ../persian
pandoc manuscript.md --template=template.tex --pdf-engine=xelatex \
    -o manuscript.tex --standalone
pandoc manuscript.md -o manuscript_body.tex
xelatex -interaction=nonstopmode manuscript.tex
xelatex -interaction=nonstopmode manuscript.tex
```

Verify zero placeholders before submission:

```bash
grep -r "TO BE EXPANDED\|CITATION NEEDED\|0000-0000-0000-0000" paper/
```

Expected: no matches (after ORCID replacement).

---

## D. Submission portals

- **JQS**: editorial contact via Centre of Islamic Studies, SOAS — see https://www.euppublishing.com/journal/jqs/submit for current routing
- **NRGS Isfahan**: https://nrgs.ui.ac.ir → Submit Manuscript (سامانه ارسال مقاله)

---

## E. After submission

- [ ] Track submission ID at both portals
- [ ] Acknowledge any editor queries within 7 days
- [ ] When reviewer comments arrive: respond point-by-point, separate "response document" alongside revised manuscript
- [ ] If JQS accepts before NRGS responds, update NRGS cover letter to reflect "accepted at JQS" rather than "concurrently under consideration"
- [ ] Archive accepted version(s) on Zenodo with new DOI

---

*Last updated: per the comprehensive May 2026 revision (PR #5).*
