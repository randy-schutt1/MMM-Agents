# SOURCE MANIFEST

Authoritative inventory of bootcamp source material.

Procedure: `SOURCE_INGESTION_PROTOCOL.md`.

---

## STATUS

```text
INGESTION STATUS:  NOT STARTED
FILES INVENTORIED: 0
LESSONS VERIFIED:  0
SOURCE LOCATION:   NOT YET PROVIDED
```

**No source video file has been seen, inventoried, hashed, or processed by any
agent session.** The table below is intentionally empty. It must be populated only
by running the ingestion protocol against real files.

Do not add speculative rows. Do not record a filename, title, duration, or lesson
number that has not been read off an actual file.

---

## EXPECTED SCOPE (UNVERIFIED)

The project owner expects **approximately 21 usable lesson videos**, possibly
inside a folder containing **around 24 files** (the remainder may be duplicates,
intros, bonuses, or handouts).

This is an expectation carried into the project, **not a verified fact**. The real
count, order, and titles are established only by ingestion. Nothing in this
repository should treat "21" or "24" as known.

---

## SOURCE LOCATION

| Field | Value |
|---|---|
| Arrangement | `NOT YET DETERMINED` (in-repo `01_SOURCE_VIDEOS/`, or external path) |
| Absolute root path | `NOT YET PROVIDED` |
| Recorded in `DECISIONS.md` | Pending — add as a new decision at ingestion time |

---

## MANIFEST TABLE

| Video ID | Original Filename | Lesson Title | Duration | File Size | Relative Path | SHA-256 | Ordering Confidence | Processing Status |
|---|---|---|---|---|---|---|---|---|
| _(empty — no files ingested)_ | | | | | | | | |

### Column definitions

| Column | Rule |
|---|---|
| **Video ID** | `V01`, `V02`, … assigned in verified lesson order. Non-lesson files get `X01`, `X02`, … |
| **Original Filename** | Exact filename as it exists on disk. Never renamed. |
| **Lesson Title** | As stated by the instructor or the file itself. `UNKNOWN` if not stated — **never invented**. |
| **Duration** | `HH:MM:SS` from `ffprobe`, or `UNKNOWN — no probe tooling`. Never estimated. |
| **File Size** | Bytes (and a human-readable value in parentheses). |
| **Relative Path** | Path relative to the recorded source root. |
| **SHA-256** | Full hex digest. The reproducibility anchor. |
| **Ordering Confidence** | `CERTAIN` / `LIKELY` / `UNCERTAIN` / `NOT A LESSON`. |
| **Processing Status** | `NOT STARTED` / `IN PROGRESS` / `STUDENT COMPLETE` / `IN REVIEW` / `IN REMEDIATION` / `PASSED`. |

---

## NON-LESSON AND SUPPORTING MATERIAL

PDFs, worksheets, spreadsheets, images, and bonus files found alongside the videos
are evidence and belong here too, with IDs `X01`, `X02`, …

| ID | Filename | Type | File Size | Relative Path | SHA-256 | Notes |
|---|---|---|---|---|---|---|
| _(empty)_ | | | | | | |

---

## INGESTION ANOMALIES

Recorded during ingestion; each requires a decision before the affected lesson is
studied.

| # | File(s) | Anomaly | Action Required | Status |
|---|---|---|---|---|
| _(none — ingestion not run)_ | | | | |

Anomaly types to watch for: duplicate checksums; expected-but-missing lesson
numbers; anomalous size or duration; unreadable or corrupt files; ambiguous
ordering; files that appear to be a different course.

---

## CHECKSUM CHANGE HISTORY

If a source file is ever replaced or re-downloaded, add a **new row** here. Never
edit a checksum in place — artifacts derived from the old file may no longer match
their source.

| Date | Video ID | Old SHA-256 | New SHA-256 | Reason | Artifacts Affected | Re-processing Decision |
|---|---|---|---|---|---|---|
| _(none)_ | | | | | | |

---

## HANDLING RULES

- Source media is **never committed to Git** (`.gitignore`). This manifest is the
  Git-visible representation of the library.
- Source files are **never modified**. If transcoding is required for processing,
  the derivative is written outside `01_SOURCE_VIDEOS/` and the manifest notes that
  a derivative was used.
- Every research artifact must be traceable to a Video ID and, through it, to a
  SHA-256.
- Study is sequential and gated: no lesson begins until the previous lesson holds a
  reviewer `PASS`.
