#!/usr/bin/env python3
"""Quotation verifier -- mechanically checks every quoted fragment in every artifact of a given
lesson against that lesson's verbatim transcript body.

GENERALISED AT V09 R2 (open item 81). This script was written at the V07 R2/R3 remediation and
was V07-specific: its `TRANSCRIPT` constant, its `ARTIFACTS` list and its printed-slide allowlist
all named V07. `V09_REVIEW_R1.md` `M1` required it to be generalised and run over V09;
`V09_REVIEW_R2.md` item 81 recorded that the generalisation and the run never happened, and that
a FIFTH instance of the defect class survived at `V09_SOURCE_NOTES.md` line 410 as a result. It
now takes a lesson identifier.

  usage: python3 05_HOMEWORK/V07/scripts/verify_quotes.py LESSON [--verbose] [--dump-allowed]
                                                                 [--transcript PATH]
  e.g.:  python3 05_HOMEWORK/V07/scripts/verify_quotes.py V09
         python3 05_HOMEWORK/V07/scripts/verify_quotes.py V07 --verbose

  exit 1 if any FLAG survives, so it can gate a commit.

WHY THE FILE STAYS AT `05_HOMEWORK/V07/scripts/`, THOUGH IT IS NO LONGER V07-SPECIFIC. Six
committed documents already cited it at this path before this edit -- `LOG.md`,
`18_REVIEW/REVIEW_INDEX.md`, `V07_MASTERY_REPORT.md`, `V07_REVIEW_R3.md`, `V09_REVIEW_R1.md` and
`V09_REVIEW_R2.md` -- and three of those are review files that
`REMEDIATION_PROTOCOL.md` §6 forbids editing after they are written. Moving it would convert
every one of those into a dangling pointer -- which is precisely the `E11` defect class this same
round is charging at item 82. The path is therefore historical, not descriptive, and this
paragraph is the disclosure. A later round that is willing to accept the stale citations may move
it to `scripts/`.

WHY THIS EXISTS. V07 R1 finding `M3` and V07 R2 finding `M1` are the same defect twice: a
quotation mark containing a word that is not in the source. Both rounds also produced a
CATEGORICAL claim -- "no other instance exists" -- earned by an ad-hoc sweep that was never
committed. `V07_REVIEW_R2.md` `N1` recorded that the sweep was not reproducible; `N2` recorded
that three sweeps of the same corpus returned 239 / 238 / 167 fragments -- a ~30% spread, and the
three surviving instances passed through the gap. This script replaces the ad-hoc sweep. It is
committed so a later round re-runs the IDENTICAL check instead of inventing a new one and getting
a fourth number. **V09 R2 item 81 is the cost of not running it: the four sites a human was
pointed at were repaired by hand and the un-enumerated fifth survived.**

WHAT IT DOES.

  1. Extracts the verbatim transcript body (everything after `# VERBATIM TRANSCRIPT`), dropping
     the bare `[HH:MM:SS]` marker lines so a quotation may legitimately span two markers.
  2. Extracts EVERY emphasised quotation -- `*"..."*`, `**"..."**`, `***"..."***`, straight or
     curly quotes -- from every artifact of the named lesson. Quotations WRAPPED ACROSS A MARKDOWN
     LINE BREAK are captured: a pattern that stops at a newline is the candidate mechanism `N2`
     named for the missed instance at `V07_SOURCE_NOTES.md` Sec 9a, and that instance is
     line-wrapped.
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

  ALLOWED    Listed in the lesson's ALLOWLIST WITH A REASON: printed slide/chart text (the
             transcript is audio only, and printed source is source), a quote from a DIFFERENT
             lesson at that lesson's marker, or an explicitly hypothesised ASR alternative. Each
             entry names its justification so a later round audits the excuses rather than
             inheriting them.

  FLAG       Everything else. Exit 1.

NOT IN SCOPE. `18_REVIEW/**` is deliberately excluded. Review files quote ARTIFACT cells, commit
messages and each other by design; running an artifact-quotation rule over them produces noise,
not findings. The claim under test is about the LESSON's artifact set, which is what ARTIFACTS
lists.

THE THREE PRECISION BOUNDS `V07_REVIEW_R3.md` Sec 4 RECOMMENDED FIXING "WHEN THE FILE IS NEXT
TOUCHED". This is that touch. Two are adopted and one is deliberately refused, with reasons:

  ADOPTED  Allowlist matching is now anchored to the FULL normalised fragment (equality), not to
           a prefix. Under the old prefix rule an entry could silently excuse a longer,
           differently-worded quotation -- R3 found this by mutation testing, and found the
           docstring claiming the opposite. Every V07 entry that was genuinely covering several
           lengths now appears as several explicit entries, so the excuses are enumerated rather
           than inferred. The V07 sweep still extracts **338** fragments and still FLAGS **0**.
           Three fragments that the prefix rule had been excusing silently now had to be written
           out with their own reasons -- the closing-synopsis slide, the full 00-04-00 bullet
           deck, and the two-sentence DM[R] quotation -- and six that were being excused for no
           reason at all fell through to `uncited, unrelated`, where they belong. The allowed
           count therefore moves 64 -> 58 and unrelated 27 -> 33, which is the hole closing.

  ADOPTED  The docstring claim about prefix matching is corrected -- it is the sentence above.

  REFUSED  R3 recommended ordering `in_blockquote()` AFTER the cited-FLAG test, because a new
           defect on a `>` line is otherwise masked. **Refused, because it would be wrong here.**
           `REMEDIATION_PROTOCOL.md` Sec 2 retention blocks re-quote the defective rendering on a
           `>` line AND carry the marker, so the reorder makes every correctly-retained
           superseded quotation a FLAG -- V09's remediation alone would produce several. What is
           done instead addresses R3's ACTUAL concern, which was masking rather than ordering:
           every RETAINED fragment now REPORTS its near-miss run against the transcript, so a
           retention block that tracks a real sentence is visible in the output and can be
           hand-ruled, exactly as R3 hand-ruled them. Mechanised visibility, not a mechanised
           verdict.
"""
import os
import re
import sys

BODY_HEADING = '# VERBATIM TRANSCRIPT'

# Per-lesson artifact sets. Listed explicitly rather than globbed: the claim under test in each
# lesson's mastery report is about a NAMED set of artifacts, and a glob would silently change what
# the claim covers when a file is added.
ARTIFACTS = {
    # The seven V07 artifacts named in V07_MASTERY_REPORT.md Sec H's sweep claim.
    'V07': [
        '03_LESSON_NOTES/V07_SOURCE_NOTES.md',
        '03_LESSON_NOTES/V07_INTERPRETATION.md',
        '05_HOMEWORK/V07/V07_HOMEWORK.md',
        '07_MASTERY_REPORTS/V07_MASTERY_REPORT.md',
        '04_SCREENSHOTS/V07/INDEX.md',
        '06_MANUAL_BACKTEST/V07/BT_V07_0001.md',
        '06_MANUAL_BACKTEST/PRE_REGISTERED/PT-033_hi_lo_ceiling_and_the_untaught_gap.md',
    ],
    # The seven V09 artifacts, in the same order and on the same principle. This is the set
    # `V09_REVIEW_R1.md` M1 and `V09_REVIEW_R2.md` item 81 both call "the seven V09 artifacts".
    'V09': [
        '03_LESSON_NOTES/V09_SOURCE_NOTES.md',
        '03_LESSON_NOTES/V09_INTERPRETATION.md',
        '05_HOMEWORK/V09/V09_HOMEWORK.md',
        '07_MASTERY_REPORTS/V09_MASTERY_REPORT.md',
        '04_SCREENSHOTS/V09/INDEX.md',
        '06_MANUAL_BACKTEST/V09/BT_V09_0001.md',
        '06_MANUAL_BACKTEST/PRE_REGISTERED/'
        'PT-035_highly_unlikely_to_lose_three_or_four_in_a_row.md',
    ],
}

# Quotations shorter than this many words after normalisation are not checked. A two-word
# fragment matches by accident too often for a hit to mean anything, and a two-word fragment that
# does not match is usually a term of art in quotes rather than a quotation.
MIN_WORDS = 3

# Tier 2 sensitivity. A quotation must track the transcript for at least this many consecutive
# words, at its head or its tail, before its divergence is treated as a misquote rather than as a
# quotation of something else.
NEAR_MISS_MIN_WORDS = 4

# Non-transcript quotations that are legitimate, per lesson. Key: (artifact basename or '*',
# FULL normalised fragment). Value: why it is not a defect.
#
# Matching is by EQUALITY on the full normalised fragment, changed from prefix matching at V09 R2
# per `V07_REVIEW_R3.md` Sec 4. Under the old rule an allowlist entry could silently excuse a
# longer, differently-worded quotation that merely began the same way. It cannot now: a fragment
# is excused only if it is character-for-character the fragment somebody wrote a reason for.
ALLOWLIST = {
    'V07': {
        # -- Printed slide and chart text. The transcript carries audio only; each of these is
        #    labelled PRINTED or names its frame at the point of use.
        ('*', 'best trade grabs mmfx breakout session 03 26 2'): 'PRINTED slide V07_00-00-10',
        ('*', 'but do they tell the whole story'): 'PRINTED slide V07_00-00-35',
        ('*', 'gotta get that m or w'): 'PRINTED slide V07_00-04-00',
        ('*', 'm or w'): 'PRINTED slide V07_00-04-00, settling a two-way ASR garble',
        ('*', 'like um homework i mean r d'): 'PRINTED slide V07_00-04-55',
        ('*', 'flashcards screenshots'): 'PRINTED slide V07_00-13-00',
        ('*', 'hi lo'): 'PRINTED slide V07_00-08-00',
        ('*', 'hi lo can this be all i need'): 'PRINTED slide V07_00-08-00',
        ('*', 'what is the requirement for good trade grabs pips'): 'PRINTED slide V07_00-12-00',
        ('*', 'setups what level am i at gotta get that m or w'):
            'PRINTED slide V07_00-04-00, bullet deck',
        # The full bullet deck, verbatim from 04_SCREENSHOTS/V07/INDEX.md row 6. Under the old
        # PREFIX rule this was silently excused by the shorter entry above -- the hole V07 R3
        # Sec 4 found by mutation testing. It is now enumerated in its own right.
        ('*', 'setups what level am i at gotta get that m or w straightaways or bust entries'
              ' it s all about the pattern if i know the pattern do i need levels'):
            'PRINTED slide V07_00-04-00, the full bullet deck (INDEX.md row 6)',
        ('*', 'i can do something else like um homework i mean r d'):
            'PRINTED slide V07_00-04-55',
        ('*', 'signature trade setup'): 'PRINTED slide V07_00-04-55',
        ('*', 'do they matter'): 'PRINTED slide V07_00-06-00, one of the deck\'s four questions',
        ('*', 'do they help'): 'PRINTED slide V07_00-06-00, one of the deck\'s four questions',
        ('*', 'isn t that all that matters'):
            'PRINTED slide V07_00-09-00, one of the deck\'s four questions',
        ('*', 'is it really important'):
            'PRINTED slide V07_00-10-00, one of the deck\'s four questions',
        ('*', 'money management those pesky stoplosses is it really important'):
            'PRINTED slide V07_00-10-00',
        ('*', 'couple it with a hi lo entry for smaller risk'): 'PRINTED slide V07_00-08-00',
        ('*', 'couple it with a hi lo entry for smaller risk and maximum gain'):
            'PRINTED closing synopsis slide, quoted in full at V07_INTERPRETATION.md Sec 2.4',
        ('*', 'shark fin in tdi'): 'PRINTED annotation V07_00-18-25',
        ('*', 'enter after 2nd leg rr tracks'): 'PRINTED annotation V07_00-19-15',
        ('*', 'exit 50 pips'): 'PRINTED annotation V07_00-19-15',
        ('*', 'exit 50 pips 8 57 gain'): 'PRINTED annotation V07_00-19-15',
        ('*', 'enter short pos 1'): 'PRINTED annotation V07_00-18-25',
        ('*', 'enter short pos 2'): 'PRINTED annotation V07_00-18-25',
        ('*', 'bias level 1 short'): 'PRINTED annotation V07_00-18-25',
        ('*', '1 st tp 52 pips'): 'PRINTED annotation V07_00-18-25',
        ('*', '2 nd tp 67 pips'): 'PRINTED annotation V07_00-18-25',
        ('*', 'mig trading station'): 'PRINTED platform title V07_00-00-10',
        ('*', 'go trader 4'): 'PRINTED platform title V07_00-19-15',
        ('*', 'go trader 4 2001 2011 metaquotes software corp'):
            'PRINTED platform title V07_00-19-15',
        ('*', 'happy trading to all i look forward to posting'): 'PRINTED slide V07_00-21-35',
        # -- Quotes from a DIFFERENT lesson, carried at that lesson's marker and labelled as such.
        ('*', 'and so i have 12 pairs that i look at'): 'V04 quote at a V04 marker, labelled',
        ('*', 'just 12 pairs'):
            "V04's guest, quoted at V04 [00:30:22]/[00:38:19] and labelled V04",
        ('*', 'so i paired it down about six weeks ago to just 12 pairs'):
            'V04 quote at V04 [00:30:22], labelled V04 in the same sentence',
        # -- A quote from an EARLIER lesson's ambiguity record, not from V07 audio.
        ('*', 'm a1 a2'): "A-047's object, quoted from an earlier lesson and named as such",
        # -- Editorial bracketing INSIDE a word rather than around an inserted word. The source
        #    reads "Do all the DMS speaker agree on this?" at [00:29:49]-[00:29:52]; the artifact
        #    renders it "DM[R] speaker[s]", correcting the ASR inside the token. Stripping the
        #    brackets therefore leaves "DM", which is not the source token "DMS".
        #    RULED AT V07 R3 `N2`: this is NOT a defect and must not be corrected -- the brackets
        #    are the visible signal whose absence is what R2 charged, intra-word bracketing is an
        #    established convention beyond V07, and the literal `DMS` is recorded in
        #    V07_TRANSCRIPT.md's own ASR-garble inventory.
        ('*', 'do all the dm speaker agree on this if so how'):
            'intra-word editorial bracket, DM[R]/speaker[s]; source reads "DMS speaker"'
            ' -- RULED NOT A DEFECT at V07 R3 N2',
        ('*', 'do all the dm speaker agree on this if so how do i see it'):
            'same intra-word bracket, spanning [00:29:49]-[00:29:52]; both sentences are'
            ' verbatim in the transcript -- RULED NOT A DEFECT at V07 R3 N2',
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
    },
    # V09's allowlist is built from the first run of this script against V09 at V09 R2 (open item
    # 81). Every entry was hand-checked against the frame table in `04_SCREENSHOTS/V09/INDEX.md`
    # or against the document it names before being written here. The run that produced it FLAGGED
    # 46 fragments; twelve were genuine defects and were fixed in the artifacts, including the
    # `experience shows me` instance item 81 named and a SIXTH `E01` instance at INDEX.md row 26
    # that no human had enumerated. The rest are these.
    'V09': {
        # -- PRINTED slide text. V09's slides carry long paragraphs and the presenter paraphrases
        #    rather than reads them, so almost none of this appears in the audio. Each frame is
        #    named by its burned-in player timecode, per the convention item 76 established.
        ('*', 'risk in forex is defined as what of our account balance would be lost if our'
              ' trade went to stop loss'):
            'PRINTED slide, frame burned 01:15. The AUDIO at [00:01:17]-[00:01:21] says "your"'
            ' for "our" twice, which is why this is tagged PRINTED and not AUDIO',
        ('*', 'one of the great benefits of trading with defined risk is that we are emotionally'
              ' prepared if a stop loss happens there is no unknown drop in our account balance'):
            'PRINTED slide, frame burned 02:05',
        ('*', 'what makes the risk defined is the lot size we choose to put on we multiply our'
              ' account balance by 02 and divide our stop loss in pips into that number that'
              ' will determine the lot size'):
            'PRINTED slide, frame burned 02:05 -- the corpus\'s first position-sizing rule',
        ('*', 'mastering hod lod entries'): 'PRINTED slide, frame burned 03:45; the audio garbles'
                                           ' HOD/LOD to "high low-day" (V09_REVIEW_R1.md M1)',
        ('*', 'mastering hod lod entries can allow one to trade with a pure 3 1 risk to reward'
              ' ratio meaning one can lose three times in a row and with one winner they can'
              ' negate the loss'):
            'PRINTED slide, frame burned 03:45, quoted in full',
        ('*', 'until one develops the hod lod skill'):
            'PRINTED slide, frame burned 04:40; same HOD/LOD garble as above',
        ('*', 'until one develops the hod lod skill they can use a 2 1 risk to reward ratio'
              ' example 25 pip s l 50 pip t p in this case two stop outs can be negated with'
              ' one win'):
            'PRINTED slide, frame burned 04:40, quoted in full',
        ('*', 'the idea is that we use a consistent lot size for the win loss cycle after we'
              ' take a stop out we come back with the same lot size until we negate the loss if'
              ' our balance is only set back 2 at each loss we are sure to avoid margin issues'
              ' for the 3rd or 4th trade which will be the one which negates the loss'):
            'PRINTED slide, frame burned 05:25',
        ('*', 'if one takes four stop losses in a row it s time to re calculate lot size as the'
              ' account balance has now drawn down to 8 of original equity 12 500 is now 11 500'
              ' 2 of 11 500 is 9 2 mini s or 92 lots'):
            'PRINTED slide, frame burned 06:00. Note "mini\'s" and ".92" -- the slide\'s own'
            ' spelling, distinct from the audio wording quoted at V09_SOURCE_NOTES.md Sec 2c',
        ('*', 'with a 2 1 ratio 25 50 first winning trade brings balance up to 11 960'):
            'PRINTED slide, frame burned 07:05. The AUDIO at [00:07:03] reads "our first-winning'
            ' winning trade will bring us back up to 11,960" and is quoted separately',
        ('*', 'to recap calculate lot size in relation to of balance draw down at stop loss 2 is'
              ' a good place to start if you take a loss at s l come back with the same lot size'
              ' if you lose a 2nd time come back with the same lot size if you lose a 3rd time'
              ' come back with the same lot size if you lose a fourth time re calculate lot size'
              ' as you are now down 8 of original account balance'):
            'PRINTED slide, frame burned 08:20 -- the complete rule',
        ('*', 'the basic idea is that as you hit winning trades you increase your lot size and as'
              ' you hit losing cycles of 3 or 4 consecutive stop outs you diminish your lot size'):
            'PRINTED slide, frame burned 09:20',
        ('*', '1 define risk by choosing lot size which is 2 of balance at stop out can then be'
              ' able to withstand three consecutive losses no margin issues you can come back'
              ' with same lot size no emotional turbulence because you have a plan to be able to'
              ' absorb losses just wait for next mmfx signal 2 use greater than 1 1 risk to'
              ' reward ratio t p greater than s l'):
            'PRINTED slide, frame burned 14:35',
        ('*', '3 simply trading with greater than 50 accuracy will bring upward equity'):
            'PRINTED slide, frame burned 16:00 -- the A-067 sufficient-not-necessary row',
        ('*', 'think of what your equity curve will look like when you can hit 70 accuracy'):
            'PRINTED slide, frame burned 16:00',
        ('*', 'basic idea is to keep a consistent ratio of lot size as your account grows or'
              ' falls'): 'PRINTED slide, frame burned 17:05',
        ('*', 'and to consistently keep take profits larger then stop losses no impulsive'
              ' increases in lot size to make up for a loss'):
            'PRINTED slide, frame burned 17:05 -- "then" for "than" is the slide\'s own typo',
        ('*', 'no impulsive increases in lot size'): 'PRINTED slide, frame burned 17:05',
        ('*', 'possible errors to guard against 1 moving your stop loss after you have placed it'
              ' 1st s l is always the cheapest 2 putting on multiple positions which add up to'
              ' greater than your risk 3 not having the discipline to keep to the risk plan as'
              ' described 4 miscalculating lot size on non usd quote pairs use a lot size'
              ' calculator 5 not having hard stop losses and take profits with the broker'):
            'PRINTED slide, the five-errors frame burned 21:40, quoted in full',
        ('*', 'moving your stop loss after you have placed it 1st s l is always the cheapest'):
            'PRINTED, five-errors frame burned 21:40, error 1',
        ('*', 'putting on multiple positions which add up to greater than your risk'):
            'PRINTED, five-errors frame burned 21:40, error 2',
        ('*', 'multiple positions which add up to greater than your risk'):
            'PRINTED, five-errors frame burned 21:40, error 2 -- un-elided partial',
        ('*', 'not having the discipline to keep to the risk plan as described'):
            'PRINTED, five-errors frame burned 21:40, error 3',
        ('*', 'miscalculating lot size on non usd quote pairs use a lot size calculator'):
            'PRINTED, five-errors frame burned 21:40, error 4',
        ('*', 'example of equity curve of 85 win rate with 2 1 risk reward profile'):
            'PRINTED caption, frame burned 22:45 -- C-012\'s object',
        ('*', '7 wins 6 losses'):
            'PRINTED, frame burned 22:45, in the presenter\'s own hand beneath the caption',
        ('*', 'possible equity gain scenario 1 2 risk at s l 2 2 1 or greater r r 25 pip s l 2'
              ' 50 pip t p 4 3 only five successful trades per week 20 gains for the week'):
            'PRINTED slide, frame burned 25:00 -- C-013\'s object',
        ('*', 'only five successful trades per week 20 gains for the week'):
            'PRINTED slide, frame burned 25:00. The AUDIO at [00:24:52]-[00:24:55] reads "only'
            ' five successful trades per week... it brings 20% gains" and is quoted separately',
        # -- Quotations of OTHER DOCUMENTS, named at the point of use.
        ('*', 'looking for the most pristine setups where there is maximum opportunity for'
              ' scaling in heavily and trading with high lot sizes without being concerned'
              ' about losses'): 'MMM-NOTES p.50, cited as such in the Tier 2 comparison table',
        ('*', 'you can afford to trade heavily'): 'MMM-NOTES p.51, cited as such',
        ('*', 'no lesson does'):
            "A-020's own retained text, quoted back at it in the mastery report's reconciliation"
            ' row. Not a transcript quotation',
        ('*', 'do not blend'): 'SOURCING_HIERARCHY.md Sec 3.2 Case A, quoted as the rule applied',
        # -- Superseded text retained INLINE in a table cell rather than on a `>` line. The
        #    RETAINED disposition only recognises block-quote lines, and this project routinely
        #    retains a corrected rendering inside the cell it corrects. Enumerated here, with the
        #    correction that supersedes each, rather than left to trip the sweep every round.
        ('*', 'what it s titanium'):
            'RETAINED superseded text, inline in V09_SOURCE_NOTES.md Sec 5 row 3. Corrected at'
            ' V09 R1 (M1) to "what it\'s it\'s titanium", the speaker\'s own stutter',
        ('*', 'usd jpy on a usd based account'):
            'RETAINED superseded text, inline in V09_SOURCE_NOTES.md Sec 5 row 4. Corrected at'
            ' V09 R2 (item 81) to the literal "USD JP why", the ASR form',
        # -- Scoped to ONE FILE, not '*', because each of these IS the defective rendering. The
        #    mastery report's Revision R2 narrative quotes the wrong text in order to name it.
        #    A '*' entry here would excuse the same misquote reappearing anywhere in the corpus.
        ('V09_MASTERY_REPORT.md', 'what is the grape'):
            'The DEFECTIVE rendering, quoted in Revision R2 while reporting it. The transcript'
            ' reads "What is the grade Fred?"; 04_SCREENSHOTS/V09/INDEX.md row 26 is corrected',
        ('V09_MASTERY_REPORT.md', 'risk management however i believe that with our training'):
            'The DEFECTIVE rendering inside PT-035, quoted in Revision R2 while disclosing it.'
            ' The transcript reads "risk management. How are I believe that with our training?"'
            ' -- NOT fixed, because COMMON_PROTOCOL.md Sec 9 rule 7 forbids editing a'
            ' pre-registration after the fact. See the Revision R2 disclosure',
    },
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


def allow_reason(allowlist, basename, norm):
    """Full-fragment equality, not prefix -- see the ALLOWLIST comment and V07 R3 Sec 4."""
    for scope in ('*', basename):
        reason = allowlist.get((scope, norm))
        if reason:
            return reason
    return None


def check(body, allowlist, path):
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
            reason = allow_reason(allowlist, basename, norm)
            if reason:
                yield 'ALLOWED', line, tier, reason, norm
            elif in_blockquote(text, m.start()):
                # The near-miss run is REPORTED here rather than acted on. V07 R3 Sec 4 observed
                # that testing the retention rule before the cited-FLAG branch masks a new defect
                # on a `>` line, and hand-checked every retained fragment as a result. Printing
                # the run mechanises that hand check without making a retention block -- whose
                # whole purpose is to re-quote a defective rendering -- fail the sweep.
                run, matched = near_miss(body, words)
                detail = 'block quote -- superseded-text retention'
                if run:
                    detail += '; tracks transcript %d words ("%s") -- expected in a retention' \
                              ' block, hand-rule if unexpected' % (run, matched)
                yield 'RETAINED', line, tier, detail, norm
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
    argv = sys.argv[1:]
    verbose = '--verbose' in argv
    dump_allowed = '--dump-allowed' in argv
    transcript = None
    if '--transcript' in argv:
        transcript = argv[argv.index('--transcript') + 1]
        argv = [a for a in argv if a != transcript]
    positional = [a for a in argv if not a.startswith('--')]
    if len(positional) != 1 or positional[0] not in ARTIFACTS:
        sys.exit('usage: verify_quotes.py {%s} [--verbose] [--dump-allowed] [--transcript PATH]'
                 % '|'.join(sorted(ARTIFACTS)))
    lesson = positional[0]

    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__)))))
    os.chdir(root)

    if transcript is None:
        transcript = '02_TRANSCRIPTS/%s/%s_TRANSCRIPT.md' % (lesson, lesson)
    artifacts = ARTIFACTS[lesson]
    allowlist = ALLOWLIST[lesson]

    body, markers = load_body(transcript)
    body_words = body.split()
    print('LESSON       %s' % lesson)
    print('TRANSCRIPT   %s' % transcript)
    print('             %d markers, %d normalised words of spoken body'
          % (markers, len(body_words)))
    print('ARTIFACTS    %d' % len(artifacts))
    print()

    tally = {'MATCH': 0, 'ALLOWED': 0, 'RETAINED': 0, 'UNRELATED': 0, 'FLAG': 0}
    flags = []
    for path in artifacts:
        if not os.path.exists(path):
            sys.exit('FATAL: missing artifact %s' % path)
        rows = list(check(body, allowlist, path))
        print('%-72s %3d fragment%s' % (path, len(rows), '' if len(rows) == 1 else 's'))
        for status, line, tier, detail, frag in rows:
            tally[status] += 1
            if status == 'FLAG':
                flags.append((path, line, frag, detail))
                print('    FLAG      %s:%d [%s]' % (path, line, tier))
                print('              "%s"' % frag)
                print('              %s' % detail)
            elif status == 'ALLOWED':
                if dump_allowed:
                    print('    allowed   line %-5d "%s"' % (line, frag))
                    print('              (%s)' % detail)
                else:
                    print('    allowed   line %-5d "%s"  (%s)' % (line, frag[:46], detail))
            elif status == 'RETAINED':
                print('    retained  line %-5d "%s"' % (line, frag[:46]))
                if 'tracks transcript' in detail:
                    print('              %s' % detail[detail.index('tracks transcript'):])
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
