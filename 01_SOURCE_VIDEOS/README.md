# 01_SOURCE_VIDEOS

Read-only source media for the Market Maker Method Bootcamp.

## STATUS: EMPTY — NO SOURCE MEDIA PRESENT

No video file has been placed here, inventoried, or processed.

## RULES

1. **Read-only evidence.** Never edit, re-encode, rename, move, trim, or "clean up"
   a source file. If transcoding is required for processing, write the derivative
   outside this folder and record that a derivative was used.
2. **Not committed to Git.** `.gitignore` excludes `01_SOURCE_VIDEOS/**` (this
   README excepted) and common video/audio extensions repository-wide. The material
   is proprietary paid course content and the files are large
   (`DECISIONS.md` D-011).
3. **No generated artifacts here.** Transcripts, notes, and screenshots go to their
   own numbered directories. This folder holds source only.
4. **Represented in Git by the manifest.** `00_SYSTEM/SOURCE_MANIFEST.md` holds
   filename, size, duration, SHA-256, and relative path for every file — so any
   artifact can be traced to the exact source that produced it.

## ALTERNATIVE: EXTERNAL LOCATION

The library may instead stay elsewhere on the machine. In that case record the
absolute root path in the manifest header and add a decision to `DECISIONS.md`.
Either arrangement is fine; what matters is that the manifest is accurate.

## WHEN THE VIDEOS ARRIVE

Run `00_SYSTEM/SOURCE_INGESTION_PROTOCOL.md`. It inventories files, computes
checksums, determines likely lesson order, and flags uncertain ordering for human
confirmation — before any lesson is studied.
