#!/usr/bin/env python3
"""Verify every quoted-with-a-marker fragment in a V06 artifact against the transcript.

Two checks, run over any number of markdown files:

  1. MARKER EXISTENCE — every `[HH:MM:SS]` citation resolves to a marker in
     02_TRANSCRIPTS/V06/V06_TRANSCRIPT.md.
  2. QUOTE MATCH — every *"..."* immediately followed by one or more `[HH:MM:SS]`
     citations actually occurs in the transcript, in the window spanned by those
     markers (padded by --pad seconds either side).

Normalisation before matching: collapse whitespace, drop editorial insertions in
square brackets (the "[trade]" convention used to gloss ASR garble), drop ellipses,
strip markdown bold/italic markers, and case-fold. Quotes containing a literal "…"
are matched limb-by-limb: every comma-free segment must be found in the window.

usage: python3 check_quotes.py FILE [FILE ...] [--pad 90]
Exit status 1 if anything fails, so it can gate a commit.
"""
import re
import sys

TRANSCRIPT = '02_TRANSCRIPTS/V06/V06_TRANSCRIPT.md'


def load_transcript(path):
    raw = open(path).read()
    body = raw[raw.index('\n[00:00:00]'):]
    per = {}
    cur = None
    for line in body.splitlines():
        m = re.fullmatch(r'\[(\d\d):(\d\d):(\d\d)\]', line.strip())
        if m:
            cur = int(m[1]) * 3600 + int(m[2]) * 60 + int(m[3])
            per[cur] = ''
        elif cur is not None and line.strip():
            per[cur] = (per[cur] + ' ' + line.strip()).strip()
    return per


def norm(s):
    s = re.sub(r'\[[^\]]*\]', ' ', s)          # editorial glosses
    s = s.replace('…', ' ').replace('—', ' ').replace('–', ' ')
    s = s.replace('’', "'").replace('“', '"').replace('”', '"')
    s = re.sub(r'[*_`]', '', s)
    s = re.sub(r'[^a-z0-9\'% ]+', ' ', s.lower())
    return re.sub(r'\s+', ' ', s).strip()


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    pad = 90
    if '--pad' in sys.argv:
        pad = int(sys.argv[sys.argv.index('--pad') + 1])
    per = load_transcript(TRANSCRIPT)
    secs = sorted(per)
    marker_set = set(secs)

    fails = 0
    for path in args:
        text = open(path).read()
        cites = re.findall(r'`\[(\d\d):(\d\d):(\d\d)\]`', text)
        cited = {int(h) * 3600 + int(m) * 60 + int(s) for h, m, s in cites}
        missing = sorted(c for c in cited if c not in marker_set)
        print(f'== {path}')
        print(f'   citations: {len(cited)} distinct   non-resolving: '
              f'{[f"{c//3600:02d}:{c%3600//60:02d}:{c%60:02d}" for c in missing]}')
        fails += len(missing)

        # Every *"..."* span, then keep the ones immediately followed by citations.
        # The quote body may not contain a table pipe, a blank line, or another quote
        # delimiter — without that the non-greedy match runs across table rows and
        # reports mismatches that are artifacts of the regex rather than of the text.
        pat = re.compile(r'\*"([^"|]+?)"\*[ ]*((?:[–-]?[ ]*`\[\d\d:\d\d:\d\d\]`[ ]*)+)')
        checked = ok = 0
        for m in pat.finditer(text):
            quote = m.group(1)
            if '\n\n' in quote:
                continue
            ms = [int(a) * 3600 + int(b) * 60 + int(c)
                  for a, b, c in re.findall(r'\[(\d\d):(\d\d):(\d\d)\]', m.group(2))]
            lo, hi = min(ms) - pad, max(ms) + pad
            window = ' '.join(per[s] for s in secs if lo <= s <= hi)
            wn = norm(window)
            limbs = [l for l in re.split(r'…|\.\.\.', quote) if norm(l)]
            checked += 1
            if all(norm(l) in wn for l in limbs):
                ok += 1
            else:
                bad = [norm(l) for l in limbs if norm(l) not in wn]
                print(f'   QUOTE MISMATCH at {m.group(2).strip()}: {bad[0][:100]}')
                fails += 1
        print(f'   quotes checked: {checked}   matched: {ok}')
    print('FAILURES:', fails)
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
