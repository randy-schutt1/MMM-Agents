# TEMPLATES

Reusable skeletons that keep artifacts consistent across sessions, models, and
months. Copy the template, fill it in, and **delete the instruction blocks**.

All templates derive from the two governing files. If a template ever conflicts
with a governing file, the governing file wins — record the conflict in
`00_SYSTEM/SETUP_ISSUES.md`.

**No template contains Market Maker Method content.** They contain structure and
integrity checks only. Any trading terminology appearing in a template
(e.g. "peak formation", "push") is illustrative of *format*, drawn from the
governing files' own examples — not a claim about what the course teaches.

| Template | Copy to | Used by |
|---|---|---|
| `TRANSCRIPT_TEMPLATE.md` | `02_TRANSCRIPTS/VXX/VXX_TRANSCRIPT.md` | Student |
| `SOURCE_NOTES_TEMPLATE.md` | `03_LESSON_NOTES/VXX_SOURCE_NOTES.md` | Student |
| `INTERPRETATION_TEMPLATE.md` | `03_LESSON_NOTES/VXX_INTERPRETATION.md` | Student |
| `SCREENSHOT_INDEX_TEMPLATE.md` | `04_SCREENSHOTS/VXX/INDEX.md` | Student |
| `HOMEWORK_TEMPLATE.md` | `05_HOMEWORK/VXX/VXX_HOMEWORK_NN.md` | Student |
| `MANUAL_BACKTEST_TEMPLATE.md` | `06_MANUAL_BACKTEST/VXX/BT_VXX_NNNN.md` | Student |
| `MASTERY_REPORT_TEMPLATE.md` | `07_MASTERY_REPORTS/VXX_MASTERY_REPORT.md` | Student |
| `CONCEPT_TEMPLATE.md` | `08_CONCEPT_LIBRARY/CL-NNN_concept-name.md` | Student |
| `AMBIGUITY_TEMPLATE.md` | a new `A-NNN` section in `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md` | Student |
| `CONTRADICTION_TEMPLATE.md` | a new `C-NNN` section in `11_CONTRADICTIONS/CONTRADICTIONS.md` | Student |
| `REVIEW_TEMPLATE.md` | `18_REVIEW/VXX/VXX_REVIEW_R<n>.md` | Reviewer |

## Notes

- The ambiguity and contradiction templates are **section** templates — those two
  logs are single accumulating files, not directories of separate records.
- Sections are load-bearing. A section left blank is a finding the reviewer will
  ask about; a section deleted looks like it never applied. Prefer writing
  `none` / `n/a` with a reason.
- The integrity checklists (manual backtest §9, mastery report QC, review
  self-check) are not decoration — the reviewer audits against them directly.
- Filenames follow `00_SYSTEM/FILE_NAMING_STANDARD.md`.

## Changing a template

Templates may improve as the project learns. When one changes:

1. Note it in `CHANGELOG.md`.
2. Do **not** retroactively reformat existing artifacts — the corpus is an audit
   trail, and churn obscures what was actually known when.
3. If the change alters what evidence is required (not merely its layout), record a
   decision in `00_SYSTEM/DECISIONS.md`.
