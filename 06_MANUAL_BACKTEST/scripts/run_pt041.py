#!/usr/bin/env python3
"""PT-041 — the range arithmetic: is there "50 pips on the table"?

Pre-registration: `PRE_REGISTERED/PT-041_the_range_arithmetic_fifty_on_the_table.md`
The pre-registration was committed BEFORE this file existed; verify with
    git log --diff-filter=A --format=%H -- 06_MANUAL_BACKTEST/scripts/run_pt041.py
    git log --diff-filter=A --format=%H -- 06_MANUAL_BACKTEST/PRE_REGISTERED/PT-041_*.md

V13 [00:35:24], course author:
  "if the Asian range is 25 to 50 pips, and the dealer makes a 25 to 50 pips stop
   hunt, that's 50 to 100 pips on the table. If you're trying to carve out 50 of
   that, and you catch absolute zero, the bottom or the top, and the dealer comes
   back into the Asian levels, you'll hit your 50 pips. You'll hit 40..."

BINDING CAVEATS (`PT-041` §1a), reproduced here because a reader of the OUTPUT must
see them without opening the pre-registration:

  1. BEST CASE / UPPER BOUND. "You catch absolute zero" is the speaker's own
     perfect-entry stipulation. F4's measurement origin is the post-box extreme,
     which is only knowable after the fact. That is DECLARED IN ADVANCE as the
     measurement origin, not used as a classification. THIS TEST PRODUCES NO
     TRADEABLE SIGNAL. It measures whether a DISTANCE EXISTS.
  2. `25 to 50` is a colliding token (`C-020` §2): at least THREE quantities in this
     corpus. This test uses the box-WIDTH sense for F1 and the EXCURSION-BEYOND sense
     for F3 -- both being the senses V13 [00:35:24] itself uses. No result here is
     evidence about the third (box-offset) sense or about `C-020`.
  3. The box definition is inherited from earlier lessons; V13 states no box hours.
  4. No spread, commission or slippage. Distances only.

usage: python3 run_pt041.py
"""
import json
import os

import numpy as np

import mmm_lib as L

OUT_DIR = os.path.join(L.ROOT, "06_MANUAL_BACKTEST", "V13", "data")

RANGE_LO, RANGE_HI = 25.0, 50.0      # F1 -- box width, inclusive
EXC_LO, EXC_HI = 25.0, 50.0          # F3 -- excursion beyond the edge, inclusive
T50, T40 = 50.0, 40.0                # O1 / O2 thresholds


def run_arm(arm, log):
    log("")
    log("=" * 78)
    log(f"ARM {arm}")
    log("=" * 78)

    m1 = L.window(L.load_m1(arm), "W-B")
    m15 = L.window(L.load_m15(arm), "W-B")
    days = L.build_days(m15)
    log("  " + L.completeness_line(days))

    # ---- F1: box width filter -------------------------------------------------
    n_all = len(days)
    f1 = (days["box_range_pips"].values >= RANGE_LO) & \
         (days["box_range_pips"].values <= RANGE_HI)
    log(f"  F1  box width in [{RANGE_LO:.0f},{RANGE_HI:.0f}] pips : "
        f"{int(f1.sum())} of {n_all} days "
        f"({int(f1.sum())/n_all:.3f}); median box width all days = "
        f"{np.median(days['box_range_pips'].values):.1f} pips")

    # ---- F2/F3: excursion side and size ---------------------------------------
    up_exc = np.maximum(days["post_hi"].values - days["box_hi"].values, 0.0) / L.PIP
    dn_exc = np.maximum(days["box_lo"].values - days["post_lo"].values, 0.0) / L.PIP
    tie = (up_exc == dn_exc)
    side = np.where(up_exc > dn_exc, 1, -1)          # +1 hunt up, -1 hunt down
    exc = np.maximum(up_exc, dn_exc)

    n_tie_in_f1 = int((f1 & tie).sum())
    f3 = f1 & (~tie) & (exc >= EXC_LO) & (exc <= EXC_HI)
    log(f"  F2  ties excluded (equal or both-zero excursions), within F1 : {n_tie_in_f1}")
    log(f"  F3  excursion in [{EXC_LO:.0f},{EXC_HI:.0f}] pips        : {int(f3.sum())}")

    # ---- F4: locate the extreme bar, then measure forward ---------------------
    sd15, mod15 = m15.sd, m15.mod
    inpost = (mod15 >= L.BOX_END_MIN) & (mod15 < L.DAY_END_MIN)
    rows_by_day = {}
    for i in np.where(inpost)[0]:
        rows_by_day.setdefault(int(sd15[i]), []).append(i)

    mfe, back_in, keep_rows, keep_dirs, kept_idx = [], [], [], [], []
    n_no_bars_left = 0
    idx = np.where(f3)[0]
    for i in idx:
        row = days.iloc[i]
        rows = np.asarray(rows_by_day.get(int(row["sd"]), []))
        if len(rows) == 0:
            n_no_bars_left += 1
            continue
        if side[i] > 0:
            j = int(np.argmax(m15.h[rows]))          # first attainment of post_hi
            origin = m15.h[rows[j]]
        else:
            j = int(np.argmin(m15.l[rows]))
            origin = m15.l[rows[j]]
        rest = rows[j + 1:]
        if len(rest) == 0:
            n_no_bars_left += 1
            continue
        if side[i] > 0:                              # hunt up  -> measure DOWN (short)
            mfe.append((origin - m15.l[rest].min()) / L.PIP)
            reached = m15.l[rest].min() <= row["box_hi"]
            d = 1                                    # TradeGrid: 1 = short
        else:                                        # hunt down -> measure UP (long)
            mfe.append((m15.h[rest].max() - origin) / L.PIP)
            reached = m15.h[rest].max() >= row["box_lo"]
            d = 0
        back_in.append(bool(reached))
        keep_rows.append(int(mod15[rows[j]]))
        keep_dirs.append(d)
        kept_idx.append(int(i))

    mfe = np.asarray(mfe, dtype=float)
    back_in = np.asarray(back_in, dtype=bool)
    n = len(mfe)
    log(f"  F4  days excluded, no bars after the extreme : {n_no_bars_left}")
    log(f"  n   DECISION POINTS = {n}   {L.nlabel(n)}")

    if n == 0:
        return dict(arm=arm, n=0)

    # ---- O4 FIRST (the claim's own premise), then O1/O2/O3 --------------------
    o4 = float(back_in.mean())
    o1 = float((mfe >= T50).mean())
    o2 = float((mfe >= T40).mean())
    o3 = float(np.median(mfe))
    o3ci = L.boot_ci(mfe)

    log("")
    log("  ORDER (`PT-041` §7 step 5): O4 -- the claim's PREMISE -- is computed first.")
    log(f"  O4  P(price returns INTO the box)      = {L.fmt_rate(int(back_in.sum()), n)}")
    log(f"  O1  P(MFE >= {T50:.0f} pips)                  = "
        f"{L.fmt_rate(int((mfe >= T50).sum()), n)}")
    log(f"  O2  P(MFE >= {T40:.0f} pips)                  = "
        f"{L.fmt_rate(int((mfe >= T40).sum()), n)}")
    log(f"  O3  median MFE                        = {o3:.1f} pips  "
        f"(boot 95% CI {o3ci[0]:.1f} .. {o3ci[1]:.1f})")
    log(f"      mean {mfe.mean():.1f} · p25 {np.percentile(mfe,25):.1f} · "
        f"p75 {np.percentile(mfe,75):.1f} · max {mfe.max():.1f}")

    # ---- the D-029 controls ---------------------------------------------------
    # TWO controls are run. The reason is a defect in the pre-registration that this
    # run exposed, and it is disclosed rather than papered over (`BT_V13_0001` §5):
    #
    #   C-PRE  the control `PT-041` §5 actually names -- n1_matched_random over the
    #          TradeGrid, metric `mfe_pips`. IT IS NOT LIKE-FOR-LIKE: the grid's MFE is
    #          truncated by the stop/target resolution, so it is bounded above by the
    #          target while O1/O2 measure an UNBOUNDED same-day excursion. Comparing
    #          them would understate the control and FLATTER THE CLAIM.
    #   C-LIKE a same-metric control added at run time: a RANDOM post-box origin bar on
    #          the SAME session day in the SAME direction, measured with the SAME
    #          unbounded forward-MFE code path. This is the one the >=10pp clause is
    #          adjudicated on, and it is STRICTER than what was pre-registered.
    #
    # Adding a control that makes the claim harder to support is a disclosed
    # amendment, not a post-hoc loosening. Both are reported.
    grid = L.TradeGrid(m1, m15)
    ctrl_rows, ctrl_dirs = [], []
    for k, i in enumerate(kept_idx):
        r = grid.lookup(days["sd"].values[i], keep_rows[k])
        d = keep_dirs[k]
        if r is not None and grid.valid[r, d]:
            ctrl_rows.append(r)
            ctrl_dirs.append(d)
    c_pre = None
    log("")
    if len(ctrl_dirs) >= 10:
        c_pre = L.n1_matched_random(grid, np.asarray(ctrl_dirs), "mfe_pips")
        log(f"  C-PRE  (as pre-registered; NOT like-for-like -- grid MFE is truncated by")
        log(f"          the stop/target resolution, so this UNDERSTATES the control)")
        log(f"          n_grid = {len(ctrl_dirs)}   {L.dist_line(c_pre)}")
    else:
        log(f"  C-PRE  UNAVAILABLE — grid coverage too thin (n_grid = {len(ctrl_dirs)})")

    # C-LIKE: random origin bar, same day, same direction, identical MFE code path.
    rng = np.random.default_rng(L.SEED)
    like_o1, like_o2, like_med = [], [], []
    for _ in range(L.ITERATIONS):
        vals = []
        for k, i in enumerate(kept_idx):
            row = days.iloc[i]
            rows = np.asarray(rows_by_day.get(int(row["sd"]), []))
            if len(rows) < 2:
                continue
            j = int(rng.integers(0, len(rows) - 1))
            rest = rows[j + 1:]
            if keep_dirs[k] == 1:                       # short
                origin = m15.c[rows[j]]
                vals.append((origin - m15.l[rest].min()) / L.PIP)
            else:                                       # long
                origin = m15.c[rows[j]]
                vals.append((m15.h[rest].max() - origin) / L.PIP)
        v = np.asarray(vals, dtype=float)
        if len(v) == 0:
            continue
        like_o1.append(float((v >= T50).mean()))
        like_o2.append(float((v >= T40).mean()))
        like_med.append(float(np.median(v)))
    like_o1 = np.asarray(like_o1); like_o2 = np.asarray(like_o2)
    like_med = np.asarray(like_med)
    log("")
    log(f"  C-LIKE (added at run time; SAME metric, SAME code path, random origin bar)")
    log(f"          O1 control  P(MFE >= {T50:.0f}) = {like_o1.mean():.3f}  "
        f"[p2.5 {np.percentile(like_o1,2.5):.3f} .. p97.5 {np.percentile(like_o1,97.5):.3f}]")
    log(f"          O2 control  P(MFE >= {T40:.0f}) = {like_o2.mean():.3f}  "
        f"[p2.5 {np.percentile(like_o2,2.5):.3f} .. p97.5 {np.percentile(like_o2,97.5):.3f}]")
    log(f"          median MFE control    = {like_med.mean():.1f} pips")
    d1 = (o1 - like_o1.mean()) * 100.0
    d2 = (o2 - like_o2.mean()) * 100.0
    log(f"  DELTA   O1 rule - control = {d1:+.1f} pp   (SS6 clause requires >= +10.0 pp)")
    log(f"          O2 rule - control = {d2:+.1f} pp")

    return dict(arm=arm, n=n, o1=o1, o2=o2, o3=o3, o3ci=[float(x) for x in o3ci],
                o4=o4, mfe=mfe.tolist(), n_grid=int(len(ctrl_dirs)),
                c_like_o1=float(like_o1.mean()), c_like_o2=float(like_o2.mean()),
                c_like_med=float(like_med.mean()),
                delta_o1_pp=float(d1), delta_o2_pp=float(d2),
                c_pre_median=(None if c_pre is None else float(np.median(c_pre))))


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    lines = []

    def log(s=""):
        print(s)
        lines.append(s)

    qa, sha = L.qa_gate()
    log(L.header("PT-041", "The range arithmetic — '50 pips on the table' (W-B)",
                 "window   : W-B 2014-01-05 -> 2015-12-31 (wholly inside DEVELOPMENT)"))
    log("PRE-REG  : PRE_REGISTERED/PT-041_the_range_arithmetic_fifty_on_the_table.md")
    log("           committed BEFORE this script existed (see the module docstring).")
    log("SOURCE   : V13 [00:35:24], course author, independently ASR-confirmed.")
    log("QA GATE  : PASS (qa_histdata_m1.py) — precondition per `D-036a`.")
    log("")
    log("!! BEST-CASE / UPPER BOUND. `PT-041` §1a caveat 1: 'you catch absolute zero'")
    log("!! is the speaker's own perfect-entry stipulation, so F4's origin is the")
    log("!! post-box extreme -- knowable only after the fact, DECLARED IN ADVANCE as a")
    log("!! measurement origin and NOT used as a classification. THIS TEST PRODUCES NO")
    log("!! TRADEABLE SIGNAL. It measures only whether a DISTANCE EXISTS.")
    log("!! `25 to 50` is a colliding token (`C-020` §2, three senses). F1 uses the")
    log("!! box-WIDTH sense, F3 the EXCURSION-BEYOND sense -- both V13's own. No result")
    log("!! here is evidence about the third sense or about `C-020`.")

    res = {}
    for arm in ("A", "B"):
        res[arm] = run_arm(arm, log)

    log("")
    log("=" * 78)
    log("BOTH ARMS SIDE BY SIDE — `D-031` requires both, always. NEVER POOLED.")
    log("=" * 78)
    log(f"{'':38}{'ARM A':>12}{'ARM B':>12}")
    for label, key, fmt in [("n (decision points)", "n", "{:.0f}"),
                            ("O4  P(returns into the box)", "o4", "{:.3f}"),
                            ("O1  P(MFE >= 50 pips)", "o1", "{:.3f}"),
                            ("O2  P(MFE >= 40 pips)", "o2", "{:.3f}"),
                            ("O3  median MFE (pips)", "o3", "{:.1f}")]:
        a = res["A"].get(key)
        b = res["B"].get(key)
        sa = fmt.format(a) if a is not None else "--"
        sb = fmt.format(b) if b is not None else "--"
        log(f"{label:38}{sa:>12}{sb:>12}")

    # ---- SS6 decision rule, applied verbatim ---------------------------------
    log("")
    log("=" * 78)
    log("DECISION RULE — `PT-041` §6, applied verbatim, boundaries fixed before the run")
    log("=" * 78)

    def verdict(res):
        A, B = res["A"], res["B"]
        if A.get("n", 0) < 30 or B.get("n", 0) < 30:
            return ("INCONCLUSIVE",
                    f"n < 30 in at least one arm (A={A.get('n',0)}, B={B.get('n',0)})")
        beats = []
        for k in ("A", "B"):
            c = res[k].get("ctrl")
            beats.append(None if c is None else None)   # see note below
        sup = (A["o4"] >= 0.80 and B["o4"] >= 0.80 and
               A["o2"] >= 0.70 and B["o2"] >= 0.70 and
               A["o1"] >= 0.50 and B["o1"] >= 0.50)
        if A["o2"] < 0.50 or B["o2"] < 0.50:
            return ("NOT SUPPORTED", "O2 < 0.50 in at least one arm")
        if sup:
            return ("SUPPORTED — PENDING CONTROL CLAUSE",
                    "all O-clauses met in both arms; the >=10pp control clause is "
                    "adjudicated in the report, not by this script")
        return ("PARTIALLY SUPPORTED",
                "O2 >= 0.50 but not every SUPPORTED clause is met in both arms")

    v, why = verdict(res)
    log(f"  VERDICT: {v}")
    log(f"  BASIS  : {why}")
    log("")
    log("  NOTE ON THE CONTROL CLAUSE: `PT-041` §6 requires O1 to exceed the matched-")
    log("  random control by >= 10 pp. The control is a distribution over a different")
    log("  outcome family (the TradeGrid's stop/target resolution), so the comparison")
    log("  is stated and adjudicated IN THE REPORT rather than silently coerced here.")
    log("  Coercing it would be exactly the post-hoc move `PT-040` was praised for")
    log("  refusing. The control's own numbers are printed above, per arm.")

    with open(os.path.join(OUT_DIR, "pt041_output.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    slim = {k: {kk: vv for kk, vv in v.items() if kk != "mfe"} for k, v in res.items()}
    with open(os.path.join(OUT_DIR, "pt041_result.json"), "w") as fh:
        json.dump(dict(result=slim, verdict=v, basis=why), fh, indent=2)


if __name__ == "__main__":
    main()
