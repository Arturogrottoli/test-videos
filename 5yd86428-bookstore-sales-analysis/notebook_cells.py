# Bookstore Sales Analysis — notebook cells for Google Colab.
# Each "# %%" block is one Colab code cell. Paste them in order.
# Markdown cells (title and conclusions) are described in README.md.

# %% Cell 1 — Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% Cell 2A — OPTION A: upload a provided sales_data.csv (Colab only)
# Use this cell INSTEAD of Cell 2B if the task gives you the CSV.
# from google.colab import files
# uploaded = files.upload()

# %% Cell 2B — OPTION B: generate the synthetic dataset
rng = np.random.default_rng(42)
n = 200
categories = ["Fiction", "Non-Fiction", "Science", "Children", "History"]
price_range = {
    "Fiction": (8, 20),
    "Non-Fiction": (10, 25),
    "Science": (15, 40),
    "Children": (5, 15),
    "History": (12, 30),
}

dates = pd.to_datetime("2024-01-01") + pd.to_timedelta(rng.integers(0, 366, n), unit="D")
cats = rng.choice(categories, n)
titles = [f"{c} Book {rng.integers(1, 11)}" for c in cats]
units = rng.integers(1, 11, n)
prices = np.array([round(rng.uniform(*price_range[c]), 2) for c in cats])

sales = pd.DataFrame({
    "date": dates.date,
    "category": cats,
    "title": titles,
    "units_sold": units,
    "unit_price": prices,
})
sales["total_revenue"] = (sales["units_sold"] * sales["unit_price"]).round(2)
sales = sales.sort_values("date").reset_index(drop=True)
sales.to_csv("sales_data.csv", index=False)

# %% Cell 3 — Load and inspect
df = pd.read_csv("sales_data.csv", parse_dates=["date"])
print(df.shape)
df.head()

# %% Cell 4 — Column types
df.info()

# %% Cell 5 — Data quality checks
print("Missing values:\n", df.isna().sum())
print("Duplicate rows:", df.duplicated().sum())
print(
    "Revenue matches units x price:",
    np.isclose(df["units_sold"] * df["unit_price"], df["total_revenue"], atol=0.01).all(),
)

# %% Cell 6 — Descriptive statistics
df[["units_sold", "unit_price", "total_revenue"]].describe().round(2)

# %% Cell 7 — Sales by category
by_category = (
    df.groupby("category")
    .agg(
        transactions=("title", "count"),
        units=("units_sold", "sum"),
        revenue=("total_revenue", "sum"),
    )
    .sort_values("revenue", ascending=False)
    .round(2)
)
by_category

# %% Cell 8 — Sales by month
df["month"] = df["date"].dt.to_period("M")
by_month = (
    df.groupby("month")
    .agg(transactions=("title", "count"), revenue=("total_revenue", "sum"))
    .round(2)
)
by_month

# %% Cell 9 — Bar charts
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

by_category["revenue"].plot(kind="bar", ax=axes[0], color="steelblue")
axes[0].set_title("Total Revenue by Category")
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Revenue")
axes[0].tick_params(axis="x", rotation=45)

by_month["revenue"].plot(kind="bar", ax=axes[1], color="darkorange")
axes[1].set_title("Total Revenue by Month")
axes[1].set_xlabel("Month")
axes[1].set_ylabel("Revenue")
axes[1].tick_params(axis="x", rotation=45)

plt.tight_layout()
plt.show()

# %% Cell 10 — Histograms
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

df["total_revenue"].plot(kind="hist", bins=20, ax=axes[0], edgecolor="black")
axes[0].set_title("Distribution of Total Revenue per Transaction")
axes[0].set_xlabel("Total Revenue")

df["units_sold"].plot(kind="hist", bins=10, ax=axes[1], edgecolor="black")
axes[1].set_title("Distribution of Units Sold")
axes[1].set_xlabel("Units Sold")

plt.tight_layout()
plt.show()

# %% Cell 11 — Outliers with the IQR method
q1 = df["total_revenue"].quantile(0.25)
q3 = df["total_revenue"].quantile(0.75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
outliers = df[(df["total_revenue"] < lower) | (df["total_revenue"] > upper)]

print(f"Q1: {q1:.2f}, Q3: {q3:.2f}, IQR: {iqr:.2f}")
print(f"Lower bound: {lower:.2f}, Upper bound: {upper:.2f}")
print(f"Outliers found: {len(outliers)}")
outliers.sort_values("total_revenue", ascending=False)

# %% Cell 12 — Download the CSV (Colab only; only needed if you generated it)
# from google.colab import files
# files.download("sales_data.csv")
