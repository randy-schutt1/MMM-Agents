#!/usr/bin/env python3
"""PT-027 — does the first move out of the week's opening range reverse? (re-issue of PT-009)

WHAT IS BEING TESTED, AND WHAT IS NOT
-------------------------------------
`PT-027` §6: this tests ONE OPERATIONALISATION of "the first move of the week" — the
first breach of the week's opening eight-hour range. `A-006` (what "the box" refers to
in V01 `[00:43:07]`) REMAINS OPEN and this test does not close it. Nothing here
identifies a "false move" or a "trap move" (`A-002`), which are undefined as patterns.

THE BLOCK COMES FROM `PT-026`, NOT FROM `PT-008`
------------------------------------------------
§7 step 2: "Run `PT-026` first. This test consumes its block definition, and running
them in the other order would mean tuning the block against this test's outcome.
`PT-008` is superseded and must not be run to supply the block." The block is imported
from `mmm_block`, the same code `run_pt026.py` uses, so the two cannot drift.

  headline trigger    first 15m CLOSE beyond the 8-hour clock block, either side
  sensitivity arm     the same trigger on the two-4h-bars block (§0b)
  the 12-hour block   NOT carried here — §0b records the omission as a CHOICE:
                      "adding a third trigger arm would multiply this test's cells
                      without answering its question."

OUTCOME 3 IS AN UPPER BOUND AND IS LABELLED ONE EVERYWHERE (§0c)
-----------------------------------------------------------------
Bid-only bars, no spread, no slippage. The prohibited trade is priced at 18/50 —
V04's own numbers, not fitted — and every figure is an upper bound on what taking it
would have returned.
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
from mmm_wtrade import resolve_week

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "V01", "data")


def universe(arm):
    m15, raw = M.load_m15(arm), M.load_m15("A")
    m1, raw1 = M.load_m1(arm), M.load_m1("A")
    roster = W.build_weeks(arm, m15)
    use = W.usable(roster, drop_truncated=True)
    keep = set(use["anchor_raw"].tolist())
    a15 = W.week_anchor(raw.tm)
    a1 = W.week_anchor(raw1.tm)
    s15 = np.array([int(a) in keep for a in a15])
    s1 = np.array([int(a) in keep for a in a1])
    M.assert_development(raw.tm[s15], f"PT-027 universe / arm {arm}")
    return (M.Bars(m15.tm[s15], m15.o[s15], m15.h[s15], m15.l[s15], m15.c[s15], arm, 15),
            M.Bars(m1.tm[s1], m1.o[s1], m1.h[s1], m1.l[s1], m1.c[s1], arm, 1),
            a15[s15], a1[s1], roster, use)


def find_breaches(m15, inv, n, w_open, block_end_off, hi, lo):
    """Discrete BREACH EVENTS — a 15m close beyond an edge that CROSSES to that side.

    A BREACH IS A CROSSING, NOT A STATE. The first implementation counted every 15m
    close that happened to sit outside the block, which made "second and later
    breaches" 66,443 events across 180 weeks — 369 per week. That is a count of bars
    spent outside the block, not a count of breaches, and it would have made the third
    baseline a different quantity from the headline trigger it is meant to contrast
    with.

    `PT-027` does not define the word for the later-breach control, so the definition
    is stated here and applied identically to the first breach and to every later one:
    a breach occurs at a close whose side (above / inside / below the block) DIFFERS
    from the previous close's side and is not "inside". Re-crossing the same edge
    after returning inside is a new breach; running from above to below without a
    close inside is also a new breach.

    The FIRST breach is unaffected by this choice — the first close beyond an edge is
    a crossing under either reading — so the headline trigger is identical and only
    the third baseline changes.
    """
    rel = m15.tm - w_open[inv]
    after = rel >= block_end_off[inv]
    side_now = np.where(m15.c > hi[inv], 1, np.where(m15.c < lo[inv], -1, 0))
    side_now = np.where(after, side_now, 0)
    # previous close's side WITHIN the same week; week starts count as "inside"
    prev = np.roll(side_now, 1)
    prev[0] = 0
    same_week = np.r_[False, inv[1:] == inv[:-1]]
    prev = np.where(same_week, prev, 0)

    is_breach = (side_now != 0) & (side_now != prev)
    idx = np.where(is_breach)[0]
    order = np.lexsort((m15.tm[idx], inv[idx]))
    idx = idx[order]
    wk = inv[idx]
    first_of = np.r_[True, wk[1:] != wk[:-1]]
    ordinal = np.arange(len(wk)) - np.maximum.accumulate(
        np.where(first_of, np.arange(len(wk)), 0))
    return idx, wk, ordinal, side_now[idx]


def run_arm(arm, log):
    m15, m1, a15, a1, roster, use = universe(arm)
    uniq, inv, n = week_index(a15)
    inv1 = np.searchsorted(uniq, a1)

    log(f"\n{'='*74}\n--- ARM {arm} ---\n{'='*74}")
    for ln in W.census_lines(roster):
        log("  " + ln)
    thu = use[use["ends_weekday"] == "Thu"]["week"].tolist()
    log(f"  WEEKS USED: {len(use)}   M15 {len(m15.tm)}   M1 {len(m1.tm)}")
    log(f"  §3a: 2014-06-01 EXCLUDED by name — no observable week open, so no block")
    log(f"       and no trigger. Six Dec/Jan closure weeks INCLUDED, reported")
    log(f"       separately. {thu} end THURSDAY — Outcome 1's reversal window and")
    log(f"       Outcome 3's holding window are SHORTER; realised times reported.")

    res = {"arm": arm}
    blk8 = block_measures(m15.tm, m15.h, m15.l, m15.c, inv, n, 0, 480)
    tb = two_bar_block_end(blk8["w_open"])
    blk2 = block_measures(m15.tm, m15.h, m15.l, m15.c, inv, n, 0, tb)

    for label, blk, end_off in (("HEADLINE — 8-hour clock block", blk8,
                                 np.full(n, 480, dtype="int64")),
                                ("SENSITIVITY — two-4h-bars block (§0b)", blk2, tb)):
        log(f"\n  {'='*70}\n  {label}\n  {'='*70}")
        idx, wk, ordn, side = find_breaches(m15, inv, n, blk["w_open"], end_off,
                                            blk["block_hi"], blk["block_lo"])
        first = ordn == 0
        fi, fw, fs = idx[first], wk[first], side[first]
        log(f"  weeks yielding a first-breach trigger: {len(fi)} of {n}"
            f"   ({n - len(fi)} weeks never closed beyond either edge)")

        w_close = blk["w_close"]
        hi, lo = blk["block_hi"], blk["block_lo"]

        # ---- Outcome 1 — reversal through the OPPOSITE edge before the week close
        rev = np.zeros(len(fi), dtype=bool)
        t_rev = np.full(len(fi), np.nan)
        for k, (i, w, s) in enumerate(zip(fi, fw, fs)):
            m = (inv == w) & (m15.tm > m15.tm[i])
            if not m.any():
                continue
            if s == 1:
                j = np.where(m & (m15.l < lo[w]))[0]
            else:
                j = np.where(m & (m15.h > hi[w]))[0]
            if len(j):
                rev[k] = True
                t_rev[k] = (m15.tm[j[0]] - m15.tm[i]) / 60.0
        log(f"\n  OUTCOME 1 — reversal back through the OPPOSITE edge before the "
            f"week's close:")
        log(f"    {M.fmt_rate(int(rev.sum()), len(rev))}")
        log(f"    hours to the reversal, when it happens: median "
            f"{np.nanmedian(t_rev):.1f}, IQR [{np.nanpercentile(t_rev, 25):.1f}, "
            f"{np.nanpercentile(t_rev, 75):.1f}]")

        # ---- Outcome 2 — trap geometry
        ext_side = blk["ext_side"]
        on_breach = ext_side[fw] == fs
        log(f"\n  OUTCOME 2 — trap geometry:")
        log(f"    week's extreme on the BREACH side: "
            f"{M.fmt_rate(int(on_breach.sum()), len(on_breach))}")
        # X reported as a DISTRIBUTION, not pre-set
        t_ext = np.full(len(fi), np.nan)
        for k, (i, w, s) in enumerate(zip(fi, fw, fs)):
            m = np.where(inv == w)[0]
            j = m[np.argmax(m15.h[m])] if ext_side[w] == 1 else m[np.argmin(m15.l[m])]
            t_ext[k] = (m15.tm[j] - m15.tm[i]) / 60.0
        log(f"    hours from trigger to the week's extreme (X as a DISTRIBUTION, "
            f"not a pre-set threshold):")
        log(f"      median {np.nanmedian(t_ext):.1f}, "
            f"IQR [{np.nanpercentile(t_ext, 25):.1f}, {np.nanpercentile(t_ext, 75):.1f}],"
            f" 5-95% [{np.nanpercentile(t_ext, 5):.1f}, {np.nanpercentile(t_ext, 95):.1f}]")
        both_cell = int((rev & on_breach).sum())
        lbl = "  <<< SAMPLE INSUFFICIENT FOR INFERENCE — descriptive only" \
            if both_cell < 30 else ""
        log(f"    §3a conditional cell (reversal AND extreme on the breach side): "
            f"{both_cell}{lbl}")

        # ---- Outcome 3 — the prohibition priced (UPPER BOUND)
        oc, pnl, hrs, tie = [], [], [], []
        for w in range(n):
            sel = fw == w
            if not sel.any():
                continue
            mm = inv1 == w
            o, p, hh, tt = resolve_week(m1.tm[mm], m1.h[mm], m1.l[mm], m1.c[mm],
                                        m15.tm[fi[sel]], m15.c[fi[sel]], w_close[w])
            d = np.where(fs[sel] == 1, 0, 1)
            oc.append(o[np.arange(len(d)), d]); pnl.append(p[np.arange(len(d)), d])
            hrs.append(hh[np.arange(len(d)), d]); tie.append(tt[np.arange(len(d)), d])
        oc = np.concatenate(oc); pnl = np.concatenate(pnl)
        hrs = np.concatenate(hrs); tie = np.concatenate(tie)
        resolved = oc != 0
        log(f"\n  OUTCOME 3 — THE PROHIBITION PRICED. Position taken IN THE BREACH")
        log(f"  DIRECTION at the trigger, stop 18 / target 50 (V04's own numbers).")
        log(f"  ⚠ BID-ONLY, NO SPREAD, NO SLIPPAGE -> AN UPPER BOUND (§0c).")
        log(f"    target hit : {M.fmt_rate(int((oc == 1).sum()), int(resolved.sum()))}")
        log(f"    stopped    : {M.fmt_rate(int((oc == -1).sum()), int(resolved.sum()))}")
        log(f"    unresolved at the week close: {int((oc == 0).sum())}")
        log(f"    expectancy : {np.nanmean(pnl):+.2f} pips/trade "
            f"(median {np.nanmedian(pnl):+.2f}), n = {int(np.isfinite(pnl).sum())}")
        log(f"    C-4 same-bar stop/target ties (resolved STOP FIRST, adverse): "
            f"{int(tie.sum())}")

        # ---- THIRD BASELINE — second and later breaches
        later = ordn >= 1
        li, lw, ls = idx[later], wk[later], side[later]
        log(f"\n  THIRD BASELINE — SECOND AND LATER breaches of the same block in the")
        log(f"  same week (the course's own contrast: V01 forbids the FIRST move,")
        log(f"  V02-V03 endorse the RETURN):")
        nlw = len(np.unique(lw))
        cav = "  <<< SAMPLE INSUFFICIENT FOR INFERENCE — descriptive only" \
            if nlw < 30 else ""
        log(f"    weeks producing a second-or-later breach: {nlw}{cav}")
        log(f"    total later-breach entries: {len(li)}")
        if len(li):
            oc2, pnl2 = [], []
            for w in np.unique(lw):
                sel = lw == w
                mm = inv1 == w
                o, p, hh, tt = resolve_week(m1.tm[mm], m1.h[mm], m1.l[mm], m1.c[mm],
                                            m15.tm[li[sel]], m15.c[li[sel]], w_close[w])
                d = np.where(ls[sel] == 1, 0, 1)
                oc2.append(o[np.arange(len(d)), d]); pnl2.append(p[np.arange(len(d)), d])
            oc2 = np.concatenate(oc2); pnl2 = np.concatenate(pnl2)
            r2 = oc2 != 0
            log(f"    target hit : {M.fmt_rate(int((oc2 == 1).sum()), int(r2.sum()))}")
            log(f"    expectancy : {np.nanmean(pnl2):+.2f} pips/trade "
                f"(n = {int(np.isfinite(pnl2).sum())})")

        # ---- PRIMARY BASELINE — N1 matched random entry
        log(f"\n  PRIMARY BASELINE — N1 matched random entry, same weeks, same")
        log(f"  eligible hours, direction matched to the breach, SAME 18/50 stop and")
        log(f"  target, {M.ITERATIONS} iterations, seed {M.SEED}:")
        pool_oc, pool_pnl, pool_w = [], [], []
        for w in range(n):
            mm = inv1 == w
            e = np.where((inv == w) & (m15.tm >= blk["w_open"][w] + end_off[w])
                         & (m15.tm < w_close[w]))[0]
            if not mm.any() or len(e) == 0:
                continue
            o, p, hh, tt = resolve_week(m1.tm[mm], m1.h[mm], m1.l[mm], m1.c[mm],
                                        m15.tm[e], m15.c[e], w_close[w])
            pool_oc.append(o); pool_pnl.append(p)
            pool_w.append(np.full(len(e), w))
        pool_oc = np.concatenate(pool_oc); pool_pnl = np.concatenate(pool_pnl)
        rng = np.random.default_rng(M.SEED)
        dirs = np.where(fs == 1, 0, 1)
        n1_tgt = np.full(M.ITERATIONS, np.nan)
        n1_exp = np.full(M.ITERATIONS, np.nan)
        P = len(pool_oc)
        for it in range(M.ITERATIONS):
            pick = rng.integers(0, P, size=len(dirs))
            o = pool_oc[pick, dirs]; p = pool_pnl[pick, dirs]
            r = o != 0
            if r.any():
                n1_tgt[it] = float((o[r] == 1).mean())
            if np.isfinite(p).any():
                n1_exp[it] = float(np.nanmean(p))
        log(f"    pool: {P} eligible M15 entries across {n} weeks")
        log(f"    target-hit rate : {M.dist_line(n1_tgt)}")
        log(f"    expectancy      : {M.dist_line(n1_exp)}")
        obs_t = float((oc[resolved] == 1).mean())
        obs_e = float(np.nanmean(pnl))
        log(f"    OBSERVED target-hit {obs_t:.3f} -> N1 percentile "
            f"{M.percentile_of(obs_t, n1_tgt):.1f}")
        log(f"    OBSERVED expectancy {obs_e:+.2f} -> N1 percentile "
            f"{M.percentile_of(obs_e, n1_exp):.1f}")

        key = "headline" if "HEADLINE" in label else "two_bars"
        res[key] = dict(
            n_trigger=len(fi), n_weeks=n,
            reversal=int(rev.sum()), reversal_n=len(rev),
            t_rev_median=float(np.nanmedian(t_rev)),
            ext_on_breach=int(on_breach.sum()),
            t_ext_median=float(np.nanmedian(t_ext)),
            conditional_cell=both_cell,
            target_hit=int((oc == 1).sum()), stopped=int((oc == -1).sum()),
            unresolved=int((oc == 0).sum()), ties=int(tie.sum()),
            expectancy=obs_e, target_rate=obs_t,
            n1_target_pct=M.percentile_of(obs_t, n1_tgt),
            n1_exp_pct=M.percentile_of(obs_e, n1_exp),
            n1_target_median=float(np.nanmedian(n1_tgt)),
            n1_exp_median=float(np.nanmedian(n1_exp)),
            later_weeks=nlw, later_n=len(li),
        )
    res["thursday_weeks"] = thu
    return res


def main():
    lines = []

    def log(s=""):
        print(s)
        lines.append(s)

    log(M.header("PT-027",
                 "Does the first move out of the week's opening range reverse?",
                 "window   : W-C' 2013-01-06 -> 2016-06-30. Re-issue of PT-009.\n"
                 "block    : supplied by PT-026 (run first, per §7 step 2).\n"
                 "           PT-008 is superseded and was NOT run to supply it.\n"
                 "⚠ OUTCOME 3 IS AN UPPER BOUND — bid-only, no spread, no slippage."))
    out = {}
    for arm in ("A", "B"):
        out[arm] = run_arm(arm, log)
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "pt027_report.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    with open(os.path.join(OUT, "pt027_results.json"), "w") as fh:
        json.dump(out, fh, indent=2, default=float)


if __name__ == "__main__":
    main()
