#!/usr/bin/env python3
"""PT-048 -- V20's "the trend move will contain 20 to 25 pip pullbacks".

Runs the test pre-registered in
`06_MANUAL_BACKTEST/PRE_REGISTERED/PT-048_the_trend_pullback_magnitude.md`,
committed at bb526f1 BEFORE this file existed.

IF THIS RUNNER AND THAT FILE DISAGREE, THAT FILE GOVERNS. Neither is edited; the
disagreement is reported in `BT_V20_0001.md`.
"""
import json
import os
import sys
from math import sqrt

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mmm_lib as M                                                   # noqa: E402

PIVOT_K = 3            # swing pivot = extreme of the +/-3 bars around it
LEG_MIN_PIPS = 40.0    # twice the top of the claimed band
LEG_MIN_BARS = 6
BAND = (20.0, 25.0)
ITERS = 10000
BOOT = 20000


def wilson(k, n, z=1.96):
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return 100 * (c - h), 100 * (c + h)


def boot_median(x, seed, iters=BOOT):
    if len(x) < 2:
        return (float("nan"), float("nan"))
    rng = np.random.default_rng(seed)
    m = [np.median(rng.choice(x, len(x), True)) for _ in range(iters)]
    return float(np.percentile(m, 2.5)), float(np.percentile(m, 97.5))


def pivots(h, l, k=PIVOT_K):
    """Indices that are the max high / min low of the +/-k bars around them."""
    n = len(h)
    hi, lo = [], []
    for t in range(k, n - k):
        if h[t] == h[t - k:t + k + 1].max():
            hi.append(t)
        if l[t] == l[t - k:t + k + 1].min():
            lo.append(t)
    return hi, lo


def legs_of_day(h, l):
    """Trend legs: swing low -> swing high (up) or high -> low (down). PT-048 §3."""
    hi, lo = pivots(h, l)
    out = []
    for a in lo:                                    # up-legs
        for b in hi:
            if b - a >= LEG_MIN_BARS and (h[b] - l[a]) / M.PIP >= LEG_MIN_PIPS:
                out.append((a, b, +1))
                break
    for a in hi:                                    # down-legs
        for b in lo:
            if b - a >= LEG_MIN_BARS and (h[a] - l[b]) / M.PIP >= LEG_MIN_PIPS:
                out.append((a, b, -1))
                break
    return out


def measures(h, l, a, b, d, k=PIVOT_K):
    """P1 swing retracement, P2 max adverse excursion, P3 largest 1-bar counter-move.

    CORRECTED 2026-08-15 -- V20 R1 `M1`, `REVIEW_INDEX.md` item 332.

    The interior counter-swing detector was hardcoded to a +/-1 local extreme. PT-048
    §3.1 defines a swing pivot as "a bar whose high is the maximum (or low the minimum)
    of the +/-3 bars around it", and P1 is defined over "interior counter-swings" -- so
    the SAME scale governs. `PIVOT_K` was honoured for the leg endpoints and bypassed
    here, which inflated n and dragged the median down into the claimed band.

    THE PRE-REGISTRATION GOVERNS AND IS NOT EDITED. This is the runner being brought
    into line with it (`PT-048` header; `COMMON_PROTOCOL.md` §9 rule 7).
    """
    hh, ll = h[a:b + 1], l[a:b + 1]
    n = len(hh)
    p1 = []
    if d > 0:
        run = np.maximum.accumulate(hh)
        for t in range(k, n - k):
            if ll[t] == ll[t - k:t + k + 1].min():        # swing low at +/-k
                p1.append((run[t] - ll[t]) / M.PIP)
        p2 = float(np.max((run - ll) / M.PIP))
        p3 = float(np.max([(hh[t - 1] - ll[t]) / M.PIP for t in range(1, n)]))
    else:
        run = np.minimum.accumulate(ll)
        for t in range(k, n - k):
            if hh[t] == hh[t - k:t + k + 1].max():        # swing high at +/-k
                p1.append((hh[t] - run[t]) / M.PIP)
        p2 = float(np.max((hh - run) / M.PIP))
        p3 = float(np.max([(hh[t] - ll[t - 1]) / M.PIP for t in range(1, n)]))
    p1 = [v for v in p1 if v > 0]
    return p1, max(0.0, p2), max(0.0, p3)


def cell(arm, win):
    m15 = M.window(M.load_m15(arm), win)
    days = M.build_days(m15, offset_min=0, require_full=True)
    post = (m15.mod >= M.BOX_END_MIN) & (m15.mod < M.DAY_END_MIN)
    P1, P2, P3 = [], [], []
    nlegs = 0
    daykeys = sorted(days["sd"].tolist())
    for day in daykeys:
        m = post & (m15.sd == day)
        h, l = m15.h[m], m15.l[m]
        if len(h) < LEG_MIN_BARS + 2 * PIVOT_K + 2:
            continue
        for a, b, d in legs_of_day(h, l):
            nlegs += 1
            p1, p2, p3 = measures(h, l, a, b, d)
            P1.extend(p1); P2.append(p2); P3.append(p3)
    r = dict(arm=arm, window=win, n_days=int(len(days)), n_legs=nlegs,
             n_p1=len(P1), n_p2=len(P2), n_p3=len(P3))
    for name, arr in (("P1", P1), ("P2", P2), ("P3", P3)):
        a_ = np.asarray(arr, float)
        if len(a_) < 2:
            r[name] = dict(insufficient=True)
            continue
        k = int(((a_ >= BAND[0]) & (a_ <= BAND[1])).sum())
        lo, hi = boot_median(a_, M.SEED)
        wl, wh = wilson(k, len(a_))
        r[name] = dict(n=len(a_), median=round(float(np.median(a_)), 2),
                       iqr=[round(float(np.percentile(a_, 25)), 2),
                            round(float(np.percentile(a_, 75)), 2)],
                       median_ci=[round(lo, 2), round(hi, 2)],
                       frac_in_band=round(100 * k / len(a_), 1),
                       frac_in_band_wilson=[round(wl, 1), round(wh, 1)])
    return r, np.asarray(P1, float)


def n1_baseline(arm, win, seed=None):
    """Matched random windows: same lengths, no leg condition. PT-048 §4."""
    m15 = M.window(M.load_m15(arm), win)
    days = M.build_days(m15, offset_min=0, require_full=True)
    post = (m15.mod >= M.BOX_END_MIN) & (m15.mod < M.DAY_END_MIN)
    rng = np.random.default_rng(M.SEED if seed is None else seed)
    lens, pool = [], []
    for day in sorted(days["sd"].tolist()):
        m = post & (m15.sd == day)
        h, l = m15.h[m], m15.l[m]
        if len(h) < LEG_MIN_BARS + 2 * PIVOT_K + 2:
            continue
        pool.append((h, l))
        for a, b, d in legs_of_day(h, l):
            lens.append(b - a)
    if not lens or not pool:
        return dict(insufficient=True)
    out = []
    for _ in range(min(ITERS, 2000)):
        h, l = pool[rng.integers(len(pool))]
        L = lens[rng.integers(len(lens))]
        if len(h) <= L + 1:
            continue
        a = int(rng.integers(0, len(h) - L - 1)); b = a + L
        d = 1 if h[b] >= h[a] else -1
        p1, _, _ = measures(h, l, a, b, d)
        out.extend(p1)
    a_ = np.asarray(out, float)
    if len(a_) < 2:
        return dict(insufficient=True)
    k = int(((a_ >= BAND[0]) & (a_ <= BAND[1])).sum())
    return dict(n=len(a_), median=round(float(np.median(a_)), 2),
                frac_in_band=round(100 * k / len(a_), 1))


def main():
    M.qa_gate()
    res, prim_p1 = {}, None
    for arm in ("A", "B"):
        for win in ("W-A", "W-B"):
            r, p1 = cell(arm, win)
            key = f"{arm}|{win}"
            res[key] = r
            if key == "A|W-A":
                prim_p1 = p1
            print(f"\n=== {key}  days={r['n_days']}  legs={r['n_legs']} ===")
            for nm in ("P1", "P2", "P3"):
                d = r[nm]
                if d.get("insufficient"):
                    print(f"  {nm}: INSUFFICIENT"); continue
                print(f"  {nm}: n={d['n']:>5} median={d['median']:>6.2f} "
                      f"ci={d['median_ci']}  IQR={d['iqr']}  "
                      f"in[20,25]={d['frac_in_band']}% Wilson{d['frac_in_band_wilson']}")

    res["N1_baseline_A_W-A"] = n1_baseline("A", "W-A")
    print("\nN1 matched-random baseline (A|W-A):", res["N1_baseline_A_W-A"])

    # ---- SWING-SCALE SENSITIVITY, reported always. Added 2026-08-15, V20 R1 M1.
    # N3's four conditions do NOT bracket the interior swing scale, and that scale was
    # verdict-determining. It is therefore published on every run rather than left to a
    # reviewer to discover. REPORTING ONLY -- k=PIVOT_K remains the pre-registered value
    # and is the only one the verdict is computed from.
    print("\nSWING-SCALE SENSITIVITY (reporting only; the verdict uses k=PIVOT_K=%d):" % PIVOT_K)
    sens = {}
    m15 = M.window(M.load_m15("A"), "W-A")
    days = M.build_days(m15, offset_min=0, require_full=True)
    post = (m15.mod >= M.BOX_END_MIN) & (m15.mod < M.DAY_END_MIN)
    for k in (1, 2, 3, 4):
        vals = []
        for day in sorted(days["sd"].tolist()):
            mm = post & (m15.sd == day)
            h, l = m15.h[mm], m15.l[mm]
            if len(h) < LEG_MIN_BARS + 2 * PIVOT_K + 2:
                continue
            for a, b, d in legs_of_day(h, l):
                if b - a >= 2 * k + 1:
                    p1, _, _ = measures(h, l, a, b, d, k=k)
                    vals.extend(p1)
        v = np.asarray(vals, float)
        if len(v) < 2:
            continue
        lo, hi = boot_median(v, M.SEED)
        inb = BAND[0] <= float(np.median(v)) <= BAND[1]
        sens[f"k={k}"] = dict(n=len(v), median=round(float(np.median(v)), 2),
                              ci=[round(lo, 2), round(hi, 2)], median_in_band=inb)
        star = "  <-- PRE-REGISTERED" if k == PIVOT_K else ""
        print(f"  k={k}: n={len(v):>5} median={np.median(v):>6.2f} "
              f"ci=[{lo:.2f}, {hi:.2f}] in_band={inb}{star}")
    res["swing_scale_sensitivity"] = sens

    # ---- N3 fragility guard, PT-048 §4
    fired = []
    def inband(v): return BAND[0] <= v <= BAND[1]
    prim = res["A|W-A"]["P1"]
    for key in ("A|W-A", "A|W-B", "B|W-A", "B|W-B"):
        d = res[key]["P1"]
        if d.get("insufficient"):
            fired.append(f"{key}: insufficient"); continue
        if inband(d["median"]) != inband(prim["median"]):
            fired.append(f"{key}: band-membership disagrees with primary")
        if res[key]["n_legs"] < 30:
            fired.append(f"{key}: n_legs<30 ({res[key]['n_legs']})")
    if prim_p1 is not None and len(prim_p1) > 2:
        drop = np.sort(prim_p1)[:-1]
        if abs(float(np.median(drop)) - prim["median"]) > 2.0:
            fired.append("primary: leave-one-out moves the median > 2 pips")

    # ---- §5 decision rule
    if fired:
        verdict = "FRAGILE"
    elif inband(prim["median"]) and inband(prim["median_ci"][0]) and inband(prim["median_ci"][1]):
        verdict = "CONFIRMED"
    elif inband(prim["median"]):
        verdict = "PARTIAL"
    else:
        lo, hi = prim["median_ci"]
        verdict = "REFUTED" if (hi < BAND[0] or lo > BAND[1]) else "PARTIAL"

    out = dict(test="PT-048", seed=M.SEED, band=list(BAND),
               primary_cell="A|W-A|P1", n3_fired=fired, verdict=verdict, cells=res)
    print("\nN3 fired:", fired if fired else "NO")
    print("VERDICT:", verdict)
    dst = os.path.join(os.path.dirname(__file__), "..", "V20", "data", "pt048_results.json")
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, "w") as f:
        json.dump(out, f, indent=2)
    print("wrote", os.path.normpath(dst))


if __name__ == "__main__":
    main()
