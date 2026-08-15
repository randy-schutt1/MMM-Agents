#!/usr/bin/env python3
"""Deterministic Phase 2 remediation and gate checks."""

from pathlib import Path
import subprocess
import sys
from typing import List, Optional

ROOT = Path(__file__).resolve().parents[1]
errors: List[str] = []


def require(path: str, needle: Optional[str] = None) -> str:
    p = ROOT / path
    if not p.is_file() or p.stat().st_size == 0:
        errors.append(f"missing or empty: {path}")
        return ""
    text = p.read_text(errors="replace")
    if needle is not None and needle not in text:
        errors.append(f"{path}: missing {needle!r}")
    return text


for artifact in (
    "00_SYSTEM/PHASE_2_GATE_AUDIT.md",
    "00_SYSTEM/SELF_VERIFICATION_POLICY.md",
    "00_SYSTEM/PHASE_2_REMEDIATION_LEDGER.md",
    "00_SYSTEM/PHASE_2_V11_V15_REMEDIATION_LEDGER.md",
    "00_SYSTEM/PHASE_2_HUMAN_RECONSTRUCTION_AUDIT.md",
    "00_SYSTEM/PHASE_2_VALIDATION_REPORT.md",
    "00_SYSTEM/PHASE_2_REVIEW_HANDOFF.md",
    "18_REVIEW/PHASE_2_OWNER_REVIEWER_CLOSEOUT.md",
    "19_STUDENT_TEST_SUITE_V01_V10/retests/PHASE_2_TARGETED_RETEST_001/README.md",
    "19_STUDENT_TEST_SUITE_V01_V10/retests/PHASE_2_TARGETED_RETEST_001/STUDENT_PACKET.md",
    "19_STUDENT_TEST_SUITE_V01_V10/retests/PHASE_2_TARGETED_RETEST_001/RESULTS_TEMPLATE.md",
    "19_STUDENT_TEST_SUITE_V01_V10/retests/PHASE_2_TARGETED_RETEST_001/INSTRUCTOR_KEY.md",
):
    require(artifact)

policy = require("00_SYSTEM/SELF_VERIFICATION_POLICY.md")
for label in (
    "APPLIED — AWAITING INDEPENDENT REVIEW",
    "CLOSED — SELF-VERIFIED AT OWNER DIRECTION",
    "CLOSED — VERIFIED",
    "CLOSED — REVIEWER REMEDIATED AT OWNER DIRECTION",
    "it does not produce an independent reviewer `PASS`",
    "D-062 records the owner's intended reviewer workflow",
):
    if label not in policy:
        errors.append(f"self-verification policy missing canonical boundary: {label!r}")

ledger = require("00_SYSTEM/PHASE_2_REMEDIATION_LEDGER.md", "**14**")
for item in (244, 245, 246, 247, 248, 249, 264, 265, 266, 267, 268, 303, 304, 348):
    if f"| {item} |" not in ledger:
        errors.append(f"remediation ledger missing item {item}")

legacy_ledger = require("00_SYSTEM/PHASE_2_V11_V15_REMEDIATION_LEDGER.md", "**13**")
for item in (109, 110, 111, 112, 113, 154, 155, 197, 198, 199, 200, 201, 202):
    if f"| {item} |" not in legacy_ledger:
        errors.append(f"V11/V13/V15 remediation ledger missing item {item}")

checks = {
    "02_TRANSCRIPTS/V17/V17_TRANSCRIPT.md": "extra **week in between**",
    "10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md": "how many candles does it take",
    "06_MANUAL_BACKTEST/V17/BT_V17_0001.md": "`load_m1` path",
    "00_SYSTEM/QUARANTINE_REGISTER.md": "10 differing lines = FIVE changed pairs",
    "05_HOMEWORK/V18/V18_HOMEWORK.md": "4.3× as likely",
    "04_SCREENSHOTS/V18/INDEX.md": "24 of the 26 filenames",
    "06_MANUAL_BACKTEST/V18/BT_V18_0001.md": "571 / 1,122 = 0.5089",
    "03_LESSON_NOTES/V18_SOURCE_NOTES.md": "`[00:42:11]`–`[00:42:13]`",
    "02_TRANSCRIPTS/V19/V19_TRANSCRIPT.md": "eight of twelve returned",
    "03_LESSON_NOTES/V19_INTERPRETATION.md": "**It remains untested.**",
    "06_MANUAL_BACKTEST/V20/BT_V20_0001.md": "direction convention now declared",
}
for path, needle in checks.items():
    require(path, needle)

gate = require("00_SYSTEM/PHASE_2_GATE_AUDIT.md", "TOTAL REVIEWED AND APPROVED:                  21 / 21")
for required in ("LESSON-REVIEW BACKLOG:                         0 / 21",
                 "TARGETED STUDENT RETEST: PENDING", "D-062"):
    if required not in gate:
        errors.append(f"gate audit missing owner-closeout state {required!r}")
require("18_REVIEW/V09/V09_REVIEW_R4.md", "Items **81–83 are `CLOSED — VERIFIED`**")
require("18_REVIEW/V10/V10_REVIEW_R2.md", "Items **91–94 are `CLOSED — VERIFIED`**")
require("18_REVIEW/V12/V12_REVIEW_R2.md", "Items **137–138 are `CLOSED — VERIFIED`**")
require("18_REVIEW/V14/V14_REVIEW_R2.md", "Items **172–176 are `CLOSED — VERIFIED`**")
require("18_REVIEW/V16/V16_REVIEW_R2.md", "Items **222–225 are `CLOSED — VERIFIED`**")

handoff = require("00_SYSTEM/PHASE_2_REVIEW_HANDOFF.md")
for required in ("21/21 reviewed and approved", "zero lesson-review backlog",
                 "clean Student session", "CUMULATIVE_75.md", "FINAL_COURSE_REVIEW.md"):
    if required not in handoff:
        errors.append(f"remaining-work handoff missing {required!r}")

closeout = require("18_REVIEW/PHASE_2_OWNER_REVIEWER_CLOSEOUT.md", "Total: 27 Phase 2 findings")
for finding_range in ("109–113", "154–155", "197–202", "244–249", "264–268", "302–304", "348"):
    if finding_range not in closeout:
        errors.append(f"owner reviewer closeout missing finding range {finding_range}")

cumulative_25 = require("18_REVIEW/CUMULATIVE_25.md", "COMPLETED — HALT AND REMEDIATE")
cumulative_50 = require("18_REVIEW/CUMULATIVE_50.md", "COMPLETED — HALT AND REMEDIATE")
cumulative_75 = require("18_REVIEW/CUMULATIVE_75.md")
if "NOT STARTED" not in cumulative_75:
    errors.append("75% cumulative checkpoint started before its prerequisites cleared")
for path, text in (
    ("18_REVIEW/CUMULATIVE_25.md", cumulative_25),
    ("18_REVIEW/CUMULATIVE_50.md", cumulative_50),
):
    for required in ("V05-06", "UNRESOLVED", "targeted retest", "PROCEED TO NEXT LESSONS: NOT AUTHORIZED"):
        if required not in text:
            errors.append(f"{path}: missing cumulative-failure control {required!r}")

course_progress = require("00_SYSTEM/COURSE_PROGRESS.md")
for checkpoint_row in (
    "| 25% | V05 | `18_REVIEW/CUMULATIVE_25.md` | **COMPLETED — HALT AND REMEDIATE** |",
    "| 50% | V10 | `18_REVIEW/CUMULATIVE_50.md` | **COMPLETED — HALT AND REMEDIATE** |",
):
    if checkpoint_row not in course_progress:
        errors.append(f"course progress missing cumulative checkpoint state: {checkpoint_row}")

reconstruction = require("00_SYSTEM/PHASE_2_HUMAN_RECONSTRUCTION_AUDIT.md")
for required in ("25% and 50% cumulative checkpoints are now completed",
                 "Tier-1 V13 definition", "`NOT MASTERED`"):
    if required not in reconstruction:
        errors.append(f"human reconstruction audit missing Phase 2 update {required!r}")

concept_index = require("08_CONCEPT_LIBRARY/CONCEPT_INDEX.md")
if "25% and 50% cumulative reviews" not in concept_index:
    errors.append("concept index formal-status boundary is stale")

retest_root = "19_STUDENT_TEST_SUITE_V01_V10/retests/PHASE_2_TARGETED_RETEST_001"
student_packet = require(f"{retest_root}/STUDENT_PACKET.md", "Closed book")
instructor_key = require(f"{retest_root}/INSTRUCTOR_KEY.md", "SEALED INSTRUCTOR KEY")
results_template = require(f"{retest_root}/RESULTS_TEMPLATE.md", "NOT SELF-GRADED")
for case_number in range(1, 11):
    case_id = f"R{case_number:02d}"
    if f"## {case_id}" not in student_packet:
        errors.append(f"targeted retest student packet missing {case_id}")
    if f"| {case_id} |" not in instructor_key:
        errors.append(f"targeted retest instructor key missing {case_id}")
for boundary in ("CF-A", "CF-B", "CF-C", "CF-D", "90/100", "NOT MASTERED"):
    if boundary not in instructor_key:
        errors.append(f"targeted retest key missing hard-gate boundary {boundary!r}")
if "FUTURE INFORMATION USED: NO" not in results_template:
    errors.append("targeted retest results template missing lookahead declaration")

final_review = require("18_REVIEW/FINAL_COURSE_REVIEW.md")
if "NOT STARTED" not in final_review:
    errors.append("final course review gate was changed")

for protected in ("12_MASTER_SPEC", "13_MACHINE_SPEC"):
    live = [p for p in (ROOT / protected).iterdir() if p.name not in {"README.md", ".gitkeep"}]
    if live:
        errors.append(f"{protected} contains gated artifacts: {', '.join(p.name for p in live)}")

for stale_path in (
    "00_SYSTEM/MMM_CURRENT_STATE.md",
    "00_SYSTEM/MMM_GAP_AND_DEPENDENCY_MATRIX.md",
    "00_SYSTEM/PHASE_1_HANDOFF.md",
    "00_SYSTEM/PHASE_1_VALIDATION_REPORT.md",
):
    text = require(stale_path)
    if "twelve open V17–V20" in text or "twelve V17–V20 minor" in text:
        errors.append(f"{stale_path}: uncorrected twelve-item claim")

diff = subprocess.run(
    ["git", "diff", "--check"], cwd=ROOT, text=True, capture_output=True, check=False
)
if diff.returncode:
    errors.append("git diff --check failed:\n" + diff.stdout + diff.stderr)

if errors:
    print("PHASE 2 VALIDATION: FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("PHASE 2 VALIDATION: PASS")
print("- remediation findings represented: 14/14")
print("- V11/V13/V15 remediation represented: 13/13; closed under D-062")
print("- V17-V20 remediation represented: 14/14; closed under D-062")
print("- lesson census: 21/21 reviewed and approved; zero lesson-review backlog")
print("- historical REVISE decisions and owner-closeout labels: preserved")
print("- cumulative 25/50: completed, HALT AND REMEDIATE; targeted retest required")
print("- targeted retest: sealed student/instructor packet present; clean Student execution pending")
print("- cumulative 75: NOT STARTED")
print("- final review: NOT STARTED")
print("- master/machine specifications: still empty")
print("- git diff whitespace check: pass")
