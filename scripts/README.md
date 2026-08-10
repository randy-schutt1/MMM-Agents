# scripts

Project tooling.

## `validate_project.py`

Structural health check. Run it at session start and before every commit.

```bash
python3 scripts/validate_project.py            # full output
python3 scripts/validate_project.py --quiet    # problems only
python3 scripts/validate_project.py --strict   # warnings become failures
```

Exit codes: `0` passed · `1` failures · `2` could not run.

### What it checks

- Required directories and files exist (root, `00_SYSTEM/`, templates, review
  infrastructure, accumulating logs).
- Required files are not empty — an empty required file is worse than a missing
  one, because it looks done.
- `COURSE_PROGRESS.md`, `SOURCE_MANIFEST.md`, and `REVIEW_INDEX.md` have their
  expected columns and fields.
- Per-lesson artifact consistency for lessons that have been started: transcript
  present, interpretation separated from source notes, screenshots indexed, mastery
  report present when a review exists. Silent when no lesson has started.
- Git hygiene: no tracked video/audio, no obviously secret-named tracked files, no
  oversized tracked files, `.gitignore` covers source media and secrets.
- `01_SOURCE_VIDEOS/` contains no generated artifacts.

### What it deliberately does NOT check

**Anything about the Market Maker Method.**

It cannot tell whether a rule is correctly understood, whether a backtest was
honest, whether hindsight contaminated a classification, or whether a lesson
deserves to pass. A green result means the scaffolding is intact — nothing more.

Those judgements require reading source evidence and belong to the Independent
Reviewer Agent (`00_SYSTEM/REVIEW_PROTOCOL.md`). A script that appeared to grade
methodology would be worse than no script, because a passing run would read as
validation.

### Requirements

Python 3.9+, standard library only. `git` optional — without it, tracked-file
checks warn and skip.
