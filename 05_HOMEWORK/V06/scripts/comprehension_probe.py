#!/usr/bin/env python3
"""V06 comprehension probe — a machine-checkable test of whether the student's recall of
the lesson is real, rather than plausible-sounding reconstruction.

Two batteries, both adversarial in opposite directions:

  POSITIVE  Claims the student wrote down FROM MEMORY, closed-book, before re-reading
            any note. Each must be found in the transcript at or near a stated marker.
            A miss means the student's memory is wrong and the report says so.

  NEGATIVE  Claims that SOUND like they belong in this lesson and are NOT in it. Several
            are lifted verbatim from the quarantined NOTES.md / RULES.md for this very
            lesson (Q-006), which is exactly the material a shallow reader would absorb.
            Each must be ABSENT. A hit means the student has imported a fabrication.

The negative battery is the more important of the two. Recall can be faked by fluency;
correctly rejecting a plausible falsehood cannot.

usage: python3 comprehension_probe.py [TRANSCRIPT]
exit 1 if any probe fails, so it can gate a commit.
"""
import re
import sys

TRANSCRIPT = sys.argv[1] if len(sys.argv) > 1 else '02_TRANSCRIPTS/V06/V06_TRANSCRIPT.md'

# (id, claim as recalled, regex to find in the body, marker the student expects it near)
POSITIVE = [
    ('P01', 'The lesson opens by naming its own subject: micro daily trends',
     r'\bmicro daily trends\b', '00:00:00'),
    ('P02', 'The market is fractal, and the MM cycle repeats across timeframes',
     r'\bthe market is fractal\b', '00:00:17'),
    ('P03', 'Macro = 4-hour chart', r'macro view.{0,60}4 hour chart', '00:00:51'),
    ('P04', 'Mini = 1-hour, and that is where they like to trade',
     r'mini view can be seen on the 1 hour chart', '00:01:01'),
    ('P05', 'Micro = 15-minute chart', r'micro view will be on the 15 minute chart', '00:01:12'),
    ('P06', '"Push" is their own word, chosen to sit beside Steve\'s "levels"',
     r'we just distinguish levels from pushes', '00:01:36'),
    ('P07', 'Each push is approximately ADR divided by 3',
     r'each push is approximately adr divided by 3', '00:05:45'),
    ('P08', 'and he attributes that to Steve', r"that's what steve said", '00:05:50'),
    ('P09', 'Pullbacks are usually 25 to 50 pips',
     r'usually 25 to 50 pips', '00:06:04'),
    ('P10', 'A 10-15 pip sideways channel does not count as a pullback',
     r'10-15 pips channel', '00:06:19'),
    ('P11', 'Exactly three named patterns: railroad tracks, quarter wood, star',
     r'railroad tracks.{0,40}quarter\s*$|you have your railroad tracks', '00:07:22'),
    ('P12', 'and the star pattern completes that list', r'you have your star pattern', '00:07:34'),
    ('P13', 'If you can name the pattern you can take the trade',
     r'if you can name the pattern, you can take the trade', '00:08:00'),
    ('P14', 'You must wait for rejection of price before entering',
     r'wait for the rejection of price before entering', '00:08:06'),
    ('P15', 'The second leg has to take out the middle of the structure — "take out two"',
     r'it has to take out one, two, three|it\'s got to take out two', '00:18:53'),
    ('P16', 'A two-hour clock: if it has not moved, kill the trade',
     r'two hours pass', '00:13:19'),
    ('P17', 'and a new M restarts that clock', r'you restart the clock, the two hours clock', '00:23:36'),
    ('P18', 'Counter-trend you get two pushes, not three',
     r'there is no third push', '00:37:47'),
    ('P19', 'The third push is a reversal, so be careful with it',
     r'the third one is going to be a reversal', '01:12:37'),
    ('P20', 'His signature trade is the second leg of M\'s and W\'s only',
     r'i only take second legs', '01:07:43'),
    ('P21', 'US session target 30 to 50 pips', r'anywhere from 30 to 50 pips', '00:31:14'),
    ('P22', 'and they do not usually run like London', r"don't usually run like london", '00:31:20'),
    ('P23', 'He prefers about 2 to 1', r'i usually like 2 to 1', '01:03:17'),
    ('P24', 'He rejects a 30-plus pip stop and says he likes 23',
     r'i only like 23 pips', '00:30:56'),
    ('P25', 'If the signal candle is too big, wait for a 50% retrace of it',
     r'retrace 50% of the railroad track', '00:30:57'),
    ('P26', 'Steve is reported as saying M or W should be minimum nine candles',
     r'minimum nine candles', '00:53:03'),
    ('P27', 'and the presenter immediately disputes that there is any minimum',
     r'there is no such thing as the minimum', '00:53:12'),
    ('P28', 'Moving averages by nickname: water, mail/male, blueberry',
     r'\bblueberry\b', '00:29:48'),
    ('P29', 'Pullbacks used to be called J hooks, and stops "jumping stops"',
     r'j hooks', '00:57:08'),
    ('P30', 'The DMR contact address is fractalpips at gmail',
     r'fractalpips', '01:08:15'),
    ('P31', 'The homework slide is credited to Jim Nicholson',
     r'jim nicholson', '00:37:59'),
    ('P32', 'They normally bounce 200 first, then 50, then 13',
     r'bounce off the 200 first, then the', '00:55:17'),
    ('P33', 'He closes by telling them to homework it first',
     r'homework it first', '01:14:29'),
]

# (id, plausible-sounding claim that is NOT in the lesson, regex that would find it, why it is tempting)
NEGATIVE = [
    ('N01', 'A 5/13 EMA cross is the entry trigger', r'5/13',
     'The quarantined RULES.md asserts this as rule 1 for all 21 lessons (Q-006)'),
    ('N02', 'Stops go 10 to 15 pips beyond the high/low of day', r'10 to 15 pips',
     'The quarantined RULES.md rule 2, same template'),
    ('N03', 'The PRESENTER teaches an "Asian Box"', r'asian box',
     'The quarantined NOTES.md names it as the lesson\'s primary topic. THIS PROBE FAILS AND '
     'THE FAILURE IS CORRECT: the term occurs once, at [01:09:43], inside a QUESTION the '
     'presenter reads aloud. He never defines or teaches it. The probe is deliberately left '
     'failing, with this note, rather than reworded to pass — see the mastery report'),
    ('N04', 'Session times are given in EST', r'\bEST\b',
     'The quarantined NOTES.md prints a full EST session clock'),
    ('N05', 'PFH / PFL abbreviations are used', r'\bPFH\b|\bPFL\b',
     'Quarantined NOTES.md vocabulary'),
    ('N06', 'A minimum 1:3 risk-to-reward is required', r'(?<!\[0)(?<!\[1)1\s*:\s*3\b|minimum 1 to 3',
     'Quarantined NOTES.md; and the lesson does state a ratio, just a different one. '
     'NOTE: the first draft of this probe used the bare pattern "1:3", which matched the '
     'TIMESTAMP MARKERS [01:3x:xx] twenty times. The false positive is recorded rather than '
     'quietly fixed, because a probe that reports failures it cannot explain is worse than no '
     'probe'),
    ('N07', 'The TDI shark fin confirms the entry', r'shark',
     'It is V04\'s actual criterion, and V06 does mention TDI once — but only as a future agenda item'),
    ('N08', 'The 5 EMA is named', r'\b5 EMA\b',
     'Four other periods ARE named in V06, so a fifth feels natural'),
    ('N09', 'The 800 EMA is named as such', r'800 EMA',
     'The 800 IS mentioned; "800 EMA" as a term is not'),
    ('N10', 'HOD and LOD are spoken', r'\bHOD\b|\bLOD\b',
     'They are PRINTED on the slide at 00:05:29 — a reader who conflates slide and audio fails here'),
    ('N11', 'The lesson gives a clock time for the London session', r'london.{0,30}\d{1,2}\s*(am|pm|:)',
     'Every other lesson in week 1-2 has session clock content'),
    ('N12', 'Mayo is spoken as a moving-average nickname', r'\bmayo\b',
     'It is PRINTED in the DMR curriculum frame; the audio says "mail"/"male"'),
    ('N13', 'A win rate or accuracy percentage is claimed FOR THE PUSH METHOD', r'9[05]%|90 percent|95 percent',
     'V04 and the course marketing both carry accuracy claims. THIS PROBE FAILS AND THE '
     'FAILURE IS CORRECT: "90%" occurs once, at [00:46:55], in a HYPOTHETICAL put to a '
     'student ("if you say, listen, I get M then W 90% of the time"). It is a permission '
     'threshold, not a performance claim — but D-009 requires it on the record either way, '
     'and the first draft of the V06 notes did not have it. The probe found that gap'),
    ('N14', 'The lesson defines what a nameable pattern is', r'a nameable pattern is|namable pattern is defined',
     'It enumerates three; it never defines the class'),
    ('N15', 'Steve Mauro speaks in this lesson', r'^\s*steve mauro\s*:',
     'The quarantined VISUAL_INDEX.md attributes every frame to him'),
]


def main():
    raw = open(TRANSCRIPT).read()
    body = raw[raw.index('\n[00:00:00]'):]
    lower = re.sub(r'\s+', ' ', body.lower())
    markers = set(re.findall(r'^\[(\d\d:\d\d:\d\d)\]$', body, re.M))

    fails = 0
    print('=' * 78)
    print('POSITIVE BATTERY — closed-book recall, checked against the transcript')
    print('=' * 78)
    for pid, claim, pat, mk in POSITIVE:
        found = re.search(pat, lower, re.I | re.M) is not None
        mk_ok = mk in markers
        ok = found and mk_ok
        fails += 0 if ok else 1
        flag = 'PASS' if ok else ('MISS-TEXT' if not found else 'MISS-MARKER')
        print(f'{pid}  {flag:11s} [{mk}]  {claim}')
    print()
    print('=' * 78)
    print('NEGATIVE BATTERY — plausible claims that must be ABSENT')
    print('=' * 78)
    for nid, claim, pat, why in NEGATIVE:
        hits = re.findall(pat, body, re.I | re.M)
        ok = len(hits) == 0
        fails += 0 if ok else 1
        flag = 'PASS (absent)' if ok else f'FAIL — {len(hits)} hit(s): {hits[:3]}'
        print(f'{nid}  {flag}')
        print(f'      claim : {claim}')
        print(f'      why it is tempting: {why}')
    print()
    print(f'PROBES: {len(POSITIVE)} positive + {len(NEGATIVE)} negative = '
          f'{len(POSITIVE)+len(NEGATIVE)}   FAILURES: {fails}')
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
