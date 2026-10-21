# 6bbsb278 — Fitness Activity Data Analysis

Recording script for analyzing 200 synthetic daily fitness records in **Google Colab**: inspect and clean `fitness_data.csv` if needed, compute descriptive statistics, compare days of the week, measure the Pearson correlation between steps and calories, draw bar and scatter charts, detect outliers with the IQR method, and write conclusions.

**Registered deliverables:** the notebook (`.ipynb`) and the CSV file (`fitness_data.csv`).

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

The CSV is **not** included on purpose. Cell 2B generates it on camera with a fixed seed (`7`): 200 consecutive days starting on 2024-01-01. Calories are built partly from steps and exercise minutes, so a positive correlation is expected *by design*. Say this on camera (Step 8) so the result isn't presented as a discovery about real people.

### Pre-test (not for narration)

I ran all the code cells locally (Python 3.14 with pandas and SciPy, without the Colab-only cells) and they finished without errors. Colab may have different library versions. During the recording, read only what your own screen shows.

## Missing information (check the original task before recording)

- Required video length: not confirmed.
- Recording rules (camera, microphone, resolution, single take, edits allowed): not confirmed.
- AutoQC requirements: not confirmed.
- **Whether `fitness_data.csv` is provided or must be generated.** If it's provided, use Cell 2A and skip 2B. A provided file may contain real cleaning issues that Step 4 has to handle.
- **Exact column names.** This script uses `date`, `day_of_week`, `steps`, `calories_burned`, `exercise_minutes` and `active_hours`. If the provided CSV uses other names, change them in every cell.
- Whether the p-value is required, or only Pearson `r`: not confirmed. The p-value is included as extra context.
- Required file names for the deliverables: not confirmed.

---

## Setup (before recording)

- Open a new notebook in Google Colab and rename it, for example `fitness_activity_analysis.ipynb`.
- Have `notebook_cells.py` open outside the recorded area so you can copy each cell.
- If the CSV is provided, have it ready to upload.
- Browser zoom around 110–125% so code and tables are readable.

---

## Recording script

### Step 1 — Title and imports

- **On screen:** Add a **text cell** with `# Fitness Activity Data Analysis`. Paste and run **Cell 1**:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  from scipy.stats import pearsonr
  ```
- **Say:** "This notebook looks at 200 synthetic daily fitness records: steps, calories, exercise minutes, and active hours. I want to compare the days of the week, measure how steps relate to calories, and check for outliers."
- **Check:** The cell runs without errors.
- **Pause:** Short.

### Step 2 — Get the data

**Option A: the CSV is provided.** Paste and run **Cell 2A** (remove the `#` signs):
```python
from google.colab import files
uploaded = files.upload()
```
- **Say:** "I'll upload the fitness data file."

**Option B: generate the CSV.** Paste and run **Cell 2B**:
```python
rng = np.random.default_rng(7)
n = 200
dates = pd.date_range("2024-01-01", periods=n, freq="D")
steps = rng.normal(8000, 2500, n).clip(1000, None).round().astype(int)
exercise_minutes = rng.normal(40, 15, n).clip(0, None).round().astype(int)
calories = (1600 + steps * 0.04 + exercise_minutes * 5 + rng.normal(0, 120, n)).round().astype(int)
active_hours = (steps / 1500 + rng.normal(0, 0.8, n)).clip(0.5, None).round(1)

fitness = pd.DataFrame({
    "date": dates.date,
    "day_of_week": dates.day_name(),
    "steps": steps,
    "calories_burned": calories,
    "exercise_minutes": exercise_minutes,
    "active_hours": active_hours,
})
fitness.to_csv("fitness_data.csv", index=False)
```
- **Say:** "Since the data is synthetic, I'll generate it here with a fixed seed: 200 consecutive days. I'm building calories partly from steps and exercise minutes, plus some random noise, so I expect them to be related. I'll keep that in mind when I look at the correlation."
- **Check:** `fitness_data.csv` appears in the Files panel.
- **Pause:** Yes.

### Step 3 — Load and inspect

- **On screen:** Paste and run **Cell 3**:
  ```python
  df = pd.read_csv("fitness_data.csv", parse_dates=["date"])
  print(df.shape)
  df.info()
  df.head()
  ```
- **Say:** "I'll load the data, parsing the date column, and check the shape, the types, and the first rows."
- **Check:** The shape should be `(200, 6)`, with numeric types for the four measures. Read the actual output.
- **Say:** "[Rows] rows and [columns] columns. The four measures are numeric, and the date was parsed correctly."
- **Pause:** Yes.

### Step 4 — Quality check and cleaning

- **On screen:** Paste and run **Cell 4**:
  ```python
  numeric_cols = ["steps", "calories_burned", "exercise_minutes", "active_hours"]
  print("Missing values:\n", df.isna().sum())
  print("Duplicate rows:", df.duplicated().sum())
  print("Negative values:\n", (df[numeric_cols] < 0).sum())
  print("Day names match dates:", (df["date"].dt.day_name() == df["day_of_week"]).all())
  ```
- **Say:** "Now a quality check. I'm looking for missing values, duplicates, and negative numbers, which wouldn't make sense for steps or calories. I'm also confirming that the day-of-week column matches the dates."
- **Check:** Read each line.
- **If everything is clean, say:** "No missing values, no duplicates, no negative numbers, and the day names match. No cleaning needed."
- **If there are problems:** Add a new cell that fixes only what was found, and explain each decision. For example:
  ```python
  df = df.drop_duplicates()
  df["day_of_week"] = df["date"].dt.day_name()
  ```
  **Say:** "There were [problem], so I'm [fix] because [reason]." Then rerun Cell 4 and confirm the result.
- **Pause:** Yes.

### Step 5 — Descriptive statistics

- **On screen:** Paste and run **Cell 5**:
  ```python
  df[numeric_cols].describe().round(1)
  ```
- **Say:** "Descriptive statistics for the four measures."
- **Check:** The full table.
- **Say:** "The average is about [mean] steps per day, with a median of [50% value]. Calories average [mean], exercise is about [mean] minutes, and active time is about [mean] hours a day."
- **Pause:** Yes, long.

### Step 6 — Compare days of the week

- **On screen:** Paste and run **Cell 6**:
  ```python
  day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  df["day_of_week"] = pd.Categorical(df["day_of_week"], categories=day_order, ordered=True)

  by_day = df.groupby("day_of_week", observed=True)[numeric_cols].mean().round(1)
  by_day
  ```
- **Say:** "I'll compare the averages for each day of the week. I'm setting the day order explicitly, so the table goes Monday to Sunday instead of alphabetically."
- **Check:** Seven rows, in order.
- **Say:** "[Day] has the most steps on average, and [day] has the fewest."
- **If the differences are small, add:** "The differences between days are fairly small, so there's no strong weekly pattern."
- **Pause:** Yes.

### Step 7 — Bar charts by day

- **On screen:** Paste and run **Cell 7** (average steps and average calories by day; see `notebook_cells.py`).
- **Say:** "Here are the same averages as bar charts, for steps and calories."
- **Check:** Both charts have titles and axis labels, and the days are in order.
- **Say:** Describe what you see, for example: "The bars are [close together / higher on X]."
- **Pause:** Yes.

### Step 8 — Pearson correlation

- **On screen:** Paste and run **Cell 8**:
  ```python
  r, p_value = pearsonr(df["steps"], df["calories_burned"])
  print(f"Pearson r: {r:.3f}")
  print(f"p-value: {p_value:.4g}")
  ```
- **Say:** "Now the Pearson correlation between steps and calories burned. I'm also printing the p-value to see whether the relationship could just be chance."
- **Check:** Read `r` and the p-value.
- **Say:** "The correlation is [r]. That's a [weak / moderate / strong] [positive / negative] relationship, and the p-value is [value], [well below / above] 0.05."
- **If you generated the data, add:** "This makes sense, because I built calories partly from steps. With real data, this would be a finding. Here it mostly confirms that the generator works as intended."
- **Rough guide for the strength of `r` (use as orientation only):** below 0.3 is weak, 0.3 to 0.7 is moderate, above 0.7 is strong.
- **Pause:** Yes.

### Step 9 — Scatter plot

- **On screen:** Paste and run **Cell 9** (scatter plot with a red linear-fit line).
- **Say:** "A scatter plot with a fitted line, to see the relationship visually."
- **Check:** The direction of the line matches the sign of `r`.
- **Say:** "The points follow the line [closely / loosely], which matches the [strength] correlation."
- **Pause:** Yes.

### Step 10 — Outliers with IQR

- **On screen:** Paste and run **Cell 10**, then **Cell 11**:
  ```python
  def iqr_outliers(series):
      """Return the lower bound, upper bound, and a mask of IQR outliers."""
      q1, q3 = series.quantile([0.25, 0.75])
      iqr = q3 - q1
      lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
      mask = (series < lower) | (series > upper)
      return lower, upper, mask


  for col in numeric_cols:
      lower, upper, mask = iqr_outliers(df[col])
      print(f"{col}: bounds [{lower:.1f}, {upper:.1f}], outliers = {mask.sum()}")
  ```
  ```python
  _, _, steps_mask = iqr_outliers(df["steps"])
  df[steps_mask]
  ```
- **Say:** "I'll apply the IQR method to each measure. I'm using a small helper function so I don't repeat the same code four times. Then I'll look at the rows flagged for steps."
- **Check:** Read the bounds and the count for each column.
- **Say:** "Steps has [n] outliers, calories [n], exercise minutes [n], and active hours [n]."
- **If there are step outliers:** "These are days with [very high / very low] step counts. They're [plausible, like a long hike or a rest day / suspicious], so I'll [keep / remove] them."
- **If a lower bound is negative:** "The lower bound for [column] is below zero, so only high values can be flagged there."
- **Pause:** Yes.

### Step 11 — Conclusions (text cell)

- **On screen:** Add a **text cell** and fill it in with the real values from your outputs:
  ```
  ## Conclusions
  - Data quality: [result of checks; cleaning applied or not needed].
  - Daily averages: [steps] steps, [calories] calories, [minutes] exercise minutes, [hours] active hours.
  - Day of week: highest steps on [day], lowest on [day]; [size of the differences].
  - Steps vs calories: Pearson r = [r], p = [p] → [strength and direction].
  - Outliers (IQR): [counts per column]; [decision: kept or removed, and why].
  - Limitations: synthetic data built with a steps–calories link; correlation does not imply causation.
  ```
- **Say:** "Here are the conclusions, based on the outputs above." Read each line as you write it.
- **Check:** Every number matches an output.
- **Pause:** While typing.

### Step 12 — Run everything and save

- **On screen:**
  1. *Runtime > Restart session and run all*.
  2. If you generated the CSV, run **Cell 12** (remove the `#` signs):
     ```python
     from google.colab import files
     files.download("fitness_data.csv")
     ```
  3. *File > Download > Download .ipynb*.
- **Say:** "I'll rerun the whole notebook from a clean state, then download the CSV and the notebook."
- **Check:** No errors, the conclusions still match the outputs, and both files are downloaded.
- **Say (once confirmed):** "Everything ran cleanly, and both files are saved."
- **Pause:** During the run.

---

## Task checklist

- [ ] 200 records and 6 columns confirmed.
- [ ] Quality check done; cleaning applied, or explained as not needed.
- [ ] `describe()` discussed.
- [ ] Days of the week compared, in Monday-to-Sunday order.
- [ ] Pearson `r` (and p-value) between steps and calories, with the synthetic-data caveat.
- [ ] Bar charts and scatter plot.
- [ ] IQR outliers for each measure.
- [ ] Conclusions use real values.
- [ ] *Restart and run all* finishes without errors.
- [ ] `.ipynb` and `fitness_data.csv` downloaded.

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
