#!/usr/bin/env python3
"""Build a chart-first Videos 1–10 practical examination from reviewed evidence."""

from __future__ import annotations

import csv
import hashlib
import json
import shutil
from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
DATA = REPO / "06_MANUAL_BACKTEST/datasets/HISTDATA_GBPUSD_M1/GBPUSD_M15_ARMA.csv"
ASSETS = ROOT / "assets"
CHARTS = ASSETS / "charts"
CSVS = ASSETS / "visible_only_csv"
CARDS = ASSETS / "source_cards"
SEALED = ROOT / "instructor_only" / "sealed_reveals"

SOURCE_CARDS = {
    "SRC01_V01_TYPICAL_WEEK": REPO / "04_SCREENSHOTS/V01/V01_00-50-55_typical-week-gbpusd-m15.png",
    "SRC02_V02_POP_QUIZ": REPO / "04_SCREENSHOTS/V02/V02_00-52-40_pop-quiz-usdchf-chart.png",
    "SRC03_V03_FLASHCARD": REPO / "04_SCREENSHOTS/V03/V03_00-43-09_flash-card-sample-chart.png",
    "SRC04_V04_SECOND_LEG": REPO / "04_SCREENSHOTS/V04/V04_00-08-40_chart-second-leg-m-over-high.png",
    "SRC05_V06_PUSHES": REPO / "04_SCREENSHOTS/V06/V06_01-14-09_live-mt4-usdcad-m15-levels-and-pushes.png",
    "SRC06_V07_STAIR_STEP": REPO / "04_SCREENSHOTS/V07/V07_00-27-00_chart-eurusd-m15-stair-step-higher-timeframe-average.png",
    "SRC07_V08_HIGH_LOW": REPO / "04_SCREENSHOTS/V08/V08_00-38-10_high-low-drill-confirmation-myth-safest-place.png",
    "SRC08_V10_SAFETY": REPO / "04_SCREENSHOTS/V10/V10_01-01-22_audusd-15m-safety-trade-walkthrough.png",
}

EXCLUDED_WEEK_DATES = {
    "2013-02-03", "2013-05-12", "2013-09-08", "2014-02-09", "2014-07-13",
    "2014-10-12", "2015-03-08", "2015-08-09", "2015-10-11", "2015-11-08",
    "2015-12-06",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def font(size: int):
    for p in (
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Helvetica.ttf",
    ):
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def load_rows():
    out = []
    with DATA.open(newline="") as f:
        for r in csv.reader(f):
            dt = datetime.strptime(r[0] + " " + r[1], "%Y.%m.%d %H:%M")
            out.append((dt, float(r[2]), float(r[3]), float(r[4]), float(r[5]), int(r[6])))
    return out


def week_map(rows):
    opens = [r[0] for r in rows if r[0].weekday() == 6 and r[0].hour == 17 and r[0].minute == 0]
    by_dt = {r[0]: r for r in rows}
    weeks = []
    for start in opens:
        if start.strftime("%Y-%m-%d") in EXCLUDED_WEEK_DATES:
            continue
        tue = start + timedelta(days=1, hours=19)  # Tuesday 12:00 fixed UTC-5
        fri = start + timedelta(days=4, hours=23, minutes=45)  # Friday 16:45
        if tue not in by_dt or fri not in by_dt:
            continue
        block = [r for r in rows if start <= r[0] <= fri]
        if len(block) < 300:
            continue
        band = block[:32]
        bhi = max(r[2] for r in band); blo = min(r[3] for r in band)
        breach = next((r for r in block[32:] if r[2] > bhi or r[3] < blo), None)
        if breach is None or breach[0] > start + timedelta(days=3):
            continue
        weeks.append(dict(start=start, tue=tue, fri=fri, rows=block, breach=breach, band_hi=bhi, band_lo=blo))
    # Spread selected periods across the development corpus instead of clustering them.
    spread = weeks[::3]
    if len(spread) < 52:
        raise RuntimeError(f"Need 52 unseen weeks, found {len(spread)}")
    return spread[:52]


def rows_through(week, decision):
    return [r for r in week["rows"] if r[0] <= decision]


def draw_chart(asset_id, cut, mode="plain", labels=None, risk_lines=None, reveal=False):
    labels = labels or []
    W, H = 1600, 900
    left, right, top, bottom = 105, 45, 100, 105
    pw, ph = W - left - right, H - top - bottom
    lo = min(r[3] for r in cut); hi = max(r[2] for r in cut)
    pad = max((hi - lo) * 0.07, 0.0005)
    lo -= pad; hi += pad

    def x(i): return left + (i + 0.5) * pw / len(cut)
    def y(v): return top + (hi - v) * ph / (hi - lo)

    im = Image.new("RGB", (W, H), "#0b1520")
    d = ImageDraw.Draw(im)
    for j in range(7):
        yy = top + j * ph / 6
        d.line((left, yy, W - right, yy), fill="#263b4c", width=1)
        d.text((10, yy - 8), f"{hi - j*(hi-lo)/6:.5f}", font=font(14), fill="#aebdca")

    day_seen = set()
    for i, r in enumerate(cut):
        day = r[0].date()
        if day not in day_seen:
            day_seen.add(day)
            xx = x(i)
            d.line((xx, top, xx, H-bottom), fill="#385164", width=1)
            d.text((xx+4, top+4), r[0].strftime("%a %m-%d"), font=font(13), fill="#9db0bf")

    if mode in {"band", "plain", "confirmation", "risk"} and len(cut) >= 32:
        first8 = cut[:32]
        bhi = max(r[2] for r in first8); blo = min(r[3] for r in first8)
        d.rectangle((left, y(bhi), W-right, y(blo)), outline="#3ca6d8", width=2)
        d.text((left+8, y(bhi)+5), "First 8 clock hours — administration aid", font=font(14), fill="#62cbf6")

    candle_w = max(2, int(pw / len(cut) * 0.62))
    index_by_dt = {}
    for i, r in enumerate(cut):
        index_by_dt[r[0]] = i
        _, o, h, l, c, _ = r
        xx = x(i); col = "#2bc48a" if c >= o else "#ef5d72"
        d.line((xx, y(h), xx, y(l)), fill=col, width=1)
        y1, y2 = y(o), y(c)
        d.rectangle((xx-candle_w/2, min(y1,y2), xx+candle_w/2, max(y1,y2)+1), fill=col)

    for dt, label in labels:
        if dt in index_by_dt:
            r = cut[index_by_dt[dt]]; xx = x(index_by_dt[dt]); yy = y(r[2]) - 34
            d.ellipse((xx-15, yy-8, xx+15, yy+22), fill="#ffcf55", outline="white", width=1)
            d.text((xx-6, yy-5), label, font=font(18), fill="#101820")

    if risk_lines:
        for name, price, color in risk_lines:
            yy = y(price)
            d.line((left, yy, W-right, yy), fill=color, width=3)
            d.text((W-right-260, yy-24), f"{name}: {price:.5f}", font=font(16), fill=color)

    kind = "SEALED REVEAL" if reveal else "VISIBLE-ONLY DECISION CHART"
    d.text((left, 22), f"{asset_id} — GBP/USD M15 — HistData development Arm A", font=font(25), fill="white")
    d.text((left, 58), f"{kind} — fixed UTC-5 — through {cut[-1][0]:%Y-%m-%d %H:%M}", font=font(18), fill="#ffcf55")
    d.text((left, H-68), f"Week open: {cut[0][0]:%Y-%m-%d %H:%M} | Last visible candle: {cut[-1][0]:%Y-%m-%d %H:%M}", font=font(16), fill="#bac8d3")
    d.text((left, H-38), "No pattern name is implied by raw OHLC or by the blue administration band.", font=font(15), fill="#8fa5b5")
    return im


def write_csv(path, cut):
    with path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["timestamp_utc_minus_5", "open", "high", "low", "close", "volume"])
        for r in cut:
            w.writerow([r[0].strftime("%Y-%m-%d %H:%M"), f"{r[1]:.5f}", f"{r[2]:.5f}", f"{r[3]:.5f}", f"{r[4]:.5f}", r[5]])


def case(case_id, block, videos, concepts, competency, asset, historical, visible, decision,
         instructions, task, markup, explanation, choices, answer, reasoning, citation,
         sequence, rejection, ambiguity, scoring, errors, difficulty, status, provenance,
         lookahead):
    return locals()


def build_cases(weeks):
    cases = []
    asset_specs = {}

    # A — 12 unseen first-eight-hours / first-breach decisions.
    for i, w in enumerate(weeks[0:12], 1):
        cid = f"A{i:02d}"; aid = f"CH_A{i:02d}"
        cut = rows_through(w, w["breach"][0])
        direction = "UPPER" if w["breach"][2] > w["band_hi"] else "LOWER"
        answer = (f"First-eight-hours high {w['band_hi']:.5f}; low {w['band_lo']:.5f}; first breach "
                  f"{direction} at {w['breach'][0]:%Y-%m-%d %H:%M}; NO TRADE in the first-breach direction under the tested V01 prohibition.")
        asset_specs[aid] = (cut, "band", [], None)
        cases.append(case(cid,"A","V01,V03","First-eight-hours context; first-move prohibition; chart markup","Recognition",aid,
            "GBP/USD M15; HistData development Arm A; fixed UTC-5", "Only candles through the first post-band breach; blue band is an administration aid",
            w["breach"][0].strftime("%Y-%m-%d %H:%M UTC-5"), "Open only the named chart/CSV; mark before making a decision",
            "Measure the first eight clock hours, identify the first breach, and classify a trade in that breach direction.",
            "Band high/low, breach candle, rejected direction arrow, and NO TRADE label.",
            "Separate observable price facts from the course prohibition; do not claim dealer intent.",
            "VALID / INVALID / NO TRADE / UNRESOLVED", answer,
            "The range and breach are visible measurements. V01 warns the student not to take the beginning-of-week first move; the administrative band does not prove a trap or a complete setup.",
            "V01_SOURCE_NOTES.md §2c [00:38:27]; V03_SOURCE_NOTES.md §§2a,4a; D-031",
            "Fix clock → mark eight hours → locate first breach → apply prohibition → stop before outcome prediction.",
            "Any later continuation cannot validate taking the prohibited first move.",
            "The course does not mechanically define the blue box or prove that this breach is dealer intent.",
            "Exact range and breach 4; decision 2; markup 2; provenance/uncertainty 2; lookahead 2.",
            "Using later candles; calling the band a universal course box; trading because the breach looks strong.",
            "intermediate","negative/lookalike","INFERRED",
            "Chart and CSV terminate at the decision candle. Cases A01–A04 have sealed post-decision charts for Phase B only."))

    # B — 8 prospective high/low-so-far decisions.
    for i, w in enumerate(weeks[12:20], 1):
        cid=f"B{i:02d}"; aid=f"CH_B{i:02d}"; cut=rows_through(w,w["tue"])
        hirow=max(cut,key=lambda r:r[2]); lorow=min(cut,key=lambda r:r[3])
        asset_specs[aid]=(cut,"plain",[],None)
        answer=(f"High-so-far {hirow[2]:.5f} at {hirow[0]:%Y-%m-%d %H:%M}; low-so-far {lorow[3]:.5f} at "
                f"{lorow[0]:%Y-%m-%d %H:%M}; final PFH/PFL = INSUFFICIENT INFORMATION.")
        cases.append(case(cid,"B","V01,V03,V10","Prospective extremes; PFH/PFL boundary; hindsight control","Ambiguity handling",aid,
            "GBP/USD M15; HistData development Arm A; fixed UTC-5","Candles from week open through Tuesday 12:00 only",w["tue"].strftime("%Y-%m-%d %H:%M UTC-5"),
            "Open only the named visible-only chart/CSV","Mark the exact high-so-far and low-so-far, then decide whether either can be certified as final PFH/PFL.",
            "Two horizontal lines with prices/timestamps and question-marked prospective labels.",
            "Explain the difference between a visible extreme-so-far and V10's retrospective weekly identity.",
            "PFH / PFL / BOTH / INSUFFICIENT INFORMATION",answer,
            "Visible data supports extrema-so-far only. V10 defines PFH/PFL as the completed week's highest/lowest point, while a prospective lock rule remains underdefined.",
            "V10_SOURCE_NOTES.md §7.1 [01:13:58]–[01:14:06]; A-010; A-077",
            "Measure visible extrema → label so-far → test whether week is complete → withhold final identity.",
            "Later-week candles are prohibited; apparent reversal strength is not an exception.",
            "Prospective peak/anchor confirmation remains unresolved through V10.",
            "Exact extrema 4; classification 2; markup 2; uncertainty/provenance 2; lookahead 2.",
            "Calling Tuesday's extreme final; selecting the most dramatic wick; peeking at Friday.",
            "advanced","borderline/insufficient","UNRESOLVED","No bars after Tuesday noon are present."))

    # C — 8 completed-week retrospective PFH/PFL markups.
    for i,w in enumerate(weeks[20:28],1):
        cid=f"C{i:02d}"; aid=f"CH_C{i:02d}"; cut=rows_through(w,w["fri"])
        hirow=max(cut,key=lambda r:r[2]); lorow=min(cut,key=lambda r:r[3]); pips=(hirow[2]-lorow[3])*10000
        asset_specs[aid]=(cut,"plain",[],None)
        answer=(f"PFH {hirow[2]:.5f} at {hirow[0]:%Y-%m-%d %H:%M}; PFL {lorow[3]:.5f} at "
                f"{lorow[0]:%Y-%m-%d %H:%M}; completed-week high-low range {pips:.1f} pips.")
        cases.append(case(cid,"C","V03,V09,V10","Completed-week PFH/PFL; range arithmetic; retrospective boundary","Calculation",aid,
            "GBP/USD M15; completed development week; fixed UTC-5","Full week through Friday 16:45 is intentionally visible",w["fri"].strftime("%Y-%m-%d %H:%M UTC-5"),
            "This is retrospective only; open the named chart/CSV","Locate PFH/PFL precisely and calculate the completed week's high-low range in pips.",
            "Horizontal PFH/PFL lines, timestamps, and range bracket.",
            "State why this completed-week identification is not a prospective entry trigger.","Free response",answer,
            "V10 explicitly defines the completed-week positions; the range is direct arithmetic. No trading edge or real-time peak rule follows.",
            "V10_SOURCE_NOTES.md §7.1; V09_SOURCE_NOTES.md §2 calculation discipline",
            "Confirm week complete → find max high/min low → subtract → convert GBP/USD price difference to pips → bound use.",
            "Do not use PFH/PFL retrospectively to claim an entry was knowable earlier.",
            "Prospective lock and safety-trade entry remain underdefined.",
            "Exact extrema 4; arithmetic 2; markup 2; provenance/boundary 2; lookahead 2.",
            "Using closes instead of extremes; wrong pip conversion; turning the retrospective label into a signal.",
            "intermediate","positive/valid","VISUAL","Full week is permitted solely for the stated retrospective task."))

    # D — 8 raw-chart discrimination tasks controlled by known curriculum gaps.
    d_specs = [
        ("V02,V05,V06,V07","DNC/straightaway recognition","Can this raw chart alone prove a DNC straightaway?","INSUFFICIENT INFORMATION; a breach is visible, but stop-hunt, box, level, and straightaway recognition are not operationally complete.","V02_SOURCE_NOTES.md §2e; V05_SOURCE_NOTES.md pass discipline; A-002/A-006/A-007"),
        ("V04,V05,V06,V07","Complete instructor entry recognition","Can this raw chart alone certify the full V04 instructor entry?","INSUFFICIENT INFORMATION; outside-box location, second-leg M/W, TDI, and entry-close conditions cannot all be graded from this asset.","V04_SOURCE_NOTES.md §§2b–2m; V05_SOURCE_NOTES.md pass discipline; A-039"),
        ("V05","Nameable-pattern pass discipline","No course labels are supplied. Must the student invent a name and trade?","PASS; unclear or non-nameable raw structure is a reason to stay out, not permission to fabricate a pattern.","V05_SOURCE_NOTES.md §§3–5"),
        ("V05,V06","Exact push count","Assign an exact course-valid push count from this raw chart.","UNRESOLVED; push/reset geometry is not mechanically defined, so candidate counts may be question-marked but not certified.","V05_SOURCE_NOTES.md pass discipline; V06_SOURCE_NOTES.md §§2–7; D-030"),
        ("V05,V07","Level and second-leg variant","Assign the exact level and preferred second-leg variant from raw OHLC.","UNRESOLVED; level and second-leg anatomy are not fully defined for blind chart certification.","V05_SOURCE_NOTES.md pass discipline; V07_SOURCE_NOTES.md §§5–11; A-004/A-007"),
        ("V08","Fast-versus-slow timing","Classify the displayed move as FAST or SLOW under V08.","INSUFFICIENT INFORMATION; static M15 OHLC has no intrabar paint-speed evidence and V08 provides no numeric boundary.","V08_SOURCE_NOTES.md §6c; A-061"),
        ("V10","Safety-trade completeness","Can raw OHLC alone certify a complete, executable V10 safety trade?","INSUFFICIENT INFORMATION; the checklist contains undefined visual objects, TDI is deferred, and V10 supplies no safety-trade stop.","V10_SOURCE_NOTES.md §§6–8,15; A-076–A-079"),
        ("V04,V05,V10","Exact blue-box construction","Draw the one exact course-authorized blue box on this raw chart.","UNRESOLVED; multiple box/range descriptions and a personal body-to-body convention do not yield one universal construction rule.","V04_SOURCE_NOTES.md §2; V05_SOURCE_NOTES.md §5g; A-006/A-076"),
    ]
    for i,(videos,concepts,task,answer,citation) in enumerate(d_specs,1):
        w=weeks[28+i-1]; cid=f"D{i:02d}"; aid=f"CH_D{i:02d}"; cut=rows_through(w,w["tue"])
        asset_specs[aid]=(cut,"plain",[],None)
        cases.append(case(cid,"D",videos,concepts,"Discrimination",aid,
            "GBP/USD M15; HistData development Arm A; fixed UTC-5","Unannotated price candles plus the administrative first-eight-hours band",w["tue"].strftime("%Y-%m-%d %H:%M UTC-5"),
            "Use only the chart and Videos 1–10; do not import common internet definitions",task,
            "Mark only objective price facts and question-marked candidates; list every missing prerequisite.",
            "Explain whether the requested conclusion is observable, stipulated, inferred, or unresolved.",
            "VALID / INVALID / PASS / INSUFFICIENT / UNRESOLVED",answer,
            "The practical tests disciplined rejection: undefined pattern geometry must not be converted into a mechanical chart rule.",citation,
            "Inventory required objects → separate visible facts from undefined terms → withhold or pass.",
            "A visually persuasive shape or later outcome cannot supply a missing definition.",
            "The controlling ambiguity is the named concept's unresolved prospective geometry.",
            "Classification 3; missing-input inventory 3; objective markup 2; provenance/uncertainty 2; lookahead 2.",
            "Shape matching; importing outside definitions; giving false certainty; choosing a line after seeing reversal.",
            "advanced","borderline/insufficient","UNRESOLVED","The chart ends at Tuesday noon; no later reversal is visible."))

    # E — 8 basic-confirmation sequence charts. Context and candle A are stipulated.
    for i,w in enumerate(weeks[36:44],1):
        cid=f"E{i:02d}"; aid=f"CH_E{i:02d}"
        base=rows_through(w,w["tue"])
        if i <= 4:
            b=base[-1]; a=base[-2]; intended="LONG" if b[4]>=b[1] else "SHORT"
            cut=base; labels=[(a[0],"A"),(b[0],"B")]
            answer=f"CONFIRMED under the stipulated basic-training sequence for {intended}: A is stipulated as the reversal candle and B is a closed direction candle in the intended direction."
            visible="The prompt stipulates valid location/context and identifies candle A as the reversal candle; candle B is closed"
            decision=b[0]
            status="positive/valid"
        else:
            a=base[-2]; cut=[r for r in base if r[0] <= a[0]]; intended="LONG" if a[4]>=a[1] else "SHORT"
            labels=[(a[0],"A")]
            answer="WAIT; candle A is stipulated as the reversal candle, but no later closed direction candle is visible at this decision point."
            visible="The prompt stipulates valid location/context and identifies the last visible candle A as the reversal candle; no next candle is visible"
            decision=a[0]
            status="negative/lookalike"
        asset_specs[aid]=(cut,"confirmation",labels,None)
        cases.append(case(cid,"E","V04,V08","Basic confirmation sequence; close discipline; advanced-entry boundary","Sequence",aid,
            "GBP/USD M15; HistData development Arm A; fixed UTC-5",visible,decision.strftime("%Y-%m-%d %H:%M UTC-5"),
            "Treat context and candle-A identity as stipulations; grade only the visible confirmation sequence",
            f"For the stipulated {intended} candidate, decide ENTER/WAIT under V08's basic live-training rule.",
            "Label reversal candle A, direction candle B if present, and the earliest permitted basic entry point.",
            "Separate the basic confirmed-entry rule from the demo-only advanced extreme-entry drill.",
            "ENTER / WAIT / INVALID / UNRESOLVED",answer,
            "The basic sequence requires a reversal candle followed by a closed direction candle. Extreme entry is a separate demo practice and cannot erase the basic prerequisite.",
            "V08_SOURCE_NOTES.md §6; C-009; V04_SOURCE_NOTES.md entry-close sequence",
            "Verify stipulated context → identify A → require closed B in direction → enter or wait → keep demo rule separate.",
            "A future B candle may not be anticipated; later profitability cannot repair an early entry.",
            "The broader pattern geometry is stipulated so the case isolates confirmation rather than pretending blind recognition is solved.",
            "Decision 3; candle markup 3; sequence/reasoning 2; provenance/uncertainty 2; lookahead 2.",
            "Entering on A; reading an unclosed candle; treating demo extreme entry as the novice live rule.",
            "intermediate",status,"INFERRED","The chart ends exactly at the candle used for the decision."))

    # F — 8 chart-anchored risk/position-sizing cases.
    risk_specs = [
        (10000,25,"single","Risk $200; $8.00 per pip. Lot conversion requires the broker/instrument pip-value convention."),
        (12000,15,"single","Risk $240; $16.00 per pip. Lot conversion requires the broker/instrument pip-value convention."),
        (8000,20,"two_equal","Total risk $160; allocate $80 to each of two simultaneous trades. At 20 and 25 pip stops: $4.00/pip and $3.20/pip."),
        (25000,25,"three_over","REJECT three separate 2% risks: proposed exposure is 6% or $1,500. Total allowed exposure is 2% or $500 across all simultaneous positions."),
        (9400,25,"loss3","Maintain the previously established size through loss 3 under the explicit sequence; do not recalculate merely because balance fell. Hard stop remains required."),
        (9200,25,"loss4","After loss 4 recalculate: risk $184; $7.36 per pip for the stipulated 25-pip stop."),
        (11960,25,"win","After the win recalculate: risk $239.20; $9.568/pip, normally recorded as $9.57/pip subject to execution precision."),
        (10000,0,"no_stop","Risk budget is $200, but $/pip and lot size are UNRESOLVED because Videos 1–10 supply no valid safety-trade stop distance for this candidate."),
    ]
    for i,(balance,stop,kind,answer) in enumerate(risk_specs,1):
        w=weeks[44+i-1]; cid=f"F{i:02d}"; aid=f"CH_F{i:02d}"; cut=rows_through(w,w["tue"]); entry=cut[-1][4]
        risk_lines=None
        if stop:
            stop_price=entry-stop/10000; target=entry+50/10000
            risk_lines=[("STIPULATED ENTRY",entry,"#ffcf55"),("ADMIN STOP",stop_price,"#ef5d72"),("50-PIP REFERENCE",target,"#2bc48a")]
        asset_specs[aid]=(cut,"risk",[],risk_lines)
        if kind=="two_equal": visible=f"Balance ${balance:,}; two simultaneous trades; equal risk allocation; stops 20 and 25 pips"
        elif kind=="three_over": visible=f"Balance ${balance:,}; proposal risks 2% independently on each of three simultaneous trades"
        elif kind=="loss3": visible=f"Balance ${balance:,}; this is loss number 3; previously established size is $8.00/pip; stipulated 25-pip stop"
        elif kind=="loss4": visible=f"Balance ${balance:,}; fourth loss has just closed; next valid trade has a separately stipulated 25-pip stop"
        elif kind=="win": visible=f"Balance ${balance:,} after a win; next valid trade has a separately stipulated 25-pip stop"
        elif kind=="no_stop": visible=f"Balance ${balance:,}; chart is proposed as a V10 safety trade, but no valid stop distance is supplied"
        else: visible=f"Balance ${balance:,}; one valid trade; separately stipulated {stop}-pip stop"
        cases.append(case(cid,"F","V09,V10","Risk budget; cumulative exposure; size sequence; stop-input boundary","Calculation",aid,
            "GBP/USD M15 development chart plus stipulated account facts",visible,w["tue"].strftime("%Y-%m-%d %H:%M UTC-5"),
            "Use chart prices only where marked; the displayed stop is an exam stipulation, not a recovered safety-trade rule",
            "Calculate the permitted risk and position-size input, or reject/withhold when a required input is absent.",
            "Annotate entry, stipulated stop, 50-pip reference where shown, account risk budget, and simultaneous exposure.",
            "Show formula, units, sequence rule, and the boundary between V09 arithmetic and V10 setup doctrine.",
            "CALCULATE / REJECT OVER-RISK / INSUFFICIENT STOP INPUT",answer,
            "V09 defines cumulative account risk and the recalculation sequence. Arithmetic is permitted only after a valid stop distance is independently supplied; V10 does not supply one for the safety trade.",
            "V09_SOURCE_NOTES.md §§2–5; V10_SOURCE_NOTES.md §15; A-065",
            "Check valid stop input → compute balance × .02 → allocate cumulatively → divide by stop pips → apply loss/win recalculation sequence.",
            "Reject any plan exceeding cumulative 2%; do not invent a V10 stop from chart appearance.",
            "Broker pip value and lot conversion remain external inputs; safety-trade stop placement is unresolved.",
            "Risk/classification 3; arithmetic 3; chart plan 2; sequence/provenance 2; lookahead 2.",
            "Applying 2% per position; manufacturing a stop; resizing after every loss; omitting units.",
            "advanced","positive/valid" if kind not in {"three_over","no_stop"} else "negative/lookalike",
            "INFERRED","No future price outcome is used; the chart anchors the plan, not setup profitability."))

    # G — 8 recording-derived chart-source audits.
    g_specs = [
        ("V01,V02","Typical-week completed chart","SRC01_V01_TYPICAL_WEEK","Identify the visible day labels and instructor annotations, then state whether this completed example can prove the same path on an unseen week.","Mark Sunday through Friday and the visible trapped-holder/swing annotations. Conclusion: VISUAL teaching example only; it cannot forecast an unseen week.","V01_SOURCE_NOTES.md §§2c–2e [00:50:55]; V02_SOURCE_NOTES.md weekly-structure continuation"),
        ("V02","Completed pop-quiz chart","SRC02_V02_POP_QUIZ","Inventory the visible boxes, R labels, moving averages and TDI panel; can the screenshot alone supply a prospective mechanical 22 rule?","Visible objects may be transcribed; a prospective mechanical 22 classification remains unresolved because exact anatomy/tolerance is not fully operational.","V02_SOURCE_NOTES.md §§2a,2i [00:52:40]"),
        ("V02,V03","Flashcard construction audit","SRC03_V03_FLASHCARD","Audit this completed flashcard as a possible unseen decision test. Where must a hard-right-edge crop occur?","The completed image is valid source evidence but contaminated as an unseen decision test; crop before any candles/annotations that reveal completion or outcome.","V02_SOURCE_NOTES.md R&D flashcard assignment; V03_SOURCE_NOTES.md §§2h–2j [00:43:09]"),
        ("V04","Second-leg teaching chart","SRC04_V04_SECOND_LEG","Mark the visible box, over-high structure, hand-drawn M/second-leg region, and later decline. What can be claimed prospectively?","The annotations are VISUAL evidence of the taught example; the later decline cannot define a blind entry, and missing TDI/operational geometry prevents transfer as a complete rule.","V04_SOURCE_NOTES.md §§2b–2m [00:08:40]"),
        ("V06","Push-label teaching chart","SRC05_V06_PUSHES","Transcribe Push 1, Push 2, Push 3, levels, and entries. Does this one annotated chart define a universal push-count algorithm?","No. The labels are VISUAL teaching evidence; universal push/reset geometry remains unresolved and the withdrawn nine-candle claim is not a rule.","V06_SOURCE_NOTES.md §§2–7 [01:14:09]; D-030"),
        ("V07","Chart-furniture and stair-step example","SRC06_V07_STAIR_STEP","Identify visible day separator, marked boxes/arrows, and moving-average context. State the naming boundary.","Visible furniture and stair-step example may be marked; incomplete nickname-to-period mapping and level/second-leg geometry must remain unresolved.","V07_SOURCE_NOTES.md §§5–11 [00:27:00]"),
        ("V08","High-low drill source boundary","SRC07_V08_HIGH_LOW","Separate what the screenshot demonstrates from the basic live-training confirmation rule.","The screenshot VISUALLY demonstrates the advanced/demo extreme-entry idea; it does not repeal the basic reversal-then-direction-candle live-training sequence or validate profitability.","V08_SOURCE_NOTES.md §6 [00:38:10]; C-009"),
        ("V10","Safety-trade walkthrough audit","SRC08_V10_SAFETY","Identify the visible completed boxes/levels, then decide whether this image supplies a stop, lot size, or prospective PFH/PFL lock.","It supplies VISUAL teaching context only. No safety-trade stop or lot size is taught, and completed-chart peak identity cannot be silently converted into a prospective lock rule.","V10_SOURCE_NOTES.md §§6–8,15 [01:01:22]"),
    ]
    for i,(videos,concepts,aid,task,answer,citation) in enumerate(g_specs,1):
        cid=f"G{i:02d}"
        cases.append(case(cid,"G",videos,concepts,"Provenance",aid,
            "Original indexed Bootcamp screenshot from the named recording","The entire completed teaching screenshot is visible; it is not an unseen replay", "Recording timestamp printed in asset provenance",
            "Use the screenshot only as source evidence; do not infer future performance or import Video 11",task,
            "Mark every requested visible object and draw a hard boundary between screenshot fact and transferable rule.",
            "Use VISUAL/EXPLICIT/INFERRED/UNRESOLVED labels claim by claim.","Free response",answer,
            "A completed recording screenshot can establish what was shown and annotated. It cannot by itself supply missing prospective definitions or prove an edge.",citation,
            "Inventory visible objects → connect only source-supported teaching → identify hindsight/completion → preserve unresolved transfer limits.",
            "Reject any claim that later movement validates the setup or that one screenshot defines universal geometry.",
            "Dates/feed details are often unrecoverable; several chart terms remain undefined through V10.",
            "Visual inventory 3; source boundary 3; reasoning/sequence 2; provenance/uncertainty 2; lookahead 2.",
            "Treating annotations as an algorithm; copying future outcome into a decision card; claiming profitability.",
            "advanced","neutral","VISUAL","The whole completed image is allowed only because the task audits source evidence, not a live decision."))

    if len(cases) != 60:
        raise RuntimeError(f"Expected 60 cases, got {len(cases)}")
    return cases, asset_specs


def student_block(c):
    return f"""## {c['case_id']} — {c['concepts']}

| Field | Student-facing specification |
|---|---|
| Videos and concepts tested | {c['videos']} — {c['concepts']} |
| Competency category | {c['competency']} |
| Instrument and timeframe | GBP/USD M15 unless the named source card shows another instrument |
| Historical date and data source | {c['historical']} |
| Information visible to student | {c['visible']} |
| Exact decision timestamp | {c['decision']} |
| Chart/replay instructions | {c['instructions']} |
| Asset | `{c['asset']}` |
| Student task | {c['task']} |
| Required chart markup | {c['markup']} |
| Required explanation | {c['explanation']} |
| Allowed answer choices | {c['choices']} |
| Source boundary | Videos 1–10 and the named chart only; controlling citation is sealed. |
| Difficulty | {c['difficulty']} |
| Lookahead-contamination check | {c['lookahead']} Lock the answer before any reveal. |

Student response must include: first classification; marked chart filename; measured values/calculation; ordered reasoning; provenance label for each material claim; confidence; missing information; `FUTURE INFORMATION USED: NO`; and `LOCKED <timestamp>`.

"""


def key_block(c):
    return f"""## {c['case_id']} — {c['concepts']}

| Field | Instructor key |
|---|---|
| Videos and concepts tested | {c['videos']} — {c['concepts']} |
| Competency category | {c['competency']} |
| Instrument and timeframe | GBP/USD M15 unless source card states otherwise |
| Historical date and data source | {c['historical']} |
| Information visible to student | {c['visible']} |
| Exact decision timestamp | {c['decision']} |
| Chart/replay instructions | {c['instructions']} |
| Asset | `{c['asset']}` |
| Student task | {c['task']} |
| Required markup | {c['markup']} |
| Required explanation | {c['explanation']} |
| Allowed choices | {c['choices']} |
| Correct answer | **{c['answer']}** |
| Evidence-based reasoning | {c['reasoning']} |
| Source citation | {c['citation']} |
| Expected-answer provenance | **{c['provenance']}** |
| Expected sequence of reasoning | {c['sequence']} |
| Valid rejection/invalidation conditions | {c['rejection']} |
| Ambiguities affecting answer | {c['ambiguity']} |
| Scoring criteria | {c['scoring']} Apply the 12-point rubric. |
| Common student errors | {c['errors']} |
| Difficulty | {c['difficulty']} |
| Case status | {c['status']} |
| Lookahead check | {c['lookahead']} |

"""


def build():
    for p in (ROOT, ROOT/"tools", ASSETS, CHARTS, CSVS, CARDS, SEALED):
        p.mkdir(parents=True, exist_ok=True)
    rows=load_rows(); weeks=week_map(rows); cases, specs=build_cases(weeks)
    manifest=[]
    for aid,(cut,mode,labels,risk_lines) in specs.items():
        img=draw_chart(aid,cut,mode,labels,risk_lines)
        ip=CHARTS/f"{aid}_visible_only.png"; cp=CSVS/f"{aid}_visible_only.csv"
        img.save(ip); write_csv(cp,cut)
        manifest.append((aid,"visible-only historical chart",ip,sha256(ip),f"{cut[0][0]} through {cut[-1][0]}; {len(cut)} M15 bars"))
        manifest.append((aid+"_CSV","visible-only data",cp,sha256(cp),f"Ends exactly {cut[-1][0]} fixed UTC-5"))

    for aid,src in SOURCE_CARDS.items():
        if not src.exists(): raise RuntimeError(f"Missing {src}")
        dst=CARDS/(aid+src.suffix.lower()); shutil.copy2(src,dst)
        manifest.append((aid,"unaltered lesson screenshot",dst,sha256(dst),str(src.relative_to(REPO))))

    # Sealed 24-hour continuations for four hindsight-control checks.
    reveal_rows=[]
    for i,w in enumerate(weeks[0:4],1):
        cid=f"A{i:02d}"; decision=w["breach"][0]; end=min(decision+timedelta(hours=24),w["fri"])
        cut=rows_through(w,end); ip=SEALED/f"{cid}_24H_REVEAL.png"
        draw_chart(f"{cid}_24H_REVEAL",cut,"plain",reveal=True).save(ip)
        delta=(cut[-1][4]-w["breach"][4])*10000
        reveal_rows.append((cid,ip,delta,sha256(ip)))

    (ROOT/"STUDENT_PRACTICAL_PACKET.md").write_text(
        "# Student Practical Examination — Videos 1–10\n\n"
        "**Closed book. Chart first. No Video 11. No instructor key. No adjacent assets.**\n\n"
        "There are 60 scored cases, all anchored to a chart or original lesson chart-image. Work directly on a duplicate of each named image. Preserve the unmarked original. Every historical decision chart is cut at its printed timestamp; completed source screenshots are used only for provenance audits.\n\n"
        "Do not infer an entry merely because candles form a familiar shape. When a required term remains undefined, mark objective facts, list missing inputs, and answer `UNRESOLVED`, `INSUFFICIENT`, or `PASS`.\n\n"+
        "".join(student_block(c) for c in cases))

    (ROOT/"INSTRUCTOR_ANSWER_KEY.md").write_text(
        "# Instructor Answer Key — Chart-Heavy Practical Videos 1–10\n\n"
        "Keep sealed. Grade the first locked decision before revealing any later chart. Correct arithmetic or profitable movement never repairs an invalid application.\n\n"+
        "".join(key_block(c) for c in cases))

    (ROOT/"COVERAGE_MATRIX.md").write_text(
        "# Coverage Matrix\n\n| Case | Block | Videos | Concept | Competency | Difficulty | Status | Provenance | Asset |\n|---|---|---|---|---|---|---|---|---|\n"+
        "".join(f"| {c['case_id']} | {c['block']} | {c['videos']} | {c['concepts']} | {c['competency']} | {c['difficulty']} | {c['status']} | {c['provenance']} | {c['asset']} |\n" for c in cases))

    results=["# Practical Examination Results Template\n\nAttempt ID:  \nStudent (AI agent):  \nExam start:  \nExam end:  \nPacket SHA-256:  \nAsset-index SHA-256:  \nInstructor:  \n\nNever overwrite the first attempt. Attach marked-chart paths and hashes.\n\n",
             "| Case | First classification | Marked chart | Measurements/calculation | Reasoning | Provenance | Confidence | Missing information | Future used? | Lock timestamp | Score /12 | Critical code | Instructor note |\n|---|---|---|---|---|---|---:|---|---|---|---:|---|---|\n"]
    for c in cases:
        results.append(f"| {c['case_id']} |  |  |  |  |  |  |  | NO |  |  |  |  |\n")
    results.append("\n## Staged reveal ledger\n\n| Case | Original answer preserved? | Revealed chart | Outcome description | Application/outcome quadrant | Phase-B lock |\n|---|---|---|---|---|---|\n")
    for cid in ["A01","A02","A03","A04"]:
        results.append(f"| {cid} |  |  |  |  |  |\n")
    results.append("\n## Section and gate summary\n\n| Area | Earned | Available | Percent | Pass/fail | Remediation |\n|---|---:|---:|---:|---|---|\n")
    for label in ["Block A","Block B","Block C","Block D","Block E","Block F","Block G","Markup","Decision/reasoning","Calculation","Provenance/uncertainty","Lookahead","Overall"]:
        results.append(f"| {label} |  |  |  |  |  |\n")
    (ROOT/"RESULTS_TEMPLATE.md").write_text("".join(results))

    by_asset={a:[] for a in [*specs,*SOURCE_CARDS]}
    for c in cases: by_asset[c["asset"]].append(c["case_id"])
    idx=["# Practical Exam Asset Index\n\nOnly open assets named by the assigned case. `instructor_only/` is forbidden during an attempt.\n\n",
         "## Visible-only historical charts\n\n| ID | Chart | CSV | Used by |\n|---|---|---|---|\n"]
    for aid in specs:
        idx.append(f"| {aid} | [open](charts/{aid}_visible_only.png) | [data](visible_only_csv/{aid}_visible_only.csv) | {', '.join(by_asset[aid])} |\n")
    idx.extend(["\n## Recording-derived source charts\n\n| ID | Image | Used by |\n|---|---|---|\n"])
    for aid,src in SOURCE_CARDS.items():
        idx.append(f"| {aid} | [open](source_cards/{aid}{src.suffix.lower()}) | {', '.join(by_asset[aid])} |\n")
    (ASSETS/"ASSET_INDEX.md").write_text("".join(idx))

    prov=["# Asset and Data Provenance\n\nThe historical charts derive only from the repository's HistData GBP/USD M15 Arm A development corpus (fixed UTC-5) ending 2016-06-30. The absent reserved holdout beginning 2016-07-01 was not used. All decision CSVs end exactly at their printed boundary. The blue band is an administration aid. Source charts are byte-for-byte copies of indexed recording screenshots.\n\n",
          "| ID | Type | Relative path | SHA-256 | Scope/source |\n|---|---|---|---|---|\n"]
    for aid,typ,path,digest,note in manifest:
        prov.append(f"| {aid} | {typ} | `{path.relative_to(ROOT)}` | `{digest}` | {note} |\n")
    (ASSETS/"DATA_PROVENANCE.md").write_text("".join(prov))

    reveal_doc=["# Instructor Reveal Protocol\n\nKeep this file and `sealed_reveals/` inaccessible until Phase A for the named case is locked. Show the image; ask whether the original decision changes and why. The correct response is always to preserve the decision-time classification and describe later movement separately.\n\n",
                "| Case | Sealed chart | 24-hour-close change from decision close | Required Phase-B response |\n|---|---|---:|---|\n"]
    for cid,ip,delta,digest in reveal_rows:
        reveal_doc.append(f"| {cid} | `{ip.relative_to(ROOT)}` (`{digest}`) | {delta:+.1f} pips | Preserve Phase A; later direction does not prove or disprove rule application. |\n")
    (ROOT/"instructor_only"/"REVEAL_PROTOCOL.md").write_text("".join(reveal_doc))

    summary={
        "cases":len(cases),"historical_chart_assets":len(specs),"source_chart_assets":len(SOURCE_CARDS),
        "sealed_reveals":len(reveal_rows),"total_scored_points":len(cases)*12,
        "by_block":dict(Counter(c["block"] for c in cases)),
        "by_status":dict(Counter(c["status"] for c in cases)),
        "by_video":{f"V{i:02d}":sum(f"V{i:02d}" in c["videos"] for c in cases) for i in range(1,11)},
        "by_competency":dict(Counter(c["competency"] for c in cases)),
    }
    (ROOT/"VALIDATION_SUMMARY.json").write_text(json.dumps(summary,indent=2)+"\n")


if __name__ == "__main__":
    build()
