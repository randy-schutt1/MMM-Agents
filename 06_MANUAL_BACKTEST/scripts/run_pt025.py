#!/usr/bin/env python3
"""PT-025 — do WEEKLY extremes cluster at the six printed boundaries? (re-issue of PT-002's W-C arm)

WINDOW AND EXCLUSIONS — `PT-025` §3c, applied BY NAME
-----------------------------------------------------
`W-C'` = 2013-01-06 -> 2016-06-30, which IS `D-035`'s DEVELOPMENT block.

  * the week of 2014-06-01 is EXCLUDED BY NAME -- the corpus holds zero bars for
    Sun 2014-06-01 and 521/1440 for Mon 2014-06-02, so neither week boundary can be
    placed, and two of this test's six boundaries ARE the week boundary;
  * the six Dec/Jan closure weeks are INCLUDED and reported separately -- the
    disposition is INHERITED from the original, not re-decided after a QA check
    surfaced them, which §3c calls "the suit-the-result choice the gate exists to
    prevent";
  * 2015-12-20 and 2015-12-27 END ON THURSDAY, and §3c requires their End Of The Week
    boundary be placed at the REALISED last bar, never at a nominal Friday 17:00:
    "Placing a boundary where the corpus has no data would invent one." Implemented in
    `_week_bound_instants` below, which reads open and close from the roster.

WHY THE BOUNDARY DISTANCE SPLITS IN TWO
---------------------------------------
Four of the six categories (day open, day close, session open, session close) are pure
MINUTE-OF-DAY facts in the arm's own clock, so a bar's distance to them does not depend
on where the week is anchored at all. Only the two WEEK boundaries move when the anchor
moves. The intraday distance is therefore computed once for every bar and reused across
all 2,000 null draws; only the weekly term is recomputed. Without this the nulls would
be a 180-week x 2,000-draw Python loop.

This also makes the arms' difference explicit and correct. The week open is one physical
instant (Sunday 22:00 UTC). Arm A calls it 17:00 and Arm B calls it 18:00 during US DST,
so the SAME instant sits at a different offset from "20:30 local" in the two arms. US
DST transitions at 02:00 local Sunday, which is before the 17:00 week open, so the DST
state is constant across any one trading week and the shift never lands mid-week.

BASELINES (`PT-025` §4), all run before the observed share is read
------------------------------------------------------------------
Primary  N2 circular clock shift, 1,000 draws, seed 20260812
Second   N3 week-anchor shift, 1,000 draws, seed 20260812 -- "the one that matters most
         here, so two of the six boundaries ARE the week anchor, so a week-anchor shift
         is the only control that can tell 'the week opens here' from 'a week opens
         somewhere'"
Third    the exposure-weighted analytic expectation over the 120-hour trading week
"""
from __future__ import annotations

import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import mmm_lib as M
import mmm_week as W
from mmm_bounds import group_extremes

BANDS = (15, 30, 60)
HEADLINE_BAND = 30
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "V01", "data")

# The V02 printed table, as minute-of-day in the ARM's own clock.
DAY_BOUND = (17 * 60,)                                   # 17:00 — day open AND day close
SESSION_OPEN = (20 * 60 + 30, 3 * 60 + 30, 9 * 60 + 30)  # Asian, London, New York
SESSION_CLOSE = (3 * 60, 9 * 60, 17 * 60)                # Asian, London, New York
INTRADAY = {"day_open": DAY_BOUND, "day_close": DAY_BOUND,
            "session_open": SESSION_OPEN, "session_close": SESSION_CLOSE}


def _circ_day_dist(mod: np.ndarray, targets) -> np.ndarray:
    """Distance in minutes to the nearest target minute-of-day, wrapping midnight."""
    out = np.full(len(mod), np.inf)
    for t in targets:
        d = np.abs(mod - t)
        out = np.minimum(out, np.minimum(d, M.DAY - d))
    return out


def _intraday_dist(m15: M.Bars, offset_min: int = 0):
    """Per-bar distance to the nearest intraday boundary, and per category.

    `offset_min` shifts the intraday LABELS, which is what N2 is: "all session and
    boundary labels shifted by an offset" (`COMMON_PROTOCOL.md` §5). N2 therefore
    moves these AND the week anchor together — a rigid shift of the whole boundary
    system, which leaves the covered fraction essentially unchanged.

    N3 is different by design: it shifts ONLY the week anchor and leaves the intraday
    labels alone, so it must be called with offset 0 here. That asymmetry is the
    point of having both nulls, and it is why §3a's covered-fraction correction has
    to be applied per draw — see `_score`.
    """
    mod = (M.minute_of_day(m15.tm) - int(offset_min)) % M.DAY
    per = {k: _circ_day_dist(mod, v) for k, v in INTRADAY.items()}
    return np.minimum.reduce(list(per.values())), per


def _weekly_dist(tm, inv, first, last):
    """Distance to this bar's own week open / week close — the REALISED instants."""
    return np.minimum(np.abs(tm - first[inv]), np.abs(tm - last[inv]))


def _partition(raw_tm, offset_min):
    """Sham (or real) week anchors under a clock shifted by `offset_min`."""
    return W.week_anchor(raw_tm - int(offset_min)) + int(offset_min)


def _score(tm, h, l, anchors, d_intra, keep_span):
    """Share of weekly extremes within each band, for one anchoring.

    `keep_span` drops any week whose span touches an excluded region — the corpus
    edges and the 2014-06-01 hole. A partially-covered sham week is not measurable
    either, and scoring the null by a looser standard than the rule arm would flatter
    whichever of the two it favoured.
    """
    uniq, inv = np.unique(anchors, return_inverse=True)
    n = len(uniq)
    first = np.full(n, np.iinfo("int64").max, dtype="int64")
    last = np.full(n, np.iinfo("int64").min, dtype="int64")
    np.minimum.at(first, inv, tm)
    np.maximum.at(last, inv, tm)
    ok = keep_span(uniq)
    if not ok.any():
        return None
    sel = ok[inv]
    days, ih, il = group_extremes(inv[sel], h[sel], l[sel])
    idx = np.where(sel)[0]
    ei = np.concatenate([idx[ih], idx[il]])
    d = np.minimum(d_intra[ei], _weekly_dist(tm[ei], inv[ei], first, last))
    # §3a's covered fraction, recomputed for THIS anchoring over the same bars.
    # Required because N3 moves the week boundaries OFF the 17:00 instants they
    # coincide with in reality, which ADDS covered area and inflates the null's raw
    # share for a purely arithmetic reason. Comparing raw shares across anchorings
    # that cover different amounts of the week would measure the coverage, not the
    # clock. The ratio observed/expected is the comparable quantity.
    d_all = np.minimum(d_intra[sel], _weekly_dist(tm[sel], inv[sel], first, last))
    return d, len(days), ei, d_all


def run_arm(arm, log):
    m15_full = M.load_m15(arm)
    raw_full = M.load_m15("A")
    roster = W.build_weeks(arm, m15_full)
    use = W.usable(roster, drop_truncated=True)

    log(f"\n{'='*74}\n--- ARM {arm} ---\n{'='*74}")
    for ln in W.census_lines(roster):
        log("  " + ln)
    log(f"  WEEKS USED (§3d)                       : {len(use)}"
        f"   -> {2*len(use)} weekly-extreme timestamps")
    log(f"  excluded by name: data hole {W.DATA_HOLE_WEEK}; "
        f"truncated {W.TRUNCATED_FINAL_WEEK}")
    thu = use[use["ends_weekday"] == "Thu"]["week"].tolist()
    log(f"  §3c End-Of-Week placed at the REALISED last bar for: {thu}")

    # bar universe = exactly the bars of the 180 usable weeks
    anchors_real = _partition(raw_full.tm, 0)
    keep_weeks = set(use["anchor_raw"].tolist())
    sel = np.array([int(a) in keep_weeks for a in anchors_real])
    tm, h, l = m15_full.tm[sel], m15_full.h[sel], m15_full.l[sel]
    raw_tm = raw_full.tm[sel]
    m15 = M.Bars(tm, m15_full.o[sel], h, l, m15_full.c[sel], arm, 15)
    d_intra, per_cat = _intraday_dist(m15)
    log(f"  bar universe: {len(tm)} M15 bars, "
        f"{M.m2s(raw_tm.min())} -> {M.m2s(raw_tm.max())}")
    M.assert_development(raw_tm, f"PT-025 universe / arm {arm}")

    lo_edge, hi_edge = raw_tm.min(), raw_tm.max()
    hole = W.dt2m(W.DATA_HOLE_WEEK)

    def keep_span(anch):
        """Reject sham weeks at the universe edges or overlapping the excluded hole."""
        return ((anch >= lo_edge) & (anch + W.DAY * 5 <= hi_edge)
                & ~((anch < hole + W.DAY * 7) & (anch + W.DAY * 5 > hole)))

    def keep_real(anch):
        return np.array([int(a) in keep_weeks for a in anch])

    # ---- THIRD BASELINE: analytic exposure-weighted expectation ----------------
    uniq_r, inv_r = np.unique(anchors_real[sel], return_inverse=True)
    first_r = np.full(len(uniq_r), np.iinfo("int64").max, dtype="int64")
    last_r = np.full(len(uniq_r), np.iinfo("int64").min, dtype="int64")
    np.minimum.at(first_r, inv_r, tm)
    np.maximum.at(last_r, inv_r, tm)
    d_bar = np.minimum(d_intra, _weekly_dist(tm, inv_r, first_r, last_r))
    exp_cov = {b: float((d_bar <= b).mean()) for b in BANDS}
    log("\n  THIRD BASELINE — exposure-weighted analytic expectation over the")
    log("  120-hour trading week, overlap-corrected, computed on REALISED bars (§3a):")
    for b in BANDS:
        log(f"    band +/-{b:2d} min : expected share {exp_cov[b]:.4f}")

    # ---- PRIMARY: N2 ----------------------------------------------------------
    def null(offsets, label, shift_intraday):
        """`shift_intraday` distinguishes the two nulls.

        N2 is a CLOCK shift: intraday labels and the week anchor move together.
        N3 is a WEEK-ANCHOR shift: only the week boundaries move, which is exactly
        what makes it "the only control that can tell 'the week opens here' from
        'a week opens somewhere'" (§4) — and exactly what makes its covered fraction
        differ from the rule arm's.
        """
        out = {b: np.full(len(offsets), np.nan) for b in BANDS}
        cov = {b: np.full(len(offsets), np.nan) for b in BANDS}
        rat = {b: np.full(len(offsets), np.nan) for b in BANDS}
        for i, off in enumerate(offsets):
            di = _intraday_dist(m15, int(off))[0] if shift_intraday else d_intra
            r = _score(tm, h, l, _partition(raw_tm, int(off)), di, keep_span)
            if r is None:
                continue
            d, _, _, d_all = r
            for b in BANDS:
                s = float((d <= b).mean())
                c = float((d_all <= b).mean())
                out[b][i], cov[b][i] = s, c
                rat[b][i] = s / c if c else np.nan
        log(f"\n  {label}:")
        for b in BANDS:
            log(f"    band +/-{b:2d} min : share {M.dist_line(out[b])}")
            log(f"{'':20s} covered {np.nanmedian(cov[b]):.4f} | "
                f"ratio {M.dist_line(rat[b])}")
        return out, cov, rat

    n2, n2c, n2r = null(M.n2_offsets(),
                        f"PRIMARY BASELINE — N2 circular clock shift (labels AND week "
                        f"anchor), {M.ITERATIONS} draws, seed {M.SEED}", True)
    n3, n3c, n3r = null(W.n3_week_shifts(),
                        f"SECOND BASELINE — N3 week-anchor shift ONLY, "
                        f"{M.ITERATIONS} draws, seed {M.SEED}", False)

    # ---- RULE ARM -------------------------------------------------------------
    d, nweeks, ei, _ = _score(tm, h, l, anchors_real[sel], d_intra, keep_real)
    log(f"\n  OBSERVED (read after all three baselines) — {nweeks} weeks, "
        f"{len(d)} extremes")
    log("  Two comparisons are reported for each band: the RAW share against each")
    log("  null's raw share, and the §3a-corrected RATIO observed/covered against")
    log("  each null's own ratio. Where a null covers a different fraction of the")
    log("  week than the rule arm does, only the ratio comparison is meaningful.")
    res = {}
    for b in BANDS:
        k = int((d <= b).sum())
        share = k / len(d)
        ratio = share / exp_cov[b]
        p2, p3 = M.percentile_of(share, n2[b]), M.percentile_of(share, n3[b])
        r2, r3 = M.percentile_of(ratio, n2r[b]), M.percentile_of(ratio, n3r[b])
        res[b] = dict(k=k, n=len(d), share=share, expected=exp_cov[b], ratio=ratio,
                      n2_pct=p2, n3_pct=p3, n2_ratio_pct=r2, n3_ratio_pct=r3,
                      n2_cov=float(np.nanmedian(n2c[b])),
                      n3_cov=float(np.nanmedian(n3c[b])))
        log(f"    band +/-{b:2d} : observed {M.fmt_rate(k, len(d))}")
        log(f"{'':17s}covered {exp_cov[b]:.4f} -> ratio {ratio:.3f}")
        log(f"{'':17s}RAW   pct : N2 {p2:5.1f} | N3 {p3:5.1f}"
            f"   (N3 covers {np.nanmedian(n3c[b]):.4f}, NOT {exp_cov[b]:.4f})")
        log(f"{'':17s}RATIO pct : N2 {r2:5.1f} | N3 {r3:5.1f}   <<< the comparable one")

    # ---- per-boundary breakdown ----------------------------------------------
    log(f"\n  PER-BOUNDARY BREAKDOWN at +/-{HEADLINE_BAND} min "
        "(§5 row 2; §3d's per-cell warning attached):")
    log("  NOTE: 17:00 is simultaneously a day open, a day close and the New York")
    log("        session close, so these rows OVERLAP and do not sum to the headline.")
    per = {}
    weekly_d = _weekly_dist(tm[ei], inv_r[ei], first_r, last_r)
    cats = dict(per_cat)
    cats["week_open"] = np.abs(tm - first_r[inv_r])
    cats["week_close"] = np.abs(tm - last_r[inv_r])
    order = ["week_open", "day_open", "session_open", "session_close",
             "day_close", "week_close"]
    for name in order:
        dd = cats[name][ei]
        k = int((dd <= HEADLINE_BAND).sum())
        e = float((cats[name] <= HEADLINE_BAND).mean())
        per[name] = dict(k=k, n=len(dd), share=k / len(dd), expected=e)
        flag = "  <<< cell n<30, descriptive only" if k < 30 else ""
        log(f"    {name:<14s} observed {k:4d}/{len(dd)} = {k/len(dd):.4f} | "
            f"expected {e:.4f} | ratio {k/len(dd)/e if e else float('nan'):.2f}{flag}")

    # §5 row 5 — the two week boundaries reported separately from the four intraday
    wk = np.minimum(cats["week_open"][ei], cats["week_close"][ei])
    intr = d_intra[ei]
    kw = int((wk <= HEADLINE_BAND).sum())
    ki = int((intr <= HEADLINE_BAND).sum())
    ew = float((np.minimum(cats["week_open"], cats["week_close"])
                <= HEADLINE_BAND).mean())
    ei_ = float((d_intra <= HEADLINE_BAND).mean())
    log(f"\n  §5 row 5 — the TWO WEEK boundaries reported separately from the FOUR")
    log(f"  intraday ones, so a later cross-source comparison with FXCM's 21:00 UTC")
    log(f"  week open is possible (`I-010` Q1 is OPEN):")
    log(f"    week boundaries only : {M.fmt_rate(kw, len(wk))} | expected {ew:.4f}")
    log(f"    intraday only        : {M.fmt_rate(ki, len(intr))} | expected {ei_:.4f}")

    # ---- closure weeks reported separately (§3c) ------------------------------
    wk_of = use.set_index("anchor_raw")["week"].to_dict()
    ext_week = np.array([wk_of[int(a)] for a in anchors_real[sel][ei]])
    clo = np.isin(ext_week, W.CLOSURE_WEEKS)
    log(f"\n  §3c — the six Dec/Jan closure weeks, INCLUDED and reported separately:")
    log(f"    closure weeks   : {M.fmt_rate(int((d[clo] <= HEADLINE_BAND).sum()), int(clo.sum()))}")
    log(f"    all other weeks : {M.fmt_rate(int((d[~clo] <= HEADLINE_BAND).sum()), int((~clo).sum()))}")

    # ---- sensitivity appendix (§7 step 7) -------------------------------------
    log("\n  PRE-REGISTERED SENSITIVITY APPENDIX — the five largest-range weeks in")
    log("  W-C'. An APPENDIX, never the headline, and NEVER a filtered re-run:")
    for r in W.largest_range_weeks(use).itertuples():
        log(f"    {r.week}  range {r.range_pips:7.1f} pips  ends {r.ends_weekday}"
            f"{'  (closure week)' if r.is_closure else ''}")

    return dict(arm=arm, n_weeks=nweeks, n_extremes=len(d), bands=res,
                per_boundary=per, thursday_weeks=thu,
                week_only=dict(k=kw, n=len(wk), expected=ew),
                intraday_only=dict(k=ki, n=len(intr), expected=ei_),
                n2={str(b): float(np.nanmedian(n2[b])) for b in BANDS},
                n3={str(b): float(np.nanmedian(n3[b])) for b in BANDS})


def main():
    lines = []

    def log(s=""):
        print(s)
        lines.append(s)

    log(M.header("PT-025",
                 "Do WEEKLY extremes cluster at the six printed boundaries?",
                 "window   : W-C' 2013-01-06 -> 2016-06-30 — IS the `D-035`\n"
                 "           DEVELOPMENT block. Re-issue of PT-002's W-C arm, which\n"
                 "           straddled the boundary by 546 days and was never run."))
    out = {}
    for arm in ("A", "B"):
        out[arm] = run_arm(arm, log)
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "pt025_report.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    with open(os.path.join(OUT, "pt025_results.json"), "w") as fh:
        json.dump(out, fh, indent=2, default=float)


if __name__ == "__main__":
    main()
