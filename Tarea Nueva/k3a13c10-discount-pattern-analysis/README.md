# k3a13c10 — Analyze Discount Patterns in Sales Data Using Python and Pandas

Guion **final y compacto** para grabar la tarea **k3a13c10**. En **Google Colab**, con **pandas**, trabajás sobre 2.200 ventas sintéticas de 2025 con problemas reales:

- corregís las unidades del descuento con evidencia;
- detectás los descuentos inusuales;
- validás las promociones;
- medís en dólares cuánto margen cuestan;
- **reescribís los dos archivos de entrada**.

Todo se **tipea y se explica en vivo**, en **una sola toma**, en **Firefox**.

**Duración estimada: ~35 minutos**, con el método que acertó tu medición real de 75 minutos (ver sección 6). Quedan unos 16 minutos de margen hasta el máximo de 50:59.

**Cómo leer este guion:**

- 🖱️ = lo decís **mientras hacés** la acción: qué, dónde y por qué. AutoQC cuenta estas frases.
- ⌨️ = lo decís **mientras tipeás** la línea indicada entre paréntesis: qué tipeás y dónde.
- 🟢 = la conclusión de un resultado, en una o dos frases. **No se leen las tablas.**
- 📘 = la explicación de cada línea, en inglés. Es para vos: **no se lee**.
- **Las frases son cortas a propósito.** Cada palabra que agregues suma tiempo: no improvises explicaciones extra.

---

## Pendientes antes de grabar

| Tema | Qué hacer |
| ---- | --------- |
| **Origen de los CSV** | Los generé yo, Claude, con un script de Python: "generated with AI" es cierto, "Gemini" no. Marcá en Studio la opción de archivos generados con IA. |
| **Porcentaje de tipeo** | Cerca del 70%. Con todo en vivo no baja al 25–30%. Confirmá el límite en las guías y usá **Tab** para autocompletar. |
| **Versión de pandas** | Lo probé con pandas 3.1. Si `info()` dice `object` en vez de `str`, es lo mismo. |

---

## 1. Qué cumple y dónde (criterios de Slack + Goal)

| Criterio o requisito | Dónde |
| -------------------- | ----- |
| Carga, dimensiones, tipos y faltantes | Step 1 |
| Corrección de unidades con evidencia, sin perder el original | Step 2 (`disc`) y Step 9 (`discount_raw`) |
| Descuentos atípicos por categoría y mes, con IQR y mínimo de 20 | Step 3 |
| Justificación del IQR (56% de descuentos en cero) | Step 3 |
| 5 validaciones del calendario y tabla visible | Step 4 |
| Reglas del 30% y del 15%, independientes | Step 5 |
| Con y sin promoción, por categoría y por promoción | Step 6 |
| Corrección por mezcla de categorías | Step 6 (0.309) |
| **Impacto en dólares:** costo total, exceso de los inusuales, distancia al piso del 15% y PRM-07 | Steps 2, 6 y 7 |
| Reconciliación de las categorías contra el total | Step 8 |
| **Modificación material de los archivos de entrada** | Step 9: se reescriben los dos CSV |
| Exportar las ventas marcadas y el resumen | Step 9 |
| Conclusiones con prioridad económica | Celda de texto |
| Declaración de IA | Celda de texto + Studio |

**Qué saqué para acortar, sin perder ningún requisito:**
- **El pivot de descuentos:** el IQR ya es por categoría × mes.
- **Dos prints:** sus números aparecen en el resumen final.
- **La columna `margin`:** `low` sale de `gap15`.
- **Las listas de columnas a mostrar.**
- **La pérdida de las ventas de más de 30%.**
- **La recomendación larga del epílogo.**

---

## 2. Código completo, por celda

Probado con los dos CSV. Los nombres son cortos a propósito: `s` = sales, `p` = promotions, `v` = validated.

### Step 1 (191 caracteres)

```python
import pandas as pd
s = pd.read_csv("sales_transactions.csv", parse_dates=["date"])
p = pd.read_csv("promotion_calendar.csv", parse_dates=["start_date", "end_date"])
s.info()
p.info()
s.describe()
```

📘 Reads both files with real dates. `info()` shows rows, columns, types and non-null counts (missing values). `describe()` shows the ranges, including the impossible max discount of 26.

### Step 2 (361 caracteres)

```python
s["disc"] = s.discount_rate.where(s.discount_rate <= 1, s.discount_rate / 100)
s["month"] = s.date.dt.month
s["gross"] = s.quantity * s.unit_price
s["net"] = s.gross * (1 - s.disc)
s["profit"] = s.net - s.quantity * s.unit_cost
s["diff"] = s.net_revenue - s.net
s["cost"] = s.gross * s.disc
s["gap15"] = (0.15 * s.net - s.profit).clip(lower=0)
s[s["diff"].abs() > 0.01]
```

📘
- `disc`: the discount as a fraction (values above 1 are divided by 100).
- `gross`, `net`, `profit`: gross sales, recalculated net revenue and gross profit.
- `diff`: recorded minus recalculated revenue.
- `cost`: the margin given away by the discount.
- `gap15`: the profit dollars missing to reach a 15% margin (0 if above the floor).
- The last line: the sales that don't reconcile. `s["diff"]` needs brackets because `s.diff` is a pandas method.

### Step 3 (248 caracteres)

```python
g = s.groupby(["category", "month"]).disc
q1, q3, n = g.transform("quantile", 0.25), g.transform("quantile", 0.75), g.transform("size")
s["iqr"] = (n >= 20) & (s.disc > q3 + 1.5 * (q3 - q1))
print((n < 20).sum(), (s.disc == 0).mean().round(2))
s[s.iqr]
```

📘
- Each sale gets the Q1, Q3 and size of its own category × month group.
- `iqr` is an outlier only in groups of 20 or more.
- The print shows the sales not screened (135) and the share of zero discounts (0.56).
- The last line shows the outliers.

### Step 4 (408 caracteres)

```python
v = s[s.promotion_id.notna()].merge(p, how="left")
v["id_ok"] = v.max_discount.notna()
v["cat_ok"] = v.category == v.applicable_category
v["date_ok"] = v.date.between(v.start_date, v.end_date)
v["max_ok"] = v.disc <= v.max_discount
v["plan_ok"] = (v.disc - v.planned_discount).abs().round(4) <= 0.05
c = ["id_ok", "cat_ok", "date_ok", "max_ok", "plan_ok"]
bad = v[v[c].all(axis=1) == False]
bad[["promotion_id"] + c]
```

📘
- The 188 promotion sales are joined with the calendar (`left` keeps unknown IDs).
- Five separate checks: the ID exists, the category matches, the date is inside the campaign, the discount is within the maximum, and it's within 5 points of the plan.
- `bad` keeps the sales that fail at least one check, and the last line shows them.

### Step 5 (233 caracteres)

```python
ok = v[v.id_ok & v.cat_ok & v.date_ok].transaction_id
s["valid"] = s.transaction_id.isin(ok)
s["promo_issue"] = s.transaction_id.isin(bad.transaction_id)
s["over30"] = (s.disc > 0.3) & (s.valid == False)
s["low"] = s.gap15 > 0
s[s.over30]
```

📘
- `valid`: a promotion that exists, matches the category and is inside its dates.
- `promo_issue`: the sale failed a check.
- `over30`: above 30% without a valid promotion.
- `low`: below the 15% margin.
- The last line shows the over-30% sales.

### Step 6 (417 caracteres)

```python
def impact(by):
    t = s.groupby(by).agg(n=("net", "size"), sales=("net", "sum"), profit=("profit", "sum"), cost=("cost", "sum"), gap15=("gap15", "sum"))
    t["margin"] = t.profit / t.sales
    return t.round(2)
cat = impact(["category", "valid"])
w = cat.xs(True, level=1).sales
print(round((cat.xs(False, level=1).margin * w).sum() / w.sum(), 3))
display(impact("valid"), cat)
pr = impact(s.promotion_id.where(s.valid))
pr
```

📘
- `impact()` returns, for any grouping, the transactions, sales, gross profit, discount cost, gap to the floor and weighted margin.
- `cat`: the same values by category, with and without a valid promotion.
- `w`: the promotional sales of each category (the mix).
- The print gives the margin without promotion **with that same mix**: 0.309.
- `display` shows valid vs not, and the category table.
- `pr`: one row per valid promotion.

Después del `return`: **Enter** y **Delete** para volver al margen.

### Step 7 (338 caracteres)

```python
plan = s.promotion_id.map(p.set_index("promotion_id").planned_discount)
s["excess"] = (s.gross * (s.disc - plan.where(s.valid, g.transform("median")))).clip(lower=0)
u = s.iqr | s.over30 | s.promo_issue
money = pd.Series({"cost": s.cost.sum(), "unusual": s[u].excess.sum(), "gap15": s.gap15.sum(), "prm07": pr.gap15["PRM-07"]}).round(2)
money
```

📘
- `excess`: the discount dollars above a reference. The reference is the planned rate if the promotion is valid, and otherwise the median of its category × month.
- `u`: the 30 unusual sales.
- `money` gathers four figures:
  - the total discount cost;
  - the excess of the unusual sales;
  - the total gap to the floor;
  - PRM-07's gap.

### Step 8 (127 caracteres)

```python
k = ["net_revenue", "net", "diff"]
r = s.groupby("category")[k].sum()
r.loc["Sum"] = r.sum()
r.loc["Total"] = s[k].sum()
r.round(2)
```

📘 The totals by category, plus the sum of the categories and the overall total. Both rows must be equal.

### Step 9 (472 caracteres)

```python
s["data_issue"] = (s["diff"].abs() > 0.01) | (s.discount_rate > 1)
f = ["iqr", "data_issue", "promo_issue", "over30", "low"]
s[s[f].any(axis=1)].to_csv("flagged_transactions.csv", index=False)
s.assign(discount_raw=s.discount_rate, discount_rate=s.disc).drop(columns="disc").to_csv("sales_transactions.csv", index=False)
p.merge(pr.reset_index(), how="left").to_csv("promotion_calendar.csv", index=False)
res = pd.concat([s[f].sum(), money])
res.to_csv("summary_results.csv")
res
```

📘
- `flagged_transactions.csv`: the 104 sales with at least one reason.
- **`sales_transactions.csv` is rewritten:** `discount_rate` holds the corrected value, the original stays in `discount_raw`, and it adds the calculations and the flags. `net_revenue` is not touched.
- **`promotion_calendar.csv` is rewritten** with each valid promotion's results.
- `summary_results.csv`: the counts by reason plus the money figures.

### Celda de texto (241 caracteres)

```markdown
## Summary
- Discounts cost $35,095; unusual ones only $1,073 above normal.
- PRM-07 explains $3,449 of the $3,870 below the 15% floor.
- Promotion margin: 17% vs 31% at the same category mix.
- Inputs fixed and updated. Files generated with AI.
```

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

## 3. Guion de grabación

**Ciclo de cada celda:** **+ Code** → tipear con ⌨️ → **Run** → señalar → 🟢.

### A. Apertura (~1 min)

Con la **descripción de la tarea** en pantalla:

> 🟢 I will be beginning my task soon. I'll analyze discount patterns in a year of sales data with pandas, measure their cost in margin dollars, and update the input files.

> 🖱️ I'm clicking the yellow minimize button at the top left, and choosing my Colab notebook, the second window of Firefox in the Dock.

> 🖱️ I'm opening the Files panel on the left: both CSV files are uploaded. They're synthetic, generated with AI, and the originals stay on my Desktop.

> 🖱️ I'm closing the panel and clicking inside the empty code cell.

### B. Step 1

> ⌨️ *(todo)* I'm typing the imports, the two files with real dates, info, and describe in the first cell.

> 🖱️ I'm clicking Run on the left of the cell, and pointing at the Non-Null column and the max discount.

> 🟢 Only promotion_id has gaps, which means no promotion. A max discount of 26 is impossible as a fraction, so I'll test it against the revenue.

### C. Step 2

> 🖱️ I'm clicking plus Code at the top left.

> ⌨️ *(disc)* I'm typing disc: values above 1 become fractions, in a new column.

> ⌨️ *(resto)* I'm typing the recalculated revenue, profit, difference, discount cost, and gap to the 15% floor, in dollars.

> 🖱️ I'm clicking Run, and pointing at the six rows.

> 🟢 Only six don't reconcile, so the eight converted values were percentages. These six ignore the discount with no evidence of which side is wrong, so I keep them as recorded.

### D. Step 3

> 🖱️ I'm clicking plus Code.

> ⌨️ *(todo)* I'm typing the IQR by category and month, only in groups of 20 or more, and the share of zero discounts.

> 🖱️ I'm clicking Run, and pointing at 135 and 0.56.

> 🟢 135 small-group sales are left to the business rules. 56% of discounts are zero, so the limit is 2.5 times Q3, and using only discounted sales would leave 8 groups, so I keep it. The 15 outliers include authorized Black Friday sales: a screen, not a verdict.

### E. Step 4

> 🖱️ I'm clicking plus Code.

> ⌨️ *(merge)* I'm typing the join with the calendar; left keeps unknown IDs.

> ⌨️ *(checks)* I'm typing the five checks and the table of failures.

> 🖱️ I'm clicking Run, and moving across the check columns.

> 🟢 17 of 188 promotion sales fail, each with its reason. Most look statistically normal, so this check is needed.

### F. Step 5

> 🖱️ I'm clicking plus Code.

> ⌨️ *(todo)* I'm typing valid promotion, the 30% rule, and the 15% rule, on all sales.

> 🖱️ I'm clicking Run, and scrolling right to the iqr column.

> 🟢 Ten discounts above 30%, and IQR missed three. That's why the rule is independent.

### G. Step 6

> 🖱️ I'm clicking plus Code.

> ⌨️ *(def)* I'm typing the impact function, so every table uses the same definitions.

> ⌨️ *(mix)* I'm pressing Delete to go back to the margin, and typing the mix check: the margin without promotion at the promotions' category mix.

> ⌨️ *(display, pr)* I'm typing the tables by validity, category, and promotion.

> 🖱️ I'm clicking Run, and pointing at 0.309 and the first table.

> 🟢 17% against 33%, but at the same mix the baseline is 31%. So most of the gap is the discount, not the category.

> 🖱️ I'm scrolling down to the PRM-07 row.

> 🟢 PRM-07 keeps a 3% margin. No other campaign comes close.

### H. Step 7

> 🖱️ I'm clicking plus Code.

> ⌨️ *(excess)* I'm typing excess: discount above the planned rate, or above the group median. A zero reference would count normal discounts as losses.

> ⌨️ *(money)* I'm typing the money summary.

> 🖱️ I'm clicking Run, and moving down the four figures.

> 🟢 Discounts cost 35,095 dollars, the unusual ones only 1,073 above normal, and PRM-07 explains 3,449 of the 3,870 below the floor. So the priority is the PRM-07 rate.

### I. Step 8

> 🖱️ I'm clicking plus Code.

> ⌨️ *(todo)* I'm typing the category totals with a Sum and a Total row.

> 🖱️ I'm clicking Run, and pointing at the two rows.

> 🟢 They match, and the 58 dollars are the six mismatches.

### J. Step 9

> 🖱️ I'm clicking plus Code.

> ⌨️ *(flags, flagged)* I'm typing the review reasons and the flagged export.

> ⌨️ *(sales, calendar)* I'm typing the rewrite of both input files: the corrected discount with the original kept, and each promotion's results in the calendar.

> ⌨️ *(res)* I'm typing the summary export.

> 🖱️ I'm clicking Run, then opening Files on the left and pointing at the four files.

> 🟢 Both inputs are rewritten, and 104 sales are flagged for review.

> 🖱️ I'm closing the Files panel.

### K. Conclusiones

> 🖱️ I'm clicking plus Text at the top left.

> ⌨️ *(todo)* I'm typing the summary, starting with dollars.

> 🖱️ I'm clicking below the cell to show it, and pressing Command + S to save.

### L. Epílogo (~1 min)

> 🖱️ I'm scrolling up through the notebook.

> 🟢 My approach was evidence first, and keeping every original value. The challenge was measuring impact fairly: counted, the violations looked like the problem, but in dollars the real issue is PRM-07, an authorized campaign. I'd review its rate first. The limits are one year of synthetic data and no customer data. Thanks for watching!

---

## 4. Resultados esperados (para vos)

| Step | Lo que tiene que aparecer |
| ---- | ------------------------- |
| 1 | `2200 entries`, `promotion_id 188 non-null`. Calendario `8 entries`. `discount_rate` max 26,0. |
| 2 | 6 filas: `T00722`, `T01588`, `T01684`, `T01737`, `T01929`, `T02155`. |
| 3 | `135 0.56`. 15 filas. |
| 4 | 17 filas: PRM-01 (4), PRM-02 (4), PRM-05 (3), PRM-99 (3) y PRM-07 (3). |
| 5 | 10 filas. `iqr` False en `T00123`, `T00649` y `T01356`. |
| 6 | `0.309`. False 0,33 / True 0,17. PRM-07: 33 · 27.874,68 · 732,29 · 9.227,69 · 3.448,92 · 0,03. |
| 7 | cost 35.094,64 · unusual 1.072,70 · gap15 3.869,71 · prm07 3.448,92. |
| 8 | `Sum` = `Total`: 489.707,18 · 489.648,79 · 58,39. |
| 9 | iqr 15, data_issue 14, promo_issue 17, over30 10, low 72, más las 4 cifras en dólares. |

---

## 5. Si algo sale mal

| Error | Qué decís y hacés |
| ----- | ----------------- |
| Un nombre mal escrito | 🖱️ *"There's a typo in this cell. I'm fixing the name and running it again."* |
| `s.diff` sin corchetes | 🖱️ *"diff is a pandas method, so I need brackets. I'm fixing it."* |
| Sangría del `def` | 🖱️ *"The indentation is wrong in the function. I'm fixing it and running again."* |
| `KeyError: 'PRM-07'` | 🖱️ *"Step six didn't run. I'm running it and then this cell."* |
| `NameError` | 🖱️ *"An earlier cell didn't run. I'm choosing Run before in the Runtime menu."* |
| Hay que repetir todo después del Step 9 | 🖱️ *"The inputs were already rewritten, so I'm uploading the originals from my Desktop again."* |

---

## 6. Cronograma

**Método calibrado** (el mismo que dio 75–80 minutos para el guion viejo, y vos mediste 75): 120 caracteres por minuto de tipeo, 130 palabras por minuto de narración, **todo sumado**, y unos 25 segundos de navegación por celda.

| | Cantidad | Tiempo |
| - | -------- | ------ |
| Tipeo (código + conclusiones) | ~3.035 caracteres | ~25 min |
| Narración | ~760 palabras | ~6 min |
| Navegación (10 celdas, Files) | — | ~4 min |
| **Total** | | **~35 min** |

| Sección | Aprox. |
| ------- | ------ |
| A. Apertura | 0:00–1:00 |
| B. Step 1 | 1:00–3:00 |
| C. Step 2 | 3:00–7:00 |
| D. Step 3 | 7:00–10:00 |
| E. Step 4 | 10:00–14:30 |
| F. Step 5 | 14:30–17:00 |
| G. Step 6 | 17:00–22:00 |
| H. Step 7 | 22:00–25:30 |
| I. Step 8 | 25:30–27:00 |
| J. Step 9 | 27:00–31:30 |
| K. Conclusiones | 31:30–34:00 |
| L. Epílogo | 34:00–35:00 |

**Margen:** unos 16 minutos hasta 50:59. Si practicás y tipeás a 150 caracteres por minuto, baja a unos **30 minutos**.

**Medilo:** hacé una práctica completa con cronómetro. Si pasa de 40 minutos, decime en qué sección se fue el tiempo.

---

## 7. Checklist

**Antes de grabar**

- [ ] Practicá tipeando las 9 celdas y las conclusiones dos veces, con cronómetro.
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
