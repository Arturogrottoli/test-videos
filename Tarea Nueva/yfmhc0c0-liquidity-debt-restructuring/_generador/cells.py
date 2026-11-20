# %% 1
import pandas as pd
import numpy as np
b = pd.read_csv("bank_transactions.csv", parse_dates=["date"])
ar = pd.read_csv("accounts_receivable.csv", parse_dates=["invoice_date", "due_date", "paid_date"])
ap = pd.read_csv("accounts_payable.csv", parse_dates=["bill_date", "due_date"])
debt = pd.read_csv("debt_facilities.csv", parse_dates=["next_payment_date"])
op = pd.read_csv("operating_forecast.csv", parse_dates=["week_start"])
for n, d in {"bank": b, "ar": ar, "ap": ap, "debt": debt, "op": op}.items():
    print(n, d.shape, "| duplicate rows:", d.duplicated().sum())
print(b.groupby(["account_id", "account_type", "status"]).amount.sum().round(0).to_dict())
debt.set_index("facility_id").T
# %% 2
b["dup"] = b.duplicated("txn_id")
pos = b[~b.dup].groupby(["account_type", "status"]).amount.sum()
cash0 = pos["operating"].sum()
print(b[b.dup].amount.sum().round(), cash0.round())
pos
# %% 3
net = b[~b.dup].groupby("reference").amount.sum()
nsf = ar.status.eq("paid") & ar.invoice_id.map(net).eq(0)
ar["status_raw"] = ar.status
ar.loc[nsf, "status"] = "returned"
print("NSF:", ar.loc[nsf, ["invoice_id", "customer", "amount"]].values.tolist())
ASOF = pd.Timestamp("2026-11-20")
ar["days_late"] = (ar.paid_date - ar.due_date).dt.days
recent = ar[ar.paid_date > ASOF - pd.Timedelta(days=90)]
delay = recent.groupby("customer").days_late.median().clip(lower=0)
o = ar[ar.status.eq("open")].copy()
o["expected"] = o.due_date + pd.to_timedelta(o.customer.map(delay), "D")
o["collect"] = (ASOF - o.due_date).dt.days.le(90)
share = o.groupby("customer").amount.sum().sort_values(ascending=False) / o.amount.sum()
top = share.index[0]
print(top, "share of open AR:", round(share.iloc[0], 2), "| median days late, all history:", ar[ar.customer.eq(top)].days_late.median(), "| last 90 days:", delay[top])
print("excluded from forecast $:", ar[ar.status.isin(["disputed", "returned"])].amount.sum().round(0), "disputed/NSF +", o[~o.collect].amount.sum().round(0), "over 90 days past due")
print("AP share with critical suppliers:", round(ap[ap.critical.eq("Y")].amount.sum() / ap.amount.sum(), 2), "| discretionary spend:", op[op.discretionary.eq("Y")].amount.sum())
delay["Other customers"] = recent[recent.customer.ne(top)].days_late.median()
op["week_raw"] = op.week
op["week"] += (op.customer.map(delay) / 7).round().fillna(0).astype(int)
print("new-sales collection lag (weeks):", (op.week - op.week_raw).groupby(op.customer).max().to_dict(), "| $ pushed past week 13:", op[op.week > 13].amount.sum())
el = o[(ASOF - o.invoice_date).dt.days.le(debt.eligibility_days[0])].groupby("customer").amount.sum()
# %% 4
W1 = pd.Timestamp("2026-11-23")
MIN = debt.min_unrestricted_cash[0]
wk = lambda d: ((d - W1).dt.days // 7 + 1).clip(lower=1)
ds = pd.concat([pd.DataFrame({"date": pd.date_range(r.next_payment_date, "2027-02-21", freq=pd.DateOffset(months=r.payment_months)), "amount": r.scheduled_payment}) for r in debt.itertuples()])
def forecast(o, ap, op, draw={}):
    f = pd.DataFrame(index=range(1, 14))
    f["ar_in"] = o[o.collect].groupby(wk(o.expected)).amount.sum()
    f["operating"] = op.groupby("week").amount.sum()
    f["ap_out"] = -ap.groupby(wk(ap.due_date)).amount.sum()
    f["debt_out"] = -ds.groupby(wk(ds.date)).amount.sum()
    f["rcf_draw"] = pd.Series(draw, dtype=float)
    f = f.fillna(0)
    f["close"] = cash0 + f.sum(axis=1).cumsum()
    return f
base = forecast(o, ap, op)
low = base.index[base.close < MIN]
print("weeks below", MIN, ":", list(low), "| trough:", round(base.close.min()), "in week", base.close.idxmin(), "| week 13:", round(base.close.iloc[-1]), "| net flow weeks 12-13:", round(base.close.diff().tail(2).mean()))
base.round(0)
# %% 5
r = debt.iloc[0]
e = el.clip(upper=r.concentration_limit * el.sum())
bb = r.advance_rate * e.sum() - r.reserve - r.drawn
lev = r.max_leverage * r.ltm_ebitda - debt.drawn.sum()
cap = min(r.commitment - r.drawn, bb, lev)
print(r.commitment - r.drawn, round(bb), lev, cap)
# %% 6
ap2 = ap.assign(due_date=ap.due_date + pd.to_timedelta(ap.max_extension_days, "D"))
op2 = op[op.discretionary.eq("N")]
o2 = o.assign(expected=o.expected.where(o.customer.ne(top), o.due_date))
op3 = op.assign(week=op.week.where(op.customer.ne(top), op.week_raw))
alts = {"base": base,
        "revolver": forecast(o, ap, op, {low[0]: cap}),
        "accelerate": forecast(o2, ap, op3),
        "defer": forecast(o, ap, op2),
        "stretch": forecast(o, ap2, op),
        "defer+stretch": forecast(o, ap2, op2)}
cmp = pd.DataFrame({k: {"trough": f.close.min(), "weeks_below_min": (f.close < MIN).sum(), "week13": f.close.iloc[-1]} for k, f in alts.items()}).T
cmp["gain_at_trough"] = cmp.trough - cmp.trough["base"]
cmp["cost"] = 0.0
cmp.loc["revolver", "cost"] = cap * r.interest_rate * (14 - low[0]) / 52
ost = o.assign(expected=o.expected + pd.to_timedelta(14 * o.customer.eq(top), "D"))
ops = op2.assign(week=op2.week + 2 * op2.customer.eq(top))
spre = forecast(ost, ap2, ops)
print("stress: Northwind 14 more days late, with defer + stretch | trough:", round(spre.close.min()), "in week", spre.close.idxmin(), "| without stretch:", round(forecast(ost, ap, ops).close.min()))
cmp.round(0)
# %% 7
w = (spre.close < MIN).idxmax()
draw = np.ceil((MIN - spre.close.min()) / 25000) * 25000
plan = forecast(o, ap2, op2, {w: draw})
stress = forecast(ost, ap2, ops, {w: draw})
print(w, draw, draw <= cap, plan.close.min().round(), stress.close.min().round())
# %% 8
ar["expected_date"] = o.expected
ar["in_forecast"] = ar.index.isin(o[o.collect].index)
b.to_csv("bank_transactions.csv", index=False)
ar.to_csv("accounts_receivable.csv", index=False)
ap.assign(due_date_raw=ap.due_date, due_date=ap2.due_date).to_csv("accounts_payable.csv", index=False)
op.assign(deferred=op.discretionary.eq("Y")).to_csv("operating_forecast.csv", index=False)
pd.concat({"base": base, "plan": plan, "stress": stress}, names=["scenario", "week"]).round(2).to_csv("liquidity_forecast_13w.csv")
cmp.round(2).to_csv("scenario_comparison.csv")
log = pd.DataFrame({"action": ["defer discretionary spend", "stretch non-critical suppliers", f"revolver draw in week {w}", f"accelerate {top}", "revolver alone"],
                    "decision": ["accepted", "accepted", "accepted", "rejected", "rejected"],
                    "usd": [-op[op.discretionary.eq("Y")].amount.sum(), ap.amount[ap.max_extension_days > 0].sum(), draw, cmp.gain_at_trough["accelerate"], cap],
                    "basis": ["capex and marketing moved past week 13, no cost", "only non-critical bills, within agreed max_extension_days", f"sized to the stress case, below real capacity {cap:,.0f}",
                              f"recent delay {delay[top]} days, no evidence it reverses", "uses all capacity, no buffer for stress"]})
log.to_csv("financing_plan.csv", index=False)
print(log, "\nleverage after draw:", round((debt.drawn.sum() + draw) / r.ltm_ebitda, 2), "| unused capacity:", cap - draw, "| interest cost:", round(draw * r.interest_rate * (14 - w) / 52))
ax = pd.DataFrame({"base": base.close, "plan": plan.close, "stress": stress.close}).plot(marker="o", title="Unrestricted cash, 13 weeks")
ax.axhline(MIN, color="red", ls="--")
