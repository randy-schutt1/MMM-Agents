#!/usr/bin/env python3
import csv, hashlib, os
from datetime import datetime

exam='/Users/randyschutt/Desktop/Trading/MMM-Agents/20_CHART_HEAVY_PRACTICAL_V01_V10'
attempt=os.path.join(exam,'attempts/AI_STUDENT_PRACTICAL_002')
def sha(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()
with open(os.path.join(attempt,'work/case_ledger.tsv'),newline='') as f:
    rows=list(csv.DictReader(f,delimiter='\t'))
expected=[f'A{i:02d}' for i in range(1,13)]
for b in 'BCDEFG': expected += [f'{b}{i:02d}' for i in range(1,9)]
assert [r['case'] for r in rows]==expected, 'case order mismatch'
assert len(rows)==60
marked=os.listdir(os.path.join(attempt,'MARKED_CHARTS'))
assert len(marked)==60 and set(marked)=={f'{c}_marked.png' for c in expected}
for r in rows: assert sha(r['marked'])==r['marked_sha256']
with open(os.path.join(attempt,'FIRST_ATTEMPT.md')) as f: first=f.read()
assert first.count('FUTURE INFORMATION USED: NO')==60
assert first.count('- LOCKED ')==60

packet=sha(os.path.join(exam,'STUDENT_PRACTICAL_PACKET.md'))
index=sha(os.path.join(exam,'assets/ASSET_INDEX.md'))
template=sha(os.path.join(exam,'RESULTS_TEMPLATE.md'))
complete=datetime.now().astimezone().isoformat(timespec='seconds')
lines=[]
lines += ['# Attempt Manifest — AI_STUDENT_PRACTICAL_002','',
          '- Exam start: `2026-08-13T21:04:05-04:00`',f'- Exam completion: `{complete}`',
          f'- Packet SHA-256: `{packet}`',f'- Asset-index SHA-256: `{index}`',
          f'- Results-template SHA-256: `{template}`','- Case order: `A01…A12, B01…B08, C01…C08, D01…D08, E01…E08, F01…F08, G01…G08`',
          '- Cases locked: `60`','- Marked chart duplicates: `60`','- Original assets modified: `NO`','- Reveal protocol/image accessed: `NO`',
          '- Forbidden access: `NONE`','']
lines += ['## Standing files accessed','',
          '- `STUDENT_PRACTICAL_PACKET.md`', '- `RESULTS_TEMPLATE.md`','- `assets/ASSET_INDEX.md`','']
lines += ['## Case assets accessed in strict order','']
for r in rows:
    parts=[f'`{os.path.relpath(r["image"],exam)}`']
    if r['csv']: parts.append(f'`{os.path.relpath(r["csv"],exam)}`')
    lines.append(f'- {r["case"]}: '+', '.join(parts))
lines += ['','## Marked-chart hashes and locks','']
for r in rows:
    rel=os.path.relpath(r['marked'],attempt)
    lines.append(f'- {r["case"]}: `{rel}` | SHA-256 `{r["marked_sha256"]}` | LOCKED `{r["locked"]}`')
lines += ['','## Visible-only CSV cutoff verification','',
          '| Case | Final CSV timestamp (UTC-5) | Decision timestamp (UTC-5) | Check |','|---|---|---|---|']
for r in rows:
    if r['csv']:
        final=r['final_csv_timestamp']; dec=r['decision_timestamp'].replace(' UTC-5','')
        ok=final<=dec
        assert ok
        lines.append(f'| {r["case"]} | {final} | {dec} | PASS (`final <= decision`) |')
lines += ['','## Attempt-owned/helper files accessed','',
          '- `attempts/AI_STUDENT_PRACTICAL_002/FIRST_ATTEMPT.md`',
          '- `attempts/AI_STUDENT_PRACTICAL_002/ATTEMPT_MANIFEST.md`',
          '- `attempts/AI_STUDENT_PRACTICAL_002/work/mark_case.py`',
          '- `attempts/AI_STUDENT_PRACTICAL_002/work/case_ledger.tsv`',
          '- `attempts/AI_STUDENT_PRACTICAL_002/work/finalize_manifest.py`',
          '- `attempts/AI_STUDENT_PRACTICAL_002/MARKED_CHARTS/*.png` (the 60 individually listed above)',
          '- `/System/Library/Fonts/Supplemental/Arial.ttf` (annotation font)',
          '- Standard local executables/libraries used: `sed`, `tail`, `cat`, `wc`, `file`, `shasum`, `date`, `mkdir`, `python3`, Pillow.','',
          '## Validation summary','',
          '- Case sequence and count: `PASS (60/60)`',
          '- Exact `FUTURE INFORMATION USED: NO` count: `PASS (60)`',
          '- Exact `LOCKED` field count: `PASS (60)`',
          '- Marked-file count and filenames: `PASS (60)`',
          '- Recomputed marked-file hashes match ledger: `PASS (60/60)`',
          '- Visible-only final timestamps at or before decision timestamps: `PASS (52/52)`',
          '- Source-card cases: `8` (CSV cutoff check not applicable)','',
          '## Signed declaration','',
          'I, **AI_STUDENT_PRACTICAL_002**, declare that I completed this Phase A attempt in packet order, used no future information, accessed no reveal material, used only the standing allowlist documents and each exact current-case asset, preserved all originals, and made no forbidden access.','',
          f'Signed: **AI_STUDENT_PRACTICAL_002**  ',f'Timestamp: `{complete}`','']
with open(os.path.join(attempt,'ATTEMPT_MANIFEST.md'),'w') as f:f.write('\n'.join(lines))
print(complete, len(rows), len(marked), first.count('FUTURE INFORMATION USED: NO'), first.count('- LOCKED '))
