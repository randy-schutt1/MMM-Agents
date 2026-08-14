#!/usr/bin/env python3
"""PT-042 — "the lock": does a session extreme that holds one hour become the day's extreme?

Pre-registration: `PRE_REGISTERED/PT-042_the_lock_and_the_high_low_board.md`
The pre-registration was committed BEFORE this file existed; verify with
    git log --diff-filter=A --format=%H -- 06_MANUAL_BACKTEST/scripts/run_pt042.py
    git log --diff-filter=A --format=%H -- 06_MANUAL_BACKTEST/PRE_REGISTERED/PT-042_*.md

V14, PRINTED on the assignment slide:
  "At 1am NYC time record the high and low of the majors / Find a pair that is
   trading in the middle of the range / Wait for the dealer to extend either level
   mark it down ... / When the dealer pulls off of the level and fails to hit it
   again for 1 hour take a position / Stop loss level is 5 pips above/ below that
   number that appears on the board."
and spoken, the two figures the slide omits:
  [00:27:28] "Identify the pairs that have not made more than a 50 pip range."
  [00:32:38] "Let it run, aim for 30 to 50 pips."
the premise, stated strongest at [00:37:53]:
  "the strongest resistance in the day is 32 30. It's the high of the day."

BINDING CAVEATS (`PT-042` §1a), reproduced because a reader of the OUTPUT must see
them without opening the pre-registration:

  1. THIS TESTS A DRILL'S OWN CLAIM, NOT ADOPTED DOCTRINE. [00:32:42] "That's a
     drill"; [00:32:25] "in demo". The 5-pip stop and 30-pip target appear NOWHERE
     in 12_MASTER_SPEC/ or 13_MACHINE_SPEC/. This is the A-082 class of error and it
     is fenced in advance.
  2. ONE OF THE COURSE'S SIX STEPS IS EXCLUDED UNDER D-030. "Trading in the middle
     of the range" has no tolerance in Tier 1 or Tier 2 and the speaker's own two
     examples sit at the 45.5th and 20.0th percentile (A-089). Excluding it makes
     the population LARGER and LESS SELECTIVE than the course intends, so every
     figure here is a LOWER BOUND on the rule as taught.
  3. The course says "the majors"; this is GBP/USD only (D-007). The cross-sectional
     pick is part of the method and is not tested.
  4. The board is a TICK object; M1 is a proxy. Biases toward fewer stopwatch resets,
     i.e. locks firing slightly EARLIER than a tick board would show.
  5. No spread, commission or slippage. Distances only. A 5-pip stop sits inside a
     realistic 2012 GBP/USD spread band.

usage: python3 run_pt042.py
"""
import json
import os

import numpy as np

import mmm_lib as L

OUT_DIR = os.path.join(L.ROOT, "06_MANUAL_BACKTEST", "V14", "data")

T0_MIN = 60                  # C-2  01:00 on the arm's clock
DAY_END = L.DAY_END_MIN      # C-1  17:00
MAX_RANGE = 50.0             # F1   board range <= 50 pips, inclusive
LOCK_MIN = 60                # C-7  the PRINTED figure. No sweep -- see PT-042 s8.6
STOP_PIPS = 5.0              # C-11 printed
TGT_PIPS = 30.0              # C-12 low end of "30 to 50"
TGT_HI = 50.0                # O3   reported, not in the verdict
S1_OFFSET = 10.0             # S1   [00:32:25] "at about 61 15" against a 61 05 lock
MIN_POST_FRAC = 0.90         # C-14 completeness on the post-T0 leg

B_O1, B_O2, B_N = 0.80, 0.50, 30     # s6 -- fixed in the pre-registration


def _pips(x):
    return x / L.PIP


def build(m1, log):
    """Return per-session-day records. All of C-1..C-14."""
    tm, hi, lo, cl = m1.tm, m1.h, m1.l, m1.c
    day = L.session_day(tm)
    mod = L.minute_of_day(tm)
    # minutes since session-day start (17:00 of D-1)
    since = np.where(mod >= DAY_END, mod - DAY_END, mod + (1440 - DAY_END))
    t0_since = T0_MIN + (1440 - DAY_END)          # 01:00 is this far into the day
    end_since = 1440                              # 17:00 next

    recs, excl = [], []
    uniq = np.unique(day)
    order = np.argsort(day, kind="stable")
    day_s, idx_s = day[order], order
    bounds = np.searchsorted(day_s, uniq)
    bounds = np.append(bounds, len(day_s))

    for k, d in enumerate(uniq):
        ii = idx_s[bounds[k]:bounds[k + 1]]
        if len(ii) == 0:
            continue
        s = since[ii]
        pre = ii[s <= t0_since]
        post = ii[(s > t0_since) & (s < end_since)]
        # ---- C-14 completeness -------------------------------------------------
        if len(pre) == 0 or len(post) == 0:
            excl.append((L.day2s(d), "empty leg", len(pre), len(post)))
            continue
        pre_hours = np.unique(s[s <= t0_since] // 60)
        need_hours = int(np.ceil(t0_since / 60))
        if len(pre_hours) < need_hours:
            excl.append((L.day2s(d), "pre-T0 hour gap",
                         len(pre_hours), need_hours))
            continue
        exp_post = end_since - t0_since
        if len(post) < MIN_POST_FRAC * exp_post:
            excl.append((L.day2s(d), "post-T0 <90%", len(post), int(exp_post)))
            continue
        # ---- C-3 board range ---------------------------------------------------
        bh, bl = hi[pre].max(), lo[pre].min()
        rng = _pips(bh - bl)
        # order the post leg by time
        po = post[np.argsort(tm[post], kind="stable")]
        recs.append(dict(day=int(d), bh=float(bh), bl=float(bl), rng=float(rng),
                         post=po))
    return recs, excl


def run_day(r, m1):
    """C-4..C-13 for one session day. Returns a dict or None (no extension)."""
    hi, lo, cl, tm = m1.h, m1.l, m1.c, m1.tm
    po = r["post"]
    H, Lo, C = hi[po], lo[po], cl[po]
    up = H > r["bh"]
    dn = Lo < r["bl"]
    iu = int(np.argmax(up)) if up.any() else None
    idn = int(np.argmax(dn)) if dn.any() else None
    if iu is None and idn is None:
        return dict(status="no-extension")
    if iu is not None and idn is not None and iu == idn:
        return dict(status="ambiguous-bar")          # C-4 exclusion
    if idn is None or (iu is not None and iu < idn):
        direction, i0 = +1, iu                        # UP extension -> SHORT
    else:
        direction, i0 = -1, idn                       # DOWN extension -> LONG

    # ---- C-5/C-6/C-7 running extreme + stopwatch ------------------------------
    n = len(po)
    if direction > 0:
        ext = H[i0]
    else:
        ext = Lo[i0]
    last_new = i0
    lock_i = None
    for i in range(i0 + 1, n):
        newer = (H[i] > ext) if direction > 0 else (Lo[i] < ext)
        if newer:
            ext = H[i] if direction > 0 else Lo[i]
            last_new = i
            continue
        if (i - last_new) >= LOCK_MIN:               # C-7, minutes == bars on M1
            lock_i = i
            break

    # session extreme over the WHOLE post leg, for O1
    sess_ext = float(H.max()) if direction > 0 else float(Lo.min())

    if lock_i is None:
        # C-8 no lock before 17:00 -> N4 natural control population
        held = (sess_ext <= ext) if direction > 0 else (sess_ext >= ext)
        return dict(status="no-lock", direction=direction, L=float(ext),
                    o1=bool(held), t_lock=None)

    Lv = float(ext)
    entry = float(C[lock_i])
    stop = Lv + STOP_PIPS * L.PIP if direction > 0 else Lv - STOP_PIPS * L.PIP
    # O1 -- is L still the day's extreme at 17:00?
    held = (sess_ext <= Lv) if direction > 0 else (sess_ext >= Lv)

    o2, o3, mfe = resolve(H, Lo, lock_i + 1, n, direction, entry, stop)
    # S1 -- limit 10 pips inside L
    lim = Lv - S1_OFFSET * L.PIP if direction > 0 else Lv + S1_OFFSET * L.PIP
    s1 = s1_arm(H, Lo, lock_i + 1, n, direction, lim, stop)

    return dict(status="lock", direction=direction, L=Lv, entry=entry,
                stop=stop, o1=bool(held), o2=o2, o3=o3, mfe=float(mfe),
                t_lock=int(lock_i), s1=s1)


def _first(mask):
    """Index of the first True, or None. O(n) numpy, no Python loop."""
    if not mask.any():
        return None
    return int(np.argmax(mask))


def resolve(H, Lo, i, n, direction, entry, stop):
    """C-13. Walk forward to 17:00. STOP WINS A SAME-BAR TIE (fixed in the
    pre-registration, not after seeing how often it happens).

    Vectorised. Identical semantics to a bar-by-bar walk: `first index where`
    is exactly what argmax-over-boolean returns, and the tie rule is applied by
    comparing indices with `<` (target must be STRICTLY earlier than the stop).
    Returns (hit30, hit50, mfe_full_ignoring_the_stop).
    """
    if i >= n:
        return False, False, 0.0
    h, l = H[i:n], Lo[i:n]
    if direction > 0:                                   # SHORT
        i_stop = _first(h >= stop)
        i_30 = _first(l <= entry - TGT_PIPS * L.PIP)
        i_50 = _first(l <= entry - TGT_HI * L.PIP)
        mfe_full = _pips(entry - l.min())
    else:                                               # LONG
        i_stop = _first(l <= stop)
        i_30 = _first(h >= entry + TGT_PIPS * L.PIP)
        i_50 = _first(h >= entry + TGT_HI * L.PIP)
        mfe_full = _pips(h.max() - entry)
    s = np.inf if i_stop is None else i_stop
    hit30 = i_30 is not None and i_30 < s
    hit50 = i_50 is not None and i_50 < s
    return bool(hit30), bool(hit50), float(mfe_full)


def s1_arm(H, Lo, i, n, direction, lim, stop):
    """S1 -- limit entry `S1_OFFSET` pips inside L (`A-090`). The FILL is reported
    separately from the outcome, because an unfilled limit is not a winning trade.
    A fill counts only if it happens strictly before the stop."""
    if i >= n:
        return dict(filled=False, o2=None)
    h, l = H[i:n], Lo[i:n]
    if direction > 0:
        i_stop = _first(h >= stop)
        i_fill = _first(h >= lim)
    else:
        i_stop = _first(l <= stop)
        i_fill = _first(l <= lim)
    s = np.inf if i_stop is None else i_stop
    if i_fill is None or i_fill >= s:
        return dict(filled=False, o2=None)
    o2, _, _ = resolve(H, Lo, i + i_fill + 1, n, direction, lim, stop)
    return dict(filled=True, o2=bool(o2))


def n1_control(recs, results, m1, log, seed=L.SEED, iters=1000):
    """N1 -- matched random entry (D-026). Same days, same eligible window,
    same 5-pip-equivalent stop geometry and 30-pip target, RANDOM direction and
    RANDOM entry bar, n matched. Reports the SAME statistics as the rule arm
    (V13 R1 M2)."""
    rng = np.random.default_rng(seed)
    hi, lo, cl = m1.h, m1.l, m1.c
    locked = [r for r, o in zip(recs, results) if o["status"] == "lock"]
    n = len(locked)
    if n == 0:
        return None
    o1s, o2s, o3s, mfes = [], [], [], []
    for _ in range(iters):
        a1 = a2 = a3 = 0
        mf = []
        for _ in range(n):
            r = locked[rng.integers(0, n)]
            po = r["post"]
            m = len(po)
            if m < 90:
                continue
            j = int(rng.integers(0, m - 60))
            d = 1 if rng.integers(0, 2) else -1
            H, Lo, C = hi[po], lo[po], cl[po]
            entry = float(C[j])
            # synthetic "L" 5 pips beyond entry-adjacent extreme, matching geometry:
            Lv = entry + 10.0 * L.PIP if d > 0 else entry - 10.0 * L.PIP
            stop = Lv + STOP_PIPS * L.PIP if d > 0 else Lv - STOP_PIPS * L.PIP
            sess = float(H[j:].max()) if d > 0 else float(Lo[j:].min())
            held = (sess <= Lv) if d > 0 else (sess >= Lv)
            a1 += held
            h30, h50, mfe = resolve(H, Lo, j + 1, m, d, entry, stop)
            a2 += h30
            a3 += h50
            mf.append(mfe)
        o1s.append(a1 / n); o2s.append(a2 / n); o3s.append(a3 / n)
        mfes.append(float(np.median(mf)) if mf else np.nan)
    return dict(o1=float(np.median(o1s)), o2=float(np.median(o2s)),
                o3=float(np.median(o3s)), mfe=float(np.nanmedian(mfes)),
                o1d=o1s, o2d=o2s)


def run_arm(arm, log):
    log("")
    log("=" * 78)
    log(f"ARM {arm}   ({'fixed UTC-5' if arm == 'A' else 'America/New_York, DST-aware'})")
    log("=" * 78)
    m1 = L.window(L.load_m1(arm), "W-B")
    log(f"  M1 bars in W-B: {len(m1):,}")

    recs, excl = build(m1, log)
    log(f"  session days with both legs present : {len(recs) + 0:,}")
    log(f"  days EXCLUDED by C-14 completeness  : {len(excl)}")
    for e in excl[:8]:
        log(f"      {e[0]}  {e[1]}  ({e[2]} / {e[3]})")
    if len(excl) > 8:
        log(f"      ... and {len(excl) - 8} more")

    # ---- F1 --------------------------------------------------------------------
    f1 = [r for r in recs if r["rng"] <= MAX_RANGE]
    log(f"  F1  board range <= {MAX_RANGE:.0f} pips : {len(f1)} of {len(recs)}"
        f"  ({100.0 * len(f1) / max(1, len(recs)):.1f}%)")

    results = [run_day(r, m1) for r in f1]
    from collections import Counter
    cnt = Counter(o["status"] for o in results)
    log(f"  statuses: {dict(cnt)}")

    locks = [o for o in results if o["status"] == "lock"]
    nolock = [o for o in results if o["status"] == "no-lock"]
    n = len(locks)

    # ---- CONTROLS FIRST (COMMON_PROTOCOL s9.1) ---------------------------------
    log("")
    log("  --- CONTROLS, computed BEFORE the rule arm's aggregate is printed ---")
    n1 = n1_control(f1, results, m1, log)
    if n1:
        log(f"  N1 matched-random  O1={n1['o1']:.4f}  O2={n1['o2']:.4f}"
            f"  O3={n1['o3']:.4f}  medMFE={n1['mfe']:.2f}   (1000 iters, seed {L.SEED})")
    n4_o1 = float(np.mean([o["o1"] for o in nolock])) if nolock else float("nan")
    log(f"  N4 natural (no-lock days, n={len(nolock)})  O1={n4_o1:.4f}"
        "   <- extended but never locked")

    if n < B_N:
        log(f"  !! n = {n} < {B_N} -- SAMPLE INSUFFICIENT FOR INFERENCE, descriptive only")

    o1 = float(np.mean([o["o1"] for o in locks])) if n else float("nan")
    o2 = float(np.mean([o["o2"] for o in locks])) if n else float("nan")
    o3 = float(np.mean([o["o3"] for o in locks])) if n else float("nan")
    o4 = float(np.median([o["mfe"] for o in locks])) if n else float("nan")
    o5 = float(np.median([o["t_lock"] for o in locks])) if n else float("nan")
    s1f = [o["s1"] for o in locks]
    fill = float(np.mean([s["filled"] for s in s1f])) if n else float("nan")
    s1o2 = [s["o2"] for s in s1f if s["filled"]]
    o6 = float(np.mean(s1o2)) if s1o2 else float("nan")

    log("")
    log("  --- RULE ARM ---")
    log(f"  n (locks fired)                      : {n}")
    log(f"  O1  P(L is still the day's extreme)  : {o1:.4f}   {L.wilson_ci(int(round(o1*n)), n)}")
    log(f"  O2  P(30 pips before the 5-pip stop) : {o2:.4f}   {L.wilson_ci(int(round(o2*n)), n)}")
    log(f"  O3  P(50 pips before the stop)       : {o3:.4f}")
    log(f"  O4  median MFE from entry (pips)     : {o4:.2f}")
    log(f"  O5  median minutes T0 -> lock        : {o5:.0f}")
    log(f"  O6  S1 limit 10 inside: fill={fill:.4f}  O2|filled={o6:.4f}  (n={len(s1o2)})")

    if n1:
        log(f"  O1 percentile vs N1: {L.percentile_of(o1, np.array(n1['o1d'])):.1f}")
        log(f"  O2 percentile vs N1: {L.percentile_of(o2, np.array(n1['o2d'])):.1f}")

    return dict(arm=arm, n=n, o1=o1, o2=o2, o3=o3, o4=o4, o5=o5,
                fill=fill, o6=o6, n1=(None if not n1 else
                                      {k: n1[k] for k in ("o1", "o2", "o3", "mfe")}),
                n4_o1=n4_o1, n_nolock=len(nolock),
                n_days=len(recs), n_f1=len(f1), n_excl=len(excl),
                statuses=dict(cnt))


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    lines = []

    def log(s=""):
        print(s)
        lines.append(s)

    log(L.header("PT-042", "the lock, and the high/low board",
                 "BOTH D-031 arms reported. W-B 2014-01-05 -> 2015-12-31."))
    qa, sha = L.qa_gate()
    log("  QA gate: PASS (qa_histdata_m1.py C1-C4)")
    log("")
    log("  CAVEATS -- see the module docstring and PT-042 s1a. In particular:")
    log("    * this tests a DRILL's own claim, not adopted doctrine (A-082 fence)")
    log("    * step 2 of the course's six is EXCLUDED under D-030 (A-089), so every")
    log("      figure here is a LOWER BOUND on the rule as taught")
    log("    * GBP/USD only; the cross-sectional pick across 'the majors' is untested")
    log("    * M1 is a proxy for a TICK board; locks fire slightly EARLY here")
    log("    * no spread/commission/slippage -- distances, not P&L")

    out = {a: run_arm(a, log) for a in ("A", "B")}

    # ---- VERDICT, per the pre-registered rule -----------------------------------
    log("")
    log("=" * 78)
    log("VERDICT -- applying PT-042 s6, fixed before this file existed")
    log("=" * 78)
    ok_n = all(out[a]["n"] >= B_N for a in out)
    p1 = all(out[a]["o1"] >= B_O1 for a in out)
    p2 = all(out[a]["o2"] >= B_O2 for a in out)
    for a in out:
        log(f"  arm {a}:  n={out[a]['n']}   O1={out[a]['o1']:.4f} vs >={B_O1}"
            f"   O2={out[a]['o2']:.4f} vs >={B_O2}")
    if not ok_n:
        verdict = "SAMPLE INSUFFICIENT FOR INFERENCE"
    elif p1 and p2:
        verdict = "SUPPORTED"
    elif p1 or p2:
        verdict = "PARTIALLY SUPPORTED"
    else:
        verdict = "NOT SUPPORTED"
    log("")
    log(f"  O1 (the premise) passes in both arms : {p1}")
    log(f"  O2 (the trade)   passes in both arms : {p2}")
    log(f"  n >= {B_N} in both arms                : {ok_n}")
    log("")
    log(f"  ==> {verdict}")

    with open(os.path.join(OUT_DIR, "pt042_output.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    with open(os.path.join(OUT_DIR, "pt042_result.json"), "w") as fh:
        json.dump(dict(test="PT-042", verdict=verdict, window="W-B",
                       boundaries=dict(O1=B_O1, O2=B_O2, n=B_N),
                       lock_minutes=LOCK_MIN, stop_pips=STOP_PIPS,
                       target_pips=TGT_PIPS, seed=L.SEED, arms=out),
                  fh, indent=2)
    print(f"\nwrote {OUT_DIR}/pt042_output.txt and pt042_result.json")


if __name__ == "__main__":
    main()
