#!/usr/bin/env python3
"""PT-003 — Is 5pm the day boundary? The printed "High / Low Reset".

Pre-registration: `PRE_REGISTERED/PT-003_five_pm_high_low_reset.md`
Runs FIRST in its pair (`INDEX.md` §3: PT-003 -> PT-004, both build the 96-slot profile).

THE 24-ANCHOR SWEEP IS THE POINT OF THE DESIGN (`PT-003` §3): "Testing only 17:00
against only 00:00 would give a two-way comparison that a coin flip wins a quarter of
the time. Ranking 17:00 among all 24 candidates is falsifiable in a way that binary
comparison is not." 17:00 is one row of a table it does not get to be the headline of.

usage: python3 run_pt003.py
"""
import json
import os
import sys

import numpy as np

import mmm_lib as L

OUT_DIR = os.path.join(L.ROOT, "06_MANUAL_BACKTEST", "V02", "data")
WINDOW = "W-A"
MONTHU = (0, 1, 2, 3)   # Mon-Thu block starts, the matched basis (see anchored_days)


def block_weekday(day_index, anchor_min):
    """Weekday (Mon=0) on which an anchored 24h block STARTS."""
    start_min = day_index * L.DAY + anchor_min
    return np.array([np.datetime64(int(x) // L.DAY, "D").astype("datetime64[D]")
                     .item().weekday() for x in start_min])


def anchored_days(m15, anchor_min, require_full=True, weekday_start=None):
    """Group bars into days anchored at `anchor_min`, keeping only 96/96-bar days.

    C-6, general form: an anchored day enters only if every one of its 96 fifteen-minute
    buckets exists. Applied identically to every anchor and to every N2 draw, so no
    anchor is scored under a looser standard than another.

    `weekday_start` restricts to blocks STARTING on the given weekdays. This exists
    because of a structural confound the raw sweep has, documented in `run_pt003`'s
    output and in the artifact: 17:00 is the ONLY anchor aligned with the market's own
    weekly open and close, so it is the only one for which Sunday-evening-to-Monday is a
    complete 24-hour block. Every other anchor loses all 52 Sunday starts AND all 50-52
    Friday starts to the weekend gap. Comparing 17:00's 256 days against 00:00's 206 is
    therefore not a like-for-like ranking. Restricting every anchor to Mon-Thu starts
    equalises the basis. BOTH sweeps are reported; neither replaces the other.
    """
    tm = m15.tm
    idx = (tm - anchor_min) // L.DAY          # anchored-day index
    slot = ((tm - anchor_min) % L.DAY) // 15
    uniq = np.unique(idx)
    pos = {int(d): i for i, d in enumerate(uniq)}
    P = np.zeros((len(uniq), 96), dtype=bool)
    rows = np.array([pos[int(x)] for x in idx])
    P[rows, slot] = True
    full = P.all(axis=1)
    if weekday_start is not None:
        wd = block_weekday(uniq, anchor_min)
        full = full & np.isin(wd, list(weekday_start))
    keep_days = uniq[full] if require_full else uniq
    keep_set = {int(d) for d in keep_days}
    sel = np.array([int(x) in keep_set for x in idx])
    return idx[sel], slot[sel], sel, int(full.sum()), int((~full).sum())


def metrics_for_anchor(m15, anchor_min, weekday_start=None):
    """`PT-003` Metrics 1-3 for one candidate anchor hour."""
    idx, slot, sel, n_full, n_drop = anchored_days(m15, anchor_min,
                                                   weekday_start=weekday_start)
    if n_full == 0:
        return None
    h, l = m15.h[sel], m15.l[sel]
    tr = (h - l) / L.PIP
    order = np.lexsort((slot, idx))
    idx, slot, h, l, tr = idx[order], slot[order], h[order], l[order], tr[order]
    n_days = n_full
    H = h.reshape(n_days, 96)
    Lo = l.reshape(n_days, 96)
    TR = tr.reshape(n_days, 96)

    i_hi = np.argmax(H, axis=1)
    i_lo = np.argmin(Lo, axis=1)

    # Metric 1 — mean absolute time-gap between the day's high and low, in bars
    m1 = float(np.mean(np.abs(i_hi.astype(float) - i_lo.astype(float))))

    # Metric 2 — share of days whose high OR low falls within 30 minutes of the anchor.
    # DECLARED READING: "within 30 minutes of the anchor" is taken as either side of the
    # anchor instant, i.e. slots {0, 1} (the first 30 min) or {94, 95} (the last 30 min).
    edge = {0, 1, 94, 95}
    near = np.array([(a in edge) or (b in edge) for a, b in zip(i_hi, i_lo)])
    m2 = float(near.mean())

    # Metric 3 — Gini-style concentration of the day's true range across its 96 bars
    m3 = float(np.mean([L.gini(TR[k]) for k in range(n_days)]))

    return dict(n_days=n_days, n_dropped=n_drop, m1=m1, m2=m2, m3=m3,
                near_count=int(near.sum()))


def run_arm(arm, log):
    m15 = L.window(L.load_m15(arm), WINDOW)
    log(f"\n----- ARM {arm} -----")
    log(f"{WINDOW} M15 bars: {len(m15):,}   span {L.m2s(m15.tm[0])} -> "
        f"{L.m2s(m15.tm[-1])}")

    # ---- BASELINE FIRST (`PT-003` §7 step 4: run N2 before ranking anything) ----
    log("\n[N2 BASELINE — circular clock shift, 1,000 draws, seed 20260812.]")
    log("  Computed and printed BEFORE any anchor is ranked.")
    offs = L.n2_offsets()
    n2 = dict(m1=[], m2=[], m3=[])
    n2m = dict(m1=[], m2=[], m3=[])
    for off in offs:
        r = metrics_for_anchor(m15, L.SESSION_ANCHOR + int(off))
        if r is not None:
            for k in ("m1", "m2", "m3"):
                n2[k].append(r[k])
        rm = metrics_for_anchor(m15, L.SESSION_ANCHOR + int(off), weekday_start=MONTHU)
        if rm is not None:
            for k in ("m1", "m2", "m3"):
                n2m[k].append(rm[k])
    n2 = {k: np.array(v) for k, v in n2.items()}
    n2m = {k: np.array(v) for k, v in n2m.items()}
    log(f"  usable draws: {len(n2['m1'])} of {L.ITERATIONS}")
    log(f"  Metric 1 (mean |high-low| gap, bars)      : {L.dist_line(n2['m1'])}")
    log(f"  Metric 2 (share of extremes near anchor)  : {L.dist_line(n2['m2'])}")
    log(f"  Metric 3 (mean Gini of intraday range)    : {L.dist_line(n2['m3'])}")
    log("  MATCHED BASIS (Mon-Thu block starts only) — see the confound note below:")
    log(f"  Metric 1 : {L.dist_line(n2m['m1'])}")
    log(f"  Metric 2 : {L.dist_line(n2m['m2'])}")
    log(f"  Metric 3 : {L.dist_line(n2m['m3'])}")
    log("  NOTE, stated rather than glossed: a circular clock shift of a 24-hour")
    log("  anchoring metric IS the anchor sweep at 15-minute granularity. N2 and the")
    log("  second baseline are therefore the same object at different resolutions, and")
    log("  that is a property of this test's design, not a defect. Both are reported.")

    # ---- THE 24-ANCHOR SWEEP (second baseline AND the rule arm together) ----
    log("\n[THE 24-ANCHOR SWEEP — 17:00 is one row of a table it does not headline]")
    rows, rowsm = {}, {}
    for hh in range(24):
        r = metrics_for_anchor(m15, hh * 60)
        if r is not None:
            rows[hh] = r
        rm = metrics_for_anchor(m15, hh * 60, weekday_start=MONTHU)
        if rm is not None:
            rowsm[hh] = rm
    log(f"  {'anchor':>7} {'n days':>7} {'excl':>5} {'M1 gap':>9} {'M2 near':>9} "
        f"{'M3 gini':>9}")
    for hh in sorted(rows):
        r = rows[hh]
        mark = "   <<< the printed reset" if hh == 17 else ""
        log(f"  {hh:02d}:00  {r['n_days']:7d} {r['n_dropped']:5d} {r['m1']:9.2f} "
            f"{r['m2']:9.4f} {r['m3']:9.4f}{mark}")

    log("\n  >>> STRUCTURAL CONFOUND IN THE RAW SWEEP, FOUND BEFORE ANY RANKING <<<")
    log("  17:00 keeps %d anchored days; every other anchor keeps ~%d." %
        (rows[17]["n_days"], rows[0]["n_days"]))
    log("  Cause: 17:00 is the ONLY anchor aligned with the market's own weekly open")
    log("  and close. A 24h block anchored at 17:00 is exactly one trading session, so")
    log("  Sunday-17:00 -> Monday-17:00 is complete and Friday-17:00 -> Saturday has no")
    log("  bars at all (it is not a block). Every OTHER anchor loses all 52 Sunday")
    log("  starts and all ~50 Friday starts to the weekend gap.")
    log("  Consequence: the raw ranking compares 17:00's 256 days against 00:00's 206")
    log("  DIFFERENT days. That is not a like-for-like ranking, and the advantage is")
    log("  a property of the CLOCK ALIGNMENT, not of price behaviour.")
    log("  Handling: the matched-basis sweep below restricts EVERY anchor to Mon-Thu")
    log("  block starts. No pre-registered threshold, window or metric is changed; the")
    log("  pre-registered comparison is made valid. BOTH sweeps are reported.")

    log("\n[MATCHED-BASIS SWEEP — every anchor restricted to Mon-Thu block starts]")
    log(f"  {'anchor':>7} {'n days':>7} {'M1 gap':>9} {'M2 near':>9} {'M3 gini':>9}")
    for hh in sorted(rowsm):
        r = rowsm[hh]
        mark = "   <<< the printed reset" if hh == 17 else ""
        log(f"  {hh:02d}:00  {r['n_days']:7d} {r['m1']:9.2f} {r['m2']:9.4f} "
            f"{r['m3']:9.4f}{mark}")

    # ---- RANKS ----
    log("\n[RANK OF 17:00 AMONG THE 24 CANDIDATES — all three metrics, none preferred]")
    ranks = {}
    for k, label, hi_is_better in (
            ("m1", "M1 mean |high-low| gap (bars)", True),
            ("m2", "M2 share of extremes within 30 min of the anchor", False),
            ("m3", "M3 mean Gini concentration of intraday range", None)):
        vals = np.array([rows[h][k] for h in sorted(rows)])
        hrs = np.array(sorted(rows))
        order_desc = np.argsort(-vals)
        rank_desc = int(np.where(hrs[order_desc] == 17)[0][0]) + 1
        rank_asc = len(hrs) + 1 - rank_desc
        obs = rows[17][k]
        pct = L.percentile_of(obs, n2[k])
        ranks[k] = dict(obs=float(obs), rank_high=rank_desc, rank_low=rank_asc,
                        n=len(hrs), pct_n2=pct,
                        best_hour=int(hrs[order_desc[0]]),
                        worst_hour=int(hrs[order_desc[-1]]))
        log(f"  {label}")
        log(f"    17:00 = {obs:.4f}   rank {rank_desc}/{len(hrs)} descending "
            f"({rank_asc}/{len(hrs)} ascending)")
        log(f"    highest {hrs[order_desc[0]]:02d}:00 = {vals[order_desc[0]]:.4f}   "
            f"lowest {hrs[order_desc[-1]]:02d}:00 = {vals[order_desc[-1]]:.4f}")
        log(f"    percentile within N2: {pct:.1f}")
        valsm = np.array([rowsm[h][k] for h in sorted(rowsm)])
        hrsm = np.array(sorted(rowsm))
        od = np.argsort(-valsm)
        rd = int(np.where(hrsm[od] == 17)[0][0]) + 1
        obsm = rowsm[17][k]
        pctm = L.percentile_of(obsm, n2m[k])
        ranks[k]["matched"] = dict(obs=float(obsm), rank_high=rd, n=len(hrsm),
                                   pct_n2=pctm,
                                   best_hour=int(hrsm[od[0]]),
                                   worst_hour=int(hrsm[od[-1]]))
        log(f"    MATCHED BASIS: 17:00 = {obsm:.4f}   rank {rd}/{len(hrsm)} descending"
            f"   percentile within N2 {pctm:.1f}")
    return dict(arm=arm, anchors={str(h): rows[h] for h in rows},
                anchors_matched={str(h): rowsm[h] for h in rowsm}, ranks=ranks,
                n2={k: L.dist_line(v) for k, v in n2.items()},
                n2_matched={k: L.dist_line(v) for k, v in n2m.items()},
                n_days_17=rows[17]["n_days"], n_drop_17=rows[17]["n_dropped"],
                n_days_17_matched=rowsm[17]["n_days"])


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    lines = []

    def log(s=""):
        print(s)
        lines.append(s)

    log(L.header("PT-003", "Is 5pm the day boundary? The printed High/Low Reset (W-A)",
                 "window   : W-A 2015-01-04 -> 2015-12-31 (wholly inside DEVELOPMENT)"))
    log("PRE-REG  : PRE_REGISTERED/PT-003_five_pm_high_low_reset.md")
    log("CLAIM    : V02 printed session table [00:45:55], first line:")
    log("           '5pm    High / Low Reset (The MM Spread Is Set)'  — printed and")
    log("           NEVER SPOKEN (`V02_INTERPRETATION.md` §10.2 U2).")
    log("DESIGN   : all 24 hourly anchors, three metrics, both `D-031` arms, in ONE")
    log("           pass so no ordering of the computation can influence what is looked")
    log("           at first (`PT-003` §7 step 3).")
    log("C-6      : an anchored day enters only with all 96 of its 15-minute buckets;")
    log("           exclusions counted per anchor in the sweep table.")
    log("SCOPE    : NOT a test of 'The MM Spread Is Set' — broker spread is invisible")
    log("           to candle data (`PT-003` §6).")

    res = {}
    for arm in ("A", "B"):
        res[arm] = run_arm(arm, log)

    log("\n" + "=" * 78)
    log("BOTH ARMS SIDE BY SIDE — `D-031` requires both, always")
    log("=" * 78)
    log(f"{'':46}{'ARM A':>12}{'ARM B':>12}")
    for k, lab in (("m1", "M1 gap: 17:00 value"), ("m2", "M2 near: 17:00 value"),
                   ("m3", "M3 gini: 17:00 value")):
        log(f"{lab:<46}{res['A']['ranks'][k]['obs']:>12.4f}"
            f"{res['B']['ranks'][k]['obs']:>12.4f}")
    for k, lab in (("m1", "M1 rank of 17:00 (of 24, descending)"),
                   ("m2", "M2 rank of 17:00 (of 24, descending)"),
                   ("m3", "M3 rank of 17:00 (of 24, descending)")):
        log(f"{lab:<46}{res['A']['ranks'][k]['rank_high']:>12d}"
            f"{res['B']['ranks'][k]['rank_high']:>12d}")
    for k, lab in (("m1", "M1 percentile within N2"),
                   ("m2", "M2 percentile within N2"),
                   ("m3", "M3 percentile within N2")):
        log(f"{lab:<46}{res['A']['ranks'][k]['pct_n2']:>12.1f}"
            f"{res['B']['ranks'][k]['pct_n2']:>12.1f}")
    log("  --- MATCHED BASIS (Mon-Thu block starts, like-for-like) ---")
    for k, lab in (("m1", "M1 rank of 17:00 (matched)"),
                   ("m2", "M2 rank of 17:00 (matched)"),
                   ("m3", "M3 rank of 17:00 (matched)")):
        log(f"{lab:<46}{res['A']['ranks'][k]['matched']['rank_high']:>12d}"
            f"{res['B']['ranks'][k]['matched']['rank_high']:>12d}")
    for k, lab in (("m1", "M1 percentile within N2 (matched)"),
                   ("m2", "M2 percentile within N2 (matched)"),
                   ("m3", "M3 percentile within N2 (matched)")):
        log(f"{lab:<46}{res['A']['ranks'][k]['matched']['pct_n2']:>12.1f}"
            f"{res['B']['ranks'][k]['matched']['pct_n2']:>12.1f}")
    da = "%d (%d)" % (res["A"]["n_days_17"], res["A"]["n_drop_17"])
    db = "%d (%d)" % (res["B"]["n_days_17"], res["B"]["n_drop_17"])
    log(f"{'anchored days at 17:00 (excluded)':<46}{da:>12}{db:>12}")

    with open(os.path.join(OUT_DIR, "pt003_results.json"), "w") as fh:
        json.dump(res, fh, indent=1, default=str)
    with open(os.path.join(OUT_DIR, "pt003_report.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print("\nwritten:", os.path.join(OUT_DIR, "pt003_results.json"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
