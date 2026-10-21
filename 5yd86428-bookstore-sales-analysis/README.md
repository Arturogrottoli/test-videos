# 5yd86428 — Bookstore Sales Analysis

Recording script for analyzing 200 synthetic bookstore transactions in **Google Colab**: load and inspect `sales_data.csv`, compute descriptive statistics, group sales by category and month, draw bar charts and histograms, detect outliers with the IQR method, and write conclusions.

**Registered deliverables:** the notebook (`.ipynb`) and the CSV file (`sales_data.csv`).

## How to use this script

Each step has four parts:

- **On screen**: what you do.
- **Say**: the exact narration. Values in `[brackets]` are read from the screen at that moment. Never say a number you have not seen on screen.
- **Check**: what must be visible before you move on.
- **Pause**: when to stop talking and let the screen speak.

## Files in this folder

| File | Purpose |
| ---- | ------- |
| `README.md` | This script |
| `notebook_cells.py` | Every code cell, in order (`# %% Cell N`). Paste each block into its own Colab cell. |

The CSV is **not** included on purpose. Cell 2B generates it on camera with a fixed seed (`42`), so the same 200 rows come out every time.

### Pre-test (not for narration)

I ran all the code cells locally (Python 3.14 with pandas, without the Colab-only cells) and they finished without errors. Colab may have different library versions. During the recording, read only what your own screen shows.

## Missing information (check the original task before recording)

- Required video length: not confirmed.
- Recording rules (camera, microphone, resolution, single take, edits allowed): not confirmed.
- AutoQC requirements: not confirmed.
- **Whether `sales_data.csv` is provided or must be generated.** If it's provided, use Cell 2A and skip 2B.
- **Exact column names.** This script uses `date`, `category`, `title`, `units_sold`, `unit_price` and `total_revenue`. If the provided CSV uses other names, change them in every cell.
- Required file names for the deliverables: not confirmed.

---

## Setup (before recording)

- Open a new notebook in Google Colab and rename it, for example `bookstore_sales_analysis.ipynb`.
- Have `notebook_cells.py` open outside the recorded area so you can copy each cell.
- If the CSV is provided, have it ready to upload.
- Browser zoom around 110–125% so the code and tables are readable.

---

## Recording script

### Step 1 — Title and imports

- **On screen:** Add a **text cell** with `# Bookstore Sales Analysis`. Below it, paste **Cell 1** and run it:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```
- **Say:** "I'm analyzing 200 synthetic sales transactions from a bookstore. The plan is to load and check the data, get descriptive statistics, group sales by category and month, plot the results, and look for outliers using the IQR method."
- **Check:** The cell runs without errors.
- **Pause:** Short.

### Step 2 — Get the data

**Option A: the CSV is provided.** Paste and run **Cell 2A** (remove the `#` signs):
```python
from google.colab import files
uploaded = files.upload()
```
- **Say:** "I'll upload the sales data CSV file."
- **Check:** `sales_data.csv` appears in the Files panel.

**Option B: generate the CSV.** Paste and run **Cell 2B**:
```python
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
```
- **Say:** "The dataset is synthetic, so I'll generate it here with a fixed random seed. That way anyone who reruns the notebook gets the same 200 rows. Each category has its own price range, and total revenue is units sold times unit price. I save everything to sales data dot CSV."
- **Check:** `sales_data.csv` appears in the Files panel (folder icon on the left).
- **Pause:** Yes. Show the file in the panel.

### Step 3 — Load and inspect

- **On screen:** Paste and run **Cell 3**, then **Cell 4**:
  ```python
  df = pd.read_csv("sales_data.csv", parse_dates=["date"])
  print(df.shape)
  df.head()
  ```
  ```python
  df.info()
  ```
- **Say:** "I'll load the file and parse the date column as dates, so I can group by month later. Then I'll check the shape and the column types."
- **Check:** The shape should be `(200, 6)`, and `date` should have a `datetime64` type. Read the actual output.
- **Say:** "There are [rows] rows and [columns] columns, and the date column was parsed as a date."
- **Pause:** Yes, on `head()` and on `info()`.

### Step 4 — Data quality

- **On screen:** Paste and run **Cell 5**:
  ```python
  print("Missing values:\n", df.isna().sum())
  print("Duplicate rows:", df.duplicated().sum())
  print(
      "Revenue matches units x price:",
      np.isclose(df["units_sold"] * df["unit_price"], df["total_revenue"], atol=0.01).all(),
  )
  ```
- **Say:** "Before analyzing anything, I'll check for missing values and duplicates. I'll also confirm that total revenue really equals units times price."
- **Check:** Read each result.
- **Say:** "[No missing values / X missing values in column Y], [no duplicates / X duplicates], and the revenue check returns [True / False]."
- **If there are problems:** Add a cell that fixes them (for example `df = df.drop_duplicates()` or recalculating `total_revenue`) and explain why. Rerun Cell 5 to confirm. Don't clean anything that doesn't need it.
- **Say (if clean):** "The data is clean, so no cleaning is needed here."
- **Pause:** Yes.

### Step 5 — Descriptive statistics

- **On screen:** Paste and run **Cell 6**:
  ```python
  df[["units_sold", "unit_price", "total_revenue"]].describe().round(2)
  ```
- **Say:** "Now the descriptive statistics for the numeric columns."
- **Check:** The table shows count, mean, std, min, the quartiles and max.
- **Say:** "The average transaction brings in [mean] in revenue. The median is [50% value], and the largest single transaction is [max]."
- **If the mean is clearly above the median, add:** "The mean is above the median, so a few large transactions are pulling it up."
- **Pause:** Yes, long. Read from the table.

### Step 6 — Sales by category

- **On screen:** Paste and run **Cell 7**:
  ```python
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
  ```
- **Say:** "Next, I'll group by category and compare the number of transactions, the units sold, and the total revenue."
- **Check:** One row per category, sorted by revenue.
- **Say:** "[Category] has the highest revenue at [value], and [category] has the lowest at [value]."
- **If the top category by revenue isn't the one with the most units:** "Interesting: [category] sells more units, but [category] earns more because of its higher prices."
- **Pause:** Yes.

### Step 7 — Sales by month

- **On screen:** Paste and run **Cell 8**:
  ```python
  df["month"] = df["date"].dt.to_period("M")
  by_month = (
      df.groupby("month")
      .agg(transactions=("title", "count"), revenue=("total_revenue", "sum"))
      .round(2)
  )
  by_month
  ```
- **Say:** "Now by month. I'm creating a month column from the date and summing revenue for each month."
- **Check:** The months are in order. Count how many there are.
- **Say:** "The strongest month is [month] with [value], and the weakest is [month] with [value]."
- **Pause:** Yes.

### Step 8 — Bar charts

- **On screen:** Paste and run **Cell 9** (two bar charts side by side; see `notebook_cells.py`).
- **Say:** "Two bar charts: revenue by category on the left, and revenue by month on the right."
- **Check:** Both charts have a title, axis labels and readable tick labels.
- **Say:** Describe what you see, for example: "The category chart shows the gap between [A] and [B] clearly. The monthly chart is [fairly even / peaks in month X / drops in month Y]."
- **Pause:** Yes, long, on the charts.

### Step 9 — Histograms

- **On screen:** Paste and run **Cell 10** (revenue histogram and units histogram).
- **Say:** "Now the distributions: one histogram of revenue per transaction, and one of units sold."
- **Check:** Look at the shape (skew, where most values fall).
- **Say:** "Most transactions fall between about [low] and [high] in revenue. The distribution is [right-skewed, with a long tail of larger sales / roughly symmetric]."
- **Pause:** Yes.

### Step 10 — Outliers with IQR

- **On screen:** Paste and run **Cell 11**:
  ```python
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
  ```
- **Say:** "For outliers, I'm using the IQR method on total revenue. Anything below Q1 minus 1.5 times the IQR, or above Q3 plus 1.5 times the IQR, counts as an outlier."
- **Check:** Read the bounds and the number of outliers.
- **Say:** "The upper bound is [value], and there are [n] outliers."
- **If the lower bound is negative, add:** "The lower bound is below zero, and revenue can't be negative, so only unusually large sales can show up as outliers."
- **If there are outliers:** "Looking at these rows, they're [category or pattern], with [many units / high prices]. They look like real large purchases, not data errors, so I'll keep them in the analysis."
- **If there are none:** "No transactions fall outside the bounds."
- **Pause:** Yes.

### Step 11 — Conclusions (text cell)

- **On screen:** Add a **text cell** and fill it in with the real values from your outputs:
  ```
  ## Conclusions
  - Data quality: [missing values / duplicates / revenue check result].
  - Typical transaction: mean revenue [x], median [y].
  - Top category by revenue: [category] ([value]); lowest: [category] ([value]).
  - Monthly pattern: best month [month], weakest month [month]; [overall trend].
  - Outliers (IQR): [n] transactions above [upper bound]; [interpretation and decision].
  - Limitation: the data is synthetic, so these patterns don't describe a real store.
  ```
- **Say:** "To finish, I'll write down the main findings using the numbers from the cells above." Read each line aloud as you write it.
- **Check:** Every number matches an output visible in the notebook.
- **Pause:** While typing.

### Step 12 — Run everything and save

- **On screen:**
  1. *Runtime > Restart session and run all*.
  2. If you generated the CSV, run **Cell 12** (remove the `#` signs):
     ```python
     from google.colab import files
     files.download("sales_data.csv")
     ```
  3. *File > Download > Download .ipynb*.
- **Say:** "I'll restart the runtime and run everything from top to bottom, to make sure the notebook works in order. Then I'll download the CSV and the notebook."
- **Check:** Every cell finishes without errors, the conclusions still match the outputs, and both files are downloaded.
- **Say (once confirmed):** "Everything ran cleanly, and both files are saved."
- **Pause:** During the run.

---

## Task checklist

- [ ] 200 rows and 6 columns confirmed on screen.
- [ ] Missing values, duplicates and the revenue formula checked.
- [ ] `describe()` shown and discussed.
- [ ] Sales grouped by category and by month.
- [ ] Bar charts and histograms with titles and axis labels.
- [ ] IQR outliers: bounds and count shown and interpreted.
- [ ] Conclusions use real numbers from the notebook.
- [ ] *Restart and run all* finishes without errors.
- [ ] `.ipynb` and `sales_data.csv` downloaded.

## General recording checklist

**Before recording**
- [ ] Read the original task instructions and resolve the missing information above.
- [ ] Notifications off. No personal tabs, emails or accounts visible.
- [ ] Browser zoom large enough to read code and tables.
- [ ] Microphone tested: volume and background noise.
- [ ] This script open on another screen or printed, outside the recorded area.

**While recording**
- [ ] Follow the steps in order. If something fails, show the error, explain it and fix it on screen.
- [ ] Read numbers from the screen. Never state a result before running the cell.
- [ ] Pause on tables, charts and key outputs.

**After recording**
- [ ] Watch the full video: audio is clear, code is readable, no sensitive information.
- [ ] Files named as the original task requires.
