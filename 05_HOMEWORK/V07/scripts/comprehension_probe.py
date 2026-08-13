#!/usr/bin/env python3
"""V07 comprehension probe — a machine-checkable test of whether the student's recall of
the lesson is real, rather than plausible-sounding reconstruction.

Three batteries.

  POSITIVE  Claims the student wrote down from memory of the lesson, WITHOUT the
            transcript open while drafting them, but AFTER V07_SOURCE_NOTES.md had been
            written. Each must be found in the transcript at or near a stated marker.

            THIS IS WEAKER THAN V06's PROBE CLAIMED FOR ITSELF AND THE DIFFERENCE IS
            STATED RATHER THAN GLOSSED: writing the notes first means the positive battery
            tests retention of this session's own work, not first-exposure recall. It is
            reported for what it is. The negative and reasoning batteries do not have this
            weakness -- a fabrication cannot be absorbed from notes that never contained
            it, and a relation between two passages cannot be produced by fluency.

  NEGATIVE  Claims that SOUND like they belong in this lesson and are NOT in it. Most are
            lifted verbatim from the quarantined NOTES.md / VISUAL_INDEX.md for this very
            lesson (Q-008), which is exactly the material a shallow reader would absorb.
            Each must be ABSENT. A hit means the student has imported a fabrication.

  REASONING A trace battery, new in V07. Each item is a claim about the lesson's STRUCTURE
            or ARITHMETIC that cannot be answered by recognising a phrase -- it requires
            the student to have understood how two parts of the lesson relate, or to have
            computed something. Each is checked by a predicate over the transcript rather
            than by a regex over one line.

The negative battery is more important than the positive one, and the reasoning battery is
more important than either: recall can be faked by fluency; correctly rejecting a plausible
falsehood cannot, and neither can a relation between two passages.

usage: python3 05_HOMEWORK/V07/scripts/comprehension_probe.py [TRANSCRIPT]
exit 1 if any probe fails, so it can gate a commit.
"""
import re
import sys

TRANSCRIPT = sys.argv[1] if len(sys.argv) > 1 else '02_TRANSCRIPTS/V07/V07_TRANSCRIPT.md'

# (id, claim as recalled, regex to find in the body, marker the student expects it near)
POSITIVE = [
    ('P01', 'The lesson opens on its own title, "best trade grabs" (ASR: graphs)',
     r'best trade graphs', '00:00:00'),
    ('P02', 'It immediately asks whether the winning charts tell the whole story',
     r'do they tell us the whole story', '00:00:32'),
    ('P03', 'Left pane is the entry, right edge is what happened after',
     r'the right edge will tell us what happened after that entry', '00:00:53'),
    ('P04', 'He deliberately includes a trade where the entry was perfect and it paid nothing',
     r'even though the entry was perfect', '00:01:06'),
    ('P05', 'and that one only consolidated', r'it only consolidated', '00:01:16'),
    ('P06', 'Left-hand side 15 minute, right-hand side one hour',
     r'left-hand side will be the 15 minute, right-hand side will be the one hour', '00:02:25'),
    ('P07', 'Four candidates: setup, level, pattern, exit, risk-to-reward',
     r'is it the level that we need to be at', '00:03:37'),
    ('P08', 'He refuses to rank them — they are all valid',
     r'they all are valid', '00:04:38'),
    ('P09', 'His own preference is setups and levels, stated as opinion',
     r'my personal opinion is i like to see setups', '00:04:49'),
    ('P10', 'He will not use the H word any more — it is R&D',
     r"i won't even use the h word anymore", '00:05:14'),
    ('P11', 'M\'s and W\'s are everywhere', r"m's and w's are everywhere", '00:06:32'),
    ('P12', 'so how do we tell which ones work', r'how do we differentiate which ones work', '00:06:39'),
    ('P13', 'Taking patterns randomly everywhere does not always pay out',
     r'taking patterns randomly everywhere', '00:07:02'),
    ('P14', 'High-low as the possible holy grail of daily trading',
     r'holy grail of daily trading', '00:07:13'),
    ('P15', 'Get in within a few pips of the high or low of the day and make pips every day',
     r"you're going to make pips every day", '00:07:17'),
    ('P16', 'Jim is the one who is a master at the high of the day, not him',
     r'he seems to be a master at the high of the day', '00:07:38'),
    ('P17', 'Confirmed second legs have little to no drawdown',
     r'second legs confirm have little to no drawdown', '00:08:04'),
    ('P18', 'It is not how many pips you make, it is how many you keep',
     r"it's how many pips you keep", '00:10:03'),
    ('P19', 'Patience is paramount — wait for the market to come to you',
     r'now you are waiting for the market to come to you', '00:10:48'),
    ('P20', 'Count how many times it occurred over a year',
     r'how many times over a year', '00:12:09'),
    ('P21', 'Flashcards embed the image implicitly in your mind',
     r'implicitly embedded in your mind', '00:13:01'),
    ('P22', 'At level one you expect an A pattern or a single leg',
     r'we expect an a pattern or a single leg', '00:14:10'),
    ('P23', 'and a second leg at level one is a gift', r"that's a gift on there", '00:14:16'),
    ('P24', 'He waits until about five seconds before the candle closes',
     r'five seconds before that candle closed', '00:15:58'),
    ('P25', 'Steve talks about second legs all the time',
     r'steve talks about it all the time', '00:19:32'),
    ('P26', 'Send your trades in and we will post them',
     r'send them in, we want to see what you', '00:21:36'),
    ('P27', 'The vertical broken line is the day separator',
     r'this is the day separator', '00:24:03'),
    ('P28', 'The brown line is the ADR and it changes colour when it is met',
     r'that brown line there is the adr', '00:25:26'),
    ('P29', 'The yellow one is a five moving average',
     r'this yellow one is a five moving average', '00:25:34'),
    ('P30', 'Stair steps are a higher-timeframe average that cannot fill the gaps',
     r"doesn't know how to fill in the gaps", '00:26:29'),
    ('P31', 'He added the stair-step averages and never actually uses them',
     r'i actually never use it', '00:27:00'),
    ('P32', 'Level three is where he would trap, if he were the market maker',
     r'in my opinion, that would be at level three', '00:29:02'),
    ('P33', 'A student asks outright whether all the DMR speakers agree about second legs',
     r'do all the dms speaker agree on this', '00:29:49'),
    ('P34', 'He likes two types: pin through the level then a confirmed candle',
     r'pin through it and come back up and give me a confirmed candle', '00:30:44'),
    ('P35', 'and close below the first leg then railroad tracks on the very next candle',
     r'railroad tracks right back into the range on the next very next candle', '00:30:52'),
    ('P36', 'He will not trade the tilted ones — not enough homework on them',
     r"i haven't done enough homework on them", '00:31:06'),
    ('P37', 'You may only trade 50% of what you see',
     r'you may only trade 50% of what you see', '00:31:29'),
    ('P38', 'He looks at at least the 10 pairs from the DMR',
     r'at least the 10 from dmr', '00:32:09'),
    ('P39', 'It is always another trade', r"it's always another trade", '00:35:05'),
    ('P40', 'The next question is from Steve — who is in the audience',
     r'next question from steve', '00:35:46'),
    ('P41', 'A missed trade is somebody else\'s trade',
     r"that was somebody else's trade", '00:36:15'),
    ('P42', 'Plan for the whole week, not just today',
     r'you have to plan for the entire week', '00:40:15'),
    ('P43', 'A student recommends analysing at least 200 examples, and he agrees',
     r'at least 200 examples', '00:41:01'),
    ('P44', 'Better to be out of a trade wishing you were in than in wishing you were out',
     r'better to not be in a trade and wishing you were', '00:45:35'),
    ('P45', 'Size from one trade of 50 pips and work out the percentage of equity',
     r'one trade, 50 pips', '00:46:06'),
]

# (id, plausible-sounding claim that is NOT in the lesson, regex that would find it, why it is tempting)
NEGATIVE = [
    ('N01', 'A 5/13 EMA cross is the entry trigger, confirmed on the M15 close', r'5/13|\bM15\b',
     'The quarantined RULES.md asserts this as rule 1 for all 21 lessons (Q-007/Q-008)'),
    ('N02', 'Stops go 10 to 15 pips beyond the high/low of day', r'10 to 15 pips|10-15 pips',
     'The quarantined RULES.md rule 2, same template'),
    ('N03', 'The lesson teaches an Asian accumulation box', r'asian box|accumulation',
     'The quarantined NOTES.md names it as the lesson\'s primary topic'),
    ('N04', 'Session times are given in EST', r'\bEST\b',
     'The quarantined NOTES.md prints a full EST session clock for this lesson'),
    ('N05', 'PFH / PFL abbreviations are used', r'\bPFH\b|\bPFL\b|peak formation',
     'Quarantined NOTES.md vocabulary'),
    ('N06', 'A minimum 1:3 risk-to-reward is required', r'1\s*:\s*3\b|minimum 1 to 3',
     'Quarantined NOTES.md. The lesson does talk about risk and reward, qualitatively, four times'),
    ('N07', 'The TDI shark fin is named as the confirmation', r'shark',
     'It is V04\'s actual criterion, and V07 PRINTS "SHARK FIN IN TDI" on frame '
     'V07_00-18-25 — so a reader who conflates slide and audio fails here. The audio '
     'never says it'),
    ('N08', 'The moving averages are given their nicknames with periods attached',
     r'\bmustard\b|\braspberry\b',
     'Quarantined NOTES.md lists 5 Mustard / 13 Water / 50 Mayo / 200 Blueberry / 800 '
     'Raspberry. Water, mail/male and blueberry ARE spoken; mustard and raspberry are not, '
     'and no period is ever attached to any of them'),
    ('N09', 'The 800 average is named', r'\b800\b',
     'V06 names the 800; a reader carrying V06 forward would expect it here'),
    ('N10', 'HOD and LOD are spoken', r'\bHOD\b|\bLOD\b',
     'They are PRINTED on the MT4 panel in three curated frames. The audio says '
     '"high of the day" in words'),
    ('N11', 'The lesson gives a clock time for the London session',
     r'london.{0,30}\d{1,2}\s*(am|pm|:)',
     'Every lesson in weeks 1-2 that this project has processed has session clock content. '
     'V07 has none at all'),
    ('N12', 'Mayo is spoken as a moving-average nickname', r'\bmayo\b',
     'It is what the speaker means at [00:01:11] and five other markers; the ASR renders it '
     '"mail"/"male" every time'),
    ('N13', 'A win rate or accuracy percentage is claimed', r'9[05]\s*%|90 percent|95 percent',
     'The course marketing carries a 90-95% claim (D-009) and V04 repeats one. V07 makes no '
     'accuracy claim at all'),
    ('N14', 'The lesson defines what a level is', r'a level is defined|level (one|1) is defined|definition of a level',
     'It uses the form level <N> 35 times and the bare token level 56 times. A-004 stays open'),
    ('N15', 'Steve Mauro speaks in this lesson', r'^\s*steve mauro\s*:|steve mauro',
     'The quarantined VISUAL_INDEX.md attributes all seven of its frames to '
     '"Steve Mauro breaking down..."'),
    ('N16', 'GBP/USD is used as an example', r'gbp|pound dollar|cable',
     'It is the project\'s primary instrument under D-007, and the examples are AUD/USD, '
     'EUR/USD and EUR/JPY instead'),
]


# ---------------------------------------------------------------------------
# REASONING BATTERY — each item is (id, question, expected answer in words, predicate)
# The predicate takes (body, lower, markers, entries) and returns (bool, evidence string).
# ---------------------------------------------------------------------------
def _r01(body, lower, markers, entries):
    """Who is the speaker? Answer: not Steve. Every 'Steve' must be third-person."""
    hits = [(m, t) for m, t in entries if re.search(r'\bSteve\b', t)]
    ok = len(hits) == 2 and all(not re.match(r'\s*Steve[:,]', t) for _, t in hits)
    return ok, f'{len(hits)} Steve mentions: ' + '; '.join(f'{m} {t[:48]}' for m, t in hits)


def _r02(body, lower, markers, entries):
    """The lesson's exit target is 50 pips and it recurs. Answer: >=3 independent markers."""
    hits = [m for m, t in entries if re.search(r'\b50\b', t) and
            re.search(r'nice 50|out for 50|getting out of 50|one trade, 50 pips', t, re.I)]
    return len(hits) >= 3, f'{len(hits)} markers: {hits}'


def _r03(body, lower, markers, entries):
    """Hi-Lo is deferred to Jim, not taught. Answer: Jim named >=3x, all third-person."""
    hits = [m for m, t in entries if re.search(r'\bJim\b', t)]
    return len(hits) >= 3, f'Jim at {hits}'


def _r04(body, lower, markers, entries):
    """The four second-leg variants are enumerated inside one contiguous stretch."""
    lo = [m for m, t in entries if 'different types of' in t.lower()]
    hi = [m for m, t in entries if 'i like those as well' in t.lower()]
    ok = bool(lo and hi and lo[0] < hi[0])
    return ok, f'enumeration runs {lo[:1]} -> {hi[:1]}'


def _r05(body, lower, markers, entries):
    """The homework is renamed, and the rename is asserted before the assignment is given."""
    ren = [m for m, t in entries if re.search(r'h word|known as homework', t, re.I)]
    asg = [m for m, t in entries if 'how many times over a year' in t.lower()]
    ok = bool(ren and asg and min(ren) < min(asg))
    return ok, f'rename first at {min(ren) if ren else None}, assignment at {min(asg) if asg else None}'


def _r06(body, lower, markers, entries):
    """The level-1 expectation and the level-1 exception are adjacent, in that order."""
    exp = [m for m, t in entries if 'we do not expect this' in t.lower()]
    exc = [m for m, t in entries if "that's a gift" in t.lower()]
    ok = bool(exp and exc and min(exp) < min(exc))
    return ok, f'expectation {exp[:1]} then exception {exc[:1]}'


def _r07(body, lower, markers, entries):
    """The student's 'do the speakers agree' question is NOT answered with a yes or a no."""
    q = [i for i, (m, t) in enumerate(entries) if 'speaker agree on this' in t.lower()]
    if not q:
        return False, 'question not found'
    nxt = " ".join(t for _, t in entries[q[0]:q[0] + 12]).lower()
    ok = not re.search(r'\b(yes,? we (all )?agree|we all agree|they all agree|no, we do not agree)\b', nxt)
    return ok, f'12 entries after the question contain no agreement claim: {nxt[:90]}...'


def _r08(body, lower, markers, entries):
    """No session clock: zero EST, zero of six candidate boundary times."""
    pats = [r'\bEST\b', r'\b7:00\b', r'\b3:00\b', r'\b3:30\b', r'\b9:00\b', r'\b9:30\b', r'\b5:00\b']
    counts = {p: len(re.findall(p, body)) for p in pats}
    return sum(counts.values()) == 0, f'{counts}'


def _r09(body, lower, markers, entries):
    """A colour is attached to a period, and nicknames to a timeframe -- and never joined."""
    colour = [m for m, t in entries if re.search(r'yellow one is a five moving average', t, re.I)]
    nick = [m for m, t in entries if re.search(r'30 minute of the water', t, re.I)]
    joined = [m for m, t in entries
              if re.search(r'(water|male|mail|blueberry)\D{0,20}\b(5|13|50|200)\b', t, re.I)
              or re.search(r'\b(5|13|50|200)\b\D{0,20}(water|male|mail|blueberry)', t, re.I)]
    ok = bool(colour) and bool(nick) and not joined
    return ok, f'colour->period {colour}, nickname->timeframe {nick}, joined {joined}'


def _r10(body, lower, markers, entries):
    """The lesson's own base-rate objection precedes his location-filter answer."""
    obj = [i for i, (m, t) in enumerate(entries) if "m's and w's are everywhere" in t.lower()]
    ans = [i for i, (m, t) in enumerate(entries) if 'i like patterns in line with what' in t.lower()]
    ok = bool(obj and ans and obj[0] < ans[0])
    return ok, f'objection at {entries[obj[0]][0] if obj else None}, answer at {entries[ans[0]][0] if ans else None}'


def _r11(body, lower, markers, entries):
    """ANSWER NOT KNOWN IN ADVANCE. Does V07 use the phrase 'trap move' at all?
    Prediction: NO -- 'trap' appears as a verb and as 'trap candle', but A-002's compound
    term is a V01/V02 object. Recorded as a prediction; whatever it returns stands."""
    compound = re.findall(r'trap move', body, re.I)
    bare = re.findall(r'\btrap\w*', body, re.I)
    return len(compound) == 0, f'"trap move" x{len(compound)}; trap-family x{len(bare)}: {sorted(set(w.lower() for w in bare))}'


def _r12(body, lower, markers, entries):
    """ANSWER NOT KNOWN IN ADVANCE. Is 'straightaway' spoken, or only printed on the slide?
    Prediction: spoken at least once -- [00:03:48] is in the transcript. If it is ONLY
    printed, this fails and the printed-vs-spoken distinction needs restating."""
    hits = [m for m, t in entries if re.search(r'straightaway', t, re.I)]
    return len(hits) >= 1, f'spoken at {hits}'


def _r13(body, lower, markers, entries):
    """ANSWER NOT KNOWN IN ADVANCE. Is any currency pair named in the AUDIO?
    Prediction: yes, but only obliquely -- 'the Euro', 'the EU', 'the CAD', 'Euro Allsy'.
    Fails if a conventional pair symbol appears, which would change what
    V07_INTERPRETATION.md 5.5 can say about GBP/USD's absence."""
    sym = re.findall(r'\b(EURUSD|GBPUSD|AUDUSD|USDJPY|EURJPY|USDCAD|EUR/USD|GBP/USD)\b', body, re.I)
    oblique = sorted(set(w.lower() for w in re.findall(r'\bEuro\b|\bEU\b|\bCAD\b|\bAllsy\b|\bAussie\b', body)))
    return len(sym) == 0, f'conventional symbols x{len(sym)} {sorted(set(sym))}; oblique names {oblique}'


def _r14(body, lower, markers, entries):
    """ANSWER NOT KNOWN IN ADVANCE. Does 'second leg' outnumber the level vocabulary?
    Prediction: yes -- second leg is the lesson's real subject. If levels win, the
    interpretation notes over-weight the taxonomy relative to the level filter."""
    sl = len(re.findall(r'second leg', body, re.I))
    lv = len(re.findall(r'\blevel (one|two|three|1|2|3)\b', body, re.I))
    return sl > lv, f'second leg x{sl} vs level-N x{lv}'


REASONING = [
    ('R01', 'Who is speaking, and how do you know without the audio?',
     'Not Steve. Both "Steve" tokens are third-person, one of them queueing him as a questioner.', _r01),
    ('R02', 'What number does this lesson use as its exit, and how confident should you be?',
     '50 pips, at three or more independent markers plus one printed on a chart.', _r02),
    ('R03', 'Who is credited with the Hi-Lo method?',
     'Jim, named three or more times, always in the third person.', _r03),
    ('R04', 'Where in the lesson is the second-leg taxonomy, and is it contiguous?',
     'One contiguous stretch, from "different types of M\'s" to "I like those as well".', _r04),
    ('R05', 'Does he rename the homework before or after assigning it?',
     'Before. The rename is asserted first, then the assignment is given.', _r05),
    ('R06', 'At level one, what is the rule and what is the exception, in that order?',
     'Expect a single leg / A pattern; a second leg there is a gift. Rule first, exception second.', _r06),
    ('R07', 'A student asks whether all the DMR speakers agree. What is the answer?',
     'He does not give one. Nothing in the following twelve entries claims they agree or disagree.', _r07),
    ('R08', 'Does this lesson contain any session clock?',
     'No. EST and all six candidate boundary times are absent.', _r08),
    ('R09', 'How close does the lesson come to solving A-020?',
     'It attaches a colour to a period and nicknames to a timeframe, and never joins the two.', _r09),
    ('R10', 'Does the base-rate objection come before or after his answer to it?',
     'Before. He raises the problem, then answers it with a location filter.', _r10),
    ('R11', 'ANSWER NOT KNOWN IN ADVANCE — does V07 use the compound "trap move"?',
     'PREDICTED: no. Trap appears as a verb and as "trap candle"; the A-002 compound is a '
     'V01/V02 object.', _r11),
    ('R12', 'ANSWER NOT KNOWN IN ADVANCE — is "straightaway" spoken, or only printed?',
     'PREDICTED: spoken at least once.', _r12),
    ('R13', 'ANSWER NOT KNOWN IN ADVANCE — is any currency pair named conventionally in the audio?',
     'PREDICTED: no conventional symbol; only oblique names like "the Euro", "the CAD".', _r13),
    ('R14', 'ANSWER NOT KNOWN IN ADVANCE — does "second leg" outnumber the level vocabulary?',
     'PREDICTED: yes, second leg is the lesson\'s real subject.', _r14),
]


def main():
    raw = open(TRANSCRIPT).read()
    body = raw[raw.index('\n[00:00:00]'):]
    lower = re.sub(r'\s+', ' ', body.lower())
    markers = set(re.findall(r'^\[(\d\d:\d\d:\d\d)\]$', body, re.M))

    entries = []
    cur = None
    for line in body.split('\n'):
        s = line.strip()
        if re.fullmatch(r'\[\d\d:\d\d:\d\d\]', s):
            cur = s
            entries.append([cur, []])
        elif s and entries:
            entries[-1][1].append(s)
    entries = [(m, ' '.join(t)) for m, t in entries]

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
    print('=' * 78)
    print('REASONING BATTERY — relations and counts, not phrases')
    print('=' * 78)
    for rid, q, expected, fn in REASONING:
        ok, ev = fn(body, lower, markers, entries)
        fails += 0 if ok else 1
        print(f'{rid}  {"PASS" if ok else "FAIL"}')
        print(f'      Q : {q}')
        print(f'      A : {expected}')
        print(f'      evidence: {ev}')

    total = len(POSITIVE) + len(NEGATIVE) + len(REASONING)
    print()
    print(f'PROBES: {len(POSITIVE)} positive + {len(NEGATIVE)} negative + '
          f'{len(REASONING)} reasoning = {total}   FAILURES: {fails}')
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
