#!/usr/bin/env python3
"""`PT-036` — V10's two quantitative structure claims.

    M1  "peak formation high to peak formation low 600 to 1000 pips is the range"
        V10 [00:14:09]-[00:14:17], [00:14:38]
    M2  "the dealer will end always 25 to 50 pips off of the high and 25 to 50 pips
        off of the low"   V10 [00:13:41]-[00:13:52]

THE PRE-REGISTRATION GOVERNS THIS FILE, NOT THE OTHER WAY ROUND.
`COMMON_PROTOCOL.md` §9 rule 7: where this runner and `PT-036` disagree, the
pre-registration wins, neither is edited, and the disagreement is reported in
`BT_V10_0001`. That rule has fired twice already (`BT_V08_0001`, `BT_V09_0001`),
both times against the runner. This runner therefore prints its decision inputs
rather than its decisions, so the verdict is applied by a human against §6's table.

WHY THERE IS NO BARRIER RACE ANYWHERE IN THIS FILE
--------------------------------------------------
`REVIEW_INDEX.md` open item 80 escalates a censoring bias that arises when a far
target and a near stop race to a day-end horizon. `PT-036` §2 asserts the design
admits no such geometry. That assertion is CHECKED here, not merely repeated:
`censored` is counted and must be 0, and §7b.1 makes a non-zero count VOID both
measures. Every observation is a completed week or a completed Friday session.

M1 IS TESTABLE ONLY BECAUSE V10 DEFINES ITS OWN ANCHOR
------------------------------------------------------
`peak formation high/low` = the week's extreme, V10 [01:13:58]-[01:14:06]:
"the highest point on a chart within the week, or the lowest point on the chart
within the week". That is the COURSE's definition (`A-010`), not this agent's.
Without it `M1` would be `D-030`-blocked like the safety trade (`PT-036` §2).
"""
from __future__ import annotations

import sys
import os
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from mmm_lib import (  # noqa: E402
    PIP, load_m15, qa_gate, verify_against_committed, assert_development,
    wilson_ci, m2s, header, nlabel,
)
import mmm_week as W  # noqa: E402

SEED = 20260813          # `PT-036` §4 — fixed in the pre-registration
ITERS = 10_000           # `PT-036` §4
BAND_LO, BAND_HI = 600.0, 1000.0        # M1
FRI_LO, FRI_HI = 25.0, 50.0             # M2
WEEKDAYS = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri"]


# ---------------------------------------------------------------- helpers

def boot_prop_ci(flags: np.ndarray, iterations=ITERS, seed=SEED):
    """Bootstrap 95% CI on a proportion. Reported alongside every rate (`E24`)."""
    rng = np.random.default_rng(seed)
    n = len(flags)
    if n == 0:
        return (float("nan"), float("nan"))
    idx = rng.integers(0, n, size=(iterations, n))
    props = flags[idx].mean(axis=1)
    return float(np.percentile(props, 2.5)), float(np.percentile(props, 97.5))


def rate_line(k: int, n: int, label: str) -> str:
    if n == 0:
        return f"  {label:<44} n=0"
    flags = np.zeros(n); flags[:k] = 1.0
    lo, hi = boot_prop_ci(flags)
    w_lo, w_hi = wilson_ci(k, n)
    return (f"  {label:<44} {k:5d}/{n:<5d} = {100*k/n:6.2f}%"
            f"   boot95 [{100*lo:5.2f}, {100*hi:5.2f}]"
            f"   wilson95 [{100*w_lo:5.2f}, {100*w_hi:5.2f}]  {nlabel(n)}")


def dist_block(x: np.ndarray, unit="pips") -> list[str]:
    q = np.percentile(x, [5, 25, 50, 75, 95])
    return [
        f"    n        {len(x)}",
        f"    min      {x.min():8.1f} {unit}",
        f"    p05      {q[0]:8.1f}",
        f"    p25      {q[1]:8.1f}",
        f"    MEDIAN   {q[2]:8.1f}",
        f"    p75      {q[3]:8.1f}",
        f"    p95      {q[4]:8.1f}",
        f"    max      {x.max():8.1f}",
        f"    mean     {x.mean():8.1f}",
    ]


def weekday_of(tm: np.ndarray) -> np.ndarray:
    """Weekday index with Sunday=0, matching `mmm_week._weekday`."""
    return W._weekday(tm)


def sessions_for_week(m15, wk_row, arm):
    """Split one week's M15 bars into SESSION DAYS on the arm's own clock.

    A session day runs 17:00 -> 17:00 (`mmm_lib` convention C-1), which is what
    makes 'Friday' a well-defined object here: the Friday session is the one whose
    session-day label is a Friday.
    """
    a = wk_row["anchor"]
    nxt = a + 5 * 24 * 60 + 2 * 24 * 60          # generous upper bound; masked below
    m = (m15.tm >= a) & (m15.tm < nxt)
    idx = np.where(m)[0]
    if len(idx) == 0:
        return {}
    tm = m15.tm[idx]
    # session day index relative to the week anchor: 0=Sun, 1=Mon, ...
    day = ((tm - a) // (24 * 60)).astype(int)
    out = {}
    for d in np.unique(day):
        if d > 5:
            continue
        sel = idx[day == d]
        out[int(d)] = sel
    return out


# ---------------------------------------------------------------- main

def run_arm(arm: str, out: list[str]):
    m15 = load_m15(arm)
    weeks_all = W.build_weeks(arm, m15)
    out.append("")
    out.append(f"================ ARM {arm} ================")
    for ln in W.census_lines(weeks_all):
        out.append("  " + ln)

    # ---- exclusions, exactly as PT-036 §7a pre-registers them
    wk = W.usable(weeks_all, drop_truncated=True)     # drops data hole + truncated
    n_hole = int(weeks_all["is_data_hole"].sum())
    n_trunc = int(weeks_all["is_truncated"].sum())
    out.append("")
    out.append(f"  EXCLUSIONS (PT-036 §7a, pre-registered by name):")
    out.append(f"    data hole  week of {W.DATA_HOLE_WEEK}          EXCLUDED  ({n_hole})")
    out.append(f"    truncated  week of {W.TRUNCATED_FINAL_WEEK}          EXCLUDED  ({n_trunc})")
    out.append(f"    Dec/Jan closure weeks                     INCLUDED, reported separately "
               f"({int(wk['is_closure'].sum())})")
    out.append(f"    usable weeks for M1                       n = {len(wk)}")

    # ================================================== M1
    out.append("")
    out.append("-- M1 : WEEKLY RANGE, peak formation high to peak formation low --")
    out.append("   V10 [00:14:09] '600 to 1000 pips is the range'")
    out.append("   anchor definition: V10 [01:14:06], the week's extreme (A-010)")
    rng_pips = wk["range_pips"].to_numpy()
    assert np.all(np.isfinite(rng_pips)), "non-finite weekly range"
    out.append("")
    out += dist_block(rng_pips)
    k = int(((rng_pips >= BAND_LO) & (rng_pips <= BAND_HI)).sum())
    out.append("")
    out.append(rate_line(k, len(rng_pips), "O1  weeks with range in [600,1000] pips"))
    out.append(rate_line(int((rng_pips >= BAND_LO).sum()), len(rng_pips),
                         "    weeks with range >= 600 pips"))
    out.append(rate_line(int((rng_pips >= 300).sum()), len(rng_pips),
                         "    (context) weeks with range >= 300 pips"))

    # O2 scale diagnostic — pre-registered in §3, reported whatever the result
    med = float(np.median(rng_pips))
    out.append("")
    out.append("  O2  SCALE DIAGNOSTIC (pre-registered; does NOT change M1's verdict)")
    out.append(f"      median observed / 800 (band midpoint) = {med/800:.3f}")
    out.append(f"      claim overshoots median by a factor of  {800/med:.2f}x")
    pct600 = float((rng_pips < BAND_LO).mean() * 100)
    out.append(f"      600 pips sits at the {pct600:.2f}th percentile of the observed distribution")
    out.append(f"      pip-vs-point check: 600 'points' on a 5-digit feed = 60 pips;")
    out.append(f"        weeks with range in [60,100] pips = "
               f"{int(((rng_pips>=60)&(rng_pips<=100)).sum())}/{len(rng_pips)}")

    # closure weeks reported separately, as pre-registered
    cl = wk[wk["is_closure"]]["range_pips"].to_numpy()
    if len(cl):
        out.append("")
        out.append(f"  Dec/Jan closure weeks reported separately: n={len(cl)}, "
                   f"median {np.median(cl):.1f} pips, "
                   f"in-band {int(((cl>=BAND_LO)&(cl<=BAND_HI)).sum())}")

    # N4 — shifted boundary control
    out.append("")
    out.append("  N4  SHIFTED-BOUNDARY CONTROL (+24h, Monday 17:00 anchors)")
    try:
        shifted = W.weeks_from_offset(m15, 24 * 60)
        srng = shifted["range_pips"].to_numpy()
        sk = int(((srng >= BAND_LO) & (srng <= BAND_HI)).sum())
        out.append(f"      shifted roster n={len(srng)}  median {np.median(srng):.1f} pips  "
                   f"in-band {sk}/{len(srng)} = {100*sk/max(len(srng),1):.2f}%")
        out.append(f"      TRUE roster    n={len(rng_pips)}  median {med:.1f} pips  "
                   f"in-band {k}/{len(rng_pips)} = {100*k/len(rng_pips):.2f}%")
        out.append(f"      median difference (true - shifted) = "
                   f"{med - float(np.median(srng)):+.1f} pips")
        out.append("      READING: if these are indistinguishable, M1 measures how far GBP/USD")
        out.append("               travels in five days, NOT anything about week structure.")
    except Exception as e:                                  # pragma: no cover
        out.append(f"      N4 UNAVAILABLE: {e!r}")

    # ================================================== M2
    out.append("")
    out.append("-- M2 : THE FRIDAY CLOSE, 25 to 50 pips off BOTH extremes --")
    out.append("   V10 [00:13:41] 'the dealer will end always 25 to 50 pips off of the high")
    out.append("                   and 25 to 50 pips off of the low'")

    rows = []
    censored = 0
    for _, r in wk.iterrows():
        sess = sessions_for_week(m15, r, arm)
        for d, sel in sess.items():
            if len(sel) == 0:
                continue
            h = float(m15.h[sel].max())
            lo = float(m15.l[sel].min())
            c = float(m15.c[sel][np.argmax(m15.tm[sel])])
            if not np.isfinite(h) or not np.isfinite(lo) or not np.isfinite(c):
                censored += 1
                continue
            rows.append(dict(week=r["week"], dow=d, dow_name=WEEKDAYS[d],
                             hi=h, lo=lo, close=c,
                             d_high=(h - c) / PIP, d_low=(c - lo) / PIP,
                             rng=(h - lo) / PIP,
                             ends_weekday=r["ends_weekday"],
                             is_closure=bool(r["is_closure"]),
                             n_bars=len(sel)))
    S = pd.DataFrame(rows)

    # §7b.1 — the design assertion, CHECKED not assumed
    out.append("")
    out.append(f"  §7b.1 CENSORING CHECK  censored/unresolved observations = {censored}")
    out.append("        (PT-036 §2 asserts the design admits ZERO; non-zero VOIDS both measures)")
    assert censored == 0, "PT-036 §7b.1: censored observation found — test is VOID"

    # Thursday-closing weeks have no Friday: excluded from M2 by name, per §7a
    thu_weeks = sorted(set(wk[wk["ends_weekday"] == "Thu"]["week"]))
    fri = S[(S["dow_name"] == "Fri")].copy()
    fri = fri[~fri["week"].isin(thu_weeks)]
    out.append("")
    out.append(f"  M2 EXCLUSIONS: Thursday-closing weeks have no Friday session — "
               f"excluded by name: {thu_weeks if thu_weeks else 'none'}")
    out.append(f"  usable Fridays for M2  n = {len(fri)}   "
               f"(exclusion count {len(thu_weeks)})")

    dh = fri["d_high"].to_numpy(); dl = fri["d_low"].to_numpy()
    joint = (dh >= FRI_LO) & (dh <= FRI_HI) & (dl >= FRI_LO) & (dl <= FRI_HI)
    out.append("")
    out.append("  O3  Friday close distance from the day's HIGH (pips)")
    out += dist_block(dh)
    out.append("")
    out.append("  O3  Friday close distance from the day's LOW (pips)")
    out += dist_block(dl)
    out.append("")
    out.append(rate_line(int(joint.sum()), len(fri),
                         "O3  JOINT: both distances in [25,50]  <-- M2a"))
    out.append(rate_line(int(((dh >= FRI_LO) & (dh <= FRI_HI)).sum()), len(fri),
                         "    marginal: distance from HIGH in [25,50]"))
    out.append(rate_line(int(((dl >= FRI_LO) & (dl <= FRI_HI)).sum()), len(fri),
                         "    marginal: distance from LOW  in [25,50]"))
    out.append("")
    out.append(f"  LITERAL 'always' reading: {int(joint.sum())}/{len(fri)} — the claim as spoken")
    out.append("    requires 100%. Reported so a reader may apply the strict standard (§6).")

    # O4 — derived, LABELLED
    out.append("")
    out.append("  O4  DERIVED IMPLICATION — THIS INFERENCE IS THE AGENT'S, NOT THE LESSON'S")
    out.append("      (V10_INTERPRETATION.md Q2. M2's verdict is taken from O3 alone.)")
    frng = fri["rng"].to_numpy()
    out.append(rate_line(int(((frng >= 50) & (frng <= 100)).sum()), len(fri),
                         "    Friday range in [50,100] pips"))
    out.append(f"      median Friday range = {np.median(frng):.1f} pips")

    # N2 — uniform-close null, computed PER FRIDAY from that Friday's own range
    out.append("")
    out.append("  N2  UNIFORM-CLOSE NULL, matched per-Friday on that Friday's own range")
    out.append("      P(close lands 25-50 from BOTH extremes | range R), uniform close:")
    out.append("      = length of the admissible sub-interval / R")
    p_null = []
    for R in frng:
        # close must be in [lo+25, lo+50] intersect [hi-50, hi-25]
        a1, b1 = FRI_LO, FRI_HI                    # from low
        a2, b2 = R - FRI_HI, R - FRI_LO            # from high
        lo_i, hi_i = max(a1, a2), min(b1, b2)
        p_null.append(max(0.0, hi_i - lo_i) / R if R > 0 else 0.0)
    p_null = np.array(p_null)
    out.append(f"      expected joint rate under the matched uniform null = "
               f"{100*p_null.mean():6.2f}%")
    out.append(f"      OBSERVED joint rate                                = "
               f"{100*joint.mean():6.2f}%")
    out.append(f"      observed - null                                    = "
               f"{100*(joint.mean()-p_null.mean()):+6.2f} pp")
    out.append("      READING: this removes the range-width artifact. A wide Friday cannot")
    out.append("               satisfy M2a at all; a ~75-pip Friday satisfies it almost")
    out.append("               automatically. The comparison is against THAT, not against 0.")

    # N3 / O5 — weekday specificity
    out.append("")
    out.append("  O5 / N3  WEEKDAY CONTROL — is FRIDAY special, as the stated mechanism claims?")
    out.append("      (mechanism: 'to trap the traders going into the weekend and hit them")
    out.append("       with the gap' — weekend-specific by its own terms)")
    out.append(f"      {'day':<5} {'n':>5} {'joint 25-50':>12} {'med d_high':>11} "
               f"{'med d_low':>10} {'med range':>10}")
    best_non_fri = -1.0
    for d in range(6):
        sub = S[S["dow_name"] == WEEKDAYS[d]]
        if len(sub) == 0:
            continue
        a = sub["d_high"].to_numpy(); b = sub["d_low"].to_numpy()
        j = ((a >= FRI_LO) & (a <= FRI_HI) & (b >= FRI_LO) & (b <= FRI_HI))
        rate = 100 * j.mean()
        if WEEKDAYS[d] != "Fri":
            best_non_fri = max(best_non_fri, rate)
        out.append(f"      {WEEKDAYS[d]:<5} {len(sub):>5} {rate:>11.2f}% "
                   f"{np.median(a):>11.1f} {np.median(b):>10.1f} "
                   f"{np.median(sub['rng'].to_numpy()):>10.1f}  {nlabel(len(sub))}")
    fri_rate = 100 * joint.mean()
    out.append("")
    out.append(f"      Friday joint rate           = {fri_rate:6.2f}%")
    out.append(f"      best Mon-Thu/Sun joint rate = {best_non_fri:6.2f}%")
    out.append(f"      Friday - best other         = {fri_rate - best_non_fri:+6.2f} pp")
    out.append("      §6 specificity threshold: Friday must exceed EVERY other day by >= 10 pp")

    return dict(arm=arm, n_weeks=len(wk), m1_k=k, m1_n=len(rng_pips),
                m1_med=med, m2_k=int(joint.sum()), m2_n=len(fri),
                fri_rate=fri_rate, best_other=best_non_fri,
                null_rate=100 * p_null.mean(), censored=censored)


def main():
    out: list[str] = []
    out.append(header("PT-036",
                      "V10: the 600-1000 pip week, and the Friday close 25-50 off both extremes",
                      "both D-031 arms, always both reported"))
    out.append("")
    out.append("PRE-REGISTRATION: 06_MANUAL_BACKTEST/PRE_REGISTERED/"
               "PT-036_weekly_range_and_the_friday_close.md (committed first, f58dce7)")
    out.append("CLAIMS: M1 V10 [00:14:09] / [00:14:38];  M2 V10 [00:13:41]")
    out.append("SPEAKER: the course author, 100% of V10's runtime (D-033)")
    out.append("WINDOW: W-C' = 2013-01-06 -> 2016-06-30 = D-035 DEVELOPMENT exactly")
    out.append("HOLDOUT: 2016-07-01 -> 2017-12-29 NOT OPENED (not on disk, D-036a)")
    out.append("SOURCE: HistData GBP/USD M1 (D-036a); M15 aggregated locally")
    out.append("WEEK RULE: Sunday 17:00 open; an intra-week holiday re-open is NEVER a")
    out.append("           week boundary, and boundaries are never taken from C7's list")
    out.append(f"SEED: {SEED}   BOOTSTRAP ITERATIONS: {ITERS}")
    out.append("")
    out.append("QA GATE (precondition, D-036a):")
    for ln in qa_gate():
        out.append("  " + ln)
    for arm in ("A", "B"):
        verify_against_committed(arm)
    out.append("  committed M15 aggregation verified for both arms")

    res = {}
    for arm in ("A", "B"):
        res[arm] = run_arm(arm, out)

    out.append("")
    out.append("================ DECISION INPUTS (verdict applied by a human vs §6) ==========")
    out.append("This runner prints inputs, not verdicts — COMMON_PROTOCOL.md §9 rule 7 and the")
    out.append("BT_V08_0001 / BT_V09_0001 precedent, where the runner's own decision logic was")
    out.append("wrong and the pre-registration was right.")
    out.append("")
    out.append(f"  {'arm':<4} {'M1 in-band':>12} {'M1 median':>10} {'M2a joint':>11} "
               f"{'N2 null':>9} {'Fri-best':>9} {'censored':>9}")
    for arm in ("A", "B"):
        r = res[arm]
        out.append(f"  {arm:<4} {100*r['m1_k']/r['m1_n']:>11.2f}% {r['m1_med']:>10.1f} "
                   f"{100*r['m2_k']/r['m2_n']:>10.2f}% {r['null_rate']:>8.2f}% "
                   f"{r['fri_rate']-r['best_other']:>+8.2f} {r['censored']:>9d}")
    out.append("")
    out.append("§6 thresholds (fixed before the run, may not be moved):")
    out.append("  M1  CONFIRMED >=50% in-band | PARTIAL 20-50% | CONTRADICTED <20%")
    out.append("  M2a CONFIRMED >=50% joint   | PARTIAL 20-50% | CONTRADICTED <20%")
    out.append("  M2 specificity: Friday must exceed EVERY other day by >= 10 pp")
    out.append("")
    out.append("§6a PREDICTIONS committed before the run (scored in BT_V10_0001):")
    out.append("  P1 M1 CONTRADICTED, <5% in-band")
    out.append("  P2 median/800 factor in [0.15, 0.40]")
    out.append("  P3 M2a CONTRADICTED, <20% joint")
    out.append("  P4 M2 fails specificity")
    out.append("  P5 N2 null within 10pp of observed M2a")
    out.append("  P6 N4 shifted roster NOT distinguishable on M1")
    out.append("  P7 arms differ negligibly on M1, detectably on M2  [flagged CHEAP]")

    print("\n".join(out))


if __name__ == "__main__":
    main()
