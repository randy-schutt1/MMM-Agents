# Videos 1–10 Evidence Inventory

This inventory records the evidence actually used to establish scope and testability. Counts are descriptive; a large count does not raise an item's source tier.

## Repository lineage

| Repository | Audited HEAD | Role in this suite |
|---|---|---|
| `MMM-Agents-v10` | `e5262b2` | Earlier student snapshot; used to identify what status/remediation did not yet exist |
| `MMM-Agents` | `a004e88` | Current authoritative repository; source of all suite citations and assets |

The current `18_REVIEW/REVIEW_INDEX.md` contains substantially later V09/V10 review-state material than the v10 snapshot. No suite files were written into the historical snapshot.

## Source and artifact census

All ten V01–V10 SWFs exist in the canonical source directory. Each was rehashed during the final audit and matched the SHA-256 value in `00_SYSTEM/SOURCE_MANIFEST.md`. V11 media and lesson artifacts were not opened.

| Video | SWF checksum | Transcript | Source + interpretation notes | Indexed PNG frames | Homework/support files | Reported manual-backtest records | Mastery report | Independent review files | Controlling status |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| V01 | Match | 1 | 2 | 22 | 0 | 5 | 1 | 3 | R3 PASS |
| V02 | Match | 1 | 2 | 25 | 2 | 10 | 1 | 3 | R3 PASS |
| V03 | Match | 1 | 2 | 24 | 1 | 3 | 1 | 3 | R3 PASS |
| V04 | Match | 1 | 2 | 27 | 1 | 3 | 1 | 2 | R2 PASS |
| V05 | Match | 1 | 2 | 30 | 1 | 0 | 1 | 4 | R3 PASS |
| V06 | Match | 1 | 2 | 32 | 1 | 1 | 1 | 2 | R2 PASS |
| V07 | Match | 1 | 2 | 24 | 1 | 1 | 1 | 3 | R3 PASS |
| V08 | Match | 1 | 2 | 26 | 1 | 1 | 1 | 2 | R2 PASS |
| V09 | Match | 1 | 2 | 27 | 1 | 1 | 1 | 2 | Self-verified complete; R2 remained REVISE |
| V10 | Match | 1 | 2 | 32 | 3 | 1 | 1 | 1 | Self-verified complete after R1 REVISE |

“Reported manual-backtest records” counts `BT_*.md` lesson records, not every metric/arm within a record. The cumulative register remains controlling: 21 of 33 pre-registered PT files were run and reported, with retired/superseded/unrun items retained rather than hidden.

## Evidence strength and limitations

- SWFs, verified lesson screenshots, and reliable recording-aligned transcripts control lesson content.
- Source notes locate the controlling recording passage; they do not outrank the recording.
- Interpretation files, mastery reports, owner attestations, and historical studies remain separately labelled.
- Review counts do not imply PASS: V09 has no final independent PASS file and V10 has no independent remediation-round PASS.
- V01 has no separate homework artifact; V05 has no reported `BT_*.md` record. Absence is preserved rather than filled with invented material.
- Existing `09_CHART_EXAMPLES` classification folders contain no promoted examples and `08_CONCEPT_LIBRARY` contains no promoted concepts. The suite therefore keeps recognition gaps visible.
- The source manifest's processing-status column is stale for several lessons; `18_REVIEW/REVIEW_INDEX.md` controls current review status.
