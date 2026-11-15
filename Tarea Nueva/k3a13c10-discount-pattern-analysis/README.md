# k3a13c10 — Analyze Discount Patterns in Sales Data Using Python and Pandas

Guion para grabar la tarea **k3a13c10**. En **Google Colab**, con **pandas**, trabajás sobre 2.200 ventas sintéticas de 2025 con problemas reales:

- corregís las unidades del descuento con evidencia;
- detectás los descuentos inusuales;
- validás las promociones;
- medís en dólares cuánto margen cuestan;
- **reescribís los dos archivos de entrada**.

Todo se **tipea y se explica en vivo**, intercalado, en **una sola toma**, en **Firefox**.

**Duración estimada: ~40 minutos**, con el método que acertó tu medición real de 75 minutos (ver "Cronograma"). Quedan unos 11 minutos de margen hasta el máximo de 50:59.

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
| **Porcentaje de tipeo** | Cerca del 65%. Con todo en vivo no baja al 25–30%. Confirmá el límite en las guías y usá **Tab** para autocompletar. |
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
   - *"I'm pressing Tab to autocomplete the column name."*
   - *"I'm scrolling right inside the table, to see the last columns."*
   - *"I'm clicking at the end of the line, to fix a typo."*
   - *"I'm pressing Escape to close the suggestion box."*

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

> 🖱️ I'm pointing at the Non-Null Count column of the first output.

> 🟢 Only promotion_id has gaps, meaning no promotion.

> 🖱️ I'm scrolling down to describe and pointing at the max discount, 26.

> 🟢 26 is impossible as a fraction, so some values look like percentages. I'll test that against the revenue.

📘 Reads both files with real dates. `info()` shows rows, columns, types and non-null counts (missing values). `describe()` shows the ranges, including the impossible max discount of 26.

**Resultado esperado:** `2200 entries`, `promotion_id 188 non-null`. Calendario `8 entries`. `discount_rate` max 26,0.

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

> 🖱️ I'm pointing at the six rows of the result.

> 🟢 Only six sales don't reconcile, so the eight converted values were really percentages.

> 🟢 These six ignore the discount, with no evidence of which side is wrong, so I won't overwrite them.

📘
- `disc`: the discount as a fraction.
- `gross`, `net`, `profit`: gross sales, recalculated net revenue and gross profit.
- `diff`: recorded minus recalculated revenue.
- `cost`: the margin given away by the discount.
- `gap15`: the profit dollars missing to reach a 15% margin. `clip(lower=0)` turns negatives into 0.
- The last line: the sales that don't reconcile. `s["diff"]` needs brackets because `s.diff` is a pandas method.

**Resultado esperado:** 6 filas: `T00722`, `T01588`, `T01684`, `T01737`, `T01929`, `T02155`.

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

> 🖱️ I'm pointing at the printed line, 135 and 0.56.

> 🟢 135 small-group sales are left to the business rules. 56% of discounts are zero, so the limit is 2.5 times Q3; using only discounted sales leaves 8 groups, so I keep this.

> 🖱️ I'm scrolling right in the outlier table to the promotion_id column.

> 🟢 15 outliers, some of them authorized Black Friday sales: a screen, not a verdict.

📘
- `g`: the discounts grouped by category × month.
- `q1, q3, n`: the quartiles and size of each sale's own group.
- `iqr`: an outlier only in groups of 20 or more.
- The print shows the sales not screened (135) and the share of zero discounts (0.56).
- `s[s.iqr]`: the outliers.

**Resultado esperado:** `135 0.56`. 15 filas.

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

> 🖱️ I'm moving the mouse across the five check columns.

> 🟢 17 of 188 promotion sales fail, and each column shows the reason.

📘
- `v`: the 188 promotion sales with their calendar data.
- The five `_ok` columns: the ID exists, the category matches, the date is inside the campaign, the discount is within the maximum, and it's within 5 points of the plan.
- `bad`: the sales that fail at least one check.

**Resultado esperado:** 17 filas: PRM-01 (4), PRM-02 (4), PRM-05 (3), PRM-99 (3) y PRM-07 (3).

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

> 🖱️ I'm scrolling right in the table to the iqr column.

> 🟢 Ten discounts above 30%, and IQR missed three, so this rule stays independent.

📘
- `valid`: a promotion that exists, matches the category and is inside its dates.
- `promo_issue`: the sale failed a check.
- `over30`: above 30% without a valid promotion.
- `low`: below the 15% margin.

**Resultado esperado:** 10 filas. `iqr` False en `T00123`, `T00649` y `T01356`.

---

### G. Step 6: impacto en el margen

> 🖱️ I'm clicking plus Code at the top left, to add the sixth cell.

> 🟢 Step six: the impact on margin. I'll write one function so every table uses the same definitions.

> ⌨️ impact adds up transactions, sales, profit, discount cost, and the gap to the floor.

```python
def impact(by):
    t = s.groupby(by).agg(n=("net", "size"), sales=("net", "sum"), profit=("profit", "sum"), cost=("cost", "sum"), gap15=("gap15", "sum"))
```

> ⌨️ The margin is total profit over total sales, so big sales weigh more.

```python
    t["margin"] = t.profit / t.sales
    return t.round(2)
```

> ⌨️ I'm pressing Delete to go back to the margin. Now the same table by category, with and without a valid promotion.

```python
cat = impact(["category", "valid"])
```

> ⌨️ Most promotions are Electronics, a thin-margin category, so I compute the no-promotion margin at the same category mix.

```python
w = cat.xs(True, level=1).sales
print(round((cat.xs(False, level=1).margin * w).sum() / w.sum(), 3))
```

> ⌨️ And I show the tables: valid or not, by category, and by valid promotion.

```python
display(impact("valid"), cat)
pr = impact(s.promotion_id.where(s.valid))
pr
```

> 🖱️ I'm clicking Run on the left of the sixth cell.

> 🖱️ I'm pointing at 0.309 and the first table below it.

> 🟢 17% against 33%, but at the same mix the baseline is 31%, so most of the gap is the discount.

> 🖱️ I'm scrolling down to the PRM-07 row of the last table.

> 🟢 PRM-07, Black Friday Electronics, keeps only a 3% margin. No other campaign comes close.

📘
- `impact()`: transactions, sales, gross profit, discount cost, gap to the floor and weighted margin, for any grouping.
- `cat`: the same values by category and validity.
- `w`: the promotional sales of each category (the mix).
- The print: the margin without promotion, with the promotions' mix (0.309).
- `pr`: one row per valid promotion.

**Resultado esperado:** `0.309`. False 0,33 / True 0,17. PRM-07: 33 · 27.874,68 · 732,29 · 9.227,69 · 3.448,92 · 0,03.

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

> 🖱️ I'm moving the mouse down the four figures.

> 🟢 Discounts cost 35,095 dollars. The unusual ones only 1,073 above normal, and PRM-07 explains 3,449 of the 3,870 below the floor.

> 🟢 So the priority is PRM-07, not the violations.

📘
- `plan`: the planned discount of each sale's promotion.
- `excess`: the discount dollars above the reference (the planned rate if valid, otherwise the group median).
- `u`: the 30 unusual sales.
- `money`: the total cost, the unusual excess, the total gap to the floor and PRM-07's gap.

**Resultado esperado:** cost 35.094,64 · unusual 1.072,70 · gap15 3.869,71 · prm07 3.448,92.

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

> 🖱️ I'm clicking Run, and pointing at the Sum and Total rows.

> 🟢 Both match; the 58 dollars are the six mismatches.

📘 The totals by category, plus the sum of the categories and the overall total. Both rows must be equal.

**Resultado esperado:** `Sum` = `Total`: 489.707,18 · 489.648,79 · 58,39.

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

> 🖱️ I'm clicking Run, then opening the Files panel on the left and pointing at the four files.

> 🟢 Both input files are rewritten with the same names, and 104 sales are flagged for review.

> 🖱️ I'm closing the Files panel.

📘
- `flagged_transactions.csv`: the 104 sales with at least one reason.
- **`sales_transactions.csv` is rewritten:** the corrected discount, the original in `discount_raw`, the calculations and the flags. `net_revenue` is not touched.
- **`promotion_calendar.csv` is rewritten** with each valid promotion's results.
- `summary_results.csv`: the counts by reason plus the money figures.

**Resultado esperado:** iqr 15, data_issue 14, promo_issue 17, over30 10, low 72, más las 4 cifras en dólares.

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
| Tipeo (código + conclusiones) | ~3.035 caracteres | ~25 min |
| Narración | ~1.360 palabras | ~10,5 min |
| Navegación | — | ~4 min |
| **Total** | | **~40 min** |

| Sección | Aprox. |
| ------- | ------ |
| A. Apertura | 0:00–1:00 |
| B. Step 1 | 1:00–3:30 |
| C. Step 2 | 3:30–8:30 |
| D. Step 3 | 8:30–12:30 |
| E. Step 4 | 12:30–17:30 |
| F. Step 5 | 17:30–20:30 |
| G. Step 6 | 20:30–26:30 |
| H. Step 7 | 26:30–30:30 |
| I. Step 8 | 30:30–32:00 |
| J. Step 9 | 32:00–37:00 |
| K. Conclusiones | 37:00–39:00 |
| L. Epílogo | 39:00–40:00 |

**Margen:** unos 11 minutos hasta 50:59. Si con práctica tipeás a 150 caracteres por minuto, baja a unos **35 minutos**. **Medilo:** hacé una práctica completa con cronómetro, y si pasa de 44 minutos, decime en qué step.

---

## Checklist

**Antes de grabar**

- [ ] Practicá dos veces, con cronómetro. `discount_analysis.ipynb` tiene el código completo para comparar.
- [ ] Creá el notebook vacío **discount_analysis** en Colab.
- [ ] En **Files**, subí los dos CSV del Escritorio. Los del Escritorio son los originales: no los toques.
- [ ] **Tools → Settings → AI assistance**: ocultá las funciones de IA.
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
