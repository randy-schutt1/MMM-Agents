# DECISION DRAFT — `D-055` (proposed) — `MMM.tpl`, THE TIME RIBBON, AND THE PIVOT SEARCH

> ## ⛔ NOTHING IN THIS FILE IS A DECISION. NOTHING HERE IS ADOPTED.
>
> One **draft**, prepared on the owner's remarks *"the pivot points may be in there"* and
> *"the time ribbon — we can replicate exactly."* It mirrors `D-045` and
> `DECISION_DRAFT_D-051` exactly, including the two disciplines that made `D-045` survivable:
> **admission is per-artifact, and admission is not reading.**
>
> Until the owner rules:
>
> - **`DECISIONS.md` is unchanged.** No `D-055` exists.
> - **`SOURCING_HIERARCHY.md` §1's `TOOLING` rung is unchanged** — it admits
>   `Ultimate Blue.tpl` / `!SM_TDI` **and nothing else** (`D-051` would add `mm_adr`; it is also
>   unadopted).
> - **`A-019`, `A-105`, `A-131`, `A-101`, `A-100`, `A-084`, `A-086`, `A-020` are ALL OPEN and
>   unchanged.**
> - **`06_MANUAL_BACKTEST/tools/MMM_SESSION_RIBBON.txt` is a DRAFT TOOL** and may be cited by
>   nothing.
>
> **Numbering.** `D-053` is the highest adopted entry; `D-054` is claimed by
> `DECISION_DRAFT_D-054_OWNER_STOP_AND_TARGETS.md`. This draft claims **`D-055`**.
>
> **The full survey this draft rests on is `INDICATOR_FOLDER_INVENTORY_2026-08-14.md`.**

---

## 0. THE ONE-PARAGRAPH SUMMARY, INCLUDING BOTH PARTS THAT DO NOT GO THE OWNER'S WAY

`MMM.tpl` was found — **the owner's entire MMM chart, fourteen indicators, every input value
saved.** It is the most informative artifact this project has been handed, and the session ribbon
the owner named is indicator #8 in it, with **six clock boundaries recovered exactly.**

⛔ **And the two things the owner hoped for are the two that do not fully arrive.**

1. **"Replicate exactly" is available for the GEOMETRY and not for the CLOCK.** The ribbon binary
   is packed and sourceless, and its sibling's filename — `no_autogmt` — is evidence that the build
   the owner runs performs an **automatic GMT adjustment whose rule cannot be read from any
   artifact on the volume.** A faithful port must therefore take the offset as an owner-supplied
   input, and that is what the draft port does.
2. **A pivot indicator exists and is not on the MMM chart.** `PivotPoints.ex4` carries a
   `Plot_middle` / `Color_Mid` pair — precisely the object `A-101` lacks — but it is **absent from
   all three MMM templates**, compiled with no source, and unattested. **`A-101` does not move.**

⭐ **And then the interesting thing happened, as in `D-051`.** Crossing the ribbon's saved
boundaries against `A-105`'s printed slide produced **the first mechanism the project has ever had
that could settle the session clock on arithmetic rather than on choosing** — and it turns on a
single fact the owner can supply in one sentence. §4.5.

---

## 1. THE ARTIFACT

| | |
|---|---|
| **Path** | `Desktop/Trading/Indicators/MMM.tpl` |
| **md5** | `db617bcdfeb5df26c033036f96c41472` |
| **Size / date** | 121,164 bytes · saved 2023-08-15 · `USDNOK` H1 |
| **Format** | ⭐ **Plain ASCII.** Every input value is readable — no decompilation, no inference |
| **Siblings** | `MMM INDICES.tpl` (`e6f977f56e5c87048795a8b344759a61`, `UK100` H1) · `RS5P.tpl` (`2709e6f6b972e6fc4d176165294d01d4`, `USDJPY` H1 — a different method) |

⚠️ **Provenance caveat, stated up front as `D-045` requires.** The file is dated **2023**, against a
**2012** course. It is the owner's *current* chart, not a course artifact. This is the same
weakness `D-045` carried (2016/2019 artifact, 2012 course) and it is not smaller here.

⚠️ **And the folder is not the one the owner named.** The owner said *"Forex222"*.
`Documents/Forex indicator/Forex222/` is **byte-for-byte unchanged** since the `D-051` survey —
**nothing was added there.** `MMM.tpl` is in `Desktop/Trading/Indicators/`. §7 Q1 asks which folder
was meant, because if the owner believes he added files to Forex222, **something did not land.**

---

## 2. ⭐ WHY THIS ARTIFACT IS WORTH MORE THAN THE SUM OF ITS INPUTS

`D-045` admitted a template to get at **one** indicator. This one carries **the whole chart**, and
that changes what it can testify to:

| | |
|---|---|
| ⭐ **It is a CONFIGURATION, not a parameter** | It says which fourteen tools run *together*. No prior artifact stated a stack |
| ⭐ **Three templates agree on the skeleton** | The six EMAs and `!sm_WorkTime_v1.5b` appear in `MMM.tpl`, `MMM INDICES.tpl` **and** `RS5P.tpl`, unchanged. Consistency across three saves and three instruments |
| ⭐ **It answers a negative question** | ⛔ **There is no pivot indicator in it.** A stack that omits a tool is evidence about the tool |
| ⚠️ **It is ONE user's habit, saved three times** | ⚠️⚠️ **Three templates are NOT three witnesses.** They are one installation, one person, one set of habits. §6 applies this against `A-084`, where it matters most |

---

## 3. ⚠️ WHAT `MMM.tpl` SAYS ABOUT THE MOVING AVERAGES — AND WHY IT IS PUT TO THE OWNER, NOT USED

**Saved: EMA on close, periods 4 · 10 · 50 · 200 · 800 · 3200.**

| Against | Result |
|---|---|
| `C-010` (the 800) | ✅ **Supports the corpus.** A third independent presence of the 800, against `MMM-NOTES` p.38's *"5 / 13 / 50 / 200, no 800"* |
| The **type** | ✅ `method=1` = **EMA**. The corpus never states SMA-vs-EMA outright |
| `D-043` (**mustard = 5 · ketchup = 13**) | ⚠️⚠️ **DISAGREES. The template says 4 and 10.** |
| The corpus generally | ⚠️ **3200 appears nowhere at any tier** |

⛔ **THIS DRAFT DOES NOT TREAT THAT AS EVIDENCE AGAINST `D-043`, AND THE REASON IS THE PROJECT'S
OWN.** `D-043` is **owner attestation about what was TAUGHT** — testimony about the 2012 lessons,
sitting *outside* the tiers (`D-041`). A 2023 chart file is **owner practice**, the `D-052`
`OWNER EMPIRICAL PREFERENCE` category. `SOURCING_HIERARCHY.md` §3.5 draws exactly this line:
*"the owner testifying to what was TAUGHT"* versus *"the owner judging what the INSTRUMENT DOES."*
**A 4/10 chart in 2023 is not testimony that the course taught 4/10 in 2012, and treating it as one
would repeat the `D-041` error the `D-043` reversal exists to warn about.**

⭐ **It is, however, a real divergence and it is owed to the owner as a question** — §7 Q3.
**`A-020` is untouched. `D-043` stands. Nothing is coded.**

---

## 4. ⭐⭐ THE TIME RIBBON

### 4.1 The saved boundaries — the substance of the find

`!sm_WorkTime v1.5b AML` · `!sm_WorkTime_v1.5b.ex4` md5 `b938ee1df8cf16a44bc16db71795e9f2`

| Band | Inputs | **Saved value** | Drawn? |
|---|---|---|---|
| **Asian** | `Begin_1`/`End_1` | **`0:00` → `8:00`** | ✅ + text + midline (`asian_midline_hours=9`, yellow) |
| **Euro** | `Begin_2`/`End_2` | **`8:30` → `14:00`** | ⛔ **`draw_euro_box=false`** — configured, switched **off** |
| **New York** | `Begin_3`/`End_3` | **`16:30` → `20:00`** | ✅ + text |
| **"Market open" A** | `Begin_5a`/`End_5a` | **`10:00` → `11:00`** | ✅ |
| **"Market open" B** | `Begin_5b`/`End_5b` | **`16:00` → `17:00`** | ✅ |

`NumberOfDays=50`; every alert **off**; `DrawStopHuntBox=false`.

⭐ **The author's own name for band 5 is `mktopen`.** That is the indicator telling us what
`10:00–11:00` and `16:00–17:00` are: **two market opens**, not two sessions.

⭐ **And two switched-off inputs are independently interesting:** `Alert25BlueBox` /
`Alert50BlueBox`, whose strings in the readable sibling build are literally
**`25 Pips above blue box`** / **`50 Pips below blue box`**. That is `A-005`'s *"the trading zone is
set 25 to 50 pips higher (or lower) than the Asian range"* **shipped as an alert** — and it is the
same 25/50 pair the owner's stop rule uses (`D-054` §3.3). ⚠️ **Corroboration of a band, not a
closure**: `A-005` is blocked on `A-019`/`D-031`, i.e. on the clock.

### 4.2 What was recoverable, and what was not

| Question | Answer |
|---|---|
| The saved clock values | ✅ **Exact**, from `MMM.tpl` plain text |
| The full input surface | ✅ **Exact** — recovered from the **pre-600 sibling** `sm_WorkTime_no_autogmt.ex4` (`8f0059bd…`), whose strings are readable |
| Object naming | ✅ `WT_1`…`WT_5`, `WT_T1`…`WT_T5`, `WT_SH` |
| The **box top/bottom** rule | ⚠️ **NOT readable.** Reconstructed from the standard MT4 idiom (session high / session low) |
| The **midline** semantics | ⚠️ **NOT readable**, and internally odd — see below |
| ⛔ **The GMT adjustment** | ⛔ **NOT readable, and this is the one that matters** — §4.4 |
| Band 4 (`Begin_4`/`End_4`) | ⚠️ **Absent from `MMM.tpl` entirely.** v1.5b appears to have dropped it — an inference from an absence |

⚠️ **The midline is internally odd and the draft flags rather than smooths it.** The Asian box is
**8 hours** (`0:00`–`8:00`) and `asian_midline_hours` is **9**. *A midline parameterised by a number
larger than the box it belongs to cannot mean "the middle of the box."* Two readings survive —
(a) the box mid-price **projected forward 9 hours**, (b) a line **at hour 9** unrelated to the
mid-price. **Neither is readable.** The port implements (a), labels it `[GUESS]`, and names it as
the first thing the acceptance test should look at.

### 4.3 ⛔⛔ THE LIMIT ON "REPLICATE EXACTLY" — STATED BEFORE THE PLAN, NOT AFTER IT

> **`!sm_WorkTime_v1.5b.ex4` is an MT4 build-600+ packed binary. `strings` returns pure noise.
> `find ~ -iname "*WorkTime*"` returns the two `.ex4` files and NOTHING ELSE — no source exists
> anywhere on this volume.**
>
> **And the sibling is named `no_autogmt`.** A build advertising the *absence* of automatic GMT
> handling is evidence that **v1.5b HAS it** — and that rule is inside the packed binary.

The consequence is exact and it is not a quibble:

- **If v1.5b applies no offset**, `Begin_1=0:00` means midnight **on an unidentified broker's
  server clock** — the identical limitation `D-051` §4 hit on the ADR day boundary.
- **If v1.5b auto-adjusts**, the saved values are in a **normalised** clock and the normalising rule
  is unreadable.

**Neither branch is decidable from any artifact found.** ⭐ One readable source *does* fix what the
adjustment is *extra to*: KimIV's `Sessions.mq4` — a **different, unattested** tool, cited for
mechanism only — shows the baseline MT4 idiom is `StrToTime(date + " " + "08:00")`, which resolves
in **server time with no conversion.** That sharpens the question; it does not answer it.

### 4.4 THE REPLICATION PLAN — `06_MANUAL_BACKTEST/tools/MMM_SESSION_RIBBON.txt`

**Written and included as a DRAFT.** Pine v6, price pane, same family as `MMM_TDI.txt` /
`MMM_Indicator.txt`.

**Design rules, each one a consequence of §4.2–4.3:**

| # | Rule |
|---|---|
| 1 | ⭐ **Every default is the owner's saved value, transcribed field for field.** Nothing invented, nothing rounded — including `draw_euro_box=false`, so the Euro band is **configured and off**, exactly as saved |
| 2 | ⭐⭐ **The clock is an INPUT, never a constant.** `ribbonTZ` is exposed. UTC+2 is pre-filled with an in-file warning that **this is the project's inference, not a source** |
| 3 | Both unreadable behaviours are marked **`[GUESS]`** inline, at the code that implements them |
| 4 | Band 4 is **omitted**, with the reason in the header |
| 5 | The 25/50 alert bands are implemented **switched off**, matching the template, and labelled *not a course rule* |
| 6 | ⛔ **Four warnings at the top and a restatement at the bottom** that the file closes `A-019`/`A-105`/`A-131` and establishes no session boundary |

⚠️ **AND IT HAS NOT BEEN RUN.** It is written to v6 syntax and reviewed by eye. **No TradingView
execution, no visual comparison against the owner's MT4 ribbon.** That is stated in the file itself
as WARNING 3, because a tool that claims fidelity it has not demonstrated is worse than no tool.

> ### ⭐ THE ACCEPTANCE TEST — PRE-REGISTERED HERE AND DELIBERATELY NOT RUN
>
> **It needs one thing this session does not have: a screenshot of the owner's live MT4 chart with
> the ribbon on it, with the broker and server time visible.** Given that:
>
> 1. Set `ribbonTZ` to the owner's actual broker offset. **Record it** — this alone is worth more
>    than the rest of the test.
> 2. Compare **box left/right edges** bar-for-bar on one full session. ✅ A match confirms the
>    geometry AND the offset simultaneously.
> 3. Compare **box top/bottom** — tests the `[GUESS]` at §4.2.
> 4. Compare the **midline**: does it sit at the box mid-price, and does it extend 9 hours past
>    `End_1`? — tests reading (a) against (b).
> 5. ⭐ **Run it across a DST transition.** ⚠️⚠️ **This is the decisive step and the only one that
>    can settle §4.3's auto-GMT question:** if the MT4 boxes **hold their clock times** across the
>    change, v1.5b normalises; if they **shift by an hour**, it does not. **A one-day test answers
>    a question no amount of file inspection can.**
>
> **Pre-registering it before the data exists is the point** — it cannot then be tuned to the
> answer. This is the `D-051` §5 discipline, reused.

### 4.5 ⭐⭐ THE `A-105` COLLISION — THE MOST CONSEQUENTIAL THING IN THIS DRAFT

`A-105` is the corpus's **only** printed, timezone-stamped session boundary:
**`London Session Start · 2:00 To 3:00 AM, EST`** — V16, slide dated **2012-05-06**, *inside US
daylight time*. Its entire open question is **one hour**: is `EST` literal (UTC−5), or NY-local
(EDT, UTC−4)?

**The ribbon's London-open box is `10:00–11:00` server. Cross the two:**

| Slide reading | → UTC | Server **UTC+2** | Server **UTC+3** |
|---|---|---|---|
| **`EST` literal (UTC−5)** | 07:00–08:00 | 09:00–10:00 — *abuts the box* | ⭐⭐ **10:00–11:00 — EXACTLY THE BOX** |
| `EST` = NY-local (EDT, UTC−4) | 06:00–07:00 | 08:00–09:00 — 2 h early | 09:00–10:00 — *abuts* |

⭐ **The slide is dated inside US daylight time, when a UTC+2/+3 broker sits on UTC+3. That cell —
`EST` read LITERALLY, on a summer clock — is the ONE combination of four in which the course's own
printed slide coincides EXACTLY with the owner's own ribbon's London market-open box.**

⭐ **And it is independently supported.** The same UTC+2 hypothesis puts `Begin_3=16:30` on the
**NYSE cash open (09:30 ET)**, `Begin_5b=16:00` on **09:00 ET**, `Begin_2=8:30` on the **Frankfurt
open (07:30 CET)**, and `Begin_1`–`End_1` on **Tokyo (07:00–15:00 JST)**. **Five boundaries, one
offset, all landing on real market events.**

> ### ⛔⛔ AND IT IS NOT ADOPTED. `A-019`, `A-105` AND `A-131` STAY OPEN.
>
> **The chain has this session's own arithmetic at its base.** The offset in §4.5 is *inferred from
> the boundaries it then explains*, which is circular unless the offset is independently attested.
> Under `SOURCING_HIERARCHY.md` §3.2 **Case C** and `D-048`'s **rung 4** — *"anything else,
> INCLUDING any case where a rung would close a load-bearing record"* — **this is put to the owner,
> not decided here.** `A-019` is the record that gates `D-031`, `A-005` and every timing rule in the
> corpus; it is as load-bearing as records get.
>
> ⭐ **What this legitimately is:** the first mechanism the project has found by which the session
> clock could close **on arithmetic instead of on choosing** — and it turns on **exactly one fact:
> the GMT offset of the MT4 server the owner's charts ran on.** That is the same shape as `D-052`'s
> *"the period is the one input that could settle this"*, and it is §7 Q2.

---

## 5. ⚠️ THE PIVOT SEARCH — THE ANSWER IS "FOUND, BUT NOT ON THE MMM CHART"

### 5.1 The negative result comes first, because it is the stronger one

⛔ **There is no pivot indicator in `MMM.tpl`, in `MMM INDICES.tpl`, or in `RS5P.tpl`.** Fourteen
slots in the owner's own MMM chart and not one draws pivots. `PZ_QuartersTheory` is a **round-number
grid**, not a pivot tool — Quarters Theory divides the *price scale*; floor-trader pivots derive
from the **previous period's H/L/C**, and `A-101`'s grid has a `CPP`. **Reading the quarters tool as
the course's pivot tool would be the `A-082` error and is not done here.**

### 5.2 The candidate that does exist

**`PivotPoints.ex4`** · `Desktop/All Folders/Downloads/` · md5 `703ec775dcdff4c6995a722209ce0f2f` ·
11,304 bytes · 2018-07-13 · `Copyright © 2010, Forex Profit Launcher`

```text
CountDays · Plot_pivots · Plot_middle · Plot_camarilla
Color_PP · Color_Res · Color_Sup · Color_Mid
Color_H4 H3 H2 H1 · Color_L1 L2 L3 L4
```

⭐ **`Plot_middle` + `Color_Mid` — a switch and colour SEPARATE from `Color_PP`/`Color_Res`/
`Color_Sup` — is exactly the class of object `A-101` is missing:** the interstitial levels between
`CPP`, `R1`/`R2` and `S1`/`S2`. The `H1`–`H4`/`L1`–`L4` family is **Camarilla**, gated by its own
switch, so the `Mid` family is **not** Camarilla.

### 5.3 ⛔ Why `A-101` does not move

| | |
|---|---|
| **Not on the owner's chart** | Absent from all three MMM templates. The `TOOLING` rung is *"the owner's working configuration for this method"* (`D-045`) — **this has no such attestation and the templates argue against one** |
| ⛔ **Compiled, no source** | Packed `.ex4`; no `.mq4` anywhere on the volume. **The input NAMES are recoverable; the FORMULA is not.** Concluding that `Plot_middle` draws midpoints is **reading a variable name**, which is `D-030`'s exact prohibition |
| **`A-101` asks for a construction** | `A-101` already records that the midpoint reading *"is consistent with the printed order and is not established by it"*, and that the schematic was **measured** (nine levels, gaps `52.5–54 px`, mean 52.9 ±1.1) and **cannot discriminate**. **A variable name cannot do what a measured diagram could not** |
| **Wrong lineage and vintage** | 2010 third-party retail product, 2018 file date, 2012 course. No `mm_` / `MM4XSF_` / `!SM_` prefix — not the family that grounded `D-045` |

```text
A-101 -- OPEN and DO NOT CODE. UNCHANGED BY THIS DRAFT.
```

⭐ **The one thing that would change this: `PivotPoints.mq4` — the SOURCE.** With it,
`Plot_middle`'s formula is readable in one line and `A-101`'s construction row becomes decidable at
`TOOLING` tier — exactly as `mm_adr.mq4`'s source did for `A-100`'s range row in `D-051`. **§7 Q4.**

---

## 6. ⚠️ `!SM_TDI`, `Daily Range PeterE` — TWO REFUSALS TO STRENGTHEN A RECORD

**`MMM.tpl`'s TDI block is identical to `Ultimate Blue.tpl`'s in every field but `Draw_MBL_Slope`**
(1 → 0, cosmetic): `RSI_Period=21`, `Volatility_Band=34`, **`RSI_Price_Line=2`**,
`Trade_Signal_Line=7`, `63`/`37`.

⛔ **AND THIS DOES NOT REPAIR `D-045`'s KNOWN WEAKNESS.** `SOURCING_HIERARCHY.md` §3.4 records that
`A-084`'s **load-bearing** field `RSI_Price_Line=2` is *not among the fields V13 `00:53:35`
corroborates.* `MMM.tpl` shows the same value — **but two templates saved by one user from one
indicator installation are not two witnesses.** A second save of the same habit cannot corroborate
the first; it is `SOURCING_HIERARCHY.md` §1.3's *"one document quoted twice"* trap in a new place.
**`A-084` stays `PROVISIONALLY RESOLVED — TOOLING` at exactly the strength `D-045` gave it**, and
stays on the §3.4 re-check list.

**Same refusal for the ADR.** `MMM.tpl` carries `Daily Range PeterE`, **`NumOfDays=10`** — the same
tool at the same value `D-051` §5 logged from `Ultimate Blue.tpl`, and now in the template *named
for this method*. ⛔ **`A-100`'s lookback row does not close.** The four-way conflict
**10 / 14 / 15 / 21** stands, and **V16 `[00:09:31]`'s *"the last two weeks, 15 days"* is TIER 1,
from the course author's own mouth**, outranking any number of `TOOLING` sightings.

**On `D-052`/`D-053`:** the parallel TDI session **has landed** (merged `34ac3f7`); `MMM_TDI.txt` is
the **PRIMARY TDI INSTRUMENT**. **Nothing here duplicates, contradicts or reopens it.**
`Volatility_Band=34` is a `TOOLING` number and `D-052` already declined to promote one —
**`A-086` stays `DO NOT CODE`.**

⭐ **One null `D-051` correction, recorded for completeness:** a **second copy** of the `mm_adr`
source exists at `Desktop/Trading/Indicators/MM_ADR.mq4` (md5 `c155757f2391b94bcd234b58ae1a340a` ≠
Forex222's `807876a6…`). `diff` shows **one moved declaration line and no functional change.**
`D-051` §2 is unaffected.

---

## 7. THE PROPOSED LEDGER ENTRY — TEXT FOR THE OWNER TO APPROVE, EDIT OR REJECT

> ## D-055 — `MMM.tpl` is admitted to the `TOOLING` rung; the session ribbon's boundaries are RECORDED but CLOSE NOTHING; a Pine replication is admitted as a DRAFT TOOL; and the pivot search returns NOT FOUND ON THE MMM CHART
>
> **Date:** 2026-08-14
> **Extends:** `D-045` Part 1 (the `TOOLING` rung), whose per-artifact rule requires a separate
> entry per artifact. `D-045` is not superseded and its three travelling rules apply unchanged.
>
> **Part 1 — the artifacts.** `MMM.tpl` (md5 `db617bcdfeb5df26c033036f96c41472`),
> `MMM INDICES.tpl` (`e6f977f56e5c87048795a8b344759a61`) and `!sm_WorkTime_v1.5b.ex4`
> (`b938ee1df8cf16a44bc16db71795e9f2`), supplied and attested by the owner as his working
> configuration for this method, are admitted to the **`TOOLING — OWNER-ATTESTED PLATFORM
> ARTIFACT`** rung. ⭐ **`MMM.tpl` is a CONFIGURATION, not a parameter — the first artifact stating
> which tools run TOGETHER.** Admission is **per-artifact** and covers these three and nothing else;
> `RS5P.tpl` is **expressly NOT admitted** (it is a different method's chart). Citations carry
> **`[TOOLING] MMM.tpl`**.
>
> **Part 2 — the ribbon's boundaries are RECORDED and CLOSE NOTHING.** Asian `0:00–8:00`; Euro
> `8:30–14:00` (**configured, switched OFF**); New York `16:30–20:00`; "market open" `10:00–11:00`
> and `16:00–17:00`; `NumberOfDays=50`; all alerts off. ⛔ **`A-019`, `A-105` and `A-131` remain
> `OPEN` and `DO NOT CODE`.** These are **clock values in an unidentified server timezone**, and the
> tool that would normalise them is a packed binary with no source on the volume — the identical
> limitation `D-051` §4 hit on the ADR day boundary.
>
> **Part 3 — ⭐ the `A-105` finding, recorded and NOT adjudicated.** One offset hypothesis
> (server = UTC+2/+3, the standard MT4 broker clock) places **five** saved boundaries on real market
> events at once, and under it — with `EST` read **literally** on a summer clock — V16's printed
> *"London Session Start 2:00 To 3:00 AM, EST"* coincides **exactly** with the ribbon's own
> `10:00–11:00` London market-open box. ⛔ **NOT ADOPTED.** The offset is **inferred from the
> boundaries it then explains**, which is circular absent independent attestation.
> `SOURCING_HIERARCHY.md` §3.2 **Case C** and `D-048` **rung 4** govern: **put to the owner.**
> ⭐ **The one input that settles it is the GMT offset of the owner's MT4 server** — the `D-052`
> shape, and the owner is asked for it directly.
>
> **Part 4 — the Pine replication is admitted as a DRAFT TOOL ONLY.**
> `06_MANUAL_BACKTEST/tools/MMM_SESSION_RIBBON.txt` ports the ribbon with **every default
> transcribed from `MMM.tpl`**, the **clock exposed as an input rather than baked in**, and both
> unreadable behaviours marked `[GUESS]` at the code that implements them. ⚠️ **It has NOT been run
> on TradingView and has NOT been compared against the owner's chart**, which is stated in the file.
> ⛔ **No `PT`/`BT` may cite it, and it establishes no session boundary.** Its **acceptance test is
> pre-registered** at `D-055` §4.4, including the **DST-transition run**, which is the only known
> procedure that can settle whether v1.5b auto-normalises the clock.
>
> **Part 5 — ⛔ the pivot search: NOT FOUND ON THE MMM CHART.** No pivot indicator exists in
> `MMM.tpl`, `MMM INDICES.tpl` or `RS5P.tpl`. A candidate exists elsewhere — `PivotPoints.ex4`
> (md5 `703ec775dcdff4c6995a722209ce0f2f`), carrying `Plot_middle`/`Color_Mid` — and is **NOT
> admitted**: it is unattested, absent from every MMM template, and **compiled with no source**, so
> its formula is unreadable and its variable names are not evidence (`D-030`). ⛔ **`A-101` remains
> `OPEN` and `DO NOT CODE`.** `PZ_QuartersTheory`, which *is* on the chart, is a **round-number
> grid and is not a pivot tool**; reading it as one would be the `A-082` error.
>
> **Part 6 — three records this artifact does NOT strengthen, stated so it cannot be misread.**
> ⛔ **`A-084` is unchanged.** `MMM.tpl`'s `RSI_Price_Line=2` is a **second save of one habit by one
> user from one installation** — not a second witness. The §3.4 weakness stands at full strength.
> ⛔ **`A-100`'s lookback is unchanged** — a second `NumOfDays=10` does not outrank V16
> `[00:09:31]`'s Tier 1 *"15 days"*; **10 / 14 / 15 / 21** stands. ⛔ **`A-020` / `D-043` are
> unchanged** — the template's **4 and 10** (vs `D-043`'s **5 and 13**) and its unattested **3200**
> are **owner PRACTICE (2023)**, not testimony about the **teaching (2012)**; the `D-052` §3.5
> distinction is applied, and the divergence is put to the owner as a question.
> ⛔ **`A-005`, `A-086`, `D-052`, `D-053` untouched.**
>
> **Reason:** the session clock (`A-019`/`A-105`/`A-131`) blocks `D-031`, `A-005` and every timing
> rule in the corpus, and 19 lessons produced **one** ambiguous timezone. The owner's offer of his
> actual chart is the `D-045` move again, and it works again — partly. It also produced something
> better than itself: the ribbon and the V16 slide are **arithmetically comparable**, and nobody had
> compared them.
>
> **Evidence:** `MMM.tpl`, `MMM INDICES.tpl`, `RS5P.tpl`, `!sm_WorkTime_v1.5b.ex4`,
> `sm_WorkTime_no_autogmt.ex4` (md5s above); `PivotPoints.ex4`; `Sessions.mq4` (mechanism only, an
> unattested third-party tool); `INDICATOR_FOLDER_INVENTORY_2026-08-14.md`; `A-019`, `A-100`,
> `A-101`, `A-105`, `A-131`, `A-084`, `A-086`, `A-020`, `A-005`, `A-082`; `C-010`; `D-030`, `D-041`,
> `D-043`, `D-045`, `D-048`, `D-051`, `D-052`, `D-053`; `SOURCING_HIERARCHY.md` §1, §3.2, §3.4, §3.5.
> Owner attestation, 2026-08-14.
>
> **Alternatives considered:** *Closing `A-105` on the §4.5 coincidence* — **rejected, and this is
> the discipline of the entry.** The offset is inferred from the very boundaries it explains; `D-048`
> rung 4 exists for exactly this. *Baking UTC+2 into the Pine port* — rejected; it would harden an
> inference into a tool, which is how a provisional entry becomes doctrine (§3.4). *Admitting
> `PivotPoints.ex4` to close `A-101`* — rejected; unattested, off-chart, and its formula is
> unreadable. *Treating the template's 4/10 as evidence against `D-043`* — rejected per Part 6.
> *Treating `MMM.tpl`'s TDI block as corroborating `A-084`* — rejected per Part 6. *Declining
> `MMM.tpl` entirely because it is dated 2023* — rejected; it is the most informative artifact the
> project holds and the vintage is disclosed rather than hidden.
>
> **Consequences:**
>
> 1. `SOURCING_HIERARCHY.md` §1's `TOOLING` rung gains `MMM.tpl`, `MMM INDICES.tpl` and
>    `!sm_WorkTime_v1.5b.ex4`, with md5s and a pointer here. The rung's rules are unchanged.
> 2. ⛔ **No `A-xxx` changes status.** Per `D-045` rule 2, **admission is not reading** — this entry
>    makes the ribbon *eligible*, and a session that reads it against `A-019`/`A-105`/`A-131`
>    closes them, **or does not.**
> 3. The **acceptance test** (§4.4), including the **DST-transition run**, is **pre-registered by
>    this entry**. A session with a screenshot of the owner's live chart runs it as specified and
>    reports the result **whether or not it helps**.
> 4. ⚠️ **The §3.4 re-check obligation attaches to everything cited from this rung**, and the
>    trigger is named so a session knows what to watch for: **any lesson showing a session box, an
>    indicator PROPERTIES DIALOG for a time tool, a stated GMT offset, or a broker/server clock.**
> 5. `MMM_SESSION_RIBBON.txt` stays a **draft tool**, citable by nothing, until the §4.4 test runs.
> 6. ⭐ **`PivotPoints.mq4` (the SOURCE) is recorded as the single highest-value artifact the owner
>    could supply for `A-101`**, exactly as `D-051` §7 recorded the course's own ADR build for
>    `A-100`.
>
> **Status:** ACTIVE — admission only; **every `A-xxx` remains OPEN**; the Pine port is a **DRAFT**

---

## 8. THE QUESTIONS FOR THE OWNER

1. ⚠️ **Which folder did you add files to?** You said *"Forex222"*, but
   `Documents/Forex indicator/Forex222/` is **byte-for-byte unchanged**. The MMM material is in
   `Desktop/Trading/Indicators/`. **If you believe you added something to Forex222, it did not
   land** — worth checking before anything else here is trusted as complete.
2. ⭐⭐ **What GMT offset did your MT4 server run on?** *(Or: which broker?)* **This is the single
   highest-value sentence you could supply.** §4.5 shows it is the one fact standing between the
   ribbon's boundaries and a real answer to `A-105`'s one-hour question — the record that gates
   `D-031`, `A-005` and every timing rule in the corpus. ⭐ **Second best if you don't recall: a
   screenshot of the live chart with the ribbon and the platform clock visible.**
3. ⚠️ **Why does your MMM chart run EMA 4 and 10, where the course taught 5 and 13** (`D-043`, your
   own attestation)? **And what is the 3200?** — it appears nowhere in the corpus at any tier. §3
   treats this as *your current practice*, not as evidence against `D-043`; confirm or correct that
   reading.
4. ⭐ **Do you have `PivotPoints.mq4` — the SOURCE?** The compiled `.ex4` has a `Plot_middle` input
   that is very likely `A-101`'s `M1`–`M4`, but **a variable name is not a formula**. The source
   would make `A-101`'s construction decidable in one line.
5. **Do you attest `MMM.tpl` as your working configuration for this method**, in the sense you
   attested `!SM_TDI` for `D-045`? Part 1 depends on it and nothing else does.
6. **Is the Euro band deliberately off?** `draw_euro_box=false` is saved in both MMM templates — a
   configured band you have chosen not to display. That may be a real fact about how you read the
   chart, or it may be an accident.
