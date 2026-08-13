# V08 — INDEPENDENT REVIEW R1

| Field | Value |
|---|---|
| Lesson | V08 — *"Jim's Journey in Learning and Trading MMFX"* (`Bootcamp1 Wk2 032612 Part3 (43mins).swf`, 00:43:03) |
| Review round | R1 |
| Reviewed | 2026-08-13 |
| Reviewer | Independent Reviewer / Teacher Agent |
| Student submission | `STUDENT STATUS: REVIEW REQUIRED`, `07_MASTERY_REPORTS/V08_MASTERY_REPORT.md` |
| `D-003` separation of duties | **SATISFIED.** This session authored **no** V08 artifact. It went to the source first (`REVIEW_PROTOCOL.md` §3): re-hashed the `.swf`, re-measured the audio, re-derived every load-bearing count mechanically from the transcript body, read the load-bearing frames as images, re-ran every committed script, and re-scored the homework with its own code before reading the student's grades |
| **Review basis — READ THIS** | Branch **`review/v08`, created FROM `video/v08` at `d9e4f9e`**, in a dedicated worktree at `/Users/randyschutt/Desktop/Trading/MMM-Agents-review-v08` (`D-038`). **`video/v08` is NOT merged into the integration branch.** See §3 — the merge-status question is flagged, not resolved here |
| Process disclosure | No owner directive was issued for this round. **Dimension B is scored under the standard protocol**, as V07 R1 scored it — not carved out. See §14 |

---

## EXECUTIVE BLOCK

```text
LESSON:     V08
DECISION:   REVISE
CONFIDENCE: HIGH

CRITICAL:   0
MAJOR:      0
MINOR:      3   (M1 — E11 provenance; M2 — E20 pre-registration
                 completeness; M3 — E19 timecode past runtime)
NOTE:       5   (N1 branch/merge state, N2 manifest staleness,
                 N3 conservative count, N4 dimension B, N5 an
                 independent corroboration of Q-009's mechanism)

DIMENSION B: NOT SATISFIED — blocked by D-030, structural and NOT
             attributable to the student. Scored, not carved out.
             Carries NO severity charge (see §14). Owner ruling owed
             on REVIEW_INDEX.md open item 36 — FOURTH lesson running.

BACKTEST:    PT-034 / BT_V08_0001 REPRODUCED BIT-FOR-BIT by this
             reviewer from the committed tree. Pre-registration
             ordering verified in Git. Checks 1-20 all pass. The
             §2 tautology finding is CONFIRMED and was correctly
             stated BEFORE the run, not discovered after it.

Q-009:       CONFIRMED image-by-image and hash-by-hash. The
             one-generator reduction is CORRECT and is a
             reframing, not a retraction of Q-005-Q-008.

C-009:       CONFIRMED as a genuine method-level contradiction.
             Slide text read directly from the frame. PROVISIONAL
             is UPHELD.

ADVANCEMENT: AUTHORIZED under D-024 (0 CRITICAL, 0 MAJOR).
             V09 gate OPENS. The three MINORs are carried as owed
             and must be applied before V08 reaches COMPLETE.
```

---

## 0. WHAT THIS REVIEWER VERIFIED INDEPENDENTLY, BEFORE ANY DIMENSION WAS GRADED

Nothing below was taken from a V08 artifact's own say-so. Each row is this session's own
measurement, with the method stated so it can be re-run.

| # | Claim under test | Method used here | Result |
|---|---|---|---|
| 1 | Source identity | `shasum -a 256` on the `.swf` at the canonical `Bootcamp/` path | **`6beedb40b7c2…f8b767` — matches `SOURCE_MANIFEST.md` exactly** |
| 2 | Runtime 2583.75 s | `ffmpeg` audio extract → `ffprobe` duration | **2583.745313 s.** Transcript states 2583.745306 s. Agrees to the microsecond band |
| 3 | 848 markers, 848 distinct, strictly increasing | regex over the verbatim body only | **848 / 848. First `[00:00:00]`, last `[00:42:58]`** |
| 4 | The file ends mid-argument | read the final two entries | *"Now what's inside? / What could possibly be left inside this area here?"* — **the recording stops there** |
| 5 | 15 `Steve` tokens, all third person | token count + read every hit | **15. Every one third-person**, including `[00:19:52]` *"Steve, take a breath of fresh air… Take a bow"* — a man addressing the course author from the podium |
| 6 | The C-009 "myth" slide | **read the PNG directly**; checked its burned-in timecode | **CONFIRMED.** Slide prints *"It flushes out the big trading myth that one needs CONFIRMATION IN THE SAME DIRECTION to enter a trade…"* and *"Contrary to the MYTH it is the SAFEST PLACE TO ENTER TRADES"*. Burned timecode `38:10 / 43:0x` matches the filename |
| 7 | The 3:1 slide | read the PNG directly | **CONFIRMED.** *"Becomes the Crown Jewel of the Method as one can enter even Tighter Stops thus bringing Risk Reward to 3:1 or greater!"* Burned timecode `40:10` |
| 8 | The final frame carries a literal `?` | read the PNG directly | **CONFIRMED.** Four rings, three labelled thresholds, **a red `?` at the centre**, `replay` button, burned timecode `43:04 / 43:0x` |
| 9 | A third section was planned and is absent | read the section-3 slide + transcript `[00:00:17]`–`[00:00:29]` | **CONFIRMED.** Slide prints *"Section 3: How to not "GET" Killed. A Defined Risk Lesson…"* at burned `06:04`; the audio plans *"about two hours"*; the file is 43 minutes |
| 10 | `PT-034` reproduces | re-ran `run_pt034.py` from the committed tree | **Output byte-identical to `data/pt034_output.txt`** except the absolute worktree path and `runtime_s` 7.2 vs 7.3. `pt034_results.json` differs in **one field**: `runtime_s`. Every number reproduces |
| 11 | The cross-check reproduces | re-ran `crosscheck_pt034_vs_pt033.py` | **Byte-identical. `CROSS-CHECK: PASS`** |
| 12 | Pre-registration genuinely preceded the data | `git log` on the three commits, and `--follow` on the two files | **`a4ab65a` prereg 11:34:31 → `e3a8e66` runner 11:37:43 → `1d206ab` results 11:44:33.** The prereg and the runner each have **exactly one commit** — neither was ever amended |
| 13 | Q-009's cross-lesson byte-identity | `shasum` over all 21 quarantine folders | **`17e5622c255a…` and `9791aacf6433…` present in exactly folders 05, 06, 07, 08 and nowhere else** |
| 14 | Q-009's four duplicate pairs | `shasum` + `stat` | **All four byte-identical, at the exact byte counts Q-009 states** (32,833 / 5,640 / 5,380 / 14,892) |
| 15 | Q-009's image descriptions | **opened and looked at the images** | **CONFIRMED.** `extracted_png_27.png` = the Camtasia Studio / TechSmith wordmark. `extracted_jpeg_1004.jpg` = *"Hopefully my Path can Sm"*. `extracted_jpeg_1005.jpg` = *"ooth the way for others…"*. `extracted_jpeg_1013.jpg` = the presenter's home-office photo |
| 16 | Homework score | **re-scored `v08_predictions.json` against `v08_flashcards_KEY.json` with my own code** | **5/12 = 0.42. Always-`TARGET` baseline 10/12 = 0.83. `TARGET`-half 4/5. `STOP`-half 1/7.** Every figure in the homework matches |
| 17 | Predictions preceded the key | `git show --stat` on both commits | **`e586db2` 11:49:45 commits predictions + fronts and **no key**; `c04ef2c` 11:52:14 commits the key and the score.** `v08_predictions.json` has exactly one commit |
| 18 | Comprehension probe | re-ran `comprehension_probe.py` | **Byte-identical, exit 0, 58/58** |
| 19 | Every marker citation resolves | parsed all `` `[hh:mm:ss]` `` citations in `V08_SOURCE_NOTES.md` against the transcript | **272 citations, 193 distinct, ZERO orphans** |
| 20 | Every quotation is verbatim | ellipsis-aware substring match of all `*"…"*` passages against the marker-stripped body | **177 quotes in the lesson notes: 162 verbatim from the transcript; the 15 non-matches are ALL printed slide text or quotations of other documents, each correctly attributed as such. 43 quotes in `A-059`–`A-064`: 41 verbatim, 2 printed slide text. ZERO misquotations found** |
| 21 | Validator | `python3 scripts/validate_project.py` | **103 passed, 0 warnings, 0 failures** |

### 0a. What this reviewer could NOT verify independently, stated plainly

**Frames after 00:08:56 were not re-captured by this session.** `ffmpeg` cannot read this
`.swf`'s video stream past that point — this reviewer reproduced the failure independently
(`pixel format change unsupported`, hard stop at frame 1608 of a 3 fps stream, with
`-err_detect ignore_err -fflags +discardcorrupt` making no difference), which **corroborates
`SWF_CAPTURE_RECIPE.md` §1's claim as structural rather than a missing flag**. Independent
re-capture would require standing up the Ruffle/Playwright rig, which needs an external
download and was not undertaken for this round.

**What was done instead, and why it is sufficient for the claims at issue:** the load-bearing
frames were **read as images** and cross-checked on three axes that a fabricated capture would
have to satisfy simultaneously — the **burned-in player timecode** inside the frame matching the
filename, the **platform pair-tab and watermark** matching the transcript's shorthand
(`CADJPY,M15` + `CJ` at 38:10 against the transcript's `CJ` = CAD/JPY), and the **chart's own
x-axis dates** matching the lesson's stated week (Mar 2012). All three agree on every frame
examined. `HUMAN REVIEW` is **not** flagged: the frames carry their own internal evidence and it
is consistent.

**Two further limits, recorded as limits:** the flashcard answer key existed on disk before the
predictions were written, so *"the key was not opened"* is attested by commit structure and by
the student's own declaration, not provable. And the acoustic F0 screen was not re-run here; it
is not load-bearing for any finding, since the speaker identification stands on the fifteen
third-person references alone.

---

## 1. FINDINGS

### M1 — `MINOR` (`E11`, provenance incomplete) — `C-009`'s Source A rests only on the V08 speaker's own reported speech, when the corpus independently attests the rule

`C-009` is correct and is confirmed (§5). But its **Source A** — the course's confirmation
requirement — is sourced entirely to `[00:37:07]`–`[00:37:16]`, i.e. to **this same speaker
reporting what *"our basic training"* says**, thirty seconds before he calls it a myth. As
constructed, the record is *one speaker reporting a rule and then overriding it*.

**The corpus supplies independent attestation and the record does not cite it.** `V07`
`[00:28:02]`–`[00:28:31]` — a **different lesson, a different guest presenter, equally normative
under `D-033`** — answers the second-leg direction question with *"you can only go by the second
rail[road] tracks"*, and `V07_SOURCE_NOTES.md` §6c records it as *"an admission of
indeterminacy: the direction question is answered 'you can only go by' the confirmation candle,
not by a prior rule."*

That is the confirmation requirement operating as the corpus's decision criterion in a second
lesson. Citing it converts `C-009` from *"a speaker contradicts his own report of a rule"* into
*"a rule attested across two lessons is called a myth in the third"* — materially stronger, and
it is the difference between a hygiene-flavoured record and a corpus-level one.

**Not `MAJOR`:** the conclusion is unchanged, `PROVISIONAL` stays correct, and nothing
downstream depends on the missing citation. It is a provenance gap in a record whose finding is
sound.

**Required:** add the V07 `[00:28:02]`–`[00:28:31]` citation to `C-009` Source A as
corroborating attestation, tagged `GUEST`, with a cross-reference to `V07_SOURCE_NOTES.md` §6c.

---

### M2 — `MINOR` (`E20`, pre-registration completeness) — `PT-034` §4 does not state the null's entry-**price** convention; the runner fixes it to the bar's close

`PT-034` §4's `N1` table holds constant *"instrument, day, eligible bars, target (50 pips),
stop (16.67 pips), horizon rule, direction, and `n`"* and randomizes *"the entry bar, drawn
uniformly from the day's bars excluding the last."*

**The entry *price* is neither held constant nor randomized — it is unspecified.** The runner
resolves it in `precompute_close_entries()`, whose docstring reads *"N1's entry price is the
chosen bar's CLOSE"*. The rule arm, by contrast, enters at an extreme-anchored price
(`LOD + X`, or the bar's low). So the two arms use different price conventions, and the
difference was settled in code rather than in the pre-registration.

**Why this is `MINOR` and not `MAJOR`, stated fairly to the student:**

1. **Nothing was chosen after seeing a result.** The runner was committed at `e3a8e66` before
   it was executed at `1d206ab`, and this reviewer verified it has exactly one commit. The
   discipline held; only its *location* was wrong.
2. **The convention is the natural neutral choice** — a random bar has no extreme to anchor to,
   so the close is the obvious unbiased price.
3. **It is validated by its own output.** For a 3:1 payoff the closed-form break-even is
   `16.67 / (50 + 16.67) = 25.00%`. `N1` returned **0.2424–0.2450 across four cells**, and
   `N1b` the same. A null that lands on the analytic value to within a quarter of a point is
   behaving exactly as a matched random entry must, which is strong evidence the convention
   introduced no bias.

**Required:** in any future `PT-xxx` carrying a matched-random null, state the null's
**entry-price convention** in the pre-registration's own parameter table. This is a forward
requirement; `PT-034` **must not be edited** — `COMMON_PROTOCOL.md` §9 rule 7 forbids it and the
student is right that a corrected specification is a new test.

---

### M3 — `MINOR` (`E19`, data/timecode inconsistency) — a screenshot filename and its INDEX row assert `00:43:10`, a timecode the 00:43:03 recording does not contain

`04_SCREENSHOTS/V08/V08_00-43-10_end-card-innermost-stage-unanswered.png` and
`04_SCREENSHOTS/V08/INDEX.md` row 26 both carry **`00:43:10`**. The lesson's measured runtime is
**00:43:03** (2583.75 s, a figure V08's own transcript establishes on three independent bases).
**This reviewer read the frame: its burned-in player timecode reads `43:04`.**

The frame is **genuine** — it is the post-playback end state, with the `replay` button visible —
and the content claim built on it (the literal `?`) is fully confirmed. The defect is purely the
label.

**Why it is charged rather than waved through.** `Q-009`, in this same submission, proposes as
its **first** cheap fabrication screen: *"any timestamp exceeding the lesson's runtime in
`SOURCE_MANIFEST.md`."* V08's own screenshot set contains one. A future session running the
screen `Q-009` recommends will hit this file and have to spend time establishing that the
project's own capture is not a fabrication. Internal consistency with a test the submission
itself authors is worth more than seven seconds normally would be.

**Required:** rename the file to its true burned timecode (`V08_00-43-04_…`), update
`INDEX.md` row 26 and the §"What the frames settled" item 7 reference, and state in `INDEX.md`
that the frame is the post-playback end card so the relationship to the 43:03 runtime is
explicit.

---

### N1 — `NOTE` — the branch and merge state this review was taken against, and the `D-038` ledger question, which this reviewer FLAGS and does not resolve

**Findings of fact, established by `git fetch` and inspection:**

- `video/v08` is at `d9e4f9e` and **is NOT an ancestor of** the integration branch
  `claude/add-documents-repository-fdfb3u` (`823458d`). It is **unmerged**, and it descends
  directly from `823458d` with no divergence — a clean fast-forward is available.
- `origin/video/v08` equals local `video/v08`. The work is pushed and backed up.
- This review was therefore taken on **`review/v08`, branched FROM `video/v08`**, in its own
  worktree, so V08's content was visible. This is recorded because a review of unmerged work
  read from the integration branch would have reviewed an empty set.

**The `D-038` ledger deviation is real, and the student disclosed it rather than hiding it.**
`D-038` says `DECISIONS.md`, `SETUP_ISSUES.md`, `COURSE_PROGRESS.md`, `LOG.md` and
`REVIEW_INDEX.md` are edited **on the integration branch**. The V08 session wrote to
`LOG.md`, `COURSE_PROGRESS.md`, `QUARANTINE_REGISTER.md`, `AUTOMATION_AMBIGUITIES.md` and
`CONTRADICTIONS.md` **on `video/v08`**. `LOG.md`'s V08 entry states this in its own words:

> *"it is a deviation from `D-038` and is recorded rather than resolved"* — and item 6 of its
> own open-items list carries it as **`D-038` ledger-location tension**.

**No finding is charged against the student for this, and the reason is on the record.** The
policy is one day old; V08 is the first full lesson run under it; the additions are append-only
in regions no concurrent session touched; and disclosing a tension rather than silently choosing
a side is exactly the behaviour `D-038`'s consequences section asked the first session to
produce. **It is an owner decision, not a student defect.**

**This reviewer's observation, offered and not imposed:** `QUARANTINE_REGISTER.md`,
`AUTOMATION_AMBIGUITIES.md` and `CONTRADICTIONS.md` are not in `D-038`'s enumerated list at all,
and they are the ones a lesson session must write to do its job — a lesson that cannot open an
`A-xxx` on its own branch cannot be worked in isolation. The list may need splitting into
*policy ledgers* (integration branch) and *evidence ledgers* (task branch, merged with the
lesson). **Recorded for the owner. Not resolved here, and the merge of `video/v08` is not
performed by this reviewer** — `D-038` makes merge-back a separate, deliberate, single-threaded
act.

**This review is committed on `review/v08` and pushed to `origin`. It is not merged.**

---

### N2 — `NOTE`, not charged — `SOURCE_MANIFEST.md`'s STATUS column still reads `NOT STARTED` for V08

It also reads `NOT STARTED` for V03, V04, V05, V06 and V07, all of which are studied and
reviewed. The column has been unmaintained since V02. **This is pre-existing project debt, not
V08's defect**, and charging it here would misattribute it. Recorded so it is visible; it
belongs with the existing bookkeeping open items.

---

### N3 — `NOTE`, not charged — the "186 marker citations" figure is conservative, not inflated

`V08_MASTERY_REPORT.md` §A claims **186** marker citations verified. This reviewer's own count
over `V08_SOURCE_NOTES.md` is **272 total, 193 distinct**, and **all of them resolve to real
transcript markers**. The claim understates the work rather than overstating it, and the
integrity property it asserts (every citation exists) is **independently confirmed**. No action.

---

### N4 — `NOTE` — dimension B has now cost FOUR lessons and still has no vocabulary

V05, V06, V07, V08. Open item 36 is now owed for the **fourth** consecutive round. See §14.
The student's handling is correct and is not the problem; the absence of a ruling is.

---

### N5 — `NOTE` — an independent corroboration of `Q-009`'s mechanism that the student could not have supplied

While reproducing the `ffmpeg` limitation, this reviewer extracted the raw video stream by
stream-copy and measured the tiles. **The `.swf` video stream is a delta-rectangle screen codec**
— 1,608 JPEGs in the first 8:56, with dimensions clustering at 640×360, 614×360, 576×360 and
occasional 40×42 cursor fragments. **The container's third stream is `rawvideo`, ARGB,
267×51.**

`extracted_png_27.png` — the Camtasia wordmark that `VISUAL_INDEX.md` sells as *"Session Recap
& Execution Rules"* — is **267×51**. The tile geometry and the chrome dimensions fall out of the
container's own structure. This independently corroborates, from the source side, both
`Q-009`'s *"SWF delta-tiles indexed as charts"* mode and its *"player chrome indexed as
content"* mode. **Recorded as corroboration of the student's finding, not as a new one.**

---

## 2. THE SEVEN ITEMS THE SUBMISSION ASKED TO BE CHECKED — ADJUDICATED

| # | Student's claim | Reviewer verdict |
|---|---|---|
| 1 | Speaker is 100% `GUEST`, zero course-author runtime, 4th consecutive lesson | **CONFIRMED.** 15 `Steve` tokens, every one third-person, verified by this reviewer against the body. `[00:19:52]` (*"Steve, take a bow"*) and `[00:32:17]` (*"go back to Steve's recording"*) are each independently sufficient. The `D-033` treatment is correct: tagged, and **not** demoted |
| 2 | The lecture is genuinely incomplete — 43 min of a planned ~2 h / 3 sections, ending mid-argument, literal `?` in the final frame | **CONFIRMED, and accurately characterised — neither overstated nor understated.** The plan is in the audio at `[00:00:17]`–`[00:00:29]`; section 3's slide is printed and read by this reviewer at burned `06:04`; the final two transcript entries pose a question and stop; the end card carries a red `?` at the centre, read directly. The student states this as a **property of the source**, not as a gap in its own work — which is the correct framing |
| 3 | `PT-034` `CONFIRMED AS TAUGHT`, 70.5–76.8% vs null 24.2–24.5%, break-even 25.00%; and the 3:1 claim identified as arithmetically empty | **CONFIRMED ON EVERY COMPONENT.** Re-ran the runner: output byte-identical bar the path and `runtime_s`. Rule arm at `X=10`: **0.7046 / 0.7095 / 0.7058 / 0.7676** → 70.5–76.8% ✓. `N1` medians **0.2424 / 0.2426 / 0.2429 / 0.2450** → 24.2–24.5% ✓. Break-even 25.00% ✓. Git ordering verified (§0 row 12) — the pre-registration genuinely preceded the data, and neither it nor the runner was ever amended. **The tautology was correctly identified and, critically, was stated in `PT-034` §2 BEFORE the run** — it is not a post-hoc gloss, and `BT_V08_0001` §2 reports it **first**, ahead of the verdict word. Measured realised `R` = exactly `50/X` (25.00 / 10.00 / 5.00), which is the bound, confirming the argument empirically |
| 4 | `Q-009` — one fabrication generator, previously counted as four separate failure modes across V05–V08 | **CONFIRMED, and the reduction is correct.** Hashes verified (`17e5622c255a…`, `9791aacf6433…`, present in exactly folders 05–08); four duplicate pairs verified byte-identical at the stated byte counts; four images opened and confirmed to be the Camtasia wordmark, two halves of one printed sentence, and an office photo. Timestamps verified as a constant 5-minute arithmetic sequence running 7 to 57 minutes over a 43-minute file. **One nuance worth stating precisely: this is a *reframing*, not a *retraction*.** `Q-009` does not claim `Q-005`–`Q-008` were wrong; it claims their four modes are outputs of one generator. That is the accurate and more useful statement, and the refusal to batch-discharge V09–V21 on four measurements is the right call |
| 5 | `C-009` — a normative speaker calls the course's own confirmation rule a "myth" in printed slide text | **CONFIRMED as a genuine method-level contradiction, not a misreading.** Slide text read directly from the frame by this reviewer; every spoken quotation verified verbatim; `D-033` provision 3 quoted accurately. **See M1** — the record is sound but under-sourced |
| 6 | Dimension B still blocked by undefined vocabulary, 4th lesson, standard treatment | **CONFIRMED.** M/W (`A-011`), second leg (`A-007`), trap area (`A-002`), *fast* (`A-061`) — named, none defined. `D-030` binds. Handled correctly: documented, escalated, **not** forced into a score, and **one genuine recognition task performed** on the day's extreme, the one object that is defined. See §14 |
| 7 | Homework self-assessment reported a clean negative — 0.42 against a 0.83 baseline | **CONFIRMED, and the disclosure is not softened anywhere.** Re-scored independently: 5/12 = 0.42, baseline 10/12 = 0.83, `TARGET`-half 4/5 = 0.80, `STOP`-half **1/7 = 0.14**. The submission states the heuristic *"failed worse than guessing"*, publishes the per-card table including its most confident miss, and labels the whole thing `SAMPLE INSUFFICIENT FOR INFERENCE`. Commit structure shows predictions committed **without** the answer key. This is the strongest integrity signal in the submission |

---

## 3. THE BRANCH AND MERGE-STATUS QUESTION — FLAGGED, NOT RESOLVED

Consolidated here because the reviewing instruction required it be explicit. Full detail in
**N1**.

```text
video/v08          d9e4f9e   NOT MERGED into claude/add-documents-repository-fdfb3u (823458d)
                             descends directly from 823458d; clean fast-forward available
origin/video/v08   d9e4f9e   in sync — the work is pushed
review/v08                   THIS REVIEW. Branched FROM video/v08. Pushed. NOT merged.
```

**Two decisions are owed to the owner and neither is taken here:**

1. **Whether to merge `video/v08`**, given that R1 returns `REVISE` with three MINORs owed. The
   project's own precedent (V03–V07) is that a `REVISE` with 0 `CRITICAL` / 0 `MAJOR` opens the
   next gate with minors deferred, so a merge is not blocked on remediation — but `D-038` makes
   merge-back a deliberate single-threaded act and this reviewer will not perform it.
2. **Whether `D-038`'s ledger list needs splitting** into policy ledgers and evidence ledgers —
   see N1. The V08 session's deviation is disclosed and, in this reviewer's judgement,
   substantively correct; the policy text is what needs adjusting, not the session's behaviour.

---

## 4. THE 17 DIMENSIONS

### A. Source fidelity — **PASS**

Verified mechanically rather than accepted: **272 marker citations, 193 distinct, zero
orphans**; **177 quoted passages in the lesson notes, 162 verbatim from the transcript, the
other 15 all correctly attributed to printed slides or to other documents**; 43 quotations in
`A-059`–`A-064`, 41 verbatim and 2 correctly labelled `printed`. **This reviewer found zero
misquotations.**

The submission's own account of how it got there is the notable part: the first pass **failed**
its own verbatim check on 22 fragments — silent ASR corrections inside quotation marks — and
the corrections are recorded with the glosses moved **outside** the quote marks. That is the
exact defect V07 R1 charged as `M3`, caught here by a checker rather than by reading. Terminology
is not altered; ASR mishearings are preserved in the transcript and corrected only in the notes,
with markers.

### B. Completeness / Recognition — **NOT SATISFIED — BLOCKED BY `D-030`. Scored, not carved out. No severity charge.**

See §14.

### C. Provenance — **PASS**, with `M1`

Every rule traces to a marker or a named frame. The two frames looked at before the notes were
written are disclosed with their mechanical justification, **in three files with identical
wording** — a direct response to `V05_REVIEW_R1.md` `M4`. `M1` is the one provenance gap found,
and it is an omission of available corroboration rather than an unsupported claim.

### D. Explicit vs inferred audit — **PASS**, and it is this submission's strongest habit

The 16.67-pip stop is marked `IMPLIED` everywhere it appears — in `PT-034` §1, in
`BT_V08_0001` §10, in the homework §2.2 and §5 — always beside the sentence *"V08 states no stop
distance."* The 10-pip tolerance is marked `printed`. *Fast* is refused as a rule and filed as
`A-061` with `DO NOT CODE`. The failure chain `REVIEW_PROTOCOL.md` §6D warns about — three
examples → pattern → universal rule → code — is not entered anywhere.

### E. Chart recognition audit — **PASS (scope limited by `D-030`)**

The only recognition performed is on the day's extreme, which is arithmetic. No pattern was
classified against an undefined definition. Future price was **not** used to justify a
classification: the flashcards truncate at the decision bar and the predictions were committed
before the key.

### F. Counterexample testing — **PASS**

The `NEGATIVE` battery is the evidence: 20 plausible fabrications, **15 lifted verbatim from
this lesson's own quarantined `NOTES.md` and `VISUAL_INDEX.md`**, all 20 correctly rejected, and
this reviewer re-ran the probe to byte-identical output. The near-miss case — *"stop loss 10–15
pips past High/Low of Day"*, where a real printed number is welded to a rule the lesson never
states — is identified as the dangerous one and is rejected.

### G. Manual backtest review — **PASS**, audited against checks 1–20

| Check | Finding |
|---|---|
| 1 GBP/USD primary | ✅ `D-007` |
| 2 period reasonable | ✅ `W-C′` 2013-01-06 → 2016-06-30 |
| 3–4 sequential / future hidden | ✅ entry bar excluded from every subsequent scan; verified in `resolve()` and `within_day()` |
| 5 rules known before result | ✅ **verified in Git**, §0 row 12 |
| 6–9 skipping / losers / borderline / invalid | ✅ nothing dropped for its result; the only exclusions are the two named `C8` data-hole days and a mechanical `<4 bars` rule, all counted and named |
| 10–11 outcomes / R consistent | ✅ realised `R` reported with `MAE = 0` as a **separate count**, not as infinite `R` |
| 12 screenshots | n/a — this is a corpus computation, not a chart walk. `E06` explicitly honoured: *"nothing measured off a rendering"* |
| 13–14 the right rule tested | ✅ and unusually well: the test distinguishes the claim's arithmetic half from its empirical half and says so before running |
| **15 baseline present** | ✅ `N1` + `N1b`, 1,000 iterations, distribution reported |
| **16 baseline pre-registered** | ✅ `PT-034` §4, committed at `a4ab65a`. **`M2` notes the one parameter left to the runner** |
| **17 period pre-registered** | ✅ §7, unchanged |
| **18 holdout intact** | ✅ never on disk; the runner also aborts on a holdout date. `E23` cannot occur |
| **19 sample / interval** | ✅ `n` = 1,803–2,172 per cell; Wilson 95% on every rate; sub-cells pre-labelled |
| **20 negatives retained** | ✅ §11 retains five, **including the student's own wrong prediction and a design defect in its own decision rule** |

**Two things raise this above a routine pass.** The **`O1` self-test** — pre-registered
expectation zero, measured zero in all 16 combinations — is a pipeline check labelled as one
rather than reported as a finding. And the **independent cross-check against `PT-033`** —
different session, different pre-registration, no shared code — agrees to +0.0007/+0.0010 where
the entry rules are provably identical and diverges by −0.0112/−0.0190 in the direction *and*
rough magnitude predicted **before** the comparison ran. This reviewer re-ran it to byte-identical
output. That is stronger corroboration than a re-run of either script alone.

**On the verdict word.** `CONFIRMED AS TAUGHT` is the pre-registered rule's output and is
correct as such. It is also, on its own, misleading — and the submission says so itself, at
length, in `BT_V08_0001` §6 and §10, and again in the mastery report. The reviewer's standard
(`REVIEW_PROTOCOL.md` §18) is whether real-money logic could safely depend on this: it could
not, and **the observation states that in its own words** (*"❌ Show Hi-Lo trading works. The
extreme is known by hindsight; there is no forward rule"*). No finding.

### H. Hindsight / lookahead audit — **PASS**

The hindsight is **named, quantified, and attributed** rather than smuggled. `PT-034` §4 warns
before the run that the rule arm knows where the extreme is and *"a high percentile is not
evidence the claim is correct"*; `BT_V08_0001` §6 then reports that the percentile came back
100.0 in all four cells and concludes that **the finding is the size of the hindsight advantage
(~24.3% → 70.5–76.8%), attributable entirely to extreme identification, which the course does
not teach.** That is the correct reading and it is the student's own.

The one place hindsight could have contaminated a definition — the flashcards — is controlled by
commit ordering, verified here.

### I. Outcome vs rule application — **PASS**

Kept distinct throughout. The clearest instance is the homework: the heuristic's `TARGET` half
scored 0.80 and is correctly described as **adding nothing**, because the base rate is 0.83. A
good outcome is explicitly refused as evidence of a good rule.

### J. Sample quality — **PASS**

`n` = 1,803–2,172 per cell on `PT-034`. The homework's `n = 12` is labelled `SAMPLE INSUFFICIENT
FOR INFERENCE — descriptive only` and the label is honoured in the conclusions drawn.

### K. Homework review — **PASS.** Disposition `SUCCESS AFTER CORRECTION` is **UPHELD**

Two `NOT APPLICABLE`, three `DEFERRED`, one performed. The dispositions are correct:

- **H4 (demo account) `NOT APPLICABLE`** — **UPHELD**, directly on V07 R1's ruling for the
  identical item.
- **H6 (2012 DMR) `NOT APPLICABLE`** — **UPHELD.** No subject matter now or ever.
- **H1 `DEFERRED`** — **UPHELD**, and the second blocker is a genuine new finding: the claim's
  own week (2012-03-19) lies outside a corpus that begins 2013-01-01.
- **H5 `DEFERRED`** — **UPHELD**, and it was *measured*: the token `box tool` occurs in no
  V01–V07 transcript.

`SUCCESS AFTER CORRECTION` is right: probe `R01` failed on first writing, and the correction was
to the **probe**, not the transcript — with the failure preserved in the function's docstring
because it generalises (*a mechanical count keyed on this lesson's usual phrasing will silently
undercount*). Preserving a failure that flattered nobody is the behaviour §K exists to reward.

### L. Teach-back — **PASS**

`V08_SOURCE_NOTES.md` §1 states what the lesson argues in three clauses, and the four-stage
model is reproduced in the presenter's own inside-out ordering with the ordering flagged as his.
What confirms, what invalidates and what is confused with what are all addressable from the
notes. What remains subjective is enumerated as `A-059`–`A-064`.

### M. Blind recognition — **NOT SATISFIED, with B.** Same `D-030` ground, same accounting (§14). Not separately charged.

The twelve-card drill is the nearest available substitute and it was run honestly, on the one
object that is defined, with `INSUFFICIENT INFORMATION` effectively expressed as the
`D-030` blocks on everything else.

### N. Ambiguity review — **PASS**

Six new records, twelve existing records given a V08 pass. **`A-061` is the important one** and
is correctly identified as such: an entry cue (*"that's your cue. Get in. Load up."*) whose only
criterion is an undefined adjective. This reviewer verified its six evidence rows verbatim
against the transcript and the printed frame. The record's closing observation — that the claim
has a testable *shape* (an asymmetry between the move in and the move out) that a **grid** could
test without selecting a constant — is a legitimate design note and is explicitly **not** a
closure. Correct under `D-010` and `D-030`.

**Two records were not closed and both were tempting**: `A-056` and `A-019`. Both refusals are
correct — see §5.

### O. Contradiction review — **PASS**, with `M1`

Three records, each with the right disposition:

- **`C-007` `RESOLVED — WORDING`** — **UPHELD.** The deck and the tally both say *setups*; the
  drift to *trades* is one rhetorical line drifting **away** from the prepared artifact. Logging
  a resolved record because the *setups → trades* transition is a standard route by which an
  unmeasured hit rate enters a corpus is good practice, and the binding consequence (the 29 may
  be cited only as setups) is correctly stated.
- **`C-008` `PROVISIONAL`** — **UPHELD**, and the separation it draws is the valuable part: the
  technique may be excellent and its stated justification still unevidenced. The record takes no
  position on the first, correctly.
- **`C-009` `PROVISIONAL`** — **UPHELD.** See §5 for the adjudication of the student's own
  invitation to raise it to `UNRESOLVED`. Under-sourced: `M1`.

### P. Machine-rule firewall — **PASS**, strictly

Nothing entered `12_MASTER_SPEC/`, `13_MACHINE_SPEC/`, `08_CONCEPT_LIBRARY/` or any machine
candidate. The 16.67-pip stop — the number most likely to leak, because it is arithmetic and
looks like a parameter — is refused explicitly in four separate files.

### Q. Claimed accuracy — **PASS**

V08 makes no 90–95% claim. Its performance claim is the 3:1 ratio, which is preserved, sourced
to both audio and print, tested, and reported with the finding that its headline form is
arithmetically guaranteed. No sample was manipulated toward it; the pre-registered grid is
reported whole and `X = 10` is the headline **because the lesson prints it**, not because it
performed best. (It performed **worst** of the four `X` values — reported anyway.)

---

## 5. DISPOSITIONS THE STUDENT ASKED THE REVIEWER TO SET

| # | Student's question | Reviewer's ruling |
|---|---|---|
| 1 | Should `A-056` have been **CLOSED**? Under `D-033` this speaker could close it, and V08 supplies more of the Hi-Lo method than anything in the corpus | **UPHELD — do NOT close.** The record asks *how the extreme is identified in advance*. V08's answer is *"the fast move is false"*, and `A-061` establishes that *fast* has no numeric, comparative or printed criterion anywhere in the lesson. `D-033` does not unblock `D-030` — `D-033`'s own text says a session reading it that way *"has misread it"*. Three of four components is not four |
| 2 | Is `C-009` `PROVISIONAL` or `UNRESOLVED`? | **`PROVISIONAL` UPHELD.** The staging rule is real, stated three times, and genuinely resolves *what a student should do now*. The record already states in its own Resolution block that the trained-state question is **NOT RESOLVED**, so nothing is hidden by the label. The student's argument for `UNRESOLVED` is respectable and is on the record; the difference is presentational, not substantive. **`M1` applies** |
| 3 | Should `PT-034` be re-run under a corrected decision rule? | **NO — UPHELD.** The student is right. `COMMON_PROTOCOL.md` §9 rule 7 forbids editing a pre-registration to match what was found, and a corrected second condition is a **new test**. **Recommended, not required:** pre-register a successor comparing the rule arm against a **non-hindsight** benchmark — the extreme of the first half of the day, knowable in real time. Carried as an open item, not as a correction owed |
| 4 | Is `n = 12` too small to carry even a descriptive conclusion? | **No, as labelled.** The label `SAMPLE INSUFFICIENT FOR INFERENCE — descriptive only` is applied and honoured. The conclusion actually drawn — *my reading of the heuristic failed* — is a statement about the student's own reasoning, not an inference about the market, and 12 cards support it |
| 5 | Dimension F's two `NOT APPLICABLE`s | **Both UPHELD.** See §4 K |
| 6 | The presenter's name | **UPHELD.** *Probable and unresolved* is the honest record. The `[00:17:29]` *"Jim's right about that one"* datum is preserved rather than smoothed, three readings are offered, none chosen, and nothing depends on it — `D-033` provision 2 exactly |

---

## 14. DIMENSION B — EXPLICIT ACCOUNTING, AND WHY IT CARRIES NO SEVERITY CHARGE

**Graded `NOT SATISFIED`. Scored, not carved out.** No owner directive was issued for this
round, so the standard protocol applies, as it did at V07 R1.

**No severity charge.** The cause is structural: V08's recognisable objects — M/W formations
(`A-011`), second legs (`A-007`), trap areas (`A-002`), railroad tracks, pins, and the *fast*
cue (`A-061`) — are **named by the course and defined by nobody**. Recognising them would mean
recognising the student's own inventions and attributing the result to the course. That is
precisely what `D-030` forbids, and refusing is compliance, not failure.

**What the student did instead is the right response and is credited:** one recognition task
**was** performed, on the one object in the lesson that is defined without invention — the day's
extreme, which `PT-034` establishes is arithmetic — with predictions committed before the key.
The result was a clean negative and was published as one.

**This is the fourth consecutive lesson (V05, V06, V07, V08) to be un-gradable on B, and the
fourth round in which `REVIEW_INDEX.md` open item 36 is owed and unanswered.** Four sessions
have now disposed of it four different ways. The vocabulary gap — a third disposition for work
`EXCLUDED BY DECISION`, distinct from `NOT APPLICABLE` and from `DEFERRED` — is not a student
problem and cannot be closed by a student or by this reviewer. **Escalated, for the fourth
time.**

**It does not gate.** Under `D-024` the progression gate follows severity, and B carries none.

---

## 15. REQUIRED CORRECTIONS

Specific, per `REVIEW_PROTOCOL.md` §10. **Three items, all `MINOR`. None blocks V09.**

1. **`M1`** — Add to `11_CONTRADICTIONS/CONTRADICTIONS.md` `C-009` **Source A** a corroborating
   citation to **V07 `[00:28:02]`–`[00:28:31]`** (*"you can only go by the second rail[road]
   tracks"*), tagged `GUEST`, cross-referenced to `V07_SOURCE_NOTES.md` §6c, with one sentence
   stating that the confirmation requirement is therefore attested in a second lesson by a
   second normative speaker and not only in this speaker's report of it. **Do not change the
   `PROVISIONAL` disposition.**

2. **`M2`** — Forward requirement, **no edit to `PT-034`**. In the next `PT-xxx` carrying a
   matched-random null, state the null's **entry-price convention** explicitly in the
   pre-registration's parameter table. Record the requirement wherever the project keeps its
   backtest conventions (`BACKTEST_EVIDENCE_STANDARD.md` or `COMMON_PROTOCOL.md` §5) so it binds
   the next session rather than living only in this review.

3. **`M3`** — Rename `04_SCREENSHOTS/V08/V08_00-43-10_end-card-innermost-stage-unanswered.png`
   to `V08_00-43-04_end-card-innermost-stage-unanswered.png` (its own burned-in timecode);
   update `04_SCREENSHOTS/V08/INDEX.md` row 26 and the §"What the frames settled" item 7
   reference; and add one clause to row 26 stating that the frame is the **post-playback end
   card**, so its relationship to the 00:43:03 runtime is explicit and it does not trip
   `Q-009`'s own first screen.

**Not required, recommended** (carried as open items, not as debt against V08):

4. Pre-register the successor test described in §5 row 3 — a decision rule whose second
   condition uses a **non-hindsight** benchmark.
5. Owner ruling on **open item 36** (dimension B vocabulary) — fourth lesson running.
6. Owner ruling on the **`D-038` ledger-location question** raised in N1, and on whether to
   merge `video/v08`.

---

## 17. DECISION

```text
LESSON:     V08 — "Jim's Journey in Learning and Trading MMFX"
DECISION:   REVISE
CONFIDENCE: HIGH

CRITICAL ISSUES:
- None.

MAJOR ISSUES:
- None.

MINOR ISSUES:
- M1  E11  C-009 Source A omits available corroboration from V07.
- M2  E20  PT-034 §4 leaves the null's entry-price convention to the runner.
- M3  E19  A screenshot filename asserts 00:43:10 on a 00:43:03 recording.

REQUIRED ACTIONS:
1. Add the V07 [00:28:02]-[00:28:31] citation to C-009 Source A.
2. Record the null-entry-price-convention requirement for future PT-xxx.
3. Rename the end-card frame to 00-43-04 and correct INDEX.md.

ADVANCEMENT:
AUTHORIZED under D-024 (0 CRITICAL, 0 MAJOR). The V09 gate OPENS.
The three MINORs are deferred and still owed; V08 reaches COMPLETE
only at R2.
```

### Why `REVISE` and not `PASS`

`REVIEW_PROTOCOL.md` §9's fourteen `PASS` conditions are met on thirteen. The exception is
**condition 2** — *important rules have provenance* — which `M1` breaches in one record, and
condition 14's *"remaining issues are minor and do not corrupt downstream learning"* is
satisfied, which is why the gate opens. This is the project's established treatment and it is
applied here without adjustment.

### Why `HIGH` and not `MEDIUM`

The load-bearing claims were not accepted on the submission's authority. The backtest was
**re-executed and reproduced bit-for-bit**; the pre-registration ordering was **verified in Git,
including that neither the prereg nor the runner was ever amended**; the homework was
**re-scored with this reviewer's own code**; the quarantine finding was verified **by hash and
by opening the images**; the quotations and marker citations were **re-derived mechanically**,
finding zero misquotations in 220 quoted passages; and the three headline slide claims were
**read directly off the frames**. The one verification not performed — independent re-capture of
frames after 08:56 — is disclosed in §0a with the reason and with what was done instead, and no
finding in this review turns on it.

### A statement this review should make plainly

The reviewer's job is to withhold confidence, not to award it. But `REVIEW_PROTOCOL.md` §1 is
explicit that independence is not reflexive disagreement, so the following is stated as a
finding of fact rather than as praise: **this submission's most important results are the ones
that are unflattering to it, and it reports them first.** The lesson's single performance number
is identified as arithmetically empty *before* the data is touched. The verdict word the
pre-registered rule returns is `CONFIRMED AS TAUGHT`, and the observation spends two sections
explaining why that word must be read narrowly. The pre-registered decision rule is disclosed as
defective **by the session that wrote it**, and is not edited. The homework heuristic is scored
against a baseline that beats it, and the losing half is broken out at 0.14. A quarantine audit
that could have counted four findings counts one generator instead.

Three minor corrections are owed. Nothing in the method is wrong.

---

## 18. LOGGING

Logged in `LOG.md` under **2026-08-13 — Reviewer Session (V08 R1)**, on branch `review/v08`.
`18_REVIEW/REVIEW_INDEX.md` updated in the same round: decision-table row, STATUS block, error
counts, severity totals, and open items **64–66** (`M1`–`M3`) plus **67** (the successor test)
and **68** (the `D-038` ledger-location question).

**Not merged.** `D-038` makes merge-back a separate, deliberate, single-threaded act, and both
`video/v08` and `review/v08` await the owner's decision — see §3.

**Next review trigger:** V08 R2, on student resubmission with `M1`–`M3` applied.
