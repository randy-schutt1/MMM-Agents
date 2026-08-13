# V10 — INDEPENDENT REVIEW

| Field | Value |
|---|---|
| Lesson | **V10** · `Bootcamp1 Wk3 040112 (96mins).swf` · session 2012-04-01 |
| Review version | **R1** |
| Review date | 2026-08-13 |
| Previous review | none |
| Reviewer branch | `review/v10`, cut from `video/v10` @ `e5262b2` (`D-038`) |
| Independence | **`D-003` satisfied.** This session did not author any V10 artifact. It read the source before the student's conclusions and re-derived every quantitative claim from the committed data with independently written code |

---

## FINAL DECISION

```text
REVISE
```

**Decision:** `REVISE` — **0 CRITICAL, 0 MAJOR, 4 MINOR, 7 NOTE.**

Under `DECISIONS.md` **D-024** a round carrying zero `CRITICAL` and zero `MAJOR`
**opens the gate for V11.** The four minors are carried in `REVIEW_INDEX.md` and are still
owed before V10 can reach `COMPLETE`. **One of them (`M1`) must be discharged before the
merge-back, not after** — it is a register-integrity defect that a merge would make concrete.

**Confidence:** **HIGH.**

Confidence is high and not merely positive because the load-bearing claims in this submission
were **re-derived rather than read**: both backtest measures were recomputed from the committed
CSV by a reviewer-written script sharing no code with `mmm_lib`/`mmm_week`, and every figure
reproduced exactly; the `Q-011` `diff` was re-run and extended; the two load-bearing slides were
opened and read pixel-by-pixel against their transcriptions; and the whole 3,557-line transcript
body was read before any student artifact was opened.

---

## SOURCE MATERIAL REVIEWED — **FIRST, BEFORE ANY STUDENT CONCLUSION**

| Source | References | Purpose |
|---|---|---|
| `02_TRANSCRIPTS/V10/V10_TRANSCRIPT.md` verbatim body | **All 3,557 lines, `[00:00:00]`–`[01:36:12]`, read in full** | The primary evidence for every finding below. Read **before** the lesson notes, interpretation, homework, backtest or mastery report were opened |
| Screenshot `43:17` — safety trade rules slide 1 | Opened and read as an image | Verify R1–R4 against the printed source |
| Screenshot `46:17` — safety trade rules slide 2 | Opened and read as an image | Verify R5–R9 against the printed source |
| Screenshot `75:57` — the 25–75 pip slide | Opened and read as an image | Verify `A-078`'s "the number is settled" and `C-017`'s printed side |
| Screenshot `96:16` — the end card | Opened and read as an image | Verify the printed-and-never-spoken close, and the Easter-Sunday forward reference |
| `_QUARANTINE_UNVERIFIED_NOTES/per_lesson/**/RULES.md` | **All 21**, `diff`ed pairwise | Independent re-derivation of `Q-011` §3, extended library-wide |
| `datasets/HISTDATA_GBPUSD_M1/GBPUSD_M15_ARM{A,B}.csv` | 86,536 / 86,532 M15 bars in `W-C′` | Independent re-derivation of `PT-036` `M1`, `M2a`, `N2`, `N3`, `O2`, `O4` and the H2 anchors |
| `02_TRANSCRIPTS/V01–V09/*_TRANSCRIPT.md` | `peak formation` census | Verify the "first operational definition in ten lessons" claim |
| `00_SYSTEM/SWF_CAPTURE_RECIPE.md` §10 | Read in full | Adjudicate the student's escalation |

**Source access was not limited.** The `.swf`, the audio-derived transcript, all 32 curated
frames and the full historical corpus were available. Nothing in this review is capped by
missing evidence.

## STUDENT ARTIFACTS REVIEWED

| Artifact | Reviewed |
|---|---|
| `02_TRANSCRIPTS/V10/V10_TRANSCRIPT.md` header (speaker table, verification, coverage, notes) | ✅ in full |
| `03_LESSON_NOTES/V10_SOURCE_NOTES.md` · `V10_INTERPRETATION.md` | ✅ in full |
| `04_SCREENSHOTS/V10/INDEX.md` + 5 frames opened | ✅ |
| `05_HOMEWORK/V10/` — homework, flashcards, comprehension answers, both scripts, both outputs | ✅ |
| `06_MANUAL_BACKTEST/PRE_REGISTERED/PT-036…md` · `V10/BT_V10_0001.md` · `data/pt036_output.txt` | ✅ in full |
| `06_MANUAL_BACKTEST/scripts/run_pt036.py` + its post-commit diff at `2856631` | ✅ |
| `07_MASTERY_REPORTS/V10_MASTERY_REPORT.md` | ✅ in full |
| `00_SYSTEM/QUARANTINE_REGISTER.md` `Q-011` · `10_AMBIGUITIES/` `A-010`, `A-076`–`A-079` · `11_CONTRADICTIONS/` `C-016`, `C-017` | ✅ |

---

## CRITICAL FINDINGS

**NONE.**

| # | Finding | Error code | Evidence | Impact |
|---|---|---|---|---|
| — | *No finding in this round could materially alter the methodology or later trading logic.* | — | — | — |

The two places a `CRITICAL` could plausibly have arisen were checked directly and both are clean:

1. **Lookahead in the backtest.** `PT-036` measures a completed week's range and a completed
   Friday's close position. There is no decision point, no entry, no barrier and nothing that
   could consume future information. Verified by re-derivation.
2. **Lookahead smuggled into the homework.** The ten H2 anchors *are* retrospective — a weekly
   extreme is knowable only after the week ends. **The submission says so itself, unprompted,
   in `V10_HOMEWORK.md` §2e**, and states that nothing in §2b may be read as evidence the
   anchors were identifiable in advance. That disclosure is the correct handling and it is why
   this is not a finding.

---

## ⭐ THE HOST-VS-GUEST DETERMINATION — THE ROUND'S MOST CONSEQUENTIAL CLAIM

**Reviewer verdict: the determination is CORRECT. Confidence HIGH. It is not merely
defensible — it is over-determined.**

This was audited hardest because it is the claim with the furthest reach: it ends a
five-lesson guest run and sets the provenance frame for V11 onward. Each of the five strands
was checked against the transcript by this reviewer, independently.

| Strand | Reviewer finding |
|---|---|
| **1 — first-person mailbox** | **CONFIRMED and decisive on its own.** `[00:07:12]` *"my only valid email address right now is Steve at"* → `[00:07:20]` the domain. This is not a reference to a third party; the possessive is first-person and the name is the object of it. The printed slide at `07:08` — which I opened — reads *"My only Valid e-mail address:"* over `steve@marketmakersforex.com` |
| **2 — the 13 `Steve` tokens** | **COUNT CONFIRMED — exactly 13 in the verbatim body, by word-boundary match.** The *characterisation* is imprecise; see `N1` below. **The evidential force is undamaged**: not one token is the speaker referring to an absent Steve in his own narrative voice |
| **3 — reads mail addressed to himself** | **CONFIRMED.** `[00:12:53]` *"Hi, Steve. Thanks for your turn to me so quickly about the ADR correction on Friday"*, read aloud and then answered in the first person at `[00:13:03]` *"here's what she's asking"*. Frame `07:57` prints a student email opening *"Hello Steve"* |
| **4 — claims authorship** | **CONFIRMED, and stronger than the submission claims.** `[01:28:11]`–`[01:28:22]` *"I wrote the lesson. I give it to my wife. She converts it to slides. I get all my chart pictures marked up and inserted into the slideshow then I do a dry run"* is an account of authoring **this artifact**, including the deck the reviewer just read |
| **5 — owns the homework loop** | **CONFIRMED.** `[00:17:49]`, `[00:20:38]`, `[01:34:26]` |
| **Negative check — handover language** | **CONFIRMED ZERO.** I ran my own scan over the body for *take it away / hand over / turn it over / the floor is yours / thanks for having me / passing it to / introduce / I'll let (him\|her\|them)*: **no matches in 96 minutes** |

### Four further strands this reviewer found that the submission does not cite

Recorded because independence means adding evidence, not only checking it. Each is
first-person ownership of something only the course's principal could own:

1. `[00:01:41]`–`[00:01:58]` — **ownership of the forum**: *"I know that the topic pages have
   gotten out of control. I'm probably gonna take all those pages, condense them down…"*
2. `[00:05:03]`–`[00:05:27]` — **ownership of the seminar**: *"on behalf of market makers
   [forex] [and] compass FX we're gonna be hosting a seminar… We asked him to come to our
   Orlando class."* First-person plural, on behalf of the business.
3. `[00:06:27]` — **ownership of the recordings**: *"everything I do is recorded, the only issue
   is his copyright. I have not cleared that a hundred percent with him."* The speaker is the
   party who clears third-party rights.
4. `[00:32:56]`–`[00:33:26]` — **the starfish story**, ending *"it matters to me that you
   understand and represent my family."* A guest does not ask a cohort to represent his family.

### Could this still be a guest impersonating or quoting the host?

**No, and the question deserves a real answer rather than a dismissal.**

The impersonation hypothesis requires a single unbroken 96-minute performance in which the
speaker claims Steve's mailbox, Steve's forum, Steve's seminar, Steve's recordings, Steve's
authorship of the deck on screen, Steve's wife, Steve's mentor and Steve's family — while
reading mail addressed to Steve, answering students who address him as Steve, and never once
breaking frame. There is no motive on the record and no seam in the audio. V04's genuine
handover, by contrast, was unannounced but still produced an audible topic seam; V10 has none,
and its closing Q&A at `[01:35:14]`–end is answered in the same voice that opened it, in the
first person, with personal preferences (*"I personally like London"*).

The quoting hypothesis is weaker still: quotation is exactly what strands 2 and 3 measure, and
the direction is wrong for it — the speaker is quoted **to**, not **about**.

**One limit, stated rather than glossed.** What the file establishes internally is that the
speaker is *the course's author and is named Steve*. That he is *Steve Mauro* rests on the
corpus-external attribution of the course, which is not in dispute but is also not proved by
this recording. The submission's transcript header labels him *"The course author (Steve
Mauro)"*; the parenthesis is an external identification and is correctly parenthetical.

### And the safeguard is the part that matters most

`D-025` consequence 4 — re-adopted verbatim by `D-033` — requires that **nothing depend on the
identification being right.** The submission asserts this and I checked it: `PT-036` measures
OHLC and never uses a speaker; every source-note row is tagged `AUDIO`/`PRINTED` rather than
speaker-weighted; and `D-033` makes all speakers equal in authority in any case. **If this
determination were wrong tomorrow, not one rule, record or number in V10 would move.** That is
the correct architecture and it is why a `HIGH`-confidence provenance call carries no risk here.

**The acoustic screen was correctly not run.** V07's carry-forward prohibits the cross-file
`f0_profile.py` comparison; V09 honoured it and V10 does too. The five non-acoustic strands
were, per the transcript header, fixed before the answer was known. Nothing in the result
depended on the prohibited instrument.

---

## RULE FIDELITY

**Grade: PASS.**

The nine printed safety-trade rules are the lesson's core. I opened both slides and compared
character by character.

| Student's rendering (`V10_SOURCE_NOTES.md` §6c) | Slide at `43:17` / `46:17` as read by the reviewer | Assessment |
|---|---|---|
| R1 *"PFH /PFL has formed as HOW or LOW (**4hr Tie in**)"* | *"PFH /PFL has formed as HOW or LOW (4hr Tie in)"* | **EXACT**, including the space before the slash |
| R2 *"Price has moved away from the area and has confirmed the formation"* | identical | **EXACT** |
| R3 *"Level one consolidation is clear"* | identical | **EXACT** |
| R4 *"DNC- Remember this is level 1 consolidation a sucker trades the breakout back towards the peak ( Don't be a sucker)"* | identical, including the stray space after `(` | **EXACT** |
| R5 *"Dealer Makes A visible stop hunt (preferably above or below blue box)"* | identical | **EXACT** |
| R6 *"Remember the "Straight-Away" develops here"* | identical | **EXACT** |
| R7 *"Obvious ones are still valid sets"* | identical | **EXACT** |
| R8 *"Dealer Issues Second Leg M or W this locks the trade"* | identical | **EXACT** |
| R9 *"If the Level is hit a third time….God help the dealer!!"* | identical, four dots | **EXACT** |
| `A-078` / frame 26: *"Look for the stop hunt to come in around 25 to 75 pips off of the LOW/HOW anchor."* | identical | **EXACT** |
| End card: *"Looks like I **will** have a session for Easter Sunday… / So same time next week / Thank you all GOOD NIGHT"* | identical, `will` underlined on the slide | **EXACT** |

**Nine printed rules and two load-bearing slide texts, transcribed without a single
substitution, including three typographic infelicities a "tidying" transcription would have
silently removed.** This is the strongest rule-fidelity result the corpus has produced.

Spoken quotations were spot-checked at fifteen markers spanning the file (`[00:13:41]`,
`[00:14:09]`, `[00:14:38]`, `[00:23:36]`, `[00:41:45]`, `[00:42:41]`, `[00:46:43]`,
`[01:00:41]`, `[01:00:43]`, `[01:01:56]`, `[01:02:04]`, `[01:06:49]`, `[01:13:47]`,
`[01:14:06]`, `[01:26:39]`). **All fifteen resolve verbatim at the cited marker.**

**Qualifiers are carried, not dropped.** The three that would have been convenient to lose
are all present: the 600–1000 band's upper end attributed to crosses (`[00:14:26]`), the
unoperationalisable exception (`[00:14:43]`), and *"never fails"* withdrawn in the same breath
(`[01:31:26]`). The last is `D-009` handling done correctly — the claim is preserved with
provenance and is not treated as a target.

---

## THE `[01:14:06]` DEFINITION — VERIFIED, AND THE NARROWING IS JUSTIFIED

**The quote exists, verbatim, at the cited marker.** Reviewer's own read of the body:

> `[01:13:58]` *"We're identifying the peak formation high or high of the week and the peak
> formation low or"* · `[01:14:05]` *"Low of the week"* · `[01:14:06]` ***"Which is the highest
> point on a chart within the week or the lowest point on the chart within the week?"***

**Is it genuinely novel? YES — independently confirmed.** I censused `peak formation` across
all nine prior transcripts:

| Video | `peak formation` occurrences in body | Definitional language |
|---|---|---|
| V01 | 2 | none |
| V02 | 6 | none |
| V03 | 1 | none |
| V04 | 1 | none |
| V05 | 2 | none |
| V06 | 8 | none |
| V07 | **0 in body** (the header hits are `Q-008`'s fabrication census) | none |
| V08 | 0 | none |
| V09 | 3 | none |

**And the decisive negative:** the strings *"highest point on/in a chart"* and *"lowest point
on/in a chart"* occur in **zero** of V01–V09. The claim *"first operational definition of peak
formation in ten lessons"* is **CONFIRMED**.

**Is `A-010 NARROWED` (not `CLOSED`) the right disposition? YES.** The submission's own Q8
argues against itself here — that the sentence is a relative clause inside a digression about
multi-timeframe analysis, stated once at minute 74 of 96, and not printed in that form. I agree
with the objection **and with the conclusion drawn from it.** Three things make `NARROWED`
correct rather than timid:

1. The identity `PFH = HOW` / `PFL = LOW` **is** printed, on the rules slide I read at `43:17`.
   The definition restates a working identity rather than coining one.
2. It is **used operationally** elsewhere: `[01:33:43]`–`[01:33:51]` *"Identifying the higher
   low point of the week… there's looks like the lowest point on the chart right now, let me
   draw a line on the lowest point of the chart."*
3. `CLOSED` would over-read a single relative clause; leaving `A-010` untouched would ignore
   the only definitional sentence in ten lessons. `NARROWED` is the disposition the evidence
   supports.

**The limit is correctly identified and it is the most important sentence in the interpretation
file:** the definition is *retrospective* and is therefore not a *setup* rule. `V10_INTERPRETATION.md`
Q1 limit 2 names conflating the two as lookahead bias and *"the single biggest hazard V10
introduces."* That is exactly right, and the submission then declines to walk into it (`PT-036`
§2). **This is the round's best single piece of judgement.**

---

## "NO STOP LOSS ANYWHERE" — VERIFIED BY THE REVIEWER'S OWN SEARCH

**CONFIRMED.** My own word-boundary search over the verbatim body:

| Pattern | Occurrences |
|---|---|
| `stop loss` / `stop-loss` / `stoploss` | **0** |
| the same, over the **entire file** including the header | **0** |
| `stop` / `stops` (any sense) | 80 — **all** of them *stop hunt*, *hit the stops*, *stop hunt zone*, *burns the stops* |

The finding in `V10_SOURCE_NOTES.md` §15 is sound: the safety trade is given an entry, a
direction, a target (*"plus 50"*) and a time horizon, **and no invalidation price.**

**One piece of evidence the submission missed, and it strengthens the finding — see `N2`.**
`[00:01:33]`: *"Hold the questions that about **trailing stops** and other things that are not
pertinent to what I'm talking about."* The only stop-management concept anywhere in 96 minutes
is the speaker **actively declining to discuss it**. That is stronger than mere absence: it
shows the topic was raised by students and deferred, rather than never arising.

`C-016`'s consequence paragraph is therefore correct and, if anything, understated: **a trade
whose only non-target exit is a holding period, and whose holding period is stated five
different ways, has no defined exit.** This is the right thing to have noticed.

---

## MANUAL BACKTESTING — **RE-DERIVED INDEPENDENTLY**

**Grade: PASS.**

### The re-derivation

A reviewer-written script (`rederive_pt036.py`, no import of `mmm_lib`, `mmm_week` or any
project module) rebuilt the week roster from the Sunday-17:00 anchor, the session-day labelling
from convention C-1, and both measures from the committed M15 CSVs. **Every reported figure
reproduced exactly.**

| Quantity | Reported | Reviewer re-derived | Match |
|---|---|---|---|
| M1 usable weeks | 180 | **180** (182 anchors − data hole − truncated) | ✅ |
| M1 in `[600, 1000]` | 0 / 180 = 0.00% | **0 / 180 = 0.00%** | ✅ |
| M1 median | 243.8 pips | **243.8** | ✅ |
| M1 p05 / p25 / p75 / p95 | 138.0 / 189.1 / 322.7 / 444.5 | **identical** | ✅ |
| M1 min / max | 76.6 / 1789.5 | **76.6 / 1789.5**, max = week of **2016-06-19** (EU referendum) | ✅ |
| percentile at which 600 sits | 99.44th | **99.44th** | ✅ |
| `O2` median ÷ 800 | 0.305 → overshoot 3.28× | **0.3047 → 3.28×** | ✅ |
| pip-vs-point rescue `[60,100]` | 4 / 180 = 2.2% | **4 / 180 = 2.22%** | ✅ |
| M2a Fridays, arm A | 13 / 178 = 7.30% | **7.30%, n = 178** | ✅ |
| M2a Fridays, arm B | 10 / 178 = 5.62% | **5.62%, n = 178** | ✅ |
| `N2` uniform null, A / B | 7.12% / 7.00% | **7.12% / 7.00%** | ✅ |
| `N3` Thursday, arm A | 13.41% | **13.41%** | ✅ |
| `N3` Friday − best other, A / B | −6.10 pp / −8.91 pp | **−6.10 / −8.91 pp** | ✅ |
| `O4` Friday range in `[50,100]` | 40.45%, median 107.0 | **40.45%, median 107.0** | ✅ |
| censored observations | 0 | **0 — structurally impossible to be otherwise** | ✅ |

**Both verdicts — `M1 CONTRADICTED AS STATED` and `M2 CONTRADICTED AS STATED, specificity
FAILED` — are upheld on independent computation.**

The `N2` result is the one I would highlight as the submission does: a close placed **at
random** inside Friday's own high–low interval lands in the 25–50-from-both-ends band about as
often as the real close does (+0.19 pp on arm A), and **less often than chance on arm B**.
Without that matched null, 7.30% reads as a weak effect. With it, the effect is zero. Building
the null *per Friday from that Friday's own realised range* removes the range-width confound by
construction rather than by assumption, and that is the correct design.

### The 14 procedural checks — `REVIEW_PROTOCOL.md` §6.G

| # | Check | Result |
|---|---|---|
| 1 | GBP/USD as primary instrument | **YES** — `D-007`, exclusively |
| 2 | Historical period selected reasonably | **YES** — `W-C′` = `D-035`'s DEVELOPMENT block exactly, pre-registered |
| 3 | Chart advanced sequentially | **N/A** — distributional measurement, no sequential decision |
| 4 | Future price hidden at the decision point | **N/A by construction** — there is no decision point |
| 5 | Rules known before the result | **YES — verified in git.** Pre-registration `f58dce7` (327 lines, one file) precedes runner `e53409e` (387 lines, one file) precedes output `2856631` |
| 6 | No trades skipped after outcomes visible | **N/A** — no trades |
| 7 | Losers retained | **N/A** — no trades |
| 8 | Borderline setups retained | **N/A** |
| 9 | Invalid setups separated from valid losers | **N/A** |
| 10 | Outcomes recorded consistently | **YES** — both arms, every observable, every time |
| 11 | R calculated consistently | **N/A** — no R |
| 12 | Screenshots before/after | **N/A and correctly justified** — every figure is parsed from a checksummed CSV; nothing is measured off a rendering |
| 13 | Exact lesson rule identified per test | **YES** — `M1` and `M2` each quoted with markers |
| 14 | Testing the lesson, not a later interpretation | **YES, and this is the strongest answer in the table** — see below |

### Checks 15–20 — `D-026` / `D-027` / `BACKTEST_EVIDENCE_STANDARD.md`

| # | Check | Result |
|---|---|---|
| 15 | Baseline present | **YES** — `N1`–`N4`, four distinct controls. `D-026`'s named default (matched random entry) is a control for a rule that *takes trades*; `PT-036` takes none, and the substitution to matched distributional nulls is **argued in the pre-registration, not after** (§4), following the `PT-028` precedent. **Correctly reasoned, not evaded** |
| 16 | Baseline pre-registered | **YES** — §4, at `f58dce7`, with seed `20260813` and 10,000 iterations fixed there |
| 17 | Period pre-registered | **YES** — §7, unchanged through the run |
| 18 | Holdout intact | **YES** — 2016-07-01 onward is **not on disk**; `D-036a` truncated it on arrival. `assert_development` enforced per slice |
| 19 | Sample sufficiency and interval | **YES** — smallest quoted cell n = 178; bootstrap **and** Wilson intervals on every rate |
| 20 | Negative results retained | **YES, and exceeded.** Both measures failed and both are reported in full; the untested safety trade is reported as a finding of equal prominence; the crashed first runner is disclosed against interest |

### The three judgement calls, adjudicated

**(a) Was the safety trade correctly identified as untestable, or dodged? — CORRECTLY
IDENTIFIED. This is the round's most defensible decision.**

I checked the condition count myself against the printed rules I read at `43:17` and `46:17`:

| Condition (from the slides) | Codable today? | Blocker — verified |
|---|---|---|
| PFH/PFL formed as HOW/LOW | **YES** | `[01:14:06]` supplies it |
| DNC — do not counter | **YES**, as a prohibition | — |
| Price moved away and confirmed (*the lock*) | **NO** | **No distance, no duration, anywhere in 96 minutes.** I searched: `[01:05:35]`'s *"15 hours 16 hours"* is narration of one chart, not a threshold |
| Level one consolidation clear | **NO** | `consolidation` undefined; `the level` = `A-004`, open since V01 |
| Visible stop hunt, preferably outside the blue box | **NO** | `blue box` undefined, and V10 states **no session clock boundary at all** |
| Second leg M or W | **NO** | `A-007`, open since V04 |
| Third touch of the level | **NO** | `A-004` |

**Five of seven blocked. `D-030` is explicit and binding.** More importantly, the *specific*
hazard is correctly named: because V10's anchor is the week's extreme and that is retrospective,
a naive backtest would use the **actual** weekly extreme as the entry anchor — **lookahead
(`E08`) producing a flattering, publishable-looking number whose caveat would not survive being
quoted twice.** The submission names this in three separate files and declines. That is `D-030`
working as designed, and declining to test is here the *harder* choice, not the easier one: this
session had working tooling, a clean QA gate and 86,824 bars, and chose to publish two null
results about context claims instead of a headline number about the trade.

**(b) The runner was edited after being committed. Is that a `COMMON_PROTOCOL.md` §9 rule 7
violation? — NO. Verified against the diff.**

I read `git show 2856631 -- run_pt036.py`. The change is confined to session-day labelling:
`WEEKDAYS` loses its `Sun` element, `sessions_for_week` derives its label from
`mmm_lib.session_day` instead of `(tm − anchor) // 1440`, and the weekday loop runs to 5 instead
of 6. **Not one threshold, seed, exclusion, prediction, estimand or decision rule moved.** The
disclosed failure — a Sunday/Monday off-by-one emptying the Friday set and raising in
`np.percentile` — is consistent with the code as committed. Rule 7 governs disagreements found
*after a result exists*; no result existed. **Disclosure is correct and the classification is
correct.**

**(c) The 6/6 prediction tally.** The submission argues its own tally **down**, correctly:
P1/P2 are one finding, P3/P4/P5 are one finding, only P6 was independent, and P7 was flagged
cheap before the run and tallied separately. **I agree, and note that a session that discounts
its own success record is doing the thing `D-009` exists to protect.**

---

## HINDSIGHT / LOOKAHEAD AUDIT

| Observation | Contamination found | Severity |
|---|---|---|
| `PT-036` `M1` — weekly range | **NONE.** Completed weeks; no decision point exists | — |
| `PT-036` `M2` — Friday close position | **NONE.** Completed sessions; no barrier, no horizon | — |
| `N4` shifted-boundary control | **NONE.** Deterministic re-anchoring; pre-registered | — |
| H2's ten anchors | **Retrospective by nature — and DISCLOSED UNPROMPTED** (`V10_HOMEWORK.md` §2e), with the explicit statement that nothing may be read as evidence they were identifiable in advance | Not a finding |
| H2 week selection | **CLEAN, and mechanically so.** Weeks 1/37/73/109/145 and 19/55/91/127/163 in chronological order — an even deterministic spread fixed before any price was read. **This is the correct defence against `STUDY_PROTOCOL.md` §2's ban on picking clean examples**, and I verified four of the ten anchors reproduce exactly from the raw data |
| The safety trade | **NOT TESTED — and the reason given is precisely the lookahead hazard.** Declining a test to avoid contamination is the opposite of contamination | — |
| Post-hoc rescue attempts | **NONE, and one was pre-empted.** The pip-vs-point unit check was pre-registered in `O2` **specifically so it could not become a post-hoc rescue**, and it is reported having failed too (4/180). `PT-037`'s path-length reading is specified and **explicitly not run**, with the reason stated as `E09` |

**Verdict: CLEAN.**

This is the cleanest hindsight audit in the corpus to date. The submission does not merely avoid
lookahead — it **names the specific mechanism by which it would have entered, pre-registers the
diagnostic that would otherwise have become a rescue, and refuses an unregistered alternative
after seeing a failure.**

---

## HOMEWORK

**Grade: PASS.**

| # | Claimed | Reviewer verification | Assessment |
|---|---|---|---|
| H1 flashcards | DONE — five cards on V10's stated rules | Read. The honest limit is stated: the printed exemplar at `34:22` depends on **five undefined terms in eight lines** (`shark fin`, `resist band`, `blue tracer`, `S/H zone`, `Level 3`), so a faithful chart card cannot presently be produced. **Correct** | ✅ |
| H2 anchors | 10 anchors, 5 long / 5 short | **Re-derived four of ten from the raw M15 corpus: 2013-01-06 LOW 1.59913 (186.7 pips), 2015-10-18 LOW 1.53058 (201.5), 2015-06-14 HIGH 1.59296 (442.1), 2016-02-21 HIGH 1.43054 (451.8) — all four match on price and week range** | ✅ |
| H2 setups | `DEFERRED` under `D-019` | **Correct, and the argument is right.** `NOT APPLICABLE` means *there was never anything here*; V10 spends fifty minutes on the setup, so subject matter plainly exists. It is blocked **definitionally**, which `D-030` says must wait. Marking it `NOT APPLICABLE` would permanently discard performable research | ✅ |
| H3 forum | `NOT APPLICABLE` under `D-018` | Correct — a 2012 venue with no present-day analogue; consistent with the V01 H1–H3 precedent upheld at R1 | ✅ |
| Comprehension | 12/12, 44 assertions | Answers committed at `54b97f2`, **before** `score_comprehension.py` existed — verified in git. **The first attempt is preserved and nothing was reconstructed after seeing a solution** | ✅ |

**Classification: `FIRST-PASS SUCCESS` for H1 and the comprehension probe; `DEFERRED` for H2's
setup half; `NOT APPLICABLE` for H3.**

**On the 12/12 — the submission is right that it should not carry much weight, and I am adopting
its own three reasons rather than inventing a fourth.** The same session wrote the answers and
the scorer; four questions were designed with their distractors in view; and the two hardest
answers are refusals, which is partly evidence about the protocol rather than about
comprehension of V10. **A student that pre-emptively discounts its own perfect score, names the
mechanism, and redirects the reviewer to `Q-011`, `C-016`/`C-017` and `BT_V10_0001` §1 as the
load-bearing evidence, is doing the reviewer's job for the reviewer — and it happens to be
right.** Those three *are* where the comprehension shows.

**The H2 cross-check is correctly valued.** Computing each anchor twice — from the M15
aggregation and from raw M1 — and gating on disagreement is good practice, and the submission
states plainly that **an M15 bar's high *is* the maximum of its M1 constituents' highs, so
agreement is expected**: the check corroborates the *aggregation*, not the market. Describing a
tooling check as a tooling check, when it could have been dressed as independent confirmation,
is exactly the discipline this project is for.

---

## PROVENANCE AUDIT

**Grade: PASS.**

| Rule | Cited source | Verified? | Status |
|---|---|---|---|
| Safety trade rules R1–R9 | Frames `43:17`, `46:17` + `[00:43:01]`–`[00:47:16]` | **Reviewer opened both frames and read them** | **SUPPORTED** |
| Anchor distance 25–75 pips | Frame `75:57` + six spoken markers | **Frame opened and read; markers verified** | **SUPPORTED** |
| PFH/PFL = week's extreme | `[01:13:58]`–`[01:14:06]` | Verified verbatim | **SUPPORTED** |
| Weekly range 600–1000 | `[00:14:09]`, `[00:14:38]` | Verified verbatim | **SUPPORTED** |
| Friday close 25–50 both sides | `[00:13:41]`–`[00:13:52]` | Verified verbatim | **SUPPORTED** |
| Timing prohibition | `[00:23:04]`, `[01:06:22]`, `[01:06:49]` + frame `23:03` | Verified | **SUPPORTED** |
| *"Sunday is not day one"* | `[01:26:39]` | Verified verbatim | **SUPPORTED** |
| Accuracy claim | `[01:31:20]`–`[01:31:34]` | Verified, **including the withdrawal of *"never fails"*** | **SUPPORTED**, `D-009` handling correct |

**Orphan rules: NONE FOUND.** Every substantive rule in `§6` of the source notes carries a
marker, and every marker I sampled resolves.

**The basis-tag mechanism is the right design and it survives its own test.** Every §6 rule is
tagged `AUDIO` or `AUDIO+PRINTED`; **none rests on `PRINTED` alone.** I verified the consequence
the tag advertises: strike every `PRINTED`-only row and the lesson's contribution stands. The
screenshots corroborate the rule set; they do not supply it.

**Frame references use burned-in player timecodes rather than ordinals.** This is V09 R1's `M4`
/ open item 76 rule, followed from the start rather than retrofitted, and it is the structurally
correct fix — an inserted frame cannot invalidate a timecode. **Confirmed on the four frames I
opened: `43:17`, `46:17`, `75:57` and `96:16` all read on-screen exactly as the index claims.**

---

## AMBIGUITIES

**Grade: PASS.**

| Term | Student handling | Reviewer assessment |
|---|---|---|
| `blue box` (`A-076`) | `DO NOT CODE`; notes that `[00:46:43]` *"you're smarter than a box"* explicitly admits setups violating the boundary | **UPHELD.** The trap is correctly named: the box is simultaneously the definition of a *true* stop hunt, a *preference*, and *optional* for the experienced |
| the lock (`A-077`) | `DO NOT CODE`; no distance, no duration | **UPHELD, and I agree it is the most consequential gap in the lesson.** `[01:05:35]`'s *"15 hours 16 hours"* is correctly read as narration of one chart rather than a threshold — I checked the surrounding context and the reading is right |
| anchor distance (`A-078`) | **Number RESOLVED by the slide; reference point NOT.** Deliberately split | **UPHELD, and the split is principled** — see below. Census undercounts by one; `M2` |
| `blue tracer` (`A-079`) | `DO NOT CODE`; *"separates the day"* reads vertical, *"pips off of"* requires horizontal | **UPHELD.** The candidate reading that would dissolve it (*the tracer is the previous day's close drawn horizontally*) is plausible, is named, and is **refused** because no source states it. Correct under `D-030` |
| `peak formation` (`A-010`) | **NARROWED** on Tier 1 evidence alone, not blended with `MMM-NOTES` | **UPHELD** — see the dedicated section above |
| `the level` (`A-004`) | STAYS OPEN; and V10 **routes around** it | **UPHELD and the observation is sharp.** At `[01:16:28]` a student says they cannot identify level three; `[01:16:36]` answers *"I'm telling you how to identify: you take the trade in line with the peak formation…"* — **a workaround that avoids needing the level, not a definition of it.** Read as corpus evidence that is genuinely important |

**On `A-078`'s split — I want to record that this is consistent, not opportunistic.** The
submission applies `D-008` (slides outrank transcripts) to settle the **number**, then declines
to apply it to the **reference point** in `C-017`. That looks like having it both ways until you
ask what `D-008` ranks. It ranks *capture reliability*. For a number, capture is exactly the
problem — the ASR demonstrably garbles digits in this very file (`20`, `50 75`, `25 to 50`), and
the speaker is heard self-correcting toward the printed form at `[00:52:09]`. For an object
**name**, capture is not the problem — the ASR renders *"blue tracer"* cleanly every time, so
the divergence is in what the speaker said, not in how it was recorded. **Applying a
capture-reliability rule where capture is at issue and withholding it where capture is not is
the correct discrimination.** I checked this specifically because it was the most likely place
for motivated reasoning, and it is not that.

**No premature constants.** Three machine candidates are recorded and fenced
`INFERRED MACHINE CANDIDATE / NOT A COURSE RULE`, including the tempting one
(`PFH(w) = max(high) over week w`), which is correctly held back on the ground that V10 states
no week boundary. **Even `target = 50 pips` and `anchor_distance ∈ [25,75]` — both of which
*are* stated numerically and printed — are held `DO NOT CODE`, on the reasoning that a target
without a defined trigger is not a rule.** That is the machine-rule firewall applied against
the session's own interest, and it is right.

## MACHINE-RULE FIREWALL

| Proposed rule | Source support | Classification |
|---|---|---|
| `PFH(w) = max(high) over trading week w` | `[01:14:06]` for the concept; **week boundary NOT stated** | `INFERRED MACHINE CANDIDATE — NOT A COURSE RULE` — correctly fenced |
| `lock(t) = extreme unbroken N hours AND displacement ≥ M pips` | **NONE.** N and M exist in no source | `NOT A COURSE RULE / DO NOT CODE` — correctly fenced |
| `stop_hunt = excursion beyond blue_box then close back inside` | `blue box` undefined; lesson admits setups that do not exit it | `NOT A COURSE RULE` — correctly fenced |
| `target = 50`, `anchor_distance ∈ [25,75]` | **Stated and printed** | Held `DO NOT CODE` at Phase 1 — **correct**, the entry they attach to is undefined |

**No unsupported quantification entered any artifact. Firewall intact.**

---

## CONTRADICTIONS

**Grade: PASS.**

| Conflict | Student resolution | Reviewer status |
|---|---|---|
| `C-016` — the lock is *"one-day"* and *"good for three days"* two seconds apart | `UNRESOLVED`; the tidy reconciliation named and **refused in writing** | **UNRESOLVED — refusal UPHELD.** See below |
| `C-017` — anchor distance measured from the **LOW/HOW anchor** in print and the **blue tracer** in speech | `UNRESOLVED as to the reference point`; `D-008` named and **declined**, with reasons | **UNRESOLVED — refusal UPHELD.** See below |

### `C-016` — was refusing the tidy reconciliation correct, or overly conservative? **CORRECT.**

I read the passage directly. `[01:00:41]` *"You have a one-day lock on the directional bias"* →
`[01:00:43]` *"You know the the lock is good for three days"*. **Two seconds, one breath, one
speaker, one object.**

The available reconciliation — that the *lock* lasts three days while the *tradeable rise* is
two, with *"one-day"* meaning "a lock established in one day" — is, as the record says,
**grammatically possible and a construction rather than a reading.** The speaker does not say
it. Three things make refusal right rather than timid:

1. **The corpus now holds five figures for one object** — `one day`, `two days`, `at least two
   days`, `three days`, `three days + maybe one more`. A reconciliation that fits two of five is
   not a resolution.
2. **`REVIEW_PROTOCOL.md` §O forbids silently resolving**, and the record does not silently
   resolve — it names the candidate, refuses it, and says why. That is the protocol's exact
   prescription.
3. **The consequence is real, not bookkeeping.** With no stop loss anywhere in the lesson, the
   holding period *is* the exit. Adopting a number here would be inventing the safety trade's
   invalidation.

**Nothing is over-conserved either:** no artifact carries a holding period, and no V10 test
depends on one. The refusal costs nothing and protects a real gap.

**One thing the record should have said and did not — `M4`.** The same transcript's
TRANSCRIPTION NOTE 1 warns that *"numeric ranges wobble, and one of them is load-bearing"*, and
rates the transcript `MEDIUM–HIGH`. `C-016` rests entirely on two ASR-rendered numbers, neither
printed on any slide. **That caution is an additional, independent reason to refuse
reconciliation** — if either figure may be a rendering artifact, no construction over them is
safe. The record argues only from the speaker's words as though their capture were certain,
which is inconsistent with how the same session (rightly) treated `A-078`. **This strengthens
the disposition rather than undermining it**, which is why it is `MINOR`.

### `C-017` — was refusing correct, or overly conservative? **CORRECT, and the reasoning is the best in the submission.**

I verified both sides. The printed slide at `75:57` — which I read — says **LOW/HOW anchor**.
The spoken instances say **blue tracer** at `[00:49:39]`, `[00:52:09]`, `[00:58:30]`,
`[01:00:20]`, `[01:23:16]`; `[01:16:20]` says **LOW/HOW**; `[01:15:36]` is ambiguous.

**They are genuinely different objects in the lesson's own usage**, and I checked this rather
than accepting it: `LOW/HOW` is the week's extreme (`[01:14:06]`); the tracer is a per-**day**
object (`[01:19:45]` *"there's a tracer in here and [it] separates the day"*; `[00:35:40]`
*"they're working the tracer from yesterday"*). A weekly extreme and a daily separator are not
the same price except by coincidence in the week's first day.

**The `D-008` analysis is correct and I would not have reached a different conclusion.** `D-008`
ranks source *classes* by capture reliability. Applying it here would convert "the slide is the
better record of what was **written**" into "the four spoken instances were **errors**" — a
claim about authorial intent that `D-008` does not license and was not written to make. Blending
into *"25–75 pips off the relevant anchor"* would be worse: a composite phrase no source states.

**And the deeper point is right.** `A-079` establishes the tracer may not be a horizontal price
at all. So the majority spoken reading is not merely in conflict with the slide — **it may not
name a measurable quantity.** That cannot be resolved by preferring the slide; preferring the
slide would hide it.

**Neither refusal is over-conservative. Both are the protocol operating as designed.** The
escalation to an owner ruling on printed-vs-spoken (`REVIEW_INDEX` item 83, → 88) is the right
next step: this corpus is slide-heavy and single-speaker from V10 onward, so the class will
recur, and a student session was correct not to legislate it unilaterally.

---

## `Q-011` — THE FABRICATION FINDING, RE-DERIVED AND EXTENDED

**Reviewer verdict: the `diff` result is CONFIRMED exactly — and it makes the "one shared
template" finding STRONGER, not weaker. It is not a new fabrication variant.**

I re-ran the diff myself:

```text
diff 01_Bootcamp1_Wk1_031812_Part1_55mins/RULES.md
     10_Bootcamp1_Wk3_040112_96mins/RULES.md
```

**Six changed lines, all six identifiers**, exactly as recorded: the title's filename, `V01-R001`
→ `V11-R001`, `V01-R002` → `V11-R002`, two `VIDEO_01_SCREENSHOT_…` → `VIDEO_11_…`, and
*"Asian Box Stop Hunt Reversal (Week 1 - Part 1)"* → *"(Week 3)"*. Both files are 69 lines.
**Every other line is byte-identical** — every rule, every `Source: Explicit` label, every
timestamp, every numeric parameter, and the *"None detected within this video"* contradiction
section.

### The reviewer's extension: I measured the whole library

Diffing all 21 quarantined `RULES.md` against V01's, then normalising away only the identifier
tokens and hashing:

| Group | Members | Content |
|---|---|---|
| **A** | V01, V02, V03, V04, V05, V09, **V10**, V11, V12, V13, V14, V15, V21 — **13 files** | identical after identifier substitution |
| **B** | V06, V07, V08 — 3 files | identical to each other |
| **C** | V16, V17, V18, V19, V20 — 5 files | identical to each other; differ from A by ~10 lines of cosmetic rewording (*"the direction of the higher-timeframe trend"* for *"direction of HTF trend"*) plus two added `Exception:` lines |

**Three documents across twenty-one lessons, and thirteen of them — including V10 — are the same
file re-badged.**

### The premise correction, stated plainly

**V10's `RULES.md` is *not* a new fabrication variant.** It is the *same* shared template that
`Q-001`–`Q-010` describe, now demonstrated by exact textual identity rather than inferred from a
normalised hash. The phrase *"by exact diff, not hash"* in the record describes a **stronger
instrument reaching the same conclusion**, not a different conclusion.

**So confidence in the "fabrication is one shared template" finding should go UP.** Q-010
inferred two template families from normalised hashing; the diff proves membership at the byte
level and my library-wide pass reproduces the grouping. There is nothing here that should reduce
confidence in `Q-009`'s conclusion.

**And the submission says this itself, against its own instrument.** Its §4 records that its
*stricter* normaliser called V10's `RULES.md` a **singleton**, while `diff` calls it V01's file —
and concludes *"`Q-010` was right; this session's stricter normalisation was not more rigorous,
it was differently blind."* **A session that publishes the measurement contradicting its own
newer tool, and rules for the older one, is behaving correctly.** The same is true of the
disclosed `EMA = 24` substring-count error (true word-boundary count: **2**), retained rather
than deleted, with the observation that *"a fabrication screen that over-counts in the
fabrication's favour is not a screen."*

### The three substantive `Q-011` claims, checked

| Claim | Reviewer finding |
|---|---|
| `NOTES.md`'s *"Topic Focus: H4 Anchor Analysis, H1 Alignment, M15 Execution"* is **contradicted in terms** | **CONFIRMED.** `[01:13:47]`–`[01:13:56]`: *"people posted in the form… that I'm using multiple time frame analysis. That's what you want to call it. That's fine, **but that's not what we're doing here**."* The fabricated framing is the one thing the lesson goes out of its way to disown. **First of its kind in the register and correctly flagged as the sharpest row** |
| `RULES.md` asserts a stop-loss rule at `[00:18:00]`, `Source: Explicit` | **CONFIRMED FALSE.** `stop loss` = **0** in the whole lesson (my own search); `[00:18:04]` is *"We are not in grade school. I don't need to see your homework…"* |
| `VISUAL_INDEX.md` describes 3 images; 1 exists, and it is the **title card** described as an *"Asian Box accumulation range with 5, 13, 50, 200 and 800 EMAs"* | **CONFIRMED.** Second instance of `Q-010`'s sixth failure mode. `800` = 0 and `EMA` = 2 in the lesson. **The only screen that catches this is opening the image**, which is the correct conclusion to draw |

---

## CHART RECOGNITION · POSITIVE / NEGATIVE / BORDERLINE EXAMPLES

**Grade: PASS on the lesson's own examples; recognition itself remains `D-030`-blocked.**

No student classification of an unseen chart exists in this round, and **that is correct rather
than a gap** — classifying would require inventing `blue box`, `second leg` and the lock
threshold. What the submission does capture is the lesson's **own** discriminations, and I
verified each against the transcript:

| Example | Type | Verified |
|---|---|---|
| `[00:23:08]`–`[00:23:34]` — *"some of you took this right here and it is a valid M. Absolutely. But… the reason the red box didn't work out is because the timing"* | **A valid pattern that lost, on timing** | ✅ **The corpus's cleanest separation of rule application from outcome** (`REVIEW_PROTOCOL.md` §I), and it comes from the lesson itself |
| `[01:01:38]`–`[01:01:53]`, frame `67:52` — *"He does **not** make a visible stop hunt… because he doesn't exploit the Asian range"* | **Negative example in the instructor's voice** | ✅ Genuine near-miss, not a straw man: the setup is otherwise present and fails on one stated condition |
| `[01:08:30]` — *"this is a **no-go**, do not fall for that"* | Rejection | ✅ |
| `[01:20:47]`–`[01:21:06]` — an M that must **not** be taken because *"he could continue to rise from here… this is DNC"* | **Lookalike rejected for the correct reason** | ✅ The rejection reason is *position relative to the peak*, which is the lesson's stated discriminator — not an outcome |
| `[01:21:48]`–`[01:22:04]` — *"How do I know to take the W and not the M?… trading in line with the peak"* | Discrimination rule | ✅ |
| `[01:09:21]`–`[01:09:29]` — the instructor's own entry that *"had to take a little heat"* | Disclosed imperfect trade | ✅ Correctly captured rather than omitted |

**No credit was given anywhere for a chart that merely became profitable, and no classification
in any V10 artifact depends on later price action.**

## BLIND RECOGNITION TEST

| Chart | Student classification | Correct? | Notes |
|---|---|---|---|
| — | **Not attempted** | **N/A** | Correctly not attempted. `REVIEW_PROTOCOL.md` §M values correct uncertainty; a session that cannot define the setup should not classify charts against it. Attempting it would have been the finding |

## TEACH-BACK ASSESSMENT

**PASS.** Against `REVIEW_PROTOCOL.md` §L's nine points, the submission can state: what the
safety trade is (`§6a`–`6c`); why it matters (the designated signature trade); what comes before
it (weekly extreme, lock, level-one consolidation); what confirms it (second leg M or W, visible
stop hunt); what invalidates it — **and here it correctly answers *"the lesson does not say"***;
what it is confused with (the DNC counter-trade, which the lesson spends five minutes on); known
exceptions (*"obvious ones are still valid"*, the strict novice variant); how it appears on
GBP/USD (frame `83:42`, the instructor's own GBP/USD example); and what remains subjective (four
new `A-xxx` records).

**The refusals are the evidence of understanding, not the gaps in it.** Answering *"what
invalidates it"* with *"the lesson supplies no invalidation price, and the only non-target exit
is a holding period stated five different ways"* is a better demonstration of mastery than any
confident answer available from this source.

---

## STUDENT MASTERY ASSESSMENT

Independent judgement, not an echo.

| Dimension | Student said | Reviewer assessment |
|---|---|---|
| **A. Recall** | SATISFIED | **SATISFIED.** 15 sections, marker-cited; fifteen spot-checked quotations resolve verbatim. **I adopt the submission's own discount of the 12/12** — it is weak evidence and it says so |
| **B. Recognition** | NOT SATISFIED, `D-030`-blocked, no severity charge | **AGREED — NOT SATISFIED, `D-030`-BLOCKED, NO SEVERITY CHARGE. Sixth consecutive lesson; standard treatment.** V10 *improves* the position by supplying the anchor and does not unblock it, because the anchor is retrospective and the lock has no threshold. Scoring it rather than carving it out is the right call — a waiver would hide accumulating debt that `D-030` is deliberately allowing to accumulate. **Open item 36 escalated a sixth time; this still needs an owner ruling and a reviewer cannot supply one** |
| **C. Discrimination** | SATISFIED | **SATISFIED** — verified above; the lesson's own valid-but-lost M is the strongest item |
| **D. Sequence** | SATISFIED | **SATISFIED.** Rules recorded in printed order, spoken markers beside each, both passes agreeing; the lesson's own priority ordering quoted rather than reordered; `[01:26:39]` *"Sunday is not day one"* captured with its counter-intuitive origin |
| **E. Exceptions** | SATISFIED | **SATISFIED**, and the strongest evidence is that two qualifiers were carried **into the backtest** where dropping them would have been convenient |
| **F. Homework** | SATISFIED with one DEFERRED | **SATISFIED.** H2's `DEFERRED` classification is argued from `D-019`'s own test and is correct. Four of ten anchors re-derived exactly |
| **G. Manual backtesting** | SATISFIED | **SATISFIED. Every figure re-derived independently and every figure matched.** All 14 procedural checks and all six `D-026`/`D-027` checks pass |
| **H. Provenance** | SATISFIED | **SATISFIED.** Zero orphan rules found; four frames opened and read; burned-timecode referencing followed from the start |
| **I. Ambiguity** | SATISFIED | **SATISFIED.** Four new records, all `DO NOT CODE`; `A-010` narrowed on Tier 1 evidence alone; no constant proposed for anything left subjective |
| **J. Contradictions** | SATISFIED | **SATISFIED.** Two conflicts found, both tidy reconciliations refused in writing with reasons. `M4` asks for one addition to `C-016`, which strengthens it |

---

## ALL FINDINGS BY SEVERITY

| # | Severity | Code | Finding | Required action |
|---|---|---|---|---|
| **M1** | **MINOR** | `E20` | **`REVIEW_INDEX.md` OPEN-ITEM IDENTIFIER COLLISION — and it must be resolved before merge-back, not after.** `video/v10` allocates open items **81, 82, 83, 84, 85**. The integration branch concurrently allocated **81, 82, 83** to **V09 R2** (`7b42156`, merged at `310362c`), after `video/v10` branched at `5db04d8`. On merge the register holds two different items numbered 81, 82 and 83. **Already load-bearing:** `04_SCREENSHOTS/V10/INDEX.md` § ESCALATION and `V10_MASTERY_REPORT.md` escalation 2 both cite *"open item 82"* for the recipe defect, while integration's 82 is a **closed** V09 frame-ordinal fix. **Not the student's fault alone — it is a policy gap.** `D-038a`'s safety evidence re-derived `A-`, `C-` and `Q-` identifier sets after merge and found no duplicates; **it did not check `REVIEW_INDEX` open-item numbers**, which are the one append-only series that is *not* mergeable by construction. The session *did* apply the discipline where the policy names it (`PT-036` §0 explicitly allocates against post-merge integration state) | **Renumber V10's five items to 86–90 in `REVIEW_INDEX.md`, with the renumbering disclosed in place**, and update the two citing artifacts. **Discharged by this reviewer at merge-back** — see REQUIRED CORRECTIONS 1. **Additionally escalate the policy gap** as a new open item |
| **M2** | **MINOR** | `E20` | **`A-078` / `C-017` undercount the spoken renderings by at least one, in the direction that STRENGTHENS the finding.** `A-078` heads *"spoken six times"* and tabulates six markers; `C-017` says *"four of six spoken instances say the tracer."* **`[01:00:20]` — *"75 pips off of the blue tracer"* — is a seventh spoken instance and it names the tracer.** The correct census is **five of seven** spoken instances naming the blue tracer, one naming the LOW/HOW anchor, one ambiguous. (`[00:54:02]`'s *"25 to 50 pips"* is an eighth distance utterance in the safety-trade walkthrough, with no reference object named.) `A-079`'s separate *"named 13 times"* headline **is correct** — `tracer` occurs 13 times, `blue tracer` 10 | **Correct the counts in `A-078`, `C-017`, `V10_MASTERY_REPORT.md` §J and the `REVIEW_INDEX` item text.** Edit, not redo — **no conclusion moves, and the correction makes the majority reading stronger** |
| **M3** | **MINOR** | `E20` | **`V10_SOURCE_NOTES.md` §15's absence claim is overstated as written.** It reads *"No session clock times. Sessions are named constantly; **no hour is ever stated**."* Hours **are** stated: `[00:02:24]` *"at 830"*, `[00:05:09]` *"seven o'clock New York time"*, `[00:42:52]` *"3 o'clock in the morning"*, `[01:03:57]` *"5 6 o'clock at night"*. **None is a session boundary — which is the point being made and which is true** — but the sentence as written is falsifiable by a one-line grep, and a later session reading it would take a stronger absence than the evidence supports. Charged because §15 exists precisely so a later session can rely on it. **`Q-011` §1's version of the same claim is precise** (it names six specific clock figures from `NOTES.md` and reports six zeroes); only the summary prose overshoots | **Reword §15 to *"No session-boundary clock time is stated. Clock times occur only incidentally (`[00:02:24]`, `[00:05:09]`, `[00:42:52]`, `[01:03:57]`) and none delimits a session."*** Edit, not redo. Check `A-076`'s parallel sentence for the same overshoot |
| **M4** | **MINOR** | `E20` | **`C-016` does not apply the transcript's own ASR caution to its own evidence.** The transcript header's TRANSCRIPTION NOTE 1 records that *"numeric ranges wobble, and one of them is load-bearing"* and rates the file `MEDIUM–HIGH`. `C-016` rests entirely on two ASR-rendered numbers two seconds apart, **neither printed on any slide**, and argues from them as though capture were certain. This is inconsistent with the same session's (correct) treatment of `A-078`, where ASR unreliability on numbers is the express reason to prefer the slide. **The omission strengthens nothing and undermines nothing in the disposition — it is an additional independent reason to refuse reconciliation** | **Add a caveat block to `C-016`** stating that both figures are ASR-rendered and unprinted, citing TRANSCRIPTION NOTE 1, and that this is a **further** reason the record stays `UNRESOLVED`. Edit, not redo |
| **N1** | **NOTE** | — | **Speaker strand 2's characterisation is imprecise, though its conclusion is not.** *"Every one of the 13 `Steve` tokens is vocative or self-quoting"*, glossed as *"he voices students addressing him"*. Three tokens are grammatically **third-person**: `[00:35:53]` *"Why does Steve have this stupid little blue line"*, `[01:05:39]` *"Pretty sure Steve told me that…"*, `[01:08:39]` *"…you're going with Steve"* (probably an ASR garble). All three sit **inside voiced student speech** and two are immediately answered in the first person, so the evidential force is intact. **The accurate statement is: no token is the speaker referring to an absent Steve in his own narrative voice.** Worth tightening because it is the round's most consequential claim; **no action required and the determination is unaffected** |
| **N2** | **NOTE** | — | **`[00:01:33]`'s *"trailing stops"* is omitted from §15 and would strengthen it.** The only stop-management concept in 96 minutes is the speaker declining to discuss it: *"Hold the questions that about trailing stops and other things that are not pertinent."* **Active deferral is stronger evidence than mere absence.** Recommended addition to §15 and to `C-016`'s consequence paragraph |
| **N3** | **NOTE** | — | **Arm B is worse for `M2` than the headline figure, and the submission headlines the weaker arm.** `BT_V10_0001` §3 quotes *"Friday ranks fourth of five"* — correct for arm A. **On arm B Friday ranks FIFTH of five** (5.62%, below Wednesday's 6.18%), which I re-derived. The arm-B *magnitude* (−8.91 pp) **is** reported and the arm-A rank **is** correctly labelled, so there is no favourable-arm selection — the opposite. Noted only because the stronger result against the claim is the one not headlined |
| **N4** | **NOTE** | — | **The runner's pre-execution crash-fix is correctly classified, verified against the diff.** `git show 2856631 -- run_pt036.py` confines the change to session-day labelling. No threshold, seed, exclusion, prediction or estimand moved. The `COMMON_PROTOCOL.md` §9 rule 7 reasoning — that rule 7 governs disagreements found *after a result exists*, and none existed — **holds** |
| **N5** | **NOTE** | — | **Open item 80's censoring bias: the design-out is genuine and the verification is real.** `PT-036` has no barrier race and no expiring horizon; `censored = 0` is not merely observed but **enforced as a hard assert that would have voided both measures.** Independently confirmed: every completed week has a high, a low and a Friday close, so `n_resolved == n` by construction. **This supports R1's narrowed scope for item 80 and does not close it** |
| **N6** | **NOTE** | — | **`SWF_CAPTURE_RECIPE.md` §10's frame-rate defect is REAL, and V10's own capture was NOT harmed.** See the dedicated section below. The escalate-don't-patch handling was correct under `D-038a` |

| **N7** | **NOTE** | — | **`COURSE_PROGRESS.md`'s PROGRESS TABLE is stale — for V10 and for four earlier lessons.** The student session updated the file's STATUS prose block at `e5262b2` but left the table's V10 row reading `NOT STARTED` with every artifact column `⬜`. **Not charged as a fifth MINOR, because the decay is systemic and pre-dates V10:** the same table reads `AWAITING REVIEW R1` for V06, V07 and V09 (V06 and V07 are `COMPLETE`) and `IN REMEDIATION` for V08 (also `COMPLETE`). **The prose block is maintained; the table is not.** V10's row corrected by this reviewer; the other four need a sweep — open item **96** |

**Severity totals for this round: 0 CRITICAL · 0 MAJOR · 4 MINOR · 7 NOTE.**

---

## THE `SWF_CAPTURE_RECIPE.md` §10 DEFECT — ADJUDICATED AND FIXED

**Reviewer verdict: a REAL documentation bug. The escalation was correct. Fixed by this reviewer
on the integration branch under `D-038a`.**

### It is real — verified by reading §10

`00_SYSTEM/SWF_CAPTURE_RECIPE.md` §10 states the header table as:

```text
V01: frameRate=3.0, frameCount=9853,  at body offset 17
V02: frameRate=3.0, frameCount=10861, at body offset 17
```

then instructs, in prose, **"Patch 3.0 → 30.0 fps"**, and its measured-speedup table labels its
control column **"3 fps control"**. Every instance reads as if 3.0 were the library's rate.
**V10's header declares 2.0** — independently corroborated by three agreeing figures in the
transcript header (11,553 frames ÷ 2.0 = 5776.5 s; audio 5776.222 s; manifest 5776 s).

### The consequence, worked through

A session following §10 literally on V10 patches 2.0 → 30.0, which is **15×, not 10×**. The
sweep loop uses `STEP_MS = STEP_PRES*1000/SPEED` with `SPEED = 10`, so screenshots land every
500 ms of wall clock — **7.5 presentation-seconds apart instead of 5.** The result is a complete,
well-formed, correctly-timecoded frame set that **under-samples the screen-state detector by a
third**, and the surplus loop iterations capture post-film end state. **Nothing fails loudly.**
This is the same family as `GOTCHA 4` and `GOTCHA 5`: a header field that varies across the
library, quoted in the recipe as a constant.

### Was V10's capture actually harmed? **NO — and I checked rather than assumed.**

The student read the header first (as `GOTCHA 5` instructs), found 2.0, and patched 2.0 → 20.0.
The arithmetic confirms it: the sweep produced **1,164 frames at 5 presentation-seconds**, and
5776.2 / 5 + 8 = **1,163**. A 15× sweep would have produced the same count at 7.5-second
spacing and the detector would have seen ~776 distinct sample points, not 1,164. **The capture
ran at the correct speed and the 32 curated frames are sound** — I opened four of them and every
burned timecode read exactly as indexed.

**So the defect is latent, not realised. That does not make it less worth fixing** — it was
avoided by a session that happened to follow `GOTCHA 5`'s advice rather than §10's prose, which
is precisely the kind of luck a recipe should not depend on.

### The handling was correct

`SWF_CAPTURE_RECIPE.md` is a **POLICY ledger** under `D-038a` and must not be edited from a task
branch. The student escalated and did not patch, citing the V09 `GOTCHA 5` precedent. **That is
right**, and it is the second consecutive lesson to get this boundary correct.

**Fix applied by this reviewer on the integration branch**, per the review scope: §10's header
table is relabelled *"Measured examples — data points, NOT the library's constant"* and gains
V10's 2.0 row with its three-way duration cross-check; a warning block states **THE RULE — read
`frameRate` from the header of the file you are about to capture and patch `rate × SPEED`, never
type a literal**; the prose becomes *"Patch `declared_rate × 10`"* with the superseded sentence
retained per `REMEDIATION_PROTOCOL.md` §2; the speedup table's control column is labelled as
V02's declared rate; and the sweep snippet derives `PATCH_FPS` from `DECLARED_FPS`. **See open
item 87 (formerly 82), now `CLOSED`.**

---

## ⭐ EVIDENCE THAT ARRIVED AT THE MERGE — AND IT WIDENS `M1`

**The `review/v10` → integration merge CONFLICTED in three files**, and every one of them is an
evidence ledger that `D-038a` classifies as *"append-only and `git`-mergeable by construction"*:

| File | Conflict hunks | What collided |
|---|---|---|
| `18_REVIEW/REVIEW_INDEX.md` | **3** | the `STATUS` block, the `DECISION TABLE` tail, the `OPEN RESEARCH ITEMS` tail |
| `LOG.md` | **2** | two session entries appended at the same tail |
| `00_SYSTEM/COURSE_PROGRESS.md` | **1** | the `STATUS` block |

**They are not mergeable by construction.** Both branches appended to the tail of the same
tables and status blocks, so git had no way to order them. `LOG.md`'s conflict was the worst of
the three: it **interleaved two session entries**, splicing the V09 R2 entry's Decision, Files,
Git and Next-Action sections into the middle of the V10 R1 entry's fenced Decision block. All
were resolved by hand and the repair is disclosed here rather than absorbed.

**This is measured evidence, not argument, and it widens `M1` from a numbering rule into a
question about how concurrent sessions append to shared ledgers at all.** `D-038a`'s safety
evidence was the `video/v08`/`review/v08` merge, which it reported as *"no conflict, no
duplication, no overwrite"* — that merge happened to have no concurrent second writer on the
same tails. **This one did, and the premise failed in three files simultaneously.** Carried on
open item **91**.

---

## REQUIRED CORRECTIONS

**Redo vs edit:** every correction below is an **EDIT**. No underlying test is invalid, so
nothing requires redoing (`REMEDIATION_PROTOCOL.md` §2). **No V10 measurement, classification or
disposition changes as a result of any of them.**

1. **`M1` — resolve the open-item collision. DISCHARGED BY THIS REVIEWER at merge-back**, because
   a collision only becomes concrete on merge and merge-back is a single-threaded act this
   session is performing. V10's items **81–85 are renumbered 86–90** in `REVIEW_INDEX.md`, with
   the renumbering disclosed in place and the old numbers retained as cross-references.
   **Still owed by the student:** update the two artifacts that cite the old numbers —
   `04_SCREENSHOTS/V10/INDEX.md` § ESCALATION and `07_MASTERY_REPORTS/V10_MASTERY_REPORT.md`
   escalation 2 — to cite **item 87** rather than *"open item 82"*.
2. **`M2` — correct the spoken-rendering census.** In `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md`
   `A-078`, change the heading *"spoken six times in four renderings"* and add the row
   `[01:00:20]` *"75 pips off of the blue tracer"*. In `11_CONTRADICTIONS/CONTRADICTIONS.md`
   `C-017`, change *"Four spoken instances say the tracer"* to **five of seven** and add the same
   row to its table. Mirror the count in `V10_MASTERY_REPORT.md` §J. Optionally record
   `[00:54:02]`'s *"25 to 50 pips"* as an eighth distance utterance with no reference object.
3. **`M3` — reword `V10_SOURCE_NOTES.md` §15.** Replace *"No session clock times. Sessions are
   named constantly; no hour is ever stated"* with a claim scoped to session boundaries, listing
   the four incidental clock times as the reason for the scoping. Check `A-076`'s sentence
   *"V10 states no clock time for any session"* — that one is **correct as written** because it
   is scoped to sessions, and it should stay as the model.
4. **`M4` — add the ASR caveat to `C-016`.** State that both figures are ASR-rendered, neither is
   printed, and TRANSCRIPTION NOTE 1 records numeric wobble in this file — **as a further
   independent reason the record stays `UNRESOLVED`**, not as a weakening of it.
5. **Recommended, not required (`N1`, `N2`):** tighten speaker strand 2's wording to *"no token
   is the speaker referring to an absent Steve in his own narrative voice"*, and add
   `[00:01:33]`'s deferred *"trailing stops"* to §15's no-stop-loss finding.

---

## REVIEWER QUESTIONS

1. **`C-016`:** does the project want a standing convention that a contradiction resting solely
   on ASR-rendered numbers, with no printed corroboration, is tagged as such at filing? Three
   such records now exist across the corpus.
2. **`M1`'s policy half:** should `D-038a` acquire an explicit consequence that
   **`REVIEW_INDEX.md` open-item numbers must be allocated against the integration branch's
   state**, as `PT-036` §0 already does for `PT` numbers? This is the one append-only series in
   the evidence-ledger list that is not mergeable by construction.
3. **`PT-037`:** the path-length reading is recorded as recommended-not-owed. Does the owner
   want it pre-registered and run, given that its textual objection (*"peak formation high **to**
   peak formation low"* names two points, i.e. a range) is already strong against it?

---

## HUMAN REVIEW

```text
HUMAN REVIEW REQUIRED: no
```

Audio quality was adequate, the load-bearing slides are legible at committed resolution and were
read directly, no instructor language required an arbitrary judgement to interpret, and where
two readings materially diverge (`C-016`, `C-017`) **both are correctly recorded as
`UNRESOLVED` rather than forced.**

**Three items nonetheless await an OWNER ruling** — none of them a defect in V10, all of them
gaps in the project's own standards: open item 36 (a disposition for `D-030`-blocked
dimensions, sixth escalation), item 88 (formerly 83 — printed-vs-spoken precedence), and
reviewer question 2 above.

---

## ADVANCEMENT DECISION

```text
LESSON: V10
DECISION: REVISE
CONFIDENCE: HIGH

CRITICAL ISSUES:
- None.

MAJOR ISSUES:
- None.

REQUIRED ACTIONS:
1. M1 - open-item ID collision 81/82/83 against V09 R2. Renumbered to 86-90 by
   this reviewer at merge-back; the student still owes the citation updates in
   04_SCREENSHOTS/V10/INDEX.md and V10_MASTERY_REPORT.md.
2. M2 - correct A-078 / C-017 / mastery §J: the spoken census is five of seven,
   not four of six. [01:00:20] is the missing instance and it says "blue tracer".
3. M3 - reword V10_SOURCE_NOTES.md §15's "no hour is ever stated" to a claim
   scoped to session boundaries.
4. M4 - add the ASR caveat to C-016 as a further reason for UNRESOLVED.

ADVANCEMENT:
AUTHORIZED. 0 CRITICAL / 0 MAJOR opens the V11 gate under D-024. The four
minors are carried in REVIEW_INDEX.md and are still owed before V10 can reach
COMPLETE. V10 is NOT COMPLETE.
```

---

## REVIEWER'S SUMMARY JUDGEMENT

**This is the strongest submission the corpus has received.**

The reasons are specific and each was verified rather than accepted. Nine printed rules and two
load-bearing slide texts transcribed without a single substitution, including three typographic
infelicities a tidying pass would have removed. Two backtest measures whose every figure —
median, percentiles, both arms, both nulls, the weekday table, the unit-error check —
reproduced exactly under independently written code. A fabrication `diff` that reproduces
exactly and extends cleanly library-wide. A host-vs-guest determination that is over-determined
and, more importantly, **architected so that nothing depends on it being right.**

But the thing that most deserves recording is what the submission **declined** to do. It
declined to test the lesson's headline trade, naming the exact lookahead mechanism that would
have produced a flattering number. It declined two tidy reconciliations that were available and
would have made the record look tidier. It declined to run an unregistered alternative after
seeing a failure. It declined to code two numbers that are stated *and printed*, on the ground
that a target without a defined trigger is not a rule. It pre-registered the diagnostic that
would otherwise have become a post-hoc rescue, and reported that the rescue fails too. And it
argued its own perfect comprehension score and its own 6/6 prediction tally **down**, in
writing, naming the mechanisms that inflate them.

`REVIEW_PROTOCOL.md` §17 lists five failure modes the reviewer exists to prevent. This
submission does not merely avoid all five — it names four of them by number, against its own
interest, in the places where it would have been easiest to commit them.

The four minors are documentation and register hygiene. **Not one of them moves a measurement, a
classification, a disposition or a rule.** `M1` is the only one with teeth, and its teeth are
procedural: it must be resolved before merge or the register acquires three duplicate
identifiers — and half of it is a gap in `D-038a`, not in this session's work.

**Would I let real-money execution eventually depend on this interpretation?** For what V10
actually establishes — the anchor definition and the two failed context claims — **yes.** For
the safety trade, **no, and the submission says so first, at greater length than I would have,
and is right.**

---

## REVIEWER SELF-CHECK

- [x] I inspected source evidence before the student's conclusions — the full 3,557-line
      transcript body and four frames were read before any student artifact was opened
- [x] I did not assume polish equals correctness — every quantitative claim was re-derived, and
      the two slides most relied upon were read pixel-by-pixel
- [x] I attempted to falsify the student's rules, not to confirm them — I searched specifically
      for a guest-impersonation reading, for a favourable-arm selection in `M2`, for motivated
      reasoning in `A-078`'s split application of `D-008`, and for a post-hoc rescue in `O2`
- [x] I did not import external trading frameworks
- [x] I did not invent a resolution where evidence was insufficient — `C-016` and `C-017` remain
      `UNRESOLVED` and I state that I would not have reached a different conclusion
- [x] I did not manufacture objections to appear rigorous — `REVIEW_PROTOCOL.md` §1 cuts both
      ways, and this round's honest finding count is four minors, one of which is half a policy
      gap
- [x] Every required correction is specific enough to act on — each names a file, a sentence and
      a replacement
- [x] Would I let real-money execution eventually depend on this interpretation? — answered
      above, scoped
