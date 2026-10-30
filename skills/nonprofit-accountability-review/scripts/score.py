#!/usr/bin/env python3
"""
Compute points, percentages and tiers from a scores CSV, applying the rules in
references/scoring-rubric.md exactly, so nobody is moved by hand.

Usage:
    python3 score.py scores.csv [--out scored.csv] [--min-tests 5]

Input CSV columns (header names are case-insensitive):
    organisation, record_type, raised, scale (optional), placement (optional: P1/P2),
    GEO, SCHED, INTERNAL, GOV, FAMILY, RESERVES, UNNAMED, CLAIMS, PAY, PUBLIC
Each test cell holds 0, 1, 2, or n/a (blank also counts as n/a).

Output: the same rows plus tests_applied, points, max_points, percent, tier,
sorted by record type, then tier, then percent (desc), raised (desc), name.
"""
import argparse
import csv
import sys

TESTS = ["GEO", "SCHED", "INTERNAL", "GOV", "FAMILY", "RESERVES", "UNNAMED", "CLAIMS", "PAY", "PUBLIC"]
TIER_ORDER = {"Tier one": 1, "Tier two": 2, "Tier three": 3, "Insufficient record to tier": 4}


def parse_score(v):
    v = (v or "").strip().lower()
    if v in ("", "n/a", "na", "-", "none"):
        return None
    if v not in ("0", "1", "2"):
        raise ValueError(f"score must be 0, 1, 2 or n/a, got {v!r}")
    return int(v)


def to_number(v):
    try:
        return float(str(v).replace(",", "").replace("$", "").replace("£", "").replace("€", "").strip())
    except (ValueError, TypeError):
        return None


def tier_for(pct, applied, min_tests):
    if applied < min_tests:
        return "Insufficient record to tier"
    if pct >= 40:
        return "Tier one"
    if pct >= 20:
        return "Tier two"
    return "Tier three"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("scores")
    ap.add_argument("--out", default="scored.csv")
    ap.add_argument("--min-tests", type=int, default=5)
    a = ap.parse_args()

    with open(a.scores, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = []
        for raw in reader:
            row = {k.strip(): v for k, v in raw.items() if k}
            lower = {k.lower(): k for k in row}
            pts, applied = 0, 0
            for t in TESTS:
                key = lower.get(t.lower())
                try:
                    s = parse_score(row.get(key) if key else None)
                except ValueError as e:
                    sys.exit(f"{row.get(lower.get('organisation', ''), '?')}: {t}: {e}")
                if s is not None:
                    pts += s
                    applied += 1
            maxp = 2 * applied
            pct = round(100 * pts / maxp, 1) if maxp else 0.0
            row.update({
                "tests_applied": applied, "points": pts, "max_points": maxp,
                "percent": pct, "tier": tier_for(pct, applied, a.min_tests),
            })
            placement = (row.get(lower.get("placement", ""), "") or "").strip().upper()
            if placement in ("P1", "P2"):
                row["tier_note"] = f"Listed beside tier one by rule {placement}"
            rows.append(row)

    def sort_key(r):
        name = r.get("organisation") or r.get("Organisation") or ""
        raised = to_number(r.get("raised") or r.get("Raised"))
        return (r.get("record_type") or r.get("Record_type") or "",
                TIER_ORDER[r["tier"]], -r["percent"],
                -(raised if raised is not None else -1), name.lower())

    rows.sort(key=sort_key)
    fields = []
    for r in rows:
        for k in r:
            if k not in fields:
                fields.append(k)
    with open(a.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    counts = {}
    for r in rows:
        counts[r["tier"]] = counts.get(r["tier"], 0) + 1
    print(f"Scored {len(rows)} organisation(s) -> {a.out}")
    for t in TIER_ORDER:
        if t in counts:
            print(f"  {t}: {counts[t]}")


if __name__ == "__main__":
    main()
