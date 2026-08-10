# SOURCE INGESTION PROTOCOL

How to inventory the bootcamp video library when it becomes locally available.

Source: `MMM_MASTER_STUDENT_RESEARCH_AGENT.md` §§9, 10, 31.

> **STATUS: NOT YET EXECUTED.** No source video has been seen by any agent session.
> `SOURCE_MANIFEST.md` contains zero rows. Do not run any part of this protocol
> against nonexistent files, and do not pre-create manifest rows, lesson folders,
> or progress rows for videos that have not been verified to exist.

---

## 1. PURPOSE

Before any lesson is studied, the project must be able to prove **which exact file**
produced **which artifact**. That requires an inventory with checksums, captured
before processing begins.

---

## 2. PRINCIPLES

1. **Source videos are read-only evidence.** Never edit, re-encode, rename, move,
   trim, or "clean up" a source file.
2. **Source videos are not committed to Git.** They are excluded by `.gitignore`.
   Git holds the manifest, not the media.
3. **Do not place generated artifacts inside `01_SOURCE_VIDEOS/`.**
4. **Do not guess.** Uncertain lesson ordering is flagged for human confirmation,
   not resolved by assumption.
5. **Do not infer course content from filenames.** A filename may suggest a topic;
   it is not a lesson, and it must not seed notes, concepts, or the master spec.

---

## 3. PROCEDURE

### STEP 1 — Locate the source files

Determine the actual local path. Two acceptable arrangements:

- **In-repo (ignored):** files placed at `01_SOURCE_VIDEOS/`. Git ignores the
  media; the folder's `README.md` stays tracked.
- **External:** files remain elsewhere on the machine. Record the absolute path in
  the manifest header and use relative paths from that root in the rows.

Record which arrangement is in use, in the manifest header and in `DECISIONS.md`.

### STEP 2 — Do not alter anything

Read-only operations only. No renaming, no conversion, no moving. If a file must be
transcoded to be processed, write the derivative to a working directory outside
`01_SOURCE_VIDEOS/`, and record that the derivative — not the original — was
processed.

### STEP 3 — Capture filenames

List every file in the source folder, including non-video files (PDFs, worksheets,
images, spreadsheets). Bonus material and instructor handouts are evidence too and
belong in the manifest, marked with their type.

```bash
ls -1 "<SOURCE_DIR>"
```

### STEP 4 — Capture file sizes

```bash
# bytes, portable enough for macOS and Linux
find "<SOURCE_DIR>" -maxdepth 1 -type f -exec ls -l {} \;
```

### STEP 5 — Capture durations (if tooling allows)

If `ffprobe` is available:

```bash
ffprobe -v error -show_entries format=duration \
        -of default=noprint_wrappers=1:nokey=1 "<FILE>"
```

If no tooling is available, record `duration: UNKNOWN — no probe tooling`.
**Do not estimate a duration.**

### STEP 6 — Calculate SHA-256

```bash
shasum -a 256 "<FILE>"     # macOS
sha256sum "<FILE>"         # Linux
```

This is the anchor for reproducibility: every transcript, screenshot, and backtest
observation traces back to a checksum, so a future researcher can confirm the same
source file was used.

Large libraries take a while to hash. Do it once, completely, before studying.

### STEP 7 — Determine likely lesson order

Evidence for ordering, strongest first:

1. An explicit numbering scheme in the filenames.
2. An instructor-provided index, curriculum, or playlist file in the folder.
3. Content-based ordering (a lesson that opens by referencing the previous one) —
   only usable after the videos are actually watched.
4. File modification timestamps — **weak**; downloads reorder them routinely.

Assign IDs `V01`, `V02`, … in the determined order. The ID is the project's
identifier; the original filename is preserved alongside it in the manifest.

### STEP 8 — Flag uncertain ordering

Each row gets an ordering confidence:

| Confidence | Meaning |
|---|---|
| `CERTAIN` | Explicit numbering or an instructor index establishes position |
| `LIKELY` | Strong but indirect evidence |
| `UNCERTAIN` | Position is a guess — **must be confirmed by a human before study** |
| `NOT A LESSON` | Duplicate, intro, bonus, handout, or non-course file |

**If any lesson in the first few positions is `UNCERTAIN`, stop and ask the project
owner before processing V01.** Studying the course out of order corrupts the
dependency chain that the mastery gate depends on.

Also flag: probable duplicates (identical checksums are definitive), files whose
size or duration looks anomalous, and any expected-but-missing lesson number.

### STEP 9 — Create / update `SOURCE_MANIFEST.md`

Fill one row per file with: Video ID, original filename, lesson title (as given —
`UNKNOWN` if not stated; do not invent one), duration, file size, relative path,
SHA-256, ordering confidence, processing status.

Set every processing status to `NOT STARTED`.

Then expand `COURSE_PROGRESS.md` to exactly the number of verified lesson videos —
no more, no fewer — and create `02_TRANSCRIPTS/VXX/` and `04_SCREENSHOTS/VXX/`
folders as each lesson is actually started (not all at once).

Commit: `chore: ingest source video manifest with checksums`.

### STEP 10 — Never begin Video 2 before Video 1 has passed review

Ingestion inventories the whole library at once. **Study is strictly sequential**
and gated: V01 must carry a reviewer `PASS` in `18_REVIEW/REVIEW_INDEX.md` before
V02 is opened.

---

## 4. RE-INGESTION

If files are added, replaced, or re-downloaded later:

1. Re-run the checksum step for affected files.
2. If a checksum changed for an already-processed lesson, that is a **material
   event**: the artifacts derived from the old file may no longer match the source.
   Record it in `LOG.md` and `DECISIONS.md`, add a new manifest row rather than
   overwriting the old one, and ask the reviewer whether re-processing is required.
3. Never silently update a checksum in place.

---

## 5. WHAT THIS PROTOCOL DOES NOT DO

It does not transcribe, summarize, interpret, or study anything. It produces an
inventory and nothing else.

After ingestion completes, the next step is `STUDY_PROTOCOL.md` §1, Step 1
(Preview) for **V01 only**.
