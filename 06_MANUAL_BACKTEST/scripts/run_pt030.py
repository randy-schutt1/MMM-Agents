#!/usr/bin/env python3
"""PT-030 — "they will not go below last week's peak formation": barrier survival (re-issue of PT-012)

THE FIRST BASELINE IS THE WHOLE TEST — `PT-030` §4
---------------------------------------------------
"DISTANCE TO A BARRIER DOMINATES THE BREACH RATE -- a barrier 200 pips away survives
longer than one 20 pips away for reasons that have nothing to do with market makers.
Any comparison that does not hold distance constant measures volatility and reports it
as doctrine."

So the sham barrier is placed at the SAME DISTANCE from the week's open as the real
one and only its identity changes.

THIS TEST LOSES TWO WEEKS TO THE DATA HOLE, NOT ONE — §3a″
-----------------------------------------------------------
  2014-06-01  EXCLUDED — no observable week open, so no survival clock
  2014-06-08  EXCLUDED — ITS BARRIER IS the 2014-06-01 week's high and low, drawn
              from a week missing 22 hours: a systematically TOO NARROW barrier,
              which would look easier to breach. "The one a careless run would miss" —
              that week's own data is clean, so nothing flags it.
Plus the two structural exclusions of §3a: 2013-01-06 (its predecessor is the corpus's
Tue-start fragment, not a week) and 2016-06-26 (truncated by the DEVELOPMENT boundary).

  182 anchors - 1 truncated - 1 first-week lag - 1 hole - 1 heir = 178 tested weeks
  178 x 2 barriers = 356 barrier observations

`C-001`: THIS TEST REPORTS A CURVE AND ADOPTS NO NUMBER — §3c
--------------------------------------------------------------
"A survival curve requires no choice. No session may read a modal survival time off
this curve and record it as resolving `C-001`. The contradiction is about what the
instructor SAID; this measures what price DID." The curve is censored at the week
close, so it speaks only to the first ~120 hours, and any reading of "three days" must
be taken against a 5-day trading week, not a 7-day calendar one.
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
CURVE_H = (12, 24, 36, 48, 60, 72, 84, 96, 108, 120)


def run_arm(arm, log):
    m15 = M.load_m15(arm)
    raw = M.load_m15("A")
    roster = W.build_weeks(arm, m15)
    keep_all = set(roster["anchor_raw"].tolist())
    anch = W.week_anchor(raw.tm)
    sel = np.array([int(a) in keep_all for a in anch])
    M.assert_development(raw.tm[sel], f"PT-030 universe / arm {arm}")
    tm, h, l, c, o = (m15.tm[sel], m15.h[sel], m15.l[sel], m15.c[sel], m15.o[sel])
    uniq, inv, n = week_index(anch[sel])
    rows = np.split(np.arange(len(tm)), np.cumsum(np.bincount(inv))[:-1])
    wk = roster.set_index("anchor_raw").loc[uniq]

    log(f"\n{'='*74}\n--- ARM {arm} ---\n{'='*74}")
    for ln in W.census_lines(roster):
        log("  " + ln)

    excl = {
        W.day2s(uniq[0] // W.DAY): "§3a — predecessor is the corpus's Tue-start "
                                   "fragment, not a week",
        W.TRUNCATED_FINAL_WEEK: "§3a — truncated by the DEVELOPMENT boundary",
        W.DATA_HOLE_WEEK: "§3a″ — DATA DEFECT, no observable week open",
        W.DATA_HOLE_HEIR_WEEK: "§3a″ — INHERITS the defect: its barrier IS the holed "
                               "week's high and low",
    }
    weeks = np.array([W.day2s(a // W.DAY) for a in uniq])
    tested = np.array([(i > 0) and (weeks[i] not in excl) for i in range(n)])
    log(f"\n  EXCLUSIONS, EVERY ONE APPLIED AND COUNTED BY NAME:")
    for k, v in excl.items():
        log(f"    {k}  {v}")
    log(f"  TESTED WEEKS: {int(tested.sum())}  -> "
        f"{2*int(tested.sum())} barrier observations   (§3b pre-registered: 178 / 356)")

    # ---- barriers, survival, depth, approach ---------------------------------
    hi_b = np.full(n, np.nan); lo_b = np.full(n, np.nan)
    for w in range(n):
        hi_b[w] = h[rows[w]].max(); lo_b[w] = l[rows[w]].min()

    def measure(barrier_hi, barrier_lo, mask):
        """Survival / breach / depth / approach for one barrier configuration."""
        out = dict(up_t=[], dn_t=[], up_br=[], dn_br=[], up_dep=[], dn_dep=[],
                   up_app=[], dn_app=[], toward=[], week=[])
        for w in range(n):
            if not mask[w]:
                continue
            idx = rows[w]
            t0 = tm[idx][0]
            bu, bl = barrier_hi[w], barrier_lo[w]
            net = c[idx][-1] - o[idx][0]
            up_hit = np.where(h[idx] > bu)[0]
            dn_hit = np.where(l[idx] < bl)[0]
            out["up_br"].append(len(up_hit) > 0)
            out["dn_br"].append(len(dn_hit) > 0)
            out["up_t"].append((tm[idx][up_hit[0]] - t0) / 60 if len(up_hit) else np.nan)
            out["dn_t"].append((tm[idx][dn_hit[0]] - t0) / 60 if len(dn_hit) else np.nan)
            out["up_dep"].append((h[idx].max() - bu) / M.PIP if len(up_hit) else np.nan)
            out["dn_dep"].append((bl - l[idx].min()) / M.PIP if len(dn_hit) else np.nan)
            out["up_app"].append((bu - h[idx].max()) / M.PIP if not len(up_hit) else np.nan)
            out["dn_app"].append((l[idx].min() - bl) / M.PIP if not len(dn_hit) else np.nan)
            out["toward"].append(1 if net > 0 else -1)
            out["week"].append(weeks[w])
        return {k: np.array(v) for k, v in out.items()}

    prev_hi = np.r_[np.nan, hi_b[:-1]]
    prev_lo = np.r_[np.nan, lo_b[:-1]]

    # ---- BASELINES FIRST -----------------------------------------------------
    w_open_px = np.array([o[rows[w]][0] for w in range(n)])
    d_up = prev_hi - w_open_px
    d_dn = w_open_px - prev_lo
    rng = np.random.default_rng(M.SEED)

    log(f"\n  PRIMARY BASELINE (§4 arm 1) — THE SHAM BARRIER, placed at the SAME")
    log(f"  DISTANCE from the week's open as the real one, direction drawn at random.")
    log(f"  {M.ITERATIONS} draws, seed {M.SEED}. §4: 'Distance to a barrier dominates")
    log(f"  the breach rate ... any comparison that does not hold distance constant")
    log(f"  measures volatility and reports it as doctrine.'")
    b1_up, b1_dn = np.full(M.ITERATIONS, np.nan), np.full(M.ITERATIONS, np.nan)
    for it in range(M.ITERATIONS):
        s = rng.choice([-1, 1], size=n)
        sh_hi = w_open_px + np.where(s > 0, np.abs(d_up), np.abs(d_dn))
        sh_lo = w_open_px - np.where(s > 0, np.abs(d_dn), np.abs(d_up))
        r = measure(sh_hi, sh_lo, tested)
        b1_up[it] = r["up_br"].mean(); b1_dn[it] = r["dn_br"].mean()
    log(f"    sham upper-barrier breach rate: {M.dist_line(b1_up)}")
    log(f"    sham lower-barrier breach rate: {M.dist_line(b1_dn)}")

    log(f"\n  THIRD BASELINE (§4 arm 3) — barrier taken from a DIFFERENT, RANDOMLY")
    log(f"  CHOSEN week, SCALED to the same distance. Implemented as: the DONOR week")
    log(f"  supplies which side is nearer, this week supplies the distances — the two")
    log(f"  requirements the pre-registration states together. It differs from arm 1")
    log(f"  only in drawing the side from the EMPIRICAL distribution rather than")
    log(f"  uniformly, and both are reported.")
    b3_up, b3_dn = np.full(M.ITERATIONS, np.nan), np.full(M.ITERATIONS, np.nan)
    near_up = np.abs(d_up) <= np.abs(d_dn)
    for it in range(M.ITERATIONS):
        donor = rng.integers(1, n, size=n)
        s = np.where(near_up[donor], 1, -1)
        sh_hi = w_open_px + np.where(s > 0, np.minimum(np.abs(d_up), np.abs(d_dn)),
                                     np.maximum(np.abs(d_up), np.abs(d_dn)))
        sh_lo = w_open_px - np.where(s > 0, np.maximum(np.abs(d_up), np.abs(d_dn)),
                                     np.minimum(np.abs(d_up), np.abs(d_dn)))
        r = measure(sh_hi, sh_lo, tested)
        b3_up[it] = r["up_br"].mean(); b3_dn[it] = r["dn_br"].mean()
    log(f"    upper: {M.dist_line(b3_up)}    lower: {M.dist_line(b3_dn)}")

    log(f"\n  SECOND BASELINE (§4 arm 2) — N3 week-anchor shift: 'the previous week's")
    log(f"  extreme computed on SHIFTED week boundaries', {M.ITERATIONS} draws.")
    lo_e, hi_e = raw.tm[sel].min(), raw.tm[sel].max()
    hole = W.dt2m(W.DATA_HOLE_WEEK)
    b2_up, b2_dn = [], []
    for off in W.n3_week_shifts():
        a_ = W.week_anchor(raw.tm[sel] - int(off)) + int(off)
        u2, i2 = np.unique(a_, return_inverse=True)
        good = ((u2 >= lo_e) & (u2 + W.DAY * 5 <= hi_e)
                & ~((u2 < hole + W.DAY * 8) & (u2 + W.DAY * 5 > hole)))
        r2 = np.split(np.arange(len(tm)), np.cumsum(np.bincount(i2))[:-1])
        hb = np.array([h[i].max() if len(i) else np.nan for i in r2])
        lb = np.array([l[i].min() if len(i) else np.nan for i in r2])
        u_, d_ = [], []
        for w in range(1, len(r2)):
            if not good[w] or not good[w - 1] or len(r2[w]) == 0:
                continue
            u_.append(bool((h[r2[w]] > hb[w - 1]).any()))
            d_.append(bool((l[r2[w]] < lb[w - 1]).any()))
        if u_:
            b2_up.append(np.mean(u_)); b2_dn.append(np.mean(d_))
    b2_up = np.array(b2_up); b2_dn = np.array(b2_dn)
    log(f"    upper: {M.dist_line(b2_up)}    lower: {M.dist_line(b2_dn)}")

    # ---- THE REAL BARRIER ----------------------------------------------------
    R = measure(prev_hi, prev_lo, tested)
    N = len(R["up_br"])
    log(f"\n  {'='*70}\n  OBSERVED — the real barrier, read after all three baselines")
    log(f"  {'='*70}")
    log(f"  MEASURE 2 — breach rate, n = {N} weeks / {2*N} barrier observations")
    log(f"    upper barrier (last week's HIGH) breached: "
        f"{M.fmt_rate(int(R['up_br'].sum()), N)}")
    log(f"    lower barrier (last week's LOW)  breached: "
        f"{M.fmt_rate(int(R['dn_br'].sum()), N)}")
    both = int((R["up_br"] & R["dn_br"]).sum())
    nei = int((~R["up_br"] & ~R["dn_br"]).sum())
    log(f"    both breached {both}    neither breached {nei}")
    pu = M.percentile_of(R["up_br"].mean(), b1_up)
    pd = M.percentile_of(R["dn_br"].mean(), b1_dn)
    log(f"    vs the DISTANCE-MATCHED sham (§4 arm 1): upper pct {pu:.1f}, "
        f"lower pct {pd:.1f}")
    log(f"    vs N3 (§4 arm 2)  : upper pct "
        f"{M.percentile_of(R['up_br'].mean(), b2_up):.1f}, lower pct "
        f"{M.percentile_of(R['dn_br'].mean(), b2_dn):.1f}")
    log(f"    vs donor-side (§4 arm 3): upper pct "
        f"{M.percentile_of(R['up_br'].mean(), b3_up):.1f}, lower pct "
        f"{M.percentile_of(R['dn_br'].mean(), b3_dn):.1f}")

    log(f"\n  MEASURE 1 — SURVIVAL CURVE, censored at the week close (§3c: the curve")
    log(f"  speaks only to the first ~120 h, and ADOPTS NO DAY COUNT — `C-001` is NOT")
    log(f"  resolved by any number below):")
    log(f"    hours   " + "".join(f"{x:>7d}" for x in CURVE_H))
    for nm, t in (("upper", R["up_t"]), ("lower", R["dn_t"])):
        surv = [float(np.mean(~(t <= x))) for x in CURVE_H]
        log(f"    {nm:<6s}" + "".join(f"{s:7.3f}" for s in surv))
    log(f"    median hours to breach — upper {np.nanmedian(R['up_t']):.1f}, "
        f"lower {np.nanmedian(R['dn_t']):.1f}")

    log(f"\n  MEASURE 3 — APPROACH (un-breached barriers only) and")
    log(f"  MEASURE 4 — BREACH DEPTH (breached only). §3b: if either subset falls")
    log(f"  under 30 every figure from it carries the §4.1 label.")
    for nm, app, dep in (("upper", R["up_app"], R["up_dep"]),
                         ("lower", R["dn_app"], R["dn_dep"])):
        na = int(np.isfinite(app).sum()); nd = int(np.isfinite(dep).sum())
        la = "  <<< SAMPLE INSUFFICIENT — descriptive only" if na < 30 else ""
        ld = "  <<< SAMPLE INSUFFICIENT — descriptive only" if nd < 30 else ""
        log(f"    {nm} approach : median {np.nanmedian(app):7.1f} pips  n = {na}{la}")
        log(f"    {nm} depth    : median {np.nanmedian(dep):7.1f} pips  n = {nd}{ld}")

    log(f"\n  DIRECTIONAL CONDITIONING — the barrier the week's net direction runs")
    log(f"  TOWARD vs AWAY FROM. §3b requires the FOUR CELL COUNTS beside the rates:")
    # A week whose net direction is UP runs TOWARD last week's HIGH and AWAY FROM
    # last week's LOW; a net-DOWN week is the mirror. The first implementation took
    # the upper barrier as "toward" for BOTH, which mislabelled the two net-down
    # cells as each other — it reported net-DOWN/toward = 0.266 when 0.266 is the
    # rate at which a FALLING week breaches the barrier ABOVE it.
    tw = R["toward"]
    cells = {}
    for dname, mask in (("net UP  ", tw == 1), ("net DOWN", tw == -1)):
        toward = R["up_br"] if dname.strip() == "net UP" else R["dn_br"]
        away = R["dn_br"] if dname.strip() == "net UP" else R["up_br"]
        for bname, br in (("toward", toward), ("away  ", away)):
            k = int(br[mask].sum()); m = int(mask.sum())
            cells[f"{dname}/{bname}"] = (k, m)
    for k, (a, b) in cells.items():
        log(f"    {k}: {M.fmt_rate(a, b)}")

    log("\n  PRE-REGISTERED SENSITIVITY APPENDIX — five largest-range weeks:")
    for r in W.largest_range_weeks(roster[roster["week"].isin(R["week"])]).itertuples():
        log(f"    {r.week}  range {r.range_pips:7.1f} pips")

    return dict(arm=arm, n_tested=N, up_breach=int(R["up_br"].sum()),
                dn_breach=int(R["dn_br"].sum()), both=both, neither=nei,
                sham_up=float(np.median(b1_up)), sham_dn=float(np.median(b1_dn)),
                sham_up_pct=pu, sham_dn_pct=pd,
                n3_up=float(np.median(b2_up)), n3_dn=float(np.median(b2_dn)),
                donor_up=float(np.median(b3_up)), donor_dn=float(np.median(b3_dn)),
                up_t_median=float(np.nanmedian(R["up_t"])),
                dn_t_median=float(np.nanmedian(R["dn_t"])),
                up_app=float(np.nanmedian(R["up_app"])),
                dn_app=float(np.nanmedian(R["dn_app"])),
                up_dep=float(np.nanmedian(R["up_dep"])),
                dn_dep=float(np.nanmedian(R["dn_dep"])),
                cells={k: list(v) for k, v in cells.items()},
                survival_upper=[float(np.mean(~(R["up_t"] <= x))) for x in CURVE_H],
                survival_lower=[float(np.mean(~(R["dn_t"] <= x))) for x in CURVE_H],
                curve_hours=list(CURVE_H))


def main():
    lines = []

    def log(s=""):
        print(s)
        lines.append(s)

    log(M.header("PT-030", "Is the previous week's extreme a barrier?",
                 "window   : W-C' 2013-01-06 -> 2016-06-30. Re-issue of PT-012.\n"
                 "⚠ THIS TEST LOSES TWO WEEKS TO THE DATA HOLE (§3a″): 2014-06-01\n"
                 "  and 2014-06-08, whose BARRIER is drawn from the holed week.\n"
                 "⚠ Breaches are BID-SIDE (§0b). No execution claim is derived.\n"
                 "⚠ `C-001`: a curve is reported and NO day count is adopted."))
    out = {}
    for arm in ("A", "B"):
        out[arm] = run_arm(arm, log)
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "pt030_report.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    with open(os.path.join(OUT, "pt030_results.json"), "w") as fh:
        json.dump(out, fh, indent=2, default=float)


if __name__ == "__main__":
    main()
