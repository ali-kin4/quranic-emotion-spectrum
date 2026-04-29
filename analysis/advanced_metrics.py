"""Research-grade extensions to the basic concordance pipeline.

Outputs (all into data/concordance/):
    morphology_by_root.csv     POS / morphological-form breakdown per root
    statistical_tests.csv      Chi-squared and binomial tests for distributional
                               claims (Stage-4 over-representation, Meccan/Medinan
                               exclusivity)
    network_centrality.csv     Degree, betweenness, eigenvector centrality on the
                               aya-level co-occurrence graph
    umbrella_cooccurrence.csv  Co-occurrence between the 10 spectrum roots and
                               the 6 umbrella moral terms (zlm, jrm, fsq, edw,
                               krh, $nA)
"""
from __future__ import annotations

import csv
import io
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path

import networkx as nx

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR / "analysis"))

from buckwalter import bw_to_arabic  # noqa: E402
from qac_parser import parse_qac  # noqa: E402
from spectrum_roots import EXPANSION, SPECTRUM, all_roots  # noqa: E402

QAC_PATH = ROOT_DIR / "data" / "quran" / "qac_morphology.txt"
CONC_DIR = ROOT_DIR / "data" / "concordance"
CONC_DIR.mkdir(parents=True, exist_ok=True)


# -------------------------------------------------------------------- #
#  Morphological breakdown                                             #
# -------------------------------------------------------------------- #

def morphological_breakdown() -> None:
    """For each spectrum root, count occurrences by part of speech.

    The QAC's POS tags include V (verb), N (noun), ADJ (adjective),
    PCPL (participle, marked via FLAGS), and a few others.  We collapse
    to four headline categories: VERB / NOUN / ADJ / PARTICIPLE, with
    OTHER as a catch-all.
    """
    target = {r.bw: r for r in all_roots(include_expansion=True)}
    counts: dict[str, Counter] = defaultdict(Counter)

    for seg in parse_qac(QAC_PATH):
        if seg.root not in target:
            continue
        pos = seg.features.get("POS", "")
        flags = seg.features.get("FLAGS", "")
        if "PCPL" in flags or "ACT PCPL" in flags or "PASS PCPL" in flags:
            cat = "PARTICIPLE"
        elif pos == "V":
            cat = "VERB"
        elif pos == "N":
            cat = "NOUN"
        elif pos == "ADJ":
            cat = "ADJECTIVE"
        else:
            cat = "OTHER" if pos else "—"
        counts[seg.root][cat] += 1

    out = CONC_DIR / "morphology_by_root.csv"
    with out.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow([
            "root_bw", "root_ar", "stage", "verb", "noun",
            "adjective", "participle", "other", "total",
        ])
        for r in all_roots(include_expansion=True):
            c = counts[r.bw]
            total = sum(c.values())
            w.writerow([
                r.bw, r.arabic, r.stage,
                c.get("VERB", 0), c.get("NOUN", 0),
                c.get("ADJECTIVE", 0), c.get("PARTICIPLE", 0),
                c.get("OTHER", 0) + c.get("—", 0), total,
            ])
    print(f"Wrote {out}")


# -------------------------------------------------------------------- #
#  Statistical tests                                                   #
# -------------------------------------------------------------------- #

def _binomial_pvalue(k: int, n: int, p: float) -> float:
    """Two-sided exact binomial p-value for observing k successes in n trials
    when the null is success-probability p.  We implement this from scratch
    rather than depend on scipy."""
    if n == 0:
        return 1.0
    # PMF
    def pmf(i):
        return (math.comb(n, i)
                * (p ** i)
                * ((1 - p) ** (n - i)))
    p_obs = pmf(k)
    p_total = sum(pmf(i) for i in range(n + 1) if pmf(i) <= p_obs + 1e-12)
    return min(1.0, p_total)


def _chi_squared(observed: list[int], expected: list[int]) -> tuple[float, int]:
    """Chi-squared statistic + degrees of freedom (no p-value, since we lack
    scipy)."""
    if len(observed) != len(expected):
        raise ValueError("Length mismatch")
    chi2 = sum(((o - e) ** 2) / e for o, e in zip(observed, expected) if e > 0)
    df = len(observed) - 1
    return chi2, df


# Critical chi-squared values at alpha=0.05, df 1..10 (scipy-free lookup)
_CHI2_CRITICAL_005 = {
    1: 3.841, 2: 5.991, 3: 7.815, 4: 9.488, 5: 11.070,
    6: 12.592, 7: 14.067, 8: 15.507, 9: 16.919, 10: 18.307,
}


def _chi2_critical_005(df: int) -> float:
    """Return the alpha=0.05 critical chi-squared value for df. Falls back
    to a Wilson–Hilferty approximation when df > 10."""
    if df in _CHI2_CRITICAL_005:
        return _CHI2_CRITICAL_005[df]
    # Wilson–Hilferty approximation; z_{0.95}=1.6449
    z = 1.6449
    return df * (1 - 2 / (9 * df) + z * (2 / (9 * df)) ** 0.5) ** 3


def statistical_tests() -> None:
    """Produce a CSV of formally reported tests.

    All test inputs and interpretations are derived dynamically from
    summary_counts.csv so that a re-run on a different corpus or root
    list produces consistent results without code changes.
    """
    # Read counts dynamically so changes to SPECTRUM / corpus reflow
    counts: dict[str, dict] = {}
    with (CONC_DIR / "summary_counts.csv").open("r", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            counts[row["root_bw"]] = {
                "occurrences": int(row["occurrences"]),
                "meccan": int(row["meccan_hits"]),
                "medinan": int(row["medinan_hits"]),
                "stage": int(row["stage"]),
            }

    # ---- Test 1: stage uniform-distribution chi-squared ----
    spectrum_bw = {r.bw for r in SPECTRUM}
    stages_present = sorted({r.stage for r in SPECTRUM})
    stage_totals = {s: 0 for s in stages_present}
    for bw in spectrum_bw:
        if bw in counts:
            stage_totals[counts[bw]["stage"]] += counts[bw]["occurrences"]

    observed = [stage_totals[s] for s in stages_present]
    n = sum(observed)
    expected_uniform = [n / len(observed)] * len(observed)
    chi2_uniform, df_uniform = _chi_squared(observed, expected_uniform)
    # Critical chi2 (alpha=0.05) for selected df values
    crit_uniform = _chi2_critical_005(df_uniform)
    rejects_uniform = chi2_uniform > crit_uniform

    # ---- Test 2: Meccan/Medinan binomial tests, dynamically per root ----
    # In the QAC the corpus baseline is ~60% Meccan, ~40% Medinan.
    p_meccan = 0.60

    def _binom_test(bw: str) -> tuple[int, int, float]:
        """Return (meccan, total, two-sided p) computed from current counts."""
        rec = counts.get(bw, {"meccan": 0, "medinan": 0})
        m, d = rec["meccan"], rec["medinan"]
        total = m + d
        if total == 0:
            return 0, 0, 1.0
        return m, total, _binomial_pvalue(m, total, p_meccan)

    sxt_m, sxt_n, sxt_p = _binom_test("sxT")
    asf_m, asf_n, asf_p = _binom_test("Asf")
    etw_m, etw_n, etw_p = _binom_test("Etw")
    jrm_m, jrm_n, jrm_p = _binom_test("jrm")
    fsq_m, fsq_n, fsq_p = _binom_test("fsq")

    # ---- Test 3: phenomenology (S1..N-1) vs outcomes (last stage) ----
    last_stage = stages_present[-1]
    lower_stages = stages_present[:-1]
    lower = sum(stage_totals[s] for s in lower_stages)
    upper = stage_totals[last_stage]
    chi2_split, df_split = _chi_squared(
        [lower, upper], [(lower + upper) / 2, (lower + upper) / 2]
    )
    crit_split = _chi2_critical_005(df_split)
    rejects_split = chi2_split > crit_split

    out = CONC_DIR / "statistical_tests.csv"
    with out.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["test", "statistic", "value", "interpretation"])
        w.writerow([
            "Stage uniform-distribution chi-squared",
            f"chi2 (df={df_uniform})", f"{chi2_uniform:.2f}",
            f"Observed: {observed}; expected uniform: ~{expected_uniform[0]:.1f} each. "
            f"chi2={chi2_uniform:.2f}; critical={crit_uniform:.2f} (alpha=0.05) — "
            + ("REJECT null. Stages are non-uniform."
               if rejects_uniform
               else "FAIL TO REJECT null. Stage frequencies are consistent with uniformity."),
        ])
        w.writerow([
            f"Phenomenology (Stages {lower_stages[0]}-{lower_stages[-1]}) vs "
            f"Behavioural outcomes (Stage {last_stage})",
            f"chi2 (df={df_split})", f"{chi2_split:.2f}",
            f"Phenomenology stages: {lower}; outcome stage: {upper}. "
            f"chi2={chi2_split:.2f}; critical={crit_split:.2f}. "
            + ("REJECT null — outcomes dominate."
               if rejects_split
               else "FAIL TO REJECT null — corpus distributes mass roughly "
                    "equally between anger phenomenology and behavioural outcomes, "
                    "consistent with the reviewer's caveat that the outcome-stage "
                    "lexemes (e.g. baghy / tughyan / 'utuww) are not exclusively "
                    "anger-derived."),
        ])
        w.writerow([
            f"sakhat (sxT) Meccan exclusivity ({sxt_m}/{sxt_n})",
            "binomial 2-sided p-value", f"{sxt_p:.4f}",
            f"Under H0 of {p_meccan} Meccan rate, observing {sxt_m}/{sxt_n} Meccan "
            + ("supports specialized Medinan use."
               if sxt_p < 0.05 and sxt_m == 0
               else "is consistent with the corpus baseline."),
        ])
        w.writerow([
            f"asaf (Asf) Meccan exclusivity ({asf_m}/{asf_n})",
            "binomial 2-sided p-value", f"{asf_p:.4f}",
            f"Under H0 of {p_meccan} Meccan rate, observing {asf_m}/{asf_n} Meccan "
            + ("is significantly Meccan-skewed."
               if asf_p < 0.05
               else "is suggestive but not decisive on its own (n is tiny)."),
        ])
        w.writerow([
            f"utuww (Etw) Meccan dominance ({etw_m}/{etw_n})",
            "binomial 2-sided p-value", f"{etw_p:.4f}",
            f"{etw_m} of {etw_n} Meccan; "
            + ("Strong Meccan preference, consistent with early-revelation "
               "rebellion-against-revelation patterns."
               if etw_p < 0.10
               else "Distribution consistent with the corpus baseline."),
        ])
        w.writerow([
            f"jrm (umbrella) Meccan dominance ({jrm_m}/{jrm_n})",
            "binomial 2-sided p-value", f"{jrm_p:.4f}",
            f"{jrm_m} of {jrm_n} Meccan; "
            + ("Robust Meccan preference, aligns with early-revelation "
               "polemic with the mushrikun."
               if jrm_p < 0.05
               else "Distribution consistent with the corpus baseline."),
        ])
        w.writerow([
            f"fsq (umbrella) Medinan tilt ({fsq_m}/{fsq_n})",
            "binomial 2-sided p-value", f"{fsq_p:.4f}",
            f"{fsq_m} Meccan / {fsq_n - fsq_m} Medinan; "
            + ("Significant Medinan tilt, reflecting community-discipline contexts."
               if fsq_p < 0.05 and fsq_m / fsq_n < p_meccan
               else "Distribution consistent with the corpus baseline."),
        ])
    print(f"Wrote {out}")


# -------------------------------------------------------------------- #
#  Network centrality                                                  #
# -------------------------------------------------------------------- #

def network_centrality() -> None:
    """Compute centrality metrics on the aya-level co-occurrence graph
    of the 10 core spectrum roots."""
    aya_to_roots: dict[tuple[int, int], set[str]] = defaultdict(set)
    with (CONC_DIR / "master_concordance.csv").open("r", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            aya_to_roots[(int(row["sura"]), int(row["aya"]))].add(row["root_bw"])

    core = {r.bw for r in SPECTRUM}
    edges: Counter = Counter()
    for (sura, aya), roots in aya_to_roots.items():
        present = sorted(roots & core)
        for i, a in enumerate(present):
            for b in present[i + 1:]:
                edges[(a, b)] += 1

    G = nx.Graph()
    for r in SPECTRUM:
        G.add_node(r.bw)
    for (a, b), w in edges.items():
        # `weight` = co-occurrence count (proximity / similarity)
        # `distance` = inverse of weight, used by NetworkX shortest-path
        # routines that expect edge cost. Using the raw weight as distance
        # would invert the meaning (frequent neighbours treated as far apart).
        G.add_edge(a, b, weight=w, distance=1.0 / w)

    # Degree centrality: sum of co-occurrence weights — proximity-based
    degree = dict(G.degree(weight="weight"))
    # Betweenness / closeness: shortest-path-based, want DISTANCE as cost
    betweenness = nx.betweenness_centrality(G, weight="distance",
                                            normalized=True)
    closeness = nx.closeness_centrality(G, distance="distance")
    # Eigenvector: power iteration (no scipy dependency, per project policy)
    try:
        eigenvector = nx.eigenvector_centrality(
            G, weight="weight", max_iter=1000, tol=1e-7,
        )
    except (nx.PowerIterationFailedConvergence, Exception):
        eigenvector = {n: float("nan") for n in G.nodes()}

    out = CONC_DIR / "network_centrality.csv"
    with out.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow([
            "root_bw", "root_ar", "stage",
            "degree_weighted", "betweenness", "closeness", "eigenvector",
        ])
        for r in SPECTRUM:
            w.writerow([
                r.bw, r.arabic, r.stage,
                degree.get(r.bw, 0),
                f"{betweenness.get(r.bw, 0):.4f}",
                f"{closeness.get(r.bw, 0):.4f}",
                f"{eigenvector.get(r.bw, 0):.4f}",
            ])
    print(f"Wrote {out}")


# -------------------------------------------------------------------- #
#  Co-occurrence with umbrella moral terms                              #
# -------------------------------------------------------------------- #

def umbrella_cooccurrence() -> None:
    """For each spectrum root × each umbrella moral term, count the number
    of ayat in which both occur."""
    aya_to_roots: dict[tuple[int, int], set[str]] = defaultdict(set)
    with (CONC_DIR / "master_concordance.csv").open("r", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            aya_to_roots[(int(row["sura"]), int(row["aya"]))].add(row["root_bw"])

    core = [r for r in SPECTRUM]
    umbrella = [r for r in EXPANSION]

    counts: dict[tuple[str, str], int] = defaultdict(int)
    for roots in aya_to_roots.values():
        present_core = [r.bw for r in core if r.bw in roots]
        present_umb = [r.bw for r in umbrella if r.bw in roots]
        for c in present_core:
            for u in present_umb:
                counts[(c, u)] += 1

    out = CONC_DIR / "umbrella_cooccurrence.csv"
    with out.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        header = ["spectrum_root_bw", "spectrum_root_ar", "spectrum_stage"]
        for u in umbrella:
            header.append(f"with_{u.bw}_({u.arabic})")
        header.append("total_with_umbrella")
        w.writerow(header)
        for c in core:
            row = [c.bw, c.arabic, c.stage]
            row_total = 0
            for u in umbrella:
                v = counts[(c.bw, u.bw)]
                row.append(v)
                row_total += v
            row.append(row_total)
            w.writerow(row)
    print(f"Wrote {out}")


if __name__ == "__main__":
    morphological_breakdown()
    statistical_tests()
    network_centrality()
    umbrella_cooccurrence()
    print("\nAll advanced metrics generated.")
