# Zenodo Archival Instructions

The target journal — *Pizhuhish'hā-yi Zabānshenakhtī-yi Qur'ān*
(University of Isfahan) — benefits from, and many international journals
require, a permanent archival snapshot of the code and data with a
citable DOI. Zenodo is the simplest path because of its native GitHub
integration.

## Why Zenodo

- Persistent DOI for code + data, distinct from the live GitHub repo
- Free, integrated with GitHub via OAuth one-click
- Mints both a *concept-DOI* (always resolves to latest version) and a
  *version-DOI* (frozen snapshot of a specific tag)
- Required by some funders and recommended by all reproducibility
  standards for computational humanities

## One-time setup (owner of `ali-kin4/quranic-emotion-spectrum`)

1. Visit <https://zenodo.org> and sign in with the GitHub account that
   owns this repo (`ali-kin4`).
2. Go to **Settings → GitHub** in Zenodo.
3. Toggle **on** the switch next to `ali-kin4/quranic-emotion-spectrum`.
4. (Optional but recommended) Edit the Zenodo metadata on the project
   page so it draws from `CITATION.cff` and `.zenodo.json`. Zenodo will
   prefer `.zenodo.json` when present.

## Triggering an archival snapshot

After the corresponding author has approved the manuscript:

```bash
git tag -a v1.0.0 -m "Pizhuhish'hā-yi Zabānshenakhtī-yi Qur'ān submission — May 2026"
git push origin v1.0.0
```

The `git push --tags` event triggers Zenodo to create a versioned release
with two DOIs:

| Kind         | Format                       | Always points to        |
|--------------|------------------------------|-------------------------|
| Concept DOI  | `10.5281/zenodo.XXXXXX0`     | Latest version (always) |
| Version DOI  | `10.5281/zenodo.XXXXXXN`     | This specific tag       |

The concept-DOI is what should be cited in the manuscript so readers
always reach the most recent version. The version-DOI is what tools
should cite for exact reproducibility.

## Inserting the DOI into the manuscript and citation files

After the Zenodo concept-DOI is assigned, replace both placeholder
strings (`10.5281/zenodo.XXXXXXX`) in **`CITATION.cff`** and in the
reproducibility appendix of **`paper/persian/manuscript.md`**:

```bash
# from repo root
sed -i 's|10.5281/zenodo.XXXXXXX|10.5281/zenodo.<CONCEPT_DOI>|g' CITATION.cff
sed -i 's|10.5281/zenodo.XXXXXXX|10.5281/zenodo.<CONCEPT_DOI>|g' paper/persian/manuscript.md
```

Then regenerate `paper/persian/manuscript.tex` and `manuscript.pdf`
(see `SUBMISSION_CHECKLIST.md` §C) and tag a new minor release so the
manuscript snapshot now carries its own DOI:

```bash
git commit -am "Insert Zenodo DOI into manuscript and CITATION.cff"
git tag -a v1.0.1 -m "DOI inserted into manuscript"
git push origin v1.0.1
```

## Canonical Zenodo metadata (suggested `.zenodo.json`)

If a `.zenodo.json` is committed at the repo root, Zenodo uses it as the
authoritative source. The fields below mirror `CITATION.cff` so the two
stay in sync. Adjust before the first release:

```json
{
  "title": "Quranic Emotion Spectrum: Reproducible Pipeline and Corpus Analysis of the Apex of Qur'anic Anger Lexicon",
  "description": "Reproducible Python pipeline and curated dataset for the analysis of fourteen Arabic anger-spectrum roots in the Qur'an across a six-stage phenomenological continuum, with tafsīr-grounded coding of all Stage-6 attestations (Cohen's κ = 0.79). Companion software to a Persian-language manuscript for Pizhuhish'hā-yi Zabānshenakhtī-yi Qur'ān (University of Isfahan).",
  "creators": [
    {
      "name": "Jabbary, Karim",
      "affiliation": "Department of Arabic Language and Literature, Urmia University"
    },
    {
      "name": "Jabbary, Ali",
      "affiliation": "Department of Computer Engineering, Urmia University"
    }
  ],
  "keywords": [
    "Qur'anic Arabic Corpus",
    "semantic field",
    "anger",
    "cognitive linguistics",
    "conceptual metaphor",
    "Toshihiko Izutsu",
    "tafsīr",
    "Persian Qur'anic studies",
    "reproducible research"
  ],
  "license": "MIT",
  "upload_type": "software",
  "access_right": "open",
  "language": "eng",
  "communities": [
    {"identifier": "digital-humanities"}
  ],
  "related_identifiers": [
    {
      "relation": "isSupplementTo",
      "identifier": "[Persian-journal DOI once assigned]",
      "resource_type": "publication-article"
    }
  ]
}
```

## Licensing summary

- **Code** (`analysis/`, `notebooks/`): MIT — see `LICENSE`.
- **Manuscripts** (`paper/`): CC-BY-4.0 (intended; declare on Zenodo).
- **Quranic Arabic Corpus** (Dukes 2011, `data/qac/`): GPL (upstream
  licence; redistribute under the same terms).
- **Tanzil Uthmani text** (`data/tanzil/`): CC-BY-ND-3.0 (upstream).

Zenodo allows a single top-level licence per record; pick MIT for the
software-release primary metadata and declare the other component
licences in the description text and in the README.

## Verification after release

After Zenodo mints the DOI, verify:

- [ ] `https://doi.org/10.5281/zenodo.<CONCEPT_DOI>` resolves to the
      Zenodo page.
- [ ] The Zenodo page lists both authors with correct affiliations.
- [ ] The release ZIP contains the `data/concordance/` CSVs and the
      `analysis/` Python pipeline.
- [ ] `CITATION.cff` validates: `pip install cffconvert && cffconvert --validate`.
- [ ] The DOI appears in the rendered Persian PDF's reproducibility
      appendix (recompile and visually inspect).
