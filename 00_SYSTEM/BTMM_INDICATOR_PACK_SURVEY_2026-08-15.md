# BTMM INDICATOR PACK — SURVEY AND PROPOSED ADMISSION (`D-060`)

> **Branch:** `tools/btmm-indicator-pack-survey` · **Status:** `SURVEY + DRAFT — NOTHING ADOPTED`
>
> ## ⛔ THIS FILE ADMITS NOTHING, CLOSES NOTHING, AND WIRES NOTHING IN.
>
> Written on the owner's remark: *"I added another template to the indicator folder called basic
> btmm. I added another indicator folder within the folder… **It does have the pivot points.** If it
> helps the agent then we can add it."*
>
> Under `D-045` rule 1 **admission to the `TOOLING` rung is per-artifact and needs its own decision
> entry.** Nothing below is admitted by being listed. §9 is a **proposed** entry, `D-060`,
> **unadopted**.
>
> **Numbering, verified across integration (`19e6c2a`) and every remote branch:** highest **adopted**
> is `D-057`; `D-051`/`D-055`/`D-056`/`D-058`/`D-059` are held by unadopted drafts. **`D-060` is free
> everywhere.**

---

## 0. THE HEADLINE — FOUR RESULTS, AND ONE OF THEM OVERTURNS A STANDING FINDING

1. ⭐⭐⭐ **`D-051`'s central negative finding is FALSE and must be corrected.** `D-051` §1 states the
   course's own ADR indicator is *"NOT FOUND anywhere on the volume"* and that a grep for
   `Reached=`, `To ADR High`, `Today's Range` *"returns **zero files**."* ⛔ **All three strings are
   present in `!SM_ADR_Marker.ex4`**, together with the complete nine-field readout the V07 frames
   print. **The indicator family is found.** §3.
2. ⭐⭐⭐ **`!sw_Multi-MA` names the five nicknames as INPUT LABELS — and `Ultimate Blue.tpl`, the
   artifact `D-045` ALREADY ADMITTED, saves them as `Mustard=5 · Ketchup=13 · Water=50 · Mayo=200 ·
   Blueberry=800`.** That is `D-043`'s mapping exactly, from a platform artifact rather than from
   recollection. §5 — **and §5.3 explains why it still does not close `A-020`.**
3. ⭐⭐ **The pivot indicator the owner promised is real and is on-lineage** — `!SM_PivotPoints.ex4`,
   `!SM_`-prefixed, **dated the same day as `!SM_TDI`**, exposing `MidPivots` / `MidPivotColor`
   alongside standard/Fib/Camarilla sets. ⛔ **Compiled. `A-101` does not close.** §4.
4. ⚠️ **`BASIC BTMM.tpl` is empty.** 650 bytes, **zero indicators** — chart cosmetics only. §2.

> ### ⛔⛔ AND THE ANSWER TO *"DOES IT HELP THE AGENT?"* IS: **PARTLY, AND NOT IN THE WAY THAT WAS HOPED.**
>
> **The owner asked whether this gives the setup-detection agent computable logic. All twenty files
> are `.ex4` — COMPILED. There is not one `.mq4` in the folder.** So the pack yields **parameter
> surfaces and field names, never algorithms.** ⭐ **What it does give is better than nothing and
> worse than source**: it identifies *which* tools are canonical, it recovers *input names* that
> constrain what each computes, and in one case (`!SM_ADR_Marker`) it leaks **debug strings that
> expose real branching.** ⛔ **`D-030` still bars reconstructing any of them into agent logic.**

---

## 1. WHAT WAS FOUND AND WHERE

| | |
|---|---|
| **New template** | `Desktop/Trading/Indicators/BASIC BTMM.tpl` · md5 `1c8f8be76507ed3a7c492e62d1f2ef34` · **650 bytes** · 2026-08-15 |
| ⭐ **New sub-folder** | `Desktop/Trading/Indicators/INDICATORS/` · **20 files, all `.ex4`** · created 2026-08-15 |
| **Also checked** | `Documents/Forex indicator/Forex222/` — **unchanged**, still 29 artifacts, nothing added |

⭐ **The pack is coherent and it is the BTMM suite.** Fifteen of twenty carry the `!SM_` / `!sm_` /
`!btmm_` prefix — the same family as `!SM_TDI`, which `D-045` admitted. Dates cluster **2010–2015**,
against a **2012** course. ⭐ **This is materially better provenance than the first survey's finds**,
which were mostly third-party retail tools of mixed origin.

⚠️ **One artifact outside this folder is noted and NOT admitted:**
`Desktop/Trading/Steve Mauro ORIGINAL The Market Maker Method BTMM.pdf`. Under
`EXTERNAL_REFERENCE/README.md`'s ⛔ default it is **not a source, not evidence, never cited** until
it has its own `D-039`-style admission. ⭐ **It is flagged as potentially high-value** — a Mauro-
attributed document is Tier-2-class material — **and it is out of scope for this survey.** §10 Q5.

---

## 2. ⚠️ `BASIC BTMM.tpl` — THE NEGATIVE RESULT, REPORTED FIRST

**650 bytes. 47 lines. One `<window>`, one empty `<indicator>` block (`name=main`). ZERO custom
indicators.**

It carries chart cosmetics only: `USDCHF`, **M15**, `digits=5`, `scale=4`,
`background_color=8421504` (grey), `bullcandle_color=25600` (green),
`bearcandle_color=255` (red), `grid=0`, `volume=0`, `ohlc=0`.

⛔ **It attaches no indicator, saves no parameter, and therefore contributes nothing to any open
record.** ⭐ **Two data points only, and both are weak:** the method's basic chart is **M15** — which
agrees with the corpus's M15 material (V19/V20 entry work, `D-043`'s blueberry on the 15-minute) —
and the candle colouring is green/red.

⚠️ **Worth telling the owner plainly: if he expected this template to carry the BTMM indicator
stack, it does not.** He may have saved it before attaching the indicators, or exported the wrong
file. §10 Q1.

---

## 3. ⭐⭐⭐ `!SM_ADR_Marker.ex4` — THE COURSE'S ADR FAMILY IS FOUND, AND `D-051` §1 IS WRONG

**md5 `cddecc008ea0314238361ea0535747dd` · 12,720 B · dated 2011-05-08**

### 3.1 The test `D-051` specified, run against the new folder

`D-051` §1: *"A grep for its distinctive strings (`Reached=`, `To ADR High`, `Today's Range`) across
every indicator folder and the MT4 install returns **zero files**."*

| String | Result now |
|---|---|
| `Reached=` | ⭐ **`!SM_ADR_Marker.ex4`** |
| `To ADR High` | ⭐ **`!SM_ADR_Marker.ex4`** |
| `Today's Range` | ⭐ **`!SM_ADR_Marker.ex4`** |

**The binary carries the complete nine-field readout the V07 frames print:**

```text
ADR Value=  | Reached=  | Today's Range=  | T's High=  | T's Low=
Target High=  | Target Low=  | To ADR High=  | To ADR Low=
```

⭐⭐ **That is field-for-field the readout `D-051` §3 reconstructed from `V07_00-13-55` and
`V07_00-16-20` — the frames it solved to six equations with zero residual.**

### 3.2 ⚠️ But it is version **1.00**, not the course's **1.5**

Its embedded stamp is **`ADR 1.00 20051027 01 Mod 01`**. The course's charts read
**`ADR 1.5 20100528 01 Mod 01`**.

⭐ **So this is the SAME indicator, five years earlier — not the exact build.** It is precisely the
version whose stamp `D-051` §4 already found saved in `3M-shadow-boxes-15M.tpl`'s chart comment.
⭐ **That loop now closes: the tool that wrote that comment is this file.**

### 3.3 ⭐⭐ Inputs and leaked internals — the most computable thing in the pack

```text
TimeZoneOfData · TimeZoneOfSession · ATRPeriod · UseManualADR · ManualADRValuePips
LineStyle · LineThickness1 · LineColor1 · LineThickness2 · LineColor2
BarForLabels · DebugLogger · showtext
```

And — because `DebugLogger` leaves its format strings in the binary — **branch labels**:

```text
adr_low= today_high-adr        adr_low= today_low
adr_low= lasthigh-adr          adr_low= adr_low
High-Low/adr-Reached           Price=  [0=low, 1=high, 2=close]
Timezoned values: t-open= , t-high= , t-low=
today_start · ADR Start · --ADR High · ---ADR Low
```

⭐ **`adr_low` has FOUR distinct assignment branches.** That is real structural information about the
algorithm — not a parameter list — and it is the only algorithmic leak in the pack.

> ### ⚠️⚠️ AND IT PUTS `D-051` PART 3 IN DOUBT — flagged, not resolved
>
> `D-051` Part 3 provisionally closes `A-100`'s **RANGE DEFINITION** as *"`high − low` of the daily
> bar, **NOT true range**"*, on `mm_adr`'s source — and states its own weakness: *"`mm_adr` is not
> the indicator on the course's charts."*
>
> ⚠️ **The course-family indicator's period input is named `ATRPeriod`.** ATR is *by definition*
> **true range**. ⛔ **This does NOT establish that it computes true range** — an input name is not
> an implementation, the binary is compiled, and `High-Low/adr-Reached` appears in the same string
> table pointing the other way. **But `D-051` Part 3's provisional closure now has a named artifact
> arguing against it, and that must be on the record before the draft is adopted.**
>
> ⭐ **`UseManualADR` / `ManualADRValuePips` also matter**: the tool permits a **hand-set ADR**,
> which means a chart's displayed ADR may not be computed at all — a possibility no `A-100` candidate
> has considered.
>
> ⭐⭐ **And `TimeZoneOfData` + `TimeZoneOfSession` are TWO separate timezone inputs** — directly on
> `D-051` §5's *"the UTC offset stays unknown"* and on `A-105`/`C-032`.

---

## 4. ⭐⭐ `!SM_PivotPoints.ex4` — THE PIVOT INDICATOR, ON-LINEAGE, STILL UNREADABLE

**md5 `3ba04380827fd70a450aaf5d92da69f3` · 15,684 B · dated 2011-05-08**
Copyright string: **`2005, Robert Hill aka MrPip`**

```text
GMTshift · LabelShift · LineShift · PipDistance · ShowComment
Pivot · PivotColor · PivotFontColor · PivotFontSize · PivotWidth
StandardPivots · StandardFontColor · StandardFontSize · SupportColor · ResistanceColor
⭐ MidPivots · MidPivotColor · MidFontSize
CamarillaPivots · UseH1H2L1L2 · CamFontColor · CamFontSize
FibPivots · FibColor · FibFontColor · FibFontSize
```
Object names: `P Label` / `P Line`, `FibR1…FibR3`, `FibS1…FibS3` (+ Label/Line each).

### 4.1 ⭐ Why this is a much better candidate than the first survey's `PivotPoints.ex4`

| | First survey's find | ⭐ **This** |
|---|---|---|
| Prefix / family | `PivotPoints.ex4`, Forex Profit Launcher | ⭐ **`!SM_`** — the `D-045` family |
| Date | 2018 file, 2010 product | ⭐ **2011-05-08 — the SAME DAY as `!SM_TDI` and `!SM_ADR_Marker`** |
| Provenance | third-party retail | ⭐ **shipped inside the BTMM pack** |
| Mid levels | `Plot_middle` / `Color_Mid` | ⭐ **`MidPivots` / `MidPivotColor` / `MidFontSize`** |

⭐ **Three files sharing one date is strong evidence they shipped as one pack**, and it is the pack
the owner has now handed over as the BTMM toolset.

### 4.2 ⛔ And `A-101` still does not close

| | |
|---|---|
| ⛔ **Compiled, no source** | No `.mq4` anywhere. **The MidPivots FORMULA is not readable.** Concluding it is the midpoint of adjacent standard pivots is reading a variable name — `D-030`'s exact prohibition |
| ⚠️ **The count fits, and that is not proof** | Standard pivots `P/R1/R2/S1/S2` have **four** interstitial gaps, and `A-101`'s printed grid has **four** mid levels `M1`–`M4` in exactly those positions. ⭐ **Structurally consistent** — and `A-101` already records that the midpoint reading *"is consistent with the printed order and is not established by it"*, and that the schematic was **measured** and cannot discriminate |
| ⛔ **No saved parameters** | `BASIC BTMM.tpl` is empty and no template on the volume attaches `!SM_PivotPoints` — so **not even its input VALUES are recoverable**, unlike the ribbon and TDI |
| ⚠️ **`GMTshift`** | The pivot day boundary is itself timezone-shifted by an input — so *"midnight to midnight"* is configurable, which **widens** `A-082`'s caution rather than narrowing it |

```text
A-101 -- OPEN and DO NOT CODE. UNCHANGED BY THIS SURVEY.
  A better-lineage candidate now exists and is named. It would need READABLE
  SOURCE to bear on the construction, and it has none.
```

⭐ **Consistent with `D-059` §5A, this stays LOW priority for tool-building** — the owner has said
pivots are *"an added bonus"*. ⛔ **Its course-study priority is unchanged** — V16 is a dedicated
lesson.

---

## 5. ⭐⭐⭐ `!sw_Multi-MA` AND THE NICKNAMES — the strongest artifact result in this survey

**`!sw_Multi-MA.ex4` · md5 `c534ce6b2b557038ce92caca92b15376` · Copyright `2011 Steve Wilson`**

⭐ **Its inputs are named for the nicknames themselves:**

```text
Mustard · Ketchup · Water · Mayo · Blueberry
ArrowDistance · arrows · ShowTrend   (+ "Buy" / "Sell" / "Multi-MA" strings)
```

### 5.1 ⭐⭐ And two templates on the volume SAVE the values

| Template | md5 | Saved |
|---|---|---|
| ⭐⭐ **`Ultimate Blue.tpl`** — ***the artifact `D-045` already admitted*** | `ea22c8cf527921cef072586b6fa28296` | **`Mustard=5 · Ketchup=13 · Water=50 · Mayo=200 · Blueberry=800`** |
| `The Beast.tpl` (instance 1) | `2e1c14c4f69e6caadc84c57d79139f8b` | **`5 · 13 · 50 · 200 · 800`** — identical |
| ⚠️ `The Beast.tpl` (**instance 2**) | same file | ⚠️ **`5 · 13 · 195 · 750 · 3000`** |

> ### ⭐⭐ THIS IS `D-043`'s MAPPING, FROM A PLATFORM ARTIFACT INSTEAD OF FROM RECOLLECTION
>
> `D-043` is **mustard = 5 · ketchup = 13 · water = 50 · mayonnaise = 200 · blueberry = 800**, and it
> rests on **owner attestation** — an attestation that `SOURCING_HIERARCHY.md` §3.4 records as having
> been **reversed once within twenty-four hours** (`D-041` → `D-043`). ⭐ **`Ultimate Blue.tpl` agrees
> with it in all five cells, and the nickname↔period pairing is made by the INDICATOR AUTHOR's input
> labels, not by the owner.**

### 5.2 ⭐ And the two SHORT periods are stable where the long ones are not

⚠️ **Instance 2 of `The Beast.tpl` disagrees on three of five** — `Water=195`, `Mayo=750`,
`Blueberry=3000`. **So the values are user-set and freely re-parameterised**, which caps how much
any single save can prove.

⭐⭐ **But `Mustard=5` and `Ketchup=13` hold across ALL THREE saved configurations** — and those are
**precisely the two cells `D-041`/`D-042`/`D-043` fought over**, and precisely the two
`SOURCING_HIERARCHY.md` §3.4 records as having **no Tier 1 statement anywhere in V01–V11.**

### 5.3 ⛔ AND IT DOES NOT CLOSE `A-020`. FOUR REASONS, STATED BEFORE ANYONE IS TEMPTED

1. ⛔ **`TOOLING` ranks BELOW Tier 1.** This cannot produce `RESOLVED BY COURSE` under any reading.
2. ⚠️ **Scope question on `D-045` itself.** `D-045` rule 1 admits *"`Ultimate Blue.tpl` / `!SM_TDI`
   … **and nothing else**."* ⭐ **It is genuinely unclear whether that admits the TEMPLATE or only
   the TDI BLOCK INSIDE IT.** Reading it as the whole template would admit the Multi-MA block for
   free — **that reading is NOT taken here.** §10 Q3 puts it to the owner. **This is the single most
   important restraint in this section.**
3. ⚠️ **One installation, one user.** `D-056` §6 already refused to let two of the owner's own
   templates corroborate each other — *"two saves of one habit by one user are not two witnesses."*
   **The same refusal applies here**, and `The Beast.tpl`'s second instance proves the values move.
4. ⚠️ **It is 2011–2019 tooling against a 2012 course**, and `MMM.tpl` (2023) runs **4 and 10** — so
   **the owner's own artifacts disagree with each other** on exactly this pair.

⭐ **What it legitimately does: it makes `D-043` the better-supported arm of `A-143` by a clear
margin** — 5/13 now has an artifact behind it and 4/10 has one too, but 5/13's comes with the
nicknames attached. ⛔ **`A-143` and `A-020` both stay OPEN.** §10 Q2 is now much more valuable.

---

## 6. ⭐⭐ `!sm_gmtoffset.ex4` — a tool aimed straight at `A-105` / `C-032`

**md5 `1429caa767031d23e6c4894448f375f8` · 5,592 B · 2011-08-07 · author `FXRay`**

```text
input:   GMO_Hours
display: "GMT Offset is "
imports: GetSystemTime  ·  kernel32.dll
```

⭐ **A dedicated broker-GMT-offset display.** It calls `GetSystemTime` and compares the machine clock
to server time to **print the offset on the chart**.

> ### ⚠️ WHAT IT DOES AND DOES NOT DO FOR `C-032`
>
> ⛔ **It records nothing historically.** It computes the offset **live, at runtime**, so it cannot
> tell us what offset the 2023 `MMM.tpl` chart was on. **`C-032` — the one-hour ribbon-vs-V16-slide
> conflict — is NOT settled by its existence.**
>
> ⭐⭐ **But it makes `D-056` §8 Q2/Q8 answerable in seconds.** The owner can attach this to his chart
> and read the offset off the screen. **`D-056` §4A.2's UTC+2-vs-UTC+3 arms differ by exactly one
> hour, and this tool prints which.** ⭐ **That is the cheapest unblock available to the project right
> now**, and it needs no research at all.

⭐ **Note also that `!sm_WorkTime` ships in three builds here** — `!sm_WorkTime.ex4` (2011,
md5 `5c0fbf832ecad6a1a6d4a34bc9ef6ba5`, **NEW to the project**), `!sm_WorkTime_no_autogmt.ex4`
(`8f0059bd…`, known) and `!sm_WorkTime_v1.5b.ex4` (`b938ee1d…`, **byte-identical to the `D-056`
artifact**). ⭐ **The existence of a separate `!sm_gmtoffset` tool alongside a `no_autogmt` build
corroborates `D-056` §4.3's inference that the plain builds DO auto-adjust** — the pack ships both a
manual offset display and a no-auto variant, which is what you would expect. ⚠️ **Corroboration of an
inference, not a reading of the code.**

---

## 7. ⭐ `!SM_Crossover_Arrows.ex4` — the object of `D-058` tier 1, and it does not name the periods

**md5 `8c9b08ce44842d5b1846b169606c173f` · 5,508 B · 2010-07-30 — the oldest file in the pack**

```text
inputs:  FasterEMA · SlowerEMA · Show_Alert · Play_Sound · Send_Mail · SoundFilename
strings: "Cross Up on " · "Cross Down on " · " min " · " EMA"
```

⭐⭐ **A two-EMA crossover alert ships in the BTMM pack.** `D-058` tier 1 is *"the entry is the close
of the candle after **the ema cross**"* — ⭐ **so the EMA cross is a native object of this toolset,
not something the owner invented.** That materially strengthens `D-058` as a description of real
method practice.

⛔ **And it does not close `A-143`.** `FasterEMA` / `SlowerEMA` are **inputs whose default values are
not in the string table**, no template on the volume attaches this indicator, and `BASIC BTMM.tpl` is
empty — **so which two periods cross is exactly as unknown as before.** ⭐ *"Cross Up on … min … EMA"*
does confirm the alert is **timeframe-aware**, which is `A-143`'s second sub-question.

---

## 8. THE FULL INVENTORY — 20 files, **all compiled, zero source**

| Artifact | md5 | Readable? | What it is | Bears on |
|---|---|---|---|---|
| ⭐⭐ `!SM_ADR_Marker.ex4` | `cddecc00…` | ⭐ **inputs + debug branches** | **The course's ADR family, v1.00** | ⭐ `A-100`, `D-051`, `C-022` |
| ⭐⭐ `!SM_PivotPoints.ex4` | `3ba04380…` | inputs only | MrPip pivots + **MidPivots** | ⭐ `A-101` |
| ⭐⭐ `!sw_Multi-MA.ex4` | `c534ce6b…` | inputs only | **the nickname EMA tool** | ⭐ `A-020`, `D-043`, `A-143` |
| ⭐ `!sm_gmtoffset.ex4` | `1429caa7…` | inputs only | **broker GMT offset display** | ⭐ `A-105`, `C-032`, `D-056` |
| ⭐ `!SM_Crossover_Arrows.ex4` | `8c9b08ce…` | inputs only | 2-EMA cross alert | ⭐ `D-058`, `A-143` |
| `!SM_TDI.ex4` | `635f7745…` | inputs only | ⭐ **byte-identical to the `D-045` TDI** | `D-045`, `A-084` |
| `!sm_WorkTime_v1.5b.ex4` | `b938ee1d…` | packed | ⭐ **byte-identical to the `D-056` ribbon** | `D-056` |
| `!sm_WorkTime.ex4` | `5c0fbf83…` | inputs | ⭐ **third build, NEW** — has band 4 | `D-056` |
| `!sm_WorkTime_no_autogmt.ex4` | `8f0059bd…` | inputs | known build | `D-056` |
| `!btmm_TDI_Plus.ex4` | `d3a239d0…` | ⛔ packed (`TDI+` only) | a TDI variant | `D-053` — ⚠️ unreadable |
| `!SM_Daily_HiLo.ex4` | `bc75dc43…` | inputs | `PrevDayHi/Lo`, `DayHi/Lo` — ⚠️ **different build** from the parent folder's `b746486d…` | `D-059` §4 |
| `!SM_IlsleyPsychLevels.ex4` | `ec0fca67…` | inputs | `PsychHi/Lo`, `Offset` — round numbers | ⚠️ *not* pivots |
| `!SM_BPCT.ex4` | `3b34dac1…` | inputs | ⚠️ **different build** from parent's `946048e2…` | — |
| `!SM_AlertZone_1.ex4` | `16ef71a6…` | ⛔ packed | zone alert | — |
| `!SM_AlertZone_2.ex4` | `a49e529b…` | ⛔ packed | zone alert | — |
| `!SM_Alerting+TL+v1.1.ex4` | `aa3c409f…` | inputs | trendline alerting | — |
| `!SM_NewHUD.ex4` | `ff657ac8…` | inputs | 100 KB heads-up display | — |
| `!SM_ZUP_updated.ex4` | `631455ab…` | inputs | 324 KB — **ZUP harmonic patterns**, a large third-party tool | ⚠️ not method-specific |
| `!Chin Breakout Alert V-1.1.2s.ex4` | `860d93a6…` | inputs | multi-pair breakout alerter | — |
| `Info Plus.ex4` | `fda1dc93…` | ⛔ packed | 2025 — **newest file in the pack** | — |

⛔ **Zero `.mq4`. Zero source. That is the survey's most consequential single fact.**

---

## 9. THE PROPOSED LEDGER ENTRY — `D-060`, FOR THE OWNER TO APPROVE, EDIT OR REJECT

> ## D-060 — Five artifacts from the owner's BTMM pack are admitted to the `TOOLING` rung; `D-051` §1's "not found" finding is CORRECTED; and NOTHING is closed
>
> **Date:** 2026-08-15
> **Extends:** `D-045` Part 1, whose per-artifact rule requires a separate entry per artifact. Its
> three travelling rules apply unchanged.
>
> **Part 1 — the artifacts.** Supplied and attested by the owner as the BTMM indicator pack, admitted
> to **`TOOLING — OWNER-ATTESTED PLATFORM ARTIFACT`**: `!SM_ADR_Marker.ex4` (`cddecc00…`),
> `!SM_PivotPoints.ex4` (`3ba04380…`), `!sw_Multi-MA.ex4` (`c534ce6b…`), `!sm_gmtoffset.ex4`
> (`1429caa7…`), `!SM_Crossover_Arrows.ex4` (`8c9b08ce…`). ⛔ **These five and nothing else** — the
> remaining fifteen are inventoried in §8 and **not admitted**. Citations carry
> **`[TOOLING] <filename>`**.
>
> **Part 2 — ⭐⭐ `D-051` §1 IS CORRECTED.** Its finding that the course's ADR indicator is *"NOT
> FOUND anywhere on the volume"* and that `Reached=` / `To ADR High` / `Today's Range` return
> *"zero files"* **is FALSE as of this pack.** All three are in `!SM_ADR_Marker.ex4`, with the
> complete nine-field readout. ⚠️ **The stamp is `ADR 1.00 20051027`, not the course's
> `ADR 1.5 20100528`** — the same indicator, five years earlier, **not the exact build**.
> ⚠️⚠️ **And `D-051` Part 3's provisional range-definition closure is PUT IN DOUBT, not overturned**:
> the input is named **`ATRPeriod`** (ATR = true range), against `mm_adr`'s plain range. **An input
> name is not an implementation and the binary is compiled** — but `D-051` must not be adopted
> without addressing it. ⭐ `UseManualADR` also admits a **hand-set ADR**, a possibility no `A-100`
> candidate has considered.
>
> **Part 3 — ⭐⭐ the nickname mapping gains an ARTIFACT.** `!sw_Multi-MA` labels its inputs
> `Mustard/Ketchup/Water/Mayo/Blueberry`, and `Ultimate Blue.tpl` — **the `D-045` artifact** — saves
> **`5 · 13 · 50 · 200 · 800`**, matching `D-043` in all five cells, with the pairing made by the
> **indicator author's labels** rather than by recollection. ⭐ **`Mustard=5`/`Ketchup=13` are stable
> across all three saved configurations** found. ⛔ **`A-020` AND `A-143` STAY OPEN**: `TOOLING`
> ranks below Tier 1; ⚠️ **it is unresolved whether `D-045` admitted the whole template or only its
> TDI block**; one user's saves are not independent witnesses (`D-056` §6); and `The Beast.tpl`'s
> second instance saves `195/750/3000`, proving the values are freely re-parameterised.
>
> **Part 4 — ⛔ `A-101` does not close.** `!SM_PivotPoints.ex4` is a **much better-lineage**
> candidate than the first survey's — `!SM_`-prefixed, dated **the same day as `!SM_TDI` and
> `!SM_ADR_Marker`** — and exposes `MidPivots`/`MidPivotColor`. **It is compiled, no source exists,
> no template saves its values, and its `MidPivots` FORMULA is unreadable.** The four-mid-levels
> count fits `A-101`'s `M1`–`M4` **structurally and is not proof** (`D-030`). ⭐ Per `D-059` §5A this
> stays **LOW priority for tool-building** and **unchanged for course study**.
>
> **Part 5 — ⛔ `BASIC BTMM.tpl` contributes nothing.** 650 bytes, **zero indicators**, chart
> cosmetics only (`USDCHF`, **M15**, grey/green/red). Recorded so no session re-opens it expecting a
> stack.
>
> **Part 6 — ⛔⛔ AND THE PACK DOES NOT MAKE ANYTHING COMPUTABLE.** **All twenty files are compiled
> `.ex4`; there is not one `.mq4`.** The pack yields **parameter surfaces and field names, never
> algorithms** — the sole exception being `!SM_ADR_Marker`'s leaked `DebugLogger` branch labels.
> ⛔ **`D-030` bars reconstructing any of it into setup-detection logic**, and **no `PT`/`BT` and no
> agent component may cite this entry as a source of rules.**
>
> **Reason:** the owner asked whether the pack helps the trading agent. It does — **by identifying
> which tools are canonical and by correcting a standing negative finding** — and it does **not**
> supply the computable logic an agent needs. Recording both halves accurately is the point.
>
> **Evidence:** the twenty artifacts and md5s at §8; `BASIC BTMM.tpl` (`1c8f8be7…`);
> `Ultimate Blue.tpl` (`ea22c8cf…`) and `The Beast.tpl` (`2e1c14c4…`) Multi-MA blocks;
> `3M-shadow-boxes-15M.tpl` (`19187de9…`); `04_SCREENSHOTS/V07/INDEX.md` frames 14–15;
> `A-020`, `A-084`, `A-100`, `A-101`, `A-105`, `A-143`, `C-022`, `C-032`; `D-030`, `D-041`, `D-043`,
> `D-045`, `D-051`, `D-053`, `D-056`, `D-058`, `D-059`; `SOURCING_HIERARCHY.md` §1, §3.4.
> Owner attestation, 2026-08-15.
>
> **Alternatives considered:** *Closing `A-101` on `!SM_PivotPoints`* — ⛔ rejected; compiled, no
> source, and a variable name is not a formula. *Closing `A-020`/`A-143` on the Multi-MA values* —
> ⛔ rejected per Part 3, and the `D-045` scope question must be answered first. *Treating
> `!SM_ADR_Marker` as the course's build* — rejected; it is v1.00, the course's is v1.5.
> *Overturning `D-051` Part 3 on `ATRPeriod`* — rejected; an input name is not an implementation —
> **but flagging it is mandatory.** *Admitting all twenty* — rejected; `D-045` rule 1 is
> per-artifact, and fifteen bear on no open record. *Admitting the Mauro BTMM PDF found nearby* —
> rejected; that is a `D-039`-class question of its own.
>
> **Consequences:**
>
> 1. `SOURCING_HIERARCHY.md` §1's `TOOLING` rung gains the five artifacts with md5s and a pointer
>    here. The rung's rules are unchanged.
> 2. ⭐⭐ **`D-051` must be amended before adoption** — §1's "not found" corrected, and Part 3's
>    range-definition closure re-argued against `ATRPeriod`. **`D-051` remains UNADOPTED.**
> 3. ⛔ **No `A-xxx` or `C-xxx` changes status.** `D-045` rule 2: **admission is not reading.**
> 4. ⭐ **`!sm_gmtoffset.ex4` is recorded as the cheapest available unblock for `C-032`** — attaching
>    it to the owner's chart prints the offset that separates `D-056` §4A.2's two one-hour-apart arms.
> 5. ⚠️ **The `D-045` scope question** — whole template or TDI block only — **is surfaced and must be
>    answered before any Multi-MA-based argument is used.**
> 6. ⛔ **No agent component may be built on this pack.** Part 6.
>
> **Status:** ACTIVE — admission only; **every `A-xxx` remains OPEN**; **nothing becomes computable**

---

## 10. THE QUESTIONS FOR THE OWNER

1. ⚠️ **`BASIC BTMM.tpl` is empty — 650 bytes, no indicators.** Did you mean to send a template with
   the stack attached? If you have the populated one, **that is what carries the saved parameter
   values**, which is where the real information lives (as `MMM.tpl` was for the ribbon and TDI).
2. ⭐⭐ **Which two EMAs does `!SM_Crossover_Arrows` use on your chart** — its `FasterEMA` /
   `SlowerEMA`? §7. This is `A-143` and `D-058` tier 1 in one question, and **a screenshot of its
   inputs dialog answers it.**
3. ⭐ **Did `D-045` admit all of `Ultimate Blue.tpl`, or only its TDI block?** §5.3. It matters:
   the whole-template reading would let the `Mustard=5/Ketchup=13` values be cited immediately.
4. ⭐⭐ **Would you attach `!sm_gmtoffset.ex4` to your chart and tell us what it prints?** §6.
   **One number settles `C-032` and the ribbon's clock** — the cheapest open item in the project.
5. ⚠️ **`Steve Mauro ORIGINAL The Market Maker Method BTMM.pdf` sits in `Desktop/Trading/`.** Is that
   a document you want admitted as evidence? It would need its own `D-039`-style ruling, as the Mauro
   seminar notes did — **it is not being used for anything until you say so.**
6. **Do you actually run `!SM_ZUP_updated` (harmonic patterns) or `!SM_NewHUD`?** Neither is in
   `D-059`'s canonical four, and both are large tools. If they are dormant, saying so keeps the
   inventory honest.
