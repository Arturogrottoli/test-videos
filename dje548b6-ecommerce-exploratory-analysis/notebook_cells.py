# E-commerce Exploratory Data Analysis (task dje548b6) — notebook cells for Google Colab.
# Each "# %%" block is one Colab code cell, in the same order as README.md.
# It also runs as a normal script: python notebook_cells.py

# %% Cell 1 — Load the data (steps 3 and 4)
import pandas as pd
import matplotlib.pyplot as plt

url = "https://datanemics.com/datasets/data/retail-orders.csv"
df = pd.read_csv(url)
# If the link fails, upload the CSV to Colab and use this line instead:
# df = pd.read_csv("retail-orders.csv")
print(df.head())

# %% Cell 2 — Explore the data (step 5)
print("Rows and columns:", df.shape)
print("Columns:", df.columns.tolist())
print(df.dtypes)

# %% Cell 3 — Convert dates and check missing values (steps 6 and 7)
df["ordered_at"] = pd.to_datetime(df["ordered_at"])
print("From", df["ordered_at"].min(), "to", df["ordered_at"].max())
print(df["ordered_at"].dtype)
print(df.isna().sum())

# %% Cell 4 — Chart 1: revenue by category (step 9)
by_category = df.groupby("category")["revenue_usd"].sum().sort_values(ascending=False)
print(by_category)

by_category.plot(kind="bar", color="steelblue", rot=0)
plt.title("Total Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue (USD)")
plt.tight_layout()
plt.show()

# %% Cell 5 — Chart 2: monthly revenue (step 9)
monthly = df.groupby(df["ordered_at"].dt.to_period("M"))["revenue_usd"].sum()
print(monthly)

monthly.plot(kind="line", marker="o")
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (USD)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# %% Cell 6 — Chart 3: revenue per order line (step 9)
print(df["revenue_usd"].describe())

df["revenue_usd"].plot(kind="hist", bins=50, color="seagreen", edgecolor="white")
plt.title("Distribution of Revenue per Order Line")
plt.xlabel("Revenue per order line (USD)")
plt.ylabel("Number of order lines")
plt.tight_layout()
plt.show()
