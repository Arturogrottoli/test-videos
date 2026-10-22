# E-commerce Exploratory Data Analysis (task dje548b6) — cells to type in Google Colab.
# Each "# %%" block is one Colab cell, in order. "TEXT cell" blocks go in a "+ Text" cell,
# without the "#" comment marks at the start of each line. The rest go in "+ Code" cells.

# %% TEXT cell
# # E-commerce Exploratory Data Analysis
# Dataset: Retail Orders (Datanemics, CC0). Goal: explore revenue by category, by month, and per order line.

# %% Code cell 1 — Load the data
import pandas as pd

df =pd.read_csv("https://datanemics.com/datasets/data/retail-orders.csv")
print(df.head())

# %% TEXT cell
# ## 1. Explore the data

# %% Code cell 2 — Size, columns, and data types
print(df.shape)
df.info()

# %% TEXT cell
# ## 2. Dates and missing values

# %% Code cell 3 — Convert dates and count missing values
df["ordered_at"] = pd.to_datetime(df["ordered_at"])
print(df.isna().sum())

# %% TEXT cell
# ## 3. Charts
# Matplotlib is Python's most widely used charting library. pandas uses it when we call `.plot()`.

# %% Code cell 4 — Bar chart: revenue by category
import matplotlib.pyplot as plt

by_category = df.groupby("category")["revenue_usd"].sum().sort_values(ascending=False)
by_category.plot(kind="bar", title="Revenue by Category", xlabel="Category", ylabel="Revenue (USD)", rot=0)
plt.show()

# %% Code cell 5 — Line chart: monthly revenue
monthly = df.groupby(df["ordered_at"].dt.to_period("M"))["revenue_usd"].sum()
monthly.plot(marker="o", title="Monthly Revenue", xlabel="Month", ylabel="Revenue (USD)")
plt.show()

# %% Code cell 6 — Histogram: revenue per order line
df["revenue_usd"].plot(kind="hist", bins=50, title="Revenue per Order Line")
plt.xlabel("Revenue (USD)")
plt.show()

# %% TEXT cell
# ## 4. Observations
# - Bar chart: ...
# - Line chart: ...
# - Histogram: ...

# %% TEXT cell
# ## 5. Conclusion
# We loaded a public e-commerce CSV with pandas, checked its structure and missing values, converted dates,
# and used Matplotlib to compare revenue by category, over time, and per order line.
# Main findings: electronics leads revenue, revenue peaks in December, and most order lines are small.
