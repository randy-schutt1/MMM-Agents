#!/usr/bin/env python3
"""PT-005 — "Take a trade at 8 o'clock and then 9:30 when the dealer hits your stops"

Pre-registration: `PRE_REGISTERED/PT-005_new_york_opens_at_930_not_8.md`
Independent of the PT-014 family; W-B.

This is the ONLY falsifiable prediction the instructor states as an experiment for the
student to run, anywhere in V01-V04. He names the entry time, the adverse event, the time
of the adverse event, and the way to check.

usage: python3 run_pt005.py
"""
import json
import os
import sys

import numpy as np

import mmm_lib as L

OUT_DIR = os.path.join(L.ROOT, "06_MANUAL_BACKTEST", "V02", "data")
WINDOW = "W-B"
ENTRY_MIN = 8 * 60                    # the 08:00 bar; its CLOSE is 08:15
BINS = [(8 * 60 + 30 * k, 8 * 60 + 30 * (k + 1)) for k in range(8)]   # 08:00-12:00
NY_BIN = (9 * 60 + 30, 10 * 60)       # the claim's window


def slot_mae(m1, sd_list, entry_min, direction, n_slots=8, slot=30):
    """`PT-005` Measure 2 — MAE accrued in each 30-minute slot, whether or not the stop
    is hit. Computed on the RAW path (unstopped), because "whether or not" requires it.
    """
    rows_by_day = {}
    sd1 = m1.sd
    for i in range(len(m1.tm)):
        rows_by_day.setdefault(int(sd1[i]), []).append(i)
    out = np.full((len(sd_list), n_slots), np.nan)
    for k, d in enumerate(sd_list):
        idx = np.asarray(rows_by_day.get(int(d), []))
        if len(idx) == 0:
            continue
        e = int(d) * L.DAY + entry_min + 15
        fwd = idx[(m1.tm[idx] >= e) & (m1.tm[idx] < e + n_slots * slot)]
        if len(fwd) == 0:
            continue
        px = m1.o[fwd[0]]
        rel = (m1.tm[fwd] - e) // slot
        for s in range(n_slots):
            sel = fwd[rel == s]
            if len(sel) == 0:
                continue
            adv = ((m1.h[sel] - px) if direction == 0 else (px - m1.l[sel])) / L.PIP
            # direction 0 = long -> adverse is DOWN; recompute correctly
            adv = ((px - m1.l[sel]) if direction == 0 else (m1.h[sel] - px)) / L.PIP
            out[k, s] = float(np.max(adv))
    return out


def hist_counts(vals, bins):
    return np.array([int(((vals >= a) & (vals < b)).sum()) for a, b in bins])


def run_arm(arm, log):
    m15 = L.window(L.load_m15(arm), WINDOW)
    m1 = L.window(L.load_m1(arm), WINDOW)
    # C-6: the measured span is the 08:00 entry through the 17:00 horizon.
    uniq, ok, excl = L.complete_days(m15, [(8 * 60, 17 * 60)])
    days = uniq[ok]
    log(f"\n----- ARM {arm} -----")
    log(f"COMPLETENESS (C-6, 08:00-17:00 required): "
        f"{L.completeness_line_general(uniq, ok, excl)}")

    # Full-day entry grid: the rule needs 08:00, N1 needs 08:00-12:00, N2 needs every
    # hour (a clock shift moves the entry as well as the event).
    grid = L.TradeGrid(m1, m15, elig_from=0, elig_to=1440)
    keep = set(int(d) for d in days)
    valid_day = np.array([int(s) in keep for s in grid.entry_sd])
    log(f"trade grid: {len(grid.entry_tm):,} entry bars x 2 directions, stop 18 / "
        f"target 50, resolved on M1")

    log("\n  >>> `PT-005` §5 warns the entry-relative grid is the arm that decides this")
    log("  test. IT IS DEGENERATE HERE, BY CONSTRUCTION, AND THAT IS ITSELF THE FINDING:")
    log("  every trade enters at exactly 08:15, so wall-clock stop-out time = 08:15 +")
    log("  elapsed, deterministically. The two grids are an affine relabelling of each")
    log("  other and carry identical information. A fixed entry time CANNOT separate")
    log("  '09:30 matters' from 'entry + 75 minutes matters'. The separation is supplied")
    log("  instead by N1 and N2, which BOTH vary the entry hour. Nothing is approximated")
    log("  and no substitute arm is invented.")

    # ---------------- BASELINES FIRST (`PT-005` §7 step 3) ----------------
    log("\n[BASELINES — computed and printed BEFORE the observed stop-out histogram]")
    pool_n1 = np.where(valid_day & (grid.entry_mod >= 8 * 60)
                       & (grid.entry_mod < 12 * 60) & grid.valid.any(1))[0]
    log(f"  N1 pool (entries drawn at random from 08:00-12:00): {len(pool_n1)} bars")
    rng = np.random.default_rng(L.SEED)
    n_rule = int(valid_day.sum() and (grid.entry_mod == ENTRY_MIN).sum())
    n_rule = int(((grid.entry_mod == ENTRY_MIN) & valid_day).sum())
    n1 = {d: np.full(L.ITERATIONS, np.nan) for d in (0, 1)}
    for d in (0, 1):
        for it in range(L.ITERATIONS):
            pick = rng.choice(pool_n1, size=n_rule, replace=True)
            ex = grid.exit_min[pick, d]
            res = np.isfinite(ex)
            if not res.any():
                continue
            wall = grid.entry_mod[pick][res] + 15 + ex[res]
            n1[d][it] = float(((wall >= NY_BIN[0]) & (wall < NY_BIN[1])).mean())
        log(f"  N1 dir {'long' if d==0 else 'short'}: share of stop-outs landing in "
            f"09:30-10:00 (wall clock) {L.dist_line(n1[d])}")

    # N2 — circular clock shift: the entry moves with the event, which is the only way
    # to ask whether 09:30 SPECIFICALLY matters or merely SOME hour does.
    offs = L.n2_offsets()
    n2 = {d: [] for d in (0, 1)}
    for d in (0, 1):
        for off in offs:
            em = int((ENTRY_MIN - int(off)) % L.DAY)
            sel = np.where((grid.entry_mod == em) & valid_day & grid.valid[:, d])[0]
            if len(sel) == 0:
                continue
            ex = grid.exit_min[sel, d]
            res = np.isfinite(ex)
            if not res.any():
                continue
            # the shifted 09:30-10:00 window is entry + 75..105 minutes
            rel = ex[res] + 15
            n2[d].append(float(((rel >= 75) & (rel < 105)).mean()))
        n2[d] = np.array(n2[d])
        log(f"  N2 dir {'long' if d==0 else 'short'}: same share under a randomised "
            f"clock {L.dist_line(n2[d])}  ({len(n2[d])} usable draws)")

    # ---------------- RULE ARM ----------------
    log("\n[RULE ARM — entry at the 08:00 bar close, EVERY trading day, no filter]")
    sel = np.where((grid.entry_mod == ENTRY_MIN) & valid_day)[0]
    sd_sel = grid.entry_sd[sel]
    res = {}
    for d, nm in ((0, "LONG"), (1, "SHORT")):
        ok_d = grid.valid[sel, d]
        rows = sel[ok_d]
        oc = grid.outcome[rows, d]
        ex = grid.exit_min[rows, d]
        pl = grid.pnl_pips[rows, d]
        stopped = oc == -1
        log(f"\n  {nm}-only arm: {L.nlabel(len(rows))}")
        log(f"    target / stop / open at 17:00 : {int((oc==1).sum())} / "
            f"{int(stopped.sum())} / {int((oc==0).sum())}")
        log(f"    hit rate (of resolved)        : "
            f"{L.fmt_rate(int((oc==1).sum()), int((oc!=0).sum()))}")
        log(f"    expectancy                    : {np.nanmean(pl):+.2f} pips")
        wall = ENTRY_MIN + 15 + ex[stopped]
        counts = hist_counts(wall, BINS)
        tot = int(counts.sum())
        log(f"    MEASURE 1 — time-of-day of the STOP-OUT ({tot} stop-outs inside "
            f"08:00-12:00 of {int(stopped.sum())} total):")
        for (a, b), c in zip(BINS, counts):
            tag = "   <<< the claim's window" if (a, b) == NY_BIN else ""
            bar = "#" * int(round(40 * c / max(counts.max(), 1)))
            log(f"      {a//60:02d}:{a%60:02d}-{b//60:02d}:{b%60:02d}  {c:4d}  "
                f"{bar}{tag}")
        obs = float(((wall >= NY_BIN[0]) & (wall < NY_BIN[1])).sum() / max(len(wall), 1))
        log(f"    share of stop-outs in 09:30-10:00 : "
            f"{L.fmt_rate(int(((wall>=NY_BIN[0])&(wall<NY_BIN[1])).sum()), len(wall))}")
        p1 = L.percentile_of(obs, n1[d])
        p2 = L.percentile_of(obs, n2[d])
        log(f"    percentile within N1 {p1:.1f}   within N2 {p2:.1f}")
        log(f"    MEASURE 1b — the SAME data on the entry-relative grid (affine "
            f"relabelling, see above):")
        relc = hist_counts(ex[stopped] + 15, [(30 * k, 30 * (k + 1)) for k in range(8)])
        log("      " + "  ".join(f"{30*k}-{30*(k+1)}m:{c}" for k, c in enumerate(relc)))

        mae = slot_mae(m1, sd_sel[ok_d], ENTRY_MIN, d)
        log(f"    MEASURE 2 — MAE accrued in each 30-min slot (raw path, unstopped), "
            f"mean pips:")
        line = "      " + "  ".join(
            f"{BINS[s][0]//60:02d}:{BINS[s][0]%60:02d} {np.nanmean(mae[:, s]):5.2f}"
            for s in range(8))
        log(line)
        peak = int(np.nanargmax(np.nanmean(mae, axis=0)))
        log(f"      peak MAE slot: {BINS[peak][0]//60:02d}:{BINS[peak][0]%60:02d}-"
            f"{BINS[peak][1]//60:02d}:{BINS[peak][1]%60:02d}"
            f"   ({'IS' if BINS[peak]==NY_BIN else 'is NOT'} the claim's window)")
        res[nm] = dict(n=len(rows), n_target=int((oc == 1).sum()),
                       n_stop=int(stopped.sum()), n_open=int((oc == 0).sum()),
                       hit_rate=float((oc[oc != 0] == 1).mean()) if (oc != 0).any() else np.nan,
                       expectancy=float(np.nanmean(pl)),
                       stopout_counts=[int(x) for x in counts],
                       share_ny=obs, pct_n1=p1, pct_n2=p2,
                       mae_by_slot=[float(np.nanmean(mae[:, s])) for s in range(8)],
                       peak_slot=f"{BINS[peak][0]//60:02d}:{BINS[peak][0]%60:02d}")
    return dict(arm=arm, n_days=int(len(days)), excluded=excl, arms=res,
                n1={str(d): L.dist_line(n1[d]) for d in (0, 1)},
                n2={str(d): L.dist_line(n2[d]) for d in (0, 1)})


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    lines = []

    def log(s=""):
        print(s)
        lines.append(s)

    log(L.header("PT-005", "'Take a trade at 8 and then 9:30 when the dealer hits your stops' (W-B)",
                 "window   : W-B 2014-01-05 -> 2015-12-31 (wholly inside DEVELOPMENT)"))
    log("PRE-REG  : PRE_REGISTERED/PT-005_new_york_opens_at_930_not_8.md")
    log("CLAIM    : V02 [00:51:03]-[00:51:20] 'Forex Factory shows New York open at 8...")
    log("           Take a trade at 8 o'clock and then 9:30 when the dealer hits your")
    log("           stops, come back next week and tell me.'")
    log("ENTRY    : mechanical, at the 08:00 bar close, EVERY trading day, NO filter of")
    log("           any kind. Both directions run as separate arms (he names none).")
    log("SCOPE    : the 08:00 entry is a MEASUREMENT DEVICE, not a strategy; its win")
    log("           rate is not a result about the method (`PT-005` §6).")

    res = {}
    for arm in ("A", "B"):
        res[arm] = run_arm(arm, log)

    log("\n" + "=" * 78)
    log("BOTH ARMS SIDE BY SIDE — `D-031` requires both, always")
    log("=" * 78)
    log(f"{'':44}{'ARM A':>12}{'ARM B':>12}")
    for nm in ("LONG", "SHORT"):
        for k, lab, fmt in (("n", "n", "{:.0f}"), ("n_stop", "stop-outs", "{:.0f}"),
                            ("share_ny", "share of stop-outs in 09:30-10:00", "{:.3f}"),
                            ("pct_n1", "  percentile within N1", "{:.1f}"),
                            ("pct_n2", "  percentile within N2", "{:.1f}"),
                            ("peak_slot", "peak MAE slot", "{}")):
            log(f"{nm+' '+lab:<44}{fmt.format(res['A']['arms'][nm][k]):>12}"
                f"{fmt.format(res['B']['arms'][nm][k]):>12}")

    with open(os.path.join(OUT_DIR, "pt005_results.json"), "w") as fh:
        json.dump(res, fh, indent=1, default=str)
    with open(os.path.join(OUT_DIR, "pt005_report.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print("\nwritten:", os.path.join(OUT_DIR, "pt005_results.json"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
