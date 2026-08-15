"""
A-085 RE-VERIFICATION PROBE — does the M15 Trade Signal Line behave like the H1?

NOT a test of the method. A measurement of the arithmetic relationship between
two constructions, in the same class as the TDI band-basis comparison.

V12 [00:11:49]: "The TSL in essence is a polling of the one-hour chart, brought
into your view on the 15 minute."
V12 [00:12:07]: "when you get a crossover right here in essence, you now have a
signal on the one-hour chart"

Parameters: MMM_TDI.txt primary instrument (D-053). RSI 21 [TIER 1], fast 2,
slow 7, all SMA. Pine conventions: ta.rsi = Wilder's RMA.
"""
import numpy as np, csv, datetime as dt

RSI_LEN, FAST, SLOW = 21, 2, 7

def load(p):
    ts, c = [], []
    with open(p) as f:
        for row in csv.reader(f):
            if len(row) < 6: continue
            ts.append(dt.datetime.strptime(row[0]+" "+row[1], "%Y.%m.%d %H:%M"))
            c.append(float(row[5]))
    return np.array(ts), np.array(c)

def rsi(x, n):                      # Wilder's RMA, matches Pine ta.rsi
    d = np.diff(x, prepend=x[0])
    up = np.where(d > 0, d, 0.0); dn = np.where(d < 0, -d, 0.0)
    au = np.full(len(x), np.nan); ad = np.full(len(x), np.nan)
    au[n] = up[1:n+1].mean(); ad[n] = dn[1:n+1].mean()
    a = 1.0/n
    for i in range(n+1, len(x)):
        au[i] = a*up[i] + (1-a)*au[i-1]
        ad[i] = a*dn[i] + (1-a)*ad[i-1]
    rs = np.divide(au, ad, out=np.full(len(x), np.inf), where=ad != 0)
    return 100 - 100/(1+rs)

def sma(x, n):
    out = np.full(len(x), np.nan)
    v = ~np.isnan(x); s = np.nan_to_num(x)
    cs = np.cumsum(np.insert(s, 0, 0.0)); cv = np.cumsum(np.insert(v.astype(int), 0, 0))
    for i in range(n-1, len(x)):
        if cv[i+1]-cv[i+1-n] == n: out[i] = (cs[i+1]-cs[i+1-n])/n
    return out

base = "06_MANUAL_BACKTEST/datasets/HISTDATA_GBPUSD_M1/derived_ext/"
t15, c15 = load(base+"GBPUSD_M15_ARMA.csv")
t60, c60 = load(base+"GBPUSD_H1_ARMA.csv")
print(f"M15 bars {len(c15):,}   H1 bars {len(c60):,}")

r15 = rsi(c15, RSI_LEN); f15 = sma(r15, FAST); s15 = sma(r15, SLOW)
r60 = rsi(c60, RSI_LEN); f60 = sma(r60, FAST); s60 = sma(r60, SLOW)

# Align H1 onto M15 with NO look-ahead: each M15 bar sees the last CLOSED H1 bar.
idx = np.searchsorted(t60, t15, side="right") - 1
ok = idx >= 0
r60_on15 = np.where(ok, r60[np.clip(idx,0,None)], np.nan)
f60_on15 = np.where(ok, f60[np.clip(idx,0,None)], np.nan)
s60_on15 = np.where(ok, s60[np.clip(idx,0,None)], np.nan)

def corr(a,b):
    m = ~(np.isnan(a)|np.isnan(b)); return np.corrcoef(a[m],b[m])[0,1]

print("\n=== 1. DOES THE M15 TSL TRACK THE H1 RSI LINE? (Pearson r) ===")
print(f"  M15 TSL  (SMA7 of RSI)   vs  H1 RSI(21)          r = {corr(s15, r60_on15):.4f}")
print(f"  M15 TSL                  vs  H1 RSI Price Line   r = {corr(s15, f60_on15):.4f}")
print(f"  M15 TSL                  vs  H1 TSL (SMA7)       r = {corr(s15, s60_on15):.4f}")
print("  -- reference lines --")
print(f"  M15 FAST (SMA2 of RSI)   vs  H1 RSI(21)          r = {corr(f15, r60_on15):.4f}")
print(f"  M15 raw RSI(21)          vs  H1 RSI(21)          r = {corr(r15, r60_on15):.4f}")

print("\n=== 2. MEAN ABSOLUTE DIFFERENCE, in RSI points ===")
for nm, a in (("M15 TSL  vs H1 RSI", s15), ("M15 FAST vs H1 RSI", f15), ("M15 raw  vs H1 RSI", r15)):
    m = ~(np.isnan(a)|np.isnan(r60_on15)); print(f"  {nm}:  {np.abs(a[m]-r60_on15[m]).mean():5.2f}")

print("\n=== 3. ⭐ THE OPERATIVE TEST — V12 [00:12:07] ===")
print("    'when you get a crossover right here ... you now have a signal on the one-hour chart'")
# M15 crossover = fast crosses slow. Side = sign(fast - slow).
side15 = np.sign(f15 - s15)
side60 = np.sign(f60_on15 - s60_on15)
cross15 = np.zeros(len(side15), bool)
cross15[1:] = (side15[1:] != side15[:-1]) & ~np.isnan(f15[1:]) & ~np.isnan(s15[1:]) & (side15[1:] != 0)
m = cross15 & ~np.isnan(side60)
agree = side15[m] == side60[m]
print(f"  M15 fast/slow crossovers found: {m.sum():,}")
print(f"  ...where the H1 TDI is ALREADY on the same side: {agree.sum():,}  ({100*agree.mean():.1f}%)")

# And: does an M15 crossover coincide with an H1 crossover nearby?
cross60 = np.zeros(len(side60), bool)
sd = side60.copy()
cross60[1:] = (sd[1:] != sd[:-1]) & ~np.isnan(sd[1:]) & ~np.isnan(sd[:-1]) & (sd[1:] != 0)
for w in (1, 2, 4, 8):
    hits = 0
    ci = np.flatnonzero(m)
    for i in ci:
        lo, hi = max(0, i-w), min(len(cross60), i+w+1)
        if cross60[lo:hi].any(): hits += 1
    print(f"  ...with an H1 crossover within ±{w} M15 bars: {hits:,}  ({100*hits/len(ci):.1f}%)")

print("\n=== 4. THE CONTROL — is 7 special, or would any smoothing do? ===")
print("    If SMA(7) is 'polling the H1', longer/shorter smoothings should track it WORSE.")
for n in (2, 4, 7, 10, 14, 21, 28):
    print(f"  SMA({n:2d}) of M15 RSI  vs  H1 RSI(21):  r = {corr(sma(r15,n), r60_on15):.4f}")

print("\n=== 5. THE BASE RATE — what does 42.9% mean? ===")
m_all = ~(np.isnan(side15) | np.isnan(side60)) & (side15 != 0) & (side60 != 0)
print(f"  On ALL M15 bars, H1 TDI on the same side as M15 TDI: {100*(side15[m_all]==side60[m_all]).mean():.1f}%")
print(f"  On M15 CROSSOVER bars only:                          {100*agree.mean():.1f}%")
print("  -> a crossover bar is the moment M15 flips, so it is EXPECTED to")
print("     disagree with a slower series. The gap is the diagnostic, not 42.9 alone.")

ch = np.flatnonzero(cross60); print(f"\n  H1 fast/slow crossovers in the same span: {len(ch):,} over {len(c60):,} H1 bars")
print(f"  M15 fast/slow crossovers:                 {m.sum():,} over {len(c15):,} M15 bars")
print(f"  ratio M15:H1 crossovers = {m.sum()/max(len(ch),1):.2f}  (M15 has 4x the bars)")

print("\n=== 6. ⚠ WHAT V12 ACTUALLY CONDITIONED THE CLAIM ON ===")
print("  [00:12:18] 'you need to look at the one-hour chart NOT NECESSARILY")
print("             IF YOU GOT A SHARK FIN BLOOD IN THE WATER'")
print("  [00:12:24] 'BLOOD IN THE WATER indicates that the one-hour chart has")
print("             fired a signal at the same time or IN CONGRUENCY'")
print("  => The claim is SCOPED to shark-fin + blood-in-the-water setups.")
print("     It is NOT 'every crossover = an H1 signal'.")
print("     Section 3 above tested ALL 57,305 unfiltered crossovers, which is")
print("     NOT THE CLAIM V12 MADE.")
print("  => The filtered test CANNOT BE RUN: shark fin (A-032) and blood in the")
print("     water (A-031) are uncomputable because the band is unconstructible")
print("     (A-086 -- the PERIOD is never stated). D-052/D-053 changed none of that.")
