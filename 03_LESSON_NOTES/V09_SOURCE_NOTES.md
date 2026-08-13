# V09 — SOURCE NOTES

**Lesson:** V09 — **no title printed in the recording** (see §1)
**Source file:** `Bootcamp1 Wk2 032612 Part4 (53mins).swf`
**SHA-256:** `b0f36b5540de7a76397c80202cf6a721a2a18aa9011c5698238c6bcc624168d4`
**Session date:** 2012-03-26 (Week 2, Part 4) — shared with V06, V07, V08
**Runtime:** 00:52:26 (3146.815 s measured)
**Transcript:** `02_TRANSCRIPTS/V09/V09_TRANSCRIPT.md` — 721 markers, verified on four axes

---

## 0. PROCESS DISCLOSURE — THE EVIDENCE ORDER DEVIATED, AND IT IS DISCLOSED RATHER THAN CONCEALED

`SWF_CAPTURE_RECIPE.md` §9 requires source notes to be written **from the transcript alone**,
before the screenshots are looked at, so a reviewer can see which conclusions survive on audio
alone. **V08 met that standard with two disclosed exceptions. V09 does not meet it, and the
honest statement of what happened is this:**

| Step | Order in which it actually happened |
|---|---|
| 1 | The **full transcript was read end to end** and this session's reading of the lesson was formed from it — before any frame existed, because no frame existed yet |
| 2 | The capture ran. Its **mandatory** checks required looking at frames: `GOTCHA 4`'s content sanity check, and then — after the first sweep silently produced 638 splash frames — a diagnostic pass to find out why |
| 3 | `QUARANTINE_REGISTER.md` **`Q-010`** was written. Auditing a fabricated `VISUAL_INDEX.md` **requires opening the images**; there is no transcript-only version of that check |
| 4 | `04_SCREENSHOTS/V09/INDEX.md` was written, which requires reading every curated frame |
| 5 | **This file was typed.** |

**So §§1–13 below were composed by a session that had already seen the slides.** Claiming
otherwise would be false, and the project's own standard (`V05` R1 `M4` — *"two files written in
the same session asserting contrary things about that session's own process"*) makes that
exactly the wrong thing to do.

**What is done instead, and it is stronger than a claim about ordering.** Every substantive row
below carries an explicit **basis** tag:

| Tag | Meaning |
|---|---|
| `AUDIO` | Established by the transcript alone. Would stand if no frame had ever been captured |
| `PRINTED` | Established by slide text. The audio may echo it, but the slide is the evidence |
| `AUDIO+PRINTED` | Both, independently |
| `VISUAL` | Established only by looking at a rendered frame |

A reviewer can therefore do the thing the ordering rule exists to enable — **strike every
non-`AUDIO` row and see what is left** — without relying on this session's word about when it
looked at what. **§9 records the one place where a slide corrected a reading formed from
audio**, and the audio reading is left standing beside it.

---

## SPEAKER TAG — READ BEFORE ANY ROW BELOW

| Tag | Runtime | Meaning |
|---|---|---|
| `GUEST` | **00:00:00 – 00:52:23 — 100%** | A presenter who is not the course author |
| `INSTRUCTOR` | **none** | The course author does not speak in this lesson |
| `AUDIENCE` | brief, `[00:41:25]` onward | Named participants asking questions: *Fred*, *Harvey*, *Susan*, *Card/Carl* |

**Every substantive row in this file is `GUEST`.** Under **`D-033`** that tag **demotes
nothing** — the material is **NORMATIVE evidence at equal weight**, may define rules, and may
close an `A-xxx` or `C-xxx` record on its own. The tag is carried because `D-033` provision 1
keeps attribution mandatory.

**V09 is the fifth consecutive lesson with zero course-author runtime** (V05–V09). The
identification evidence, including the confirmation that this is V08's presenter continuing the
same talk, is in the transcript header and is not repeated here.

> **One `GUEST` statement in this lesson is a self-limiting disclaimer and it matters later.**
> `[00:42:16]` — *"**Steve doesn't teach it.** It's okay. This is my my twist on it. Just what
> I'm bringing to the table."* See §9 for what it does and does not scope.

---

## 1. LESSON OVERVIEW

**No title is printed.** Unlike V07 (which printed `03-26-2012`) and V08 (which printed *"Jim's
Journey in Learning and Trading MMFX"*), this recording opens with **no title slide** — the file
begins with the presenter already speaking over the previous session's closing diagram. **No
title is asserted anywhere in this project's V09 artifacts.**

The lesson has **two structurally distinct halves**, and they are unlike each other:

| Part | Runtime | What it is |
|---|---|---|
| **A — the defined-risk lecture** | `[00:00:00]` – `[00:27:28]`, ~52% | A prepared slide deck on **position sizing and risk**, delivered from printed text. This is **V08's announced but missing "section 3"** |
| **B — the DMR chart walkthrough** | `[00:27:30]` – `[00:52:23]`, ~48% | A live MetaTrader session calling **level counts and directional biases on twelve pairs**, followed by audience Q&A |

**Part A is the most operationally complete material in the corpus so far, and it is the first
of its kind.** V01–V08 supply pattern language, session structure, entry location and — in V08 —
a claimed 3:1 payoff. **None of them says how much to trade.** V09 does, in a closed formula,
with worked arithmetic, printed on slides.

**Part B is the opposite**: it is dense, fluent, and almost entirely uncodable, because it
applies a level-counting scheme the course has never defined (`A-004`) to charts, live.

---

## 2. THE DEFINED-RISK SYSTEM — THE CORPUS'S FIRST POSITION-SIZING RULE — `GUEST`

### 2a. The definition of risk

| # | Statement | Marker | Basis |
|---|---|---|---|
| 1 | *"Risk in forex is defined as what percent of your account balance would be lost if your trade went to stop loss?"* | `[00:01:17]`–`[00:01:21]` | `AUDIO+PRINTED` (frame burned `01:15`) |
| 2 | *"What makes the risk defined is the lot size we choose to put on."* | `[00:01:53]` | `AUDIO+PRINTED` (frame burned `02:05`) |

**This is a definition, not a heuristic**, and it is the first time the corpus supplies one for
any quantity.

### 2b. The formula — stated in words, printed, and arithmetically closed

> `[00:02:00]`–`[00:02:03]` *"We multiply our account balance by point O2 and divide our stop
> loss and pips into that number that will determine the lot size."*
> Printed (frame burned `02:05`): *"We multiply our account balance by **.02** and divide our **Stop Loss in
> pips** into that number. That will determine the lot size."*

```text
risk_dollars = account_balance × 0.02
lot_size     = risk_dollars ÷ stop_loss_pips        [in $/pip terms]
```

**The worked example, and it reconciles exactly** (`[00:02:25]`–`[00:02:38]`, `AUDIO+PRINTED`):

| Input | Value |
|---|---|
| Account | $12,500 |
| × 0.02 | **$250** — *"that would equal 2% of this account balance"* |
| ÷ 25-pip stop | **$10 per pip** |
| Stated result | *"that gives us **10 minis or one lot** to trade"* |

$10/pip is one standard lot on a USD-quoted pair, and 10 mini lots is the same size. **The
arithmetic is correct and internally consistent.** This is checked, not assumed —
`05_HOMEWORK/V09/scripts/verify_v09_arithmetic.py` re-derives every number V09 states.

> **`A-065` is opened on the `0.02` itself.** He gives it as *"2% is a good place to start"*
> (`[00:08:28]`, `PRINTED`, frame burned `08:20`) and never states a rule for choosing a different one. The
> constant is **explicit**; the **policy governing it is not**. Per `D-010` this is recorded and
> not coded.

### 2c. The loss-recovery cycle — the operative rule

Printed in full on the frame burned `08:20` (`[00:08:20]`–`[00:08:43]`, `AUDIO+PRINTED`):

| Event | Action |
|---|---|
| Loss 1 | *"come back with the SAME LOT SIZE"* |
| Loss 2 | *"come back with the SAME LOT SIZE"* |
| Loss 3 | *"come back with the SAME LOT SIZE"* |
| **Loss 4** | *"**re calculate LOT SIZE** as you are now down 8% of Original Account Balance"* |
| **Any win** | `[00:07:14]` *"after each win we recalculate our lot size based on two percent risk of balance at stop loss"* |

**Rationale, in his words** (`[00:05:36]`–`[00:05:40]`, `AUDIO+PRINTED`): *"If our balance is
only set back two percent at each loss we are sure to avoid margin issues for the third or
fourth trade which will be the one that negates the loss."*

**Direction of travel, stated as the summary of the whole system** (`[00:09:14]`–`[00:09:23]`,
`AUDIO+PRINTED`, frame burned `09:20`): *"as you hit winning trades you **increase** your lot size and as you
hit losing cycles of three or four consecutive stopouts you **diminish** your lot size."*

**The recalculation is worked, and it reconciles** (`[00:06:01]`–`[00:07:14]`,
`AUDIO+PRINTED`, frames burned `06:00` and `07:05`):

| Step | Value | Check |
|---|---|---|
| Start | $12,500 | |
| After 4 losses at 2% | *"12,500 is now 11,500"* | 4 × $250 = $1,000. **$11,500 ✓** |
| Drawdown described as | *"down eight percent of original equity"* | $1,000 / $12,500 = **8.0% ✓**. The slide burned `06:00` prints *"drawn down **to** 8% of original equity"*, which literally says the balance IS 8%; the audio's *"down eight percent"* is the right sense. **Loose wording, correct arithmetic — recorded here, not registered as an ambiguity** |
| New size | *"two percent of 11,500 is 9.2 minis or 0.92 lots"* | $230 / 25 pips = **$9.20/pip ✓** |
| First 2:1 winner | *"will bring us back up to 11,960"* | $11,500 + (50 × $9.20) = **$11,960 ✓** |
| Second winner | *"brings the account balance up to 12,500"* | $11,960 × 0.02 / 25 = $9.568/pip; +50 pips = $478.40 → **$12,438.40**, not $12,500. **Off by $61.60 — see `C-014`** |

> *(Superseded text, retained per `REMEDIATION_PROTOCOL.md` §2 — the two rows above previously
> read *"**2%** of 11,500 is 9.2 minis or 0.92 lots"* and *"**brings** us back up to 11,960"*.
> `[00:06:52]`–`[00:06:55]` reads *"**two percent** of 11,500 is 9.2 minis or 0.92 lots"* and
> `[00:07:03]` reads *"our first-winning winning trade **will bring** us back up to 11,960"*.
> Neither arithmetic check moves. Found by `05_HOMEWORK/V07/scripts/verify_quotes.py V09`, the
> sweep `V09_REVIEW_R2.md` open item **81** required; the numeral-for-word and tense
> substitutions are the same `E01` class as `V09_REVIEW_R1.md` `M1`.)*

### 2d. Cumulative exposure — the rule that is easiest to miss

`[00:19:18]`–`[00:19:43]`, `AUDIO+PRINTED` (the five-errors frame, burned `21:40` — error 2):

> *"When I say two percent of risk on your account I don't mean two percent GJ two percent GU
> two percent EU another two percent UJ… Talking about a **cumulative risk that's never greater
> than two percent across your account**. If you're looking at three pairs to trade you want to
> carve that lot size in three to come out to two percent. Your overall exposure should be two
> percent."*

**This is a portfolio-level constraint, not a per-trade one**, and it is stated twice — once in
speech and once as printed error #2. It materially changes the meaning of everything in §2b.

---

## 3. THE TWO RISK-TO-REWARD GEOMETRIES — `GUEST`

| Geometry | Stop | Target | Gate | Markers | Basis |
|---|---|---|---|---|---|
| **Beginner — 2:1** | **25 pips** | **50 pips** | *"Until one develops the HOD/LOD SKILL"* — **the PRINTED wording** (frame burned `04:40`). The audio says *"high low-day"* | `[00:04:49]`–`[00:04:55]` | quoted string is `PRINTED` (frames burned `04:40`, `10:15`); the rule itself is `AUDIO+PRINTED` |
| **Ideal — 3:1** | **15 pips** | **50 pips** | *"Mastering **HOD/LOD** entries"* — **the PRINTED wording** (frame burned `03:45`). The audio says *"high low-day"* | `[00:03:33]`–`[00:03:56]` | quoted string is `PRINTED` (frames burned `03:45`, `11:40`); the rule itself is `AUDIO+PRINTED` |

> **The printed slides resolve an ASR garble, and it is the most useful single thing the frames
> supplied.** The transcript renders the gate as *"high low-day"* / *"high-low"* throughout.
> The frames burned `03:45` and `04:40` print **`HOD/LOD`** — High Of Day / Low Of Day, a term the corpus already
> carries from V08's high-low drill. **This is the V01 *"pendings"* case exactly.**
>
> **⚠ AND THE EXPANSION MAY NOT BE CARRIED INSIDE A QUOTATION OF THE AUDIO.** Corrected
> 2026-08-13 per `V09_REVIEW_R1.md` `M1` (`E01`, open item 73). Every quotation below that is
> tagged `AUDIO` now carries the transcript's literal wording, with the expansion **outside** the
> quote marks. Where the printed form is what is being quoted, the row says so.

**His own arithmetic on the 3:1 arm** (`[00:03:49]`–`[00:04:05]`, `AUDIO`, transcript wording
verbatim): *"Example solid high low-day entries can warrant a 15-pip stop loss. Three stop outs
is then minus 45 pips, one win is plus 50 pips, that nets out to plus five pips."* — *high
low-day* is the ASR's rendering of **HOD/LOD**, printed on the frame burned `03:45`. **The arithmetic is correct**,
and note it is 50/15 = **3.33:1**, described as *"3:1"*. Recorded, not corrected.

> *(Superseded text, retained per `REMEDIATION_PROTOCOL.md` §2 — this paragraph previously read
> `**His own arithmetic on the 3:1 arm** (`[00:03:49]`–`[00:04:05]`, `AUDIO`): *"Example solid
> HOD/LOD entries can warrant a 15-pip stop loss…"*`, i.e. it substituted the printed expansion
> for the spoken words **inside quotation marks under an `AUDIO` tag**. The substitution was
> explained in the box above and was still a misquotation. `V09_REVIEW_R1.md` `M1`.)*

**Break-even, computed here and stated as this project's arithmetic, not his:** at 2:1 the
break-even hit rate is 33.3%; at 3:1 it is 25%; at 3.33:1 it is 23.1%.

> ### `A-067` — *"greater than 50% accuracy will bring UPWARD EQUITY"* is TRUE, and it is not the threshold
>
> `[00:15:36]`, printed on the frames burned `16:00` and `17:05`. It is a **sufficient** condition presented in the
> rhetorical position of a **necessary** one — *"I gotta just stop this whole thing and freeze
> this frame"* `[00:15:43]`. The frame at `00:15:00` prints the correct weaker claim one slide
> earlier: *"Can have **MORE Losers than Winners** and still have UPWARD EQUITY"*. **Both are
> his, one slide apart. The register records the gap, not a correction.**

---

## 4. THE EQUITY-CURVE DEMONSTRATIONS — `GUEST`

Four hand-drawn staircases, each a claim about win/loss ratios under a stated geometry.

| # | Marker | Geometry | Stated record | Arithmetic check (this project's) |
|---|---|---|---|---|
| 1 | `[00:10:35]` | 2:1 (−25/+50), frame burned `10:15` | *"eight wins and 11 losses"* | 8 × 50 − 11 × 25 = **+125 pips ✓ positive** |
| 2 | `[00:11:17]` | 3.33:1 (−15/+50), frame burned `11:40` | *"seven wins and 12 losses"* | 7 × 50 − 12 × 15 = **+170 pips ✓ positive** |
| 3 | `[00:12:06]` | *"jumping out when it hits you 15"* | *"six wins and 14 count them 14 losses"* (`[00:12:06]`); restated *"six wins 14 losses"* (`[00:12:38]`) | **Under-specified** — see below |
| 4 | `[00:22:47]` | 2:1, frame burned `22:45` | *"an **85 win rate**… seven wins and six losses"* | 7/13 = **53.8%. See `C-012`** |

**Demonstration 3 is the one that does not close, and it is recorded as an ambiguity rather than
an error.** `[00:11:41]`–`[00:11:46]` describes taking 15 pips *out* (*"you're jumping out when
it hits you 15, take your 15 out"*), which reads as a **15-pip target**, while the staircase is
introduced under the HOD/LOD 15-pip **stop**. With a 15-pip stop and a 15-pip target, 6 wins and
14 losses is **−120 pips**, i.e. **negative**, contradicting *"you still had a net positive
equity curve"* `[00:12:12]`. Under the −15/+50 geometry of demonstration 2 it is 6 × 50 − 14 × 15
= **+90 pips, positive**. **The lesson does not state which**, so this project does not choose:
recorded as **`A-068`**, `DO NOT CODE`.

---

## 5. THE FIVE ERRORS TO GUARD AGAINST — `GUEST`

Printed complete on the frame burned `21:40`, spoken `[00:18:31]`–`[00:22:40]`. `AUDIO+PRINTED`.

| # | Printed text | Spoken gloss |
|---|---|---|
| 1 | *"Moving your Stop Loss After you have placed it: 1st S/L is always the cheapest"* | `[00:18:48]`, attributed to a named participant: *"the seebull always says the first stop loss is always the cheapest"* |
| 2 | *"Putting on Multiple Positions which add up to GREATER than your % Risk"* | `[00:19:13]`–`[00:19:40]` — the cumulative-2% rule of §2d |
| 3 | *"Not having the DISCIPLINE to KEEP TO the Risk Plan as described"* | `[00:19:48]`–`[00:20:27]`, framed as V08's **innermost ring**: *"that inner shell has like I don't know what it's it's titanium or diamond… it's the circle within the circle"* — the doubled *"it's"* is the speaker's own stutter and is left standing (`V09_REVIEW_R1.md` `M1`; it previously read *"what it's titanium"*) |
| 4 | *"Miscalculating Lot size on NON USD quote Pairs -- use a lot size calculator!"* | `[00:20:48]`–`[00:21:31]` — *"USD JP why on a USD based account is going to be a larger unit than a pair that ends in USD"*. The ASR renders **USD/JPY** as *"USD JP why"*; the reconstruction is stated here rather than inside the quote (`V09_REVIEW_R2.md` item 81; it previously read *"USD JPY on a USD based account"*) |
| 5 | *"Not having HARD Stop Losses and Take Profits WITH THE BROKER"* | `[00:21:44]`–`[00:22:40]` — explicitly against stealth-EA stop management; *"there's going to be times where your platform goes down"* |

**Error 3 is the answer to V08's unanswered question.** V08's final frame is a red `?` at the
centre of a four-ring model and the file cuts before he says what is in it. **V09 says: the
innermost ring is discipline in keeping to the risk plan.** This is `AUDIO`, and it is the
single most important cross-file result in this lesson.

---

## 6. THE EQUITY PROJECTION — `GUEST`

`[00:24:20]`–`[00:26:40]`, `AUDIO+PRINTED` (frames burned `25:00`, `26:00`, `26:40`).

| Component | Value |
|---|---|
| Risk at stop | 2% |
| Geometry | 2:1 or greater, −25 / +50 |
| Per trade | **−2% on a loss, +4% on a win** |
| Claim | `AUDIO` `[00:24:52]`–`[00:24:55]`: *"only **five successful trades per week**… it brings **20% gains**"*. `PRINTED`, frame burned `25:00`: *"Only FIVE successful trades per Week = 20% Gains for the Week!"* |
| Compounding | *"In four weeks you doubled your account with a $5,000 account. You now have 10,000 368"* |
| Spreadsheet (frame burned `26:40`) | `Base 5,000.00`, `% profit 0.2000`, Week 4 = `10,368.00`, running 28 weeks to **`824,223.31`** |

> *(Superseded text, retained per `REMEDIATION_PROTOCOL.md` §2 — the Claim row previously read
> *"only **five successful trades per week** brings **20% gains** for the week"*, which is
> neither source verbatim: it drops the audio's *"it"* and imports *"for the week"* from the
> slide. Both sources are now quoted separately and the claim is unchanged. Found by the item 81
> sweep.)*

**Arithmetic check:** 5 × 4% = 20% ✓. $5,000 × 1.2⁴ = **$10,368.00** ✓ exactly. The 28-week
terminal value is $5,000 × 1.2²⁸ = **$824,223.31** ✓ exactly.

> **`C-013` — every number above is right and the projection is still not reachable from this
> lesson's own premises.** The table compounds 20% per week for **28 consecutive weeks with no
> losing week and no losing trade**, inside a lesson whose four worked demonstrations are 8W/11L,
> 7W/12L, 6W/14L and 7W/6L, and whose printed headline one slide earlier is *"Can have MORE
> Losers than Winners and still have UPWARD EQUITY"*. He states the loss cost himself —
> `[00:24:46]` *"4% per trade if we get it, **2% if we don't get it**"* — and then omits it.
> **This is logged as a contradiction in the lesson, not as an arithmetic error, because the
> arithmetic is exact.**

---

## 7. PART B — THE DMR CHART WALKTHROUGH — `GUEST`

A live pass over **twelve pairs**, calling a **level count** and a directional bias on each.

### 7a. The chart furniture he names

| Object | Marker | What he says | Basis |
|---|---|---|---|
| **Weekly divider** | `[00:28:11]` | *"I divide the week with a weekly divider. **I draw in by hand.** We do have an indicator in process to be made that will do this for us"* | `AUDIO`; visible on the frames burned `28:45` and `31:50` |
| **High-low tracer** | `[00:28:19]` | *"our days are depicted by the **high low tracer** as you can see monday tuesday wednesday thursday friday"* | `AUDIO` |
| **The grape / the blueberry** | `[00:33:21]`, `[00:41:25]`–`[00:42:16]` | See §9 | `AUDIO` |

> **`A-069` — *"high low tracer"* is named and never defined.** It is a per-day marking on his
> chart. Whether it is an indicator, a template object or hand drawing is not stated. **The
> corpus has a `tracer` reference in the `D-039` gap list already** — `MMM-NOTES` contains
> **zero** occurrences of *tracer* in 84 pages (`SOURCING_HIERARCHY.md` §2 step 3 negative
> result). Tier 1 and Tier 2 are both silent. `DO NOT CODE`.

### 7b. The twelve calls, as given

Recorded because a level-count call is an **observation of his method in use**, and because
`[00:39:43]`–`[00:41:13]` is a clean recap he gives himself.

| Pair | Call | Marker |
|---|---|---|
| EUR/USD | Level 1 long | `[00:39:48]` |
| EUR/JPY | Level 2 long | `[00:39:53]` |
| EUR/CAD | Level 2 long, *"with a three looming very close by"* | `[00:39:59]` |
| GBP/USD | Level 1 long | `[00:40:05]` |
| GBP/JPY | Level 2 long | `[00:40:10]` |
| GBP/CHF | Level 3 long | `[00:40:15]` |
| AUD/USD | Level 3 **down** | `[00:40:21]` |
| AUD/JPY | Level 2 up, *"take with a green [grain of] salt"* | `[00:40:28]`–`[00:40:36]` |
| USD/CHF | Level 3 long | `[00:41:07]` |
| USD/CAD | Level 2 **down** | `[00:41:13]` |

**Two pairs discussed but not in the recap:** USD/JPY (`[00:35:31]`, explicitly excluded from the
DMR — see §11) and the `GF`/`UF` charts shown in the tile view (frame burned `41:25`).

**None of this is codable and none of it is offered as such.** The count depends on
`A-004` (*"level"* as a countable unit), which the course has still not defined at V09.

### 7c. Level-3 characteristics — the one generalization in Part B

| Statement | Marker | Basis |
|---|---|---|
| *"Lot of volume always at level three. It's characterized by heavy volume and big moves both direction"* | `[00:30:34]` | `AUDIO` |
| *"Level three is always characterized by expansion and acceleration"* | `[00:33:53]` | `AUDIO` |

**Two `always` claims about level 3, 200 seconds apart, with compatible content.** They are
recorded as stated. **They are not testable**, because `A-004` leaves *level* undefined —
`D-030` binds and this project does not approximate it. Logged as **`A-070`**.

### 7d. The market-maker cycle and the "dinosaur pattern"

`[00:34:18]`–`[00:34:48]`, `AUDIO`:

> *"the caveat to all of this is our lovely **market maker cycle**… we all know what that is
> right, I don't need to draw that out for you guys, but because I'm crazy I will… **the dinosaur
> pattern**… This pattern can always impose itself on the week. Our level count many times will
> have to change."*

> **`A-071` — *"the dinosaur pattern"*.** A named object, drawn live in MS Paint, described only
> as something that *"can always impose itself on the week"* and force a level-count change. He
> says *"we all know what that is"* and does not restate it. **Tier 2 is silent:** `dinosaur`
> occurs **0×** in `MMM-NOTES`'s 84 pages. `DO NOT CODE`.

**One mechanism statement inside it is worth preserving verbatim** (`[00:34:59]`, `AUDIO`):
*"these guys don't move it much between these two areas because they're **killing people on this
side** and they're **killing people on this side**."*

### 7e. Inducement — a three-push description, and the trap it sets

`[00:44:29]`–`[00:44:48]`, `AUDIO`:

> *"When the market makers start their cycle, **induce once, induce twice, induce the third
> time**. We want to try to get people long. They form a pin up here because they're going to
> pull it back the other way and they're going to grab their pips, and experiences show me that
> they can grab all their stuff at **50 pips**"* (`[00:44:44]`).

> *(Superseded text, retained per `REMEDIATION_PROTOCOL.md` §2 — this quotation previously read
> *"…and **experience shows** me…"*; the transcript reads *"**experiences show** me"*. Nothing
> turns on it, and an `AUDIO`-tagged quotation may not be tidied. `V09_REVIEW_R1.md` `M1`.)*

`[00:46:28]`, `AUDIO`: *"I honestly look more towards **inducements, which would be three pushes,
three accelerations, the third being the longest**."*

> ### ⚠ THIS DOES NOT UNBLOCK `push`, AND SAYING SO IS THE POINT
>
> *"three pushes… the third being the longest"* is the most specific statement about push
> structure anywhere in V01–V09, and it is **still not a recognition rule**. It says nothing
> about how large a push is, how it is delimited, what separates a push from noise, or how any
> of it is identified **before** the third one has happened. **`D-030` binds, `D-033` does not
> relax it, `D-039`/`D-040` do not relax it, and V05/V06/V07 dimension B stays BLOCKED.** This
> is recorded in `A-072` as an **extension** of the push record, explicitly **not** a closure —
> the exact over-reach `D-039`'s own text refuses in advance.

---

## 8. NUMBERS STATED IN V09 — `GUEST`

Every number, with its status. **None is a machine rule** (`D-010`).

| Value | What it governs | Marker | Status |
|---|---|---|---|
| **0.02 / 2%** | Risk per trade at stop loss | `[00:02:00]`, `[00:08:28]` | **EXPLICIT.** Policy for changing it: **absent** (`A-065`) |
| **2%** | *Cumulative* exposure across all open positions | `[00:19:29]` | **EXPLICIT** |
| **3 / 4** | Losses before lot size is recalculated | `[00:08:20]`–`[00:08:43]` | **EXPLICIT** |
| **8%** | Drawdown after four 2% losses | `[00:06:01]` | **EXPLICIT**, arithmetically exact. Slide wording is loose (§2c) |
| **25 / 50 pips** | Beginner 2:1 stop / target | `[00:04:55]` | **EXPLICIT** |
| **15 / 50 pips** | HOD/LOD 3:1 stop / target | `[00:03:49]`–`[00:03:56]` | **EXPLICIT** (stated as *"3:1"*, is 3.33:1) |
| **> 50%** | Accuracy said to bring upward equity | `[00:15:36]` | **EXPLICIT**, and sufficient-not-necessary (`A-067`) |
| **70%, 85%** | Illustrative accuracy figures | `[00:15:59]`, `[00:22:47]` | **ILLUSTRATIVE.** The 85% is `C-012` |
| **5 trades / week, 20% / week** | Target throughput and return | `[00:24:52]`–`[00:24:57]` | **EXPLICIT**, and `C-013` |
| **29** | Setups *"last week"* | `[00:10:06]` | **REPEATED FROM V08** — V08's own 29-setup gallery (`C-007`) |
| **50 pips** | What market makers *"can grab all their stuff at"* | `[00:44:44]` | **ANECDOTAL** — *"experiences show me"* (`[00:44:39]`) |
| **800 / 200** | The blueberry / the grape | `[00:41:43]`–`[00:41:48]` | **EXPLICIT.** See §9 |

> *(Superseded text, retained per `REMEDIATION_PROTOCOL.md` §2 — the `50 pips` row previously
> read *"**experience shows** me"*; `[00:44:39]` reads *"**experiences show** me"*. **This is the
> FIFTH instance of the `E01` class in this file and the SECOND of this exact phrase** — §7e's
> identical quotation was corrected at R1 while this one, 38 lines below it, was not, because
> the R1 remediation fixed the four sites it was pointed at by hand and did not run the sweep
> `V09_REVIEW_R1.md` `M1` also required. The file therefore contradicted itself about its own
> audio for one round. `V09_REVIEW_R2.md` open item **81**; now found mechanically by
> `05_HOMEWORK/V07/scripts/verify_quotes.py V09`.)*

---

## 9. THE MOVING-AVERAGE ANSWER — THE `SOURCING_HIERARCHY.md` §3.4 RECONCILIATION EVENT — `GUEST`

`SOURCING_HIERARCHY.md` §3.4 imposes a **standing obligation**: any session reaching a lesson
that touches *"the moving-average set"* **must** re-check `A-014`, `A-020` and `A-023` against
that lesson and run the §3.1 six-step process if Tier 1 speaks. **Tier 1 speaks here**, and this
section discharges that obligation for `A-020`.

### 9a. What the audience asked and what he answered

`[00:41:25]`–`[00:42:16]`, `AUDIO`, verbatim across five markers. **Two ASR artefacts are left
standing in the quotation and named outside it** — corrected 2026-08-13 per `V09_REVIEW_R1.md`
`M1`:

> *"What is the **grade** Fred? That's the name that I've given to the **800 moving average on
> the one hour chart**. Don't concern yourself with it. It's just my own little twist twist of the
> thing that will be **your blueberry** on your charts. Okay. This is the blueberry. **The
> blueberry is the 800 on the 15 minute time frame.** Okay, which makes this **a 200**. I
> synchronized my EMAs. I'm a little out of the box… I like to keep my EMAs consistent
> throughout all time [frames]. **Steve doesn't teach it.** It's okay. This is my my twist on
> it."*

| ASR rendering, left in the quote | The word | How it is established |
|---|---|---|
| *"the **grade**"* `[00:41:25]` | **grape** | The transcript itself renders it correctly twice — `[00:33:21]` *"We have the **grape** up here"* and `[00:41:31]` *"that will be your blueberry"* answering the same question. It is a one-letter ASR slip on a term the same file gets right elsewhere |
| *"my own little twist **twist**"* | a stutter | Left as spoken |

> *(Superseded text, retained per `REMEDIATION_PROTOCOL.md` §2 — this block previously opened
> *"What is the grape, Fred?"* and dropped the doubled *"twist"*, i.e. it silently corrected the
> audio **inside quotation marks** in a block that introduces itself as *"verbatim across five
> markers"*. The reading is unchanged; the quotation now is what it claims to be.
> `V09_REVIEW_R1.md` `M1`.)*

### 9b. What this establishes, and what it does not — the four claims separated

| Claim | Status | Why |
|---|---|---|
| **Blueberry = the 800, on the 15-minute** | ✅ **Tier 1, explicit.** `RESOLVED BY COURSE` for this half of `A-020` | Stated outright, unhedged, to an audience of students, as *"**your** blueberry"* — i.e. a shared course object, not his own coinage |
| **The timeframe is part of the definition** | ✅ **New.** `A-020`'s closure carried *"Blueberry = 800"* with **no timeframe** | *"800"* alone is ambiguous across charts; **15-minute** is the missing half |
| **The grape = the 800 on the 1-hour** | ✅ Stated — and **explicitly his own**, not course doctrine | *"the name that **I've** given"*, *"my own little twist"*, *"**Steve doesn't teach it**"* |
| **800-on-15m ≡ 200-on-1h** | ⚠️ **NOTED, NOT ADOPTED.** See below | It is arithmetically true (800 × 15m = 12,000 minutes = 200 × 60m) and he says it — but what it licenses is a separate question |

### 9c. Effect on `A-020` — a status change, made with the reading done

**`A-020` was closed on 2026-08-13 as `RESOLVED — OWNER ATTESTATION`, with its own text
insisting the distinction survive**: *"`RESOLVED BY COURSE` means a later lesson defines it
explicitly. **No lesson does.**"*

**A lesson now does.** Under `SOURCING_HIERARCHY.md` §3.2 **Case A** (*Tier 1 is clear and
specific*), the *Blueberry* row's basis is **upgraded from owner attestation to course
evidence**, cited `V09 [00:41:43]`. The superseded basis is retained per §3.1 step 4. **The
other four nicknames are untouched** — V09 says nothing about mustard, ketchup, water or mayo,
and `Mayo = 200` remains on owner attestation + `MMM-NOTES` p.66.

### 9d. Effect on `C-010` — it NARROWS, and it does not close

`C-010` records that `MMM-NOTES` enumerates the EMA set as *"the 5, 13, 50 and 200"* with **no
800 in 84 pages**, while the corpus uses *"blueberry"*.

| What V09 changes | What it does not |
|---|---|
| The corpus's 800 now rests on **Tier 1 course evidence**, not owner attestation alone. `C-010`'s resolution — *the recordings win* — is **strengthened** | It does **not** close `C-010` |
| It supplies a **candidate reconciliation**: if the notes' `200` is read on the 1-hour and the corpus's `800` on the 15-minute, **they are the same line** | The notes list `5, 13, 50, 200` as one set on one chart; nothing in Tier 2 says which timeframe. **Reading a timeframe into the notes to make them agree is exactly the blending `SOURCING_HIERARCHY.md` §3.2 forbids** |

> ### ⚠ AND THE CANDIDATE RECONCILIATION FAILS ARITHMETICALLY — ADDED 2026-08-13
>
> `V09_REVIEW_R1.md` `M5` (open item 77). The row above refuses the reconciliation on
> `SOURCING_HIERARCHY.md` §3.2's *"do not blend"*, which is correct. **There is a second and
> stronger reason.** The identity is a factor of four, so reading the notes' full enumeration
> `5, 13, 50, 200` on the 1-hour maps it onto the 15-minute as `20, 52, 200, 800` — and the corpus
> carries a **5, a 13 and a 50**, not a 20, a 52 and a 200. It also collides with `A-020`, whose
> mapping needs **mayo = 200 and blueberry = 800 to be two lines on one chart**. **One member of
> four lands.** Full working in `CONTRADICTIONS.md` `C-010` and `V09_INTERPRETATION.md` Q5, whose
> grade is downgraded `MEDIUM` → `LOW`.

**So `C-010` is annotated with the V09 evidence and stays OPEN.** Recording the candidate
reconciliation without adopting it is the whole of what this project's rules permit here.

### 9e. The one place a frame corrected an audio-formed reading — disclosed per §0

Working from the transcript alone, this session's first reading of `[00:42:16]` *"Steve doesn't
teach it"* was that it scoped **the 800 itself**, which would have made the corpus's 800 a
guest's private indicator and turned `C-010` on its head in the notes' favour.

**Reading the surrounding markers carefully — not a frame — corrected it**: *"that will be
**your** blueberry on your charts"* addresses the students' own charts, so the blueberry is
shared course furniture and what is *"his twist"* is the **synchronisation across timeframes**
and the **grape** name. **The original misreading is recorded here rather than deleted**, because
it is the kind of error that would have silently inverted a contradiction record.

---

## 10. VOCABULARY USED WITHOUT DEFINITION IN V09 — `GUEST`

Terms this lesson uses fluently and never defines. **All `DO NOT CODE`.**

| Term | Occurrences | Existing record |
|---|---|---|
| *level* (as a countable unit) | 50 markers | **`A-004`** — still open at V09 |
| *reset* | 16 markers | **`A-073`** — new; the count-restarting event, used constantly, never defined |
| *trap* / *trap area* / *trap volume* | 16 markers | Existing trap-move records; `[00:50:57]` adds *"that trap volume means what they sent the market down to get shorts committed this direction"* |
| *inducement* / *push* | 4 markers | **`A-072`** extension only — see §7e |
| *straightaway* | `[00:29:46]`, `[00:32:04]` | Existing |
| *peak formation* | `[00:32:32]`, `[00:38:00]`, `[00:39:21]` | Existing; all three are unglossed chart labels |
| *multi-day W* / *multi-week W* / *multi-week M* | `[00:29:33]`, `[00:32:45]`, `[00:35:41]` | **`A-011`** — still open |
| *high low tracer* | `[00:28:19]` | **`A-069`** — new |
| *dinosaur pattern* | `[00:34:44]` | **`A-071`** — new |
| *fractional disparity* | `[00:35:15]` | **`A-014`** — see §12 |
| *dominant pair* | `[00:42:47]`–`[00:43:09]` | **`A-074`** — new |
| *alternate count* | `[00:40:55]`, `[00:45:51]`–`[00:46:14]` | **`A-075`** — new |
| *DMR / DMOR* | 9 markers | A paid service, not a method term. Not registered |

---

## 11. WHAT V09 ASSIGNS — `GUEST`

| # | Assignment | Marker | Performable today? |
|---|---|---|---|
| **H1** | *"type in a lot size calculator, 4x lot size calculator, tons of free ones… I suggest you go get one"* — the ASR's *"4x"* is **forex** | `[00:02:56]`–`[00:03:16]` | **YES** — and it is checkable by arithmetic instead, which is what `05_HOMEWORK/V09` does |
| **H2** | *"go back, study it, do what you can… take notes heavily because this is everything"* — of the risk section | `[00:23:37]`–`[00:23:47]` | **YES**, and it is what this file is |
| **H3** | **The USD/JPY arrow drill.** *"take usd jpy for the specific reason that we don't cover it in the dmor… try to sus levels in it, and then at the end of every day he's going to pop in an arrow… in the direction that he thinks this bad boy is going to go, and then see what it does tomorrow… I'm going to pass that out to you guys"* — the ASR's *"dmor"* is **DMR** (§10 records both spellings) | `[00:47:57]`–`[00:49:01]` | **BLOCKED by `D-030`** — see below |
| **H4** | *"Slap some arrows on there and see what it does the next day"* — the same drill generalized to levels | `[00:51:31]`–`[00:51:43]` | **BLOCKED**, same reason |
| **H5** | Steve's week-1 assignment, referred to but not reissued: *"our homework from last week that Steve gave us was to mark up this chart"* (USD/CHF) | `[00:37:43]`–`[00:38:00]` | **Not V09's assignment.** Recorded as a pointer only |

> *(Superseded text, retained per `REMEDIATION_PROTOCOL.md` §2 — `V09_REVIEW_R2.md` open item
> **81**, found by `05_HOMEWORK/V07/scripts/verify_quotes.py V09`. **H1** previously read *"Type
> in a lot size calculator, **forex** lot size calculator, tons of free ones…"*; `[00:02:56]`
> reads *"**4x** lot size calculator"* — an ASR form silently expanded inside the quote marks.
> **H2** previously read *"…do what you can**,** take notes heavily…"*, joining `[00:23:37]` to
> `[00:23:43]` across the dropped words *"you know"* with a comma rather than an ellipsis.
> **H3** previously read *"…we don't cover it in the **DMR**…"* (`[00:47:57]` reads *"dmor"*)
> and *"…pop in an arrow **in the direction**…"*, joining `[00:48:13]` to `[00:48:18]` across the
> dropped *"hopefully bigger than that"*. **No assignment, marker or disposition changes** —
> H3/H4 stay `BLOCKED by D-030`.)*

> ### WHY H3/H4 ARE BLOCKED, AND WHY THAT IS NOT AN EXCUSE
>
> H3 is a genuinely well-designed exercise — a **daily committed directional prediction on a
> pair excluded from the paid service, scored the next day, done alone** (`[00:48:41]` *"I
> wouldn't even talk about it with anybody"*). It is a pre-registration discipline, and this
> project would ordinarily jump at it.
>
> **Its predictor is the level count, and `A-004` leaves *level* undefined.** Performing it would
> require this session to invent a level-counting rule, which is precisely `D-030`. An arrow
> placed by an invented rule produces a **number**, and a number acquires authority a note never
> does.
>
> **So the homework performs H1/H2 in full and substitutes NOTHING for H3/H4**, which are
> `DEFERRED` under `D-019` and carried until a lesson defines a level.
>
> **An earlier draft of this paragraph proposed running "H3's structure with one of V09's own
> explicit numbers as the predictor", and that was dropped.** V09's explicit numbers are risk
> parameters, not directional signals, and dressing one up as an arrow predictor would have been
> the `D-030` substitution wearing a disclosure. **The superseded text is retained above the
> change per `REMEDIATION_PROTOCOL.md` §2** — see the strikethrough note below.
>
> What `05_HOMEWORK/V09` §3 does instead applies the **same commit-before-you-look discipline** to
> something V09 specifies in full: its own sizing algorithm, executed literally on real trade
> sequences under four predictions committed in advance.
>
> <details><summary>superseded draft text, retained</summary>
>
> *"Instead `05_HOMEWORK/V09` runs the exercise H3's structure licenses without its blocked
> predictor: a committed, pre-registered, next-day-scored prediction whose predictor is one of
> V09's own explicit numbers. The substitution is declared there, not smuggled."*
>
> </details>

---

## 12. THE `SOURCING_HIERARCHY.md` §3.1 STEP 1 SWEEP — RUN BEFORE THIS FILE WAS WRITTEN

`SOURCING_HIERARCHY.md` §3.1 step 1 makes it a **required step of the study protocol** to grep a
new lesson's key terms against `EXTERNAL_VOCABULARY_REFERENCE.md` §5/§9.2 and
`AUTOMATION_AMBIGUITIES.md` before writing notes. Result:

| Term V09 uses | Tier 2 (`MMM-NOTES`, 84 pp.) | Disposition |
|---|---|---|
| *fractional disparity* | Present, p.52 — **`A-014` is `RESOLVED BY MMM-NOTES`** | **§3.2 Case D at best.** V09 `[00:35:15]` **uses** the term (*"somewhat against fractional disparity on euro USD and pound USD"*) and does **not** define it. Consistent with cross-pair level analysis; **adds no constraint**. `A-014` is **not reopened and not restated** — annotated only |
| *blueberry* / *800* | **0 occurrences** | §9. Tier 1 wins; `C-010` narrowed |
| *lot size*, *risk %* | **Present, pp. 50–51, 67** | **§13 — this is the substantive Tier 1 / Tier 2 divergence and it gets its own `C-015`** |
| *dinosaur*, *tracer*, *grape*, *reset*, *inducement*, *alternate count*, *dominant* | **0 occurrences each** | Negative results recorded (`SOURCING_HIERARCHY.md` §2 step 3). All stay `DO NOT CODE` |

---

## 13. TIER 1 vs TIER 2 ON RISK — THE MANDATORY CALL-OUT — `GUEST` vs `MMM-NOTES`

`D-039`'s owner direction is **mandatory, not permissive**: *"if at any time the videos
contradict the pdf then we can call it out."*

**The corroboration first, because it is real and it is the larger part.** `MMM-NOTES` p.67
prints a `RISK LEVEL` table whose arithmetic is **the same formula V09 states**: 1% of $100K =
$1,000, at a 10-pip stop = **10 lots**. That is `risk_dollars ÷ stop_pips`, exactly §2b.
**Tier 2 independently corroborates V09's position-sizing method**, and neither source cites the
other.

**The divergence is on the *policy*, and it runs in opposite directions:**

| | V09 (Tier 1) | `MMM-NOTES` (Tier 2) |
|---|---|---|
| Risk per trade | **2%**, flat | **1–3% when learning**, then *"when you are proficient (hitting 9 – 10), **increase the per trade risk to 5%**"* (p.67) |
| After losses | **Diminish** lot size at 3–4 consecutive stops `[00:09:23]` | Not addressed |
| Scaling in | Error #2: *"multiple positions which add up to greater than your % risk"* | A **5:4:3:2:1 scale-in** ladder is taught as *"a safer way of gaining profit"* (p.67) |
| Sizing philosophy | *"**No impulsive increases in lot size**"*; *"you will blow up accounts unless you work this way"* `[00:09:07]` | *"looking for the most pristine setups where there is maximum opportunity for **scaling in heavily and trading with high lot sizes without being concerned about losses**"* (p.50); *"you can afford to **trade heavily**"* (p.51) |

**Logged as `C-015`.** Under `SOURCING_HIERARCHY.md` §3.3 the **recording wins** and the note is
superseded **on this point** — but note the asymmetry `C-011` made concrete: V09's 2% sits
*inside* Tier 2's 1–3% learning band, so the **numbers** are compatible and only the
**escalation and scale-in policy** conflict. **Tier 2 is defeated on policy without being
defeated on the formula.**

---

## 14. WHAT V09 DOES **NOT** CONTAIN

Stated because absence is evidence, and because the quarantined `NOTES.md` asserts most of it.

- **No entry rule.** V09 never says when to enter. It says how much to trade once you have.
- **No stop *placement* rule.** It gives stop **sizes** (25, 15 pips) and never says where the
  stop goes relative to structure. **V08's promised stop-side payoff is only half delivered.**
  Registered as **`A-066`** — a stop size with no placement rule is not a stop rule.
- **No session times.** Six clock figures in the quarantined file; zero in the audio.
- **No TDI, shark fin, railroad track, pin bar, EMA cross, or 30–90-minute leg gap.** All zero.
- **No definition of *level*, *reset*, *push*, *M/W anatomy*, or *trap*.**
- **No answer to V08's `A-061`** (*"the fast move is false"*) — the highest-value gap V08 left is
  untouched here.
- **No `A-056` closure.** V09 confirms the term is **HOD/LOD** and adds the 15-pip stop that the
  skill *"warrants"*, but still does not say how to identify the extreme before it is one.

---

## 15. HOW V09 RELATES TO V08 — `GUEST`, both

| V08 left open | V09's answer |
|---|---|
| The **innermost ring** of the four-stage model — a literal `?` on the final frame | **§5 error 3: discipline in keeping to the risk plan.** `[00:19:48]`–`[00:20:27]` |
| *"a lot of ramifications in about 35, 40 minutes when we get into that section"* — the promised stop-side consequence of the 3:1 claim | **Partly paid.** V09 supplies the 15-pip stop *size* and the sizing formula built on it, and **no placement rule** |
| Section 3, *"how to not GET killed"*, announced twice and absent | **Is Part A of V09**, in full |
| The 29-setup gallery | Referred to again at `[00:10:06]`, `[00:25:11]` as the availability argument for 5 trades/week |
| **`A-061`** — *"the fast move is false"* | **Untouched** |
| **`A-063`** — the 25-pip stop hunt box | **Untouched**; V09's 25 pips is a stop-loss size, a different object, and is **not** merged with it |
