#!/usr/bin/env python3
"""Voice-pitch (F0) profile of a lesson's audio, for speaker identification.

Reproducible, no third-party audio libraries: numpy + the stdlib `wave` module.

Method: 8 kHz mono PCM -> 48 ms frames, 24 ms hop -> keep frames whose RMS is above
the 60th percentile of all frame RMS (voiced/speech frames) -> per-frame F0 by
normalized autocorrelation peak in the 70-320 Hz band, keeping only frames whose peak
correlation exceeds 0.35 (periodic = voiced). Report the median and quartiles of the
per-frame F0, overall and per 60-second block.

Usage:  python3 f0_profile.py FILE.wav [block_seconds]
"""
import sys, wave, numpy as np

path = sys.argv[1]
BLOCK = int(sys.argv[2]) if len(sys.argv) > 2 else 60

w = wave.open(path, 'rb')
sr = w.getframerate()
n = w.getnframes()
x = np.frombuffer(w.readframes(n), dtype=np.int16).astype(np.float64)
w.close()

FRAME = int(0.048 * sr)          # 384 samples @ 8 kHz
HOP = int(0.024 * sr)
nf = 1 + (len(x) - FRAME) // HOP
idx = np.arange(FRAME)[None, :] + HOP * np.arange(nf)[:, None]
F = x[idx]
F = F - F.mean(axis=1, keepdims=True)
rms = np.sqrt((F ** 2).mean(axis=1))
thr = np.percentile(rms, 60)
voiced_i = np.nonzero(rms > thr)[0]

lo_lag, hi_lag = int(sr / 320), int(sr / 70)      # 25 .. 114 samples
f0 = np.full(nf, np.nan)
win = np.hanning(FRAME)
for i in voiced_i:
    f = F[i] * win
    ac = np.correlate(f, f, mode='full')[FRAME - 1:]
    if ac[0] <= 0:
        continue
    seg = ac[lo_lag:hi_lag] / ac[0]
    k = int(np.argmax(seg))
    if seg[k] > 0.35:
        f0[i] = sr / (lo_lag + k)

ok = ~np.isnan(f0)
vals = f0[ok]
print(f'file={path}  sr={sr}  dur={len(x)/sr:.1f}s  frames={nf}  voiced={len(voiced_i)}  pitched={ok.sum()}')
print(f'OVERALL  median_F0={np.median(vals):.1f} Hz   q25={np.percentile(vals,25):.1f}  '
      f'q75={np.percentile(vals,75):.1f}  mean={vals.mean():.1f}')

print(f'\nper-{BLOCK}s block (start_s, n_pitched, median_F0):')
per = int(BLOCK * sr / HOP)
rows = []
for b in range(0, nf, per):
    seg = f0[b:b + per]
    s = seg[~np.isnan(seg)]
    if len(s) >= 30:
        rows.append((b * HOP / sr, len(s), float(np.median(s))))
for t, c, m in rows:
    print(f'{t:8.0f} {c:6d} {m:7.1f}')
meds = np.array([r[2] for r in rows])
print(f'\nblock medians: n={len(meds)} min={meds.min():.1f} max={meds.max():.1f} '
      f'median={np.median(meds):.1f} sd={meds.std():.1f}')
