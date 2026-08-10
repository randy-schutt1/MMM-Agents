# V01 — INDEPENDENT REVIEW

| Field | Value |
|---|---|
| Lesson | V01 |
| Review version | R2 |
| Review date | 2026-08-10 |
| Previous review | `18_REVIEW/V01/V01_REVIEW_R1.md` (`REVISE`, HIGH, 0 critical, 2 major) |
| Reviewer | Independent Reviewer / Teacher session (produced no V01 artifact and applied no correction) |

---

## FINAL DECISION

```text
REVISE
```

**Decision:** `REVISE`

**Confidence:** HIGH

One `MAJOR` finding stands, no `CRITICAL` findings.

The headline result of this round is narrow and specific: **`MAJOR` finding 1 from R1
was applied in three places out of four.** The withdrawn claim — that the visual
evidence *eliminates* the session-time reading of the blue/red boxes — survives
verbatim, unmarked and reading as current, in the trailing
`### Visual Evidence Update — 2026-08-10 — one candidate reading ELIMINATED` block of
`A-006` in `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md` (lines 522–545). It directly
contradicts the corrected text 45 lines above it in the same record, and it is the last
thing a reader of `A-006` sees. The ambiguity register is the file that downstream
machine-specification work will actually read, so this is the *worst* of the four places
for the overturned claim to survive.

Everything else in this round is a documentation defect. The corrections that were
applied were applied well and honestly — the remediation session marked its own
supersessions, retained original wording, refused to sweep up work it could not certify,
and reported a defect it discovered that widened its own scope. That conduct is the
reason this review is short on suspicion and long on specifics.

R1's judgement that V01 "should reach `PASS` in R2 without further study of the source"
was optimistic in one respect: ruling on `REVIEW_INDEX.md` open item 6 required opening
frames and making fresh visual determinations. That work is done below and is reported
as reviewer findings, not left as an instruction to guess.

---

## SOURCE MATERIAL REVIEWED

Inspected **first**, before opening any student artifact, per `REVIEW_PROTOCOL.md` §3.
This round is a targeted re-verification, not a repeat of R1's full pass
(`REVIEW_PROTOCOL.md` §4 — do not become a second student).

| Source | References | Purpose |
|---|---|---|
| `V01_TRANSCRIPT.md` | `[00:35:55]`–`[00:37:28]` read line by line | Adjudicate R1 findings 3 and 4 and the six-vs-four enumeration independently |
| `V01_TRANSCRIPT.md` | `[00:37:49]`–`[00:38:13]`, `[00:52:19]`–`[00:53:07]` | Verify the H4/H5 assignment text and its true timestamps |
| `V01_TRANSCRIPT.md` | `[00:38:57]`–`[00:39:04]`, `[00:43:21]`, `[00:44:45]`, `[00:51:42]`–`[00:51:50]` | Establish which frames bear on `A-007`, `A-008`, `A-009`, `A-016` |
| `V01_00-38-50_beginning-of-week-chart.png` | `[00:38:50]` | Box geometry, MA colours, the two vertical dotted lines |
| `V01_00-39-40_beginning-of-week-drawn-on.png` | `[00:39:40]` | R1 reviewer question 2 — does the freehand mark the anchor point? |
| `V01_00-40-25_beginning-of-session-chart.png` | `[00:40:25]` | "Trigger The Pendings"; whether the slide supports `S31` |
| `V01_00-43-58_beginning-of-session-drawn-on.png` | `[00:43:58]` | Live annotation bearing on `A-006` / `A-007` |
| `V01_00-44-40_end-of-week-chart.png` | `[00:44:40]` | Box geometry; the "goes into chop" region |
| `V01_00-48-35_trap-higher-level-long-holders.png` | `[00:48:35]` | `R = 70.5` / `R = 51…` / `= 43.1`; box/separator adjacency; the big entry candle |
| `V01_00-50-55_typical-week-gbpusd-m15.png` | `[00:50:55]` | Header, day labels, five printed annotations, horizontal levels |
| `V01_00-51-45_typical-week-drawn-on.png` | `[00:51:45]` | `A-009` freehand |
| `V01_00-16-55`, `V01_00-19-20` | `[00:16:55]`, `[00:19:20]` | Survey items 1–18, for R1 finding 7c and for `A-011` / `A-012` / `A-014` |
| `V01_00-02-35_managing-expectations-slide.png` | `[00:02:35]` | Five bullets, for R1 finding 7a |

**Twelve screenshots opened and read at full resolution.** Every one carried a burned-in
player timecode matching its filename — 12 for 12, consistent with R1's result and with
`INDEX.md`'s sync claim.

**Source access limitation, unchanged.** I did not listen to the audio. `N9`–`N11` and
the `[00:46:04]` / `[00:48:05]` / `[00:48:13]` session times remain unverified. No
finding below depends on them.

**Not re-tested this round** (R1 tested these and recorded them under "things checked
that passed"; `REVIEW_PROTOCOL.md` §4 forbids re-litigating them without cause, and no
cause appeared): the SHA-256 provenance root, the 144-quotation fabrication sweep, the
quarantine integrity check, and the adversarial test of the dimension G waiver.
`scripts/validate_project.py` was re-run: **97 passed, 0 warnings, 0 failures.**

---

## PART 1 — THE FOUR APPLIED CORRECTIONS

Verified against the source, not against the commit message.

### 1.1 R1 finding 1 (`E02`, MAJOR) — the box reading

**Verdict: `PARTIALLY APPLIED`. The finding is reopened as R2 finding N1.**

Three of four locations are correct:

| Location | State | Verdict |
|---|---|---|
| `V01_INTERPRETATION.md` §10.1 `U2` | Withdrawn, original wording retained and marked, points forward to `C5` | ✅ Correct, and correctly *not* deleted |
| `V01_INTERPRETATION.md` §10.2 `C5` | New entry; both readings live; `Q4` reopened; `A-006` stays `DO NOT CODE` | ✅ Correct |
| `V01_MASTERY_REPORT.md` "WHAT THE VISUALS CHANGED" | "eliminated one of two competing readings" struck through and corrected | ✅ Correct |
| `AUTOMATION_AMBIGUITIES.md` `A-006` — *Visual Characteristics* | Rewritten; "**Neither candidate is eliminated**" | ✅ Correct |
| `AUTOMATION_AMBIGUITIES.md` `A-006` — *trailing Visual Evidence Update* | **Untouched.** Header still reads "one candidate reading ELIMINATED"; body still reads "**This eliminates candidate 1**… The boxes do not align with session boundaries" | ❌ **Not applied** |

I verified the underlying visual claim myself rather than accepting either version:

- `[00:38:50]` — two vertical dotted lines sit near the left edge; the pale-blue
  rectangle's left edge coincides with the second of them.
- `[00:44:40]` — two vertical dotted separators at the right of the chart; the pale-blue
  rectangle begins immediately to the right of the second.
- `[00:48:35]` — a dashed vertical pair at the right; the pale-blue rectangle labelled
  `R = 51…` abuts it.

The sentence "The boxes do not align with session boundaries" is therefore **refuted by
the three frames it cites**. R1 was right; the surviving block is wrong on the facts, not
merely stale in tone.

### 1.2 R1 finding 2 (`E10`, MAJOR) — the D-018 / D-019 homework scope split

**Verdict: `APPLIED CORRECTLY`. Finding closed. One citation defect, logged as N4.**

I re-derived H4 and H5 from the transcript before reading the report.

- H4 — `[00:37:58]` "So I want you to start doing is on the one hour chart", `[00:38:04]`
  "I want you to start looking at the levels and the cycle." An observational instruction
  aimed at a chart.
- H5 — `[00:52:38]`–`[00:52:50]` "if you haven't marked the chart up once or twice and
  looked at Wow, same shit every week"; `[00:53:07]` "Go look at the pairs this week."

R1's substantive reading is correct and I endorse it independently: neither exercise
requires "level" to be defined. Both require a chart, a feed and a timezone — i.e. they
are blocked by `I-007`, which is the textbook `DEFERRED` case. Closing them permanently
would have discarded the only cheap empirical check available against `CL3`.

`D-019` is well-drafted. Its test — *"is there anything here to do at all"*, not *"can
this be done today"* — is the right test, it is stated crisply, it names the worked
example, and it explicitly leaves `D-018` `ACTIVE` rather than editing it, which respects
`DECISIONS.md`'s append-only rule. The mastery report's dimension F table shows the
struck-through original dispositions rather than overwriting them. Open research item 3
in `REVIEW_INDEX.md` carries H4/H5 forward. The chain is complete.

**The defect:** H5 is cited as `[00:52:20]`, `[00:53:02]` in `D-019`, in the mastery
report's dimension F table, and in `REVIEW_INDEX.md`. Those timestamps are wrong.
`[00:52:20]` is "Is this the cycle?" and `[00:53:02]` is "Sometimes it might start on
Thursday" — neither is the assignment. `V01_SOURCE_NOTES.md` §11 has it right
(`[00:52:38]`, `[00:53:07]`), and so does the transcript's own homework table. The error
originated in R1 and was propagated into a permanent `ACTIVE` decision record by the
remediation. See N4.

### 1.3 R1 finding 4 (`E13`, MINOR) — the six-vs-four trap-move mismatch

**Verdict: `APPLIED CORRECTLY`. Finding closed. One citation-range defect, logged as N6.**

`V01_SOURCE_NOTES.md` §14 now carries the mismatch. I checked the substance
independently:

```text
Slide [00:30:35]      six: week (Sun/Mon), day, session, session end, day end, week end
Spoken [00:36:49]     "beginning of the week, Sunday and Monday"          (1)
       [00:36:56]     "beginning of every day, Asian session"             (2)
       [00:37:04]     "beginning of London's day and… the U.S. day"       (3)
       [00:37:14]     "false move at the end of the session"              (4)
       [00:37:23]     "end of the day and Friday at the end of the week"  (5, 6)
Recap  [00:45:44]     "week beginning, beginning of the session, end of
                       the session, end of the week"                       (4 items)
```

Six spoken, six on the slide, four in the recap. Confirmed. The entry records the
abbreviated-recap reading **as a reading, not as a resolution**, states which evidence
tier outranks which, and adds a caution against treating the six-item list as evidence
that day-boundary traps are *taught* here. That last sentence is better than what the
finding asked for. This is the strongest of the four applied corrections.

The defect is only in the citation range: §14 gives the spoken enumeration as
`[00:36:38]`–`[00:37:09]`, which stops two items short — `[00:37:09]` is mid-list, and
the sixth item lands at `[00:37:28]`. As written the cited range contains four items, not
six, which undercuts the note's own arithmetic. See N6.

### 1.4 R1 finding 6b (`E20`, MINOR) — stale "no course material has been studied"

**Verdict: `APPLIED CORRECTLY, AND WIDENED HONESTLY`. Finding 6b closed; 6a and 6c
remain open, as the remediation itself stated.**

`CONCEPT_INDEX.md`'s status block now states the *actual* current reason for emptiness —
V01 studied, zero concepts produced, every candidate an open `DO NOT CODE` record — which
is exactly what R1 required, and it retains the superseded wording in a marked note.
`09_CHART_EXAMPLES/README.md` received the equivalent fix.

The remediation then found the same defect in two files R1 had not checked:
`AUTOMATION_AMBIGUITIES.md` and `CONTRADICTIONS.md` both declared `RECORDS: 0` while
holding 18 and 2 records. Both corrected with accurate counts. **Widening one's own
scope to fix a defect the reviewer missed, and then reporting it, is the behaviour this
project needs**, and it is recorded here so it is visible in the learning record.

`V01_TRANSCRIPT.md`'s "SCREENSHOT-WORTHY MOMENTS" still says *"**None has been
captured**"* (6a) and `SETUP_ISSUES.md` I-006's interim-handling paragraph still says
*"No item in `V01_INTERPRETATION.md` is classified `VISUAL`"* (6c). Both confirmed open.
Both were correctly reported as out of scope rather than quietly left.

---

## PART 2 — DISPOSITION OF R1'S REMAINING OPEN FINDINGS

Each was re-examined against the source this round, not carried forward on R1's word.

| R1 # | Severity | Verified this round? | Disposition |
|---|---|---|---|
| 3 | MINOR `E11` | Yes — transcript read at `[00:36:07]`–`[00:36:38]` | **UPHELD, OPEN, and WIDENED.** See below |
| 5 | MINOR `E20` | Yes | **UPHELD, OPEN.** §10.1 still opens "Four of the **eleven** undefined terms in §6"; §6 lists `A-001`…`A-017` and §6's own closing line says "Seventeen". Self-contradiction within one file |
| 6a / 6c | MINOR `E20` | Yes | **UPHELD, OPEN** (see §1.4) |
| 7 | MINOR `E20` | Yes — all three checked against the images | **UPHELD, OPEN, all three confirmed.** See below |
| 8 | MINOR `E20` | Yes — recounted | **UPHELD, OPEN, and CORRECTED: it is eight screenshots, not seven.** See below |
| 9 | NOTE `E20` | Yes | **UPHELD, OPEN.** `V01_INTERPRETATION.md:375` and `V01_MASTERY_REPORT.md:273` both still say the over-generalisation "took a screenshot to catch". `G5` — written from the transcript alone — already read the enumeration as "a list, not a principle" and already forbade writing "every session boundary" into any specification. The screenshots supplied the closed count of six; the *correction* originated in the transcript-only audit |
| 10 | NOTE `E20` | Yes | **UPHELD, OPEN, and SUBSTANTIALLY WIDENED.** See below |
| 11 | NOTE — | Yes | **UPHELD, OPEN.** `S27` still renders the ASR's "the trap moves **or** the key" as "**are** the key" unbracketed, while `S29` in the same table brackets `[intra]day` and `S38` brackets `[or]`. The reading is obviously right; only the convention slipped |
| 12 | NOTE — | Yes | **UPHELD, OPEN.** `QUARANTINE_REGISTER.md:87` still says "Relocated to `02_TRANSCRIPTS/V01/`" while a byte-identical copy remains at the original path |

### Finding 3 — widened

R1 required three recitations. Verified correct, and the same misdating occurs in three
further places R1 did not list:

```text
Quoted words:  "But if the dealer anchors in early because he completed the pattern…
                in the previous week, then you're still looking for trades away from
                the anchor point going into Friday if he issues you the signal."
Actually at:   [00:36:17]–[00:36:31]
At [00:36:38]: "Understand that the trap moves or the key to your success…"  (= S27)

Cited as [00:36:38] in:
  V01_SOURCE_NOTES.md:85      S19          ← R1 listed
  V01_SOURCE_NOTES.md:355     X3           ← R1 listed
  V01_INTERPRETATION.md:174   §6 "anchor point" usage list   ← NOT listed
  AUTOMATION_AMBIGUITIES.md:131  A-001 Evidence table        ← NOT listed
  V01_MASTERY_REPORT.md:102   "anchoring from a prior week"  ← NOT listed

X2 (V01_SOURCE_NOTES.md:354) cites [00:36:17]; its quote begins at [00:36:07].
```

`V01_INTERPRETATION.md:175` (`A-002`, "trap move") and `CONTRADICTIONS.md:138` both cite
`[00:36:38]` **correctly** and must not be changed.

### Finding 7 — all three confirmed against the images

| Row | Claimed | What the image shows | Correct value |
|---|---|---|---|
| `[00:02:35]` | `S1–S7` | Five bullets: follow along free from distraction / honest effort on all assignments / execute in demo / refrain from negativity / take your time. `S2` ("it's not the method") and `S6` (the four-week pact) are **spoken only** | `S1, S3, S4, S5, S7` |
| `[00:40:25]` | `S29–S31` | "Beginning Of Session" prints "Trigger The Pendings", "Trigger The Stops", "Beginning Of Sessions". **Nothing on the slide concerns the end of a session**, which is `S31` | `S29–S30` |
| `[00:19:20]` | `H1, A-013` | Q16 reads "Can you identify a mid week reversal" = `A-012`. No item on the slide bears on the skill threshold (`A-013`) | `H1, A-012` |

### Finding 8 — corrected upward

§4's visual-observations table runs `V1`–`V13` and covers **14** of the 22 indexed
screenshots (`V13` covers two). R1 listed seven omissions. There are **eight**:
`[00:00:35]`, `[00:02:35]`, `[00:06:15]`, `[00:09:50]`, `[00:14:10]`, `[00:24:10]`,
`[00:27:50]` — and `[00:54:30]`.

The eighth matters more than the other seven. `V01_00-54-30_typical-week-final-state.png`
is **not** an administrative slide; it is the final annotated state of the "Typical Week"
chart at lesson end. §4 covers `[00:51:45]` and `[00:52:10]` but stops before the last
drawing state. So R1's proposed remedy — "state at the head of §4 that it covers the
teaching slides only" — would be *false as stated* while `[00:54:30]` is missing. Either
add a `V14` row for `[00:54:30]` and then scope §4 to teaching slides, or extend §4 to
all 22.

### Finding 10 — substantially widened

R1 named `A-003`'s Risk cell in the INDEX table. That cell is indeed still stale
("Unknown — the word itself is unrecovered") against a status of `RESOLVED BY COURSE`.
But **five** fields inside the `A-003` record itself contradict its own resolution:

```text
Course Meaning:       "The word itself has not been recovered."          STALE
Visual Characteristics: "no screenshot exists for V01"                   STALE
Classification block: "INFERRED MACHINE CANDIDATE / NOT A COURSE RULE"   STALE
Required Research:    "Re-listening to the audio… the cheapest open
                       question in V01 to resolve"                       STALE
Impact If Wrong:      "Unknown, which is itself the problem."            STALE
Trailing block:       "RESOLVED BY COURSE — the word is 'pendings'"      CORRECT
```

`A-003` is the project's one resolved ambiguity and its showcase for resolution-from-
visual-evidence. As it stands, a reader who stops before the trailing block learns the
opposite of the truth. This is the same structural defect as N1 and should be fixed
with it.

---

## PART 3 — RULING ON REVIEW_INDEX OPEN ITEM 6 (THE 16-RECORD STALENESS)

**Ruling: the item is upheld and is real study work, but its own framing is partly
wrong, and the correct scope is narrower and differently distributed than stated.**

### 3.1 What is actually there

The sentence *"**Unknown — no screenshot exists for V01** (`SETUP_ISSUES.md` I-006). The
instructor was pointing at a slide while using this phrase…"* appears in the *Visual
Characteristics* field of 17 records. `A-006` is fixed. **Sixteen remain:** `A-001`–
`A-005`, `A-007`–`A-017`. The count in `REVIEW_INDEX.md` is exact.

Six records already carry a trailing `### Visual Evidence Update — 2026-08-10`:
`A-001`, `A-004`, `A-006`, `A-009`, `A-015`, `A-017`. Five of those six (all but `A-006`)
therefore contain a stale "no screenshot exists" field *and* an accurate visual update,
in the same record — the `A-003` pattern again.

### 3.2 Correction to the item's framing

Open item 6 names `A-009`, `A-015` and `A-017` as the records that "need fresh visual
claims". **That is the wrong trio.** All three already have visual updates, and I audited
all three this round:

- `A-009` — cites `[00:51:45]` and `[00:52:10]`; says the freehand shows *where* he is
  pointing but yields no anatomy. I opened `[00:51:45]`: a green near-vertical
  down-stroke from the Sunday/Monday high region to the Monday low, plus a loop around
  the prior consolidation. Consistent with "straight drop" and with the hedge. **Sound.**
- `A-015` — four MA lines present (yellow, red, cyan, white), no periods anywhere, and
  the inversion warning restated. Verified against `[00:38:50]`, `[00:40:25]`,
  `[00:44:40]`, `[00:50:55]`. **Sound, and the inversion warning remains the best single
  judgement call in the V01 corpus.**
- `A-017` — the large green candle breaking up out of the blue range immediately before
  the red area at `[00:48:35]`. Confirmed present. The refusal to derive a size multiple
  from one unlabelled instance is correct. **Sound.**

For these three the remaining defect is **only** the stale sentence. That is mechanical.

`A-004`'s trailing update states that a "level" is a horizontal price line on the
template and that this "eliminates the third candidate measure". Unlike `A-006`'s
elimination, this one is supported: `[00:50:55]` shows horizontal dashed lines in yellow,
red and cyan and prints *"Level Not Crossed Until Late Friday"* against one. Positive
printed evidence for one reading, not absence of evidence for another. **Upheld.**

`A-001`'s trailing update is correctly hedged — it shows structure, defines nothing, and
says so. **Sound.**

### 3.3 Where fresh visual claims *are* warranted

Four records have frames bearing directly on them and **no** visual update at all. These
are the real study work:

| Record | Frame | What bears on it | Reviewer's determination |
|---|---|---|---|
| `A-002` "trap move / false move" | `[00:30:35]`, `[00:38:50]`, `[00:48:35]` | The `[00:30:35]` slide is titled "How To Beat The Market Maker — The Trap Moves Are Made:"; `[00:38:50]` prints **"Week Beginning Trap High"** directly on the chart above the area inside the blue rectangle; `[00:48:35]` prints **"Trap Here..Higher Level Long Holders"** | **Materially constrained, still `DO NOT CODE`.** The lesson's central object is *named on screen twice, at specific chart locations*. That is more than the audio gave: it fixes *where* on a chart he applies the word. It defines nothing — no shape, no size, no invalidation — and the two labelled instances are on prepared examples with no stated outcome |
| `A-003` "pendings" | `[00:40:25]` | Already resolved; the record's own field says otherwise | **Fix the five stale fields (see finding 10 above).** No new claim needed |
| `A-008` "the tracer" | `[00:38:50]`, `[00:39:10]`, `[00:39:40]` | `[00:38:57]` "this is the tracer Sunday Monday, right?" `[00:39:02]` "**These two lines.**" `[00:39:03]` "This is Sunday." The `[00:38:50]` frame shows **exactly two vertical dotted lines near the left edge**, with the pale-blue rectangle beginning at the second | **Materially constrained, still `DO NOT CODE`.** The referent of "these two lines" is almost certainly the two vertical dotted separators bounding Sunday. Record it as *constrained*, not resolved: the deixis is not verifiable from a still frame, and nothing states what draws the lines or what the tracer measures. This is a genuine gain — `A-008` currently records the tracer as having no visual referent at all |
| `A-016` "goes into chop" | `[00:44:40]` | `[00:44:45]` "you see an outside spike to the low and the dealer goes into chop." The "End Of Week" frame shows a deep single-candle spike low, then a flat sideways range, with the pale-blue rectangle drawn over that sideways range | **Materially constrained, still `DO NOT CODE`.** The frame shows the described sequence. It gives no measure of "chop" — no range, no duration, no bar count — and one instance cannot bound one |

Two further records have *slide text* bearing on them, which is weaker but not nothing:

- `A-011` "M and W formation" — survey Q5 at `[00:16:55]` prints *"Do you clearly see
  M's/W's before they **SHIFT**?"*. Note "SHIFT" is a term that appears **nowhere** in the
  transcript. Worth recording as a printed-only vocabulary item to watch for in V02–V21;
  it does not describe the anatomy.
- `A-014` "fractional disparity" — Q8 prints *"How are you at spotting Fractional
  Disparity?"*, confirming the exact term and capitalisation. Still never explained.
- `A-012` "midweek reversal" — Q16 prints *"Can you identify a mid week reversal"*, which
  is also the fix for R1 finding 7c.

`A-007` "second leg": the `[00:43:58]` frame is on screen when `[00:43:21]` is spoken and
shows the instructor's live green marks around the small pop above the blue rectangle and
around the pullback low before the large up-candle. **I decline to convert that into a
leg definition.** He does not label a leg, does not count legs, and the drawing is
consistent with several readings. Record that the frame exists and that it does not
define the term.

The remaining records — `A-005`, `A-010`, `A-013` — have no bearing frame. `A-010` and
`A-013` are already covered by `V01_INTERPRETATION.md` §10.3's explicit "not resolved by
the visuals" list, and `A-005` is deferred to V02 by the instructor himself. For these,
the stale sentence should be replaced with an accurate statement — *screenshots exist and
none bears on this term* — which is a different and more useful claim than "no screenshot
exists".

### 3.4 Disposition

```text
Open item 6:  UPHELD — REMAINS OPEN
Scope:        4 records need a fresh visual determination (A-002, A-008, A-016,
              plus A-003's five stale fields)
              3 records gain slide-text evidence (A-011, A-012, A-014)
              1 record needs an explicit no-bearing-frame note (A-007)
              8 records are mechanical (A-001, A-004, A-005, A-009, A-010, A-013,
              A-015, A-017 — replace the sentence; four of them already carry an
              accurate visual update below it)
Framing fix:  item 6 names A-009/A-015/A-017 as needing fresh claims. They do not —
              all three already carry sound visual updates, audited above. Correct
              the item's wording when it is next touched.
```

The reviewer's determinations in §3.3 are offered as **findings, not as text to paste**.
Per `REVIEW_PROTOCOL.md` §N the reviewer may indicate what the evidence supports; the
records remain the student's to write, and R3 audits them.

---

## PART 4 — NEW FINDINGS RAISED BY THIS ROUND

| # | Severity | Code | Finding | Required action |
|---|---|---|---|---|
| N1 | **MAJOR** | E02 | `AUTOMATION_AMBIGUITIES.md` `A-006`, trailing block (lines 522–545): header reads *"one candidate reading ELIMINATED"*; body reads *"**This eliminates candidate 1**… The boxes do not align with session boundaries; they are drawn around price structures."* This is the exact claim R1 finding 1 overturned as MAJOR `E02`. It is unmarked, reads as current, contradicts the corrected *Visual Characteristics* section 45 lines above, and is refuted by the three frames it relies on — at `[00:38:50]`, `[00:44:40]` and `[00:48:35]` the pale-blue rectangle's left edge sits on, or immediately right of, a vertical dotted separator. It survives in the **ambiguity register**, which is the file downstream machine-spec work reads | Withdraw the block in place using the same convention already used at `V01_INTERPRETATION.md` §10.1 `U2` — retain the original wording, mark it `WITHDRAWN 2026-08-10 by review R1 finding 1 / confirmed R2 finding N1`, and point to the corrected *Visual Characteristics* text. Change the section header. **Do not delete it.** `A-006` stays `DO NOT CODE`; both candidate measures stay live. **Edit** |
| N2 | MINOR | E11 | `V01_SOURCE_NOTES.md:99` `S29` cites `[00:37:04]`; its quoted words ("In [intra]day, they're made at the beginning of every day, Asian session") are at `[00:36:56]`. `[00:37:04]` is `S30`. Two statements share one timestamp — the identical defect as `S19`/`S27`, missed by R1 | Recite `S29` to `[00:36:56]`. **Edit** |
| N3 | MINOR | E11 | R1 finding 3's `[00:36:38]` misdating propagates to three locations R1 did not list: `V01_INTERPRETATION.md:174`, `AUTOMATION_AMBIGUITIES.md:131` (`A-001` Evidence table), `V01_MASTERY_REPORT.md:102`. `V01_INTERPRETATION.md:175` and `CONTRADICTIONS.md:138` cite `[00:36:38]` correctly and must not be touched | Extend finding 3's recitation to all five wrong instances. **Edit** |
| N4 | MINOR | E11 | H5 is cited as `[00:52:20]`, `[00:53:02]` in `DECISIONS.md` `D-019` (line 481) and `V01_MASTERY_REPORT.md` dimension F (line 125). The assignment is at `[00:52:38]`–`[00:52:50]` and `[00:53:07]`; `V01_SOURCE_NOTES.md` §11 has it right. `[00:52:20]` is "Is this the cycle?"; `[00:53:02]` is "Sometimes it might start on Thursday". Originated in R1, propagated into an `ACTIVE` decision record | Correct both. `D-019` is append-only *as to meaning*: fix the citation in place with a dated marked note (`CITATION CORRECTED 2026-08-10 per review R2 finding N4`), not a silent edit, and not a superseding decision — the decision's meaning is unchanged. **Edit** |
| N5 | MINOR | E02 | The corrected box text states *"Pale blue sits over flat, low-range consolidation"* (`V01_INTERPRETATION.md` §10.2 `C5`; `AUTOMATION_AMBIGUITIES.md` `A-006` Visual Characteristics). True at `[00:40:25]`, `[00:44:40]` and `[00:48:35]` — but **not** at `[00:38:50]`, which the same sentence cites: there the pale-blue rectangle spans the sharp initial rise from the week-open low to the "Week Beginning Trap High", which is neither flat nor low-range. A generalisation was drawn across four frames that one of the four contradicts. Introduced during remediation, from R1's own prescribed wording | Narrow the claim to what all four frames support: the rectangles are shaded regions with both a time and a price extent; pale blue covers *flat consolidation at* `[00:40:25]`, `[00:44:40]`, `[00:48:35]` **and the initial week-opening advance at** `[00:38:50]`. Do not offer a unifying rule for what blue marks — four frames do not supply one. **Edit** |
| N6 | NOTE | E11 | `V01_SOURCE_NOTES.md` §14 gives the spoken trap-move enumeration as `[00:36:38]`–`[00:37:09]`. The list completes at `[00:37:28]`; the cited range contains four of the six items, which contradicts the note's own count. Same range appears in `V01_MASTERY_REPORT.md:338`. Originated in R1 finding 4 | Correct the range to `[00:36:49]`–`[00:37:28]` in both. **Edit** |
| N7 | NOTE | E20 | `04_SCREENSHOTS/V01/INDEX.md` `[00:30:35]` row cites "Rule supported: **S28–S33**". `S33` is the four-item recap at `[00:45:40]` and is not on this slide — it is the *other side* of the mismatch §14 now records. R1's own rule-fidelity table matched the slide to `S28–S32` | Correct to `S28–S32`. Fold into finding 7's edit. **Edit** |
| N8 | NOTE | E20 | R1 finding 8 lists seven screenshots absent from §4; there are eight — `[00:54:30]` was omitted, and unlike the other seven it is a teaching frame (the final annotated "Typical Week" state), not an administrative slide | Add a `V14` row for `[00:54:30]` before scoping §4's coverage statement, or extend §4 to all 22. **Edit** |

---

## PART 5 — DIMENSIONS RE-GRADED

Only dimensions touched by this round are re-graded. Everything else stands as R1 graded
it, per `REVIEW_PROTOCOL.md` §4.

| Dimension | R1 | R2 | Basis |
|---|---|---|---|
| Rule fidelity | `PASS` | `PASS` | Unchanged. No fabricated quotation appeared in anything I re-read |
| Provenance | `PASS` (2 corrections) | `MINOR ISSUE` | Corrections not yet applied, and the defect is wider than R1 measured: five wrong `[00:36:38]` citations, `S29`, `X2`, and H5's timestamps in three files including an `ACTIVE` decision. No orphan rules; no quotation that the recording does not contain. The evidence is sound; the citation layer is not |
| Ambiguity | `PASS` | `MINOR ISSUE` | 18 records, no premature constants, two exemplary refusals — all upheld. But `A-006` carries a self-contradiction (N1), `A-003` carries five, and sixteen records assert that no screenshot exists for a lesson with 22 indexed screenshots |
| Contradictions | `SATISFIED (logged)` | `SATISFIED (logged)` | The six-vs-four mismatch is now logged and well handled. `C-001` and `C-002` unchanged |
| Homework (F) | `MINOR ISSUE` | `PASS` | The split is applied, `D-019` is sound, H4/H5 are carried open. Only the H5 citation is wrong (N4) |
| Manual backtesting (G) | `PASS` | `PASS` | Not re-tested; no cause appeared |
| Hindsight / lookahead | `CLEAN` | `CLEAN` | The pre-/post-screenshot separation was maintained through remediation. Every superseded claim I checked was struck and retained rather than edited away — with the single exception of N1, which was *not edited at all*. No claim was quietly improved after the fact |

**On hindsight specifically.** Remediation is the moment this discipline is most likely
to break, because it is the moment a session is rewriting its own past conclusions. It
held. `U2` is withdrawn and legible; the mastery report's over-claim is struck through
and legible; `A-006`'s Visual Characteristics preserves what it replaced. That is the
right instinct, and N1 is a miss of *coverage*, not of *honesty*.

---

## PART 6 — ANSWERS TO R1'S REVIEWER QUESTIONS

**Q2 — does the `[00:39:40]` freehand show him marking the anchor point?**

**Answered: no, and it is determinable.** I opened
`V01_00-39-40_beginning-of-week-drawn-on.png`. The green freehand consists of (a) a
zig-zag traced *along* the rising candles inside the pale-blue rectangle, terminating in
an up-arrow above the "Week Beginning Trap High" label; (b) horizontal strokes and a
small scribble over the pre-open range to the left of the two vertical dotted lines; (c)
a short stroke at the right of the blue rectangle. He is tracing the shape of the
week-opening advance and marking the range it came out of. **No stroke isolates a turning
point, and nothing is annotated with a name.** This neither supports nor undermines `I7`.
`§10.3`'s statement that the visuals leave `I7` open is correct and should now cite
`[00:39:40]` explicitly as *examined and non-determinative*, rather than leaving the
question implicit.

**Q1 (minimum `I-007` specification) and Q3 (dimension B trigger)** are properly the
student's to answer on resubmission and are not blocking. They are not re-asked here;
they stand from R1.

---

## HUMAN REVIEW

```text
HUMAN REVIEW REQUIRED: no
```

Every open item is a documentation edit against verified evidence, or a visual
determination I have made explicitly above and which the next round can audit against
the same frames.

---

## ADVANCEMENT DECISION

```text
LESSON: V01
DECISION: REVISE
CONFIDENCE: HIGH

CRITICAL ISSUES:
- None.

MAJOR ISSUES:
- N1 (E02). AUTOMATION_AMBIGUITIES.md A-006's trailing "Visual Evidence Update"
  block still asserts "This eliminates candidate 1" and "The boxes do not align
  with session boundaries" — the claim R1 finding 1 overturned. Unmarked, reading
  as current, contradicting the corrected text in the same record, and refuted by
  the frames at [00:38:50], [00:44:40] and [00:48:35]. R1 finding 1 is therefore
  NOT fully applied.

REQUIRED ACTIONS:
1.  Withdraw A-006's trailing block in place, marked, retaining the original
    wording. Change its header. A-006 stays DO NOT CODE; both candidates live. (N1)
2.  Fix A-003's five stale fields — Course Meaning, Visual Characteristics, the
    classification block, Required Research, Impact If Wrong — plus the INDEX
    table's Risk cell. (R1 finding 10, widened)
3.  Clear the stale "no screenshot exists for V01" sentence from the remaining 16
    ambiguity records, per the scope in Part 3.4. Four need a fresh visual
    determination (A-002, A-008, A-016 — determinations supplied in Part 3.3);
    three gain slide-text evidence (A-011, A-012, A-014); A-007 needs an explicit
    "frame exists, defines nothing" note; the rest are mechanical.
4.  Recite: S19, X3 -> [00:36:17]; X2 -> [00:36:07]; S29 -> [00:36:56]; and the
    three further [00:36:38] instances in V01_INTERPRETATION.md:174,
    AUTOMATION_AMBIGUITIES.md:131, V01_MASTERY_REPORT.md:102. (R1 finding 3 + N2 + N3)
5.  Correct H5's citation to [00:52:38], [00:53:07] in DECISIONS.md D-019 line 481
    and V01_MASTERY_REPORT.md line 125 — marked in place, not superseded. (N4)
6.  Narrow the "pale blue sits over flat consolidation" claim; [00:38:50]
    contradicts it. (N5)
7.  Fix "eleven" -> "seventeen" in V01_INTERPRETATION.md §10.1. (R1 finding 5)
8.  Correct the two remaining stale statements: V01_TRANSCRIPT.md
    "SCREENSHOT-WORTHY MOMENTS", SETUP_ISSUES.md I-006 interim-handling
    paragraph. (R1 finding 6a, 6c)
9.  Correct four INDEX.md rows: [00:02:35] -> S1,S3,S4,S5,S7; [00:40:25] ->
    S29-S30; [00:19:20] -> A-012; [00:30:35] -> S28-S32. (R1 finding 7 + N7)
10. Resolve §4's coverage against INDEX.md's 22 — eight are missing, and
    [00:54:30] is a teaching frame, not an administrative slide. (R1 finding 8 + N8)
11. Reword the "took a screenshot to catch" claim in V01_INTERPRETATION.md §10.6
    and V01_MASTERY_REPORT.md:273. (R1 finding 9)
12. Bracket S27's [are]. (R1 finding 11)
13. Reword QUARANTINE_REGISTER.md:87 "Relocated" -> "Copied", or remove the
    duplicate. (R1 finding 12)
14. Correct the enumeration range [00:36:38]-[00:37:09] -> [00:36:49]-[00:37:28]
    in V01_SOURCE_NOTES.md §14 and V01_MASTERY_REPORT.md:338. (N6)
15. Cite [00:39:40] in §10.3 as examined and non-determinative for I7. (R1
    reviewer question 2, answered in Part 6)

CLOSED THIS ROUND:
- R1 finding 2 (E10, MAJOR) — dimension F split applied correctly; D-019 is sound
  and sets the right precedent for all 21 lessons.
- R1 finding 4 (E13, MINOR) — six-vs-four mismatch logged as a reading, not a
  resolution, with the evidence tiers correctly ranked.
- R1 finding 6b (E20, MINOR) — concept index and chart-examples README corrected;
  scope honestly widened to two further files the reviewer had missed.

UPHELD ON AUDIT:
- A-006's corrected Visual Characteristics text, A-004's, A-001's, A-009's,
  A-015's and A-017's visual updates — all six read against the frames; all sound.
- A-004's elimination of its third candidate measure is supported by printed
  evidence at [00:50:55] and is NOT the same error as N1.
- H4/H5 are DEFERRED, not NOT APPLICABLE — re-derived independently from the
  transcript.
- validate_project.py: 97 passed, 0 warnings, 0 failures.
- No fabricated quotation, no invented rule, no imported framework, and no
  premature quantification appeared in anything re-read this round.

ADVANCEMENT:
NOT AUTHORIZED
```

**On the shape of this decision.** Fifteen required actions is a long list, and thirteen
of them are wording. It would be easy to read that as bureaucracy and pass the lesson
anyway. I have not, for one reason: N1 is not wording. A claim that this project's own
reviewer graded `MAJOR` and overturned is still sitting, unmarked and reading as current,
in the register that governs what may later be coded. `REVIEW_PROTOCOL.md` §9 permits
`PASS` when "remaining issues are minor and do not corrupt downstream learning" — an
un-withdrawn elimination in `AUTOMATION_AMBIGUITIES.md` is precisely a downstream
corruption risk, and `A-003`'s five self-contradicting fields are the same defect in the
one record the project points to as its resolution success story.

Nothing here requires re-studying V01. Every action is specified to the file, and where
a fresh visual judgement was needed I made it in Part 3.3 rather than leaving it as an
instruction to guess. **R3 should be short.**

---

## REVIEWER SELF-CHECK

- [x] I inspected source evidence before student conclusions — transcript passages and
      twelve frames read before any artifact section was opened
- [x] I did not rubber-stamp the applied corrections. I re-derived H4/H5 from the
      transcript, recounted the trap-move enumeration line by line, and re-read the box
      geometry off the frames. Three corrections survived; one did not
- [x] I did not take R1 on trust either — findings 7, 8 and 10 were each verified
      independently, and each turned out to need widening or correcting
- [x] I did not import external trading frameworks, and I declined to convert the
      `[00:43:58]` freehand into a definition of "second leg"
- [x] I did not invent a resolution where evidence was insufficient — `A-008` and
      `A-016` are recorded as *materially constrained*, not resolved, and `I7` stays open
- [x] I did not manufacture objections to appear rigorous — three of eight new findings
      are graded `NOTE`, dimension F is upgraded to `PASS`, and the remediation's honesty
      is recorded as a positive result rather than passed over
- [x] I did not edit any student artifact. This session reviewed; it did not remediate
      (`DECISIONS.md` D-003)
- [x] Every required action names the file and the value to change it to
- [x] Would I let real-money execution eventually depend on this interpretation?
      **Not yet — and the reason is instructive.** The substance of V01 is in better
      shape after remediation than before it. What is not yet in shape is the *citation
      layer*: eight wrong timestamps found across two rounds, in a project whose founding
      injury was 72 files asserting timestamps that did not match their content. None of
      them changes a rule. All of them are the same reflex that produced Q-001, caught
      early and cheaply. Fix them, and V01 passes.
