"""Run the QAC extraction for the spectrum roots and write CSV concordances.

Usage (from repo root):
    python analysis/extract_concordance.py

Outputs to data/concordance/:
    master_concordance.csv     — every hit, every spectrum root
    by_root_<root>.csv         — per-root concordance
    summary_counts.csv         — aggregated frequency table
    sura_distribution.csv      — counts per sura per root
"""
from __future__ import annotations

import csv
import io
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

# Ensure UTF-8 stdout on Windows so Arabic prints cleanly
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR / "analysis"))

from buckwalter import bw_to_arabic  # noqa: E402
from qac_parser import collapse_to_words, segments_by_roots  # noqa: E402
from spectrum_roots import STAGE_LABELS_EN, all_roots  # noqa: E402

QAC_PATH = ROOT_DIR / "data" / "quran" / "qac_morphology.txt"
QURAN_JSON = ROOT_DIR / "data" / "quran" / "quran_check.json"
OUT_DIR = ROOT_DIR / "data" / "concordance"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def load_quran_text() -> dict[tuple[int, int], str]:
    """Return (sura, aya) → verse text for the verse-level surface lookup."""
    if not QURAN_JSON.exists():
        return {}
    data = json.loads(QURAN_JSON.read_text(encoding="utf-8"))
    out: dict[tuple[int, int], str] = {}
    for sura in data:
        sid = sura["id"]
        for v in sura["verses"]:
            out[(sid, v["id"])] = v["text"]
    return out


def load_sura_meta() -> dict[int, dict]:
    """Return sura_id → {name, type, total_verses}."""
    if not QURAN_JSON.exists():
        return {}
    data = json.loads(QURAN_JSON.read_text(encoding="utf-8"))
    return {s["id"]: {"name": s["name"], "type": s["type"], "total_verses": s["total_verses"],
                      "transliteration": s.get("transliteration", "")} for s in data}


def main() -> None:
    roots = all_roots(include_expansion=True)
    bw_list = [r.bw for r in roots]

    print(f"Parsing QAC at {QAC_PATH} ...")
    grouped = segments_by_roots(QAC_PATH, bw_list)
    text_lookup = load_quran_text()
    sura_meta = load_sura_meta()

    # ---- master concordance (one row per surface word) ----
    master_path = OUT_DIR / "master_concordance.csv"
    summary_counter: Counter = Counter()
    sura_counter: dict[str, Counter] = defaultdict(Counter)
    revelation_counter: dict[str, Counter] = defaultdict(Counter)

    with master_path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow([
            "sura", "aya", "word", "root_bw", "root_ar", "stage",
            "english_gloss", "persian_gloss", "surface_form_bw",
            "surface_form_ar", "lemma_bw", "lemma_ar", "pos",
            "sura_name", "sura_type", "verse_text",
        ])
        for r in roots:
            segs = grouped.get(r.bw, [])
            words = collapse_to_words(segs)
            summary_counter[r.bw] = len(words)
            for word in words:
                meta = sura_meta.get(word["sura"], {})
                sura_counter[r.bw][word["sura"]] += 1
                rev_type = meta.get("type", "?")
                revelation_counter[r.bw][rev_type] += 1
                w.writerow([
                    word["sura"], word["aya"], word["word"],
                    r.bw, r.arabic, r.stage, r.english, r.persian,
                    word["surface_form"], bw_to_arabic(word["surface_form"]),
                    word["lemma"] or "",
                    bw_to_arabic(word["lemma"]) if word["lemma"] else "",
                    word["pos"] or "",
                    meta.get("name", ""), rev_type,
                    text_lookup.get((word["sura"], word["aya"]), ""),
                ])
    print(f"Wrote {master_path}")

    # ---- per-root files ----
    by_root_dir = OUT_DIR / "by_root"
    by_root_dir.mkdir(exist_ok=True)
    for r in roots:
        segs = grouped.get(r.bw, [])
        words = collapse_to_words(segs)
        if not words:
            continue
        path = by_root_dir / f"{r.bw}.csv"
        with path.open("w", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh)
            w.writerow([
                "sura", "aya", "word_index", "surface_form_ar",
                "lemma_ar", "pos", "sura_name", "sura_type", "verse_text",
            ])
            for word in words:
                meta = sura_meta.get(word["sura"], {})
                w.writerow([
                    word["sura"], word["aya"], word["word"],
                    bw_to_arabic(word["surface_form"]),
                    bw_to_arabic(word["lemma"]) if word["lemma"] else "",
                    word["pos"] or "",
                    meta.get("name", ""), meta.get("type", ""),
                    text_lookup.get((word["sura"], word["aya"]), ""),
                ])

    # ---- summary counts ----
    summary_path = OUT_DIR / "summary_counts.csv"
    with summary_path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow([
            "root_bw", "root_ar", "english_gloss", "persian_gloss",
            "stage", "stage_label", "occurrences",
            "meccan_hits", "medinan_hits",
        ])
        for r in roots:
            cnt = summary_counter.get(r.bw, 0)
            w.writerow([
                r.bw, r.arabic, r.english, r.persian, r.stage,
                STAGE_LABELS_EN[r.stage], cnt,
                revelation_counter[r.bw].get("meccan", 0),
                revelation_counter[r.bw].get("medinan", 0),
            ])
    print(f"Wrote {summary_path}")

    # ---- sura distribution ----
    sura_path = OUT_DIR / "sura_distribution.csv"
    with sura_path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["root_bw", "root_ar", "sura", "sura_name", "sura_type", "count"])
        for r in roots:
            for sura_id, cnt in sorted(sura_counter[r.bw].items()):
                meta = sura_meta.get(sura_id, {})
                w.writerow([
                    r.bw, r.arabic, sura_id,
                    meta.get("name", ""), meta.get("type", ""), cnt,
                ])
    print(f"Wrote {sura_path}")

    # Print human-readable summary
    print("\n=== SPECTRUM FREQUENCY SUMMARY ===")
    print(f"{'Root':>6}  {'Arabic':>10}  Stage  Occurrences  Meccan  Medinan")
    print("-" * 60)
    for r in roots:
        c = summary_counter.get(r.bw, 0)
        print(f"{r.bw:>6}  {r.arabic:>10}    {r.stage}     {c:>6}   "
              f"{revelation_counter[r.bw].get('meccan', 0):>5}   "
              f"{revelation_counter[r.bw].get('medinan', 0):>5}")
    print(f"\nTotal hits across all spectrum roots: {sum(summary_counter.values())}")


if __name__ == "__main__":
    main()
