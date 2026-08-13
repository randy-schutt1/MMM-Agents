#!/usr/bin/env python3
"""PT-020 — The London-open conditional: cut the high, sell; extend the low, stand aside.

Pre-registration: `PRE_REGISTERED/PT-020_london_open_asymmetric_conditional.md`
Depends on: PT-014 (`BT_V04_0001`).

THE VARIANCE CLAIM IS THE POINT AND IS REPORTED FIRST (`PT-020` §3). The instructor's
stated reason is epistemic - "I don't know if it's a straightaway or if it's a stop
hunt. So I don't take it." That is a claim about outcome DISPERSION, not direction:
the low-side branch should show HIGHER dispersion, not merely worse returns.

`PT-020` §3b: this test uses the BROAD reading of the conditional, applied to every day
regardless of weekly bias, because the narrow reading needs the anchor point (`A-001`),
which is undefined. The result is evidence about the broad reading ONLY.

`PT-020` §3a: `C-004` (3:30 printed vs 4 o'clock spoken) is OPEN and this test does not
close it. The trigger window 03:30-04:30 spans both readings and the sub-window split
reports them separately.

usage: python3 run_pt020.py
"""
import json
import os
import sys

import numpy as np

import mmm_lib as L

OUT_DIR = os.path.join(L.ROOT, "06_MANUAL_BACKTEST", "V03", "data")
TRIG_FROM, TRIG_TO = 3 * 60 + 30, 4 * 60 + 30      # 03:30 - 04:30
SUB = ((3 * 60 + 30, 4 * 60, "03:30-04:00"), (4 * 60, 4 * 60 + 30, "04:00-04:30"))
BRANCH_N_ENTRY = 4 * 60 + 30                        # 04:30, per `PT-020` §4


def branches(m15, days):
    """Assign each session day to branch H, L or N from the trigger window only.

    DECLARED READING, because `PT-020` §3 does not state it: a 15m bar is "inside the
    trigger window" if its STAMP lies in [03:30, 04:30) - stamps 03:30, 03:45, 04:00,
    04:15, whose closes fall at 03:45 ... 04:30.

    DECLARED READING, because `PT-020` §3 lists three branches as though disjoint but a
    day can breach both edges inside one hour: the day is assigned by whichever edge is
    breached FIRST. Days breaching both are counted and reported separately, and the
    assignment uses only information available at the decision point.
    """
    sd, mod = m15.sd, m15.mod
    inwin = (mod >= TRIG_FROM) & (mod < TRIG_TO)
    rows_by_day = {}
    for i in np.where(inwin)[0]:
        rows_by_day.setdefault(int(sd[i]), []).append(i)
    br = np.array(["N"] * len(days), dtype=object)
    when = np.full(len(days), np.nan)
    both = np.zeros(len(days), dtype=bool)
    for i, row in enumerate(days.itertuples()):
        rows = np.asarray(sorted(rows_by_day.get(int(row.sd), [])))
        if len(rows) == 0:
            continue
        C = m15.c[rows]
        up = np.where(C > row.box_hi)[0]
        dn = np.where(C < row.box_lo)[0]
        both[i] = len(up) > 0 and len(dn) > 0
        if len(up) == 0 and len(dn) == 0:
            continue
        fu = up[0] if len(up) else 10 ** 9
        fd = dn[0] if len(dn) else 10 ** 9
        j = min(fu, fd)
        br[i] = "H" if fu < fd else "L"
        when[i] = int(mod[rows[j]])
    return br, when, both


def rows_for(grid, days, mask, when, direction):
    """`direction`: 1 = short, 0 = long. Branch H and branch L both take the SAME SHORT
    (`PT-020` §3) - branch L's is a measurement of what standing aside avoids, not a
    recommendation. The mirror (long after a low breach) is the third baseline."""
    rows, dirs, keep = [], [], []
    for i in np.where(mask)[0]:
        if not np.isfinite(when[i]):
            continue
        r = grid.lookup(days["sd"].values[i], when[i])
        if r is None or not grid.valid[r, direction]:
            continue
        rows.append(r); dirs.append(direction); keep.append(i)
    return np.array(rows, int), np.array(dirs, int), np.array(keep, int)


def describe(grid, rows, dirs, label, log):
    if len(rows) == 0:
        log(f"  {label}: n = 0")
        return dict(n=0)
    oc = grid.outcome[rows, dirs]
    pl = grid.pnl_pips[rows, dirs]
    rr = oc != 0
    d = dict(n=len(rows), n_target=int((oc == 1).sum()), n_stop=int((oc == -1).sum()),
             n_open=int((oc == 0).sum()), n_resolved=int(rr.sum()),
             hit_rate=float((oc[rr] == 1).mean()) if rr.any() else float("nan"),
             expectancy=float(np.nanmean(pl)),
             sd=float(np.nanstd(pl, ddof=1)),
             iqr=float(np.nanpercentile(pl, 75) - np.nanpercentile(pl, 25)),
             mad=float(np.nanmedian(np.abs(pl - np.nanmedian(pl)))))
    log(f"  {label}: {L.nlabel(len(rows))}")
    log(f"    >>> DISPERSION FIRST (`PT-020` §3, the variance claim):")
    log(f"        outcome SD {d['sd']:.2f}   IQR {d['iqr']:.2f}   MAD {d['mad']:.2f} pips")
    log(f"    target / stop / open : {d['n_target']} / {d['n_stop']} / {d['n_open']}")
    log(f"    hit rate (of resolved): {L.fmt_rate(d['n_target'], d['n_resolved'])}")
    log(f"    expectancy            : {d['expectancy']:+.2f} pips  boot 95% CI "
        f"{L.boot_ci(pl, stat=np.mean)}")
    return d


def run_arm(arm, log):
    m15 = L.window(L.load_m15(arm), "W-B")
    m1 = L.window(L.load_m1(arm), "W-B")
    days = L.build_days(m15)
    log(f"\n----- ARM {arm} -----")
    log(f"COMPLETENESS (C-6): {L.completeness_line(days)}")

    br, when, both = branches(m15, days)
    isH, isL, isN = br == "H", br == "L", br == "N"
    log("\n[BRANCH FREQUENCY — `PT-020` §7 step 4: report these WITH the outcome table]")
    log(f"  branch H (cuts the high)   : {L.fmt_rate(int(isH.sum()), len(days))}")
    log(f"  branch L (extends the low) : {L.fmt_rate(int(isL.sum()), len(days))}")
    log(f"  branch N (neither)         : {L.fmt_rate(int(isN.sum()), len(days))}")
    log(f"  days breaching BOTH edges inside 03:30-04:30 (assigned by whichever came "
        f"first): {int(both.sum())}")

    grid = L.TradeGrid(m1, m15)
    win_pool = np.where((grid.entry_mod >= TRIG_FROM) & (grid.entry_mod < TRIG_TO)
                        & grid.valid.any(1))[0]
    log(f"  N1 eligible pool = the same 03:30-04:30 window: {len(win_pool)} entry bars")

    # ---------------- BASELINES FIRST (`PT-020` §7 step 3) ----------------
    log("\n[BASELINES — run and printed BEFORE branch H's result is read]")
    n1 = {}
    for tag, mask in (("H", isH), ("L", isL)):
        r, d, k = rows_for(grid, days, mask, when, 1)
        if len(r) == 0:
            n1[tag] = None; continue
        tgt, expd = L.n1_outcome(grid, d, pool=win_pool)
        n1[tag] = dict(tgt=tgt, exp=expd)
        log(f"  N1 branch {tag} (n = {len(r)}, short, 1,000 iters, seed {L.SEED}, "
            f"drawn from 03:30-04:30):")
        log(f"      hit rate   {L.dist_line(tgt)}")
        log(f"      expectancy {L.dist_line(expd)} pips")
        # dispersion null: what outcome SD does matched random entry produce?
        rng = np.random.default_rng(L.SEED)
        sds = np.empty(L.ITERATIONS)
        for it in range(L.ITERATIONS):
            pick = rng.choice(win_pool, size=len(r), replace=True)
            v = grid.pnl_pips[pick, d]
            sds[it] = float(np.nanstd(v, ddof=1))
        n1[tag]["sd"] = sds
        log(f"      outcome SD {L.dist_line(sds)} pips   <- the dispersion null")

    log("\n  THIRD BASELINE — the direction-symmetry control (`PT-020` §4, "
        "'the sharpest arm'):")
    log("    the MIRROR rule — LONG after a low-side breach. If the mirror performs "
        "like\n    branch H, the asymmetry is in the instructor's framing rather than "
        "in GBP/USD.")
    rM, dM, kM = rows_for(grid, days, isL, when, 0)
    mirror = describe(grid, rM, dM, "MIRROR (long after a low breach)", log)

    log("\n  SECOND BASELINE — the natural control (`PT-020` §4): branch N days, "
        "entered\n    SHORT at 04:30. Isolates the breach from the hour.")
    rN, dN, kN = [], [], []
    for i in np.where(isN)[0]:
        r = grid.lookup(days["sd"].values[i], BRANCH_N_ENTRY)
        if r is None or not grid.valid[r, 1]:
            continue
        rN.append(r); dN.append(1); kN.append(i)
    natural = describe(grid, np.array(rN, int), np.array(dN, int),
                       "BRANCH N (short at 04:30)", log)

    # ---------------- RULE ARM ----------------
    log("\n[RULE ARM]")
    res = {}
    for tag, mask, lab in (("H", isH, "BRANCH H — 'cuts the high, you sell'"),
                           ("L", isL, "BRANCH L — 'extends the low, forget it' "
                                      "(same short, taken anyway, to price what "
                                      "standing aside avoids)")):
        r, d, k = rows_for(grid, days, mask, when, 1)
        dd = describe(grid, r, d, lab, log)
        if dd["n"] and n1.get(tag):
            dd["pct_hit"] = L.percentile_of(dd["hit_rate"], n1[tag]["tgt"])
            dd["pct_exp"] = L.percentile_of(dd["expectancy"], n1[tag]["exp"])
            dd["pct_sd"] = L.percentile_of(dd["sd"], n1[tag]["sd"])
            log(f"    vs N1: hit rate pct {dd['pct_hit']:.1f}; expectancy pct "
                f"{dd['pct_exp']:.1f}; OUTCOME SD pct {dd['pct_sd']:.1f}")
        dd["rows"], dd["dirs"], dd["keep"] = r, d, k
        res[tag] = dd

    log("\n[THE VARIANCE CLAIM, TESTED DIRECTLY — is branch L more dispersed than "
        "branch H?]")
    if res["H"]["n"] and res["L"]["n"]:
        plH = grid.pnl_pips[res["H"]["rows"], res["H"]["dirs"]]
        plL = grid.pnl_pips[res["L"]["rows"], res["L"]["dirs"]]
        log(f"  outcome SD  : H {res['H']['sd']:.2f}  vs  L {res['L']['sd']:.2f} pips  "
            f"(L - H = {res['L']['sd']-res['H']['sd']:+.2f})")
        log(f"  outcome IQR : H {res['H']['iqr']:.2f}  vs  L {res['L']['iqr']:.2f} pips")
        # A MEDIAN-based scale test degenerates here and that is worth recording:
        # the modal outcome IS the 18-pip stop, so the median outcome equals the
        # median of |deviation| for both branches and the test returns p = 1.000 by
        # construction. The mean absolute deviation and a direct SD-difference
        # permutation are used instead. Neither was chosen for its result: both were
        # run together and both are reported.
        o, p, _ = L.perm_diff(np.abs(plL - np.nanmedian(plL)),
                              np.abs(plH - np.nanmedian(plH)), stat=np.mean)
        log(f"  permutation on MEAN |deviation from own median| (scale test), L - H: "
            f"{o:+.2f} pips, two-sided p = {p:.3f}")
        osd, psd, _ = L.perm_diff(plL, plH, stat=lambda x, **kw: np.nanstd(x, ddof=1))
        log(f"  permutation on OUTCOME SD, L - H: {osd:+.2f} pips, "
            f"two-sided p = {psd:.3f}")
        oiq, piq, _ = L.perm_diff(
            plL, plH,
            stat=lambda x, **kw: np.nanpercentile(x, 75) - np.nanpercentile(x, 25))
        log(f"  permutation on OUTCOME IQR, L - H: {oiq:+.2f} pips, "
            f"two-sided p = {piq:.3f}")
        o2, p2, _ = L.perm_diff(plL, plH, stat=np.mean)
        log(f"  permutation on mean expectancy, L - H: {o2:+.2f} pips, "
            f"two-sided p = {p2:.3f}")
        res["variance"] = dict(sd_H=res["H"]["sd"], sd_L=res["L"]["sd"],
                               scale_diff=float(o), scale_p=float(p),
                               sd_diff=float(osd), sd_p=float(psd),
                               iqr_H=res["H"]["iqr"], iqr_L=res["L"]["iqr"],
                               iqr_diff=float(oiq), iqr_p=float(piq),
                               mean_diff=float(o2), mean_p=float(p2))

    log("\n[SUB-WINDOW SPLIT — the `C-004` split. Reported separately; resolves nothing]")
    sub = {}
    for lo, hi, lab in SUB:
        for tag, mask in (("H", isH), ("L", isL)):
            m = mask & np.isfinite(when) & (when >= lo) & (when < hi)
            r, d, k = rows_for(grid, days, m, when, 1)
            if len(r) == 0:
                log(f"  {lab} branch {tag}: n = 0")
                continue
            oc = grid.outcome[r, d]; pl = grid.pnl_pips[r, d]; rr = oc != 0
            hr = float((oc[rr] == 1).mean()) if rr.any() else float("nan")
            log(f"  {lab} branch {tag}: {L.nlabel(len(r))}  "
                f"hit {L.fmt_rate(int((oc==1).sum()), int(rr.sum()))}  "
                f"expectancy {np.nanmean(pl):+.2f}  SD {np.nanstd(pl, ddof=1):.2f}")
            sub[f"{lab}_{tag}"] = dict(n=len(r), hit=hr,
                                       exp=float(np.nanmean(pl)),
                                       sd=float(np.nanstd(pl, ddof=1)))

    clean = {t: {k: v for k, v in res[t].items() if k not in ("rows", "dirs", "keep")}
             for t in ("H", "L")}
    return dict(arm=arm, n_days=int(len(days)),
                n_H=int(isH.sum()), n_L=int(isL.sum()), n_N=int(isN.sum()),
                n_both=int(both.sum()), branches=clean, mirror=mirror,
                natural=natural, variance=res.get("variance"), sub=sub,
                n1={k: (None if v is None else dict(hit=L.dist_line(v["tgt"]),
                                                    exp=L.dist_line(v["exp"]),
                                                    sd=L.dist_line(v["sd"])))
                    for k, v in n1.items()})


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    lines = []

    def log(s=""):
        print(s)
        lines.append(s)

    log(L.header("PT-020", "The London-open asymmetric conditional (W-B)",
                 "window   : W-B 2014-01-05 -> 2015-12-31 (wholly inside DEVELOPMENT)"))
    log("PRE-REG  : PRE_REGISTERED/PT-020_london_open_asymmetric_conditional.md")
    log("CLAIM    : V03 [00:39:49]-[00:40:10] 'If the dealer cuts the high at the")
    log("           beginning of the London, you sell. If he extends the low at the")
    log("           beginning of the session, forget it. Why? ... I don't know if it's a")
    log("           straightaway or if it's a stop hunt. So I don't take it.'")
    log("SCOPE    : BROAD reading only (`PT-020` §3b). The narrow reading needs `A-001`")
    log("           (the anchor), which is undefined, so it is not testable today.")
    log("C-004    : OPEN. The 03:30-04:30 window spans both readings; the sub-window")
    log("           split reports them separately and resolves nothing.")

    res = {}
    for arm in ("A", "B"):
        res[arm] = run_arm(arm, log)

    log("\n" + "=" * 78)
    log("BOTH ARMS SIDE BY SIDE — `D-031` requires both, always")
    log("=" * 78)
    log(f"{'':40}{'ARM A':>12}{'ARM B':>12}")
    rows = [
        ("branch H n", lambda r: r["n_H"], "{:.0f}"),
        ("branch L n", lambda r: r["n_L"], "{:.0f}"),
        ("branch N n", lambda r: r["n_N"], "{:.0f}"),
        ("H outcome SD (the variance claim)", lambda r: r["branches"]["H"].get("sd", float('nan')), "{:.2f}"),
        ("L outcome SD", lambda r: r["branches"]["L"].get("sd", float('nan')), "{:.2f}"),
        ("H outcome IQR", lambda r: r["branches"]["H"].get("iqr", float('nan')), "{:.2f}"),
        ("L outcome IQR", lambda r: r["branches"]["L"].get("iqr", float('nan')), "{:.2f}"),
        ("  SD-difference p (L - H)", lambda r: (r["variance"] or {}).get("sd_p", float('nan')), "{:.3f}"),
        ("  IQR-difference p (L - H)", lambda r: (r["variance"] or {}).get("iqr_p", float('nan')), "{:.3f}"),
        ("H hit rate", lambda r: r["branches"]["H"].get("hit_rate", float('nan')), "{:.3f}"),
        ("L hit rate", lambda r: r["branches"]["L"].get("hit_rate", float('nan')), "{:.3f}"),
        ("H expectancy", lambda r: r["branches"]["H"].get("expectancy", float('nan')), "{:+.2f}"),
        ("L expectancy", lambda r: r["branches"]["L"].get("expectancy", float('nan')), "{:+.2f}"),
        ("H pct vs N1 (expectancy)", lambda r: r["branches"]["H"].get("pct_exp", float('nan')), "{:.1f}"),
        ("MIRROR (long after low) hit rate", lambda r: r["mirror"].get("hit_rate", float('nan')), "{:.3f}"),
        ("MIRROR expectancy", lambda r: r["mirror"].get("expectancy", float('nan')), "{:+.2f}"),
        ("branch N (short at 04:30) expectancy", lambda r: r["natural"].get("expectancy", float('nan')), "{:+.2f}"),
    ]
    for lab, f, fmt in rows:
        log(f"{lab:<40}{fmt.format(f(res['A'])):>12}{fmt.format(f(res['B'])):>12}")

    with open(os.path.join(OUT_DIR, "pt020_results.json"), "w") as fh:
        json.dump(res, fh, indent=1, default=str)
    with open(os.path.join(OUT_DIR, "pt020_report.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print("\nwritten:", os.path.join(OUT_DIR, "pt020_results.json"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
