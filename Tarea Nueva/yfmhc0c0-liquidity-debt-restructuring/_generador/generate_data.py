"""Genera los cinco CSV sintéticos de yfmhc0c0 (13-week liquidity).
Uso: python generate_data.py <carpeta_destino>
Fecha de corte (as-of): viernes 2026-11-20. Semana 1 = lunes 2026-11-23.
"""
import sys
import numpy as np
import pandas as pd

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
OPEN_OPR = float(sys.argv[2]) if len(sys.argv) > 2 else 620000.0
RESERVE = float(sys.argv[3]) if len(sys.argv) > 3 else 150000.0
rng = np.random.default_rng(42)
ASOF = pd.Timestamp("2026-11-20")
W1 = pd.Timestamp("2026-11-23")

# ---------------------------------------------------------------- AR
# customer: (weekly sales, terms, base days late, trend days late added by Nov)
cust = {
    "Northwind Retail":    (96000, 45, 4, 23),
    "Bluefield Grocers":   (36000, 30, 3, 0),
    "Cedar Home Supply":   (29000, 30, 8, 0),
    "Delta Foods":         (23000, 30, 6, 0),
    "Evergreen Markets":   (21000, 30, 0, 0),
    "Foxglove Pharmacy":   (18000, 30, 12, 0),
    "Granite Hardware":    (17000, 30, 5, 0),
    "Harbor Cafe Group":   (10000, 30, 18, 0),
    "Ironwood Outfitters": (15000, 30, 2, 0),
    "Juniper Pet Co":      (14000, 30, 6, 0),
    "Keystone Office":     (12000, 30, 15, 0),
    "Lakeside Clinics":    (9000, 30, 0, 0),
}
start = pd.Timestamp("2026-03-02")
rows = []
n = 1
for c, (wk_sales, terms, late0, trend) in cust.items():
    for d in pd.date_range(start, ASOF, freq="7D"):
        inv_date = d + pd.Timedelta(days=int(rng.integers(0, 5)))
        if inv_date > ASOF:
            continue
        amt = round(wk_sales * rng.uniform(0.85, 1.15), 2)
        due = inv_date + pd.Timedelta(days=terms)
        prog = (due - start).days / (ASOF + pd.Timedelta(days=45) - start).days
        late = late0 + trend * (due >= pd.Timestamp("2026-08-01")) + rng.normal(0, 3)
        late = max(int(round(late)), -3)
        paid = due + pd.Timedelta(days=late)
        rows.append([f"INV-{n:05d}", c, inv_date, due, amt, paid])
        n += 1
ar = pd.DataFrame(rows, columns=["invoice_id", "customer", "invoice_date", "due_date", "amount", "paid_date"])
ar = ar.sort_values("invoice_date").reset_index(drop=True)
ar["invoice_id"] = [f"INV-{i:05d}" for i in range(10001, 10001 + len(ar))]
ar["status"] = np.where(ar.paid_date <= ASOF, "paid", "open")
ar.loc[ar.status == "open", "paid_date"] = pd.NaT

# Delta Foods: two invoices in dispute (quality claim), never paid
dlt = ar[(ar.customer == "Delta Foods") & (ar.invoice_date.between("2026-09-01", "2026-09-20"))].index[:2]
ar.loc[dlt, ["status", "paid_date"]] = ["disputed", pd.NaT]
# Keystone Office: two old invoices never paid (>90 days past due)
ks = ar[(ar.customer == "Keystone Office") & (ar.invoice_date.between("2026-06-01", "2026-06-20"))].index[:2]
ar.loc[ks, ["status", "paid_date"]] = ["open", pd.NaT]
# Harbor Cafe: one invoice paid in October, later returned NSF by the bank (AR still says paid)
hb = ar[(ar.customer == "Harbor Cafe Group") & (ar.paid_date.between("2026-10-05", "2026-10-20"))].index[0]
nsf_id = ar.loc[hb, "invoice_id"]

# ---------------------------------------------------------------- BANK
b = []
def add(date, acct, typ, desc, ref, amt, status="cleared"):
    b.append([pd.Timestamp(date), acct, typ, desc, ref, round(amt, 2), status])

add("2026-09-30", "OPR-01", "operating", "Opening balance", "OPEN", OPEN_OPR)
add("2026-09-30", "PAY-02", "operating", "Opening balance", "OPEN", 25000.00)
add("2026-09-30", "DSR-03", "restricted", "Opening balance - debt service reserve", "OPEN", 380000.00)

paid_win = ar[(ar.status == "paid") & (ar.paid_date >= "2026-10-01")]
for r in paid_win.itertuples():
    add(r.paid_date, "OPR-01", "operating", f"Customer payment - {r.customer}", r.invoice_id, r.amount)
nsf = ar.loc[hb]
add(nsf.paid_date + pd.Timedelta(days=4), "OPR-01", "operating", f"Returned item NSF - {nsf.customer}", nsf_id, -nsf.amount)

vendors_paid = ["Summit Foods Supply", "Rapid Freight", "PackRight Packaging", "Metro Utilities", "Cloudline IT"]
k = 1
for d in pd.date_range("2026-10-02", "2026-11-20", freq="7D"):
    for v, base in zip(vendors_paid, [100000, 20000, 12000, 6000, 4000]):
        add(d, "OPR-01", "operating", f"Vendor payment - {v}", f"BILL-P{k:04d}", -base * rng.uniform(0.9, 1.1))
        k += 1
for d in pd.date_range("2026-10-09", "2026-11-20", freq="14D"):
    add(d - pd.Timedelta(days=1), "OPR-01", "operating", "Transfer to payroll account", "XFER", -110000)
    add(d - pd.Timedelta(days=1), "PAY-02", "operating", "Transfer from operating account", "XFER", 110000)
    add(d, "PAY-02", "operating", "Payroll run", "PAYROLL", -110000)
for d in ["2026-10-01", "2026-11-02"]:
    add(d, "OPR-01", "operating", "Warehouse rent", "RENT", -45000)
    add(d, "OPR-01", "operating", "Equipment loan EQ-01 payment", "EQ-01", -15500)
    add(pd.Timestamp(d) - pd.Timedelta(days=1), "OPR-01", "operating", "Revolver RCF-01 interest", "RCF-01", -5938)
    add(d, "DSR-03", "restricted", "Interest credit", "INT", 950)
add("2026-10-15", "OPR-01", "operating", "Term loan TL-01 quarterly payment", "TL-01", -168000)
for d in pd.date_range("2026-10-05", "2026-11-20", freq="7D"):
    add(d, "OPR-01", "operating", "Operating expenses - card settlement", "OPEX", -14000 * rng.uniform(0.9, 1.1))
# outstanding checks (issued, not yet cleared)
add("2026-11-17", "OPR-01", "operating", "Check 40118 - County property tax", "CHK-40118", -28400, "pending")
add("2026-11-18", "OPR-01", "operating", "Check 40119 - Lark & Co audit fees", "CHK-40119", -19500, "pending")
add("2026-11-19", "OPR-01", "operating", "Check 40120 - State sales tax", "CHK-40120", -16250, "pending")

bk = pd.DataFrame(b, columns=["date", "account_id", "account_type", "description", "reference", "amount", "status"])
bk = bk.sort_values(["date", "account_id"]).reset_index(drop=True)
bk.insert(0, "txn_id", [f"T{i:05d}" for i in range(1, len(bk) + 1)])
# export error: five rows duplicated (two of them large customer receipts)
big = bk[bk.description.str.startswith("Customer payment - Northwind")].index[-2:]
dup_idx = list(big) + list(bk[bk.description.str.startswith("Customer payment - Bluefield")].index[-1:]) \
    + list(bk[bk.description.str.startswith("Vendor payment - Metro")].index[-2:])
bk = pd.concat([bk, bk.loc[dup_idx]]).sort_values(["date", "txn_id"]).reset_index(drop=True)

# ---------------------------------------------------------------- AP (open bills at as-of)
vend = {  # vendor: (category, critical, max_extension_days, weekly amount, terms)
    "Summit Foods Supply": ("inventory", "Y", 0, 100000, 30),
    "Rapid Freight": ("freight", "Y", 0, 20000, 30),
    "Orchard Produce Co": ("inventory", "N", 21, 30000, 30),
    "PackRight Packaging": ("packaging", "N", 30, 12000, 45),
    "Metro Utilities": ("utilities", "N", 0, 6000, 30),
    "Cloudline IT": ("it_services", "N", 30, 4000, 30),
    "Keller Maintenance": ("maintenance", "N", 30, 5000, 45),
    "Brightline Marketing": ("marketing", "N", 30, 7000, 45),
}
ap_rows = []
j = 1
for v, (cat, crit, ext, amt, terms) in vend.items():
    for d in pd.date_range(ASOF - pd.Timedelta(days=terms + 3), ASOF, freq="7D"):
        bd = d + pd.Timedelta(days=int(rng.integers(0, 3)))
        ap_rows.append([f"BILL-{j:05d}", v, cat, bd, bd + pd.Timedelta(days=terms), round(amt * rng.uniform(0.9, 1.1), 2), crit, ext])
        j += 1
ap = pd.DataFrame(ap_rows, columns=["bill_id", "vendor", "category", "bill_date", "due_date", "amount", "critical", "max_extension_days"])
ap = ap[ap.bill_date <= ASOF].sort_values("due_date").reset_index(drop=True)
ap["bill_id"] = [f"BILL-{i:05d}" for i in range(20001, 20001 + len(ap))]

# ---------------------------------------------------------------- DEBT
debt = pd.DataFrame([
    ["RCF-01", "revolver", "First Harbor Bank", 1200000, 750000, 0.095, "2028-06-30", "2026-11-30", 1, 5938, 0.80, 90, 0.25, RESERVE, 500000, 3.5, 1070000],
    ["TL-01", "term_loan", "First Harbor Bank", 3000000, 2400000, 0.080, "2029-01-15", "2027-01-15", 3, 168000, None, None, None, None, None, None, None],
    ["EQ-01", "equipment_loan", "Copperline Leasing", 500000, 360000, 0.070, "2029-06-01", "2026-12-01", 1, 15500, None, None, None, None, None, None, None],
], columns=["facility_id", "facility_type", "lender", "commitment", "drawn", "interest_rate", "maturity_date",
            "next_payment_date", "payment_months", "scheduled_payment", "advance_rate", "eligibility_days",
            "concentration_limit", "reserve", "min_unrestricted_cash", "max_leverage", "ltm_ebitda"])

# ---------------------------------------------------------------- OPERATING FORECAST
of = []
def wk_of(date):
    return (pd.Timestamp(date) - W1).days // 7 + 1
for w in range(1, 14):
    ws = W1 + pd.Timedelta(weeks=w - 1)
    if w >= 5:  # new sales from week 1 collected on terms (management view): 30 days, Northwind 45
        holiday = 1.0
        of.append([w, ws, "collections_new_sales", "Other customers", round(204000 * holiday * rng.uniform(0.97, 1.03), -2), "N"])
        if w >= 7:
            of.append([w, ws, "collections_new_sales", "Northwind Retail", round(96000 * holiday * rng.uniform(0.97, 1.03), -2), "N"])
    if w >= 5:
        of.append([w, ws, "supplier_payments_new_purchases", None, -round(184000 * rng.uniform(0.97, 1.03), -2), "N"])
    if w % 2 == 1:
        of.append([w, ws, "payroll", None, -110000, "N"])
    of.append([w, ws, "other_opex", None, -14000, "N"])
    if w % 2 == 0:
        of.append([w, ws, "marketing", None, -9000, "Y"])
for d in ["2026-12-01", "2027-01-01", "2027-02-01"]:
    of.append([wk_of(d), W1 + pd.Timedelta(weeks=wk_of(d) - 1), "rent", None, -45000, "N"])
of.append([6, W1 + pd.Timedelta(weeks=5), "year_end_bonus", None, -65000, "N"])
of.append([7, W1 + pd.Timedelta(weeks=6), "insurance_premium", None, -92000, "N"])
of.append([6, W1 + pd.Timedelta(weeks=5), "capex_warehouse_racking", None, -85000, "Y"])
of.append([9, W1 + pd.Timedelta(weeks=8), "capex_forklift", None, -40000, "Y"])
op = pd.DataFrame(of, columns=["week", "week_start", "category", "customer", "amount", "discretionary"]).sort_values(["week", "category"])

# ---------------------------------------------------------------- WRITE
ar[["invoice_id", "customer", "invoice_date", "due_date", "amount", "status", "paid_date"]].to_csv(f"{OUT}/accounts_receivable.csv", index=False, date_format="%Y-%m-%d")
bk.to_csv(f"{OUT}/bank_transactions.csv", index=False, date_format="%Y-%m-%d")
ap.to_csv(f"{OUT}/accounts_payable.csv", index=False, date_format="%Y-%m-%d")
debt.to_csv(f"{OUT}/debt_facilities.csv", index=False)
op.to_csv(f"{OUT}/operating_forecast.csv", index=False, date_format="%Y-%m-%d")
print("bank", bk.shape, "ar", ar.shape, "ap", ap.shape, "debt", debt.shape, "op", op.shape)
