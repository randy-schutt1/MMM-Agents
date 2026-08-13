#!/usr/bin/env python3
"""PT-026 — is the first-eight-hours range of the week cut? (re-issue of PT-008)

THE THREE BLOCK ARMS ARE ALL REPORTED, AND NONE IS ADOPTED
----------------------------------------------------------
`PT-026` §0c: the instructor's "first eight hours" and "two bars" are DIFFERENT SPANS
on this corpus, because the 17:00 week open no longer lands on a 4-hour bucket
boundary as FXCM's 16:00 did. `D-030` forbids picking one and calling it the
definition, so all three arms (8h clock, two-4h-bars, 12h) are measured and reported
every time. "Reporting only the block that worked is `E09`."

BASELINES (`PT-026` §4), all run before the week-open block's numbers are looked at
-----------------------------------------------------------------------------------
Primary  N3 week-anchor shift, 1,000 draws, seed 20260812
Second   the natural control -- 8-hour blocks at EVERY 4-hour offset through the
         120-hour week (30 offsets). The week-open block is RANKED among them rather
         than tested alone.
Third    block-width sweep at 4/8/12/24 h, so a "wider blocks get breached less"
         artifact cannot masquerade as a finding about the week's open. This also
         absorbs §0c: the two-bars arm's realised 6-7 h sits inside the sweep.
"""
from __future__ import annotations

import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import mmm_lib as M
import mmm_week as W
from mmm_block import block_measures, two_bar_block_end, week_index

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "V03", "data")
SWEEP_OFFSETS = [i * 4 * 60 for i in range(30)]          # 30 four-hour offsets
WIDTHS = (240, 480, 720, 1440)                            # 4, 8, 12, 24 hours
MATCHED_CAP = 24 * 60      # the matched outcome window for the de-confounded sweep


def universe(arm):
    """The 180 usable weeks' bars, and the week partition over them."""
    m15 = M.load_m15(arm)
    raw = M.load_m15("A")
    roster = W.build_weeks(arm, m15)
    use = W.usable(roster, drop_truncated=True)
    keep = set(use["anchor_raw"].tolist())
    anch = W.week_anchor(raw.tm)
    sel = np.array([int(a) in keep for a in anch])
    M.assert_development(raw.tm[sel], f"PT-026 universe / arm {arm}")
    return (m15.tm[sel], m15.h[sel], m15.l[sel], m15.c[sel], raw.tm[sel],
            anch[sel], roster, use)


def summarise(m, label, log, weeks=None):
    ok = m["measurable"]
    n = int(ok.sum())
    log(f"\n  {label}   (measurable weeks n = {n})")
    log(f"    realised block length: median {np.nanmedian(m['realised_block_h'][ok]):.2f} h"
        f"  min {np.nanmin(m['realised_block_h'][ok]):.2f}"
        f"  max {np.nanmax(m['realised_block_h'][ok]):.2f}")
    log("    M1 is it cut? — "
        f"above {M.fmt_rate(int(m['up'][ok].sum()), n)}")
    log(f"{'':18s}below {M.fmt_rate(int(m['dn'][ok].sum()), n)}")
    log(f"{'':18s}BOTH  {M.fmt_rate(int(m['both'][ok].sum()), n)}")
    log(f"{'':18s}NEITHER {M.fmt_rate(int(m['neither'][ok].sum()), n)}")
    t = m["t_first"][ok]
    log(f"    M2 when? — hours from block close to first breach: "
        f"median {np.nanmedian(t):.2f}, "
        f"IQR [{np.nanpercentile(t, 25):.2f}, {np.nanpercentile(t, 75):.2f}], "
        f"n = {int(np.isfinite(t).sum())}")
    eu, ed = m["exc_up"][ok], m["exc_dn"][ok]
    log(f"    M3 how far? — max excursion beyond the HIGH: "
        f"median {np.nanmedian(eu):.1f} pips (n = {int(np.isfinite(eu).sum())})")
    log(f"{'':18s}beyond the LOW : "
        f"median {np.nanmedian(ed):.1f} pips (n = {int(np.isfinite(ed).sum())})")
    fs = m["first_side"][ok]
    ag = m["agree"][ok]
    nb = int((fs != 0).sum())
    log(f"    M4 which first? — up first {int((fs==1).sum())}, "
        f"down first {int((fs==-1).sum())}, no breach {int((fs==0).sum())}")
    log(f"       week's extreme on the FIRST-BREACH side: {M.fmt_rate(int(ag.sum()), nb)}")
    return dict(n=n, up=int(m["up"][ok].sum()), dn=int(m["dn"][ok].sum()),
                both=int(m["both"][ok].sum()), neither=int(m["neither"][ok].sum()),
                t_median=float(np.nanmedian(t)),
                exc_up_median=float(np.nanmedian(eu)),
                exc_dn_median=float(np.nanmedian(ed)),
                agree=int(ag.sum()), n_breach=nb,
                block_h_median=float(np.nanmedian(m["realised_block_h"][ok])))


def run_arm(arm, log):
    tm, h, l, c, raw_tm, anch, roster, use = universe(arm)
    log(f"\n{'='*74}\n--- ARM {arm} ---\n{'='*74}")
    for ln in W.census_lines(roster):
        log("  " + ln)
    log(f"  WEEKS USED (§3d): {len(use)}   bar universe {len(tm)} M15 bars")
    log(f"  §3c: 2014-06-01 EXCLUDED by name (no observable week open, so no block).")
    log(f"       six Dec/Jan closure weeks INCLUDED, reported separately — all six")
    log(f"       open normally on Sunday, so all three blocks are intact in each.")
    thu = use[use["ends_weekday"] == "Thu"]["week"].tolist()
    log(f"       {thu} end on THURSDAY — Measures 2-4 censored earlier, realised")
    log(f"       censoring time reported below.")

    uniq, inv, n = week_index(anch)

    # ---------------- BASELINE 2: the 30-offset sweep, FIRST ----------------
    log(f"\n  SECOND BASELINE — the natural control: 8-hour blocks at every 4-hour")
    log(f"  offset through the 120-hour week ({len(SWEEP_OFFSETS)} offsets).")
    log(f"  The week-open block is RANKED among them, not tested alone.")
    sweep = []
    for off in SWEEP_OFFSETS:
        m = block_measures(tm, h, l, c, inv, n, start_off=off, block_min=480)
        ok = m["measurable"]
        sweep.append(dict(off_h=off / 60, n=int(ok.sum()),
                          both=float(m["both"][ok].mean()) if ok.any() else np.nan,
                          neither=float(m["neither"][ok].mean()) if ok.any() else np.nan,
                          t=float(np.nanmedian(m["t_first"][ok])) if ok.any() else np.nan))
    both_v = np.array([s["both"] for s in sweep])
    neither_v = np.array([s["neither"] for s in sweep])
    t_v = np.array([s["t"] for s in sweep])
    log(f"    'both edges cut' across the 30 offsets: "
        f"median {np.nanmedian(both_v):.3f}, range "
        f"[{np.nanmin(both_v):.3f}, {np.nanmax(both_v):.3f}]")
    log(f"    'neither edge cut'                    : "
        f"median {np.nanmedian(neither_v):.3f}, range "
        f"[{np.nanmin(neither_v):.3f}, {np.nanmax(neither_v):.3f}]")
    log(f"    median hours to first breach          : "
        f"median {np.nanmedian(t_v):.2f}, range "
        f"[{np.nanmin(t_v):.2f}, {np.nanmax(t_v):.2f}]")
    n_dropped = sum(1 for s in sweep if s["n"] == 0)
    log(f"    offsets yielding NO measurable week (block runs past the week close):"
        f" {n_dropped} of {len(SWEEP_OFFSETS)} — +112 h and +116 h")

    # ---- THE CONFOUND IN THE PRE-REGISTERED SWEEP, AND THE MATCHED BASIS -------
    # The sweep as pre-registered gives offset 0 an outcome window of ~112 h and
    # offset +108 h a window of ~4 h. Breach rate falls with offset for a purely
    # mechanical reason, so the week-open block would rank first however the market
    # behaved. This is the same class of defect the earlier batch found in PT-003
    # (`9eb2d0c`), and it is handled the same way: a MATCHED-BASIS sweep is added
    # ALONGSIDE the pre-registered one and both are reported. The pre-registered
    # sweep is NOT changed or discarded — `D-027` forbids that.
    log(f"\n  ⚠ STRUCTURAL CONFOUND IN THE PRE-REGISTERED SWEEP, and the matched basis")
    log(f"  added alongside it (the pre-registered sweep above is retained, not")
    log(f"  replaced). Every offset is re-measured with the SAME {MATCHED_CAP//60}-hour")
    log(f"  outcome window after its own block close:")
    msweep = []
    for off in SWEEP_OFFSETS:
        m = block_measures(tm, h, l, c, inv, n, off, 480,
                           outcome_cap_min=MATCHED_CAP)
        ok = m["measurable"]
        msweep.append(dict(off_h=off / 60, n=int(ok.sum()),
                           both=float(m["both"][ok].mean()) if ok.any() else np.nan,
                           t=float(np.nanmedian(m["t_first"][ok])) if ok.any() else np.nan))
    mboth = np.array([s["both"] for s in msweep])
    log(f"    'both edges cut' within {MATCHED_CAP//60} h, across the offsets: "
        f"median {np.nanmedian(mboth):.3f}, range "
        f"[{np.nanmin(mboth):.3f}, {np.nanmax(mboth):.3f}]")
    log(f"    offsets measurable on this basis: "
        f"{sum(1 for s in msweep if s['n'] > 0)} of {len(SWEEP_OFFSETS)}")

    # ---------------- BASELINE 3: the width sweep ----------------
    log(f"\n  THIRD BASELINE — block-width sweep at the WEEK OPEN (4/8/12/24 h), so a")
    log(f"  'wider blocks get breached less' artifact cannot masquerade as a finding:")
    width = {}
    for wmin in WIDTHS:
        m = block_measures(tm, h, l, c, inv, n, 0, wmin)
        ok = m["measurable"]
        width[wmin] = dict(n=int(ok.sum()), both=float(m["both"][ok].mean()),
                           neither=float(m["neither"][ok].mean()),
                           t=float(np.nanmedian(m["t_first"][ok])))
        log(f"    {wmin//60:2d} h block: both {width[wmin]['both']:.3f}  "
            f"neither {width[wmin]['neither']:.3f}  "
            f"median hours-to-breach {width[wmin]['t']:.2f}  (n = {width[wmin]['n']})")

    # ---------------- BASELINE 1: N3 ----------------
    log(f"\n  PRIMARY BASELINE — N3 week-anchor shift, {M.ITERATIONS} draws, "
        f"seed {M.SEED}:")
    lo_e, hi_e = raw_tm.min(), raw_tm.max()
    hole = W.dt2m(W.DATA_HOLE_WEEK)
    n3_both, n3_neither, n3_t = [], [], []
    for off in W.n3_week_shifts():
        a = W.week_anchor(raw_tm - int(off)) + int(off)
        u2, i2, n2_ = week_index(a)
        good = ((u2 >= lo_e) & (u2 + W.DAY * 5 <= hi_e)
                & ~((u2 < hole + W.DAY * 7) & (u2 + W.DAY * 5 > hole)))
        if not good.any():
            continue
        m = block_measures(tm, h, l, c, i2, n2_, 0, 480)
        ok = m["measurable"] & good
        if not ok.any():
            continue
        n3_both.append(float(m["both"][ok].mean()))
        n3_neither.append(float(m["neither"][ok].mean()))
        n3_t.append(float(np.nanmedian(m["t_first"][ok])))
    n3_both = np.array(n3_both); n3_neither = np.array(n3_neither)
    n3_t = np.array(n3_t)
    log(f"    'both edges cut'             : {M.dist_line(n3_both)}")
    log(f"    'neither edge cut'           : {M.dist_line(n3_neither)}")
    log(f"    median hours to first breach : {M.dist_line(n3_t)}")

    # ---------------- THE RULE ARM — read only now ----------------
    log(f"\n  {'='*70}\n  OBSERVED — the week-open block, read after all three baselines")
    log(f"  {'='*70}")
    res = {}
    m8 = block_measures(tm, h, l, c, inv, n, 0, 480)
    res["headline_8h"] = summarise(m8, "HEADLINE — 'the first eight hours', 8 h by "
                                       "clock from the realised week open", log)
    w_open = m8["w_open"]
    tb = two_bar_block_end(w_open)
    m2b = block_measures(tm, h, l, c, inv, n, 0, tb)
    res["two_bars"] = summarise(m2b, "SECOND ARM — 'the first two 4-hour bars', "
                                     "midnight-anchored (§0c)", log)
    m12 = block_measures(tm, h, l, c, inv, n, 0, 720)
    res["twelve_h"] = summarise(m12, "THIRD ARM — the 12-hour block, V03 [00:29:51]",
                                log)

    ok = m8["measurable"]
    m8_both = float(m8["both"][ok].mean())
    m8m = block_measures(tm, h, l, c, inv, n, 0, 480, outcome_cap_min=MATCHED_CAP)
    okm = m8m["measurable"]
    m8m_both = float(m8m["both"][okm].mean())
    res["matched"] = dict(both=m8m_both, n=int(okm.sum()),
                          rank=int((mboth > m8m_both).sum()) + 1,
                          n_offsets=int(np.isfinite(mboth).sum()),
                          sweep_median=float(np.nanmedian(mboth)))
    res["ranks"] = dict(
        both_rank=int((both_v > m8["both"][ok].mean()).sum()) + 1,
        neither_rank=int((neither_v < m8["neither"][ok].mean()).sum()) + 1,
        n_offsets=len(SWEEP_OFFSETS),
        n3_both_pct=M.percentile_of(float(m8["both"][ok].mean()), n3_both),
        n3_neither_pct=M.percentile_of(float(m8["neither"][ok].mean()), n3_neither),
        n3_t_pct=M.percentile_of(float(np.nanmedian(m8["t_first"][ok])), n3_t),
    )
    log(f"\n  THE WEEK-OPEN BLOCK RANKED AMONG THE 30 SWEEP OFFSETS (§4 arm 2):")
    log(f"    'both edges cut'  = {m8['both'][ok].mean():.3f}  -> rank "
        f"{res['ranks']['both_rank']} of {len(SWEEP_OFFSETS)} (1 = most cut)")
    log(f"    'neither cut'     = {m8['neither'][ok].mean():.3f} -> rank "
        f"{res['ranks']['neither_rank']} of {len(SWEEP_OFFSETS)} (1 = least often uncut)")
    log(f"  ON THE MATCHED BASIS (same {MATCHED_CAP//60} h outcome window for every offset):")
    log(f"    'both edges cut'  = {m8m_both:.3f} (n = {res['matched']['n']}) -> rank "
        f"{res['matched']['rank']} of {res['matched']['n_offsets']} measurable offsets,")
    log(f"    against a sweep median of {res['matched']['sweep_median']:.3f}.")
    log(f"    THIS is the comparison the pre-registered sweep cannot make, and it is")
    log(f"    reported beside it rather than instead of it.")
    log(f"  AGAINST N3 (§4 arm 1):")
    log(f"    'both edges cut'  percentile {res['ranks']['n3_both_pct']:.1f}")
    log(f"    'neither edge cut' percentile {res['ranks']['n3_neither_pct']:.1f}")
    log(f"    hours-to-breach   percentile {res['ranks']['n3_t_pct']:.1f}")

    # closure weeks reported separately (§3c)
    wk = np.array([W.day2s(a // W.DAY) for a in uniq])
    clo = np.isin(wk, W.CLOSURE_WEEKS)
    thu_m = np.isin(wk, thu)
    log(f"\n  §3c — the six Dec/Jan closure weeks, INCLUDED and reported separately")
    log(f"  (headline 8h arm):")
    log(f"    closure weeks   : both {M.fmt_rate(int(m8['both'][clo & ok].sum()), int((clo&ok).sum()))}")
    log(f"    all other weeks : both {M.fmt_rate(int(m8['both'][~clo & ok].sum()), int((~clo&ok).sum()))}")
    log(f"    the two THURSDAY-ending weeks, realised outcome window:")
    for wname, oh in zip(wk[thu_m], m8["outcome_h"][thu_m]):
        log(f"      {wname}: {oh:.2f} h after the block close "
            f"(a full week gives {np.nanmedian(m8['outcome_h'][ok]):.2f} h)")

    log("\n  PRE-REGISTERED SENSITIVITY APPENDIX — five largest-range weeks:")
    for r in W.largest_range_weeks(use).itertuples():
        log(f"    {r.week}  range {r.range_pips:7.1f} pips  ends {r.ends_weekday}")

    res["sweep"] = sweep
    res["matched_sweep"] = msweep
    res["width"] = {str(k): v for k, v in width.items()}
    res["n3"] = dict(both_median=float(np.median(n3_both)),
                     neither_median=float(np.median(n3_neither)),
                     t_median=float(np.median(n3_t)))
    res["thursday_weeks"] = thu
    res["arm"] = arm
    return res, m8


def main():
    lines = []

    def log(s=""):
        print(s)
        lines.append(s)

    log(M.header("PT-026", "Is the first-eight-hours range of the week cut?",
                 "window   : W-C' 2013-01-06 -> 2016-06-30. Re-issue of PT-008,\n"
                 "           which straddled the D-035 boundary and was never run.\n"
                 "blocks   : ALL THREE arms reported (8h clock / two 4h bars / 12h).\n"
                 "           `D-030` forbids adopting one as THE definition."))
    out = {}
    for arm in ("A", "B"):
        out[arm], _ = run_arm(arm, log)
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "pt026_report.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    with open(os.path.join(OUT, "pt026_results.json"), "w") as fh:
        json.dump(out, fh, indent=2, default=float)


if __name__ == "__main__":
    main()
