#!/usr/bin/env python3
"""V07 quotation verifier -- mechanically checks every quoted fragment in every V07 artifact
against the verbatim transcript body.

WHY THIS EXISTS. V07 R1 finding `M3` and V07 R2 finding `M1` are the same defect twice: a
quotation mark containing a word that is not in the source. Both rounds also produced a
CATEGORICAL claim -- "no other instance exists" -- earned by an ad-hoc sweep that was never
committed. `V07_REVIEW_R2.md` `N1` recorded that the sweep was not reproducible; `N2` recorded
that three sweeps of the same corpus returned 239 / 238 / 167 fragments -- a ~30% spread, and the
three surviving instances passed through the gap. This script replaces the ad-hoc sweep. It is
committed so a later round re-runs the IDENTICAL check instead of inventing a new one and getting
a fourth number.

WHAT IT DOES.

  1. Extracts the verbatim transcript body (everything after `# VERBATIM TRANSCRIPT`), dropping
     the bare `[HH:MM:SS]` marker lines so a quotation may legitimately span two markers.
  2. Extracts EVERY emphasised quotation -- `*"..."*`, `**"..."**`, `***"..."***`, straight or
     curly quotes -- from every V07 artifact. Quotations WRAPPED ACROSS A MARKDOWN LINE BREAK are
     captured: a pattern that stops at a newline is the candidate mechanism `N2` named for the
     missed instance at `V07_SOURCE_NOTES.md` Sec 9a, and that instance is line-wrapped.
  3. Normalises both sides -- lowercase, straighten quotes, collapse every non-alphanumeric run
     to a single space -- and asks whether the quotation is a substring of the transcript body.
  4. Splits on explicit elisions (`...`) and checks each segment independently.
  5. Strips bracketed editorial insertions (`[it's met]`) BEFORE matching, because square
     brackets are this project's declared convention for a word inserted rather than heard. That
     is precisely why bracketing is the repair R2 asked for: a bracketed reconstruction is no
     longer an assertion about the source, and this script treats it as one.

THE TWO TIERS, AND WHY THE SWEEP IS TIERED RATHER THAN FLAT.

  A flat "every quotation must be in the transcript" rule is unusable: these artifacts also quote
  printed slide text, the student's own prose, pre-registered predictions and other documents.
  A citation-windowed rule -- only check fragments with a nearby `[HH:MM:SS]` -- is what earlier
  sweeps used, and TWO of R2's three instances sat outside such a window. So both tiers run:

  TIER 1  CITED.  A `[HH:MM:SS]` appears in the quotation's own paragraph (its line, the line
          above, or the line below). The quotation is being asserted as spoken source. It MUST
          resolve to the transcript body. Anything else is a FLAG.

  TIER 2  UNCITED.  No marker in context, so the quotation may legitimately be of anything. It is
          NOT required to match. It is flagged only when it TRACKS a real transcript sentence for
          at least NEAR_MISS_MIN_WORDS consecutive words, at its head or its tail, and then
          diverges. That is exactly the defect class of R1 `M3` and R2 `M1`: a real sentence with
          one word swapped. Quotation of the student's own prose, of a printed slide or of a
          pre-registered prediction shares no such run with the transcript and does not fire.

  R2's instance (c) -- `04_SCREENSHOTS/V07/INDEX.md` item 6 -- is a TIER 2 catch, and is the
  reason tier 2 exists.

DISPOSITIONS. A non-matching quotation is not automatically a defect. Two classes are legitimate
and are separated mechanically or by explicit register:

  RETAINED   The quotation sits on a Markdown block-quote line (`>`). Superseded-text retention
             blocks re-quote defective renderings VERBATIM ON PURPOSE, because
             `REMEDIATION_PROTOCOL.md` Sec 2 forbids deleting them. These are the audit trail.
             Reported, never failing. This is the mechanical explanation for the raw-count
             inflation `V07_REVIEW_R2.md` Sec 4 measured (238 -> 252).

  ALLOWED    Listed in ALLOWLIST below WITH A REASON: printed slide/chart text (the transcript is
             audio only, and printed source is source), a quote from a DIFFERENT lesson at that
             lesson's marker, or an explicitly hypothesised ASR alternative. Each entry names its
             justification so a later round audits the excuses rather than inheriting them.

  FLAG       Everything else. Exit 1.

NOT IN SCOPE. `18_REVIEW/V07/*` is deliberately excluded. Review files quote ARTIFACT cells,
commit messages and each other by design; running an artifact-quotation rule over them produces
noise, not findings. The claim under test in `V07_MASTERY_REPORT.md` Sec H is about the V07
artifact set, which is what ARTIFACTS lists.

usage: python3 05_HOMEWORK/V07/scripts/verify_quotes.py [--verbose] [TRANSCRIPT]
exit 1 if any FLAG survives, so it can gate a commit.
"""
import os
import re
import sys

TRANSCRIPT = '02_TRANSCRIPTS/V07/V07_TRANSCRIPT.md'
BODY_HEADING = '# VERBATIM TRANSCRIPT'

# The seven V07 artifacts named in V07_MASTERY_REPORT.md Sec H's sweep claim.
ARTIFACTS = [
    '03_LESSON_NOTES/V07_SOURCE_NOTES.md',
    '03_LESSON_NOTES/V07_INTERPRETATION.md',
    '05_HOMEWORK/V07/V07_HOMEWORK.md',
    '07_MASTERY_REPORTS/V07_MASTERY_REPORT.md',
    '04_SCREENSHOTS/V07/INDEX.md',
    '06_MANUAL_BACKTEST/V07/BT_V07_0001.md',
    '06_MANUAL_BACKTEST/PRE_REGISTERED/PT-033_hi_lo_ceiling_and_the_untaught_gap.md',
]

# Quotations shorter than this many words after normalisation are not checked. A two-word
# fragment matches by accident too often for a hit to mean anything, and a two-word fragment that
# does not match is usually a term of art in quotes rather than a quotation.
MIN_WORDS = 3

# Tier 2 sensitivity. A quotation must track the transcript for at least this many consecutive
# words, at its head or its tail, before its divergence is treated as a misquote rather than as a
# quotation of something else.
NEAR_MISS_MIN_WORDS = 4

# Non-transcript quotations that are legitimate. Key: (artifact basename or '*', normalised
# fragment prefix). Value: why it is not a defect. Matching is by PREFIX on normalised text, so an
# entry cannot silently excuse a longer, differently-worded quotation.
ALLOWLIST = {
    # -- Printed slide and chart text. The transcript carries audio only; each of these is
    #    labelled PRINTED or names its frame at the point of use.
    ('*', 'best trade grabs mmfx breakout session'): 'PRINTED slide V07_00-00-10',
    ('*', 'but do they tell the whole story'): 'PRINTED slide V07_00-00-35',
    ('*', 'gotta get that m or w'): 'PRINTED slide V07_00-04-00',
    ('*', 'm or w'): 'PRINTED slide V07_00-04-00, settling a two-way ASR garble',
    ('*', 'like um homework i mean r d'): 'PRINTED slide V07_00-04-55',
    ('*', 'flashcards screenshots'): 'PRINTED slide V07_00-13-00',
    ('*', 'hi lo'): 'PRINTED slide V07_00-08-00',
    ('*', 'what is the requirement for good trade grabs'): 'PRINTED slide V07_00-12-00',
    ('*', 'setups what level am i at'): 'PRINTED slide V07_00-04-00, bullet deck',
    ('*', 'i can do something else like um homework'): 'PRINTED slide V07_00-04-55',
    ('*', 'signature trade setup'): 'PRINTED slide V07_00-04-55',
    ('*', 'do they matter'): 'PRINTED slide V07_00-06-00, one of the deck\'s four questions',
    ('*', 'do they help'): 'PRINTED slide V07_00-06-00, one of the deck\'s four questions',
    ('*', 'isn t that all that matters'):
        'PRINTED slide V07_00-09-00, one of the deck\'s four questions',
    ('*', 'is it really important'):
        'PRINTED slide V07_00-10-00, one of the deck\'s four questions',
    ('*', 'money management those pesky stoplosses'): 'PRINTED slide V07_00-10-00',
    ('*', 'couple it with a hi lo entry'): 'PRINTED slide V07_00-08-00',
    ('*', 'shark fin in tdi'): 'PRINTED annotation V07_00-18-25',
    ('*', 'enter after 2nd leg rr tracks'): 'PRINTED annotation V07_00-19-15',
    ('*', 'exit 50 pips'): 'PRINTED annotation V07_00-19-15',
    ('*', 'enter short pos'): 'PRINTED annotation V07_00-18-25',
    ('*', 'bias level 1 short'): 'PRINTED annotation V07_00-18-25',
    ('*', '1 st tp 52 pips'): 'PRINTED annotation V07_00-18-25',
    ('*', '2 nd tp 67 pips'): 'PRINTED annotation V07_00-18-25',
    ('*', 'mig trading station'): 'PRINTED platform title V07_00-00-10',
    ('*', 'go trader 4'): 'PRINTED platform title V07_00-19-15',
    ('*', 'happy trading to all'): 'PRINTED slide V07_00-21-35',
    # -- Quotes from a DIFFERENT lesson, carried at that lesson's marker and labelled as such.
    ('*', 'and so i have 12 pairs that i look at'): 'V04 quote at a V04 marker, labelled',
    ('*', 'just 12 pairs'): "V04's guest, quoted at V04 [00:30:22]/[00:38:19] and labelled V04",
    ('*', 'so i paired it down about six weeks ago to just 12 pairs'):
        'V04 quote at V04 [00:30:22], labelled V04 in the same sentence',
    # -- A quote from an EARLIER lesson's ambiguity record, not from V07 audio.
    ('*', 'm a1 a2'): "A-047's object, quoted from an earlier lesson and named as such",
    # -- Editorial bracketing INSIDE a word rather than around an inserted word. The source reads
    #    "Do all the DMS speaker agree on this?" at [00:29:49]-[00:29:52]; the artifact renders it
    #    "DM[R] speaker[s]", correcting the ASR inside the token. Stripping the brackets therefore
    #    leaves "DM", which is not the source token "DMS". Dispositioned as the bracket convention
    #    working as intended, NOT silently ignored: R2 did not raise it and this remediation does
    #    not widen its own scope, but it is recorded here so R3 can rule on whether intra-word
    #    bracketing should be spelled differently.
    ('*', 'do all the dm speaker agree on this'):
        'intra-word editorial bracket, DM[R]/speaker[s]; source reads "DMS speaker" -- see note',
    # -- Every word is in the spoken source and the string is verbatim in the printed source.
    ('*', 'tell the whole story'):
        'spoken at [00:00:32] ("do they tell us the whole story?") and PRINTED verbatim on'
        ' slide V07_00-00-35; an un-elided partial, not a substituted word',
    # -- The declared second-ASR-pass reading, marked as such at every point of use.
    ('*', 'i made it dotted in the 13 50 and the 200'):
        'declared second ASR pass (V07_TRANSCRIPT.md PROVENANCE criterion 2)',
    ('*', 'i made a dot it in the 13 50 and the 200'):
        'declared second ASR pass (V07_TRANSCRIPT.md PROVENANCE criterion 2)',
    # -- An explicitly hypothesised ASR alternative, offered as a candidate, not asserted.
    ('*', 'an m pattern'): 'hypothesised ASR alternative offered as a candidate (A-057)',
}

# `[^"“”]` rather than `.` so a quotation cannot run past its own closing mark and swallow the
# next one; `DOTALL` is unnecessary with a negated class, and a line-wrapped quotation is still
# captured because the class admits newlines.
QUOTE_RE = re.compile(r'(\*{1,3})["“]([^"“”]+?)["”]\1')
MARKER_LINE_RE = re.compile(r'^\[(\d{2}:\d{2}:\d{2})\]\s*$')
MARKER_RE = re.compile(r'\[\d{2}:\d{2}:\d{2}\]')
BRACKET_RE = re.compile(r'\[[^\]]*\]')
ELISION_RE = re.compile(r'…|\.\.\.')


def normalize(text):
    """Lowercase, straighten quotes, collapse every non-alphanumeric run to a single space."""
    text = text.replace('’', "'").replace('‘', "'")
    text = text.replace('“', '"').replace('”', '"')
    return re.sub(r'[^0-9a-zA-Z]+', ' ', text.lower()).strip()


def load_body(path):
    """Return (normalised body, marker count) for the verbatim transcript body."""
    with open(path, encoding='utf-8') as fh:
        lines = fh.read().splitlines()
    try:
        start = next(i for i, ln in enumerate(lines) if ln.strip() == BODY_HEADING) + 1
    except StopIteration:
        sys.exit('FATAL: %s has no %r heading' % (path, BODY_HEADING))
    spoken, markers = [], 0
    for ln in lines[start:]:
        if MARKER_LINE_RE.match(ln.strip()):
            markers += 1
            continue
        spoken.append(ln)
    return normalize(' '.join(spoken)), markers


def near_miss(body, q_words):
    """Longest run of the quotation's leading OR trailing words that IS in the transcript body.

    This is the shape of the defect, so it is what is tested for. A word-substitution misquote is
    a real sentence that tracks the source and then diverges: `"it turns red when it's met"`
    against `"It turns red when Beth."` shares a four-word head and then parts company. A
    quotation of the student's own prose, a printed slide or a prediction shares no such run.

    A similarity RATIO was tried first and rejected: `"it turns red when it's met"` and
    `"it turns red when Beth"` differ in length, so a same-length window comparison scores them
    below any threshold loose enough to be safe -- which is how R2's instance (c) survived an
    earlier sweep. Matched-run length has no such blind spot.

    Returns (run length in words, the matching run).
    """
    n = len(q_words)
    for k in range(n, NEAR_MISS_MIN_WORDS - 1, -1):
        for run in (q_words[:k], q_words[n - k:]):
            joined = ' '.join(run)
            if joined in body:
                return k, joined
    return 0, ''


def cited(text, offset):
    """True if an [HH:MM:SS] marker appears in the quotation's own context.

    The context is the line the quotation STARTS on, extended to the neighbouring lines only when
    neither line is a Markdown table row. Table rows are independent records -- extending across
    them makes every printed-slide row inherit its neighbour's marker, which is a false positive,
    not a catch. Wrapped prose is genuinely continuous, so it is extended: `V07_SOURCE_NOTES.md`
    Sec 9a carries its marker on the line the quotation opens on and wraps to the next.
    """
    lines = text.splitlines()
    pos, idx = 0, 0
    for i, ln in enumerate(lines):
        if pos + len(ln) + 1 > offset:
            idx = i
            break
        pos += len(ln) + 1
    here = lines[idx]
    window = [here]
    if not here.lstrip().startswith('|'):
        for j in (idx - 1, idx + 1):
            if 0 <= j < len(lines) and not lines[j].lstrip().startswith('|'):
                window.append(lines[j])
    return bool(MARKER_RE.search('\n'.join(window)))


def in_blockquote(text, offset):
    """True if the quotation starts on a Markdown block-quote line -- a retention block."""
    bol = text.rfind('\n', 0, offset) + 1
    return text[bol:bol + 8].lstrip().startswith('>')


def allow_reason(basename, norm):
    for (scope, prefix), reason in ALLOWLIST.items():
        if scope in ('*', basename) and norm.startswith(prefix):
            return reason
    return None


def check(body, body_words, path):
    """Yield (status, line, tier, detail, fragment) for every quotation in one artifact."""
    with open(path, encoding='utf-8') as fh:
        text = fh.read()
    basename = os.path.basename(path)
    for m in QUOTE_RE.finditer(text):
        line = text.count('\n', 0, m.start()) + 1
        tier = 'cited' if cited(text, m.start()) else 'uncited'
        # Bracketed editorial insertions are removed before matching -- that is what the brackets
        # declare. A quotation only asserts the words left outside them.
        stripped = BRACKET_RE.sub(' ', m.group(2))
        for seg in ELISION_RE.split(stripped):
            norm = normalize(seg)
            words = norm.split()
            if len(words) < MIN_WORDS:
                continue
            if norm in body:
                yield 'MATCH', line, tier, '', norm
                continue
            reason = allow_reason(basename, norm)
            if reason:
                yield 'ALLOWED', line, tier, reason, norm
            elif in_blockquote(text, m.start()):
                yield 'RETAINED', line, tier, 'block quote -- superseded-text retention', norm
            elif tier == 'cited':
                yield 'FLAG', line, tier, 'cited to a marker but not in the transcript', norm
            elif len(words) >= NEAR_MISS_MIN_WORDS:
                run, matched = near_miss(body, words)
                if run:
                    yield ('FLAG', line, tier,
                           'tracks the transcript for %d words -- "%s" -- then diverges'
                           % (run, matched), norm)
                else:
                    yield 'UNRELATED', line, tier, 'not a transcript sentence', norm
            else:
                yield 'UNRELATED', line, tier, 'not a transcript sentence', norm


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    verbose = '--verbose' in sys.argv[1:]
    transcript = args[0] if args else TRANSCRIPT

    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__)))))
    os.chdir(root)

    body, markers = load_body(transcript)
    body_words = body.split()
    print('TRANSCRIPT   %s' % transcript)
    print('             %d markers, %d normalised words of spoken body'
          % (markers, len(body_words)))
    print()

    tally = {'MATCH': 0, 'ALLOWED': 0, 'RETAINED': 0, 'UNRELATED': 0, 'FLAG': 0}
    flags = []
    for path in ARTIFACTS:
        if not os.path.exists(path):
            sys.exit('FATAL: missing artifact %s' % path)
        rows = list(check(body, body_words, path))
        print('%-72s %3d fragment%s' % (path, len(rows), '' if len(rows) == 1 else 's'))
        for status, line, tier, detail, frag in rows:
            tally[status] += 1
            if status == 'FLAG':
                flags.append((path, line, frag, detail))
                print('    FLAG      %s:%d [%s]' % (path, line, tier))
                print('              "%s"' % frag)
                print('              %s' % detail)
            elif status == 'ALLOWED':
                print('    allowed   line %-5d "%s"  (%s)' % (line, frag[:46], detail))
            elif status == 'RETAINED':
                print('    retained  line %-5d "%s"' % (line, frag[:46]))
            elif verbose:
                print('    %-9s line %-5d "%s"' % (status.lower(), line, frag[:46]))

    total = sum(tally.values())
    print()
    print('FRAGMENTS CHECKED      %d' % total)
    print('  matched transcript   %d' % tally['MATCH'])
    print('  allowed (see list)   %d' % tally['ALLOWED'])
    print('  retained (audit)     %d' % tally['RETAINED'])
    print('  uncited, unrelated   %d' % tally['UNRELATED'])
    print('  FLAGGED              %d' % tally['FLAG'])
    print()
    if flags:
        print('RESULT: FAIL -- %d quotation(s) assert words the source does not contain.'
              % len(flags))
        return 1
    print('RESULT: PASS -- every marker-cited quotation resolves to the transcript body, and no')
    print('        uncited quotation is a near miss of a transcript sentence. Bracketed')
    print('        insertions, printed source and retention blocks are dispositioned above.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
