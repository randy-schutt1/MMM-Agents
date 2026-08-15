# INDICATOR FOLDER INVENTORY — COMPLETE SURVEY, 2026-08-14

> **Branch:** `tools/indicator-folder-survey-and-owner-risk-rule` · **Status:** `SURVEY — NO RECORD CLOSED BY THIS FILE`
>
> ## ⛔ THIS FILE ADMITS NOTHING AND CLOSES NOTHING.
>
> It is an **inventory**, written because the owner added material to the indicator folders and
> said *"the pivot points may be in there"* and *"the time ribbon — we can replicate exactly."*
> Under `D-045` rule 1, **admission to the `TOOLING` rung is per-artifact and requires its own
> decision entry.** Nothing listed below is admitted by being listed. The proposals that would
> admit anything are `DECISION_DRAFT_D-056_MMM_TPL_AND_TIME_RIBBON.md`, and they are **drafts.**
>
> **`SOURCING_HIERARCHY.md` §1's `TOOLING` rung still admits exactly two things** —
> `Ultimate Blue.tpl` / `!SM_TDI` (`D-045`) — plus `mm_adr` **only if `D-051` is adopted**, which
> it has not been.

---

## 0. THE HEADLINE, INCLUDING THE PART THAT DOES NOT GO THE OWNER'S WAY

Three results, in descending order of value:

1. ⭐⭐ **`MMM.tpl` EXISTS.** `Desktop/Trading/Indicators/MMM.tpl` is a saved MetaTrader 4 chart
   template **named for this method**, carrying **fourteen indicators with every input value
   persisted**. It is by a wide margin the most informative artifact yet found on this volume: it
   is the owner's *whole chart*, not one tool off it. **It names the moving-average set, the TDI
   configuration, the ADR tool, and the session ribbon, all in one file.**
2. ⭐⭐ **THE TIME RIBBON IS FOUND AND ITS SESSION BOUNDARIES ARE FULLY RECOVERED** —
   `!sm_WorkTime_v1.5b`, with **six saved clock boundaries**. See §4.
   ⚠️ **But "replicate exactly" is not quite available and this file says so before it says
   anything else:** the binary is packed and unreadable, and one behaviour — the **automatic GMT
   adjustment** its own sibling filename advertises the *absence* of — **cannot be read from any
   artifact found.** The box *geometry* is exactly recoverable; the *clock the boxes are anchored
   to* is not. See §4.4.
3. ⚠️ **A PIVOT INDICATOR WAS FOUND, AND IT IS NOT ON THE OWNER'S MMM CHART.**
   `PivotPoints.ex4` exists (`Desktop/All Folders/Downloads/`) and it does carry a `Plot_middle` /
   `Color_Mid` input pair — **exactly the object `A-101` is missing.** But it is **absent from
   `MMM.tpl`, from `MMM INDICES.tpl` and from `RS5P.tpl`**, it is compiled with no source, and
   nothing attests it. See §5 — the answer to *"the pivot points may be in there"* is
   **"a pivot indicator is in there, but not in the MMM template, and it cannot be read."**

---

## 1. WHAT WAS SEARCHED

| Location | Result |
|---|---|
| `Documents/Forex indicator/Forex222/` | 29 artifacts — the `D-051` folder, **unchanged** since that draft |
| `Documents/Forex indicator/DOWNLOAD ALL TEMPLATES/` | 6 `CueFX*.tpl` templates, none MMM-related |
| ⭐ `Desktop/Trading/Indicators/` | **40 artifacts — this is the folder that changed.** Directory mtime `2026-08-14 21:58` |
| ⭐ `Desktop/All Folders/Downloads/` | 10 loose MT4 artifacts incl. **`PivotPoints.ex4`**, `Sessions.mq4`, `MM4XSF_TDI.ex4` |
| `Desktop/All Folders/Downloads/11. Indicators & Templates/DOWNLOAD ALL INDICATORS/` | 22 files — **MT4 stock indicators only** (ATR, RSI, MACD…) plus `Traders_Dynamic_Index.mq4` (the *generic* TDI, not the MMM build) |
| `Desktop/All Folders/Most Viewed/…/Forex/`, `Desktop/Trading/Forex Robot/` | EA/bot material, unrelated |
| Volume-wide sweep for `*pivot*`, `*ribbon*`, `*session*`, `*.mq4/.ex4/.tpl` | Complete; everything found is listed here |

⚠️ **Note on the folder the owner named.** The owner said *"Forex222"*. `Forex222/` is **byte-for-byte
unchanged** from the `D-051` survey. **The new material is in `Desktop/Trading/Indicators/`** — a
different folder, and the one holding `MMM.tpl`. This inventory covers both and does not assume
which one was meant. **Worth confirming with the owner**, because `Forex222/` being static means
*nothing was added there today.*

---

## 2. ⭐⭐ `MMM.tpl` — THE OWNER'S MMM CHART, INDICATOR BY INDICATOR

`Desktop/Trading/Indicators/MMM.tpl` · md5 `db617bcdfeb5df26c033036f96c41472` · 121,164 bytes
Saved on **`USDNOK`, H1** (`period=60`), 2023-08-15.

| # | Indicator | Saved inputs | Bears on |
|---|---|---|---|
| 1–6 | **Moving Average** ×6 | `method=1` (**EMA**), `apply=0` (**close**), `shift=0`; periods **4 · 10 · 50 · 200 · 800 · 3200** | ⭐ `A-020`, `C-010`, `D-043` — see §3 |
| 7 | `!SM_Daily_HiLo` | `offset=2`, `BreakoutPrice=0` | previous-day high/low levels |
| 8 | ⭐ **`!sm_WorkTime_v1.5b`** | **the session ribbon — 30 inputs, see §4** | ⭐ `A-105`, `A-019`, `A-131` |
| 9 | `Weekly_High_Low Great` | `TimeZoneOfData=0` | weekly extremes |
| 10 | `Candle Timer` | `DisplayTimeByTheBar=1`, `AutoTimeShiftAdjust=1` | bar countdown, cosmetic |
| 11 | ⭐ **`Daily Range PeterE`** | **`NumOfDays=10`** | ⭐ `A-100` lookback — see §6 |
| 12 | `ICT Day Of Week` | day-coloured vertical separators | day boundaries, cosmetic |
| 13 | `PZ_QuartersTheory (3)` | `RoundNumberColor`, `QuarterPointsColor`, `HalfPointsColor`, `HesitationPointColor` | round-number levels — ⚠️ **not** pivots, see §5.3 |
| 14 | ⭐ **`!SM_TDI`** | `RSI_Period=21` · `Volatility_Band=34` · `RSI_Price_Line=2` · `Trade_Signal_Line=7` · `63`/`37` | ⭐ `A-084`, `A-086`, `D-045`, `D-052`, `D-053` — see §7 |

⛔ **THERE IS NO PIVOT INDICATOR IN THIS TEMPLATE.** Fourteen slots, none of them pivots. The same
is true of `MMM INDICES.tpl` and `RS5P.tpl`. **This is a negative result and it is worth as much as
a positive one** — the owner's own MMM chart does not carry the tool that would draw `M1`–`M4`.

### 2.1 The two sibling templates

| Template | md5 | Symbol | Differences from `MMM.tpl` |
|---|---|---|---|
| `MMM INDICES.tpl` | `e6f977f56e5c87048795a8b344759a61` | `UK100` H1 | ⭐ **Same six EMAs, same ribbon, same TDI, same `NumOfDays=10`.** Drops `Candle Timer`; carries `PZ_QuartersTheory` **twice** |
| `RS5P.tpl` | `2709e6f6b972e6fc4d176165294d01d4` | `USDJPY` H1 | Same six EMAs + ribbon; ⚠️ **no `!SM_TDI`** — instead Ichimoku, `RSI(5)`, `MFI(5)`, `RSI(99)`, two MACDs. **A different method's chart**, sharing this one's skeleton |

⭐ **The six-EMA set and `!sm_WorkTime_v1.5b` appear in ALL THREE templates, unchanged.** That is
the strongest internal consistency signal in the whole artifact set.

---

## 3. ⭐ THE MOVING-AVERAGE SET — AND WHAT IT DOES *NOT* DO TO `A-020`

`MMM.tpl` states, in a saved parameter block: **EMA on close, periods 4 · 10 · 50 · 200 · 800 · 3200.**

| | |
|---|---|
| ✅ **Agrees with the corpus on** | the presence of **800** — `C-010`'s finding, against the Mauro PDF's *"5 / 13 / 50 / 200, no 800"* (p.38). A **third** independent support for the 800 |
| ⚠️ **DISAGREES with `D-043` on the two short ones** | `D-043` is **mustard = 5 · ketchup = 13**. The template says **4 and 10.** *Not 5 and 13.* |
| ⚠️ **Adds one the corpus never mentions** | **3200**. It appears in no lesson, no slide, and no note at any tier |
| ✅ **Confirms the type** | `method=1` = **EMA**, not SMA — the corpus has never stated this outright |

⛔ **THIS DOES NOT REOPEN `D-043` AND THIS FILE DOES NOT TREAT IT AS EVIDENCE AGAINST IT.**
`D-043` rests on **owner attestation about what was TAUGHT**, which sits *outside* the tiers
(`D-041`). A 2023 chart file is the owner's **current practice**, which is the `D-052`
`OWNER EMPIRICAL PREFERENCE` category — *"what the instrument does"*, not *"what was taught"*.
**They are different questions and a 4/10 chart in 2023 is not testimony that the course taught
4/10 in 2012.** The `D-052` entry draws exactly this distinction; it is applied here.

⭐ **But it is a real divergence and it is owed to the owner as a question**, not buried:
**why does your own MMM chart run 4 and 10 where the course taught 5 and 13?** See
`DECISION_DRAFT_D-056` §8 Q3. Until answered, **`A-020` is untouched**, `D-043` stands, and
**nothing here is coded.**

---

## 4. ⭐⭐ THE TIME RIBBON — `!sm_WorkTime_v1.5b`

**Artifact:** `Desktop/Trading/Indicators/!sm_WorkTime_v1.5b.ex4` · md5 `b938ee1df8cf16a44bc16db71795e9f2` · 62,866 bytes · dated 2015-02-17
**Sibling:** `sm_WorkTime_no_autogmt.ex4` / `… (1).ex4` · md5 `8f0059bd2abf728b53198bb59f5ecaa2` · 37,956 bytes · **present in BOTH folders**
**Version string, from `MMM.tpl`:** `!sm_WorkTime v1.5b AML`

### 4.1 ⭐ THE SAVED SESSION BOUNDARIES — read directly off `MMM.tpl`

| Band | Input pair | **Saved value** | Drawn? | Colour |
|---|---|---|---|---|
| **Asian** | `Begin_1` / `End_1` | **`0:00` → `8:00`** | ✅ box + text + **midline** | `15128749` |
| **Euro** | `Begin_2` / `End_2` | **`8:30` → `14:00`** | ⛔ **`draw_euro_box=false`** — configured but **switched off** | `6908265` |
| **New York** | `Begin_3` / `End_3` | **`16:30` → `20:00`** | ✅ box + text | `8419743` |
| *(Asian-range update)* | `Begin_4` / `End_4` | ⚠️ **ABSENT from the template entirely** — see §4.3 | — | — |
| ⭐ **"Market open" A** | `Begin_5a` / `End_5a` | **`10:00` → `11:00`** | ✅ | `14599344` |
| ⭐ **"Market open" B** | `Begin_5b` / `End_5b` | **`16:00` → `17:00`** | ✅ | `14599344` |

Plus: `NumberOfDays=50` · `draw_asian_midline=true`, `asian_midline_color=65535` (yellow),
**`asian_midline_hours=9`** · every alert **off** (`Alert25BlueBox`, `Alert50BlueBox`,
`Alert50EMA`/`Alert50Pips=20`, `Alert200EMA`/`20`, `Alert800EMA`/`30`, `SoundOn=false`) ·
**`DrawStopHuntBox=false`**.

⭐ **Two of those input names are independently interesting even switched off:**
`Alert25BlueBox` / `Alert50BlueBox`, whose strings in the readable sibling build are literally
**`25 Pips above blue box` / `50 Pips above blue box` / `25 Pips below…` / `50 Pips below…`**.
**That is `A-005`'s *"the trading zone is set 25 to 50 pips higher (or lower) than the Asian
range"* implemented as a shipped alert** — the "blue box" being the Asian box. ⚠️ **It corroborates
the 25/50 band; it does not close `A-005`**, which is blocked on `A-019`/`D-031`, i.e. on the
clock — the very thing §4.4 says is unreadable.

### 4.2 The complete input surface, recovered from the readable sibling

`!sm_WorkTime_v1.5b.ex4` is **MT4 build-600+ packed — `strings` returns nothing but noise.**
The older `sm_WorkTime_no_autogmt.ex4` is a **pre-600 build with readable input names**, and it
yields the full ordered surface: `NumberOfDays` · `draw_asian_*` · `Begin_1`/`End_1`/`Color_1`/
`Color_1_Text` · `draw_euro_*` · `Begin_2…` · `draw_ny_*` · `Begin_3…` · **`draw_upd_asian_range_box`
/ `draw_upd_asian_range_text` / `Begin_4`/`End_4`/`Color_4`** · `draw_mktopen_*` ·
`Begin_5a`/`End_5a`/`Begin_5b`/`End_5b`/`Color_5` · `Alert25BlueBox` · `Alert50BlueBox` ·
`DrawStopHuntBox` · `StopHuntBoxColor` · `Alert50EMA`/`Pips` · `Alert200EMA`/`Pips` ·
`Alert800EMA`/`Pips` · `SoundOn` · `SoundFile` · `HighRange`.
Object prefixes: **`WT_1`…`WT_5`, `WT_T1`…`WT_T5`, `WT_SH`** (stop-hunt), `ilWT_`.

⭐ **So band 5 is named `mktopen` by the author** — *market open* — and it is **the only band with
two disjoint windows.** That is the ribbon's own answer to what `10:00–11:00` and `16:00–17:00`
are for: **they mark two market opens**, not sessions.

### 4.3 ⚠️ Band 4 is missing, and that is a fact about the build, not a reading error

`Begin_4`/`End_4` (`draw_upd_asian_range_*`) exist in the older build and **do not appear in
`MMM.tpl` at all** — grep returns `0`. MT4 writes every extern of the attached build into the
template, so **v1.5b appears to have dropped band 4.** ⚠️ **Unverified** — it is an inference from
an absence, and the alternative (MT4 omitting an input) is not excluded.

### 4.4 ⛔⛔ THE ONE THING THAT CANNOT BE REPLICATED, AND IT IS THE ONE THAT MATTERS

The owner's words were *"we can replicate exactly."* **The geometry, yes. The clock, no.**

> **The sibling is named `no_autogmt`. A build advertising the ABSENCE of automatic GMT handling
> is evidence that the build the owner actually runs — `v1.5b` — HAS it.**

And the consequence is precise:

- **If v1.5b applies no offset**, `Begin_1=0:00` means midnight **on the broker's server clock**,
  and the broker is unidentified — the identical limitation `D-051` §4 hit on the ADR day boundary.
- **If v1.5b auto-adjusts to a detected GMT offset**, the saved values are in a **normalised**
  clock, and the rule that normalises them is **inside a packed binary with no source anywhere on
  this volume** (searched: `find ~ -iname "*WorkTime*"` → the two `.ex4` and nothing else).

**Neither branch can be decided from any artifact found.** A faithful port must therefore expose
the offset as a **declared, owner-supplied input** and must not bake a guess into it. That is what
the replication plan does — `DECISION_DRAFT_D-056` §4.

### 4.5 ⭐ WHAT THE BOUNDARIES IMPLY ABOUT THE CLOCK — AN INFERENCE, LABELLED AS ONE

**One offset hypothesis makes all four drawn boundaries land on real market events at once:**
**server = UTC+2 (winter) / UTC+3 (summer)** — the standard MT4 broker clock.

| Ribbon boundary | Under UTC+2 | Real event |
|---|---|---|
| `Begin_3 = 16:30` (NY box) | 14:30 UTC = **09:30 ET** | ⭐ **NYSE cash open** |
| `Begin_5a = 10:00` (mktopen A) | 08:00 UTC = **08:00 London** | ⭐ **London open** |
| `Begin_5b = 16:00` (mktopen B) | 14:00 UTC = **09:00 ET** | US pre-cash / NY FX open |
| `Begin_2 = 8:30` (Euro) | 06:30 UTC = **07:30 CET** | Frankfurt open |
| `Begin_1`–`End_1 = 0:00–8:00` | 22:00–06:00 UTC | **07:00–15:00 JST** — Tokyo |

⚠️⚠️ **THIS IS THIS SESSION'S ARITHMETIC, NOT A SOURCE.** Five boundaries fitting one offset is a
strong coincidence and it is **not** an attestation. It is written down so the owner can confirm or
kill it in one sentence, and it is **not** used to close anything. **`A-019`, `A-105` and `A-131`
are OPEN and unchanged by this file.**

### 4.6 ⭐⭐ AND HERE IS WHY IT MATTERS — THE `A-105` COLLISION

`A-105` is the corpus's only printed, timezone-stamped session boundary:
**`London Session Start · 2:00 To 3:00 AM, EST`** (V16, slide dated **2012-05-06** — inside US DST).
Its open question is exactly **one hour**: is `EST` literal (UTC−5) or NY-local (EDT, UTC−4)?

**Cross the slide against the ribbon's London-open box (`10:00–11:00` server):**

| Slide reading | → UTC | Server **UTC+2** | Server **UTC+3** |
|---|---|---|---|
| **`EST` literal (UTC−5)** | 07:00–08:00 | 09:00–10:00 — *abuts* the box | ⭐⭐ **10:00–11:00 — EXACTLY THE BOX** |
| `EST` = NY-local (EDT, UTC−4) | 06:00–07:00 | 08:00–09:00 — 2 h early | 09:00–10:00 — *abuts* |

⭐ **The slide is dated inside US daylight time, when a UTC+2/+3 broker sits on UTC+3. That cell —
literal `EST` on a summer clock — is the ONE combination of the four that makes the V16 slide
coincide EXACTLY with the ribbon's own London market-open box.**

⛔⛔ **AND IT IS NOT ADOPTED.** It is an inference resting on §4.5's inferred offset, which is
itself unattested. Under `SOURCING_HIERARCHY.md` §3.2 **Case C** and `D-048`'s **rung 4** this is
put to the owner, not decided here. **What it is:** the first mechanism the project has ever found
that could settle `A-105`'s one-hour question on arithmetic instead of on choosing. **What settles
it is one fact only — the broker/server GMT offset the owner's MT4 ran on** — which is the same
shape as `D-052`'s *"the period is the one input that could settle this."*

---

## 5. ⚠️ THE PIVOT QUESTION — ANSWERED, AND THE ANSWER IS "NOT ON THE MMM CHART"

### 5.1 What was found

**`PivotPoints.ex4`** · `Desktop/All Folders/Downloads/` · md5 `703ec775dcdff4c6995a722209ce0f2f` · 11,304 bytes · dated 2018-07-13
Readable copyright strings: **`Copyright © 2010, Forex Profit Launcher` / `www.forexprofitlauncher.com`**

Recovered input surface:

```text
CountDays
Plot_pivots      Plot_middle      Plot_camarilla
Color_PP   Color_Res   Color_Sup   Color_Mid
Color_H4 Color_H3 Color_H2 Color_H1   Color_L1 Color_L2 Color_L3 Color_L4
==== Main Settings ====        ==== Pivot Point Colors ====
```

⭐ **`Plot_middle` + `Color_Mid`, as a switch and colour SEPARATE from `Color_PP`/`Color_Res`/
`Color_Sup`, is exactly the class of object `A-101` is missing** — the interstitial levels between
`CPP`, `R1`/`R2` and `S1`/`S2`. `Color_H1`–`H4`/`L1`–`L4` are the **Camarilla** set, which
`Plot_camarilla` gates separately, so the `Mid` family is **not** Camarilla.

### 5.2 ⛔ Why it does NOT answer `A-101`

| | |
|---|---|
| **It is not on the owner's chart** | Absent from `MMM.tpl`, `MMM INDICES.tpl` and `RS5P.tpl`. The `TOOLING` rung is *"the owner's working configuration for this method"* (`D-045`) — **this artifact has no such attestation and the templates argue against one** |
| **It is compiled and unreadable** | Packed `.ex4`, no `.mq4` anywhere on the volume. **The input NAMES are recoverable; the FORMULA is not.** That `Plot_middle` draws midpoints is a reading of a variable name, which is `D-030`'s exact prohibition |
| **`A-101` asks for a construction** | `A-101` already records that `M3 = midpoint(CPP,R1)` etc. is *"consistent with the printed order and not established by it"*, and that the schematic was **measured** and found equally spaced — i.e. the diagram cannot discriminate. **A name cannot do what a measured diagram could not** |
| **Wrong vintage and lineage** | 2010 third-party retail product, **2018** file date, against a 2012 course. No `mm_`/`MM4XSF_`/`!SM_` prefix — it is not in the family that grounded `D-045` |

```text
A-101 -- OPEN and DO NOT CODE. UNCHANGED BY THIS SURVEY.
  A candidate artifact exists and is named in DECISION_DRAFT_D-056 §5.
  It would need (a) owner attestation and (b) READABLE SOURCE to bear on the
  construction. It currently has neither.
```

⭐ **The single highest-value item the owner could supply for `A-101` is `PivotPoints.mq4` — the
SOURCE.** With it, `Plot_middle`'s formula is readable in one line and `A-101`'s construction row
becomes decidable at `TOOLING` tier, exactly as `mm_adr.mq4`'s source did for `A-100`'s range row.
Without it, a compiled binary and a suggestive variable name are **not** evidence.

### 5.3 ⚠️ And `PZ_QuartersTheory` is NOT the pivot indicator

`PZ_QuartersTheory (3)` **is** on the MMM chart, and its `RoundNumberColor` /
`QuarterPointsColor` / `HalfPointsColor` / `HesitationPointColor` inputs make it superficially
look like a levels grid. **It is not a pivot tool.** Quarters Theory divides the *price scale* into
fixed round-number fractions; floor-trader pivots derive from the **previous period's H/L/C**.
`A-101`'s grid is explicitly `R2 · M4 · R1 · M3 · CPP · M2 · S1 · M1 · S2` — a **pivot** grid with
a `CPP`. **Reading the owner's quarters tool as the course's pivot tool would be the `A-082` error**
and is not done here.

---

## 6. `Daily Range PeterE` — `A-100`'s LOOKBACK, AND A SECOND SIGHTING OF `10`

`MMM.tpl` carries **`Daily Range PeterE`, `NumOfDays=10`** — the *same indicator at the same value*
`D-051` §5 already logged from `Ultimate Blue.tpl`.

⭐ **This is a second, independently-saved owner template showing `10`** — and `MMM.tpl` is the one
*named for this method*, which `Ultimate Blue.tpl` is not.

⛔ **It does not close `A-100`'s lookback row and this file does not offer it as doing so.**
`D-051` §5's four-way conflict — **10 / 14 / 15 / 21** — stands, and **V16 `[00:09:31]`'s
*"the last two weeks, 15 days"* is TIER 1, from the course author's own mouth**, which outranks any
number of `TOOLING`-tier sightings. Two templates agreeing is **one habit recorded twice**, not
independent corroboration — the `SOURCING_HIERARCHY.md` §1.3 trap, in a new place.
**`A-100` stays `OPEN`. `D-051` stays `NOT ADOPTED`.**

⭐ **One genuine `D-051` correction, and it is null:** a **second copy** of the `mm_adr` source
exists as `Desktop/Trading/Indicators/MM_ADR.mq4` (md5 `c155757f2391b94bcd234b58ae1a340a`, different
from Forex222's `807876a6…`). **`diff` shows one moved declaration line and no functional change.**
`D-051` §2's construction is unaffected; the extra copy is recorded for completeness.

---

## 7. `!SM_TDI` — CONSISTENT WITH `D-052`/`D-053`, AND ONE HONEST NON-RESULT

`MMM.tpl`'s TDI block is **identical to `Ultimate Blue.tpl`'s in every field but one**:

```text
RSI_Period=21   Volatility_Band=34   RSI_Price_Line=2   RSI_Price_Type=0
Trade_Signal_Line=7   Trade_Signal_Type=0
SharkFin_Upper_Level=63.0   SharkFin_Lower_Level=37.0
VB_High_Value=45.0   VB_Low_Value=55.0   Sensitivity=0.0001
```

Sole difference: **`Draw_MBL_Slope`** — `1` in `Ultimate Blue.tpl`, `0` in `MMM.tpl`. Cosmetic.

⚠️ **AND THIS DOES *NOT* REPAIR `D-045`'s KNOWN WEAKNESS.** `SOURCING_HIERARCHY.md` §3.4 records
that `A-084`'s load-bearing field `RSI_Price_Line=2` **is not among the fields V13 `00:53:35`
corroborates**. `MMM.tpl` shows the same value — but **two templates saved by one user from one
indicator installation are not two witnesses.** A second save of the same habit cannot corroborate
the first. **`A-084` stays `PROVISIONALLY RESOLVED — TOOLING` at exactly the strength `D-045` gave
it**, and it stays on the §3.4 re-check list. ⭐ *The `RSI_Period=21` does agree with V13's
corroborated `21`* — which was already true and adds nothing.

**On `D-053`:** the parallel TDI session **has landed** — `D-053` is merged at `34ac3f7`, `MMM_TDI.txt`
is the **PRIMARY TDI INSTRUMENT**, and `06_MANUAL_BACKTEST/tools/MMM_TDI.txt` carries it. **Nothing
in this survey duplicates, contradicts or reopens it.** `A-086`'s band **period** is still stated
nowhere at any tier — `Volatility_Band=34` is a *TOOLING* number, which is what `D-052` already
declined to promote. **`A-086` stays `DO NOT CODE`.**

---

## 8. THE FULL INVENTORY

### 8.1 `Desktop/Trading/Indicators/` — 40 artifacts *(the folder that changed)*

| Artifact | md5 | Source? | What it is |
|---|---|---|---|
| ⭐ `MMM.tpl` | `db617bcdfeb5df26c033036f96c41472` | text | ⭐⭐ **The owner's MMM chart** — §2 |
| ⭐ `MMM INDICES.tpl` | `e6f977f56e5c87048795a8b344759a61` | text | Index variant — §2.1 |
| `RS5P.tpl` | `2709e6f6b972e6fc4d176165294d01d4` | text | Different method, same skeleton — §2.1 |
| ⭐ `!sm_WorkTime_v1.5b.ex4` | `b938ee1df8cf16a44bc16db71795e9f2` | ⛔ packed | ⭐⭐ **The time ribbon** — §4 |
| `sm_WorkTime_no_autogmt (1).ex4` | `8f0059bd2abf728b53198bb59f5ecaa2` | ⚠️ strings only | Older build; **yielded the input surface** — §4.2 |
| `!SM_TDI.ex4` | `635f774df6a5d83c9ed58104bf126b06` | ⛔ packed | The `D-045` TDI — §7 |
| `MM4XSF_TDI.ex4` | `42e97991cd6af1dfec95fbb333ae45ac` | ⛔ packed | Same family, **different binary**; identical to `Forex222/MM4XSF_TDI (1).ex4` |
| `Daily Range PeterE.ex4` | `b8d56b138186634fb6db287bb1caa683` | ⛔ packed | ADR on the MMM chart, `NumOfDays=10` — §6 |
| `MM_ADR.mq4` | `c155757f2391b94bcd234b58ae1a340a` | ✅ **SOURCE** | 2nd copy of `D-051`'s `mm_adr`; functionally identical — §6 |
| `PZ_QuartersTheory (3).ex4` | `4f7363d53c62b5e20093e9c24f1c975d` | ⛔ packed | Round-number grid — ⚠️ **not pivots**, §5.3 |
| `Quarters Theory indicator.ex4` | `2760c2a129c48eb9dd9084649b7b1e4d` | ⛔ packed | Same family, not on the MMM chart |
| `!SM_Daily_HiLo.ex4` | `b746486df691d261cf6002a732415caa` | ⛔ packed | On the MMM chart — prev-day H/L |
| `Weekly_High_Low Great.ex4` | `5323cf8799aa73a23c77b2ebc4ae0216` | ⛔ packed | On the MMM chart |
| `Candle Timer.ex4` | `7d7fa714dd712d9e6400385103330e45` | ⛔ packed | On the MMM chart, cosmetic |
| `ICT Day Of Week.ex4` | `7521bb3755dc95283f3f62e044bb3d60` | ⛔ packed | On the MMM chart, day separators |
| `Ultimate Blue.tpl` | `ea22c8cf527921cef072586b6fa28296` | text | ⭐ **The `D-045` artifact**, already admitted |
| `3M-shadow-boxes-15M.tpl` | `19187de9ac84dce672849c5cfa52a795` | text | `D-051` §4's ADR-stamp sibling |
| `FX dynasty.tpl` | `f2adbb3ecfc497a6f97b85983c27ba82` | text | `D-051` §1 |
| `Bo.tpl` | `cfa32805fbc37a089dc4e17b4c3fafb7` | text | `D-051` §1 — `ADRPeriod=21.0` |
| `W3Adeviation (1).mq4` | `25bfaf15b13c655b42ccc86c325657e1` | ✅ SOURCE | Weekly deviation levels. **Not on any MMM template** |
| `MM_Daily-Weekly_HL_Band (1).mq4` | `7e47af6031483292e90688360a95db28` | ✅ SOURCE | Daily/weekly H-L bands. Not on any MMM template |
| `automatic-trendlines.mq4` | `3af8f4aab7541affd87e4b0282b63c20` | ✅ SOURCE | Auto trendlines. Not on any MMM template |
| `Time Range Separator.ex4` | `ddd2cf80ba306edff0a4d128a04ddc22` | ⛔ packed | ⚠️ **A second time tool — NOT on any MMM template.** Not the ribbon |
| `!sw_Multi-MA.ex4` · `4X-2010-SEMA4X.ex4` · `PB Channel.ex4` · `!BP_Symbol.ex4` · `Watermark for MT4.ex4` · `candle_time_end_and_spread.ex4` · `Currency-Strength-Alerts-Indicator.ex4` · `Beast Super Signal.ex4` · `TMT - Daily Candle.ex4` · `SM_BPCT.ex4` · `Support and Resistance # TLB OC v02.ex4` · `ForexBlade.ex4` · `IceFX.NewsInfo.ex4` | *(see repo `git` blob)* | ⛔ packed | **None on any MMM template.** Unrelated tooling |
| `The Beast.tpl` · `Ultimate Blue.tpl` · `Clearer Vision.tpl` · `EN SR.tpl` · `- All in One - EMA Trend Trader (1).tpl` | — | text | Other methods' templates |
| `BEEKAY_FX (Trends &Resets)-1.pdf` · `BeeKay FX (Counting Levels). (2).pdf` | — | PDF | ⚠️ **A DIFFERENT AUTHOR'S MATERIAL.** Under `EXTERNAL_REFERENCE/README.md`'s ⛔ default: **not a source, not evidence, never cited** unless given its own `D-039`-style admission |

### 8.2 `Documents/Forex indicator/Forex222/` — unchanged since `D-051`

29 artifacts. `mm_adr.mq4`/`.ex4`, `MM4XSF_TDI (1).ex4`, `sm_WorkTime_no_autogmt.ex4`,
`Sessions (1).mq4`, `SupDem.ex4`, `PositionSizeCalculator.mq4`, `iExposure.mq4`,
`P4L CandleTime.mq4`, `average_price_v_3_0.mq4`, `daily_high_low.ex4`, `PipCounter1.ex4`,
`i-profittracker.ex4`, `R-Fish.ex4`, `SkarsFisherAlert.ex4`, `Multi-Chart-Sync.ex4`,
`Average Position.ex4`, `!XPS v8 PROFIT.ex4`, `luktom-pipsometer.ex4`, `SM_BPCT.ex4`,
`Support and Resistance # TLB OC v02.ex4`, `W3Adeviation.mq4`, `automatic-trendlines.mq4`,
`candle_time_end_and_spread.ex4`, `3M-shadow-boxes-15M.tpl`, `FX dynasty.tpl`.
**No pivot indicator. No `MMM.tpl`.**

### 8.3 `Desktop/All Folders/Downloads/` — the loose cluster

| Artifact | md5 | Note |
|---|---|---|
| ⭐ `PivotPoints.ex4` | `703ec775dcdff4c6995a722209ce0f2f` | ⭐ **The pivot candidate** — §5 |
| `Sessions.mq4` | `135d3d862c0441bc63b4ee00cdda307e` | ✅ **SOURCE** — see §8.4 |
| `MM4XSF_TDI.ex4` · `SM_BPCT.ex4` | as above | duplicates of the Forex222 copies |
| `Day Trading.mq4` · `SpreadIndicator.mq4` | ✅ SOURCE | unrelated |
| `FXWizard.ex4` · `XUP_Scanner_Client_*.ex4` · `x2014-pipsv2.ex4` | — | unrelated third-party products |

### 8.4 ⚠️ `Sessions.mq4` is NOT the ribbon — recorded so it is not mistaken for it later

`Sessions.mq4` / `Sessions (1).mq4` is **KimIV's `i-Sessions`** (2005, `kimiv.ru`) — a well-known
generic public indicator. Its defaults are `Asia 01:00–10:00`, `Eur 08:00–18:00`, `USA 14:00–23:00`.

⛔ **These numbers are NOT evidence about this course and must never be cited as session
boundaries.** They are one Russian author's 2005 defaults, they are **not** on any MMM template,
and they **disagree** with the ribbon the owner actually runs. They are recorded here **only** so a
future session that greps for "session" and finds readable source does not mistake it for the
attested tool.

⭐ **One thing it does supply, and it is mechanical, not evidential.** Its `DrawObjects()` shows the
standard MT4 idiom the ribbon must also use:

```mql4
t1 = StrToTime(TimeToStr(dt, TIME_DATE) + " " + tb);   // "08:00" -> a datetime on that date
b1 = iBarShift(NULL, 0, t1);
p1 = High[Highest(NULL, 0, MODE_HIGH, b1-b2, b2)];      // box top  = session high
p2 = Low [Lowest (NULL, 0, MODE_LOW , b1-b2, b2)];      // box base = session low
```

⭐ **`StrToTime` on the chart's own date resolves in SERVER TIME with NO GMT CONVERSION.** That is
the *baseline* behaviour, and it is exactly what a `no_autogmt` build would do — which sharpens
§4.4's question rather than answering it: **v1.5b's extra behaviour is the unknown, and this
confirms what it is extra to.**

---

## 9. WHAT THIS SURVEY CHANGED IN THE LEDGERS

**Nothing.** Stated explicitly so it cannot be misread:

| Record | Status after this file |
|---|---|
| `A-019`, `A-105`, `A-131` (session clock) | **OPEN.** ⭐ *Materially narrowed in §4.5–4.6, adjudicated nowhere.* One owner sentence could close them |
| `A-101` (pivot `M1`–`M4`) | **OPEN, `DO NOT CODE`.** A candidate artifact is named; it lacks source and attestation |
| `A-100` (ADR) | **OPEN.** `D-051` unchanged and still **NOT ADOPTED** |
| `A-084`, `A-086` | **Unchanged.** §7 explicitly declines to strengthen `A-084` |
| `A-020`, `D-043` (the MA set) | **Unchanged.** §3's 4/10 divergence is a **question to the owner**, not evidence |
| `A-005` (the trading zone) | **Unchanged.** §4.1's `25/50` alert strings corroborate the band, do not close it |
| `D-052`, `D-053` | **Consistent. Not reopened.** §7 |
| `SOURCING_HIERARCHY.md` §1 `TOOLING` rung | **Unchanged** — still `Ultimate Blue.tpl` / `!SM_TDI` and nothing else |

**The proposals that would change any of this are drafts:**
`DECISION_DRAFT_D-055_OWNER_STOP_AND_TARGETS.md` and
`DECISION_DRAFT_D-056_MMM_TPL_AND_TIME_RIBBON.md`.
