# CONTRADICTIONS

Conflicting teachings found within the course.

Template: `00_SYSTEM/TEMPLATES/CONTRADICTION_TEMPLATE.md`

---

## STATUS

```text
RECORDS:         2   (C-001, C-002)
LESSONS STUDIED: 1   (V01)
UNRESOLVED:      1   (C-001 — foundational)
```

> **UPDATED 2026-08-10 (review R1, finding 6b).** This block previously read
> `RECORDS: 0` and *"**Intentionally empty.** No course material has been studied, so no
> course contradiction has been observed."* Both statements were true at project start
> and are now false — the file holds two records. Corrected so the status does not
> contradict the file's own contents.

Both are **intra-lesson** contradictions within V01, and both originate with the
instructor rather than with the reading of him. `C-001` (how long price runs away from
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
| 8 | Instructor shorthand | `[00:36:17]` — "It's more than what I've told you. I understand that." — reads as an admission of loose prior teaching. | **Plausible** |
| 9 | Actual inconsistency in the course | The instructor's own acknowledgement at `[00:36:07]`–`[00:36:17]` is direct evidence for this. | **Most strongly supported** |

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
