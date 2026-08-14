#!/usr/bin/env python3
"""Structural and hindsight-control validation for the practical exam."""

import csv
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    errors=[]; checks={}
    summary=json.loads((ROOT/"VALIDATION_SUMMARY.json").read_text())
    student=(ROOT/"STUDENT_PRACTICAL_PACKET.md").read_text()
    key=(ROOT/"INSTRUCTOR_ANSWER_KEY.md").read_text()
    student_ids=re.findall(r"^## ([A-G]\d{2}) —",student,re.M)
    key_ids=re.findall(r"^## ([A-G]\d{2}) —",key,re.M)
    checks["student_cases"]=len(student_ids); checks["key_cases"]=len(key_ids)
    if len(student_ids)!=60 or len(set(student_ids))!=60: errors.append("Student packet must have 60 unique cases")
    if student_ids!=key_ids: errors.append("Student/key case order mismatch")
    if "Correct answer" in student: errors.append("Student packet leaks a Correct answer row")
    if "sealed_reveals" in student or "24H_REVEAL" in student: errors.append("Student packet leaks reveal paths")

    charts=sorted((ROOT/"assets/charts").glob("CH_*_visible_only.png"))
    csvs=sorted((ROOT/"assets/visible_only_csv").glob("CH_*_visible_only.csv"))
    cards=sorted((ROOT/"assets/source_cards").glob("SRC*.png"))
    checks.update(charts=len(charts),csvs=len(csvs),source_cards=len(cards))
    if len(charts)!=52 or len(csvs)!=52 or len(cards)!=8: errors.append("Asset count mismatch")

    # Each CSV must be ordered, end at the decision time displayed in the matching chart's key case,
    # and remain strictly inside the development corpus.
    key_blocks={m.group(1):m.group(0) for m in re.finditer(r"^## ([A-G]\d{2}) —.*?(?=^## [A-G]\d{2} —|\Z)",key,re.M|re.S)}
    asset_to_case={}
    for cid,block in key_blocks.items():
        m=re.search(r"\| Asset \| `([^`]+)` \|",student[student.find(f"## {cid} —"):])
        if m: asset_to_case[m.group(1)]=cid
    for cp in csvs:
        aid=cp.name.replace("_visible_only.csv","")
        rows=list(csv.DictReader(cp.open()))
        if not rows: errors.append(f"Empty CSV {cp.name}"); continue
        times=[r["timestamp_utc_minus_5"] for r in rows]
        if times!=sorted(times) or len(times)!=len(set(times)): errors.append(f"Ordering/duplicate failure {cp.name}")
        if times[-1] >= "2016-07-01 00:00": errors.append(f"Holdout contamination {cp.name}")
        cid=asset_to_case.get(aid)
        if not cid: errors.append(f"Unmapped asset {aid}"); continue
        km=re.search(r"\| Exact decision timestamp \| (\d{4}-\d{2}-\d{2} \d{2}:\d{2}) UTC-5 \|",key_blocks[cid])
        if not km or km.group(1)!=times[-1]: errors.append(f"Decision cutoff mismatch {cid}/{aid}")

    prov=(ROOT/"assets/DATA_PROVENANCE.md").read_text()
    for p in [*charts,*csvs,*cards]:
        if sha(p) not in prov: errors.append(f"Missing hash in provenance: {p.name}")

    # Exact requested deliverables and separation.
    required=["README.md","PRACTICAL_EXAM_BLUEPRINT.md","STUDENT_PRACTICAL_PACKET.md","INSTRUCTOR_ANSWER_KEY.md","SCORING_RUBRIC.md","COVERAGE_MATRIX.md","RESULTS_TEMPLATE.md","assets/ASSET_INDEX.md","assets/DATA_PROVENANCE.md","instructor_only/REVEAL_PROTOCOL.md"]
    for rel in required:
        if not (ROOT/rel).exists(): errors.append(f"Missing {rel}")
    checks["sealed_reveals"]=len(list((ROOT/"instructor_only/sealed_reveals").glob("*.png")))
    if checks["sealed_reveals"]!=4: errors.append("Expected four sealed reveals")
    checks["status_balance"]=summary["by_status"]
    checks["videos"]=summary["by_video"]
    if any(v<3 for v in summary["by_video"].values()): errors.append("Every video must map to at least three cases")

    report={"status":"PASS" if not errors else "FAIL","checks":checks,"errors":errors}
    (ROOT/"VALIDATION_REPORT.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))
    raise SystemExit(1 if errors else 0)


if __name__=="__main__": main()
