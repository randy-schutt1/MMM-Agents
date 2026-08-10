# AUTOMATION AMBIGUITIES

Every subjective phrase in the course that would be dangerous to code prematurely.

Template: `00_SYSTEM/TEMPLATES/AMBIGUITY_TEMPLATE.md`

---

## STATUS

```text
RECORDS:         18   (A-001 … A-018)
LESSONS STUDIED:  1   (V01)
RESOLVED:         1   (A-003 — "pendings", on visual evidence at [00:40:25])
DO NOT CODE:     17
```

> **UPDATED 2026-08-10 (review R1, finding 6b).** This block previously read
> `RECORDS: 0` and *"**Intentionally empty.** No course material has been studied, so no
> course ambiguity has been observed."* Both statements were true at project start and
> are now false — the file holds eighteen records. Corrected so the status does not
> contradict the file's own contents.

All eighteen arise from **V01 alone**, which names seventeen load-bearing terms and
defines none of them. `A-003` is the only one resolved, and it was resolved by text
printed on a slide rather than by anything spoken. The remaining seventeen are
`DO NOT CODE`.

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
| A-003 | "picks up the [?penings?]" → **"pendings"** | V01 `[00:39:12]` | **RESOLVED BY COURSE** | Unknown — the word itself is unrecovered. Sits at two steps of the core sequence. |
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
| V01 | `00:36:38` | "if the dealer anchors in early because he completed the pattern… in the previous week" |
| V01 | `00:51:22` | "When the dealer anchors in the middle of the week, you only are trading one direction till Friday away from the peak formation down short." |
| V01 | `00:51:38` | "I want you to try to identify the anchor point and take shorts off of stop [hunt] high drop" |

### Visual Characteristics

**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost.

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

**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost.

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

**The word itself has not been recovered.** It is transcribed as "penings" four times in identical construction, always as a thing the dealer collects at the same moment he "hits the stops". It is not an English word and no course meaning can be stated. Recording it as an ambiguity rather than guessing is the correct handling.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V01 | `00:39:12` | "the dealer comes out of the consolidation. It's the stops or picks up the penings, whatever happens to be there" |
| V01 | `00:39:43` | "The dealer then hits the stops, picks up the penings." |
| V01 | `00:40:46` | "Don't fall for the false move to pick up the penings and grab the breakout traders as a trade." |

### Visual Characteristics

**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost.

### Counter-examples

None. V01 shows no example where this was rejected or explicitly not applied. Counter-examples are what would bound this concept, and the lesson provides none.

### Possible Measurable Features

| # | Candidate measure | Rationale | Course support |
|---|---|---|---|
| 1 | (none proposed) | Proposing a measurable representation for a word that has not been read would be inventing the concept outright | NONE |

```text
Classification:          INFERRED MACHINE CANDIDATE
Canonical Course Status: NOT A COURSE RULE
```

### Current Status

```text
RESOLVED BY COURSE
```

### Required Research

Re-listening to the audio at `[00:39:12]` and `[00:39:43]`. This is the cheapest open question in V01 to resolve and it sits at two of the twelve steps of the core sequence.

### Impact If Wrong

Unknown, which is itself the problem. It is a named object in the mechanism the whole lesson describes. It may be trivial or it may be a core concept.

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

**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost.

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

**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost.

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

The boxes are **shaded rectangles with both a time extent and a price extent**. Pale blue covers flat, low-range consolidation; dark red covers the extended area where price is described as trapped. At `[00:48:35]` each rectangle carries a numeric label (`R = 70.5`, `R = 51…`, `= 43.1`) — see `A-018` — so they bound a measured region rather than being decorative shading.

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

A screenshot of `[00:43:53]` or `[00:45:55]`, or a later lesson that draws a box and names its colour. Note that the two candidate readings above are mutually exclusive, so this cannot be resolved by reasoning from the transcript.

### Impact If Wrong

High. An entry prohibition (`[00:43:07]`) and a wait condition (`[00:47:55]`) both reference "the box" with no stated referent. Binding them to the wrong object produces confidently wrong entry logic.

### Related

| Type | Reference |
|---|---|
| Ambiguity | A-005 |
| Contradiction | C-002 |
| Interpretation | `03_LESSON_NOTES/V01_INTERPRETATION.md` I2, Q3, Q4 |

---

### Visual Evidence Update — 2026-08-10 — one candidate reading ELIMINATED

The boxes are **shaded rectangles drawn over price areas on the chart**:

- **Pale blue** over flat consolidation ranges —
  `V01_00-40-25_beginning-of-session-chart.png` (over the low pre-session range),
  `V01_00-44-40_end-of-week-chart.png` (lower right), `V01_00-48-35_...png` (two of them).
- **Dark red** over the extended area where price has run and traders are described as
  trapped — same frames, plus `V01_00-38-50_beginning-of-week-chart.png`.

At `[00:48:35]` each rectangle carries a numeric label (`R = 70.5`, `R = 51…`, `= 43.1`),
so they are **measured regions**, not shading for emphasis. See A-018.

**This eliminates candidate 1** ("a session range rectangle drawn on the chart,
colour-coded by session"). The boxes do not align with session boundaries; they are
drawn around price structures. Candidate 2 — a price zone bounding valid entries — is
consistent with what is shown, but is not confirmed: nothing on the slides states that
the box governs entry eligibility.

Still unresolved: whether "the box" of `[00:43:07]` means the blue one, the red one, or
either; and how the rectangles are placed.

**Status unchanged: `DO NOT CODE`.**
## A-007 — "second leg"

### Course Meaning

The preferred entry timing. "The best way to grab setups is to wait for a second leg." What constitutes a leg, how a first leg is distinguished from a second, and on what timeframe, are not stated.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| V01 | `00:03:40` | "I'll show it off a[?] [f]ormation second leg and you'll tell me the trend's up" — garbled, but the term appears |
| V01 | `00:43:21` | "The best way to grab setups is to wait for a second leg." |

### Visual Characteristics

**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost.

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

**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost.

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

A screenshot of `[00:38:57]`. This term is unusual enough that it may be idiosyncratic to this instructor and may not recur; watch V02–V05.

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

**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost.

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

A screenshot of `[00:51:42]`–`[00:51:56]`. Ten seconds of video would resolve what fourteen seconds of audio cannot. Until then this is a name with no referent.

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

**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost.

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

**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost.

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

**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost.

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

**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost.

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

**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost.

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

**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost.

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

Later lessons showing what the dealer displays at each stage. The `[00:39:26]` moving-average reference is the only indicator-adjacent content in V01 and it warrants a screenshot before anything is built on it.

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

**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost.

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

A later lesson, or a labelled example. "Outside spike to the low" at `[00:44:41]` is more concrete than most of V01's language and may be recoverable from a screenshot.

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

**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost.

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

A screenshot of `[00:48:41]`, or later lessons using the phrase with more than one example. A single unlabelled instance cannot bound a size threshold.

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

### Current Status

```text
DO NOT CODE
```

### Required Research

A later slide or lesson that expands the abbreviation, or uses `HOW` in a sentence that
fixes the period.

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
