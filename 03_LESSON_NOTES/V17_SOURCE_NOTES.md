# V17 — SOURCE NOTES

**Lesson:** `Bootcamp1 Wk8 051312 Part1 (57mins).swf` · V17 · **2012-05-13** · 00:57:09
**Branch:** `video/v17`, worktree `MMM-Agents-v17` (`D-038`)
**Every item below is tagged `[AUDIO]`, `[PRINTED]` or `[VISUAL]`.** The tags are
`grep`-falsifiable: `[PRINTED]` means the words are legible on a committed frame, `[AUDIO]` means
they are in the committed marker grid, `[VISUAL]` means the claim rests on something drawn or shown
but not written.

---

## §0 — DECLARED DEVIATIONS, READ THIS FIRST

| # | What | Consequence |
|---|---|---|
| `D1` | ⚠ **`SWF_CAPTURE_RECIPE.md` §9's transcript-before-frames ordering was BROKEN**, as in V13–V16. The frames were captured and read before these notes were written. **Mitigated by the `[AUDIO]`/`[PRINTED]`/`[VISUAL]` tag on every item**, so a reviewer can strike the visual legs and see what survives | The §9 rationale — *"keeping the two passes separate is what lets a reviewer see which conclusions survive on audio alone"* — is **not** satisfied by tagging. It is mitigated, not met. **Fifth consecutive lesson.** Open item **241** |
| `D2` | **Four conclusions rest on frames and would not exist without them.** Named individually: `D2a` §7's identification of the two quiz pairs as **GBPUSD** and **GBPJPY**; `D2b` §8's seven-point answer key, which is **printed and never read aloud in full**; `D2c` §11's *"50/200"*, printed, against the audio's *"5200"*; `D2d` §14's live slide edit | A reviewer who discards the frames loses all four |
| `D2a′` | ⚠⚠ **`D2a` AS FIRST COMMITTED OVERSTATED ITS CASE AND IS CORRECTED HERE.** It carried the clause *"(the audio's ~~`"G U"` at `[00:21:10]` is **wrong**~~)"*. **The independent ASR pass renders `GU` as well** — the committed transcript is faithful, and **the SPEAKER is the one who is wrong**, as `[00:21:50]`'s *"Now this is pound yen"* about the same chart shows. `V17_TRANSCRIPT.md` §5a; **`C-027`**. Superseded text retained per `REMEDIATION_PROTOCOL.md` §2 | ⭐ **The pair identification itself is UNAFFECTED** — GBP/JPY on three supports |
| `D3` | ⚠ **The frame sweep DID NOT follow §10's script literally** — `t0` is set **before** the click, which is open item **188**'s proposed fix and V16's `D3`. **This is why §8a's offset measured zero for the second consecutive lesson.** The recipe file itself was **NOT** edited (`D-038a`: policy ledger, integration branch only) | `04_SCREENSHOTS/V17/INDEX.md` §0.2; item **218** is now **twice**-confirmed and still owed |
| `D4` | **No forward read.** V18+ was not opened. V16's committed artifacts *were* read — a **backward** read, which needs no precedent | — |
| `D5` | ⚠ **The §7 screen detector under-samples short-lived screens, and it did so here.** The 5-second grid missed nothing structural, but *"trade two"* was on screen for **≈7 seconds** and is caught by exactly **one** frame (`i=245`). A screen shown for under 5 s would have been missed entirely | Declared rather than discovered later. Open item **242** |
| `D6` | ⚠ **The independent ASR pass ran CONCURRENTLY with the frame sweep on the same machine.** This is a resource-contention risk to the sweep's pacing — the §8a *rate* check (`§0.1`) was run **specifically** to detect it, and the per-100-frame interval held at `499.6–500.4 ms` throughout | No effect found. Disclosed because the risk was taken, not because it landed |

---

## §1 — WHAT THIS LESSON IS `[AUDIO+PRINTED]`

**Week 8, Sunday 2012-05-13, Part 1 of two.** It is a **two-part** lesson with a printed seam:

**R1 correction (item 244):** `[00:11:22]` is *"we took an extra **week in between**"*, not the
marker grid's *"extra weekend"*. Three independent ASR engines agree. Nine calendar weeks carrying
eight sessions supports the **shape** of `A-01`'s missing-week gap, not the missing lesson's date or
contents.

* `00:00:00`–`00:30:05` — **housekeeping, a progress audit, two graded pop quizzes and a
  week-in-review.** No printed section title; the deck's running head only.
* `00:30:10`–`00:57:10` — **`TREND`**, a printed section title card followed by eleven slides. This
  is the lesson's teaching content and its most structured material in the corpus to date.

The spoken framing is `[00:01:33]` *"tonight we're gonna cover basic stuff trends trap moves"* and
`[00:01:39]` *"next week I think we're gonna do some fractional disparity stuff"*.

⭐ **It is the first lesson in this corpus that dates and numbers itself from the inside AND prints
the same numbers on a slide.** `[00:00:11]` *"Today's the 13th"*, `[00:02:36]` *"Welcome to week
eight"*, and `V17_00-00-20_boot-camp-schedule-slide-may-13-to-july-1.png`.

---

## §2 — ⭐⭐ WHY YOUR PIVOTS DO NOT MATCH HIS: THE INDICATOR'S RECALCULATION WINDOW `[AUDIO]`

**This is the single highest-value passage in V17, and it answers a question the corpus has carried
open since V16.**

> `[00:08:09]` *"One of the biggest questions were my pivots don't match the pivots that you have on
> the chart. Yes, here's the reason why"*
> `[00:08:15]` *"When you measure the 24-hour period on a daily candle that can look closes at 5
> p.m"*
> `[00:08:22]` *"Our indicators designed to take the pivots"*
> `[00:08:27]` *"Around 12 1 o'clock in the morning depending on your dealer and what his GMT offset
> is and recalculate the 24-hour period"*
> `[00:08:33]` *"So the pivots are freshly put in place right before the London open"*
> `[00:08:37]` *"…and that's why your pivots will not match"*

**What this settles.** V16 `§9b` recorded the contradiction `C-023`: he says pivots are computed
*"midnight to midnight"* and forty seconds later says *"just do it on the daily candle for right
now."* **V17 says both are true of different objects** — the *daily candle* closes at 17:00
**`[INFERRED: dealer time]`**; the source says only *"5 p.m."*. The *indicator* re-cuts its own
24-hour window at 00:00–01:00 dealer time so the levels are
fresh at the London open. **`C-023` is not a contradiction between two statements about one thing;
it is a statement about a chart object and a statement about an indicator.** Recorded as an
**amendment to `C-023`**, and `C-023` is **downgraded, not closed** — see `§2a`.

### §2a — ⚠ AND IT INTRODUCES A NEW UNDERSPECIFICATION IN THE SAME BREATH

*"Around 12 1 o'clock in the morning **depending on your dealer and what his GMT offset is**"* is a
**one-hour-wide window whose position is a function of an unstated broker parameter.** For an
automation project this is worse than a wrong constant, because it is not a constant at all.
**`A-107`.**

⚠ **And it does not agree with V16's own printed slide.** V16 printed
`London Session Start / 2:00 To 3:00 AM, EST` (`A-105`). V17 says the pivots are placed *"right
before the London open"* at *"12, 1 o'clock in the morning"*. **12–01 is not immediately before
02:00–03:00**; there is a one-to-two-hour gap, and neither statement carries a timezone that would
close it. **`C-024`.**

---

## §3 — ⭐ THE PIVOT-ZONE SHIFT RULE `[AUDIO]`

**A conditional override of V16's candle-colour rule, and V16's rule is named explicitly.**

> `[00:08:49]` *"another question was that if you see candles falling down, but then the last candle
> you know it's been three days of drop"*
> `[00:08:56]` *"And it's midweek or it's coming to the end of the week"*
> `[00:09:00]` *"Because you know better you shift the pivot zone"* `[00:09:05]` *"To the pivot
> reversal"*
> `[00:09:08]` *"Okay, so what do I mean candles read it's down. **That's an m1 m3 day**"*
> `[00:09:13]` *"It's been dropping for three days. You got a W formation on the one-hour chart
> double-rearer"* `[00:09:19]` *"tracks to the low of the week"*
> `[00:09:21]` *"**Shift the pivot zone to m2 m4 for the next day even though the daily candles
> read**"* `[00:09:28]` *"The pivot projection is still down"*

**Reconstructed as a rule, with every antecedent left in:**

| | Condition |
|---|---|
| 1 | Yesterday's daily candle is **red** → V16's rule selects **`M1`/`M3`** |
| 2 | Price has been **dropping for three days** |
| 3 | It is **midweek or approaching the end of the week** |
| 4 | There is a **`W` formation on the 1-hour chart** with ⭐ **`double railroad tracks`** to the week's low *(`A-108`, **ARBITRATED** — not `double bottom`, which is what this session first guessed)* |
| 5 | That `W` **tracks to the low of the week** |
| **⇒** | **Override: use `M2`/`M4` tomorrow**, against what the candle colour says |

⚠ **Three of the five conditions are undefined in this corpus.** *"Three days of drop"* has no
tolerance, *"midweek or coming to the end of the week"* has no day list, and `W` has been undefined
since `A-011`. **This rule cannot be coded.** `A-109`.

⚠ **And note what it does to V16.** V16's colour rule was graded *"the most completely specified
rule in the lesson, and mechanically checkable"* (`V16_MASTERY_REPORT.md` §4). **V17 attaches an
override to it whose trigger is not checkable.** The colour rule's testability does not survive
contact with the next lesson. `A-109` records that; it is the sharpest thing V17 does to V16.

---

## §4 — ⭐⭐ WHAT PIVOTS ARE MADE OF — THE `OHLC` ↔ SESSION MAPPING `[AUDIO]`

**The lesson's best single idea, and it is delivered as an aside.**

> `[00:09:39]` *"It's kind of interesting that the pivot uses the open high low and closed as it's
> supporting resistance factors"*
> `[00:09:47]` *"I told you the whole business was about the open Asian range Asian channel"*
> `[00:09:52]` *"The high and low and where the dealer goes back into consolidation. **That's the
> pattern and that's what pivots are based on**"*
> `[00:10:13]` *"Support and resistance is the high below the Asian range **which is where it
> opens**"*
> `[00:10:22]` *"The consolidation at the end of New York going into Asia, **which is where it
> closes**"*
> `[00:10:27]` *"Okay, if you just had your alcohol moment for me saying that congratulations"*
> *(ASR: **a-ha moment**)*

**The claim, stated plainly:** the four inputs to a floor-trader pivot are not arbitrary — each maps
onto a phase of the market-maker day.

| Pivot input | Claimed session referent |
|---|---|
| `O` — open | the **Asian range**, where the day opens |
| `H` / `L` | the day's **extension** of that range |
| `C` — close | the **New York→Asia consolidation** |

⚠ **This is a rhetorical identity, not an arithmetic one, and it should not be coded as one.** A
daily bar's `O` is a single price at a single instant; the Asian range is an interval. He says
*"which is where it opens"*, not *"the open equals the Asian range high"*. **Graded `TIER 3 —
FRAMING`**, and `A-110` records that the corpus has no statement converting it into arithmetic.

---

## §5 — THE PROGRESS AUDIT, PRINTED `[PRINTED]`

Two printed checklists, both read aloud. They matter because they are **the course's own statement
of what a Week-8 student is supposed to be able to do**, which is the closest thing the corpus has
to a syllabus.

**`V17_00-06-05_where-are-you-by-now-you-should-checklist-slide.png`:**

> `Where are you?` · `By now you should…..` · `Have a set of Flash cards` · `Have 4hr Markups` ·
> `Have Taken TDI only Trades` · `Worked the Big Board` · `Moving AVG Only trades` ·
> `Understand Pivot Points` · `Use ADR and Hi/Lo Markers`

**`V17_00-11-15_take-a-ways-flash-card-4hr-big-board-slide.png`:**

> `Take – a- ways:` · `Can spot a clean set-up pattern (Flash Card)` · `Understand the big picture
> (4hr)` · `Have a deeper understanding as to how the dealer extends the Hi/Lo holds a level and
> comes above/below the same level for stop triggers and trap moves etc. (Big Board)` ·
> `Understand the traps and how the dealers set-up the traders for wrong directional trades with
> aggressive moves`

**`V17_00-12-40_take-a-ways-tdi-and-adr-slide.png`:**

> `Understand how to really use the TDI and how to manage your trades with it.` · `Can confirm a
> trade signal when combined with dealer price action, Timing and larger cycle` · `Can understand
> the relationship to yesterdays' High and Low and the behaviors at these levels` · `Can understand
> that price can not rise or fall indefinitely so ADR is used to see and track this behavior.`

The associated audio adds the 4-hour markup procedure — `[00:06:10]` *"You should wait for eight
hours into the session draw your support and resistance on the for our chart psychological levels"*
— and the Big Board drill's **purpose**, which he insists is not the trade: `[00:06:44]`–`[00:06:59]` *"Whether
you actually got the trades right or not… you just have to see how these jerks \| Dealers push the
price hit it lay on it open the spread \| And very their behavior at the high and low. That's what
you're supposed to get out of the big board"*, and `[00:07:04]` *"It took me six months to start
mastering the board."*

⚠ **`Big Board` is finally defined, and the definition is thin.** `[00:38:51]` *"the big board is
all price action with the high and low"*, opened with `F10` (`[00:39:14]`–`[00:39:16]`, *"F10 …
12 F10 thank you guys"* — a student supplies the key). This is an **MT4 platform feature**, not a
concept, and it is the first time in seventeen lessons that the corpus says what it is. `A-111`
records that *"all price action with the high and low"* does not identify the window.

---

## §6 — ⭐⭐ THE STUDENT FLASHCARD, PRINTED IN FULL `[PRINTED]`

`V17_00-14-15_student-flash-card-the-pattern-short-and-long-trade.png`. He puts it up as a model:
`[00:14:03]`–`[00:14:22]` *"Okay a pretty good flash card that I took out of the board that I thought
was awesome… \| if yours don't look like this \| Take a picture make them look like this."*

> **`The Pattern The Pattern The Pattern!!!`**
>
> `Short Trade:`
> `1) Asian range less than 50pips`
> `2) Stophunt 25-50pips above Asian range`
> `3) M reversal pattern`
> `4) RR on 2nd leg of M pattern`
> `5) TDI had Shark Fin`
>
> `Long Trade:`
> `1) Coming into US session(variation on theme).`
> `2) W reversal pattern`
> `3) Pins to the Blueberry & Mayo`
> `4) ADR nearly filled(close enough)`
> `5) TDI had Shark Fin`
> `6) TDI & Price already had 3 pushes lower`

⚠⚠ **PROVENANCE, AND IT IS THE WHOLE POINT.** This is **a student's checklist, endorsed by the
instructor** — not the instructor's own specification. Under `SOURCING_HIERARCHY.md` it is
**`TIER 2` at best**, and the project must not launder it into `TIER 1` because it is legible and
tidy. **It is the most complete entry checklist in the corpus and it is the least authoritative
one.** `A-112`.

⭐ **What it nevertheless supplies, and nothing else in the corpus does:**

1. **An Asian-range size FILTER** — `< 50 pips` — a precondition, not a measurement. New.
2. **`Stophunt 25-50pips above Asian range`**, agreeing to the pip with `[00:28:59]`'s *"25 to 50
   pips as his normal stop hunt"* on the same night. ⭐ **A student wrote a number and the
   instructor said the same number 15 minutes later, independently.**
3. **`Pins to the Blueberry & Mayo`** — **printed** moving-average nicknames, corroborating
   `V17_00-51-00_trend-reset-mayo-blue-berry-slide.png`'s `(Mayo ,Blue Berry)`. See `§15`.
4. **`ADR nearly filled(close enough)`** — the first statement anywhere in the corpus of *how much*
   ADR must be consumed before the reversal is expected, and it is **`close enough`**. `A-113`
   records that this is the corpus's answer and that it is not a number.
5. `RR on 2nd leg of M pattern` — **`RR` is undefined.** It is not expanded on the card, not spoken,
   and not in `EXTERNAL_VOCABULARY_REFERENCE.md`. `A-114`.

---

## §7 — POP QUIZ 1: TWO SAFETY TRADES `[PRINTED]` `[VISUAL]` `[AUDIO]`

**Format** `[00:19:34]`–`[00:19:45]`: *"I'm gonna show you two sets of trades…"* — two charts, 30 seconds
each, *"I want you to tell me which one is better and \| Why it's better."*

| | Chart | Frame |
|---|---|---|
| Trade one | **`GBPUSD,M15 1.61657 1.61677 1.61624 1.61659`** | `V17_00-20-05_pop-quiz-trade-one-gbpusd-m15-chart.png` |
| Trade two | **`GBPJPY,M15 128.848 128.876 128.760 128.813`** | `V17_00-20-25_pop-quiz-trade-two-gbpjpy-m15-chart.png` |

**The printed answer** (`V17_00-20-30_pop-quiz-answers-gj-ketchup-and-mustard-slide.png`):

> `Answers:` · `Safety Trades` · `Better selection: G/J gives clear confirmation by a close above the
> ketchup and mustard then soars to TP` · `G/U uses one bar to confirm and shift…no entry`

### ⚠⚠ THE PARAGRAPH THAT STOOD HERE WAS WRONG, AND ITS RETRACTION IS THE MORE INTERESTING RESULT

> *Superseded, retained per `REMEDIATION_PROTOCOL.md` §2:* *"~~AND THE FRAME CORRECTS THE
> TRANSCRIPT. At `[00:21:10]` the committed ASR reads "All right, this is **G U** safety trade" — but
> the chart on screen at burned timecode `21:10` is `GBPJPY,M15`, and the printed slide credits
> `G/J`. The ASR's "G U" is a mishearing of "G J".~~"*

**The independent ASR pass renders it `GU` too.** Two engines, same word. **The transcript is
faithful; the speaker misnamed his own chart** — forty seconds later, on the same chart, he says
`[00:21:50]` *"Now this is pound yen"*. **Filed as `C-027`.**

⭐ **The substantive answer is UNCHANGED and never depended on the retracted claim.** The better
trade is **GBP/JPY**, on three independent supports: the slide's printed `G/J`, the chart header's
`GBPJPY,M15`, and `[00:21:50]`. ⚠ **What the frames actually corrected was my reading of the
SPEAKER, which is a weaker claim than correcting the ASR.**

**The trade, from audio** `[00:21:16]`–`[00:21:48]`:

| | Value |
|---|---|
| Trigger | *"this clothes more right here it crossed is above the catch-up in the mustard"* → **a close above the ketchup and mustard** |
| Entry | *"grabbed here on the open of this candle"* — **the open of the bar after the confirming close** |
| Drawdown | *"absolutely zero draw down"* |
| Stop | *"very tight about **1819 pips**"* → **18–19 pips** |
| Held | *"the entire trade lasted **45 minutes to an hour**"* |
| Taken | *"I took **40** off of there because it was getting late for me"* |

⚠ **This is the most completely specified single trade in the corpus — and it is a post-hoc
narration of one trade, not a rule.** No `R:R` is stated (18–19 risk for 40 taken is ≈ `1:2.1`, but
**he does not say that and it is not a target**).

**Why `G/U` failed, audio** `[00:22:23]`–`[00:22:45]`: *"this was the actual entry bar this bar is not
an entry. It's blown out. It's too big"* … *"the first confirmed entry comes up here too late, man…
**45 pips off the low of the day too late scratch ain't no trade**"*. ⭐ **A printed disqualifier and
a spoken one: an entry bar that is *"blown out"*, and a late entry more than ~45 pips off the LOD.**
Neither has a threshold. `A-115`.

---

## §8 — ⭐⭐ POP QUIZ 2: THE SEVEN-POINT ANSWER KEY, PRINTED `[PRINTED]`

Seven numbers are drawn on a `GBPJPY,M15` chart
(`V17_00-24-30_gbpjpy-m15-chart-numbered-one-to-seven.png`); students get five minutes
(`[00:24:05]` *"it is now Seven o'clock straight up… No, it's 701. I'll be back at 706"*). The
answer key is then printed
(`V17_00-24-45_seven-point-answer-key-safety-trade-slide.png`) — **verbatim, `sic` included:**

> `Safety Trade`
> `1. Visible Trap Yesterday (PFL) LOW`
> `2. Dealer Handles The BO Traders and 200 Traders`
> `3. Dealer is Trading 25 to 75 pips off Y-LOD`
> `4. Dealer Cuts the Asain Range as a visible stop hunt`   *(`sic` — `Asain`)*
> `5. MM throws a spike and comes above for 1 hour`
> `6. W -TDI Blood`
> `7. Consolidation TP`

**⭐ This is the most complete printed setup checklist in the corpus.** It is `TIER 1` — the
instructor's own slide, walked through aloud for five minutes.

**The spoken gloss, point by point:**

| # | Audio | Marker |
|---|---|---|
| 1 | *"peak formation… is a miss peak formation low in the low of the week"* | `[00:24:46]` |
| 2 | *"the dealer handles the breakout traders here by grabbing their orders \| Right past the man using the dragon and backwards"* — ⭐⭐ **ARBITRATED: *"right past the mayonnaise and then dragging them backwards"***, so the mechanism is *take the orders beyond the Mayo, then drag price back* (`V17_TRANSCRIPT.md` §5c) | `[00:26:01]`–`[00:26:10]` |
| 3 | *"There's yesterday's low peak formation the distance from here here. Yes, he is"* | `[00:26:36]` |
| 4 | *"he extends the Asian low… with the session in a visible stop hunting motion. He gives you a clean stop hunt"* | `[00:26:45]` |
| 5 | ⭐ *"he came right back above that low… and stayed up there for a look one two three four five \| **An hour and 15 minutes**… if the dealer quits extending the low for **an hour and 15 minutes** You take a long position"* | `[00:27:30]`–`[00:27:48]` |
| 6 | *"Shark fin blood in the water a nice fat W. **You don't have a W in price you have a W in the closing of price**"* | `[00:28:06]`–`[00:28:09]` |
| 7 | *"you got Four green bars price takes off for one hour… it goes into its first level consolidation this was about **plus 40 and change**"* | `[00:28:22]`–`[00:28:26]` |

⭐⭐ **POINT 6 IS A DEFINITION AND IT HAS NEVER BEEN GIVEN BEFORE.** *"You don't have a `W` in price,
you have a `W` in the **closing** of price"* is the first statement in seventeen lessons that says
what the `W` is measured on. **It does not close `A-011`** — it says *which series*, not *how many
bars*, *what depth* or *what tolerance* — but it **narrows** it for the first time, and it explains
why `M`/`W` are readable in the TDI (a line of closes) and argued about in candles. `A-011` is
**AMENDED, NOT CLOSED**.

⚠ **AND THE PRINTED KEY DISAGREES WITH THE AUDIO ON POINT 1.** The slide says the trap was
**`Yesterday`**; the audio says the peak formation low was **the low of the week**. Point 3 then
references `Y-LOD` as a *separate* object. **Either yesterday's low and the week's low coincide on
this chart, or the anchor is stated two ways.** Nothing in the file decides it. **`A-116`.**

### §8a — ⭐ THE SAFETY TRADE, ASSEMBLED FROM ITS OWN SUMMARY `[AUDIO]`

He states the definition twice, and the two statements differ:

> `[00:28:53]` *"Peak formation has been formed the dealer makes a visible stop hunt below the Asian
> range \| **25 to 50 pips as his normal stop hunt** \| And he's trading above \| **25 to 75 pips off
> of yesterday's low**"*

> `[00:55:20]` *"coming at a level one consolidation if the dealer makes a visible stop on **25 to
> 75 pits off of that number** \| Paint a V or a W for me clearly at **3 30 in the morning** and I own
> that guy \| Because I know that that peak formation is a lock for at least **a London session** for
> me to book my **50**"*

⭐ **TWO DIFFERENT PIP BANDS FOR TWO DIFFERENT REFERENCE POINTS, AND THIS IS NOT A CONTRADICTION:**

| Band | Measured from |
|---|---|
| **25–50 pips** | the **Asian range** boundary — the stop hunt itself |
| **25–75 pips** | **yesterday's low/high** — where the dealer is *trading* |

The corpus has been carrying these as one figure. **They are two, and V17 is the first lesson that
uses both in the same paragraph with different anchors.** ⚠ **But `[00:55:20]` then applies
`25–75` to *"that number"* meaning the peak-formation level, which is a **third** anchor. `A-117`.

⭐ **And it supplies a time, a horizon and a target in one sentence** — *"clearly at 3:30 in the
morning"*, *"a lock for at least a London session"*, *"to book my 50"*. ⚠ **No timezone on 3:30**
(the same defect as `A-105`), and *"my 50"* is a personal target, not an instruction.

---

## §9 — THE WEEK IN REVIEW: THE `LEVEL THREE WEEK` `[AUDIO+VISUAL]`

`V17_00-14-40_level-3-week-after-a-correction-chart.png` prints
`Level 3 week after a correction / Confuse traders` on a chart annotated `HOW` / `LOW`
(ASR/handwriting for **HOW** = *high of week*, **LOW** = *low of week*).

> `[00:14:42]` *"there was what I call a **level three week** on the higher time frame"*
> `[00:14:46]` *"last week was corrective in nature… **This is pound dollar by the way**"*
> `[00:14:50]` *"Most people so it was a choppy week was volatile… **that is an excuse for retail
> traders**"*
> `[00:15:12]` *"What I want you to look for is **Short position near the high and a long position
> near the low everything else is bullshit**"*
> `[00:15:20]` *"Every day the dealer will make a high every day the dealer will make a low \| The
> only variation on that theme is he will trade in between those numbers and \| Repeat the same high
> or the same low and not necessarily take it out"*

⚠ **`level three week` is used, never defined.** The corpus has `level one` / `level two` /
`level three` as intraday consolidation counts (`A-036`); this applies the same word to a **week**.
Whether a *"level three week"* means three levels were completed in the week, or is a severity
grade, is not said. **`A-118`.**

⚠ **AND THE SAME IMAGE IS CALLED TWO DIFFERENT TIMEFRAMES.** At `[00:14:50]` it is
*"pound dollar"*; at `[00:31:39]`, on what the frames show to be **the same chart**
(`V17_00-35-00_level-3-week-chart-heavily-circled.png` is the same image with hand annotation),
he says *"This is the **four-hour** chart on GU by the way"*. **The chart carries no legible symbol
or period label** — that region is blank, unlike the quiz charts. **The timeframe cannot be
recovered from the frame** and rests on `[00:31:39]` alone. `A-119`.

### §9a — ⭐ THE ELEVEN-CANDLE ARITHMETIC, AND IT IS WRONG ON AIR `[AUDIO]`

> `[00:17:41]` *"one two three four five six seven eight nine ten eleven. **What's eleven times
> fifteen minutes** anybody"*
> `[00:17:55]` *"**165 divided by 60** how many hours is that it's easy to go?"*
> `[00:18:00]` *"One two three four one hour one two three four two hours one two three four three
> hours"*
> `[00:18:06]` *"Yeah, **four hour fifteen minutes**. Thanks man. All right, so roughly"*
> `[00:18:10]` *"**Three to four hours** right the dealer trapped this area worked it for three to
> four hours"*

**11 × 15 = 165 minutes = 2 h 45 m.** A student answers *"four hour fifteen"*, he accepts it, and
then immediately says *"three to four hours"* — a third figure. **The correct answer is none of
the three.** `C-025`.

⚠ **It changes nothing downstream** — no rule depends on it, and *"roughly three to four hours"* is
the number he uses. **It is recorded because an arithmetic slip accepted from the floor and repeated
is exactly the class of defect a transcript-only reading would smooth away**, and because his own
counting-out-loud at `[00:18:00]` reaches *"three hours"* and stops.

---

## §10 — THE TREND: TWO OF THEM `[PRINTED+AUDIO]`

`V17_00-38-20_how-do-we-identify-the-trend-slide.png`:

> `How Do We Identify The Trend?` · `There Are Two Types Of Trend.` · `MM Trend (Real Trend)` ·
> `Technical Trend (Rest of the world)` · `Levels Are Visible on all Time Compressions` ·
> `They Are Highly Visible On The One Hour Chart` · `TDI on the 4hr chart is very telling!!`

Audio adds the hedge: `[00:37:32]` *"to me the levels are visible on all-time compressions \| But
I've been added a little while so to be fair. **I want you to use the one hour chart** to view the
levels in the market maker cycles."*

⭐ **A quantified TDI signal, and it is the only pip-denominated prediction in the lesson:**

> `[00:38:29]` *"You get a **sharp fin** above these lines or below these lines **on a four hour
> chart** \| You get **blood in the water** \| prices gonna reverse \| **at least 50 pips**"*

⚠ *"these lines"* = *"there's support and resistance lines. There's a 50 in the middle"*
(`[00:38:25]`) — **the TDI's own bands, whose levels are `A-084`-blocked** (no indicator properties
dialog has appeared in **3,908 frames** across V12–V17). **The signal is stated; its threshold is
not knowable.** This is the pre-registered hypothesis `PT-045`.

`V17_00-39-25_trend-is-set-by-the-market-maker-slide.png`:

> `Trend Is Set By The Market Maker And Can Be Reversed At Any Time` · `Understanding This Gives You
> An Edge And Allows You To Trade Both Ways.` · `Don't Become So Biased That You Miss The Setups`

with `[00:40:33]` *"The stop on high drops and stop on low rises at the start of the session"* and
`[00:40:39]` *"Look to take positions when the dealer extends the high or low coming out of the
Asian range aggressively \| **He is setting the trend for the day**"* — ⭐ **a cycle-start test, and
the corpus's first.** `V16_MASTERY_REPORT.md` §4 listed *"no cycle-start test"* under what V16 does
not supply. **V17 supplies one, and it is qualitative** (*"aggressively"*). `A-120`.

---

## §11 — ⭐⭐ THE THREE-DAY CYCLE, DAY BY DAY `[PRINTED+AUDIO]`

**The lesson's centrepiece, printed across three slides and narrated in full.**

### Day 1 — `V17_00-42-10_three-day-cycle-day-1-slide-news-is-use-typo.png`

> `Trend Is Generally Setup As A 3 Day Cycle.` · `Day 1: Reversal Day Peak Formation High/Low` ·
> `Comes As A Market Surprise` · `Catches Everyone Following Traditional Indicators And Trend
> Following Strategy (Retail) Off Guard` · `News Is Use To Perpetuate False Trend` *(`sic`)*

> `[00:43:09]` *"day one is what I like to call **reversal day** \| It's where you get the peak
> formation higher low. It's the beginning of our market maker dealer cycle"*
> `[00:43:28]` *"It usually comes as a market surprise because everyone's reading… **It's going
> above the four hours crossed over TDI is above the market baseline** everything's on its way up"*
> `[00:44:35]` *"**The news is used**… to perpetuate the false trend \| The news is the trigger or the
> reason or the excuse to hit the stops or to spike away from the lower level shorts"*

### Day 2 — `V17_00-45-15_three-day-cycle-day-2-fifty-two-hundred-crossover-slide.png`

> `Day 2: Moving Avgs On Higher Time Frames Will Signal.` · `50/200 Cross Over Etc.` ·
> `Traditional Indicators Will Cross Over Or Fire A Signal` · `Zero Line MACD Crossover CCI Zero
> line Cross` · `Retail Traders Will Wait For Confirmations To Enter`

⭐⭐ **THE SLIDE SUPPLIES THE REFERENT.** The committed ASR renders *"you get a **5200** crossover"*
`[00:45:16]` and *"**The 5200** will cross over"* `[00:45:52]`, **and the independent ASR pass reads
it the same way** — so the transcript is faithful, and *"fifty-two-hundred"* is simply how `50/200`
is read aloud. **The slide prints `50/200`.** There is no *"5200"* period in this methodology; it is
the **50 EMA crossing the 200 EMA**. `[00:45:55]`'s
*"if the blueberries present you'll get the crossover on the old blueberry"* is consistent — the
crossover moves to the 800 when the 800 is on the chart.

⚠ **Note what this costs.** Without the frame, an automation project would have hunted for a `5200`
period. **`D2c`.**

### Day 3 — `V17_00-47-05_three-day-cycle-day-3-acceleration-slide.png`

> `Day 3: Traders Are Convinced This Is The Real Move.` · `Market Makers Show Acceleration &
> Separation From MAs A Certain Trap` · `News Is Used To Further The Cause` · `MM Apply The Brakes
> And Trap Everyone (Except Us) The Wrong Way`

> `[00:47:12]` *"**trend acceleration**. It's in the textbooks. It's where prices moving away from
> the averages you get **angle and separation** on the averages \| They're open and fanned out"*
> `[00:47:27]` *"**Prices dancing above the mustard** \| Price won't cut the mustard. That's how you
> remember prices above the mustard"*
> `[00:47:47]` *"The third leg of the third leg will show **three candles straight up**
> acceleration"*
> `[00:48:17]` *"That acceleration at **333 trade** where he hits the last three bars \| He gives you
> **three vector candles** at the end of a nice run"*
> `[00:48:31]` *"Is **the end of the dealer cycle most of the time** and that's where we take the
> opposite"*

⭐ **`A-097`'s *"33 trade"* / *"333 trade"* gains its clearest statement yet**: three vector candles
at the end of the third leg, read as a **terminal** signal. ⚠ **`A-097` is ADVANCED, NOT CLOSED** —
*"three candles straight up"* has no size test, *"vector candle"* is undefined in this corpus, and
*"most of the time"* is the reliability claim.

### And the mechanism he gives for why

> `[00:48:44]` *"People buy he sells to them over three days four days the dealer becomes \| **heavy
> net short** \| If you are heavy net short, how do you get paid? \| **Correct a market against the
> retail traders and book a profit**"*

⭐ **This is the first inventory-based explanation in the corpus** — the reversal is not a pattern,
it is the dealer's position being unwound. `V17_00-49-35_reversal-books-profit-broker-other-side-slide.png`
prints the retail-facing version.

### The timing arithmetic, and it does not close

> `[00:42:04]` *"The trend is generally set up as a three-day cycle **as soon as I say that it goes
> six days right?**"*
> `[00:42:14]` *"after the midweek reversal the reversal comes on Tuesday you'll probably have a
> **four-day** trend Until Friday"*
> `[00:42:25]` *"Once the trend is set there'll be a unidirectional swing for **two and a half to
> three days**"*

**Three durations in twenty seconds — 3, 4, and 2.5–3 — and he flags the instability himself.**
`A-121` records that the cycle length is a **distribution he never bounds**, not a constant.

⭐ **And one genuinely new mechanical claim:**
> `[00:42:48]` *"They'll make the clothes off of those numbers open high low clothes **gives you the
> wick on the daily candle**"* → `[00:42:55]` *"**the wick on the daily candle represents the
> consolidation off of the high or off of the low** To end the cycle for 24 hours"*

**A daily wick is re-read as the end-of-cycle consolidation.** ⭐ This is **falsifiable** and is the
descriptive half of `PT-045`.

---

## §12 — ⭐ TREND RESET vs TREND REVERSAL `[PRINTED+AUDIO]`

`V17_00-51-00_trend-reset-mayo-blue-berry-slide.png`, verbatim:

> `A Trend Reset Will Be Used For Market Makers To Book Profit And Not Reverse Directions.` ·
> `This will usually appear on a chart landmark (Mayo ,Blue Berry)` · `This is where there are retail
> order build ups` · `The Reset Will Represent A New Peak Formation` · `3 More Days Can Be Expected.`
> · `However, If No One Falls For It, He May Reverse After Only One More Level Of Rise/Fall` ·
> `4 Or 5 Levels Might Be Identified…….That Is Why We Use A Stop Loss!!!!!`

> `[00:51:17]` *"they'll go up up up they'll correct **make a W formation to continue up**"*
> `[00:51:39]` *"people trade across over the four hour… they traded **20 EMA on a four hour** charter
> or **20 EMA on a daily** chart crossover a break plus a close… **naturally that's where the orders
> build up so naturally that's where the aggressive behavior by the dealer will come in**"*
> `[00:52:05]` *"the dealer will break above will break below **the 200** and go back above"*

⭐⭐ **A RESET AND A REVERSAL ARE THE SAME SHAPE AND DIFFERENT EVENTS, AND THE DISCRIMINATOR IS
STATED:** *"The Reset Will Represent A New Peak Formation"* + *"3 More Days Can Be Expected"*.
**A reset is a continuation that re-anchors the peak; a reversal is a direction change.** This is
`§11`'s cycle applied recursively.

⚠⚠ **AND IT IS NOT DECIDABLE IN REAL TIME, WHICH THE SLIDE ITSELF CONCEDES.** *"If No One Falls For
It, He May Reverse After Only One More Level"* makes the outcome depend on **other traders'
behaviour**, which is unobservable, and *"4 Or 5 Levels Might Be Identified"* removes the count as a
discriminator. **The slide's own resolution is `That Is Why We Use A Stop Loss!!!!!`** — i.e. the
method's answer to its own ambiguity is risk control, not a rule. **`A-122`, and it is the most
honest thing in the lesson.**

⭐ **The stop, finally, and it is garbled:** `[00:53:42]` *"**15 25's** \| Total above the high below
the low if you grab a good entry."* ⚠ **This is the first stop-loss distance stated in the corpus
since `A-023`** and it is stated in a five-word fragment.

⭐ **ARBITRATED (`V17_TRANSCRIPT.md` §5, candidate 3):** the second engine reads *"**15, 20 pips.**
Total above the high, below the low."* **Both engines agree on `15` and on `total above the high,
below the low`; they disagree on the second number — `25` against `20`.** **Recorded as
`TIER 2 — PARTLY RECOVERED`:** the band starts at 15 and ends at 20 or 25, and **no V17 artifact
uses the upper figure.** `A-123` also records that *"total"* is unresolved (per-side, or summed).

---

## §13 — THE NUMBERS, ALL OF THEM `[AUDIO+PRINTED]`

Every quantity V17 states, with its anchor. **This table is the lesson's automation surface.**

| Value | What it measures | Marker / frame | Tier |
|---|---|---|---|
| **< 50 pips** | Asian range size, as a **filter** | flashcard, `00:14:15` | ⚠ **2** (student) |
| **25–50 pips** | stop hunt beyond the Asian range | `[00:28:59]`; flashcard | **1** |
| **25–75 pips** | dealer trading off **yesterday's** high/low | `[00:10:54]`, `[00:26:30]`, key point 3 | **1** |
| **25–75 pips** | visible stop hunt off **the peak-formation** number | `[00:55:20]` | ⚠ **1**, third anchor — `A-117` |
| **~25 pips** | *"if you only get 25 pips stop hunts"* — sizing a marginal trade | `[00:25:48]` | 1 |
| **18–19 pips** | the `G/J` trade's actual stop | `[00:21:39]` | 1 — **narration** |
| **15–25 pips** | *"total above the high below the low"* — stop placement | `[00:53:42]` | ⚠ 2 — garbled |
| **40 pips** | taken on the `G/J` trade | `[00:21:43]` | 1 — narration |
| **~+40** | *"plus 40 and change"* at first-level consolidation, key point 7 | `[00:28:26]` | 1 |
| **45 pips** | *"off the low of the day too late"* — a late-entry disqualifier | `[00:22:45]` | 1 |
| **50 pips** | *"prices gonna reverse at least 50 pips"* after a 4H TDI shark fin | `[00:38:41]` | ⭐ **1 — testable** |
| **50 pips** | *"a lock for at least a London session for me to book my 50"* | `[00:55:37]` | 1 — personal |
| **≥ 8 candles** | *"how many tails that take to form a good M and W on a 15-minute chart — eight Candles or above"* | `[00:34:55]`–`[00:35:04]` | ⭐ **1 — NEW** |
| **1 hour** | dealer stops extending the low → take the position | `[00:27:54]`, key point 5 | 1 |
| **1 h 15 m** | the same figure, measured on the example | `[00:27:41]` | 1 |
| **3 days / 4 days / 2.5–3 days** | trend cycle length | `[00:42:04]`–`[00:42:25]` | ⚠ `A-121` |
| **3 more days** | expected after a reset | `00:51:00` slide | 1 |
| **4–5 levels** | how many may be identified before a reversal | `00:51:00` slide | 1 |
| **3 candles** | the `333` acceleration | `[00:47:47]` | 1 |
| **50/200** | the Day-2 crossover pair | `00:45:15` slide | ⭐ **1 — PRINTED** |
| **20 EMA (4H, D)** | where retail orders build | `[00:51:47]` | 1 |
| **3:30 a.m.** | when the `V`/`W` should be clear | `[00:55:30]` | ⚠ no timezone |
| **8 hours** | how long into the session before drawing 4H S/R | `[00:06:10]` | 1 |

⭐⭐ **`≥ 8 candles` is the first quantitative constraint on `M`/`W` in the corpus.** With `§8`'s
*"a `W` in the closing of price"*, **`A-010`/`A-011` are ADVANCED on two independent axes in one
lesson** — series and minimum width. **Neither closes**: no depth, no symmetry tolerance, no
statement of whether *"eight candles"* counts the whole formation or one leg.

### §13a — ⚠⚠ A REAL `S/L` IS LEGIBLE ON A REAL TICKET, AND IT IS **NOT** A RULE `[PRINTED]`

`V17_00-13-40_andrew-closed-transactions-account-statement.png` is a student's broker statement,
shown for its **result** — `[00:13:31]` *"Andrew double this demo"*, `[00:13:36]` *"in a few days.
I might add I'm very proud of him"*. The table is legible:

```text
Account: 7131248   Name: Andrew   Currency: USD
Closed Transactions:
Ticket      Open Time           Type       Size  Item     Price     S/L       T/P       Close Time
106621630   2012.03.25 23:57    balance    Deposit
106637069   2012.03.26 14:07    sell       0.10  eurusd   1.33213   1.33813   0.00000   2012.03.26 14:10
106637070   2012.03.26 14:07    sell limit 0.20  eurusd   1.33663   1.33813   0.00000   2012.03.26 14:10
```

⭐ **This is the first observed stop-loss DISTANCE anywhere in the corpus that is a number on a
record rather than a phrase in speech**: `1.33813 − 1.33213 = 60.0 pips` on the market sell, and
`1.33813 − 1.33663 = 15.0 pips` on the sell limit — **a shared stop price for a two-leg position**,
which is a scale-in, not two trades. `T/P` is `0.00000` on both: **no take-profit was set.**

⚠⚠ **AND IT MUST NOT BE PROMOTED INTO A RULE.** Under `SOURCING_HIERARCHY.md` this is **`TIER 3`** —
a third party's execution record, displayed to praise a P&L curve. **The instructor does not read the
`S/L` column, does not endorse `60` or `15`, and does not mention stops on this slide at all.** It is
recorded here because *"the corpus contains no stop-loss distance"* would now be false, and because a
future session that finds this frame should find this caveat attached to it. **`A-125`.**

⚠ **The dates also correct the audio, mildly.** `[00:13:46]` says *"Last week of March \| Going into
April"*; the legible rows are `2012.03.25`–`2012.03.26`, i.e. the last week of March, and no April
row is legible at this resolution. And the three growth figures he gives — *"double this demo"*,
*"about 50% a week"*, *"33% over three weeks"* `[00:13:49]`–`[00:13:56]` — **are mutually
inconsistent** (doubling is +100%; 50%/week compounded over three weeks is +238%; 33% over three
weeks is neither). **`C-026`, low-stakes**, recorded because no artifact depends on it and because
V17 contains two independent arithmetic slips (`§9a` is the other).

---

---

## §14 — ⭐ THE SLIDE IS EDITED LIVE, ON CAMERA `[VISUAL+AUDIO]`

`V17_00-45-05_powerpoint-editor-open-news-is-used-caret.png`.

At burned `42:10` and `43:20` the Day-1 slide reads **`News Is Use To Perpetuate False Trend`**. At
`[00:44:56]` he says *"you're gonna laugh at me, but I got a correct. it's gonna drive me insane for
the rest of my life **the news is used**"*, and at burned `45:05` **the PowerPoint editor is open on
that slide with the text cursor sitting immediately after `News Is Used`.**

⚠⚠ **THIS IS A PROVENANCE FINDING, NOT AN ANECDOTE.** **The course deck is mutable and was being
mutated during the recorded session.** Any downstream claim of the form *"the slide says X"* is a
claim about **the deck as it stood at that timecode**, not about a stable artifact. The corrected
slide is **never shown again in slideshow mode in this file**, so V17 contains the typo, the
correction, and no image of the corrected slide. `A-124`.

---

## §15 — VOCABULARY: WHAT ARRIVES, WHAT STAYS UNDEFINED

### ⭐ Arrives, with support

| Term | Status |
|---|---|
| **`Mayo`, `Blue Berry`** | ⭐⭐ **PRINTED TWICE** — `(Mayo ,Blue Berry)` on the `00:51:00` slide and `Pins to the Blueberry & Mayo` on the `00:14:15` flashcard. **`A-020`'s nickname set gains printed corroboration for the first time.** ⚠ **The mapping to periods is NOT printed here** — V09 established `blueberry = 800 (15-min)`; V17 adds only that both are *"chart landmarks"* where retail orders build |
| **`ketchup` / `mustard`** | ⭐ **PRINTED** on the `00:20:30` answers slide (*"a close above the ketchup and mustard"*). First printed instance in the corpus. ⚠ **Still unmapped to periods** |
| **`Big Board`** | ⭐ **DEFINED** — *"all price action with the high and low"*, opened with `F10`. `A-111` |
| **`W` in the closing of price** | ⭐ **NEW** — `A-011` amended |
| **`≥ 8 candles`** | ⭐ **NEW** — `A-010` amended |
| **`50/200`** | ⭐ **PRINTED**, correcting the ASR's `5200` |
| **`Y-LOD`** | printed abbreviation for *yesterday's low of day* |
| **`PFL`** | printed abbreviation for *peak formation low* — first printed expansion |
| **`BO Traders` / `200 Traders`** | printed — *breakout traders* and *traders trading the 200* |
| **`trend reset`** | ⭐ **NEW CONCEPT**, printed and contrasted with reversal — `§12` |
| **`reversal day`** | ⭐ **NEW** — Day 1 of the cycle, `[00:43:09]` |
| **`vector candle`** | used at `[00:48:22]`, **never defined** |

### ⚠ Still undefined after seventeen lessons

`M` / `W` depth and tolerance · `peak formation`'s formal test · `level one/two/three` ·
`level three week` (`A-118`) · `aggressively` (`A-120`) · `RR` (`A-114`) · `vector candle` ·
`shark fin`'s TDI threshold (`A-084`-blocked) · `blown out` bar (`A-115`) ·
*"nearly filled (close enough)"* ADR (`A-113`) · the timezone on every clock time in the corpus.

---

## §16 — WHAT THIS LESSON DOES **NOT** SUPPLY, AND ABSENCE IS EVIDENCE

Machine-counted on the committed 690-marker transcript:

| Term | Count |
|---|---|
| `5/13` | **0** |
| `800` | **0** |
| `Asian box` | **0** |
| `M15` | **0** |
| `10 to 15` / `10-15` | **0** |
| `EMA` | 4 (all *"20 EMA"* or *"moving average"* glosses) |
| `stop loss` | 4 — and **not one** is a distance except the garbled `[00:53:42]` |

**No position size. No account risk %. No stated `R:R`. No take-profit rule other than
*"consolidation TP"*. No indicator properties dialog in 694 frames — 3,908 across V12–V17.**
`A-084` stays blocked, and this session did **not** hunt for it.

⭐ **And the zeroes are load-bearing:** `5/13`, `800`, `Asian box` and `M15` are precisely the terms
the quarantined `RULES.md` / `VISUAL_INDEX.md` assert as **explicit instructor statements with
timestamps**. See `QUARANTINE_REGISTER.md` **Q-018**.
