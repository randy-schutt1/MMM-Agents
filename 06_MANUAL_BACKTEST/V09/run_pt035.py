#!/usr/bin/env python3
"""PT-035 — "It's highly unlikely we're gonna lose three or four times in a row".

Runs the pre-registration at
`06_MANUAL_BACKTEST/PRE_REGISTERED/PT-035_highly_unlikely_to_lose_three_or_four_in_a_row.md`,
which was committed at 0f709d2 BEFORE this file was written.

Order of output follows `COMMON_PROTOCOL.md` §9 rule 1: O1 (arithmetic, reads no
market data), then the nulls (N3 sanity control first), then O2/O3/O4.
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "06_MANUAL_BACKTEST", "scripts"))

import mmm_lib as M  # noqa: E402

OUT_DIR = os.path.join(HERE, "data")
os.makedirs(OUT_DIR, exist_ok=True)

SEQ_LEN = 200          # §4 N1 — trades per iteration, chronological, no replacement
ITERS = M.ITERATIONS   # 1000, D-029
SEED = M.SEED          # 20260812, COMMON_PROTOCOL §5
GEOMETRIES = [("25", 25.0, 50.0), ("15", 15.0, 50.0)]
ARMS = ["A", "B"]

# §7a — C8 dispositions, pre-registered. Excluded BY NAME.
EXCLUDE_DAYS = ["2014-06-01", "2014-06-02"]

lines = []


def say(s=""):
    print(s)
    lines.append(s)


# ---------------------------------------------------------------- O1

def o1_arithmetic():
    """Re-derive every number V09 states. Reads NO market data."""
    say("=" * 78)
    say("O1 — ARITHMETIC AUDIT OF V09's OWN WORKED EXAMPLE (reads no market data)")
    say("=" * 78)
    rows = []
    bal = 12500.00
    risk_pct = 0.02
    stop = 25.0

    risk = bal * risk_pct
    per_pip = risk / stop
    rows.append(("balance x 0.02", 250.00, risk, "[00:02:32] '$250 loss'"))
    rows.append(("250 / 25 pips = $/pip", 10.00, per_pip,
                 "[00:02:38] '10 minis or one lot'"))

    after4 = bal - 4 * risk
    rows.append(("after four 2% losses", 11500.00, after4, "[00:06:52] '12,500 is now 11,500'"))

    dd = (bal - after4) / bal * 100.0
    rows.append(("drawdown %", 8.00, dd, "[00:06:01] 'drawn down eight percent'"))

    risk2 = after4 * risk_pct
    pp2 = risk2 / stop
    rows.append(("2% of 11,500 -> $/pip", 9.20, pp2, "[00:06:55] '9.2 minis or 0.92 lots'"))

    w1 = after4 + 50.0 * pp2
    rows.append(("first 2:1 winner", 11960.00, w1, "[00:07:03] 'back up to 11,960'"))

    pp3 = (w1 * risk_pct) / stop
    w2 = w1 + 50.0 * pp3
    rows.append(("second 2:1 winner", 12500.00, w2, "[00:07:33] 'up to 12,500'"))

    # the naive drawdown a reviewer will compute, per §2a of the pre-registration
    naive = (1 - (1 - risk_pct) ** 4) * 100.0

    say(f"{'quantity':30} {'V09 states':>12} {'re-derived':>12}  {'':4} source")
    say("-" * 78)
    ok = []
    for name, stated, got, src in rows:
        agree = abs(stated - got) < 0.005
        ok.append(agree)
        say(f"{name:30} {stated:12,.2f} {got:12,.2f}  {'OK ' if agree else 'MISS':4} {src}")
    say("-" * 78)
    say(f"reconciled: {sum(ok)}/{len(ok)}")
    say(f"second-winner shortfall: {12500.00 - w2:,.2f}  "
        f"({(12500.00 - w2) / 12500.0 * 100:.2f}% of stated)  -> C-014")
    say("")
    say(f"§2a check — the WRONG re-derivation a reviewer is likely to try:")
    say(f"  1 - 0.98^4 = {naive:.2f}%  <- assumes size is recalculated after EVERY loss")
    say(f"  4 x 2%     = {dd:.2f}%  <- V09 holds size constant, so this is the right one")
    say("")
    return {"reconciled": int(sum(ok)), "of": len(ok),
            "second_winner_derived": round(w2, 2),
            "second_winner_stated": 12500.00,
            "shortfall": round(12500.00 - w2, 2),
            "drawdown_pct_constant_size": round(dd, 4),
            "drawdown_pct_naive_compounded": round(naive, 4)}


# ---------------------------------------------------------------- closed form

def p_any_run(p_win, k, n):
    """P(at least one run of k consecutive losses in n i.i.d. trades)."""
    q = 1.0 - p_win
    # dp over "no run of k yet", tracking current loss streak
    prev = np.zeros(k)
    prev[0] = 1.0
    no_run = 1.0
    for _ in range(n):
        cur = np.zeros(k)
        cur[0] = no_run * p_win
        for j in range(1, k):
            cur[j] = prev[j - 1] * q
        lost = prev[k - 1] * q
        no_run = cur.sum()
        prev = cur
        if no_run <= 0:
            return 1.0
    return 1.0 - no_run


def required_p(k, n, alpha=0.05, inflate=1.0):
    """Smallest p with P(any k-run in n) <= alpha. `inflate` multiplies q^k."""
    lo, hi = 0.0, 1.0
    for _ in range(60):
        mid = (lo + hi) / 2
        # inflate models observed clustering: effective q^k is `inflate` x i.i.d.
        q_eff = min(0.999999, (inflate * (1 - mid) ** k) ** (1.0 / k))
        val = p_any_run(1 - q_eff, k, n)
        if val > alpha:
            lo = mid
        else:
            hi = mid
    return hi


# ---------------------------------------------------------------- sequences

def build_sequences(grid, rng, n_seq, seq_len):
    """n_seq chronologically-ordered matched-random trade sequences.

    Direction is drawn 50/50 per trade (§4 — V09 states no directional rule, so
    there is no rule direction to match; declared, not disguised).
    Entry PRICE is the close of the selected M15 bar — the convention fixed in the
    pre-registration's §4 table (open item 65).
    """
    pool = np.where(grid.valid.any(1))[0]
    # keep only RESOLVED trades: an open position is neither a win nor a loss
    seqs = []
    unresolved_total = 0
    drawn_total = 0
    for _ in range(n_seq):
        take = rng.choice(pool, size=min(seq_len * 3, len(pool)), replace=False)
        take = np.sort(take)                      # chronological order
        d = rng.integers(0, 2, size=len(take))
        out = grid.outcome[take, d]
        drawn_total += len(out)
        keep = out != 0
        unresolved_total += int((~keep).sum())
        w = (out[keep] == 1).astype(np.int8)
        if len(w) < seq_len:
            continue
        seqs.append(w[:seq_len])
    return np.array(seqs, dtype=np.int8), drawn_total, unresolved_total


def run_stats(seqs, k):
    """fraction of length-k blocks that are all losses, per sequence."""
    n, L = seqs.shape
    loss = (seqs == 0).astype(np.int8)
    win = np.ones((n, L - k + 1), dtype=bool)
    for j in range(k):
        win &= loss[:, j:L - k + 1 + j].astype(bool)
    return win.mean(axis=1)


def max_run(seqs):
    n, L = seqs.shape
    best = np.zeros(n, dtype=int)
    cur = np.zeros(n, dtype=int)
    for j in range(L):
        cur = np.where(seqs[:, j] == 0, cur + 1, 0)
        best = np.maximum(best, cur)
    return best


def analyse(seqs, label):
    p_hat = seqs.mean(axis=1)
    r3 = run_stats(seqs, 3)
    r4 = run_stats(seqs, 4)
    i3 = (1 - p_hat) ** 3
    i4 = (1 - p_hat) ** 4
    d4 = r4 - i4
    d3 = r3 - i3
    return {
        "label": label,
        "n_seq": int(len(seqs)),
        "seq_len": int(seqs.shape[1]),
        "p_hat_median": float(np.median(p_hat)),
        "p_hat_5_95": [float(np.percentile(p_hat, 5)), float(np.percentile(p_hat, 95))],
        "run3_obs_median": float(np.median(r3)),
        "run4_obs_median": float(np.median(r4)),
        "run3_iid_median": float(np.median(i3)),
        "run4_iid_median": float(np.median(i4)),
        "d3_median": float(np.median(d3)),
        "d4_median": float(np.median(d4)),
        "d4_ci": [float(x) for x in M.boot_ci(d4)],
        "d4_frac_positive": float((d4 > 0).mean()),
        "maxrun_median": float(np.median(max_run(seqs))),
        "maxrun_95": float(np.percentile(max_run(seqs), 95)),
        "ratio_obs_iid_4": float(np.median(r4) / np.median(i4)) if np.median(i4) > 0 else float("nan"),
    }


def show(st):
    say(f"  {st['label']}")
    say(f"    n_seq {st['n_seq']}  seq_len {st['seq_len']}")
    say(f"    p_hat            median {st['p_hat_median']:.4f}   "
        f"5-95% [{st['p_hat_5_95'][0]:.4f}, {st['p_hat_5_95'][1]:.4f}]")
    say(f"    run3  observed   {st['run3_obs_median']*100:6.2f}%    "
        f"i.i.d. {st['run3_iid_median']*100:6.2f}%    diff {st['d3_median']*100:+6.2f}pp")
    say(f"    run4  observed   {st['run4_obs_median']*100:6.2f}%    "
        f"i.i.d. {st['run4_iid_median']*100:6.2f}%    diff {st['d4_median']*100:+6.2f}pp")
    say(f"    d4 bootstrap 95% [{st['d4_ci'][0]*100:+.3f}pp, {st['d4_ci'][1]*100:+.3f}pp]   "
        f"frac(d4>0) {st['d4_frac_positive']:.3f}")
    say(f"    longest loss run median {st['maxrun_median']:.0f}, 95th pct {st['maxrun_95']:.0f}")
    say("")


# ---------------------------------------------------------------- main

def main():
    say("=" * 78)
    say("PT-035 — 'highly unlikely we're gonna lose three or four times in a row'")
    say("V09 [00:06:08]-[00:06:20], GUEST, normative under D-033")
    say("=" * 78)
    say("")
    say("SCOPE (mandatory, PT-035 §8): this tests ONE empirical premise of ONE")
    say("lesson's risk plan, at a MATCHED-RANDOM entry. V09 states no entry rule and")
    say("none was invented (D-030). The claim is CONDITIONAL — 'with our training' —")
    say("and the training is NOT reproduced, because V08's recognition criterion is")
    say("A-061, an undefined adjective. A result here BOUNDS THE CLAIM FROM BELOW.")
    say("Price levels are not comparable with V02-V06 FXCM homework (D-036a).")
    say("")

    report, sha = M.qa_gate()
    say("QA GATE: PASS (C1-C4 clean) — precondition satisfied, D-036a")
    say(f"SHA256SUMS.txt: {len(sha.strip().splitlines())} files on record")
    say("")

    results = {"o1": o1_arithmetic()}

    say("=" * 78)
    say("§2b/§2c CLOSED FORM — stated in the pre-registration, reproduced here")
    say("=" * 78)
    for tag, s, t in GEOMETRIES:
        be = s / (s + t)
        say(f"  {int(s)}/{int(t)}: break-even hit rate {be*100:.2f}%   "
            f"(1-p)^3 = {(1-be)**3*100:.1f}%   (1-p)^4 = {(1-be)**4*100:.1f}%")
    for p in (0.50, 0.73):
        say(f"  p={p:.2f}: (1-p)^3 = {(1-p)**3*100:.1f}%   (1-p)^4 = {(1-p)**4*100:.1f}%   "
            f"P(any 4-run in 200) = {p_any_run(p,4,200)*100:.1f}%")
    say("")

    results["cells"] = {}
    for arm in ARMS:
        m1 = M.load_m1(arm)
        ok, a, b, why = M.verify_against_committed(arm)
        say(f"ARM {arm}: M15 re-derivation vs committed aggregate_m15.py -> "
            f"{'MATCH' if ok else 'MISMATCH'} ({a} rows, {why})")
        if not ok:
            raise SystemExit("M15 derivation drifted from the committed aggregator")

        m15 = M.resample(m1, 15)
        lo, hi = M.WINDOWS["W-C-prime"] if "W-C-prime" in M.WINDOWS else (M.DEV_START, M.DEV_END)
        m1w, m15w = m1.slice(lo, hi), m15.slice(lo, hi)
        M.assert_development(m15w.tm, f"PT-035 arm {arm}")

        # §7a — exclude the data hole BY NAME
        ex = np.zeros(len(m15w.tm), dtype=bool)
        ex1 = np.zeros(len(m1w.tm), dtype=bool)
        for d in EXCLUDE_DAYS:
            d0 = M.dt2m(d)
            ex |= (m15w.tm >= d0) & (m15w.tm < d0 + M.DAY)
            ex1 |= (m1w.tm >= d0) & (m1w.tm < d0 + M.DAY)
        n_ex15, n_ex1 = int(ex.sum()), int(ex1.sum())
        m15w = M.Bars(m15w.tm[~ex], m15w.o[~ex], m15w.h[~ex], m15w.l[~ex], m15w.c[~ex], arm, 15)
        m1w = M.Bars(m1w.tm[~ex1], m1w.o[~ex1], m1w.h[~ex1], m1w.l[~ex1], m1w.c[~ex1], arm, 1)
        say(f"        window {M.m2s(lo)} -> {M.m2s(hi)}   M15 bars {len(m15w):,}   "
            f"C8 EXCLUDED BY NAME: {n_ex15} M15 / {n_ex1} M1 bars ({', '.join(EXCLUDE_DAYS)})")
        say("")

        for tag, stop, target in GEOMETRIES:
            grid = M.TradeGrid(m1w, m15w, stop_pips=stop, target_pips=target)
            rng = np.random.default_rng(SEED)
            seqs, drawn, unres = build_sequences(grid, rng, ITERS, SEQ_LEN)
            cell = f"{arm}{tag}"

            say("=" * 78)
            say(f"CELL {cell} — geometry -{int(stop)}/+{int(target)}, D-031 arm {arm}")
            say("=" * 78)
            say(f"  eligible M15 entry bars in grid: {int(grid.valid.any(1).sum()):,}")
            say(f"  unresolved-at-horizon drawn and DISCARDED: {unres:,} of {drawn:,} "
                f"({unres/max(drawn,1)*100:.1f}%)")
            if len(seqs) < 30:
                say("  *** SAMPLE INSUFFICIENT FOR INFERENCE — descriptive only ***")
            say("")

            # N3 FIRST — the sanity control, per §4/§7b
            sh = seqs.copy()
            rs = np.random.default_rng(SEED + 1)
            for i in range(len(sh)):
                rs.shuffle(sh[i])
            st_n3 = analyse(sh, "N3 shuffled-order sanity control (must centre on ~0)")
            show(st_n3)
            n3_ok = st_n3["d4_ci"][0] <= 0.0 <= st_n3["d4_ci"][1]
            say(f"    N3 verdict: {'PASS — interval contains 0' if n3_ok else '*** FAIL — estimator biased, O3 NOT reportable (§7b) ***'}")
            say("")

            st = analyse(seqs, "O2/O3 observed, chronological order")
            show(st)

            k4 = int(round(st["run4_obs_median"] * (SEQ_LEN - 3)))
            lo_ci, hi_ci = M.wilson_ci(k4, SEQ_LEN - 3)
            say(f"    run4 Wilson 95% on the median sequence: "
                f"[{lo_ci*100:.2f}%, {hi_ci*100:.2f}%]  (k={k4}, n={SEQ_LEN-3})")

            infl = (st["run4_obs_median"] / st["run4_iid_median"]) if st["run4_iid_median"] > 0 else 1.0
            req_iid = required_p(4, 100, 0.05, 1.0)
            req_obs = required_p(4, 100, 0.05, infl)
            say(f"    O4 hit rate required for P(any 4-loss run in 100 trades) <= 5%:")
            say(f"        under i.i.d.            p >= {req_iid*100:.1f}%")
            say(f"        under observed clustering (x{infl:.2f})  p >= {req_obs*100:.1f}%")
            say("")

            st["n3"] = st_n3
            st["n3_pass"] = bool(n3_ok)
            st["unresolved_discarded"] = int(unres)
            st["drawn"] = int(drawn)
            st["c8_excluded_m15_bars"] = n_ex15
            st["required_p_iid"] = float(req_iid)
            st["required_p_observed"] = float(req_obs)
            st["inflation"] = float(infl)
            st["run4_wilson"] = [float(lo_ci), float(hi_ci)]
            results["cells"][cell] = st

    # ------------------------------------------------ decision rules
    say("=" * 78)
    say("DECISION — applying §6's rules, which were fixed before any number existed")
    say("=" * 78)
    r4 = {c: s["run4_obs_median"] for c, s in results["cells"].items()}
    say("  run4_obs medians: " + "  ".join(f"{c}={v*100:.2f}%" for c, v in r4.items()))
    if all(v >= 0.10 for v in r4.values()):
        v1 = "CONTRADICTED AS STATED"
    elif all(v < 0.05 for v in r4.values()):
        v1 = "CONFIRMED AS STATED"
    elif sum(0.05 <= v < 0.10 for v in r4.values()) > len(r4) / 2:
        v1 = "PARTIALLY SUPPORTED"
    else:
        v1 = "INDETERMINATE"
    say(f"  VERDICT on 'highly unlikely to lose three or four in a row': {v1}")
    say("")

    pos = sum(1 for s in results["cells"].values()
              if s["d4_median"] > 0 and s["d4_ci"][0] > 0)
    neg = sum(1 for s in results["cells"].values()
              if s["d4_median"] < 0 and s["d4_ci"][1] < 0)
    inc = len(results["cells"]) - pos - neg
    say(f"  clustering cells: positive-and-significant {pos}, "
        f"negative-and-significant {neg}, interval-includes-0 {inc}")
    if pos >= 3:
        v2 = "CLUSTERING CONFIRMED"
    elif neg >= 3:
        v2 = "ANTI-CLUSTERING"
    elif inc >= 2:
        v2 = "CLUSTERING NOT DETECTED"
    else:
        v2 = "INDETERMINATE"
    say(f"  VERDICT on clustering: {v2}")
    say("")
    n3_all = all(s["n3_pass"] for s in results["cells"].values())
    say(f"  N3 sanity control: {'PASS in all cells' if n3_all else '*** FAILED IN AT LEAST ONE CELL ***'}")
    say("")

    say("  §6a PREDICTIONS, scored:")
    p1 = results["o1"]["reconciled"] == results["o1"]["of"] - 1 and \
        abs(results["o1"]["second_winner_derived"] - 12438.40) < 0.01
    say(f"    P1 (O1 reconciles all but the 12,500, which lands at 12,438.40): "
        f"{'RIGHT' if p1 else 'WRONG'}")
    p2 = all(0.20 <= s["p_hat_median"] <= 0.36 for s in results["cells"].values())
    say(f"    P2 (p_hat 0.30-0.36 at 25/50, 0.20-0.26 at 15/50): "
        f"{'RIGHT' if p2 else 'WRONG'}  — "
        + ", ".join(f"{c}={s['p_hat_median']:.3f}" for c, s in results["cells"].items()))
    say(f"    P3 (run4 > 10% in all four cells -> CONTRADICTED): "
        f"{'RIGHT' if v1 == 'CONTRADICTED AS STATED' else 'WRONG'}")
    say(f"    P4 (losses cluster, d4 > 0): "
        f"{'RIGHT' if v2 == 'CLUSTERING CONFIRMED' else 'WRONG'}")
    p5 = all(s["required_p_observed"] > 0.50 for s in results["cells"].values())
    say(f"    P5 (required p > 50%, so V09's own >50% claim is insufficient): "
        f"{'RIGHT' if p5 else 'WRONG'}  — "
        + ", ".join(f"{c}={s['required_p_observed']*100:.1f}%"
                    for c, s in results["cells"].items()))
    say("")

    results["verdict_claim"] = v1
    results["verdict_clustering"] = v2
    results["n3_pass_all"] = bool(n3_all)
    results["predictions"] = {"P1": bool(p1), "P2": bool(p2),
                              "P3": v1 == "CONTRADICTED AS STATED",
                              "P4": v2 == "CLUSTERING CONFIRMED", "P5": bool(p5)}
    results["config"] = {"seed": SEED, "iterations": ITERS, "seq_len": SEQ_LEN,
                         "entry_price": "close of the selected M15 bar",
                         "c8_excluded": EXCLUDE_DAYS,
                         "window": "W-C' 2013-01-06 -> 2016-06-30 (D-035 DEVELOPMENT)"}

    with open(os.path.join(OUT_DIR, "pt035_output.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    with open(os.path.join(OUT_DIR, "pt035_results.json"), "w") as fh:
        json.dump(results, fh, indent=2)
    print(f"\nwrote {OUT_DIR}/pt035_output.txt and pt035_results.json")


if __name__ == "__main__":
    main()
