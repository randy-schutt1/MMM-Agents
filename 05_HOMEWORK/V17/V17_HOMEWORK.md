# V17 — HOMEWORK

**Lesson:** `Bootcamp1 Wk8 051312 Part1 (57mins).swf` · V17 · 2012-05-13
**Runner:** `06_MANUAL_BACKTEST/scripts/hw_v17.py` · **Output:** `data/hw_v17_output.txt`,
`data/hw_v17_results.json`, `data/probe_v17_output.txt`

---

## §0 — THE ASSIGNMENT, AS V17 GIVES IT

⚠ **V17 has no `R&D` homework slide.** V16 ended on one (*"Find the expected high and low for the
day on six majors"*); **V17 ends on an exhortation**, `[00:56:33]` *"Make the safety trade your
signature trade."*

**What V17 assigns is a printed AUDIT of the whole course to date** —
`V17_00-06-05_where-are-you-by-now-you-should-checklist-slide.png`:

> `Have a set of Flash cards` · `Have 4hr Markups` · `Have Taken TDI only Trades` · `Worked the Big
> Board` · `Moving AVG Only trades` · `Understand Pivot Points` · `Use ADR and Hi/Lo Markers`

**Six of those seven are chart drills a machine cannot perform** (flashcards, markups, TDI-only and
MA-only trades, the Big Board drill). **This homework does the seventh — `Understand Pivot Points`
and `Use ADR and Hi/Lo Markers` — by taking V17's own printed seven-point answer key and carrying it
as far as it goes on real data.**

## §0a — SCOPE LIMITS, DECLARED BEFORE ANY NUMBER

| # | Limit |
|---|---|
| 1 | **GBP/USD only.** V17's own quiz charts are `GBPUSD,M15` and `GBPJPY,M15`; only GBP/USD is in the checksummed corpus. **`GBPJPY` is not tested and its ranges are materially larger**, which matters for `§2`. |
| 2 | **`D-035` DEVELOPMENT only** (2013-01-06 → 2016-06-30). Not the `D-044` extension — this is homework, not a test, and a second window would invite a comparison the exercise does not support. |
| 3 | **No 2012 data exists on disk.** The lesson is from 2012-05-13. |
| 4 | **The Asian box is `mmm_lib` convention `C-2`** — `20:30 → 03:00`, from V02's printed slide. **V17 states no Asian-session boundary anywhere.** Every `§2`/`§3` number is therefore a statement about `C-2`'s box. |
| 5 | **Both `D-031` arms are run and both are reported.** |
| 6 | ⚠ **This is HOMEWORK. It states no hypothesis, scores no prediction and returns no verdict.** `PT-045` / `BT_V17_0001` is the pre-registered work. |

---

## §1 — ⛔ WHERE THE ANSWER KEY STOPS, STATED FIRST

V17's printed `Safety Trade` answer key has **seven** points. **Five of them cannot be evaluated by
this project at all**, and that is the first result rather than a caveat at the end:

| # | Printed point | Computable? | Blocked by |
|---|---|---|---|
| 1 | `Visible Trap Yesterday (PFL) LOW` | ❌ | `peak formation` has no formal test; and `A-116` — the slide says *yesterday*, the audio says *the week* |
| 2 | `Dealer Handles The BO Traders and 200 Traders` | ❌ | *"handles"* is not a measurement |
| **3** | `Dealer is Trading 25 to 75 pips off Y-LOD` | ✅ | — **§3** |
| **4** | `Dealer Cuts the Asain Range as a visible stop hunt` | ✅ | — **§2** |
| 5 | `MM throws a spike and comes above for 1 hour` | ❌ | *"spike"* undefined; the 1-hour clock has no start test |
| 6 | `W -TDI Blood` | ❌ | `A-010`/`A-011` (the `W`) **and** `A-084` (the TDI bands) |
| 7 | `Consolidation TP` | ❌ | `consolidation` undefined; no exit rule anywhere in the corpus |

⭐⭐ **TWO OF SEVEN.** V16's homework completed to five of seven numbers and stopped; **V17's
completes to two of seven and stops.** The lesson with the most complete printed checklist in the
corpus yields the *least* computable one, because its points are about **behaviour** rather than
about **levels**.

---

## §2 — POINT 4: *"Dealer Cuts the Asain Range as a visible stop hunt"*

**Measured as:** the post-box (`03:00 → 17:00`) excursion **beyond** each Asian-box edge, in pips.

| | arm A | arm B |
|---|---|---|
| `n` complete session days | **899** (5 excluded) | **898** (6 excluded) |
| **fraction of days cutting EITHER edge** | ⚠ **0.9967** | ⚠ **0.9978** |
| median downward extension | **25.5 pips** | **27.0 pips** |
| median upward extension | **21.1 pips** | **22.7 pips** |
| fraction with the down-extension inside `25–50` | 0.2080 | 0.2127 |
| fraction with the up-extension inside `25–50` | 0.1802 | 0.1759 |
| **fraction with EITHER inside `25–50`** | **0.3648** `[0.334, 0.397]` | **0.3608** `[0.330, 0.393]` |

### ⚠⚠ THE FIRST NUMBER IS THE FINDING, AND IT IS AWKWARD FOR THE CHECKLIST

**GBP/USD extends beyond one side of the `C-2` Asian box on 99.7% of days.** *"Dealer cuts the
Asian range"* is therefore **true on essentially every day** and **carries no information as a
selection criterion.** A checklist item satisfied 997 times in 1,000 does not discriminate between
a setup and a Tuesday.

### ⭐ AND THE SECOND NUMBER IS A GENUINE CORROBORATION

**The median downward extension is `25.5` / `27.0` pips** — sitting almost exactly on the **lower
edge of the `25–50` band** the instructor states at `[00:28:59]` and a student had printed on his
flashcard 15 minutes earlier. ⭐ **The magnitude is right. It is the *"visible stop hunt"* framing
that does not survive: the typical day's extension is a stop hunt by his numbers, which is another
way of saying the band describes ordinary daily behaviour.**

⚠ **Only 36% of days land the extension INSIDE `25–50`** — the rest are smaller or (more often)
much larger. So the band is a **median**, not a range that days respect.

### §2a — DOES THE FLASHCARD'S `< 50 pips` FILTER HELP? **NO.**

The student flashcard's first `Short Trade` criterion is `Asian range less than 50pips`.

| | arm A | arm B |
|---|---|---|
| **median Asian-box range** | **33.1 pips** | **29.3 pips** |
| inter-quartile range | `24.7 – 43.8` | `21.9 – 39.3` |
| **fraction of days PASSING `< 50 pips`** | ⚠⚠ **0.8509** `[0.826, 0.873]` | ⚠⚠ **0.8931** `[0.871, 0.912]` |
| stop-hunt-in-band rate on **passing** days | 0.3673 | 0.3616 |
| stop-hunt-in-band rate on **failing** days | 0.3507 | 0.3542 |

⭐⭐ **THE FILTER PASSES 85–89% OF ALL DAYS AND CHANGES THE DOWNSTREAM RATE BY 1.6 AND 0.7
PERCENTAGE POINTS.** On GBP/USD in this window, `Asian range less than 50pips` **is not a filter.**

⚠⚠ **THIS IS THE SHARPEST THING THIS HOMEWORK FOUND, AND IT LANDS ON `A-112`.** The single most
codeable-looking line on the most codeable-looking artifact in V17 — a **student's** card the
instructor praised the *labelling* of — is **inert on this instrument.** A session that had coded
the card without measuring it would have shipped a no-op and called it a rule.

⚠ **The honest counter, stated because it is real:** V17's better trade was **GBP/JPY**, whose
ranges are larger, and the card's author does not say which pair he traded. **On a wider-ranging
pair the filter could bite.** It is not tested here (`§0a` limit 1). **What is established is that
it does not bite on GBP/USD**, which is the pair the card's own `Short Trade` column would most
naturally be applied to and the only one in the corpus.

---

## §3 — POINT 3: *"Dealer is Trading 25 to 75 pips off Y-LOD"*

**Measured as:** today's session low minus **yesterday's** session low, in pips (positive = today's
low is above yesterday's), and the mirror on the highs.

| | arm A | arm B |
|---|---|---|
| `n` | **898** | **897** |
| **median (today's low − yesterday's low)** | ⚠ **−2.8 pips** | ⚠ **−2.9 pips** |
| fraction with today's low `25–75` **above** yesterday's low | **0.2138** | **0.2062** |
| fraction with today's high `25–75` **below** yesterday's high | **0.2261** | **0.2297** |
| **fraction satisfying EITHER** | **0.4243** `[0.392, 0.457]` | **0.4214** `[0.390, 0.454]` |

### ⚠ THE MEDIAN POINTS THE WRONG WAY

**The typical GBP/USD day makes its low fractionally BELOW yesterday's low, not 25–75 pips above
it.** The claim describes **21%** of days on the low side.

⭐ **This does not refute the lesson**, and the homework does not claim it does. `[00:26:30]`'s
*"is the dealer trading 25 to 75 pips off yesterday's low?"* is a question asked **about a chart he
has already selected as a safety trade** — it is a *confirmation* criterion inside a setup, not a
description of the average day. **What the measurement establishes is that it is not a base rate**,
and therefore that points 3 and 4 together select roughly a third to two-fifths of days **before**
any of the five uncomputable points are applied.

⚠ **And `A-116` bites here.** The printed key says the trap is *yesterday's*; the audio says the peak
formation low is *the week's*. **This section measured `Y-LOD`, because that is what point 3
prints.** A week-anchored reading would give different numbers and **is not computed**, because
choosing between them is exactly what `A-116` says the corpus cannot do.

---

## §4 — H4: COMPREHENSION PROBE — **33/33**, AND THE SCORE IS WEAK EVIDENCE

`data/probe_v17_output.txt`. **Thirty-three recall claims about V17 were written out, then a checker
was run that looks for required substrings at each claim's own marker in the committed transcript
(±2 lines).** The answers were fixed before the checker ran; the checker is committed alongside.

**Result: 33/33.**

⚠⚠ **AND THE SCORE IS NEARLY WORTHLESS AS EVIDENCE OF UNDERSTANDING, WHICH THIS SECTION SAYS RATHER
THAN LEAVING IMPLICIT.** The probe was written **after four close readings of the transcript**, by
the same session that wrote the claims. **It tests that the source notes quote the file accurately —
which is worth having, and is what a `grep` proves — and it tests nothing about comprehension.**
`V16_HOMEWORK.md` §6 made the same disclosure about its 22/22 and it applies unchanged.

⭐ **The one thing it does establish, and it is not nothing:** every load-bearing quotation in
`V17_SOURCE_NOTES.md` and `V17_INTERPRETATION.md` is **machine-verified against the committed
transcript at its own marker.** After V16's `S1` — eleven frame names fabricated from a transcript —
a mechanical check that the *quotations* are real is worth its cost.

---

## §5 — WHAT THE HOMEWORK PRODUCED, IN ONE LINE

⭐⭐ **V17's most complete-looking checklist reduces to two computable points, both of which describe
between a fifth and two-fifths of ordinary GBP/USD days — and the flashcard filter that looked most
codeable of all passes 85–89% of days and changes nothing.**
