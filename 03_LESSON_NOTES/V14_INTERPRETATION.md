# V14 — INTERPRETATION

Written from the transcript, with the frame pass declared in `V14_SOURCE_NOTES.md` §0.
**Confidence grades are per-question and are meant to be argued with.**

---

## Q1 — Does V14 settle whether a Week 6 recording is missing, or whether the break just ran long?

### ⭐ **YES. It settles it, in the direction of MISSING — and the decisive datum is not in V14.**
**Confidence: HIGH on the arithmetic, MEDIUM-HIGH on the conclusion.**

`V13_REVIEW_R1.md` GATE (c) asked V14 to listen for *"anything about the return date or the week
numbering — it is the cheap decider."* **V14 supplies the return date and does not supply a week
number.** What it supplies instead is better: **an account of what happens to the skipped week.**

**What V14 says, confirmed verbatim by this session's own ASR pass:**

| `[ts]` | Words |
|---|---|
| `[00:00:57]` | *"if you don't get a link from me on Saturday, then after the meetup, **Tannen will take this recording, go home, render it**, and then we'll post it up for Sunday morning"* |
| `[00:01:08]` | ⭐ *"**So that will be your boot camp for the week** — to watch the recording that we did over there"* |
| `[00:24:18]` | *"**Week five R&D**, you got two weeks to do this stuff"* |
| `[00:40:46]` | *"you've got two weeks. **We're off next week.**"* |
| `[00:47:34]` | *"I'll see you in **two weeks**, unless you come to Orlando"* |

**`[00:01:08]` is the new fact.** The 2012-04-22 week is not merely cancelled — **it is filled, by a
different artifact**: a recording of the Orlando meetup, rendered by a named person and posted to
the forum. **That artifact is also absent from this library**, and it is a second missing item, not
the same one.

### The calendar, laid out

| Date | Day | What the corpus says | File present? |
|---|---|---|---|
| 2012-04-08 | Sun | Week 4 (V11, V12) | ✅ `Wk4 040812` |
| **2012-04-15** | **Sun** | **Week 5 (V13, V14)** — *"this is week five"* V13 `[00:17:52]` | ✅ `Wk5 041512` |
| 2012-04-21 | Sat | **Orlando meetup.** *"that will be your boot camp for the week"* | ❌ **absent** |
| **2012-04-29** | **Sun** | **The announced return.** V13 `[00:05:20]` *"Next session is going to be Sunday the 29th, that's two weeks"*; V13 `[00:05:33]` *"we'll get started again with **week six** through ten"* | ❌ **absent** |
| 2012-05-06 | Sun | next surviving file | ✅ `Wk7 050612` |

### ⭐ The decider, and it is a forward check into a file this session did NOT ingest

**Disclosed plainly:** to settle the numbering this session ran **one narrow `grep` for week-number
statements** against the *supplied* transcript of `Wk7 050612 Part1` — the V15 source. **This is a
corpus-level string check, not an ingestion**: no V15 artifact was created, no V15 content was read
beyond the week-number lines and the surrounding twenty lines needed to see they were unprompted,
and the V15 gate is untouched. It returns:

```text
[00:00:02]  "Alright, week seven."
[00:00:23]  "Week seven."
```

**The speaker's own spoken numbering on 2012-05-06 is SEVEN.** If the schedule had merely slipped —
if the 04-29 session never happened and 05-06 was the return — the speaker would have called it
**week six**, because that is the number he announced for the return. **He calls it seven.**

**Therefore a Week 6 session took place, on or about 2012-04-29, and its recording is not in this
library.** The week numbering did not slip; a file is missing.

### What would defeat this, stated because it should be

1. The speaker miscounts. Possible — he is loose with numbers throughout this corpus — but he
   states *"week seven"* **twice, unprompted, in the first 25 seconds**, which is where a person is
   most likely to be reading it off a plan.
2. *"Week 6"* was the Orlando meetup, making 04-29 Week 7's session held a week early. **Defeated
   by the file's own name**, `Wk7 050612` = 2012-05-06, and by V13 `[00:05:20]` placing the next
   *session* on the 29th.
3. The library is the owner's copy and the file may exist elsewhere. **This is not a defeater, it
   is the precise claim**: the recording is **absent from this corpus**, and this record says
   nothing about whether it exists in the world.

**Two artifacts are missing, not one: the Week 6 session (≈2012-04-29) and the Orlando meetup
recording (2012-04-21).** Filed as `A-092`.

---

## Q2 — Does V14 deliver the content V13 promised?

### **YES, and it is the most completely specified method the corpus has produced.**
**Confidence: HIGH.**

`COURSE_PROGRESS.md` V13 GATE (b) set the test: *"if it does not, THAT is when a gap is recorded."*
No gap is recorded. `[00:00:00]` *"let's get back to today's lesson and what you're going to do
this week."*

**Why "most completely specified" is a claim worth making, and how it is checked.** The corpus's
standing problem, recorded across `A-001`, `A-004`, `A-007`, `A-010`, `A-011`, `A-033`, `A-039`,
`A-056`, `A-077`, is that named objects are never defined. **The board drill is built almost
entirely from objects that need no definition:**

| Step | Object | Definable? |
|---|---|---|
| record high/low at 01:00 NYC | a clock time and two prices | ✅ arithmetic |
| range ≤ 50 pips | subtraction | ✅ arithmetic |
| *"trading in the middle of the range"* | **a position within the range** | ❌ **`A-089` — the one gap** |
| dealer extends either level | a breach of a recorded number | ✅ arithmetic |
| fails to hit it again for 1 hour | **a duration** | ✅ **stated, printed and spoken** |
| stop 5 pips beyond that number | a distance | ✅ arithmetic |
| aim for 30 to 50 pips | a distance | ✅ arithmetic |

**Six of seven steps are computable. One is not.** That ratio is unprecedented in this corpus, and
it is why V14 supports a pre-registered test where most lessons do not.

---

## Q3 — What does the TDI passage do to `A-084`, `A-085` and `A-086`?

**Three different answers. This is the section a reviewer should attack hardest.**

### Q3a — `A-084`: **NARROWED, NOT CLOSED. Confidence: HIGH.**

`A-084`'s required research is *"(a) a statement that the plotted line **is** the RSI… or (b) a
smoothing length."* V13's carry-forward (a) named **a spoken identity statement** as one of exactly
three surviving routes. **V14 contains the closest thing the corpus has produced to one — a direct
student question about the green line's construction, answered live — and it still does not close.**

**The temptation, stated so it can be checked:** `[00:44:45]` asks whether *"the green RSI line
represent[s] the **15-minute chart candles**"* and the answer at `[00:44:51]` is **"Yes."** If the
green line *is* the 15-minute — with no aggregation and no lag — that reads as **`k = 1`, the bare
RSI**, which would close `A-084` outright and unblock the whole of V11's RSI half.

**It was declined, on a defeater this session considers decisive:**

> ⭐ **The same sentence that would have to be read literally for green is demonstrably figurative
> for red.** `[00:44:49]` asks whether *"the red trade signal line represent[s] the **one hour**"*,
> and `[00:44:51]`'s **"Yes"** covers **both halves of a compound question**. But the red line in
> every TDI build — including this project's own `MMM_TDI.txt` — is a **short moving average of the
> RSI computed on the chart's own timeframe**. It does not read the one-hour chart. **So the red
> half of that "Yes" is a lag-gloss, not a construction.**
>
> **You cannot take the green half literally and the red half figuratively from a single "Yes".**
> Either the answer describes construction — in which case it is **false for red** — or it
> describes felt timeframe-equivalence, in which case **it says nothing about `k` for green.**
> `D-030` does not permit picking the reading that unblocks the most work.

**Three further defeaters, none of which alone would be enough:**

1. `[00:44:56]` *"The TDI line, **RSI is green**"* is a **naming** statement, and it is the exact
   shape V13 R1 tested and rejected: `MMM_TDI.txt`'s own buffer list calls the smoothed buffer
   **`RSI Price Line`**. **Naming a smoothed buffer after its input is the shipped convention**, so
   the name is evidence of lineage, not identity.
2. **The premise of the question is false as construction for all three lines.** The TDI's three
   lines are all built from the same chart's RSI at different smoothing lengths; **none of them
   polls another timeframe.** A student's false premise, affirmed, is not a specification.
3. **`k = 2` also fits.** On a 15-minute chart a 2-period average spans 30 minutes — which a
   speaker may loosely call *"the 15-minute"* just as readily as a 7-period average (105 min) gets
   called *"the one hour"*. **The passage cannot separate `k = 1` from `k = 2`**, and `PT-040`
   already measured that `k = 2` disagrees with `k = 1` by **5.16 pp at `t = 50`**, past its own
   materiality boundary.

```text
A-084 -- REMAINS AN ACTIVE BLOCKER. V11's RSI threshold claims STAY BLOCKED.
```

**⭐ And the negative result is the more valuable half, for the gap audit.** V13's carry-forward
listed three surviving routes: a properties dialog, a Navigator/inputs tab, **or a spoken identity
statement**. V14 is the best spoken opportunity the corpus is likely to offer — an unprompted
student question about exactly this — and the answer is a naming restatement plus a false-premise
affirmation. **The spoken route is now demonstrably weaker than it looked**, not because it was
tried and failed once, but because **the failure mode is structural**: the speaker answers questions
about the indicator in terms of what it *feels like*, not what it *computes*. `[00:15:40]` in V12
already said so — *"I don't know the math on it"*. See `A-093`.

**Frame route, V14: NEGATIVE, and measured rather than assumed.** All **582** swept frames were
scanned in code for a large light-on-dark rectangular region (`>25%` light pixels in the stage area,
excluding player chrome). **54 frames trip the detector, in four contiguous runs, and every run was
accounted for**: **50** are the lesson's hand-drawn white-background whiteboard slides, one
unbroken run `[07:45]`–`[11:50]`; **2** are the opening title `[00:00]`–`[00:10]`; and **2 are
stray Windows windows** — `[20:10]` a small file dialog and `[34:40]` a driver install log listing
`ChipsetENU.dll` and siblings, **both opened and read as images**. **No MetaTrader properties dialog
and no Navigator panel exists in this lesson.** Third consecutive lesson; **2,047 frames now
swept across V12, V13 and V14 with no dialog.**

### Q3b — `A-085`: **EXTENDED, NOT CLOSED, and made worse. Confidence: HIGH.**

V12 gave the claim four times as a **mechanism** (*"polls"*, *"pulls the one-hour chart and brings
it into the 15 minute"*). **V14 gives it in its strongest form yet — flat identity:**

> `[00:44:59]` *"**The red line, blood in the water, is the one hour.**"*

**No period, no formula, no account of polling — for a second lesson and a fifth statement.** And
the identity phrasing removes the last bit of hedging the word *"polls"* carried. `A-085`'s required
research is *"any statement distinguishing 'polls the one-hour chart' as a mechanism from the same
phrase as a description of lag."* **V14 supplies the opposite: a statement that makes the two harder
to separate.** Stays `DO NOT CODE`.

### Q3c — `A-086`: ⭐ **MATERIALLY ADVANCED on one axis, and it opens a contradiction on the other.**
**Confidence: MEDIUM-HIGH.**

`A-086` records two defects in V12's band passage. **V14 moves both, in opposite directions.**

| Axis | V12 | **V14 `[00:45:09]`** | Effect |
|---|---|---|---|
| **Multiplier** | *"some formula deviation **2%**, I don't know, **two standard deviations**… or something like that. **I don't really know because I didn't invent it**"* | *"**two standard deviations**"* — **flat, unhedged, unprompted** | ⭐ **ADVANCED.** The `2%` alternative is not repeated; the speaker states one value with no disclaimer, five weeks later |
| **Basis** | *"away from **the market baseline**"* → corrected on a chat prompt to *"based on **the RSI line itself**… **from the RSI line. Thank you.**"* | *"away from **the market base**"* | ⚠️ **REVERTS to the answer V12 RETRACTED** |
| **Period** | never stated | **never stated** | ❌ unchanged |

**The basis reversion is a genuine Tier-1 contradiction and is filed as `C-021`.** Its shape matters:
V12's final position was reached **under correction from the chat** and held with the least
confidence in the lesson; V14's is **unprompted, unhedged, and five weeks later**. ⭐ **And
`MMM-NOTES` p.45 — Tier 2 — sides with V14**: *"applied to the **market baseline** of the indicator
instead of price."*

**`A-086` nonetheless STAYS `DO NOT CODE`, and the reason is the third row.** The band's **period**
is still never stated anywhere in Tier 1 or Tier 2. A multiplier and a basis do not construct a
band without a lookback. **`A-031` and `A-032` — shark fin and blood in the water, the corpus's
best-defined signals — therefore remain uncomputable**, exactly as `A-086` says they do.

> ⚠️ **This is the second consecutive round in which this session's most attractive result did not
> deliver what it was hoped to deliver.** The temptation here was to write *"A-086 CLOSED"* on the
> strength of an unhedged Tier-1 sentence that Tier 2 corroborates. **It closes one of three
> required quantities.**

---

## Q4 — Is the drill a deployable method, or a training exercise? (the `A-082` hazard)

### **The speaker says both, and this session adopts NEITHER as doctrine.**
**Confidence: HIGH that the tension is real; the record carries both.**

`COURSE_PROGRESS.md` V13 GATE (f) flagged **the `A-082` class of error** — a drill parameter
adopted as the method's parameter — as *"the V13/V14 audit target"*, and it has a live instance
here. **The 5-pip stop and the 30–50 pip target are the most tempting numbers in this lesson**,
because they are precise, printed (the stop), and would slot straight into a spec.

**They must not.** The evidence runs both ways and the record carries it that way:

| Reads as EXERCISE | Reads as METHOD |
|---|---|
| `[00:32:42]` *"**That's a drill**"* | `[00:07:40]` *"**This is how I learned**"* |
| `[00:37:12]` *"a very important drill **to help you understand the candles**"* | `[00:28:33]` *"**This is how I learned how to trade**"* |
| `[00:40:33]` *"It's going to make you **see what's going on in the candles**"* | `[00:46:20]` *"technically, Keith, **you will be able to trade off of the board only**"* |
| `[00:32:25]` *"open a long position **in demo**"* | `[00:07:43]` *"this is **why I don't take shit inside the blue box**"* — present tense, his own trading |
| `[00:34:35]` *"**Promise me you will do this** — this and the TDI are priceless"* | `[00:41:04]` *"This is what **the drill** is"* |

**`[00:46:20]` is the strongest single line for METHOD**, and it is an answer to a student asking
precisely this question. ⚠️ **Its first word is unresolved between two ASR engines** — *"No"* or
*"Now"* — and the transcript says so. **The substance survives either parse** (*"No, technically you
will be able to…"* and *"Now technically you will be able to…"* both assert the capability), but a
reviewer should know the record rests on a line whose first word this session could not read.

```text
NOT ADOPTED AS DOCTRINE. The 5-pip stop and the 30-50 pip target are recorded as
THIS DRILL'S parameters and are cited nowhere in 12_MASTER_SPEC/ or 13_MACHINE_SPEC/.
PT-042 tests them AS THE DRILL'S OWN CLAIM and says so in its scope statement.
```

---

## Q5 — What does the drill do to `A-056` ("Hi-Lo": named, recommended, never taught)?

### ⭐ **`A-056`'s required research is ANSWERED. The record advances further than any other in V14 —
### and it does not fully close, on one step.**
**Confidence: HIGH that it is answered; MEDIUM that it should not be closed outright.**

`A-056`'s Required Research, verbatim: *"Whether any later lesson — or 'Jim' in any recording in
this library — states **how** the day's extreme is identified before it is known. If no lesson does,
the project must record that the corpus recommends a method it does not contain."*

**A later lesson does. It is this one, and it is taught by the course author, not by Jim.** V07
`[00:07:38]` deferred it — *"Jim… seems to be a master at the high of the day"* — and V14 delivers
it directly, seven lessons later, as a printed six-step procedure plus a week's assignment.

**The match to `A-056`'s stated object is exact.** `A-056`'s course meaning is *"entry at, or within
a few pips, of the day's high or low"*, and the missing piece is *"a method of identifying the
extreme in real time"*. V14: `[00:35:51]` *"you're looking for **the lock**, you're looking for the
number that's the **highest point on the board for the day**"*; `[00:37:53]` *"the strongest
resistance in the day is 32 30. **It's the high of the day.**"* — with entry **10 pips inside** and
a **5-pip** stop, i.e. within a few pips.

**Why this session does not write `CLOSED`:** step 2 — *"Find a pair that is trading in the middle
of the range"* — is **printed and spoken and never defined**, and the speaker's own two worked
examples span the **20th and 45th percentiles** of their ranges. **A method with an undefined
selection step is not yet computable**, and `D-030` binds. `A-056` is updated to
**`MATERIALLY ADVANCED — the method is present and specified; one printed step lacks a
definition (A-089)`** and the closure decision is **put to the reviewer**, not taken here.

⭐ **Note for the gap audit:** this is the first time in the corpus that an `A-039`-shaped
record — *"load-bearing component, never defined"* — has been **answered by a later lesson rather
than deferred again**. `PT-033`/`BT_V07_0001` measured that the missing skill was worth **+0.29 to
+0.37 in hit rate** against matched random entry. **`PT-042` now tests the skill itself.**

---

## Q6 — What does it do to `A-077` ("the lock", with no threshold)?

### ⭐ **V14 supplies the `N` that `A-077` says appears in no lesson — at a DIFFERENT SCALE from
### V10's. The record splits rather than closes. Confidence: HIGH.**

`A-077` records an inferred candidate it explicitly refused: *"the extreme is unbroken for **N**
hours AND price has travelled **M** pips from it"*, with the note **"N and M appear in no lesson and
in no `MMM-NOTES` page."**

**V14 supplies both, printed and spoken:**

| | Value | Where |
|---|---|---|
| **`N`** | **1 hour** | **PRINTED** on the assignment slide: *"fails to hit it again for **1 hour** take a position"*. Spoken `[00:28:09]`, `[00:31:33]` *"start a stopwatch"*, `[00:34:36]` *"45 minutes, an hour, hour and 15"*, `[00:46:05]` *"a lock for one hour, one and a half hours, ninety minutes"* |
| **`M`** | **~15 pips** | `[00:09:43]` *"14, 15 pips with the spread he pulled off the level"*; `[00:11:40]` *"he pulls back quickly 15 pips or so"*; `[00:39:56]` *"trading 15 pips or so off of the low plus the spread"* |

**And the speaker uses `A-077`'s own word for it:** `[00:35:51]` *"you're looking for **the lock**"*.

### ⚠️ Why this does NOT close `A-077`, and the reason is a real finding

**The scales differ by an order of magnitude.** V10's lock is narrated at *"the last **15 hours, 16
hours**"* on a **weekly** extreme (peak formation high/low). V14's is **1 to 1.5 hours** on a
**session** extreme. **Same word, same mechanism, thresholds ~10× apart, and no lesson reconciles
them.**

**This is not filed as a contradiction**, because `A-077` itself records that V10's *"15 hours, 16
hours"* is **narration of one chart, not a rule** — so there is no rule-versus-rule clash to
adjudicate. It is filed as `A-094`: **is "the lock" one concept with a scale-dependent threshold, or
two concepts sharing a word?** Until that is answered, **V14's 1 hour may not be transplanted onto
V10's safety trade**, which is exactly the lookahead-bias hazard `A-077` exists to prevent.

```text
A-077 -- ADVANCED, NOT CLOSED. The SESSION-scale lock now has a stated threshold
(1 hour, printed). The WEEKLY-scale lock in V10 still has none, and V14's figure
must NOT be borrowed for it. See A-094.
```

---

## Q7 — The EMA frame: does V14 bear on `D-041`/`D-042`/`D-043`?

### ⭐ **YES — an independent Tier-1 corroboration of `D-043`'s period↔colour mapping, by ORDERING.**
**Confidence: MEDIUM-HIGH. It is ordinal evidence, not a printed period, and it is offered as such.**

`D-042` §1 records that the exhaustive nickname↔period search returned **NEGATIVE**, and that **one
Tier 1 colour statement contradicts** the owner's mapping. `D-043` then reversed `D-041` and
`D-042` §2 on owner ruling. **The mapping currently rests on owner attestation with thin Tier-1
support.**

`V14_00-13-05_emas-yellow-red-cyan-white-low-test-candle.png` is a **2012, Tier-1, instructor's-own
chart** carrying **four** moving averages, and their speed ordering is unambiguous at full
resolution:

```text
YELLOW  — fastest; weaves through the candle bodies
RED     — second; lags yellow throughout
CYAN    — third; smooth, crosses price rarely
WHITE   — slowest; near-straight across the visible window
```

**Under `D-043`:** Mustard = 5 = **yellow** · Ketchup = 13 = **red** · Water = 50 = **aqua/cyan** ·
Mayonnaise = 200 = **white**. **The observed speed ordering is `yellow < red < cyan < white`, which
is exactly `5 < 13 < 50 < 200` under `D-043`'s colours.**

⭐ **And it is inconsistent with the superseded `D-042` §2 mapping**, which had **5 = red** and
**13 = yellow** — under which **red would be the faster of the two**. The frame shows the opposite.

**What this is and is not.** It is **not** a printed period and it does **not** close `A-020`. It is
an **ordinal** datum: the *relative speeds* of four differently-coloured lines on the instructor's
own 2012 chart. **It corroborates `D-043` and falsifies `D-042` §2 on the 5/13 rows, on the one axis
a picture can carry.** No fifth (blue/800) line is visible in the window, so nothing is claimed
about Blueberry. Recorded in `04_SCREENSHOTS/V14/INDEX.md` §3 and offered to the owner as the
Tier-1 corroboration `D-042` §1 said was missing.

---

## Q8 — Vocabulary: what does V14 name and not define?

Six terms, all worked in `10_AMBIGUITIES/`. **Per `D-040` the Mauro PDF (Tier 2) was searched before
any web research; results are tagged.**

| Term | `[ts]` | Status |
|---|---|---|
| *"trading in the middle of the range"* | printed + `[00:27:34]` | ⭐ **`A-089` — the drill's one uncomputable step** |
| *"blood in the water"* as the red line's name | `[00:44:59]` | ✅ **Not new** — `A-031` already CLOSED. V14 **corroborates the closure from a second lesson** |
| *"fractional disparity"* | `[00:20:55]` | **`A-091`** — a mechanism claim, recorded not adopted |
| *"the lock"* at session scale | `[00:35:51]` | **`A-094`** — scale relative to V10's |
| *"R&D"* as an assignment block label | `[00:24:18]` | Not a trading term. Noted, not filed |
| *"It's a liquid 50"* | `[00:45:14]` | ⚠️ **Unresolved by two ASR engines.** Not filed as vocabulary — this session cannot say it is a term |

---

## Q9 — What V14 contributes, and what it does not

**Contributes:**

1. ⭐ **The corpus's first fully-specified, real-time method for the day's extreme** — six of seven
   steps computable, printed and spoken, answering `A-056`'s seven-lesson-old required research.
2. ⭐ **A stated lock threshold** (`A-077`'s missing `N`), printed.
3. ⭐ **The Week-6 question settled** — a session is missing, and so is the Orlando recording.
4. ⭐ **An unhedged band multiplier**, advancing `A-086`'s first axis and opening `C-021` on its
   second.
5. ⭐ **Tier-1 ordinal corroboration of `D-043`** from a 2012 instructor chart.
6. **A pre-registerable test** — `PT-042` — on a claim the course states in its own numbers.

**Does not contribute:**

1. ❌ **`A-084` stays blocked.** The best spoken opportunity the corpus offers does not close it,
   and the reason is structural (`A-093`).
2. ❌ **No shark-fin `63`/`37` material.** `shark` and `63` occur **zero** times in 600 markers.
   `REVIEW_INDEX.md` item 157's `!SM_TDI` provenance question **gets no help from V14.**
3. ❌ **`A-085` gets worse, not better.**
4. ❌ **The bands are still not constructible** — no period.
5. ❌ **`A-011` (M/W anatomy) untouched for a tenth lesson.** `[00:08:11]` *"this looks like an M to
   you and you want to take it — but nothing has happened yet"* uses the shape to **forbid** a trade
   and still does not describe it.
