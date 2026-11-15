# oyi436dd — Customer Data Reconstruction & Analytics

Guion **optimizado** para grabar la tarea **oyi436dd** (Data Science & Analytics). En **Google Colab**, con **pandas, NumPy, Matplotlib y Seaborn**, trabajás con tres CSV sintéticos e imperfectos de una tienda online ficticia:

- perfilás los datos;
- investigás las anomalías antes de tocar nada;
- corregís solo lo que tiene evidencia;
- armás un dataset analítico confiable;
- analizás el negocio y validás los totales;
- entregás el dataset limpio, el reporte de excepciones, los gráficos y las conclusiones.

Se graba en **Firefox**, en **una sola toma**. El código y las conclusiones se **tipean y se explican en vivo**, y los CSV se suben **antes** de grabar.

| | Guion anterior | Ahora |
| - | -------------- | ----- |
| Celdas de código | 16 | **9** |
| Caracteres de código | ~4.720 | **~3.310** |
| Caracteres de las conclusiones | ~930 | **~530** |
| Palabras de narración | ~4.300 | **~2.300** (unas 780 se dicen mientras tipeás) |
| Duración estimada | **~85 min** | **~40–46 min** |

**Cómo leer este guion:**

- 🖱️ = lo decís **mientras hacés** la acción: **qué** hacés, **dónde** está y **por qué**. AutoQC cuenta estas frases: **no te saltees ninguna**.
- ⌨️ = lo decís **mientras tipeás** la línea indicada entre paréntesis. Tiene dos partes y se dicen las dos: **qué tipeás y dónde** (*"I'm typing … at the top of the third cell."*), que es lo que cuenta AutoQC, y **para qué sirve**.
- 🟢 = la interpretación de un resultado, o la transición.
- 📘 **What each line does** (sección 4): la explicación de cada línea, en inglés, por si tenés dudas. **No se lee**.
- **Resultado esperado**: los números reales que tienen que aparecer. Son para vos.
- Si usás un atajo de teclado, decí la tecla en voz alta: *"I'm pressing Command + S"*.

---

## Pendientes antes de grabar

| Tema | Situación | Qué hacer |
| ---- | --------- | --------- |
| **Duración: el prompt pide 15–30 minutos** | Con todo tipeado en vivo, la estimación da **40–46 minutos**. Solo el tipeo son 3.850 caracteres, unos 26 minutos a 150 caracteres por minuto. Así no se llega a 30 sin sacar contenido. El máximo general de la plataforma es 50:59, así que sigue siendo una grabación válida en ese sentido. | Confirmá si el tope de 30 minutos del prompt es **obligatorio**. Si lo es, avisame y saco lo que el prompt no exija. Candidatos: el top 5 de productos, el desglose de junio por canal y la línea de categorías y canales del Step 1. Eso ahorra unos 2–3 minutos. Para llegar a 30 hay que recortar más, y para eso necesito saber qué es obligatorio. |
| **Porcentaje de tipeo** | Cerca del **60%** de la grabación. Bajar al 25–30% es imposible tipeando todo en vivo. | Igual que en k3a13c10: confirmá el límite en las guías. Usá el **autocompletado con Tab** para los nombres largos. |
| **Origen de los CSV** | Los tres CSV los generé yo, Claude, con un script de Python. "Generated with AI" es **cierto**; "Gemini" **no**. | Las conclusiones dicen *"generated with AI before recording"*. Marcá en Studio la opción de archivos generados con IA. |
| **Versión de pandas** | Lo probé con pandas 3.1. Colab suele traer la 2.x. | Si ves `object` en vez de `str`, o los arreglos de `unique()` se ven distintos, es lo mismo: decí lo que veas. |

---

## La regla del mouse (leela antes de practicar)

Para el revisor, y para AutoQC, **cada movimiento del mouse es una acción**, y una acción sin frase cuenta como no explicada.

1. **El mouse solo se mueve cuando decís una frase 🖱️.** Si no estás diciendo una, la mano no toca el mouse.
2. **Mientras tipeás, soltá el mouse.** Las dos manos en el teclado.
3. **Al terminar una acción, dejá el cursor quieto en el margen derecho de Colab**, en la zona blanca. Nunca encima de botones.
4. **Primero decís la frase y después movés el mouse**, en un solo movimiento, directo.
5. **Si leés el guion, leelo con el mouse quieto.**
6. **Si hacés algo que no está en el guion**, usá una frase comodín de la tabla siguiente. Nunca lo hagas en silencio.

| Acción | Frase comodín |
| ------ | ------------- |
| Mover el mouse hacia el botón Run | *"I'm moving the mouse to the Run button, on the left of the cell."* |
| Scroll de más | *"I'm scrolling down a bit, to see the end of the output."* / *"I'm scrolling back up to the cell I'm working on."* |
| Scroll horizontal en una tabla | *"I'm scrolling right inside the table, to see the last columns."* |
| Clic para corregir | *"I'm clicking at the end of the line in the third cell, to fix a typo."* |
| Autocompletar | *"I'm pressing Tab to autocomplete the column name."* |
| Cerrar sugerencias de Colab | *"I'm pressing Escape to close the suggestion box."* |
| Esperar a que termine una celda | *"I'm waiting for the cell to finish; the spinner on the left shows it's running."* |
| Cerrar un aviso | *"I'm clicking Close on the notice at the bottom of the screen."* |
| Volver a una celda anterior | *"I'm scrolling up to the second cell, to check the anomaly table again."* |

---

## 1. Diagnóstico: por qué el guion anterior lleva unos 85 minutos

**Estos tiempos son estimaciones mías, no mediciones.** Los calculé con el mismo método que en k3a13c10, que para esa tarea coincidió con tus 75 minutos reales: **130 palabras por minuto** de narración y **120 caracteres por minuto** de tipeo.

| Origen del tiempo | Cantidad en el guion anterior | Tiempo estimado |
| ----------------- | ----------------------------- | --------------- |
| Tipear el código (16 celdas) | ~4.720 caracteres | **~39 min** |
| Tipear las conclusiones | ~930 caracteres | **~8 min** |
| Narración | ~4.100 palabras | **~32 min** |
| Navegación (17 ciclos de celda, subir archivos, 3 descargas, visor) | — | **~6–7 min** |
| **Total** | | **~85 min** |

Las causas son las mismas que en k3a13c10:

1. **El tipeo.** Nombres largos (`orders`, `items`, `products`, `clean`, `order_val`) repetidos decenas de veces, columnas escritas entre corchetes y comillas, y celdas de una sola línea que igual llevan su ciclo completo.
2. **Cada celda se explicaba tres veces:** antes, mientras se tipeaba y después.
3. **16 ciclos de celda**, cuando varias son pasos chicos (las celdas 3, 8, 10 y 12).
4. **Navegación que puede ir antes o después de grabar:** subir los tres CSV, las tres descargas y el visor de archivos.

---

## 2. Qué se reduce, se agrupa o se elimina

En la columna "Tiempo real probable" van mis **estimaciones** (no son mediciones), con las velocidades de la sección 1.

| Paso actual | En el guion | Real probable | Problema | Optimización |
| ----------- | ----------- | ------------- | -------- | ------------ |
| A. Apertura y subida | 2:00 | ~4 min | 386 palabras y la subida de 3 archivos | Los CSV se suben **antes**. ~170 palabras. |
| B. Celdas 1–2: carga y calidad | 3:30 | ~9 min | 586 caracteres y dos ciclos | **Step 1**: una celda de 380 caracteres, con nombres `o`, `i`, `p`. |
| C. Celdas 3–4: anomalías | 4:00 | ~9 min | 525 caracteres, dos ciclos y una explicación larga de `format="mixed"` | **Step 2**: una celda de 345 caracteres. Lo de `mixed` queda en una frase. |
| D. Celdas 5–8: transformación y join | 5:30 | **~20 min** | 1.726 caracteres, la parte más larga. La celda 8 solo mostraba los *mismatches*. | **Step 3** (771) y **Step 4** (490). Sale la celda 8: los 6 *mismatches* quedan en el reporte de excepciones. |
| E. Celdas 9–13: negocio y outliers | 6:00 | ~15 min | 960 caracteres en cinco ciclos | **Step 5** (494), que junta métricas, categorías, top 5, meses y junio, y **Step 6** (207), con los outliers. |
| F. Celda 14: gráficos | 1:30 | ~4 min | — | **Step 7**: 202 caracteres. |
| G. Celda 15: validación | 2:00 | ~5 min | 374 caracteres | **Step 8**: 233 caracteres. |
| H. Celda 16, conclusiones, descargas y visor | 3:00 | ~13 min | 930 caracteres de conclusiones, 3 descargas y el visor | **Step 9** (183) y conclusiones de 534 caracteres. Las descargas van **después** de grabar. |
| I. Epílogo | 3:00 | ~2,5 min | Largo | ~2 min. |

---

## 3. Notebook compacto

`sales_analysis.ipynb` es el **notebook de referencia** para practicar. **No se usa en la grabación**: ahí empezás con el notebook vacío y tipeás todo. Cada celda empieza con un comentario corto con la sección del prompt.

| Celda | Sección | Qué hace | Caracteres |
| ----- | ------- | -------- | ---------- |
| Step 1 | 1–3. Context, loading, quality | Lee los 3 CSV. Muestra tamaños, faltantes, duplicados, estados, canales, categorías y `describe`. | 380 |
| Step 2 | 4. Anomalies | Revisa el formato de las fechas y compara precios y cantidades contra el catálogo. | 345 |
| Step 3 | 5. Transformation | Saca duplicados, convierte fechas, normaliza canales y categorías, completa GUEST y hace 3 correcciones con su valor original y su etiqueta. | 771 |
| Step 4 | 5. Reconciliation | Une las tablas con `validate="m:1"`, marca 3 tipos de excepción y define `in_revenue`. | 490 |
| Step 5 | 6. Business analysis | Calcula ingreso, pedidos y ticket promedio. Muestra categorías, top 5 de productos, meses con variación y junio por canal. | 494 |
| Step 6 | 6. Outliers | Aplica IQR sobre log10 del valor de pedido, por canal. | 207 |
| Step 7 | 7. Visualizations | Dibuja la línea mensual (Matplotlib) y el box plot por canal (Seaborn). | 202 |
| Step 8 | 8. Validation | Compara el join ingenuo con las líneas, las filas de entrada con las de salida, las categorías con el ingreso y el total por estado. | 233 |
| Step 9 | 9. Deliverables | Exporta `clean_sales.csv` y `exceptions_report.csv`. | 183 |
| Texto | 9. Conclusions | Conclusiones y notas finales. | 534 |

---

## 4. Código completo, por celda

Probado con los tres CSV. Los nombres son cortos a propósito: `o` = orders, `i` = items, `p` = products, `oc` = clean orders, `c` = clean table, `r` = revenue lines, `ov` = order values.

### Step 1

```python
# 1-3. Context, loading, quality
import pandas as pd, numpy as np, matplotlib.pyplot as plt, seaborn as sns
o = pd.read_csv("orders.csv")
i = pd.read_csv("order_items.csv")
p = pd.read_csv("products.csv")
for t in [o, i, p]: print(t.shape, t.isna().sum().to_dict())
print(o.duplicated().sum(), o.status.value_counts().to_dict())
print(o.channel.unique(), p.category.unique())
i.describe()
```

📘 **What each line does** (para vos, no se lee):

- `# 1-3. ...`: a section comment. It doesn't run.
- `import ...`: the four libraries with their usual short names.
- The three `read_csv` lines: orders, order lines and catalog.
- `for t in [o, i, p]: print(...)`: for each table, (rows, columns) and the missing values per column.
- `print(o.duplicated().sum(), o.status.value_counts().to_dict())`: exact duplicate order rows, and orders per status.
- `print(o.channel.unique(), p.category.unique())`: every way the channel and the category are written.
- `i.describe()`: the statistics of the order lines (count, mean, min, quartiles, max).

### Step 2

```python
# 4. Anomalies
d = o.order_date[o.order_date.str.contains("/")]
print(len(d), (d.str[:2].astype(int) > 12).sum(), (d.str[3:5].astype(int) > 12).sum())
i = i.merge(p[["product_id", "list_price"]], how="left")
i["ratio"] = i.unit_price / i.list_price
i["implied"] = i.line_total / i.unit_price
i[(i.ratio > 2) | (i.quantity >= 50) | i.unit_price.isna()]
```

📘 **What each line does** (para vos, no se lee):

- `d = o.order_date[o.order_date.str.contains("/")]`: the dates written with slashes.
- `print(len(d), ...)`: how many there are, how many have a first number above 12, and how many have a second number above 12.
- `i = i.merge(p[["product_id", "list_price"]], how="left")`: adds the list price to each line. It joins on `product_id`, the only shared column. `left` keeps the products that aren't in the catalog.
- `i["ratio"]`: charged price ÷ list price (1 = full price, 0.85 = B2B, 100 = cents).
- `i["implied"]`: the quantity implied by the line total.
- The last line shows the suspicious lines: a price more than double, a quantity of 50 or more, or a missing price.

### Step 3

```python
# 5. Transformation
oc = o.drop_duplicates().copy()
oc["order_date"] = pd.to_datetime(oc.order_date, format="ISO8601", errors="coerce").fillna(pd.to_datetime(oc.order_date, format="%d/%m/%Y", errors="coerce"))
oc["channel"] = oc.channel.str.strip().str.title()
oc["customer_id"] = oc.customer_id.fillna("GUEST")
p["category"] = p.category.str.strip().str.title()
i["price_raw"], i["qty_raw"] = i.unit_price, i.quantity
i["fix"] = np.select([i.ratio > 50, i.unit_price.isna(), i.quantity == 999], ["cents", "no price", "999 qty"], "")
i.loc[i.fix == "cents", "unit_price"] /= 100
i["unit_price"] = i.unit_price.fillna(i.line_total / i.quantity)
i.loc[i.fix == "999 qty", "quantity"] = i.implied
print(oc.order_date.isna().sum(), oc.channel.unique(), p.category.unique())
i.fix.value_counts()
```

📘 **What each line does** (para vos, no se lee):

- `oc = o.drop_duplicates().copy()`: the orders without the exact duplicates. `o` stays raw for the validation.
- `oc["order_date"] = ...`: reads year-first dates first. The ones that fail become empty and are filled by reading them as day/month/year. This avoids `format="mixed", dayfirst=True`, which also flips the correct dates.
- `oc["channel"] = ...strip().str.title()`: removes spaces and unifies capitalization (`web`, `WEB ` → `Web`; `b2b` → `B2B`).
- `oc["customer_id"] = ...fillna("GUEST")`: a missing customer is a guest checkout.
- `p["category"] = ...`: the same normalization for the categories.
- `i["price_raw"], i["qty_raw"] = ...`: keeps the original values.
- `i["fix"] = np.select([...], [...], "")`: the label of the rule that applies, decided **before** changing anything.
- `i.loc[i.fix == "cents", "unit_price"] /= 100`: cents → dollars.
- `i["unit_price"] = ...fillna(line_total / quantity)`: a missing price, recovered from the total.
- `i.loc[i.fix == "999 qty", "quantity"] = i.implied`: 999 → the quantity confirmed by the total (1).
- `print(...)`: 0 unread dates, and the clean channels and categories.
- `i.fix.value_counts()`: how many lines each rule fixed.

### Step 4

```python
# 5. Reconciliation
c = i.drop(columns=["list_price", "ratio", "implied"]).merge(oc, how="left", validate="m:1")
c = c.merge(p[["product_id", "product_name", "category"]], how="left", validate="m:1")
c["category"] = c.category.fillna("Unknown")
c["exception"] = np.select([c.status.isna(), c.category == "Unknown", (c.quantity * c.unit_price - c.line_total).abs() > 0.01], ["no order", "unknown product", "total mismatch"], "")
c["in_revenue"] = c.status == "completed"
c.exception.value_counts()
```

📘 **What each line does** (para vos, no se lee):

- First line: removes the helper columns and joins the clean orders on `order_id`. `validate="m:1"` stops with an error if an order appears twice: the protection against double counting.
- Second line: adds the product name and category, with the same protection.
- `c["category"] = ...fillna("Unknown")`: products that aren't in the catalog.
- `c["exception"] = np.select(...)`: no status → the order doesn't exist; Unknown → product not in the catalog; quantity × price ≠ total → mismatch.
- `c["in_revenue"]`: only completed orders count as revenue.
- `c.exception.value_counts()`: lines per exception.

### Step 5

```python
# 6. Business analysis
r = c[c.in_revenue]
ov = r.groupby(["order_id", "channel"], as_index=False).line_total.sum()
print(r.line_total.sum().round(2), len(ov), ov.line_total.mean().round(2))
display(r.groupby("category").line_total.sum().sort_values())
display(r.groupby("product_name").line_total.sum().nlargest(5))
m = r.groupby(r.order_date.dt.to_period("M")).line_total.sum()
display(pd.concat([m, m.pct_change()], axis=1).round(2))
r[r.order_date.dt.month == 6].groupby("channel").line_total.sum()
```

📘 **What each line does** (para vos, no se lee):

- `r = c[c.in_revenue]`: only the revenue lines.
- `ov = ...`: one row per order, with its channel and its value.
- `print(...)`: total revenue, number of orders and average order value (per order, not per line).
- `display(... category ...)`: revenue by category, from lowest to highest.
- `display(... nlargest(5))`: the top 5 products.
- `m = ...to_period("M")...`: revenue by month.
- `display(pd.concat([m, m.pct_change()], axis=1))`: each month and its change from the previous one (0.50 = +50%).
- The last line: June revenue by channel.

### Step 6

```python
# 6. Outliers (IQR on log10)
lg = np.log10(ov.line_total)
q1, q3 = lg.quantile([0.25, 0.75])
lim = q3 + 1.5 * (q3 - q1)
ov["outlier"] = lg > lim
print(10 ** lim)
ov.groupby("channel").outlier.agg(["sum", "count"])
```

📘 **What each line does** (para vos, no se lee):

- `lg = np.log10(...)`: the logarithm of each order value, because the values are skewed to the right.
- `q1, q3 = ...`: quartiles on the log scale.
- `lim = q3 + 1.5 * (q3 - q1)`: the upper IQR limit.
- `ov["outlier"] = lg > lim`: True above the limit.
- `print(10 ** lim)`: the limit back in dollars.
- The last line: outliers (`sum`) out of total orders (`count`) per channel.

### Step 7

```python
# 7. Visualizations
fig, ax = plt.subplots(1, 2, figsize=(12, 4))
m.plot(ax=ax[0], marker="o", title="Monthly revenue")
sns.boxplot(data=ov, x="channel", y="line_total", log_scale=True, ax=ax[1])
plt.show()
```

📘 **What each line does** (para vos, no se lee):

- `plt.subplots(1, 2, ...)`: two charts side by side.
- `m.plot(...)`: the monthly revenue line, drawn with Matplotlib.
- `sns.boxplot(...)`: the Seaborn box plot of order value by channel, on a log scale.
- `plt.show()`: shows the figure without the `Axes(...)` text above it.

### Step 8

```python
# 8. Validation
print(i.merge(o, on="order_id").line_total.sum().round(2), i.line_total.sum().round(2))
print(len(i), len(c), r.groupby("category").line_total.sum().sum().round(2))
c.groupby(c.status.fillna("no order")).line_total.sum()
```

📘 **What each line does** (para vos, no se lee):

- First line: the total of a naive join with the raw orders (with duplicates) vs the sum of the raw line totals. The fixes never changed `line_total`.
- Second line: lines in vs lines out, and the sum of the categories (it must equal the revenue).
- Third line: the raw total split into completed, cancelled and without an order.

### Step 9

```python
# 9. Deliverables
c.to_csv("clean_sales.csv", index=False)
rep = c[(c.fix != "") | (c.exception != "") | (c.in_revenue == False)]
rep.to_csv("exceptions_report.csv", index=False)
len(rep)
```

📘 **What each line does** (para vos, no se lee):

- `c.to_csv(...)`: the clean dataset, with the original values, the `fix` label and the exceptions.
- `rep = ...`: the lines that were corrected, have an exception or are out of revenue.
- `rep.to_csv(...)`: the exception report.
- `len(rep)`: how many lines are in the report.

### Celda de texto (se tipea en vivo)

```markdown
## 9. Conclusions
- Data: removed 20 duplicate orders (a naive join adds $4,911.90), fixed 127 day-first dates and 26 lines with evidence. Unresolved: 6 total mismatches, 8 P025 lines, 5 lines without an order.
- Business: revenue $433,779.55 from 1,328 orders, AOV $326.64. Bedding leads. June +50% came from 3 B2B orders; November is the peak.
- Outliers: 36 orders, all B2B: a segment, not errors.
- Next: one date format, prices in dollars, add P025, report B2B apart.
- Final notes: synthetic files generated with AI before recording.
```

---

## 5. Verificación de requisitos

| Requisito | Dónde | Qué se ve |
| --------- | ----- | --------- |
| Contexto del negocio | Apertura y comentario del Step 1 | Brightside Home, 3 canales, el problema de Finanzas y la pregunta sobre junio |
| Carga e inspección | Step 1 | `(1420, 5)`, `(3061, 6)`, `(24, 5)` y los faltantes |
| Evaluación de calidad | Step 1 | 20 duplicados, 9 formas de escribir el canal, 10 de la categoría y los máximos sospechosos |
| Investigación antes de corregir | Step 2 | Fechas `127 83 0` y una tabla de 29 líneas |
| Transformación con evidencia y trazabilidad | Step 3 | `price_raw`, `qty_raw`, `fix` (12 / 10 / 4) |
| Conciliación sin doble conteo | Step 4 | `validate="m:1"` y las excepciones 8 / 6 / 5 |
| Análisis de negocio | Step 5 | Ingreso, pedidos, ticket promedio, categorías, top 5, meses y junio |
| Outliers con un método justificado | Step 6 | IQR sobre log10: 36 de 61 pedidos B2B |
| Matplotlib + Seaborn | Step 7 | La línea mensual y el box plot |
| Validación de totales | Step 8 | 465.624,75 vs 460.712,85; 3.061 = 3.061; desglose por estado |
| Dataset limpio | Step 9 | `clean_sales.csv` |
| Reporte de excepciones | Step 9 | `exceptions_report.csv` (211) |
| Conclusiones | Celda de texto | Tipeadas en vivo |
| Declaración de IA | Celda de texto + Studio | "generated with AI before recording" |

---

## 6. Guion de grabación

**Ciclo de cada celda:** **+ Code** → tipear con ⌨️ → **Run** → señalar → 🟢. Entre una frase 🖱️ y la siguiente, el mouse **no se mueve**.

### A. 0:00–1:30 — Apertura

Con la **descripción de la tarea** en pantalla, en menos de 20 segundos:

> 🟢 I will be beginning my task soon. I'll take an imperfect sales export from a fictional home-goods retailer, investigate its anomalies, rebuild a reliable dataset in Google Colab, and use it to answer business questions about revenue, products, and channels.

> 🖱️ I'm clicking the yellow minimize button at the top left of this Firefox window, to put the task description away.

> 🖱️ I'm clicking the Firefox icon in the Dock, on the right side of the screen, and choosing the second window in the list, my empty Colab notebook.

> 🖱️ I'm clicking the Files icon, the folder in the left sidebar, to show the input files.

> 🟢 I uploaded the three CSV files before recording: orders, order items, and the product catalog of Brightside Home, which sells through Web, App, and B2B. They're synthetic, generated with AI. Finance can't match the 2025 revenue from this export, and management wants to know what drives revenue and what happened in June.

> 🖱️ I'm clicking the Files icon again to close the panel, and clicking inside the empty code cell at the top.

### B. 1:30–5:00 — Step 1: carga y calidad (380 caracteres)

> ⌨️ *(comment and import)* I'm typing the section comment and the imports at the top of the first cell: pandas, NumPy, Matplotlib, and Seaborn.

> ⌨️ *(three read_csv)* I'm typing the three read_csv lines below them, with short names: o for orders, i for items, p for products.

> ⌨️ *(for loop)* I'm typing the loop in the middle of the cell. It prints the size and the missing values of each table.

> ⌨️ *(two prints)* I'm typing two prints below it: duplicate orders and statuses, and the channel and category labels.

> ⌨️ *(describe)* I'm typing describe on the last line, to see the ranges of the order lines.

> 🖱️ I'm clicking the Run cell button, the play icon on the left of the first cell, to load and profile the data.

> 🖱️ I'm pointing at the first three lines of the output.

> 🟢 1,420 orders, 3,061 order lines, and 24 products. 18 orders have no customer, and 10 lines have no price. I won't fill or delete them until I know what they mean.

> 🖱️ I'm pointing at the next line: 20 and the statuses.

> 🟢 20 exact duplicate orders. If I join the lines to them, their revenue counts twice. And 72 cancelled orders, which aren't revenue but I'll keep.

> 🖱️ I'm moving the mouse along the channel and category labels.

> 🟢 Three channels written nine ways, and six categories written ten ways. Same meaning, different text.

> 🖱️ I'm pointing at the max row of the describe table, at the bottom.

> 🟢 A quantity of 999, a price of 15,900 dollars, and a line total of 6,579. Some may be errors, some real large orders. I'll investigate before changing anything.

**Resultado esperado:** `(1420, 5)` con `customer_id 18`, `(3061, 6)` con `unit_price 10`, `(24, 5)` sin faltantes. `20 {'completed': 1348, 'cancelled': 72}`. 9 canales y 10 categorías. Máximos: quantity 999, unit_price 15.900, line_total 6.579.

### C. 5:00–9:00 — Step 2: anomalías (345 caracteres)

> 🖱️ I'm scrolling down and clicking the plus Code button at the top left, to add the second cell.

> ⌨️ *(comment, d)* I'm typing the section comment and the d line at the top of the second cell. It keeps the dates written with slashes.

> ⌨️ *(print)* I'm typing the print below it: how many there are, and whether the first or the second number is ever above 12, because a number above 12 can only be a day.

> ⌨️ *(merge)* I'm typing the merge in the middle of the cell. It adds the catalog list price to every line, and left keeps the products that aren't in the catalog.

> ⌨️ *(ratio, implied)* I'm typing ratio and implied: the charged price over the list price, and the quantity implied by the line total.

> ⌨️ *(filter)* I'm typing the filter on the last line: prices above double, quantities of 50 or more, or missing prices.

> 🖱️ I'm clicking the Run cell button on the left of the second cell.

> 🖱️ I'm pointing at the first output line, 127, 83, and 0.

> 🟢 127 dates use slashes. In 83 the first number is above 12, and the second never is, so the format is day, month, year. A shortcut like dayfirst True would also flip the correct dates, so I'll parse each format separately.

> 🖱️ I'm pointing at the rows with a ratio of 100 or 80.

> 🟢 Twelve prices are 100 times the list price, and their line total is in dollars: 3,200 against a total of 32. Two sources agree, so it's a unit error, cents.

> 🖱️ I'm pointing at the four rows with quantity 999.

> 🟢 999 units, but the total implies one unit: a system placeholder.

> 🖱️ I'm pointing at the three rows with 60, 80, and 100 units.

> 🟢 These are different: a ratio of 0.85, the B2B price, and the implied quantity matches. Real hotel orders. Same filter, opposite conclusion.

> 🖱️ I'm pointing at the rows with NaN in unit_price.

> 🟢 Ten missing prices, but every one has a quantity and a total, so the price can be recovered.

**Resultado esperado:** `127 83 0`. 29 filas: 12 con ratio 100 u 80, 4 con quantity 999 (implied 1,0), 3 B2B con ratio 0,85 (`O10492` 60, `O10493` 80, `O10494` 100) y 10 con unit_price NaN.

### D. 9:00–15:00 — Step 3: transformación (771 caracteres)

> 🖱️ I'm scrolling down and clicking the plus Code button at the top left, to add the third cell.

> ⌨️ *(comment, oc)* I'm typing the section comment and oc at the top of the third cell: a copy of the orders without the exact duplicates.

> ⌨️ *(the long date line)* I'm typing the date line. It reads the year-first dates first, and fillna reads the ones that failed as day, month, year.

> ⌨️ *(channel, customer_id, category)* I'm typing three cleaning lines: strip and title unify the channel labels, a missing customer becomes GUEST because it's a guest checkout, and the categories get the same cleaning.

> ⌨️ *(price_raw, qty_raw)* I'm typing the line that keeps the original price and quantity, so every change can be audited.

> ⌨️ *(np.select)* I'm typing the fix column with np.select. It labels each rule before any value changes: cents, no price, or the 999 placeholder.

> ⌨️ *(the three fixes)* I'm typing the three fixes: divide by 100, fill the missing price with total over quantity, and replace 999 with the implied quantity.

> ⌨️ *(print, value_counts)* I'm typing the checks on the last two lines.

> 🖱️ I'm clicking the Run cell button on the left of the third cell.

> 🖱️ I'm pointing at the printed line.

> 🟢 Zero dates left unread, three clean channels, and six clean categories.

> 🖱️ I'm moving the mouse down the fix counts.

> 🟢 12 prices in cents, 10 recovered prices, and 4 placeholder quantities: 26 corrections, each one labeled and with its original value kept.

**Resultado esperado:** `0 ['App' 'Web' 'B2B'] ['Kitchen' 'Bedding' 'Lighting' 'Decor' 'Bath' 'Outdoor']`. `fix`: vacío 3035, cents 12, no price 10, 999 qty 4.

### E. 15:00–19:30 — Step 4: conciliación (490 caracteres)

> 🖱️ I'm scrolling down and clicking the plus Code button at the top left, to add the fourth cell.

> ⌨️ *(comment, first merge)* I'm typing the first join at the top of the fourth cell. It drops the helper columns and joins the clean orders. validate m to 1 stops with an error if an order appears twice: that's my protection against double counting.

> ⌨️ *(second merge)* I'm typing the second join below it, the product name and category, with the same protection.

> ⌨️ *(Unknown)* I'm typing the Unknown line, for products that aren't in the catalog.

> ⌨️ *(exception)* I'm typing the exception column: no order, unknown product, or a total that doesn't match quantity times price.

> ⌨️ *(in_revenue, value_counts)* I'm typing in_revenue, only completed orders, and the counts on the last line.

> 🖱️ I'm clicking the Run cell button on the left of the fourth cell.

> 🟢 No error, so validate confirmed that every order and product appears only once.

> 🖱️ I'm moving the mouse down the exception counts.

> 🟢 Eight lines for P025, a product not in the catalog. The sale is real, so it stays in revenue as Unknown. Six totals don't match quantity times price: maybe a double charge or a refund. I can't tell which value is right, so I keep them and report them. And five lines belong to orders that don't exist, so they stay out of revenue.

**Resultado esperado:** vacío 3042, unknown product 8, total mismatch 6, no order 5.

### F. 19:30–25:00 — Step 5: análisis de negocio (494 caracteres)

> 🖱️ I'm scrolling down and clicking the plus Code button at the top left, to add the fifth cell.

> ⌨️ *(comment, r, ov)* I'm typing r and ov at the top of the fifth cell: the revenue lines, and one row per order, because the average order value must be per order, not per line.

> ⌨️ *(print)* I'm typing the print: total revenue, orders, and average order value.

> ⌨️ *(two displays)* I'm typing two displays: revenue by category, and the top five products.

> ⌨️ *(m and its display)* I'm typing the monthly revenue and its change from the previous month.

> ⌨️ *(June line)* I'm typing the last line: June revenue by channel.

> 🖱️ I'm clicking the Run cell button on the left of the fifth cell.

> 🖱️ I'm pointing at the first output line.

> 🟢 433,779 dollars of completed revenue, 1,328 orders, and an average order value of about 327 dollars.

> 🖱️ I'm pointing at the bottom of the category list, Bedding.

> 🟢 Bedding leads with about 112,000 dollars, followed by Lighting. 731 dollars are Unknown, the P025 sales.

> 🖱️ I'm moving the mouse down the top five products.

> 🟢 The Linen Duvet Cover leads with about 50,000 dollars, then the Brass Floor Lamp.

> 🖱️ I'm scrolling down to the monthly table and pointing at June and November.

> 🟢 June jumps 50% and then falls 25% in July. November rises 45%, the best month, which looks seasonal. June has no obvious season.

> 🖱️ I'm pointing at the B2B row of the last output.

> 🟢 B2B brought 21,000 dollars in June, more than Web and App together. That's the three hotel orders, so June wasn't general demand. It may not repeat, which matters for forecasting.

**Resultado esperado:** `433779.55 1328 326.64`. Bedding 112.125,95 · Lighting 81.683,65 · Unknown 731,00. Top: Linen Duvet Cover 50.161,65 · Brass Floor Lamp 41.467,20. Junio 40.937,45 (0,50), julio −0,25, noviembre 69.483,90 (0,45). Junio: B2B 21.312,05 · Web 11.431,60 · App 8.193,80.

### G. 25:00–28:00 — Step 6: outliers (207 caracteres)

> 🖱️ I'm scrolling down and clicking the plus Code button at the top left, to add the sixth cell.

> ⌨️ *(comment, lg)* I'm typing lg at the top of the sixth cell, the logarithm of each order value, because the values are skewed: many small orders and a few huge ones.

> ⌨️ *(q1, q3, lim, outlier)* I'm typing the quartiles, the IQR limit, and the outlier flag.

> ⌨️ *(print, groupby)* I'm typing the limit back in dollars, and the outliers by channel.

> 🖱️ I'm clicking the Run cell button on the left of the sixth cell.

> 🖱️ I'm pointing at the limit and then at the B2B row.

> 🟢 The limit is about 2,165 dollars. 36 orders are above it, all B2B, out of 61. These aren't errors: B2B is a separate segment. Deleting them would remove real revenue, so I'll report B2B separately. A z-score would fail here, because the large orders inflate the standard deviation.

**Resultado esperado:** `2165.16...`. App 0 de 451, B2B 36 de 61, Web 0 de 816.

### H. 28:00–30:30 — Step 7: gráficos (202 caracteres)

> 🖱️ I'm scrolling down and clicking the plus Code button at the top left, to add the seventh cell.

> ⌨️ *(comment, subplots)* I'm typing subplots at the top of the seventh cell, for two charts side by side.

> ⌨️ *(m.plot)* I'm typing the monthly line with Matplotlib, a line because it's a trend over time.

> ⌨️ *(boxplot, show)* I'm typing the Seaborn box plot by channel, on a log scale so small and large orders fit, and plt show.

> 🖱️ I'm clicking the Run cell button on the left of the seventh cell.

> 🖱️ I'm pointing at the June spike and the November peak on the left chart.

> 🟢 The June spike from the hotel orders, and the November peak.

> 🖱️ I'm moving the mouse across the three boxes on the right chart.

> 🟢 Web and App look alike. B2B sits far above, with a median more than ten times larger.

### I. 30:30–33:00 — Step 8: validación (233 caracteres)

> 🖱️ I'm scrolling down and clicking the plus Code button at the top left, to add the eighth cell.

> ⌨️ *(first print)* I'm typing the first print at the top of the eighth cell: a naive join of the raw files, against the raw line totals.

> ⌨️ *(second print)* I'm typing the second print: lines in, lines out, and the sum of the categories.

> ⌨️ *(groupby)* I'm typing the last line: the raw total split by status.

> 🖱️ I'm clicking the Run cell button on the left of the eighth cell.

> 🖱️ I'm pointing at the first line.

> 🟢 The naive join gives 465,624 dollars against 460,712 in the raw lines: almost 4,900 dollars too much, only because of the duplicates. That could explain part of finance's mismatch.

> 🖱️ I'm pointing at the second line.

> 🟢 3,061 lines in and out, and the categories add up exactly to the revenue.

> 🖱️ I'm moving the mouse down the three totals.

> 🟢 Completed, plus cancelled, plus 395 dollars without an order, adds up to the raw total. Nothing was forced to match.

**Resultado esperado:** `465624.75 460712.85`. `3061 3061 433779.55`. cancelled 26.538,30 · completed 433.779,55 · no order 395,00.

### J. 33:00–34:30 — Step 9: entregables (183 caracteres)

> 🖱️ I'm scrolling down and clicking the plus Code button at the top left, to add the ninth cell.

> ⌨️ *(comment, to_csv)* I'm typing the export of the clean dataset at the top of the ninth cell.

> ⌨️ *(rep, to_csv, len)* I'm typing the exception report: every line that was corrected, has an exception, or is out of revenue.

> 🖱️ I'm clicking the Run cell button on the left of the ninth cell.

> 🖱️ I'm pointing at the output, 211.

> 🟢 211 lines in the report: 26 corrected, 19 with an exception, and the rest are lines of cancelled orders.

> 🖱️ I'm clicking the Files icon in the left sidebar, and pointing at clean_sales and exceptions_report.

Si no aparecen: 🖱️ *"I'm clicking the refresh icon at the top of the Files panel, to update the list."*

> 🖱️ I'm clicking the Files icon again to close the panel.

### K. 34:30–38:00 — Conclusiones (534 caracteres)

> 🖱️ I'm clicking the plus Text button at the top left, next to plus Code, to add the conclusions cell.

> ⌨️ *(title, Data)* I'm typing the title and the data line in the text cell: the duplicates, the dates, the 26 corrections, and what remains unresolved.

> ⌨️ *(Business)* I'm typing the business line: revenue, orders, average order value, Bedding, June, and November.

> ⌨️ *(Outliers, Next)* I'm typing the outliers and the recommendations.

> ⌨️ *(Final notes)* I'm typing the final note at the bottom: the files are synthetic, generated with AI.

> 🖱️ I'm clicking the empty area below the text cell, to close the editor and show the formatted conclusions.

> 🖱️ I'm pressing Command + S to save the notebook in Drive.

### L. 38:00–40:00 — Epílogo

> 🖱️ I'm scrolling up slowly through the notebook, in the center of the screen.

> 🟢 My approach was to treat every anomaly as a question first. The same filter showed prices in cents, which were errors, and hotel orders of 100 units, which were real. The evidence decided, not the size of the number.

> 🟢 The main challenge was the duplicates: a simple join would have overstated revenue by almost 5,000 dollars, and nobody would see it in a chart. Another challenge was the dates: the convenient one-line parse would have silently flipped correct dates.

> 🟢 For the business, Bedding leads revenue, June's jump was three hotel orders, and B2B should be reported separately. The limits: one year of synthetic data, no costs per line, and six mismatches I can't resolve without the source system. Next, I'd send the exception report to sales operations and fix the export at the source. Thanks for watching!

---

## 7. Cronograma

Estimado, con dos velocidades: **150 caracteres por minuto** de tipeo y **130 palabras por minuto** de narración. Las frases ⌨️ se dicen mientras tipeás.

| Sección | Tiempo | Tipeo |
| ------- | ------ | ----- |
| A. Apertura | 0:00–1:30 | — |
| B. Step 1 | 1:30–5:00 | 380 (~2:30) |
| C. Step 2 | 5:00–9:00 | 345 (~2:20) |
| D. Step 3 | 9:00–15:00 | 771 (~5:10) |
| E. Step 4 | 15:00–19:30 | 490 (~3:15) |
| F. Step 5 | 19:30–25:00 | 494 (~3:20) |
| G. Step 6 | 25:00–28:00 | 207 (~1:25) |
| H. Step 7 | 28:00–30:30 | 202 (~1:20) |
| I. Step 8 | 30:30–33:00 | 233 (~1:35) |
| J. Step 9 | 33:00–34:30 | 183 (~1:15) |
| K. Conclusiones | 34:30–38:00 | 534 (~3:35) |
| L. Epílogo | 38:00–40:00 | — |
| **Total** | **~40 min** | ~3.840 (~26 min) |

Si tipeás a 120 caracteres por minuto, el total sube a unos **46 minutos**. Sigue por debajo de 50:59, pero **por encima de los 30 del prompt**: ver "Pendientes".

---

## 8. Checklist final

### Preparación (sin grabar)

- [ ] Practicá **tipeando las 9 celdas y las conclusiones** en un notebook de prueba, con cronómetro, al menos dos veces. Practicá sobre todo el Step 3 (la línea de fechas) y el Step 4 (`np.select`).
- [ ] Practicá el **autocompletado con Tab** (`o.order_d` + Tab → `order_date`) y decí la frase cuando lo uses.
- [ ] Creá el notebook vacío **sales_analysis** (**File → New notebook in Drive**).
- [ ] En el panel **Files**, subí `orders.csv`, `order_items.csv` y `products.csv` desde el Escritorio. Que estén solo esos tres.
- [ ] **Tools → Settings → AI assistance**: ocultá las funciones de IA, incluidas las sugerencias de código.
- [ ] Zoom (`Cmd + +`). Ventana maximizada.
- [ ] En Firefox, ventana 1 con la descripción de la tarea y ventana 2 con Colab, en la **segunda línea** del Dock.
- [ ] Grabá **enseguida** después de subir los CSV.

### Durante la grabación

- [ ] Las celdas se ejecutan **en orden** y **una sola vez** cada una. El Step 3 divide por 100: si lo corrés dos veces, divide de nuevo.
- [ ] La regla del mouse: se mueve solo con una frase 🖱️.
- [ ] No termines antes de: Step 9 ejecutado, los 2 archivos en Files, las conclusiones tipeadas, **Cmd + S** y el epílogo.

### Después de grabar

- [ ] Detené TaskRecorder.
- [ ] Descargá el `.ipynb` (**File → Download → Download .ipynb**) y los 2 CSV exportados.
- [ ] **Run full AutoQC**: What + Where tiene que pasar el **70%**.
- [ ] **Deliverables.zip** con el `.ipynb`, `clean_sales.csv`, `exceptions_report.csv` y los **tres CSV originales**.
- [ ] En Studio, marcá la opción de archivos generados con IA.
- [ ] Subí por separado el **MP4**, el **ZIP de TaskRecorder**, **Deliverables.zip** y **Metadata.rtf**.

---

## Si algo sale mal

Siempre decí **qué** corregís y **en qué celda**.

| Error | Qué pasa | Qué decís y hacés |
| ----- | -------- | ----------------- |
| `MergeError` en el Step 4 | `validate` encontró duplicados: el Step 3 no se ejecutó | 🖱️ *"The validate check stopped the join because the orders still have duplicates. That's the protection working. I'm running the third cell, and then this one again."* |
| El Step 3 corrido dos veces | Los precios en centavos se dividen otra vez | 🖱️ *"I ran the third cell twice, so the prices were divided again. I'm opening the Runtime menu and choosing Restart and run all."* |
| `AttributeError` o `KeyError` | Un nombre mal escrito | 🖱️ *"There's a typo in the column name in this cell. I'm fixing it and running it again."* |
| `NameError` | Una celda anterior no se ejecutó | 🖱️ *"An earlier cell didn't run. I'm opening the Runtime menu and choosing Run before."* |
| `FileNotFoundError` | El runtime se reinició | 🖱️ *"The files were deleted when the runtime restarted. I'm uploading the three CSV files again in the Files panel and running the first cell."* |
| Error en `log_scale` | Seaborn antiguo | 🖱️ *"This Seaborn version doesn't support log_scale. I'm removing it and adding a line with ax 1 set y scale log."* |

---

## Archivos de la carpeta

```
oyi436dd-customer-data-reconstruction/
├── README.md              ← este guion
├── orders.csv             ← entrada 1 (no se modifica)
├── order_items.csv        ← entrada 2 (no se modifica)
├── products.csv           ← entrada 3 (no se modifica)
└── sales_analysis.ipynb   ← notebook de referencia para practicar (no se usa en la grabación)
```
