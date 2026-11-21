"""Synthetic inputs for oyi436dd - E-commerce Financial Reconstruction (Q4 2025).

Writes orders.csv, payments.csv, refunds.csv, products.csv, processor_terms.csv
into the parent folder. Planted issues (all counted at the end):
  - exact duplicate order rows (export error)
  - failed payment attempts (retried, or never recovered)
  - orders with no payment record at all
  - captures whose amount differs from the order total
  - captures that reference an order id that does not exist
  - captures not yet paid out at period end (pending)
  - payouts short of the expected net (processor adjustments)
  - refunds: partial, full, over-refunded, and refunds with bad payment refs
  - products without a unit cost
"""
from pathlib import Path
import numpy as np
import pandas as pd

rng = np.random.default_rng(436)
OUT = Path(__file__).resolve().parent.parent
END = pd.Timestamp("2025-12-31")

products = pd.DataFrame([
    ("P001", "Chef Knife Set", "Kitchen", 89.0, 44.99), ("P002", "Cast Iron Skillet", "Kitchen", 34.0, 15.13),
    ("P003", "Pour-Over Kettle", "Kitchen", 79.0, 48.17), ("P004", "Bamboo Cutting Board", "Kitchen", 99.0, 61.09),
    ("P005", "Spice Rack", "Kitchen", 69.0, 36.31), ("P006", "Linen Throw", "Home", 39.0, 16.44),
    ("P007", "Ceramic Vase", "Home", 39.0, 21.49), ("P008", "Scented Candle Trio", "Home", 99.0, 60.48),
    ("P009", "Wall Clock", "Home", 45.0, 23.63), ("P010", "Storage Baskets", "Home", 129.0, 74.72),
    ("P011", "Camping Lantern", "Outdoor", 99.0, 55.32), ("P012", "Insulated Bottle", "Outdoor", 39.0, 20.77),
    ("P013", "Folding Chair", "Outdoor", 99.0, 58.23), ("P014", "Picnic Blanket", "Outdoor", 19.0, 10.90),
    ("P015", "Garden Tool Kit", "Outdoor", 45.0, 23.06), ("P016", "Wireless Earbuds", "Tech", 49.0, 28.15),
    ("P017", "USB-C Hub", "Tech", 79.0, np.nan), ("P018", "Phone Stand", "Tech", 39.0, 17.43),
    ("P019", "Bluetooth Speaker", "Tech", 45.0, 20.10), ("P020", "Desk Lamp", "Tech", 29.0, 15.55),
    ("P021", "Yoga Mat", "Fitness", 59.0, 27.43), ("P022", "Resistance Bands", "Fitness", 24.0, np.nan),
    ("P023", "Foam Roller", "Fitness", 129.0, 54.24), ("P024", "Jump Rope", "Fitness", 45.0, 19.65),
    ("P025", "Kettlebell 12kg", "Fitness", 24.0, 12.16),
], columns=["product_id", "product_name", "category", "unit_price", "unit_cost"])
price = products.set_index("product_id").unit_price
costed = products[products.unit_cost.notna()].product_id.tolist()

terms = pd.DataFrame({
    "method": ["card", "wallet", "bank_transfer"],
    "fee_pct": [0.029, 0.0349, 0.008],
    "fee_fixed": [0.30, 0.49, 0.00],
    "payout_days": [2, 1, 3],
})
T = terms.set_index("method")

# ---------- orders ----------
N = 1150
days = pd.to_datetime(rng.integers(0, 92, N), unit="D", origin=pd.Timestamp("2025-10-01"))
days = days.sort_values()
orders = pd.DataFrame({
    "order_id": [f"O{80001 + i}" for i in range(N)],
    "customer_id": [f"C{x:04d}" for x in rng.integers(1, 420, N)],
    "order_date": days.strftime("%Y-%m-%d"),
    "product_id": rng.choice(products.product_id, N),
    "quantity": rng.choice([1, 1, 1, 2, 2, 3], N),
})
# no-cost products are not sold in the last week (keeps one issue per row)
late = days > pd.Timestamp("2025-12-24")
orders.loc[late & ~orders.product_id.isin(costed), "product_id"] = rng.choice(costed, (late & ~orders.product_id.isin(costed)).sum())
orders["order_total"] = (orders.quantity * orders.product_id.map(price)).round(2)

# special cases are drawn from costed, non-late orders so each row has a single issue
pool = orders.index[~late & orders.product_id.isin(costed)].to_numpy().copy()
rng.shuffle(pool)
never_paid = pool[:6]           # no payment record at all
only_failed = pool[6:16]        # failed attempts, never captured
amount_diff = pool[16:24]       # captured amount != order total
short_paid = pool[24:30]        # payout short of expected net
retried = pool[30:120]          # failed first, then captured OK
refund_pool = pool[120:]

# ---------- payments ----------
rows = []
pid = 300001
def stamp(day):
    return (pd.Timestamp(day) + pd.Timedelta(minutes=int(rng.integers(8 * 60, 22 * 60)))).strftime("%Y-%m-%d %H:%M")

for i, od in orders.iterrows():
    if i in never_paid:
        continue
    method = rng.choice(["card", "wallet", "bank_transfer"], p=[0.7, 0.2, 0.1])
    when = stamp(od.order_date)
    if i in only_failed or i in retried:
        for _ in range(1 if i in retried else rng.integers(1, 3)):
            rows.append(dict(payment_id=f"PAY{pid}", order_id=od.order_id, method=method,
                             amount=od.order_total, status="failed", created_at=when))
            pid += 1
        if i in only_failed:
            continue
    amt = od.order_total
    if i in amount_diff:
        amt = round(amt * rng.choice([0.9, 0.85, 1.1]), 2)
    rows.append(dict(payment_id=f"PAY{pid}", order_id=od.order_id, method=method,
                     amount=amt, status="captured", created_at=when if i not in retried else (pd.Timestamp(when) + pd.Timedelta(minutes=int(rng.integers(3, 15)))).strftime("%Y-%m-%d %H:%M"), _short=i in short_paid))
    pid += 1

# captures whose order id is not in orders.csv
for j in range(5):
    day = pd.Timestamp("2025-10-05") + pd.Timedelta(days=int(rng.integers(0, 75)))
    rows.append(dict(payment_id=f"PAY{pid}", order_id=f"O{89001 + j}", method="card",
                     amount=float(rng.choice([39.0, 45.0, 99.0, 129.0])), status="captured", created_at=stamp(day)))
    pid += 1

pay = pd.DataFrame(rows).sort_values(["created_at", "payment_id"]).reset_index(drop=True)
pay["_short"] = pay["_short"].fillna(False).astype(bool)
cap = pay.status.eq("captured")
fee = (pay.amount * pay.method.map(T.fee_pct) + pay.method.map(T.fee_fixed)).round(2)
pdate = pd.to_datetime(pay.created_at).dt.normalize() + pd.to_timedelta(pay.method.map(T.payout_days), "D")
paid_out = cap & (pdate <= END)
pay["payout_id"] = np.where(paid_out, "PO-" + pdate.dt.strftime("%Y%m%d"), None)
pay["settled"] = np.where(paid_out, (pay.amount - fee).round(2), np.nan)
adj = rng.choice([12.50, 15.00, 25.00, 7.80, 18.40, 30.00], pay._short.sum(), replace=False)
pay.loc[pay._short, "settled"] = (pay.loc[pay._short, "settled"] - adj).round(2)
payments = pay.drop(columns="_short")

# ---------- refunds ----------
cappay = payments[cap].set_index("order_id")
cand = orders.loc[refund_pool, "order_id"]
cand = cand[cand.isin(cappay.index) & cappay.reindex(cand).payout_id.notna().to_numpy()]
picked = cand.sample(70, random_state=7)
ref = []
for k, oid in enumerate(picked):
    pr = cappay.loc[oid]
    full = k % 5 < 3
    amt = pr.amount if full else round(pr.amount * float(rng.choice([0.2, 0.25, 0.3, 0.5])), 2)
    day = pd.Timestamp(pr.created_at[:10]) + pd.Timedelta(days=int(rng.integers(2, 20)))
    ref.append(dict(payment_id=pr.payment_id, amount=amt, refund_date=min(day, END).strftime("%Y-%m-%d")))
    if k < 2:  # full refund issued twice -> over-refund
        ref.append(dict(payment_id=pr.payment_id, amount=pr.amount,
                        refund_date=min(day + pd.Timedelta(days=3), END).strftime("%Y-%m-%d")))
failed_ids = payments[payments.status.eq("failed")].payment_id.sample(2, random_state=3)
for f in failed_ids:  # refunds pointing at a failed attempt
    ref.append(dict(payment_id=f, amount=float(payments.set_index("payment_id").amount[f]), refund_date="2025-11-18"))
for f, a in [("PAY399120", 45.0), ("PAY399377", 29.0)]:  # ids that do not exist
    ref.append(dict(payment_id=f, amount=a, refund_date="2025-12-09"))
refunds = pd.DataFrame(ref).sort_values("refund_date", kind="stable").reset_index(drop=True)
refunds.insert(0, "refund_id", [f"RF{6001 + i}" for i in range(len(refunds))])

# ---------- duplicate export rows ----------
dups = orders.sample(30, random_state=11)
orders_out = pd.concat([orders, dups]).sort_values(["order_date", "order_id"], kind="stable").reset_index(drop=True)

orders_out.to_csv(OUT / "orders.csv", index=False)
payments.to_csv(OUT / "payments.csv", index=False)
refunds.to_csv(OUT / "refunds.csv", index=False)
products.to_csv(OUT / "products.csv", index=False)
terms.to_csv(OUT / "processor_terms.csv", index=False)

print("orders", orders_out.shape, "payments", payments.shape, "refunds", refunds.shape)
print("pending captures:", (cap & ~paid_out).sum(), "| short payouts:", pay._short.sum())
