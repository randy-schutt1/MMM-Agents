#!/usr/bin/env python3
"""PT-028 — on which weekday does the GBP/USD week make its high and its low? (re-issue of PT-010)

THE NULL IS EXPOSURE-WEIGHTED, NOT 1/6 — `PT-028` §3a
------------------------------------------------------
The trading week is 120 h and is NOT five equal days: Sunday 7 h, Mon-Thu 24 h each,
Friday 17 h. "A per-weekday-uniform null (1/6 each) is wrong and would manufacture a
result." Weights are computed PER WEEK and PER ARM from REALISED bars, so a week with
a closed Wednesday contributes zero Wednesday exposure and cannot inflate or deflate
that cell -- and Arm B's DST weeks give Sunday 6 h rather than 7.

This is also why the 2014-06-01 data hole must be excluded BEFORE the weights are
computed (§3c): including it would record 22 missing hours as GENUINE ZERO EXPOSURE,
encoding a corpus defect as a market fact, and would bias the Sunday cell downward in
exactly the cell that is already thinnest.

WHAT MAY AND MAY NOT CARRY A p-VALUE — `PT-028` §3d
---------------------------------------------------
  * the SIX-CELL MARGINALS may carry a chi-square and a p-value;
  * the 6x6 JOINT TABLE MAY NOT -- 36 cells over 180 weeks averages 5.0 per cell and
    the Sunday row/column average ~1. It is printed as a RAW COUNT MATRIX, labelled
    descriptive;
  * Measure 2's 30-bin hour-of-week histogram averages 6.0 per bin -- counts and the
    N3 distribution only, NO per-bin inference;
  * the SUNDAY and FRIDAY cells are below n = 30 under the exposure-weighted null and
    carry `SAMPLE INSUFFICIENT FOR INFERENCE - descriptive only` in the same sentence
    as any rate quoted from them.

scipy is not installed in this project, so the chi-square p-value is computed by
MONTE CARLO from the exposure-weighted multinomial (same seed, same iteration count)
rather than from an analytic chi-square CDF. That is stated in the observation; it is
also the more defensible choice at these cell counts, where the asymptotic
approximation is weakest.
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

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "V01", "data")

# trading-week day order: the week OPENS on Sunday, so Sunday is category 0
DAYS = ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri")
DAY_FROM_WD = {6: 0, 0: 1, 1: 2, 2: 3, 3: 4, 4: 5}      # Mon=0..Sun=6  ->  0..5


def day_cat(tm):
    wd = (np.floor_divide(np.asarray(tm, dtype="int64"), M.DAY) + 3) % 7
    return np.array([DAY_FROM_WD.get(int(x), -1) for x in wd])


def chi2_mc(obs, exp, iterations=M.ITERATIONS, seed=M.SEED):
    """Chi-square statistic, with a MONTE-CARLO p-value (scipy is not installed).

    Draws `iterations` multinomial samples of the same total from the exposure-
    weighted expected distribution and reports the share whose statistic equals or
    exceeds the observed one.
    """
    obs = np.asarray(obs, float)
    exp = np.asarray(exp, float)
    keep = exp > 0
    stat = float(((obs[keep] - exp[keep]) ** 2 / exp[keep]).sum())
    rng = np.random.default_rng(seed)
    p = exp[keep] / exp[keep].sum()
    n = int(obs.sum())
    draws = rng.multinomial(n, p, size=iterations).astype(float)
    e = exp[keep]
    null = ((draws - e) ** 2 / e).sum(axis=1)
    return stat, float((null >= stat).mean())


def run_arm(arm, log):
    m15 = M.load_m15(arm)
    raw = M.load_m15("A")
    roster = W.build_weeks(arm, m15)
    use = W.usable(roster, drop_truncated=True)
    keep = set(use["anchor_raw"].tolist())
    anch = W.week_anchor(raw.tm)
    sel = np.array([int(a) in keep for a in anch])
    M.assert_development(raw.tm[sel], f"PT-028 universe / arm {arm}")
    tm, h, l = m15.tm[sel], m15.h[sel], m15.l[sel]
    uniq, inv, n = week_index(anch[sel])

    log(f"\n{'='*74}\n--- ARM {arm} ---\n{'='*74}")
    for ln in W.census_lines(roster):
        log("  " + ln)
    log(f"  TRADING WEEKS USED: {len(use)}   (2014-06-01 EXCLUDED BY NAME before the")
    log(f"  exposure weights were computed — §3c: including it would encode 22 missing")
    log(f"  hours as genuine zero exposure and bias the thinnest cell downward.)")

    # ---- BASELINE 1: the exposure-weighted expectation, computed FIRST ----------
    exp_w = W.week_exposure_hours(use, M.Bars(tm, m15.o[sel], h, l, m15.c[sel], arm, 15))
    hrs = exp_w[["Sun", "Mon", "Tue", "Wed", "Thu", "Fri"]].values
    tot = hrs.sum(axis=1, keepdims=True)
    pw = np.divide(hrs, tot, out=np.zeros_like(hrs), where=tot > 0)
    expected = pw.sum(axis=0)                       # expected COUNT per weekday
    log(f"\n  PRIMARY BASELINE — exposure-weighted expectation over the hours ACTUALLY")
    log(f"  PRESENT in each week (§3a), computed BEFORE any extreme was located:")
    log("    weekday :  " + "  ".join(f"{d:>6s}" for d in DAYS))
    log("    hours   :  " + "  ".join(f"{hrs[:,i].mean():6.2f}" for i in range(6)))
    log("    share   :  " + "  ".join(f"{100*hrs[:,i].sum()/hrs.sum():5.1f}%"
                                      for i in range(6)))
    log("    expected:  " + "  ".join(f"{expected[i]:6.1f}" for i in range(6)))
    thin = [DAYS[i] for i in range(6) if expected[i] < 30]
    log(f"    cells below the n = 30 floor: {thin}  <<< DESCRIPTIVE ONLY, per §3d")

    # ---- BASELINE 2: N3 --------------------------------------------------------
    lo_e, hi_e = raw.tm[sel].min(), raw.tm[sel].max()
    hole = W.dt2m(W.DATA_HOLE_WEEK)
    n3_max = []
    for off in W.n3_week_shifts():
        a = W.week_anchor(raw.tm[sel] - int(off)) + int(off)
        u2, i2 = np.unique(a, return_inverse=True)
        good = ((u2 >= lo_e) & (u2 + W.DAY * 5 <= hi_e)
                & ~((u2 < hole + W.DAY * 7) & (u2 + W.DAY * 5 > hole)))
        if not good.any():
            continue
        m = good[i2]
        idx = np.where(m)[0]
        o = np.lexsort((h[idx], i2[idx]))
        li = np.lexsort((-l[idx], i2[idx]))
        wsort = i2[idx][o]
        last = np.r_[wsort[1:] != wsort[:-1], True]
        hi_i = idx[o][last]
        lo_i = idx[li][np.r_[i2[idx][li][1:] != i2[idx][li][:-1], True]]
        # position of the extreme WITHIN its sham week, in 6 exposure-matched bins
        c = np.bincount(np.clip(day_cat(tm[hi_i]), 0, 5), minlength=6)
        n3_max.append(c.max() / c.sum())
    n3_max = np.array(n3_max)
    log(f"\n  SECOND BASELINE — N3 week-anchor shift, {M.ITERATIONS} draws, "
        f"seed {M.SEED}.")
    log(f"    modal weekday share of HIGHS under a shifted anchor: "
        f"{M.dist_line(n3_max)}")
    log(f"    (If extremes cluster mid-week under ANY week anchor, the finding is")
    log(f"     about the middle of a 5-day span, not about Tuesday.)")

    # ---- BASELINE 3: randomly re-blocked 5-day spans ---------------------------
    # "The same measurement on randomly re-blocked 5-day spans that do not respect
    # the calendar week." Implemented in TRADING-BAR space: the bar series is cut
    # into consecutive 480-bar (120 trading-hour) spans from a random offset, so the
    # weekend is not a boundary and the calendar week plays no part. The extreme's
    # position is then binned with the SAME relative widths as the realised weekday
    # exposure shares, so the two are comparable.
    widths = hrs.sum(axis=0) / hrs.sum()
    edges = np.r_[0.0, np.cumsum(widths)]
    rng = np.random.default_rng(M.SEED)
    span = 480
    reb = []
    for _ in range(M.ITERATIONS):
        st = int(rng.integers(0, span))
        k = (len(tm) - st) // span
        if k < 30:
            continue
        idx = np.arange(st, st + k * span).reshape(k, span)
        pos_h = np.argmax(h[idx], axis=1) / span
        c = np.histogram(pos_h, bins=edges)[0]
        reb.append(c.max() / c.sum())
    reb = np.array(reb)
    log(f"\n  THIRD BASELINE — randomly re-blocked 5-day (120 trading-hour) spans that")
    log(f"  do NOT respect the calendar week, {len(reb)} draws, binned with the same")
    log(f"  relative widths as the realised weekday exposure:")
    log(f"    modal-bin share of HIGHS: {M.dist_line(reb)}")
    log(f"    (This separates 'the calendar week is a real unit for GBP/USD' from")
    log(f"     'any 5-day span has a middle'.)")

    # ---- THE OBSERVED DISTRIBUTION — read only now -----------------------------
    o = np.lexsort((h, inv)); li = np.lexsort((-l, inv))
    lastm = np.r_[inv[o][1:] != inv[o][:-1], True]
    lastl = np.r_[inv[li][1:] != inv[li][:-1], True]
    hi_i, lo_i = o[lastm], li[lastl]
    hd, ld = day_cat(tm[hi_i]), day_cat(tm[lo_i])
    ch = np.bincount(np.clip(hd, 0, 5), minlength=6)
    cl = np.bincount(np.clip(ld, 0, 5), minlength=6)

    log(f"\n  {'='*70}\n  OBSERVED — read after all three baselines\n  {'='*70}")
    log(f"  MEASURE 1 — weekday of the week's high and of its low (n = {len(hd)} each)")
    log("    weekday :  " + "  ".join(f"{d:>6s}" for d in DAYS))
    log("    expected:  " + "  ".join(f"{expected[i]:6.1f}" for i in range(6)))
    log("    HIGHS   :  " + "  ".join(f"{ch[i]:6d}" for i in range(6)))
    log("    LOWS    :  " + "  ".join(f"{cl[i]:6d}" for i in range(6)))
    log("    hi/exp  :  " + "  ".join(f"{ch[i]/expected[i]:6.2f}" for i in range(6)))
    log("    lo/exp  :  " + "  ".join(f"{cl[i]/expected[i]:6.2f}" for i in range(6)))
    for nm, c in (("HIGH", ch), ("LOW", cl)):
        for i in range(6):
            if expected[i] < 30 or c[i] < 30:
                log(f"    ⚠ {nm} {DAYS[i]} cell: observed {c[i]}, expected "
                    f"{expected[i]:.1f} — SAMPLE INSUFFICIENT FOR INFERENCE, "
                    f"descriptive only (§3d)")
    s_h, p_h = chi2_mc(ch, expected)
    s_l, p_l = chi2_mc(cl, expected)
    log(f"\n    chi-square on the SIX-CELL MARGINALS ONLY (§3d permits this and only")
    log(f"    this), Monte-Carlo p from the exposure-weighted multinomial, "
        f"{M.ITERATIONS} draws:")
    log(f"      HIGHS  chi2 = {s_h:7.2f}   p = {p_h:.4f}")
    log(f"      LOWS   chi2 = {s_l:7.2f}   p = {p_l:.4f}")

    mode_h, mode_l = DAYS[int(np.argmax(ch))], DAYS[int(np.argmax(cl))]
    focal = mode_h in ("Tue", "Wed") and mode_l in ("Tue", "Wed")
    log(f"\n    PRE-REGISTERED FOCAL PREDICTION — the MODE of both marginals falls on")
    log(f"    Tuesday or Wednesday:")
    log(f"      mode of HIGHS = {mode_h}   mode of LOWS = {mode_l}")
    log(f"      FOCAL PREDICTION {'HOLDS' if focal else 'FAILS'}")
    log(f"    observed modal share {max(ch.max(), cl.max())/len(hd):.4f} vs N3 median "
        f"{np.median(n3_max):.4f} (pct {M.percentile_of(ch.max()/len(hd), n3_max):.1f})"
        f" and re-blocked median {np.median(reb):.4f} "
        f"(pct {M.percentile_of(ch.max()/len(hd), reb):.1f})")

    # ---- MEASURE 2 — hour-of-week in 4-hour bins -------------------------------
    mfw_h = (tm[hi_i] - uniq[inv[hi_i]]) if False else (tm[hi_i] - W.week_anchor(
        raw.tm[sel][hi_i]))
    bins = np.clip(mfw_h // 240, 0, 29).astype(int)
    hist = np.bincount(bins, minlength=30)
    log(f"\n  MEASURE 2 — hour-of-week of the HIGH, 4-hour bins (30 bins, "
        f"{len(hd)/30:.1f} per bin).")
    log(f"  COUNTS ONLY — §3d forbids per-bin inference at this density:")
    log("    " + " ".join(f"{v:d}" for v in hist))
    log(f"    busiest bins: " + ", ".join(
        f"{int(b)*4}-{int(b)*4+4}h ({hist[b]})" for b in np.argsort(-hist)[:4]))

    # ---- MEASURE 3 — joint table and the sign -----------------------------------
    log(f"\n  MEASURE 3 — the 6x6 JOINT TABLE. RAW COUNTS, DESCRIPTIVE ONLY, NO chi2")
    log(f"  and NO p-value (§3d point 3: 36 cells over {len(hd)} weeks averages "
        f"{len(hd)/36:.1f} per cell):")
    J = np.zeros((6, 6), dtype=int)
    for a, b in zip(np.clip(hd, 0, 5), np.clip(ld, 0, 5)):
        J[a, b] += 1
    log("      low ->  " + "  ".join(f"{d:>4s}" for d in DAYS))
    for i in range(6):
        log(f"    hi {DAYS[i]:<4s}" + "  ".join(f"{J[i,j]:4d}" for j in range(6)))
    sign = np.sign(np.clip(hd, 0, 5) - np.clip(ld, 0, 5))
    log(f"\n    THE INFERENTIALLY USABLE PART of Measure 3 — the SIGN of "
        f"(high_day - low_day),")
    log(f"    a single ordinal summary at n = {len(sign)}:")
    log(f"      high AFTER low  (+): {M.fmt_rate(int((sign>0).sum()), len(sign))}")
    log(f"      high BEFORE low (-): {M.fmt_rate(int((sign<0).sum()), len(sign))}")
    log(f"      same day        (0): {int((sign==0).sum())}")

    log("\n  PRE-REGISTERED SENSITIVITY APPENDIX — five largest-range weeks:")
    for r in W.largest_range_weeks(use).itertuples():
        log(f"    {r.week}  range {r.range_pips:7.1f} pips  ends {r.ends_weekday}")

    return dict(arm=arm, n=len(hd), expected=expected.tolist(),
                highs=ch.tolist(), lows=cl.tolist(),
                chi2_high=s_h, p_high=p_h, chi2_low=s_l, p_low=p_l,
                mode_high=mode_h, mode_low=mode_l, focal_holds=bool(focal),
                joint=J.tolist(), hour_bins=hist.tolist(),
                sign_pos=int((sign > 0).sum()), sign_neg=int((sign < 0).sum()),
                sign_zero=int((sign == 0).sum()),
                n3_modal_median=float(np.median(n3_max)),
                reblock_modal_median=float(np.median(reb)),
                thin_cells=thin)


def main():
    lines = []

    def log(s=""):
        print(s)
        lines.append(s)

    log(M.header("PT-028",
                 "On which weekday does the week make its high and its low?",
                 "window   : W-C' 2013-01-06 -> 2016-06-30. Re-issue of PT-010.\n"
                 "⚠ THE SUNDAY AND FRIDAY CELLS ARE BELOW n = 30 AND ARE\n"
                 "  DESCRIPTIVE ONLY. The 6x6 joint table carries NO chi-square.\n"
                 "  The null is EXPOSURE-WEIGHTED, never 1/6 per weekday."))
    out = {}
    for arm in ("A", "B"):
        out[arm] = run_arm(arm, log)
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "pt028_report.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    with open(os.path.join(OUT, "pt028_results.json"), "w") as fh:
        json.dump(out, fh, indent=2, default=float)


if __name__ == "__main__":
    main()
