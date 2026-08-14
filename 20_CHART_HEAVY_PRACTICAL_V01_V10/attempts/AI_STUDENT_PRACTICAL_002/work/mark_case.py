#!/usr/bin/env python3
import argparse, csv, hashlib, os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

def sha(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()

def font(size):
    for p in ('/System/Library/Fonts/Supplemental/Arial.ttf','/System/Library/Fonts/SFNS.ttf'):
        try: return ImageFont.truetype(p,size)
        except OSError: pass
    return ImageFont.load_default()

ap=argparse.ArgumentParser()
ap.add_argument('--case',required=True); ap.add_argument('--image',required=True)
ap.add_argument('--csv'); ap.add_argument('--mode',required=True)
ap.add_argument('--classification',required=True); ap.add_argument('--measurements',required=True)
ap.add_argument('--reasoning',required=True); ap.add_argument('--provenance',required=True)
ap.add_argument('--confidence',required=True); ap.add_argument('--missing',required=True)
ap.add_argument('--labels',default=''); ap.add_argument('--decision-ts',default='')
ap.add_argument('--boundary-frac',type=float,default=.72)
a=ap.parse_args()
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out=os.path.join(root,'MARKED_CHARTS',f'{a.case}_marked.png')
rows=[]
if a.csv:
    with open(a.csv,newline='') as f:
        rows=list(csv.DictReader(f))
im=Image.open(a.image).convert('RGBA'); d=ImageDraw.Draw(im,'RGBA')
W,H=im.size; left,right,top,bottom=105,W-45,100,H-105
f18,f24,f30=font(18),font(24),font(30)

if a.measurements == 'AUTO' and rows:
    if a.mode == 'A':
        band=rows[:32]; hi=max(float(r['high']) for r in band); lo=min(float(r['low']) for r in band)
        ih=max(range(32),key=lambda i:float(rows[i]['high'])); il=min(range(32),key=lambda i:float(rows[i]['low']))
        breach=next((r for r in rows[32:] if float(r['high'])>hi or float(r['low'])<lo),rows[-1])
        direction='up' if float(breach['high'])>hi else 'down'
        excess=(float(breach['high'])-hi if direction=='up' else lo-float(breach['low']))*10000
        a.measurements=(f'First 8 clock hours: {rows[0]["timestamp_utc_minus_5"]} through {rows[31]["timestamp_utc_minus_5"]} '
                        f'(32 M15 bars). Band high {hi:.5f} at {rows[ih]["timestamp_utc_minus_5"]}; '
                        f'band low {lo:.5f} at {rows[il]["timestamp_utc_minus_5"]}; range {(hi-lo)*10000:.1f} pips. '
                        f'First breach: {breach["timestamp_utc_minus_5"]}, {direction}, {excess:.1f} pips beyond the band.')
    elif a.mode in ('B','C'):
        hi=max(float(r['high']) for r in rows); lo=min(float(r['low']) for r in rows)
        ih=max(range(len(rows)),key=lambda i:float(rows[i]['high'])); il=min(range(len(rows)),key=lambda i:float(rows[i]['low']))
        prefix='Visible high-so-far/low-so-far' if a.mode=='B' else 'Completed-week PFH/PFL'
        a.measurements=(f'{prefix}: high {hi:.5f} at {rows[ih]["timestamp_utc_minus_5"]}; '
                        f'low {lo:.5f} at {rows[il]["timestamp_utc_minus_5"]}; range {(hi-lo)*10000:.1f} pips '
                        f'({hi:.5f} - {lo:.5f}) × 10,000.')
    elif a.mode == 'D':
        hi=max(float(r['high']) for r in rows); lo=min(float(r['low']) for r in rows)
        ih=max(range(len(rows)),key=lambda i:float(rows[i]['high'])); il=min(range(len(rows)),key=lambda i:float(rows[i]['low']))
        a.measurements=(f'Objective visible range: high {hi:.5f} at {rows[ih]["timestamp_utc_minus_5"]}; '
                        f'low {lo:.5f} at {rows[il]["timestamp_utc_minus_5"]}; span {(hi-lo)*10000:.1f} pips across {len(rows)} M15 bars.')
    elif a.mode == 'E':
        take=rows[-1:] if 'A_ONLY' in a.labels else rows[-2:]
        a.measurements='; '.join(f'{r["timestamp_utc_minus_5"]} O {float(r["open"]):.5f} H {float(r["high"]):.5f} L {float(r["low"]):.5f} C {float(r["close"]):.5f}' for r in take)
    elif a.mode == 'F':
        r=rows[-1]; a.measurements=(f'Chart anchor at {r["timestamp_utc_minus_5"]}: O {float(r["open"]):.5f}, H {float(r["high"]):.5f}, '
                                    f'L {float(r["low"]):.5f}, C {float(r["close"]):.5f}. '+a.labels)

def pmap(v):
    vals=[float(r[k]) for r in rows for k in ('high','low')]
    lo,hi=min(vals),max(vals); pad=(hi-lo)*.12 or .001
    lo-=pad; hi+=pad
    return bottom-(v-lo)/(hi-lo)*(bottom-top)
def xmap(i): return left+(right-left)*(i+.5)/max(1,len(rows))
def hline(price,color,label):
    y=pmap(price); d.line((left,y,right,y),fill=color,width=4)
    d.rectangle((left+8,y-17,left+360,y+17),fill=(5,15,25,220))
    d.text((left+14,y-14),label,font=f18,fill=color)
def vmark(i,color,label):
    x=xmap(i); d.rectangle((x-10,top,x+10,bottom),outline=color,width=4)
    d.text((max(left,x-150),top+42),label,font=f18,fill=color,stroke_width=3,stroke_fill=(5,15,25,255))

if rows and a.mode=='A':
    band=rows[:32]
    hi=max(float(r['high']) for r in band); lo=min(float(r['low']) for r in band)
    hline(hi,(0,220,255,255),f'8H HIGH {hi:.5f}')
    hline(lo,(0,220,255,255),f'8H LOW {lo:.5f}')
    i=len(rows)-1; vmark(i,(255,210,0,255),'FIRST BREACH / REJECTED DIRECTION')
    x=xmap(i); y=pmap(float(rows[i]['low']))
    d.line((x-150,y-80,x,y),fill=(255,80,80,255),width=7)
    d.polygon([(x,y),(x-20,y-6),(x-12,y-24)],fill=(255,80,80,255))
elif rows and a.mode in ('B','C'):
    hi=max(float(r['high']) for r in rows); lo=min(float(r['low']) for r in rows)
    ih=max(range(len(rows)),key=lambda i:float(rows[i]['high']))
    il=min(range(len(rows)),key=lambda i:float(rows[i]['low']))
    q='?' if a.mode=='B' else ''
    hline(hi,(255,90,90,255),f'{q} HIGH {hi:.5f} @ {rows[ih]["timestamp_utc_minus_5"]}')
    hline(lo,(70,220,255,255),f'{q} LOW {lo:.5f} @ {rows[il]["timestamp_utc_minus_5"]}')
    d.line((right-50,pmap(hi),right-50,pmap(lo)),fill=(255,210,0,255),width=5)
elif rows and a.mode=='D':
    hi=max(float(r['high']) for r in rows); lo=min(float(r['low']) for r in rows)
    hline(hi,(255,120,120,255),f'OBJECTIVE HIGH {hi:.5f} (?)')
    hline(lo,(80,210,255,255),f'OBJECTIVE LOW {lo:.5f} (?)')
    vmark(len(rows)-1,(255,210,0,255),'HARD RIGHT EDGE — NO LATER BARS')
elif rows and a.mode=='E':
    n=len(rows); vmark(n-1,(255,210,0,255),'DECISION CANDLE / HARD RIGHT EDGE')
    if 'A_ONLY' in a.labels:
        d.text((right-420,top+100),'REVERSAL CANDLE A\nNO CANDLE B VISIBLE',font=f24,fill=(255,210,0,255),stroke_width=3,stroke_fill=(5,15,25,255))
    else:
        vmark(n-2,(0,220,255,255),'REVERSAL CANDLE A')
        d.text((right-420,top+100),'CLOSED CANDLE B\nEARLIEST BASIC ENTRY: AFTER B CLOSE',font=f24,fill=(255,210,0,255),stroke_width=3,stroke_fill=(5,15,25,255))
elif rows and a.mode=='F':
    vmark(len(rows)-1,(255,210,0,255),'PLAN ANCHOR / NO OUTCOME USED')
elif a.mode=='G':
    bx=int(W*a.boundary_frac)
    d.line((bx,70,bx,H-140),fill=(255,70,70,255),width=7)
    d.rectangle((80,72,W-80,118),fill=(3,12,22,230),outline=(255,210,0,255),width=3)
    d.text((96,80),'COMPLETED SCREENSHOT FACT  |  HARD BOUNDARY  |  NO UNSEEN-PATH GUARANTEE',font=f24,fill=(255,220,40,255))
    d.rectangle((88,128,W-88,H-145),outline=(0,220,255,255),width=5)

# Persistent, conspicuous decision panel.
panel_h=112
d.rectangle((80,H-panel_h-8,W-80,H-8),fill=(3,12,22,235),outline=(255,210,0,255),width=4)
d.text((100,H-panel_h+5),f'{a.case} — {a.classification}',font=f30,fill=(255,220,40,255))
text=a.labels or a.measurements
if len(text)>145: text=text[:142]+'...'
d.text((100,H-panel_h+47),text,font=f18,fill=(235,245,255,255))
im.convert('RGB').save(out,quality=95)
lock=datetime.now().astimezone().isoformat(timespec='seconds')
oh=sha(out)
final_ts=rows[-1]['timestamp_utc_minus_5'] if rows else 'N/A (source-card)'
entry=f'''\n+## {a.case}\n+\n+- First classification/decision: {a.classification}\n+- Marked image path: `MARKED_CHARTS/{a.case}_marked.png`\n+- Marked image SHA-256: `{oh}`\n+- Measurements/calculations: {a.measurements}\n+- Ordered reasoning: {a.reasoning}\n+- Required provenance labels: {a.provenance}\n+- Confidence: {a.confidence}\n+- Missing/unresolved information: {a.missing}\n+- FUTURE INFORMATION USED: NO\n+- LOCKED {lock}\n+'''
with open(os.path.join(root,'FIRST_ATTEMPT.md'),'a') as f:f.write(entry)
with open(os.path.join(root,'work','case_ledger.tsv'),'a') as f:
    f.write('\t'.join([a.case,a.image,a.csv or '',out,oh,final_ts,a.decision_ts,lock])+'\n')
print(f'{a.case}\t{out}\t{oh}\t{final_ts}\t{lock}')
