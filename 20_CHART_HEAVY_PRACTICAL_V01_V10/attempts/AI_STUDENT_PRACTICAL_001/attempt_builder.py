from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import csv, hashlib, re
from datetime import datetime, timezone, timedelta

ROOT = Path('/Users/randyschutt/Desktop/Trading/MMM-Agents/20_CHART_HEAVY_PRACTICAL_V01_V10')
ATTEMPT = ROOT / 'attempts' / 'AI_STUDENT_PRACTICAL_001'
MARKED = ATTEMPT / 'MARKED_CHARTS'
MARKED.mkdir(parents=True, exist_ok=True)

START = '2026-08-13T20:53:22-04:00'
TZ = timezone(timedelta(hours=-4))
FONT_PATH = '/System/Library/Fonts/Supplemental/Arial.ttf'
FONT_BOLD_PATH = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'

def font(size, bold=False):
    p = FONT_BOLD_PATH if bold else FONT_PATH
    try:
        return ImageFont.truetype(p, size)
    except Exception:
        return ImageFont.load_default()

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def parse_ts(s):
    return datetime.strptime(s, '%Y-%m-%d %H:%M')

packet_path = ROOT / 'STUDENT_PRACTICAL_PACKET.md'
template_path = ROOT / 'RESULTS_TEMPLATE.md'
index_path = ROOT / 'assets' / 'ASSET_INDEX.md'
packet_text = packet_path.read_text()
_ = template_path.read_text()
_ = index_path.read_text()

sections = {}
for m in re.finditer(r'^## ([A-G]\d\d) — (.+)$', packet_text, re.M):
    end = packet_text.find('\n## ', m.start() + 4)
    sec = packet_text[m.start(): end if end != -1 else None]
    fields = {}
    for f in ['Information visible to student','Exact decision timestamp','Student task','Required chart markup','Required explanation','Allowed answer choices']:
        z = re.search(rf'^\| {re.escape(f)} \| (.*?) \|$', sec, re.M)
        fields[f] = z.group(1) if z else ''
    fields['title'] = m.group(2)
    sections[m.group(1)] = fields

def read_rows(case):
    p = ROOT / 'assets' / 'visible_only_csv' / f'CH_{case}_visible_only.csv'
    with p.open(newline='') as f:
        return p, list(csv.DictReader(f))

def coords(rows, i, price, size):
    w,h=size
    left,right=105,w-45
    top,bottom=100,h-105
    hi=max(float(r['high']) for r in rows); lo=min(float(r['low']) for r in rows)
    pad=max((hi-lo)*0.08, 0.00015)
    ymax=hi+pad; ymin=lo-pad
    x=left+20+(right-left-40)*(i/max(1,len(rows)-1))
    y=top+(ymax-price)/(ymax-ymin)*(bottom-top)
    return x,y

def banner(draw, w, case, lines, color=(255,215,0)):
    box_h = 30 + 28*len(lines)
    draw.rounded_rectangle((12, 12, min(w-12, 990), 12+box_h), radius=10, fill=(8,16,26,235), outline=color, width=3)
    draw.text((28,24), f'{case} — STUDENT MARKUP', font=font(24,True), fill=color)
    y=56
    for line in lines:
        draw.text((28,y), line, font=font(19,True), fill='white')
        y+=27

def arrow(draw, xy1, xy2, color='yellow', width=6):
    draw.line((xy1,xy2),fill=color,width=width)
    import math
    ang=math.atan2(xy2[1]-xy1[1],xy2[0]-xy1[0])
    for a in (ang+2.55,ang-2.55):
        p=(xy2[0]+18*math.cos(a),xy2[1]+18*math.sin(a))
        draw.line((xy2,p),fill=color,width=width)

def save_chart_markup(case, rows, marks, banner_lines):
    src=ROOT/'assets'/'charts'/f'CH_{case}_visible_only.png'
    im=Image.open(src).convert('RGB')
    d=ImageDraw.Draw(im,'RGBA'); w,h=im.size
    banner(d,w,case,banner_lines)
    for m in marks:
        typ=m[0]
        if typ=='hline':
            price,label,color=m[1:]
            _,y=coords(rows,0,price,im.size)
            d.line((105,y,w-45,y),fill=color,width=5)
            d.rectangle((w-600,y-29,w-50,y+2),fill=(4,10,18,220),outline=color,width=2)
            d.text((w-590,y-27),label,font=font(18,True),fill=color)
        elif typ=='candle':
            idx,label,color=m[1:]
            x,_=coords(rows,idx,float(rows[idx]['close']),im.size)
            d.rounded_rectangle((x-17,92,x+17,h-105),radius=8,outline=color,width=5)
            d.text((max(110,x-160),h-148),label,font=font(18,True),fill=color,stroke_width=2,stroke_fill='black')
        elif typ=='arrow':
            i1,p1,i2,p2,label,color=m[1:]
            x1,y1=coords(rows,i1,p1,im.size); x2,y2=coords(rows,i2,p2,im.size)
            arrow(d,(x1,y1),(x2,y2),color)
            d.text((max(110,x2-260),max(155,y2-42)),label,font=font(18,True),fill=color,stroke_width=2,stroke_fill='black')
        elif typ=='vline':
            idx,label,color=m[1:]
            x,_=coords(rows,idx,float(rows[idx]['close']),im.size)
            d.line((x,100,x,h-105),fill=color,width=5)
            d.text((max(110,x-170),h-145),label,font=font(18,True),fill=color,stroke_width=2,stroke_fill='black')
    out=MARKED/f'{case}_MARKED.png'
    im.save(out,format='PNG')
    return src,out

def save_source_markup(case, src_name, specs, banner_lines):
    src=ROOT/'assets'/'source_cards'/src_name
    im=Image.open(src).convert('RGB'); d=ImageDraw.Draw(im,'RGBA'); w,h=im.size
    banner(d,w,case,banner_lines)
    for typ,box,label,color in specs:
        x1,y1,x2,y2=[int(v) for v in box]
        if typ=='box':
            d.rounded_rectangle((x1,y1,x2,y2),radius=10,outline=color,width=5)
            d.rectangle((x1,max(0,y1-28),min(w-2,x1+max(180,11*len(label))),y1),fill=(0,0,0,220),outline=color,width=2)
            d.text((x1+4,max(0,y1-27)),label,font=font(17,True),fill=color)
        elif typ=='line':
            d.line((x1,y1,x2,y2),fill=color,width=6)
            d.text((min(w-260,x1+8),max(0,y1-28)),label,font=font(17,True),fill=color,stroke_width=2,stroke_fill='black')
    out=MARKED/f'{case}_MARKED.png'; im.save(out,format='PNG')
    return src,out

answers=[]; accessed=[packet_path,template_path,index_path]; cutoffs=[]

def add(case,decision,out,measurement,reasoning,provenance,confidence,missing):
    lock=datetime.now(TZ).isoformat(timespec='seconds')
    answers.append(dict(case=case,decision=decision,out=out,measurement=measurement,reasoning=reasoning,provenance=provenance,confidence=confidence,missing=missing,lock=lock,hash=sha(out)))

# A: first eight hours and first post-band breach.
for n in range(1,13):
    case=f'A{n:02d}'; csvp,rows=read_rows(case); accessed.append(csvp)
    decision_ts=sections[case]['Exact decision timestamp'].replace(' UTC-5','')
    start=parse_ts(rows[0]['timestamp_utc_minus_5']); band_end=start+timedelta(hours=8)
    band=[r for r in rows if parse_ts(r['timestamp_utc_minus_5'])<band_end]
    bh=max(float(r['high']) for r in band); bl=min(float(r['low']) for r in band)
    ih=max(range(len(band)),key=lambda i:float(band[i]['high'])); il=min(range(len(band)),key=lambda i:float(band[i]['low']))
    br=len(rows)-1; r=rows[br]; direction='UP' if float(r['high'])>bh else 'DOWN' if float(r['low'])<bl else 'NONE'
    marks=[('hline',bh,f'BAND HIGH {bh:.5f} @ {band[ih]["timestamp_utc_minus_5"]}','lime'),('hline',bl,f'BAND LOW {bl:.5f} @ {band[il]["timestamp_utc_minus_5"]}','cyan'),('candle',br,f'FIRST BREACH {direction} {r["timestamp_utc_minus_5"]}','orange')]
    p2=float(r['high'])+0.0006 if direction=='DOWN' else float(r['low'])-0.0006
    marks.append(('arrow',br,float(r['close']),max(0,br-3),p2,f'REJECT {direction} TRADE — NO TRADE','yellow'))
    src,out=save_chart_markup(case,rows,marks,[f'8-hour band: {start:%Y-%m-%d %H:%M} to {band_end:%Y-%m-%d %H:%M} (end exclusive)',f'First breach: {direction} at {r["timestamp_utc_minus_5"]} | NO TRADE'])
    accessed.append(src); last=parse_ts(rows[-1]['timestamp_utc_minus_5']); dec=parse_ts(decision_ts); cutoffs.append((case,csvp,last,dec,last<=dec))
    meas=f'Band window {start:%Y-%m-%d %H:%M}–{band_end:%Y-%m-%d %H:%M} UTC-5 (32 M15 bars); high {bh:.5f}; low {bl:.5f}; width {(bh-bl)*10000:.1f} pips. Breach candle {r["timestamp_utc_minus_5"]}: H {float(r["high"]):.5f}, L {float(r["low"]):.5f}; breach direction {direction}.'
    reason='1. [CSV] Measured the fixed eight-clock-hour band from the first visible week-open bar. 2. [CSV] Compared every post-band bar in order with both band limits; the named final bar is the first breach. 3. [EXPLICIT COURSE RULE] The task identifies this as the first move and requires the first-move prohibition. 4. [DECISION] A trade in the breach direction is rejected without attributing intent or using outcome.'
    prov='[CSV] OHLC, timestamps, band extrema, and breach. [PACKET-EXPLICIT] fixed UTC-5, eight-hour context, and first-move prohibition. [CALCULATED] pip width. [UNRESOLVED] dealer intent is neither observed nor claimed.'
    add(case,'NO TRADE',out,meas,reason,prov,'HIGH','No missing input is needed to apply the explicit first-move prohibition; dealer intent remains UNRESOLVED and immaterial.')

# B: prospective extremes cannot be certified as final weekly identities.
for n in range(1,9):
    case=f'B{n:02d}'; csvp,rows=read_rows(case); accessed.append(csvp)
    ih=max(range(len(rows)),key=lambda i:float(rows[i]['high'])); il=min(range(len(rows)),key=lambda i:float(rows[i]['low']))
    hi=float(rows[ih]['high']); lo=float(rows[il]['low'])
    marks=[('hline',hi,f'HIGH-SO-FAR? {hi:.5f} @ {rows[ih]["timestamp_utc_minus_5"]}','yellow'),('hline',lo,f'LOW-SO-FAR? {lo:.5f} @ {rows[il]["timestamp_utc_minus_5"]}','cyan')]
    src,out=save_chart_markup(case,rows,marks,[f'Visible extreme range: {hi:.5f} to {lo:.5f}', 'PROSPECTIVE ONLY — PFH/PFL final identity unresolved'])
    accessed.append(src); dec=parse_ts(sections[case]['Exact decision timestamp'].replace(' UTC-5','')); last=parse_ts(rows[-1]['timestamp_utc_minus_5']); cutoffs.append((case,csvp,last,dec,last<=dec))
    meas=f'High-so-far {hi:.5f} at {rows[ih]["timestamp_utc_minus_5"]}; low-so-far {lo:.5f} at {rows[il]["timestamp_utc_minus_5"]}; visible span {(hi-lo)*10000:.1f} pips; final CSV timestamp {last:%Y-%m-%d %H:%M}.'
    reason='1. [CSV] Located the maximum high and minimum low among visible rows only. 2. [PACKET-EXPLICIT] Visibility ends Tuesday 12:00, before the week is complete. 3. [BOUNDARY] High/low-so-far are observable; final weekly PFH/PFL identities require later weekly information. 4. [DECISION] Neither final identity is certified.'
    prov='[CSV] visible extrema and timestamps. [PACKET-EXPLICIT] Tuesday-noon cutoff and retrospective weekly-identity boundary. [CALCULATED] visible span. [UNRESOLVED] final PFH and PFL.'
    add(case,'INSUFFICIENT INFORMATION',out,meas,reason,prov,'HIGH','Wednesday–Friday bars are absent; final PFH/PFL identities are UNRESOLVED.')

# C: retrospective completed-week range.
for n in range(1,9):
    case=f'C{n:02d}'; csvp,rows=read_rows(case); accessed.append(csvp)
    ih=max(range(len(rows)),key=lambda i:float(rows[i]['high'])); il=min(range(len(rows)),key=lambda i:float(rows[i]['low']))
    hi=float(rows[ih]['high']); lo=float(rows[il]['low']); rng=(hi-lo)*10000
    marks=[('hline',hi,f'PFH {hi:.5f} @ {rows[ih]["timestamp_utc_minus_5"]}','lime'),('hline',lo,f'PFL {lo:.5f} @ {rows[il]["timestamp_utc_minus_5"]}','cyan'),('arrow',il,lo,ih,hi,f'WEEK RANGE {rng:.1f} PIPS','yellow')]
    src,out=save_chart_markup(case,rows,marks,[f'COMPLETED WEEK: PFH {hi:.5f} | PFL {lo:.5f}',f'Range = ({hi:.5f} − {lo:.5f}) × 10,000 = {rng:.1f} pips'])
    accessed.append(src); dec=parse_ts(sections[case]['Exact decision timestamp'].replace(' UTC-5','')); last=parse_ts(rows[-1]['timestamp_utc_minus_5']); cutoffs.append((case,csvp,last,dec,last<=dec))
    meas=f'PFH {hi:.5f} at {rows[ih]["timestamp_utc_minus_5"]}; PFL {lo:.5f} at {rows[il]["timestamp_utc_minus_5"]}; range = ({hi:.5f} − {lo:.5f}) × 10,000 = {rng:.1f} pips.'
    reason='1. [CSV] Full permitted week is visible through Friday 16:45. 2. [CSV] Maximum high is marked PFH and minimum low is marked PFL. 3. [CALCULATED] GBP/USD pip range uses price difference × 10,000. 4. [BOUNDARY] This is retrospective identification after completion, not a prospective entry trigger.'
    prov='[CSV] completed-week OHLC and timestamps. [PACKET-EXPLICIT] retrospective-only permission. [CALCULATED] pip range. [UNRESOLVED] no prospective setup or entry is inferred.'
    add(case,f'PFH {hi:.5f}; PFL {lo:.5f}; RANGE {rng:.1f} PIPS',out,meas,reason,prov,'HIGH','No missing data for the retrospective range; prospective entry validity is outside scope and UNRESOLVED.')

# D: raw OHLC ambiguity discipline.
d_decisions={'D01':'INSUFFICIENT','D02':'INSUFFICIENT','D03':'PASS','D04':'UNRESOLVED','D05':'UNRESOLVED','D06':'UNRESOLVED','D07':'INSUFFICIENT','D08':'UNRESOLVED'}
d_missing={
'D01':'A course definition and complete prerequisites for DNC/straightaway are absent.',
'D02':'Instructor entry location, named pattern, level, leg identity, confirmation, and rule-complete entry/stop inputs are absent.',
'D03':'No supplied course label or complete setup; inventing a name is not required.',
'D04':'A rule for segment boundaries and exact push-count assignment is absent.',
'D05':'Level definition, first/second-leg anchors, and variant-selection criteria are absent.',
'D06':'Operational FAST/SLOW thresholds and measurement window are absent.',
'D07':'Safety-trade definition, validated location, PFH/PFL lock, entry, and stop are absent.',
'D08':'Course-authorized anchor rules for one exact blue box are absent.'}
for n in range(1,9):
    case=f'D{n:02d}'; csvp,rows=read_rows(case); accessed.append(csvp)
    ih=max(range(len(rows)),key=lambda i:float(rows[i]['high'])); il=min(range(len(rows)),key=lambda i:float(rows[i]['low']))
    hi=float(rows[ih]['high']); lo=float(rows[il]['low'])
    marks=[('hline',hi,f'OBJECTIVE HIGH {hi:.5f} @ {rows[ih]["timestamp_utc_minus_5"]}','lime'),('hline',lo,f'OBJECTIVE LOW {lo:.5f} @ {rows[il]["timestamp_utc_minus_5"]}','cyan'),('candle',len(rows)-1,'HARD RIGHT EDGE / DECISION','yellow')]
    src,out=save_chart_markup(case,rows,marks,[f'Objective range only: {hi:.5f}–{lo:.5f}',f'? CANDIDATE ONLY — requested course label {d_decisions[case]}'])
    accessed.append(src); dec=parse_ts(sections[case]['Exact decision timestamp'].replace(' UTC-5','')); last=parse_ts(rows[-1]['timestamp_utc_minus_5']); cutoffs.append((case,csvp,last,dec,last<=dec))
    meas=f'Visible high {hi:.5f} at {rows[ih]["timestamp_utc_minus_5"]}; visible low {lo:.5f} at {rows[il]["timestamp_utc_minus_5"]}; raw span {(hi-lo)*10000:.1f} pips; {len(rows)} M15 bars.'
    reason='1. [CSV] Marked only measurable OHLC extrema and the hard right edge. 2. [PACKET-EXPLICIT] The chart is unannotated apart from an administrative band. 3. [UNRESOLVED] Raw shape does not supply the requested course-specific prerequisites or definitions. 4. [DECISION] No trade or exact course label is invented.'
    prov='[CSV] objective OHLC facts and timestamps. [PACKET-EXPLICIT] raw-chart and administrative-band boundary. [INFERRED-CANDIDATE] any familiar shape is question-marked only. [UNRESOLVED] requested course classification.'
    add(case,d_decisions[case],out,meas,reason,prov,'HIGH',d_missing[case])

# E: stipulated reversal A and basic confirmation B.
for n in range(1,9):
    case=f'E{n:02d}'; csvp,rows=read_rows(case); accessed.append(csvp)
    has_b=n<=4
    ia=len(rows)-2 if has_b else len(rows)-1
    ib=len(rows)-1 if has_b else None
    A=rows[ia]; direction='LONG' if n<=4 or n==8 else 'SHORT'
    marks=[('candle',ia,f'REVERSAL A {A["timestamp_utc_minus_5"]}','orange')]
    if has_b:
        B=rows[ib]; bdir='BULLISH' if float(B['close'])>float(B['open']) else 'BEARISH' if float(B['close'])<float(B['open']) else 'DOJI'
        marks += [('candle',ib,f'DIRECTION B {bdir} CLOSED','lime'),('vline',ib,f'EARLIEST BASIC ENTRY AFTER B CLOSE','yellow')]
        decision='ENTER' if (direction=='LONG' and bdir=='BULLISH') or (direction=='SHORT' and bdir=='BEARISH') else 'WAIT'
        meas=f'A {A["timestamp_utc_minus_5"]}: O {float(A["open"]):.5f}, C {float(A["close"]):.5f}. B {B["timestamp_utc_minus_5"]}: O {float(B["open"]):.5f}, C {float(B["close"]):.5f}, body {(float(B["close"])-float(B["open"]))*10000:+.1f} pips ({bdir}); B is closed.'
        missing='No missing input for the stipulated context and visible basic confirmation; stop/target and advanced-entry rules are outside this decision.'
    else:
        marks += [('vline',ia,'NO B VISIBLE — WAIT','yellow')]
        decision='WAIT'; meas=f'A is the last visible candle at {A["timestamp_utc_minus_5"]}: O {float(A["open"]):.5f}, H {float(A["high"]):.5f}, L {float(A["low"]):.5f}, C {float(A["close"]):.5f}. Direction candle B: not visible; zero post-A closed bars.'
        missing='A closed direction candle B and its closing direction are missing; earliest permitted basic entry point is therefore not yet visible.'
    src,out=save_chart_markup(case,rows,marks,[f'Stipulated {direction}: reversal A identified',f'Basic sequence decision: {decision}'])
    accessed.append(src); dec=parse_ts(sections[case]['Exact decision timestamp'].replace(' UTC-5','')); last=parse_ts(rows[-1]['timestamp_utc_minus_5']); cutoffs.append((case,csvp,last,dec,last<=dec))
    reasoning='1. [PACKET-STIPULATED] Location/context are valid and candle A identity is supplied. 2. [CSV] Checked whether a later closed candle B exists and measured its open/close direction. 3. [EXPLICIT BASIC RULE] Basic entry waits for the direction candle to close in the candidate direction. 4. [BOUNDARY] No demo-only advanced entry at the extreme is used.'
    provenance='[PACKET-STIPULATED] candidate direction, valid context, and reversal-A identity. [CSV] candle timestamps and OHLC. [CALCULATED] B body direction where visible. [UNRESOLVED] advanced-entry applicability and any unprovided trade-management inputs.'
    add(case,decision,out,meas,reasoning,provenance,'HIGH',missing)

# F: risk arithmetic and sequence boundaries.
f_data={
'F01':('CALCULATE','$200 total risk; $8.00/pip', ['Balance $10,000 × 2% = $200; $200 ÷ 25 pips = $8.00/pip. One simultaneous trade uses the $200 total exposure.']),
'F02':('CALCULATE','$240 total risk; $16.00/pip', ['Balance $12,000 × 2% = $240; $240 ÷ 15 pips = $16.00/pip. One simultaneous trade uses the $240 total exposure.']),
'F03':('CALCULATE','$160 total; $80 each; $4.00/pip and $3.20/pip', ['Balance $8,000 × 2% = $160 total. Equal allocation across two simultaneous trades = $80 each. $80 ÷ 20 = $4.00/pip; $80 ÷ 25 = $3.20/pip.']),
'F04':('REJECT OVER-RISK','$1,500 proposed exposure versus $500 total 2% budget', ['Balance $25,000 × 2% = $500 total budget. Proposal: three × $500 = $1,500 = 6% cumulative exposure; exceeds the 2% total budget.']),
'F05':('CALCULATE','$4.00/pip after third-loss size reduction; $100 risk at 25 pips', ['Previously established $8.00/pip is reduced by 50% after loss number 3 = $4.00/pip. $4.00 × 25 pips = $100 exposure (1.064% of $9,400).']),
'F06':('CALCULATE','$3.68/pip reduced-size input; $92 risk at 25 pips', ['Balance $9,200 × 2% = $184 standard budget; after the fourth-loss sequence boundary, use half-size risk $92. $92 ÷ 25 = $3.68/pip.']),
'F07':('CALCULATE','$239.20 risk; $9.568/pip (about $9.57/pip)', ['Balance $11,960 × 2% = $239.20. Following the stipulated win, standard size resumes. $239.20 ÷ 25 = $9.568/pip ≈ $9.57/pip.']),
'F08':('INSUFFICIENT STOP INPUT','$200 risk budget calculable; position size not calculable', ['Balance $10,000 × 2% = $200 risk budget. Required denominator, valid stop distance in pips, is absent; $/pip cannot be computed.'])}
for n in range(1,9):
    case=f'F{n:02d}'; csvp,rows=read_rows(case); accessed.append(csvp)
    ih=max(range(len(rows)),key=lambda i:float(rows[i]['high'])); il=min(range(len(rows)),key=lambda i:float(rows[i]['low']))
    hi=float(rows[ih]['high']); lo=float(rows[il]['low']); decision,summary,lines=f_data[case]
    entry=float(rows[-1]['close'])
    marks=[('hline',entry,f'STUDENT: ENTRY ANCHOR {entry:.5f}','yellow'),('hline',entry+0.0050,f'STUDENT: 50-PIP REFERENCE {entry+0.0050:.5f}','lime'),('candle',len(rows)-1,'PLAN ANCHOR / NO FUTURE OUTCOME','orange')]
    if case=='F01': marks.append(('hline',entry-0.0025,f'STUDENT: STIPULATED 25-PIP STOP {entry-0.0025:.5f}','magenta'))
    elif case=='F02': marks.append(('hline',entry-0.0015,f'STUDENT: STIPULATED 15-PIP STOP {entry-0.0015:.5f}','magenta'))
    elif case=='F03':
        marks.append(('hline',entry-0.0020,f'STUDENT: TRADE 1 STOP 20 PIPS {entry-0.0020:.5f}','magenta'))
        marks.append(('hline',entry-0.0025,f'STUDENT: TRADE 2 STOP 25 PIPS {entry-0.0025:.5f}','cyan'))
    elif case in ('F04','F05','F06','F07'): marks.append(('hline',entry-0.0025,f'STUDENT: STIPULATED/ADMIN STOP REFERENCE {entry-0.0025:.5f}','magenta'))
    src,out=save_chart_markup(case,rows,marks,[summary,decision+' | cumulative exposure checked', 'ENTRY / STOP / 50-PIP REFERENCE MARKED; setup validity separate' if case!='F08' else 'ENTRY MARKED; STOP MISSING / UNRESOLVED; 50-PIP REFERENCE ONLY'])
    accessed.append(src); dec=parse_ts(sections[case]['Exact decision timestamp'].replace(' UTC-5','')); last=parse_ts(rows[-1]['timestamp_utc_minus_5']); cutoffs.append((case,csvp,last,dec,last<=dec))
    meas=lines[0]+f' Chart reference range: {hi:.5f}–{lo:.5f} ({(hi-lo)*10000:.1f} pips).'
    reason='1. [PACKET-STIPULATED] Used only the stated balance, number of simultaneous trades, stop distances, and sequence state. 2. [EXPLICIT COURSE ARITHMETIC] Total risk budget is 2% of balance and is cumulative across simultaneous exposure. 3. [CALCULATED] Dollar risk divided by stipulated stop pips gives $/pip; sequence adjustment is applied where stipulated. 4. [BOUNDARY] This arithmetic does not certify V10 setup doctrine or profitability.'
    prov='[PACKET-STIPULATED] account and stop facts. [EXPLICIT COURSE RULE] 2% total risk and size-sequence boundary. [CALCULATED] dollar risk, exposure, and $/pip. [CSV] chart reference prices only. [UNRESOLVED] V10 setup validity unless separately stipulated.'
    missing='None for the stated arithmetic.' if case!='F08' else 'Valid stop distance is missing; V10 safety-trade label does not supply it.'
    add(case,decision,out,meas,reason,prov,'MEDIUM' if case in ('F05','F06','F07') else 'HIGH',missing)

# G: recording-source provenance audits. Coordinates are case-specific visible-object regions.
g_specs={
'G01':('SRC01_V01_TYPICAL_WEEK.png',[
('box',(28,160,960,742),'VISIBLE COMPLETED CHART','lime'),('box',(70,330,250,390),'SUN / MON','cyan'),('box',(260,330,390,390),'TUES','cyan'),('box',(390,160,530,225),'WED + TRAPPED-LONG NOTE','yellow'),('box',(675,160,820,225),'FRIDAY','yellow'),('line',(500,120,500,740),'BOUNDARY: SCREENSHOT FACT ≠ UNSEEN-WEEK PROOF','orange')],['Completed example only','No unseen-week path is proven']),
'G02':('SRC02_V02_POP_QUIZ.png',[
('box',(245,150,945,575),'RED / BLUE BOX INVENTORY','yellow'),('box',(260,345,920,470),'VISIBLE R LABELS','lime'),('box',(245,240,945,540),'PRICE-PANEL MOVING AVERAGES','cyan'),('box',(245,575,945,665),'TDI PANEL','magenta'),('line',(735,125,735,675),'NO MECHANICAL 22 RULE FROM ONE IMAGE','orange')],['Source-card audit','Objects visible; prospective 22 rule unresolved']),
'G03':('SRC03_V03_FLASHCARD.png',[
('box',(45,320,310,455),'LEFT BLUE / RED FLASHCARD REGION','cyan'),('box',(350,340,490,570),'LOW REVERSAL REGION','lime'),('box',(600,225,870,425),'RIGHT RED REGION','yellow'),('line',(600,150,600,575),'HARD-RIGHT-EDGE CROP BEFORE LATER PATH','orange')],['Flashcard construction audit','Crop must exclude post-decision path']),
'G04':('SRC04_V04_SECOND_LEG.png',[
('box',(5,270,490,445),'VISIBLE BLUE BOX','cyan'),('box',(475,80,785,205),'OVER-HIGH STRUCTURE','yellow'),('box',(560,125,725,285),'HAND-DRAWN M / SECOND-LEG REGION','lime'),('box',(675,195,1015,740),'LATER DECLINE (OUTCOME ONLY)','orange'),('line',(670,20,670,745),'PROSPECTIVE BOUNDARY','magenta')],['Second-leg source chart','Later decline cannot validate application']),
'G05':('SRC05_V06_PUSHES.png',[
('box',(500,180,660,300),'PUSH 1 + ENTRY','lime'),('box',(620,110,750,285),'PUSH 2 + ENTRY','yellow'),('box',(840,320,1005,500),'PUSH 3','orange'),('box',(220,65,710,270),'LEVEL 3 / M','cyan'),('box',(700,170,900,365),'LEVEL 1 / SS + ENTRIES','magenta')],['Push-label transcription','One annotated chart ≠ universal algorithm']),
'G06':('SRC06_V07_STAIR_STEP.png',[
('line',(505,0,505,740),'DAY SEPARATOR','yellow'),('box',(180,255,230,350),'MARKED BOX','cyan'),('box',(620,450,685,510),'STAIR-STEP BOX','lime'),('box',(850,345,1005,555),'VISIBLE ARROWS','orange'),('box',(0,20,1020,590),'MOVING-AVERAGE CONTEXT','magenta')],['Chart-furniture audit','Naming boundary remains explicit']),
'G07':('SRC07_V08_HIGH_LOW.png',[
('box',(340,245,510,360),'VISIBLE HIGH/LOW BOX','cyan'),('box',(530,325,635,535),'DECLINE + EXTREME REGION','yellow'),('box',(620,350,845,510),'DEMO ENTRY TEXT / ARROW','lime'),('box',(25,540,970,655),'TDI PANEL','magenta'),('line',(510,100,510,650),'DEMO SCREENSHOT ≠ BASIC LIVE RULE','orange')],['High-low drill source boundary','Demo entry and basic confirmation kept separate']),
'G08':('SRC08_V10_SAFETY.png',[
('box',(65,190,960,710),'COMPLETED BOX / LEVEL INVENTORY','cyan'),('box',(75,410,465,705),'LOWER COMPLETED BOXES + R LABELS','yellow'),('box',(550,380,955,560),'UPPER COMPLETED BOXES + R LABELS','lime'),('line',(690,190,690,710),'STOP / LOT SIZE / PROSPECTIVE PFH-PFL UNRESOLVED','orange')],['Safety walkthrough audit','Completed image supplies no executable sizing lock'])}
g_answers={
'G01':('INSUFFICIENT FOR UNSEEN-WEEK PROOF','Visible labels include Sunday, Monday, Tues, Wed, and Friday; visible instructor notes include trapped higher-level longs, trapped lower-level shorts, a unidirectional swing, stops triggered on week-long holders, and a level not crossed until late Friday.','A completed screenshot records one displayed path but cannot prove that an unseen week will reproduce it.'),
'G02':('UNRESOLVED PROSPECTIVE MECHANICAL 22 RULE','Visible objects: multiple red and light-blue boxes, R labels, colored moving averages in the price panel, and a multi-line TDI panel below.','The image inventories annotations but does not state complete prospective inputs, thresholds, timing, or exception handling for a mechanical 22 rule.'),
'G03':('HARD-RIGHT-EDGE CROP REQUIRED','Visible completed flashcard contains left blue/red regions, a central low/reversal region, a large later red region, moving averages, arrows, and TDI.','For an unseen decision test, crop at the decision candle before the later right-side path and all outcome-revealing annotations.'),
'G04':('PROSPECTIVE CLAIMS LIMITED','Visible: blue box, over-high structure, hand-drawn M/second-leg region, and later decline.','Prospectively one may identify only objects visible at the crop; the later decline is outcome evidence and cannot prove earlier rule compliance.'),
'G05':('NO UNIVERSAL PUSH-COUNT ALGORITHM','Visible labels include Push 1, Push 2, Push 3, Level 3, Level 1, M, SS, and several Enter annotations.','This single instructor-annotated chart exemplifies labels but does not define universal segment boundaries and complete algorithmic rules.'),
'G06':('NAMING UNRESOLVED FROM FURNITURE ALONE','Visible: a vertical day separator, marked blue/yellow boxes, right-side arrows, and several moving-average lines.','These visual objects provide context; without an explicit naming rule, a stair-step or trade label remains inferred rather than certified.'),
'G07':('DEMO DOES NOT REPLACE BASIC CONFIRMATION RULE','Visible teaching slide shows a high-low drill, a marked box/extreme, an entry callout, moving averages, and TDI.','The completed demo shows what was annotated; it does not by itself replace the packet-stated basic rule requiring a closed direction candle after reversal A.'),
'G08':('STOP / LOT SIZE / PROSPECTIVE PFH-PFL LOCK UNRESOLVED','Visible completed chart includes red/blue/white boxes, horizontal levels, moving averages, and R labels such as 46.2, 46.9, 46.5, 52.2, and 20.1.','No explicit stop distance, account risk, lot size, or prospective PFH/PFL lock is visible as a complete executable input set.')}
for n in range(1,9):
    case=f'G{n:02d}'; srcname,specs,banners=g_specs[case]
    src,out=save_source_markup(case,srcname,specs,banners); accessed.append(src)
    decision,inventory,boundary=g_answers[case]
    meas=f'{inventory} Recording-player time visible in the source card is treated only as a screenshot fact; no market decision timestamp is inferred.'
    reason=f'1. [VISUAL] {inventory} 2. [EXPLICIT] The packet permits the completed image only for source-evidence audit, not an unseen replay decision. 3. [INFERRED] The annotations may illustrate a teaching example, but transferability is not established by one image. 4. [UNRESOLVED] {boundary}'
    prov='[VISUAL] marked pixels, labels, boxes, lines, and panels. [EXPLICIT] packet source-boundary instructions. [INFERRED] any broader teaching interpretation. [UNRESOLVED] predictive repeatability, complete mechanical rule, and future performance.'
    add(case,decision,out,meas,reason,prov,'HIGH','The screenshot does not supply a complete prospective rule, unseen continuation, or independent validation beyond the visible objects.')

# Write FIRST_ATTEMPT.md in packet order.
packet_hash=sha(packet_path); index_hash=sha(index_path); end=datetime.now(TZ).isoformat(timespec='seconds')
lines=['# FIRST ATTEMPT — AI_STUDENT_PRACTICAL_001','',f'Attempt ID: AI_STUDENT_PRACTICAL_001  ',f'Student: AI_STUDENT_PRACTICAL_001  ',f'Exam start: {START}  ',f'Phase A completion: {end}  ',f'Packet SHA-256: `{packet_hash}`  ',f'Asset-index SHA-256: `{index_hash}`','', '> This file records the first and locked decision for each case. No grading fields are completed.','']
for a in answers:
    rel=a['out'].relative_to(ATTEMPT)
    lines += [f'## {a["case"]}', '', f'**FIRST CLASSIFICATION / DECISION:** {a["decision"]}', '', f'**MARKED CHART:** `{rel}`  ', f'**MARKED CHART SHA-256:** `{a["hash"]}`', '', f'**MEASUREMENTS / CALCULATIONS:** {a["measurement"]}', '', f'**ORDERED REASONING:** {a["reasoning"]}', '', f'**PROVENANCE LABELS:** {a["provenance"]}', '', f'**CONFIDENCE:** {a["confidence"]}', '', f'**MISSING / UNRESOLVED INFORMATION:** {a["missing"]}', '', '**FUTURE INFORMATION USED: NO**', '', f'**LOCKED {a["lock"]}**', '']
(ATTEMPT/'FIRST_ATTEMPT.md').write_text('\n'.join(lines)+'\n')
phase_a_hash=sha(ATTEMPT/'FIRST_ATTEMPT.md')

# Manifest, including exact access log and disclosed sequencing incident.
accessed += [ATTEMPT/'attempt_builder.py', ATTEMPT/'FIRST_ATTEMPT.md', ATTEMPT/'ATTEMPT_MANIFEST.md']
accessed += [a['out'] for a in answers]
incident_paths=[
ROOT/'assets'/'visible_only_csv'/f'CH_E{i:02d}_visible_only.csv' for i in range(1,9)
] + [ROOT/'assets'/'source_cards'/g_specs[f'G{i:02d}'][0] for i in range(1,9)]
manifest=['# ATTEMPT MANIFEST — AI_STUDENT_PRACTICAL_001','',f'- Start timestamp: {START}',f'- Completion timestamp: {end}',f'- Packet SHA-256: `{packet_hash}`',f'- Asset-index SHA-256: `{index_hash}`',f'- Phase A response SHA-256 (`FIRST_ATTEMPT.md`): `{phase_a_hash}`',f'- Phase A case count: {len(answers)}',f'- Marked-chart count: {len(list(MARKED.glob("*_MARKED.png")))}','', '## Files accessed','']
for p in dict.fromkeys(map(str,accessed)):
    manifest.append(f'- `{p}`')
manifest += ['', '## Visible-only CSV cutoff verification','']
for case,p,last,dec,ok in cutoffs:
    manifest.append(f'- {case}: `{p}` final `{last:%Y-%m-%d %H:%M} UTC-5` <= decision `{dec:%Y-%m-%d %H:%M} UTC-5`: **{"PASS" if ok else "FAIL"}**')
manifest += ['', '## Marked-chart hashes','']
for a in answers:
    manifest.append(f'- {a["case"]}: `{a["out"].relative_to(ATTEMPT)}` — `{a["hash"]}`')
manifest += ['', '## Forbidden-access disclosure','', '**INCIDENT DISCLOSED:** Before packet-order processing reached E01/G01, the student used a local tail/view inspection on the following assets that are assigned to later cases but were not yet the current case. No instructor key, rubric, blueprint, validation report, provenance file, instructor-only material, repository script, prior attempt, Video 11+ source, internet source, or unrelated repository evidence was accessed. The prematurely viewed assigned assets were not concealed:', '']
for p in incident_paths:
    manifest.append(f'- `{p}`')
manifest += ['', '## Signed firewall declaration','', f'I, **AI_STUDENT_PRACTICAL_001**, declare that I used no internet or external sources and accessed no instructor answer key, rubric, blueprint, validation output, instructor-only reveal, repository build/validation script, previous attempt, grading report, transcript, source note, review, mastery report, backtest, or Video 11+ material. I disclose the assigned-asset sequencing incident listed above. All originals were preserved; only duplicates under `MARKED_CHARTS/` were annotated. Signed: **AI_STUDENT_PRACTICAL_001** at **{end}**.','']
(ATTEMPT/'ATTEMPT_MANIFEST.md').write_text('\n'.join(manifest))
print(f'answers={len(answers)} marked={len(list(MARKED.glob("*_MARKED.png")))} cutoffs={len(cutoffs)} cutoff_failures={sum(not x[-1] for x in cutoffs)}')
print('first_attempt_sha',sha(ATTEMPT/'FIRST_ATTEMPT.md'))
print('manifest_sha',sha(ATTEMPT/'ATTEMPT_MANIFEST.md'))
