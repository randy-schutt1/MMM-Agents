# DECISION DRAFT — `D-059` (proposed) — THE OWNER'S CANONICAL TRADING TOOLSET

> ## ⛔ NOTHING IN THIS FILE IS A DECISION. NOTHING HERE IS ADOPTED.
>
> One **draft**, prepared on the owner's direct scoping statement of which indicators he needs while
> trading. It is written to the point where the owner can answer **yes / no / edit**, and the
> approved text can be appended to `DECISIONS.md` unchanged.
>
> Until the owner rules:
>
> - **`DECISIONS.md` is unchanged.** No `D-059` exists.
> - ⛔⛔ **NO AMBIGUITY IS CLOSED, EXCLUDED OR MARKED OUT-OF-SCOPE BY THIS FILE.**
>   `A-101`, `A-100`, `A-143`, `A-019`/`A-105`/`A-131`, `A-086` and every record touching
>   `PZ_QuartersTheory`, `PivotPoints.ex4`, `Weekly_High_Low Great`, `Candle Timer` and
>   `ICT Day Of Week` **keep their status exactly as it is.** §6 states this at length because it is
>   the easiest thing in this file to get wrong.
> - ⚠️ **ONE THING IS DEPRIORITISED, AND ONLY ONE, AND ONLY IN ONE SENSE.** Per the owner's
>   2026-08-15 pivot ruling (§5A), **`A-101`'s TOOL-BUILDING priority drops to LOW.**
>   ⛔ **Its STATUS is unchanged (`OPEN`, `DO NOT CODE`) and its COURSE-STUDY priority is
>   unchanged** — pivots are referenced in V10, V15, V16 (dedicated lesson) and V17.
>
> **Numbering, verified rather than assumed.** Swept across integration (`19e6c2a`) **and every
> remote branch**: highest **adopted** entry is **`D-057`**; `D-051`, `D-055`, `D-056` and `D-058`
> are held by **unadopted drafts**. `D-059` is **free on every branch.** ⚠️ `D-047` gives the number
> to whoever **adopts** first — a session adopting this must re-check.

---

## 0. THE ONE-PARAGRAPH SUMMARY, INCLUDING THE THREE PARTS THAT DO NOT GO THE OWNER'S WAY

The owner has scoped the toolset to **four instruments**. ⭐ **This is the most useful thing the
project has been told about its own priorities**: the indicator-folder survey found ~70 artifacts
and `MMM.tpl` carries fourteen, and until now nothing distinguished the load-bearing ones from the
incidental. **Four does that in one sentence.**

⛔ **And then three problems, all of which this draft states before it states anything else.**

1. ⚠️⚠️ **Only ONE of the four is settled.** The TDI has three adopted decisions behind it
   (`D-045`, `D-052`, `D-053`). **The ribbon rests on an unadopted draft, the ADR on an unadopted
   draft, and the EMAs on an ACTIVE CONTRADICTION** (`A-143`). **The owner has named the four things
   that matter and the project can currently compute none of them but the TDI — and not even the
   TDI fully** (`A-086` is still `DO NOT CODE`).
2. ⚠️ **The ribbon description does not match his own chart.** He says the ribbon *"highlights
   sessions **and previous highs and lows**."* On `MMM.tpl` the ribbon draws **sessions only**;
   previous highs and lows come from **two separate indicators** — `!SM_Daily_HiLo` (#7) and
   `Weekly_High_Low Great` (#9). ⭐ **This is the SECOND time he has described the session indicator
   as containing something `MMM.tpl` puts elsewhere** — the first was `A-141`'s High/Low Trainer.
   **A pattern, and §4 says what it might mean rather than which.**
3. ⚠️ **He did not mention pivots** — and **V16 is an entire lesson on pivot points.** §5 put it to
   him rather than resolving it, and ⭐ **he has since ANSWERED: *"Pivot points aren't how I trade.
   It's an added bonus."*** §5A. **A third position, not either reading §5 offered** — his list was
   a ***need*** list and a bonus is not a need, so the omission was principled. ✅ Pivots are
   **non-load-bearing for his practice** and **tool-building priority drops to LOW**;
   ⛔ **`A-101` is NOT closed and its course-study priority is untouched.**

---

## 1. THE ATTESTATION, RECORDED VERBATIM AND UNINTERPRETED

> **Owner, 2026-08-15:** *"The indicators that we'll need while trading are: 1. Worktime ribbon:
> highlights sessions and previous highs and lows. 2. TDI. 3. EMAs. 4. ADR. **I believe that's it.**"*

| # | Named | Descriptor he gave |
|---|---|---|
| 1 | **Worktime ribbon** | *"highlights sessions **and previous highs and lows**"* |
| 2 | **TDI** | — |
| 3 | **EMAs** | — |
| 4 | **ADR** | — |

⚠️ **The closing hedge is recorded, not trimmed.** *"I believe that's it"* is **not** *"that is
it."* This project reads hedges as evidence (`A-086`'s *"I don't know"* analysis is the precedent),
and a **hedged enumeration is not a closed set.** It is strong scoping information and it is **not a
guarantee of completeness** — which is exactly why §5's pivot omission is a question rather than a
finding.

---

## 2. THE TIER — `OWNER EMPIRICAL PREFERENCE`, AND ONE THING IT IS NOT

Classification follows `D-055` §2 and `D-058` §2 and is re-applied, not re-derived:
**`OWNER EMPIRICAL PREFERENCE`** (`D-052`) — the owner reporting **his own practice**, outside the
tiers and outside the `D-048` ladder. **No new tier or rung** (`SOURCING_HIERARCHY.md` §3.5).

> ### ⭐⭐ BUT THIS ONE DIFFERS FROM `D-055`/`D-058` IN KIND, AND THE DIFFERENCE IS THE WHOLE RISK
>
> `D-055` and `D-058` are **rules** — they assert *how to trade*. **This is a SCOPING statement** —
> it asserts *what he uses*. **A scoping statement about the owner's practice says NOTHING about
> what the COURSE teaches**, and therefore **nothing about what this project must study.**
>
> ⛔ **The project exists to study the corpus** (`README.md`, `SOURCING_HIERARCHY.md` §0). **The
> owner's toolset is not the course's curriculum**, and a tool he does not use can still be a tool
> the course teaches — **V16 teaches pivots for forty-four minutes.** Treating this statement as a
> curriculum filter would silently narrow the corpus on non-Tier-1 authority, which is the
> `A-082`/`D-030` error in its most consequential possible form.
>
> ⭐ **What it legitimately governs: PRIORITISATION and TOOL-BUILDING EFFORT**, which is a real and
> valuable thing to govern.

---

## 3. ⭐ THE FOUR, MAPPED ONTO THE PROJECT'S ACTUAL EVIDENCE — THE SCORECARD

| # | Tool | The artifact | Project status | Settled? |
|---|---|---|---|---|
| 1 | **Worktime ribbon** | `!sm_WorkTime_v1.5b` (md5 `b938ee1d…`), `MMM.tpl` #8 | `D-056` **DRAFT, UNADOPTED**; `MMM_SESSION_RIBBON.txt` **draft, never run**; `A-019`/`A-105`/`A-131` **OPEN**; `C-032` proposed | ⛔ **No** |
| 2 | **TDI** | `!SM_TDI` / `MMM_TDI.txt` | ⭐ `D-045` **ADOPTED** (TOOLING), `D-052` **ADOPTED** (band basis), `D-053` **ADOPTED** (primary instrument) | ⚠️ **Mostly** — see below |
| 3 | **EMAs** | six on `MMM.tpl`: 4 · 10 · 50 · 200 · 800 · 3200 | ⚠️⚠️ `D-043` **ADOPTED** says **5 · 13** · 50 · 200 · 800. **The chart says 4 · 10** and adds **3200**. `A-143` **OPEN** | ⛔ **No — actively contradictory** |
| 4 | **ADR** | ⚠️ **three different indicators** | `A-100` **OPEN** (lookback **10 / 14 / 15 / 21**); `D-051` **DRAFT, UNADOPTED**; `C-022` untouched | ⛔ **No** |

> ### ⚠️⚠️ ONE OF FOUR. THAT IS THE HEADLINE OF THIS SECTION.
>
> **The owner has named the four instruments that matter, and three of them rest on unadopted drafts
> or an open contradiction.** ⚠️ **And even the TDI is not fully settled**: `D-053` §2 says in terms
> that fixing the instrument *"does not make the principles computable"*, and **`A-086`'s volatility-
> band PERIOD is still stated nowhere at any tier**, so `A-031`/`A-032` stay uncomputable.
>
> ⭐ **This is the single most actionable output of the ruling**, and it is a *prioritisation* result,
> not a closure: **the shortest path to a computable toolset now runs through `D-056`, `D-051`,
> `A-143` and `A-100`** — and every one of those is waiting on **one owner sentence**, not on more
> research.

### 3.1 ⚠️ *"ADR"* names a family with three members, and does not pick one

| Candidate | Where | Status |
|---|---|---|
| `ADR 1.5 20100528 01 Mod 01` | ⭐ **the course's own**, V07 frames | ⛔ **NOT FOUND anywhere on the volume** (`D-051` §1) |
| `mm_adr` | `Forex222/`, **with MQL4 source**; `ADRPeriod` default **21** | `D-051` **DRAFT, UNADOPTED** |
| ⭐ `Daily Range PeterE`, **`NumOfDays=10`** | ⭐ **on `MMM.tpl` — the one he actually runs** | admitted only by `D-056`, **a draft** |

⭐ **The strongest inference available — and it is only an inference:** *"ADR"* in his list most
plausibly means **the one on his own chart**, `Daily Range PeterE` at `NumOfDays=10`. ⛔ **Not
adopted.** He named a *quantity*, not a *tool*, and `A-100`'s lookback conflict is
**10 / 14 / 15 / 21** with **V16 `[00:09:31]`'s *"the last two weeks, 15 days"* at TIER 1** — which
outranks any chart file. **`A-100` does not close. §8 Q3 asks.**

### 3.2 ⚠️ *"EMAs"* confirms the family and not the membership — `A-143` does not close

His statement **confirms EMAs are load-bearing**, which was never seriously in doubt, and
**resolves nothing about which**:

| | |
|---|---|
| ✅ **Confirmed** | EMAs are in the canonical four |
| ⛔ **Not stated** | how many, which periods, which are load-bearing, or which two cross for `D-058`'s tier-1 entry |
| ⚠️ **Still contradictory** | `D-043` (**adopted**, owner attestation about the *teaching*): **5 · 13** · 50 · 200 · 800. `MMM.tpl` (his *practice*, 2023): **4 · 10** · 50 · 200 · 800 · **3200** |

⛔ **`A-143` STAYS OPEN**, and this statement does not narrow it by a single period. ⭐ **It does
raise its priority sharply**: `A-143` blocks `D-058`'s entire tier 1, and the owner has now
independently confirmed that the object `A-143` is about is one of only four things he needs.

---

## 4. ⚠️ THE RIBBON DESCRIPTION DOES NOT MATCH HIS OWN CHART — the checkable discrepancy

> He says: *"Worktime ribbon: highlights sessions **and previous highs and lows**."*

**Verified directly against `MMM.tpl` (md5 `db617bcdfeb5df26c033036f96c41472`), indicator by
indicator:**

| `MMM.tpl` # | Indicator | What it draws |
|---|---|---|
| **#7** | ⭐ **`!SM_Daily_HiLo`** (`offset=2`) | ⭐ **previous-day high/low** |
| **#8** | **`!sm_WorkTime_v1.5b`** | ⭐ **session boxes ONLY** — Asian / Euro / NY / two market-open windows, plus the ±25/±50 alert bands |
| **#9** | ⭐ **`Weekly_High_Low Great`** | ⭐ **weekly extremes** |

⛔ **The ribbon does not draw previous highs and lows. Two other indicators on his own chart do.**
Its full recovered input surface (`D-056` §4.2) contains **no** daily- or weekly-extreme inputs of
any kind.

### 4.1 ⭐⭐ This is the SECOND instance of the same pattern

| Occasion | He said | `MMM.tpl` says |
|---|---|---|
| `A-141`, 2026-08-15 | *"The high low trainer is **part of the sessions indicator**. It's embedded in it"* | The ribbon has the ±25/±50 level bands; **the order placement is absent, and categorically so** |
| **Here**, 2026-08-15 | the ribbon *"highlights sessions **and previous highs and lows**"* | The ribbon draws **sessions only**; H/L is `!SM_Daily_HiLo` + `Weekly_High_Low Great` |

**Three readings, none excluded, and this draft picks none:**

| # | Reading | What would follow |
|---|---|---|
| **a** | ⭐ He means a **functional bundle** — *"the ribbon"* = the whole box-and-level drawing layer, several MT4 indicators he thinks of as one thing | Most economical. **Then `!SM_Daily_HiLo` and `Weekly_High_Low Great` are IN SCOPE**, as components of item 1 — see §6.1 |
| **b** | ⚠️⚠️ He runs a **NEWER `!sm_WorkTime` build** that genuinely bundles daily/weekly H/L — and perhaps the Trainer's order placement too | ⭐⭐ **This would be the single most valuable artifact the project could receive.** It would close `A-141` and settle `D-056`'s auto-GMT question in one file |
| **c** | Ordinary misrecollection across a 2023 chart and a 2012 course | Then `MMM.tpl` governs and item 1 means the ribbon alone |

⭐ **Reading (b) is cheap to test and nobody has tested it: ask him for the file.** §8 Q2.

---

## 5. ⚠️⚠️ THE PIVOT OMISSION — FLAGGED AS A QUESTION, RESOLVED IN NEITHER DIRECTION

**He did not mention pivot points.** The project has been actively chasing pivot construction:
`A-101` (`M1`–`M4`, `DO NOT CODE`), the `PivotPoints.ex4` find, and `D-056` §7's standing request
for `PivotPoints.mq4` source as *"the single highest-value artifact the owner could supply."*

**Two readings, and choosing between them is exactly what this draft refuses to do:**

| # | Reading | Evidence for it |
|---|---|---|
| **a** | ⭐ **Pivots are genuinely NOT part of his trading approach** | **No pivot indicator is on `MMM.tpl`, `MMM INDICES.tpl` or `RS5P.tpl`** — fourteen slots, none pivots (`D-056` §5.1). `PivotPoints.ex4` sits in a Downloads folder, **not on any chart.** ⭐ **The chart file and the omission AGREE**, and that is a real convergence of two independent signals |
| **b** | He simply did not think to list it | The list is **hedged** (*"I believe that's it"*), it is four items long, and `PZ_QuartersTheory` — a **levels** tool — **is** on his chart and **also** went unmentioned, so the list demonstrably omits things he runs |

⚠️ **Reading (b) has one hard piece of support that must not be skipped: `PZ_QuartersTheory` is on
all three of his templates and he did not list it either.** So the list **provably** under-reports
what is on his charts, which weakens any argument from silence — **including the argument for (a).**

> ### ⛔⛔ AND HERE IS THE PART THAT MATTERS MOST, WHICHEVER READING IS TRUE
>
> **`A-101` DOES NOT CHANGE STATUS, AND ITS PRIORITY FOR COURSE-STUDY PURPOSES DOES NOT DROP.**
>
> **V16 is an entire lesson on pivot points** — it *prints* the grid
> `R2 · M4 · R1 · M3 · CPP · M2 · S1 · M1 · S2` and states the roles out loud and in print
> (`[00:17:53]`–`[00:18:19]`). **That is Tier 1, and Tier 1 is what this project studies.**
>
> ⛔ **Even if the owner confirms reading (a) outright, `A-101` stays OPEN at full priority**, because
> `A-101` asks *what the course taught*, and the answer to that does not depend on what the owner
> trades. §2's distinction is doing real work here: **a scoping statement about practice cannot
> narrow a curriculum.**
>
> ⭐ **What reading (a) WOULD legitimately change:** the priority of **hunting for `PivotPoints.mq4`
> as a TOOL**, and of building a pivot renderer. **Those are effort questions, not evidence
> questions**, and they are exactly what §2 says this ruling may govern.

---

## 5A. ⭐⭐ THE OWNER ANSWERED Q1 — AND THE ANSWER IS A **THIRD** POSITION, NOT (a) OR (b)

> *"Pivot points aren't how I trade. **It's an added bonus.**"* — owner, 2026-08-15

§5 offered two readings: **(a)** pivots are not part of his approach, or **(b)** he forgot to list
them. ⭐ **The answer is neither.** He uses them — as a **supplementary / confluence factor**, not as
a driver. **That is a third position and it is better than either candidate**, because it explains
the omission *principledly* rather than as disuse or oversight:

> ⭐ **His list was a `NEED` list — *"the indicators that we'll **need** while trading"*. A bonus is
> by definition not a need. The omission was therefore CORRECT BY HIS OWN CRITERION, and no
> inference about disuse was ever available from it.**

⚠️⚠️ **AND *"AN ADDED BONUS"* IS NOT *"I DON'T USE THEM"*. THE DIFFERENCE IS LOAD-BEARING AND IS NOT
FLATTENED HERE.** He did not say he ignores pivots; he said they are not **how he trades**. A record
that flattened this to *"the owner does not use pivots"* would overstate his statement in exactly
the direction that would justify dropping the topic — and this draft does not do that.

### 5A.1 ⭐⭐ AND IT AGREES WITH TIER 1 — the course frames pivots the same way

**`04_SCREENSHOTS/V15/V15_00-41-30_confluence-slide-yesterday-high-low-pivot-adr.png`** — the
course's own **confluence** slide, pairing:

```text
yesterday's high/low   ·   PIVOT   ·   ADR
```

⭐⭐ **Two of those three are on the owner's canonical list** — *"previous highs and lows"* (item 1)
and *"ADR"* (item 4). **The third is the one he calls an added bonus.** So the owner's *"bonus"*
framing and the course's *"confluence"* framing describe **the same role for the same object**,
arrived at independently.

⚠️ **This is corroboration of a ROLE, not a closure of a CONSTRUCTION.** It says pivots are used
*for confluence*; it says nothing about **how `M1`–`M4` are computed**, which is the whole of
`A-101`. **`A-101` does not narrow by one line.**

### 5A.2 ⛔ Pivots are referenced in FOUR lessons — the "if" in "if the lessons ever reference it" is already satisfied

| Lesson | Frame |
|---|---|
| **V10** | `V10_01-23-42_gbpusd-15m-with-adr-low-and-pivot.png` |
| **V15** | `V15_00-41-30_confluence-slide-yesterday-high-low-pivot-adr.png` |
| ⭐ **V16** | **nine pivot frames — the dedicated lesson**, title slide through `price-fails-at-m3-pivot-4-times` |
| **V17** | `V17_00-22-00_gbpusd-m15-chart-with-pivot-labels.png` |

⛔ **So `A-101` is not a dormant record waiting for a trigger — it is an ACTIVE course-content record
across four lessons, one of them dedicated.** Any framing that treats it as conditional on some
future reference is **already overtaken by the corpus.**

### 5A.3 ⭐ What actually changes, and what does not

| | |
|---|---|
| ✅ **CONFIRMED** | Pivots are **non-load-bearing for the owner's trading practice**, on his own statement. **They are NOT part of `D-059`'s canonical four.** |
| ✅ **CHANGES** | ⭐ **TOOL-BUILDING PRIORITY drops to LOW** — hunting `PivotPoints.mq4` source, and building a pivot renderer, are **deprioritised**. `D-056` §7's standing request for that source is **downgraded from "the single highest-value artifact the owner could supply" to a low-priority nice-to-have.** |
| ⛔ **DOES NOT CHANGE** | **`A-101` STATUS: `OPEN`, `DO NOT CODE`.** Its **course-study** priority is **untouched** — V16 is a dedicated lesson and `A-101` asks what the course taught |
| ⛔ **DOES NOT CHANGE** | The **`M5` addendum** stays live: *"DO NOT assume the printed nine levels are exhaustive"*, with required research across V17–V21 |
| ⚠️ **NOT ESTABLISHED** | **How** he uses pivots as a bonus — as confluence with the four? as a level filter? — and therefore **whether a pivot tool is eventually wanted at all.** §8 Q6 |

### 5A.4 ⭐ It also retro-explains the `PZ_QuartersTheory` omission — as a hypothesis

§5 leaned hard on *"the list omits `PZ_QuartersTheory`, which IS on all three templates"* to argue
that silence established nothing. ⭐ **The `need`-vs-`bonus` distinction supplies a candidate
explanation for that omission too**: quarters/round-number levels are plausibly **also** a bonus
confluence layer rather than a need.

⚠️ **A hypothesis, not a finding — the owner has not said it**, and §8 Q5 already asks. **§5's
reasoning is NOT retracted**: it was correct that *at the time* no inference from silence was
available.

---

## 6. ⛔⛔ WHAT THIS RULING DOES **NOT** DO — stated at length, because it is the easiest error here

**No record is closed, excluded, deprioritised, or marked out-of-scope. Not one.**

| Artifact / record | Status after this draft |
|---|---|
| `PZ_QuartersTheory` (on all three templates) | ⭐ **Every record stands.** `D-056` §5.3's finding — that it is a **round-number grid and NOT a pivot tool** — is unaffected |
| `PivotPoints.ex4` / `A-101` | **OPEN, `DO NOT CODE`, full priority.** §5 |
| `Weekly_High_Low Great`, `!SM_Daily_HiLo` | ⚠️ **Arguably IN scope** — see §6.1 |
| `Candle Timer`, `ICT Day Of Week` | Unmentioned; **cosmetic on the evidence** (`D-056` §2). **No record about them changes** |
| `mm_adr`, `D-051` | Untouched; still an unadopted draft |
| `A-100`, `A-086`, `A-019`, `A-105`, `A-131`, `A-143`, `C-022`, `C-032` | ⛔ **ALL OPEN AND UNCHANGED** |

⚠️ **The reason this section is emphatic.** An owner statement that four things matter is very easy
to read as *"the other ten do not."* **He did not say that.** He answered *what he needs while
trading*; **he did not survey his chart and rule things out**, and §5 proves the list under-reports
his own templates. **An argument from silence at `OWNER EMPIRICAL PREFERENCE` tier cannot close a
Tier 1 record**, and `SOURCING_HIERARCHY.md` §2's *"silence is never permission"* applies to the
owner's silence exactly as it applies to the corpus's.

### 6.1 ⭐ The two indicators the wording arguably pulls INTO scope

Under §4 reading (a) — *"the ribbon"* as a functional bundle — **`!SM_Daily_HiLo` and
`Weekly_High_Low Great` are components of item 1**, because *"previous highs and lows"* is a
function he **named explicitly** and those are the tools on his chart that deliver it.

⭐ **So the canonical set may be four FUNCTIONS delivered by SIX indicators**, not four indicators.
⛔ **Not adopted** — it depends on which §4 reading is true. **§8 Q2 settles both at once.**

---

## 7. THE PROPOSED LEDGER ENTRY — TEXT FOR THE OWNER TO APPROVE, EDIT OR REJECT

> ## D-059 — The owner scopes the canonical trading toolset to FOUR instruments; this governs PRIORITISATION ONLY, closes NO record, and EXCLUDES NOTHING from course study
>
> **Date:** 2026-08-15
> **Category:** `OWNER EMPIRICAL PREFERENCE` (`D-052`) — the owner reporting his own practice,
> **outside the tiers and outside the `D-048` ladder**. **No new tier or rung.**
>
> **Part 1 — the statement.** The owner attests, 2026-08-15: *"The indicators that we'll need while
> trading are: 1. Worktime ribbon: highlights sessions and previous highs and lows. 2. TDI. 3. EMAs.
> 4. ADR. I believe that's it."* ⚠️ **The hedge is part of the record** — *"I believe that's it"* is
> not *"that is it"*, and a hedged enumeration is **not a closed set**.
>
> **Part 2 — ⛔⛔ WHAT THIS DOES NOT DO.** **It closes, excludes and deprioritises NOTHING.** It is a
> statement about the owner's **practice**, not about the **course's curriculum**, and **the project
> exists to study the corpus.** ⛔ **No record concerning `PZ_QuartersTheory`, `PivotPoints.ex4`,
> `Weekly_High_Low Great`, `Candle Timer`, `ICT Day Of Week`, `mm_adr` or anything else changes
> status.** An argument from silence at this tier cannot close a Tier 1 record —
> `SOURCING_HIERARCHY.md` §2's *"silence is never permission"* applies to the owner's silence too.
> ⚠️ **And the list demonstrably under-reports his own charts**: `PZ_QuartersTheory` is on all three
> of his templates and went unmentioned.
>
> **Part 3 — ⚠️⚠️ WHAT IT REVEALS: ONE OF THE FOUR IS SETTLED.** **TDI** has three adopted decisions
> (`D-045`, `D-052`, `D-053`) — ⚠️ and even so `A-086`'s band **period** is stated nowhere, so
> `A-031`/`A-032` stay uncomputable. **The Worktime ribbon** rests on `D-056`, **an unadopted draft**,
> with `A-019`/`A-105`/`A-131` open. **The ADR** rests on `D-051`, **an unadopted draft**, with
> `A-100`'s lookback conflict **10 / 14 / 15 / 21** live, and *"ADR"* **names three different
> indicators without picking one**. **The EMAs** are **actively contradictory**: `D-043` (adopted)
> says **5 · 13** · 50 · 200 · 800 and `MMM.tpl` says **4 · 10** · 50 · 200 · 800 · **3200**
> (`A-143`, OPEN). ⭐ **The owner has named the four things that matter and the project can compute
> none of them but the TDI. The shortest path to a usable toolset runs through `D-056`, `D-051`,
> `A-143` and `A-100` — and each waits on ONE OWNER SENTENCE, not on more research.**
>
> **Part 4 — ⚠️ the ribbon description does not match his chart, and this is the SECOND instance.**
> He describes the ribbon as highlighting *"sessions **and previous highs and lows**."* On `MMM.tpl`
> the ribbon (#8) draws **sessions only**; previous highs and lows are **`!SM_Daily_HiLo`** (#7) and
> **`Weekly_High_Low Great`** (#9). The ribbon's full input surface contains no daily/weekly-extreme
> input. ⭐ **`A-141` was the first instance** (*"the high low trainer is part of the sessions
> indicator"*). **Three readings stand and none is adopted:** a functional **bundle**; ⭐⭐ a **newer
> `!sm_WorkTime` build** that really does bundle them — *which would be the most valuable artifact
> the project could receive, closing `A-141` and settling `D-056`'s auto-GMT question at once*; or
> ordinary misrecollection. ⚠️ Under the bundle reading, **`!SM_Daily_HiLo` and
> `Weekly_High_Low Great` are IN SCOPE as components of item 1**, making the set **four functions
> delivered by six indicators.** Not adopted.
>
> **Part 5 — ⚠️⚠️ pivots were not mentioned, and this is NOT resolved in either direction.** ⭐ The
> omission **agrees with his chart files** — no pivot indicator is on any of his three templates, and
> `PivotPoints.ex4` sits unused in a Downloads folder. ⚠️ **But the list also omits
> `PZ_QuartersTheory`, which IS on all three**, so silence here does not establish disuse.
> ⛔⛔ **`A-101` STAYS OPEN AT FULL PRIORITY FOR COURSE STUDY REGARDLESS**, because **V16 is an
> entire lesson on pivot points** and prints the grid `R2 · M4 · R1 · M3 · CPP · M2 · S1 · M1 · S2`
> at Tier 1 — and `A-101` asks **what the course taught**, which does not depend on what the owner
> trades. ⭐ What a confirmed *"I don't use pivots"* **would** change is the priority of **hunting
> `PivotPoints.mq4` and building a pivot renderer** — effort questions, not evidence questions.
> **Put to the owner as `D-059` §8 Q1.**
>
> **Part 5A — ⭐⭐ THE PIVOT QUESTION IS ANSWERED, AND `A-101` STILL DOES NOT CLOSE.** The owner
> ruled: *"Pivot points aren't how I trade. **It's an added bonus.**"* ⭐ **This is a THIRD position,
> not either reading Part 5 offered** — he uses pivots as a **supplementary / confluence** factor,
> not as a driver, and since his list was a ***need*** list, **the omission was correct by his own
> criterion and no inference about disuse was ever available from it.**
> ⚠️⚠️ ***"An added bonus"* is NOT *"I don't use them"***, and this entry does not flatten it.
> ⭐⭐ **It agrees with Tier 1**: V15's own **confluence** slide pairs *yesterday's high/low · PIVOT ·
> ADR* — **two of which are on the canonical list** — so the owner's *"bonus"* and the course's
> *"confluence"* describe the same role for the same object, arrived at independently. ⚠️ That
> corroborates a **ROLE**, not a **CONSTRUCTION**.
> ✅ **CONFIRMED: pivots are NON-LOAD-BEARING for the owner's trading practice and are NOT part of
> the canonical four.** ✅ **TOOL-BUILDING PRIORITY DROPS TO LOW** — hunting `PivotPoints.mq4` and
> building a pivot renderer are deprioritised, and **`D-056` §7's description of that source as
> *"the single highest-value artifact the owner could supply"* is DOWNGRADED to a low-priority
> nice-to-have.**
> ⛔⛔ **AND `A-101` IS NOT CLOSED AND ITS COURSE-STUDY PRIORITY IS UNCHANGED.** It stays **`OPEN`,
> `DO NOT CODE`.** Pivots are referenced in **FOUR lessons — V10, V15, V16 (dedicated, nine frames),
> V17** — so it is an **active** course-content record, not one awaiting a future trigger. `A-101`
> asks **what the course taught**, and that does not depend on what the owner trades (§2). The
> **`M5` addendum** stays live in full.
>
> **Part 6 — `A-143` does not close.** *"EMAs"* confirms the **family** is load-bearing and states
> **nothing** about membership — not how many, not which periods, not which two cross for `D-058`'s
> tier-1 entry. **`D-043` and `MMM.tpl` still disagree on the fast pair.** ⭐ It does **raise
> `A-143`'s priority sharply**: it blocks `D-058` entirely and the owner has now independently
> confirmed the object it concerns is one of only four he needs.
>
> **Reason:** the indicator survey found ~70 artifacts and `MMM.tpl` carries fourteen, with nothing
> distinguishing load-bearing from incidental. This supplies that distinction in one sentence, and it
> is the best prioritisation signal the project has received. Recording it accurately at a weak tier
> — as scope, not as doctrine — is strictly better than either acting on it as a curriculum filter or
> losing it.
>
> **Evidence:** owner attestation, 2026-08-15 (§1, verbatim). `MMM.tpl` (md5
> `db617bcdfeb5df26c033036f96c41472`, fourteen indicators, verified #7/#8/#9 for Part 4);
> `MMM INDICES.tpl`; `RS5P.tpl`; `INDICATOR_FOLDER_INVENTORY_2026-08-14.md`; `D-043`, `D-045`,
> `D-051`, `D-052`, `D-053`, `D-055`, `D-056`, `D-058`; `A-086`, `A-100`, `A-101`, `A-105`, `A-141`,
> `A-143`, `A-019`, `A-131`, `C-010`, `C-022`, `C-032`; V16 `[00:09:31]`, `[00:17:53]`–`[00:18:19]`;
> `SOURCING_HIERARCHY.md` §2, §3.5; `D-030`.
>
> **Alternatives considered:** *Marking the unlisted indicators OUT OF SCOPE* — ⛔ **rejected, and it
> is the central discipline of the entry**; he answered what he needs while trading, he did not
> survey his chart and rule things out, and the list provably omits `PZ_QuartersTheory` which he
> runs. *Deprioritising `A-101` on the pivot omission* — rejected; V16 teaches pivots at Tier 1 and a
> practice statement cannot narrow a curriculum. *Reading "ADR" as `Daily Range PeterE`* — **not
> adopted**, though it is the most plausible reading, because V16's Tier 1 *"15 days"* outranks a
> chart file and `A-100` stays open. *Reading "EMAs" as endorsing `MMM.tpl`'s 4/10 over `D-043`'s
> 5/13* — rejected; he named a family, not periods. *Treating the ribbon description as authoritative
> over `MMM.tpl`* — rejected; the template is a verifiable artifact and the description is
> recollection, but **neither is promoted over the other here** — the discrepancy is surfaced, not
> adjudicated.
>
> **Consequences:**
>
> 1. ⭐ **Prioritisation, and this is the entry's real product.** Work on the toolset orders itself:
>    **`D-056` (ribbon) · `D-051` (ADR) · `A-143` (EMA set) · `A-100` (ADR lookback)** — the four
>    blockers standing between the owner's own four instruments and a computable toolset. **Each
>    needs one owner sentence.**
> 2. ⛔ **No `A-xxx` or `C-xxx` changes status.** Per `D-045` rule 2, **admission is not reading**;
>    here, **scoping is not closing.**
> 3. ⚠️ **The §3.4 re-check obligation attaches.** A later Tier 1 statement about which indicators
>    the method requires governs over this and triggers `SOURCING_HIERARCHY.md` §3.1.
> 4. ⭐ **Four questions are owed to the owner** (§8), of which **Q1 (pivots)** and **Q2 (a newer
>    ribbon build)** are the highest-value in the project right now.
> 5. `12_MASTER_SPEC` / `13_MACHINE_SPEC` gain **nothing** from this entry.
>
> **Status:** ACTIVE — `OWNER EMPIRICAL PREFERENCE`, **SCOPING ONLY**, **CLOSES NOTHING**,
> **EXCLUDES NOTHING FROM COURSE STUDY**

---

## 8. THE QUESTIONS FOR THE OWNER

1. ✅ **ANSWERED 2026-08-15 — see §5A.** *"Pivot points aren't how I trade. It's an added bonus."*
   ⭐ Pivots are **non-load-bearing for your practice** and **not in the canonical four**;
   tool-building priority drops to **LOW**. ⛔ **`A-101` stays `OPEN` for course study** — V16 is a
   dedicated lesson. ⚠️ **Residual, now §8 Q6.** *(Original question retained below.)*
   ~~**Do you use pivot points at all?** §5.~~ You did not list them, and **no pivot indicator is on
   any of your three templates** — which agrees with the omission. But V16 is a **whole lesson** on
   them, and the project has been hunting `PivotPoints.mq4` on the assumption they matter. ⚠️ **Either
   answer is useful and neither is assumed.** *(Note: the project will keep studying V16's pivots
   either way — that is the course's content. This only changes whether we build a pivot tool.)*
2. ⭐⭐ **Does your Worktime ribbon actually draw previous highs and lows?** §4. On `MMM.tpl` that
   comes from two **separate** indicators (`!SM_Daily_HiLo`, `Weekly_High_Low Great`) and the ribbon
   draws sessions only. ⭐ **If you are running a NEWER `!sm_WorkTime` build that bundles them — and
   perhaps the High/Low Trainer's order placement too — that file is the single most valuable
   artifact you could send.** It would close `A-141` and settle the ribbon's GMT question at once.
3. **Which ADR?** §3.1. Three exist: the course's own `ADR 1.5 20100528` (**not found anywhere**),
   `mm_adr` (source, default 21), and `Daily Range PeterE` at **`NumOfDays=10`** — the one on your
   chart. ⚠️ **And what lookback?** V16 `[00:09:31]` says *"the last two weeks, **15 days**"*; your
   chart says **10**.
4. **Which EMAs?** §3.2 — still the open question from `D-058`. Your chart runs **4 · 10** · 50 · 200
   · 800 · 3200; `D-043`, on your own earlier attestation about the teaching, is **5 · 13** · 50 ·
   200 · 800. **Both cannot be the canonical set**, and `D-058`'s entry trigger depends on which.
5. **Is `PZ_QuartersTheory` in or out?** It is on **all three** of your templates and you did not
   list it. ⭐ **Sharpened by Q1's answer:** is it, like pivots, **an added bonus** rather than a
   need? §5A.4 offers that as a hypothesis and it is **not** assumed.
6. ⭐ **NEW — HOW do you use pivots as a "bonus"?** §5A.3. Confluence with the four? A level filter?
   ⚠️ *"An added bonus"* is **not** *"I don't use them"*, so this decides whether a pivot renderer is
   **eventually** wanted at all — not just whether it is urgent. ⭐ Note that **V15's own confluence
   slide pairs *yesterday's high/low · pivot · ADR*, and two of those three are on your list** — so
   the course appears to frame pivots exactly as you do.
