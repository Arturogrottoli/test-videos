# %% 1
import pandas as pd
import numpy as np
b = pd.read_csv("bank_transactions.csv", parse_dates=["date"])
ar = pd.read_csv("accounts_receivable.csv", parse_dates=["invoice_date", "due_date", "paid_date"])
ap = pd.read_csv("accounts_payable.csv", parse_dates=["bill_date", "due_date"])
debt = pd.read_csv("debt_facilities.csv")
op = pd.read_csv("operating_forecast.csv")
W1 = pd.Timestamp("2026-11-23")
for n, d in {"bank": b, "ar": ar, "ap": ap, "debt": debt, "op": op}.items():
    print(n, d.shape, "| duplicate rows:", d.duplicated().sum())
print(b.groupby(["account_type", "status"]).amount.sum().round(0).to_dict())
debt.set_index("facility_id").T
# %% 2
cash0 = b[~b.duplicated("txn_id") & b.account_type.eq("operating")].amount.sum()
round(cash0)
# %% 3
ar["late"] = (ar.paid_date - ar.due_date).dt.days
d = ar[ar.paid_date > "2026-08-22"].groupby("customer").late.median()
ar["exp"] = ar.due_date + pd.to_timedelta(ar.customer.map(d), "D")
ar.to_csv("accounts_receivable.csv")
d
# %% 4
W = lambda s: (s - W1).dt.days.clip(0) // 7 + 1
o = ar[ar.status.eq("open")].assign(week=W(ar.exp))
f = pd.concat([o, ap.assign(week=W(ap.due_date), amount=-ap.amount), op.assign(week=op.week + op.customer.map(d).fillna(0) // 7)])
c = lambda x: cash0 + x.groupby("week").amount.sum().loc[:13].cumsum()
c(f)
# %% 5
r = debt.iloc[0]
bb = r.advance_rate * o.amount.sum() - r.reserve - r.drawn
cap = min(r.commitment - r.drawn, bb, r.max_leverage * r.ltm_ebitda - debt.drawn.sum())
print(bb, cap)
# %% 6
p = f[f.discretionary.ne("Y")]
q = p.assign(week=p.week + p.max_extension_days.fillna(0) // 7)
s = q.assign(week=q.week + 2 * q.customer.eq(d.idxmax()))
x = np.ceil((500000 - c(s).min()) / 25000) * 25000
t = pd.DataFrame({"base": c(f), "levers": c(q), "plan": c(q) + x, "stress": c(s) + x})
print(x, x <= cap)
t.min()
