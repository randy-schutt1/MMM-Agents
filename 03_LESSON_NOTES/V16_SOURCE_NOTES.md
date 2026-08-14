# V16 — SOURCE NOTES

**Source:** `Bootcamp1 Wk7 050612 Part2 (45mins).swf` · V16 · 2012-05-06 · 00:44:35
**Timestamp convention:** the committed marker grid of `02_TRANSCRIPTS/V16/V16_TRANSCRIPT.md`,
stated once at the top of that file and used unchanged here. Slide timings are the burned-in
player timecode, which is **the same clock** — measured to **zero offset** at ten points this
session, not assumed (`04_SCREENSHOTS/V16/INDEX.md` §0).

---

## §0 — DECLARED DEVIATIONS, READ THIS FIRST

**`D1` — the `SWF_CAPTURE_RECIPE.md` §9 ordering was broken the same way V13, V14 and V15 broke
it, and it is disclosed here rather than in a footnote.**

§9 requires source notes to be written **from the transcript alone**, before any frame is opened.
This session read the full 377-marker transcript first, but then ran screen detection and **opened
frames before writing this file**. So §9's ordering is broken.

**The mitigation, and it is falsifiable by `grep`:** every numbered item below carries **`[AUDIO]`**,
**`[PRINTED]`**, **`[AUDIO+PRINTED]`** or **`[VISUAL]`**. Any reader can check an `[AUDIO]` tag by
searching the transcript for the quoted words, and a `[PRINTED]`/`[VISUAL]` tag by opening the
named PNG. **Nothing tagged `[AUDIO]` depends on a frame.** Strike every non-`[AUDIO]` row and the
lesson's spine survives, because this lesson is unusually well printed.

**`D2` — the deviations that MATTER here are the other way round: three conclusions rest on frames
and are named so a reader can discount them.**

| # | Conclusion | Rests on |
|---|---|---|
| `D2a` | The printed pivot-grid **ordering** `R2 · M4 · R1 · M3 · CPP · M2 · S1 · M1 · S2` (§2) | `[VISUAL]` only — the audio never enumerates it |
| `D2b` | The **London session start `2:00 To 3:00 AM, EST`** (§9) | `[PRINTED]` only — the audio at that moment is the ASR-damaged *"At the moment open"* |
| `D2c` | The **equal pixel spacing** of the nine grid levels, which is what DEFEATS the midpoint reading (§2b) | `[VISUAL]`, measured; see the numbers, not the impression |

**`D3` — NO FORWARD READ WAS PERFORMED, and no backward read beyond committed files.**
`REVIEW_INDEX.md` item **179** (the forward-read precedent) is still unsettled and its clause (d)
binds. This session did **not** open V17 or any later file. V15's committed artifacts *were* read —
that is a **backward** read into a file on this branch's own history, which needs no precedent, and
is the move item 190 recommended.

**`D4` — the frame sweep did NOT follow `SWF_CAPTURE_RECIPE.md` §10's script literally, and the
deviation is the reason §8a's offset came out at zero.** See `04_SCREENSHOTS/V16/INDEX.md` §0.2.
It is reported as a deviation, not as a compliant run, and **no edit was made to the recipe file** —
that is a policy ledger and `D-038a` puts it on the integration branch (open item **197**).

---

## §1 — WHAT THIS LESSON IS `[AUDIO+PRINTED]`

**One sentence:** a single-topic lesson on **floor-trader pivot points — how they are constructed,
what the `M1`–`M4` labels on the instructor's grid mean, how a daily candle's COLOUR selects which
pair of levels is the day's projected high and low, and how that fixed grid is coupled with the
floating ADR markers V15 taught to produce a projected high and low for tomorrow.**

**It is Part 2 of the same recording as V15 and it opens mid-sentence** `[AUDIO]`: `[00:00:00]`
*"pivot points. Okay, how can you project the high and low and have a rough idea"*. There is **no
greeting, no title read and no re-introduction** — the title slide is already on screen when the
file starts (`V16_00-00-20_…png`). V15 `[00:35:00]` had promised *"I'm going to tie pivots in the
blue tracer into it in a minute."* **This is that minute.**

**The lesson has a printed topic title, which is rare in this corpus** `[PRINTED]`: `Pivot Points`,
over three sub-lines — *"How to Project High and Low"*, *"Intra-Day Support and Resistance"*,
*"Possible Trading Range"* (`V16_00-00-20_…png`). Every slide up to `00:34:55` carries `Pivot
Points` as a running head.

**Structure, by the clock:**

| Span | Content | Screen |
|---|---|---|
| `[00:00:00]`–`[00:00:44]` | Title and purpose | title slide |
| `[00:00:45]`–`[00:01:34]` | **The four printed rules** (§3) | bullets slide |
| `[00:01:35]`–`[00:14:20]` | ⭐ **THE WHITEBOARD HOUR** — one static slide, annotated live for thirteen minutes: the dealer's pip allotment, the intraday cycle, the three-day cycle, the fourth-day flip | pivot-grid diagram |
| `[00:14:25]`–`[00:17:50]` | The London-open read, then the grid on a real price scale | session slide, then charts |
| `[00:17:53]`–`[00:19:55]` | **The HOD/LOD rule, printed** (§2) | bullets slide |
| `[00:20:00]`–`[00:27:35]` | Five worked chart examples: `M1/M3` day, `M2/M4` day, a level-3 day, an `M4` open, an outside-ADR day | annotated charts |
| `[00:27:36]`–`[00:29:05]` | ⭐ **PIVOTS × ADR — the confluence claim, printed** (§7) | bullets slide |
| `[00:29:06]`–`[00:34:55]` | When pivots fail, *"YOU are the filter"*, and the wrong-segment rule (§8) | bullets slide + 3 charts |
| `[00:35:00]`–`[00:39:50]` | **Homework**, then the course calendar to Labor Day (§11, §12) | `R&D` slide, roll-call slide |
| `[00:39:55]`–`[00:44:30]` | Q&A and sign-off | *"Good night"* slide, then back to the roll-call |

⚠ **THIS FILE ENDS THE SESSION.** `[00:44:30]` *"It works. Daniel, thank you. You guys have a good
night, man. Always enjoy this time together."* Unlike V08, nothing is announced-and-missing.

---

## §2 — THE PIVOT GRID: WHAT `M1`–`M4` ACTUALLY ARE `[PRINTED]` `[VISUAL]`

⭐⭐ **THIS IS THE LESSON'S SINGLE MOST IMPORTANT CONTRIBUTION AND IT ANSWERS `A-096` DIRECTLY.**
`A-096` was opened by V15 as *"`S1`/`R1`/`M1`–`M4` are PIVOT levels, not M-formations — DECODED
from the frames, DEFINED only at Tier 2."* **V16 prints the whole grid in Tier 1.**

The diagram on `V16_00-01-40_…png` (clean at sweep `i=19`, before annotation) shows a single
vertical bar with nine labelled levels. Reading top to bottom `[VISUAL]`:

```text
        R2        <- resistance 2
        M4
        R1        <- resistance 1
        M3
        CPP       <- central pivot point   (printed "CPP", spoken "central pivot point")
        M2
        S1        <- support 1
        M1
        S2        <- support 2
```

**So `M1`–`M4` are the instructor's own INTERSTITIAL levels, interleaved between the standard
floor-trader pivots.** The legend on the same slide prints the colour semantics
`OVER BOUGHT` (red) · `SHADES OF GREY` (grey) · `OVER SOLD` (green), and, bottom-right,
`PRICE AT LONDON OPEN` with a red capsule → `SELL` and a green capsule → `BUY`.

The ordering is corroborated in spoken audio, though never enumerated `[AUDIO]`:
`[00:17:53]`–`[00:18:19]` *"it's that M3 and M4 \| are possible day highs. They are located above the
central pivot point. All right? Central pivot point, \| yellow, M3 above, M4 above, M1 and M2 are
below the central pivot point and they're possible \| low projections."* — and printed on the following slide
(`V16_00-18-00_…png`) as:

> *"M3 And M4 Are Possible HODs · They Are Located Above The CP"*
> *"M1 And M2 Are Possible LOD's · They Are Located Below The CP"*
> *"Subtract The Value Of Today's Projection And This Is The Trading Range · Ex: ( M1 – M3)"*

### §2b — ⛔ THE CONSTRUCTION OF `M1`–`M4` IS **NOT** GIVEN, AND THE DIAGRAM CANNOT SUPPLY IT

The obvious reading — *"`M3` is the midpoint of `CPP` and `R1`, `M4` the midpoint of `R1` and
`R2`"* — is **consistent with the ordering and is NOT established by it**, and this session tested
the one piece of evidence that could have settled it rather than asserting the tidy answer.

**Measured, on the clean unannotated frame (sweep `i=19`), the y-pixel centres of the nine level
labels:**

```text
235 · 288 · 340 · 393 · 446 · 497 · 549.5 · 602.5
deltas: 53 · 52 · 53 · 53 · 51 · 52.5 · 53      (mean 52.5, spread ±1)
```

**All nine levels are EQUALLY SPACED to within one pixel.** Under any standard floor-trader pivot
formula the gap `R1→R2` is **not** generally equal to the gap `CPP→R1`. **Therefore the diagram is
a SCHEMATIC, not a scale drawing, and no arithmetic construction of `M1`–`M4` can be read off it.**

⛔ **`M1`–`M4` REMAIN `DO NOT CODE`.** The corpus now knows their **order** and their **role**; it
still does not know their **formula**. Filed as **`A-101`**. The midpoint hypothesis is recorded
there as a hypothesis with its defeater attached, and is **not adopted**.

---

## §3 — THE CANDLE-COLOUR RULE `[AUDIO+PRINTED]`

**Printed, on the second slide** (`V16_00-00-50_…png`), four bullets, complete:

> * *"Calculated on Daily Candles"*
> * *"Yesterday's Price Action Gives Tomorrow's Pivot Points"*
> * *"Red Candle Indicates M1/M3 Day"*
> * *"Green Candle Indicates M2/M4 Day"*

**Spoken, twice** `[AUDIO]`:
`[00:00:59]` *"if yesterday's candle was red then it's understood that you're in a downtrend but we
know a little better about the cycle. So the projection would come in as an M1 M3 day. If the daily
candles green were in an uptrend we expect price to come into M2 M4."*
`[00:14:50]`–`[00:15:11]` *"So if you understand that those are M1M3 is projected range \| when the
daily candle closes red. Okay? When the daily candle closes green, the projections are \| that price
will move between the M2 and M4 grid."*

**And annotated live on the session slide** `[VISUAL]` (`V16_00-15-00_…png`): hand-written
`M1/M3 DOWN DAY` in red beside the red `SELL` capsule and `M2/M4 UP DAY` in green beside the green
`BUY` capsule.

⭐ **This is the most completely-specified rule in the lesson: printed, spoken twice, and drawn
once.** It is also **mechanically checkable** — it takes one candle's colour and returns a pair of
level names.

⚠ **What it still does not fix:** *which* daily candle, on *whose* clock. See §9's midnight
question and `C-023`.

---

## §4 — THE DEALER'S PIP ALLOTMENT — THE WHITEBOARD HOUR `[AUDIO]` + `[VISUAL]`

Thirteen minutes on one static slide, drawn over live. The screen-state detector found **no slide
change between `01:35` and `14:25`**, which is itself the evidence that this is one continuous
argument.

**The premise, first person, in the dealer's voice** `[00:01:27]`–`[00:01:40]`:
> *"Understand I'm a dealer. I have a hundred pips to work with. Right? Of my hundred pips, how
> will I allot those pips?"*

**The split** `[00:01:59]`–`[00:02:21]`:
> *"So what am I going to do with those hundred pips? I'm going to use 25% of them or in this
> example 25 pips to hit the stops and fake traders out. 75% of what's left for me to work. I'm
> going to use to make my trend run and then I'm going to end off with a higher low and close the
> day."*

**The 25% is applied to a named object** `[00:02:59]`–`[00:03:17]`:
> *"Now this move I took the top of the Asian range and I exceeded it by 25 pips. Okay, I cut the
> Asian high by 25 pips because I want to save my 75 to get everybody out."*

**The narrated day, in order** `[AUDIO]`, `[00:02:29]`–`[00:05:04]`:

| Step | Verbatim |
|---|---|
| 1 | *"the central pivot point price comes out and forms the Asian range right at the central pivot point"* |
| 2 | *"At 1 o'clock or 2 o'clock or 3 o'clock depending on when I feel like it because I'm a dealer I can do what I want. I decide that I'm going to trigger the stops and pick up the breakout traders by widening the swing"* |
| 3 | *"breaking to the upside and going somewhere around the M3 number and making my M formation"* |
| 4 | *"My downside target is the M1 pivot"* |
| 5 | *"get the stops, get the stops drop level 1 is formed I'm in level 2"* |
| 6 | *"maybe I go to lunch mid session. I come back I show some consolidation… I just kind of drift down and make level 3"* |
| 7 | *"There's been three intraday pushes. I've made my trap move to end the day."* |
| 8 | *"I closed the session strong by making my W formation to end the day and I pass it off to the US guy and he takes it back into the range and consolidates"* |
| 9 | *"I decide I'm going to go ahead and consolidate right around level 2 to make up some fake support and resistance for everybody on the chart. So when they draw their line tomorrow I could just laugh at them."* |

⚠ **THE `25` AND THE `100` ARE EXAMPLE VALUES, AND HE SAYS SO** — *"or in this example 25 pips"*.
They are **`A-082`-class figures** and are fenced out of every spec file. See §10.

⚠ **STEP 2 IS THE CLOSEST THING TO A SESSION CLOCK IN THE AUDIO, AND IT IS DELIBERATELY VAGUE:**
*"1 o'clock or 2 o'clock or 3 o'clock depending on when I feel like it"*. **No timezone.** The
printed slide at `14:25` gives a different and narrower window (§9) — recorded, not reconciled.

---

## §5 — THE THREE-DAY CYCLE AND THE FOURTH-DAY FLIP `[AUDIO]`

**The claim** `[00:12:30]`: *"So in a three-day cycle, the pivot points will be accurate."*
**The failure mode** `[00:12:51]`–`[00:12:58]`: *"So for a couple of days during the cycle, \| the
pivot will be at a whack"* (ASR; *"out of whack"*).

**The rule** `[00:13:14]`–`[00:13:32]`:
> *"going into the end of the week, the dealer will reverse. Okay? So if we know ahead of everyone
> else, that the dealer will probably reverse, then we simply adjust the pivot points to the next
> day ahead of everybody else, M2M4 projections."*

**Stated again with the direction made explicit** `[00:15:11]`–`[00:15:36]`:
> *"the fourth day of the cycle in a downtrend, the dealer issues the W, M2M4 is your projection.
> The fourth day in an uptrend, the dealer issues an M4, the projection goes back to M1M3."*

**And a third time as the takeaway** `[00:31:32]`–`[00:31:48]`:
> *"Remember that during the cycle, because the dealers make three red candles or three ring
> \[green\] candles, that the fourth day, the pivot will be off. So take away from that on the
> fourth day, use the next offset of pivots for the projections. I can't say this enough."*

⭐ **This is the lesson's one genuinely COMPOUND rule** — it composes §3's colour rule with a
day-count, and it **inverts** §3 on day 4. It is stated three times and is internally consistent
on all three.

⚠ **`[00:15:36]` says *"the dealer issues an M4"* where the parallel construction wants *"an M"*.**
Recorded as a probable ASR artefact and **not** relied on; the direction is fixed by the surrounding
clause either way.

⚠ **WHAT IS UNDEFINED AND BLOCKS IMPLEMENTATION:** *"the cycle"* has no start rule here. Day 1 of
a three-day cycle is not identified by any test given in this file. `A-010`/`A-011`'s peak-formation
question is the same question wearing a different hat, and it is **not** answered here.

---

## §6 — ⭐⭐ THE ADR LOOKBACK ARRIVES `[AUDIO]`

**`COURSE_PROGRESS.md`'s V16 GATE (c) named this as *"the highest-value thing V16 could contain."*
It contains it.** `A-100` was opened one lesson ago on the finding that the ADR is taught for a
whole lesson and *"its LOOKBACK is never stated: the corpus cannot compute the object it teaches."*

**Verbatim, `[00:09:31]`, course author, Tier 1:**

> *"the ADR is calculated over the last two weeks, 15 days."*

**Immediately corroborated by its own consequence** `[00:09:37]`:
> *"We have an average of what prices moved over the last two weeks. The ranges will tighten up when
> the market is quiet. The ranges will expand when the market is more volatile because it's an
> average. We're averaging what the move is."*

⭐ **This CORROBORATES the Tier 2 figure V15 could only cite at Tier 2** (*"the last 2 weeks"*), and
it **adds a day count Tier 2 did not have.**

### ⚠ AND IT ARRIVES CARRYING ITS OWN DEFECT, WHICH IS RECORDED RATHER THAN SMOOTHED

**`"two weeks"` and `"15 days"` are not the same number on any convention this corpus uses:**

| Reading | Value |
|---|---|
| Two weeks of *trading* days (Mon–Fri) | **10** |
| Two *calendar* weeks | **14** |
| Two weeks of forex sessions (Sun 22:00 open → Fri close) | **10** |
| Stated | **15** |

**No reading yields 15.** Nothing in the file resolves it, and **it is not this session's job to
pick one.** `A-100` is **ADVANCED, NOT CLOSED**, and the reason it cannot close is now a *different*
and *smaller* reason than it was: not *"no number exists"* but *"two numbers exist and they
disagree by up to 50%."*

**What is STILL missing for the ADR to be computable, unchanged from `A-100`:**

1. What *"range"* means per day — high−low of the day? Of the body? On which timeframe?
2. The **day boundary** for the ADR. `[00:40:27]` gives *"midnight to midnight"* — **for PIVOTS.**
   It is **not** stated of the ADR, and §9's `C-023` shows the speaker does not hold that boundary
   firmly even for pivots. **Transplanting it onto the ADR would be exactly the `A-082` error.**
3. Whether the average is simple or weighted.
4. `C-022`'s repaint conflict, opened by V15, **is not touched here.** V16 never says the word.

---

## §7 — PIVOTS × ADR: THE CONFLUENCE CLAIM `[AUDIO+PRINTED]`

**Printed** (`V16_00-27-45_…png`), and this is the join V15 was building toward:

> * *"PP Are An ADR Grid, The Extremes Are Representative Of ADR High /Low."*
> * *"Since The Grid Is Fixed, And Trading Ranges Are Not, We Couple Pivots With ADR Markers For
>   Strong Confirmations"*

**Spoken** `[00:27:36]`–`[00:28:06]`:
> *"Pivot points are essentially if you haven't figured out. They're an ADR grid that's fixed. The
> extremes of the pivot pivot grid represent the ADR high and low in essence. So M1 and ADR line
> line up or M3 or M4 and the ADR high line up. That's given you the floating grid and the fixed
> grid coming together. That's a pretty good area for an M or W to \[form\]."*

**And the third leg, added out loud** `[00:28:25]`–`[00:28:48]`:
> *"Couple it with ADR high or low. It's an M1 or M2 and ADR lows lay in there. And if you happen
> to see off in the distance right around slightly below M1 a big fat blueberry line line there.
> I'm pretty sure a price will go there or false just short of it for fake."*

⭐ **THE FOUR-PART CONFLUENCE V15 §12 DESCRIBED IS NOW COMPLETE ACROSS THE TWO FILES:**
pivot level · ADR marker · a moving average (*"blueberry"*) · an `M`/`W` pattern at that location.

⛔ **AND IT IS STILL NOT CODEABLE, FOR REASONS THAT ARE NOW ENUMERATED RATHER THAN VAGUE:**

| Leg | Blocker |
|---|---|
| Pivot level | `A-101` — `M1`–`M4` construction unstated (§2b) |
| ADR marker | `A-100` — lookback now `10 or 14 or 15`, range definition and day boundary still absent; `C-022` repaint conflict open |
| *"blueberry"* | `A-020` — nickname carries **no period** here either. `[00:28:34]` and `[00:28:53]` are the only two occurrences and neither attaches a number |
| *"line up"* | ⛔ **UNQUANTIFIED.** *"line up"*, *"lay in there"*, *"slightly below"* — no tolerance is stated anywhere. Filed as **`A-102`** |

---

## §8 — WHEN PIVOTS FAIL, AND THE ESCAPE RULE `[AUDIO+PRINTED]`

**Printed** (`V16_00-29-10_…png`):
> * *"Pivots Are Intraday Support And Resistance"*
> * *"A Break Of One Level Is Almost Always Certain To Give Way To The Next Pivot Level"*
> * *"YOU Are The Filter!"*
> * *"Identify The Market Condition And Candle Pattern For Next Level Support /Resistance"*

**Printed** (`V16_00-32-05_…png`):
> * *"Big Market Moves Will Often Disrupt The Pivot Points For The Following Trade Session"*
> * *"In Order To Find Opportunity, We Must Set Some Rules For Trading When Price Comes Out At The
>   Wrong Segment Of The Trading Zone…."*
> * *"Ignore The Pivots and Identify the Pattern"*

**The escape rule, spoken, and it is the whole of it** `[00:33:43]`–`[00:33:58]`:
> *"In order to find opportunity, you got to set some rules for trading when the price comes out of
> the wrong segment of the trading zone. You know what the rule is? Ignore the pivots and identify
> what I've taught you, the pattern, the pattern, that's the answer."*

⭐ **This is unusually candid and it is the honest reading of the whole lesson: the pivot grid is a
LOCATION HINT, and the pattern is the trigger.** `[00:32:08]` *"You, my friend, are the filter.
You're the filter."*

**The disruption cause is given concretely** `[00:32:55]`–`[00:33:17]`:
> *"the pivots are messed up because there was a 250-pit \[pip\] move yesterday… if there's a
> 250-pit move on Tuesday, Wednesday's pivots will be based on the open high, low close of
> Tuesday's price."*

⚠ **`"the wrong segment"` IS NEVER DEFINED.** The three charts that follow (`34:10`, `34:30`,
`34:50`) show it rather than say it, captioned `Price in wrong Segment M is clearly visible….Sell`
and `Straight Away….Sell` `[PRINTED]`. Filed as **`A-103`**.

---

## §9 — ⭐ THE LONDON-OPEN READ, AND THE MIDNIGHT QUESTION

### §9a — A PRINTED SESSION CLOCK TIME `[PRINTED]`

`V16_00-14-25_…png` is a full slide carrying nothing but:

> **`London Session Start`**
> **`2:00 To 3:00 AM, EST`**
> red capsule → **`SELL`** · green capsule → **`BUY`**

⭐ **THIS MATTERS OUT OF PROPORTION TO ITS SIZE.** V10's source notes carry the finding, corrected
under open item 93, that clock times occur in this corpus but **none delimits a session**. **This
one does, in print, unambiguously, with a timezone.** It is the second printed session clock in the
corpus after V06's `3:45am or 9:45am est.` (V06 R1 item 57).

**The rule it carries** `[AUDIO]`, `[00:14:23]`, ASR-damaged and quoted verbatim:
> *"At the moment open, if the dealer breaks high, then the top, upside of the pivot grid, you're a
> seller. If the dealer breaks low, at the bottom side of the pivot grid, if he hits M1, gives you
> a nice setup, if he hits M2, he gives you a nice setup."*

⭐⭐ **ARBITRATED AND CONFIRMED.** *"At the moment open"* is **`"At the London Open"`** — ASR
correction **#1**, `V16_TRANSCRIPT.md` §5, resolved by an independent `large-v3-turbo` pass which
reads *"I'm getting ahead of myself. **At the London Open**, if the dealer breaks high in the top
side of the pivot grid, you're a seller."* The same pass corrects a **second** garbled *"London
Open"* at `[00:05:24]` (correction #7). **So the rule has an AUDIO leg, a PRINTED slide two seconds
later, and the grid slide's own `PRICE AT LONDON OPEN` legend — three independent supports.**
⚠ **`A-105`'s `EST`/`EDT` hour is untouched by this.**

### §9b — MIDNIGHT TO MIDNIGHT, AND THE CONTRADICTION FORTY SECONDS LATER `[AUDIO]`

⭐⭐ **AND THE STUDENT ASKED IT AS A CHALLENGE — the committed ASR obscured that, and the
independent pass restored it** (correction **#6**). The committed text renders the question as two
unrelated sentences; the second pass renders it as one:

> `[00:40:07]`–`[00:40:16]` *"Steve, **why are you stating the London session started on your slide
> when it's the daily candle that we were looking at?**"*

**The student is pointing at the inconsistency directly.** That makes the answer below a
considered reply rather than an aside.

`[00:40:22]`–`[00:40:34]`:
> *"I wanted the pivot points of price action to be as fresh as possible right before we trade. So
> we calculate our pivot points from midnight to midnight. I know they're based on the daily candle,
> **but they're based on price action from the 24 hour period from midnight to midnight.**"*

**Forty seconds later, asked the same thing by a second student, he answers the other way**
`[00:41:09]`–`[00:41:18]`:
> *"Reese, when we calculate pivot points from the open high, low close from midnight, time to
> midnight, **no, just do it on the daily candle for right now.** You don't have to get all
> technical. I just want you to understand what you're doing."*

**These give different numbers whenever the broker's daily candle does not run midnight-to-midnight,
which is the normal case** — and no timezone is attached to *"midnight"* anywhere in the file.
Filed as **`C-023`**, with the mitigation recorded in the record itself: **he flags the second
answer as a simplification (*"for right now"*, *"you don't have to get all technical"*), which is
why it is a weak contradiction rather than a strong one — but it is still two different
computations and nothing says which is normative.**

---

## §10 — THE PIP FIGURES: FIVE OF THEM, IN ONE LESSON `[AUDIO]`

⚠ **`A-095` is the `A-082`-class record for *"pip figures stated as fact with no instrument and no
period."* V16 states FIVE, and three of them are stated as facts about the world rather than as
example values.**

| # | Marker | Verbatim | Kind |
|---|---|---|---|
| 1 | `[00:01:27]` | *"I have a hundred pips to work with"* | **example**, flagged as such at `[00:02:05]` |
| 2 | `[00:06:02]`–`[00:06:15]` | *"I know that there's about \| 120 pips ADR"* | worked example on an unnamed pair |
| 3 | `[00:16:59]` | *"about 150 pips. Okay? So there's 150 pips possible for the day"* | worked example, `EJ` |
| 4 | `[00:22:44]`–`[00:22:50]` | *"approximately what? 200 pips in every pair except GJ and some of the crosses"* | ⚠ **stated as FACT, with a named exception** |
| 5 | `[00:30:12]` | *"these guys are told **do not exceed 200 pips** on the average day"* | ⚠ **stated as an externally-imposed LIMIT** |

⭐ **#4 and #5 are the corpus's first ADR figure with an INSTRUMENT SCOPE attached** — *"every pair
except GJ and some of the crosses"*. That is still not an instrument list, but it is not nothing,
and it is the thing `A-095` says is always missing. **Logged in `A-095`; NOT promoted to a
parameter.**

### ⚠ AND THE `600–1000` WEEK IS RESTATED, FOR THE SECOND TIME `[AUDIO]`

`[00:23:24]`:
> *"it always comes back within a range within a **600 to 1000 pips range for the week** or within a
> reasonable amount of pips for the cycle"*

**`BT_V10_0001` CONTRADICTED this figure AS STATED: 0 of 180 weeks, median 243.8 pips.**
**`COURSE_PROGRESS.md`'s V16 GATE (e) rules on exactly this case: log it as DURABILITY evidence in
`A-095`, DO NOT re-test it (`D-027`). That is what was done — it was NOT re-tested.** Its value is
that the figure is *durable* across four lessons and two years of the instructor's own examples,
which makes the measured refutation more interesting, not less.

---

## §11 — THE HOMEWORK, AS ASSIGNED `[AUDIO+PRINTED]`

**Printed** (`V16_00-35-05_…png`), under an `R&D` heading:
> *"Find the Expected High/Low for the day on the 6 majors, using Pivot calculations."*
> *"Do it pre London for Mon & Tues"*

**Spoken, with the tool named** `[00:35:03]`–`[00:35:36]`:
> *"Find the expected high and low for the day on six majors using pivot calculations. Do it free
> \[pre\] London from Monday and Tuesday. So tomorrow night, Monday night and Tuesday night, go to
> **mypivotcalculator.com**, take the daily candle, take the open high, low close, calculate the
> values, post them in the forum for me to see. Okay? Do the six majors for two nights, that's all."*

**And the reason** `[00:35:36]`:
> *"I know the indicator does it for you, but I want you to understand what you're doing."*

**The six majors, enumerated on request** `[00:40:52]`–`[00:41:02]`:
> *"Javan, here you go. Pound dollar, Euro dollar. Dollar yen. Dollar Swissy. Australian. Canadian.
> … It's actually four majors in due \[and two\] commodity crosses if you want to get technical."*

⭐ **This is the first homework in the corpus that is fully specified: the instrument list is
enumerated, the input is named (daily OHLC), the tool is named, the output format is named (post
in the forum) and the schedule is named (two nights, pre-London).** It is done in
`05_HOMEWORK/V16/`.

**The standing roll-call, printed** (`V16_00-36-35_…png`), under `Market Maker Boot Camp`:
> *`R& D` · `Continue with your flash cards` · `TDI only trades` · `Big board only entries` ·
> `Moving Avg Only Trades` · `Estimate the High and Low using pivots`*

⚠ **The audio says *"big board only trades"* `[00:38:06]` where the slide prints *"Big board only
entries"*.** Recorded, not reconciled; it is the fifth item of a five-item drill list this corpus
has now seen twice (V15 §3 carries the same list).

---

## §12 — THE COURSE CALENDAR, EXTENDED PAST THE BOOTCAMP `[AUDIO]`

V15 gave the calendar to `June 17`. **V16 gives it to Thanksgiving, and it is first-person
throughout** (speaker strand 3):

| When | What | Marker |
|---|---|---|
| *"a couple of weeks left"* | of bootcamp | `[00:36:34]` |
| at the end | *"I'm going to leave the bootcamp recordings up"* | `[00:36:50]` |
| after | *"I'm going to teach a couple of classes"* (the web class and the live class V15 dated) | `[00:36:59]`, `[00:38:46]` |
| summer | *"I'm going to take two months off… I will be in a bathing suit"* | `[00:36:59]`, `[00:37:09]` |
| **after Labor Day** | *"I'll start another bootcamp cycle"* — *"probably September, October, and maybe end right before Thanksgiving"* | `[00:37:41]`, `[00:38:57]` |

⭐ **`"a couple of weeks left"` is consistent with V15's *"about two or three more weeks… we're
going to wind up around 10 or 11 weeks"`, and with `SOURCE_MANIFEST.md`'s last file being
`Wk10 061712`.** Three independent statements, two lessons apart, agreeing.

⚠ **AND IT CREATES A NEW, ANSWERABLE QUESTION THIS CORPUS CANNOT ANSWER:** a **second bootcamp
cycle** was planned for autumn 2012. Nothing in this library is from it. Recorded in `A-104` as an
out-of-corpus dependency of the `A-042` kind — **not** as a gap in this corpus.

---

## §13 — VOCABULARY: WHAT ARRIVES, WHAT STAYS UNDEFINED

| Term | Status after V16 |
|---|---|
| ⭐ `CPP` / *"central pivot point"* | **PRINTED AND SPOKEN.** Standard floor-trader central pivot; position in the grid printed (§2) |
| ⭐ `M1`–`M4` | **ORDER and ROLE settled** (§2). **Construction still absent** → `A-101` |
| ⭐ ADR lookback | **STATED**: *"the last two weeks, 15 days"* → `A-100` **ADVANCED, NOT CLOSED** (§6) |
| *"the wrong segment"* | ⛔ shown, never defined → `A-103` |
| *"line up"* / *"lay in there"* | ⛔ no tolerance → `A-102` |
| *"33 trade"* | ⚠ **occurs TWICE and is still not defined** — `[00:09:06]` *"perhaps on the last leg, you get a 33 trade"*, `[00:09:57]` *"you got your 33 trade inside of a daily candle"`. `A-097` is **CORROBORATED, NOT RESOLVED**: V16 confirms the term is real and intraday and late-in-the-move, and defines nothing. The *"22-trade"* half of `A-097` gets **zero** help — the token does not occur |
| *"half a batman"* | `[00:26:39]`, `[00:27:31]` — **corroborates V05's printed *"1/2 Batman"***. Still undefined |
| *"blueberry"* | `[00:28:34]`, `[00:28:53]` — a *"big fat blueberry line"* slightly below `M1`. **No period attached.** `A-020` extended, still `DO NOT CODE` |
| *"level 1 / 2 / 3"* | used freely `[00:04:09]`, `[00:25:07]`; never defined here |
| `M5` | ⚠⚠ `[00:33:24]`–`[00:33:30]`. Corrected to *"the M&W might form an M5, **oh, Steve**, it wasn't M4, M3, it was M5"* (correction **#3**) — *"Most of you"* was a student's voice. ⭐ **`M5` SURVIVES BOTH ASR ENGINES, TWICE IN ONE SENTENCE, and there is NO `M5` on the printed nine-level grid.** Either the live grid carries levels the slide does not, or he misspoke twice. **Nothing in the file decides it.** Recorded in `A-101` |
| *"stop loss"* | **ZERO occurrences**, as in V10. Absence is evidence |
| *"Asian box"* | **ZERO occurrences.** *"Asian range"* occurs twice. ⚠ This falsifies the quarantined `NOTES.md`/`RULES.md` directly (`Q-017`) |
| *"shark"* / *"63"* | **ZERO occurrences.** `A-084`'s open item 157 gets **no help**, as expected |

---

## §14 — WHAT THIS LESSON DOES NOT SUPPLY, AND ABSENCE IS EVIDENCE

1. **NO STOP LOSS.** *"stop loss"* occurs **0** times in 6,453 words. The quarantined `RULES.md`
   asserts a *"10 to 15 pips beyond the High or Low of the Day"* stop at `[00:18:00]`; the real
   `[00:18:01]` is *"are possible day highs."* (`Q-017`).
2. **NO POSITION SIZE, NO R:R, NO TARGET IN PIPS** for the trade the lesson implies.
3. **NO ENTRY TRIGGER OF ITS OWN.** The lesson explicitly delegates it — *"identify what I've
   taught you, the pattern"* (§8).
4. **NO `M`/`W` DEFINITION.** Used ~9 times, defined never; `A-010`/`A-011` unmoved.
5. **NO CYCLE-START TEST** (§5).
6. **NO TIMEZONE ON *"midnight"*** (§9b).
7. **NO PROPERTIES DIALOG, NO NAVIGATOR, NO INPUTS TAB** in any of the **544** sweep frames —
   the fourth consecutive lesson to return that negative, now **3,214** frames across V12–V16.
   `A-084` stays blocked; V15's item 187 reading (that the setup content was scheduled *outside*
   the bootcamp) is **neither confirmed nor defeated** here.
8. **NO WEEK NUMBER AND NO DATE.** V16 never says which session it is (see the SOURCE table, and
   open item **196**). ⚠ **This DEFEATS the cheap forward-read check V15 offered at item 190** —
   a session that had reached forward into V16 hoping to confirm the Week-6 calendar **would have
   found nothing.** That is worth recording for item 179's ruling: *the forward read that was
   deliberately not taken would also not have paid.*
