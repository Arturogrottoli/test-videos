# k3a13c10 — Analyze Discount Patterns in Sales Data Using Python and Pandas

Guion para grabar la tarea **k3a13c10** (Data Science & Analytics): en **Google Colab**, con **pandas**, analizás los descuentos de 2.200 ventas sintéticas de 2025, encontrás los descuentos inusuales por categoría y mes, los comparás con el calendario de promociones autorizadas y medís su impacto en el margen bruto. Se graba en **Firefox**, en **una sola toma**. La grabación tiene que durar **entre 15:00 y 50:59**. Este guion apunta a unos **32 minutos**, epílogo incluido.

**Cómo leer este guion:**

- 🖱️ = lo decís **mientras hacés** la acción. Siempre dice **qué** hacés, **dónde** está en la pantalla y, si no es obvio, **por qué**. Son las frases que cuenta AutoQC: **no te saltees ninguna**.
- 🟢 = explicación corta, entre una acción y otra. La última 🟢 de cada sección es la **transición** a la siguiente.
- ⌨️ = lo que vas diciendo **mientras tipeás** una celda larga, para no quedarte más de 5 segundos callado. Explica el bloque, no cada línea.
- 📘 **What each line does**: debajo de cada código, la explicación línea por línea en inglés, por si tenés dudas o tenés que explicar algo en voz alta. Es solo para vos: **no se lee en la grabación**, porque ahí cada celda se explica con una sola frase 🟢.
- Debajo de cada celda: **Resultado esperado** (lo que tiene que aparecer, con los números reales) y **Razonamiento profesional** (por qué importa y qué haría mal un analista sin experiencia). Esas dos partes son para vos: **no se leen**.
- Si usás un **atajo de teclado**, decí la tecla en voz alta: *"I'm pressing Command + S"*.
- **Todas las celdas son de código**, salvo la última (resumen y notas finales), que es de texto. El título de cada paso **no se escribe**: lo decís en voz alta (*"Step two: financial calculations"*).
- Toda celda sigue el mismo ciclo: **scroll hasta el final → clic en + Code → frase 🟢 de para qué sirve → tipear (con ⌨️) → clic en Run → señalar el resultado → explicarlo.**

---

## Pendientes antes de grabar

| Tema | Situación | Qué hacer |
| ---- | --------- | --------- |
| **Origen de los CSV** | La idea aprobada dice que los archivos **los genera Gemini antes de grabar**, y el revisor pide decirlo en las *Final notes*. Los dos CSV de esta carpeta **los generé yo con un script de Python**, no con Gemini. | Elegí una de dos: **(a)** generás los CSV con Gemini y me los pasás: vuelvo a correr el análisis y actualizo todos los números del guion. **(b)** Usás estos CSV y cambiás la nota final por una que sea cierta, por ejemplo *"generated with a Python script before recording"*. Pero eso contradice la idea aprobada: consultalo antes. **No digas "Gemini" si no es cierto.** |
| **Tipeo** | El código suma unos **3.600 caracteres**, más **1.100** del resumen. A 300 caracteres por minuto son unos **15 minutos de tipeo**: cerca del **45%** de una grabación de 32 minutos. El límite es **25%**. | Practicá las celdas hasta tipearlas rápido. Alargá las explicaciones de los resultados, que no son tipeo (la grabación puede llegar a 50:59). Si igual no alcanza, avisame y vemos cómo achicar más el código o el resumen. |
| **Versión de pandas** | Lo probé con pandas 3.1. Colab suele traer pandas 2.x. | Si `info()` dice `object` en vez de `str`, decí *"object means text"*. Los números no cambian. |

---

## Archivos de la carpeta

```
k3a13c10-discount-pattern-analysis/
├── README.md                  ← este guion
├── sales_transactions.csv     ← archivo de entrada 1 (no se modifica)
├── promotion_calendar.csv     ← archivo de entrada 2 (no se modifica)
└── discount_analysis.ipynb    ← notebook de referencia, completo y en orden
```

Para probar el notebook de referencia: en Colab, **File → Upload notebook → Browse**, elegís `discount_analysis.ipynb`, subís los dos CSV en el panel **Files** y ejecutás **Runtime → Run all**. Crea `flagged_transactions.csv`.

---

## Los datos

**`sales_transactions.csv`**: 2.200 ventas, del 1/1/2025 al 31/12/2025, en 6 categorías.

| Columna | Qué contiene |
| ------- | ------------ |
| `transaction_id` | `T00001` … `T02200` |
| `date` | Fecha de la venta |
| `category` | Electronics 478 · Clothing 445 · Home & Kitchen 410 · Sports & Outdoors 369 · Beauty 334 · Toys 164 |
| `quantity` | Unidades |
| `unit_price`, `unit_cost` | Precio y costo por unidad |
| `discount_rate` | Descuento como fracción (`0.25` = 25%)… salvo 8 filas |
| `promotion_id` | Vacío si no hubo promoción. 188 ventas tienen uno |
| `net_revenue` | Ingreso neto registrado = cantidad × precio × (1 − descuento) |
| `gross_margin` | Margen bruto registrado, en dólares = ingreso neto − cantidad × costo |

**`promotion_calendar.csv`**: 8 promociones autorizadas, `PRM-01` a `PRM-08`, con `campaign_name`, `applicable_category`, `start_date`, `end_date`, `planned_discount` y `max_discount`.

**Lo que tiene el dataset a propósito** (para vos; en el video se **descubre** con el código, no se anticipa):

| Qué | Filas |
| --- | ----- |
| Descuento guardado como porcentaje (`25` en vez de `0.25`) | 8 |
| Ingreso neto registrado sin restar el descuento | 6 |
| ID de promoción que no existe (`PRM-99`, 35%) | 3 |
| `PRM-07` (Electronics) usado en otra categoría | 3 |
| `PRM-02` usado después de su fecha de fin | 4 |
| `PRM-05` por encima del máximo aprobado | 3 |
| `PRM-01` dentro del máximo pero fuera de la tolerancia de 5 puntos | 4 |
| Más de 30% sin promoción | 7 |
| Campaña autorizada con margen muy bajo (`PRM-07`, Black Friday, 25%) | 33 |

---

## Antes de grabar

1. Leé el Goal y comparalo con este guion.
2. En **Firefox**, dejá **dos ventanas**: la primera con la **descripción de la tarea**, en pantalla, porque con ella arranca la grabación. La segunda con **Google Colab** y el notebook ya creado: **File → New notebook in Drive**, con el nombre `discount_analysis` y la **celda de código vacía** que Colab crea sola. Revisá que, al hacer clic en el ícono de Firefox en el **Dock (a la derecha)**, Colab aparezca en la **segunda línea** de la lista.
3. Tené `sales_transactions.csv` y `promotion_calendar.csv` en el **Escritorio**. Son los originales: no se tocan.
4. En Colab, **Tools → Settings → AI assistance**: ocultá las funciones de IA, si está la opción. No uses ninguna IA durante la grabación.
5. Maximizá la ventana de Colab y agrandá el zoom (`Cmd + +`) para que el código se lea.
6. Practicá una vez entera en voz alta, con cronómetro. Practicá sobre todo el tipeo de las celdas 5, 7, 8 y 11.
7. Ejecutá las celdas con el **botón Run** (mouse), así cada ejecución tiene su frase.
8. Nunca más de **5 segundos** en silencio: mientras tipeás, decí las frases ⌨️.
9. Salvo la descripción de la tarea del principio, no muestres Studio, el Slack del proyecto, Metadata.rtf, Insightful ni datos personales.

---

## A. 0:00–2:00 — Apertura

Empezás con la **descripción de la tarea** en pantalla. Esta primera parte dura **menos de 20 segundos**:

> 🟢 I will be beginning my task soon. I'll analyze discount patterns in a year of sales data with Python and pandas in Google Colab: find unusually high discounts, check them against the promotion calendar, and measure their impact on gross margin.

> 🖱️ I'm clicking the yellow minimize button at the top left of this Firefox window, to put the task description away.

> 🖱️ I'm clicking the Firefox icon in the Dock, on the right side of the screen, to see my open Firefox windows.

> 🖱️ I'm clicking the second line of the list, the Google Colab window, to open my notebook.

> 🖱️ I'm pointing at the notebook name, discount_analysis, at the top left next to the Colab logo. I created this empty notebook before starting.

> 🖱️ I'm clicking the Files icon, the folder in the left sidebar, to open the file panel.

> 🖱️ I'm clicking the Upload to session storage button, the page with an up arrow at the top of the left panel, to choose the two input files.

> 🖱️ In the file window, I'm clicking Desktop on the left, selecting sales_transactions.csv and promotion_calendar.csv with Command held down, and clicking Open at the bottom right.

Si aparece el aviso de que los archivos se borran al reiniciar el runtime:

> 🖱️ I'm clicking OK on the warning in the center of the screen. It only says uploaded files are deleted when the runtime restarts.

> 🖱️ I'm pointing at the two files in the left panel, in the file list.

> 🟢 These are my two starting files. They're synthetic, generated before recording. sales_transactions has 2,200 sales from 2025, and promotion_calendar lists the authorized campaigns, with their categories, dates, planned discount, and maximum approved discount. I'll only read them: the originals stay unchanged, and every change happens in a copy.

> 🟢 My approach: first, check the data and recalculate the money, so I know which numbers I can trust. Then find unusual discounts with the IQR method, by category and month, only in groups with at least 20 transactions. Then validate the promotions: ID, category, dates, maximum, and a tolerance of 5 percentage points around the planned discount.

> 🟢 Two business rules run separately from the statistics: no discount above 30% outside an authorized promotion, and a gross margin floor of 15%. At the end, I'll reconcile the totals, export the transactions that need review, and write a summary. And I'll keep four things apart: statistical anomalies, data quality issues, policy violations, and possible commercial decisions.

> 🖱️ I'm clicking the Files icon in the left sidebar again, to close the panel.

> 🟢 Let's start by loading the data.

**Razonamiento profesional:** decir al principio las reglas de negocio (30%, 15%, 20 transacciones, 5 puntos) deja claro que no se inventan sobre la marcha según lo que aparezca. Un analista sin experiencia empieza a calcular sin definir los criterios, y después los ajusta para que "den".

---

## B. 2:00–6:00 — Carga e inspección inicial

> 🟢 Step one: loading and inspection.

> 🖱️ I'm clicking inside the empty code cell at the top of the notebook, to start typing in it.

> 🟢 This first code cell imports pandas and reads both CSV files, telling pandas which columns are dates, and then shows the structure of the sales table with info.

> 🖱️ I'm typing the code in the first code cell, in the middle of the screen.

> ⌨️ I read the dates as real dates, not text, because later I'll compare them with the campaign dates.

**Celda 1:**

```python
import pandas as pd
sales = pd.read_csv("sales_transactions.csv", parse_dates=["date"])
promos = pd.read_csv("promotion_calendar.csv", parse_dates=["start_date", "end_date"])
sales.info()
```

📘 **What each line does** (para vos, no se lee):

- `import pandas as pd`: imports pandas, the table library, with the short name `pd`.
- `sales = pd.read_csv(...)`: reads the sales CSV into a table called `sales`. `parse_dates=["date"]` turns the `date` column into real dates, not text.
- `promos = pd.read_csv(...)`: reads the promotion calendar into `promos` and turns `start_date` and `end_date` into dates.
- `sales.info()`: shows the number of rows, the columns, the non-null values, and the data type of each column.

> 🖱️ I'm clicking the Run cell button, the play icon on the left edge of the first code cell, to load the files.

> 🖱️ I'm pointing at the status at the top right of Colab, which turns green when the runtime is connected.

> 🖱️ I'm moving the mouse down the Non-Null Count column in the info output, below the first code cell.

> 🟢 2,200 rows and 10 columns. Every column is complete except promotion_id, with only 188 values. That's expected: an empty promotion ID means the sale had no promotion. The date is a real datetime, and the money columns are numbers.

> 🖱️ I'm scrolling down to the end of the info output, and clicking the plus Code button in the toolbar at the top left, to add the second code cell.

> 🟢 This second code cell shows the whole promotion calendar. It's small, so I can read it all.

> 🖱️ I'm typing promos in the second code cell.

**Celda 2:**

```python
promos
```

📘 **What each line does** (para vos, no se lee):

- `promos`: because it's the last line of the cell, Colab displays the whole table (8 rows).

> 🖱️ I'm clicking the Run cell button on the left of the second code cell, to show the calendar.

> 🖱️ I'm moving the mouse down the eight rows of the calendar, from PRM-01 at the top to PRM-08 at the bottom.

> 🟢 Eight authorized campaigns, PRM-01 to PRM-08. For example, PRM-07 is Black Friday Electronics, from November 21st to December 1st, with a planned discount of 25% and a maximum of 30%. Discounts are stored as fractions: 0.25 means 25%.

> 🖱️ I'm scrolling down below the calendar, and clicking the plus Code button in the toolbar at the top left, to add the third code cell.

> 🟢 This third code cell checks the date range, the categories, the promotion IDs, and the distribution of the discount rate.

> 🖱️ I'm typing the four checks in the third code cell.

> ⌨️ dropna equals False also counts the sales with no promotion, so nothing is hidden.

**Celda 3:**

```python
print(sales["date"].min(), "to", sales["date"].max())
print(sales["category"].value_counts())
print(sales["promotion_id"].value_counts(dropna=False))
sales["discount_rate"].describe()
```

📘 **What each line does** (para vos, no se lee):

- `print(sales["date"].min(), "to", sales["date"].max())`: shows the first and the last date.
- `print(sales["category"].value_counts())`: counts the sales in each category.
- `print(sales["promotion_id"].value_counts(dropna=False))`: counts the sales for each promotion ID. `dropna=False` also counts the empty ones (`NaN`), that is, the sales without a promotion.
- `sales["discount_rate"].describe()`: summary statistics of the discount: count, mean, standard deviation, minimum, quartiles, and maximum.

> 🖱️ I'm clicking the Run cell button on the left of the third code cell, to run the checks.

> 🖱️ I'm pointing at the first line of the output, the date range.

> 🟢 The data covers the whole of 2025, from January 1st to December 31st.

> 🖱️ I'm moving the mouse down the category counts.

> 🟢 Six categories. Electronics is the largest, with 478 sales, and Toys the smallest, with only 164. That will matter for the minimum group size.

> 🖱️ I'm moving the mouse down the promotion IDs, to the last one, PRM-99.

> 🟢 2,012 sales have no promotion. And here's the first issue: three sales use PRM-99, an ID that isn't in the calendar. I'll come back to it in the promotion check.

> 🖱️ I'm pointing at the max row of the discount description, at the bottom of the output.

> 🟢 The second issue: the median discount is 0 and the third quartile is 10%, but the maximum is 26. A discount of 26 as a fraction would mean 2,600%, which is impossible. It looks like some discounts were stored as percentages. But I won't change anything yet. First, I'll check it.

**Resultado esperado:** fechas `2025-01-01` a `2025-12-31`. Categorías: Electronics 478, Clothing 445, Home & Kitchen 410, Sports & Outdoors 369, Beauty 334, Toys 164. Promociones: `NaN` 2012, PRM-07 36, PRM-05 27, PRM-01 26, PRM-02 22, PRM-06 22, PRM-08 20, PRM-03 16, PRM-04 16, **PRM-99 3**. `discount_rate`: mean 0,131, 50% 0, 75% 0,10, **max 26,0**.

**Razonamiento profesional:** la inspección no es un trámite: acá aparecen los dos problemas que, si no se ven, arruinan todo lo demás. Un analista sin experiencia dividiría por 100 todo lo que pase de 1 "porque es obvio", sin comprobar que el ingreso registrado lo confirma.

> 🟢 Before I calculate anything, let's investigate those large discount values.

---

## C. 6:00–10:30 — Cálculos financieros

> 🟢 Step two: financial calculations, starting with the ambiguous discount units.

> 🖱️ I'm scrolling down to the end of the third code cell, and clicking the plus Code button in the toolbar at the top left, to add the fourth code cell.

> 🟢 This fourth code cell takes the rows with a discount above 1, adds the campaign's planned discount, and recalculates net revenue in both ways: as a fraction and as a percentage. Then I compare both with the recorded net revenue.

> 🖱️ I'm typing the investigation in the fourth code cell.

> ⌨️ The merge brings the planned discount from the calendar. The left join keeps every odd row, even without a promotion.

**Celda 4:**

```python
odd = sales[sales["discount_rate"] > 1].merge(promos, on="promotion_id", how="left")
gross = odd["quantity"] * odd["unit_price"]
odd["as_fraction"] = gross * (1 - odd["discount_rate"])
odd["as_percent"] = gross * (1 - odd["discount_rate"] / 100)
odd[["transaction_id", "discount_rate", "planned_discount", "net_revenue", "as_fraction", "as_percent"]].round(2)
```

📘 **What each line does** (para vos, no se lee):

- `odd = sales[sales["discount_rate"] > 1].merge(promos, on="promotion_id", how="left")`: keeps the sales with a discount above 1 (impossible as a fraction) and adds their campaign data. `how="left"` also keeps the one without a promotion.
- `gross = odd["quantity"] * odd["unit_price"]`: gross sales (before the discount) of each row.
- `odd["as_fraction"] = ...`: net revenue if the discount is read as a fraction (26 = 2,600%).
- `odd["as_percent"] = ...`: net revenue if it's read as a percentage (26 = 26%), dividing by 100.
- `odd[[...]].round(2)`: shows only those columns, with 2 decimals.

> 🖱️ I'm clicking the Run cell button on the left of the fourth code cell, to compare both readings.

> 🖱️ I'm moving the mouse down the as_fraction column, in the middle of the table.

> 🟢 Eight transactions. Read as a fraction, every one gives a large negative revenue, like minus 998 dollars. That's impossible.

> 🖱️ I'm moving the mouse between the net_revenue and as_percent columns, on the right of the table.

> 🟢 Read as a percentage, the result matches the recorded net revenue to the cent, in all eight rows.

> 🖱️ I'm pointing at the planned_discount column, next to discount_rate.

> 🟢 And the values fit the campaigns: 25 where the plan is 25%, 22 where the plan is 20%. One row has no promotion, but its revenue also confirms 12%. Three independent pieces of evidence agree, so this is a data quality issue, a unit error, and not a real discount of 2,500%.

> 🖱️ I'm scrolling down below the table, and clicking the plus Code button in the toolbar at the top left, to add the fifth code cell.

> 🟢 This fifth code cell works on a copy of the sales, so the original stays untouched. It creates a new column, disc, with the discount as a fraction, keeping the original discount_rate column. Then it recalculates gross sales, net revenue, gross margin in dollars and in percent, and the difference with the recorded revenue.

> 🖱️ I'm typing the recalculation in the fifth code cell, in the middle of the screen.

> ⌨️ eval lets me write the formulas almost like plain math, one per line.

> ⌨️ At the end, I keep only the rows where the recorded revenue differs from mine by more than one cent.

**Celda 5:**

```python
df = sales.copy()
df["disc"] = df["discount_rate"].where(df["discount_rate"] <= 1, df["discount_rate"] / 100)
df = df.eval("""
gross = quantity * unit_price
calc_net = gross * (1 - disc)
calc_margin = calc_net - quantity * unit_cost
margin_pct = calc_margin / calc_net
diff = net_revenue - calc_net
""")
mismatch = df[df["diff"].abs() > 0.01]
mismatch[["transaction_id", "disc", "gross", "net_revenue", "calc_net", "gross_margin", "calc_margin"]].round(2)
```

📘 **What each line does** (para vos, no se lee):

- `df = sales.copy()`: a working copy. `sales`, the original, stays untouched.
- `df["disc"] = df["discount_rate"].where(df["discount_rate"] <= 1, df["discount_rate"] / 100)`: a new column with the discount as a fraction. It keeps values up to 1 and divides the others by 100. `discount_rate` stays as it was.
- `df = df.eval("""...""")`: calculates several columns from formulas written as text, one per line:
  - `gross`: quantity × price.
  - `calc_net`: recalculated net revenue = gross × (1 − discount).
  - `calc_margin`: recalculated gross margin in dollars = net revenue − quantity × cost.
  - `margin_pct`: the margin as a share of net revenue.
  - `diff`: recorded revenue − recalculated revenue.
- `mismatch = df[df["diff"].abs() > 0.01]`: rows where the difference is more than one cent (`abs` ignores the sign).
- `mismatch[[...]].round(2)`: shows those rows, with the columns to compare.

> 🖱️ I'm clicking the Run cell button on the left of the fifth code cell, to recalculate the money.

> 🖱️ I'm pointing at the number of rows in the result, six.

> 🟢 Out of 2,200 transactions, only six don't match. So the other 2,194, including the eight unit errors, reconcile to the cent.

> 🖱️ I'm moving the mouse between the gross and net_revenue columns of the six rows.

> 🟢 The pattern is clear: in these six rows, the recorded net revenue equals the gross sales. The discount, between 5% and 14%, was never subtracted. And the recorded gross margin follows that same revenue, so it's overstated too.

> 🟢 What I don't know is which side is wrong: maybe the customer got the discount and the revenue is wrong, or maybe the customer paid full price and the discount rate is wrong. The data can't tell me, so I won't correct these values. I keep them as recorded and document them as unresolved.

**Resultado esperado:** celda 4 con 8 filas (`T00769` 25 → planned 0.25 … `T01734` 12 → planned NaN); `as_percent` = `net_revenue` en todas; `as_fraction` negativo. Celda 5 con **6 filas**: `T00722`, `T01588`, `T01684`, `T01737`, `T01929`, `T02155`, con `net_revenue` = `gross` (por ejemplo, `T00722`: gross 90,42, recorded 90,42, calc_net 84,99).

**Razonamiento profesional:** la unidad del descuento se corrige **solo después** de que tres evidencias coinciden (ingreso registrado, tasa de la campaña, cálculo imposible como fracción), en una columna nueva y en una copia. En cambio, las 6 diferencias de ingreso **no** se corrigen, porque no hay evidencia de cuál valor es el correcto. El error típico es "arreglar" las dos cosas para que los totales cierren.

> 🟢 Now that the money is checked, let's look at how discounts move across categories and months.

---

## D. 10:30–14:00 — Análisis estadístico

> 🟢 Step three: discount patterns and the IQR screen.

> 🖱️ I'm scrolling down below the mismatch table, and clicking the plus Code button in the toolbar at the top left, to add the sixth code cell.

> 🟢 This sixth code cell adds the month and builds a table with the average discount for each category and month.

> 🖱️ I'm typing the pivot table in the sixth code cell.

**Celda 6:**

```python
df["month"] = df["date"].dt.month
df.pivot_table(index="category", columns="month", values="disc", aggfunc="mean").round(2)
```

📘 **What each line does** (para vos, no se lee):

- `df["month"] = df["date"].dt.month`: the month number, from 1 to 12.
- `df.pivot_table(index="category", columns="month", values="disc", aggfunc="mean").round(2)`: a table with categories as rows, months as columns, and the average discount in each cell.

> 🖱️ I'm clicking the Run cell button on the left of the sixth code cell, to see the pattern.

> 🖱️ I'm moving the mouse across the table, row by row, from Beauty at the top to Toys at the bottom.

> 🟢 Most months average between 3% and 6%. The peaks match the campaigns: Clothing in January, 15%, and March, 10%. Beauty in May, Sports in June, Electronics in November, and Toys in December.

> 🖱️ I'm pointing at Toys in April and August, at the bottom row of the table.

> 🟢 But Toys also jumps to 8% in April and August, with no campaign. Toys has very few sales per month, so a single large discount moves the whole average. That's exactly why small groups need care.

> 🖱️ I'm scrolling down below the table, and clicking the plus Code button in the toolbar at the top left, to add the seventh code cell.

> 🟢 This seventh code cell applies the IQR method inside each category and month. For each group, it calculates Q1 and Q3, the 25th and 75th percentiles, and the limit Q3 plus 1.5 times the IQR. A discount above that limit is an outlier, but only in groups with at least 20 transactions.

> 🖱️ I'm typing the IQR screen in the seventh code cell.

> ⌨️ transform gives every row the values of its own group, so each sale is compared with its category and month, not with the whole year.

> ⌨️ The print line tells me how many groups and rows are too small to screen.

**Celda 7:**

```python
g = df.groupby(["category", "month"])["disc"]
q1, q3, n = g.transform("quantile", 0.25), g.transform("quantile", 0.75), g.transform("size")
df["iqr_limit"] = q3 + 1.5 * (q3 - q1)
df["iqr_flag"] = (n >= 20) & (df["disc"] > df["iqr_limit"])
print("Groups below 20:", (g.size() < 20).sum(), "| rows not screened:", (n < 20).sum())
df[df["iqr_flag"]].groupby(["category", "month"]).size()
```

📘 **What each line does** (para vos, no se lee):

- `g = df.groupby(["category", "month"])["disc"]`: groups the discounts by category and month.
- `q1, q3, n = g.transform(...)`: for each row, the Q1, the Q3, and the size of **its own** group. `transform` returns one value per row, not one per group.
- `df["iqr_limit"] = q3 + 1.5 * (q3 - q1)`: the upper IQR limit of each group.
- `df["iqr_flag"] = (n >= 20) & (df["disc"] > df["iqr_limit"])`: True if the group has at least 20 sales **and** the discount is above the limit (`&` means "and").
- `print("Groups below 20:", ...)`: how many groups have fewer than 20 sales, and how many rows aren't screened with IQR.
- `df[df["iqr_flag"]].groupby(["category", "month"]).size()`: how many outliers there are in each group.

> 🖱️ I'm clicking the Run cell button on the left of the seventh code cell, to run the IQR screen.

> 🖱️ I'm pointing at the printed line, under the seventh code cell.

> 🟢 Eleven groups have fewer than 20 transactions: Toys, from January to November, with only 10 to 15 sales each. That's 135 sales I don't screen with IQR.

> 🟢 Why exclude them? With 10 sales, the quartiles depend on one or two values, so the limit isn't reliable: it would flag normal sales or miss real problems. Excluding them from IQR doesn't mean ignoring them. The 30% and 15% rules, coming next, still check every one of these sales.

> 🖱️ I'm moving the mouse down the list of flagged groups.

> 🟢 The screen flags 15 transactions in 9 groups. For example, three in Home & Kitchen in July, three in Electronics in May, and three in Electronics in December.

> 🟢 But a statistical outlier isn't a problem by itself. The three in December are Black Friday sales on December 1st, an authorized campaign. And the three in May are normal 13% to 15% discounts in a month where most Electronics sales had little or no discount. IQR tells me what's unusual, not what's wrong.

**Resultado esperado:** `Groups below 20: 11 | rows not screened: 135`. Grupos marcados: Beauty 3 (1), Beauty 11 (1), Electronics 2 (1), Electronics 5 (3), Electronics 10 (1), Electronics 12 (3), Home & Kitchen 7 (3), Home & Kitchen 11 (1), Sports & Outdoors 9 (1). Total 15.

**Razonamiento profesional:** el IQR se calcula **por grupo**, porque un 25% es normal en Black Friday y raro en febrero. El mínimo de 20 evita límites inestables, y se dice en voz alta que esas filas quedan cubiertas por las otras reglas. Un analista sin experiencia trata cada outlier como un error, o aplica el IQR a todo el año junto, y entonces cada campaña sale como anomalía.

> 🟢 Now let's check every promotion against the calendar.

---

## E. 14:00–17:30 — Validación de promociones

> 🟢 Step four: promotion validation.

> 🖱️ I'm scrolling down below the flagged groups, and clicking the plus Code button in the toolbar at the top left, to add the eighth code cell.

> 🟢 This eighth code cell joins every sale that has a promotion ID with the calendar, and runs five checks: the ID exists, the category matches, the date is inside the campaign, the discount is at or below the maximum, and it's within 5 percentage points of the planned discount. Then it shows every sale that fails at least one check.

> 🖱️ I'm typing the five checks in the eighth code cell.

> ⌨️ I validate all 188 promotion sales, not only the IQR outliers, because a wrong promotion can look statistically normal.

> ⌨️ The tolerance compares the distance to the planned discount with 0.05, five percentage points.

**Celda 8:**

```python
v = df[df["promotion_id"].notna()].merge(promos, on="promotion_id", how="left")
v["id_ok"] = v["planned_discount"].notna()
v["category_ok"] = v["category"] == v["applicable_category"]
v["dates_ok"] = v["date"].between(v["start_date"], v["end_date"])
v["max_ok"] = v["disc"] <= v["max_discount"]
v["tolerance_ok"] = (v["disc"] - v["planned_discount"]).abs().round(4) <= 0.05
checks = ["id_ok", "category_ok", "dates_ok", "max_ok", "tolerance_ok"]
issues = v[~v[checks].all(axis=1)]
issues[["transaction_id", "category", "promotion_id", "disc", "iqr_flag"] + checks]
```

📘 **What each line does** (para vos, no se lee):

- `v = df[df["promotion_id"].notna()].merge(promos, on="promotion_id", how="left")`: the sales with a promotion ID, joined with the calendar. If the ID doesn't exist, the campaign data stays empty.
- `v["id_ok"] = v["planned_discount"].notna()`: the ID exists if its planned discount was found.
- `v["category_ok"] = v["category"] == v["applicable_category"]`: the sale's category matches the campaign's category.
- `v["dates_ok"] = v["date"].between(v["start_date"], v["end_date"])`: the date is inside the campaign, including both ends.
- `v["max_ok"] = v["disc"] <= v["max_discount"]`: the discount doesn't exceed the approved maximum.
- `v["tolerance_ok"] = (v["disc"] - v["planned_discount"]).abs().round(4) <= 0.05`: the distance to the planned discount is 5 points or less. `round(4)` avoids decimal errors like 0.05000001.
- `checks = [...]`: a list with the names of the five checks.
- `issues = v[~v[checks].all(axis=1)]`: the sales that fail at least one check. `all(axis=1)` is True when all five are True, and `~` inverts it.
- `issues[[...] + checks]`: shows the key columns and the five checks.

> 🖱️ I'm clicking the Run cell button on the left of the eighth code cell, to validate the promotions.

> 🖱️ I'm pointing at the number of rows of the result, 17.

> 🟢 17 of the 188 promotion sales fail at least one check. Let me go through them by type.

> 🖱️ I'm pointing at the three PRM-99 rows, in the middle of the table.

> 🟢 PRM-99, 35% off: the ID doesn't exist, so every other check fails too, because there's nothing to compare with. That's a policy violation.

> 🖱️ I'm pointing at the three PRM-07 rows at the bottom, with category_ok False.

> 🟢 PRM-07 is the Black Friday campaign for Electronics, but here it was used on Beauty, Toys, and Home & Kitchen. The dates and the rate are fine, the category isn't.

> 🖱️ I'm pointing at the four PRM-02 rows, with dates_ok False.

> 🟢 PRM-02, Spring Fashion, ended on March 31st, but these four sales are from April. A hypothesis is that the campaign was extended informally. But that's a hypothesis: the calendar doesn't show it, so it stays a violation until someone confirms it.

> 🖱️ I'm pointing at the three PRM-05 rows, with max_ok False.

> 🟢 PRM-05 allows up to 25%, and these three sales got 32% and 33%. Above the approved maximum: a clear violation.

> 🖱️ I'm pointing at the four PRM-01 rows at the top, where only tolerance_ok is False.

> 🟢 These are the ambiguous cases. PRM-01, Winter Clearance, plans 30% with a maximum of 40%. Three sales got 37% and 38%: inside the maximum, but more than 5 points above the plan. And one got 22%, more than 5 points below. None breaks the maximum, so they're not violations of the limit. They're deviations from the plan that a manager should explain. The 22% one even cost the company less than planned.

> 🖱️ I'm moving the mouse down the iqr_flag column.

> 🟢 And notice: only 5 of these 17 were IQR outliers. Most promotion problems look statistically normal, so the calendar check is essential.

**Resultado esperado:** **17 filas**. PRM-01 (4): 0,37, 0,38, 0,37 y 0,22, solo `tolerance_ok` False. PRM-02 (4): `dates_ok` False. PRM-05 (3): 0,32, 0,33, 0,32, `max_ok` y `tolerance_ok` False. PRM-99 (3): todo False, `iqr_flag` True. PRM-07 (3, Beauty, Toys, Home & Kitchen): `category_ok` False. `iqr_flag` True en 5 de las 17.

**Razonamiento profesional:** se validan **todas** las ventas con promoción, no solo las que marcó el IQR, porque el IQR mide lo raro, no lo autorizado. Las cinco comprobaciones se muestran por separado para que cada caso tenga su motivo. Error típico: dar por bueno un descuento solo porque tiene un ID de promoción, o tratar igual una desviación dentro del máximo que una que lo supera.

> 🟢 Next, the two business rules that don't depend on the statistics.

---

## F. 17:30–22:00 — Investigación de negocio y financiera

> 🟢 Step five: business rules and financial impact.

> 🖱️ I'm scrolling down below the validation table, and clicking the plus Code button in the toolbar at the top left, to add the ninth code cell.

> 🟢 This ninth code cell marks a sale as authorized when its promotion ID exists, matches the category, and is inside the dates. Then it flags every discount above 30% outside an authorized promotion, and shows whether IQR had caught it.

> 🖱️ I'm typing the over-30% rule in the ninth code cell.

> ⌨️ Authorized here only means a valid campaign. The maximum and the tolerance were already checked in the previous cell.

**Celda 9:**

```python
ok = v["id_ok"] & v["category_ok"] & v["dates_ok"]
df["authorized"] = df["transaction_id"].isin(v.loc[ok, "transaction_id"])
df["over_30"] = (df["disc"] > 0.30) & ~df["authorized"]
df.loc[df["over_30"], ["transaction_id", "category", "month", "promotion_id", "disc", "iqr_limit", "iqr_flag"]].round(2)
```

📘 **What each line does** (para vos, no se lee):

- `ok = v["id_ok"] & v["category_ok"] & v["dates_ok"]`: a valid promotion: the ID exists, the category is right, and the date is inside the campaign.
- `df["authorized"] = df["transaction_id"].isin(v.loc[ok, "transaction_id"])`: True if the sale is in that list of valid promotions.
- `df["over_30"] = (df["disc"] > 0.30) & ~df["authorized"]`: a discount above 30% without an authorized promotion.
- `df.loc[df["over_30"], [...]].round(2)`: shows those sales, with their IQR limit and whether IQR had flagged them.

> 🖱️ I'm clicking the Run cell button on the left of the ninth code cell, to apply the rule.

> 🖱️ I'm pointing at the number of rows of the result, 10.

> 🟢 Ten sales got more than 30% outside an authorized promotion: seven without any promotion, from 35% to 55%, and the three PRM-99 sales.

> 🖱️ I'm moving the mouse down the iqr_flag column, to the rows with False.

> 🟢 And here's why this rule must be independent: IQR missed three of them. Two are in Toys, in April and August, the small groups that IQR doesn't screen. The third is in Clothing in January, with 36%: the Winter Clearance campaign pushed that month's IQR limit up to 75%, so a 36% discount without any promotion looked normal.

> 🖱️ I'm scrolling down below the table, and clicking the plus Code button in the toolbar at the top left, to add the tenth code cell.

> 🟢 This tenth code cell flags every sale with a gross margin below the 15% floor, and counts them by category, with and without an authorized promotion.

> 🖱️ I'm typing the margin check in the tenth code cell.

**Celda 10:**

```python
df["low_margin"] = df["margin_pct"] < 0.15
pd.crosstab(df.loc[df["low_margin"], "category"], df["authorized"], margins=True)
```

📘 **What each line does** (para vos, no se lee):

- `df["low_margin"] = df["margin_pct"] < 0.15`: True if the margin is below 15%.
- `pd.crosstab(df.loc[df["low_margin"], "category"], df["authorized"], margins=True)`: counts the low-margin sales by category, split by whether they had an authorized promotion. `margins=True` adds the totals (All).

> 🖱️ I'm clicking the Run cell button on the left of the tenth code cell, to count the low margins.

> 🖱️ I'm pointing at the All row at the bottom of the table.

> 🟢 72 sales are below 15%: 37 without an authorized promotion and 35 inside one. An authorized promotion doesn't make a sale profitable.

> 🖱️ I'm pointing at the Electronics row, at the top.

> 🟢 66 of the 72 are Electronics. Electronics has the thinnest margin, about 24% on normal sales, so even an ordinary 12% to 15% discount takes it below the floor. That's not an error in the data: it's how the cost structure works. The other six are the extreme discounts we already saw.

> 🖱️ I'm scrolling down below the table, and clicking the plus Code button in the toolbar at the top left, to add the eleventh code cell.

> 🟢 This eleventh code cell compares each campaign with the same category without a promotion: number of sales, average units per sale, revenue, gross profit, and gross margin.

> 🖱️ I'm typing the comparison in the eleventh code cell.

> ⌨️ Sales that aren't authorized go into the "None" group, the baseline of each category.

> ⌨️ The margin is total profit over total revenue, not an average of percentages, so big sales weigh more.

**Celda 11:**

```python
df["promo"] = df["promotion_id"].where(df["authorized"], "None")
perf = df.groupby(["category", "promo"]).agg(sales=("quantity", "size"), avg_units=("quantity", "mean"),
                                             revenue=("calc_net", "sum"), profit=("calc_margin", "sum"))
perf["margin_pct"] = perf["profit"] / perf["revenue"]
perf.round(2)
```

📘 **What each line does** (para vos, no se lee):

- `df["promo"] = df["promotion_id"].where(df["authorized"], "None")`: keeps the ID if the promotion is authorized. If not, it writes "None", the baseline without a promotion.
- `perf = df.groupby(["category", "promo"]).agg(...)`: for each category and campaign: number of sales, average units per sale, total revenue, and total gross profit.
- `perf["margin_pct"] = perf["profit"] / perf["revenue"]`: the weighted margin = total profit ÷ total revenue.
- `perf.round(2)`: shows the table with 2 decimals.

> 🖱️ I'm clicking the Run cell button on the left of the eleventh code cell, to compare the campaigns.

> 🖱️ I'm moving the mouse down the avg_units column.

> 🟢 Every campaign increases volume: promotion sales average between 2.7 and 3.7 units, against about 1.7 without a promotion. So the campaigns do what they're meant to do.

> 🖱️ I'm moving the mouse down the margin_pct column, comparing each campaign with the None row above it.

> 🟢 And every campaign lowers the margin, as expected. Most stay well above 15%: for example, Summer Sports keeps 29%, against 42% without a promotion.

> 🖱️ I'm pointing at the PRM-07 row, in the Electronics group.

> 🟢 Except PRM-07, Black Friday Electronics. It doubled the units per sale, 3.3 against 1.66, and brought almost 28,000 dollars of revenue, but kept only 732 dollars of gross profit: a 3% margin, against 24% for normal Electronics sales. PRM-06, the other Electronics campaign at 10%, kept 19%.

> 🟢 Now, evidence versus hypothesis. The evidence: PRM-07 was authorized and breaks the margin floor. The hypothesis: it may be intentional, a loss leader to bring customers in for later purchases. This data can't confirm that, because I don't see repeat customers. So I report the fact and leave the intent as a question for the business.

**Resultado esperado:** celda 9 con **10 filas** (`T00123` Clothing mes 1, 0,36, límite 0,75, False · `T00262` Electronics 0,40 · `T00459` Beauty 0,50 · `T00649` Toys mes 4, 0,40, False · 3 × PRM-99 0,35 · `T01356` Toys mes 8, 0,55, False · `T01606` Sports 0,45 · `T01679` Electronics 0,35). Celda 10: All 37 / 35 / 72; Electronics 31 / 35 / 66; Home & Kitchen 3; Sports & Outdoors 1; Toys 2. Celda 11: Electronics None 423 ventas, 1,66 unidades, margen 0,24 · PRM-06 22, 3,32, 0,19 · **PRM-07 33, 3,30, revenue 27.874,68, profit 732,29, margen 0,03**. Sports None 0,42 vs PRM-05 0,29.

**Razonamiento profesional:** las reglas de 30% y 15% se aplican a **todas** las ventas, sin pasar por el IQR, porque son reglas de negocio, no estadísticas. El IQR se pierde justo los casos de grupos chicos o de meses con campaña. Error típico: suponer que una promoción autorizada es rentable, o atribuir intención comercial ("es un loss leader") sin datos que lo prueben.

---

## G. 22:00–23:30 — Recomendaciones

Sin código. Hacés scroll hacia arriba por los resultados mientras hablás.

> 🟢 Step six: recommendations, each one tied to a number I calculated.

> 🖱️ I'm scrolling up to the fifth and eighth code cells, the mismatches and the promotion checks.

> 🟢 First, individual review: the 6 sales whose revenue ignores the discount, the 17 promotion check failures, and the 10 discounts above 30% outside a promotion. Each of these is a specific transaction someone can look up.

> 🖱️ I'm scrolling down to the ninth code cell, the over-30% table.

> 🟢 Second, approval controls. The system accepted an ID that doesn't exist, a campaign on the wrong category, a campaign after its end date, and discounts above the approved maximum. Those should be blocked at checkout. Discounts above 30% without a promotion should require approval. And discounts should be stored in one unit only, as fractions, because 8 were saved as percentages.

> 🖱️ I'm scrolling down to the eleventh code cell, the campaign comparison.

> 🟢 Third, campaign rate review: PRM-07. At 25%, Electronics keeps a 3% margin. At 10%, PRM-06 kept 19%. So the Black Friday rate should be reviewed, unless the business confirms that the low margin is a deliberate choice.

> 🟢 Now let's validate the results before exporting.

**Razonamiento profesional:** cada recomendación nace de un número que está en pantalla. Error típico: recomendar "revisar la política de descuentos" en general, sin decir qué transacciones ni qué campaña.

---

## H. 23:30–27:00 — Validación y entregables

> 🟢 Step seven: validation and deliverables.

> 🖱️ I'm scrolling down to the end of the notebook, and clicking the plus Code button in the toolbar at the top left, to add the twelfth code cell.

> 🟢 This twelfth code cell reconciles the revenue: the recorded total, the recalculated total, and their difference. Then it compares that difference with the six mismatches, and checks that the category totals add up to the overall total.

> 🖱️ I'm typing the reconciliation in the twelfth code cell.

**Celda 12:**

```python
print(df[["net_revenue", "calc_net", "diff"]].sum().round(2))
print("Mismatches:", mismatch["diff"].sum().round(2))
print("Sum of categories:", df.groupby("category")["calc_net"].sum().sum().round(2))
```

📘 **What each line does** (para vos, no se lee):

- `print(df[["net_revenue", "calc_net", "diff"]].sum().round(2))`: adds up the recorded revenue, the recalculated revenue, and the difference.
- `print("Mismatches:", mismatch["diff"].sum().round(2))`: how much of the difference comes from the 6 rows that don't match.
- `print("Sum of categories:", ...)`: adds up the totals of every category, to compare them with the overall total.

> 🖱️ I'm clicking the Run cell button on the left of the twelfth code cell, to reconcile.

> 🖱️ I'm pointing at the first three lines of the output.

> 🟢 Recorded net revenue is 489,707.18 dollars, and my recalculation is 489,648.79. The difference is 58.39 dollars.

> 🖱️ I'm pointing at the Mismatches line.

> 🟢 58.35 of it comes from the six sales without the discount. The remaining 4 cents is rounding, because the recorded values have two decimals. So the difference is fully explained, and I didn't change any source value to make it match. The 58.35 stays as an unresolved discrepancy in the summary.

> 🖱️ I'm pointing at the Sum of categories line.

> 🟢 The six categories add up to 489,648.79, exactly the recalculated total. No sale was lost or counted twice.

> 🖱️ I'm scrolling down below the output, and clicking the plus Code button in the toolbar at the top left, to add the thirteenth code cell.

> 🟢 This thirteenth code cell adds two last flags, promotion issues and data issues, keeps every sale with at least one flag, exports them to flagged_transactions.csv, and counts each reason.

> 🖱️ I'm typing the export in the thirteenth code cell.

> ⌨️ Each flag stays as its own True or False column in the file, so a reviewer can filter by reason.

**Celda 13:**

```python
df["promo_issue"] = df["transaction_id"].isin(issues["transaction_id"])
df["data_issue"] = (df["diff"].abs() > 0.01) | (df["discount_rate"] > 1)
flags = ["iqr_flag", "data_issue", "promo_issue", "over_30", "low_margin"]
flagged = df[df[flags].any(axis=1)]
flagged.to_csv("flagged_transactions.csv", index=False)
flagged[flags].sum()
```

📘 **What each line does** (para vos, no se lee):

- `df["promo_issue"] = df["transaction_id"].isin(issues["transaction_id"])`: True if the sale failed any promotion check.
- `df["data_issue"] = (df["diff"].abs() > 0.01) | (df["discount_rate"] > 1)`: True if the revenue doesn't match or the discount was stored as a percentage (`|` means "or").
- `flags = [...]`: the five review reasons.
- `flagged = df[df[flags].any(axis=1)]`: the sales with at least one reason (`any` means at least one is True).
- `flagged.to_csv("flagged_transactions.csv", index=False)`: saves those sales to a CSV, without the index column.
- `flagged[flags].sum()`: how many sales each reason has (True counts as 1).

> 🖱️ I'm clicking the Run cell button on the left of the thirteenth code cell, to export the file.

> 🖱️ I'm moving the mouse down the counts, under the thirteenth code cell.

> 🟢 15 IQR outliers, 14 data issues, the 8 unit errors plus the 6 mismatches, 17 promotion issues, 10 discounts above 30%, and 72 low margins. Some sales have several reasons, so the file has 104 transactions, not the sum.

> 🖱️ I'm scrolling down to the end of the notebook, and clicking the plus Text button in the toolbar at the top left, to add the summary cell.

> 🟢 This last cell summarizes the findings, separated into the four types, and the final notes.

> 🖱️ I'm typing the summary in the new text cell, at the bottom of the notebook.

```markdown
## Summary of findings
- **Data quality:** 8 discounts are stored as percentages (net revenue confirms the fraction), and 6 transactions record net revenue without the discount (+$58.35). Those source values were kept and are documented, not corrected.
- **Statistical anomalies:** 15 IQR outliers. 11 Toys groups have fewer than 20 transactions and were not screened. 3 outliers belong to an authorized Black Friday promotion.
- **Policy violations:** 17 promotion check failures (unknown PRM-99, PRM-07 on the wrong category, PRM-02 after its end date, PRM-05 above its maximum) and 10 discounts above 30% outside authorized promotions. IQR missed 3 of the 10.
- **Margin:** 72 transactions are below the 15% floor, 35 of them in authorized promotions. PRM-07 doubled the units per sale (3.3 vs 1.7) but kept only a 3% margin.
- **Recommendations:** review the flagged transactions, validate promotion IDs, categories, dates, and limits at checkout, require approval above 30%, and review the PRM-07 discount rate.

## Final notes
- The two synthetic input files were generated by Gemini before recording. The original files were not modified.
```

Ver "Pendientes": la última línea tiene que ser **cierta**.

> 🖱️ I'm clicking the empty area below the summary cell, to close the editor and show the formatted text.

> 🖱️ I'm pressing Command + S to save the notebook in Drive.

> 🖱️ I'm opening the File menu at the top left, choosing Download, then Download .ipynb, to keep the notebook for the deliverables.

> 🖱️ I'm clicking the Files icon in the left sidebar, then the three dots next to flagged_transactions.csv, and choosing Download.

**Resultado esperado:** celda 12: `net_revenue 489707.18`, `calc_net 489648.79`, `diff 58.39`, `Mismatches: 58.35`, `Sum of categories: 489648.79`. Celda 13: iqr_flag 15, data_issue 14, promo_issue 17, over_30 10, low_margin 72. El archivo tiene **104 filas**.

**Razonamiento profesional:** la conciliación demuestra que la diferencia está **explicada**, no que se hizo desaparecer. El total por categorías confirma que no se perdieron filas en los `groupby`. Error típico: reemplazar el ingreso registrado por el recalculado para que "cierre", y borrar la evidencia del problema.

> 🟢 Let me show the final results.

---

## I. 27:00–28:30 — Presentación final

> 🟢 Step eight: the final deliverables.

> 🖱️ I'm double-clicking flagged_transactions.csv in the Files panel on the left, to open it in Colab's file viewer.

Si Colab no abre un visor, agregá una celda con `flagged.head()` y mostrá la tabla.

> 🖱️ I'm scrolling right across the columns of the file, to the five flag columns at the end.

> 🟢 This is the export: 104 transactions, with the original columns, my recalculated values, and one column for each reason, so the review team can filter, for example, only the policy violations.

> 🖱️ I'm closing the file viewer tab at the top, and clicking the Files icon in the left sidebar to close the panel.

> 🖱️ I'm clicking the Downloads arrow at the top right of Firefox, to show the notebook and the flagged transactions file.

> 🖱️ I'm clicking an empty area of the page to close the Downloads panel, and scrolling down to the summary cell, at the bottom of the notebook.

> 🟢 And this is the summary, with the four types of findings, the recommendations, and the final notes. That completes the analysis.

---

## J. 28:30–32:00 — Epílogo

Dura **menos de 4 minutos**. No repitas los pasos: reflexioná.

> 🖱️ I'm scrolling up slowly through the notebook with the mouse wheel, in the center of the screen.

> 🟢 Let me reflect on what I found. The most significant finding isn't the biggest discount. It's PRM-07: an authorized campaign, with no rule broken, that turned about 28,000 dollars of Electronics revenue into only 732 dollars of gross profit. None of the policy checks would catch that. Only the margin analysis does.

> 🟢 The hardest decisions were about what not to change. The eight percentage values had three pieces of evidence, so I converted them, in a new column, keeping the original. The six revenue mismatches had no evidence of which side was right, so I left them as recorded and documented the 58 dollars. Forcing them to match would have hidden a real problem.

> 🟢 This project also showed the difference between a statistical anomaly and a business problem. IQR flagged authorized Black Friday sales and normal Electronics discounts, which aren't problems. And it missed three discounts above 30% with no promotion, which are. Statistics tell me what's unusual. Business rules tell me what's wrong. I needed both, and independent.

> 🟢 Financially, the controls matter more than the individual cases. The six mismatches are only 58 dollars. But a system that accepts a promotion ID that doesn't exist, or a campaign after its end date, will repeat those errors.

> 🟢 There are limits. The data is synthetic and covers one year. I can't see customers, so I can't test whether Black Friday brought repeat buyers, and I can't tell whether April's use of Spring Fashion was an informal extension. As next steps, I'd confirm those cases with the commercial team, add customer data to measure the long-term effect of campaigns, and turn these checks into an automatic monthly report. Thanks for watching!

Si el reloj todavía no pasó los 15:00 (no debería pasar), no cortes: abrí la celda 11 y compará cada campaña con su categoría, una por una.

---

## Si algo sale mal (frases para corregir)

Siempre decí **qué** corregís y **en qué celda**:

| Error | Qué pasa | Qué decís y hacés |
| ----- | -------- | ----------------- |
| `KeyError` con una columna | Nombre mal escrito (por ejemplo `discount` en vez de `disc`) | 🖱️ *"There's a KeyError in the ninth code cell, because I typed discount instead of disc. I'm fixing the name on that line and clicking Run again."* |
| `NameError` (`df`, `v`, `issues`, `mismatch`) | Una celda anterior no se ejecutó | 🖱️ *"There's a NameError, because an earlier cell didn't run. I'm opening the Runtime menu at the top and choosing Run before."* |
| `FileNotFoundError` en la celda 1 | Los CSV no se subieron o se borraron al reiniciar | 🖱️ *"The first code cell can't find the files. I'm opening the Files panel on the left, uploading both CSV files again, and running the cell again."* |
| `UndefinedVariableError` en la celda 5 | Error de tipeo dentro del texto de `eval` | 🖱️ *"There's a typo inside the eval formulas in the fifth code cell. I'm fixing the column name and running it again."* |
| Error de sintaxis | Falta un paréntesis o una comilla | 🖱️ *"There's a syntax error on the line Colab underlines. I'm adding the missing parenthesis and running the cell again."* |
| Un número distinto del guion | Otra versión de pandas o una celda corrida dos veces | Decí el número que ves. Si una celda se corrió dos veces, usá **Runtime → Run before** y volvé a correrla. No digas números que no estén en pantalla. |

---

## Línea de tiempo estimada

| Sección | Tiempo | Duración |
| ------- | ------ | -------- |
| A. Apertura (intro de menos de 20 s + subir archivos + enfoque) | 0:00–2:00 | 2:00 |
| B. Carga e inspección (celdas 1–3) | 2:00–6:00 | 4:00 |
| C. Cálculos financieros y unidades (celdas 4–5) | 6:00–10:30 | 4:30 |
| D. Patrones e IQR (celdas 6–7) | 10:30–14:00 | 3:30 |
| E. Validación de promociones (celda 8) | 14:00–17:30 | 3:30 |
| F. 30%, 15% y campañas (celdas 9–11) | 17:30–22:00 | 4:30 |
| G. Recomendaciones | 22:00–23:30 | 1:30 |
| H. Conciliación, exportación, resumen y guardado (celdas 12–13 + texto) | 23:30–27:00 | 3:30 |
| I. Presentación final | 27:00–28:30 | 1:30 |
| J. Epílogo | 28:30–32:00 | 3:30 |

Si tipeás más lento, la grabación se alarga, y está bien: el máximo es 50:59. Lo que no puede pasar es que el tipeo supere el 25% (ver "Pendientes").

---

## Después de grabar

1. Abrí TaskRecorder **solo cuando terminó el epílogo**.
2. Ejecutá **Run full AutoQC**, no solo *Rerun failing*. Revisá que el porcentaje de acciones con What + Where pase el **70%** y que el tipeo esté por debajo del **25%**.
3. Armá **Deliverables.zip** con el `.ipynb` descargado al final, `flagged_transactions.csv` y los **dos CSV originales** (sin modificar).
4. Subí los **cuatro archivos por separado**: el **MP4**, el **ZIP original de TaskRecorder**, **Deliverables.zip** y **Metadata.rtf**.
