#!/usr/bin/env python3
"""PT-033 INDEPENDENT CROSS-CHECK — second data source, second vendor.

D-034 names the Yahoo Finance chart API as the project's CORROBORATION source (never a
substitute primary). This script checks PT-033's O1 -- the daily-range distribution -- from
a completely different vendor, whose bars this project has never aggregated and whose day
boundary is its own.

What it can and cannot show:
  CAN  : whether the SHAPE of the daily-range distribution reproduces off a second vendor.
  CANNOT: anything about price LEVELS. D-036a records that the cross-vendor level offset is
          unmeasurable for 2013-2016 because FXCM serves no data there. Only distance
          claims travel.

Usage:  python3 06_MANUAL_BACKTEST/V07/crosscheck_pt033_second_source.py
"""
import json, os, statistics, urllib.request
from datetime import datetime, timezone

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
URL = ("https://query1.finance.yahoo.com/v8/finance/chart/GBPUSD=X"
       "?period1=1357430400&period2=1467331200&interval=1d")   # 2013-01-06 -> 2016-07-01
PIP = 0.0001
T_GRID = [10, 20, 30, 40, 50, 60, 80, 100]


def main():
    os.makedirs(OUT, exist_ok=True)
    req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    raw = urllib.request.urlopen(req, timeout=60).read()
    j = json.loads(raw)
    r = j["chart"]["result"][0]
    ts = r["timestamp"]
    q = r["indicators"]["quote"][0]
    rows = []
    for i, t in enumerate(ts):
        h, l = q["high"][i], q["low"][i]
        if h is None or l is None:
            continue
        d = datetime.fromtimestamp(t, timezone.utc).date()
        if not (datetime(2013, 1, 6).date() <= d <= datetime(2016, 6, 30).date()):
            continue
        rng = (h - l) / PIP
        if rng <= 0:
            continue
        rows.append((str(d), rng))
    rows.sort()
    with open(os.path.join(OUT, "pt033_yahoo_daily.json"), "w") as f:
        json.dump({"url": URL, "n": len(rows), "rows": rows}, f, indent=1)

    rng = sorted(x[1] for x in rows)
    n = len(rng)
    print("=" * 78)
    print("PT-033 CROSS-CHECK — Yahoo Finance daily GBP/USD, 2013-01-06 -> 2016-06-30")
    print("=" * 78)
    print(f"  bars (days) with a usable range : {n}")
    print(f"  median daily range              : {statistics.median(rng):.1f} pips")
    print(f"  5-95%                           : [{rng[int(.05*n)]:.1f}, {rng[int(.95*n)-1]:.1f}]")
    print("  frac(range >= T): " + "  ".join(
        f"{T}={sum(1 for x in rng if x >= T)/n:.3f}" for T in T_GRID))
    print("\n  PT-033 primary, for comparison (HistData M1 -> M15):")
    prim = json.load(open(os.path.join(OUT, "pt033_results.json")))
    for cell in ("A|D-SESSION", "A|D-MIDNIGHT"):
        o1 = prim["cells"][cell]["O1"]
        print(f"    {cell:14} median={o1['median_range_pips']:.1f}  "
              f"5-95%=[{o1['p05']:.1f}, {o1['p95']:.1f}]  "
              f"frac>=50={o1['frac_ge_T']['50']:.3f}")
    print("\n  Levels are NOT compared, and cannot be (D-036a).")


if __name__ == "__main__":
    main()
