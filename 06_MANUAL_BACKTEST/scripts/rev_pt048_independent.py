#!/usr/bin/env python3
"""REVIEWER's independent re-implementation of PT-048 (V20 R1).

Written from `06_MANUAL_BACKTEST/PRE_REGISTERED/PT-048_the_trend_pullback_magnitude.md`
ALONE, before `run_pt048.py` was opened. `mmm_lib` is used for data loading only.

Implements §3 (leg identification, P1/P2/P3), §4 (N1 matched-random baseline,
N3 fragility guard) and §5 (the decision rule AS WRITTEN — which references
N3 but NOT N1; that is the point under review).
"""
from __future__ import annotations

import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mmm_lib as L  # noqa: E402

PIP = L.PIP
BOX_END = L.BOX_END_MIN          # 03:00
DAY_END = L.DAY_END_MIN          # 17:00
LEG_MIN_PIPS = 40.0
LEG_MIN_BARS = 6
PIVOT_K = 3
BAND = (20.0, 25.0)
N1_ITER = 10000
BOOT_ITER = 10000


def wilson(k, n, z=1.959963984540054):
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - h) / d, (c + h) / d)


def boot_median_ci(x, rng, iters=BOOT_ITER):
    x = np.asarray(x, dtype=float)
    if len(x) == 0:
        return (float("nan"), float("nan"))
    idx = rng.integers(0, len(x), size=(iters, len(x)))
    meds = np.median(x[idx], axis=1)
    return (float(np.percentile(meds, 2.5)), float(np.percentile(meds, 97.5)))


def day_slices(b):
    """Post-box bars 03:00 -> 17:00 grouped by session day (§3)."""
    sd = L.session_day(b.tm)
    mod = L.minute_of_day(b.tm)
    m = (mod >= BOX_END) & (mod < DAY_END)
    sd, h, l, c, tm = sd[m], b.h[m], b.l[m], b.c[m], b.tm[m]
    order = np.argsort(tm, kind="stable")
    sd, h, l, c, tm = sd[order], h[order], l[order], c[order], tm[order]
    out = []
    for d in np.unique(sd):
        k = sd == d
        out.append((int(d), h[k], l[k], c[k], tm[k]))
    return out


def pivots(h, l, k=PIVOT_K):
    """§3.1 — a bar whose high is the max (or low the min) of the +/-k bars around it."""
    n = len(h)
    hi, lo = [], []
    for i in range(k, n - k):
        w = slice(i - k, i + k + 1)
        if h[i] == h[w].max():
            hi.append(i)
        if l[i] == l[w].min():
            lo.append(i)
    return sorted(hi), sorted(lo)


def legs_for_day(h, l):
    """§3.2/3.3 — swing-low -> swing-high (up) or high -> low (down),
    net displacement >= 40 pips, >= 6 bars."""
    hi, lo = pivots(h, l)
    marks = sorted([(i, 'H') for i in hi] + [(i, 'L') for i in lo])
    out = []
    for a in range(len(marks)):
        ia, ta = marks[a]
        for bb in range(a + 1, len(marks)):
            ib, tb = marks[bb]
            if tb == ta:
                continue
            if ib - ia + 1 < LEG_MIN_BARS:
                continue
            if ta == 'L' and tb == 'H':
                disp = (h[ib] - l[ia]) / PIP
                if disp >= LEG_MIN_PIPS:
                    out.append((ia, ib, +1))
            elif ta == 'H' and tb == 'L':
                disp = (h[ia] - l[ib]) / PIP
                if disp >= LEG_MIN_PIPS:
                    out.append((ia, ib, -1))
            break     # nearest opposite pivot only -> non-overlapping legs
    # keep non-overlapping legs, earliest first
    kept, last_end = [], -1
    for ia, ib, d in out:
        if ia >= last_end:
            kept.append((ia, ib, d))
            last_end = ib
    return kept


def measures_for_window(h, l, i0, i1, direction):
    """P1 swing retracements, P2 max adverse excursion, P3 largest 1-bar counter-move."""
    H, Ls = h[i0:i1 + 1], l[i0:i1 + 1]
    n = len(H)
    if n < 2:
        return [], None, None
    if direction > 0:
        run = np.maximum.accumulate(H)
        p2 = float(np.max((run - Ls) / PIP))
        p3 = float(np.max(np.maximum(0.0, (H[:-1] - Ls[1:]) / PIP)))
    else:
        run = np.minimum.accumulate(Ls)
        p2 = float(np.max((H - run) / PIP))
        p3 = float(np.max(np.maximum(0.0, (H[1:] - Ls[:-1]) / PIP)))
    # P1 — interior counter-swings
    hi, lo = pivots(H, Ls)
    p1 = []
    if direction > 0:
        for j in lo:
            prior = [H[x] for x in hi if x < j]
            if prior:
                p1.append(float((max(prior) - Ls[j]) / PIP))
    else:
        for j in hi:
            prior = [Ls[x] for x in lo if x < j]
            if prior:
                p1.append(float((H[j] - min(prior)) / PIP))
    return [v for v in p1 if v > 0], p2, p3


def collect(b, lo_tm, hi_tm):
    days = day_slices(b.slice(lo_tm, hi_tm))
    P1, P2, P3, legspec = [], [], [], []
    for d, h, l, c, tm in days:
        if len(h) < 2 * PIVOT_K + 2:
            continue
        for (i0, i1, dirn) in legs_for_day(h, l):
            a, p2, p3 = measures_for_window(h, l, i0, i1, dirn)
            if p2 is None:
                continue
            P1 += a
            P2.append(p2)
            P3.append(p3)
            legspec.append((d, i1 - i0 + 1, dirn))
    return P1, P2, P3, legspec, days


def n1_baseline(days, legspec, rng, iters=N1_ITER):
    """§4 N1 — for each leg draw a same-length window at a random start from the
    same day-hour pool, no leg condition, and compute the same measures."""
    pool = {d: (h, l) for d, h, l, c, tm in days}
    keys = list(pool)
    meds1, meds2, meds3 = [], [], []
    per_iter = max(1, iters // max(1, len(legspec))) if legspec else 0
    reps = max(1, min(iters, 2000))     # iterations over the whole leg set
    for _ in range(reps):
        a1, a2, a3 = [], [], []
        for (d, ln, dirn) in legspec:
            h, l = pool[keys[rng.integers(0, len(keys))]]
            if len(h) <= ln:
                continue
            s = int(rng.integers(0, len(h) - ln))
            p1, p2, p3 = measures_for_window(h, l, s, s + ln - 1, dirn)
            a1 += p1
            if p2 is not None:
                a2.append(p2)
                a3.append(p3)
        if a1:
            meds1.append(float(np.median(a1)))
        if a2:
            meds2.append(float(np.median(a2)))
            meds3.append(float(np.median(a3)))
    return meds1, meds2, meds3, reps


def summarise(vals, rng, label):
    v = np.asarray(vals, dtype=float)
    n = len(v)
    if n == 0:
        return {"n": 0}
    med = float(np.median(v))
    lo, hi = boot_median_ci(v, rng)
    k = int(((v >= BAND[0]) & (v <= BAND[1])).sum())
    wl, wh = wilson(k, n)
    # N3 leave-one-out: remove the single largest value
    v2 = np.sort(v)[:-1]
    med_drop = float(np.median(v2)) if len(v2) else float("nan")
    return {"label": label, "n": n, "median": med, "median_ci": [lo, hi],
            "iqr": [float(np.percentile(v, 25)), float(np.percentile(v, 75))],
            "frac_in_band": k / n, "frac_ci": [wl, wh], "k": k,
            "median_drop_largest": med_drop,
            "drop_shift": abs(med - med_drop)}


def main():
    rng_master = np.random.default_rng(L.SEED)
    WINDOWS = {"W-A": L.WINDOWS["W-A"], "W-B": L.WINDOWS["W-B"]}
    res = {}
    for arm in ("A", "B"):
        b = L.load_m15(arm, "development")
        for wname, (t0, t1) in WINDOWS.items():
            # Assert on the WINDOW actually read. Arm B's +1h shift relabels the
            # last DEVELOPMENT bars to 2016-07-01 wall-clock (`I-010` Q2), which
            # trips the seal on the full load even though W-A/W-B are 2014-2015.
            L.assert_development(b.slice(t0, t1).tm, f"REV PT-048 {wname}/{arm}")
            rng = np.random.default_rng(L.SEED)
            P1, P2, P3, legspec, days = collect(b, t0, t1)
            cell = {"arm": arm, "window": wname, "n_legs": len(legspec)}
            for nm, arr in (("P1", P1), ("P2", P2), ("P3", P3)):
                cell[nm] = summarise(arr, rng, nm)
            m1, m2, m3, reps = n1_baseline(days, legspec, rng)
            cell["N1"] = {
                "iterations_over_leg_set": reps,
                "P1_median_of_random_windows": float(np.median(m1)) if m1 else None,
                "P1_random_2_5": float(np.percentile(m1, 2.5)) if m1 else None,
                "P1_random_97_5": float(np.percentile(m1, 97.5)) if m1 else None,
                "P2_median_of_random_windows": float(np.median(m2)) if m2 else None,
                "P3_median_of_random_windows": float(np.median(m3)) if m3 else None,
            }
            res[f"{wname}/{arm}"] = cell
            print(f"\n### {wname} / arm {arm}   legs={len(legspec)}")
            for nm in ("P1", "P2", "P3"):
                s = cell[nm]
                if s.get("n"):
                    print(f"  {nm}: n={s['n']:6d} median={s['median']:6.2f} "
                          f"CI[{s['median_ci'][0]:.2f},{s['median_ci'][1]:.2f}] "
                          f"in-band={s['frac_in_band']:.3f} "
                          f"drop-largest shift={s['drop_shift']:.2f}")
            print(f"  N1 random-window P1 median = {cell['N1']['P1_median_of_random_windows']}"
                  f"  [{cell['N1']['P1_random_2_5']}, {cell['N1']['P1_random_97_5']}]")

    # ---- §5 decision rule AS WRITTEN (N3 referenced, N1 NOT referenced)
    prim = res["W-A/A"]["P1"]
    med, (clo, chi) = prim["median"], prim["median_ci"]
    n3 = []
    if not (BAND[0] <= res["W-A/A"]["P1"]["median"] <= BAND[1]) != \
       (not (BAND[0] <= res["W-A/B"]["P1"]["median"] <= BAND[1])):
        pass
    inA = BAND[0] <= res["W-A/A"]["P1"]["median"] <= BAND[1]
    inB = BAND[0] <= res["W-A/B"]["P1"]["median"] <= BAND[1]
    inWB = BAND[0] <= res["W-B/A"]["P1"]["median"] <= BAND[1]
    if inA != inB:
        n3.append("arms A/B disagree on band membership")
    if inA != inWB:
        n3.append("W-A/W-B disagree on band membership")
    for k, v in res.items():
        if v["n_legs"] < 30:
            n3.append(f"{k} has {v['n_legs']} legs (<30)")
    if prim["drop_shift"] > 2.0:
        n3.append(f"dropping largest P1 moves median by {prim['drop_shift']:.2f} (>2)")

    if n3:
        verdict = "FRAGILE (reported as a null)"
    elif BAND[0] <= med <= BAND[1] and BAND[0] <= clo and chi <= BAND[1]:
        verdict = "CONFIRMED"
    elif BAND[0] <= med <= BAND[1]:
        verdict = "PARTIAL"
    else:
        verdict = "REFUTED"

    base = res["W-A/A"]["N1"]["P1_median_of_random_windows"]
    print("\n" + "=" * 70)
    print(f"§5 VERDICT AS THE RULE IS WRITTEN : {verdict}")
    print(f"   primary P1 median = {med:.2f}  CI [{clo:.2f}, {chi:.2f}]  band {BAND}")
    print(f"   N3 conditions fired: {n3 if n3 else 'none'}")
    print(f"\n   N1 BASELINE (defined in §4, NEVER REFERENCED BY §5):")
    print(f"   random same-length windows give P1 median = {base:.2f}")
    if base is not None:
        print(f"   separation from the trend-leg median = {abs(med-base):.2f} pips")
        print(f"   -> the baseline lands INSIDE the claimed band too: "
              f"{BAND[0] <= base <= BAND[1]}")
    print("=" * 70)

    json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                     "rev_pt048_results.json"), "w"),
              indent=2, default=str)
    print("wrote rev_pt048_results.json")


if __name__ == "__main__":
    main()
