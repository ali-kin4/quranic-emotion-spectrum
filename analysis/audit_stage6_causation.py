"""Reproducible audit of the Stage-6 bidirectional-causation coding.

The Stage-6 behavioural-outcome lexemes (baghy / ṭughyān / ʿutuww — 145
attestations) are each classified, on the joint reading of the four reference
commentaries (al-Mīzān, al-Kashshāf, Majmaʿ al-Bayān, al-Taḥrīr wa-l-Tanwīr,
3-of-4 majority rule), as:

    A    anger-derived  — behavioural completion of an inner-anger trajectory
    S    structurally derived — arising from greed / istikbār / ʿulw fi al-arḍ
         or institutional-power asymmetry, with no explicit anger antecedent
    A+S  both readings available, or the commentaries diverge

This script does two things and fabricates nothing:

  * ``--init`` (re)generates the row-level worksheet
    ``data/concordance/stage6_causation_coding.csv`` *directly from the
    committed corpus* — the real 145 attestations (root, sūra, āya, sūra name,
    verse text) with EMPTY ``coding`` / ``coder2`` / ``rationale_short``
    columns for the corresponding author to fill from the coding sheet.

  * default mode audits a *filled* worksheet: aggregate A/S/A+S counts,
    per-root breakdown, and — when a second-coder column is present — the
    3x3 confusion matrix and Cohen's kappa. No scipy dependency (kappa is
    implemented directly), matching the repository's dependency policy.

Usage:
    python analysis/audit_stage6_causation.py --init   # build the blank worksheet
    python analysis/audit_stage6_causation.py          # audit a filled worksheet
"""
from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CODING = ROOT / "data" / "concordance" / "stage6_causation_coding.csv"
MASTER = ROOT / "data" / "concordance" / "master_concordance.csv"

SPECTRUM_S6 = ["bgy", "Tgy", "Etw"]          # baghy, ṭughyān, ʿutuww (Buckwalter)
LABELS = ["A", "S", "A+S"]
FIELDS = ["root_bw", "root_ar", "sura", "aya", "sura_name", "sura_type",
          "coding", "coder2", "rationale_short", "verse_text"]

HEADER_COMMENT = [
    "# Stage-6 causation coding worksheet (baghy / ṭughyān / ʿutuww, n=145).",
    "# Coding scheme: A = anger-derived; S = structurally derived",
    "#                (greed / istikbār / ʿulw fi al-arḍ / power asymmetry);",
    "#                A+S = both readings available or commentaries diverge.",
    "# Decision rule: 3-of-4 majority across al-Mīzān, al-Kashshāf,",
    "#                Majmaʿ al-Bayān, al-Taḥrīr wa-l-Tanwīr.",
    "# Reliability:   second-coder verification on a 20% sample, Cohen's kappa = 0.79.",
    "# Reported aggregates (corresponding author's coding): A=38 (26%),",
    "#                S=71 (49%), A+S=36 (25%). Per root: bgy A=22/S=50/A+S=24;",
    "#                Tgy A=11/S=19/A+S=9; Etw A=5/S=2/A+S=3.",
    "# The verse-level codes below are entered by the corresponding author;",
    "# run `python analysis/audit_stage6_causation.py` to regenerate the",
    "# aggregates, confusion matrix and kappa deterministically.",
]


def load_attestations():
    """The real 145 spectrum Stage-6 attestations, straight from the corpus."""
    rows = []
    with open(MASTER, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["stage"] == "6" and r["root_bw"] in SPECTRUM_S6:
                rows.append(r)
    order = {b: i for i, b in enumerate(SPECTRUM_S6)}
    rows.sort(key=lambda r: (order[r["root_bw"]], int(r["sura"]), int(r["aya"])))
    return rows


def init_worksheet():
    atts = load_attestations()
    with open(CODING, "w", encoding="utf-8", newline="") as f:
        for line in HEADER_COMMENT:
            f.write(line + "\n")
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        for r in atts:
            row = {k: r.get(k, "") for k in FIELDS}
            row["coding"] = row["coder2"] = row["rationale_short"] = ""
            w.writerow(row)
    print(f"Wrote {CODING.relative_to(ROOT)} with {len(atts)} attestations "
          f"({Counter(r['root_bw'] for r in atts)}). Codes left blank for coding.")


def read_filled():
    rows = []
    with open(CODING, encoding="utf-8") as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            rows.append(line)
    reader = csv.DictReader(rows)
    return [r for r in reader]


def cohens_kappa(pairs):
    """Unweighted Cohen's kappa for a list of (coder1, coder2) label pairs."""
    n = len(pairs)
    if n == 0:
        return None
    po = sum(1 for a, b in pairs if a == b) / n
    c1 = Counter(a for a, _ in pairs)
    c2 = Counter(b for _, b in pairs)
    pe = sum((c1.get(l, 0) / n) * (c2.get(l, 0) / n) for l in LABELS)
    return (po - pe) / (1 - pe) if pe != 1 else 1.0


def audit():
    rows = read_filled()
    coded = [r for r in rows if (r.get("coding") or "").strip() in LABELS]
    print(f"Attestations in worksheet: {len(rows)}")
    if not coded:
        print("Per-verse codes not yet entered — worksheet is the blank scaffold.")
        print("Fill the 'coding' (and optional 'coder2') column, then re-run.")
        return
    counts = Counter(r["coding"].strip() for r in coded)
    total = sum(counts.values())
    print("\nAggregate counts:")
    for l in LABELS:
        print(f"  {l:>3}: {counts.get(l, 0):>3}  ({counts.get(l, 0)/total:.0%})")
    print("\nPer root:")
    for b in SPECTRUM_S6:
        sub = Counter(r["coding"].strip() for r in coded if r["root_bw"] == b)
        print(f"  {b:>3} (n={sum(sub.values())}): " +
              ", ".join(f"{l}={sub.get(l, 0)}" for l in LABELS))
    pairs = [(r["coding"].strip(), r["coder2"].strip())
             for r in coded if (r.get("coder2") or "").strip() in LABELS]
    if pairs:
        print(f"\nSecond-coder overlap: {len(pairs)} attestations")
        print("Confusion matrix (rows=coder1, cols=coder2):")
        print("        " + "".join(f"{l:>6}" for l in LABELS))
        for a in LABELS:
            print(f"  {a:>5} " +
                  "".join(f"{sum(1 for x,y in pairs if x==a and y==l):>6}" for l in LABELS))
        print(f"Cohen's kappa = {cohens_kappa(pairs):.3f}")


if __name__ == "__main__":
    if "--init" in sys.argv[1:]:
        init_worksheet()
    else:
        audit()
