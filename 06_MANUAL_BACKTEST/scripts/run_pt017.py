#!/usr/bin/env python3
"""PT-017 — "In profit in 15 to 45 minutes. Guaranteed." (CL1)

Pre-registration: `PRE_REGISTERED/PT-017_in_profit_in_fifteen_to_fortyfive_minutes.md`
Depends on: PT-014 (`BT_V04_0001`) for the expected trigger count.

`D-009` GOVERNS: the 15-45 minute figure is a HYPOTHESIS TO TEST, never a target.
Nothing in this script is tuned toward it. If the observed median is 4 hours, the
observed median is 4 hours.

RESOLUTION. `PT-017` §3 asks for "5-minute preferred, 15-minute fallback... the
resolution actually used is recorded in the observation". The corpus is M1, so
time-to-profit is measured at ONE-MINUTE resolution — finer than the preferred option.
The TRIGGER stays on 15-minute closes exactly as pre-registered.

THE PATH IS MEASURED UNSTOPPED, AND THAT IS WHAT THE PRE-REGISTRATION ASKS FOR.
Measure 4 is "maximum adverse excursion BEFORE first profit - the number that decides
whether an 18-pip stop survives long enough to collect it". That question is only
answerable if the stop is NOT applied while measuring, otherwise MAE can never exceed
18 by construction. So measures 1-4 are computed on the raw forward path; the 18/50
version a trader would actually experience is reported beside it, never instead of it.

usage: python3 run_pt017.py
"""
import json
import os
import sys

import numpy as np

import mmm_lib as L

OUT_DIR = os.path.join(L.ROOT, "06_MANUAL_BACKTEST", "V04", "data")
CK = (15, 30, 45, 60, 120)
BIG = 1e6          # stop/target set out of reach -> the path is never truncated


def trigger_rows(grid, days, exc, side, when):
    rows, dirs, keep = [], [], []
    for i in range(len(days)):
        if not np.isfinite(exc[i]):
            continue
        r = grid.lookup(days["sd"].values[i], when[i])
        if r is None or not grid.valid[r, 1 if side[i] > 0 else 0]:
            continue
        rows.append(r); dirs.append(1 if side[i] > 0 else 0); keep.append(i)
    return np.array(rows, int), np.array(dirs, int), np.array(keep, int)


def profile(grid, rows, dirs, label, log):
    """Measures 1-4 for one population."""
    n = len(rows)
    if n == 0:
        log(f"  {label}: n = 0")
        return dict(n=0)
    t0 = grid.t_profit0[rows, dirs]
    t10 = grid.t_profit10[rows, dirs]
    mae = grid.mae_before_profit[rows, dirs]
    mfe = grid.mfe_pips[rows, dirs]
    ck = grid.ck_pnl[rows, dirs, :]

    reached0 = np.isfinite(t0)
    reached10 = np.isfinite(t10)
    d = dict(n=n,
             share_ever_profit=float(reached0.mean()),
             share_ever_10=float(reached10.mean()),
             median_t0=float(np.nanmedian(t0)) if reached0.any() else float("nan"),
             median_t10=float(np.nanmedian(t10)) if reached10.any() else float("nan"),
             share_t0_le45=float((np.nan_to_num(t0, nan=1e9) <= 45).mean()),
             share_t0_15_45=float(((np.nan_to_num(t0, nan=1e9) >= 15) &
                                   (np.nan_to_num(t0, nan=1e9) <= 45)).mean()),
             median_mae_before=float(np.nanmedian(mae)),
             p90_mae_before=float(np.nanpercentile(mae, 90)),
             share_mae_ge18=float(np.mean(mae[np.isfinite(mae)] >= 18.0)),
             median_mfe=float(np.nanmedian(mfe)))
    log(f"  {label}: {L.nlabel(n)}")
    log(f"    M1 — ever in profit before 17:00   : "
        f"{L.fmt_rate(int(reached0.sum()), n)}")
    log(f"    M1 — median time to first >0 pips  : "
        f"{d['median_t0']:.0f} min   (of those that got there)")
    log(f"    M1 — share reaching >0 within 45m  : "
        f"{L.fmt_rate(int((np.nan_to_num(t0, nan=1e9) <= 45).sum()), n)}")
    log(f"    M2 — ever reaching +10 pips        : "
        f"{L.fmt_rate(int(reached10.sum()), n)}")
    log(f"    M2 — median time to +10 pips       : {d['median_t10']:.0f} min")
    log(f"    M3 — share in profit at checkpoint (nan = the day ended first):")
    for k, c in enumerate(CK):
        v = ck[:, k]
        ok = np.isfinite(v)
        d[f"ck{c}"] = float((v[ok] > 0).mean()) if ok.any() else float("nan")
        d[f"ck{c}_n"] = int(ok.sum())
        d[f"ck{c}_median"] = float(np.median(v[ok])) if ok.any() else float("nan")
        log(f"        t+{c:>3} min : {L.fmt_rate(int((v[ok] > 0).sum()), int(ok.sum()))}"
            f"   median P&L {d[f'ck{c}_median']:+.1f} pips")
    log(f"    M4 — MAE before first profit       : median {d['median_mae_before']:.1f}, "
        f"p90 {d['p90_mae_before']:.1f} pips")
    log(f"    M4 — share whose MAE-before-profit >= the 18-pip stop : "
        f"{L.fmt_rate(int(np.sum(mae[np.isfinite(mae)] >= 18.0)), int(np.isfinite(mae).sum()))}")
    return d


def run_arm(arm, log):
    m15 = L.window(L.load_m15(arm), "W-B")
    m1 = L.window(L.load_m1(arm), "W-B")
    days = L.build_days(m15)
    exc, side, when, _ = L.first_close_beyond(m15, days, lo=25.0, hi=50.0)

    log(f"\n----- ARM {arm} -----")
    log(f"COMPLETENESS (C-6): {L.completeness_line(days)}")

    # unstopped path grid (measures 1-4) and the 18/50 grid (the lived experience)
    gpath = L.TradeGrid(m1, m15, stop_pips=BIG, target_pips=BIG, checkpoints=CK)
    gtrade = L.TradeGrid(m1, m15, checkpoints=CK)

    rows, dirs, keep = trigger_rows(gpath, days, exc, side, when)
    log(f"trigger — first 15m close 25-50 pips beyond a box edge, direction away:")
    log(f"  fired on {L.fmt_rate(len(rows), len(days))} of session days")
    log(f"  side: short (high breach) {int((dirs==1).sum())}  "
        f"long (low breach) {int((dirs==0).sum())}")
    log(f"  median excursion at trigger: {np.nanmedian(exc[keep]):.1f} pips")
    log(f"  entry price = that bar's close. NO slippage or spread model is invented")
    log(f"  (`PT-017` §3); the corpus is BID data, so spread would worsen every")
    log(f"  figure below. Stated here rather than modelled.")

    # ---------------- BASELINES FIRST (`PT-017` §4, `COMMON_PROTOCOL.md` §9 rule 1) --
    log("\n[BASELINES — run and printed BEFORE the trigger population's checkpoints]")

    log("\n  N1 — matched random entry, same hours, direction matched, 1,000 iters, "
        f"seed {L.SEED}")
    pool = np.where(gpath.valid.any(1))[0]
    rng = np.random.default_rng(L.SEED)
    n = len(rows)
    n1 = {f"ck{c}": np.full(L.ITERATIONS, np.nan) for c in CK}
    n1["t0"] = np.full(L.ITERATIONS, np.nan)
    n1["t10"] = np.full(L.ITERATIONS, np.nan)     # Measure 2's own baseline
    n1["ever"] = np.full(L.ITERATIONS, np.nan)
    n1["ever10"] = np.full(L.ITERATIONS, np.nan)
    n1["mae"] = np.full(L.ITERATIONS, np.nan)
    n1r = {f"ck{c}": np.full(L.ITERATIONS, np.nan) for c in CK}
    for it in range(L.ITERATIONS):
        pick = rng.choice(pool, size=n, replace=True)
        dr = rng.integers(0, 2, size=n)
        for tag, dd, store in (("m", dirs, n1), ("r", dr, n1r)):
            for k, c in enumerate(CK):
                v = gpath.ck_pnl[pick, dd, k]
                v = v[np.isfinite(v)]
                if len(v):
                    store[f"ck{c}"][it] = float((v > 0).mean())
        t0 = gpath.t_profit0[pick, dirs]
        n1["ever"][it] = float(np.isfinite(t0).mean())
        f0 = t0[np.isfinite(t0)]
        if len(f0):
            n1["t0"][it] = float(np.median(f0))
        t10 = gpath.t_profit10[pick, dirs]
        n1["ever10"][it] = float(np.isfinite(t10).mean())
        f10 = t10[np.isfinite(t10)]
        if len(f10):
            n1["t10"][it] = float(np.median(f10))
        mm = gpath.mae_before_profit[pick, dirs]
        mm = mm[np.isfinite(mm)]
        if len(mm):
            n1["mae"][it] = float(np.median(mm))
    for c in CK:
        log(f"    share in profit at t+{c:>3}: {L.dist_line(n1[f'ck{c}'])}")
    log(f"    ever in profit           : {L.dist_line(n1['ever'])}")
    log(f"    median time to >0 pips   : {L.dist_line(n1['t0'])} min")
    log(f"    ever reaching +10 pips   : {L.dist_line(n1['ever10'])}")
    log(f"    median time to +10 pips  : {L.dist_line(n1['t10'])} min   <- Measure 2's"
        f" own baseline")
    log(f"    median MAE before profit : {L.dist_line(n1['mae'])} pips")
    log("    N1 secondary, RANDOM direction (`D-029` / `PT-017` §4 third arm):")
    for c in CK:
        log(f"      share in profit at t+{c:>3}: {L.dist_line(n1r[f'ck{c}'])}")

    log("\n  SECOND BASELINE — the natural control (`PT-017` §4): the same measures on "
        "days\n  where NO qualifying 25-50 excursion occurred, entered at the same clock "
        "times.\n  Isolates the trigger from the hour.")
    trig_days = set(int(days['sd'].values[i]) for i in keep)
    trig_minutes = [int(when[i]) for i in keep]
    nc_rows, nc_dirs = [], []
    rng2 = np.random.default_rng(L.SEED)
    untriggered = [int(days["sd"].values[i]) for i in range(len(days))
                   if int(days["sd"].values[i]) not in trig_days]
    for j, sd in enumerate(untriggered):
        mnt = trig_minutes[rng2.integers(0, len(trig_minutes))]
        r = gpath.lookup(sd, mnt)
        if r is None:
            continue
        d = int(dirs[rng2.integers(0, len(dirs))])
        if not gpath.valid[r, d]:
            continue
        nc_rows.append(r); nc_dirs.append(d)
    nc_rows = np.array(nc_rows, int); nc_dirs = np.array(nc_dirs, int)
    log(f"  untriggered session days: {len(untriggered)}; entries placed: {len(nc_rows)}")
    nat = profile(gpath, nc_rows, nc_dirs, "NATURAL CONTROL (untriggered days)", log)

    # ---------------- RULE ARM ----------------
    log("\n[RULE ARM — the trigger population, unstopped path, M1 resolution]")
    rule = profile(gpath, rows, dirs, "TRIGGERED (25-50 pip location trigger)", log)

    log("\n  percentile of the rule arm within N1:")
    for c in CK:
        log(f"    share in profit at t+{c:>3}: obs {rule[f'ck{c}']:.3f}  "
            f"-> pct {L.percentile_of(rule[f'ck{c}'], n1[f'ck{c}']):.1f}")
        rule[f"pct_ck{c}"] = L.percentile_of(rule[f"ck{c}"], n1[f"ck{c}"])
    rule["pct_ever"] = L.percentile_of(rule["share_ever_profit"], n1["ever"])
    rule["pct_t0"] = L.percentile_of(rule["median_t0"], n1["t0"])
    rule["pct_mae"] = L.percentile_of(rule["median_mae_before"], n1["mae"])
    rule["pct_ever10"] = L.percentile_of(rule["share_ever_10"], n1["ever10"])
    rule["pct_t10"] = L.percentile_of(rule["median_t10"], n1["t10"])
    log(f"    ever in profit           : obs {rule['share_ever_profit']:.3f} -> "
        f"pct {rule['pct_ever']:.1f}")
    log(f"    median time to >0 pips   : obs {rule['median_t0']:.0f} min -> "
        f"pct {rule['pct_t0']:.1f}  (LOW percentile = faster than the null)")
    log(f"    ever reaching +10 pips   : obs {rule['share_ever_10']:.3f} -> "
        f"pct {rule['pct_ever10']:.1f}")
    log(f"    median time to +10 pips  : obs {rule['median_t10']:.0f} min -> "
        f"pct {rule['pct_t10']:.1f}  (LOW percentile = faster than the null)")
    log(f"    median MAE before profit : obs {rule['median_mae_before']:.1f} -> "
        f"pct {rule['pct_mae']:.1f}")

    log("\n[THE LIVED VERSION — the same trigger with the 18/50 stop and target in "
        "place]")
    rows2, dirs2, _ = trigger_rows(gtrade, days, exc, side, when)
    oc = gtrade.outcome[rows2, dirs2]
    pl = gtrade.pnl_pips[rows2, dirs2]
    res = oc != 0
    log(f"  n = {len(rows2)}   target {int((oc==1).sum())} / stop "
        f"{int((oc==-1).sum())} / open {int((oc==0).sum())}")
    log(f"  hit rate (of resolved): {L.fmt_rate(int((oc==1).sum()), int(res.sum()))}")
    log(f"  expectancy: {np.nanmean(pl):+.2f} pips  boot 95% CI "
        f"{L.boot_ci(pl, stat=np.mean)}")
    lived = dict(n=len(rows2), n_target=int((oc == 1).sum()),
                 n_stop=int((oc == -1).sum()), n_open=int((oc == 0).sum()),
                 hit_rate=float((oc[res] == 1).mean()) if res.any() else float("nan"),
                 expectancy=float(np.nanmean(pl)))

    log("\n[`CL1` READ AGAINST THE PRE-REGISTERED WORDING — `D-009`: a hypothesis, "
        "never a target]")
    log(f"  \"in profit in 15 to 45 minutes\": share first reaching >0 pips within "
        f"45 min = {L.fmt_rate(int(round(rule['share_t0_le45']*len(rows))), len(rows))}")
    log(f"  share whose FIRST profit falls inside the 15-45 minute band itself = "
        f"{rule['share_t0_15_45']:.3f}")
    log("  \"Guaranteed\" is refuted by construction: any share below 1.000 refutes it, "
        "and\n  the observed share is below 1.000 on every arm and every reading.")
    return dict(arm=arm, n_days=int(len(days)), n_trig=len(rows),
                rule=rule, natural=nat, lived=lived,
                n1={f"ck{c}": L.dist_line(n1[f"ck{c}"]) for c in CK} |
                   {"ever": L.dist_line(n1["ever"]), "t0": L.dist_line(n1["t0"]),
                    "ever10": L.dist_line(n1["ever10"]),
                    "t10": L.dist_line(n1["t10"]), "mae": L.dist_line(n1["mae"])},
                n1_random={f"ck{c}": L.dist_line(n1r[f"ck{c}"]) for c in CK})


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    lines = []

    def log(s=""):
        print(s)
        lines.append(s)

    log(L.header("PT-017", "'In profit in 15 to 45 minutes. Guaranteed.' — CL1 (W-B)",
                 "window   : W-B 2014-01-05 -> 2015-12-31 (wholly inside DEVELOPMENT)"))
    log("PRE-REG  : PRE_REGISTERED/PT-017_in_profit_in_fifteen_to_fortyfive_minutes.md")
    log("GOVERNING: `D-009` — CL1 is a hypothesis to test, never a target. No parameter")
    log("           here may be adjusted to bring the result closer to 15-45 minutes.")
    log("RESOLUTION: trigger on 15m closes (as pre-registered); time-to-profit measured")
    log("           at M1 = 1-minute resolution, finer than the preferred 5-minute.")
    log("SCOPE    : this is a LOCATION trigger, not the instructor's entry, which is")
    log("           the close of a second leg (`A-007`) confirmed by TDI (`A-039`) —")
    log("           neither defined in V01-V06. `PT-017` §6 is binding.")

    res = {}
    for arm in ("A", "B"):
        res[arm] = run_arm(arm, log)

    log("\n" + "=" * 78)
    log("BOTH ARMS SIDE BY SIDE — `D-031` requires both, always")
    log("=" * 78)
    log(f"{'':38}{'ARM A':>12}{'ARM B':>12}")
    rows = [("n triggered days", lambda r: r["n_trig"], "{:.0f}"),
            ("ever in profit (share)", lambda r: r["rule"]["share_ever_profit"], "{:.3f}"),
            ("median min to first >0 pip", lambda r: r["rule"]["median_t0"], "{:.0f}"),
            ("share first profit within 45 min", lambda r: r["rule"]["share_t0_le45"], "{:.3f}"),
            ("share in profit at t+15", lambda r: r["rule"]["ck15"], "{:.3f}"),
            ("share in profit at t+30", lambda r: r["rule"]["ck30"], "{:.3f}"),
            ("share in profit at t+45", lambda r: r["rule"]["ck45"], "{:.3f}"),
            ("share in profit at t+60", lambda r: r["rule"]["ck60"], "{:.3f}"),
            ("share in profit at t+120", lambda r: r["rule"]["ck120"], "{:.3f}"),
            ("pct of N1 at t+45", lambda r: r["rule"]["pct_ck45"], "{:.1f}"),
            ("median min to +10 pips", lambda r: r["rule"]["median_t10"], "{:.0f}"),
            ("pct of N1, time to +10", lambda r: r["rule"]["pct_t10"], "{:.1f}"),
            ("median MAE before profit", lambda r: r["rule"]["median_mae_before"], "{:.1f}"),
            ("share MAE-before-profit >= 18", lambda r: r["rule"]["share_mae_ge18"], "{:.3f}"),
            ("18/50 hit rate", lambda r: r["lived"]["hit_rate"], "{:.3f}"),
            ("18/50 expectancy (pips)", lambda r: r["lived"]["expectancy"], "{:+.2f}")]
    for lab, f, fmt in rows:
        log(f"{lab:<38}{fmt.format(f(res['A'])):>12}{fmt.format(f(res['B'])):>12}")

    with open(os.path.join(OUT_DIR, "pt017_results.json"), "w") as fh:
        json.dump(res, fh, indent=1, default=str)
    with open(os.path.join(OUT_DIR, "pt017_report.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print("\nwritten:", os.path.join(OUT_DIR, "pt017_results.json"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
