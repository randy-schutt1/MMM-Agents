#!/usr/bin/env python3
"""
Structural health check for the MMM-MASTERY research repository.

SCOPE — deliberately narrow.

This script checks that the project's *scaffolding* is intact: required files and
directories exist, the review/progress bookkeeping is present, no obvious secret or
source-video is tracked by Git, and the source manifest has the expected shape.

It does NOT inspect, interpret, grade, or judge any Market Maker Method content.
It cannot tell whether a rule is correct, whether a backtest was honest, or whether
a lesson deserves to pass. Those judgements belong to the Independent Reviewer
Agent, working from source evidence — not to a script.

Usage:
    python3 scripts/validate_project.py
    python3 scripts/validate_project.py --quiet     # only problems
    python3 scripts/validate_project.py --strict    # warnings become failures

Exit codes:
    0  all checks passed (warnings may be present unless --strict)
    1  one or more failures
    2  could not run (e.g. repository root not found)
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

# --------------------------------------------------------------------------
# Expectations
# --------------------------------------------------------------------------

REQUIRED_ROOT_FILES = [
    "README.md",
    "LOG.md",
    "CHANGELOG.md",
    ".gitignore",
    "MMM_MASTER_STUDENT_RESEARCH_AGENT.md",
    "MMM_INDEPENDENT_REVIEWER_TEACHER_AGENT.md",
]

REQUIRED_DIRS = [
    "00_SYSTEM",
    "00_SYSTEM/TEMPLATES",
    "01_SOURCE_VIDEOS",
    "02_TRANSCRIPTS",
    "03_LESSON_NOTES",
    "04_SCREENSHOTS",
    "05_HOMEWORK",
    "06_MANUAL_BACKTEST",
    "06_MANUAL_BACKTEST/cumulative",
    "06_MANUAL_BACKTEST/datasets",
    "07_MASTERY_REPORTS",
    "08_CONCEPT_LIBRARY",
    "09_CHART_EXAMPLES",
    "09_CHART_EXAMPLES/positive",
    "09_CHART_EXAMPLES/negative",
    "09_CHART_EXAMPLES/borderline",
    "09_CHART_EXAMPLES/unresolved",
    "10_AMBIGUITIES",
    "11_CONTRADICTIONS",
    "12_MASTER_SPEC",
    "13_MACHINE_SPEC",
    "14_PINE",
    "15_AUTOMATED_BACKTEST",
    "16_FORWARD_TEST",
    "17_EXECUTION_ROBOT",
    "18_REVIEW",
    "scripts",
]

REQUIRED_SYSTEM_FILES = [
    "00_SYSTEM/AGENT_ROLE.md",
    "00_SYSTEM/STUDY_PROTOCOL.md",
    "00_SYSTEM/MASTERY_STANDARD.md",
    "00_SYSTEM/COURSE_PROGRESS.md",
    "00_SYSTEM/FILE_NAMING_STANDARD.md",
    "00_SYSTEM/DECISIONS.md",
    "00_SYSTEM/SOURCE_MANIFEST.md",
    "00_SYSTEM/REVIEW_PROTOCOL.md",
    "00_SYSTEM/REMEDIATION_PROTOCOL.md",
    "00_SYSTEM/SOURCE_INGESTION_PROTOCOL.md",
    "00_SYSTEM/SETUP_ISSUES.md",
    "00_SYSTEM/SESSION_START.md",
    "00_SYSTEM/SESSION_CLOSE.md",
    "00_SYSTEM/STUDENT_SESSION_PROMPT.md",
    "00_SYSTEM/REVIEWER_SESSION_PROMPT.md",
    "00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md",
]

REQUIRED_TEMPLATES = [
    "TRANSCRIPT_TEMPLATE.md",
    "SOURCE_NOTES_TEMPLATE.md",
    "INTERPRETATION_TEMPLATE.md",
    "SCREENSHOT_INDEX_TEMPLATE.md",
    "HOMEWORK_TEMPLATE.md",
    "MANUAL_BACKTEST_TEMPLATE.md",
    "MASTERY_REPORT_TEMPLATE.md",
    "REVIEW_TEMPLATE.md",
    "CONCEPT_TEMPLATE.md",
    "CONTRADICTION_TEMPLATE.md",
    "AMBIGUITY_TEMPLATE.md",
]

REQUIRED_REVIEW_FILES = [
    "18_REVIEW/REVIEW_INDEX.md",
    "18_REVIEW/CUMULATIVE_25.md",
    "18_REVIEW/CUMULATIVE_50.md",
    "18_REVIEW/CUMULATIVE_75.md",
    "18_REVIEW/FINAL_COURSE_REVIEW.md",
]

REQUIRED_LOG_FILES = [
    "10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md",
    "11_CONTRADICTIONS/CONTRADICTIONS.md",
    "08_CONCEPT_LIBRARY/CONCEPT_INDEX.md",
]

# Directories that must carry a README explaining their contract.
README_DIRS = [d for d in REQUIRED_DIRS if "/" not in d and d != "scripts"]

# Video/audio extensions that must never be tracked by Git.
MEDIA_EXTENSIONS = {
    ".mp4", ".m4v", ".mov", ".avi", ".mkv", ".wmv", ".flv", ".webm",
    ".mpg", ".mpeg", ".vob", ".mp3", ".wav", ".m4a", ".aac", ".flac",
}

# Filenames that should never be tracked. Substring match, lowercased.
SECRET_NAME_PATTERNS = [
    ".env", "credentials", "secrets", "id_rsa", ".pem", ".p12", ".pfx",
    ".keystore", "api_key", "apikey", "_token", ".netrc", ".htpasswd",
]
# Allow legitimate documentation that merely mentions these words.
SECRET_NAME_ALLOW = [".env.example", "readme", "template", "protocol", "gitignore"]

# .gitignore entries that must be present for the project's core risks.
REQUIRED_GITIGNORE_PATTERNS = ["01_SOURCE_VIDEOS", "*.mp4", ".env", "secrets/", "credentials/"]

MAX_TRACKED_FILE_MB = 25

# --------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------


class Report:
    def __init__(self, quiet: bool = False, strict: bool = False) -> None:
        self.quiet = quiet
        self.strict = strict
        self.passes: list[str] = []
        self.warnings: list[str] = []
        self.failures: list[str] = []

    def ok(self, msg: str) -> None:
        self.passes.append(msg)
        if not self.quiet:
            print(f"  \033[32mPASS\033[0m  {msg}")

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)
        print(f"  \033[33mWARN\033[0m  {msg}")

    def fail(self, msg: str) -> None:
        self.failures.append(msg)
        print(f"  \033[31mFAIL\033[0m  {msg}")

    def section(self, title: str) -> None:
        if not self.quiet:
            print(f"\n\033[1m{title}\033[0m")

    def summary(self) -> int:
        print("\n" + "=" * 70)
        print(
            f"  {len(self.passes)} passed   "
            f"{len(self.warnings)} warnings   "
            f"{len(self.failures)} failures"
        )
        print("=" * 70)

        if self.failures:
            print("\nFailures:")
            for f in self.failures:
                print(f"  - {f}")
        if self.warnings and self.quiet:
            print("\nWarnings:")
            for w in self.warnings:
                print(f"  - {w}")

        if self.failures:
            print("\nStructural validation FAILED.")
            return 1
        if self.strict and self.warnings:
            print("\nStructural validation FAILED (--strict: warnings are failures).")
            return 1

        print("\nStructural validation passed.")
        print(
            "Note: this script checks structure only. It makes no judgement about "
            "methodology,\n      evidence quality, or lesson mastery — that is the "
            "Reviewer Agent's role."
        )
        return 0


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------


def find_repo_root() -> Path | None:
    """Repository root = the directory containing both governing files."""
    here = Path(__file__).resolve().parent
    for candidate in [here.parent, *here.parents]:
        if (candidate / "MMM_MASTER_STUDENT_RESEARCH_AGENT.md").exists():
            return candidate
    return None


def git_tracked_files(root: Path) -> list[str] | None:
    try:
        out = subprocess.run(
            ["git", "-C", str(root), "ls-files"],
            capture_output=True, text=True, timeout=30, check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    if out.returncode != 0:
        return None
    return [line for line in out.stdout.splitlines() if line.strip()]


# --------------------------------------------------------------------------
# Checks
# --------------------------------------------------------------------------


def check_structure(root: Path, r: Report) -> None:
    r.section("Directory structure")
    for d in REQUIRED_DIRS:
        (r.ok if (root / d).is_dir() else r.fail)(f"directory {d}/")

    r.section("Root files")
    for f in REQUIRED_ROOT_FILES:
        (r.ok if (root / f).is_file() else r.fail)(f"file {f}")

    r.section("System files")
    for f in REQUIRED_SYSTEM_FILES:
        (r.ok if (root / f).is_file() else r.fail)(f"file {f}")

    r.section("Templates")
    for t in REQUIRED_TEMPLATES:
        p = root / "00_SYSTEM" / "TEMPLATES" / t
        (r.ok if p.is_file() else r.fail)(f"template {t}")

    r.section("Review infrastructure")
    for f in REQUIRED_REVIEW_FILES:
        (r.ok if (root / f).is_file() else r.fail)(f"file {f}")

    r.section("Accumulating logs")
    for f in REQUIRED_LOG_FILES:
        (r.ok if (root / f).is_file() else r.fail)(f"file {f}")

    r.section("Directory documentation")
    for d in README_DIRS:
        p = root / d / "README.md"
        (r.ok if p.is_file() else r.warn)(f"{d}/README.md")


def check_empty_files(root: Path, r: Report) -> None:
    """A required file that exists but is empty is worse than a missing one."""
    r.section("File contents present")
    required = REQUIRED_ROOT_FILES + REQUIRED_SYSTEM_FILES + REQUIRED_REVIEW_FILES + REQUIRED_LOG_FILES
    empties = [
        f for f in required
        if (root / f).is_file() and (root / f).stat().st_size < 50
    ]
    if empties:
        for f in empties:
            r.fail(f"{f} exists but is effectively empty")
    else:
        r.ok("no required file is empty")


def check_progress_and_manifest(root: Path, r: Report) -> None:
    r.section("Progress and manifest structure")

    progress = root / "00_SYSTEM" / "COURSE_PROGRESS.md"
    if progress.is_file():
        text = progress.read_text(encoding="utf-8", errors="replace")
        needed = ["Source Verified", "Transcript", "Manual Backtest",
                  "Student Mastery", "Reviewer", "Final Status"]
        missing = [c for c in needed if c not in text]
        if missing:
            r.fail(f"COURSE_PROGRESS.md is missing columns: {', '.join(missing)}")
        else:
            r.ok("COURSE_PROGRESS.md has the required columns")

    manifest = root / "00_SYSTEM" / "SOURCE_MANIFEST.md"
    if manifest.is_file():
        text = manifest.read_text(encoding="utf-8", errors="replace")
        needed = ["Video ID", "SHA-256", "Processing Status", "Ordering Confidence"]
        missing = [c for c in needed if c not in text]
        if missing:
            r.fail(f"SOURCE_MANIFEST.md is missing fields: {', '.join(missing)}")
        else:
            r.ok("SOURCE_MANIFEST.md has the required fields")

    index = root / "18_REVIEW" / "REVIEW_INDEX.md"
    if index.is_file():
        text = index.read_text(encoding="utf-8", errors="replace")
        codes = re.findall(r"\bE(\d{2})\b", text)
        if len({c for c in codes}) >= 20:
            r.ok("REVIEW_INDEX.md carries the full E01–E20 error taxonomy")
        else:
            r.warn("REVIEW_INDEX.md does not list the full E01–E20 error taxonomy")


def check_lesson_artifact_consistency(root: Path, r: Report) -> None:
    """
    For any lesson that has been started, flag obviously missing companions.
    Silent when no lesson exists yet.
    """
    r.section("Lesson artifact consistency")

    lesson_re = re.compile(r"^V(\d{2})$")
    started = sorted(
        {
            p.name
            for base in ("02_TRANSCRIPTS", "04_SCREENSHOTS", "05_HOMEWORK",
                         "06_MANUAL_BACKTEST", "18_REVIEW")
            for p in (root / base).iterdir()
            if (root / base).is_dir() and p.is_dir() and lesson_re.match(p.name)
        }
    )

    if not started:
        r.ok("no lessons started yet — nothing to cross-check")
        return

    for vid in started:
        transcript = root / "02_TRANSCRIPTS" / vid / f"{vid}_TRANSCRIPT.md"
        if not transcript.is_file():
            r.warn(f"{vid}: no transcript at {transcript.relative_to(root)}")

        notes = root / "03_LESSON_NOTES" / f"{vid}_SOURCE_NOTES.md"
        interp = root / "03_LESSON_NOTES" / f"{vid}_INTERPRETATION.md"
        if notes.is_file() and not interp.is_file():
            r.warn(f"{vid}: source notes exist but no separate interpretation file")

        shots = root / "04_SCREENSHOTS" / vid
        if shots.is_dir():
            images = [p for p in shots.iterdir() if p.suffix.lower() in {".png", ".jpg", ".jpeg"}]
            if images and not (shots / "INDEX.md").is_file():
                r.warn(f"{vid}: {len(images)} screenshot(s) but no INDEX.md — unindexed images are not evidence")

        mastery = root / "07_MASTERY_REPORTS" / f"{vid}_MASTERY_REPORT.md"
        reviews = root / "18_REVIEW" / vid
        if reviews.is_dir() and any(reviews.glob(f"{vid}_REVIEW_R*.md")) and not mastery.is_file():
            r.warn(f"{vid}: review exists but no mastery report")

    r.ok(f"cross-checked {len(started)} started lesson(s)")


def check_backtest_evidence_gate(root: Path, r: Report) -> None:
    """
    Enforce the D-026 / D-027 hard gate.

    If any BT_*.md observation exists, the baseline and period pre-registration
    decisions must exist too, and each observation must carry its own §0
    pre-registration and result classification.

    Silent-pass when no observation exists yet — the gate is not a burden until
    the first backtest is written.
    """
    r.section("Backtest evidence gate (D-026 / D-027)")

    bt_files = sorted((root / "06_MANUAL_BACKTEST").rglob("BT_*.md")) if (root / "06_MANUAL_BACKTEST").is_dir() else []

    if not bt_files:
        r.ok("no backtest observations yet — gate not engaged")
        return

    decisions = root / "00_SYSTEM" / "DECISIONS.md"
    dtext = decisions.read_text(encoding="utf-8", errors="replace") if decisions.is_file() else ""

    if "D-026" in dtext and "D-027" in dtext:
        r.ok("D-026 and D-027 present in DECISIONS.md")
    else:
        r.fail("BT_ observations exist but D-026/D-027 are missing from DECISIONS.md — "
               "baseline and period pre-registration are required BEFORE any observation")

    # The concrete boundaries must have been decided, not left as OWED.
    if "OWED NOW" in dtext:
        r.fail("BT_ observations exist while DECISIONS.md still lists baseline/holdout "
               "parameters as 'OWED NOW' — decide and record them before testing")
    else:
        r.ok("no outstanding 'OWED NOW' backtest decisions")

    missing_pre, missing_class, bare_rate = [], [], []
    rate_re = re.compile(r"\b\d{1,3}(?:\.\d+)?\s?%")
    for f in bt_files:
        t = f.read_text(encoding="utf-8", errors="replace")
        rel = f.relative_to(root)
        if "PRE-REGISTRATION" not in t.upper():
            missing_pre.append(str(rel))
        if not any(k in t for k in ("DESCRIPTIVE", "EVIDENTIAL", "INVALID")):
            missing_class.append(str(rel))
        # a percentage with no interval/baseline/insufficiency label nearby
        if rate_re.search(t) and not any(
            k in t.upper() for k in ("INTERVAL", "BASELINE", "SAMPLE INSUFFICIENT")
        ):
            bare_rate.append(str(rel))

    for label, bucket, msg in (
        ("pre-registration", missing_pre, "has no §0 PRE-REGISTRATION block"),
        ("classification", missing_class, "has no DESCRIPTIVE/EVIDENTIAL/INVALID classification"),
        ("bare rate", bare_rate, "quotes a percentage with no interval, baseline, or insufficiency label"),
    ):
        if bucket:
            for f in bucket[:5]:
                r.fail(f"{f} {msg}")
        else:
            r.ok(f"all {len(bt_files)} observation(s) carry a {label}")


def check_git_hygiene(root: Path, r: Report) -> None:
    r.section("Git hygiene")

    tracked = git_tracked_files(root)
    if tracked is None:
        r.warn("could not read Git index (not a repo, or git unavailable) — skipping tracked-file checks")
        return

    r.ok(f"Git index readable ({len(tracked)} tracked files)")

    media = [f for f in tracked if Path(f).suffix.lower() in MEDIA_EXTENSIONS]
    if media:
        for f in media[:10]:
            r.fail(f"source media is tracked by Git: {f}")
    else:
        r.ok("no video/audio files tracked by Git")

    suspicious = []
    for f in tracked:
        low = f.lower()
        if any(a in low for a in SECRET_NAME_ALLOW):
            continue
        if any(p in low for p in SECRET_NAME_PATTERNS):
            suspicious.append(f)
    if suspicious:
        for f in suspicious[:10]:
            r.fail(f"possible secret tracked by Git: {f}")
    else:
        r.ok("no obviously secret-named files tracked by Git")

    large = []
    for f in tracked:
        p = root / f
        if p.is_file() and p.stat().st_size > MAX_TRACKED_FILE_MB * 1024 * 1024:
            large.append((f, p.stat().st_size / 1024 / 1024))
    if large:
        for f, mb in large[:10]:
            r.warn(f"large tracked file ({mb:.1f} MB): {f}")
    else:
        r.ok(f"no tracked file exceeds {MAX_TRACKED_FILE_MB} MB")

    gitignore = root / ".gitignore"
    if gitignore.is_file():
        text = gitignore.read_text(encoding="utf-8", errors="replace")
        missing = [p for p in REQUIRED_GITIGNORE_PATTERNS if p not in text]
        if missing:
            r.fail(f".gitignore is missing protections for: {', '.join(missing)}")
        else:
            r.ok(".gitignore covers source media and secrets")


def check_source_videos_dir(root: Path, r: Report) -> None:
    r.section("Source video directory")
    d = root / "01_SOURCE_VIDEOS"
    if not d.is_dir():
        return
    # .DS_Store is Finder metadata, not a generated study artifact. It is gitignored,
    # it reappears whenever anyone opens this folder in Finder, and warning about it
    # trains the reader to ignore this check. The check exists to catch transcripts,
    # JSON and screenshots being written into the source-media directory.
    strays = [
        p.name for p in d.iterdir()
        if p.is_file() and p.name not in {"README.md", ".gitkeep", ".DS_Store"}
        and p.suffix.lower() not in MEDIA_EXTENSIONS
    ]
    if strays:
        r.warn(f"non-media files in 01_SOURCE_VIDEOS/ (generated artifacts do not belong here): {', '.join(strays[:5])}")
    else:
        r.ok("01_SOURCE_VIDEOS/ holds no generated artifacts")


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Structural health check for the MMM-MASTERY repository."
    )
    ap.add_argument("--quiet", action="store_true", help="only show problems")
    ap.add_argument("--strict", action="store_true", help="treat warnings as failures")
    args = ap.parse_args()

    root = find_repo_root()
    if root is None:
        print("ERROR: could not locate the repository root "
              "(no MMM_MASTER_STUDENT_RESEARCH_AGENT.md found above scripts/).",
              file=sys.stderr)
        return 2

    print("=" * 70)
    print("  MMM-MASTERY — STRUCTURAL VALIDATION")
    print(f"  {root}")
    print("=" * 70)

    r = Report(quiet=args.quiet, strict=args.strict)

    check_structure(root, r)
    check_empty_files(root, r)
    check_progress_and_manifest(root, r)
    check_lesson_artifact_consistency(root, r)
    check_source_videos_dir(root, r)
    check_backtest_evidence_gate(root, r)
    check_git_hygiene(root, r)

    return r.summary()


if __name__ == "__main__":
    sys.exit(main())
