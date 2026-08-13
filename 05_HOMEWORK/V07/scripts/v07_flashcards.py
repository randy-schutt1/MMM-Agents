#!/usr/bin/env python3
"""V07 HOMEWORK H3 — build the flashcards the lesson demands.

V07 defines the artifact in print, frame V07_00-13-00: "Flashcards (Screenshots)". The
audio says "flashcard" 15 times and never says what one physically is; the slide does.

    [00:12:43] "Take enough of these and keep them by your computer"
    [00:12:58] "Flashcards do one thing. They get the actual image to be implicitly
                embedded in your mind."
    [00:13:18] "the more you look at them, the easier you get to remember what the good
                setups and the good entries look like"

STUDY_PROTOCOL.md §8 requires positive AND negative examples, and requires that failed
cases be kept rather than dropped. So this builds both: days that offered a 50-pip run
from the extreme, and days that did not.

The images are a PRODUCT of numbers parsed from a checksummed CSV. Nothing is measured off
them (E06 / D-036a) -- a chart may be looked at; nothing may be measured off one.

No third-party plotting library is used (matplotlib is not installed on this machine and
D-011's spirit is to avoid adding dependencies for a one-off). Candles are drawn directly
into an SVG, which is text, diffable, and reproducible from the same CSV.

Usage:  python3 05_HOMEWORK/V07/scripts/v07_flashcards.py
"""
import json, os, sys
from datetime import date, timedelta
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import v07_homework as H

CHARTS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "charts")
W, HT, PAD = 1000, 420, 46


def svg_day(bars, title, subtitle, hod, lod, i_s, i_l, hit_s, hit_l, path):
    los = min(b[3] for b in bars)
    his = max(b[2] for b in bars)
    span = (his - los) or 1e-9
    n = len(bars)
    cw = (W - 2 * PAD) / n

    def x(i): return PAD + i * cw + cw / 2
    def y(p): return PAD + (his - p) / span * (HT - 2 * PAD)

    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{HT}" '
           f'viewBox="0 0 {W} {HT}" font-family="monospace">',
           f'<rect width="{W}" height="{HT}" fill="#ffffff"/>']
    # HOD / LOD lines
    out.append(f'<line x1="{PAD}" y1="{y(hod):.1f}" x2="{W-PAD}" y2="{y(hod):.1f}" '
               f'stroke="#c00" stroke-width="1" stroke-dasharray="4 3"/>')
    out.append(f'<line x1="{PAD}" y1="{y(lod):.1f}" x2="{W-PAD}" y2="{y(lod):.1f}" '
               f'stroke="#06c" stroke-width="1" stroke-dasharray="4 3"/>')
    out.append(f'<text x="{W-PAD}" y="{y(hod)-4:.1f}" text-anchor="end" font-size="11" '
               f'fill="#c00">HOD {hod:.5f}</text>')
    out.append(f'<text x="{W-PAD}" y="{y(lod)+13:.1f}" text-anchor="end" font-size="11" '
               f'fill="#06c">LOD {lod:.5f}</text>')
    # 50-pip goals from each extreme
    for goal, col in ((hod - 50 * H.PIP, "#c00"), (lod + 50 * H.PIP, "#06c")):
        if los <= goal <= his:
            out.append(f'<line x1="{PAD}" y1="{y(goal):.1f}" x2="{W-PAD}" y2="{y(goal):.1f}" '
                       f'stroke="{col}" stroke-width="1" stroke-dasharray="1 4" opacity=".7"/>')
    # candles
    for i, b in enumerate(bars):
        up = b[4] >= b[1]
        col = "#1a7f37" if up else "#b32020"
        out.append(f'<line x1="{x(i):.1f}" y1="{y(b[2]):.1f}" x2="{x(i):.1f}" '
                   f'y2="{y(b[3]):.1f}" stroke="{col}" stroke-width="1"/>')
        top, bot = max(b[1], b[4]), min(b[1], b[4])
        h = max(1.0, y(bot) - y(top))
        out.append(f'<rect x="{x(i)-cw*0.35:.1f}" y="{y(top):.1f}" '
                   f'width="{max(1.0, cw*0.7):.1f}" height="{h:.1f}" fill="{col}"/>')
    # entry markers
    for i, lab, col, ok in ((i_s, "SHORT@HOD", "#c00", hit_s), (i_l, "LONG@LOD", "#06c", hit_l)):
        p = bars[i][2] if lab.startswith("SHORT") else bars[i][3]
        out.append(f'<circle cx="{x(i):.1f}" cy="{y(p):.1f}" r="4" fill="none" '
                   f'stroke="{col}" stroke-width="2"/>')
        out.append(f'<text x="{x(i)+7:.1f}" y="{y(p)+4:.1f}" font-size="11" fill="{col}">'
                   f'{lab} {"HIT 50p" if ok else "NO 50p"}</text>')
    out.append(f'<text x="{PAD}" y="20" font-size="14" font-weight="bold">{title}</text>')
    out.append(f'<text x="{PAD}" y="36" font-size="11" fill="#444">{subtitle}</text>')
    out.append(f'<text x="{PAD}" y="{HT-10}" font-size="10" fill="#666">'
               f'GBP/USD 15m · HistData M1-&gt;M15 · drawn from CSV numbers, nothing measured '
               f'off this image (E06 / D-036a)</text>')
    out.append("</svg>")
    open(path, "w").write("\n".join(out))


def main():
    os.makedirs(CHARTS, exist_ok=True)
    bars = H.load_m15(os.path.join(H.DATA, "GBPUSD_M15_ARMA.csv"))
    days = H.group(bars, "D-SESSION", date(2015, 1, 1), date(2015, 12, 31))
    r = H.h1_count(days)
    misses = set(r["misses"])
    keys = sorted(days)
    # positives: evenly spaced through the year, so nothing is cherry-picked
    pos = [k for k in keys if str(k) not in misses]
    step = max(1, len(pos) // 6)
    chosen = [("POSITIVE", k) for k in pos[::step][:6]] + \
             [("NEGATIVE", k) for k in keys if str(k) in misses]
    made = []
    for kind, k in chosen:
        b = days[k]
        hod = max(x[2] for x in b)
        lod = min(x[3] for x in b)
        i_s = next(i for i, x in enumerate(b) if x[2] >= hod)
        i_l = next(i for i, x in enumerate(b) if x[3] <= lod)
        hs = any(x[3] <= hod - 50 * H.PIP for x in b[i_s + 1:])
        hl = any(x[2] >= lod + 50 * H.PIP for x in b[i_l + 1:])
        rng = (hod - lod) / H.PIP
        name = f"V07_flashcard_{kind.lower()}_{k}.svg"
        svg_day(b, f"{kind} — session day {k}  (17:00 -> 17:00, D-031 Arm A)",
                f"range {rng:.1f} pips · bars {len(b)} · dotted lines are 50 pips from each "
                f"extreme · SHORT hit={hs} LONG hit={hl}",
                hod, lod, i_s, i_l, hs, hl, os.path.join(CHARTS, name))
        made.append({"kind": kind, "day": str(k), "range_pips": round(rng, 1),
                     "short_hit": hs, "long_hit": hl, "file": name})
        print(f"  {kind:8} {k}  range={rng:6.1f}p  short={hs}  long={hl}  -> {name}")
    json.dump(made, open(os.path.join(H.OUT, "v07_flashcards.json"), "w"), indent=1)
    print(f"\n{len(made)} flashcards written to 05_HOMEWORK/V07/charts/")


if __name__ == "__main__":
    main()
