# V19 — HOMEWORK

## §1 — ⭐ V19 SETS NO NEW ASSIGNMENT, AND THAT IS THE FIRST FINDING

**V18 closed with a homework block at `[00:45:31]`. V19 has none.** The file ends mid-example at
`[01:07:13]` — *"it's an essence broken down railroad tracks which gives you an extra entry and
earlier entry"* — with no summary, no assignment and no sign-off. **That is the shape of a recording
that continues into V20** (`Wk9 Part2`, the same night), and it is recorded as evidence for that
reading rather than as an omission.

**What V19 does instead is restate a cumulative STANDING checklist**, `[00:07:40]`–`[00:08:26]`, and
put it on screen at `06:45`. Quoted from the marker grid with its ASR defects intact:

> `[00:07:40]` *"you should notice by now to keep adding things every week. You have your
> flashcards"*
> `[00:07:57]` *"You have to mark up the four hour chart and you have it taking your TDI only
> trades"*
> `[00:08:01]` *"If you haven't worked **the big boy, don't your movie average only**"*
> `[00:08:06]` *"If you haven't worked on the pivot points and review the recording used to **I low
> market the blue tracer**"* → `[00:08:12]` *"**A yard**"*
> `[00:08:15]` *"These are the things you have to do if you're struggling in the business and you
> can't check off every single one of those things on the list"* → `[00:08:23]` *"You're failing
> yourself"*

⚠️⚠️ **THREE OF THE SEVEN ITEMS ARE UNRECOVERABLE FROM THE AUDIO AND ARE RECOVERED FROM THE SLIDE.**
The printed checklist at `06:45` reads:

| # | Printed item | Committed transcript |
|---|---|---|
| 1 | `Have a set of Flash cards` | ✅ recoverable |
| 2 | `Have 4hr Markups` | ✅ *"mark up the four hour chart"* |
| 3 | `Have Taken TDI only Trades` | ✅ recoverable |
| 4 | **`Worked the Big Board`** | ❌ *"worked the big boy"* |
| 5 | **`Moving AVG Only trades`** | ❌ *"don't your movie average only"* |
| 6 | `Understand Pivot Points` | ✅ recoverable |
| 7 | **`Use ADR and Hi/Lo Markers`** | ❌ *"I low market the blue tracer"* / *"A yard"* |

⭐ ***"A yard" is `ADR`.*** Recorded prominently because
`00_SYSTEM/DECISION_DRAFT_D-051_ADR_INDICATOR.md` concerns exactly this indicator, and **this frame
is Tier 1 evidence that the course prescribes an ADR marker as standing homework.** Flagged for
that draft. **No adoption is proposed by this session.**

---

## §2 — WHAT COULD BE EXECUTED, AND WHAT COULD NOT

| # | Item | Executed? | Why |
|---|---|---|---|
| 1 | Flash cards | ❌ | needs the student's own card set; V19 shows one student's card at `43:50` and defines no schema |
| 2 | 4hr markups | ❌ | a drawing task; and the markup convention is not stated in V19 |
| 3 | TDI-only trades | ❌ **BLOCKED** | `D-030`. V19 gives no TDI level, threshold or setting. The bands are not mentioned at all (`V19_SOURCE_NOTES.md` §6) |
| 4 | The Big Board | ❌ | undefined in V19 — the phrase occurs only on the slide |
| 5 | Moving-average-only trades | ❌ **BLOCKED** | `D-030`. *"Mustard"* is bound by `D-043` to a **colour**; V19 supplies no period, and *"blue tracer"* is undefined (`A-133`) |
| 6 | Pivot points | ❌ | V19 names them once (`[00:08:06]`) and defines nothing |
| 7 | **`Use ADR and Hi/Lo Markers`** | ⚠️ **PARTIALLY** | ADR and prior-session extremes are computable from price alone. **The ADR lookback is NOT stated by V19 and is this session's convention** — see §3 |

**Six of seven are recorded as NOT DONE, with reasons, rather than approximated.** `D-030` is
explicit that definitions are never approximated, and four of the six fail on exactly that.

---

## §3 — WHAT WAS RUN

`06_MANUAL_BACKTEST/scripts/hw_v19.py` → `data/hw_v19_output.txt`, `data/hw_v19_results.json`.

**This is HOMEWORK, not a test.** It states no hypothesis, scores no prediction, and returns no
verdict. Corpus: HistData GBP/USD M1 → M15, DEVELOPMENT scope only (`D-035`), both `D-031` arms,
windows `W-A` and `W-B`. Days are included only if complete (all 26 box + 56 post buckets);
**2 days excluded in `W-A`, 3 in `W-B`, on each arm.**

⚠️⚠️ **THE ADR LOOKBACK IS THIS SESSION'S CONVENTION, NOT V19's.** V19 says *"ADR"* once, via the
printed slide, and **never states a period.** Three periods (5, 10, 20 sessions) are reported so
that no single one is privileged, and **none of them is presented as the course's.**

---

## §4 — ADR

Session range = post-box high − post-box low (`03:00`–`17:00`), in pips.

| arm | window | `ADR5` median | `ADR10` median | `ADR20` median | next day exceeds `ADR10` |
|---|---|---|---|---|---|
| A | `W-A` (2015) | 114.64 | 112.06 | 110.52 | 37.8 % |
| A | `W-B` (2014–15) | 95.42 | 99.45 | 101.11 | 39.8 % |
| B | `W-A` | 115.74 | 114.45 | 112.05 | 39.0 % |
| B | `W-B` | 95.92 | 100.05 | 102.21 | 40.4 % |

**Descriptive reading, offered as description only:**

* ⭐ **GBP/USD's daily range over 2014–2015 sits near 100–115 pips at the median**, and the three
  lookbacks agree to within ~4 pips — so the ADR figure is **not sensitive** to the period choice
  this session had to invent. **That is the most useful thing here**, because it means the
  undefined lookback (§3) does not much matter for the marker's practical value.
* **A session exceeds its own trailing ADR about 36–43 % of the time**, stable across arms, windows
  and lookbacks. **A marker drawn at ADR is therefore exceeded on roughly two days in five.**
* ⚠ `W-A` (2015) runs ~13 pips wider than `W-B` (which contains 2014 as well), i.e. **2015 was the
  wider year.** Recorded because any V19-derived pip figure inherits that regime difference.

---

## §5 — HI/LO MARKERS

How often the **previous** session's extreme is reached in the **next** session:

| arm | window | prev high touched | prev low touched | both | neither |
|---|---|---|---|---|---|
| A | `W-A` | 46.3 % | 52.2 % | 12.9 % | 14.5 % |
| A | `W-B` | 47.0 % | 51.5 % | 12.1 % | 13.7 % |
| B | `W-A` | 45.9 % | 52.2 % | 12.2 % | 14.1 % |
| B | `W-B` | 46.4 % | 51.9 % | 11.9 % | 13.7 % |

**Descriptive reading:**

* ⭐ **A prior-session extreme is reached about half the time, and the four cells agree to within
  1.1 percentage points** — arms and windows do not move it. **This is why the marker is worth
  drawing**: it is a level price interacts with on roughly every other day.
* ⭐ **The low is touched more often than the high, consistently, on every cell** (51.5–52.2 % vs
  45.9–47.0 %). ⚠ **No explanation is offered.** GBP/USD fell over much of this period, which would
  produce exactly this asymmetry without any dealer behaviour, and **this measurement cannot
  separate the two.** Recorded as an observation, not a finding.
* **Both extremes are taken on ~12 % of days and neither on ~14 %.** So ~74 % of days take exactly
  one of the two.

---

## §6 — ⚠ THE PULLBACK OFF THE SESSION HIGH — AND WHY IT IS **NOT** A TEST OF V19's `15 to 25`

V19 states a consolidation distance **eight times** (`[00:18:09]`, `[00:18:23]`, `[00:18:41]`,
`[00:42:10]`, `[00:42:50]`, `[00:43:02]`, `[00:52:16]`, and `[00:17:29]`): **15 to 25 pips, as much
as 50 on the crosses.** It costs nothing to look at the corpus beside it.

Maximum pullback from the session high over the following **8 bars (2 h)**:

| arm | window | n | median | IQR | in 15–25 | < 15 | > 50 |
|---|---|---|---|---|---|---|---|
| A | `W-A` | 238 | **45.90** | 33.68 – 64.40 | 10.1 % | 2.1 % | 40.8 % |
| A | `W-B` | 474 | **40.75** | 27.52 – 58.50 | 16.0 % | 3.8 % | 34.4 % |
| B | `W-A` | 234 | **46.10** | 33.95 – 62.73 | 8.6 % | 1.7 % | 41.0 % |
| B | `W-B` | 469 | **40.60** | 28.70 – 57.20 | 14.3 % | 3.2 % | 33.5 % |

⚠️⚠️ **THIS IS NOT A REFUTATION OF V19 AND MUST NOT BE READ AS ONE. THE TWO QUANTITIES ARE
DIFFERENT.**

* **V19's `15 to 25`** is *where the dealer consolidates and holds* — `[00:18:16]` *"the deal[er]
  will consolidate off of the low or the high[,] 15 to 25 pips"*. It is a **resting distance**.
* **What is measured above** is the **maximum** excursion away from the high in two hours — the
  deepest point, not the resting point. **A maximum is necessarily larger than the level it
  oscillates around**, so a gap in this direction is expected *a priori*.

**What is worth recording is the SIZE of the gap, not its direction:** the median maximum pullback
is **~41–46 pips**, roughly **double** the top of V19's stated band, and **a third to two-fifths of
sessions exceed 50 pips** — the figure V19 reserves for *"some of the crosses"*. **On GBP/USD, the
majors' own excursions routinely reach the level V19 attributes to crosses.**

⚠️ **A proper test of `15 to 25` would have to identify the consolidation and measure its centre,
which needs a consolidation definition V19 does not supply.** That is why this sits in HOMEWORK
under a "no verdict" heading and **not** in a `PT-` file. **It is offered to a future test as a
starting distribution, not as a result.**

---

## §7 — REPRODUCTION

```bash
cd 06_MANUAL_BACKTEST/scripts
python3 hw_v19.py
```

Requires the Git-ignored HistData corpus (`D-011`/`D-036a`). `mmm_lib.qa_gate()` runs as a
precondition and passed on the run reported here.
