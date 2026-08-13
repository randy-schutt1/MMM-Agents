#!/usr/bin/env python3
"""PT-032 — the weekend gap, and the one mechanical rationale in V01 (re-issue of PT-019)

NOTHING IS ASSUMED ABOUT THE TWO INSTANTS — §3, §7 step 4
----------------------------------------------------------
"No boundary instant may be assumed. 15 of the corpus's 187 opens are LATE
(17:01-17:10), and `D-036a` documents the week OPEN but NOT the week CLOSE, so the
Friday close is a run-time fact. For this test in particular the whole measurement is
those two instants."

Both are therefore read from M1 timestamps, not M15 buckets: an M15 aggregation floors
a 17:03 open into the 17:00 bucket and would silently erase the lateness this test is
required to measure.

§3a″ — THE FABRICATED GAP, EXCLUDED BY NAME
--------------------------------------------
Applied mechanically across the 2014-06-01 hole, the gap definition would compare the
Friday 2014-05-30 close with the first bar seen at Mon 2014-06-02 15:01 — a price
change accumulated over ~22 hours of trading THE CORPUS DOES NOT CONTAIN. It would be
large, it would land in Measure 1's tail and Measure 2's >50-pip bucket, and it would
be an artifact of absent data. On a test whose entire finding is "how large is the
weekend gap", that single observation could move the headline. EXCLUDED BY NAME, and
that week's four Mon-Thu 17:00 instants are excluded from Measure 4 too (§3a‴).

§0c — THE CONTROL THAT HAD TO BE RELABELLED
--------------------------------------------
`PT-019`'s Measure 4 compared the weekend gap against "intra-week daily-boundary GAPS".
THIS CORPUS HAS NO DAILY BREAK -- QA `C6` finds three intra-week gaps >= 30 min in 3.5
years, 4h43m total. So on Mon-Thu at 17:00 consecutive bars simply abut. The control is
RETAINED (it holds the clock instant, instrument and everything but calendar position
fixed) and RELABELLED to what it measures: a CONTINUOUS-TRADING RETURN across the 17:00
instant. It is a FLOOR, not a matched comparator, and N3 is promoted to CO-PRIMARY
because it is now the only control that separates a real discontinuity from a defect.

§7 step 5 — N3 RUNS FIRST OF ALL
---------------------------------
"A non-zero result there means the harvest is wrong and no other number in the test can
be trusted." It is therefore computed and printed before anything else.
"""
from __future__ import annotations

import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import mmm_lib as M
import mmm_week as W

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "V01", "data")
THRESHOLDS = (10.0, 15.0, 18.0, 50.0)      # V04 [00:04:43], [00:05:07]
FILL_H = (4, 24)


def run_arm(arm, log):
    m1 = M.load_m1(arm)
    raw1 = M.load_m1("A")
    m15 = M.load_m15(arm)
    roster = W.build_weeks(arm, m15)
    keep = set(roster["anchor_raw"].tolist())
    a1 = W.week_anchor(raw1.tm)
    sel = np.array([int(a) in keep for a in a1])
    M.assert_development(raw1.tm[sel], f"PT-032 universe / arm {arm}")
    tm, o, h, l, c = m1.tm[sel], m1.o[sel], m1.h[sel], m1.l[sel], m1.c[sel]
    anch = a1[sel]
    uniq, inv = np.unique(anch, return_inverse=True)
    n = len(uniq)
    rows = np.split(np.arange(len(tm)), np.cumsum(np.bincount(inv))[:-1])
    weeks = np.array([W.day2s(a // W.DAY) for a in uniq])

    log(f"\n{'='*74}\n--- ARM {arm} ---\n{'='*74}")
    for ln in W.census_lines(roster):
        log("  " + ln)

    # ---- §7 step 5 — N3 FIRST OF ALL ------------------------------------------
    log(f"\n  {'='*70}")
    log(f"  CO-PRIMARY BASELINE, RUN FIRST OF ALL (§7 step 5) — N3 week-anchor shift.")
    log(f"  'Gaps' computed at SHIFTED boundaries, most of which fall inside")
    log(f"  continuous trading and should therefore be NEAR ZERO.")
    log(f"  ⚠ A NON-ZERO RESULT HERE MEANS THE HARVEST IS WRONG AND NO OTHER NUMBER")
    log(f"    IN THIS TEST CAN BE TRUSTED (§5 row 5).")
    log(f"  {'='*70}")
    n3 = []
    for off in W.n3_week_shifts()[:200]:
        a_ = W.week_anchor(raw1.tm[sel] - int(off)) + int(off)
        b = np.where(np.r_[True, a_[1:] != a_[:-1]])[0]
        b = b[(b > 0) & (b < len(tm) - 1)]
        if not len(b):
            continue
        g = np.abs(o[b] - c[b - 1]) / M.PIP
        n3.append(float(np.median(g)))
    n3 = np.array(n3)
    log(f"    median |shifted-boundary change|: {M.dist_line(n3)}")
    verdict = "PASS — near zero, the harvest is sound" if np.median(n3) < 2.0 \
        else "FAIL — STOP, the harvest is wrong"
    log(f"    N3 HARVEST CHECK: {verdict}")
    if np.median(n3) >= 2.0:
        raise SystemExit("N3 returned non-zero shifted-boundary gaps — refusing to "
                         "report any other figure (`PT-032` §5 row 5).")

    # ---- the realised open and close of every week, from M1 timestamps --------
    w_open_tm = np.array([tm[r][0] for r in rows])
    w_close_tm = np.array([tm[r][-1] for r in rows])
    w_open_px = np.array([o[r][0] for r in rows])
    w_close_px = np.array([c[r][-1] for r in rows])
    anchor_arm = W.shift_to_arm(uniq, arm)
    lag = w_open_tm - anchor_arm
    late = lag > 0
    log(f"\n  REALISED BOUNDARY INSTANTS, READ FROM M1 TIMESTAMPS (§7 step 4 —")
    log(f"  'do not assume 17:00 for either'):")
    log(f"    weeks whose open is LATE: {int(late.sum())} of {n}"
        f"   lags (min): {sorted(set(int(x) for x in lag[late]))[:12]}")
    ends = np.array([W.WEEKDAY_NAMES[int(W._weekday(t))] for t in w_close_tm])
    log(f"    realised week-close weekday: "
        + ", ".join(f"{d}={int((ends==d).sum())}" for d in ("Thu", "Fri")))

    # ---- exclusions ------------------------------------------------------------
    log(f"\n  EXCLUSIONS, APPLIED AND COUNTED BY NAME:")
    log(f"    {weeks[0]}  §3a — the gap INTO it needs the close of 2013-01-04, which")
    log(f"                lies inside the corpus but OUTSIDE W-C'. Using it would")
    log(f"                silently widen the pre-registered window (`D-027`).")
    log(f"    {W.DATA_HOLE_WEEK}  §3a″ — THE FABRICATED GAP. ~22 hours of MISSING data")
    log(f"                sit between the 2014-05-30 close and the first bar seen at")
    log(f"                2014-06-02 15:01. Measuring it would record absent data as a")
    log(f"                weekend gap. EXCLUDED BY NAME.")
    log(f"    {W.TRUNCATED_FINAL_WEEK}  §3a — the gap INTO it is fully determined by data")
    log(f"                before the boundary and is RETAINED, even though the week")
    log(f"                itself is truncated.")
    ok = np.array([(i > 0) and (weeks[i] != W.DATA_HOLE_WEEK) for i in range(n)])
    gap = np.where(ok, (w_open_px - np.r_[np.nan, w_close_px[:-1]]) / M.PIP, np.nan)
    closure_h = np.where(ok, (w_open_tm - np.r_[0, w_close_tm[:-1]]) / 60.0, np.nan)
    G = gap[ok]
    log(f"  WEEKEND GAPS USED: {len(G)}   (§3a‴ pre-registered: 180)")

    # ---- Measure 1 -------------------------------------------------------------
    A = np.abs(G)
    log(f"\n  MEASURE 1 — distribution of the ABSOLUTE weekend gap, in pips.")
    log(f"  ⚠ BID-TO-BID, NO SPREAD -> A LOWER BOUND on execution risk (§0b).")
    log(f"    median {np.median(A):6.2f}   90th {np.percentile(A,90):6.2f}   "
        f"99th {np.percentile(A,99):6.2f}   max {A.max():6.2f}")
    log(f"    §3a: the 99th percentile at n = {len(A)} is an order statistic over ~2")
    log(f"    observations. THE TOP FIVE, ORDERED, reported beside it:")
    top = np.argsort(-A)[:5]
    wl = weeks[ok]
    ch = closure_h[ok]
    for i in top:
        flag = "  <<< EXTENDED CLOSURE >= 72 h" if ch[i] >= 72 else ""
        log(f"      into {wl[i]}  {G[i]:+8.2f} pips   closure {ch[i]:6.1f} h{flag}")

    # ---- Measure 2 -------------------------------------------------------------
    log(f"\n  MEASURE 2 — share of weekends whose gap exceeds the instructor's own")
    log(f"  stop and target numbers (V04 [00:04:43], [00:05:07]). Distances, so they")
    log(f"  travel across vendors:")
    m2 = {}
    for t in THRESHOLDS:
        k = int((A > t).sum())
        m2[t] = k
        sub = ("  <<< subset < 30: any statement ABOUT these weekends is "
               "descriptive only") if k < 30 else ""
        log(f"    > {t:4.0f} pips : {M.fmt_rate(k, len(A))}{sub}")

    # ---- Measure 3 — gap fill --------------------------------------------------
    log(f"\n  MEASURE 3 — GAP FILL: does price return to the previous week's close?")
    fill_t = np.full(len(G), np.nan)
    gi = np.where(ok)[0]
    for j, w in enumerate(gi):
        prev_close = c[rows[w - 1]][-1]
        r = rows[w]
        if G[j] > 0:
            hit = np.where(l[r] <= prev_close)[0]
        elif G[j] < 0:
            hit = np.where(h[r] >= prev_close)[0]
        else:
            fill_t[j] = 0.0
            continue
        if len(hit):
            fill_t[j] = (tm[r][hit[0]] - w_open_tm[w]) / 60.0
    for hh in FILL_H:
        k = int((fill_t <= hh).sum())
        log(f"    filled within {hh:2d} h : {M.fmt_rate(k, len(G))}")
    k = int(np.isfinite(fill_t).sum())
    log(f"    filled by the week's end: {M.fmt_rate(k, len(G))}")
    log(f"    median time to fill (filled only): {np.nanmedian(fill_t):.2f} h")

    # ---- Measure 4 — RELABELLED (§0c) ------------------------------------------
    log(f"\n  MEASURE 4 — ⚠ RELABELLED PER §0c. On this corpus there is NO daily break,")
    log(f"  so these are NOT gaps: they are CONTINUOUS-TRADING RETURNS across the 17:00")
    log(f"  instant on Mon-Thu. Comparing a discontinuous weekend jump against a")
    log(f"  continuous weekday return is a FLOOR, not an apples-to-apples null.")
    m4, m4_excl = [], []
    for w in range(n):
        if weeks[w] == W.DATA_HOLE_WEEK:          # §3a‴ — its four instants excluded
            continue
        r = rows[w]
        t, oo, cc = tm[r], o[r], c[r]
        for d in range(4):                        # Mon..Thu
            inst = w_open_tm[w] - (w_open_tm[w] % M.DAY) + (d + 1) * M.DAY + 17 * 60
            after = np.where(t >= inst)[0]
            before = np.where(t < inst)[0]
            if not len(after) or not len(before):
                continue
            if (t[after[0]] - inst) > 15 or (inst - t[before[-1]]) > 15:
                m4_excl.append(f"{weeks[w]}+{d+1}")
                continue
            m4.append(abs(oo[after[0]] - cc[before[-1]]) / M.PIP)
    m4 = np.array(m4)
    log(f"    n = {len(m4)}   (§3a‴ expected ~720, floor ~714;"
        f" {len(m4_excl)} instants excluded for not being bracketed within 15 min)")
    log(f"    median {np.median(m4):5.2f}   90th {np.percentile(m4,90):5.2f}   "
        f"99th {np.percentile(m4,99):5.2f}   max {m4.max():6.2f}")
    log(f"    WEEKEND median {np.median(A):.2f} vs WEEKDAY-17:00 median "
        f"{np.median(m4):.2f}  ->  ratio {np.median(A)/np.median(m4):.1f}x")
    log(f"    share of weekday instants over 18 pips: "
        f"{M.fmt_rate(int((m4 > 18).sum()), len(m4))}")

    # ---- QA C6's three real intra-week gaps, descriptive only ------------------
    log(f"\n  §0c — QA `C6`'s THREE real intra-week gaps >= 30 min in 3.5 years")
    log(f"  (4h43m total). THREE OBSERVATIONS IS FAR BELOW ANY INFERENTIAL FLOOR;")
    log(f"  listed for completeness, DESCRIPTIVE ONLY, and never compared:")
    for s in ("2015-01-01 13:33", "2015-08-21 13:16", "2013-04-11 19:11"):
        log(f"      {s}  (see QA_REPORT.txt C6)")

    # ---- the four holiday re-open moves, reported separately -------------------
    log(f"\n  §3a′.1 — THE FOUR MID-WEEK HOLIDAY RE-OPENS. `C7` counts these as week")
    log(f"  opens; they are NOT weekend gaps and are NEVER merged into Measure 1.")
    log(f"  Reported separately and by name, as a distinct quantity:")
    for d in W.HOLIDAY_REOPENS:
        t0 = W.dt2m(d)
        j = np.where((tm >= t0) & (tm < t0 + M.DAY))[0]
        k = np.where(tm < t0)[0]
        if len(j) and len(k):
            log(f"      re-open {d}: {abs(o[j[0]] - c[k[-1]])/M.PIP:6.2f} pips "
                f"across a {(tm[j[0]] - tm[k[-1]])/60:5.1f} h closure")

    # ---- the two extended closures --------------------------------------------
    ext = np.where(ch >= 72)[0]
    log(f"\n  §3a‴ — EXTENDED CLOSURES >= 72 h, RETAINED and flagged with their")
    log(f"  realised duration. 'A 75-hour gap and a 48-hour gap are not the same")
    log(f"  event and a distribution that silently mixes them is misleading.'")
    for i in ext:
        log(f"      into {wl[i]}: {G[i]:+7.2f} pips across {ch[i]:.1f} h")
    log(f"    ordinary weekends: median closure {np.median(ch[ch < 72]):.1f} h")

    # ---- Measure 5 --------------------------------------------------------------
    log(f"\n  MEASURE 5 — DIRECTIONAL: is the gap's sign related to the PRIOR FRIDAY's")
    log(f"  direction? ('the dealer squares his books' predicts a relationship; NO")
    log(f"  relationship is the null.) §3a: the four cell COUNTS are reported.")
    prior = np.full(len(G), 0)
    for j, w in enumerate(gi):
        r = rows[w - 1]
        lastday = tm[r] >= (tm[r][-1] - (tm[r][-1] % M.DAY))
        prior[j] = np.sign(c[r][lastday][-1] - o[r][lastday][0])
    cells = {}
    for pn, pm in (("prior UP  ", prior > 0), ("prior DOWN", prior < 0)):
        for gn, gm in (("gap UP  ", G > 0), ("gap DOWN", G < 0)):
            cells[f"{pn}/{gn}"] = (int((pm & gm).sum()), int(pm.sum()))
    for k_, (a_, b_) in cells.items():
        log(f"    {k_}: {M.fmt_rate(a_, b_)}")
    same = int(((prior > 0) & (G > 0)).sum() + ((prior < 0) & (G < 0)).sum())
    tot = int(((prior != 0) & (G != 0)).sum())
    log(f"    gap CONTINUES the prior Friday's direction: {M.fmt_rate(same, tot)}")

    return dict(arm=arm, n_gaps=len(G),
                median=float(np.median(A)), p90=float(np.percentile(A, 90)),
                p99=float(np.percentile(A, 99)), max=float(A.max()),
                top5=[[wl[i], float(G[i]), float(ch[i])] for i in top],
                thresholds={str(k): v for k, v in m2.items()},
                fill={str(hh): int((fill_t <= hh).sum()) for hh in FILL_H},
                fill_any=int(np.isfinite(fill_t).sum()),
                fill_median_h=float(np.nanmedian(fill_t)),
                m4_n=len(m4), m4_median=float(np.median(m4)),
                m4_p99=float(np.percentile(m4, 99)), m4_max=float(m4.max()),
                m4_over18=int((m4 > 18).sum()), m4_excluded=len(m4_excl),
                n3_median=float(np.median(n3)),
                extended=[[wl[i], float(G[i]), float(ch[i])] for i in ext],
                late_opens=int(late.sum()),
                cells={k_: list(v) for k_, v in cells.items()},
                continues=[same, tot])


def main():
    lines = []

    def log(s=""):
        print(s)
        lines.append(s)

    log(M.header("PT-032", "The weekend gap, and the one mechanical rationale in V01",
                 "window   : W-C' 2013-01-06 -> 2016-06-30. Re-issue of PT-019.\n"
                 "⚠ EVERY GAP FIGURE IS BID-TO-BID WITH NO SPREAD AND IS A LOWER\n"
                 "  BOUND on execution risk (§0b). The error runs IN FAVOUR of the\n"
                 "  instructor's rationale, which is why it is declared first.\n"
                 "⚠ Measure 4 is NOT a gap comparison on this corpus (§0c)."))
    out = {}
    for arm in ("A", "B"):
        out[arm] = run_arm(arm, log)
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "pt032_report.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    with open(os.path.join(OUT, "pt032_results.json"), "w") as fh:
        json.dump(out, fh, indent=2, default=float)


if __name__ == "__main__":
    main()
