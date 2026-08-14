# V12 — HOMEWORK

**Lesson:** V12 · `Bootcamp1 Wk4 040812 Part2 (55mins).swf` · 2012-04-08 · course author, 100%
**Assignments source:** `03_LESSON_NOTES/V12_SOURCE_NOTES.md` §8, taken from the transcript before
the screenshot pass; the printed slide (`V12_00-42-06_this-weeks-r-and-d-assignment-slide.png`)
was reconciled against it afterwards.

## ⭐ THE HEADLINE FACT: THIS IS V11'S MISSING ASSIGNMENT, AND IT ARRIVES IN FULL

V11 `[00:00:46]` promised *"a really good assignment coming up this week… I'm gonna **insist** that
you do it"* and **ended 50 minutes later without giving it**. `05_HOMEWORK/V11/V11_HOMEWORK.md`
recorded the promise and **refused to invent the content**.

**V12 delivers it.** `COURSE_PROGRESS.md` V12 GATE (c) is discharged, and **this is V11's
assignment as much as V12's** — same session, same week, the promise made in Part 1 and kept in
Part 2.

**It is also the most specific homework in the corpus**: printed as four lines, spoken for six
minutes, with a named account size, a named instrument list, an enforced constraint, a method for
enforcing it, and a posting requirement.

---

## THE ASSIGNMENT AS GIVEN

**Printed**, frame `42:06`, headed `THIS WEEKS R & D`:

> *"Find And Identify The Trade Signals Using TDI · Use any pair you like. Black out price action
> and check your knowledge."*

**Spoken**, `[00:42:09]`–`[00:49:08]` — **substantially more than the slide.** The slide is the
short form; the six minutes of speech are the assignment.

## DISPOSITIONS — `D-018` / `D-019`

> `D-019` binds: **`NOT APPLICABLE` means there is nothing here to do, ever, for this lesson.
> `DEFERRED` means the work exists and is blocked.** The test is *"is there anything here to do at
> all"*, not *"can this be done today"*.

| # | Item | Timestamp | Disposition |
|---|---|---|---|
| **H1** | **Mark up TDI trade signals with price action blacked out** — *"about four of those"* / *"five of those"* on any pair | `[00:42:15]`–`[00:43:11]`; printed `42:06` | ⛔ **DEFERRED — blocked by `A-039` + `A-086`** |
| **H2** | ⭐ **THE DRILL.** Open a **$10,000 demo account**, strip the chart of everything **including the candles**, stretch the TDI to full screen, and **execute five live demo trades on the TDI alone** | `[00:43:18]`–`[00:44:13]` | ⛔ **DEFERRED — blocked by `A-039` + `A-086`.** It is *also* real-time forward testing, which `16_FORWARD_TEST/` holds for a later phase — but **that is a scheduling fact, not a second blocker**, see the note below |
| **H3** | Permitted instruments: **the TDI and a wristwatch, nothing else** — *"because I don't want you trading TDI signals at two in the afternoon"* | `[00:45:11]`–`[00:45:33]` | ⛔ **DEFERRED — rides on H2** |
| **H4** | Restrict the live drill to **EUR/USD and GBP/USD** — *"so we're all trading the same shit"* | `[00:46:27]`–`[00:48:12]` | ⛔ **DEFERRED — rides on H2** |
| **H5** | **Post the results** in the forum's homework section with a marked-up screenshot | `[00:44:13]`–`[00:44:26]`, `[00:45:43]` | **NOT APPLICABLE** |
| **H6** | The blacking-out method, read from chat and endorsed: line graph, then **F8 → properties → line colour = background colour** | `[00:47:36]`–`[00:47:48]` | **PERFORMED — see §3.** The only item in this lesson's homework that could be done |
| **H7** | Choose your own stop size for the drill — *"you tell me… seven, ten sounds great"* | `[00:48:15]`–`[00:48:54]` | ⛔ **DEFERRED — blocked by `A-066`, and the LESSON ITSELF declines to answer it** |

**One `NOT APPLICABLE`, five `DEFERRED`, one `PERFORMED`.**

> ### ⚠️ WHY SO MUCH IS DEFERRED, AND WHY THAT IS NOT A COP-OUT
>
> **Every item H1–H4 and H7 requires reading the TDI, and the TDI is not reconstructible.**
> `A-039` narrows on V12 but does not close: **three of its four parameters remain unstated**
> (`A-085` the trade signal line, `A-086` the volatility bands — whose basis the instructor
> **retracts mid-sentence** — and the market baseline's smoothing). `A-031` and `A-032` close
> **as to meaning** and are explicitly **not computable** for the same reason.
>
> **The drill's whole premise is that you see NOTHING except the indicator.** There is no partial
> version: with the bands unspecified there is no *"outside the band"*, and with no *"outside the
> band"* there is no shark fin, no blood in the water, and nothing to trade. **`D-030` forbids
> substituting Dean Malone's shipped defaults**, and `[00:07:20]` *"I've altered it or tweaked it
> a little bit"* is the lesson's own reason why doing so would reconstruct a different indicator.
>
> ### ⚠️ A CORRECTION THIS SESSION MADE TO ITSELF, RECORDED RATHER THAN APPLIED SILENTLY
>
> The first draft of the H2 row read *"and independently blocked by `D-006`"*. **That citation is
> wrong and was corrected on checking the decision.** `D-006` defers **automated backtesting,
> Pine Script and optimisation** to Phase 8; it says nothing about placing demo orders.
>
> **The accurate statement is weaker and is the one that stands:** H2 is real-time forward
> testing, `16_FORWARD_TEST/` is empty until its phase is reached, and **the project has no
> standing decision forbidding a demo order.** So H2 rests on **one** blocker — `A-039`/`A-086` —
> not two. **The convenient second blocker was not available and the record says so**, because a
> deferral propped up by a mis-cited decision is worse than a deferral with one honest reason.

---

## 1. WHAT WAS DONE INSTEAD — a bounded demonstration of the blocker

`05_HOMEWORK/V11/V11_HOMEWORK.md` §3 set the precedent: where an assignment is blocked, **perform
a bounded demonstration of the blocker rather than a substitute for the assignment.**

**`PT-040` is that demonstration, and it is more than a gesture.** It asks the narrowest possible
version of H1's question — *can this session even construct the line the drill is about?* — and
answers it **quantitatively and in the negative**:

```text
PT-040:  side disagreement between RSI(21) and MA_k(RSI(21)) at every threshold
         V11 prints, 24,730 M15 bars, W-A / D-031 Arm A
         M = 10.481 pp at k=5, t=50.  Even k=2 gives 5.16 pp at t=50.
         Pre-registered verdict band: MATERIAL.
```

**The drill cannot be simulated because the series it is run on is not determined**, and that is
now a measured fact with a pre-registered decision rule behind it rather than an assertion.
See `06_MANUAL_BACKTEST/V12/BT_V12_0001.md`.

---

## 2. ⚠️ TWO DEFECTS IN THE ASSIGNMENT AS GIVEN — recorded, not smoothed over

### 2a. The quantity is stated twice and differs

| Timestamp | Quantity |
|---|---|
| `[00:42:23]` | *"I want you to do **about four** of those"* |
| `[00:43:05]` | *"I want you to do **five** of those"* |

**Forty-two seconds apart, neither corrected.** A third figure appears for the *trades* — *"at
least **five** times… if you're having fun with it do it more"* `[00:47:02]`, and *"do **five or
ten** trades"* `[00:47:59]`.

**Not filed as a `C-xxx`.** `C-007`'s precedent is for a count that changes what a **claim**
asserts; this is a self-directed practice quantity with no downstream dependency. **Recorded here
as "four or five — the lesson says both"**, which is what a student following the recording would
have to conclude.

### 2b. ⭐ The lesson supplies a stop distance and then declines to supply one

Forty minutes before the assignment, V12 prints **and** speaks a stop rule:

> Printed, frame `29:11`: *"Enter The Trade **Stop Loss 23 Pips above the HOD**"*
> Spoken `[00:30:33]`: *"stop loss 23 pips above the high"*

Asked directly, for the drill:

> `[00:48:15]`–`[00:48:54]`: *"**what size stop loss, Aaron? You tell me** what size stop loss…
> Do you think you caught the second leg, it should be what? … some are saying **10, 23, 25** —
> you guys **take a guess, figure it out**… **seven, ten sounds great**"*

**The lesson that printed `23` will not restate `23` when asked.** This is `A-066`'s standing
problem — a stop size with no rule for choosing it — **appearing inside the lesson that supplied
the corpus's one well-anchored stop distance**, and it is the main reason
`V12_INTERPRETATION.md` Q4 declines to discharge `A-066` on the `23`.

**It also bears on the printed-vs-spoken precedence question** V10 carry-forward (f) puts to the
owner: this is neither agreement nor contradiction but **abandonment** — a third polarity, logged
at `V12_INTERPRETATION.md` Q7 row 2.

---

## 3. H6 — PERFORMED

**The one item in this lesson's homework that this session could actually do**, because it is a
platform procedure rather than a trading instruction.

The instructor reads a student's method from the chat and endorses it verbatim
(`[00:47:36]`–`[00:47:48]`):

> *"**Water** was kind enough to tell us how to do this. Maybe I'll post that in the forum, make it
> sticky. Says: **make the candles invisible — set to line graph instead of candles or bars, then
> F8 for properties, and give the line graph the same color as the background color.** Yes, that's
> how you do it."*

**Recorded and verified as a coherent MT4 procedure:** `F8` is MetaTrader 4's Chart Properties
shortcut, and the Colors tab exposes `Line graph` as a settable colour; setting it equal to
`Background` renders the price plot invisible while the sub-window indicator continues to compute
on the underlying closes. **The method is sound and it is the student's, not the instructor's.**

> ### ⚠️ ONE NOTE ON THE NAME, BECAUSE IT IS A TRAP
>
> The ASR renders the contributor's name as ***"Water"***. **`water` is also the corpus's nickname
> for the 50 moving average** (`D-043`), and it occurs **21 times** in this lesson, almost all of
> them referring to *"blood in the water"* and *"the water line"*. **This instance is a person.**
> Recorded so that a future token census of `water` across V12 does not miscount this line as a
> moving-average reference — the same class of measurement trap `Q-013` §0 records twice.

**Not performed:** the drill the method enables (H2). Blocked as above.

---

## 4. STANDING WORK CARRIED FROM EARLIER LESSONS, RE-CHECKED AGAINST V12

| Item | Status after V12 |
|---|---|
| **The flashcards** (V11 H3, `DEFERRED` on `A-082`) | ⭐ **UNBLOCKED AS TO SPECIFICATION, STILL DEFERRED AS TO CONTENT.** `A-082`'s premise was **false** — V03 `[00:40:57]`–`[01:06:55]` teaches them: **40 cards, 15-minute default, labelled, winners only**, generalised to the trader's own entry timeframe. See `V12_SOURCE_NOTES.md` §9a. **They remain deferred because what goes ON a card is *"identify"* the setups, and those setups are `A-011`, `A-002`, `A-007` and `A-076` — all open.** The blocker moved; it did not lift |
| **V11 H6** — open the sub-graph and watch the 80/40 ↔ 60/20 switch (`DEFERRED` on `A-080`) | ⛔ **STILL DEFERRED — and the blocker has MOVED, not lifted.** `A-080` is **closed** (RSI = 21) and the drill is still not performable, because `PT-040` shows the smoothing ambiguity is `MATERIAL` at exactly the thresholds this drill is about. **`A-084` replaces `A-080` as the blocker on this item.** `BT_V12_0001.md` §7 |
| **V11 H4** — the five `Trade Strong` commitments | **RE-AFFIRMED BY V12.** `[00:03:05]` *"I need you guys to step it up and **trade strong**"*; `[00:24:36]` *"I need you guys to stop taking crap and I need you to **trade strong**"*. No new commitment is added |
| **Two hours a week on charts** (V11 H1) | **PERFORMED.** This session spent substantially more than two hours on GBP/USD M15 data and on the V12 frame set |

---

## 5. WHAT A STUDENT WITH THE TEMPLATE COULD DO THAT THIS SESSION CANNOT

Stated plainly, because it is the honest shape of the gap and it is not a failure of effort:

**A 2012 bootcamp student had the `.tpl` file.** `[00:07:38]` — *"the way it's **preset in the
templates** is the way I want us to learn how to use it"* — and `[00:55:02]`, where the instructor
offers to mail *"the old student folder"* to anyone who has lost it. **For them, every parameter in
`A-039`, `A-085` and `A-086` was a right-click away and never needed saying.**

**That is why the corpus does not contain them, and it is why this homework is deferred rather
than failed.** The one parameter that *did* get said — `RSI = 21` — was said only because the
instructor had **changed** it from the shipped default and wanted the group to know why
(`[00:07:24]`–`[00:08:22]`). **The corpus records the deviations, not the settings.**

**The cheapest thing that would unblock H1–H4:** a single frame, in **any** lesson V13–V21, showing
the TDI's properties dialog — or one sentence naming the smoothing length. **V12 was predicted to
be that place and was not** (`04_SCREENSHOTS/V12/INDEX.md` §1: no dialog exists in 672 frames).
