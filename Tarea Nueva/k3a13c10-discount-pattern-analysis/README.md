# k3a13c10 — Analyze Discount Patterns in Sales Data Using Python and Pandas

Guion para grabar la tarea **k3a13c10**. En **Google Colab**, con **pandas**, trabajás sobre 2.200 ventas sintéticas de 2025 con problemas reales:

- corregís las unidades del descuento con evidencia;
- detectás los descuentos inusuales;
- validás las promociones;
- medís en dólares cuánto margen cuestan;
- **reescribís los dos archivos de entrada**.

Todo se **tipea y se explica en vivo**, intercalado, en **una sola toma**, en **Firefox**.

**Duración estimada: ~45 minutos**, con el método que acertó tu medición real de 75 minutos (ver "Cronograma"). Quedan unos 6 minutos de margen hasta el máximo de 50:59.

**Cómo leer este guion:**

- 🟢 = lo decís **antes** de tipear: qué vas a hacer en esa celda. O **después** de ejecutar: qué muestra el resultado y qué decidís.
- ⌨️ = lo decís **mientras tipeás** el código que está **justo debajo**. Dice qué tipeás y qué hace.
- 🖱️ = lo decís **mientras hacés** una acción con el mouse: qué, dónde y por qué. AutoQC cuenta estas frases.
- 📘 = la explicación de cada línea, en inglés. Es para vos: **no se lee**.
- **Resultado esperado** = lo que tiene que aparecer. Es para vos.

**El ritmo de cada celda:**

1. 🖱️ **+ Code**.
2. 🟢 Qué vas a hacer.
3. ⌨️ Frase → tipeás el bloque de abajo → ⌨️ frase → tipeás el bloque siguiente → …
4. 🖱️ **Run**.
5. 🖱️ Señalás el resultado → 🟢 lo explicás.

---

## Pendientes antes de grabar

| Tema | Qué hacer |
| ---- | --------- |
| **Origen de los CSV** | Los generé yo, Claude, con un script de Python: "generated with AI" es cierto, "Gemini" no. Marcá en Studio la opción de archivos generados con IA. |
| **Porcentaje de tipeo** | Cerca del 65%. Con todo en vivo no baja al 25–30%. Confirmá el límite en las guías. |
| **Versión de pandas** | Lo probé con pandas 3.1. Si `info()` dice `object` en vez de `str`, es lo mismo. |

---

## Qué cumple y dónde (criterios de Slack + Goal)

| Criterio o requisito | Dónde |
| -------------------- | ----- |
| Carga, dimensiones, tipos y faltantes | Step 1 |
| Corrección de unidades con evidencia, sin perder el original | Step 2 (`disc`) y Step 9 (`discount_raw`) |
| Descuentos atípicos por categoría y mes, IQR, mínimo de 20, justificación de los ceros | Step 3 |
| 5 validaciones del calendario y tabla visible | Step 4 |
| Reglas del 30% y del 15%, independientes | Step 5 |
| Con y sin promoción, por categoría, por promoción y ajuste por mezcla | Step 6 |
| **Impacto en dólares:** costo total, exceso de los inusuales, distancia al piso y PRM-07 | Steps 2, 6 y 7 |
| Reconciliación de las categorías contra el total | Step 8 |
| **Modificación material de los dos archivos de entrada** | Step 9 |
| Exportar las ventas marcadas y el resumen | Step 9 |
| Conclusiones con prioridad económica y declaración de IA | Celda de texto |

---

## La regla del mouse

1. El mouse **solo se mueve con una frase 🖱️**. Mientras tipeás, soltalo.
2. Al terminar una acción, el cursor queda **quieto en el margen derecho**, lejos de los botones.
3. **Primero la frase, después el movimiento.** Leé el guion con el mouse quieto.
4. Si hacés algo fuera del guion, usá una frase comodín:
   - *"I'm scrolling right inside the table, to see the last columns."*
   - *"I'm clicking at the end of the line, to fix a typo."*
   - *"I'm pressing Escape to close the suggestion box."* Si Colab muestra una caja de sugerencias, **no la aceptes**: con la caja abierta, Enter inserta la sugerencia. Apretá Escape y seguí tipeando.

---

## Guion de grabación

### A. Apertura (~1 min)

Con la **descripción de la tarea** en pantalla, en menos de 20 segundos:

> 🟢 I will be beginning my task soon. I'll analyze discount patterns in sales data with pandas, measure their cost in margin dollars, and update the input files.

> 🖱️ I'm clicking the yellow minimize button at the top left, then the Firefox icon in the Dock, and choosing the second window, my empty Colab notebook.

> 🖱️ I'm opening the Files panel on the left: both CSV files are uploaded. They're synthetic, generated with AI, and the originals stay on my Desktop.

> 🖱️ I'm closing the Files panel and clicking inside the empty code cell at the top.

---

### B. Step 1: carga e inspección

> 🟢 Step one: loading and inspection.

> ⌨️ I'm typing the import and reading the sales file, with real dates for the campaign checks.

```python
import pandas as pd
s = pd.read_csv("sales_transactions.csv", parse_dates=["date"])
```

> ⌨️ Now the promotion calendar, with its start and end dates as dates too.

```python
p = pd.read_csv("promotion_calendar.csv", parse_dates=["start_date", "end_date"])
```

> ⌨️ info shows the size, the types, and the missing values of each file, and describe shows the ranges of the numbers.

```python
s.info()
p.info()
s.describe()
```

> 🖱️ I'm clicking the Run button on the left of the cell.

> 🖱️ I'm pointing at the top of the first output: RangeIndex, 2,200 entries, and 10 columns.

> 🟢 2,200 sales, one row per transaction, and the date is already a real datetime.

> 🖱️ I'm moving the mouse down the Non-Null Count column, to promotion_id.

> 🟢 Every column has 2,200 values except promotion_id, with 188. An empty ID means the sale had no promotion, so I keep it empty. Below, the calendar has 8 campaigns and no gaps.

> 🖱️ I'm scrolling down to the describe table, and pointing at the max row of discount_rate.

> 🟢 The 75th percentile is 0.10, but the maximum is 26. As a fraction that's 2,600%, so some values look like percentages. I'll test that against the revenue before changing anything.

> 🖱️ I'm pointing at the min of gross_margin, in the same row of minimums.

> 🟢 The minimum gross margin is negative, minus 62 dollars: some sales lost money. The 15% rule will catch them.

📘 **What each line does** (para vos, no se lee):

- `import pandas as pd`: loads pandas with the short name `pd`.
- `s = pd.read_csv("sales_transactions.csv", parse_dates=["date"])`: reads the sales into `s`. `parse_dates` turns `date` into a real date.
- `p = pd.read_csv("promotion_calendar.csv", parse_dates=["start_date", "end_date"])`: reads the calendar into `p`, with both dates as real dates.
- `s.info()`: the rows, columns, non-null count (so, missing values) and type of each sales column.
- `p.info()`: the same for the calendar.
- `s.describe()`: count, mean, min, quartiles and max of the numeric and date columns.

**Resultado esperado (dónde mirar):**

- **Primer `info()`, arriba:** `RangeIndex: 2200 entries`, `10 columns`. En **Non-Null Count**, todo dice 2200 salvo `promotion_id` (188 non-null). `date` es `datetime64`.
- **Segundo `info()`:** `8 entries`, 7 columnas, todo con 8 non-null.
- **`describe()`:** en `discount_rate`, la fila `75%` dice 0,10 y la fila `max` dice **26,0**. En `gross_margin`, `min` = **−62,45**.

---

### C. Step 2: preparación del dinero

> 🖱️ I'm clicking plus Code at the top left, to add the second cell.

> 🟢 Step two: fix the discount units and recalculate the money, in new columns.

> ⌨️ disc is the discount as a fraction: values up to 1 stay, larger ones are divided by 100.

```python
s["disc"] = s.discount_rate.where(s.discount_rate <= 1, s.discount_rate / 100)
```

> ⌨️ The month, and the gross sales: quantity times price.

```python
s["month"] = s.date.dt.month
s["gross"] = s.quantity * s.unit_price
```

> ⌨️ Net revenue after the discount, and gross profit after the cost.

```python
s["net"] = s.gross * (1 - s.disc)
s["profit"] = s.net - s.quantity * s.unit_cost
```

> ⌨️ diff compares the recorded revenue with mine.

```python
s["diff"] = s.net_revenue - s.net
```

> ⌨️ Two money columns: cost, the margin each discount gives away, and gap15, the profit dollars missing to reach the 15% floor.

```python
s["cost"] = s.gross * s.disc
s["gap15"] = (0.15 * s.net - s.profit).clip(lower=0)
```

> ⌨️ And I show the sales where my revenue differs by more than one cent.

```python
s[s["diff"].abs() > 0.01]
```

> 🖱️ I'm clicking Run on the left of the second cell.

> 🖱️ I'm pointing at the row count under the table: six rows.

> 🟢 Only six of 2,200 sales don't reconcile. That also proves the conversion: the eight values I divided by 100 now match the recorded revenue, so they really were percentages.

> 🖱️ I'm pointing at the first row, T00722, between net_revenue and net.

> 🟢 Recorded 90.42, mine 84.99. And 90.42 is exactly the gross column: the 6% discount was never subtracted.

> 🖱️ I'm moving the mouse down the disc column of the six rows.

> 🟢 Discounts from 5 to 14%, all ignored. I can't tell whether the revenue or the discount is wrong, so I keep them as recorded, as a data issue.

📘 **What each line does** (para vos, no se lee):

- `s["disc"] = s.discount_rate.where(s.discount_rate <= 1, s.discount_rate / 100)`: the discount as a fraction. It keeps values up to 1 and divides the others by 100. `discount_rate` doesn't change.
- `s["month"] = s.date.dt.month`: the month number (1–12).
- `s["gross"] = s.quantity * s.unit_price`: gross sales, before the discount.
- `s["net"] = s.gross * (1 - s.disc)`: recalculated net revenue.
- `s["profit"] = s.net - s.quantity * s.unit_cost`: recalculated gross profit.
- `s["diff"] = s.net_revenue - s.net`: recorded minus recalculated revenue.
- `s["cost"] = s.gross * s.disc`: the margin given away by the discount, in dollars.
- `s["gap15"] = (0.15 * s.net - s.profit).clip(lower=0)`: the profit dollars missing to reach a 15% margin. `clip(lower=0)` turns negatives into 0.
- `s[s["diff"].abs() > 0.01]`: the sales whose difference is more than one cent. `s["diff"]` uses brackets because `s.diff` is a pandas method.

**Resultado esperado (dónde mirar):**

- **Tabla de 6 filas** debajo de la celda: `T00722`, `T01588`, `T01684`, `T01737`, `T01929`, `T02155`.
- **Primera fila:** `gross` 90,42 = `net_revenue` 90,42; `net` 84,99; `diff` 5,43; `disc` 0,06.
- **Columna `disc`:** valores entre 0,05 y 0,14.

---

### D. Step 3: descuentos inusuales con IQR

> 🖱️ I'm clicking plus Code at the top left, to add the third cell.

> 🟢 Step three: unusual discounts, comparing each sale with its own category and month.

> ⌨️ I group the discounts by category and month.

```python
g = s.groupby(["category", "month"]).disc
```

> ⌨️ transform gives each sale its group's quartiles and size.

```python
q1, q3, n = g.transform("quantile", 0.25), g.transform("quantile", 0.75), g.transform("size")
```

> ⌨️ An outlier is above Q3 plus 1.5 times the IQR, only in groups of 20 or more.

```python
s["iqr"] = (n >= 20) & (s.disc > q3 + 1.5 * (q3 - q1))
```

> ⌨️ I print how many sales are in small groups, and the share of sales with no discount. Then the outliers.

```python
print((n < 20).sum(), (s.disc == 0).mean().round(2))
s[s.iqr]
```

> 🖱️ I'm clicking Run on the left of the third cell.

> 🖱️ I'm pointing at the printed line above the table: 135 and 0.56.

> 🟢 135 sales are in groups with fewer than 20 sales, all Toys months, so IQR doesn't screen them; the business rules will. And 56% of all sales have no discount, so Q1 is zero and the limit is about 2.5 times Q3. Using only discounted sales would leave just 8 groups, so I keep this version.

> 🖱️ I'm pointing at the row count under the table: 15 rows.

> 🟢 15 outliers out of 2,200.

> 🖱️ I'm scrolling right to the promotion_id column, and pointing at the PRM-99 rows and the December PRM-07 rows.

> 🟢 Three are PRM-99, an ID I'll check in the next step. Three are Black Friday sales on December 1st, an authorized campaign. So IQR shows what's unusual, not what's wrong.

> 🖱️ I'm pointing at the three Electronics rows from May, in the disc column.

> 🟢 And these are only 13 to 15%: normal discounts, flagged because most Electronics sales that month had none.

📘 **What each line does** (para vos, no se lee):

- `g = s.groupby(["category", "month"]).disc`: the discounts grouped by category and month.
- `q1, q3, n = g.transform("quantile", 0.25), g.transform("quantile", 0.75), g.transform("size")`: for every sale, the Q1, the Q3 and the size of **its own** group. `transform` returns one value per row.
- `s["iqr"] = (n >= 20) & (s.disc > q3 + 1.5 * (q3 - q1))`: True only if the group has 20 sales or more **and** the discount is above Q3 + 1.5 × IQR.
- `print((n < 20).sum(), (s.disc == 0).mean().round(2))`: the sales in groups under 20, and the share of sales with no discount.
- `s[s.iqr]`: the outliers.

**Resultado esperado (dónde mirar):**

- **Línea impresa:** `135 0.56`.
- **Tabla de 15 filas.** En la columna `promotion_id`:
  - `T01134`, `T01169` y `T01210` con **PRM-99** (Home & Kitchen, mes 7, 0,35);
  - `T02013`, `T02014` y `T02015` con **PRM-07** (Electronics, mes 12).
- **Electronics, mes 5:** `T00763`, `T00825` y `T00880`, con `disc` de 0,13 a 0,15.

---

### E. Step 4: validación de promociones

> 🖱️ I'm clicking plus Code at the top left, to add the fourth cell.

> 🟢 Step four: I'll check every promotion against the calendar, not only the outliers.

> ⌨️ I join the promotion sales with the calendar. Left keeps the IDs that don't exist.

```python
v = s[s.promotion_id.notna()].merge(p, how="left")
```

> ⌨️ First check: the ID exists. Second: the category matches the campaign.

```python
v["id_ok"] = v.max_discount.notna()
v["cat_ok"] = v.category == v.applicable_category
```

> ⌨️ Third: the date is inside the campaign. Fourth: the discount is within the approved maximum.

```python
v["date_ok"] = v.date.between(v.start_date, v.end_date)
v["max_ok"] = v.disc <= v.max_discount
```

> ⌨️ Fifth: within 5 points of the plan, separate from the maximum, because only the maximum is a hard limit.

```python
v["plan_ok"] = (v.disc - v.planned_discount).abs().round(4) <= 0.05
```

> ⌨️ I list the five checks, keep the sales that fail at least one, and show them.

```python
c = ["id_ok", "cat_ok", "date_ok", "max_ok", "plan_ok"]
bad = v[v[c].all(axis=1) == False]
bad[["promotion_id"] + c]
```

> 🖱️ I'm clicking Run on the left of the fourth cell.

> 🖱️ I'm pointing at the row count under the table: 17 rows.

> 🟢 17 of 188 promotion sales fail at least one check.

> 🖱️ I'm pointing at the first four rows, PRM-01, where only plan_ok is False.

> 🟢 PRM-01 plans 30%, and these got 37, 38, and 22%. They're inside the 40% maximum, so they're deviations to explain, not violations.

> 🖱️ I'm pointing at the three PRM-99 rows in the middle, where every check is False.

> 🟢 PRM-99 isn't in the calendar, so nothing can be validated: a clear violation.

> 🖱️ I'm moving the mouse over the other groups: PRM-02 with date_ok False, PRM-05 with max_ok False, and PRM-07 with cat_ok False.

> 🟢 PRM-02 used after its end date, PRM-05 above its 25% maximum, and the Electronics Black Friday code used in other categories.

📘 **What each line does** (para vos, no se lee):

- `v = s[s.promotion_id.notna()].merge(p, how="left")`: the 188 sales with a promotion ID, joined with the calendar on `promotion_id`. `left` keeps the IDs that don't exist.
- `v["id_ok"] = v.max_discount.notna()`: the ID exists (calendar data was found).
- `v["cat_ok"] = v.category == v.applicable_category`: the category matches the campaign's.
- `v["date_ok"] = v.date.between(v.start_date, v.end_date)`: the date is inside the campaign, both ends included.
- `v["max_ok"] = v.disc <= v.max_discount`: the discount is at or below the approved maximum.
- `v["plan_ok"] = (v.disc - v.planned_discount).abs().round(4) <= 0.05`: within 5 points of the planned discount. `round(4)` avoids decimal noise.
- `c = [...]`: the five check names.
- `bad = v[v[c].all(axis=1) == False]`: the sales where at least one check fails.
- `bad[["promotion_id"] + c]`: shows the promotion ID and the five checks.

**Resultado esperado (dónde mirar):**

- **Tabla de 17 filas**, en este orden:
  - **PRM-01 (4):** 0,37, 0,38, 0,37 y 0,22. Solo `plan_ok` False.
  - **PRM-02 (4):** `date_ok` False.
  - **PRM-05 (3):** 0,32 y 0,33. `max_ok` y `plan_ok` False.
  - **PRM-99 (3):** todo False.
  - **PRM-07 (3):** `cat_ok` False.

---

### F. Step 5: reglas de negocio independientes

> 🖱️ I'm clicking plus Code at the top left, to add the fifth cell.

> 🟢 Step five: two business rules that don't depend on the statistics.

> ⌨️ A promotion is valid if it exists, matches the category, and is inside its dates.

```python
ok = v[v.id_ok & v.cat_ok & v.date_ok].transaction_id
s["valid"] = s.transaction_id.isin(ok)
s["promo_issue"] = s.transaction_id.isin(bad.transaction_id)
```

> ⌨️ The two rules, on all 2,200 sales: more than 30% without a valid promotion, and a margin below the 15% floor.

```python
s["over30"] = (s.disc > 0.3) & (s.valid == False)
s["low"] = s.gap15 > 0
s[s.over30]
```

> 🖱️ I'm clicking Run on the left of the fifth cell.

> 🖱️ I'm pointing at the row count under the table: 10 rows.

> 🟢 Ten discounts above 30% without a valid promotion.

> 🖱️ I'm scrolling right to the disc and promotion_id columns.

> 🟢 Seven have no promotion at all, from 35 up to 55%. The other three are the PRM-99 sales.

> 🖱️ I'm scrolling right to the iqr column, and pointing at the three False values.

> 🟢 IQR missed three of them: T00123, 36% in Clothing in January, where the campaign raised the limit, and two Toys sales, 40 and 55%, in groups IQR doesn't screen. That's why this rule is independent.

📘 **What each line does** (para vos, no se lee):

- `ok = v[v.id_ok & v.cat_ok & v.date_ok].transaction_id`: the IDs of the sales with a valid promotion.
- `s["valid"] = s.transaction_id.isin(ok)`: True if the sale has a valid promotion.
- `s["promo_issue"] = s.transaction_id.isin(bad.transaction_id)`: True if the sale failed any calendar check.
- `s["over30"] = (s.disc > 0.3) & (s.valid == False)`: above 30% without a valid promotion.
- `s["low"] = s.gap15 > 0`: below the 15% margin (it has a gap to the floor).
- `s[s.over30]`: shows the over-30% sales.

**Resultado esperado (dónde mirar):**

- **Tabla de 10 filas.**
- **Columna `promotion_id`:** 7 sin promoción (NaN) y 3 con PRM-99.
- **Columna `iqr`:** False en `T00123` (Clothing, mes 1, 0,36), `T00649` (Toys, mes 4, 0,40) y `T01356` (Toys, mes 8, 0,55).

---

### G. Step 6: impacto en el margen

> 🖱️ I'm clicking plus Code at the top left, to add the sixth cell.

> 🟢 Step six: the impact on margin. I'll write one function so every table uses the same definitions.

> ⌨️ impact adds up net sales, profit, discount cost, and the gap to the floor, and counts the transactions.

```python
def impact(by):
    t = s.groupby(by)[["net", "profit", "cost", "gap15"]].sum()
    t["n"] = s.groupby(by).size()
```

> ⌨️ The margin is total profit over total sales, so big sales weigh more.

```python
    t["margin"] = t.profit / t.net
    return t.round(2)
```

> ⌨️ I'm pressing Delete to go back to the margin. Now the same table by category, with and without a valid promotion.

```python
cat = impact(["category", "valid"])
```

> ⌨️ Most promotions are Electronics, a thin-margin category, so I compute the no-promotion margin at the same category mix.

```python
w = cat.xs(True, level=1).net
print(round((cat.xs(False, level=1).margin * w).sum() / w.sum(), 3))
```

> ⌨️ And I show the tables: valid or not, by category, and by valid promotion.

```python
display(impact("valid"), cat)
pr = impact(s.promotion_id.where(s.valid))
pr
```

> 🖱️ I'm clicking Run on the left of the sixth cell.

> 🖱️ I'm pointing at the printed number at the top: 0.309.

> 🟢 Without promotions, but with the same category mix as the promotions, the margin would be 31%.

> 🖱️ I'm pointing at the margin column of the first table: 0.33 for False and 0.17 for True.

> 🟢 Promotional sales keep 17% against 33%. Against the 31% baseline, about 14 of the 16 points are the discount, and about 2 are the category mix.

> 🖱️ I'm scrolling down to the two Electronics rows of the category table.

> 🟢 Electronics drops from 24% to 10% with promotions, and it's almost all of the gap15 column.

> 🖱️ I'm scrolling down to the last table, and pointing at the PRM-07 row.

> 🟢 PRM-07: 9,228 dollars of discounts, a 3% margin, and 3,449 dollars below the floor. PRM-06, the other Electronics campaign, keeps 19%.

📘 **What each line does** (para vos, no se lee):

- `def impact(by):`: defines a reusable function that receives the grouping.
- `t = s.groupby(by)[["net", "profit", "cost", "gap15"]].sum()`: for each group, the net sales, gross profit, discount cost and gap to the floor.
- `t["n"] = s.groupby(by).size()`: the number of transactions of each group.
- `t["margin"] = t.profit / t.net`: the weighted margin, total profit ÷ total net sales.
- `return t.round(2)`: returns the table with 2 decimals.
- `cat = impact(["category", "valid"])`: the table by category, with and without a valid promotion.
- `w = cat.xs(True, level=1).net`: the promotional net sales of each category (the mix).
- `print(round((cat.xs(False, level=1).margin * w).sum() / w.sum(), 3))`: the margin without promotion, weighted with the promotions' mix.
- `display(impact("valid"), cat)`: shows valid vs not, and the category table.
- `pr = impact(s.promotion_id.where(s.valid))`: one row per valid promotion. Invalid IDs are left out.
- `pr`: shows it.

**Resultado esperado (dónde mirar):**

- **Número impreso:** `0.309`.
- **Primera tabla:** False: 2022 ventas, margin **0,33**. True: 178 ventas, margin **0,17**, gap15 3.468,17.
- **Tabla por categoría:** Electronics False 0,24 / True **0,10**.
- **Última tabla:** PRM-07: n 33, margin **0,03**, cost **9.227,69**, gap15 **3.448,92**. PRM-06: margin 0,19.

---

### H. Step 7: cuánto cuestan los descuentos inusuales

> 🖱️ I'm clicking plus Code at the top left, to add the seventh cell.

> 🟢 Step seven: what the unusual discounts actually cost, in dollars.

> ⌨️ plan is the planned discount of each sale's promotion.

```python
plan = s.promotion_id.map(p.set_index("promotion_id").planned_discount)
```

> ⌨️ excess is the discount above the planned rate, or above the group median. A zero reference would count normal discounts as losses.

```python
s["excess"] = (s.gross * (s.disc - plan.where(s.valid, g.transform("median")))).clip(lower=0)
```

> ⌨️ The unusual sales are IQR outliers, over 30%, or promotion issues. And I put the four key figures in one summary.

```python
u = s.iqr | s.over30 | s.promo_issue
money = pd.Series({"cost": s.cost.sum(), "unusual": s[u].excess.sum(), "gap15": s.gap15.sum(), "prm07": pr.gap15["PRM-07"]}).round(2)
money
```

> 🖱️ I'm clicking Run on the left of the seventh cell.

> 🖱️ I'm pointing at the first line, cost: 35,094.64.

> 🟢 Discounts gave away 35,095 dollars of margin, 6.7% of gross sales.

> 🖱️ I'm pointing at the second line, unusual: 1,072.70.

> 🟢 The 30 unusual sales cost only 1,073 dollars above normal.

> 🖱️ I'm pointing at the last two lines, gap15 and prm07.

> 🟢 Sales are 3,870 dollars below the 15% floor, and PRM-07 alone explains 3,449 of them, about 89%. So the priority is the PRM-07 rate; the violations are many but cheap, and need controls.

📘 **What each line does** (para vos, no se lee):

- `plan = s.promotion_id.map(p.set_index("promotion_id").planned_discount)`: the planned discount of each sale's promotion.
- `s["excess"] = (s.gross * (s.disc - plan.where(s.valid, g.transform("median")))).clip(lower=0)`: the discount dollars above a reference. The reference is the planned rate if the promotion is valid, and otherwise the median of its category and month. Negatives become 0.
- `u = s.iqr | s.over30 | s.promo_issue`: the unusual sales: an IQR outlier, over 30%, or a promotion issue (`|` means "or").
- `money = pd.Series({...}).round(2)`: the four figures: total discount cost, the excess of the unusual sales, the total gap to the floor and PRM-07's gap.
- `money`: shows it.

**Resultado esperado (dónde mirar):** cuatro líneas, de arriba hacia abajo: `cost` **35094.64**, `unusual` **1072.70**, `gap15` **3869.71** y `prm07` **3448.92**.

---

### I. Step 8: reconciliación

> 🖱️ I'm clicking plus Code at the top left, to add the eighth cell.

> 🟢 Step eight: I'll check that the categories add up to the total, so no sale was lost or counted twice.

> ⌨️ Recorded revenue, my revenue, and the difference, by category.

```python
k = ["net_revenue", "net", "diff"]
r = s.groupby("category")[k].sum()
```

> ⌨️ One row with the sum of the categories, and one with the total over all sales.

```python
r.loc["Sum"] = r.sum()
r.loc["Total"] = s[k].sum()
r.round(2)
```

> 🖱️ I'm clicking Run on the left of the eighth cell.

> 🖱️ I'm pointing at the Sum and Total rows at the bottom of the table.

> 🟢 Both rows are 489,707.18 recorded and 489,648.79 recalculated, so no sale was lost or counted twice.

> 🖱️ I'm moving the mouse down the diff column.

> 🟢 The total difference is 58.39 dollars: 58.35 from the six mismatches, plus a few cents of rounding, like the 0.04 in Electronics.

📘 **What each line does** (para vos, no se lee):

- `k = ["net_revenue", "net", "diff"]`: recorded revenue, recalculated revenue and the difference.
- `r = s.groupby("category")[k].sum()`: the totals of each category.
- `r.loc["Sum"] = r.sum()`: a row with the sum of the six categories.
- `r.loc["Total"] = s[k].sum()`: a row with the total over all sales.
- `r.round(2)`: shows the table. "Sum" and "Total" must be equal.

**Resultado esperado (dónde mirar):**

- **Filas `Sum` y `Total`, abajo:** iguales, con 489.707,18 · 489.648,79 · 58,39.
- **Columna `diff`:** Electronics 0,04 y Sports & Outdoors −0,02 (redondeo). El resto es entre 11 y 17 dólares.

---

### J. Step 9: modificar los archivos de entrada y exportar

> 🖱️ I'm clicking plus Code at the top left, to add the ninth cell.

> 🟢 Step nine: I'll update the input files and export the results.

> ⌨️ A data issue is a revenue mismatch or a percentage value. With it, I list the five review reasons.

```python
s["data_issue"] = (s["diff"].abs() > 0.01) | (s.discount_rate > 1)
f = ["iqr", "data_issue", "promo_issue", "over30", "low"]
```

> ⌨️ I export the sales with at least one reason, each reason as a column, so the team can filter.

```python
s[s[f].any(axis=1)].to_csv("flagged_transactions.csv", index=False)
```

> ⌨️ Now I rewrite the sales file: the corrected discount, with the original kept in discount_raw. net_revenue stays as recorded.

```python
s.assign(discount_raw=s.discount_rate, discount_rate=s.disc).drop(columns="disc").to_csv("sales_transactions.csv", index=False)
```

> ⌨️ And I rewrite the calendar, adding each valid promotion's results.

```python
p.merge(pr.reset_index(), how="left").to_csv("promotion_calendar.csv", index=False)
```

> ⌨️ Last, a summary file with the counts and the money figures.

```python
res = pd.concat([s[f].sum(), money])
res.to_csv("summary_results.csv")
res
```

> 🖱️ I'm clicking Run on the left of the ninth cell.

> 🖱️ I'm moving the mouse down the summary under the cell.

> 🟢 15 IQR outliers, 14 data issues, 17 promotion issues, 10 over 30%, and 72 below the margin floor, followed by the four money figures.

> 🖱️ I'm opening the Files panel on the left and pointing at sales_transactions and promotion_calendar.

> 🟢 The two input files keep their names, but now hold the corrected discount, the original value, the calculations, the flags, and each promotion's results.

> 🖱️ I'm pointing at flagged_transactions and summary_results, and closing the Files panel.

> 🟢 And the two new files: the sales to review, and the summary.

📘 **What each line does** (para vos, no se lee):

- `s["data_issue"] = (s["diff"].abs() > 0.01) | (s.discount_rate > 1)`: a revenue mismatch, or a discount stored as a percentage.
- `f = [...]`: the five review reasons.
- `s[s[f].any(axis=1)].to_csv("flagged_transactions.csv", index=False)`: exports the sales with at least one reason.
- `s.assign(discount_raw=s.discount_rate, discount_rate=s.disc).drop(columns="disc").to_csv("sales_transactions.csv", index=False)`: **rewrites the sales file**. `discount_rate` gets the corrected value, the original goes to `discount_raw`, and it adds the calculations and the flags.
- `p.merge(pr.reset_index(), how="left").to_csv("promotion_calendar.csv", index=False)`: **rewrites the calendar** with each valid promotion's results.
- `res = pd.concat([s[f].sum(), money])`: the counts by reason plus the money figures.
- `res.to_csv("summary_results.csv")`: exports the summary.
- `res`: shows it.

**Resultado esperado (dónde mirar):**

- **Resumen debajo de la celda:** iqr 15, data_issue 14, promo_issue 17, over30 10, low 72, cost 35094,64, unusual 1072,70, gap15 3869,71, prm07 3448,92.
- **Panel Files:** cuatro archivos: `flagged_transactions.csv`, `promotion_calendar.csv`, `sales_transactions.csv` y `summary_results.csv`. Si no aparecen, tocá el ícono de refresh arriba del panel y decí la frase.

---

### K. Conclusiones

> 🖱️ I'm clicking plus Text at the top left, to add the conclusions cell.

> ⌨️ I'm typing the summary, starting with dollars, because that's what sets the priority.

```markdown
## Summary
- Discounts cost $35,095; unusual ones only $1,073 above normal.
- PRM-07 explains $3,449 of the $3,870 below the 15% floor.
- Promotion margin: 17% vs 31% at the same category mix.
- Inputs fixed and updated. Files generated with AI.
```

> 🖱️ I'm clicking below the cell to show it formatted, and pressing Command + S to save the notebook.

---

### L. Epílogo (~1 min)

> 🖱️ I'm scrolling up slowly through the notebook.

> 🟢 My approach was evidence first, keeping every original value. The challenge was measuring impact fairly: counted, the violations looked like the problem, but in dollars it's PRM-07, an authorized campaign. I'd review its rate first. The limits are one year of synthetic data. Thanks for watching!

---

## Si algo sale mal

| Error | Qué decís y hacés |
| ----- | ----------------- |
| Un nombre mal escrito | 🖱️ *"There's a typo in this cell. I'm fixing the name and running it again."* |
| `s.diff` sin corchetes | 🖱️ *"diff is a pandas method, so I need brackets. I'm fixing it."* |
| Sangría del `def` | 🖱️ *"The indentation is wrong in the function. I'm fixing it and running again."* |
| `KeyError: 'PRM-07'` | 🖱️ *"Step six didn't run. I'm running it and then this cell."* |
| `NameError` | 🖱️ *"An earlier cell didn't run. I'm choosing Run before in the Runtime menu."* |
| Hay que repetir todo después del Step 9 | 🖱️ *"The inputs were already rewritten, so I'm uploading the originals from my Desktop again."* |

---

## Cronograma

**Método calibrado** (el mismo que dio 75–80 minutos para el guion viejo, y vos mediste 75): 120 caracteres por minuto de tipeo, 130 palabras por minuto de narración, **todo sumado**, y unos 25 segundos de navegación por celda.

| | Cantidad | Tiempo |
| - | -------- | ------ |
| Tipeo (código + conclusiones) | ~2.990 caracteres | ~25 min |
| Narración | ~2.040 palabras | ~15,5 min |
| Navegación | — | ~4 min |
| **Total** | | **~45 min** |

| Sección | Aprox. |
| ------- | ------ |
| A. Apertura | 0:00–1:00 |
| B. Step 1 | 1:00–3:30 |
| C. Step 2 | 3:30–9:00 |
| D. Step 3 | 9:00–14:00 |
| E. Step 4 | 14:00–19:30 |
| F. Step 5 | 19:30–23:00 |
| G. Step 6 | 23:00–30:00 |
| H. Step 7 | 30:00–34:30 |
| I. Step 8 | 34:30–36:30 |
| J. Step 9 | 36:30–42:00 |
| K. Conclusiones | 42:00–44:00 |
| L. Epílogo | 44:00–45:00 |

**Margen:** unos 6 minutos hasta 50:59. Si con práctica tipeás a 150 caracteres por minuto, baja a unos **40 minutos**. **Medilo:** hacé una práctica completa con cronómetro. Si pasa de 46 minutos, el primer recorte es la segunda frase 🖱️ + 🟢 de los resultados de los Steps 1, 3 y 6, que son los más largos.

---

## Checklist

**Antes de grabar**

- [ ] Practicá dos veces, con cronómetro. `discount_analysis.ipynb` tiene el código completo para comparar.
- [ ] Creá el notebook vacío **discount_analysis** en Colab.
- [ ] En **Files**, subí los dos CSV del Escritorio. Los del Escritorio son los originales: no los toques.
- [ ] **Tools → Settings → AI assistance**: ocultá las funciones de IA.
- [ ] **Tools → Settings → Editor**: si está la opción, desactivá las sugerencias automáticas de código (*Automatically trigger code completions*). Todo se tipea a mano: **no se usa autocompletado**.
- [ ] Zoom (`Cmd + +`). Firefox con la ventana 1 en la descripción de la tarea y la ventana 2 en Colab (segunda línea del Dock).
- [ ] Grabá enseguida después de subir los CSV.

**Durante**

- [ ] Ejecutá cada celda una vez, en orden. **No repitas el Step 1 después del Step 9.**
- [ ] Respetá la regla del mouse.
- [ ] No termines antes de las conclusiones, **Cmd + S** y el epílogo.

**Después**

- [ ] Detené TaskRecorder. Descargá el `.ipynb` y los 4 CSV de Colab.
- [ ] **Run full AutoQC**: What + Where tiene que pasar el 70%.
- [ ] Armá **Deliverables.zip** con el `.ipynb`, los 4 CSV y la carpeta `original/` con los dos CSV del Escritorio.
- [ ] Marcá en Studio la opción de archivos generados con IA.
- [ ] Subí por separado el **MP4**, el **ZIP de TaskRecorder**, **Deliverables.zip** y **Metadata.rtf**.
