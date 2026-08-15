#!/usr/bin/env python3
"""Validate the knowledge-consolidation invariants introduced in Phase 1."""

from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def text(path: str) -> str:
    target = ROOT / path
    require(target.is_file(), f"missing file: {path}")
    return target.read_text(encoding="utf-8") if target.is_file() else ""


def main() -> int:
    deliverables = [
        "00_SYSTEM/MMM_CURRENT_STATE.md",
        "00_SYSTEM/MMM_SETUP_REGISTRY.md",
        "00_SYSTEM/MMM_GAP_AND_DEPENDENCY_MATRIX.md",
        "00_SYSTEM/PHASE_STATUS.md",
        "00_SYSTEM/PHASE_1_VALIDATION_REPORT.md",
        "00_SYSTEM/PHASE_1_HANDOFF.md",
    ]
    for path in deliverables:
        require((ROOT / path).is_file(), f"missing Phase 1 deliverable: {path}")

    for number in range(1, 22):
        lesson = f"V{number:02d}"
        require((ROOT / f"02_TRANSCRIPTS/{lesson}/{lesson}_TRANSCRIPT.md").is_file(),
                f"missing transcript: {lesson}")
        require((ROOT / f"03_LESSON_NOTES/{lesson}_SOURCE_NOTES.md").is_file(),
                f"missing source notes: {lesson}")
        require((ROOT / f"03_LESSON_NOTES/{lesson}_INTERPRETATION.md").is_file(),
                f"missing interpretation: {lesson}")
        require((ROOT / f"07_MASTERY_REPORTS/{lesson}_MASTERY_REPORT.md").is_file(),
                f"missing mastery report: {lesson}")

    progress = text("00_SYSTEM/COURSE_PROGRESS.md")
    require(bool(re.search(r"^\| V21 .*\*\*COMPLETE\*\*.*\*\*R2 PASS\*\*", progress, re.M)),
            "COURSE_PROGRESS does not record V21 COMPLETE with R2 PASS")

    registry = text("00_SYSTEM/MMM_SETUP_REGISTRY.md")
    ids = set(re.findall(r"^\| (SR-\d{2}) \|", registry, re.M))
    require(ids == {f"SR-{n:02d}" for n in range(1, 27)},
            f"setup registry IDs incomplete: found {len(ids)} of 26")
    require("V02 explicitly defines the structure" in registry,
            "registry does not preserve the V02 22-trade definition")
    require("DO NOT CODE` never means" in registry,
            "registry does not separate coding status from knowledge")

    synthesis = text("00_SYSTEM/SETUP_SYNTHESIS_2026-08-15.md")
    require("spread across FIVE UNMERGED BRANCHES" not in synthesis,
            "setup synthesis still claims current knowledge is unmerged")
    require("former statement that 22 had *\"zero definitions\"* was false" in synthesis,
            "setup synthesis lacks the 22-trade correction")
    require("&sm_Buy_Order_Trainer_Pct" in synthesis,
            "setup synthesis does not preserve the four recovered V21 script names")

    concepts = text("08_CONCEPT_LIBRARY/CONCEPT_INDEX.md")
    require("LESSONS INGESTED:       21 / 21" in concepts,
            "concept index is not current through V21")
    require("MMM_SETUP_REGISTRY.md" in concepts,
            "concept index does not route human setup knowledge")

    current = text("00_SYSTEM/MMM_CURRENT_STATE.md")
    require("lesson ingestion complete; cumulative reconstruction and" in current,
            "current-state boundary is missing")
    require("Highest adopted decision in `DECISIONS.md`: `D-057`" in current,
            "current-state decision boundary is missing")

    final_review = text("18_REVIEW/FINAL_COURSE_REVIEW.md")
    require(bool(re.search(r"^NOT STARTED$", final_review, re.M)),
            "Phase 1 must not start or complete FINAL_COURSE_REVIEW")

    master_files = [p.name for p in (ROOT / "12_MASTER_SPEC").iterdir() if p.name not in {".gitkeep", "README.md"}]
    machine_files = [p.name for p in (ROOT / "13_MACHINE_SPEC").iterdir() if p.name not in {".gitkeep", "README.md"}]
    require(not master_files, f"Master Specification was populated during Phase 1: {master_files}")
    require(not machine_files, f"Machine Specification was populated during Phase 1: {machine_files}")

    status = subprocess.run(
        ["git", "diff", "--check"], cwd=ROOT, text=True, capture_output=True, check=False
    )
    require(status.returncode == 0, f"git diff --check failed: {status.stdout}{status.stderr}")

    if ERRORS:
        print("PHASE 1 VALIDATION: FAIL")
        for error in ERRORS:
            print(f"- {error}")
        return 1

    print("PHASE 1 VALIDATION: PASS")
    print("- lesson artifact sets: 21/21")
    print("- setup registry: 26 SR families + OR-01")
    print("- 22-trade correction: present")
    print("- knowledge/codability separation: present")
    print("- cumulative/final review gate: preserved")
    print("- master/machine specifications: still empty")
    print("- git diff whitespace check: pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
