# `verify_quotes.py` — GENERALISED AND RUN OVER V10–V14 FOR THE FIRST TIME (gap-audit item 180)

```text
DATE:     2026-08-14
BRANCH:   fix/verify-quotes-and-summary-refresh
SCOPE:    ROUTINE TOOLING MAINTENANCE, at owner direction. No content was changed.
STATUS:   ⚠ THE RUN SURFACED CONFIRMED COURSE-CONTENT DISCREPANCIES.
          NONE OF THEM IS FIXED HERE. They are referred, not resolved -- see §4.
RAW LOGS: 05_HOMEWORK/V07/scripts/runs/verify_quotes_V{07,09,10,11,12,13,14}_2026-08-14.txt
          committed verbatim, unedited.
```

---

## 1. WHAT WAS BROKEN

`GAP_AUDIT_2026-08-14.md` item 180 charged that `verify_quotes.py`'s argument parser *"still
accepts only `{V07|V09}`"* and that the tool **had never run against V10, V11, V12, V13 or
V14**. Both are confirmed by reading the code as it stood at `e97e89c`:

- `ARTIFACTS` and `ALLOWLIST` were two dictionaries with exactly two keys each;
- `main()` validated the positional argument with `positional[0] not in ARTIFACTS` and exited
  `usage: verify_quotes.py {V07|V09}` for anything else.

**The V09 R2 "generalisation" reached the docstring and the argument name, not the code.** The
docstring said *"It now takes a lesson identifier"* while the code accepted two hardcoded
strings. This is a **fix recorded as made that never reached the code** — the same class as the
audit's other two findings, and the audit's summary of the cost stands:

> *"An un-run check is how the fifth instance survives."*

## 2. WHAT WAS CHANGED, AND WHAT DELIBERATELY WAS NOT

| Changed | |
|---|---|
| Lesson validation | Now `^V\d\d$` **plus the existence of that lesson's transcript**, not membership of a dict |
| `ARTIFACTS` → `ARTIFACT_OVERRIDES` | V07's and V09's lists are kept **verbatim**, because each is the NAMED set a committed mastery-report claim is about |
| `ARTIFACT_TEMPLATES` + `LESSON_PT` | Every other lesson resolves its artifact set from six documented path shapes plus its own pre-registration. The resolved set is **printed at the head of each run**, so a run's coverage is visible in its own output |
| `ALLOWLIST` lookup | `.get(lesson, {})`. A lesson with no allowlist is not an error; the run **says so explicitly** in its header |

**Not changed:** `MIN_WORDS`, `NEAR_MISS_MIN_WORDS`, `QUOTE_RE`, the two tiers, the four
dispositions, full-fragment allowlist equality, the `in_blockquote` ordering V07 R3 asked to
reverse and V09 R2 refused with reasons. **No matching rule moved.**

**That is verified rather than asserted.** The pre-change script was recovered with
`git show e97e89c:05_HOMEWORK/V07/scripts/verify_quotes.py` and run side by side:

| Lesson | Before | After |
|---|---|---|
| V07 | 353 fragments · 237 matched · 59 allowed · 23 retained · 34 unrelated · **0 FLAGGED** · PASS | **identical** |
| V09 | 316 fragments · 189 matched · 45 allowed · 35 retained · 47 unrelated · **0 FLAGGED** · PASS | **identical** |

⚠ **One pre-existing discrepancy, noted and NOT touched:** the docstring's own claim that
*"The V07 sweep still extracts **338** fragments"* is stale — it extracts **353** today, and did
so before this change too. The corpus grew after that sentence was written. The sentence is
V09 R2's record of what V09 R2 saw and is left as written.

## 3. THE RUN — V10 THROUGH V14, FIRST TIME EVER

| Lesson | Fragments | Matched | Allowed | Retained | Unrelated | **FLAGGED** | Exit |
|---|---:|---:|---:|---:|---:|---:|---|
| V10 | 357 | 249 | **0** | 21 | 35 | **52** | 1 |
| V11 | 331 | 182 | **0** | 15 | 61 | **73** | 1 |
| V12 | 294 | 145 | **0** | 38 | 35 | **76** | 1 |
| V13 | 330 | 195 | **0** | 19 | 66 | **50** | 1 |
| V14 | 245 | 119 | **0** | 10 | 46 | **70** | 1 |
| **Total** | **1,557** | **890** | **0** | **103** | **243** | **321** | — |

### ⚠ 321 IS NOT A DEFECT COUNT, AND MUST NOT BE QUOTED AS ONE

**The `allowed` column is zero for all five lessons because no allowlist has ever been written
for them.** Printed slide text, quotations of `MMM-NOTES`, quotations of a *different* lesson at
that lesson's marker, and quotations of the student's own prose all have nowhere to land, so they
fall through to `FLAG`. This is exactly the state V09 was in at its first run: **that run FLAGGED
46, of which 12 were genuine defects and 34 became allowlist entries.**

Triage of the 321, by tier and by whether the flagged line self-labels its source as printed:

| | cited tier | uncited (near-miss) tier |
|---|---:|---:|
| Line self-labels PRINTED / slide / frame | 93 | 36 |
| Line does **not** | 144 | 48 |

The 93 + 36 are allowlist work, not defects. **The 144 cited-tier flags on lines that do not
declare a printed source are the population that needs adjudication**, and a sample of them is
genuine.

## 4. ⚠ CONFIRMED COURSE-CONTENT DISCREPANCIES — REFERRED, NOT RESOLVED

**These were verified by hand against the lesson's own transcript. They are the `E01`/`E11`
narrative-prose quotation class. NOTHING BELOW HAS BEEN CHANGED**, because a quotation defect in
a lesson artifact is evidentiary and belongs in the normal review / contradiction-and-ambiguity
ledger process, not in a tooling-maintenance commit.

| # | Site | Artifact asserts | Transcript reads |
|---|---|---|---|
| 1 | `03_LESSON_NOTES/V11_SOURCE_NOTES.md:432`, cited `[00:00:38]` | *"two hours a week looking at charts"* | *"I want two hours a week **now** looking at charts"* — a word dropped mid-quotation with no elision |
| 2 | `03_LESSON_NOTES/V11_SOURCE_NOTES.md:325`, cited `[00:14:46]`–`[00:14:59]` | *"**there is** not one flashcard in my collection"* | *"**There are** not one flashcard in my collection"* |
| 3 | `03_LESSON_NOTES/V11_SOURCE_NOTES.md:76`, cited `[00:04:30]`–`[00:04:36]` | *"…**that** you're stepping in front of a moving train"* | *"the old adage you're stepping in front of a moving train"* — the leading token is not in the source |
| 4 | `03_LESSON_NOTES/V14_SOURCE_NOTES.md:83`, cited `[00:27:11]` | *"**the** four majors plus the two commodity crosses"* | *"**of** four majors plus the two commodity crosses"* |

**Sample #4 is the exact defect shape V07 R1 `M3` and V07 R2 `M1` charged**: a real sentence,
tracked verbatim, with one word substituted at the head.

**One further class needs a ruling rather than a correction**, and is listed separately because
calling it a defect would prejudge it: `V14_SOURCE_NOTES.md:144` renders `[00:45:18]` as
*"**Ted**, if you can't make it at 1 a.m."* where the transcript reads *"**10** if you if you
can't make it at 1 a.m."*. That is almost certainly a correct reconstruction of an ASR garble —
but it is **unbracketed**, and this project's convention is that a reconstruction is bracketed
precisely so it stops being an assertion about the source (V07 R3 `N2`).

### What is owed, and by whom

1. **A ruling round over the 144**, lesson by lesson, splitting them into allowlist entries (with
   a written reason each, per the V07/V09 pattern) and genuine `E01` instances.
2. **A ledger entry per genuine instance**, through `REMEDIATION_PROTOCOL.md`, with the
   superseded rendering retained.
3. **Only then** does `verify_quotes.py VNN` exit 0 for V10–V14, and only then may it gate a
   commit for those lessons.

**Until (1) is done, the correct reading of a `FLAG` in these five logs is "an unadjudicated
question", not "a proven misquote" — and the correct reading of the four rows in §4 is that
adjudication will find real ones, because it already has.**
