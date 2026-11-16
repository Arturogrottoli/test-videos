# k3a13c10 — Analyze Discount Patterns in Sales Data Using Python and Pandas

Guion **corregido según el feedback del reviewer** para volver a grabar la tarea **k3a13c10** en **Google Colab** con **pandas**, en una sola toma, en **Firefox**.

**Qué corrige:**

| Problema del reviewer | Medido | Mínimo o máximo | Cómo lo corrige este guion |
| --------------------- | ------ | --------------- | -------------------------- |
| Tipeo | 42,91% | **≤ 35%** | La celda 1 ya está armada. Hablás **con las manos quietas** y después tipeás **en silencio**, en tramos de menos de 45 s. Más tiempo de inspección de resultados. |
| WHAT + WHERE | 52,6% | **≥ 70%** | Cada frase dice **qué** hacés, **dónde** (número de celda, línea, columna, botón) y **por qué**. Cada tramo de tipeo tiene su propia frase. |

**El análisis, el código y los resultados no cambian.** Solo cambia cómo se narra y en qué orden hablás y tipeás.

**Duración estimada: ~48 minutos** (máximo 50:59). Ver "Cronograma".

---

## Cómo leer este guion

- 🟢 = lo decís con el mouse quieto: **qué vas a hacer y por qué**, o **qué muestra un resultado y qué decidís**.
- 🗣️⌨️ = lo decís **con las manos fuera del teclado**, y **recién después** tipeás el bloque de abajo, **en silencio**. Cada bloque marca sus caracteres y el tiempo de tipeo.
- 🖱️ = lo decís **mientras hacés** la acción con el mouse: qué, dónde y por qué.
- 📘 = la explicación de cada línea, en inglés. Es para vos: **no se lee**.
- **Resultado esperado** = lo que tiene que aparecer. Es para vos.

**El ritmo de cada celda:**

1. 🖱️ **+ Code**, diciendo el número de la celda nueva.
2. 🟢 Qué vas a hacer y por qué.
3. 🗣️⌨️ Frase con las manos quietas → tipeás el bloque en silencio → 🗣️⌨️ frase → tipeás el bloque siguiente → …
4. 🖱️ **Run**, diciendo dónde aparece el resultado.
5. 🖱️ Señalás un lugar concreto → 🟢 dos o tres datos y qué decidís. Se repite por cada salida.

---

## Estrategia para bajar el tipeo a menos del 35%

**La cuenta:** el porcentaje de tipeo es el tiempo con el teclado activo dividido por la duración del video.

| | Antes | Ahora |
| - | ----- | ----- |
| Caracteres tipeados | ~2.990 | **2.851** (la celda 1 ya está armada) |
| Narración | mientras tipeabas | **antes de tipear, con las manos quietas** |
| Inspección de resultados | corta | **2 o 3 pares 🖱️ + 🟢 por salida** |

**Las cinco reglas:**

1. **Hablar y tipear nunca al mismo tiempo.** Al hablar mientras tipeás, tipeás más lento y todo ese tiempo cuenta como tipeo. Primero la frase 🗣️⌨️, después el bloque, rápido y en silencio.
2. **Ningún tramo de tipeo pasa de 45 segundos.** Cada bloque del guion tiene como máximo 93 caracteres (~32 s a 175 caracteres por minuto, ~37 s a 150). Las tres líneas más largas están partidas en dos, con una frase en el medio.
3. **La celda 1 no se tipea:** se explica señalando cada línea y se ejecuta.
4. **El tiempo ahorrado va a explicar:** decisiones (🟢 *why*) e inspección de resultados (🖱️ señalar + 🟢 datos).
5. **Nada de tipeo extra:** ni comentarios `#`, ni `print` de prueba, ni celdas que no estén en el guion.

**Lo que tenés que medir en la práctica:** el tipeo en silencio de todos los bloques tiene que entrar en **~16 minutos** (unos **175 caracteres por minuto**). Con eso, sobre ~48 minutos, el tipeo da **~34%**.

> ⚠️ Si en la práctica el tipeo total pasa de **17 minutos**, avisame **antes de grabar**. Con el código sin cambios, la única palanca que queda es la velocidad: habría que decidir entre acortar algo del código o tener más celdas preparadas.

---

## Pendientes antes de grabar

| Tema | Qué hacer |
| ---- | --------- |
| **Celda 1 armada** | Tiene que contener **solo** el `import` y los dos `read_csv` (ver el bloque del Step 1). Si además tiene `info()` y `describe()`, salteá la celda 2 del guion y restá 1 a cada número de celda que decís. |
| **Origen de los CSV** | Los generé yo, Claude, con un script de Python: "generated with AI" es cierto, "Gemini" no. Marcá en Studio la opción de archivos generados con IA. |
| **Versión de pandas** | Lo probé con pandas 3.1. Si `info()` dice `object` en vez de `str`, es lo mismo. |

---

## Qué cumple y dónde (análisis aprobado)

| Etapa aprobada | Dónde |
| -------------- | ----- |
| 1–2. Carga, columnas, tipos, fechas y faltantes | Celdas 1 y 2 |
| 3. Recalcular net revenue, descuento y gross margin | Celda 3 |
| 4. IQR por categoría y mes, mínimo 20 por grupo | Celda 4 |
| 5. Calendario: ID, categoría, fechas, máximo y tolerancia de 5 puntos | Celda 5 |
| 6. Más del 30% sin promoción autorizada | Celda 6 |
| 7. Margen bajo el 15%, incluso con promoción autorizada | Celdas 3 (`gap15`) y 6 (`low`) |
| 8. Con y sin promoción: volumen y gross profit | Celda 7 |
| 9. Anomalía estadística vs. calidad de datos vs. incumplimiento vs. decisión comercial | Celdas 4, 5, 7 y 10 |
| 10. Validar y conciliar por categoría | Celda 9 |
| 11. Exportar ventas marcadas y resumen (y reescribir las entradas) | Celda 10 |
| 12. Conclusiones y recomendaciones | Celda de texto 11 |

---

## La regla del mouse y del teclado

1. El mouse **solo se mueve con una frase 🖱️**. Mientras tipeás, soltalo.
2. Al terminar una acción, el cursor queda **quieto en el margen derecho**, lejos de los botones.
3. **Primero la frase, después el movimiento o el tipeo.** Leé el guion con las manos quietas.
4. **Repetí el número de celda al menos una vez por minuto.** Las frases ya lo hacen ("In cell five…", "Still in cell five…").
5. Si hacés algo fuera del guion, usá una frase comodín (todas con qué + dónde + por qué):
   - *"I'm scrolling right inside the table under cell N, to see the last columns."*
   - *"I'm clicking at the end of line N in cell N, to fix a typo."*
   - *"I'm pressing Escape to close the suggestion box, because I type everything by hand."* Si Colab muestra una caja de sugerencias, **no la aceptes**: con la caja abierta, Enter inserta la sugerencia.
   - *"I'm waiting for cell N to finish; the spinner on the left of the cell is still running."*

---

## Guion de grabación

### A. Apertura (0:00–2:00)

Con la **descripción de la tarea** en pantalla:

> 🟢 I will be beginning my task soon. The goal is to find discount patterns in one year of sales data, check them against the promotion calendar, and measure what they cost in gross margin dollars, not only in number of cases.

> 🟢 I have two input files: sales_transactions, one row per sale, and promotion_calendar, one row per campaign, with its dates, category, and planned and maximum discount.

> 🟢 The stages are: inspect and clean the data, recalculate revenue and margin, flag unusual discounts with IQR by category and month, validate every promotion against the calendar, apply the 30% and 15% business rules, compare promotional and regular sales, reconcile the totals, and finally rewrite the input files and export the results.

> 🟢 I expect to end with a list of flagged sales, each one with its reason, the dollar cost of each problem, and corrected input files.

> 🖱️ I'm clicking the yellow minimize button at the top left of this window, to put the task description away.

> 🖱️ I'm clicking the Firefox icon in the Dock, on the right of the screen, and choosing the second window in the list: my Colab notebook.

> 🖱️ I'm clicking the folder icon in Colab's left sidebar, to open the Files panel and check the inputs.

> 🖱️ I'm pointing at the two files in the panel: promotion_calendar and sales_transactions.

> 🟢 Both are already uploaded. They're synthetic, generated with AI, and the untouched originals stay on my Desktop, because at the end this notebook rewrites these copies.

> 🖱️ I'm clicking the same folder icon to close the Files panel, so the notebook gets the full width.

---

### B. Step 1: carga e inspección (2:00–6:00) · celdas 1 y 2

**Celda 1 (ya armada, no se tipea):**

```python
import pandas as pd
s = pd.read_csv("sales_transactions.csv", parse_dates=["date"])
p = pd.read_csv("promotion_calendar.csv", parse_dates=["start_date", "end_date"])
```

> 🟢 Step one: loading and inspection.

> 🖱️ I'm pointing at cell one, at the top of the notebook. I prepared this cell before recording: it only has the import and the two read_csv calls. That saves typing time, and I'll use it to explain the analysis. I'm not changing it.

> 🖱️ I'm pointing at line two of cell one: it reads the sales into s. parse_dates turns the date column into real dates, because I'll compare each sale with the campaign windows.

> 🖱️ I'm pointing at line three: it reads the calendar into p, with start_date and end_date as dates too, for the same reason.

> 🖱️ I'm clicking the Run button on the left of cell one. It prints nothing; it only loads the two tables.

> 🖱️ I'm clicking plus Code at the top left of the notebook, to add cell two, below cell one.

> 🗣️⌨️ In cell two, I'll type info for both tables, to see size, types, and missing values, and describe for the sales, to see the ranges before any calculation.

```python
s.info()
p.info()
s.describe()
```
*(30 caracteres · ~10 s)*

> 🖱️ I'm clicking the Run button on the left of cell two. The output appears right below the cell.

> 🖱️ I'm pointing at the top of the first info output, under cell two: RangeIndex, 2,200 entries, and 10 columns.

> 🟢 2,200 sales, one row per transaction. And the date column says datetime, so the parsing in cell one worked.

> 🖱️ I'm moving the mouse down the Non-Null Count column of the same output, to the promotion_id row.

> 🟢 Every column has 2,200 values except promotion_id, with 188. An empty ID means the sale had no promotion, so it's information, not a gap: I keep it empty instead of filling it.

> 🖱️ I'm pointing at the second info output, the calendar.

> 🟢 8 campaigns, 7 columns, and no missing values, so every promotion has its dates and limits.

> 🖱️ I'm scrolling down to the describe table at the bottom of cell two, and pointing at the discount_rate column, rows 75% and max.

> 🟢 The 75th percentile is 0.10, but the maximum is 26. As a fraction that would be a 2,600% discount, so some values look like they were stored as percentages. I won't convert them blindly: I'll test that against the recorded revenue in the next cell.

> 🖱️ I'm moving the mouse to the gross_margin column, in the min row of the same table.

> 🟢 The minimum gross margin is minus 62 dollars, so some sales lost money. The 15% floor rule will catch them.

📘 **What each line does** (para vos, no se lee):

- `import pandas as pd`: loads pandas with the short name `pd`.
- `s = pd.read_csv("sales_transactions.csv", parse_dates=["date"])`: reads the sales into `s`. `parse_dates` turns `date` into a real date.
- `p = pd.read_csv("promotion_calendar.csv", parse_dates=["start_date", "end_date"])`: reads the calendar into `p`, with both dates as real dates.
- `s.info()`: the rows, columns, non-null count (so, missing values) and type of each sales column.
- `p.info()`: the same for the calendar.
- `s.describe()`: count, mean, min, quartiles and max of the numeric and date columns.

**Resultado esperado (dónde mirar):**

- **Celda 1:** no muestra nada.
- **Primer `info()` de la celda 2:** `RangeIndex: 2200 entries`, `10 columns`. En **Non-Null Count**, todo dice 2200 salvo `promotion_id` (188 non-null). `date` es `datetime64`.
- **Segundo `info()`:** `8 entries`, 7 columnas, todo con 8 non-null.
- **`describe()`:** en `discount_rate`, la fila `75%` dice 0,10 y la fila `max` dice **26,0**. En `gross_margin`, `min` = **−62,45**.

---

### C. Step 2: recalcular el dinero (6:00–11:00) · celda 3

> 🖱️ I'm clicking plus Code at the top left, to add cell three, below the inspection.

> 🟢 Step two: fix the discount units and recalculate revenue and margin myself, in new columns, so the original values stay untouched.

> 🗣️⌨️ On the first line of cell three, I'll create disc, the discount as a fraction: values up to 1 stay, larger ones are divided by 100.

```python
s["disc"] = s.discount_rate.where(s.discount_rate <= 1, s.discount_rate / 100)
```
*(78 caracteres · ~27 s)*

> 🗣️⌨️ Below it, in the same cell, the month, for the IQR groups, and gross sales, quantity times unit price.

```python
s["month"] = s.date.dt.month
s["gross"] = s.quantity * s.unit_price
```
*(67 caracteres · ~23 s)*

> 🗣️⌨️ Next, still in cell three: net revenue after the discount, and gross profit after the unit cost.

```python
s["net"] = s.gross * (1 - s.disc)
s["profit"] = s.net - s.quantity * s.unit_cost
```
*(80 caracteres · ~27 s)*

> 🗣️⌨️ Now diff, the recorded revenue minus mine, to test the conversion. And cost, the margin dollars each discount gives away.

```python
s["diff"] = s.net_revenue - s.net
s["cost"] = s.gross * s.disc
```
*(62 caracteres · ~21 s)*

> 🗣️⌨️ Last two lines of cell three: gap15, the profit dollars missing to reach a 15% margin, with negatives set to zero. And the sales where my revenue differs by more than one cent.

```python
s["gap15"] = (0.15 * s.net - s.profit).clip(lower=0)
s[s["diff"].abs() > 0.01]
```
*(78 caracteres · ~27 s)*

> 🖱️ I'm clicking the Run button on the left of cell three. The mismatches appear as a table below it.

> 🖱️ I'm pointing at the row count under the table in cell three: six rows.

> 🟢 Only six of 2,200 sales don't reconcile. That also proves the conversion: the eight values I divided by 100 now match the recorded revenue, so they really were percentages. That's the evidence I wanted before changing units.

> 🖱️ I'm pointing at the first row, T00722, and moving between the gross, net_revenue, and net columns.

> 🟢 Recorded 90.42, mine 84.99. And 90.42 is exactly the gross column, so the 6% discount was never subtracted.

> 🖱️ I'm moving the mouse down the disc column of the six rows.

> 🟢 Discounts from 5 to 14%, all ignored by the recorded revenue. I can't prove whether the revenue or the discount is wrong, so I don't overwrite them: they'll be flagged as a data quality issue.

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

- **Tabla de 6 filas** debajo de la celda 3: `T00722`, `T01588`, `T01684`, `T01737`, `T01929`, `T02155`.
- **Primera fila:** `gross` 90,42 = `net_revenue` 90,42; `net` 84,99; `diff` 5,43; `disc` 0,06.
- **Columna `disc`:** valores entre 0,05 y 0,14.

---

### D. Step 3: descuentos inusuales con IQR (11:00–16:00) · celda 4

> 🖱️ I'm clicking plus Code at the top left, to add cell four, below the money columns.

> 🟢 Step three: unusual discounts. I compare each sale with its own category and month, because a 20% discount is normal in a December campaign and unusual in a quiet month.

> 🗣️⌨️ On the first line of cell four, I'll group the discounts by category and month.

```python
g = s.groupby(["category", "month"]).disc
```
*(41 caracteres · ~14 s)*

> 🗣️⌨️ On the next line of cell four, transform gives every sale the first quartile, the third quartile, and the size of its own group.

```python
q1, q3, n = g.transform("quantile", 0.25), g.transform("quantile", 0.75), g.transform("size")
```
*(93 caracteres · ~32 s)*

> 🗣️⌨️ Now the rule, on line three: an outlier is above Q3 plus 1.5 times the IQR, and only in groups of 20 sales or more, because quartiles of tiny groups aren't reliable.

```python
s["iqr"] = (n >= 20) & (s.disc > q3 + 1.5 * (q3 - q1))
```
*(54 caracteres · ~19 s)*

> 🗣️⌨️ Last two lines of cell four: I print how many sales fall in small groups and the share of sales with no discount, to check the method's blind spots. Then I show the outliers.

```python
print((n < 20).sum(), (s.disc == 0).mean().round(2))
s[s.iqr]
```
*(61 caracteres · ~21 s)*

> 🖱️ I'm clicking the Run button on the left of cell four. The printed line and the table appear below it.

> 🖱️ I'm pointing at the printed line at the top of the output under cell four: 135 and 0.56.

> 🟢 135 sales are in groups with fewer than 20 sales, all of them Toys months, so IQR doesn't screen them; the business rules in cell six will. 

> 🟢 And 56% of all sales have no discount, so Q1 is zero and the limit becomes about 2.5 times Q3. I tested using only discounted sales, but that leaves just 8 groups with 20 or more, so I keep this version and treat IQR as a screen.

> 🖱️ I'm pointing at the row count under the table: 15 rows.

> 🖱️ I'm scrolling right inside the table, to the promotion_id column, and pointing at the PRM-99 rows and then the PRM-07 rows from December.

> 🟢 Three are PRM-99, an ID I'll validate in the next cell. Three are Black Friday sales from an authorized campaign. So IQR finds what's statistically unusual, not what's wrong: that's a statistical anomaly, not yet a violation.

> 🖱️ I'm pointing at the three Electronics rows from May, in the disc column.

> 🟢 These are only 13 to 15%: normal discounts, flagged because most Electronics sales that month had none. Another reason not to treat IQR as a verdict.

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

### E. Step 4: validación de promociones (16:00–22:00) · celda 5

> 🖱️ I'm clicking plus Code at the top left, to add cell five.

> 🟢 Step four: I check every promotional sale against the calendar, not only the outliers, because a violation doesn't have to be statistically unusual.

> 🗣️⌨️ On the first line of cell five, I'll join the promotional sales with the calendar. A left join keeps the IDs that don't exist in the calendar, instead of dropping them.

```python
v = s[s.promotion_id.notna()].merge(p, how="left")
```
*(50 caracteres · ~17 s)*

> 🗣️⌨️ Below the merge, the first two checks: the ID exists in the calendar, and the category matches the campaign.

```python
v["id_ok"] = v.max_discount.notna()
v["cat_ok"] = v.category == v.applicable_category
```
*(85 caracteres · ~29 s)*

> 🗣️⌨️ Still in cell five, checks three and four: the date is inside the campaign window, and the discount is within the approved maximum.

```python
v["date_ok"] = v.date.between(v.start_date, v.end_date)
v["max_ok"] = v.disc <= v.max_discount
```
*(94 caracteres · ~32 s)*

> 🗣️⌨️ Check five, on the next line: within 5 points of the planned discount. I keep it separate from the maximum, because the maximum is a hard limit and the plan is a target.

```python
v["plan_ok"] = (v.disc - v.planned_discount).abs().round(4) <= 0.05
```
*(67 caracteres · ~23 s)*

> 🗣️⌨️ Now, in cell five, a list with the five check names, so I can use them together.

```python
c = ["id_ok", "cat_ok", "date_ok", "max_ok", "plan_ok"]
```
*(55 caracteres · ~19 s)*

> 🗣️⌨️ Last two lines of cell five: the sales that fail at least one check, and a table with the promotion and the five checks, so each row shows its reason.

```python
bad = v[v[c].all(axis=1) == False]
bad[["promotion_id"] + c]
```
*(60 caracteres · ~21 s)*

> 🖱️ I'm clicking the Run button on the left of cell five. The failing sales appear in a table below it.

> 🖱️ I'm pointing at the row count under the table in cell five: 17 rows.

> 🟢 17 of 188 promotional sales fail at least one check.

> 🖱️ I'm pointing at the first four rows, PRM-01, where only plan_ok is False.

> 🟢 PRM-01 plans 30%, and these got 37, 38, and 22%. They're inside the 40% maximum, so they're deviations to explain, not violations.

> 🖱️ I'm pointing at the three PRM-99 rows in the middle of the table, where every check is False.

> 🟢 PRM-99 isn't in the calendar, so nothing can be validated: a clear violation.

> 🖱️ I'm moving the mouse over the other groups in the same table: PRM-02 with date_ok False, PRM-05 with max_ok False, and PRM-07 with cat_ok False.

> 🟢 PRM-02 used after its end date, PRM-05 above its 25% maximum, and the Electronics Black Friday code used in other categories. Each failure has a different business owner, which is why I keep the five checks separate.

📘 **What each line does** (para vos, no se lee):

- `v = s[s.promotion_id.notna()].merge(p, how="left")`: the 188 sales with a promotion ID, joined with the calendar on `promotion_id`. `left` keeps the IDs that don't exist.
- `v["id_ok"] = v.max_discount.notna()`: the ID exists (calendar data was found).
- `v["cat_ok"] = v.category == v.applicable_category`: the category matches the campaign's.
- `v["date_ok"] = v.date.between(v.start_date, v.end_date)`: the date is inside the campaign, both ends included.
- `v["max_ok"] = v.disc <= v.max_discount`: the discount is at or below the approved maximum.
- `v["plan_ok"] = (v.disc - v.planned_discount).abs().round(4) <= 0.05`: within 5 points of the planned discount. `round(4)` avoids decimal noise.
- `c = ["id_ok", "cat_ok", "date_ok", "max_ok", "plan_ok"]`: the five check names.
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

### F. Step 5: reglas del 30% y del 15% (22:00–26:00) · celda 6

> 🖱️ I'm clicking plus Code at the top left, to add cell six.

> 🟢 Step five: two business rules that don't depend on the statistics, applied to all 2,200 sales.

> 🗣️⌨️ On the first line of cell six, I'll keep the IDs of the sales with a valid promotion: it exists, matches the category, and is inside its dates.

```python
ok = v[v.id_ok & v.cat_ok & v.date_ok].transaction_id
```
*(53 caracteres · ~18 s)*

> 🗣️⌨️ Next line of cell six: valid marks those sales in the full table.

```python
s["valid"] = s.transaction_id.isin(ok)
```
*(38 caracteres · ~13 s)*

> 🗣️⌨️ Still in cell six: promo_issue marks every sale that failed any of the five checks.

```python
s["promo_issue"] = s.transaction_id.isin(bad.transaction_id)
```
*(60 caracteres · ~21 s)*

> 🗣️⌨️ Last three lines of cell six: over30, more than 30% without a valid promotion. low, any sale below the 15% floor, even inside an authorized campaign. And I show the over-30% sales.

```python
s["over30"] = (s.disc > 0.3) & (s.valid == False)
s["low"] = s.gap15 > 0
s[s.over30]
```
*(84 caracteres · ~29 s)*

> 🖱️ I'm clicking the Run button on the left of cell six. The over-30% table appears below it.

> 🖱️ I'm pointing at the row count under the table in cell six: 10 rows.

> 🟢 Ten discounts above 30% without a valid promotion.

> 🖱️ I'm scrolling right inside the table, to the disc and promotion_id columns.

> 🟢 Seven have no promotion at all, from 35 up to 55%. The other three are the PRM-99 sales. These are policy violations.

> 🖱️ I'm scrolling right to the iqr column of the same table, and pointing at the three False values.

> 🟢 IQR missed three of them: T00123, 36% in Clothing in January, where the campaign raised the group's limit, and two Toys sales, 40 and 55%, in the small groups IQR doesn't screen. That's why this rule is independent from the statistics.

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

### G. Step 6: con y sin promoción, impacto en el margen (26:00–33:00) · celda 7

> 🖱️ I'm clicking plus Code at the top left, to add cell seven.

> 🟢 Step six: promotional versus regular sales, in volume and gross profit. I'll write one small function, so every table uses exactly the same definitions.

> 🗣️⌨️ At the top of cell seven, I'll define impact: for any grouping, it adds up net sales, profit, discount cost, and the gap to the floor.

```python
def impact(by):
    t = s.groupby(by)[["net", "profit", "cost", "gap15"]].sum()
```
*(79 caracteres · ~27 s)*

> 🗣️⌨️ Inside the same function, still in cell seven: the number of sales, for volume, and the margin as total profit over total net sales, so big sales weigh more.

```python
    t["n"] = s.groupby(by).size()
    t["margin"] = t.profit / t.net
    return t.round(2)
```
*(90 caracteres · ~31 s)*

> 🗣️⌨️ I'll press Delete to go back to the left margin, outside the function. Then the same table by category, with and without a valid promotion.

```python
cat = impact(["category", "valid"])
```
*(35 caracteres · ~12 s)*

> 🗣️⌨️ Most promotions are Electronics, a thin-margin category. So, on the next line of cell seven, I take the promotional sales of each category as weights.

```python
w = cat.xs(True, level=1).net
```
*(29 caracteres · ~10 s)*

> 🗣️⌨️ And I print the regular margin with that same category mix, so the comparison isn't biased by mix.

```python
print(round((cat.xs(False, level=1).margin * w).sum() / w.sum(), 3))
```
*(68 caracteres · ~23 s)*

> 🗣️⌨️ Last lines of cell seven: I show the valid-or-not table and the category table, and build one row per valid promotion.

```python
display(impact("valid"), cat)
pr = impact(s.promotion_id.where(s.valid))
pr
```
*(75 caracteres · ~26 s)*

> 🖱️ I'm clicking the Run button on the left of cell seven. A number and three tables appear below it.

> 🖱️ I'm pointing at the printed number at the top of the output under cell seven: 0.309.

> 🟢 Without promotions, but with the same category mix as the promotions, the margin would be 31%.

> 🖱️ I'm pointing at the first table, the n and margin columns: False 2,022 sales at 0.33, True 178 sales at 0.17.

> 🟢 Promotional sales are only 178 of 2,200, and keep 17% margin against 33%. Against the 31% baseline, about 14 of the 16 points are the discount itself, and about 2 are the category mix.

> 🖱️ I'm scrolling down to the category table, still under cell seven, and pointing at the two Electronics rows.

> 🟢 Electronics drops from 24% to 10% with promotions, and it carries almost all of the gap15 column.

> 🖱️ I'm scrolling down to the last table, one row per valid promotion, and pointing at the PRM-07 row.

> 🟢 PRM-07: 33 sales, 9,228 dollars of discounts, a 3% margin, and 3,449 dollars below the floor. PRM-06, the other Electronics campaign, keeps 19%. So PRM-07 is an authorized campaign with a pricing problem: a business decision to review, not a data error.

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

### H. Step 7: cuánto cuestan los descuentos inusuales (33:00–37:30) · celda 8

> 🖱️ I'm clicking plus Code at the top left, to add cell eight.

> 🟢 Step seven: what the unusual discounts actually cost, in dollars, because counting cases doesn't tell me where the money goes.

> 🗣️⌨️ On the first line of cell eight, plan is the planned discount of each sale's promotion, looked up in the calendar.

```python
plan = s.promotion_id.map(p.set_index("promotion_id").planned_discount)
```
*(71 caracteres · ~24 s)*

> 🗣️⌨️ Next, excess: the discount dollars above a fair reference. The reference is the planned rate when the promotion is valid, and the median of the category and month otherwise. A zero reference would count normal discounts as losses.

```python
s["excess"] = (s.gross * (s.disc - plan.where(s.valid, g.transform("median")))).clip(lower=0)
```
*(93 caracteres · ~32 s)*

> 🗣️⌨️ Still in cell eight: u marks the unusual sales, an IQR outlier, over 30%, or a promotion issue.

```python
u = s.iqr | s.over30 | s.promo_issue
```
*(36 caracteres · ~12 s)*

> 🗣️⌨️ Now a summary with names, so each figure is labeled. First half: the total discount cost and the excess of the unusual sales.

```python
money = pd.Series({"cost": s.cost.sum(), "unusual": s[u].excess.sum(), 
```
*(71 caracteres · ~24 s)*

> 🗣️⌨️ Same line, second half: the total gap to the 15% floor, and PRM-07's share of it from the promotion table. Then I show it.

```python
"gap15": s.gap15.sum(), "prm07": pr.gap15["PRM-07"]}).round(2)
money
```
*(68 caracteres · ~23 s)*

> 🖱️ I'm clicking the Run button on the left of cell eight. Four labeled numbers appear below it.

> 🖱️ I'm pointing at the first line of the output under cell eight, cost: 35,094.64.

> 🟢 Discounts gave away 35,095 dollars of margin, about 6.7% of gross sales.

> 🖱️ I'm pointing at the second line, unusual: 1,072.70.

> 🟢 The 30 unusual sales cost only 1,073 dollars above their reference. Many cases, little money.

> 🖱️ I'm pointing at the last two lines, gap15 and prm07.

> 🟢 Sales are 3,870 dollars below the 15% floor, and PRM-07 alone explains 3,449 of them, about 89%. So the priority is the PRM-07 rate; the violations are many but cheap, and they need controls rather than repricing.

📘 **What each line does** (para vos, no se lee):

- `plan = s.promotion_id.map(p.set_index("promotion_id").planned_discount)`: the planned discount of each sale's promotion.
- `s["excess"] = (s.gross * (s.disc - plan.where(s.valid, g.transform("median")))).clip(lower=0)`: the discount dollars above a reference. The reference is the planned rate if the promotion is valid, and otherwise the median of its category and month. Negatives become 0.
- `u = s.iqr | s.over30 | s.promo_issue`: the unusual sales: an IQR outlier, over 30%, or a promotion issue (`|` means "or").
- `money = pd.Series({...}).round(2)`: the four figures: total discount cost, the excess of the unusual sales, the total gap to the floor and PRM-07's gap. Se tipea en una sola línea, en dos tramos (no apretes Enter en el medio).
- `money`: shows it.

**Resultado esperado (dónde mirar):** cuatro líneas, de arriba hacia abajo: `cost` **35094.64**, `unusual` **1072.70**, `gap15` **3869.71** y `prm07` **3448.92**.

---

### I. Step 8: conciliación por categoría (37:30–40:00) · celda 9

> 🖱️ I'm clicking plus Code at the top left, to add cell nine.

> 🟢 Step eight: I validate that the categories add up to the total, so no sale was lost or counted twice in the groupings.

> 🗣️⌨️ At the top of cell nine: recorded revenue, my revenue, and the difference, summed by category.

```python
k = ["net_revenue", "net", "diff"]
r = s.groupby("category")[k].sum()
```
*(69 caracteres · ~24 s)*

> 🗣️⌨️ Below that, one row with the sum of the categories, and one with the total over all sales. They must be equal.

```python
r.loc["Sum"] = r.sum()
r.loc["Total"] = s[k].sum()
r.round(2)
```
*(61 caracteres · ~21 s)*

> 🖱️ I'm clicking the Run button on the left of cell nine. The reconciliation table appears below it.

> 🖱️ I'm pointing at the Sum and Total rows at the bottom of the table under cell nine.

> 🟢 Both rows are 489,707.18 recorded and 489,648.79 recalculated, so the groupings are complete.

> 🖱️ I'm moving the mouse down the diff column of the same table.

> 🟢 The total difference is 58.39 dollars: 58.35 from the six mismatches, plus a few cents of rounding, like the 0.04 in Electronics. Nothing else is unexplained.

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

### J. Step 9: reescribir las entradas y exportar (40:00–45:00) · celda 10

> 🖱️ I'm clicking plus Code at the top left, to add cell ten, the last code cell.

> 🟢 Step nine: I update the two input files with the corrections, and export the flagged sales and a summary.

> 🗣️⌨️ On the first line of cell ten: data_issue, a revenue mismatch or a discount stored as a percentage. Those are data quality problems, not business ones.

```python
s["data_issue"] = (s["diff"].abs() > 0.01) | (s.discount_rate > 1)
```
*(66 caracteres · ~23 s)*

> 🗣️⌨️ Next line of cell ten: the five review reasons, kept separate so each team filters its own.

```python
f = ["iqr", "data_issue", "promo_issue", "over30", "low"]
```
*(57 caracteres · ~20 s)*

> 🗣️⌨️ Still in cell ten: I export every sale with at least one reason to flagged_transactions.

```python
s[s[f].any(axis=1)].to_csv("flagged_transactions.csv", index=False)
```
*(67 caracteres · ~23 s)*

> 🗣️⌨️ Now I rewrite the sales input file. First half of the line: discount_rate gets the corrected fraction, and the original value moves to discount_raw, so nothing is lost.

```python
s.assign(discount_raw=s.discount_rate, discount_rate=s.disc)
```
*(60 caracteres · ~21 s)*

> 🗣️⌨️ Same line, second half: I drop the helper column and save over sales_transactions. net_revenue stays as recorded, because I had no evidence to change it.

```python
.drop(columns="disc").to_csv("sales_transactions.csv", index=False)
```
*(67 caracteres · ~23 s)*

> 🗣️⌨️ Next line of cell ten: I rewrite the calendar, adding each valid promotion's sales, profit, and margin.

```python
p.merge(pr.reset_index(), how="left").to_csv("promotion_calendar.csv", index=False)
```
*(83 caracteres · ~28 s)*

> 🗣️⌨️ Last three lines of cell ten: the counts by reason plus the money figures, saved as summary_results, and shown.

```python
res = pd.concat([s[f].sum(), money])
res.to_csv("summary_results.csv")
res
```
*(74 caracteres · ~25 s)*

> 🖱️ I'm clicking the Run button on the left of cell ten. The summary appears below it.

> 🖱️ I'm moving the mouse down the first five lines of the output under cell ten.

> 🟢 15 IQR outliers are statistical anomalies. 14 data issues are quality problems. 17 promotion issues and 10 over 30% are policy violations. And 72 sales below the floor, 35 of them in valid promotions like PRM-07: legitimate campaigns that still need a pricing decision.

> 🖱️ I'm pointing at the last four lines, the money figures, under the counts.

> 🟢 The same four dollar figures from cell eight, now saved next to the counts, so the summary file stands on its own.

> 🖱️ I'm clicking the folder icon in the left sidebar, to open the Files panel and check the outputs.

> 🖱️ I'm pointing at sales_transactions and promotion_calendar in the panel.

> 🟢 The two input files keep their names, but now hold the corrected discount, the original value, the calculations, the flags, and each promotion's results.

> 🖱️ I'm pointing at flagged_transactions and summary_results, the two new files.

> 🟢 104 sales to review, each with its reasons as columns, and the summary.

> 🖱️ I'm clicking the folder icon again to close the Files panel.

📘 **What each line does** (para vos, no se lee):

- `s["data_issue"] = (s["diff"].abs() > 0.01) | (s.discount_rate > 1)`: a revenue mismatch, or a discount stored as a percentage.
- `f = ["iqr", "data_issue", "promo_issue", "over30", "low"]`: the five review reasons.
- `s[s[f].any(axis=1)].to_csv("flagged_transactions.csv", index=False)`: exports the sales with at least one reason.
- `s.assign(discount_raw=s.discount_rate, discount_rate=s.disc).drop(columns="disc").to_csv("sales_transactions.csv", index=False)`: **rewrites the sales file**. `discount_rate` gets the corrected value, the original goes to `discount_raw`, and it adds the calculations and the flags. Se tipea en una sola línea, en dos tramos (no apretes Enter en el medio).
- `p.merge(pr.reset_index(), how="left").to_csv("promotion_calendar.csv", index=False)`: **rewrites the calendar** with each valid promotion's results.
- `res = pd.concat([s[f].sum(), money])`: the counts by reason plus the money figures.
- `res.to_csv("summary_results.csv")`: exports the summary.
- `res`: shows it.

**Resultado esperado (dónde mirar):**

- **Resumen debajo de la celda 10:** iqr 15, data_issue 14, promo_issue 17, over30 10, low 72, cost 35094,64, unusual 1072,70, gap15 3869,71, prm07 3448,92.
- **Panel Files:** cuatro archivos: `flagged_transactions.csv` (104 filas), `promotion_calendar.csv`, `sales_transactions.csv` y `summary_results.csv`. Si no aparecen, tocá el ícono de refresh arriba del panel y decí: *"I'm clicking refresh at the top of the Files panel, to show the new files."*

---

### K. Conclusiones (45:00–46:30) · celda de texto 11

> 🖱️ I'm clicking plus Text at the top left, to add a text cell at the end of the notebook, for the conclusions.

> 🗣️⌨️ In the text cell, I'll start with the title and the first finding, in dollars, because dollars set the priority.

```markdown
## Summary
- Discounts cost $35,095; unusual ones only $1,073 above normal.
```
*(75 caracteres · ~26 s)*

> 🗣️⌨️ Second line of the text cell: the main recommendation, PRM-07.

```markdown
- PRM-07 explains $3,449 of the $3,870 below the 15% floor.
```
*(59 caracteres · ~20 s)*

> 🗣️⌨️ Third line: the fair margin comparison, at the same category mix.

```markdown
- Promotion margin: 17% vs 31% at the same category mix.
```
*(56 caracteres · ~19 s)*

> 🗣️⌨️ Last line: the files I changed, and the AI declaration.

```markdown
- Inputs fixed and updated. Files generated with AI.
```
*(52 caracteres · ~18 s)*

> 🖱️ I'm clicking on the empty area below the text cell, to show it formatted.

> 🖱️ I'm pressing Command and S to save the notebook; the save message appears at the bottom left.

---

### L. Epílogo (46:30–48:30)

Sin tipear nada. Recién **después** del epílogo abrís TaskRecorder para detener la grabación.

> 🖱️ I'm scrolling up slowly through the notebook, from the conclusions back to cell one.

> 🟢 The most important decisions were about fairness. I converted the discount units only after the recorded revenue confirmed them, and I kept the six unexplained mismatches visible instead of forcing them. I ran IQR within each category and month, with a minimum of 20 sales, because one global threshold would mix December campaigns with quiet months. And I measured the impact in dollars against fair references: the planned rate, the group median, and a baseline with the same category mix.

> 🟢 To verify quality, I made each check visible instead of trusting one flag: five separate calendar checks, two business rules independent from the statistics, and a reconciliation where every category adds up to the total. Every changed value keeps its original next to it, so the corrections can be audited.

> 🟢 The main limitations: it's one year of synthetic data, with no customer or competitor information, so I can't tell whether PRM-07 brought new customers that justify its margin. The median reference is an assumption, and 135 Toys sales sit in groups too small for IQR, so they rely only on the business rules. With more data, I'd test a lower PRM-07 rate, and I'd move the calendar checks to checkout, so invalid codes are blocked before the sale. Thanks for watching!

---

## Si algo sale mal

| Error | Qué decís y hacés |
| ----- | ----------------- |
| Un nombre mal escrito | 🖱️ *"There's a typo in cell N. I'm clicking on that line to fix the name, and running the cell again."* |
| `s.diff` sin corchetes | 🖱️ *"diff is a pandas method, so in cell N I need brackets. I'm fixing it and running again."* |
| Sangría del `def` | 🖱️ *"The indentation is wrong in the function in cell seven. I'm fixing it and running again."* |
| `KeyError: 'PRM-07'` | 🖱️ *"Cell seven didn't run. I'm clicking its Run button, then this cell's."* |
| `NameError` | 🖱️ *"An earlier cell didn't run. I'm opening the Runtime menu at the top and choosing Run before."* |
| Hay que repetir todo después de la celda 10 | 🖱️ *"The inputs were already rewritten, so I'm uploading the originals from my Desktop again in the Files panel."* |

---

## Cronograma

**Método:** narración a 130 palabras por minuto, **sumada** al tipeo (no se superponen: primero hablás, después tipeás), y unos 25 segundos de navegación por celda.

| | Cantidad | Tiempo |
| - | -------- | ------ |
| Tipeo (código + conclusiones) | 2.851 caracteres | **~16,3 min** a 175 car./min (~19 min a 150) |
| Narración | ~3.460 palabras | ~26,5 min |
| Navegación (11 celdas + Files) | — | ~5 min |
| **Total** | | **~48 min** (~50,5 min a 150 car./min) |

| Sección | Aprox. |
| ------- | ------ |
| A. Apertura | 0:00–2:00 |
| B. Step 1 (celdas 1 y 2) | 2:00–6:00 |
| C. Step 2 (celda 3) | 6:00–11:00 |
| D. Step 3 (celda 4) | 11:00–16:00 |
| E. Step 4 (celda 5) | 16:00–22:00 |
| F. Step 5 (celda 6) | 22:00–26:00 |
| G. Step 6 (celda 7) | 26:00–33:00 |
| H. Step 7 (celda 8) | 33:00–37:30 |
| I. Step 8 (celda 9) | 37:30–40:00 |
| J. Step 9 (celda 10) | 40:00–45:00 |
| K. Conclusiones (celda 11) | 45:00–46:30 |
| L. Epílogo | 46:30–48:30 |

**Porcentaje de tipeo esperado:** 16,3 ÷ 48 ≈ **34%** a 175 caracteres por minuto. A 150 caracteres por minuto da ~38% y el video roza el máximo: **no alcanza**. Por eso la velocidad de tipeo en silencio es lo que tenés que practicar.

**Margen:** unos 3 minutos hasta 50:59. Si en la práctica te pasás de 49 minutos, recortá **palabras** de las 🟢 (nunca las 🖱️ ni las 🗣️⌨️, que son las que cuentan para What + Where).

---

## Checklist

**Antes de grabar**

- [ ] Practicá dos veces con cronómetro. En una de las prácticas, medí **solo el tipeo** (pausá el cronómetro mientras hablás): tiene que dar **≤ 16 min**.
- [ ] Creá el notebook **discount_analysis** en Colab, con la **celda 1 ya armada** (import + dos `read_csv`) y **sin ejecutar**.
- [ ] En **Files**, subí los dos CSV del Escritorio. Los del Escritorio son los originales: no los toques.
- [ ] **Tools → Settings → AI assistance**: ocultá las funciones de IA.
- [ ] **Tools → Settings → Editor**: si está la opción, desactivá las sugerencias automáticas de código (*Automatically trigger code completions*). Todo se tipea a mano: **no se usa autocompletado**.
- [ ] Zoom (`Cmd + +`). Firefox con la ventana 1 en la descripción de la tarea y la ventana 2 en Colab (segunda línea del Dock).
- [ ] Grabá enseguida después de subir los CSV.

**Durante (lo que marcó el reviewer)**

- [ ] **Nunca hablar y tipear al mismo tiempo.** Frase 🗣️⌨️ con las manos quietas → bloque en silencio.
- [ ] **Ningún tramo de tipeo de más de 45 s.** Las dos líneas partidas (`money` y `s.assign`) se tipean en dos tramos, con la frase en el medio y **sin Enter**.
- [ ] **Cada acción con qué + dónde** (número de celda, línea, columna, botón) y, cuando no es obvio, **por qué**.
- [ ] **El número de celda se repite al menos una vez por minuto.**
- [ ] Respetá la regla del mouse. Si hacés algo fuera del guion, usá una frase comodín.
- [ ] Ejecutá cada celda una vez, en orden. **No repitas la celda 1 después de la celda 10.**
- [ ] No termines antes de las conclusiones, **Cmd + S** y el epílogo. **TaskRecorder se abre recién después del epílogo.**

**Después**

- [ ] Detené TaskRecorder. Descargá el `.ipynb` y los 4 CSV de Colab.
- [ ] **Run full AutoQC** y revisá los dos números: **tipeo ≤ 35%** y **What + Where ≥ 70%**. Si alguno falla, no subas: avisame con los números.
- [ ] Armá **Deliverables.zip** con el `.ipynb`, los 4 CSV y la carpeta `original/` con los dos CSV del Escritorio.
- [ ] Marcá en Studio la opción de archivos generados con IA.
- [ ] Subí por separado el **MP4**, el **ZIP de TaskRecorder**, **Deliverables.zip** y **Metadata.rtf**.
