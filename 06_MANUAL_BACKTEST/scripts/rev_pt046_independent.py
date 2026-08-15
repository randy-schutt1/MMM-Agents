#!/usr/bin/env python3
"""REVIEWER's independent re-implementation of PT-046 (V18 R1).

Written from `06_MANUAL_BACKTEST/PRE_REGISTERED/PT-046_two_sessions_then_a_corrective_third.md`
ALONE, before `run_pt046.py` was opened. `mmm_lib` is used for data loading only
(`load_m15`, `session_day`, `minute_of_day`, `SEED`) — it is shared infrastructure,
not the submission's test logic.

Disclosure: before writing this, the reviewer had seen exactly three lines of
`run_pt046.py` via a grep for `load_m1` (item-247 provenance check) — the import
line, `b = L.load_m15(arm, scope)` and the `assert_development` call. No measure,
control or verdict logic was seen.

Implements: §2a partition, §3 inclusion/adjacency, §4 direction, §5 O1-O6,
§5a N1/N2/N3/N5, §6 decision rule.
"""
from __future__ import annotations

import json
import math
import sys

import numpy as np

sys.path.insert(0, __import__("os").path.dirname(__file__))
import mmm_lib as L  # noqa: E402

DAY = 1440
SHUFFLE_ITER = 200


# ----------------------------------------------------------------- helpers
def wilson(k: int, n: int, z: float = 1.959963984540054):
    """Wilson score interval for a binomial proportion."""
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    d = 1.0 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - h) / d, (c + h) / d)


# ----------------------------------------------------- §2a / §3 / §4 build
def build_sessions(b, mid_boundary_min: int):
    """Return (day_index[], session_slot[], direction[]) for COMPLETE session days.

    §2a partition on the arm clock, three contiguous sessions of the C-1 session
    day `[D-1 17:00, D 17:00)`:
        S1 17:00 -> 03:00 | S2 03:00 -> `mid` | S3 `mid` -> 17:00
    §3 completeness: a session day is INCLUDED only if all 96 fifteen-minute
    buckets of its 17:00 -> 17:00 span are present.
    §4 direction: sign(close of last bar in window - open of first bar in window).
    """
    sd = L.session_day(b.tm)
    mod = L.minute_of_day(b.tm)

    # minutes since the 17:00 session-day anchor, 0..1439
    since = (mod - L.DAY_END_MIN) % DAY
    s1_len = (DAY - L.DAY_END_MIN) + L.BOX_END_MIN          # 17:00 -> 03:00 = 600
    s2_len = mid_boundary_min - L.BOX_END_MIN               # 03:00 -> mid
    slot = np.where(since < s1_len, 0,
                    np.where(since < s1_len + s2_len, 1, 2))

    days, counts = np.unique(sd, return_counts=True)
    complete = set(days[counts == 96].tolist())

    out_day, out_slot, out_dir = [], [], []
    order = np.argsort(sd, kind="stable")
    sd_s, slot_s = sd[order], slot[order]
    o_s, c_s = b.o[order], b.c[order]
    tm_s = b.tm[order]

    # iterate day by day, slot by slot, in chronological order
    for d in sorted(complete):
        m_day = sd_s == d
        for sl in (0, 1, 2):
            m = m_day & (slot_s == sl)
            if not m.any():
                out_day, out_slot, out_dir = out_day, out_slot, out_dir
                continue
            idx = np.nonzero(m)[0]
            idx = idx[np.argsort(tm_s[idx])]
            delta = c_s[idx[-1]] - o_s[idx[0]]
            out_day.append(int(d))
            out_slot.append(sl)
            out_dir.append(int(np.sign(delta)))
    return (np.array(out_day, dtype="int64"),
            np.array(out_slot, dtype="int64"),
            np.array(out_dir, dtype="int64"),
            len(days), len(complete))


def blocks(day, slot, bridge_gaps: bool):
    """Split the session sequence into unbroken runs of CORPUS-ADJACENT sessions.

    §3: a run may only be counted across sessions adjacent in the corpus. Within a
    day, slots 0->1->2 are adjacent. Across days, day d slot 2 -> day d+1 slot 0 is
    adjacent only if d+1 immediately follows d (so an excluded day or a weekend
    RESETS the counter).

    `bridge_gaps=True` is control N5: calendar-consecutive rather than
    corpus-adjacent — gaps do not reset.
    """
    n = len(day)
    out, start = [], 0
    for i in range(1, n):
        if bridge_gaps:
            adj = True
        elif slot[i] == slot[i - 1] + 1 and day[i] == day[i - 1]:
            adj = True
        elif slot[i] == 0 and slot[i - 1] == 2 and day[i] == day[i - 1] + 1:
            adj = True
        else:
            adj = False
        if not adj:
            out.append((start, i))
            start = i
    out.append((start, n))
    return out


# --------------------------------------------------------------- §5 measures
def measures(direction, blks):
    """O1 (primary), O2 (base rate), O3 (lift), O4, O5 over the given blocks."""
    o1_k = o1_n = 0          # third corrects | prior pair same direction
    o2_k = o2_n = 0          # any session reverses the one before it
    o4_k = o4_n = 0          # fourth resumes | pair + correction
    for lo, hi in blks:
        d = direction[lo:hi]
        for i in range(len(d) - 1):
            if d[i] == 0 or d[i + 1] == 0:
                continue
            o2_n += 1
            if d[i + 1] == -d[i]:
                o2_k += 1
        for i in range(len(d) - 2):
            if d[i] == 0 or d[i] != d[i + 1] or d[i + 2] == 0:
                continue
            o1_n += 1
            corrects = d[i + 2] == -d[i]
            if corrects:
                o1_k += 1
                if i + 3 < len(d) and d[i + 3] != 0:
                    o4_n += 1
                    if d[i + 3] == d[i]:
                        o4_k += 1
    return dict(o1_k=o1_k, o1_n=o1_n, o2_k=o2_k, o2_n=o2_n, o4_k=o4_k, o4_n=o4_n)


def run_lengths(direction, blks):
    """O5 — distribution of same-direction run lengths. Zeros break a run."""
    lens = []
    for lo, hi in blks:
        d = direction[lo:hi]
        cur = 0
        prev = None
        for x in d:
            if x == 0:
                if cur:
                    lens.append(cur)
                cur, prev = 0, None
                continue
            if prev is None or x != prev:
                if cur:
                    lens.append(cur)
                cur, prev = 1, x
            else:
                cur += 1
        if cur:
            lens.append(cur)
    return np.array(lens, dtype="int64")


def summarise(direction, blks):
    m = measures(direction, blks)
    o1 = m["o1_k"] / m["o1_n"] if m["o1_n"] else float("nan")
    o2 = m["o2_k"] / m["o2_n"] if m["o2_n"] else float("nan")
    o4 = m["o4_k"] / m["o4_n"] if m["o4_n"] else float("nan")
    return dict(
        O1=o1, O1_ci=wilson(m["o1_k"], m["o1_n"]), O1_n=m["o1_n"],
        O2=o2, O2_ci=wilson(m["o2_k"], m["o2_n"]), O2_n=m["o2_n"],
        O3=o1 - o2,
        O4=o4, O4_n=m["o4_n"],
    )


# --------------------------------------------------------------- §5a N1
def n1_percentile(direction, blks, observed_o3, seed):
    """Matched-random: shuffle the direction sequence preserving +1/-1/0 counts."""
    rng = np.random.default_rng(seed)
    d = direction.copy()
    vals = []
    for _ in range(SHUFFLE_ITER):
        rng.shuffle(d)
        s = summarise(d, blks)
        vals.append(s["O3"])
    vals = np.array(vals)
    pct = float((vals < observed_o3).mean() * 100.0)
    return pct, float(np.nanmean(vals)), float(np.nanstd(vals))


# --------------------------------------------------------------- §6 verdict
def verdict(o3, n1_pct, n3_flips):
    if n3_flips:
        return "INCONCLUSIVE (N3 fragility guard fired)"
    if o3 >= 0.05 and n1_pct >= 95:
        return "SUPPORTED AS STATED"
    if 0.02 <= o3 < 0.05 and n1_pct >= 90:
        return "WEAKLY SUPPORTED"
    if o3 <= -0.05 and n1_pct <= 5:
        return "CONTRADICTED AS STATED"
    if -0.02 < o3 < 0.02 or n1_pct < 90:
        return "NOT SUPPORTED"
    return "NOT SUPPORTED"


# ------------------------------------------------------------------- driver
def cell(arm, scope, mid_min, bridge=False, label=""):
    b = L.load_m15(arm, scope)
    if scope == "development":
        L.assert_development(b.tm, f"REV PT-046 {label}")
    day, slot, direction, n_days, n_complete = build_sessions(b, mid_min)
    blks = blocks(day, slot, bridge_gaps=bridge)
    s = summarise(direction, blks)
    s.update(arm=arm, scope=scope, mid_min=mid_min, bridge=bridge, label=label,
             n_sessions=len(direction), n_days_seen=n_days,
             n_days_complete=n_complete, n_days_excluded=n_days - n_complete,
             n_zero=int((direction == 0).sum()), n_blocks=len(blks))
    return s, direction, blks


def main():
    results = {}

    for scope, wname in (("development", "W-D"), ("extended", "W-E")):
        for arm in ("A", "B"):
            key = f"{wname}/{arm}"
            try:
                base, direction, blks = cell(arm, scope, 9 * 60, label=key)
            except SystemExit as e:
                results[key] = {"sealed": str(e)}
                print(f"\n### {key}: SEAL FIRED -> {e}")
                continue

            pct, mu, sd_ = n1_percentile(direction, blks, base["O3"], L.SEED)
            base["N1_percentile"] = pct
            base["N1_mean_O3"] = mu
            base["N1_sd_O3"] = sd_

            # N3 — mandatory boundary sensitivity: 08:00 and 10:00
            n3 = {}
            for mm, nm in ((8 * 60, "08:00"), (10 * 60, "10:00")):
                alt, _, _ = cell(arm, scope, mm, label=f"{key} N3 {nm}")
                n3[nm] = {"O1": alt["O1"], "O2": alt["O2"], "O3": alt["O3"],
                          "O1_n": alt["O1_n"]}
            signs = [np.sign(base["O3"])] + [np.sign(v["O3"]) for v in n3.values()]
            nonzero = [s for s in signs if s != 0]
            n3_flips = len(set(nonzero)) > 1
            base["N3"] = n3
            base["N3_signs"] = [float(s) for s in signs]
            base["N3_flips_sign"] = bool(n3_flips)

            # N2 — run-length null
            rl = run_lengths(direction, blks)
            counts = {int(k): int(v) for k, v in
                      zip(*np.unique(rl, return_counts=True))}
            n_runs = len(rl)
            # geometric with p = P(direction changes) estimated from the data
            p = base["O2"]
            geo = {k: n_runs * ((1 - p) ** (k - 1)) * p for k in sorted(counts)}
            base["N2_observed"] = counts
            base["N2_geometric"] = {k: round(v, 1) for k, v in geo.items()}
            base["N2_mode"] = int(max(counts, key=counts.get))
            base["N2_median"] = float(np.median(rl))
            base["N2_n_runs"] = n_runs

            # N5 — adjacency artefact control
            alt5, _, _ = cell(arm, scope, 9 * 60, bridge=True, label=f"{key} N5")
            base["N5_bridged"] = {"O1": alt5["O1"], "O2": alt5["O2"],
                                  "O3": alt5["O3"], "O1_n": alt5["O1_n"]}

            base["VERDICT"] = verdict(base["O3"], pct, n3_flips)
            results[key] = base

            print(f"\n### {key}")
            print(f"  sessions={base['n_sessions']}  days complete={base['n_days_complete']}"
                  f"  excluded={base['n_days_excluded']}  zeros={base['n_zero']}"
                  f"  blocks={base['n_blocks']}")
            print(f"  O1 P(3rd corrects|2 same) = {base['O1']:.4f} "
                  f"[{base['O1_ci'][0]:.4f}-{base['O1_ci'][1]:.4f}]  n={base['O1_n']}")
            print(f"  O2 base rate             = {base['O2']:.4f} "
                  f"[{base['O2_ci'][0]:.4f}-{base['O2_ci'][1]:.4f}]  n={base['O2_n']}")
            print(f"  O3 LIFT                  = {base['O3']:+.4f}")
            print(f"  N1 percentile of observed O3 = {pct:.1f}")
            print(f"  N3 O3 @08:00={n3['08:00']['O3']:+.4f}  "
                  f"@09:00={base['O3']:+.4f}  @10:00={n3['10:00']['O3']:+.4f}"
                  f"   SIGN FLIPS={n3_flips}")
            print(f"  N2 run-length mode={base['N2_mode']} median={base['N2_median']}"
                  f"  len2 observed={counts.get(2)} vs geometric={geo.get(2, 0):.1f}")
            print(f"  N5 bridged O3={alt5['O3']:+.4f} (reported, not substituted)")
            print(f"  VERDICT: {base['VERDICT']}")

    with open(__import__("os").path.join(
            __import__("os").path.dirname(__file__), "rev_pt046_results.json"), "w") as f:
        json.dump(results, f, indent=2, default=str)
    print("\nwrote rev_pt046_results.json")


if __name__ == "__main__":
    main()
