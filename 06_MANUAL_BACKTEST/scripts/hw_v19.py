#!/usr/bin/env python3
"""V19 HOMEWORK — descriptive measurement, NOT a test.

States no hypothesis, scores no prediction, returns no verdict.

V19 sets no new assignment. It restates a seven-item STANDING checklist
(printed at 06:45, spoken [00:07:40]-[00:08:26]). Of those seven, exactly one is
computable from the corpus without a definition the course has not supplied:
`Use ADR and Hi/Lo Markers`.

Two descriptive blocks are produced:
  (1) ADR -- over 5/10/20 sessions. THE PERIOD IS THIS SESSION'S CONVENTION.
      V19 says "A yard" ([00:08:12] = "ADR", settled by the printed slide) and
      never states a lookback. Three are reported so no single one is privileged.
  (2) Hi/Lo markers -- how often the previous session's high and low are touched
      in the next session, which is what a "marker" is drawn for.

Plus one V19-specific descriptive block, because the lesson repeats the number
eight times and it costs nothing to look at:
  (3) the pullback off the session high, against V19's "15 to 25 pips, as much
      as 50" ([00:18:09], [00:18:41], [00:42:10], [00:52:16]).

⚠ NONE of this scores V19. It is the "look at the chart" half of the homework,
done on data instead of by eye.
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
import mmm_lib as M                                                   # noqa: E402

ADR_PERIODS = (5, 10, 20)          # THIS SESSION'S CONVENTION -- not V19's
PULLBACK_BARS = 8                  # 2 h after the high, V19's own formation length


def blocks(arm, win):
    m15 = M.window(M.load_m15(arm), win)
    days = M.build_days(m15, offset_min=0, require_full=True)
    hi = days["post_hi"].to_numpy()
    lo = days["post_lo"].to_numpy()
    rng = (hi - lo) / M.PIP
    out = {"arm": arm, "window": win, "n_days": int(len(days)),
           "n_excluded_incomplete": int(days.attrs["n_excluded_incomplete"])}

    # ---- (1) ADR
    out["adr"] = {}
    for p in ADR_PERIODS:
        if len(rng) > p:
            adr = np.convolve(rng, np.ones(p) / p, mode="valid")[:-1]
            out["adr"][f"adr{p}"] = dict(
                median=round(float(np.median(adr)), 2),
                p10=round(float(np.percentile(adr, 10)), 2),
                p90=round(float(np.percentile(adr, 90)), 2),
                # how often the NEXT day's range exceeds the trailing ADR
                next_day_exceeds=round(float((rng[p:] > adr).mean()), 4))

    # ---- (2) Hi/Lo markers: prior session extreme touched next session
    out["hilo_markers"] = dict(
        prev_high_touched=round(float((hi[1:] >= hi[:-1]).mean()), 4),
        prev_low_touched=round(float((lo[1:] <= lo[:-1]).mean()), 4),
        both_touched=round(float(((hi[1:] >= hi[:-1]) & (lo[1:] <= lo[:-1])).mean()), 4),
        neither_touched=round(float(((hi[1:] < hi[:-1]) & (lo[1:] > lo[:-1])).mean()), 4))

    # ---- (3) pullback off the session high, 2 h
    sd, mod = m15.sd, m15.mod
    post = (mod >= M.BOX_END_MIN) & (mod < M.DAY_END_MIN)
    pulls = []
    for day in sorted(set(days["sd"].tolist())):
        m = post & (sd == day)
        h, l = m15.h[m], m15.l[m]
        if len(h) < PULLBACK_BARS + 2:
            continue
        k = int(np.argmax(h))
        if k + PULLBACK_BARS >= len(h):
            continue                      # high too late to measure a pullback
        pulls.append((float(h[k]) - float(l[k + 1:k + 1 + PULLBACK_BARS].min())) / M.PIP)
    pulls = np.array(pulls)
    out["pullback_off_high_2h"] = dict(
        n=len(pulls),
        median=round(float(np.median(pulls)), 2),
        p25=round(float(np.percentile(pulls, 25)), 2),
        p75=round(float(np.percentile(pulls, 75)), 2),
        frac_in_15_25=round(float(((pulls >= 15) & (pulls <= 25)).mean()), 4),
        frac_under_15=round(float((pulls < 15).mean()), 4),
        frac_over_50=round(float((pulls > 50).mean()), 4))
    return out


def main():
    M.qa_gate()
    res = []
    for arm in ("A", "B"):
        for win in ("W-A", "W-B"):
            r = blocks(arm, win)
            res.append(r)
            print(f"\n=== arm {arm} / {win}  ({r['n_days']} days, "
                  f"{r['n_excluded_incomplete']} excluded) ===")
            for p in ADR_PERIODS:
                a = r["adr"].get(f"adr{p}")
                if a:
                    print(f"  ADR{p:<3} median {a['median']:>6.2f} pips  "
                          f"[p10 {a['p10']:.2f}, p90 {a['p90']:.2f}]  "
                          f"next day exceeds it {a['next_day_exceeds']*100:.1f}%")
            hl = r["hilo_markers"]
            print(f"  prev high touched {hl['prev_high_touched']*100:.1f}%  "
                  f"prev low touched {hl['prev_low_touched']*100:.1f}%  "
                  f"both {hl['both_touched']*100:.1f}%  "
                  f"neither {hl['neither_touched']*100:.1f}%")
            pb = r["pullback_off_high_2h"]
            print(f"  pullback off high (2h): n={pb['n']} median {pb['median']:.2f} pips "
                  f"[IQR {pb['p25']:.2f}-{pb['p75']:.2f}]  "
                  f"in 15-25: {pb['frac_in_15_25']*100:.1f}%  "
                  f"<15: {pb['frac_under_15']*100:.1f}%  "
                  f">50: {pb['frac_over_50']*100:.1f}%")

    dst = os.path.join(os.path.dirname(__file__), "..", "..",
                       "05_HOMEWORK", "V19", "data", "hw_v19_results.json")
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, "w") as f:
        json.dump(dict(adr_periods=list(ADR_PERIODS),
                       pullback_bars=PULLBACK_BARS, cells=res), f, indent=2)
    print("\nwrote", os.path.normpath(dst))


if __name__ == "__main__":
    main()
