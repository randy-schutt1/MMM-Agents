#!/usr/bin/env python3
"""PT-029 — is the rest of the week a "unidirectional swing" after the extreme? (re-issue of PT-011)

CLASS: DESCRIPTIVE BY CONSTRUCTION — the anchor is RETROSPECTIVE
----------------------------------------------------------------
`PT-029` §3: "A trader cannot know on Wednesday that Wednesday's high is the week's
high. This test measures whether the STRUCTURE the course describes exists; it does
not and cannot show that it is tradeable. Any report that elides that is `E14` at the
level of the whole test." Every figure this script produces carries that.

THE RESOLUTION IS A FIRST-CLASS PARAMETER — §0b
------------------------------------------------
Directional efficiency is |net| / sum|bar-to-bar move|, and THE DENOMINATOR GROWS AS
THE BAR GETS FINER: the same week measured on M1 has a longer path than on M15, so
efficiency is LOWER at finer resolution. That is arithmetic, not a market property.

Pre-registered: the path is summed over 15-MINUTE bars, for every week and every
control alike. THE M1 CORPUS IS NOT USED FOR THE PATH SUM. "An efficiency number
without its bar size is unreadable and not comparable with any figure computed
elsewhere in this project on a different timeframe."

THE ANCHOR RULE IS FIXED HERE AND NOT DECIDED PER WEEK — §3
------------------------------------------------------------
"The timestamp of the week's high OR low, whichever the week's net direction runs
away FROM." Net up  -> the run is away from the LOW,  so the anchor is the low.
Net down -> the run is away from the HIGH, so the anchor is the high.
Both are computed; the rule is stated once and applied mechanically.
"""
from __future__ import annotations

import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import mmm_lib as M
import mmm_week as W
from mmm_block import week_index

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "V02", "data")
NET_ZERO_PIPS = 25.0        # V03's own counter-case, as a DISTANCE (travels across vendors)


def efficiency(c, a, b):
    """|net| / path over closes c[a:b+1]. Returns nan for a degenerate span."""
    if b <= a:
        return np.nan
    seg = c[a:b + 1]
    path = np.abs(np.diff(seg)).sum()
    if path <= 0:
        return np.nan
    return abs(seg[-1] - seg[0]) / path


def max_counter_retrace(c, a, b):
    """Largest counter-directional retracement over c[a:b+1], in pips and as a share."""
    if b <= a:
        return np.nan, np.nan
    seg = c[a:b + 1]
    net = seg[-1] - seg[0]
    if net == 0:
        return np.nan, np.nan
    if net > 0:
        run = np.maximum.accumulate(seg)
        dd = (run - seg).max()
    else:
        run = np.minimum.accumulate(seg)
        dd = (seg - run).max()
    return dd / M.PIP, float(dd / abs(net))


def run_arm(arm, log):
    m15 = M.load_m15(arm)
    raw = M.load_m15("A")
    roster = W.build_weeks(arm, m15)
    use = W.usable(roster, drop_truncated=True)
    keep = set(use["anchor_raw"].tolist())
    anch = W.week_anchor(raw.tm)
    sel = np.array([int(a) in keep for a in anch])
    M.assert_development(raw.tm[sel], f"PT-029 universe / arm {arm}")
    tm, h, l, c, o = (m15.tm[sel], m15.h[sel], m15.l[sel], m15.c[sel], m15.o[sel])
    uniq, inv, n = week_index(anch[sel])

    log(f"\n{'='*74}\n--- ARM {arm} ---\n{'='*74}")
    for ln in W.census_lines(roster):
        log("  " + ln)
    thu = use[use["ends_weekday"] == "Thu"]["week"].tolist()
    log(f"  TRADING WEEKS USED: {len(use)}")
    log(f"  §3a: 2014-06-01 EXCLUDED BY NAME. This is the test where the hole does the")
    log(f"       most damage — the efficiency DENOMINATOR is a path summed over M15")
    log(f"       bars, so 22 missing hours would shorten the path and INFLATE")
    log(f"       efficiency, biasing the headline metric TOWARD the claim under test.")
    log(f"  §3a: {thu} end THURSDAY — the net-zero metric uses the REALISED last bar,")
    log(f"       never a nominal Friday close.")
    log(f"  §0b: PATH RESOLUTION = 15-MINUTE BARS, for every week and every control")
    log(f"       alike. The M1 corpus is NOT used for the path sum. Efficiency figures")
    log(f"       below are NOT comparable with any computed on another timeframe.")

    rows = np.split(np.arange(len(tm)), np.cumsum(np.bincount(inv))[:-1])

    eff, mono_p, mono_s, netzero, span_len, anchor_pos = [], [], [], [], [], []
    for w, idx in enumerate(rows):
        cc = c[idx]
        w_open_px = o[idx][0]
        w_close_px = cc[-1]
        net = w_close_px - w_open_px
        ih, il = int(np.argmax(h[idx])), int(np.argmin(l[idx]))
        # §3 anchor rule: the extreme the week's net direction runs AWAY FROM
        a = il if net > 0 else ih
        e = efficiency(cc, a, len(cc) - 1)
        p, s = max_counter_retrace(cc, a, len(cc) - 1)
        eff.append(e); mono_p.append(p); mono_s.append(s)
        span_len.append(len(cc) - 1 - a)
        anchor_pos.append(a / max(len(cc) - 1, 1))
        netzero.append(abs(net) / M.PIP <= NET_ZERO_PIPS)
    eff = np.array(eff); mono_p = np.array(mono_p); mono_s = np.array(mono_s)
    netzero = np.array(netzero); span_len = np.array(span_len)
    anchor_pos = np.array(anchor_pos)

    # ---------------- BASELINES, ALL BEFORE THE OBSERVED DISTRIBUTION -----------
    rng = np.random.default_rng(M.SEED)

    log(f"\n  PRIMARY BASELINE (§4 arm 1) — efficiency over EQUAL-LENGTH spans anchored")
    log(f"  at a RANDOM bar in the SAME week, {M.ITERATIONS} draws, seed {M.SEED}.")
    log(f"  Same week, same volatility, same length; only the anchor changes.")
    b1 = np.full(M.ITERATIONS, np.nan)
    for it in range(M.ITERATIONS):
        vals = []
        for w, idx in enumerate(rows):
            L = span_len[w]
            if L <= 0:
                continue
            cc = c[idx]
            hi = len(cc) - 1 - L
            if hi <= 0:
                continue
            a = int(rng.integers(0, hi + 1))
            v = efficiency(cc, a, a + L)
            if np.isfinite(v):
                vals.append(v)
        b1[it] = np.median(vals) if vals else np.nan
    log(f"    median efficiency across weeks: {M.dist_line(b1)}")

    log(f"\n  SECOND BASELINE (§4 arm 2) — equal-length spans anchored at the RELATIVE")
    log(f"  POSITION of a RANDOMLY CHOSEN OTHER WEEK'S extreme, {M.ITERATIONS} draws.")
    log(f"  ⚠ WHAT THIS DOES AND DOES NOT CONTROL, stated rather than assumed. §4 calls")
    log(f"    it the control for 'the mechanical fact that any span starting at a local")
    log(f"    extreme has elevated efficiency by construction'. Read literally — and it")
    log(f"    is implemented literally — it borrows the extreme's TIMING, not its")
    log(f"    EXTREMENESS: the borrowed anchor is a typical extreme POSITION in this")
    log(f"    week, but need not be an extreme of it. It therefore isolates POSITION,")
    log(f"    and arm 1 plus arm 2 BRACKET the extremeness effect rather than measuring")
    log(f"    it directly. Constructing a 'local extreme' would require a definition the")
    log(f"    course does not give, which `D-030` forbids inventing.")
    b2 = np.full(M.ITERATIONS, np.nan)
    for it in range(M.ITERATIONS):
        vals = []
        donors = rng.integers(0, n, size=n)
        for w, idx in enumerate(rows):
            L = span_len[w]
            cc = c[idx]
            if L <= 0 or len(cc) < 2:
                continue
            a = int(round(anchor_pos[donors[w]] * (len(cc) - 1)))
            a = min(max(a, 0), len(cc) - 2)
            v = efficiency(cc, a, len(cc) - 1)
            if np.isfinite(v):
                vals.append(v)
        b2[it] = np.median(vals) if vals else np.nan
    log(f"    median efficiency across weeks: {M.dist_line(b2)}")

    log(f"\n  THIRD BASELINE (§4 arm 3) — N3 week-anchor shift, {M.ITERATIONS} draws:")
    lo_e, hi_e = raw.tm[sel].min(), raw.tm[sel].max()
    hole = W.dt2m(W.DATA_HOLE_WEEK)
    b3 = []
    for off in W.n3_week_shifts():
        a_ = W.week_anchor(raw.tm[sel] - int(off)) + int(off)
        u2, i2 = np.unique(a_, return_inverse=True)
        good = ((u2 >= lo_e) & (u2 + W.DAY * 5 <= hi_e)
                & ~((u2 < hole + W.DAY * 7) & (u2 + W.DAY * 5 > hole)))
        r2 = np.split(np.arange(len(tm)), np.cumsum(np.bincount(i2))[:-1])
        vals = []
        for w, idx in enumerate(r2):
            if not good[w] or len(idx) < 2:
                continue
            cc = c[idx]
            net = cc[-1] - o[idx][0]
            a = int(np.argmin(l[idx])) if net > 0 else int(np.argmax(h[idx]))
            v = efficiency(cc, a, len(cc) - 1)
            if np.isfinite(v):
                vals.append(v)
        if vals:
            b3.append(float(np.median(vals)))
    b3 = np.array(b3)
    log(f"    median efficiency across sham weeks: {M.dist_line(b3)}")

    # ---------------- OBSERVED ----------------
    obs = float(np.nanmedian(eff))
    log(f"\n  {'='*70}\n  OBSERVED — read after all three baselines\n  {'='*70}")
    log(f"  ⚠ CLASS: DESCRIPTIVE. The anchor is knowable only AFTER the week ends.")
    log(f"  ⚠ PATH RESOLUTION: 15-MINUTE BARS (§0b). Not comparable across timeframes.")
    log(f"\n  METRIC — DIRECTIONAL EFFICIENCY after the retrospective extreme, "
        f"n = {int(np.isfinite(eff).sum())}")
    log(f"    median {obs:.4f}, IQR [{np.nanpercentile(eff,25):.4f}, "
        f"{np.nanpercentile(eff,75):.4f}], "
        f"5-95% [{np.nanpercentile(eff,5):.4f}, {np.nanpercentile(eff,95):.4f}]")
    lo95, hi95 = M.boot_ci(eff)
    log(f"    bootstrap 95% CI on the median: [{lo95:.4f}, {hi95:.4f}]")
    p1 = M.percentile_of(obs, b1); p2 = M.percentile_of(obs, b2)
    p3 = M.percentile_of(obs, b3)
    log(f"    vs arm 1 (random anchor, same week) : median {np.nanmedian(b1):.4f}"
        f"   percentile {p1:.1f}")
    log(f"    vs arm 2 (borrowed extreme position): median {np.nanmedian(b2):.4f}"
        f"   percentile {p2:.1f}")
    log(f"    vs arm 3 (N3 week-anchor shift)     : median {np.nanmedian(b3):.4f}"
        f"   percentile {p3:.1f}")

    log(f"\n  METRIC — MONOTONICITY: largest counter-directional retracement after the")
    log(f"  anchor:")
    log(f"    in pips           : median {np.nanmedian(mono_p):.1f}, "
        f"IQR [{np.nanpercentile(mono_p,25):.1f}, {np.nanpercentile(mono_p,75):.1f}]")
    log(f"    as a share of the total move: median {np.nanmedian(mono_s):.3f}, "
        f"IQR [{np.nanpercentile(mono_s,25):.3f}, {np.nanpercentile(mono_s,75):.3f}]")

    nz = int(netzero.sum())
    log(f"\n  METRIC — NET-ZERO WEEKS (§7 step 6 requires this in the HEADLINE, not the")
    log(f"  appendix). Friday close within +/-{NET_ZERO_PIPS:.0f} pips of the week open,")
    log(f"  using the REALISED last bar for the two Thursday-ending weeks:")
    log(f"    {M.fmt_rate(nz, len(netzero))}")
    sub = "  <<< SAMPLE INSUFFICIENT FOR INFERENCE — descriptive only" if nz < 30 else ""
    log(f"    subset size for any statement ABOUT net-zero weeks: {nz}{sub}")
    if nz:
        log(f"    their median efficiency: {np.nanmedian(eff[netzero]):.4f}"
            f"   (all other weeks {np.nanmedian(eff[~netzero]):.4f})")

    log("\n  PRE-REGISTERED SENSITIVITY APPENDIX — five largest-range weeks:")
    for r in W.largest_range_weeks(use).itertuples():
        i = int(np.where(use['week'].values == r.week)[0][0])
        log(f"    {r.week}  range {r.range_pips:7.1f} pips  efficiency {eff[i]:.4f}")

    return dict(arm=arm, n=int(np.isfinite(eff).sum()), eff_median=obs,
                eff_ci=[lo95, hi95],
                b1_median=float(np.nanmedian(b1)), b1_pct=p1,
                b2_median=float(np.nanmedian(b2)), b2_pct=p2,
                b3_median=float(np.nanmedian(b3)), b3_pct=p3,
                mono_pips=float(np.nanmedian(mono_p)),
                mono_share=float(np.nanmedian(mono_s)),
                netzero=nz, netzero_n=len(netzero),
                path_resolution_min=15)


def main():
    lines = []

    def log(s=""):
        print(s)
        lines.append(s)

    log(M.header("PT-029",
                 "Is the rest of the week a unidirectional swing after the extreme?",
                 "window   : W-C' 2013-01-06 -> 2016-06-30. Re-issue of PT-011.\n"
                 "⚠ CLASS: DESCRIPTIVE BY CONSTRUCTION — the anchor is retrospective\n"
                 "  and is unknowable in real time. This is NOT a trading result.\n"
                 "⚠ PATH RESOLUTION: 15-MINUTE BARS (§0b), a first-class parameter."))
    out = {}
    for arm in ("A", "B"):
        out[arm] = run_arm(arm, log)
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "pt029_report.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    with open(os.path.join(OUT, "pt029_results.json"), "w") as fh:
        json.dump(out, fh, indent=2, default=float)


if __name__ == "__main__":
    main()
