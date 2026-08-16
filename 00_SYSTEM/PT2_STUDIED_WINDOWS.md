# PT 2 STUDIED WINDOWS — DATA CONTAMINATION LOG

**Created:** 2026-08-15 · **Required by:** `MMM_PT2_INTAKE_AND_ALLOCATION_PLAN.md` §4
**Status:** `ACTIVE` — append-only. Add a row whenever a Pt 2 chart example is examined.

---

## WHY THIS FILE EXISTS

`MMM_PT2` §4 required this log **before video study begins**: every Pt 2 chart example's pair and
date range is recorded, and those windows are marked **EXCLUDED** from any later out-of-sample
claim on the `D-044` 2017–2025 block. *"Cheap now; unrecoverable if skipped."*

**The transcripts have now been read, so the obligation is live.** Reading a transcript that says
*"this is November 20th, 2018 — notice the induction off the PSR"* is a look at an answer inside
data the project intends to test on. That does not invalidate anything; it means those windows can
no longer serve as out-of-sample evidence.

| Block | Range | Status |
|---|---|---|
| `D-035` **holdout** | 2016-07-01 → 2017-12-29 | ✅ **UNTOUCHED AND SEALED.** No Pt 2 example falls in it |
| `D-044` extension | 2017 → 2025 | ⚠️ **PARTIALLY CONTAMINATED** — see the table below |
| X-series (`D-063`) | 2012 | ✅ **Clean** — predates both blocks entirely |

---

## CONTAMINATED WINDOWS — FROM TRANSCRIPT READING, 2026-08-15

Derived from the 18 Pt 2 transcripts. ⚠️ **Years are mostly implicit in speech.** Only
`3. Cycles Lesson 4 [23:06]` ("November 20th, **2018**") and `6. Lesson 2 [04:19]` ("since **2019**,
since the beginning of January") state a year outright. The rest are inferred from surrounding
context and the intake plan's §4 survey, and should be treated as **approximate month/day, probable
year** until frame-checked.

| Source | TS | Pair | Window (inferred) | Confidence |
|---|---|---|---|---|
| 3. Cycles L2 | 12:21, 13:22 | not stated in segment | Nov 9–13, prob. 2018 | year inferred |
| 3. Cycles L3 | 07:44 | not stated | Nov 30 – Dec 3, prob. 2018 | year inferred |
| 3. Cycles L3 | 24:00 | not stated | Dec 7–10, prob. 2018 | year inferred |
| 3. Cycles L3 | 34:09 | not stated | ~Dec 25 (*"market was closed on the 25th"*, "current time") | year inferred |
| 3. Cycles L4 | 10:29 | not stated | Nov 2–5, prob. 2018 | year inferred |
| 3. Cycles L4 | 23:06 | not stated | **Nov 20, 2018** | ✅ explicit |
| 3. Cycles L6 | 18:29 | **Gold / XAU** (ADR ~300–315) | not dated | — |
| 6. 1-on-1 Webinar | 52:51 | not stated | **Feb 18** (*"this was yesterday"* → recording ≈ Feb 19) | year inferred |
| 6. Exclusive Webinar | 26:24 | not stated | Mar 25 | year inferred |
| 6. Exclusive Webinar | 01:04:26 | not stated | Apr 5 | year inferred |
| 6. Lesson 1 | 29:23 | not stated | Oct 29–30, prob. 2018 | year inferred |
| 6. Lesson 2 | 04:19–30:07 | **NZD/USD** | **Jan 7 – Jan 18, 2019** | ✅ explicit year |
| 7. Lesson 1 | 06:10 | **GBP/JPY** | Dec 17, prob. 2018 | year inferred |
| 7. Lesson 1 | 08:12 | **USD/CAD** | Dec 3, prob. 2018 | year inferred |
| 7. Lesson 2 | 06:42 | not stated | Dec 14, prob. 2018 | year inferred |
| 7. Lesson 2 | 11:52 | **GBP/JPY** | the *"700 pip drop"* day | undated in segment |
| 7. Lesson 2 | 30:42 | not stated | Jan 10, prob. 2019 | year inferred |
| 7. Lesson 2 | 39:03 | not stated | Dec 5, prob. 2018 | year inferred |

Also logged from the intake plan's own §4 survey of the video frames (not re-derived here):
EU 15 Feb – 1 Mar 2018 · UJ 30 Jan – 5 Feb 2018 · EU 22 Aug 2018 · GCAD 27–28 Aug 2018 ·
"XU" 10–14 Sep 2018 · GCad 15 Sep 2018 · EU ~4–17 Dec 2018 · GBPJPY 18–29 Jan 2019 ·
GBPUSD 11 Feb – 1 Mar 2019 · GU 2–6 Apr 2019.

## RULING FOR TESTING

**Treat `2018-01-01 → 2019-06-30` as contaminated across all majors.** The individual windows above
are sparse and their years are mostly inferred; carving narrow per-pair exclusions from uncertain
dates would give false precision and risk letting a contaminated window through. A blanket
18-month exclusion is the conservative call and costs little — the `D-044` block runs to 2025.

**Consequences:**

1. No out-of-sample claim may rest on 2018-01-01 → 2019-06-30 for any pair.
2. `D-035`'s holdout (2016-07-01 → 2017-12-29) is **unaffected and stays sealed.** It remains the
   project's one clean shot and should still be spent only on a frozen, complete rule set.
3. The 2012 X-series is contamination-free and can be studied in full detail at no data cost.
4. If Pt 2 **frames** are ever extracted, append every new date encountered to this file at that
   time — the transcripts name far fewer dates than the charts show.

**Status:** ACTIVE — append-only.
