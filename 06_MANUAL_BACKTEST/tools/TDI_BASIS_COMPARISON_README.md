# TDI VOLATILITY-BAND BASIS — SIDE-BY-SIDE COMPARISON KIT

**Purpose:** settle, *by the owner's own eye on a real chart*, which series the TDI volatility
bands are two standard deviations **of**.

**Status of what this kit produces:** ⛔ **NOT a course-verified fact.** Whatever the owner picks
is logged as an **`OWNER EMPIRICAL PREFERENCE`**, a tier of its own. See
[§6 How to log the result](#6-how-to-log-the-result-and-how-not-to) — that section is the part
that matters most, and it is the part easiest to get wrong.

| | |
|---|---|
| **Open record** | `C-021` — `11_CONTRADICTIONS/CONTRADICTIONS.md` |
| **Review item** | **187** — `18_REVIEW/REVIEW_INDEX.md`, marked ⬜ *PUT TO THE OWNER* |
| **Governing decision** | `D-048` Part 2 — ladder applied in full, returned **RUNG 4: DO NOT ADJUDICATE** |
| **Branch** | `tools/tdi-basis-comparison` — **NOT merged to integration.** Test artifacts, not adopted content |

---

## 1. THE TWO FILES

Both in this directory. Both Pine Script **v5**. Paste into TradingView → Pine Editor → Add to chart.

| File | Bands are 2 std-devs of… | Evidence |
|---|---|---|
| **`MMM_TDI_RSI_BASIS.txt`** (VARIANT **A**) | **the RSI line itself** | **V12 `[00:16:16]`–`[00:16:20]`** — *"it's two standard deviations away from price action… from the RSI line. Thank you."* Course author's final position that lesson, reached under an in-chat correction. Dean Malone's public stock TDI agrees (Tier 3, non-normative) |
| **`MMM_TDI_MARKETBASE_BASIS.txt`** (VARIANT **B**) | **the market base line** | **V14 `[00:45:09]`** — *"The bands are two standard deviations away from the market base."* Unhedged, unprompted, one week later, verbatim on two ASR engines. **Tier 2 `MMM-NOTES` p.45 independently agrees** |

### What is held identical (so the comparison is clean)

Everything. The two files differ in exactly **one line of arithmetic**:

```
VARIANT A:   dev = bandMult * ta.stdev(rsiVal,   bandLen)
VARIANT B:   dev = bandMult * ta.stdev(baseLine, bandLen)
```

…plus the panel title and one tooltip, so the two can be told apart in the TradingView legend.
Nothing else. Verified by diff.

Shared, in both: RSI period **21** (`[TIER 1]`, `A-080` **CLOSED — RESOLVED BY COURSE**), fast MA
**2** SMA, slow MA **7** SMA, band/MBL period **34** `[TOOLING]`, std-dev multiple **2.0**, levels
68 / 63 / 50 / 37 / 32. The band **centre** is the market base line in *both* variants — only the
**width** changes.

> ⚠️ **Two deliberate departures from `MMM_TDI.txt`,** both stated so they are not mistaken for drift:
> 1. **Multiplier is `2.0`, not `1.6185`.** `MMM_TDI.txt` still carries the Tier-3 public guess. The
>    multiplier is **not disputed** — V12 and V14 both say *"two standard deviations"* — so `2.0` is
>    the better number *and* it keeps the basis as the sole variable under test.
> 2. **Pine v5, not v6.** `MMM_TDI.txt` was ported to v6 in commit `c8246bb`. These were written to
>    v5 as briefed; the source uses no v6-only features, so this is a one-line change either way —
>    flip `//@version=5` to `6` in both files if you'd rather they match the parent.
>
> ℹ️ **`MMM_TDI.txt` is not on this branch.** It lives on `feature/tradingview-mmm-indicator`,
> which has never been merged. These two files are self-contained and don't need it.

---

## 2. HOW TO SET UP THE COMPARISON

1. Open a chart you know well — ideally one you have **watched the TDI on in practice**, on the
   timeframe you actually trade. Recognition is the whole instrument here; an unfamiliar chart tells
   you nothing.
2. Add **both** scripts. TradingView gives each its own pane. **Do not merge the panes** — you want
   two identically-scaled 0–100 panels stacked, so band width is compared by eye at a glance.
3. In **both** panels, turn ON **"Raw RSI line"** (Settings → Lines). It is off by default. You need
   to see the RSI and the market base line together to understand *why* the two disagree.
4. Scroll back across several hundred bars — trends, ranges, and the transitions between them.

---

## 3. ⭐ WHAT TO LOOK FOR — THE DECISIVE TEST

I measured both variants over **86,824 bars of GBPUSD M15 (2013→)** from
`06_MANUAL_BACKTEST/datasets/HISTDATA_GBPUSD_M1/GBPUSD_M15_ARMA.csv`, at the exact shared parameters
above. The two are not subtly different. They are **grossly** different, and one number separates
them cleanly:

### 3.1 The single most decisive thing: how often the RSI Price Line breaks a band

| | Variant A (RSI basis) | Variant B (market-base basis) |
|---|---|---|
| **RSI Price Line sits OUTSIDE the bands** | **8.7%** of bars | **52.6%** of bars |

**This is the test.** A "VB break" in variant A is an **event** — it happens on roughly one bar in
twelve, which is what a signal-bearing threshold should look like, and the `.ex4` has dedicated
*"Upper/Lower VB Break"* buffers implying it is meant to be one. In variant B the RSI Price Line is
outside the bands **more than half the time** — it would not be a signal, it would be the default
state.

> **Ask yourself the one question that decides it:** when you were taught this, and when you have
> used it — was a volatility-band break a **notable event** you waited for, or was the line **usually
> outside** the bands? If it was an event, that is **variant A**. If the fast line genuinely spent
> most of its life outside a narrow ribbon, that is **variant B**.

### 3.2 Band width

| | Median full band width | 10th pct | 90th pct |
|---|---|---|---|
| **Variant A** (RSI basis) | **20.7 RSI points** | 11.6 | 35.0 |
| **Variant B** (market-base basis) | **8.4 RSI points** | 3.4 | 18.0 |

Variant B's bands are a **median 40% of variant A's width** — and narrower on **91.3%** of all bars.
On the quietest stretches B collapses to **~16%** of A's width: a thin ribbon hugging the base line.

**Visually:** variant A looks like a normal Bollinger envelope with room in it. Variant B looks like
a **tight tube tracing the market base line**, with the RSI Price Line whipping in and out of it
constantly. You will be able to tell them apart from across the room.

### 3.3 Why they diverge — and where the divergence is largest

`baseLine` is already a 34-period SMA of the RSI. Variant B then takes the standard deviation **of
that already-smoothed series**, so it measures how much the *slow average* wanders — not how much
the RSI itself wanders. Smoothing strips out exactly the variance the standard deviation is trying
to measure.

The consequence is that **the two series decouple**, and they decouple hardest in the case the brief
anticipated:

- **Choppy price, RSI oscillating fast around a flat base line** → A **wide** (the RSI is genuinely
  volatile), B **collapses to near-nothing** (the base line is flat, so its dispersion ≈ 0). This is
  the most extreme divergence you will see. Look for it in ranges.
- **Steady trend, RSI grinding in one direction** → the base line *slopes*, so its 34-bar dispersion
  is large, and **B widens** — sometimes approaching A. This is the low-RSI-volatility-but-trending
  case: B's bands are driven by the base line's **slope**, not by the RSI's noise, which is a
  genuinely different behaviour and arguably the strongest argument that B is a different indicator
  rather than a scaled version of A.
- **Sharp reversal** → A widens immediately (the RSI moved); B lags by roughly the smoothing period.

So: **B is not simply "A but narrower."** It responds to different things. If you can find a stretch
where one variant is wide and the other is narrow *at the same moment*, that single screenshot will
tell you more than any of the statistics above.

### 3.4 A caveat on the numbers

These are one instrument, one timeframe, one 12-year sample, at a **`[TOOLING]`-sourced band period
of 34 that is itself not course-confirmed** (`A-086` is *eligible, not closed*). The direction and
rough magnitude of the difference are robust — B is structurally narrower for arithmetic reasons
that hold on any input — but treat the exact percentages as indicative, not as measurements of the
method.

---

## 4. WHAT THIS DOES **NOT** SETTLE

⚠️ **Nothing is unblocked whichever way you pick.** Stated plainly so the pick is not oversold:

- **`A-086` — the bands' PERIOD — stays `DO NOT CODE`.** It is never stated in Tier 1 *or* Tier 2.
  `Volatility_Band=34` is a `[TOOLING]` candidate only. Picking a basis does not supply a period.
- **`A-031`** ("blood in the water" — the market-baseline cross) and **`A-032`** ("shark fin") stay
  uncomputable, because they depend on the period.
- **No backtest** depending on these numbers may yet be reported as a test of the method.
- **`C-021` is not deleted or downgraded** by the pick. Both statements stay on the record, visible,
  per `D-048` limit 2.

**A ruling here buys clarity in the record. It does not buy an unblock.**

---

## 5. WHAT THE EVIDENCE ALREADY SAYS (so the eye is not the only input)

Recorded so the owner is choosing informed, not blind. **Neither side is clean:**

**For A (RSI line):** it is the course author's *corrected, final* position in V12, and a correction
accepted on the record (*"…from the RSI line. Thank you."*) — `D-048` **rung 1**. The public Dean
Malone TDI does build on the RSI line.
**Against A:** the corrector is **unidentified and is not the speaker**, and V12 `[00:07:20]` says
the build in use is an **altered** one — so the chat may have been right about the *public* indicator
and wrong about *this* one. Rung 1 therefore *arguably* answers, and **not cleanly.**

**For B (market base):** V14 is **later by one week, unhedged, unprompted**, against a V12 position
that was hedged, prompted and retracted — `D-048` **rung 3**. **Tier 2 `MMM-NOTES` p.45 independently
agrees**, recorded as a tiebreaker input and never as a warrant (`D-048` limit 3).
**Against B:** it states back the answer V12 explicitly **withdrew**, and rung 3 by its own terms
records **a position, not a fact** — it could never yield `RESOLVED BY COURSE`. The owner
**expressly declined** to have rung 3 applied as a default.

**Rung 2 is SILENT** — neither statement is a construction; both say what the band is *built upon*,
never what it *computes*. `A-093`'s pattern exactly.

**The `D-045` `TOOLING` artifact was checked field by field and is a NEGATIVE.** `Volatility_Band=34`
is a *period*; `63`/`37` are *static levels*; the RSI/MA fields build the *line* buffers; the `.ex4`
buffer-name list (*"MarketBase Line"*, *"RSI Price Line"*) says which lines are **drawn**, not what
the bands are a deviation **of**. ⚠️ **The one field that could encode a basis — the standard-deviation
multiplier — is not exposed by the MT4 indicator at all.** It is compiled into the binary.

⭐ **Rungs 1 and 3 point OPPOSITE WAYS. That is `D-048` rung 4's stated case, verbatim: DO NOT
ADJUDICATE, put it to the owner.** Which is what this kit does.

---

## 6. HOW TO LOG THE RESULT — AND HOW NOT TO

**Report back:** which variant you judge as matching what you were taught and have used — **A**, **B**,
or **neither / can't tell** — and, if you can, *why* (which of the visual tells in §3 decided it).
"Neither" and "can't tell" are **real, acceptable answers**; do not force a pick to close an item.
A screenshot of the moment that decided it is worth more than a sentence.

### ⛔ The evidentiary rule — this is the part that must not be got wrong

The result is logged as:

> **`OWNER EMPIRICAL PREFERENCE`** — the owner's visual judgment against his own experience of the
> indicator, recorded as such.

It is **NOT**, and must never be written up as:

- ❌ `RESOLVED BY COURSE` — only an **uncontradicted Tier 1 statement** produces that, and `C-021`
  is contradicted by definition. `D-048` limit 1 forbids it explicitly.
- ❌ `PROVISIONALLY RESOLVED — TIER 1 STANDING POSITION` — that is the **rung 3** outcome, and rung
  3 did **not** govern here; rung 4 did. Do not borrow rung 3's label for an owner pick.
- ❌ a closure of `A-086`, `A-031` or `A-032` (see §4).
- ❌ grounds to delete, downgrade or hide `C-021`. Both statements stay on the record.

**Why the distinct tier:** owner adjudication sits **outside** the ladder, exactly as `D-041`
established it sits outside the tiers. It is a legitimate and authoritative input — the owner is the
one person who has actually watched this indicator work — but it is **recollection of practice, not
course evidence**, and the record has to be able to tell the two apart fourteen years after the fact.
Recording it honestly costs nothing now and protects every downstream claim that leans on it.

**Where it goes when reported:**

- `11_CONTRADICTIONS/CONTRADICTIONS.md` → `C-021`, appended as a new dated section. **Leave §1–§7
  unedited.** Both statements stay.
- `18_REVIEW/REVIEW_INDEX.md` → **item 187**, ⬜ → status change citing the new `C-021` section.
- `00_SYSTEM/DECISIONS.md` → a new `D-xxx` recording the owner's pick, its tier, and — explicitly —
  what it does **not** unblock.
- This kit and its branch stay **unmerged** either way. They are test artifacts. If the picked
  variant is later promoted into `MMM_TDI.txt`, that is a separate, deliberate act on the
  `feature/tradingview-mmm-indicator` line, carrying the `OWNER EMPIRICAL PREFERENCE` tag with it.
