#!/usr/bin/env python3
"""PT-045 -- V17's daily WICK and its three-day unidirectional SWING.

Runs the design pre-registered in
`06_MANUAL_BACKTEST/PRE_REGISTERED/PT-045_the_daily_wick_and_the_three_day_swing.md`,
which was committed at `7eaf4d1`, BEFORE this file existed and before any bar was read.

`COMMON_PROTOCOL.md` §9 rule 7: if this runner and that pre-registration disagree,
THE PRE-REGISTRATION GOVERNS and neither file is edited -- the disagreement is
reported in `BT_V17_0001.md`.

Everything here reads M1 bars parsed from the checksummed HistData corpus. Two scopes
are read and reported SEPARATELY and never pooled (§4): `D-035` DEVELOPMENT is the
primary window `W-D`; the `D-044` extension is the replication window `W-E`. The
`2016-07-01 -> 2016-12-31` holdout is not on disk and is not touched.

No value is read from a rendering of any kind. No M, W, peak formation, level, entry or
exit is computed anywhere in this file (§1b).

usage:  python3 run_pt045.py > ../V17/data/pt045_output.txt
"""
from __future__ import annotations

import json
import numpy as np

import mmm_lib as L

BUCKETS_PER_DAY = 96          # §3a completeness, same as PT-044
WICK_MIN_PIPS = 5.0           # §5 O2
ARMS = ["A", "B"]
PRIOR_RUN = 3                 # §3 -- V17's own cycle length
RUN_BAND = (2, 4)             # §6 decision rule for claim S
DIFF_THRESH = 0.05            # §6 decision rule for claim W and O5
SEED = getattr(L, "SEED", 20260810)
SHUFFLE_ITER = 20             # §5a N1 -- shuffled replicates per day
LABEL_SEED = {"W-D": 1000, "W-E": 2000}     # fixed, not hashed -- see run()
ARM_SEED = {"A": 11, "B": 22}


# ------------------------------------------------------------------ days

def daily_ohlc(b: L.Bars):
    """Per COMPLETE session day: (day, O, H, L, C, n_excluded).

    Completeness is `mmm_lib` C-6 generalised to the whole 24 h span: all 96
    fifteen-minute buckets of the session day must carry at least one M1 bar.
    Exclusions are COUNTED and returned, never dropped quietly (§5a N4).
    """
    sd = b.sd
    bucket = (b.mod // 15).astype("int64")
    order = np.lexsort((b.tm,))
    sd, bucket = sd[order], bucket[order]
    tm, o, h, l, c = b.tm[order], b.o[order], b.h[order], b.l[order], b.c[order]

    uniq, start = np.unique(sd, return_index=True)
    end = np.append(start[1:], len(sd))

    days, O, H, Lo, C = [], [], [], [], []
    excluded = 0
    for d, s, e in zip(uniq, start, end):
        if len(np.unique(bucket[s:e])) < BUCKETS_PER_DAY:
            excluded += 1
            continue
        days.append(d)
        O.append(o[s]); H.append(h[s:e].max()); Lo.append(l[s:e].min()); C.append(c[e - 1])
    return (np.array(days, dtype="int64"), np.array(O), np.array(H),
            np.array(Lo), np.array(C), excluded, (tm, sd, c))


def wick_stats(O, H, Lo, C):
    """§3 wick construction, in pips."""
    body_hi = np.maximum(O, C)
    body_lo = np.minimum(O, C)
    upper = (H - body_hi) / L.PIP
    lower = (body_lo - Lo) / L.PIP
    rng = (H - Lo) / L.PIP
    ok = rng > 0
    frac = np.full(len(O), np.nan)
    frac[ok] = (upper[ok] + lower[ok]) / rng[ok]
    both = (upper >= WICK_MIN_PIPS) & (lower >= WICK_MIN_PIPS)
    return upper, lower, rng, frac, both


# --------------------------------------------------- §5a N1 shuffled control

def shuffled_control(b: L.Bars, keep_days, rng_seed):
    """§5a N1. For each included day, permute THAT day's own M1 close-to-close
    returns with a fixed seed and rebuild the path from the same open.

    Volatility, return distribution and day length are preserved EXACTLY;
    only the ORDER is destroyed. Returns (median_frac, frac_both) pooled over
    all replicates.
    """
    rs = np.random.default_rng(rng_seed)
    sd = b.sd
    order = np.lexsort((b.tm,))
    sd = sd[order]
    o, c = b.o[order], b.c[order]
    keep = set(int(x) for x in keep_days)

    uniq, start = np.unique(sd, return_index=True)
    end = np.append(start[1:], len(sd))

    fracs, boths = [], []
    for d, s, e in zip(uniq, start, end):
        if int(d) not in keep:
            continue
        closes = c[s:e]
        if len(closes) < 3:
            continue
        rets = np.diff(closes)
        o0 = o[s]
        for _ in range(SHUFFLE_ITER):
            path = o0 + np.cumsum(rs.permutation(rets))
            path = np.concatenate(([o0], path))
            sO, sC = path[0], path[-1]
            sH, sL = path.max(), path.min()
            bh, bl = max(sO, sC), min(sO, sC)
            up = (sH - bh) / L.PIP
            lo = (bl - sL) / L.PIP
            r = (sH - sL) / L.PIP
            if r <= 0:
                continue
            fracs.append((up + lo) / r)
            boths.append(1.0 if (up >= WICK_MIN_PIPS and lo >= WICK_MIN_PIPS) else 0.0)
    return float(np.median(fracs)), float(np.mean(boths)), len(fracs)


# ------------------------------------------------------------------ runs

def runs_from(signs):
    """All maximal same-sign runs in a sign array (zeros break runs)."""
    out, cur = [], 0
    for s in signs:
        if s == 0:
            if cur:
                out.append(cur)
            cur = 0
            continue
        if cur and np.sign(prev) == s:
            cur += 1
        else:
            if cur:
                out.append(cur)
            cur = 1
        prev = s
    if cur:
        out.append(cur)
    return np.array(out, dtype="int64")


def reversal_runs(days, C, reading=1):
    """§3. Reversal day R: sign(R) != 0 and the three prior days share -sign(R).
    Run length from R = consecutive days from R inclusive carrying sign(R).

    TWO READINGS OF §3a's WORD "CONSECUTIVE", BOTH RUN AND BOTH REPORTED
    ---------------------------------------------------------------------
    READING 1 (as first executed, and it is the LITERAL reading of the
      pre-registration): consecutive CALENDAR days -- `sdays[j] - sdays[j-1] == 1`.

      ⚠⚠ THIS READING DESTROYS THE TEST AND ITS OUTPUT IS AN ARTEFACT.
      FX has no Saturday or Sunday session, so EVERY window spanning a weekend
      fails the check. It drops ~95% of eligible windows and TRUNCATES EVERY RUN
      AT A WEEKEND, which forces P(run >= 3) to 0 mechanically -- including for
      the N3 matched-random control, which is the tell.

    READING 2 (the disclosed correction): consecutive among the session days that
      EXIST in the corpus after §3a's completeness filter -- i.e. array-adjacent.
      A Friday and the following Monday are adjacent session days.

    NEITHER SET OF FIGURES IS DISCARDED. Reading 1's output is retained in
    `../V17/data/pt045_output_reading1.txt` and reported in `BT_V17_0001.md` §6a,
    per `REMEDIATION_PROTOCOL.md` §2 and the `PT-044` §6a precedent.
    """
    d = np.diff(C)
    signs = np.sign(d)
    sdays = days[1:]                     # sign[i] belongs to day sdays[i]
    n = len(signs)
    rev_idx, run_len, dropped = [], [], 0
    for i in range(PRIOR_RUN, n):
        if signs[i] == 0:
            continue
        # consecutiveness of the whole window R-3 .. R
        if reading == 1 and sdays[i] - sdays[i - PRIOR_RUN] != PRIOR_RUN:
            dropped += 1
            continue
        if not np.all(signs[i - PRIOR_RUN:i] == -signs[i]):
            continue
        k, j = 1, i + 1
        broke = False
        while j < n and signs[j] == signs[i]:
            if reading == 1 and sdays[j] - sdays[j - 1] != 1:
                broke = True
                break
            k += 1
            j += 1
        if broke:
            dropped += 1
            continue
        rev_idx.append(i)
        run_len.append(k)
    return np.array(rev_idx), np.array(run_len, dtype="int64"), dropped, signs, sdays


def matched_random_runs(signs, sdays, n_draw, seed, reading=1):
    """§5a N3. Same count of days drawn at random from NON-reversal days."""
    rs = np.random.default_rng(seed)
    n = len(signs)
    pool = []
    for i in range(PRIOR_RUN, n):
        if signs[i] == 0:
            continue
        if reading == 1 and sdays[i] - sdays[i - PRIOR_RUN] != PRIOR_RUN:
            continue
        if np.all(signs[i - PRIOR_RUN:i] == -signs[i]):
            continue                      # exclude actual reversals
        pool.append(i)
    if not pool or n_draw == 0:
        return np.array([], dtype="int64")
    pick = rs.choice(pool, size=min(n_draw, len(pool)), replace=False)
    out = []
    for i in pick:
        k, j = 1, i + 1
        while j < n and signs[j] == signs[i] and (reading == 2 or sdays[j] - sdays[j - 1] == 1):
            k += 1
            j += 1
        out.append(k)
    return np.array(out, dtype="int64")


# ------------------------------------------------------------------ verdicts

def verdict_w(d_frac, d_both):
    if d_frac > DIFF_THRESH and d_both > DIFF_THRESH:
        return "SUPPORTED"
    if d_frac < -DIFF_THRESH or d_both < -DIFF_THRESH:
        if d_frac > DIFF_THRESH or d_both > DIFF_THRESH:
            return "INDETERMINATE"
        return "CONTRADICTED"
    if abs(d_frac) <= DIFF_THRESH and abs(d_both) <= DIFF_THRESH:
        return "NOT SUPPORTED"
    return "INDETERMINATE"


def verdict_s(med_run, p3_rev, p3_uncond):
    if not (RUN_BAND[0] <= med_run <= RUN_BAND[1]):
        return "CONTRADICTED AS STATED"
    return "SUPPORTED" if (p3_rev - p3_uncond) > DIFF_THRESH else "WEAKLY SUPPORTED"


# ------------------------------------------------------------------ main

def run(arm, scope, lo, hi, label, reading=1):
    b = L.load_m1(arm, scope=scope)
    b = b.slice(L.dt2m(lo), L.dt2m(hi + " 23:59"))
    days, O, H, Lo, C, excl, _ = daily_ohlc(b)
    upper, lower, rng, frac, both = wick_stats(O, H, Lo, C)

    ok = ~np.isnan(frac)
    o1 = float(np.median(frac[ok]))
    o2 = float(np.mean(both[ok]))
    # ⚠ FIXED after the first two executions: this line read
    #     `SEED + hash(label) % 9973`
    # and Python SALTS str.__hash__ PER PROCESS, so the shuffle seed -- and
    # therefore O3 -- was NOT reproducible across runs. `COMMON_PROTOCOL.md` §2
    # requires that re-running reproduces every figure exactly, seed included.
    # Disclosed in `BT_V17_0001.md` §6b; the superseded figures are retained.
    s1, s2, s_n = shuffled_control(b, days, SEED + LABEL_SEED[label] + ARM_SEED[arm])

    rev_idx, run_len, rev_dropped, signs, sdays = reversal_runs(days, C, reading)
    all_runs = runs_from(signs)
    med_run = float(np.median(run_len)) if len(run_len) else float("nan")
    p_band = float(np.mean((run_len >= RUN_BAND[0]) & (run_len <= RUN_BAND[1]))) if len(run_len) else float("nan")
    p3_rev = float(np.mean(run_len >= 3)) if len(run_len) else float("nan")
    p3_unc = float(np.mean(all_runs >= 3)) if len(all_runs) else float("nan")
    n3 = matched_random_runs(signs, sdays, len(run_len), SEED + 17, reading)
    p3_n3 = float(np.mean(n3 >= 3)) if len(n3) else float("nan")

    # O6 -- cumulative signed move over R..R+2
    cum = []
    for i in rev_idx:
        if i + 2 < len(signs):
            d3 = C[i + 1 + 2] - C[i]          # C index is day-aligned: signs[i] -> days[i+1]
            cum.append(np.sign(signs[i]) * d3 / L.PIP)
    cum = np.array(cum)
    o6 = float(np.mean(cum)) if len(cum) else float("nan")
    o6ci = L.boot_ci(cum, stat=np.mean) if len(cum) > 5 else (float("nan"), float("nan"))

    return dict(
        label=label, arm=arm, window=f"{lo} -> {hi}", reading=reading,
        n_days=int(ok.sum()), excluded=int(excl),
        O1_median_wick_frac=round(o1, 4),
        O2_both_wicks_ge_5pips=round(o2, 4),
        O3_shuffled_median=round(s1, 4), O3_shuffled_both=round(s2, 4),
        O3_diff_frac=round(o1 - s1, 4), O3_diff_both=round(o2 - s2, 4),
        O3_shuffle_n=int(s_n),
        verdict_W=verdict_w(o1 - s1, o2 - s2),
        n_reversals=int(len(run_len)), reversals_dropped=int(rev_dropped),
        O4_median_run=med_run, O4_p_run_in_2_4=round(p_band, 4) if p_band == p_band else None,
        O5_p_run_ge3_rev=round(p3_rev, 4) if p3_rev == p3_rev else None,
        O5_p_run_ge3_uncond=round(p3_unc, 4) if p3_unc == p3_unc else None,
        O5_margin=round(p3_rev - p3_unc, 4) if p3_rev == p3_rev else None,
        N3_p_run_ge3_matched=round(p3_n3, 4) if p3_n3 == p3_n3 else None,
        O6_mean_cum_pips_R_to_R2=round(o6, 2) if o6 == o6 else None,
        O6_boot_ci=[round(float(x), 2) for x in o6ci] if o6ci[0] == o6ci[0] else None,
        verdict_S=verdict_s(med_run, p3_rev, p3_unc) if med_run == med_run else "UNDERPOWERED",
        underpowered=bool(len(run_len) < 60),
    )


def main():
    print("PT-045 -- V17's daily wick and three-day swing")
    print("pre-registration: PT-045_the_daily_wick_and_the_three_day_swing.md @ 7eaf4d1")
    print()
    for scope in ("development", "extended"):
        rep, sha = L.qa_gate(scope)
        print(f"QA GATE [{scope}]: PASSED")
    print()

    results = []
    for reading in (1, 2):
        for arm in ARMS:
            results.append(run(arm, "development", "2013-01-02", "2016-06-30", "W-D", reading))
            results.append(run(arm, "extended", "2017-01-03", "2025-12-31", "W-E", reading))

    for r in results:
        print(f"--- {r['label']} / arm {r['arm']} / {r['window']} / READING {r['reading']} ---")
        for k, v in r.items():
            if k in ("label", "arm", "window", "reading"):
                continue
            print(f"    {k:28s} {v}")
        print()

    with open("../V17/data/pt045_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("wrote ../V17/data/pt045_results.json")


if __name__ == "__main__":
    main()
