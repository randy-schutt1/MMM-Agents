#!/usr/bin/env python3
"""PT-044 -- V16's 200-pip daily allotment: a CEILING or a TYPICAL day?

Runs the design pre-registered in
`06_MANUAL_BACKTEST/PRE_REGISTERED/PT-044_the_two_hundred_pip_daily_allotment.md`,
which was committed at `9cc1cae`, BEFORE this file existed and before any bar was read.

`COMMON_PROTOCOL.md` §9 rule 7: if this runner and that pre-registration disagree,
THE PRE-REGISTRATION GOVERNS and neither file is edited -- the disagreement is
reported in `BT_V16_0001.md`.

Everything here reads M1 bars parsed from the checksummed HistData corpus. Two scopes
are read and reported SEPARATELY and never pooled (§4): `D-035` DEVELOPMENT is the
primary window `W-D`; the `D-044` extension is the replication window `W-E`. The
`2016-07-01 -> 2016-12-31` holdout is not on disk and is not touched.

No value is read from a rendering of any kind. No M, W, entry, exit or level is
computed anywhere in this file (§8).

usage:  python3 run_pt044.py > ../V16/data/pt044_output.txt
"""
from __future__ import annotations

import json
import numpy as np

import mmm_lib as L

BUCKETS_PER_DAY = 96          # §3a completeness
ADR_LOOKBACK = 15             # §3 -- V16's own stated number, [00:09:31]
ARMS = ["A", "B"]
BAND = (150.0, 250.0)         # §5 O4, "approximately 200" at +/-25%
CEILING = 200.0               # §5 O1


def day_ranges(b: L.Bars):
    """Per included session day: (day index, range in pips). §3, §3a.

    Inclusion: all 96 fifteen-minute buckets of the day's 24-hour span carry a bar.
    Exclusions are counted and returned, never dropped quietly (§5a N4).
    """
    tm = b.tm
    sd = L.session_day(tm)
    order = np.argsort(sd, kind="stable")
    sd_s = sd[order]
    uniq, starts, counts = np.unique(sd_s, return_index=True, return_counts=True)

    days, rng, excluded = [], [], []
    for d, s, n in zip(uniq, starts, counts):
        idx = order[s:s + n]
        end = (int(d) * L.DAY) + L.DAY_END_MIN
        start = end - L.DAY
        nb = len(np.unique((tm[idx] - start) // 15))
        if nb == BUCKETS_PER_DAY:
            days.append(int(d))
            rng.append((float(b.h[idx].max()) - float(b.l[idx].min())) / L.PIP)
        else:
            excluded.append((int(d), int(nb)))
    return np.asarray(days), np.asarray(rng), excluded


def adr15(days: np.ndarray, rng: np.ndarray):
    """§5a N2. Trailing mean of the previous ADR_LOOKBACK included days' ranges.

    Uses the ordinal sequence of INCLUDED days, not calendar days -- stated here
    because the two differ wherever §3a excluded a day, and the pre-registration
    fixes the number 15 but not this detail. Reported in BT_V16_0001.md §7.
    """
    out = np.full(len(rng), np.nan)
    for i in range(ADR_LOOKBACK, len(rng)):
        out[i] = rng[i - ADR_LOOKBACK:i].mean()
    return out


def measures(rng: np.ndarray) -> dict:
    """§5 O1-O5. No measure not listed in the pre-registration."""
    return dict(
        n=int(len(rng)),
        O1_p_gt_200=float((rng > CEILING).mean()),
        O2_median=float(np.median(rng)),
        O3_mean=float(rng.mean()),
        O4_p_in_150_250=float(((rng >= BAND[0]) & (rng <= BAND[1])).mean()),
        O5_p99=float(np.percentile(rng, 99)),
    )


def verdict_ceiling(o1: float) -> str:
    """§6, reading B. Thresholds fixed before the run."""
    if o1 <= 0.02:
        return "SUPPORTED"
    if o1 <= 0.10:
        return "WEAKLY SUPPORTED"
    return "CONTRADICTED AS STATED"


def verdict_typical(o2: float) -> str:
    """§6, reading A. Thresholds fixed before the run."""
    if 150.0 <= o2 <= 250.0:
        return "SUPPORTED"
    if 100.0 <= o2 < 150.0 or 250.0 < o2 <= 300.0:
        return "PARTIALLY SUPPORTED"
    return "CONTRADICTED AS STATED"


def per_year(days: np.ndarray, rng: np.ndarray):
    """§5a N3."""
    yr = np.array([int(str(np.datetime64(int(d), "D"))[:4]) for d in days])
    out = {}
    for y in sorted(set(yr.tolist())):
        m = yr == y
        out[str(y)] = dict(n=int(m.sum()), median=round(float(np.median(rng[m])), 1))
    return out


def main() -> None:
    print("PT-044 -- V16's 200-pip daily allotment: CEILING or TYPICAL day?")
    print("pre-registration: PRE_REGISTERED/PT-044_the_two_hundred_pip_daily_allotment.md @ 9cc1cae")
    print()

    results = {"windows": {}}

    for scope, wname in [("development", "W-D"), ("extension", "W-E")]:
        report, manifest = L.qa_gate(scope)
        print(f"=== {wname}  (scope={scope}) ===")
        print(f"QA gate: PASSED   report={report}")
        w = {"scope": scope, "qa_report": report, "arms": {}}

        for arm in ARMS:
            b = L.load_m1(arm, scope=scope)
            days, rng, excluded = day_ranges(b)
            m = measures(rng)
            a15 = adr15(days, rng)
            a15v = a15[~np.isnan(a15)]

            m["N2_adr15_median"] = float(np.median(a15v))
            m["N2_adr15_mean"] = float(a15v.mean())
            m["N2_p_adr15_gt_200"] = float((a15v > CEILING).mean())
            m["N3_per_year"] = per_year(days, rng)
            m["N4_excluded_days"] = len(excluded)
            m["N4_excluded_pct"] = round(100.0 * len(excluded) / (len(excluded) + len(rng)), 1)
            m["first_day"] = L.day2s(days[0])
            m["last_day"] = L.day2s(days[-1])
            m["verdict_ceiling"] = verdict_ceiling(m["O1_p_gt_200"])
            m["verdict_typical"] = verdict_typical(m["O2_median"])
            w["arms"][arm] = m

            print(f"  arm {arm}: n={m['n']}  {m['first_day']} -> {m['last_day']}"
                  f"  (excluded {m['N4_excluded_days']}, {m['N4_excluded_pct']}%)")
            print(f"    O1 P(range>200) = {m['O1_p_gt_200']:.4f}   -> CEILING: {m['verdict_ceiling']}")
            print(f"    O2 median       = {m['O2_median']:.1f} pips -> TYPICAL: {m['verdict_typical']}")
            print(f"    O3 mean         = {m['O3_mean']:.1f} pips")
            print(f"    O4 P(150-250)   = {m['O4_p_in_150_250']:.4f}")
            print(f"    O5 p99          = {m['O5_p99']:.1f} pips")
            print(f"    N2 ADR15 median = {m['N2_adr15_median']:.1f}  mean = {m['N2_adr15_mean']:.1f}"
                  f"  P(ADR15>200) = {m['N2_p_adr15_gt_200']:.4f}")
            print(f"    N3 per-year median: {m['N3_per_year']}")

        da = w["arms"]["A"]["O2_median"]
        db = w["arms"]["B"]["O2_median"]
        w["N1_arm_delta_median"] = round(abs(da - db), 2)
        print(f"  N1 arm A/B median delta = {w['N1_arm_delta_median']:.2f} pips")
        print()
        results["windows"][wname] = w

    with open("../V16/data/pt044_results.json", "w") as fh:
        json.dump(results, fh, indent=2, sort_keys=True)
    print("wrote ../V16/data/pt044_results.json")


if __name__ == "__main__":
    main()
