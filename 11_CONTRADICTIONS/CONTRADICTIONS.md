# CONTRADICTIONS

Conflicting teachings found within the course.

Template: `00_SYSTEM/TEMPLATES/CONTRADICTION_TEMPLATE.md`

---

## STATUS

```text
RECORDS:         5   (C-001 … C-005)
LESSONS STUDIED: 4   (V01, V02 reviewed R3: PASS; V03 REVISE R1 minors-only;
                      V04 not yet reviewed)
UNRESOLVED:      4   (C-001 foundational; C-003; C-004; C-005)
RESOLVED/OTHER:  1   (C-002 — STATED EXCEPTION, condition unmeasurable)
```

> **UPDATED 2026-08-10 (review R1, finding 6b).** This block previously read
> `RECORDS: 0` and *"**Intentionally empty.** No course material has been studied, so no
> course contradiction has been observed."* Both statements were true at project start
> and are now false. Corrected so the status does not contradict the file's own contents.
>
> **UPDATED again 2026-08-10 (review R3).** The R1 correction read `RECORDS: 2 /
> LESSONS STUDIED: 1`, accurate when written and stale the moment the V02 pass added
> `C-003` and `C-004`. Same staleness class (`E20`), same file, second occurrence. The
> counts above are arithmetic over the records the file contains.
>
> **UPDATED again 2026-08-10 (V02 review R1, finding 4).** `UNRESOLVED` read `1 (C-001)`
> while the INDEX below showed **three** `UNRESOLVED` records — C-001, C-003 and C-004.
> Introduced by the R3 edit that was itself correcting this same block. **This is the
> fourth occurrence of this staleness class in this one file**, so the cause is now
> treated as structural rather than as four separate slips: the STATUS block duplicates
> information that already exists in the INDEX table, and a hand-maintained duplicate of
> a growing table goes stale by default.
>
> **Standing rule adopted:** every value in this STATUS block is arithmetic over the
> INDEX table immediately below, and **the INDEX is the authority**. Any session touching
> this file recounts the block from the INDEX rather than incrementing it from memory. If
> the two ever disagree again, the INDEX wins and the block is the defect.
>
> **UPDATED again 2026-08-10 (V03 pass).** Recounted from the INDEX per the standing
> rule above. The V03 pass added evidence to all four records and opened none, so only
> `LESSONS STUDIED` moved (2 → 3); the V02 review state is also refreshed from R1 to its
> final R3 `PASS`. Record counts are unchanged and were re-derived, not assumed.
>
> **UPDATED again 2026-08-10 (V04 pass).** Recounted from the INDEX per the standing rule.
> The V04 pass **opens `C-005`** (two presenters teaching different entry systems inside
> one lesson) and adds evidence to `C-001` and `C-004` without resolving either. Updated
> in the same commit that added the record.

`C-001` and `C-002` are **intra-lesson** contradictions within V01, and both originate
with the instructor rather than with the reading of him. `C-001` (how long price runs away from
the anchor point) is foundational and `UNRESOLVED` — the instructor was challenged on it
at `[00:36:07]`, conceded at `[00:36:13]`, and moved on. Review R1 ruled that it does
**not** justify `BLOCKED`, since no further work on V01 can resolve what the recording
does not say; it travels forward as an open research item with no day-count value
committed anywhere.

> Infrastructure conflicts — including disagreements between the two governing
> agent files — are **not** recorded here. They belong in
> `00_SYSTEM/SETUP_ISSUES.md`. This file is exclusively about the Market Maker
> Method as taught.

---

## PURPOSE

**Never silently reconcile conflicting teachings.**

When lesson 3 and lesson 9 appear to disagree, the tempting move is to pick the
reading that makes the corpus tidy. That invents a rule the instructor never
taught, and the invention is untraceable afterwards.

A contradiction may turn out to be:

- a timeframe difference,
- a market-phase difference,
- a setup-subtype difference,
- a later lesson refining an earlier one,
- an instrument difference,
- a context difference,
- a stated exception,
- instructor shorthand,
- or a genuine inconsistency in the course.

All nine are worth knowing. Collapsing them into a guess destroys that information.

---

## RESOLUTION STATES

| Status | Meaning |
|---|---|
| `UNRESOLVED` | No evidence yet distinguishes the readings. **Default, and often the correct end state during the Student Phase.** |
| `PROVISIONAL` | A working interpretation is adopted with evidence, flagged for confirmation. Must not be written into the concept library as fact. |
| `RESOLVED` | Later course material settles it. Cite the resolving evidence. |
| `HUMAN REVIEW REQUIRED` | Two plausible readings materially change trading logic. |

A **foundational** unresolved contradiction may justify a reviewer `BLOCKED`. A
non-foundational one may permit `PASS` with an open research item carried in
`18_REVIEW/REVIEW_INDEX.md`.

---

## REVIEW CADENCE

Re-examine every open contradiction at each cumulative checkpoint (25/50/75/100%).
Later lessons frequently resolve earlier conflicts — and occasionally create new
ones that are invisible within any single lesson.

An ignored contradiction is reviewer error code E13.

---

## INDEX

| ID | Concept | Sources | Status | Foundational? |
|---|---|---|---|---|
| C-001 | How long price runs away from the anchor point | V01 `[00:35:05]` vs V01 `[00:35:15]` / `[00:35:55]` | UNRESOLVED | **Yes** |
| C-002 | Whether the trading-zone / blue-box filter and the one-direction rule are mandatory | V01 `[00:44:15]` / `[00:51:22]` vs V01 `[00:44:03]` / `[00:51:34]` | STATED EXCEPTION — condition unmeasurable | No, but blocking for implementation |
| C-003 | Whether M and W formations can fail | V02 `[00:38:40]` vs V02 `[00:38:40]` (same sentence) | UNRESOLVED — self-contradictory as spoken | No |
| C-004 | London session open — 3:30am printed vs 4:00 spoken | V02 slide `[00:45:55]` vs V02 `[00:50:32]` | UNRESOLVED — daylight-saving explanation plausible but unstated | No, but blocking for any time-gated rule |
| C-005 | Instructor vs guest presenter — different entry gate, session, second-leg dependence and stop reference, in one lesson | V04 `[00:15:34]`–`[00:15:57]` (instructor) vs V04 `[01:13:34]`–`[01:14:18]` (guest) | UNRESOLVED as corpus hygiene. **Scope ruling made 2026-08-11 — `D-025`**: guest material is secondary DESCRIPTIVE evidence, excluded as NORMATIVE doctrine | No on the method; **yes on corpus hygiene** |

---

## RECORDS

## C-001 — Duration of the move away from the anchor point

### Concept

How many days price continues away from the anchor point once the anchor is
established. This sets the holding period for every weekly-cycle trade.

### Source A

| Field | Value |
|---|---|
| Video | V01 |
| Timestamp | `[00:35:05]` |
| Screenshot | None — I-006 |
| What is said/shown | "Now you know one thing **for sure**. If the anchor point is in place, you trade away from the anchor for **two and a half to three more days**." |

### Source B

| Field | Value |
|---|---|
| Video | V01 |
| Timestamp | `[00:35:15]`, `[00:35:55]` |
| Screenshot | None — I-006 |
| What is said/shown | `[00:35:15]` "if the anchor point comes in on a Tuesday, it is **likely** that they will rise for what's perceived as **four days, three and a half days, three days**." `[00:35:55]` "if the dealer anchors in on Tuesday and rises Tuesday, [Asian] session, half a day, he'll rise Wednesday, Thursday and **complete the cycle on Friday**." |

### Conflict

Source A gives 2.5–3 days and asserts it as certain. Source B, ten seconds later,
gives a three-value range topping out at 4 days and hedges it as "likely". Source B's
worked Tuesday example spans Tuesday-half through Friday — roughly 3.5 days —
which is inside B's range and outside A's.

These cannot both be stated certainties about the same quantity. Either the "for
sure" in A is loose speech, or A and B are describing different things that the
lesson does not distinguish.

**The instructor is aware of the conflict and does not resolve it.** At `[00:36:07]`
he quotes students back at himself — "Steve, you said three days, three levels. Four
days or three and a half days, everyone['s] counting. It's more than what I've told
you. I understand that." He then moves to a different point at `[00:36:38]`. This is
a source-level inconsistency, not a transcription artifact.

### Possible Explanations

| # | Explanation | Supporting evidence | Assessment |
|---|---|---|---|
| 1 | Different timeframe | None. Both statements concern days within one week. | Rejected |
| 2 | Different market phase | None stated. | No evidence |
| 3 | Different setup subtype | None stated. | No evidence |
| 4 | Later lesson refines the earlier one | Not applicable within V01; possible for V02–V21. | **Open — most likely route to resolution** |
| 5 | Different instrument | None. No instrument is attached to either statement. | Rejected |
| 6 | Different context | Partially: A speaks of "trading away from the anchor", B of the market "rising". These may be a trader-side window and a market-side move, which need not be identical — the trade window could reasonably be shorter than the move. **The lesson never says this.** | **Plausible, unstated — do not adopt** |
| 7 | Stated exception | `[00:35:43]` adds "an extra day if it happens to fall on Friday", which extends but does not reconcile. | Partial |
| 8 | Instructor shorthand | `[00:36:13]`–`[00:36:15]` — "It's more than what I've told you. I understand that." — reads as an admission of loose prior teaching. | **Plausible** |
| 9 | Actual inconsistency in the course | The instructor's own acknowledgement at `[00:36:07]`–`[00:36:15]` is direct evidence for this. | **Most strongly supported** |

Explanations 6, 8 and 9 are all live. 6 is the only one that would make both
statements true; it is also the one with no textual support, and adopting it would be
inventing a distinction to make the course consistent. That is exactly the silent
reconciliation this log forbids.

### Resolution

```text
UNRESOLVED
```

**Foundational: yes.** Holding period is a first-order parameter. Any weekly-cycle
rule, backtest, or specification that commits to a day count is committing to one
side of an unresolved conflict.

### Required to resolve

A later lesson stating the day count unambiguously, or — failing that — manual
backtest observation across enough weeks to distinguish the readings empirically.
Note that empirical resolution answers "what the market did", not "what the course
taught"; only the former is available if the course never clarifies.

### Interim handling

`DO NOT CODE` any day count. Where a holding period is needed downstream, carry the
conflict forward explicitly rather than picking a value.

---

## C-002 — Whether the entry filter and direction restriction are mandatory

### Concept

Whether (a) taking only trading-zone / blue-box setups and (b) trading only one
direction after a mid-week anchor are absolute rules or training constraints.

### Source A

| Field | Value |
|---|---|
| Video | V01 |
| Timestamp | `[00:44:15]`, `[00:51:22]` |
| Screenshot | None — I-006 |
| What is said/shown | `[00:44:15]` "if you are struggling… then I need you to take **only** those trades that are established by the proper formation of the trading zone." `[00:51:22]` "**Only** short trades will be warranted." |

### Source B

| Field | Value |
|---|---|
| Video | V01 |
| Timestamp | `[00:44:03]`, `[00:51:34]` |
| Screenshot | None — I-006 |
| What is said/shown | `[00:44:03]` "When you become more experienced… you can start to see that the blue box is **more of a guide**." `[00:51:34]` "When you become more proficient, you can **trade both ways**." |

### Conflict

Both pairs sit within seconds of each other and the instructor plainly intends them
as a strict form for beginners and a relaxed form for the experienced. **This is a
stated exception, not a genuine contradiction** — logged here because the condition
that selects between the two forms is unmeasurable (A-013), so downstream the two
forms are indistinguishable in practice.

### Possible Explanations

| # | Explanation | Supporting evidence | Assessment |
|---|---|---|---|
| 7 | Stated exception | Explicit in both pairs — "when you become more experienced", "when you become more proficient". | **Confirmed** |
| 9 | Actual inconsistency | None. The conditional is stated openly each time. | Rejected |

### Resolution

```text
RESOLVED AS STATED EXCEPTION — CONDITION UNMEASURABLE
```

The course's position is clear. What is missing is any test for which side of the
condition a given trader is on. See A-013.

**Foundational: no** — but blocking for implementation. Any specification must state
which form it encodes, and must record that the course offers both. Encoding the
relaxed form silently would drop a constraint the course places on its stated target
audience; encoding the strict form silently would present a training constraint as
doctrine.

### Interim handling

Encode neither form as unconditional. Carry both, tagged with the skill condition,
until A-013 resolves or is declared permanently unmeasurable.

---

## C-003 — Whether M and W formations can fail

### Concept

Whether the course's core entry formations are presented as reliable, and what a
student is supposed to do when one does not work.

### Source A

| Field | Value |
|---|---|
| Video | V02 |
| Timestamp | `[00:38:40]` |
| What is said | "MRWs will not fail" — ASR for "**M's and W's will not fail**". |

### Source B

| Field | Value |
|---|---|
| Video | V02 |
| Timestamp | `[00:38:40]` — the same sentence |
| What is said | "…**and when they do, cut them quickly and control your loss.**" |

### Conflict

The claim and its refutation are one sentence: *"M's and W's will not fail, and when
they do, cut them quickly and control your loss."*

This is not two statements minutes apart that might be reconciled by context. The
subordinate clause presupposes exactly what the main clause denies.

### Possible Explanations

| # | Explanation | Supporting evidence | Assessment |
|---|---|---|---|
| 1 | Rhetorical emphasis — "will not fail" means "fail rarely" | The immediately preceding passage `[00:38:19]` is about following "a simple set of rules" and being "man enough to admit it… and let your stop trigger and look for the next set up". The whole surrounding paragraph is about handling being wrong. | **Strongly supported.** The context is a lesson about accepting losses, which makes a literal "never fails" reading implausible on its face. |
| 2 | Two different objects — some M/W's fail, canonical ones don't | Nothing stated. Would require a "perfect M/W" category, which the homework at `[00:56:01]` does gesture at ("pick one perfect M and one perfect W"). | **Speculative.** The homework's "perfect" is about selecting good teaching examples, not about a reliability tier. Do not adopt. |
| 3 | Transcription artifact | The phrase is rendered "MRWs", so the ASR is imperfect here. | Partial — but the *structure* of the sentence (claim + "and when they do") is not the kind of thing ASR invents. |
| 4 | Genuine inconsistency in the teaching | The instructor makes several absolute claims in V02 that he softens in the same breath. | Plausible |

### Resolution

```text
UNRESOLVED — but low-stakes, and explanation 1 is strongly favoured
```

This is logged not because the practical guidance is unclear — it is not; he plainly
says to cut losers quickly — but because **"M's and W's will not fail" is exactly the
kind of sentence that gets extracted as a quotable course rule and propagates as a
reliability claim.** The quarantined `RULES.md` files demonstrate how readily this
project's source material generates unsupported confidence assertions. Recording the
contradiction here means any later session that finds the first half of the sentence
also finds the second.

**Foundational: no.** No downstream rule depends on M/W formations being infallible,
and the actionable half of the sentence is unambiguous.

### Required to resolve

A later lesson stating a failure rate, or stating the conditions under which an M or W
is expected to fail.

### Interim handling

**Do not record "M's and W's will not fail" as a course claim without its second
clause.** Where a reliability figure is needed downstream, note that the course offers
none — the only number in this vicinity is the Zaireen backtest hit rate at V02
`[00:37:37]`, which the instructor retracts as he says it.

---

## V02 EVIDENCE ADDED TO C-001

C-001 (duration of the move away from the anchor point) listed *"a later lesson
refines the earlier one"* as explanation 4, and identified it as the **most likely
route to resolution**. V02 is the next lesson. It does not resolve it.

| Video | Timestamp | What is said |
|---|---|---|
| V02 | `[00:05:30]` | "I know it's **not always three days**… It could be **four days**. It could be **two and a half days**." |
| V02 | `[00:16:15]` | "The objective is to stay above/below the perceived support or resistance level for **at least three days**, causing exhaustion and panic." |
| V02 | `[00:16:23]` | "The dealer's job is to not cross that level for **two and a half to three days or four days**." |
| V02 | `[00:17:09]` | "The dealer will not cross the level for **two and a half to three or four days**." |

`[00:16:15]` and `[00:16:23]` are eight seconds apart and give incompatible lower
bounds — "at least three" against "two and a half".

**Effect on C-001:** none of the ambiguity is removed, and one thing is added — V02
shows the same spread (2.5 / 3 / 4) recurring in a second lesson, which makes
explanation 8 ("instructor shorthand") and explanation 9 ("actual inconsistency in the
course") more likely, and explanation 4 ("a later lesson refines it") less likely. The
range appears to be how the course talks about this quantity, not a slip in V01.

C-001 remains `UNRESOLVED` and remains foundational. Re-test at V03.

### Chart datum from V02 homework 11a — recorded, NOT counted as support

**Added 2026-08-10 during V02 R1 remediation.** This entry exists so the datum is not
lost. It is **not** evidence for or against any day count, and nothing anywhere may cite
it as such.

The V02 homework markup (`05_HOMEWORK/V02/V02_HOMEWORK.md` §1) originally stated that a
real USD/CHF week held away from the Monday high *"Tuesday through Thursday — about three
days — consistent with the printed 'For At Least 3 Days'"*. **That statement was false and
is withdrawn** (V02 review R1, MAJOR 1): the markup had misread the chart, and price
traded back *above* the Monday high on Thursday.

The chart has since been re-measured from the committed PNG (method: `V02_HOMEWORK.md`
§1.1; ±0.5 pip, ~~self-validating on day boundaries~~ **day boundaries taken from the
chart's own dotted separators — corrected 2026-08-10, V02 review R2 Minor 1; the earlier
"self-validating" description was wrong, see below**). The corrected measurement:

| | |
|---|---|
| Level taken | Mon 3 Aug 2026 high, **0.81151**, set `15:00` UTC |
| First hourly bar above it | Thu 6 Aug 2026 `15:00` UTC, high **0.81356** |
| Elapsed | **72 hours = exactly 3.00 days** |

**Why this resolves nothing.** The same price series yields 2, 3 or 3 days depending on
the counting convention used (hours elapsed / whole days closing below / days to the first
daily close above) — and *the counting convention is exactly what C-001 is a contradiction
about*. A week landing on precisely 72 hours can be read into or out of "at least three
days" at will.

More fundamentally: **"the level" here was selected by the reader, not by the
instructor.** `A-004` records that the course's "level" is an ordinal leg, not a price
line, and the instructor never says the level is the prior swing high. Taking Monday's
high as the level is an unsourced choice, so the test measures a hypothesis the course
did not state.

```text
EFFECT ON C-001: NONE.
n = 1, on a substituted 2026 week, against a self-selected level and a
self-selected counting convention. Does not resolve. Does not refute.
NO DAY-COUNT VALUE IS COMMITTED ANYWHERE AS A RESULT OF THIS DATUM.
```

**Precondition for this test ever counting:** `A-004` must first settle what "the level"
is as a price. If it does, ~~the measurement pipeline in `V02_HOMEWORK.md` §1.1 is
reusable and~~ this week becomes the first observation of the manual backtest
(dimension G), which `V02_REVIEW_R1.md` recommends. Until then it is an anecdote with a
decimal point.

> **AMENDED 2026-08-10 (V02 review R2, Minor 1).** The struck clause overstated §1.1.
> §1.1's **price** measurement is verified (`±0.5 pip`, confirmed against the chart's own
> printed last-bar OHLC) and is reusable. Its **day-boundary** derivation was not: it
> placed one bar on the wrong side of the Fri 31 Jul → Sun 2 Aug weekend boundary, and its
> *"open = prior close on all six boundaries"* self-validation was applied at the one
> boundary where continuity does not apply — a Friday-to-Sunday gap is normal, and the
> check selected the mapping that made a real −12.6 pip weekend gap vanish. Corrected in
> §1.1: day boundaries come from the chart's own dotted separators; continuity is a
> within-session check only.
>
> **The datum above is unaffected.** The 72-hour result, the level 0.81151 (Mon 3 Aug
> `15:00`) and the first breach (Thu 6 Aug `15:00`, 0.81356) were independently
> re-measured and reproduced exactly in R2. Only Sun 2 Aug's open and high and the
> prior-week Friday row moved, and no claim here rests on them. `EFFECT ON C-001` remains
> **NONE**.

---

## C-004 — London session open: 3:30am printed against 4:00 spoken

### Concept

What time the London session opens, which gates the pattern-arrival window that V02 calls
one of the two things that matter ("timing and pattern… if the pattern hits at the right
time, solid gold").

### Source A — the slide

| Field | Value |
|---|---|
| Video | V02 |
| Timestamp | slide `[00:45:55]`, shown again `[00:50:50]` |
| Screenshot | `04_SCREENSHOTS/V02/V02_00-45-55_forex-trading-times-slide.png` |
| What is shown | `London Session 3:30am-9:00am Gap 9-9:30a`, and above it `Asian Session: 8:30pm -3:00am Gap 3-3:30a` |

### Source B — the audio

| Field | Value |
|---|---|
| Video | V02 |
| Timestamp | `[00:50:32]` |
| What is said | "3 to 3.30 is the gap, **4 o'clock session open**. After March 25th, after our breakout session next week." |

### Conflict

The slide puts the London open at **3:30am**; speaking over that same slide, he puts it at
**4 o'clock**. Thirty minutes apart, in the same breath as the gap figure, which *does*
match the slide (3–3:30).

He is aware something moves. Immediately before, at `[00:50:18]`: "I know it starts March
25th. These are the times that are up right now, or for summer. And we back up the London
session in the winter."

### Possible Explanations

| # | Explanation | Supporting evidence | Assessment |
|---|---|---|---|
| 1 | **Daylight saving transition.** The slide shows one regime; the spoken 4:00 is what the London open becomes after the clocks change | UK BST began **25 March 2012**, one week after this 18 March lesson, and he names that exact date at `[00:50:18]`. US DST had already started 11 March 2012, so for one fortnight the usual UK–US offset is shifted by an hour — which is precisely the kind of thing that moves a New-York-clock London open from 3:30 to 4:00 | **Strongly supported and internally coherent.** But he never actually says "the open moves to 4:00 on the 25th"; that is the reader joining the pieces. |
| 2 | Loose speech — "around 3, 4 o'clock" | `[00:50:42]` immediately after: "the pattern has to come in around 3, 4 o'clock, 3.30, 4.30 in that range into the new session" — which reads as a *window* rather than a precise open | **Plausible.** This sentence treats 3:30–4:30 as a band, which would make the "4 o'clock" of `[00:50:32]` approximate rather than exact. |
| 3 | The slide is stale | No evidence. He presents it as current ("These are the times that are up right now"). | Weak |

Explanations 1 and 2 are both live and are not mutually exclusive — the band in
explanation 2 may exist precisely because the true open shifts seasonally.

### Resolution

```text
UNRESOLVED
```

**Foundational: no**, but **blocking for any time-gated rule.** The lesson's own position
is that timing is half the method, so a 30-minute ambiguity at the London open is not
cosmetic. Note also that this conflict cannot be settled without A-019 — a 3:30 that is
not attached to a timezone is not a time.

### Required to resolve

A later lesson stating the London open unambiguously with a timezone, or a lesson
recorded after 25 March 2012 showing an updated version of the same slide. V03 is
Week 2, 25 March 2012 — **the exact date he names** — so it is the natural place to
check, and should be checked deliberately rather than incidentally.

### Interim handling

Carry both values. Do not encode a London open. Where a session boundary is needed
downstream, record it as `3:30–4:00, timezone unresolved (A-019), seasonal shift
suspected (C-004)`.

---

## V03 EVIDENCE ADDED TO EXISTING RECORDS

The V03 pass adds evidence to all four records and **opens no new one**. That is a
finding in itself: V03 re-teaches week-1 material at a larger scale and, in doing so,
repeats the same unresolved spreads rather than introducing fresh conflicts.

One candidate was examined and deliberately **not** logged — *"swing trades pay… none"*
`[00:34:15]` against *"the target for swing trading… three times ADR over three days"*
`[00:34:58]`. Context separates them cleanly: the "none" describes holding a position
through a net-zero week, the target describes the course's three-day swing. Logging it
would manufacture a conflict the passage does not contain, which is the failure mode this
file's PURPOSE section exists to prevent.

### C-001 — how long price runs away from the anchor point

**More evidence, same spread, and one new formulation.** V03 restates the run length five
more times without narrowing it: *"Sunday, Monday, and Tuesday. Two or three days"*
`[00:31:19]`, *"two and a half, three days"* `[00:32:00]`, *"three days cycle for three
levels"* `[00:34:04]`, *"Two and a half to three days. Day one, day two, hold the level in
day three"* `[00:35:48]`, *"Two and a half to three days of rise"* `[00:36:05]`.

The new thing is that V03 gives the window an **exit rule** for the first time:

> *"If ADR times three is met or not met, but the three day time window is, and you get an
> outside structure high, you better take your money."* `[00:36:11]`–`[00:36:16]`

This makes the day count load-bearing in a way it was not in V01. Previously an
unresolved 2.5-vs-3-vs-4-day spread only blurred a description; now it gates an exit, so
the ambiguity has a direct P&L consequence. **Still `UNRESOLVED`** — V03 states the window
more often and no more precisely, and "outside structure" is itself undefined (A-033).

### C-002 — whether the both-ways rule is gated on proficiency

**New evidence, and it cuts against the V01 gating.** At `[00:36:23]`–`[00:36:24]` he says
*"And go the other way. Trade both ways"* — spoken unconditionally, to the whole class,
immediately after the exit rule above, with no proficiency qualifier anywhere near it.
V01 `[00:44:03]` / `[00:51:34]` conditioned both-ways trading on the student being past a
struggling stage (A-013).

Two readings, neither adopted: the V01 gate has quietly lapsed by week 2, or "trade both
ways" here means only *the direction reverses after the exit* rather than *you personally
should now trade both directions*. The surrounding sentences (*"the dealer trades off of
those numbers and back and forth… you're a trend trader"* `[00:36:29]`–`[00:36:34]`) fit
the second reading, but the imperative *"Trade both ways"* is addressed to the student.
**Status unchanged: `STATED EXCEPTION — condition unmeasurable`.**

### C-003 — whether M and W formations can fail

**Supports explanation 1 (rhetoric), does not resolve.** V02's *"M's and W's will not
fail"* is answered in V03 by an explicitly hedged version of the same claim:

> *"If you wait for the second leg, most of the time with the exception of the third leg,
> which doesn't happen that often, you are going to make money."* `[00:25:43]`–`[00:25:48]`

Same speaker, one week later, on the same object: *"most of the time"*, plus a named
exception. This is strong evidence that V02's absolute was emphasis rather than doctrine —
but it does not resolve C-003, because C-003 is a contradiction **internal to a single V02
sentence**, and nothing in V03 revisits that sentence. **Still `UNRESOLVED`.**

### C-004 — London session open, 3:30am printed vs 4:00 spoken

**The deliberate check this record required has been performed. The result is negative,
and it weakly cuts against the daylight-saving explanation without settling anything.**

C-004's "Required to resolve" field named V03 specifically: *"V03 is Week 2, 25 March 2012
— the exact date he names — so it is the natural place to check, and should be checked
deliberately rather than incidentally."*

What the V03 pass found:

| Check | Result |
|---|---|
| An updated forex-trading-times slide | **None.** No session-times slide appears among V03's captured screen states. |
| Any spoken restatement of the London open | **None.** The London open is never mentioned in V03. |
| Any spoken session time at all | Two, neither with a timezone: *"Came back right before the US session at 9.30"* `[00:55:05]`, and *"if you're sitting in front of your screen at 3 30 in the morning inside the shadow box"* `[01:03:21]`. |

The `[01:03:21]` "3 30 in the morning" is the interesting one. It is spoken **on 25 March
2012 — the DST date itself**, the very day after which explanation 1 predicts the relevant
boundary shifts to 4:00. He says 3:30, unprompted, in the ordinary course of describing
when a student would be at the screen.

**Why this does not resolve the record.** The `[01:03:21]` reference attaches "3 30" to
the *shadow box* (A-030), which is not stated to be the London open — the Asian session on
V02's slide also ends at 3:00 with a gap to 3:30, so a 3:30 reference is equally
consistent with the Asian-session boundary. Reading it as the London open is exactly the
kind of joining-the-pieces the record already declined to do for explanation 1.

**What it does do** is remove V03 as the hoped-for resolution route and slightly weaken
explanation 1: the one time-of-day he utters on the transition date is the slide's number,
not the spoken 4:00. **Still `UNRESOLVED`**, and the interim handling is unchanged: carry
both values, encode no London open.

**Required to resolve — updated.** V04 or V05 (same 25 March 2012 session date) or any
later lesson showing an updated times slide. V03 is now struck off as checked and negative.

---

## C-005 — The instructor and the guest presenter teach different entry systems in one lesson

### Concept

What gates an entry, and in which session. V04 contains two complete, internally coherent
accounts, delivered 30 minutes apart in the same recording, by two different people, with
**no speaker labels anywhere in the transcript**.

> **This record is unusual and the reason it exists should be stated first.** It is
> **probably not a contradiction in the Market Maker Method at all.** The guest scopes his
> statements to the US session and says so repeatedly. It is recorded because the two
> voices sit in one undifferentiated transcript, and a future session mining V04 for rules
> — or an automated extraction pass — has no way to know it is reading two people. The
> hazard is not that the course contradicts itself; it is that **the corpus will
> contradict itself if this is not written down.**

### Source A — the instructor, `[00:00:00]`–`[00:26:56]`

| Field | Value |
|---|---|
| Video | V04 |
| Timestamp | `[00:15:34]`–`[00:15:57]` |
| Screenshot | None for TDI — *"I can't show you TDI because it's not here"* `[00:13:53]` |
| What is said | *"The criteria is this. … 25 to 50 pips above and below the blue box. M formation second leg, W formation second leg, TDI confirms blood in the water shark fin outside the band to back in. That's the criteria. Simple."* |

Supporting: the session he works is the London stop-hunt window — *"From one to five AM
New York, one to four AM New York"* `[00:21:33]`, *"You're looking for the dealer to
exploit the shadow at the start of the London and to start of the US"* `[00:21:44]`. The
three bursts are central — *"You're looking for the three bursts"* `[00:00:36]`.

### Source B — the guest presenter, `[00:26:59]`–`[01:25:37]`

| Field | Value |
|---|---|
| Video | V04 |
| Timestamp | `[01:13:34]`–`[01:14:18]` |
| Screenshot | `04_SCREENSHOTS/V04/V04_00-34-00_pre-trade-question-checklist-slide.png` |
| What is said | *"first of all, I'm looking for the ADR to run. What I mean by that is if the pair generally every day runs 100 pips, if it's not in the mid 90s, it's not ready. … So I'm looking for one, the ADR to be met. Two, I'm looking for where it's at on TDI. … Three, what type of reversal candles is it giving me? … In the London, I'm sorry, in the US session, you generally don't get a lot of second lads [legs]. You just don't get them."* |

### The three specific divergences

| Topic | Source A (instructor) | Source B (guest) |
|---|---|---|
| **Session** | London stop-hunt window, 1–5 AM New York `[00:21:33]` | US session only. *"I think the only way I would ever trade the money session now is if somebody forced me to move overseas. Because I love the US session."* `[01:21:04]`–`[01:21:10]` |
| **Second leg** | A **necessary** entry condition `[00:15:49]` | *"in the US session, you generally don't get a lot of second lads. You just don't get them."* `[01:14:13]`–`[01:14:18]`; *"more than 50% of the time it's a retracement, and then it continues the move"* `[00:54:11]`–`[00:54:14]` |
| **Three pushes** | *"You're looking for the three bursts"* `[00:00:36]` | *"Jose, I do not look for three pushes because there's no pushes in the US session. The pushes come in the London session."* `[01:12:37]`–`[01:12:44]` |
| **Primary gate** | Location relative to the blue box, ± TDI `[00:15:43]` | **ADR ~90–95% complete** `[01:13:34]`, `[01:17:17]` |
| **Stop placement** | Sized from the **entry** — *"if your entry is here, your stop loss is right there. Ten fifteen pips"* `[00:04:24]`–`[00:04:30]` | Sized from the **low of the day** — *"My stop loss is seven pips plus the spread below the low of the day"* `[01:04:41]` |

### Conflict

Taken as statements about *the same system*, A and B are incompatible: B removes A's
second condition, removes A's three bursts, replaces A's primary gate, and measures the
stop from a different reference.

Taken as statements about *two different sessions by two different traders*, they are
consistent and B is explicitly derivative of A — the guest says so at length
(*"every single thing that I know about trading, I learned from Steve"* `[00:42:25]`–`[00:42:29]`).

**The transcript provides nothing that would let a reader tell which is happening.** There
are no speaker labels; the handover is unannounced; the only marker is a title card at
`00:27:20` that a text-only pass never sees.

### Possible Explanations

| # | Explanation | Supporting evidence | Assessment |
|---|---|---|---|
| 1 | **Different session, explicitly scoped** — B is A's method applied to a session where the second leg and the pushes do not occur | The guest scopes almost every claim ("in the US session…", 14 occurrences). He attributes the underlying method to the instructor throughout | **Strongly supported — the leading explanation** |
| 2 | Different speaker authority — B is a practitioner's personal adaptation, not doctrine | *"this is just me"* `[00:46:19]`, *"that's simply just my opinion"* `[01:00:10]`, *"in my opinion, this is just my opinion"* `[01:06:31]` | **Strongly supported, and compatible with 1** |
| 3 | Later refinement of an earlier rule | None — same recording, and B never claims to correct A | Rejected |
| 4 | Different instrument | None. Both range over the majors | Rejected |
| 5 | A genuine inconsistency in the course | Would require reading B as doctrine, which D-008 forbids without a decision | **Not supported** |

Explanations 1 and 2 together account for every divergence without inventing anything.
**They are not adopted as a resolution**, because adopting them would amount to ruling that
the guest's material is out of scope — and that is a scope decision the project owner and
the reviewer should make, not a student session.

### Resolution

```text
UNRESOLVED as a corpus-hygiene record.
THE SCOPE RULING HAS BEEN MADE — DECISIONS.md D-025, 2026-08-11.
```

**Foundational: no**, on the method. **Yes, on corpus hygiene.**

This is the distinguishing feature of this record: unlike `C-001`, no further course
material will resolve it, because there is nothing factually in doubt. What was needed is a
**ruling on how guest-presenter material is treated** across the corpus.

> **THE RULING — `D-025`, recorded 2026-08-11 from V04 review R1.** Guest-presenter
> material is admissible as **SECONDARY, DESCRIPTIVE** evidence (that a term exists, how it
> is spelled, that an object is displayed, what a printed artifact says) and is **EXCLUDED
> as NORMATIVE** material (entry criteria, gates, filters, stops, targets, sessions,
> thresholds, watchlists, schedules). Descriptive guest evidence may **EXTEND** an
> `A-xxx`/`C-xxx` record and may **NEVER RESOLVE or CLOSE** one, and may never outweigh an
> instructor statement. A guest/instructor divergence is **not a contradiction in the
> method** and is filed as corpus hygiene — which is what this record is, and it is the
> right category for every future instance. Speaker tagging is **mandatory** from V04
> forward for any lesson with more than one voice.
>
> **This record stays open.** The ruling settles the *scope* question it raised; it does
> not make the two accounts one account, and the hygiene hazard it exists to flag — two
> voices in one undifferentiated transcript — is permanent. The interim handling below is
> now the standing handling, ratified rather than replaced.

The interim handling, in force since the record was opened and now ratified by `D-025`:

1. Every V04 artifact tags each statement `INSTRUCTOR` or `GUEST`.
2. **No `GUEST` statement enters the canonical methodology**, the concept library, the
   master spec or any machine candidate.
3. No `GUEST` number is adopted — not the 7-pip stop, not the 35–50 pip target, not the
   ADR gate.

### Required to resolve

~~A project-owner or reviewer decision on the status of non-instructor presenters, recorded
in `DECISIONS.md`.~~ — **DISCHARGED 2026-08-11. The decision exists: `D-025`.** It was
raised before V05, as this field required, and it applies prospectively to V05–V21 and to
the third presenter, "Carl", who is queued at `[01:19:02]` and does not speak inside this
file. V05 shares the same session date.

What remains owed on this record is **not** a further ruling. It is the mechanical
obligation `D-025` imposes on every future multi-voice lesson: establish the number of
voices and the boundaries **before** writing notes, tag every source-note row, and carry a
speaker table in the transcript header.

### Related

| Type | Reference |
|---|---|
| Source | `03_LESSON_NOTES/V04_SOURCE_NOTES.md` §3f |
| Interpretation | `03_LESSON_NOTES/V04_INTERPRETATION.md` I9, §8.2 |
| Ambiguity | A-038 (the guest's ADR window), A-039 (TDI required but untaught) |
| Decision | **D-025 (the ruling — guest material is descriptive, never normative)**; D-008 (evidence hierarchy, which D-025 refines) |
| Review | `18_REVIEW/V04/V04_REVIEW_R1.md` § "THE C-005 RULING" |

---

## V04 EVIDENCE ADDED TO EXISTING RECORDS

| ID | V04 evidence | Effect |
|---|---|---|
| **C-001** — duration away from the anchor | `[00:20:28]`–`[00:20:33]` *"Now you trade away from the high of the week for two and a half to three days until the dealer issues another signal."* | **New source; lands squarely on Source A; does NOT resolve.** This is a near-verbatim restatement of `C-001` Source A (V01 `[00:35:06]`–`[00:35:11]`, *"you trade away from the anchor for two and a half to three more days"*), three lessons later. It does **not** match Source B (V01 `[00:35:15]`–`[00:35:25]`, four / three-and-a-half / three days) and does **not** match V02 `[00:16:15]` (*"at least three days"*, no upper bound). **What it adds beyond a repetition:** a terminating condition Source A lacked — *"until the dealer issues another signal"* — which reframes the quantity from a fixed holding period into a typical duration with an event-driven exit. That is the first textual support this record has ever had for **explanation 6** (a trader-side window distinct from the market-side move), which was previously marked *"plausible, unstated — do not adopt"*. It is now *plausible and partially stated*, and still **not adopted**: "another signal" is itself undefined, Source B is never retracted, and the day-counting convention remains unstated. **Status unchanged: `UNRESOLVED`. No day-count value is committed anywhere.** |
| **C-004** — London open, 3:30 printed vs 4:00 spoken | **Deliberate check performed, as `C-004`'s own "Required to resolve" field instructed.** Result: **negative on both halves.** | **No progress; V04 struck off as checked.** See the check record below. |

### The `C-004` deliberate check on V04 — method and negative result

`C-004`'s "Required to resolve — updated" field named V04 explicitly (*"V04 or V05 (same
25 March 2012 session date) or any later lesson showing an updated times slide"*). The
check was run deliberately, not incidentally, and both halves are negative.

**Visual half.** The full 1,037-frame sweep was segmented into **47 distinct screen
states** by anchor-based differencing (a new segment opens whenever a frame differs from
its segment's anchor by more than a set threshold, so slow accumulating changes such as
the instructor's 22 minutes of drawing are caught rather than collapsed). **One
representative frame per state was rendered into contact sheets and every one was
reviewed.** No forex-trading-times slide, no session-boundary table, and no clock-time
graphic of any kind appears anywhere in V04.

**Spoken half.** Every transcript entry containing a clock time, `am`/`pm`/`o'clock`, or
the words *London*, *Asian*, *New York*, *US session* or *session open* was extracted and
read — 47 entries. **The London open is never given a time in V04.**

The only timezoned clock times in the lesson are `[00:21:33]`–`[00:21:37]`: *"From one to
five AM New York, one to four AM New York, four or five hours. Take a break from eight to
11 New York time."* These are **hours to be at the screen**, not session boundaries, and
the instructor immediately marks them as a restatement (*"nothing's changed"* `[00:21:41]`).

**Why this does not discriminate 3:30 from 4:00.** The 1–5 AM New York window *contains*
both candidate values, so it is consistent with either and evidence for neither. The
adjacent line — *"You're looking for the dealer to exploit the shadow at the start of the
London and to start of the US"* `[00:21:44]` — confirms the window is meant to cover the
London start but attaches no number to it. Reading a boundary out of a screen-time window
would be exactly the joining-the-pieces this record has twice declined to do.

**Status: `UNRESOLVED`, unchanged. Interim handling unchanged: carry both values, encode
no London open.**

**Required to resolve — updated again.** V05 (same 25 March 2012 session date) or any
later lesson showing an updated times slide. **V03 and V04 are now both struck off as
checked and negative.**
