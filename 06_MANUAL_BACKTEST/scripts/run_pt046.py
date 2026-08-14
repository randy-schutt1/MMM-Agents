#!/usr/bin/env python3
"""PT-046 -- V18's "two sessions of rise or fall, third session corrective in nature".

Runs the design pre-registered in
`06_MANUAL_BACKTEST/PRE_REGISTERED/PT-046_two_sessions_then_a_corrective_third.md`,
committed at c1cb2c7, BEFORE this file existed and before any bar was read.

`COMMON_PROTOCOL.md` §9 rule 7: if this runner and that pre-registration disagree,
THE PRE-REGISTRATION GOVERNS and neither file is edited -- the disagreement is
reported in `BT_V18_0001.md`.

Everything here reads M1 bars parsed from the checksummed HistData corpus. Two scopes
are read and reported SEPARATELY and never pooled (§3): `D-035` DEVELOPMENT is the
primary window `W-D`; the `D-044` extension is the replication window `W-E`. The
2016-07-01 -> 2016-12-31 holdout is not on disk and is not touched.

No entry, exit, stop, target, M, W, peak formation or level is computed anywhere in
this file (§1a).

usage:  python3 run_pt046.py > ../V18/data/pt046_output.txt
"""
from __future__ import annotations

import json
import numpy as np

import mmm_lib as L

ARMS = ["A", "B"]
BUCKETS_PER_DAY = 96                 # §3 completeness over the 17:00->17:00 span
SHUFFLE_ITER = 200                   # §5a N1
SEED = getattr(L, "SEED", 20260810)
ARM_SEED = {"A": 11, "B": 22}
LABEL_SEED = {"W-D": 1000, "W-E": 2000}

# §2a declared partition, as offsets in minutes from the 17:00 session anchor.
# S1 17:00->03:00 (600 min), S2 03:00->09:00 (360), S3 09:00->17:00 (480).
BOUNDARY_DEFAULT = 9 * 60            # the INVENTED 09:00 line -- see §2a
BOUNDARY_VARIANTS = [8 * 60, 9 * 60, 10 * 60]     # §5a N3

LIFT_STRONG = 0.05                   # §6
LIFT_WEAK = 0.02
ANCHOR = L.SESSION_ANCHOR            # 17*60


# ---------------------------------------------------------------- sessions

def session_index(mod, boundary_min):
    """Map minute-of-day -> 0,1,2 for S1/S2/S3 under the declared partition.

    Offsets are taken from the 17:00 session anchor so the S1 window wraps midnight
    exactly the way `mmm_lib` C-1's session day does.
    """
    off = (np.asarray(mod) - ANCHOR) % L.DAY        # 0 .. 1439, 0 == 17:00
    b_s2 = (3 * 60 - ANCHOR) % L.DAY                # 03:00 -> 600
    b_s3 = (boundary_min - ANCHOR) % L.DAY          # 09:00 -> 960
    idx = np.zeros(len(off), dtype="int64")
    idx[(off >= b_s2) & (off < b_s3)] = 1
    idx[off >= b_s3] = 2
    return idx


def complete_days(b: L.Bars):
    """Session days for which all 96 fifteen-minute buckets carry >= 1 M1 bar."""
    sd = b.sd
    slot = L.session_slot(b.mod)
    key = sd.astype("int64") * 100 + slot
    uniq_days, counts = np.unique(sd, return_counts=True)
    present = {}
    for d, s in zip(sd, slot):
        present.setdefault(d, set()).add(int(s))
    ok = np.array([d for d in uniq_days if len(present[d]) == BUCKETS_PER_DAY])
    excluded = len(uniq_days) - len(ok)
    return ok, len(uniq_days), excluded


def session_directions(b: L.Bars, boundary_min):
    """Per (complete session day, session) -> direction, in strict time order.

    Returns (days, sess_idx, dirs) aligned, plus counts.
    """
    ok_days, n_days_total, n_excluded = complete_days(b)
    ok_set = set(int(d) for d in ok_days)

    sd = b.sd
    keep = np.array([int(d) in ok_set for d in sd])
    tm, o, c, mod, sd = b.tm[keep], b.o[keep], b.c[keep], b.mod[keep], sd[keep]

    si = session_index(mod, boundary_min)
    order = np.argsort(tm, kind="stable")
    tm, o, c, si, sd = tm[order], o[order], c[order], si[order], sd[order]

    key = sd.astype("int64") * 10 + si
    # first open and last close per (day, session)
    _, first_idx = np.unique(key, return_index=True)
    # np.unique returns sorted-unique keys; keys sort by day then session, which is
    # also time order because the partition is contiguous from the 17:00 anchor.
    uniq = key[np.sort(first_idx)]
    starts = np.sort(first_idx)
    ends = np.append(starts[1:], len(key)) - 1

    opens = o[starts]
    closes = c[ends]
    dirs = np.sign(closes - opens).astype("int64")
    days = uniq // 10
    sess = uniq % 10
    return days, sess, dirs, n_days_total, n_excluded


def adjacency_breaks(days, sess, bridge_gaps: bool):
    """True where the session at i is NOT corpus-adjacent to the one at i-1.

    §3: a run may only be counted across sessions adjacent in the corpus. Where a day
    is excluded or a weekend intervenes, the run RESETS. N5 (bridge_gaps=True) relaxes
    this to calendar-consecutive, and is reported beside the primary, never as it.
    """
    n = len(days)
    brk = np.zeros(n, dtype=bool)
    if n == 0:
        return brk
    brk[0] = True
    if bridge_gaps:
        return brk
    for i in range(1, n):
        same_day = days[i] == days[i - 1]
        if same_day:
            brk[i] = (sess[i] != sess[i - 1] + 1)
        else:
            brk[i] = not (days[i] == days[i - 1] + 1 and sess[i - 1] == 2 and sess[i] == 0)
    return brk


# ---------------------------------------------------------------- measures

def measures(dirs, brk):
    """O1..O6 from a direction sequence with reset flags."""
    n = len(dirs)
    pair_n = 0          # prior pairs (two adjacent same non-zero)
    pair_corr = 0       # ... whose third session went the other way
    pair_zero = 0       # ... whose third was a tie
    rev_n = 0           # unconditional adjacent transitions (both non-zero)
    rev_k = 0           # ... that reversed
    quad_n = 0          # O4 denominators
    quad_res = 0

    for i in range(1, n):
        if brk[i] or dirs[i] == 0 or dirs[i - 1] == 0:
            continue
        rev_n += 1
        if dirs[i] == -dirs[i - 1]:
            rev_k += 1

    for i in range(2, n):
        if brk[i] or brk[i - 1]:
            continue
        d = dirs[i - 2]
        if d == 0 or dirs[i - 1] != d:
            continue
        pair_n += 1
        if dirs[i] == 0:
            pair_zero += 1
        elif dirs[i] == -d:
            pair_corr += 1
            if i + 1 < n and not brk[i + 1]:
                quad_n += 1
                if dirs[i + 1] == d:
                    quad_res += 1

    o1 = pair_corr / pair_n if pair_n else float("nan")
    o2 = rev_k / rev_n if rev_n else float("nan")
    o4 = quad_res / quad_n if quad_n else float("nan")

    # O5 run lengths
    runs = []
    cur = 0
    cur_d = 0
    for i in range(n):
        if brk[i] or dirs[i] == 0 or dirs[i] != cur_d:
            if cur:
                runs.append(cur)
            cur = 1 if dirs[i] != 0 else 0
            cur_d = dirs[i]
        else:
            cur += 1
    if cur:
        runs.append(cur)
    runs = np.array(runs) if runs else np.array([0])

    return dict(O1=o1, O2=o2, O3=o1 - o2, O4=o4,
                pair_n=pair_n, pair_corr=pair_corr, pair_zero=pair_zero,
                rev_n=rev_n, rev_k=rev_k, quad_n=quad_n,
                run_median=float(np.median(runs)),
                run_mode=int(np.bincount(runs).argmax()),
                run_hist={int(k): int(v) for k, v in
                          zip(*np.unique(runs, return_counts=True))})


def n1_shuffle(dirs, brk, seed):
    """§5a N1 -- shuffle preserving the exact counts of +1/-1/0."""
    rng = np.random.default_rng(seed)
    obs = measures(dirs, brk)["O3"]
    dist = []
    d = dirs.copy()
    for _ in range(SHUFFLE_ITER):
        rng.shuffle(d)
        dist.append(measures(d, brk)["O3"])
    dist = np.array(dist)
    pct = float((dist < obs).mean() * 100.0)
    return dict(obs=obs, mean=float(dist.mean()), sd=float(dist.std()),
                p95=float(np.percentile(dist, 95)),
                p05=float(np.percentile(dist, 5)), percentile=pct)


def geometric_expectation(runs_hist, total):
    """§5a N2 -- an i.i.d. fair sequence gives geometric run lengths, mode 1."""
    out = {}
    for k in sorted(runs_hist):
        if k >= 1:
            out[k] = round(total * (0.5 ** k), 1)
    return out


# ---------------------------------------------------------------- run

def run_one(arm, scope, label, boundary_min, bridge_gaps=False):
    b = L.load_m15(arm, scope)
    if scope == "development":
        L.assert_development(b.tm, f"PT-046 {label} arm {arm}")
    days, sess, dirs, n_days_total, n_excluded = session_directions(b, boundary_min)
    brk = adjacency_breaks(days, sess, bridge_gaps)
    m = measures(dirs, brk)
    m.update(n_sessions=len(dirs), n_days_total=int(n_days_total),
             n_excluded=int(n_excluded),
             n_zero=int((dirs == 0).sum()),
             arm=arm, window=label, boundary=boundary_min,
             bridge_gaps=bridge_gaps)
    return m, dirs, brk


def verdict(o3, pct, flipped):
    if flipped:
        return "INCONCLUSIVE (N3 flipped)"
    if o3 >= LIFT_STRONG and pct >= 95:
        return "SUPPORTED AS STATED"
    if LIFT_WEAK <= o3 < LIFT_STRONG and pct >= 90:
        return "WEAKLY SUPPORTED"
    if o3 <= -LIFT_STRONG and pct <= 5:
        return "CONTRADICTED AS STATED"
    return "NOT SUPPORTED"


def main():
    print("=" * 78)
    print("PT-046 -- V18: two sessions of rise or fall, third session corrective")
    print("pre-registration: PT-046_two_sessions_then_a_corrective_third.md @ c1cb2c7")
    print("=" * 78)

    L.qa_gate()
    results = {}

    for label, scope in (("W-D", "development"), ("W-E", "extended")):
        for arm in ARMS:
            key = f"{label}/{arm}"
            # `assert_development` is a SEAL, not an inconvenience. If it fires we do
            # NOT weaken it to obtain a number -- we record the abort and move on.
            # (It fires on W-D arm B: the `I-010` Q2 DST relabelling, an OPEN OWNER
            # QUESTION documented in `mmm_lib.load_m1`'s docstring.)
            try:
                m, dirs, brk = run_one(arm, scope, label, BOUNDARY_DEFAULT)
            except SystemExit as e:
                print(f"\n{'-'*78}\n{key}   ** NOT RUN **")
                print(f"  {e}")
                print("  The DEVELOPMENT seal fired and was NOT overridden. See "
                      "BT_V18_0001.md §5 and `I-010` Q2.")
                results[key] = dict(not_run=True, reason=str(e))
                continue
            n1 = n1_shuffle(dirs, brk, SEED + ARM_SEED[arm] + LABEL_SEED[label])

            # N3 boundary sensitivity
            sens = {}
            for bnd in BOUNDARY_VARIANTS:
                mm, _, _ = run_one(arm, scope, label, bnd)
                sens[bnd] = mm["O3"]
            signs = {np.sign(round(v, 4)) for v in sens.values()}
            decisions = {verdict(sens[b], n1["percentile"], False) for b in sens}
            flipped = len(signs) > 1 or len(decisions) > 1

            # N5 adjacency artefact control
            m5, _, _ = run_one(arm, scope, label, BOUNDARY_DEFAULT, bridge_gaps=True)

            v = verdict(m["O3"], n1["percentile"], flipped)
            results[key] = dict(primary=m, n1=n1, n3=sens, n3_flipped=bool(flipped),
                                n5=m5, verdict=v)

            print(f"\n{'-'*78}\n{key}   boundary {BOUNDARY_DEFAULT//60:02d}:00")
            print(f"  sessions {m['n_sessions']}  days {m['n_days_total']} "
                  f"(excluded {m['n_excluded']})  zero-dir {m['n_zero']}")
            print(f"  O1 P(3rd corrects | 2 same) = {m['O1']:.4f}  "
                  f"({m['pair_corr']}/{m['pair_n']}, ties {m['pair_zero']})")
            print(f"  O2 base reversal rate       = {m['O2']:.4f}  "
                  f"({m['rev_k']}/{m['rev_n']})")
            print(f"  O3 LIFT                     = {m['O3']:+.4f}")
            print(f"  O4 P(4th resumes)           = {m['O4']:.4f}  (n={m['quad_n']}) "
                  f"[descriptive only]")
            print(f"  O5 run median {m['run_median']:.1f}  mode {m['run_mode']}  "
                  f"hist {m['run_hist']}")
            print(f"  N1 shuffle: mean O3 {n1['mean']:+.4f} sd {n1['sd']:.4f}  "
                  f"p95 {n1['p95']:+.4f}  observed percentile {n1['percentile']:.1f}")
            print(f"  N2 geometric expectation (mode 1 under i.i.d.): "
                  f"{geometric_expectation(m['run_hist'], sum(m['run_hist'].values()))}")
            print("  N3 boundary sensitivity: " +
                  "  ".join(f"{b//60:02d}:00 O3={sens[b]:+.4f}" for b in BOUNDARY_VARIANTS) +
                  f"   FLIPPED={flipped}")
            print(f"  N5 bridging gaps (artefact control): O3={m5['O3']:+.4f} "
                  f"median run {m5['run_median']:.1f}  [reported, NOT substituted]")
            print(f"  VERDICT: {v}")

    with open("../V18/data/pt046_results.json", "w") as f:
        json.dump(results, f, indent=2, default=float)
    print("\nwrote ../V18/data/pt046_results.json")


if __name__ == "__main__":
    main()
