# SESSION CLOSE PROTOCOL

Run before ending **every** meaningful session.

Source: `MMM_MASTER_STUDENT_RESEARCH_AGENT.md` §34;
`MMM_INDEPENDENT_REVIEWER_TEACHER_AGENT.md` §35.

> **The repository must always be resumable by another competent agent.**
> If your session ended right now, could a stranger pick it up from the repository
> alone? That is the standard.

---

## 1. FINISH OR MARK PARTIAL WORK

Every artifact you touched is either complete or **explicitly marked** partial:

```text
> **STATUS: PARTIAL** — transcript covers 00:00:00–00:31:45.
> Remaining: 00:31:45 → end. Resume at STUDY_PROTOCOL.md Step 2.
```

An unmarked partial artifact reads as finished to the next session and to the
reviewer. That is how false completeness enters the corpus.

---

## 2. UPDATE PROJECT STATE

- [ ] `00_SYSTEM/COURSE_PROGRESS.md` — artifact columns, mastery/reviewer columns,
      final status.
- [ ] `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md` — new subjective language found.
- [ ] `11_CONTRADICTIONS/CONTRADICTIONS.md` — new conflicts found.
- [ ] `08_CONCEPT_LIBRARY/CONCEPT_INDEX.md` — new or changed concept entries.
- [ ] `00_SYSTEM/SETUP_ISSUES.md` — new infrastructure issues, or status changes.
- [ ] `18_REVIEW/REVIEW_INDEX.md` — reviewer sessions only.
- [ ] `README.md` — only if phase, architecture, methodology, or scope changed.
- [ ] `CHANGELOG.md` — only for project-level structural changes.

---

## 3. APPEND TO `LOG.md`

One entry, appended at the end. **Never rewrite a previous entry.**

Student entries use the §6 format: Objective, Work Completed, Key Findings, Manual
Backtesting, Ambiguities, Contradictions, Decisions, Files Created/Updated, Git,
Next Action.

Reviewer entries use the reviewer §6 format: Lesson, Review Objective, Source
Evidence Reviewed, Student Artifacts Reviewed, Findings, Required Corrections,
Decision, Git, Next Review Trigger — and are labelled `Reviewer Session`.

Write honestly. If a test was invalid, if work was skipped, if something remains
confused — the log says so. A log that only records successes is not an audit
trail.

---

## 4. REVIEW YOUR CHANGES

```bash
git status
git diff --stat
git diff
```

Confirm:

- [ ] Only intended files changed.
- [ ] No temporary or scratch files.
- [ ] No credentials, tokens, API keys, cookies, or broker configuration.
- [ ] **No source video files** (check `git status` for large binaries).
- [ ] No accidentally huge files (`git diff --stat` will show them).
- [ ] Artifact names follow `FILE_NAMING_STANDARD.md`.
- [ ] No prior review file, log entry, or losing observation was deleted or
      rewritten.

---

## 5. RUN VALIDATION

```bash
python3 scripts/validate_project.py
```

Fix structural failures before committing. Warnings may be acceptable — note them
in `LOG.md` if you are leaving them open.

---

## 6. COMMIT

Focused commits at logical checkpoints. Avoid one giant commit of unrelated work.

```bash
git add <intentional files only>
git commit -m "<clear message>"
```

### Commit during the session, not only at the end

**Do not save all committing for session close** (`DECISIONS.md` D-015). Commit and
push at checkpoints as you work — roughly every 5–10 artifacts, or at any natural
boundary:

```text
transcript complete                     → commit
source notes + interpretation complete  → commit
screenshots captured and indexed        → commit
homework complete                       → commit
first batch of backtest observations    → commit
mastery report written                  → commit
```

Three reasons this matters here: a session can be interrupted at any point and
uncommitted work is simply lost; the commit sequence is itself audit-trail evidence
of the order in which understanding was built; and small commits can actually be
reviewed.

A checkpoint commit does **not** require the session to be finished. It does
require the repository to be left coherent — nothing half-written that reads as
complete, and any partial artifact explicitly marked `STATUS: PARTIAL` (§1).

`LOG.md` is still appended **once**, at session close. Its `### Git` section lists
every commit from the session, not just the last one.

Message conventions:

```text
chore:  infrastructure, tooling, structure
docs:   protocols, README, standards, mastery certification
study:  transcripts, notes, lesson artifacts
charts: screenshots and chart examples
test:   manual backtesting
review: reviewer decisions and audits
fix:    corrections and remediation
spec:   master/machine specification work (Phase 3+)
```

Examples:

```text
study: complete video 01 transcript and notes
test: complete video 01 manual backtest
docs: certify video 01 mastery
review: pass video 01 mastery audit
review: block video 04 due to lookahead bias
fix: address V04 review R1 required corrections
```

Never use destructive Git commands, and never rewrite history to make the audit
trail look cleaner. The history is evidence.

---

## 7. PUSH

```bash
git push -u origin <branch>
```

On network failure, retry with backoff (2s, 4s, 8s, 16s). If the push still fails,
**record why in `LOG.md`** — the next session must know that local work is ahead of
the remote.

---

## 8. RECORD THE COMMIT

Add the commit message (and hash if available) to the `### Git` section of the
`LOG.md` entry you just wrote.

---

## 9. WRITE A PRECISE NEXT ACTION

The last line of your log entry is the handoff. It must be executable by someone
with no context.

Good:

```text
Next Action: Reviewer session for V03. Audit against 18_REVIEW/V03/ — start with
source evidence at V03 @ 12:40–19:05 (the confirmation sequence), then compare
against 03_LESSON_NOTES/V03_INTERPRETATION.md rules R3–R7.
```

Bad:

```text
Next Action: Continue studying.
```

---

## 10. FINAL SELF-CHECK

- [ ] Would a stranger know exactly what to do next?
- [ ] Is every claim in my artifacts traceable to evidence I actually saw?
- [ ] Did I invent anything to fill a gap? (If yes — remove it and mark the gap.)
- [ ] Did I preserve every failure, loser, and mistake?
- [ ] Did I stop where the protocol says to stop, rather than working ahead?
