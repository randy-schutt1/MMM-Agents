#!/usr/bin/env python3
"""PT-040 -- does A-084's smoothing ambiguity change the RSI thresholds V11 states?

Runs the design pre-registered in
`06_MANUAL_BACKTEST/PRE_REGISTERED/PT-040_does_the_A084_smoothing_ambiguity_change_the_rsi_thresholds.md`,
committed at `83110f1` (2026-08-13T22:00:37-04:00), BEFORE this file existed and
before any bar was read.

`COMMON_PROTOCOL.md` §9 rule 7: if this runner and that pre-registration disagree,
THE PRE-REGISTRATION GOVERNS, neither file is edited, and the disagreement is
reported in `BT_V12_0001.md`.

Everything here reads M1 bars parsed from the checksummed HistData corpus (`D-036a`)
and aggregated to M15. No value is read from a rendering of any kind.

NO RANDOMISATION IS USED. Every observation is a deterministic count over a fixed
series -- no bootstrap, no permutation, no shuffle. See PT-040 §7 on the seed.

usage:  python3 run_pt040.py > ../V12/data/pt040_output.txt
"""
from __future__ import annotations

import numpy as np

import mmm_lib as L

SEED = 20260813                      # PT-040 §7, recorded before the run. UNUSED.
PERIOD = 21                          # A-080 -- the course's number, V12 [00:07:24]
KS = [1, 2, 3, 5]                    # §4 -- the sweep. NO k IS ADOPTED (§2.3)
THRESHOLDS = [20, 40, 50, 60, 80]    # §3.2 -- every one printed by V11
BULL = (40.0, 80.0)                  # V11 printed 31:25 "Bull Range: 80/40"
BEAR = (20.0, 60.0)                  # V11 printed 31:25 "Bear Range: 60/20"

IMMATERIAL_PP = 2.0                  # §5, fixed before the run
MATERIAL_PP = 5.0                    # §5, fixed before the run


# ----------------------------------------------------------------- construction

def rsi_wilder(c: np.ndarray, n: int = PERIOD) -> np.ndarray:
    """Wilder's RSI on closes. NaN for the first n bars (warm-up), per §3.1.

    Seeded by the simple mean of the first n gains and losses, then Wilder
    smoothing (alpha = 1/n). This is the standard formulation.
    """
    d = np.diff(c)
    up = np.where(d > 0, d, 0.0)
    dn = np.where(d < 0, -d, 0.0)
    au = np.full(len(c), np.nan)
    ad = np.full(len(c), np.nan)
    if len(c) <= n:
        return np.full(len(c), np.nan)
    au[n] = up[:n].mean()
    ad[n] = dn[:n].mean()
    for i in range(n + 1, len(c)):
        au[i] = (au[i - 1] * (n - 1) + up[i - 1]) / n
        ad[i] = (ad[i - 1] * (n - 1) + dn[i - 1]) / n
    with np.errstate(divide="ignore", invalid="ignore"):
        rs = au / ad
    r = 100.0 - 100.0 / (1.0 + rs)
    r = np.where(ad == 0, 100.0, r)          # all-gains window
    r = np.where((au == 0) & (ad > 0), 0.0, r)
    r[:n] = np.nan
    return r


def rsi_simple(c: np.ndarray, n: int = PERIOD) -> np.ndarray:
    """N3 robustness only (§4 N3): simple rolling mean of gains/losses, not Wilder."""
    d = np.diff(c)
    up = np.where(d > 0, d, 0.0)
    dn = np.where(d < 0, -d, 0.0)
    r = np.full(len(c), np.nan)
    cu = np.concatenate([[0.0], np.cumsum(up)])
    cd = np.concatenate([[0.0], np.cumsum(dn)])
    for i in range(n, len(c)):
        au = (cu[i] - cu[i - n]) / n
        ad = (cd[i] - cd[i - n]) / n
        if ad == 0:
            r[i] = 100.0
        elif au == 0:
            r[i] = 0.0
        else:
            r[i] = 100.0 - 100.0 / (1.0 + au / ad)
    return r


def sma(x: np.ndarray, k: int) -> np.ndarray:
    """Simple moving average over k bars; NaN where the window is not full or has NaN."""
    if k == 1:
        return x.copy()
    out = np.full(len(x), np.nan)
    for i in range(k - 1, len(x)):
        w = x[i - k + 1:i + 1]
        if not np.isnan(w).any():
            out[i] = w.mean()
    return out


def series(b: L.Bars, rsi_fn=rsi_wilder):
    """Return (R, {k: S_k}) on a window's closes, and the valid mask common to all."""
    r = rsi_fn(b.c, PERIOD)
    s = {k: sma(r, k) for k in KS}
    ok = ~np.isnan(r)
    for k in KS:
        ok &= ~np.isnan(s[k])
    return r, s, ok


# ----------------------------------------------------------------- observations

def o1(s, ok):
    return {(k, t): float(np.mean(s[k][ok] >= t)) * 100.0 for k in KS for t in THRESHOLDS}


def o2(r, s, ok):
    out = {}
    for k in KS:
        if k == 1:
            continue
        for t in THRESHOLDS:
            a = s[k][ok] >= t
            bb = r[ok] >= t
            out[(k, t)] = float(np.mean(a ^ bb)) * 100.0
    return out


def crossings(x, t):
    side = (x >= t).astype(np.int8)
    return int(np.abs(np.diff(side)).sum())


def o3(r, s, ok):
    base = {t: crossings(r[ok], t) for t in THRESHOLDS}
    out = {}
    for k in KS:
        for t in THRESHOLDS:
            n = crossings(s[k][ok], t)
            out[(k, t)] = (n, base[t], (n / base[t]) if base[t] else float("nan"))
    return out


def o4(s, ok):
    out = {}
    for k in KS:
        v = s[k][ok]
        inb = (v >= BULL[0]) & (v <= BULL[1])
        inr = (v >= BEAR[0]) & (v <= BEAR[1])
        out[k] = (float(np.mean(inb)) * 100.0, float(np.mean(inr)) * 100.0,
                  float(np.mean(~inb & ~inr)) * 100.0, float(np.mean(inb & inr)) * 100.0)
    return out


# ----------------------------------------------------------------- reporting

def cell_table(title, d, fmt="{:6.2f}", ks=None):
    ks = ks or KS
    print(f"\n  {title}")
    print("    k  |" + "".join(f"  t={t:<3d} " for t in THRESHOLDS))
    print("    ---+" + "-" * (8 * len(THRESHOLDS)))
    for k in ks:
        row = "".join(" " + fmt.format(d[(k, t)]) + " " for t in THRESHOLDS)
        print(f"    {k:<2d} |{row}")


def run_cell(window_name, arm, rsi_fn=rsi_wilder, label=""):
    b15 = L.window(L.load_m15(arm), window_name)
    r, s, ok = series(b15, rsi_fn)
    n = int(ok.sum())
    print(f"\n{'-'*78}")
    print(f"CELL: window={window_name}  arm={arm}  rsi={label or 'wilder'}")
    print(f"{'-'*78}")
    print(f"  N1  bars in window        : {len(b15.c):,}")
    print(f"  N1  bars valid after warm-up and smoothing : {n:,}"
          f"   (discarded {len(b15.c)-n:,})")
    print(f"  N1  span                  : {L.m2s(int(b15.tm[0]))} -> {L.m2s(int(b15.tm[-1]))}")
    return r, s, ok, n


def main():
    print(L.header("PT-040",
                   "Does A-084's smoothing ambiguity change the RSI thresholds?",
                   "arms     : `D-031` A (fixed UTC-5) and B (US DST). "
                   "Unit of analysis is the BAR, so REVIEW_INDEX item 101 does not bite."))
    print("\nPRE-REGISTRATION: PT-040_does_the_A084_smoothing_ambiguity_change_"
          "the_rsi_thresholds.md")
    print("                  committed 83110f1, 2026-08-13T22:00:37-04:00, "
          "BEFORE this runner existed.")
    print("NOTE: this test uses NO randomisation. The `seed` in the banner above is the")
    print("      library batch constant and affects NOTHING here (PT-040 §7, item 113).")
    print(f"RSI period {PERIOD} is the COURSE's number (A-080, V12 [00:07:24]).")
    print(f"Smoothing lengths swept: {KS}. NO k IS ADOPTED (PT-040 §2.3).")

    results = {}
    for wname in ["W-A", "W-B"]:
        for arm in ["A", "B"]:
            r, s, ok, n = run_cell(wname, arm)
            d1, d2, d3, d4 = o1(s, ok), o2(r, s, ok), o3(r, s, ok), o4(s, ok)
            results[(wname, arm)] = (d1, d2, d3, n)

            cell_table("O1  marginal occupancy, % of bars with S_k >= t", d1)
            cell_table("O2  SIDE DISAGREEMENT vs R, percentage points  <-- PRIMARY",
                       d2, ks=[k for k in KS if k != 1])
            print("\n  O3  crossings of t, count and ratio to R")
            print("    k  |" + "".join(f"   t={t:<3d}     " for t in THRESHOLDS))
            for k in KS:
                row = "".join(f"  {d3[(k,t)][0]:5d}/{d3[(k,t)][2]:5.3f} "
                              for t in THRESHOLDS)
                print(f"    {k:<2d} |{row}")
            print("\n  O4  range occupancy (DESCRIPTIVE -- tests nothing, PT-040 §4)")
            print("    k  |  in[40,80]  in[20,60]     neither        both")
            for k in KS:
                a, bb, c_, dd = d4[k]
                print(f"    {k:<2d} |   {a:7.2f}    {bb:7.2f}    {c_:7.2f}    {dd:7.2f}")

    # ---------------- N3 formula robustness: O2 on the simple-average RSI, W-A / A
    print(f"\n{'='*78}")
    print("N3  FORMULA ROBUSTNESS -- O2 recomputed with the SIMPLE-AVERAGE RSI variant")
    print(f"{'='*78}")
    r3, s3, ok3, _ = run_cell("W-A", "A", rsi_simple, label="simple-average")
    d2_3 = o2(r3, s3, ok3)
    cell_table("O2 (simple-average RSI), percentage points", d2_3,
               ks=[k for k in KS if k != 1])

    # ---------------- §5 decision
    d2_primary = results[("W-A", "A")][1]
    M = max(d2_primary.values())
    arg = max(d2_primary, key=d2_primary.get)

    print(f"\n{'='*78}")
    print("§5  DECISION -- rule fixed BEFORE the run, boundaries not adjustable")
    print(f"{'='*78}")
    print(f"  M = max O2 over k in {{2,3,5}}, t in {THRESHOLDS}, on W-A / Arm A")
    print(f"  M = {M:.3f} pp   attained at k={arg[0]}, t={arg[1]}")
    if M <= IMMATERIAL_PP:
        verdict = "IMMATERIAL"
        meaning = ("A-084 stays OPEN as a definitional gap but has NO PRACTICAL "
                   "CONSEQUENCE for threshold-crossing claims. V11's RSI half may be "
                   "tested on RSI(21) directly, with A-084 cited.")
    elif M <= MATERIAL_PP:
        verdict = "INCONCLUSIVE"
        meaning = ("Neither unblocked nor confirmed blocked. NO CLAIM MOVES. A test of "
                   f"a V11 threshold claim must report A-084 as live uncertainty up to {M:.2f} pp.")
    else:
        verdict = "MATERIAL"
        meaning = ("The choice of smoothing changes the answer. V11's RSI threshold "
                   "claims STAY BLOCKED pending a course statement of the smoothing "
                   "length. A-084 is promoted to an active blocker.")
    print(f"\n  VERDICT: {verdict}")
    print(f"  {meaning}")

    # ---------------- secondary pre-registered checks
    print(f"\n{'-'*78}")
    print("  SECONDARY CHECKS -- expectations fixed in PT-040 §5")
    print(f"{'-'*78}")
    a_cells = results[("W-A", "A")][1]
    b_cells = results[("W-A", "B")][1]
    armdiff = max(abs(a_cells[c] - b_cells[c]) for c in a_cells)
    print(f"  Arm A vs Arm B, max |O2 difference| : {armdiff:.3f} pp"
          f"   (expected < 0.5 pp)  {'OK' if armdiff < 0.5 else '** VIOLATED **'}")
    o1_50 = results[("W-A", "A")][0][(1, 50)]
    print(f"  O1(k=1, t=50)                      : {o1_50:.2f} %"
          f"   (expected 45-55 %)   {'OK' if 45 <= o1_50 <= 55 else '** VIOLATED **'}")
    d3a = o3(*series(L.window(L.load_m15('A'), 'W-A'))[:2],
             series(L.window(L.load_m15('A'), 'W-A'))[2])
    bad = [(k, t) for k in KS if k != 1 for t in THRESHOLDS if d3a[(k, t)][2] >= 1.0]
    print(f"  O3 ratios < 1.0 for every k>=2     : "
          f"{'OK' if not bad else '** VIOLATED at ' + str(bad) + ' **'}")
    wb = max(results[("W-B", "A")][1].values())
    wb_band = ("IMMATERIAL" if wb <= IMMATERIAL_PP
               else "INCONCLUSIVE" if wb <= MATERIAL_PP else "MATERIAL")
    print(f"  N2  W-B / Arm A max O2             : {wb:.3f} pp -> band {wb_band}"
          f"   {'(same as W-A)' if wb_band == verdict else '** DIFFERENT BAND **'}")
    n3 = max(d2_3.values())
    n3_band = ("IMMATERIAL" if n3 <= IMMATERIAL_PP
               else "INCONCLUSIVE" if n3 <= MATERIAL_PP else "MATERIAL")
    print(f"  N3  simple-average RSI max O2      : {n3:.3f} pp -> band {n3_band}")
    print(f"\n{'='*78}")
    print("END PT-040")
    print(f"{'='*78}")


if __name__ == "__main__":
    main()
