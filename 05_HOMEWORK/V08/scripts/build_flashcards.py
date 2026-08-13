#!/usr/bin/env python3
"""V08 homework H3 — hard-right-edge flashcards, built exactly as the lesson describes.

V08 [00:31:37]-[00:31:53]:
    "All I had to do was go back and erase the candles... Why not erase all the candles which
     lead up to the setup? I could create many movies of the candles as they formed."
V08 [00:28:00]:
    "we take an ideal setup and then we chop it back. So we're now looking at the setup as it
     would be at the best possible entry on the hard right edge."

WHAT MAKES THIS PERFORMABLE WHEN MOST OF V08 IS NOT. The lesson's flashcards are built around
M/W formations, and M/W anatomy is undefined (A-011), so a flashcard set keyed on M/W would be
keyed on THIS SESSION'S definition -- D-030. This exercise therefore keys on the object PT-034
established is ARITHMETIC and needs no course definition: the day's low. That is also the object
V08's own high-low drill targets, so the exercise is closer to the lesson than an invented M/W
proxy would be, not further from it.

TWO PHASES, AND THE SEPARATION IS THE POINT.

  build   Emits ONLY the fronts: the bars visible at the decision point, and nothing after it.
          The answer key is written to a SEPARATE file that the student does not open.
  score   Reads the student's committed predictions and the answer key, and scores them.

The predictions are committed to Git BEFORE score is run. That is the same discipline D-026/
D-027 impose on a backtest, applied to a comprehension exercise, and it is what makes the
result mean anything.

usage:
    python3 05_HOMEWORK/V08/scripts/build_flashcards.py build
    python3 05_HOMEWORK/V08/scripts/build_flashcards.py score
"""
import csv, json, os, random, sys
from datetime import datetime, timedelta, date

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
DATA = os.path.join(ROOT, "06_MANUAL_BACKTEST", "datasets", "HISTDATA_GBPUSD_M1")
OUT = os.path.join(ROOT, "05_HOMEWORK", "V08", "data")
CHARTS = os.path.join(ROOT, "05_HOMEWORK", "V08", "charts")

SEED = 20260813
PIP = 0.0001
N_CARDS = 12
X_PIPS = 10.0                    # the lesson's own printed tolerance (frame V08_00-05-40)
TARGET_PIPS = 50.0               # the lesson's own exit
STOP_PIPS = TARGET_PIPS / 3.0    # IMPLIED from "three to one or greater"
WIN_START = date(2013, 1, 6)
WIN_END = date(2016, 6, 30)
C8_EXCLUDE = {date(2014, 6, 1), date(2014, 6, 2)}


def load():
    ts, op, hi, lo, cl = [], [], [], [], []
    with open(os.path.join(DATA, "GBPUSD_M15_ARMA.csv"), newline="") as f:
        for r in csv.reader(f):
            if len(r) < 6:
                continue
            ts.append(datetime.strptime(r[0] + " " + r[1], "%Y.%m.%d %H:%M"))
            op.append(float(r[2])); hi.append(float(r[3])); lo.append(float(r[4])); cl.append(float(r[5]))
    return ts, op, hi, lo, cl


def session_days(ts):
    b = {}
    for i, dt in enumerate(ts):
        b.setdefault((dt - timedelta(hours=17)).date(), []).append(i)
    return {k: v for k, v in b.items()
            if WIN_START <= k <= WIN_END and k not in C8_EXCLUDE and len(v) >= 20}


def build():
    os.makedirs(OUT, exist_ok=True); os.makedirs(CHARTS, exist_ok=True)
    ts, op, hi, lo, cl = load()
    days = session_days(ts)
    rng = random.Random(SEED)
    keys = sorted(days)
    rng.shuffle(keys)

    fronts, key = [], []
    for k in keys:
        if len(fronts) >= N_CARDS:
            break
        idx = days[k]
        lod = min(lo[i] for i in idx)
        want = lod + X_PIPS * PIP
        ent = next((i for i in idx if lo[i] <= want + 1e-12), None)
        if ent is None or ent == idx[-1]:
            continue
        # need at least 8 bars of visible history before the decision bar
        if idx.index(ent) < 8:
            continue
        px = want if lo[ent] <= want <= hi[ent] else lo[ent]

        vis = [i for i in idx if i <= ent]
        front = {
            "card": len(fronts) + 1,
            "day": str(k),
            "decision_bar_time": ts[ent].strftime("%Y-%m-%d %H:%M"),
            "entry_price": round(px, 5),
            "bars_visible": len(vis),
            "visible_ohlc": [[ts[i].strftime("%H:%M"), round(op[i], 5), round(hi[i], 5),
                              round(lo[i], 5), round(cl[i], 5)] for i in vis[-24:]],
            "question": ("LONG at the entry price. Does +50 pips arrive before -16.67 pips? "
                         "Answer TARGET or STOP."),
        }
        # ---- answer key, written to a DIFFERENT file ----
        tgt, stp = px + TARGET_PIPS * PIP, px - STOP_PIPS * PIP
        out, nb = "UNRESOLVED", None
        for j in range(ent + 1, len(ts)):
            if lo[j] <= stp:
                out, nb = "STOP", j - ent; break
            if hi[j] >= tgt:
                out, nb = "TARGET", j - ent; break
        fronts.append(front)
        key.append({"card": front["card"], "day": str(k), "outcome": out, "bars": nb})
        svg(front, os.path.join(CHARTS, f"V08_flashcard_{front['card']:02d}_{k}.svg"))

    json.dump({"seed": SEED, "x_pips": X_PIPS, "target_pips": TARGET_PIPS,
               "stop_pips": STOP_PIPS, "cards": fronts},
              open(os.path.join(OUT, "v08_flashcards_FRONT.json"), "w"), indent=2)
    json.dump({"cards": key}, open(os.path.join(OUT, "v08_flashcards_KEY.json"), "w"), indent=2)
    print(f"built {len(fronts)} flashcards")
    print(f"  fronts -> data/v08_flashcards_FRONT.json  (+ {len(fronts)} SVGs in charts/)")
    print(f"  KEY    -> data/v08_flashcards_KEY.json    <-- DO NOT OPEN BEFORE PREDICTING")


def svg(front, path):
    """Minimal candlestick SVG of the visible bars. The hard right edge is the decision bar."""
    bars = front["visible_ohlc"]
    W, H, PAD = 900, 420, 40
    los = min(b[3] for b in bars); his = max(b[2] for b in bars)
    rng_ = (his - los) or 1e-6
    def y(p): return PAD + (his - p) / rng_ * (H - 2 * PAD)
    bw = (W - 2 * PAD) / max(len(bars), 1)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
             f'viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="#f7f7f7"/>']
    for n, (t, o, h, l, c) in enumerate(bars):
        x = PAD + n * bw + bw / 2
        col = "#1a7f37" if c >= o else "#b32424"
        parts.append(f'<line x1="{x:.1f}" y1="{y(h):.1f}" x2="{x:.1f}" y2="{y(l):.1f}" '
                     f'stroke="{col}" stroke-width="1"/>')
        y1, y2 = sorted((y(o), y(c)))
        parts.append(f'<rect x="{x-bw*0.3:.1f}" y="{y1:.1f}" width="{bw*0.6:.1f}" '
                     f'height="{max(y2-y1,1):.1f}" fill="{col}"/>')
    ey = y(front["entry_price"])
    parts.append(f'<line x1="{PAD}" y1="{ey:.1f}" x2="{W-PAD}" y2="{ey:.1f}" '
                 f'stroke="#0b5fff" stroke-dasharray="4,3" stroke-width="1"/>')
    parts.append(f'<text x="{PAD}" y="20" font-family="monospace" font-size="13">'
                 f'V08 flashcard {front["card"]:02d} — GBP/USD M15 — HARD RIGHT EDGE at '
                 f'{front["decision_bar_time"]} — entry {front["entry_price"]}</text>')
    parts.append(f'<text x="{PAD}" y="{H-12}" font-family="monospace" font-size="12">'
                 f'nothing after the right edge is shown. TARGET +50 / STOP -16.67</text>')
    parts.append('</svg>')
    open(path, "w").write("".join(parts))


def score():
    front = json.load(open(os.path.join(OUT, "v08_flashcards_FRONT.json")))
    key = {c["card"]: c for c in json.load(open(os.path.join(OUT, "v08_flashcards_KEY.json")))["cards"]}
    pf = os.path.join(OUT, "v08_predictions.json")
    if not os.path.exists(pf):
        print(f"No predictions at {pf} — nothing to score. Commit predictions FIRST.")
        return 1
    pred = {int(k): v for k, v in json.load(open(pf))["predictions"].items()}

    print("=" * 74)
    print("V08 FLASHCARD DRILL — SCORED")
    print("=" * 74)
    print(f"entry = day LOW + {X_PIPS:.0f} pips (the lesson's printed tolerance); "
          f"TARGET +{TARGET_PIPS:.0f}, STOP -{STOP_PIPS:.2f}")
    print()
    ok = 0
    for c in front["cards"]:
        i = c["card"]; k = key[i]
        p = pred.get(i, "(none)")
        hit = (p == k["outcome"])
        ok += hit
        print(f"  card {i:02d}  {c['day']}  predicted={p:<10s} actual={k['outcome']:<10s} "
              f"{'OK ' if hit else 'MISS'}  bars={k['bars']}")
    n = len(front["cards"])
    base = sum(1 for c in key.values() if c["outcome"] == "TARGET")
    print()
    print(f"  score: {ok}/{n} = {ok/n:.2f}")
    print(f"  ALWAYS-TARGET baseline on this set: {base}/{n} = {base/n:.2f}")
    print(f"  A score at or below the always-TARGET baseline means the predictions carried")
    print(f"  NO information beyond the base rate. That is the honest comparison and it is")
    print(f"  printed whether or not it flatters the result.")
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "build"
    sys.exit(build() if cmd == "build" else score())
