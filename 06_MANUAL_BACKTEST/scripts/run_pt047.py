#!/usr/bin/env python3
"""PT-047 — V19's second-leg time cap and the 25-50 pip extension.

Runs the test pre-registered in
`06_MANUAL_BACKTEST/PRE_REGISTERED/PT-047_the_second_leg_time_cap_and_the_extension.md`,
which was committed at b34d1a1 BEFORE this file existed.

IF THIS RUNNER AND THAT FILE DISAGREE, THAT FILE GOVERNS. Neither is edited; the
disagreement is reported in `BT_V19_0001.md`.

Every number produced here is parsed from the checksummed HistData M1 CSVs via
`mmm_lib`. Nothing is read from a rendering. Re-running against the same corpus
reproduces every figure exactly, seed included.
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
import mmm_lib as M                                                   # noqa: E402

# ---------------------------------------------------------------- §3 constants
MIN_AGE = 8            # level at least eight bars old        -- V19 [00:41:32]
MAX_AGE = 24           # and no more than six hours           -- this test's convention
HORIZON = 16           # 4 h of outcome measurement
CAP_PRIMARY = 2        # 30 minutes
CAP_ROBUST = 3         # 45 minutes
BAND = (25.0, 50.0)    # the lesson's strike-zone step, after the ASR correction
BAND_ALT = (25.0, 55.0)  # PT-047 §2d -- the uncorrected reading
DELTA_FLOOR = 10.0     # pre-registered materiality floor
PERM_ITER = 10000


def events(m15, days, cap):
    """Identify one exceed event per included session day. PT-047 §3."""
    sd = m15.sd
    mod = m15.mod
    post = (mod >= M.BOX_END_MIN) & (mod < M.DAY_END_MIN)
    keep = set(days["sd"].tolist())
    out = []
    for day in sorted(keep):
        m = post & (sd == day)
        h, l, c = m15.h[m], m15.l[m], m15.c[m]
        n = len(h)
        if n < MIN_AGE + 1 + HORIZON:
            continue
        run_hi = -np.inf
        anchor = -1
        for t in range(n):
            if run_hi > -np.inf:
                age = t - anchor
                if (h[t] > run_hi and MIN_AGE <= age <= MAX_AGE
                        and t + HORIZON < n):
                    L = float(run_hi)
                    # classifier: does it close back below L within `cap` bars?
                    closed_back = bool(
                        np.any(c[t + 1:t + 1 + cap] < L))
                    fwd_h = h[t + 1:t + 1 + HORIZON]
                    fwd_l = l[t + 1:t + 1 + HORIZON]
                    o1 = max(0.0, (float(fwd_h.max()) - L) / M.PIP)
                    o4 = max(0.0, (L - float(fwd_l.min())) / M.PIP)
                    out.append(dict(day=M.day2s(day), L=L, t=int(t),
                                    age=int(age), closed_back=closed_back,
                                    o1=o1, o4=o4))
                    break                       # first event per day only
            if h[t] > run_hi:
                run_hi = float(h[t])
                anchor = t
    return out


def perm_p(a, b, iterations=PERM_ITER, seed=M.SEED):
    """N1 -- label permutation, group sizes preserved exactly."""
    obs = float(np.median(a) - np.median(b))
    pool = np.concatenate([a, b])
    na = len(a)
    rng = np.random.default_rng(seed)
    hits = 0
    for _ in range(iterations):
        rng.shuffle(pool)
        if float(np.median(pool[:na]) - np.median(pool[na:])) >= obs:
            hits += 1
    return obs, (hits + 1) / (iterations + 1)


def cell(arm, win, cap):
    m15 = M.window(M.load_m15(arm), win)
    days = M.build_days(m15, offset_min=0, require_full=True)
    ev = events(m15, days, cap)
    held = np.array([e["o1"] for e in ev if not e["closed_back"]])
    back = np.array([e["o1"] for e in ev if e["closed_back"]])
    r = dict(arm=arm, window=win, cap_bars=cap, cap_min=cap * 15,
             n_days_included=int(len(days)),
             n_days_excluded_incomplete=int(days.attrs["n_excluded_incomplete"]),
             n_events=len(ev), n_held=int(len(held)), n_back=int(len(back)))
    if len(held) < 2 or len(back) < 2:
        r["insufficient"] = True
        return r, ev
    delta, p = perm_p(held, back)
    r.update(
        median_o1_held=round(float(np.median(held)), 4),
        median_o1_back=round(float(np.median(back)), 4),
        delta_pips=round(delta, 4),
        perm_p=round(p, 5),
        o2_held=round(float((held >= 25).mean()), 4),
        o2_back=round(float((back >= 25).mean()), 4),
        o3_band_held=round(float(((held >= BAND[0]) & (held <= BAND[1])).mean()), 4),
        o3_band_back=round(float(((back >= BAND[0]) & (back <= BAND[1])).mean()), 4),
        o3_bandalt_held=round(float(((held >= BAND_ALT[0]) & (held <= BAND_ALT[1])).mean()), 4),
        o4_median_held=round(float(np.median([e["o4"] for e in ev if not e["closed_back"]])), 4),
        o4_median_back=round(float(np.median([e["o4"] for e in ev if e["closed_back"]])), 4),
    )
    # N3 leave-one-out: drop the largest o1 from each group, re-check the primary gate
    h2 = np.sort(held)[:-1]
    b2 = np.sort(back)[:-1]
    d2 = float(np.median(h2) - np.median(b2))
    r["loo_delta_pips"] = round(d2, 4)
    return r, ev


def main():
    M.qa_gate()
    res = {}
    for arm in ("A", "B"):
        for win in ("W-A", "W-B"):
            for cap in (CAP_PRIMARY, CAP_ROBUST):
                key = f"{arm}|{win}|{cap*15}m"
                r, ev = cell(arm, win, cap)
                res[key] = r
                print(f"{key:>16}  n={r['n_events']:>4} "
                      f"held={r['n_held']:>4} back={r['n_back']:>4} "
                      + (f"Δ={r.get('delta_pips'):>8} p={r.get('perm_p')} "
                         f"medH={r.get('median_o1_held')} medB={r.get('median_o1_back')}"
                         if not r.get("insufficient") else "INSUFFICIENT"))

    # ------------------------------------------------- N3 fragility guard, §4
    prim = res[f"A|W-A|{CAP_PRIMARY*15}m"]
    fired = []
    if prim.get("insufficient"):
        fired.append("primary cell insufficient")
    else:
        sgn = np.sign(prim["delta_pips"])
        for key, r in res.items():
            if r.get("insufficient"):
                fired.append(f"{key}: insufficient")
                continue
            if np.sign(r["delta_pips"]) != sgn:
                fired.append(f"{key}: direction disagrees with primary")
            if r["n_held"] < 30 or r["n_back"] < 30:
                fired.append(f"{key}: n<30 (held={r['n_held']}, back={r['n_back']})")
        if np.sign(prim["loo_delta_pips"]) != sgn or (
                prim["loo_delta_pips"] >= DELTA_FLOOR) != (prim["delta_pips"] >= DELTA_FLOOR):
            fired.append("primary: leave-one-out flips the verdict")

    # ------------------------------------------------- §5 decision rule
    if prim.get("insufficient"):
        verdict = "REFUTED"
    elif fired:
        verdict = "FRAGILE"
    elif prim["delta_pips"] < DELTA_FLOOR or prim["perm_p"] >= 0.05:
        verdict = "REFUTED"
    elif BAND[0] <= prim["median_o1_held"] <= BAND[1]:
        verdict = "CONFIRMED"
    else:
        verdict = "PARTIAL"

    out = dict(test="PT-047", seed=M.SEED, perm_iterations=PERM_ITER,
               primary_cell=f"A|W-A|{CAP_PRIMARY*15}m",
               n3_fired=fired, verdict=verdict, cells=res)
    print("\nN3 fired:", fired if fired else "NO")
    print("VERDICT:", verdict)
    dst = os.path.join(os.path.dirname(__file__), "..", "V19", "data",
                       "pt047_results.json")
    with open(dst, "w") as f:
        json.dump(out, f, indent=2)
    print("wrote", os.path.normpath(dst))


if __name__ == "__main__":
    main()
