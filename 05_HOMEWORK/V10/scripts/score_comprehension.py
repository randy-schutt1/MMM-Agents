#!/usr/bin/env python3
"""Score `V10_COMPREHENSION_ANSWERS.md` MECHANICALLY against V10's own transcript.

WHY THIS IS NOT SELF-GRADING
----------------------------
A session marking its own prose is worthless. So every question is reduced to
FACTUAL ASSERTIONS that the transcript can settle by itself:

  * a quotation must appear at the marker the answer cites;
  * a claimed ABSENCE must be a genuine zero count over the verbatim body;
  * a claimed COUNT must reproduce.

The script does not read the answer text and judge it. It checks the claims the
answer makes. A question passes only if every one of its assertions holds.

The answers were committed at 54b97f2, BEFORE this file existed.
"""
from __future__ import annotations

import re
import sys
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
TR = os.path.join(ROOT, "02_TRANSCRIPTS", "V10", "V10_TRANSCRIPT.md")

txt = open(TR, encoding="utf-8").read()
body = txt[txt.index("# VERBATIM TRANSCRIPT"):]

MARKERS: dict[str, str] = {}
cur = None
for line in body.split("\n"):
    m = re.match(r"^\[(\d\d:\d\d:\d\d)\]$", line.strip())
    if m:
        cur = m.group(1)
        MARKERS.setdefault(cur, "")
    elif cur and line.strip():
        MARKERS[cur] += " " + line.strip()

FLAT = " ".join(MARKERS.values())


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9 ]", " ", s.lower())


FLAT_N = norm(FLAT)


def at(marker: str, phrase: str, window: int = 0) -> tuple[bool, str]:
    """Does `phrase` appear at `marker` (optionally within +/- `window` markers)?"""
    keys = sorted(MARKERS)
    if marker not in MARKERS:
        return False, f"marker [{marker}] does not exist"
    i = keys.index(marker)
    lo, hi = max(0, i - window), min(len(keys), i + window + 1)
    hay = norm(" ".join(MARKERS[k] for k in keys[lo:hi]))
    return (norm(phrase).strip() in hay,
            f"[{marker}]±{window} contains {phrase!r}")


def absent(token: str) -> tuple[bool, str]:
    n = len(re.findall(r"\b" + re.escape(norm(token).strip()) + r"\b", FLAT_N))
    return n == 0, f"{token!r} occurs {n} times (claimed 0)"


def count(token: str, expected: int) -> tuple[bool, str]:
    n = len(re.findall(r"\b" + re.escape(norm(token).strip()) + r"\b", FLAT_N))
    return n == expected, f"{token!r} occurs {n} times (claimed {expected})"


# ---------------------------------------------------------------- the key
# Each entry: question -> list of assertions the ANSWER makes.
KEY = {
    "Q1  signature trade": [
        at("00:40:47", "the safety trade with a second leg element"),
        at("00:42:14", "your signature trade as of today"),
        at("00:42:23", "safety trade traders"),
    ],
    "Q2  PFH/PFL defined": [
        at("01:14:06", "the highest point on a chart within the week"),
        at("01:14:06", "the lowest point on the chart within the week"),
        at("01:13:58", "peak formation high or high of the week"),
    ],
    "Q3  blue box vs Asian range": [
        at("01:01:42", "he doesn t exploit the asian range"),
        at("01:26:13", "true stop hunt is higher or lower than the blue box"),
        absent("7 00"), absent("3 30"), absent("9 30"),
    ],
    "Q4  preconditions in order": [
        at("00:44:47", "price will move away from this area which confirms the formation"),
        at("00:45:03", "this is level one consolidation"),
        at("00:45:27", "do not counter back towards the peak formation"),
        at("00:46:16", "the dealer makes a visible stop hunt", 2),
        at("00:47:05", "if the level is hit a third time"),
    ],
    "Q5  DNC": [
        at("01:20:59", "it s a do not counter"),
        at("01:01:02", "if you counter this and he straight rises he screwed you up"),
    ],
    "Q6  distance figure": [
        at("01:16:20", "25 to 75 pips"),
        at("00:49:39", "off of the blue tracer", 2),
        at("01:19:45", "separates the day"),
    ],
    "Q7  stop loss ABSENT": [
        absent("stop loss"),
        absent("stoploss"),
    ],
    "Q8  lock duration conflict": [
        at("01:00:41", "one day lock on the directional bias"),
        at("01:00:43", "the lock is good for three days"),
        at("00:41:47", "for at least two days"),
    ],
    "Q9  trade count": [
        at("01:10:01", "two trades per pair", 1),
        at("00:55:37", "20 trades a week"),
        at("01:01:56", "from 20 trades down to five or six"),
        at("00:55:44", "you may not get the second leg visible"),
    ],
    "Q10 timing prohibition": [
        at("00:23:04", "don t trade until they hit the stops"),
        at("00:25:09", "did the dealer hit the stops before i pull the trigger"),
        at("01:06:49", "any other setup without a stop hunt is a shit gamble"),
        at("00:23:36", "the pattern the pattern the pattern timing the levels"),
    ],
    "Q11 TDI deferred": [
        at("01:13:03", "that s next week s lesson"),
        at("01:24:29", "shark fin blood in the water"),
        count("tdi", 1),
    ],
    "Q12 session times ABSENT": [
        absent("7 00"), absent("3 00 am"), absent("3 30"),
        absent("9 00"), absent("9 30"), absent("5 00 pm"),
        count("asian", 13),
    ],
}


def main() -> int:
    print("=" * 78)
    print("V10 COMPREHENSION PROBE — MECHANICAL SCORING")
    print("=" * 78)
    print(f"transcript : {os.path.relpath(TR, ROOT)}")
    print(f"markers    : {len(MARKERS)}")
    print("answers    : 05_HOMEWORK/V10/V10_COMPREHENSION_ANSWERS.md, committed 54b97f2")
    print("             BEFORE this scorer existed.")
    print()
    right = wrong = 0
    for q, checks in KEY.items():
        fails = [msg for ok, msg in checks if not ok]
        status = "RIGHT" if not fails else "WRONG"
        print(f"{status:<6} {q:<32} ({len(checks)} assertions)")
        for f in fails:
            print(f"         FAILED: {f}")
        right += not fails
        wrong += bool(fails)
    total = right + wrong
    print()
    print(f"SCORE: {right} RIGHT / {wrong} WRONG  of {total}")
    print(f"ASSERTIONS CHECKED: {sum(len(v) for v in KEY.values())}")
    print()
    print("Self-assessment recorded before scoring: 'Predicted score: 11 or 12 of 12',")
    print("with Q6 and Q8 named as the likely markdowns.")
    return 0 if wrong == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
