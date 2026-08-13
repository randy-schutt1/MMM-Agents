#!/usr/bin/env python3
"""PT-004 — Are the printed "Dead Gap" and the two session gaps actually quiet?

Pre-registration: `PRE_REGISTERED/PT-004_dead_gap_and_session_gaps.md` (AMENDED
2026-08-13 — the amendment adds a disclosure row about where the week open falls and a
required Sunday-instance arm comparison; no trigger, window, metric, comparator or
threshold moved).
Depends on: PT-003 (`BT_V02_0003`) — both build the 96-slot profile, PT-003 first.

THE AMENDMENT, IMPLEMENTED. The corpus week open is 17:00 EXACTLY, so on Sundays it is
the FIRST BAR of window (i). Under Arm B it moves to 18:00 during US DST — one hour INTO
the window — and stays 17:00 during standard time. The Sunday instance's contamination
is therefore arm- AND season-dependent IN POSITION, not merely present. The two arms are
compared on the Sunday instance specifically, and divergence there is a `D-031` finding,
not a defect.

`PT-004` §7 step 3: build the full 96-slot profile FIRST, for both arms, before
extracting any named window. Done — `profile()` runs before `window_stats()`.

usage: python3 run_pt004.py
"""
import json
import os
import sys

import numpy as np

import mmm_lib as L

OUT_DIR = os.path.join(L.ROOT, "06_MANUAL_BACKTEST", "V02", "data")
WINDOW = "W-A"
FULL_DAY = [(0, 720), (720, 1440)]        # C-6: require all 96 session slots

# (label, from, to) in minute-of-day. (iv) is the `C-004` fourth window, `PT-004` §3a.
NAMED = [
    ("i   Dead Gap 17:00-20:00", 17 * 60, 20 * 60),
    ("ii  gap 03:00-03:30", 3 * 60, 3 * 60 + 30),
    ("iii gap 09:00-09:30", 9 * 60, 9 * 60 + 30),
    ("iv  03:30-04:00 (C-004)", 3 * 60 + 30, 4 * 60),
]


def comparators(a, b):
    """The equal-length window immediately before and immediately after."""
    n = (b - a) % L.DAY
    return ((a - n) % L.DAY, a), (b % L.DAY, (b + n) % L.DAY)


def day_matrix(m15, offset_min=0):
    """Session days x 96 slots of open/high/low/close, complete days only (C-6)."""
    tm = m15.tm - int(offset_min)
    sd = L.session_day(tm)
    slot = L.session_slot(L.minute_of_day(tm))
    uniq = np.unique(sd)
    pos = {int(d): i for i, d in enumerate(uniq)}
    rows = np.array([pos[int(x)] for x in sd])
    P = np.zeros((len(uniq), 96), dtype=bool)
    P[rows, slot] = True
    ok = P.all(axis=1)
    O = np.full((len(uniq), 96), np.nan); H = O.copy(); Lo = O.copy(); C = O.copy()
    O[rows, slot] = m15.o; H[rows, slot] = m15.h
    Lo[rows, slot] = m15.l; C[rows, slot] = m15.c
    return uniq[ok], O[ok], H[ok], Lo[ok], C[ok], uniq[~ok]


def slots_of(a, b):
    """Session-slot indices covered by minute range [a, b)."""
    n = int(((b - a) % L.DAY) // 15)
    s0 = int(L.session_slot(a))
    return np.array([(s0 + k) % 96 for k in range(n)])


def profile(H, Lo):
    """`PT-004` §4 second baseline: the full 24-hour profile of mean per-bar range."""
    return np.nanmean((H - Lo) / L.PIP, axis=0)


def window_stats(O, H, Lo, C, a, b, mask=None):
    """Metrics 1-3 for one window over the selected session days."""
    s = slots_of(a, b)
    if mask is None:
        mask = np.ones(len(O), dtype=bool)
    if mask.sum() == 0 or len(s) == 0:
        return dict(n=0)
    Hs, Ls = H[np.ix_(mask, s)], Lo[np.ix_(mask, s)]
    m1 = float(np.nanmean((Hs - Ls) / L.PIP))
    net = np.abs(C[np.ix_(mask, s)][:, -1] - O[np.ix_(mask, s)][:, 0]) / L.PIP
    m2 = float(np.nanmean(net))
    hi_slot = np.nanargmax(H[mask], axis=1)
    lo_slot = np.nanargmin(Lo[mask], axis=1)
    inset = set(int(x) for x in s)
    hi_in = np.array([int(x) in inset for x in hi_slot])
    lo_in = np.array([int(x) in inset for x in lo_slot])
    return dict(n=int(mask.sum()), m1=m1, m2=m2,
                m3_hi=float(hi_in.mean()), m3_lo=float(lo_in.mean()),
                m3_any=float((hi_in | lo_in).mean()),
                m3_any_k=int((hi_in | lo_in).sum()))


def run_arm(arm, log):
    m15 = L.window(L.load_m15(arm), WINDOW)
    days, O, H, Lo, C, dropped = day_matrix(m15)
    log(f"\n----- ARM {arm} -----")
    log(f"COMPLETENESS (C-6, all 96 session slots required): n = {len(days)} "
        f"({len(dropped)} excluded for incomplete sessions: "
        f"{', '.join(L.day2s(d) for d in dropped) if len(dropped) else 'none'})")
    log("  Dispositions per `QA_REPORT.txt` C8: Dec/Jan flagged sessions are real market")
    log("  CLOSURES; they still cannot support a full-window measurement and are")
    log("  excluded and named. No day is excluded for being unrepresentative.")

    # ---- STEP 3: the 96-slot profile FIRST, before any named window is extracted ----
    prof = profile(H, Lo)
    log("\n[SECOND BASELINE — the full 24-hour profile, built BEFORE any named window]")
    log("  mean per-bar true range, pips, by slot (slot 0 = 17:00):")
    for r in range(0, 96, 8):
        seg = "  ".join(f"{prof[r+k]:5.2f}" for k in range(8))
        t0 = (L.SESSION_ANCHOR + r * 15) % L.DAY
        log(f"    {t0//60:02d}:{t0%60:02d}  {seg}")
    order = np.argsort(prof)
    def slot_time(s):
        t = (L.SESSION_ANCHOR + int(s) * 15) % L.DAY
        return f"{t//60:02d}:{t%60:02d}"
    log(f"  quietest 6 slots : "
        f"{', '.join(f'{slot_time(s)} ({prof[s]:.2f})' for s in order[:6])}")
    log(f"  busiest 6 slots  : "
        f"{', '.join(f'{slot_time(s)} ({prof[s]:.2f})' for s in order[-6:][::-1])}")

    # ---- N2 BASELINE, before comparing ----
    log("\n[N2 BASELINE — circular clock shift, 1,000 draws, seed 20260812, "
        "computed before any comparison]")
    offs = L.n2_offsets()
    n2 = {lab: dict(m1=[], m2=[], m3=[]) for lab, _, _ in NAMED}
    for off in offs:
        d2, O2, H2, L2, C2, _ = day_matrix(m15, offset_min=int(off))
        if len(d2) == 0:
            continue
        for lab, a, b in NAMED:
            r = window_stats(O2, H2, L2, C2, a, b)
            if r.get("n"):
                n2[lab]["m1"].append(r["m1"])
                n2[lab]["m2"].append(r["m2"])
                n2[lab]["m3"].append(r["m3_any"])
    for lab, _, _ in NAMED:
        for k in ("m1", "m2", "m3"):
            n2[lab][k] = np.array(n2[lab][k])
        log(f"  {lab}: M1 {L.dist_line(n2[lab]['m1'])} | "
            f"M2 {L.dist_line(n2[lab]['m2'])} | M3 {L.dist_line(n2[lab]['m3'])}")

    # ---- THE NAMED WINDOWS vs THEIR COMPARATORS ----
    log("\n[RULE ARM — the named windows and their immediate neighbours]")
    res = {}
    for lab, a, b in NAMED:
        (ba, bb), (aa, ab) = comparators(a, b)
        w = window_stats(O, H, Lo, C, a, b)
        pre = window_stats(O, H, Lo, C, ba, bb)
        post = window_stats(O, H, Lo, C, aa, ab)
        log(f"\n  {lab}   n = {w['n']}")
        log(f"    {'':22}{'M1 per-bar TR':>15}{'M2 |net move|':>15}"
            f"{'M3 extreme in':>15}")
        for nm, r, rng in (("BEFORE", pre, (ba, bb)), ("THE WINDOW", w, (a, b)),
                           ("AFTER", post, (aa, ab))):
            t = f"{rng[0]//60:02d}:{rng[0]%60:02d}-{rng[1]//60:02d}:{rng[1]%60:02d}"
            log(f"    {nm:<10}{t:>12}{r['m1']:>15.3f}{r['m2']:>15.3f}"
                f"{r['m3_any']:>15.4f}")
        pm1 = L.percentile_of(w["m1"], n2[lab]["m1"])
        pm2 = L.percentile_of(w["m2"], n2[lab]["m2"])
        pm3 = L.percentile_of(w["m3_any"], n2[lab]["m3"])
        log(f"    percentile within N2: M1 {pm1:.1f}   M2 {pm2:.1f}   M3 {pm3:.1f}")
        log(f"    quieter than BOTH neighbours on M1? "
            f"{'YES' if w['m1'] < pre['m1'] and w['m1'] < post['m1'] else 'NO'}"
            f"   on M2? "
            f"{'YES' if w['m2'] < pre['m2'] and w['m2'] < post['m2'] else 'NO'}")
        log(f"    M3 detail: daily HIGH inside "
            f"{L.fmt_rate(int(round(w['m3_hi']*w['n'])), w['n'])}; "
            f"daily LOW inside {L.fmt_rate(int(round(w['m3_lo']*w['n'])), w['n'])}")
        res[lab] = dict(window=w, before=pre, after=post,
                        pct=dict(m1=pm1, m2=pm2, m3=pm3))

    # ---- WEEKDAY HANDLING, and the amendment's Sunday-instance arm comparison ----
    log("\n[WEEKDAY HANDLING — `PT-004` §3, unchanged: Sunday and Friday reported "
        "SEPARATELY]")
    log("  Instances are labelled by the CALENDAR weekday on which the window STARTS.")
    log("  Window (i) 17:00-20:00 of session day D physically occurs on the EVENING of")
    log("  D-1, so the 'Sunday instance' is the one belonging to session day Monday —")
    log("  and it is the WEEK OPEN.")
    start_wd = np.array([np.datetime64(int(d) - 1, "D").astype("datetime64[D]")
                         .item().weekday() for d in days])
    names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    a, b = NAMED[0][1], NAMED[0][2]
    log(f"\n  window (i) 17:00-20:00 by start weekday:")
    log(f"    {'start':<6}{'n':>5}{'M1 per-bar TR':>15}{'M2 |net move|':>15}"
        f"{'M3 extreme in':>15}")
    bywd = {}
    for w_ in range(7):
        m = start_wd == w_
        if m.sum() == 0:
            continue
        r = window_stats(O, H, Lo, C, a, b, mask=m)
        tag = "  <<< WEEK OPEN" if w_ == 6 else ""
        log(f"    {names[w_]:<6}{r['n']:>5}{r['m1']:>15.3f}{r['m2']:>15.3f}"
            f"{r['m3_any']:>15.4f}{tag}")
        bywd[names[w_]] = r
    log("  There is no Friday-evening instance of window (i): the week closes at Friday")
    log("  17:00, so Fri 17:00-20:00 contains no bars and forms no session day. The")
    log("  Friday effect appears instead in the BEFORE comparator 14:00-17:00 of session")
    log("  day Friday, which ends exactly at the weekly close:")
    fri_end = np.array([np.datetime64(int(d), "D").astype("datetime64[D]").item()
                        .weekday() == 4 for d in days])
    rf = window_stats(O, H, Lo, C, 14 * 60, 17 * 60, mask=fri_end)
    ro = window_stats(O, H, Lo, C, 14 * 60, 17 * 60, mask=~fri_end)
    log(f"    14:00-17:00 on session-day Friday : n = {rf['n']}  M1 {rf['m1']:.3f}  "
        f"M2 {rf['m2']:.3f}")
    log(f"    14:00-17:00 on all other days     : n = {ro['n']}  M1 {ro['m1']:.3f}  "
        f"M2 {ro['m2']:.3f}")

    # the week-open position, measured not assumed
    sun = start_wd == 6
    first_slot = np.array([int(np.argmax(np.isfinite(H[i]))) for i in range(len(days))])
    open_min = [(L.SESSION_ANCHOR + int(s) * 15) % L.DAY for s in first_slot[sun]]
    vals, cnts = np.unique(open_min, return_counts=True)
    log(f"\n  WEEK-OPEN POSITION on Sunday instances, MEASURED on this arm:")
    for v, c in zip(vals, cnts):
        log(f"    first bar of the session day at {v//60:02d}:{v%60:02d}  x{c}")
    sun_r = window_stats(O, H, Lo, C, a, b, mask=sun)
    log(f"  Sunday instance of window (i): n = {sun_r['n']}  M1 {sun_r['m1']:.3f}  "
        f"M2 {sun_r['m2']:.3f}  M3 {sun_r['m3_any']:.4f}")
    nonsun_r = window_stats(O, H, Lo, C, a, b, mask=~sun)
    log(f"  non-Sunday instances         : n = {nonsun_r['n']}  M1 {nonsun_r['m1']:.3f}"
        f"  M2 {nonsun_r['m2']:.3f}  M3 {nonsun_r['m3_any']:.4f}")

    # season split of the Sunday instance — the amendment's "arm- AND season-dependent"
    utc = m15.tm + 5 * L.HOUR
    dst_days = set()
    for s_, e_ in L._DST:
        sel = (utc >= s_) & (utc < e_)
        dst_days.update(int(x) for x in L.session_day(m15.tm[sel]))
    is_dst = np.array([int(d) in dst_days for d in days])
    log(f"\n  SUNDAY INSTANCE SPLIT BY SEASON (the amendment: position is arm- AND")
    log(f"  season-dependent). US DST in force on the session day:")
    season = {}
    for tag, m in (("US DST", sun & is_dst), ("standard time", sun & ~is_dst)):
        if m.sum() == 0:
            continue
        r = window_stats(O, H, Lo, C, a, b, mask=m)
        fs = [(L.SESSION_ANCHOR + int(s) * 15) % L.DAY for s in first_slot[m]]
        v2, c2 = np.unique(fs, return_counts=True)
        pos = ", ".join(f"{x//60:02d}:{x%60:02d} x{y}" for x, y in zip(v2, c2))
        log(f"    {tag:<14} n = {r['n']:3d}  M1 {r['m1']:.3f}  M2 {r['m2']:.3f}  "
            f"M3 {r['m3_any']:.4f}   week open at: {pos}")
        season[tag] = dict(r, open_positions=pos)

    return dict(arm=arm, n_days=int(len(days)),
                excluded=[L.day2s(d) for d in dropped],
                profile=[float(x) for x in prof], named=res,
                by_weekday={k: v for k, v in bywd.items()},
                friday_before=dict(friday=rf, other=ro),
                sunday=sun_r, nonsunday=nonsun_r, season=season,
                n2={lab: {k: L.dist_line(n2[lab][k]) for k in ("m1", "m2", "m3")}
                    for lab, _, _ in NAMED})


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    lines = []

    def log(s=""):
        print(s)
        lines.append(s)

    log(L.header("PT-004", "Are the printed Dead Gap and session gaps actually quiet? (W-A)",
                 "window   : W-A 2015-01-04 -> 2015-12-31 (wholly inside DEVELOPMENT)"))
    log("PRE-REG  : PRE_REGISTERED/PT-004_dead_gap_and_session_gaps.md (AMENDED)")
    log("AMENDMENT: adds a disclosure row on where the week open falls, and REQUIRES the")
    log("           two `D-031` arms be compared on the SUNDAY INSTANCE specifically.")
    log("           No trigger, window, metric, comparator or threshold moved.")
    log("CLAIM    : V02 slide [00:45:55] prints three inactive windows; [00:50:32] says")
    log("           '3 to 3:30 is the gap, 4 o'clock session open'.")
    log("C-004    : OPEN. 03:30-04:00 is measured as a FOURTH window so the two readings")
    log("           can be compared on the same data. This test resolves nothing.")
    log("SCOPE    : NOT a test of any trading rule; NOT a test of 'The MM Spread Is Set'.")

    res = {}
    for arm in ("A", "B"):
        res[arm] = run_arm(arm, log)

    log("\n" + "=" * 78)
    log("BOTH ARMS SIDE BY SIDE — `D-031` requires both, always")
    log("=" * 78)
    log(f"{'':44}{'ARM A':>12}{'ARM B':>12}")
    for lab, _, _ in NAMED:
        for k, nm in (("m1", "M1 per-bar TR"), ("m2", "M2 |net move|")):
            log(f"{lab[:30]+' '+nm:<44}"
                f"{res['A']['named'][lab]['window'][k]:>12.3f}"
                f"{res['B']['named'][lab]['window'][k]:>12.3f}")
        log(f"{lab[:30]+' pct N2 M1':<44}"
            f"{res['A']['named'][lab]['pct']['m1']:>12.1f}"
            f"{res['B']['named'][lab]['pct']['m1']:>12.1f}")
    log("  --- THE AMENDMENT: the Sunday instance of window (i) ---")
    for k, nm in (("m1", "Sunday M1"), ("m2", "Sunday M2"), ("m3_any", "Sunday M3")):
        log(f"{nm:<44}{res['A']['sunday'][k]:>12.4f}{res['B']['sunday'][k]:>12.4f}")
    for k, nm in (("m1", "non-Sunday M1"), ("m2", "non-Sunday M2")):
        log(f"{nm:<44}{res['A']['nonsunday'][k]:>12.4f}"
            f"{res['B']['nonsunday'][k]:>12.4f}")

    with open(os.path.join(OUT_DIR, "pt004_results.json"), "w") as fh:
        json.dump(res, fh, indent=1, default=str)
    with open(os.path.join(OUT_DIR, "pt004_report.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print("\nwritten:", os.path.join(OUT_DIR, "pt004_results.json"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
