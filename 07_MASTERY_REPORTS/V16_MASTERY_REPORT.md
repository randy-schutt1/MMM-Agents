# V16 — MASTERY REPORT

**Lesson:** `Bootcamp1 Wk7 050612 Part2 (45mins).swf` · V16 · 2012-05-06 · 00:44:35
**Printed title:** ⭐ **`Pivot Points`** (`V16_00-00-20_…png`) — a real topic title, on the running
head of every slide to `34:55`
**Branch:** `video/v16`, worktree `MMM-Agents-v16` (`D-038`)
**Submitted as:** ⚠ **REVIEW REQUIRED** — not PASS. See §5.

---

## §1 — WHAT V16 IS, IN ONE PARAGRAPH

**Part 2 of the same recording as V15, opening mid-sentence on the word *"pivot points"* with no
greeting.** It is a single-topic lesson on floor-trader pivot points: how they are computed, what
the instructor's `M1`–`M4` labels are, how a daily candle's **colour** selects the day's projected
high and low, how that projection inverts on the fourth day of a cycle, and how the fixed pivot
grid is coupled with V15's floating ADR markers. **It is the join V15 promised and did not make.**

---

## §2 — ⚠ DECLARED DEVIATIONS AND SELF-CORRECTIONS, BEFORE ANY GRADE

**Five deviations and four self-corrections. They are listed first, in full, because a report that
buries them is worth less than one that leads with them.**

### Deviations

| # | What | Where declared |
|---|---|---|
| `D1` | **`SWF_CAPTURE_RECIPE.md` §9's transcript-before-frames ordering was BROKEN**, as in V13/V14/V15. Mitigated by tagging every source-notes item `[AUDIO]` / `[PRINTED]` / `[VISUAL]`, which is `grep`-falsifiable | `V16_SOURCE_NOTES.md` §0 |
| `D2` | **Three conclusions rest on frames**, named individually so a reader can discount them | `V16_SOURCE_NOTES.md` §0 `D2a`–`D2c` |
| `D3` | ⚠ **The frame sweep DID NOT follow §10's script literally** — `t0` is set **before** the click, which is item 188's proposed fix. **This is why §8a's offset measured zero.** The recipe file itself was **not** edited (`D-038a`, policy ledger) | `04_SCREENSHOTS/V16/INDEX.md` §0.2; item **197** |
| `D4` | **No forward read.** Item 179 is unsettled and its clause (d) binds. V17+ was not opened. V15's committed artifacts *were* read — a **backward** read, which needs no precedent | `V16_SOURCE_NOTES.md` §0 `D3` |
| `D5` | **`PT-044`'s runner was corrected twice after its first execution** — once for a scope-name error, once because it had not implemented §4's `W-E` window and pooled it with `W-D`. Superseded figures printed rather than discarded | `BT_V16_0001.md` §6a |

### Self-corrections — ⚠ ALL FOUR CHARGED AGAINST THIS SESSION

| # | What I got wrong | How it was caught |
|---|---|---|
| `S1` | ⚠⚠ **ELEVEN of thirty-four frames were named from the TRANSCRIPT, and not one of those names described anything visible in its own frame.** `asian-range-forms-at-central-pivot`, `three-intraday-pushes-annotated`, `candle-overlap-annotated`… **This is the exact failure `§8` warns about and the exact failure the `Q-xxx` register exists for**, reproduced in the same session that filed `Q-017` | Re-rendering the eleven at `490 × 370` and looking. All renamed. `INDEX.md` §6 |
| `S2` | ⭐ **The sharpest instance of `S1`:** `V16_00-09-30` was named `adr-written-on-grid` on the strength of `[00:09:31]`, the lesson's most important line. **The word `ADR` is not on that frame.** It appears at `00-10-00` | Same |
| `S3` | ⚠ **My first draft asserted `M1`–`M4` are midpoints of adjacent pivots as a FINDING.** It is unsupported — the diagram is a schematic | Measuring the pixel spacing (all nine levels equal to ±1 px) instead of eyeballing it. `A-101`, `V16_INTERPRETATION.md` §3 |
| `S4` | ⚠ **The homework's first attempt computed `M3` and `M1` as midpoints anyway** and produced a plausible 104.8-pip expected range on real GBP/USD data. **Nothing downstream would have flagged it.** Preserved and struck | `V16_HOMEWORK.md` §3a |

⚠ **`S1`/`S2` are a SAMPLE, not the population.** They are the ones a second look caught.

### One process error, disclosed

While supplying the gitignored raw dataset to a fresh worktree, this session briefly replaced two
**tracked** `SHA256SUMS.txt` files with symlinks. **Restored with `git checkout` before anything
was committed; the CSVs were then copied and all 13 verified against the committed manifest
(`shasum -c`: 13 OK) before a single bar was read.** Nothing entered a commit in the broken state.
`BT_V16_0001.md` §6c.

---

## §3 — THE TEN DIMENSIONS

| | Dimension | Status | Basis |
|---|---|---|---|
| **A** | **Recall** | ⭐ **PASS** | `05_HOMEWORK/V16/` §6: 14/14 recall claims machine-checked against the committed transcript, answers committed before the checker ran. ⚠ **The report says why 22/22 is weak evidence** — the probe was written after three close readings |
| **B** | **Recognition** | ⛔ **BLOCKED BY `D-030`, EXCLUDED FROM PASS/FAIL PER OWNER DIRECTIVE** — **the seventh consecutive lesson.** `REVIEW_INDEX.md` open item 36 (the project has no vocabulary for this disposition) is still owed. ⚠ **V16 makes the block sharper than usual: the lesson's own patterns (`M`/`W` at a level) are undefined (`A-010`/`A-011`), and now the LEVELS are undefined too (`A-101`)** |
| **C** | **Discrimination** | **PARTIAL** | The colour rule (`§3`) is a genuine discriminator and is exercised in the homework — both target days classified `RED → M1/M3` from data. **But the discrimination that matters (is this level `M3`?) cannot be performed at all** |
| **D** | **Sequence** | ⭐ **PASS** | The lesson's own sequence — Asian range at `CPP` → stop trigger → `M` at `M3` → three pushes to `M1` → mid-session drift → closing `W` → hand-off → consolidation — is reconstructed step by step from audio in `V16_SOURCE_NOTES.md` §4, with the whiteboard frames as corroboration, and the **three-day/fourth-day** compound rule verified consistent across **three** separate statements |
| **E** | **Exceptions** | ⭐ **PASS** | The lesson's own escape rule is captured verbatim and treated as the lesson's most honest moment (`§8`): *"Ignore the pivots and identify… the pattern."* Its **trigger** is recorded as undefined (`A-103`) rather than reconstructed |
| **F** | **Homework** | ⭐ **PERFORMED — and it produced the session's sharpest single finding** | `05_HOMEWORK/V16/`. Done on real checksummed data for the assigned Monday and Tuesday. ⭐ **It completes to five of the seven numbers and stops**, which is `A-101` demonstrated rather than asserted. It also **found `A-106`** (a 72.6-pip fork nobody had noticed) and **quantified `C-023`** (under 4 pips). ⚠ **Scope: GBP/USD only, not the six majors assigned** |
| **G** | **Manual backtesting** | ⭐ **PERFORMED** | `PT-044` / `BT_V16_0001`, pre-registered at `9cc1cae` before the runner existed and before any bar was read. **4 of 5 predictions correct, and the miss is reported first.** Two windows, two arms, four controls, verdicts differing by reading and by window |
| **H** | **Provenance** | ⭐ **PASS** | SHA verified before **and after** the frame-rate patch; port and served bytes verified (`GOTCHA 4`); play click confirmed by guard (`GOTCHA 5`); **§8a offset MEASURED at ten points**; transcript verified on **five** checks including a full independent ASR pass; dataset checksums re-verified after the §2 process error |
| **I** | **Ambiguity** | ⭐ **PASS** | **Six opened** (`A-101`–`A-106`), **four amended** (`A-095`, `A-096`, `A-097`, `A-100`). ⚠ **`A-096`'s identity half is CLOSED and its `TIER 2 ONLY` clause SUPERSEDED** — the only closure V16 earns, and it is stated as such |
| **J** | **Contradictions** | **PASS** | `C-023` filed **with its own mitigation and with a measurement that cuts against its importance** (under 4 pips), and with an explicit instruction that a reviewer should escalate `A-106` instead |

---

## §4 — WHAT V16 CONTRIBUTES

### ⭐⭐ The two that matter

1. **THE ADR LOOKBACK, IN TIER 1.** `[00:09:31]` *"the ADR is calculated over the last two weeks,
   15 days."* `COURSE_PROGRESS.md`'s V16 GATE (c) named this as *"the highest-value thing V16 could
   contain"*, and it contains it. **Confirmed verbatim by an independent ASR engine.**
   ⚠ **`A-100` ADVANCES, DOES NOT CLOSE** — *"two weeks"* is 10 or 14 and neither is 15, and the
   range definition, marker anchor and day boundary are all still absent.
2. **THE PIVOT GRID, PRINTED.** `R2 · M4 · R1 · M3 · CPP · M2 · S1 · M1 · S2`. **`A-096`'s identity
   question closes.** ⛔ **`A-101` opens in its place** — the *construction* of `M1`–`M4` is stated
   nowhere, and the diagram that looks like it encodes the arithmetic is **equally spaced to ±1 px**
   and therefore a schematic.

### ⭐ The rest

3. **A printed, timezone-stamped SESSION BOUNDARY** — `London Session Start / 2:00 To 3:00 AM, EST`
   — the corpus's first (`A-105`), with the `EST`-in-May hour left unresolved rather than assumed.
4. **The candle-colour rule**, printed, spoken twice and hand-drawn once — the most completely
   specified rule in the lesson, and mechanically checkable.
5. **`PT-044`:** the same sentence in two moods gets two verdicts. CEILING **WEAKLY SUPPORTED**
   (7.3% / 4.9% breach); TYPICAL **PARTIALLY SUPPORTED** in `W-D` and **CONTRADICTED AS STATED** in
   `W-E`. Median GBP/USD day: **102.6 / 92.3 pips**, not 200.
6. **`A-106`**, found by doing the homework: *"yesterday"* on a **Monday** is undefined, and the two
   readings differ by **72.6 pips on `R2`** on a day whose whole range was 133.9.
7. **`Q-017`, and the pattern has CHANGED** — the sixth fabricated trio is a **paraphrase** of
   V15's, not a byte clone. **A `diff`-based check would have missed it.** The invariant is the
   three timestamps and three subjects.
8. **`A-104`:** a second bootcamp cycle was planned for autumn 2012 and is not in this library —
   filed as an out-of-corpus dependency, **deliberately not as a corpus gap**, because item 185's
   audit must not count it against completeness.

### ⚠ What it does NOT supply, and absence is evidence

**No stop loss (0 occurrences), no position size, no R:R, no target, no `M`/`W` definition, no
cycle-start test, no timezone on *"midnight"*, and — for the fourth consecutive lesson — no
indicator properties dialog in 544 frames (3,214 across V12–V16).** `A-084` stays blocked, exactly
as V16 GATE (b) predicted, and this session did **not** hunt for it.

### ⚠ And one thing worth carrying to item 179's ruling

**V16 states NO week number, NO date and NO session number in 377 markers.** V15's item 190 offered
a *"cheap forward-read check"* into V16 to confirm the Week-6 calendar and deliberately did not take
it. **It would have returned nothing.** The forward read that was declined would also not have paid.

---

## §5 — WHY THIS IS SUBMITTED AS **REVIEW REQUIRED** AND NOT **PASS**

**Two reasons, and the first is the same one for the seventh lesson running.**

1. **Dimension B is `D-030`-blocked and the project still has no vocabulary for that disposition.**
   `REVIEW_INDEX.md` open item 36 has been owed since V08. An owner ruling is still outstanding.
2. ⚠ **`S1`/`S2`.** This session reproduced, in eleven of its own thirty-four frames, the precise
   fabrication pattern it filed `Q-017` against — naming visual artifacts from the transcript rather
   than from the image. **It was caught by this session and fixed by this session, and that is not
   the same as it not having happened.** A reviewer should treat the eleven as a sample and re-check
   the naming of the remaining twenty-three independently.

**`D-003` reserves closure to an independent reviewer. This report is a self-assessment and a
submission, not an authorisation to advance.**

---

## §6 — OPEN ITEMS RAISED FOR THE REVIEWER

`REVIEW_INDEX.md` items **195–200**. In brief:

| Item | Subject |
|---|---|
| **195** | ⭐⭐ `A-100`'s lookback arrives and **disagrees with itself** — 10 vs 14 vs 15 |
| **196** | V16 carries **no internal date or week number**; the forward read item 190 declined **would not have paid** |
| **197** | ⭐ Item 188's `t0`-before-click fix is **CONFIRMED by measurement** (offset 0 vs 4-of-4 at +15/+16) — a **policy-ledger** edit to `SWF_CAPTURE_RECIPE.md` §10 is owed on the integration branch |
| **198** | `A-101`'s cheapest close is a **higher-resolution re-capture** of two named frames whose price axis is illegible at `1024 × 786` |
| **199** | ⚠ **`S1`/`S2` self-charge** — eleven frame names fabricated from the transcript, in the session that filed `Q-017` |
| **200** | `Q-017`'s detection note: the generator now **paraphrases**, so a byte-`diff` will not flag V17–V21 |

---

## §7 — SESSION HYGIENE

* **No `I-009` collision.** V16 ran in a dedicated worktree on branch `video/v16` under `D-038`,
  with evidence ledgers written on the task branch as `D-038a` expects and **no policy ledger
  edited** (item 218, allocated 197, is deferred for exactly that reason).
* **`12_MASTER_SPEC/` and `13_MACHINE_SPEC/` untouched.** `09_CHART_EXAMPLES/`, `14_PINE/`, `15_`,
  `16_`, `17_` untouched. No Pine, no signals, no spec population.
* **Nothing merged to integration.** That is a separate, single-threaded act performed by a
  different session after independent review.
