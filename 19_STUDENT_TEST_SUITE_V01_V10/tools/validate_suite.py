#!/usr/bin/env python3
"""Independent integrity checks for the Videos 1–10 student suite."""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
BUILD_PATH = ROOT / "tools/build_suite.py"


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_builder():
    spec = importlib.util.spec_from_file_location("suite_builder", BUILD_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def main():
    b = load_builder()
    checks = {}

    student = (ROOT / "STUDENT_TEST_PACKET.md").read_text()
    key = (ROOT / "INSTRUCTOR_ANSWER_KEY.md").read_text()
    matrix = (ROOT / "COVERAGE_MATRIX.md").read_text()
    pattern = r"^## ((?:V\d{2}-\d{2}|I\d{2})) —"
    student_ids = re.findall(pattern, student, re.M)
    key_ids = re.findall(pattern, key, re.M)
    matrix_ids = re.findall(r"^\| ((?:V\d{2}-\d{2}|I\d{2})) \|", matrix, re.M)
    expected_ids = [c["case_id"] for c in b.CASES]
    assert student_ids == key_ids == matrix_ids == expected_ids
    assert len(student_ids) == len(set(student_ids)) == 88
    checks["case_id_alignment"] = "88 unique IDs aligned across packet, key, and matrix"

    required_key_rows = [
        "| Correct answer |", "| Evidence-based reasoning |", "| Source citation |",
        "| Expected-answer provenance |", "| Expected sequence of reasoning |",
        "| Valid rejection/invalidation conditions |", "| Ambiguities affecting answer |",
        "| Scoring criteria |", "| Common student errors |", "| Difficulty |",
        "| Lookahead check |",
    ]
    for row in required_key_rows:
        assert key.count(row) == 88, (row, key.count(row))
    assert "| Correct answer |" not in student
    assert "| Evidence-based reasoning |" not in student
    checks["required_fields_and_separation"] = "all key fields present 88 times; answer/reasoning rows absent from student packet"

    video_counts = Counter(c["case_id"][:3] for c in b.CASES if c["case_id"].startswith("V"))
    for i in range(1, 11):
        assert video_counts[f"V{i:02d}"] >= 6
    assert sum(c["case_id"].startswith("I") for c in b.CASES) == 20
    checks["lesson_and_integration_floor"] = {**dict(sorted(video_counts.items())), "integration": 20}

    expected_status = {
        "positive/valid": 34, "negative/lookalike": 22,
        "borderline/insufficient": 21, "neutral": 11,
    }
    actual_status = Counter(b.norm_status(c["status"]) for c in b.CASES)
    assert dict(actual_status) == expected_status
    checks["case_balance"] = expected_status
    by_id = {c["case_id"]: c for c in b.CASES}

    required_primary_dimensions = {
        "Recall", "Recognition", "Discrimination", "Sequence", "Exceptions",
        "Homework application", "Manual backtesting", "Provenance",
        "Ambiguity handling", "Contradiction handling",
    }
    primary_counts = Counter(c["competency"] for c in b.CASES)
    assert required_primary_dimensions <= set(primary_counts)
    checks["ten_mastery_dimensions"] = {d: primary_counts[d] for d in sorted(required_primary_dimensions)}

    difficulty_counts = Counter(c["difficulty"] for c in b.CASES)
    assert set(difficulty_counts) == {"foundational", "intermediate", "advanced", "integration"}
    checks["difficulty_coverage"] = dict(difficulty_counts)

    markup_cases = [c["case_id"] for c in b.CASES if c["markup"] != "N/A"]
    uncertainty_cases = [c["case_id"] for c in b.CASES if b.norm_status(c["status"]) == "borderline/insufficient"]
    calculation_cases = [c["case_id"] for c in b.CASES if c["competency"] == "Calculation" or any(x in c["concepts"].lower() for x in ["risk", "loss sequence", "quantitative"])]
    assert len(markup_cases) >= 12 and len(uncertainty_cases) >= 12 and len(calculation_cases) >= 10
    checks["task_type_floors"] = {"markup": len(markup_cases), "borderline_or_insufficient": len(uncertainty_cases), "calculation_or_quantitative_risk": len(calculation_cases)}

    assert "Valid application/Loser" in by_id["V06-04"]["answer"]
    invalid_winner_ids = ["V01-04", "V04-03", "V07-02", "V10-04", "I02", "I10"]
    assert all(b.norm_status(by_id[x]["status"]) == "negative/lookalike" for x in invalid_winner_ids)
    checks["outcome_application_separation"] = {"valid_but_loses": ["V06-04"], "invalid_but_wins_or_profitable_lookalike": invalid_winner_ids}

    explicit_uncertainty_answers = [c["case_id"] for c in b.CASES if any(x in c["answer"].upper() for x in ["UNRESOLVED", "INSUFFICIENT", "NOT SUPPORTED", "INDETERMINATE", "NO: CANNOT"])]
    assert len(explicit_uncertainty_answers) >= 12
    checks["explicit_uncertainty_answers"] = explicit_uncertainty_answers

    clusters = {
        "weekly_context": {
            "positive/valid": ["V01-02", "V01-03", "I01"],
            "negative/lookalike": ["V01-04", "V03-06", "I02"],
            "borderline/insufficient": ["V01-05", "V02-04", "I03"],
        },
        "v04_sequence": {
            "positive/valid": ["V04-01", "V04-02", "I04"],
            "negative/lookalike": ["V04-03", "V04-04", "I05"],
            "borderline/insufficient": ["V04-05", "V04-06", "I06"],
        },
        "v08_confirmation": {
            "positive/valid": ["V08-01", "V08-02", "I07"],
            "negative/lookalike": ["V08-03", "V08-04", "I08"],
            "borderline/insufficient": ["V08-05", "V08-06", "I17"],
        },
        "v10_safety": {
            "positive/valid": ["V10-02", "V10-09", "I09"],
            "negative/lookalike": ["V10-03", "V10-04", "I10"],
            "borderline/insufficient": ["V10-05", "V10-06", "V10-07"],
        },
    }
    for cluster, groups in clusters.items():
        for expected_class, ids in groups.items():
            assert len(ids) >= {"positive/valid": 3, "negative/lookalike": 3, "borderline/insufficient": 2}[expected_class]
            for case_id in ids:
                assert b.norm_status(by_id[case_id]["status"]) == expected_class, (cluster, case_id)
    checks["recognition_clusters"] = "four clusters meet at least 3 valid, 3 invalid/lookalike, and 2 borderline/insufficient"

    chart_checks = {}
    source_rows = b.load_rows()
    for chart_id, decision_text in b.CHART_SPECS.items():
        csv_path = b.SLICES / f"{chart_id}_visible_only.csv"
        image_path = b.CHARTS / f"{chart_id}_visible_only.png"
        assert csv_path.exists() and image_path.exists()
        rows = list(csv.reader(csv_path.open()))
        assert rows[0] == ["timestamp_utc_minus_5", "open", "high", "low", "close", "volume"]
        stamps = [datetime.strptime(r[0], "%Y-%m-%d %H:%M") for r in rows[1:]]
        decision = datetime.strptime(decision_text, "%Y-%m-%d %H:%M")
        assert stamps == sorted(stamps) and stamps[-1] == decision
        assert max(stamps) < datetime(2016, 7, 1)
        assert stamps[0].weekday() == 6 and stamps[0].hour == 17 and stamps[0].minute == 0
        chart_checks[chart_id] = {"rows": len(stamps), "first": str(stamps[0]), "last": str(stamps[-1])}

    for chart_id in ("CH01", "CH04"):
        decision = datetime.strptime(b.CHART_SPECS[chart_id], "%Y-%m-%d %H:%M")
        eligible = [r for r in source_rows if r[0] <= decision]
        week_i = max(i for i, r in enumerate(eligible) if r[0].weekday() == 6 and r[0].hour == 17 and r[0].minute == 0)
        cut = eligible[week_i:]
        first8 = cut[:32]
        high = max(r[2] for r in first8)
        low = min(r[3] for r in first8)
        breaches = [r for r in cut[32:] if r[2] > high or r[3] < low]
        assert breaches and breaches[0][0] == decision
    checks["chart_boundaries"] = chart_checks
    checks["first_breach_cases"] = "CH01 and CH04 end exactly on the first post-band breach"

    card_checks = {}
    for card_id, source in b.SOURCE_CARDS.items():
        copy = b.CARDS / (card_id + source.suffix.lower())
        assert source.exists() and copy.exists()
        assert digest(source) == digest(copy)
        card_checks[card_id] = digest(copy)
    checks["source_card_identity"] = card_checks

    known_assets = set(b.CHART_SPECS) | set(b.SOURCE_CARDS)
    for c in b.CASES:
        for asset_id in ([] if c["asset"] == "None" else c["asset"].split("+")):
            assert asset_id in known_assets
    checks["asset_resolution"] = "every case asset ID resolves through the generated asset index"

    source_texts = []
    source_files = []
    for path in REPO.rglob("*"):
        if ROOT in path.parents or not path.is_file() or path.suffix.lower() not in {".md", ".txt", ".json", ".csv"}:
            continue
        source_files.append(path)
        source_texts.append(path.read_text(errors="ignore"))
    source_text = "\n".join(source_texts)
    source_names = {p.name for p in source_files}
    citation_ids = set()
    for c in b.CASES:
        for filename in re.findall(r"[A-Za-z0-9_]+\.md", c["citation"]):
            assert filename in source_names, (c["case_id"], filename)
        citation_ids.update(re.findall(r"\b(?:PT-\d{3}|BT_V\d{2}_\d{4}|[ACD]-\d{3})\b", c["citation"]))
    missing_ids = sorted(x for x in citation_ids if x not in source_text)
    assert not missing_ids, missing_ids
    checks["citation_resolution"] = f"all cited filenames and {len(citation_ids)} formal IDs resolve in repository evidence"

    manifest = (REPO / "00_SYSTEM/SOURCE_MANIFEST.md").read_text()
    video_root = REPO / "01_SOURCE_VIDEOS/Forex Bootcamp"
    video_hashes = {}
    for i in range(1, 11):
        vid = f"V{i:02d}"
        row = next(line for line in manifest.splitlines() if line.startswith(f"| {vid} |"))
        cells = [cell.strip() for cell in row.strip("|").split("|")]
        video_path = video_root / cells[5].strip("`")
        expected_hash = cells[6].strip("`")
        actual_hash = digest(video_path)
        assert actual_hash == expected_hash
        video_hashes[vid] = actual_hash
    checks["source_video_hashes"] = video_hashes
    checks["v11_boundary"] = "validator hashes V01–V10 only; no V11 lesson artifact is addressed"

    report = {"status": "PASS", "checks": checks}
    (ROOT / "FINAL_VALIDATION.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
