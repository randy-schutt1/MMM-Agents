# REVIEW INDEX

Master record of every independent review decision, and the project's running
error statistics.

Maintained by the Reviewer Agent. Append-only for decisions — a superseded decision
stays visible with its round number.

---

## STATUS

```text
LESSONS REVIEWED: 11 (superseded text, retained: "LESSONS REVIEWED: 10")
V11:              R1 2026-08-13 — REVISE, HIGH confidence,
                  0 CRITICAL / 0 MAJOR / 5 MINOR / 7 NOTE.
                  GATE TO V12 IS OPEN under D-024 and this round does
                  NOT qualify that — the owner's V12 work is not held
                  by anything in it. V11 is IN REMEDIATION, NOT
                  COMPLETE: items 109-113 are owed first.
                  ⭐ This is a FULLY INDEPENDENT round — D-003
                  SATISFIED, unlike V09 R2 and V10 R1's fix round.
                  The reviewer authored no V11 artifact, cut its
                  branch from INTEGRATION (not from video/v11) so the
                  source was read before the student's conclusions,
                  and merged the submission in only AFTER the verdict
                  was committed.
                  RE-DERIVED, NOT READ: PT-039 reproduced END TO END
                  by reviewer-written code parsing the RAW HistData
                  CSVs, sharing no line with run_pt039.py or mmm_lib
                  — all four cells EXACT (O1 to 4dp, every n(T), every
                  Wilson bound, all six N3 strata, O3/O4/O5, 894/777
                  session days, 11/245 exclusions) and all four
                  verdicts reproduce (M1a PARTIAL, M1b CONFIRMED,
                  M1c CONTRADICTED, M1d PARTIAL). Homework H6
                  recomputed: 36/36 cells to 2dp. Q-012's RULES.md
                  diff re-run: 12 lines, 6 substitutions, ZERO content
                  lines. 21 SCREENSHOT_001 files MD5'd: 21 distinct.
                  Lookahead RE-DERIVED and CLEAN.
                  THE ONE FINDING A READING-ONLY REVIEW WOULD HAVE
                  MISSED is item 109, and it came from OPENING AN
                  IMAGE: the categorical "no frame shows an indicator
                  legend" is false — frame 14 (27:35) carries RSI(21),
                  ATR(14), CCI(14), MACD(12,26,9), Sto(5,3,3), Mom,
                  AO and GBPUSD,H1. A-080's DISPOSITION IS CORRECT AND
                  UNCHANGED (the chart is the lesson's DISOWNED
                  anti-example, on H1) but RSI(21) is a NEARER trap
                  than the 13 the record names.
                  Host-vs-guest: CORRECT, HIGH, over-determined. Four
                  strands confirmed, handover scan re-run with a
                  17-pattern superset (ZERO), and FIVE new strands
                  added — including [00:23:06]'s CHECKABLE back-
                  reference to V01's own week-1 blue-box instruction,
                  the only cross-file strand in the determination.
                  C-018's closure is FAITHFUL to D-041 in BOTH
                  directions — no "Tier 0", no Tier 1 override, §3.4
                  stays live, superseded text retained. Item 110 is a
                  correction that RUNS IN THE CLAIM'S FAVOUR.
                  V10's PT-037/PT-038 numbering VERIFIED UNTOUCHED at
                  every site; two V11-side renumbering gaps remain
                  (items 111, 112).
                  Items 101 and 108 VERIFIED and NOT understated —
                  Arm B's DST defect reproduces exactly (Mon 118 /
                  Sat 117, 64.8% of Mondays lost).
                  Item 105's reviewer judgement is ANSWERED: A-039's
                  narrowing is NOT generous, it is accurate — item 105
                  can be closed.
                  NO QUESTION IS PUT BACK TO THE OWNER on the D-041
                  period mapping: the reviewer checked the corpus
                  independently and DECLINES the escalation D-041
                  consequence 7 invited (item 114), a result D-042 §1
                  independently corroborated mid-review.
PASSED:           10 (V10 — ⚠ COMPLETE 2026-08-13, SELF-VERIFIED AT
                      OWNER DIRECTION, NOT INDEPENDENTLY VERIFIED.
                      Superseded text, retained: "PASSED: 9".
                      R1's four MINORs -- items 91 (student half), 92,
                      93 and 94 -- are all APPLIED and all CLOSED —
                      SELF-VERIFIED AT OWNER DIRECTION. ⚠⚠ READ THE
                      V10 NOTICE UNDER THE DECISION TABLE BEFORE
                      RELYING ON THIS ROW. The owner explicitly
                      authorised ONE session to both fix AND verify
                      this round, on the ground that all four items are
                      small documentation edits. That authorisation is
                      real and recorded, but it does not manufacture
                      independence and this round does NOT satisfy
                      D-003. There was NO R2 and no independent PASS.
                      SECOND use of the pattern, after V09 R2 on the
                      same date, and recorded in the same words so the
                      two are countable.
                      WHAT MOVED: nothing that bears on a measurement,
                      classification, disposition or rule. M2 corrects
                      the spoken census from "four of six" to FIVE OF
                      SEVEN -- [01:00:20] "75 pips off of the blue
                      tracer" was missing -- which WIDENS the spoken
                      majority and STRENGTHENS C-017. M3 rescopes §15's
                      "no hour is ever stated" to "no session-boundary
                      clock time is stated", listing the four
                      incidental times ([00:02:24], [00:05:09],
                      [00:42:52], [01:03:57]) that falsified the
                      stronger form; A-076's parallel sentence was
                      checked, found CORRECT as written, and left as
                      the model. M4 adds an ASR caution to C-016 --
                      both figures ASR-rendered, neither printed, no
                      curated frame carries a holding period -- as a
                      FURTHER reason for UNRESOLVED, superseding
                      nothing. M1's student half: the renumbering
                      81-85 -> 86-90 is VERIFIED COMPLETE by repo-wide
                      sweep, and the review's claim that two V10
                      artifacts "cite open item 82" is FALSE -- neither
                      ever carried an item number, so nothing was
                      orphaned; both have GAINED a pointer to item 87
                      instead, and the error is corrected in place
                      rather than absorbed.
                      Every marker was re-derived from
                      02_TRANSCRIPTS/V10/V10_TRANSCRIPT.md at source,
                      not copied from the review. M2's sweep found
                      THREE sites beyond the four the review named --
                      04_SCREENSHOTS/V10/INDEX.md, the V10 comprehension
                      answers, and the transcript's own TRANSCRIPTION
                      NOTE 1, the last being the note M4 relies on.
                      The comprehension answer was NOT rewritten: it is
                      a preserved first attempt and carries an appended
                      correction instead. The transcript's VERBATIM BODY
                      IS UNTOUCHED. Superseded text retained at every
                      site per REMEDIATION_PROTOCOL.md §2. Validator
                      103/0/0. Applied and self-verified on branch
                      fix/v10-r1-minors, cut from the integration branch
                      at 9c00a60 after git fetch --all confirmed zero
                      divergence (D-038), and merged back by this
                      session because its own verdict is what closes
                      the round.
                      STILL OPEN and NOT covered by this verdict: items
                      86, 88, 89, 91's POLICY half, 95 and 96. None was
                      owed before COMPLETE.
                      GATE TO V11 IS CONFIRMED OPEN under D-024 -- it
                      was already open on R1's 0 CRITICAL / 0 MAJOR and
                      never depended on these four minors.
                      V09 — COMPLETE 2026-08-13, ⚠ SELF-VERIFIED AT
                      OWNER DIRECTION, NOT through the normal
                      independent process. See the V09 block under
                      IN REMEDIATION below, which carries the full
                      disclosure and must be read before this row is
                      relied on. Items 81-83 are CLOSED — SELF-VERIFIED
                      AT OWNER DIRECTION, a status that exists solely so
                      it cannot be mistaken for CLOSED — VERIFIED;
                      V01, V02, V03, V04 — V04 PASS at R2, COMPLETE;
                      V05 — PASS at R3 2026-08-12, COMPLETE;
                      V06 — PASS at R2 2026-08-13, COMPLETE;
                      V07 — PASS at R3 2026-08-13, COMPLETE. Items 70
                      and 63 are ✅ CLOSED -- VERIFIED at R3, and with
                      them items 61-63 and 70 are all discharged. All
                      three item-70 instances were re-checked against
                      02_TRANSCRIPTS/V07/V07_TRANSCRIPT.md by the R3
                      reviewer BEFORE any remediated artifact text was
                      read ([00:27:24] "male"; [00:25:26] "Beth"), and
                      items 61/62 were re-derived a second time (56;
                      "the peak" 5; body 7,436 words). §H's categorical
                      claim is replaced by a HISTORICAL COUNT backed by
                      committed code -- the structurally correct fix,
                      not a third attempt at the same sentence.
                      R2's N1 is DISCHARGED: R3 RE-RAN
                      05_HOMEWORK/V07/scripts/verify_quotes.py rather
                      than writing a fourth sweep, confirmed 3 flags on
                      the pre-correction tree and 0 after, and then
                      ATTACKED it by mutation testing. Four precision
                      bounds were found (allowlist prefix-widening --
                      whose docstring claims the opposite; MIN_WORDS=3;
                      emphasised quotes only; in_blockquote tested
                      before the cited-FLAG branch) and ALL FOUR were
                      then searched BY HAND: nothing lives in them, so
                      §H's surviving "at every site" claim is TRUE and
                      is established independently of the tool. Recorded
                      as NOTE N1, NOT charged -- V07 is not held for a
                      tool's documented, harmless precision limit.
                      THE BRACKET-TOKEN ITEM IS RULED, NOT DEFERRED:
                      "Do all the DM[R] speaker[s]" against [00:29:49]'s
                      "DMS speaker" is NOT a defect -- the brackets are
                      a visible signal (which is exactly what instances
                      (a)-(c) lacked), intra-word bracketing is an
                      established convention across V01/V07/V08, the
                      literal DMS is recorded in the transcript's own
                      ASR-garble inventory, and DM is not a corpus
                      object so no reader can be misled. No correction
                      required and none should be made. THE POSSIBLY-
                      OVERWRITTEN-FILE ALARM IS INVESTIGATED AND
                      DISMISSED: no work was lost. verify_quotes.py
                      exists in exactly one commit ever; not one of the
                      31 unreachable blobs is a Python file; no stash,
                      no backups, no untracked leftovers in the main
                      tree, none in any sibling worktree; and R2 -- the
                      only other session in this working directory --
                      lists three files and no script, describing its
                      sweep in prose BECAUSE it was uncommitted. Most
                      probably the session observed its OWN in-run
                      draft. Stated honestly: an untracked file leaves
                      no git trace, so this is "no evidence of loss plus
                      positive evidence of sole authorship", not proof.
                      D-038 branch isolation is NOT implicated. Carried
                      as N3, with N4 the process gap it exposed -- the
                      concern was reported in session output but never
                      recorded in LOG.md, which is why a forensic
                      reconstruction was needed at all. Dimension B
                      carried from R1/R2 UNCHANGED: NOT SATISFIED,
                      blocked by D-030, structural, not attributable to
                      the student, NO severity charge. Open item 36 is
                      owed for the SIXTH lesson-round running -- not a
                      gate, and it did not hold V07. REVIEWED ON BRANCH
                      review/v07-r3, cut FROM the UNMERGED
                      fix/v07-r2-item70 at cc74051 (D-038; the
                      V08_REVIEW_R1.md §3 precedent for reviewing
                      unmerged work), fetch confirming a clean
                      fast-forward -- 1 ahead, 0 behind. REVIEW_INDEX.md
                      and LOG.md written there as evidence ledgers per
                      D-038a, and the branch merged back by the reviewer
                      as the deliberate D-038 merge-back step, the
                      verdict being clean.
                      V08 — PASS at R2 2026-08-13, COMPLETE. Items 64,
                      65 and 66 are all ✅ CLOSED -- VERIFIED at R2, and
                      with them V08's whole R1 finding set is
                      discharged. NOTHING WAS TAKEN ON THE REMEDIATION'S
                      WORD: the V07 [00:28:02]-[00:28:31] citation was
                      read out of 02_TRANSCRIPTS/V07/V07_TRANSCRIPT.md
                      at source (verbatim, ellipsis honest, and the
                      [00:28:31] garble "in your flashcard" PRESERVED
                      rather than smoothed -- the exact defect class
                      V07's item 63 was charged for); entry_for() and
                      precompute_close_entries() were read and both
                      documented descriptions are EXACT; PT-034's
                      pre-registration is BYTE-UNCHANGED (one commit
                      ever, empty diff); and the end-card's burned-in
                      timecode was re-read FROM THE PIXELS by cropping
                      and 20x-magnifying the player chrome -- it reads
                      43:04. An independent repo sweep for the old
                      string found NO FIFTH reference; every survivor is
                      a retention block, the R1 file, LOG history, or a
                      real [00:43:10] marker in V01/V06. The disclosed
                      0.25s ceil() residual was re-derived across all 26
                      V08 frames: row 26 is the ONLY frame over raw
                      runtime, at exactly ceil(2583.745)=2584, and
                      nothing flags under "> ceil(runtime)".
                      THE PRESENTER-IDENTITY QUESTION IS RULED, NOT
                      DEFERRED AGAIN: V07's and V08's presenters are
                      DIFFERENT MEN, HIGH confidence, on TEXTUAL
                      evidence only. V08 names Ray x3 in the third
                      person -- at [00:00:49], 49 seconds in, as the man
                      who had been taking the questions -- and Ray
                      occurs ZERO times in V07 and ZERO in V06; V07 is
                      the Q&A part (16 named questioners) and V08 reads
                      none. Independently, V07's presenter defers to Jim
                      x3 and disclaims the high-of-day skill at
                      [00:07:43], which V08's second half teaches under
                      a deck titled "Jim's Journey". Probable names V07
                      = Ray, V08 = Jim at MEDIUM -- provenance, not
                      evidence, per D-033 prov. 2. NO cross-file F0
                      comparison was used: COURSE_PROGRESS.md V06 GATE
                      item (a) prohibits it, and the ruling would be
                      unchanged if the numbers did not exist. One
                      residual stated rather than smoothed: V08
                      [00:17:29] "Jim's right about that one" is
                      unexplained, which is why the NAMES are MEDIUM --
                      it does not touch the different-men finding, which
                      does not require the identification. R1's "a
                      different guest presenter" is SUPPORTED, and the
                      remediation's refusal to write it unverified was
                      STILL the right act -- carried as NOTE N1 and item
                      71, a documentation follow-up NOT owed as a
                      defect. C-009 stays PROVISIONAL; D-025's
                      guest/instructor carve-out does NOT apply, both
                      speakers being GUEST, so it remains a method-level
                      contradiction.
                      Dimension B carried from R1 UNCHANGED: NOT
                      SATISFIED, blocked by D-030, structural, not
                      attributable to the student, NO severity charge.
                      Open item 36 owed for the FIFTH lesson-round -- not
                      a gate, and it did not hold V08. REVIEWED ON BRANCH
                      review/v08-r2, cut from the integration branch at
                      a6ee013 (fix/v08-r1-minors was ALREADY MERGED when
                      the round opened), in a DEDICATED WORKTREE -- see
                      new item 72: a concurrent session moved the shared
                      main working directory onto review/v09 (bb4097b,
                      descended from f3f9006, which predates BOTH the V07
                      R2/R3 merge AND the entire V08 remediation) partway
                      through this review. Detected, not missed; every
                      read taken after the switch was re-run in the
                      clean worktree before use, and two stale
                      REVIEW_INDEX reads were discarded and redone. NO
                      conclusion rests on a read from the wrong tree.
                      Charged to PROCESS, not to V08.)
IN REMEDIATION:   0  (Superseded text, retained per
                      REMEDIATION_PROTOCOL.md §2 -- this line and its
                      V10 block previously read:

                      "IN REMEDIATION:   1  (V10 — R1 REVISE 2026-08-13,
                      0 CRITICAL / 0 MAJOR / 4 MINOR / 7 NOTE, HIGH
                      confidence. Items 91-94 are OWED and NOT yet
                      applied. All four are documentation or register
                      hygiene and none moves a measurement,
                      classification, disposition or rule. V10 reaches
                      COMPLETE only at R2, and D-003 reserves that
                      verification to an independent session."

                      ⚠ THE SUPERSEDED SENTENCE IS THE POINT, NOT A
                      FORMALITY. It said V10 reaches COMPLETE only at
                      R2, by an independent session. THERE WAS NO R2.
                      The owner authorised one session to fix AND
                      verify instead, and V10's COMPLETE is therefore
                      ⚠ SELF-VERIFIED AT OWNER DIRECTION -- recorded in
                      the PASSED block above and in the notice under
                      the DECISION TABLE, which must be read before
                      that status is relied on. D-003 is NOT satisfied.

                      Superseded text, retained: "IN REMEDIATION: 0"
                      (the value before V10 R1 opened)

                      V09 — ⚠ COMPLETE 2026-08-13, SELF-VERIFIED AT
                      OWNER DIRECTION, NOT INDEPENDENTLY VERIFIED.
                      Items 81, 82 and 83 are all APPLIED and are
                      CLOSED — SELF-VERIFIED AT OWNER DIRECTION.
                      ⚠⚠ READ THIS BEFORE RELYING ON THAT STATUS. The
                      owner explicitly authorised ONE session to both
                      fix AND verify this round, on the grounds that
                      the three items are small. That authorisation is
                      real and it is recorded — but it does not
                      manufacture independence, and this round does NOT
                      satisfy D-003. The distinct status string exists
                      so no later reader mistakes it for an arm's-length
                      verdict. PRECEDENT AND THE DIFFERENCE FROM IT:
                      V09's own R1 remediation used the same
                      owner-authorised pattern for the FIX — but it
                      CLOSED NOTHING, because R2 was still coming. THIS
                      round closes its own items, which is the stronger
                      deviation of the two.
                      WHAT THE SELF-VERIFICATION ACTUALLY DID, so a
                      later session can judge its weight rather than
                      take its word: every cited marker was re-derived
                      from V09_TRANSCRIPT.md with a parser written for
                      the pass, not the fix's; item 82 was re-derived
                      FROM THE IMAGES (all five PNGs opened — 28:45,
                      31:50 and 41:25 are charts carrying "Reset" and
                      DayHi/DayLo lines; 26:40 is the spreadsheet and
                      34:35 the MS Paint email, confirming the stale
                      ordinals pointed at neither); item 83's premise
                      was re-derived from MMM-NOTES at source (p.38 =
                      the 5, 13, 50 and 200 bar EMAs, "800" ZERO times,
                      p.66 "Hold the Mayo - 200 Bounce"); and the
                      generalised verify_quotes.py was MUTATION-TESTED
                      three ways — item 81's defect reintroduced, the
                      "grape" instance reintroduced, and words appended
                      to an allowlisted fragment — all three FLAG.
                      IT FOUND SIX MORE DEFECTS AND TWO OF ITS OWN
                      ERRORS, which is the only real evidence that a
                      self-verification pass did any work. The six:
                      A-066, A-071, A-072 (x2), A-073 and A-075 in the
                      SHARED ambiguity register — including a SEVENTH
                      copy of "experience shows me", the very phrase
                      item 81 was raised about, in a file the review's
                      named artifact set does not cover. The two own
                      errors: a citation to [00:24:55], WHICH DOES NOT
                      EXIST, and a superseded block that wrongly said
                      "for the week" came from the slide when the audio
                      says it at [00:24:59]. Both corrected in place and
                      both reported against itself.
                      TOTAL: NINETEEN genuine quotation defects found
                      and fixed this round, against the ONE the review
                      named. verify_quotes.py is generalised (per-lesson
                      artifact sets and allowlists) AND extended to scan
                      10_AMBIGUITIES/ and 11_CONTRADICTIONS/ for every
                      lesson, restricted to rows whose first cell names
                      that lesson. V09 -> 315 fragments, 0 FLAGGED.
                      V07 -> 353 fragments, 0 FLAGGED, so no earlier
                      lesson carries the same debt. Two of V07 R3 §4's
                      three recommended precision fixes ADOPTED (full-
                      fragment allowlist anchoring, and the false
                      docstring claim about it); the third REFUSED with
                      reasons, because ordering in_blockquote after the
                      cited-FLAG test would FLAG every correctly
                      retained superseded quotation — R3's actual
                      concern, masking, is addressed instead by having
                      every RETAINED fragment report its near-miss run.
                      ONE DEFECT FOUND AND DELIBERATELY NOT FIXED:
                      PT-035 renders [00:06:08]'s "How are I believe"
                      as "However I believe". Same E01 class. NOT fixed
                      and MUST NOT BE — COMMON_PROTOCOL.md §9 rule 7,
                      and R2 verified PT-035 byte-identical to its
                      pre-registration blob. Disclosed in
                      V09_MASTERY_REPORT.md Revision R2 and LOG.md so a
                      later round rules on it deliberately. PT-035,
                      run_pt035.py and pt035_output.txt are UNTOUCHED.
                      Nothing moves: no status, disposition, DO NOT CODE
                      verdict, grade, marker or conclusion changes
                      anywhere. Superseded text retained at every site
                      per REMEDIATION_PROTOCOL.md §2. Validator 103/0/0.
                      Applied and self-verified on branch
                      fix/v09-r2-minors, cut from review/v09-r2 at
                      dc427dc after git fetch --all confirmed zero
                      divergence (D-038), and merged back by this
                      session because its own verdict is what closes
                      the round.
                      WHAT A LATER REVIEWER SHOULD DO IF IT WANTS THE
                      INDEPENDENCE THIS ROUND LACKS: re-derive item 81's
                      line-410 quotation, item 82's three frame
                      identities and item 83's C-010 arithmetic from
                      02_TRANSCRIPTS/V09/, 04_SCREENSHOTS/V09/ and
                      MMM-NOTES directly, and re-run
                      verify_quotes.py V09. None of it takes long.
                      Gate to V10 REMAINS OPEN under D-024.)

                      GATE TO V11: ⚠ CONFIRMED OPEN under D-024 as of
                      2026-08-13. V10 R1 returned 0 CRITICAL and 0
                      MAJOR, which is what D-024 gates on, so the gate
                      opened at R1 and never depended on the four
                      minors -- their closure removes the "V10 is NOT
                      COMPLETE" qualifier, not the authorization. READ
                      WITH THE QUALIFICATION IT CARRIES: V10's COMPLETE
                      is ⚠ SELF-VERIFIED AT OWNER DIRECTION, not an
                      independent verdict, and a V11 session inherits
                      that qualification along with the gate.
                      Still owed and NOT gating: items 86, 88, 89,
                      91's policy half, 95, 96, and item 36 -- the
                      D-030 dimension-B disposition, now owed for the
                      SIXTH consecutive lesson-round.)

                     (Superseded text, retained per REMEDIATION_PROTOCOL
                      §2 — this block previously read, at R2:)
                      "IN REMEDIATION:   1  (V09 — R2 REVISE 2026-08-13, 0 CRITICAL / 0 MAJOR /
                      3 MINOR (new open items 81-83). R1's items 73-78
                      are ALL CLOSED — VERIFIED at R2 by an independent
                      session that re-derived every finding from primary
                      source before reading any fix: the transcript at
                      the four M1 markers, its own gap scanner (7 ten-
                      second gaps confirmed), the SWF RECT parsed from
                      all 21 canonical files (exactly 3 at 1280x738),
                      MMM-NOTES read at source (four averages, no 800
                      in 84 pages), PT-035 §6 read in the PRE-
                      REGISTRATION BLOB, and the binomial re-derived in
                      its own run-length DP (99.93 / 54.13 / 100.00 /
                      84.19). PT-035 and run_pt035.py are BYTE-UNCHANGED
                      -- verified by blob SHA and single-commit history,
                      not by diff -- and both re-executed to byte-
                      identical output. Item 78 verified on BOTH halves
                      (the reviewer's SWF_CAPTURE_RECIPE.md policy edit
                      at 89bb858, whose probe script was RUN VERBATIM
                      here on both stage classes, and the student half)
                      and found mutually consistent. Superseded-text
                      convention followed at every site checked; the
                      transcript body is byte-identical by hash; 208
                      citations, ZERO orphans; validator 103/0/0.
                      V09 does NOT reach COMPLETE — items 81-83 are
                      owed and V09 reaches COMPLETE at R3. Gate to V10
                      REMAINS OPEN under D-024.
                      ⚠ THE R1 REMEDIATION WAS PERFORMED BY THE SAME
                      SESSION THAT WROTE R1, AT OWNER DIRECTION. The
                      D-003 deviation is DISCHARGED: that session closed
                      nothing, and this independent R2 supplied the
                      verification the authorization did not waive.
                      (Superseded text, retained per REMEDIATION_PROTOCOL
                      §2 -- this block previously read:)
                      "IN REMEDIATION: 1 (V09 — R1 REVISE 2026-08-13,
                      0 CRITICAL / 0 MAJOR / 6 MINOR (open items 73-78).
                      ALL SIX APPLIED 2026-08-13 on branch
                      fix/v09-r1-minors (D-038),
                      PENDING VERIFICATION at R2 -- superseded text
                      retained in place per REMEDIATION_PROTOCOL.md §2
                      at every site, and the item-76 fix is STRUCTURAL:
                      frame cross-references now name the burned-in
                      timecode, which no later insertion can invalidate.
                      NOTHING IS SELF-CERTIFIED and NOTHING IS CLOSED:
                      D-003 reserves verification to an independent
                      reviewer. ⚠ AND THE REMEDIATION WAS PERFORMED BY
                      THE SAME SESSION THAT WROTE THE REVIEW, AT OWNER
                      DIRECTION -- a D-003 deviation, disclosed in
                      V09_MASTERY_REPORT.md Revision R1 and in LOG.md
                      rather than resolved. V09 R2 MUST be an
                      independent session and must re-derive each item
                      from source. Gate to V10 OPENS under D-024 — the
                      minors are deferred and still owed, and V09
                      reaches COMPLETE only at R2."
                      (End of superseded R1 text. What follows is R1's
                      own verification record, which R2 re-derived
                      independently and CONFIRMS in every particular.)
                      NOTHING LOAD-BEARING WAS ACCEPTED ON THE
                      SUBMISSION'S AUTHORITY: PT-035 was re-run to a
                      BYTE-IDENTICAL data/pt035_output.txt; its headline
                      binomial result was RE-DERIVED FROM FIRST
                      PRINCIPLES in the reviewer's own run-length
                      recursion (99.93% at p=0.50, 54.13% at p=0.73,
                      threshold 84.19%) rather than checked against the
                      runner; all four committed scripts re-ran to
                      byte-identical output; the source SHA-256 and BOTH
                      audio durations were re-measured (3146.814694 s ==
                      3146.814694 s, 64001 vs 40000 bit/s); the
                      transcript's timestamp structure was re-derived
                      mechanically and ONE claim in it falsified (M3);
                      312 marker citations were machine-checked with
                      ZERO orphans; and six load-bearing frames were
                      read as images.
                      THE CONTINUITY PREDICTION IS GENUINE AND IS
                      VERIFIED IN GIT: 3026a81 at 11:10:45 and d9e4f9e
                      at 11:59:51, both authored by the V08 session,
                      against V09's first artifact at 13:21:36. All four
                      non-acoustic strands hold; strand 4 was confirmed
                      by comparing V08's end card and V09's opening
                      frame IMAGE-TO-IMAGE. The unrun acoustic screen is
                      NOT a gap — running it was PROHIBITED by the V07
                      GATE carry-forward.
                      THE N3 SELF-CORRECTION IS REAL, not narrated: the
                      runner PRINTS "CLUSTERING CONFIRMED" and scores P4
                      RIGHT; BT_V09_0001 withdraws both and scores P4
                      VOID. M2 is the one place the same gate was not
                      applied twice — PT-035 §6 makes an N3 failure
                      INDETERMINATE for the EMPIRICAL arm too, and that
                      clause is neither applied nor disclosed. The
                      CONTRADICTED verdict survives it on §2c closed
                      form, which the reviewer re-derived.
                      THE CAPTURE BUG IS CONFIRMED AND GENERALISED from
                      the SWF headers of all 21 source files: V08, V09
                      and V21 declare a 1280x738 stage, the other 18
                      declare 1024x786. It is stage geometry, not a
                      per-file fluke — and it ALREADY FAILED ON V08,
                      which V08's own INDEX.md records (M6).
                      SWF_CAPTURE_RECIPE.md is FIXED BY THE REVIEWER on
                      the integration branch as a POLICY-ledger edit
                      under D-038a.
                      Dimension B was SCORED, not carved out: NOT
                      SATISFIED, blocked by D-030, structural and not
                      attributable to the student, carrying NO severity
                      charge. No owner directive was issued for this
                      round — open item 36 is now owed for the FIFTH
                      lesson running.
                      REVIEWED ON BRANCH review/v09, branched FROM
                      video/v09 (bb4097b), which had DIVERGED 11 commits
                      each way from integration. Integration was merged
                      INTO review/v09 before the ledger rows were
                      written, so this round's REVIEW_INDEX.md and
                      LOG.md additions sit on top of V07 R2/R3 and V08
                      R2 rather than reverting them. BOTH review/v09 AND
                      video/v09 ARE MERGED to integration by this
                      reviewer as the deliberate D-038 merge-back —
                      required this round because the recipe fix cannot
                      be made anywhere else. SEE ALSO item 72: the
                      shared-working-directory switch that round charged
                      to PROCESS WAS THIS SESSION, and V09_REVIEW_R1.md
                      N8 discloses it against the reviewer.)"
                      (End of superseded R2 text. R2's own verification
                      record above stands unaltered and is CONFIRMED
                      wherever this round re-derived the same fact --
                      the frame identities, the MMM-NOTES arithmetic and
                      the transcript readings all reproduce. What this
                      round adds is the mechanized sweep R2 charged as
                      missing, and what it CANNOT add is R2's
                      independence.)

                     (Previously — EVERYTHING BELOW THIS LINE IS
                      RETAINED HISTORICAL TEXT describing V08's state
                      BETWEEN R1 AND R2, kept per REMEDIATION_PROTOCOL.md
                      §2 and superseded by the V08 entry under PASSED
                      above; read it in the past tense.
                      V08 — R1 REVISE 2026-08-13, 0 CRITICAL / 0 MAJOR /
                      3 MINOR (open items 64-66) — ALL THREE NOW CLOSED
                      AT R2.
                      Gate to V09 OPENS under
                      D-024 — the minors are deferred and still owed, and
                      V08 reaches COMPLETE only at R2. Dimension B was
                      SCORED, not carved out: NOT SATISFIED, blocked by
                      D-030, structural and not attributable to the
                      student, carrying NO severity charge. No owner
                      directive was issued for this round — open item 36
                      is now owed for the FOURTH lesson running.
                      REVIEWED ON BRANCH review/v08, branched FROM
                      video/v08 (d9e4f9e). BOTH ARE NOW MERGED into the
                      integration branch (46d09ed, a025b97), and the
                      D-038 ledger-location question is RULED as D-038a —
                      open item 68 CLOSED. Open item 69, the cross-branch
                      C-007/C-008 identifier collision it surfaced, is
                      CLOSED at the infra/add-steve-moro-reference-book
                      merge-back.
                      ALL THREE MINORS APPLIED 2026-08-13 on branch
                      fix/v08-r1-minors (D-038), PENDING VERIFICATION at
                      R2. Superseded text retained in place per
                      REMEDIATION_PROTOCOL.md §2 at every prose site; the
                      item-66 fix is a FILE RENAME, so the old filename is
                      retained by explicit naming in a dated correction
                      block in 04_SCREENSHOTS/V08/INDEX.md rather than as
                      an inline superseded passage. PT-034 was NOT edited
                      (item 65 is a forward requirement; COMMON_PROTOCOL
                      §9 rule 7). NOTHING IS SELF-CERTIFIED: D-003
                      reserves verification to an independent reviewer,
                      and this remediation session neither re-reviewed nor
                      closed anything.)
AWAITING REVIEW:  0  (V10 R1 is DONE, 2026-08-13 -- REVISE, HIGH
                      confidence, 0 CRITICAL / 0 MAJOR / 4 MINOR / 7 NOTE.
                      The V11 gate is OPEN under D-024 and V11 may start;
                      V10 is NOT COMPLETE until items 91-94 are applied
                      and re-reviewed. The next trigger is V10 R2 on
                      student resubmission. V10 R1 additionally CLOSED
                      item 87 (the SWF_CAPTURE_RECIPE.md §10 frame-rate
                      defect) by policy edit on the integration branch
                      under D-038a, and renumbered V10's open items
                      81-85 to 86-90 to resolve a collision with V09 R2 --
                      see the RENUMBERING DISCLOSURE beneath the
                      open-items table.

                      Superseded text, retained: "V09 R1 is DONE. Nothing is awaiting a first review.
                      The next trigger is V09 R2, on student
                      resubmission with items 73-78 applied. V10's gate
                      is OPEN under D-024 and V10 may start.

                      Superseded text, retained: "V08 R2 is DONE and V08
                      is COMPLETE — no further V08 round is triggered.
                      V07 R3 is COMPLETE and closed. Nothing is awaiting
                      a first review, and NO lesson is in remediation for
                      the first time since V01. The next review trigger
                      is R1 of V09, whose student submission exists on
                      the unmerged branch video/v09 (bb4097b) and is NOT
                      part of this round.")
```

> *(Superseded STATUS text, retained per `REMEDIATION_PROTOCOL.md` §2 — between V08's R2 and
> this V09 R1 review, `LESSONS REVIEWED` read `8`, `IN REMEDIATION` read
> `0  (NONE — for the first time since V01, no lesson is in remediation…` and `AWAITING REVIEW`
> carried the V09-not-yet-reviewed text now retained inside its own entry. V09's R1 restores
> `IN REMEDIATION` to **1**; V08 and V07 remain `COMPLETE` and are untouched by this round.)*

> *(Superseded STATUS text, retained per `REMEDIATION_PROTOCOL.md` §2 — between the V08
> remediation and this R2 review, `PASSED` read `7` and carried no V08 entry; `IN REMEDIATION`
> read `1  (V08 — R1 REVISE 2026-08-13, 0 CRITICAL / 0 MAJOR / 3 MINOR (open items 64-66)…`
> without the `— ALL THREE NOW CLOSED AT R2` qualifier; and `AWAITING REVIEW` read `0  (V08 R2 is
> TRIGGERED: the remediation of items 64-66 is complete and submitted for verification. V07 R3 is
> COMPLETE and the lesson is closed — no further V07 round is triggered. Nothing is awaiting a
> first review.)`. The three minors are no longer merely applied; they are **verified and
> closed**, and V08 has reached `COMPLETE`.)*

> *(Superseded STATUS text, retained per `REMEDIATION_PROTOCOL.md` §2 — between V08's R1 review
> and this remediation, the `IN REMEDIATION` V08 entry ended at `…is CLOSED at the
> infra/add-steve-moro-reference-book merge-back.)` with no applied note, and `AWAITING REVIEW`
> read `0 (V07 R3 is COMPLETE and the lesson is closed — no further V07 round is triggered.
> Nothing is awaiting a first review.)`. The three minors are no longer deferred; they are
> **applied and owed verification**. `IN REMEDIATION` stays at **1** and V08 stays `⏳` — this
> remediation does not move V08 toward COMPLETE, only toward reviewable.)*

> *(Superseded STATUS text, retained per `REMEDIATION_PROTOCOL.md` §2 — between the item-70
> remediation and this R3 verification, `PASSED` read **6** and did not list V07; `IN REMEDIATION`
> read **2** and opened with the full V07 R2 entry — `V07 — R2 REVISE 2026-08-13, 0 CRITICAL /
> 0 MAJOR / 1 NEW MINOR (open item 70). … Item 63 stays OPEN until item 70 discharges. … V07 does
> NOT reach COMPLETE. … Open item 36 is now owed for the FIFTH lesson-round running. REVIEWED ON
> BRANCH review/v07-r2, cut from the integration branch at f3f9006 (D-038)…` followed by
> `ITEM 70 APPLIED 2026-08-13 on branch fix/v07-r2-item70 (D-038), PENDING VERIFICATION at R3 …
> NOTHING IS SELF-CERTIFIED: D-003 reserves verification to an independent reviewer, and this
> remediation session neither re-reviewed nor closed anything.` — and `AWAITING REVIEW: 0 (V07 R3
> is TRIGGERED: the remediation of item 70 is complete and submitted for verification. Nothing is
> awaiting a first review.)`. **The remediation was right not to self-certify.** R3 verified it
> independently: items **70** and **63** are now CLOSED, V07 is **COMPLETE**, and the full R3
> record — including the bracket-token ruling, the four verifier precision bounds and the
> overwrite investigation — is in `18_REVIEW/V07/V07_REVIEW_R3.md`.)*

> *(Superseded STATUS text, retained — between the V07 R2 review and this item-70 remediation the
> `IN REMEDIATION` V07 entry ended at `…REVIEW_INDEX.md and LOG.md written there as evidence
> ledgers per D-038a.` with no applied note, and `AWAITING REVIEW: 0 (V07 R3 is triggered by
> remediation of item 70. Nothing is awaiting a first review.)`. Item 70 is now **applied and
> owed verification**, not open and unworked. **Item 70 is NOT closed here** — `D-003` reserves
> that to an independent reviewer at R3, and item 63 stays open until 70 discharges.)*

> *(Superseded STATUS text, retained — between the V07 R1 remediation and this R2 verification
> the `IN REMEDIATION` V07 entry read: `V07 — R1 REVISE 2026-08-13, 0 CRITICAL / 0 MAJOR /
> 3 MINOR (open items 61-63). ALL THREE APPLIED 2026-08-13 on branch fix/v07-r1-minors (D-038),
> PENDING VERIFICATION at R2 -- superseded text retained in place per REMEDIATION_PROTOCOL.md §2
> at all three sites. Nothing is self-certified: D-003 reserves verification to an independent
> reviewer, and that remediation session neither re-reviewed nor closed anything. Gate to V08
> remains OPEN under D-024. V07 reaches COMPLETE only at R2. Dimension B was SCORED, not carved
> out: NOT SATISFIED, blocked by D-030, structural and not attributable to the student, carrying
> NO severity charge -- UNCHANGED by that remediation.`, with `AWAITING REVIEW: 0 (V07 R2 is
> triggered: the remediation of items 61-63 is complete and submitted for verification.)`. **Two
> of the three verified; the third verified in half.** V07 does not reach COMPLETE at R2.)*

> *(Superseded STATUS text, retained — between V07's R1 and this remediation the
> `IN REMEDIATION` entry read `3 MINOR (open items 61-63). Gate to V08 OPENS under D-024 — the
> minors are deferred and still owed, and V07 reaches COMPLETE only at R2.` with `AWAITING
> REVIEW: 0` unqualified. The three minors are no longer deferred; they are applied and owed
> **verification**.)*

> *(Superseded STATUS text, retained — between V06's R2 and V07's R1 this block read
> `LESSONS REVIEWED: 6` / `PASSED: 6 (… V06 — PASS at R2 2026-08-13, COMPLETE. Dimension B
> carried as "blocked by D-030, excluded from pass/fail per owner directive". V07 gate OPEN.)`
> / `IN REMEDIATION: 0` / `AWAITING REVIEW: 0`.)*

> *(Superseded STATUS text, retained — between V06's R1 and R2 this block read
> `IN REMEDIATION: 1 (V06 — R1 REVISE 2026-08-13, 0 CRITICAL / 1 MAJOR / 3 MINOR
> (open items 57-60). Gate to V07 CLOSED under D-024 pending remediation of the
> MAJOR and re-review. Dimension B blocked by D-030 ("push" undefined), EXCLUDED
> from pass/fail per owner directive — it is not what holds the gate.)`. R2
> verified items 57-60 closed the same day; the item-57 sweep surfaced one further
> MINOR (M5), fixed and verified in-round. Same-session remediation and re-review
> were owner-directed and are disclosed in `V06_REVIEW_R2.md`'s header;
> `CUMULATIVE_25.md` should independently re-sample this round.)*

> *(Superseded STATUS text, retained — before V06's R1 this block read
> `LESSONS REVIEWED: 5` / `IN REMEDIATION: 0` / `AWAITING REVIEW: 0`.)*

> *(Superseded STATUS text, retained — before V05's R3 PASS this block read:
> `PASSED: 4 (V01, V02, V03, V04 — V04 PASS at R2, COMPLETE)` /
> `IN REMEDIATION: 1 (V05 — R2 REVISE, 0 CRITICAL / 0 MAJOR / 5 MINOR. R1
> REVISE (0/0/6) + R1B REVISE (0/0/4, parallel second opinion in the same
> round) = 10 R1-round minors. R1's 6 VERIFIED APPLIED at R2 and CLOSED; open
> item 39 (EMA 3 -> 2) APPLIED AT R2 and CLOSED; R1B's 4 + its note n1 are
> CONFIRMED VALID and were adopted as M7-M11 -> open items 47-51; ALL FIVE
> (M7-M11) APPLIED 2026-08-11, PENDING R3 VERIFICATION, with the M11
> marker-existence sweep run and CLEAN (no fourth cluster member); the
> dimension-B re-disposition remains blocked on an owner ruling (open item
> 36); V06 gate OPEN under D-024)`. R3 verified all five applied, re-derived
> from source, and re-ran the sweep independently; the dimension-B/G
> re-labelling stays owner-blocked on open item 36 and does not gate.)*

**V05 review lineage — four files, two rounds of remediation, closed at R3.**
`V05_REVIEW_R1.md` (`c41e686`) and `V05_REVIEW_R1B.md` (`8403914`) are **two independent
reviews of the same round**, produced concurrently by duplicate sessions; R1B declined to
overwrite R1 and named itself accordingly (`SETUP_ISSUES.md` I-002, `REVIEW_PROTOCOL.md` §11).
R1B was committed but **never indexed** — it was referenced zero times in this file and zero
times in `LOG.md` — so the remediation at `152f4ea` addressed R1's six minors only.
`V05_REVIEW_R2.md` verifies those six, applies open item 39, and **folds R1B into this lineage**:
its four findings plus its note `n1` are adopted as `M7`–`M11` (open items 47–51), its body is
**unedited and NOT marked invalid** (all five reproduce against `HEAD`), and an append-only
status footer points readers here. **`V05_REVIEW_R2.md` was the operative list of what V05
owed; `V05_REVIEW_R3.md` (2026-08-12) verifies all five applied — each re-derived from
primary source, the `M11` marker-existence sweep re-run independently and clean, frame 26's
disputed left label read a third time and upheld as *value not legible* — and closes V05 at
`PASS` (0 critical / 0 major / 0 minor).** The dimension-B/G re-labelling stays
owner-blocked (open item 36) and does not gate. Whether parallel reviews become policy is an
owner decision.

V01 reviewed 2026-08-10 (R1): `REVISE`, confidence HIGH. 0 critical, 2 major.
V01 re-reviewed 2026-08-10 (R2): `REVISE`, confidence HIGH. 0 critical, 1 major.
V01 re-reviewed 2026-08-10 (R3): **`PASS`**, confidence HIGH. 0 critical, 0 major.
All 15 of R2's required actions verified applied against the source, not against the
commit message. R2 finding N1 (the only open MAJOR) is closed. **The V02 gate is now
open** — D-004 satisfied.

V02 reviewed 2026-08-10 (R1): **`REVISE`**, confidence HIGH. 0 critical, 1 major,
5 minor. Reviewed by a genuinely independent session (D-003 satisfied). The source
notes, interpretation, ambiguity and contradiction work are the strongest evidence
artifacts in the repository to date, and V01's recurring `E11` citation defect does
**not** recur. The single MAJOR is in the homework: the 11a markup contradicts the
chart it cites, and produces a false confirmation that a real week held away from its
Monday high for three days — bearing directly on `C-001`. **V03 remains gated** until
V02 receives reviewer `PASS`.

V02 re-reviewed 2026-08-10 (R2): **`REVISE`**, confidence HIGH. 0 critical, **0 major**,
3 minor — **plus 1 MAJOR process finding: the D-004 V03 gate is being breached.** **R1's MAJOR is CLOSED**, verified by re-measuring the committed PNG in the R2
session rather than by reading the new pipeline's self-description: every price, day,
direction and hour in the corrected markup reproduces to within 0.2 pip, as does the
72-hour `C-001` result. The `C-001` non-resolution is correct in both directions — the
datum is recorded and fenced, and no day-count value is committed anywhere. R2 returns
`REVISE` because the remediation deliberately escalated one item *to* R2 (the `PFH`/`PFL`
count R1 had signed off on, now adjudicated: both abbreviations occur **zero** times), and
because the corrected §1.1 measurement misplaces one bar at the Fri 31 Jul → Sun 2 Aug
boundary and rests on a *"self-validating on all six boundaries"* claim that does not
hold — continuity was tested at a weekend boundary, where it should not be expected. **No
conclusion in the homework changes**; §1.1 is charged only because two files advertise it
as the reusable pipeline for the dimension-G backtest.

**The V03 gate did NOT hold.** It had held at review start — `git status` showed no V03
artifact — and by the time R2 staged its files the tree contained an in-progress V03
student pass (`02_TRANSCRIPTS/V03/V03_TRANSCRIPT.md`, 1,230 entries, marked COMPLETE;
`04_SCREENSHOTS/V03/` and `05_HOMEWORK/V03/` created; `QUARANTINE_REGISTER.md` +102 lines
adding `Q-003`, whose own text says it precedes *"writing V03's notes"*), from a session
other than the reviewer's, while `COURSE_PROGRESS.md` reads `V03 GATE: CLOSED` and V02 is
unpassed. **Second occurrence, and unlike R1's it is not moot** — V02 is `REVISE` with
three corrections outstanding, one of them in the measurement pipeline V03's chart work
would inherit. Charged as a **process** MAJOR, deliberately kept out of V02's mastery
counts, and left untouched and unstaged by R2. **V03 remains gated; the pass must stop
until V02 receives `PASS`.**

V02 re-reviewed 2026-08-10 (R3): **`PASS`**, confidence HIGH. 0 critical, 0 major,
2 minor — both non-blocking. **Both of R2's required student corrections are applied and
both were re-derived from the source in the R3 session, not read from the diffs.** The
chart was re-measured from the committed PNG with an independent pipeline (177 bars,
52.277 px per 0.00100, max residual 0.086 pip, validated against the header's *printed*
last-bar OHLC to 0.48 pip) and the transcript re-counted by regex over the verbatim body.
Everything reproduces: the day separators at `x = 147, 273, 429, 573, 717, 861, 987, 1149`;
Sun 2 Aug = **2 bars**, open **0.80552**, high **0.80737 `23:00`**; Fri 31 Jul open
**0.80578**, low **0.80538**, close **0.80678**; the weekend gap at **−12.63 pip**; the
`31` and `Aug` label centroids at **146.12** and **273.03**; and `PFH`/`PFL` at **zero**
occurrences with "peak formation" spelled out four times. `REMEDIATION_PROTOCOL.md` §2 was
verified line by line — every deleted line has a superseded-in-place counterpart.

**Open item 12 is DISCHARGED.** The two remaining minors are documentation-precision items
inside sentences that were themselves just corrected, neither of which changes any value or
conclusion: the `level count` clause in `V02_TRANSCRIPT.md` (the literal string occurs zero
times; the referent occurs once at `[00:33:11]`), and the *"174 of 176"* continuity figure,
which does not reproduce — R3 measures **172** at the stated 0.15-pip threshold or **175**
above 0.8 pip, with three genuine sub-pip gaps besides the weekend one. **The continuity
figure is recorded against R2, not against the student**, since required correction 1
instructed the student to state R2's number and the remediation did so accurately. This is
the second round in a row in which a reviewer's own verified figure failed to reproduce
under the next round's independent measurement (R1's `PFH`/`PFL` count at R2, R2's
continuity count at R3) — the pattern is worth carrying to `CUMULATIVE_25.md`.

**The V03 gate is now OPEN** — D-004 satisfied. Separately, the project owner has confirmed
the parallel V03 work as an **intentional override** of the closed gate rather than an error
to correct. R3 took no position on the override itself but recorded that it was **not yet
written down**: `DECISIONS.md` had no entry for it, so `COURSE_PROGRESS.md` and open item 9
below described an authorized action as a live violation. Recommended owner action —
record it as a numbered decision and reconcile both. **The mechanism finding behind open
item 9 survives the override and is not closed by it:** a written gate with no enforcement
failed twice in one day.

> **DISCHARGED 2026-08-10 by the project owner.** `DECISIONS.md` **D-023** records the
> override (one instance, V02 → V03, not precedent, not to be reverted) and
> `COURSE_PROGRESS.md` is reconciled to it; open item 17 is **CLOSED**. Recorded with it,
> **D-024** sets the standing rule this collision exposed: a review round with **0
> `CRITICAL` and 0 `MAJOR`** opens the next lesson's gate even on a `REVISE` verdict, with
> the minor fixes deferred but still owed before the lesson can reach `COMPLETE`; **any
> `CRITICAL` or `MAJOR`** holds the gate closed until fixed *and re-reviewed*. Under D-024,
> V02 R2 would have opened the V03 gate on its own terms and no override would have been
> needed. Open item 9 remains **OPEN** on its mechanism ground, unchanged.

V03 reviewed 2026-08-10 (R1): **`REVISE`**, confidence HIGH. **0 critical, 0 major,
3 minor** — under D-024 the **V04 gate is OPEN**, with the minors owed before V03 reaches
`COMPLETE`. This is the strongest student submission to date, and the review was run
adversarially against the six audit items the mastery report itself nominated. Everything
load-bearing reproduced: the citation audit was independently re-performed (425 marker
citations checked for existence; **99 quote+timestamp pairs re-matched at exact marker
resolution, all 99 resolving**), the §4e fifteen-`R =`-label correction re-derived from
independent crops, A-026's spoken resolution read directly in a full-transcript pass, the
homework's 116/116 chain validation and every derived table figure recomputed from the raw
JSON, the dataset externally corroborated against ECB reference fixes on all five days and
all four pairs, and — the round's substantive addition — **the C-004 negative claim was
re-verified on the complete 857-frame sweep** (found intact in the prior session's
scratchpad, identity confirmed pixel-exactly, re-clustered into 76 states, every state
reviewed: no session-times slide exists in V03). The three minors are precision defects
that change no conclusion: the homework's ADR figures do not re-derive from the committed
data (E19), the transcript's coverage block claims "strictly monotonic, no duplicates"
against three benign same-second duplicate markers (E20), and the 2.5–3-day-window
finding is stated as 4-of-4 where only 2 of 4 measure the taught object (E02 — the datum
must be scoped before it is cited against `C-001`). Reviewer-side housekeeping in this
round: the DECISION TABLE below had never gained its V02 R3 row (same staleness class as
open item 14); added with this update.

**Student remediation applied 2026-08-10 (same day, post-R1).** All three minors were
corrected: M1 — the day-boundary convention is now stated in homework §2.5 (the 21:00 UTC
FX day, five days of six 4h bars) and the twenty per-pair daily ranges behind it are
committed in the file, with the four ADR figures recomputed under that stated convention
(46.5 / 55.7 / 138.9 / 54.4; the un-re-derivable 47.0 / 54.8 / 148.2 / 56.5 are retained
in a correction note); M2 — the transcript's I-008 coverage line now reads
"1,230 timestamps, 1,227 distinct, non-decreasing throughout, three benign same-second
adjacent pairs", the duplicates named; M3 — the duration finding is scoped to 2 of 4 in
homework §2.5 Finding A, homework §4 point 3, and mastery report §2 and §D. No conclusion
changed anywhere: 0 of 4 still reach 3 × ADR, and both supported pairs still exceed the
taught window. **Open items 18–20 move to APPLIED — PENDING VERIFICATION at R2.**

V03 re-reviewed 2026-08-10 (R2): **`REVISE`**, confidence HIGH. 0 critical, 0 major,
**1 minor**. Remediation-verification round by a fresh session; each of the three minors
was re-derived from primary data rather than read for plausibility. **M1 and M3 verify
cleanly and close.** M1: the 21:00-UTC FX day is the only convention that splits the
30-bar dataset into five whole days, all twenty committed daily ranges reproduce exactly
from the raw JSON, all four ADR figures and their multiples re-derive, and 0 of 4 reaching
3 × ADR holds with margin (max 2.41×). M3: the 2-of-4 scoping is correct against the raw
OHLC — USDJPY and USDCHF never cut their block low, whose level *is* the week low at
bar 0 — and propagation was verified at all four named sites plus a whole-repo sweep for
surviving pre-correction figures; the `C-001` non-citation was independently confirmed by
reading the record, making the deferral legitimate. **M2 does not close.** The replacement
wording is correct in every component, but it was applied to the `PROVENANCE` I-008
criterion only — the `COVERAGE` block R1 explicitly named still reads *"strictly
monotonic, no duplicates"*, so `V03_TRANSCRIPT.md` now contradicts itself fourteen lines
apart. Carried as **R2 M2′ (`E20`)**; open item 19 stays open with a corrected status.
The V02 cross-check was re-tested independently and the remediation is right — V02 is
genuinely strictly monotonic (1,026 / 1,026). **Open items 18 and 20 CLOSE. V03 does not
reach `COMPLETE` this round**; the V04 gate was already OPEN per D-024 and is unaffected.

**Student remediation applied 2026-08-10 (commit `492bb11`).** The `COVERAGE` block's
residual sentence was replaced with the true statement; the verified I-008 wording at
lines 39–47 was correctly left alone. **Open item 19 moves to APPLIED — PENDING
VERIFICATION at R3.**

V03 re-reviewed 2026-08-10 (R3): **`PASS`**, confidence HIGH. **0 critical, 0 major,
0 minor.** Single-item closing round by a fresh session. `M2′` is discharged: the
`COVERAGE` and `PROVENANCE`/I-008 blocks now assert the same proposition, and it is true —
**1,230 markers, 1,227 distinct, zero decreasing transitions, exactly three adjacent
same-second pairs at `[00:35:21]` / `[01:00:13]` / `[01:04:30]`, largest gap 13 s at
`[01:09:02]`, final entry `[01:10:39]`** — every component re-derived this session by an
independent marker scan, with the header-block counting artifact explicitly ruled out (all
1,230 counted markers fall between lines 115 and 3,802, below the last `##` heading at 87).
The diff was read rather than the commit message: one file, five lines, `COVERAGE` only.
No third instance of the claim survives, and the **`E20` monotonicity class is now empty
project-wide** on a fresh scan of all four transcripts (V01 makes no claim; V02 is
genuinely strict at 1,026 / 1,026; V04 states the weaker true property). `LOG.md`
1746–1747 confirmed untouched and properly superseded at `LOG.md` 1848 ff. — append-only
handling is correct and must not be "fixed". `validate_project.py` clean: 97 / 0 / 0.
**Open item 19 CLOSES, completing 18–20. V03 is `COMPLETE`** — the V04 gate, already OPEN
under D-024, is now open on V03's own `PASS`.

V04 reviewed 2026-08-10 (R1): **`REVISE`**, confidence HIGH. **0 critical, 0 major,
7 minor**, 5 note — under D-024 the **V05 gate is OPEN**, with the minors owed before V04
reaches `COMPLETE`. Reviewed by a fresh session (D-003). **This is the strongest submission
in the repository to date and it is not close.** Everything load-bearing reproduced under
independent measurement: **487 of 487** cited markers resolve to markers carrying their
words (`E11` absent for a third consecutive lesson — **de-escalated**); **320** italic-quoted
fragments were re-matched against the transcript body with only two inexact; the homework's
**476/480** cross-check against V03's dataset, its **474/480** 4h↔15m reconstruction, every
block figure, every weekly extreme and the **3.83-day** duration on both formed-anchor pairs
were recomputed from the committed JSON and match to the decimal; and the fenced 9-entry ASR
tail was confirmed properly fenced, terminated and uncited anywhere.

**The `M3` reproduction is genuine, not copied** — the two datasets *disagree* on four
fields, carry entirely different schemas, and both harvest scripts are committed. **This is
the project's first true cross-session replication.**

**The systemic-fabrication claim was verified at full population rather than spot-checked,
and is broader than the student claimed.** All 21 quarantined `RULES.md` files carry both
template quotes at `[00:05:00]` and `[00:18:00]`, exactly two rules each, **and a
byte-identical `NUMERICAL PARAMETERS` block (one hash, 21/21)**; `INFERRED VISUAL RULES` and
`TERMS` each have only two variants across 21 files. `EMA` occurs **zero** times in V04's
transcript. **Consequence for V05–V21: the per-lesson `RULES.md` audit is a solved problem**
and may be discharged in one step by confirming the three template markers and citing this
review plus `Q-004`. `NOTES.md` and `VISUAL_INDEX.md` are **not** covered — all 21 of each
are pairwise distinct and still need per-lesson examination.

**The `C-005` scope ruling is rendered in this review** — see open item 22. The
speaker-identification was verified independently, including reading *"Zen Jason … Alldredge"*
off frame 21's Navigator at 4× magnification; the boundary is confirmed by the speaker
referring to Steve in the third person 40+ times through segment B and, decisively, by
*"Steve is asking, do you ever take continuation trades?"* `[01:24:53]`. **69% measures at
68.5%.** The TDI gap was confirmed real at both cited markers and dimension G's `DEFERRED`
is upheld, as is `A-039`'s prohibition on dropping condition (c).

The seven minors are precision defects, none of which changes any conclusion: an undiagnosed
USDCHF 15-minute mis-slice at a partial week-open bar (`E19`), two smoothed quotations
inside the transcript's own verbatim-proof paragraph (`E01`), two ambiguity cross-references
pointing at the wrong records (`E20`/`E11`), a stale frame count and a stale index filename
(`E20`), a continuity validation not reproducible from committed data (`E20`), an unrecorded
visible TDI panel in two curated frames (`E20`), and four undeclared quality-control
checklist boxes (`E20`). **N1 additionally requires dimensions B and C to be re-dispositioned
from `PARTIAL`/`FAIL` to `DEFERRED` under `D-019`** — as labelled, V04 could never reach
`PASS`, because the cause sits in the source and will not change until TDI is taught.

**Pattern worth carrying to `CUMULATIVE_25.md`:** the student predicted its residual defects
would be in the interpretation file's prose. They were not — the interpretation came through
clean, and all four substantive minors landed in the **narrative describing mechanically
checked work** (the transcript's provenance paragraph, the homework's validation prose).
**The checked artifact is reliable; the paragraph describing the check is not, because it is
the one part nothing recomputes.**

V04 re-reviewed 2026-08-11 (R2): **`PASS`**, confidence HIGH. **0 critical, 0 major, 1 minor
(non-blocking)**, 3 note. **V04 is `COMPLETE`** (`D-004`). Reviewed by a fresh session that
authored no V04 artifact and applied none of the R1 corrections (`D-003`). **All seven minors,
note `N1` and the owner action are applied, and all nine verify.**

`M1`, the round's only evidence fix, was **re-derived from the data in both directions rather
than read off the diff**: the parent commit's JSON was recomputed to confirm the defect was
real (one −12.7 pip discontinuity at `m[3]→m[4]`, bar-0 open off by 28.1 pips,
`aggregate(m[4:16])` equal to 4h bar 0 on all four fields), and the corrected JSON was
recomputed to confirm the fix (**476/480 fields, 116/120 bars, zero in-week 15m
discontinuities in all four pairs**, all four residuals ≤ 0.3 pip and all in highs or lows).
The new array is exactly `old[4:]`, only USDCHF changed, and the 4h series is untouched and
continuous **116/116**. An independent cross-check the remediation did not claim: every pair's
re-indexed `j_hi_15m`/`j_lo_15m` maps through the new partial-first-bar arithmetic onto the
4h bar holding the same extreme, at an identical price — which closes under the new indices
and does not under the old ones. **The scoped 2-of-4 / 3.83-day result is unchanged**, USDCHF
still excluded on the 4-hour fact that its week low sits on bar 0.

`M5`'s judgement call was reviewed on the merits, not just for execution, and is **upheld**:
the harvest arrays were never written to disk, so committing a fresh harvest would attach data
to claims never computed on it — provenance fabrication, and worse than a declared gap. `M6`
was checked by opening both frames and magnifying them: the `Traders Dynamic Index Visual`
panel is there, the six-value readout is genuinely at the edge of legibility, and **declining
to transcribe it was correct**. `M7` accounts for all 19 `MASTERY_STANDARD.md` boxes
(13 + 2 `DEFERRED` + 4 UNCHECKED) and refuses to excuse the concept-library box by pointing at
`A-039`. `N1` follows `D-019`'s V01 F/G pattern exactly, with the original `PARTIAL`/`FAIL`
prose retained **verbatim** — diffed, not eyeballed. **`D-025` is faithful to the ruling** and
all four cross-references are live; the `REVIEW_PROTOCOL.md` §2 edit is the best of them,
because it makes future reviewers audit the **over-exclusion** direction too.

The one residual minor (`m1`, open item 34) is a mechanism clause inside a sentence written
*during* the remediation: the *"§3.3 windows are identical"* justification is true for the
high-side window (bar-for-bar identical) and false for the low-side one (clipped at the array
head; 5 bars → 1). **The descriptor table it justifies is genuinely unchanged — 1/1/1/1 on
both datasets, recomputed** — so under `REVIEW_PROTOCOL.md` §9 criterion 14 and the
`V02_REVIEW_R3.md` precedent it does not withhold the `PASS`, and an R3 for it would be the
artificial difficulty §16 forbids. **It is also one more instance of R1's own `N5` pattern**,
produced in the very commit that quoted `N5` approvingly: the paragraph describing the check
is the one part nothing recomputes.

V05 reviewed 2026-08-11 (R1): **`REVISE`**, confidence HIGH. **0 critical, 0 major, 6 minor,
5 note** — under D-024 the **V06 gate is OPEN**, with the minors owed before V05 reaches
`COMPLETE`. Reviewed by a fresh session that authored no V05 artifact (`D-003`).

**The concurrency scare is unfounded and the repository needs no cleanup.** This round was
told V05 might carry duplicated or conflicting content from several sessions running the task
at once. Verified at the repository level first: `HEAD` is `b4b690b` with **no commits beyond
it**, the pipeline is exactly **nine** commits in correct protocol order, and the two findings
described as possible separate additions (`Zen_man`, the on-screen session date) are **inside
`8223224`**, part of the main pipeline. `A-001`…`A-049` and `C-001`…`C-005` are contiguous
with **zero duplicate headings and zero gaps**; no doubled V05 blocks in `LOG.md` or
`CHANGELOG.md`; `validate_project.py` 97/0/0. The one untracked file is open item 13,
correctly left alone.

**Everything load-bearing reproduced under independent measurement.** The transcript's
coverage block is **the first in the project to assert strict monotonicity and be right** —
1,353 markers, 1,353 distinct, zero decreasing transitions, zero same-second pairs, largest
gap 13 s at both named markers, final entry `[01:08:20]`, every component re-derived (V03's
identical claim took three rounds to close, open item 19). The speaker finding was re-counted
(`Steve` **21**, `Zen` **2**, `DMR` **9**, `TDI` **6**, all exact). `C-003`'s strike-off
re-measured: **zero clock-time tokens** in the body. The fabrication quarantine was discharged
at **full population** per open item 33 — both template markers 21/21, exactly two rules
21/21, `NUMERICAL PARAMETERS` **one hash 21/21** — and `Q-005`'s audio cross-check verified
word for word. **356 citations checked, 2 defective; 92 marker-cited quote fragments
re-matched verbatim, 90 exact.** `E11` does not recur as a class.

**The screenshot findings are real and were checked against the pixels, not the prose.**
`Zen_man / System Folder` is unambiguous in the Save As dialog; the taskbar clock reads
**`10:31 PM 3/25/2012`**, which is **the first in-recording corroboration of the session
date**, until now resting on the filename alone; frame 26's status bar (`4 Majors`,
`2012.01.04 01:15`, `O 1.56413 H 1.56418 L 1.56374 C 1.56381 V 352`) reads exactly as
transcribed; and `A-043`'s toolbar dialog shows precisely the two text objects claimed —
**`A Text`** in *Selected*, **`T Text label`** in *Available*.

**The homework answers the data question cleanly and fixes V04's defect at source.** The
harvester was read line by line: it parses TradingView's **Data Window `innerText`** for
`Date/Time/O/H/L/C`; **no pixel is sampled and no colour is tested anywhere.** Every committed
figure recomputed from the JSON and reproduces exactly — **480/480/480/476 bars, 1,912/1,912
continuity with zero breaks, the full `by_day` table, and all eight extremes with prices,
timestamps and pip ranges to the decimal.** Because each bar now carries its own timestamp,
the USDCHF anomaly that broke V04 silently (open item 25) is **caught by the tooling**:
476 = 480 − 4, the missing session hour visible directly in the data, independently
reproducing V04's corrected 476 on a different week, feed and method. The boundary-limited
USDCHF week low is disclosed and the pair excluded from every conclusion depending on it.

**Three rulings were rendered on items the student escalated.** (1) **`A-043`'s closure is
AFFIRMED** (open item 40) — a record whose subject is *a guest's own utterance or a platform
artifact*, not the method, may be closed on descriptive guest evidence; owner should record
the carve-out as a `D-025` refinement so it is a rule rather than a per-record judgement.
(2) **The third-disposition escalation is upheld** (open item 36): dimension **G**'s
`NOT APPLICABLE` stands on the purposive reading — `DEFERRED` would be false, since no future
lesson makes a V05 guest rule testable — but its **stated reason must change** to "excluded by
decision under D-025"; dimension **F** stands as graded; dimension **B**'s `NOT APPLICABLE`
is **not available**, since `D-019` grants it for F and G only (same class as V04 R1 `N1`,
carried the same way as a NOTE with a required action). The reviewer recommends the owner
adopt **`EXCLUDED BY DECISION`** as a third disposition. (3) **The `EMA` 3 → 2 correction is
CONFIRMED** (open item 39) and the fix belongs in `V05_TRANSCRIPT.md` and `Q-005`.

The six minors are precision defects, none of which changes any conclusion — and none could,
because V05 yields no doctrine for a defect to corrupt: the same quote miscited two different
ways in two files, neither a marker (`M1`, `E11`); a citation off by one marker (`M2`); one
smoothed quotation dropping "level three" (`M3`, `E01`); **three V05 files disagreeing about
V05's own evidence order** (`M4`, `E20` — `INDEX.md` discloses the process deviation
prominently and correctly, and `V05_INTERPRETATION.md` line 12 claims the opposite); a stale
"V05 is the next candidate" pointer in `A-039` (`M5`); and an unrecorded oscillator sub-panel
in curated frame 26 (`M6`, the V04 `M6` class exactly).

**Pattern worth carrying to `CUMULATIVE_25.md` — the status-staleness class did NOT recur.**
All four status blocks were checked against their own contents and **all four are current**.
Open item 14 has failed in six previous rounds and is the project's most persistent weakness;
**this is the first clean round**, achieved without the `validate_project.py` guard having
been built. Separately, this round records a reviewer error worth keeping: R1 initially scored
the six record extensions as missing, because they live in a consolidated block at the foot of
`AUTOMATION_AMBIGUITIES.md` (V02's precedent) rather than inside each record. The block is
real, the mastery report's claim is accurate, and the finding was withdrawn before it was
charged — **the third consecutive round in which a reviewer's own first reading failed to
survive its own verification step.**

**The counterfactual is the round's most important observation.** Instructor runtime across
one session date runs **~100% (V03) → ~31% (V04) → 0% (V05)**. A session that skipped speaker
identification would have written an entire lesson of false doctrine — anchor theory, level
assignment, a three-day reversal expectation, an 80% accuracy claim — and every downstream
file would have inherited it. `D-025` consequence 3 was written one lesson before it was
needed. **Open item 38 is upheld and should be read at the start of every remaining lesson.**

V05 reviewed 2026-08-11 (**R1B**): **`REVISE`**, confidence HIGH. **0 critical, 0 major,
4 minor, 4 note.** A **second, independent R1** produced concurrently by a duplicate reviewer
session, which discovered R1 on disk mid-round, **declined to overwrite it** (`SETUP_ISSUES.md`
I-002, `REVIEW_PROTOCOL.md` §11), declined to race another session's uncommitted
`REVIEW_INDEX.md`, and disclosed the collision in full. It agrees with R1 on the verdict, the
gate and every finding R1 raised, and adds four of its own. **It was committed at `8403914`
but never indexed here or in `LOG.md`, so the remediation at `152f4ea` never saw it** — that
omission, not the file, is the single-source-of-truth defect, and it is corrected at R2.
Verified *within that round*: 1,353/1,353 markers; `Steve` 21, all third-person; `Q-005`'s
`VISUAL_INDEX` claim at the byte level (**12/12 SHA-256 pairs, 15 distinct images across 27
files**); all thirty ASR-garble citations; every homework figure from the committed JSON. **R2
did not re-run those** (`V05_REVIEW_R2.md` §4) — two independent confirmations already agree.
**What R2 did re-derive is R1B's five findings, and all five reproduce. Folded into the R1/R2
lineage at R2** — findings adopted as `M7`–`M11`, body unedited,
**not marked invalid**, append-only status footer added.

V05 re-reviewed 2026-08-11 (R2): **`REVISE`**, confidence HIGH. **0 critical, 0 major,
5 minor** — the V06 gate **remains OPEN** under D-024, and V05 is **NOT COMPLETE**.

**All six of R1's minors verify, re-derived from source rather than from the diff.** `M1` both
citations corrected to `[00:57:35]`–`[00:57:36]` and **split across the two markers the words
actually span**; `M2` corrected to `[00:36:05]` with that marker's literal sentence replacing
the smoothed fragment; `M3` restored verbatim with the elision removed rather than annotated —
the excised level number is back inside the file's own evidence for the level↔day relabelling;
`M4` reconciled **toward the honest file** — `V05_INTERPRETATION.md` now leads with the
deviation and names `INDEX.md` as governing, and `git show` confirms `INDEX.md` was **not
weakened** (one line touched, row 26, for `M6`); `M5` the stale TDI pointer updated with
*"a name is not a definition"*; `M6` frame 26's oscillator sub-panel recorded as **presence
only**, the illegible header verifiably **not** transcribed. **Zero scope creep, superseded
text retained at every site, and the two refusals were in the right direction.** Open item 39
(`EMA` 3 → 2) was re-derived a third time and **applied this round** at both sites — a declared
`D-003` deviation, scoped to two numerals, recorded at `V05_REVIEW_R2.md` §3.1.

**`PASS` was withheld for one reason: R1B's findings are real and none has been applied.**
All four plus its note `n1` were re-derived at R2 from the transcript and the pixels,
independently of R1B's prose, and **all five reproduce at `HEAD`** — adopted as `M7`–`M11`,
open items 47–51. `M7` is the consequential one: `CONTRADICTIONS.md`'s **STATUS block** states
that `C-003` — *"whether M and W formations can fail"* — was checked against V05 and struck
off, when the record checked was `C-004` and `C-003` contains no V05 text at all. **That also
retires R1's `N5` superlative** that all four status blocks were current; the improvement it
described is real, the superlative is not. `M11` shows R1's `M1` fixed two thirds of a single
defect — all three V05 citation errors map `00:57:3x` → `01:0x:3x`, one displaced cluster, and
a mechanical marker-existence sweep is owed with the fix.

**The honest summary: V05's understanding passed and V05's bookkeeping did not.** Across three
independent rounds V05 has drawn **ten minors, zero major, zero critical**, and every one lives
in counting, citing or cross-referencing — **not one touches what V05 was understood to mean.**
Its single load-bearing claim, *that the method is not in this lesson*, has now survived three
separate audits of the audio, the frames, the committed data and the registers. **Five small
corrections and an R3 verification pass and this lesson is `COMPLETE`.** Dimension B's
re-disposition remains **blocked on the owner** (open item 36) and is carried, not charged.

V05 re-reviewed 2026-08-12 (R3): **`PASS`**, confidence HIGH. **0 critical, 0 major,
0 minor** — **V05 is `COMPLETE`.** All five of R2's minors (`M7`–`M11`, open items 47–51)
verified applied, each **re-derived from primary source before the remediation diff was
read**: `M7`'s four `C-003`→`C-004` sites with superseded text retained and `C-004` still
`UNRESOLVED`; `M8`'s *"but up to five days"* re-counted at exactly two; `M9`'s frame-26
labels re-read from fresh 10× crops — `40.9` / `40.6` / `41.1` confirmed, and **the disputed
left label upheld as *value not legible* on a third independent read** (R1B's `74.6` stays
untranscribed); `M10`'s §4c framing verified two-of-four row by row; `M11`'s `A-042`
citation verified at `[00:57:39]`. **The `M11` marker-existence sweep was re-run from
scratch this round** — 1,353 markers, 7 non-resolving citations, all seven accounted for
(six cross-lesson cites, one burned-in slide time); **the displaced cluster is closed at
three.** The post-R2 merge (`9ad57b8`) touched no V05 artifact — verified by diff. The
dimension-B/G re-labelling stays owner-blocked (open item 36) and does not gate
(`REVIEW_PROTOCOL.md` §9 criterion 14; §1 forbids holding a lesson on an owner-blocked
label). Owner actions from R2 §5 (open items 35, 36, 40; R1B naming; parallel-session
ruling) are carried forward unchanged. **The next review trigger is the V06 submission, or
`CUMULATIVE_25.md` if that milestone arrives first.** `V05_REVIEW_R3.md`.

---

## DECISION TABLE

| Video | Student Status | Review Version | Reviewer Decision | Critical Issues | Major Issues | Final |
|---|---|---|---:|---:|---:|---|
| V01 | REVIEW REQUIRED | R1 | REVISE | 0 | 2 | ⏳ |
| V01 | REVIEW REQUIRED | R2 | REVISE | 0 | 1 | ⏳ |
| V01 | REVIEW REQUIRED | R3 | PASS | 0 | 0 | ✅ |
| V02 | REVIEW REQUIRED | R1 | REVISE | 0 | 1 | ⏳ |
| V02 | REVIEW REQUIRED | R2 | REVISE | 0 | 0 | ⏳ |
| V02 | REVIEW REQUIRED | R3 | PASS | 0 | 0 | ✅ |
| V03 | REVIEW REQUIRED | R1 | REVISE | 0 | 0 | ⏳ |
| V03 | REVIEW REQUIRED | R2 | REVISE | 0 | 0 | ⏳ |
| V03 | REVIEW REQUIRED | R3 | PASS | 0 | 0 | ✅ |
| V04 | REVIEW REQUIRED | R1 | REVISE | 0 | 0 | ⏳ |
| V04 | REMEDIATION APPLIED | R2 | **PASS** | 0 | 0 | ✅ COMPLETE |
| V05 | REVIEW REQUIRED | R1 | REVISE | 0 | 0 | ⏳ |
| V05 | REVIEW REQUIRED | R1B | REVISE | 0 | 0 | ⏳ |
| V05 | REMEDIATION APPLIED | R2 | REVISE | 0 | 0 | ⏳ |
| V05 | REMEDIATION APPLIED | R3 | **PASS** | 0 | 0 | ✅ COMPLETE |
| V06 | REVIEW REQUIRED | R1 | REVISE | 0 | 1 | ⏳ |
| V06 | REMEDIATION APPLIED | R2 | **PASS** | 0 | 0 | ✅ COMPLETE |
| V07 | REVIEW REQUIRED | R1 | REVISE | 0 | 0 | ⏳ |
| V07 | REMEDIATION APPLIED | R2 | REVISE | 0 | 0 | ⏳ |
| V07 | REMEDIATION APPLIED | R3 | **PASS** | 0 | 0 | ✅ COMPLETE |
| V08 | REVIEW REQUIRED | R1 | REVISE | 0 | 0 | ⏳ |
| V08 | REMEDIATION APPLIED | R2 | **PASS** | 0 | 0 | ✅ COMPLETE |
| V09 | REVIEW REQUIRED | R1 | REVISE | 0 | 0 | ⏳ |
| V09 | REMEDIATION APPLIED | R2 | REVISE | 0 | 0 | ⏳ |
| V09 | REMEDIATION APPLIED | R3 | ⚠ **SELF-VERIFIED** | 0 | 0 | ⚠ **COMPLETE — SELF-VERIFIED AT OWNER DIRECTION** |

> ## ⚠⚠ V09's `COMPLETE` IS NOT AN INDEPENDENT VERDICT. READ THIS BEFORE RELYING ON IT.
>
> **Items 81–83 were fixed AND verified by the SAME session, on the owner's explicit
> authorisation for this round specifically.** That authorisation is real and it is recorded — but
> it does not manufacture independence, and this round does **not** satisfy `D-003`. The items
> carry the status **`CLOSED — SELF-VERIFIED AT OWNER DIRECTION`**, which exists for no other
> purpose than to be visibly different from `CLOSED — VERIFIED`. The `PASS` column reads
> `SELF-VERIFIED` rather than `PASS` for the same reason. **No reviewer `PASS` was issued for this
> round by anyone other than the session that did the work.**
>
> **Precedent, and how this differs from it.** V09's own R1 remediation used the same
> owner-authorised pattern — but only for the **fix**, and it **closed nothing**, because R2 was
> still coming. **This round closes its own items.** That is the stronger deviation, which is why
> the notice is here rather than in a footnote.
>
> **What the self-verification did, so its weight can be judged rather than taken on trust.** Every
> cited marker was re-derived from `V09_TRANSCRIPT.md` with a parser written for the pass; item 82
> was re-derived **from the images**, all five PNGs opened; item 83's premise was re-derived from
> `MMM-NOTES` at source; and the generalised `verify_quotes.py` was **mutation-tested three ways**.
> **It found six defects the fix pass had missed and two errors of its own**, including a citation
> to `[00:24:55]`, a marker that does not exist. That is the only real evidence that a
> self-verification pass did any work, and it is offered as such rather than as a substitute for
> independence.
>
> **What a later reviewer should do if it wants the independence this round lacks:** re-derive item
> 81's line-410 quotation, item 82's three frame identities and item 83's `C-010` arithmetic from
> `02_TRANSCRIPTS/V09/`, `04_SCREENSHOTS/V09/` and `MMM-NOTES` directly, and re-run
> `05_HOMEWORK/V07/scripts/verify_quotes.py V09`. **None of it takes long.**
>
> *(Superseded text, retained per `REMEDIATION_PROTOCOL.md` §2 — this block previously read:
> "**V09 R2 closed R1's items 73–78 as `VERIFIED` and opened three new MINORs (81–83).** The R1
> remediation was performed by the session that wrote R1, at owner direction — a `D-003` deviation
> the owner authorized for the fix step only. **R2 is the independent verification that
> authorization did not waive**, and it re-derived all six findings from primary source before
> reading any fix. V09 reaches `COMPLETE` at R3." **R2's own verdict and verification record stand
> unaltered** — everything it said about items 73–78 is untouched, and every fact this round
> re-derived independently reproduces what R2 found. Only the forward-looking sentence about R3 is
> superseded, by this round.)*
| V10 | REVIEW REQUIRED | R1 | REVISE | 0 | 0 | ⏳ |
| V10 | REMEDIATION APPLIED | R1 (fix round) | ⚠ **SELF-VERIFIED** | 0 | 0 | ⚠ **COMPLETE — SELF-VERIFIED AT OWNER DIRECTION** |
| V11 | REVIEW REQUIRED | — | — | — | — | ⏳ *(superseded, retained: `AWAITING R1`)* |
| V11 | REVIEW REQUIRED | **R1** | **REVISE** | **0** | **0** | 🔶 **GATE TO V12 OPEN (`D-024`) · 5 MINOR (109–113) owed before `COMPLETE`** |
| V12 | REVIEW REQUIRED | **R1** | **REVISE** | **0** | **0** | 🔶 **GATE TO V13 OPEN (`D-024`) · 2 MINOR (137–138) owed before `COMPLETE`** |

> ## ⚠⚠ V10's `COMPLETE` IS NOT AN INDEPENDENT VERDICT. READ THIS BEFORE RELYING ON IT.
>
> **R1's four MINORs — items 91 (student half), 92, 93 and 94 — were fixed AND verified by the
> SAME session, on the owner's explicit authorisation for this round specifically**, on the ground
> that all four are small documentation edits. That authorisation is real and it is recorded — but
> **it does not manufacture independence, and this round does NOT satisfy `D-003`.** All four
> items carry the status **`CLOSED — SELF-VERIFIED AT OWNER DIRECTION`**, which exists for no
> other purpose than to be visibly different from `CLOSED — VERIFIED`, and the decision column
> reads `SELF-VERIFIED` rather than `PASS` for the same reason. **No independent reviewer issued a
> `PASS` for this round. There was no R2.**
>
> **This row is NOT a new review round.** It is R1's remediation, closed against R1's own findings.
> The R1 row above is untouched and its `REVISE` verdict stands as the last arm's-length judgement
> anyone made about V10.
>
> **Precedent: this is the second use of the pattern**, after V09 R2's items 81–83 on 2026-08-13,
> and it is deliberately recorded in the same words so the two are comparable and countable.
>
> **What the round actually changed, so its weight can be judged rather than taken on trust.**
> Nothing that bears on a measurement, a classification, a disposition or a rule. `M2` corrects a
> spoken-instance census from *four of six* to **five of seven** — a correction that **widens** the
> majority and therefore **strengthens** `C-017`; `M3` rescopes an absence claim from *"no hour is
> ever stated"* to *"no session-boundary clock time is stated"*, listing the four incidental times
> that falsified the stronger form; `M4` adds an ASR caution to `C-016` as a **further** reason for
> `UNRESOLVED`; `M1`'s student half turned out to be an addition rather than a correction, the two
> artifacts having never carried the stale number the review attributed to them. **Every marker
> was re-derived from `02_TRANSCRIPTS/V10/V10_TRANSCRIPT.md` at source rather than copied from the
> review**, `M2`'s sweep found **three sites beyond the four the review named**, and `M1`'s sweep
> **found the review itself to be wrong on a point of fact and says so in place.**
>
> **What a later reviewer should do if it wants the independence this round lacks:** read
> `[01:00:20]` and `[00:54:02]` in the transcript body; read `[00:02:24]`, `[00:05:09]`,
> `[00:42:52]` and `[01:03:57]` for `M3`; confirm no curated frame prints a holding period for
> `M4`; and re-run `grep -rn "item 8[1-5]"` for the renumbering. **None of it takes long.**
>
> **What is NOT closed and is NOT covered by this verdict:** open items **86** (recommended
> `PT-037`), **88** (printed-vs-spoken precedence, owner), **89** (`A-077`, the lock), **91**'s
> **policy half** (`D-038a`'s mergeability premise — an owner ruling a reviewer may not make),
> **95** (owner question) and **96** (the `COURSE_PROGRESS.md` table sweep). None of these was
> owed before `COMPLETE`; all remain open.

> **`R1B` is a parallel second opinion on the R1 round, not a separate round of remediation.**
> It is listed so the decision history is complete; the two R1-round rows describe **one**
> submission audited twice. R2 is the first remediation-verification round.

### Row template

```text
| V01 | PASS | R1 | REVISE | 0 | 2 | ⏳ |
| V01 | PASS | R2 | PASS   | 0 | 0 | ✅ |
```

Each review round gets its **own row**. Earlier rows are never edited or removed —
the progression from `REVISE` to `PASS` is part of the learning record.

### Legend

| Symbol | Meaning |
|---|---|
| ✅ | Reviewer PASS — advancement authorized |
| ⏳ | REVISE — in remediation |
| ⛔ | BLOCKED — substantial remediation required |
| 🔍 | Awaiting review |
| 👤 | Human review required |
| — | Not yet reached |

**Student Status** uses the student vocabulary (`PASS` / `REVIEW REQUIRED` /
`BLOCKED`); **Reviewer Decision** uses the reviewer vocabulary (`PASS` / `REVISE` /
`BLOCKED`). They are different actors' judgements and are deliberately not merged
(`SETUP_ISSUES.md` I-001).

---

## RECURRING ERROR COUNTS

Updated after every review. Reveals systematic weakness over time — a code that
keeps recurring is a training problem, not a lesson problem.

| Code | Description | Count | Lessons |
|---|---|---:|---|
| E01 | Source misquote | 7 | **V09 (R1 ×1 — `M1`, `MINOR`, open item 73):** four silent ASR corrections inside quotation marks under `AUDIO` basis tags in `V09_SOURCE_NOTES.md` — §3 *"Example solid **HOD/LOD** entries…"* where `[00:03:49]` says *"high low-day"*; §9a, a block introduced as *"`AUDIO`, verbatim across five markers"*, rendering `[00:41:25]`'s *"What is the **grade** Fred?"* as *"grape"*; §7e *"**experience shows** me"* for *"**experiences show** me"*; §5's stutter removal in *"what **it's it's** titanium"*. **Fifth lesson to carry this class, and the first where the file's own basis-tag mechanism is what the defect defeats** — the whole point of an `AUDIO` tag is that a reviewer may strike every other row and trust what is left. **Mitigated on three counts and therefore `MINOR`:** no conclusion moves (HOD/LOD is established from printed slides two paragraphs above, and the transcript itself renders *grape* correctly at `[00:33:21]`); the **transcript body is untouched**, every garble preserved as its TRANSCRIPTION NOTES promise; and `05_HOMEWORK/V07/scripts/verify_quotes.py` — the tool that catches exactly this — was committed to integration **after** `video/v09` branched, and is V07-specific in any case. **Required: generalise that script to take a lesson identifier and run it**, which would close the class rather than the instance | **V07 (R2 ×1 — `M1`, `MINOR`, co-code `E20`, open item 70):** the R1 `M3` remediation **repaired** §H's categorical claim rather than scoping it, and the repair is false. `V07_MASTERY_REPORT.md` §H now asserts *"no other instance exists"* and that *"it's met"* and *"mayo"* *"were moved **outside** the quotes"* — **three quotations falsify it**: `V07_SOURCE_NOTES.md` §9a renders `[00:27:24]`'s *"…30 minute of the **male**,"* as *"…30 minute of the **mayo**."* (while §10 of the same file measures `mayo` at **0** and §9's evidence table ten lines above renders it correctly with the reconstruction outside the quotes); `V07_SOURCE_NOTES.md` §11's row headed *"`[00:25:26]`'s **unrecovered** word"* then quotes *"it turns red when **it's met**"* where the marker reads *"…when **Beth**."*; and `04_SCREENSHOTS/V07/INDEX.md` item 6 repeats the second unbracketed, where **row 15 of its own table brackets it correctly**. **The class is now a narrative-prose class specifically** — this is the fourth instance of V04 R1's `N5` (a narrative restatement of an evidence table losing the table's quotation discipline), and in two of the three cases the correct rendering sits in the same file. **No conclusion moves:** `A-020` is not disturbed, §10's `mayo` 0 row is correct, the ADR observation is correctly fenced in both places. **Counterweight, measured:** this reviewer's own sweep over the pre-remediation tree returned **238** marker-cited quotes against R1's 239 under an independently written matcher — the two agree to one fragment; the remediation's own sweep returned **167**, and that 30% gap is what the false claim rests on | **V07 (R1 ×1 — `M3`, co-code `E11`, ⚠️ HALF-VERIFIED at R2 2026-08-13 — the §D quotation and citation are CLOSED, VERIFIED against the transcript; the §H repair is NOT, and is carried as open item 70; item 63 stays open):** `V07_MASTERY_REPORT.md` §D renders `[00:28:31]`'s *"if it doesn't do what you expect **in** your flashcard isn't the same"* as *"…**and** your flashcard…"* — a silent smoothing of a garbled ASR passage inside quotation marks, **and** cited to `[00:28:28]`, which exists and carries a different sentence. **The defect falsifies §H's own categorical claim** *"No quotation mark in any V07 artifact contains a word that is not in the source"*. **Counterweight, measured:** this reviewer machine-checked **239 marker-cited quotes across seven V07 artifacts and this is the only defect in the set** — the narrative-prose-vs-evidence-table pattern (V04 `M2`, V05 `M3`) holds, and `V07_SOURCE_NOTES.md` §6c renders the same passage correctly | **V05 (R1B ×1 — `M8`, APPLIED 2026-08-11, pending R3 verification, open item 48):** `V05_MASTERY_REPORT.md` §E counts the verbatim string *"but up to five days"* **four times**; it occurs **twice**. **Third live instance of the verbatim-count class** (open items 15, 39) — three is `REVIEW_PROTOCOL.md` §7's escalation threshold, raise at `CUMULATIVE_25.md`. **V05 (R1 ×1 — `M3`, ✅ CLOSED — VERIFIED at R2 2026-08-11, open item 43):** `V05_SOURCE_NOTES.md` §4b renders *"…and **level three** second leg of that pattern…"* `[00:13:05]` as *"**the** second leg of that pattern…"*. Third occurrence overall and **second consecutive lesson** — both times inside supporting prose rather than the notes proper. Not an escalation trigger on its own, but the pattern is now "quotations in narrative paragraphs are less reliable than quotations in evidence tables", which is `N5`'s class from V04 R1 in a new guise. V02 (R1 ×1) — two ASR garbles repaired inside quotation marks; V04 (R1 ×1 — `M2`, **✅ CLOSED — VERIFIED at R2 2026-08-11** — both fragments restored to the adopted transcript's literal wording and the quoted side of the comparison stated: two of the six "matched near-verbatim" spot-check fragments in `V04_TRANSCRIPT.md` criterion 2 are smoothed readings, not the adopted wording. **The student self-caught and fixed ~20 instances of this class in its own draft before commit and the fix verifies** — an independent 320-fragment audit at R1 found only these two survivors, both in the provenance narrative rather than in the notes) |
| E02 | Unsupported generalization | 6 | **V09 (R1 ×1 — `M5`, `MINOR`, open item 77):** `V09_INTERPRETATION.md` Q5 holds the candidate `C-010` reconciliation — *the notes' `200` and the corpus's `800` are one line seen from two timeframes* — at `MEDIUM`, *"more likely than not"*, and Q8 lists evidence that the notes' `200` sits on the 1-hour as what would promote it. **Applied to the whole enumeration it fails.** `MMM-NOTES` p.38 lists **four** averages (5, 13, 50, 200); the identity is a factor of four, so reading that set on the 1-hour maps it to **20, 52, 200, 800** on the 15-minute — and the corpus carries a 5, a 13 and a 50, not a 20, a 52 and a 200. It also collides with `A-020`, whose attested mapping requires **mayo = 200 and blueberry = 800 to be two lines on one chart**. So the hypothesis reconciles **one member of four and breaks the other three**. **THE DECISION IS UPHELD AND UNCHANGED — `C-010` stays OPEN and the refusal to close it was correct**; this is charged against the confidence, not the call, and it retires the submission's own escalation 5 to the owner: the route does not reach, so there is no blending judgement left to make | **V05 (R1B ×1 — `M10`, APPLIED 2026-08-11, pending R3 verification, open item 50):** `V05_SOURCE_NOTES.md` §4c heads its table *"Repeated four times, always with the same escape clause"*; two of the four rows carry none. **The origin of `M8`** — a framing sentence becoming a false verbatim count one file downstream. V01 (R1 ×1, R2 ×2) — all closed at R3; V03 (R1 ×1 — duration finding scoped 4-of-4 where 2-of-4 is supported, M3 — **applied 2026-08-10, pending verification at R2**) |
| E03 | Missed qualifier | 0 | |
| E04 | Wrong sequence | 0 | |
| E05 | Wrong pattern boundary | 0 | |
| E06 | False positive | 1 | V02 (R1 ×1, also codes `E19`) — homework markup contradicts its own chart |
| E07 | False negative | 1 | **V06 (R1 ×1 — `M1`, `MAJOR`, co-code `E11`, open item 57):** frame `V06_00-48-29` Week 10 prints *"and more specifically at 3:45am or 9:45am est."* — legible at committed resolution, elided in the frame-26 transcription as "not legible", and its absence then asserted as *"no session clock appears on any of the 32 frames"* in both `04_SCREENSHOTS/V06/INDEX.md` and `V06_SOURCE_NOTES.md` §11d. First printed `est` in the corpus evidence; bears on `A-019` and `A-030`. The audio-scoped §10 claim (`EST` 0× spoken) is true and unaffected |
| E08 | Hindsight contamination | 0 | |
| E09 | Cherry-picking | 0 | |
| E10 | Incomplete homework | 1 | V01 |
| E11 | Missing provenance | 15 | **V09 (R1 ×1 — `M4`, `MINOR`, open item 76):** **fourteen frame cross-references at 15 or above are off by one across five files**, after `ff7b8bd` inserted a 27th frame at **position 15** and renumbered the `INDEX.md` table without renumbering the back-references. *"frame 17 error 2"* (×2, plus `A-065`) is the five-errors slide at **18**; *"frame 18"* for the 85% staircase is **19**; *"frames 19–21"* and *"frame 21"* are **20–22** and **22**; *"frames 22–23"* is **23–24**; `INDEX.md`'s own *"frame 22"* for the FXDD title bar is **23** and *"frames 22, 23 and 25"* is **23, 24 and 26**; `C-015`'s *"frame 16"* is **17**; the mastery report's *"frame 24"* is **25**. **Every content claim they support is correct** — the reviewer read the four load-bearing frames. **Charged because these ordinals are the provenance handle for every `PRINTED`-basis row**, and `Q-010`, in this same submission, establishes that *a real frame from the right lesson with an invented description* is the fabrication mode the project's screens are weakest against. **Required: renumber, or better, replace the ordinals with burned timecodes, which an insertion cannot invalidate.** The marker half of this dimension is meanwhile in excellent health — **312 citations re-derived by the reviewer, ZERO orphans** | **V08 (R1 ×1 — `M1`, `MINOR`, ✅ CLOSED — VERIFIED at R2 2026-08-13, open item 64):** *(R2: `Source A′` added and the V07 citation read at source — verbatim, ellipsis honest, `[00:28:31]`'s garble preserved; `GUEST` tag and §6c cross-reference resolve; `PROVISIONAL` unchanged. **R2 additionally RULED the presenter question the remediation deferred: the two presenters ARE different men, `HIGH` confidence, textual evidence only — R1's framing SUPPORTED.** Carried forward as documentation item 71, not as a defect.)* `C-009`'s **Source A** — the course's confirmation requirement — is sourced entirely to the V08 speaker's own reported speech (`[00:37:07]`–`[00:37:16]`, *"in **our** basic training, **we** do say…"*) thirty seconds before he calls it a myth, when **V07 `[00:28:02]`–`[00:28:31]` independently attests the same requirement** from a different lesson and a different equally-normative `GUEST` (*"you can only go by the second rail[road] tracks"*, recorded at `V07_SOURCE_NOTES.md` §6c as the direction question being answered by the confirmation candle). Citing it converts the record from *one speaker overriding his own report of a rule* into *a rule attested across two lessons, called a myth in the third*. **A new sub-class: omitted available corroboration, as distinct from an absent or wrong citation** — every citation V08 does make resolves (272 checked, 193 distinct, zero orphans, re-derived by the reviewer). Conclusion and `PROVISIONAL` disposition unaffected | **V07 (R1 ×1 — `M3` co-code, APPLIED 2026-08-13, pending R2 verification, open item 63):** `V07_MASTERY_REPORT.md` §D cites `[00:28:28]` for words that are at `[00:28:31]` — open item 7's class exactly (the neighbouring marker rather than the one the sentence's first words fall under). **The class is otherwise in excellent health and the de-escalation holds:** a mechanical marker-existence sweep over all seven V07 artifacts resolved **300 distinct citations**, with every non-resolving hit declared in advance by the student — `[00:21:35]` and `[00:34:50]` are screenshot timestamps, `[00:30:22]` and `[00:38:19]` are labelled **V04** markers. The transcript header carries its own pre-submission sweep block, which is V05 R2's `M11` discipline applied **before** review rather than after | **V05 (R1B ×1 — `M11`, APPLIED 2026-08-11, pending R3 verification, open item 51):** `A-042` cites `[01:01:39]`, not a marker; the words are at `[00:57:39]`. **Third member of one displaced cluster** — all three V05 citation defects map `00:57:3x` → `01:0x:3x`, so `M1`'s fix closed two thirds of a single defect. A mechanical marker-existence sweep is owed with the fix. **V05 (R1 ×2 — `M1`, `M2`, both ✅ CLOSED — VERIFIED at R2 2026-08-11, open items 41–42):** the *"I use E and I use the box"* quote cited at `[01:07:36]` in `V05_SOURCE_NOTES.md` and at `[01:01:35]` in `A-043` when it is at `[00:57:35]`–`[00:57:36]` — **two different wrong timestamps for one quote, neither a marker**; and `A-039`'s extension row citing `[00:36:03]` where the words are at `[00:36:05]`. **The de-escalation HOLDS**: 356 V05 citations were checked and 354 resolve, with 92 marker-cited quote fragments re-matched verbatim (90 exact). Two isolated instances, not a recurrence of the class. V01 (R1 ×1, R2 ×4, R3 ×4) — 8 closed at R3, 1 carried (open item 7). **DE-ESCALATED at V04 R1** — absent for a third consecutive lesson: V04's 487 cited markers were independently re-checked and **487 resolve** (V04 `M3` is a wrong *ambiguity-record* pointer, co-coded `E20`, not a wrong timestamp) |
| E12 | Ambiguity treated as rule | 0 | |
| E13 | Contradiction ignored | 1 | V01 |
| E14 | Outcome confused with correctness | 0 | |
| E15 | Machine assumption introduced prematurely | 0 | |
| E16 | Terminology drift | 0 | |
| E17 | Missing negative examples | 0 | |
| E18 | Invalid manual-backtest procedure | 0 | |
| E19 | Data/timeframe inconsistency | 4 | **V09 (R1 ×1 — `M3`, `MINOR`, open item 75):** `V09_TRANSCRIPT.md`'s COVERAGE block states *"Next largest 10 s, **four times**"* and lists four markers. **Re-measured with the block's own stated method there are SEVEN** — `[00:02:38]`, `[00:03:23]`, `[00:19:18]`, `[00:23:05]`, `[00:45:41]`, `[00:49:35]`, `[00:49:47]`. **Every other assertion in the block reproduces exactly** (721/718 markers, zero decreasing transitions, three same-second pairs at the named markers, 11 s twice at the named markers), which is why this is one cell and not the block. **Charged because the block declares itself MEASURED and invites the check, and because V03 R1 charged this same block in this same file family for a false property of the timestamps** — V09's block corrects V03's error, explicitly declining to claim strict monotonicity, and then introduces a new one two sentences later | **V08 (R1 ×1 — `M3`, `MINOR`, ✅ CLOSED — VERIFIED at R2 2026-08-13, open item 66):** *(R2: the burned-in timecode was re-read FROM THE PIXELS at 20× magnification — **`43:04`** — rather than taken on the remediation's word; file renamed with the blob preserved at 100 % similarity; **all four** references updated and an independent repo sweep confirms **no fifth**; the 0.25 s `ceil()` residual re-derived across all 26 frames and correctly resolved as `> ceil(runtime)`.)* `04_SCREENSHOTS/V08/V08_00-43-10_end-card-innermost-stage-unanswered.png` and `INDEX.md` row 26 both assert **`00:43:10`** on a recording measured at **00:43:03**; the frame's own burned-in player timecode reads **`43:04`**. The frame is genuine (the post-playback end card, `replay` button visible) and the content claim built on it — the literal `?` at the centre of the ring diagram — is fully confirmed by the reviewer reading the image. **Charged because `Q-009`, in this same submission, proposes "any timestamp exceeding the lesson's runtime" as its FIRST cheap fabrication screen for V09–V21, and V08's own screenshot set trips it.** Label-only defect; no conclusion affected | V02 (R1 ×1 as a co-code with `E06` — closed at R2; R2 ×1 — day boundary off by one bar, open); V03 (R1 ×1 — ADR figures not reproducible from committed data, M1 — **✅ CLOSED at R2 2026-08-10**: all twenty daily ranges and all four ADR figures re-derived exactly from the raw JSON under the stated 21:00-UTC convention); V04 (R1 ×1 — `M1`, **✅ CLOSED — VERIFIED at R2 2026-08-11** — partial 12-bar week-open 4h bar diagnosed and the slice corrected to 476 bars; 474/480 → 476/480; `bars_15m_in_4h_bar_0` and `verify_reconstruction.py` committed: USDCHF's 15-minute series is mis-sliced at a partial week-open bar, and the 27/30 reconstruction symptom was attributed to ±0.4 pip harvest noise when bar 0's open differs by **28.1 pips**. No conclusion changes; the 4h data is clean at 116/116) |
| E20 | Other | 40 | **V10 (R1 x4 - `M1`-`M4`, all `MINOR`, open items 91-94):** `M1` **an open-item identifier collision** - `video/v10` allocated items 81-85 while integration concurrently allocated 81-83 to V09 R2; renumbered 86-90 at merge-back, **and the policy half is a gap in `D-038a`**, whose merge-safety evidence checked `A-`/`C-`/`Q-` identifier sets but **not `REVIEW_INDEX` open-item numbers** - the one series in its evidence-ledger list that is not mergeable by construction. `M2` **a census undercount** - `A-078`/`C-017` say six spoken renderings and *"four of six"* name the blue tracer; `[01:00:20]` is a seventh and names the tracer, so the true figure is **five of seven**, which **widens the spoken majority and strengthens `C-017`**. `M3` **an overstated absence** - §15's *"no hour is ever stated"* is falsified by four incidental clock times; the intended and true claim is that no **session-boundary** hour is stated, which `A-076`'s parallel sentence already scopes correctly. `M4` **an unapplied self-caution** - `C-016` rests on two ASR-rendered, unprinted numerals and does not cite the same transcript's TRANSCRIPTION NOTE 1 on numeric wobble, which is **a further reason for `UNRESOLVED`**, not a weakening of it. **All four are edits; none moves a conclusion, and three of the four correct the record in the direction that strengthens the finding it belongs to.** | **V09 (R1 ×2 — `M2`, `M6`, both `MINOR`, open items 74 and 78):** `M2` — **a pre-registered decision rule was not applied and the clause was not disclosed.** `PT-035` §6's table for the claim under test reads *"INDETERMINATE — cells disagree across the 5%/10% boundaries, **or `N3` fails**"*, and §7b is headed *"WHAT WOULD MAKE THIS TEST VOID"*. **`N3` failed.** `BT_V09_0001` identifies the runner's failure to encode §7b for the **clustering** arm, voids that arm, and scores `P4` VOID against a runner that printed `RIGHT` — and then applies `v1`'s verdict word for the **empirical** arm, whose identical gate `run_pt035.py` lines 356–366 also do not encode. The string `INDETERMINATE` appears nowhere in `BT_V09_0001`, the mastery report or `LOG.md`. **`MINOR` because the conclusion does not rest on the measurement**: `CONTRADICTED AS STATED` follows from §2c's closed form, committed before the corpus was read, and **the reviewer re-derived it from first principles** — 99.93% at p=0.50, 54.13% at p=0.73, 84.19% required. **Required: report the empirical arm as `INDETERMINATE` and carry the verdict on the closed form alone; do NOT edit `PT-035` or the runner** (`COMMON_PROTOCOL.md` §9 rule 7); the owed successor must encode both gates **in code**. `M6` — **omitted available corroboration, the V08 R1 `M1` sub-class:** the capture-bug escalation states `mouse.click(512, 300)` is *"the coordinate that starts the Camtasia player on **V01–V08**"*. It does not. `04_SCREENSHOTS/V08/INDEX.md`, on a branch this session merged from, records *"the first 529-frame sweep produced one distinct image, 529 times… misses the play target on this file — V08's splash centres its play button at approximately `(512, 325)`"* — same coordinate, same corrected coordinate, one lesson earlier. **The bug itself is CONFIRMED and is broader than claimed:** the reviewer parsed the stage `RECT` from all 21 source files and **V08, V09 and V21 declare a 1280×738 stage against the other 18 at 1024×786**, so at the recipe's 1024×786 viewport those three letterbox and every calibrated coordinate is displaced — measured on the committed pixels. The disposition (a `D-038a` policy edit owed on integration) was **correct**, and the reviewer made the fix | **V07 (R2 ×1 — `M1` co-code, `MINOR`, open item 70):** co-coded here for the *intra-file disagreement* limb, which is the V05 `M4` class and the exact shape R1's own `M1` was charged for: `V07_SOURCE_NOTES.md` §10 measures `mayo` at **0** and states that the audio only garbles it to *mail*/*male*, while **§9a of the same file quotes the presenter saying it** at `[00:27:24]` — one file, two contradictory records of the same object, **recurring in the same file that item 61 had just corrected for the same fault**. Primary charge and full detail on the `E01` row. **The count class itself is NOT recurring:** items 61 and 62 were re-derived by two independent methods and are ✅ **CLOSED — VERIFIED at R2 2026-08-13** (`level` 53 + `levels` 3 = 56 over a body `wc -w` puts at exactly the stated 7,436 words; *"the peak"* 5, enumerated at the five listed markers, with no sixth use behind a different article). **The sixth and seventh instances of the count class are discharged** | **V08 (R1 ×1 — `M2`, `MINOR`, pre-registration-completeness class, ✅ CLOSED — VERIFIED at R2 2026-08-13, open item 65):** *(R2: `entry_for()` and `precompute_close_entries()` **read** — both documented descriptions **exact**; `PT-034` **byte-unchanged**, one commit ever and an empty diff; `BACKTEST_EVIDENCE_STANDARD.md` §2.1a binds the requirement forward and goes **beyond** R1's ask by naming the bias it guards and setting a `MINOR E20` enforcement floor.)* `PT-034` §4's `N1` table holds constant *"instrument, day, eligible bars, target, stop, horizon rule, direction, and `n`"* and randomizes *"the entry bar"* — **the entry PRICE is neither, and the runner fixes it to the chosen bar's CLOSE** (`precompute_close_entries()`), while the rule arm enters at an extreme-anchored price. A parameter that materially defines the null was settled in code rather than in the pre-registration. **Mitigated on three counts and therefore `MINOR`:** the runner was committed at `e3a8e66` **before** it was executed at `1d206ab` and has exactly one commit, so nothing was chosen after seeing a result; the close is the natural neutral choice for a bar with no extreme to anchor to; and the null landed at **0.2424–0.2450** against the closed-form 3:1 break-even of **0.2500**, which is what an unbiased matched-random entry must return. **Forward requirement only — `PT-034` must NOT be edited** (`COMMON_PROTOCOL.md` §9 rule 7) | **V07 (R1 ×2 — `M1`, `M2`, both `MINOR`, count class, ✅ BOTH CLOSED — VERIFIED at R2 2026-08-13, open items 61–62):** `V07_SOURCE_NOTES.md` §10's table of "measured negatives" carries two wrong counts. `M1` — the *level* row states **26 uses**; the true count is **56** (`level` 53 + `levels` 3), the `level <N>` compound is 35, and entries containing the token are 44, so 26 matches nothing — **and §5 of the same file states 56 correctly**, so one file holds a right record and a wrong record for the same object fourteen sections apart (the V05 `M4` intra-file-disagreement class layered on the count class). `M2` — the *"the peak"* row states **4×** and then lists **five** markers; the true count is **5**, and the listed markers are all correct, so the row is internally inconsistent on its face. **Both conclusions are unaffected and, in `M1`'s case, understated.** Charged because §10's own preamble states the counts are given *"so a reviewer can falsify them cheaply"* — the invitation was taken and two cells falsified. **Sixth and seventh instances of the count class (open items 15, 39, 48, 58, 59) — it is now the single most durable defect class in the project and is well past `REVIEW_PROTOCOL.md` §7's threshold. Raise at `CUMULATIVE_25.md` together with V06 R2 `M5`'s one-ledger-per-lesson proposal, which would fix both classes at once** | **V06 (R2 ×1 — `M5`, ✅ CLOSED IN-ROUND at `4c89db1`):** `V06_SOURCE_NOTES.md` §11b's R-label cell carried **five wrong values of eight claims** (21.1→31.1; a 24.3 attributed to `V06_00-15-49`, which carries 80.6/41.5; 47.3→67.3; 38.8→80.6; 26.9→28.9), disagreeing with `04_SCREENSHOTS/V06/INDEX.md` and the `A-018` register row (both correct) on the same frames — the V05 R1B `M9` evidence-value class plus the V05 `M4` cross-file-disagreement class in one finding. Surfaced by R1 item 57's required frame sweep; corrected with superseded text retained; `A-018`'s negative conclusion survives the corrected value set. **Third consecutive round with a small-printed-value defect — raise the one-ledger-per-lesson rule at `CUMULATIVE_25.md`** | **V06 (R1 ×3 — `M2`, `M3`, `M4`, all `MINOR`, open items 58–60):** `M2` the transcript header's *"Steve occurs 25 times, 23 + 2"* is irreproducible — 26 tokens measured, and a **third** read-aloud instance (`[01:11:39]`, inside the Isubio quotation) is unclassified; speaker-identification conclusion unaffected and strengthened. **Token/verbatim-count class again (open items 15, 39, 48) — already at the escalation threshold, raise at `CUMULATIVE_25.md`.** `M3` the *already-corrected* `Asian`/`Asia` row in `V06_SOURCE_NOTES.md` §10 is still miscounted: `Asia` is 2× (`[00:50:25]`, `[01:09:55]`), not 1×. Same class. `M4` the `D-033` propagation (`612f431`, *"every place they change"*) did not touch the five live `D-025` fences in the V06 lesson artifacts themselves (transcript header, source notes, interpretation, homework, screenshot index) — each still states superseded prohibitions in present tense; status-staleness class, open item 14. | **V05 (R1B ×2 — `M7`, `M9`, both APPLIED 2026-08-11, pending R3 verification, open items 47, 49):** `M7` the V05 contradiction check that was actually run against `C-004` is named `C-003` at four sites including `CONTRADICTIONS.md`'s **STATUS block** — the record named contains no V05 text at all, and this retires R1's `N5` claim that all four status blocks were current; `M9` four printed `R =` labels unrecorded in curated frame 26, leaving `A-018`'s *"V05 adds four more labels"* an undercount of at least half — **the same frame and the same class as `M6`**. **V05 (R1 ×3 — `M4`, `M5`, `M6`, all ✅ CLOSED — VERIFIED at R2 2026-08-11, open items 44–46):** `M4` three V05 files disagreeing about V05's own evidence order, with `INDEX.md` disclosing the deviation correctly and `V05_INTERPRETATION.md` line 12 claiming the opposite — **a new sub-class: not stale text, but two files written in the same session asserting contrary things about that session's own process**; `M5` `A-039`'s *"V05 is the next candidate"* pointer left stale by the lesson that answered it — **eighth instance of the status-staleness class (open item 14), and the only staleness this round**; `M6` an unrecorded oscillator sub-panel in curated frame 26, the V04 `M6` class exactly. **Counterweight worth recording: V05 is the FIRST round in which all four STATUS blocks were current** (`AUTOMATION_AMBIGUITIES.md`, `CONTRADICTIONS.md`, `COURSE_PROGRESS.md`, `REVIEW_INDEX.md`), verified by re-deriving each against its own file's contents. Open item 14 has failed in six previous rounds; this one is clean, and it was achieved **without** the proposed `validate_project.py` guard existing. V01 (R1 ×6, R2 ×2, R3 ×1) — all closed at R3; V02 (R1 ×4) — closed at R2; V02 (R2 ×2) — open; V03 (R1 ×1 — transcript coverage block overclaims "strictly monotonic, no duplicates", M2 — **✅ CLOSED at R3 2026-08-10**: applied to the `PROVENANCE` I-008 criterion at `683a12a` and to the `COVERAGE` block at `492bb11`; both blocks now assert the same true proposition, re-derived component by component at R3. Carried as R2 M2′, never double-counted — one occurrence, remediated in two commits. The **monotonicity class is now empty project-wide**: V01 makes no such claim, V02 is genuinely strict (1,026 / 1,026), V04 states the weaker true property) | **V04 (R1 ×5 — all ✅ CLOSED — VERIFIED at R2 2026-08-11):** `M3` two ambiguity cross-references in `V04_TRANSCRIPT.md` pointing at `A-037`/`A-038` where the register holds `A-031`/`A-030` (co-codes `E11`); `M4` stale "26 frames" (27 exist) and stale `VISUAL_INDEX` filename — **sixth and seventh instances of the status-staleness class, open item 14**; `M5` homework validation 1's 569/549/20 continuity figures not reproducible from committed data (same promise as open item 13); `M6` a visible `Traders Dynamic Index Visual` panel in curated frames 21 and 22, unrecorded in `INDEX.md` and in `A-039`; `M7` four `MASTERY_STANDARD.md` quality-control boxes unchecked and undeclared (concept library, positive/negative/borderline examples) — **shared with V02 and V03, raise at `CUMULATIVE_25.md`** **V04 (R2 ×1 — `m1`, OPEN, non-blocking, open item 34):** the *"§3.3 windows are identical"* justification written during the R1 remediation is true for the high-side window and false for the low-side one; the descriptor row it justifies is genuinely unchanged (1/1/1/1, recomputed at R2). **Eighth instance of the narrative-about-a-check class R1's `N5` named** |

**Escalation rule:** any code reaching 3 occurrences is a systematic weakness.
Note it in the next cumulative review and consider whether the student protocol
itself needs strengthening — not just the individual lesson.

### ESCALATION TRIGGERED 2026-08-10 (R2)

Three codes have reached or passed the threshold on a single lesson.

- **`E11` — missing provenance (5).** The substantive defect. Across two rounds,
  eight statements were found citing a timestamp that does not carry their words:
  `S19`, `S27`-collision ×3 more locations, `X2`, `X3`, `S29`, and H5 in three
  files including an `ACTIVE` decision record. **No quotation was fabricated** — in
  every case the words exist in the recording and are quoted accurately; only the
  citation is off, typically by 10–40 s and usually because the passage start was
  cited instead of the sentence. This is the same reflex that produced `Q-001`,
  caught at the cheap end. **Protocol implication:** `STUDY_PROTOCOL.md` should
  require that a quoted sentence cite the marker its *first words* fall under, and
  that passage-level citation be written as a range (`[a]`–`[b]`), never as a bare
  start. Raise at the 25% cumulative review.
- **`E20` — other (8).** Almost entirely stale status text: files asserting a state
  of the world that was true when written and is now false. Same class as `Q-001`
  in miniature. **Protocol implication:** any file carrying a `STATUS` block or a
  "none / empty / not captured" assertion should be re-read at the close of every
  session that changes what it describes.
- **`E02` — unsupported generalization (3).** All three concern the blue/red boxes.
  Two of the three were *introduced during remediation of the first*, which is
  itself the lesson: a correction is new work and carries the same generalization
  risk as the original.

### ESCALATION UPDATE 2026-08-10 (R3)

All three escalated codes are **closed for V01**. The counts above are cumulative and are
not reset — a closed finding still happened.

- **`E11` rose from 5 to 9 at R3**, eight of them closed. R3 found three further misdatings of
  the same class while applying R2's action 4: the instructor's day-count acknowledgement
  cited at `[00:36:17]` in six places when it is at `[00:36:13]`–`[00:36:15]`; "trap move"
  first-use cited at `[00:33:33]`, which is neither a marker nor a passage about trap
  moves; and `S33` cited at `[00:45:40]` when the four-item recap is at `[00:45:44]`. All
  corrected. **Every V01 quotation now resolves to a marker carrying its words.**
- **Deliberately not corrected, and carried as open item 7:** seven cited timestamps in
  V01 files are not transcript markers at all — `[00:25:51]`, `[00:30:44]`, `[00:35:38]`,
  `[00:38:02]`, `[00:39:43]`, `[00:40:26]` (and `[00:33:33]`, which *was* corrected
  because it also pointed at the wrong content). The remaining six each land inside the
  passage they cite, 2–4 s past the marker, and resolve to the right words. Fixing them is
  precisely the `STUDY_PROTOCOL.md` amendment proposed below and deferred to the 25%
  review; applying an unadopted rule retroactively was judged worse than leaving six
  resolvable approximations. **This is the strongest concrete argument for adopting the
  amendment**, and it should be quoted at `CUMULATIVE_25.md`.
- **`E20` rose to 9.** `AUTOMATION_AMBIGUITIES.md` and `CONTRADICTIONS.md` status blocks
  had gone stale **a third time** — corrected at R1 finding 6b, then invalidated again by
  the V02 pass adding `A-019`–`A-028` and `C-003`–`C-004`. The R2 protocol implication
  ("any file carrying a `STATUS` block should be re-read at the close of every session
  that changes what it describes") is not a theoretical concern; it has now failed three
  times on the same two blocks. **Recommend promoting it from a suggestion to a
  `STUDY_PROTOCOL.md` session-close requirement at the 25% review**, alongside the
  citation amendment.

### ESCALATION UPDATE 2026-08-10 (V02 R1)

- **`E11` — missing provenance — did NOT recur.** This is the headline. It was V01's
  dominant defect across three rounds (9 occurrences) and prompted the proposed
  `STUDY_PROTOCOL.md` citation amendment. V02's R1 sampled ~20 cited timestamps against
  the transcript, weighted toward numbers and load-bearing claims, and **every one
  resolved to a marker carrying its words.** The amendment is still worth adopting at the
  25% review, but the behaviour it targets has already improved without it.
- **`E20` — other — rose from 9 to 13, four of them open on V02.** Same class as before:
  status text asserting a state of the world that has gone stale, plus occurrence counts
  that do not match the artifact they count. Two are especially instructive. The
  `CONTRADICTIONS.md` STATUS block is now wrong for the **fourth** time — and this time
  the error was *introduced by the R3 edit that was correcting that same block*, which is
  the R2 lesson repeating ("a correction is new work and carries the same risk as the
  original"). The `COURSE_PROGRESS.md` PHASE STATUS row contradicts the same file's own
  SUMMARY. **This code has now failed on status blocks in four separate rounds and is the
  project's most persistent weakness.** Promote the session-close re-read from suggestion
  to requirement at the 25% review, and consider a mechanical check in
  `validate_project.py` — every one of these is arithmetic over the file's own contents
  and could be verified automatically rather than by eye.
- **`E06` — false positive (1), new.** V02's homework markup states price levels and days
  that its own committed chart does not show, and draws a confirmation of the C-001 day
  count from them. Novel class for this project: the previous defects were all about
  *citing sources*; this is the first about *reading price*. **Protocol implication:**
  chart-derived claims need the same verifiability standard as transcript-derived ones.
  A markup keyed to dates and prices should be reproducible from the image by someone
  who was not there — which means naming how the day boundaries were established, not
  estimating them from axis ticks.
- **`E01` — source misquote (1), new.** Minor in effect — both repairs are almost
  certainly correct — but it is the first time this project has smoothed ASR garble
  inside quotation marks, and the file it happened in explicitly promises not to.

---

## SEVERITY TOTALS

Last fully reconciled at V02 R1; the pre-V03 rows below are carried as found and were
not re-audited by the V03 round (reconciling them against V02 R2/R3 is folded into
open item 14's arithmetic-check work item). **V03 R1's delta is authoritative:
+3 MINOR (M1–M3, all open), +5 NOTE (N1, N2, N3, N5 closed as observations; N4 —
the three-lesson manual-backtest debt — carried open).** The V02 R1 open MAJOR
recorded below this table closed at R2/R3.

**V03 R2's delta:** +0 MINOR, +5 NOTE (all closed as observations). R2 raised no new
finding — its single minor, M2′, is R1's M2 carried forward as incompletely remediated,
not a fresh defect, and is not double-counted. **2 of V03 R1's 3 minors close** (M1, M3),
leaving MINOR open at 6.

**V03 R3's delta:** +0 MINOR, +4 NOTE (N1 the missing log entry for `492bb11`, N2 the
V04 marker-scan counting trap, N3 the now-stale pointer in `V04_TRANSCRIPT.md` line 30,
N6 the clean validator run — all closed as observations; R3's N4 and N5 restate carried
items and are **not** double-counted). R3 raised no new finding of any severity.
**V03 R1's last remaining minor closes** (M2, via M2′), leaving MINOR open at 5 — none of
them V03's. All of V03's own findings across three rounds are now closed.

**V04 R1's delta:** **+7 MINOR (M1–M7, all open), +5 NOTE** (N3, N4, N5 closed as
observations; **N1 — re-disposition dimensions B and C as `DEFERRED` under `D-019` — carried
open as a required action**; N2 restates the carried manual-backtest debt and is **not**
double-counted). **0 CRITICAL, 0 MAJOR — the V05 gate opens under D-024.**

**V04 R2's delta:** **+1 MINOR (`m1`, open item 34 — non-blocking and deferred by design),
+3 NOTE** (all closed as observations: N1 the accuracy of the remediation's own self-report,
N2 the stale `CONCEPT_INDEX.md` STATUS block — **not charged against V04**, it belongs with
open item 14 and the concept-library debt, N3 the statement of what R2 did not re-audit under
`REVIEW_PROTOCOL.md` §4). **All seven of V04 R1's minors close, and `N1` closes as a required
action discharged.** 0 CRITICAL, 0 MAJOR. **V04 PASSES and is `COMPLETE`.**

**V05 R1's delta:** **+6 MINOR (`M1`–`M6`, all open), +5 NOTE** (`N1` the withdrawn
extensions finding, `N2` the substituting bracket, `N3` the inclusive-endpoint window figures,
`N5` the first clean status-block round — all closed as observations; **`N4` restates the
now five-lesson-deep manual-backtest debt and is NOT double-counted**). Plus one **NOTE-level
required action** on dimension B's disposition, carried in the same class as V04 R1's `N1`.
**0 CRITICAL, 0 MAJOR — the V06 gate opens under D-024.**

**V05 R1B's delta:** **+4 MINOR (`m1`–`m4`), +4 NOTE** (`n1` the third cluster citation —
**escalated to MINOR at R2 and counted there, not here**, so it is not double-counted; `n2`
the `E11` re-escalation, `n3` the `A-043` affirmation on a narrower basis, `n4` the mastery
report's honesty — all closed as observations). Raised concurrently with R1 against the same
tree; **not double-counted against R1's six, which are distinct findings.** The R1-round total
is therefore **10 MINOR**. **0 CRITICAL, 0 MAJOR.**

**V05 R2's delta:** **+1 MINOR (`M11`, R1B's `n1` escalated from NOTE), +4 NOTE** (`N1` the
`E11` class re-escalation, `N2` the two owner-decision items confirmed accurately logged and
deliberately unresolved, `N3` the dimension-B re-disposition still correctly blocked, `N4` the
second review-layer concurrency event — all closed as observations). **`M7`–`M10` are R1B's
`m1`–`m4` adopted, NOT new findings, and are counted once at R1B.** **Closed this round: R1's
`M1`–`M6` (all six verified against source) and open item 39.** 0 CRITICAL, 0 MAJOR — the V06
gate stays open; **V05 does not reach `COMPLETE`.**

**V05 R3's delta (for the table below):** R3 raised nothing and verified `M7`–`M11`
(open items 47–51) closed — MINOR open 11 → 6. V05 is `COMPLETE`.

**V06 R1's delta:** **+1 MAJOR (`M1`, open item 57 — the frame-26 elided `3:45am /
9:45am est.` line and the false "no session clock on any frame" claim, `E07`+`E11`),
+3 MINOR (`M2`–`M4`, open items 58–60), +3 NOTE** (`N1` the PT-023 `T1` convention,
`N2` the arm-B label correctly quarantined under `D-031`, `N3` the student's
self-audit tooling — all closed as observations). **Dimension B is blocked by `D-030`
and is EXCLUDED from pass/fail per the owner's directive — documented in
`V06_REVIEW_R1.md` §B/§14, not scored, and not the cause of the `REVISE`.**
**1 MAJOR — the V07 gate stays CLOSED under D-024** until item 57 is remediated and
re-reviewed. First round audited under `D-033`/`D-034`/`D-035`; first exercise of
`REVIEW_PROTOCOL.md` §6.G checks 15–20 against a run backtest, all clean.

**V06 R2's delta:** **+1 MINOR (`M5`, found by the item-57 sweep, ✅ CLOSED IN-ROUND),
+1 NOTE (`N1`, closed as an observation — the sweep design validated).** **Closed this
round: R1's `M1` (the MAJOR) and `M2`–`M4`, all verified against primary sources**
(frames re-read at 2×–4×, transcript re-measured). Same-session remediation and
re-review were owner-directed and disclosed; `CUMULATIVE_25.md` re-samples this round.
**0 CRITICAL, 0 MAJOR — V06 PASSES at R2 and is `COMPLETE`; the V07 gate OPENS.**

**V07 R1's delta:** **+3 MINOR (`M1`, `M2` — `E20` count class, `M3` — `E01`+`E11`; all
open as items 61–63), +4 NOTE** (`N1` the `I-009` git recurrence — audited independently and
**closed as an observation: zero damage**; `N2` §H's stale citation figure — closed, explained
by §9b being added after the sweep ran; `N3` the `R11` probe failure — closed, verified genuine
and correctly written up; `N4` the dimension-B vocabulary gap — **carried OPEN**, it restates
open item 36 for the third lesson and is counted once here as this round's escalation).
**0 CRITICAL, 0 MAJOR — the V08 gate OPENS under `D-024` with three minors deferred and owed.**
**Dimension B was scored rather than carved out** (no owner directive this round) and returned
**NOT SATISFIED with no severity charge** — the cause is the source material, and charging it
would penalise the `D-030` discipline the project mandates. See `V07_REVIEW_R1.md` §14.

**V08 R1's delta:** **+3 MINOR (`M1` — `E11`, a new "omitted available corroboration"
sub-class; `M2` — `E20`, pre-registration completeness; `M3` — `E19`, a timecode past the
runtime; all open as items 64–66), +5 NOTE** (`N1` the branch/merge state and the `D-038`
ledger-location tension — **carried OPEN as item 68**, an owner decision and explicitly **not**
a student defect; `N2` `SOURCE_MANIFEST.md`'s STATUS column stale since V02 — closed as an
observation and **not charged to V08**, it is pre-existing project debt; `N3` the mastery
report's "186 marker citations" being **conservative rather than inflated** (272 measured, 193
distinct, all resolving) — closed; `N4` the dimension-B vocabulary gap — **carried OPEN**, it
restates open item 36 for the **fourth** lesson and is counted once here as this round's
escalation; `N5` the reviewer's own delta-tile / 267×51 measurement independently corroborating
`Q-009`'s mechanism from the source side — closed as an observation **in the student's favour**).
**0 CRITICAL, 0 MAJOR — the V09 gate OPENS under `D-024` with three minors deferred and owed.**
**Dimension B was scored rather than carved out** (no owner directive this round) and returned
**NOT SATISFIED with no severity charge**, on V07 R1's reasoning exactly. See
`V08_REVIEW_R1.md` §14.

**Recorded because it is a first for the project:** V08's backtest was **re-executed by the
reviewer and reproduced bit-for-bit** — `pt034_output.txt` byte-identical bar the absolute path,
`pt034_results.json` differing in the single field `runtime_s`, the `PT-033` cross-check
byte-identical, the comprehension probe byte-identical at 58/58, and the homework re-scored from
raw JSON with the reviewer's own code to the same 5/12 and 10/12. Pre-registration ordering was
verified in Git, **including that neither the pre-registration nor the runner was ever amended**.
No previous round has been verified to this depth, and it is the reason this round's confidence
is `HIGH` on a `REVISE`.

**V07 R2's delta:** **+1 MINOR (`M1` — `E01` with co-code `E20`, open as item 70), +2 NOTE**
(`N1` the remediation's re-verification sweep is not reproducible — no script committed with
`98d893a` — closed as an observation and forwarded to `CUMULATIVE_25.md` as a candidate standing
rule, **not** charged as a required correction; `N2` the 239 / 238 / 167 gap between three sweeps
of the same corpus, with a line-wrap mechanism tested as a candidate — closed as an observation).
**Items 61 and 62 CLOSED — VERIFIED**, each re-derived from the transcript by two independent
methods; **item 63 PARTIALLY VERIFIED and left OPEN** — its §D half is closed, its §H half is
not. **The superseded-text convention was verified SATISFIED at all three remediation sites**;
no incorrect text was deleted anywhere in `98d893a`. **0 CRITICAL, 0 MAJOR — the V08 gate stays
OPEN, R1's `D-024` authorization undisturbed; V07 does NOT reach `COMPLETE`.** Dimension B
carried from R1 unchanged, and open item 36 is restated for the **fifth** lesson-round without
being counted again. See `V07_REVIEW_R2.md`.

**V07 R3's delta:** **+0 MINOR, +4 NOTE, all closed as observations.** **Items 70 and 63 CLOSED —
VERIFIED**, and with them V07's whole R1–R2 finding set is discharged. `N1` — four precision bounds
in `verify_quotes.py` found by mutation testing, including an allowlist `startswith` hole whose
docstring claims the opposite; **all four hand-searched and empty**, so the §H claim they support is
true independently of the tool; recorded, deliberately **not** charged. `N2` — the bracket-token
item **RULED, not deferred a second time**: `DM[R] speaker[s]` is **not** a defect, because the
bracket is the visible signal whose *absence* is what R2 charged in instances (a)–(c), and
intra-word bracketing spans V01/V07/V08. `N3` — the possibly-overwritten-file alarm **investigated
across seven independent tests and dismissed**: no work was lost, `D-038` isolation not implicated,
with the honest caveat that an untracked file leaves no git trace so this is evidence of sole
authorship rather than proof of a negative. `N4` — the process gap that investigation exposed: the
concern was reported in session output but never written to `LOG.md`, so record the working-tree
state **observed at start**, not only the one produced at commit. **0 CRITICAL, 0 MAJOR, 0 MINOR —
V07 PASSES at R3 and is `COMPLETE`; the V08 gate is undisturbed.** Dimension B carried unchanged
from R1/R2 and open item 36 restated for the **sixth** lesson-round without being counted again —
it is not a gate and it did not hold V07. See `V07_REVIEW_R3.md`.

**V08 R2's delta:** **+0 MINOR, +3 NOTE.** **Items 64, 65 and 66 CLOSED — VERIFIED**, discharging
V08's whole R1 finding set. Every one was re-derived from primary sources before the remediation's
account was accepted: the V07 citation **read at source** (verbatim, honest ellipsis, and the
`[00:28:31]` garble *"**in** your flashcard"* **preserved** — the exact class V07's item 63 was
charged for, avoided in the one file where smoothing would have been easiest); `entry_for()` and
`precompute_close_entries()` **read**, both documented descriptions **exact**; `PT-034`
**byte-unchanged**, one commit ever and an empty diff; and the end-card timecode **re-read from the
pixels** at 20× magnification — **`43:04`**. An independent sweep found **no fifth** reference to the
old string, and the disclosed 0.25 s `ceil()` residual was re-derived across all 26 frames and is
correctly characterised. `N1` — **the presenter-identity question is RULED, not deferred a second
time: V07's and V08's presenters are DIFFERENT MEN, `HIGH` confidence, on textual evidence only**
(V08 names **Ray** ×3 third-person, at `[00:00:49]` as the man who had been taking the questions;
`Ray` occurs **zero** times in V07 and V06; V07 is the Q&A part and V08 reads none; independently,
V07's presenter defers to **Jim** ×3 and disclaims at `[00:07:43]` the high-of-day skill V08's second
half teaches under a deck titled *"Jim's Journey"*). **Cross-file F0 comparison was available and
deliberately NOT used** — `COURSE_PROGRESS.md` V06 GATE item (a) prohibits it. R1's *"a different
guest presenter"* is **SUPPORTED**, and the remediation's refusal to write it unverified was **still
the right act**; carried as item 71, a documentation follow-up **not owed as a defect**. `N2` — a
**concurrency incident**: a concurrent session moved the shared main working directory onto
`review/v09`, a tree predating both the V07 R2/R3 merge and the entire V08 remediation, partway
through this review. **Detected, not missed**; every post-switch read was re-run in a dedicated
worktree and two stale reads discarded. Charged to **process**, carried as item 72, **not
attributable to V08**. `N3` — a bracketed ASR expansion (*"second rail[road] tracks"*) that a
mechanical verbatim sweep will flag as a non-match; **already ruled not-a-defect at V07 R3**,
recorded only so a future sweep does not re-charge a closed question. **0 CRITICAL, 0 MAJOR, 0
MINOR — V08 PASSES at R2 and is `COMPLETE`; the V09 gate was already OPEN under `D-024` and is
unaffected.** Dimension B carried from R1 unchanged and open item 36 restated for the **fifth**
lesson-round without being counted again. See `V08_REVIEW_R2.md`.

**V10 R1's delta:** **+4 MINOR (`M1`-`M4`, open items 91-94), +7 NOTE** (`N1` the imprecise
wording of speaker strand 2 - closed as an observation, **the determination itself UPHELD at HIGH
confidence on five verified strands plus four the reviewer added**; `N2` the omitted
`[00:01:33]` *"trailing stops"* deferral, which **strengthens** §15's no-stop-loss finding -
closed as a recommended addition; `N3` that arm B is **worse** for `M2` than the headlined arm A
(Friday 5th of 5, not 4th), i.e. the submission headlined the weaker result against the claim -
closed in the student's favour; `N4` the runner's pre-execution crash-fix **verified against the
diff** and its `COMMON_PROTOCOL.md` §9 rule 7 classification **upheld** - closed; `N5` open item
80's censoring bias **designed out AND enforced as a hard assert**, confirming R1's narrowed
scope without closing item 80 - carried as item 90; `N6` the `SWF_CAPTURE_RECIPE.md` §10 defect
**confirmed real, V10's own capture confirmed UNHARMED**, and **FIXED by this reviewer on the
integration branch** - item 87 `CLOSED`; `N7` the **stale PROGRESS TABLE**, which is **systemic across five lessons and therefore NOT charged as a fifth minor** - carried as item 96). **0 CRITICAL, 0 MAJOR - the V11 gate OPENS under
`D-024` with four minors deferred and owed.** **Dimension B was scored rather than carved out**
and returned **NOT SATISFIED with no severity charge, for the sixth consecutive lesson**, on V07
R1's reasoning exactly; **open item 36 is escalated a sixth time and still needs an owner
ruling.** **All four minors are documentation or register hygiene: not one moves a measurement,
a classification, a disposition or a rule.** `M1` is the only one with procedural teeth, and half
of it is a gap in `D-038a` rather than in the student's work.

**Every quantitative claim in this round was RE-DERIVED, not read.** `PT-036`'s `M1`, `M2a`,
`N2`, `N3`, `O2` and `O4` were recomputed on both `D-031` arms by a reviewer-written script
importing no project module: **every figure reproduced exactly** (0/180 in band; median 243.8;
600 at the 99.44th percentile; overshoot 3.28x; 4/180 on the pip-vs-point rescue; 7.30% / 5.62%
joint; nulls 7.12% / 7.00%; Thursday 13.41%; -6.10 / -8.91 pp; 40.45% at median 107.0;
`censored = 0`). `Q-011`'s `diff` was re-run and **extended library-wide: three distinct
`RULES.md` documents across 21 lessons, thirteen of them - including V10 - the same file
re-badged.** Four of ten H2 anchors were re-derived from the raw corpus and matched on price and
week range. Four frames, including both rules slides and the 25-75 slide, were **opened and read
as images**: nine printed rules and two load-bearing slide texts transcribed with **zero
substitutions**.

*(V10 R1 fix-round arithmetic, 2026-08-13: CRITICAL, MAJOR, MINOR and NOTE **totals** unchanged —
no new finding was charged. **The delta is −4 open MINOR / +4 closed MINOR** (items 91's student
half, 92, 93, 94); NOTE unchanged. **ABSOLUTE FIGURES ARE DELIBERATELY NOT QUOTED HERE, and the
reason is a defect this round found and is disclosing rather than papering over: the SEVERITY
TOTALS table above has not been reconciled since V09 R1** — it still reads `MINOR 57 / 12 open /
45 closed`, which predates **V09 R2's +3** and **V10 R1's +4**, and **neither of those rounds
posted an arithmetic paragraph at all**, breaking a convention every round from V07 R1 onward had
kept. Quoting a total off a stale table would manufacture a number rather than record one.
**A reconciliation sweep is owed and belongs with open item 96's bookkeeping-decay work**, which
is the same class one file over. **⚠ THE FOUR ARE `CLOSED — SELF-VERIFIED AT OWNER DIRECTION`, NOT
`CLOSED — VERIFIED`** — one session both fixed and verified them on the owner's explicit
authorisation, and this round does **not** satisfy `D-003`. They are counted in the *closed* column
because they are applied and discharged; **the status string, not the column, is what records that
no independent session checked them.** Read the notice under the DECISION TABLE before relying on
any of the four. Item **91's policy half stays OPEN** and is not counted as closed; items 86, 88,
89, 95 and 96 are untouched. **V10 is `COMPLETE`, qualified.** The **V11 gate is CONFIRMED OPEN**
— it opened at R1 on 0 CRITICAL / 0 MAJOR under `D-024` and never depended on these four.
Dimension B and open item 36 are restated, **not re-counted**.)*

**V09 R1's delta:** **+6 MINOR (`M1`–`M6`, open items 73–78), +8 NOTE** (`N1` the branch and
merge state and the 11-commit divergence — closed as disclosure; `N2` the oscillator sub-panel,
which the reviewer **magnified and read** as `TDI  MMM  59.8444 66.7359 68.0841`, corroborating the
frame's contents while **upholding the student's refusal to transcribe it** and its conclusion that
it does **not** narrow `A-039` — closed **in the student's favour**; `N3` the **count class clean
for the first time in five rounds**, all seven citation counts re-derived and reconciling — closed;
`N4` the dimension-B vocabulary gap, **carried OPEN**, restating open item 36 for the **fifth**
lesson and counted once here as this round's escalation; `N5` the reviewer's own corroboration that
`PT-034`'s `N1` came in **below** its closed-form break-even in **all four cells** (0.2424–0.2450
against 0.2500), which is the censoring signature `PT-035` §3 names — **carried OPEN as item 80**;
`N6` the evidence-order deviation **NOT charged**; `N7` `C-014`'s disposition upheld as filed;
`N8` **a process collision this round CAUSED and discloses against itself** — item 72's shared-
working-directory switch was this session, and this round did **not** use a dedicated worktree,
**carried OPEN**). **0 CRITICAL, 0 MAJOR — the V10 gate OPENS under `D-024` with six minors
deferred and owed.** **Dimension B was scored rather than carved out** (no owner directive this
round) and returned **NOT SATISFIED with no severity charge**, on V07 R1's reasoning exactly.

**Two things about this round's verification depth are worth recording, because they set the bar
the next round will be read against.** The backtest's headline result was not merely reproduced —
it was **re-derived from first principles in the reviewer's own code** rather than checked against
the runner, which is a stronger property than byte-identity: a shared bug in `run_pt035.py` would
survive a re-run and not survive an independent recursion. And the capture-tool finding was
established from **the SWF headers of all 21 source files** rather than from the one file that
failed, which converted a reported oddity into a rule about a knowable class — and produced the
policy fix in `SWF_CAPTURE_RECIPE.md` that three sessions had now hit and none had been able to
make. See `V09_REVIEW_R1.md`.

| Severity | Total | Open | Closed |
|---|---:|---:|---:|
| CRITICAL | 0 | 0 | 0 |
| MAJOR | 5 | 0 | 5 |
| MINOR | 57 | 12 | 45 |
| NOTE | 78 | 13 | 65 |

> **⚠ THIS TABLE IS STALE AS OF 2026-08-13 AND MUST NOT BE QUOTED AS CURRENT.** It reflects the
> state at **V09 R1** and has not been advanced since. It does **not** include **V09 R2's +3
> MINOR** (items 81–83, subsequently closed) or **V10 R1's +4 MINOR** (items 91–94, closed this
> round). **Neither of those rounds posted the per-round arithmetic paragraph** that every round
> from V07 R1 onward had posted, which is how the drift went unrecorded. **Found and disclosed by
> the V10 R1 fix round rather than corrected**, because reconciling it means re-auditing the
> pre-V03 rows this table has carried unreconciled since V02 R1 — a sweep, not an edit, and one
> this session was not authorised to make. **Owed with open item 96**, which is the same
> bookkeeping-decay class in `COURSE_PROGRESS.md`. The per-round delta paragraphs below and above
> are authoritative; the table is not.

*(V08 R2 arithmetic: CRITICAL, MAJOR and MINOR **totals** unchanged — no new finding was charged.
MINOR open 9 − 3 (items **64**, **65** and **66** verified closed) = **6**, closed 42 + 3 = **45**.
NOTE 67 → 70 (+`N1`–`N3`), open 8 + 2 (`N1` → item **71**, `N2` → item **72**, both carried) =
**10**, closed 59 + 1 (`N3` closed as an observation) = **60**. **The six carried minors are V02's
and V04's — none is V08's, and none is V05's, V06's or V07's.** Dimension B is restated, not
re-counted.)*

*(V07 R3 arithmetic: CRITICAL, MAJOR and MINOR **totals** unchanged — no new finding was charged.
MINOR open 11 − 2 (items **70** and **63** verified closed) = **9**, closed 40 + 2 = **42**. NOTE
63 → 67 (+`N1`–`N4`, all four closed as observations), open **8** unchanged, closed 55 + 4 = **59**.
The nine carried minors are V02's, V04's and V08's — **none is V07's**. Dimension B is restated,
not re-counted.)*

*(V07 R2 arithmetic: CRITICAL and MAJOR unchanged. MINOR 50 → 51 (+`M1`), open
12 + 1 (item 70) − 2 (items 61–62 verified closed; **item 63 is NOT closed** — half of it
verified, and it stays open until item 70 discharges) = 11, closed 38 + 2 = 40. NOTE 61 → 63
(+`N1`, `N2`, both closed as observations), open 8 unchanged, closed 53 + 2 = 55. Dimension B
is restated, not re-counted — R1's `N4` already carries it.)*

*(V08 R1 arithmetic: CRITICAL and MAJOR unchanged. MINOR 47 → 50 (+`M1`–`M3`), open
9 + 3 = 12 (items 64–66; nothing closed this round — V08 is the submission under review, and
the nine carried minors are V02's, V04's and V07's), closed 38 unchanged. NOTE 56 → 61
(+`N1`–`N5`), open 6 + 2 = 8 (`N1` → item 68 and `N4` carried open), closed 50 + 3 = 53.)*

*(V07 R1 arithmetic: CRITICAL and MAJOR unchanged. MINOR 44 → 47 (+`M1`–`M3`), open
6 + 3 = 9 (items 61–63; nothing closed this round — V07 is the submission under review, and
the six carried minors are V02's and V04's), closed 38 unchanged. NOTE 52 → 56 (+`N1`–`N4`),
open 5 + 1 = 6 (`N4` carried open), closed 47 + 3 = 50.)*

*(V06 R1 arithmetic: MAJOR 4 → 5, open +1 (item 57). MINOR 40 → 43, open
11 − 5 (V05 R3 closures, items 47–51) + 3 (items 58–60) = 9; closed 29 + 5 = 34.
NOTE 48 → 51, all three closed as observations, 43 + 3 = 46.
V06 R2 arithmetic: MAJOR open 1 → 0 (item 57 closed), closed 4 → 5. MINOR 43 → 44
(+`M5`), open 9 − 3 (items 58–60) = 6, closed 34 + 3 + 1 = 38. NOTE 51 → 52 (+`N1`,
closed), closed 46 + 1 = 47.)*

**Arithmetic of the V05 R1B + R2 update, written out so it can be checked.**
`MINOR` 35 → 40: **+4** (R1B `m1`–`m4`) **+1** (R2 `M11`, R1B's `n1` escalated). Open 12 →
11: **−6** (R1's `M1`–`M6` verified closed at R2) **+5** (open items 47–51). Closed 23 → 29.
`NOTE` 44 → 48: **+3** (R1B `n2`, `n3`, `n4`) **+1** (R2 `N4`, the second review-layer
concurrency event). **R2's `N1`, `N2` and `N3` restate carried items — the `E11` class
re-escalation, the two owner-decision items, and the blocked dimension-B action — and are
deliberately NOT double-counted**, on the V03 R2 / V04 R2 precedent for restated notes.
**`M7`–`M10` are counted once, at R1B, not again at R2.**

**Open MAJOR — V02 R1 finding 1.** The 11a homework markup contradicts the chart it
cites (PFH misplaced by 15 pips; the reversal attributed to Friday when it is Thursday's
move and Friday ran the opposite way), producing a false confirmation of the "at least
3 days" doctrine that `C-001` has open. Blocks V02 advancement. See
`18_REVIEW/V02/V02_REVIEW_R1.md`.

A lesson with unresolved CRITICAL issues cannot pass.

**MAJOR ledger — closed.** R1 raised 2. Finding 2 (`E10`, dimension F) closed at R2.
Finding 1 (`E02`, the box reading) closed in three of four locations at R2, reopened as
R2 finding N1, and **closed at R3**: `A-006`'s trailing block is withdrawn in place with
its original wording retained and its refutation recorded beside it.

**Closed at R3:** every remaining R1 and R2 finding. Three new `E11` defects were found
and closed in the same round, and one new `E20` (status blocks stale a third time) was
found and closed. **Two NOTES stay open** and neither bears on V01's mastery: the six
non-marker timestamp approximations, deferred with the `STUDY_PROTOCOL.md` amendment to
the 25% review (open item 7); and the V02 gate finding (open item 9), which is a process
observation about how the project sequenced its sessions, not about what V01 understood.

---

## OPEN RESEARCH ITEMS CARRIED FORWARD

Non-foundational issues that permitted a `PASS` but must not be forgotten.

| # | From | Item | Where tracked | Status |
|---|---|---|---|---|
| 1 | V01 R1 | `C-001` — day-count away from the anchor is self-contradicted in source and unresolved by the instructor. No artifact may commit a value. Re-examine at every weekly-holding-period lesson and at the 25% cumulative review | `CONTRADICTIONS.md` C-001 | OPEN |
| 2 | V01 R1 | `I7` — whether "anchor point", "peak formation high/low" and "M or W formation" are one concept. Stays `INFERRED / Low`; **re-adjudicate at V02** | `V01_INTERPRETATION.md` I7 / G4 | OPEN |
| 3 | V01 R1 | H4 / H5 `DEFERRED` pending `I-007` (chart data source). Reclassified in the mastery report 2026-08-10; `D-019` records the general rule. Perform when I-007 closes | `SETUP_ISSUES.md` I-007; `DECISIONS.md` D-019, **D-034** | ⚠️ **UNBLOCKED IN PART 2026-08-13 — `I-007` is CLOSED (`D-034`: TradingView / FXCM).** H4/H5 are observational chart exercises, so they need chart access rather than deep history; whether the declared feed's depth suits them is for the performing session to state. **OPEN — now actionable** |
| 4 | V01 R1 | Re-check `[00:46:04]`, `[00:48:05]`, `[00:48:13]` against the retained mp4 before any session-timing parameter is coded (`M3`) | `V01_INTERPRETATION.md` M3 / Q7 | OPEN |
| 5 | V01 R1 | Dimension B (Recognition) deferred to after V02 defines the trading zone | `V01_MASTERY_REPORT.md` B | OPEN |
| 6 | V01 R1 remediation | The stale *"no screenshot exists for V01"* paragraph appears in **17** ambiguity records, not the 3 instances R1 counted. `A-006` fixed as a dependency; **16 remain** (`A-001`–`A-005`, `A-007`–`A-017`). **Adjudicated by R2 (Part 3) — this is partly study work, but the scope stated here was wrong.** `A-009`, `A-015` and `A-017` were named as needing fresh visual claims; all three already carry sound visual updates, audited and upheld in R2. The records that actually need a fresh visual determination are **`A-002`, `A-008`, `A-016`** (determinations supplied in R2 Part 3.3), plus `A-003`'s five self-contradicting fields. `A-011` / `A-012` / `A-014` gain slide-text evidence; `A-007` needs a "frame exists, defines nothing" note; the remaining eight are mechanical | `AUTOMATION_AMBIGUITIES.md`; `18_REVIEW/V01/V01_REVIEW_R2.md` Part 3 | **CLOSED at R3** — all 16 records corrected; `A-002`, `A-008`, `A-016` determinations written and audited against the frames; two of R2's supporting claims corrected in the process (see `V01_REVIEW_R3.md` Part 3) |
| 7 | V01 R2 | Citation hygiene is the project's recurring weakness (`E11` ×5). Eight statements across two rounds cite a timestamp that does not carry their words. No quotation is fabricated. Consider requiring in `STUDY_PROTOCOL.md` that a quoted sentence cite the marker its first words fall under, and that passage-level citation be written as an explicit range | `18_REVIEW/REVIEW_INDEX.md` escalation note; raise at `CUMULATIVE_25.md` | OPEN |
| 8 | V01 R2 | `SETUP_ISSUES.md` I-006 described the SWF header frame-rate speedup as "an untested faster path". **R2's own framing was stale in turn:** it cited `D-020` as having ruled the speedup out, but `D-020` is `RETRACTED` and `D-021` records that the speedup **works at 40×** and is the default method. `I-006` now points to `D-021` | `SETUP_ISSUES.md` I-006; `DECISIONS.md` D-021 | **CLOSED at R3** |
| 9 | V01 R3 | **The V02 gate was not honoured.** `D-004` makes reviewer `PASS` the only progression gate, and `COURSE_PROGRESS.md` recorded `V02 GATE: CLOSED`, yet a full V02 student pass (transcript, notes, interpretation, 25 screenshots, homework, mastery report, `A-019`–`A-028`, `C-003`–`C-004`) was completed while V01 was in remediation. V01's `PASS` makes this moot going forward, and none of the V02 work is discarded — but the gate did not hold, and the next one (V02 `PASS` before V03) must | `DECISIONS.md` D-004; `COURSE_PROGRESS.md` | OPEN — process. **First test PASSED at R2:** V02 R1 returned `REVISE` and no V03 artifact was created — verified at the filesystem level across `03_LESSON_NOTES/`, `04_SCREENSHOTS/`, `05_HOMEWORK/`, `07_MASTERY_REPORTS/`. Stays open until a second gate holds. **ESCALATED at R2 to a LIVE BREACH — the second occurrence, and this one is not moot.** A V03 student pass appeared in the working tree during R2 while V02 was unpassed. **Two failures of the same written gate in one day is a mechanism problem, not a discipline problem:** D-004 has no enforcement, exactly like the status-block rule in R2 Minor 3. Concrete fix — a pre-flight guard in `validate_project.py` that refuses `VNN` artifact creation while `VNN GATE: CLOSED`. Required disposition in `18_REVIEW/V02/V02_REVIEW_R2.md` §7: stop the V03 pass, **do not delete the V03 work**, re-audit it against a passed V02. **UPDATED 2026-08-10 — `DECISIONS.md` D-023 and D-024.** The second occurrence is now recorded as an **owner-authorized override** (D-023): R2 §7's "stop the V03 pass" disposition is discharged and the V03 work stands as committed — nothing to revert or re-audit. **This item stays OPEN on its mechanism ground alone**, which the override does not touch: an unenforced written gate failed twice, and the override explains only why the second failure was authorized, not why an unauthorized one would have been caught. D-024 now defines what holds the gate (minors-only opens it; any `CRITICAL`/`MAJOR` closes it), so the `validate_project.py` pre-flight guard should implement **D-024's severity table**, not D-004's simpler `PASS`-only reading, plus an explicit override flag that must name the authorizing decision entry |
| 10 | V02 R1 | ~~**`C-001` has one empirical datum and it was misread.**~~ The 11a homework is the only independent observation the project has made about the day-count doctrine, and its "runs Tuesday through Thursday, consistent with 'At Least 3 Days'" claim is contradicted by the chart (price traded back above the Monday high on Thursday). Once 11a is corrected, record what the week **actually** shows against `C-001` — including "nothing", which is a legitimate result. Do not let a corrected reading quietly drop the C-001 entry | `CONTRADICTIONS.md` C-001; `18_REVIEW/V02/V02_REVIEW_R1.md` MAJOR 1 | **CLOSED at R2** — 11a redone from measurement and independently re-verified; the "three days" confirmation withdrawn; the corrected result (level 0.81150 set Mon 3 Aug 15:00 UTC, first bar above it Thu 6 Aug 15:00, **72 hours exactly**) recorded in `CONTRADICTIONS.md` under C-001 as explicitly non-resolving. The entry was **not** quietly dropped. `EFFECT ON C-001: NONE` is correct in both directions — three counting conventions give three answers, and the level was reader-selected against `A-004`. No day-count value is committed anywhere |
| 11 | V02 R1 | **A-006 / A-003 spot-check requested by V01 R3 — completed, both PASS.** Verified against the frames, not against R3's word: `[00:40:25]` prints "Trigger The Pendings"/"Trigger The Stops" as A-003 claims; `[00:38:50]` shows the pale-blue rectangle's left edge on the second vertical separator and covering a sharp advance, confirming both A-006's withdrawal and R2's narrowing. R3's remediation is substantively correct despite its D-003 departure — though two records is not an audit of fifteen actions | `18_REVIEW/V02/V02_REVIEW_R1.md` Ambiguities | **CLOSED** |
| 12 | V02 R2 | **`V02_HOMEWORK.md` §1.1's measurement pipeline is advertised as reusable for the dimension-G backtest but places one bar on the wrong side of the Fri 31 Jul → Sun 2 Aug boundary**, and its *"open = prior close on all six boundaries"* self-validation was applied at a weekend boundary where continuity should not be expected. The chart's own dotted day separators (`x = 147, 273, 429, 573, 717, 861, 987, 1149`) settle it. No conclusion in the homework changes. Must be corrected before the pipeline is reused | `V02_HOMEWORK.md` §1.1; `18_REVIEW/V02/V02_REVIEW_R2.md` Minor 1 | **CLOSED at R3** — corrected in `8df7c32` and independently re-derived at R3 from the PNG: separators, bar counts, both corrected rows, the −12.63 pip weekend gap and the `31`/`Aug` label centroids (146.12 / 273.03) all reproduce exactly. The two refuted arguments are withdrawn with the measurements that kill them, the superseded reasoning is retained in place per `REMEDIATION_PROTOCOL.md` §2, and the pipeline's real limits are now written into the file: read the chart's own separators, and do not expect continuity across a session gap |
| 13 | V02 R2 | **Two measurements of the same chart disagree, and one is untracked.** `05_HOMEWORK/V02/measure_usdchf_week.py` is a working, uncommitted measurement script that encodes the *correct* Sun 2 Aug mapping and calls the boundary *"uncertain by one bar"*, contradicting committed §1.1's "settled". **Leave it in place, adjudicate with item 12, do not delete.** §1.1 promises a reproducible method and commits no script; committing a corrected one discharges that promise | `05_HOMEWORK/V02/`; `18_REVIEW/V02/V02_REVIEW_R2.md` Note 8 | ✅ **CLOSED 2026-08-12 — `1fa087f`.** The project owner committed `05_HOMEWORK/V02/measure_usdchf_week.py` (166 lines) directly. The file is now tracked, so §1.1's promise of a reproducible method is discharged by a script under version control rather than by an untracked working-tree artifact, and the standing *"leave in place, do not delete"* instruction — honoured by every session from V02 R2 through V05 R3 — is spent. The script reads only the committed PNG (no network, no TradingView account), so any session can re-derive the per-bar highs and lows. **This closes the tracking half of the item only.** The substantive question the row also raises — committed §1.1's *"settled"* against the script's *"uncertain by one bar"* — belongs to **item 12** and is neither adjudicated nor altered here |
| 14 | V02 R2 | **A stated rule did not prevent the defect it was written for.** `COURSE_PROGRESS.md`'s status view went stale in the same commit that declared the SUMMARY authoritative — fifth occurrence of this class. Promote R1's proposed mechanical check in `validate_project.py` from suggestion to work item at the 25% review; all five occurrences are arithmetic over a file's own contents | `18_REVIEW/REVIEW_INDEX.md` escalation notes; raise at `CUMULATIVE_25.md` | OPEN — **sixth occurrence at R3**, again inside a remediation: correction 2 shipped in `d030a14` without updating `COURSE_PROGRESS.md`, which still read `⏳ OUTSTANDING` for it, and the PROGRESS TABLE's V02 row had never been reconciled to R2 at all. Discharged by the R3 session, which had to rewrite those lines to record its decision. Six instances, all arithmetic over a file's own contents. **This is a work item at the 25% review, not a suggestion** |
| 15 | V02 R3 | **`level count` is presented as a verbatim transcript occurrence and the literal string occurs zero times.** The referent is real — *"you can't count the levels"*, `[00:33:11]` — and `A-004` rests on the passage, not the string. `V02_SOURCE_NOTES.md` §3 needs **no** change (its row is headed *"Level count / counting the levels"* and quotes the actual words); only `V02_TRANSCRIPT.md`'s "One thing was removed" paragraph does. Notable because it is the residue of the same false claim: three verbatim counts were asserted, two were checked and found to be zero, the third was carried forward unchecked in the edit that corrected the other two. **Non-blocking; fix at the next natural touch** — exact wording in `V02_REVIEW_R3.md` §3 | `V02_TRANSCRIPT.md` §"One thing was removed"; `18_REVIEW/V02/V02_REVIEW_R3.md` Minor 1 | OPEN |
| 16 | V02 R3 | **The *"174 of 176"* continuity figure does not reproduce.** R3's independent measurement finds **172** boundaries continuous at the stated 0.15-pip threshold, or **175** above 0.8 pip; three genuine sub-pip gaps exist besides the weekend one (`x=285` −0.19 pip, `x=447` +0.77, `x=933` −0.77, confirmed visually at 4× zoom), so *"the only open ≠ prior-close discontinuity"* is overstated. **174 is unreachable under any threshold. Charged against R2, not the student** — required correction 1 instructed the student to state R2's number and the remediation did so accurately. Changes nothing and errs in the safe direction: continuity is *weaker* than claimed, which strengthens the corrected reasoning. **Non-blocking**; restate as 175 of 176 within 1 pip, only material discontinuity −12.6 pip at `x=273`, three sub-pip gaps besides | `V02_HOMEWORK.md` §1.1/§1.4; `V02_MASTERY_REPORT.md`; `COURSE_PROGRESS.md`; `18_REVIEW/V02/V02_REVIEW_R2.md` §1c | OPEN |
| 17 | V02 R3 | **An owner-authorized override is recorded in the repository as an unresolved violation.** The project owner confirmed the parallel V03 work as an intentional override of the closed D-004 gate, but `DECISIONS.md` carries no entry for it (last entry D-022), so `COURSE_PROGRESS.md`'s `V03 GATE` block and open item 9 above still read as a live breach. A future session will either halt authorized work or conclude the gate register is unreliable. **Owner action:** record the override as a numbered decision and reconcile both locations to it. **Does not close item 9's mechanism finding** — a written gate with no enforcement failed twice in one day, and the `validate_project.py` pre-flight guard is still the fix | `DECISIONS.md`; `COURSE_PROGRESS.md`; `18_REVIEW/V02/V02_REVIEW_R3.md` Note 3 | ✅ **CLOSED 2026-08-10 — `DECISIONS.md` D-023** records the override as a numbered decision (scope: one instance, V02 → V03, source-side work only; not precedent; not to be reverted), and `COURSE_PROGRESS.md`'s `V03 GATE` block and `NEXT ACTION` item (c) are reconciled to it. `V02_REVIEW_R2.md` is deliberately left unedited per §11. Item 9 below is **not** closed by this — see its own row |

| 18 | V03 R1 | **M1 — homework ADR figures not reproducible.** State the day-boundary convention and commit the five per-pair daily ranges (or recompute under a stated convention). The 0-of-4 conclusion survives every convention tried | `V03_HOMEWORK.md` §2.5 Finding B; `18_REVIEW/V03/V03_REVIEW_R1.md` M1 | ✅ **CLOSED 2026-08-10 — VERIFIED at R2.** Convention stated (21:00 UTC FX day; bars 0–5 / 6–11 / 12–17 / 18–23 / 24–29); all twenty daily ranges committed in §2.5; ADR recomputed to 46.5 / 55.7 / 138.9 / 54.4 with a correction note retaining the superseded figures. R2 re-derived every one of the twenty ranges from the raw JSON — all match to a tenth of a pip — plus 3×ADR, the four multiples (1.73 / 1.64 / 2.41 / 1.48), and the 116/116 bar continuity the split depends on. 21:00 UTC confirmed as the only 4h-aligned boundary yielding five whole days. 0 of 4 reaching 3×ADR holds with margin |
| 19 | V03 R1 | **M2 — transcript coverage block overclaims.** "Strictly monotonic, no duplicates" is false: three benign same-second adjacent duplicate markers (`[00:35:21]`, `[01:00:13]`, `[01:04:30]`); sequence is non-decreasing. Fix the wording | `V03_TRANSCRIPT.md` COVERAGE; `V03_REVIEW_R1.md` M2 | ✅ **CLOSED 2026-08-10 — VERIFIED at R3.** Commit `492bb11` replaced the `COVERAGE` sentence with the true statement and left the verified I-008 text at lines 39–47 untouched (diff read: one file, five lines). R3 re-derived every component from the transcript itself — 1,230 markers, 1,227 distinct, 0 decreasing transitions, exactly 3 adjacent same-second pairs at the three named markers, largest gap 13 s at `[01:09:02]`, final entry `[01:10:39]` — and ruled out the header-block counting artifact (all counted markers fall between lines 115 and 3,802; last `##` heading at 87). Both blocks now agree and both are true; no third instance survives; the `E20` monotonicity class is empty project-wide on a fresh scan of all four transcripts. **This closes items 18–20 as a set and takes V03 to `COMPLETE`.** `LOG.md` 1746–1747 re-confirmed untouched and properly superseded at 1848 ff. — do not "fix" them. **Prior status, retained for the record:** ⚠️ *STILL OPEN after R2 — applied to the wrong location.* The corrected line ("1,230 timestamps, 1,227 distinct, non-decreasing throughout, three benign same-second adjacent pairs at `[00:35:21]`, `[01:00:13]`, `[01:04:30]`", plus a correction note) was added to the **`PROVENANCE AND VERIFICATION` I-008 criterion 1**, lines 39–46. R2 re-derived every component of it by regex and **all seven check out exactly** — that wording stands. But the sentence R1 charged lives in the **`COVERAGE`** block, lines 23–24, which was left untouched and still reads *"timestamps strictly monotonic, no duplicates"*; the file now asserts both propositions fourteen lines apart. **Required: replace `COVERAGE` lines 23–24 with the true statement; leave lines 39–46 alone.** V02's identical-sounding line was independently re-scanned at R2 and is confirmed **true as written** (1,026 markers, 1,026 distinct, zero decreasing transitions) — leaving it unchanged was correct. Note: `V01_TRANSCRIPT.md` has five same-second pairs (974 / 969) but makes no monotonicity claim, so nothing is false there — the E20 class is empty project-wide once this row closes. Carried as `V03_REVIEW_R2.md` M2′ |
| 20 | V03 R1 | **M3 — duration finding over-scoped.** "4 of 4 exceed the 2.5–3-day window" counts two pairs (USDJPY, USDCHF) whose low is the week-open bar with no formed anchor — supported sample is 2 of 4 (both 3.8 days, still exceeding). Scope it in homework §2.5A and mastery report §2 before it is cited against `C-001` | `V03_HOMEWORK.md` §2.5; `V03_MASTERY_REPORT.md` §2; `V03_REVIEW_R1.md` M3 | ✅ **CLOSED 2026-08-10 — VERIFIED at R2.** Homework §2.5 Finding A now carries a per-pair "does this measure the taught object?" column, an explicit 2-of-4 scope statement, and the instruction that any citation against `C-001` must carry it; homework §4 point 3 and mastery report §2 and §D re-scoped to match. R2 re-derived the basis from the raw OHLC: USDJPY and USDCHF have `cut_lo` = 0 bars — the block low is never taken out and *is* the week low at bar 0 — while EURUSD and GBPUSD cut at bar 2 and form their lows at bars 4 and 5, both 92 h = 3.8 days. Propagation confirmed at all four sites, plus a whole-repo sweep finding no surviving pre-correction figure (the stale numbers in `LOG.md` 1746–1747 are a historical journal entry, superseded at 1859/1892, and must **not** be edited). The `C-001` deferral was tested by reading the record rather than trusting it: the V03 evidence section cites only transcript restatements and the new exit rule, and no homework duration appears anywhere in the file — so the datum is genuinely not yet cited, and the standing "scoping travels with it" instruction is committed in both homework §2.5A and mastery report §2, where a future session will be standing when it bites |
| 21 | V03 R1 | **N4 — manual-backtest debt, three lessons deep.** Each deferral individually sound (no testable entry rule yet), but the obligation accrues: when the first testable rule lands (plausibly the V03 exit once A-033 "outside structure" is defined), the hidden-future backtest backlog must be discharged against it. The reviewer will require it | `V03_REVIEW_R1.md` N4; `06_MANUAL_BACKTEST/` | OPEN |

| 22 | V04 student pass | **`C-005` needs a SCOPE RULING on guest-presenter material — owner or reviewer, not a student session.** V04 is 69% presented by someone who is not the course author, and the student session fenced all of it as non-doctrine. That is a large unilateral exclusion. **Should be settled before V05**, which shares V04's 2012-03-25 session date and may contain the same guest or the third presenter ("Carl", queued at V04 `[01:19:02]`). The record is `UNRESOLVED` *pending a ruling, not pending evidence* — no future lesson can resolve it | `CONTRADICTIONS.md` C-005; `V04_MASTERY_REPORT.md` audit item 1; `18_REVIEW/V04/V04_REVIEW_R1.md` §"The C-005 ruling" | ⚖️ **RULED 2026-08-10 at V04 R1 — OPEN only on the recording step.** **Guest-presenter material is admissible as SECONDARY, DESCRIPTIVE evidence and is EXCLUDED from the canonical methodology as NORMATIVE material.** Neither extreme is correct. *Normative* content (entry criteria, gates, filters, stops, targets, sessions, thresholds, schedules) may not enter the master spec, machine spec, concept library or any machine candidate, may not be cited **for or against** an instructor rule, and may never be merged with instructor statements into one rule set. *Descriptive* content (that a term exists, how it is spelled, that an object is displayed, what a printed artifact says) is admissible at a weight strictly below any instructor statement — it may **extend** an `A-xxx`/`C-xxx` record and may **never close** one. Four binding consequences: a guest statement can never resolve an ambiguity or contradiction; a guest/instructor divergence is a **corpus-hygiene** record, never a contradiction charged against the instructor; **speaker tagging is mandatory** from V04 forward for any multi-voice lesson; identifying a guest is provenance, not evidence. **Retroactive effect on V04: none — the ruling ratifies the student's existing handling exactly, and no V04 grade changes.** The reviewer verified the identification independently (*"Zen Jason … Alldredge"* read off frame 21's Navigator; segment B refers to Steve in the third person 40+ times and at `[01:24:53]` *"Steve is asking…"* places him in the audience; 69% measures at 68.5%). ~~**Owner action, before V05: record as `DECISIONS.md` D-025.**~~ ✅ **CLOSED 2026-08-11 — RECORDED as `DECISIONS.md` D-025**, refining `D-008`, with the ruling's four consequences carried into the entry verbatim in substance and cross-referenced from `D-008`, `D-004`'s pointer block, `COURSE_PROGRESS.md`'s `PROGRESSION RULE` and `REVIEW_PROTOCOL.md` §2. `C-005` updated: its "Required to resolve" field is discharged, and the record stays open as a **corpus-hygiene** record, which the ruling says is the right category. The recording step was the only thing left open here. |
| 23 | V04 student pass | **`A-039` — TDI is a REQUIRED condition of V04's entry rule and the course has never taught it.** Deferred at V03 `[01:01:53]` and again at V04 `[00:22:11]`; the instructor could not even display it on his own example chart. This is what blocks V04's dimension G. The record carries an explicit prohibition: **no session may drop condition (c) to make the rule testable** — a two-condition version is a different rule with a different hit rate (`E06`/`E18`) | `AUTOMATION_AMBIGUITIES.md` A-039 | OPEN — **UPHELD at V04 R1.** Both deferrals read at their markers and exact; all 13 `TDI` occurrences in V04 read in context and not one defines the indicator, its inputs, its bands, the shark-fin geometry or "blood in the water". Dimension G's `DEFERRED` upheld and `NOT APPLICABLE` correctly declined. The counter-argument (test (a)∧(b) alone) is **rejected**: dropping a *necessary* condition does not shrink the sample, it changes the population, because the discarded condition is the confirmation step. See also item 30 — TDI is *displayed* on the guest's platform, which changes nothing here |
| 24 | V04 student pass | **Manual-backtest debt is now FOUR lessons deep, and its character has changed.** Through V03 the deferral was "no testable entry rule exists". From V04 it is "a testable rule exists and one named input is missing". Item 21's obligation therefore has a concrete trigger for the first time: **when TDI is taught, the hidden-future backlog becomes dischargeable and must be discharged** | `REVIEW_INDEX.md` item 21; `A-039`; `06_MANUAL_BACKTEST/` | OPEN — **UPHELD at V04 R1.** The reviewer will require the backlog to be discharged in the lesson that teaches TDI |
| 25 | V04 R1 | **`M1` — USDCHF's 15-minute series is mis-sliced at a partial week-open bar.** On this feed USDCHF's first 4h bar of the week holds only twelve 15m bars; the fixed 16-bar aggregation therefore puts four previous-week bars at the head of the committed 480-bar slice (`offset_in_harvest = 261`) and leaves it four short at the tail. The `−12.7` pip weekend gap sits *inside* the committed week at `m[3]→m[4]`, and `aggregate(m[4:16])` reproduces 4h bar 0 exactly on all four fields. The 27/30 symptom was reported as ±0.4 pip harvest noise when bar 0's **open** differs by 28.1 pips. **No conclusion changes** — the 4h data is continuous 116/116 and USDCHF is already outside the scoped 2-of-4 result — but the 15m harvest is the pipeline V05 inherits. Same class as open item 12 | `05_HOMEWORK/V04/`; `V04_REVIEW_R1.md` M1 | ✅ **CLOSED — VERIFIED at R2 2026-08-11**, re-derived from `V05_TRANSCRIPT.md` and the committed PNGs rather than from the remediation diff. Diagnosed and re-sliced from the committed data. USDCHF's week is **476 = 12 + 29 × 16** bars, not 480 — the four leading bars were previous-week and nothing was missing from the tail. `offset_in_harvest` 261 → **265**, `j_hi_15m` 363 → 359, `j_lo_15m` 4 → 0, and a new per-pair **`bars_15m_in_4h_bar_0`** field (16/16/16/**12**) makes the aggregation explicit rather than assumed. USDCHF 27/30 → **28/30**; the 4h↔15m total **474/480 → 476/480**, its four residuals now all ≤ 0.3 pip and all in highs or lows. The ±0.4 pip misattribution is replaced by the real diagnosis in `V04_HOMEWORK.md` §1.2 validation 3, with the partial-first-bar behaviour stated as a limit of the 15m pipeline and a standing instruction to future sessions not to assume 16. New committed script **`scripts/verify_reconstruction.py`** recomputes it and exits non-zero on mismatch. **No conclusion changed, verified not assumed:** the 4h data is untouched (116/116), USDCHF stays excluded from the scoped 2-of-4 result on 4h grounds, and the §3.3 descriptor windows are identical because index and window shifted together ✅ **CLOSED — VERIFIED at R2 2026-08-11.** Re-derived in both directions from the parent and current JSON by an independent script: the defect was real (one −12.7 pip discontinuity at `m[3]→m[4]`; bar-0 open off by 28.1 pips; `aggregate(m[4:16])` equal to 4h bar 0 on all four fields) and the fix is exact and minimal (new array is exactly `old[4:]`, only USDCHF changed, 4h untouched, `476 = 12 + 29×16` consumes the array, bar 29 reconstructs). **476/480 fields, 116/120 bars, zero in-week 15m discontinuities in all four pairs**, all residuals ≤ 0.3 pip and all in highs/lows. `verify_reconstruction.py` run as shipped: exits 0, and its checks are not tautological. Every pair's re-indexed 15m extreme maps onto the 4h bar holding the same extreme at an identical price — closes under the new indices, not the old. Scoped 2-of-4 / 3.83-day result unchanged, USDCHF still excluded on 4h bar 0 |
| 26 | V04 R1 | **`M2` — two smoothed quotations inside the transcript's own verbatim-proof paragraph** (`E01`): *"sitting up here"* for *"set up here"* `[00:50:34]`, and *"gave you a nice ugly looking kindergarten"* for *"Gaby a nice ugly look in kindergarten ma'am there"* `[01:10:36]`. Either restore both or state that the list quotes the Whisper re-transcription. **The student self-caught ~20 instances of this class before commit and that fix verifies** — these two are survivors in the provenance narrative, not in the notes | `V04_TRANSCRIPT.md` criterion 2; `V04_REVIEW_R1.md` M2 | ✅ **CLOSED — VERIFIED at R2 2026-08-11**, re-derived from `V05_TRANSCRIPT.md` and the committed PNGs rather than from the remediation diff. Both restored to the **adopted transcript's** literal wording — *"There was a bunch of money **set up** here…"* `[00:50:34]` and *"One, two, three, swipes. **Gaby** a nice ugly **look in** kindergarten **ma'am** there."* `[01:10:33]`–`[01:10:36]` — and the paragraph now states explicitly that the six specifics are quoted from the adopted transcript. The smoothing is disclosed in place rather than silently corrected ✅ **CLOSED — VERIFIED at R2 2026-08-11.** Checked against the transcript **body**, not the diff: line 3047 *"There was a bunch of money set up here and they had to go after it."* `[00:50:34]` and lines 4138/4142 *"One, two, three, swipes. / Gaby a nice ugly look in kindergarten ma'am there."* `[01:10:33]`/`[01:10:36]` — both exact. Restoration taken rather than re-attribution, and the paragraph now states which side it quotes |
| 27 | V04 R1 | **`M3` — two ambiguity cross-references point at the wrong records.** `V04_TRANSCRIPT.md` `TRANSCRIPTION NOTES` sends *"the water"* to `A-037` and *"Timing Shadow Box / Brink Spox"* to `A-038`; the register holds the Asian-range halving and the guest's ADR window at those IDs. Correct targets **`A-031`** and **`A-030`**. Orphaned pre-assignments — the transcript shipped at `d6acbf8`, the register at `4235df1` | `V04_TRANSCRIPT.md`; `V04_REVIEW_R1.md` M3 | ✅ **CLOSED — VERIFIED at R2 2026-08-11**, re-derived from `V05_TRANSCRIPT.md` and the committed PNGs rather than from the remediation diff. *"the water"* → **`A-031`**; *"Timing Shadow Box / Brink Spox"* → **`A-030`**. A dated note in `TRANSCRIPTION NOTES` records the orphaned pre-assignments and their cause ✅ **CLOSED — VERIFIED at R2 2026-08-11.** `A-031` is *"blood in the water"/"bloodline"* and `A-030` is *"brinks shadow"/"shadow box"* — the correct subjects. `A-037` (Asian-range halving) and `A-038` (guest ADR lookback) confirmed to be the wrong ones, and every surviving `A-037`/`A-038` reference in the V04 artifacts re-checked and legitimate |
| 28 | V04 R1 | **`M4` — stale count and stale filename.** `V04_SOURCE_NOTES.md` says *"26 frames"* (27 exist); `V04_MASTERY_REPORT.md` FILES PRODUCED says `VISUAL_INDEX` (renamed to `INDEX.md` in the same session). **Sixth and seventh instances of the status-staleness class** — both are arithmetic or a filename check over the repository's own contents and belong in the `validate_project.py` check proposed at open item 14 | `V04_REVIEW_R1.md` M4; open item 14 | ✅ **CLOSED — VERIFIED at R2 2026-08-11**, re-derived from `V05_TRANSCRIPT.md` and the committed PNGs rather than from the remediation diff. `V04_SOURCE_NOTES.md` now reads *"27 frames, indexed in `04_SCREENSHOTS/V04/INDEX.md`"*; the mastery report's FILES PRODUCED block reads `INDEX.md` (and *"2 scripts"* → 3, since `verify_reconstruction.py` was added under item 25) ✅ **CLOSED — VERIFIED at R2 2026-08-11.** Counted: 27 PNGs in `04_SCREENSHOTS/V04/`, 3 scripts in `05_HOMEWORK/V04/scripts/`. Both files corrected; the only surviving `VISUAL_INDEX` string is inside the remediation log describing the fix |
| 29 | V04 R1 | **`M5` — homework validation 1 is not reproducible from committed data.** *"569 bar transitions, 549 continuous, 20 breaks"* with break indices 15/45/75/105/135 and a GBPUSD exception at 143 requires full harvests; the JSON holds only the 30-bar week per pair (116 transitions available, and those reproduce 116/116). Accuracy is not in doubt — reproducibility is. Same promise as open item 13 | `V04_HOMEWORK.md` §1.2; `V04_REVIEW_R1.md` M5 | ✅ **CLOSED — VERIFIED at R2 2026-08-11**, re-derived from `V05_TRANSCRIPT.md` and the committed PNGs rather than from the remediation diff. Restated over the committed data — **116/116 continuous**, recomputed by `verify_reconstruction.py` — and the harvest-wide **569 / 549 / 20** figures explicitly marked **UNREPRODUCED**, in validation 1 and again in §1.3 "What is NOT validated". **The arrays were deliberately not manufactured back into the repo:** they were never written to disk, and re-harvesting today would produce a *different* dataset from the one every figure in the file was computed on. The week boundary the figures existed to establish is independently supported by the committed data (116/116, plus 476/480 agreement with V03's dataset) ✅ **CLOSED — VERIFIED at R2 2026-08-11, and the judgement call upheld on the merits.** The honest-caveat route was the correct one: the arrays were never written to disk, so committing a fresh harvest would attach data to claims never computed on it — provenance fabrication, worse than a declared gap. Figures are marked UNREPRODUCED, not withdrawn; nothing downstream depends on them; the caveat also appears in §1.3. The reproducible half recomputes here: **116 transitions, 116 continuous, zero breaks** |
| 30 | V04 R1 | **`M6` — a visible TDI panel is unrecorded.** Curated frames 21 (`01-04-10`) and 22 (`01-08-40`) each render a sub-panel titled **`Traders Dynamic Index Visual`** with its parameter list and cyan volatility bands — the very object condition (c) refers to — on the guest's platform. Both frames are otherwise described in detail. **This does not weaken `A-039`**: displayed is not taught, and no settings or decision rule is recoverable. Add to `INDEX.md` and to `A-039`'s evidence table scoped *"displayed, not taught"*; as descriptive evidence under the item-22 ruling it also settles that "TDI" denotes the **Traders Dynamic Index**, which no line of V01–V04 audio states | `04_SCREENSHOTS/V04/INDEX.md`; `A-039`; `V04_REVIEW_R1.md` M6 | ✅ **CLOSED — VERIFIED at R2 2026-08-11**, re-derived from `V05_TRANSCRIPT.md` and the committed PNGs rather than from the remediation diff. Recorded in `INDEX.md` on both frame rows and as a new §"What the visuals added" item 7, and in `A-039`'s evidence table as two rows tagged **`GUEST`, DESCRIPTIVE ONLY**, each scoped **"displayed, not taught"** with an explicit statement that they do **not** narrow `A-039` — guest evidence may extend a record and may never close it (`D-025`). The frames were opened and magnified before the descriptions were written: the six-value numeric readout beside each panel title is **not legible** at this resolution and is deliberately **not transcribed**. `A-039`'s *"the example chart carries no TDI panel"* line is now scoped to the instructor's own Segment-A chart, which is what it always meant ✅ **CLOSED — VERIFIED at R2 2026-08-11.** Both frames opened and magnified before the new text was read. The `Traders Dynamic Index Visual` panel, its coloured lines and its bands are on both frames as described. **The six-value readout is genuinely at the edge of legibility — declining to transcribe it was the right call** and saying so in the index beats a guess or a silent omission. "Displayed, not taught" is accurate on the merits: no inputs, periods, band construction or decision rule is recoverable. Beyond what was asked, `A-039`'s *"the example chart carries no TDI panel"* line is now correctly scoped to the instructor's Segment-A chart |
| 31 | V04 R1 | **`M7` — four quality-control boxes unchecked and undeclared**: concept library, positive / negative / borderline examples. `08_CONCEPT_LIBRARY/` and all four `09_CHART_EXAMPLES/` subdirectories are empty four lessons in. `MASTERY_STANDARD.md` requires unchecked boxes to be *stated*. **Shared with V02 and V03, not a V04 lapse** — but V04 is the first lesson with a complete entry rule and a body of named terms, so the library should begin here. **Raise the underlying debt at `CUMULATIVE_25.md`** | `MASTERY_STANDARD.md`; `V04_REVIEW_R1.md` M7 | ✅ **CLOSED — VERIFIED at R2 2026-08-11**, re-derived from `V05_TRANSCRIPT.md` and the committed PNGs rather than from the remediation diff. New **QUALITY-CONTROL CHECKLIST** section in `V04_MASTERY_REPORT.md`: of nineteen boxes, **13 checked, 2 `DEFERRED`** (manual chart testing and failed-valid-setups, both blocked by `A-039` and stated rather than ticked), **4 UNCHECKED and declared** with a reason each. The concept-library box is explicitly **not** excused by `A-039` — unlike the three example boxes it was performable and was not done. **The project-wide instance is still owed at `CUMULATIVE_25.md`** — V02's and V03's reports omit the same four boxes ✅ **CLOSED — VERIFIED at R2 2026-08-11.** All 19 `MASTERY_STANDARD.md` boxes accounted for: **13 checked + 2 `DEFERRED` + 4 UNCHECKED**. Declarations true against the repository (`09_CHART_EXAMPLES/` subdirs hold only `.gitkeep`; `CONCEPT_INDEX.md` reads `CONCEPTS: 0`). Notably **refuses to excuse the concept-library box** by pointing at `A-039`, and argues the two `DEFERRED` boxes rather than ticking them |
| 32 | V04 R1 | **`N1` — dimensions B and C are mis-dispositioned.** Graded `PARTIAL` and `FAIL` for one reason: condition (c)'s indicator has never been taught. That is `D-019`'s definition of **`DEFERRED`**, not a failure of mastery. **As labelled, V04 can never reach `PASS`**, because the cause sits in the source and will not change until TDI is taught — the same trap `D-018` was written to escape for dimensions F and G, arriving now for B and C. Re-disposition as `DEFERRED — blocked by A-039`, retaining the present honest text beneath the new label. **`NOT APPLICABLE` is not available and must not be used** | `V04_MASTERY_REPORT.md` B, C; `DECISIONS.md` D-019; `V04_REVIEW_R1.md` N1 | ✅ **CLOSED — VERIFIED at R2 2026-08-11**, re-derived from `V05_TRANSCRIPT.md` and the committed PNGs rather than from the remediation diff. **B `PARTIAL` → `DEFERRED`, C `FAIL` → `DEFERRED`**, both labelled *"blocked by `A-039`"* under `D-019`, with the original text retained **verbatim** beneath the new label and a dated note giving the mechanical reason (a `FAIL` whose cause sits in the source can never be cleared by studying). `NOT APPLICABLE` explicitly declined. Both are carried in `CARRIED FORWARD` as open items alongside the manual-backtest debt, to be performed in the lesson that teaches TDI ✅ **CLOSED — VERIFIED at R2 2026-08-11.** Checked against `D-019`'s own V01 F/G worked example, not the label: subject matter exists, `NOT APPLICABLE` explicitly declined, blocker is a missing prerequisite (`A-039`), items stay **open** and are carried. Original `PARTIAL`/`FAIL` prose retained **verbatim** — diffed, not eyeballed; not one word of body text changed |
| 33 | V04 R1 | **The `RULES.md` fabrication audit is a SOLVED PROBLEM for V05–V21 — a time-saver, recorded so it is not re-discovered 17 times.** Verified at full population this round: all 21 files carry both template quotes at `[00:05:00]` and `[00:18:00]`, exactly two rules each, **and a byte-identical `NUMERICAL PARAMETERS` block (one hash, 21/21)**; `INFERRED VISUAL RULES` and `TERMS` have only two variants each across 21 files. A future session may discharge the per-lesson audit in one step by confirming those three markers and citing `V04_REVIEW_R1.md` + `Q-004`. **No `RULES.md` in this library can come back clean.** `NOTES.md` and `VISUAL_INDEX.md` are **NOT** covered — all 21 of each are pairwise distinct and still require per-lesson examination | `QUARANTINE_REGISTER.md` Q-001…Q-004; `V04_REVIEW_R1.md` | OPEN — informational, no action owed |
| 34 | V04 R2 | **`m1` — the *"§3.3 windows are identical"* justification is true for one window and false for the other** (`E20`). Both `V04_HOMEWORK.md` §1.2 (M1 correction block) and `V04_MASTERY_REPORT.md` §"Was any conclusion affected?" state that *"the extreme's index and the 44-bar window shifted together by exactly four bars, so the bars examined are the same bars"*. True for USDCHF's **high**-side window (`j_hi` 363→359, bar-for-bar identical); **false for the low-side one** — `j_lo` 4→0 was clipped at the head of the array in **both** datasets, so it went from 5 bars (four of them previous-week bars) to 1 and could not "shift". **The descriptor row it justifies is genuinely unchanged — 1/1/1/1 across all four tolerances on both datasets, recomputed at R2** — the direction is safe (the new window correctly excludes out-of-week bars) and nothing downstream reads the justification. Charged because it is one more instance of R1's `N5` pattern, produced in the commit that quoted `N5` approvingly | `V04_HOMEWORK.md` §1.2; `V04_MASTERY_REPORT.md`; `18_REVIEW/V04/V04_REVIEW_R2.md` §4 | 🔧 **OPEN — NON-BLOCKING, deferred by design.** Fix the mechanism clause whenever either file is next edited: the high-side window is bar-for-bar identical; the low-side window was clipped at the array head in both datasets and now correctly excludes the four previous-week bars it previously contained; both descriptor rows are unchanged, recomputed. **Do NOT open an R3 for this** — `REVIEW_PROTOCOL.md` §9 criterion 14 and the `V02_REVIEW_R3.md` precedent (`PASS` with non-blocking documentation-precision minors); §16 forbids the artificial extra round |
| 35 | V05 student pass | **`A-042` — AN OUT-OF-CORPUS DEPENDENCY. Owner decision needed, not a reviewer finding.** The V05 presenter defers the operative detail for **levels and reset** `[00:10:51]`, **what makes a pattern nameable and how big railroad tracks must be** `[00:26:45]`, **traps** `[00:56:48]` and **signature trades/checklists** `[00:33:17]` to the **DMR** — a separate programme with its own video library that **this repository does not contain**. Four of those are questions the bootcamp has left open across five lessons. **If this testimony holds, some `A-xxx` records are unresolvable from this corpus IN PRINCIPLE, not merely unresolved so far** — and the project currently has no vocabulary for that state. `D-019` separates `NOT APPLICABLE` from `DEFERRED`; neither describes "the source that would answer this is not in the library". **Explicit warning attached to the record: an unavailable source is a reason to leave a record OPEN, never a reason to infer what it said** (`D-008`, `D-010`) | `AUTOMATION_AMBIGUITIES.md` `A-042`; `V05_INTERPRETATION.md` §2.3 | OPEN — **owner decision** |
| 36 | V05 student pass | **A THIRD DISPOSITION may be needed for work EXCLUDED BY DECISION.** `D-018` grants `NOT APPLICABLE` for lessons stating **no testable rule**; `D-019` insists `NOT APPLICABLE` ≠ `DEFERRED` and that `D-018` grants only the first. **V05 is a third case neither contemplates:** it *states* several testable-shaped rules and they are **withheld by `D-025`**. `DEFERRED` is wrong — deferral implies the work becomes possible later, and **no future lesson makes a V05 guest rule testable**. Dimensions **F** and **G** were graded on a *purposive* reading of `D-018` with the *strict* reading flagged, and **this is the sole reason V05 is submitted `REVIEW REQUIRED` rather than `PASS`** | `V05_MASTERY_REPORT.md` §F, §G, Escalation; `DECISIONS.md` D-018, D-019, D-025 | ⚖️ **RULED 2026-08-11 at V05 R1 — OPEN only on the owner's adoption step.** The escalation is **upheld: the project needs a third disposition and V05 is the lesson that proves it.** Neither label fits work permanently excluded by decision — `NOT APPLICABLE` says *there was never anything here* (false; there is an hour of it), `DEFERRED` says *this becomes possible later* (false; it never does). **Dimension G's `NOT APPLICABLE` is UPHELD** on the purposive reading, because `DEFERRED` would be affirmatively false — no future lesson makes a V05 guest rule testable — **but its stated reason must change** from *"states no testable rule"* to *"states rules excluded by D-025"*, or V06–V21 will inherit the wrong precedent. **Dimension F is UPHELD as graded** (`SUCCESS AFTER SOURCE REVIEW`): it correctly refuses `NOT APPLICABLE`, since the assignment is partly performable and the performable part was performed on real data. **Dimension B's `NOT APPLICABLE` is NOT AVAILABLE** — `D-019`'s table grants it for dimensions **F and G only**; this is the same mis-disposition as V04 R1 `N1` and is carried the same way, as a **NOTE with a required action**, because the prose beneath the label is accurate. **Reviewer recommendation to the owner: adopt `EXCLUDED BY DECISION`** — subject matter exists; the work is permanently barred by a numbered decision, which must be cited; the item closes like `NOT APPLICABLE` and accrues no debt; the record states *what* was excluded and *under which decision*, so the exclusion is auditable rather than invisible; available to **any** dimension. On adoption, V05's **B** and **G** take it and **F** stays as graded. **This ruling does not hold the gate** — it is a vocabulary gap in the project's own standards, not a defect in V05's understanding, and the student diagnosed it correctly and declined to resolve it unilaterally |
| 37 | V05 student pass | **`A-049` — the stop-hunt vs trap-move discriminator is the highest-priority research question the project now carries.** V05's guest gives a clean two-limb test — **close beyond the level vs pin beyond without closing**, plus **immediate directional shift vs continued oscillation** — for two objects the instructor uses constantly across V01–V04 and has **never distinguished on the record**. It is `GUEST` material and **excluded**. Standing question for V06–V21: **does the instructor ever draw this distinction himself?** If he does, his statement becomes the record and this becomes corroboration; if no lesson does, the project must state that the corpus does not contain the distinction. **Named failure mode:** a future session reconciling this with an instructor passage would manufacture a rule neither man stated and would feel like good scholarship doing it | `AUTOMATION_AMBIGUITIES.md` `A-049`; `V05_SOURCE_NOTES.md` §5h | OPEN — carry to every remaining lesson |
| 38 | V05 student pass | **SPEAKER IDENTIFICATION MUST BE THE FIRST STEP OF EVERY REMAINING LESSON — evidenced, not just asserted.** Instructor runtime across the single 2012-03-25 session date runs **~100% (V03) → ~31% (V04) → 0% (V05)**. `D-025` consequence 3 already mandates speaker tagging; V05 shows the cost of skipping it — **a session that assumed V05 was the instructor would have written an entire lesson of false doctrine, and every downstream file would have inherited it.** Whether the trend is structural (a multi-presenter programme) or incidental (one long day split among coaches) is **not settled**, and the actionable consequence holds either way | `V05_INTERPRETATION.md` §3; `DECISIONS.md` D-025 | OPEN — informational, standing procedure |
| 39 | V05 student pass | **A correction issued against two ALREADY-COMMITTED files, recorded rather than silently patched.** `V05_TRANSCRIPT.md` § TRANSCRIPTION NOTES and `QUARANTINE_REGISTER.md` `Q-005` both state *"`EMA` occurs 3 times"*. **The literal token occurs twice** (verbatim body, word-boundary, case-sensitive; body lines 1271 and 3944); the third item in the transcript's own list, *"closing below the 200"* `[01:06:02]`, does not contain the token. **No conclusion in either file changes** — the point both were making (no 5/13/800 EMA, no colours or nicknames) is unaffected and re-confirmed. Logged in `V05_SOURCE_NOTES.md` §7 for the reviewer to disposition; a correction that leaves no trace is worse than the error | `V05_SOURCE_NOTES.md` §7 note 1 | ✅ **CONFIRMED 2026-08-11 at V05 R1 — the fix location is `V05_TRANSCRIPT.md` § TRANSCRIPTION NOTES and `Q-005`.** Re-measured independently (word-boundary, case-sensitive, verbatim body): **`EMA` occurs exactly twice** — `[00:23:52]` *"Nice close below the 50 EMA."* and `[01:05:53]` *"…below the 200 EMA."* The third item in the transcript's own list, *"closing below the 200"* `[01:06:02]`, is present and **does not contain the token**. **The student is right, and logging the correction rather than silently patching was the correct call.** No conclusion in either file changes: the point both were making is independently re-confirmed here — `5 EMA` **0**, `13 EMA` **0**, `800` **0**, `mayonnaise` **0**, `mustard` **0**, `water` **0**. **Required:** correct both files in place, retaining the superseded text per `REMEDIATION_PROTOCOL.md` §2. ✅ **CLOSED — APPLIED AND VERIFIED at V05 R2 2026-08-11.** The count was re-derived a third time before any edit (`grep -n -w EMA`, verbatim body only: body lines 1271 and 3944 — the same two the student found) and then corrected at both sites with the superseded text retained. **Applied by the R2 reviewer session on explicit owner instruction — a declared `D-003` deviation, scoped to two numerals and recorded at `V05_REVIEW_R2.md` §3.1.** `A-020`'s V05 row already stated *"twice"* and needed no change |
| 41 | V05 R1 | **`M1` (`E11`) — the same quote is cited at two different wrong timestamps, neither a marker.** *"I use the trend line. I use E and I use the box."* is at **`[00:57:35]`–`[00:57:36]`**; `V05_SOURCE_NOTES.md` §3b cites `[01:07:36]` and `A-043`'s evidence table cites `[01:01:35]`. The quotation is accurate; only the citations are wrong, and being wrong two different ways means neither was checked against the other. **`A-043`'s closure does not rest on this row** — it rests on the toolbar dialog, verified at pixel level at R1 | `V05_SOURCE_NOTES.md` §3b; `AUTOMATION_AMBIGUITIES.md` `A-043`; `V05_REVIEW_R1.md` M1 | ✅ **CLOSED — VERIFIED at R2 2026-08-11**, re-derived from `V05_TRANSCRIPT.md` and the committed PNGs rather than from the remediation diff. Both citations corrected to the marker the words actually carry. `V05_SOURCE_NOTES.md` §3b now cites *"I use E"* at **`[00:57:36]`** (was `[01:07:36]`); `A-043`'s evidence table now cites **`[00:57:35]`–`[00:57:36]`** (was `[01:01:35]`) and splits the fragment across the two markers it spans — `[00:57:35]` *"I use the trend line."*, `[00:57:36]` *"I use E and I use the box."* Both re-verified against `V05_TRANSCRIPT.md`. **`A-043`'s closure is untouched**; it rests on the toolbar dialog, not on this row |
| 42 | V05 R1 | **`M2` (`E11`) — citation off by one marker.** `A-039`'s V05 extension row cites `[00:36:03]` for *"looking for shorts, the trend line goes on the top and on the top"*; `[00:36:03]` reads *"I can start drawing my trend line."* and the quoted words are at **`[00:36:05]`**. Open item 7's class — the passage marker rather than the sentence's first words | `AUTOMATION_AMBIGUITIES.md` `A-039`; `V05_REVIEW_R1.md` M2 | ✅ **CLOSED — VERIFIED at R2 2026-08-11**, re-derived from `V05_TRANSCRIPT.md` and the committed PNGs rather than from the remediation diff. `A-039`'s V05 extension row now cites **`[00:36:05]`** and quotes that marker's literal text — *"So I'm going, I'm looking for shorts, the trend line goes on the top and on the top."* — rather than a smoothed fragment under the preceding marker. `[00:36:03]` (*"I can start drawing my trend line."*) verified as the adjacent, different sentence |
| 43 | V05 R1 | **`M3` (`E01`) — a smoothed quotation.** `V05_SOURCE_NOTES.md` §4b quotes *"**the** second leg of that pattern, that three hits to the high"* `[00:13:05]`; the transcript reads *"…and **level three** second leg of that pattern…"*. Same class as V04 `M2`, and again in supporting prose rather than the notes proper — but the passage is the file's evidence for the **level↔day relabelling** and the excised words are a level number | `V05_SOURCE_NOTES.md` §4b; `V05_REVIEW_R1.md` M3 | ✅ **CLOSED — VERIFIED at R2 2026-08-11**, re-derived from `V05_TRANSCRIPT.md` and the committed PNGs rather than from the remediation diff. The elision was **not** marked; the literal wording was **restored**, and the sentence boundary the ellipsis had hidden is now explicit — `[00:13:05]`–`[00:13:12]` *"So the consolidation and level three second leg of that pattern, that three hits to the high."* and `[00:13:13]` *"That's the third type, I guess the third leg begins your level one drop."* The excised level number is back in the file's evidence for the level↔day relabelling. **No conclusion in §4b changes** — the relabelling claim is carried by `[00:12:50]` and `[00:12:57]`–`[00:13:03]`, both unaltered |
| 44 | V05 R1 | **`M4` (`E20`) — three V05 files disagree about V05's own evidence order.** `04_SCREENSHOTS/V05/INDEX.md` discloses, prominently and unprompted, that *"that order was **not** preserved for V05"* and that the audio-only separation is *"**weaker** for V05 than for V01–V04"*; `V05_INTERPRETATION.md` line 12 says V05 *"**restored** the recipe's evidence order that V03 and V04 deviated from"*. Opposite claims about the same fact, and the interpretation's is the self-flattering one. **Fix the interpretation; do NOT weaken the `INDEX.md` disclosure to match** | `V05_INTERPRETATION.md` line 12; `04_SCREENSHOTS/V05/INDEX.md`; `V05_REVIEW_R1.md` M4 | ✅ **CLOSED — VERIFIED at R2 2026-08-11**, re-derived from `V05_TRANSCRIPT.md` and the committed PNGs rather than from the remediation diff. `V05_INTERPRETATION.md`'s Screenshots row now states, first and in bold, that **the recipe's evidence order was NOT preserved for V05**, names `INDEX.md`'s § "⚠ PROCESS DEVIATION, DISCLOSED" as **the governing statement**, gives the cause, and carries `INDEX.md`'s own consequence — the audio-only / visual-corroborated separation is **weaker for V05 than for V01–V04**. What *was* held (source notes §§1–8 from transcript only, visuals confined to §9, one disclosed pre-sweep sanity frame) is stated as a partial, not as restoration. Superseded text retained beneath the table per `REMEDIATION_PROTOCOL.md` §2. **`04_SCREENSHOTS/V05/INDEX.md` was NOT edited** — the disclosure is verbatim as R1 found it |
| 45 | V05 R1 | **`M5` (`E20`) — a stale pointer inside `A-039`.** It still reads *"The promised TDI lesson. V05 … is the next candidate."* V05 has now been studied and did **not** define TDI. **Eighth instance of the status-staleness class (open item 14) — and the only one this round**; see `N5`, the first round in which the four status blocks were all current | `AUTOMATION_AMBIGUITIES.md` `A-039`; `V05_REVIEW_R1.md` M5 | ✅ **CLOSED — VERIFIED at R2 2026-08-11**, re-derived from `V05_TRANSCRIPT.md` and the committed PNGs rather than from the remediation diff. `A-039`'s *Required Research* now records that **V05 was checked and did NOT define TDI** — it supplies the first *displayed* name (`TDI_MMM`, frame `V05_00-36-54`) and the first slide titled to mark the panel up, but no inputs, periods, bands, line names or decision rule; **a name is not a definition**. **V06 (or any later lesson) is named as the next candidate.** Superseded text retained per `REMEDIATION_PROTOCOL.md` §2. Record stays **OPEN** and `DO NOT CODE` |
| 46 | V05 R1 | **`M6` (`E20`) — an unrecorded oscillator sub-panel in curated frame 26.** `V05_00-40-04` renders a multi-line sub-panel of the same family the index records carefully on frames 19–21; the frame-26 row describes the frame down to the taskbar clock and a 9× status-bar read and does not mention it. **Directly the V04 `M6` class, whose precedent is binding.** R1 magnified the header and confirms it is at the edge of legibility and **should not be transcribed**. Record scoped *"displayed, not taught; header not legible"* in `INDEX.md` and in `A-039`'s extension row. **It does NOT narrow `A-039`** (`D-025`) | `04_SCREENSHOTS/V05/INDEX.md` frame 26; `A-039`; `V05_REVIEW_R1.md` M6 | ✅ **CLOSED — VERIFIED at R2 2026-08-11**, re-derived from `V05_TRANSCRIPT.md` and the committed PNGs rather than from the remediation diff. Frame 26's row in `04_SCREENSHOTS/V05/INDEX.md` now records the multi-line oscillator sub-panel beneath the price pane, scoped **"displayed, not taught"**, noting the presenter neither points at nor discusses it at `40:04`. The header sits in the same position as frame 21's `TDI_MMM` header and is **deliberately NOT transcribed** — presence only, at the edge of legibility, the same call frame 27's OHLC row gets. Added to `A-039`'s extension row on the same terms. **It does NOT narrow `A-039`** (guest material, `D-025`) |
| 40 | V05 student pass | **`A-043` is the project's first ambiguity closed on GUEST evidence, and the precedent is deliberately narrow.** The MT4 text tool is settled by the displayed *Customizing toolbar* dialog: MT4 carries exactly two text objects whose icons are the literal letters **`A`** (`Text`) and **`T`** (`Text label`), so *"use the one that says A, don't use the one that says T"* means **use `Text`**, and the transcript's *"E"* is a mishearing of *"A"*. **Claimed basis:** the record concerns a **platform artifact**, not methodology, and closes an ambiguity about **this lesson's own ASR** rather than about the method — so no instructor record is closed on guest evidence and no precedent for that is claimed. **A reviewer who disagrees should downgrade it to `EXTENDED, NOT CLOSED`; nothing downstream depends on it** | `AUTOMATION_AMBIGUITIES.md` `A-043`; `04_SCREENSHOTS/V05/INDEX.md` frame 4a | ⚖️ **AFFIRMED 2026-08-11 at V05 R1 — closure UPHELD, not downgraded; OPEN only on the owner's recording step.** The evidence was verified at the pixel level on the 2× re-render and is exactly as described: MT4's *Customizing toolbar* dialog carries two text objects — **`A Text`** in *Selected* (icon: a plain letter A) and **`T Text label`** in *Available* (icon: a boxed T). *"Just use the one that says A. Don't use the one that says T."* therefore means **use `Text`**, and the transcript's *"one that says E"* is an ASR mishearing of *"A"*. **Why `D-025` does not bar it, stated as a class rather than a one-off excuse:** D-025 bars guest evidence from closing records *about the method*, because that would give a guest's normative claims operative standing. `A-043`'s subject is **which button this speaker's own mouth referred to** — a question about *this lesson's ASR* and *a platform artifact*, answered by a screenshot of a dialog box. Closing it promotes no guest statement into doctrine and nothing downstream depends on it. **Ruling: a record whose subject is a guest's own utterance or a platform artifact, and not the method, may be closed on descriptive guest evidence; a record about the method may not be, ever, however clear the guest evidence.** `A-020`, `A-039`, `A-032`, `A-018`, `A-010`/`A-011` and `A-019` sit on the far side of that line and the student correctly left every one open. **Owner action:** record the carve-out as a numbered refinement of `D-025` — D-025's own "Alternatives considered" rejected *case-by-case adjudication with no standing rule*, and the student's per-record justification is exactly that even though it reaches the right answer. Writing the class down converts a good judgement call into an enforceable rule. **Recording step only; the finding stands either way** · ✅ **CLOSED — MOOT, 2026-08-13.** `D-033` reverses `D-025`'s normative exclusion outright: guest material may now close any record, method or otherwise. A numbered carve-out is an exception to a bar that no longer exists. `A-043`'s closure **stands** and no longer needs the special argument. The general ruling quoted here — *"a record about the method may not be closed on guest evidence, ever"* — is **superseded** |
| 47 | V05 R1B (adopted at R2 as `M7`) | **`M7` (`E20`) — `C-003` is named four times for a check that belongs to `C-004`.** The V05 check actually performed and struck off is `C-004` — *"London session open: 3:30am printed against 4:00 spoken"* — and it is written correctly inside the `C-004` record. **`C-003` is *"Whether M and W formations can fail"*; it contains no V05 text at all and names no next candidate.** Four sites name the wrong record: `CONTRADICTIONS.md` line 23 (**the STATUS block**), lines 845 and 846, and `V05_MASTERY_REPORT.md` §J. A future session reading the status block learns that the *"M's and W's will not fail"* record was tested against V05 and came back negative — **it was never tested.** Same class as V04 R1's `M3`. The underlying check reproduces exactly and `C-004`'s disposition does not move. **`V05_REVIEW_R1.md` §6 dimension O carries the same error and must NOT be edited** (`REVIEW_PROTOCOL.md` §11); it also retires R1's `N5` superlative that *"all four status blocks are current"* | `CONTRADICTIONS.md` lines 23, 845, 846; `V05_MASTERY_REPORT.md` §J; `V05_REVIEW_R1B.md` `m1`; `V05_REVIEW_R2.md` `M7` | ✅ **APPLIED 2026-08-11; VERIFIED CLOSED at R3 2026-08-12 (`V05_REVIEW_R3.md` §1, re-derived from source).** All four sites now name **`C-004`**: `CONTRADICTIONS.md`'s STATUS block, the two sentences in § "V05 PASS", and `V05_MASTERY_REPORT.md` §J. Superseded text retained at each location per `REMEDIATION_PROTOCOL.md` §2, each naming `C-003` as the wrong record and stating that `C-003` (M/W failure) contains no V05 text and was never tested. **The check itself does not move** — V05 contains zero clock times and `C-004` stays `UNRESOLVED`. **`V05_REVIEW_R1.md` was NOT edited** (`REVIEW_PROTOCOL.md` §11) |
| 48 | V05 R1B (adopted at R2 as `M8`) | **`M8` (`E01`) — a verbatim string quoted with a count the string does not support.** `V05_MASTERY_REPORT.md` §E records the day count's escape clause *"but up to five days"* as occurring **four times**. **The literal string occurs twice**, at `[00:11:11]` and `[00:24:37]`; *"five days"* occurs four times, but `[00:11:16]` (*"sometimes five days depending"*) and `[00:12:39]` (*"Remember three to five days"*) do not contain the quoted words. **Third live instance of the project's verbatim-count class** — with open item 15 (V02 *"level count"*) and open item 39 (`EMA`, closed at R2). The generative rule is identical every time: **a count asserted over a string inside quotation marks, without re-measuring the string.** Three instances is `REVIEW_PROTOCOL.md` §7's systematic-weakness threshold — raise at `CUMULATIVE_25.md` | `V05_MASTERY_REPORT.md` §E; `V05_REVIEW_R1B.md` `m2`; `V05_REVIEW_R2.md` `M8` | ✅ **APPLIED 2026-08-11; VERIFIED CLOSED at R3 2026-08-12 (`V05_REVIEW_R3.md` §1, re-derived from source).** `V05_MASTERY_REPORT.md` §E now reads *"**twice verbatim**, `[00:11:11]` and `[00:24:37]`; the day-count expectation itself is stated four times"*. Re-measured this session before the edit: the literal string *"but up to five days"* occurs **2**, *"five days"* occurs **4**. Superseded text retained, naming the two non-matching hits and pointing at `V05_SOURCE_NOTES.md` §4c as the origin (`M10`). The exception is still recorded and the §E grade does not move |
| 49 | V05 R1B (adopted at R2 as `M9`) | **`M9` (`E20`) — unrecorded printed `R =` labels in curated frame 26, and `A-018` undercounts.** `V05_00-40-04` carries **four printed `R = <number>` labels** on its cyan boxes, confirmed at R2 by magnification: three legible (`R = 40.9`, `R = 40.6`, `R = 41.1`) and one **partly occluded by the moving-average line** (`R = 7?.6`, most consistent with `74.6` — R1B read it flat as `74.6`; **R2 corrects that to a scoped reading**). `INDEX.md`'s frame-26 row records none of them despite describing the frame down to a taskbar clock. `A-018`'s V05 row lists only the four **slide** labels and concludes *"V05 adds four more labels"* — **V05 adds at least eight**, and the unrecorded four are the *stronger* evidentiary class because they are auto-rendered on the presenter's **live MT4 platform**, which is exactly the proposition `A-018` accumulates. **It does NOT narrow or close `A-018`** — guest material, `D-025`, and V05 states no stop and no target. Stays `DO NOT CODE`. Same class as R1's `M6`, in the same frame | `04_SCREENSHOTS/V05/INDEX.md` frame 26; `A-018`; `V05_REVIEW_R1B.md` `m3`; `V05_REVIEW_R2.md` `M9` | ✅ **APPLIED 2026-08-11; VERIFIED CLOSED at R3 2026-08-12 (`V05_REVIEW_R3.md` §1, re-derived from source).** Frame 26 was **re-opened and magnified by this session** (16× nearest-neighbour and 16× LANCZOS) rather than taken from either review's prose. Four `R = ` labels confirmed: **`R = 40.9`** (upper-centre), **`R = 40.6`** (centre-right), **`R = 41.1`** (lower-right) all legible, and a **fourth at the left where `R = ` is legible but the value is NOT** — the cyan moving average runs directly through the digits and only a trailing glyph separates. **R2's correction of R1B is upheld: `74.6` is not supportable from this PNG and is NOT transcribed**, per the frame-27 / V04 `M6` precedent. Recorded in `INDEX.md` row 26 and in `A-018`'s V05 row, scoped *printed, not spoken; live platform; three values legible, one not*; *"four more labels"* → **"at least eight"**. Superseded text retained. **`A-018` is extended, not narrowed** — stays `DO NOT CODE` |
| 50 | V05 R1B (adopted at R2 as `M10`) | **`M10` (`E02`) — a framing sentence over-generalises its own table.** `V05_SOURCE_NOTES.md` §4c heads its four-row table *"Repeated four times, **always with the same escape clause**"*. **Two of the four rows carry no escape clause**, in the quoted text or its neighbourhood — `[00:15:47]` and `[00:16:35]`, verified at R2 by reading the surrounding markers. The rows are accurate; the sentence above them is not. **This is `M8`'s origin** — the generalisation hardened into a false verbatim count one file downstream in the mastery report, which is `REVIEW_PROTOCOL.md` §17 failure mode 3 in miniature. Charged separately because this is where it starts | `V05_SOURCE_NOTES.md` §4c line 251; `V05_REVIEW_R1B.md` `m4`; `V05_REVIEW_R2.md` `M10` | ✅ **APPLIED 2026-08-11; VERIFIED CLOSED at R3 2026-08-12 (`V05_REVIEW_R3.md` §1, re-derived from source).** §4c's framing sentence now reads *"Repeated four times; **two of the four carry the explicit "up to five days" escape clause**"*, and the table gains an **Escape clause** column recording ✅ / ❌ per row with the adjacent markers quoted for the two negatives (`[00:15:52]`/`[00:15:55]` and `[00:16:36]`/`[00:16:39]`). Superseded text retained, naming this sentence as `M8`'s origin. The four rows were and remain individually accurate; no conclusion in §4c changes |
| 51 | V05 R1B (adopted at R2 as `M11`) | **`M11` (`E11`) — a third citation in the same wrong-offset cluster, escalated from `NOTE` to `MINOR` at R2.** `AUTOMATION_AMBIGUITIES.md` `A-042` cites `[01:01:39]` for *"for the DMR, I kind of use the ellipse to show the moving average crossover"*; **`[01:01:39]` is not a marker** and the words are at **`[00:57:39]`**. All three of V05's defective citations map `00:57:3x` → `01:0x:3x` — `[01:01:35]` (`A-043`), `[01:07:36]` (§3b), `[01:01:39]` (`A-042`) — which is **one bad offset applied to a neighbourhood, not three independent slips**, so R1's `M1` fix closed two thirds of a single defect. R1B graded it a note only because it filed it alongside `M1`; on its own merits it is a nonexistent-marker citation in a live register, which is what `M1` and `M2` were charged as. **Required with the fix: a mechanical marker-existence sweep of every `[hh:mm:ss]` citation in the V05 artifacts**, to confirm no fourth cluster member survives — R1 hand-checked 356 citations and missed this one | `AUTOMATION_AMBIGUITIES.md` `A-042`; `V05_REVIEW_R1B.md` `n1`; `V05_REVIEW_R2.md` `M11` | ✅ **APPLIED 2026-08-11; VERIFIED CLOSED at R3 2026-08-12 (`V05_REVIEW_R3.md` §1, re-derived from source).** `A-042`'s evidence table now cites **`[00:57:39]`** and carries that marker's literal sentence — *"And obviously for the DMR, I kind of use the ellipse to show the moving average crossover"*. **The required mechanical sweep was run and is CLEAN:** every `[hh:mm:ss]` citation on a V05-attributed line across `AUTOMATION_AMBIGUITIES.md`, `CONTRADICTIONS.md`, `V05_SOURCE_NOTES.md`, `V05_INTERPRETATION.md`, `V05_MASTERY_REPORT.md`, `04_SCREENSHOTS/V05/INDEX.md` and `05_HOMEWORK/V05/` was matched against the 1,353 markers in `V05_TRANSCRIPT.md`. **No fourth cluster member exists** — the only non-resolving hits are six explicit V01/V02/V04 cross-citations and one slide timecode (`CONTRADICTIONS.md` line 850, `(slide, [00:15:49])`, frame 11's own burned-in time), none of which is a V05 marker citation. The displaced cluster is closed at three |

> ✅ **MERGE NOTE RESOLVED 2026-08-12 (owner instruction).** Two lines of work branched from
> `3a13441` and each appended rows starting at **34**. The upper block (**34–51**, V04 R2 / V05
> student pass / V05 R1 / V05 R1B) **keeps its numbers** — it is the more heavily cited
> (`LOG.md` *"open item 34/36/39"*, the V05 review files, `COURSE_PROGRESS.md`). The lower
> block (backtest-evidence-standard lineage, `D-026`…`D-031`, `PT-001`) is **renumbered
> 34→52, 35→53, 36→54, 37→55, 38→56**, and its citing references were updated in the same
> pass: `CHANGELOG.md` (the `[0.7.2]` entry) and `LOG.md` (the D-028/029/030 and D-031
> session entries). No row's content was altered. The original note read: *"DUPLICATE ITEM
> NUMBERS 34–38, OWNER RECONCILIATION OWED … Neither block was renumbered on merge …
> Renumbering either side would silently break live cross-references."*

| 52 | External methodological review 2026-08-11 | **Baseline + pre-registration standard adopted (`D-026`/`D-027`, `BACKTEST_EVIDENCE_STANDARD.md`).** The four-lesson manual-backtest debt is now owed under it: each discharged test needs a pre-registered period and a matched random-entry baseline, exactly as a fresh test would. **Reviewer must audit checks 15-20 on the first discharged test.** Where the sample permits, V04's inside-box vs outside-box contrast is the course's own natural control and should be run | `BACKTEST_EVIDENCE_STANDARD.md`; `REVIEW_PROTOCOL.md` §6.G 15-20 | OPEN |
| 53 | Same | **Owner owed two decisions before the first `BT_` file.** ✅ **CLOSED 2026-08-11** — `D-028` (70/30 development/holdout, exact dates pinned at first data-source decision) and `D-029` (baseline parameters: 1,000 iterations, seed recorded, matched window, direction-matched primary + random-direction secondary arm). `OWED NOW` markers cleared | `DECISIONS.md` D-028, D-029 | ✅ CLOSED |
| 54 | Owner direction 2026-08-11 | **`D-030` — blocked tests wait for the course; definitions are never approximated.** Generalizes `A-039`'s TDI prohibition to every definitional blocker (`A-011` M/W anatomy, `A-004` the level, `A-002` trap move, `A-019` timezone). Manual-backtest debt will keep accruing and **that is correct behaviour**, not a backlog to clear by lowering the standard. Reviewer: treat an approximated definition inside a test as `E06`+`E18`, **CRITICAL** | `DECISIONS.md` D-030 | OPEN — standing |
| 55 | Owner request 2026-08-11 | **`PT-001` — the one test available before the course teaches more.** Pre-registered at `06_MANUAL_BACKTEST/PRE_REGISTERED/PT-001_asian_range_predictive_content.md`: does the Asian range boundary carry predictive content? No pattern recognition, no indicator — the box is pure measurement. Tests the **load-bearing premise** under V04's prohibition, V03's accumulation phase and condition (a). ~~Blocked by `A-019`~~ **— UNBLOCKED 2026-08-11 by `D-031`'s two-arm timezone design.** Remaining prerequisites are `I-007` (data source) and the `D-028` boundary dates — and unlike the other blockers this plausibly closes from existing V01–V05 evidence rather than a future lesson (V04 `[00:07:01]` Eastern; V01 `[00:46:09]` US session 9:30 Eastern; but `C-004` warns session times in this course are messy). **Prerequisite work item: a focused timezone evidence pass.** Do NOT assume Eastern to unblock it (`D-030`) | `PT-001…md`; `A-019`; `C-004` | ⚠️ **PREREQUISITES DISCHARGED 2026-08-13 — and a new one appeared.** `I-007` CLOSED (`D-034`); `D-028` boundary PINNED at 2016-07-01 (`D-035`); `PT-001`'s window `W-A` **conforms**. **Still blocked by DATA AVAILABILITY**: the declared feed serves 15m GBP/USD back only to 2026-05-31, and `W-A` is 2015. `D-035` records the three exits and they are the **owner's** to choose. **OPEN — owner flagged, do not lose** |
| 56 | Owner direction 2026-08-11 | **`D-031` — session timezone is a TESTED VARIABLE, two arms, both always reported.** Arm A fixed `UTC−5`; Arm B DST-aware `America/New_York`. **Reviewer must check that BOTH arms are reported** on any session-dependent test — reporting only the better one is `E09`+`E24`. Fact of record: the bootcamp ran 2012-03-18→06-17, entirely inside US DST, so **Arm B reproduces the instructor's own stated times and Arm A displaces them by an hour**; this is evidence about the source and does not settle which reading the method needs. `A-019` remains **OPEN** — `D-031` governs project method, not course content, and may never be cited as instruction | `DECISIONS.md` D-031; `A-019`; `PT-001` §3 | OPEN — standing |
| 57 | V06 R1 | **`M1` (`E07`+`E11`, `MAJOR`) — frame `V06_00-48-29` Week 10 prints *"and more specifically at 3:45am or 9:45am est."*, legible at committed resolution, elided as "not legible" in the frame-26 transcription; its absence then asserted as *"no session clock appears on any of the 32 frames"* in `04_SCREENSHOTS/V06/INDEX.md` and `V06_SOURCE_NOTES.md` §11d.** First printed `est` in the corpus evidence; two fire times attached to the Brinks trade. Fix: complete the transcription (superseded text retained), correct both sentences, extend `A-019` and `A-030` with the printed evidence and its provenance (DMR syllabus, guest programme, printed not spoken), re-sweep the other 31 frames for elided-but-legible text. **Holds the V07 gate closed (`D-024`)** | `V06_REVIEW_R1.md` M1 | ✅ **CLOSED — APPLIED at `4c89db1`, VERIFIED at R2 2026-08-13** (`V06_REVIEW_R2.md` §1). Week 10 transcribed in full, both false sentences corrected, `A-019`/`A-030` extended, full-frame sweep run — the sweep surfaced `M5` (see E20 ledger), fixed in-round |
| 58 | V06 R1 | **`M2` (`E20`, count class) — transcript header "Steve 25× = 23 + 2" irreproducible: 26 tokens; third read-aloud instance `[01:11:39]` (Isubio quotation) unclassified.** Speaker conclusion unaffected and strengthened. Count class is at its escalation threshold (items 15, 39, 48) — raise at `CUMULATIVE_25.md` | `V06_REVIEW_R1.md` M2 | ✅ **CLOSED — VERIFIED at R2** (26 tokens with accounting; three read-alouds incl. `[01:11:39]`; re-measured, reproduces exactly) |
| 59 | V06 R1 | **`M3` (`E20`, count class) — `V06_SOURCE_NOTES.md` §10's once-corrected row still miscounts: `Asia` is 2× (`[00:50:25]`, `[01:09:55]`), not 1×.** Conclusion (Asian box undefined) unaffected | `V06_REVIEW_R1.md` M3 | ✅ **CLOSED — VERIFIED at R2** (`Asia` 2× with both markers cited; re-measured) |
| 60 | V06 R1 | **`M4` (`E20`, staleness class, item 14 lineage) — the `D-033` propagation (`612f431`) left the five live `D-025` fences in the V06 lesson artifacts untouched** (transcript header, source notes, interpretation, homework, screenshot index — each states superseded prohibitions in present tense). Fix: dated `D-033` notice under each fence, noting `D-030` still blocks the *push*-family material; with it, record the restated V06 corpus contribution under `D-033` (`V06_REVIEW_R1.md` §13.2). Error is conservative (over-restricts), hence MINOR | `V06_REVIEW_R1.md` M4, §13 | ✅ **CLOSED — VERIFIED at R2** (five dated `D-033` notices in place; `V06_INTERPRETATION.md` §9 delivers the §13.2 restatement, seven doctrine-eligible statements checked against markers, nothing promoted) |
| 61 | V07 R1 | **`M1` (`E20`, count class — items 15/39/48/58/59 lineage) — `V07_SOURCE_NOTES.md` §10 states the *level* count as 26 uses; it is 56, and §5 of the same file says 56 correctly.** Re-measured: `level` 53 + `levels` 3 = **56**; the `level <N>` compound is 35; entries containing the token are 44. **26 matches none of them.** The file therefore holds one right record and one wrong record for the same object fourteen sections apart — the V05 `M4` intra-file-disagreement class on top of the count class. **Conclusion unaffected and understated** (*level* is used constantly and never defined; `A-004` untouched); no other artifact cites 26. Charged because §10's preamble offers the counts *"so a reviewer can falsify them cheaply"*. **Fix:** correct §10's cell to **56** (or name the sub-count intended); **do NOT change §5**; retain superseded text | `V07_SOURCE_NOTES.md` §10, §5; `V07_REVIEW_R1.md` M1 | ✅ **APPLIED 2026-08-13 — PENDING VERIFICATION at R2.** §10's cell reads **56 uses** (`level` 53 + `levels` 3), re-derived from the verbatim body this session rather than taken from the review's prose (compound `level <N>` 35, entries containing the token 44 — all three re-measured, 26 matches none). **§5 not edited.** Superseded cell retained in a dated block beneath the table per `REMEDIATION_PROTOCOL.md` §2. Conclusion unchanged; `A-004` untouched. ✅ **CLOSED — VERIFIED at R2 2026-08-13** (`V07_REVIEW_R2.md` §1): re-derived by this reviewer from the verbatim body by **two independent methods** (Python `re` word-boundary and `grep -oiE`), both returning `level` **53** + `levels` **3** = **56**, over a body `wc -w` measures at exactly the stated **7,436** words. The two competing sub-counts were also re-measured — compound `level <N>` **35**, marker entries containing the token **44** — confirming 26 matches none of them. §5 verified unedited and still reading 56; `A-004` verified untouched |
| 62 | V07 R1 | **`M2` (`E20`, same count class) — `V07_SOURCE_NOTES.md` §10's *"the peak"* row says 4×, lists five markers, and the true count is 5.** The five markers listed (`[00:00:26]`, `[00:03:18]`, `[00:03:20]`, `[00:14:02]`, `[00:16:44]`) are **all correct**; only the number is wrong, so the row contradicts itself on its face. The row's `peak formation` / `PFH` / `PFL` zero counts are correct and its conclusion is unaffected. **Fix:** `4×` → **5×**; leave the marker list alone; retain superseded text | `V07_SOURCE_NOTES.md` §10; `V07_REVIEW_R1.md` M2 | ✅ **APPLIED 2026-08-13 — PENDING VERIFICATION at R2.** The row reads **5×**; re-measured from the verbatim body this session at exactly the five markers already listed. **Marker list unchanged**, `peak formation`/`PFH`/`PFL` zeros unchanged. Superseded cell retained in the same dated block as `M1` per `REMEDIATION_PROTOCOL.md` §2. Conclusion unchanged. ✅ **CLOSED — VERIFIED at R2 2026-08-13** (`V07_REVIEW_R2.md` §2): re-derived by two independent methods, both returning **5**, and this reviewer **enumerated** the occurrences rather than only counting them — they fall at exactly `[00:00:26]`, `[00:03:18]`, `[00:03:20]`, `[00:14:02]`, `[00:16:44]`, the five markers the row already listed, in that order. A separate sweep for the bare token `peak`/`peaks` returns the same five hits and no others, so no sixth use hides behind a different article. `peak formation` / `PFH` / `PFL` re-measured at **0 / 0 / 0** |
| 63 | V07 R1 | **`M3` (`E01` misquote, co-code `E11` wrong marker) — `V07_MASTERY_REPORT.md` §D alters a word inside quotation marks and cites the wrong marker, falsifying §H's own categorical integrity claim.** §D's Sequence table quotes *"if it doesn't do what you expect **and** your flashcard isn't the same"* at `[00:28:28]`; the transcript reads *"…**in** your flashcard…"* at **`[00:28:31]`**, and `[00:28:28]` exists carrying a different sentence (*"We'll say whether it's something that you will take."*). The `in` → `and` substitution is the *sensible* reading of a garbled ASR passage, which is exactly why it must not be made silently inside quotes (V04 `M2` / V05 `M3` class). **§H states, unhedged, *"No quotation mark in any V07 artifact contains a word that is not in the source"* — this is the instance that falsifies it.** Materiality to the method is nil: §D's grading does not turn on the word and `V07_SOURCE_NOTES.md` §6c renders the passage correctly. **Counterweight, measured by the reviewer:** 239 marker-cited quotes across seven artifacts were machine-checked and **this is the only defect**. **Fix:** restore *"in your flashcard"*, re-cite to `[00:28:31]`, and **in the same edit** repair or scope §H's sentence; **do NOT edit `V07_SOURCE_NOTES.md` §6c**; retain superseded text | `V07_MASTERY_REPORT.md` §D, §H; `V07_REVIEW_R1.md` M3 | ✅ **APPLIED 2026-08-13 — PENDING VERIFICATION at R2.** §D's Invalidates cell now reads *"If it doesn't do what you expect **in** your flashcard isn't the same"* cited to **`[00:28:31]`**, re-derived from `V07_TRANSCRIPT.md` this session. §H's categorical sentence **repaired, not merely scoped**: it now states that one such quotation existed, was found at R1 and is corrected. **The repair was earned by a fresh sweep, not assumed from the review's count** — every `*"…"*` fragment with an adjacent citation across all seven V07 artifacts re-matched against the transcript: **167 marker-cited quotes, zero remaining word-substitutions after the §D fix**; the nine flags raised were opened by hand and cleared (printed slide/chart text, a labelled **V04** quote, the student's own first reading, a hypothesised ASR alternative, and two explicitly-marked elisions). **`N2` folded into the same edit as the review directed** — §H's *"163 citations"* is recorded as true-when-measured and now stale (190 occurrences / 171 distinct; 182 / 168 excluding §11), with the cause named (§9b added after the sweep, following `R11`'s failure). **`V07_SOURCE_NOTES.md` §6c not edited.** Superseded text retained at both §D and §H per `REMEDIATION_PROTOCOL.md` §2. ⚠️ **PARTIALLY VERIFIED at R2 2026-08-13 — STAYS OPEN** (`V07_REVIEW_R2.md` §3). **The §D half is CLOSED, VERIFIED**: the transcript literally reads *"If it doesn't do what you expect **in** your flashcard isn't the same…"* at `[00:28:31]`, `[00:28:28]` carries a different sentence, the corrected cell matches both, and §6c and §5 were verified unedited. **The §H half is NOT VERIFIED.** R1 required the categorical sentence be *repaired or scoped*; the remediation repaired it, on the strength of its own sweep, to *"One quotation in the V07 set contained a word that is not in the source… no other instance exists"* — **and that is false. Three further instances exist**, two of them naming the very reconstructions §H claims were *"moved outside the quotes"*. **Carried forward as open item 70**; item 63 stays OPEN until 70 discharges. ✅ **CLOSED — VERIFIED at R3 2026-08-13** (`V07_REVIEW_R3.md` §3): item 70 discharged, so this item's §H half discharges with it. **The replacement claim was verified on its merits, not merely re-read.** §H no longer asserts completeness of a search — it states a **historical count** (*"Four quotations… One was found at R1 (§D, `[00:28:31]`); three more were found at R2 and are corrected here"*), which is arithmetically right, and it names committed, re-runnable evidence rather than a hand sweep. Its one surviving categorical residue — that reconstructions are outside the quotes or bracketed *"at **every** site"* — was tested by R3 **independently of the script**, by hand-searching all four of the script's precision bounds (§4b); nothing survives, so the claim is true. The §D half's verification at R2 was spot-re-checked and still holds: `[00:28:31]` reads *"If it doesn't do what you expect **in** your flashcard isn't the same…"* and §D cites it |
| 64 | V08 R1 | **`M1` (`E11`) — `C-009` Source A omits available corroboration.** The confirmation requirement is sourced only to the V08 speaker's own reported speech (`[00:37:07]`–`[00:37:16]`) thirty seconds before he calls it a myth. **V07 `[00:28:02]`–`[00:28:31]` attests the same requirement from a different lesson and a different equally-normative `GUEST`** (`V07_SOURCE_NOTES.md` §6c). **Required:** add the V07 citation to Source A as corroborating attestation, tagged `GUEST`, cross-referenced to §6c, with one sentence on what it changes. **Do NOT change the `PROVISIONAL` disposition** — it is upheld | `CONTRADICTIONS.md` C-009; `18_REVIEW/V08/V08_REVIEW_R1.md` M1 | ✅ **CLOSED — VERIFIED at R2 2026-08-13** (superseded status retained: this cell read `APPLIED 2026-08-13 — PENDING VERIFICATION at R2` between the remediation and R2). `C-009` gains a new **Source A′** block, tagged `GUEST`, citing **V07 `[00:28:02]`–`[00:28:31]`** with the four spoken lines quoted verbatim and cross-referenced to `V07_SOURCE_NOTES.md` **§6c**. **The citation was verified against `02_TRANSCRIPTS/V07/V07_TRANSCRIPT.md` in this session, not copied from the review** — the marked lines read *"Yes, David, it's tough to know when second legs will be above or below the first leg"* `[00:28:02]`, *"You can only go by the second rail tracks"* `[00:28:15]`, and the flashcard-pass sentences at `[00:28:17]`–`[00:28:31]`. `PROVISIONAL` **unchanged**; nothing in the original Source A is superseded, since the defect was an omission rather than an error. ⚠ **ONE CORRECTION TO THE REVIEW'S OWN WORDING, MADE DELIBERATELY AND FLAGGED FOR R2:** `M1` (and this item's description above) call V07's presenter *"a different equally-normative `GUEST`"*. **That is not established and the remediation does not repeat it.** `V07_SOURCE_NOTES.md` records V07 as *"a single unidentified presenter"*; `V08_SOURCE_NOTES.md` records V08's as unnamed (`D-033` provision 2); and V07/V08 are **Part 2 and Part 3 of the same day's bootcamp**, so they may be the **same** person. The added block therefore claims *a second **lesson***, not *a second **speaker***, and states that limit in its own text — as it does the narrower limit that V07 `[00:28:15]` attests the requirement **in use** rather than restating V08's two-candle specification. **R2 should adjudicate whether this narrowing is correct**. ⬛ **R2 VERDICT — VERIFIED, AND THE NARROWING IS ADJUDICATED CORRECT.** The citation was **read at source** in `02_TRANSCRIPTS/V07/V07_TRANSCRIPT.md`, not against the review: all four fragments verbatim, the `[00:28:28]` omission honestly marked with an ellipsis, and the `[00:28:31]` garble *"if it doesn't do what you expect **in** your flashcard isn't the same"* **preserved** — the precise passage V07's item 63 was charged for smoothing to *"and"*, avoided here in the one file where tidying it would have been easiest. `GUEST` tag ✅, `V07_SOURCE_NOTES.md` §6c cross-reference resolves ✅, *"what this changes"* paragraph present ✅, `PROVISIONAL` untouched ✅, Source A verbatim and purely additive ✅. **On the flagged narrowing:** a finding whose whole subject is under-sourcing must not itself assert an unverified claim, and the block's text — *a second **lesson**, not a second **speaker*** — contains **no false statement**; it under-claims, it does not mis-claim. **R2 then made the determination the remediation declined to make, and it SUPPORTS R1's framing — see new item 71 and `V08_REVIEW_R2.md` §2: the presenters ARE different men, `HIGH` confidence, textual evidence only.** No finding is charged for the deferral — charging one for correctly deferring to the reviewer, when the reviewer then resolves it, would penalise the discipline `REVIEW_PROTOCOL.md` §1 and §16 ask for |
| 65 | V08 R1 | **`M2` (`E20`) — a matched-random null's entry-PRICE convention was left to the runner.** `PT-034` §4 specifies what is held constant and what is randomized; the entry price is neither, and `run_pt034.py` fixes it to the bar's close. **Forward requirement only — `PT-034` must NOT be edited** (`COMMON_PROTOCOL.md` §9 rule 7, and the runner was committed before it ran). **Required:** state the null's entry-price convention in the parameter table of the next `PT-xxx` carrying a matched-random null, and record the requirement in `BACKTEST_EVIDENCE_STANDARD.md` or `COMMON_PROTOCOL.md` §5 so it binds future sessions rather than living only in a review | `BACKTEST_EVIDENCE_STANDARD.md`; `COMMON_PROTOCOL.md` §5; `18_REVIEW/V08/V08_REVIEW_R1.md` M2 | ✅ **CLOSED — VERIFIED at R2 2026-08-13** (superseded status retained: this cell read `APPLIED 2026-08-13 — PENDING VERIFICATION at R2` between the remediation and R2). Applied at **two** sites. (1) **`BACKTEST_EVIDENCE_STANDARD.md` §2.1a is new** — the null's entry-price convention is now a **required pre-registration field**, the §2.1 held-constant table gains an *Entry PRICE convention* row, the requirement to state it **even when it differs from the rule arm's** is spelled out, the specific bias it guards (giving a null its bar's low for a long / high for a short) is named, and an unstated convention is set at minimum a `MINOR` `E20` for reviewer enforcement. (2) **`06_MANUAL_BACKTEST/V08/BT_V08_0001.md` §5** — the results file, which is where §4's `O3` table's null actually lives — gains a dated block stating the convention forward: **`N1`/`N1b` enter at the chosen bar's CLOSE**, against a rule arm entering **extreme-anchored** at `LOD + X` (or the bar's low if that price is outside its range), with both traced to the functions that implement them (`precompute_close_entries()` / `entry_for()`) and a table making the asymmetry explicit. The rationale is stated so a reader can disagree with it, and the validating evidence is given: `N1` returned **0.2424–0.2450** against a closed-form break-even of **25.00%**, so the convention introduced no measurable bias. **`PT-034` WAS NOT EDITED and its §4 is byte-unchanged** — verified in `git diff`; `COMMON_PROTOCOL.md` §9 rule 7 binds a *completion* exactly as it binds a *correction*, and the block says so. **No result, table or value in `BT_V08_0001.md` is altered or superseded** — this is documentation of a convention that was fixed in committed code (`e3a8e66`) before the run (`1d206ab`); only its **location** was wrong, not its timing. ⬛ **R2 VERDICT — VERIFIED.** Both functions were **read**, not taken on the documentation's word, and both descriptions are **EXACT**: `precompute_close_entries()` calls `resolve(hi, lo, i, **cl[i]**, d, n)` — the entry price is literally the bar's close; `entry_for()` computes `want = lod + X*PIP` and returns `want if lo[i] <= want <= hi[i] else lo[i]`, with the `hod`/`hi[i]` mirror, exactly as the new asymmetry table states. **`PT-034` is genuinely untouched — verified independently, not accepted:** `git log --follow` shows **exactly one commit ever** (`a4ab65a`) and `git diff a4ab65a HEAD` on the file is **EMPTY**. The section-number correction the remediation flagged is **right**: `BT_V08_0001.md` §4 is `O3`, §5 is `O4` and is where `N1`/`N1b` actually sit. All four `N1` medians re-read from the committed output are **0.2450 / 0.2426 / 0.2424 / 0.2429** — the claimed `0.2424–0.2450` is **exact, not rounded to flatter** — the `BT_V08_0001.md` table reproduces all four rows and both intervals without error, and the closed-form break-even recomputes to **0.250037**. **§2.1a is a stronger instrument than R1 asked for:** R1 required the convention be stated; §2.1a also **names the bias it guards** (never give a null its bar's low for a long) and sets reviewer enforcement at *"at minimum a `MINOR` `E20`"*, telling a future reviewer what to do when it is absent. No number, table or value in `BT_V08_0001.md` changed — the file gains 48 lines and loses none |
| 66 | V08 R1 | **`M3` (`E19`) — a screenshot filename asserts `00:43:10` on a `00:43:03` recording**; the frame's own burned timecode reads `43:04`. The frame is genuine and its content claim (the literal `?`) is confirmed. **Required:** rename to `V08_00-43-04_end-card-innermost-stage-unanswered.png`, update `04_SCREENSHOTS/V08/INDEX.md` row 26 and the "What the frames settled" item 7 reference, and add a clause stating the frame is the post-playback end card — so V08's own screenshot set does not trip `Q-009`'s first recommended fabrication screen | `04_SCREENSHOTS/V08/INDEX.md`; `18_REVIEW/V08/V08_REVIEW_R1.md` M3 | ✅ **CLOSED — VERIFIED at R2 2026-08-13** (superseded status retained: this cell read `APPLIED 2026-08-13 — PENDING VERIFICATION at R2` between the remediation and R2). File renamed via `git mv` to **`V08_00-43-04_end-card-innermost-stage-unanswered.png`** (rename detected as `R` in Git, so the blob and its history are preserved). **All three prose references updated** — `04_SCREENSHOTS/V08/INDEX.md` row 26, its "What the frames settled" item 7, **and `V08_SOURCE_NOTES.md` §12 item 4**, which the review did not enumerate but which carried the same wrong timecode and was found by sweeping the repo for the old string. Row 26 now states the frame is the **post-playback end card** (`replay` button visible), making its relationship to the 00:43:03 runtime explicit. **The timecode was verified in this session, not taken on the review's word:** the PNG's bottom-right player chrome was cropped and magnified, and the burned-in elapsed field reads **`43:04`** (total field truncated at `43:0` by the frame edge). Old filename and all three old values are **retained by explicit naming** in a dated correction block in `INDEX.md` — `REMEDIATION_PROTOCOL.md` §2's retention requirement satisfied without an inline superseded passage, since a rename is a file operation rather than prose; `V08_SOURCE_NOTES.md` §12 additionally carries an inline `SUPERSEDED` bracket. ⚠ **ONE RESIDUAL FOUND BY THIS REMEDIATION AND DISCLOSED RATHER THAN GLOSSED, FOR R2 TO ADJUDICATE:** `00:43:04` is **2,584 s** and the runtime is **2,583.75 s**, so the *corrected* label **still exceeds the runtime, by 0.25 s**, and a naive implementation of `Q-009`'s screen will still flag row 26. This is unavoidable and is not a further defect — a player's whole-second elapsed field cannot print `43:03.75` and displays the ceiling, so the frame **cannot** carry both its true burned timecode and a strictly-under-runtime label; matching the artifact's own internal evidence is the correct choice. `INDEX.md` records the consequence for whoever implements the screen: **flag `timestamp > ceil(runtime)`, not `timestamp > runtime`**, or it false-positives on the legitimate final frame of any recording whose duration is not a whole number of seconds. Under that form `00:43:10` remains a true positive and `00:43:04` is not. **A mechanical sweep of all 26 V08 filenames confirmed row 26 was the only one over runtime**. ⬛ **R2 VERDICT — VERIFIED, INCLUDING THE TIMECODE ITSELF.** The reading was **not** taken on the remediation's word: this reviewer cropped the frame's player chrome at `(968,676)`–`(1024,688)`, linear-stretched it across its own dynamic range and magnified it 20×, and **read the pixels — the burned-in elapsed field reads `43:04`**, total field truncated at `43:0` by the frame edge. The frame's content claim was re-confirmed by opening the full PNG: four rings, three labelled thresholds, **a red `?` at the centre**, `replay` button — the post-playback end card. **All four references verified updated, and an INDEPENDENT repo-wide sweep for `43:10`/`43-10` confirms there is NO FIFTH** — every survivor is a `REMEDIATION_PROTOCOL.md` §2 retention block, the R1 review file (which must never be edited), `LOG.md`/`REVIEW_INDEX.md` history, or an unrelated **real** `[00:43:10]` marker in V01's and V06's transcripts. No live assertion of the wrong timecode survives anywhere. `git diff -M --summary` confirms `rename … (100%)` — blob and history preserved. **The disclosed residual is adjudicated CORRECT:** all 26 frame timecodes were re-derived mechanically here — row 26 is the **only** frame over the raw runtime, at exactly `ceil(2583.745) = 2584`, and **nothing flags** under `> ceil(runtime)` while `00:43:10` (2,590 s) would remain a true positive. **Credit where R1 was incomplete:** the fourth reference (`V08_SOURCE_NOTES.md` §12 item 4) was **not** in R1's enumeration; the remediation found it by sweeping for the string rather than working the reviewer's list, which is the correct method |
| 67 | V08 R1 | **RECOMMENDED, NOT OWED — a successor to `PT-034` with a non-hindsight second condition.** `BT_V08_0001` §6 discloses, against its own test, that `PT-034` §6's second condition (rule arm above `N1`'s 95th percentile) is near-tautological given that the rule arm knows where the day's extreme is; it returned 100.0 in all four cells. The reviewer **upheld the refusal to re-run** — editing a pre-registration after seeing the number is forbidden and a corrected rule is a new test. **Proposal:** pre-register a successor whose second condition compares the rule arm against a benchmark knowable in real time, e.g. the extreme of the first half of the day | `06_MANUAL_BACKTEST/PRE_REGISTERED/`; `18_REVIEW/V08/V08_REVIEW_R1.md` §5 row 3 | OPEN |
| 68 | V08 R1 | **OWNER DECISION — `D-038`'s ledger-location rule, and the merge status of `video/v08`.** `D-038` says the append-only ledgers are edited **on the integration branch**; the V08 session wrote `LOG.md`, `COURSE_PROGRESS.md`, `QUARANTINE_REGISTER.md`, `AUTOMATION_AMBIGUITIES.md` and `CONTRADICTIONS.md` on `video/v08` and **disclosed the deviation rather than resolving it**. **No finding is charged against the student** — the policy is one day old and disclosure is the behaviour it asked for. **Reviewer's observation, offered not imposed:** the last three files are not in `D-038`'s enumerated list at all and are exactly what a lesson session must write to do its job; the list may need splitting into *policy* ledgers (integration branch) and *evidence* ledgers (task branch, merged with the lesson). **Also owed:** whether to merge `video/v08` (unmerged at `d9e4f9e`, clean fast-forward available) and `review/v08`. **Neither merge was performed by the reviewer** — `D-038` makes merge-back a separate single-threaded act | `DECISIONS.md` D-038, **D-038a**; `18_REVIEW/V08/V08_REVIEW_R1.md` §3, N1 | ✅ **CLOSED 2026-08-13 — both parts settled.** (1) **The ledger question is RULED and RECORDED as `DECISIONS.md` D-038a**, which adopts the reviewer's proposed split substantially as offered: **POLICY ledgers** (`DECISIONS.md`, `SETUP_ISSUES.md`, `CHANGELOG.md`, the protocols and standards) stay integration-branch-only; **EVIDENCE ledgers** (`LOG.md`, `COURSE_PROGRESS.md`, `QUARANTINE_REGISTER.md`, `AUTOMATION_AMBIGUITIES.md`, `CONTRADICTIONS.md`, `REVIEW_INDEX.md`, `SOURCE_MANIFEST.md`) are written on the task branch and merged with the work. **The V08 session's handling is retroactively correct**, not a deviation, and no finding was or is charged. `D-038`'s superseded paragraph is retained with an amendment pointer. (2) **Both merges are DONE** — `video/v08` at `46d09ed`, `review/v08` at `a025b97`, in that order, single-threaded per `D-038`, validator `103 passed / 0 warnings / 0 failures` after each. The append-only merge was verified rather than assumed: zero deleted lines in four of the five ledgers, no duplicate `A-`/`C-`/`Q-` identifiers, no conflict. **One real defect surfaced and is carried forward as item 69** — a cross-branch record-ID collision on `C-007`/`C-008` |
| 69 | Integration (V08 merge-back) | **CROSS-BRANCH RECORD-ID COLLISION — two different `C-007`s and two different `C-008`s exist on two branches.** Found during the `video/v08` / `review/v08` merge-back, by re-deriving the identifier set after the merge rather than trusting `git`. Now on the integration branch (from `video/v08`): `C-007` *"Twenty-nine 'set ups' become twenty-nine 'trades' inside eight minutes"*, `C-008` *"'Go off my faith here' and 'big scientific reason', four sentences apart"*, `C-009`. Still unmerged on `infra/add-steve-moro-reference-book` (`1728287`): a **different** `C-007` *"The moving-average SET: the corpus uses an `800` the admitted seminar notes do not contain"* and a **different** `C-008` *"The ADR lookback window: the notes say two weeks, the corpus says two days"*. **`git` cannot detect this** — the two branches append to different regions of the same file, so it merges cleanly and silently produces four records under two identifiers. **Required, by whoever merges `infra/add-steve-moro-reference-book` next:** renumber that branch's two records to `C-010`/`C-011` (integration's `C-009` is the current high-water mark) and fix every cross-reference to them before merging. `infra/external-vocabulary-reference` should be checked the same way. **`D-038a` consequence 1 records the general obligation** — allocate identifiers against the latest integration branch and re-check at merge-back | `11_CONTRADICTIONS/CONTRADICTIONS.md`; `DECISIONS.md` D-038a consequence 1 | ✅ **CLOSED 2026-08-13 — discharged at the `infra/add-steve-moro-reference-book` merge-back, exactly as required.** That branch's two records were renumbered **`C-007` → `C-010`** and **`C-008` → `C-011`** at `6ba1024`, before the merge, with **34 references across 5 files** updated — `CONTRADICTIONS.md` (13), `LOG.md` (9), `AUTOMATION_AMBIGUITIES.md` (6), `SOURCING_HIERARCHY.md` (3), `EXTERNAL_VOCABULARY_REFERENCE.md` (3) — and zero `C-007`/`C-008` occurrences left on the branch. `video/v08`'s `C-007`/`C-008` were **not touched**. Each renumbered record carries a provenance banner giving its original identifier, so citations written before the merge are not orphaned. `infra/external-vocabulary-reference` was checked as this item directed and needed no separate action: it is an **ancestor** of `infra/add-steve-moro-reference-book` (merged into it at `14f0c70`), so the renumbering covers it. **The collision hunt was widened rather than stopped at the known pair**, per `D-038a` consequence 1 — `D-`, `A-`, `Q-`, `PT-`, `I-` and `REVIEW_INDEX` item numbers were all re-derived on both sides against the merge base `823458d`. `C-xxx` was the only collision |
| 70 | V07 R2 | **`M1` (`E01`, co-code `E20`) — the repair that discharged item 63's second half is itself a false categorical claim, and three quotations falsify it.** `V07_MASTERY_REPORT.md` §H now asserts *"One quotation in the V07 set contained a word that is not in the source. It was found at R1, it is corrected, and **no other instance exists**"*, and that four reconstructions — *"it's met"*, *"the 15 minute"*, *"mayo"*, the 13/50/200 reading — *"were moved **outside** the quotes"*. **Three instances stand:** (a) `V07_SOURCE_NOTES.md` **§9a** quotes `[00:27:24]` as *"30 minute of the water, 30 minute of the **mayo**."* — the marker reads *"…30 minute of the **male**,"*, and **§10 of the same file measures `mayo` at 0 occurrences and says the audio only garbles it to mail/male**, so one file again holds a right record and a wrong record for the same object; **§9's evidence table ten lines above renders it correctly**, reconstruction outside the quotes with `A-020` provenance — the fourth instance of V04 R1's `N5` narrative-restates-the-table class; (b) `V07_SOURCE_NOTES.md` **§11**, the row headed *"`[00:25:26]`'s **unrecovered** word"*, then quotes *"it turns red when **it's met**"* — `[00:25:26]` reads *"It turns red when **Beth**."*; (c) `04_SCREENSHOTS/V07/INDEX.md` **"what the frames add" item 6**, same substitution unbracketed, where **row 15 of its own frame table brackets it correctly as `[it's met]`**. **Materiality to any conclusion: none** — `A-020` is not moved, §10's `mayo` 0 row is correct, and the ADR observation is correctly fenced as display behaviour rather than a course rule in both places. **Charged because a categorical self-certification is exactly what a later session relies on instead of re-checking — the remediation's own stated reason for repairing rather than scoping.** **Fix:** correct §H (both sentences) with superseded text retained, and **in the same edit** fix all three sites — literal *"male"* with *mayo* outside the quotes at §9a, *met* out of the quotes or bracketed at §11 and at `INDEX.md` item 6. **Do NOT edit §9's table, §10's `mayo` row, §5, §6c, or `INDEX.md` row 15 — all five are correct and are the model.** Do not re-open items 61/62. Two supporting NOTES: **`N1`** the sweep that earned the repaired claim is **not reproducible** — no script was committed with `98d893a`; **`N2`** three sweeps returned 239 (R1), 238 (R2, pre-remediation tree, independently written matcher) and **167** (the remediation), and the 30% gap is why the instances passed | `V07_MASTERY_REPORT.md` §H; `V07_SOURCE_NOTES.md` §9a, §11; `04_SCREENSHOTS/V07/INDEX.md` item 6; `V07_REVIEW_R2.md` M1; `05_HOMEWORK/V07/scripts/verify_quotes.py` | ⚠️ **APPLIED 2026-08-13 — PENDING VERIFICATION at R3.** Branch `fix/v07-r2-item70`, cut from the integration branch at `6d86272` after `git fetch --all` confirmed no divergence (`D-038`). **Both marker texts were re-derived from `02_TRANSCRIPTS/V07/V07_TRANSCRIPT.md` before any edit, not taken from the review's prose:** `[00:27:24]` reads *"The dashed ones like this are 30 minute versions, 30 minute of the water, 30 minute of the **male**,"* and `[00:25:26]` reads *"That brown line there is the ADR. It turns red when **Beth**."* **All four sites corrected in one edit:** §H now states that **four** quotations contained a word not in the source — one found at R1, three at R2 — and cites committed code instead of asserting completeness; §9a quotes the literal *"…30 minute of the male,"* with *mayo* outside the quotes carrying its `A-020` provenance, as §9's table already did; §11's `[00:25:26]` row and `INDEX.md` item 6 both read *"it turns red when **[it's met]**"*, bracketed to match `INDEX.md` row 15. **Superseded text retained at all four sites** per `REMEDIATION_PROTOCOL.md` §2, each block naming the round, open item, finding code and instance letter. **The prohibitions were honoured:** §9's evidence table, §10's `mayo` **0** row, §5, §6c and `INDEX.md` row 15 are **unedited**; items 61 and 62 were not re-opened; no V07 script, homework, backtest or probe was re-run; `R11` is still failing; no git history was rewritten; no retention block was deleted. **`N1` DISCHARGED — this is the substantive change of the round.** The sweep is no longer an uncommitted throwaway: `05_HOMEWORK/V07/scripts/verify_quotes.py` is committed and re-runnable, and it checks in **two tiers** — marker-cited quotations must resolve to the transcript exactly, and **uncited** quotations are flagged when they track a transcript sentence for ≥4 consecutive words and then diverge. The second tier is why instance (c) is reachable at all: it carries **no adjacent marker**, so no citation-windowed sweep could ever have found it, which is the mechanism behind `N2`'s 239/238/**167** spread. **Run against the pre-correction tree the script reproduces exactly the three instances R2 found and nothing else** (338 fragments extracted, 3 flagged); run against the corrected tree it returns **0 flags**, with 64 non-transcript quotations dispositioned by a reasoned allowlist (printed slide/chart text, labelled V04 quotes, a hypothesised ASR alternative, the declared second ASR pass) and 23 by the retention-block rule — the rise from 14 to 23 retained fragments being exactly the expected audit-trail inflation `V07_REVIEW_R2.md` §4 predicted. **One further flag was surfaced, hand-checked and deliberately NOT edited:** `V07_MASTERY_REPORT.md`'s *"Do all the DM[R] speaker[s] agree on this?"* brackets a correction **inside** a token, where `[00:29:49]` reads *"DMS speaker"* — the bracket convention working as designed rather than a substitution, R2 did not raise it, and this remediation does not widen its own scope. It is recorded in the script's allowlist with its reason so **R3 can rule on whether intra-word bracketing should be spelled differently**, rather than it passing unseen. **Nothing is self-certified** — `D-003` reserves verification and closure to an independent reviewer; item 63 stays OPEN until this item discharges at R3. ✅ **CLOSED — VERIFIED at R3 2026-08-13** (`V07_REVIEW_R3.md`). **Source read first, per `REVIEW_PROTOCOL.md` §3:** both markers were read from `V07_TRANSCRIPT.md` before any remediated artifact text — `[00:27:24]` *"…30 minute of the water, 30 minute of the **male**,"* and `[00:25:26]` *"It turns red when **Beth**."* — and all three sites match. §9a quotes literally with *mayo* outside the marks carrying `A-020`; §11 and `INDEX.md` item 6 bracket as `[it's met]`, **and item 6 exceeds what R2 required** by also adding the missing `[00:25:26]` citation and printing the literal *Beth*, which repairs both limbs of the defect R2 named. Superseded text retained at all four sites — `V07_SOURCE_NOTES.md` has exactly **two** deletion lines in the entire commit, both reproduced verbatim in dated blocks. Prohibitions verified individually: §9's table, §10's `mayo` **0** row, §5, §6c and `INDEX.md` row 15 are **byte-identical to `6d86272`**; 61/62 not re-opened and re-derived a second time anyway (56; 5; 7,436 words); `R11` re-run and **still FAIL**; no history rewritten; no retention block deleted. **`N1` DISCHARGED — and the script was ATTACKED, not merely trusted.** R3 re-ran it (3 flags pre-correction at exactly R2's three sites, 0 after) and then mutation-tested it, finding **four precision bounds**: allowlist matching by `startswith` **can** excuse a longer differently-worded quotation *although the docstring at line 105 claims it cannot*; `MIN_WORDS = 3`; only `*`-emphasised quotations are extracted; and `in_blockquote()` is tested **before** the cited-FLAG branch, so a new defect on a `>` line is masked. **All four were then searched by hand and are empty** — the 22 unemphasised ≥3-word fragments all have a near-miss run of **0**, and every `RETAINED` fragment with a run ≥4 sits in a genuine retention block re-quoting an already-charged defect. **Recorded as `N1`, NOT charged:** the load-bearing claim is true and was established independently of the tool, and charging a tool's documented, harmless precision limit as a defect in a *lesson* would be `REVIEW_PROTOCOL.md` §16's artificial difficulty. Recommended when the file is next touched, not owed: anchor allowlist matching to the full fragment, fix the line-105 comment, order `in_blockquote` after the cited-FLAG test. **THE BRACKET-TOKEN ITEM IS RULED — `N2`.** *"Do all the DM[R] speaker[s] agree on this?"* against `[00:29:49]`'s *"Do all the DMS speaker agree on this?"* is **NOT a defect and must not be corrected.** The brackets are a **visible signal** — precisely what instances (a)–(c) lacked, and the whole basis on which R2 charged them — so §H's *"outside the quotes **or inside square brackets**"* is not falsified; intra-word bracketing is an established convention beyond V07 (`V01_SOURCE_NOTES.md` S63 *"mov[ing]"*, `V08_TRANSCRIPT.md` `[00:08:58]` *"sca[m]"*), so charging it here would charge a three-lesson-wide convention on one lesson's review; the literal *DMS* **is** recorded, in `V07_TRANSCRIPT.md`'s own ASR-garble inventory; and *DM* is not a corpus object while *DMR* is heavily attested, so the lossy bracket-strip cannot mislead a reader to a wrong referent. No conclusion turns on it — `C-005`'s extension rests on the presenter's **non-answer**. **The remediation was right to flag rather than fix it**, and that behaviour is the one that would have prevented item 70 a round earlier. Non-blocking observation only: V08 pairs its intra-word bracket with an inline *"the ASR prints `scan`"*; V07's four sites carry no adjacent disclosure — adopt the V08 form whenever those lines are next edited for another reason, and do **not** open an edit for it |
| 71 | V08 R2 | **DOCUMENTATION FOLLOW-UP, NOT OWED AS A DEFECT — carry R2's presenter-identity ruling into `C-009`.** `Source A′`'s speaker-identity row states the point is *"NOT established, and deliberately not asserted here"*. **That was true when written and this round supersedes it.** `V08_REVIEW_R2.md` §2 rules that **V07's and V08's presenters are DIFFERENT MEN, `HIGH` confidence, on textual evidence only:** V08's speaker names **Ray** three times in the third person — `[00:00:49]` *"I may or may not be able to be as responsive as **Ray** was with the questions"*, forty-nine seconds into Part 3, and `[00:05:59]` *"the information that **Ray** was beginning to answer… is leading into this topic"* — while `Ray` occurs **zero** times in V07's body and **zero** in V06's; V07 is the Q&A part (sixteen named questioners read aloud) and V08 *"reads no questions"*. **Independently:** V07's presenter defers to **Jim** ×3 and at `[00:07:43]` disclaims the high-of-day skill (*"I like second legs because I can't do that sometimes"*) that V08's second half teaches under a deck titled *"Jim's Journey"*; and the programme roster names Ray and Jim as distinct coaches (V02 `[00:57:02]`, V03 `[00:22:51]`). **Probable names — V07 = Ray, V08 = Jim — at `MEDIUM`**, held back by the one residual (V08 `[00:17:29]` *"Jim's right about that one"*, unexplained), which does **not** touch the different-men finding since that does not require the identification. **Names remain provenance, not evidence (`D-033` provision 2).** **NO cross-file F0 comparison was used** — `COURSE_PROGRESS.md` V06 GATE item (a) prohibits it and the ruling is unchanged without it. **Required of nobody now:** update the row whenever `C-009` is next edited for another reason; **do NOT open an edit for it alone.** `C-009` stays `PROVISIONAL`, and `D-025`'s guest/instructor carve-out does **not** apply — both speakers are `GUEST`, so it remains a method-level contradiction | `CONTRADICTIONS.md` C-009 `Source A′`; `18_REVIEW/V08/V08_REVIEW_R2.md` §2, N1 | OPEN — **not a gate, and it did not hold V08** |
| 72 | V08 R2 | **OWNER / PROCESS — a concurrent session moved the shared working directory's branch mid-review, and the failure mode is SILENT.** This reviewer cut `review/v08-r2` from the integration branch at `a6ee013` in the **main** working directory; partway through verification, `git status` showed that directory on **`review/v09` at `bb4097b`**, a branch this session never created or checked out. `video/v09` descends from **`f3f9006`**, which predates **both** the V07 R2/R3 merge (`a886585`) **and** the entire V08 remediation — so that tree contains neither the `Source A′` block nor the item-65/66 fixes. **A reviewer reading it would have found the remediation's work simply ABSENT, with no error and entirely plausible file contents — i.e. would have verified a fix against a tree predating it.** It surfaced only because `18_REVIEW/V07/` listed one file where three are committed ancestors, an impossibility that prompted a check rather than an assumption. **Contained:** a dedicated worktree was created and **every** read taken after the switch was re-run there before use; two `REVIEW_INDEX.md` reads had indeed come from the stale tree and were **discarded and redone**. **No conclusion in `V08_REVIEW_R2.md` rests on a read from the wrong tree**, and the main directory was left on `review/v09` as found so the concurrent session was not disturbed. **Recommendation, offered not imposed:** review and remediation sessions should take a **dedicated worktree** rather than switching the shared main directory (the V08 R1 reviewer already did), and should re-assert `git branch --show-current` before any load-bearing read. `D-038` treats branch isolation as a safety property; this shows the hazard is live | `DECISIONS.md` D-038 / D-038a; `18_REVIEW/V08/V08_REVIEW_R2.md` N2 | OPEN — **owner/process. NOT attributable to V08, to the remediation session, or to any lesson artifact; no finding charged** |
| 73 | V09 R1 | **`M1` (`E01`) — four silent ASR corrections inside quotation marks, under `AUDIO` basis tags.** `V09_SOURCE_NOTES.md` §3 quotes *"Example solid **HOD/LOD** entries can warrant a 15-pip stop loss"* as `AUDIO` at `[00:03:49]`, where the audio says *"high low-day"*; §9a, introduced as *"`AUDIO`, verbatim across five markers"*, renders `[00:41:25]`'s *"What is the **grade** Fred?"* as *"grape"*; §7e gives *"experience shows me"* for *"experiences show me"* `[00:44:39]`; §5 removes the stutter from *"what it's it's titanium"* `[00:19:55]`. No conclusion moves and the transcript body is untouched. **Required:** generalise `05_HOMEWORK/V07/scripts/verify_quotes.py` to take a lesson identifier (its transcript, artifact list and printed-slide allowlist are V07-specific), run it over the seven V09 artifacts, and for each hit move the correction **outside** the quote marks with its marker or retag the row `PRINTED`. **Do not edit the transcript body.** | `03_LESSON_NOTES/V09_SOURCE_NOTES.md`; `V09_REVIEW_R1.md` `M1` | ✅ **CLOSED — VERIFIED at R2** (`V09_REVIEW_R2.md` §1). All four markers re-read in the transcript by an independent session: the finding was real. All four sites correctly repaired, two of them by the stronger `PRINTED`-retag route. Superseded text retained at each. **Transcript body byte-identical by hash.** ⚠ **The item's OTHER required action — generalise and RUN `verify_quotes.py` — was NOT performed, and a fifth instance survives: NEW ITEM 81.** |
| 74 | V09 R1 | **`M2` (`E20`) — `PT-035` §6's `INDETERMINATE`-on-`N3`-failure clause is neither applied nor disclosed.** The pre-registration's decision table for the claim under test reads *"INDETERMINATE — cells disagree…, **or `N3` fails**"*, and §7b is headed *"WHAT WOULD MAKE THIS TEST VOID"*. `N3` failed. `BT_V09_0001` enforces that gate on the **clustering** arm — correctly, and against a runner that printed the opposite — and then applies the empirical arm's verdict word without mentioning that the same clause covers it; `run_pt035.py` lines 356–366 do not encode it either. **The conclusion survives**: `CONTRADICTED AS STATED` follows from §2c's closed form, pre-committed and **re-derived independently by the reviewer**. **Required:** record the clause in `BT_V09_0001` §5, report the empirical arm as `INDETERMINATE`, carry the verdict on the §2c/`O4` closed form alone, and propagate to `V09_MASTERY_REPORT.md` §G and `LOG.md`. **`PT-035` and `run_pt035.py` must NOT be edited** (`COMMON_PROTOCOL.md` §9 rule 7). | `06_MANUAL_BACKTEST/V09/BT_V09_0001.md`; `V09_REVIEW_R1.md` `M2` | ✅ **CLOSED — VERIFIED at R2** (`V09_REVIEW_R2.md` §1). §6's clause re-read **in the pre-registration blob**: real and unapplied as charged. Fix complete — the table is quoted in full, the measured arm is reported `INDETERMINATE`, the verdict is carried on §2c/`O4` alone, `P3` re-scored and the tally moved `3/1/1`→`2/1/1/1` with both prior values retained, and it is propagated to `BT_V09_0001`, the mastery report §G and `LOG.md`. **`PT-035` and `run_pt035.py` BYTE-UNCHANGED — verified by blob SHA and single-commit history.** The closed form was **re-derived in the R2 reviewer's own run-length DP** and confirms the verdict needs no measurement. |
| 75 | V09 R1 | **`M3` (`E19`) — a MEASURED count in the transcript's COVERAGE block is wrong.** *"Next largest 10 s, four times"* lists four markers; there are **seven** — `[00:02:38]`, `[00:03:23]`, `[00:19:18]`, `[00:23:05]`, `[00:45:41]`, `[00:49:35]`, `[00:49:47]`. Everything else in the block reproduces exactly. **Required:** correct the count and list all seven, retaining the superseded text per `REMEDIATION_PROTOCOL.md` §2. | `02_TRANSCRIPTS/V09/V09_TRANSCRIPT.md`; `V09_REVIEW_R1.md` `M3` | ✅ **CLOSED — VERIFIED at R2** (`V09_REVIEW_R2.md` §1). Independently re-measured with a scanner the R2 reviewer wrote: **721/718 markers, zero decreasing transitions, 11 s twice, 10 s SEVEN times at exactly the seven markers listed.** The original *"four"* was wrong and the correction is exact. Superseded text retained; **transcript body byte-identical by hash**. |
| 76 | V09 R1 | **`M4` (`E11`) — fourteen frame cross-references at 15 or above are off by one, across five files**, after a 27th frame was inserted at position 15 and the index table renumbered without the back-references. Full list in `V09_REVIEW_R1.md` `M4`. Every content claim they support is correct. **Required:** renumber all fourteen; **preferred**, replace the bare ordinals with the frames' burned timecodes or filenames, which a later insertion cannot invalidate. | `03_LESSON_NOTES/V09_SOURCE_NOTES.md`; `04_SCREENSHOTS/V09/INDEX.md`; `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md`; `11_CONTRADICTIONS/CONTRADICTIONS.md`; `07_MASTERY_REPORTS/V09_MASTERY_REPORT.md` | ✅ **CLOSED — VERIFIED at R2** (`V09_REVIEW_R2.md` §1). The off-by-one re-derived from the 27-frame listing: real. The fix took the **preferred structural route** — burned timecodes, which an insertion cannot invalidate. **Zero bare ordinals remain in any V09-scoped file**; `INDEX.md`'s four survivors were each checked and are legitimate. Conversions spot-verified against the frame list and one against the image itself. ⚠ **Two references carrying the identical stale string survive in the SHARED register at sites R1 mis-attributed: NEW ITEM 82.** |
| 77 | V09 R1 | **`M5` (`E02`) — the candidate `C-010` reconciliation is held at *"more likely than not"* and fails at the set level.** Reading the notes' `5, 13, 50, 200` on the 1-hour maps it to `20, 52, 200, 800` on the 15-minute; the corpus carries a 5, a 13 and a 50, and `A-020` requires mayo = 200 and blueberry = 800 to be **two lines on one chart**. One member of four reconciles. **`C-010` STAYS OPEN and the refusal to close it is UPHELD** — this is charged against the confidence, not the decision. **Required:** annotate `V09_INTERPRETATION.md` Q5 with the set-level arithmetic and downgrade `MEDIUM` → `LOW`, correct Q8's falsification row, and record the same in `C-010`'s V09 block. **This also retires the submission's escalation 5 to the owner** — the route does not reach, so no blending judgement is owed. | `03_LESSON_NOTES/V09_INTERPRETATION.md`; `11_CONTRADICTIONS/CONTRADICTIONS.md` `C-010`; `V09_REVIEW_R1.md` `M5` | ✅ **CLOSED — VERIFIED at R2** (`V09_REVIEW_R2.md` §1). The arithmetic re-verified **against `MMM-NOTES` at source** — four averages enumerated, `800` absent from all 84 pages — and against `A-020`'s attested Mayo = 200 / Blueberry = 800. All three required actions performed: Q5 downgraded `MEDIUM`→`LOW` with the mapping written out, Q8's row corrected, `C-010` annotated. **`C-010` stays OPEN, disposition unchanged.** Superseded text retained. ⚠ **The escalation this retires was not marked retired in the mastery report: NEW ITEM 83.** |
| 78 | V09 R1 | **`M6` (`E20`, omitted-corroboration sub-class) — the capture-bug escalation says the coordinate works *"on V01–V08"*.** It does not: `04_SCREENSHOTS/V08/INDEX.md` records the identical failure at the identical coordinate one lesson earlier, with the same corrected `(512, 325)`. **The bug is CONFIRMED and generalised by the reviewer** — V08, V09 and V21 declare a 1280×738 stage against the other 18 files at 1024×786, so the recipe's 1024×786 viewport letterboxes exactly those three. **Required:** correct the sentence in `04_SCREENSHOTS/V09/INDEX.md` and `V09_MASTERY_REPORT.md` escalation 2, cite V08's index, and reference the stage-geometry cause. **The recipe fix itself is NOT owed by the student** — it is a policy ledger and the reviewer has made it on integration. | `04_SCREENSHOTS/V09/INDEX.md`; `07_MASTERY_REPORTS/V09_MASTERY_REPORT.md`; `00_SYSTEM/SWF_CAPTURE_RECIPE.md`; `V09_REVIEW_R1.md` `M6`, §16 | ✅ **CLOSED — VERIFIED at R2, BOTH HALVES** (`V09_REVIEW_R2.md` §1). **Reviewer half:** the stage geometry was **re-derived independently** — exactly three of the 21 canonical files declare 1280×738 — and the `GOTCHA 5` probe script was **run verbatim on both classes and works**. The edit is correctly hedged and makes the table-free before/after guard the standard. **Student half:** both files now state the coordinate also failed on V08, quote and cite V08's index (verified verbatim), and carry the stage-geometry cause; **no live *"V01–V08"* claim remains** — the surviving occurrences are all retained superseded text. **The two halves are mutually consistent.** |
| 79 | V09 R1 | **RECOMMENDED, NOT OWED — the `PT-035` successor.** `BT_V09_0001` §4 names the correct clustering comparator (chronological `run4_obs` against the **shuffled** `run4_obs` of the same sequences, composition held fixed) and **declines to compute it** because it was not pre-registered — which is the right refusal, `D-026`/`E21` exactly. Pre-register it under a new `PT` number. **Carry one requirement into it:** both `N3` gates must be encoded **in code**, not in prose — `M2` is what happens when a decision rule lives only in a markdown section. | `06_MANUAL_BACKTEST/V09/BT_V09_0001.md` §4; `V09_REVIEW_R1.md` §5 item 8 | 🔶 **OPEN — recommended** |
| 80 | V09 R1 | **ESCALATED — the resolution-censoring bias, with the scope tightened.** `PT-035` §3 diagnoses it against its own interest: within a bounded intraday horizon a distant target is censored more often than a near stop, so conditioning on resolution over-weights stop-outs and biases every hit rate **downward**. The submission flags `PT-002`…`PT-032` as possibly affected. **The reviewer's judgement: the mechanism is real and the concern is well-founded, but that framing is too broad** — most of that family measures range, weekday, gap and barrier statistics with no stop/target race and no discard. **Where it lands is `PT-033`, `PT-034`, `PT-035` and any successor racing asymmetric barriers inside a bounded horizon.** **First evidence already exists:** `PT-034`'s `N1` returned 0.2424 / 0.2426 / 0.2429 / 0.2450 against a closed-form break-even of **0.2500** — below it in **all four cells**, which is the predicted direction. **It does NOT retroactively invalidate `PT-034`**: a small consistent downward bias in a null makes the rule-arm gap it was compared against slightly *wider*, not narrower. **Owner/reviewer action:** open a scoped investigation over those three tests before any further test reuses a day-end horizon with asymmetric geometry. | `06_MANUAL_BACKTEST/V09/BT_V09_0001.md` §3; `06_MANUAL_BACKTEST/V08/BT_V08_0001.md`; `V09_REVIEW_R1.md` §2 item 7, `N5` | 🔶 **OPEN — escalated** |
| 81 | V09 R2 | **`MINOR` (`E01`) — item 73's required mechanized quote sweep was never run, and a FIFTH instance of the same defect survives.** `V09_REVIEW_R1.md` §15 item 1 required **two** actions: generalise and **run** `05_HOMEWORK/V07/scripts/verify_quotes.py` over the seven V09 artifacts, *and* fix each hit. The four enumerated hits were fixed by hand; **the sweep was not run** — `verify_quotes.py` is still V07-specific with a single commit (`cc74051`, V07 R2/R3) and nothing has touched it since. **The cost is demonstrable, not theoretical:** `V09_SOURCE_NOTES.md` line 410 still renders `[00:44:39]`'s *"experiences show me"* as *"experience shows me"* inside quote marks — **the same phrase, in the same file, that item 73 corrected 38 lines above**, where a retained superseded block now states that the transcript reads *"experiences show"* and that an `AUDIO`-tagged quotation may not be tidied. **The file contradicts itself about what the audio says.** Nothing moves — it is a plural in a descriptive basis column — but the prescribed remedy for this class is mechanization *precisely because* hand-fixing an enumerated list leaves the un-enumerated ones, and that is what happened. **Required:** generalise `verify_quotes.py` to take a lesson identifier, **run it over the seven V09 artifacts and commit the run**, and fix every hit it returns, beginning with line 410. Retain superseded text. | `03_LESSON_NOTES/V09_SOURCE_NOTES.md`:410; `05_HOMEWORK/V07/scripts/verify_quotes.py`; `V09_REVIEW_R2.md` item 81 | 🔶 **OPEN — owed at V09 R3** ⚠ **CLOSED — SELF-VERIFIED AT OWNER DIRECTION 2026-08-13** (branch `fix/v09-r2-minors`, cut from `review/v09-r2` at `dc427dc`, zero divergence confirmed by `git fetch --all` first, `D-038`). **NOT `CLOSED — VERIFIED`. This round was fixed AND verified by ONE session on the owner's explicit authorisation; it does not satisfy `D-003` and the distinct status string exists so it is never mistaken for an arm's-length verdict.** **BOTH halves of item 73's original requirement are now discharged.** `verify_quotes.py` is **generalised** — `ARTIFACTS` and `ALLOWLIST` are per-lesson dicts keyed by lesson id, the transcript path is derived, usage is `verify_quotes.py {V07|V09}` — and it was **RUN**, for the first time ever, against all seven V09 artifacts. **The first run FLAGGED 46 fragments.** **Then it was extended**, because the seventh instance of the defect was in a file the review's named artifact set does not cover: it now also scans `10_AMBIGUITIES/` and `11_CONTRADICTIONS/` for **every** lesson, restricted to table rows whose FIRST cell names that lesson — the register's own declaration of which transcript a row asserts, which is what makes the check sound on a cross-lesson file. **NINETEEN genuine defects found; all nineteen fixed; superseded text retained at every one.** The review named **one**. **The two that vindicate the charge:** `V09_SOURCE_NOTES.md` line 410's *"experience shows me"* for `[00:44:39]`'s *"experiences show me"* — item 81 verbatim, the fifth instance and the second copy of that phrase; and **`04_SCREENSHOTS/V09/INDEX.md` row 26's *"What is the grape?"* cited to `[00:41:25]`, where the transcript reads *"What is the **grade** Fred?"* — the SIXTH instance, which NO HUMAN IN EITHER REVIEW ROUND FOUND**, and whose twin `V09_SOURCE_NOTES.md` §9a had corrected at R1. **The six in the SHARED register**, found only after the extension: `A-072` carrying a **third** live copy of *"experience shows me"*, `A-066`'s *"solid HOD/LOD entries"* for *"Example solid high low-day entries"* (item 73's own defect, one register over), `A-072`/`A-073`'s *"people trapped"* for `[00:44:48]`'s *"people trap"*, `A-071`'s unmarked join across *"All right, so"*, and `A-075`'s *"count lists"* for *"count list"*. **The other eleven**, in the artifact set: *"2%"* for the spoken *"two percent"*, *"brings"* for *"will bring"*, *"forex"* for the ASR's *"4x"*, *"DMR"* for *"dmor"*, *"USD JPY"* for *"USD JP why"*, a Claim row that blended audio and slide into a quotation verbatim in neither, and four unmarked elisions joining non-adjacent markers with a comma or a full stop. **THREE further fragments were flagged and HAND-RULED NOT DEFECTS** on `V07_REVIEW_R3.md` `N2`'s ground — `A-071`'s two `[M]` brackets and `A-073`'s `[seeing]` bracket leave a hole when stripped, but every unbracketed word is verbatim and `[seeing]` is the reading `V09_TRANSCRIPT.md`'s own TRANSCRIPTION NOTES record as correct; each is enumerated in the allowlist with its reason rather than left to re-flag. **TWO OF `V07_REVIEW_R3.md` §4's THREE RECOMMENDED PRECISION FIXES ARE ADOPTED AND ONE IS REFUSED WITH REASONS:** allowlist matching is anchored to the **full** normalised fragment instead of a prefix (closing the hole R3 found by mutation testing — three V07 fragments the prefix rule had been excusing silently now carry their own written reasons), and the docstring claim that prefix matching could not do that, which was false, is corrected; **REFUSED** — ordering `in_blockquote()` after the cited-FLAG test, because `REMEDIATION_PROTOCOL.md` §2 retention blocks re-quote the defective rendering on a `>` line **and** carry its marker, so the reorder would FLAG every correctly-retained superseded quotation. R3's actual concern was masking, not ordering, and it is addressed instead by having **every** `RETAINED` fragment report its near-miss run — mechanised visibility, not a mechanised verdict. **MUTATION-TESTED three ways during the self-verification pass**: reintroducing item 81's defect at line 410 FLAGs, reintroducing the *grape* instance FLAGs, and appending words to an allowlisted fragment FLAGs — which proves the prefix hole is genuinely closed. **FINAL: V09 → 315 fragments, 0 FLAGGED, exit 0. V07 → 353 fragments, 0 FLAGGED, exit 0**, so no earlier lesson carries the same debt. **ONE DEFECT FOUND AND DELIBERATELY NOT FIXED:** `PT-035` renders `[00:06:08]`'s *"risk management. **How are** I believe that with our training?"* as *"…**However** I believe…"* — the same `E01` class. **It must not be fixed:** `COMMON_PROTOCOL.md` §9 rule 7 forbids editing a pre-registration after the fact, and `V09_REVIEW_R2.md` verified `PT-035` byte-identical to its pre-registration blob by SHA — **fixing a typo there would destroy a stronger guarantee than the typo violates.** Recorded in `V09_MASTERY_REPORT.md` Revision R2, in `LOG.md` and in the script's own allowlist so a later round rules on it deliberately. **The script stays at `05_HOMEWORK/V07/scripts/` on purpose**, though it is no longer V07-specific: six committed documents cite it there and three are review files `REMEDIATION_PROTOCOL.md` §6 forbids editing, so moving it would create exactly the dangling-pointer defect item 82 charges. Disclosed in the docstring. **The transcript body is untouched; `PT-035`, `run_pt035.py` and `pt035_output.txt` are untouched; no marker, status, disposition, grade or conclusion moves anywhere.** |
| 82 | V09 R2 | **`MINOR` (`E11`) — two stale frame ordinals survive in the SHARED ambiguity register.** Item 76 eliminated bare ordinals from every V09-scoped file, but `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md` still carries *"frames 22, 23 and 25"* twice: line 4982 (**`A-069`**, *"high low tracer"*) and line 5173 (**`A-073`**, *"reset"*). **They should read 23, 24 and 26** — burned `28:45`, `31:50`, `41:25`. **These are live wrong pointers and where they land was confirmed:** under the current numbering frame 22 is the **compounding spreadsheet** and frame 25 is the **MS Paint email address**, neither of which is a chart. A reader following `A-069` for chart furniture lands on a spreadsheet — `M4`'s stated harm, verbatim, still present. **The miss originates in R1's enumeration, not in the remediation's execution:** `V09_REVIEW_R1.md` `M4` attributed that exact string to `04_SCREENSHOTS/V09/INDEX.md` alone; it occurred in three places and R1 found one. The two `AUTOMATION_AMBIGUITIES.md` references R1 *did* enumerate (`A-065`, `A-067`) were both correctly converted. **Charged anyway, and at the class's own severity, because these sit in a shared register that OUTLIVES V09** — every later session working on *tracer* or *reset* will read them. **Required:** convert both to burned timecodes per item 76's convention. Retain superseded text. | `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md` `A-069`, `A-073`; `V09_REVIEW_R2.md` item 82 | 🔶 **OPEN — owed at V09 R3** ⚠ **CLOSED — SELF-VERIFIED AT OWNER DIRECTION 2026-08-13.** **NOT `CLOSED — VERIFIED`** — see item 81 for the full `D-003` disclosure. Both records converted from the stale ordinals to **burned-in player timecodes** `28:45` / `31:50` / `41:25`, matching the structural convention item 76 established, which no later insertion can invalidate. Superseded text retained at both sites naming the cause (`ff7b8bd`'s insertion at position 15), the review round and the item. **RE-DERIVED FROM THE IMAGES, not from `INDEX.md`'s description of them** — all five relevant PNGs were opened: `00-28-45` is full-screen MetaTrader `EURUSD,H1` with hand-drawn levels, a level count `1`/`2`/`3`, **`Reset` printed twice as a chart label** and DayHi/DayLo tracer lines; `00-31-50` is `GBPJPY,H1` with `Reset` and numbered levels; `00-41-25` is the nine-tile view with `Reset` on the `EU` and `GU` tiles. **All three carry exactly what `A-069` (*"high low tracer"*) and `A-073` (*"reset"*) describe.** And the harm was confirmed the same way: `00-26-40` is the **compounding spreadsheet** and `00-34-35` is the **MS Paint email address** — neither is a chart, so a reader following `A-069` really did land on a spreadsheet. **The disposition, evidence, Tier 2 negative and `DO NOT CODE` status of both records are unchanged.** **`A-069` and `A-073` were also found to carry six QUOTATION defects between them and their neighbours** — see item 81; the register turned out to be carrying both classes of debt, which is the strongest available argument for R2's point that a shared register outlives its lesson. |
| 83 | V09 R2 | **`MINOR` (`E19`) — the mastery report still puts a retired question to the owner.** Item 77's own `REVIEW_INDEX.md` row states that it *"retires the submission's escalation 5 to the owner — the route does not reach, so no blending judgement is owed"*, and `C-010`'s new V09 block says the same in its own words. **`V09_MASTERY_REPORT.md` escalation 5 is unchanged**, still reading *"if the owner judges that reading a timeframe into `MMM-NOTES` is acceptable, `C-010` closes immediately"* and still flagged **OWNER**. It does not close immediately, and the project now knows why. **Escalation 2 in the same table was given a `✅ DISCHARGED` marker in this same remediation**, so the mechanism was available and was applied one row away. Charged because the owner-escalation table is an **action list, not prose** — its whole function is to tell a human what is owed, and it currently owes them a judgement the project has established is moot. This is the *"files that disagree about their own state"* class (V05 R1 `M4`), here between the mastery report and both `C-010` and this index. **Required:** mark escalation 5 retired citing item 77 and `C-010`'s V09 block, in the form escalation 2 already uses, with superseded text retained. | `07_MASTERY_REPORTS/V09_MASTERY_REPORT.md` escalation 5; `11_CONTRADICTIONS/CONTRADICTIONS.md` `C-010`; `V09_REVIEW_R2.md` item 83 | 🔶 **OPEN — owed at V09 R3** ⚠ **CLOSED — SELF-VERIFIED AT OWNER DIRECTION 2026-08-13.** **NOT `CLOSED — VERIFIED`** — see item 81 for the full `D-003` disclosure. Escalation 5 is marked ✅ **RETIRED**, in the same form escalation 2 already used one row away, with the original text retained **in full** per `REMEDIATION_PROTOCOL.md` §2 and the reason stated: **the premise is false.** The escalation offered the owner a ruling on which `C-010` *"closes immediately"*; it does not, on **any** ruling. **RE-DERIVED FROM `MMM-NOTES` AT SOURCE rather than from item 77's account of itself:** p.38 reads *"The specific EMA's used in Mauro's charts are the **5, 13, 50 and 200** bar EMA's"* — four averages — **`800` occurs ZERO times in the entire extract**, and p.66 reads *"Hold the Mayo – 200 Bounce"*, independently corroborating `A-020`'s Mayo = 200. So the factor-of-four identity lands **one member of a four-member set** and **collides with `A-020`**, which attests Mayo = 200 and Blueberry = 800 as two distinct lines. Even granting the most permissive possible owner ruling, `C-010` stays `UNRESOLVED`. **`C-010`'s disposition is UNCHANGED** — item 83 retires a *question about* `C-010`, not `C-010` — and the `SOURCING_HIERARCHY.md` §3.2 *"Do not blend"* refusal recorded in the original text still stands; it is simply no longer the only thing keeping the record open. **The owner-escalation table now owes a human nothing that the project has already settled**, which was the whole charge: it is an action list, not prose. |
| 86 | V10 student | **RECOMMENDED, NOT OWED — the `PT-037` path-length reading of `M1`.** `BT_V10_0001` §9 records that a reading exists on which V10's *"600 to 1000 pips a week"* could survive — **total distance travelled** rather than high-minus-low **range** — and **declines to run it**, because it was not pre-registered and running an unregistered alternative after seeing a failure is how a contradicted claim gets rescued (`E09`). **Pre-register it before measuring.** Carry one requirement: the successor must also report the **textual objection** against itself — the speaker says *"peak formation high **to** peak formation low"*, which names two points and the distance between them, i.e. a range, not a path. | `06_MANUAL_BACKTEST/V10/BT_V10_0001.md` §9 | 🔶 **OPEN — recommended** |
| 87 | V10 student | **ESCALATED — `SWF_CAPTURE_RECIPE.md` §10 states the frame-rate patch as `3.0 → 30.0` fps, carried from V01/V02. V10 declares 2.0 fps.** Applied literally to V10 it sweeps at **15×, not 10×**, and **fails silently**: a complete, well-formed, correctly-timecoded frame set at 7.5-presentation-second spacing, under-sampling the screen-state detector by a third. **Same family as `GOTCHA 4` and `GOTCHA 5`** — a header field that varies across the library, quoted in the recipe as a constant, with no loud failure when wrong. **Fix is one line: read `frameRate` from the header and patch `rate × 10`; `GOTCHA 5`'s probe already parses the adjacent field.** **POLICY ledger under `D-038a` — owed on the integration branch, and correctly NOT patched by the V10 student session.** | `04_SCREENSHOTS/V10/INDEX.md` § ESCALATION; `00_SYSTEM/SWF_CAPTURE_RECIPE.md` §10 | ✅ **CLOSED — FIXED AND VERIFIED at V10 R1, 2026-08-13, on the integration branch under `D-038a`.** **The defect is REAL — reviewer read §10 and confirmed all three sites** (the header table, the prose *"Patch 3.0 → 30.0 fps"*, and the speedup table's *"3 fps control"* column) quote 3.0 as if it were the library's constant. **V10's own capture was NOT harmed, and this was CHECKED rather than assumed:** the student read the header first per `GOTCHA 5`, found 2.0, and patched 2.0 → 20.0 — arithmetically confirmed by the realised sweep of **1,164 frames** (5776.2 s ÷ 5 + 8 = 1,163); a 15× sweep would have yielded ~776 distinct sample points instead. **So the defect was latent, not realised — avoided by a session following `GOTCHA 5`'s advice rather than §10's prose, which is exactly the luck a recipe must not depend on.** **FIX APPLIED:** §10's header table is relabelled *"Measured examples — data points, NOT the library's constant"* and gains V10's 2.0 row with its three-way duration cross-check; a warning block states **THE RULE — read `frameRate` from the header of the file you are about to capture and patch `rate × SPEED`, never type a literal**; the prose becomes *"Patch `declared_rate × 10`"* with the superseded sentence retained per `REMEDIATION_PROTOCOL.md` §2; the speedup table's control column is labelled as V02's rate; and the sweep snippet derives `PATCH_FPS` from `DECLARED_FPS`. **The escalate-don't-patch handling by the V10 student session was CORRECT** — `SWF_CAPTURE_RECIPE.md` is a POLICY ledger and a task branch may not edit it. Second consecutive lesson to get that boundary right. |
| 88 | V10 student | **ESCALATED — `C-017` is the corpus's FIRST printed-vs-spoken contradiction and the project has no standing rule for that class.** V10's anchor distance is measured *"off of the LOW/HOW anchor"* on the printed slide and *"off of the blue tracer"* in **five of seven** spoken instances (**corrected 2026-08-13 from *"four of six"*** under item 92; superseded text retained here per `REMEDIATION_PROTOCOL.md` §2 — the escalation is **strengthened**, the spoken majority being wider than first recorded), and the two are different objects in the lesson's own usage. `D-008`'s hierarchy ranks slides above transcripts and **would settle it by class**; the V10 session **declined to apply it**, reasoning that `D-008` ranks *capture reliability* and was written to stop an agent's reading outranking the course, not to adjudicate between two things one speaker said in one hour. **An owner or reviewer ruling would settle a question that will recur** — this corpus is slide-heavy and single-speaker from V10 on. | `11_CONTRADICTIONS/CONTRADICTIONS.md` `C-017`; `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md` `A-078`, `A-079` | 🔶 **OPEN — escalated** |
| 89 | V10 student | **`A-077` (the lock) is now the highest-value gap in the project, and it is a NEW record.** V10 supplies the safety trade's **anchor** — `[01:14:06]`, the week's extreme — which is **retrospective**. The *"lock"* is the lesson's real-time substitute and carries **no distance and no duration**. It is the **only** thing standing between a defined anchor and a prospectively identifiable setup, and it blocks dimension **B**, V10's deferred **H2** setup half, and **`PT-038`**. **Any lesson attaching a number to *"price has moved away and confirmed"* discharges all three at once.** | `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md` `A-077`; `03_LESSON_NOTES/V10_INTERPRETATION.md` Q3 | 🔶 **OPEN — watch item for V11+** |
| 90 | V10 student | **NOTE — open item 80's censoring bias was DESIGNED OUT of `PT-036` and VERIFIED, which is evidence for the reviewer's narrowed scope.** R1's judgement was that the bias lands on tests *"racing asymmetric barriers inside a bounded horizon"* and not on range/weekday/gap statistics. `PT-036` is exactly the latter kind: no barrier, no horizon, **zero possible censored observations** — asserted in §2 and **enforced as a hard assert** that would have voided both measures. Result: `censored = 0` on both arms. **This does not close item 80** (which is about `PT-033`–`PT-035` and successors) but it confirms the narrowed scope was right. | `06_MANUAL_BACKTEST/PRE_REGISTERED/PT-036_…md` §2, §7b; `06_MANUAL_BACKTEST/V10/BT_V10_0001.md` §6 | ℹ️ **NOTE — supports item 80's scope** |
| 91 | **V10 R1** | **`M1` — OPEN-ITEM IDENTIFIER COLLISION, and the policy gap behind it.** `video/v10` allocated open items **81–85**; the integration branch concurrently allocated **81–83** to **V09 R2** (`7b42156`, merged `310362c`) after `video/v10` branched at `5db04d8`. **Resolved mechanically: V10's items are renumbered 86–90 by the V10 R1 reviewer at merge-back** (see the disclosure beneath this table). **The policy half is NOT resolved.** `D-038a` classifies `REVIEW_INDEX.md` as an evidence ledger on the ground that *"evidence ledgers are append-only and their additions are `git`-mergeable by construction"*, and its safety evidence re-derived `A-`, `C-` and `Q-` identifier sets after the V08 merge. **Open-item numbers were not in that check, and they are the one series in the list that is NOT mergeable by construction** — two branches append `| 81 |` and git merges both. **Recommended: `D-038a` gains an explicit consequence that `REVIEW_INDEX.md` open-item numbers are allocated against the integration branch's state**, as `PT-036` §0 already does for `PT` numbers. Owner ruling needed; a reviewer cannot amend a `DECISIONS.md` entry. **⭐ DIRECT EVIDENCE ADDED AT THE MERGE ITSELF, and it is stronger than the argument:** the `review/v10` → integration merge **CONFLICTED in three files — `REVIEW_INDEX.md` (3 hunks), `LOG.md` (2 hunks) and `COURSE_PROGRESS.md` (1 hunk)** — every one of them an evidence ledger `D-038a` classifies as *"append-only and `git`-mergeable by construction"*. **They are not.** Both branches appended to the same tail of the same tables and status blocks, so git could not order them; `LOG.md`'s conflict additionally **interleaved two session entries**, splicing the V09 R2 entry's Decision/Files/Git/Next-Action sections into the middle of the V10 R1 entry's fenced Decision block. All were resolved by hand at merge-back and the repair is disclosed here rather than absorbed. **`D-038a`'s mergeability premise is measurably false for tail-appended ledgers, not only for numbered identifiers** — which widens this item from a numbering rule to a question about how concurrent sessions append to shared ledgers at all. | `18_REVIEW/V10/V10_REVIEW_R1.md` `M1`; `DECISIONS.md` `D-038a`; the merge commit's own conflict set | 🔶 **OPEN — POLICY HALF ONLY; the numbering instance is FULLY discharged.** ⚠ **STUDENT-OWED HALF CLOSED — SELF-VERIFIED AT OWNER DIRECTION 2026-08-13** (see item 92 for the `D-003` disclosure). **THE RENUMBERING WAS VERIFIED COMPLETE BY REPO-WIDE SWEEP, not by reading the reviewer's account of it:** `grep` for `item 8[1-5]` across every `.md` in the tree returns **zero V10-scoped hits** — every surviving 81/82/83 reference belongs to **V09 R2**, which correctly keeps those numbers, and items **86, 87, 88, 89, 90** are each present exactly once in the open-items table with the subjects the RENUMBERING DISCLOSURE maps them to. **⚠ ONE CORRECTION AGAINST THE REVIEW, stated rather than absorbed:** `M1` and the disclosure both assert that `04_SCREENSHOTS/V10/INDEX.md` § ESCALATION and `07_MASTERY_REPORTS/V10_MASTERY_REPORT.md` escalation 2 *"cite open item 82"*. **THEY DO NOT, AND NEVER DID.** Both referred to the recipe defect **by description, carrying no item number at all** — verified by grepping `82` in both files, whose only hits are the source `.swf` SHA-256 and an `R = 82.0` chart label. **So there were no stale pointers to correct**; the renumbering could not have orphaned a citation that did not exist. **What was actually owed, and is now done, is the OPPOSITE act:** both artifacts have **gained** a pointer naming open item **87**, recording that it is ✅ CLOSED, that it was `82` on `video/v10`, and that the collision and the `D-038a` gap are carried here at item 91. **Nothing in either artifact is superseded** — these are additions, and each says so. **The policy half remains OPEN and is untouched by this session:** a `DECISIONS.md` amendment requires an owner ruling, and neither a reviewer nor a student session may make one. |
| 92 | **V10 R1** | **`M2` — `A-078` / `C-017` undercount the spoken renderings.** `A-078` heads *"spoken six times"*; `C-017` says *"four of six spoken instances say the tracer."* **`[01:00:20]` — *"75 pips off of the blue tracer"* — is a seventh, and it names the tracer.** Correct census: **five of seven** spoken instances name the blue tracer, one names the LOW/HOW anchor, one is ambiguous. (`[00:54:02]`'s *"25 to 50 pips"* is an eighth distance utterance with no reference object named.) **`A-079`'s separate *"named 13 times"* headline is CORRECT** — `tracer` 13, `blue tracer` 10. **The direction STRENGTHENS `C-017`**: the spoken majority is wider than recorded. Edit, not redo; no conclusion moves | `A-078`, `C-017`, `V10_MASTERY_REPORT.md` §J | ⚠ **CLOSED — SELF-VERIFIED AT OWNER DIRECTION 2026-08-13** (branch `fix/v10-r1-minors`, cut from the integration branch at `9c00a60` after `git fetch --all` confirmed zero divergence, `D-038`). **NOT `CLOSED — VERIFIED`. This round was fixed AND verified by ONE session on the owner's explicit authorisation; it does not satisfy `D-003`, and the distinct status string exists solely so it is never mistaken for an arm's-length verdict.** **`[01:00:20]` WAS RE-DERIVED FROM `02_TRANSCRIPTS/V10/V10_TRANSCRIPT.md` AT SOURCE**, not copied from the review: line 2452 of the body reads *"75 pips off of the blue tracer"*, and `[00:54:02]` (line 2203) reads *"25 to 50 pips the dealer falls into the shadow box"* — an eighth **distance** utterance that names **no reference object** and is therefore recorded in `A-078` and `C-017` **but deliberately NOT counted** in either census. **CORRECTED AT SEVEN SITES, not the four the review named** — a repo-wide sweep for the undercount found three more: `A-078` (heading, marker list, renderings table + the new `[01:00:20]` row, and the *"four of the six"* sentence), `C-017` (table row added; *"Four spoken instances"* → **five of seven**), `V10_MASTERY_REPORT.md` §J, **item 88's own text in this register**, and additionally **`04_SCREENSHOTS/V10/INDEX.md`** (*"the audio gives it six times"*), **`05_HOMEWORK/V10/V10_COMPREHENSION_ANSWERS.md` Q6** and **`02_TRANSCRIPTS/V10/V10_TRANSCRIPT.md` TRANSCRIPTION NOTE 1** (*"given six times"*, with its own six-marker list) — the last being the note that `M4` relies on, so leaving it stale would have left two V10 records disagreeing about the same census. **The comprehension answer was NOT rewritten**: it is a preserved first attempt, so the correction is appended as a block and the original wording stands, per `REMEDIATION_PROTOCOL.md` §2 and the first-attempt rule. **The transcript's VERBATIM BODY IS UNTOUCHED** — only the header note is corrected. **Superseded text retained at every one of the seven sites. NOTHING MOVES:** no marker, no disposition, no `DO NOT CODE` verdict, no grade, no conclusion. `A-078`'s number stays `RESOLVED BY COURSE`, its reference point stays `DO NOT CODE`, and `C-017` stays `UNRESOLVED` — **strengthened**, because a 5/7 spoken majority makes the misspeak reading `C-017` refuses *less* available than a 4/6 majority did. |
| 93 | **V10 R1** | **`M3` — `V10_SOURCE_NOTES.md` §15's absence claim is overstated.** *"No session clock times. Sessions are named constantly; **no hour is ever stated**."* Hours **are** stated — `[00:02:24]` *"at 830"*, `[00:05:09]` *"seven o'clock New York time"*, `[00:42:52]` *"3 o'clock in the morning"*, `[01:03:57]` *"5 6 o'clock at night"*. **None is a session boundary, which is the true and intended claim**, but the sentence as written is falsifiable by a one-line grep and §15 exists precisely so a later session can rely on it. **`A-076`'s parallel sentence is correctly scoped and is the model to copy.** Reword to a session-boundary-scoped claim listing the four incidental times | `V10_SOURCE_NOTES.md` §15 | ⚠ **CLOSED — SELF-VERIFIED AT OWNER DIRECTION 2026-08-13.** **NOT `CLOSED — VERIFIED`** — see item 92 for the full `D-003` disclosure; one session both fixed and verified this, on the owner's explicit authorisation. §15's bullet now reads **"No session-boundary clock time is stated"**, states that sessions are named constantly and **not one is given an opening or closing hour on any clock**, and then **lists all four incidental times with what each actually is** — `[00:02:24]` *"at 830"* (a chart students are being told to stop watching), `[00:05:09]` *"seven o'clock New York time"* (the seminar announcement), `[00:42:52]` *"3 o'clock in the morning"* (the speaker's own readiness, rhetorical), `[01:03:57]` *"5 6 o'clock at night"* — **none of which delimits a session**, which is the claim §15 was always making. **ALL FOUR MARKERS RE-DERIVED FROM `02_TRANSCRIPTS/V10/V10_TRANSCRIPT.md` AT SOURCE**, not copied from the review; all four resolve verbatim at the cited marker. **`A-076`'s parallel sentence was CHECKED as the review directed and is CORRECT AS WRITTEN — it is left untouched and is cited in the fix as the model.** It reads *"V10 states **no clock time for any session**"* and backs it with six specific zero-counts (`7:00`, `3:00 am`, `3:30`, `9:00`, `9:30`, `5:00 pm`, all **0** in the body, `Q-011` §1), so it never overshot. **Superseded text retained in full per `REMEDIATION_PROTOCOL.md` §2.** **NOTHING DOWNSTREAM MOVES:** no rule, machine candidate, ambiguity disposition or backtest rests on this bullet, and the no-session-boundary finding it supports is unchanged and still true. |
| 94 | **V10 R1** | **`M4` — `C-016` does not apply the transcript's own ASR caution to its own evidence.** TRANSCRIPTION NOTE 1 records that *"numeric ranges wobble, and one of them is load-bearing"* and rates the file `MEDIUM–HIGH`. `C-016` rests entirely on two ASR-rendered numbers two seconds apart, **neither printed on any slide**, and argues from them as though capture were certain — inconsistent with the same session's correct treatment of `A-078`, where ASR unreliability on numbers is the express reason to prefer the slide. **The caveat STRENGTHENS the `UNRESOLVED` disposition**: if either figure may be a rendering artifact, no construction over them is safe. Add the caveat; the disposition does not change | `C-016`; `V10_TRANSCRIPT.md` TRANSCRIPTION NOTES 1 | ⚠ **CLOSED — SELF-VERIFIED AT OWNER DIRECTION 2026-08-13.** **NOT `CLOSED — VERIFIED`** — see item 92 for the full `D-003` disclosure. **An ASR CAUTION block is added to `C-016`, and NOTHING ABOVE IT IS SUPERSEDED** — the review is explicit that the omission *"strengthens nothing and undermines nothing in the disposition"*, so this is the **omitted-available-self-caution** class (the V08 R1 `M1` shape), not a correction. The block states that `[01:00:41]`'s *"one-day"* and `[01:00:43]`'s *"three days"* are **both ASR renderings and NEITHER is printed on any slide**, cites TRANSCRIPTION NOTE 1 (*"Numeric ranges wobble, and one of them is load-bearing"*) and the transcript's own **`MEDIUM–HIGH`** self-rating, and concludes it is a **FURTHER independent reason to refuse the reconciliation**: the refused reading is a *construction over the two numerals*, and a construction over figures that may themselves be rendering artifacts is unsafe. **RE-DERIVED, NOT TAKEN ON THE REVIEW'S WORD:** TRANSCRIPTION NOTE 1 and the confidence rating were read at source, and the **absence of any printed holding period was checked against all 32 curated frames via `04_SCREENSHOTS/V10/INDEX.md` — no frame carries one**, which is what makes *"neither is printed"* a verified claim rather than a repeated one. **The block also states what the caution does NOT license**, which the review did not ask for and which matters: it is **not** grounds to discard either figure (`D-030`, `SOURCING_HIERARCHY.md` §3.2 forbid selecting the convenient one), and the contradiction is **over-determined without them** — strike both ASR-suspect figures and `[00:41:45]` *"at least two days"*, `[01:32:07]` *"two days"* and `[01:26:39]` *"three days … maybe one more"* still state the duration three incompatible ways. **The consistency charge is answered directly:** `A-078` invokes ASR unreliability to prefer the slide; here **there is no slide**, so the same unreliability points toward `UNRESOLVED`. `C-016`'s Related section now cites TRANSCRIPTION NOTE 1 and `A-078`. **The `UNRESOLVED` disposition, every marker, every quotation and every figure are UNCHANGED.** Cross-referenced to item **95**, the standing owner question about tagging this class at filing. |
| 95 | **V10 R1** | **NOTE — a standing convention for ASR-only contradictions?** `M4` is the third corpus record resting solely on ASR-rendered numbers with no printed corroboration. **Reviewer question to the owner:** should a `C-xxx` filed on unprinted ASR numerals carry that tag at filing, rather than a reviewer noticing it per lesson? Not a defect in V10 | `V10_REVIEW_R1.md` reviewer question 1 | ℹ️ **NOTE — owner question** |
| 96 | **V10 R1** | **NOTE - `COURSE_PROGRESS.md`'s PROGRESS TABLE has decayed and is now stale for FIVE lessons.** The V10 student session updated the STATUS prose block at `e5262b2` but left the table's V10 row reading `NOT STARTED` with every artifact column `⬜`, against a full committed artifact set. **This is not a V10 defect alone** - the same table reads `AWAITING REVIEW R1` for **V06, V07 and V09** (V06 and V07 are `COMPLETE` per `REVIEW_INDEX`) and `IN REMEDIATION (items 64-66)` for **V08** (also `COMPLETE`). **The prose block above it is maintained; the table below it is not**, so the file now contradicts itself and `REVIEW_INDEX.md` in four places. **Not charged as a MINOR against V10** for that reason. V10's row is corrected by this reviewer; **the other four rows need a sweep**, and the durable fix is to state which of the two blocks is authoritative | `00_SYSTEM/COURSE_PROGRESS.md` PROGRESS TABLE vs its STATUS block and `18_REVIEW/REVIEW_INDEX.md` DECISION TABLE | 🔶 **OPEN - bookkeeping sweep owed. ⚠ WIDENED 2026-08-13 by the V10 R1 fix round: the SAME DECAY IS PRESENT IN THIS FILE.** `REVIEW_INDEX.md`'s own **SEVERITY TOTALS table is stale at V09 R1** — `MINOR 57 / 12 open / 45 closed`, predating **V09 R2's +3** and **V10 R1's +4** — because **neither round posted the per-round arithmetic paragraph** that every round from V07 R1 onward had posted. **So the pattern item 96 names is not confined to `COURSE_PROGRESS.md`: in both files a maintained prose/delta layer sits above an unmaintained table, and the table is the part a reader scans.** Flagged in place under the table rather than silently corrected — reconciling it requires re-auditing the pre-V03 rows carried unreconciled since V02 R1, which is a sweep and not an edit. **The durable fix is the same for both files and should be ruled once:** declare which layer is authoritative, or delete the derived table. |
| 97 | V11 student | ⭐ **`C-018` NEEDS AN OWNER ADJUDICATION — `SOURCING_HIERARCHY.md` §3.2 Case C.** V11 `[00:46:45]` — *"Look where the **averages** are. **There's the mayonnaise. There's the 50.**"* — is Tier 1 speaking on `A-020`, which `§3.4` names as one of the project's three highest-priority reconciliation targets and which is **CLOSED as `Mayo = 200`** on owner attestation + `MMM-NOTES` p.66. **The V11 session filed the conflict and refused to adjudicate it**, because §3.3's *"the recording wins"* cannot close a record when the recording is itself two-ways readable: **the identical phrase *"there's the 50"* means the RSI MARKET BASELINE seven seconds later at `[00:46:52]`**, and `"the 50"` occurs 14 times in V11 with every unambiguous instance being the sub-graph baseline. The frame at `46:45` was extracted **specifically to arbitrate** and shows **four averages with no legend** — `A-020`'s own *Required Research* is still unsatisfied. **`A-020` was neither reopened nor re-closed; it is annotated `CONFLICT — OWNER ADJUDICATION REQUIRED` on its `Mayo = 200` half only.** Its `Blueberry = 800` half (`RESOLVED BY COURSE`, V09) is untouched. **Noted trap:** the quarantined `NOTES.md` for this very lesson asserts *"50 (Mayo)"* (`Q-012` §2) — agreeing with it would be coincidence with a fabricated file, not corroboration. **V12 is the cheapest route to Tier 1 closure: same session, same day, same charts.** | `11_CONTRADICTIONS/CONTRADICTIONS.md` `C-018`; `A-020`; `04_SCREENSHOTS/V11/INDEX.md` §4; `03_LESSON_NOTES/V11_INTERPRETATION.md` Q2 | ✅ **CLOSED 2026-08-13 — `D-041`.** The owner adjudicated and **`C-018` is CLOSED as reading B (enumeration)**: mayo is **not** the 50, and `A-020` is untouched by the utterance. **The V11 session's refusal to adjudicate was correct and its reading was right** — the owner's ruling agrees with the three grounds it gave. Note precisely what this does NOT establish: the owner supplied a **disambiguation of an ambiguous Tier 1 sentence**, not a trump card over Tier 1. **No "Tier 0" exists**, and `SOURCING_HIERARCHY.md` §3.4's re-check obligation on `A-020` **stays live**. ⚠ The same ruling **overturned `A-020`'s ketchup/mustard rows** (now **ketchup = 5, mustard = 13**, inverting the prior record) — a reviewer may put that inversion back to the owner |
| 98 | V11 student | ⭐ **`A-080` — THE RSI PERIOD IS THE BINDING CONSTRAINT ON HALF OF V11, AND BOTH ADMISSIBLE TIERS ARE SILENT.** V11's printed slide is **headed *"Parameters of RSI"***, lists **six** parameters (`0–100`, `70/30`, `80/40`, `60/20`, `80/20`, mid-point `50`) and **does not contain the lookback**. `rsi` occurs 33 times in the audio with no period attached; **no frame among 28 detected screen states** shows a settings dialog or legend; and the **Tier 2 `MMM-NOTES` PDF is also silent** (`D-040` step 2, searched — it describes the TDI's four components with no lookback for any). **The near-miss is the hazard: a session skimming for a parameter block FINDS one, and it does not contain the parameter.** The TDI's distributed default of **13** was refused explicitly, and the trap named — `MMM-NOTES` p.38 lists a **13 EMA**, so a session could reach *"13"* by conflating two indicators and feel sourced doing it. **The cost was MEASURED rather than asserted** (`V11_HOMEWORK.md` §3): across six candidate periods, *"time above 80"* — V11's own **overextended** condition and half of the `[00:36:19]` composite entry — ranges **0.04% → 5.66%, a ratio of 144×**; even adjacent 13 vs 14 differ ~20% relative. **This blocks V11 dimension B, every RSI threshold in `PT-039` §2b, and homework H6. One frame from ANY lesson showing an indicator-properties dialog closes it.** | `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md` `A-080`; `05_HOMEWORK/V11/data/rsi_period_sensitivity_output.txt`; `04_SCREENSHOTS/V11/INDEX.md` §1 | 🔶 **OPEN — watch item for V12+** |
| 99 | V11 student | ⭐ **`PT` NUMBERING COLLISION — self-disclosed, with a proposed resolution the reviewer may reverse.** `BT_V10_0001.md` §9, **this register's item 86** and `LOG.md` reserved **`PT-037`** (the path-length reading of V10's weekly-range claim) and **`PT-038`** (the safety trade) **in prose, with no files**. The V11 session's `PT-037` §0 searched `PRE_REGISTERED/` for existing **files**, found `PT-001…PT-036`, allocated `PT-037`, **and ran it**. **This is exactly the concurrent-allocation hazard `D-038a` consequence 1 names — and it is a second, distinct instance of item 91's finding**, because a `PT` *reservation* is no more git-mergeable than an open-item number. **PROPOSED: V11's file KEEPS `PT-037`** (renumbering a committed, run pre-registration is what `D-027`'s retention rule exists to prevent, and the number appears in four commits, the runner, the output and `BT_V11_0001`); **V10's reservations move to `PT-039` (path-length) and `PT-040` (safety trade)** — a reservation with no file is free to move. **`BT_V10_0001.md` and `V10_REVIEW_R1.md` are NOT edited** (`REVIEW_PROTOCOL.md` §11). **If the reviewer or owner prefers the reverse, `PT-037` is marked `SUPERSEDED — NUMBERING`, re-issued, and its result RETAINED.** The disclosure is appended to `PT-037` §0 and changes nothing in §§1–9. **⛔ THE PROPOSAL ABOVE WAS REVERSED — retained per `REMEDIATION_PROTOCOL.md` §2 as the history, not the state.** | `06_MANUAL_BACKTEST/PRE_REGISTERED/PT-039_…md` (re-issued) §0; `06_MANUAL_BACKTEST/V10/BT_V10_0001.md` §9; item 86; item 91 | ✅ **CLOSED 2026-08-13 — OWNER RULED, AND REVERSED THE PROPOSAL.** ***"Move V11 not V10 since V11 is after."*** **V10 KEEPS `PT-037` and `PT-038`; V11's test is re-issued as `PT-039`** — `SUPERSEDED — NUMBERING`, result **retained in full**, nothing in §§1–9 touched, `BT_V10_0001` and `V10_REVIEW_R1` still **not** edited (`REVIEW_PROTOCOL.md` §11). The proposal reasoned from the **artifact**; the owner ruled on **precedence**. ⚠ **`PT-040` was NOT allocated and remains free** — the reversal was framed as *"V11 moves to 039/040"*, but **V11 only ever held ONE number**; every `PT-038` reference in V11's artifacts points at **V10's** reservation, which never moved. **The self-disclosure is what made the ruling cheap and the session is credited for it** |
| 100 | V11 student | **`SETUP_ISSUES.md` ENTRY FOR `C-018` IS OWED AND NOT DONE.** `SOURCING_HIERARCHY.md` §3.2 Case C requires a genuine Tier-1-vs-Tier-2 conflict to be logged in `SETUP_ISSUES.md` as well as in `CONTRADICTIONS.md`. **`SETUP_ISSUES.md` is a POLICY ledger under `D-038a` and may not be written from a task branch**, so the V11 session recorded the obligation instead of quietly skipping it (`C-018` § "A NOTE ON `SETUP_ISSUES.md`"). **Must be done at the integration step.** | `11_CONTRADICTIONS/CONTRADICTIONS.md` `C-018`; `D-038a`; `SOURCING_HIERARCHY.md` §3.2 | ✅ **CLOSED 2026-08-13 — DISCHARGED BY `D-041`, NOT PERFORMED.** §3.2 **Case C** is *"genuine conflict — do **not** adjudicate, log it, surface to the owner."* The owner has now adjudicated and `C-018` is closed, so **there is no live conflict for a `SETUP_ISSUES.md` entry to describe.** Reasoned in `D-041` consequence 5 on the integration branch rather than silently skipped. **The V11 session was right to record the obligation instead of quietly skipping it** |
| 101 | V11 student | ⭐ **A `D-031` ARM-B DESIGN DEFECT THAT THE WHOLE `PT` FAMILY INHERITS, found at run time.** `PT-039` is a **day-boundary** test, and Arm B shifts corpus stamps `+1 h` during US DST. The Friday close therefore lands at 18:00 and the Sunday open at 18:00 **on the arm's own clock**, so for every DST week the **Monday** session day `[Sun 17:00, Mon 17:00)` loses its first hour (**92/96 buckets → excluded by the completeness rule**) and a **junk Saturday** session day materialises holding the stray Friday hour (**4/96 → excluded**). **Arm A excluded 11 session days; Arm B excluded 245**, and Arm B's result therefore rests on a sample **missing most DST-period Mondays** — a systematic weekday loss in a test whose own `N3` shows the effect varies strongly by time of day. **The two arms nonetheless agree within 1.7 pp and Arm A is the pre-registered primary cell, so no V11 verdict moves.** But **`D-031` Arm B is not a clean robustness check for ANY session-day-unit test**, and `PT-003`, `PT-004`, `PT-005`, `PT-006`, `PT-007`, `PT-014`–`PT-018`, `PT-020`, `PT-021` all use the `C-1` session day. **Reported as a defect in `PT-039`'s design, NOT corrected in the pre-registration.** | `06_MANUAL_BACKTEST/V11/BT_V11_0001.md` §9, §13; `PT-039` §5; `mmm_lib.py` convention `C-1` | 🔶 **OPEN — affects the PT family, not only V11** |
| 102 | V11 student | **NOTE — `Q-011`'s "one generator" finding REPRODUCES on a second lesson, by exact `diff`.** V11's quarantined `RULES.md` is **V01's file with SIX identifier strings swapped**: an exact `diff` returns **12 differing lines — six substitutions — and ZERO content lines.** Every rule, timestamp, parameter, ambiguity and "coding implication" is byte-identical across two lessons recorded three weeks apart on entirely different subjects. **This upgrades the claim from *inferred from a normalised hash* (`Q-007`) to *twice-demonstrated by exact diff* (`Q-011`, `Q-012`).** Also: V11 is the **third** confirmed instance of the sixth failure mode — a genuine frame carrying an invented description — and the **first in which the misdescribed frame is a TITLE CARD**, i.e. contains no chart content at all. It is indexed as *"Asian Box accumulation range with 5, 13, 50, 200, and 800 EMAs."* | `00_SYSTEM/QUARANTINE_REGISTER.md` `Q-012` §1, §3a | ℹ️ **NOTE — pattern confirmation** |
| 103 | V11 student | **NOTE — a MEASUREMENT correction future audits should inherit.** The `Q-012` token census was nearly wrong: a naive `grep -ci "EMA"` over the raw transcript returns **11** (matching *email*, *them a*, *problem*) and `grep -c "9:30"` returns **3** by matching **`[HH:MM:SS]` timestamp lines**. The correct figures require **stripping marker lines and using word boundaries**, after which `EMA` = **0** and every clock time = **0**. **This session made the error and caught it before it reached a record**, and the method is stated inside `Q-012` so the next per-lesson audit inherits it rather than re-deriving it. | `00_SYSTEM/QUARANTINE_REGISTER.md` `Q-012` § "Measurement note" | ℹ️ **NOTE — method** |
| 104 | V11 student | **NOTE — V10's END-CARD DATE PREDICTION IS CONFIRMED, from inside V11.** V10's carry-forward (b) recorded that V10's final slide — **printed, never spoken** — reads *"Looks like I will have a session for Easter Sunday… So same time next week"*, and that Easter 2012 was **2012-04-08**, exactly V11's filename date. **V11 corroborates it in audio V10 could not have anticipated**: `[00:25:33]` *"I figured it was **sunday** and it was **easter**."* **This is the corpus's first cross-lesson dated continuity check predicted in advance and then confirmed by independent in-recording evidence**, and it is a genuine if small validation of `D-017` §2's ordering, which until now rested on filenames and week labels. | `07_MASTERY_REPORTS/V11_MASTERY_REPORT.md` § carry-forward (b); `COURSE_PROGRESS.md` V11 GATE (b) | ℹ️ **NOTE — ordering evidence** |
| 105 | V11 student | **`A-039`'s five-lesson debt is PARTIALLY discharged and the reviewer should check whether the narrowing is generous.** V10 `[01:13:03]` promised the TDI *"next week"*, and the carry-forward said **if V11 teaches it, `A-039` closes.** V11 **does** teach it — 25 minutes, six printed slides, eight substantive points — so *"displayed, not taught"* is retired. **But `A-039` NARROWS rather than closes**, because the lesson supplies **no RSI period (`A-080`), no TDI component periods, and no volatility-band settings** — and `[00:32:34]` promises *"I'm going to explain the TDI in a minute"* and **the file ends 18 minutes later without the band or signal-line treatment.** The V11 session's own self-assessment flags this as a place it may be **over-crediting** (`V11_INTERPRETATION.md` Q8.3): if V12 delivers the bands, V11's RSI section is a prologue rather than a lesson. | `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md` `A-039` status change; `V11_INTERPRETATION.md` Q8 | 🔶 **OPEN — reviewer judgement, and a V12 watch item** |
| 106 | V11 student | **NOTE — `C-017`'s printed-vs-spoken question gets TWO more instances, and they point OPPOSITE ways.** V10's carry-forward (f) asks the owner to rule on printed-vs-spoken precedence, the corpus having no standing rule. **V11 supplies both polarities.** (i) **`A-081`** — the `Trade Strong` slide prints *"I will not overleverage my account"* and the **speech adds *"I will not take a 25 risk on one trade"***: **speech is the SUPERSET**, and the added figure carries **no unit** in either medium. (ii) **`Q7`** — the `POSITIVE TREND` slide prints *"Begins Upside Acceleration"* and **the speaker reads it and repudiates it**: *"they call that trend acceleration… but we know better: trend acceleration is a sucker's play"*, having already disowned the deck's provenance (*"maybe 15 years ago… I'm not even sure these slides came from that guy"*). **⭐ (ii) is evidence AGAINST a simple "print beats speech" rule**: adopting it would make doctrine of a slide the instructor rejected on the record. **No `C-xxx` is opened for (ii)** — a speaker disagreeing *and saying so* is the method being stated, not two asserted claims. | `A-081`; `V11_INTERPRETATION.md` Q7; `V11_SOURCE_NOTES.md` §4f, §5.4; `C-017` | ℹ️ **NOTE — supports the owner ruling requested at V10 carry-forward (f)** |
| 107 | V11 student | **NOTE — `A-077` (the lock) and `A-004` (the level) were both CHECKED against V11 and NEITHER ADVANCED.** Recorded as **negative results**, not as unchecked, because item 89 designated `A-077` a *"watch item for V11+"*. **`A-077`:** V11 attaches no number to *"price has moved away and confirmed"*; it restates the entry protocol six times and the anchor distance four times and supplies no real-time confirmation threshold for the lock. (V11's `[00:14:31]` hold-duration claim **is** a real-time confirmation threshold — but for a **candidate low**, not for the lock, and the two are not conflated.) **`A-004`:** V11 uses `level three` **11 times** and says at `[00:29:52]` that *"the levels can actually be counted inside the indicator"* — suggestive, not a definition, and **doubly blocked**, since counting them inside the indicator needs `A-080`'s period. `[00:47:31]`–`[00:49:52]` counts three touches **at a level** without saying how the level is located. **V10's observation that the course may route around `A-004` rather than define it is STRENGTHENED by V11.** | item 89; `A-077`; `A-004`; `V11_MASTERY_REPORT.md` § carry-forward (d), (e) | ℹ️ **NOTE — negative result, carried forward** |
| 108 | V11 student | **NOTE — a validator failure occurred in this session and is recorded rather than hidden.** The first `BT_V11_0001.md` commit shipped **without** the `EVIDENTIAL`/`DESCRIPTIVE` classification `BACKTEST_EVIDENCE_STANDARD.md` requires, because the validator was run **before** the file was staged rather than after. `validate_project.py` caught it on the next run and it was fixed in the following commit, with the cause stated in that commit message. **The durable lesson is ordering, not the rule**: `stage → validate → commit`, never `validate → stage → commit`. Recorded because the branch was pushed in the failing state for one commit. | `06_MANUAL_BACKTEST/V11/BT_V11_0001.md` §1a; the two commits | ℹ️ **NOTE — process, self-reported** |
| 109 | **V11 R1** | ⭐ **`M1` — A CATEGORICAL CLAIM ABOUT THE FRAMES IS FALSE, AND V11'S OWN FRAME 14 FALSIFIES IT.** Six artifacts state that **no frame in the lesson shows an indicator legend or a settings dialog**. **`V11_00-27-35_can-you-decide-cluttered-subgraph-chart.png` carries a full MT4 legend stack, legible without magnification: `GBPUSD,H1`, `RSI(21) 57.5053`, `ATR(14)`, `CCI(14)`, `MACD(12,26,9)`, `Sto(5,3,3)`, `Mom(N)`, `AO`.** `INDEX.md`'s row for that frame records the **pane count** (*"six stacked sub-graph indicator panes"*) and not the legends, against §8's rule that every frame was *"opened and looked at before it was named"*. **⭐ `A-080`'s DISPOSITION IS CORRECT AND DOES NOT MOVE, and the reviewer verified its substance on both admissible tiers with a wider search than the submission ran** — the chart is the lesson's **disowned anti-example** (`[00:27:30]` *"this was Cars chart when i met them"*; `[00:27:42]` *"absolutely ridiculous"*; `[00:27:54]` *"get rid of all this crap"*), it is on **`H1`** not the lesson's 15-minute frame, and the instructor's **own** charts (`46:45`, `47:35`, opened by the reviewer) carry **no legend at all**. **But `RSI(21)` is a NEARER near-miss trap than the `13` `A-080` names, and it sits inside V11's own curated frames** — and the V12 session is explicitly instructed to hunt frames for exactly this. `A-080` even illustrates its own point with the phrase *"RSI(2), RSI(9) and RSI(21)"*, unaware it was describing its own screenshot folder. **REQUIRED:** rescope the six sentences to *"no frame of the INSTRUCTOR'S OWN chart shows a legend or a period"*; add **`RSI(21)`** to `A-080`'s named-trap list beside `13`, with the three reasons it must not be adopted; record the legend stack in `INDEX.md`'s frame-14 row. **Superseded text retained** (`REMEDIATION_PROTOCOL.md` §2). **`A-080`'s status does NOT change** | `A-080`; `V11_SOURCE_NOTES.md` §4b; `V11_INTERPRETATION.md` Q3; `04_SCREENSHOTS/V11/INDEX.md` §1 and row 14; `V11_MASTERY_REPORT.md`; `LOG.md`; item 98 | 🔶 **OPEN — MINOR** |
| 110 | **V11 R1** | **`M2` — `C-018` / item 97's *"every unambiguous instance of 'the 50' is the sub-graph baseline"* is FALSE, and the correction RUNS IN THE CLAIM'S FAVOUR.** The **count is right** — the reviewer measured exactly **14**, word-boundary, markers stripped — but `[00:12:42]` *"You got in right before the shift candle and **you were out to the 50 in no time**"* is a counterexample: it is at minute **12**, **fourteen minutes before RSI is introduced at `[00:26:18]`**, inside a price-chart markup discussion, and *"out to"* is destination language — price does not travel *out to* an oscillator reading. Under `D-041` it is the **water / 50 EMA**. **⭐ This STRENGTHENS reading B:** it establishes that *"the 50"* in this very lesson already denotes a **price-pane moving average** in at least one place, which is a **fourth independent ground** for the enumeration reading the session held and the owner confirmed — one the session had in its own transcript and did not use. **REQUIRED:** append the correction to `C-018` and mirror it in item 97; state that it supports reading B. **`C-018` stays `CLOSED`.** Owed because `SOURCING_HIERARCHY.md` §3.4's re-check on `A-020` is **live** and the session performing it will read this sentence | `C-018`; item 97; `V11_TRANSCRIPT.md` `[00:12:42]`, `[00:46:45]`, `[00:46:52]` | 🔶 **OPEN — MINOR** |
| 111 | **V11 R1** | **`M3` — `pt039_output.txt` is still TITLED `PT-037`, with no banner.** Line 2 reads *"PT-037 — V11 -- how long must the low hold?"*; the rename was `{pt037_output.txt => pt039_output.txt}` with **zero content change**, so a reader who opens the file sees the old number as its title and nothing explains it. **Not editing the run's body is CORRECT** — it is committed evidence and `D-027`'s retention rule protects it. **What is owed is a PREPENDED BANNER**, in the same `SUPERSEDED — NUMBERING` form the pre-registration itself uses. **This is the only un-annotated stale `PT-037` reference in the tree**; the reviewer swept every occurrence repo-wide and every other one is either **V10's (correct, and verified untouched)** or explicitly marked history | `06_MANUAL_BACKTEST/V11/data/pt039_output.txt` line 2; `PT-039_…md` top banner; item 99 | 🔶 **OPEN — MINOR** |
| 112 | **V11 R1** | **`M4` — the mastery report states the owner's ruling with the WRONG NUMBER.** `07_MASTERY_REPORTS/V11_MASTERY_REPORT.md:391`, inside the ✅ resolution block for escalation 3: *"V11's test is re-issued as `PT-039`. **V10 keeps `PT-039` and `PT-038`.**"* — **V10 keeps `PT-037`.** It is contradicted five lines earlier in the same block, in `LOG.md`, in `COURSE_PROGRESS.md`, in item 99 and in the pre-registration, so it is a typo — **but it is the single sentence in that file that states what the owner ruled**, and as written it gives V10 and V11 the same number. **It is invisible to a `PT-037` grep, because the defect is that number's ABSENCE.** Correct it, marked as a correction | `07_MASTERY_REPORTS/V11_MASTERY_REPORT.md:391`; item 99 | 🔶 **OPEN — MINOR** |
| 113 | **V11 R1** | **`M5` — the committed run output prints TWO DIFFERENT SEEDS.** `pt039_output.txt` line 10's provenance banner reads `seed : 20260812` — inherited from `mmm_lib.SEED`, the `COMMON_PROTOCOL.md` §5 batch constant — while line 19 and `run_pt039.py:23` both use **`20260813`**, which is what `PT-039` §4 pre-registered and what `N4`'s 1,000 shifts actually ran on. **No number in the file is affected**, but a reproducer following the header banner **cannot reproduce `N4`**. V11 is the **first** `PT` to override the batch seed (`PT-036` prints only the library value and matches it), so the banner had never contradicted anything before. **The durable fix is in the LIBRARY, not in V11:** `mmm_lib.provenance_header()` should print the **calling runner's** seed. That is a tooling/policy change for the integration branch — see reviewer question 1. V11's own half is to state the operative seed in `BT_V11_0001` §1a or in a banner on the output | `06_MANUAL_BACKTEST/V11/data/pt039_output.txt` lines 10, 19; `scripts/run_pt039.py:23`; `scripts/mmm_lib.py:116`, `:898`; `PT-039` §4 | 🔶 **OPEN — MINOR** |
| 114 | **V11 R1** | **NOTE — the ketchup/mustard inversion was independently re-checked by this reviewer, who DECLINES the escalation `D-041` consequence 7 invited; and `D-042` landed mid-review and reached the same result by a different route.** The reviewer's body-only census across **V01–V11** returns `ketchup` **0×** and finds V04's two `mustard` uses attach **no number**, so `D-041`'s operative claim — *"No Tier 1 statement attaches a period to ketchup or mustard anywhere in V01–V11"* — **is verified, not inherited**. The one near-miss is **V01 `[00:19:24]`** *"the man is the **water** that **catch up** in the **mustard**"*, which V01's own `TRANSCRIPTION NOTES` already call the only such vocabulary in V01 and *"too garbled to source anything from"* — it attaches **no period to anything**. **⭐ `D-042` (`195970d`) was committed to integration while this review was in progress and the reviewer did not have it**; it ran the same search on the owner's conditional instruction, returned the same exhaustive negative, and **named the same two near-hits independently**. **Two sessions, two branches, two search designs, one negative — `D-041` is doubly verified.** ⚠ `D-042` §3's **new** conflict (V07 `[00:25:34]` *"this yellow one is a five moving average"* vs the owner's `5 = red`) is about **COLOURS**, is filed as `SETUP_ISSUES.md` `I-011`, and **no V11 artifact, record, number or verdict depends on it**. **Charged against no one — `D-041`/`D-042` are integration-branch policy entries, not V11's work** | `D-041` Evidence block; `D-042` §1, §3; `I-011`; `V01_TRANSCRIPT.md` `[00:19:24]` + TRANSCRIPTION NOTES; `V11_REVIEW_R1.md` § `N1` IN FULL | ℹ️ **NOTE — verified negative, escalation checked and DECLINED** |
| 115 | **V11 R1** | **NOTE — `PT-039`'s `N1` is the CONSERVATIVE construction, and the reviewer tested the alternative the submission does not discuss.** §4 defines `N1` as `P(FINAL)` over **all** candidates while `P(30)` is taken over the `R ≥ 30` eligible set. The eligibility-matched alternative, computed independently: `P(FINAL | R ≥ 30) = 3.33%` (vs `N1 = 3.43%`), which would make `M1a` **+15.91 pp** rather than +15.80 — a **better** result for the claim. `P(FINAL | R ≥ 90) = 3.26%` → **+28.16 pp** vs +27.98. **`M1a` stays `PARTIALLY SUPPORTED` under both constructions.** The verdict is robust to the design choice and the choice was not made to flatter the result | `PT-039` §3.1, §4 `N1`; `BT_V11_0001` §3; reviewer re-derivation | ℹ️ **NOTE — design check, favourable** |
| 116 | **V11 R1** | **NOTE — `PT-039` §4 `N2`'s feature test is UNDER-SPECIFIED at `T* = 90`, and both readings agree.** The rule requires *"the mean increment per minute of the **two adjacent UNNAMED intervals**"*, but at `T* = 90` **only one adjacent interval is bounded by unnamed thresholds**, because 120 is named. The runner used one neighbour (excess **−1.23 pp**); the reviewer used both, treating `(90,120]` as available (**−0.20 pp**). **Both are far below the +5 pp bar and both return *no feature*, in both `D-031` arms.** `COMMON_PROTOCOL.md` §9 rule 7 does not bite — the pre-registration is silent, not contradicted. **Specify the boundary case in the next `PT` carrying an `N2` feature test** | `PT-039` §4 `N2`; `pt039_output.txt` M1c block; `BT_V11_0001` §5 | ℹ️ **NOTE — forward requirement for the next `PT`** |
| 117 | **V11 R1** | **NOTE — available Tier 2 corroboration on the range parameters is not cited.** `MMM-NOTES` **pp.48–49** give *"**RSI in the 80 to 40 range**"* among the features of an uptrend and *"**RSI in the 60 to 20 range**"* for a downtrend — independent support for two of V11's six printed parameters. **Nothing changes**: Tier 1 already carries all six **printed AND spoken** and outranks Tier 2. Recorded because the submission searched that document for the **period** (correctly, and correctly found nothing) without noting what it **does** supply on the adjacent question | `EXTERNAL_Mauro_MMM_seminar_notes_TEXT_EXTRACT.md` pp.48–49; `V11_SOURCE_NOTES.md` §4b.5; `A-080` | ℹ️ **NOTE — omitted available corroboration, non-material** |
| 118 | **V11 R1** | **NOTE — a transcript labelling convention worth stating once.** `COVERAGE` reports the largest gap as *"14 s, ONCE, at `[00:31:17]`"*, labelling it by the marker that **ends** it; the prose beneath describes it as sitting between `[00:31:03]` and `[00:31:25]`, which spans **two** gaps (14 s then 8 s). The reviewer re-measured the whole block independently: **643 markers, 643 distinct, STRICTLY increasing, max gap 14 s from `[00:31:03]` to `[00:31:17]`, final marker `[00:50:56]` against 3056.93 s measured audio.** **Every figure in the block is correct**; only the labelling convention is unstated. State it once in the next transcript header | `V11_TRANSCRIPT.md` § COVERAGE; reviewer re-measurement | ℹ️ **NOTE — convention, no defect** |
| 119 | **V11 R1** | **NOTE — item 108's *"pushed in the failing state"* is NOT verifiable by repository inspection, and the validator failure itself IS verified.** Push timing is not recoverable from git, so this reviewer could **neither confirm nor refute** that half. **The substance is confirmed at source:** `git show 735a458:…/BT_V11_0001.md` contains **zero** `EVIDENTIAL` tokens, `d2c1d57` adds **eight**, and `scripts/validate_project.py:412` enforces `("DESCRIPTIVE", "EVIDENTIAL", "INVALID")` on backtest observation files — so `735a458` **would have failed the validator**, exactly as reported, and the stated cause and the durable lesson (`stage → validate → commit`) are both right. **NOT CHARGED — volunteering a fact the record cannot prove is the opposite of understatement** | item 108; commits `735a458`, `d2c1d57`; `scripts/validate_project.py:412` | ℹ️ **NOTE — self-report accepted, one half unverifiable** |
| 120 | **V11 R1** | **NOTE — there is NO *"V14-not-V13"* recommendation anywhere in V11's artifacts, and the V12 reasoning HOLDS on every limb.** `SOURCE_MANIFEST.md` gives **V12 = `Bootcamp1 Wk4 040812 Part2 (55mins).swf`** — *the same session date as V11*, `CERTAIN` provenance — V13 = `Wk5 041512 Part1`, V14 = `Wk5 041512 Part2`; **nothing in the submission proposes skipping V13 or reordering the two**, and the only forward pointer is `V11_INTERPRETATION.md` Q5's neutral *"V12/V13 is where the forward pointer lands"* for `A-011`. **The V12 case was sanity-checked limb by limb and every limb holds:** same session ✅; the week-4 assignment promised at `[00:00:46]` and never given (the file ends mid-sentence at `[00:50:56]`) ✅; the TDI proper promised at `[00:32:34]` and not delivered in the remaining 18 minutes ✅; cheapest route to `A-080` and to `A-020`'s still-unsatisfied *Required Research* ✅; speaker still to be tested, not assumed ✅. **⭐ `M1` SHARPENS the V12 instruction rather than weakening it:** the V12 session must check **whose** chart a legend belongs to before reading a period off it. Recorded so a later session does not go looking for a recommendation that was never made | `SOURCE_MANIFEST.md` rows V12–V14; `COURSE_PROGRESS.md` V12 GATE (a)–(h); `V11_TRANSCRIPT.md` `[00:00:46]`, `[00:32:34]`, `[00:50:56]` | ℹ️ **NOTE — recommendation sanity-checked, HOLDS** |
| 121 | V12 student | ⭐ **`A-080` CLOSES `RESOLVED BY COURSE`, AND IT CLOSES ON THE AUDIO — NOT ON THE FRAME THE WHOLE PROJECT PREDICTED.** The course author states the RSI lookback **four times** — `[00:07:24]` *"I like the RSI line to be set at **21**"*, `[00:07:53]` *"21 slows it down"*, `[00:08:09]` *"**21 closing periods back** for our line… **instead of 14 periods**"*, `[00:10:51]` *"this line set to 21, 21 look back periods, that's all"* — gives the **rationale**, contrasts it with the **default it replaces**, and declares it the group's **template preset** (`[00:07:38]`). Confirmed by an independent Whisper `small.en` pass on both passages. **⚠ `A-080`'s *Required Research* and `COURSE_PROGRESS.md` V12 GATE (b) both asked for a properties dialog, a Navigator entry or a legend. NONE EXISTS — measured, not assumed: all 672 sweep frames scanned at mean-difference threshold 2.0, a THIRD of the 6.0 used for screen-state detection, returning 27 states plus three announcement text edits and no modal window; and all five legible legends transcribed in `INDEX.md` §1 carry no parenthesised parameter.** ⭐ **The durable lesson for the gap audit: a *"look for a frame showing X"* instruction should be written *"look for X"*, because this corpus's parameters live in speech.** | `A-080`; `V12_SOURCE_NOTES.md` §3; `04_SCREENSHOTS/V12/INDEX.md` §1, §3 | ✅ **CLOSED by the lesson — reviewer verification invited** |
| 122 | V12 student | ⭐ **ITEM 109's `RSI(21)` TRAP RESOLVED — THE INADMISSIBLE SOURCE WAS RIGHT, AND REFUSING IT WAS STILL CORRECT.** Item 109 required `RSI(21)` be added to `A-080`'s named-trap list because V11's frame 14 carries it on **the lesson's disowned anti-example, on `H1`**, and instructed V12 to *"check whose chart it is before reading a period off it."* **The instruction was followed and the number is the same.** Stated precisely because the tempting conclusion is wrong: **`A-080` does NOT close on frame 14 and nothing here makes it admissible** — it closes on V12's audio, from the course author, about his **own** preset. **The agreement is explicable rather than lucky**: that chart belonged to a student presumably given the same student folder and template, so `RSI(21)` on it is what a group preset *predicts*. ⭐ **The process point is the durable one — item 109's rule COST NOTHING and would have saved everything in the other branch: had the anti-example carried `RSI(13)`, the TDI's shipped default and `A-080`'s originally-named trap, adopting it would have produced a WRONG NUMBER WITH A SCREENSHOT BEHIND IT.** The value of a precaution is not measured by whether it turned out to be needed | item 109; `A-080` V12 update; `V12_SOURCE_NOTES.md` §3 | ℹ️ **NOTE — prior finding vindicated** |
| 123 | V12 student | ⭐⭐ **`A-020`'s MAYO ROW REACHES TIER 1 AND `A-064` CLOSES — PRINTED AND SPOKEN, SAME INSTANT.** `[00:31:22]`–`[00:31:27]`, **two adjacent sentences, one object**: *"Price comes out and it's **held by the mayonnaise** perfectly. **Held by the 200**, okay."* — and the slide **on screen at that second** prints **`TDI VB BREAK, PRICE HELD BY 200`**, so **the identification survives without the audio.** Corroborated independently five minutes earlier on a different chart (`[00:26:20]`–`[00:27:19]`: *"perhaps a **200 EMA**… a spike to **the mayonnaise**… people take a **close below the 200** as a trade signal"*), and the word is **PRINTED** — `Shark Fin Hold The Mayo`, burned `26:11` — at the same second the ASR renders it *"hold the **mail**"*, which closes `A-064`'s three-rendering hazard by demonstration. **This is what V12 GATE (b) asked for and it is stronger than what was asked for: a legend would have shown a period on a line; this is the speaker joining the nickname to the period himself.** **Second nickname ever to reach Tier 1 after blueberry = 800, and the FIRST from the course author.** ⚠ **`D-043` is AGREED WITH, not amended — only the WARRANT moves, not the value** — and `D-042` §1's exhaustive negative is **unaffected**: `ketchup`, `mustard`, `blueberry`, `raspberry` all **0×** in V12. Ketchup, mustard and water stay owner-attested and stay on `SOURCING_HIERARCHY.md` §3.4's list | `A-020`, `A-064`, `C-018`, `D-043`; `V12_SOURCE_NOTES.md` §5; `04_SCREENSHOTS/V12/INDEX.md` frames 16, 19 | ✅ **CLOSED by the lesson — reviewer verification invited** |
| 124 | V12 student | ⚠️ **THE COLOUR AXIS WAS DELIBERATELY NOT UPGRADED, AND A REVIEWER SHOULD CHECK WHETHER THAT RESTRAINT IS RIGHT OR EXCESSIVE.** Two frames show price held at a **WHITE** line, one captioned `Shark Fin Hold The Mayo` and one captioned `PRICE HELD BY 200` — which is consistent with `D-043`'s **mayo = 200 = white**, a row currently resting on owner attestation plus the `[TOOLING]` value `color=16777215`. **This session recorded it as corroboration and REFUSED to move the warrant**, on the ground that no legend on either frame says the white line is that line, that each chart carries several lines (white, cyan, red, yellow), and that `D-030` forbids closing the gap by eye. **The reviewer may hold that this is over-cautious** — the caption names the 200, the visible thing holding price is white, and no other line is doing the holding. **Recorded as a judgement call, not as a finding**, because it runs the *opposite* way to every other disposition in this pass and the session's reasoning was explicitly *"refusing the free upgrade is the same discipline that made item 109 right"* | `D-043` §1; `V12_SOURCE_NOTES.md` §10.3; `A-020` V12 update; item 109 | 🔶 **OPEN — reviewer judgement invited** |
| 125 | V12 student | ⭐ **`C-019` OPENED: THE ADMITTED NOTES NAME THE WRONG LINE FOR `blood in the water`, AND THE TIER 3 SECTION HAD GUESSED RIGHT.** `MMM-NOTES` p.46 lists *"the Market base line cross (**referred to as Blood in the Water**)"*; **V12 puts it on the TRADE SIGNAL LINE**, printed (`19:06`, *"Fin Goes Back Under The Waterline and Crosses The Signal (Red, Blood In The Water)"*), spoken (`[00:20:00]`), and demonstrated a third time on a worked chart (`[00:31:34]`). **Different lines and different rungs of the same three-rung ladder** — V12's *second* rung is the MB break (`[00:30:45]`, printed `29:11`). `SOURCING_HIERARCHY.md` §3.2 **Case A** + §3.3: the recording wins; `A-031` and `A-032` close and the Tier 2 basis is **REPLACED, not supplemented**. ⭐ **The finding worth more than the fact:** `EXTERNAL_VOCABULARY_REFERENCE.md` §5.7's own **Tier 3** paragraph reasoned from V04's *"the secondary line"* that the bloodline *"would be the **red Trade Signal Line**"* — **correct** — while the **normative Tier 2** document was wrong, and §9.2 had labelled the Tier 2 answer *"a lead for the promised TDI lesson, **not an answer**"*. **Had it closed `A-031` on the only definition anyone could find, the corpus would now carry the wrong line for its own entry trigger.** This is the second time in two days `D-040`'s machinery caught an error by forbidding a session to resolve something it could have resolved (`D-043` §3 is the first) | `C-019`; `A-031`, `A-032`; `EXTERNAL_VOCABULARY_REFERENCE.md` §5.6, §5.7, §9.2; `MMM-NOTES` pp.45–46 | ✅ **OPENED AND RESOLVED — reviewer verification invited** |
| 126 | V12 student | ⛔ **`PT-040` RETURNED `MATERIAL` AND THE SESSION'S OWN HEADLINE FINDING DID NOT BUY WHAT IT WAS SUPPOSED TO BUY.** `A-080`'s closure was meant to unblock V11's RSI half. `A-084` — opened this session — asks whether the line plotted in the TDI sub-window **is** `RSI(21)` or **a smoothing of it**; V12 says only *"TDI is developed off of the RSI"*, which is lineage, not identity. `PT-040` measured the **side disagreement** between `RSI(21)` and `MA_k(RSI(21))` at every threshold V11 prints, 24,730 M15 bars: **`M = 10.481 pp` at `k=5, t=50`, and `5.16 pp` even at `k=2` — the shipped TDI's own default.** Pre-registered bands `≤2 / 2–5 / >5`. **`A-084` is PROMOTED TO AN ACTIVE BLOCKER and V11's RSI threshold claims STAY BLOCKED. `A-080`'s closure is NECESSARY AND NOT SUFFICIENT.** ⭐ **The boundaries were committed at `83110f1`, before `run_pt040.py` existed** — verifiable because that commit contains the design and no runner — **and `M = 10.48` sits close enough to a defensible-sounding *"10 pp"* that a post-hoc boundary would have been a live temptation.** The damage is concentrated at `t = 50`, which is V11's bias baseline and the single most-used RSI rule in the corpus. Both `D-031` arms agree to **0.000 pp**, `W-B` agrees (10.66), the simple-average RSI variant agrees (12.15) | `PT-040`; `BT_V12_0001.md` §3; `A-084` | ✅ **REPORTED — reviewer verification invited** |
| 127 | V12 student | ⭐ **`PT-040` IS THE FIRST TEST SINCE ITEM 101 FOR WHICH `D-031` ARM B IS A CLEAN ROBUSTNESS CELL, AND IT COMES BACK CLEAN.** Item 101 found Arm B corrupts any test whose **unit of analysis is the session day**, because the ±1 h DST shift breaks the 96-bucket completeness rule. **`PT-040`'s unit is the BAR** — no session-day construction, no completeness rule, no `C-1` boundary, no per-day exclusion — and `PT-040` §3.4 **pre-registered both** that item 101 cannot bite **and** that any material arm disagreement would be **a TOOLING BUG, not a finding**. **Measured difference: `0.000 pp`, exactly.** That is positive evidence for `mmm_lib.shift_to_arm`, recorded beside item 101's negative one, and it is offered as a **template for scoping future `PT` designs**: item 101 does not condemn Arm B generally, it condemns Arm B *for session-day units* | item 101; `PT-040` §3.4; `BT_V12_0001.md` §4 | ℹ️ **NOTE — item 101 scoped, favourable** |
| 128 | V12 student | ⭐⭐ **`A-082`'s PREMISE IS FALSE — AND THIS SESSION ASSERTED THE SAME FALSEHOOD FIRST AND WAS FALSIFIED BY RUNNING ITS OWN SWEEP.** `A-082` reads *"referred to as already existing, **never specified**"*. `COURSE_PROGRESS.md` V12 GATE (e) named the command; it was run. **`flash ?cards?`, word-boundary, markers stripped: 119 occurrences across 18 of 21 lessons** — and **V03 TEACHES them**: `[00:40:57]` *"I asked you last week to make **40 flash cards**"*, `[01:02:41]` *"**the flashcards are on a 15 minute**"*, `[00:53:04]` *"you should have… flashcards **that are labeled**"*, `[01:04:20]` *"having a flashcard of a **loser** is not going to help you"*, `[01:06:55]` the timeframe rule generalised. **`A-082` is REFRAMED, not closed** — its *content* is `A-011`/`A-002`/`A-007`/`A-076`, all open. ⭐ **THE PROCESS FINDING IS BIGGER THAN THE FLASHCARDS.** `A-082` was raised by **V11 against already-ingested, already-transcribed, already-REVIEWED material**; the claim was **reachable and wrong on the day it was written** and **survived V11's own pass and V11 R1**. **What caught it was a carry-forward that named the command — and the V11 session's explicit disclosure that it had NOT run the sweep.** **This session's own first draft of the gate-(e) row asserted *"V11 (×1) and V12 (×1) only… specified nowhere in the entire corpus"***, written from a local census where `\bflashcard\b` returns 0 because it does not match the plural; superseded text retained in `V12_SOURCE_NOTES.md` §9 and §9a | `A-082`; `V12_SOURCE_NOTES.md` §9a; `V03_TRANSCRIPT.md` `[00:40:57]`–`[01:06:55]`; `COURSE_PROGRESS.md` V12 GATE (e) | ✅ **DISCHARGED — and it overturned the record it was checking** |
| 129 | V12 student | ⭐ **A GAP-AUDIT ITEM FOR V13/V14, GENERALISED FROM ITEM 128 AND DELIBERATELY NOT RUN.** *A record asserting "the corpus never says X" is only as good as the sweep behind it, and **late-raised records are systematically the least likely to have had one*** — a session working on lesson *N* is looking at lesson *N*, and asserting a negative over V01–V21 costs a search it did not budget for. **Five candidates are named with the cheap test for each, and NONE is asserted to be wrong**: `A-004` (*"never defined"* across 9 lessons), `A-011` (*"nine lessons, zero definitions"*), `A-076` (*"never defined"* — and V12 `[00:23:43]` already attaches a **size**), `A-056` (*"named as a primary method and never taught"*), `A-002` (*"fourth speaker, fourth role, still no definition"*). **They were NOT run by this session and that is stated rather than implied** — they belong to a gap audit, not to a lesson pass. **V13/V14 are the last two lessons before the owner's hard stop, which makes this the last scheduled opportunity** | `V12_INTERPRETATION.md` Q6; item 128 | 🔶 **OPEN — V13/V14 audit item** |
| 130 | V12 student | **`A-039` NARROWS AGAIN AND DOES NOT CLOSE — AND THE SESSION STATES THE OPPOSITE CASE AT FULL STRENGTH AND INVITES REVERSAL.** V12 teaches the TDI in full: four components built one at a time, two setups, a three-rung scale-in ladder, an exit rule, six worked charts, a printed deck and a homework drill that uses nothing else. **`A-039`'s *"the course has never taught it"* is no longer defensible.** But plotting the indicator needs four numbers and **V12 supplies ONE** — the TSL's smoothing (`A-085`), the baseline's smoothing and the bands' basis and deviation (`A-086`, where the speaker **retracts the basis mid-sentence** and says *"I don't really know because I didn't invent it"*) are all unstated, and `[00:07:20]` *"I've altered it or tweaked it a little bit"* forecloses substituting the shipped defaults. **⚠ The session flags that it may be UNDER-crediting** and declines to close **for one reason only: `A-039` is cited as an upstream blocker by `A-031` (*"`A-039` is upstream and still blocks"*), and closing it here would silently unblock a dependent as a side effect.** **If R1 prefers the split the mechanism is clean** — close `A-039`, re-point its dependents at `A-085`/`A-086` | `A-039` V12 update; `A-031`, `A-085`, `A-086`; `V12_INTERPRETATION.md` Q1 | 🔶 **OPEN — reviewer judgement invited** |
| 131 | V12 student | **`A-066` NOT DISCHARGED, ON MEDIUM CONFIDENCE, AND THE COUNTER-ARGUMENT IS GIVEN.** V12 supplies **the corpus's first stop distance stated WITH its anchor** — `Stop Loss 23 Pips above the HOD`, **printed** (`29:11`) **and spoken** (`[00:30:33]`) — which is exactly the placement rule `A-066` records as missing. **Three reasons it is still not discharged**, the third being the one weighed most heavily: (i) **`HOD` is `A-056`'s undefined object** — a placement rule anchored to an undefined anchor is not a placement rule; (ii) a **second, incompatible** size sits one sentence away (`[00:30:37]` *"seven to ten pips above the second leg"*); (iii) ⭐ **asked directly for a stop 18 minutes later, the lesson DECLINES to restate it** — `[00:48:24]` *"what size stop loss, Aaron? **You tell me**… some are saying 10, 23, 25 — take a guess, figure it out… **seven, ten sounds great**"*. **A reviewer may reasonably discharge it on the printed slide**, and doing so turns partly on the printed-vs-spoken precedence question **V10 carry-forward (f) still has open** | `A-066`, `A-056`; `V12_INTERPRETATION.md` Q4; `V12_HOMEWORK.md` §2b | 🔶 **OPEN — reviewer judgement invited** |
| 132 | V12 student | **NOTE — `C-017` / item 106's printed-vs-spoken question gets THREE more instances and a THIRD POLARITY, with a narrow rule proposed.** V11 supplied two instances pointing opposite ways. **V12 supplies:** (i) `[00:09:51]` the speaker **reads Dean Malone's definition off the slide and repudiates two-thirds of it** — *"momentum we know is bullshit"* — same shape as V11's `POSITIVE TREND` case, **speech overrides print with a reason given**; (ii) ⚠️ **a NEW polarity — ABANDONMENT**: the slide prints `Stop Loss 23 Pips` and the speech, asked, declines to restate it (item 131); (iii) `[00:43:18]` the spoken assignment is a **strict superset** of the printed one, same shape as `A-081`. ⭐ **The recurring fact across all six instances is that the decks are borrowed or old and the speaker talks over them** — `[00:08:32]` *"they're kind enough to let me use the slides"*; V11's *"I'm not even sure these slides came from that guy"*. **A blanket *print beats speech* rule would make doctrine of decks the instructor rejects on the record; a blanket *speech beats print* rule mistakes looseness for disagreement.** **Proposed to the owner, NOT adopted and no record's status turns on it:** *both are Tier 1; where they conflict, **the medium in which the speaker gives a reason wins**; where neither gives a reason, the record carries both and codes neither* — which resolves (i) and (ii) in **opposite** directions, the property a blanket rule lacks | `C-017`; item 106; V10 carry-forward (f); `V12_INTERPRETATION.md` Q7 | ℹ️ **NOTE — supports the owner ruling requested at V10 carry-forward (f)** |
| 133 | V12 student | **NOTE — `Q-013`: `VISUAL_INDEX.md` IS NOW SHOWN BY EXACT `diff` TO BE ONE FILE ACROSS **TEN** LESSONS, AND THE FABRICATION HAS TAKEN ITS MOST DANGEROUS FORM YET.** `Q-011`/`Q-012` upgraded the one-generator claim for `RULES.md` from a normalised hash to an exact `diff`; **V12 does the same for `VISUAL_INDEX.md`, which had never had it.** V11's and V12's differ by **four lines — the filename header and three `VIDEO_NN` ids — and ZERO content lines**, across two halves of one session sharing no material; normalising ids, **ten of 21 lessons share one identical body** (03,04,09,10,11,12,13,14,15,21) and five more share a second. **Fourth instance of the sixth failure mode and the SECOND CONSECUTIVE title card**, indexed with the identical sentence used on V11. ⭐ **And §4 records the new hazard: V12 is the FIRST lesson on which the generator's text is ABOUT THE RIGHT SUBJECT** — its *"TDI Shark Fin setup with green line hooking inside volatility bands"* is a fair description of this lesson — **and those exact sentences are attached to ten other lessons, including ones where `TDI` occurs zero times.** A sentence printed identically on ten lessons is not an observation about any of them. **This is dangerous specifically to a reviewer sampling quickly**, and the defence is `Q-007`'s blanket rule and the `diff`, which do not care whether the text happens to be true. Also: the `EMAs` nickname line is a **constant across all 21 files**, wrong on **four of five rows** against `D-043`, and invents **`Raspberry`** for the 800 — **zero occurrences in the corpus or either external tier** | `Q-013` §1, §2, §3, §4; `Q-011`, `Q-012`, `Q-009` | ℹ️ **NOTE — pattern confirmation and a NEW failure mode** |
| 134 | V12 student | **NOTE — a self-reported error, and a MEASUREMENT trap that would have FLATTERED a fabricated file.** `Q-013` §0 records two artifacts caught in this session's own first pass, inherited from `Q-012`'s method note: a naive `grep -ci "EMA"` returns **7** against **2** word-boundary; and **a naive `grep -ci "morning star"` returns 1**, which **is a substring of `[00:30:20]` *"10 in the **morning star**ted the US session"***. **The true count is 0.** Had it not been checked it would have appeared to **corroborate** the quarantined `NOTES.md`'s fabricated *"Evening/Morning Stars"* topic line — **the closest this register has come to a false positive running in a fabrication's favour.** Same class as `Q-012`'s `9:30`-matches-a-timestamp trap and item 103's method note, in a new costume. Recorded per item 108's precedent that a session's own errors belong in the record | `Q-013` §0, §2; item 103; `Q-012` measurement note | ℹ️ **NOTE — method, self-reported** |
| 135 | V12 student | **NOTE — two disclosures a reviewer should adjudicate rather than discover.** **(1) `EXTERNAL_VOCABULARY_REFERENCE.md` was edited on the task branch.** It is named in **NEITHER** of `D-038a`'s two lists. Classified here as an **EVIDENCE ledger** by `D-038a`'s own test (*does an unmerged edit change what another session is permitted to do?* — it records what a session found), which is **also what `SOURCING_HIERARCHY.md` §3.1 steps 3–4 require of the reconciling session, and that requirement is what forced the choice.** **R1 may overrule.** **(2) A mis-cited decision was corrected in place rather than quietly:** `V12_HOMEWORK.md`'s first draft blocked the demo-trade drill on **`D-006`**, which in fact defers *automated backtesting and Pine Script*, not demo orders. **The correction REDUCED the blocker count from two to one**, and the file says so — *"a deferral propped up by a mis-cited decision is worse than a deferral with one honest reason"* | `D-038a`; `SOURCING_HIERARCHY.md` §3.1; `D-006`; `V12_HOMEWORK.md` § dispositions | ℹ️ **NOTE — disclosures, reviewer adjudication invited** |
| 136 | V12 student | ⭐ **`08_CONCEPT_LIBRARY` — V12 IS THE FIRST LESSON THAT GENUINELY TESTS ITS 0-CONCEPT POLICY, AND THE SESSION DECLINES TO RESOLVE THE TENSION ALONE.** The index holds **0 concepts** on a reasoned, **R1-upheld** rule: promote a term only when the course defines it, never while it is an open `A-xxx`, because that *"would launder an open ambiguity into a citable definition"*. **Every prior lesson made that easy — nothing was defined.** V12 breaks the pattern: **`shark fin` and `blood in the water` are now `RESOLVED BY COURSE`, printed and spoken**, and `mayonnaise = 200` is Tier 1 — **exactly the terms the index was written to wait for.** ⚠ **No entry was created**, because all three are closed **as to meaning** and **not computable** (`A-086`), so an entry could be mistaken for a codable rule — **a different laundering than the index's rules name, in the opposite direction.** The likely right answer — an entry carrying the closure **and** the blocker in one breath — **is a change to the index's own rules, which a task branch should not make.** Put to R1 and the owner | `08_CONCEPT_LIBRARY/CONCEPT_INDEX.md`; `A-031`, `A-032`, `A-086`; `V12_MASTERY_REPORT.md` §2, carry-forward (j) | 🔶 **OPEN — owner/reviewer decision invited** |
| 137 | **V12 R1** | **`M1` — `04_SCREENSHOTS/V12/INDEX.md` §1's categorical *"Every legend legible in any V12 frame is transcribed below"* is FALSE.** Frame `00-34-26` carries an **untranscribed sixth on-screen text block**: a multi-timeframe indicator dashboard with rows **`MACD / STR / EMA`** over columns **`1 · 5 · 15 · 30 · H1 · H4 · D · W · MN`**, plus `108.093`, `Spread 33`, `Pips to Open`, `Hi to Low 315`, `Daily Av`. The reviewer cropped and enlarged the region to confirm legibility. **⭐ `A-080` IS UNAFFECTED AND ITS NEGATIVE IS STRENGTHENED**, for three reasons each checked: (i) the columns are **TIMEFRAMES, not lookback periods** — the `5` and `15` are minutes, and the `EMA` row carries **no number at all**; (ii) the chart is a **STUDENT's**, given to the instructor — `[00:34:19]` *"this came to me from my good friend… who graduated Harvard business school"* — which is the exact category V11 R1 item 109 warned about; (iii) the dashboard appears on **NO other frame** — the reviewer cropped the same region from `00-37-21`, `00-40-36`, `00-22-11` and `00-20-41` and it is absent from all four. **The defect is that this is the same class of error V11 R1 item 109 charged, inside the very section written to discharge it** — V11 recorded a pane count and missed a legend; V12 recorded the legends and missed a dashboard. **REQUIRED:** add the dashboard as a sixth `INDEX.md` §1 row, transcribed verbatim, `Carries a period?` = **NO — columns are TIMEFRAMES**, noting the student-chart provenance; and **rescope** the categorical sentence to *"every legend and on-screen readout block identified in the 28 curated frames"*. Superseded text retained (`REMEDIATION_PROTOCOL.md` §2). **`A-080`'s status does not change** | `04_SCREENSHOTS/V12/INDEX.md` §1; `V12_00-34-26_…png`; `V12_TRANSCRIPT.md` `[00:34:19]`; item 109 | 🔶 **OPEN — MINOR** |
| 138 | **V12 R1** | **`M2` — `Q-013` §4's *"THE FIRST TIME THE GENERATOR'S TEXT IS ABOUT THE RIGHT SUBJECT"* is FALSE, and the register itself records the other two instances.** §4 asserts *"on eleven previous lessons the fabricated files were wrong in an obvious way."* **`Q-003` Finding 2 is headed *"the new hazard: this time some of the fabricated vocabulary is real"*** and names **the same `NOTES.md` sentence** (*"Green Price Line crossing Red Signal Line after breaking outside Blue Volatility Bands (Shark Fin)"*); **`Q-004` Finding 3 is headed *"the `Q-003` hazard recurs and is worse here."*** Reviewer's own word-boundary census over the transcript bodies: **V03 — `TDI` 12, `shark fin` 3, `volatility band` 2, `blood in the water` 2; V04 — `TDI` 11, `shark fin` 5, `blood in the water` 2**, against **V12 — `TDI` 46, `shark fin` 20, `blood in the water` 14**. **And V03 and V04 share BOTH the ten-lesson `VISUAL_INDEX.md` body AND the `NOTES.md` TDI-sentence variant with V12** — the reviewer verified the `NOTES.md` line has three variants across the 21 files and that V01–V04, V09–V15 and V21 all carry V12's exact wording. **⭐ THE CORRECTION STRENGTHENS THE ENTRY:** V12 is the **third and most complete** instance of a documented, escalating hazard, not a novel one — and *a recurring hazard is a far better argument for §4's own conclusion* (*"the defence is not vigilance — it is `Q-007`'s blanket rule and the exact-`diff` test"*) than novelty was. **Disposition UNCHANGED — all three files stay quarantined and no V12 artifact draws on them, verified independently.** **REQUIRED:** rewrite §4's opening to name `Q-003` and `Q-004` as first and second, restate V12 as third and most complete, and carry the measured counts and the shared-body/shared-sentence fact. Superseded text retained | `Q-013` §4; `Q-003` Finding 2; `Q-004` Finding 3; reviewer TDI-vocabulary census | 🔶 **OPEN — MINOR** |
| 139 | **V12 R1** | **NOTE — ⭐ `PT-040` WAS REPRODUCED EXACTLY BY INDEPENDENT RE-DERIVATION, AND ONE UNDER-SPECIFICATION WAS FOUND IN `N3`.** The reviewer wrote `reviewer_pt040.py` from `PT-040` §§3–5 and `COMMON_PROTOCOL.md` §§1–3 alone, parsing the **1,297,781 raw M1 bars** directly (not the `_cache`, not the pre-aggregated ARMA/ARMB CSVs), with its own M15 aggregation, its own Wilder RSI, its own US-DST rule and its own observations — **sharing no line with `run_pt040.py` or `mmm_lib`, neither of which was opened until after the run completed.** **EVERY WILDER CELL MATCHES TO THE PRINTED DECIMAL** across `W-A`/A, `W-A`/B and `W-B`/A: `O1` ×20, `O2` ×15, `O3` ×20, `O4` ×16, bars **24,755 / 24,730 / discarded 25**, `W-B` **49,421 / 49,396**, spans, **`M = 10.4812 pp` at `k=5,t=50`**, **`k=2` max `5.1638 pp`**, arm gap **0.0000 pp**, `N2` **10.6608 pp**. All four pre-registered secondary checks re-derived and all four hold. **The `N3` simple-average cell differs by ≤ 0.02 pp** (`k=5,t=50`: 12.15 vs reviewer's 12.14). **Cause identified exactly:** `PT-040` §3.1 names *"the simple-average variant"* without giving its formula; the runner uses a **prefix-sum** rolling mean, the reviewer a **direct windowed sum**. Max divergence **5.16 × 10⁻¹¹** — but **48 bars in `W-A` sit at EXACTLY `RSI = 50.0`** (up-sum equals down-sum exactly) and `O2`'s `≥` is **tie-sensitive**, so float noise flips 15 of them. **NO VERDICT MOVES — both are `MATERIAL`. NOT CHARGED**, because `N3` is a reported line with no decision attached. **FORWARD REQUIREMENT: the next `PT` carrying a formula-robustness line should state the summation method and the tie convention at the threshold** | `PT-040` §3.1, §4 `N3`; `pt040_output.txt` N3 cell; reviewer re-derivation | ℹ️ **NOTE — reproduced exactly; forward requirement for the next `PT`** |
| 140 | **V12 R1** | **NOTE — the *"all 672 sweep frames"* scan is NOT verifiable by repository inspection**, because the sweep frames are not committed. Same class of limit V11 R1 recorded at its `N6` for push timing. **What IS verifiable was checked and holds:** the reviewer opened **8 of the 28 committed frames** and found no properties dialog and no Navigator panel; the six timecode-sync rows in `INDEX.md` §0 spot-check correct; the `26:11` print-vs-audio cross-check lands on the same second in both media; and **the load-bearing observation — that MT4 prints an indicator's inputs in parentheses after its name, and here there are none — was confirmed by reading the TDI sub-window legend off the pixels on two separate frames** (`00-26-11` and `00-34-26`), both showing `Traders Dynamic Index Visual` followed by six **unparenthesised** output values. **NOT CHARGED** — the claim is recorded so its evidential status is explicit, and `A-080` closes on the audio in any case | `04_SCREENSHOTS/V12/INDEX.md` §0, §1; `A-080` V12 update; V11 R1 item 119 | ℹ️ **NOTE — self-report accepted, one half unverifiable** |
| 141 | **V12 R1** | **NOTE — a sentence supporting `A-080` that the record does not cite, and it forecloses the last alternative reading.** `[00:08:22]`, from the reviewer's own independent ASR pass: *"**You want to use it at 14, knock yourself out.**"* The instructor contrasts his preset against the RSI's own default **as a choice he is consciously making and consciously offering to the group** — which rules out both remaining alternative readings of `A-080`'s evidence: that `21` is a misspeak, and that he is reporting some third party's setting rather than his own. **Worth adding to `A-080`'s evidence table**, where it costs nothing and closes the last door. Recorded because independence means adding evidence, not only checking it | `A-080` V12 update evidence table; reviewer ASR `00:07:05`–`00:08:40` | ℹ️ **NOTE — added evidence, favourable** |
| 142 | **V12 R1** | **NOTE — `PT-040` bundles the runner, the output, the scoring report and the `A-084` record update into ONE commit (`69539c5`), where `PT-039` used FOUR.** **No rule requires the split**, and the load-bearing ordering is intact and was verified rather than accepted: `git cat-file -e 83110f1:…/run_pt040.py` returns **ABSENT**, as does the output, so the pre-registration provably precedes the runner and **`D-026` is satisfied by ordering, not by assertion** — `BT_V12_0001` §1a item 1 is exactly right. **But the repository can no longer demonstrate *"output committed before the scoring"***, which V11's four-commit history could and which V11 R1 checked as its procedural checks 2–4. **FORWARD REQUIREMENT: restore `PT-039`'s commit separation in the next `PT`** — prereg → runner → output → scoring, each in its own commit | commits `83110f1`, `69539c5`; `BT_V12_0001` §1a; V11 R1 procedural checks 1–5 | ℹ️ **NOTE — process regression against V11's precedent, no rule breached** |
| 143 | **V12 R1** | **NOTE — ⚖️ ITEM 124 ADJUDICATED: THE COLOUR-AXIS RESTRAINT IS CORRECT, AND THIS REVIEWER WOULD HAVE CHARGED THE UPGRADE HAD IT BEEN TAKEN.** Item 124 asked whether refusing to move `D-043`'s mayo **colour** row was right or over-cautious. The reviewer opened both frames and confirms the premise is genuinely suggestive — on `31:31` and `26:11` price is held at a **white** line under captions naming the 200 and the Mayo. **It is still inadmissible, for a mechanical reason rather than a matter of taste: `COMMON_PROTOCOL.md` §2 forbids measuring anything off a rendering** (*"a chart may be looked at; nothing may be measured off one"*), and a *convenient* confirmation is the kind most likely to be adopted without scrutiny. **⭐ AND THE REVIEWER FOUND A FURTHER STRAND AND REFUSED IT TOO:** on both frames the four price-pane curves are ordered by responsiveness — **yellow hugs price most closely, then red, then cyan, then white as slowest and flattest** — which is consistent with `D-043` on **all four** colour rows and appeals to a mathematical property rather than to a caption. **It still closes nothing and must not be promoted.** `D-043` §1's mayo colour row stays `OWNER-ATTESTED` + `[TOOLING]`. **Item 124 may be CLOSED as adjudicated** | item 124; `D-043` §1; `COMMON_PROTOCOL.md` §2; frames `31:31`, `26:11` | ✅ **ADJUDICATED — restraint UPHELD; item 124 closable** |
| 144 | **V12 R1** | **NOTE — ⚖️ ITEMS 130 AND 135 ADJUDICATED.** **(1) Item 130 — `A-039` does NOT close. The non-closure is UPHELD, on a ground stronger than the one given.** The session named **one** dependent; the reviewer measured the surface: **`A-039` is referenced 287 times across 65 files**, including nine `PT-xxx` pre-registrations, `BACKTEST_EVIDENCE_STANDARD.md`, four mastery reports and five prior reviews. **But the decisive reason is `D-003`, not arithmetic:** `A-084`, `A-085` and `A-086` were opened by the **same session**, so closing `A-039` and re-pointing 287 references at three records that session had just written would put the closure, the replacements and the completeness of the re-pointing all in one unchecked pair of hands. **Deferring to a reviewer is the separation of duties working, not caution.** **CONDITION FOR CLOSING LATER:** a dedicated pass that (a) enumerates all 287 references, (b) re-points or marks each historical, and (c) is reviewed independently of the session that opened the replacements. **It is NOT V13's work and must not be bundled into a lesson pass.** **(2) Item 135 — `EXTERNAL_VOCABULARY_REFERENCE.md` is an EVIDENCE ledger and the session classified it correctly.** Under `D-038a`'s own test, the permission to close a record on Tier 2 comes from `D-039` and `SOURCING_HIERARCHY.md` — **both POLICY ledgers, both on integration** — while this file records what the external documents *say*, not what may be done with them. **FORWARD REQUIREMENT: name the file explicitly in `D-038a`'s table on the integration branch**, since the classification has now been re-derived twice. **Items 130 and 135 may be CLOSED as adjudicated** | items 130, 135; `A-039` V12 update; `A-031` status block; `D-038a` test; `D-003` | ✅ **ADJUDICATED — `A-039` stays NARROWED; `EXTERNAL_VOCABULARY_REFERENCE.md` = EVIDENCE ledger** |

---


> ### ⚠ RENUMBERING DISCLOSURE — V10's open items were 81–85 on `video/v10`
>
> **`video/v10` branched from `5db04d8` and allocated open items 81, 82, 83, 84, 85. The
> integration branch concurrently allocated 81, 82 and 83 to V09 R2** (`7b42156`, merged at
> `310362c`). Merging both would have left the register with three duplicate identifiers.
>
> **V10's five items are renumbered 86–90 by the V10 R1 reviewer, at merge-back, as the
> single-threaded integrator** (`D-038` merge-back is its own act). **V09 R2's 81–83 keep their
> numbers**, because they were allocated on the integration branch and are already cited in
> merged commits. The old→new map is recorded here rather than applied silently:
>
> | On `video/v10` | Now | Subject |
> |---|---|---|
> | 81 | **86** | `PT-037` path-length reading, recommended not owed |
> | 82 | **87** | `SWF_CAPTURE_RECIPE.md` §10 frame-rate defect |
> | 83 | **88** | `C-017`, printed-vs-spoken precedence |
> | 84 | **89** | `A-077`, the lock |
> | 85 | **90** | `PT-036`'s censoring design-out |
>
> **Two committed V10 artifacts still cite the old numbers** — `04_SCREENSHOTS/V10/INDEX.md`
> § ESCALATION and `07_MASTERY_REPORTS/V10_MASTERY_REPORT.md` escalation 2, both citing
> *"open item 82"* for the recipe defect, which is now **87**. Correcting them is carried as
> item **91**'s student-owed half. The cause, and the `D-038a` gap behind it, is item **91**.
>
> ---
>
> #### ⚠ RENUMBERING VERIFIED COMPLETE — AND THE PARAGRAPH ABOVE IS FACTUALLY WRONG. 2026-08-13
>
> **Superseded text, retained per `REMEDIATION_PROTOCOL.md` §2** — the paragraph immediately above
> is left standing and is corrected here rather than edited away.
>
> **Neither artifact cited *"open item 82"*, or any item number at all.** Both referred to the
> recipe defect **by description**. Verified by grepping `82` in each file: the only hits are the
> source `.swf`'s SHA-256 and an `R = 82.0` chart label in the frame table. **There were no stale
> pointers, so the renumbering orphaned nothing.**
>
> **The renumbering itself is COMPLETE and was verified by sweep, not by assertion.** `grep` for
> `item 8[1-5]` across every `.md` in the repository returns **no V10-scoped hit** — every
> surviving 81/82/83 belongs to V09 R2, which correctly keeps those numbers — and 86, 87, 88, 89
> and 90 each appear exactly once in the open-items table, with the subjects mapped above.
>
> **What was owed turned out to be an addition rather than a correction, and it is done:** both
> artifacts now carry a pointer naming open item **87** as ✅ CLOSED, recording that it was `82`
> on `video/v10` and pointing at item **91** for the collision and the `D-038a` gap. **Nothing in
> either artifact is superseded.**
>
> **⚠ Verified by the same session that made these edits, at owner direction — `D-003` is NOT
> satisfied.** See item 92's status cell for the full disclosure.

## HUMAN REVIEW QUEUE

| # | Lesson | Issue | Why a human is needed | Status |
|---|---|---|---|---|
| _(none)_ | | | | |

---

## CUMULATIVE REVIEWS

| Checkpoint | Trigger | File | Status |
|---|---|---|---|
| 25% | TBD at ingestion | `CUMULATIVE_25.md` | Not started |
| 50% | TBD at ingestion | `CUMULATIVE_50.md` | Not started |
| 75% | TBD at ingestion | `CUMULATIVE_75.md` | Not started |
| Final | All lessons passed | `FINAL_COURSE_REVIEW.md` | Not started |

---

## REVIEW FILE LOCATIONS

```text
18_REVIEW/VXX/VXX_REVIEW_R1.md
18_REVIEW/VXX/VXX_REVIEW_R2.md
```

Never overwrite a round (`SETUP_ISSUES.md` I-002).
