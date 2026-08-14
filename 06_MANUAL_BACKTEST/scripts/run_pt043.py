#!/usr/bin/env python3
"""PT-043 -- V15's DAILY restatement: does the session day close sit 25-50 pips off
its own high or low?

Runs the design pre-registered in
`06_MANUAL_BACKTEST/PRE_REGISTERED/PT-043_the_daily_close_twenty_five_to_fifty_off_the_extreme.md`,
which was committed at `1a3667e`, BEFORE this file existed and before any bar was read.

`COMMON_PROTOCOL.md` §9 rule 7: if this runner and that pre-registration disagree,
THE PRE-REGISTRATION GOVERNS and neither file is edited -- the disagreement is
reported in `BT_V15_0001.md`.

Everything here reads M1 bars parsed from the checksummed HistData corpus (`D-036a`),
DEVELOPMENT scope only (`D-035`). No value is read from a rendering of any kind.

usage:  python3 run_pt043.py > ../V15/data/pt043_output.txt
"""
from __future__ import annotations

import json
import numpy as np

import mmm_lib as L

SEED = 20260814            # PT-043 §5a, recorded before the run
ITERATIONS = 2000          # §5a N1 / §5 bootstrap
BAND = (25.0, 50.0)        # §3 -- inclusive at both ends
OFFSETS = [-120, -60, 60, 120]                       # §5a N2
N3_BANDS = [(0, 25), (25, 50), (50, 75), (75, 100), (100, np.inf)]   # §5a N3
BUCKETS_PER_DAY = 96       # §3a completeness, general form of C-6
WINDOWS = ["W-B", "W-A"]   # §4: W-B primary, W-A pre-registered replication
ARMS = ["A", "B"]


# ----------------------------------------------------------------- construction

def session_days(b: L.Bars, offset_min: int = 0):
    """Included session days and their per-day M1 index slices.

    Inclusion (§3a): all 96 fifteen-minute buckets of the day's 24-hour span present.
    `offset_min` carries the §5a N2 circular clock shift: the price path is untouched
    and every boundary label moves, so the null is scored under the same rule.
    Exclusions are counted and named, never dropped quietly.
    """
    tm = b.tm - int(offset_min)
    sd = L.session_day(tm)
    order = np.argsort(sd, kind="stable")
    sd_s = sd[order]
    uniq, starts, counts = np.unique(sd_s, return_index=True, return_counts=True)

    kept, excluded = [], []
    for d, s, n in zip(uniq, starts, counts):
        idx = order[s:s + n]
        idx = idx[np.argsort(tm[idx], kind="stable")]
        end = (d * L.DAY) + L.DAY_END_MIN
        start = end - L.DAY
        nb = len(np.unique((tm[idx] - start) // 15))
        if nb == BUCKETS_PER_DAY:
            kept.append((int(d), idx))
        else:
            excluded.append(dict(day=L.day2s(d), buckets=int(nb)))
    return kept, excluded


def day_table(b: L.Bars, offset_min: int = 0):
    """Per included day: high, low, close, and the two distances in pips.

    Returns (days, hi, lo, close, d_hi, d_lo, idx_list, excluded).
    `idx_list` is retained so N1 can draw a pseudo-close from inside the SAME day.
    """
    kept, excluded = session_days(b, offset_min)
    days, hi, lo, cl, idxs = [], [], [], [], []
    for d, idx in kept:
        days.append(d)
        hi.append(float(b.h[idx].max()))
        lo.append(float(b.l[idx].min()))
        cl.append(float(b.c[idx][-1]))
        idxs.append(idx)
    hi = np.asarray(hi); lo = np.asarray(lo); cl = np.asarray(cl)
    d_hi = (hi - cl) / L.PIP
    d_lo = (cl - lo) / L.PIP
    return np.asarray(days), hi, lo, cl, d_hi, d_lo, idxs, excluded


def in_band(x, band=BAND):
    return (x >= band[0]) & (x <= band[1])


def outcomes(d_hi, d_lo):
    """§5: O1 = min in band (V15's 'or'); O2 = both in band (V10's 'and');
    O3 = max in band (descriptive)."""
    mn = np.minimum(d_hi, d_lo)
    mx = np.maximum(d_hi, d_lo)
    return dict(
        O1=float(in_band(mn).mean()),
        O2=float((in_band(d_hi) & in_band(d_lo)).mean()),
        O3=float(in_band(mx).mean()),
    )


# ----------------------------------------------------------------- controls

def n1_random_close(b: L.Bars, hi, lo, idxs, rng):
    """§5a N1: pseudo-close drawn uniformly from M1 bars INSIDE the same day.

    H and L are held fixed. Only WHERE IN THE DAY the observation is taken varies.
    """
    o1 = np.empty(ITERATIONS); o2 = np.empty(ITERATIONS); o3 = np.empty(ITERATIONS)
    lens = np.array([len(i) for i in idxs])
    flat = np.concatenate(idxs)
    offs = np.concatenate([[0], np.cumsum(lens)[:-1]])
    for k in range(ITERATIONS):
        pick = flat[offs + (rng.random(len(lens)) * lens).astype(np.int64)]
        c = b.c[pick]
        dh = (hi - c) / L.PIP
        dl = (c - lo) / L.PIP
        r = outcomes(dh, dl)
        o1[k], o2[k], o3[k] = r["O1"], r["O2"], r["O3"]
    return o1, o2, o3


# ----------------------------------------------------------------- verdict

def verdict(p_hat, m):
    """§6, applied verbatim. Returns (label, reason)."""
    d = p_hat - m
    if p_hat < 0.10:
        return "CONTRADICTED AS STATED", f"p_hat={p_hat:.4f} < 0.10 against the speaker's 'always' (clause a)"
    if p_hat >= 0.60 and d >= 0.10:
        return "SUPPORTED", f"p_hat={p_hat:.4f} >= 0.60 and beats N1 by {d:+.4f} >= +0.10"
    if (p_hat >= 0.40 and d >= 0.10) or (p_hat >= 0.60 and d < 0.10):
        return "PARTIALLY SUPPORTED", f"p_hat={p_hat:.4f}, N1 delta {d:+.4f}"
    return "NOT SUPPORTED", f"p_hat={p_hat:.4f}, N1 delta {d:+.4f}"


def dist_block(name, x):
    q = np.percentile(x, [10, 25, 50, 75, 90])
    ci = L.boot_ci(x, iterations=ITERATIONS, seed=SEED)
    return (f"    {name:<18} n={len(x):5d}  median={q[2]:8.2f}  "
            f"IQR=[{q[1]:7.2f},{q[3]:7.2f}]  D1={q[0]:7.2f} D9={q[4]:7.2f}  "
            f"median95CI=[{ci[0]:.2f},{ci[1]:.2f}]")


# ----------------------------------------------------------------- main

def main():
    rep, sha = L.qa_gate("development")
    print("=" * 78)
    print("PT-043 -- the DAILY close, 25-50 pips off the high or low")
    print("=" * 78)
    print(f"QA gate (development scope): PASS   manifest sha256={sha}")
    print(f"seed={SEED}  iterations={ITERATIONS}  band={BAND[0]:.0f}-{BAND[1]:.0f} pips inclusive")
    print("scope = DEVELOPMENT only (D-035). No D-044 year is read.")
    print()

    results = {}
    for arm in ARMS:
        b_all = L.load_m1(arm)                       # defaults to DEVELOPMENT scope
        for w in WINDOWS:
            b = L.window(b_all, w)                   # re-asserts the holdout
            L.assert_development(b.tm, f"{w} / arm {arm}")
            days, hi, lo, cl, d_hi, d_lo, idxs, excl = day_table(b)
            n = len(days)
            obs = outcomes(d_hi, d_lo)

            rng = np.random.default_rng(SEED)
            c1, c2, c3 = n1_random_close(b, hi, lo, idxs, rng)
            m1, m2, m3 = float(np.median(c1)), float(np.median(c2)), float(np.median(c3))

            key = f"{w}/{arm}"
            print("-" * 78)
            print(f"WINDOW {w}   ARM {arm}")
            print("-" * 78)
            print(f"  n = {n} complete session days; {len(excl)} excluded for incomplete sessions")
            if excl:
                named = ", ".join(f"{d['day']} ({d['buckets']}/96)" for d in excl[:12])
                more = "" if len(excl) <= 12 else f", +{len(excl)-12} more"
                print(f"    excluded: {named}{more}")
            print()
            print("  OUTCOMES (observed) vs N1 random-intraday-close control (median of 2000)")
            for oid, o, c, m in (("O1 min in band  (V15 'or')", obs["O1"], c1, m1),
                                 ("O2 both in band (V10 'and')", obs["O2"], c2, m2),
                                 ("O3 max in band  (descriptive)", obs["O3"], c3, m3)):
                k = int(round(o * n))
                wl, wh = L.wilson_ci(k, n)
                p5, p95 = np.percentile(c, [5, 95])
                print(f"    {oid:<30} p_hat={o:.4f}  Wilson95=[{wl:.4f},{wh:.4f}]  "
                      f"N1 median={m:.4f} [P5={p5:.4f},P95={p95:.4f}]  delta={o-m:+.4f}")
            print()
            print("  D1 -- distributions, pips")
            print(dist_block("d_hi (H-C)", d_hi))
            print(dist_block("d_lo (C-L)", d_lo))
            print(dist_block("min(d_hi,d_lo)", np.minimum(d_hi, d_lo)))
            print(dist_block("day range H-L", d_hi + d_lo))
            print()
            rng2 = np.argsort(-(d_hi + d_lo))[:5]
            print("  D2 -- five largest-range days (reported, NOT excluded)")
            for i in rng2:
                print(f"    {L.day2s(days[i])}  range={d_hi[i]+d_lo[i]:7.2f}  "
                      f"d_hi={d_hi[i]:7.2f}  d_lo={d_lo[i]:7.2f}")
            print()
            print("  N3 -- where the closes actually sit (DESCRIPTIVE, changes no verdict)")
            mn = np.minimum(d_hi, d_lo)
            for a, bb in N3_BANDS:
                f = float(((mn >= a) & (mn <= bb)).mean()) if np.isinf(bb) else \
                    float(((mn >= a) & (mn <= bb)).mean())
                lab = f"[{a:.0f},{'inf' if np.isinf(bb) else f'{bb:.0f}'}]"
                print(f"    min(d_hi,d_lo) in {lab:<10} {f:.4f}")
            print()

            n2 = {}
            print("  N2 -- day-boundary offset control on O1")
            for off in OFFSETS:
                _, h2, l2, c2_, dh2, dl2, _, _ = day_table(b, off)
                r = outcomes(dh2, dl2)
                n2[off] = r["O1"]
                print(f"    offset {off:+4d} min   O1={r['O1']:.4f}   delta_vs_17:00={r['O1']-obs['O1']:+.4f}")
            print()

            v1, why1 = verdict(obs["O1"], m1)
            v2, why2 = verdict(obs["O2"], m2)
            close = sum(1 for off in OFFSETS if abs(n2[off] - obs["O1"]) <= 0.05)
            downgraded = False
            if v1 == "SUPPORTED" and close >= 3:
                v1 = "PARTIALLY SUPPORTED"
                downgraded = True
            print(f"  VERDICT O1 ({'HEADLINE' if key == 'W-B/A' else 'reported'}): {v1}")
            print(f"    reason: {why1}")
            if downgraded:
                print(f"    ** DOWNGRADED one step by clause (c): {close}/4 N2 offsets within +/-0.05 **")
            print(f"  VERDICT O2 (secondary): {v2}")
            print(f"    reason: {why2}")
            print()

            results[key] = dict(n=n, n_excluded=len(excl), observed=obs,
                                n1_median=dict(O1=m1, O2=m2, O3=m3),
                                n2_O1={str(k): v for k, v in n2.items()},
                                verdict_O1=v1, verdict_O2=v2,
                                downgraded_by_clause_c=downgraded,
                                median_day_range_pips=float(np.median(d_hi + d_lo)))

    print("=" * 78)
    print("HEADLINE (PT-043 §6): W-B, Arm A, O1")
    h = results["W-B/A"]
    print(f"  {h['verdict_O1']}   p_hat={h['observed']['O1']:.4f}  "
          f"N1={h['n1_median']['O1']:.4f}  n={h['n']}")
    print("=" * 78)
    print()
    print("RESULTS_JSON_BEGIN")
    print(json.dumps(results, indent=2, sort_keys=True))
    print("RESULTS_JSON_END")


if __name__ == "__main__":
    main()
