# V08 — INDEPENDENT REVIEW R2 (verification of open items 64–66)

| Field | Value |
|---|---|
| Lesson | V08 — *"Jim's Journey in Learning and Trading MMFX"* (`Bootcamp1 Wk2 032612 Part3 (43mins).swf`, 00:43:03) |
| Review round | R2 — **verification round.** R1 returned `REVISE`, 0 `CRITICAL` / 0 `MAJOR` / 3 `MINOR` (open items 64–66) |
| Reviewed | 2026-08-13 |
| Reviewer | Independent Reviewer / Teacher Agent |
| Submission under review | The remediation of items 64–66, applied on `fix/v08-r1-minors` at `20d1e3d`, `43494ab`, `4477846`, merged to integration at `dd787d9` / `a6ee013` |
| `D-003` separation of duties | **SATISFIED.** This session authored **no** V08 artifact and **no** part of the remediation. Every claim below was re-derived from primary sources — the V07 and V08 transcript bodies, the PNG's own pixels, the runner's source, and `git` — **before** the remediation's account of itself was accepted. Where the remediation's reading and this reviewer's disagree in emphasis, the primary source decides |
| **Review basis — READ THIS** | Branch **`review/v08-r2`, cut from the integration branch at `a6ee013`**, in a dedicated worktree at `/Users/randyschutt/Desktop/Trading/MMM-Agents-review-v08-r2` (`D-038`). **`fix/v08-r1-minors` was ALREADY MERGED** when this round opened — see §6, which also records a concurrency incident that nearly corrupted this review and is charged to project process, not to V08 |
| Scope | The three items, **plus** a full standard pass for regression (§5). The presenter-identity question the remediation deliberately deferred is **RULED**, not deferred again (§2) |

---

## EXECUTIVE BLOCK

```text
LESSON:     V08
DECISION:   PASS
CONFIDENCE: HIGH

CRITICAL:   0
MAJOR:      0
MINOR:      0
NOTE:       3   (N1 the presenter-identity ruling and its one
                 residual; N2 a concurrency incident in the shared
                 working directory, charged to process not to V08;
                 N3 a bracketed ASR expansion that a mechanical
                 verbatim sweep will flag as a non-match)

ITEM 64:    ✅ CLOSED — VERIFIED. V07 [00:28:02]-[00:28:31] read at
            source in this session. The citation is accurate, the
            quotation is verbatim (garble preserved, ellipsis honest),
            the GUEST tag and the §6c cross-reference resolve, and
            PROVISIONAL is unchanged. The remediation's deliberate
            NARROWING was correct as an act of discipline and its
            text contains no false statement.

ITEM 65:    ✅ CLOSED — VERIFIED. entry_for() and
            precompute_close_entries() were read and do exactly what
            the new documentation says. PT-034's pre-registration is
            byte-unchanged against its original commit (one commit
            ever, empty diff). BACKTEST_EVIDENCE_STANDARD.md §2.1a
            binds the requirement forward.

ITEM 66:    ✅ CLOSED — VERIFIED. This reviewer cropped and magnified
            the frame's player chrome independently: the burned-in
            elapsed field reads 43:04. All FOUR references updated;
            an independent sweep for the old string finds NO FIFTH.
            The disclosed 0.25 s residual is real, correctly
            characterised, and correctly resolved.

PRESENTER
IDENTITY:   RULED — DIFFERENT MEN, at HIGH confidence, on TEXTUAL
            evidence only. R1's "a different guest presenter" is
            SUPPORTED. The names (V07 = Ray, V08 = Jim) are PROBABLE
            and remain provenance, not evidence, per D-033 prov. 2.
            No cross-file F0 comparison was used — prohibited.

REGRESSION: NONE. The remediation touched 8 files, additive but for
            three replaced timecode strings. No script, no data file,
            no transcript, no pre-registration was altered. The
            crosscheck re-runs to PASS. Validator 103/0/0.

V08 STATUS: ✅ COMPLETE.
ADVANCEMENT: AUTHORIZED. V09 gate was already OPEN under D-024 and is
             unaffected.
```

---

## 0. WHAT THIS REVIEWER VERIFIED INDEPENDENTLY, BEFORE THE REMEDIATION'S ACCOUNT WAS ACCEPTED

| # | Claim under test | Method used here | Result |
|---|---|---|---|
| 1 | The V07 citation exists and says what `Source A′` says it says | read `[00:27:41]`–`[00:28:40]` in `02_TRANSCRIPTS/V07/V07_TRANSCRIPT.md` directly | **CONFIRMED.** All four quoted fragments are verbatim; the `[00:28:28]` omission is correctly marked with an ellipsis |
| 2 | The garbled passage is not silently smoothed | compared `[00:28:31]` character by character | **CONFIRMED.** *"if it doesn't do what you expect **in** your flashcard isn't the same"* is preserved. This is the exact passage V07's item 63 charged a different artifact for smoothing to *"and"* |
| 3 | `PROVISIONAL` unchanged | read `C-009`'s disposition block | **CONFIRMED.** `PROVISIONAL` at the disposition, and the new block says so twice in its own text |
| 4 | `V07_SOURCE_NOTES.md` §6c exists and is the right section | opened it | **CONFIRMED.** §6c, *"What decides which second legs come back past the first leg"* |
| 5 | Presenter identity — is it determinable at all? | swept both transcript bodies for every named third party; cross-read `SOURCE_MANIFEST.md` and the V02/V03 coach roster | **DETERMINABLE, and DETERMINED — see §2.** V08 names **Ray** ×3 in the third person; `Ray` occurs **0 times** in V07 and **0 times** in V06 |
| 6 | `precompute_close_entries()` does what is now documented | read the function | **CONFIRMED.** It calls `resolve(hi, lo, i, cl[i], d, n)` — the entry price is literally `cl[i]`, the bar's close |
| 7 | `entry_for()` does what is now documented | read the function | **CONFIRMED.** LONG: `want = lod + X*PIP`, returns `want if lo[i] <= want <= hi[i] else lo[i]`. SHORT mirrors on `hod`/`hi[i]`. The documented *"`LOD + X` if inside the bar's range, else that bar's low"* is exact |
| 8 | `PT-034`'s pre-registration is genuinely untouched | `git log --follow` + `git diff a4ab65a HEAD` on the file | **CONFIRMED. Exactly one commit ever; the diff is EMPTY.** Byte-unchanged |
| 9 | The null's numbers are as claimed | read all four cells out of `data/pt034_output.txt` | **CONFIRMED.** `N1` medians **0.2450 / 0.2426 / 0.2424 / 0.2429** — the claimed range `0.2424–0.2450` is exact, and the `BT_V08_0001.md` table reproduces all four rows and both intervals |
| 10 | The 25.00% break-even | computed `16.67 / (50 + 16.67)` | **0.250037.** The claim is correct |
| 11 | **The burned-in timecode** | **cropped the frame's player chrome at `(968,676)`–`(1024,688)`, linear-stretched and magnified 20×, and read the pixels** | **`43:04`** — elapsed field unambiguous, total field truncated at `43:0` by the frame edge. **The remediation's reading is correct and was not taken on trust** |
| 12 | The frame's content claim still holds | opened the full PNG | **CONFIRMED.** Four rings, three labelled thresholds, **a red `?` at the centre**, `replay` button visible — the post-playback end card |
| 13 | No fifth reference to the old timecode | repo-wide sweep for `43:10` and `43-10` | **CONFIRMED.** Every surviving hit is either a **retention/superseded** block (required by `REMEDIATION_PROTOCOL.md` §2), the **R1 review file** (must never be edited), `LOG.md` **history**, or an unrelated **real marker** in V01's and V06's transcripts. **No live assertion survives** |
| 14 | The `git mv` preserved the blob | `git diff -M --summary` | **CONFIRMED.** `rename … (100%)` — blob and history intact |
| 15 | The disclosed `ceil()` residual | re-derived all 26 V08 frame timecodes against the runtime mechanically | **CONFIRMED, and the disclosure is exactly right.** Row 26 is the **only** frame over the raw runtime, at **2584 s vs 2583.745 s**; under `> ceil(runtime)` **nothing flags**. `00:43:10` (2590 s) would still be a true positive |
| 16 | Regression scope | `git diff --stat -M a886585 HEAD` | **8 files.** No script, no data file, no transcript, no pre-registration. Additive except **three** replaced timecode strings, each read individually |
| 17 | The pipeline still reproduces | re-ran `crosscheck_pt034_vs_pt033.py` | **`CROSS-CHECK: PASS`** |
| 18 | Validator | `python3 scripts/validate_project.py` | **103 passed, 0 warnings, 0 failures** |

### 0a. What this reviewer did NOT re-verify, stated plainly

**The `.swf` was not re-hashed and the frames were not re-captured this round.** R1 did both and the remediation altered neither the media nor the capture recipe; item 16 above establishes that no binary but the renamed PNG moved, and the rename is a 100 % blob-preserving `git mv`. Re-hashing would test nothing this round put at risk.

**Cross-file F0 comparison was available and was deliberately NOT used** — see §2. It would have been the shortest route to the presenter question and it is **prohibited** by `COURSE_PROGRESS.md`'s V06 GATE item (a). The ruling in §2 stands on transcript text alone.

---

## 1. ITEM 64 — `C-009`'s corroboration — ✅ CLOSED, VERIFIED

**What was required (R1 `M1`):** add the V07 `[00:28:02]`–`[00:28:31]` citation to `C-009` Source A as corroborating attestation, tagged `GUEST`, cross-referenced to `V07_SOURCE_NOTES.md` §6c, with one sentence on what it changes, and **do not** disturb `PROVISIONAL`.

**What was delivered:** a new `### Source A′` block in `CONTRADICTIONS.md`, +33 lines, purely additive — Source A stands verbatim, which is correct, because the defect was an **omission** and nothing in the original was wrong.

**Every element of the requirement is present and correct.** Tagged `GUEST` ✅. Cross-referenced to §6c, which exists and is the right section ✅. Carries a *"What this changes about the record, and what it does not"* paragraph ✅. `PROVISIONAL` untouched ✅.

**The citation was checked at source, not against the review.** This reviewer read `[00:27:41]`–`[00:28:40]` in the V07 transcript body. All four quoted fragments are verbatim, and two details deserve credit rather than silence:

- The `[00:28:26]`–`[00:28:31]` quotation **omits `[00:28:28]`** (*"We'll say whether it's something that you will take."*) and marks the omission with an ellipsis. That is honest quotation, not a seam hidden.
- `[00:28:31]`'s garble — *"if it doesn't do what you expect **in** your flashcard isn't the same"* — is **preserved verbatim**. V07's own open item 63 was charged, at R1 and again at R2, against an artifact that smoothed this precise passage to *"**and** your flashcard"*. The remediation session had every incentive to tidy it and did not. **That is the project's most-charged defect class being correctly avoided in the file where it would have been easiest to commit.**

**The one substantive judgement call, and this reviewer's ruling on it: the narrowing was correct.** R1's `M1` described V07's presenter as *"a different guest presenter"*. The remediation declined to repeat that, on the ground that it could not verify it, and flagged the disagreement for this round rather than quietly adopting either framing. **That was the right act.** A finding whose whole subject is *under-sourcing* must not itself assert an unverified claim, and the block's text — *a second **lesson**, not a second **speaker*** — contains **no false statement**. It under-claims; it does not mis-claim.

**Item 64 is CLOSED — VERIFIED at R2.** The determination the remediation could not make is made below, and it **supports** R1's original framing.

---

## 2. THE PRESENTER-IDENTITY QUESTION — RULED, NOT DEFERRED

> **RULING: V07's presenter and V08's presenter are DIFFERENT MEN. Confidence HIGH.**
> **Probable names: V07 = Ray, V08 = Jim. Confidence MEDIUM — and the names are provenance, not evidence (`D-033` provision 2). Nothing depends on them.**

The remediation was right that neither transcript header settles this. It is settled by evidence **neither header collects**, because the discriminator is not in the speaker-identification sections — it is in the lesson bodies.

### 2a. The decisive evidence: V08's speaker names his predecessor, and it is not himself

`Ray` occurs **three times** in V08's verbatim body, every one third-person:

| Marker | Words |
|---|---|
| `[00:00:49]` | *"I may or may not be able to be as responsive as **Ray** was with the questions."* |
| `[00:05:59]` | *"Some of the information that **Ray** was beginning to answer with people is leading excellently into this topic."* |
| `[00:20:49]` | *"Like **Ray**."* |

`[00:00:49]` lands **forty-nine seconds into Part 3**, in the opening housekeeping, and its whole grammatical work is to contrast the speaker with someone who **had just been** fielding the audience's questions. `[00:05:59]` does it again and explicitly hands the baton — *"the information that Ray was beginning to answer… is leading into this topic."* A man does not introduce himself as his own predecessor.

**And `Ray` occurs ZERO times in V07's body, and zero times in V06's.** That is exactly the distribution expected when Ray is the man speaking those files, and it is the same negative signature the corpus already relies on: V07's presenter is identified as not-Steve partly because *"a man does not read out his own name as the next questioner."*

### 2b. The format contrast is the one the sentence actually makes

V07 is **Part 2** and V08 **Part 3 of the same day's bootcamp** (`SOURCE_MANIFEST.md`: `Bootcamp1 Wk2 032612 Part2` / `Part3`). V07's defining format is audience Q&A — its presenter reads out **sixteen named questioners**. V08's transcript records the opposite in its own transcription notes: *"Unlike V07, **no questions are read out** — this lesson is a continuous presentation."*

*"as responsive as Ray was with the questions"* is therefore not a vague nod to some earlier session. It is a precise contrast with **the immediately preceding part's format**, spoken at its start.

### 2c. A second, independent chain reaches the same place

- V07's presenter refers to **Jim** in the third person **three times** and defers to him as another coach: `[00:07:38]` *"**Jim**, I'm going to do a presentation there but he seems to be a master at the high of the day"*; `[00:21:16]` *"**Jim** gets great graphs all the time near the high of the day"*; `[00:38:26]` *"I think **Jim** covers some of that on how he gets into those entries."*
- Immediately after the first, at `[00:07:43]`, he **disclaims that very skill for himself**: *"I like second legs because **I can't do that** sometimes."*
- **V08's second half is the high-low drill**, and its deck is titled *"**Jim's** Journey in Learning and Trading MMFX"* — read off the title slide, narrated in the first person throughout (*"my trading sanctuary"*, *"here's my hobby"*, *"I was a musician"*).

A single-speaker reading requires the same man to disclaim the high-of-the-day entry in Part 2 and then teach it authoritatively in Part 3 an hour later, over a deck bearing another man's name and life story. That is not a coherent reading.

- The programme's own roster corroborates that these are two people: V02 `[00:57:02]` *"Monday features Kar, Kim, **Jim** and **Ray**"*; V03 `[00:22:51]`–`[00:23:03]` *"Ray Kim and Jim"*.

**Two independent chains — the Ray contrast and the Jim deferral — converge on the same conclusion.** The Ray chain is the stronger of the two, and note that **it does not depend on V08's speaker being Jim at all**: whoever V08's speaker is, he distinguishes himself from the man who had been taking the questions.

### 2d. What was deliberately not used

**No cross-file F0 comparison.** V07's presenter measures median F0 142.9 Hz and V08's 145.5 Hz, and that pairing is the obvious shortcut. `COURSE_PROGRESS.md`'s V06 GATE item (a) **prohibits** using the acoustic screen to identify a speaker across files, and the screen was validated only for detecting handovers *within* one file. **This ruling rests on transcript text alone and would be unchanged if the F0 numbers did not exist.** Recorded so no future reader mistakes the numeric coincidence for part of the argument.

### 2e. The residual, stated rather than smoothed

**V08 `[00:17:29]` — *"Okay, **Jim's right** about that one"* — remains unexplained.** It is a third-person reference to a Jim by V08's own speaker, mid chart-walkthrough, and the V08 transcript already flags it and offers three readings without choosing. This reviewer does not choose either, and notes only that the vocative idiom the corpus uses when addressing a chat participant (*"Okay, **Mel**, trap volume…"*, *"Yes, **David**, …"*) is **grammatically different** from this possessive construction — so the "chat acknowledgement" reading is **weaker** than it first appears.

**What the residual does and does not touch.** It weakens *"V08's speaker is Jim"* — which is why that half of the ruling is `MEDIUM` and why the name stays provenance. It does **not** touch *"V07's and V08's presenters are different men"*, which rests on §2a–§2b and does not require the identification.

**One further limit:** whether Ray also presented V06 (Part 1) cannot be settled here. It does not matter — either way, V08's speaker is not the man who had been taking the questions, and V07 is the questions part.

### 2f. Consequence for `C-009` — and it is not a defect

`C-009` is now attested across **two lessons AND two speakers**. Under `D-033` all of it is normative at equal weight, so the record's **strength is unchanged in kind** and its **disposition stays `PROVISIONAL`** — the staging rule still defers the trained-state question. Because both speakers are `GUEST`, `D-025`'s *"a guest/instructor divergence is corpus-hygiene, not a contradiction in the method"* carve-out **does not apply**: this is guest-versus-guest across lessons, and `C-009` remains a genuine method-level contradiction, exactly as R1 found.

**No finding is charged, and the reason is on the record.** `Source A′`'s speaker-identity row says the point is *"NOT established, and deliberately not asserted here"*. That was true when written and the block invited this round to adjudicate. Charging a `MINOR` for correctly deferring to the reviewer, when the reviewer then resolves it, would penalise precisely the discipline `REVIEW_PROTOCOL.md` §1 and §16 ask for. **It is carried as `NOTE` `N1` and as new open item 71 — a documentation follow-up, NOT owed as a defect**, for whoever next has cause to touch `C-009`.

---

## 3. ITEM 65 — the null's entry-price convention — ✅ CLOSED, VERIFIED

**What was required (R1 `M2`):** state the null's entry-price convention in the pre-registration's own parameter table **for any future `PT-xxx`**, and — critically — **do not edit `PT-034`**.

**The binding half is in place.** `BACKTEST_EVIDENCE_STANDARD.md` gains **§2.1a** plus a row in §2.1's table. It states the requirement, requires it *"even when — especially when — it differs from the rule arm's"*, **names the bias it guards** (*"A null must not be given an intrabar-favourable price… that borrows the very favourability the rule arm is being tested for"*), and sets reviewer enforcement at *"at minimum a `MINOR` `E20`"*. That is a stronger instrument than R1 asked for: R1 required the convention be stated; this also tells a future reviewer what to do when it is not.

**`PT-034` is genuinely untouched, and this was checked rather than accepted.** `git log --follow` shows **exactly one commit ever** (`a4ab65a`), and `git diff a4ab65a HEAD` on the file is **empty**. Byte-unchanged. `COMMON_PROTOCOL.md` §9 rule 7 is honoured, and the remediation's reasoning for honouring it — *"a reader of the prereg must be able to see what it did and did not fix"* — is correct and is the same principle that forbids retroactive correction.

**The documentation is accurate against the code.** Both functions were read:

| Documented claim | Code | Verdict |
|---|---|---|
| `N1`/`N1b` enter at the chosen bar's **close** | `precompute_close_entries()` calls `resolve(hi, lo, i, **cl[i]**, d, n)` | **EXACT** |
| Rule arm enters at `LOD + X` if inside the bar's range, else the bar's **low**; SHORT mirrors | `entry_for()`: `want = lod + X*PIP`; `return i, (want if lo[i] <= want <= hi[i] else lo[i])`, and the `hod`/`hi[i]` mirror | **EXACT** |

**The section-number correction the remediation flagged is right.** R1's `M2` heading says *"`PT-034` §4"* — correct, that is the prereg's `N1` table. The remediation placed the documentation in **`BT_V08_0001.md` §5**, noting §4 there is `O3`. Verified: `BT_V08_0001.md` §4 is *"`O3` — IS THE 50-PIP TARGET REACHED, WITHIN THE DAY"* and §5 is *"`O4` — THE DECISION ARM"*, under which *"The nulls, computed and printed BEFORE the rule arm"* sits. **§5 is where `N1`/`N1b` actually live, and the remediation put the note in the right place for the right reason.**

**The supporting numbers check out.** All four `N1` medians read out of the committed output are **0.2450 / 0.2426 / 0.2424 / 0.2429** — the claimed `0.2424–0.2450` is exact, not rounded to flatter. The `BT_V08_0001.md` table reproduces all four rows and both interval columns without error. The closed-form break-even is **0.250037**. The argument that a null landing within a quarter-point of the analytic value is evidence of no bias is sound, **and the note states the falsifier** — *"Had the close been favourable, `N1` would have printed above 25.00%"* — which is what makes it an argument rather than a rationalisation.

**No number, table or value in `BT_V08_0001.md` changed.** Confirmed in the diff: the file gains 48 lines and loses none.

---

## 4. ITEM 66 — the screenshot timecode — ✅ CLOSED, VERIFIED

**The timecode was re-read from the pixels by this session.** The frame's player chrome was cropped at `(968,676)`–`(1024,688)`, linear-stretched across its own dynamic range and magnified 20×. **The burned-in elapsed field reads `43:04`**, with the total field truncated at `43:0` by the frame's right edge. The remediation's reading is correct. The frame's content claim is also re-confirmed by opening the image: four rings, three labelled thresholds, **a red `?` at the centre**, `replay` button — the post-playback end card.

**All four references were updated, and there is no fifth.** This reviewer swept the repository independently for `43:10` and `43-10` rather than checking the remediation's list:

| Site | State |
|---|---|
| Filename | ✅ `V08_00-43-04_…`, via `git mv`, **rename detected at 100 %** — blob and history preserved |
| `04_SCREENSHOTS/V08/INDEX.md` row 26 | ✅ `00:43:04`, and it now states the frame is the **post-playback end card**, as required |
| `INDEX.md` "What the frames settled" item 7 | ✅ `00-43-04` |
| `V08_SOURCE_NOTES.md` §12 item 4 | ✅ `00-43-04`, with an inline `SUPERSEDED` bracket |

**The fourth site was not in R1's enumeration.** R1 named three; the remediation found the fourth by sweeping for the string instead of working the list. **That is the correct method and it is worth saying so** — R1's enumeration was incomplete, and the remediation caught the reviewer's own omission rather than discharging the letter of the instruction.

**Every surviving occurrence of the old string is legitimate**, and each was inspected: `REMEDIATION_PROTOCOL.md` §2 retention blocks in `INDEX.md`; the R1 review file, which must never be edited; `LOG.md` and `REVIEW_INDEX.md` history; and unrelated **real** `[00:43:10]` markers in V01's and V06's transcripts. **No live assertion of the wrong timecode survives anywhere in the repository.**

### 4a. The disclosed residual — adjudicated

The remediation disclosed, against its own fix, that `00:43:04` = **2,584 s** against a **2,583.745 s** runtime, so the corrected label *still* exceeds the runtime by 0.25 s and a naive `timestamp > runtime` screen will still flag row 26.

**The disclosure is accurate, the characterisation is correct, and the resolution is right.** This reviewer re-derived all 26 V08 frame timecodes mechanically: row 26 is the **only** frame over the raw runtime, at exactly `ceil(2583.745) = 2584`; under the `> ceil(runtime)` form **nothing flags**, while `00:43:10` (2,590 s) would remain a true positive. The remediation's reasoning — a player's whole-second elapsed field cannot print `43:03.75` and displays the ceiling, so the frame **cannot** carry both its true burned timecode and a strictly-under-runtime label — is correct, and matching the artifact's own internal evidence is the right choice over cosmetic conformance to a screen.

**Recording the consequence for whoever implements `Q-009`'s screen, rather than leaving a booby trap, is the behaviour this item existed to produce.** Item 66's whole charge was that V08's screenshot set tripped a test V08 itself authored. It no longer does, **and the test has been made more precise in the process.**

---

## 5. REGRESSION PASS — `REVIEW_PROTOCOL.md` §6 DIMENSIONS

The remediation could only have regressed what it touched. `git diff --stat -M a886585 HEAD` bounds that to **8 files**: three system/artifact files carrying the fixes, the renamed PNG, and four ledgers. **No script, no data file, no transcript, no pre-registration, and no homework artifact was altered.** The diff is additive but for **three** deleted lines, each read individually and each the timecode-carrying line its replacement supersedes.

| Dim | Subject | Verdict |
|---|---|---|
| **A** | Source fidelity | **PASS.** The one new block of quoted source (`Source A′`) was checked verbatim at source. Garble preserved, ellipsis honest, no qualifier dropped. See `N3` for the single bracketed expansion |
| **B** | Completeness | **NOT SATISFIED — blocked by `D-030`, structural, NOT attributable to the student, carrying NO severity charge.** Unchanged from R1 and carried on R1's and V07 R1's reasoning exactly. **Open item 36 is now owed for the fifth lesson-round running** and needs an **owner** ruling, which no student or reviewer session can supply. It did not hold V08 and does not hold it now |
| **C** | Provenance | **PASS — and improved.** Item 64 was itself a provenance item; `C-009` now carries corroboration from a second lesson and, per §2, a second speaker. Every new citation resolves |
| **D** | Explicit vs inferred | **PASS.** `Source A′` labels what it establishes and, in a separate paragraph, what it does **not** — that V07 `[00:28:15]` attests the requirement *in use* rather than restating V08's two-candle specification, which stays sourced to V08 alone. That is the audit performed on the record's own new content |
| **E/F/M** | Chart recognition, counterexamples, blind recognition | **UNCHANGED.** No example, classification or frame content was touched; the only frame operation was a 100 %-similarity rename |
| **G** | Manual backtest procedure | **PASS, checks 1–20, unchanged.** `PT-034` byte-unchanged; the crosscheck re-runs to `PASS`. Check 16 (baseline pre-registered) is **strengthened** — the null's price convention is now documented, and §2.1a binds it forward for every future test |
| **H** | Hindsight / lookahead | **PASS.** Nothing was re-run and no rule was re-specified after a result. The remediation's refusal to edit `PT-034` is the anti-hindsight rule being observed at cost |
| **I/J** | Outcome vs rule application, sample quality | **UNCHANGED.** No outcome or sample was touched |
| **K** | Homework | **UNCHANGED.** Not touched |
| **L** | Teach-back | **UNCHANGED** from R1's assessment |
| **N** | Ambiguity | **PASS.** No subjective term was quantified. §2.1a adds a *procedural* requirement, not a constant |
| **O** | Contradiction review | **PASS.** `C-009` `PROVISIONAL` upheld; §2f confirms the `D-025` guest/instructor carve-out does not apply and the record remains method-level |
| **P** | Machine-rule firewall | **PASS.** Nothing new was quantified or promoted toward automation |
| **Q** | Claimed accuracy | **UNCHANGED.** No accuracy claim touched |

**Validator: `103 passed, 0 warnings, 0 failures`**, run in this reviewer's own worktree.

---

## 6. NOTES

### N1 — `NOTE` — the presenter-identity ruling, and its one residual

Full reasoning in §2. Recorded here as the round's substantive addition to the corpus's knowledge, and carried as **open item 71** — a documentation follow-up so `C-009`'s speaker-identity row can be brought into line with the ruling by whoever next has cause to edit it. **Not owed as a defect**, and it does **not** hold V08: the row asserts no falsehood, nothing downstream depends on it, and the names remain provenance under `D-033` provision 2.

### N2 — `NOTE`, charged to PROJECT PROCESS and NOT to V08 — a concurrent session moved this working directory's branch mid-review

**Findings of fact.** This session cut `review/v08-r2` from the integration branch at `a6ee013` in the **main** working directory and began verifying there. Partway through, `git status` showed the main worktree on **`review/v09` at `bb4097b`** — a branch this session never created or checked out, belonging to concurrent V09 work. `video/v09` descends from **`f3f9006`**, which predates both the V07 R2/R3 merge (`a886585`) and the entire V08 remediation, so that tree contains **neither** the `Source A′` block **nor** the item-65/66 fixes.

**Detected, not missed.** The switch surfaced when `18_REVIEW/V07/` listed only `V07_REVIEW_R1.md` although `V07_REVIEW_R2.md` and `R3.md` are committed ancestors of the integration branch — an impossibility that prompted the check rather than an assumption.

**What was done.** A dedicated worktree was created for `review/v08-r2` at `a6ee013`, and **every** read taken after the switch was re-run there before any of it was used. Two `REVIEW_INDEX.md` reads had in fact come from the stale tree and were discarded and redone; the transcript, screenshot, runner and `git` verifications all predate the switch and were re-confirmed regardless. **No conclusion in this review rests on a read from the wrong tree.** The main working directory was left on `review/v09` as found, so the concurrent session was not disturbed.

**Why this is recorded rather than waved through.** `D-038` makes branch isolation and single-threaded merge-back a **safety** property, and V08 R1's reviewer took a dedicated worktree for exactly this reason. This incident shows the hazard is live and that the failure mode is **silent**: a reviewer reading a stale tree gets plausible file contents, no error, and would have found the remediation's work simply absent — verifying a fix against a tree that predates it. **Recommendation, offered and not imposed:** a reviewer or remediation session should take a dedicated worktree rather than switching the shared main directory, and should re-assert `git branch --show-current` before any load-bearing read. **This is an owner/process matter. It is not attributable to V08, to the remediation session, or to any lesson artifact, and no finding is charged.**

### N3 — `NOTE`, not charged — a bracketed ASR expansion a mechanical verbatim sweep will flag

`Source A′` quotes `[00:28:15]` as *"You can only go by the second **rail[road]** tracks."* The transcript body reads *"the second **rail** tracks"*. The bracket is a **transparent editorial expansion**, it is the corpus's documented reading (V07's transcript lists *"the second rail tracks"* in its own ASR-garble inventory as *"railroad tracks"*), the convention is established across V01/V07/V08, and **V07 R3 has already ruled that visibly-bracketed intra-word expansion is not a defect**. R1's own `M1` used the identical form.

**No correction is required and none should be made.** It is recorded only because a future mechanical verbatim sweep — the project runs several — will return this as a non-match, and a session that has not read this note may re-charge a closed question.

---

## 7. OPEN ITEMS — DISPOSITION AT R2

| Item | Was | Now |
|---|---|---|
| **64** | OPEN — applied, pending verification | ✅ **CLOSED — VERIFIED at R2.** Citation read at source; verbatim, honest ellipsis, garble preserved; `GUEST` tag and §6c cross-reference resolve; `PROVISIONAL` unchanged. The deliberate narrowing was **correct**, and §2 now supplies the determination it declined to assert |
| **65** | OPEN — applied, pending verification | ✅ **CLOSED — VERIFIED at R2.** `§2.1a` binds the requirement forward with a named bias and a reviewer-enforcement floor; `BT_V08_0001.md` §5 documents it for this test; both functions read and both descriptions **exact**; `PT-034` **byte-unchanged**, one commit ever |
| **66** | OPEN — applied, pending verification | ✅ **CLOSED — VERIFIED at R2.** Burned timecode re-read from the pixels: **`43:04`**. Four references updated; independent sweep finds **no fifth**; rename preserves the blob; the `ceil()` residual is real, correctly characterised and correctly resolved |
| **67** | OPEN — recommended, not owed | **UNCHANGED, still OPEN.** A `PT-034` successor with a non-hindsight second condition. Not a defect and not a gate |
| **36** | OPEN — owner ruling owed | **UNCHANGED, still OPEN.** Dimension B / `D-030`, now owed for the **fifth** lesson-round running. Needs an **owner**; did not hold V08 |
| **71** | — | 🆕 **OPEN — documentation follow-up, NOT owed as a defect.** Carry R2's presenter-identity ruling (§2) into `C-009`'s `Source A′` speaker-identity row, whose *"NOT established"* wording this round supersedes. **Does not hold V08** |
| **72** | — | 🆕 **OPEN — owner/process.** The concurrency hazard in `N2`: a concurrent session moved the shared working directory's branch mid-review. Recommend dedicated worktrees for review and remediation sessions, and a branch re-assertion before load-bearing reads. **Not attributable to V08** |

---

## 8. EXECUTIVE OUTPUT

```text
LESSON: V08
DECISION: PASS
CONFIDENCE: HIGH

CRITICAL ISSUES:
- None.

MAJOR ISSUES:
- None.

MINOR ISSUES:
- None. Items 64, 65 and 66 are CLOSED — VERIFIED at R2.

REQUIRED ACTIONS:
1. None owed by V08. The lesson is COMPLETE.
2. Carried, not owed: item 67 (PT-034 successor), item 71
   (C-009 speaker-identity row), item 72 (worktree discipline).
3. Owner ruling still owed on item 36 — Dimension B / D-030,
   fifth lesson-round running. It is not a gate and did not
   hold V08.

ADVANCEMENT:
AUTHORIZED. V08 is COMPLETE. The V09 gate was already OPEN under
D-024 and is unaffected.
```

---

## 9. WHAT THIS ROUND ESTABLISHES ABOUT THE REMEDIATION, RECORDED PLAINLY

Three things are worth stating because they are the behaviours the review system exists to elicit, and all three were produced without a reviewer present.

1. **It refused an upgrade it could not source.** R1 handed the remediation a stronger framing — *"a different guest presenter"* — and it declined to write it, in a fix whose entire subject is under-sourcing. §2 finds the stronger framing was in fact **correct**; the discipline was still right, and adopting an unverified claim because a reviewer supplied it would have been the worse act.
2. **It swept instead of working the list**, and found a fourth reference R1's own enumeration had missed.
3. **It disclosed a residual that made its own fix look imperfect** — the 0.25 s `ceil()` overhang — rather than leaving a future session to trip over it, and specified the correct screen in the process.

**Against that, R1's enumeration of item 66's references was incomplete**, and this review's own §2 shows R1 asserted the presenter difference without collecting the evidence that establishes it. Both are recorded so the audit trail is symmetric: **the remediation was more careful than the review it was discharging, on the two points where they differed.**
