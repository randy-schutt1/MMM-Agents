#!/usr/bin/env python3
"""REVIEWER-INDEPENDENT re-implementation of PT-047 (V19 R1).

Written from
`06_MANUAL_BACKTEST/PRE_REGISTERED/PT-047_the_second_leg_time_cap_and_the_extension.md`
§3-§5 ONLY. `run_pt047.py` was read for the reproduction check that precedes this
file, but nothing in this implementation is copied from it: the event scan is
vectorised per day rather than looped, the classifier is expressed as a close-count,
the permutation uses a DIFFERENT SEED, and a rank test is added that the student's
runner does not contain.

`mmm_lib` is used for corpus loading, the arm clocks and the C-1..C-6 calendar only.
That layer is shared infrastructure, checksummed by `qa_gate()` and audited in earlier
rounds; re-deriving it here would test the vendor CSVs, not PT-047.

Beyond replication this file runs the four probes the review needs:

  P1  a 60-MINUTE cap arm            -- REVIEW_INDEX item 290 asks for it by name
  P2  MAX_AGE sensitivity            -- PT-047 §6 attack 2 (the >=24 bound is convention)
  P3  every event per day, not first -- PT-047 §6 attack 3
  P4  Mann-Whitney U on O1           -- a test of the whole distribution, not the median
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mmm_lib as M                                                   # noqa: E402

HORIZON = 16
BAND = (25.0, 50.0)
DELTA_FLOOR = 10.0
REV_SEED = 77190419          # deliberately NOT mmm_lib.SEED
ITERS = 10000


def day_slices(arm, win):
    """Yield (day, high, low, close) for each C-6-complete session day's post-box bars."""
    m15 = M.window(M.load_m15(arm), win)
    days = M.build_days(m15, offset_min=0, require_full=True)
    post = (m15.mod >= M.BOX_END_MIN) & (m15.mod < M.DAY_END_MIN)
    for day in sorted(days["sd"].tolist()):
        m = post & (m15.sd == day)
        yield day, m15.h[m], m15.l[m], m15.c[m]
    yield None, int(len(days)), int(days.attrs["n_excluded_incomplete"]), None


def scan(arm, win, cap, min_age=8, max_age=24, first_only=True, out_from=1):
    """PT-047 §3. Vectorised: cummax gives R(t), argmax-of-tie gives a(t)."""
    held, back, meta = [], [], {}
    for day, h, l, c in day_slices(arm, win):
        if day is None:
            meta = dict(n_days=h, n_excluded=l)
            continue
        n = len(h)
        if n < min_age + 1 + HORIZON:
            continue
        # R(t) = running high strictly before t; a(t) = index that set it
        prev_max = np.maximum.accumulate(h)[:-1]          # R over bars <= t-1
        R = np.concatenate([[-np.inf], prev_max])         # R(t), aligned to t
        anchor = np.zeros(n, dtype=int)
        cur, ai = -np.inf, -1
        for t in range(n):                                # anchor is inherently serial
            anchor[t] = ai
            if h[t] > cur:
                cur, ai = h[t], t
        age = np.arange(n) - anchor
        elig = (h > R) & (age >= min_age) & (age <= max_age) & \
               (np.arange(n) + HORIZON < n) & np.isfinite(R)
        idx = np.flatnonzero(elig)
        if first_only:
            idx = idx[:1]
        for t in idx:
            L = float(R[t])
            # classifier: how many of the next `cap` closes sit below L
            n_below = int(np.count_nonzero(c[t + 1:t + 1 + cap] < L))
            o1 = max(0.0, (float(h[t + out_from:t + 1 + HORIZON].max()) - L) / M.PIP)
            (back if n_below > 0 else held).append(o1)
    return np.asarray(held, float), np.asarray(back, float), meta


def perm(a, b, seed=REV_SEED, iters=ITERS):
    obs = float(np.median(a) - np.median(b))
    pool = np.concatenate([a, b])
    na, rng, hits = len(a), np.random.default_rng(seed), 0
    for _ in range(iters):
        p = rng.permutation(pool)
        if float(np.median(p[:na]) - np.median(p[na:])) >= obs:
            hits += 1
    return obs, (hits + 1) / (iters + 1)


def mwu(a, b):
    """Mann-Whitney U, normal approximation with tie correction. Two-sided p."""
    n1, n2 = len(a), len(b)
    allv = np.concatenate([a, b])
    order = np.argsort(allv, kind="mergesort")
    ranks = np.empty(len(allv), float)
    sv = allv[order]
    i = 0
    while i < len(sv):
        j = i
        while j + 1 < len(sv) and sv[j + 1] == sv[i]:
            j += 1
        ranks[order[i:j + 1]] = (i + j) / 2.0 + 1.0
        i = j + 1
    R1 = ranks[:n1].sum()
    U = R1 - n1 * (n1 + 1) / 2.0
    mu = n1 * n2 / 2.0
    _, cnt = np.unique(allv, return_counts=True)
    tie = (cnt ** 3 - cnt).sum()
    N = n1 + n2
    sd = np.sqrt(n1 * n2 / 12.0 * ((N + 1) - tie / (N * (N - 1))))
    z = (U - mu) / sd
    from math import erfc, sqrt
    return U, z, erfc(abs(z) / sqrt(2))


def boot_ci(a, b, seed=REV_SEED, iters=5000):
    rng = np.random.default_rng(seed)
    d = [np.median(rng.choice(a, len(a), True)) - np.median(rng.choice(b, len(b), True))
         for _ in range(iters)]
    return float(np.percentile(d, 2.5)), float(np.percentile(d, 97.5))


def line(tag, held, back, extra=""):
    if len(held) < 2 or len(back) < 2:
        print(f"{tag:>26}  INSUFFICIENT nH={len(held)} nB={len(back)}")
        return None
    d, p = perm(held, back)
    print(f"{tag:>26}  nH={len(held):>4} nB={len(back):>4}  "
          f"medH={np.median(held):6.2f} medB={np.median(back):6.2f}  "
          f"D={d:6.2f}  p={p:.4f}  {extra}")
    return d, p


def main():
    M.qa_gate()

    print("=" * 100)
    print("REPLICATION -- PT-047 §3/§5 re-implemented, reviewer seed", REV_SEED)
    print("=" * 100)
    prim = None
    for arm in ("A", "B"):
        for win in ("W-A", "W-B"):
            for cap in (2, 3):
                held, back, meta = scan(arm, win, cap)
                r = line(f"{arm}|{win}|{cap*15}m", held, back,
                         f"days={meta['n_days']} excl={meta['n_excluded']}")
                if (arm, win, cap) == ("A", "W-A", 2):
                    prim = (held, back, r)

    held, back, r = prim
    d, p = r
    lo, hi = boot_ci(held, back)
    U, z, pm = mwu(held, back)
    print(f"\nPRIMARY CELL A|W-A|30m")
    print(f"  delta                    {d:.2f} pips   (floor {DELTA_FLOOR})")
    print(f"  median O1 HELD           {np.median(held):.2f}  in band {BAND}: "
          f"{BAND[0] <= np.median(held) <= BAND[1]}")
    print(f"  permutation p            {p:.4f}")
    print(f"  P4 Mann-Whitney U        U={U:.0f}  z={z:.3f}  two-sided p={pm:.2e}")
    print(f"  bootstrap 95% CI on D    [{lo:.2f}, {hi:.2f}] pips")
    print(f"  mean O1  HELD/BACK       {held.mean():.2f} / {back.mean():.2f}")

    print("\n" + "=" * 100)
    print("P1 -- THE 60-MINUTE ARM (REVIEW_INDEX item 290). N3 fires if any group n<30.")
    print("=" * 100)
    for arm in ("A", "B"):
        for win in ("W-A", "W-B"):
            for cap in (2, 3, 4):
                held, back, _ = scan(arm, win, cap)
                flag = "  <-- N3 n<30 WOULD FIRE" if min(len(held), len(back)) < 30 else ""
                line(f"{arm}|{win}|{cap*15}m", held, back, flag)

    print("\n" + "=" * 100)
    print("P2 -- MAX_AGE SENSITIVITY (PT-047 §6 attack 2). Primary arm/window, cap=2.")
    print("=" * 100)
    for ma in (12, 16, 20, 24, 32, 48, 10 ** 6):
        held, back, _ = scan("A", "W-A", 2, max_age=ma)
        line(f"max_age={ma if ma < 10**6 else 'none'}", held, back)

    print("\n" + "=" * 100)
    print("P3 -- EVERY EVENT PER DAY, NOT THE FIRST (PT-047 §6 attack 3). cap=2.")
    print("=" * 100)
    for arm in ("A", "B"):
        for win in ("W-A", "W-B"):
            held, back, _ = scan(arm, win, 2, first_only=False)
            line(f"{arm}|{win}|all-events", held, back)

    print("\n" + "=" * 100)
    print("DISJOINT-WINDOW CHECK (BT_V19_0001 §4), re-implemented: O1 over t+3..t+16.")
    print("=" * 100)
    for arm in ("A", "B"):
        for win in ("W-A", "W-B"):
            held, back, _ = scan(arm, win, 2, out_from=3)
            line(f"{arm}|{win}|disjoint", held, back)


if __name__ == "__main__":
    main()
