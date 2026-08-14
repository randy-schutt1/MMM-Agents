# V14 — HOMEWORK

## §0 — THE ASSIGNMENT AS SET, AND THE DECLARED SUBSTITUTION

**V14 sets an explicit two-week assignment**, `[00:24:18]` *"Week five R&D, you got two weeks to do
this stuff"*, in two parts:

| # | `[ts]` | Assignment |
|---|---|---|
| **1** | `[00:24:27]` | *"**TDI drill: do at least five more trades using only TDI.** Keep going till you get it. It's demo, folks"* — the V13 assignment, carried forward |
| **2** | `[00:24:51]`, printed | ⭐ *"I want you to **use the big board** to enter all your trades"* — the six-step high/low board drill |

> ### ⚠️ `D2` — DECLARED DEVIATION: THE ASSIGNMENT AS SET CANNOT BE PERFORMED, AND A FAKED VERSION WOULD BE WORSE THAN A DECLARED SUBSTITUTION
>
> **Both parts are LIVE-MARKET, FORWARD-LOOKING, TWO-WEEK exercises.** Part 2 requires sitting at
> an MT4 pop-up-prices board at 01:00 New York on successive nights, watching a tick feed, and
> recording numbers by hand in a notebook. **This session has no live feed, no MT4 terminal, and no
> two weeks**, and the corpus on disk is **2013–2016 historical M1**.
>
> **Part 1 is additionally BLOCKED, not merely impractical.** *"Five more trades using only TDI"*
> requires constructing the TDI — and `A-084` (green line), `A-085` (red line) and `A-086` (the
> bands, still with **no period**, see `C-021`) mean **the indicator cannot be built to the
> standard `D-030` requires.** V14 does not unblock it; it narrows `A-084` and does not close it.
>
> **What was done instead, and why it is the honest substitution:** the drill's **six computable
> steps** are reconstructed on the historical corpus as a pre-registered test, **`PT-042`**. That
> is the closest thing to *"record your results and post it in the forum"* `[00:28:26]` that this
> project can actually do — it records results against data whose SHA-256 is on the record, which
> is a **stronger** evidentiary standard than a notebook.
>
> **A fabricated notebook of two weeks of 1 a.m. board readings would have been the corrosive
> option** in a repository that has quarantined **fifteen** sets of files for exactly that
> (`Q-001`…`Q-015`). It was not written.

---

## §1 — COMPREHENSION: THE DRILL, RESTATED WITHOUT LOOKING BACK

Written before re-opening `V14_SOURCE_NOTES.md`, then checked against it. **Two errors were made
and both are left visible below**, per `REMEDIATION_PROTOCOL.md` §2.

| # | Step, as recalled | Check |
|---|---|---|
| 1 | At 01:00 New York, record the high and low of the majors | ✅ |
| 2 | Keep pairs whose range is **≤ 50 pips** | ✅ — and ⚠️ **this is spoken only; it is NOT on the printed slide.** I had assumed it was printed |
| 3 | Pick one trading in the middle of the range | ✅ printed — ❌ **undefined** (`A-089`) |
| 4 | Wait for the dealer to extend either level; write the new number down; wait for repeat hits and write it down again | ✅ |
| 5 | ~~Enter when price pulls away~~ → **enter when the level has gone ONE HOUR without being hit again** | ⚠️ **Error 1, corrected.** My first recall had the trigger as *"price pulls away"*, which is V10's lock language (`A-077`). **V14's trigger is a DURATION, and the duration is the whole point** — it is the `N` `A-077` says appears in no lesson |
| 6 | Stop **5 pips** beyond the number on the board | ✅ printed |
| 7 | ~~Target 25 to 50~~ → **target 30 to 50 pips** | ⚠️ **Error 2, corrected.** I recalled `25 to 50`, which is the *level-spacing / stop-hunt* token from `[00:19:17]` and `C-020` §2. **The target is `30 to 50`** `[00:32:38]`. ⭐ **This is exactly the `C-020` §2 collision doing its damage inside my own head**, which is the best argument for why that record exists |

**Both errors ran in the same direction: toward numbers I already knew from earlier lessons.** That
is the failure mode this repository's whole method is built against, and it is recorded rather than
quietly fixed.

---

## §2 — THE QUESTIONS THE LESSON ASKS, ANSWERED

**Q1. `[00:29:51]` *"This is the reason that I don't take M's and W's in the blue box. Here's why."*
What is the why?**

> `[00:29:57]` *"**If the dealer hasn't extended the 61 60 or 61 27 level, you have nothing.** Since
> he hasn't extended that level, **it's impossible to take a trade in between these numbers.**"*
> `[00:30:15]` *"if I see something in between here… **it's chop, it's nothing**."*

**The argument is that a pattern inside the range is not evidence of anything, because the
information the method uses — which level the dealer chose to extend — has not yet been produced.**
`[00:08:13]` *"this looks like an M to you and you want to take it, but **nothing has happened yet
other than consolidation**."*

⭐ This is the clearest statement in the corpus of **why** the blue box is a no-trade zone, and it is
a *causal* reason rather than a rule. **It still does not define the M** (`A-011`, tenth lesson).

**Q2. What is the drill's stated purpose, and does the lesson claim it is tradeable?**

**It says both, and `V14_INTERPRETATION.md` Q4 refuses to pick.** Purpose: `[00:37:08]` *"a very
important drill **to help you understand the candles**"*. Tradeable: `[00:46:19]` *"technically,
Keith, **you will be able to trade off of the board only**"* — ⚠️ whose first word two ASR engines
render differently (*"No"* / *"Now"*), which the transcript records rather than resolves.

**Q3. Why does the lesson insist on removing the charts?**

> `[00:35:59]` *"you're **not looking at levels**, you're **not looking at candles**, you're
> **looking inside the numbers**"*
> `[00:45:35]` *"getting away from the charts for a couple of weeks is going to **change you as a
> trader. You're too reliant on candles.**"*
> `[00:46:31]` *"I want you to **tie one hand behind your back**, or I want you to **trade
> blindfolded** away from the charts"*

**The stated mechanism is that the candle is a lagging artifact** — `[00:07:14]` *"When a candle
paints, the damage is done"* — **so a student reading candles is reading a report of a decision
already executed, while the board shows it happening.**

**Q4. What does the lesson say happens if you are caught on the wrong side?**

Printed: *"If You Are Caught By This Move You Must Wait For Next Level Rise/Fall — **Minimum 2 Hrs**
— Session Change Over"*. Spoken `[00:23:22]`: *"You wait for the next rise or fall, **minimum of two
hours**, or you wait for the **session changeover**."*

⚠️ **Note the asymmetry, and it is not remarked on by the lesson:** the entry trigger is a **1-hour**
hold, and the recovery wait after being wrong is a **2-hour** minimum. **Nothing relates the two
figures.**

**Q5. Which claim in this lesson is testable, and which is the most tempting untestable one?**

**Testable:** *"after that number is a lock for one hour"* → *"it's the high of the day"*. Arithmetic
once the session day is fixed. **`PT-042` `O1`.**

**Most tempting untestable:** `[00:10:45]` *"**How long does the structure take? An hour, 90
minutes, two hours?** … an hour, hour and a half, 90 minutes is **primo**, that's ideal."* It sounds
like a parameter and it is a **retrospective description of a completed structure**, with *"the
structure"* undefined (`A-007`, `A-033`). **Coding it would require inventing what counts as the
structure starting.** Not tested, and named here so the temptation is on the record.

---

## §3 — WHAT WAS ACTUALLY DONE

| Deliverable | Where |
|---|---|
| The drill's six computable steps, fully specified before any data was read | `PT-042` §3 |
| The one step that could not be specified, and why | `PT-042` §3a · `A-089` |
| The test | `06_MANUAL_BACKTEST/V14/BT_V14_0001.md` |
| The `A-084`/`A-085`/`A-086` pass on the TDI half of the assignment | `V14_INTERPRETATION.md` Q3 |

**The TDI half of the assignment is reported as BLOCKED, not as done, and not as skipped.**
