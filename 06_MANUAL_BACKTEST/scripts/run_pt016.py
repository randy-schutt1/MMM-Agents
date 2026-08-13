#!/usr/bin/env python3
"""PT-016 — "Asian range... less than 50" as a filter.

Pre-registration: `PRE_REGISTERED/PT-016_asian_range_under_fifty_pips_filter.md`
Depends on: PT-014 (`BT_V04_0001`) for the excursion distribution this test conditions.

PROVENANCE CAVEAT (`PT-016` §1a) — binding on this run: the `< 50` threshold is the
course author's, spoken in V03 and printed on his own card, but he is quoting teaching
that is NOT in this 21-video library ("Steve said"). Whatever this finds, `< 50 pips`
may not enter `12_MASTER_SPEC/` or `13_MACHINE_SPEC/` on the strength of it.

THE SAFEGUARD IS THE CONTINUOUS CURVE. A binary split at a threshold from an
uncapturable lesson invites the reader to believe the threshold; the 10-pip binned curve
shows whether anything happens at 50 at all. Both are computed, and the curve and the
random-median control are computed BEFORE the 50-pip cut is applied (`PT-016` §7 step 3).

usage: python3 run_pt016.py
"""
import json
import os
import sys

import numpy as np

import mmm_lib as L

OUT_DIR = os.path.join(L.ROOT, "06_MANUAL_BACKTEST", "V03", "data")


def measures(days, m15, grid):
    """PT-016 §3 outcome measures (a), (b), (c) — one row per session day."""
    hi = np.maximum(days["post_hi"].values - days["box_hi"].values, 0.0) / L.PIP
    lo = np.maximum(days["box_lo"].values - days["post_lo"].values, 0.0) / L.PIP
    a_max_exc = np.maximum(hi, lo)                                    # (a)

    day_hi = np.maximum(days["box_hi"].values, days["post_hi"].values)
    day_lo = np.minimum(days["box_lo"].values, days["post_lo"].values)
    b_hi_beyond = days["post_hi"].values > days["box_hi"].values      # (b)
    b_lo_beyond = days["post_lo"].values < days["box_lo"].values
    day_tr = (day_hi - day_lo) / L.PIP

    # (c) the PT-001/PT-015 trade proxy: FIRST close 25-50 pips beyond an edge.
    # NOTE this is a different trigger from PT-015's stratum assignment, which takes the
    # first close >= 10 and then classifies it. PT-016 §3 names this one; it is used as
    # named and the difference is reported rather than reconciled.
    exc, side, when, _ = L.first_close_beyond(m15, days, lo=25.0, hi=50.0)
    rows = np.full(len(days), -1)
    dirs = np.zeros(len(days), dtype=int)
    for i in range(len(days)):
        if not np.isfinite(exc[i]):
            continue
        r = grid.lookup(days["sd"].values[i], when[i])
        if r is None:
            continue
        d = 1 if side[i] > 0 else 0
        if not grid.valid[r, d]:
            continue
        rows[i] = r
        dirs[i] = d
    return dict(a_max_exc=a_max_exc, b_hi_beyond=b_hi_beyond, b_lo_beyond=b_lo_beyond,
                b_any_beyond=(b_hi_beyond | b_lo_beyond), day_tr=day_tr,
                a_norm=np.where(day_tr > 0, a_max_exc / day_tr, np.nan),
                trig_rows=rows, trig_dirs=dirs, trig_exc=exc)


def group_stats(grid, M, mask, label, log, quiet=False):
    n = int(mask.sum())
    if n == 0:
        if not quiet:
            log(f"  {label}: n = 0")
        return dict(n=0)
    a = M["a_max_exc"][mask]
    an = M["a_norm"][mask]
    beyond = M["b_any_beyond"][mask]
    bhi = M["b_hi_beyond"][mask]
    blo = M["b_lo_beyond"][mask]
    bboth = bhi & blo
    r = M["trig_rows"][mask]
    d = M["trig_dirs"][mask]
    ok = r >= 0
    out = dict(n=n, median_exc=float(np.median(a)), mean_exc=float(a.mean()),
               median_exc_norm=float(np.nanmedian(an)),
               share_extreme_beyond=float(beyond.mean()),
               share_hi_beyond=float(bhi.mean()),
               share_lo_beyond=float(blo.mean()),
               share_both_beyond=float(bboth.mean()),
               n_trig=int(ok.sum()))
    if ok.any():
        oc = grid.outcome[r[ok], d[ok]]
        pl = grid.pnl_pips[r[ok], d[ok]]
        res = oc != 0
        out["hit_rate"] = float((oc[res] == 1).mean()) if res.any() else float("nan")
        out["n_resolved"] = int(res.sum())
        out["n_target"] = int((oc == 1).sum())
        out["expectancy"] = float(np.nanmean(pl))
    if not quiet:
        log(f"  {label}: {L.nlabel(n)}")
        log(f"    (a) max excursion beyond box : median {out['median_exc']:.1f} pips  "
            f"mean {out['mean_exc']:.1f}")
        log(f"    (a) volatility-normalised    : median {out['median_exc_norm']:.3f} "
            f"of the day's own true range")
        # (b) is reported in three parts. The "either edge" form is 1.000 by
        # construction on this corpus — BT_V04_0001 §4 found every one of 515 days
        # cleared at least one edge — so reporting only that would be reporting a
        # tautology. The per-edge and both-edge forms are the informative ones.
        log(f"    (b) day's HIGH beyond box hi : {L.fmt_rate(int(bhi.sum()), n)}")
        log(f"    (b) day's LOW  beyond box lo : {L.fmt_rate(int(blo.sum()), n)}")
        log(f"    (b) BOTH extremes beyond box : {L.fmt_rate(int(bboth.sum()), n)}")
        log(f"    (b) either edge (tautological here): "
            f"{L.fmt_rate(int(beyond.sum()), n)}")
        log(f"    (c) trigger fired on         : {L.fmt_rate(int(ok.sum()), n)} of days")
        if ok.any():
            log(f"    (c) hit rate (of resolved)   : "
                f"{L.fmt_rate(out['n_target'], out['n_resolved'])}")
            log(f"    (c) expectancy               : {out['expectancy']:+.2f} pips  "
                f"boot 95% CI {L.boot_ci(grid.pnl_pips[r[ok], d[ok]], stat=np.mean)}")
    return out


def run_arm(arm, log):
    m15 = L.window(L.load_m15(arm), "W-B")
    m1 = L.window(L.load_m1(arm), "W-B")
    days = L.build_days(m15)
    grid = L.TradeGrid(m1, m15)
    M = measures(days, m15, grid)
    box = days["box_range_pips"].values

    log(f"\n----- ARM {arm} -----")
    log(f"COMPLETENESS (C-6): {L.completeness_line(days)}")
    log(f"session days: {len(days)}   trade grid: {len(grid.entry_tm):,} eligible "
        f"entry bars x 2 directions")

    # ---- STEP 3 of `PT-016` §7: the distribution and the random-median control FIRST,
    # ---- before the 50-pip cut is applied anywhere.
    log("\n[1. THE BOX-RANGE DISTRIBUTION — computed before the 50-pip cut is applied]")
    log(f"  median {np.median(box):.1f}  mean {box.mean():.1f}  "
        f"p10 {np.percentile(box,10):.1f}  p25 {np.percentile(box,25):.1f}  "
        f"p75 {np.percentile(box,75):.1f}  p90 {np.percentile(box,90):.1f}  "
        f"max {box.max():.1f}")
    edges = np.arange(0, 121, 10.0)
    cnt, _ = np.histogram(np.clip(box, 0, 119.99), bins=np.append(edges, 1e9))
    for e, c in zip(edges, cnt):
        mark = "   <<< the instructor's cut, V03 [00:44:48]" if e == 50 else ""
        log(f"    [{e:5.0f},{e+10:5.0f})  {c:4d}  "
            f"{'#'*int(round(50*c/max(cnt.max(),1)))}{mark}")
    log(f"  share of days with box < 50 pips: "
        f"{L.fmt_rate(int((box < 50).sum()), len(box))}")

    log("\n[2. THE CONTINUOUS CURVE — outcome as a function of box range, 10-pip bins]")
    log("   (the safeguard: it shows whether anything happens AT 50, without anyone "
        "having chosen 50)")
    log(f"    {'bin':>12} {'n':>5} {'med exc':>9} {'exc/TR':>8} {'both':>9} "
        f"{'trig':>6} {'hit':>7} {'exp':>8}")
    curve = []
    for e in edges:
        m = (box >= e) & (box < e + 10) if e < 120 else (box >= 120)
        if not m.any():
            continue
        g = group_stats(grid, M, m, "", log, quiet=True)
        curve.append(dict(lo=float(e), **{k: v for k, v in g.items()}))
        hit = g.get("hit_rate", float("nan"))
        exp = g.get("expectancy", float("nan"))
        log(f"    [{e:4.0f},{e+10:4.0f}) {g['n']:5d} {g['median_exc']:9.1f} "
            f"{g['median_exc_norm']:8.3f} {g['share_both_beyond']:9.3f} "
            f"{g['n_trig']:6d} "
            f"{('%.3f'%hit) if np.isfinite(hit) else '   n/a':>7} "
            f"{('%+.2f'%exp) if np.isfinite(exp) else '   n/a':>8}")

    log("\n[3. SECOND BASELINE — the random-median split (`PT-016` §4)]")
    med = float(np.median(box))
    lowm, highm = box < med, box >= med
    log(f"  median split point (no doctrinal claim attached): {med:.1f} pips")
    gl = group_stats(grid, M, lowm, f"median-LOW (box < {med:.1f})", log)
    gh = group_stats(grid, M, highm, f"median-HIGH (box >= {med:.1f})", log)
    sep_med = dict(
        exc=float(gl["median_exc"] - gh["median_exc"]),
        extreme=float(gl["share_both_beyond"] - gh["share_both_beyond"]),
        hit=float(gl.get("hit_rate", np.nan) - gh.get("hit_rate", np.nan)),
        exp=float(gl.get("expectancy", np.nan) - gh.get("expectancy", np.nan)))

    log("\n[4. PRIMARY BASELINE — N1 matched random entry WITHIN EACH ARM (`PT-016` §4)]")
    pool = np.where(grid.valid.any(1))[0]
    n1 = {}
    for nm, m in (("L", box < 50), ("H", box >= 50)):
        r = M["trig_rows"][m]; d = M["trig_dirs"][m]
        ok = r >= 0
        if not ok.any():
            log(f"  N1 arm {nm}: no triggered trades")
            n1[nm] = None
            continue
        tgt, expd = L.n1_outcome(grid, d[ok], pool=pool)
        tgt_r, exp_r = L.n1_outcome(grid, d[ok], pool=pool, random_direction=True)
        n1[nm] = dict(tgt=tgt, exp=expd)
        log(f"  N1 arm {nm} (n = {int(ok.sum())}, direction matched, 1,000 iters, "
            f"seed {L.SEED}):")
        log(f"      hit rate   {L.dist_line(tgt)}")
        log(f"      expectancy {L.dist_line(expd)} pips")
        log(f"    N1 secondary, RANDOM direction: hit {L.dist_line(tgt_r)}; "
            f"expectancy {L.dist_line(exp_r)} pips")

    log("\n[5. RULE ARM — the instructor's 50-pip cut]")
    gL = group_stats(grid, M, box < 50, "arm L  box range < 50 pips", log)
    gH = group_stats(grid, M, box >= 50, "arm H  box range >= 50 pips", log)
    for nm, g in (("L", gL), ("H", gH)):
        if n1.get(nm) and "hit_rate" in g:
            g["pct_hit_vs_N1"] = L.percentile_of(g["hit_rate"], n1[nm]["tgt"])
            g["pct_exp_vs_N1"] = L.percentile_of(g["expectancy"], n1[nm]["exp"])
            log(f"  arm {nm} vs its own N1: hit rate pct {g['pct_hit_vs_N1']:.1f}; "
                f"expectancy pct {g['pct_exp_vs_N1']:.1f}")

    log("\n[6. DOES THE 50-PIP CUT SEPARATE BETTER THAN THE MEANINGLESS ONE?]")
    sep_50 = dict(
        exc=float(gL["median_exc"] - gH["median_exc"]),
        extreme=float(gL["share_both_beyond"] - gH["share_both_beyond"]),
        hit=float(gL.get("hit_rate", np.nan) - gH.get("hit_rate", np.nan)),
        exp=float(gL.get("expectancy", np.nan) - gH.get("expectancy", np.nan)))
    log(f"    {'measure':<28}{'50-pip cut':>14}{'median cut':>14}")
    for k, lab in (("exc", "median excursion L-H"),
                   ("extreme", "share BOTH-edge breach L-H"),
                   ("hit", "hit rate L-H"), ("exp", "expectancy L-H (pips)")):
        log(f"    {lab:<28}{sep_50[k]:>14.3f}{sep_med[k]:>14.3f}")
    log("  If the median cut separates as well as the 50-pip cut, then 50 is doing")
    log("  nothing that 'big box vs small box' does not already do (`PT-016` §4).")

    log("\n[7. THIRD BASELINE — volatility control, measure (a) normalised]")
    log(f"  raw    : arm L median excursion {gL['median_exc']:.1f} vs "
        f"arm H {gH['median_exc']:.1f} pips  (diff {sep_50['exc']:+.1f})")
    log(f"  normed : arm L {gL['median_exc_norm']:.3f} vs arm H "
        f"{gH['median_exc_norm']:.3f} of the day's own true range  "
        f"(diff {gL['median_exc_norm']-gH['median_exc_norm']:+.3f})")
    aL = M["a_max_exc"][box < 50]; aH = M["a_max_exc"][box >= 50]
    o, p, _ = L.perm_diff(aL, aH, stat=np.median)
    log(f"  permutation on raw excursion   : diff {o:+.1f} pips, two-sided p = {p:.3f}")
    nL = M["a_norm"][box < 50]; nH = M["a_norm"][box >= 50]
    o2, p2, _ = L.perm_diff(nL, nH, stat=np.median)
    log(f"  permutation on normalised      : diff {o2:+.3f}, two-sided p = {p2:.3f}")

    return dict(arm=arm, n_days=int(len(days)),
                box_median=float(np.median(box)),
                share_box_lt50=float((box < 50).mean()),
                armL=gL, armH=gH, medianL=gl, medianH=gh,
                sep_50=sep_50, sep_med=sep_med, curve=curve,
                perm_raw_p=p, perm_norm_p=p2,
                n1={k: (None if v is None else dict(hit=L.dist_line(v["tgt"]),
                                                    exp=L.dist_line(v["exp"])))
                    for k, v in n1.items()})


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    lines = []

    def log(s=""):
        print(s)
        lines.append(s)

    log(L.header("PT-016", "'Asian range... less than 50' as a filter (W-B)",
                 "window   : W-B 2014-01-05 -> 2015-12-31 (wholly inside DEVELOPMENT)"))
    log("PRE-REG  : PRE_REGISTERED/PT-016_asian_range_under_fifty_pips_filter.md")
    log("CAVEAT   : `PT-016` §1a — the threshold is the course author's but is quoted")
    log("           from teaching OUTSIDE this 21-video library. No result here")
    log("           authorises `< 50 pips` as a course rule or a spec entry.")
    log("ORDER    : distribution + continuous curve + random-median control are")
    log("           computed BEFORE the 50-pip cut is applied (`PT-016` §7 step 3).")

    res = {}
    for arm in ("A", "B"):
        res[arm] = run_arm(arm, log)

    log("\n" + "=" * 78)
    log("BOTH ARMS SIDE BY SIDE — `D-031` requires both, always")
    log("=" * 78)
    log(f"{'':34}{'ARM A':>12}{'ARM B':>12}")
    rows = [("median box range (pips)", lambda r: r["box_median"], "{:.1f}"),
            ("share of days box < 50", lambda r: r["share_box_lt50"], "{:.3f}"),
            ("arm L n", lambda r: r["armL"]["n"], "{:.0f}"),
            ("arm H n", lambda r: r["armH"]["n"], "{:.0f}"),
            ("arm L median excursion", lambda r: r["armL"]["median_exc"], "{:.1f}"),
            ("arm H median excursion", lambda r: r["armH"]["median_exc"], "{:.1f}"),
            ("arm L exc/TR", lambda r: r["armL"]["median_exc_norm"], "{:.3f}"),
            ("arm H exc/TR", lambda r: r["armH"]["median_exc_norm"], "{:.3f}"),
            ("arm L hit rate", lambda r: r["armL"].get("hit_rate", float('nan')), "{:.3f}"),
            ("arm H hit rate", lambda r: r["armH"].get("hit_rate", float('nan')), "{:.3f}"),
            ("arm L expectancy", lambda r: r["armL"].get("expectancy", float('nan')), "{:+.2f}"),
            ("arm H expectancy", lambda r: r["armH"].get("expectancy", float('nan')), "{:+.2f}"),
            ("perm p, raw excursion", lambda r: r["perm_raw_p"], "{:.3f}"),
            ("perm p, normalised", lambda r: r["perm_norm_p"], "{:.3f}")]
    for lab, f, fmt in rows:
        log(f"{lab:<34}{fmt.format(f(res['A'])):>12}{fmt.format(f(res['B'])):>12}")

    with open(os.path.join(OUT_DIR, "pt016_results.json"), "w") as fh:
        json.dump(res, fh, indent=1, default=str)
    with open(os.path.join(OUT_DIR, "pt016_report.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print("\nwritten:", os.path.join(OUT_DIR, "pt016_results.json"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
