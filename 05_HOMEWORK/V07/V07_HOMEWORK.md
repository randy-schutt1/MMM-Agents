# V07 — HOMEWORK

> **All of V07 is `GUEST` material.** Under `DECISIONS.md` **`D-033`** that is normative
> evidence at equal weight with the course author's, and the tag records **who spoke**, not a
> demotion. **`D-030` is untouched**: nothing built on an undefined term becomes performable
> because the speaker's authority changed — which is why the assignment below is done on the
> one object in V07 that needs no course definition, and why §3's shape census is fenced.

---

## 1. THE ASSIGNMENT, AS GIVEN

There is no slide headed "Homework" in V07. There is a **renamed** assignment, and the rename
is printed on the deck — frame `V07_00-04-55` shows *"like Um.. ~~Homework~~.. I mean R&D."*
with **Homework struck through in red**.

| Marker | The assignment, verbatim |
|---|---|
| `[00:11:59]` | *"R&D, what form they were known as homework."* |
| `[00:12:03]` | *"They have to go back to looking charts so you can see how many times it occurred."* |
| **`[00:12:09]`** | ***"How many times over a year is what I am looking for actually occurred, where I am looking to get it."*** |
| `[00:12:27]` | *"So a little bit of scrutiny as far as what you are looking for."* |
| `[00:12:43]` | *"Take enough of these and keep them by your computer and you will see a whole lot of good trades that seem to slip by."* |
| `[00:12:58]`–`[00:13:01]` | *"Flashcards do one thing. They get the actual image to be implicitly embedded in your mind."* |
| `[00:13:18]` | *"So the more you look at them, the easier you get to remember what the good setups and the good entries look like and you will take them."* |
| `[00:11:44]`–`[00:11:48]` | *"The next thing is you need to practice getting those entries. That's what all these demo accounts for."* |
| printed, `V07_00-13-00` | slide bullet **"Flashcards (Screenshots)"** — the physical definition of the artifact |

**Disposition of each part**

| Part | Disposition | Why |
|---|---|---|
| **Count how many times it occurred over a year** | ✅ **PERFORMED** — §2 | Fully performable on real data |
| **Check whether the year you pick matters** | ✅ **PERFORMED** — §2b | Not asked for. Done because the answer turned out to move |
| **Build flashcards (screenshots)** | ✅ **PERFORMED** — §4 | The slide defines the artifact; the artifact is buildable |
| **Is the shape really "everywhere"?** `[00:12:14]` | ⚠️ **PERFORMED UNDER A FENCE** — §3 | The presenter's claim is qualitative. `D-030` forbids defining his M/W, so a declared non-course stand-in is used and labelled as one |
| **Practise the entries on a demo account** | ❌ **NOT APPLICABLE** (`D-018`) | No account exists and none may be opened. This is the V01 H6/H7 disposition, unchanged |

### What "what I am looking for" is, in this homework, and why

The assignment tells the student to pick their own setup. **`D-030` bars this session from
picking one built on a course term** — *second leg* (`A-007`), *level* (`A-004`), *M/W*
(`A-011`), *railroad tracks*, *tilted* (`A-058`) are all named and undefined, and counting an
approximation of any of them would produce a number that outlives its caveat.

**The setup counted here is the one V07 makes mechanical itself:**

> **a 50-pip run away from the day's extreme** — the *"Hi-Lo"* object of `[00:07:17]`, with the
> lesson's own 50-pip exit (`[00:13:45]`, `[00:15:17]`, `[00:16:24]`, `[00:46:06]`, and printed
> *"Exit +50 pips & 8.57% gain"* at `V07_00-19-15`).

Its ceiling is measured separately and at length in
`06_MANUAL_BACKTEST/V07/BT_V07_0001.md` (`PT-033`). **This homework is not that test.** `PT-033`
asks *"what is the ceiling over 3.5 years"*; the homework asks the lesson's own question —
*"how many times over a year"* — and then asks whether that instruction is stable.

---

## 2. THE COUNT, AS ASSIGNED  *(script label `H1`)*

**Method.** `05_HOMEWORK/V07/scripts/v07_homework.py`. GBP/USD 15-minute bars from the HistData
M1 corpus (`D-036a`), one full calendar year, **2015-01-01 → 2015-12-31**, wholly inside
DEVELOPMENT (`D-035`). Both `D-031` timezone arms and both day definitions from `PT-033` §5, all
four reported. Input digests printed by the script and recorded in §6.

| Cell | days in 2015 | days offering a 50-pip run from the extreme | fraction |
|---|---|---|---|
| **A · D-SESSION** | 259 | **258** | **0.996** |
| **A · D-MIDNIGHT** | 312 | 264 | 0.846 |
| **B · D-SESSION** | 293 | 259 | 0.884 |
| **B · D-MIDNIGHT** | 312 | 264 | 0.846 |

**Where the successful entries sat on the clock** (V02's printed session table, read in the
corpus's own fixed `UTC−5` clock — the table is instructor material, the windows are its):

| Cell | Asian | London | New York | outside all three |
|---|---|---|---|---|
| A · D-SESSION | 91 | **172** | 69 | 37 |
| A · D-MIDNIGHT | 90 | **197** | 84 | 5 |
| B · D-SESSION | 63 | **163** | 92 | 46 |
| B · D-MIDNIGHT | 70 | **188** | 112 | 5 |

**London holds the day's extreme more often than either other session, in all four cells.**
That is an observation about where the extreme *is*, not a rule, and it is not offered as
support for anything V07 says — V07 states no session times at all (`V07_SOURCE_NOTES.md` §10).

### 2a. FIRST ATTEMPT, PRESERVED — AND IT WAS MISLEADING

**This is what happened, in order, and the first reading is kept because
`STUDY_PROTOCOL.md` §6 requires it.**

> **First attempt.** I ran the count for 2015 only, because the assignment says *"over a year"*
> and 2015 is a year. `A · D-SESSION` returned **0.996 — 258 of 259 days**. My first reading was
> that the answer is *"essentially every day"*, which would have made `[00:07:17]`'s *"you're
> going to make pips every day"* look almost literally true at the ceiling.
>
> **Why that was wrong.** It disagreed with `PT-033`'s **0.9535** over 2013-01-06 → 2016-06-30 —
> the same measurement, the same cell, a wider window. A single year cannot be both 0.996 and
> consistent with a 0.954 average unless the other years are worse. **The disagreement is what
> prompted §2b**, and had I not been running `PT-033` in the same session I might not have
> noticed.

### 2b. CORRECTION — "OVER A YEAR" UNDER-SPECIFIES THE ANSWER

`05_HOMEWORK/V07/scripts/v07_year_sensitivity.py`, one calendar year at a time:

| Cell | 2013 | 2014 | 2015 | spread | 2016 H1 *(half year — not comparable)* |
|---|---|---|---|---|---|
| **A · D-SESSION** | 0.981 | **0.861** | **0.996** | **0.135** | 1.000 |
| A · D-MIDNIGHT | 0.830 | **0.724** | 0.846 | 0.122 | 0.871 |
| B · D-SESSION | 0.867 | **0.761** | 0.884 | 0.123 | 0.903 |
| B · D-MIDNIGHT | 0.827 | **0.724** | 0.846 | 0.122 | 0.871 |

> ### **THE ANSWER TO THE LESSON'S OWN QUESTION MOVES BY 12–14 PERCENTAGE POINTS DEPENDING ON WHICH YEAR YOU PICK.**
>
> 2014 is the low year in every cell; 2015 the high one. A student who does the R&D on 2015 and
> a student who does it on 2014 come away with materially different priors from **the same
> instruction, correctly followed.**
>
> **This is a finding about the assignment, not about the market.** `[00:12:09]` says *"over a
> year"* and does not say which, and the difference is large enough to matter to the confidence
> the exercise is explicitly designed to build (`[00:20:36]` *"you've already seen the outcome
> of R&D… so now it's no problem taking that trade"*).
>
> **`INFERRED`, and offered as a suggestion rather than a rule:** the instruction is repaired by
> reporting the count **per year with its spread**, which costs nothing, rather than by choosing
> a longer window — a longer window would hide exactly the year-to-year variation the student
> needs to see. **The course does not say this. I do.**

2016 is deliberately shown as a **half year** and never blended with the three full years:
`D-035` puts the boundary at 2016-07-01 and the corpus stops there, so 2016 H1 is not a year and
is not treated as one.

---

## 3. IS THE SHAPE REALLY "EVERYWHERE"? — PERFORMED UNDER A FENCE  *(script label `H3`)*

> ## ⚠ FENCE — READ THIS BEFORE ANY NUMBER IN THIS SECTION
>
> **The shapes counted here are NOT the course's M and W, and are not offered as a definition
> of one.** `A-011` is open, `D-030` forbids approximating it, and this session has not done so.
>
> What is counted is a **deliberately crude, fully-stated, non-course stand-in**: two local
> extremes, each higher (or lower) than the `n` bars on both sides, separated by between `n` and
> 40 bars, whose extreme prices lie within `tol` pips of each other. **`n` and `tol` are swept
> across a grid rather than chosen** (`D-010`), and no cell of the grid is preferred.
>
> **The claim being checked is qualitative and is the presenter's own**: `[00:06:32]` *"M's and
> W's are everywhere"*, `[00:12:14]`–`[00:12:21]` *"you will see M's and W's everywhere… all
> over the place everywhere in the day in different ranges."* A census of a crude stand-in can
> support or embarrass a claim of the form *"these are everywhere"*. **It cannot and does not
> measure any rule, hit rate, or edge, and no number here may be cited as one.**

GBP/USD 15-minute, 2015, Arm A. **24,853 bars in the year**, across **259 session days**.

| swing `n` | local highs | local lows | tol 3p | tol 5p | tol 10p | tol 20p |
|---|---|---|---|---|---|---|
| **2** | 3,584 | 3,585 | 2,849 / 2,915 | 4,515 / 4,525 | 7,825 / 7,703 | 12,034 / 11,871 |
| **3** | 2,546 | 2,551 | 1,431 / 1,467 | 2,262 / 2,256 | 3,830 / 3,782 | 5,816 / 5,827 |
| **4** | 1,948 | 1,929 | 790 / 801 | 1,245 / 1,216 | 2,163 / 2,018 | 3,297 / 3,159 |
| **5** | 1,602 | 1,602 | 497 / 528 | 793 / 797 | 1,363 / 1,321 | 2,126 / 2,085 |

*(cells are `M-like / W-like` counts)*

**Result: the presenter's qualitative claim survives every cell of the grid.** At the strictest
setting — a 5-bar swing and a 3-pip tolerance — there are still **497 M-like and 528 W-like
shapes in a single year on a single pair**, roughly **two per session day**. At the loosest,
about **46 per session day**. There is no parameterisation in this grid under which such shapes
are rare.

**M-like and W-like counts are near-symmetric in all sixteen cells** (largest divergence **6.7%**,
at `n=4, tol=10`), which is what you would expect if the shapes are a property of noisy price
paths rather than of direction.

> **What this does and does not license.** It supports *"they are everywhere"* — the premise of
> the presenter's own argument that the information must live in the filter rather than the
> shape (`V07_INTERPRETATION.md` §2.1). **It says nothing about whether the course's M and W are
> everywhere**, because the course has not said what they are.

---

## 4. THE FLASHCARDS, BUILT  *(script `v07_flashcards.py`)*

`05_HOMEWORK/V07/scripts/v07_flashcards.py` builds the artifact the slide defines — a
**screenshot** of a specific day, with the objects marked. Seven cards, in
`05_HOMEWORK/V07/charts/`:

| Card | Day (session day, Arm A) | Range | SHORT@HOD | LONG@LOD |
|---|---|---|---|---|
| POSITIVE | 2015-01-02 | 262.7 p | HIT | miss |
| POSITIVE | 2015-03-04 | 119.8 p | HIT | miss |
| POSITIVE | 2015-05-04 | 84.5 p | HIT | HIT |
| POSITIVE | 2015-07-02 | 77.1 p | miss | HIT |
| POSITIVE | 2015-09-01 | 108.0 p | HIT | miss |
| POSITIVE | 2015-10-30 | 162.7 p | HIT | HIT |
| **NEGATIVE** | **2015-11-16** | **48.9 p** | **miss** | **miss** |

**Selection rule, stated so it cannot be mistaken for curation:** the positives are taken at an
**even stride through the sorted list of qualifying days** — every 43rd of the 258 — so no day was chosen
for how it looks. The negative is **the only qualifying miss in 2015 under `A · D-SESSION`**, so
there was nothing to select between.

`STUDY_PROTOCOL.md` §8 requires positive **and** negative examples, and requires that failed
cases be kept. **Four of the six positives are half-failures** — the day offered 50 pips from
one extreme and not the other — and they are labelled that way on the card rather than being
replaced with cleaner ones.

**The negative card is the instructive one.** 2015-11-16 had a 48.9-pip range: the 50-pip target
was **arithmetically unreachable from either extreme, on a day with 96 bars of perfectly normal
price action.** That is what the 0.4%–27.6% of days that fail look like, and it is not a failure
of pattern recognition.

Cards are **SVG**, drawn directly from CSV numbers, with no plotting library (matplotlib is not
installed on this machine and this is not a reason to add a dependency). They are a **product**
of the data, never a measurement source — `E06` as restated by `D-036a`: *a chart may be looked
at; nothing may be measured off one.*

---

## 5. INDEPENDENT CROSS-CHECK: A SECOND MEASUREMENT METHOD  *(script label `H4`)*

The owner's standing requirement is at least one independent cross-check on homework
conclusions. **Two were run, on different axes.**

### 5a. Second measurement method — recompute §2 from M1 directly

§2's count is computed from `GBPUSD_M15_ARMA.csv`, an aggregate built by a **different session**
(`aggregate_m15.py`, `D-036a`). If that aggregation has a bug, every number in §2 inherits it.
So the same count was recomputed from the **raw M1 file**, bypassing the aggregate entirely
(372,231 M1 bars for 2015):

| Cell | days (M15) | days (M1) | hits (M15) | hits (M1) | miss-day sets |
|---|---|---|---|---|---|
| D-SESSION | 259 | **259** | 258 (0.996) | **258 (0.996)** | **identical — 1 day, agreed** |
| D-MIDNIGHT | 312 | **312** | 264 (0.846) | **264 (0.846)** | **identical — 48 days, agreed** |

**Exact agreement on counts and on the identity of every failing day.** This validates
`aggregate_m15.py` on the property this homework depends on, from a session that did not write
it — which is worth more than a self-check.

### 5b. Second data source — a different vendor

Run in `BT_V07_0001.md` §7 and not repeated here: **Yahoo Finance daily GBP/USD**, same window,
a day boundary nobody chose for this work, reproduces the shape of the range distribution and
independently confirms the day-boundary effect (`frac ≥ 50` of 0.906, sitting between the two
tested definitions' 0.954 and 0.810). **Levels are not compared and cannot be** (`D-036a`).

---

## 6. REPRODUCIBILITY

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Data source | **HistData.com M1 → M15** (`D-036a`); raw M1 for §5a |
| `GBPUSD_M15_ARMA.csv` | `857f91d74e663538fb6434d70e7e24d9cf0237b3678446f94e00e3210dc61ff4` |
| `GBPUSD_M15_ARMB.csv` | `eaf77f2b9fd33c713c7b66338f5b0ee4b2c1a4b43c3d3d57ff1cfbd8a8cc9b5c` |
| `DAT_MT_GBPUSD_M1_2015.csv` | `88e48765e2113cbcff053ca23cd965c3016416b2b8268db0046e2b8dcedf2673` |
| Data QA gate | `qa_histdata_m1.py` — C1–C4 `PASS`, C5–C7 signed off |
| Chart timezone | fixed `UTC−5`, no DST (Arm A); Arm B = +1 h under US DST |
| Window | 2015 for §§2–4; 2013 / 2014 / 2015 / 2016 H1 for §2b. **All inside DEVELOPMENT**; the holdout was never on disk |
| Measurement | **numbers parsed from checksummed CSVs. No chart was opened; nothing measured off a rendering** |

```bash
python3 05_HOMEWORK/V07/scripts/v07_homework.py
python3 05_HOMEWORK/V07/scripts/v07_year_sensitivity.py
python3 05_HOMEWORK/V07/scripts/v07_flashcards.py
```

---

## 6a. ADDENDUM 2026-08-13 (later, same day) — THE `C8` DATA HOLE

A concurrent session added a QA check after this homework was published (`f7c5c04`) and found a
**~22-hour hole at `2014-05-30 16:59` → `2014-06-02 15:01`** in the corpus — the only
unexplained absence in 3.5 years, and one that `D-036a`'s original `C5`–`C7` sign-off passed.

**It falls inside §2b's 2014 row and nowhere else.** One day bucket (`2014-06-02`) is affected,
it is a **miss**, and excluding it moves that cell's fraction by **+0.001 or less** — measured in
`BT_V07_0001.md` §9a, which carries the full four-cell table. **2014 remains the low year and
§2b's 12–14 point spread is unchanged.**

**§5a's second-measurement-method check is unaffected in a way worth stating:** it compares the
M15 aggregate against the raw M1 file, and a hole present in both is invisible to that
comparison. **A cross-source check validates aggregation, not completeness** — which is exactly
why `C8` was needed and why it is a different kind of control.

---

## 7. MASTERY RESULT FOR THIS HOMEWORK

**`SUCCESS AFTER CORRECTION`.**

The count was performed as assigned and the flashcards were built. **The first attempt returned
a number (0.996) that I read as "essentially every day", and that reading was wrong** — not
because the arithmetic was wrong but because a single year is not a stable answer to the
question, which I only established after the fact and only because an unrelated test in the same
session disagreed with it. The first attempt is preserved in §2a and the correction is §2b.

**One part is `NOT APPLICABLE` under `D-018`** — practising entries on a demo account
(`[00:11:44]`–`[00:11:48]`). No account exists, none may be opened, and this is the same
disposition V01's H6/H7 received. It is `NOT APPLICABLE` rather than `DEFERRED` because no
future lesson or infrastructure change makes it performable by an agent
(`D-019`'s test: *is there anything here to do at all* — for an agent, there is not).
