#!/usr/bin/env python3
"""V11 homework H6 -- and a SENSITIVITY DEMONSTRATION for `A-080`.

WHAT THIS IS, AND WHAT IT IS EMPHATICALLY NOT
---------------------------------------------
V11 `[00:40:56]`-`[00:41:18]` sets one new, performable exercise: open the RSI/TDI
sub-graph full height and scroll back through it quickly to watch the oscillation
band switch between 80/40 and 60/20.

THAT EXERCISE CANNOT BE PERFORMED AS SET, because the lesson never states the RSI
lookback period (`A-080`) and neither does the Tier 2 seminar-notes PDF (`D-040`
step 2). Rendering ANY RSI requires choosing a period, and choosing one to make a
blocked exercise runnable is exactly what `D-030` forbids.

So this script does the ONLY honest thing available: it computes the lesson's own
printed range statistics at SEVERAL candidate periods AND ADOPTS NONE, in order to
show how much the answer moves. The output is a measurement of the COST of `A-080`,
not an answer to it.

  * NO PERIOD IS ADOPTED, HERE OR ANYWHERE IN V11's ARTIFACTS.
  * NO ROW OF THIS OUTPUT MAY BE CITED AS "the course's RSI behaviour".
  * NOTHING HERE CLOSES `A-080`, NARROWS IT, OR UNBLOCKS ANY `PT` TEST.
  * The periods swept are ARBITRARY SPREAD POINTS chosen to bracket plausible
    values. The inclusion of 13 is NOT an endorsement -- it is included precisely
    because it is the value a careless session would reach for (`A-080`'s named
    trap), so that its distance from its neighbours is visible.

Data: the `D-036a` HistData GBP/USD M1 corpus, aggregated to M15 -- the timeframe
V11 `[00:31:39]` names first. Window: `W-C'`, `D-035` DEVELOPMENT. Holdout never
opened.

usage: python3 rsi_period_sensitivity.py > ../data/rsi_period_sensitivity_output.txt
"""
from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "06_MANUAL_BACKTEST", "scripts"))
import mmm_lib as L                                          # noqa: E402

PERIODS = [5, 9, 13, 14, 21, 34]
WC_PRIME = (L.DEV_START, L.DEV_END)


def rsi(close: np.ndarray, n: int) -> np.ndarray:
    """Wilder's RSI, the standard construction. The PERIOD is the open question,
    not the formula -- V11 states no variant either, and this uses the ordinary one."""
    d = np.diff(close, prepend=close[0])
    up = np.where(d > 0, d, 0.0)
    dn = np.where(d < 0, -d, 0.0)
    au = np.empty_like(up)
    ad = np.empty_like(dn)
    au[:n] = up[:n].mean()
    ad[:n] = dn[:n].mean()
    a = 1.0 / n
    for i in range(n, len(close)):
        au[i] = au[i - 1] + a * (up[i] - au[i - 1])
        ad[i] = ad[i - 1] + a * (dn[i] - ad[i - 1])
    rs = np.divide(au, ad, out=np.full_like(au, np.inf), where=ad > 0)
    out = 100.0 - 100.0 / (1.0 + rs)
    out[:n] = np.nan
    return out


def main():
    print("=" * 78)
    print("V11 HOMEWORK H6 -- RSI PERIOD SENSITIVITY DEMONSTRATION")
    print("=" * 78)
    print("⚠ NO PERIOD IS ADOPTED. This output measures the COST of `A-080`,")
    print("  not the course's RSI behaviour. No row may be cited as doctrine.")
    print("  `A-080` is NOT closed, NOT narrowed, and NO test is unblocked.")
    print("=" * 78)
    qa, _ = L.qa_gate()
    print("QA gate : " + [l for l in qa.splitlines() if l.startswith("GATE:")][0])
    print(f"window  : W-C' {L.m2s(WC_PRIME[0])} -> {L.m2s(WC_PRIME[1])} (D-035 DEVELOPMENT)")
    print("timeframe: M15 (V11 [00:31:39] names 15-minute first). Arm A (corpus stamps).")
    print()

    b = L.load_m15("A").slice(*WC_PRIME)
    L.assert_development(b.tm, "H6 / arm A")
    c = b.c.astype(float)
    print(f"bars: {len(c)}")
    print()

    print("V11's printed thresholds (frame 31:25 / 37:30), measured at each period:")
    print()
    hdr = (f"{'period':>7} | {'>80':>7} {'<20':>7} | {'>50':>7} | {'in 70-30':>9} "
           f"| {'in 80-40':>9} {'in 60-20':>9} | {'mean':>6} {'sd':>6}")
    print(hdr)
    print("-" * len(hdr))
    rows = {}
    for n in PERIODS:
        r = rsi(c, n)
        v = r[~np.isnan(r)]
        f = lambda m: 100.0 * m.mean()
        rows[n] = dict(
            hi=f(v > 80), lo=f(v < 20), up=f(v > 50),
            norm=f((v <= 70) & (v >= 30)),
            bull=f((v <= 80) & (v >= 40)), bear=f((v <= 60) & (v >= 20)),
            mean=v.mean(), sd=v.std())
        d = rows[n]
        print(f"{n:>7} | {d['hi']:6.2f}% {d['lo']:6.2f}% | {d['up']:6.2f}% "
              f"| {d['norm']:8.2f}% | {d['bull']:8.2f}% {d['bear']:8.2f}% "
              f"| {d['mean']:6.2f} {d['sd']:6.2f}")

    print()
    print("=" * 78)
    print("  THE SPREAD -- this is the actual result")
    print("=" * 78)
    for key, label in [("hi", "time above 80 (V11's 'overextended')"),
                       ("lo", "time below 20 (V11's 'overextended', downside)"),
                       ("norm", "time inside the printed NORMAL range 70/30"),
                       ("bull", "time inside the printed BULL range 80/40"),
                       ("bear", "time inside the printed BEAR range 60/20")]:
        vals = [rows[n][key] for n in PERIODS]
        lo, hi = min(vals), max(vals)
        ratio = (hi / lo) if lo > 0 else float("inf")
        print(f"  {label:<48} {lo:6.2f}% .. {hi:6.2f}%   "
              f"spread {hi-lo:6.2f}pp  ratio {ratio:5.2f}x")

    print()
    print("  The 13 vs 14 pair is printed deliberately: they are ADJACENT candidate")
    print("  values and their difference is the floor on how much `A-080` matters.")
    for key in ("hi", "lo", "norm"):
        print(f"    {key:>5}:  n=13 -> {rows[13][key]:6.2f}%   n=14 -> {rows[14][key]:6.2f}%"
              f"   diff {abs(rows[13][key]-rows[14][key]):5.2f}pp")

    print()
    print("=" * 78)
    print("  WHAT THIS DOES NOT SHOW")
    print("=" * 78)
    print("  - It does not show which period the instructor used.")
    print("  - It does not test any V11 claim. The 80/40 <-> 60/20 SWITCH he asks")
    print("    students to watch for is a REGIME-TRANSITION claim; these are")
    print("    unconditional occupancy fractions and are not the same statistic.")
    print("  - It does not license reading '13 is close enough'. See `A-080`.")


if __name__ == "__main__":
    main()
