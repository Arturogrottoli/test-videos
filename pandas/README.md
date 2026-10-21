# E-commerce Exploratory Data Analysis

A beginner-friendly exploratory data analysis (EDA) in **Google Colab**, using **Python**, **pandas**, and **Matplotlib**. You load a public e-commerce dataset, explore it, convert the dates, check for missing values, and create three charts: revenue by category, monthly revenue, and the distribution of revenue per order line.

Colab already includes pandas and Matplotlib, so there is **nothing to install**.

> **Before recording:** open the official Mercor Goal for task `dje548b6` and compare it with this plan. If the Goal asks for a different dataset, different charts, or extra steps, the Goal wins. Change this plan to match it.

---

## Objectives

1. Load a public CSV file with pandas.
2. Explore the data: first rows, columns, size, and data types.
3. Convert the `ordered_at` column to real dates.
4. Check for missing values.
5. Create three readable charts with Matplotlib and explain what each one shows.

---

## Technologies used

| Tool | Purpose |
| ---- | ------- |
| Google Colab | Free online notebook that runs Python in the browser |
| pandas | Loading, exploring, and grouping tabular data |
| Matplotlib | Creating charts |

---

## Dataset

**Retail orders** by Datanemics.

- Page: https://datanemics.com/datasets/retail-orders/
- Direct CSV link: https://datanemics.com/datasets/data/retail-orders.csv
- License: public domain (CC0 1.0). The data is **synthetic**, so there are no real customers.
- Size: **7,000 rows** (order lines) and **12 columns**, from January 2023 to December 2024.
- One order can have several lines, so `order_id` repeats.

### Columns

| Column | Type | Description |
| ------ | ---- | ----------- |
| `order_id` | text | Order ID. Repeats across the lines of one order |
| `line_no` | integer | Line number inside the order |
| `ordered_at` | timestamp | When the order was placed (UTC) |
| `customer_id` | text | Customer ID |
| `channel` | text | web, ios, android, or marketplace |
| `country` | text | Two-letter shipping country code |
| `category` | text | apparel, beauty, electronics, grocery, home, or sports |
| `units` | integer | Units on this line |
| `unit_price_usd` | float | List price per unit |
| `discount_pct` | float | Discount, from 0 to 0.45 |
| `revenue_usd` | float | `units × unit_price_usd × (1 − discount_pct)` |
| `returned` | boolean | Whether the line was returned later |

This analysis uses only `ordered_at`, `category`, and `revenue_usd`.

---

## How to run it in Colab

1. Open https://colab.research.google.com and sign in with a Google account.
2. Click **New notebook**.
3. Type each cell from [The notebook, cell by cell](#the-notebook-cell-by-cell) and run it with `Shift + Enter`.

Cell 1 loads the CSV straight from its URL. If that doesn't work, download the file from the dataset page, open the **Files** panel (folder icon on the left), click **Upload to session storage**, choose `retail-orders.csv`, and use `pd.read_csv("retail-orders.csv")` instead.

---

## The notebook, cell by cell

Add a short Markdown cell above each code cell with its title, for example `## 1. Load the data`.

### Cell 1 — Load the data

```python
import pandas as pd
import matplotlib.pyplot as plt

url = "https://datanemics.com/datasets/data/retail-orders.csv"
df = pd.read_csv(url)
df.head()
```

### Cell 2 — Size, columns, and data types

```python
print("Rows and columns:", df.shape)
print("Columns:", df.columns.tolist())
df.dtypes
```

### Cell 3 — Convert dates and check missing values

```python
df["ordered_at"] = pd.to_datetime(df["ordered_at"])
print("From", df["ordered_at"].min(), "to", df["ordered_at"].max())
print(df.isna().sum())
```

### Cell 4 — Chart 1: revenue by category (bar chart)

```python
by_category = df.groupby("category")["revenue_usd"].sum().sort_values(ascending=False)

by_category.plot(kind="bar", color="steelblue", rot=0)
plt.title("Total Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue (USD)")
plt.tight_layout()
plt.show()
```

### Cell 5 — Chart 2: monthly revenue (line chart)

```python
monthly = df.groupby(df["ordered_at"].dt.to_period("M"))["revenue_usd"].sum()

monthly.plot(kind="line", marker="o")
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (USD)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### Cell 6 — Chart 3: revenue per order line (histogram)

```python
print(df["revenue_usd"].describe())

df["revenue_usd"].plot(kind="hist", bins=50, color="seagreen", edgecolor="white")
plt.title("Distribution of Revenue per Order Line")
plt.xlabel("Revenue per line (USD)")
plt.ylabel("Number of order lines")
plt.tight_layout()
plt.show()
```

---

## Charts generated

| Chart | Type | Question it answers |
| ----- | ---- | ------------------- |
| Total Revenue by Category | Bar chart | Which categories bring in the most money? |
| Monthly Revenue | Line chart | How does revenue change over time? |
| Distribution of Revenue per Order Line | Histogram | Are most order lines small or large? |

---

## Example findings (illustrative)

> **Illustrative only.** I calculated these numbers from the CSV downloaded on 21 Oct 2026, outside Colab. Run the notebook yourself and use **your** output as the source of truth. If the dataset changes, these numbers will change.

- The file has 7,000 order lines from 4,169 orders, from 1 Jan 2023 to 30 Dec 2024. It has **no missing values**.
- Total revenue is about **$773,924**.
- **Electronics** is the top category (about $326,204, roughly 42% of revenue), even though it has fewer lines (960) than apparel (1,696). Electronics items are more expensive. **Grocery** is the lowest (about $36,694).
- Monthly revenue mostly stays between about $25,000 and $38,000. It peaks in **December** in both years (about $48,202 in 2023 and $43,976 in 2024) and drops in January (the lowest month is January 2024, about $18,567).
- The histogram is **right-skewed**: most lines are small (median about $60, and 75% are under about $125), but a few lines are much larger (198 lines are over $500, and the maximum is about $2,318).

---

## Limitations

- The data is synthetic, so the results are for practice, not for real business decisions.
- Revenue includes the 677 lines that were later returned. A deeper analysis could exclude them.
- We only use three of the twelve columns. Channel, country, and discount could also be analyzed.

---

## Recording guide (about 15 minutes)

Each block says **which window to show**, **what to do**, **what code to write**, and **what to say**. The English lines are for the recording. The Spanish lines are only for your preparation. Times are approximate: if the official Goal needs more time, take it.

### Before you record

1. Read the official Mercor Goal and recording rules for `dje548b6`. Check that the three charts are the ones the task asks for.
2. Sign in to Google in the browser.
3. Open the dataset page in one tab and Colab in another.
4. Zoom in so the code is easy to read (`Ctrl + +`).
5. Do one full practice run in a separate notebook, and write down your real numbers for the last block.
6. If the recording rules say you must type the code on screen, type it. Don't paste it.

---

### 0:00–2:00 — Objective and the dataset

**Window:** the dataset page (https://datanemics.com/datasets/retail-orders/).

**Do:** Scroll through the page and show the column list and the CSV download link.

**Say:**

> **EN:** Hi! Today I'm going to do an exploratory data analysis of a public e-commerce dataset, using Python, pandas, and Matplotlib in Google Colab.
> *ES: ¡Hola! Hoy voy a hacer un análisis exploratorio de un dataset público de e-commerce, usando Python, pandas y Matplotlib en Google Colab.*
>
> **EN:** This is the Retail Orders dataset. It's synthetic, so there's no real customer data, and it's in the public domain. It has 7,000 order lines from 2023 and 2024.
> *ES: Este es el dataset Retail Orders. Es sintético, así que no hay datos reales de clientes, y es de dominio público. Tiene 7.000 líneas de pedidos de 2023 y 2024.*
>
> **EN:** The data comes as a CSV file. CSV means "comma-separated values": it's a simple text file where each line is a row, and commas separate the columns.
> *ES: Los datos vienen en un archivo CSV. CSV significa "valores separados por comas": es un archivo de texto simple donde cada línea es una fila y las comas separan las columnas.*
>
> **EN:** I'll focus on three columns: the order date, the product category, and the revenue in US dollars.
> *ES: Me voy a centrar en tres columnas: la fecha del pedido, la categoría del producto y el ingreso en dólares.*

---

### 2:00–4:00 — Open Colab, pandas, and load the data

**Window:** Google Colab.

**Do:** Click **New notebook** and rename it to `ecommerce_eda.ipynb`. Add a Markdown cell with the title. Type **Cell 1** and run it.

**Say:**

> **EN:** I'll create a new notebook. A notebook is made of cells: we write code in a cell, run it, and the result appears below.
> *ES: Voy a crear un notebook nuevo. Un notebook está formado por celdas: escribimos código en una celda, la ejecutamos y el resultado aparece debajo.*
>
> **EN:** pandas is a Python library for working with tables of data. It lets us load, filter, and summarize data with very little code. Colab already has it installed.
> *ES: pandas es una librería de Python para trabajar con tablas de datos. Nos permite cargar, filtrar y resumir datos con muy poco código. Colab ya la tiene instalada.*
>
> **EN:** read_csv loads the file straight from its link into a DataFrame. A DataFrame is like a spreadsheet inside Python. And head shows the first five rows.
> *ES: read_csv carga el archivo directamente desde su enlace en un DataFrame. Un DataFrame es como una hoja de cálculo dentro de Python. Y head muestra las primeras cinco filas.*

If the link doesn't load, upload the file from the **Files** panel instead:

> **EN:** If loading from the link doesn't work, we can download the CSV and upload it to Colab from the Files panel.
> *ES: Si la carga desde el enlace no funciona, podemos descargar el CSV y subirlo a Colab desde el panel de archivos.*

---

### 4:00–6:00 — Explore the data and convert the dates

**Window:** Colab.

**Do:** Type and run **Cell 2**, then **Cell 3**.

**Say:**

> **EN:** First, let's get to know the data. shape gives us the number of rows and columns, and dtypes shows the type of each column.
> *ES: Primero, conozcamos los datos. shape nos da el número de filas y columnas, y dtypes muestra el tipo de cada columna.*
>
> **EN:** Look at ordered_at: pandas reads it as text, not as a date. So I'll convert it with to_datetime. Now we can group by month.
> *ES: Fíjense en ordered_at: pandas lo lee como texto, no como fecha. Así que lo convierto con to_datetime. Ahora podemos agrupar por mes.*
>
> **EN:** Next, I check for missing values. This matters because missing or dirty data can give us wrong totals. Here, every column shows zero, so the data is complete.
> *ES: Después, reviso los valores faltantes. Esto importa porque los datos faltantes o sucios pueden darnos totales incorrectos. Acá todas las columnas muestran cero, así que los datos están completos.*

(Say "zero" only if your output really shows zero.)

---

### 6:00–11:30 — Matplotlib and the three charts

**Window:** Colab.

**Do:** Type and run **Cell 4**, **Cell 5**, and **Cell 6**, one at a time. Look at each chart before moving on.

**Say:**

> **EN:** Now the charts. Matplotlib is the most common Python library for charts. pandas uses it behind the scenes when we call plot.
> *ES: Ahora los gráficos. Matplotlib es la librería de gráficos más común en Python. pandas la usa por detrás cuando llamamos a plot.*

**Chart 1 — bar chart:**

> **EN:** For the first chart, I group the rows by category and add up the revenue. I sort it from highest to lowest, and I show it as a bar chart, with a title and labels on both axes.
> *ES: Para el primer gráfico, agrupo las filas por categoría y sumo los ingresos. Lo ordeno de mayor a menor y lo muestro como gráfico de barras, con un título y etiquetas en los dos ejes.*

**Chart 2 — line chart:**

> **EN:** For the second chart, I group the revenue by month, using the dates we converted earlier. A line chart is a good choice here, because it shows how revenue changes over time.
> *ES: Para el segundo gráfico, agrupo los ingresos por mes, usando las fechas que convertimos antes. Un gráfico de líneas es una buena opción acá, porque muestra cómo cambian los ingresos con el tiempo.*

**Chart 3 — histogram:**

> **EN:** The third chart is a histogram. It splits the revenue of each order line into ranges, called bins, and counts how many lines fall into each range. So it shows the distribution: are most lines small or large?
> *ES: El tercer gráfico es un histograma. Divide el ingreso de cada línea de pedido en rangos, llamados bins, y cuenta cuántas líneas caen en cada rango. Así muestra la distribución: ¿la mayoría de las líneas son chicas o grandes?*
>
> **EN:** I also print describe, which gives the mean, the median, and the minimum and maximum values.
> *ES: También imprimo describe, que da la media, la mediana y los valores mínimo y máximo.*

---

### 11:30–14:00 — Interpret and check the charts

**Window:** Colab. Scroll back to each chart.

**Do:** Check that each chart has a title and axis labels, and that the numbers make sense compared with the printed output. Describe **what you see in your own output**. The lines below are based on the [example findings](#example-findings-illustrative). Change them if your results are different.

**Say:**

> **EN:** In the bar chart, electronics is clearly the top category, even though it doesn't have the most order lines. That's because electronics products are more expensive. Grocery brings in the least revenue.
> *ES: En el gráfico de barras, electrónica es claramente la categoría principal, aunque no tiene la mayor cantidad de líneas de pedido. Eso es porque los productos de electrónica son más caros. Almacén es la que menos ingresos genera.*
>
> **EN:** In the line chart, revenue is fairly stable most of the year, but it peaks in December in both years and drops in January. That looks like a holiday season effect.
> *ES: En el gráfico de líneas, los ingresos son bastante estables durante la mayor parte del año, pero tienen un pico en diciembre en los dos años y bajan en enero. Parece un efecto de la temporada de fiestas.*
>
> **EN:** The histogram is right-skewed. Most order lines are small, under about 125 dollars, but there's a long tail of a few large lines. That's why the mean is higher than the median.
> *ES: El histograma tiene asimetría a la derecha. La mayoría de las líneas de pedido son chicas, de menos de unos 125 dólares, pero hay una cola larga de pocas líneas grandes. Por eso la media es mayor que la mediana.*
>
> **EN:** Let me check the charts: each one has a title, labeled axes, and the values match the totals we printed.
> *ES: Reviso los gráficos: cada uno tiene título, ejes con etiquetas, y los valores coinciden con los totales que imprimimos.*

---

### 14:00–15:00 — Summary

**Window:** Colab, scrolled to the top of the notebook.

**Say** (replace the words in brackets with your real results):

> **EN:** To sum up, we loaded a public e-commerce dataset with pandas, explored its structure, converted the dates, checked for missing values, and created three charts with Matplotlib.
> *ES: Para resumir, cargamos un dataset público de e-commerce con pandas, exploramos su estructura, convertimos las fechas, revisamos los valores faltantes y creamos tres gráficos con Matplotlib.*
>
> **EN:** The main findings: [top category] brings in the most revenue, sales peak in [peak month], and most order lines are small.
> *ES: Los hallazgos principales: [categoría principal] genera la mayor cantidad de ingresos, las ventas tienen su pico en [mes pico], y la mayoría de las líneas de pedido son chicas.*
>
> **EN:** The goal of an exploratory analysis is to understand the data before making decisions or building anything more complex. Thanks for watching!
> *ES: El objetivo de un análisis exploratorio es entender los datos antes de tomar decisiones o construir algo más complejo. ¡Gracias por mirar!*
