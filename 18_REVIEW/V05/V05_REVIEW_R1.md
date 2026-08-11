# V05 — INDEPENDENT REVIEW R1

| Field | Value |
|---|---|
| Lesson | V05 — `Bootcamp1 Wk2 032512 Part3 (68mins).swf` |
| Review round | R1 |
| Reviewed | 2026-08-11 |
| Reviewer | Independent Reviewer / Teacher Agent, fresh session (`D-003` satisfied — this session authored no V05 artifact) |
| Protocol | `00_SYSTEM/REVIEW_PROTOCOL.md` (17 dimensions, error taxonomy, severity) |
| Standard | `00_SYSTEM/MASTERY_STANDARD.md`; `DECISIONS.md` D-001 … D-025 |

---

## EXECUTIVE BLOCK

```text
LESSON:     V05
DECISION:   REVISE
CONFIDENCE: HIGH

CRITICAL:   0
MAJOR:      0
MINOR:      6   (M1 … M6, all open)
NOTE:       5   (N1 … N5)

ADVANCEMENT: AUTHORIZED — the V06 gate OPENS under D-024
             (0 CRITICAL, 0 MAJOR). The six minors are deferred
             and still owed before V05 can reach COMPLETE.
```

**V05 does not reach `COMPLETE` this round.** No finding alters any conclusion in any V05
artifact, and none could: V05 yields no doctrine, so there is no rule for a defect to
corrupt. All six minors are precision and documentation defects.

---

## 0. REPOSITORY STATE — VERIFIED BEFORE ANYTHING ELSE

This session was told V05 may have been produced by **multiple concurrent duplicate
sessions**, with a risk of duplicated or conflicting committed content. That account was
checked against the repository rather than taken on trust, and it is **partly wrong in a way
worth recording**.

`git log --oneline -20` and `git status` at review start:

| Finding | Evidence |
|---|---|
| `HEAD` is `b4b690b`. **There are no commits beyond it.** | `git log` |
| The V05 pipeline is exactly **9 commits**, `a34d2f2` → `b4b690b`, in correct protocol order: source notes → screenshots → screenshots (2×) → notes §9 → homework → interpretation → ambiguities → contradictions → mastery report | `git log`, `git show --stat` on all nine |
| **The two findings described to this session as possible separate additions are inside the main pipeline, not extra commits.** The `Zen_man` finding and the on-screen taskbar date are both in `8223224`, the first screenshots commit | `git show --stat 8223224`; `04_SCREENSHOTS/V05/INDEX.md` §§ "THE ZEN_MAN FINDING", "THE SESSION DATE IS ON SCREEN" |
| **No duplicate, conflicting, or orphaned V05 content anywhere.** `A-001`…`A-049` are contiguous with **zero duplicate headings and zero gaps**; `C-001`…`C-005` likewise; no duplicated V05 blocks in `LOG.md` or `CHANGELOG.md` | scripted heading scan; duplicate-line scan |
| `validate_project.py`: **97 passed, 0 warnings, 0 failures** | run this session |
| One untracked file: `05_HOMEWORK/V02/measure_usdchf_week.py` | This is **`REVIEW_INDEX.md` open item 13**, deliberately left in place by every session since V02 R2. Correct; not concurrent-session debris. Left untouched by this round |

> ### ⚠ ANSWER TO THE EXPLICIT QUESTION: **NO DUPLICATION OR COLLISION DAMAGE EXISTS.**
>
> Whatever the other sessions did, **nothing of theirs reached this repository.** There is
> exactly one V05 pipeline, it is internally consistent, and it needs no cleanup. The
> registers were audited specifically for the failure modes concurrency would produce —
> duplicate `A-xxx`/`C-xxx` IDs, re-used numbers, doubled evidence rows, conflicting status
> blocks — and all are clean. **No data-integrity remediation is required.**

---

## 1. SOURCE REVIEWED FIRST (`REVIEW_PROTOCOL.md` §3)

Source before student work, to avoid anchoring:

1. `02_TRANSCRIPTS/V05/V05_TRANSCRIPT.md` — full header, coverage block, speaker section, transcription notes, and the verbatim body scanned programmatically end to end.
2. The 30 curated frames + 5 `hires/` re-renders — **opened and magnified**, not read about.
3. `00_SYSTEM/QUARANTINE_REGISTER.md` Q-005 and all 21 quarantined `RULES.md` at population scale.
4. `DECISIONS.md` D-001 … D-025 (D-018, D-019, D-024, D-025 in full); `REVIEW_INDEX.md` in full, including open items 1–40.

Student artifacts were read afterwards.

### 1.1 The transcript's self-report reproduces exactly — every component

Re-derived this session by an independent marker scan (lines fully matching `^\[\d\d:\d\d:\d\d\]$`):

| Claim | Stated | Measured | |
|---|---|---|---|
| Markers | 1,353 | **1,353** | ✅ |
| Distinct | 1,353 | **1,353** | ✅ |
| Decreasing transitions | 0 | **0** | ✅ |
| Same-second adjacent pairs | 0 | **0** | ✅ |
| Largest gap | 13 s at `[00:08:38]`, `[00:19:38]` | **13 s, at exactly those two markers** | ✅ |
| Final entry | `[01:08:20]` | **`[01:08:20]`** | ✅ |

**This is the first transcript in the project to assert strict monotonicity and be right.**
V03's `COVERAGE` block was charged at R1 for exactly this claim where it was false, and took
three rounds to close (open item 19). V05's block not only states the true property, it
**names the prior failure and tells the reader how to reproduce the measurement**. The
`E20` monotonicity class remains empty project-wide.

### 1.2 Speaker identification — the load-bearing fact, independently confirmed

V05's central claim is that it is **100% guest**, by a **third** voice. Verified:

| Claim | Measured |
|---|---|
| 21 third-person references to Steve | **`Steve` occurs exactly 21× in the verbatim body** ✅ |
| The presenter speaks of Zen in the third person | **`Zen` occurs 2×**, at `[00:01:41]` and `[00:30:32]`, both read in context ✅ |
| `DMR` count, corrected 12 → 9 during the pass | **exactly 9** ✅ |
| `TDI` occurs 6× and is never defined | **exactly 6**, all read in context — no inputs, periods, bands or decision rule ✅ |

The argument is sound and the strongest limb is the one the screenshot index added, not the
transcript's: ***"even I can't get that"* `[00:01:41]` cannot be said by Zen about Zen.**
That is a genuine inference and it is correctly labelled **provenance, not evidence**
(`D-025` consequence 4). Nothing in V05 depends on it.

### 1.3 Fabrication quarantine — discharged at population scale, per open item 33

Open item 33 permits the per-lesson `RULES.md` audit to be discharged in one step. Verified
this session across **all 21** quarantined files, not just V05's:

| Template marker | Population |
|---|---|
| Rule 1 quote at `[00:05:00]` | **21 / 21** |
| Rule 2 quote at `[00:18:00]` | **21 / 21** |
| Exactly two rules | **21 / 21** |
| `NUMERICAL PARAMETERS` block hash | **one hash, 21 / 21** |

V05's file names its rules `V06-R001` / `V06-R002` — consistent with the *"Video 06 of 21"*
mislabel the adopted transcript dropped from its header. Q-005's cross-check against real
audio was re-read **word for word** and every claim holds:

- `[00:05:00]`, `[00:02:00]`, `[00:04:00]`, `[00:22:00]` — **none is a marker in this transcript.** ✅
- `[00:04:57]` = *"You need to know how to use scripts and customize them to your settings using that editor."* ✅ exact
- `[00:05:05]` = *"You need to know how to mock up your charts…"* ✅ exact
- `[00:18:00]` = *"We have our levels."* ✅ exact — and it is not a stop rule
- `5/13` 0, `5 EMA` 0, `13 EMA` 0, `800` 0, `EST` 0 — **all re-measured, all zero** ✅

**Q-005 is correct and the quarantine is complete.** Q-005's own measurement note (hash the
block, not the tail) is a useful trap-avoidance record; this session's independent hash gave
one hash under both slices, which does not contradict it.

### 1.4 Screenshot claims verified against the pixels, not the prose

| Claim | Verdict |
|---|---|
| `Zen_man` / `System Folder` in the MT4 Save As dialog | ✅ **CONFIRMED** — opened at 2×, unambiguous, alongside `Libraries` and `Homegroup`, filename `M Pattern`, type `GIF File (*.gif)` |
| Windows taskbar clock reads **`10:31 PM  3/25/2012`** | ✅ **CONFIRMED** — bottom-right of frame 26. **This is real, independent, in-recording corroboration of the session date, which until now rested on the filename `032512` alone.** A genuinely valuable find |
| Frame 26 status bar: `4 Majors`, `2012.01.04 01:15`, `O: 1.56413 H: 1.56418 L: 1.56374 C: 1.56381 V: 352` | ✅ **CONFIRMED** — read independently; the `L ≤ C ≤ O ≤ H` ordering check the index cites as its own guard holds |
| Frame 26 title bar `67342442: FXDD - MetaTrader - Demo Account - [GBPUSD,M15]` | ✅ **CONFIRMED** |
| `A-018` `R = 24.6`, `R = 18.8`; `A-047` `A1`/`A2` as yellow-boxed labels | ✅ **CONFIRMED** on the 2× MM-full-cycle frame, together with `BIG M`, `M`, `SS`, `RR`, `Level 1/2/3`, `Enter` |
| `A-043`: MT4 carries two text objects, icons `A` (`Text`) and `T` (`Text label`) | ✅ **CONFIRMED** at 2× — **Available:** `… Rectangle, Triangle, Andrews' Pitchfork, Cycle Lines, `**`T Text label`**; **Selected:** `Crosshair, Vertical Line, Horizontal Line, Trendline, Ellipse, `**`A Text`**`, Arrows`. Exactly as described |

---

## 2. CITATION AND QUOTATION AUDIT

Performed mechanically over every V05 artifact.

### 2.1 Timestamp existence — 356 citations

| File | Citations | Distinct | Non-markers |
|---|---:|---:|---|
| `V05_SOURCE_NOTES.md` | 297 | 247 | 4 |
| `V05_INTERPRETATION.md` | 23 | 23 | 2 |
| `04_SCREENSHOTS/V05/INDEX.md` | 10 | 7 | **0** |
| `V05_HOMEWORK.md` | 17 | 16 | 1 |
| `V05_MASTERY_REPORT.md` | 9 | 9 | **0** |

**Six of the seven non-markers are legitimate and correctly labelled cross-lesson
references** — `V04 [00:15:05]`, `V02 [00:20:37]`, `V04 [00:26:56]`, `V04 [00:18:24]` — each
carrying its lesson tag. Only **one** is a defect (`M1`).

### 2.2 Quotation fidelity — 92 marker-cited fragments re-matched verbatim

Every quote presented in the canonical `*"…"* \`[marker]\`` form was normalised and matched
against the transcript body, then locality-checked against the cited marker's neighbourhood.
**90 of 92 pass exactly.** One is `M3`; one is `N2` (a disclosed bracket).

**This is a strong result and it continues V04's trend.** `E11` — the project's historic
dominant defect, de-escalated at V04 R1 — **does not recur as a class**: `M1` and `M2` are
two isolated instances against 356 citations, not a pattern.

---

## 3. HOMEWORK — THE DATA QUESTION, ANSWERED DIRECTLY

### 3.1 The data is read from TradingView's Data Window text. It is not pixel-derived.

`scripts/tv_harvest_v05.mjs` was **read line by line**. It drives synthetic mouse moves
across the price pane and after each move parses the Data Window panel's `innerText` for
`Date`, `Time`, `Open`, `High`, `Low`, `Close`. **No pixel is sampled and no colour is
tested anywhere in the file.** The header comment says so and the code matches the comment.

This is the correct method and it is the direct remedy for V02's `MAJOR` (`E06`/`E19`),
where a price line drawn in the bullish-candle colour corrupted a pixel read.

### 3.2 Every committed figure recomputed from the JSON — all reproduce

| Figure | Stated | Recomputed |
|---|---|---|
| Week bars | 480 / 480 / 480 / **476** | ✅ identical |
| Total bars / transitions | 1,916 / 1,912 | ✅ identical |
| Continuity | **1,912 / 1,912, zero breaks, all four pairs** | ✅ **zero breaks**, recomputed at `c[i] == o[i+1]` |
| `by_day` table (§2.2) | 12/96/96/96/96/84, USDCHF 8 | ✅ identical for all four pairs |
| EURUSD | H `1.15808` 08-07 12:45 · L `1.15003` 08-03 15:30 · 80.5 pips | ✅ exact, to 0.1 pip |
| GBPUSD | H `1.35089` 08-07 13:15 · L `1.34175` 08-03 18:00 · 91.4 pips | ✅ exact |
| USDJPY | H `158.572` 08-07 00:45 · L `155.228` 08-03 00:45 · 334.4 pips | ✅ exact |
| USDCHF | H `0.81356` 08-06 15:45 · L `0.80552` **08-02 22:00** · 80.4 pips | ✅ exact |
| Feed / full harvest | FXCM, 687 bars per pair | ✅ exact |
| Last bar before week open | `2026-07-31 20:45`, all four | ✅ exact |
| Scoped 3-of-4: high Friday, low Monday | — | ✅ EURUSD/GBPUSD/USDJPY all Fri/Mon; **USDCHF is Thu/Sun and is correctly excluded** |

**The V04 defect is genuinely fixed at source, and the fix is the right one.** V04's
harvesters captured `O H L C` only, so week boundaries had to be *inferred* from bar cadence
— the inference that broke on USDCHF (open item 25). Here each bar carries its own
timestamp, so the boundary is a lookup. **The same USDCHF anomaly recurs and is caught by
the tooling instead of by a reviewer**: 476 = 480 − 4, the missing hour visible directly in
the data. That it independently reproduces V04's corrected 476 on a different week, a
different feed and a different method is a real cross-session replication, and the *cause* is
now visible rather than reconstructed.

**The boundary-limited USDCHF week low is disclosed, not smoothed.** `0.80552` is the open
of the pair's first available bar; the file says so, says the true low could be lower on
another feed, and excludes the pair from every conclusion that depends on it. That is the
correct handling and it is volunteered, not extracted.

### 3.3 The D-025 line is held in the artifact itself

The homework's most impressive property is that it **performs the descriptive half of the
assignment and visibly declines the normative half**, with a table for each. Day separators,
week extremes, body-to-body boxes and flashcard crops are marked; levels, anchor, cycle
labels, entries, stops, targets and the three-day claim are not — and the rendered images
carry their own footer, *"No Level/anchor/entry marked: guest-normative, excluded under
D-025,"* so a frame that escapes the directory still carries its provenance. **A homework
artifact that marked levels would have looked more like the lesson and been wrong.**

Dimension G of `REVIEW_PROTOCOL.md` (manual-backtest procedure) is **not engaged** — no
trades, no entries, no outcomes, therefore no hindsight surface. Dimension H (hindsight /
lookahead audit) returns **nil**: the flashcard crops deliberately withhold the future half
of the chart, which is the opposite of contamination.

---

## 4. FINDINGS

### MINOR

#### M1 — the same quote is cited at two different wrong timestamps, neither a marker (`E11`)

*"I use the trend line. I use E and I use the box."* is at **`[00:57:35]`–`[00:57:36]`**.

| File | Cited as | Is it a marker? |
|---|---|---|
| `V05_SOURCE_NOTES.md` §3b (`A-043` note) | `[01:07:36]` | **No** — `[01:07:35]` carries *"people that haven't done the homework yet"* |
| `AUTOMATION_AMBIGUITIES.md` `A-043` evidence table | `[01:01:35]` | **No** |

The quotation itself is accurate and the words exist; only the citations are wrong, and they
are wrong **two different ways in two files**, which means neither was checked against the
other. **`A-043`'s closure does not rest on this row** — it rests on the toolbar dialog,
which this session verified at the pixel level — so no conclusion moves.

**Required:** correct both to `[00:57:35]`–`[00:57:36]`.

#### M2 — a citation off by one marker (`E11`)

`AUTOMATION_AMBIGUITIES.md` `A-039` extension row cites `[00:36:03]` for *"looking for
shorts, the trend line goes on the top and on the top"*. `[00:36:03]` reads *"I can start
drawing my trend line."*; the quoted words are at **`[00:36:05]`**.

This is open item 7's class exactly — the marker of the passage rather than of the sentence's
first words. It resolves to adjacent content and misleads no one.

**Required:** correct to `[00:36:05]`.

#### M3 — a smoothed quotation (`E01`)

`V05_SOURCE_NOTES.md` §4b quotes:

> *"the second leg of that pattern, that three hits to the high…"* `[00:13:05]`

The transcript reads: *"So the consolidation and level three **second leg of that pattern,
that three hits to the** high."* **"level three" has been silently replaced by "the".**

Same class as V04's `M2`, and again it lands in the *supporting* prose rather than in the
notes proper. It is a small change with a real edge: the passage is the file's evidence for
the **level↔day relabelling**, and the excised words are a level number.

**Required:** restore the literal wording, or mark the elision explicitly.

#### M4 — three V05 files disagree about V05's own evidence order (`E20`)

| File | Says |
|---|---|
| `04_SCREENSHOTS/V05/INDEX.md` § "⚠ PROCESS DEVIATION, DISCLOSED" | *"**That order was not preserved for V05.**"* … *"the audio-only / visual-corroborated separation is **weaker for V05 than for V01–V04**"* |
| `V05_INTERPRETATION.md` header table, line 12 | *"**V05 restored the recipe's evidence order that V03 and V04 deviated from**"* |
| `V05_SOURCE_NOTES.md` process disclosure | Order followed for §§1–8, with **one** disclosed pre-sweep sanity frame |

The first two are **opposite claims about the same fact**, and the interpretation's is the
self-flattering one. The source notes' version is the careful and probably correct one.

This matters more than a wording slip because the evidence order is *the* mechanism by which
a reader judges which V05 conclusions survive on audio alone. **The honest disclosure exists
and is prominent** — `INDEX.md` states the deviation, its cause and its consequences without
being asked, which is exactly right — so a reader does get the truth. But the interpretation
contradicts it in the one line a skimmer reads first.

**Required:** reconcile line 12 of `V05_INTERPRETATION.md` to `INDEX.md`'s disclosure. Do
not weaken `INDEX.md`.

#### M5 — `A-039` still points at V05 as the future candidate (`E20`)

`A-039` reads *"The promised TDI lesson. V05 (`Bootcamp1 Wk2 032512 Part3`) is the next
candidate."* V05 has now been studied and has **not** defined TDI. The line describes a
state of the world that is no longer true.

**Eighth instance of the status-staleness class** (open item 14) and the only one this
round — see `N5`.

**Required:** update to name V06 (or "any later lesson") as the next candidate, and record
that V05 was checked and produced a displayed name but no definition.

#### M6 — an unrecorded oscillator sub-panel in a curated frame (`E20`)

Frame 26 (`V05_00-40-04`) renders a **multi-line oscillator sub-panel beneath the price
pane** — the same object family the index records carefully on frames 19, 20 and 21. The
frame-26 row describes the frame in unusual detail, down to the taskbar clock and a nine-times
magnified status bar, and **does not mention the sub-panel at all.**

This is precisely V04 review `M6`, whose precedent is binding: a visible TDI panel in a
curated frame is recorded, scoped *"displayed, not taught."* This session magnified the
panel's header and confirms it is **at the edge of legibility and should not be transcribed**
— which is the same call frame 27's OHLC row already gets, and gets right.

**Required:** add the sub-panel to frame 26's row, scoped *"displayed, not taught; header
not legible at this resolution"*, and add the frame to `A-039`'s extension row. **It does not
narrow `A-039`** — guest material, `D-025`.

### NOTE

- **`N1` — the six record extensions are physically separated from the records they extend.**
  They live in a `V05 EVIDENCE ADDED TO EXISTING RECORDS` block at the foot of
  `AUTOMATION_AMBIGUITIES.md`. **This follows V02's precedent exactly** and the block is
  excellent — `A-020`, `A-039`, `A-032`, `A-018`, `A-010`/`A-011`, `A-019`, each with its
  effect stated and each explicitly *extended, not narrowed*. **Not charged.** But a reader
  opening `A-039` or `A-020` sees no V05 evidence and no pointer to the block. A one-line
  back-reference in each extended record would close the gap. *(This reviewer initially
  scored the extensions as missing and was wrong; the block is real and the mastery report's
  "six existing records extended" is accurate.)*
- **`N2` — a bracket that substitutes rather than inserts.** *"candles with pins are stop
  [hunt] moves"* renders an ASR reading of *"stop **and** moves"*. The bracket signals
  editorial intervention, so nothing is hidden, but the project's convention elsewhere is
  that brackets *add*. Worth one line in `TRANSCRIPTION NOTES`.
- **`N3` — §2.2's `9` and `5` bar counts reproduce only on an inclusive endpoint.** The
  "20:00–23:00 window" gives 8 and 4 exclusive, **9 and 5 inclusive** — the stated figures.
  The difference is 4 either way and the conclusion is identical. No action; recorded because
  a future session re-deriving it will hit the same ambiguity.
- **`N4` — the manual-backtest debt is now FIVE lessons deep** (open items 21, 24). V05's
  dimension-G `NOT APPLICABLE` is upheld below, but it must **not** be read as retiring the
  backlog. The trigger is unchanged: **when TDI is taught, the hidden-future backlog becomes
  dischargeable and must be discharged.**
- **`N5` — the status-block staleness class did NOT recur, for the first time in the
  project's history.** All four status blocks were checked against their own file contents
  and **all four are current**: `AUTOMATION_AMBIGUITIES.md` (49 records, 5 lessons),
  `CONTRADICTIONS.md` (5 records, 5 lessons), `COURSE_PROGRESS.md`, `REVIEW_INDEX.md`
  (open items 35–40 added in the same commit as the mastery report). `M5` is a stale
  *pointer inside a record*, not a stale status block. **Open item 14 has been the project's
  most persistent weakness across six occurrences; this is the first clean round.** Worth
  carrying to `CUMULATIVE_25.md` as evidence the discipline took hold without the
  `validate_project.py` guard having been built.

---

## 5. RULINGS THE STUDENT ESCALATED

### 5.1 Open item 40 — `A-043`'s closure: **AFFIRMED**

The student closed `A-043` on guest evidence and invited a reviewer to downgrade it to
`EXTENDED, NOT CLOSED`. **I affirm the closure.**

The evidence was verified at the pixel level and is exactly as described: MT4 carries two
text objects, `Text` with a plain letter **`A`** icon and `Text label` with a boxed **`T`**.
*"Just use the one that says A. Don't use the one that says T."* therefore means **use
`Text`**, and the transcript's *"one that says E"* is an ASR mishearing of *"A"*.

**Why `D-025` does not bar it, stated as a class rather than as a one-off excuse.** D-025
bars guest evidence from closing records *about the method*, because doing so would give a
guest's normative claims operative standing. `A-043` is not about the method. Its subject is
**which button this speaker's own mouth referred to** — a question about *this lesson's ASR*
and *a platform artifact*, answered by a screenshot of a dialog box. Closing it promotes no
guest statement into doctrine, resolves nothing about trading, and nothing downstream depends
on it.

**Ruling, and the boundary that goes with it:** a record whose **subject is a guest's own
utterance or a platform artifact, and not the method**, may be closed on descriptive guest
evidence. A record about the method may not be, ever, regardless of how clear the guest
evidence is. `A-020`, `A-039`, `A-032`, `A-018`, `A-010`/`A-011` and `A-019` sit on the far
side of that line and the student correctly left every one of them open.

> **Owner action recommended:** record this carve-out as a numbered refinement of `D-025`.
> D-025's own "Alternatives considered" rejected *case-by-case adjudication with no standing
> rule*; the student's per-record justification is exactly that, even though it reaches the
> right answer. Writing the class down converts a good judgement call into an enforceable
> rule. **This is a recording step, not a re-litigation** — the finding stands either way.

### 5.2 Open item 36 — dimensions B, F and G, and the third disposition

**The escalation is correct and the student was right to refuse to settle it alone.** V05 is
a case `D-018` and `D-019` genuinely do not contemplate: the lesson **states** several
testable-shaped rules and they are **withheld by decision**, permanently.

| Dimension | Student's grade | Ruling |
|---|---|---|
| **G** — manual backtesting | `NOT APPLICABLE` (purposive reading, flagged) | ✅ **UPHELD.** `DEFERRED` would be false — deferral implies the work becomes possible later, and **no future lesson makes a V05 guest rule testable.** D-019's test is *"is there anything here to do at all"*, and for V05 the honest answer is no. **But the recorded reason must change**: it is not *"states no testable rule"*, it is *"states rules excluded by D-025"*. Left as-is, V06–V21 will read this as precedent for the wrong proposition |
| **F** — homework | `SUCCESS AFTER SOURCE REVIEW`, partial by decision | ✅ **UPHELD.** Correctly refuses `NOT APPLICABLE`: the assignment is partly performable, the performable part was performed on real data, and grading it `NOT APPLICABLE` would have hidden real work. The H3 substitution is declared rather than counted silently, which is the right call |
| **B** — recognition | `NOT APPLICABLE (with reason)` | ⚠ **NOT AVAILABLE AS LABELLED.** `D-019`'s table grants `NOT APPLICABLE` **for dimensions F and G only.** Dimension B has no such grant. This is the same mis-disposition V04 R1 raised as `N1` for its dimensions B and C, and it is carried the same way — **as a NOTE with a required action, not as a new severity** — because the prose beneath the label is accurate and honest |

**Ruling on the third disposition: the project needs one, and V05 is the lesson that proves
it.** Neither existing label fits work that is *permanently excluded by a standing decision*:

- `NOT APPLICABLE` says *there was never anything here* — false; there is an hour of it.
- `DEFERRED` says *this becomes possible later* — false; it never does.

> **Recommended to the owner: adopt a third disposition, `EXCLUDED BY DECISION`.**
> Semantics: subject matter **exists**; the work is **permanently barred by a numbered
> decision**, which must be cited; the item is **closed like `NOT APPLICABLE`** and does not
> accrue as debt; but the record states **what was excluded and under which decision**, so
> the exclusion is auditable rather than invisible. Available to **any** dimension, unlike
> `NOT APPLICABLE`. On adoption, V05's **B** and **G** take it, `F` stays as graded.

**This ruling does not hold the gate.** It is a vocabulary gap in the project's own
standards, not a defect in V05's understanding — and the student diagnosed it correctly,
argued both readings, and declined to resolve it unilaterally. That is the behaviour the
protocol asks for.

### 5.3 Open item 39 — the `EMA` correction: **CONFIRMED, and the fix location is here**

Re-measured word-boundary, case-sensitive, over the verbatim body: **`EMA` occurs exactly
twice** — `[00:23:52]` *"Nice close below the 50 EMA."* and `[01:05:53]` *"…or below the 200
EMA."* The third item in the transcript's own list, *"closing below the 200"* `[01:06:02]`,
is verified present and **does not contain the token**.

**The student is right, and handling it as a logged correction rather than a silent patch was
the right call.** Two committed files (`V05_TRANSCRIPT.md` § TRANSCRIPTION NOTES, `Q-005`)
still read *"EMA occurs 3 times"*.

**Required:** correct both files in place, retaining the superseded text per
`REMEDIATION_PROTOCOL.md` §2. No conclusion in either file changes — the point both were
making (no 5/13/800 EMA, no colours, no nicknames) is independently re-confirmed here:
`5 EMA` 0, `13 EMA` 0, `800` 0, `mayonnaise` 0, `mustard` 0, `water` 0.

---

## 6. THE SEVENTEEN DIMENSIONS

| | Dimension | Verdict |
|---|---|---|
| A | Source fidelity | **PASS** — one smoothed quotation (`M3`) against 92 verified fragments. No qualifier dropped; the *"but up to five days"* escape clause is preserved at all four occurrences |
| B | Completeness | **PASS** — ten structural blocks, and the pass discipline and Q&A block (the substantive half) are captured where a slide-skimmer would have missed them |
| C | Provenance | **PASS** — 356 citations, 2 defective (`M1`, `M2`). **Orphan rules: none, vacuously — there are no rules** |
| D | Explicit vs inferred | **PASS** — `EXPLICIT`/`VISUAL`/`IMPLIED`/`INFERRED`/`UNRESOLVED` used correctly; §4 "INTERPRETED RULES: **None**" is present and deliberately empty, with the rejected candidates enumerated so a future session sees they were considered, not missed |
| E | Chart recognition | **NOT ENGAGED** — no setup is classified anywhere |
| F | Counterexample testing | **PASS** — nine worked passes recorded as negatives, not coded |
| G | Manual backtest procedure | **NOT ENGAGED** — none performed. See `N4` |
| H | Hindsight / lookahead | **PASS — nil return.** The flashcard crops withhold the future half of the chart by construction |
| I | Outcome vs rule application | **NOT ENGAGED** — no trades |
| J | Sample quality | **PASS** — the one-week four-pair observation is explicitly labelled *"not a finding"*, with `n = 3` stated |
| K | Homework review | **PASS** — see §3. First attempt preserved; every limit declared |
| L | Teach-back | **PASS** — §1 of the interpretation states the lesson's argument in four steps and separates what is stated from what the agent assembled |
| M | Blind recognition | **NOT ENGAGED** — correctly; V05 supplies no admissible criterion to test against |
| N | Ambiguity review | **PASS** — `A-042`…`A-049` opened; `A-045` and `A-048` left **unrepaired**; `A-046` explicitly forbids a future session from "fixing" a self-contradiction by picking a half. No subjective phrase turned into a constant |
| O | Contradiction review | **PASS** — nil return **with reasoning**. Three candidates examined and dispositioned. `C-003` struck off: **zero clock-time tokens in the body, re-measured this session with markers excluded** ✅ |
| P | Machine-rule firewall | **PASS** — nothing entered any spec or the concept library; the checklist declares the concept-library omission rather than hiding it |
| Q | Claimed accuracy | **PASS** — the guest's 80–85% is preserved with provenance, **not reconciled** with V01's 90–95%, and correctly held to be evidence about neither |

---

## 7. WHAT THIS SUBMISSION DID PARTICULARLY WELL

Stated because `REVIEW_PROTOCOL.md` §1 forbids manufacturing objections, and three things
here are better than anything the project has produced before.

1. **It refused to convert an hour of good material into doctrine, and said why.** The
   interpretation names the temptation explicitly — V05 contains the corpus's clearest
   stop-hunt/trap-move discriminator, its only sustained answer to *how do you draw the box*,
   and its first usable description of daily study — and excludes all of it. *"A session that
   promotes them because they are good would be doing precisely what failure mode 3
   describes… and would be doing it with the best of intentions."* That is the single most
   valuable paragraph in the V05 pass.

2. **The homework holds the D-025 line inside the artifact.** Not in a caveat — in the
   rendered PNG's footer. The exclusion is legible to anyone who finds the file with no
   context at all.

3. **It submitted `REVIEW REQUIRED`, not `PASS`, for the right reason.** The report identifies
   the exact standards gap, argues both readings, states which it chose, and hands the
   decision up. Contrast the failure mode the reviewer exists to prevent: a session that
   graded V05 `PASS` on a purposive reading and moved on.

**And the counterfactual is worth recording.** Instructor runtime across one session date
runs **~100% (V03) → ~31% (V04) → 0% (V05)**. A session that had skipped speaker
identification would have written an entire lesson of false doctrine — anchor theory, level
assignment, a three-day reversal expectation, an 80% accuracy claim — and every downstream
file would have inherited it. `D-025` consequence 3 was written one lesson before it was
needed, and this is the lesson that shows the cost of skipping it. **Open item 38 is upheld
and should be read by every remaining session.**

---

## 8. REQUIRED ACTIONS

Ordered. All six are localised; none requires reprocessing any artifact.

1. **`M1`** — correct the *"I use the trend line. I use E and I use the box."* citation to
   `[00:57:35]`–`[00:57:36]` in **both** `V05_SOURCE_NOTES.md` §3b and `A-043`'s evidence table.
2. **`M2`** — correct `A-039`'s extension row citation `[00:36:03]` → **`[00:36:05]`**.
3. **`M3`** — restore *"level three second leg of that pattern…"* in `V05_SOURCE_NOTES.md` §4b,
   or mark the elision.
4. **`M4`** — reconcile `V05_INTERPRETATION.md` line 12 to `INDEX.md`'s disclosed process
   deviation. **Do not weaken the `INDEX.md` disclosure to match the interpretation.**
5. **`M5`** — update `A-039`'s stale *"V05 is the next candidate"* pointer.
6. **`M6`** — record frame 26's oscillator sub-panel in `INDEX.md` and in `A-039`'s extension
   row, scoped *"displayed, not taught; header not legible"*. It does **not** narrow `A-039`.
7. **Open item 39** — apply the `EMA` 3 → 2 correction in `V05_TRANSCRIPT.md` and `Q-005`,
   superseded text retained.
8. **Dimension B** — re-dispose from `NOT APPLICABLE`, retaining the present text verbatim
   beneath the new label (`D-019` / V04 `N1` precedent). **Dimension G's grade is upheld; its
   stated reason must change** to *"excluded by decision under D-025"*.

**Owner actions (not blocking, not for a student session):**

- **`A`** — adopt the third disposition `EXCLUDED BY DECISION` (§5.2), or rule that the
  existing two suffice and say which applies to V05.
- **`B`** — record §5.1's `A-043` carve-out as a numbered refinement of `D-025`.
- **`C`** — `A-042`: decide whether the project acknowledges an **out-of-corpus dependency**.
  If the operative detail for levels, reset, nameable patterns and traps genuinely lives in
  the DMR, some `A-xxx` records are unresolvable from this library **in principle**. The
  record's own warning is correct and must be preserved: **an unavailable source is a reason
  to leave a record OPEN, never a reason to infer what it said** (`D-008`, `D-010`).

---

## 9. WHAT THIS ROUND DID NOT RE-AUDIT (`REVIEW_PROTOCOL.md` §4)

Stated so a later round knows the boundary:

- V01–V04 artifacts, except where V05 cites them. All four are `COMPLETE`.
- The 799 sweep frames not curated into `INDEX.md`. The 30 curated frames and 5 `hires/`
  re-renders were examined; the index's 80-distinct-states clustering claim was **not**
  re-run.
- The five Whisper spot-check windows in `V05_TRANSCRIPT.md` criterion 2 were not
  re-transcribed from audio. The transcript's **structural** claims were fully re-derived and
  all reproduce; I-008 adoption is accepted on that basis plus Q-005's independent failure of
  the fabricated siblings.
- `A-045` and `A-048`'s ASR garbles were not independently re-listened to. Leaving them
  unrepaired is correct and no reading is proposed here.

---

## 10. DECISION

```text
LESSON: V05
DECISION: REVISE
CONFIDENCE: HIGH

CRITICAL ISSUES:
- None.

MAJOR ISSUES:
- None.

MINOR ISSUES:
- M1 (E11) same quote miscited two ways, neither a marker
- M2 (E11) citation off by one marker in A-039
- M3 (E01) smoothed quotation, "level three" dropped
- M4 (E20) three files disagree about V05's own evidence order
- M5 (E20) A-039's "V05 is the next candidate" pointer is stale
- M6 (E20) unrecorded oscillator sub-panel in curated frame 26

DATA-INTEGRITY / CONCURRENT-SESSION DAMAGE:
- NONE FOUND. One pipeline, nine commits, registers contiguous
  and duplicate-free. No cleanup required.

REQUIRED ACTIONS: 8 (§8), plus 3 owner actions
ADVANCEMENT: AUTHORIZED — V06 gate OPEN under D-024
V05 STATUS: NOT COMPLETE until the minors are applied and re-reviewed
```

**Would I be comfortable letting future code depend on this interpretation?**
(`REVIEW_PROTOCOL.md` §18.) **Yes — because it asks nothing of future code.** V05's
interpretation makes exactly one claim about the method: that the method is not in V05. This
session tested that claim against the audio, the frames, the registers and the decisions, and
it holds. The lesson that produces no doctrine is the easiest one to certify and the hardest
one to resist over-reading, and this submission did not over-read it.

---

*Round R1. Never overwrite (`SETUP_ISSUES.md` I-002). Remediation → `V05_REVIEW_R2.md`.*
