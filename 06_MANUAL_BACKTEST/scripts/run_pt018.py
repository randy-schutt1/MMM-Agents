#!/usr/bin/env python3
"""PT-018 — The two-hour time stop: is "not in profit yet" predictive?

Pre-registration: `PRE_REGISTERED/PT-018_two_hour_time_stop.md`
Depends on: PT-014 (`BT_V04_0001`) and PT-017 (`BT_V04_0003`), whose time-to-profit
curve makes this test's classifier interpretable (`PT-018` §7 step 1).

MEASURE 3 IS NOT MODELLED, AND THAT IS PRE-REGISTERED, NOT AN OMISSION.
`PT-018` §3 Measure 3: the second-leg clock reset — "If you see a second leg, restart
the clock" V02 [00:34:51] — is NOT MODELLED because `A-007` is undefined across
V01-V06 and `D-030` forbids approximating it. The omission is recorded in every report
of this test. Its direction of bias is stated in `PT-018` §6: this measures a STRICTER
rule than the one taught, which favours finding the time stop WORSE than it is.

usage: python3 run_pt018.py
"""
import json
import os
import sys

import numpy as np

import mmm_lib as L

OUT_DIR = os.path.join(L.ROOT, "06_MANUAL_BACKTEST", "V02", "data")
CK = (60, 120, 180)          # T+1h, T+2h (the pre-registered classifier), T+3h
CUT = 25.0                   # `PT-018` §3: the LOWEST of the instructor's 25/30/40
SENSITIVITIES = (30.0, 40.0)  # the other two, pre-registered as sensitivities


def trigger_rows(grid, days, exc, side, when):
    rows, dirs = [], []
    for i in range(len(days)):
        if not np.isfinite(exc[i]):
            continue
        r = grid.lookup(days["sd"].values[i], when[i])
        if r is None:
            continue
        d = 1 if side[i] > 0 else 0
        if not grid.valid[r, d]:
            continue
        rows.append(r); dirs.append(d)
    return np.array(rows, int), np.array(dirs, int)


def classify(grid, rows, dirs, ck_index, cut):
    """Classify each trade at the checkpoint, exactly as `PT-018` §3 words it.

    Four mutually exclusive states, and the third and fourth exist because a trade can
    stop being classifiable before the checkpoint arrives:

      RESOLVED_EARLY  the 18/50 stop or target fired before the checkpoint, so there is
                      no open position for a time stop to act on
      PROGRESSED      still open at the checkpoint with unrealised P&L >= `cut`
      STALLED         still open at the checkpoint with unrealised P&L <  `cut`
      NO_HORIZON      the 17:00 session end arrived before the checkpoint did. These
                      cannot be classified at all and are counted separately rather
                      than being swept into STALLED, which would inflate it with days
                      that simply triggered late.
    """
    exit_min = grid.exit_min[rows, dirs]
    outcome = grid.outcome[rows, dirs]
    ck = grid.ck_pnl[rows, dirs, ck_index]
    resolved_early = np.isfinite(exit_min) & (exit_min <= CK[ck_index])
    has_ck = np.isfinite(ck)
    no_horizon = (~resolved_early) & (~has_ck)
    live = (~resolved_early) & has_ck
    progressed = live & (ck >= cut)
    stalled = live & (ck < cut)
    return dict(resolved_early=resolved_early, progressed=progressed,
                stalled=stalled, no_horizon=no_horizon, ck=ck,
                outcome=outcome, exit_min=exit_min)


def outcome_block(grid, rows, dirs, mask, label, log):
    n = int(mask.sum())
    if n == 0:
        log(f"    {label}: n = 0")
        return dict(n=0)
    oc = grid.outcome[rows, dirs][mask]
    pl = grid.pnl_pips[rows, dirs][mask]
    res = oc != 0
    d = dict(n=n, n_target=int((oc == 1).sum()), n_stop=int((oc == -1).sum()),
             n_open=int((oc == 0).sum()), n_resolved=int(res.sum()),
             hit_rate=float((oc[res] == 1).mean()) if res.any() else float("nan"),
             expectancy=float(np.nanmean(pl)))
    log(f"    {label}: {L.nlabel(n)}")
    log(f"      eventual target / stop / open at 17:00 : {d['n_target']} / "
        f"{d['n_stop']} / {d['n_open']}")
    log(f"      eventual hit rate (of resolved)        : "
        f"{L.fmt_rate(d['n_target'], d['n_resolved'])}")
    log(f"      expectancy if LET RUN                  : {d['expectancy']:+.2f} pips  "
        f"boot 95% CI {L.boot_ci(pl, stat=np.mean)}")
    return d


def run_arm(arm, log):
    m15 = L.window(L.load_m15(arm), "W-B")
    m1 = L.window(L.load_m1(arm), "W-B")
    days = L.build_days(m15)
    exc, side, when, _ = L.first_close_beyond(m15, days, lo=25.0, hi=50.0)

    log(f"\n----- ARM {arm} -----")
    log(f"COMPLETENESS (C-6): {L.completeness_line(days)}")

    grid = L.TradeGrid(m1, m15, checkpoints=CK)
    rows, dirs = trigger_rows(grid, days, exc, side, when)
    log(f"entry proxy — first 15m close 25-50 pips beyond a box edge, direction away, "
        f"stop 18 / target 50")
    log(f"  triggered on {L.fmt_rate(len(rows), len(days))} of session days")

    log("\n  >>> MEASURE 3 — the second-leg clock reset (V02 [00:34:51], "
        "'If you see a second leg,")
    log("      restart the clock') is NOT MODELLED. `A-007` is undefined across "
        "V01-V06 and")
    log("      `D-030` forbids approximating it. This therefore measures a STRICTER "
        "rule than")
    log("      the one taught, and the bias favours finding the time stop WORSE than "
        "it is.")

    # ------------- BASELINE FIRST: `PT-018` §7 step 3 is explicit that the N1
    # ------------- classification base rate is computed BEFORE the trigger population's
    log("\n[PRIMARY BASELINE — N1 matched random entry, classified identically at T+2h]")
    log("  `PT-018` §4: 'Establishes the base rate at which ANY position that is flat at")
    log("   2 hours goes on to lose. This is the comparison that decides whether the "
        "rule adds anything.'")
    pool = np.where(grid.valid.any(1))[0]
    rng = np.random.default_rng(L.SEED)
    n = len(rows)
    n1 = {k: np.full(L.ITERATIONS, np.nan) for k in
          ("share_stalled", "stalled_hit", "stalled_exp", "prog_hit", "prog_exp",
           "gain_of_timestop")}
    for it in range(L.ITERATIONS):
        pick = rng.choice(pool, size=n, replace=True)
        c = classify(grid, pick, dirs, 1, CUT)
        pl = grid.pnl_pips[pick, dirs]
        live_n = int(c["progressed"].sum() + c["stalled"].sum())
        if live_n:
            n1["share_stalled"][it] = float(c["stalled"].sum() / live_n)
        for tag, m in (("stalled", c["stalled"]), ("prog", c["progressed"])):
            if m.any():
                oc = c["outcome"][m]
                r = oc != 0
                if r.any():
                    n1[f"{tag}_hit"][it] = float((oc[r] == 1).mean())
                n1[f"{tag}_exp"][it] = float(np.nanmean(pl[m]))
        if c["stalled"].any():
            let_run = np.nanmean(pl[c["stalled"]])
            cut_now = np.nanmean(c["ck"][c["stalled"]])
            n1["gain_of_timestop"][it] = float(cut_now - let_run)
    log(f"    share of live positions STALLED at T+2h : "
        f"{L.dist_line(n1['share_stalled'])}")
    log(f"    STALLED    eventual hit rate            : {L.dist_line(n1['stalled_hit'])}")
    log(f"    STALLED    expectancy if let run        : {L.dist_line(n1['stalled_exp'])} pips")
    log(f"    PROGRESSED eventual hit rate            : {L.dist_line(n1['prog_hit'])}")
    log(f"    PROGRESSED expectancy if let run        : {L.dist_line(n1['prog_exp'])} pips")
    log(f"    VALUE OF THE TIME STOP under N1         : "
        f"{L.dist_line(n1['gain_of_timestop'])} pips per STALLED trade")

    # ------------- RULE ARM -------------
    log("\n[RULE ARM — the trigger population classified at T+2h, cut = +25 pips]")
    c = classify(grid, rows, dirs, 1, CUT)
    log(f"  RESOLVED before T+2h (stop or target already fired): "
        f"{int(c['resolved_early'].sum())}")
    log(f"  NO HORIZON (17:00 arrived before T+2h, unclassifiable): "
        f"{int(c['no_horizon'].sum())}")
    live_n = int(c["progressed"].sum() + c["stalled"].sum())
    log(f"  live and classifiable at T+2h: {live_n}")
    log(f"    PROGRESSED (>= +25 pips): {int(c['progressed'].sum())}")
    log(f"    STALLED    (<  +25 pips): {int(c['stalled'].sum())}")
    log(f"  share of live positions STALLED: "
        f"{L.fmt_rate(int(c['stalled'].sum()), live_n)}")

    log("\n  MEASURE 1 — eventual outcome by class:")
    prog = outcome_block(grid, rows, dirs, c["progressed"], "PROGRESSED", log)
    stal = outcome_block(grid, rows, dirs, c["stalled"], "STALLED", log)
    early = outcome_block(grid, rows, dirs, c["resolved_early"],
                          "RESOLVED before T+2h (not subject to the rule)", log)
    for tag, d, key in (("STALLED", stal, "stalled"), ("PROGRESSED", prog, "prog")):
        if d["n"]:
            d["pct_hit_vs_N1"] = L.percentile_of(d["hit_rate"], n1[f"{key}_hit"])
            d["pct_exp_vs_N1"] = L.percentile_of(d["expectancy"], n1[f"{key}_exp"])
            log(f"    {tag} vs N1: hit rate pct {d['pct_hit_vs_N1']:.1f}; "
                f"expectancy pct {d['pct_exp_vs_N1']:.1f}")
    if stal["n"] and prog["n"]:
        pl = grid.pnl_pips[rows, dirs]
        o, p, _ = L.perm_diff(pl[prog["n"] and c["progressed"]], pl[c["stalled"]],
                              stat=np.mean)
        log(f"    PROGRESSED - STALLED mean expectancy = {o:+.2f} pips; "
            f"permutation two-sided p = {p:.3f}")

    log("\n  MEASURE 2 — THE COUNTERFACTUAL, IN PIPS OF EXPECTANCY "
        "(`PT-018` §7 step 4: never a win-rate delta alone)")
    res = {}
    if stal["n"]:
        pl = grid.pnl_pips[rows, dirs]
        let_run = pl[c["stalled"]]
        cut_now = c["ck"][c["stalled"]]
        gain = float(np.nanmean(cut_now) - np.nanmean(let_run))
        log(f"    STALLED positions, n = {stal['n']}")
        log(f"      LET RUN to stop/target/17:00 : {np.nanmean(let_run):+.2f} pips "
            f"(boot 95% CI {L.boot_ci(let_run, stat=np.mean)})")
        log(f"      CLOSED at T+2h at the mark   : {np.nanmean(cut_now):+.2f} pips "
            f"(boot 95% CI {L.boot_ci(cut_now, stat=np.mean)})")
        log(f"      VALUE OF THE TIME STOP       : {gain:+.2f} pips per STALLED trade")
        pv = L.percentile_of(gain, n1["gain_of_timestop"])
        log(f"      percentile within N1         : {pv:.1f}")
        o, p, _ = L.perm_diff(cut_now, let_run, stat=np.mean)
        log(f"      paired permutation p         : {p:.3f}")
        # whole-population effect
        total_gain = gain * stal["n"] / len(rows)
        log(f"      spread over ALL {len(rows)} trades : {total_gain:+.3f} pips/trade")
        # win-rate framing, reported second and never alone
        wr_run = float(np.mean(let_run > 0))
        wr_cut = float(np.mean(cut_now > 0))
        log(f"      win rate, let run {wr_run:.3f} vs closed at T+2h {wr_cut:.3f} "
            f"(reported SECOND, never alone — `PT-018` §5)")
        res["counterfactual"] = dict(n=stal["n"], let_run=float(np.nanmean(let_run)),
                                     cut_now=float(np.nanmean(cut_now)), gain=gain,
                                     pct=pv, perm_p=p, per_all_trades=total_gain,
                                     wr_run=wr_run, wr_cut=wr_cut)

    log("\n  MEASURE 4 — the same classification at T+1h and T+3h, so '2 hours' is "
        "RANKED, not assumed")
    ranking = {}
    for k, hh in ((0, "T+1h"), (1, "T+2h"), (2, "T+3h")):
        cc = classify(grid, rows, dirs, k, CUT)
        ln = int(cc["progressed"].sum() + cc["stalled"].sum())
        if not cc["stalled"].any():
            log(f"    {hh}: no STALLED positions")
            continue
        pl = grid.pnl_pips[rows, dirs]
        lr = pl[cc["stalled"]]; cn = cc["ck"][cc["stalled"]]
        g = float(np.nanmean(cn) - np.nanmean(lr))
        oc = cc["outcome"][cc["stalled"]]; r = oc != 0
        hr = float((oc[r] == 1).mean()) if r.any() else float("nan")
        ocp = cc["outcome"][cc["progressed"]]; rp = ocp != 0
        hrp = float((ocp[rp] == 1).mean()) if rp.any() else float("nan")
        log(f"    {hh}: live {ln}  STALLED {int(cc['stalled'].sum())} "
            f"(unclassifiable {int(cc['no_horizon'].sum())})  "
            f"STALLED hit {hr:.3f}  PROGRESSED hit {hrp:.3f}  "
            f"time-stop value {g:+.2f} pips/STALLED trade")
        ranking[hh] = dict(live=ln, stalled=int(cc["stalled"].sum()),
                           stalled_hit=hr, prog_hit=hrp, gain=g)

    log("\n  PRE-REGISTERED SENSITIVITIES — the instructor's other two thresholds "
        "(30 / 40 pips)")
    sens = {}
    for cut in SENSITIVITIES:
        cc = classify(grid, rows, dirs, 1, cut)
        if not cc["stalled"].any():
            continue
        pl = grid.pnl_pips[rows, dirs]
        lr = pl[cc["stalled"]]; cn = cc["ck"][cc["stalled"]]
        g = float(np.nanmean(cn) - np.nanmean(lr))
        oc = cc["outcome"][cc["stalled"]]; r = oc != 0
        log(f"    cut = +{cut:.0f} pips: STALLED {int(cc['stalled'].sum())}  "
            f"PROGRESSED {int(cc['progressed'].sum())}  "
            f"STALLED hit {L.fmt_rate(int((oc==1).sum()), int(r.sum()))}  "
            f"time-stop value {g:+.2f} pips")
        sens[f"cut{cut:.0f}"] = dict(stalled=int(cc["stalled"].sum()),
                                     progressed=int(cc["progressed"].sum()), gain=g)

    log("\n  THIRD BASELINE — expectancy PER HOUR OF EXPOSURE (`PT-018` §4). "
        "Positions are open\n  for different durations by construction, so per-trade "
        "expectancy is not comparable.")
    third = {}
    for tag, m in (("PROGRESSED", c["progressed"]), ("STALLED", c["stalled"]),
                   ("RESOLVED<2h", c["resolved_early"])):
        if not m.any():
            continue
        pl = grid.pnl_pips[rows, dirs][m]
        ex = grid.exit_min[rows, dirs][m]
        # unresolved positions ran to the 17:00 close; use their realised hold time
        hold = np.where(np.isfinite(ex), ex, np.nan)
        hrs = np.where(np.isfinite(hold), hold / 60.0, np.nan)
        ok = np.isfinite(hrs) & (hrs > 0) & np.isfinite(pl)
        if ok.any():
            log(f"    {tag}: median hold {np.nanmedian(hold[ok]):.0f} min; "
                f"expectancy per hour of exposure "
                f"{float(np.nanmean(pl[ok] / hrs[ok])):+.2f} pips/h "
                f"(resolved trades only, n = {int(ok.sum())})")
            third[tag] = float(np.nanmean(pl[ok] / hrs[ok]))

    return dict(arm=arm, n_days=int(len(days)), n_trig=len(rows),
                resolved_early=int(c["resolved_early"].sum()),
                no_horizon=int(c["no_horizon"].sum()),
                live=live_n, progressed=prog, stalled=stal, early=early,
                ranking=ranking, sensitivities=sens, per_hour=third,
                n1={k: L.dist_line(v) for k, v in n1.items()}, **res)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    lines = []

    def log(s=""):
        print(s)
        lines.append(s)

    log(L.header("PT-018", "The two-hour time stop — is 'not in profit yet' predictive? (W-B)",
                 "window   : W-B 2014-01-05 -> 2015-12-31 (wholly inside DEVELOPMENT)"))
    log("PRE-REG  : PRE_REGISTERED/PT-018_two_hour_time_stop.md")
    log("CLAIM    : slide [00:33:10] 'If Trade Does Not See Substantial Profit In 2 Hours,")
    log("           Take Profit Or Small Loss'; audio [00:34:23] 'The time clock is not")
    log("           negotiable... 25, 30, 40 pips - then out. Scratch out.'")
    log("CLASSIFIER: PROGRESSED if unrealised P&L >= +25 pips at T+2h, else STALLED.")
    log("           +25 is the LOWEST of the instructor's three; 30 and 40 are run as")
    log("           PRE-REGISTERED sensitivities, not as alternatives to choose among.")
    log("SCOPE    : a MANAGEMENT rule on a PROXY entry. Measure 3 NOT MODELLED (`A-007`).")

    res = {}
    for arm in ("A", "B"):
        res[arm] = run_arm(arm, log)

    log("\n" + "=" * 78)
    log("BOTH ARMS SIDE BY SIDE — `D-031` requires both, always")
    log("=" * 78)
    log(f"{'':40}{'ARM A':>12}{'ARM B':>12}")
    rows = [
        ("triggered trades", lambda r: r["n_trig"], "{:.0f}"),
        ("resolved before T+2h", lambda r: r["resolved_early"], "{:.0f}"),
        ("unclassifiable (no 2h horizon)", lambda r: r["no_horizon"], "{:.0f}"),
        ("live at T+2h", lambda r: r["live"], "{:.0f}"),
        ("  PROGRESSED n", lambda r: r["progressed"]["n"], "{:.0f}"),
        ("  STALLED n", lambda r: r["stalled"]["n"], "{:.0f}"),
        ("PROGRESSED eventual hit rate", lambda r: r["progressed"].get("hit_rate", float('nan')), "{:.3f}"),
        ("STALLED eventual hit rate", lambda r: r["stalled"].get("hit_rate", float('nan')), "{:.3f}"),
        ("PROGRESSED expectancy, let run", lambda r: r["progressed"].get("expectancy", float('nan')), "{:+.2f}"),
        ("STALLED expectancy, let run", lambda r: r["stalled"].get("expectancy", float('nan')), "{:+.2f}"),
        ("STALLED closed at T+2h", lambda r: r.get("counterfactual", {}).get("cut_now", float('nan')), "{:+.2f}"),
        ("VALUE OF THE TIME STOP (pips)", lambda r: r.get("counterfactual", {}).get("gain", float('nan')), "{:+.2f}"),
        ("  percentile within N1", lambda r: r.get("counterfactual", {}).get("pct", float('nan')), "{:.1f}"),
        ("  permutation p", lambda r: r.get("counterfactual", {}).get("perm_p", float('nan')), "{:.3f}"),
        ("  spread over all trades", lambda r: r.get("counterfactual", {}).get("per_all_trades", float('nan')), "{:+.3f}"),
    ]
    for lab, f, fmt in rows:
        log(f"{lab:<40}{fmt.format(f(res['A'])):>12}{fmt.format(f(res['B'])):>12}")

    with open(os.path.join(OUT_DIR, "pt018_results.json"), "w") as fh:
        json.dump(res, fh, indent=1, default=str)
    with open(os.path.join(OUT_DIR, "pt018_report.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print("\nwritten:", os.path.join(OUT_DIR, "pt018_results.json"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
