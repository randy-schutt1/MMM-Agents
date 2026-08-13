# PT-032 — The weekend gap, and the one mechanical rationale in V01 (RE-ISSUE of PT-019)

```text
STATUS:      PRE-REGISTERED — NOT YET RUN
WRITTEN:     2026-08-13
RE-ISSUES:   PT-019, which is NON-CONFORMING under D-035 (its window W-C straddles the
             pinned DEVELOPMENT/HOLDOUT boundary by 546 days). PT-019 is RETAINED, NOT
             DELETED, NEVER RUN, and is not edited into conformance — only its status
             block is added, per D-027 and the PT-022 precedent.
LESSON:      V01 [00:48:58]-[00:49:44], [00:49:12], [00:50:17]; V02 [00:05:24]
ATTESTATION: No chart, no price series and no outcome data of any kind — in W-C′ or in
             any other window — was opened, loaded, parsed or inspected by the session
             that wrote this file. The HistData corpus was cited from its committed
             provenance (SHA256SUMS.txt) and its QA report; not one quote was read from
             it. The D-035 holdout (2016-07-01 → 2017-12-29) was not opened, and per
             D-036a it is not on disk.
NOTE:        THE ORIGINAL'S PRIMARY CONTROL DOES NOT SURVIVE THE VENDOR CHANGE INTACT.
             This corpus trades continuously through the week, so "intra-week daily
             boundary GAPS" are not gaps. See 0c. The control is retained, relabelled,
             and its meaning restated — not quietly reinterpreted.
```

Shared machinery: `COMMON_PROTOCOL.md`. Standard: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`.
Decisions: `D-007` · `D-026`/`D-029` · `D-027`/`D-028` · **`D-030`** · **`D-031`** ·
`D-034` → **`D-036`/`D-036a`** · **`D-035`**.

---

## 0. WHY THIS FILE EXISTS, AND WHAT THE SUBSTITUTIONS COST

`D-035` pins **DEVELOPMENT = 2013-01-06 → 2016-06-30**, **HOLDOUT = 2016-07-01 → 2017-12-29**.
`PT-019`'s window `W-C` runs to 2017-12-29 and **straddles the boundary by 546 days**.
`COMMON_PROTOCOL.md` §3a and `D-027` require re-issue under a new `PT` number; the original is
**retained and marked, never edited**.

| Field | `PT-019` | **PT-032** | Cost, stated now |
|---|---|---|---|
| Window | `W-C` 2013-01-06 → **2017-12-29** | **`W-C′` 2013-01-06 → 2016-06-30** | 260 weekends → **180 usable** (§3a–§3a‴) |
| Block | `PROVISIONAL DEVELOPMENT pending D-028` | **DEVELOPMENT — confirmed against `D-035`** | none; this is the gain |
| Data source | TradingView / FXCM (`D-034`) | **HistData GBP/USD M1 CSV corpus** (`D-036a`) | **levels no longer comparable**; **bid-only, no spread → the measured gap is a LOWER BOUND** — §0b |
| **Week open** | FXCM **21:00 UTC** | **22:00 UTC** (Sunday 17:00, fixed UTC−5, no DST) | **this test is *entirely* about that instant**, so the change is total, not incidental |
| Measure 4's control | *"intra-week daily-boundary gaps"* | **relabelled** — §0c | the control survives; **the word "gap" does not** |
| Everything else | — | **unchanged** — question, five measures, nulls, seed, scope | — |

### 0a. Three losses that are not negotiable

1. **Price levels do not travel.** FXCM serves no 2013–2016 GBP/USD, so `D-034`'s cross-vendor
   offset cannot be measured here. **Levels are not comparable with the V02–V06 FXCM homework;
   only shape and distance claims travel** (`D-036a`). **A gap is a difference of two prices from
   the same file, so it is a distance and it travels** — this test is well matched to the
   corpus's limitation.
2. **The October 2016 flash crash is in HOLDOUT and unavailable to the Student Phase at all.**
   It was not a weekend gap, but it is the era's canonical evidence that GBP/USD can move faster
   than a stop can bound. Its absence limits what the **tail** of this distribution can be said
   to represent. Stated in the report.
3. **The EU referendum (2016-06-23, a Thursday) is inside `W-C′` and inside DEVELOPMENT.** The
   **weekend gap into Sunday 2016-06-26** is therefore inside the window — and that week is
   truncated by the DEVELOPMENT boundary, which affects the *following* week, not the gap
   itself. **The gap is retained and not excluded** (`E09`), and it is stated **now** that it is
   very likely to be the largest in the sample, so that cannot later be presented as a discovery.
   **The five largest gaps are reported as the pre-registered sensitivity appendix and are
   retained in the headline distribution.**

### 0b. Bid-only data makes every number here a LOWER BOUND on execution risk

The corpus is **bid-only M1 bars, no spread, volume structurally zero** (`D-036a`). The Sunday
reopen is precisely where a real spread is widest. So:

> **The measured weekend gap is a bid-to-bid difference. A position carried through the weekend
> would be closed against a spread that is not in this data. Every gap figure in this test is
> therefore a LOWER BOUND on the true execution gap, and is labelled as one.**

**This runs *in favour* of the instructor's rationale**, which is exactly why it must be stated
before the result: a test whose measurement error points one way must declare the direction in
advance, or a confirmation is unreadable. Inventing a spread would be `D-030`'s exact
prohibition.

### 0c. THE CONTROL THAT HAD TO BE RELABELLED — AND WHY IT IS NOT QUIETLY REINTERPRETED

`PT-019` Measure 4 compared the weekend gap against **"intra-week daily-boundary gaps at the
same clock instant on Mon–Thu"**. That comparison assumed a feed with a **daily break** at the
5pm boundary.

**This corpus has no daily break.** QA `C6` finds **three** intra-week gaps ≥ 30 minutes in
3.5 years, **4h43m in total** — the week is otherwise continuous from Sunday 17:00 to Friday
17:00. So on Mon–Thu at 17:00 there is **no gap at all**: consecutive bars simply abut.

**Pre-registered handling, fixed now:**

- The control is **retained**, because what it holds constant — *the same clock instant, the same
  instrument, only the calendar position changes* — is still exactly right.
- It is **relabelled** to what it actually measures: **the bar-to-bar price change across the
  17:00 instant on Monday–Thursday**, i.e. a **continuous-trading return over one 15-minute
  boundary**, not a gap.
- **The asymmetry is declared, not hidden.** Comparing a discontinuous weekend jump against a
  continuous weekday return is **not** an apples-to-apples null; it is a **floor**. It answers
  *"is the weekend jump bigger than an ordinary move at the same clock time?"* and it does
  **not** answer *"is the weekend jump bigger than other gaps?"*, because **this corpus contains
  almost no other gaps to compare against.**
- **Therefore the second baseline (N3, the shifted-week sanity control) is promoted from sanity
  check to co-primary**, since it is now the only control that can distinguish a harvest defect
  from a real discontinuity.
- QA `C6`'s three real intra-week gaps are **reported individually** — three observations is
  **far below any inferential floor** and they are `DESCRIPTIVE ONLY`, listed for completeness
  rather than compared.

**This is a disclosure, not a repair.** A different vendor with a genuine daily break would
restore the original control, and that is recorded here so a future session re-runs it rather
than inheriting this substitute.

---

## 1. WHY THIS TEST IS WORTH RUNNING

*"Don't carry trades through on Friday"* is the **only** instruction in V01 whose rationale is
**mechanical rather than pattern-based** — `V01_INTERPRETATION.md` §7 `M5` singles it out for
exactly that, and then refuses to code it because he gives no time, no session and no exception
handling. V02 restates the instruction flatly: *"You always get out on Friday, my friend,
always"* `[00:05:24]`.

The rationale is a claim about **execution**, not about the dealer: a position held over the
weekend is filled at the first available price on the Sunday open, so the weekend gap is a risk
that no stop can bound.

That is measurable directly and it is the last piece of V01 that has never been checked. It is
also the one test in this batch whose result is **actionable regardless of whether the Market
Maker Method works at all** — the gap distribution of GBP/USD is a fact about the instrument,
and it will still be true if every other test in this batch returns null.

---

## 2. THE QUESTION

> How large is the GBP/USD weekend gap, how often does it exceed the stop distances this course
> teaches, and does it exceed the largest ordinary move at the same clock instant within the
> week?

Null hypothesis: **the weekend gap is not distinguishable** from the price change observed at
other daily boundaries within the week.

## 3. PRE-REGISTRATION — FIXED BEFORE ANY BAR IN `W-C′` WAS READ

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Timeframe | 15-minute |
| **Window** | **`W-C′` — 2013-01-06 → 2016-06-30** |
| **Block (data split)** | **DEVELOPMENT, confirmed.** `W-C′` **is** `D-035`'s DEVELOPMENT block |
| **Data source** | **HistData GBP/USD M1 CSV corpus** (`D-036a`), `datasets/HISTDATA_GBPUSD_M1/`, SHA-256 in `raw/SHA256SUMS.txt`; aggregated by `scripts/aggregate_m15.py` per `D-031` arm |
| **Week open** | **22:00 UTC — Sunday 17:00, fixed UTC−5, no DST** (`D-036a`, QA `C7`: 187 opens, 172 at exactly 17:00, the remainder 17:01–17:10, modal 17:00 in all twelve months). **NOT FXCM's 21:00 UTC.** **Late opens are real and are read per week from timestamps, never assumed** |
| **Week close** | **A RUN-TIME FACT, read from timestamps.** `D-036a` documents the week *open* and not the week *close*. **No session may assume Friday 17:00.** The realised last-bar timestamp of each trading week is recorded per week as a first-class parameter |
| **Data-QA gate** | **Precondition.** `scripts/qa_histdata_m1.py`; `QA_REPORT.txt`; `C1`–`C4` PASS, `C5`–`C8` signed off in `D-036a`. **`C6`'s gap census is cited directly by §0c** |
| Measurement rule | `E06` restated for a CSV corpus (`COMMON_PROTOCOL.md` §2) |
| Timezone | **Both `D-031` arms.** Arm A = corpus stamps verbatim; Arm B = +1h during US DST |
| Gap definition | `open(first bar of the new trading week) − close(last bar of the previous week)`, in pips, **signed and absolute**. **Boundaries by timestamp lookup, never by bar count.** **Bid-to-bid, no spread → a lower bound** (§0b) |
| Measure 1 | Distribution of absolute gap size; **median, 90th, 99th percentile, maximum** |
| Measure 2 | **Share of weekends whose gap exceeds 10, 15, 18 and 50 pips** — the instructor's own stop and target numbers (V04 `[00:04:43]`, `[00:05:07]`), so the risk is expressed in the units the course uses. **These are distances and they travel across vendors** |
| Measure 3 | **Gap fill:** share of gaps closed within 4 h, 24 h and by the week's end, with time-to-fill |
| Measure 4 | Comparison against the **bar-to-bar change across the 17:00 instant on Mon–Thu** — **relabelled per §0c; it is not a gap** |
| Measure 5 | **Directional test:** is the gap's sign related to the **prior Friday's** direction? A *"the dealer squares his books"* reading predicts a relationship; **no relationship is the null** |
| Excluded weekends | **None.** Holiday weekends are retained and reported separately |
| Decision point | **Friday close.** Everything after is outcome |
| **Sample** | **180 weekend gaps** — denominated in **trading weeks present in the corpus with an observable week open**, not calendar weeks. See §3a–§3a‴; the **2014-06-02** "gap" is **excluded by name** because ~22 hours of data are missing across it |

### 3a. The sample, computed honestly

`W-C′` contains **182 calendar Sundays** (2013-01-06 … 2016-06-26) but only **181 observable
Sunday week opens** — see §3a′. A weekend gap needs **both** a preceding Friday close inside the
window **and** an observable week open:

- The gap into **2013-01-06** would need the close of **2013-01-04**, which lies **inside the
  corpus but outside `W-C′`**. **Excluded** — using it would silently widen the pre-registered
  window, which `D-027` forbids. **Counted and reported.**
- **The gap into 2014-06-02 is EXCLUDED BY NAME — see §3a″. It does not exist; measuring it
  would fabricate a ~22-hour gap out of missing data.**
- Every remaining week-open has its preceding Friday inside the window. **The gap into
  2016-06-26 is measurable and is retained**, even though that week is itself truncated by the
  DEVELOPMENT boundary — the gap is fully determined by data before the boundary.

### 3a′. THE WEEK CENSUS — CALENDAR WEEKS ARE NOT TRADING WEEKS

**The first draft of this file counted calendar Sundays and called them week opens. That was
wrong, and this test is the one where that error would have produced a fabricated number rather
than merely a mislabelled one.** Against the corpus's own census (QA `C7`, `C8`):

| Quantity | Count | Source |
|---|---|---|
| Calendar Sundays in `W-C′` (2013-01-06 … 2016-06-26) | **182** | calendar arithmetic |
| **Week opens the corpus actually contains in `W-C′`** | **186** | `C7` (187 corpus-wide, less the Tue 2013-01-01 corpus start) |
| — opening on a **Sunday** | **181** | `C7` |
| — opening on another weekday | **5** | `C7` |
| — of the 187 corpus-wide, **late opens (17:01–17:10)** | **15** | `C7` |
| **Weeks with an observable Sunday week open** | **181** | 182 calendar Sundays, less **2014-06-01**, which has none |

**Two facts a naive reading of `C7` gets backwards, and for this test both are fatal:**

1. **Four of the five irregular opens are NOT week starts.** `C7`'s detector emits the first bar
   after any gap ≥ 12 h — and it **cannot distinguish a weekend from a holiday closure from a
   missing session by duration alone**. `2013-12-26 Thu`, `2014-01-01 Wed`, `2014-12-25 Thu` and
   `2015-01-01 Thu` sit **inside** weeks that opened normally on Sunday. **A run session taking
   its "weekend gaps" from `C7`'s open list would report four extra "weekend gaps" that are
   actually mid-week holiday re-opens** — which is precisely the class of fabricated observation
   this test exists to avoid producing. Pre-registered: **a weekend gap is measured only across a
   Sunday week open; an intra-week holiday re-open is never a weekend gap.** The four re-opens
   **are** reported, separately and by name, as **holiday-closure re-open moves** — a distinct,
   interesting quantity, and never merged into Measure 1's distribution.
2. **The fifth, `2014-06-02 Mon 15:01`, IS a week start — and it is a data defect.** The corpus
   holds **zero bars** for `2014-06-01 Sun` (nominal ~420) and **521 of 1,440** for
   `2014-06-02 Mon`: **~22 continuous hours missing**. `C8` marks it
   `*** ABSENT AND UNEXPLAINED ***`.

### 3a″. THE 2014-05-30 → 2014-06-02 "GAP" IS FABRICATED, AND IS EXCLUDED BY NAME

**This is the single most consequential correction in this file.** The gap definition is
`open(first bar of the new trading week) − close(last bar of the previous week)`. Applied
mechanically across the hole:

```text
close(last bar of week ending Fri 2014-05-30)   ->   open(first bar seen, Mon 2014-06-02 15:01)
                    ~22 hours of MISSING DATA sit between them
```

A price change accumulated over **~22 hours of trading that the corpus does not contain** would
be recorded as a **weekend gap**. It would be **large**, it would land in Measure 1's tail and
Measure 2's `> 50 pip` bucket, it would very likely appear in the **five-largest-gaps sensitivity
appendix**, and **it would be an artifact of absent data, not of a weekend.** On a test whose
entire finding is *"how large is the weekend gap, and does it exceed the stops this course
teaches"*, that single fabricated observation could move the headline.

**Disposition: EXCLUDED BY NAME, counted, and reported as an exclusion in the observation.**

**Why this is not `E09`.** `E09` forbids excluding an observation because of **what the market
did** — because it was a news day, an outlier, "not representative". This is excluded because
**the corpus does not contain what the market did**. The distinction is the whole reason `C8`
was written, and it is stated here so that no later reader mistakes a data-integrity exclusion
for a convenience one. **Every other weekend in `W-C′` is retained, including the largest.**

### 3a‴. `C8` DISPOSITIONS — PRE-REGISTERED, BY NAME

Eleven `C8`-flagged sessions fall into **seven weeks** inside `W-C′`. The disposition is **not
uniform**, and for this test the holiday weeks are **more** interesting than average, not less:

| Week (Sunday) | `C8`-flagged sessions | Kind | **Disposition for this test** |
|---|---|---|---|
| 2013-12-22 | Wed 2013-12-25 (0) | market closure | **INCLUDE** the weekend gap into it; **report separately** the mid-week re-open move |
| 2013-12-29 | Wed 2014-01-01 (392) | market closure | **INCLUDE**; re-open move reported separately |
| **2014-06-01** | **Sun (0), Mon (521)** | **DATA DEFECT** | **EXCLUDE the weekend gap BY NAME (§3a″)**; also **exclude that week's four Mon–Thu 17:00 observations** from Measure 4 |
| 2014-12-21 | Wed 2014-12-24 (840), Thu 2014-12-25 (360) | market closure | **INCLUDE**; re-open move reported separately |
| 2014-12-28 | Thu 2015-01-01 (424) | market closure | **INCLUDE**; re-open move reported separately |
| 2015-12-20 | Thu 2015-12-24 (840), Fri 2015-12-25 (0) | market closure | **INCLUDE** — **but the week ends THURSDAY**, so the gap *out of* it spans **Thu → Sun ≈ 75 h**, not ≈ 48 h. **A REAL extended closure, retained, and flagged with its realised duration** |
| 2015-12-27 | Fri 2016-01-01 (0) | market closure | **INCLUDE** — **week ends Thursday**; same extended-closure flag |

*(The eleventh, `2013-01-01 Tue`, lies **outside** `W-C′`. Not applicable.)*

**The two extended closures are the interesting case, and they are the opposite of the hole.**
`2015-12-25` and `2016-01-01` are **genuinely absent from the market**, not from the corpus. A
75-hour closure gap is exactly what V01's rationale is about — *a position held over a closure is
filled at the first available price* — so excluding them would remove the strongest real evidence
in the sample. **They are retained, and reported with their realised closure duration in hours
beside the pip figure**, because a 75-hour gap and a 48-hour gap are not the same event and a
distribution that silently mixes them is misleading.

**Why the six holiday weeks are INCLUDED.** `PT-019` pre-registered *"Excluded weekends: **None.**
Holiday weekends are retained and reported separately"*, and `COMMON_PROTOCOL.md` §3 disclosure 1
forbids dropping an observation for being unrepresentative (`E09`). **Re-deciding that now, after
a QA check surfaced them, would be the suit-the-result choice the gate exists to prevent.**

**The honest sample:**

| Quantity | `W-C` (original) | **`W-C′` (this file)** |
|---|---|---|
| Calendar span, inclusive | 1,819 days | **1,272 days** |
| Calendar Sundays | 260 | **182** |
| **Observable Sunday week opens** | 260 | **181** |
| **Weekend gaps USED (Measures 1, 2, 3, 5)** | 260 | **180** — less the 2013-01-06 lag and the 2014-06-02 fabrication (§3a, §3a″) |
| — of which **extended closures ≥ 72 h** | — | **2, retained and flagged** (§3a‴) |
| **Mon–Thu 17:00 boundary observations (Measure 4)** | 1,040 | **720** (180 usable complete weeks × 4), **plus up to 4** from the truncated final week (2016-06-26), whose Mon–Thu 17:00 instants all fall inside DEVELOPMENT — **counted at run time**. Any instant not bracketed by a bar within 15 minutes on each side is **excluded, counted and listed by date**; the six holiday weeks are expected to supply most of these, giving a **floor of ≈ 714** |
| Holiday-closure re-open moves, reported separately | — | **4** (§3a′.1) |
| Real intra-week gaps ≥ 30 m in the corpus (§0c) | — | **3 — descriptive only** |

**`n = 180` clears `BACKTEST_EVIDENCE_STANDARD.md` §4.1's floor of 30 by a factor of six for
Measures 1, 2, 3 and 5, and `n ≈ 720` does so for Measure 4.** Both are denominated in **trading
weeks present in the corpus with an observable week open**, never in calendar weeks.

**Where it thins, pre-registered rather than discovered:**

- **Measure 2's upper thresholds are counts of a tail.** A "> 50 pips" bucket at n = 180 may
  contain very few weekends. **The share is reportable** (a proportion over 180), **but any
  statement about what those weekends were like — their fill time, their direction, their prior
  Friday — is computed on that subset and carries `SAMPLE INSUFFICIENT FOR INFERENCE —
  descriptive only` in the same sentence** if it is under 30. The 10- and 15-pip thresholds are
  not expected to have this problem; the 18- and 50-pip ones might. **Fixed here so it cannot be
  renegotiated at run time.**
- **Measure 1's 99th percentile at n = 180 is an order statistic over roughly two observations.**
  It is reported **as a raw ordered list of the top five gaps** alongside the percentile, never as
  a percentile alone. At `W-C`'s 260 it would have been ~3 observations — **thin there too; this
  is a property of weekly data, not of the re-issue.**
- **Measure 5 splits 180 gaps by prior-Friday direction into two cells (~90 each) and by gap sign
  into four (~45 each).** Above the floor, but **report the four cell counts beside the four cell
  rates**.
- The original claimed *"~260 weekends. ≥ 30 satisfied"*. **That is now 180 and the caveats above
  are new — a consequence of an honest window and an honest corpus, not of a weaker test.**

**No boundary instant may be assumed.** The run session **reads the week roster and every
realised open and close from timestamps** and records them: **15 of the corpus's 187 opens are
late (17:01–17:10)**, and `D-036a` documents the week *open* but **not** the week *close*, so the
Friday close is a run-time fact. **For this test in particular the whole measurement is those two
instants.**

> **`C8` DID NOT EXIST WHEN THIS FILE WAS FIRST WRITTEN, AND THIS FILE IS THE REASON THAT
> MATTERS MOST.** The session-completeness check was added to
> `06_MANUAL_BACKTEST/scripts/qa_histdata_m1.py` **after** this pre-registration was drafted. It
> is what surfaced the 2014-06-01 hole — which `C6` had excluded **by construction** (its gap
> census skips anything ≥ 12 h as "the weekend", and **a missing session is indistinguishable
> from a weekend by duration alone**) and `C7` had rendered cosmetic (a decorative **Monday**
> entry in a weekday tally). **A weekend-gap test whose data check treats missing sessions as
> weekends is exactly the test that will fabricate a weekend gap.** §3a′, §3a″, §3a‴ and the
> corrected counts above are the **correction that check forced**, made **before any bar in
> `W-C′` was read**.

## 4. BASELINE

| Arm | Null |
|---|---|
| **Co-primary — the natural control** | Measure 4's Mon–Thu 17:00 boundary changes. Same instrument, same clock, same measurement; **only the calendar position changes**. **Relabelled per §0c: on this corpus these are continuous-trading returns, so this control is a FLOOR, not a matched comparator** |
| **Co-primary — promoted** | **N3 — week-anchor shift**, 1,000 draws, seed `20260812`: "gaps" computed at **shifted** week boundaries, most of which fall inside continuous trading and should therefore be **near zero**. **A non-zero result here means the harvest is wrong and no other number in the test can be trusted.** §0c promotes this from sanity check to co-primary, because it is now the only control that separates a real discontinuity from a defect |

Baselines are run **before** the observed gap distribution is read. **N3 is run first of all**
(§7 step 5).

## 5. WHAT EACH OUTCOME MEANS

| Result | Reading |
|---|---|
| A material share of weekend gaps exceed 18 pips | **The instructor's rationale holds on its own terms**: an 18-pip stop cannot bound weekend risk, and the Friday-flat instruction is justified mechanically rather than doctrinally. The clearest supportable instruction in V01. **State that §0b makes this a lower bound, so the true case is at least this strong** |
| Gaps are almost always small | The rationale is weak on this instrument in this era. Report prominently. The instruction may still be right for other reasons; **this test speaks only to the stated one** — and even here §0b's missing spread means the executed cost was larger than measured |
| Gaps fill quickly and consistently | Interesting and **must not be turned into a strategy here.** A gap-fill edge is not in this course; recording one as if it were would be `E02` and `D-030` at once |
| Measure 5 shows a directional relationship | A genuinely new observation. Record as such — **an observation, not a rule**, and **not attributed to the instructor**, who says nothing about gap direction |
| N3 returns non-zero "gaps" at shifted boundaries | **Not a finding — a defect.** Stop, fix the harvest, and record that the run was restarted |
| Arms A and B diverge | Report both. Under Arm B the week open moves to local 18:00 during US DST, so the **gap is measured across a different instant** in summer weeks; state how much of any divergence is that |

## 6. MANDATORY SCOPE STATEMENT

> **PT-032 measures the GBP/USD weekend gap.** It tests the **stated rationale** for the
> Friday-flat instruction, **not the instruction itself** — the instruction names no time, no
> session and no exception, so there is no rule with parameters to apply
> (`V01_INTERPRETATION.md` §7 `M5`). **No gap-fill trading rule may be derived from this test.**
>
> It **re-issues `PT-019`** onto `W-C′` under `D-035`; `PT-019` is retained, marked and never
> run, and no result here may be reported as `PT-019`'s result.
>
> **Every gap figure is bid-to-bid with no spread and is a LOWER BOUND on execution risk**
> (§0b). **Measure 4 is not a gap comparison on this corpus** and is labelled accordingly
> (§0c). **Price levels are not comparable with the V02–V06 FXCM homework** (`D-036a`); the
> **distances** reported here do travel. The **week open is 22:00 UTC**, not FXCM's 21:00 UTC.

## 7. TO RUN THIS

1. **Run the QA gate first**; confirm `C1`–`C4` PASS; cite `QA_REPORT.txt` **and quote `C6`'s
   three-gap census**, which §0c depends on.
2. Build **both** `D-031` arms with `aggregate_m15.py`; record row counts and spans.
3. Confirm the window is `2013-01-06 → 2016-06-30`, wholly inside DEVELOPMENT. **Read nothing
   past 2016-06-30.** Record which `D-031` clock the boundary was applied in (`I-010` Q2, OPEN).
4. **Record the feed's realised week-open AND week-close timestamps for every week** — this test
   is *entirely* about those two instants. **Do not assume 17:00 for either**; 15 of the corpus's
   187 opens are late, and the week *close* is documented nowhere. **Never take the open list
   from `C7`** (§3a′.1). **Apply and count every exclusion by name: the 2013-01-06 lag gap (§3a),
   the 2014-06-02 fabricated gap and that week's four Measure-4 instants (§3a″, §3a‴).** Report
   the four holiday re-open moves separately, and flag the **two ≥ 72 h extended closures**
   (2015-12-25, 2016-01-01) with their realised duration.
5. **Run the shifted-boundary sanity control (N3) FIRST.** A non-zero result there means the
   harvest is wrong and no other number in the test can be trusted.
6. Compute Measure 4's Mon–Thu 17:00 boundary changes **before** the weekend distribution.
7. Report the **five largest gaps** as the pre-registered sensitivity appendix, **retained in the
   headline distribution**. Report the top-five ordered list beside the 99th percentile (§3a).
8. Report **both `D-031` arms** and label every figure a **lower bound** (§0b).
9. Write `BT_V01_NNNN.md` from the template, §0 referencing **this file and `PT-019`**.
10. **Neither this file nor `PT-019` is ever edited to match what was found.**
