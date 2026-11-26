# ANALYSIS ROADMAP
## Northstar Industrial Components Ltd. — 20–28 Minute Expert Demonstration

---

## Setup (before recording)

Upload these four files to Google Colab:
- `general_ledger.csv`
- `monthly_financials.csv`
- `accounts_receivable_aging.csv`
- `management_adjustments.csv`

Open `northstar_due_diligence.ipynb` in Colab.

---

## Phase 1 — Data Loading and Initial Inspection
**Time: 3–4 minutes**

**Objective:** Load all four datasets. Establish the company's financial baseline.

| Step | Action | Time |
|------|--------|------|
| 1.1 | Import pandas, numpy, load 4 CSVs (note: `dtype={'Account_Code': str}` on GL) | 1 min |
| 1.2 | Print row counts | 30 sec |
| 1.3 | Print 2-year P&L summary (Revenue, GP, EBITDA, Net Income) | 1 min |
| Commentary | "Revenue is ~$19M growing to ~$21M. EBITDA margins around 15%. We have 24 months of data across 4 datasets. EBITDA is reported before D&A — that matters for how we evaluate the management adjustments." | 1 min |

**Expected outputs:**
- 4 datasets loaded
- P&L shows 2024 and 2025 side by side
- Two-year growth clearly visible

---

## Phase 2 — Revenue and Transaction Investigation
**Time: 6–7 minutes**

**Objective:** Reconcile GL revenue with management accounts. Identify the cutoff issue. Detect duplicated transactions.

| Step | Action | Time |
|------|--------|------|
| 2.1 | Group GL revenue (account 4010) by **posting** year | 1 min |
| 2.2 | Group MF revenue by year. Build reconciliation table | 30 sec |
| 2.3 | Explain F1 variance: 2024 GL is **below** MF by $148,500; 2025 GL is **above** MF by same | 1 min |
| 2.4 | Filter GL: revenue invoices with 2024 transaction date, 2025 posting date | 30 sec |
| 2.5 | Show INV2024-12-C002 (Cascade Engineering) posted 2025-01-08 | 30 sec |
| 2.6 | Commentary: "This Dec-28 invoice hit the GL on January 8th. Management accounts are on accrual — they caught it. The GL missed it. $148,500 of 2024 revenue is sitting in 2025. This is a timing difference, not a loss." | 1 min |
| 2.7 | Group GL debits by (Document_Reference, Account_Code, Debit) — flag count > 1 | 30 sec |
| 2.8 | Drill into PO-2024-0892. Show 4 rows. Total debit $84,600. | 30 sec |
| 2.9 | Commentary: "Same PO, same vendor, same amount, two posting dates in October. That's $84,600 debited for a single $42,300 service. Expense overstatement is $42,300 — one posting is real, one is the duplicate. Management has proposed an add-back for this — we'll evaluate it in Phase 3." | 1 min |

**Findings confirmed:** F1 (revenue cutoff $148,500), F5 (duplicate $42,300)

---

## Phase 3 — Earnings Quality and Receivables Assessment
**Time: 8–10 minutes**

**Objective:** Evaluate all 2025 management adjustment proposals individually. Test recurrence of restructuring. Assess the most material overdue receivable.

| Step | Action | Time |
|------|--------|------|
| 3.1 | Filter to 2025 adjustments (`adj['Period'] == 2025`, Period is int64) | 30 sec |
| 3.2 | Print management EBITDA bridge: reported → management-adjusted (2025 only) | 1 min |
| 3.3 | ADJ-005 investigation: extract doc ref CONS-ERP-2025 | 30 sec |
| 3.4 | Search GL for CONS-ERP-2025. Result: 0 rows. | 30 sec |
| 3.5 | Show largest SGA charges in GL (CONS-2025-Q4 appears, $55k, different ref) | 30 sec |
| 3.6 | Commentary: "Management claims $95,000 for ERP advisory. Supporting reference doesn't exist in the GL. There IS a consulting payment — but $55k under a different PO. We cannot substantiate $95,000. ADJ-005 rejected." | 1 min |
| 3.7 | Filter GL for account 6100 (restructuring). Group by year. | 30 sec |
| 3.8 | Show $95,000 in Nov-2024, $78,000 in Feb-2025 | 30 sec |
| 3.9 | Show ADJ-002 and ADJ-003 both labelled "One-time" | 30 sec |
| 3.10 | Commentary: "Restructuring in two consecutive periods. If the same type of charge recurs within 12 months, it fails the non-recurring test by definition. ADJ-003 ($78,000) rejected." | 1 min |
| 3.11 | Print individual assessment for each 2025 adjustment | 1 min |
| 3.12 | Note on ADJ-006: "Depreciation normalization — EBITDA already excludes D&A by definition. Adding it back would double-count the depreciation. Reject regardless of the recurrence label." | 30 sec |
| 3.13 | Print AR aging bucket summary | 30 sec |
| 3.14 | Show IronBridge Works — $312,800, **407 days**, in administration | 30 sec |
| 3.15 | Commentary: "407 days. The customer is in formal administration proceedings. Legal counsel is already engaged. Recovery is highly uncertain. Full impairment recommended. That's a $312,800 reduction in reported AR." | 1 min |

**Findings confirmed:** F2 (IronBridge $312,800), F3 (ADJ-005 $95,000), F4 (restructuring $78,000)

---

## Phase 4 — Findings and Financial Conclusions
**Time: 4–5 minutes**

**Objective:** Calculate defensible EBITDA. Adjust AR. Consolidate all five findings. Present categorised exposures.

| Step | Action | Time |
|------|--------|------|
| 4.1 | Build EBITDA bridge: reported → accepted adj → defensible | 1 min |
| 4.2 | Print: reported $3.16M + accepted $174.5k = defensible $3.33M | 30 sec |
| 4.3 | Calculate adjusted AR: reported $1.20M − impairment $312.8k = adjusted $883.4k | 30 sec |
| 4.4 | Commentary: "The revenue cutoff ($148,500) doesn't reduce AR — that invoice is real and collectible. It's purely a GL period classification issue." | 30 sec |
| 4.5 | Print consolidated findings register (5 findings, categorised by type) | 1 min |
| 4.6 | Print executive summary with all key figures | 30 sec |
| 4.7 | Print 4 open information requests | 30 sec |
| 4.8 | Closing commentary: "Defensible EBITDA comes in at $3.33M versus management's claim of $3.55M — a $215k gap from rejected add-backs. The bigger balance sheet risk is IronBridge at $312.8k. These are the conversations to have before you finalise valuation." | 1 min |

---

## Total time estimate

| Phase | Duration |
|-------|---------|
| Phase 1 — Loading | 3–4 min |
| Phase 2 — Revenue & transactions | 6–7 min |
| Phase 3 — QoE & receivables | 8–10 min |
| Phase 4 — Conclusions | 4–5 min |
| **Total** | **21–26 min** |

Buffer to 30-minute maximum: 4–9 minutes. Pause after any finding for a deeper explanation without exceeding the limit.

---

## Key figures to have ready

| Metric | Value |
|--------|-------|
| Revenue 2024 | $18,979,748 |
| Revenue 2025 | $21,068,722 |
| EBITDA 2025 (reported) | $3,157,374 |
| Management add-backs 2025 | $389,500 |
| Management-adjusted EBITDA 2025 | $3,546,874 |
| Accepted adjustments (ADJ-004, 007, 009) | $174,500 |
| Rejected adjustments (ADJ-003, 005, 006) | $215,000 |
| **Defensible EBITDA 2025** | **$3,331,874** |
| Reported AR | $1,196,200 |
| IronBridge impairment | $312,800 |
| **Adjusted AR** | **$883,400** |
| IronBridge days overdue | **407** |
| F1 revenue cutoff | $148,500 |
| F5 duplicate overstatement | $42,300 |
