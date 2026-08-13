#!/usr/bin/env python3
"""Scores the committed V09 comprehension answers against the source, mechanically.

The answers were committed at 97d2c1b BEFORE this file was written. Nothing here
can have been shaped to make an answer come out right.

Checks:
  transcript_contains — the reasoning cites a phrase; it must be IN the transcript
  transcript_absent   — the answer claims something is NOT stated; verify it is not
  arithmetic          — re-derive the number independently
  manual              — a disposition claim, reported for the reviewer, not auto-scored
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
ROOT = os.path.normpath(os.path.join(BASE, "..", ".."))
TRANSCRIPT = os.path.join(ROOT, "02_TRANSCRIPTS", "V09", "V09_TRANSCRIPT.md")
ANSWERS = os.path.join(BASE, "data", "v09_comprehension_ANSWERS.json")

lines = []


def say(s=""):
    print(s)
    lines.append(s)


def transcript_body():
    txt = open(TRANSCRIPT).read().split("# VERBATIM TRANSCRIPT", 1)[1]
    body = "\n".join(l for l in txt.splitlines()
                     if not re.fullmatch(r"\[\d\d:\d\d:\d\d\]", l.strip()))
    return re.sub(r"\s+", " ", body).lower()


def arithmetic(qid):
    if qid == "Q2":
        bal, risk = 12500.0, 12500.0 * 0.02
        after = bal - 4 * risk
        return {"balance": after, "pct": (bal - after) / bal * 100.0}
    if qid == "Q4":
        return {"rr_beginner": 50.0 / 25.0, "rr_ideal_stated": 3.0,
                "rr_ideal_actual": 50.0 / 15.0}
    if qid == "Q5":
        return {"breakeven_2to1": 25.0 / (25.0 + 50.0),
                "breakeven_3to1": 15.0 / (15.0 + 50.0)}
    if qid == "Q9":
        return {"week4": 5000.0 * 1.2 ** 4, "week28": 5000.0 * 1.2 ** 28}
    return {}


def main():
    body = transcript_body()
    ans = json.load(open(ANSWERS))
    say("=" * 78)
    say("V09 COMPREHENSION PROBE — scoring answers committed at 97d2c1b")
    say("=" * 78)
    say(f"transcript body: {len(body.split()):,} words")
    say("")

    right = wrong = manual = 0
    detail = {}
    for qid in sorted(k for k in ans if k.startswith("Q")):
        q = ans[qid]
        say("-" * 78)
        say(f"{qid}. {q['question']}")
        say(f"    ANSWER: {q['answer']}")
        kind = q["check"]
        ok = None
        if kind == "transcript_contains":
            hits = {p: (p.lower() in body) for p in q["expect_any"]}
            ok = any(hits.values())
            for p, h in hits.items():
                say(f"    check   in transcript? {'YES' if h else 'no '}  \"{p}\"")
        elif kind == "transcript_absent":
            hits = {p: (p.lower() in body) for p in q["expect_absent"]}
            ok = not any(hits.values())
            for p, h in hits.items():
                say(f"    check   absent? {'no — FOUND' if h else 'YES'}  \"{p}\"")
        elif kind == "arithmetic":
            got = arithmetic(qid)
            ok = True
            for k, v in q["expect"].items():
                g = got.get(k)
                good = g is not None and abs(g - v) <= max(0.01, abs(v) * 1e-4)
                ok &= good
                say(f"    check   {k}: claimed {v}  re-derived {g:.6g}  "
                    f"{'OK' if good else 'MISMATCH'}")
        else:
            manual += 1
            say(f"    MANUAL — {q.get('expect_note','')}")
            detail[qid] = "MANUAL"
            say("")
            continue
        detail[qid] = "RIGHT" if ok else "WRONG"
        right += bool(ok)
        wrong += (not ok)
        say(f"    ==> {'RIGHT' if ok else 'WRONG'}")
        say("")

    say("=" * 78)
    say(f"SCORE: {right} right, {wrong} wrong, {manual} manual "
        f"({right}/{right+wrong} of auto-scored)")
    say("=" * 78)
    say("")
    say("Reasoning traces are in v09_comprehension_ANSWERS.json and were committed")
    say("before this scorer existed. A wrong answer is analysed in V09_HOMEWORK.md")
    say("and is NOT revised.")

    out = os.path.join(BASE, "data", "comprehension_probe_output.txt")
    with open(out, "w") as fh:
        fh.write("\n".join(lines) + "\n")
    with open(os.path.join(BASE, "data", "comprehension_score.json"), "w") as fh:
        json.dump({"right": right, "wrong": wrong, "manual": manual,
                   "detail": detail}, fh, indent=2)
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
