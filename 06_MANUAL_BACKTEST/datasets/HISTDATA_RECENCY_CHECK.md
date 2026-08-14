# HISTDATA RECENCY CHECK — how recent is the free tier, actually?

> **THIS FILE IS A FEASIBILITY FINDING, NOT A DECISION.** It answers one question that
> `D-036` and `D-036a` left unanswered, and it authorises nothing. It does **not** amend
> `D-034`, does **not** move the `D-035` development/holdout boundary, does **not** extend
> the corpus, and does **not** unblock any `PT`. Extending
> `HISTDATA_GBPUSD_M1/` past **2016-06-30** requires a **new owner decision**.

**Checked:** 2026-08-14, ≈ 12:26–12:31 UTC
**Vendor:** HistData.com — the same vendor already declared by `D-036a`
**Instrument / product checked:** GBP/USD, `MetaTrader` format, **M1** (the exact product in the corpus)
**Method:** HTTP GET of four public listing pages + **one** ranged probe of the public
`get.php` endpoint. **No bulk data was retained** — see §5.

---

## 1. THE QUESTION THIS ANSWERS

`D-036` sourced the claim that HistData publishes GBP/USD M1 *"back to 2000"*. It recorded
only the **start** of the vendor's range. Nobody had ever checked the **end** — whether the
free tier stops at some rolling cutoff, lags by months, or gates recent years behind payment.
The corpus stops at **2016-06-30** because that is the `D-035` boundary, **not** because the
vendor stopped there, and that distinction had never been evidenced.

## 2. FINDING — THE FREE TIER IS CURRENT TO WITHIN ABOUT A WEEK

**Answer: yes. 2016H2 through 2025 is available, free, no account, no payment, and the vendor
is current to within ~6 days of this check.**

The GBP/USD M1 index page offers **34 downloads**, and the listing is complete with no holes:

| Block | Granularity | Coverage |
|---|---|---|
| **2000 – 2025** | **one .zip per full year** (26 files) | every year present, none skipped |
| **2026** | **one .zip per month**, January … August (8 files) | the current year, month by month |

Exact text of the newest entry: **`2026 / August - .Zip with Full Month Data`**.

**Recency, stated by the vendor on the page itself:**

> `DataFiles Last Updated at: 2026-08-08 22:45:31`

That is **6 days** before this check. There is **no rolling cutoff and no multi-month
embargo** — the lag is on the order of days, and the current partial month is published.

**The years the owner asked about are all present as ordinary free-year files:**
`2016`, `2017`, `2018`, `2019`, `2020`, `2021`, `2022`, `2023`, `2024`, `2025`.

## 3. ACCESS — NO GATE ON THE DATA ITSELF

The download mechanism is **unchanged from the one `D-036a` used on 2026-08-13**: each
year/month page carries a hidden POST form to `/get.php` with fields
`tk, date, datemonth, platform, timeframe, fxpair`.

A single probe against the **2025** form (the most recent *full year*, and the far end of the
range in question) returned:

```
HTTP/1.1 200 OK
Content-Disposition: attachment; filename=HISTDATA_COM_MT_GBPUSD_M12025.zip
Content-Length: 3604850
Content-Type: application/octet-stream
```

with a valid ZIP local header naming **`DAT_MT_GBPUSD_M1_2025.csv`**. **No login, no account,
no cookie, no referral gate, no payment.** Identical in kind to the 2013–2016 retrieval.

**Paid tiers exist but do not gate the data.** The pages advertise FTP/SFTP access via PayPal
and *"Automatic Updates"* to Google Drive at **$7.00 USD monthly** (MetaTrader 4/5 or Generic
ASCII). These sell **delivery convenience**, not access — the same files are served free by
the `get.php` POST above.

## 4. CAVEATS — READ THESE BEFORE PLANNING AN EXTENSION

1. **⚠ THERE IS NO `2016H2` FILE. THE VENDOR SELLS 2016 ONLY AS A WHOLE YEAR.**
   Confirmed on both the `metatrader` and `ascii` 2016 pages: neither exposes month-level
   links. Past years are **full-year only**; monthly granularity exists **for the current
   year (2026) only**. The corpus's `DAT_MT_GBPUSD_M1_2016H1.csv` is a **local truncation**
   performed on arrival (`D-036a`; `README.md` "Holdout never on disk"), not a vendor product.
   **Any session fetching 2016H2 necessarily pulls the whole 2016 year, holdout included, and
   is bound by the same truncate-on-arrival-or-record-the-breach rule.**
2. **Format is unverified past 2016.** Nothing here inspected a single post-2016 bar. The
   column layout, the fixed UTC−5/no-DST clock, the structurally-zero volume field and the
   week-open convention are **2013–2016 facts** (`D-036a`). They are *expected* to hold —
   same vendor, same product code — but that is an assumption, and it must be **re-measured
   per `D-034`'s mandatory depth/clock probe** before any post-2016 bar is read by a test.
3. **The 2026 file is partial and moves.** August 2026 is an in-progress month; its contents
   change between fetches. Any use of the current year must pin a retrieval timestamp and a
   SHA-256, and must not be treated as stable.
4. **No terms-of-service page was located.** The site footer offers only *Cookies and
   Privacy*, *Data Privacy Policy*, *Support* and *About Us* — no ToS or licence link was
   present on the pages fetched. **Redistribution/licensing therefore remains an open
   question**, not a cleared one. It does not affect local use, and the corpus is gitignored
   in any case.
5. **`00_SYSTEM/EXTERNAL_REFERENCE/VENDOR_TIMEFRAME_AVAILABILITY.md` does not exist** in this
   repository, and never has. This file was placed in `datasets/` instead, next to the
   `README.md` that actually holds HistData provenance under `D-036a`.

## 5. WHAT WAS AND WAS NOT DOWNLOADED

**No corpus data was added, extracted, or read.** The single `get.php` probe was issued as a
1 KB HTTP range request; **the server ignored `Range` and returned the full 3,604,850-byte
2025 zip**. It was written to a session scratchpad outside the repository, its first 64 bytes
inspected to confirm the ZIP magic and inner filename, and then **deleted unopened** — never
unzipped, never parsed, never placed under `datasets/`. `HISTDATA_GBPUSD_M1/` is byte-for-byte
unchanged by this check, and the `D-035` holdout was never on disk.

Request volume: **6 HTTP requests total**, spaced ≥ 3 s apart, ordinary browser user-agent.

## 6. PAGES CHECKED — CITATIONS AND HASHES

| # | URL | Bytes | SHA-256 of body as fetched |
|---|---|---|---|
| 1 | `https://www.histdata.com/download-free-forex-historical-data/?/metatrader/1-minute-bar-quotes/gbpusd` | 38,551 | `7408772d15c94a9f853c37bf1129efdae0f285c090853624fde32aa20199c29f` |
| 2 | `…/?/metatrader/1-minute-bar-quotes/gbpusd/2025` | 31,526 | `83a73f6ee7c5417194d12cdf73b1f79e8460d145130df247655517dc7d8304c8` |
| 3 | `…/?/metatrader/1-minute-bar-quotes/gbpusd/2016` | 31,526 | `0f1739c0967ae1e247cc72e3e7406278c56827521549a320068ee5d3acaa52f7` |
| 4 | `…/?/metatrader/1-minute-bar-quotes/gbpusd/2026/8` | 31,536 | `db819cbdeaacae12d85d737fb3e178e9aa5732be489bebda4548ac0ea6abfa62` |
| 5 | `…/?/ascii/1-minute-bar-quotes/gbpusd/2016` | — | `06aaa62b3f1b84146a9fafcc05a4ee978cd5ca4d258a46d5b54ff9a64bc7ad5e` |

> **⚠ THESE HASHES ARE NOT REPRODUCIBLE, AND THAT IS A PROPERTY OF THE PAGES, NOT AN ERROR.**
> Each page embeds a **per-request `tk` token** in the download form and third-party ad-tag
> JavaScript. **A re-fetch will produce a different SHA-256 even if the data listing is
> identical.** These are single-fetch fingerprints of what was read on 2026-08-14 — they
> establish *what this session saw*, and they are **not** integrity checks for a later
> session. The reproducible claims are the listing contents and the quoted strings above.
> Per-file SHA-256 for actual downloads is a separate mechanism and lives in
> `HISTDATA_GBPUSD_M1/raw/SHA256SUMS.txt`.

## 7. WHAT IS STILL OWED IF THE OWNER EXTENDS THE CORPUS

Out of scope here, listed so it is not mistaken for cleared:

- A **new owner decision**, cited alongside `D-036a`, declaring the extended span.
- **`D-035`'s development/holdout boundary is final and does not auto-extend.** New data does
  not become development data by arriving.
- The **truncate-on-arrival** discipline for any file straddling the boundary (§4.1).
- A **re-measured clock/format probe** on post-2016 bars before any test reads one (§4.2).
- The `2014-06-01` hole and the `D-034` cross-vendor level caveat are unaffected and still stand.

---

**Related:** `D-034`, `D-035`, `D-036`, `D-036a` in `00_SYSTEM/DECISIONS.md`;
`README.md` (this directory); `HISTDATA_GBPUSD_M1/QA_REPORT.txt`.
