# Zenodo Archival Instructions

JQS, DSH, *Cognitive Linguistics*, and NRGS all benefit from (and DSH requires) a permanent archival snapshot of the code and data, with a citable DOI.

## Why Zenodo

- Persistent DOI for code + data, distinct from the live GitHub repo
- Required by some funders / journals for reproducibility
- Free, integrated with GitHub via OAuth one-click

## One-time setup

1. Visit https://zenodo.org and sign in with the GitHub account that owns this repo (`ali-kin4`).
2. Go to **Settings → GitHub** in Zenodo.
3. Toggle **on** the switch next to `ali-kin4/quranic-emotion-spectrum`.
4. (Optional) Edit the Zenodo metadata (authors, license, keywords) — defaults from the repo's `.zenodo.json` or fall back to GitHub metadata.

## Triggering an archival snapshot

After the corresponding author has approved the manuscript:

```bash
git tag -a v1.0-jqs-submission -m "JQS submission snapshot — May 2026"
git push origin v1.0-jqs-submission
```

That `git push --tags` event triggers Zenodo to create a versioned release with a permanent DOI of the form `10.5281/zenodo.XXXXXXX`. Concept-DOI (always points to latest) and version-DOI (points to v1.0) are both generated.

## Inserting the DOI into the manuscripts

Replace `[ZENODO DOI to be inserted]` in:

- `paper/english/manuscript.md` — "Data and Code Availability" section (`§ Data and Code Availability`)
- `paper/persian/manuscript.md` — پیوست `پیوست: داده‌ها، کد، و قابلیت بازتولید`
- `paper/english/cover_letter.md` — references to data availability
- `paper/persian/cover_letter.md` — references to data availability

After the Zenodo DOI is assigned, run:

```bash
sed -i 's|\[ZENODO DOI to be inserted\]|10.5281/zenodo.XXXXXXX|g' \
    paper/english/manuscript.md \
    paper/persian/manuscript.md \
    paper/english/cover_letter.md \
    paper/persian/cover_letter.md
```

Then regenerate `.tex` and `.pdf` (see `SUBMISSION_CHECKLIST.md` §C).

## Suggested Zenodo metadata

```yaml
title: "Quranic Emotion Spectrum: Code, Data, and Manuscripts"
authors:
  - name: Jabbary, Karim
    affiliation: Urmia University
    orcid: 0000-0000-0000-0000  # replace with real ORCID
  - name: Jabbary, Ali
    affiliation: Urmia University
    orcid: 0000-0000-0000-0000  # replace with real ORCID
description: >
  Reproducible Python pipeline and dataset for the analysis of fourteen
  Arabic anger-spectrum roots in the Qur'an across six phenomenological
  stages, accompanying two manuscripts: an English-language paper for
  Journal of Qur'anic Studies and a Persian-language tafsir-comparative
  companion paper for Pizhūhish-hā-yi Zabānshinākhtī-yi Qur'ān (NRGS,
  University of Isfahan).
keywords:
  - Qur'anic Arabic Corpus
  - semantic field
  - anger
  - cognitive linguistics
  - conceptual metaphor
  - Izutsu
  - tafsir
license: MIT (code) / CC-BY-4.0 (manuscripts)
upload_type: software (with publication metadata)
related_identifiers:
  - relation: isSupplementTo
    identifier: 10.3366/jqs.20XX.XXXX  # JQS DOI when assigned
```
