# REMEDIATION PROTOCOL

What happens after a review decision. Defines the progression loop, and the
non-negotiable rule that invalid work is **redone, not reworded**.

Source: `MMM_INDEPENDENT_REVIEWER_TEACHER_AGENT.md` §§13, 27, 29, 30, 31, 36.

---

## 1. THE LOOP

```text
STUDENT COMPLETE
      ↓
STUDENT SELF-REVIEW              (07_MASTERY_REPORTS/VXX_MASTERY_REPORT.md)
      ↓
REVIEWER AUDIT                   (independent session, 18_REVIEW/VXX/VXX_REVIEW_R<n>.md)
      ↓
   DECISION
      │
      ├── PASS ────────► ADVANCE TO NEXT LESSON
      │
      ├── REVISE ──────► FIX SPECIFIC ISSUES
      │                  → RETEST AFFECTED WORK
      │                  → RESUBMIT
      │                  → REVIEW AGAIN  (R2, R3, …)
      │
      └── BLOCKED ─────► RE-STUDY FOUNDATIONAL SOURCE
                         → REDO AFFECTED HOMEWORK / CHART WORK / BACKTEST
                         → SELF-REVIEW
                         → REVIEW AGAIN  (R2, R3, …)
```

There is no path from `REVISE` or `BLOCKED` to the next lesson that does not pass
back through review. **Reviewer `PASS` is the only gate.**

---

## 2. THE CENTRAL RULE — REDO, DO NOT REWORD

> **Inaccurate work must not be cosmetically edited if the underlying test was
> invalid.**

Editing the write-up of a broken test produces a document that *looks* correct
while the evidence beneath it remains worthless. That is precisely the failure this
project's two-agent design exists to prevent.

Concretely:

| If the reviewer found… | You must… | You must NOT… |
|---|---|---|
| Hindsight / lookahead bias in a backtest sample | Repeat the affected observations from scratch, with future candles hidden at the decision point, and assign **new** test IDs | Rewrite the notes to sound like the future wasn't used |
| A classification that depended on seeing the later reversal | Re-classify at the decision candle, with no knowledge of the outcome | Adjust the wording of the justification |
| A rule with no provenance | Locate the actual timestamp/screenshot, or relabel the rule `INFERRED` and move it out of the canonical set | Add a plausible-looking citation |
| Homework answered after seeing the solution | Preserve that fact, record it as `SUCCESS AFTER SOURCE REVIEW`, and attempt a comparable unseen task | Relabel it `FIRST-PASS SUCCESS` |
| Cherry-picked sample (losers dropped) | Restore or re-run the full sequential sample, including the losers | Add a sentence acknowledging the losers exist |
| Missing negative examples | Find and document genuine lookalikes that fail | Reclassify an existing positive example as "borderline" |
| A generalization from three instructor examples | Relabel as `INFERRED`, note the evidence limit | Leave it as `EXPLICIT` with softer wording |

**Old, invalid observations are not deleted.** They are marked
`SUPERSEDED — INVALID PROCEDURE (see R<n> finding)` and retained, with the
replacement observation cross-referenced. The research corpus keeps its failures;
deleting them would destroy the audit trail (see §6).

---

## 3. HANDLING `REVISE`

1. **Read the review file in full**, not just the executive block. Required
   corrections are enumerated and specific.
2. **Scope the work.** Fix only what the reviewer identified plus anything that
   directly depends on it. Do not reprocess the entire lesson — the governing files
   explicitly warn against wasteful complete reprocessing.
3. **Determine for each item whether it is a documentation fix or an evidence
   fix.**
   - Documentation fix → correct the file (e.g. relabel `EXPLICIT` → `INFERRED`,
     add a missing timestamp).
   - Evidence fix → **redo the underlying work** per §2.
4. **Retest affected work.** If a rule definition changed, every chart
   classification and backtest observation that used the old definition is now
   suspect and must be re-examined.
5. **Update the mastery report** — do not overwrite it. Append a
   `## Revision R<n>` section describing what changed and why.
6. **Append to `LOG.md`** with a Remediation entry (§5).
7. **Update `COURSE_PROGRESS.md`** — status returns to `IN REMEDIATION`.
8. **Commit** with a message such as `fix: address V04 review R1 required corrections`.
9. **Request a fresh reviewer session.** The reviewer writes `VXX_REVIEW_R2.md`;
   `R1` is never edited.

---

## 4. HANDLING `BLOCKED`

`BLOCKED` means the foundation is wrong, not that details need polishing. Do not
attempt a quick patch.

1. **Identify the foundational defect** from the review file: wrong understanding,
   unusable source, materially biased testing, fabricated evidence, invalidating
   contradiction, unreliable pattern recognition, or dependence on an unmastered
   earlier lesson.
2. **Re-study the foundational source.** Rewatch the specific timestamp ranges the
   reviewer identified. If the review cites an earlier lesson, that earlier lesson
   is the real work item — a lesson cannot be built on an unmastered dependency.
3. **Redo affected work completely** — homework, chart classifications, and
   backtest samples produced under the wrong understanding are void. Assign new
   IDs; mark the old ones `SUPERSEDED`.
4. **Rebuild the affected concept-library entries** rather than editing them into
   shape.
5. **Re-run the full self-review** against `MASTERY_STANDARD.md`. A blocked lesson
   returning for review must be re-assessed on all ten dimensions, not just the
   broken one.
6. **Append to `LOG.md`**, update `COURSE_PROGRESS.md` (`BLOCKED` →
   `IN REMEDIATION`), commit, and request a fresh reviewer session.

### Special case: fabricated or invented evidence

If the reviewer found fabricated evidence, the remediation is not partial. Every
artifact from that session is suspect. Quarantine the lesson's outputs, mark them
`SUSPECT — FABRICATION FINDING R<n>`, and rebuild from source. Record the incident
in `LOG.md` and `DECISIONS.md`. This is a research-integrity event, and the record
of it stays permanently.

---

## 5. LOG ENTRY FOR REMEDIATION

```text
## YYYY-MM-DD — Session N — Remediation of VXX (Review R<n>)

### Objective
Address the required corrections from 18_REVIEW/VXX/VXX_REVIEW_R<n>.md.

### Findings Addressed
- [E08 / CRITICAL] Hindsight in BT_V04_0011..0015 → resample, new IDs
  BT_V04_0031..0035; originals marked SUPERSEDED.
- [E11 / MAJOR] "Third push must be larger" had no provenance → relabelled
  INFERRED, moved out of the canonical set, logged as A-0XX.

### Work Redone (not edited)
...

### Work Corrected (documentation only)
...

### Retesting
What was re-tested and why.

### Remaining Open Items
...

### Files Created/Updated
...

### Git
...

### Next Action
Request reviewer session for VXX R<n+1>.
```

---

## 6. WHAT MUST NEVER HAPPEN DURING REMEDIATION

- Deleting a losing backtest observation.
- Deleting or editing a prior review file.
- Rewriting a historical `LOG.md` entry.
- Renumbering test IDs so a failed sample disappears.
- Changing a rule definition so that existing (failed) classifications become
  correct.
- Narrowing the sample window so an inconvenient period is excluded.
- Adjusting labelling rules until the results look better.
- Rewriting Git history to make the audit trail look cleaner.

Every one of these converts a research repository into a marketing document.

---

## 7. REPEATED REVISIONS

If a lesson reaches `R3` without a `PASS`, stop iterating and escalate:

1. Record the pattern in `LOG.md` and in `18_REVIEW/REVIEW_INDEX.md` under
   recurring errors.
2. Check whether the true problem is an **earlier** lesson. Repeated failure on
   lesson N is often an unmastered dependency at lesson N−1 or N−2.
3. Consider whether the lesson contains genuinely subjective material — if two
   plausible readings materially change trading logic, the correct outcome may be
   `HUMAN REVIEW REQUIRED`, not another student attempt.
4. Do not lower the standard to close out the lesson.

---

## 8. AFTER `PASS`

1. Reviewer updates `18_REVIEW/REVIEW_INDEX.md` with the decision and issue counts.
2. Reviewer appends the decision to `LOG.md`.
3. `COURSE_PROGRESS.md` final status becomes `COMPLETE`.
4. Any open research items noted in the review (permitted with a non-foundational
   `PASS`) are carried into `10_AMBIGUITIES/` or `11_CONTRADICTIONS/` so they are
   not forgotten.
5. Only then may a Student session open the next video.
