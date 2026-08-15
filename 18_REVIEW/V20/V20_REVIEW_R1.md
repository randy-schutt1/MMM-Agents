# V20 — INDEPENDENT REVIEW

**Round:** R1
**Reviewer:** Independent Reviewer / Teacher Agent, fresh session (`DECISIONS.md` `D-003`)
**Date:** 2026-08-15
**Lesson:** `Bootcamp1 Wk9 052012 Part2 (46mins) (1).swf` · V20 · 2012-05-20 · 00:45:49
**Printed subject:** `MARKET MAKER BOOT CAMP` / `THE OUT SIDE STRUCTURE`
**Submission reviewed:** `video/v20` @ `2ab5e83` (3 commits, `bd88e99`…`2ab5e83`), forked from `50edf5f`
**Review branch:** `review/v20`, isolated worktree `MMM-Agents-v20-review` (`D-038`)

---

## FINAL DECISION

**Decision:** `REVISE` — **0 CRITICAL, 2 MAJOR, 2 MINOR, 12 NOTE.**
**Confidence:** `HIGH`.

⛔ **`V21`'s GATE IS CLOSED** under `DECISIONS.md` **D-024** — two `MAJOR`s. It opens when actions 1
and 2 land **and are re-reviewed** (`D-003`).

**Neither `MAJOR` is the defect the submission flagged.** Both of the items it put to the reviewer —
the unwired baseline and the missing ASR pass — were correctly identified, disclosed everywhere, and
are charged `MINOR`. **What this round found underneath them is what a session cannot find about
itself:**

* **`M1`** — the runner does not implement `PT-048`'s **primary measure** as the pre-registration
  defines it. The substitution biases the statistic toward the claimed band, and correcting it flips
  the primary verdict from `CONFIRMED` to `REFUTED`. `BT_V20_0001.md` §6 states there was *"no other
  disagreement"* between runner and pre-registration. There was, and it decided the result.
* **`M2`** — ⭐ **found by running the independent ASR pass the submission declared it owed.** The
  committed transcript renders **`candle`** as **`handle`** four times, three of them inside the
  one-third entry rule. **`A-136` — described in the mastery report as *"the cheapest high-value
  blocker in the project"* — is an artifact of that mishearing.** The entry rule is not blocked; it
  is fully mechanical as spoken, and `PT-048` §1a excluded it from testing on the strength of the
  artifact.

⭐ **`M2` is the realised cost of the gap the submission itself declared**, which is the strongest
possible argument both for its honesty and for `D-003`.

**Everything else in this submission is strong.** Source integrity, frame naming, `Q-021`, the `M15`
attestation, the homework and the ambiguity discipline all verified from source and all hold.

---

## §0 — THE GATE V20 WAS OPENED ON, AND WHAT THIS ROUND DOES ABOUT IT

The submission's `§0` states — unprompted — that V19's `MAJOR` (item **302**) was *"fixed and closed
by the session that raised it, on owner authorisation"*, that **`D-003` is not satisfied for that fix
round**, and that *"if it reopens, this branch was authorised by a gate that would not have been
open."* **It says this while benefiting from it.** Verified from the graph:

| Fact | Verified |
|---|---|
| V19 R1 verdict | `REVISE`, **0C / 1 MAJOR / 3 MINOR / 18 NOTE**, `973e1f0`, 2026-08-14 23:02:23 |
| V19 R1's ruling | ⛔ *"`V20`'s GATE IS CLOSED under `D-024` — one `MAJOR`. It opens when actions 1–3 land **and are re-reviewed**"* |
| The fix | `213af37`, 2026-08-15 02:39:58 — **"SELF-VERIFIED AT OWNER DIRECTION"** |
| Merged | `e6b0e73` 02:41:16, then `50edf5f` 02:43:03 |
| V20 forked from | **`50edf5f`**, first content commit `bd88e99` 03:05:40 — **22 minutes after** |

**So the sequence is correct on its face and the fork is clean.** ⚠️ **The residue is real and the
submission named it:** `D-024` requires *"fixed **and re-reviewed**"*, and the re-review was done by
the raising session under owner direction rather than by an independent one.

⭐ **This round does not reopen item 302, and it does not need to.** That is V19's record, not V20's,
and this reviewer's scope is V20. **The submission's disclosure is exactly what `REVIEW_PROTOCOL.md`
§1 asks for and it is charged as nothing.** It is carried to the owner as a standing question (§6.1)
because the same shape will recur.

⚠️ **And note the consequence of this round's own findings:** V21's gate is now closed on V20's
merits, independently of anything about item 302.

### §0.1 — THE "TWO OPEN ITEMS TOUCH V20" CLAIM — CHECKED

The submission claims items **245** (V17) and **296** (V19) reach V20. **Both check out:**

* **245** corrects `A-010` to *"On a **15-minute chart**, eight"*. **V20 prints `M15` on three
  charts** — verified from the pixels below. The routing instruction is correct and useful.
* **296** is V19's §8a latency hypothesis. **V20's sweep independently produces the same transient
  shape** — verified below. Corroboration, and the submission correctly says *corroborated, not
  proven*.

---

## §1 — SOURCE MATERIAL REVIEWED, BEFORE ANY STUDENT CONCLUSION

| Evidence | What was done |
|---|---|
| The `.swf` | **SHA-256 re-computed: `96eba8c82366de12b928c900397b58104dc8ae445d4ca5851b16ad5d522a43c6`** — matches `SOURCE_MANIFEST.md` exactly. **17,724,102 bytes**, matches |
| Audio | Extracted independently. **2749.100 s**, against `frameCount/fps` **2749.333 s** and the manifest's **00:45:49**. The three agree to **0.33 s** |
| **Independent ASR** | ⭐ **A full-file `faster-whisper` / CTranslate2 `large-v3` pass (848 segments) was run BY THIS REVIEWER** — the channel the submission declares it did not run — plus four targeted multi-model decodes on the disputed passage (§3) |
| Printed slides | **Read directly from the PNGs at full resolution** — the three `M15` chart headers, the railroad-track definition, the nine-item answer key |
| Frame timecodes | **All 23 burned player readouts cropped from the pixels and read** |
| Quarantined trio | Re-hashed, re-diffed against **all 21 lessons**, and the off-by-one checked in this reviewer's own shell |
| GBP/USD M1 corpus | `mmm_lib`, DEVELOPMENT scope, both `D-031` arms, `W-A` and `W-B` |

---

## §2 — `PT-048` — RE-IMPLEMENTED FROM ITS PRE-REGISTRATION, AND THE PRIMARY MEASURE DOES NOT MATCH

`06_MANUAL_BACKTEST/scripts/rev_pt048_independent.py` was written from `PT-048` §§3–5 **before
`run_pt048.py` was opened**, and is committed so its figures are falsifiable.

### §2.1 — WHAT AGREES

The convention-light measures reproduce closely, which establishes that the leg identification is
broadly right and that the divergence below is localised:

| Cell `W-A` / arm A | Submission | **Reviewer, independent code** |
|---|---|---|
| `P2` max adverse excursion, median | 32.50 `[31.4, 33.5]` | **31.20** `[29.70, 32.35]` |
| `P3` largest one-bar counter-move, median | 23.00 `[22.4, 23.7]` | **21.70** `[20.90, 22.60]` |

⭐ **And the reviewer's `P2` reproduces the submission's central finding about it** — the maximum
adverse excursion sits **above** the band on every cell, as `BT_V20_0001.md` §2 says.

### §2.2 — ⛔ WHAT DOES NOT: THE PRIMARY MEASURE `P1`

`PT-048` §3 defines, in its first numbered line:

> **1.** A **swing pivot** is a bar whose high is the maximum (or low the minimum) of the **`±3`**
> bars around it.

and defines the primary measure as:

> **`P1`** — **PRIMARY — swing retracement.** For each **interior counter-swing** inside the leg,
> the distance from its local extreme back against the leg direction.

⛔ **`run_pt048.py` does not use that swing definition for `P1`.** `PIVOT_K = 3` is applied to the
**leg endpoints** only (`pivots()`, and two day-length guards). The interior counter-swings that
produce every `P1` value are found by a hardcoded **`±1`** test:

```python
# a counter-swing bottoms where the low is a local min of +/-1
for t in range(1, len(ll) - 1):
    if ll[t] <= ll[t - 1] and ll[t] <= ll[t + 1]:
```

**A `±1` local minimum is not a swing in this file's sense — it is any bar not lower on both sides,
which on M15 is roughly every third bar.**

### §2.3 — ⛔⛔ THE SENSITIVITY IS VERDICT-DETERMINING, AND IT RUNS TOWARD THE CLAIMED BAND

Holding **everything else identical to the runner** — same leg construction, same window, same arm,
same 20,000-draw bootstrap — and changing **only** the interior counter-swing detector:

| interior swing at | `n` | **median `P1`** | **bootstrap 95 %** | median in `[20,25]`? | **CI inside band?** | §5 verdict |
|---|---|---|---|---|---|---|
| **`±1`** — the runner's choice | 2,519 | **22.40** | `[22.00, 23.20]` | ✅ | ✅ | **`CONFIRMED`** |
| `±2` | 1,204 | 26.80 | `[25.85, 27.60]` | ❌ | ❌ | outside |
| **`±3`** — **`PT-048` §3.1's own definition** | 706 | **30.10** | `[28.70, 31.25]` | ❌ | ❌ | **`REFUTED`** |

*(The `±1` row reproduces the submission's published 22.45 / `[22.0, 23.2]` to within 0.05 pips, so
the runner is faithfully reproduced and the single variable is isolated.)*

⚠️ **Three things follow, and they compound:**

1. **The verdict flips outright.** Under the file's own swing definition the median is **30.10** —
   above the band, with an interval that **excludes** it. That is `REFUTED` by §5, not `CONFIRMED`.
2. **The bias has a direction.** `±1` admits one- and two-bar dips as "counter-swings", which are
   small by construction and drag the median **down into** `[20, 25]`.
3. ⭐ **It manufactures both halves of `CONFIRMED` at once.** `±1` inflates `n` from 706 to 2,519,
   and the bootstrap interval narrows with `n`. **`PT-048` §5 made "the interval inside the band" a
   condition precisely because item 302 charged V19 for omitting intervals** — and the `±1` choice
   is what makes that condition pass.

### §2.4 — ⛔ AND `BT_V20_0001.md` §6 SAYS THERE WAS NO SUCH DIVERGENCE

§6 is headed *"RUNNER / PRE-REGISTRATION DISAGREEMENTS"*, reports the `N1` iteration reduction, and
then states:

> **No other disagreement.** `PIVOT_K = 3`, `LEG_MIN_PIPS = 40`, `LEG_MIN_BARS = 6`, `BAND = (20, 25)`,
> the three measures, `P1` as primary … are all the values fixed in `PT-048` before the run.

**`PIVOT_K = 3` is honoured for legs and bypassed for `P1`.** The sentence is true of the leg
constructor and false of the primary measure, and `PT-048`'s governance clause — *"If the runner and
this file ever disagree, THIS FILE GOVERNS … and the disagreement is reported in `BT_V20_0001.md`"* —
was therefore exercised for the 2,000-iteration reduction and **not** for the divergence that decided
the outcome.

⚠️ **In fairness, and it matters:** `PT-048` §3 does not restate `±3` inside the `P1` row, so an
implementer could argue the interior scale was underspecified. **That reading does not rescue the
result.** If the scale was ambiguous, it was a free convention on the primary measure with a
verdict-flipping effect — which is exactly what `N3` exists to bracket, and **`N3`'s four conditions
do not include swing scale.** Ambiguous or not, it had to be declared and its sensitivity shown.

### §2.5 — THE BASELINE POINT THE SUBMISSION RAISED — UPHELD, AND CHARGED AS `MINOR`

`PT-048` §4 defines `N1` and states the scientific null in its own words: *"the null is that any
window of the same length looks the same."* **§5's verdict table never references `N1`.** The
submission reports the consequence in its verdict block (*"the `N1` matched-random baseline returns
median 23.0 … the null is not merely close — it is on the far side of the point estimate"*),
downgrades the observation to `DESCRIPTIVE`, raises its own item **320**, and puts to the reviewer
whether the `CONFIRMED` should read as a null.

⭐ **Ruling: yes. The standing result of `PT-048` is a NULL, and this reviewer records it as one.**
Reasons, in order: **(a)** §4's own statement of the null is not rejected; **(b)** §5 already has a
`FRAGILE` row that is *"reported as a null"*, so the pre-registration knows how to say this and
merely failed to attach `N1` to it; **(c)** the evidence class is already `DESCRIPTIVE` and the
verdict word should follow the evidence class; **(d)** `M1` independently removes the `CONFIRMED`.

⚠️ **This is charged `MINOR`, not `MAJOR`.** The word never travelled unqualified — checked by
`grep` across `COURSE_PROGRESS.md`, `REVIEW_INDEX.md`, `LOG.md`, the mastery report, the
interpretation and `CONCEPT_INDEX.md`: **every mention outside `BT_V20_0001.md` carries the null in
the same sentence.** Nothing downstream is corrupted and no rule was coded. **The disclosure
discipline here is the reason this is not a second `MAJOR`.**

### §2.6 — THE `N1` ITERATION REDUCTION, AND A LATENT HOLE

* **2,000 iterations against a committed 10,000** — declared at `BT_V20_0001.md` §6 and mastery §2.4,
  pre-registration not edited. ⭐ **Correct handling**, and immaterial: the baseline median over
  thousands of draws is far more precise than the 0.55-pip gap at issue. `NOTE` only.
* ⚠️ **`PT-048` §5's decision table has a hole**, reached by this reviewer's own implementation: a
  median **outside** the band whose interval **overlaps** it satisfies none of `CONFIRMED`,
  `PARTIAL`, `REFUTED` or `FRAGILE`. Same shape as V17 R1's item 259. `NOTE` — for the successor
  pre-registration, not for this one.

---

## §3 — THE MISSING ASR PASS — THIS REVIEWER RAN ONE, AND IT FOUND A `MAJOR`

The submission declares (mastery §2.2, its own item **326**): *"NO INDEPENDENT ASR PASS WAS RUN —
NOT FULL-FILE, NOT SEGMENTED … the weakest verification position in six lessons and it is OWED."*

**Rather than score the absence in the abstract, this round ran the pass** — full-file
`faster-whisper` / CTranslate2 `large-v3` over all 45:49, 848 segments.

### §3.1 — ⭐ FIRST, IT VINDICATES THE SUBMISSION'S OWN CORRECTIONS

**All four deck-settled corrections are independently confirmed**, and two of them gain material the
committed grid had lost:

| Correction | Committed grid | **Independent ASR** |
|---|---|---|
| `Shift the zone` | *"shift his own"* ×5 | ⭐ **"shift the zone"** at **4 of the 5** markers |
| `HOW or LOW` | *"The high and the weak in the low of the week"* | **"the high of the week and the low of the week"** |
| `HOD /LOD … single leg only` | *"Use to set the high or low of the day."* | ⭐ **"used to set the high or low of the day <em>as a single leg only</em>"** — the clause the grid dropped |
| `AB=CD` | *"The AV equals"* | **"The AB equals … that famous lightning bolt pattern"** |
| `Lint` | *"comes up with my friends"* | **"comes up with length, my friends"** |

⭐ **And the one claim the submission graded down for resting on audio alone is confirmed twice.**
`V20_INTERPRETATION.md` §2.1 gives **MEDIUM** confidence to *outside structure = the vector of an
M/W* because the deck prints only the Half-A-Batman. The independent pass returns it verbatim:
`[00:00:10]` *"The outside structure is the **vector side of the M or W formation**"* and
`[00:00:23]` *"the vector portion of a half of Batman, **the vector portion of M or W formation**"*.
**That grade can be raised on a second channel.** *"An absolute sign of reversal, an absolute sign of
reversal"* is likewise confirmed verbatim at `[00:01:41]`, twice in one breath, exactly as recorded.

### §3.2 — ⛔⛔ AND THEN IT FOUND `M2`: `A-136` IS AN ARTIFACT OF A MISHEARD WORD

**The committed transcript renders `candle` as `handle`.** Every noun use of *"handle"* in V20 is the
same mishearing; the two genuine verb uses (*"handled them"*, *"this bullet handles this"*) are
rendered correctly and are not affected.

| Marker | Committed grid | **Independent ASR** |
|---|---|---|
| `[00:22:41]` | *"on this **t-handle**"* | *"on this **candle**"* |
| `[00:28:36]` | *"shift his own in the next **handle**"* | *"shift his own in the next **candle**"* |
| ⭐ `[00:29:16]` | *"distance of this **handle**"* | *"Take the distance of this **candle**"* |
| ⭐ `[00:29:25]` | *"one third off the high of this **handle**"* | *"take your entry one-third off the high of this **candle**"* |
| ⭐ `[00:29:43]` | *"Take the length of the **handle**"* | *"Take the length of the **candle**"* |

**Verified to a standard well above the threshold for charging it:** four decodes — `large-v3` at
`float32` and `medium.en` at `int8`, each under **both** `vad_filter` settings, `beam_size=10`,
temperature 0 — **all four return `candle` at both critical positions. None returns `handle`.**

⛔ **`A-136` is titled *"V20's one-third entry is fully mechanical except for the word `handle`,
which is never defined."* There is no such word.** With `candle`, the rule is fully specified and
needs nothing the course has not supplied:

> `[00:29:16]` *"Take the distance of this **candle**."* → `[00:29:20]` *"Divide it by three."*
> → `[00:29:25]` *"take your entry **one-third off the high of this candle**."*
> → `[00:29:44]` *"Take the length of the **candle**. Let's say it's 100 pips…"*
> → `[00:29:50]` *"**Subtract 33 pips off the high**, a third, and put an entry right here."*

⭐ **The independent pass also recovers the worked example's closing line**, which the committed grid
garbles to *"So track 33 pitch off the high"*. **`entry = high − (range ÷ 3)` is arithmetic on one
bar.**

⚠️⚠️ **THREE CONSEQUENCES:**

1. **`A-136` should not have been opened** and must be **CLOSED as an ASR artifact**, not carried.
2. **The mastery report calls `A-136` *"the cheapest high-value blocker in the project"*** (§4.5) and
   `V20_INTERPRETATION.md`'s dimension **B** grades recognition `BLOCKED` partly on it. **It would
   have directed the next session's effort at a problem that does not exist.**
3. ⛔ **`PT-048` §1a excluded the one-third entry from testing** — *"Not the one-third entry.
   **'Handle' is undefined — `A-136`, `D-030`**"* — **so the artifact also suppressed the one V20
   rule that is mechanical enough to test.** That is the substantive cost.

⭐ **This is the mirror image of V18's `[00:19:40]`.** There a transcript defect would have entered an
inverted rule; here a transcript defect **withheld a rule that the lesson fully specifies.** Both were
invisible to every check except an independent pass over the audio.


## §4 — WHAT ELSE WAS RE-DERIVED, AND HOLDS

### ⭐⭐ `M15` IS PRINTED — VERIFIED ON ALL THREE CHARTS FROM THE PIXELS

| Frame | Header read by this reviewer | Burned timecode |
|---|---|---|
| `V20_00-04-35_…gbpchf-m15-annotated.png` | **`GBPCHF,M15`** | `04:35` ✅ |
| `V20_00-18-20_…gbpusd-m15.png` | **`GBPUSD,M15`** | `18:20` ✅ |
| `V20_00-33-15_fib-retracement-not-usdchf-m15.png` | **`USDCHF,M15`** | `33:15` ✅ |

⭐ **The claim holds, and the submission's qualification of it is the right one.** `M15` is spoken
**zero** times — verified by `grep` on the marker grid. **This is direct attestation of the charts the
instructor uses, not a spoken instruction**, and `V20_INTERPRETATION.md` §2.7 and `PT-048` §2c both
say so rather than promoting it. **Routing item 245's `A-010` remediation through this is sound.**

### ⭐ ALL 23 FRAME TIMECODES VERIFIED — 23 OF 23

`00:17 00:25 02:00 04:35 11:20 18:20 20:00 20:30 22:15 25:50 26:15 27:30 29:00 30:15 31:35 32:45
33:15 34:55 38:15 39:05 39:45 43:40 44:00` — **every one matches its filename exactly.**
⭐ **And the §8a transient claim is confirmed structurally:** exactly one frame (`00:17`) is **not**
on the 5-second grid, which is what naming from the burned value inside a decaying transient
produces and what `i × 5` naming could not. The other 22 are exact multiples of 5.

### ⭐ `Q-021` — EVERY CLAIM RE-DERIVED IN THIS REVIEWER'S OWN SHELL

| Claim | Verified |
|---|---|
| SHA-256 ×3 and byte lengths `3,177 / 1,716 / 1,257` | ✅ **exact** |
| V20 vs **V16, V17, V18, V19** | ✅ **2 / 10 / 8 differing lines against each of the four** |
| V20 vs **V15** and vs **V21** | ✅ **32 / 30 / 26 in both directions** |
| The `+4` bytes on all three files | ✅ V16–V19 are `3,173 / 1,712 / 1,253`; V20 is **exactly +4 on each** |
| Off-by-one | ✅ lesson 20's folder carries **`V21-R001`/`V21-R002`**, **`VIDEO_21_`**, and `TRANSCRIPT.md` reads *"Course Position: **Video 21 of 21**"* |
| The shipped `.jpg` | ✅ `VIDEO_21_SCREENSHOT_001_00-02-00.jpg` exists and is the only image in the folder |
| `TDI` / `shark fin` / `RSI` | ✅ **0 / 0 / 1** — and the single `RSI` is the substring inside *"**Unive**RSI**ty** of Florida"* at `[00:08:54]`, exactly as `V20_SOURCE_NOTES.md` §11 says |

⭐⭐ **The V16–V20 block closure claim is confirmed on all five members, in both directions, with no
exceptions** — consistent with this reviewer's independent normalised-hash derivation in the V18
round (item 276). **Item 254's prediction is now closed.**

### ⭐ THE COUNT DISCIPLINE ITEM 249/293/317 ASKED FOR IS BEING APPLIED

`shift his own` is claimed **×5** at five named markers. **Re-derived: exactly 5 in the body**, at
`[00:24:55]`, `[00:25:55]`, `[00:27:04]`, `[00:28:36]`, `[00:30:40]` — the fifth being the plural
*"shifts his own"*. **The list and the count are both right.** `handle` = **7** and `RSI` = **1** also
re-derived and both correctly explained rather than merely counted.

### ⭐ THE DECK-SETTLED CORRECTIONS — ALL CITED COMMITTED LINES VERIFIED

`[00:00:32]` *"Use to set the high or low of the day."* · `[00:00:48]` *"The high and the weak in the
low of the week."* · `[00:32:48]` *"The AV equals."* · `[00:43:37]` *"I hope he comes up with my
friends."* — **all four present verbatim in the marker grid as quoted.** The railroad-track
definition was read from the `26:15` pixels and matches the quoted text **word for word**, including
`Shift the zone`. ⭐ *"Slow and steady"* returns **0** occurrences in the grid, confirming §10.3's
printed-only rule.

### ⭐ THE HOMEWORK

The nine-item answer key was read from the `38:15` pixels and **matches the transcription exactly**,
including the idiosyncratic `Half –A-Batman` en-dash. The `GBPCHF` picture task is genuinely
discharged by a frame whose header this reviewer confirmed reads `GBPCHF,M15`. The flash-card item is
correctly recorded **NOT DONE with a reason** rather than manufactured. ⚠️ The 8-of-9 self-score's
ordering claim is **not verifiable from the files**, as the submission itself states — carried as a
`NOTE`, not charged.

---

## §5 — FINDINGS

### `CRITICAL` — **NONE**

Weighed and rejected. `M1` was weighed for `CRITICAL` because it inverts a headline result. It is
`MAJOR` because the observation is already classified `DESCRIPTIVE`, the verdict is flagged as
non-citable in every file that mentions it, **no rule, code or downstream artifact depends on it**,
and `REVIEW_PROTOCOL.md` §6.G's checks 15–20 are otherwise all met.

### `MAJOR`

| # | Item |
|---|---|
| **332** | ⛔⛔ **`M1` — `E18` — `PT-048`'s PRIMARY MEASURE IS NOT THE ONE THE PRE-REGISTRATION DEFINES, THE SUBSTITUTION RUNS TOWARD THE CLAIMED BAND, AND CORRECTING IT FLIPS THE VERDICT.** `PT-048` §3.1 defines a swing pivot at **`±3`**; `run_pt048.py` applies that to leg endpoints only and finds every `P1` counter-swing with a hardcoded **`±1`** local-extremum test that never references `PIVOT_K`. Holding all else identical: `±1` → median **22.40** `[22.00, 23.20]` = **`CONFIRMED`**; `±3` → median **30.10** `[28.70, 31.25]` = **`REFUTED`**; `±2` → 26.80, monotonic between them. `±1` also inflates `n` from **706 to 2,519**, narrowing the bootstrap interval — **so it manufactures BOTH conditions of `CONFIRMED`, including the interval condition `PT-048` §5 adopted in direct response to item 302.** ⛔ **And `BT_V20_0001.md` §6 states *"No other disagreement"* and cites `PIVOT_K = 3` as honoured** — true of the legs, false of the primary measure — so the pre-registration's governance clause did not fire on the divergence that decided the result. ⚠️ `N3`'s four conditions do not bracket swing scale. **Even on the charitable reading that §3 left the interior scale underspecified, an undeclared free convention on the primary measure with a verdict-flipping effect had to be declared and its sensitivity shown.** |
| **333** | ⛔⛔ **`M2` — `E01`/`E11` — `A-136` IS AN ARTIFACT OF A MISHEARD WORD, AND IT BLOCKED THE ONE V20 RULE THAT IS MECHANICAL ENOUGH TO TEST.** The committed grid renders **`candle`** as **`handle`** at `[00:22:41]`, `[00:28:36]`, `[00:29:16]`, `[00:29:25]` and `[00:29:43]` — every noun use in the lesson. **Four independent decodes (`large-v3` `float32` and `medium.en` `int8`, each under both `vad_filter` settings, `beam_size=10`) all return `candle` at both critical positions; none returns `handle`.** ⛔ `A-136` is titled *"fully mechanical except for the word `handle`, which is never defined"* — **there is no such word.** With `candle` the rule is complete: *"Take the distance of this candle … divide it by three … one-third off the high of this candle"*, worked at 100 → *"subtract 33 pips off the high"* (a line the grid garbles to *"So track 33 pitch"*). **`entry = high − (range ÷ 3)`.** ⚠️ Consequences: `A-136` must be **CLOSED as an artifact**; the mastery report's *"cheapest high-value blocker in the project"* (§4.5) and `V20_INTERPRETATION.md`'s dimension-`B` `BLOCKED` grade both rest on it; and ⛔ **`PT-048` §1a excluded the one-third entry from testing citing `A-136` by name** — so the artifact suppressed a testable rule. **Found only by the independent ASR pass the submission declared it owed (item 335).** |

### `MINOR`

| # | Item |
|---|---|
| **334** | ⚠️ **`PT-048`'s STANDING VERDICT MUST BE RECORDED AS A NULL — THE SUBMISSION'S OWN ITEM 320, RULED ON.** §4 defines `N1` and states the null in its own words; §5's table never references it; the baseline returns **23.0** against the legs' **22.45**, on the far side of the point estimate. The submission disclosed this everywhere, downgraded the class to `DESCRIPTIVE`, and asked the reviewer to rule. **Ruling: the standing result is a NULL.** `MINOR` rather than `MAJOR` because **the word never travelled unqualified** — every mention outside `BT_V20_0001.md` carries the null in the same sentence. `E25`-adjacent, but the negative result was retained, not omitted |
| **335** | ⚠️⚠️ **THE MISSING INDEPENDENT ASR PASS — THE SUBMISSION'S OWN ITEM 326, RULED ON, AND ITS COST IS `M2`.** No pass of any kind was run; the transcript corrections rest on the printed deck plus internal consistency. ⭐ **The deck is Tier 2 and the ASR would have been Tier 3, so the four corrections V20 actually makes are better evidenced than an ASR could have made them** — the exposure is what was *not* looked for. **This reviewer ran the full-file pass the submission owed** (§3). ⭐ **It confirmed all four deck-settled corrections and upgraded an audio-only claim — and it found `M2`.** Charged `MINOR` rather than `MAJOR` **only because `M2` already carries the substance**; charging both would double-count one root cause. **Discharged for V20 by this round. It must not become the norm, and `M2` is the argument.** |

### `NOTE` — no action required

| # | Item |
|---|---|
| **336** | ⭐ **THE GATE DISCLOSURE IS EXEMPLARY AND IS CHARGED AS NOTHING.** The submission states unprompted that V19's `MAJOR` was closed by the session that raised it, that `D-003` is not satisfied for that round, and that *"if it reopens, this branch was authorised by a gate that would not have been open"* — **while benefiting from it.** Timeline verified from the graph. This round does not reopen item 302; it carries the shape to the owner (§6.1) |
| **337** | ⭐ **SOURCE INTEGRITY EXACT.** SHA-256 `96eba8c8…d522a43c6` and 17,724,102 bytes re-computed and matching; audio **2749.100 s** against `frameCount/fps` **2749.333 s** and the manifest's **00:45:49** — three independent measures agreeing to **0.33 s** |
| **338** | ⭐ **ALL 23 FRAME TIMECODES VERIFIED 23/23 FROM THE PIXELS**, and the §8a transient is confirmed structurally: exactly one frame (`00:17`) sits off the 5-second grid, which burned-value naming produces and `i × 5` naming cannot. Item 296 is corroborated from a second sweep, and the submission correctly says *corroborated, not proven* |
| **339** | ⭐⭐ **`Q-021` FULLY RE-DERIVED — hashes, byte lengths, the `+4`, the `2/10/8` against all four block members, the `32/30/26` against both neighbours, the `V21-`/`VIDEO_21_`/*"Video 21 of 21"* off-by-one, and the shipped `.jpg`.** The V16–V20 block closure is confirmed on all five members in both directions. **Item 254's prediction is closed** |
| **340** | ⭐⭐ **`M15` VERIFIED ON ALL THREE CHART HEADERS FROM THE PIXELS**, and spoken **zero** times — so the submission's framing (attestation of the instructor's charts, not a spoken instruction) is exactly right, and it is not promoted beyond that anywhere |
| **341** | ⭐ **THE COUNT DISCIPLINE ASKED FOR BY ITEMS 249 / 293 / 317 IS BEING APPLIED AND IS CORRECT.** `shift his own` ×5 re-derived at the five named markers (the fifth is the plural form); `RSI` = 1 correctly explained as the substring in *"Unive**RSI**ty"*. ⚠️ **The one count that is right about its arithmetic and wrong about its object is `handle` = 7** — the census is correct, but five of the seven are `candle` (item 333). **The discipline caught the substring case and could not catch the homophone**, which is precisely what an independent audio channel is for |
| **342** | ⭐ **THE DECK-SETTLED CORRECTIONS ALL VERIFY.** Four cited committed lines present verbatim; the `26:15` railroad-track definition matches the quoted text word for word from the pixels; *"slow and steady"* returns 0 in the grid, confirming the printed-only rule at §10.3 |
| **343** | ⭐ **`P2` AND `P3` REPRODUCE ON INDEPENDENT CODE** — reviewer `P2` median **31.20** against the submission's 32.50, `P3` **21.70** against 23.00, **and the submission's central `P2` finding reproduces**: the maximum adverse excursion sits above the band on every cell. **This is what localises `M1` to `P1` rather than to the leg construction** |
| **344** | **THE `N1` ITERATION REDUCTION IS CORRECTLY HANDLED.** 2,000 against a committed 10,000, declared at `BT_V20_0001.md` §6 and mastery §2.4, pre-registration not edited. **Immaterial** — the baseline median's precision far exceeds the 0.55-pip gap at issue |
| **345** | ⚠️ **`PT-048` §5's DECISION TABLE HAS A HOLE**, reached by this reviewer's own implementation: a median **outside** the band whose interval **overlaps** it satisfies none of the four branches. Same shape as V17 R1's item 259. For the successor pre-registration |
| **346** | ⭐ **THE HOMEWORK IS SOUND.** Nine-item answer key matches the pixels exactly, en-dash included; the `GBPCHF` task discharged by a frame whose header reads `GBPCHF,M15`; the flash-card item recorded **NOT DONE with a reason**; the deliberate omission of a data block explained rather than left as a gap. ⚠️ The 8-of-9 ordering claim is unverifiable from the files, as the submission states |
| **347** | ⭐⭐ **CALIBRATION — THE SUBMISSION FOUND, DISCLOSED AND SELF-CHARGED MOST OF ITS OWN DEFECTS.** Items **320** (the baseline), **326** (the ASR gap), the `N1` reduction, the self-scored recall test and the gate residue were all raised by the session against itself, prominently and in the ledgers rather than in footnotes. ⭐ **`CONCEPT_INDEX.md` was updated — V18's item 264 applied.** ⭐ **The `§9` two-pass order was followed.** ⚠️ **`M1` and `M2` are both things a session cannot find about itself** — one needs an independent re-implementation, the other an independent ear. **That is the argument for `D-003`, not against this submission's honesty**, and the submission had already named the gap that produced `M2` |

---

## §6 — REQUIRED CORRECTIONS

1. ⛔ **Item 332 (`MAJOR`).** Change `run_pt048.py`'s `P1` interior counter-swing detector to use
   `PIVOT_K`, re-run, and republish `BT_V20_0001.md` §§0/2/3 with the corrected primary figures.
   **Correct §6's *"No other disagreement"* sentence** to record the divergence — the
   pre-registration governs and is **not** edited. **State the resulting verdict on the corrected
   primary cell.** If the implementer maintains `±1` is a defensible reading of §3, report **both**
   scales side by side and apply §5 to the pre-registration's own `±3`, with the sensitivity shown as
   `N3`-style bracketing. **This round's figures are in `rev_pt048_independent.py` and are
   re-runnable.**
2. ⛔ **Item 333 (`MAJOR`).** **Close `A-136` as an ASR artifact** — the word is `candle`. Correct the
   five markers in `V20_SOURCE_NOTES.md`, `V20_INTERPRETATION.md`, `V20_MASTERY_REPORT.md` §4.5 and
   `AUTOMATION_AMBIGUITIES.md`, recording the correction rather than editing the grid (the transcript
   body is byte-for-byte source and stays as it is, annotated). **Re-grade `V20_INTERPRETATION.md`
   dimension `B`**, which cites `A-136` as part of its `BLOCKED` basis. **Record that `PT-048` §1a's
   exclusion of the one-third entry no longer has a basis** — the rule is `entry = high − (range ÷ 3)`
   and is testable. ⚠️ **Do not retro-fit it into `PT-048`**; it is a candidate for a successor test,
   pre-registered in the normal way.
3. **Item 334.** Record `PT-048`'s standing result as a **NULL** in `BT_V20_0001.md` §0,
   `REVIEW_INDEX.md` item 320, `LOG.md` and the mastery report. Keep *"`CONFIRMED` by the rule as
   written"* as historical fact; it must not be the standing verdict.
4. **Item 335.** No action for V20 — the pass was run in this round and is reported at §3. **The
   requirement stands for V21**, and item 333 is the argument for it.

**Not required:** items 344–347 and the §5 decision-table hole are for the successor
pre-registration, not for this lesson.

---

## §7 — REVIEWER QUESTIONS FOR THE OWNER

1. ⚠️ **The `SELF-VERIFIED AT OWNER DIRECTION` route is now load-bearing for a gate.** V19's `MAJOR`
   was closed by the session that raised it, and V20 forked on the strength of it. **The submission
   flagged this itself.** `D-024` says *"fixed **and re-reviewed**"* and `D-003` reserves closure to an
   independent reviewer. **Recommendation: either a numbered decision that authorises self-verified
   closure of a `MAJOR` for gate purposes, or a rule that a `MAJOR` needs an independent round.** The
   current position is that the exception exists in practice but not in the ledger.
2. **Should the baseline be a mandatory verdict condition in every `PT-` pre-registration?** Item 333
   is the second time a pre-registration has defined the right null and not scored it. A standing
   clause in `BACKTEST_EVIDENCE_STANDARD.md` would close the class rather than the instance.
3. **A convention-sensitivity requirement for primary measures.** `M1` would have been caught before
   the run by a rule that every free parameter in the primary measure is either fixed by the
   pre-registration or reported at three settings. `N3` does this for boundaries in `PT-046` and for
   arms/windows here — **it does not cover measure internals.**

---

## §8 — ADVANCEMENT

```text
LESSON: V20
DECISION: REVISE
CONFIDENCE: HIGH

CRITICAL ISSUES: none

MAJOR ISSUES:
- M1  E18  PT-048's primary measure P1 uses a +/-1 interior swing detector while
           PT-048 §3.1 defines a swing pivot at +/-3. Correcting it moves the
           primary median from 22.40 [22.00,23.20] to 30.10 [28.70,31.25] and
           flips the verdict CONFIRMED -> REFUTED. It also inflates n from 706
           to 2,519, narrowing the very interval §5 made a condition.
           BT_V20_0001.md §6 records "no other disagreement".
- M2  E01  A-136 is an artifact. The committed grid renders "candle" as
           "handle" at all five noun positions; four independent decodes across
           two models and both VAD settings return "candle", none "handle". The
           one-third entry rule is fully mechanical as spoken --
           entry = high - (range / 3) -- and PT-048 §1a excluded it from
           testing citing A-136 by name.

REQUIRED ACTIONS:
1. Fix the P1 detector to use PIVOT_K, re-run, republish BT §§0/2/3, correct
   §6. Do not edit the pre-registration.                                 (332)
2. Close A-136 as an ASR artifact; correct five markers in four files;
   re-grade interpretation dimension B; record that PT-048 §1a's exclusion
   of the one-third entry no longer has a basis.                         (333)
3. Record PT-048's standing result as a NULL in four files.              (334)
4. No action - the owed ASR pass was run in this round.                  (335)

ADVANCEMENT: NOT AUTHORIZED
```

⛔ **`V21`'s GATE IS CLOSED** under `D-024` — two `MAJOR`s. It opens when actions 1–2 land **and are
re-reviewed**. ⭐ **Action 1 changes one constant and re-runs a 90-second script; action 2 corrects
one word in four files and closes a record.** Neither requires re-capturing, re-transcribing or
re-testing anything. **This is a short remediation round.**

**V20 STATUS: `IN REMEDIATION`.** Not `COMPLETE` until items 332–335 are applied and independently
verified.

---

## §9 — REVIEWER'S OWN DISCLOSURES

1. **Worktree isolation honoured.** All work in `MMM-Agents-v20-review` on branch `review/v20`,
   created from `2ab5e83`. The shared checkout was read only for Git-ignored source media and the
   quarantined corpus, and nothing in it was written.
2. **The dataset was symlinked, not copied**, into this worktree's Git-ignored
   `06_MANUAL_BACKTEST/datasets/` so `mmm_lib`'s path resolution would find it. Not committed.
3. **Order of work.** Source evidence first. `PT-048` was re-implemented **from the pre-registration
   before `run_pt048.py` was opened**; the runner was read only afterwards, to locate the divergence
   that the independent figures had already exposed.
4. ⚠️ **My own first implementation initially tripped the `W-D`-style holdout seal on arm B** by
   asserting on the full load rather than on the window actually read (`I-010` Q2). **Corrected in my
   code, disclosed here**, and it does not affect any figure above — `W-A` and `W-B` are 2014–2015.
5. **Reviewer code is committed** as `rev_pt048_independent.py` so every figure in §2 is falsifiable.
6. **Item numbering.** Items **332–347** allocated against integration at `50edf5f`, where **317** was
   the highest item before `video/v20` allocated **318–331**. Re-check at merge-back per `D-047`.
