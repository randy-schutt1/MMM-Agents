# V10 — INTERPRETATION NOTES

> **NOTHING IN THIS FILE IS INSTRUCTION.** It is this session's reading of V10, kept separate from
> `V10_SOURCE_NOTES.md` so that a reviewer can tell at a glance which is which (`D-008`,
> `STUDY_PROTOCOL.md` §4). Every entry carries **evidence**, a **timestamp**, and a **confidence
> classification** from `EXPLICIT` / `VISUAL` / `IMPLIED` / `INFERRED` / `UNRESOLVED`.
>
> **No numeric constant is proposed here for anything the lesson left subjective** (`D-010`).
> Where a quantification is obvious and tempting, it is written down as
> `INFERRED MACHINE CANDIDATE / NOT A COURSE RULE` and goes no further.

**Lesson:** V10 · session 2012-04-01 · **course author, 100% of runtime**

---

## Q1 — Does V10 define `peak formation high` / `peak formation low`? **YES — and this is the lesson's largest contribution to the corpus.**

**Confidence: `EXPLICIT`.**

**Evidence.** `[01:13:58]`–`[01:14:06]`: *"We're identifying the peak formation high, or high of the
week, and the peak formation low, or low of the week — **which is the highest point on a chart
within the week, or the lowest point on the chart within the week**."*

Corroborated in print at frame `43:17` — *"PFH /PFL has formed as HOW or LOW (4hr Tie in)"* — where
`HOW`/`LOW` are the lesson's own abbreviations for high-of-week / low-of-week, spelled out aloud at
`[01:16:20]`.

**Why this matters more than its length suggests.** Across V01–V09 the corpus used `peak
formation` constantly and never said what one *is*. It was carried as an undefined named object.
V10 supplies a definition that is **purely positional and needs no pattern judgment at all**: the
extreme of the week. A weekly extreme is computable from OHLC with no shape recognition, no leg
counting, and no subjective threshold.

**Three limits, stated so the definition is not over-read:**

1. **It defines the *anchor*, not the *setup*.** The safety trade still needs `second leg`,
   `blue box`, `blue tracer` and the boundary of a `stop hunt` — **all still undefined**. The
   definition unblocks *where to measure from*, not *when to enter*.
2. **It is a retrospective definition used prospectively, and the lesson knows it.** The week's
   extreme is only certain when the week ends. The lesson's answer is the *lock* (Q3), which is a
   causal proxy, not the definition itself. **Conflating the two would be lookahead bias**, and it
   is the single biggest hazard V10 introduces.
3. **"Within the week" does not fix the week's boundaries.** V10 states no week open. The project
   has one only by vendor convention (`D-036a`: Sunday 17:00, UTC−5, fixed).

**Effect on records:** `A-010` **narrows on Tier 1 evidence alone** (`SOURCING_HIERARCHY.md` §3.2
case **A**). **Not blended** with any `MMM-NOTES` text. `A-004` (*the level*) is **untouched** —
see Q7.

---

## Q2 — What does the Friday claim jointly imply, and should that implication be tested?

**Confidence: `INFERRED` — the arithmetic is mine, not the lesson's.**

**Evidence.** `[00:13:41]`–`[00:13:52]`: *"the dealer will end **always** 25 to 50 pips off of the
high **and** 25 to 50 pips off of the low."*

**The implication the lesson does not state.** If Friday's close is simultaneously 25–50 pips below
the day's high and 25–50 pips above the day's low, then Friday's high-to-low range is
**arithmetically constrained to 50–100 pips**. That is a strong, falsifiable side-condition that
follows from the claim as spoken and is nowhere asserted by the speaker.

**How it is handled.** It is **tested as a derived measure, labelled as derived**, in `PT-036`
measure **M2b**, and its result is **reported separately from M2a** (the claim as stated). It is
**not** attributed to the instructor. A test that silently substituted the range constraint for the
distance claim would be testing my arithmetic and reporting it as his rule — `E06`/`E18`.

**A qualifier that must travel with it.** *"25 to 50 pips"* is pip-denominated and V10 teaches
across GBP/USD, AUD/USD, USD/CAD and GBP/JPY. A GBP/JPY pip is a different fraction of price than a
GBP/USD pip. The test runs on GBP/USD (`D-007`) and says so.

---

## Q3 — What is "the lock", and is it usable without lookahead?

**Confidence: `IMPLIED` for the mechanism; `UNRESOLVED` for its boundary.**

**Evidence.** `[00:44:47]`–`[00:45:00]` *"price will move away from this area which confirms the
formation … this is a lock, it's locked in"*; `[01:14:13]`–`[01:14:19]` *"we are simply waiting for
the dealer to pull away from there, and we are waiting for a visible stop hunt … to confirm what we
are seeing as a lock"*; `[01:05:31]`–`[01:05:38]` *"the dealer has now moved away from there for the
last 15 hours, 16 hours."*

**The reading.** The lock is the lesson's **causal, real-time substitute** for the retrospective
weekly extreme. You do not know the week's low; you know that price made a low, then moved away and
stayed away, and that is the tradeable claim.

**What is `UNRESOLVED`, and it is the load-bearing gap.** *How far* and *for how long* price must
move away is **never stated as a number**. `[01:05:35]` mentions *"15 hours, 16 hours"* as a
description of one chart, not as a threshold. **`D-010` and `D-030` both bite here**: any figure I
supplied would become the rule.

> `INFERRED MACHINE CANDIDATE / NOT A COURSE RULE` — a lock might be operationalised as *"the
> extreme is unbroken for N hours and price has travelled M pips from it."* **N and M are not in
> the lesson, in any lesson, or in `MMM-NOTES`.** Recorded so a later session can see the shape of
> the gap; **it must not be coded, and no V10 test uses it.**

**Consequence for testing.** The safety trade **cannot be backtested at V10** without inventing
either the lock threshold or the second-leg definition. This is recorded as a `D-030` block, not as
a testing failure — see the mastery report's dimension G.

---

## Q4 — Is the "600 to 1000 pips a week" claim plausible for GBP/USD, and what happens if it is not?

**Confidence: `EXPLICIT` for the claim; the assessment below is `INFERRED`.**

**Evidence.** `[00:14:09]`–`[00:14:17]`, `[00:14:38]`. Qualifiers at `[00:14:26]` (crosses run
higher) and `[00:14:43]` (*"unless he's shifting the zone"*).

**This session's prior, recorded BEFORE the measurement was taken and committed before the runner
was written.** A 600–1000 pip weekly range is **large** for GBP/USD in the 2013–2016 era, where
weekly ranges of 150–350 pips are typical. **I expect M1 to be CONTRADICTED, and by a wide margin.**

**Why the prediction is being written down rather than discovered.** `BACKTEST_EVIDENCE_STANDARD.md`
and `D-026`/`D-027` exist so that the direction of a result cannot be chosen after seeing it. This
prediction is committed in `PT-036` §5 **before** any bar is read, and it is scored honestly whether
right or wrong.

**What a contradiction would and would NOT mean:**

| It WOULD mean | It would NOT mean |
|---|---|
| The number as stated does not describe GBP/USD in the tested window | That the *method* fails — the weekly range is context, not a trade rule |
| A `C-xxx`-worthy divergence between a stated figure and the corpus's own primary instrument | That the speaker meant something else. **I do not get to reinterpret a number to save it** (`E01`, `E03`) |
| That any later spec quoting "600–1000" must carry the measurement beside it | That the figure should be adjusted to fit. `D-009` forbids exactly that |

**A reading I considered and REFUSED.** One could rescue the claim by measuring PFH-to-PFL across
**multiple** weeks — the cycle rather than the calendar week — since `peak formation` turns need not
occur weekly. **That is a different claim.** The speaker says *"a thousand pips **a week**"* at
`[00:14:38]` and the question he is answering says *"per week"* at `[00:14:02]`. **Re-scoping the
window until the number works is the `E09`/`D-009` failure**, and it is refused here in writing so a
later session can see it was considered and declined. `PT-036` §7 records it as a **pre-registered
secondary**, run and reported *in addition*, never *instead*.

---

## Q5 — Is "don't trade until they hit the stops" a rule or an exhortation?

**Confidence: `EXPLICIT` as a prohibition; `UNRESOLVED` as a machine condition.**

It is stated at least **seven** times, printed once (`23:03`), given a pre-trade checklist form
(`[00:25:09]` *"Did the dealer hit the stops before I pull the trigger?"*), and given a categorical
consequence (`[01:06:49]` *"Any other setup without a stop hunt is a shit gamble"*). **It is
unambiguously normative.**

**But it is not yet machine-readable, because `stop hunt` has no stated boundary.** V10 gets
*closer* than any prior lesson:

- `[01:26:13]` *"A true stop hunt is higher or lower than the blue box"* — a **necessary** condition
  under the strict variant;
- `[00:46:16]` *"preferably above or below the blue box"* — **preference**, not requirement;
- `[00:46:43]`–`[00:46:52]` *"The obvious ones are still valid if he doesn't come above or below the
  blue box … you're smarter than a box"* — which **explicitly re-opens** what the strict form closed.

**The three statements are consistent only if there are two grades of setup** — a strict one for
novices and a discretionary one for the experienced. **The lesson says exactly that**
(`[01:01:48]` *"those [of] you that are struggling — only take the ones where he breaks the Asian
range"*; `[01:26:06]` *"for novices"*). So this is **not** a contradiction; it is a stated
skill-tiering. **Recorded as such rather than filed as a `C-xxx`** — see `C-017` for the one place
V10 genuinely does conflict with itself.

**And the boundary is still missing at both tiers**: `blue box` is undefined, so even the strict
form is uncodable. `A-076`.

---

## Q6 — How many independent conditions does the safety trade actually have?

**Confidence: `IMPLIED` — this is a count of the lesson's own printed list, not a new rule.**

Printed rules R1–R9 (`V10_SOURCE_NOTES.md` §6c) plus 6.11–6.18 reduce to **four preconditions and
three triggers**:

| Class | Condition | Codable today? | Blocker |
|---|---|---|---|
| Pre | A weekly extreme exists (PFH/PFL = HOW/LOW) | **YES** — Q1 gives it | — |
| Pre | Price has moved away and confirmed ("the lock") | **NO** | Q3 — no threshold |
| Pre | Level-one consolidation is clear | **NO** | `consolidation` undefined; `level` undefined (`A-004`) |
| Pre | DNC — do not counter back toward the peak | **YES as a prohibition** | — |
| Trig | Visible stop hunt, preferably outside the blue box | **NO** | `blue box`, `stop hunt` boundary — `A-076` |
| Trig | Second leg M or W | **NO** | `second leg` — `A-007`, still open after ten lessons |
| Trig | (bonus) third touch of the level | **NO** | `level` — `A-004` |

**Two of seven are codable. The lesson's headline trade is not testable at V10**, and that is the
honest position rather than a reason to approximate. `D-030`.

**This is why `PT-036` tests V10's *quantitative context claims* and not its *signature trade*.**
Testing the signature trade would require inventing three definitions, producing a number that
would outlive its caveat — the precise failure `D-030` was written to stop.

---

## Q7 — Does V10 advance `A-004` (*the level*)?

**Confidence: `EXPLICIT` that it does not; the assessment is `INFERRED`.**

**No — and it makes the gap more conspicuous, not less.** V10 uses level-language throughout:
*"level one consolidation"* (`[00:45:03]`), *"level three"* (`[00:59:16]`), *"Level 3"* printed on
the flashcard (`34:22`), *"the levels"* as the fourth item in the priority list (`[00:23:36]`),
*"I can't identify level three"* quoted from a student (`[01:16:28]`).

**That last one is the telling row.** The speaker quotes a student saying they cannot identify level
three, and answers `[01:16:36]`–`[01:16:46]` *"I'm telling you how to identify: you take the trade
in line with the peak formation that was previously formed from yesterday."* **He answers a
different question** — he supplies a *workaround that avoids needing the level*, not a definition of
it. Read charitably that is good teaching; read as corpus evidence it means **`A-004` is
deliberately routed around rather than resolved.**

**`A-004` stays OPEN and is now the project's largest single blocker for the tenth consecutive
lesson.** Escalated in the mastery report.

---

## Q8 — What is the strongest reason to doubt this session's reading of V10?

*Required by `REVIEW_PROTOCOL.md` §1's standard — the falsification question, asked against myself.*

**The strongest doubt is that I have treated `[01:14:06]` as a definition when it may be an
aside.**

The sentence sits inside a digression about whether the method is "multi-timeframe analysis". It is
a **relative clause**, not a numbered rule: *"…the peak formation low, or low of the week, which is
the highest point on a chart within the week."* It is stated **once**, at minute 74 of 96, and is
not printed on any slide in that form.

**What survives the doubt:**

- The identity `PFH = HOW` and `PFL = LOW` **is printed**, on the rules slide (`43:17`), which is
  the lesson's most formal artifact.
- The equation of HOW/LOW with the week's extreme is **used operationally** elsewhere:
  `[01:33:43]`–`[01:33:51]` *"Identifying the higher low point of the week … there's looks like the
  lowest point on the chart right now, let me draw a line on the lowest point of the chart."*
- `[01:14:06]` is therefore **restating** a working identity, not coining one.

**What does not survive, and is recorded as a limit:** a single relative clause is thinner evidence
than a printed definition would be, and **`A-010` is therefore recorded as NARROWED, not CLOSED.**
If a reviewer reads `[01:14:06]` as an aside, the correct consequence is that `A-010` stays where it
was — **and nothing else in this session's work changes**, because no test and no rule depends on it.
`PT-036` measures weekly ranges from OHLC and does not use the term at all.

---

## Q9 — Machine candidates, recorded and fenced

`D-010` / `REVIEW_PROTOCOL.md` §P. **None of these is a course rule. None may be coded.**

| Candidate | Would formalise | Status |
|---|---|---|
| `PFH(w) = max(high) over trading week w` | Q1's definition | `INFERRED MACHINE CANDIDATE / NOT A COURSE RULE` — closest to codable of anything in V10, but still needs the week boundary, which V10 does not state |
| `lock(t) = extreme unbroken for N hours AND displacement ≥ M pips` | Q3 | `NOT A COURSE RULE` — **N and M do not exist in any source.** `DO NOT CODE` |
| `stop_hunt = excursion beyond blue_box then close back inside` | Q5 | `NOT A COURSE RULE` — `blue box` undefined; and the lesson explicitly admits setups that do **not** exit the box |
| `target = 50 pips`, `anchor_distance ∈ [25,75]` | 6.13, 6.19 | **These two ARE stated numerically and printed.** They are still `DO NOT CODE` at Phase 1 because the *entry* they attach to is undefined — a target without a trigger is not a rule |

---

## Q10 — Confidence summary

| Claim | Confidence |
|---|---|
| V10 is presented entirely by the course author | `EXPLICIT` (five strands, zero counter-evidence) |
| V10 defines PFH/PFL as the week's extreme | `EXPLICIT`, with the Q8 caveat |
| The safety trade's rule list is complete as *stated* | `EXPLICIT` — printed on two slides |
| The safety trade is **not codable** at V10 | `EXPLICIT` — five of seven conditions rest on undefined terms |
| The lock has no stated threshold | `EXPLICIT` (absence verified by search) |
| Weekly range 600–1000 pips | `EXPLICIT` as a claim; **empirically tested in `PT-036`** |
| Friday close 25–50 pips off both extremes | `EXPLICIT` as a claim; **empirically tested in `PT-036`** |
| The 50–100 pip Friday-range implication | `INFERRED` — mine, labelled, tested separately |
| `A-004` is unresolved and routed around | `EXPLICIT` for the absence; `INFERRED` for "routed around" |
