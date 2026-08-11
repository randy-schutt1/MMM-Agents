# AUTOMATION AMBIGUITIES

Every subjective phrase in the course that would be dangerous to code prematurely.

Template: `00_SYSTEM/TEMPLATES/AMBIGUITY_TEMPLATE.md`

---

## STATUS

```text
RECORDS:         41   (A-001 … A-041)
LESSONS STUDIED:  4   (V01, V02, V03, V04 — V03 REVISE R1 minors-only; V04 not yet reviewed)
RESOLVED:         2   (A-003 — "pendings", on visual evidence at [00:40:25];
                       A-026 — HOW = High Of the Week, spoken expansion V03 [00:26:40])
DO NOT CODE:     39
```

> **UPDATED 2026-08-10 (review R1, finding 6b).** This block previously read
> `RECORDS: 0` and *"**Intentionally empty.** No course material has been studied, so no
> course ambiguity has been observed."* Both statements were true at project start and
> are now false. Corrected so the status does not contradict the file's own contents.
>
> **UPDATED again 2026-08-10 (review R3).** The R1 correction read `RECORDS: 18 /
> LESSONS STUDIED: 1`, which was accurate when written and went stale the moment the
> V02 pass added `A-019`–`A-028`. This is the third occurrence of the same staleness
> class in this one status block (`E20`); the counts above are arithmetic over the
> records the file actually contains.
>
> **UPDATED again 2026-08-10 (V03 pass).** Counts re-derived after `A-029`–`A-036` were
> added and `A-026` resolved. Updated in the same commit that added those records,
> which is the discipline the three prior corrections were asking for.
>
> **UPDATED again 2026-08-10 (V04 pass).** Counts re-derived after `A-037`–`A-041` were
> added. Nine earlier records gained V04 evidence and **none resolved**; the V04 evidence
> block at the end of this file records each one. Updated in the same commit that added
> the records.

Eighteen (`A-001`–`A-018`) arise from **V01 alone**, which names seventeen load-bearing
terms and defines none of them. Ten (`A-019`–`A-028`) were added by the V02 pass, which
also extended six of the V01 records. Eight (`A-029`–`A-036`) were added by the V03 pass,
which also extended seven earlier records and **resolved one** (`A-026`). Five (`A-037`–`A-041`)
were added by the V04 pass, which also extended nine earlier records and resolved none.

**A-039 is a different kind of record from the rest and is worth reading on its own.** It
does not ask what a phrase means; it records that V04 states the course's first complete
entry rule and that one of that rule's three necessary conditions (TDI) has been deferred
to a future lesson twice. It carries an explicit prohibition: **no session may drop that
condition in order to make the rule testable.** Six of V03's
eight are the vocabulary of a single slide — the sample flashcard's entry-criteria list
— which asks the student to verify conditions the course has never defined.

Two records are resolved: `A-003`, by text printed on a slide, and `A-026`, by a spoken
expansion of the abbreviation. The remaining thirty-four are `DO NOT CODE`.

Records appear here only when an actual lesson uses an actual subjective phrase.

---

## PURPOSE

Trading instruction is full of judgement words. Left unexamined, they take a
predictable path:

```text
"strong push"
  → agent needs something codable
  → agent picks a threshold that fits the examples it saw
  → threshold enters the concept library
  → threshold enters the machine spec
  → Pine Script enforces it
  → backtest validates the threshold against the data it was fitted to
  → the number looks like a course rule and no one can remember it wasn't
```

This log stops that at step 2 by keeping judgement **visibly** judgement.

`DECISIONS.md` D-010 (machine-rule firewall) is the governing decision.

---

## PHRASES TO WATCH FOR

Not a claim that the course uses these — a checklist of the kind of language that
gets logged when encountered:

*strong, clean, obvious, significant, nice, enough space, high quality, weak,
extended, too extended, momentum, trapped, aggressive, proper, correct-looking,
textbook, healthy, decent, clear.*

Also: quantities stated with a hedge ("usually about 20 pips", "roughly the
London open"). The hedge is part of the teaching. Recording the number without the
hedge is error code E03.

---

## STATUS VALUES

| Status | Meaning | Phase |
|---|---|---|
| `DO NOT CODE` | Default. Subjective; no numeric representation permitted. | 1 |
| `RESEARCH CANDIDATE` | A measurable hypothesis is defined but unvalidated. | 4 |
| `EMPIRICALLY VALIDATED` | Tested against manually labelled history. | 6 |
| `RESOLVED BY COURSE` | A later lesson defines it explicitly. Cite the evidence. | any |

Promotion requires evidence, never convenience. Records are never deleted — a
resolved record keeps its history.

---

## INDEX

| ID | Phrase | First seen | Status | Impact if wrong |
|---|---|---|---|---|
| A-001 | "anchor point" | V01 `[00:34:47]` | DO NOT CODE | Foundational. Sets weekly direction and holding period. Wrong = every weekly-bias rule is wrong. |
| A-002 | "trap move" / "false move" | V01 `[00:34:33]` | DO NOT CODE | Foundational. The lesson's central object. Wrong = the whole framing is misapplied. |
| A-003 | "picks up the [?penings?]" → **"pendings"** | V01 `[00:39:12]` | **RESOLVED BY COURSE** | Contained. The word is recovered — *pendings* = pending orders, printed at `[00:40:25]`. It is *identified*, not *quantified*: nothing supports a numeric representation of where pending orders sit. |
| A-004 | "level" (countable unit) | V01 `[00:35:38]` | DO NOT CODE — **materially constrained** by V02 slide `[00:18:00]` | High. V02's chart prints Level 1/2/3 as an ordinal sequence of legs. |
| A-005 | "the trading zone" | V01 `[00:30:40]` | DO NOT CODE | Foundational. The stated entry filter for struggling traders. **Deferred twice: V01→V02, then V02 `[00:45:52]`→V03.** |
| A-006 | "the blue box" / "the box" / "the red box" | V01 `[00:43:07]` | DO NOT CODE | High. Three box terms, no definition, one entry prohibition attached. |
| A-007 | "second leg" | V01 `[00:43:21]` | DO NOT CODE | **Foundational (raised from High at V02).** Three of V02's instructions route through it, and V02 promises a definition then withholds it. |
| A-008 | "the tracer" | V01 `[00:38:57]` | DO NOT CODE | Medium. Named as the only thing that varies week to week. |
| A-009 | "stop hunt high drop" / "straight drop" | V01 `[00:51:42]` | DO NOT CODE | High. The named entry formation for struggling traders. |
| A-010 | "peak formation high or low" | V01 `[00:34:26]` | DO NOT CODE | Foundational. May or may not be the same object as A-001. |
| A-011 | "M and W formation" | V01 `[00:17:45]` | DO NOT CODE | Foundational. Assumed known; never described in V01. |
| A-012 | "midweek reversal" | V01 `[00:21:43]` | DO NOT CODE | Medium. The stated alternative to a Sunday/Monday cycle start. |
| A-013 | "struggling" vs "more experienced" / "more proficient" | V01 `[00:44:03]` | DO NOT CODE | High. Two rules are conditional on it and it is unmeasurable. |
| A-014 | "fractional disparity" | V01 `[00:18:16]` | DO NOT CODE | Unknown. Named once in a survey, never explained. |
| A-015 | "shows something to the traders" | V01 `[00:39:19]` | DO NOT CODE | Medium. The inducement mechanism in the core sequence. |
| A-016 | "goes into chop" | V01 `[00:44:45]` | DO NOT CODE | Medium. The stated end-of-week failure state. |
| A-017 | "big entry candle" | V01 `[00:48:41]` | DO NOT CODE | Medium. The only entry-trigger language in the lesson. |
| A-018 | `R = <number>` labels on the shaded boxes | V01 `[00:48:35]` | DO NOT CODE | Medium. If misread as a risk-to-reward ratio it would invent a target rule the lesson never states. |
| A-019 | session times with **no timezone stated** | V02 `[00:50:32]` | DO NOT CODE — **materially constrained** by slide `[00:45:55]` | Foundational. The full session table is now recovered from the slide; only the timezone is missing. |
| A-020 | "mayonnaise" (a moving average) | V02 `[00:19:46]` | DO NOT CODE | High. Used as a support/resistance reference *and* as the distance test for whether a trade is worth taking. |
| A-021 | the letter sequence for "the cycle" | V02 `[00:07:28]` / `[00:19:31]` | DO NOT CODE | Medium. Two incompatible strings ("M-A-A-W", "WVVM") for the same named object. |
| A-022 | "half-Batman" | V02 `[00:20:37]` | DO NOT CODE | High. One of exactly two named continuations at outside structure high. |
| A-023 | "33 trade" | V02 `[00:22:16]` | DO NOT CODE — **constrained** by V02 slide `[00:18:00]` | Medium. Printed on the **Level 3** move, tying it to level rather than calendar day. Digits still undecoded. |
| A-024 | "slightly above" (22-trade overshoot tolerance) | V02 `[00:01:32]` | DO NOT CODE | Medium. Decides whether an otherwise-valid 22 setup is invalidated. |
| A-025 | "a good close below" | V02 `[00:39:19]` | DO NOT CODE | Medium. The trigger for the only numeric exit rule in V02 (−15 scratch-out). |
| A-026 | `HOW` (printed beside `LOW`) | V02 slide `[00:08:55]` | DO NOT CODE | Medium. Names the level the dealer moves away from; "High Of Week" is plausible but unstated. |
| A-027 | "Swing Traders Book- Day Traders Book" | V02 slide `[00:18:00]` | DO NOT CODE | Medium. Printed over the Level 3 exit — reads like a target rule, and would invent one if adopted. |
| A-028 | `V-3` | V02 slide `[00:18:00]` | DO NOT CODE | Low-Medium. Printed beside `PFL` at the week's low, unexplained. |

---

## RECORDS

## A-001 — "anchor point"

### Course Meaning

A point established by the dealer, usually mid-week, after which price moves away from it in one direction for the remainder of the week. The instructor never defines what forms it, what confirms it, or how it is identified in real time. He associates it with a "W or M formation, multi session" and with "peak formation high or low" without stating whether these are the same thing.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V01 | `00:34:47` | "you identify the anchor point of the cycle, W or M formation, multi session over Tuesday, Wednesday or Monday, Tuesday" |
| V01 | `00:35:05` | "If the anchor point is in place, you trade away from the anchor for two and a half to three more days." |
| V01 | `00:35:55` | "if the dealer anchors in on Tuesday and rises Tuesday… he'll rise Wednesday, Thursday and complete the cycle on Friday" |
| V01 | `00:36:17` | "if the dealer anchors in early because he completed the pattern… in the previous week" |
| V01 | `00:51:22` | "When the dealer anchors in the middle of the week, you only are trading one direction till Friday away from the peak formation down short." |
| V01 | `00:51:38` | "I want you to try to identify the anchor point and take shorts off of stop [hunt] high drop" |

### Visual Characteristics

> **CORRECTED 2026-08-10 (review R3, action 3).** This field previously read: *"**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost."* That was true when written and became false when I-006 was `RESOLVED` and 22 frames were captured. Original wording retained so the change is visible.

**Not defined by the frames, but no longer unseen.** 22 screenshots exist for V01
(`04_SCREENSHOTS/V01/INDEX.md`). See the *Visual Evidence Update* at the foot of this
record: `[00:50:55]` shows the structure the instructor describes and names none of it
"anchor point".

### Counter-examples

None. V01 shows no example where this was rejected or explicitly not applied. Counter-examples are what would bound this concept, and the lesson provides none.

### Possible Measurable Features

| # | Candidate measure | Rationale | Course support |
|---|---|---|---|
| 1 | A weekly extremum (high or low) occurring Monday–Wednesday, after which directional persistence to Friday exceeds some threshold | The instructor consistently ties it to a mid-week extremum and a subsequent one-way run | NONE |
| 2 | The turning point of a multi-session M or W formation | `[00:34:47]` names the formation in the same breath | NONE — and the equivalence itself is unestablished (see A-010, A-011) |

```text
Classification:          INFERRED MACHINE CANDIDATE
Canonical Course Status: NOT A COURSE RULE
```

### Current Status

```text
DO NOT CODE
```

### Required Research

V02 onward — the instructor defers the trading zone to V02 and may define the anchor there. Also: a screenshot of `[00:34:47]`–`[00:35:15]`. Failing both, accumulated manual backtest labelling once the concept is understood well enough to label.

### Impact If Wrong

Foundational. Weekly directional bias, permitted trade direction, and holding period all hang off it. If this is quantified wrongly, every weekly-cycle rule in the corpus is wrong in the same direction, and the error will not be visible because everything will remain internally consistent.

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-010 (peak formation), A-011 (M and W) |
| Contradiction | C-001 (the duration attached to it) |
| Interpretation | `03_LESSON_NOTES/V01_INTERPRETATION.md` I6, I7 |

---

### Visual Evidence Update — 2026-08-10

Screenshots now exist. `04_SCREENSHOTS/V01/V01_00-50-55_typical-week-gbpusd-m15.png`
shows the fullest depiction of the cycle: on `GBPUSD,M15`, a low under **Tues** printed
*"Stops Are Triggered on The Weak long Holders"* and *"Lower Level Short Holders Are Now
trapped"*, followed by *"A uni-directional Swing The Rest Of The Week"*, then *"Higher
Level Longs Are Now Trapped"* under **Wed**.

This shows the *structure* the instructor is describing. It does **not** define the
anchor point: none of the five printed labels on that chart uses the words "anchor
point", "peak formation", "M" or "W". One annotated instance is not a definition, and
it gives no rule for recognising the turn before the swing has happened.

**Status unchanged: `DO NOT CODE`.**
## A-002 — "trap move / false move"

### Course Meaning

A deliberate price movement made by the dealer to induce retail traders into the wrong directional position, then reverse against them. The instructor defines it entirely by **when** it happens — week open, day open, each session open, session close, day close, week close — and never by what it looks like on a chart.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V01 | `00:34:33` | "the trap moves that are made at the beginning of the week to induce traders to take a position the wrong way and jam them up for the cycle" |
| V01 | `00:36:38` | "the trap moves are the key to your success in the business. It's identifying where the trap moves are made" |
| V01 | `00:36:49` | "On the broader spectrum, the trap moves are made at the beginning of the week, Sunday and Monday" |
| V01 | `00:37:14` | "They make a false move at the end of the session for that dealer to square his books" |
| V01 | `00:45:40` | "False move week beginning, beginning of the session, end of the session, end of the week" |

### Visual Characteristics

> **CORRECTED 2026-08-10 (review R3, action 3).** This field previously read: *"**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost."* 22 frames were subsequently captured and I-006 is `RESOLVED`. Original wording retained so the change is visible. The determination below is the student's, made against the frames named, and was flagged as required work by review R2 Part 3.3.

**Materially constrained by the frames; still not defined.** Read from `[00:30:35]`,
`[00:38:50]` and `[00:48:35]`:

- `[00:30:35]` is a text slide headed **"How To Beat The Market Maker"** / **"The Trap
  Moves Are Made:"** followed by the six boundaries. It fixes the *taxonomy* — the term
  is defined by occasion, exactly as the audio has it — and shows nothing of shape.
- `[00:38:50]` prints **"Week Beginning Trap High"** on the chart itself, directly above
  the advance enclosed by the pale-blue rectangle. This is the one place in V01 where the
  word "trap" is pinned to a specific location on a specific price move.
- `[00:48:35]` carries the printed title **"Trap Here..Higher Level Long Holders"**,
  positioned above the dark-red rectangle that covers the area price ran into. This is a
  slide title placed over a region, not a label attached to a candle.

**What this adds:** it fixes *where on a chart the instructor applies the word* — at the
top of a week-opening advance, and over the region traders are left holding. The audio
gave only *when*.

**What it does not add:** no shape, no size, no bar count, no invalidation, and no
outcome. Both labelled instances are prepared examples with no stated result, and two
instances cannot bound a definition. **Status unchanged: `DO NOT CODE`.**

### Counter-examples

None. V01 shows no example where this was rejected or explicitly not applied. Counter-examples are what would bound this concept, and the lesson provides none.

### Possible Measurable Features

| # | Candidate measure | Rationale | Course support |
|---|---|---|---|
| 1 | A move at a named session/week boundary that is subsequently fully retraced within N bars | Retracement is implied by "false", and the timing is the one thing stated explicitly | PARTIAL — timing is stated; retracement is not |
| 2 | Any excursion beyond the prior session range that fails to hold | Matches the "hits the stops… pulls back" narration at `[00:39:07]`–`[00:39:34]` | NONE |

```text
Classification:          INFERRED MACHINE CANDIDATE
Canonical Course Status: NOT A COURSE RULE
```

### Current Status

```text
DO NOT CODE
```

### Required Research

Examples with outcomes. V01 gives none — `[00:40:26]` names USDCHF and EURUSD but describes no result. Later lessons, or manual backtest observations once a working definition exists.

### Impact If Wrong

Foundational. This is the lesson's central object and the thing the trader is told not to trade. A wrong definition inverts the method — the trader would take exactly the moves he is told to avoid.

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-003, A-015 |
| Interpretation | `03_LESSON_NOTES/V01_INTERPRETATION.md` I1, I9 |

---

## A-003 — "picks up the [?penings?]"

### Course Meaning

> **CORRECTED 2026-08-10 (review R3, action 2 — R1 finding 10 as widened by R2).** The five fields flagged below were written before the word was recovered and were left unchanged when the trailing `RESOLVED BY COURSE` block was appended. A reader who stopped before that block learned the opposite of the truth. Each is corrected in place with its original wording retained.

**The word is "pendings" — pending orders.** Original wording: *"**The word itself has
not been recovered.** It is transcribed as "penings" four times in identical
construction, always as a thing the dealer collects at the same moment he 'hits the
stops'. It is not an English word and no course meaning can be stated. Recording it as
an ambiguity rather than guessing is the correct handling."*

That refusal was correct at the time and the resolution vindicates it: the word was
never guessable from audio. `V01_00-40-25_beginning-of-session-chart.png` prints
**"Trigger The Pendings"** on the chart, paired with **"Trigger The Stops"**. The
recurring construction therefore names **two distinct pools of resting orders** the
dealer collects at a boundary — stop orders and pending orders. See the trailing
`RESOLVED BY COURSE` block for the full evidence.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V01 | `00:39:12` | "the dealer comes out of the consolidation. It's the stops or picks up the penings, whatever happens to be there" |
| V01 | `00:39:43` | "The dealer then hits the stops, picks up the penings." |
| V01 | `00:40:46` | "Don't fall for the false move to pick up the penings and grab the breakout traders as a trade." |

### Visual Characteristics

**The word is printed on the `[00:40:25]` slide.** Original wording: *"**Unknown — no
screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a
slide while using this phrase, so the visual characteristics are precisely the part that
was lost."* That diagnosis was exactly right — the missing channel was carrying the
answer. `V01_00-40-25_beginning-of-session-chart.png` prints **"Trigger The Pendings"**
above the pre-session range and **"Trigger The Stops"** below it, on a slide titled
"Beginning Of Session". The instructor never reads either label aloud.

### Counter-examples

None. V01 shows no example where this was rejected or explicitly not applied. Counter-examples are what would bound this concept, and the lesson provides none.

### Possible Measurable Features

| # | Candidate measure | Rationale | Course support |
|---|---|---|---|
| 1 | (none proposed) | The word is now read, but reading a word is not measuring an object. Nothing in V01 states where pending orders sit, how many there are, or how a chart would show them | NONE |

> Original rationale for candidate 1, retained: *"Proposing a measurable representation
> for a word that has not been read would be inventing the concept outright."* The reason
> has changed; the conclusion has not.

```text
Classification:          RESOLVED BY COURSE — the term is identified
Canonical Course Status: COURSE TERM (printed on the [00:40:25] slide)
```

> Original classification block, retained: `INFERRED MACHINE CANDIDATE` /
> `NOT A COURSE RULE`. Superseded — the term is printed on the instructor's own slide,
> so it is course vocabulary, not an agent inference. **This resolves the word, not a
> rule:** no rule attaches to it and none may be written from it.

### Current Status

```text
RESOLVED BY COURSE
```

### Required Research

**None outstanding for the word itself.** Original entry, retained: *"Re-listening to
the audio at `[00:39:12]` and `[00:39:43]`. This is the cheapest open question in V01 to
resolve and it sits at two of the twelve steps of the core sequence."* It was resolved
instead by a printed slide label, at no audio cost. What remains open is not lexical:
whether any later lesson attaches an identifiable chart location to pending orders. Watch
V03 onward; do not go looking for one in V01.

### Impact If Wrong

**Contained.** Original entry, retained: *"Unknown, which is itself the problem. It is a
named object in the mechanism the whole lesson describes. It may be trivial or it may be
a core concept."* Now that the word is read, the exposure is bounded: it names a pool of
resting orders alongside stops at two steps of the core sequence. The live risk is no
longer misreading the word — it is quantifying it, which nothing in V01 supports.

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-002 |
| Interpretation | `03_LESSON_NOTES/V01_INTERPRETATION.md` I11, Q5 |

---

### RESOLVED BY COURSE — 2026-08-10

The word is **"pendings"** — pending orders.

`04_SCREENSHOTS/V01/V01_00-40-25_beginning-of-session-chart.png` prints
**"Trigger The Pendings"** directly on the chart above the pre-session range, paired
with **"Trigger The Stops"** below it. The slide is titled "Beginning Of Session".

So the recurring construction the ASR mangled — *"hits the stops or picks up the
[pendings]"* — names two distinct pools of resting orders the dealer collects at a
boundary: **stop orders** and **pending orders**.

This was never guessable from audio, and the record correctly refused to guess. It was
resolved by a label printed on a slide that the instructor never read aloud.

Note the concept is now *identified*, not *quantified*. Nothing here supports a
numeric representation of where pending orders sit.
## A-004 — "level (as a countable unit)"

### Course Meaning

A discrete unit of price movement that can be counted. The instructor and his students both use it as though its size is known and agreed — "four levels here", "one to three levels". No definition, no measurement, and no relationship to pips, ranges, or structure is given anywhere in V01.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V01 | `00:35:38` | Quoting a student: "Steve, I don't understand because there's four levels here." |
| V01 | `00:36:07` | Quoting students: "Steve, you said three days, three levels." |
| V01 | `00:39:53` | "You're only going to get one to three levels out of the false move week beginning." |

### Visual Characteristics

> **CORRECTED 2026-08-10 (review R3, action 3).** This field previously read: *"**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost."* 22 frames were subsequently captured and I-006 is `RESOLVED`. Original wording retained so the change is visible.

**Constrained by the frames.** See the *Visual Evidence Update* at the foot of this
record: `[00:50:55]` shows horizontal dashed lines in yellow, red and cyan and prints
*"Level Not Crossed Until Late Friday"* against one. Note that V02's slide `[00:18:00]`
subsequently prints `Level 1` / `Level 2` / `Level 3` as an ordinal sequence of legs,
which is a *different* reading of the same word; both are recorded, neither is adopted
(see the V02 evidence table at the foot of this file).

### Counter-examples

None. V01 shows no example where this was rejected or explicitly not applied. Counter-examples are what would bound this concept, and the lesson provides none.

### Possible Measurable Features

| # | Candidate measure | Rationale | Course support |
|---|---|---|---|
| 1 | A fixed pip increment per instrument | "Level" is counted like a unit, which suggests fixed size | NONE |
| 2 | A prior-session or prior-day range multiple | Would make levels instrument- and volatility-relative | NONE |
| 3 | A structural swing count rather than a distance | "three days, three levels" pairs levels with days, hinting at one level per session | NONE — the pairing may be coincidental |

```text
Classification:          INFERRED MACHINE CANDIDATE
Canonical Course Status: NOT A COURSE RULE
```

### Current Status

```text
DO NOT CODE
```

### Required Research

A later lesson defining or drawing levels. The `[00:38:02]` instruction — "on the one hour chart… start looking at the levels and the cycle" — implies levels are visible on a 1H chart, so a screenshot of any lesson showing marked levels would resolve it.

### Impact If Wrong

High. It is the only unit in which V01 expresses expected move size. Quantifying it wrongly makes every target and every "how far will it run" statement wrong by a scale factor.

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-001 |
| Contradiction | C-001 ("three days, three levels") |

---

### Visual Evidence Update — 2026-08-10

`V01_00-50-55_typical-week-gbpusd-m15.png` shows horizontal dashed lines in yellow, red
and cyan spanning the chart, and prints *"Level Not Crossed Until Late Friday"* against
one of them.

A "level" is therefore a **horizontal price line drawn on the instructor's template** —
not a distance, not a swing count, and not a session boundary. That eliminates the third
candidate measure below ("a structural swing count rather than a distance").

What is still unknown: how the lines are derived, what spacing separates them, and
whether "one to three levels out of the false move week beginning" `[00:39:53]` counts
lines crossed or something else.

**Status unchanged: `DO NOT CODE`.**
## A-005 — "the trading zone"

### Course Meaning

An area or condition that qualifies a setup. The instructor makes it the mandatory entry filter for struggling traders and then **explicitly defers defining it** to later in the same session (V02). Nothing in V01 describes it.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V01 | `00:30:40` | "let's talk about some trap moves, the trading zone, and some things I want you to try to understand a little clearer" |
| V01 | `00:43:35` | "grab only trades that come out and are set in the trading zone exactly where I'm going to lay it out for you" |
| V01 | `00:44:22` | "take only those trades that are established by the proper formation of the trading zone which I'm going to discuss tonight" |

### Visual Characteristics

> **CORRECTED 2026-08-10 (review R3, action 3).** This field previously read: *"**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost."* 22 frames were subsequently captured and I-006 is `RESOLVED`. Original wording retained so the change is visible.

**Screenshots exist and none bears on this term.** All 22 V01 frames were read
(`04_SCREENSHOTS/V01/INDEX.md`). None prints the words "trading zone" or marks a region
so named. That is a stronger and more useful statement than "no screenshot exists": the
visual channel was recovered and the term still is not shown, which is consistent with
the instructor deferring it — twice, V01→V02→V03.

### Counter-examples

None. V01 shows no example where this was rejected or explicitly not applied. Counter-examples are what would bound this concept, and the lesson provides none.

### Possible Measurable Features

| # | Candidate measure | Rationale | Course support |
|---|---|---|---|
| 1 | (deferred) | V02 is expected to define this. Proposing a measure before the definition arrives would be premature by exactly one lesson | NONE |

```text
Classification:          INFERRED MACHINE CANDIDATE
Canonical Course Status: NOT A COURSE RULE
```

### Current Status

```text
DO NOT CODE
```

### Required Research

**V02.** This is the single highest-value open question carried out of V01. Do not attempt to resolve it from V01 material.

### Impact If Wrong

Foundational. It is stated as the gating filter on every entry for the lesson's target audience. Getting it wrong means every entry in the corpus is filtered wrongly.

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-006 (the boxes may be part of it) |
| Interpretation | `03_LESSON_NOTES/V01_INTERPRETATION.md` Q2 |

---

## A-006 — "the blue box / the box / the red box"

### Course Meaning

Three distinct box terms appear in V01. **None is defined and it is not established that they are three things, two things, or one thing.** The blue box is characterised only as "more of a guide" for experienced traders. "The box" carries an entry prohibition. The red box appears in a US-session timing scenario.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V01 | `00:43:07` | "You're taking the first move out of the box as a trade and it's messing you up." |
| V01 | `00:43:56` | "This trade is not below the blue box. I know that." |
| V01 | `00:44:03` | "the blue box is more of a guide" |
| V01 | `00:45:55` | "You've been in a trade, US session, not quite in the red box yet." |
| V01 | `00:47:55` | "It is always better to wait to be inside the box and wait for the next part of the session to start" |

### Visual Characteristics

> **UPDATED 2026-08-10 (review R1, finding 1).** The original entry read: *"Unknown — no screenshot exists for V01 (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost."* Screenshots were subsequently captured and I-006 is `RESOLVED`. Original wording retained so the change is visible.

Read from captured frames `[00:38:50]`, `[00:40:25]`, `[00:44:40]`, `[00:48:35]`:

The boxes are **shaded rectangles with both a time extent and a price extent**. At
`[00:48:35]` each rectangle carries a numeric label (`R = 70.5`, `R = 51…`, `= 43.1`) —
see `A-018` — so they bound a measured region rather than being decorative shading.

> **NARROWED 2026-08-10 (review R2 finding N5, `E02`).** This paragraph previously
> continued: *"Pale blue covers flat, low-range consolidation; dark red covers the
> extended area where price is described as trapped."* The first half is contradicted by
> one of the four frames it rests on. Corrected below; original wording retained.

What the four frames actually show, frame by frame:

| Frame | Pale blue covers | Dark red covers |
|---|---|---|
| `[00:38:50]` | the **sharp week-opening advance** from the week-open low to the "Week Beginning Trap High" — neither flat nor low-range | a later decline |
| `[00:40:25]` | a low, flat pre-session range | the high area after a steep rise |
| `[00:44:40]` | a flat sideways range at lower right | a decline mid-chart |
| `[00:48:35]` | a flat low range at left, and a range at right | the area price ran into after the large up-candle |

Three of four pale-blue rectangles sit over flat consolidation and the fourth sits over
a directional advance. **No unifying rule for what blue marks is offered here**, because
four frames do not supply one. Dark red is more consistent — in all four it covers the
region price has run into and where traders are described as trapped — but four
prepared examples are not a definition either.

**What this does NOT settle.** Both candidate measures below remain live. A rectangle has two axes and the time axis carries information too: the blue rectangle's left edge sits on a vertical day-separator at `[00:38:50]`, the blue rectangle at `[00:44:40]` begins immediately after two vertical separators, and the blue rectangle at `[00:48:35]` abuts a dashed vertical pair. An earlier reading (`V01_INTERPRETATION.md` §10.1 `U2`, now **withdrawn**) declared the session-time reading wrong; review R1 finding 1 overturned that as unsupported. **Neither candidate is eliminated.**

### Counter-examples

None. V01 shows no example where this was rejected or explicitly not applied. Counter-examples are what would bound this concept, and the lesson provides none.

### Possible Measurable Features

| # | Candidate measure | Rationale | Course support |
|---|---|---|---|
| 1 | A session range rectangle drawn on the chart, colour-coded by session | The red box appears in a US-session context and "inside the box" is used as a waiting condition | NONE |
| 2 | A price zone bounding valid entries, independent of session | `[00:43:56]` describes a trade being outside it, implying a positional not temporal boundary | NONE — and this reading conflicts with the one above |

Both candidates survive the visual evidence. The frames show rectangles that are bounded on **both** axes, which is consistent with either reading and decisive for neither. Resolving this requires a later lesson that draws a box live or states what bounds it — not further inspection of these four frames.

```text
Classification:          INFERRED MACHINE CANDIDATE
Canonical Course Status: NOT A COURSE RULE
```

### Current Status

```text
DO NOT CODE
```

### Required Research

~~A screenshot of `[00:43:53]` or `[00:45:55]`.~~ **Both obtained** — `[00:43:58]` and
`[00:46:05]` — and neither resolves it; see Visual Characteristics above. What is needed
is **a later lesson that draws a box live or states what bounds it**. Note that the two
candidate readings above are mutually exclusive, so this cannot be resolved by reasoning
from the transcript, and R2 confirmed it cannot be resolved by further inspection of
these four frames either.

### Impact If Wrong

High. An entry prohibition (`[00:43:07]`) and a wait condition (`[00:47:55]`) both reference "the box" with no stated referent. Binding them to the wrong object produces confidently wrong entry logic.

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-005 |
| Contradiction | C-002 |
| Interpretation | `03_LESSON_NOTES/V01_INTERPRETATION.md` I2, Q3, Q4 |

---

### Visual Evidence Update — 2026-08-10 — WITHDRAWN, no candidate reading eliminated

> **WITHDRAWN 2026-08-10 by review R1 finding 1 (`E02`, MAJOR) / confirmed R2 finding N1
> / applied R3.** This block asserted that the visual evidence *eliminates* the
> session-time reading of the boxes. It does not. It is the same overturned claim as the
> withdrawn `U2` in `V01_INTERPRETATION.md` §10.1, and it survived here after the other
> three locations were corrected — in the register downstream machine-spec work reads,
> forty-five lines below the corrected *Visual Characteristics* text that contradicts it.
> **The current statement of what the frames show is the *Visual Characteristics* section
> above.** Both candidate measures remain live; `A-006` remains `DO NOT CODE`.
>
> The original text is retained below in full, per `REMEDIATION_PROTOCOL.md` §2 — it is
> not deleted, and its refutation is recorded with it.

**ORIGINAL TEXT — WITHDRAWN, DO NOT CITE:**

> The boxes are **shaded rectangles drawn over price areas on the chart**:
>
> - **Pale blue** over flat consolidation ranges —
>   `V01_00-40-25_beginning-of-session-chart.png` (over the low pre-session range),
>   `V01_00-44-40_end-of-week-chart.png` (lower right), `V01_00-48-35_...png` (two of them).
> - **Dark red** over the extended area where price has run and traders are described as
>   trapped — same frames, plus `V01_00-38-50_beginning-of-week-chart.png`.
>
> At `[00:48:35]` each rectangle carries a numeric label (`R = 70.5`, `R = 51…`, `= 43.1`),
> so they are **measured regions**, not shading for emphasis. See A-018.
>
> **This eliminates candidate 1** ("a session range rectangle drawn on the chart,
> colour-coded by session"). The boxes do not align with session boundaries; they are
> drawn around price structures. Candidate 2 — a price zone bounding valid entries — is
> consistent with what is shown, but is not confirmed: nothing on the slides states that
> the box governs entry eligibility.
>
> Still unresolved: whether "the box" of `[00:43:07]` means the blue one, the red one, or
> either; and how the rectangles are placed.

**Why it is wrong.** The load-bearing sentence — *"The boxes do not align with session
boundaries"* — is refuted by the three frames the block itself cites:

- `[00:38:50]` — two vertical dotted lines near the left edge; the pale-blue rectangle's
  left edge sits on the second of them.
- `[00:44:40]` — two vertical dotted separators at the right; the pale-blue rectangle
  begins immediately to the right of the second.
- `[00:48:35]` — a dashed vertical pair at the right; the pale-blue rectangle labelled
  `R = 51…` begins at the second.

A rectangle has two axes. Showing that it bounds a price region says nothing about
whether its time edges are placed on session boundaries — and here they demonstrably
are, on all three frames. The block also contains the claim narrowed under R2 finding
N5: pale blue is *not* uniformly over flat consolidation (`[00:38:50]` contradicts it).

**Status unchanged: `DO NOT CODE`. Both candidate measures live. `Q4` fully open.**
## A-007 — "second leg"

### Course Meaning

The preferred entry timing. "The best way to grab setups is to wait for a second leg." What constitutes a leg, how a first leg is distinguished from a second, and on what timeframe, are not stated.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V01 | `00:03:40` | "I'll show it off a[?] [f]ormation second leg and you'll tell me the trend's up" — garbled, but the term appears |
| V01 | `00:43:21` | "The best way to grab setups is to wait for a second leg." |

### Visual Characteristics

> **CORRECTED 2026-08-10 (review R3, action 3).** This field previously read: *"**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost."* 22 frames were subsequently captured and I-006 is `RESOLVED`. Original wording retained so the change is visible.

**A bearing frame exists and it defines nothing.** `[00:43:21]` ("the best way to grab
setups is to wait for a second leg") is spoken over the "Beginning Of Session" chart;
`V01_00-43-58_beginning-of-session-drawn-on.png` captures the instructor's live green
marks on that chart 37 seconds later.

**No leg is labelled, no legs are counted, and no first/second boundary is drawn.** The
freehand is consistent with several readings and is deliberately **not** converted into a
leg definition here — review R2 declined the same conversion for the same reason
(R2 Part 3.3). Recording that the frame was examined and found non-determinative is the
finding; it is materially different from "no screenshot exists", and it closes the
cheap route to resolving this record.

V02 makes this worse rather than better: at `[00:35:22]` the instructor says "**And I'm
going to define what a second leg is**" and then defines it by gesture. See the V02
evidence table at the foot of this file.

### Counter-examples

None. V01 shows no example where this was rejected or explicitly not applied. Counter-examples are what would bound this concept, and the lesson provides none.

### Possible Measurable Features

| # | Candidate measure | Rationale | Course support |
|---|---|---|---|
| 1 | The second push of a two-push structure, i.e. the second peak of an M or the second trough of a W | `[00:34:47]` associates the anchor with an M or W, which is a two-leg structure by construction | NONE — the connection is the agent's, not the instructor's |
| 2 | The second directional move after a session open | Would fit the wait-for-the-session-to-start instruction at `[00:46:39]` | NONE |

```text
Classification:          INFERRED MACHINE CANDIDATE
Canonical Course Status: NOT A COURSE RULE
```

### Current Status

```text
DO NOT CODE
```

### Required Research

A later lesson with a labelled example, or a screenshot showing a first and second leg marked. The two candidates above lead to materially different entries.

### Impact If Wrong

High. It is the lesson's only stated entry-timing preference. If "leg" is defined wrongly the trader enters on the move the instructor is warning against.

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-011 (M and W) |
| Interpretation | `03_LESSON_NOTES/V01_INTERPRETATION.md` I3, G2 |

---

## A-008 — "the tracer"

### Course Meaning

Named as the one element that varies from week to week — "the only difference between one week to the next is where the tracer falls". At `[00:38:57]` it appears to be two lines drawn on a slide marking Sunday and Monday. Whether it is a chart annotation, a time marker, or a price level is not stated.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V01 | `00:38:57` | "this is the tracer Sunday Monday, right? These two lines. This is Sunday." |
| V01 | `00:52:50` | "the only difference between one week to the next is where the tracer falls" |

### Visual Characteristics

> **CORRECTED 2026-08-10 (review R3, action 3).** This field previously read: *"**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost."* 22 frames were subsequently captured and I-006 is `RESOLVED`. Original wording retained so the change is visible. The determination below is the student's, made against the frames named, and was flagged as required work by review R2 Part 3.3.

**Materially constrained by the frames; still not defined.** The words at `[00:38:57]`
("this is the tracer Sunday Monday, right?"), `[00:39:02]` ("**These two lines.**") and
`[00:39:03]` ("This is Sunday") are spoken over the "Beginning Of Week" chart, captured
at `[00:38:50]`, `[00:39:10]` and `[00:39:40]`.

`V01_00-38-50_beginning-of-week-chart.png` shows **exactly two vertical dotted lines near
the left edge**, with the pale-blue rectangle beginning at the second. Two lines, in the
week-open region, at the moment he says "these two lines… this is Sunday": the referent
is almost certainly that pair of vertical day separators.

**Recorded as constrained, not resolved,** for two reasons that matter:

1. The deixis is not verifiable from a still frame — he is pointing with a cursor that
   the capture does not track, and "these two lines" could in principle name the two
   dotted lines, two of the four moving averages, or two horizontal levels. The dotted
   pair is the best fit; it is not proof.
2. Even granting the identification, **nothing states what draws the lines, what the
   tracer measures, or why "where the tracer falls" is the one thing that varies week to
   week** (`[00:52:50]`). Identifying a mark is not defining a concept.

This is still a genuine gain: the record previously held that the tracer had no visual
referent at all. **Status unchanged: `DO NOT CODE`.**

### Counter-examples

None. V01 shows no example where this was rejected or explicitly not applied. Counter-examples are what would bound this concept, and the lesson provides none.

### Possible Measurable Features

| # | Candidate measure | Rationale | Course support |
|---|---|---|---|
| 1 | A vertical time separator marking the week open | "These two lines" plus "Sunday Monday" reads as vertical day boundaries | NONE |
| 2 | The starting position of the cycle within the week | `[00:52:56]` — "sometimes this might start Sunday, Monday… sometimes it might start on Thursday" — immediately follows the "where the tracer falls" line | NONE — but this is the closer contextual fit |

```text
Classification:          INFERRED MACHINE CANDIDATE
Canonical Course Status: NOT A COURSE RULE
```

### Current Status

```text
DO NOT CODE
```

### Required Research

~~A screenshot of `[00:38:57]`.~~ **Obtained** — see Visual Characteristics above; it
constrains the referent without defining the term. What is still needed is a lesson that
says what the tracer *is*. This term is unusual enough that it may be idiosyncratic to
this instructor and may not recur; watch V02–V05. (It does not appear in V02.)

### Impact If Wrong

Medium. If the tracer is the cycle's phase within the week, it is the parameter that determines everything else, and misreading it as a mere annotation would discard the lesson's one stated variable.

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-001, A-012 |

---

## A-009 — "stop hunt high drop / straight drop"

### Course Meaning

Named formations, spoken four times in fourteen seconds while pointing at a chart, with no description whatsoever. These are given as the entries a struggling trader should take.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V01 | `00:39:47` | "The [?stop hunt?] high drop away from the peak" — transcribed "The pun high drop" |
| V01 | `00:51:42` | "take shorts off of stop on[?] high drop. Stop on high drop. Stop on high drop straight drop." |
| V01 | `00:51:53` | "Straight drop with a little pin right there. Straight drop." |

### Visual Characteristics

> **CORRECTED 2026-08-10 (review R3, action 3).** This field previously read: *"**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost."* 22 frames were subsequently captured and I-006 is `RESOLVED`. Original wording retained so the change is visible.

**Constrained by the frames; no anatomy.** See the *Visual Evidence Update* at the foot
of this record: `[00:51:45]` and `[00:52:10]` capture the instructor's live green marks
over the decline he is naming. They fix *where* on the chart he is pointing. They yield
no leg count, no proportion, no invalidation, and nothing on either frame is labelled
"stop hunt high drop" or "straight drop".

### Counter-examples

None. V01 shows no example where this was rejected or explicitly not applied. Counter-examples are what would bound this concept, and the lesson provides none.

### Possible Measurable Features

| # | Candidate measure | Rationale | Course support |
|---|---|---|---|
| 1 | A spike above a prior high that closes back below it, followed by directional decline | "stop hunt" + "high" + "drop" read compositionally | NONE — this is decomposing a name, not evidence |
| 2 | "Straight drop" as a distinct variant without the preceding spike | The instructor names them separately and contrasts one as having "a little pin" | PARTIAL — he does distinguish them |

```text
Classification:          INFERRED MACHINE CANDIDATE
Canonical Course Status: NOT A COURSE RULE
```

### Current Status

```text
DO NOT CODE
```

### Required Research

~~A screenshot of `[00:51:42]`–`[00:51:56]`. Ten seconds of video would resolve what
fourteen seconds of audio cannot.~~ **Obtained** (`[00:51:45]`, `[00:52:10]`) — and the
ten seconds did *not* resolve it. The frames show freehand strokes over the decline, not
a labelled construction. It is no longer a name with no referent; it is a name with a
location and no anatomy. What is needed is a later lesson that names the formation
against a marked shape.

### Impact If Wrong

High. These are the only named entry formations in V01 and they are prescribed to the lesson's target audience. Guessing at the shape from the name is exactly the failure this log exists to prevent.

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-002, A-010 |
| Interpretation | `03_LESSON_NOTES/V01_INTERPRETATION.md` §4 V5 |

---

### Visual Evidence Update — 2026-08-10

`V01_00-51-45_typical-week-drawn-on.png` and `V01_00-52-10_typical-week-more-drawing.png`
capture the instructor's live green freehand marks over the decline he is naming while
saying "stop [hunt] high drop… straight drop with a little pin right there".

The marks show *where* on the chart he is pointing, which is more than the audio gave.
They are freehand strokes over a sequence of candles, not a labelled construction, so
they still do not yield an anatomy: no leg count, no proportion, no invalidation.

**Status unchanged: `DO NOT CODE`.**
## A-010 — "peak formation high or low"

### Course Meaning

A structural anchor on the weekly cycle. Introduced only inside an anecdote about a former student, not taught. Later used to describe where the anchor point sits — "away from the peak formation". Whether it is the anchor point, marks the anchor point, or is a different object entirely is **not stated**.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V01 | `00:34:26` | "She identified on the weekly cycle the peak formation high or low." |
| V01 | `00:39:47` | "…away from the peak" |
| V01 | `00:51:26` | "you only are trading one direction till Friday away from the peak formation down short" |

### Visual Characteristics

> **CORRECTED 2026-08-10 (review R3, action 3).** This field previously read: *"**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost."* 22 frames were subsequently captured and I-006 is `RESOLVED`. Original wording retained so the change is visible.

**Screenshots exist and none bears on this term.** All 22 V01 frames were read
(`04_SCREENSHOTS/V01/INDEX.md`). None prints "peak formation". This is a more useful
statement than "no screenshot exists", and it carries weight for `I7`: `[00:50:55]` is
the lesson's fullest annotated depiction of the weekly cycle, it carries five printed
labels, and **not one of them says "peak formation", "anchor point", "M" or "W"**. The
visual channel therefore does *not* merge these terms. See `V01_INTERPRETATION.md`
§10.3.

### Counter-examples

None. V01 shows no example where this was rejected or explicitly not applied. Counter-examples are what would bound this concept, and the lesson provides none.

### Possible Measurable Features

| # | Candidate measure | Rationale | Course support |
|---|---|---|---|
| 1 | The extreme high or low of the weekly cycle, as a single price point | "high or low" is stated | PARTIAL |
| 2 | A multi-bar formation whose extreme is the reference point | "formation" implies structure rather than a single point | NONE |

```text
Classification:          INFERRED MACHINE CANDIDATE
Canonical Course Status: NOT A COURSE RULE
```

### Current Status

```text
DO NOT CODE
```

### Required Research

A later lesson teaching it directly. Note that V01 introduces it via anecdote, which strongly suggests it was taught before this recording — possibly in material outside this 21-video library.

### Impact If Wrong

Foundational, and compounded: if this is the same object as the anchor point (A-001) then two records describe one concept; if it is not, then the corpus has two undefined foundational objects that were merged by a careless reading. Either error propagates everywhere.

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-001, A-011 |
| Interpretation | `03_LESSON_NOTES/V01_INTERPRETATION.md` I7, G4, Q1 |

---

## A-011 — "M and W formation"

### Course Meaning

Treated throughout as already known. It appears in the student survey as something a competent student should "clearly see", is named as the shape of the anchor point, is what a trader thinks he has before being stopped out, and is what the dealer makes regardless of news. **V01 never describes it.** No leg count, no timing, no proportions, no invalidation.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V01 | `00:17:45` | Survey question 5: "Do you clearly see M's and W's before they shift away from the level?" |
| V01 | `00:27:35` | "Do you see the M and W before the dealer snatches it away? That's the question." |
| V01 | `00:34:47` | "you identify the anchor point of the cycle, W or M formation, multi session" |
| V01 | `00:46:28` | "you sit there stunned and watch it because you thought you had the M or W formation" |
| V01 | `00:53:51` | "They still make an M&W formation and drop [or] rise price." |
| V01 | `00:54:04` | "M&W weekly cycles, they use that shit as the reason to trick you." |

### Visual Characteristics

> **CORRECTED 2026-08-10 (review R3, action 3).** This field previously read: *"**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost."* 22 frames were subsequently captured and I-006 is `RESOLVED`. Original wording retained so the change is visible.

**Printed evidence exists; still no anatomy.** Survey question 5 on
`V01_00-16-55_survey-questions-1-to-9.png` prints *"Do you clearly see M's/W's before
they **SHIFT**?"*.

What that adds: the term is confirmed as the instructor's own printed vocabulary rather
than an ASR reading, and the survey slide shows he treats seeing them "before they
shift" as a rateable competence — i.e. as something that happens *in advance*, which is
a stronger claim than anything he says aloud about M's and W's.

What it does not add: **no chart slide in V01 labels an M or a W anywhere.** The
`[00:50:55]` "Typical Week" chart, which would be the natural place, prints five
annotations and names neither letter. No leg count, no proportion, no timing, no
invalidation. **Status unchanged: `DO NOT CODE`.**

> **Correction to review R2 Part 3.3.** R2 recorded that "SHIFT" is a term that appears
> **nowhere** in the transcript and proposed logging it as a printed-only vocabulary
> item. That is not correct and is not adopted. The instructor reads the question aloud
> at `[00:17:45]` — *"Do you clearly see M's and W's before they shift away from the
> level?"* — and again in garbled form at `[00:27:35]`. The slide is the *shortened*
> form; the spoken version carries the extra qualifier *"away from the level"*, which is
> the more informative of the two and ties the term to `A-004`. Verified against the
> transcript at R3.

### Counter-examples

None. V01 shows no example where this was rejected or explicitly not applied. Counter-examples are what would bound this concept, and the lesson provides none.

### Possible Measurable Features

| # | Candidate measure | Rationale | Course support |
|---|---|---|---|
| 1 | A double-top (M) or double-bottom (W) structure | The letter shapes are conventional in technical analysis | NONE from this course — importing the external convention is precisely the substitution the naming standard forbids |
| 2 | A multi-session structure spanning two or more trading sessions | `[00:34:47]` says "multi session over Tuesday, Wednesday or Monday, Tuesday" | PARTIAL — this is stated |

```text
Classification:          INFERRED MACHINE CANDIDATE
Canonical Course Status: NOT A COURSE RULE
```

### Current Status

```text
DO NOT CODE
```

### Required Research

A later lesson describing it. Until then, resist filling it in from general technical-analysis knowledge; the instructor's usage (`[00:46:28]` — traders *think* they have one and get stopped) suggests his definition is stricter than the conventional one.

### Impact If Wrong

Foundational. It is the shape of the anchor point, the thing the survey treats as core competence, and the thing the dealer allegedly always produces. Substituting the textbook double-top definition would quietly replace the course's concept with a different one.

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-001, A-007, A-010 |
| Interpretation | `03_LESSON_NOTES/V01_INTERPRETATION.md` I7, §4 |

---

## A-012 — "midweek reversal"

### Course Meaning

An alternative cycle shape in which the turn occurs mid-week rather than at the week's start. Named twice, once in the survey and once at the end of the teaching section. Never described.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V01 | `00:21:43` | Survey: "Can you identify a midweek reversal? Can you see it? Do you understand that it's coming?" |
| V01 | `00:53:02` | "Sometimes it might start on Thursday. You might get the midweek reversal." |

### Visual Characteristics

> **CORRECTED 2026-08-10 (review R3, action 3).** This field previously read: *"**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost."* 22 frames were subsequently captured and I-006 is `RESOLVED`. Original wording retained so the change is visible.

**Printed evidence exists; no description.** Survey question 16 on
`V01_00-19-20_survey-questions-10-to-18.png` prints *"Can you identify a mid week
reversal  1-10"*. This confirms the term and its spelling as the instructor's, and
confirms he treats identifying one as a rateable competence.

No chart slide in V01 shows or labels a midweek reversal. **Status unchanged:
`DO NOT CODE`.**

### Counter-examples

None. V01 shows no example where this was rejected or explicitly not applied. Counter-examples are what would bound this concept, and the lesson provides none.

### Possible Measurable Features

| # | Candidate measure | Rationale | Course support |
|---|---|---|---|
| 1 | A weekly cycle whose anchor point forms Wednesday or later | `[00:53:02]` pairs it with a Thursday start | PARTIAL — the timing hint is stated |

```text
Classification:          INFERRED MACHINE CANDIDATE
Canonical Course Status: NOT A COURSE RULE
```

### Current Status

```text
DO NOT CODE
```

### Required Research

A later lesson. The survey question implies it is predictable in advance ("do you understand that it's coming?"), which if true is a substantial claim requiring its own evidence.

### Impact If Wrong

Medium. It is the stated exception to the Sunday/Monday cycle start. Missing it means half the weekly-cycle logic applies to weeks it was never meant for.

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-001, A-008 |

---

## A-013 — "struggling / more experienced / more proficient"

### Course Meaning

A skill threshold that **gates two different rules**. Struggling traders must take only trading-zone setups and only shorts after a mid-week anchor; experienced traders may treat the blue box as a guide and may trade both directions. No test, metric, or milestone for crossing the threshold is given.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V01 | `00:44:03` | "When you become more experienced at grabbing the perfect setups, you can start to see that the blue box is more of a guide." |
| V01 | `00:44:15` | "if you are struggling and having problems identifying the setups, then I need you to take only those trades…" |
| V01 | `00:51:34` | "When you become more proficient, you can trade both ways." |
| V01 | `00:51:38` | "right now, if you're struggling, I want you to try to identify the anchor point and take shorts…" |

### Visual Characteristics

> **CORRECTED 2026-08-10 (review R3, action 3).** This field previously read: *"**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost."* 22 frames were subsequently captured and I-006 is `RESOLVED`. Original wording retained so the change is visible.

**One printed item bears on candidate measure 1, and it does not close the gap.** Survey
question 12 on `V01_00-19-20_survey-questions-10-to-18.png` prints *"Have you doubled a
demo account?  Y  N"*. That is the printed origin of the `[00:20:00]` bar quoted in the
candidate table below.

It does **not** define the threshold. It is a yes/no fact about a student, asked in a
self-rating survey, and the instructor attaches it to *going live* — not to relaxing the
blue-box rule or to trading both directions. The gap this record exists to hold open is
between "struggling" and "more proficient" as used at `[00:44:03]`, `[00:44:15]`,
`[00:51:34]` and `[00:51:38]`, and nothing printed or spoken in V01 bridges it.
**Status unchanged: `DO NOT CODE`.**

### Counter-examples

None. V01 shows no example where this was rejected or explicitly not applied. Counter-examples are what would bound this concept, and the lesson provides none.

### Possible Measurable Features

| # | Candidate measure | Rationale | Course support |
|---|---|---|---|
| 1 | Doubling a demo account, per `[00:20:00]` | It is the one competence bar the instructor states anywhere in V01, though he states it as a live-trading gate rather than a rule-relaxation gate | PARTIAL — stated, but for a different purpose |
| 2 | A measured hit-rate on labelled setups | Would make the gate testable | NONE |

```text
Classification:          INFERRED MACHINE CANDIDATE
Canonical Course Status: NOT A COURSE RULE
```

### Current Status

```text
DO NOT CODE
```

### Required Research

A later lesson stating a progression criterion. Note that this may never be defined — the instructor may treat it as a matter of judgement, in which case the correct outcome is a permanent `DO NOT CODE`, not a threshold.

### Impact If Wrong

High and structural. Two rules exist in strict and relaxed forms with an unmeasurable switch between them. Any implementation must pick one form, and picking silently means shipping a rule the course states conditionally as though it were absolute.

### Related

| Type | Reference |
|---|---|
| Contradiction | C-002 |
| Interpretation | `03_LESSON_NOTES/V01_INTERPRETATION.md` I6, I10, Q8 |

---

## A-014 — "fractional disparity"

### Course Meaning

Named once, as survey question 8 — "How are you at spotting fractional disparity?" — and never mentioned again in V01. No meaning is given. Logged because the survey is the instructor's own inventory of expected competencies, so this is something he considers part of the method.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V01 | `00:18:16` | Survey question 8: "How are you at spotting fractional disparity?" |

### Visual Characteristics

> **CORRECTED 2026-08-10 (review R3, action 3).** This field previously read: *"**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost."* 22 frames were subsequently captured and I-006 is `RESOLVED`. Original wording retained so the change is visible.

**Printed evidence exists; still no meaning.** Survey question 8 on
`V01_00-16-55_survey-questions-1-to-9.png` prints *"How are you at spotting Fractional
Disparity?  1 - 10"*, capitalised as a proper term.

That settles the transcription — the phrase is real, is spelled this way, and is
capitalised by the instructor as a named concept — and settles nothing else. Nothing in
V01 explains it, and no chart slide illustrates it. **Status unchanged: `DO NOT CODE`.**

### Counter-examples

None. V01 shows no example where this was rejected or explicitly not applied. Counter-examples are what would bound this concept, and the lesson provides none.

### Possible Measurable Features

| # | Candidate measure | Rationale | Course support |
|---|---|---|---|
| 1 | (none proposed) | Nothing in V01 constrains the meaning enough to propose a measure | NONE |

```text
Classification:          INFERRED MACHINE CANDIDATE
Canonical Course Status: NOT A COURSE RULE
```

### Current Status

```text
DO NOT CODE
```

### Required Research

A later lesson. If none of V02–V21 defines it, that is itself a finding — it would confirm the survey references material outside this library.

### Impact If Wrong

Unknown. It cannot be assessed without knowing what it is. Logged so it is not silently dropped.

### Related

| Type | Reference |
|---|---|
| Interpretation | `03_LESSON_NOTES/V01_INTERPRETATION.md` Q10 |

---

## A-015 — "shows something to the traders"

### Course Meaning

The inducement step of the core sequence: the dealer creates an appearance that persuades retail traders to take a position. Described only by its effect ("he shows longs") and by one instance of its mechanism ("look at the moving averages fan out").

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V01 | `00:39:19` | "And shows something to the traders." |
| V01 | `00:39:26` | "Look at the moving averages fan out. He shows something to the traders. He shows longs, right?" |
| V01 | `00:54:26` | "use people to go short by showing them something and use people to go long by showing them something else" |

### Visual Characteristics

> **CORRECTED 2026-08-10 (review R3, action 3).** This field previously read: *"**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost."* 22 frames were subsequently captured and I-006 is `RESOLVED`. Original wording retained so the change is visible.

**Constrained by the frames.** See the *Visual Evidence Update* at the foot of this
record: four moving-average lines (yellow, red, cyan, white) are present on every chart
slide, with **no period or setting printed anywhere**. The inversion warning below is
unaffected and better supported.

### Counter-examples

None. V01 shows no example where this was rejected or explicitly not applied. Counter-examples are what would bound this concept, and the lesson provides none.

### Possible Measurable Features

| # | Candidate measure | Rationale | Course support |
|---|---|---|---|
| 1 | Moving-average separation/fanning in one direction | It is the one concrete instance given, at `[00:39:26]` | PARTIAL — but note this is described as **bait**, not as an entry signal. Coding it as an entry inverts the lesson. |
| 2 | Any conventionally bullish or bearish technical appearance | `[00:54:26]` is deliberately general | NONE |

```text
Classification:          INFERRED MACHINE CANDIDATE
Canonical Course Status: NOT A COURSE RULE
```

### Current Status

```text
DO NOT CODE
```

### Required Research

Later lessons showing what the dealer displays at each stage. ~~The `[00:39:26]`
moving-average reference … warrants a screenshot before anything is built on it.~~ **The
screenshots were taken and they showed four MA lines with no periods printed anywhere**
(see the Visual Evidence Update below, and A-020 for the same negative result in V02).
What is needed is a frame showing the platform's indicator list or a legend — no V01 or
V02 frame carries one.

### Impact If Wrong

Medium, with a specific inversion risk: this is the lesson's one mention of moving averages, and it describes them as the trap. A careless later reading could turn "moving averages fan out" into an entry condition, producing a system that does exactly what V01 warns against.

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-002 |
| Interpretation | `03_LESSON_NOTES/V01_INTERPRETATION.md` §2 "Explicitly NOT interpreted" |

---

### Visual Evidence Update — 2026-08-10

Four moving-average lines are visibly present on every chart slide in the lesson —
**yellow, red, cyan and white**. This corroborates `[00:39:26]` "look at the moving
averages fan out" as describing something genuinely on the instructor's template.

**No period or setting appears anywhere on any slide.** The lines exist; their values do
not. The refusal in `V01_INTERPRETATION.md` §2 to name EMA periods is unaffected and now
better supported.

The inversion warning stands and is strengthened: the MAs are shown in the context of
what the dealer *displays to induce a position*, not as an entry signal.

**Status unchanged: `DO NOT CODE`.**
## A-016 — "goes into chop"

### Course Meaning

The state price enters after the end-of-week trap, in which a correct-looking position stops working. "Just because you're in it, he's not going to continue."

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V01 | `00:44:41` | "you happen to catch this right here in your short and all of a sudden you see an outside spike to the low and the dealer goes into chop" |
| V01 | `00:44:49` | "Just because you're in it, he's not going to continue." |

### Visual Characteristics

> **CORRECTED 2026-08-10 (review R3, action 3).** This field previously read: *"**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost."* 22 frames were subsequently captured and I-006 is `RESOLVED`. Original wording retained so the change is visible. The determination below is the student's, made against the frame named, and was flagged as required work by review R2 Part 3.3.

**Materially constrained by the frame; still not defined.** `[00:44:45]` — "you see an
outside spike to the low and the dealer goes into chop" — is spoken over the "End Of
Week" chart, captured at `[00:44:40]`.

`V01_00-44-40_end-of-week-chart.png` shows the described sequence: a decline out of the
dark-red rectangle, a **deep single-candle spike low** whose lower wick runs well below
every surrounding candle, and then a sideways range that persists to the right of the
two vertical dotted separators, where the pale-blue rectangle is drawn over it.

**What this adds:** the words map onto a real, locatable sequence on the instructor's own
example, so "chop" is not a figure of speech — it names a visible state, and it follows
the spike rather than preceding it.

**What it does not add:** no range, no duration, no bar count, no volatility measure, and
no statement of when chop ends. One instance cannot bound any of them, and the frame
carries no printed label for the region. **Status unchanged: `DO NOT CODE`.**

### Counter-examples

None. V01 shows no example where this was rejected or explicitly not applied. Counter-examples are what would bound this concept, and the lesson provides none.

### Possible Measurable Features

| # | Candidate measure | Rationale | Course support |
|---|---|---|---|
| 1 | A period of range-bound movement following a range extension, measured by reduced directional persistence | "goes into chop" after "an outside spike" is the stated sequence | NONE |

```text
Classification:          INFERRED MACHINE CANDIDATE
Canonical Course Status: NOT A COURSE RULE
```

### Current Status

```text
DO NOT CODE
```

### Required Research

A later lesson, or a labelled example. ~~"Outside spike to the low" at `[00:44:41]` …
may be recoverable from a screenshot.~~ **Recovered** at `[00:44:40]` — see Visual
Characteristics above. The sequence is visible; the *measure* of chop is not, and one
instance cannot supply one.

### Impact If Wrong

Medium. It is the stated end-of-week failure mode and the justification for not holding into the weekend. Defining it wrongly affects exit timing rather than entry logic.

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-002 |
| Interpretation | `03_LESSON_NOTES/V01_INTERPRETATION.md` I5 |

---

## A-017 — "big entry candle"

### Course Meaning

The closest thing to an entry trigger in V01 — four words, spoken while pointing at a chart, with no size, no comparison basis, and no timeframe.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V01 | `00:48:33` | "Don't trade this as a short. This is the opportunity." |
| V01 | `00:48:41` | "That's a big entry candle." |

### Visual Characteristics

> **CORRECTED 2026-08-10 (review R3, action 3).** This field previously read: *"**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost."* 22 frames were subsequently captured and I-006 is `RESOLVED`. Original wording retained so the change is visible.

**Constrained by the frame.** See the *Visual Evidence Update* at the foot of this
record: `[00:48:35]` shows a single large green candle breaking upward out of the blue
range immediately before the red trap area. The slide does not label it, and one
unlabelled instance cannot bound a size threshold.

### Counter-examples

None. V01 shows no example where this was rejected or explicitly not applied. Counter-examples are what would bound this concept, and the lesson provides none.

### Possible Measurable Features

| # | Candidate measure | Rationale | Course support |
|---|---|---|---|
| 1 | Candle range exceeding a multiple of recent average range | "big" implies a comparison, and the comparison basis is exactly what is missing | NONE |
| 2 | Candle range exceeding the preceding N candles' combined range | Alternative comparison basis with materially different results | NONE |

```text
Classification:          INFERRED MACHINE CANDIDATE
Canonical Course Status: NOT A COURSE RULE
```

### Current Status

```text
DO NOT CODE
```

### Required Research

~~A screenshot of `[00:48:41]`~~ — **obtained** at `[00:48:35]`, and it is a single
unlabelled instance, which cannot bound a size threshold. What is needed is later lessons
using the phrase with **more than one** example, or one where the comparison basis is
stated.

### Impact If Wrong

Medium. It is the only entry-trigger language in the lesson. Attaching a number to "big" during the Student Phase is precisely the premature quantification this log exists to prevent (reviewer error codes E12, E15).

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-002, A-009 |

### Visual Evidence Update — 2026-08-10

`V01_00-48-35_trap-higher-level-long-holders.png` shows a single large green candle
breaking upward out of the blue range immediately before the red trap area, under the
printed title "Trap Here..Higher Level Long Holders".

That is very likely the candle referred to at `[00:48:41]` — but the slide does not label
it, and one unlabelled instance cannot bound a size threshold. Comparing it to
neighbouring candles to derive a multiple would be exactly the premature quantification
this log exists to prevent.

**Status unchanged: `DO NOT CODE`.**

---

## A-018 — "R = <number>" labels attached to the shaded boxes

### Course Meaning

Unknown. Numeric labels printed against the blue and red rectangles on one chart slide.
The instructor does not read them aloud or explain them anywhere in V01.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V01 | `[00:48:35]` | Dark-red rectangle labelled `R = 70.5`; pale-blue rectangle at right labelled `R = 51…` (truncated by the frame edge); pale-blue rectangle at left labelled `= 43.1`. Screenshot: `04_SCREENSHOTS/V01/V01_00-48-35_trap-higher-level-long-holders.png` |

### Visual Characteristics

Each label sits at the lower edge of a shaded rectangle. The values are in the 40–75
range. The rectangles span both price and time, but the label is a single scalar.

### Counter-examples

None. Only one slide in V01 shows these labels; the other chart slides carry rectangles
without visible `R =` text.

### Possible Measurable Features

| # | Candidate measure | Rationale | Course support |
|---|---|---|---|
| 1 | **Range of the boxed area, in pips** | The same MT4 template prints `Previous Days Range= 146.4` and `Current Days Range= 110.6` in its header at `[00:50:55]`, so "Range" is already a template concept expressed in pips at this magnitude. The labelled objects are rectangles spanning a price span. | PARTIAL — consistent, not stated |
| 2 | A risk-to-reward ratio | "R" is conventional shorthand for R-multiple in retail trading | **NONE — and actively doubted.** V01 states no stop, no target and no position size, so there is nothing for an R-multiple to be computed from. Adopting this reading would manufacture a target rule out of a label. |

```text
Classification:          INFERRED MACHINE CANDIDATE
Canonical Course Status: NOT A COURSE RULE
```

### Current Status

```text
DO NOT CODE
```

### Required Research

A later lesson using the same template and explaining the label, or a frame where the
truncated `R = 51…` value is fully visible alongside a measurable box. Cheap to revisit:
the full V01 mp4 is retained, so any nearby frame can be extracted in seconds.

### Impact If Wrong

Reading `R` as risk-to-reward would insert a target/risk rule into a lesson that states
none — the exact fabrication pattern that caused 72 files to be quarantined
(`00_SYSTEM/QUARANTINE_REGISTER.md` Q-001). This record exists mainly to make sure that
misreading is never made silently.

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-004 (level), A-006 (the boxes) |
| Interpretation | `03_LESSON_NOTES/V01_INTERPRETATION.md` §10.4 |

---

## A-019 — session times with no timezone stated

### Course Meaning

A set of clock times that gate every timing instruction in V02: "3 to 3:30 is the gap,
4 o'clock session open"; "the pattern has to come in around 3, 4 o'clock — 3:30, 4:30";
"at 9:30 this is the candle that paints"; "the vector candle at the release of the news
at 8:31"; "the vector candle at 4:30 London".

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V02 | `[00:50:32]` | "3 to 3.30 is the gap, 4 o'clock session open." |
| V02 | `[00:50:42]` | "The pattern has to come in around 3, 4 o'clock, 3.30, 4.30 in that range into the new session. You got to trade." |
| V02 | `[00:47:34]` | "You need to know that at 9.30, this is the candle that paints. At 9.45, this is the candle that paints on my platform." |
| V02 | `[00:43:55]` | "Using the vector candle at the release of the news at 831." |
| V02 | `[00:43:59]` | "Using the vector candle at 430 London." |
| V02 | `[00:51:03]` | "Forex Factory shows New York open at 8… Forex Factory is clueless." |
| V01 | `[00:46:09]` | "US session starts at 930 New York Eastern" — the one clean, timezone-qualified value in the course so far. |

### Why it is unresolved

Only two of these carry any timezone marker: "4:30 **London**", and V01's "930 New York
**Eastern**". The rest are bare numbers. The 3:00/3:30/4:00 group is almost certainly not
New York time if it denotes the London open, which means at least two timezones are in
use in a single list with only one of them labelled.

**The instructor explicitly refuses to reason about it.** At `[00:49:52]`–`[00:50:16]`:
"I was taught these are the times, and the only adjustment for daylight savings is for
us — that 9:30… Listen, don't analyse it. I was taught if it works… the answer was,
don't worry about it. These are the times." He also says at `[00:49:22]` that he cannot
ask the person who taught him because "the guy died", and at `[00:50:26]` that "we back
up the London session in the winter" — i.e. the whole table shifts seasonally by an
unstated amount.

So this is not a transcription gap. The source itself declines to specify.

### Possible Measurable Features

| # | Candidate reading | Rationale | Course support |
|---|---|---|---|
| 1 | 3:00/3:30/4:00 are **New York Eastern**, describing the London session as seen from NY | Consistent with V01's "930 New York Eastern" for the US session, and with a 3–4 am ET London open | PARTIAL — arithmetically plausible, never stated |
| 2 | They are London local time | "4:30 London" is adjacent in the same list | **Weak** — would put the "session open" at 4 am London, which does not match a London open |
| 3 | The lesson's slide shows the timezone | Not audible; the times are read off a slide he calls up at `[00:49:16]` | **Testable from screenshots** |

### Current Status

```text
DO NOT CODE
```

### Required Research

A screenshot of the session-times slide (this lesson displays one — see
`04_SCREENSHOTS/V02/`), or a later lesson that states the zone. This is the cheapest
open ambiguity in the project to resolve and the highest-leverage: it unblocks M3, M6,
I21, I29 and I30 in `V02_INTERPRETATION.md` at once.

### Impact If Wrong

Every time-gated rule fires at the wrong hour. A three-hour error would place the
"pattern arrival window" in the middle of the Asian session instead of the London open,
inverting the method.

### Related

| Type | Reference |
|---|---|
| Interpretation | `03_LESSON_NOTES/V02_INTERPRETATION.md` I21, I29, I30, M3, M6 |
| Source | `03_LESSON_NOTES/V02_SOURCE_NOTES.md` §2k, §10 |

---

## A-020 — "mayonnaise"

### Course Meaning

A moving average plotted on the instructor's chart, referred to only by this nickname.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V02 | `[00:19:46]` | "That one in this example paid out because there was enough distance between the entry and the mayonnaise to make it worth your while." |
| V02 | `[00:25:18]` | "Consolidates, straight rise out of here. Right back to the mayonnaise." |
| V02 | `[00:25:45]` | "So now, support/resistance, you can use the low as resistance and look for an M formation here. And it just so happens to coincide with the mayonnaise." |
| V02 | `[00:05:00]` | ⚠ **PROBABLE, NOT CONFIRMED.** ASR: "you can go, oh man, Steve, this looks like perfect pins to the **manays**." |

> **Added 2026-08-10 (V02 review R1, finding 9).** `[00:05:00]`'s *"manays"* is very
> likely a fourth "mayonnaise", but it is **a different string in the transcript and no
> audio re-check has been performed**, so it is recorded as probable and is *not* adopted
> as a confirmed fourth instance. Per `REVIEW_PROTOCOL.md` §15, an attractive reading is
> not promoted to certain because it is convenient.
>
> **Why it is worth recording anyway.** It is the only usage in which the average behaves
> as a **magnet that price travels to** — "perfect pins to the manays" — rather than as a
> support/resistance reference (`[00:25:45]`) or a distance measure (`[00:19:46]`). If it
> is genuine it slightly strengthens candidate 2 below (the slowest/most prominent
> average), because a magnet across a multi-hour move suits a slow average. **It does not
> change the status**, which stays `DO NOT CODE`.
>
> Also noted: the surrounding context is a **short** setup — `[00:04:56]` "You should not
> be looking for longs is what I'm saying" — so the pin is downward to the average, not a
> bounce off it. Recorded because direction would matter if this were ever coded, and it
> is the sort of detail that gets lost when a probable reading is later promoted.

### Why it matters more than a nickname should

It is not decorative. At `[00:19:46]` the distance from entry to the mayonnaise is the
stated reason a trade was "worth your while" — that is a viability filter. At
`[00:25:45]` it is a confluence factor for locating an M formation. Both are decision
inputs.

### What is NOT evidence

The quarantined `NOTES.md` for this lesson asserts a full colour scheme —
*5 Mustard, 13 Water, 50 Mayo, 200 Blueberry, 800 Raspberry*. That file is fabricated
(`QUARANTINE_REGISTER.md` Q-002) and **must not be used to resolve this record**, even
though "mayo" appears in it and "mayonnaise" is genuinely spoken. A fabricated document
containing one true-sounding token is still not a source. Note also that V01's
transcript contains the garbled *"the water that catch up in the mustard"*
(`V01 [00:19:24]`), which suggests "water" and "mustard" are also real course terms —
but *suggests* is the operative word, and no mapping to a period has been heard in
either lesson.

### Possible Measurable Features

| # | Candidate | Rationale | Course support |
|---|---|---|---|
| 1 | A specific EMA period, identifiable from a chart legend | The instructor's MT4 template prints indicator settings | **Testable from screenshots** |
| 2 | The slowest/most prominent average on the chart | It acts as support/resistance across a whole week, which suits a slow average | INFERRED — no course support |

### Current Status

```text
DO NOT CODE
```

### Required Research

A screenshot showing the chart's indicator list or a labelled average, at a timestamp
where he says the word. `[00:25:18]` and `[00:25:45]` are 27 seconds apart on the same
chart and are the best candidates.

### Impact If Wrong

Assigning the wrong period would put a support/resistance reference in the wrong place
and would silently import an indicator rule the course never stated — the Q-001/Q-002
failure mode.

### Related

| Type | Reference |
|---|---|
| Quarantine | Q-002 Finding 2 |
| Interpretation | `03_LESSON_NOTES/V02_INTERPRETATION.md` Q2, §6 |

---

## A-021 — the letter sequence for "the cycle"

### Course Meaning

A mnemonic naming the order of formations in the dealer's cycle.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V02 | `[00:07:28]` | "You're looking for stop hunt high drop, stop hunt high drop, reverse. That's the cycle, **M-A-A-W**." |
| V02 | `[00:19:28]` | "Stop hunt low rise, the formation. **WVVM**, the cycle." |

### Conflict

Two different strings, twelve minutes apart, both introduced as "the cycle". They are
not anagrams of each other and cannot both be right as transcribed. Both were produced
by ASR from a spoken sequence of single letters, which is the transcription case most
prone to error.

Note the surrounding context differs in direction: `[00:07:28]` follows a *high drop*
(bearish) description, `[00:19:28]` follows a *low rise* (bullish) one. It is therefore
possible that these are two genuinely different sequences — a bearish cycle and a
bullish cycle — rather than one sequence transcribed two ways. **The lesson does not
say this**, and adopting it would be inventing a distinction to reconcile the source.

### Current Status

```text
DO NOT CODE
```

### Required Research

Screenshots of the slide at either timestamp, if the sequence is written down. Failing
that, careful re-listening to both points at reduced speed. Cheap either way — the full
V02 mp4 is retained.

### Impact If Wrong

Low for trading, high for comprehension: this string appears to encode the order of
formations across a cycle, which is the lesson's core object.

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-011 (M and W formation) |
| Interpretation | `03_LESSON_NOTES/V02_INTERPRETATION.md` Q4 |

---

## A-022 — "half-Batman"

### Course Meaning

Unknown. Used as an established term for one of two possible continuations after an
outside structure high.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V02 | `[00:20:33]` | "One of two things can happen when you hit outside structure high. **The dealer can half-Batman to the low**, or he can finish out the M formation in London and correct." |

### Why it is load-bearing

It is one branch of an explicitly closed binary. The instruction "one of two things can
happen" is only usable if both things can be recognised. The other branch ("finish out
the M formation in London") is itself dependent on A-011.

### Possible Measurable Features

| # | Candidate | Rationale | Course support |
|---|---|---|---|
| 1 | A shape term — "Batman" being a double-top-with-a-dip silhouette, "half" being one side of it | The name is visually suggestive and the course uses shape names (M, W, V) throughout | INFERRED — **no course support whatsoever.** Recorded only so the reasoning is visible and rejectable. |

**Do not adopt candidate 1.** It is pattern-matching on a word, which is precisely how
a plausible-sounding fabrication enters a record.

### Current Status

```text
DO NOT CODE
```

### Required Research

A later lesson defining it, or a screenshot at `[00:20:33]`–`[00:20:44]` showing what he
draws while saying it. The latter is likely: he is annotating a chart live at this point.

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-011 (M and W formation) |
| Interpretation | `03_LESSON_NOTES/V02_INTERPRETATION.md` I18, Q6 |

---

## A-023 — "33 trade"

### Course Meaning

Unknown. A named trade, introduced alongside the well-specified "22 trade" but not
decomposed the way "22" is.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V02 | `[00:22:16]` | "And day three, he issues a beautiful **33 trade** where he makes an aggressive move and fills the ADR completely. Or more than the ADR." |

### The trap

"22" is defined in this same lesson as *a second leg of a second leg* `[00:00:56]`. The
obvious inference is that "33" means *a third leg of a third leg*. But what he actually
attaches to "33" is a **day-three move that fills the ADR** — a statement about timing
and extent, not about leg structure. Those are different kinds of fact, and the lesson
never bridges them.

Adopting the leg-structure reading would be exactly the kind of tidy, plausible
inference this register exists to block.

### Current Status

```text
DO NOT CODE
```

### Required Research

A later lesson that defines it, or one that uses "33" in a context where leg structure
is visible.

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-007 (second leg) |
| Interpretation | `03_LESSON_NOTES/V02_INTERPRETATION.md` Q7 |

---

## A-024 — "slightly above" (the 22-trade overshoot tolerance)

### Course Meaning

How far the dealer may exceed the prior high while leaving a 22 setup valid.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V02 | `[00:01:28]` | "There can be a variation on the 22… The dealer can go **slightly above**, pull back. And you'll look like, oh no, this is invalidated. No." |
| V02 | `[00:01:38]` | "What makes it valid is that the dealer has fallen back below the previous high level." |
| V02 | `[00:29:37]` | "If he comes back just **slightly outside** the blue box, right? Same thing." |
| V02 | `[00:24:43]` | Related mechanism: "See how the spike **slightly** goes above? Slightly above the level right there… the dealer has the spread to reach a little higher with this big fat hand." |

### Assessment

This is a **partially self-resolving** ambiguity and is recorded as such. The *validity
test* he gives at `[00:01:38]` is genuinely objective in form: price must fall back
below the previous high level. That is checkable without knowing what "slightly" means.

What remains unmeasured is the upper bound — how far above is too far before the setup
is a genuine break rather than a stop-grab. `[00:24:51]` hints at a mechanism (the
dealer reaches up by roughly the spread) but states no number, and "the spread" is
broker-dependent.

### Possible Measurable Features

| # | Candidate | Rationale | Course support |
|---|---|---|---|
| 1 | No upper bound needed — the fall-back-below test is sufficient | It is the test he actually states | **This is the reading the source supports.** |
| 2 | Bounded by the spread | `[00:24:51]` | PARTIAL — mechanism named, no number, broker-dependent |

### Current Status

```text
DO NOT CODE
```

Reading 1 is close to codeable and is the honest reading, but it is recorded here rather
than promoted because it depends on "the previous high level" (A-004) and "the blue box"
(A-006) being defined.

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-004, A-006 |
| Interpretation | `03_LESSON_NOTES/V02_INTERPRETATION.md` I26 |

---

## A-025 — "a good close below"

### Course Meaning

The trigger condition for the only numeric exit rule stated in V02.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V02 | `[00:39:09]` | "If you're in a trade and the dealer cuts the low or the high and starts going this way, don't sit there like a deer in the headlights." |
| V02 | `[00:39:19]` | "The dealer gives you **a good close below** and opens the next candle and starts dropping and you're only down 15. Eat it." |
| V02 | `[00:39:34]` | "Scratch out at minus 15, because then if you hit 25 or 30 on your next trade, you're up instead of even." |

### Why it matters

The −15 scratch-out is one of the few fully numeric instructions in the lesson, and it
is the closest thing V02 has to loss control. But it does not fire on the number alone —
it fires on "a good close below" **plus** the next candle opening and dropping. Without
"good", the rule reduces to "exit at −15", which is a different and stricter rule than
the one he states.

### Unstated components

- **Timeframe.** No chart interval is given, so "a close" has no duration.
- **"Good".** Presumably means decisive rather than marginal — a close clearly beyond
  the level rather than a wick through it. Not stated.
- **"Below"** what. The level cut at `[00:39:09]`, most likely, but not said.

### Current Status

```text
DO NOT CODE
```

Specifically: **do not simplify this to a flat −15 stop.** That would convert a
conditional management action into an unconditional stop-loss rule, and V02 explicitly
defers stop-loss placement to a later lesson (`[00:17:39]`).

### Related

| Type | Reference |
|---|---|
| Interpretation | `03_LESSON_NOTES/V02_INTERPRETATION.md` I23, M4 |
| Source | `03_LESSON_NOTES/V02_SOURCE_NOTES.md` §2h, §6 |

---

## V02 EVIDENCE ADDED TO EXISTING RECORDS

V02 supplies further occurrences of six ambiguities first logged against V01. The
records above are new; these are extensions, kept here in one place rather than
scattered through the originals so the V02 pass is auditable as a unit.

| ID | V02 evidence | Effect on the record |
|---|---|---|
| **A-004** — "level" (countable) | `[00:33:11]` "especially when you're new and you can't count the levels" | Confirms level-counting is a taught skill not yet taught. No new information about the unit. Status unchanged. |
| **A-005** — "the trading zone" | `[00:45:52]` "we'll talk about the trading zone next week"; `[00:37:10]` "when the trading zone is set exactly the way I lay it out" | **Second deferral.** Index note updated from "Deferred to V02" to record V01→V02→V03. `[00:37:10]` newly establishes that the trading zone is the thing the Zaireen backtest was conditioned on, which raises its importance. |
| **A-006** — "the box" | `[00:12:15]`, `[00:29:37]` "slightly outside the blue box", `[00:37:26]` "second leg out of the box, 25 to 50 pips", `[00:43:48]` "sometimes they'll be below the box" | Substantially more usage, still no definition. `[00:37:26]` attaches a **pip distance** to "out of the box" for the first time, making the referent more consequential. |
| **A-007** — "second leg" | `[00:34:57]` "I'm only going to take second leg trades"; `[00:35:22]` "**And I'm going to define what a second leg is**"; `[00:35:25]` the "definition", which is "If you see this, that's not a trade. This is not a trade. That's a trade." | **Impact raised from High to Foundational.** V02 is materially worse than V01 here: the definition is promised and then given only by gesture. Three V02 instructions depend on it. |
| **A-010** — "peak formation high/low" | `[00:07:07]`, `[00:18:06]`, `[00:15:46]` "they will not go below last week's peak formation" | Adds a new load-bearing claim built on the undefined object. Still no definition. Still not distinguished from the anchor point. |
| **A-014** — "fractional disparity" | `[00:43:26]` "He handled the crosses fractional disparity" | **Second occurrence**, first outside a survey. Now clearly a live term in the instructor's vocabulary rather than a one-off. Still unexplained. |

---

## A-026 — `HOW` (printed beside `LOW`)

### Course Meaning

Unknown. Printed on the Weekly Structure slide as one of the two things the dealer moves
away from after trapping traders.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V02 | slide `[00:08:55]` | "Market Makers' Trap Traders On The First Day Of The Trading Week And Tie Up Your Margin For The Remaining Days By Aggressively Moving Away From The **LOW or HOW**." Screenshot: `04_SCREENSHOTS/V02/V02_00-08-55_weekly-structure-text-slide.png` |

### Assessment

Read beside `LOW` in the same phrase, "High Of Week" is the natural expansion, and the
symmetry of the sentence (the dealer moves away from whichever extreme he set) supports
it. **The slide does not expand it and the audio never says it.** V01's quarantined
`RULES.md` used "HOD/LOD" (high/low of *day*), which is a different unit — and that file
is fabricated, so it is not evidence either way.

Not adopted. The cost of guessing wrong is that every weekly-level reference points at a
daily extreme, or vice versa.

> **RESOLVED 2026-08-10 (V03 pass).** The assessment above is superseded by direct
> evidence and is retained so the change is visible. V03 `[00:26:40]` spells the
> abbreviation out in speech — *"**H-O-W high of the week**"* — immediately after
> *"Lock off the first eight hours"* `[00:26:38]`, and pairs it at `[00:26:55]` with
> *"Low of the week"*. This is an expansion stated by the instructor, not the
> symmetry inference this record declined to adopt.
>
> The week-vs-day question the record was opened over is settled: **both extremes are
> weekly**. V01's quarantined `RULES.md` reading of "HOD/LOD" (high/low of *day*) is
> now positively contradicted rather than merely unsupported — one more independent
> confirmation that the fabricated files invent detail.

### Current Status

```text
RESOLVED — HOW = High Of the Week; LOW (beside it) = Low Of the Week.
Source: V03 [00:26:40], [00:26:55] (spoken expansion).
Codable as a label. It does NOT follow that the *levels* are codable — how the
high and low of the week are determined in real time is A-010/A-033 territory and
remains DO NOT CODE.
```

### Required Research

None outstanding. (Formerly: a later slide or lesson that expands the abbreviation, or
uses `HOW` in a sentence that fixes the period. V03 `[00:26:40]` is that sentence.)

---

## A-027 — "Swing Traders Book- Day Traders Book"

### Course Meaning

Unknown. Printed text on the Weekly Market Structure chart, positioned over the Level 3
exit region.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V02 | slide `[00:18:00]` | Printed above the final rise, beside "Level 3 Exit and Reverse". Screenshot: `04_SCREENSHOTS/V02/V02_00-18-00_weekly-market-structure-levels-chart.png` |

The instructor does **not** read this label aloud at any point in the lesson.

### Why it is recorded rather than interpreted

"Book" in trading usually means "book profit". The label's placement at the exit region,
naming two trader types, reads naturally as *this is where swing traders take profit and
this is where day traders take profit* — i.e. a target rule differentiated by holding
style. That would connect neatly to `[00:30:32]`, where he offers swing traders an
ADR × 1.5 / × 2 hold.

**It is not adopted, and the neatness is the reason to be suspicious.** Nothing states
it. This is structurally the same trap as A-018: a suggestive label on a chart, which if
read as a rule inserts a target the lesson never states. The connection to the swing
option is exactly the kind of tidy inference that produced the quarantined files.

### Current Status

```text
DO NOT CODE
```

### Required Research

A lesson where he reads this label aloud or draws the two exits separately.

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-018 (`R =` labels — same failure mode), A-004 (levels) |
| Interpretation | `03_LESSON_NOTES/V02_INTERPRETATION.md` §10.4 X2 |

---

## A-028 — `V-3`

### Course Meaning

Unknown. Printed beside `PFL` at the week's low on the Weekly Market Structure chart.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V02 | slide `[00:18:00]` | `V-3` printed immediately left of and above `PFL`, at the bottom of the false-move leg. Screenshot: `04_SCREENSHOTS/V02/V02_00-18-00_weekly-market-structure-levels-chart.png` |

### Candidate readings, none adopted

| # | Reading | Note |
|---|---|---|
| 1 | A "V" formation with a 3-something (three touches? three candles?) | The course uses shape letters (M, W, V) — `[00:19:52]` "the real trade obviously is V-patterns of the low or W to the low" — so "V" as a shape is well supported. The "-3" is not. |
| 2 | A level count running backwards from the low | Would conflict with Level 1/2/3 running forward from it on the same chart. |

Reading 1 is the more likely and is still a guess.

### Current Status

```text
DO NOT CODE
```

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-010 (peak formation), A-011 (M and W formation), A-004 (levels) |

---

## V02 VISUAL EVIDENCE ADDED TO EXISTING RECORDS

The 25 screenshots captured on 2026-08-10 bear on six earlier records. Kept together so
the visual pass is auditable as a unit.

| ID | Visual evidence | Effect |
|---|---|---|
| **A-004** — "level" | Slide `[00:18:00]` prints `Level 1`, `Level 2`, `Level 3` as consecutive legs across day columns, each opened by a "Stop Hunt Low-Rise", terminating at "Level 3 Exit and Reverse" | **Materially constrained.** A level is an ordinal leg in a sequence, not a price line. Still no rule for when one level ends and the next begins, so it stays `DO NOT CODE`. |
| **A-007** — "second leg" | Slide `[00:33:10]` prints "If Second Leg Presents, Restart The Clock" | **No progress, and the gap is now worse.** The term is load-bearing in *print* as well as in speech, and defined in neither. Remains Foundational. |
| **A-018** — `R =` labels | Slide `[00:18:00]` carries eight `R =` values on one chart: `15.0`, `~25`, `29.6`, `53.8`, `61.4`, `70.7`, `86.7`, `100.6` | **More samples, same status.** The values scale with the visible height of each rectangle, which strengthens candidate 1 (range of the boxed area in pips) and further weakens the risk-to-reward reading — V02 states no stop and no target either. Still `DO NOT CODE`. |
| **A-019** — session times | Slide `[00:45:55]` prints the full table: 5pm high/low reset, 5pm–8pm dead gap, Asian 8:30pm–3:00am (gap 3–3:30a), London 3:30am–9:00am (gap 9–9:30a), New York 9:30–5pm. Slide `[00:47:20]` adds "Time Ribbon … (Server Times)" and "All Other Time References Are GARBAGE" | **Materially constrained.** Everything except the timezone is now recovered. New York time is strongly indicated (V01 `[00:46:09]` "930 New York Eastern"; V02's "6:30 New York time") but **is not printed**, so the record stays open rather than closing on inference. |
| **A-023** — "33 trade" | `33-Trade` printed on the **Level 3** move of slide `[00:18:00]` | **Constrained.** Ties "33" to level 3 rather than calendar day 3, correcting the natural reading of the audio's "day three". Digits still undecoded. |
| **A-020** — "mayonnaise" | Charts show three coloured moving averages (white, cyan, red/yellow). **No legend, no period label on any captured frame** | **Not resolved.** The hoped-for resolution route in A-020's "Required Research" has been tried and failed for V02. |

---

## A-029 — `wt = <number>` labels attached to shaded boxes

### Course Meaning

Unknown. Printed inside pale-blue rectangles on the intraday charts shown during the
mail segment. Never spoken, never explained, and never referred to.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V03 | slide `[00:09:49]` | Three boxes on a 19–20 Mar intraday chart labelled `wt = 24.8`, `wt = 116.1`, `wt = 18.5`, alongside stepped blue `DayHi` / `DayLo` lines. Screenshot: `04_SCREENSHOTS/V03/V03_00-09-49_annotated-chart-blue-boxes-wt-values.png` |

### Candidate readings, none adopted

| # | Reading | Note |
|---|---|---|
| 1 | The same quantity as `R =` (A-018) under a different label — the height of the boxed area in pips | The magnitudes (18.5 – 116.1) sit in the same range as the `R =` values on the same instructor's charts, and the label sits inside a box the same way. Strongest reading. |
| 2 | "weight" — a scoring or sizing figure | No course support whatever; recorded only because the letters suggest it. |
| 3 | A time quantity ("wait time") | The values do not scale with the visible width of the boxes, which argues against it. |

### Current Status

```text
DO NOT CODE
```

### Required Research

A frame where `wt =` and `R =` appear on the same chart, which would settle whether they
are the same measure. None exists in V01–V03.

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-018 (`R =` labels) |
| Source | `03_LESSON_NOTES/V03_SOURCE_NOTES.md` §4h |

---

## A-030 — "brinks shadow" / "shadow box"

### Course Meaning

Unknown. Used as an established object — a region price is inside of — in both speech and
print, with no definition anywhere in V01–V03.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V03 | slide `[00:44:19]` | Printed entry criterion: **"In brinks shadow"**. Screenshot: `04_SCREENSHOTS/V03/V03_00-44-19_flash-card-sample-entry-criteria-text.png` |
| V03 | `[01:03:21]` | *"if you're sitting in front of your screen at 3 30 in the morning inside the shadow box"* |

### Assessment

The printed form settles the ASR's "in the brink shadow" as **"In brinks shadow"**, and
pairs it with the spoken "shadow box" as apparently the same idea. What the shadow is
cast *by* is never stated. The `[01:03:21]` usage attaches it to a clock time, which
suggests a session-based window rather than a price structure — but "in" a box is spatial
language, and the criteria slide lists it among structural conditions, not timing ones.
Both readings cannot be right and the lesson does not choose.

### Current Status

```text
DO NOT CODE
```

### Required Research

A chart frame where the instructor draws or names the shadow box, or any sentence giving
its boundaries.

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-019 (session times), A-006 (the blue/red box) |
| Source | `03_LESSON_NOTES/V03_SOURCE_NOTES.md` §3, §4d |

---

## A-031 — "blood in the water" / "bloodline"

### Course Meaning

Unknown. Used as a named, recognisable chart condition and listed as an entry criterion.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V03 | slide `[00:44:19]` | Printed entry criterion: **"Blood in the water"**, listed immediately after "Shark fin" |
| V03 | transcript preamble | *"there's a shark fin, it crosses back in, hits the bloodline"* — recorded in the transcript's own terminology note |

### Assessment

The adjacency to "Shark fin" and the phrase "hits the bloodline" indicate both belong to
the **TDI subgraph** vocabulary rather than to price. The instructor explicitly defers TDI
coverage at `[01:01:53]` (*"I'm going to cover TDI later"*), so the terms are used before
the indicator they apparently describe has been taught. Which line of the TDI is the
"bloodline" is not stated.

### Current Status

```text
DO NOT CODE
```

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-032 (shark fin), A-020 (mayonnaise) |

---

## A-032 — "shark fin"

### Course Meaning

Unknown. A named shape, listed as an entry criterion and used as if long established.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V03 | slide `[00:44:19]` | Printed entry criterion: **"Shark fin"** |
| V03 | transcript preamble | *"there's a shark fin, it crosses back in, hits the bloodline"* — "crosses back in" implies a line crossing a band |

### Assessment

"Crosses back in" is band language, which points at the TDI rather than at a candle
pattern. Whether the fin is the shape of the TDI line excursion or of price is not stated.
As with A-031, the term is in use before TDI is taught.

### Current Status

```text
DO NOT CODE
```

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-031 (blood in the water), A-011 (M and W formation) |

---

## A-033 — "outside structure"

### Course Meaning

Unknown. Printed as an entry criterion and spoken repeatedly as a condition on where price
has travelled, with no definition of what the "structure" is or where its boundary lies.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V03 | slide `[00:44:19]` | Printed entry criterion: **"Outside structure"** |
| V03 | `[00:16:40]`–`[00:17:12]` | Worked example narrated as "outside structure to the high" |

### Assessment

The most likely referent is the first-eight-hours block (§2a) — price outside the week's
accumulation high/low. That reading is coherent and is **not stated**. It matters because
"outside structure" is one of the two conditions in the swing-exit gesture the
interpretation file parks as a machine candidate; coding it against the wrong boundary
would change every exit.

### Current Status

```text
DO NOT CODE
```

### Required Research

A frame where he marks the structure boundary while saying the phrase.

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-004 (level), A-010 (peak formation) |
| Interpretation | `03_LESSON_NOTES/V03_INTERPRETATION.md` §7 |

---

## A-034 — "safety trade"

### Course Meaning

Unknown. Named as a trade type with an approximate distance attached, but no entry rule.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V03 | `[00:57:14]`–`[00:57:15]` | *"Slightly below the tracer, right? The dealer makes the stop slightly below the tracer and rises."* |
| V03 | `[00:57:30]` | *"comes back. 50 to 75 pips off of the level"* |

### Assessment

This is the closest V03 comes to a complete entry: a location (slightly below the tracer),
a magnitude (50–75 pips off the level) and a name. It still lacks a trigger, a stop, and a
target, and "slightly below" is the same unquantified tolerance already recorded as A-024.

### Current Status

```text
DO NOT CODE
```

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-024 ("slightly above"), A-008 (the tracer) |

---

## A-035 — "vectors" (as a counted quantity)

### Course Meaning

Unknown. Counted on the sample card and listed on the notation checklist, so it is a
quantity the student is expected to measure — but the course never says what one is.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V03 | slide `[00:41:54]` | **"Vectors"** is item 3 of the eight-item flashcard notation checklist |
| V03 | slide `[00:44:19]` | **"3 vectors passed mayo"** — counted, and related to the "mayo" average |
| V03 | `[00:42:33]` | Spoken in the same list: *"Time, position of the indicator, vectors, Asian range, distance out of Asia"* |

### Assessment

Being *countable* and *passing* something makes a vector most likely a directional price
leg or an impulse candle group. Neither is stated. This is the most dangerous kind of
ambiguity in the register: the course asks the student to record a number, which makes it
look like objective data, while leaving the counting rule entirely to judgement.

### Current Status

```text
DO NOT CODE
```

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-020 (mayonnaise — what is passed), A-007 (second leg) |

---

## A-036 — "quarter of wood" / `COW` (the dealer "lays on" the level)

### Course Meaning

**Partially defined by V03** — the only new term in this lesson the instructor actually
explains — but the operative criterion is qualitative.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V03 | `[01:00:02]`–`[01:00:16]` | *"when the dealer just lays on the low or lays on the high. And he forms like what looks like a quarter of wood, just all sideways logs… the dealer would hit the level and just lay there"* |
| V03 | slide `[00:54:39]` | A personal flashcard labelled **"COW on LOD"**. Screenshot: `04_SCREENSHOTS/V03/V03_00-54-39_cow-on-lod-flashcard.png` |

### Assessment

The concept is clear enough to recognise by eye — sideways consolidation sitting directly
on a high or low — and the screenshot confirms the visual. What is missing is every number
that would make it codable: how many bars constitute "laying there", how tight the range
must be, and how close to the level counts as "on" it. `COW` is also never expanded on the
recording; "quarter of wood" is the audio and `COW` is the card label, and the transcript
garbles it once as *"Court of words are the low of the day"* `[00:54:39]`.

### Current Status

```text
DO NOT CODE
```

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-016 ("goes into chop"), A-004 (level) |

---

## V03 EVIDENCE ADDED TO EXISTING RECORDS

V03's transcript and its 24 screenshots bear on seven earlier records. One record
**resolves**. Kept together so the V03 pass is auditable as a unit.

| ID | V03 evidence | Effect |
|---|---|---|
| **A-026** — `HOW` | `[00:26:40]` spells the abbreviation out in speech: *"**H-O-W high of the week**"*, followed at `[00:26:55]` by *"Low of the week"* | **RESOLVED.** `HOW` = High Of the Week, and `LOW` beside it = Low Of the Week. This is a spoken expansion of the abbreviation, not an inference from symmetry, and it settles the week-vs-day question the record was opened over — the fabricated `RULES.md` reading of "HOD/LOD" (high/low of *day*) is now positively contradicted, not merely unsupported. Status changes from `DO NOT CODE` to `RESOLVED`. |
| **A-008** — "the tracer" | `[00:14:06]` *"You count the first two bars a[s] the tracer"*, on the four-hour chart; `[00:57:15]` *"The dealer makes the stop slightly below the tracer and rises"*; `[01:08:16]` *"it just hits the tracer on the left"* | **Materially constrained; still not defined.** The tracer is now attached to a concrete object — the first two 4h bars of the week, i.e. the same eight-hour accumulation block as §2a — which is consistent with V01's "these two lines… Sunday Monday" if V01's two lines demarcate that same week-open window. It also behaves as a *price* reference, since stops sit "slightly below" it. Still unstated: whether the tracer is the bars, their high, their low, or the band between, which is exactly what a stop rule would need. Stays `DO NOT CODE`. |
| **A-018** — `R =` labels | Student's AJ chart `[00:28:44]` carries fifteen `R =` labels on day-boxes (43.9, 62.3, 58.2, 34.4, 53.2, 33.7, 60.8, 47.2, 46.2, 46.6, 103.1, 98.0, 117.3, plus `80.x` and `47.0` partly occluded); the sample card `[00:43:09]` labels the Asian-range box `R = 41.4` while the criteria text beside it reads **"Asian Range =41"** | **Strongly constrained, still not closed.** The `R = 41.4` / "Asian Range =41" pairing on one chart is the first direct evidence tying `R =` to *the range of the boxed area in pips*, and the day-box magnitudes match daily ranges. The risk-to-reward reading is now very hard to sustain. It stays `DO NOT CODE` only because the equivalence is never stated in words and the rounding (41.4 → 41) is unexplained. |
| **A-020** — "mayonnaise" | Criteria slide `[00:44:19]` prints **"3 vectors passed mayo"**; charts still show unlabelled coloured averages | **Spelling resolved, referent not.** The printed **"mayo"** settles that the ASR's "manays / mannees / minis" is one word the instructor spells this way, which retires the transcription question. The A-020 "Required Research" route — a legend or period label — fails again: no captured V03 frame labels any average. §14 item 12 records that one card is described as *"past the 200 in the shadow"* where another says *"passed mayo"*, which would make mayo the 200-period average; **this is not stated and is not adopted.** Stays `DO NOT CODE`. |
| **A-024** — "slightly above/below" | `[00:57:14]` *"Slightly below the tracer"* as the safety-trade location | **No progress; scope widened.** The same unquantified tolerance now governs a second, differently-named trade, so the record is load-bearing in more places than when it was opened. |
| **A-005** — "the trading zone" | Printed on the V03 agenda slide `[00:12:09]` ("R & D / Weekly Cycle / Flash Cards / **Trading Zone**"); the recording ends after Q&A without reaching it | **Deferred a third time (V01 → V02 → V03).** The term is now on a printed agenda as a scheduled topic, which confirms it is a real course concept rather than a passing phrase, and confirms it has still never been taught. |
| **A-019** — session times | No session-times slide appears anywhere in V03 (see `CONTRADICTIONS.md` C-004). Spoken only: `[00:55:05]` *"right before the US session at 9.30"*, `[01:03:21]` *"3 30 in the morning inside the shadow box"* — neither carries a timezone | **No progress.** Two more untimezoned references added to the pile. |

---

## A-037 — halving the Asian range ("27 divided by 2 … you have a 13.5 trading range")

### Course Meaning

Unknown whether this is a **method** or a **remark about one chart**. On the V04 flashcard
chart the instructor measures the Asian range as 27 pips, then argues the tradeable range
is half of it.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V04 | `[00:11:27]`–`[00:11:31]` | *"It actually is less than 27 pips. Here's why."* |
| V04 | `[00:11:33]`–`[00:11:44]` | *"The dealer, mid-Asia, snatches the low away from traders that were in this range right here… He shifts it higher, right? Then he holds the level."* |
| V04 | `[00:11:48]` | *"This is an Essenture Consolidation Zone, which 27 divided by 2, 28 is 14, so 13 and a half."* (ASR: *"Essenture"* = "in essence, the") |
| V04 | `[00:11:56]` | *"In Essenture, you have a 13.5 trading range."* |
| V04 | `[00:12:11]` | *"Your Asian range is technically 13 pips."* |
| V04 | `[00:12:03]` | *"No Joe, there are two boxes I'll talk about it"* — **and he never does** |

### Why it matters

This is not cosmetic. V04's only entry condition (a) is *"25 to 50 pips above and below
the blue box"* `[00:15:43]`. **If the box's effective edge moves, the 25–50 pip
measurement moves with it.** A 13.5-pip box and a 27-pip box place the qualifying zone in
two different places on the same chart.

### The two readings

| # | Reading | Support | Against |
|---|---|---|---|
| 1 | **A general method** — the tradeable Asian range is the post-shift consolidation zone, roughly half the full overnight range | The arithmetic is presented as a derivation (*"Here's why"*), and he restates the result twice in different words | Applied to exactly one chart; the divisor 2 is never justified; "mid-Asia snatches the low" is a description of *this* night, not a rule |
| 2 | **A remark about this chart** — on this night the dealer shifted the low mid-session, so the range that actually held is the later, narrower one | The whole passage is inside a flashcard walkthrough of one example | He generalises freely elsewhere in the same segment |

**Neither is adopted.** The "two boxes" remark at `[00:12:03]` is the strongest hint that
there is a real distinction here with a name, and it is exactly the part he skips.

### Possible Measurable Features

| # | Candidate | Course support |
|---|---|---|
| 1 | `tradeable_range = full_asian_range / 2` | **NONE beyond one worked example.** The divisor is stated once, about one chart |
| 2 | The consolidation zone bounded by the *post-shift* low and the range high | PARTIAL — this is what he describes, but neither boundary is defined |

```text
Classification:          INFERRED MACHINE CANDIDATE
Canonical Course Status: NOT A COURSE RULE
```

### Current Status

```text
DO NOT CODE
```

### Required Research

A later lesson that either (a) explains "the two boxes", or (b) applies the halving to a
second chart. One instance is an anecdote.

### Impact If Wrong

Adopting reading 1 as a rule would silently relocate the reference edge for V04's only
stated entry condition on every chart in the corpus. Rejecting it if it *is* the method
would put the qualifying zone 13 pips too far out.

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-004 (the level), A-018 (`R =` labels), A-006 (the boxes) |
| Interpretation | `03_LESSON_NOTES/V04_INTERPRETATION.md` Q4, Q5, §9.4 |

---

## A-038 — the ADR lookback window (GUEST presenter)

### Course Meaning

The guest presenter gates every entry on the day's range being ~90–95% of "the ADR", and
never states over how many days the average is taken, or whose ADR it is.

> **Speaker note.** This record is `GUEST`, not instructor. It is logged because the
> guest's ADR gate is the single most-repeated numeric filter anywhere in V04, and a
> future session mining the lesson for rules will meet it six times.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V04 | `[00:36:43]`–`[00:37:01]` | *"Was the ADR met? … if it normally runs 110 pips and it's sitting at 80 but you're getting a signal, am I going to take that trade? Normally I do not"* |
| V04 | `[01:05:36]`–`[01:06:09]` | *"Basically, what I'm doing is measuring off the ADR… if it's behavior for the two previous days, and it's basically ran the same ADR, 110 pips, 80 pips, 120 pips, whatever it is, the two previous days, when it gets down to around 115 pips… that's how I know it by measuring the ADR"* |
| V04 | `[01:07:01]`–`[01:07:22]` | *"There's two ways. For one… I've been looking at these same pairs for nearly three years now. At first, I basically have kept a tab, but a lot of these indicators they'll tell you… previous day it ran… current day it ran"* |
| V04 | `[01:13:34]`–`[01:13:50]` | *"if the pair generally every day runs 100 pips, if it's not in the mid 90s, it's not ready"* |
| V04 | `[01:17:17]`–`[01:17:25]` | *"if this pair runs 100 pips on average ADR, and it's at 94[,] 95 right now"* |
| V04 | `[01:21:30]`–`[01:21:46]` | ADR **exceeded** ⇒ *"generally I pass on it… It simply isn't behaving itself"* |
| V04 | frame `00:40:40` | Printed on the per-pair form: **`ADR`** |
| V04 | frame `01:08:40` | The platform panel prints **`TDR / YDR / WADR / MADR / %DADR`** — see `A-040` |

### The two incompatible bases in one lesson

At `[01:05:36]` the reference is explicitly **the two previous days**. At `[01:13:34]` and
`[01:17:17]` it is *"generally every day runs"* — an unbounded average. At `[01:07:01]` it
is whatever the indicator reports, which (per `A-040`) offers weekly and monthly variants
as well. **These are three different numbers on the same chart.**

### Possible Measurable Features

| # | Candidate | Course support |
|---|---|---|
| 1 | Mean true daily range over the **2** previous days | Stated once, `[01:05:36]` |
| 2 | Mean over an unstated longer window | Implied by *"generally every day runs"* |
| 3 | Whatever `%DADR` on his template reports | `A-040`; the template's own definition is not visible |

```text
Classification:          INFERRED MACHINE CANDIDATE
Canonical Course Status: NOT A COURSE RULE  (and NOT an instructor rule at all)
```

### Current Status

```text
DO NOT CODE
```

### Required Research

An instructor lesson that defines ADR, or a frame where the indicator's settings dialog is
open. The `01:08:40` frame prints values but not periods.

### Impact If Wrong

A 2-day and a 20-day ADR differ by tens of pips on a volatile pair. The gate is *whether today is at 90–95% of it*, so the window choice decides whether a
setup is taken at all.

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-040 (the printed ADR family) |
| Contradiction | C-005 (guest vs instructor) |
| Interpretation | `03_LESSON_NOTES/V04_INTERPRETATION.md` I9, M6 |

---

## A-039 — TDI is a *required* entry criterion that the course has never taught

### Course Meaning

TDI confirmation is condition (c) of the only complete entry rule the course has stated,
and TDI has been explicitly deferred to a future lesson twice.

> **This record is not about a word's meaning.** It is about a **structural gap**: V04
> states a rule that V04 does not equip a student to apply. It is filed here because it
> blocks the same thing the other records block — application.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V04 | `[00:15:49]`–`[00:15:55]` | Condition (c), verbatim: *"TDI confirms blood in the water shark fin outside the band to back in"* |
| V04 | `[00:13:43]`–`[00:13:51]` | *"Any else agrees TDI is overextended and forms an M or some type of divergence… It'll be outside the volatility ban. You'll have blood in the water on the secondary line"* |
| V04 | `[00:13:53]` | *"I can't show you TDI because it's not here"* — **the instructor's own example chart carries no TDI panel** (frames 3–12, Segment A) |
| V04 | `[00:22:11]` | *"I'm going to do the TDI next week"* |
| V03 | `[01:01:53]` | *"I am going to cover TDI later, but just so you know what I'm talking about"* |
| V04 | frame `01:04:10` (`V04_01-04-10_gbpjpy-m15-platform-window.png`) | **DISPLAYED, NOT TAUGHT — `GUEST`, DESCRIPTIVE ONLY.** A sub-panel titled **`Traders Dynamic Index Visual`** is rendered across the lower third of the guest presenter's platform, with its coloured lines and volatility bands drawn |
| V04 | frame `01:08:40` (`V04_01-08-40_audcad-m15-r-labels-adr-panel.png`) | **DISPLAYED, NOT TAUGHT — `GUEST`, DESCRIPTIVE ONLY.** Same panel, same title, on the AUDCAD,M15 chart |

> **The two frames above were added 2026-08-11 per V04 review R1 finding `M6` (`E20`), and
> they do NOT narrow this record.** They are `GUEST` material and therefore **descriptive
> only** under the `C-005` ruling (`D-025`): guest evidence may **extend** an `A-xxx`
> record and may **never close** one. A rendered indicator is not a taught indicator — no
> inputs, periods, band construction, geometry or decision rule is recoverable from either
> frame, and the numeric readout beside each panel title is illegible at this resolution
> and is not transcribed. What they establish is **terminology only**: `TDI` denotes the
> **Traders Dynamic Index**, an expansion no line of audio in V01–V04 states. The
> structural gap this record exists for is unchanged, and so is the prohibition below.

### Why this is worse than an ordinary undefined term

The other TDI-family records (`A-031` blood in the water, `A-032` shark fin) ask *what does
this phrase mean*. This record notes that **all three of them sit inside a stated
necessary condition**, and that the presenter who states the condition cannot display the
indicator on his own chart. *(It is rendered later in the lesson on the **guest's**
platform — frames 21 and 22 — which is descriptive evidence about the term and teaches
nothing about the condition.)* The result is that V04's criteria list — the most complete entry
statement in the course — cannot be executed or graded from V04 alone.

This is the direct reason `V04_MASTERY_REPORT.md` records dimension G as `DEFERRED` rather
than attempting a backtest: grading rule *application* against a condition that must be
partly invented is `E18` (invalid manual-backtest procedure).

### Current Status

```text
DO NOT CODE — and DO NOT SUBSTITUTE.
```

Specifically: **no session may drop condition (c) in order to make the rule testable.** A
two-condition version of V04's rule is a different rule with a different hit rate, and
testing it while calling it the course's rule is the `E06`/`E18` failure.

### Required Research

The promised TDI lesson. V05 (`Bootcamp1 Wk2 032512 Part3`) is the next candidate; the
instructor says *"next week"*, which would be V06 or later by session date.

### Impact If Wrong

Treating the rule as complete without TDI would produce a backtest of a rule the
instructor did not state, whose results would then be attributed to him.

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-031 (blood in the water), A-032 (shark fin), A-005 (trading zone — also deferred repeatedly) |
| Interpretation | `03_LESSON_NOTES/V04_INTERPRETATION.md` §1, §4, §9.6 |

---

## A-040 — the printed ADR family: `TDR / YDR / WADR / MADR / %DADR`

### Course Meaning

Unknown. A block of range statistics printed by the guest presenter's chart template,
never read aloud and never explained.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V04 | frame `01:08:40` (`V04_01-08-40_audcad-m15-r-labels-adr-panel.png`) | Top-right panel prints, with values: `HOD 1.0339 / 17`, `LOD 1.0285 / 37`, `TDR 55`, `YDR 91`, `WADR 101`, `MADR 111`, `%DADR 100` |
| V04 | frame `01:08:40` | The chart legend separately prints `Previous Days Range: 118.3` and `Current Days Range: 12.9` |
| V04 | `[01:07:07]`–`[01:07:22]` | *"a lot of these indicators they'll tell you… previous day it ran[,] it tells you right there, current day it ran, she tells you right there"* — he points at this panel without naming its fields |

### The obvious expansions, and why they are not adopted

`TDR` = today's daily range, `YDR` = yesterday's, `WADR` = weekly average daily range,
`MADR` = monthly average daily range, `%DADR` = percent of average daily range completed.
These are **conventional readings of the abbreviations, not course statements.** The
numbers are broadly consistent with them (55 < 91 < 101 < 111 is a plausible
today/yesterday/weekly/monthly ladder), which is suggestive and is not evidence.

**It matters because `A-038` turns on exactly this.** If `WADR` and `MADR` are the
available averages, then the guest's *"generally every day runs 100 pips"* is probably one
of them, and his *"two previous days"* is not any of them.

### Current Status

```text
DO NOT CODE
```

### Required Research

A frame with the indicator's settings dialog open, or a lesson where a presenter reads the
fields aloud.

### Impact If Wrong

Guessing the expansions would fix `A-038`'s window by assumption rather than by evidence —
resolving one open record with another record's guess.

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-038 (ADR lookback), A-018 (`R =` labels — also printed, also unexplained) |
| Interpretation | `03_LESSON_NOTES/V04_INTERPRETATION.md` M6 |

---

## A-041 — `[00:22:49]` the forum/mail instruction is internally inconsistent

### Course Meaning

A single homework-administration line that, as transcribed, contradicts the same speaker
four minutes later.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V04 | `[00:22:46]`–`[00:22:49]` | *"We're going to go at Thursday night as the homework again, but don't mail it to me. I don't need it posted in the forum."* |
| V04 | `[00:26:27]`–`[00:26:40]` | *"I'm going to go post the homework assignment in the forum under my boot camp thread. And then I want you to go ahead work your charts and post them in there."* |
| V04 | `[00:26:41]`–`[00:26:48]` | *"I'll post my answer key… I'll post the answer key in my section. Compare your charts to that."* |

### Assessment

Almost certainly an **ASR-inserted negation** — the sentence without the negation would be
consistent with everything around it. **The repair is not made.** The audio was not
re-checked at this marker, and this project does not smooth garble inside quotation marks
(`E01`, charged against V02 R1).

**Nothing downstream depends on it.** The assignment's *content* is unaffected either way;
only the submission channel is in doubt, and no present-day session can submit to a 2012
forum regardless.

### Current Status

```text
DO NOT CODE — trivial; recorded for completeness and to prevent a future session
"fixing" the quotation silently.
```

### Required Research

A 10-second audio re-check at `[00:22:49]`. Cheap; simply not done here.

### Related

| Type | Reference |
|---|---|
| Source | `03_LESSON_NOTES/V04_SOURCE_NOTES.md` §8c |

---

## V04 EVIDENCE ADDED TO EXISTING RECORDS

V04's transcript and its 26 screenshots bear on nine earlier records. **None resolves.**
Kept together so the V04 pass is auditable as a unit.

| ID | V04 evidence | Effect |
|---|---|---|
| **A-010** — "peak formation high or low" | `[00:21:55]`–`[00:22:02]` *"if you see an AM on the four hour that's your anchor point, if you got an AM on the four hour charge that's your peak formation high"* (ASR: *"an AM"* = the letter M; *"charge"* = chart) | **Materially advanced; not resolved.** For the first time the course predicates *anchor point* and *peak formation high* of the same subject — an M formation on the four-hour chart — in two parallel clauses. This is the direct evidence `REVIEW_INDEX` open item 2 has been waiting for since V01 R1. It remains open because: the sentence is scoped to the four-hour chart and says nothing about other scales; it says nothing about the **low** side (peak formation low / W); and it is one Q&A utterance, not a slide or a repeated definition. **Symmetry to the low side is NOT assumed.** Stays `DO NOT CODE` — the identity names the object, it still does not say how to *locate* one. |
| **A-011** — "M and W formation" | The same passage; plus `[00:15:49]` *"M formation second leg, W formation second leg"* as a necessary entry condition; plus `[00:20:20]` *"On the 15 minute chart it'll make the M formation"* coordinated with a four-hour railroad track | **No definition added; load increased.** V04 makes the M/W the **second** condition of the only stated entry rule and equates it with the anchor point (`A-010`), so an undefined term is now load-bearing in two more places. V02 R1's finding — that M/W anatomy is undefined across the corpus — survives V04 intact. The guest's *"Gaby a nice ugly look in kindergarten ma'am there"* `[01:10:36]` (ASR: *"ma'am"* = M), *"It's like a pre-school M or maybe a kindergarten now"* `[01:12:09]` (ASR: *"now"* = M) and *"Maybe a preschool W right here"* `[00:44:04]` are evidence **against** any tight geometric definition: the course tolerates badly-formed instances and offers no boundary. |
| **A-018** — `R =` labels | Frame `00:04:40` prints **`R = 27.0`** on the Asian-range box; on that same chart the instructor says *"What's the Asian range?"* `[00:08:08]` / *"27 pips"* `[00:08:09]` and *"27 pips range"* `[00:11:25]`. Further labels on the guest's platform: `R = 33.2 / 58.4 / 15.5` (frame `01:04:10`), `R = 52.4 / 65.9 / 54.6` (frame `01:08:40`), `R = 95.2` (frame `01:12:00`) | **Second agreeing pair, and the first with a *spoken* side.** V03 supplied a printed-vs-printed pairing (`R = 41.4` beside *"Asian Range =41"*). V04 supplies printed-vs-spoken, on a different chart, in a different lesson, to **0.0 discrepancy**. The risk-to-reward reading is now very hard to sustain on a second ground as well: V04 *does* state a stop (10–18 pips) and a target (50), and `R = 27.0` is not an R-multiple of either. **Still not closed** — no presenter states the equivalence in words, and the guest's `R = 95.2` box has no spoken range to check it against. Stays `DO NOT CODE`. |
| **A-020** — "mayonnaise" | Frame `00:50:00` prints the chart caption **"Entered here after 4th retest Mayo"**; the surrounding speech `[00:49:46]`–`[00:49:51]` is *"you can see one, two, three, four times… It came up against the mail here"* | **Spelling corroborated a second time; referent still unknown.** V03 already settled the spelling from its criteria slide, so this is **not** a new resolution. What it adds: a **second, independent** printed instance, by a **different presenter**, on a **different platform**, in which "Mayo" is a **price level that price retests four times** — a stronger functional reading than V03's slide caption gave. The `A-020` "Required Research" route fails for a third lesson running: no captured V04 frame labels any average with a period. Stays `DO NOT CODE`. |
| **A-030** — "brinks shadow" / "shadow box" | `[00:12:53]`–`[00:13:01]` *"stop on Zone, Gray Box. Timing Shadow Box or the Brink Spox"*; `[00:13:40]` *"It's in the shadow, the Brink Shadow"*; `[00:10:53]` *"It hit the stop hunt shadow in the bricks"*; visually, grey and white vertical bands on the frames from `00:04:40` on | **Constrained, not defined.** V04 confirms the object is a **vertical, time-based band drawn on the chart** (the bands are visible and price passes through them), and that "shadow box", "brick(s)" and "grey box" are used for it interchangeably. Still unstated: which clock hours it spans, and whether "grey box" and "shadow box" are the same band or two. The guest is unhelpfully explicit that they do not matter to him — *"really all these boxes, the shadow boxes, all the stuff they really don't matter, guys… They just really do not matter"* `[00:44:38]`–`[00:44:43]` — which is a `GUEST` opinion and **not** an instructor retraction. |
| **A-031** — "blood in the water" / "bloodline" | `[00:15:49]` puts *"blood in the water"* inside the necessary entry condition; `[00:13:51]` *"You'll have blood in the water on the secondary line"*. **Separately**, the guest uses a bare *"the water"* 20 times as a **price destination**: *"my take profits are at the water, generally at the water"* `[00:46:19]`–`[00:46:24]`, *"it's usually three or four or five pips below the water in most cases"* `[00:46:27]`, *"I'm headed right back to the water"* `[01:19:53]` | **Widened, and a new ambiguity exposed inside it.** V03 established "blood in the water" as a **TDI** condition. The guest's *"the water"* is a **price level on the chart** he takes profit at. These cannot be the same object — a TDI oscillator line is not a price target. Either the course uses one word for two things, or one of the two usages is being misread. **Not resolved here**; recorded as `V04_INTERPRETATION.md` Q6. `[00:13:51]`'s *"on the secondary line"* is the best hint that the TDI sense names a specific plotted line. Stays `DO NOT CODE`. |
| **A-032** — "shark fin" | `[00:15:49]`–`[00:15:55]` *"shark fin outside the band to back in"* — the most explicit geometric statement of the shape so far; guest usages `[00:40:12]`, `[00:48:46]` *"Also got a shark fin here"* `[00:48:46]`, *"It was not out of the water, but it wasn't shark fin"* `[00:48:47]` (garbled) | **Geometry constrained for the first time.** *"Outside the band to back in"* gives the shape a **direction and a boundary condition**: the line must exit the band and re-enter it. That is more than V03's usage carried. Still unstated: which band (`A-031`'s "secondary line"? the volatility band?), how far outside, and over how many bars. Stays `DO NOT CODE`. |
| **A-033** — "outside structure" | `[00:21:04]`–`[00:21:16]` *"Outside structure is when the dealer creates a spike vector to the high and then trade off that level in here with these candles. Outside structure, high outside structure."* Immediately followed by `[00:21:17]` *"Let me see if I got a I'll pull a flash card up for you"* and `[00:21:20]` *"Leave that"* — **the promised card is never shown** | **First definition attempt; still not codable.** V04 is the first lesson to answer "what is outside structure" directly, and the answer names two components: a **spike vector to the high**, then **trading off that level**. That is genuine progress over V03, where the term appeared only as a printed criterion. It remains `DO NOT CODE` because the "structure" whose outside is meant is still never bounded — the definition describes the dealer's *behaviour*, not the chart *boundary* a machine would test. The withdrawn flashcard is a near miss worth noting: the visual that would have settled it was queued and abandoned on air. |
| **A-005** — "the trading zone" | `[00:26:15]`–`[00:26:23]` *"We're going to work on the trading zone. We're going to start talking about the 22, 33 trades, multi session M and W's"* | **Deferred a fourth time (V01 → V02 → V03 → V04).** Now promised as upcoming in two consecutive lessons. Also forward-points `A-023` (33 trade) and `A-024` (22 trade), which are likewise named-not-taught. |
| **A-019** — session times | `[00:21:33]`–`[00:21:37]` *"From one to five AM New York, one to four AM New York, four or five hours. Take a break from eight to 11 New York time"*; `[00:21:41]` *"nothing's changed"* | **First timezoned times in the corpus — and they are not session boundaries.** Unlike every prior reference, these carry an explicit zone ("New York"). But they define **when to be at the screen**, not when a session starts or ends, and the instructor immediately marks them as a restatement. **No session-boundary table exists anywhere in V04**, spoken or printed — checked against all 1,037 sweep frames. `A-019` is unaffected on its actual question. |
