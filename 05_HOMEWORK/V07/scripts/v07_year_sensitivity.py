#!/usr/bin/env python3
"""V07 HOMEWORK H2 — does "over a year" give the same answer whichever year you pick?

The assignment [00:12:09] says "How many times OVER A YEAR". This script runs H1's count
one calendar year at a time across the DEVELOPMENT block, to see whether the instruction is
stable. If it is not, the instruction under-specifies the answer, and that is worth the
student knowing before he flashcards anything.

Usage:  python3 05_HOMEWORK/V07/scripts/v07_year_sensitivity.py
"""
import json, os, sys
from datetime import date
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import v07_homework as H

OUT = H.OUT

def main():
    os.makedirs(OUT, exist_ok=True)
    res = {}
    print("=" * 78)
    print('V07 HOMEWORK H2 — "over a year": which year?')
    print("=" * 78)
    for arm in ("A", "B"):
        bars = H.load_m15(os.path.join(H.DATA, f"GBPUSD_M15_ARM{arm}.csv"))
        for dd in ("D-SESSION", "D-MIDNIGHT"):
            print(f"\n  cell {arm}|{dd}")
            for y in (2013, 2014, 2015):
                days = H.group(bars, dd, date(y, 1, 1), date(y, 12, 31))
                r = H.h1_count(days)
                res[f"{arm}|{dd}|{y}"] = {k: r[k] for k in ("n_days", "hit_days", "frac")}
                print(f"    {y}: days={r['n_days']:4}  offered a 50-pip run on "
                      f"{r['hit_days']:4}  frac={r['frac']:.3f}")
            # 2016 is a half year -- reported as such, never blended
            days = H.group(bars, dd, date(2016, 1, 1), date(2016, 6, 30))
            r = H.h1_count(days)
            res[f"{arm}|{dd}|2016H1"] = {k: r[k] for k in ("n_days", "hit_days", "frac")}
            print(f"    2016H1 (HALF YEAR, not comparable): days={r['n_days']:4}  "
                  f"hits={r['hit_days']:4}  frac={r['frac']:.3f}")
            fr = [res[f"{arm}|{dd}|{y}"]["frac"] for y in (2013, 2014, 2015)]
            print(f"    spread across the three FULL years: "
                  f"{min(fr):.3f} .. {max(fr):.3f}   range={max(fr)-min(fr):.3f}")
    with open(os.path.join(OUT, "v07_year_sensitivity.json"), "w") as f:
        json.dump(res, f, indent=1, sort_keys=True)
    print(f"\nwrote {os.path.join(OUT, 'v07_year_sensitivity.json')}")

if __name__ == "__main__":
    main()
