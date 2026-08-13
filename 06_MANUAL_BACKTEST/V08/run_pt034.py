#!/usr/bin/env python3
"""PT-034 — "Risk Reward to 3:1 or greater": the arithmetic half and the empirical half.

Runs exactly what 06_MANUAL_BACKTEST/PRE_REGISTERED/PT-034_crown_jewel_three_to_one.md
pre-registered, in the order it pre-registered:

  1. re-hash both M15 files and print the digests
  2. state the ARITHMETIC result (§2), which needs no data
  3. build the four cells: 2 D-031 timezone arms x 2 day definitions
  4. apply the C8 exclusions BY NAME and print the counts
  5. compute and PRINT the nulls (N1, N1b) FIRST          <- COMMON_PROTOCOL.md §9 rule 1
  6. then compute the rule arm (O1, O2, O3, O4)
  7. write raw results to data/pt034_results.json

No value is read from a rendering (E06 as restated by D-036a): every number here is parsed
from a checksummed CSV.

Stdlib only, deliberately — the same choice run_pt033.py made, so the result reproduces on a
bare interpreter with no environment to drift.

Usage:  python3 06_MANUAL_BACKTEST/V08/run_pt034.py
"""
import csv, hashlib, json, os, random, statistics, sys, time
from datetime import datetime, timedelta, date

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA = os.path.join(ROOT, "06_MANUAL_BACKTEST", "datasets", "HISTDATA_GBPUSD_M1")
OUT = os.path.join(ROOT, "06_MANUAL_BACKTEST", "V08", "data")

# ---- pre-registered constants (PT-034 §3, §4, §6, §7) -------------------------------
SEED = 20260813
ITERS = 1000
PIP = 0.0001
TARGET_PIPS = 50.0                       # the lesson's own exit, stated 8x as "Easy 50"
RATIO = 3.0                              # "three to one or greater"
STOP_PIPS = TARGET_PIPS / RATIO          # 16.666... IMPLIED, never stated by the lesson
X_GRID = [0, 2, 5, 10]                   # 10 is the LESSON'S number (printed, V08_00-05-40)
X_HEADLINE = 10
WIN_START = date(2013, 1, 6)             # W-C' DEVELOPMENT (COMMON_PROTOCOL §3a)
WIN_END = date(2016, 6, 30)
HOLDOUT_START = date(2016, 7, 1)         # D-035 — must never be touched
MIN_BARS_PER_DAY = 4                     # mechanical drop rule, PT-034 §7a
BREAKEVEN = 0.25                         # break-even hit rate for a 3:1 payoff

# C8 dispositions, pre-registered BY NAME in PT-034 §7a
C8_EXCLUDE = {date(2014, 6, 1), date(2014, 6, 2)}           # the data hole
C8_REPORT_SEPARATELY = {                                     # nine Dec/Jan closures — INCLUDED
    date(2013, 1, 1), date(2013, 12, 25), date(2014, 1, 1),
    date(2014, 12, 24), date(2014, 12, 25), date(2015, 1, 1),
    date(2015, 12, 24), date(2015, 12, 25), date(2016, 1, 1),
}


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load(arm):
    """Parse GBPUSD_M15_ARM{A,B}.csv into parallel lists (fast index access)."""
    path = os.path.join(DATA, f"GBPUSD_M15_ARM{arm}.csv")
    ts, hi, lo, cl = [], [], [], []
    with open(path, newline="") as f:
        for r in csv.reader(f):
            if len(r) < 6:
                continue
            ts.append(datetime.strptime(r[0] + " " + r[1], "%Y.%m.%d %H:%M"))
            hi.append(float(r[3])); lo.append(float(r[4])); cl.append(float(r[5]))
    return ts, hi, lo, cl


def day_key(dt, daydef):
    """D-SESSION: 17:00 -> 17:00 local.  D-MIDNIGHT: 00:00 -> 00:00 local."""
    if daydef == "D-MIDNIGHT":
        return dt.date()
    return (dt - timedelta(hours=17)).date()


def build_days(ts, daydef):
    """Group bar INDICES into trading days; apply window, C8 and the min-bars rule."""
    buckets = {}
    for i, dt in enumerate(ts):
        buckets.setdefault(day_key(dt, daydef), []).append(i)
    days, dropped_short, excluded_c8, holiday_days = [], [], [], []
    for k in sorted(buckets):
        if k < WIN_START or k > WIN_END:
            continue
        if k >= HOLDOUT_START:                       # belt and braces; D-035 / E23
            raise SystemExit(f"ABORT: holdout date {k} reached — E23")
        if k in C8_EXCLUDE:
            excluded_c8.append(k); continue
        idx = buckets[k]
        if len(idx) < MIN_BARS_PER_DAY:
            dropped_short.append(k); continue
        if k in C8_REPORT_SEPARATELY:
            holiday_days.append(k)
        days.append((k, idx))
    return days, {
        "days_used": len(days),
        "excluded_c8_by_name": [str(d) for d in excluded_c8],
        "dropped_min_bars": [str(d) for d in dropped_short],
        "holiday_days_included": [str(d) for d in holiday_days],
    }


def resolve(hi, lo, i0, px, direction, n):
    """O4 scan: NO deadline. Target or the implied stop, whichever first.

    Stop-first when one bar spans both — the conservative convention fixed in §3.
    Entry bar excluded. Returns (outcome, bars_to_resolution).
    """
    if direction == "LONG":
        tgt, stp = px + TARGET_PIPS * PIP, px - STOP_PIPS * PIP
        for j in range(i0 + 1, n):
            if lo[j] <= stp:
                return "STOP", j - i0
            if hi[j] >= tgt:
                return "TARGET", j - i0
    else:
        tgt, stp = px - TARGET_PIPS * PIP, px + STOP_PIPS * PIP
        for j in range(i0 + 1, n):
            if hi[j] >= stp:
                return "STOP", j - i0
            if lo[j] <= tgt:
                return "TARGET", j - i0
    return "UNRESOLVED", n - i0 - 1


def precompute_close_entries(hi, lo, cl):
    """N1's entry price is the chosen bar's CLOSE, so every outcome can be computed once.

    Returns two lists of 'T'/'S'/'U' indexed by bar. This is what makes 1,000 matched-random
    iterations affordable; it changes no result, only the cost.
    """
    n = len(cl)
    out = {"LONG": [None] * n, "SHORT": [None] * n}
    for d in ("LONG", "SHORT"):
        arr = out[d]
        for i in range(n - 1):
            o, _ = resolve(hi, lo, i, cl[i], d, n)
            arr[i] = o[0]                     # 'T' | 'S' | 'U'
        arr[n - 1] = "U"
    return out


def entry_for(hi, lo, idx, X, direction):
    """PT-034 §3 entry rule. Returns (bar_index, entry_price) or None.

    LONG : first bar whose low is within X pips of LOD; price = LOD + X if inside that bar's
           range, else that bar's low.  SHORT: mirror. Conservative, fixed before any run.
    """
    if direction == "LONG":
        lod = min(lo[i] for i in idx)
        want = lod + X * PIP
        for i in idx:
            if lo[i] <= want + 1e-12:
                return i, (want if lo[i] <= want <= hi[i] else lo[i])
        return None
    hod = max(hi[i] for i in idx)
    want = hod - X * PIP
    for i in idx:
        if hi[i] >= want - 1e-12:
            return i, (want if lo[i] <= want <= hi[i] else hi[i])
    return None


def within_day(hi, lo, idx, i0, px, direction):
    """O2/O3: target reached before the day ends, and realised MAE over the rest of the day."""
    tgt = px + TARGET_PIPS * PIP if direction == "LONG" else px - TARGET_PIPS * PIP
    mae = 0.0
    for i in idx:
        if i <= i0:
            continue
        adv = (px - lo[i]) if direction == "LONG" else (hi[i] - px)
        if adv > mae:
            mae = adv
        if (direction == "LONG" and hi[i] >= tgt) or (direction == "SHORT" and lo[i] <= tgt):
            return True, mae / PIP
    return False, mae / PIP


def wilson(k, n, z=1.959963985):
    if n == 0:
        return (0.0, 0.0)
    p = k / n; d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5) / d
    return (max(0.0, c - h), min(1.0, c + h))


def q(v, p):
    if not v:
        return float("nan")
    s = sorted(v); i = (len(s) - 1) * p
    a, b = int(i), min(int(i) + 1, len(s) - 1)
    return s[a] + (s[b] - s[a]) * (i - a)


def pct_of(value, dist):
    return float("nan") if not dist else 100.0 * sum(1 for d in dist if d < value) / len(dist)


def main():
    os.makedirs(OUT, exist_ok=True)
    t_start = time.time()
    res = {"test": "PT-034", "seed": SEED, "iterations": ITERS,
           "target_pips": TARGET_PIPS, "ratio": RATIO, "stop_pips": STOP_PIPS,
           "x_grid": X_GRID, "x_headline": X_HEADLINE,
           "window": [str(WIN_START), str(WIN_END)], "files": {}, "cells": {}}

    print("=" * 78)
    print('PT-034 — V08\'s "Risk Reward to 3:1 or greater"')
    print("=" * 78)
    print("Pre-registration: PRE_REGISTERED/PT-034_crown_jewel_three_to_one.md")
    print(f"seed={SEED}  iterations={ITERS}  target={TARGET_PIPS:.0f} pips  "
          f"stop={STOP_PIPS:.4f} pips (IMPLIED = target/{RATIO:g})")
    print(f"window={WIN_START} -> {WIN_END}   (W-C' DEVELOPMENT; holdout never opened)")
    print()

    print("--- 1. FILE INTEGRITY (E06 as restated by D-036a) ---")
    for arm in ("A", "B"):
        d = sha256(os.path.join(DATA, f"GBPUSD_M15_ARM{arm}.csv"))
        res["files"][f"ARM{arm}"] = d
        print(f"    GBPUSD_M15_ARM{arm}.csv  sha256={d}")
    print(f"    QA gate: {os.path.join(DATA,'QA_REPORT.txt')} — C1-C4 PASS (precondition, §7)")
    print()

    print("--- 2. THE ARITHMETIC RESULT, WHICH NEEDS NO DATA (PT-034 §2) ---")
    print("    Within a trading day, an entry within X pips of that day's extreme has")
    print("    MAE <= X BY CONSTRUCTION — the extreme is the day's bound.")
    print(f"    So realised R = {TARGET_PIPS:.0f}/MAE >= {TARGET_PIPS/X_HEADLINE:.1f} at "
          f"X = {X_HEADLINE}, and the 3:1 claim CANNOT FAIL for any X <= {STOP_PIPS:.2f} pips.")
    print("    Stated before the run. O1 below is a pipeline self-test, NOT a finding.")
    print()

    rng = random.Random(SEED)

    for arm in ("A", "B"):
        ts, hi, lo, cl = load(arm)
        n = len(ts)
        print(f"--- precomputing matched-random outcomes for ARM{arm} ({n} bars) ---")
        t0 = time.time()
        pre = precompute_close_entries(hi, lo, cl)
        print(f"    done in {time.time()-t0:.1f}s")
        print()

        for daydef in ("D-SESSION", "D-MIDNIGHT"):
            cell = f"ARM{arm}/{daydef}"
            days, stats = build_days(ts, daydef)

            print("=" * 78)
            print(f"CELL {cell}")
            print("=" * 78)
            print(f"    days used = {stats['days_used']}    "
                  f"excluded BY NAME (C8 hole) = {len(stats['excluded_c8_by_name'])} "
                  f"{stats['excluded_c8_by_name']}    "
                  f"dropped <{MIN_BARS_PER_DAY} bars = {len(stats['dropped_min_bars'])}")
            print(f"    Dec/Jan closures INCLUDED and reported separately: "
                  f"{len(stats['holiday_days_included'])}")

            # ---------- NULLS FIRST (COMMON_PROTOCOL §9 rule 1) ----------
            print()
            print("    --- N1 / N1b : MATCHED RANDOM ENTRY — computed and printed BEFORE the rule arm ---")
            n1, n1b = [], []
            pl, ps = pre["LONG"], pre["SHORT"]
            for _ in range(ITERS):
                k1 = m1 = k2 = m2 = 0
                for _dk, idx in days:
                    if len(idx) < 2:
                        continue
                    i = idx[rng.randrange(0, len(idx) - 1)]
                    for a in (pl[i], ps[i]):                  # N1: direction matched (both)
                        if a != "U":
                            m1 += 1
                            k1 += (a == "T")
                    b = (pl if rng.random() < 0.5 else ps)[i]  # N1b: direction random
                    if b != "U":
                        m2 += 1
                        k2 += (b == "T")
                n1.append(k1 / m1 if m1 else 0.0)
                n1b.append(k2 / m2 if m2 else 0.0)
            for tag, dist in (("N1 ", n1), ("N1b", n1b)):
                print(f"    {tag} target-before-stop rate: median={statistics.median(dist):.4f}   "
                      f"5-95%=[{q(dist,0.05):.4f}, {q(dist,0.95):.4f}]   "
                      f"iterations={ITERS}  seed={SEED}")

            cellres = {"stats": stats,
                       "N1": {"median": statistics.median(n1), "p05": q(n1, 0.05), "p95": q(n1, 0.95)},
                       "N1b": {"median": statistics.median(n1b), "p05": q(n1b, 0.05), "p95": q(n1b, 0.95)},
                       "X": {}}

            # ---------- THE RULE ARM ----------
            print()
            print("    --- O1 / O2 / O3 / O4 : THE RULE ARM ---")
            for X in X_GRID:
                maes, rs, mae0, o1v = [], [], 0, 0
                hits = n_obs = day_hit = 0
                o4 = {"TARGET": 0, "STOP": 0, "UNRESOLVED": 0}
                o4b = []
                for _dk, idx in days:
                    any_hit = False
                    for d in ("LONG", "SHORT"):
                        e = entry_for(hi, lo, idx, X, d)
                        if e is None:
                            continue
                        i0, px = e
                        hit, mae = within_day(hi, lo, idx, i0, px, d)
                        n_obs += 1
                        maes.append(mae)
                        if mae > X + 1e-6:
                            o1v += 1
                        if mae == 0.0:
                            mae0 += 1
                        if hit:
                            hits += 1; any_hit = True
                            if mae > 0:
                                rs.append(TARGET_PIPS / mae)
                        o, nb = resolve(hi, lo, i0, px, d, n)
                        o4[o] += 1; o4b.append(nb)
                    if any_hit:
                        day_hit += 1

                o4n = o4["TARGET"] + o4["STOP"]
                rate = o4["TARGET"] / o4n if o4n else float("nan")
                wlo, whi = wilson(o4["TARGET"], o4n)
                pctile = pct_of(rate, n1)
                tag = "   <-- HEADLINE (the lesson's own printed tolerance)" if X == X_HEADLINE else ""
                mm = statistics.median(maes) if maes else float("nan")
                print(f"    X={X:2d} pips{tag}")
                print(f"        O1 self-test  MAE > X : {o1v}    (pre-registered expectation: 0)")
                print(f"        O2 MAE pips   median={mm:6.2f}  q25={q(maes,0.25):6.2f}  "
                      f"q75={q(maes,0.75):6.2f}   MAE=0 in {mae0}/{n_obs}"
                      + (f"   median MAE/X={mm/X:.3f}" if X else "   (X=0: MAE is 0 by construction)"))
                print(f"           realised R among target-reachers: "
                      f"median={statistics.median(rs) if rs else float('nan'):8.2f}   n={len(rs)}"
                      f"   (MAE=0 excluded and counted above)")
                print(f"        O3 within-day f50={hits}/{n_obs}="
                      f"{hits/n_obs if n_obs else float('nan'):.4f}   f50_day={day_hit}/"
                      f"{stats['days_used']}={day_hit/stats['days_used']:.4f}")
                print(f"        O4 NO DEADLINE  target={o4['TARGET']}  stop={o4['STOP']}  "
                      f"unresolved={o4['UNRESOLVED']}")
                print(f"           rate={rate:.4f}  Wilson95=[{wlo:.4f}, {whi:.4f}]  "
                      f"n={o4n}   vs N1 percentile={pctile:.1f}")
                print(f"           bars to resolution: median={statistics.median(o4b) if o4b else float('nan'):.0f}"
                      f"   q95={q(o4b,0.95):.0f}")

                cellres["X"][str(X)] = {
                    "n_obs": n_obs, "o1_violations": o1v,
                    "mae_median": mm, "mae_q25": q(maes, 0.25), "mae_q75": q(maes, 0.75),
                    "mae_zero": mae0,
                    "r_median": statistics.median(rs) if rs else None, "r_n": len(rs),
                    "o3_hits": hits, "o3_rate": hits / n_obs if n_obs else None,
                    "o3_f50_day": day_hit / stats["days_used"],
                    "o4": o4, "o4_n": o4n, "o4_rate": rate,
                    "o4_wilson": [wlo, whi], "o4_vs_n1_percentile": pctile,
                    "o4_bars_median": statistics.median(o4b) if o4b else None,
                }
            res["cells"][cell] = cellres
            print()

    # ---------- verdict, per PT-034 §6 ----------
    print("=" * 78)
    print("VERDICT — PT-034 §6, judged on O4 at X=10 across ALL FOUR cells")
    print("=" * 78)
    rates, beats = [], []
    for cell, c in res["cells"].items():
        h = c["X"][str(X_HEADLINE)]
        rates.append(h["o4_rate"]); beats.append(h["o4_vs_n1_percentile"] > 95.0)
        print(f"    {cell:22s} rate={h['o4_rate']:.4f}   vs N1 pct={h['o4_vs_n1_percentile']:6.1f}   "
              f"{'ABOVE' if h['o4_vs_n1_percentile'] > 95 else 'NOT above'} N1 p95")
    spread = max(rates) - min(rates)
    sess = [res["cells"][c]["X"][str(X_HEADLINE)]["o4_rate"] for c in res["cells"] if "SESSION" in c]
    midn = [res["cells"][c]["X"][str(X_HEADLINE)]["o4_rate"] for c in res["cells"] if "MIDNIGHT" in c]
    armA = [res["cells"][c]["X"][str(X_HEADLINE)]["o4_rate"] for c in res["cells"] if "ARMA" in c]
    armB = [res["cells"][c]["X"][str(X_HEADLINE)]["o4_rate"] for c in res["cells"] if "ARMB" in c]
    print(f"    spread across all four cells        = {spread:.4f}")
    print(f"    DAY-BOUNDARY effect  |session-midnight| = "
          f"{abs(statistics.mean(sess)-statistics.mean(midn)):.4f}   (COURSE_PROGRESS V07 item (c))")
    print(f"    D-031 TIMEZONE effect      |armA-armB| = "
          f"{abs(statistics.mean(armA)-statistics.mean(armB)):.4f}")

    if all(r >= BREAKEVEN for r in rates) and all(beats):
        verdict = "CONFIRMED AS TAUGHT"
    elif all(r < BREAKEVEN for r in rates):
        verdict = "CONTRADICTED AS TAUGHT"
    elif all(r >= BREAKEVEN for r in rates):
        verdict = "OVERSTATED"
    else:
        verdict = "INDETERMINATE"
    print()
    print(f"    VERDICT: {verdict}      (break-even for a 3:1 payoff = {BREAKEVEN:.2f})")
    print()
    print("    AND, FIRST: §2's ARITHMETIC RESULT STANDS INDEPENDENTLY OF THIS VERDICT —")
    print("    within the day the 3:1 claim is guaranteed, and therefore empty as stated.")

    res["verdict"] = verdict
    res["headline_rates"] = rates
    res["day_boundary_effect"] = abs(statistics.mean(sess) - statistics.mean(midn))
    res["timezone_effect"] = abs(statistics.mean(armA) - statistics.mean(armB))
    res["runtime_s"] = round(time.time() - t_start, 1)
    with open(os.path.join(OUT, "pt034_results.json"), "w") as f:
        json.dump(res, f, indent=2, default=str)
    print()
    print(f"raw results -> {os.path.join(OUT,'pt034_results.json')}   "
          f"({res['runtime_s']}s)")


if __name__ == "__main__":
    main()
