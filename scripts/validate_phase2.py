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
):
    require(artifact)

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

gate = require("00_SYSTEM/PHASE_2_GATE_AUDIT.md", "INDEPENDENT REVIEWER PASS: 14 / 21")
if "LATEST INDEPENDENT DECISION REVISE: 7 / 21" not in gate:
    errors.append("gate audit missing 7/21 REVISE census")
require("18_REVIEW/V09/V09_REVIEW_R4.md", "Items **81–83 are `CLOSED — VERIFIED`**")
require("18_REVIEW/V10/V10_REVIEW_R2.md", "Items **91–94 are `CLOSED — VERIFIED`**")
require("18_REVIEW/V12/V12_REVIEW_R2.md", "Items **137–138 are `CLOSED — VERIFIED`**")
require("18_REVIEW/V14/V14_REVIEW_R2.md", "Items **172–176 are `CLOSED — VERIFIED`**")
require("18_REVIEW/V16/V16_REVIEW_R2.md", "Items **222–225 are `CLOSED — VERIFIED`**")

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
print("- V11/V13/V15 backlog remediation represented: 13/13; independent R2 pending")
print("- formal independent-PASS census: 14/21")
print("- seven latest independent non-PASS decisions: preserved")
print("- final review: NOT STARTED")
print("- master/machine specifications: still empty")
print("- git diff whitespace check: pass")
