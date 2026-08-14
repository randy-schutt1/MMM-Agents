#!/usr/bin/env python3
"""Build the two-phase HOW/LOW, HOD/LOD, and signature-trade practical."""

from __future__ import annotations

import csv
import hashlib
import json
import random
from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parent
DATA=REPO/"06_MANUAL_BACKTEST/datasets/HISTDATA_GBPUSD_M1/GBPUSD_M15_ARMA.csv"
ASSETS=ROOT/"assets"
DECISION=ASSETS/"decision_charts"
DECISION_CSV=ASSETS/"decision_csv"
REVEALS=ROOT/"instructor_only"/"completed_week_reveals"
REVEAL_CSV=ROOT/"instructor_only"/"completed_week_csv"


def font(size):
    for p in ("/System/Library/Fonts/Supplemental/Arial.ttf","/System/Library/Fonts/Supplemental/Helvetica.ttf"):
        if Path(p).exists(): return ImageFont.truetype(p,size)
    return ImageFont.load_default()


def sha256(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()


def load_rows():
    out=[]
    with DATA.open(newline="") as f:
        for r in csv.reader(f):
            dt=datetime.strptime(r[0]+" "+r[1],"%Y.%m.%d %H:%M")
            out.append((dt,float(r[2]),float(r[3]),float(r[4]),float(r[5]),int(r[6])))
    return out


def prior_week_starts():
    used=set()
    for base in (REPO/"19_STUDENT_TEST_SUITE_V01_V10/assets/visible_only_csv",REPO/"20_CHART_HEAVY_PRACTICAL_V01_V10/assets/visible_only_csv"):
        if not base.exists(): continue
        for p in base.glob("*.csv"):
            with p.open() as f:
                rows=list(csv.DictReader(f))
            if rows:
                key="timestamp_utc_minus_5"
                used.add(rows[0][key][:10])
    return used


def collect_weeks(rows):
    by_dt={r[0]:r for r in rows}; used=prior_week_starts(); weeks=[]
    starts=[r[0] for r in rows if r[0].weekday()==6 and r[0].hour==17 and r[0].minute==0]
    for start in starts:
        if start.strftime("%Y-%m-%d") in used: continue
        closes=[start+timedelta(days=d,hours=23,minutes=45) for d in range(5)]
        if any(x not in by_dt for x in closes): continue
        full=[r for r in rows if start<=r[0]<=closes[4]]
        if len(full)<400: continue
        # Rank visual extrema difficulty using prominence of top/bottom observations.
        hs=sorted((r[2] for r in full),reverse=True); ls=sorted(r[3] for r in full)
        span=max(hs[0]-ls[0],1e-9)
        prominence=((hs[0]-hs[min(8,len(hs)-1)])+(ls[min(8,len(ls)-1)]-ls[0]))/span
        weeks.append(dict(start=start,closes=closes,full=full,prominence=prominence))
    if len(weeks)<36: raise RuntimeError(f"Only {len(weeks)} unused complete weeks")
    weeks=sorted(weeks,key=lambda w:w["prominence"],reverse=True)
    easy=weeks[:12]
    hard=weeks[-12:]
    mid_pool=[w for w in weeks if w not in easy and w not in hard]
    mid=mid_pool[::max(1,len(mid_pool)//12)][:12]
    selected=easy+mid+hard
    remaining=[w for w in weeks if w not in selected]
    stride=max(1,len(remaining)//10)
    extras=remaining[::stride][:10]
    selected += extras
    if len(selected)!=46 or len({w["start"] for w in selected})!=46: raise RuntimeError("Week selection overlap/count")
    return selected


def write_csv(path,rows):
    with path.open("w",newline="") as f:
        w=csv.writer(f); w.writerow(["timestamp_utc_minus_5","open","high","low","close","volume"])
        for r in rows: w.writerow([r[0].strftime("%Y-%m-%d %H:%M"),f"{r[1]:.5f}",f"{r[2]:.5f}",f"{r[3]:.5f}",f"{r[4]:.5f}",r[5]])


def draw_chart(case_id,rows,day_start,day_end,difficulty,facts,reveal=False):
    W,H=1800,980; left,right,top,bottom=100,390,105,105
    pw,ph=W-left-right,H-top-bottom
    lo=min(r[3] for r in rows); hi=max(r[2] for r in rows); pad=max((hi-lo)*.06,.0004); lo-=pad; hi+=pad
    def x(i): return left+(i+.5)*pw/len(rows)
    def y(v): return top+(hi-v)*ph/(hi-lo)
    im=Image.new("RGB",(W,H),"#0b1520"); d=ImageDraw.Draw(im)
    for j in range(7):
        yy=top+j*ph/6; d.line((left,yy,left+pw,yy),fill="#263b4c",width=1)
        d.text((8,yy-8),f"{hi-j*(hi-lo)/6:.5f}",font=font(14),fill="#aebdca")
    day_indices=[i for i,r in enumerate(rows) if day_start<=r[0]<=day_end]
    if day_indices:
        d.rectangle((x(day_indices[0])-3,top,x(day_indices[-1])+3,top+ph),fill="#132c3b",outline="#58b8e6",width=2)
        d.text((x(day_indices[0])+8,top+8),f"TARGET TRADING DAY {day_start:%a %m-%d %H:%M} to {day_end:%a %m-%d %H:%M}",font=font(14),fill="#6bd3ff")
    seen=set()
    for i,r in enumerate(rows):
        date=r[0].date()
        if date not in seen:
            seen.add(date); xx=x(i); d.line((xx,top,xx,top+ph),fill="#3b5264",width=1); d.text((xx+4,top+ph-20),r[0].strftime("%a %m-%d"),font=font(12),fill="#9eb0bf")
    cw=max(2,int(pw/len(rows)*.62))
    for i,r in enumerate(rows):
        _,o,h,l,c,_=r; xx=x(i); col="#2bc48a" if c>=o else "#ef5d72"
        d.line((xx,y(h),xx,y(l)),fill=col,width=1); d.rectangle((xx-cw/2,min(y(o),y(c)),xx+cw/2,max(y(o),y(c))+1),fill=col)
    panel_x=left+pw+25
    d.rounded_rectangle((panel_x,top,panel_x+340,top+ph),radius=15,fill="#111f2b",outline="#4c6678",width=2)
    panel_title="PHASE B — EXTREMA REVEAL" if reveal else "PHASE A — SIGNATURE FACTS"
    d.text((panel_x+18,top+18),panel_title,font=font(18),fill="#ffcf55")
    yy=top+60
    lines=["Official signature trade:","V10 Safety Trade",""]
    if reveal:
        lines += ["Full week intentionally visible.","Mark HOW and LOW.","Do NOT revise Phase A.","",f"Difficulty: {difficulty.upper()}"]
    else:
        lines += facts+["","Classify checklist only.","No stop or profitability", "is implied.","",f"Difficulty: {difficulty.upper()}"]
    for line in lines:
        d.text((panel_x+18,yy),line,font=font(15 if len(line)>30 else 16),fill="white" if line else "#8fa5b5"); yy+=29
    phase="COMPLETED-WEEK REVEAL" if reveal else "VISIBLE-ONLY DECISION"
    d.text((left,22),f"{case_id} — GBP/USD M15 — {difficulty.upper()}",font=font(26),fill="white")
    d.text((left,60),f"{phase} — fixed UTC-5 — through {rows[-1][0]:%Y-%m-%d %H:%M}",font=font(18),fill="#ffcf55")
    d.text((left,H-65),f"Week begins {rows[0][0]:%Y-%m-%d %H:%M} | Chart ends {rows[-1][0]:%Y-%m-%d %H:%M}",font=font(16),fill="#bac8d3")
    d.text((left,H-36),"Trading day boundary is an examination input, not a claimed universal Bootcamp session clock.",font=font(15),fill="#8fa5b5")
    return im


def scenario(index,difficulty):
    peak="PFH" if index%2 else "PFL"; direction="SHORT" if peak=="PFH" else "LONG"; pattern="second-leg M" if peak=="PFH" else "second-leg W"
    all_yes=[f"Peak candidate: {peak} (stipulated)","Pull-away/lock: YES","Level-1 consolidation: YES",f"Direction away: {direction}","Visible stop hunt: YES","Beyond-box novice test: YES",f"Second leg: {pattern} (stipulated)"]
    if difficulty=="easy":
        if index<=6: return all_yes,"VALID CHECKLIST",f"V10 safety-trade checklist is valid under the stipulated facts; direction {direction} away from {peak}. No executable trade is established because V10 supplies no safety-trade stop."
        mods={7:(4,"Visible stop hunt: NO","INVALID — missing visible stop hunt"),8:(6,"Second leg: NO","WAIT/INCOMPLETE — missing second-leg M/W"),9:(3,"Direction: TOWARD PEAK","INVALID/DNC — candidate trades back toward the peak"),10:(1,"Pull-away/lock: NO","WAIT/INCOMPLETE — peak not confirmed by pull-away"),11:(2,"Level-1 consolidation: NOT CLEAR","INSUFFICIENT/WAIT — consolidation prerequisite is not clear"),12:(0,"Peak candidate: NOT STIPULATED","UNRESOLVED — prospective peak identity is not established")}
        pos,text,label=mods[index]; f=all_yes[:]; f[pos]=text; return f,label,label
    if difficulty=="intermediate":
        if index<=3:
            facts=all_yes[:]; facts=[facts[j] for j in (2,5,0,6,1,3,4)]
            return facts,"VALID CHECKLIST",f"All V10 checklist facts are stipulated despite scrambled presentation; trade direction is {direction} away from {peak}. Stop/position size remain unavailable."
        if index==4:
            f=all_yes[:]; f[4]="Visible stop hunt: NO"; return f,"INVALID","INVALID — no visible stop hunt."
        if index==5:
            f=all_yes[:]; f[3]="Direction: TOWARD PEAK"; return f,"INVALID/DNC","INVALID/DNC — direction is back toward the peak."
        if index==6:
            f=all_yes[:]; f[6]="Second leg: NOT PRESENT"; return f,"WAIT","WAIT — second-leg M/W is missing."
        if index==7:
            f=all_yes[:]; f[2]="Consolidation: NOT SUPPLIED"; return f,"UNRESOLVED","UNRESOLVED — level-one consolidation is not supplied."
        if index==8:
            f=all_yes[:]; f[4]="Stop hunt: VISUAL CANDIDATE ONLY"; return f,"UNRESOLVED","UNRESOLVED — a visual candidate is not a certified stop hunt without an operational boundary."
        if index==9:
            f=all_yes[:]; f[1]="Lock duration: 1 day / 3 days conflict"; return f,"UNRESOLVED","UNRESOLVED — the controlling lock-duration conflict remains open."
        if index==10: return all_yes,"VALID CHECKLIST / NOT EXECUTABLE",f"Checklist valid under stipulations; not executable because no safety-trade stop is taught in V10."
        if index==11:
            return ["Repeated level: YES","Second leg of second leg: YES","Return through level: YES","Safety prerequisites: NOT SUPPLIED"],"22 CANDIDATE; SIGNATURE UNRESOLVED","A stipulated V02 22 candidate is present, but the official V10 safety/signature checklist is unresolved."
        return ["No stop hunt below box: STIPULATED","Straightaway: STIPULATED","Counter direction: TOWARD RANGE","Safety prerequisites: NOT SUPPLIED"],"STRAIGHTAWAY/DNC; SIGNATURE INCOMPLETE","V02 straightaway/DNC applies; no complete V10 signature-trade checklist is established."
    return ["Raw OHLC only","No peak/lock stipulation","No level definition supplied","No stop-hunt certification","No second-leg certification","No TDI rule through V10"],"UNRESOLVED / NONE CONFIRMABLE","No official V10 signature trade can be certified from raw OHLC alone; candidate shapes may be question-marked only."


def build_cases(weeks):
    cases=[]
    for n,w in enumerate(weeks[:36]):
        difficulty="easy" if n<12 else "intermediate" if n<24 else "difficult"
        idx=n%12+1; prefix={"easy":"E","intermediate":"I","difficult":"D"}[difficulty]; cid=f"{prefix}{idx:02d}"
        day_index={"easy":0,"intermediate":1,"difficult":2}[difficulty]
        day_end=w["closes"][day_index]; day_start=day_end-timedelta(hours=23,minutes=45)
        decision=[r for r in w["full"] if r[0]<=day_end]; target=[r for r in decision if day_start<=r[0]<=day_end]
        hod=max(target,key=lambda r:r[2]); lod=min(target,key=lambda r:r[3]); how=max(w["full"],key=lambda r:r[2]); low=min(w["full"],key=lambda r:r[3])
        facts,sig_class,sig_answer=scenario(idx,difficulty)
        cases.append(dict(id=cid,kind="extrema_signature",difficulty=difficulty,week=w,day_start=day_start,day_end=day_end,decision=decision,target=target,
                          hod=hod,lod=lod,how=how,low=low,facts=facts,sig_class=sig_class,sig_answer=sig_answer))

    direction_specs=[
        ("intermediate",1,["Peak: PFL (stipulated)","Pull-away/lock: YES","Level-1 consolidation: YES","Visible stop hunt: YES","Second leg W: YES","Required direction: AWAY/UP"],"BUY","BUY — all stipulated V10 safety prerequisites align away from the PFL. Mark the long arrow only after the second-leg W."),
        ("easy",0,["Peak: PFH (stipulated)","Pull-away/lock: YES","Level-1 consolidation: YES","Visible stop hunt: YES","Second leg M: YES","Required direction: AWAY/DOWN"],"SELL","SELL — all stipulated V10 safety prerequisites align away from the PFH. Mark the short arrow only after the second-leg M."),
        ("difficult",2,["Peak: PFL (stipulated)","Pull-away/lock: YES","Consolidation: YES","Stop hunt beyond box: YES","Second leg W: YES","Direction away: UP"],"BUY","BUY — the stipulated complete checklist supports the away-from-PFL direction; chart shape alone is not the source of validity."),
        ("intermediate",1,["Peak: PFH (stipulated)","Pull-away/lock: YES","Consolidation: YES","Stop hunt beyond box: YES","Second leg M: YES","Direction away: DOWN"],"SELL","SELL — the stipulated complete checklist supports the away-from-PFH direction."),
        ("easy",0,["Peak: PFH (stipulated)","Consolidation: YES","Candidate direction: UP/TOWARD PEAK","Visible stop hunt: YES","Second leg W candidate: YES","DNC: ACTIVE"],"NO TRADE / DNC","NO TRADE — the proposed buy points back toward the PFH and is explicitly DNC."),
        ("difficult",2,["Peak: PFL (stipulated)","Pull-away/lock: YES","Consolidation: YES","Visible stop hunt: NO","Second leg W candidate: YES","Candidate direction: UP"],"NO TRADE","NO TRADE — a required visible stop hunt is absent; a bullish-looking outcome cannot repair it."),
        ("intermediate",1,["Peak: PFH (stipulated)","Pull-away/lock: YES","Consolidation: YES","Visible stop hunt: YES","Second leg M: NOT YET PRESENT","Candidate direction: DOWN"],"WAIT","WAIT — the direction may be away from the PFH, but the required second-leg M has not appeared."),
        ("difficult",2,["Peak candidate: PFL?","Pull-away/lock: NOT CONFIRMED","Consolidation: candidate only","Visible stop hunt: candidate only","Second leg W: candidate only","Direction proposal: UP"],"WAIT / UNRESOLVED","WAIT/UNRESOLVED — peak confirmation and other prerequisites are not established; do not buy from shape alone."),
        ("easy",0,["Raw OHLC only","No peak stipulation","No stop-hunt certification","No second-leg certification","No TDI rule through V10","Direction must be decided now"],"UNRESOLVED","UNRESOLVED — neither BUY nor SELL is source-supported from raw OHLC alone."),
        ("difficult",2,["Peak evidence: CONFLICTING","Lock duration: 1 day / 3 days conflict","Level: NOT DEFINED","Stop hunt: NOT CERTIFIED","Second leg: NOT CERTIFIED","Direction proposal: unspecified"],"UNRESOLVED","UNRESOLVED — the evidence does not support a buy or sell decision and conflicts may not be silently resolved."),
    ]
    new=[]
    for j,(difficulty,day_index,facts,decision_class,decision_answer) in enumerate(direction_specs,1):
        w=weeks[35+j]; cid=f"M{j:02d}"; day_end=w["closes"][day_index]; day_start=day_end-timedelta(hours=23,minutes=45)
        decision=[r for r in w["full"] if r[0]<=day_end]; target=[r for r in decision if day_start<=r[0]<=day_end]
        hod=max(target,key=lambda r:r[2]); lod=min(target,key=lambda r:r[3]); how=max(w["full"],key=lambda r:r[2]); low=min(w["full"],key=lambda r:r[3])
        new.append(dict(id=cid,kind="direction",difficulty=difficulty,week=w,day_start=day_start,day_end=day_end,decision=decision,target=target,
                        hod=hod,lod=lod,how=how,low=low,facts=facts,sig_class=decision_class,sig_answer=decision_answer))
    # Deterministically randomize the ten new direction cases into the original case order.
    rng=random.Random(1010)
    for c in new:
        cases.insert(rng.randrange(0,len(cases)+1),c)
    return cases


def student_case(c):
    if c['kind']=="direction":
        phase_a_task="Mark and report HOD and LOD for the printed target trading day. At the hard right edge decide BUY, SELL, NO TRADE, WAIT, or UNRESOLVED using only visible/stipulated Videos 1–10 facts."
        phase_a_markup="HOD/LOD with exact prices/timestamps; peak or candidate peak; pull-away; consolidation; stop hunt; second-leg M/W; decision candle; BUY/SELL arrow or crossed-out arrow; controlling invalidation."
        phase_a_choices="BUY / SELL / NO TRADE / DNC / WAIT / UNRESOLVED"
    else:
        phase_a_task="Mark and report HOD and LOD for the printed target trading day. Then classify any official V10 signature/safety trade and any separately stipulated V01–V10 named candidate."
        phase_a_markup="HOD/LOD lines with exact prices and timestamps; signature prerequisites in sequence; entry direction or rejection/WAIT/UNRESOLVED label."
        phase_a_choices="VALID CHECKLIST / INVALID / DNC / WAIT / UNRESOLVED / NONE CONFIRMABLE; separately identify 22 or straightaway only when stipulated."
    return f"""## {c['id']} — {c['difficulty'].title()}

| Field | Student-facing requirement |
|---|---|
| Videos | V01–V10, primarily V03/V05/V10 with V02/V04 where named |
| Instrument/timeframe | GBP/USD M15 |
| Development week | Begins {c['week']['start']:%Y-%m-%d %H:%M} fixed UTC-5 |
| Target trading day | {c['day_start']:%Y-%m-%d %H:%M} through {c['day_end']:%Y-%m-%d %H:%M} fixed UTC-5 |
| Phase-A decision timestamp | {c['day_end']:%Y-%m-%d %H:%M} UTC-5 |
| Phase-A asset | `DEC_{c['id']}` |
| Phase-A task | {phase_a_task} |
| Phase-A required markup | {phase_a_markup} |
| Phase-A choices | {phase_a_choices} |
| Phase-B asset | Instructor reveals `FULL_{c['id']}` only after Phase A is locked. |
| Phase-B task | Mark and report HOW and LOW for the completed week. Preserve Phase A verbatim and state whether the later chart changes the original signature classification. |
| Phase-B required markup | HOW/LOW lines with exact prices and timestamps on a new marked copy. |
| Evidence labels | Label each material claim `EXPLICIT`, `VISUAL`, `IMPLIED`, `INFERRED`, or `UNRESOLVED`. |
| Difficulty | {c['difficulty']} |

Required locks: `PHASE A LOCKED <timestamp>` before reveal and `PHASE B LOCKED <timestamp>` after the completed-week markup. Text-only answers do not satisfy the chart-markup requirement.

"""


def key_case(c):
    decision_label="Phase-A buy/sell decision" if c['kind']=="direction" else "Phase-A signature classification"
    decision_reason=("Mark the decision only after the supplied prerequisites. A BUY must be away/up from a stipulated PFL; a SELL must be away/down from a stipulated PFH. Missing prerequisites require NO TRADE, WAIT, or UNRESOLVED."
                     if c['kind']=="direction" else
                     "Apply only printed stipulations and visible facts in prerequisite order. Raw OHLC cannot supply missing level, stop-hunt, second-leg, M/W, or prospective-peak definitions.")
    return f"""## {c['id']} — {c['difficulty'].title()}

| Field | Instructor key |
|---|---|
| Development week | {c['week']['start']:%Y-%m-%d %H:%M} through {c['week']['closes'][4]:%Y-%m-%d %H:%M} fixed UTC-5 |
| Target trading day | {c['day_start']:%Y-%m-%d %H:%M} through {c['day_end']:%Y-%m-%d %H:%M} |
| HOD | **{c['hod'][2]:.5f} at {c['hod'][0]:%Y-%m-%d %H:%M}** |
| LOD | **{c['lod'][3]:.5f} at {c['lod'][0]:%Y-%m-%d %H:%M}** |
| {decision_label} | **{c['sig_class']}** |
| Decision/signature answer | {c['sig_answer']} |
| Phase-A reasoning | {decision_reason} |
| HOW | **{c['how'][2]:.5f} at {c['how'][0]:%Y-%m-%d %H:%M}** |
| LOW | **{c['low'][3]:.5f} at {c['low'][0]:%Y-%m-%d %H:%M}** |
| Phase-B rule | The completed-week reveal permits retrospective HOW/LOW only. It must not revise the locked signature decision. |
| Source citation | V03_SOURCE_NOTES.md first-eight-hours/HOW-LOW sections; V05_SOURCE_NOTES.md pass discipline; V10_SOURCE_NOTES.md §§6b–6c [00:40:14]–[00:47:12]; V02_SOURCE_NOTES.md §§2a/2e where named. |
| Expected provenance | Extrema `VISUAL`; arithmetic/selection `INFERRED`; signature doctrine `EXPLICIT`; raw-chart certification gaps `UNRESOLVED`. |
| Invalidation | Any missing pull-away, consolidation, away-from-peak direction, visible stop hunt, or second-leg condition blocks a complete signature checklist. DNC blocks countering toward the peak. |
| Ambiguities | Prospective peak lock, level, box, stop-hunt geometry, M/W, and second-leg anatomy remain incomplete; V10 supplies no safety-trade stop. |
| Scoring | HOD/LOD 4; Phase-A signature or buy/sell decision 4; HOW/LOW 4; provenance/uncertainty 2; lookahead/lock integrity 1 = 15. |
| Common errors | Using calendar midnight instead of the printed trading day; using closes instead of wicks; revising Phase A after reveal; calling a familiar shape a safety trade; inventing a stop. |

"""


def build():
    for p in (ROOT,ROOT/"tools",ASSETS,DECISION,DECISION_CSV,REVEALS,REVEAL_CSV): p.mkdir(parents=True,exist_ok=True)
    weeks=collect_weeks(load_rows()); cases=build_cases(weeks); manifest=[]
    for c in cases:
        did=f"DEC_{c['id']}"; fid=f"FULL_{c['id']}"
        dip=DECISION/f"{did}.png"; dcp=DECISION_CSV/f"{did}.csv"; fip=REVEALS/f"{fid}.png"; fcp=REVEAL_CSV/f"{fid}.csv"
        draw_chart(c['id'],c['decision'],c['day_start'],c['day_end'],c['difficulty'],c['facts'],False).save(dip); write_csv(dcp,c['decision'])
        draw_chart(c['id'],c['week']['full'],c['day_start'],c['day_end'],c['difficulty'],c['facts'],True).save(fip); write_csv(fcp,c['week']['full'])
        manifest += [(did,"decision chart",dip,sha256(dip),c['decision'][-1][0]),(did+"_CSV","decision data",dcp,sha256(dcp),c['decision'][-1][0]),
                     (fid,"sealed completed-week chart",fip,sha256(fip),c['week']['full'][-1][0]),(fid+"_CSV","sealed completed-week data",fcp,sha256(fcp),c['week']['full'][-1][0])]
    (ROOT/"STUDENT_TEST_PACKET.md").write_text("# Student Test Packet — Extrema, Signature Trades, and Direction Decisions\n\n**46 two-phase chart cases, including 10 randomly mixed BUY/SELL decision cases. No Video 11. Phase A must be immutable before the completed week is revealed.**\n\nThe official signature trade in scope is V10's safety trade with a second-leg element. V04's four-trade taxonomy and V02's 22/straightaway terms are separate named teachings and must not be silently relabelled as the official signature trade.\n\n"+"".join(student_case(c) for c in cases))
    (ROOT/"INSTRUCTOR_ANSWER_KEY.md").write_text("# Instructor Answer Key — Extrema and Signature Trades\n\nKeep sealed. Administer decision charts first; reveal completed weeks only after Phase A is locked.\n\n"+"".join(key_case(c) for c in cases))
    idx=["# Asset Index\n\nStudents may open only the Phase-A asset assigned to the current case. `instructor_only/` remains forbidden until that case is locked.\n\n| Case | Difficulty | Phase-A chart | Phase-A CSV | Phase-B reveal (instructor only) |\n|---|---|---|---|---|\n"]
    for c in cases: idx.append(f"| {c['id']} | {c['difficulty']} | [DEC_{c['id']}](decision_charts/DEC_{c['id']}.png) | [CSV](decision_csv/DEC_{c['id']}.csv) | `FULL_{c['id']}` |\n")
    (ASSETS/"ASSET_INDEX.md").write_text("".join(idx))
    prov=["# Data and Asset Provenance\n\nAll charts use unused weeks from the repository's HistData GBP/USD M15 Arm A development corpus, fixed UTC-5. No reserved holdout data is present or used. Phase-A files end exactly at the target trading-day close. Phase-B files show the completed week solely for retrospective HOW/LOW.\n\n| ID | Type | Relative path | SHA-256 | Last timestamp |\n|---|---|---|---|---|\n"]
    for aid,typ,path,digest,last in manifest: prov.append(f"| {aid} | {typ} | `{path.relative_to(ROOT)}` | `{digest}` | {last:%Y-%m-%d %H:%M} UTC-5 |\n")
    (ASSETS/"DATA_PROVENANCE.md").write_text("".join(prov))
    coverage=["# Coverage Matrix\n\n| Case | Type | Difficulty | HOD/LOD | HOW/LOW | Decision/signature status | Primary videos |\n|---|---|---|---|---|---|---|\n"]
    for c in cases: coverage.append(f"| {c['id']} | {c['kind']} | {c['difficulty']} | Phase A | Phase B | {c['sig_class']} | V03,V05,V10; V02/V04 where named |\n")
    (ROOT/"COVERAGE_MATRIX.md").write_text("".join(coverage))
    results=["# Results Template\n\nAttempt ID:  \nStudent (AI agent):  \nStart:  \nEnd:  \nPacket hash:  \nAsset-index hash:  \n\n| Case | Phase-A marked chart/hash | HOD | LOD | Signature classification | Phase-A lock | Phase-B marked chart/hash | HOW | LOW | Phase A preserved? | Phase-B lock | Score /15 | Critical code |\n|---|---|---:|---:|---|---|---|---:|---:|---|---|---:|---|\n"]
    for c in cases: results.append(f"| {c['id']} |  |  |  |  |  |  |  |  |  |  |  |  |\n")
    (ROOT/"RESULTS_TEMPLATE.md").write_text("".join(results))
    reveal=["# Instructor Reveal Protocol\n\nFor each case: verify the Phase-A response and marked chart are locked and hashed; then reveal only the matching `FULL_<case>` chart. The student marks HOW/LOW and must preserve the signature answer verbatim.\n\n| Case | Reveal chart | Reveal CSV |\n|---|---|---|\n"]
    for c in cases: reveal.append(f"| {c['id']} | `completed_week_reveals/FULL_{c['id']}.png` | `completed_week_csv/FULL_{c['id']}.csv` |\n")
    (ROOT/"instructor_only"/"REVEAL_PROTOCOL.md").write_text("".join(reveal))
    summary={"cases":46,"points":690,"decision_charts":46,"sealed_completed_week_charts":46,"difficulty":dict(Counter(c['difficulty'] for c in cases)),"case_type":dict(Counter(c['kind'] for c in cases)),"decision_status":dict(Counter(c['sig_class'] for c in cases)),"prior_weeks_excluded":len(prior_week_starts()),"direction_case_order":[c['id'] for c in cases if c['kind']=="direction"]}
    (ROOT/"VALIDATION_SUMMARY.json").write_text(json.dumps(summary,indent=2)+"\n")


if __name__=="__main__": build()
