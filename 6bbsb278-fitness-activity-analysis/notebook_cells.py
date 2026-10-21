# Fitness Activity Data Analysis — notebook cells for Google Colab.
# Each "# %%" block is one Colab code cell. Paste them in order.
# Markdown cells (title and conclusions) are described in README.md.

# %% Cell 1 — Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# %% Cell 2A — OPTION A: upload a provided fitness_data.csv (Colab only)
# Use this cell INSTEAD of Cell 2B if the task gives you the CSV.
# from google.colab import files
# uploaded = files.upload()

# %% Cell 2B — OPTION B: generate the synthetic dataset
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

# %% Cell 3 — Load and inspect
df = pd.read_csv("fitness_data.csv", parse_dates=["date"])
print(df.shape)
df.info()
df.head()

# %% Cell 4 — Data quality checks
numeric_cols = ["steps", "calories_burned", "exercise_minutes", "active_hours"]
print("Missing values:\n", df.isna().sum())
print("Duplicate rows:", df.duplicated().sum())
print("Negative values:\n", (df[numeric_cols] < 0).sum())
print("Day names match dates:", (df["date"].dt.day_name() == df["day_of_week"]).all())

# %% Cell 5 — Descriptive statistics
df[numeric_cols].describe().round(1)

# %% Cell 6 — Averages by day of week
day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
df["day_of_week"] = pd.Categorical(df["day_of_week"], categories=day_order, ordered=True)

by_day = df.groupby("day_of_week", observed=True)[numeric_cols].mean().round(1)
by_day

# %% Cell 7 — Bar charts by day of week
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

by_day["steps"].plot(kind="bar", ax=axes[0], color="seagreen")
axes[0].set_title("Average Steps by Day of Week")
axes[0].set_ylabel("Steps")

by_day["calories_burned"].plot(kind="bar", ax=axes[1], color="indianred")
axes[1].set_title("Average Calories Burned by Day of Week")
axes[1].set_ylabel("Calories")

for ax in axes:
    ax.set_xlabel("Day of Week")
    ax.tick_params(axis="x", rotation=45)

plt.tight_layout()
plt.show()

# %% Cell 8 — Pearson correlation between steps and calories
r, p_value = pearsonr(df["steps"], df["calories_burned"])
print(f"Pearson r: {r:.3f}")
print(f"p-value: {p_value:.4g}")

# %% Cell 9 — Scatter plot with a linear fit
plt.figure(figsize=(8, 6))
plt.scatter(df["steps"], df["calories_burned"], alpha=0.6)
m, b = np.polyfit(df["steps"], df["calories_burned"], 1)
x = np.linspace(df["steps"].min(), df["steps"].max(), 100)
plt.plot(x, m * x + b, color="red", label="Linear fit")
plt.title(f"Steps vs Calories Burned (r = {r:.2f})")
plt.xlabel("Steps")
plt.ylabel("Calories Burned")
plt.legend()
plt.show()


# %% Cell 10 — Outliers with the IQR method (all numeric columns)
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

# %% Cell 11 — Rows flagged as step outliers
_, _, steps_mask = iqr_outliers(df["steps"])
df[steps_mask]

# %% Cell 12 — Download the CSV (Colab only; only needed if you generated it)
# from google.colab import files
# files.download("fitness_data.csv")
