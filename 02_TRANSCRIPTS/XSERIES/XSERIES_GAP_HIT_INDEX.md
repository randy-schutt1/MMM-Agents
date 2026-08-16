# X-SERIES GAP HIT INDEX — CANDIDATE PASSAGES AGAINST THE OPEN GAP MATRIX

**Date:** 2026-08-15
**Scope:** all 21 X-series transcripts in `01_SOURCE_VIDEOS/Forex Bootcamp/More videos/transcripts/`
**Sorted by gap, not by file**, per `CLAUDE_MMM_XSERIES_TRANSCRIPTION_PROMPT.md` §Output.

> ## ⛔ STATUS — THIS FILE CLOSES NOTHING
>
> Every row below is a **candidate passage**, not a resolution. No `A-xxx` changes status, no
> `C-xxx` closes, no tier is assigned, no lesson is ingested by this file. `SOURCE_MANIFEST.md`
> `10_AMBIGUITIES/`, `11_CONTRADICTIONS/`, `MMM_SETUP_REGISTRY.md`,
> `MMM_GAP_AND_DEPENDENCY_MATRIX.md` and `08_CONCEPT_LIBRARY/` are untouched.
>
> ### ⭐ UPDATED 2026-08-15 — THE OWNER RULED ON ALL THREE §0 QUESTIONS
>
> | §0 question | Ruling | Decision |
> |---|---|---|
> | Is the X-series Tier 1? | **YES — same level as the bootcamp**, to fill gaps and add detail. `A-03` discharged | **`D-063`** |
> | Are the three ASR garbles real? | **court of wood · shooting star · railroad tracks** — one of my three guesses was wrong | **`D-064`** |
> | Where may the derivatives live? | **`01_SOURCE_VIDEOS/` is fine.** §0.3 withdrawn | owner, 2026-08-15 |
> | The TDI band basis conflict | **`D-052` reversed** — bands deviate from the **market baseline**. Conditional on chart-application verification | **`D-065`** |
>
> ⚠️ **Tier 1 status does not make these transcripts verified.** `D-063` §5: no numeric figure from
> this single-pass `whisper-small.en` output may close a record before two-tier verification. §0.1
> stands, and is now the *only* remaining blocker.

---

## 0. THREE THINGS TO SETTLE BEFORE ANY OF THIS CAN CLOSE A RECORD

### 0.1 ⚠ The transcripts are single-pass small-model ASR — the numbers are the least reliable part

`transcribe_batch.py` uses `mlx-community/whisper-small.en-mlx`, one pass, no second engine, no
isolated re-transcription of crucial passages. The transcription task prompt required a **large**
model plus **two-tier verification**, precisely because *"pip figures, minute counts, candle
counts, EMA periods and RSI periods are load-bearing and are the most common ASR failure in this
corpus."*

Almost every finding below is load-bearing **because** it carries a number. Treat every figure as
**unverified** until a second engine and a direct listen confirm it. **This is now the only
remaining blocker on this material** (`D-063` §5).

**Known garbles — corrected by the owner, `D-064`:**

| ASR produced | Actual | |
|---|---|---|
| *"quart of wood"*, *"quarter wood"* | **court of wood** | its own pattern — ⚠️ ~~railroad tracks?~~ **my guess was wrong.** Spelling likely *cord of wood*, unconfirmed |
| *"human star"*, *"morning speaking star"* | **shooting star** | ⚠️ ~~evening star~~ **wrong** — X12 names evening star separately, so they are two objects |
| *"Rarotracts"*, *"aero tracks"*, *"rubber track"* | **railroad tracks** | confirmed |

Still-unresolved garbles: *"nameable second leg"*, *"pins the man-made"* (= **mayonnaise**), *"the
male"* (= **mayo**), *"$22.16"* for a quote of `1.2216`, *"naders to the center"* (= **nadir**).

> ⚠️ **`court of wood` is a name-only pattern.** `X13 [33:25]` — *"He forms a court of wood on the
> low. This is a double… double court of wood"* — is a usage, not a definition. It joins the P3
> name-only backlog and stays `DO NOT CODE` (`D-064` consequence 2).

### 0.2 ~~The X-series tier is contradictory as written~~ — **RESOLVED, `D-063`**

<details>
<summary>Original text, retained per <code>REMEDIATION_PROTOCOL.md</code> §2</summary>

- `SOURCING_HIERARCHY.md` §1: **Tier 3** is *"generic internet research… `EXTERNAL — NON-NORMATIVE`,
  permanently… Closes nothing, unblocks nothing, cited in no artifact."*
- `MMM_PT2_INTAKE_AND_ALLOCATION_PLAN.md` §5 Track B step 1 assigns the X-series **"T3, cross-course
  note required"** while describing it as *"**Does Mauro state it?** … same instructor, already owned."*

These cannot both be right… **An owner ruling is owed on whether a fourth rung exists for "same
instructor, different course" and what it may close.**

</details>

**The ruling:** *"X series is not contradictory. It should be treated on the same level as the
bootcamp to fill in the gaps and adds more details."* — owner, 2026-08-15. **The X-series is
Tier 1.** `A-03` is discharged; the `MMM_PT2` "T3" assignment is superseded.

**What still constrains it** — `D-063` §1–5, none relaxed: `D-025`/`D-033` still rank the author
above a guest (**X11, X15, X16, X21 are guest-presented; X01–X03 are Dean Malone**); `D-030` still
forbids approximating a definition the tape does not supply, so every §15 negative stays
`DO NOT CODE`; `D-048`'s ladder now applies routinely because Tier 1 has more internal
disagreements; and **admission is not verification** — see §0.1.

### 0.3 ~~Derivative location violates `SOURCE_INGESTION_PROTOCOL.md` §2.3~~ — **WITHDRAWN**

> *"Source videos is fine to have it. It's just where it lives."* — owner, 2026-08-15

The transcripts stay where they are. No move, no re-pathing. **Two smaller items survive the
withdrawal and are still owed**, since they are about traceability rather than location: the 21
source SWF hashes have **not** been re-verified against `SOURCE_MANIFEST.md` since transcription,
and **no per-file SOURCE table, speaker note, VERIFICATION section or confidence rating exists for
any of the 21 files**.

---

## 1. SUMMARY — WHAT THE X-SERIES DOES AND DOES NOT REACH

| Gap | Priority | Verdict from X-series |
|---|---|---|
| `A-011` M/W first-leg anatomy | **P0** | **SUBSTANTIALLY ANSWERED** — explicit verbal definition of both M and W, plus a start rule for leg 1 |
| `A-007` / `A-004` leg & level segmentation | **P0** | **SUBSTANTIALLY ANSWERED** — level vs. push explicitly disambiguated; EMA-based level markers given |
| `A-010` / `A-056` prospective PFH/PFL | **P0** | **PARTIALLY ANSWERED** — an explicit *prospective* "lock" criterion exists |
| `A-133` blue tracer | P1 | **ANSWERED** — and it confirms the `MMM_PT2` §6.1 prediction against the 800-EMA reading |
| `A-086` TDI band period / multiplier | P1 | **PARTIAL** — multiplier stated; period not. **Band basis reversed `D-052` → `D-065`**; see §5 |
| `A-024` "22" overshoot tolerance | P1 | **NOT ANSWERED** — "slightly" is still unbounded |
| `C-029` / `C-030` second-leg time cap | P1 | **RESOLVED IN-SOURCE** — the instructor reconciles the 30 / 30–45 / 90-minute figures himself |
| `A-141` High/Low Trainer | P1 | **NOT ANSWERED — zero hits.** Confirms it must come from owner artifacts (Track C) |
| `A-033` outside-structure boundary | P2 | **ANSWERED** — explicit definition plus a pip boundary |
| `A-049` / `C-006` stop hunt vs. trap | P2 | **NOT ANSWERED** — and a student asks this exact question on tape and is deferred |
| `A-138` Level-1/2/3 quantification | P2 | **SUBSTANTIALLY ANSWERED** — EMA-geometry criteria for all three levels |
| `A-139` one-third entry candle | P2 | **NOT ANSWERED** — the "one-third" hits are about the Asian box, a different object |
| `A-019` / `A-105` / `A-131` session clock & DST | P2 | **SUBSTANTIALLY ANSWERED** — full time map, explicit EST anchor, **explicit DST policy** |
| `A-100` / `C-011` / `C-022` ADR lookback / repaint | P2 | **NOT ANSWERED** — ADR *use* is fully specified; its *construction* is never stated |
| Name-only pattern anatomy | P3 | **PARTIALLY ANSWERED** — 22, 33, 333, straightaway, half-a-Batman, shark fin, blood in the water all defined |
| Stops / targets / sizing (absent for every setup) | — | **SUBSTANTIALLY ANSWERED** — see §14 |

**Two records closed below Tier 1 are put back in play** by this material: `A-023` (the 33 trade,
`RESOLVED BY MMM-NOTES`) and `C-021` (band basis, `CLOSED — OWNER EMPIRICAL PREFERENCE`). See §5
and §12 — both are `SOURCING_HIERARCHY.md` §3.4 standing-re-check targets, and §3.4 names the
trigger for `C-021` explicitly.

---

## 2. `A-011` — M/W ANATOMY **AND** THE FIRST-LEG START RULE (P0)

### 2.1 The full verbal definition — X13 `Trap Moves`

> **X13 [23:36]** *"Definition of the M. An aggressive move by the dealer to set the high of the day
> or the high of the session. **The first leg rise induces traders to take long positions.**"*
>
> **X13 [24:06]** *"The center… the apex… **triggers your stops and gets traders to stop and reverse
> short.**"* (he then corrects himself: *"it was called a nadir"*)
>
> **X13 [24:18]** *"**The second leg rise triggers those stops. The second leg rise can be slightly
> above the first but must close below within 30 to 45 minutes.**"*
>
> **X13 [24:31]** *"When you're right here at the high, it can do one of two things. **Miss it, or it
> can go above and come right back below. That is a valid M pattern.**"*

The W is given as the exact mirror, unprompted, nine minutes later:

> **X13 [32:14]** *"By definition, it's the exact opposite of the M formation… to set the low of the
> day or low of the session… The first leg correction induces traders to take the short positions…
> The second leg correction **can be slightly below the first, but must close above within 30 to 45
> minutes.** The second leg correction **will only go below the first leg if there are orders built
> up there.**"*

### 2.2 ⭐ The start rule — this is the piece the gap matrix says does not exist

The matrix records for `A-011`: *"Second-leg behavior… exist; **start rule does not**."* Two
passages supply one:

> **X06 [00:52–01:22]** *"What is a vector candle? A vector candle **by definition** is like a spike
> or a breakout candle… **it's the first leg of the stop hunt**… it's the candle that gets the action
> going, **it's the candle that breaks out of the Asian range and starts the action.**"*
>
> **X12 [15:14]** *"**Usually the vector candles will form the first leg** of the reversal pattern.
> It's the start of the show, so to speak. **It's the start of the M or W formation.**"*

**Candidate rule:** *leg 1 begins at the vector (breakout) candle that exits the Asian range.*
This is objectively codable and prospective. It has not been tested.

### 2.3 Invalidation and confirmation — also previously absent

| Item | Passage |
|---|---|
| **Invalidation** | **X13 [29:46]** *"There is **no close above the first high that is set**. When the dealer sets the high of the day right here, **nothing closes above that high.**"* |
| **Confirmation candle** | **X13 [29:08]** *"…you could simply wait for the confirmation candle, which gives you the **signal crossover, close below the ketchup**, to make this a confirmed formation."* ⚠ *ketchup* = **13** under `D-043` — this is a **5/13 cross** confirmation stated in one sentence |
| **Second-leg distance** | **X10 [28:42]** *"The dealer makes a visible second leg formation **25 to 75 pips off of the peak formation low.**"* · **X10 [55:53]** *"The safety trade second leg can be **up to 75 pips** from the peak formation, not 50 pips, right? Yes."* |
| **Entry point** | **X10 [24:19]** *"It forms the M. **The entry is on the second leg when it confirms below the mustard**"* (*mustard* = **5**) |
| **Do not take leg 1** | **X13 [02:19]** *"…to short the first leg. **It does not work.**"* · **X17 [11:43]** *"how do you know if there's going to be a second leg trade? Man, **I have no idea.**"* |

### 2.4 What is still NOT answered

Whether a formation that **misses** the level and one that **overshoots** it are the same object
for entry purposes is stated ("either is valid") but the **overshoot magnitude is never bounded** —
that is `A-024`, still open (§7).

---

## 3. `A-004` / `A-007` — LEVEL AND PUSH SEGMENTATION (P0)

### 3.1 ⭐ The vocabulary is explicitly disambiguated — a two-tier scheme

This is the single most clarifying passage in the 21 files for this gap:

> **X14 [02:57–04:08]** *"…they would say **levels over the course of the week, like level one day
> one, level two day two, level three day three**… **I call it three pushes, but that's not the same
> term. The pushes are intraday**, which comprise of the ADR — three levels of rise, or three
> pushes."*
>
> **X14 [03:43]** *"So swipes, pushes will be comprised of the entire ADR, and then **levels will be
> from the low of the week to the high of the week.**"*
>
> **X07 [47:32]** *"**The three levels of intraday price movement will comprise the entire ADR.**"*

**Candidate reading:** *level* = a **daily** unit of the weekly cycle (low-of-week → high-of-week);
*push/swipe* = an **intraday** unit, three of which comprise one day's ADR. The corpus's level
confusion may be two different objects sharing one word. This directly bears on `C-001`-family
disagreements and on the `MMM_PT2` §2 note that BEEKAY and `e-book 1` contradict each other on
exactly this point — **X14 says both readings are in use and are different things.**

### 3.2 EMA-geometry markers for the level boundaries — X19

> **X19 [22:27]** *"**Level one is identified by a flattening and tightening of the averages.**"*
> **X19 [22:36] / [23:39]** *"**Level two is identified** most of the time **by a crossing**… level
> two is identified by the 50… **first touch to the 50 is good for 50.**"*
> **X19 [23:56]** *"**Level three is identified by a fanning out of the averages** — the averages get
> huge, price acceleration, price is out here."*

Guest **Kar** (X11 — `D-033` applies, guest-only material cannot close a record) gives the same
scheme operationally:

> **X11 [14:05]** *"So you see a **1350 cross** with the downside, price consolidating over here.
> **That's your level one.** So this is day one drop."*
> **X11 [16:41]** *"…comes out sort of like a W pattern, rises off the low. Now you go to **1350
> cross, now you're level one.**"*

⚠ **This independently reproduces the Tier-6 BEEKAY candidate** recorded in `MMM_PT2` §3
(L1 = 13/50 cross, L2 = 50/200, L3 = fanned EMAs). Note the corroboration is **partial**: X19 and
X11 both give **13/50 for L1** and **fanning for L3**, but X19 attaches **the 50** to L2 where
BEEKAY says 50/200. Do not average them.

### 3.3 ⚠ The three-level cycle is not a hard ceiling

> **X21 [22:07]** *"…even though the pair can go into level three, **it can go into level four, and
> five, and six, and seven** — the pair can just, when it's on a trend move, it can really trend."*

(Guest, `D-033`.) This conflicts with the "market makers will not move one direction more than
three days in a row" statement at **X07 [01:35]**. Preserve both; a `C-xxx` may be owed.

---

## 4. `A-010` / `A-056` — PROSPECTIVE PFH/PFL (P0)

The X-series does **not** give an arithmetic rule for identifying the week's extreme in advance.
It gives something different and arguably better: a **behavioural confirmation event** the
instructor calls *the lock*.

| Element | Passage |
|---|---|
| Definition | **X06 [14:53]** *"Peak formation is the highest point on the chart for the week, the lowest point on the chart for a week."* |
| Where it forms | **X06 [05:49–06:09]** *"…the dealer will set the psychological support and resistance levels in the first part of the week and trade away from those levels. **He will then issue a midweek reversal in the form of an M or W, which becomes the anchor point or the new peak formation for the cycle.**"* |
| ⭐ **The lock — the prospective criterion** | **X06 [21:28]** *"…the dealer **never breaks the previous level. By never breaking the previous level, this is now a lock as peak formation.**"* · **X10 [29:45]** *"…**fails to violate the peak formation, then this becomes an absolute certainty that this is my peak.**"* · **X18 [33:56]** *"When he does this, **the peak formation is a lock.**"* |
| **Lead time** | **X08 [33:57]** *"the peak formation has to be **locked in place. You know that a day or two beforehand.**"* · **X08 [34:21]** *"**You got 12, 15, 18 hours to figure those out.** You can see those coming from a mile away."* |
| The lock's shape | **X21 [06:23]** *"…**the peak formation low is when you see a W pattern**"* (guest) · **X10 [05:17]** *"**The M forms the anchor, the M is the peak formation high for the week.**"* |

**Candidate operational rule:** *a swing extreme becomes a certified PF when the dealer returns to
it (25–75 pips off) and fails to violate it, forming an M/W second leg.* Prospective, codable,
untested.

⚠ **This does not dissolve the honest uncertainty flagged in `MMM_PT2` §2** (BEEKAY: *"nobody knows
when a reset will occur"*). Note **X17 [11:43]** — *"how do you know if there's going to be a second
leg trade? **I have no idea**"* — the instructor is explicit that the confirming event is not
predictable, only recognisable once printed. The remedy stays as `MMM_PT2` framed it: a decision
about what to do under irreducible uncertainty, not a missing lesson.

---

## 5. `A-086` / `A-084` — TDI, AND A DIRECT CHALLENGE TO AN OWNER RULING (P1)

### 5.1 ⚠⚠ `C-021` — the bands' basis. **`SOURCING_HIERARCHY.md` §3.4 is triggered.**

`C-021` was closed by **`D-052`** on the owner's ruling: *"It's definitely **not** the market basis.
It's the RSI [line]."* §3.4 records that this override *"applies with full force: **a later video
that states a construction for the bands governs and triggers §3.1.**"*

**Mauro states a construction, twice, in one passage:**

> **X20 [17:27–17:46]** *"So to further the cause, he added some **volatility bands**, which are
> simply a take on **Bollinger's standard deviation** and the way they're plotted… **deviations away
> from the market base.** So taking **the market basis line**, remember standard deviation, if it
> gets too far away…"*
>
> **X20 [18:17–18:24]** *"This is divergent based on standard deviation rules because it was above
> the **two standard deviations**. Now it's below **two standard deviations**…"*

This **agrees with V14 `[00:45:09]` and `MMM-NOTES` p.45** — both of which `D-052` overrode — and
**disagreed with the owner's ruling**.

> ### ⭐ RESOLVED 2026-08-15 — `D-065`. **`D-052` IS REVERSED. THE BANDS DEVIATE FROM THE MARKET
> ### BASELINE.**
>
> *"It's okay the definitions of the tdi bands. We just need to ensure we are applying it correctly.
> If you want to update so it matches, then I'm okay with it — **as long as we are applying it
> correctly to the charts**."* — owner, 2026-08-15
>
> Under `D-063` X20 is Tier 1, and it states a **construction** rather than a characterisation —
> `D-048` rung 2. `C-021` re-closes as `RESOLVED BY COURSE (X20)`, superseding `D-052`, which is
> retained unedited. **§3.5's re-check obligation is vindicated a third time:** it named this exact
> trigger — *"a later video that states a construction for the bands governs"* — and that is the
> trigger that fired.
>
> ⭐ **The owner's authorization is CONDITIONAL.** Before the corrected basis enters any spec, it
> must be reconciled against X20 [20:21–22:50]'s operational shark-fin description **and confirmed
> on the owner's own chart** that the corrected construction reproduces what he is actually seeing
> (`D-057` records that those signals work for him, without a number). If it does not reproduce,
> that is a finding and goes back to the owner — not resolved by preferring whichever version codes
> more easily.

**Separately, `A-086` gains a MULTIPLIER it never had at any tier — "two standard deviations."**
⚠️ Unverified ASR; `D-063` §5 applies. The **period** is still not stated by Mauro, so **`A-086`
does not close** and `A-031`/`A-032` stay uncomputable — `D-052`'s *"it unblocks nothing"* survives
its own reversal.

### 5.2 The band period — one candidate, and it is exactly the kind of number §0.1 warns about

From the indicator's **author**:

> **X01 [01:18:28]** *"**It's 30, the deviation's 34.** The period is based upon **the period within
> the RSI**."*
> **X01 [01:18:37]** *"So again, the deviation, if you just go in and say, well I'm gonna put in a
> **34 deviation**, it's **not gonna match up exactly**, because we're coming off of the **modulated
> RSI**."*

⚠ **Do not use these figures.** "It's 30, the deviation's 34" is internally odd — a standard-deviation
*multiplier* of 34 is not a coherent reading, and the stock TDI ships a **34-period** band with a
**1.6185** multiplier, which is what a garbled utterance here would most likely be. **This passage
is the single highest-value Tier-2 verification target in all 21 files** — re-run with a second
engine and listen to `X01` 01:18:00–01:19:00 directly. The one part that is clear and useful:
**the band period is tied to the RSI period, not set independently.**

### 5.3 `A-084` / `A-039` — the author corroborates the owner's `!SM_TDI` artifact

> **X01 [16:58]** *"**he uses an RSI 21 in his tool**, and again, **his range is a 63 to 68**."*
> **X01 [40:44]** *"**I used an RSI 10.** I originally designed it with an **RSI 13**… I literally
> timed it from a 13 down to a 10."*
> **X01 [01:02:22]** *"**I use an SMA**, but speaking to Steve… about Steve's model, **he does use an
> EMA.** And so, yes, the red line is [an EMA of the RSI]."*
> **X01 [01:02:39]** *"If you take a regular RSI 21 and set it on top of Steve's TDI, **they're not
> gonna necessarily match up**… because **it's a modulated RSI**."*

This is **independent corroboration of `21` and `63/37`** from the tool's author, against a
`D-045` `TOOLING` closure whose recorded weakness was that *"the corroborated fields and the
load-bearing field are NOT the same fields."* ⚠ It does **not** corroborate `RSI_Price_Line=2` —
the actual load-bearing field — and *"it's a modulated RSI, not exactly a regular RSI"* is
**material evidence bearing directly on `A-084`'s question** (is the green line `RSI(21)` or a
smoothing of it?). The author says: **neither, exactly.** `A-084`'s provisional closure should be
re-examined, not confirmed.

### 5.4 Shark fin and blood in the water — defined, having been absent from all four PDFs

> **X20 [20:21–21:13]** *"A shark fin short sets up exactly like this. **The bands are tight**, which
> means you are in phase one of the market cycle, accumulation or consolidation… **The RSI line
> breaks out and comes right back in.** It appears that a shark fin is coming out of the water,
> coming out of the band… **When it crosses the red line, it's like the shark came up and took a bite
> out of the red line and made some blood.** … When you have shark fin high, blood in the water,
> what's happened in essence is that **the dealer made an aggressive stop hunt to the high, came
> right back below the level.**"*
>
> **X20 [14:49]** *"He added a **TSL or trade signal line**, which provides us blood in the water."*
> **X20 [22:40]** *"**Confirmed by coming back inside the volatility band**"*

**Candidate rule:** *shark fin* = RSI price line exits the volatility band and returns inside;
*blood in the water* = that excursion also crosses the trade signal line. Both codable.

---

## 6. `C-029` / `C-030` — THE SECOND-LEG TIME CAP. RESOLVED BY THE INSTRUCTOR HIMSELF

The corpus conflict is 30 vs. 30–45 vs. up-to-an-hour. **X12 and X17 explain why all three numbers
are in circulation — they measure different things.**

> **X12 [34:42–35:08]** *"…and this behavior takes up to 90 minutes, up to two hours, 30 to 90
> minutes. **A true M should take a minimum of 90 minutes. A good M or W should take a minimum of 90
> minutes. An outside structure should take 90 minutes.** **The problem with the 30 minutes, and we
> have to account for it, is those damn railroad tracks** where he goes in in one move, hits the
> number, and comes right back out. **That's the problem. You have to account for that.**"*

And the quiz answer, stated as doctrine:

> **X17 [03:53]** *"**How long will the dealer work the price levels? Thirty to ninety minutes, but
> up to two hours. Two hours is better. Ninety minutes is really good. Thirty minutes you got to
> account for the railroad tracks. Forty-five minutes for the evening star**, the extra formation in
> there."*

> **X05 [22:35 / 28:43]** *"So we say **30 minutes up to two hours**… **The 30 minutes accounts for
> railroad tracks.** I like to see second leg formations and structures that last **an hour, hour and
> a half, two hours.**"*

**Candidate reconciliation:**

| Quantity | Value | What it measures |
|---|---|---|
| Second-leg **close-back-inside** window | **30–45 min** | how fast the overshoot must be reclaimed (X13 [24:24], [32:43]; X10 [14:56], [37:18]; X12 [10:23]) |
| **Whole M/W duration** | **90 min minimum, 30–120 min range, 2 h better** | how long the dealer works the level |
| **30 min** | the acknowledged **exception** | railroad tracks — one swipe handles all the criteria (X20 [22:51]) |
| **45 min** | the second exception | evening-star formation |
| **2 h** | **time stop**, not a cap | X12 [30:33] *"If the dealer doesn't shift the zone in two hours, something's wrong"*; X17 [07:49] *"if the dealer issues a second leg, you reset your time clock"* |

⚠ This reconciliation is **internally consistent and stated by the instructor** — but it comes from
the X-series, and `C-029`/`C-030` are records about **V01–V21**. Whether it may resolve them turns
entirely on §0.2.

---

## 7. `A-024` — "22" OVERSHOOT TOLERANCE. **NOT ANSWERED**

The **22 trade** itself is now defined:

> **X06 [21:49]** *"**What is a 22 trade? A 22 trade is when you have a second leg of a second leg.**
> You have a W formation off of the larger W formation… **that's where the 22 comes in.**"*
> **X07 [58:43]** *"The dealer makes a second leg of a second leg M or W formation where he **goes
> near the level and fails to break it, or goes slightly above the level and comes back below.**"*

But *"slightly"* is **never quantified anywhere in the 21 files.** The nearest figures are about
different objects — the trading zone (25–50 pips beyond the Asian range, §13) and the safety-trade
second leg (25–75 pips off the PF, §2.3). **`A-024` stays open.**

---

## 8. `A-033` — OUTSIDE-STRUCTURE BOUNDARY (P2). ANSWERED

> **X17 [03:25]** *"**What is an outside structure? A spike candle or set of spike candles that form
> the high or low where the next set of candles immediately trade off of the level.**"*
> **X13 [39:01]** *"**Outside structures by definition are the vector portion of the half of
> Batman.**"* · **X13 [40:02]** *"The outside structure is this portion of the vector candle that
> makes [the move]… **he does not make the second leg.**"*
> **X12 [34:54]** *"**An outside structure should take 90 minutes.**"*
> **X17 [46:44]** *"The dealer made an outside structure to the low. **25 pips below the Asian or
> initial low of the day.**"*
> **X17 [45:06]** *"…**We don't know if it's going to be a second leg element, but it's an outside
> structure right now.**"* ← the prospective/retrospective boundary, stated

Companion — **half a Batman**, previously name-only:

> **X13 [16:36]** *"**By definition, half of Batman is the dealer has spiked the high or low**…"*
> **X13 [23:13]** *"**The entry on a half of Batman is: wait one hour and make sure the dealer hasn't
> extended the high or low any more, and then look for an entry.** They're not good solid entries."*

---

## 9. `A-138` — LEVEL 1/2/3 CHARACTER AND QUANTIFICATION (P2). SUBSTANTIALLY ANSWERED

Geometry criteria are in §3.2. Character and trading rules:

| Level | Statements |
|---|---|
| **L1** | **X07 [30:33]** *"aggressive move to make you turn the corner"* · **X04 [41:16]** / **X07 [45:15]** *"**Never trade against peak formation coming out of level one consolidation. It is a sucker's trade.**"* (repeated in X09, X10, X18 — the most-repeated rule in the series) |
| **L2** | **X07 [30:26]** *"**Level two, absent of market maker support. Level two is usually smaller.**"* |
| **L3** | **X07 [20:44]** *"always at level three you will see aggressive moves"* · **X07 [24:54]** *"**that's why level three is choppy**"* · **X07 [24:32]** *"the heaviest volume will be seen at level three"* · **X07 [41:32]** *"**The head and shoulders develops at level three**"* · **X10 [14:13]** *"**Level three behavior: erratic sideways movement with no real direction**"* · **X21 [11:27]** *"level three… **you want to be flexible enough to trade both ways because it will be the most volatile level**"* (guest) |
| **Cycle wrap** | **X07 [40:54]** *"**level three becomes level one**"* — the reversal handoff, stated four times |
| **Target** | **X09 [10:52]** *"**the projected target is simply ADR times 3**"* · **X09 [12:41]** *"take the high or low of the day **at the time the anchor is formed**, and add or subtract 3 × ADR"* |

---

## 10. `A-019` / `A-105` / `A-131` — SESSION CLOCK AND DST (P2). SUBSTANTIALLY ANSWERED

**X05 `Daily Setup and Time Mapping` is a dedicated time-map lesson.** It supplies the anchor and —
crucially — **the DST policy the Mauro PDF lacked** (`MMM_PT2` §3.1: *"No DST policy stated"*).

> **X05 [06:51]** *"From 5 p.m. to 8 p.m., **all times Eastern Standard New York.**"*
> **X05 [07:34]** *"**At 5 p.m., the high and low reset.**"*
> **X05 [34:25–34:33]** *"**5 p.m., high and low reset**, the market maker spread starts. **5 p.m. to
> 8 p.m., dead gap, no exchanges are open. Asian session, 8:30 to 3 a.m.**"*
> **X05 [24:23]** *"from 8:30 to 3:00 AM is the Asian session"* · **X05 [25:47]** *"**from 9:30 to
> 5 PM is the US session**"*
> **X05 [17:31]** *"This structure will develop **between 2 and 4 AM** with the **gap time being 3 to
> 3:30 AM**."* · **X05 [37:12]** *"the two most telling candle, **3:30 to 3:45**, that 15-minute
> candle that paints **right at the London Open**"*
> **X05 [08:56]** *"**At 1 a.m. New York time to 2 a.m.**, one hour, is about the time he will widen
> the swing."*

⭐ **The DST policy, stated outright:**

> **X05 [29:46–30:06]** *"…in the summertime, **New York is GMT minus four.** In the winter, **New
> York is GMT minus five.**"*
> **X05 [29:12]** *"In the winter, **London adjusts one hour** because we're GMT minus five in the
> winter."* · **X05 [29:32]** *"**London is an hour longer in the winter.**"*
> **X17 [02:58]** *"**Summer hours, the clock we're on now. GMT minus four.**"*

⭐ **And the broker-server-time trap, stated outright** — this bears on `A-131`:

> **X05 [36:27]** *"**If the dealer has a server at GMT plus one, then that time ribbon on the bottom,
> GMT plus one, has nothing to do with the times that I'm talking about.**"*
> **X18 [04:37]** *"**You ping your dealer server**, and a big fat letter tells you your GMT minus
> two, your GMT plus one."*

⚠ **One internal tension to preserve, not resolve:** the Asian box end is given as **3:00 a.m.**
(X05 [24:23], [34:33]) and as **1:00 a.m.** (X05 [10:07] *"One to 2 a.m. is the end of the Asian
session"*; X07 [11:59] *"you need to know that this ends at 1 a.m."*; X18 [06:59] *"I used to, **at
1 a.m. New York**, record the Asian high and Asian low"*; X18 [13:34] *"The blue box will stop
painting around 1 a.m. or 2 a.m. **But I do 1 a.m. because that's how I was taught**"*; guest Kar
X11 [51:18] *"**that'll go from eight to one o'clock**"*). Read one way this is *session* vs.
*blue-box-painting* window; that reading is not stated. **File it; do not average it.**

Also `A-131`-adjacent: **X11 [51:18]** names the tool — *"**work time 1.6**… automatically… figures
out what your GMT offset is and sets it to where the Asian session starts."* A concrete artifact
name to hunt for under Track C.

---

## 11. `A-133` — BLUE TRACER. **ANSWERED, AND IT CONFIRMS THE §6.1 PREDICTION**

`MMM_PT2` §6.1 predicted, from V19 frames alone, that the tracer is a **Hi/Lo marker, not an
800 EMA**, and called the test *"the highest value-per-hour item in the program."* The X-series
settles it in plain speech, 27 times across 8 files:

> **X13 [19:14]** *"**Blue tracer is yesterday's high.** The dealer has spiked above yesterday's
> high."*
> **X06 [08:00]** *"He's trapping slightly above **yesterday's high, the blue tracer**."*
> **X13 [20:47]** *"**yesterday's blue tracer, yesterday's high.**"*
> **X16 [36:21]** *"**The daily high-low tracer** gives me a sense of what day it is."*
> **X16 [31:02]** *"my **day high and day low tracer**"* · **X16 [27:43]** *"Nice W through the **day
> low tracer**."*
> **X08 [26:53]** *"**5 p.m. blue tracer**, some of you six, some of you four depending on where
> you're dealing at"* ← ties the tracer to the **5 p.m. high/low reset** of §10
> **X11 [52:13]** *"your box will start from **wherever your tracer is**… **your day tracer**"*
> **X10 [18:17]** *"Turn to the four-hour chart, look at your tracer, **control-Y on your MetaTrader
> platform**"*
> **X04 [29:00]** *"Here's your **double tracer** starting the next week."*

**Candidate resolution:** the blue tracer is a **horizontal marker of the prior day's (or prior
week's) high and low**, reset at the 5 p.m. EST rollover — **not a moving average**, and
specifically **not the 800/blueberry**. The 800-EMA reading is eliminated: X10 [02:45] and X09
[01:17] use *blueberry* and *tracer* as **different objects in the same lessons**.

⚠ Note X10 [18:17]'s *"control-Y on your MetaTrader platform"* is likely garbled (Ctrl+Y toggles
period separators in MT4) — flag for verification; the surrounding claim does not depend on it.

---

## 12. `A-023` (33 TRADE) — RE-CHECK OBLIGATION TRIGGERED

`A-023` is `RESOLVED BY MMM-NOTES` (`MMM-NOTES` p.64), and `SOURCING_HIERARCHY.md` §3.4 lists it
among *"the highest-priority reconciliation targets in the project."* The X-series gives a direct
statement:

> **X07 [56:04]** *"**33 trade. A 33 trade is a trade where on the third day of the cycle, the dealer
> will issue three intraday levels.** Let me say it again. **On the third day of the cycle, the dealer
> will extend it by three intraday levels. So you have a third day — three — and three intraday
> levels, another three. A 33 trade.**"*
>
> **X07 [57:11]** *"**A 333 trade is this. The last leg of the last leg is a stop hunt that contains
> three vector candles.**"* · **X07 [57:59]** *"…on the very last segment of that leg, he makes
> **three vector candles as a stop hunt**, to induce the last batch of traders."*

Also newly defined, previously name-only:

> **X07 [35:22]** *"**Straightaway trade by definition is a trade where the dealer does not trade
> below or above the blue box and issue you a visible stop hunt.**"*
> **X07 [51:34]** *"So what are the trades? **M, W, a 33, 22, a 333, and a multi-session M or W.**"*
> **X07 [50:23]** *"Here's the four trades. **Stop hunt high, drop — M formation. Stop hunt low, rise
> — a W formation.**"*

**§3.1 must be run against `A-023`** once §0.2 is settled.

---

## 13. VISIBLE STOP HUNT AND THE TRADING ZONE — QUANTIFIED

Not a numbered gap, but load-bearing for SR-01/02/06/07 and for `A-049`:

> **X08 [23:49]** *"**The trading zone is always set 25 to 50 pips higher than the Asian high or the
> Asian low.** … we measure the distance from the top here, the initial high, the **IHOD**… and the
> **IL**, the initial low of the day."*
> **X08 [24:19]** *"The reason for that is, where does everybody put their stops? 25, 30, 35, 40, a
> couple smart alecks 45, 50. **The dealer triggers those stops as part of the cycle.**"*
> **X05 [08:27]** *"**A 50-pips-or-less Asian range allows you to see the visible stop hunt.**"*
> **X05 [08:36]** *"**A stop hunt that occurs above or below the Asian blue box on our template.**"*
> **X17 [45:44]** *"**The box needs to be 50 pips or less and there needs to be a visible stop hunt
> above or below the blue box.**"*
> **X10 [08:47]** *"**unless the stop hunt is more than 25 pips, you will not produce a successful
> trade.**"*
> **X18 [15:30]** *"**The stop hunt is calculated from the initial high or the initial low.**"*
> **X08 [22:57]** — the blown-box workaround: *"if you look at the **last quarter to one-third of the
> box** and you re-evaluate the consolidation"* (this is the real referent of the "one-third"
> language — **it is not `A-139`'s entry candle**)

---

## 14. STOPS, TARGETS AND MANAGEMENT — PREVIOUSLY ABSENT FOR EVERY SETUP

| Item | Statement |
|---|---|
| **Second-leg stop** | **X14 [43:19]** *"**A second leg trader can use a stop loss of 7 to 10 pips above the high or below the low.**"* (repeated X17 [11:09], [38:48]) |
| **First-leg stop** | **X17 [11:09]** *"**Lazy stop is twenty-three pips above the first leg** if you take the first leg"* · **X14 [42:35]** *"23 is enough to keep you first-leg traders safe"* |
| **Entry-vs-stop pairing** | **X13 [29:25]** *"A good entry's here, very tight stop, **12–13 pips**. A good entry here, probably around **20 pips** stop. Either one is acceptable **because you're going for 50.**"* |
| **Target** | **X13 [29:35]** *"you're going for 50"* · **X08 [49:22]** *"**Why 50 pips? 50 pips is the average size of a stop hunt**"* · **X09 [10:52]** swing target = **ADR × 3** |
| **Dealer's increment** | **X14 [25:46]** *"**The market maker's job is to trigger the stop loss level in 25 to 50 pip increments**"* · **X14 [30:36]** *"in Australian, Canadian, **25 to 30 pips** moves"* |
| **Time stop** | **X12 [30:33]** / **X17 [07:21]** *"**If the dealer doesn't shift the zone in two hours, something's wrong.**"* ⚠ matches the supported `PT-018` and the Tier-6 e-book 2-hour rule — **three independent sources now agree** |
| **Clock reset** | **X17 [07:49]** *"**If you take a first leg trade and you start your timer and the dealer issues a second leg, you reset your time clock.**"* · **X04 [45:36]** *"you restart the clock if a second leg presents itself"* |
| **Break-even** | **X17 [40:33]** *"**Stop moves to break even on the second bar.**"* |
| **Trailing** | **X14 [49:14]** *"A trailing stop of **32 pips** is what's needed"* · **X14 [52:40]** *"if you can't watch the trade, use about a **50 to 75 pip trailer**"* |
| **Trading hours** | **X08 [44:48]** *"**Trade the end of the Asian and London open for about four hours. That's it.**"* · **X17 [17:10]** *"best time of day to trade — **London Open and US Open**"* |

⚠ Every figure in this table is subject to §0.1.

---

## 15. CONFIRMED NEGATIVES — WHAT THE X-SERIES DOES **NOT** CONTAIN

A negative result here is a real finding and directly informs whether more material must be bought.

| Gap | Result |
|---|---|
| **`A-141` High/Low Trainer** | **Zero hits in 18.9 hours.** The only match for "trainer" is *"if a **flea trainer** puts a flea in a jar"* (X15 [05:28]). **This must come from owner artifacts** — `MMM_PT2` Track C was right |
| **`A-100` / `C-011` ADR lookback & repaint** | ADR **use** is fully specified (× 3 target, cap, no-trade-once-met). Its **construction is never stated.** The closest is X09 [12:23] *"you look over here in the corner **on the indicator**, and you take the ADR marker"* — i.e. he defers to a tool. **Stays `DO NOT CODE`** |
| **`A-049` / `C-006` stop hunt vs. trap** | ⭐ **X11 [44:13]** — a student asks *"**how do you distinguish a stop hunt from a trap move?**"* and the guest answers *"I think Steve would probably answer that tomorrow."* **The question is asked on tape and deferred.** Everywhere else the two are used as one sequential event (hunt = mechanism, trap = resulting structure), which **supports the `MMM_PT2` §3.1 reading that the discriminator may be a false distinction** |
| **`A-139` one-third entry candle** | Not present. All five "one-third" hits are the blown-Asian-box workaround (§13) |
| **`A-024` "slightly" tolerance** | Not present (§7) |
| **Pivot construction (`C-023`)** | X19 characterises pivots — *"**pivot points are essentially an ADR grid**"* [48:26] — but **never gives the formula** |
| **TDI band period** | One garbled candidate only (§5.2). Not usable as transcribed |

---

## 16. RECOMMENDED NEXT ACTIONS, IN ORDER

✅ ~~1. Owner ruling on §0.2~~ — **done, `D-063`.** ✅ ~~4. Surface `C-021`~~ — **done, `D-065`.**
✅ ~~3a. Relocate derivatives~~ — **withdrawn by the owner.**

1. ⭐ **Re-transcribe the numeric passages properly** — the last remaining blocker (`D-063` §5).
   Large model + second engine + direct listen, in this order: `X01` 01:18:00–01:19:00 (band period
   — highest value in the program), `X13` 23:30–33:30 (M/W definition), `X17` 03:20–04:10 (quiz
   answers), `X05` 06:30–07:40 / 24:00–30:10 (clock + DST), `X14` 43:00–44:00 (stops),
   `X20` 17:20–18:30 (the `D-065` multiplier).
2. **Amend `SOURCING_HIERARCHY.md` §1.1** to state Tier 1 = V01–V21 **and** X01–X21 (`D-063`
   consequence 3), and append the supersession block to §3.5 for `D-065`.
3. **Chart-application check for `D-065`** — the owner's stated condition. Confirm the corrected
   band construction reproduces the shark fin / blood in the water he actually reads.
4. **Run §3.1 reconciliation on `A-023`, `A-084` and `C-021`** — all three §3.4 re-check targets
   fired at once (`D-063` consequence 4). Individually, on verified text.
5. **Re-verify the 21 source SHA-256 hashes** against `SOURCE_MANIFEST.md`, and add per-file SOURCE
   / speaker / VERIFICATION sections. Survives the §0.3 withdrawal — traceability, not location.
6. **Frames, not more audio.** See §17.

---

## 17. ON SCREENSHOTS — WHERE FRAMES WOULD AND WOULD NOT HELP

`SETUP_ISSUES.md` `I-006` records that `ffmpeg` cannot decode these SWFs' screen-recording video
layer. Frames would have to come through the **Ruffle** pipeline already present in the folder
(`Ruffle.app`) — screen-capture playback, not extraction. That is expensive per file, so it should
be aimed, not swept.

**Worth the cost — these are gesture-dependent and audio alone cannot carry them:**

| Target | Why |
|---|---|
| **X07 `Level Count and 4 Trades` 50:20–58:60** | the *"here's the four trades"* slide sequence and the 22/33/333 diagrams — the closest thing to a canonical setup taxonomy in the corpus |
| **X13 `Trap Moves` 23:36–33:30** | the M and W definition slides, spoken almost verbatim off the screen. Frames would confirm the wording and show the labelled apex/nadir |
| **X17 `Quiz Answers` 02:50–04:40** | the quiz answers are read off a slide — a written source for the time-cap and outside-structure definitions |
| **X05 `Daily Setup and Time Mapping` 06:30–08:00, 22:00–26:00, 34:20–37:20** | the time map is a **diagram**. This is the single best candidate for a reproducible session/DST table |
| **X19 `Moving Averages and Pivot Points` 22:20–24:10** | the L1/L2/L3 EMA-geometry criteria, drawn on chart |
| **X20 `TDI` 20:00–23:30** | shark fin / blood in the water drawn on the TDI panel |
| **⭐ X01 `Steve's use of TDI` 01:18:00–01:19:00** | Dean is **on the indicator's colour dialog** — *"right click on the indicator, go to colors"* — immediately before the band-period answer. **If any frame in 30 hours shows a TDI properties dialog, it is here.** `SOURCING_HIERARCHY.md` §3.4 names that dialog as the specific trigger for re-running §3.1 against `A-084` |

**Not worth it:** X15/X16 (`Jim`), X21 (`Kar and Kim on DMR`) — live trade commentary on charts the
project does not need to reproduce; and X17's second half (motivation/movies).

⚠ **Before any frame work begins**, `MMM_PT2` §4's contamination rule applies here too: these are
**2012** charts, so they fall **outside** both the `D-035` holdout (2016-07-01 → 2017-12-29) and
the `D-044` 2017–2025 block. **The X-series is contamination-free for testing purposes.** That is
worth recording — it means these lessons can be studied in full detail without spending any
out-of-sample data.

---

---

## 18. BEYOND THE GAP MATRIX — SIX RECORDS THE SWEEP HIT THAT WERE NOT ON THE LIST

Added 2026-08-15. The sweep targeted the 15 matrix gaps; these surfaced alongside and are **higher
value than several matrix rows**, because two of them are foundational records the ambiguity file
marks as compounding into everything downstream.

### 18.1 ⭐ `A-001` "anchor point" — and the `A-001` = `A-010` identity question

`AUTOMATION_AMBIGUITIES.md` line 298 rates `A-001` *"Foundational. Sets weekly direction and holding
period. **Wrong = every weekly-bias rule is wrong**,"* and line 1266 flags the compounding risk:
*"if this is the same object as the anchor point then two records describe one concept; if it is
not, the corpus has two undefined foundational objects merged by a careless reading."*

**The X-series answers both halves, in one sentence each:**

> **X10 [00:09]** *"**The anchor point is always the W or the M.**"*
> **X06 [06:02]** *"…which becomes **the anchor point or the new peak formation for the cycle** —
> peak formation is the low of the week or the high of the week."*
> **X06 [08:55]** *"**Once the anchor is established, the peak formation high**…"*
> **X11 [11:52]** *"**The anchor of peak formation high or low is where the market makers start their
> move after trapping volume.**"* (guest, `D-033`)

**Candidate resolution: they are the same object.** *Anchor point* = *peak formation* = the M or W
that sets the week's extreme. That is the merge the ambiguity file feared — except the corpus turns
out to license it, so it is a resolution rather than an error. **Run §3.1 on `A-001` and `A-010`
together; do not close one without the other.**

### 18.2 ⭐ `push` — the `D-030` canonical blocker, and V05/V06/V07 dimension B

`SOURCING_HIERARCHY.md` §1.2 limit 2 uses `push` as **the** worked example of why Tier 2 cannot
unblock a record: the notes give 25–50 pips *"in 3 pushes or candles"* and then withdraw the
regularity in the next sentence, so *"`push` is not unblocked and V05/V06/V07 dimension B stays
BLOCKED."* `A-072` was likewise ruled `EXTENSION ONLY`.

**X14 gives the figure unhedged, and gives a three-term vocabulary that separates the objects:**

> **X14 [03:26]** *"**These three little pushes will be about 25 to 50 pips**, or these three swipes
> at the stops will be about 25 to 50 pips."*
> **X14 [04:08–04:13]** *"**The pushes are intraday**, which comprise of the ADR — three levels of
> rise, or three pushes of rise — **and then swipes are the move towards the stop-loss levels.**"*
> **X14 [03:43]** *"**levels will be from the low of the week to the high of the week.**"*

**Candidate scheme: `level` (weekly/daily) ⊃ `push` (intraday, 25–50 pips, ×3 = one ADR) ⊃ `swipe`
(the move at the stops).** ⚠️ Note X14 uses *pushes* and *swipes* interchangeably in the same
breath at [03:26] and then distinguishes them at [04:13] — that is an internal wobble, not a clean
taxonomy. **This is the strongest candidate in the corpus to unblock dimension B, and it is exactly
the kind of claim that must not be adopted casually** given the record's history. §3.1, on verified
text, or not at all.

### 18.3 `A-054` — "is push three taken, avoided, or diagnostic?"

> **X19 [26:40]** *"if the dealer hasn't issued three pushes intraday, then he comes back for one
> more"* · **X19 [27:06]** *"waiting for three levels of rise, three pushes of rise — **if he doesn't
> give it… there's always tomorrow**"*
> **X10 [35:57]** *"**That third swipe is to beat up the retail traders.**"*
> **X18 [28:53]** *"**The last push** that the dealer makes to induce everybody to take it is three
> aggressive pushes"* · **X15 [41:10]** *"**vector is that fast last third push that gives us the
> indication that a trap is in progress**"*

**Candidate reading: diagnostic, and a no-trade-yet condition** — the third push is the *signal that
the reversal setup is arriving*, not itself the entry, and its absence is a reason to stand aside.

### 18.4 `A-005` "the trading zone" — a `DO NOT CODE` record gets an explicit definition

> **X08 [23:49]** *"**The trading zone is always set 25 to 50 pips higher than the Asian high or the
> Asian low.** … we measure from the initial high, the **IHOD**, and the **IL**, the initial low of
> the day."*
> **X08 [24:19]** *"where does everybody put their stops? 25, 30, 35, 40, a couple smart alecks 45,
> 50. **The dealer triggers those stops as part of the cycle.**"*

Objectively codable, with a stated rationale. See also §13.

### 18.5 `A-078` — the safety-trade anchor distance, `25 to 75`

The record notes the figure is *printed once as `25 to 75`* and *spoken seven times*. The X-series
adds an **instructor answer to a direct student challenge on exactly this number:**

> **X10 [55:53]** *"Joe, good question. **The safety trade second leg can be up to 75 pips from the
> peak formation, not 50 pips, right? Yes.**"*
> **X10 [56:01]** *"**The range for the safety trade to come in is around 25 to 75 pips above or
> below the peak formation.**"* · **X06 [37:19]** *"The low of the week in this example — how many
> pips? **25 to 75.**"*

The printed figure is the one the instructor defends when challenged. Strong `§3.1` candidate.

### 18.6 `A-042` — "the operative detail is deferred to the DMR." **Confirmed, and the DMR is named**

> **X21 [00:04]** *"**The DMR — the technical analysis of the market.**"*
> **X21 [02:21]** *"**The DMR curriculum** is an added bonus to the market analysis where we go over
> Steve's market maker method in a step-by-step fashion and address all the main points learned
> during the live class."* · **X21 [02:43]** *"part of the **daily market review** session"*
> **X10 [26:58]** *"**When DMR is over, you will start the boot camp cycle.**"*

**DMR = Daily Market Review — an ongoing subscription session held *after* the course.** `A-042`'s
diagnosis is **confirmed, not resolved**: the operative daily detail lives in material this library
does not contain and cannot buy retrospectively. ⭐ **What X21 does supply is one worked instance** —
44 minutes of pair-by-pair level counts and next-day biases (EU, GU, GJ, AU, AJ, EJ, ECAD, GCHF,
UCHF, UCAD, UJ). That is a **ready-made blind-practical answer key**: the calls are on tape with
dates, so the level-count rules of §3 can be scored against the instructor's own labelling.
⚠️ Guest-presented (`D-033`) — usable as a labelling exercise, not as doctrine.

---

*Produced by transcript retrieval against the fixed gap list. No ambiguity closed, no tier
assigned, no lesson ingested. Owner rulings `D-063`/`D-064`/`D-065` applied 2026-08-15.*
