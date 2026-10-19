# Sales Data Analysis and Business Insights

A beginner-friendly data analysis project in **Google Colab**, using **Python**, **pandas**, and **Matplotlib**. You upload a synthetic sales dataset, clean it, calculate key business metrics, find the best-selling products and the sales trend over the year, and create three charts.

Colab already includes pandas and Matplotlib, so there is **nothing to install**.

---

## Business problem and objectives

A small company that sells electronics, furniture, and office supplies wants to understand its sales from last year. Managers want simple answers to these questions:

1. How much revenue did we make, and how many units did we sell?
2. How many orders did we get, and what is the average order value?
3. Which products and categories bring in the most money?
4. Are sales growing, shrinking, or flat during the year?

**Objectives**

- Check the quality of the raw data and fix common problems (duplicates, missing values, wrong data types).
- Calculate the key metrics above.
- Show the results in clear charts that a non-technical audience can read.
- Save a clean version of the data.

---

## Technologies used

| Tool | Purpose |
| ---- | ------- |
| Google Colab | Free online notebook that runs Python in the browser |
| pandas | Loading, cleaning, and analyzing tabular data |
| Matplotlib | Creating and saving charts |

---

## Project structure

```
pandas/
├── README.md        ← this file
└── sales_data.csv   ← raw synthetic dataset
```

The notebook is written in Colab during the session. Running it creates these files in Colab's **Files** panel:

```
cleaned_sales_data.csv
charts/
├── revenue_by_product.png
├── revenue_by_category.png
└── monthly_revenue.png
```

Colab deletes uploaded and created files when the session ends. To keep them, right-click each file in the **Files** panel and choose **Download**.

---

## Dataset description

`sales_data.csv` is a **synthetic** dataset: it was generated for practice and does not contain real customers, people, or companies. It has **205 rows** of orders from January to December 2025, sold in four regions.

To practice data cleaning, the file **intentionally** contains:

- **5 duplicate rows** (exact copies of another order)
- **9 missing values**: 4 in `region`, 3 in `unit_price`, and 2 in `quantity`

### Column definitions

| Column | Type | Description |
| ------ | ---- | ----------- |
| `order_id` | text | Unique order ID, for example `ORD-1001` |
| `order_date` | date | Date of the order, in `YYYY-MM-DD` format |
| `product` | text | Laptop, Headphones, Wireless Mouse, Office Chair, Standing Desk, Notebook Pack, or Pen Set |
| `category` | text | Electronics, Furniture, or Office Supplies |
| `quantity` | number | Units sold in the order |
| `unit_price` | number | Price of one unit, in US dollars |
| `region` | text | North, South, East, or West |

The analysis adds one more column:

| Column | Type | Description |
| ------ | ---- | ----------- |
| `revenue` | number | `quantity * unit_price` |

---

## How to run it in Colab

1. Open https://colab.research.google.com and sign in with a Google account.
2. Click **New notebook**.
3. Click the folder icon (**Files**) on the left, then **Upload to session storage**, and choose `sales_data.csv`.
4. Type each cell from [The notebook, cell by cell](#the-notebook-cell-by-cell) and run it with `Shift + Enter`.

---

## The notebook, cell by cell

### Cell 1 — Load the data

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")
df.head()
```

### Cell 2 — Size, columns, and data types

```python
print("Rows and columns:", df.shape)
print("Columns:", df.columns.tolist())
df.dtypes
```

### Cell 3 — Check data quality

```python
print("Missing values per column:")
print(df.isna().sum())
print("Duplicate rows:", df.duplicated().sum())
```

### Cell 4 — Clean the data

```python
df = df.drop_duplicates()

df["order_date"] = pd.to_datetime(df["order_date"])
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")

df["region"] = df["region"].fillna("Unknown")
product_price = df.groupby("product")["unit_price"].transform("median")
df["unit_price"] = df["unit_price"].fillna(product_price)
df = df.dropna(subset=["quantity"])
df["quantity"] = df["quantity"].astype(int)

print("Rows after cleaning:", len(df))
print("Missing values left:", df.isna().sum().sum())
```

### Cell 5 — Revenue and key metrics

```python
df["revenue"] = df["quantity"] * df["unit_price"]

total_revenue = df["revenue"].sum()
total_units = df["quantity"].sum()
orders = df["order_id"].nunique()
average_order = total_revenue / orders

print(f"Total revenue: ${total_revenue:,.2f}")
print(f"Total units sold: {total_units}")
print(f"Number of orders: {orders}")
print(f"Average order value: ${average_order:,.2f}")
```

### Cell 6 — Revenue by product, category, and month

```python
by_product = df.groupby("product")["revenue"].sum().sort_values(ascending=False)
by_category = df.groupby("category")["revenue"].sum().sort_values(ascending=False)
monthly = df.groupby(df["order_date"].dt.strftime("%Y-%m"))["revenue"].sum()

print(by_product, "\n")
print(by_category, "\n")
print(monthly)
```

### Cell 7 — Chart: revenue by product

```python
import os
os.makedirs("charts", exist_ok=True)

by_product.plot(kind="bar", title="Revenue by Product", color="steelblue", rot=30)
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig("charts/revenue_by_product.png")
plt.show()
```

### Cell 8 — Chart: revenue by category

```python
by_category.plot(kind="bar", title="Revenue by Category", color="seagreen", rot=0)
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig("charts/revenue_by_category.png")
plt.show()
```

### Cell 9 — Chart: monthly revenue trend

```python
monthly.plot(kind="line", marker="o", title="Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.xticks(range(len(monthly)), monthly.index, rotation=45)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("charts/monthly_revenue.png")
plt.show()
```

### Cell 10 — Save the cleaned data

```python
df.to_csv("cleaned_sales_data.csv", index=False)
print("Saved cleaned_sales_data.csv")
```

---

## Data cleaning steps

| Step | Problem | What the code does | Why |
| ---- | ------- | ------------------ | --- |
| 1 | Duplicate rows | `drop_duplicates()` removes exact copies | The same order should only be counted once |
| 2 | Dates stored as text | `pd.to_datetime()` converts `order_date` | So we can group by month |
| 3 | Numbers with gaps | `pd.to_numeric(errors="coerce")` converts `quantity` and `unit_price` | Guarantees numeric columns; bad values become missing |
| 4 | Missing `region` | Filled with `"Unknown"` | We can't guess the region, but the order is still valid |
| 5 | Missing `unit_price` | Filled with the median price of the same product | Each product has one fixed price in this dataset |
| 6 | Missing `quantity` | The order is removed | We can't know how many items were sold, and guessing would distort revenue |

---

## Key metrics and analysis performed

- **Total revenue:** sum of `revenue`
- **Total units sold:** sum of `quantity`
- **Number of orders:** number of unique `order_id` values
- **Average order value:** total revenue ÷ number of orders
- **Revenue by product** and **by category:** `groupby`, sorted from highest to lowest
- **Monthly revenue:** revenue grouped by year and month (`YYYY-MM`)

---

## Charts generated

| File | Chart | Question it answers |
| ---- | ----- | ------------------- |
| `charts/revenue_by_product.png` | Bar chart | Which products make the most money? |
| `charts/revenue_by_category.png` | Bar chart | Which categories make the most money? |
| `charts/monthly_revenue.png` | Line chart | How did revenue change during the year? |

---

## Example findings (illustrative)

> **Illustrative only.** These numbers come from one test run of the cells above on the included `sales_data.csv`. Run the notebook yourself and use **your** output as the source of truth. If you change the dataset, these numbers will change.

- After cleaning, 198 of the 205 rows remain: 5 duplicates and 2 orders without a quantity were removed.
- Total revenue was about **$36,986** from **812 units** in **198 orders**, an average order value of about **$186.80**.
- **Laptop** was the top product (about $8,500), followed by **Standing Desk** (about $7,700). **Pen Set** was the lowest (about $1,992).
- **Electronics** brought in about half of the revenue (about $18,355), then **Furniture** (about $13,460) and **Office Supplies** (about $5,171).
- Monthly revenue grew strongly during the year, from about $349 in January to about $6,904 in December, with small dips in March and October.

Note: depending on the pandas version, text columns show the data type `object` or `str`. Both are fine.

---

## Limitations and possible future improvements

**Limitations**

- The data is synthetic and small (about 200 orders), so the results are for practice, not for real decisions.
- Removing orders with a missing quantity loses a little revenue. A real project would try to recover that data from the source system.
- Each row is treated as one order with one product. Real orders often contain many products.
- There are no costs in the data, so we can measure revenue but not profit.

**Future improvements**

- Analyze revenue by region and by region over time.
- Find the best and worst months and compare quarters.
- Add costs to calculate profit and margin.
- Use a larger, real (anonymized) dataset.

---

## Recording guide (15–20 minutes)

A step-by-step walkthrough for a screen recording in Google Colab. Each step says **what to do** and **what to say**. Times are approximate.

### Before you record

1. Sign in to your Google account in the browser.
2. Keep `sales_data.csv` somewhere easy to find, like your Desktop.
3. Zoom in the browser so the code is easy to read (`Ctrl + +`, or `Cmd + +` on a Mac).
4. Do one full practice run in a separate notebook.

---

### Step 1 — Introduction (about 1 minute)

**Do:** Show https://colab.research.google.com.

**Say:**

> Hi everyone! Today we're going to analyze a year of sales data with Python, using two very popular libraries: pandas, for working with tables of data, and Matplotlib, for charts.
>
> Imagine a small company that sells electronics, furniture, and office supplies. The managers want to know four things: how much money they made, how many orders they got, which products sell best, and whether sales are growing. We'll answer all four questions, and we'll create charts to show the results.
>
> We'll use Google Colab, which runs Python in the browser for free. pandas and Matplotlib are already installed, so there's nothing to set up.

---

### Step 2 — Create the notebook and upload the data (about 2 minutes)

**Do:** Click **New notebook**. Rename it to `sales_analysis.ipynb` (click the name at the top left). Open the **Files** panel, click **Upload to session storage**, and choose `sales_data.csv`. Click **OK** on the warning.

**Say:**

> I'll create a new notebook and call it "sales_analysis". A notebook is made of cells. We write code in a cell, run it, and the result appears right below.
>
> Now I'll upload our dataset. I'll open the Files panel on the left and upload sales_data.csv. Colab warns us that uploaded files are deleted when the session ends. That's fine for today.
>
> This is synthetic data. It was generated for practice, so there's no real customer information. It has about 200 orders from 2025, with seven columns: an order ID, the date, the product, its category, the quantity, the unit price, and the region.

---

### Step 3 — Load the data (cell 1, about 1.5 minutes)

**Do:** Type cell 1 and press `Shift + Enter`.

**Say:**

> In the first cell, we import pandas as "pd", which is the usual short name, and Matplotlib for the charts.
>
> "read_csv" loads our file into a DataFrame. A DataFrame is like a spreadsheet inside Python, with rows and columns. And "head" shows the first five rows, so we can check that everything loaded correctly.

---

### Step 4 — Size, columns, and types (cell 2, about 1.5 minutes)

**Do:** Type cell 2 and run it.

**Say:**

> Next, let's get to know our data. "shape" tells us how many rows and columns we have. Then we list the column names. And "dtypes" shows the data type of each column.
>
> Look at the order date. pandas sees it as text, not as a date. We'll fix that during cleaning.

---

### Step 5 — Check data quality (cell 3, about 1.5 minutes)

**Do:** Type cell 3 and run it.

**Say:**

> Before doing any math, we always check the quality of the data, because dirty data gives wrong answers.
>
> "isna().sum()" counts the missing values in each column. We have some missing quantities, prices, and regions. And "duplicated().sum()" counts the rows that are exact copies of another row. We have a few of those too.

---

### Step 6 — Clean the data (cell 4, about 3 minutes)

**Do:** Type cell 4 slowly, one block at a time, and run it.

**Say:**

> Now the cleaning. This is where a lot of real data work happens.
>
> First, "drop_duplicates" removes the copied rows, so we don't count the same order twice.
>
> Then we fix the data types. "to_datetime" turns the date text into real dates, so we can group by month later. "to_numeric" makes sure quantity and price are numbers.
>
> Now the missing values. Each column needs a different decision.
>
> If the region is missing, we don't know it, but the sale still happened. So we fill it with the word "Unknown".
>
> If the unit price is missing, we can fix it, because each product always has the same price. So we fill it with the usual price of that product.
>
> But if the quantity is missing, we can't know how many items were sold. Guessing would make our revenue wrong. So we remove those orders.
>
> Let's run it. We can see how many rows are left, and zero missing values. Our data is clean.

---

### Step 7 — Revenue and key metrics (cell 5, about 2 minutes)

**Do:** Type cell 5 and run it.

**Say:**

> Now we can answer our business questions. First, we create a new column, revenue, which is quantity times unit price. pandas calculates it for every row at once.
>
> Total revenue is the sum of that column. Total units is the sum of quantity. The number of orders counts the unique order IDs. And the average order value is the total revenue divided by the number of orders.
>
> Let's run it, and here are our four key numbers.

---

### Step 8 — Revenue by product, category, and month (cell 6, about 2 minutes)

**Do:** Type cell 6 and run it.

**Say:**

> Now let's dig deeper with "groupby". It groups rows that share a value, and then adds them up.
>
> We group by product to see which products make the most money, and by category to see which part of the business is strongest. We sort both from highest to lowest, so the winners come first.
>
> And we group by month, using the date we fixed during cleaning, to see how sales changed over the year.

---

### Step 9 — The charts (cells 7 to 9, about 3 minutes)

**Do:** Type and run cells 7, 8, and 9, one at a time. After each one, look at the chart.

**Say:**

> Numbers are useful, but charts are easier to understand. First, we create a folder called "charts" to save our images.
>
> Our first chart is a bar chart of revenue by product. We add a title and a label for the vertical axis, "savefig" saves it as an image, and "show" displays it here. The tallest bars are our best sellers.
>
> The second chart shows revenue by category, which tells us which part of the business brings in the most money.
>
> And the third one is a line chart of revenue by month. This shows the trend over the year: we can see right away if sales are going up or down.

---

### Step 10 — Save the cleaned data (cell 10, about 1 minute)

**Do:** Type cell 10 and run it. Open the **Files** panel and show `cleaned_sales_data.csv` and the `charts` folder. Right-click one file and show **Download**.

**Say:**

> Finally, we save our clean data to a new CSV file, so we, or anyone on the team, can reuse it without cleaning it again.
>
> In the Files panel, we can see our cleaned file and the charts folder. To keep them, right-click and choose Download.

---

### Step 11 — Business insights and conclusion (about 2 minutes)

**Do:** Scroll back to the metrics and the charts.

**Say** (replace the words in brackets with your real results):

> So, what did we learn? The company made [total revenue] from [number of orders] orders, with an average order value of [average order value].
>
> The top product was [top product], and the top category was [top category]. And over the year, monthly revenue [describe the trend, for example: grew from January to December].
>
> For the business, this suggests focusing on the products that bring in the most money, and understanding what drove the trend during the year.
>
> And from the technical side, we practiced the full workflow: loading data, checking its quality, cleaning it, calculating metrics with groupby, and sharing the results with charts. You can use the same steps with your own data.
>
> Thanks for watching!
