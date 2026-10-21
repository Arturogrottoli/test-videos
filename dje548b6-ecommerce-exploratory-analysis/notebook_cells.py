# E-commerce Exploratory Data Analysis (task dje548b6) — same cells as ecommerce_eda.ipynb.
# Each "# %%" block is one Colab code cell. Run it with: python notebook_cells.py

# %% Cell 1
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://datanemics.com/datasets/data/retail-orders.csv")
print(df.head())

# %% Cell 2
print(df.shape)
df.info()

# %% Cell 3
df["ordered_at"] = pd.to_datetime(df["ordered_at"])
print(df.isna().sum())

# %% Cell 4
by_category = df.groupby("category")["revenue_usd"].sum().sort_values(ascending=False)
by_category.plot(kind="bar", title="Revenue by Category", xlabel="Category", ylabel="Revenue (USD)", rot=0)
plt.show()

# %% Cell 5
monthly = df.groupby(df["ordered_at"].dt.to_period("M"))["revenue_usd"].sum()
monthly.plot(marker="o", title="Monthly Revenue", xlabel="Month", ylabel="Revenue (USD)")
plt.show()

# %% Cell 6
df["revenue_usd"].plot(kind="hist", bins=50, title="Revenue per Order Line")
plt.xlabel("Revenue (USD)")
plt.show()
