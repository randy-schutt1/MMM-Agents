# V21 — MASTERY REPORT

**Lesson:** `Bootcamp1 Wk10 061712 (75mins).swf` — Week 10, 2012-06-17 — ⭐⭐ **THE FINAL LESSON OF THE COURSE**
**Printed subject:** `MARKET MAKERS BOOT CAMP` — master review, money management, and the
`High / Low Trainer` script
**Branch:** `video/v21`, isolated worktree per `D-038`
**Student status:** ⚠️ **REVIEW REQUIRED** — not `PASS`. `D-004`.

---

## §0 — GATE STATUS, CHECKED RATHER THAN TRUSTED

| Check | Result |
|---|---|
| Integration tip at fork | **`19e6c2a`** — `merge(review/v20): V20 student work + R1 + R2` |
| V20's standing tally | **0 CRITICAL / 0 MAJOR / 1 MINOR** at R2 |
| V21 gate | ⭐ **OPEN under `D-024`**, and **opened by an INDEPENDENT R2**, not by a self-verify |
| This branch forked from | `19e6c2a`, before any V21 content commit |

⭐ **This is the first gate in three lessons opened without an owner-authorised self-verify in the
chain.** V19's item 302 was closed that way; **V20's two `MAJOR`s were fixed and then independently
re-verified by the R1 reviewer**, which is what `D-024` actually asks for.

⚠️ **V20 remains IN REMEDIATION on item 348; V19 on 303–304; V18 on 264–268; V17 on 244–249.**
**None is discharged here.**

---

## §1 — WHAT V21 IS

**The last night of a ten-week course.** It reviews the standing checklist, argues that a struggling
trader should **manage equity like a dealer** rather than chase a better entry, and then **ships and
installs the course's only mechanical tool** — the `High / Low Trainer`: a market order plus two
pendings 20 pips apart, hard-stopped, with a 1–5 % risk dial and aggregated lot sizing. It closes
with a **four-rung self-diagnostic ladder** whose top rung is *"stop using the script"*.

⭐⭐ **V21 is the lesson V19 promised.** V19 `[00:02:12]` — *"we're gonna release the scripts on the
last night of boot camp"* — and `[00:00:52]` fixed that night as June 17. **It was a forward
EXPECTATION, `D-049` was never invoked, and it was correct.**

---

## §2 — ⚠️ DECLARED DEVIATIONS, BEFORE ANY GRADE

1. ⭐ **The §9 two-pass order was followed** — §§1–9 written while the sweep ran, no frame on disk.
   **Item 286 did not recur.** ⚠️ Achieved by scheduling, not by resolving item 306.
2. ⭐⭐ **An independent ASR pass WAS run** on the load-bearing passages — the check V20 was charged
   for omitting (item 326). ⚠️ **It was TARGETED, not full-file**: three passages, ~2 minutes of
   audio out of 75. **Weaker than V15/V16/V18's full-file passes and it is owed.**
3. ⚠️ **The install walkthrough is ~20 minutes of screen recording and five frames were kept.**
   A reviewer wanting the script's filename would need a denser sweep of `42:38`–`62:28`.
4. ⚠️ **`PT-050` borrows `PT-047`'s event definition.** Declared in the pre-registration as the
   largest threat, but it means **the test's event is not V21's**.
5. ⚠️ **I published a corrected figure mid-round.** `BT_V21_0001.md` §0/§2 were first written from a
   **truncated terminal view** and carried a wrong primary median (26.05 for 29.70). **Caught by
   re-reading the JSON before commit and corrected in the same commit.** Recorded because the
   near-miss class — quoting a number from a scrollback rather than the artifact — is exactly what
   items 265 and 332 are about.

---

## §3 — THE TEN DIMENSIONS

| # | Dimension | Status | Basis |
|---|---|---|---|
| **A** | **Recall** | ✅ **SATISFIED** | Every structure, figure and rule recorded with its marker; 17 frames transcribed from the pixels |
| **B** | **Recognition** | ⚠️ **BLOCKED — `D-030`** | ⛔⛔ **EIGHTH lesson running, and now PERMANENTLY** — `A-133` (*blue tracer*) survives V21, **and V21 is the last lesson.** The course ended without defining it |
| **C** | **Discrimination** | ✅ **SATISFIED** | The lesson's own discriminators kept apart: the four benchmark rungs (`[00:38:42]`–`[00:41:57]`), *"stop using the script"* as the exit condition, and ⭐ the pivot condition at `[00:18:08]` (*"only valid if the dealer throws an M or a W on it"*) |
| **D** | **Sequence** | ✅ **SATISFIED** | The order structure (market → 2 pendings → stop) and the three choices on a partial fill are recorded in order with markers |
| **E** | **Exceptions** | ✅ **SATISFIED** | ⭐ V21's central exception is **its own tool's expiry** — `[00:41:48]` *"stop using the script and place regular orders"*. **A lesson that tells you when to stop using what it just gave you** |
| **F** | **Homework** | ✅ **SATISFIED** | `V21_HOMEWORK.md`. ⚠️ **All four items NOT DONE or NOT APPLICABLE with reasons** — the first lesson whose primary assignment this project cannot perform even in principle (`A-141`) |
| **G** | **Manual backtesting** | ✅ **SATISFIED** | `PT-050` pre-registered before its runner, **`N1` an explicit verdict condition**, the §5 decision-table hole closed, every scale stated inside its measure. ⛔ **Verdict `FRAGILE`, reported as a null** — and the report leads with it |
| **H** | **Provenance** | ✅ **SATISFIED** | `.swf` SHA-256 and byte length re-computed and matching; **four independent length measures agreeing to 0.33 s**; port and bytes verified; §8a measured and published; **17 of 17 frames named from individually-read burned timecodes**; ⭐ **and the recording dates itself — `6/17/2012` legible in the OS clock of the install frames** |
| **I** | **Ambiguity** | ✅ **SATISFIED** | `A-140`, `A-141` opened, each with what would close it. ⭐ **And a near-miss recorded rather than a closure claimed** — see §4.2 |
| **J** | **Contradictions** | ✅ **SATISFIED** | `C-031`, disposition **`UNRESOLVED`** with the reason it is not `PROVISIONAL` — ⚠️ **and it can no longer be closed by a later lesson, because there is no later lesson** |

**Eight satisfied, one blocked, and the blocked one is now permanent.**

---

## §4 — WHAT V21 CONTRIBUTES

### 4.1 ⭐⭐⭐ THE COURSE'S ONLY MECHANICAL ARTIFACT, WITH ITS PARAMETERS IN THE AUTHOR'S HAND

The `31:25` frame photographs handwritten notes dated `1-27-2010`: **`High / Low Trainer`**,
`MAX RISK 5%`, risk dial `1–5 %`, `↕20 ↕20 ↕20` pips, `Take profit +30 from ORDER 1`,
`Cycle 30 + 50 + 70` = `150`, *"most often"* `+80`. ⚠️ **The artifact itself is not in this
repository — `A-141`.**

### 4.2 ⭐⭐ A NEAR-MISS THAT WOULD HAVE CLOSED THE CORPUS'S LONGEST-STANDING BLOCKER — WRONGLY

The committed grid reads `[00:05:21]` as *"the light blue tracer **in** the a DR line"*. **Read as an
apposition that DEFINES the blue tracer as the ADR line and closes `A-133` after seven lessons.**
⛔ **The independent decode reads *"the light blue tracer **AND** the ADR line"* — a list of two.**
⭐ **Caught before it reached any artifact.** ⚠️ **`A-133` is narrowed (the tracer is *light blue* and
belongs to the ADR/hi-lo marker family) and NOT closed.**

### 4.3 ⭐ V21 DEFINES WHAT V19 COULD NOT

`[00:04:41]` ***"the big board is the high low board"*** — confirmed verbatim independently. **V19
recorded `Worked the Big Board` as printed-only and undefined** (item 298, `V19_HOMEWORK.md` §2).
**Closed by V21.** `Moving AVG Only trades` is likewise expanded at `[00:04:51]`–`[00:05:11]`.

### 4.4 ⭐⭐ `Q-022` CONFIRMS THE TEMPLATE BREAK — AND CORRECTS THE CORPUS'S DESCRIPTION OF THE OFF-BY-ONE

V21 diffs at **`32/30/26` against ALL FIVE** B-block members and **near every A-block member** —
item 254's prediction confirmed **from the far side of the boundary, on all twenty comparisons.**
⭐⭐ **And the *"counts one ahead"* description in `Q-019`/`Q-020`/`Q-021` is a generalisation from
the middle of the range:** V01→V01 and V02→V02 are **correct**, V03–V20 shift `+1`, and **V21 wraps
to `V03`.** **It is a closed permutation, not a shift.**

### 4.5 ⭐ §8a RETURNS A SIXTH SHAPE, AND `GOTCHA 5` EARNED ITS PLACE

`+16 s` startup transient — **the same value V19 and V20 measured** — absorbed to zero by 30 s
(**item 296 corroborated on a third sweep**), **plus a slow negative drift to `−2 s`**.
⚠️ **And V21 is a `1280 × 738` file**: the play click is `(512, 325)` and the player chrome sits at
`y ≈ 670`. **Reusing V20's coordinates would have swept a splash screen.**

---

## §5 — WHY THIS IS `REVIEW REQUIRED` AND NOT `PASS`

1. **`D-004`.** A student `PASS` is not a gate.
2. **The ASR pass was targeted, not full-file** (§2.2) — ~2 minutes of 75.
3. **`PT-050` returned `FRAGILE`** and borrows another test's event definition (§2.4).
4. **Dimension B is blocked permanently** — the course ended without defining the blue tracer.
5. **I published a wrong figure mid-round and corrected it** (§2.5).

---

## §6 — WHERE I WOULD MARK MYSELF DOWN

* ⚠️⚠️ **The near-miss on `A-133` is what I would lead with as a reviewer.** I had drafted the
  closure. **One preposition, and only an independent decode stood between it and the corpus.**
* ⚠️ **Quoting `26.05` from a truncated terminal view** instead of the JSON. Caught, corrected,
  and exactly the defect class items 265/332 exist for.
* ⚠️ **Five frames of a twenty-minute install walkthrough.** If the script's filename is legible
  anywhere, I did not find it.
* ⚠️ **I did not chase `M3`, the *"25-pip box"* or *"shark fin"***, all named at `[00:18:18]`.

---

## §7 — OPEN ITEMS FOR THE REVIEWER

| # | Item |
|---|---|
| 1 | ⚠️ **A full-file independent ASR pass is OWED.** Priority: `[00:30:18]` (the script's name), `[00:26:52]` (*"by order percent"*), the install section's filenames |
| 2 | ⚠️ **`PT-050` borrows `PT-047`'s event.** A reviewer preferring a V21-native *"stop hunt"* would build a different event set — and might get 50 pips |
| 3 | ⛔ **`A-141`: the script is not in this repository.** ⭐ **The single highest-value acquisition available to this project** — it is the course's own implementation |
| 4 | ⛔ **`A-133` is now PERMANENTLY open.** Dimension B has been blocked for eight lessons and the course has ended |
| 5 | ⭐ **`Q-022` §1 corrects three prior quarantine entries.** A reviewer should check the permutation independently — it is one `grep` over 21 folders |
| 6 | ⚠️ **`C-031` can never be closed by a later lesson.** There is none |
| 7 | ⭐ **The corpus is COMPLETE.** All 21 lessons ingested. A **cumulative review** (`REVIEW_PROTOCOL.md` §14) and `FINAL_COURSE_REVIEW.md` are now due |

---

## §8 — SESSION HYGIENE

| Item | State |
|---|---|
| Branch | `video/v21` from `19e6c2a` |
| Worktree | `/Users/randyschutt/Desktop/Trading/MMM-Agents-v21` — isolated per `D-038` |
| Corpus wiring | CSVs symlinked individually, never a tracked directory; `git status` type-change check — **zero** (item 300's trap) |
| Staging | explicit paths only; **no `git add -A`** (`I-009`) |
| Policy ledgers | **NONE touched.** `DECISIONS.md`, `SETUP_ISSUES.md`, protocol files untouched |
| Merged to integration | ❌ **NO — deliberately.** `D-003` |
| Record IDs allocated against | `19e6c2a`. **`D-047` re-check owed at merge-back** |
