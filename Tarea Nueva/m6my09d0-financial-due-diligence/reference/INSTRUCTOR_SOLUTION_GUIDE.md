# INSTRUCTOR SOLUTION GUIDE
## Northstar Industrial Components Ltd. — Compact Due Diligence

**CONFIDENTIAL — DO NOT DISTRIBUTE TO PARTICIPANTS**

---

## FINDINGS REGISTER

| ID | Description | Severity | Source Files | Impact (USD) | Category |
|----|-------------|----------|-------------|-------------|---------|
| F1 | Revenue cutoff — Dec 2024 invoice posted Jan 2025 | High | GL + MF | $148,500 | Revenue timing |
| F2 | IronBridge Works — in administration, 407 days overdue | High | AR aging | $312,800 | Balance sheet |
| F3 | ADJ-005 unsupported — no GL evidence for CONS-ERP-2025 | High | Adj + GL | $95,000 | EBITDA |
| F4 | Restructuring in both 2024 and 2025 — not one-time | High | GL + Adj | $78,000 | EBITDA |
| F5 | Duplicate maintenance charge — PO-2024-0892 | Medium | GL | $42,300 | Expense |

**Exposures by category (no double-counting):**
- Revenue timing (period reclassification): $148,500
- Balance sheet — AR impairment: $312,800
- EBITDA rejected add-backs (F3 + F4): $173,000
- Conditional expense correction (F5, pending IR-003): $42,300

---

## FINDING F1 — Revenue Cutoff (High)

**Files:** `general_ledger.csv`, `monthly_financials.csv`

**What happened:** Invoice INV2024-12-C002 (Cascade Engineering, $148,500), dated 28-Dec-2024, was posted to the GL on 2025-01-08. Management accounts correctly include it in December 2024 (accrual basis). The GL does not.

**Key figures:**
- MF Revenue 2024: $18,979,748
- GL Revenue 2024: $18,831,248 → gap of -$148,500 (GL is **below** management accounts)
- MF Revenue 2025: $21,068,722
- GL Revenue 2025: $21,217,222 → gap of +$148,500 (GL is **above** management accounts)

**Direction of variance:** 2024 GL understates; 2025 GL overstates — both by the same amount.

**Detection:**
```python
rev_gl = gl[gl['Account_Code'] == '4010'].copy()
rev_gl['Year'] = rev_gl['Posting_Date'].dt.year
recon = pd.DataFrame({
    'GL': rev_gl.groupby('Year')['Credit'].sum(),
    'MF': mf.groupby('Year')['Revenue'].sum()
})
recon['Variance_GL_minus_MF'] = recon['GL'] - recon['MF']
print(recon)

# Identify the transaction
cutoff = gl[
    (gl['Account_Code'] == '4010') &
    (gl['Transaction_Date'].dt.year == 2024) &
    (gl['Posting_Date'].dt.year == 2025)
]
print(cutoff[['Transaction_Date','Posting_Date','Credit','Counterparty','Document_Reference']])
```

**Expected output:**
- 2024 variance: -$148,500 (GL under-reports vs MF)
- 2025 variance: +$148,500 (GL over-reports vs MF)
- Transaction: INV2024-12-C002, Cascade Engineering, $148,500, posted 2025-01-08

**Treatment:** Period reclassification. Reclassify $148,500 from 2025 to 2024 in the GL. This is a timing difference, not a loss — the invoice is a real, collectible receivable.

---

## FINDING F2 — IronBridge Receivables Impairment (High)

**File:** `accounts_receivable_aging.csv`

**What happened:** Customer C008 (IronBridge Works) has invoice INV2024-0845 outstanding at $312,800, **407 days** overdue. Collection notes state the customer entered administration proceedings in August 2025.

**Detection:**
```python
print(ar.groupby('Aging_Bucket')['Outstanding_Amount'].agg(['count','sum']))

over90 = ar[ar['Aging_Bucket'] == 'Over 90']
print(over90[['Customer_Name','Invoice_Number','Outstanding_Amount',
              'Days_Overdue','Collection_Notes']])

ironbridge = ar[ar['Customer_ID'] == 'C008']
print(ironbridge)
```

**Expected output:** IronBridge Works, $312,800, **407 days**, "in administration proceedings — legal counsel engaged 2025-08"

**Treatment:** Full impairment. Working capital reduction: -$312,800. Requires a bad debt provision if not already recognised.

**Note:** 407 days is the actual value in the CSV. Do not use any other figure.

---

## FINDING F3 — Unsupported EBITDA Adjustment ADJ-005 (High)

**Files:** `management_adjustments.csv`, `general_ledger.csv`

**What happened:** Management proposes adding back $95,000 for "ERP implementation advisory" costs, referencing document CONS-ERP-2025. No GL entry exists under this reference. The actual consulting payment in Dec 2025 uses a different reference (CONS-2025-Q4, $55,000).

**Detection:**
```python
adj5 = adj[adj['Adjustment_ID'] == 'ADJ-005'].iloc[0]
doc_ref = adj5['Supporting_Document_Reference']   # 'CONS-ERP-2025'
print(f"ADJ-005 references: {doc_ref}")

gl_match = gl[gl['Document_Reference'] == doc_ref]
print(f"GL entries found: {len(gl_match)}")   # Expected: 0

# Show what IS in GL for consulting (different reference)
consult = gl[gl['Account_Code'] == '6030'].nlargest(5, 'Debit')
print(consult[['Posting_Date','Debit','Counterparty','Document_Reference']])
```

**Expected output:** 0 GL entries for CONS-ERP-2025

**Treatment:** Reject ADJ-005. EBITDA reduction vs management: -$95,000.

---

## FINDING F4 — Recurring Restructuring (High)

**Files:** `general_ledger.csv`, `management_adjustments.csv`

**What happened:** Restructuring charges appear in both November 2024 ($95,000) and February 2025 ($78,000). Management proposes to add back both as one-time (ADJ-002 and ADJ-003). Two consecutive periods of restructuring cannot be classified as non-recurring.

**Detection:**
```python
restr_gl = gl[gl['Account_Code'] == '6100'].copy()
restr_gl['Year'] = restr_gl['Posting_Date'].dt.year
print(restr_gl.groupby('Year')['Debit'].sum())
print(restr_gl[['Posting_Date','Debit','Description','Document_Reference']])

# Note: Account_Code in adj file is int64 (no dtype override on adj load)
restr_adj = adj[adj['Account_Code'] == 6100]
print(restr_adj[['Adjustment_ID','Period','Amount','Recurrence_Indicator']])
```

**Expected output:**
- GL: 2024 → $95,000; 2025 → $78,000
- Both ADJ-002 and ADJ-003 labelled "One-time"

**Treatment:** Accept ADJ-002 (2024, $95,000 — arguably the first occurrence, affects 2024 QoE only). Reject ADJ-003 (2025, $78,000). EBITDA reduction vs management: -$78,000.

---

## FINDING F5 — Duplicate Transaction (Medium)

**File:** `general_ledger.csv`

**What happened:** PO-2024-0892 (TechServ Maintenance, equipment maintenance, $42,300) was posted twice in October 2024 — same document reference, same account, same amount, two posting dates (Oct-05 and Oct-08). The result is a **$42,300 overstatement** of expenses.

Management proposes ADJ-008 ($42,300) to add this back (accept if confirmed by vendor credit note).

**Common misconception:** The GL shows a total debit of $84,600 (two × $42,300). The **overstatement is $42,300**, not $84,600 — one posting is legitimate; only the duplicate is erroneous.

**Detection:**
```python
gl_debits = gl[gl['Debit'] > 0].copy()
dup_flags = gl_debits.groupby(['Document_Reference','Account_Code','Debit']).size()
dup_flags = dup_flags[dup_flags > 1].reset_index(name='Count')
print(dup_flags)

dup_detail = gl[gl['Document_Reference'] == 'PO-2024-0892'].sort_values('Posting_Date')
print(dup_detail[['Transaction_ID','Transaction_Date','Posting_Date',
                   'Account_Code','Debit','Credit','Counterparty']])
print(f"Total debited: ${dup_detail[dup_detail['Debit']>0]['Debit'].sum():,.0f}")
print("Overstatement: $42,300  (one duplicate posting)")
```

**Expected output:** 4 rows for PO-2024-0892; total debit $84,600; overstatement = $42,300

**Treatment:** Accept ADJ-008 ($42,300) if TechServ credit note is confirmed. Flag as open item (IR-003).

---

## EXPECTED FINANCIAL CONCLUSIONS

### Key figures

| Metric | Value |
|--------|-------|
| Revenue 2024 | $18,979,748 |
| Revenue 2025 | $21,068,722 |
| EBITDA 2024 (reported) | $2,713,401 |
| EBITDA 2025 (reported) | $3,157,374 |
| Management proposed 2025 add-backs | $389,500 |
| Management-adjusted EBITDA 2025 | $3,546,874 |
| Accepted 2025 adjustments | $174,500 |
| Rejected 2025 adjustments | $215,000 |
| **Defensible normalized EBITDA 2025** | **$3,331,874** |
| Reported AR | $1,196,200 |
| Less: IronBridge impairment | -$312,800 |
| **Adjusted AR** | **$883,400** |

### EBITDA bridge (2025 only)

| Item | Amount | Verdict |
|------|--------|---------|
| Reported EBITDA 2025 | $3,157,374 | — |
| ADJ-004 Owner comp normalization | +$120,000 | ACCEPT |
| ADJ-007 Above-market rent | +$36,000 | ACCEPT |
| ADJ-009 FX revaluation loss | +$18,500 | ACCEPT |
| ADJ-003 Restructuring Feb-2025 | +$78,000 | **REJECT** (recurring) |
| ADJ-005 ERP consulting | +$95,000 | **REJECT** (unsupported) |
| ADJ-006 Depreciation normalization | +$42,000 | **REJECT** (D&A double-count) |
| **Defensible EBITDA 2025** | **$3,331,874** | — |

**ADJ-006 reject rationale:** EBITDA by definition excludes Depreciation & Amortization. Any adjustment that adds back a D&A item (acct 6040) to an EBITDA baseline is a double-count. Reject regardless of recurrence label.

**2024 adjustments (ADJ-001, ADJ-002, ADJ-008) are excluded from the 2025 bridge.** They affect 2024 quality of earnings analysis, not the 2025 EBITDA baseline. Filter: `adj[adj['Period'] == 2025]` (Period is int64).

### Open information requests

| IR | Item |
|----|------|
| IR-001 | IronBridge administration status and recovery prospects |
| IR-002 | Supporting invoices for CONS-ERP-2025 (ADJ-005) |
| IR-003 | TechServ credit note for duplicate PO-2024-0892 |
| IR-004 | 2026 restructuring forecast to assess recurrence |

---

## TECHNICAL NOTES FOR INSTRUCTORS

**Account_Code dtype:**
`general_ledger.csv` stores Account_Code as integers. Notebook must load with:
```python
gl = pd.read_csv('general_ledger.csv', dtype={'Account_Code': str}, ...)
```
This enables string comparisons like `gl['Account_Code'] == '4010'`.

**Period dtype:**
`management_adjustments.csv` stores Period as int64 (2024 / 2025).
Filter with `adj['Period'] == 2025` (integer). Using `== '2025'` returns empty DataFrame.

**Account_Code in adjustments file:**
No dtype override is applied to `adj`. Its Account_Code column is int64.
Use integer comparisons: `adj[adj['Account_Code'] == 6100]`.
