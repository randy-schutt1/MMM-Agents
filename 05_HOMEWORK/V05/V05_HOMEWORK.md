# V05 — HOMEWORK

| Field | Value |
|---|---|
| Video ID | V05 |
| Assigned | `[00:04:34]`–`[00:05:22]` (the printed task list, frame `V05_00-04-35`), restated across `[00:10:07]`–`[00:17:25]` — **by a guest presenter, not the instructor** |
| Attempted | 2026-08-11 |
| Data source | TradingView, **FXCM** feed, 15-minute. **No login, no account, no paywalled feature, no CAPTCHA encountered or bypassed.** |
| Raw data | `data/v05_harvest_15m_full.json` — 687 timestamped bars per pair, 2026-07-31 → 2026-08-11 |
| Week slice | `data/v05_week_2026-08-02_15m.json` — 480/480/480/**476** bars |
| Charts | `charts/` — 12 images, **rendered from the committed JSON, not screenshots** |
| Scripts | `scripts/` — harvester, slicer, renderer; all three committed and re-runnable |
| Week analysed | **Sun 02 Aug 2026 21:00 UTC → Fri 07 Aug 2026 21:00 UTC** |

**Completed on real data. No substitution was needed.**

---

> ## ⚠ WHAT THIS HOMEWORK DELIBERATELY DOES NOT DO
>
> V05 is **100% guest-presented** (`V05_SOURCE_NOTES.md` header). Under `DECISIONS.md`
> **D-025** its **normative** content — entry criteria, level assignments, the anchor
> theory, the day-count expectation, targets, stops — is **excluded from doctrine** and may
> not be coded, backtested, or cited for or against an instructor rule.
>
> Its **descriptive** content — *how you operate the platform and lay a markup down* — is
> admissible. **That is the half this homework performs.**
>
> Concretely, the charts in `charts/` carry:
>
> | Marked | Why it is allowed |
> |---|---|
> | Day separators, at each day's **own first bar** | A fact read from the data's timestamps |
> | **Week high** and **week low**, with exact prices | **Instructor-sourced objects** — V04 `[00:18:24]` *"try to identify the high of the week and the low of the week"* |
> | Body-to-body boxes at those extremes, wicks left outside | The guest's stated **drawing convention**, `[00:56:11]`–`[00:56:27]` — a procedure, not a market claim |
> | Flashcard crops cut **at** the decision candle | The guest's stated **file convention**, `[00:31:04]` *"Everything past this candle is garbage. You cut it off right there"* |
>
> And they deliberately **omit**:
>
> | Not marked | Why |
> |---|---|
> | `Level 1` / `Level 2` / `Level 3` | Guest normative. Assigning levels applies the guest's cycle theory |
> | The `anchor` / `peak formation` | Same. `[00:10:26]`–`[00:10:45]` |
> | `D1 drop` / `D2 drop` / `D3 drop` as *cycle* labels | Same. The day separators here are calendar facts, and are labelled `D1…D6` by **date**, not by cycle position |
> | Any entry, stop or target | Guest normative, and `D-010`'s machine-rule firewall applies independently |
> | *"3 days of drop, expect a reversal"* | The single most normative claim in the lesson |
>
> **A homework artifact that marked levels and entries would look more like the lesson and
> would be wrong.** The exclusion is the assignment being done correctly, not skipped.

---

## 0. THE ASSIGNMENT, AS GIVEN

The lesson prints its own task list (frame `V05_00-04-35_slide-what-would-be-considered-rd.png`):

> *"First, YOU got to KNOW your platform."*
> *"You need to know how to add Indicators, Scripts, & Templates."*
> *"You need to know how to work the Toolbar."*
> *"You need to know how to use SCRIPTS and customize them to your settings using Meta Editor."*
> **"You need to know how to mark up your charts."**
> **"You need to know how to SAVE the mark ups."**
> **"You need to know how to make FLASH CARDS and have the Setups in-grained in your head."**

| # | Assignment | Performable? | Done |
|---|---|---|---|
| H1 | Add indicators/scripts/templates; work the toolbar; Meta Editor | **No** — MT4 with the course's own templates and scripts is not in this library | `DEFERRED` |
| H2 | **Mark up your charts** | **Yes** | ✅ §2 |
| H3 | **Save the markups** | **Yes** | ✅ §3 |
| H4 | **Make flashcards** | **Yes** | ✅ §4 |
| H5 | Mark the full market-maker cycle (anchor, days, levels, consolidation boxes) | **Partly** | ⚠ §2 — the mechanical half only; levels/anchor excluded under D-025 |
| H6 | Mark the patterns and entries inside the cycle | **Excluded** | ❌ Guest normative |
| H7 | *"going over your trades you have taken"* `[00:03:04]` | **No** — no trade history exists | `DEFERRED` |
| H8 | The DMR *"accountability factor"* — send your week to a coach `[00:03:33]` | **No** — 2012 programme, no coach | `NOT APPLICABLE` |

---

## 1. METHOD

### 1.1 No price is read from a pixel

Every number in this file is **TradingView's own Data Window text, read from the DOM.**
The chart is driven with synthetic mouse moves across the price pane; after each move the
Data Window panel is parsed for `Date`, `Time`, `Open`, `High`, `Low`, `Close`. That panel
is the platform's report of the hovered bar.

This is the V02 `MAJOR` (`E06`/`E19`) lesson applied — there a price line drawn in the same
colour as bullish candles corrupted a pixel-based read. **Nothing here depends on a colour.**

The twelve images in `charts/` are **rendered from the committed JSON**, not screenshots.
They exist to be looked at; **no measurement is taken from them.**

### 1.2 Every bar carries its own timestamp — and this is the V04 defect fixed at source

**This is the single methodological change from V04, and it was made because of that
lesson's review.** V04's two harvesters (`05_HOMEWORK/V04/scripts/harvest_*.mjs`) captured
`O H L C` only. With no timestamps, the week boundary had to be **inferred** from bar
cadence — a fixed sixteen 15m bars per 4h bar. Review R1 finding `M1` established that the
inference was wrong for USDCHF: its week opens with a **partial** 4h bar of twelve 15m
bars, so four previous-week bars were pushed onto the head of the committed slice.

`scripts/tv_harvest_v05.mjs` reads `Date` and `Time` alongside the OHLC. **The week and day
boundaries below are therefore looked up, not assumed**, and the same condition that broke
V04 silently is here reported by the tooling.

### 1.3 The live-edge artifact, and why trailing bars are dropped

Hovering past the last real bar makes TradingView report the still-forming bar's OHLC for
every projected future slot, producing trailing rows with **distinct timestamps and
identical OHLC**. `scripts/slice_week.py` drops the trailing run of identical quadruples
(687 → 677/682 bars). The committed week ends 2026-08-07, four days clear of the live edge,
so no analysed bar is affected either way. Disclosed because a reader diffing the two JSON
files will see the row-count difference.

---

## 2. RESULT — H2 / H5, THE MARKUP

### 2.1 The week, as the timestamps define it

| Pair | Week bars | First bar (UTC) | Last bar (UTC) | Continuity breaks |
|---|---|---|---|---|
| EURUSD | **480** | `2026-08-02 21:00` | `2026-08-07 20:45` | **0** |
| GBPUSD | **480** | `2026-08-02 21:00` | `2026-08-07 20:45` | **0** |
| USDJPY | **480** | `2026-08-02 21:00` | `2026-08-07 20:45` | **0** |
| USDCHF | **476** | `2026-08-02 22:00` | `2026-08-07 20:45` | **0** |

**Continuity test:** within a trading week each bar's open must equal the prior bar's close.
Over the committed slice — **1,916 bars, 1,912 transitions — the chain is 1,912/1,912
continuous, zero breaks, in all four pairs.** That is the evidence the slice is one
unbroken week containing no weekend, and `scripts/slice_week.py` recomputes it from the
committed JSON.

### 2.2 USDCHF opens an hour late — measured, not inferred

Bars per calendar day (UTC), counted from the bars' own timestamps:

| Pair | 08-02 | 08-03 | 08-04 | 08-05 | 08-06 | 08-07 | total |
|---|---|---|---|---|---|---|---|
| EURUSD | 12 | 96 | 96 | 96 | 96 | 84 | 480 |
| GBPUSD | 12 | 96 | 96 | 96 | 96 | 84 | 480 |
| USDJPY | 12 | 96 | 96 | 96 | 96 | 84 | 480 |
| **USDCHF** | **8** | 96 | 96 | 96 | 96 | 84 | **476** |

**USDCHF has no bars at all between 21:00 and 22:00 on Sunday 02 Aug on this feed**, while
the other three trade the full hour. Verified directly rather than assumed: the 20:00–23:00
window holds **9** bars for EURUSD, GBPUSD and USDJPY and **5** for USDCHF, and the last
bar before the week open is `2026-07-31 20:45` for all four, so nothing earlier is being
missed by the query.

**476 = 480 − 4**, and 4 × 15m is exactly the missing hour.

> **This independently reproduces V04 review R1's corrected figure.** V04's remediation
> concluded USDCHF's week is **476** 15-minute bars, `12 + 29 × 16`. A different session, a
> different harvester, a different week, and timestamps instead of cadence arrive at the
> same 476 — and here the *reason* is directly visible in the data rather than reconstructed.
> The condition is a property of the **feed's session open for this symbol**, not a one-off.

### 2.3 The extremes

Read from the Data Window text, not from the rendered images:

| Pair | Week high | at (UTC) | Week low | at (UTC) | Range |
|---|---|---|---|---|---|
| EURUSD | `1.15808` | `08-07 12:45` | `1.15003` | `08-03 15:30` | 80.5 pips |
| GBPUSD | `1.35089` | `08-07 13:15` | `1.34175` | `08-03 18:00` | 91.4 pips |
| USDJPY | `158.572` | `08-07 00:45` | `155.228` | `08-03 00:45` | 334.4 pips |
| USDCHF | `0.81356` | `08-06 15:45` | `0.80552` | **`08-02 22:00`** | 80.4 pips |

> ### ⚠ USDCHF's week low is boundary-limited and is flagged, not reported flat
>
> `0.80552` is the **open of USDCHF's very first available bar of the week.** Because that
> bar is 22:00 and the other three pairs open at 21:00, the low sits exactly on the edge of
> the data rather than inside it. **If USDCHF traded in the missing hour on any other feed,
> its true week low could be lower**, and nothing in this dataset can rule that out.
>
> **USDCHF is therefore excluded from any conclusion below that depends on the week low**,
> and the three-pair result is reported separately. This mirrors V04, where USDCHF was
> excluded from the scoped result on 4h grounds — the same symbol failing the same way for
> the same reason, which is why it is called out rather than smoothed over.
>
> The other three pairs' extremes sit **well inside** the week (Mon–Fri), so none of them
> is boundary-limited.

**Scoped result, 3 of 4 pairs (USDCHF excluded):** every week high falls on **Friday
07 Aug** and every week low on **Monday 03 Aug**. Stated as an observation about one week
in four instruments; **no rule is drawn from it**, and with n = 3 none could be.

### 2.4 What the charts show

`charts/<PAIR>_15m_week_marked.png` — the full week, 15-minute, with day separators at each
day's own first bar (labelled with that bar's actual open time, which is where USDCHF's
22:00 is visible), the week high and low as horizontal lines with exact prices, and
body-to-body boxes at both extremes with the wicks left outside.

The footer of every image states in the image itself: *"No Level/anchor/entry marked:
guest-normative, excluded under D-025."* — so a frame that escapes this directory still
carries its own provenance.

---

## 3. RESULT — H3, SAVING THE MARKUP

The guest's save procedure `[00:37:52]`–`[00:38:27]` is MT4-specific (right-click →
*Save As Picture* → *Active workspace* → name it → GIF). **The procedure is not
reproducible here** — this project has no MT4 — so what is performed is its *purpose*: a
named, dated, reproducible image artifact per pair, stored in `charts/`, regenerable from
committed data by `scripts/render_charts.py`.

**This is a substitution and is declared as one.** The guest saves a screenshot of his
terminal; this saves a render of the underlying data. The render is the stronger artifact
for a project that quarantined 72 files for unverifiable claims — it can be regenerated and
checked — but it is **not the same act**, and a reviewer should not read §3 as MT4's
procedure having been executed.

---

## 4. RESULT — H4, THE FLASHCARDS

The one flashcard rule V05 states is a **crop** rule, and it is stated twice:

> *"my flash card is going to be right up to this point right there"* `[00:21:02]`
> *"Everything past this candle is garbage. You cut it off right there, bam. You don't see
> any other stuff to the right of it."* `[00:31:04]`–`[00:31:08]`

Eight flashcards, two per pair, in `charts/<PAIR>_15m_flashcard_week-{high,low}.png`: the
same week, cut **at** the extreme candle, with nothing to its right. This is the lesson's
"hard right edge" made into a file — the card shows what was visible at the moment of
decision and withholds what came next.

**What these cards are not.** They are **not** setup cards. The guest's cards show *"the
Mona Lisa of the M & W pattern"* — an instance of a named setup. Naming a setup on these
charts would require the guest's pattern criteria, which are excluded. These demonstrate
the **construction convention** on instructor-sourced objects (the week's extremes), which
is the admissible part. **H4 is therefore performed in form and not in content**, and that
limit is the honest result, not a shortfall to be papered over.

---

## 5. WHAT THIS HOMEWORK ESTABLISHED

1. **The V04 harvesting defect is fixed at source.** Timestamped bars make week and day
   boundaries a lookup. The class of error behind review R1 `M1` cannot recur silently.
2. **USDCHF's late session open is a reproducible property of the feed**, independently
   reaching V04's corrected 476, with the cause visible rather than reconstructed.
3. **1,912/1,912 continuity** across four pairs — the cleanest week slice the project has
   committed.
4. **A worked demonstration of the D-025 boundary.** The markup separates cleanly into a
   descriptive half that can be performed and a normative half that cannot, and the
   artifacts show the line being held.

## 6. WHAT IT DID NOT, AND COULD NOT, ESTABLISH

- **Nothing about whether the method works.** No entry, no exit, no outcome. By design.
- **Nothing about the market-maker cycle.** Levels and the anchor are guest theory.
- **Nothing that touches `C-001`, `A-020` or `A-039`.**
- **A one-week, four-pair observation is not evidence of a pattern.** §2.3's Friday-high /
  Monday-low coincidence is recorded as an observation and is explicitly not a finding.
- **The MT4 half of the assignment (H1, and H3's actual procedure) remains unperformed**
  and is deferred, not quietly dropped.
