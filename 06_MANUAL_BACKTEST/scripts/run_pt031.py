#!/usr/bin/env python3
"""PT-031 — are Sunday and Monday the week's accumulation phase? (re-issue of PT-013)

§0c — "SUNDAY + MONDAY" IS 31 HOURS, NOT TWO DAYS, AND THAT DECIDES THE HEADLINE
--------------------------------------------------------------------------------
The trading week is Sunday 17:00 -> Friday 17:00 = 120 h, so the spans compared are
31 / 7 / 48 / 48 / 48 / 48 / 41 hours. "A raw range comparison is rigged against Arm 1
and Arm 2 by arithmetic alone. A 31-hour span contains less range than a 48-hour span
for reasons that have nothing to do with market makers."

So: BOTH forms are always reported, and THE LENGTH-NORMALISED ONE GOVERNS THE VERDICT
(§0c.1, §5 row 5). Under Arm B the week opens at local 18:00 during US DST, so Sunday
is 6 h and Arm 1 is 30 h -- span lengths are computed PER WEEK and PER ARM from
realised bars, never once for the batch (§0c.2).

§0c.3 — THU+FRI HAS NO "REMAINING WEEK"
----------------------------------------
Metric 2 (containment of the remaining week) and Metric 4 (time to first breach after
the span) are UNDEFINED for it. They are reported as `NOT APPLICABLE`, never as zero
and never silently dropped: "a zero would read as 'perfectly contained' and invert the
meaning."

§0b — WHAT THIS TEST DOES NOT RESOLVE
--------------------------------------
"Accumulation" is NOT defined by the course (`V02_SOURCE_NOTES.md` §3 — given as an
answer, never expanded). This test measures a NAMED PROXY: range, containment and
boundary relevance. That block is inherited unchanged and nothing here closes it.
"""
from __future__ import annotations

import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import mmm_lib as M
import mmm_week as W
from mmm_block import week_index

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "V02", "data")

SUN, MON, TUE, WED, THU, FRI = 6, 0, 1, 2, 3, 4          # Mon=0 ... Sun=6

SPANS = [
    ("Sun+Mon  (ARM 1)", (SUN, MON)),
    ("Sun      (ARM 2)", (SUN,)),
    ("Mon+Tue  (ctrl) ", (MON, TUE)),
    ("Tue+Wed  (ctrl) ", (TUE, WED)),
    ("Wed+Thu  (ctrl) ", (WED, THU)),
    ("Thu+Fri  (ctrl) ", (THU, FRI)),
]
RANK_SET = ["Sun+Mon  (ARM 1)", "Mon+Tue  (ctrl) ", "Tue+Wed  (ctrl) ",
            "Wed+Thu  (ctrl) ", "Thu+Fri  (ctrl) "]
NO_REMAINDER = "Thu+Fri  (ctrl) "        # §0c.3


def wd(tm):
    return (np.floor_divide(np.asarray(tm, dtype="int64"), M.DAY) + 3) % 7


def run_arm(arm, log):
    m15 = M.load_m15(arm)
    raw = M.load_m15("A")
    roster = W.build_weeks(arm, m15)
    keep_all = set(roster["anchor_raw"].tolist())
    anch = W.week_anchor(raw.tm)
    sel = np.array([int(a) in keep_all for a in anch])
    M.assert_development(raw.tm[sel], f"PT-031 universe / arm {arm}")
    tm, h, l, c, o = (m15.tm[sel], m15.h[sel], m15.l[sel], m15.c[sel], m15.o[sel])
    uniq, inv, n = week_index(anch[sel])
    rows = np.split(np.arange(len(tm)), np.cumsum(np.bincount(inv))[:-1])
    weeks = np.array([W.day2s(a // W.DAY) for a in uniq])
    dow = wd(tm)

    log(f"\n{'='*74}\n--- ARM {arm} ---\n{'='*74}")
    for ln in W.census_lines(roster):
        log("  " + ln)
    log(f"\n  §3a — THE FEED PRINTS SUNDAY BARS, so `PT-013` §3a's conditional resolves")
    log(f"  IN FAVOUR OF RUNNING ARM 2, and arm 2 is NOT redefined as 'Monday's first")
    log(f"  eight hours' — that substitution would be `D-030`'s exact prohibition.")

    excl = {W.DATA_HOLE_WEEK: "§3b″ — DATA DEFECT, no Sunday session exists, so arms "
                              "1, 2 and 3 have no span to measure",
            W.TRUNCATED_FINAL_WEEK: "§3b — truncated by the DEVELOPMENT boundary, "
                                    "no Friday and no remaining week"}
    base = np.array([weeks[i] not in excl for i in range(n)])
    arm3_ok = base.copy()
    arm3_ok[0] = False        # §3b: its Friday (2013-01-04) is outside W-C'
    log(f"\n  EXCLUSIONS, APPLIED AND COUNTED BY NAME:")
    for k, v in excl.items():
        log(f"    {k}  {v}")
    log(f"    {weeks[0]}  §3b — ARM 3 ONLY: its Friday is 2013-01-04, inside the")
    log(f"                corpus but OUTSIDE W-C'. Using it would silently widen the")
    log(f"                pre-registered window, which `D-027` forbids.")
    log(f"  n: arms 1 and 2 = {int(base.sum())}   arm 3 = {int(arm3_ok.sum())}"
        f"   (§3c pre-registered: 180 / 180 / 179)")

    # ---------- per-week, per-span metrics ----------
    res = {name: dict(rng=[], hrs=[], norm=[], sqrtn=[], share=[], contain=[],
                      relev=[], dist=[], breach_h=[], week=[]) for name, _ in SPANS}
    res["Fri+Sun+Mon (ARM 3)"] = dict(rng=[], hrs=[], norm=[], sqrtn=[], share=[],
                                      contain=[], relev=[], dist=[], breach_h=[],
                                      week=[])

    for w in range(n):
        if not base[w]:
            continue
        idx = rows[w]
        wk_hi, wk_lo = h[idx].max(), l[idx].min()
        wk_rng = (wk_hi - wk_lo) / M.PIP
        d = dow[idx]

        span_defs = list(SPANS)
        extra = None
        if arm3_ok[w]:
            pidx = rows[w - 1]
            pfri = pidx[wd(tm[pidx]) == FRI]
            extra = np.concatenate([pfri, idx[np.isin(d, (SUN, MON))]])

        for name, days in span_defs + ([("Fri+Sun+Mon (ARM 3)", None)] if extra is not None else []):
            si = extra if days is None else idx[np.isin(d, days)]
            if len(si) == 0:
                continue
            s_hi, s_lo = h[si].max(), l[si].min()
            rng = (s_hi - s_lo) / M.PIP
            hrs = len(si) * 0.25
            R = res[name]
            R["week"].append(weeks[w]); R["rng"].append(rng); R["hrs"].append(hrs)
            R["norm"].append(rng / hrs if hrs else np.nan)
            # A THIRD form, added alongside the two pre-registered ones and NOT
            # replacing them. Range grows as ~sqrt(T) for a random-walk path, not
            # linearly, so BOTH pre-registered forms are biased and in OPPOSITE
            # directions: raw range favours the LONGER span, pips-per-hour
            # over-corrects and favours the SHORTER one. sqrt-time normalisation is
            # the neutral form between them. Disclosed in the observation; the
            # pre-registered normalised form still governs the verdict per 0c.1.
            R["sqrtn"].append(rng / np.sqrt(hrs) if hrs else np.nan)
            R["share"].append(rng / wk_rng if wk_rng else np.nan)

            # remainder of the week AFTER the span's last bar
            end = tm[si].max()
            rem = idx[tm[idx] > end]
            if name == NO_REMAINDER or len(rem) == 0:
                # §0c.3 — UNDEFINED, never zero
                R["contain"].append(np.nan); R["breach_h"].append(np.nan)
            else:
                inside = (h[rem] <= s_hi) & (l[rem] >= s_lo)
                R["contain"].append(float(inside.mean()))
                br = np.where((h[rem] > s_hi) | (l[rem] < s_lo))[0]
                R["breach_h"].append((tm[rem][br[0]] - end) / 60.0 if len(br) else np.nan)
            beyond = (wk_hi > s_hi) or (wk_lo < s_lo)
            R["relev"].append(bool(beyond))
            R["dist"].append(max((wk_hi - s_hi), (s_lo - wk_lo)) / M.PIP)

    for k in res:
        for f in res[k]:
            res[k][f] = np.array(res[k][f])

    # ---------- BASELINE: the four other spans, computed BEFORE Sun+Mon is read ----
    log(f"\n  PRIMARY BASELINE (§4 arm 1) — the four OTHER two-day spans, computed")
    log(f"  before Sun+Mon's own numbers are looked at (§7 step 6). Ranking is done on")
    log(f"  the LENGTH-NORMALISED metric, because the spans are 31/48/48/48/41 hours.")
    log(f"\n  METRIC 1 — RANGE. BOTH FORMS REPORTED; THE NORMALISED ONE GOVERNS (§0c.1)")
    log(f"    {'span':<20s}{'n':>5s}{'hours':>8s}{'RAW pips':>11s}"
        f"{'pips/HOUR':>12s}{'pips/sqrtH':>12s}{'share':>8s}")
    order = [s[0] for s in SPANS] + ["Fri+Sun+Mon (ARM 3)"]
    for name in order:
        R = res[name]
        if not len(R["rng"]):
            continue
        log(f"    {name:<20s}{len(R['rng']):>5d}{np.median(R['hrs']):>8.2f}"
            f"{np.median(R['rng']):>11.1f}{np.median(R['norm']):>12.3f}"
            f"{np.median(R['sqrtn']):>12.2f}{np.median(R['share']):>8.3f}")

    # ---------- the ranking ----------
    log(f"\n  THE RANKING (§4 arm 1) — is Sun+Mon the lowest-range span in the week?")
    log(f"  §3c: report the DENOMINATOR with every ranking figure; a rank-of-5 and a")
    log(f"  rank-of-4 are not comparable numbers.")
    common = set(res[RANK_SET[0]]["week"])
    for nm in RANK_SET[1:]:
        common &= set(res[nm]["week"])
    common = sorted(common)
    ranks_raw, ranks_norm, ranks_sqrt = [], [], []
    for wkname in common:
        vr = [res[nm]["rng"][res[nm]["week"] == wkname][0] for nm in RANK_SET]
        vn = [res[nm]["norm"][res[nm]["week"] == wkname][0] for nm in RANK_SET]
        ranks_raw.append(int(np.argsort(np.argsort(vr))[0]) + 1)
        ranks_norm.append(int(np.argsort(np.argsort(vn))[0]) + 1)
        vs = [res[nm]["sqrtn"][res[nm]["week"] == wkname][0] for nm in RANK_SET]
        ranks_sqrt.append(int(np.argsort(np.argsort(vs))[0]) + 1)
    ranks_raw = np.array(ranks_raw); ranks_norm = np.array(ranks_norm)
    ranks_sqrt = np.array(ranks_sqrt)
    log(f"    denominator = 5 spans, n = {len(common)} weeks   (1 = LOWEST range)")
    log(f"    RAW range        — Sun+Mon mean rank {ranks_raw.mean():.2f}, "
        f"rank-1 share {M.fmt_rate(int((ranks_raw==1).sum()), len(ranks_raw))}")
    log(f"    NORMALISED       — Sun+Mon mean rank {ranks_norm.mean():.2f}, "
        f"rank-1 share {M.fmt_rate(int((ranks_norm==1).sum()), len(ranks_norm))}")
    log(f"    rank histogram (normalised): "
        + "  ".join(f"r{r}={int((ranks_norm==r).sum())}" for r in range(1, 6)))
    log(f"    SQRT-TIME        — Sun+Mon mean rank {ranks_sqrt.mean():.2f}, "
        f"rank-1 share {M.fmt_rate(int((ranks_sqrt==1).sum()), len(ranks_sqrt))}")
    log(f"    rank histogram (sqrt-time) : "
        + "  ".join(f"r{r}={int((ranks_sqrt==r).sum())}" for r in range(1, 6)))
    log(f"    chance expectation under no effect: mean rank 3.00, rank-1 share 0.200")
    log(f"    ⚠ THE VERDICT DEPENDS ON THE NORMALISATION, and no form is neutral:")
    log(f"      raw range favours the LONGER span; pips-per-hour over-corrects and")
    log(f"      penalises the SHORTER one (range grows as ~sqrt(T), not as T);")
    log(f"      sqrt-time sits between them. §0c.1 pre-registers pips-per-hour as the")
    log(f"      governing form and it governs -- but all three are reported and the")
    log(f"      dependence is disclosed rather than resolved by preference (`D-030`).")

    # ---------- Metrics 2, 3, 4 ----------
    log(f"\n  METRIC 2 — CONTAINMENT of the remaining week's bars inside the span:")
    for name in order:
        R = res[name]
        if not len(R["contain"]):
            continue
        if name == NO_REMAINDER:
            log(f"    {name:<20s}  NOT APPLICABLE (§0c.3 — no remaining week; a zero")
            log(f"    {'':<20s}  would read as 'perfectly contained' and invert it)")
            continue
        log(f"    {name:<20s} median {np.nanmedian(R['contain']):.3f}  "
            f"(n = {int(np.isfinite(R['contain']).sum())})")

    log(f"\n  METRIC 3 — BOUNDARY RELEVANCE. §3c: the SHARE is near-certain by")
    log(f"  construction for a 31-hour span in a 120-hour week; THE DISTANCE is the")
    log(f"  informative quantity.")
    for name in order:
        R = res[name]
        if not len(R["relev"]):
            continue
        k = int(R["relev"].sum()); m = len(R["relev"])
        inside_n = m - k
        lab = "  <<< complementary subset < 30, descriptive only" if inside_n < 30 else ""
        log(f"    {name:<20s} extreme beyond an edge {k}/{m} = {k/m:.3f}"
            f"   median distance {np.nanmedian(R['dist']):7.1f} pips"
            f"   (extreme INSIDE: {inside_n}){lab}")

    log(f"\n  METRIC 4 — hours from span close to the first breach of either edge:")
    for name in order:
        R = res[name]
        if not len(R["breach_h"]):
            continue
        if name == NO_REMAINDER:
            log(f"    {name:<20s}  NOT APPLICABLE (§0c.3)")
            continue
        log(f"    {name:<20s} median {np.nanmedian(R['breach_h']):6.2f} h"
            f"   (n = {int(np.isfinite(R['breach_h']).sum())})")

    # ---------- N3 ----------
    log(f"\n  SECOND BASELINE (§4 arm 2) — N3 week-anchor shift, {M.ITERATIONS} draws:")
    lo_e, hi_e = raw.tm[sel].min(), raw.tm[sel].max()
    hole = W.dt2m(W.DATA_HOLE_WEEK)
    n3 = []
    for off in W.n3_week_shifts():
        a_ = W.week_anchor(raw.tm[sel] - int(off)) + int(off)
        u2, i2 = np.unique(a_, return_inverse=True)
        good = ((u2 >= lo_e) & (u2 + W.DAY * 5 <= hi_e)
                & ~((u2 < hole + W.DAY * 7) & (u2 + W.DAY * 5 > hole)))
        r2 = np.split(np.arange(len(tm)), np.cumsum(np.bincount(i2))[:-1])
        v = []
        for w2, idx in enumerate(r2):
            if not good[w2] or len(idx) < 40:
                continue
            # the FIRST 31 hours of the sham week, normalised — arm 1's analogue
            k = min(124, len(idx))
            s = idx[:k]
            v.append(((h[s].max() - l[s].min()) / M.PIP) / (k * 0.25))
        if v:
            n3.append(float(np.median(v)))
    n3 = np.array(n3)
    obs = float(np.median(res["Sun+Mon  (ARM 1)"]["norm"]))
    log(f"    normalised range of the sham week's FIRST 31 HOURS: {M.dist_line(n3)}")
    log(f"    OBSERVED Sun+Mon normalised range {obs:.3f} -> percentile "
        f"{M.percentile_of(obs, n3):.1f}")

    log("\n  PRE-REGISTERED SENSITIVITY APPENDIX — five largest-range weeks:")
    for r in W.largest_range_weeks(roster[roster["week"].isin(
            res['Sun+Mon  (ARM 1)']['week'])]).itertuples():
        log(f"    {r.week}  range {r.range_pips:7.1f} pips")

    return dict(arm=arm, n_arm12=int(base.sum()), n_arm3=int(arm3_ok.sum()),
                spans={k: dict(n=len(v["rng"]), hours=float(np.median(v["hrs"])),
                               raw=float(np.median(v["rng"])),
                               norm=float(np.median(v["norm"])),
                               sqrtn=float(np.median(v["sqrtn"])),
                               share=float(np.median(v["share"])),
                               contain=(None if k == NO_REMAINDER
                                        else float(np.nanmedian(v["contain"]))),
                               relev=int(v["relev"].sum()),
                               dist=float(np.nanmedian(v["dist"])),
                               breach_h=(None if k == NO_REMAINDER
                                         else float(np.nanmedian(v["breach_h"]))))
                       for k, v in res.items() if len(v["rng"])},
                rank_raw_mean=float(ranks_raw.mean()),
                rank_norm_mean=float(ranks_norm.mean()),
                rank_sqrt_mean=float(ranks_sqrt.mean()),
                rank_sqrt_hist=[int((ranks_sqrt == r).sum()) for r in range(1, 6)],
                rank_norm_hist=[int((ranks_norm == r).sum()) for r in range(1, 6)],
                rank_n=len(common),
                n3_median=float(np.median(n3)), n3_pct=M.percentile_of(obs, n3))


def main():
    lines = []

    def log(s=""):
        print(s)
        lines.append(s)

    log(M.header("PT-031", "Are Sunday and Monday the week's accumulation phase?",
                 "window   : W-C' 2013-01-06 -> 2016-06-30. Re-issue of PT-013.\n"
                 "⚠ 'Sunday + Monday' is 31 HOURS on this corpus, not two days.\n"
                 "  BOTH raw and length-normalised forms are reported and THE\n"
                 "  NORMALISED ONE GOVERNS THE VERDICT (§0c.1, §5 row 5).\n"
                 "⚠ 'Accumulation' is UNDEFINED by the course (§0b). This measures a\n"
                 "  named proxy — range, containment, boundary relevance."))
    out = {}
    for arm in ("A", "B"):
        out[arm] = run_arm(arm, log)
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "pt031_report.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    with open(os.path.join(OUT, "pt031_results.json"), "w") as fh:
        json.dump(out, fh, indent=2, default=float)


if __name__ == "__main__":
    main()
