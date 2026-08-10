# V01 — INDEPENDENT REVIEW

| Field | Value |
|---|---|
| Lesson | V01 |
| Review version | R3 |
| Review date | 2026-08-10 |
| Previous reviews | `V01_REVIEW_R1.md` (`REVISE`, HIGH, 0 critical, 2 major); `V01_REVIEW_R2.md` (`REVISE`, HIGH, 0 critical, 1 major, 15 required actions) |
| Reviewer | Review session, R3 |

---

## FINAL DECISION

```text
PASS
```

**Decision:** `PASS`

**Confidence:** HIGH

Zero `CRITICAL`, zero `MAJOR`, zero open `MINOR`. Two `NOTE`s carry forward as open
research items; neither bears on what V01 understood.

**R2's one open MAJOR is closed.** `A-006`'s trailing "Visual Evidence Update — one
candidate reading ELIMINATED" block is withdrawn in place: the header now says
`WITHDRAWN, no candidate reading eliminated`, the original text is retained in full and
marked `DO NOT CITE`, and the refutation is recorded beside it. I re-opened the three
frames the block relies on before accepting the withdrawal rather than taking R1's or
R2's word for it. All fifteen of R2's required actions are applied.

**Disclosure of this round's shape.** This session applied the corrections *and* renders
the verdict, at the project owner's direction. That departs from `DECISIONS.md` D-003,
which separates the two. It is recorded here rather than glossed. Two things mitigate it
and one does not:

- Every determination written into a record was verified against the primary source
  first — nine screenshots opened at full resolution, the transcript read at every
  timestamp changed. Nothing was taken on a prior review's word, and **two of R2's own
  claims did not survive that check and are corrected below**.
- Every edit is a documentation fix. No test was invalid, because no test was performed;
  there is no evidence layer here that a rewording could launder.
- What is *not* mitigated: an independent session did not audit this round's work. A
  reader should weigh the `PASS` accordingly, and V02's review — which is a genuinely
  fresh session — should spot-check `A-006` and `A-003` while it is in those files.

---

## SOURCE MATERIAL REVIEWED

Inspected before opening any student artifact, per `REVIEW_PROTOCOL.md` §3. This round is
a verification pass against R2's fifteen actions plus the evidence each rests on — not a
repeat of R1's full audit (`REVIEW_PROTOCOL.md` §4).

| Source | Purpose |
|---|---|
| `V01_TRANSCRIPT.md` `[00:34:47]`–`[00:37:49]` | Re-derive the `[00:36:38]` cluster, `S29`, the six-item enumeration, and the day-count acknowledgement, line by line |
| `V01_TRANSCRIPT.md` `[00:52:10]`–`[00:53:21]` | Re-derive H5 independently of R1, R2 and the source notes |
| `V01_TRANSCRIPT.md` `[00:38:57]`–`[00:39:12]`, `[00:43:02]`–`[00:44:13]`, `[00:44:41]`, `[00:45:31]`–`[00:45:55]`, `[00:17:44]`, `[00:27:35]`, `[00:30:40]` | Establish what bears on `A-002`, `A-007`, `A-008`, `A-011`, `A-016`, and `S33` |
| `V01_00-38-50_beginning-of-week-chart.png` | Box geometry vs the two vertical dotted lines; the "Week Beginning Trap High" label; whether pale blue is over flat range |
| `V01_00-44-40_end-of-week-chart.png` | Box/separator adjacency; the spike low and the chop range |
| `V01_00-48-35_trap-higher-level-long-holders.png` | Box/separator adjacency; the printed title's placement |
| `V01_00-40-25_beginning-of-session-chart.png` | Finding 7 row 2; `A-003`'s printed evidence |
| `V01_00-39-40_beginning-of-week-drawn-on.png` | R1 reviewer question 2 — does the freehand mark the anchor point? |
| `V01_00-46-05_end-of-week-drawn-on.png` | Whether the captured frame recovers the garbled session times |
| `V01_00-54-30_typical-week-final-state.png` | The `V14` row's content |
| `V01_00-02-35`, `V01_00-16-55`, `V01_00-19-20`, `V01_00-30-35` | Finding 7's three rows and N7 |

**Nine screenshots opened and read at full resolution**, plus three re-read from R2's
list. Every one carried a burned-in player timecode matching its filename.

**Source access limitation, unchanged.** No audio was listened to. `N9`–`N11` and the
`[00:46:04]` / `[00:48:05]` / `[00:48:13]` session times remain unverified — and the
`[00:46:05]` frame, opened this round, **does not** show them, so the audio route is now
the only one left. No finding below depends on them.

**Not re-tested this round:** the SHA-256 provenance root, the 144-quotation fabrication
sweep, the quarantine integrity check, the dimension G waiver.
`scripts/validate_project.py`: **97 passed, 0 warnings, 0 failures.**

---

## PART 1 — THE FIFTEEN REQUIRED ACTIONS

Verified against the source and the frames, not against the diff.

| # | Action | Verdict |
|---|---|---|
| 1 | Withdraw `A-006`'s trailing block in place, marked, original retained, header changed | ✅ **APPLIED.** See Part 2 |
| 2 | Fix `A-003`'s five stale fields + the INDEX Risk cell | ✅ **APPLIED.** All five carry their original wording and a correction; the Risk cell now reads "Contained" with the reason |
| 3 | Clear the stale "no screenshot exists" sentence from the remaining 16 records | ✅ **APPLIED.** Zero live instances remain; all 16 survive only inside retained-original quotes. Scope honoured: fresh determinations for `A-002`/`A-008`/`A-016`, slide-text for `A-011`/`A-012`/`A-014`, a "frame exists, defines nothing" note for `A-007`, accurate no-bearing-frame statements for `A-005`/`A-010`, pointers to the existing updates for the rest |
| 4 | Recite `S19`, `X3` → `[00:36:17]`; `X2` → `[00:36:07]`; `S29` → `[00:36:56]`; three further `[00:36:38]` instances | ✅ **APPLIED**, all seven. I re-derived each from the transcript. `X2` is written as the range `[00:36:07]`–`[00:36:15]` rather than a bare start, which is what R2's own proposed convention asks for. `V01_INTERPRETATION.md:175` and `CONTRADICTIONS.md:139` are untouched, correctly |
| 5 | Correct H5's citation in `D-019` and dimension F, marked in place | ✅ **APPLIED.** `D-019` carries a dated `CITATION CORRECTED` note, is **not** superseded, and remains `ACTIVE`. Re-derived: `[00:52:38]`–`[00:52:50]` and `[00:53:07]` are the assignment; `[00:52:20]` is "Is this the cycle?" and `[00:53:02]` is "Sometimes it might start on Thursday" |
| 6 | Narrow the "pale blue sits over flat consolidation" claim | ✅ **APPLIED**, and better than asked. `A-006` now carries a four-row frame-by-frame table and states explicitly that no unifying rule for blue is offered. `C5` carries the matching note |
| 7 | "eleven" → "seventeen" in §10 | ✅ **APPLIED**, with the reason recorded |
| 8 | The two remaining stale statements | ✅ **APPLIED.** The transcript's "SCREENSHOT-WORTHY MOMENTS" note enumerates which flagged moments were captured, and names the one whose *purpose* was not served (`[00:45:55]`–`[00:46:35]`, the session times). `I-006`'s interim paragraph is marked stale with both false statements named |
| 9 | Four `INDEX.md` rows | ✅ **APPLIED**, all four checked against the images by me. See the qualification in Part 3 |
| 10 | Resolve §4's coverage against the 22 | ✅ **APPLIED** in the order R2 required: `V14` added for `[00:54:30]` **first**, then the coverage statement. The statement is now true; R1's version would not have been |
| 11 | Reword "took a screenshot to catch" | ✅ **APPLIED** in both files, each recording that `G5` caught it from the transcript alone |
| 12 | Bracket `S27`'s `[are]` | ✅ **APPLIED** — now consistent with `S29`'s `[intra]` and `S38`'s `[or]` |
| 13 | `QUARANTINE_REGISTER.md` "Relocated" → "Copied" | ✅ **APPLIED**, with a correction to R2's own description — see Part 3 |
| 14 | Enumeration range → `[00:36:49]`–`[00:37:28]` | ✅ **APPLIED** in both files. I recounted: the six land at `[00:36:49]`, `[00:36:56]`, `[00:37:04]`, `[00:37:14]`, `[00:37:23]`, `[00:37:28]` |
| 15 | Cite `[00:39:40]` as examined and non-determinative for `I7` | ✅ **APPLIED.** I opened the frame and confirm the description: a zig-zag along the rising candles ending in an up-arrow near the "Week Beginning Trap High" label, strokes over the pre-open range left of the two dotted lines, a short stroke at the blue rectangle's right edge. **No stroke isolates a turning point; nothing is named** |

---

## PART 2 — THE MAJOR FINDING, CLOSED

`A-006`'s trailing block asserted *"This eliminates candidate 1"* and *"The boxes do not
align with session boundaries; they are drawn around price structures."*

**I verified the refutation myself before accepting the withdrawal**, because the whole
point of this finding is that it survived two rounds of being asserted and re-asserted:

- `[00:38:50]` — two vertical dotted lines near the left edge. The pale-blue rectangle's
  left edge **coincides with the second**.
- `[00:44:40]` — two vertical dotted separators toward the right. The pale-blue rectangle
  **begins immediately to the right of the second**.
- `[00:48:35]` — a dashed vertical pair at the right. The pale-blue rectangle labelled
  `R = 51…` **begins at the second**.

Three frames, three coincidences, on the frames the block itself cites. The sentence is
refuted on its own evidence.

The withdrawal is executed to the convention: header changed, original text retained in
full and blockquoted under **"ORIGINAL TEXT — WITHDRAWN, DO NOT CITE"**, refutation
stated beneath it, status restated as `DO NOT CODE` with both candidates live and `Q4`
fully open. It matches how `U2` was handled in `V01_INTERPRETATION.md` §10.1. **Nothing
was deleted.**

**On N5, the generalisation introduced by remediation.** Confirmed at `[00:38:50]`: the
pale-blue rectangle spans the sharp advance from the week-open low to the "Week Beginning
Trap High". That is neither flat nor low-range, and the corrected record now says so with
a per-frame table instead of a summary sentence. The corrected text offers no unifying
rule for blue and says explicitly that four frames do not supply one. That is the right
altitude.

---

## PART 3 — CORRECTIONS TO R2, AND WHAT R3 FOUND ON ITS OWN

R2 asked to be audited against the same frames. It was, and three of its statements needed
adjusting. None changes R2's decision or its required actions; all three would have entered
the corpus as fact if pasted.

### 3.1 "SHIFT appears nowhere in the transcript" — **refuted**

R2 Part 3.3 proposed logging "SHIFT" (survey question 5, printed at `[00:16:55]`) as a
printed-only vocabulary item on the basis that the word appears **nowhere** in the
transcript. It appears at `[00:17:45]` — *"Do you clearly see M's and W's before they
shift away from the level?"* — where the instructor reads the question aloud, and again
in garbled form at `[00:27:35]`.

This inverts the finding's interest. The slide is the **shortened** form; the **spoken**
version carries the extra qualifier *"away from the level"*, which ties `A-011` to
`A-004` and is the more informative of the two. `A-011` records the correction explicitly
so a later session does not re-derive the wrong version from R2.

### 3.2 "No item on the `[00:19:20]` slide bears on `A-013`" — **overstated**

Question 12 prints *"Have you doubled a demo account? Y N"*. That is the printed origin of
`A-013`'s candidate measure 1 and of `S8` (`[00:20:00]`, "if you can't double a demo you
got no business going live").

R2's required change is nonetheless correct and is applied — `Rule supported` →
`H1, A-012` — because Q12 does **not** define the skill threshold the record exists to
hold open: it is a yes/no fact attached to *going live*, not to relaxing the blue-box rule
or trading both directions. But the basis is narrower than R2 stated, `INDEX.md` now names
Q12 explicitly, and `A-013` records what it does and does not establish.

### 3.3 "A byte-identical copy remains at the original path" — **half right**

R1 finding 12 and R2 both described the V01 transcript as having a byte-identical copy at
the original path. The original **is** still there
(`01_SOURCE_VIDEOS/.../01_Bootcamp1_Wk1_031812_Part1_55mins/TRANSCRIPT.md`, git-ignored),
so "Relocated" was always wrong and "Copied" is right. But the two are no longer identical:
the working copy has gained the homework, screenshot-moment and transcription-notes
appendices — 3,097 lines against 2,930. The spoken content is unchanged. The register now
says this precisely, which matters: the untouched original is the artifact a future
integrity check would diff against.

### 3.4 Three further `E11` defects, found and closed this round

Found while applying action 4, verified in the transcript, all corrected:

```text
"It's more than what I've told you. I understand that."
  Cited as [00:36:17] in 6 places   Actually at [00:36:13]-[00:36:15]
  [00:36:17] is the NEXT statement ("But if the dealer anchors in early…" = S19/X3)
  Fixed in: V01_SOURCE_NOTES.md ×2, V01_INTERPRETATION.md ×2,
            V01_MASTERY_REPORT.md, CONTRADICTIONS.md

"Trap move / false move" first use
  Cited as [00:33:33]              Not a marker; [00:33:32] is "And have access to it"
  First occurrence is [00:30:40]   "Now let's talk about some trap moves…"

S33, the four-item recap
  Cited as [00:45:40]              [00:45:40] is "so we're talking about trapping those"
  Actually at [00:45:44]           §14 already had this right
```

The `[00:36:17]` cluster is the same defect R1 found once and R2 found four more times,
propagating one further step. It is now closed: **every quotation in the V01 corpus
resolves to a marker carrying its words.** I checked this mechanically across all
quote-bearing rows in the source notes, not by sampling.

### 3.5 One `E20` — the status blocks stale a **third** time

`AUTOMATION_AMBIGUITIES.md` read `RECORDS: 18 / LESSONS STUDIED: 1` against 28 records
and two lessons; `CONTRADICTIONS.md` read `RECORDS: 2 / LESSONS STUDIED: 1` against four
records. Both blocks were corrected under R1 finding 6b and both were invalidated again by
the V02 pass. Corrected, with the second correction marked as a second correction so the
recurrence is visible rather than smoothed away.

**This is the concrete case for R2's protocol implication.** Three failures on the same two
blocks is not a lapse; it is a missing session-close step. Recommended for promotion from
suggestion to requirement at the 25% review.

### 3.6 What was deliberately **not** corrected

Six cited timestamps in V01 files are not transcript markers at all — `[00:25:51]`,
`[00:30:44]`, `[00:35:38]`, `[00:38:02]`, `[00:39:43]`, `[00:40:26]`. Each lands *inside*
the passage it cites, typically 2–4 s past the nearest marker, and each resolves to the
correct words. (`[00:33:33]` was in this set and **was** corrected, because it also pointed
at the wrong content.)

They are left as they are, and the reason is a matter of principle rather than effort:
fixing them is exactly the `STUDY_PROTOCOL.md` amendment R2 proposed and explicitly
deferred to the 25% cumulative review. Retro-fitting an unadopted rule to old work, in the
same round that certifies the lesson, is how a standard gets applied inconsistently. They
are recorded under `REVIEW_INDEX.md` open item 7 as the strongest argument for adopting it.

**Answering the question directly:** R2 did propose the `STUDY_PROTOCOL.md` amendment —
in the `REVIEW_INDEX.md` escalation note and open item 7, not in the review file's
required-action list — and explicitly scheduled it for `CUMULATIVE_25.md`. It is left as a
proposal. Applying it now would be a protocol change made by a lesson-level review, which
is not that review's authority.

---

## PART 4 — DIMENSIONS RE-GRADED

Only dimensions R2 downgraded are re-graded. Everything else stands as R1 and R2 graded it
(`REVIEW_PROTOCOL.md` §4).

| Dimension | R1 | R2 | R3 | Basis |
|---|---|---|---|---|
| Rule fidelity | `PASS` | `PASS` | `PASS` | No fabricated quotation in anything re-read. `S27`'s ASR normalisation is now bracketed |
| Provenance | `PASS` | `MINOR ISSUE` | **`PASS`** | Every quotation resolves to a marker carrying its words — checked mechanically across the source notes, not sampled. Eleven citations corrected across three rounds. No orphan rules; no quotation the recording does not contain. Six non-marker approximations remain, each resolving to the right passage, carried as a `NOTE` under an adopted-later protocol amendment |
| Ambiguity | `PASS` | `MINOR ISSUE` | **`PASS`** | `A-006`'s self-contradiction withdrawn; `A-003`'s five stale fields corrected; all 16 "no screenshot exists" assertions cleared. 28 records, no premature constants. The three new determinations (`A-002`, `A-008`, `A-016`) are all recorded as *materially constrained*, none as resolved, and each states what it does **not** add |
| Contradictions | `SATISFIED (logged)` | `SATISFIED (logged)` | `SATISFIED (logged)` | `C-001` unchanged and still `UNRESOLVED`; the six-vs-four mismatch well handled |
| Homework (F) | `MINOR ISSUE` | `PASS` | `PASS` | H5's citation now correct in `D-019` and the mastery report |
| Manual backtesting (G) | `PASS` | `PASS` | `PASS` | Not re-tested; no cause appeared |
| Hindsight / lookahead | `CLEAN` | `CLEAN` | `CLEAN` | The discipline held through a second remediation. Every withdrawn claim is retained and legible; the `A-006` block was **not** deleted even though deleting it would have been tidier and no one would have noticed |

**On the ambiguity dimension specifically.** The three new determinations are the part of
this round most at risk of over-reach, because a remediation under pressure to close a
finding is exactly when a "materially constrained" quietly becomes a "resolved". They do
not. `A-008` states that the deixis is not verifiable from a still frame and that nothing
says what the tracer measures. `A-016` states that the frame gives no range, no duration
and no bar count. `A-002` states that two labelled instances on prepared examples with no
outcome cannot bound a definition. All three end `DO NOT CODE`. That is the correct
handling, and it is the reason this dimension returns to `PASS` rather than being carried
as a residual concern.

---

## PART 5 — WHAT IS CARRIED FORWARD

`PASS` here is not "V01 is finished". Six research items travel with it
(`REVIEW_INDEX.md`), and two deserve naming:

- **`C-001` — the day-count contradiction — is still `UNRESOLVED`, and V02 did not
  resolve it.** C-001's own record named "a later lesson refines it" as the most likely
  route out; V02 is that lesson and it did not. This does not justify `BLOCKED` (R1 ruled
  on that and I do not disturb it — no further work on V01 can resolve what the recording
  does not say), but it should be re-tested at every weekly-holding-period lesson and
  raised explicitly at the 25% review if still open. **No artifact may commit a day-count
  value.**
- **`I7` stays `INFERRED / Low`** and is re-adjudicated at V02. The `[00:39:40]` frame is
  now recorded as examined and non-determinative, so the cheap route is closed.

**A process finding, logged as open item 9 and not held against V01.** `D-004` makes
reviewer `PASS` the only progression gate, and `COURSE_PROGRESS.md` recorded `V02 GATE:
CLOSED` — yet a complete V02 student pass was performed while V01 was in remediation. V01's
`PASS` makes it moot going forward and none of the V02 work is discarded. But the gate did
not hold, and the value of a gate is entirely in its holding. **V03 is gated behind V02's
reviewer `PASS`**, and the correct next action is an independent V02 review session, not
V03 study.

---

## HUMAN REVIEW

```text
HUMAN REVIEW REQUIRED: no
```

Every closed item was verified against the transcript or the frames. The two open `NOTE`s
are a deferred protocol amendment and a process observation, neither of which requires a
human judgement about the trading material.

---

## ADVANCEMENT DECISION

```text
LESSON: V01
DECISION: PASS
CONFIDENCE: HIGH

CRITICAL ISSUES:
- None.

MAJOR ISSUES:
- None. R2 finding N1 (E02) is CLOSED. AUTOMATION_AMBIGUITIES.md A-006's trailing
  "Visual Evidence Update" block is withdrawn in place, header changed, original
  text retained in full and marked DO NOT CITE, refutation recorded beside it.
  Verified independently against [00:38:50], [00:44:40] and [00:48:35]: on all
  three, the pale-blue rectangle's left edge sits on or begins at a vertical
  dotted separator. A-006 stays DO NOT CODE; both candidates live; Q4 fully open.

REQUIRED ACTIONS:
- None for V01.

CLOSED THIS ROUND:
- All 15 of R2's required actions, verified against the source rather than the
  commit.
- R1 findings 3, 5, 6a, 6c, 7, 8, 9, 10, 11, 12 — the full remaining R1 backlog.
- R2 findings N1 (MAJOR), N2, N3, N4, N5 (MINOR), N6, N7, N8 (NOTE).
- REVIEW_INDEX open item 6 (the 16-record staleness) and open item 8 (I-006
  frame-rate staleness, whose own R2 framing was stale in turn — D-020 is
  RETRACTED and D-021 records the speedup works at 40x).
- Three further E11 defects found by R3 and closed: the [00:36:17] acknowledgement
  cluster (6 locations), "trap move" first use [00:33:33] -> [00:30:40], and S33
  [00:45:40] -> [00:45:44].
- One further E20 found by R3 and closed: the ambiguity and contradiction STATUS
  blocks were stale for a third time after the V02 pass.

CORRECTED IN R2 ITSELF:
- "SHIFT appears nowhere in the transcript" — refuted; it is spoken at [00:17:45]
  with the extra qualifier "away from the level".
- "No item on the [00:19:20] slide bears on A-013" — overstated; Q12 prints
  "Have you doubled a demo account?", the printed origin of A-013's candidate 1.
  R2's required change is still correct and is applied.
- "A byte-identical copy remains at the original path" — the original remains, but
  the working copy has since gained appendices (3,097 vs 2,930 lines).

CARRIED FORWARD (do not lose):
- C-001 UNRESOLVED and foundational. V02 did not resolve it. No artifact may
  commit a day-count value.
- I7 stays INFERRED / Low; re-adjudicate at V02. [00:39:40] is now recorded as
  examined and non-determinative.
- H4 / H5 DEFERRED pending I-007.
- [00:46:04] / [00:48:05] / [00:48:13] need an audio re-check. The [00:46:05]
  frame was opened this round and does NOT show the session times.
- STUDY_PROTOCOL.md citation-hygiene amendment: proposal stands, deferred to
  CUMULATIVE_25.md. Six non-marker timestamp approximations are left in place
  deliberately as the case for it.
- The V02 gate did not hold. V03 is gated behind V02's reviewer PASS.

ADVANCEMENT:
AUTHORIZED

V02 opens. V03 does NOT — D-004 requires reviewer PASS on V02 first, and the V02
student pass is already complete and AWAITING REVIEW.
```

**On passing a lesson whose central objects are all still undefined.** V01 names seventeen
load-bearing terms and defines none of them. Its Confirmation and Invalidation columns are
empty across all eight rows. `PASS` here does not certify that the method is understood —
it certifies that **what the lesson actually contains has been recorded accurately, that
what it does not contain has not been invented, and that every claim traces to a timestamp
or a frame that carries it.** That is the whole of what a framing lesson can be graded on,
and it is the standard `REVIEW_PROTOCOL.md` §9 sets: remaining issues minor, downstream
learning uncorrupted.

The thing that earns the `PASS` is not the polish. It is that across three rounds the
corpus never once acquired a fact it did not have. Eleven citations were wrong and every
quotation was real. One generalisation was too wide and was withdrawn rather than softened.
A resolution that was offered on a plate — reading `R = 70.5` as a risk-to-reward ratio —
was refused. That is the behaviour that makes the later phases of this project survivable.

---

## REVIEWER SELF-CHECK

- [x] I inspected source evidence before student conclusions — transcript passages and
      nine frames read before the corresponding artifact section was opened
- [x] I did not rubber-stamp R2. Three of its statements needed correcting, two of which
      would have entered the corpus as fact if its determinations had been pasted
- [x] I did not rubber-stamp the corrections either. The `A-006` refutation, the `N5`
      contradiction at `[00:38:50]`, H5's timestamps, the six-item enumeration and the
      `[00:39:40]` freehand were each re-derived from the primary source
- [x] I did not import external trading frameworks. `A-011` still has no M/W anatomy,
      `A-007` still has no leg definition, and the `[00:43:58]` freehand was again
      declined as a definition
- [x] I did not invent a resolution where evidence was insufficient — `A-002`, `A-008`
      and `A-016` are all *materially constrained*, all still `DO NOT CODE`
- [x] I did not manufacture objections to appear rigorous, and I did not manufacture a
      clean sheet either: six known-imperfect citations are left in place and named
      rather than quietly fixed to make the round look complete
- [x] **I did edit student artifacts this round**, contrary to `DECISIONS.md` D-003, at
      the project owner's direction. It is disclosed at the head of this file rather than
      omitted, and the V02 reviewer should spot-check `A-006` and `A-003`
- [x] Would I let real-money execution eventually depend on this interpretation?
      **Not on V01's content — there is no executable rule in it to depend on.** On the
      *record* of V01: yes. It says what was taught, marks what was not, and every
      timestamp now points at the words it claims. R2 wrote "fix them, and V01 passes."
      They are fixed.
