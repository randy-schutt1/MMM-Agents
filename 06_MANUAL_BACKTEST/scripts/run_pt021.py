#!/usr/bin/env python3
"""PT-021 — DNC and the straightaway test: does a prior opposite-side breach change
what follows?

Pre-registration: `PRE_REGISTERED/PT-021_straightaway_versus_stop_hunt_dnc.md`
Depends on: PT-014 (`BT_V04_0001`), whose excursion distribution predicts how many days
fall into class SW (`PT-021` §7 step 1).

THE CLASS ASSIGNMENT IS FROZEN BEFORE ANY OUTCOME IS COMPUTED (`PT-021` §7 step 3).
`assign_classes()` reads only bars at or before the qualifying close; the outcome
functions are not called until the assignment file has been written to disk.

A TERMINOLOGY NOTE THAT MATTERS FOR REPRODUCTION. `PT-015` §3 calls "breach high ->
short" the direction "away from the box"; `PT-021` §3 calls the same geometry the
"counter-trade (back into the range)". The WORDS differ between two pre-registered
files; the GEOMETRY is identical and unambiguous in both, and it is the geometry that
is implemented here: breach high -> short, breach low -> long. Neither file is edited.

usage: python3 run_pt021.py
"""
import json
import os
import sys

import numpy as np

import mmm_lib as L

OUT_DIR = os.path.join(L.ROOT, "06_MANUAL_BACKTEST", "V02", "data")
QUALIFY = 25.0          # V04 [00:15:43] floor, per `PT-021` §3
FOUR_HOURS = 240


def assign_classes(m15, days):
    """Class membership from PRIOR bars only. No later bar is consulted, ever.

    SW  "stop-hunt-first" — the opposite edge was breached by a 15m close BEFORE the
        qualifying move began, same day, after the box closed
    SA  "straightaway"    — no opposite-edge breach; the day's first excursion IS the
        qualifying move
    NEITHER — no qualifying move at all that day

    The discriminator is a GEOMETRIC EVENT, not a stop hunt. `A-002` is undefined,
    `A-049` records that the course never stated a discriminator, and `C-006` records
    that two guest accounts of it are incompatible. None of that is used here.
    """
    exc, side, when, where = L.first_close_beyond(m15, days, lo=QUALIFY, hi=np.inf)
    sd, mod = m15.sd, m15.mod
    inpost = (mod >= L.BOX_END_MIN) & (mod < L.DAY_END_MIN)
    rows_by_day = {}
    for i in np.where(inpost)[0]:
        rows_by_day.setdefault(int(sd[i]), []).append(i)

    cls = np.array(["NEITHER"] * len(days), dtype=object)
    for i, row in enumerate(days.itertuples()):
        if not np.isfinite(exc[i]):
            continue
        rows = np.asarray(rows_by_day.get(int(row.sd), []))
        prior = rows[rows < where[i]]          # STRICTLY before the qualifying close
        if len(prior) == 0:
            cls[i] = "SA"
            continue
        C = m15.c[prior]
        if side[i] > 0:                        # qualifying move broke the HIGH
            opposite = (C < row.box_lo).any()  # ... was the LOW taken out first?
        else:                                  # qualifying move broke the LOW
            opposite = (C > row.box_hi).any()  # ... was the HIGH taken out first?
        cls[i] = "SW" if opposite else "SA"
    return cls, exc, side, when, where


def continuation(m1, days, when, side, mask):
    """Measure 1 — max favourable excursion in the BREACH direction.

    Two horizons, both pre-registered: the following 4 hours, and to the 17:00 close.
    Computed on M1 so the excursion is not blurred by 15-minute bucketing.
    """
    sd1 = m1.sd
    rows_by_day = {}
    for i in range(len(m1.tm)):
        rows_by_day.setdefault(int(sd1[i]), []).append(i)
    out4, outday, entry_px = [], [], []
    for i in np.where(mask)[0]:
        day = int(days["sd"].values[i])
        idx = np.asarray(rows_by_day.get(day, []))
        if len(idx) == 0:
            out4.append(np.nan); outday.append(np.nan); entry_px.append(np.nan)
            continue
        e_moment = day * L.DAY + int(when[i]) + 15
        day_end = day * L.DAY + L.DAY_END_MIN
        fwd = idx[(m1.tm[idx] >= e_moment) & (m1.tm[idx] < day_end)]
        if len(fwd) == 0:
            out4.append(np.nan); outday.append(np.nan); entry_px.append(np.nan)
            continue
        px = m1.o[fwd[0]]
        f4 = fwd[m1.tm[fwd] < e_moment + FOUR_HOURS]
        if side[i] > 0:      # broke the high -> continuation is UP
            out4.append((m1.h[f4].max() - px) / L.PIP if len(f4) else np.nan)
            outday.append((m1.h[fwd].max() - px) / L.PIP)
        else:                # broke the low -> continuation is DOWN
            out4.append((px - m1.l[f4].min()) / L.PIP if len(f4) else np.nan)
            outday.append((px - m1.l[fwd].min()) / L.PIP)
        entry_px.append(px)
    return np.array(out4), np.array(outday)


def counter_rows(grid, days, when, side, mask):
    """Measure 2 — the DNC counter-trade: back into the range, stop 18 / target 50.

    Direction: breach high -> SHORT, breach low -> LONG. This is the prohibited trade,
    priced in both classes, which is the only honest way to test a prohibition.
    """
    rows, dirs, keep = [], [], []
    for i in np.where(mask)[0]:
        r = grid.lookup(days["sd"].values[i], when[i])
        if r is None:
            continue
        d = 1 if side[i] > 0 else 0
        if not grid.valid[r, d]:
            continue
        rows.append(r); dirs.append(d); keep.append(i)
    return np.array(rows, int), np.array(dirs, int), np.array(keep, int)


def run_arm(arm, log):
    m15 = L.window(L.load_m15(arm), "W-B")
    m1 = L.window(L.load_m1(arm), "W-B")
    days = L.build_days(m15)
    log(f"\n----- ARM {arm} -----")
    log(f"COMPLETENESS (C-6): {L.completeness_line(days)}")

    cls, exc, side, when, where = assign_classes(m15, days)
    # `PT-021` §7 step 3: freeze the class assignment BEFORE any outcome is computed
    frozen = os.path.join(OUT_DIR, f"pt021_classes_arm{arm}.csv")
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(frozen, "w") as fh:
        fh.write("session_day,class,first_qualifying_excursion_pips,side,minute_of_day\n")
        for i in range(len(days)):
            fh.write(f"{L.day2s(days['sd'].values[i])},{cls[i]},"
                     f"{exc[i] if np.isfinite(exc[i]) else ''},"
                     f"{side[i]},{when[i] if np.isfinite(when[i]) else ''}\n")
    log(f"class assignment FROZEN to {os.path.basename(frozen)} before any outcome "
        f"was computed (`PT-021` §7 step 3)")

    isSA, isSW = cls == "SA", cls == "SW"
    n_none = int((cls == "NEITHER").sum())
    log("\n[MEASURE 3 — frequency. A rule's firing rate matters as much as its accuracy]")
    log(f"  class SA (straightaway)    : {L.fmt_rate(int(isSA.sum()), len(days))}")
    log(f"  class SW (stop-hunt-first) : {L.fmt_rate(int(isSW.sum()), len(days))}")
    log(f"  neither (no qualifying move >= {QUALIFY:.0f} pips): "
        f"{L.fmt_rate(n_none, len(days))}")

    grid = L.TradeGrid(m1, m15)
    pool = np.where(grid.valid.any(1))[0]

    # ------------- BASELINES BEFORE THE CLASS COMPARISON (`PT-021` §7 step 4) --------
    log("\n[BASELINES — run and printed BEFORE the classes are compared]")
    n1 = {}
    for tag, mask in (("SA", isSA), ("SW", isSW)):
        r, d, k = counter_rows(grid, days, when, side, mask)
        if len(r) == 0:
            n1[tag] = None
            log(f"  N1 {tag}: n = 0")
            continue
        tgt, expd = L.n1_outcome(grid, d, pool=pool)
        tgt_r, exp_r = L.n1_outcome(grid, d, pool=pool, random_direction=True)
        n1[tag] = dict(tgt=tgt, exp=expd, n=len(r))
        log(f"  N1 {tag} (n = {len(r)}, direction matched, 1,000 iters, seed {L.SEED}):")
        log(f"      counter-trade hit rate   {L.dist_line(tgt)}")
        log(f"      counter-trade expectancy {L.dist_line(expd)} pips")
        log(f"    N1 secondary, RANDOM direction: hit {L.dist_line(tgt_r)}; "
            f"expectancy {L.dist_line(exp_r)} pips")

    # ------------- MEASURE 1 -------------
    log("\n[MEASURE 1 — continuation: max favourable excursion in the BREACH direction]")
    cont = {}
    for tag, mask in (("SA", isSA), ("SW", isSW)):
        c4, cd = continuation(m1, days, when, side, mask)
        cont[tag] = dict(h4=c4, day=cd)
        log(f"  {tag}: {L.nlabel(int(mask.sum()))}")
        log(f"    next 4 hours   : median {np.nanmedian(c4):.1f} pips  "
            f"mean {np.nanmean(c4):.1f}  p90 {np.nanpercentile(c4, 90):.1f}")
        log(f"    to 17:00 close : median {np.nanmedian(cd):.1f} pips  "
            f"mean {np.nanmean(cd):.1f}  p90 {np.nanpercentile(cd, 90):.1f}")
    if cont["SA"]["h4"].size and cont["SW"]["h4"].size:
        for hz in ("h4", "day"):
            o, p, _ = L.perm_diff(cont["SA"][hz], cont["SW"][hz], stat=np.median)
            lab = "next 4h" if hz == "h4" else "to 17:00"
            log(f"  SA - SW median continuation, {lab}: {o:+.1f} pips, "
                f"two-sided p = {p:.3f}")
            cont[f"perm_{hz}"] = (float(o), float(p))

    # ------------- MEASURE 2 — THE TEST -------------
    log("\n[MEASURE 2 — THE DNC TEST. The prohibited counter-trade, priced in BOTH "
        "classes.]")
    log("  `PT-021` §3: 'the only way to test a prohibition honestly is to price the")
    log("   prohibited trade in both classes'. The prohibition predicts this LOSES in")
    log("   class SA and is ACCEPTABLE in class SW.")
    res = {}
    for tag, mask in (("SA", isSA), ("SW", isSW)):
        r, d, k = counter_rows(grid, days, when, side, mask)
        if len(r) == 0:
            res[tag] = dict(n=0)
            log(f"  {tag}: n = 0")
            continue
        oc = grid.outcome[r, d]
        pl = grid.pnl_pips[r, d]
        mae = grid.mae_pips[r, d]
        rr = oc != 0
        dd = dict(n=len(r), n_target=int((oc == 1).sum()), n_stop=int((oc == -1).sum()),
                  n_open=int((oc == 0).sum()), n_resolved=int(rr.sum()),
                  hit_rate=float((oc[rr] == 1).mean()) if rr.any() else float("nan"),
                  expectancy=float(np.nanmean(pl)),
                  sd_outcome=float(np.nanstd(pl)),
                  iqr_outcome=float(np.nanpercentile(pl, 75) - np.nanpercentile(pl, 25)),
                  median_mae=float(np.nanmedian(mae)), rows=r, dirs=d, keep=k)
        log(f"  {tag}: {L.nlabel(len(r))}")
        log(f"    target / stop / open : {dd['n_target']} / {dd['n_stop']} / "
            f"{dd['n_open']}")
        log(f"    hit rate (of resolved): {L.fmt_rate(dd['n_target'], dd['n_resolved'])}")
        log(f"    expectancy            : {dd['expectancy']:+.2f} pips  boot 95% CI "
            f"{L.boot_ci(pl, stat=np.mean)}")
        log(f"    outcome SD / IQR      : {dd['sd_outcome']:.1f} / {dd['iqr_outcome']:.1f}"
            f" pips")
        if n1.get(tag):
            dd["pct_hit"] = L.percentile_of(dd["hit_rate"], n1[tag]["tgt"])
            dd["pct_exp"] = L.percentile_of(dd["expectancy"], n1[tag]["exp"])
            log(f"    vs N1: hit rate pct {dd['pct_hit']:.1f}; expectancy pct "
                f"{dd['pct_exp']:.1f}")
        res[tag] = dd

    if res["SA"].get("n") and res["SW"].get("n"):
        plSA = grid.pnl_pips[res["SA"]["rows"], res["SA"]["dirs"]]
        plSW = grid.pnl_pips[res["SW"]["rows"], res["SW"]["dirs"]]
        o, p, _ = L.perm_diff(plSA, plSW, stat=np.mean)
        log(f"\n  PRIMARY BASELINE — the course's own contrast, SA vs SW:")
        log(f"    mean expectancy SA - SW = {o:+.2f} pips; permutation two-sided "
            f"p = {p:.3f}")
        log(f"    hit rate SA {L.fmt_rate(res['SA']['n_target'], res['SA']['n_resolved'])}")
        log(f"    hit rate SW {L.fmt_rate(res['SW']['n_target'], res['SW']['n_resolved'])}")
        res["contrast"] = dict(diff=float(o), p=float(p))

    # ------------- THIRD BASELINE: volatility control -------------
    log("\n[THIRD BASELINE — volatility control. A day with breaches on BOTH sides is")
    log("  by construction a wider day; `PT-021` §5 calls this 'the likeliest confound")
    log("  in the whole batch'. Outcomes normalised by the day's own PRIOR true range.]")
    tr = (np.maximum(days["box_hi"].values, days["post_hi"].values) -
          np.minimum(days["box_lo"].values, days["post_lo"].values)) / L.PIP
    prior = np.full(len(tr), np.nan); prior[1:] = tr[:-1]
    third = {}
    for tag in ("SA", "SW"):
        if not res[tag].get("n"):
            continue
        k = res[tag]["keep"]
        pl = grid.pnl_pips[res[tag]["rows"], res[tag]["dirs"]]
        pv = prior[k]
        ok = np.isfinite(pv) & (pv > 0) & np.isfinite(pl)
        third[tag] = dict(median_prior_tr=float(np.nanmedian(pv)),
                          median_box=float(np.median(days["box_range_pips"].values[k])),
                          exp_norm=float(np.mean(pl[ok] / pv[ok])) if ok.any() else np.nan)
        log(f"  {tag}: median prior TR {third[tag]['median_prior_tr']:.1f} pips  "
            f"median box {third[tag]['median_box']:.1f}  "
            f"expectancy / prior TR {third[tag]['exp_norm']:+.4f}")
    if "SA" in third and "SW" in third:
        kA = res["SA"]["keep"]; kW = res["SW"]["keep"]
        o, p, _ = L.perm_diff(prior[kA], prior[kW], stat=np.median)
        log(f"  prior-TR difference SA - SW: {o:+.1f} pips, two-sided p = {p:.3f}  "
            f"(is the confound even present?)")
        plA = grid.pnl_pips[res["SA"]["rows"], res["SA"]["dirs"]] / prior[kA]
        plW = grid.pnl_pips[res["SW"]["rows"], res["SW"]["dirs"]] / prior[kW]
        o2, p2, _ = L.perm_diff(plA, plW, stat=np.mean)
        log(f"  NORMALISED expectancy SA - SW: {o2:+.4f} of prior TR, "
            f"two-sided p = {p2:.3f}")
        third["perm_prior"] = (float(o), float(p))
        third["perm_norm"] = (float(o2), float(p2))

    clean = {t: {k: v for k, v in res[t].items() if k not in ("rows", "dirs", "keep")}
             for t in ("SA", "SW") if isinstance(res.get(t), dict)}
    return dict(arm=arm, n_days=int(len(days)), n_SA=int(isSA.sum()),
                n_SW=int(isSW.sum()), n_none=n_none, measure2=clean,
                contrast=res.get("contrast"), third=third,
                cont={k: (v if not isinstance(v, dict) else
                          dict(median_4h=float(np.nanmedian(v["h4"])),
                               median_day=float(np.nanmedian(v["day"]))))
                      for k, v in cont.items()},
                n1={k: (None if v is None else dict(hit=L.dist_line(v["tgt"]),
                                                    exp=L.dist_line(v["exp"])))
                    for k, v in n1.items()})


def main():
    lines = []

    def log(s=""):
        print(s)
        lines.append(s)

    log(L.header("PT-021", "DNC and the straightaway test (W-B)",
                 "window   : W-B 2014-01-05 -> 2015-12-31 (wholly inside DEVELOPMENT)"))
    log("PRE-REG  : PRE_REGISTERED/PT-021_straightaway_versus_stop_hunt_dnc.md")
    log("CLAIM    : V02 [00:18:44] 'DNC. Do not counter trade back into the range.'")
    log("           [00:18:58] 'This is a straightaway... the dealer didn't make a stop")
    log("           hunt below the box.'  [00:19:06] 'if the dealer comes back in here,")
    log("           that's a trade.'")
    log("DESIGN   : the closest the corpus comes to a PRE-SPECIFIED CONTROL GROUP")
    log("           (`BACKTEST_EVIDENCE_STANDARD.md` §2.2). SA vs SW is the course's own")
    log("           contrast: same instrument, box, session and geometry; only the prior")
    log("           opposite-side breach differs.")

    res = {}
    for arm in ("A", "B"):
        res[arm] = run_arm(arm, log)

    log("\n" + "=" * 78)
    log("BOTH ARMS SIDE BY SIDE — `D-031` requires both, always")
    log("=" * 78)
    log(f"{'':40}{'ARM A':>12}{'ARM B':>12}")
    rows = [
        ("class SA n", lambda r: r["n_SA"], "{:.0f}"),
        ("class SW n", lambda r: r["n_SW"], "{:.0f}"),
        ("neither n", lambda r: r["n_none"], "{:.0f}"),
        ("SA counter-trade hit rate", lambda r: r["measure2"]["SA"].get("hit_rate", float('nan')), "{:.3f}"),
        ("SW counter-trade hit rate", lambda r: r["measure2"]["SW"].get("hit_rate", float('nan')), "{:.3f}"),
        ("SA counter-trade expectancy", lambda r: r["measure2"]["SA"].get("expectancy", float('nan')), "{:+.2f}"),
        ("SW counter-trade expectancy", lambda r: r["measure2"]["SW"].get("expectancy", float('nan')), "{:+.2f}"),
        ("SA outcome SD", lambda r: r["measure2"]["SA"].get("sd_outcome", float('nan')), "{:.1f}"),
        ("SW outcome SD", lambda r: r["measure2"]["SW"].get("sd_outcome", float('nan')), "{:.1f}"),
        ("SA - SW expectancy diff", lambda r: (r["contrast"] or {}).get("diff", float('nan')), "{:+.2f}"),
        ("  permutation p", lambda r: (r["contrast"] or {}).get("p", float('nan')), "{:.3f}"),
        ("SA median continuation, 4h", lambda r: r["cont"]["SA"]["median_4h"], "{:.1f}"),
        ("SW median continuation, 4h", lambda r: r["cont"]["SW"]["median_4h"], "{:.1f}"),
    ]
    for lab, f, fmt in rows:
        log(f"{lab:<40}{fmt.format(f(res['A'])):>12}{fmt.format(f(res['B'])):>12}")

    with open(os.path.join(OUT_DIR, "pt021_results.json"), "w") as fh:
        json.dump(res, fh, indent=1, default=str)
    with open(os.path.join(OUT_DIR, "pt021_report.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print("\nwritten:", os.path.join(OUT_DIR, "pt021_results.json"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
