# AUTOMATION AMBIGUITIES

Every subjective phrase in the course that would be dangerous to code prematurely.

Template: `00_SYSTEM/TEMPLATES/AMBIGUITY_TEMPLATE.md`

---

## STATUS

```text
RECORDS: 0
```

**Intentionally empty.** No course material has been studied, so no course
ambiguity has been observed. Records appear here only when an actual lesson uses an
actual subjective phrase.

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
| A-003 | "picks up the [?penings?]" | V01 `[00:39:12]` | DO NOT CODE | Unknown — the word itself is unrecovered. Sits at two steps of the core sequence. |
| A-004 | "level" (countable unit) | V01 `[00:35:38]` | DO NOT CODE | High. Used to bound expected move size ("one to three levels"). |
| A-005 | "the trading zone" | V01 `[00:30:40]` | DO NOT CODE | Foundational. The stated entry filter for struggling traders. Deferred to V02. |
| A-006 | "the blue box" / "the box" / "the red box" | V01 `[00:43:07]` | DO NOT CODE | High. Three box terms, no definition, one entry prohibition attached. |
| A-007 | "second leg" | V01 `[00:43:21]` | DO NOT CODE | High. The stated preferred entry timing. |
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
DO NOT CODE
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

**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The instructor was pointing at a slide while using this phrase, so the visual characteristics are precisely the part that was lost.

### Counter-examples

None. V01 shows no example where this was rejected or explicitly not applied. Counter-examples are what would bound this concept, and the lesson provides none.

### Possible Measurable Features

| # | Candidate measure | Rationale | Course support |
|---|---|---|---|
| 1 | A session range rectangle drawn on the chart, colour-coded by session | The red box appears in a US-session context and "inside the box" is used as a waiting condition | NONE |
| 2 | A price zone bounding valid entries, independent of session | `[00:43:56]` describes a trade being outside it, implying a positional not temporal boundary | NONE — and this reading conflicts with the one above |

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
