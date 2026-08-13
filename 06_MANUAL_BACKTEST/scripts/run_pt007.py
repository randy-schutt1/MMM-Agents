#!/usr/bin/env python3
"""PT-007 — The two named vector-candle clock windows: 8:31 and 4:30 London.

Pre-registration: `PRE_REGISTERED/PT-007_vector_candle_clock_windows.md`
Independent; W-B.

"Vector candle" is `A-035` and is NOT used here: this test does not identify one, does
not count them, and does not require the term to mean anything. What it uses is the part
of the sentence that is a MEASUREMENT — two named minutes.

`PT-007` §3a, binding: no economic calendar exists in this corpus, so this test CANNOT
separate "the dealer places a move at 8:31" from "US data is released at 8:30". It
measures the CLOCK, which is what the instructor named, and reports the clock.

usage: python3 run_pt007.py
"""
import json
import os
import sys

import numpy as np

import mmm_lib as L

OUT_DIR = os.path.join(L.ROOT, "06_MANUAL_BACKTEST", "V02", "data")
WINDOW = "W-B"
NAMED = [("08:30 bar", 8 * 60 + 30), ("04:30 bar", 4 * 60 + 30)]
WD = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def day_matrix(m15, offset_min=0):
    tm = m15.tm - int(offset_min)
    sd = L.session_day(tm)
    slot = L.session_slot(L.minute_of_day(tm))
    uniq = np.unique(sd)
    pos = {int(d): i for i, d in enumerate(uniq)}
    rows = np.array([pos[int(x)] for x in sd])
    P = np.zeros((len(uniq), 96), dtype=bool)
    P[rows, slot] = True
    ok = P.all(axis=1)
    H = np.full((len(uniq), 96), np.nan); Lo = H.copy()
    H[rows, slot] = m15.h
    Lo[rows, slot] = m15.l
    return uniq[ok], H[ok], Lo[ok], uniq[~ok]


def metrics(H, Lo, minute):
    """`PT-007` Metrics 1-3 for the 15-minute bar containing `minute`."""
    s = int(L.session_slot(minute % L.DAY))
    TR = (H - Lo) / L.PIP
    bar = TR[:, s]
    # Metric 1 — rank of that bar's true range within the day's 96 bars (1 = largest)
    rank = (TR > bar[:, None]).sum(axis=1) + 1
    # Metric 2 — share of days on which the day's high or low is set inside that bar
    hi_in = np.nanargmax(H, axis=1) == s
    lo_in = np.nanargmin(Lo, axis=1) == s
    # Metric 3 — share of days on which the bar's range exceeds 2x the day's median bar
    med = np.nanmedian(TR, axis=1)
    over = bar > 2.0 * med
    return dict(n=int(len(bar)), mean_tr=float(np.nanmean(bar)),
                median_rank=float(np.median(rank)), mean_rank=float(np.mean(rank)),
                top_decile=float((rank <= 9.6).mean()),
                m2_hi=float(hi_in.mean()), m2_lo=float(lo_in.mean()),
                m2_any=float((hi_in | lo_in).mean()),
                m2_any_k=int((hi_in | lo_in).sum()),
                m3=float(over.mean()), m3_k=int(over.sum()),
                rank=rank, over=over, hi_in=hi_in, lo_in=lo_in)


def run_arm(arm, log):
    m15 = L.window(L.load_m15(arm), WINDOW)
    days, H, Lo, dropped = day_matrix(m15)
    log(f"\n----- ARM {arm} -----")
    log(f"COMPLETENESS (C-6, all 96 session slots required): n = {len(days)} "
        f"({len(dropped)} excluded: "
        f"{', '.join(L.day2s(d) for d in dropped) if len(dropped) <= 8 else str(len(dropped))+' days'})")

    # ---- SECOND BASELINE FIRST: the full 96-slot profile (`PT-007` §7 step 3) ----
    TR = (H - Lo) / L.PIP
    prof = np.nanmean(TR, axis=0)
    order = np.argsort(-prof)
    def st(s):
        t = (L.SESSION_ANCHOR + int(s) * 15) % L.DAY
        return f"{t//60:02d}:{t%60:02d}"
    log("\n[SECOND BASELINE — the full 96-slot intraday profile, built FIRST]")
    log(f"  busiest 8 slots: "
        f"{', '.join(f'{st(s)} ({prof[s]:.2f})' for s in order[:8])}")
    log(f"  quietest 4     : "
        f"{', '.join(f'{st(s)} ({prof[s]:.2f})' for s in order[-4:][::-1])}")
    for lab, mn in NAMED:
        s = int(L.session_slot(mn))
        rk = int(np.where(order == s)[0][0]) + 1
        log(f"  {lab}: mean TR {prof[s]:.2f} pips -> rank {rk}/96 in the profile "
            f"({'TOP DECILE' if rk <= 9.6 else 'not top decile'})")

    # ---- N2 PRIMARY BASELINE ----
    log("\n[N2 BASELINE — circular clock shift, 1,000 draws, seed 20260812, "
        "before ranking]")
    offs = L.n2_offsets()
    n2 = {lab: dict(rank=[], m2=[], m3=[]) for lab, _ in NAMED}
    for off in offs:
        d2, H2, L2, _ = day_matrix(m15, offset_min=int(off))
        if len(d2) == 0:
            continue
        for lab, mn in NAMED:
            r = metrics(H2, L2, mn)
            n2[lab]["rank"].append(r["median_rank"])
            n2[lab]["m2"].append(r["m2_any"])
            n2[lab]["m3"].append(r["m3"])
    for lab, _ in NAMED:
        for k in n2[lab]:
            n2[lab][k] = np.array(n2[lab][k])
        log(f"  {lab}: median rank {L.dist_line(n2[lab]['rank'])} | "
            f"M2 {L.dist_line(n2[lab]['m2'])} | M3 {L.dist_line(n2[lab]['m3'])}")

    # ---- RULE ARM ----
    log("\n[RULE ARM — the two named bars]")
    res = {}
    for lab, mn in NAMED:
        r = metrics(H, Lo, mn)
        pr = L.percentile_of(r["median_rank"], n2[lab]["rank"])
        p2 = L.percentile_of(r["m2_any"], n2[lab]["m2"])
        p3 = L.percentile_of(r["m3"], n2[lab]["m3"])
        log(f"\n  {lab}   n = {r['n']}   mean true range {r['mean_tr']:.2f} pips")
        log(f"    M1 rank within the day's 96 bars: median {r['median_rank']:.1f}, "
            f"mean {r['mean_rank']:.1f}   share in the day's top decile "
            f"{L.fmt_rate(int(round(r['top_decile']*r['n'])), r['n'])}")
        log(f"    M2 day's high or low set inside it: "
            f"{L.fmt_rate(r['m2_any_k'], r['n'])}   "
            f"(high {r['m2_hi']:.4f}, low {r['m2_lo']:.4f}; a 1/96 bar would give "
            f"~{2/96:.4f})")
        log(f"    M3 bar range > 2x the day's median bar: "
            f"{L.fmt_rate(r['m3_k'], r['n'])}")
        log(f"    percentile within N2: M1(rank, LOW = bigger bar) {pr:.1f}   "
            f"M2 {p2:.1f}   M3 {p3:.1f}")
        res[lab] = {k: v for k, v in r.items()
                    if k not in ("rank", "over", "hi_in", "lo_in")}
        res[lab].update(pct_rank=pr, pct_m2=p2, pct_m3=p3)

        # weekday split — pre-registered, because US macro releases cluster by weekday
        wd = np.array([np.datetime64(int(d), "D").astype("datetime64[D]").item()
                       .weekday() for d in days])
        log(f"    WEEKDAY SPLIT (pre-registered: a Friday-only effect is a different "
            f"finding from an every-day one):")
        bywd = {}
        for w_ in range(7):
            m = wd == w_
            if m.sum() == 0:
                continue
            rr = metrics(H[m], Lo[m], mn)
            log(f"      {WD[w_]:<4} n={rr['n']:4d}  mean TR {rr['mean_tr']:6.2f}  "
                f"median rank {rr['median_rank']:5.1f}  M2 {rr['m2_any']:.4f}  "
                f"M3 {rr['m3']:.4f}")
            bywd[WD[w_]] = {k: v for k, v in rr.items()
                            if k not in ("rank", "over", "hi_in", "lo_in")}
        res[lab]["by_weekday"] = bywd
    return dict(arm=arm, n_days=int(len(days)), named=res,
                profile=[float(x) for x in prof],
                n2={lab: {k: L.dist_line(n2[lab][k]) for k in ("rank", "m2", "m3")}
                    for lab, _ in NAMED})


def confirmatory(arm, log):
    """`PT-007` §3: 5-minute confirmatory "because a claim about 8:31 is finer than a
    15m bar can resolve". The corpus is M1, so the finer series is M1 — better than the
    preferred M5, and BOTH are reported. `PT-007` §5: the finer series governs, and any
    discrepancy is itself reported.
    """
    m1 = L.window(L.load_m1(arm), WINDOW)
    m5 = L.resample(m1, 5)
    log(f"\n  [CONFIRMATORY — finer than the 15m primary. `PT-007` §5: the finer series "
        f"governs]")
    out = {}
    for name, b in (("M5", m5), ("M1", m1)):
        mod = b.mod
        tr = (b.h - b.l) / L.PIP
        sd = b.sd
        # mean TR of every distinct minute-of-day, so the named minutes are ranked
        uniq_mod = np.unique(mod)
        means = np.array([np.nanmean(tr[mod == u]) for u in uniq_mod])
        order = np.argsort(-means)
        def fmt(u):
            return f"{int(u)//60:02d}:{int(u)%60:02d}"
        log(f"    {name}: busiest 6 stamps "
            f"{', '.join(f'{fmt(uniq_mod[s])} ({means[s]:.2f})' for s in order[:6])}")
        for target, tlab in ((8 * 60 + 31, "08:31 — the named minute"),
                             (8 * 60 + 30, "08:30"),
                             (4 * 60 + 30, "04:30 — the named minute")):
            if name == "M5":
                target = (target // 5) * 5
                tlab = tlab + f" (M5 bucket {fmt(target)})"
            w = np.where(uniq_mod == target)[0]
            if len(w) == 0:
                continue
            rk = int(np.where(order == w[0])[0][0]) + 1
            log(f"      {tlab:<34} mean TR {means[w[0]]:6.2f} pips   "
                f"rank {rk}/{len(uniq_mod)}")
            out[f"{name}_{fmt(target)}"] = dict(mean_tr=float(means[w[0]]), rank=rk,
                                                of=int(len(uniq_mod)))
    return out


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    lines = []

    def log(s=""):
        print(s)
        lines.append(s)

    log(L.header("PT-007", "The two named vector-candle clock windows: 8:31 and 4:30 (W-B)",
                 "window   : W-B 2014-01-05 -> 2015-12-31 (wholly inside DEVELOPMENT)"))
    log("PRE-REG  : PRE_REGISTERED/PT-007_vector_candle_clock_windows.md")
    log("CLAIM    : V02 [00:43:52] 'Concealing them behind news and announcements. Using")
    log("           the vector candle at the release of the news at 8:31. Using the")
    log("           vector candle at 4:30 London.'")
    log("SCOPE    : 'Vector candle' is `A-035` and is NOT used — this test does not")
    log("           identify one, count them, or require the term to mean anything. It")
    log("           measures a CLOCK and reports a clock (`PT-007` §6).")
    log("§3a      : NO economic calendar exists in this corpus, so this test CANNOT")
    log("           separate 'the dealer places a move at 8:31' from 'US data is released")
    log("           at 8:30'. The mundane explanation is the release schedule itself.")

    res = {}
    for arm in ("A", "B"):
        res[arm] = run_arm(arm, log)
        res[arm]["confirmatory"] = confirmatory(arm, log)

    log("\n" + "=" * 78)
    log("BOTH ARMS SIDE BY SIDE — `D-031` requires both, always")
    log("=" * 78)
    log(f"{'':44}{'ARM A':>12}{'ARM B':>12}")
    for lab, _ in NAMED:
        for k, nm, fmt in (("mean_tr", "mean true range (pips)", "{:.2f}"),
                           ("median_rank", "median rank of 96", "{:.1f}"),
                           ("top_decile", "share in day's top decile", "{:.4f}"),
                           ("m2_any", "M2 day's extreme inside", "{:.4f}"),
                           ("m3", "M3 range > 2x day median", "{:.4f}"),
                           ("pct_rank", "  pct N2 (rank)", "{:.1f}"),
                           ("pct_m2", "  pct N2 (M2)", "{:.1f}"),
                           ("pct_m3", "  pct N2 (M3)", "{:.1f}")):
            log(f"{lab+' '+nm:<44}{fmt.format(res['A']['named'][lab][k]):>12}"
                f"{fmt.format(res['B']['named'][lab][k]):>12}")

    with open(os.path.join(OUT_DIR, "pt007_results.json"), "w") as fh:
        json.dump(res, fh, indent=1, default=str)
    with open(os.path.join(OUT_DIR, "pt007_report.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print("\nwritten:", os.path.join(OUT_DIR, "pt007_results.json"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
