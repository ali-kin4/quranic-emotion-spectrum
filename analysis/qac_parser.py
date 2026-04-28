"""Parser for the Quranic Arabic Corpus (QAC) v0.4 morphology file.

The QAC file (Dukes 2011, GPL) provides one row per morphological segment:

    LOCATION    FORM    TAG    FEATURES

LOCATION is `(sura:aya:word:segment)`. FEATURES is a pipe-delimited
key:value field that includes ROOT and LEM among others. We extract a
flat per-segment record plus a per-word aggregation that joins all
segments of a single token (prefix + stem + suffix).
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator, Optional

LOCATION_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")
KV_RE = re.compile(r"([A-Z]+):([^|]+)")


@dataclass
class Segment:
    sura: int
    aya: int
    word: int
    seg: int
    form: str
    tag: str
    root: Optional[str] = None
    lemma: Optional[str] = None
    features: dict[str, str] = field(default_factory=dict)
    raw: dict = field(default_factory=dict)

    @property
    def location(self) -> tuple[int, int, int, int]:
        return self.sura, self.aya, self.word, self.seg


def parse_qac(path: str | Path) -> Iterator[Segment]:
    """Yield Segment records from a QAC v0.4 morphology file."""
    p = Path(path)
    with p.open("r", encoding="utf-8") as fh:
        in_header = True
        for line in fh:
            line = line.rstrip("\n")
            if not line or line.startswith("#"):
                continue
            if in_header and line.startswith("LOCATION"):
                in_header = False
                continue
            parts = line.split("\t")
            if len(parts) < 4:
                continue
            loc, form, tag, feats = parts[0], parts[1], parts[2], parts[3]
            m = LOCATION_RE.match(loc)
            if not m:
                continue
            sura, aya, word, seg = (int(x) for x in m.groups())
            features: dict[str, str] = {}
            for kv in feats.split("|"):
                if ":" in kv:
                    k, _, v = kv.partition(":")
                    features[k] = v
                else:
                    features.setdefault("FLAGS", "")
                    features["FLAGS"] += ("|" if features["FLAGS"] else "") + kv
            yield Segment(
                sura=sura,
                aya=aya,
                word=word,
                seg=seg,
                form=form,
                tag=tag,
                root=features.get("ROOT"),
                lemma=features.get("LEM"),
                features=features,
            )


def segments_by_root(path: str | Path, root_bw: str) -> list[Segment]:
    """Return every segment whose ROOT exactly matches `root_bw` (Buckwalter)."""
    return [s for s in parse_qac(path) if s.root == root_bw]


def segments_by_roots(path: str | Path, roots_bw: list[str]) -> dict[str, list[Segment]]:
    """One pass over the corpus, returning a dict root → segments."""
    out: dict[str, list[Segment]] = {r: [] for r in roots_bw}
    for s in parse_qac(path):
        if s.root in out:
            out[s.root].append(s)
    return out


def collapse_to_words(segs: list[Segment]) -> list[dict]:
    """Group segments by (sura, aya, word) — one row per surface word.

    Returns dicts with: sura, aya, word, surface_form, root, lemma, tag.
    """
    groups: dict[tuple[int, int, int], list[Segment]] = {}
    for s in segs:
        groups.setdefault((s.sura, s.aya, s.word), []).append(s)
    out = []
    for (sura, aya, word), parts in sorted(groups.items()):
        parts.sort(key=lambda x: x.seg)
        stem = next((p for p in parts if "POS" in p.features), parts[0])
        out.append({
            "sura": sura,
            "aya": aya,
            "word": word,
            "surface_form": "".join(p.form for p in parts),
            "root": stem.root,
            "lemma": stem.lemma,
            "tag": stem.tag,
            "pos": stem.features.get("POS"),
            "n_segments": len(parts),
        })
    return out
