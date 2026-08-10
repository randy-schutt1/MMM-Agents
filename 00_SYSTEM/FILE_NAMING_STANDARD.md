# FILE NAMING STANDARD

Predictable names make the corpus navigable by future agents and humans, and make
`scripts/validate_project.py` able to check structure mechanically.

Source: `MMM_MASTER_STUDENT_RESEARCH_AGENT.md` §32.

---

## 1. GENERAL RULES

- **No spaces.** Use underscores between fields, hyphens inside a field's words.
- **Uppercase** for document type (`TRANSCRIPT`, `SOURCE_NOTES`, `MASTERY_REPORT`).
- **Lowercase** for free-text descriptors in screenshot names.
- **Zero-padded IDs**: `V01`, not `V1`. `BT_V01_0001`, not `BT_V1_1`.
- **No version words in filenames** — `final`, `new`, `latest`, `v2`, `updated`,
  `copy` are forbidden. Git holds versions. The one exception is the reviewer's
  explicit round suffix `_R1`, `_R2`, which is a first-class part of the audit
  trail.
- **Never rename an artifact after it is cited** by another file. Add a new file
  and cross-reference.

### Forbidden examples

```text
notes final.md
new test 2.md
screenshot.png
latest version final final.txt
V1 notes (copy).md
```

---

## 2. IDENTIFIERS

| Prefix | Meaning | Format | Example |
|---|---|---|---|
| `V` | Lesson video | `V` + 2 digits | `V07` |
| `X` | Non-lesson source file (handout, bonus, duplicate) | `X` + 2 digits | `X02` |
| `BT` | Manual backtest observation | `BT_VXX_NNNN` | `BT_V07_0013` |
| `A` | Ambiguity record | `A-NNN` | `A-004` |
| `C` | Contradiction record | `C-NNN` | `C-002` |
| `D` | Project decision | `D-NNN` | `D-011` |
| `I` | Setup issue | `I-NNN` | `I-003` |
| `E` | Reviewer error code | `ENN` | `E08` |
| `R` | Review round | `R` + integer | `R2` |
| `CL` | Concept library entry | `CL-NNN` | `CL-012` |

IDs are permanent. A superseded observation keeps its ID and gains a `SUPERSEDED`
marker; the replacement gets a **new** ID.

---

## 3. FILE NAMES BY DIRECTORY

### `02_TRANSCRIPTS/VXX/`

```text
VXX_TRANSCRIPT.md
```

### `03_LESSON_NOTES/`

```text
VXX_SOURCE_NOTES.md
VXX_INTERPRETATION.md
```

### `04_SCREENSHOTS/VXX/`

```text
INDEX.md
VXX_HH-MM-SS_short-descriptor.png
```

Timestamp uses hyphens (colons are illegal in filenames on some systems).
Descriptor is lowercase, hyphenated, 2–5 words, describing **what is shown** — not
an interpretation.

```text
V07_00-43-12_three-push-example.png        ← good
V07_00-43-12_perfect-entry-signal.png      ← bad: interpretation, not content
V07_screenshot3.png                        ← bad: meaningless
```

### `05_HOMEWORK/VXX/`

```text
VXX_HOMEWORK_NN.md
VXX_HOMEWORK_NN_attempt1.png
VXX_HOMEWORK_NN_final.png
```

The first attempt is preserved permanently — never overwritten by the corrected
version.

### `06_MANUAL_BACKTEST/VXX/`

```text
BT_VXX_NNNN.md
BT_VXX_NNNN_before.png
BT_VXX_NNNN_after.png
```

`before` = the chart at the decision point, with future candles hidden.
`after` = the same chart with the outcome revealed.

Observation numbers are sequential within a lesson and never reused.

### `06_MANUAL_BACKTEST/cumulative/`

```text
CUMULATIVE_SUMMARY.md
CUMULATIVE_VXX_TO_VYY.md
```

### `07_MASTERY_REPORTS/`

```text
VXX_MASTERY_REPORT.md
```

One per lesson. Revisions append a `## Revision R<n>` section rather than creating
a new file.

### `08_CONCEPT_LIBRARY/`

```text
CONCEPT_INDEX.md
CL-NNN_concept-name.md
```

Example: `CL-003_peak-formation-high.md`. Use the instructor's terminology in the
name; do not rename a concept to a more familiar external term.

### `09_CHART_EXAMPLES/{positive,negative,borderline,unresolved}/`

```text
VXX_concept-name_NNN.png
VXX_concept-name_NNN.md
```

The `.md` sidecar records what the example shows, why it is classified this way,
what was visible at the decision point, and which rule it supports or violates.
An image with no sidecar is not evidence.

### `10_AMBIGUITIES/` and `11_CONTRADICTIONS/`

Single accumulating files:

```text
10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md
11_CONTRADICTIONS/CONTRADICTIONS.md
```

Records are `A-NNN` / `C-NNN` sections within them.

### `18_REVIEW/`

```text
REVIEW_INDEX.md
CUMULATIVE_25.md
CUMULATIVE_50.md
CUMULATIVE_75.md
FINAL_COURSE_REVIEW.md
VXX/VXX_REVIEW_R1.md
VXX/VXX_REVIEW_R2.md
```

Never overwrite a review round. See `SETUP_ISSUES.md` I-002.

### `12_MASTER_SPEC/` (Phase 3)

```text
MMM_MASTER_SPECIFICATION.md
```

### `13_MACHINE_SPEC/` (Phase 4)

```text
MMM_MACHINE_SPECIFICATION.md
```

### `14_PINE/` (Phase 5+)

```text
mmm_<component>_v<major>.<minor>.pine
```

Example: `mmm_peak_formation_v0.1.pine`. Indicator logic stays separate from
strategy logic.

---

## 4. CROSS-REFERENCING

Cite artifacts by their identifier, and prefer repository-relative paths:

```text
See BT_V07_0013.
Evidence: V07 @ 00:43:12 — 04_SCREENSHOTS/V07/V07_00-43-12_three-push-example.png
Rule classification per CL-003.
Blocked by A-004 (DO NOT CODE).
Reviewer finding: E08 / CRITICAL, 18_REVIEW/V07/V07_REVIEW_R1.md
```

Every rule statement in the corpus should be traceable to a video ID and timestamp,
and through `SOURCE_MANIFEST.md` to a SHA-256.

---

## 5. STATUS MARKERS

Applied inside files, not in filenames:

```text
SUPERSEDED — INVALID PROCEDURE (see R<n> finding)
SUSPECT — FABRICATION FINDING R<n>
PROVISIONAL
UNRESOLVED
DO NOT CODE
HUMAN REVIEW REQUIRED
INFERRED MACHINE CANDIDATE — NOT A COURSE RULE
```

Superseded work stays in the repository. Deleting it would destroy the audit trail.
