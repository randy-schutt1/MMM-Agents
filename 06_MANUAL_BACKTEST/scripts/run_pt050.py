#!/usr/bin/env python3
"""PT-050 -- V21's High/Low Trainer grid: the 20-pip spacing and the "50-pip average move".

Runs the test pre-registered in
`06_MANUAL_BACKTEST/PRE_REGISTERED/PT-050_the_high_low_trainer_grid.md`, committed
BEFORE this file existed. IF THIS RUNNER AND THAT FILE DISAGREE, THAT FILE GOVERNS.

The event is PT-047 §3's, reused verbatim and declared as a borrowed convention in
PT-050 §2a. Every scale used by a measure is stated inside that measure -- the lesson
of V20 R1 M1 (item 332).
"""
import json, os, sys
from math import sqrt
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mmm_lib as M

MIN_AGE, MAX_AGE, HORIZON = 8, 24, 16      # PT-047 §3, borrowed verbatim
GRID = (0.0, 20.0, 40.0)                   # PT-050 §3: G0=L, G1=L+20, G2=L+40
BAND = (40.0, 60.0)                        # PT-050 §2c: "about 50" fixed in advance
BOOT = 20000

def wilson(k, n, z=1.96):
    if n == 0: return (float('nan'), float('nan'))
    p=k/n; d=1+z*z/n; c=(p+z*z/(2*n))/d
    h=z*sqrt(p*(1-p)/n+z*z/(4*n*n))/d
    return 100*(c-h), 100*(c+h)

def boot_med(x, seed=None, it=BOOT):
    if len(x) < 2: return (float('nan'), float('nan'))
    rng=np.random.default_rng(M.SEED if seed is None else seed)
    m=[np.median(rng.choice(x,len(x),True)) for _ in range(it)]
    return float(np.percentile(m,2.5)), float(np.percentile(m,97.5))

def events(m15, days):
    post=(m15.mod>=M.BOX_END_MIN)&(m15.mod<M.DAY_END_MIN)
    out=[]
    for day in sorted(days["sd"].tolist()):
        m=post&(m15.sd==day); h,l=m15.h[m],m15.l[m]; n=len(h)
        if n < MIN_AGE+1+HORIZON: continue
        run=-np.inf; anchor=-1
        for t in range(n):
            if run>-np.inf:
                age=t-anchor
                if h[t]>run and MIN_AGE<=age<=MAX_AGE and t+HORIZON<n:
                    L=float(run); fwd=h[t+1:t+1+HORIZON]
                    mfe=max(0.0,(float(fwd.max())-L)/M.PIP)
                    filled=sum(1 for g in GRID if float(fwd.max()) >= L+g*M.PIP)
                    out.append((mfe,filled)); break
            if h[t]>run: run=float(h[t]); anchor=t
    return out

def n1(m15, days, seed=None):
    """Matched random windows: same horizon, same days/hours, NO exceed condition."""
    post=(m15.mod>=M.BOX_END_MIN)&(m15.mod<M.DAY_END_MIN)
    rng=np.random.default_rng(M.SEED if seed is None else seed)
    pool=[]
    for day in sorted(days["sd"].tolist()):
        m=post&(m15.sd==day); h=m15.h[m]
        if len(h)>=MIN_AGE+1+HORIZON: pool.append(h)
    out=[]
    for _ in range(2000):
        h=pool[rng.integers(len(pool))]
        t=int(rng.integers(0,len(h)-HORIZON-1))
        L=float(h[t]); fwd=h[t+1:t+1+HORIZON]
        out.append((max(0.0,(float(fwd.max())-L)/M.PIP),
                    sum(1 for g in GRID if float(fwd.max())>=L+g*M.PIP)))
    return out

def cell(arm, win):
    m15=M.window(M.load_m15(arm),win)
    days=M.build_days(m15,offset_min=0,require_full=True)
    ev=events(m15,days)
    mfe=np.array([e[0] for e in ev]); fills=[e[1] for e in ev]
    lo,hi=boot_med(mfe)
    k=int(((mfe>=BAND[0])&(mfe<=BAND[1])).sum()); wl,wh=wilson(k,len(mfe))
    dist={}
    for f in (0,1,2,3):
        c=fills.count(f); a,b=wilson(c,len(fills))
        dist[str(f)]=dict(n=c,pct=round(100*c/len(fills),1),wilson=[round(a,1),round(b,1)])
    b=n1(m15,days); bm=np.array([x[0] for x in b]); bf=[x[1] for x in b]
    return dict(arm=arm,window=win,n_events=len(ev),
                median_mfe=round(float(np.median(mfe)),2),
                median_ci=[round(lo,2),round(hi,2)],
                iqr=[round(float(np.percentile(mfe,25)),2),round(float(np.percentile(mfe,75)),2)],
                in_band_pct=round(100*k/len(mfe),1), in_band_wilson=[round(wl,1),round(wh,1)],
                fill_distribution=dist, modal_fill=max(dist,key=lambda x:dist[x]['n']),
                n1_median_mfe=round(float(np.median(bm)),2),
                n1_modal_fill=max(range(4),key=lambda f:bf.count(f)),
                n1_fill_pct={str(f):round(100*bf.count(f)/len(bf),1) for f in range(4)})

def main():
    M.qa_gate(); res={}
    for arm in ("A","B"):
        for win in ("W-A","W-B"):
            r=cell(arm,win); res[f"{arm}|{win}"]=r
            print(f"\n=== {arm}|{win}  n_events={r['n_events']} ===")
            print(f"  A: median MFE {r['median_mfe']} ci={r['median_ci']} IQR={r['iqr']}"
                  f"  in[40,60]={r['in_band_pct']}% W{r['in_band_wilson']}")
            print(f"     N1 median MFE {r['n1_median_mfe']}")
            print("  B: fills " + "  ".join(
                f"{f}:{r['fill_distribution'][f]['pct']}%W{r['fill_distribution'][f]['wilson']}" for f in "0123"))
            print(f"     modal={r['modal_fill']}   N1 modal={r['n1_modal_fill']} N1 pct={r['n1_fill_pct']}")
    p=res["A|W-A"]; fired=[]
    inb=lambda v: BAND[0]<=v<=BAND[1]
    for k,r in res.items():
        if r['n_events']<30: fired.append(f"{k}: n<30")
        if inb(r['median_mfe'])!=inb(p['median_mfe']): fired.append(f"{k}: band membership disagrees")
        if r['modal_fill']!=p['modal_fill']: fired.append(f"{k}: modal fill differs")
    lo,hi=p['median_ci']
    if fired: v="FRAGILE"
    elif inb(p['median_mfe']) and inb(lo) and inb(hi) and abs(p['median_mfe']-p['n1_median_mfe'])>1e-9: v="CONFIRMED"
    elif inb(p['median_mfe']): v="PARTIAL"
    elif hi<BAND[0] or lo>BAND[1]: v="REFUTED"
    else: v="PARTIAL"
    out=dict(test="PT-050",seed=M.SEED,band=list(BAND),grid=list(GRID),
             primary_cell="A|W-A",n3_fired=fired,verdict=v,cells=res)
    print("\nN3 fired:",fired if fired else "NO"); print("VERDICT:",v)
    d=os.path.join(os.path.dirname(__file__),"..","V21","data","pt050_results.json")
    os.makedirs(os.path.dirname(d),exist_ok=True)
    json.dump(out,open(d,"w"),indent=2); print("wrote",os.path.normpath(d))

if __name__=="__main__": main()
