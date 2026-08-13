#!/usr/bin/env python3
"""V08 comprehension probe — a machine-checkable test of whether this session's recall of the
lesson is real, rather than plausible-sounding reconstruction.

Four batteries. The last one is new in V08.

  POSITIVE   Claims written from memory of the lesson, WITHOUT the transcript open while
             drafting them, but AFTER V08_SOURCE_NOTES.md had been written. Each must be
             found in the transcript at or near a stated marker.

             SAME WEAKNESS V07 DISCLOSED, DISCLOSED AGAIN RATHER THAN GLOSSED: writing the
             notes first means this battery tests retention of this session's own work, not
             first-exposure recall. Reported for what it is.

  NEGATIVE   Claims that SOUND like they belong in this lesson and are NOT in it. Most are
             lifted VERBATIM from the quarantined NOTES.md / VISUAL_INDEX.md for this very
             lesson (Q-009) — exactly the material a shallow reader would absorb. Each must
             be ABSENT. A hit means this session imported a fabrication.

  REASONING  Claims about the lesson's STRUCTURE or ARITHMETIC that cannot be answered by
             recognising a phrase. Each is checked by a predicate over the transcript.

  VISUAL     NEW IN V08. Claims about what is PRINTED on a frame and what the audio does or
             does not say about the same thing. These test the one place V08's notes depend
             on a source the transcript cannot corroborate, and they are checked in the only
             way available without re-reading pixels: by asserting the AUDIO's side of the
             relation, which is falsifiable. A visual claim whose audio side fails is a claim
             this session got wrong about which evidence supports what.

The negative battery is more important than the positive one, and the reasoning battery is
more important than either: recall can be faked by fluency; correctly rejecting a plausible
falsehood cannot, and neither can a relation between two passages.

usage: python3 05_HOMEWORK/V08/scripts/comprehension_probe.py [TRANSCRIPT]
exit 1 if any probe fails, so it can gate a commit.
"""
import re
import sys

TRANSCRIPT = sys.argv[1] if len(sys.argv) > 1 else '02_TRANSCRIPTS/V08/V08_TRANSCRIPT.md'

# (id, claim as recalled, regex to find in the body, marker this session expects it near)
POSITIVE = [
    ('P01', 'He opens by promising a journey through how HE learned the method',
     r'a little journey in how i learned and traded the market maker', '00:00:00'),
    ('P02', 'He names the course author in the third person in the first minute',
     r'steve asked me to do something for 90 minutes', '00:00:32'),
    ('P03', 'He plans THREE sections plus the DMR, about two hours',
     r'come back and do the third section and the dmr', '00:00:26'),
    ('P04', 'Section 3 is the defined-risk lesson — and it is not in this file',
     r'section three is how to not get killed', '00:05:55'),
    ('P05', 'The model has four distinct levels, worked from the ideal outward',
     r'i see it as four distinct levels', '00:06:21'),
    ('P06', 'The innermost ring is steady equity growth',
     r'the inner circle of this method is steady equity growth', '00:06:44'),
    ('P07', 'The validation exercise: two hours a week after Friday\'s close, ten or more pairs',
     r'two hours a week after the market closes on friday', '00:11:21'),
    ('P08', 'The gallery is the week of March 19th 2012',
     r'weather report, week of march 19th, 2012', '00:15:24'),
    ('P09', 'The count is 29 setups',
     r"that's 29 set ups", '00:16:22'),
    ('P10', 'The stop hunt box has a stated size of 25 pips',
     r'this stop hunt box is 25 pips', '00:19:31'),
    ('P11', 'The lesson\'s pivot: he can see M/W after they form, not before',
     r"clearly after they.*form, but i can't see him before they form", '00:27:50'),
    ('P12', 'The technique is to chop the chart back to the hard right edge',
     r'we take an ideal setup and then we chop it back', '00:28:00'),
    ('P13', 'It took him three months to see M/W even AFTER they formed',
     r'three months into the market maker effects training', '00:28:19'),
    ('P14', 'Eight hours to build ten movies, and his trading instantly improved',
     r'ten movies of n\'s and w\'s from the previous week', '00:31:56'),
    ('P15', 'The worked example is CAD/JPY, M15, Monday March 19th 2012, 1:30 AM EDT',
     r'monday, march 19th 2012, 1\.30 am eastern daylight time', '00:33:30'),
    ('P16', 'The fast move is false; the slow and steady move is correct',
     r'the fast move is false', '00:36:15'),
    ('P17', 'He calls the confirmation requirement a MYTH',
     r'the big trading myth that one needs confirmation', '00:36:58'),
    ('P18', 'and states the basic-training rule he is contradicting',
     r'in our basic training, we do say that you want to have a confirmation candle', '00:37:07'),
    ('P19', 'Entering at the extreme is called the SAFEST place to enter',
     r"it's actually the safest place to enter trades", '00:37:27'),
    ('P20', 'The drill is to be practised on DEMO',
     r'we do this drill on demo', '00:38:55'),
    ('P21', 'The crown-jewel claim: tighter stops, risk-reward three to one or greater',
     r'risk we reward to three to one or greater', '00:39:58'),
    ('P22', 'He draws a physical line on a previous trap area',
     r'physically draw a line that corresponds to that trap area', '00:40:34'),
    ('P23', 'The lesson ends on an unanswered question about the innermost area',
     r'what could possibly be left inside this area here', '00:42:58'),
]

# Claims that are NOT in V08. Most are lifted verbatim from the quarantined files (Q-009).
NEGATIVE = [
    ('N01', 'QUARANTINED NOTES.md: the 5/13 EMA cross confirms on the M15 close', r'5/13'),
    ('N02', 'QUARANTINED NOTES.md: EMAs nicknamed Mustard / Water / Mayo / Blueberry / Raspberry',
     r'\bmustard\b'),
    ('N03', 'QUARANTINED NOTES.md: 200 EMA is "Blueberry"', r'\bblueberry\b'),
    ('N04', 'QUARANTINED NOTES.md: 800 EMA is "Raspberry"', r'\braspberry\b'),
    ('N05', 'QUARANTINED NOTES.md: TDI green line crossing red signal line', r'\btdi\b'),
    ('N06', 'QUARANTINED NOTES.md: Shark Fin confirmation outside the volatility bands',
     r'shark fin'),
    ('N07', 'QUARANTINED NOTES.md: Peak Formation High / Low (PFH / PFL)', r'peak formation'),
    ('N08', 'QUARANTINED NOTES.md: Asian session 7:00 PM - 3:00 AM EST', r'7:00'),
    ('N09', 'QUARANTINED NOTES.md: London session 3:30 AM - 9:00 AM EST', r'3:30'),
    ('N10', 'QUARANTINED NOTES.md: New York session 9:30 AM - 5:00 PM EST', r'9:30'),
    ('N11', 'QUARANTINED NOTES.md: stop loss 10-15 pips past the High/Low of Day',
     r'10\s*(?:-|to)\s*15'),
    ('N12', 'QUARANTINED VISUAL_INDEX.md: Morning Star / Evening Star anatomy',
     r'(?:morning|evening) star'),
    ('N13', 'QUARANTINED VISUAL_INDEX.md: multi-timeframe confluence H4/H1/M15',
     r'confluence'),
    ('N14', 'QUARANTINED VISUAL_INDEX.md: TDI divergence and momentum hooks', r'divergence'),
    ('N15', 'QUARANTINED VISUAL_INDEX.md: high-volume pin bars', r'pin bar'),
    ('N16', 'PLAUSIBLE BUT ABSENT: a stated stop-loss distance in pips',
     r'stop (?:loss|is) \d+ pips'),
    ('N17', 'PLAUSIBLE BUT ABSENT: any mention of the ATR', r'\batr\b'),
    ('N18', 'PLAUSIBLE BUT ABSENT: a named candlestick pattern (doji / hammer / engulfing)',
     r'\b(?:doji|hammer|engulfing)\b'),
    ('N19', 'PLAUSIBLE BUT ABSENT: risk expressed as a percentage of the account per trade',
     r'\d+\s*%\s*(?:risk|per trade|of your account)'),
    ('N20', 'IMPORTED FROM V07, NOT IN V08: "shark fin in TDI"', r'shark'),
]

# Predicates over the transcript. Each returns (ok, detail).
def r_count_arithmetic(body):
    """R01 — the day x session tally the lesson reads out actually sums to its own headline 29.

    THIS PROBE FAILED ON ITS FIRST WRITING AND THE FAILURE IS RECORDED IN V08_HOMEWORK.md.
    The first version required each figure to sit near the tokens "set ups" or "session", and
    summed to 27. It was the PROBE that was wrong, not the transcript: two of the ten figures
    are stated in a different grammatical form -- "On Tuesday we had one AT LONDON." and "We
    had one AT NEW YORK." -- with neither token. A mechanical count over this transcript that
    keys on the lesson's usual phrasing silently drops them.

    The rewrite below keys on the VENUE instead, which every one of the ten figures names.
    """
    nums = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
            'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    seg = body[body.index('so we had two m&w set ups'):body.index("that's 29 set ups")]
    toks = list(re.finditer(r'\b(one|two|three|four|five|six|seven|eight|nine)\b', seg))
    total, parts = 0, []
    for k, m in enumerate(toks):
        tail = seg[m.end():toks[k + 1].start()] if k + 1 < len(toks) else seg[m.end():]
        venue = 'london' if 'london' in tail else ('new york' if 'new york' in tail else None)
        if venue:
            total += nums[m.group(1)]
            parts.append(f'{m.group(1)}@{venue}')
    return total == 29, f'day x session figures sum to {total}; headline says 29; {len(parts)} figures: {parts}'


def r_no_ema(body):
    """R02 — the food-nicknamed MA scheme is USED but never EXPANDED: 'EMA' never occurs."""
    ema = len(re.findall(r'\bema\b', body))
    mayo = len(re.findall(r'\bmayo\b', body))
    mail = len(re.findall(r'\bmail\b|\bmale\b', body))
    water = len(re.findall(r'\bwater\b', body))
    return (ema == 0 and (mayo + mail + water) >= 5,
            f'EMA={ema} (must be 0); mayo={mayo} mail/male={mail} water={water}, sum must be >=5')


def r_setups_not_trades(body):
    """R03 — C-007: the count is announced as SET UPS and closed as TRADES."""
    a = "that's 29 set ups" in body
    b = bool(re.search(r'29th steve marr market maker fx trades', body))
    return a and b, f'announced-as-setups={a}; closed-as-trades={b}'


def r_faith_before_science(body):
    """R04 — C-008: 'go off my faith here' occurs BEFORE 'big scientific reason'."""
    i = body.find('go off my faith here')
    j = body.find('big scientific reason')
    return (i != -1 and j != -1 and i < j,
            f'faith at char {i}, scientific at char {j}; faith must come first')


def r_myth_and_rule(body):
    """R05 — C-009: he states the basic-training rule AND calls the requirement a myth."""
    rule = 'in our basic training, we do say that you want to have a confirmation candle' in body
    myth = 'the big trading myth that one needs confirmation' in body
    demo = 'we do this drill on demo' in body
    return rule and myth and demo, f'rule={rule} myth={myth} staging-rule-on-demo={demo}'


def r_no_section_three(body):
    """R06 — section 3 is announced twice and its content never arrives."""
    announced = len(re.findall(r'how to not get killed', body))
    blowup = 'never again blow up an account' in body
    return (announced >= 2 and blowup,
            f'"how to not get killed" occurs {announced}x (need >=2); blow-up-an-account={blowup}')


def r_tolerance_absent_from_audio(body):
    """R07 — the 10-pip tolerance is NOT recoverable from the audio; the ASR garbles it."""
    garbled = 'intent pips' in body
    clean = bool(re.search(r'within (?:10|ten) pips', body))
    return garbled and not clean, f'ASR garble present={garbled}; clean phrasing present={clean} (must be False)'


def r_hilo_cue_is_speed_only(body):
    """R08 — the ONLY forward-looking cue offered for the extreme is speed, and it is undefined."""
    cue = "move this fast down here really fast, that's your cue" in body
    numeric = bool(re.search(r'(?:fast|slow)(?:er)?\s+(?:than\s+)?\d', body))
    return cue and not numeric, f'speed-cue={cue}; any numeric speed criterion={numeric} (must be False)'


def r_only_one_gbpusd(body):
    """R09 — GBP/USD, the project's own instrument (D-007), appears in the gallery exactly once."""
    n = len(re.findall(r'pound dollar', body))
    return n == 1, f'"pound dollar" occurs {n}x; expected exactly 1'


def r_two_hour_is_a_hold_not_a_deadline(body):
    """R10 — the two-hour mark is a HOLD rule, not an exit deadline. PT-034 relies on this."""
    m = re.search(r'past our two-hour mark where we can say we can (\w+) this trade', body)
    return (m is not None and m.group(1) == 'hold',
            f'verb after the two-hour mark = {m.group(1) if m else None!r}; must be "hold"')


REASONING = [
    ('R01', 'The day x session tally sums to the headline 29', r_count_arithmetic),
    ('R02', 'MA nicknames are used but "EMA" is never said — A-020/A-064 non-joining', r_no_ema),
    ('R03', 'C-007: announced as SET UPS, closed as TRADES', r_setups_not_trades),
    ('R04', 'C-008: "go off my faith" precedes "big scientific reason"', r_faith_before_science),
    ('R05', 'C-009: the rule, the myth, and the demo staging rule are all three present',
     r_myth_and_rule),
    ('R06', 'Section 3 is announced twice and never delivered', r_no_section_three),
    ('R07', 'The 10-pip tolerance is NOT in the audio — the ASR garbles it as "intent pips"',
     r_tolerance_absent_from_audio),
    ('R08', 'The only forward cue for the extreme is speed, and it carries no number',
     r_hilo_cue_is_speed_only),
    ('R09', 'GBP/USD appears in the 29-chart gallery exactly once', r_only_one_gbpusd),
    ('R10', 'The two-hour mark is a HOLD rule, not a deadline', r_two_hour_is_a_hold_not_a_deadline),
]

# VISUAL battery: each asserts the AUDIO side of a claim this session made about a frame.
# The frame itself cannot be checked here; the audio side can, and it is the falsifiable half.
VISUAL = [
    ('V01', 'Frame 00-05-40 prints "within 10 pips of HOD/LOD" — the AUDIO must NOT contain it',
     lambda b: (not re.search(r'\bhod\b|\blod\b|high of day.{0,20}low of day', b),
                'HOD/LOD initialisms in audio: must be absent')),
    ('V02', 'Frame 00-08-55 prints "FX scam" — the AUDIO must have the ASR\'s "scan"',
     lambda b: ('another fx scan' in b, '"another fx scan" present in audio')),
    ('V03', 'Frame 00-13-55 prints "Prussion" — the AUDIO must have "Depression-based"',
     lambda b: ('depression-based origins' in b, '"depression-based origins" present in audio')),
    ('V04', 'Frames show a TDI panel throughout — the AUDIO must never mention TDI',
     lambda b: (len(re.findall(r'\btdi\b', b)) == 0, 'TDI occurrences in audio: must be 0')),
    ('V05', 'Frame 00-17-00 prints "29 SETUPS" — the AUDIO must say "set ups" at the headline',
     lambda b: ("that's 29 set ups" in b, 'audio headline uses "set ups"')),
]


def main():
    raw = open(TRANSCRIPT, encoding='utf-8').read()
    body = raw[raw.rindex('\n# VERBATIM TRANSCRIPT'):]
    body = re.sub(r'\[\d\d:\d\d:\d\d\]', ' ', body)
    body = re.sub(r'\s+', ' ', body).lower()

    fails = []
    print('=' * 78)
    print('V08 COMPREHENSION PROBE')
    print('=' * 78)
    print(f'transcript: {TRANSCRIPT}   body words: {len(body.split())}')
    print()

    print(f'--- POSITIVE ({len(POSITIVE)}) — each MUST be found ---')
    for pid, claim, rx, marker in POSITIVE:
        ok = bool(re.search(rx, body))
        print(f'  {pid} {"PASS" if ok else "FAIL"}  ~[{marker}]  {claim}')
        if not ok:
            fails.append((pid, claim))
    print()

    print(f'--- NEGATIVE ({len(NEGATIVE)}) — each MUST be ABSENT ---')
    for nid, claim, rx in NEGATIVE:
        hits = len(re.findall(rx, body))
        ok = hits == 0
        print(f'  {nid} {"PASS" if ok else "FAIL"}  ({hits} hits)  {claim}')
        if not ok:
            fails.append((nid, claim))
    print()

    print(f'--- REASONING ({len(REASONING)}) — predicates, not phrase matches ---')
    for rid, claim, fn in REASONING:
        try:
            ok, detail = fn(body)
        except Exception as e:                       # a probe that cannot run is a FAIL
            ok, detail = False, f'probe raised {type(e).__name__}: {e}'
        print(f'  {rid} {"PASS" if ok else "FAIL"}  {claim}')
        print(f'        {detail}')
        if not ok:
            fails.append((rid, claim))
    print()

    print(f'--- VISUAL ({len(VISUAL)}) — the AUDIO side of a frame claim ---')
    for vid, claim, fn in VISUAL:
        try:
            ok, detail = fn(body)
        except Exception as e:
            ok, detail = False, f'probe raised {type(e).__name__}: {e}'
        print(f'  {vid} {"PASS" if ok else "FAIL"}  {claim}')
        print(f'        {detail}')
        if not ok:
            fails.append((vid, claim))
    print()

    total = len(POSITIVE) + len(NEGATIVE) + len(REASONING) + len(VISUAL)
    print('=' * 78)
    print(f'{total - len(fails)}/{total} passed')
    if fails:
        print(f'FAILURES ({len(fails)}):')
        for i, c in fails:
            print(f'  {i}  {c}')
        return 1
    print('ALL PROBES PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main())
