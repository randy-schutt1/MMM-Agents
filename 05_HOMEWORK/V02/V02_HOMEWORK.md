# V02 — HOMEWORK

| Field | Value |
|---|---|
| Video ID | V02 |
| Assigned | `[00:52:20]`–`[00:56:14]`, and the R&D slide at `[00:55:35]` |
| Attempted | 2026-08-10 |
| Data source | TradingView, FXCM feed, 1-hour charts, **no account used** |
| Charts | `05_HOMEWORK/V02/charts/` |

Two assignments were set. **11a is completed on real data with a documented substitution.
11b is NOT completed, and the reason is evidential, not logistical** — see §2.

---

## 0. THE DATA SUBSTITUTION, STATED UP FRONT

The instructor set this on **18 March 2012** and asked for *"last Sunday to this Sunday"*
— i.e. the week of **11–18 March 2012** — on the **one-hour** chart.

**That data is not obtainable.** TradingView's free tier caps intraday history at
**5,000 bars**; on a 1-hour chart that reaches back only to **6 January 2025**. The block
is explicit and is captured as evidence:

```text
"Power up your plan — You're limited to 5,000 bars. Upgrade now to see further back in time."
   After sign up:  Basic    5,000 bars
   Recommended:    Premium 20,000 bars
```

→ `charts/EVIDENCE_tradingview-5000-bar-limit.png`

Note that even the Premium tier's 20,000 hourly bars falls **between ~2.3 years**
(counting 24 bars per calendar day) **and ~3.2 years** (counting the ~120 H1 bars an FX
week actually produces) — and would still not reach 2012 under either reading. This is an
account/paid gate, not a navigation problem, and per the standing instruction it is
**flagged rather than worked around**. No account was created, no credentials were
entered, and no bot check was bypassed.

> **RECONCILIATION NOTE — added 2026-08-10 (R1 finding 6).** The two figures above do not
> fully reconcile, and that is recorded rather than smoothed over. The evidence screenshot
> shows 1H candles displayed across **2–8 January 2025** (crosshair: `Mon 06 Jan '25
> 04:00`; 6 Jan 2025 was indeed a Monday), i.e. a reach of **~19 months** before the
> 10 Aug 2026 capture. At ~120 H1 bars per FX week, 19 months is roughly **9,800 bars** —
> about double the stated 5,000-bar cap.
>
> **I cannot explain the discrepancy from the screenshot alone**, and I am not going to
> invent a mechanism for it. Both observations stand as observed: the platform displays
> the 5,000-bar upsell dialog, *and* 1H data was reachable back to early January 2025.
> Neither reading changes the conclusion — 2012 is unreachable by an order of magnitude
> either way — so the substitution decision does not depend on resolving it.

**Substitution made:** the same exercise, on the same instrument and timeframe, for the
most recent complete week — **Sunday 2 August to Friday 7 August 2026**. The exercise is
"label one week's cycle on the 1H chart"; its instructional value does not depend on
which week. What *is* lost is the ability to compare against the instructor's own answer
key, which he said he would post in the 2012 forum — that key is unavailable to this
project regardless of which week is used.

---

## 1. ASSIGNMENT 11a — LABEL THE WEEKLY CYCLE (USD/CHF, 1H)

**Chart:** `charts/USDCHF_1H_2026-08-10_tradingview-fxcm.png`
Week analysed: Sun 2 Aug – Fri 7 Aug 2026.

> ### ⚠ R1 REMEDIATION NOTICE — 2026-08-10
>
> Review `18_REVIEW/V02/V02_REVIEW_R1.md` raised a **MAJOR** finding (`E06`/`E19`)
> against this section: the first-pass markup below misread the chart it cites, and the
> misreading produced a **false confirmation** of the "at least 3 days" doctrine that
> `C-001` has open as the project's foundational unresolved contradiction.
>
> Per `REMEDIATION_PROTOCOL.md` §2 the original markup is **redone, not reworded**. The
> first-pass table and its conclusions are retained below, marked
> `SUPERSEDED — INVALID READING (R1 MAJOR 1)`, and the corrected reading follows in
> §1.2. Nothing has been deleted.
>
> The reviewer's own measured per-day table was used **as a check, not as the answer**
> (`REVIEW_PROTOCOL` instruction in required correction 1). The chart was re-measured
> independently from the committed PNG; the method is stated in §1.1 so it can be
> reproduced.

### Why this is presented as a table rather than as drawings on the chart

The instructor's instruction is to mark up the chart and post the image. Drawing on
TradingView reliably requires a saved layout, which requires an account. Rather than
place boxes at coordinates estimated from axis ticks — the Sunday session is partial, so
the day-column boundaries cannot be pinned from the tick labels alone — the markup is
given as a table keyed to date, time and price. That is auditable in a way an
approximately-placed rectangle is not. The clean chart is included as the evidence.

> **CORRECTED 2026-08-10 (R1 remediation).** The claim above that *"the day-column
> boundaries cannot be pinned from the tick labels alone"* is **false, and it was the
> excuse that let the MAJOR through.** §1.1 pins every boundary exactly: ~~the x-axis date
> labels sit on the 6-px bar lattice and give Mon–Thu = 24 bars, Fri = 21, Sun = 3, with
> the day mapping independently confirmed by open = prior close on all six boundaries.~~
> The boundaries were pinnable the whole time; they simply were not pinned.
>
> **AMENDED 2026-08-10 (R2 Minor 1).** The struck sentence above is corrected: the chart
> draws its **own dotted day separators** at `x = 147, 273, 429, 573, 717, 861, 987, 1149`,
> and they give Mon–Thu = 24 bars, **Fri 31 Jul = 21**, **Sun 2 Aug = 2**, Fri 7 Aug = 21.
> The open = prior close check does **not** validate all six boundaries — see the R2
> correction block in §1.1. The point being made here is unaffected and is in fact
> stronger: the boundaries were not merely pinnable, they were **printed in the image**.
>
> The *conclusion* of this section still stands — a table keyed to date, time and price
> remains more auditable than a drawn rectangle, and is more so now that the values are
> measured. Only the stated reason was wrong.

### The markup — `SUPERSEDED — INVALID READING (R1 MAJOR 1)`

```text
SUPERSEDED — INVALID READING (R1 MAJOR 1)
Retained per REMEDIATION_PROTOCOL.md §2. Superseded by §1.2.
Do not cite any price or date from this table.
```

The claim that opened this section — *"price levels are read off the chart's price axis
and are accurate to roughly ±5 pips"* — was **not true**. Rows 1, 2, 4, 5 are off by
10–15 pips, row 2 names a price (`0.8130`) that was not traded on the day it is assigned
to, and row 7 attributes Thursday's move to Friday with the direction inverted.

Labels are the ones the instructor uses on his own worked answer chart at `[00:18:00]`
(`04_SCREENSHOTS/V02/V02_00-18-00_weekly-market-structure-levels-chart.png`). I am
imitating his demonstrated example, not inventing a scheme.

| # | His label | Where I place it this week | Price region | Reasoning |
|---|---|---|---|---|
| 1 | **False Move Week Beginning** | Sun 2 – early Mon 3 Aug | ~0.8070 – 0.8090 | The week opens in a narrow range after the previous week's sharp sell-off, then pushes **up** into Mon 3 Aug. Under the lesson's framing this opening push is the move that traps — here it would trap shorts carried over from the prior week's drop. |
| 2 | **PFH** (peak formation high) | Mon 3 Aug | ~0.8130 | The high of the opening push. This is the week's first structural extreme. |
| 3 | **Stop Hunt / reversal** | Mon 3 → Tue 4 Aug | from ~0.8130 back to ~0.8100 | Price rejects the 0.8130 area and settles into a tight range. |
| 4 | **Level 1** | Tue 4 Aug | ~0.8095 – 0.8115 | First leg after the anchor: a contained range, no new extreme. |
| 5 | **Level 2** | Wed 5 Aug | ~0.8075 – 0.8100 | Second leg, lower. Direction is now established downward. |
| 6 | **Level 3 / PFL** | Thu 6 Aug | low ~0.8062 | Third leg completes at the week's low. Under his scheme this is where "Level 3 Exit and Reverse" belongs. |
| 7 | **Reverse** | Fri 7 Aug | ~0.8062 → ~0.8130 | Sharp rise off the low back to the week's high area — the reversal after Level 3, matching the shape of his answer chart. |
| 8 | **End of week** | late Fri 7 Aug | drop to ~0.8060 | A second sharp drop into the close. |

### What matches the lesson, and what does not — `SUPERSEDED (R1 MAJOR 1)`

```text
SUPERSEDED — INVALID READING (R1 MAJOR 1). Superseded by §1.3.
The "three days" bullet below is WITHDRAWN. It was a false confirmation of C-001.
```

**Matches:**
- The week does resolve into roughly **three legs** between the opening extreme and the
  opposite extreme, which is the shape his answer chart shows.
- ~~The move away from the Monday high runs **Tuesday through Thursday** — about three
  days — consistent with the printed "For At Least 3 Days" on the Weekly Structure
  slide.~~ **WITHDRAWN.** Thursday is when price came back *above* the Monday high, not
  part of the move away from it. See §1.3.
- The Level 3 termination is followed by a sharp reversal, as his chart labels.

**Does not match, and is recorded rather than smoothed:**
- **The anchor point is ambiguous this week.** The lesson says the anchor is "where the
  midweek reversal comes in". Here the decisive extreme is on **Monday**, not midweek.
  Under `[00:11:44]` ("Sunday is the Asian session… could be Friday, Sunday, Monday") this
  is an allowed variation, but it means the single most important object in the lesson is
  placed by judgement, not by rule.
  → **Corrected in §1.3:** the week's decisive extreme is on **Thursday**, not Monday.
- **Friday does not behave.** `[00:05:24]` says "You always get out on Friday, always",
  and his chart shows the week ending quietly. This week Friday carried the largest range
  of the week in both directions. The lesson has no label for that.
- **I cannot verify the "does not cross the level for 2.5–4 days" claim** because
  "the level" (A-004) is defined only as an ordinal leg, not as a specific price line.
  → This bullet **survives correction** and is the load-bearing one. See §1.3.

---

## 1.1 HOW THE CHART WAS MEASURED (R1 remediation)

The first pass placed prices by eye against the axis tick labels. That is what failed.
The corrected reading is measured from the pixels of the committed PNG, so it is
reproducible by anyone with the file.

| Step | Method | Result |
|---|---|---|
| Candle detection | Select pixels matching TradingView's default body colours exactly — bullish `rgb(8,153,129)`, bearish `rgb(242,54,69)`, tolerance ±8. Volume bars use distinct lighter tints and are excluded automatically. | Candle mask |
| Artifact removal | The dashed current-price line at `y=434` is drawn in the **exact** bullish body colour and spans the chart. Pixels on that row are kept only where the same column also has candle pixels at `y=433` or `y=435`. | Without this the measured high of three separate days reads exactly `0.81025`, the current price — the tell that caught it |
| Price calibration | Least-squares fit through the 13 unobstructed right-axis label centres (`0.81700` … `0.80400`) | **52.27 px per 0.00100**; max residual **0.10 pip** |
| Bar pitch | Column structure of the candle mask | **6 px per H1 bar**, bar centres ≡ 3 (mod 6) |
| Day boundaries | ~~The x-axis date labels are centred on the first bar of each day. Labels `4`, `5`, `6`, `7`, `9`, `11` sit at x = 429, 573, 717, 861, 987, 1149 — all on the 6-px lattice.~~ **SUPERSEDED (R2 Minor 1)** — six of the eight labels were measured and the other two were declared ambiguous. See the corrected row below. | ~~Mon–Thu = **24 bars**, Fri = **21 bars** (861→987 = 126 px), Sun = **3 bars** (987→1005 = 18 px)~~ |
| **Day boundaries — CORRECTED (R2 Minor 1)** | The chart **draws its own day separators**: faint dotted vertical lines in `rgb(213,213,213)`, at `x = 147, 273, 429, 573, 717, 861, 987, 1149` — every one on a bar centre (`x ≡ 3 mod 6`). All eight x-axis date labels sit within 0.9 px of their separator, including the two the first correction declined to measure (`31` → centroid **146.12**, i.e. bar 147; `Aug` → centroid **273.03**, i.e. bar 273). | Fri 31 Jul = **21 bars** (147→273), **Sun 2 Aug = 2 bars** (273→285), Mon–Thu = **24 bars**, Fri 7 Aug = **21 bars**, Sun 9 Aug = **3 bars** |
| Independent check | Each measured daily **open** should equal the previous day's **close** | ~~It does, on all six boundaries — this validates the day mapping, which was the first pass's actual failure~~ **RESTATED (R2 Minor 1):** it holds on **174 of the 176 bar-to-bar boundaries** to within 0.15 pip, which is what makes the series verifiable — but it **cannot** adjudicate the Fri→Sun weekend boundary, where a non-zero gap is the normal case. The one true discontinuity in all 177 bars is **−12.6 pip at `x=273`**, and that is the weekend gap. See the correction block below |

Chart timezone is **UTC** (printed in the chart footer: `19:21:20 UTC`). ~~Sunday's three
bars are 21:00, 22:00 and 23:00 UTC.~~ **CORRECTED (R2 Minor 1): Sun 2 Aug carries two
bars, 22:00 and 23:00 UTC.** (Sun 9 Aug, outside the analysed week, carries three.)

**Timebase confirmation.** The last-price badge shows a countdown of `38:40` at a footer
clock of `19:21:20 UTC`, and `19:21:20 + 38:40 = 20:00:00` exactly — so the rightmost bar
is the 19:00 UTC hour and the hour indices above are UTC, not a local offset.

```text
SUPERSEDED — INVALID BOUNDARY REASONING (R2 MINOR 1)
Retained in place per REMEDIATION_PROTOCOL.md §2. Superseded by the
corrected block that follows. Do not cite the adopted hypothesis or the
Sun 2 Aug / Fri 31 Jul values that follow from it.
```

**The one boundary that had to be settled: Sun 2 Aug.** Whether Sunday 2 Aug carries two
bars or three shifts the whole Fri 31 Jul → Mon 3 Aug chain by one bar, and the `31` date
label is ambiguous between the two (it is a two-character label and sits between the two
candidate bar centres). It was resolved by the open-equals-prior-close test rather than
by preference:

| Hypothesis | Fri 31 Jul close → Sun 2 Aug open |
|---|---|
| **Sunday = 3 bars** (21:00, 22:00, 23:00) — adopted | 0.80831 → 0.80831 — **0.0 pip** |
| Sunday = 2 bars (22:00, 23:00) | 0.80678 → 0.80552 — **12.6 pip discontinuity** |

The three-bar reading is also what the unambiguous end of the chart requires: Sun 9 Aug is
pinned between the verified `9` and `11` labels and carries **exactly three** bars, and
the same feed cannot give one Sunday three bars and the other two. Nothing in §1.2 turns
on this — the week's low sits in the 22:00 bar either way — but it is recorded because
"nothing turns on it" was the reasoning that let the first pass leave its day boundaries
unpinned.

#### CORRECTED BOUNDARY REASONING — 2026-08-10 (R2 Minor 1)

**The adopted hypothesis above is wrong. Sun 2 Aug carries 2 bars, not 3; bar `x=267`
belongs to Friday 31 July.** The boundary did not have to be "settled" by inference at
all — the chart states it. Four lines of evidence, three of them in the PNG and none of
them consulted above:

1. **The chart's own dotted day separators** sit at `x = 147` and `x = 273`. `147→273` is
   **21 bars** — a complete Friday, identical to Friday 7 Aug's 21. `273→429` is 26 bars
   = Sunday (2) + Monday (24).
2. **The two date labels the block above declined to measure settle it.** The claim that
   `31` *"is ambiguous… it sits between the two candidate bar centres"* is **withdrawn**:
   its sub-pixel ink centroid is **146.12** — 0.88 px from bar 147 and 5.12 px from bar
   141. `Aug`, the first bar of the month and therefore the first bar of the Sunday
   session, centres at **273.03** — 0.03 px from bar 273 and 6.03 px from bar 267. The
   worst of the six labels that *were* measured misses its bar by 0.64 px, and the
   two-glyph `11` misses by 0.06 px, so multi-character labels are not offset.
3. **The continuity test points the other way.** There is exactly **one** open ≠
   prior-close discontinuity in all 177 bars: **−12.6 pip at `x=273`**. Under the
   corrected mapping that is the **weekend gap**, exactly where a gap belongs, and every
   other boundary is continuous. Under the superseded mapping the weekend gap is 0.0 pip
   and a 12.6-pip discontinuity sits *inside* the Sunday session, between its 21:00 and
   22:00 bars — unexplained, and not surfaced in the table above.
4. **Bar 267 does not behave like a Sunday-open bar.** Its volume bar is 49 px and its
   range 23.7 pip; the unambiguous Sunday bars either side are 27 px and 27 px, and Sun
   9 Aug's three are 9, 14 and 13 px. Bar 285's volume is 113 px — a session open, not a
   Sunday 23:00 — confirming Monday starts at 285 and holds a full 24 bars.

**The `"the same feed cannot give one Sunday three bars and the other two"` argument is
also withdrawn.** It is a symmetry assumption and the separators refute it: Sun 2 Aug
carries two bars and Sun 9 Aug carries three. A missing thin Sunday-open hour is an
ordinary feed artifact.

**The methodological error matters more than the pips.** Open = prior close is a sound
check *within* a session — it is what makes 174 of the 176 bar boundaries verifiable —
but it **cannot adjudicate a weekend boundary**, because a non-zero Friday-to-Sunday gap
is the normal case. It was used above to choose between two hypotheses at precisely that
boundary, and it selected the one that made the real weekend gap vanish. So the sentence
*"it does, on all six boundaries"* was never evidence that the mapping was right; under
the correct mapping it is evidence that one day boundary had been placed at a continuous
point **inside Friday**.

**What this changes, stated exactly:**

| | Superseded | Corrected |
|---|---|---|
| Sun 2 Aug bar count | 3 | **2** (22:00, 23:00) |
| Sun 2 Aug Open | 0.80831 | **0.80552** *(0.80831 is Friday's 19:00 close)* |
| Sun 2 Aug High | 0.80870 `21:00` | **0.80737 `23:00`** |
| Sun 2 Aug Low / Close | 0.80552 `22:00` / 0.80699 | unchanged — both already correct |
| *Fri 31 Jul* Open / Low / Close | *0.80527 / 0.80514 / 0.80831* | ***0.80578 / 0.80538 `00:00` / 0.80678*** |
| *Fri 31 Jul* High | *0.81289* | unchanged — already correct |

**No conclusion in this homework changes.** Both mappings anchor Mon 3 Aug 00:00 at
`x=285`, so the week's low is still 0.80552 in the Sunday 22:00 bar, the week's high is
still Thursday's, all of Mon–Fri is untouched, and §1.3's 72-hour `C-001` result is
unaffected. What moves is a partial weekend session's open and high, plus a prior-week
reference row that no claim rests on.

**The transferable lesson**, recorded because it is a second instance of the same class
of failure R1 charged: *the parts of a source you did not read are not thereby ambiguous.*
Six of eight date labels were measured and the other two were declared ambiguous without
being measured. The chart had been drawing its own day boundaries the whole time.

**Residual uncertainty: ±1 px ≈ ±0.2 pip** on each extreme, plus the ±0.1 pip
calibration residual. The honest accuracy claim for the corrected table is therefore
**±0.5 pip**, and it is measured rather than asserted.

### Measured daily OHLC — USD/CHF 1H, FXCM — `SUPERSEDED IN PART (R2 MINOR 1)`

```text
SUPERSEDED IN PART — rows 1 and 2 only (Fri 31 Jul, Sun 2 Aug).
Retained in place per REMEDIATION_PROTOCOL.md §2. Superseded by the
corrected table below. Mon 3 Aug – Fri 7 Aug are unaffected and were
independently verified correct by V02 review R2.
```

| Day (UTC) | Open | High | Low | Close |
|---|---|---|---|---|
| *Fri 31 Jul (prior week)* | *0.80527* | *0.81289* | *0.80514* | *0.80831* |
| Sun 2 Aug (3 bars) | 0.80831 | 0.80870 `21:00` | **0.80552** `22:00` ← week low | 0.80699 |
| Mon 3 Aug | 0.80697 | **0.81151** `15:00` | 0.80560 `00:00` | 0.81038 |
| Tue 4 Aug | 0.81038 | 0.81061 `05:00` | 0.80801 `14:00` | 0.80910 |
| Wed 5 Aug | 0.80910 | 0.81013 `08:00` | 0.80606 `21:00` | 0.80667 |
| Thu 6 Aug | 0.80667 | **0.81356** `15:00` ← week high | 0.80602 `02:00` | 0.81239 |
| Fri 7 Aug (21 bars) | 0.81239 | 0.81291 `00:00` | 0.80564 `12:00` | 0.80753 |

### Measured daily OHLC — CORRECTED (R2 Minor 1) — USD/CHF 1H, FXCM

Day boundaries taken from the chart's own dotted separators. **This is the table to
cite.** Values are ±0.5 pip; where this table and R2's independent re-measurement differ
it is by 0.1–0.2 pip, i.e. one pixel.

| Day (UTC) | bars | Open | High | Low | Close |
|---|---:|---|---|---|---|
| *Fri 31 Jul (prior week)* | *21* | *0.80578* | *0.81289* `14:00` | *0.80538* `00:00` | *0.80678* |
| Sun 2 Aug | **2** | **0.80552** | **0.80737** `23:00` | **0.80552** `22:00` ← week low | 0.80699 |
| Mon 3 Aug | 24 | 0.80697 | **0.81151** `15:00` | 0.80560 `00:00` | 0.81038 |
| Tue 4 Aug | 24 | 0.81038 | 0.81061 `05:00` | 0.80801 `14:00` | 0.80910 |
| Wed 5 Aug | 24 | 0.80910 | 0.81013 `08:00` | 0.80606 `21:00` | 0.80667 |
| Thu 6 Aug | 24 | 0.80667 | **0.81356** `15:00` ← week high | 0.80602 `02:00` | 0.81239 |
| Fri 7 Aug | 21 | 0.81239 | 0.81291 `00:00` | 0.80564 `12:00` | 0.80753 |

Sun 2 Aug's open and low are the same bar: the week opens **at the week's low**, in its
first bar. The weekend gap Fri 31 Jul close → Sun 2 Aug open is **−12.6 pip**, and it is
the only open ≠ prior-close discontinuity in the series.

---

## 1.2 THE CORRECTED MARKUP

Same labelling scheme, same source (`04_SCREENSHOTS/V02/V02_00-18-00_weekly-market-structure-levels-chart.png`).
**Only the prices, days and directions are corrected.** The labels themselves remain my
imitation of a worked example and are still unverified — see §1.4.

| # | His label | Corrected placement | Measured price region | Reasoning |
|---|---|---|---|---|
| 1 | **False Move Week Beginning** | Sun 2 Aug 21:00 → Mon 3 Aug 15:00 | **0.80552 → 0.81151** | The week does **not** open in a narrow range. It opens by making **the week's low** in **the first bar of the week** (0.80552 at Sun 22:00 — the Sunday session is 2 bars, not 3; corrected R2 Minor 1), then runs ~60 pips up into Monday afternoon. Under the lesson's framing this opening push is the move that traps; here it would trap shorts carried over from Friday's decline. |
| 2 | **PFH** (peak formation high) | Mon 3 Aug **15:00** | **0.81151** | Monday's high, and the week's first structural extreme. *(First pass said `~0.8130` — a price not traded on Monday at all.)* |
| 3 | **Stop hunt / reversal** | Mon 3 Aug 15:00 → Tue 4 Aug | 0.81151 → 0.80801 | Price rejects the Monday high and contracts. Tuesday is the week's **narrowest** day (26 pips). |
| 4 | **Level 1** | Tue 4 Aug | **0.80801 – 0.81061** | First leg after the anchor: a contained range, no new extreme. |
| 5 | **Level 2** | Wed 5 Aug | **0.80606 – 0.81013** | Second leg, lower. Direction is established downward. |
| 6 | **Level 3 / PFL?** | Thu 6 Aug 02:00 | **0.80602** | Thursday's low. ⚠ **It is not the week's low** — Sunday's 0.80552 and Friday's 0.80564 are both lower. Calling it `PFL` is not supportable. |
| 7 | **Reverse** | **Thu 6 Aug** 02:00 → 15:00 | **0.80602 → 0.81356** | The sharp rise off the low is **Thursday's**, not Friday's, and it is the largest move of the week (75 pips in 13 hours, 33 of them in the 15:00 bar). *(First pass assigned this to Friday and inverted it.)* |
| 8 | **End of week** | Fri 7 Aug | **0.81291 `00:00` → 0.80564 `12:00`**, close 0.80753 | Friday **opened at its high and fell 73 pips**, then recovered ~19 into the close. *(First pass had Friday rising.)* |

### What the correction changes structurally

The first pass produced a tidy five-stage week: push up → three descending legs → reverse
→ drop. **The measured week is not that.**

- The week's **low** (0.80552) is in the **Sunday open**, and the week's **high**
  (0.81356) is on **Thursday afternoon**. Both extremes are in places the first pass did
  not put them.
- **Rows 6, 7 and 8 collapse onto one day.** Thursday makes the low at 02:00 *and* the
  week's high at 15:00. The instructor's scheme labels "Level 3", "Reverse" and the
  week's terminal extreme as separate structural events; here they are hours apart on a
  single day, and **the lesson provides no label for that**.
- The "three descending legs" reading survives only for **Tue → Wed**. Thursday breaks it.

---

## 1.3 WHAT THE CORRECTED WEEK ACTUALLY SAYS ABOUT `C-001`

**The withdrawn claim.** The first pass wrote that the move away from the Monday high ran
*"Tuesday through Thursday — about three days — consistent with the printed 'For At Least
3 Days'"*. That is **withdrawn**. Thursday is when price traded back *above* the Monday
high, not part of a move away from it.

**What was measured instead.** Taking Monday's high as the level — a choice discussed
below — the first hourly bar to trade above 0.81151 is:

```text
level set:      Mon 3 Aug 15:00 UTC   high 0.81151
first breach:   Thu 6 Aug 15:00 UTC   high 0.81356
elapsed:        72 hours = exactly 3.00 days
```

The 72-hour figure is exact to the hour, not rounded. Tue and Wed both closed below the
level; Thursday's 13:00 and 14:00 bars reached 0.81027 and then the 15:00 bar cleared it.

**Why this neither confirms nor refutes the doctrine.**

| Counting convention | Result | Verdict against "at least 3 days" |
|---|---|---|
| Hours elapsed, level-set bar → first breach bar | 72 h = 3.00 days | Satisfied, **by zero margin** |
| Whole calendar days closing below the level | Tue, Wed = **2** days | Not satisfied |
| Days until the *daily close* exceeded it | Thu closed 0.81239 > 0.81151 → **3** days | Satisfied |
| `[00:16:23]`'s upper bound ("or four days") | 3 days | Not reached |

Three conventions, three different answers, from one unambiguous price series. **This is
`C-001`'s problem restated, not a resolution of it.** C-001 is precisely the dispute over
whether the quantity is 2.5, 3 or 4 days; a week that lands on exactly 72 hours can be
read into or out of the doctrine depending on a convention **the course has never
stated**.

**And the deeper blocker stands.** Choosing Monday's high as "the level" is *my* choice.
`A-004` records that the instructor's "level" is an **ordinal leg**, not a price line, and
he never says the level is the prior swing high. So this test measures a level I selected,
against a day-count convention I selected. Neither selection is sourced.

```text
EFFECT ON C-001: NONE. Does not resolve, does not refute.
n = 1 week, on a substituted 2026 week, against a self-selected level.
Recorded so the datum is not lost, and explicitly NOT counted as support.
```

This is recorded against `C-001` in `11_CONTRADICTIONS/CONTRADICTIONS.md` under the same
non-resolving framing. **No day-count value is committed anywhere as a result of this
homework**, which is the condition C-001 has carried since V01.

**What the week does establish, weakly:** that this test becomes performable the moment
`A-004` settles what "the level" is. ~~The measurement pipeline in §1.1 is reusable~~, and
`18_REVIEW/V02/V02_REVIEW_R1.md` notes this should become the first datum of the manual
backtest (dimension G) once that ambiguity resolves.

> **AMENDED 2026-08-10 (R2 Minor 1) — the reusability claim was overstated.** §1.1's
> *price* measurement (colour-exact candle detection, axis calibration, 6-px bar lattice,
> `±0.5 pip`) is verified and is reusable. §1.1's **day-boundary derivation was not**: it
> placed one bar on the wrong side of the Fri 31 Jul → Sun 2 Aug weekend boundary and used
> an open = prior-close continuity check at the one boundary where continuity does not
> apply. Both are corrected in §1.1, and the correction is what makes the boundary method
> reusable: **read the chart's own dotted day separators**, and treat continuity as a
> within-session check only.
>
> So §1.1 is **not** a fully general, self-validating measurement pipeline, and it should
> not be described as one. It is a documented method for this chart, whose price half is
> verified and whose boundary half now rests on the separators rather than on inference.
> Anything reusing it for dimension G must re-derive boundaries from the separators of
> **that** chart, and must not expect continuity across a weekend or a session gap.

---

## 1.4 HONEST SELF-ASSESSMENT OF 11a (post-correction)

```text
FIRST PASS: INVALID — misread the chart (R1 MAJOR 1). Retained, superseded.
SECOND PASS: prices/dates/directions MEASURED and reproducible (§1.1).
             LABELS still unverified — no answer key exists for this week.
DIMENSION B (Recognition): FAIL — unchanged.
```

The correction fixes **what the chart did**, not **whether my labels are the right
labels**. Those are two different claims and only the first is now evidenced:

- The measured OHLC in §1.1 is reproducible from the committed PNG. ~~and self-validates
  (open = prior close on all six day boundaries).~~ **CORRECTED (R2 Minor 1):** it does
  **not** self-validate on all six day boundaries. Open = prior close holds on 174 of the
  176 bar boundaries and is a valid *within-session* check, but it cannot validate the
  Fri→Sun weekend boundary, where the real −12.6 pip gap belongs. The day boundaries are
  established instead by the chart's own dotted separators.
- The *labels* in §1.2 — `PFH`, `Level 1/2/3`, `Reverse` — remain plausible imitations of
  a worked example. **It has not been checked against any answer key**, because none
  exists for this week. Row 6 is now explicitly flagged as unsupportable.

I am **not** claiming this demonstrates recognition ability, and the correction makes that
more clearly true rather than less. Per `MASTERY_STANDARD.md` §B, recognition means
identifying taught concepts on charts *not used in the lesson* — this is such a chart, but
with no ground truth the exercise demonstrates only that I can apply the vocabulary. The
first pass showed I applied it to the wrong prices; the second pass shows the right
prices, and still cannot show the labels are right.

**The lesson I take from the MAJOR finding**, recorded because it is the transferable
part: the source-reading in this project was held to a citation standard (every claim to a
timestamp, verified) and the chart-reading was not held to any standard at all. Prices
were eyeballed off axis ticks and written down as though measured. A chart is a source
document, and reading one needs the same discipline as reading a transcript.

---

## 2. ASSIGNMENT 11b — 40 FLASHCARDS — NOT COMPLETED

Printed instruction, from `04_SCREENSHOTS/V02/V02_00-55-35_rd-assignment-40-flashcards.png`:

```text
R & D assignment  Cycle 1 Week 1
Map out last weeks  Usd/Chf
Develop 40 flash cards
4 Majors: EUR/USD, GBP/USD, USD/CHF, USD/JPY
5Ms
5Ws
Out of the 40, Pick one perfect M and W (only 1)
Label it post it for review in the forum
```

**Data is not the blocker.** All four majors were captured and are in `charts/`; the
free tier reaches back to **early January 2025** on the 1H chart (see §0 and the
reconciliation note there) — far more than enough to find forty formations.

> **CORRECTED 2026-08-10 (R1 finding 6).** This sentence previously read *"the free tier
> gives ~7 months of 1H history per pair"*, which contradicted §0's own statement that
> 1H history reaches back to 6 January 2025. The `~7 months` figure had no source and is
> withdrawn; the observed reach from the evidence screenshot is used instead.

**The blocker is that the course has not defined what an M or a W is.**

- `A-011` — "M and W formation" — is logged as **Foundational, `DO NOT CODE`**, first
  seen V01 `[00:17:45]`, used throughout both lessons and described in neither.
- V02 adds `A-007` — "second leg" — also Foundational and also undefined, and the M/W
  legs are precisely what a second leg would be counted against.
- The assignment does not ask for forty *examples*; it asks for **five M's and five W's
  per pair**, and then for the **one perfect M and one perfect W**. "Perfect" is a
  quality judgement against a standard that has not been issued.

To produce forty cards I would have to invent the anatomy — how many touches, what leg
symmetry, what depth of retracement, what makes one "perfect" — and then present my
invention as coursework. That is the exact failure mode that put 63 files in quarantine
(`QUARANTINE_REGISTER.md` Q-001, Q-002): plausible domain knowledge formatted as though
it were sourced.

```text
DEFERRED — blocked on A-011 and A-007, not on infrastructure
```

Per `D-019`, `DEFERRED` is the correct disposition and not `NOT APPLICABLE`: there is
real subject matter here and the work is performable **once the course defines the
formation**. It stays open and is carried in `18_REVIEW/REVIEW_INDEX.md`.

**Recommended trigger to unblock:** the first lesson that describes M/W anatomy — V02
`[00:45:39]` promises "I will draw this for you next week", so **V03 should be checked
for it deliberately.** At that point this assignment becomes performable and the charts
already captured can be reused.

### What was done toward 11b

The four majors were captured on the 1H timeframe so the data side is ready and the
account gate is documented:

| Pair | File |
|---|---|
| USD/CHF | `charts/USDCHF_1H_2026-08-10_tradingview-fxcm.png` |
| EUR/USD | `charts/EURUSD_1H_2026-08-10_tradingview-fxcm.png` |
| GBP/USD | `charts/GBPUSD_1H_2026-08-10_tradingview-fxcm.png` |
| USD/JPY | `charts/USDJPY_1H_2026-08-10_tradingview-fxcm.png` |

---

## 3. ITEMS THAT ARE GENUINELY NOT APPLICABLE

| Item | Timestamp | Disposition | Why |
|---|---|---|---|
| Post the marked-up chart under "homework" in the 2012 forum | `[00:56:08]`, `[00:54:44]` | `NOT APPLICABLE` | The forum is a 2012 private members' site. No present-day agent can post to it. Matches D-018's eligibility test. |
| Collect the answer key the instructor said he would post | `[00:54:44]` | `NOT APPLICABLE` | Same reason. This is the reason 11a cannot be graded. |
| "Email me the surveys only" | `[00:54:51]` | `NOT APPLICABLE` | 2012 email address; and the survey belongs to V01. |
| Download the student folder / template | `[00:47:51]` | `NOT APPLICABLE` | He explicitly takes it offline in this very lesson — "don't download anything until I get it straight". |

---

## 4. SUMMARY

| Assignment | Status | Blocker |
|---|---|---|
| 11a — label the weekly cycle, USD/CHF 1H | **Redone from measurement after R1 MAJOR 1.** Prices/dates/directions now measured and reproducible (§1.1–§1.2); invalid first pass preserved in place. **Labels still unverified** | Answer key does not exist; 2012 data account-gated. Label correctness remains unverifiable for any week |
| 11b — 40 flashcards | **DEFERRED** | A-011 (M/W undefined), A-007 (second leg undefined) |
| Forum posting / answer key / survey / student folder | `NOT APPLICABLE` | 2012 infrastructure |
