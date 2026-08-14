# V15 — INDEPENDENT REVIEW

| Field | Value |
|---|---|
| Lesson | **V15** · `Bootcamp1 Wk7 050612 Part1 (52mins).swf` · session **2012-05-06, Week 7**, Part 1 of a two-part recording whose Part 2 is V16 |
| Review version | **R1** |
| Review date | 2026-08-14 |
| Previous review | none |
| Reviewer branch | `review/v15`, cut from the integration branch @ `61042e5` (**post-`D-045`…`D-050`**), own worktree at `MMM-Agents-v15-review` (`D-038`) |
| Submission reviewed | `video/v15` @ `d60324b` (7 commits, `9dea4c1`…`d60324b`), branched from `ddd226f` and merged forward to `fb9eee5` at `08a0cd4` |
| Independence | **`D-003` satisfied.** This session authored no V15 artifact. It located the source `.swf` from `SOURCE_MANIFEST.md` and **re-computed its SHA-256**; extracted the audio itself and **re-transcribed the load-bearing passages on a different runtime from the student's** — `faster-whisper` / CTranslate2 at `large-v3`, against the student's `openai-whisper` PyTorch `medium.en` + `large-v3-turbo`; **re-derived `PT-043` end to end** in code sharing no line with `run_pt043.py` or `mmm_lib`, parsing the raw HistData CSVs directly; re-ran every `Q-016` `diff` and re-computed all three SHA-256s itself; **counted the `Q-016` transcript negatives in its own parser**; opened the load-bearing frames as images and read their burned-in timecodes; and **went back to V13's own `.swf` and re-transcribed the Week-6 lines from audio** — the check the submission itself declared it had not done |

---

## FINAL DECISION

```text
REVISE
```

**Decision:** `REVISE` — **0 CRITICAL, 0 MAJOR, 6 MINOR, 13 NOTE.**

Under `DECISIONS.md` **D-024**, a round carrying zero `CRITICAL` and zero `MAJOR` **opens the gate
for V16.** `COURSE_PROGRESS.md` currently reads *"V16 GATE: CLOSED until V15's R1 returns
(`D-004`)"* — that was the correct state to hold, and on the merits **this review opens it.**

> ⚠️ **THE GATE BEING OPEN IS NOT AN INSTRUCTION TO WALK THROUGH IT.** `D-024` rules on finding
> severity and has nothing to say about the owner's standing comprehension/gap audit, which V14 R1
> recorded as undischarged and which item 185 still carries. The owner's hard stop was lifted for
> **V15 only**, by an instruction naming V15. **The gate is open; whether there is a V16 pass at
> all remains the owner's call.**

The six minors are carried in `REVIEW_INDEX.md` as items **197–202** and are owed before V15 can
reach `COMPLETE`. **None of them touches a lesson conclusion, a record's disposition, or
`PT-043`'s result.** Four are documentation; one is a mechanism claim that contradicts the ledger
it cites; one is an obligation created by a decision that landed 45 minutes after this branch filed
the record it applies to, and is expressly **not** charged as conduct.

**Confidence: HIGH.**

Confidence is high because every load-bearing claim was re-derived from source rather than read:

- **`PT-043` was independently re-implemented and it reproduces.** Reviewer-written code — its own
  CSV parser, its own EST→`America/New_York` conversion, its own session-day rule, its own
  completeness filter, its own `N1`/`N2`/`N3` controls, written from `PT-043` §§3–6 before
  `run_pt043.py` was opened — returns **`O1` = 0.3645** against the committed **0.3640**, an
  **`N1` control median of 0.3762** against **0.3757**, **`O1` − `N1` = −0.0117 exactly as
  committed**, **`O2` = 0.0955** against **0.0939**, **`O3` = 0.2437** against **0.2427**, and a
  **median nearer-distance of 21.40 pips — exact to the committed figure.** The `N3` band census
  reproduces to three decimals. **The verdict is unchanged in every cell.**
- **The lesson's central contradiction was re-transcribed and it is verbatim.** `large-v3` on
  audio extracted from the SHA-verified `.swf` returns *"They'll move. They'll creep up or creep
  down to try to fit price action, so to speak… They're a moving grid… **Not repaint**, they adjust
  for price action"* — **both halves of `C-022`, in one unbroken passage.**
- ⭐ **The attack the submission named as its weakest point is CLOSED IN ITS FAVOUR, from audio.**
  `V15_MASTERY_REPORT.md` §7.1: *"If V13's 'week six through ten' is a mis-transcription, the whole
  reading falls. I did not re-verify V13's audio."* This review did. V13's `.swf` SHA-256
  re-verified `106bb863…67807`; `large-v3` returns *"**Next session is going to be Sunday the
  29th.** That's two weeks… we'll take a two-week break, and then we'll get started again with
  **week six through ten** or six through, I don't know how many we're going to do yet."*
  **Verbatim. The Week-6 dating stands.**
- **`Q-016`'s three SHA-256s reproduce exactly**, all three `diff`s reproduce, and **every one of
  its transcript negatives was independently counted** in reviewer code over the 492-marker body:
  `M15` 0 · `5/13` 0 · `10 to 15` 0 · `fake breakout` 0 · `level 1`/`level one` 0 · `level three` 3
  · `trap` 3. **The fabricated stop-loss rule occurs zero times, confirmed.**
- **The frames were opened and read.** Both forum-post dates were read off the pixels by this
  reviewer — `April 30, 2012, 03:12:23 AM` and `April 28, 2012, 07:57:45 PM` — as were the
  `6pm-10pm with Sat as the Indicator chart setup day.` line and the five-item Week-7 roll-call.
  **Each frame carries its own burned-in timecode and each matched its filename.**
- **Pre-registration ordering was re-proven, not read.**
  `git cat-file -e 1a3667e:06_MANUAL_BACKTEST/scripts/run_pt043.py` → **ABSENT** at 13:19:35; the
  runner appears at `6b4d4a3`, 13:21:04; results at `2b78501`, 13:23:47. The post-run diff on the
  pre-registration file is **the RUN banner plus one line of the STATUS block, and nothing else.**

---

## SOURCE MATERIAL REVIEWED — **FIRST, BEFORE ANY STUDENT CONCLUSION**

| Source | References | Purpose |
|---|---|---|
| `02_TRANSCRIPTS/V15/V15_TRANSCRIPT.md` verbatim body | **All 492 markers, `[00:00:00]`–`[00:51:56]`** | Primary evidence. Read **before** the source notes, interpretation, homework, backtest or mastery report were opened |
| **The source `.swf` itself** | SHA-256 re-verified `5308c350…82b49`; audio extracted to 16 kHz mono, measured **3125.4466 s** against the submission's **3125.4465** | **Independent ASR.** Twelve passages re-transcribed on **`faster-whisper` / CTranslate2 `large-v3`** — a different engine and runtime from the student's `openai-whisper` |
| **V13's source `.swf`** | SHA-256 re-verified `106bb863…67807`; `[00:05:12]`–`[00:05:52]` and `[00:07:30]`–`[00:07:55]` re-transcribed | ⭐ **The submission's own named attack point.** The Week-6 date and the Orlando date, from audio |
| The load-bearing frames | `00-14-20`, `00-16-00`, `00-05-55`, `00-07-15` opened at full resolution; burned-in timecodes read | Verify the forum-post dates, the web-class slide line and the roll-call — **and this is where `M5`'s counter-datum was first suspected** |
| `_QUARANTINE_UNVERIFIED_NOTES/per_lesson/14_…` and `15_…` | All three files `diff`ed in full; all three SHA-256s recomputed; `RULES.md` read end to end | Independent re-derivation of `Q-016` §§1–5. **This is where `M4` came from** |
| `datasets/HISTDATA_GBPUSD_M1/raw/*.csv` | **Parsed directly**, 2013→2015; 2014 SHA-256 re-verified against `raw/SHA256SUMS.txt` | Independent re-derivation of `PT-043` |
| `02_TRANSCRIPTS/V10/V10_TRANSCRIPT.md` `[00:13:03]`–`[00:13:44]` | Read at source | Adjudicate `PT-043` §1a's *"different object"* defence (attack point 3) |
| `00_SYSTEM/SWF_CAPTURE_RECIPE.md` §10 `sweep.mjs` | Read line by line on **both** `video/v15` and integration; confirmed byte-identical | Check `INDEX.md` §0.3's mechanism claim. **This is where `M2` came from** |
| `DECISIONS.md` `D-003`, `D-004`, `D-024`, `D-026`–`D-031`, `D-035`, `D-036a`, `D-038`/`D-038a`, `D-039`, `D-043`, `D-044`, `D-045`–`D-050`; `REVIEW_PROTOCOL.md` §6a; `COMMON_PROTOCOL.md` §§1–6 | Read | Governing policy |

**Source access was not limited.** The `.swf`, its audio, V13's `.swf`, the transcript, all 37
curated frames, the quarantined tree, the raw M1 corpus and the recipe were all available. Nothing
in this review is capped by missing evidence, with the one standing exception the submission itself
records at item 196: **the 623 sweep frames are not committed**, so §2's negative-space scan is not
repository-reproducible for the 586 uncurated frames — the same limit V12 R1 recorded at item 140,
V13 R1 at 160 and V14 R1 at 171.

## STUDENT ARTIFACTS REVIEWED

| Artifact | Reviewed |
|---|---|
| `V15_TRANSCRIPT.md` — header, clock-convention table, speaker table + 6 strands, verification table, 12 corrections, 5 flags | ✅ in full |
| `V15_SOURCE_NOTES.md` · `V15_INTERPRETATION.md` Q1–Q2 and beyond | ✅ |
| `04_SCREENSHOTS/V15/INDEX.md` §0–§4 **+ the load-bearing frames** | ✅ |
| `05_HOMEWORK/V15/V15_HOMEWORK.md` §0–§3 | ✅ in full |
| `PT-043_…md` · `BT_V15_0001.md` · `data/pt043_output.txt` · `data/pt043_results.json` | ✅ in full |
| `06_MANUAL_BACKTEST/scripts/run_pt043.py` | ✅ — **opened only AFTER the reviewer's own re-derivation had run and printed** |
| `07_MASTERY_REPORTS/V15_MASTERY_REPORT.md` §1–§7 | ✅ in full |
| `QUARANTINE_REGISTER.md` `Q-016` · `A-095`–`A-100` · `C-022` | ✅ in full |
| `LOG.md`, `COURSE_PROGRESS.md`, `REVIEW_INDEX.md` items 189–196 | ✅ |

---

## CRITICAL FINDINGS

**NONE.**

The seven places a `CRITICAL` could plausibly have arisen were checked directly and all seven are
clean:

1. **A holdout breach (`E23`).** `PT-043` runs `W-B` = 2014-01-05 → 2015-12-31 and `W-A` =
   2015-01-04 → 2015-12-31, both wholly inside `D-035` DEVELOPMENT. My own re-derivation loaded
   **only** 2013–2015 and reproduces every headline figure. **The 2016H2 holdout was never opened,
   and neither was `D-044`'s 2017–2025** — the submission explicitly declined the extension in
   `PT-043` §4 as unnecessary to the question, which is the correct instinct.
2. **Post-hoc threshold movement (`E21`).** `git diff 1a3667e video/v15` on the pre-registration
   file is **the RUN banner plus one line of the STATUS block, and nothing else.** No threshold, no
   band, no window, no arm, no outcome measure, no decision rule and no prediction moved.
3. **Pre-registration ordering.** Proven by commit-timestamp and object existence, not asserted.
   See the confidence block above.
4. **Selective reporting (`E25`/`E09`).** Both `D-031` arms are reported in all four cells; the
   `N3` band census — the table that most invites a post-hoc band rescue — is printed **with the
   prohibition against using it repeated beside it**; the five largest-range days are named and
   **not excluded**; the Arm-B exclusion asymmetry is disclosed **before** a reviewer found it; and
   the 5/5 prediction score is **discounted by the session that earned it**.
5. **A fabricated rule reaching an artifact.** No V15 artifact cites `NOTES.md`, `RULES.md` or
   `VISUAL_INDEX.md` as evidence — verified by `grep` across the V15 set. The fabricated stop-loss
   rule is quarantined and quoted **only** inside `Q-016`.
6. **Hindsight/lookahead in the lesson's own rule (`E08`).** The lesson's headline confluence rule
   was **not** backtested, and the reason — `C-022` + `A-100` make an ADR level's past visibility
   undecidable — was **pre-registered in `PT-043` §1b before the run**, not offered afterwards as an
   excuse. This is the single best judgement call in the submission and it is the opposite of the
   failure mode `REVIEW_PROTOCOL.md` §17.2 exists to catch.
7. **Guest material admitted as doctrine (`D-025`/`D-033`).** No second voice exists; see the
   speaker section below.

## MAJOR FINDINGS

**NONE.**

⚠️ **`M2` was weighed for `MAJOR` and deliberately not charged there. The reasoning is recorded so
the owner can overrule it.** `M2` is a mechanism claim that contradicts the committed script it
cites, and it sits in front of the owner as an actionable policy edit — which is `MAJOR`'s
*"meaningful misunderstanding, but localized"*. Against that: the **measurement** it decorates is
correct and independently verified; **`SWF_CAPTURE_RECIPE.md` §8a's per-lesson measurement
requirement is explicitly preserved by the same paragraph**; the edit was **deliberately not
applied** (`D-038a`) and is flagged `PUT TO R1 / OWNER`; and nothing in V15's lesson content,
records, frames or backtest depends on it. Applying the proposed fix would be a **no-op**, not a
corruption. `REVIEW_PROTOCOL.md` §8 forbids softening a `MAJOR` to unblock work — this is not that;
it is a wrong explanation attached to a correct measurement and a correct policy, which §8's own
`MINOR` definition covers. **Charged `MINOR`, flagged loudly, with a specific remediation.**

---

## MINOR FINDINGS

### `M1` — `A-095` misidentifies which of its own three figures `PT-043` tests · `E11`/`E20` · item 197

`A-095` tabulates three pip figures and then says:

> *"**Figure 2 is the exception** — it names a period (a week) and a unit, and can therefore be
> measured… **`PT-043` pre-registers exactly that**, and only that."*

and its `Current Status` block reads:

```text
Figure 1 (25-50 pips daily):  UNTESTABLE AS STATED.
Figure 2 (600-1000 wk range): TESTABLE -> PT-043, pre-registered before any result.
```

**Both statements are wrong, and they are wrong in the direction that erases the session's own best
work.** `PT-043` pre-registers and runs **Figure 1** — the 25–50-pip daily close — and `PT-043`
**§1b** says of Figure 2, in bold: *"V15's other quantitative claim, 'The weekly range is 600 to
1000 pips'… is **DELIBERATELY NOT RE-TESTED**"*, because `PT-036` `M1` already returned
`CONTRADICTED AS STATED` on it.

**Four other artifacts state it correctly** — `PT-043` §1/§1a/§1b, `BT_V15_0001.md` §0, the homework
§3 row 5 and §3's *"deliberately NOT done"* list, and `V15_MASTERY_REPORT.md` §3.4 (*"V15's one new
measurable claim"*). **`A-095` is the isolated error — and it is the durable ambiguity record a
later session reads first**, which is exactly the file where this mistake costs the most: a session
reading only `A-095` would believe Figure 1 was never tested and that the already-contradicted
Figure 2 had been re-run.

**Required:** correct `A-095`'s exception paragraph and its `Current Status` block so Figure 1 reads
`TESTED -> PT-043 / BT_V15_0001, NOT SUPPORTED` and Figure 2 reads `ALREADY CONTRADICTED BY PT-036
M1 / BT_V10_0001; NOT re-tested, per PT-043 §1b; V15 adds DURABILITY only`. Do not edit `PT-043` or
`BT_V15_0001` — they are right.

### `M2` — `INDEX.md` §0.3's mechanism claim contradicts `SWF_CAPTURE_RECIPE.md` §10, and the fix it proposes is already the code · `E20` · item 198

`04_SCREENSHOTS/V15/INDEX.md` §0.3 states:

> *"`SWF_CAPTURE_RECIPE.md` §10's `sweep.mjs` clicks play, then **waits a fixed `1500 ms`**… and
> **only then** sets `const t0 = Date.now()`."*

and puts a durable fix to the owner at item 190:

> *"**set `t0` immediately before `p.mouse.click(...)` and take the guard screenshot afterwards**,
> which removes the 15-second term entirely."*

**The committed script does the opposite of what is described, and it already does what the fix
proposes.** `SWF_CAPTURE_RECIPE.md` §10, verified **byte-identical on `video/v15` and on
integration**, reads:

```js
const t0=Date.now();                      // <-- t0 is set FIRST
const before = await p.screenshot();
await p.mouse.click(PLAY_X, PLAY_Y);      // <-- click comes AFTER t0
await p.waitForTimeout(1500);             // <-- the guard comes AFTER the click
```

Consequences, in order of how much they matter:

1. **The proposed policy edit is a no-op.** `t0` is already set immediately before the click; only
   the `before` screenshot sits between them, and the guard is already taken afterwards. Applying
   item 190 would change nothing and would remove no 15-second term.
2. **The stated formula is unsupported.** `offset ≈ guard_ms / 1000 × SPEED + latency` is derived
   from an ordering the script does not have, so the identification of the guard as *"the dominant
   term"* is not established. ⚠️ **This review does not supply a replacement mechanism** — the
   `sweep.log` and per-frame capture timings are not committed, so the true cause of the observed
   `+15` is not determinable from the repository. `REVIEW_PROTOCOL.md` §4 applies: **the evidence
   is insufficient and this review says so rather than inventing a resolution.**
3. ⚠️ **What is NOT affected, and this is most of it.** The **measurement** — `+15 s` on 8 frames
   spanning 52 minutes plus the clamped tail, origin-not-rate confirmed on two independent delta
   pairs — rests on pixels and is untouched. **§8a's mandatory per-lesson measurement stands**, and
   §0.3 itself says so twice. Frames are named from the burned timecode, which is correct
   regardless. **Item 186's conclusion — that the offset cannot be hardcoded — is unaffected and
   remains right.**

⭐ **The danger being guarded against is not the wrong formula; it is the fix.** If the owner applied
item 190 believing the 15-second term had been removed, a later session could reasonably conclude
§8a's measurement was no longer load-bearing and skip it — which is precisely the dropped step item
186 was opened to prevent.

**Required:** (a) withdraw §0.3's mechanism paragraph and its formula, or re-derive it against the
actual script and publish the derivation; (b) withdraw the proposed edit at item 190, or restate it
against the script's real ordering; (c) **retain §0's measurement table and §8a unchanged** — they
are correct and independently verified.

### `M3` — `COURSE_PROGRESS.md`'s progress table still carries V15 as `NOT STARTED` · `E20` · item 199

The narrative block and the `V16 GATE` section were both updated for the student pass. The
`PROGRESS TABLE` was not:

```text
| V15 | Wk7 P1 | 00:52:05 | ✅ | ⚠️ | ⬜ | ⬜ | ⬜ | ⬜ | — | — | NOT STARTED |
```

**Notes, Screenshots, Homework, Manual Backtest and Student Mastery are all `⬜` and the final
status reads `NOT STARTED`**, on a lesson with a verified transcript, 37 curated frames, a full
source-notes/interpretation pair, a homework artifact, a pre-registered and executed backtest and a
mastery report. Every other completed lesson's row is filled in. **The same file now contradicts
itself**, and the progress table is the one place a new session looks first.

**Required:** update the V15 row to match V14's pattern —
`✅ | ✅ | ✅ | ✅ | ✅ | ✅ | REVIEW REQUIRED | R1 REVISE 0C/0M/6m/13n | IN REMEDIATION (items 197–202) · V16 GATE OPEN`.

### `M4` — `Q-016`'s `diff` line counts use two different conventions, and one reference count is wrong · `E20` · item 200

**Every substantive claim in `Q-016` verified.** The three SHA-256s reproduce exactly; the
`VISUAL_INDEX.md` clone is real with zero content lines changed; the two "Instructor Statements"
occur zero times in 492 markers; the `NOTES.md` EMA table is wrong on four of five rows under
`D-043` and *"Raspberry"* appears nowhere in the corpus. The defect is in the arithmetic labels:

| Section | Register says | Measured this session |
|---|---|---|
| §1 `VISUAL_INDEX.md` | *"8 differing lines = FOUR changed pairs"* | ✅ **8 differing lines**, 16 total `diff`-output lines. Correct |
| §3 `RULES.md` | *"**24 differing lines**"* | ❌ **12 differing lines**; 24 is the **total `diff` output**, including hunk headers and `---` separators |
| §4 `NOTES.md` | *"**10 differing lines**"* | ❌ **6 differing lines**; 10 is the total `diff` output |
| §3 `RULES.md` | *"**three** `VIDEO_15`→`VIDEO_16` visual references"* | ❌ **two.** `RULES.md` contains exactly two `VIDEO_16` strings. Three is `VISUAL_INDEX.md`'s count, carried across |

§3's and §4's own enumerations are right (6 changed pairs and 3 changed pairs respectively); only
the totals and the word *"three"* are wrong. **Nothing in the fabrication finding moves.**

**Required:** restate §3 and §4 on §1's convention (differing lines, and the pair count), and
correct *"three"* → *"two"*.

### `M5` — the Orlando conclusion is stated more categorically than the source supports, and the strongest contrary datum is in the file the session mined and is never engaged · `E02`/`E03` · item 201

`V15_INTERPRETATION.md` Q1 §1 is headed *"Orlando — CLOSED, and the answer is **'no recording was
ever made'**"*; `V15_MASTERY_REPORT.md` §3.1 repeats *"**the Orlando recording was never made**"*
and *"the answer is that no recording exists"*.

**The source says something narrower.** V15 `[00:05:21]`, confirmed verbatim by this reviewer's
independent `large-v3` pass:

> *"The same shit that happened in Orlando **where I didn't get a recording out of there** is
> exactly why I'm not streaming this class or doing it again."*

*"I didn't get a recording out of there"* establishes that **no usable recording resulted**. It does
not establish that **none was attempted** — and the difference is not academic, because the corpus
contains the contrary datum, in the very lesson this session mined for the Week-6 dating:

> V13 `[00:02:26]`–`[00:02:30]`: *"But **we will try to either stream it and record it or just
> record it. So we'll hang it in the forum** in place of the boot camp for next Sunday."*

⭐ **This line was re-transcribed from V13's audio by this reviewer and it confirms verbatim** —
`large-v3` returns *"But we will try to either stream it and record it or just record it. And we'll
hang it in the form \[forum\]."* **It is not a transcript artifact.**

**V13 states an intention to record Orlando and to publish it.** V15 then reports the outcome. The
sequence *intended → attempted → nothing usable came out* fits both statements; *"never made"* fits
only one and is contradicted by the other. **The V15 artifact set cites V13 `[00:01:55]`,
`[00:05:20]`, `[00:05:33]` and `[00:07:41]` — four lines from the same eight minutes — and never
`[00:02:26]`.** For a session whose declared method is to look for what would defeat its own
reading, missing the one line in its own cited passage that bears against it is the finding.

⚠️ **The operative conclusion survives intact and is not disturbed:** there is no Orlando file, none
is recoverable, and no session should look for one. `A-092`'s practical disposition is right.

**Required:** restate the Orlando conclusion as *"no recording was obtained; the corpus holds no
Orlando file and none is recoverable"* in `V15_INTERPRETATION.md` Q1 §1, `V15_MASTERY_REPORT.md`
§3.1 and item 191; and cite V13 `[00:02:26]` beside it, with the reading that the attempt failed
rather than that it was never made.

### `M6` — `C-022` does not name a `D-048` rung · **NOT CHARGED AS CONDUCT** · item 202

`C-022` is a **Tier 1 against Tier 1** conflict — one speaker, two sentences, ten seconds apart —
which is exactly the class `D-048` Part 1's ladder governs, and `REVIEW_PROTOCOL.md` §6a check (2)
requires a session resolving one to **name the rung that answered**. `C-022` names none.

⚠️ **This is not chargeable to the submission and is expressly not charged as one.** `D-048` was
adopted onto integration at `61042e5`, **2026-08-14 14:04**. `video/v15` filed `C-022` at
`1a3667e`, **13:19** — 45 minutes earlier — and had already synced integration at `08a0cd4`, 13:11,
when `D-048` did not exist. **The session applied a rule that had not been written.** The obligation
is created by the merge, not by any act of the student session.

**The reviewer ran the ladder, so the remediation is a transcription rather than an analysis:**

- **Rung 1 — SILENT.** Neither statement is retracted or corrected by the speaker. *"Not repaint"*
  is offered as an assertion about the same objects, not as a correction of *"they'll creep."*
- **Rung 2 — SILENT.** **Neither statement is a construction.** *"They'll creep up or creep down to
  try to fit price action"* and *"Not repaint. They adjust for price action"* are both
  characterisations of behaviour; neither states how a level is computed or when it is fixed. **This
  is `A-093`'s pattern for the third time in this corpus**, and it is the reason `A-100` exists.
- **Rung 3 — arguably answers for *"Not repaint"***: it is ten seconds later, unhedged, and the
  earlier statement carries *"so to speak."* ⚠️ **But closing on it would close a load-bearing
  record** — `C-022` is one of the two blockers that make the lesson's own object uncodeable — and
  `D-048` rung 4 expressly catches *"any case where… a rung would close a load-bearing record."*
- **RUNG 4 — DO NOT ADJUDICATE.** The `C-xxx` stays `OPEN`, both statements stay on the record, the
  ADR marker stays `DO NOT CODE`.

⭐ **The outcome is identical in substance to the disposition `C-022` already carries**, which is
why this is a `MINOR` and not more: the session reached `D-048`'s answer without `D-048`, by
declining to pick. **Nothing about the record changes except that the rung is now named.**

**Required:** add a `D-048` ladder section to `C-022` recording the four rungs above and the rung-4
return. Do not change `C-022`'s status, its consequence block, or `A-100`.

---

## NOTES

### `N1` — ⭐ `PT-043` INDEPENDENTLY RE-DERIVED, AND IT REPRODUCES · item 203

Reviewer code written from `PT-043` §§3–6 **before `run_pt043.py` or `mmm_lib` was opened** — its
own HistData CSV parser, its own fixed-`UTC−5` and `zoneinfo` `America/New_York` arms, its own
`[D−1 17:00, D 17:00)` session-day rule, its own completeness filter, its own `N1`/`N2`/`N3`
controls and its own Wilson interval:

| Figure | Committed | Reviewer, independent | Δ |
|---|---|---|---|
| `O1`, W-B / Arm A | **0.3640** | **0.3645** | +0.0005 |
| `N1` control median | **0.3757** | **0.3762** | +0.0005 |
| **`O1` − `N1`** | **−0.0117** | **−0.0117** | **exact** |
| `O2` | 0.0939 | 0.0955 | +0.0016 |
| `O3` | 0.2427 | 0.2437 | +0.0010 |
| **median `min(d_hi,d_lo)`** | **21.40 pips** | **21.40 pips** | **exact** |
| median day range | 96.00 | 95.4 | −0.6 |
| `O1`, W-A / Arm A | 0.4180 | 0.4202 | +0.0022 |
| `N3` census `[0,25]` / `[25,50]` / `[50,75]` | 0.5832 / 0.3640 / 0.0509 | 0.583 / 0.365 / 0.051 | ≤0.001 |

`n` differs (513 vs 511) **only** because the reviewer's completeness rule is a bar-count threshold
(≥ 90% of the median day's M1 bars) rather than the submission's stricter all-96-buckets rule; the
two rules disagree on three holiday days and on nothing else in Arm A. **Every headline figure lands
within 0.0022, two land exactly, and the verdict — `O1` NOT SUPPORTED, `O2` CONTRADICTED, control
beats the rule — is unchanged in every cell.** The `2014-06-02` `D-036a` hole was found
independently (115 bars against a 1,438-bar median) without reading the submission's exclusion list.

### `N2` — the twelve corrections: four load-bearing ones confirmed verbatim on a different engine · item 204

`faster-whisper` `large-v3` on audio from the SHA-verified `.swf`:

| # | Committed grid | Adopted reading | Reviewer's independent pass |
|---|---|---|---|
| 1 | *"Steve **Socks**"* | *"Steve **sucks**"* | ✅ *"If you start mumbling under your breath, **Steve sucks**, he's crazy, I hate him… **Steve's going to suck, you're going to hate me.**"* |
| 3 | *"the **80 are** high low"* | *"the **ADR** high low"* | ✅ *"So when the **ADR high-low** couples with the pivot point, the blue tracer"* |
| 11 | *"off of the **higher low**"* | *"off of the **high or low**"* | ✅ *"We know that they always complete the cycle **25 to 50 pips off of the high or low**, depending on the pair"* |
| — | (`C-022`, both halves) | — | ✅ *"They'll **creep up or creep down to try to fit price action**, so to speak… They're a moving grid… **Not repaint**, they adjust for price action."* |

⭐ **Correction 11 is the one that mattered most and it holds.** The uncorrected reading would have
made `[00:31:27]` a claim about *a higher low* — a market structure — instead of about two levels,
and `PT-043` would have measured the wrong object. **A third engine confirms the arbitration.**
The four-part confluence list also confirms verbatim: *"TDI, shark fin, blood in the water… ADR, met
or exceeded. Yesterday's high-low is laying there, blue tracer, a pivot point."* So do
`[00:27:26]`–`[00:27:39]` (the ADR definition and *"limitations of about 200 pips"*, **with no
lookback stated anywhere in the passage** — `A-100` confirmed at source), `[00:38:26]` (*"The weekly
range is 600 to 1,000 pips"* — `A-095` figure 2 verbatim), `[00:48:24]` (*"Stop loss goes three pips
below the entry bar. I've read it a thousand times. It's the stupidest thing I've ever read"* —
`N5`), and `[00:00:33]`–`[00:00:40]` (the June calendar, whose *"the final boot camp will be on the
17th, **which is Father's Day**"* is an independent confirmation of the year: 2012-06-17 was
Father's Day).

⚠️ **One small over-reach inside correction 8.** The correction's stated object is
*manage → mayonnaise*, which confirms; but the adopted reading also silently changes *"**There's**
your mayonnaise, your M3"* to *"**Here's**"*. **Two engines say *There's*** — the committed grid and
this reviewer's independent pass. Nothing turns on it (`A-096`'s pairing of mayonnaise with `M3` is
unaffected), but a correction should change only the word it is arbitrating. **Fold into `M5`'s
remediation pass; not charged separately.**

### `N3` — ⭐ ATTACK POINT 1 IS CLOSED IN THE SUBMISSION'S FAVOUR, FROM V13's AUDIO · item 205

`V15_MASTERY_REPORT.md` §7.1 named this as the place to attack and said the check had not been done.
It has now. V13's `.swf` SHA-256 re-verified; `large-v3` on the extracted audio returns, at the
cited markers, **verbatim**: *"Next session is going to be Sunday the 29th. That's two weeks"* and
*"we'll take a two-week break, and then we'll get started again with **week six through ten**"*; and
at `[00:07:41]`, *"it's 6 p.m. **Saturday, April 21st** at the Bohemian Hotel in Celebration,
Florida."* **The Week-6 date (2012-04-29) and the Orlando date (2012-04-21) both rest on audio now,
not on a committed transcript.** The two forum-post dates were read off the pixels by this reviewer
— `April 28, 2012, 07:57:45 PM` and `April 30, 2012, 03:12:23 AM` — and they do bracket 2012-04-29.
The five-item Week-7 roll-call was read off the pixels and every item is a V13/V14 drill.
**Item 191's calendar stands, on independent evidence, with one caveat at `N4`.**

### `N4` — the V13 citation trims a hedge, and it does not matter · item 206

The full line is *"week six through ten **or six through, I don't know how many we're going to do
yet**."* The interpretation and the mastery report both quote only *"week six through ten."* **The
trimmed clause hedges how many weeks the course will run, not where the numbering resumes** — the
words *"week six"* are unhedged in both readings — so the inference is unaffected. Recorded because
a trimmed quotation is a habit worth not forming, and because `REVIEW_PROTOCOL.md` §6.A asks
specifically whether qualifiers were dropped. **Restore the full clause when `M5` is applied.**

### `N5` — `Q-016`'s transcript negatives independently counted, and the register **understates** its own evidence · item 207

Counted in reviewer code over the 492-marker body: `M15` **0**, `5/13` **0**, `10 to 15` **0**,
`fake breakout` **0**, `peak formation` **0**, `level 1`/`level one` **0**, `level three` **3**,
`trap` **3**. **All confirm.** The fabricated *"Place your stop loss 10 to 15 pips beyond the High
or Low of the Day"* occurs **zero** times.

⭐ **And `Q-016` §3 is weaker than the facts allow.** It says the lesson *"says **only** 'That is why
you use a stop loss. Okay. A tight stop loss' (`[00:42:15]`) with **no number attached**."* The
lesson does attach a number to a stop — at `[00:48:24]`: *"In those textbooks, **stop-loss goes
three pips below the entry bar**. I've read it a thousand times. **This is the stupidest thing I've
ever read.**"* **The only stop-loss number the lesson contains is one the course author explicitly
derides**, which makes a fabricated quoted stop-loss rule worse, not better. **Recommend `Q-016` §3
be strengthened rather than corrected** — this is evidence the entry left on the table.

### `N6` — ⭐ ATTACK POINT 3 RESOLVED IN THE SUBMISSION'S FAVOUR, FROM SOURCE · item 208

`PT-043` §1a invites the reviewer to strike the test if V15 `[00:31:27]` and V10 `[00:13:41]` are
the same claim. Read at source, **they are not**, and both pre-registered differences hold:

| | V10 `[00:13:03]`–`[00:13:44]` | V15 `[00:31:20]`–`[00:31:36]` |
|---|---|---|
| Period | *"If market makers run the ADR **on Friday**… to trap the traders **going into the weekend**"* — **weekly** | *"his entire run **for the day**"… *"trap the traders **for tomorrow**"* — **daily** |
| Conjunction | *"25 to 50 pips off of the high **and** 25 to 50 pips off of the low"* | *"25 to 50 pips off of the high **or** low"* |

**The period difference alone makes it a different measurement**, and `PT-043` neutralises the
conjunction difference by reporting **both** readings (`O1` = *or*, `O2` = *and*) rather than
choosing. **The test is not a re-run of `PT-036` `M2` and should not be struck.**

### `N7` — ⭐ ATTACK POINT 6 ANSWERED BY MEASUREMENT: the Arm-B subset IS biased, and the bias FLATTERS the claim · item 209

`V15_MASTERY_REPORT.md` §7.6 asks the reviewer to check whether Arm B's surviving 444 days are a
biased subset. **They are, and the submission's §5 diagnosis is exactly right — this review
confirms the mechanism independently and then measures the consequence, which §5 could not.**

My Arm-B day partition produces **70 near-empty residual days** (< 100 bars) in `W-B` — the Friday
17:00–18:00 tail that the DST-shifted boundary strands at each week's end — matching the submission's
weekly-pair exclusion pattern precisely. The submission's remaining ~71 exclusions are the Monday
session days that hold **92 of 96 buckets** because the corpus's week opens an hour after Arm B's
day boundary. **The all-96-buckets rule removes them; a 90%-of-median bar rule keeps them.**

**Measured effect of keeping them:** Arm B `O1` moves from the committed **0.3604** (n = 444) to
**0.3431** (n = 513), and `O1` − `N1` widens from **−0.0225** to **−0.0331**. ⭐ **The exclusion is
therefore not neutral: it flatters the claim slightly.** The verdict is `NOT SUPPORTED` either way,
and the submission's *"it does not change the answer"* is **confirmed** — but the direction is now
on the record rather than assumed, which is what §7.6 asked for.

### `N8` — the seed departs from `COMMON_PROTOCOL.md` §5's pre-registered value · item 210

`COMMON_PROTOCOL.md` §5 fixes *"**Random seed: `20260812`**, for every test, every arm.
**Pre-registered to make seed-shopping impossible**"*, and `D-029` fixes 1,000 iterations.
`PT-043` §5a instead says *"seed fixed in the runner and printed"* and specifies 2,000 iterations;
the run used **`20260814`**.

**Iterations are a clean, pre-registered upward override and are better than the floor.** The
**seed** is different in kind: `COMMON_PROTOCOL.md`'s value is pre-registered precisely so that
seed-shopping is impossible *without having to trust ordering*, and `PT-043` deferred it to an
artifact that did not yet exist. **In this instance nothing is wrong** — the runner is committed at
`6b4d4a3` **before** execution at `2b78501`, ordering is proven, and my own re-derivation on a
completely different seed reproduces the control median to 0.0005, which is the strongest possible
evidence that no seed was shopped. **Recorded so the next `PT` names its seed in the `PT` file, not
in the runner.** `PT-043` §1's *"the `PT-NNN` file governs"* makes this legal; it is a hygiene note,
not a defect.

### `N9` — ⭐ the June web class **was** to be recorded, which sharpens item 189 rather than defeating it · item 211

Item 189 rests on `V15_00-05-55_…png`'s *"6pm-10pm with Sat as the Indicator chart setup day."* —
verified verbatim off the pixels by this reviewer. **The same slide's next bullet reads *"These
recordings will be left up all during the Live event"*, and `[00:06:36]` says *"The recording from
this class will replace the recordings that are up right now… they're going to be available to
you guys."***

**The distinction the corpus actually draws is in-person versus web, not recorded versus not.** The
**in-person** events — Orlando, and the June 23–27 New Jersey class — were deliberately not recorded
(`[00:05:07]`, `[00:05:12]`, and the printed
`This Class will NOT be recorded or streamed!!!!!!!`). The **June 2–6 web class**, which is where
the *"Indicator chart setup day"* sits, was to be recorded and posted.

Two consequences, both of which strengthen the practical recommendation:

1. ✅ **Item 189's core reading is confirmed and sharpened:** the indicator-setup content was
   scheduled outside the bootcamp series, so **the in-corpus frame hunt should indeed be closed as
   EXPLAINED.** The June web class is not in `SOURCE_MANIFEST.md` and never was.
2. ⚠️ **But "EXPLAINED" must not be read as "unrecoverable."** Unlike Orlando, this material was
   *intended to exist as a recording*. **`A-084`'s surviving route "material from outside the
   bootcamp series" is therefore a concrete, named artifact — the June 2012 web class, Saturday
   session — not a vague hope.** That is worth recording where the owner weighs item 157's ruling
   against further searching.
3. ⚠️ Consequently `V15_INTERPRETATION.md` Q1 §1's *"**This instructor deliberately did not record
   his live events.** That is a structural fact about what this corpus can ever contain"* is right
   about **live** events and over-broad about **the corpus**, whose own contents are recorded web
   classes. **Folded into `M5`'s remediation rather than charged separately.**

### `N10` — `REVIEW_PROTOCOL.md` §6a checks (1) and (3): not triggered, and the abstentions are documented correctly · item 212

**Check (1), `D-046`.** `grep` over the whole V15 artifact set returns **zero** occurrences of
`EXCLUDED BY DECISION`. No dimension claims the disposition, so the four-condition audit is not
engaged. **The mastery report's §6 uses `✅`/`⚠` and its "where I would mark myself down" paragraph
names three shortfalls plainly** — including that two of the five roll-call drills are simply not
done. That is the honest form of the disposition and needs no decision citation.

**Check (3), `D-049`.** The session declares `D3` — **no forward read into V16+** — in
`V15_SOURCE_NOTES.md` §0, `V15_MASTERY_REPORT.md` §2 and the homework §3, and item 192 offers the
cheap V16/V17 calendar check and expressly declines to perform it pending item 179. **No clause is
engaged because no forward read occurred.** ⭐ **And the process point item 192 makes is correct and
worth carrying:** the Week-6 decider was *behind* the session, in V13, and needed no precedent at
all. *Check backwards before arguing to read forwards.*

### `N11` — the speaker determination is sound and the strand that carries it is confirmed on audio · item 213

**100% course author / 0% guest, HIGH confidence, upheld.** `COURSE_PROGRESS.md` V14 GATE (d)
required this be re-tested rather than inherited because V15 is a new week and a new date after a
multi-week gap — the V03→V04 failure condition — and it was, on six non-acoustic strands fixed
before the answer was known.

Strand 1 is decisive and this reviewer confirmed it verbatim on an independent engine: *"If you
start mumbling under your breath, **Steve sucks**, he's crazy, I hate him… **Steve's going to suck,
you're going to hate me.** I'm kidding, but halfway."* **The pronoun switch from *Steve* to *me*
inside one breath is the identification.** I independently read the transcript for a second voice
and found none: the twenty named third parties are all being answered, congratulated or shown, and
`[00:46:36]`'s *"Someone said to take a sip of coke"* is the speaker reading chat aloud, not a
second speaker. **`D-025`/`D-033` audit: no guest statement was admitted as a rule, because there is
no guest.**

### `N12` — `D-047` numbering collision, resolved at this merge and disclosed · item 214

`video/v15` synced integration at `08a0cd4` (13:11), when **186 was the highest item**, and
allocated **187–194** — correctly, against that state. `decisions/adopt-045-050` then landed on
integration at `61042e5` (14:04) claiming **187–188**. Under `D-047` Consequence A the later arrival
renumbers, so **the V15 student items are renumbered 189–196 in this review's merge commit**, with
cross-references updated in `AUTOMATION_AMBIGUITIES.md`, `V15_INTERPRETATION.md`,
`V15_SOURCE_NOTES.md`, `CONTRADICTIONS.md`, `V15_MASTERY_REPORT.md`, `COURSE_PROGRESS.md` and
`LOG.md`. **No item content changed.** ⚠️ **One reference was missed by the merge's own sweep and is
carried into `M2`'s remediation:** `04_SCREENSHOTS/V15/INDEX.md` §0.3 still reads *"item **188**"*
and must read **190**. **This is not charged against the submission** — the collision was created by
a branch that landed after V15 had allocated, and item 188's own numbering-disclosure block
anticipated exactly this.

### `N13` — CALIBRATION, CHARGED AS NOTHING · item 215

Recorded because a review listing only defects gives the next session no signal (item 161):

1. ⭐ **The single best decision in the submission is a negative one.** `PT-043` §1b declines to
   backtest the lesson's own headline rule, **before the run**, because `C-022` + `A-100` make an
   ADR level's past visibility undecidable — and then tests a different, cleanly-defined claim
   instead. A session that wanted a result would have pre-registered an ADR definition and called
   it an assumption. **This one wrote down why it could not, in advance.**
2. ⭐ **The self-correction at `S1` is the second-pass rule catching exactly what it exists to
   catch.** *"ADM"* read as `ADR` would have manufactured a fifth ADR mention inside the ADR
   lesson. It was caught, published as a correction with the self-correction called out, and not
   fixed silently.
3. **The 5-of-5 prediction score is discounted by the session that earned it**, on the correct
   ground that P1–P3 were largely one prediction inherited from `BT_V10_0001`.
4. **The Arm-B exclusion asymmetry was disclosed before a reviewer found it**, with the direction
   stated — and `N7`'s measurement **strengthens** the disclosure rather than contradicting it.
5. **No homework was invented** on a lesson that sets none, in a repository that has now quarantined
   sixteen fabrication entries. The declared substitution is the right call and is argued, not
   asserted.
6. **`A-096` is the record that would not have existed in a careless round.** Read from audio alone,
   *"Here's your mayonnaise, your M3"* and *"This is an M1, M3 day"* would have been read as
   M-formations. The frames settle it as pivot mid-levels — **and the record still refuses to
   close**, because the trigger is Tier 2 only and the pivot formula is stated nowhere.
7. ⭐ **The session named six attack points and it was right about all six being the right places to
   look.** Three of them (1, 3, 6) are resolved **in its favour** by this review; the other three
   are correctly left open. **That is calibration, and it is rarer than being right.**

---

## REVIEW DIMENSIONS — `REVIEW_PROTOCOL.md` §6

| Dim | Grade | Basis |
|---|---|---|
| **A** Source fidelity | **MINOR ISSUE** | `M5` (Orlando stated more categorically than the source supports; contrary datum unengaged) and `N4` (trimmed hedge). Every other quotation checked was verbatim, including four confirmed on a second engine |
| **B** Completeness | **PASS** | The lesson's operational meaning is captured: the ADR as a watchlist filter, the four-part confluence, the 9:30 timing, the floating-vs-fixed grid, and the reliability disclaimer the lesson attaches to its own rule |
| **C** Provenance | **PASS** | Every record cites markers and frames; `[AUDIO]`/`[PRINTED]` tags are `grep`-checkable; `M1` is a mislabel inside a record, not an orphan rule |
| **D** Explicit vs inferred | **PASS** | Tier 2 is quoted as Tier 2 throughout and never promoted — `A-096` and `A-100` both refuse to close on it, and the homework §1 catches the author of this set doing it once, in themselves, and says so |
| **E** Chart recognition | **PASS** | 37 frames each opened and read; four read independently by this reviewer and all four matched. `A-096`'s decoding is correct and correctly bounded |
| **F** Counterexamples | **PASS** | `C-022`'s Reading C is constructed and **not adopted**; the `A-084` "explained" claim carries its own defeater; item 189 flags its own thinness |
| **G** Manual backtest | **PASS** — all 20 checks | See the dedicated section below |
| **H** Hindsight / lookahead | **PASS** | The one place lookahead could have entered — a backtest of the ADR confluence rule — was identified and declined **in advance**, in writing |
| **I** Outcome vs rule | **PASS** | `A-098` logs the *"five for five"* student report as anecdote and explicitly refuses to let it rebut `PT-042` |
| **J** Sample quality | **PASS** | n = 511 / 444 / 256 / 222, all ≫ 30; Wilson intervals on every rate |
| **K** Homework | **PASS** | V15 sets none; the substitution is declared, argued and reasonable. §2 Q1 answers the roll-call **against this project** honestly — two of five done, one blocked, two not done |
| **L** Teach-back | **PASS** | Homework §1 restates the lesson from memory and leaves **two** comprehension errors visible rather than correcting them away |
| **M** Blind recognition | **NOT APPLICABLE** | No classification set was produced; none was called for by this lesson |
| **N** Ambiguity | **PASS** | `A-095`'s three figures, `A-097`'s two undefined trade names and `A-100`'s missing lookback are all held open. **No subjective term became a constant** |
| **O** Contradictions | **MINOR ISSUE** | `C-022` is correctly raised, correctly left `OPEN` and correctly used to block; `M6` is the missing rung name only |
| **P** Machine-rule firewall | **PASS** | `12_MASTER_SPEC/` and `13_MACHINE_SPEC/` re-checked this session: **`.gitkeep` and a README only.** No V15 number reached either |
| **Q** Claimed accuracy | **PASS** | *"Is that always true? **No**"* is preserved beside the rule; `[00:29:14]` is quoted rather than smoothed |

---

## `PT-043` — THE TWENTY BACKTEST CHECKS, `REVIEW_PROTOCOL.md` §6.G

| # | Check | Verdict |
|---|---|---|
| 1 | GBP/USD primary | ✅ `D-007`, and it is the pair the lesson's own chart shows |
| 2 | Period reasonable | ✅ `W-B`/`W-A`, `COMMON_PROTOCOL.md` §3, adjacency to 2012 argued |
| 3–4 | Sequential / future hidden | ✅ **N/A by construction** — a whole-day H/L/C measurement reads no forward bar |
| 5 | Rules known before result | ✅ **PROVEN by object existence at `1a3667e`** |
| 6–9 | No skipping, losers retained, borderline retained, invalid separated | ✅ No day excluded for size, news or shape; the five largest-range days named and kept |
| 10–11 | Consistent recording / R | ✅ Deterministic script, committed output, results JSON |
| 12 | Screenshots before/after | ✅ **N/A** — CSV corpus, `COMMON_PROTOCOL.md` §2's restated rule |
| 13 | Exact lesson rule identified | ✅ Verbatim, with the ASR arbitration disclosed |
| 14 | Testing the lesson, not a later interpretation | ✅ And `N6` confirms it is not `PT-036` `M2` re-run |
| **15** | **Baseline present** | ✅ `N1`, 2,000 iterations, distribution reported. **Reproduced independently** |
| **16** | **Baseline pre-registered** | ✅ `PT-043` §5a, before the runner existed |
| **17** | **Period pre-registered** | ✅ §4, unchanged; post-run diff is the banner only |
| **18** | **Holdout intact** | ✅ 2016H2 never opened; no `D-044` year read. **Independently confirmed** — my re-derivation loaded 2013–2015 only |
| **19** | **Sample sufficiency and interval** | ✅ n ≥ 222 in every cell; Wilson 95% on every rate; bootstrap CI on every median |
| **20** | **Negative results retained** | ✅ **This test *is* a negative result, reported as the headline.** Both arms, both windows, `O3`, all four `N2` offsets and the full `N3` census are printed |

**Where the course supplies its own control, was it used?** ✅ **Yes, and better than required.**
`N1` holds each day's high and low fixed and varies only where in the day the observation is taken —
which is the sharpest available separation of *placement* from *range*, and it is what produced the
finding. **The rate is not the result; the control is.**

---

## WHAT V15 CONTRIBUTES, AND WHAT IT DOES NOT

**Contributes.** A verified transcript with twelve arbitrated corrections and its own self-correction
published; 37 frames each proving its own timestamp; the first `SWF_CAPTURE_RECIPE.md` §8a
compliance run; six ambiguity records and one contradiction; `Q-016`, the fifth consecutive
`VISUAL_INDEX.md` fabrication and the first to carry a fabricated **stop-loss rule in quotation
marks**; a pre-registered, independently reproduced backtest returning an honest negative on the
course's own claim; and — the finding with the longest reach — **the corpus's Week-6 gap fixed to a
single named date, from a line that was behind us in V13 the whole time.**

**Does not.** It does not advance `A-084`, `A-085`, `A-086` or item 157 by one number, and it does
not claim to. **The `A-084` blocker is intact and this review verifies the negative was measured
rather than asserted:** 623 frames with no properties dialog, no Navigator and no inputs tab; both
`TDI_MMM` legends showing a short name and three current values with no parameter tuple; the spoken
route logged as a **sixth restatement** of `68`/`32` and explicitly **not** treated as new evidence,
per V14 R1's instruction. **`A-100` and `C-022` between them make the lesson's own central object
undrawable, and this review confirms both from source** — the transcript states no lookback, no range
definition, no anchor and no day boundary anywhere in `[00:26:57]`–`[00:51:56]`, and the two
incompatible statements about the levels' behaviour are ten seconds apart in one passage, confirmed
on a second engine. **A lesson whose subject cannot be drawn is the honest finding here, and the
submission reaches it without flinching.**

---

## REQUIRED ACTIONS

1. **`M1`** — correct `A-095`'s exception paragraph and `Current Status` block: Figure **1** is the
   one `PT-043` tested (`NOT SUPPORTED`); Figure **2** was already contradicted by `PT-036` `M1` and
   is **not** re-tested. Leave `PT-043` and `BT_V15_0001.md` untouched.
2. **`M2`** — withdraw `04_SCREENSHOTS/V15/INDEX.md` §0.3's mechanism paragraph and its formula, and
   withdraw or restate item 190's proposed `SWF_CAPTURE_RECIPE.md` edit. `const t0=Date.now()` is
   already set before `p.mouse.click(...)`. **Retain §0's measurement table and §8a unchanged.**
   Fix the stale *"item 188"* → *"item 190"* in the same section.
3. **`M3`** — update `COURSE_PROGRESS.md`'s `PROGRESS TABLE` V15 row from `NOT STARTED` to the
   completed-student-pass state, matching V14's row pattern.
4. **`M4`** — restate `Q-016` §3 and §4 on §1's line-counting convention (12 and 6 differing lines),
   and correct *"three `VIDEO_15`→`VIDEO_16` visual references"* to **two**.
5. **`M5`** — restate the Orlando conclusion as *"no recording was **obtained**"* in
   `V15_INTERPRETATION.md` Q1 §1, `V15_MASTERY_REPORT.md` §3.1 and item 191; cite and engage V13
   `[00:02:26]` (*"we will try to either stream it and record it or just record it"*); restore the
   full V13 *"week six through ten or six through…"* clause (`N4`); and narrow *"a structural fact
   about what this corpus can ever contain"* to **in-person events**, per `N9`.
6. **`M6`** — add a `D-048` ladder section to `C-022` recording rungs 1–4 and the **rung-4** return.
   Do not change `C-022`'s status or consequence block.

**Do not reprocess anything else.** The transcript, the frames, the source notes, the interpretation
beyond Q1 §1, the homework, `PT-043`, `BT_V15_0001.md`, `Q-016`'s substance, `A-096`–`A-100` and the
speaker determination all stand.

---

## EXECUTIVE BLOCK

```text
LESSON: V15
DECISION: REVISE
CONFIDENCE: HIGH

CRITICAL ISSUES:
- NONE

MAJOR ISSUES:
- NONE
  (M2 was weighed for MAJOR and charged MINOR; the reasoning is on the record
   above so the owner can overrule it.)

MINOR ISSUES: 6   (items 197-202)
NOTES:       13   (items 203-215)

REQUIRED ACTIONS:
1. A-095 -- correct which figure PT-043 tested.
2. INDEX.md s0.3 -- withdraw the mechanism claim; withdraw/restate item 190's
   proposed recipe edit; fix the stale item number.
3. COURSE_PROGRESS.md -- update the V15 progress-table row.
4. Q-016 -- one diff-counting convention; "three" -> "two".
5. Orlando -- "no recording was OBTAINED"; cite and engage V13 [00:02:26];
   restore the trimmed V13 clause; narrow the "structural fact" sentence.
6. C-022 -- name the D-048 rung (rung 4, DO NOT ADJUDICATE).

ADVANCEMENT:
AUTHORIZED -- V16 GATE OPEN under D-024 (0 CRITICAL, 0 MAJOR).
  The six MINORs are owed before V15 can reach COMPLETE (D-004).
  The owner's comprehension/gap audit (item 185) is NOT discharged by this
  review and is not addressed by D-024.
```
