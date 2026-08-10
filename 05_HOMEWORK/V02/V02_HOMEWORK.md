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

Note that even the Premium tier's 20,000 hourly bars is ~2.3 years and would still not
reach 2012. This is an account/paid gate, not a navigation problem, and per the standing
instruction it is **flagged rather than worked around**. No account was created, no
credentials were entered, and no bot check was bypassed.

**Substitution made:** the same exercise, on the same instrument and timeframe, for the
most recent complete week — **Sunday 2 August to Friday 7 August 2026**. The exercise is
"label one week's cycle on the 1H chart"; its instructional value does not depend on
which week. What *is* lost is the ability to compare against the instructor's own answer
key, which he said he would post in the 2012 forum — that key is unavailable to this
project regardless of which week is used.

---

## 1. ASSIGNMENT 11a — LABEL THE WEEKLY CYCLE (USD/CHF, 1H)

**Chart:** `charts/USDCHF_1H_2026-08-10_tradingview-fxcm.png`
Week analysed: Sun 2 Aug – Fri 7 Aug 2026. Price levels are read off the chart's price
axis and are accurate to roughly ±5 pips; they are structural markers, not quotes.

### Why this is presented as a table rather than as drawings on the chart

The instructor's instruction is to mark up the chart and post the image. Drawing on
TradingView reliably requires a saved layout, which requires an account. Rather than
place boxes at coordinates estimated from axis ticks — the Sunday session is partial, so
the day-column boundaries cannot be pinned from the tick labels alone — the markup is
given as a table keyed to date, time and price. That is auditable in a way an
approximately-placed rectangle is not. The clean chart is included as the evidence.

### The markup

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

### What matches the lesson, and what does not

**Matches:**
- The week does resolve into roughly **three legs** between the opening extreme and the
  opposite extreme, which is the shape his answer chart shows.
- The move away from the Monday high runs **Tuesday through Thursday** — about three
  days — consistent with the printed "For At Least 3 Days" on the Weekly Structure slide.
- The Level 3 termination is followed by a sharp reversal, as his chart labels.

**Does not match, and is recorded rather than smoothed:**
- **The anchor point is ambiguous this week.** The lesson says the anchor is "where the
  midweek reversal comes in". Here the decisive extreme is on **Monday**, not midweek.
  Under `[00:11:44]` ("Sunday is the Asian session… could be Friday, Sunday, Monday") this
  is an allowed variation, but it means the single most important object in the lesson is
  placed by judgement, not by rule.
- **Friday does not behave.** `[00:05:24]` says "You always get out on Friday, always",
  and his chart shows the week ending quietly. This week Friday carried the largest range
  of the week in both directions. The lesson has no label for that.
- **I cannot verify the "does not cross the level for 2.5–4 days" claim** because
  "the level" (A-004) is defined only as an ordinal leg, not as a specific price line.

### Honest self-assessment of 11a

```text
FIRST-PASS ATTEMPT — completed, unverified
```

This is my first pass and it is preserved as written. **It has not been checked against
any answer key**, because none exists for this week. The labels are plausible imitations
of a worked example, not confirmed identifications — and the ambiguity noted above (a
Monday anchor in a lesson that says midweek) is exactly the kind of judgement call that a
real answer key would settle and I cannot.

I am **not** claiming this demonstrates recognition ability. Per
`MASTERY_STANDARD.md` §B, recognition means identifying taught concepts on charts *not
used in the lesson* — this is such a chart, but with no ground truth the exercise
demonstrates only that I can apply the vocabulary, not that I applied it correctly.

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
free tier gives ~7 months of 1H history per pair, which is far more than enough to find
forty formations.

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
| 11a — label the weekly cycle, USD/CHF 1H | **Attempted on substituted week, first pass preserved, ungraded** | Answer key does not exist; 2012 data account-gated |
| 11b — 40 flashcards | **DEFERRED** | A-011 (M/W undefined), A-007 (second leg undefined) |
| Forum posting / answer key / survey / student folder | `NOT APPLICABLE` | 2012 infrastructure |
