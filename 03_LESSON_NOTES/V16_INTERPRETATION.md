# V16 — INTERPRETATION

**Source:** `Bootcamp1 Wk7 050612 Part2 (45mins).swf` · V16 · 2012-05-06 · 00:44:35
**Timestamp convention:** the committed marker grid of `02_TRANSCRIPTS/V16/V16_TRANSCRIPT.md`.

**This file is kept strictly separate from `V16_SOURCE_NOTES.md`.** The source notes record what
was said and printed. This file records **what I take it to mean, and how confident I am**, using
the classification `STUDY_PROTOCOL.md` §1.4 requires:

| Class | Meaning |
|---|---|
| **EXPLICIT** | Stated in words by the course author, in this file |
| **VISUAL** | Printed or drawn on screen, in this file |
| **IMPLIED** | Not stated, but the lesson does not make sense without it |
| **INFERRED** | My reading. Could be wrong. The evidence is given so it can be attacked |
| **UNRESOLVED** | I do not know, and I am not guessing |

⛔ **NOTHING IN THIS FILE IS PROMOTED TO A RULE.** `D-030` and the Student-Phase prohibition on
populating `12_MASTER_SPEC/` and `13_MACHINE_SPEC/` are untouched by anything below.

---

## §1 — THE LESSON'S CLAIM, RESTATED IN MY OWN WORDS

**INFERRED, HIGH confidence.** The lesson makes one argument in four moves:

1. A daily candle's OHLC generates a fixed grid of nine price levels for the following day
   (**EXPLICIT**, §3 of the source notes).
2. The candle's **colour** selects which pair of those levels is the day's projected high and low
   (**EXPLICIT + VISUAL**).
3. That projection is reliable for about three days and then **inverts** on the fourth
   (**EXPLICIT**, stated three times).
4. Where a grid level coincides with an ADR marker and a moving average, that coincidence is where
   an `M` or `W` is expected to form — and **the `M`/`W`, not the level, is the trigger**
   (**EXPLICIT**, `[00:33:43]`–`[00:33:58]`).

⭐ **The fourth move is the one that matters for this project, and the lesson is unusually honest
about it.** *"Ignore the pivots and identify what I've taught you, the pattern, the pattern, that's
the answer."* The pivot grid is a **location prior**, not a signal. Any implementation that treats
a pivot touch as an entry is implementing something the lesson explicitly disclaims.

---

## §2 — ITEM-BY-ITEM CLASSIFICATION

| # | Item | Class | Evidence | Confidence |
|---|---|---|---|---|
| 1 | Pivots are computed from the previous day's daily candle OHLC | **EXPLICIT + VISUAL** | `[00:00:41]`–`[00:00:47]`; slide `V16_00-00-50` | HIGH |
| 2 | Red daily candle → project `M1`/`M3`; green → `M2`/`M4` | **EXPLICIT + VISUAL** | `[00:00:59]`, `[00:14:50]`–`[00:15:11]`; slide `V16_00-00-50`; annotation `V16_00-15-00` | HIGH |
| 3 | Grid order is `R2 M4 R1 M3 CPP M2 S1 M1 S2` | **VISUAL** | `V16_00-01-40`, measured | HIGH |
| 4 | `M3`/`M4` are candidate day highs; `M1`/`M2` candidate day lows | **EXPLICIT + VISUAL** | `[00:17:53]`–`[00:18:19]`; slide `V16_00-18-00` | HIGH |
| 5 | Projected range = `M3 − M1` (or `M4 − M2`) | **EXPLICIT + VISUAL** | `[00:19:49]`; slide `V16_00-18-00` *"Ex: ( M1 – M3)"* | HIGH |
| 6 | `M1`–`M4` are arithmetic midpoints of adjacent standard pivots | **UNRESOLVED** | See §3 below — the tidy answer was tested and is **not** supported | — |
| 7 | ADR lookback = *"the last two weeks, 15 days"* | **EXPLICIT** | `[00:09:31]` | HIGH **that he said it**; ⚠ LOW that it is self-consistent |
| 8 | The three-day cycle, and the fourth-day inversion | **EXPLICIT ×3** | `[00:12:30]`, `[00:13:14]`–`[00:13:32]`, `[00:15:11]`–`[00:15:36]`, `[00:31:32]`–`[00:31:48]` | HIGH |
| 9 | What starts a cycle | **UNRESOLVED** | Never stated. See §4 | — |
| 10 | The London-open read: price in the red band at the London open → SELL; green band → BUY | ⭐ **EXPLICIT + VISUAL** *(upgraded from `VISUAL`, MEDIUM, after arbitration)* | `[00:14:23]` **arbitrated to *"At the London Open, if the dealer breaks high in the top side of the pivot grid, you're a seller"*** (correction #1); slide `V16_00-14-25`; legend `PRICE AT LONDON OPEN` on `V16_00-01-40` | **HIGH** |
| 11 | London session start = `2:00 To 3:00 AM, EST` | **VISUAL** | slide `V16_00-14-25` | HIGH **that it is printed**; see §5 for what it does and does not settle |
| 12 | Pivot grid ≈ ADR grid; their coincidence is the high-value location | **EXPLICIT + VISUAL** | `[00:27:36]`–`[00:28:06]`; slide `V16_00-27-45` | HIGH |
| 13 | The tolerance for *"line up"* | **UNRESOLVED** | Never stated → `A-102` | — |
| 14 | *"the wrong segment"* of the grid | **UNRESOLVED** | Shown on three charts, defined never → `A-103` | — |
| 15 | The dealer's daily allotment is ~200 pips in every pair except `GJ` | **EXPLICIT**, stated as fact | `[00:22:44]`–`[00:22:50]`, `[00:30:12]` | HIGH that he said it; **the claim itself is untested here** |
| 16 | The `600–1000` pip week | **EXPLICIT**, and **already CONTRADICTED by measurement** | `[00:23:24]`; `BT_V10_0001` 0/180 weeks | — |
| 17 | Pivots are computed midnight-to-midnight | **EXPLICIT**, and **contradicted 40 s later by the same speaker** | `[00:40:22]`–`[00:40:34]` vs `[00:41:09]`–`[00:41:18]` → `C-023` | — |
| 18 | The homework specification | **EXPLICIT + VISUAL**, complete | `[00:35:03]`–`[00:35:36]`, `[00:40:52]`–`[00:41:02]`; slide `V16_00-35-05` | HIGH |
| 19 | Speaker is the course author, 100% | **INFERRED** from six non-acoustic strands | `V16_TRANSCRIPT.md` SPEAKER TABLE | HIGH, not CERTAIN |
| 20 | `M5` exists as a grid level | **UNRESOLVED — and NO LONGER attributable to ASR damage** | `[00:33:24]`–`[00:33:30]`, **confirmed twice in one sentence by BOTH engines** (correction #3); **no `M5` on the printed grid** → `A-101` | — |

---

## §3 — Q1: ARE `M1`–`M4` MIDPOINTS? THE TIDY ANSWER WAS TESTED AND IT DID NOT SURVIVE

**This is the question a reader will ask first, and it is the one I most wanted to answer yes to.**

**The case FOR:** the printed order interleaves `M4` between `R1` and `R2`, `M3` between `CPP` and
`R1`, `M2` between `S1` and `CPP`, `M1` between `S2` and `S1`. Interleaving is what a midpoint
does. The naming (`M` for *mid*) is suggestive. It would make the whole grid computable from four
lines of arithmetic, and it would unblock `A-096` completely.

**The case AGAINST, and it is a measurement rather than an argument:** if the slide were drawn to
scale, the vertical gaps would encode the arithmetic. They do not encode anything — **all eight
gaps between the nine labels are equal to within one pixel** (53 · 52 · 53 · 53 · 51 · 52.5 · 53,
mean 52.5). Under every standard floor-trader formula the `R1→R2` gap differs from the `CPP→R1`
gap. **A schematic drawn with equal spacing looks exactly like this whatever the real formula is,
so the diagram carries no information about the formula at all.**

**Verdict: UNRESOLVED, and `A-101` records the hypothesis WITH its defeater so a later session does
not re-derive the same tidy wrong answer.** ⚠ **What would settle it in one frame:** a chart
screenshot where both the pivot levels and their numeric prices are legible. `V16_00-16-50` and
`V16_00-17-30` show the grid on a price scale, and I could not read the price axis at 1024×786.
**A higher-resolution capture of those two frames is the cheapest open route** and is offered at
open item **198**.

⚠ **Self-charge:** my first draft of the source notes asserted the midpoint reading as a finding.
It is recorded here because it was caught by doing the measurement, not by being careful.

---

## §4 — Q2: WHAT DOES V16 ACTUALLY UNBLOCK?

**Honest accounting, because the temptation after a lesson this well-printed is to overclaim.**

| Record | Before V16 | After V16 | Closed? |
|---|---|---|---|
| `A-096` (`M1`–`M4` are pivot levels) | decoded from frames, Tier 2 only | **PRINTED IN TIER 1, with the full nine-level order** | ⭐ **The IDENTITY question closes. The CONSTRUCTION question does not, and moves to `A-101`** |
| `A-100` (ADR lookback absent) | *"the corpus cannot compute the object it teaches"* | **a number exists**: *"two weeks, 15 days"* | ❌ **NO.** Three of four missing pieces are still missing, and the number contradicts its own gloss |
| `A-095` (`A-082`-class pip figures) | three figures in V15 | **five more**, one with an instrument scope | ❌ extended, not closed |
| `A-097` (*"22-trade"*, *"3333 trade"*) | two undefined trade names | *"33 trade"* occurs **twice**; *"22"* zero times | ❌ **corroborated as real, still undefined** |
| `A-020` (MA nicknames → periods) | nicknames without periods | *"blueberry"* twice, **still no period** | ❌ |
| `A-084` (TDI thresholds) | blocked; 2,670 frames of nothing | **544 more frames of nothing** (3,214 total) | ❌ and **expected** — GATE (b) said not to hunt |
| `C-022` (ADR repaint) | open | **V16 never mentions repainting** | ❌ untouched |
| `A-010`/`A-011` (`M`/`W` definition) | open | used ~9 times, defined never | ❌ |
| — | — | **`C-023`, `A-101`, `A-102`, `A-103`, `A-104` opened** | — |

⭐ **The one clean win is `A-096`'s identity half.** Everything else advanced or held. **That is
the correct result to report, and it is smaller than the lesson feels.**

---

## §5 — Q3: THE PRINTED SESSION CLOCK — WHAT IT SETTLES AND WHAT IT DOES NOT

`V16_00-14-25` prints `London Session Start / 2:00 To 3:00 AM, EST`. **This is the corpus's first
printed, timezone-stamped, session-BOUNDARY clock time.** (V06's `3:45am or 9:45am est.` is a
clock time on a chart, not a labelled session boundary.)

**What it settles:** that the course does attach a definite clock to *"the London open"*, and that
the pivot-grid read in §2 item 10 is taken at that time.

**What it does NOT settle, and I am not going to let the find run past its evidence:**

1. ⚠ **It disagrees with the same lesson's own audio.** `[00:02:36]` puts the stop-trigger at
   *"1 o'clock or 2 o'clock or 3 o'clock depending on when I feel like it"* — no timezone, wider
   window, and about a *different event* (the stop hunt, not the session start). **I record both
   and reconcile neither.**
2. ⚠ **`EST` vs `EDT`.** 2012-05-06 is inside US daylight time. A slide reading `EST` in May is
   either loose usage for *"New York time"* or a literal claim about a standard-time offset, and
   the two differ by an hour. **Nothing in the corpus decides it.** This is the same class of
   defect as `A-019`, and `BT_V06_0001` already showed a one-hour shift can flip a result's sign.
3. It says nothing about the London **close**, the New York boundaries, or the Asian range's
   bounds.

**Recorded in `A-105`. It is a genuine advance on a question this corpus has been vague about for
sixteen lessons, and it is one line on one slide.**

---

## §6 — Q4: HOW MUCH OF THIS IS TESTABLE, AND WHAT I CHOSE TO TEST

**Testable as stated, on data this project already holds:**

| Claim | Testable? |
|---|---|
| *"Red candle → the day's high and low fall at `M1`/`M3`"* | ⛔ **NO** — `M1`/`M3` are not computable (`A-101`) |
| *"Pivots are accurate for three days, off on the fourth"* | ⛔ **NO** — same blocker, plus no cycle-start test (`A-104`… §4 item 9) |
| *"Coupling pivots with ADR markers gives strong confirmations"* | ⛔ **NO** — both legs blocked, plus `C-022`'s lookahead problem |
| *"~200 pips in every pair except `GJ`"* | ⭐ **YES** — a daily-range claim with an instrument scope, a stated value, and a named exception |
| *"600–1000 pips for the week"* | ✅ already **CONTRADICTED** (`BT_V10_0001`) — **`D-027` forbids re-testing it** |
| *"A break of one level is almost always certain to give way to the next"* | ⛔ **NO** — levels not computable |

⭐ **So exactly one claim in this lesson survives to a testable form, and it is the one the lesson
states most confidently and least carefully.** `PT-044` tests it. **It was pre-registered before
the data existed and before the runner was written** — see `06_MANUAL_BACKTEST/V16/BT_V16_0001.md`.

⚠ **AND THE CHOICE IS ITSELF A FINDING.** A lesson that prints four bullet-slides of rules yields
**one** testable proposition, and that proposition is an aside about dealers' limits rather than
anything a student would trade. **That is `D-030`'s case made for the sixteenth time.**

---

## §7 — WHAT I WOULD BE WRONG ABOUT IF I AM WRONG

Stated so a reviewer can aim.

1. **The speaker.** Five *"Steve"* tokens, **none** a self-naming. If strands 1 and 2 are
   *"reading a student's post aloud"* rather than *"answering in his own voice"*, the
   identification leans entirely on ownership language. I still think HIGH is right; I would not
   defend CERTAIN.
2. **§3's midpoint defeater.** If the slide is a *rendering* of a real grid rather than a
   schematic — i.e. if the underlying pivots on that particular day happened to be near-equally
   spaced — then equal pixel spacing is consistent with the midpoint reading after all. **I think
   this is unlikely (equal spacing to ±1 px across eight gaps is a drawing artefact, not a
   market coincidence) but it is not impossible, and it is the attack I would make.**
3. **§5's `EST`/`EDT`.** I have treated the slide as evidence that a definite clock exists, not as
   evidence of *which* clock. A reader who reads `EST` literally gets a different hour than one who
   reads it as *"New York time"*.
4. ~~**`[00:14:23]`.** If the independent ASR pass returns something other than *"London"*, item 10
   in §2 loses its audio leg and becomes `[VISUAL]`-only.~~ ⭐ **RESOLVED IN THIS SESSION.** The
   pass returned *"At the **London** Open"* and item 10 was upgraded to **EXPLICIT + VISUAL, HIGH**.
   *(Retained per `REMEDIATION_PROTOCOL.md` §2 — the prediction was made before the answer was
   known and it is worth more visible than deleted.)*
5. ⭐ **`M5`, which I did not anticipate at all.** Two independent engines hear *"M5"* twice in one
   sentence, and there is no `M5` on the printed grid. **If a later session shows the live grid has
   more levels than the slide, `A-101`'s pixel-spacing argument (§3) is unaffected but §2's
   nine-level enumeration is incomplete.** I do not think that is likely; I did not test it.
