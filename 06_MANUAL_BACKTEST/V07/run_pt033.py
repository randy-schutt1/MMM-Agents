#!/usr/bin/env python3
"""PT-033 — the Hi-Lo ceiling, and the size of the untaught gap.

Runs exactly what 06_MANUAL_BACKTEST/PRE_REGISTERED/PT-033_hi_lo_ceiling_and_the_untaught_gap.md
pre-registered, in the order it pre-registered:

  1. re-hash both M15 files and print the digests
  2. build the four cells: 2 D-031 timezone arms x 2 day definitions
  3. compute and PRINT the nulls (N1, N1b) FIRST         <- COMMON_PROTOCOL.md §9 rule 1
  4. then compute the rule arm (O1, O2, O3)
  5. write raw results to data/pt033_results.json

No value is read from a rendering (E06 as restated by D-036a): every number here is parsed
from a checksummed CSV.

Usage:  python3 06_MANUAL_BACKTEST/V07/run_pt033.py
"""
import csv, hashlib, json, os, random, statistics, sys
from datetime import datetime, timedelta, date

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA = os.path.join(ROOT, "06_MANUAL_BACKTEST", "datasets", "HISTDATA_GBPUSD_M1")
OUT = os.path.join(ROOT, "06_MANUAL_BACKTEST", "V07", "data")

# ---- pre-registered constants (PT-033 §3, §4, §6, §7) -------------------------------
SEED = 20260812
ITERS = 1000
TARGET_PIPS = 50.0                      # the lesson's own exit
T_GRID = [10, 20, 30, 40, 50, 60, 80, 100]
X_GRID = [0, 2, 5, 10]
WIN_START = date(2013, 1, 6)            # W-C' DEVELOPMENT
WIN_END = date(2016, 6, 30)
MIN_BARS_PER_DAY = 4                    # mechanical drop rule, stated in §7
PIP = 0.0001


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load(path):
    """CSV -> list of (datetime, o, h, l, c). Timestamps are the file's own."""
    bars = []
    with open(path, newline="") as f:
        for row in csv.reader(f):
            if len(row) < 6:
                continue
            d, t = row[0], row[1]
            dt = datetime(int(d[0:4]), int(d[5:7]), int(d[8:10]), int(t[0:2]), int(t[3:5]))
            bars.append((dt, float(row[2]), float(row[3]), float(row[4]), float(row[5])))
    return bars


def day_key(dt, daydef):
    """Which trading day a bar belongs to."""
    if daydef == "D-MIDNIGHT":
        return dt.date()
    # D-SESSION: 17:00 -> 17:00 local. A bar at or after 17:00 belongs to the NEXT date.
    return (dt + timedelta(hours=7)).date()


def group_days(bars, daydef):
    days = {}
    for b in bars:
        if not (WIN_START <= b[0].date() <= WIN_END):
            continue
        days.setdefault(day_key(b[0], daydef), []).append(b)
    out = {}
    dropped = 0
    for k, v in days.items():
        if len(v) < MIN_BARS_PER_DAY:
            dropped += 1
            continue
        v.sort(key=lambda x: x[0])
        out[k] = v
    return out, dropped


def target_reached(bars, i, direction, entry, target_pips):
    """Did price reach entry -/+ target after bar i, within the same day?
    The entry bar itself is EXCLUDED (PT-033 §3, O2)."""
    if direction == "SHORT":
        goal = entry - target_pips * PIP
        return any(b[3] <= goal for b in bars[i + 1:])
    goal = entry + target_pips * PIP
    return any(b[2] >= goal for b in bars[i + 1:])


def rule_arm(days, X):
    """O2 (X=0 is the exact extreme) and O3 (X>0 tolerance)."""
    obs = []
    for k in sorted(days):
        bars = days[k]
        hod = max(b[2] for b in bars)
        lod = min(b[3] for b in bars)
        # SHORT: first bar whose high is within X pips of HOD
        i_s = next((i for i, b in enumerate(bars) if b[2] >= hod - X * PIP), None)
        # LONG: first bar whose low is within X pips of LOD
        i_l = next((i for i, b in enumerate(bars) if b[3] <= lod + X * PIP), None)
        if i_s is not None:
            obs.append((k, "SHORT", target_reached(bars, i_s, "SHORT", bars[i_s][2], TARGET_PIPS)))
        if i_l is not None:
            obs.append((k, "LONG", target_reached(bars, i_l, "LONG", bars[i_l][3], TARGET_PIPS)))
    return obs


def null_arm(days, rng, random_direction):
    """N1 / N1b — one iteration. Same n, same target, same deadline; entry bar randomized."""
    hits = 0
    n = 0
    for k in sorted(days):
        bars = days[k]
        if len(bars) < 2:
            continue
        for base_dir in ("SHORT", "LONG"):
            d = rng.choice(("SHORT", "LONG")) if random_direction else base_dir
            i = rng.randrange(0, len(bars) - 1)
            entry = bars[i][2] if d == "SHORT" else bars[i][3]
            hits += 1 if target_reached(bars, i, d, entry, TARGET_PIPS) else 0
            n += 1
    return hits / n if n else float("nan")


def wilson(k, n, z=1.96):
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5)
    return ((c - h) / d, (c + h) / d)


def pct_within(value, dist):
    return 100.0 * sum(1 for v in dist if v < value) / len(dist)


def main():
    os.makedirs(OUT, exist_ok=True)
    print("=" * 78)
    print("PT-033 — Hi-Lo ceiling and the untaught gap")
    print("=" * 78)

    files = {"A": os.path.join(DATA, "GBPUSD_M15_ARMA.csv"),
             "B": os.path.join(DATA, "GBPUSD_M15_ARMB.csv")}
    print("\n--- INPUT INTEGRITY (E06 / D-036a: numbers come from checksummed files) ---")
    digests = {}
    for arm, p in files.items():
        digests[arm] = sha256(p)
        print(f"  ARM {arm}: {os.path.basename(p)}  sha256={digests[arm]}")
    print(f"  window   : {WIN_START} -> {WIN_END}  (W-C' DEVELOPMENT, D-035)")
    print(f"  holdout  : 2016-07-01 -> 2017-12-29 — NOT ON DISK (D-036a). E23 cannot occur")
    print(f"  seed     : {SEED}   iterations: {ITERS}   target: {TARGET_PIPS:.0f} pips")

    results = {"seed": SEED, "iterations": ITERS, "target_pips": TARGET_PIPS,
               "window": [str(WIN_START), str(WIN_END)], "digests": digests,
               "T_grid": T_GRID, "X_grid": X_GRID, "cells": {}}

    cells = []
    for arm in ("A", "B"):
        bars = load(files[arm])
        for daydef in ("D-SESSION", "D-MIDNIGHT"):
            days, dropped = group_days(bars, daydef)
            cells.append((arm, daydef, days, dropped))

    # ---------- STEP 3: NULLS FIRST (COMMON_PROTOCOL.md §9 rule 1) ----------
    print("\n" + "=" * 78)
    print("STEP 1 of 2 — NULLS, COMPUTED AND PRINTED BEFORE THE RULE ARM")
    print("=" * 78)
    nulls = {}
    for arm, daydef, days, dropped in cells:
        key = f"{arm}|{daydef}"
        rng1 = random.Random(SEED)
        rng2 = random.Random(SEED)
        n1 = [null_arm(days, rng1, False) for _ in range(ITERS)]
        n1b = [null_arm(days, rng2, True) for _ in range(ITERS)]
        nulls[key] = {"N1": n1, "N1b": n1b}
        print(f"\n  cell {key}   days={len(days)}  dropped(<{MIN_BARS_PER_DAY} bars)={dropped}")
        for nm, dist in (("N1 matched random entry", n1), ("N1b random entry+direction", n1b)):
            print(f"    {nm:28} median={statistics.median(dist):.4f}  "
                  f"5-95%=[{sorted(dist)[int(.05*ITERS)]:.4f}, {sorted(dist)[int(.95*ITERS)-1]:.4f}]")

    # ---------- STEP 4: RULE ARM ----------
    print("\n" + "=" * 78)
    print("STEP 2 of 2 — RULE ARM")
    print("=" * 78)
    for arm, daydef, days, dropped in cells:
        key = f"{arm}|{daydef}"
        cell = {"n_days": len(days), "dropped_days": dropped}

        # O1 — the ceiling
        ranges = sorted(((max(b[2] for b in v) - min(b[3] for b in v)) / PIP) for v in days.values())
        cell["O1"] = {
            "median_range_pips": statistics.median(ranges),
            "p05": ranges[int(.05 * len(ranges))],
            "p95": ranges[int(.95 * len(ranges)) - 1],
            "frac_ge_T": {str(T): sum(1 for r in ranges if r >= T) / len(ranges) for T in T_GRID},
        }

        # O2 / O3
        cell["O3"] = {}
        for X in X_GRID:
            obs = rule_arm(days, X)
            hits = sum(1 for o in obs if o[2])
            n = len(obs)
            byday = {}
            for k, d, h in obs:
                byday[k] = byday.get(k, False) or h
            f_day = sum(1 for v in byday.values() if v) / len(byday)
            short = [o for o in obs if o[1] == "SHORT"]
            lng = [o for o in obs if o[1] == "LONG"]
            rec = {
                "n_obs": n, "hits": hits, "f50": hits / n,
                "ci95": wilson(hits, n),
                "f50_day": f_day, "n_days_scored": len(byday),
                "f50_short": sum(1 for o in short if o[2]) / len(short),
                "f50_long": sum(1 for o in lng if o[2]) / len(lng),
                "pct_within_N1": pct_within(hits / n, nulls[key]["N1"]),
                "pct_within_N1b": pct_within(hits / n, nulls[key]["N1b"]),
            }
            cell["O3"][str(X)] = rec
        cell["O2"] = cell["O3"]["0"]
        results["cells"][key] = cell

        o1, o2 = cell["O1"], cell["O2"]
        print(f"\n  cell {key}   days={len(days)}")
        print(f"    O1 daily range pips: median={o1['median_range_pips']:.1f}  "
              f"5-95%=[{o1['p05']:.1f}, {o1['p95']:.1f}]")
        print("    O1 frac(range >= T): " +
              "  ".join(f"{T}={o1['frac_ge_T'][str(T)]:.3f}" for T in T_GRID))
        print(f"    O2 X=0  f50={o2['f50']:.4f} [{o2['ci95'][0]:.4f},{o2['ci95'][1]:.4f}]  "
              f"n={o2['n_obs']}   f50_day={o2['f50_day']:.4f}")
        print(f"           short={o2['f50_short']:.4f}  long={o2['f50_long']:.4f}   "
              f"(pct within N1={o2['pct_within_N1']:.1f} — TAUTOLOGICAL, see PT-033 §4)")
        print("    O3 f50_day by tolerance X: " +
              "  ".join(f"X={X}:{cell['O3'][str(X)]['f50_day']:.3f}" for X in X_GRID))

    # ---------- verdict, applying §6 exactly ----------
    f_days = [results["cells"][f"{a}|{d}"]["O2"]["f50_day"]
              for a in ("A", "B") for d in ("D-SESSION", "D-MIDNIGHT")]
    if all(f >= 0.95 for f in f_days):
        verdict = "CONFIRMED AS TAUGHT"
    elif all(f < 0.50 for f in f_days):
        verdict = "CONTRADICTED AS TAUGHT"
    elif all(0.50 <= f < 0.95 for f in f_days):
        verdict = "OVERSTATED"
    else:
        verdict = "INDETERMINATE"
    results["verdict"] = verdict
    results["f50_day_all_cells"] = f_days

    print("\n" + "=" * 78)
    print(f"VERDICT (PT-033 §6, conjunctive across all four cells): {verdict}")
    print(f"  f50_day per cell: " + ", ".join(f"{f:.4f}" for f in f_days))
    print("=" * 78)

    # null medians summary, for the gap
    print("\n--- THE GAP THIS TEST EXISTS TO SIZE ---")
    for arm, daydef, days, dropped in cells:
        key = f"{arm}|{daydef}"
        nm = statistics.median(nulls[key]["N1"])
        rm = results["cells"][key]["O2"]["f50"]
        print(f"  {key:16} perfect-entry f50={rm:.4f}   random-entry f50={nm:.4f}   "
              f"gap={rm - nm:+.4f}")

    results["nulls_summary"] = {
        k: {n: {"median": statistics.median(v[n]),
                "p05": sorted(v[n])[int(.05 * ITERS)],
                "p95": sorted(v[n])[int(.95 * ITERS) - 1]} for n in ("N1", "N1b")}
        for k, v in nulls.items()}

    with open(os.path.join(OUT, "pt033_results.json"), "w") as f:
        json.dump(results, f, indent=1, sort_keys=True)
    print(f"\nwrote {os.path.join(OUT, 'pt033_results.json')}")


if __name__ == "__main__":
    main()
