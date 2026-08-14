#!/usr/bin/env python3
"""PT-039 -- V11's hold-duration claim: "the low has to hold -- how long? 30 to 90 minutes".

Runs the design pre-registered in
`06_MANUAL_BACKTEST/PRE_REGISTERED/PT-039_how_long_must_the_low_hold.md`,
which was committed at `beee96a`, BEFORE this file existed and before any bar was read.

`COMMON_PROTOCOL.md` §9 rule 7: if this runner and that pre-registration disagree,
THE PRE-REGISTRATION GOVERNS and neither file is edited -- the disagreement is
reported in `BT_V11_0001.md`.

Everything here reads M1 bars parsed from the checksummed HistData corpus (`D-036a`).
No value is read from a rendering of any kind.

usage:  python3 run_pt039.py > ../V11/data/pt039_output.txt
"""
from __future__ import annotations

import numpy as np

import mmm_lib as L

SEED = 20260813          # PT-039 §4, recorded before the run
ITERATIONS = 1000        # D-029
THRESHOLDS = [5, 10, 15, 30, 45, 60, 90, 120, 180, 240]   # §3.2 O1
NAMED = {30, 90, 120}                                     # §1 -- 120 is the agent's extension
UNNAMED = [t for t in THRESHOLDS if t not in NAMED]       # §4 N2
STRATA = [(0, 240), (240, 480), (480, 720), (720, 960), (960, 1200), (1200, 1440)]

# W-C' = D-035's DEVELOPMENT block exactly. Not in mmm_lib.WINDOWS; stated here.
WC_PRIME = (L.DEV_START, L.DEV_END)

BUCKETS_PER_DAY = 96     # §7a: all 96 fifteen-minute buckets must be present


def wcp(b: L.Bars) -> L.Bars:
    """Slice to W-C' and re-assert the D-035 holdout on every slice."""
    out = b.slice(*WC_PRIME)
    L.assert_development(out.tm, f"W-C' / arm {b.arm}")
    return out


# ----------------------------------------------------------------- construction

def session_days(b: L.Bars):
    """Included session days and their per-day M1 slices.

    Inclusion (§7a, the general form of convention C-6): all 96 fifteen-minute
    buckets of the day's 24-hour span present. Exclusions are counted and returned,
    never dropped quietly.
    """
    sd = L.session_day(b.tm)
    order = np.argsort(sd, kind="stable")
    sd_s = sd[order]
    uniq, starts, counts = np.unique(sd_s, return_index=True, return_counts=True)

    kept, excluded = [], []
    for d, s, n in zip(uniq, starts, counts):
        idx = order[s:s + n]
        idx = idx[np.argsort(b.tm[idx], kind="stable")]
        tm = b.tm[idx]
        # session start = the day's 17:00 boundary of D-1
        end = (d * L.DAY) + L.DAY_END_MIN          # D 17:00
        start = end - L.DAY
        nb = len(np.unique((tm - start) // 15))
        if nb == BUCKETS_PER_DAY:
            kept.append((int(d), idx, int(start), int(end)))
        else:
            excluded.append((int(d), nb))
    return kept, excluded


def candidates(v: np.ndarray, tm: np.ndarray, end: int, side: str) -> np.ndarray:
    """Running-extreme events for one session day, vectorised.

    Columns: (t_candidate, delta_or_-1, is_final, remaining). `delta = -1` marks a
    candidate never superseded, i.e. the FINAL one -- exactly one per day.

    `np.minimum.accumulate` changes value ONLY on a STRICTLY lower low, so
    `run[i] != run[i-1]` is exactly the pre-registered "strictly below the running
    minimum" test (§3.0). Vectorised because N4 runs this 1,000 times over ~900
    session days; the scalar version made the null computationally infeasible, which
    would have meant silently dropping a pre-registered control.
    """
    run = np.minimum.accumulate(v) if side == "low" else np.maximum.accumulate(v)
    is_new = np.empty(len(v), dtype=bool)
    is_new[0] = True
    is_new[1:] = run[1:] != run[:-1]
    idxs = np.flatnonzero(is_new)

    t = tm[idxs].astype(np.int64)
    delta = np.full(len(idxs), -1, dtype=np.int64)
    if len(idxs) > 1:
        delta[:-1] = t[1:] - t[:-1]
    final = np.zeros(len(idxs), dtype=np.int64)
    final[-1] = 1
    return np.column_stack([t, delta, final, end - t])


def harvest(arm: str, side: str):
    b = wcp(L.load_m1(arm))
    days, excluded = session_days(b)
    parts = []
    for d, idx, start, end in days:
        v = b.l[idx] if side == "low" else b.h[idx]
        parts.append(candidates(v, b.tm[idx], end, side))
    return np.vstack(parts), len(days), excluded


# ----------------------------------------------------------------- estimation

def curve(rows: np.ndarray, T: int):
    """§3.1. Eligible iff R >= T. held(T) iff (superseded and delta >= T) or final."""
    t, delta, final, rem = rows[:, 0], rows[:, 1], rows[:, 2].astype(bool), rows[:, 3]
    elig = rem >= T
    held = elig & (final | (delta >= T))
    k = int((held & final).sum())
    n = int(held.sum())
    return k, n, int(elig.sum())


def wilson(k, n):
    return L.wilson_ci(k, n) if n else (float("nan"), float("nan"))


def rate_line(k, n, extra=""):
    if n == 0:
        return "     n=0   --"
    lo, hi = wilson(k, n)
    lab = "" if n >= 30 else "  [SAMPLE INSUFFICIENT FOR INFERENCE -- descriptive only]"
    return f"{100*k/n:6.2f}%  (k={k:6d}  n={n:6d}  95% CI {100*lo:5.2f}-{100*hi:5.2f}){extra}{lab}"


def main():
    print(L.header("PT-039", "V11 -- how long must the low hold? 30 / 90 / 120 minutes",
                   "D-031: BOTH arms reported for every observable (binding)"))
    qa_txt, _ = L.qa_gate()   # raises unless "GATE: PASS" -- §7b.4
    print("QA GATE (precondition, D-036a): " +
          [l for l in qa_txt.splitlines() if l.startswith("GATE:")][0])
    print(f"WINDOW  W-C' = {L.m2s(WC_PRIME[0])} -> {L.m2s(WC_PRIME[1])}  (D-035 DEVELOPMENT)")
    print(f"HOLDOUT 2016-07-01 -> 2017-12-29  NOT OPENED (not on disk; assert_development re-checks)")
    print(f"SEED {SEED}   ITERATIONS {ITERATIONS}   TIMEFRAME M1")
    print()

    store = {}
    for arm in ("A", "B"):
        for side in ("low", "high"):
            rows, ndays, excl = harvest(arm, side)
            store[(arm, side)] = (rows, ndays, excl)

    # ---- VOID checks (§7b), run before anything is reported
    print("=" * 78)
    print("  §7b VOID CHECKS")
    print("=" * 78)
    for (arm, side), (rows, ndays, excl) in store.items():
        finals = int(rows[:, 2].sum())
        unresolved = 0                      # by construction: final or superseded
        assert finals == ndays, f"{arm}/{side}: {finals} finals vs {ndays} days"
        print(f"  arm {arm} {side:<4}  session days {ndays:5d}   FINAL candidates {finals:5d}"
              f"   unresolved {unresolved}   -> OK")
    print(f"  eligibility rule: no candidate enters a T-denominator with R < T -- enforced in curve()")
    print()

    # ---- completeness (§7a)
    print("=" * 78)
    print("  §7a INCLUSION / COMPLETENESS -- counts reported beside every n")
    print("=" * 78)
    for arm in ("A", "B"):
        rows, ndays, excl = store[(arm, "low")]
        print(f"  arm {arm}: INCLUDED {ndays} session days;  EXCLUDED {len(excl)} "
              f"(fewer than {BUCKETS_PER_DAY}/96 fifteen-minute buckets present)")
        named = [f"{L.day2s(d)}({nb}/96)" for d, nb in excl[:12]]
        print(f"          first excluded: {', '.join(named)}")
        hole = [d for d, _ in excl if L.day2s(d) in ("2014-06-01", "2014-06-02")]
        print(f"          the D-036a C8 data hole (2014-06-01/02) excluded by name: "
              f"{'YES -- ' + ', '.join(L.day2s(d) for d in hole) if hole else 'NOT PRESENT IN EXCLUSION LIST -- INVESTIGATE'}")
    print()

    # ---- O4 base rate
    print("=" * 78)
    print("  O4 -- CANDIDATES PER SESSION DAY   (fixes N1, the unconditional base rate)")
    print("=" * 78)
    for arm in ("A", "B"):
        for side in ("low", "high"):
            rows, ndays, _ = store[(arm, side)]
            # count per day: finals delimit days, so count via cumulative final markers
            fin = np.flatnonzero(rows[:, 2] == 1)
            counts = np.diff(np.concatenate([[-1], fin]))
            print(f"  arm {arm} {side:<4}  n_days={ndays:5d}  median={np.median(counts):6.1f}  "
                  f"mean={counts.mean():6.2f}  q25={np.percentile(counts,25):5.1f}  "
                  f"q75={np.percentile(counts,75):5.1f}  min={counts.min()}  max={counts.max()}")
            print(f"              implied unconditional P(FINAL) = 1/mean = {100/counts.mean():5.2f}%")
    print()

    # ---- O1 / O2 / N1 / N2
    print("=" * 78)
    print("  O1 -- THE SURVIVAL-CONFIRMATION CURVE   P(FINAL | held >= T)")
    print("  N1 = the T=0 row (unconditional base rate).  * = a threshold the lesson NAMES.")
    print("  N2 = the unnamed rows, run alongside so a smooth rise is distinguishable")
    print("       from a feature at 30 / 90 / 120.")
    print("=" * 78)
    for arm in ("A", "B"):
        for side in ("low", "high"):
            rows = store[(arm, side)][0]
            k0, n0, _ = curve(rows, 0)
            base = 100 * k0 / n0
            print(f"\n  --- arm {arm}, {side} ---   N1 base rate {base:5.2f}%  (n={n0})")
            prev = base
            for T in THRESHOLDS:
                k, n, ne = curve(rows, T)
                r = 100 * k / n if n else float("nan")
                star = " *" if T in NAMED else "  "
                ext = " <- AGENT'S EXTENSION (O6)" if T == 120 else ""
                print(f"   T={T:4d}{star} {rate_line(k, n)}   d(prev)={r-prev:+6.2f}pp"
                      f"  margin_vs_N1={r-base:+6.2f}pp{ext}")
                prev = r
            store[(arm, side, "base")] = base
    print()

    # ---- O3 / O5
    print("=" * 78)
    print("  O3 -- HOLD-DURATION DISTRIBUTION OF SUPERSEDED CANDIDATES")
    print("  O5 -- where the NAMED numbers sit as percentiles of that distribution")
    print("=" * 78)
    for arm in ("A", "B"):
        for side in ("low", "high"):
            rows = store[(arm, side)][0]
            d = rows[rows[:, 1] >= 0][:, 1].astype(float)
            in_band = float(((d >= 30) & (d <= 90)).mean() * 100)
            print(f"\n  --- arm {arm}, {side} ---  n_superseded={len(d)}")
            print(f"    median={np.median(d):7.1f} min   mean={d.mean():7.1f}   "
                  f"p05={np.percentile(d,5):6.1f}  q25={np.percentile(d,25):6.1f}  "
                  f"q75={np.percentile(d,75):7.1f}  p95={np.percentile(d,95):7.1f}  max={d.max():7.0f}")
            print(f"    proportion of superseded holds falling in [30, 90] min: {in_band:5.2f}%   (P5 tests this)")
            for T in (30, 90, 120):
                pct = float((d < T).mean() * 100)
                print(f"    O5: T={T:4d} min sits at the {pct:5.2f}th percentile of superseded hold durations")
    print()

    # ---- N3 stratification
    print("=" * 78)
    print("  N3 -- TIME-OF-DAY STRATIFICATION   (the confound control; M1d's verdict comes from here)")
    print("  Strata are minute-of-day of the CANDIDATE on the arm's own clock.")
    print("=" * 78)
    for arm in ("A", "B"):
        for side in ("low",):     # M1d is defined on the low arm; high reported in O1
            rows = store[(arm, side)][0]
            mod = rows[:, 0] - (rows[:, 0] // L.DAY) * L.DAY
            print(f"\n  --- arm {arm}, {side} ---")
            for lo, hi in STRATA:
                m = (mod >= lo) & (mod < hi)
                sub = rows[m]
                if len(sub) == 0:
                    continue
                k0, n0, _ = curve(sub, 0)
                b30 = 100 * k0 / n0 if n0 else float("nan")
                k, n, _ = curve(sub, 30)
                r = 100 * k / n if n else float("nan")
                medR = float(np.median(sub[:, 3]))
                lab = "" if n >= 30 else "  [n<30 -- descriptive only]"
                print(f"    {lo//60:02d}:00-{hi//60:02d}:00  n_cand={len(sub):6d}  median R={medR:6.0f} min"
                      f"   N1={b30:5.2f}%   P(F|held>=30)={r:5.2f}%   margin={r-b30:+6.2f}pp{lab}")
    print()

    # ---- N4 circular clock shift
    print("=" * 78)
    print("  N4 -- CIRCULAR CLOCK SHIFT   (does the 17:00 session boundary matter at all?)")
    print(f"  {ITERATIONS} iterations, offsets uniform on +/-12h in 15-min steps, seed {SEED}")
    print("=" * 78)
    rng = np.random.default_rng(SEED)
    offsets = rng.choice(np.arange(-720, 721, 15), size=ITERATIONS)
    b = wcp(L.load_m1("A"))
    margins = []
    for off in offsets[:ITERATIONS]:
        tm2 = b.tm + int(off)
        sd = L.session_day(tm2)
        order = np.argsort(sd, kind="stable")
        sd_s = sd[order]
        uniq, starts, counts = np.unique(sd_s, return_index=True, return_counts=True)
        parts = []
        for d, st, n in zip(uniq, starts, counts):
            if n < 1200:            # shifted windows: skip obviously partial days
                continue
            idx = order[st:st + n]
            idx = idx[np.argsort(tm2[idx], kind="stable")]
            end = (d * L.DAY) + L.DAY_END_MIN
            parts.append(candidates(b.l[idx], tm2[idx], end, "low"))
        if not parts:
            continue
        rows = np.vstack(parts)
        k0, n0, _ = curve(rows, 0)
        k, n, _ = curve(rows, 30)
        if n0 and n:
            margins.append(100 * k / n - 100 * k0 / n0)
    margins = np.array(margins)
    rows = store[("A", "low")][0]
    k0, n0, _ = curve(rows, 0)
    k, n, _ = curve(rows, 30)
    true_margin = 100 * k / n - 100 * k0 / n0
    pct = float((margins < true_margin).mean() * 100)
    print(f"  true margin (arm A, low, T=30): {true_margin:+6.2f}pp")
    print(f"  shifted-boundary null: n={len(margins)}  median={np.median(margins):+6.2f}pp  "
          f"5-95% [{np.percentile(margins,5):+6.2f}, {np.percentile(margins,95):+6.2f}]")
    print(f"  the true margin sits at the {pct:5.2f}th percentile of the shifted-boundary null")
    print()

    # ---- N2 feature test (M1c)
    print("=" * 78)
    print("  M1c FEATURE TEST -- is there anything AT 30 or AT 90, versus the unnamed neighbours?")
    print("  A named T* shows a FEATURE if its per-minute increment exceeds the mean per-minute")
    print("  increment of the two adjacent UNNAMED intervals by >= 5pp scaled to interval width.")
    print("=" * 78)
    for arm in ("A", "B"):
        rows = store[(arm, "low")][0]
        vals = {}
        for T in [0] + THRESHOLDS:
            k, n, _ = curve(rows, T)
            vals[T] = 100 * k / n if n else float("nan")
        seq = [0] + THRESHOLDS
        per_min = {}
        for i in range(1, len(seq)):
            w = seq[i] - seq[i - 1]
            per_min[seq[i]] = (vals[seq[i]] - vals[seq[i - 1]]) / w
        print(f"\n  --- arm {arm}, low ---")
        for T in (30, 90):
            i = seq.index(T)
            nb = [seq[j] for j in (i - 1, i + 1) if 0 < j < len(seq) and seq[j] not in NAMED]
            if not nb:
                print(f"    T={T}: no unnamed neighbour available"); continue
            ref = np.mean([per_min[x] for x in nb])
            w = T - seq[i - 1]
            excess = (per_min[T] - ref) * w
            verdict = "FEATURE" if excess >= 5.0 else "no feature"
            print(f"    T={T:3d}: own {per_min[T]:+7.4f} pp/min   unnamed neighbours {nb} "
                  f"mean {ref:+7.4f} pp/min   excess over interval = {excess:+6.2f}pp   -> {verdict}")
    print()

    print("=" * 78)
    print("  END. Verdicts against §6's fixed thresholds are recorded in")
    print("  06_MANUAL_BACKTEST/V11/BT_V11_0001.md, not here. This runner reports numbers.")
    print("=" * 78)


if __name__ == "__main__":
    main()
