#!/usr/bin/env python3
"""Validate extrema answers, chart cutoffs, separation, provenance, and coverage."""

import csv
import hashlib
import json
import re
from datetime import datetime
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


def sha(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()


def rows(path):
    out=[]
    for r in csv.DictReader(path.open()):
        out.append((datetime.strptime(r["timestamp_utc_minus_5"],"%Y-%m-%d %H:%M"),float(r["high"]),float(r["low"])))
    return out


def main():
    errors=[]; checks={}
    student=(ROOT/"STUDENT_TEST_PACKET.md").read_text(); key=(ROOT/"INSTRUCTOR_ANSWER_KEY.md").read_text(); prov=(ROOT/"assets/DATA_PROVENANCE.md").read_text()
    sids=re.findall(r"^## ([EIDM]\d{2}) —",student,re.M); kids=re.findall(r"^## ([EIDM]\d{2}) —",key,re.M)
    checks["student_cases"]=len(sids); checks["key_cases"]=len(kids)
    if len(sids)!=46 or len(set(sids))!=46 or sids!=kids: errors.append("Case count/order mismatch")
    if "| HOD | **" in student or "| HOW | **" in student or "Decision/signature answer" in student: errors.append("Student packet leaks key fields")
    decision_png=list((ROOT/"assets/decision_charts").glob("DEC_*.png")); decision_csv=list((ROOT/"assets/decision_csv").glob("DEC_*.csv")); full_png=list((ROOT/"instructor_only/completed_week_reveals").glob("FULL_*.png")); full_csv=list((ROOT/"instructor_only/completed_week_csv").glob("FULL_*.csv"))
    checks.update(decision_charts=len(decision_png),decision_csv=len(decision_csv),completed_week_charts=len(full_png),completed_week_csv=len(full_csv))
    if any(x!=46 for x in checks.values() if isinstance(x,int)): errors.append("Expected 46 cases/assets in each set")

    blocks={m.group(1):m.group(0) for m in re.finditer(r"^## ([EIDM]\d{2}) —.*?(?=^## [EIDM]\d{2} —|\Z)",key,re.M|re.S)}
    starts=set()
    for cid in sids:
        dc=ROOT/f"assets/decision_csv/DEC_{cid}.csv"; fc=ROOT/f"instructor_only/completed_week_csv/FULL_{cid}.csv"
        dr=rows(dc); fr=rows(fc); starts.add(fr[0][0])
        b=blocks[cid]
        dm=re.search(r"\| Target trading day \| (\d{4}-\d{2}-\d{2} \d{2}:\d{2}) through (\d{4}-\d{2}-\d{2} \d{2}:\d{2}) \|",b)
        if not dm: errors.append(f"Missing target window {cid}"); continue
        ds=datetime.strptime(dm.group(1),"%Y-%m-%d %H:%M"); de=datetime.strptime(dm.group(2),"%Y-%m-%d %H:%M")
        if dr[-1][0]!=de: errors.append(f"Decision cutoff mismatch {cid}")
        if fr[-1][0].weekday()!=4 or fr[-1][0].strftime("%H:%M")!="16:45": errors.append(f"Full week cutoff mismatch {cid}")
        target=[r for r in dr if ds<=r[0]<=de]
        hod=max(target,key=lambda r:r[1]); lod=min(target,key=lambda r:r[2]); how=max(fr,key=lambda r:r[1]); low=min(fr,key=lambda r:r[2])
        expected={"HOD":(hod[1],hod[0]),"LOD":(lod[2],lod[0]),"HOW":(how[1],how[0]),"LOW":(low[2],low[0])}
        for label,(price,dt) in expected.items():
            m=re.search(rf"\| {label}.*?\*\*(\d+\.\d{{5}}) at (\d{{4}}-\d{{2}}-\d{{2}} \d{{2}}:\d{{2}})\*\*",b)
            if not m or abs(float(m.group(1))-price)>1e-9 or m.group(2)!=dt.strftime("%Y-%m-%d %H:%M"):
                errors.append(f"Extrema key mismatch {cid} {label}")
        if any(r[0]>=datetime(2016,7,1) for r in fr): errors.append(f"Holdout contamination {cid}")
        for p in (dc,fc,ROOT/f"assets/decision_charts/DEC_{cid}.png",ROOT/f"instructor_only/completed_week_reveals/FULL_{cid}.png"):
            if sha(p) not in prov: errors.append(f"Missing provenance hash {p.name}")

    checks["unique_weeks"]=len(starts)
    if len(starts)!=46: errors.append("Cases do not use 46 unique weeks")
    # Prior suites are excluded by week-start timestamp.
    prior=set()
    for base in (ROOT.parent/"19_STUDENT_TEST_SUITE_V01_V10/assets/visible_only_csv",ROOT.parent/"20_CHART_HEAVY_PRACTICAL_V01_V10/assets/visible_only_csv"):
        for p in base.glob("*.csv"):
            rr=rows(p)
            if rr: prior.add(rr[0][0])
    overlap=starts & prior; checks["prior_week_overlap"]=len(overlap)
    if overlap: errors.append("Historical week overlaps prior suites")
    required=["README.md","TEST_BLUEPRINT.md","STUDENT_TEST_PACKET.md","INSTRUCTOR_ANSWER_KEY.md","SCORING_RUBRIC.md","COVERAGE_MATRIX.md","RESULTS_TEMPLATE.md","assets/ASSET_INDEX.md","assets/DATA_PROVENANCE.md","instructor_only/REVEAL_PROTOCOL.md"]
    for rel in required:
        if not (ROOT/rel).exists(): errors.append(f"Missing {rel}")
    report={"status":"PASS" if not errors else "FAIL","checks":checks,"errors":errors}
    (ROOT/"VALIDATION_REPORT.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2)); raise SystemExit(1 if errors else 0)


if __name__=="__main__": main()
