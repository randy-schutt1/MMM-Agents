# MMM-MASTERY — Market Maker Method Research & Automation Project

**CURRENT STATUS: INFRASTRUCTURE READY / SOURCE VIDEOS NOT YET AVAILABLE**

No bootcamp lesson has been processed. No transcript, note, chart example, homework
answer, backtest, concept definition, or Market Maker Method rule exists in this
repository. Everything currently present is operating-system scaffolding.

---

## 1. PURPOSE

This repository is a long-term research program to study, faithfully reconstruct,
validate, formalize, and eventually automate the **Market Maker Method Bootcamp by
Steve Mauro**.

The governing documents for the project are:

| File | Role |
|---|---|
| `MMM_MASTER_STUDENT_RESEARCH_AGENT.md` | Defines the Student / Research Agent |
| `MMM_INDEPENDENT_REVIEWER_TEACHER_AGENT.md` | Defines the Independent Reviewer / Teacher Agent |

Those two files are the **source of truth**. Every file in `00_SYSTEM/` is derived
from them. If an operating document ever disagrees with a governing file, the
governing file wins, and the disagreement is recorded in
`00_SYSTEM/SETUP_ISSUES.md`.

---

## 2. LONG-TERM OBJECTIVE

```text
Bootcamp
  → Expert Knowledge System
  → Formal Trading Specification
  → TradingView Recognition Engine
  → Strategy Backtester
  → Validated Strategy
  → Controlled Trading Robot
```

The full 13-stage roadmap (Phase 0 through Phase 12) is recorded in
`00_SYSTEM/STUDY_PROTOCOL.md`.

---

## 3. CURRENT PHASE

**PHASE 0 — ENVIRONMENT (complete)**

Repository, directory structure, protocols, templates, logging, review
infrastructure, and validation tooling are in place.

**PHASE 1 — STUDENT (blocked, waiting on source access)**

Phase 1 cannot begin until the bootcamp video files are locally accessible to the
agent session. See §11, *Current Limitation*.

---

## 4. THE TWO AGENTS

### Student / Research Agent

Studies one lesson at a time. Produces transcript, source notes, interpretation
notes, screenshots, homework, manual backtests, chart examples, concept entries,
ambiguity and contradiction records, and a self-assessed mastery report.

The Student Agent **cannot certify its own progression**.

### Independent Reviewer / Teacher Agent

Runs in a **separate session** with no memory of the student's reasoning.
Inspects source evidence *before* student conclusions, audits the lesson against
the review dimensions, and issues exactly one decision:

```text
PASS      → advance to the next lesson
REVISE    → specific correctable deficiencies; fix and resubmit
BLOCKED   → foundational problem; re-study and redo affected work
```

---

## 5. PROGRESSION GATE

```text
STUDENT COMPLETE
      ↓
STUDENT SELF-REVIEW  (mastery report: PASS / REVIEW REQUIRED / BLOCKED)
      ↓
REVIEWER AUDIT       (independent session)
      ↓
    PASS?
  ↙       ↘
NO         YES
↓           ↓
REMEDIATE   NEXT LESSON
↓
REVIEW AGAIN
```

**Reviewer `PASS` is the only gate that authorizes advancement.** A student
mastery report of `PASS` is a self-assessment and a request for review — nothing
more. Lesson N+1 must not be started until lesson N carries a reviewer `PASS` in
`18_REVIEW/REVIEW_INDEX.md`.

The full remediation loop is defined in `00_SYSTEM/REMEDIATION_PROTOCOL.md`.

---

## 6. REPOSITORY-AS-MEMORY PRINCIPLE

**Chat sessions are disposable. The repository is authoritative.**

- An agent must never rely on conversational memory when repository state provides
  stronger evidence.
- Every meaningful session appends to `LOG.md` and updates
  `00_SYSTEM/COURSE_PROGRESS.md`.
- Historical log entries and review decisions are **append-only**. Corrections are
  added as new entries; they never overwrite old ones.
- A competent new agent (or human) must be able to read the repository cold and
  resume exactly where the last session stopped.

Session boot and shutdown checklists live in `00_SYSTEM/SESSION_START.md` and
`00_SYSTEM/SESSION_CLOSE.md`.

---

## 7. SOURCE MATERIAL

**Expected:** the Market Maker Method Bootcamp video library by Steve Mauro.

Working assumption, **unverified**: roughly 21 usable lesson videos, possibly
within a folder of ~24 files (some may be duplicates, intros, bonuses, or
non-lesson material). The exact count, order, and titles will be established only
by running `00_SYSTEM/SOURCE_INGESTION_PROTOCOL.md` against the real files.

Handling rules:

- Source videos are **read-only evidence**. Never edit, re-encode, rename, or move
  them.
- Source videos are **not committed to Git**. `.gitignore` excludes video formats
  from `01_SOURCE_VIDEOS/`.
- Each video is represented in Git by a manifest row in
  `00_SYSTEM/SOURCE_MANIFEST.md` with filename, size, duration, SHA-256 checksum,
  and relative path — so any artifact can later be traced to the exact file that
  produced it.
- Do not place generated research artifacts inside `01_SOURCE_VIDEOS/`.

This is proprietary paid course material. See §13, *Git & GitHub Workflow*.

---

## 8. PRIMARY RESEARCH INSTRUMENT

**GBP/USD.**

Used for manual chart study, manual backtesting, examples, later formalization,
TradingView validation, and automated historical testing.

If the instructor teaches a concept using a different instrument, that example is
preserved faithfully as taught. Do not assume a rule is GBP/USD-specific unless
evidence supports it.

---

## 9. STUDY METHODOLOGY

Per lesson, in order (full detail in `00_SYSTEM/STUDY_PROTOCOL.md`):

1. **Preview** — title, duration, subjects, homework references, continuity.
2. **Transcript** — `02_TRANSCRIPTS/VXX/VXX_TRANSCRIPT.md`, timestamped; uncertain
   wording marked, never silently invented.
3. **Source notes** — `03_LESSON_NOTES/VXX_SOURCE_NOTES.md`; explicit teaching only.
4. **Interpretation notes** — `03_LESSON_NOTES/VXX_INTERPRETATION.md`; kept
   strictly separate from source notes.
5. **Screenshots** — `04_SCREENSHOTS/VXX/` plus an `INDEX.md`.
6. **Homework** — `05_HOMEWORK/VXX/`, using Learn → Attempt → Grade → Diagnose →
   Reattempt → Pass, preserving the first attempt.
7. **Manual backtest** — `06_MANUAL_BACKTEST/VXX/`, one record per observation.
8. **Chart examples** — positive, negative, borderline, unresolved.
9. **Concept library, ambiguities, contradictions** — updated as encountered.
10. **Mastery report** — `07_MASTERY_REPORTS/VXX_MASTERY_REPORT.md`.
11. **Stop.** Request review. Do not start the next lesson.

### Evidence / provenance standard

Every important rule carries a classification and a traceable source:

| Label | Meaning |
|---|---|
| `EXPLICIT` | Directly stated by the instructor |
| `VISUAL` | Clearly demonstrated on a chart or slide |
| `IMPLIED` | Strongly suggested but not directly stated |
| `INFERRED` | Agent interpretation based on course material |
| `UNRESOLVED` | Still ambiguous or contradictory |

An inferred rule stays marked inferred until evidence supports promotion. A rule
with no citable source is an **orphan rule** and may not enter the canonical
methodology.

Evidence hierarchy, highest first: original video/audio → original
screenshots/charts/slides → transcript → instructor homework and solutions →
student source notes → student interpretation → student machine ideas. Lower
levels never override higher levels.

### Ambiguity & contradiction handling

- Subjective language ("strong push", "clean move", "enough space") is logged in
  `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md` and marked `DO NOT CODE`. It must not
  become an arbitrary numeric constant during the Student Phase.
- Conflicting teachings are logged in `11_CONTRADICTIONS/CONTRADICTIONS.md` as
  `RESOLVED` / `PROVISIONAL` / `UNRESOLVED`. They are never silently reconciled.

---

## 10. MANUAL VS AUTOMATED BACKTESTING

These are different activities at different phases and must not be confused.

| | Manual backtesting (now, Phase 1) | Automated backtesting (later, Phase 8+) |
|---|---|---|
| Purpose | Prove the agent can *apply* what was taught | Measure strategy performance |
| Method | Human-style sequential chart walk, future candles hidden at the decision point | Coded strategy over historical data |
| Output | Per-observation records in `06_MANUAL_BACKTEST/` | Metrics, equity curves, robustness tests in `15_AUTOMATED_BACKTEST/` |
| Judged by | Was the **rule applied correctly**? | Expectancy, drawdown, stability — never win rate alone |

The essential distinction, enforced in every manual backtest record:

> **Trade outcome ≠ rule application.**
> A losing trade can be a correctly applied rule.
> A winning trade can be an incorrectly applied rule.

Any manual backtest contaminated by hindsight or lookahead bias must be **redone**,
not edited. See `00_SYSTEM/REMEDIATION_PROTOCOL.md`.

---

## 11. CURRENT LIMITATION — SOURCE VIDEOS NOT ACCESSIBLE

The agent session that built this infrastructure had **no access to the bootcamp
video files**. Accordingly, and deliberately:

- No transcripts were created.
- No lessons were summarized.
- No Market Maker Method rules, concepts, or definitions were written.
- No screenshots were captured or referenced.
- No homework was attempted or answered.
- No manual or automated backtesting was performed.
- No chart examples were added.
- `12_MASTER_SPEC/` and `13_MACHINE_SPEC/` are empty of methodology.
- No Pine Script, signals, optimization, or win-rate estimates exist.
- The course sequence has **not** been inferred.

`00_SYSTEM/SOURCE_MANIFEST.md` contains **zero video rows**. It will be populated
only by running the ingestion protocol against real files.

### What to do when the videos are available

1. Place the video library at `01_SOURCE_VIDEOS/` (or a local path recorded in the
   manifest — the files themselves stay out of Git either way).
2. Start a Student session and say:
   *"Source videos are now available. Run the ingestion protocol, verify the course
   order, and begin Video 1."*
3. The agent runs `00_SYSTEM/SOURCE_INGESTION_PROTOCOL.md`, fills
   `SOURCE_MANIFEST.md`, flags any uncertain ordering for human confirmation, then
   processes **V01 only** and stops for review.

---

## 12. FOLDER STRUCTURE

```text
.
├── README.md                                  ← you are here
├── LOG.md                                     ← append-only research journal
├── CHANGELOG.md                               ← notable project changes
├── .gitignore
├── MMM_MASTER_STUDENT_RESEARCH_AGENT.md       ← governing file (Student)
├── MMM_INDEPENDENT_REVIEWER_TEACHER_AGENT.md  ← governing file (Reviewer)
│
├── 00_SYSTEM/            operating system: protocols, standards, prompts, templates
├── 01_SOURCE_VIDEOS/     read-only source media (contents not committed)
├── 02_TRANSCRIPTS/       VXX/VXX_TRANSCRIPT.md
├── 03_LESSON_NOTES/      VXX_SOURCE_NOTES.md + VXX_INTERPRETATION.md
├── 04_SCREENSHOTS/       VXX/ + VXX/INDEX.md
├── 05_HOMEWORK/          VXX/
├── 06_MANUAL_BACKTEST/   VXX/, cumulative/, datasets/
├── 07_MASTERY_REPORTS/   VXX_MASTERY_REPORT.md  (student self-assessment)
├── 08_CONCEPT_LIBRARY/   one file per concept + CONCEPT_INDEX.md
├── 09_CHART_EXAMPLES/    positive/, negative/, borderline/, unresolved/
├── 10_AMBIGUITIES/       AUTOMATION_AMBIGUITIES.md
├── 11_CONTRADICTIONS/    CONTRADICTIONS.md
├── 12_MASTER_SPEC/       canonical methodology (Phase 3 — empty until then)
├── 13_MACHINE_SPEC/      measurable machine layer (Phase 4 — empty until then)
├── 14_PINE/              TradingView code (Phase 5+ — empty until then)
├── 15_AUTOMATED_BACKTEST/ (Phase 8+ — empty until then)
├── 16_FORWARD_TEST/      (Phase 10 — empty until then)
├── 17_EXECUTION_ROBOT/   (Phase 12 — empty until then)
├── 18_REVIEW/            REVIEW_INDEX.md, VXX/, cumulative reviews
└── scripts/              validate_project.py (structural health check)
```

Every numbered directory contains a `README.md` explaining its contract.

---

## 13. GIT & GITHUB WORKFLOW

- Remote: `randy-schutt1/MMM-Agents` — **private**. It must stay private: the
  repository describes proprietary paid course material.
- **Never commit source videos.** They are excluded by `.gitignore`. If media must
  ever be versioned, that requires an explicit decision recorded in
  `00_SYSTEM/DECISIONS.md` and the use of Git LFS — not normal Git history.
- **Commit at checkpoints during a session, not once at the end** — roughly every
  5–10 artifacts, or at any natural boundary (`DECISIONS.md` D-015). A session can
  be interrupted, and uncommitted work is lost work. The commit sequence is also
  audit-trail evidence of the order in which understanding was built.
- Focused commits at logical checkpoints. Examples:

```text
chore: initialize MMM mastery project structure
study: complete video 01 transcript and notes
charts: add video 01 annotated examples
test: complete video 01 manual backtest
docs: certify video 01 mastery
review: pass video 01 mastery audit
review: request revisions for video 02
```

- Before every commit: review the diff, confirm no temp files, confirm no
  credentials or tokens, confirm no source media, confirm `LOG.md` is current.
- Never rewrite Git history to make the audit trail look cleaner. The history *is*
  the evidence.
- If a push fails, record why in `LOG.md`.

---

## 14. SESSION WORKFLOW

One lesson per session, and **separate sessions for student and reviewer work** —
independence is the point.

```text
Student session   → 00_SYSTEM/STUDENT_SESSION_PROMPT.md
Reviewer session  → 00_SYSTEM/REVIEWER_SESSION_PROMPT.md
```

Both start with `00_SYSTEM/SESSION_START.md` and end with
`00_SYSTEM/SESSION_CLOSE.md`.

---

## 15. HOW TO RESUME THIS PROJECT

Read, in order:

1. This `README.md`
2. The tail of `LOG.md`
3. `00_SYSTEM/COURSE_PROGRESS.md`
4. `00_SYSTEM/DECISIONS.md`
5. `18_REVIEW/REVIEW_INDEX.md`
6. `00_SYSTEM/SETUP_ISSUES.md`

Then run `git status`, run `python3 scripts/validate_project.py`, and identify the
first unfinished required artifact. Continue from there. Do not restart completed
work.

---

## 16. CURRENT COURSE PROGRESS

**0 videos ingested. 0 videos processed. 0 lessons reviewed. 0 lessons passed.**

Live detail: `00_SYSTEM/COURSE_PROGRESS.md` and `18_REVIEW/REVIEW_INDEX.md`.

---

## 17. STANDING PROHIBITIONS

Until the relevant phase is genuinely reached:

- Do not invent Market Maker Method rules or fill gaps from general trading
  knowledge.
- Do not import ICT, SMC, Wyckoff, Elliott Wave, or other external frameworks.
- Do not convert subjective course language into numeric constants.
- Do not write Pine Script or generate trading signals.
- Do not optimize anything, and do not treat any advertised accuracy claim
  (e.g. 90–95%) as a target. Record such claims with provenance and treat them as
  **hypotheses to test**, never as performance requirements.
- Do not advance a lesson without a reviewer `PASS`.
- Never treat backtested profitability as proof of live profitability, and never
  move from historical testing to unrestricted live trading.

---

**Master the method first. Formalize second. Automate third. Validate before
risking capital.**
