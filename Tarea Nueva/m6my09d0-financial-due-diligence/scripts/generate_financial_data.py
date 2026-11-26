"""
Northstar Industrial Components Ltd.
Financial Due Diligence — Compact Edition
Generates 4 CSV input files with 5 engineered findings.
Fixed seed=42 for reproducibility.
"""

import pandas as pd
import numpy as np
import os

SEED = 42
rng = np.random.default_rng(SEED)

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "inputs")
os.makedirs(BASE_DIR, exist_ok=True)

# ─────────────────────────────────────────────
# MONTHLY FINANCIALS
# ─────────────────────────────────────────────
def generate_monthly_financials():
    months = pd.period_range("2024-01", "2025-12", freq="M")

    base_rev_2024 = 1_580_000
    base_rev_2025 = 1_754_400  # ~11% growth

    seasonality = np.array([
        0.82, 0.78, 0.92, 0.95, 1.02, 1.08,
        0.97, 0.94, 1.03, 1.10, 1.07, 1.32
    ])

    rows = []
    for i, m in enumerate(months):
        yr = m.year
        base = base_rev_2024 if yr == 2024 else base_rev_2025
        s = seasonality[m.month - 1]
        noise = 1 + rng.uniform(-0.015, 0.015)
        revenue = round(base * s * noise, 0)

        # F1: Dec 2024 — revenue includes INV2024-12-C003 ($148,500)
        # This is correct on the management P&L (accrual intent)
        # but the GL will show it posted in Jan 2025

        cogs = round(revenue * rng.uniform(0.595, 0.615), 0)
        gross_profit = revenue - cogs
        payroll = round(revenue * rng.uniform(0.148, 0.162), 0)
        rent = 42_000
        sga = round(revenue * rng.uniform(0.055, 0.075), 0)
        da = round(revenue * rng.uniform(0.038, 0.048), 0)

        # Restructuring: Nov 2024 and Feb 2025 (F4 — recurring)
        restructuring = 0
        if m == pd.Period("2024-11", "M"):
            restructuring = 95_000
        elif m == pd.Period("2025-02", "M"):
            restructuring = 78_000

        ebit = gross_profit - payroll - rent - sga - da - restructuring
        interest = round(revenue * 0.009, 0)
        taxes = round(max(ebit - interest, 0) * 0.265, 0)
        net_income = ebit - interest - taxes
        ebitda = ebit + da

        rows.append({
            "Month": str(m),
            "Revenue": revenue,
            "COGS": cogs,
            "Gross_Profit": gross_profit,
            "Payroll_Expenses": payroll,
            "Rent": rent,
            "SGA_Expenses": sga,
            "Restructuring": restructuring,
            "Depreciation_Amortization": da,
            "EBIT": ebit,
            "Interest_Expense": interest,
            "Taxes": taxes,
            "Net_Income": net_income,
            "EBITDA": ebitda,
        })

    return pd.DataFrame(rows)


# ─────────────────────────────────────────────
# GENERAL LEDGER
# ─────────────────────────────────────────────
def generate_general_ledger(mf):
    rows = []
    tx_id = 10001
    jnl = 5001

    customers = {
        "C001": "Apex Manufacturing Corp",
        "C002": "Cascade Engineering",
        "C003": "Delta Industrial",
        "C004": "Evergreen Components",
        "C005": "FrontLine Fabricators",
        "C006": "GridPoint Systems",
        "C007": "HorizonTech Ltd",
        "C008": "IronBridge Works",
        "C009": "JetStream Precision",
        "C010": "Keystone Assembly",
    }
    vendors = {
        "V001": "RawMat Supplies Inc",
        "V002": "TechServ Maintenance",
        "V003": "BuildCo Components",
        "V004": "Consulting Partners LLC",
        "V005": "Meridian Logistics",
        "V006": "PrecisionParts Co",
        "V007": "SafeGuard Insurance",
        "V008": "MachineWorks Leasing",
    }

    cust_list = list(customers.keys())
    vend_list = list(vendors.keys())

    months = pd.period_range("2024-01", "2025-12", freq="M")

    inv_num = 1001  # invoice counter
    po_num = 2001   # PO counter

    for idx, m in enumerate(months):
        mf_row = mf[mf["Month"] == str(m)].iloc[0]
        revenue = mf_row["Revenue"]
        cogs = mf_row["COGS"]
        payroll = mf_row["Payroll_Expenses"]
        rent = mf_row["Rent"]
        sga = mf_row["SGA_Expenses"]
        da = mf_row["Depreciation_Amortization"]
        restructuring = mf_row["Restructuring"]

        month_start = pd.Timestamp(str(m.start_time.date()))
        month_end = pd.Timestamp(str(m.end_time.date()))

        def rand_date(start, end):
            delta = (end - start).days
            return start + pd.Timedelta(days=int(rng.integers(0, delta + 1)))

        # ── Revenue invoices (4-6 per month) ──
        n_inv = int(rng.integers(4, 7))

        # F1: Dec 2024 — split revenue so the cutoff invoice is exactly $148,500
        # and the remaining invoices sum to (Dec revenue - 148,500)
        is_dec_2024 = (m == pd.Period("2024-12", "M"))
        if is_dec_2024:
            cutoff_amt = 148_500
            remaining_rev = revenue - cutoff_amt
            n_inv_regular = n_inv - 1
            rev_splits_regular = rng.dirichlet(np.ones(n_inv_regular)) * remaining_rev
            rev_splits_regular = np.round(rev_splits_regular, 0)
            rev_splits_regular[-1] = remaining_rev - rev_splits_regular[:-1].sum()
            # Build invoice list: regular ones first, cutoff last
            invoice_amts = list(rev_splits_regular) + [cutoff_amt]
        else:
            rev_splits = rng.dirichlet(np.ones(n_inv)) * revenue
            rev_splits = np.round(rev_splits, 0)
            rev_splits[-1] = revenue - rev_splits[:-1].sum()
            invoice_amts = list(rev_splits)

        for k, amt in enumerate(invoice_amts):
            cust = cust_list[int(rng.integers(0, len(cust_list)))]
            txn_date = rand_date(month_start, month_end)

            # F1: Dec 2024 last invoice → posting date Jan 2025
            is_cutoff_inv = (is_dec_2024 and k == len(invoice_amts) - 1)
            if is_cutoff_inv:
                amt = 148_500
                cust = "C002"  # Cascade Engineering
                txn_date = pd.Timestamp("2024-12-28")
                post_date = pd.Timestamp("2025-01-08")
                doc_ref = "INV2024-12-C002"
            else:
                # Keep posting within same month to avoid cross-year revenue leakage
                offset = int(rng.integers(0, 3))
                post_date = txn_date + pd.Timedelta(days=offset)
                # Clamp to same month-end to avoid Dec→Jan spillover for non-cutoff invoices
                if post_date.month != txn_date.month or post_date.year != txn_date.year:
                    post_date = txn_date
                doc_ref = f"INV{m.year}-{m.month:02d}-{k+1:03d}"

            # AR debit
            rows.append({
                "Transaction_ID": f"TXN{tx_id}", "Transaction_Date": txn_date.date(),
                "Posting_Date": post_date.date(), "Account_Code": "1200",
                "Account_Name": "Accounts Receivable", "Debit": amt, "Credit": 0,
                "Description": f"Customer invoice — {customers[cust]}",
                "Journal_Reference": f"JNL{jnl}", "Counterparty": customers[cust],
                "Document_Reference": doc_ref
            })
            tx_id += 1
            # Revenue credit
            rows.append({
                "Transaction_ID": f"TXN{tx_id}", "Transaction_Date": txn_date.date(),
                "Posting_Date": post_date.date(), "Account_Code": "4010",
                "Account_Name": "Revenue", "Debit": 0, "Credit": amt,
                "Description": f"Customer invoice — {customers[cust]}",
                "Journal_Reference": f"JNL{jnl}", "Counterparty": customers[cust],
                "Document_Reference": doc_ref
            })
            tx_id += 1; jnl += 1

        # ── COGS / inventory purchases ──
        n_po = int(rng.integers(3, 6))
        cogs_splits = rng.dirichlet(np.ones(n_po)) * cogs
        cogs_splits = np.round(cogs_splits, 0)
        cogs_splits[-1] = cogs - cogs_splits[:-1].sum()
        for k, amt in enumerate(cogs_splits):
            vend = vend_list[int(rng.integers(0, 3))]
            txn_date = rand_date(month_start, month_end)
            post_date = txn_date + pd.Timedelta(days=int(rng.integers(0, 3)))
            doc_ref = f"PO-{m.year}-{po_num:04d}"
            po_num += 1

            # F5: Duplicate transaction — Oct 2024, TechServ, $42,300
            # Inject on k==0 of Oct 2024
            is_dup_first = (m == pd.Period("2024-10", "M") and k == 0)
            is_dup_second = (m == pd.Period("2024-10", "M") and k == 1)
            if is_dup_first:
                amt = 42_300; vend = "V002"
                txn_date = pd.Timestamp("2024-10-05"); post_date = pd.Timestamp("2024-10-05")
                doc_ref = "PO-2024-0892"
            elif is_dup_second:
                # second (duplicate) posting of same PO
                amt = 42_300; vend = "V002"
                txn_date = pd.Timestamp("2024-10-08"); post_date = pd.Timestamp("2024-10-08")
                doc_ref = "PO-2024-0892"  # same ref!

            rows.append({
                "Transaction_ID": f"TXN{tx_id}", "Transaction_Date": txn_date.date(),
                "Posting_Date": post_date.date(), "Account_Code": "5010",
                "Account_Name": "Cost of Goods Sold", "Debit": amt, "Credit": 0,
                "Description": "Inventory purchase" if vend != "V002" else "Equipment maintenance",
                "Journal_Reference": f"JNL{jnl}", "Counterparty": vendors[vend],
                "Document_Reference": doc_ref
            })
            tx_id += 1
            rows.append({
                "Transaction_ID": f"TXN{tx_id}", "Transaction_Date": txn_date.date(),
                "Posting_Date": post_date.date(), "Account_Code": "2010",
                "Account_Name": "Accounts Payable", "Debit": 0, "Credit": amt,
                "Description": "Inventory purchase" if vend != "V002" else "Equipment maintenance",
                "Journal_Reference": f"JNL{jnl}", "Counterparty": vendors[vend],
                "Document_Reference": doc_ref
            })
            tx_id += 1; jnl += 1

        # ── Payroll ──
        txn_date = month_end - pd.Timedelta(days=1)
        rows.append({"Transaction_ID": f"TXN{tx_id}", "Transaction_Date": txn_date.date(),
            "Posting_Date": txn_date.date(), "Account_Code": "6010",
            "Account_Name": "Payroll Expenses", "Debit": payroll, "Credit": 0,
            "Description": f"Monthly payroll — {m}", "Journal_Reference": f"JNL{jnl}",
            "Counterparty": "Payroll", "Document_Reference": f"PAY-{m.year}-{m.month:02d}"})
        tx_id += 1
        rows.append({"Transaction_ID": f"TXN{tx_id}", "Transaction_Date": txn_date.date(),
            "Posting_Date": txn_date.date(), "Account_Code": "1010",
            "Account_Name": "Cash", "Debit": 0, "Credit": payroll,
            "Description": f"Monthly payroll — {m}", "Journal_Reference": f"JNL{jnl}",
            "Counterparty": "Payroll", "Document_Reference": f"PAY-{m.year}-{m.month:02d}"})
        tx_id += 1; jnl += 1

        # ── Rent ──
        rent_date = month_start + pd.Timedelta(days=1)
        rows.append({"Transaction_ID": f"TXN{tx_id}", "Transaction_Date": rent_date.date(),
            "Posting_Date": rent_date.date(), "Account_Code": "6020",
            "Account_Name": "Rent", "Debit": rent, "Credit": 0,
            "Description": "Monthly office and warehouse rent", "Journal_Reference": f"JNL{jnl}",
            "Counterparty": "Landlord Corp", "Document_Reference": f"RENT-{m.year}-{m.month:02d}"})
        tx_id += 1
        rows.append({"Transaction_ID": f"TXN{tx_id}", "Transaction_Date": rent_date.date(),
            "Posting_Date": rent_date.date(), "Account_Code": "1010",
            "Account_Name": "Cash", "Debit": 0, "Credit": rent,
            "Description": "Monthly office and warehouse rent", "Journal_Reference": f"JNL{jnl}",
            "Counterparty": "Landlord Corp", "Document_Reference": f"RENT-{m.year}-{m.month:02d}"})
        tx_id += 1; jnl += 1

        # ── SGA ──
        rows.append({"Transaction_ID": f"TXN{tx_id}", "Transaction_Date": month_end.date(),
            "Posting_Date": month_end.date(), "Account_Code": "6030",
            "Account_Name": "SGA Expenses", "Debit": sga, "Credit": 0,
            "Description": "Selling and administrative expenses", "Journal_Reference": f"JNL{jnl}",
            "Counterparty": "Various", "Document_Reference": f"SGA-{m.year}-{m.month:02d}"})
        tx_id += 1
        rows.append({"Transaction_ID": f"TXN{tx_id}", "Transaction_Date": month_end.date(),
            "Posting_Date": month_end.date(), "Account_Code": "2010",
            "Account_Name": "Accounts Payable", "Debit": 0, "Credit": sga,
            "Description": "Selling and administrative expenses", "Journal_Reference": f"JNL{jnl}",
            "Counterparty": "Various", "Document_Reference": f"SGA-{m.year}-{m.month:02d}"})
        tx_id += 1; jnl += 1

        # ── Depreciation ──
        rows.append({"Transaction_ID": f"TXN{tx_id}", "Transaction_Date": month_end.date(),
            "Posting_Date": month_end.date(), "Account_Code": "6040",
            "Account_Name": "Depreciation & Amortization", "Debit": da, "Credit": 0,
            "Description": "Monthly depreciation", "Journal_Reference": f"JNL{jnl}",
            "Counterparty": "Internal", "Document_Reference": f"DEP-{m.year}-{m.month:02d}"})
        tx_id += 1
        rows.append({"Transaction_ID": f"TXN{tx_id}", "Transaction_Date": month_end.date(),
            "Posting_Date": month_end.date(), "Account_Code": "1510",
            "Account_Name": "Accumulated Depreciation", "Debit": 0, "Credit": da,
            "Description": "Monthly depreciation", "Journal_Reference": f"JNL{jnl}",
            "Counterparty": "Internal", "Document_Reference": f"DEP-{m.year}-{m.month:02d}"})
        tx_id += 1; jnl += 1

        # ── Restructuring (F4) ──
        if restructuring > 0:
            rows.append({"Transaction_ID": f"TXN{tx_id}", "Transaction_Date": month_end.date(),
                "Posting_Date": month_end.date(), "Account_Code": "6100",
                "Account_Name": "Restructuring Charges", "Debit": restructuring, "Credit": 0,
                "Description": "Workforce restructuring and severance costs",
                "Journal_Reference": f"JNL{jnl}", "Counterparty": "Internal",
                "Document_Reference": f"RESTR-{m.year}-{m.month:02d}"})
            tx_id += 1
            rows.append({"Transaction_ID": f"TXN{tx_id}", "Transaction_Date": month_end.date(),
                "Posting_Date": month_end.date(), "Account_Code": "2020",
                "Account_Name": "Accrued Liabilities", "Debit": 0, "Credit": restructuring,
                "Description": "Workforce restructuring and severance costs",
                "Journal_Reference": f"JNL{jnl}", "Counterparty": "Internal",
                "Document_Reference": f"RESTR-{m.year}-{m.month:02d}"})
            tx_id += 1; jnl += 1

    # ── F3: ERP consulting (ADJ-005 doc ref) — no matching GL entry ──
    # Intentionally NOT adding any entry for CONS-ERP-2025
    # The actual consulting payment (different ref) was booked in Dec 2025
    rows.append({"Transaction_ID": f"TXN{tx_id}", "Transaction_Date": "2025-12-15",
        "Posting_Date": "2025-12-15", "Account_Code": "6030",
        "Account_Name": "SGA Expenses", "Debit": 55_000, "Credit": 0,
        "Description": "Strategic consulting services Q4 2025",
        "Journal_Reference": f"JNL{jnl}", "Counterparty": "Consulting Partners LLC",
        "Document_Reference": "CONS-2025-Q4"})
    tx_id += 1
    rows.append({"Transaction_ID": f"TXN{tx_id}", "Transaction_Date": "2025-12-15",
        "Posting_Date": "2025-12-15", "Account_Code": "1010",
        "Account_Name": "Cash", "Debit": 0, "Credit": 55_000,
        "Description": "Strategic consulting services Q4 2025",
        "Journal_Reference": f"JNL{jnl}", "Counterparty": "Consulting Partners LLC",
        "Document_Reference": "CONS-2025-Q4"})
    tx_id += 1; jnl += 1

    df = pd.DataFrame(rows)
    df = df.sort_values(["Posting_Date", "Transaction_ID"]).reset_index(drop=True)
    return df


# ─────────────────────────────────────────────
# AR AGING
# ─────────────────────────────────────────────
def generate_ar_aging():
    ref_date = pd.Timestamp("2025-12-31")
    rows = [
        # Current
        {"Customer_ID":"C001","Customer_Name":"Apex Manufacturing Corp",
         "Invoice_Number":"INV2025-1120","Invoice_Date":"2025-12-05","Due_Date":"2026-01-04",
         "Outstanding_Amount":287_400,"Days_Overdue":0,"Aging_Bucket":"Current",
         "Dispute_Status":"No","Collection_Notes":"Within terms"},
        {"Customer_ID":"C003","Customer_Name":"Delta Industrial",
         "Invoice_Number":"INV2025-1118","Invoice_Date":"2025-11-28","Due_Date":"2025-12-28",
         "Outstanding_Amount":143_200,"Days_Overdue":3,"Aging_Bucket":"1-30",
         "Dispute_Status":"No","Collection_Notes":"Payment expected imminently"},
        {"Customer_ID":"C005","Customer_Name":"FrontLine Fabricators",
         "Invoice_Number":"INV2025-1105","Invoice_Date":"2025-11-10","Due_Date":"2025-12-10",
         "Outstanding_Amount":98_600,"Days_Overdue":21,"Aging_Bucket":"1-30",
         "Dispute_Status":"No","Collection_Notes":"Chaser sent 2025-12-18"},
        {"Customer_ID":"C006","Customer_Name":"GridPoint Systems",
         "Invoice_Number":"INV2025-1082","Invoice_Date":"2025-10-20","Due_Date":"2025-11-19",
         "Outstanding_Amount":74_300,"Days_Overdue":42,"Aging_Bucket":"31-60",
         "Dispute_Status":"No","Collection_Notes":"Partial payment promised"},
        {"Customer_ID":"C007","Customer_Name":"HorizonTech Ltd",
         "Invoice_Number":"INV2025-1061","Invoice_Date":"2025-10-01","Due_Date":"2025-10-31",
         "Outstanding_Amount":56_800,"Days_Overdue":61,"Aging_Bucket":"61-90",
         "Dispute_Status":"No","Collection_Notes":"Credit hold applied"},
        {"Customer_ID":"C004","Customer_Name":"Evergreen Components",
         "Invoice_Number":"INV2025-1044","Invoice_Date":"2025-09-15","Due_Date":"2025-10-15",
         "Outstanding_Amount":112_500,"Days_Overdue":77,"Aging_Bucket":"61-90",
         "Dispute_Status":"No","Collection_Notes":"Repayment plan agreed"},
        # F2: IronBridge — in administration, 437 days
        {"Customer_ID":"C008","Customer_Name":"IronBridge Works",
         "Invoice_Number":"INV2024-0845","Invoice_Date":"2024-10-20","Due_Date":"2024-11-19",
         "Outstanding_Amount":312_800,"Days_Overdue":407,"Aging_Bucket":"Over 90",
         "Dispute_Status":"No",
         "Collection_Notes":"Customer in administration proceedings — legal counsel engaged 2025-08"},
        {"Customer_ID":"C010","Customer_Name":"Keystone Assembly",
         "Invoice_Number":"INV2025-0988","Invoice_Date":"2025-07-10","Due_Date":"2025-08-09",
         "Outstanding_Amount":67_400,"Days_Overdue":144,"Aging_Bucket":"Over 90",
         "Dispute_Status":"No","Collection_Notes":"Slow payer — monitoring"},
        {"Customer_ID":"C002","Customer_Name":"Cascade Engineering",
         "Invoice_Number":"INV2025-0954","Invoice_Date":"2025-06-01","Due_Date":"2025-07-01",
         "Outstanding_Amount":43_200,"Days_Overdue":183,"Aging_Bucket":"Over 90",
         "Dispute_Status":"No","Collection_Notes":"Settlement discussion ongoing"},
    ]
    df = pd.DataFrame(rows)
    df["Invoice_Date"] = pd.to_datetime(df["Invoice_Date"])
    df["Due_Date"] = pd.to_datetime(df["Due_Date"])
    return df


# ─────────────────────────────────────────────
# MANAGEMENT ADJUSTMENTS
# ─────────────────────────────────────────────
def generate_management_adjustments():
    rows = [
        {"Adjustment_ID":"ADJ-001","Period":"2024","Description":"Legal settlement — one-time litigation cost",
         "Account_Code":"6030","Amount":185_000,"Adjustment_Category":"Non-recurring expense",
         "Management_Rationale":"Settled a supplier contract dispute in Q2 2024; not expected to recur.",
         "Supporting_Document_Reference":"LEGAL-SET-2024","Recurrence_Indicator":"One-time"},
        # F4: recurring restructuring — 2024
        {"Adjustment_ID":"ADJ-002","Period":"2024","Description":"Restructuring charges — workforce right-sizing Nov 2024",
         "Account_Code":"6100","Amount":95_000,"Adjustment_Category":"Non-recurring expense",
         "Management_Rationale":"One-time headcount reduction to align with revised operating model.",
         "Supporting_Document_Reference":"RESTR-2024-11","Recurrence_Indicator":"One-time"},
        # F4: recurring restructuring — 2025
        {"Adjustment_ID":"ADJ-003","Period":"2025","Description":"Restructuring charges — operational consolidation Feb 2025",
         "Account_Code":"6100","Amount":78_000,"Adjustment_Category":"Non-recurring expense",
         "Management_Rationale":"One-time cost to consolidate two distribution facilities.",
         "Supporting_Document_Reference":"RESTR-2025-02","Recurrence_Indicator":"One-time"},
        {"Adjustment_ID":"ADJ-004","Period":"2025","Description":"Owner compensation normalization",
         "Account_Code":"6010","Amount":120_000,"Adjustment_Category":"Normalization",
         "Management_Rationale":"CEO compensation above market rate; normalized to $280k benchmark.",
         "Supporting_Document_Reference":"HR-COMP-2025","Recurrence_Indicator":"Recurring"},
        # F3: unsupported ERP consulting
        {"Adjustment_ID":"ADJ-005","Period":"2025","Description":"Strategic consulting — ERP implementation advisory",
         "Account_Code":"6030","Amount":95_000,"Adjustment_Category":"Non-recurring expense",
         "Management_Rationale":"One-time cost for external ERP advisory engagement (project NOVA).",
         "Supporting_Document_Reference":"CONS-ERP-2025","Recurrence_Indicator":"One-time"},
        {"Adjustment_ID":"ADJ-006","Period":"2025","Description":"Depreciation normalization — accelerated assets",
         "Account_Code":"6040","Amount":42_000,"Adjustment_Category":"Normalization",
         "Management_Rationale":"Accelerated depreciation on legacy tooling; normalized to straight-line.",
         "Supporting_Document_Reference":"FA-DEP-2025","Recurrence_Indicator":"Recurring"},
        {"Adjustment_ID":"ADJ-007","Period":"2025","Description":"Above-market rent normalization",
         "Account_Code":"6020","Amount":36_000,"Adjustment_Category":"Normalization",
         "Management_Rationale":"Facility rent $36k above comparable market lease; normalized to market.",
         "Supporting_Document_Reference":"LEASE-MKT-2025","Recurrence_Indicator":"Recurring"},
        # F5: duplicate — management proposes add-back
        {"Adjustment_ID":"ADJ-008","Period":"2024","Description":"Duplicate maintenance charge reversal — PO-2024-0892",
         "Account_Code":"5010","Amount":42_300,"Adjustment_Category":"Accounting correction",
         "Management_Rationale":"TechServ maintenance invoice PO-2024-0892 posted twice in Oct 2024.",
         "Supporting_Document_Reference":"PO-2024-0892","Recurrence_Indicator":"One-time"},
        {"Adjustment_ID":"ADJ-009","Period":"2025","Description":"FX revaluation loss — non-operational",
         "Account_Code":"6030","Amount":18_500,"Adjustment_Category":"Non-recurring expense",
         "Management_Rationale":"Mark-to-market FX loss on USD/EUR exposure; non-cash and non-recurring.",
         "Supporting_Document_Reference":"FX-REVAL-2025","Recurrence_Indicator":"One-time"},
    ]
    return pd.DataFrame(rows)


# ─────────────────────────────────────────────
# VALIDATE
# ─────────────────────────────────────────────
def validate(mf, gl, ar, adj):
    print("\n" + "="*60)
    print("NORTHSTAR COMPACT — VALIDATION REPORT")
    print("="*60)

    passed = 0
    total = 5

    # F1: Revenue cutoff
    gl["Posting_Date"] = pd.to_datetime(gl["Posting_Date"])
    gl["Transaction_Date"] = pd.to_datetime(gl["Transaction_Date"])
    rev_gl = gl[gl["Account_Code"] == "4010"].copy()
    rev_gl_2025 = rev_gl[rev_gl["Posting_Date"].dt.year == 2025]["Credit"].sum()
    mf["Year"] = pd.to_datetime(mf["Month"]).dt.year
    rev_mf_2025 = mf[mf["Year"] == 2025]["Revenue"].sum()
    diff_f1 = rev_gl_2025 - rev_mf_2025
    ok_f1 = abs(diff_f1 - 148_500) < 500
    print(f"\n[F1] Revenue cutoff: MF 2025=${rev_mf_2025:,.0f} | GL 2025=${rev_gl_2025:,.0f} | Diff=${diff_f1:,.0f}")
    print(f"     {'✓ PASS' if ok_f1 else '✗ FAIL'}")
    if ok_f1: passed += 1

    # F2: IronBridge
    ironbridge = ar[ar["Customer_ID"] == "C008"]
    ok_f2 = len(ironbridge) == 1 and ironbridge["Outstanding_Amount"].values[0] == 312_800
    print(f"\n[F2] IronBridge overdue: ${ironbridge['Outstanding_Amount'].sum():,.0f} | Days: {list(ironbridge['Days_Overdue'].values)}")
    print(f"     {'✓ PASS' if ok_f2 else '✗ FAIL'}")
    if ok_f2: passed += 1

    # F3: Unsupported adjustment
    doc_ref = adj[adj["Adjustment_ID"] == "ADJ-005"]["Supporting_Document_Reference"].values[0]
    gl_match = gl[gl["Document_Reference"] == doc_ref]
    ok_f3 = len(gl_match) == 0
    print(f"\n[F3] ADJ-005 doc ref '{doc_ref}' found in GL: {len(gl_match)} rows")
    print(f"     {'✓ PASS' if ok_f3 else '✗ FAIL'}")
    if ok_f3: passed += 1

    # F4: Recurring restructuring
    restr_gl = gl[gl["Account_Code"] == "6100"].copy()
    restr_gl["Year"] = restr_gl["Posting_Date"].dt.year
    years = set(restr_gl["Year"].unique())
    restr_adj = adj[adj["Account_Code"] == "6100"]
    ok_f4 = 2024 in years and 2025 in years and len(restr_adj) == 2
    print(f"\n[F4] Restructuring in years: {sorted(years)} | Adj count: {len(restr_adj)}")
    print(f"     {'✓ PASS' if ok_f4 else '✗ FAIL'}")
    if ok_f4: passed += 1

    # F5: Duplicate transaction
    dup = gl[gl["Document_Reference"] == "PO-2024-0892"]
    total_debit = dup[dup["Debit"] > 0]["Debit"].sum()
    ok_f5 = len(dup) == 4 and abs(total_debit - 84_600) < 1
    print(f"\n[F5] PO-2024-0892 rows: {len(dup)} | Total debit: ${total_debit:,.0f}")
    print(f"     {'✓ PASS' if ok_f5 else '✗ FAIL'}")
    if ok_f5: passed += 1

    print(f"\n{'='*60}")
    print(f"Findings detectable: {passed} / {total} tested")
    for i, (ok, label) in enumerate(zip(
        [ok_f1, ok_f2, ok_f3, ok_f4, ok_f5],
        ["F1-Revenue Cutoff","F2-AR Impairment IronBridge","F3-Unsupported Adj ADJ-005",
         "F4-Recurring Restructuring","F5-Duplicate Transaction"]
    ), 1):
        print(f"  {'✓' if ok else '✗'} {label}")

    # Key figures
    rev_2024 = mf[mf["Year"] == 2024]["Revenue"].sum()
    rev_2025 = mf[mf["Year"] == 2025]["Revenue"].sum()
    ebitda_2024 = mf[mf["Year"] == 2024]["EBITDA"].sum()
    ebitda_2025 = mf[mf["Year"] == 2025]["EBITDA"].sum()
    accepted_adj = adj[~adj["Adjustment_ID"].isin(["ADJ-003","ADJ-005"])]["Amount"].sum()
    rejected_adj = adj[adj["Adjustment_ID"].isin(["ADJ-003","ADJ-005"])]["Amount"].sum()
    norm_ebitda = ebitda_2025 + accepted_adj
    ar_total = ar["Outstanding_Amount"].sum()

    print(f"\nKEY FINANCIAL FIGURES:")
    print(f"  Revenue 2024:              ${rev_2024:>12,.0f}")
    print(f"  Revenue 2025:              ${rev_2025:>12,.0f}")
    print(f"  EBITDA 2024:               ${ebitda_2024:>12,.0f}")
    print(f"  EBITDA 2025:               ${ebitda_2025:>12,.0f}")
    print(f"  Mgmt adj accepted:         ${accepted_adj:>12,.0f}")
    print(f"  Mgmt adj rejected:         ${rejected_adj:>12,.0f}")
    print(f"  Normalized EBITDA 2025:    ${norm_ebitda:>12,.0f}")
    print(f"  AR total outstanding:      ${ar_total:>12,.0f}")
    print("="*60)

    return passed == total


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("Generating Northstar Industrial Components Ltd. — Compact Edition...")

    mf = generate_monthly_financials()
    gl = generate_general_ledger(mf)
    ar = generate_ar_aging()
    adj = generate_management_adjustments()

    # Ensure Account_Code is stored as string
    gl["Account_Code"] = gl["Account_Code"].astype(str)

    mf.to_csv(os.path.join(BASE_DIR, "monthly_financials.csv"), index=False)
    gl.to_csv(os.path.join(BASE_DIR, "general_ledger.csv"), index=False)
    ar.to_csv(os.path.join(BASE_DIR, "accounts_receivable_aging.csv"), index=False)
    adj.to_csv(os.path.join(BASE_DIR, "management_adjustments.csv"), index=False)

    all_ok = validate(mf, gl, ar, adj)

    if all_ok:
        print("\n✓ All validations passed. Dataset ready for distribution.")
    else:
        print("\n✗ One or more validations failed. Review the script.")

    print(f"\nCSV files written to: {BASE_DIR}")
