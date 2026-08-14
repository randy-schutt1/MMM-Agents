# V14 — SOURCE NOTES

`Bootcamp1 Wk5 041512 Part2 (48mins).swf` · session **2012-04-15** · **Part 2 of the same
recording as V13** · course author, 100% of runtime.

---

## §0 — DECLARED DEVIATION FROM `SWF_CAPTURE_RECIPE.md` §9, READ THIS FIRST

**`D1` — the §9 ordering was broken in the same way V13 broke it, and it is disclosed here rather
than in a footnote.**

§9 requires source notes to be written **from the transcript alone**, before any frame is opened.
This session read the full 600-marker transcript first — before the sweep finished — but then ran
screen detection and **opened frames before writing this file**. So §9's ordering is broken.

**The mitigation, and it is falsifiable by `grep`:** every numbered item below carries **`[AUDIO]`**,
**`[PRINTED]`** or **`[AUDIO+PRINTED]`**. Any reader can check a tag by searching the transcript for
the quoted words. **Nothing tagged `[AUDIO]` depends on a frame**, and the conclusions this lesson
turns on — the drill, the TDI answer, the Week-6 evidence — are **all `[AUDIO]` or
`[AUDIO+PRINTED]`**, so the ordering break does not reach them.

---

## §1 — WHAT THIS LESSON IS

**V14 is the lesson content V13 promised and deferred, and it arrives.** `COURSE_PROGRESS.md`
V13 GATE (b) said *"the promised 'new lesson' content is deferred to V14 by the speaker himself,
twice. V14 is where it should arrive; if it does not, THAT is when a gap is recorded."*

**No gap is recorded. It arrives, and it is the most completely specified method in the corpus so
far.** `[00:00:00]` *"Okay, so look, let's get back to today's lesson and what you're going to do
this week."* **`[AUDIO]`**

The lesson has two halves:

| Half | `[ts]` | Content |
|---|---|---|
| **A — candles as footprint** | `[00:01:14]`–`[00:24:14]` | A taxonomy of candle formations, all read as **evidence the dealer's work is already done**, not as signals |
| **B — the high/low board drill** | `[00:24:18]`–`[00:47:46]` | **The week's assignment**: identify the day's extreme in real time **from the price board with no chart at all** |

---

## §2 — HALF B, THE ASSIGNMENT — THE PRINTED SLIDE, VERBATIM `[PRINTED]`

Read at full resolution from `V14_00-26-50_assignment-slide-the-high-low-board-drill.png`, which
carries its own burned-in timecode:

```text
MARKET MAKERS BOOT CAMP

 •  At 1am NYC time record the high and low of the majors
 •  Find a pair that is trading in the middle of the range
 •  Wait for the dealer to extend either level mark it down, wait for him to hit it
    several more times write it down again.
 •  When the dealer pulls off of the level and fails to hit it again for 1 hour take a position
 •  Stop loss level is 5 pips above/ below that number that appears on the board.
 •  Record your results and post in the forum
 •  Good luck
```

**The slide is on screen from `[00:26:50]` to the end of the lesson**, annotated live in green four
times. It is the only slide in the lesson that persists.

### §2a — WHAT THE SPEECH ADDS THAT THE PRINT DOES NOT CARRY

**Speech is a strict SUPERSET of print here.** This is the `A-081` / V12 `[00:43:18]` shape, **not**
a `C-017` print-vs-speech conflict — nothing printed is contradicted, three things are added:

| Added by speech only | `[ts]` | Words |
|---|---|---|
| **The ≤ 50-pip range filter** | `[00:27:28]` | *"**Identify the pairs that have not made more than a 50 pip range**"*; `[00:29:34]` *"Anything that's exploited or blown out **greater than 50**, exit out for the day at one o'clock, cross it out"*; `[00:38:35]` *"**if the box is less than 50 pips**"* |
| **The target** | `[00:32:38]` | *"Let it run, **aim for 30 to 50 pips**"* |
| **The entry offset** | `[00:32:25]` | *"open a long position in demo **at about 61 15**"* — the locked low being **61 05**, i.e. **10 pips inside the locked number** |

**⚠️ The ≤ 50-pip filter is the single most important omission from the printed slide**, because
without it the drill has no candidate-selection step at all. A session working from the slide alone
would run a different test from a session working from the recording.

### §2b — THE MECHANISM, IN THE SPEAKER'S OWN SEQUENCE `[AUDIO]`

1. `[00:27:05]` *"At **1 a.m. New York time**, record the high and low of the major six pairs"* —
   `[00:27:11]` *"the four majors plus the two commodity crosses"*
2. `[00:27:22]` *"**subtract them**… find out if it's 50 pips, 40 pips, 30 pips"*
3. `[00:27:28]` keep only ranges **≤ 50 pips**
4. `[00:27:34]` *"Find a pair that's **trading between the high and the low in the mid range**"*
5. `[00:27:47]` *"**Wait for the dealer to extend either level**, mark it down"*
6. `[00:31:33]` *"**Start a stopwatch right here.** Every time the dealer extends the high or low,
   start a stopwatch"* — **each new extreme restarts the clock**
7. `[00:28:09]` *"after the dealer pulls off the level and **fails to hit it again for one hour**"*
8. `[00:28:13]` *"if you've noted this, **take a position**"*
9. `[00:28:18]` *"the **stop-loss level is five pips above or below** the number that appears on
   the board"*
10. `[00:32:38]` *"Let it run, **aim for 30 to 50 pips**"*

**The worked example, given twice with real numbers `[AUDIO]`:**

| | Long example `[00:29:09]`–`[00:32:42]` | Short example `[00:33:02]`–`[00:35:37]` |
|---|---|---|
| 01:00 high / low | `6160` / `6127` | `3190` / `3155` |
| Range | 33 pips — *"less than 50 pips. Yes"* | 35 pips — *"Less than 50 pips. Yes"* |
| Price at 01:00 | `6142` — *"in the middle of the range. Hell yeah, it is"* | `3162` — *"He's off of the low and off of the high, **he's closer to the low right now**"* |
| Extension | low → `6115`, then → `6105` | high → `3230` |
| The lock | *"45 minutes, an hour, and price hasn't come off of 61 05"* | *"an hour, hour and 15, hour and 30"* |
| Entry | *"**go long… at about 61 15**"* | *"take a short… **around 32 25, 32 22**"* |
| Stop | *"**61 05, 5 pips below**"* | *"**32 30 plus 5**, stop loss is 32 35"* |

**⚠️ The two examples do not use the same entry offset** — 10 pips inside in the first, 5–8 pips
inside in the second. Logged as `A-090`.

**⚠️ And the second example's price at 01:00 fails the filter the first example applies.** `3162`
in a `3155`–`3190` range is at the **20th percentile**, and the speaker calls it *"closer to the
low"* and proceeds anyway. `6142` in `6127`–`6160` is at the **45th percentile**. **The printed
step 2 says *"in the middle of the range"* and the speaker's own two examples span 20% to 45%.**
Logged as `A-089` — this is the step that makes the drill non-computable as printed.

---

## §3 — THE US-SESSION VARIANT `[AUDIO]`

`[00:36:35]` *"If you're going to try it in the U.S. session, **re-bracket the data** and do it
8 to 9, re-bracket from 8 to 9:30 session changeover, and look for the move to come 9:45,
10 o'clock."* `[00:33:25]` *"You got to do this for **London**, but you can try it in New York…
It's harder for New York, it's easier in London."*

`[00:41:57]` names the reason the US variant is harder: *"if he extends below at nine thirty…
**the high's all the way up here on the big board. You can't reset your big board.** That's the
problem with the U.S."* — the MT4 board's high/low is a **broker-day** figure and does not restart
at the New York session.

## §4 — THE CLOCK `[AUDIO+PRINTED]`

⭐ **The drill's clock reference carries an EXPLICIT TIMEZONE, printed and spoken.** Printed:
*"At **1am NYC time**"*. Spoken `[00:27:05]`: *"At **1 a.m. New York time**"*. `[00:45:16]`:
*"**Ted**, if you can't make it at 1 a.m., do 2 a.m. **1 a.m. is the time I was taught to do it**,
man."*

**This is notable because `A-019` records that the course's session-map slide prints times with no
timezone and the instructor declines to supply one.** V14 does not close `A-019` — it is a
different slide and a different clock reference — but it is **the first explicitly timezoned clock
statement in the corpus**, and `[00:45:16]` shows the 1 a.m. figure is **inherited, not derived**.

---

## §5 — THE TDI PASSAGE — the lesson's other load-bearing minute `[AUDIO]`

Reproduced in full because every word is contested. **This is a student question read aloud from
chat and answered live**, `[00:44:41]`–`[00:45:14]`, confirmed verbatim by two ASR engines:

```text
[00:44:41]  John has a question. Let me see.
[00:44:43]  "Steve, I know that you're not looking at comments, but I am right now.
[00:44:45]   The TDI, does the green RSI line represent the 15-minute chart candles?
[00:44:49]   Does the red trade signal line represent the one hour?"
[00:44:51]  Yes.
[00:44:52]  "Does the yellow market baseline represent the four hour candles?"
[00:44:55]  No.
[00:44:56]  The TDI line, RSI is green.
[00:44:59]  The red line, blood in the water, is the one hour.
[00:45:02]  The market baseline is the basis of where price is ranging.
[00:45:09]  The bands are two standard deviations away from the market base.
[00:45:14]  It's a liquid 50.                       <- UNRESOLVED BY BOTH ENGINES
```

**Four separate records are touched and the effects run in different directions.** Each is worked
in `V14_INTERPRETATION.md` Q3 and filed in `10_AMBIGUITIES/` / `11_CONTRADICTIONS/`:

| Record | Effect |
|---|---|
| **`A-084`** — is the green line `RSI(21)` or a smoothing of it? | **NARROWED, NOT CLOSED.** Second consecutive lesson |
| **`A-085`** — *"the TSL polls the one-hour chart"* | **EXTENDED, NOT CLOSED.** Restated in its strongest form yet, still with no construction |
| **`A-086`** — the volatility bands | ⭐ **MATERIALLY ADVANCED.** The multiplier is stated **unhedged** for the first time |
| **`C-021`** — NEW | ⭐ The band **basis** is stated as *"the market base"*, which is the answer V12 **retracted** |

---

## §6 — HALF A: THE CANDLE TAXONOMY `[AUDIO+PRINTED]`

Every formation is given the **same** reading — the candle is the footprint of work already
completed. `[00:07:05]` *"Understand something about candles: it represents where price has been"*;
`[00:07:14]` *"**When a candle paints, the damage is done.**"*

| Formation | `[ts]` | The speaker's reading |
|---|---|---|
| **Hammer / inverted hammer** | `[00:01:43]` | *"a hammer is a beautiful entry… the dealer went down there, got what he needed and came back above or below"*. `[00:17:46]` printed: *"Used to activate pendings, trigger the stops"* |
| **Vector candle** | `[00:02:52]`–`[00:03:15]` | ⚠️ *"Why do you take the vector candle as an anticipation of where the dealer's gonna stall? **And that is a mistake.** The vector candle means nothing other than the fact that the dealer has **extended the level**"* |
| **"Momentum" candle** | `[00:03:30]` | ⭐ **Repudiated by name**: *"retail traders call it momentum candles and **they couldn't be more wrong**… that is a **stop-hunt candle**"* |
| **High test / low test** | `[00:02:18]` | *"the dealer makes the run back towards the high… and **fails to take that level out**"*; `[00:02:36]` *"usually the formation of the **second leg**"* |
| **Railroad tracks** | `[00:02:12]`, `[00:17:59]` | *"15 minutes in, cuts the high, comes right back below the high 15 minutes later"*; *"get in, grab the money, **create immediate drawdown and panic**"* |
| **Evening / morning star** | `[00:15:55]`–`[00:17:00]` | ⭐ **Repudiated by name, at length**: *"indecision of traders — **bullshit**… an evening star morning star formation is a **bullshit ploy by people that don't know any better**. There is absolutely no indecision, the dealer knows exactly where he's going"* |
| **Doji / spinning top** | `[00:02:00]`, `[00:17:27]` | *"the dealer adds an **extra 15 minutes** in there to snag the traders"* |

⭐ **`[00:03:30]` and `[00:15:55]` are the third and fourth instances in the corpus of the speaker
repudiating a named retail concept off a slide he is presenting** — the pattern `REVIEW_INDEX.md`
item 132 records (V12 `[00:09:51]` *"momentum we know is bullshit"* on Dean Malone's definition;
V11's `POSITIVE TREND`). **V14 `[00:03:30]` repudiates the same word V12 did, five weeks later, on
a different slide.**

## §7 — THE TRAP-MOVE SLIDES `[PRINTED]`

Three consecutive slides, `[00:18:10]`–`[00:23:20]`, printed:

```text
MARKET MAKER TRAP MOVES
  Market Makers Induce Traders To Take The Wrong Directional Move By Sharp
  Aggressive Price Changes At Or Near The HOD and LOD
  These Patterns Will Almost Always Reveal A Reversal Setup
  Why Would It Fail? Trap Volume Does Not Total The Value They Were Seeking,
  Extended Stop Hunt Will Be Seen ( 2HR Time Gap)

MARKET MAKER TRAP MOVE
  When Trap Volume Is Not Met The Market Maker Will Have 2 Moves Left....
    1. Hit The Stops And Rise /Fall
    2. Hold The Level And Handle The Cross
  These Moves Are Carried Out Over A Time Interval, And Induce Traders To Take A Position

MARKET MAKER TRAP MOVE
  If You Are Caught By This Move You Must Wait For Next Level Rise/Fall
    Minimum 2 Hrs
    Session Change Over
```

**Spoken corroboration:** `[00:19:17]` *"he's got to hit the stops one more level **25 to 50 pips
higher, 25 to 50 pips lower**"*; `[00:23:22]` *"You wait for the next rise or fall, **minimum of two
hours**, or you wait for the **session changeover**"*; `[00:24:01]` *"session changeover, minimum
two hours"*.

⚠️ **`25 to 50` appears again**, in the **level-spacing** sense. `C-020` §2 records this token as
colliding across at least three quantities in this corpus. **V14 adds a fourth use and does not
disambiguate it.** Nothing here is adopted.

## §8 — "HANDLING THE CROSS" — a mechanism claim `[AUDIO]`

`[00:20:51]`–`[00:21:14]`: *"He's handling the crosses. If you understand **fractional disparity**…
to create a disparity between the numerator and the denominator, **one pair has to freeze at a
level and hold it and another pair has to be moved.** Creates the disparity in the crosses, in the
fraction — makes EJ move, EC move, EA move, EG move."*

**Recorded, not adopted.** It is an unsourced mechanism claim of the `A-085` family: a real
arithmetic property of cross rates offered as an account of intent. **No V14 artifact rests on it.**
Filed as `A-091`.

## §9 — THE HUMAN-CONDITION PASSAGE `[AUDIO]`

`[00:21:56]`–`[00:23:07]`. The dealer *"exploits people and their 24-hour body cycle, because he's
three guys working eight hours apiece"*. **Rhetorical, not operational** — but it is the stated
reason for the two-hour wait rule in §7, so it is recorded as the rule's rationale.

## §10 — WHAT THE LESSON SAYS ABOUT ITS OWN STATUS

| `[ts]` | Words | Bearing |
|---|---|---|
| `[00:32:42]` | *"That's **a drill**"* | ⚠️ The `A-082` hazard — see `V14_INTERPRETATION.md` Q4 |
| `[00:37:12]` | *"This is a very important drill **to help you understand the candles**"* | Stated purpose is pedagogical |
| `[00:40:33]` | *"It's going to make you **see what's going on in the candles**"* | Same |
| `[00:07:40]` | *"**This is how I learned**, and this is why I don't take shit inside the blue box"* | Autobiographical warrant |
| `[00:28:33]` | *"**This is how I learned how to trade**, by the way"* | Same, restated |
| `[00:46:20]` | *"technically, Keith, **you will be able to trade off of the board only**"* | ⭐ **Answering a direct student question about whether it is deployable.** See `A-056` |
