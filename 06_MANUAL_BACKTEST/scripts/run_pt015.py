#!/usr/bin/env python3
"""PT-015 — Does a ceiling exist? Excursions beyond 50 pips versus 25-50.

Pre-registration: `PRE_REGISTERED/PT-015_does_the_fifty_pip_ceiling_exist.md`
Depends on: PT-014 (`BT_V04_0001`), which reported in advance that S3 will be thin and
S4 empty under this test's own assignment rule. That forecast is NOT acted on here —
PT-015 runs exactly as pre-registered and reports the shortfall.

STRATUM MERGING IS FORBIDDEN AFTER THE FACT (`PT-015` §3). S3 and S4 are reported at
whatever n they have, with the `SAMPLE INSUFFICIENT` label, and are not collapsed into
a neighbour however reasonable that would look.

usage: python3 run_pt015.py
"""
import json
import os
import sys

import numpy as np

import mmm_lib as L

OUT_DIR = os.path.join(L.ROOT, "06_MANUAL_BACKTEST", "V04", "data")

# The instructor's own numbers (`PT-015` §3: 10 / 25-50 / 100 are the three severities
# named at V02 [00:44:59]; 25-50 is the criterion at V04 [00:15:43]). Not this session's.
STRATA = [("S1", 10.0, 24.999999, "10 <= e < 25"),
          ("S2", 25.0, 50.0, "25 <= e <= 50"),
          ("S3", 50.000001, 100.0, "50 < e <= 100"),
          ("S4", 100.000001, np.inf, "e > 100")]


def day_true_range(days):
    """Whole-session-day range (box window and post-box window together), in pips."""
    hi = np.maximum(days["box_hi"].values, days["post_hi"].values)
    lo = np.minimum(days["box_lo"].values, days["post_lo"].values)
    return (hi - lo) / L.PIP


def prior_true_range(days):
    """`PT-015` §4 third arm's matching variable: the day's PRIOR true range.

    Prior, not current — a matching variable known before the trigger cannot leak the
    outcome into the match. Uses the previous *included* session day; the first day of
    the window has none and is nan.
    """
    tr = day_true_range(days)
    out = np.full(len(tr), np.nan)
    out[1:] = tr[:-1]
    return out


def trades_for(grid, days, mask, exc, side, when):
    """Resolve the pre-registered proxy trade for every day in `mask`.

    Direction is AWAY from the box, matching V04's geometry (`PT-015` §3): breach high
    -> short, breach low -> long. Stop 18 / target 50, the instructor's numbers.
    """
    rows, dirs, keep = [], [], []
    for i in np.where(mask)[0]:
        r = grid.lookup(days["sd"].values[i], when[i])
        if r is None:
            continue
        d = 1 if side[i] > 0 else 0          # 1 = short, 0 = long
        if not grid.valid[r, d]:
            continue
        rows.append(r); dirs.append(d); keep.append(i)
    return np.array(rows, dtype=int), np.array(dirs, dtype=int), np.array(keep, dtype=int)


def describe(grid, rows, dirs, label, log):
    if len(rows) == 0:
        log(f"  {label}: n = 0 — no trades")
        return dict(n=0)
    oc = grid.outcome[rows, dirs]
    pl = grid.pnl_pips[rows, dirs]
    mae = grid.mae_pips[rows, dirs]
    ex = grid.exit_min[rows, dirs]
    res = oc != 0
    n = len(rows)
    n_res = int(res.sum())
    n_tgt = int((oc == 1).sum())
    n_stp = int((oc == -1).sum())
    d = dict(n=n, n_resolved=n_res, n_target=n_tgt, n_stop=n_stp,
             n_open=int((oc == 0).sum()),
             hit_rate=(n_tgt / n_res if n_res else float("nan")),
             expectancy=float(np.nanmean(pl)),
             median_mae=float(np.nanmedian(mae)),
             p90_mae=float(np.nanpercentile(mae, 90)),
             mae_gt_stop=float(np.mean(mae[np.isfinite(mae)] >= grid.stop_pips)),
             median_hold=float(np.nanmedian(ex)),
             ties=int(grid.tie[rows, dirs].sum()))
    log(f"  {label}: {L.nlabel(n)}")
    log(f"    target / stop / open        : {n_tgt} / {n_stp} / {d['n_open']}")
    log(f"    hit rate (of resolved)      : {L.fmt_rate(n_tgt, n_res)}")
    log(f"    expectancy (pips/trade)     : {d['expectancy']:+.2f}   "
        f"boot 95% CI {L.boot_ci(pl, stat=np.mean)}")
    log(f"    MAE median / p90 (pips)     : {d['median_mae']:.1f} / {d['p90_mae']:.1f}")
    log(f"    median hold to exit (min)   : {d['median_hold']:.0f}")
    log(f"    intrabar stop/target ties   : {d['ties']} (convention C-4, stop first)")
    return d


def run_arm(arm, log):
    m15 = L.window(L.load_m15(arm), "W-B")
    m1 = L.window(L.load_m1(arm), "W-B")
    days = L.build_days(m15)
    exc, side, when, _ = L.first_close_beyond(m15, days, lo=10.0, hi=np.inf)

    log(f"\n----- ARM {arm} -----")
    log(f"COMPLETENESS (C-6): {L.completeness_line(days)}")
    log(f"session days: {len(days)}   days with a first qualifying close (>=10 pips): "
        f"{int(np.isfinite(exc).sum())}")

    grid = L.TradeGrid(m1, m15)
    log(f"trade grid: {len(grid.entry_tm):,} eligible M15 entry bars x 2 directions, "
        f"stop {grid.stop_pips:.0f} / target {grid.target_pips:.0f}, resolved on M1")

    masks = {}
    for nm, lo, hi, _lab in STRATA:
        masks[nm] = np.isfinite(exc) & (exc >= lo) & (exc <= hi)

    # ---------------- BASELINES FIRST (`COMMON_PROTOCOL.md` §9 rule 1) ---------------
    log("\n[BASELINES — run and printed BEFORE any stratum's result is read]")
    pool = np.where(grid.valid.any(1))[0]
    base = {}
    for nm, _, _, _lab in STRATA:
        rows, dirs, keep = trades_for(grid, days, masks[nm], exc, side, when)
        if len(rows) == 0:
            log(f"  N1 {nm}: n = 0 — no baseline possible")
            base[nm] = None
            continue
        tgt, expd = L.n1_outcome(grid, dirs, pool=pool)
        tgt_r, exp_r = L.n1_outcome(grid, dirs, pool=pool, random_direction=True)
        mae_d = L.n1_matched_random(grid, dirs, "mae_pips", pool=pool, agg="median")
        base[nm] = dict(tgt=tgt, exp=expd, tgt_r=tgt_r, exp_r=exp_r, mae=mae_d,
                        n=len(rows))
        log(f"  N1 {nm} (n = {len(rows)}, direction matched, 1,000 iters, seed "
            f"{L.SEED}):")
        log(f"      hit rate   {L.dist_line(tgt)}")
        log(f"      expectancy {L.dist_line(expd)} pips")
        log(f"      median MAE {L.dist_line(mae_d)} pips")
        log(f"    N1 secondary, RANDOM direction (`D-029`):")
        log(f"      hit rate   {L.dist_line(tgt_r)}")
        log(f"      expectancy {L.dist_line(exp_r)} pips")

    # ---------------- RULE ARM ----------------
    log("\n[RULE ARM — the four pre-registered strata, NOT merged]")
    out = {}
    for nm, lo, hi, lab in STRATA:
        rows, dirs, keep = trades_for(grid, days, masks[nm], exc, side, when)
        d = describe(grid, rows, dirs, f"{nm}  {lab} pips", log)
        d["rows"], d["dirs"], d["keep"] = rows, dirs, keep
        if base.get(nm) and d["n"]:
            oc = grid.outcome[rows, dirs]
            pl = grid.pnl_pips[rows, dirs]
            res = oc != 0
            hr = float((oc[res] == 1).mean()) if res.any() else float("nan")
            ex = float(np.nanmean(pl))
            d["pct_hit_vs_N1"] = L.percentile_of(hr, base[nm]["tgt"])
            d["pct_exp_vs_N1"] = L.percentile_of(ex, base[nm]["exp"])
            log(f"    vs N1: hit rate at pct {d['pct_hit_vs_N1']:.1f}; "
                f"expectancy at pct {d['pct_exp_vs_N1']:.1f}")
            if d["n"] < 30:
                log("    >>> SAMPLE INSUFFICIENT FOR INFERENCE — descriptive only. "
                    "No rate above may be quoted without this label.")
        out[nm] = d

    # ------------- SECOND ARM: the course's own natural low-side comparator ----------
    log("\n[SECOND BASELINE — S1 as the natural low-side comparator for S2 "
        "(`PT-015` §4)]")
    if out["S1"]["n"] and out["S2"]["n"]:
        p1 = grid.pnl_pips[out["S1"]["rows"], out["S1"]["dirs"]]
        p2 = grid.pnl_pips[out["S2"]["rows"], out["S2"]["dirs"]]
        obs, pv, _ = L.perm_diff(p2, p1, stat=np.mean)
        log(f"  mean expectancy S2 - S1 = {obs:+.2f} pips; label-shuffle permutation "
            f"two-sided p = {pv:.3f} (1,000 shuffles, seed {L.SEED})")
        o1 = grid.outcome[out["S1"]["rows"], out["S1"]["dirs"]]
        o2 = grid.outcome[out["S2"]["rows"], out["S2"]["dirs"]]
        log(f"  hit rate S1 {L.fmt_rate(int((o1==1).sum()), int((o1!=0).sum()))}")
        log(f"  hit rate S2 {L.fmt_rate(int((o2==1).sum()), int((o2!=0).sum()))}")

    # ------------- THIRD ARM: volatility-matched pairing S2 vs S3 -------------------
    log("\n[THIRD BASELINE — volatility-matched S2 vs S3 pairing (`PT-015` §4). "
        "'The third arm decides the test.']")
    ptr = prior_true_range(days)
    m2, m3 = out["S2"], out["S3"]
    match = None
    if m2["n"] and m3["n"]:
        v2 = ptr[m2["keep"]]
        v3 = ptr[m3["keep"]]
        used, pairs = set(), []
        for j, tv in enumerate(v3):
            if not np.isfinite(tv):
                continue
            cand = [(abs(v2[i] - tv), i) for i in range(len(v2))
                    if i not in used and np.isfinite(v2[i])]
            if not cand:
                continue
            cand.sort()
            d0, i = cand[0]
            used.add(i)
            pairs.append((j, i, d0))
        if pairs:
            jj = np.array([p[0] for p in pairs]); ii = np.array([p[1] for p in pairs])
            p3 = grid.pnl_pips[m3["rows"][jj], m3["dirs"][jj]]
            p2m = grid.pnl_pips[m2["rows"][ii], m2["dirs"][ii]]
            log(f"  matched pairs: {len(pairs)}   "
                f"median |prior-TR difference| = "
                f"{np.median([p[2] for p in pairs]):.1f} pips")
            log(f"  prior TR: S3 median {np.nanmedian(v3):.1f}, "
                f"matched S2 median {np.nanmedian(v2[ii]):.1f}, "
                f"unmatched S2 median {np.nanmedian(v2):.1f} pips")
            log(f"  paired mean expectancy  S3 {np.nanmean(p3):+.2f}  "
                f"S2 {np.nanmean(p2m):+.2f}  diff {np.nanmean(p3-p2m):+.2f} pips")
            obs, pv, _ = L.perm_diff(p3, p2m, stat=np.mean)
            log(f"  permutation two-sided p = {pv:.3f}")
            log(f"  >>> {L.nlabel(len(pairs))}")
            match = dict(n_pairs=len(pairs), s3_exp=float(np.nanmean(p3)),
                         s2_exp=float(np.nanmean(p2m)), p=pv)
        else:
            log("  no matched pairs could be formed")
    else:
        log(f"  NOT PERFORMED — S2 n = {m2['n']}, S3 n = {m3['n']}. "
            "A pairing needs both arms populated.")

    # unconditional volatility context
    log("\n[context — prior true range by stratum, pips]")
    for nm, _, _, _lab in STRATA:
        k = out[nm]["keep"]
        if len(k):
            log(f"  {nm}: median prior TR {np.nanmedian(ptr[k]):.1f}   "
                f"median box range {np.median(days['box_range_pips'].values[k]):.1f}")

    clean = {}
    for nm, d in out.items():
        clean[nm] = {k: v for k, v in d.items() if k not in ("rows", "dirs", "keep")}
    return dict(arm=arm, n_days=int(len(days)), strata=clean,
                n1={nm: (None if base[nm] is None else dict(
                    hit=L.dist_line(base[nm]["tgt"]),
                    exp=L.dist_line(base[nm]["exp"]),
                    hit_rand=L.dist_line(base[nm]["tgt_r"]),
                    exp_rand=L.dist_line(base[nm]["exp_r"])))
                    for nm, _, _, _lab in STRATA},
                matched=match)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    lines = []

    def log(s=""):
        print(s)
        lines.append(s)

    log(L.header("PT-015", "Does a 50-pip ceiling exist? Excursion strata (W-B)",
                 "window   : W-B 2014-01-05 -> 2015-12-31 (wholly inside DEVELOPMENT)"))
    log("PRE-REG  : PRE_REGISTERED/PT-015_does_the_fifty_pip_ceiling_exist.md")
    log("STRATA   : S1 10-24 | S2 25-50 | S3 51-100 | S4 >100  — the instructor's own")
    log("           numbers (V02 [00:44:59], V04 [00:15:43]). MERGING IS FORBIDDEN.")
    log("BASELINE : N1 matched random entry per stratum + random-direction secondary;")
    log("           S1 as the natural low-side comparator; volatility-matched S2/S3.")
    log("DEPENDS  : PT-014 / BT_V04_0001 forecast S3 thin and S4 empty BEFORE this ran.")

    res = {}
    for arm in ("A", "B"):
        res[arm] = run_arm(arm, log)

    log("\n" + "=" * 78)
    log("BOTH ARMS SIDE BY SIDE — `D-031` requires both, always")
    log("=" * 78)
    log(f"{'stratum':<10}{'n (A)':>8}{'hit (A)':>10}{'exp (A)':>10}"
        f"{'n (B)':>8}{'hit (B)':>10}{'exp (B)':>10}")
    for nm, _, _, _lab in STRATA:
        a, b = res["A"]["strata"][nm], res["B"]["strata"][nm]
        def f(d, k, fmt):
            v = d.get(k)
            return "n/a" if v is None or (isinstance(v, float) and not np.isfinite(v)) \
                else fmt.format(v)
        log(f"{nm:<10}{a['n']:>8}{f(a,'hit_rate','{:.3f}'):>10}"
            f"{f(a,'expectancy','{:+.2f}'):>10}"
            f"{b['n']:>8}{f(b,'hit_rate','{:.3f}'):>10}"
            f"{f(b,'expectancy','{:+.2f}'):>10}")

    with open(os.path.join(OUT_DIR, "pt015_results.json"), "w") as fh:
        json.dump(res, fh, indent=1, default=str)
    with open(os.path.join(OUT_DIR, "pt015_report.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print("\nwritten:", os.path.join(OUT_DIR, "pt015_results.json"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
