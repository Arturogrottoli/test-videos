# %% 1
import pandas as pd
import numpy as np
n = "orders payments refunds products processor_terms".split()
o, p, r, k, t = [pd.read_csv(f + ".csv") for f in n]
for d in [o, p, r, k, t]: d.info()
t
# %% 2
dup = o[o.duplicated()]
o = o.drop_duplicates()
print(len(dup), dup.order_total.sum(), o.order_id.is_unique, p.payment_id.is_unique)
# %% 3
c = p[p.status.eq("captured")].merge(t, on="method")
L = o.merge(c, on="order_id", how="outer", indicator=True, validate="1:1")
print(p.amount.sum() - c.amount.sum())
L._merge.value_counts()
# %% 4
L["fee"] = (L.amount * L.fee_pct + L.fee_fixed).round(2)
L["gap"] = (L.amount - L.fee - L.settled).round(2)
L.gap.value_counts()
# %% 5
L["refund"] = L.payment_id.map(r.groupby("payment_id").amount.sum()).fillna(0)
r.amount.sum() - L.refund.sum()
# %% 6
L["cogs"] = L.quantity * L.product_id.map(k.set_index("product_id").unit_cost)
L["margin"] = L.amount - L.refund - L.fee - L.cogs
k[k.unit_cost.isna()]
# %% 7
e = {"no_payment": L.payment_id.isna(), "no_order": L.order_total.isna(),
     "amount_diff": L.amount.ne(L.order_total), "over_refund": L.refund.gt(L.amount),
     "short_paid": L.gap.gt(0), "pending": L.settled.isna(), "no_cost": L.cogs.isna()}
L["issue"] = np.select(list(e.values()), list(e), "ok")
x = pd.concat([L[L.issue.ne("ok")], dup.assign(issue="duplicate"), r[~r.payment_id.isin(c.payment_id)].assign(issue="bad_refund")])
x.issue.value_counts()
# %% 8
s = L.groupby("issue")["order_total amount refund fee settled gap cogs margin".split()].sum(min_count=1)
s.loc["total"] = s.sum()
L.to_csv("transaction_reconciliation_ledger.csv", index=False)
x.to_csv("exception_register.csv", index=False)
s.to_csv("financial_control_summary.csv")
s.round(2)
# %% 9
(s.loc["total", ["order_total", "amount", "settled"]] - [o.order_total.sum(), c.amount.sum(), p.settled.sum()]).abs().round(2)
