#!/usr/bin/env python3
"""PT-014 — Is 25-50 pips actually the modal excursion beyond the Asian range?

Pre-registration: `06_MANUAL_BACKTEST/PRE_REGISTERED/PT-014_excursion_size_distribution_beyond_the_box.md`
Shared machinery: `COMMON_PROTOCOL.md`; conventions C-1..C-5 in `mmm_lib.py`.

RUNS FIRST IN ITS FAMILY, by `INDEX.md` §3: PT-015, PT-016, PT-017, PT-018, PT-020 and
PT-021 all select inside the distribution this file reports. Discovering after the fact
that a band selects a tail is how a thin sample gets explained away instead of reported.

Nothing here is an entry rule and nothing here is tuned. Every day in W-B with a box and
a post-box window is included, zero-excursion days included (PT-014 §3), and the two
`D-031` arms are both computed and both reported.

usage: python3 run_pt014.py
"""
import json
import os
import sys

import numpy as np

import mmm_lib as L

OUT_DIR = os.path.join(L.ROOT, "06_MANUAL_BACKTEST", "V04", "data")
BANDS = [(0, 0), (0, 10), (10, 25), (25, 50), (50, 100), (100, 1e9)]
BAND_NAMES = ["exactly 0", "0 < e < 10", "10 <= e < 25", "25 <= e <= 50",
              "50 < e <= 100", "e > 100"]


def excursions(days):
    """Measure 1 — max excursion beyond each box edge inside the post-box day (C-3)."""
    hi = np.maximum(days["post_hi"].values - days["box_hi"].values, 0.0) / L.PIP
    lo = np.maximum(days["box_lo"].values - days["post_lo"].values, 0.0) / L.PIP
    return hi, lo


def band_counts(x):
    out = []
    for (a, b), name in zip(BANDS, BAND_NAMES):
        if name == "exactly 0":
            out.append(int((x == 0).sum()))
        elif b >= 1e9:
            out.append(int((x > a).sum()))
        elif name == "25 <= e <= 50":
            out.append(int(((x >= 25) & (x <= 50)).sum()))
        elif name == "0 < e < 10":
            out.append(int(((x > 0) & (x < 10)).sum()))
        elif name == "10 <= e < 25":
            out.append(int(((x >= 10) & (x < 25)).sum()))
        else:  # 50 < e <= 100
            out.append(int(((x > 50) & (x <= 100)).sum()))
    return out


def hist5(x, top=150):
    edges = np.arange(0, top + 5, 5.0)
    counts, _ = np.histogram(np.clip(x, 0, top + 4.999), bins=np.append(edges, 1e9))
    return edges, counts


def modal_bin(x, top=150):
    edges, counts = hist5(x, top)
    i = int(np.argmax(counts))
    if i >= len(edges) - 1:
        return (float(edges[-1]), float("inf")), int(counts[i])
    return (float(edges[i]), float(edges[i] + 5)), int(counts[i])


def summarise(days):
    """Every statistic PT-014 pre-registered, from one session-day frame."""
    hi, lo = excursions(days)
    pooled = np.concatenate([hi, lo])
    larger = np.maximum(hi, lo)
    box = days["box_range_pips"].values
    dayrange = days["post_range_pips"].values
    with np.errstate(divide="ignore", invalid="ignore"):
        scaled = np.where(box > 0, larger / box, np.nan)
        norm = np.where(dayrange > 0, larger / dayrange, np.nan)
    no_exc = (hi == 0) & (lo == 0)
    both = (hi > 0) & (lo > 0)
    return dict(
        n_days=int(len(days)),
        hi=hi, lo=lo, pooled=pooled, larger=larger, scaled=scaled, norm=norm,
        no_exc=no_exc, both=both,
        median_pooled=float(np.median(pooled)),
        median_larger=float(np.median(larger)),
        share_no_exc=float(no_exc.mean()),
        share_2550_pooled=float(((pooled >= 25) & (pooled <= 50)).mean()),
        share_2550_larger=float(((larger >= 25) & (larger <= 50)).mean()),
        modal_pooled=modal_bin(pooled),
        modal_larger=modal_bin(larger),
    )


def first_breach_detail(m15, days):
    """Measure 4 — which edge breaks first, is it the larger, and when is the maximum."""
    sd, mod = m15.sd, m15.mod
    inpost = (mod >= L.BOX_END_MIN) & (mod < L.DAY_END_MIN)
    idx = np.where(inpost)[0]
    by = {}
    for i in idx:
        by.setdefault(int(sd[i]), []).append(i)
    first_side, first_is_larger, max_mod, first_mod = [], [], [], []
    hi, lo = excursions(days)
    for k, row in enumerate(days.itertuples()):
        rows = by.get(int(row.sd))
        if not rows:
            first_side.append(0); first_is_larger.append(np.nan)
            max_mod.append(np.nan); first_mod.append(np.nan)
            continue
        rows = np.asarray(rows)
        H, Lw, M = m15.h[rows], m15.l[rows], mod[rows]
        up = H > row.box_hi
        dn = Lw < row.box_lo
        fu = np.where(up.any(), up.argmax(), 10 ** 9)
        fd = np.where(dn.any(), dn.argmax(), 10 ** 9)
        if fu == 10 ** 9 and fd == 10 ** 9:
            first_side.append(0); first_is_larger.append(np.nan)
            max_mod.append(np.nan); first_mod.append(np.nan)
            continue
        side = 1 if fu < fd else (-1 if fd < fu else 0)   # 0 = same bar both sides
        first_side.append(side)
        first_mod.append(float(M[min(fu, fd)]))
        eh, el = hi[k], lo[k]
        if side == 1:
            first_is_larger.append(bool(eh >= el))
        elif side == -1:
            first_is_larger.append(bool(el >= eh))
        else:
            first_is_larger.append(np.nan)
        if eh >= el:
            j = int(np.argmax(H))
        else:
            j = int(np.argmin(Lw))
        max_mod.append(float(M[j]))
    return (np.array(first_side), np.array(first_is_larger, dtype=float),
            np.array(max_mod, dtype=float), np.array(first_mod, dtype=float))


def first_qualifying_close(m15, days, floor=10.0):
    """Forecast service for PT-015/016/017/018/020/021, not a PT-014 measure.

    `INDEX.md` §3: PT-014 runs first "because it reports the excursion distribution the
    others select inside; discovering after the fact that a band selects a tail is how a
    thin sample gets explained away instead of reported." The dependent tests classify a
    day by its FIRST 15m CLOSE beyond a box edge, not by the day's maximum — and those
    are very different objects when price walks out of the box gradually. This forecasts
    the first object so the shortfall is visible BEFORE any stratified test is read.

    Delegates to `mmm_lib.first_close_beyond`, which is the batch's single implementation
    of that sentence, so PT-014's forecast and PT-015's actual classification cannot
    drift apart.
    """
    exc, side, when, _ = L.first_close_beyond(m15, days, lo=floor, hi=np.inf)
    return exc, side, when


def run_arm(arm, log):
    m15 = L.window(L.load_m15(arm), "W-B")
    days = L.build_days(m15)
    s = summarise(days)

    # ---------------- BASELINE FIRST (`COMMON_PROTOCOL.md` §9 rule 1) ----------------
    # N2 — circular clock shift. The sham box is an equally-long window placed at a
    # random hour; the whole session structure moves with it, prices untouched.
    offsets = L.n2_offsets()
    n2 = dict(median_pooled=[], share_no_exc=[], share_2550_pooled=[],
              modal_lo=[], median_larger=[])
    for off in offsets:
        d = L.build_days(m15, offset_min=int(off))
        if len(d) == 0:
            continue
        h2, l2 = excursions(d)
        p2 = np.concatenate([h2, l2])
        lg2 = np.maximum(h2, l2)
        n2["median_pooled"].append(float(np.median(p2)))
        n2["median_larger"].append(float(np.median(lg2)))
        n2["share_no_exc"].append(float(((h2 == 0) & (l2 == 0)).mean()))
        n2["share_2550_pooled"].append(float(((p2 >= 25) & (p2 <= 50)).mean()))
        n2["modal_lo"].append(modal_bin(p2)[0][0])
    n2 = {k: np.array(v) for k, v in n2.items()}

    log(f"\n----- ARM {arm} -----")
    log(f"W-B M15 bars: {len(m15):,}   span {L.m2s(m15.tm[0])} -> {L.m2s(m15.tm[-1])}")
    log(f"COMPLETENESS (C-6): {L.completeness_line(days)}")
    log(f"session days included (C-5+C-6): {s['n_days']}   "
        f"box bars/day min {int(days['box_n'].min())} max {int(days['box_n'].max())}   "
        f"post bars/day min {int(days['post_n'].min())} max {int(days['post_n'].max())}")

    log("\n[N2 baseline — computed BEFORE the rule arm's aggregate was read]")
    log(f"  draws                 : {len(n2['median_pooled'])} of {L.ITERATIONS} "
        f"(a draw is dropped only if the shifted clock yields no session day)")
    log(f"  median pooled excursion: {L.dist_line(n2['median_pooled'])}")
    log(f"  share no excursion     : {L.dist_line(n2['share_no_exc'])}")
    log(f"  share in 25-50 (pooled): {L.dist_line(n2['share_2550_pooled'])}")
    log(f"  modal 5-pip bin (lower): {L.dist_line(n2['modal_lo'])}")

    log("\n[MEASURE 1/2 — the distribution, every day included]")
    edges, counts = hist5(s["pooled"])
    log(f"  pooled observations (520 days x 2 edges): n = {len(s['pooled'])}")
    log(f"  median {s['median_pooled']:.1f} pips   mean {s['pooled'].mean():.1f}   "
        f"p90 {np.percentile(s['pooled'], 90):.1f}   max {s['pooled'].max():.1f}")
    (a, b), c = s["modal_pooled"]
    log(f"  MODAL 5-pip bin: [{a:.0f}, {b:.0f}) with {c} of {len(s['pooled'])} "
        f"({c/len(s['pooled']):.3f})")
    log("  5-pip histogram (pooled, both edges):")
    for e, ct in zip(edges[:-1], counts[:len(edges) - 1]):
        mark = ""
        if e == 10:
            mark = "   <- 10, V02 [00:44:59] 'maybe they'll only do 10 pips'"
        if e == 25:
            mark = "   <- 25, floor of V04 [00:15:43]"
        if e == 50:
            mark = "   <- 50, ceiling of V04 [00:15:43]"
        if e == 100:
            mark = "   <- 100, V02 [00:44:59] 'then they'll do it 100 pips'"
        bar = "#" * int(round(60 * ct / max(counts.max(), 1)))
        log(f"    [{e:5.0f},{e+5:5.0f})  {ct:5d}  {bar}{mark}")
    log(f"    [  150,  inf)  {counts[-1]:5d}")

    log("\n  named bands (pooled, both edges):")
    bc = band_counts(s["pooled"])
    for nm, c2 in zip(BAND_NAMES, bc):
        log(f"    {nm:>14} : {L.fmt_rate(c2, len(s['pooled']))}")

    log("\n  the day's LARGER excursion (one per day):")
    (a, b), c = s["modal_larger"]
    log(f"    median {s['median_larger']:.1f} pips; modal 5-pip bin [{a:.0f},{b:.0f}) "
        f"n={c}")
    bc2 = band_counts(s["larger"])
    for nm, c2 in zip(BAND_NAMES, bc2):
        log(f"    {nm:>14} : {L.fmt_rate(c2, len(s['larger']))}")

    nz = s["pooled"][s["pooled"] > 0]
    (a, b), c = modal_bin(nz)
    log(f"\n  CONDITIONAL ON A BREACH (zeros dropped) — reported second, deliberately:")
    log(f"    n = {len(nz)}   median {np.median(nz):.1f}   modal bin [{a:.0f},{b:.0f}) n={c}")
    log(f"    share in 25-50: {L.fmt_rate(int(((nz>=25)&(nz<=50)).sum()), len(nz))}")

    log("\n[MEASURE 3 — the 'it won't come out of the box' case]")
    log(f"  days with NO excursion beyond either edge: "
        f"{L.fmt_rate(int(s['no_exc'].sum()), s['n_days'])}")
    log(f"  days breaching BOTH edges                : "
        f"{L.fmt_rate(int(s['both'].sum()), s['n_days'])}")
    log(f"  days breaching exactly one edge          : "
        f"{L.fmt_rate(int(s['n_days'] - s['no_exc'].sum() - s['both'].sum()), s['n_days'])}")

    fs, fil, mx, fm = first_breach_detail(m15, days)
    ok = np.isfinite(fil)
    log("\n[MEASURE 4 — first excursion vs larger excursion; timing]")
    log(f"  days with an identifiable first breach: {int(ok.sum())}")
    log(f"  first-breached edge is also the LARGER excursion: "
        f"{L.fmt_rate(int(np.nansum(fil[ok])), int(ok.sum()))}")
    log(f"  first breach side: high {int((fs==1).sum())}  low {int((fs==-1).sum())}  "
        f"same bar {int((fs==0).sum())}")
    good = np.isfinite(mx)
    if good.any():
        hrs = (mx[good] // 60).astype(int)
        vals, cnts = np.unique(hrs, return_counts=True)
        log("  hour-of-day of the day's maximum excursion (arm clock):")
        for v, c2 in zip(vals, cnts):
            log(f"    {v:02d}:00  {c2:4d}  {'#'*int(round(50*c2/cnts.max()))}")
    goodf = np.isfinite(fm)
    if goodf.any():
        hrs = (fm[goodf] // 60).astype(int)
        vals, cnts = np.unique(hrs, return_counts=True)
        log("  hour-of-day of the FIRST breach (arm clock):")
        for v, c2 in zip(vals, cnts):
            log(f"    {v:02d}:00  {c2:4d}  {'#'*int(round(50*c2/cnts.max()))}")

    log("\n[MEASURE 5 — excursion scaled by the box's own range, dimensionless]")
    sc = s["scaled"][np.isfinite(s["scaled"])]
    log(f"  larger excursion / box range: n = {len(sc)}  median {np.median(sc):.3f}  "
        f"p25 {np.percentile(sc,25):.3f}  p75 {np.percentile(sc,75):.3f}")
    nb = s["norm"][np.isfinite(s["norm"])]
    log(f"  larger excursion / day's own post-box range (2nd baseline, volatility "
        f"normalised): median {np.median(nb):.3f}")
    br = days["box_range_pips"].values
    log(f"  box range itself: median {np.median(br):.1f} pips  "
        f"p10 {np.percentile(br,10):.1f}  p90 {np.percentile(br,90):.1f}")

    fq_exc, fq_side, fq_when = first_qualifying_close(m15, days)
    got = np.isfinite(fq_exc)
    log("\n[FORECAST FOR THE DEPENDENT TESTS — not a PT-014 measure, `INDEX.md` §3]")
    log(f"  days with a first close >= 10 pips beyond an edge: "
        f"{L.fmt_rate(int(got.sum()), s['n_days'])}")
    strata = [("S1 10-24", 10, 24.999), ("S2 25-50", 25, 50), ("S3 51-100", 50.001, 100),
              ("S4 >100", 100.001, 1e9)]
    log("  PT-015 strata as pre-registered (day assigned by its FIRST qualifying close):")
    for nm, a, b in strata:
        c = int(((fq_exc >= a) & (fq_exc <= b)).sum())
        flag = "   <<< BELOW n=30" if c < 30 else ""
        log(f"    {nm:<10} n = {c:4d}{flag}")
    log("  contrast — the same strata by the day's MAXIMUM excursion (NOT the "
        "pre-registered rule, shown only to make the gap visible):")
    for nm, a, b in strata:
        c = int(((s["larger"] >= a) & (s["larger"] <= b)).sum())
        log(f"    {nm:<10} n = {c:4d}")

    log("\n[RULE ARM vs N2 — percentile of the observed value within the null]")
    log(f"  median pooled excursion  obs {s['median_pooled']:.2f}  -> "
        f"pct {L.percentile_of(s['median_pooled'], n2['median_pooled']):.1f}")
    log(f"  share no excursion       obs {s['share_no_exc']:.3f}  -> "
        f"pct {L.percentile_of(s['share_no_exc'], n2['share_no_exc']):.1f}")
    log(f"  share in 25-50 (pooled)  obs {s['share_2550_pooled']:.3f}  -> "
        f"pct {L.percentile_of(s['share_2550_pooled'], n2['share_2550_pooled']):.1f}")

    # yearly split, pre-registered nowhere but reported as a descriptive stability note
    yr = (days["sd"].values * 1440 // 1440)
    years = np.array([int(L.day2s(d)[:4]) for d in days["sd"].values])
    log("\n[stability note — by calendar year, descriptive]")
    for y in np.unique(years):
        m = years == y
        p = np.concatenate([s["hi"][m], s["lo"][m]])
        log(f"  {y}: n_days {int(m.sum())}  median pooled {np.median(p):.1f}  "
            f"share 25-50 {((p>=25)&(p<=50)).mean():.3f}  "
            f"share no-exc {float(((s['hi'][m]==0)&(s['lo'][m]==0)).mean()):.3f}")

    return dict(
        arm=arm, n_days=s["n_days"], n_pooled=int(len(s["pooled"])),
        median_pooled=s["median_pooled"], median_larger=s["median_larger"],
        modal_pooled=list(s["modal_pooled"][0]) + [s["modal_pooled"][1]],
        modal_larger=list(s["modal_larger"][0]) + [s["modal_larger"][1]],
        share_no_exc=s["share_no_exc"],
        share_2550_pooled=s["share_2550_pooled"],
        share_2550_larger=s["share_2550_larger"],
        bands_pooled=dict(zip(BAND_NAMES, band_counts(s["pooled"]))),
        bands_larger=dict(zip(BAND_NAMES, band_counts(s["larger"]))),
        hist_edges=list(np.arange(0, 155, 5.0)),
        hist_counts=[int(x) for x in hist5(s["pooled"])[1]],
        both_edges=float(s["both"].mean()),
        first_is_larger=float(np.nanmean(fil)),
        scaled_median=float(np.nanmedian(s["scaled"])),
        box_range_median=float(np.median(days["box_range_pips"].values)),
        n2=dict(
            median_pooled=L.dist_line(n2["median_pooled"]),
            share_no_exc=L.dist_line(n2["share_no_exc"]),
            share_2550_pooled=L.dist_line(n2["share_2550_pooled"]),
            pct_median_pooled=L.percentile_of(s["median_pooled"], n2["median_pooled"]),
            pct_share_no_exc=L.percentile_of(s["share_no_exc"], n2["share_no_exc"]),
            pct_share_2550=L.percentile_of(s["share_2550_pooled"], n2["share_2550_pooled"]),
            draws=int(len(n2["median_pooled"])),
        ),
        # forecast handed to the dependent tests (see first_qualifying_close docstring)
        forecast_first_close={
            nm: int(((fq_exc >= a) & (fq_exc <= b)).sum())
            for nm, a, b in [("S1 10-24", 10, 24.999), ("S2 25-50", 25, 50),
                             ("S3 51-100", 50.001, 100), ("S4 >100", 100.001, 1e9)]},
        forecast_by_max={
            nm: int(((s["larger"] >= a) & (s["larger"] <= b)).sum())
            for nm, a, b in [("S1 10-24", 10, 24.999), ("S2 25-50", 25, 50),
                             ("S3 51-100", 50.001, 100), ("S4 >100", 100.001, 1e9)]},
        days_with_first_close_ge10=int(np.isfinite(fq_exc).sum()),
    )


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    lines = []

    def log(s=""):
        print(s)
        lines.append(s)

    log(L.header("PT-014", "Excursion size distribution beyond the Asian box (W-B)",
                 "window   : W-B 2014-01-05 -> 2015-12-31 (wholly inside DEVELOPMENT)"))
    log("PRE-REG  : PRE_REGISTERED/PT-014_excursion_size_distribution_beyond_the_box.md")
    log("BASELINE : N2 circular clock shift (sham box), 1,000 draws, seed 20260812")
    log("           + volatility normalisation (2nd baseline, PT-014 §4)")
    log("NOTE     : DESCRIPTIVE by pre-registration (PT-014 §6) whatever it shows.")

    res = {}
    for arm in ("A", "B"):
        res[arm] = run_arm(arm, log)

    log("\n" + "=" * 78)
    log("BOTH ARMS SIDE BY SIDE — `D-031` requires both, always")
    log("=" * 78)
    log(f"{'':28}{'ARM A (UTC-5)':>18}{'ARM B (NY/DST)':>18}")
    for key, label, fmt in [
        ("n_days", "session days", "{:.0f}"),
        ("median_pooled", "median pooled excursion", "{:.1f}"),
        ("median_larger", "median larger excursion", "{:.1f}"),
        ("share_no_exc", "share no excursion", "{:.3f}"),
        ("share_2550_pooled", "share pooled in 25-50", "{:.3f}"),
        ("share_2550_larger", "share larger in 25-50", "{:.3f}"),
        ("box_range_median", "median box range (pips)", "{:.1f}"),
        ("scaled_median", "median exc / box range", "{:.3f}"),
        ("first_is_larger", "first breach is larger", "{:.3f}"),
    ]:
        log(f"{label:<28}{fmt.format(res['A'][key]):>18}{fmt.format(res['B'][key]):>18}")
    ma = "[%.0f,%.0f)" % (res["A"]["modal_pooled"][0], res["A"]["modal_pooled"][1])
    mb = "[%.0f,%.0f)" % (res["B"]["modal_pooled"][0], res["B"]["modal_pooled"][1])
    log(f"{'modal 5-pip bin (pooled)':<28}{ma:>18}{mb:>18}")

    with open(os.path.join(OUT_DIR, "pt014_results.json"), "w") as fh:
        json.dump(res, fh, indent=1, default=str)
    with open(os.path.join(OUT_DIR, "pt014_report.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print("\nwritten:", os.path.join(OUT_DIR, "pt014_results.json"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
