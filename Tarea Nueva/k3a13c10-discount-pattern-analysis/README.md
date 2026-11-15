# k3a13c10 — Analyze Discount Patterns in Sales Data Using Python and Pandas

Guion **optimizado** para grabar la tarea **k3a13c10** (Data Science & Analytics). En **Google Colab**, con **pandas**, analizás los descuentos de 2.200 ventas sintéticas de 2025:

- encontrás los descuentos inusuales por categoría y mes;
- los comparás con el calendario de promociones;
- aplicás dos reglas de negocio independientes;
- medís el impacto en el margen bruto;
- reconciliás los totales y exportás los entregables.

Se graba en **Firefox**, en **una sola toma**, y tiene que durar **entre 15:00 y 50:59**. Este guion apunta a **32–37 minutos reales**.

**El código y el resumen se tipean y se explican en vivo**, como exige la tarea. Para bajar el tiempo achiqué lo que hay que tipear y lo que hay que decir, sin sacar ningún requisito:

| | Antes | Ahora |
| - | ----- | ----- |
| Celdas de código | 13 | **8** |
| Caracteres de código | ~3.600 | **~2.165** |
| Caracteres del resumen | ~900 | **~465** |
| Palabras de narración | ~4.360 | **~2.400** (unas 370 se dicen mientras tipeás, así que no suman tiempo) |

**Cómo leer este guion:**

- 🖱️ = lo decís **mientras hacés** la acción: **qué** hacés, **dónde** está en la pantalla y **por qué**. AutoQC cuenta estas frases: **no te saltees ninguna**.
- ⌨️ = lo decís **mientras tipeás** la línea indicada (entre paréntesis). Tiene dos partes, y las dos se dicen:
  - **qué** tipeás y **dónde**: *"I'm typing the disc line, the first line of the second cell."* Esta parte es la que cuenta AutoQC;
  - **para qué** sirve esa línea.
- 🟢 = la interpretación de un resultado, o la transición.
- 📘 **What each line does** (sección 4): la explicación de cada línea, en inglés, por si tenés dudas. **No se lee**.
- **Resultado esperado**: los números reales que tienen que aparecer. Son para vos.
- Si usás un atajo de teclado, decí la tecla en voz alta: *"I'm pressing Command + S"*.

---

## La regla del mouse (leela antes de practicar)

El revisor marcó que **no explicás todo lo que hacés**. Casi siempre pasa por movimientos del mouse sin frase: lo movés hacia cualquier lado mientras pensás, mientras leés el guion o mientras esperás. Para el revisor, y para AutoQC, **cada movimiento es una acción**, y una acción sin frase cuenta como no explicada.

1. **El mouse solo se mueve cuando decís una frase 🖱️.** Si no estás diciendo una, la mano no toca el mouse.
2. **Mientras tipeás, soltá el mouse.** Las dos manos en el teclado. El cursor queda quieto donde estaba.
3. **Al terminar una acción, dejá el cursor quieto en el margen derecho de Colab**, en la zona blanca, lejos del código. Nunca lo dejes encima de botones: Colab muestra cartelitos y parece que hacés algo.
4. **Para señalar un resultado, decí primero la frase y movelo después**: *"I'm pointing at…"* y recién ahí el mouse va a ese lugar. Un solo movimiento, directo, sin vueltas.
5. **Si tenés que leer el guion, leelo con el mouse quieto.** Los ojos se mueven, la mano no.
6. **Si hacés algo que no está en el guion** (un scroll de más, un clic para corregir, cerrar un cartel), usá una frase comodín de la tabla siguiente. Nunca lo hagas en silencio.

### Frases comodín para acciones no planificadas

| Acción | Frase |
| ------ | ----- |
| Mover el mouse hacia el botón Run | *"I'm moving the mouse to the Run button, on the left of the cell."* |
| Scroll de más, hacia abajo o hacia arriba | *"I'm scrolling down a bit, to see the end of the output."* / *"I'm scrolling back up to the cell I'm working on."* |
| Scroll horizontal en una tabla ancha | *"I'm scrolling right inside the table, to see the last columns."* |
| Hacer clic en una celda para seguir tipeando o corregir | *"I'm clicking at the end of the line in the second cell, to fix a typo."* |
| Autocompletar con Tab | *"I'm pressing Tab to autocomplete the column name."* |
| Cerrar la ventanita de autocompletado o de ayuda de Colab | *"I'm pressing Escape to close the suggestion box."* |
| Esperar a que termine una celda | *"I'm waiting for the cell to finish; the spinner on the left shows it's running."* |
| Cerrar un aviso de Colab | *"I'm clicking Close on the notice at the bottom of the screen."* |
| Acomodar la pantalla | *"I'm scrolling so the whole cell is visible in the center of the screen."* |
| Volver a mirar algo de una celda anterior | *"I'm scrolling up to the third cell, to check the IQR result again."* |

---

## Pendientes antes de grabar

| Tema | Situación | Qué hacer |
| ---- | --------- | --------- |
| **Porcentaje de tipeo** | ~2.630 caracteres a unos 150 por minuto son **~17 min de tipeo**: cerca del **50%** de una grabación de 34 minutos. Con todos los requisitos tipeados en vivo, bajar del 25–30% obligaría a pasar los 50:59, así que no se puede cumplir del todo. El guion anterior tenía el mismo problema, con ~45% y más caracteres. | Confirmá en las guías de Project Dawn si el límite de tipeo aplica a las tareas de programación y cuánto es. Si es estricto, avisame y vemos qué se puede recortar del alcance. Mientras tanto, usá el **autocompletado de Colab** (ver "Antes de grabar"), que reduce las teclas. |
| **Origen de los CSV** | Los dos CSV los generé yo, Claude, con un script de Python. "Generated with AI" es **cierto**; "Gemini" **no**. | El resumen dice *"generated with AI before recording"*. Marcá en Studio la opción de archivos generados con IA. Si el formulario pide la herramienta: Claude. |
| **Versión de pandas** | Lo probé con pandas 3.1. Colab suele traer la 2.x. | Si `info()` dice `object` en vez de `str`, decí *"object means text"*. Los números no cambian. |

---

## 1. Diagnóstico: por qué el guion anterior lleva unos 75 minutos

**Lo único medido es tu tiempo total: 75 minutos.** Todo lo demás de esta sección son **estimaciones mías**. Las calculé contando el guion anterior y usando dos velocidades:

- **Hablar** a unas 130 palabras por minuto.
- **Tipear** código a unos 120 caracteres por minuto, mientras leés el guion y hablás.

Con esas velocidades, el total da 75–80 minutos, lo que coincide con tu medición.

| Origen del tiempo | Cantidad en el guion anterior | Tiempo estimado |
| ----------------- | ----------------------------- | --------------- |
| Tipear el código (13 celdas) | ~3.600 caracteres | **~30 min** |
| Tipear el resumen | ~900 caracteres | **~7,5 min** |
| Narración (🖱️ + 🟢 + ⌨️) | ~4.360 palabras | **~33 min** |
| Navegación (14 ciclos de *+ Code*, subir archivos, descargar, abrir el visor) | — | **~5–6 min** |
| **Total** | | **~75–80 min** |

Las causas, de mayor a menor peso:

1. **El tipeo.** El guion suponía 300 caracteres por minuto, y eso no es realista para código. Había columnas que se mostraban y no se usaban, nombres largos (`sales`, `promos`, `calc_margin`) repetidos decenas de veces, un `eval` con comillas triples y un resumen de 900 caracteres.
2. **Cada celda se explicaba tres veces:** antes de escribirla (🟢), mientras la escribías (⌨️) y después de ejecutarla. Además, cada resultado tenía varios párrafos.
3. **Demasiados ciclos de celda.** Las celdas 2, 3, 4 y 6 eran pasos chicos, y cada ciclo de *+ Code* suma unos 20–30 segundos.
4. **Pasos que se pueden mover o sacar:** subir los CSV, descargar archivos, el visor de CSV y la sección de recomendaciones, que repetía el resumen.
5. **El resumen quedaba para el final**, cuando ya pasaba la hora. Por eso quedó sin terminar en la grabación anterior.

---

## 2. Qué se reduce, se agrupa o se elimina

En la columna "Tiempo real probable" van mis **estimaciones** (no son mediciones), con las velocidades de la sección 1.

| Paso actual | Tiempo en el guion | Tiempo real probable | Problema detectado | Optimización propuesta |
| ----------- | ------------------ | -------------------- | ------------------ | ---------------------- |
| A. Apertura y subida | 2:00 | ~4 min | 408 palabras de narración y la subida de los archivos (diálogo, Cmd + clic, aviso) | Los CSV se suben **antes**. Apertura de ~200 palabras. |
| B. Celdas 1–3: inspección | 4:00 | ~9 min | Tres celdas, `value_counts` que después no se usan | **Una celda** (Step 1), con `info()` de los dos archivos, que ya muestra dimensiones, tipos y faltantes, y `describe()`. 191 caracteres. |
| C. Celdas 4–5: unidades y recálculo | 4:30 | ~12 min | 800 caracteres. La celda 4 solo servía para probar la conversión. | **Una celda** (Step 2). La prueba de que la conversión es correcta sale gratis: después de convertir, las 8 filas reconcilian al centavo, y solo quedan 6 diferencias. 291 caracteres. |
| D. Celdas 6–7: pivot e IQR | 3:30 | ~9 min | Dos ciclos de celda y un `groupby` extra para contar | **Una celda** (Step 3). 300 caracteres. |
| E. Celda 8: validación | 3:30 | ~9 min | 564 caracteres y un párrafo por tipo de error | El mismo control con nombres cortos (Step 4). 435 caracteres. Una frase por tipo de error. |
| F. Celdas 9–11: 30%, 15% e impacto | 4:30 | ~13 min | Tres celdas. Faltaba comparar el total con promoción contra el total sin promoción. | **Step 5**, las dos reglas, 217 caracteres. **Step 6**, con una **función `impact()`** que se tipea una vez y se usa tres veces, 263 caracteres. |
| G. Recomendaciones | 1:30 | ~2 min | Repite el resumen | **Se elimina**. Van en una línea del epílogo. |
| H. Celdas 12–13 y resumen | 3:30 | **~17 min** | 525 caracteres de código y 900 de resumen, todo al final. Acá se cortó. | **Step 7**, 127 caracteres. **Step 8**, 341 caracteres, con el export del resumen que faltaba. El resumen pasa a **465 caracteres**. |
| I. Presentación final | 1:30 | ~2,5 min | El visor de CSV y el panel de descargas | Los archivos se muestran en el panel **Files**. Las descargas se hacen **después** de grabar. |
| J. Epílogo | 3:30 | ~2,5 min | Largo | ~2 min. |

---

## 3. Notebook compacto

`discount_analysis.ipynb` (en esta carpeta) es el **notebook de referencia** para probar y practicar. **No se usa en la grabación**: ahí empezás con un notebook vacío y tipeás todo.

| Celda | Qué hace | Caracteres | Requisitos |
| ----- | -------- | ---------- | ---------- |
| Step 1 | Carga los dos CSV. Muestra dimensiones, columnas, tipos y faltantes de los dos, y `describe`. | 191 | A |
| Step 2 | Convierte los descuentos guardados como porcentaje, agrega el mes y recalcula ventas, profit, margen y diferencia. Muestra los 6 *mismatches*. | 291 | A |
| Step 3 | Arma el pivot categoría × mes y aplica IQR por grupo, solo en los grupos con 20 ventas o más. | 300 | B |
| Step 4 | Hace las 5 comprobaciones del calendario y muestra la tabla de las 17 ventas inconsistentes. | 435 | C |
| Step 5 | Aplica las reglas de más de 30% sin promoción válida y de margen menor a 15%. | 217 | D |
| Step 6 | Usa `impact()` para comparar con y sin promoción, por categoría y por promoción. | 263 | E |
| Step 7 | Compara las categorías con el total general y muestra las diferencias. | 127 | F |
| Step 8 | Exporta `flagged_transactions.csv` y `summary_results.csv`. | 341 | G |
| Texto | El resumen y las *Final notes*. | 465 | G |

---

## 4. Código completo, por celda

Igual al del notebook de referencia y probado con los dos CSV. Los nombres son cortos a propósito: `s` = sales, `p` = promotions, `v` = validated promotions.

### Step 1

```python
import pandas as pd
s = pd.read_csv("sales_transactions.csv", parse_dates=["date"])
p = pd.read_csv("promotion_calendar.csv", parse_dates=["start_date", "end_date"])
s.info()
p.info()
s.describe()
```

📘 **What each line does** (para vos, no se lee):

- `import pandas as pd`: imports pandas as `pd`.
- `s = pd.read_csv(...)`: reads the sales into `s`, with `date` as a real date.
- `p = pd.read_csv(...)`: reads the calendar into `p`, with the start and end dates as real dates.
- `s.info()` / `p.info()`: rows, columns, non-null count (so, missing values) and data type of each column.
- `s.describe()`: count, mean, min, quartiles and max of the numeric columns (and the date range).

### Step 2

```python
s["disc"] = s.discount_rate.where(s.discount_rate <= 1, s.discount_rate / 100)
s["month"] = s.date.dt.month
s["net"] = s.quantity * s.unit_price * (1 - s.disc)
s["profit"] = s.net - s.quantity * s.unit_cost
s["margin"] = s.profit / s.net
s["diff"] = s.net_revenue - s.net
s[s["diff"].abs() > 0.01]
```

📘 **What each line does** (para vos, no se lee):

- `s["disc"] = ...where(...)`: the discount as a fraction. It keeps values up to 1 and divides the others by 100. `discount_rate` stays as it was, and the CSV file is never changed.
- `s["month"] = s.date.dt.month`: the month number (1–12).
- `s["net"] = ...`: recalculated net revenue = quantity × price × (1 − discount).
- `s["profit"] = ...`: recalculated gross profit = net revenue − quantity × cost.
- `s["margin"] = s.profit / s.net`: the margin as a share of net revenue.
- `s["diff"] = s.net_revenue - s.net`: recorded minus recalculated revenue.
- `s[s["diff"].abs() > 0.01]`: the sales that differ by more than a cent. `s["diff"]` uses brackets because `s.diff` is a pandas method.

### Step 3

```python
display(s.pivot_table("disc", "category", "month").round(2))
g = s.groupby(["category", "month"]).disc
q1, q3, n = g.transform("quantile", 0.25), g.transform("quantile", 0.75), g.transform("size")
s["iqr"] = (n >= 20) & (s.disc > q3 + 1.5 * (q3 - q1))
print((g.size() < 20).sum(), (n < 20).sum())
s[s.iqr]
```

📘 **What each line does** (para vos, no se lee):

- `display(s.pivot_table("disc", "category", "month").round(2))`: the average discount, with categories as rows and months as columns.
- `g = s.groupby(["category", "month"]).disc`: the discounts grouped by category and month.
- `q1, q3, n = g.transform(...)`: for every sale, the Q1, the Q3 and the size of **its own** group.
- `s["iqr"] = (n >= 20) & (...)`: True only if the group has 20 sales or more **and** the discount is above Q3 + 1.5 × IQR.
- `print(...)`: the number of groups below 20 and the number of sales not screened.
- `s[s.iqr]`: the outliers.

### Step 4

```python
v = s[s.promotion_id.notna()].merge(p, how="left")
v["id_ok"] = v.max_discount.notna()
v["cat_ok"] = v.category == v.applicable_category
v["date_ok"] = v.date.between(v.start_date, v.end_date)
v["max_ok"] = v.disc <= v.max_discount
v["plan_ok"] = (v.disc - v.planned_discount).abs().round(4) <= 0.05
c = ["id_ok", "cat_ok", "date_ok", "max_ok", "plan_ok"]
bad = v[v[c].all(axis=1) == False]
bad[["promotion_id", "category", "disc", "iqr"] + c]
```

📘 **What each line does** (para vos, no se lee):

- `v = s[s.promotion_id.notna()].merge(p, how="left")`: the 188 sales with a promotion ID, joined with the calendar on `promotion_id` (the only shared column). `left` keeps unknown IDs.
- `id_ok`: the ID exists (calendar data was found).
- `cat_ok`: the category matches the campaign's.
- `date_ok`: the date is inside the campaign, both ends included.
- `max_ok`: the discount is at or below the approved maximum.
- `plan_ok`: within 5 percentage points of the planned discount. `round(4)` avoids decimal noise.
- `c = [...]`: the five check names.
- `bad = v[v[c].all(axis=1) == False]`: the sales that fail at least one check.
- `bad[[...] + c]`: the visible table of inconsistent sales.

### Step 5

```python
ok = v[v.id_ok & v.cat_ok & v.date_ok].transaction_id
s["valid"] = s.transaction_id.isin(ok)
s["over30"] = (s.disc > 0.3) & (s.valid == False)
s["low"] = s.margin < 0.15
print(s.low.sum(), s[s.low].valid.sum())
s[s.over30]
```

📘 **What each line does** (para vos, no se lee):

- `ok = ...`: the IDs of the sales with a valid promotion (the ID exists, the category matches, the date is inside).
- `s["valid"] = ...isin(ok)`: True if the sale has a valid promotion.
- `s["over30"] = ...`: discount above 30% without a valid promotion. Its own column, separate from the calendar checks.
- `s["low"] = s.margin < 0.15`: margin below 15%, on every sale.
- `print(...)`: the total low-margin sales, and how many of them had a valid promotion.
- `s[s.over30]`: the over-30% sales. The `iqr` column shows whether IQR caught them.

### Step 6

```python
def impact(by):
    t = s.groupby(by).agg(n=("net", "size"), sales=("net", "sum"), profit=("profit", "sum"))
    t["margin"] = t.profit / t.sales
    return t.round(2)
display(impact("valid"))
display(impact(["category", "valid"]))
impact(s.promotion_id.fillna("None"))
```

📘 **What each line does** (para vos, no se lee):

- `def impact(by):`: a reusable function. It groups the sales by `by` and returns:
  - `n`: the number of transactions;
  - `sales`: net revenue;
  - `profit`: gross profit;
  - `margin`: profit ÷ sales, a weighted margin.
- `display(impact("valid"))`: with a valid promotion (True) vs without (False).
- `display(impact(["category", "valid"]))`: the same, inside each category.
- `impact(s.promotion_id.fillna("None"))`: one row per promotion ID as recorded.

Al tipear el `def`, Colab indenta solo las dos líneas siguientes. Después del `return`, apretá **Enter** y **Delete** una vez para volver al margen.

### Step 7

```python
k = ["net_revenue", "net", "diff"]
r = s.groupby("category")[k].sum()
r.loc["Sum"] = r.sum()
r.loc["Total"] = s[k].sum()
r.round(2)
```

📘 **What each line does** (para vos, no se lee):

- `k = [...]`: recorded revenue, recalculated revenue and their difference.
- `r = s.groupby("category")[k].sum()`: the totals of each category.
- `r.loc["Sum"] = r.sum()`: a row with the sum of the six categories.
- `r.loc["Total"] = s[k].sum()`: a row with the total calculated over all sales.
- `r.round(2)`: shows the table. "Sum" and "Total" must be equal.

### Step 8

```python
s["promo_issue"] = s.transaction_id.isin(bad.transaction_id)
s["data_issue"] = (s["diff"].abs() > 0.01) | (s.discount_rate > 1)
f = ["iqr", "data_issue", "promo_issue", "over30", "low"]
s[s[f].any(axis=1)].to_csv("flagged_transactions.csv", index=False)
res = s[f].sum()
res["flagged"] = s[f].any(axis=1).sum()
res.to_csv("summary_results.csv")
res
```

📘 **What each line does** (para vos, no se lee):

- `promo_issue`: the sale failed a calendar check.
- `data_issue`: the revenue doesn't match, or the discount was stored as a percentage (`|` means "or").
- `f = [...]`: the five review reasons.
- `s[s[f].any(axis=1)].to_csv(...)`: exports the sales with at least one reason.
- `res = s[f].sum()`: the count for each reason.
- `res["flagged"] = ...`: the number of distinct flagged sales.
- `res.to_csv("summary_results.csv")`: exports the summary of results.
- `res`: shows it.

### Celda de texto (se tipea en vivo)

```markdown
## Summary
- Data: 8 discounts saved as percentages, fixed in disc. 6 sales without the discount (+$58.35), kept as recorded.
- IQR: 15 outliers. 11 small Toys groups (135 sales) not checked.
- Promotions: 17 of 188 fail the calendar checks.
- Rules: 10 over 30% without a valid promotion. 72 under the 15% margin.
- Impact: valid promotions keep a 17% margin vs 33%. PRM-07 kept 3%.
- Final notes: synthetic files generated with AI before recording. Originals unchanged.
```

---

## 5. Verificación de requisitos

| Requisito | Dónde | Qué se ve |
| --------- | ----- | --------- |
| A. Carga de los dos CSV | Step 1 | Dos `read_csv` |
| A. Dimensiones, columnas, tipos y faltantes | Step 1 | `info()` de los dos: 2.200 × 10 y 8 × 7; `promotion_id` con 188 no nulos |
| A. Preparación de columnas | Step 2 | `disc`, `month`, `net`, `profit`, `margin`, `diff` |
| B. Por categoría y mes | Step 3 | Pivot 6 × 12 y `groupby(["category", "month"])` |
| B. IQR | Step 3 | `s["iqr"]`: 15 outliers |
| B. Grupos con menos de 20 sin evaluar | Step 3 | `n >= 20` y el print `11 135` |
| C. ID / categoría / fecha / máximo | Step 4 | `id_ok`, `cat_ok`, `date_ok`, `max_ok` |
| C. Más de 5 puntos del plan | Step 4 | `plan_ok` |
| C. Tabla visible de inconsistencias | Step 4 | `bad`: 17 filas |
| D. Más de 30% sin promoción | Step 5 | `over30`: 10 filas |
| D. Margen menor a 15% | Step 5 | `low`: 72 (35 con promoción válida) |
| D. Separados del calendario | Step 5 | Columnas propias, aplicadas a las 2.200 ventas |
| E. Con promoción vs sin promoción | Step 6 | `impact("valid")` |
| E. Por categoría | Step 6 | `impact(["category", "valid"])` |
| E. Por promoción | Step 6 | `impact(promotion_id)` |
| E. Transacciones, ventas y gross profit | Step 6 | `n`, `sales`, `profit` (+ `margin`) |
| E. Sin afirmaciones de más | Narración del Step 6 | "Association, not proof". El *loss leader* queda como pregunta. |
| F. Categorías vs total general | Step 7 | Filas `Sum` y `Total` iguales |
| F. Mostrar diferencias | Step 7 | Columna `diff` por categoría: 58,39 = 58,35 + 0,04 de redondeo |
| G. Exportar las transacciones marcadas | Step 8 | `flagged_transactions.csv` (104) |
| G. Exportar el resumen | Step 8 | `summary_results.csv` |
| G. Conclusión en el notebook | Celda de texto | Tipeada en vivo |
| Declaración de IA | Celda de texto + Studio | "generated with AI before recording" |

---

## 6. Guion de grabación

**Ciclo de cada celda:** clic en **+ Code** → tipear con ⌨️ → **Run** → señalar → 🟢. No hay frase previa para explicar la celda: la explicación va **mientras tipeás**. Entre una frase 🖱️ y la siguiente, el mouse **no se mueve** (ver "La regla del mouse").

### A. 0:00–1:30 — Apertura

Con la **descripción de la tarea** en pantalla, en menos de 20 segundos:

> 🟢 I will be beginning my task soon. I'll analyze discount patterns in a year of sales data with Python and pandas in Google Colab: find unusually high discounts, check them against the promotion calendar, and measure their impact on gross margin.

> 🖱️ I'm clicking the yellow minimize button at the top left of this Firefox window, to put the task description away.

> 🖱️ I'm clicking the Firefox icon in the Dock, on the right side of the screen, and choosing the second window in the list, my empty Colab notebook.

> 🖱️ I'm clicking the Files icon, the folder in the left sidebar, to show the input files.

> 🟢 I uploaded both CSV files before recording: sales_transactions, with 2,200 sales, and promotion_calendar, with the authorized campaigns. They're synthetic, generated with AI, and I won't modify them.

> 🟢 My rules are set before I look at the data: IQR only in groups with at least 20 sales, 5 points of tolerance around the planned discount, a 30% limit without a valid promotion, and a 15% margin floor.

> 🖱️ I'm clicking the Files icon again to close the panel, and clicking inside the empty code cell at the top.

### B. 1:30–4:00 — Step 1: carga e inspección (191 caracteres)

> 🟢 Step one: loading and inspection.

> ⌨️ *(import and the two read_csv lines)* I'm typing the import and the two read_csv lines at the top of the first cell. I import pandas and read both files, with the date columns as real dates, because later I compare them with the campaign dates. I use short names: s for sales and p for promotions.

> ⌨️ *(s.info, p.info, s.describe)* I'm typing info for both tables and describe, below the read_csv lines. info shows the size, columns, types, and missing values of each file, and describe shows the numeric ranges.

> 🖱️ I'm clicking the Run cell button, the play icon on the left of the cell, to load the data.

> 🖱️ I'm moving the mouse down the Non-Null Count column of the first info output.

> 🟢 2,200 rows and 10 columns. Only promotion_id has missing values, 188 filled, which is expected: an empty ID means no promotion. The calendar has 8 rows and no missing values.

> 🖱️ I'm scrolling down to the describe table and pointing at the max of discount_rate.

> 🟢 The third quartile of the discount is 0.10, but the maximum is 26. As a fraction, that's 2,600%, so some discounts look like percentages. I'll check that with the revenue in the next step.

**Resultado esperado:** `RangeIndex: 2200 entries`, `promotion_id 188 non-null`. Calendario: `8 entries`, todo non-null. `describe`: `date` de 2025-01-01 a 2025-12-31, `discount_rate` 75% 0,10 y max 26,0.

### C. 4:00–7:30 — Step 2: preparación y recálculo (291 caracteres)

> 🖱️ I'm scrolling down and clicking the plus Code button at the top left, to add the second cell.

> 🟢 Step two: preparing the columns and recalculating the money.

> ⌨️ *(disc)* I'm typing the disc line, the first line of the second cell. disc is the discount as a fraction: values up to 1 stay, larger ones are divided by 100. The original column stays as it is.

> ⌨️ *(month)* I'm typing the month line, below it. The month, for the analysis by period.

> ⌨️ *(net, profit, margin)* I'm typing the net, profit, and margin lines, in the middle of the cell. Then I recalculate net revenue, gross profit, and margin from quantity, price, cost, and discount.

> ⌨️ *(diff and the last line)* I'm typing the diff line and the filter, at the bottom of the cell. diff compares the recorded revenue with mine, and I show the sales that differ by more than one cent.

> 🖱️ I'm clicking the Run cell button on the left of the second cell.

> 🖱️ I'm pointing at the six rows of the result, below the cell.

> 🟢 Only six sales out of 2,200 don't match. That also proves my conversion: the eight discounts I divided by 100 now match the recorded revenue to the cent, so they really were percentages.

> 🖱️ I'm moving the mouse between the net_revenue and net columns of these six rows.

> 🟢 In these six, the recorded revenue ignores a discount of 5 to 14%. I can't tell whether the revenue or the discount is wrong, so I keep them as recorded and report them.

**Resultado esperado:** 6 filas: `T00722`, `T01588`, `T01684`, `T01737`, `T01929`, `T02155`. En todas, `net_revenue` es mayor que `net` (por ejemplo, `T00722`: 90,42 contra 84,99).

### D. 7:30–11:30 — Step 3: patrones e IQR (300 caracteres)

> 🖱️ I'm scrolling down and clicking the plus Code button at the top left, to add the third cell.

> 🟢 Step three: patterns by category and month, and the IQR screen.

> ⌨️ *(display pivot_table)* I'm typing the pivot table line at the top of the third cell. First, the average discount for each category and month.

> ⌨️ *(g and the transform line)* I'm typing the groupby and transform lines below it. Then I group by category and month, and give each sale the Q1, Q3, and size of its own group, because 25% is normal on Black Friday and unusual in February.

> ⌨️ *(s["iqr"])* I'm typing the iqr flag line, in the middle of the cell. A sale is an outlier only if its group has at least 20 sales and the discount is above Q3 plus 1.5 times the IQR.

> ⌨️ *(print and s[s.iqr])* I'm typing the print and the outlier filter at the bottom of the cell. I print how many groups and sales are too small to screen, and show the outliers.

> 🖱️ I'm clicking the Run cell button on the left of the third cell.

> 🖱️ I'm moving the mouse across the pivot table, from Beauty to Toys.

> 🟢 Most months average 3 to 6%. The peaks match the campaigns: Clothing in January, Beauty in May, Sports in June, Electronics in November, Toys in December.

> 🖱️ I'm pointing at the printed line, 11 and 135.

> 🟢 Eleven groups, all Toys months, have fewer than 20 sales: 135 sales that IQR doesn't screen, because ten values don't give reliable quartiles. The 30% and 15% rules will still check them.

> 🖱️ I'm scrolling right in the outlier table to the promotion_id column.

> 🟢 15 outliers. Three are PRM-99, which I'll check next, and three are December Black Friday sales, an authorized campaign. IQR tells me what's unusual, not what's wrong.

**Resultado esperado:** `11 135`. 15 filas: 3 × PRM-99 (Home & Kitchen, julio), 3 × PRM-07 (Electronics, diciembre), 2 × PRM-07 en Beauty y Home & Kitchen (noviembre) y 7 sin promoción.

### E. 11:30–16:00 — Step 4: validación de promociones (435 caracteres)

> 🖱️ I'm scrolling down and clicking the plus Code button at the top left, to add the fourth cell.

> 🟢 Step four: promotion validation.

> ⌨️ *(v = ... merge)* I'm typing the merge line at the top of the fourth cell. I take every sale with a promotion ID and join it with the calendar. Left keeps the IDs that don't exist.

> ⌨️ *(id_ok, cat_ok)* I'm typing the ID and category checks below it. First check: the ID exists. Second: the category matches the campaign.

> ⌨️ *(date_ok, max_ok)* I'm typing the date and maximum checks. Third: the date is inside the campaign. Fourth: the discount is within the approved maximum.

> ⌨️ *(plan_ok)* I'm typing the plan check, the last of the five. Fifth: it's within 5 percentage points of the planned discount.

> ⌨️ *(c, bad, last line)* I'm typing the check list, the bad filter, and the table at the bottom of the cell. Then I keep the sales that fail at least one check, and show the five checks side by side.

> 🖱️ I'm clicking the Run cell button on the left of the fourth cell.

> 🖱️ I'm pointing at the row count of the table, 17.

> 🟢 17 of 188 promotion sales fail at least one check.

> 🖱️ I'm pointing at the four PRM-01 rows at the top, where only plan_ok is False.

> 🟢 PRM-01 plans 30%: these got 37, 38, and 22%. They're inside the maximum, so they're deviations to explain, not limit violations.

> 🖱️ I'm pointing at the PRM-02 rows, with date_ok False.

> 🟢 PRM-02 ended on March 31st, and these are from April.

> 🖱️ I'm pointing at the PRM-05 rows, with max_ok False.

> 🟢 32 and 33% against a 25% maximum: clear violations.

> 🖱️ I'm pointing at the PRM-99 and PRM-07 rows at the bottom.

> 🟢 PRM-99 doesn't exist, so every check fails. And PRM-07, Black Friday Electronics, was used in Beauty, Toys, and Home & Kitchen.

> 🖱️ I'm moving the mouse down the iqr column.

> 🟢 Only 5 of the 17 were IQR outliers. Most promotion problems look statistically normal, so this check is necessary.

**Resultado esperado:** 17 filas. PRM-01 (4), PRM-02 (4), PRM-05 (3), PRM-99 (3) y PRM-07 (3). `iqr` True en 5.

### F. 16:00–19:00 — Step 5: reglas independientes (217 caracteres)

> 🖱️ I'm scrolling down and clicking the plus Code button at the top left, to add the fifth cell.

> 🟢 Step five: two business rules, separate from the calendar check.

> ⌨️ *(ok, valid)* I'm typing the ok and valid lines at the top of the fifth cell. A promotion is valid if the ID exists, the category matches, and the date is inside the campaign.

> ⌨️ *(over30, low)* I'm typing the over30 and low lines below them. Then two flags on all 2,200 sales: a discount above 30% without a valid promotion, and a margin below 15%.

> ⌨️ *(print, last line)* I'm typing the print and the over30 filter at the bottom of the cell. I print the low-margin count, and how many of those had a valid promotion, and I show the over-30% sales.

> 🖱️ I'm clicking the Run cell button on the left of the fifth cell.

> 🖱️ I'm pointing at the printed line, 72 and 35.

> 🟢 72 sales are below the 15% floor, and 35 of them were inside a valid promotion. An authorized promotion doesn't make a sale profitable.

> 🖱️ I'm pointing at the ten rows of the over-30% table.

> 🟢 Ten discounts above 30% without a valid promotion: seven with no promotion at all, up to 55%, and the three PRM-99 sales.

> 🖱️ I'm scrolling right to the iqr column, and pointing at the three False values.

> 🟢 IQR missed three of them: two in the small Toys groups, and one in Clothing in January, where the campaign raised the limit. That's why this rule must be independent.

**Resultado esperado:** `72 35`. 10 filas. `iqr` False en `T00123` (Clothing, 0,36), `T00649` (Toys, 0,40) y `T01356` (Toys, 0,55).

### G. 19:00–23:00 — Step 6: impacto en el margen (263 caracteres)

> 🖱️ I'm scrolling down and clicking the plus Code button at the top left, to add the sixth cell.

> 🟢 Step six: the impact on gross margin. I'll write a small function, because I need the same table three times.

> ⌨️ *(def and the agg line)* I'm typing the impact function at the top of the sixth cell. impact groups the sales and counts the transactions, adds up sales and gross profit.

> ⌨️ *(margin and return)* I'm typing the margin and return lines, indented inside the function. The margin is total profit over total sales, so bigger sales weigh more.

> ⌨️ *(the three calls)* I'm pressing Delete to go back to the left margin, and typing the three calls at the bottom of the cell. I call it three times: with or without a valid promotion, by category, and by promotion ID.

> 🖱️ I'm clicking the Run cell button on the left of the sixth cell.

> 🖱️ I'm pointing at the first table, False and True.

> 🟢 Sales with a valid promotion keep a 17% margin, against 33% without one. That's an association, not proof of cause: I don't have a control group.

> 🖱️ I'm scrolling down to the two Electronics rows of the category table.

> 🟢 Every category loses margin with promotions, and Electronics ends lowest: from 24% to 10%.

> 🖱️ I'm scrolling down to the last table and pointing at the PRM-07 row.

> 🟢 PRM-07 brought about 28,000 dollars in sales and only 809 dollars of profit: a 3% margin. PRM-06, the other Electronics campaign, kept 19%. It might be a deliberate loss leader, but I can't see repeat customers, so that's a question for the business, not a conclusion.

**Resultado esperado:** False 2022 · 417.860,60 · 139.867,11 · 0,33. True 178 · 71.788,20 · 12.429,46 · 0,17. Electronics: False 0,24, True 0,10. PRM-07: 36 · 28.172,10 · 808,87 · 0,03. PRM-06: 0,19.

### H. 23:00–25:00 — Step 7: reconciliación (127 caracteres)

> 🖱️ I'm scrolling down and clicking the plus Code button at the top left, to add the seventh cell.

> 🟢 Step seven: reconciliation.

> ⌨️ *(k, r)* I'm typing the column list and the category totals at the top of the seventh cell. I add up recorded revenue, recalculated revenue, and the difference, for each category.

> ⌨️ *(Sum, Total, round)* I'm typing the Sum and Total rows below them. Then one row with the sum of the categories, and one with the overall total, to check that no sale was lost or counted twice.

> 🖱️ I'm clicking the Run cell button on the left of the seventh cell.

> 🖱️ I'm pointing at the Sum and Total rows at the bottom.

> 🟢 Both rows are identical, so the categories reconcile with the overall total.

> 🖱️ I'm pointing at the diff column.

> 🟢 The total difference is 58.39 dollars: 58.35 from the six sales without the discount, and 4 cents of rounding. It's explained, and I didn't change any source value to hide it.

**Resultado esperado:** `Sum` = `Total`: 489.707,18 · 489.648,79 · 58,39.

### I. 25:00–27:30 — Step 8: entregables (341 caracteres)

> 🖱️ I'm scrolling down and clicking the plus Code button at the top left, to add the eighth cell.

> 🟢 Step eight: the deliverables.

> ⌨️ *(promo_issue, data_issue)* I'm typing the promo_issue and data_issue flags at the top of the eighth cell. Two last flags: the sale failed a calendar check, or it has a data issue, a mismatch or a percentage value.

> ⌨️ *(f and to_csv)* I'm typing the flag list and the first export below them. I export every sale with at least one of the five reasons, each reason as its own column, so the team can filter.

> ⌨️ *(res lines)* I'm typing the summary lines and the second export at the bottom of the cell. And I export a summary with the count for each reason and the number of flagged sales.

> 🖱️ I'm clicking the Run cell button on the left of the eighth cell.

> 🖱️ I'm moving the mouse down the summary under the cell.

> 🟢 15 IQR outliers, 14 data issues, 17 promotion issues, 10 above 30%, 72 low margins: 104 distinct sales to review.

> 🖱️ I'm clicking the Files icon in the left sidebar, and pointing at flagged_transactions and summary_results.

Si no aparecen: 🖱️ *"I'm clicking the refresh icon at the top of the Files panel, to update the list."*

> 🖱️ I'm clicking the Files icon again to close the panel.

**Resultado esperado:** iqr 15, data_issue 14, promo_issue 17, over30 10, low 72, flagged 104.

### J. 27:30–31:00 — Resumen (465 caracteres)

> 🖱️ I'm clicking the plus Text button at the top left, next to plus Code, to add a text cell at the end.

> ⌨️ *(Data)* I'm typing the Summary title and the Data line in the new text cell. First, data issues: the eight percentages I fixed, and the six mismatches I kept.

> ⌨️ *(IQR)* I'm typing the IQR line below it. The statistical anomalies, with the small Toys groups excluded.

> ⌨️ *(Promotions, Rules)* I'm typing the Promotions and Rules lines. The policy violations: the calendar checks and the two business rules.

> ⌨️ *(Impact)* I'm typing the Impact line. The margin impact, with PRM-07 as the main finding.

> ⌨️ *(Final notes)* I'm typing the Final notes line at the bottom of the text cell. And the final note: the files are synthetic, generated with AI before recording.

> 🖱️ I'm clicking the empty area below the text cell, to close the editor and show the formatted summary.

> 🖱️ I'm pressing Command + S to save the notebook in Drive.

### K. 31:00–33:00 — Epílogo

> 🖱️ I'm scrolling up slowly through the notebook, in the center of the screen.

> 🟢 My approach was to check the data before trusting it, then use statistics to see what's unusual and business rules to see what's wrong, keeping them independent.

> 🟢 The main challenge was deciding what not to change. The percentages had evidence, so I converted them. The six mismatches didn't, so I kept them and explained the 58 dollars instead of forcing the totals to match.

> 🟢 Another challenge was the small Toys groups: IQR isn't reliable there, and the 30% rule caught two discounts IQR could never see.

> 🟢 The most important finding is PRM-07: an authorized campaign that left about 800 dollars of profit on 28,000 dollars of sales. My recommendations are to review the 104 flagged sales, block invalid promotions at checkout, and review the PRM-07 rate. The limits are one year of synthetic data and no customer information. Thanks for watching!

---

## 7. Cronograma

Estimado, con dos velocidades: **150 caracteres por minuto** de tipeo (después de practicar) y **130 palabras por minuto** de narración. Las frases ⌨️ se dicen **mientras** tipeás, así que no suman tiempo aparte.

| Sección | Tiempo | Duración | Tipeo | Narración fuera del tipeo |
| ------- | ------ | -------- | ----- | ------------------------- |
| A. Apertura | 0:00–1:30 | 1:30 | — | ~170 palabras |
| B. Step 1 | 1:30–4:00 | 2:30 | 191 (~1:20) | ~120 |
| C. Step 2 | 4:00–7:30 | 3:30 | 291 (~2:00) | ~130 |
| D. Step 3 | 7:30–11:30 | 4:00 | 300 (~2:00) | ~170 |
| E. Step 4 | 11:30–16:00 | 4:30 | 435 (~2:55) | ~190 |
| F. Step 5 | 16:00–19:00 | 3:00 | 217 (~1:30) | ~150 |
| G. Step 6 | 19:00–23:00 | 4:00 | 263 (~1:45) | ~160 |
| H. Step 7 | 23:00–25:00 | 2:00 | 127 (~0:50) | ~100 |
| I. Step 8 | 25:00–27:30 | 2:30 | 341 (~2:15) | ~90 |
| J. Resumen | 27:30–31:00 | 3:30 | 465 (~3:05) | ~30 |
| K. Epílogo | 31:00–33:00 | 2:00 | — | ~200 |
| **Total** | | **~33 min** | ~2.630 (~17,5 min) | |

**Si tipeás a 120 caracteres por minuto**, el total sube a unos **37 minutos**. Sigue dentro del rango.

**El orden de prioridad si vas atrasado:** nunca saltees el Step 8, el resumen ni el guardado. Lo que se puede acortar es la interpretación del pivot (D) y de la tabla por categoría (G).

---

## 8. Checklist final

### Preparación (sin grabar)

- [ ] Practicá **tipeando las 8 celdas y el resumen** en un notebook de prueba, con cronómetro, al menos dos veces. Si tenés dudas, `discount_analysis.ipynb` es la referencia.
- [ ] Practicá el **autocompletado de Colab**: escribí `s.disc` y apretá **Tab** para completar `discount_rate`. Sirve para `transaction_id`, `promotion_id`, `applicable_category`, `planned_discount`, `max_discount` y `net_revenue`. Mientras tanto decí: *"I'm pressing Tab to autocomplete the column name."*
- [ ] Colab cierra solo comillas y paréntesis. Si tipeás el de cierre, lo pisa (no lo duplica). Practicalo para que no te sorprenda.
- [ ] Creá el notebook vacío **discount_analysis** (**File → New notebook in Drive**), con la celda vacía que Colab crea sola.
- [ ] En el panel **Files** de ese notebook, subí `sales_transactions.csv` y `promotion_calendar.csv` desde el Escritorio. Comprobá que estén solo esos dos.
- [ ] **Tools → Settings → AI assistance**: ocultá las funciones de IA, incluidas las sugerencias de código. No uses IA durante la grabación.
- [ ] Zoom (`Cmd + +`). Ventana maximizada.
- [ ] En Firefox, ventana 1 con la descripción de la tarea y ventana 2 con Colab, en la **segunda línea** de la lista del Dock.
- [ ] Grabá **enseguida** después de subir los CSV: si Colab desconecta el runtime, se borran.

### Durante la grabación

- [ ] Las celdas se ejecutan **en orden**, con el **botón Run**.
- [ ] Nunca más de 5 segundos en silencio: mientras tipeás, decí las frases ⌨️.
- [ ] No muestres Studio, Slack, Metadata.rtf, Insightful ni datos personales.
- [ ] No termines antes de: Step 8 ejecutado, los 2 archivos visibles en Files, el resumen tipeado, **Cmd + S** y el epílogo.

### Después de grabar

- [ ] Detené TaskRecorder.
- [ ] Descargá: **File → Download → Download .ipynb**, y los 2 CSV exportados (en **Files**, los tres puntos → **Download**).
- [ ] **Run full AutoQC**: What + Where tiene que pasar el **70%**. Revisá el porcentaje de tipeo (ver "Pendientes").
- [ ] **Deliverables.zip** con el `.ipynb`, `flagged_transactions.csv`, `summary_results.csv` y los **dos CSV originales**, sin modificar.
- [ ] En Studio, marcá la opción de archivos generados con IA.
- [ ] Subí por separado el **MP4**, el **ZIP de TaskRecorder**, **Deliverables.zip** y **Metadata.rtf**.

---

## Si algo sale mal

Siempre decí **qué** corregís y **en qué celda**.

| Error | Qué pasa | Qué decís y hacés |
| ----- | -------- | ----------------- |
| `AttributeError` o `KeyError` | Un nombre de columna mal escrito | 🖱️ *"There's an error in the fourth cell: I typed applicable_categry. I'm fixing the name and running it again."* |
| Error en `s.diff` | Escribiste `s.diff` en vez de `s["diff"]` (`diff` también es un método de pandas) | 🖱️ *"diff is also a pandas method, so I need brackets here. I'm changing it to s, bracket, diff, and running again."* |
| `IndentationError` en el Step 6, o la celda no muestra nada | Las líneas del `def` quedaron sin sangría, o los `display` quedaron con sangría (dentro de la función) | 🖱️ *"The indentation is wrong in the sixth cell. I'm fixing it and running again."* |
| `NameError` | Una celda anterior no se ejecutó | 🖱️ *"An earlier cell didn't run. I'm opening the Runtime menu and choosing Run before."* |
| `FileNotFoundError` | El runtime se reinició y borró los CSV | 🖱️ *"The files were deleted when the runtime restarted. I'm uploading both CSV files again in the Files panel and running the first cell."* |
| Una celda corrida dos veces | Columnas recalculadas sobre datos ya cambiados | En este código no pasa: cada columna se recalcula igual. Si algo da distinto: **Runtime → Run before**. |

---

## Archivos de la carpeta

```
k3a13c10-discount-pattern-analysis/
├── README.md                  ← este guion
├── sales_transactions.csv     ← entrada 1 (no se modifica)
├── promotion_calendar.csv     ← entrada 2 (no se modifica)
└── discount_analysis.ipynb    ← notebook de referencia para practicar (no se usa en la grabación)
```
