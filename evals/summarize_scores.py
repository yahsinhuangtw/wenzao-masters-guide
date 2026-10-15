#!/usr/bin/env python3
"""Summarize a scored run sheet: with the guide versus without it.

    python3 evals/summarize_scores.py evals/run-sheet.csv

Blank cells are skipped (item did not apply or was not scored). Standard library only.
"""
import csv
import json
import pathlib
import statistics
import sys
from collections import defaultdict

HERE = pathlib.Path(__file__).resolve().parent
ITEMS = ["F1", "F2", "F3", "F4", "F5", "F6"]


def num(x):
    x = (x or "").strip()
    if x == "" or x.upper() == "NA":
        return None
    return float(x)


def mean(values):
    return statistics.mean(values) if values else None


def fmt(v):
    return "  -  " if v is None else f"{v:.2f}"


def main():
    path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "run-sheet.csv"
    cats = {e["id"]: e["category"] for e in json.loads((HERE / "evals.json").read_text(encoding="utf-8"))["evals"]}
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    scored = [r for r in rows if any(num(r.get(c)) is not None for c in ITEMS + ["helpful_1to5"])]
    print(f"{len(scored)} scored rows out of {len(rows)}\n")
    if not scored:
        return

    groups = defaultdict(list)
    for r in scored:
        groups[(r["assistant"], r["arm"])].append(r)

    header = "assistant".ljust(12) + "arm".ljust(15) + "n".rjust(3) + "  " + "  ".join(i.rjust(5) for i in ITEMS) + "  helpful"
    print(header)
    print("-" * len(header))
    means = {}
    for (assistant, arm), rs in sorted(groups.items()):
        per = {i: mean([num(r[i]) for r in rs if num(r[i]) is not None]) for i in ITEMS}
        helpful = mean([num(r["helpful_1to5"]) for r in rs if num(r["helpful_1to5"]) is not None])
        means[(assistant, arm)] = (per, helpful)
        print(assistant.ljust(12) + arm.ljust(15) + str(len(rs)).rjust(3) + "  "
              + "  ".join(fmt(per[i]).rjust(5) for i in ITEMS) + "  " + fmt(helpful))

    print("\nDifference (with_guide minus without_guide):")
    for assistant in sorted({a for a, _ in groups}):
        w, wo = means.get((assistant, "with_guide")), means.get((assistant, "without_guide"))
        if not w or not wo:
            continue
        deltas = []
        for i in ITEMS:
            a, b = w[0][i], wo[0][i]
            deltas.append("  -  " if a is None or b is None else f"{a - b:+.2f}")
        h = "  -  " if w[1] is None or wo[1] is None else f"{w[1] - wo[1]:+.2f}"
        print(assistant.ljust(27) + "   " + "  ".join(d.rjust(5) for d in deltas) + "  " + h)

    print("\nF1 (no invented facts) on hallucination-trap questions:")
    for (assistant, arm), rs in sorted(groups.items()):
        vals = [num(r["F1"]) for r in rs if cats.get(int(r["eval_id"])) == "hallucination-trap" and num(r["F1"]) is not None]
        print(f"  {assistant.ljust(12)}{arm.ljust(15)}{fmt(mean(vals))}  (n={len(vals)})")


if __name__ == "__main__":
    main()
