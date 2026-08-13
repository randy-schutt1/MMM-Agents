#!/usr/bin/env python3
"""PT-006 — The NYC Reversal: does the new session reverse the old one's direction?

Pre-registration: `PRE_REGISTERED/PT-006_nyc_reversal_at_session_changeover.md`
Independent; W-A.

`PT-006` §4 third arm decides what the result MEANS: "Mean reversion at a 5-hour horizon
would produce a reversal rate above 50% with no market maker involved at all."

usage: python3 run_pt006.py
"""
import json
import os
import sys

import numpy as np

import mmm_lib as L

OUT_DIR = os.path.join(L.ROOT, "06_MANUAL_BACKTEST", "V02", "data")
WINDOW = "W-A"
FULL_DAY = [(0, 720), (720, 1440)]


def series_lookup(m15):
    """Absolute-minute lookup of bar open/close. Returns (tm_sorted, O, C)."""
    return m15.tm, m15.o, m15.c


def val_at(tm, arr, want):
    """Value of the bar stamped exactly `want`; nan where that bar does not exist."""
    i = np.searchsorted(tm, want)
    ok = (i < len(tm))
    i2 = np.clip(i, 0, len(tm) - 1)
    good = ok & (tm[i2] == want)
    out = np.where(good, arr[i2], np.nan)
    return out


def session_bases(m15, offset_min=0):
    """Absolute minute at which each session day STARTS (its 17:00), complete days only.

    A session day enters only if all 96 of its slots exist (C-6).
    """
    tm = m15.tm - int(offset_min)
    sd = L.session_day(tm)
    slot = L.session_slot(L.minute_of_day(tm))
    uniq = np.unique(sd)
    pos = {int(d): i for i, d in enumerate(uniq)}
    P = np.zeros((len(uniq), 96), dtype=bool)
    P[np.array([pos[int(x)] for x in sd]), slot] = True
    ok = P.all(axis=1)
    base = (uniq - 1) * L.DAY + L.SESSION_ANCHOR + int(offset_min)
    return uniq[ok], base[ok], uniq[~ok]


def reversal(m15, base, c_min, prior_len=330, post_len=60):
    """Reversal rate for a changeover at `c_min` with the tested geometry.

    ABSOLUTE-MINUTE ARITHMETIC, deliberately. An earlier draft indexed a
    session-day x 96-slot matrix by wrapped slot, which silently computed the POST leg
    BACKWARDS across the 17:00 row boundary for every changeover between 16:30 and
    22:30 — 7 of the 24 candidates, including a spurious 0.707 at 16:30. Anchoring every
    leg to the changeover instant and stepping forward in absolute minutes cannot wrap.

    DECLARED READING, because `PT-006` §3 writes "close(09:00)" without saying which bar:
    open(t) is the OPEN of the bar stamped t; close(t) is the CLOSE of the bar stamped
    t-15, i.e. the price AT time t. So "open(03:30) -> close(09:00)" spans the bars
    stamped 03:30 through 08:45 inclusive — exactly the printed London session.
    """
    tm, O, C = m15.tm, m15.o, m15.c
    c_abs = base + int(L.session_slot(c_min % L.DAY)) * 15
    po = val_at(tm, O, c_abs - prior_len - 30)
    pc = val_at(tm, C, c_abs - 30 - 15)
    qo = val_at(tm, O, c_abs)
    qc = val_at(tm, C, c_abs + post_len - 15)
    s_prior = np.sign(pc - po)
    s_post = np.sign(qc - qo)
    good = np.isfinite(s_prior) & np.isfinite(s_post)
    both = good & (s_prior != 0) & (s_post != 0)
    if both.sum() == 0:
        return dict(n=0, k=0, rate=float("nan"), n_flat=0, n_missing=int((~good).sum()))
    diff = (s_prior[both] != s_post[both])
    return dict(n=int(both.sum()), k=int(diff.sum()), rate=float(diff.mean()),
                n_flat=int((good & ~both).sum()), n_missing=int((~good).sum()))


def run_arm(arm, log):
    m15 = L.window(L.load_m15(arm), WINDOW)
    days, base, dropped = session_bases(m15)
    log(f"\n----- ARM {arm} -----")
    log(f"COMPLETENESS (C-6, all 96 session slots required): n = {len(days)} "
        f"({len(dropped)} excluded: "
        f"{', '.join(L.day2s(d) for d in dropped) if len(dropped) else 'none'})")

    # ---------- BASELINES FIRST (`PT-006` §7 step 4) ----------
    log("\n[N2 BASELINE — circular clock shift, 1,000 draws, seed 20260812, "
        "before the 09:30 number is read]")
    offs = L.n2_offsets()
    n2 = []
    for off in offs:
        d2, b2, _ = session_bases(m15, offset_min=int(off))
        if len(d2) == 0:
            continue
        r = reversal(m15, b2, 9 * 60 + 30)
        if r.get("n"):
            n2.append(r["rate"])
    n2 = np.array(n2)
    log(f"  reversal rate between two arbitrary adjacent windows of the same lengths: "
        f"{L.dist_line(n2)}  ({len(n2)} draws)")

    log("\n[THIRD BASELINE — the serial-correlation control (`PT-006` §4). "
        "'The arm that decides\n  what the result means: mean reversion at a 5-hour "
        "horizon would produce a reversal\n  rate above 50% with no market maker "
        "involved at all.']")
    log("  `PT-006` §4 says 'two adjacent windows of the same lengths INSIDE the London")
    log("  session' — but London is 5.5h and the tested pair is 5.5h + 1h, which does not")
    log("  fit inside it. Two DECLARED variants are run and BOTH are reported; neither")
    log("  is preferred and nothing is approximated away.")
    w2 = reversal(m15, base, 6 * 60 + 15, prior_len=150, post_len=165)
    log(f"  W2 — two EQUAL halves wholly inside London (03:30-06:15 | 06:15-09:00): "
        f"{L.fmt_rate(w2['k'], w2['n'])}")
    w1 = reversal(m15, base, 6 * 60, prior_len=330, post_len=60)
    log(f"  W1 — the TESTED GEOMETRY (5.5h + 1h) with its boundary moved to 06:00, "
        f"mid-London: {L.fmt_rate(w1['k'], w1['n'])}")

    log("\n[SECOND BASELINE — all 24 candidate changeover hours, same geometry]")
    sweep = {}
    for k in range(24):
        c = (30 + 60 * k) % L.DAY
        r = reversal(m15, base, c)
        if r.get("n"):
            sweep[c] = r
    for c in sorted(sweep):
        r = sweep[c]
        tag = ""
        if c == 9 * 60 + 30:
            tag = "   <<< the NYC changeover"
        if c == 3 * 60 + 30:
            tag = "   <<< the Asian->London changeover"
        log(f"    {c//60:02d}:{c%60:02d}  n={r['n']:4d}  reversal {r['rate']:.4f}"
            f"   ({r['k']}/{r['n']}){tag}")
    rates = np.array([sweep[c]["rate"] for c in sorted(sweep)])
    hrs = np.array(sorted(sweep))
    od = np.argsort(-rates)
    rank = int(np.where(hrs[od] == 9 * 60 + 30)[0][0]) + 1

    # ---------- RULE ARM ----------
    log("\n[RULE ARM — the NYC Reversal at 09:30]")
    main = reversal(m15, base, 9 * 60 + 30)
    log(f"  prior session : open(03:30) -> close(09:00)  [the printed London session]")
    log(f"  post window   : open(09:30) -> close(10:30)  [the printed first NY hour]")
    log(f"  PRIMARY — share of days on which the two signs DIFFER: "
        f"{L.fmt_rate(main['k'], main['n'])}")
    log(f"  days with a flat leg (sign = 0), reported not dropped: {main['n_flat']}"
        f"   days with a missing bar in a leg: {main['n_missing']}")
    pct = L.percentile_of(main["rate"], n2)
    log(f"  percentile within N2: {pct:.1f}")
    log(f"  rank among the 24 candidate changeover hours: {rank}/{len(hrs)} descending")
    log(f"  vs the within-session controls: W2 {w2['rate']:.4f}   W1 {w1['rate']:.4f}")

    log("\n  SECOND MEASURE — the same test at 30 min, 2 h, and to the 17:00 close")
    horizons = {}
    for lab, plen in (("30 min", 30), ("1 h", 60), ("2 h", 120),
                      ("to 17:00", (17 * 60 - (9 * 60 + 30)))):
        r = reversal(m15, base, 9 * 60 + 30, post_len=plen)
        horizons[lab] = r
        log(f"    post = {lab:<9}: {L.fmt_rate(r['k'], r['n'])}")

    log("\n  THIRD MEASURE — the OTHER changeover, Asian -> London at 03:30")
    other = reversal(m15, base, 3 * 60 + 30)
    log(f"    prior = Asian open(20:30) -> close(03:00); post = open(03:30) -> "
        f"close(04:30)")
    r_as = reversal(m15, base, 3 * 60 + 30, prior_len=390, post_len=60)
    log(f"    with the Asian session's OWN length (6.5h prior): "
        f"{L.fmt_rate(r_as['k'], r_as['n'])}")
    log(f"    with the tested 5.5h geometry, for comparability: "
        f"{L.fmt_rate(other['k'], other['n'])}")

    return dict(arm=arm, n_days=int(len(days)),
                excluded=[L.day2s(d) for d in dropped],
                main=main, pct_n2=pct, rank=rank, n_candidates=len(hrs),
                n2=L.dist_line(n2), w1=w1, w2=w2, horizons=horizons,
                other_5h5=other, other_asian=r_as,
                sweep={f"{c//60:02d}:{c%60:02d}": sweep[c] for c in sorted(sweep)})


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    lines = []

    def log(s=""):
        print(s)
        lines.append(s)

    log(L.header("PT-006", "The NYC Reversal at session changeover (W-A)",
                 "window   : W-A 2015-01-04 -> 2015-12-31 (wholly inside DEVELOPMENT)"))
    log("PRE-REG  : PRE_REGISTERED/PT-006_nyc_reversal_at_session_changeover.md")
    log("CLAIM    : V02 [00:34:05] 'The new session brings a new target and a new market")
    log("           maker on duty.'  [00:34:09] 'The new guy came on and he changes the")
    log("           direction.'  Slide [00:33:10] 'New Session Brings New Targets For")
    log("           Market Makers ( NYC Reversal)' — a printed name never spoken.")
    log("SCOPE    : does NOT test 'a new market maker on duty' — that is a claim about")
    log("           who is behind the price, which candle data cannot observe")
    log("           (`PT-006` §6, `V01_INTERPRETATION.md` §3 G7).")

    res = {}
    for arm in ("A", "B"):
        res[arm] = run_arm(arm, log)

    log("\n" + "=" * 78)
    log("BOTH ARMS SIDE BY SIDE — `D-031` requires both, always")
    log("=" * 78)
    log(f"{'':44}{'ARM A':>12}{'ARM B':>12}")
    rows = [("n days", lambda r: r["n_days"], "{:.0f}"),
            ("09:30 reversal rate", lambda r: r["main"]["rate"], "{:.4f}"),
            ("  n (both legs non-flat)", lambda r: r["main"]["n"], "{:.0f}"),
            ("  percentile within N2", lambda r: r["pct_n2"], "{:.1f}"),
            ("  rank of 09:30 among 24", lambda r: r["rank"], "{:.0f}"),
            ("within-London control W2", lambda r: r["w2"]["rate"], "{:.4f}"),
            ("within-London control W1", lambda r: r["w1"]["rate"], "{:.4f}"),
            ("03:30 changeover (Asian prior)", lambda r: r["other_asian"]["rate"], "{:.4f}"),
            ("09:30, post = 30 min", lambda r: r["horizons"]["30 min"]["rate"], "{:.4f}"),
            ("09:30, post = 2 h", lambda r: r["horizons"]["2 h"]["rate"], "{:.4f}"),
            ("09:30, post = to 17:00", lambda r: r["horizons"]["to 17:00"]["rate"], "{:.4f}")]
    for lab, f, fmt in rows:
        log(f"{lab:<44}{fmt.format(f(res['A'])):>12}{fmt.format(f(res['B'])):>12}")

    with open(os.path.join(OUT_DIR, "pt006_results.json"), "w") as fh:
        json.dump(res, fh, indent=1, default=str)
    with open(os.path.join(OUT_DIR, "pt006_report.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print("\nwritten:", os.path.join(OUT_DIR, "pt006_results.json"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
