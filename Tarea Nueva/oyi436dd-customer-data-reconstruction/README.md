# oyi436dd — Customer Data Reconstruction & Analytics

Guion para grabar la tarea **oyi436dd** (Data Science & Analytics). En **Google Colab**, con **pandas, NumPy, Matplotlib y Seaborn**, tomás tres CSV sintéticos e imperfectos de una tienda online ficticia. Con ellos perfilás los datos, investigás las anomalías antes de tocar nada, corregís solo lo que tiene evidencia y armás un dataset analítico confiable. Después analizás el negocio, validás los totales y entregás el dataset limpio, el reporte de excepciones, los gráficos y las conclusiones. Se graba en **Firefox**, en **una sola toma**, y el prompt pide **entre 15 y 30 minutos**. Este guion apunta a unos **30 minutos**, epílogo incluido.

**Cómo leer este guion:**

- 🖱️ = lo decís **mientras hacés** la acción. Siempre dice **qué** hacés, **dónde** está en la pantalla y, si no es obvio, **por qué**. Son las frases que cuenta AutoQC: **no te saltees ninguna**.
- 🟢 = explicación corta, entre una acción y otra. La última 🟢 de cada sección es la **transición** a la siguiente.
- ⌨️ = lo que vas diciendo **mientras tipeás** una celda larga, para no quedarte callado. Explica el bloque, no cada línea.
- 📘 **Qué hace cada línea**: debajo de cada código, la explicación línea por línea, por si tenés dudas o te preguntan. Es solo para vos: **no se lee en la grabación**, porque ahí cada celda se explica con una sola frase 🟢.
- Debajo de cada celda: **Resultado esperado** (lo que tiene que aparecer, con los números reales) y **Razonamiento profesional** (qué se decide, por qué, qué alternativas había y qué haría mal un analista sin experiencia). Esas dos partes son para vos: **no se leen**.
- Si usás un **atajo de teclado**, decí la tecla en voz alta: *"I'm pressing Command + S"*.
- **Todas las celdas son de código**, salvo la última (conclusiones), que es de texto. Las 9 secciones del notebook aparecen como **comentarios** en la primera línea de cada celda (`# 3. Data quality assessment`). Así el notebook queda ordenado sin celdas de texto extra.
- Toda celda sigue el mismo ciclo: **scroll hasta el final → clic en + Code → frase 🟢 de para qué sirve → tipear (con ⌨️) → clic en Run → señalar el resultado → explicarlo.**

---

## Pendientes antes de grabar

| Tema | Situación | Qué hacer |
| ---- | --------- | --------- |
| **Origen de los CSV** | El prompt pide que los archivos **los genere Gemini antes de grabar**, y la nota final del notebook dice eso. Los tres CSV de esta carpeta **los generé yo con un script de Python**. | Igual que en k3a13c10: **(a)** los generás con Gemini (abajo hay un prompt) y me los pasás: vuelvo a correr todo y actualizo los números. **(b)** Usás estos y la nota final dice cómo se generaron de verdad. **No digas "Gemini" si no es cierto.** |
| **Tipeo** | El código suma unos **4.700 caracteres**, más **930** de las conclusiones. A 300 caracteres por minuto son unos **19 minutos de tipeo** en una grabación de 30. Muy por encima del 25–30% que acepta AutoQC. | El prompt pide 9 secciones, 5 entregables y dos librerías de gráficos: no entra en mucho menos código. Practicá el tipeo y alargá las explicaciones (la grabación puede pasar de 30 minutos si las reglas de Odin lo permiten: el máximo general es 50:59). Si querés, saco secciones (por ejemplo, el top 5 de productos o el análisis de junio). |
| **Versión de pandas** | Lo probé con pandas 3.1. Colab suele traer pandas 2.x. | Si ves `object` en vez de `str`, o `1433.0` en vez de `1433`, es lo mismo: decí el número que veas. |

**Prompt sugerido para Gemini (opción a):**

> Create three synthetic CSV files for a fictional online home-goods retailer, "Brightside Home", for 2025, with no real people. 1) products.csv (24 rows): product_id (P001–P024), product_name, category (Kitchen, Bedding, Lighting, Decor, Bath, Outdoor; write 4 of them with inconsistent case or spaces), list_price, unit_cost. 2) orders.csv (about 1,400 orders): order_id, order_date (YYYY-MM-DD, but about 10% as DD/MM/YYYY), customer_id (about 18 missing), channel (Web, App, B2B, with some inconsistent spellings like "web", "APP ", "b2b"), status (completed or cancelled, about 6% cancelled); include 20 exact duplicate rows. 3) order_items.csv (about 3,000 lines): order_id, line_no, product_id, quantity, unit_price, line_total = quantity × unit_price. Include: 12 unit prices written in cents, 10 missing unit prices, 4 quantities of 999 where line_total equals one unit, 6 line totals that don't match, 8 lines for a product P025 that isn't in the catalog, 5 lines whose order doesn't exist, B2B orders of 10–40 units at 85% of list price, three very large B2B orders in June, and a November peak.

---

## Archivos de la carpeta

```
oyi436dd-customer-data-reconstruction/
├── README.md              ← este guion
├── orders.csv             ← archivo de entrada 1: cabecera de pedidos (no se modifica)
├── order_items.csv        ← archivo de entrada 2: líneas de pedido (no se modifica)
├── products.csv           ← archivo de entrada 3: catálogo (no se modifica)
└── sales_analysis.ipynb   ← notebook de referencia, completo y en orden
```

Para probar el notebook de referencia: en Colab, **File → Upload notebook → Browse**, elegís `sales_analysis.ipynb`, subís los tres CSV en el panel **Files** y ejecutás **Runtime → Run all**. Crea `clean_sales.csv` y `exceptions_report.csv`.

---

## 1. El escenario de negocio

**Brightside Home** es una tienda online ficticia de artículos para el hogar. Vende por tres canales: **Web**, **App** y **B2B** (hoteles y oficinas, con precio mayorista). Finanzas no logra que el ingreso de 2025 calculado con la exportación de ventas coincida con sus números. Además, la dirección quiere saber qué categorías y productos generan el ingreso y qué pasó en junio. El trabajo es reconstruir un dataset confiable y, recién con él, responder esas preguntas.

## 2. Los archivos de entrada

| Archivo | Filas | Columnas |
| ------- | ----- | -------- |
| `orders.csv` | 1.420 | `order_id`, `order_date`, `customer_id`, `channel`, `status` |
| `order_items.csv` | 3.061 | `order_id`, `line_no`, `product_id`, `quantity`, `unit_price`, `line_total` |
| `products.csv` | 24 | `product_id`, `product_name`, `category`, `list_price`, `unit_cost` |

## 3. Los problemas de calidad que contienen

Son para vos. En el video se **descubren** con el código, no se anticipan.

| Problema | Dónde | Cuántos | Qué se hace |
| -------- | ----- | ------- | ----------- |
| Filas de pedido duplicadas exactas | orders | 20 | Se eliminan (duplicarían el ingreso en el join) |
| Fechas en formato DD/MM/YYYY | orders | 127 | Se convierten, con evidencia de que el día va primero |
| Canal escrito de varias formas | orders | 9 variantes | Se normaliza a Web, App, B2B |
| Cliente vacío | orders | 18 | Se completa con `GUEST`: es compra como invitado, no un error |
| Pedidos cancelados | orders | 72 | Se conservan, pero quedan fuera del ingreso |
| Categoría escrita de varias formas | products | 4 | Se normaliza |
| Precio en centavos | items | 12 | Se divide por 100, con evidencia del catálogo y del total |
| Precio vacío | items | 10 | Se calcula como total ÷ cantidad |
| Cantidad 999 (valor de relleno) | items | 4 | Se reemplaza por la cantidad que confirma el total (1) |
| Total de línea que no coincide | items | 6 | **No se corrige**: queda como excepción sin resolver |
| Producto que no está en el catálogo (P025) | items | 8 líneas | Se mantiene en el ingreso como `Unknown` y se reporta |
| Línea sin pedido | items | 5 líneas | Queda fuera del ingreso y se reporta |
| Pedidos B2B grandes (legítimos) | items | 3 en junio | **No** son errores: se explican |

## 4. Las decisiones profesionales

1. Investigar antes de corregir: cada corrección necesita evidencia (catálogo, total de línea o patrón de fechas).
2. Guardar los valores originales (`unit_price_raw`, `quantity_raw`) y una columna `fix` que dice qué se corrigió.
3. No borrar faltantes ni outliers sin entender qué significan para el negocio.
4. No corregir lo que no tiene evidencia (los 6 totales que no coinciden).
5. Evitar el doble conteo: sacar los duplicados antes del join y usar `validate="m:1"`.
6. Medir los outliers del valor de pedido con IQR sobre el **logaritmo**, porque los importes tienen sesgo a la derecha.
7. Separar lo que es un error de datos de lo que es un comportamiento legítimo del negocio (B2B, descuentos, cancelaciones).

## 5. Los entregables

1. `clean_sales.csv`: dataset analítico limpio y validado, una fila por línea de pedido, con valores originales, correcciones y excepciones.
2. `exceptions_report.csv`: cada línea corregida, con excepción o fuera del ingreso.
3. Resumen del negocio: ingreso, ticket promedio, categorías, productos, meses.
4. Dos gráficos: ingreso mensual (Matplotlib) y valor de pedido por canal (Seaborn).
5. El notebook reproducible, con las conclusiones.

---

## Antes de grabar

1. Leé el Goal y comparalo con este guion.
2. En **Firefox**, dejá **dos ventanas**: la primera con la **descripción de la tarea**, en pantalla, porque con ella arranca la grabación. La segunda con **Google Colab** y el notebook ya creado: **File → New notebook in Drive**, con el nombre `sales_analysis` y la **celda de código vacía** que Colab crea sola. Revisá que, al hacer clic en el ícono de Firefox en el **Dock (a la derecha)**, Colab aparezca en la **segunda línea** de la lista.
3. Tené `orders.csv`, `order_items.csv` y `products.csv` en el **Escritorio**. Son los originales: no se tocan.
4. En Colab, **Tools → Settings → AI assistance**: ocultá las funciones de IA, si está la opción. No uses ninguna IA durante la grabación.
5. Maximizá la ventana de Colab y agrandá el zoom (`Cmd + +`) para que el código se lea.
6. Practicá una vez entera en voz alta, con cronómetro. Practicá sobre todo el tipeo de las celdas 5, 6 y 7.
7. Ejecutá las celdas con el **botón Run** (mouse), así cada ejecución tiene su frase.
8. No te quedes callado más de unos segundos: mientras tipeás, decí las frases ⌨️.
9. Salvo la descripción de la tarea del principio, no muestres Studio, Slack, Metadata.rtf, Insightful ni datos personales.

---

## A. 0:00–2:00 — Apertura

Empezás con la **descripción de la tarea** en pantalla. Esta primera parte dura **menos de 20 segundos**:

> 🟢 I will be beginning my task soon. I'll take an imperfect sales export from a fictional home-goods retailer, investigate its anomalies, rebuild a reliable analytical dataset in Google Colab, and use it to answer business questions about revenue, products, and channels.

> 🖱️ I'm clicking the yellow minimize button at the top left of this Firefox window, to put the task description away.

> 🖱️ I'm clicking the Firefox icon in the Dock, on the right side of the screen, to see my open Firefox windows.

> 🖱️ I'm clicking the second line of the list, the Google Colab window, to open my notebook.

> 🖱️ I'm pointing at the notebook name, sales_analysis, at the top left next to the Colab logo. I created this empty notebook before starting.

> 🖱️ I'm clicking the Files icon, the folder in the left sidebar, to open the file panel.

> 🖱️ I'm clicking the Upload to session storage button, the page with an up arrow at the top of the left panel, to choose the input files.

> 🖱️ In the file window, I'm clicking Desktop on the left, selecting orders.csv, order_items.csv, and products.csv with Command held down, and clicking Open at the bottom right.

Si aparece el aviso de que los archivos se borran al reiniciar el runtime:

> 🖱️ I'm clicking OK on the warning in the center of the screen. It only says uploaded files are deleted when the runtime restarts.

> 🖱️ I'm pointing at the three files in the left panel, in the file list.

> 🟢 Here's the business problem. Brightside Home sells home goods through three channels: the website, the app, and B2B sales to hotels and offices. Finance can't make the 2025 revenue from this export match their own numbers, and management wants to know which categories and products drive revenue, and what happened in June.

> 🟢 I have three synthetic files, created before recording: orders, with one row per order; order items, with one row per product in an order; and the product catalog. The originals stay unchanged. I'll work on copies and keep the original values next to every correction.

> 🟢 The plan: profile the data, investigate every anomaly before changing anything, correct only what has evidence, and build one clean table. Then analyze revenue, products, channels, and months, check outliers, validate every total against the original, and export the clean dataset and an exception report.

> 🖱️ I'm clicking the Files icon in the left sidebar again, to close the panel.

> 🟢 Let's load the data.

**Razonamiento profesional:** decir el problema de negocio antes que el código fija qué significa "confiable": que los totales cierren y que cada cambio se pueda rastrear. Un analista sin experiencia empieza a limpiar sin saber qué pregunta responde, y termina borrando datos que el negocio necesitaba.

---

## B. 2:00–5:30 — Carga y perfil de los datos

> 🟢 Section two: loading and initial inspection.

> 🖱️ I'm clicking inside the empty code cell at the top of the notebook, to start typing in it.

> 🟢 This first code cell imports the four libraries, reads the three files, and prints the size and the missing values of each one.

> 🖱️ I'm typing the code in the first code cell, in the middle of the screen.

> ⌨️ The comment at the top marks the section, so the notebook reads like a report. The list comprehension reads the three files in one line.

**Celda 1:**

```python
# 1-2. Business context and data loading
import pandas as pd, numpy as np, matplotlib.pyplot as plt, seaborn as sns
orders, items, products = [pd.read_csv(f) for f in ["orders.csv", "order_items.csv", "products.csv"]]
for t in [orders, items, products]:
    print(t.shape, t.isna().sum()[lambda s: s > 0].to_dict())
```

📘 **Qué hace cada línea** (para vos, no se lee):

- `# 1-2. Business context and data loading`: comentario con el nombre de la sección. No se ejecuta.
- `import pandas as pd, numpy as np, matplotlib.pyplot as plt, seaborn as sns`: importa las cuatro librerías con sus nombres cortos habituales.
- `orders, items, products = [pd.read_csv(f) for f in [...]]`: lee los tres CSV en una línea y guarda cada tabla en su variable, en ese orden.
- `for t in [orders, items, products]:`: recorre las tres tablas.
- `print(t.shape, t.isna().sum()[lambda s: s > 0].to_dict())`: muestra (filas, columnas) y, solo para las columnas con vacíos, cuántos tiene cada una.

> 🖱️ I'm clicking the Run cell button, the play icon on the left edge of the first code cell, to load the files.

> 🖱️ I'm pointing at the status at the top right of Colab, which turns green when the runtime is connected.

> 🖱️ I'm moving the mouse down the three lines of the output, under the first code cell.

> 🟢 1,420 orders, 3,061 order lines, and 24 products. Only two columns have missing values: 18 orders without a customer ID, and 10 order lines without a unit price. I won't fill or delete them yet. First, I need to know what they mean.

> 🖱️ I'm scrolling down to the end of the output, and clicking the plus Code button in the toolbar at the top left, to add the second code cell.

> 🟢 This second code cell assesses quality: duplicate orders, the labels used for channels and categories, the order statuses, and the distribution of the order lines.

> 🖱️ I'm typing the quality checks in the second code cell.

> ⌨️ duplicated counts rows that are identical to an earlier one. And I also count repeated order IDs, to see if a duplicate could be a different order with the same ID.

**Celda 2:**

```python
# 3. Data quality assessment
print("Duplicate order rows:", orders.duplicated().sum(), "| repeated IDs:", orders["order_id"].duplicated().sum())
print(orders["channel"].unique(), products["category"].unique(), orders["status"].value_counts().to_dict())
items.describe().round(2)
```

📘 **Qué hace cada línea** (para vos, no se lee):

- `# 3. Data quality assessment`: comentario de sección.
- `print("Duplicate order rows:", orders.duplicated().sum(), "| repeated IDs:", orders["order_id"].duplicated().sum())`: cuenta las filas idénticas a una anterior y los IDs de pedido repetidos.
- `print(orders["channel"].unique(), products["category"].unique(), orders["status"].value_counts().to_dict())`: muestra las distintas formas en que están escritos el canal y la categoría, y cuántos pedidos hay en cada estado.
- `items.describe().round(2)`: estadísticas de las columnas numéricas de las líneas (también aparece `line_no`).

> 🖱️ I'm clicking the Run cell button on the left of the second code cell, to run the checks.

> 🖱️ I'm pointing at the first line of the output.

> 🟢 20 duplicate order rows, and exactly 20 repeated IDs. So every repeated ID is a full copy of the same order, probably exported twice. That matters a lot: if I join the order lines to these orders, each of those orders would count its revenue twice.

> 🖱️ I'm moving the mouse along the channel and category labels, on the second line.

> 🟢 Three channels written nine different ways: Web, web, WEB, Web with a space, and so on. And six categories written ten ways. Same meaning, different text, so any group by would split them.

> 🖱️ I'm pointing at the statuses at the end of the line.

> 🟢 1,348 completed and 72 cancelled. Cancelled orders aren't revenue, but I won't delete them: they're still part of the business.

> 🖱️ I'm moving the mouse down the max row of the description table, at the bottom.

> 🟢 And the order lines have three suspicious maximums: a quantity of 999, a unit price of 15,900 dollars for home goods, and a line total of 6,579 dollars. Some of these may be errors and some may be real large orders. That's what I'll investigate next.

**Resultado esperado:** celda 1: `(1420, 5) {'customer_id': 18}`, `(3061, 6) {'unit_price': 10}`, `(24, 5) {}`. Celda 2: `Duplicate order rows: 20 | repeated IDs: 20`; canales `App, Web, B2B, WEB, web, Web , app, b2b, APP`; categorías `Kitchen, kitchen, Bedding, Lighting, ' Lighting', Decor, 'decor ', Bath, Outdoor, OUTDOOR`; `{'completed': 1348, 'cancelled': 72}`; máximos: quantity **999**, unit_price **15.900**, line_total **6.579**.

**Razonamiento profesional:** comparar duplicados de fila completa con IDs repetidos dice **qué tipo** de duplicado es. Si los IDs repetidos fueran más que las filas duplicadas, habría pedidos distintos con el mismo ID, y borrarlos perdería ventas reales. Error típico: llamar a `drop_duplicates(subset="order_id")` sin mirar, o ver los máximos y borrar "los outliers" sin preguntar qué son.

> 🟢 Let's investigate those values one by one, starting with the dates.

---

## C. 5:30–9:30 — Investigación de anomalías

> 🟢 Section four: anomaly investigation.

> 🖱️ I'm scrolling down below the table, and clicking the plus Code button in the toolbar at the top left, to add the third code cell.

> 🟢 This third code cell finds the dates that aren't in the year-first format, and tests which part is the day: if the first number is ever above 12, it can't be a month.

> 🖱️ I'm typing the date investigation in the third code cell.

> ⌨️ The pattern backslash d four times plus a dash matches dates that start with a four-digit year. The tilde keeps the ones that don't.

**Celda 3:**

```python
# 4. Anomaly investigation
other = orders.loc[~orders["order_date"].str.match(r"\d{4}-"), "order_date"]
print(len(other), other.head(3).tolist(), "| day > 12:", (other.str[:2].astype(int) > 12).sum(), "| month > 12:", (other.str[3:5].astype(int) > 12).sum())
```

📘 **Qué hace cada línea** (para vos, no se lee):

- `# 4. Anomaly investigation`: comentario de sección.
- `other = orders.loc[~orders["order_date"].str.match(r"\d{4}-"), "order_date"]`: fechas que **no** empiezan con cuatro dígitos y un guion, o sea, que no son año-mes-día.
- `print(len(other), other.head(3).tolist(), "| day > 12:", ..., "| month > 12:", ...)`: cuántas son, tres ejemplos, en cuántas el primer número (`str[:2]`) es mayor que 12 y en cuántas lo es el segundo (`str[3:5]`).

> 🖱️ I'm clicking the Run cell button on the left of the third code cell, to check the dates.

> 🖱️ I'm pointing at the output under the third code cell.

> 🟢 127 dates use another format, like 02/01/2025. That could be February 1st or January 2nd. The evidence settles it: in 83 of them, the first number is above 12, so it must be the day. And the second number is never above 12. So the format is day, month, year.

> 🟢 This is where an inexperienced analyst often goes wrong. A one-line fix like to_datetime with format mixed and dayfirst True looks convenient, but I tested it: it also reads the correct year-first dates with the day first, so January 2nd silently becomes February 1st. I'll parse each format explicitly instead.

> 🖱️ I'm scrolling down below the output, and clicking the plus Code button in the toolbar at the top left, to add the fourth code cell.

> 🟢 This fourth code cell compares every order line with the catalog. The price ratio is the unit price over the list price, and the implied quantity is the line total over the unit price. Then it shows the suspicious lines: prices more than twice the list price, quantities of 50 or more, and missing prices.

> 🖱️ I'm typing the price and quantity investigation in the fourth code cell.

> ⌨️ The left merge keeps every line, even if its product isn't in the catalog.

> ⌨️ A normal discount gives a ratio between 0.8 and 1, so anything above 2 isn't a discount.

**Celda 4:**

```python
li = items.merge(products[["product_id", "list_price"]], on="product_id", how="left")
li["price_ratio"] = li["unit_price"] / li["list_price"]
li["implied_qty"] = li["line_total"] / li["unit_price"]
li[(li["price_ratio"] > 2) | (li["quantity"] >= 50) | li["unit_price"].isna()]
```

📘 **Qué hace cada línea** (para vos, no se lee):

- `li = items.merge(products[["product_id", "list_price"]], on="product_id", how="left")`: agrega a cada línea el precio de lista del catálogo. `how="left"` conserva las líneas cuyo producto no está en el catálogo.
- `li["price_ratio"] = li["unit_price"] / li["list_price"]`: precio cobrado ÷ precio de lista (1 = precio lleno, 0,8 = 20% de descuento, 100 = centavos).
- `li["implied_qty"] = li["line_total"] / li["unit_price"]`: la cantidad que se deduce del total.
- `li[(li["price_ratio"] > 2) | (li["quantity"] >= 50) | li["unit_price"].isna()]`: muestra las líneas con un precio de más del doble, una cantidad de 50 o más, o un precio vacío (`|` = "o").

> 🖱️ I'm clicking the Run cell button on the left of the fourth code cell, to compare with the catalog.

> 🖱️ I'm pointing at the rows where price_ratio is 100 or 80, in the table.

> 🟢 Twelve lines have a price ratio of 100 or 80: exactly 100 times the list price, or 100 times a 20% discount. And look at the line total: 32 dollars for a price of 3,200. The line total is in dollars and the price is in cents. Two independent sources agree, so this is a unit error.

> 🖱️ I'm pointing at the four rows with a quantity of 999.

> 🟢 Four lines have a quantity of 999, but the implied quantity is exactly 1: the line total equals one unit. 999 is a typical placeholder value from a system, not a real order of 999 items.

> 🖱️ I'm pointing at the three rows with quantities of 60, 80, and 100.

> 🟢 And these three are different. 60, 80, and 100 units, at 85% of the list price, and the implied quantity matches the recorded one. That's the B2B wholesale price, so these are real bulk orders. Same filter, opposite conclusion: they stay as they are.

> 🖱️ I'm pointing at the rows with NaN in unit_price.

> 🟢 Ten lines have no price, but they all have a quantity and a line total, so the price can be recovered as total divided by quantity, and it's traceable.

**Resultado esperado:** celda 3: `127 ['02/01/2025', '03/01/2025', '04/01/2025'] | day > 12: 83 | month > 12: 0`. Celda 4: **29 filas**: 12 con `price_ratio` 100 u 80 (por ejemplo, `O10386` P014: 3.200,00 con total 32,0), 4 con `quantity` 999 e `implied_qty` 1,0, 3 pedidos B2B (`O10492` 60 × 109,65 = 6.579,0, `O10493` 80 × 67,15, `O10494` 100 × 50,15, ratio 0,85) y 10 con `unit_price` NaN.

**Razonamiento profesional:** la misma tabla mezcla errores y ventas reales a propósito, para mostrar que un filtro no es un veredicto. La evidencia (ratio contra el catálogo y cantidad implícita por el total) decide en cada caso. Alternativa descartada: marcar outliers con z-score sobre `unit_price` o `quantity`. Habría señalado igual los pedidos de hotel y los errores de centavos, sin distinguirlos.

> 🟢 I've investigated the anomalies. Now I'll apply the rules, keeping every original value.

---

## D. 9:30–15:00 — Transformación y conciliación

> 🟢 Section five: transformation and reconciliation.

> 🖱️ I'm scrolling down below the table, and clicking the plus Code button in the toolbar at the top left, to add the fifth code cell.

> 🟢 This fifth code cell cleans a copy of the orders: it removes the exact duplicates, parses each date format explicitly, normalizes the channel labels, and fills missing customers with GUEST. It also normalizes the catalog categories. The last line checks that nothing was left unparsed.

> 🖱️ I'm typing the order transformations in the fifth code cell.

> ⌨️ The first parse reads the year-first dates, and fillna uses the day-first parse only where the first one failed.

> ⌨️ strip removes the spaces, and title gives every label the same capitalization.

> ⌨️ A missing customer here means a guest checkout, so I label it instead of deleting the order.

**Celda 5:**

```python
# 5. Transformation and reconciliation
o = orders.drop_duplicates().copy()
d = o["order_date"]
o["order_date"] = pd.to_datetime(d, format="ISO8601", errors="coerce").fillna(pd.to_datetime(d, format="%d/%m/%Y", errors="coerce"))
o["channel"] = o["channel"].str.strip().str.title()
o["customer_id"] = o["customer_id"].fillna("GUEST")
p = products.assign(category=products["category"].str.strip().str.title())
print(o["order_date"].isna().sum(), o["channel"].unique(), p["category"].unique())
```

📘 **Qué hace cada línea** (para vos, no se lee):

- `# 5. Transformation and reconciliation`: comentario de sección.
- `o = orders.drop_duplicates().copy()`: copia de los pedidos sin las filas duplicadas exactas.
- `d = o["order_date"]`: guarda la columna de fecha original (texto) con un nombre corto.
- `o["order_date"] = pd.to_datetime(d, format="ISO8601", errors="coerce").fillna(pd.to_datetime(d, format="%d/%m/%Y", errors="coerce"))`: primero lee las fechas año-mes-día. Las que fallan quedan vacías (`errors="coerce"`), y `fillna` las completa leyéndolas como día/mes/año.
- `o["channel"] = o["channel"].str.strip().str.title()`: saca los espacios y pone mayúscula inicial (`web` y `WEB` → `Web`, `b2b` → `B2B`).
- `o["customer_id"] = o["customer_id"].fillna("GUEST")`: completa los clientes vacíos con `GUEST`.
- `p = products.assign(category=...)`: copia del catálogo, con la categoría normalizada igual que el canal.
- `print(o["order_date"].isna().sum(), o["channel"].unique(), p["category"].unique())`: comprueba que no quedó ninguna fecha sin leer y muestra los valores ya limpios.

> 🖱️ I'm clicking the Run cell button on the left of the fifth code cell, to clean the orders.

> 🖱️ I'm pointing at the output under the fifth code cell.

> 🟢 Zero dates left unparsed, three channels, Web, App, and B2B, and six clean categories.

> 🖱️ I'm scrolling down below the output, and clicking the plus Code button in the toolbar at the top left, to add the sixth code cell.

> 🟢 This sixth code cell fixes the order lines. First, it keeps the original price and quantity in new columns. Then it writes in a fix column which rule applies to each line, and applies the three rules: cents divided by 100, missing prices from the line total, and the 999 placeholder replaced by the implied quantity.

> 🖱️ I'm typing the line corrections in the sixth code cell.

> ⌨️ np.select checks the conditions in order and writes the matching label, or an empty text if none applies.

> ⌨️ The labels are decided before any value changes, so they describe the original data.

**Celda 6:**

```python
li["unit_price_raw"], li["quantity_raw"] = li["unit_price"], li["quantity"]
li["fix"] = np.select([li["price_ratio"] > 50, li["unit_price"].isna(), li["quantity"] == 999],
                      ["price in cents", "price from line total", "placeholder quantity"], "")
li.loc[li["fix"] == "price in cents", "unit_price"] /= 100
li["unit_price"] = li["unit_price"].fillna(li["line_total"] / li["quantity"])
li.loc[li["fix"] == "placeholder quantity", "quantity"] = li["implied_qty"]
li["fix"].value_counts()
```

📘 **Qué hace cada línea** (para vos, no se lee):

- `li["unit_price_raw"], li["quantity_raw"] = li["unit_price"], li["quantity"]`: guarda el precio y la cantidad originales en columnas nuevas.
- `li["fix"] = np.select([...], [...], "")`: escribe la etiqueta de la primera condición que se cumpla: precio más de 50 veces el de lista → `price in cents`; precio vacío → `price from line total`; cantidad 999 → `placeholder quantity`. Si no se cumple ninguna, texto vacío.
- `li.loc[li["fix"] == "price in cents", "unit_price"] /= 100`: divide por 100 el precio de esas líneas.
- `li["unit_price"] = li["unit_price"].fillna(li["line_total"] / li["quantity"])`: completa los precios vacíos con total ÷ cantidad.
- `li.loc[li["fix"] == "placeholder quantity", "quantity"] = li["implied_qty"]`: reemplaza el 999 por la cantidad que da el total (1).
- `li["fix"].value_counts()`: cuántas líneas tuvo cada corrección.

> 🖱️ I'm clicking the Run cell button on the left of the sixth code cell, to apply the rules.

> 🖱️ I'm moving the mouse down the counts.

> 🟢 Twelve prices in cents, ten prices from the line total, and four placeholder quantities. 26 corrections, each one labeled and with its original value kept. Every other line is untouched.

> 🖱️ I'm scrolling down below the counts, and clicking the plus Code button in the toolbar at the top left, to add the seventh code cell.

> 🟢 This seventh code cell builds the analytical table: it joins the lines with the clean orders and the catalog, and marks three exceptions: lines whose order doesn't exist, products missing from the catalog, and lines where quantity times price doesn't match the total. Only completed orders count as revenue.

> 🖱️ I'm typing the join in the seventh code cell.

> ⌨️ validate m to 1 makes pandas stop with an error if an order or a product appears twice on the right side. That's my protection against double counting.

> ⌨️ The left joins keep every order line, even the ones with problems, so nothing disappears silently.

**Celda 7:**

```python
clean = (li.drop(columns=["list_price", "price_ratio", "implied_qty"])
           .merge(o, on="order_id", how="left", validate="m:1")
           .merge(p[["product_id", "product_name", "category"]], on="product_id", how="left", validate="m:1"))
clean["category"] = clean["category"].fillna("Unknown")
clean["exception"] = np.select([clean["status"].isna(), clean["category"] == "Unknown",
                                (clean["quantity"] * clean["unit_price"] - clean["line_total"]).abs() > 0.01],
                               ["order not found", "product not in catalog", "line total mismatch"], "")
clean["in_revenue"] = clean["status"] == "completed"
clean["exception"].value_counts()
```

📘 **Qué hace cada línea** (para vos, no se lee):

- `clean = (li.drop(columns=[...])`: saca las columnas auxiliares de la investigación.
- `.merge(o, on="order_id", how="left", validate="m:1")`: agrega los datos del pedido. `validate="m:1"` frena con un error si un pedido aparece dos veces en `o`: es la protección contra el doble conteo.
- `.merge(p[[...]], on="product_id", how="left", validate="m:1"))`: agrega el nombre y la categoría del producto, con la misma protección.
- `clean["category"] = clean["category"].fillna("Unknown")`: los productos que no están en el catálogo quedan como `Unknown`.
- `clean["exception"] = np.select([...], [...], "")`: etiqueta la excepción. Sin estado → el pedido no existe. Categoría `Unknown` → producto fuera del catálogo. Cantidad × precio distinto del total por más de un centavo → total que no coincide.
- `clean["in_revenue"] = clean["status"] == "completed"`: solo los pedidos completados cuentan como ingreso. Los cancelados y las líneas sin pedido, no.
- `clean["exception"].value_counts()`: cuántas líneas hay de cada excepción.

> 🖱️ I'm clicking the Run cell button on the left of the seventh code cell, to build the table.

> 🟢 The join ran without an error, so validate confirmed that every order and every product appears only once.

> 🖱️ I'm moving the mouse down the exception counts.

> 🟢 Five lines belong to orders that don't exist, so I can't date them or know their status. They stay out of revenue. Eight lines are for product P025, which isn't in the catalog. The sale is real, so it stays in revenue, but under the category Unknown. And six lines have a total that doesn't match.

> 🖱️ I'm scrolling down below the counts, and clicking the plus Code button in the toolbar at the top left, to add the eighth code cell.

> 🟢 This eighth code cell shows those six mismatches, with the first six columns of the table.

> 🖱️ I'm typing the filter in the eighth code cell.

**Celda 8:**

```python
clean[clean["exception"] == "line total mismatch"].iloc[:, :6]
```

📘 **Qué hace cada línea** (para vos, no se lee):

- `clean[clean["exception"] == "line total mismatch"].iloc[:, :6]`: muestra las líneas cuyo total no coincide, solo con las 6 primeras columnas (pedido, línea, producto, cantidad, precio y total).

> 🖱️ I'm clicking the Run cell button on the left of the eighth code cell, to show the mismatches.

> 🖱️ I'm moving the mouse across the six rows, between the quantity, unit_price, and line_total columns.

> 🟢 Two totals are double the expected value, two are one and a half times, and two are half. Maybe a line was charged twice, or a partial refund was recorded in the same line. I can't tell which value is right: the total may be what the customer actually paid. So I keep the recorded total and report these six as unresolved.

**Resultado esperado:** celda 5: `0 ['App' 'Web' 'B2B'] ['Kitchen' 'Bedding' 'Lighting' 'Decor' 'Bath' 'Outdoor']`. Celda 6: price in cents 12, price from line total 10, placeholder quantity 4. Celda 7: product not in catalog 8, line total mismatch 6, order not found 5. Celda 8: `O10348` 2 × 75,0 = 300,0 · `O10564` 2 × 99,0 = 99,0 · `O10644` 3 × 30,4 = 136,8 · `O10943` 1 × 99,0 = 198,0 · `O10988` 2 × 39,0 = 117,0 · `O11321` 1 × 24,0 = 12,0.

**Razonamiento profesional:** cada corrección queda rastreable (valor original + etiqueta en `fix`), y las tres reglas se deciden antes de cambiar valores. `validate="m:1"` convierte el riesgo de doble conteo en un error visible. Alternativas descartadas: borrar las líneas con problemas (se pierde ingreso real, como el de P025) o "arreglar" los 6 totales con cantidad × precio (se borraría la evidencia de un posible cobro doble).

> 🟢 The dataset is reconstructed. Now I can trust it to answer the business questions.

---

## E. 15:00–21:00 — Análisis de negocio

> 🟢 Section six: business analysis.

> 🖱️ I'm scrolling down below the table, and clicking the plus Code button in the toolbar at the top left, to add the ninth code cell.

> 🟢 This ninth code cell keeps only the revenue lines, adds them up by order to get each order's value, and prints total revenue, the number of orders, and the average order value. Then it compares revenue and units by category.

> 🖱️ I'm typing the analysis in the ninth code cell.

> ⌨️ The average order value has to be calculated per order, not per line, because one order can have several lines.

**Celda 9:**

```python
# 6. Business analysis
rev = clean[clean["in_revenue"]]
order_val = rev.groupby(["order_id", "channel"], as_index=False)["line_total"].sum()
print("Revenue:", rev["line_total"].sum().round(2), "| Orders:", len(order_val), "| AOV:", order_val["line_total"].mean().round(2))
rev.groupby("category").agg(revenue=("line_total", "sum"), units=("quantity", "sum")).sort_values("revenue", ascending=False)
```

📘 **Qué hace cada línea** (para vos, no se lee):

- `# 6. Business analysis`: comentario de sección.
- `rev = clean[clean["in_revenue"]]`: solo las líneas que cuentan como ingreso.
- `order_val = rev.groupby(["order_id", "channel"], as_index=False)["line_total"].sum()`: suma las líneas de cada pedido. Queda una fila por pedido, con su canal y su valor.
- `print("Revenue:", ..., "| Orders:", len(order_val), "| AOV:", order_val["line_total"].mean().round(2))`: ingreso total, cantidad de pedidos y ticket promedio (el promedio por pedido).
- `rev.groupby("category").agg(revenue=..., units=...).sort_values("revenue", ascending=False)`: ingreso y unidades por categoría, de mayor a menor ingreso.

> 🖱️ I'm clicking the Run cell button on the left of the ninth code cell, to calculate the metrics.

> 🖱️ I'm pointing at the printed line under the ninth code cell.

> 🟢 Completed revenue is 433,779 dollars from 1,328 orders, an average order value of about 327 dollars.

> 🖱️ I'm moving the mouse down the category table.

> 🟢 Bedding leads with about 112,000 dollars, followed by Lighting with almost 82,000. Bath sells the most units, 1,516, but ranks last in revenue among the real categories, because its products are cheap. So volume and revenue tell different stories.

> 🖱️ I'm scrolling down below the table, and clicking the plus Code button in the toolbar at the top left, to add the tenth code cell.

> 🟢 This tenth code cell lists the five products with the most revenue.

> 🖱️ I'm typing the top products in the tenth code cell.

**Celda 10:**

```python
rev.groupby("product_name")["line_total"].sum().nlargest(5)
```

📘 **Qué hace cada línea** (para vos, no se lee):

- `rev.groupby("product_name")["line_total"].sum().nlargest(5)`: ingreso por producto, y los 5 más altos.

> 🖱️ I'm clicking the Run cell button on the left of the tenth code cell, to rank the products.

> 🖱️ I'm moving the mouse down the five products.

> 🟢 The Linen Duvet Cover is the top product, with about 50,000 dollars, followed by the Brass Floor Lamp. Both are among the most expensive items in the catalog.

> 🖱️ I'm scrolling down below the list, and clicking the plus Code button in the toolbar at the top left, to add the eleventh code cell.

> 🟢 This eleventh code cell adds up revenue by month and shows the change from the previous month, to find unusual movements.

> 🖱️ I'm typing the monthly table in the eleventh code cell.

**Celda 11:**

```python
monthly = rev.groupby(rev["order_date"].dt.to_period("M"))["line_total"].sum()
pd.DataFrame({"revenue": monthly, "change": monthly.pct_change()}).round(2)
```

📘 **Qué hace cada línea** (para vos, no se lee):

- `monthly = rev.groupby(rev["order_date"].dt.to_period("M"))["line_total"].sum()`: ingreso por mes. `to_period("M")` convierte cada fecha en su mes, por ejemplo `2025-06`.
- `pd.DataFrame({"revenue": monthly, "change": monthly.pct_change()}).round(2)`: tabla con el ingreso de cada mes y su variación contra el mes anterior (0,50 = +50%).

> 🖱️ I'm clicking the Run cell button on the left of the eleventh code cell, to see the trend.

> 🖱️ I'm pointing at the June row, in the middle of the table.

> 🟢 Two months stand out. June jumps 50%, to almost 41,000 dollars, and then falls 25% in July.

> 🖱️ I'm pointing at the November row, near the bottom.

> 🟢 And November rises 45%, to about 69,000 dollars, the best month of the year. November looks seasonal, the holiday and Black Friday period. But June has no obvious season, so I'll check it.

> 🖱️ I'm scrolling down below the table, and clicking the plus Code button in the toolbar at the top left, to add the twelfth code cell.

> 🟢 This twelfth code cell splits June's revenue by channel.

> 🖱️ I'm typing the June breakdown in the twelfth code cell.

**Celda 12:**

```python
rev[rev["order_date"].dt.month == 6].groupby("channel")["line_total"].agg(["sum", "count"])
```

📘 **Qué hace cada línea** (para vos, no se lee):

- `rev[rev["order_date"].dt.month == 6].groupby("channel")["line_total"].agg(["sum", "count"])`: solo junio, por canal: ingreso total y cantidad de líneas.

> 🖱️ I'm clicking the Run cell button on the left of the twelfth code cell, to break down June.

> 🖱️ I'm pointing at the B2B row.

> 🟢 B2B brought about 21,000 dollars in June, with only 8 lines, more than Web and App together. That's the three hotel orders we saw earlier, about 17,000 dollars together. So June wasn't a general increase in demand: it was three large customers. For forecasting, that's very different, because it may not repeat.

> 🖱️ I'm scrolling down below the table, and clicking the plus Code button in the toolbar at the top left, to add the thirteenth code cell.

> 🟢 This thirteenth code cell looks for outlier orders with the IQR method. Order values are skewed to the right: many small orders and a few very large ones. So I apply IQR to the logarithm of the value, which makes the distribution more symmetric. Then I count the outliers by channel.

> 🖱️ I'm typing the outlier check in the thirteenth code cell.

> ⌨️ The upper limit is converted back from the logarithm, so I can read it in dollars.

**Celda 13:**

```python
log_value = np.log10(order_val["line_total"])
q1, q3 = log_value.quantile([0.25, 0.75])
order_val["outlier"] = log_value > q3 + 1.5 * (q3 - q1)
print("Upper limit:", round(10 ** (q3 + 1.5 * (q3 - q1)), 2))
order_val.groupby("channel")["outlier"].agg(["sum", "count"])
```

📘 **Qué hace cada línea** (para vos, no se lee):

- `log_value = np.log10(order_val["line_total"])`: logaritmo en base 10 del valor de cada pedido (100 → 2, 1.000 → 3).
- `q1, q3 = log_value.quantile([0.25, 0.75])`: primer y tercer cuartil, en escala logarítmica.
- `order_val["outlier"] = log_value > q3 + 1.5 * (q3 - q1)`: True si el pedido supera el límite superior del IQR.
- `print("Upper limit:", round(10 ** (q3 + 1.5 * (q3 - q1)), 2))`: el límite, vuelto a dólares (`10 **` deshace el logaritmo).
- `order_val.groupby("channel")["outlier"].agg(["sum", "count"])`: por canal, cuántos outliers hay (`sum`) sobre cuántos pedidos (`count`).

> 🖱️ I'm clicking the Run cell button on the left of the thirteenth code cell, to find the outliers.

> 🖱️ I'm pointing at the upper limit, and then at the B2B row.

> 🟢 The upper limit is about 2,165 dollars per order. 36 orders are above it, and all 36 are B2B, out of 61 B2B orders. Web and App have none.

> 🟢 So these aren't errors. B2B is a different customer segment, with much larger orders. Deleting them would remove real revenue, and averaging them with consumer orders would distort the average order value. The professional answer is to report B2B separately.

> 🟢 Why not the mean and standard deviation, the z-score? Because it assumes a symmetric distribution, and the large orders themselves inflate the standard deviation, hiding the outliers. IQR on the log scale is robust to that.

**Resultado esperado:** celda 9: `Revenue: 433779.55 | Orders: 1328 | AOV: 326.64`; Bedding 112.125,95 · Lighting 81.683,65 · Outdoor 71.573,65 · Kitchen 58.372,80 · Decor 58.125,30 · Bath 51.167,20 (1.516 unidades) · Unknown 731,00. Celda 10: Linen Duvet Cover 50.161,65 · Brass Floor Lamp 41.467,20 · Cotton Sheet Set 29.719,80 · Garden Hose Reel 28.785,25 · Wall Mirror 25.759,80. Celda 11: junio 40.937,45 (+0,50), julio −0,25, noviembre 69.483,90 (+0,45), diciembre −0,35. Celda 12: B2B 21.312,05 (8 líneas), Web 11.431,60, App 8.193,80. Celda 13: `Upper limit: 2165.16`; B2B 36 de 61, App 0 de 451, Web 0 de 816.

**Razonamiento profesional:** el ticket promedio se calcula por pedido y no por línea. El IQR va sobre el logaritmo porque los importes tienen sesgo a la derecha. Cada pico se explica antes de concluir nada. Error típico: celebrar junio como "crecimiento" sin ver que son tres clientes, o borrar los 36 outliers y perder casi todo el negocio B2B.

> 🟢 Let's see these patterns in charts.

---

## F. 21:00–22:30 — Visualizaciones

> 🟢 Section seven: visualizations.

> 🖱️ I'm scrolling down below the table, and clicking the plus Code button in the toolbar at the top left, to add the fourteenth code cell.

> 🟢 This fourteenth code cell draws two charts side by side: monthly revenue as a line with Matplotlib, and the order value by channel as a Seaborn box plot on a log scale.

> 🖱️ I'm typing the charts in the fourteenth code cell.

> ⌨️ A line chart fits a trend over time. A box plot fits a comparison of distributions, and the log scale lets small and large orders share the same chart.

**Celda 14:**

```python
# 7. Visualizations
fig, ax = plt.subplots(1, 2, figsize=(13, 4))
monthly.plot(ax=ax[0], marker="o", title="Monthly revenue ($)")
sns.boxplot(data=order_val, x="channel", y="line_total", log_scale=True, ax=ax[1]).set_title("Order value by channel ($)")
plt.show()
```

📘 **Qué hace cada línea** (para vos, no se lee):

- `# 7. Visualizations`: comentario de sección.
- `fig, ax = plt.subplots(1, 2, figsize=(13, 4))`: crea una figura con dos gráficos lado a lado (1 fila, 2 columnas), de 13 × 4 pulgadas.
- `monthly.plot(ax=ax[0], marker="o", title="Monthly revenue ($)")`: gráfico de líneas del ingreso mensual en el primer espacio, con un punto en cada mes.
- `sns.boxplot(data=order_val, x="channel", y="line_total", log_scale=True, ax=ax[1]).set_title(...)`: boxplot de Seaborn del valor de pedido por canal, en escala logarítmica, en el segundo espacio y con su título.
- `plt.show()`: muestra la figura.

> 🖱️ I'm clicking the Run cell button on the left of the fourteenth code cell, to draw the charts.

> 🖱️ I'm pointing at the June peak on the line chart, on the left.

> 🟢 The June spike from the hotel orders, the dip in July, and the November peak.

> 🖱️ I'm moving the mouse across the three boxes of the box plot, on the right.

> 🟢 Web and App have similar boxes, mostly between about 90 and 300 dollars. B2B sits much higher: its median order is more than ten times larger. That's the visual reason to treat it as a separate segment.

**Resultado esperado:** dos gráficos. Izquierda: línea con pico en junio (≈ 41 mil), bajada en julio y máximo en noviembre (≈ 69 mil). Derecha: tres cajas en escala logarítmica, con B2B muy por encima de Web y App.

> 🟢 Before I export anything, let's validate the totals.

---

## G. 22:30–24:30 — Validación

> 🟢 Section eight: validation.

> 🖱️ I'm scrolling down below the charts, and clicking the plus Code button in the toolbar at the top left, to add the fifteenth code cell.

> 🟢 This fifteenth code cell compares a naive join of the raw files with the raw line totals, checks that no line was lost or duplicated, checks that the categories add up to total revenue, and breaks the raw total into completed, cancelled, and lines without an order.

> 🖱️ I'm typing the validation in the fifteenth code cell.

> ⌨️ The naive join is what someone would get by joining the original files directly, with the duplicates.

**Celda 15:**

```python
# 8. Validation
print("Naive join:", items.merge(orders, on="order_id")["line_total"].sum().round(2), "| raw lines:", items["line_total"].sum().round(2))
print("Rows in:", len(items), "| rows out:", len(clean), "| category total:", rev.groupby("category")["line_total"].sum().sum().round(2))
clean.groupby(clean["status"].fillna("order not found"))["line_total"].sum().round(2)
```

📘 **Qué hace cada línea** (para vos, no se lee):

- `# 8. Validation`: comentario de sección.
- `print("Naive join:", items.merge(orders, on="order_id")["line_total"].sum().round(2), "| raw lines:", items["line_total"].sum().round(2))`: el total de un join directo entre los archivos originales (con los duplicados), contra la suma de las líneas originales.
- `print("Rows in:", len(items), "| rows out:", len(clean), "| category total:", ...)`: filas de entrada y de salida, y la suma de los ingresos por categoría.
- `clean.groupby(clean["status"].fillna("order not found"))["line_total"].sum().round(2)`: divide el total original por estado: completado, cancelado y sin pedido.

> 🖱️ I'm clicking the Run cell button on the left of the fifteenth code cell, to validate.

> 🖱️ I'm pointing at the first line of the output.

> 🟢 The naive join gives 465,624.75 dollars, but the raw line totals are only 460,712.85. The naive join is about 4,900 dollars too high, only because of the 20 duplicate orders. That alone could explain part of finance's mismatch.

> 🖱️ I'm pointing at the second line.

> 🟢 3,061 lines in and 3,061 lines out: no line lost or duplicated. And the category total, 433,779.55, equals the revenue, so the grouping is consistent.

> 🖱️ I'm moving the mouse down the three totals at the bottom.

> 🟢 And the raw total reconciles exactly: 433,779.55 completed, plus 26,538.30 cancelled, plus 395 dollars in lines without an order, adds up to 460,712.85. My corrections didn't change any line total, so nothing was forced to match. The only unresolved items are the six mismatches, the eight P025 lines, and the five lines without an order.

**Resultado esperado:** `Naive join: 465624.75 | raw lines: 460712.85`; `Rows in: 3061 | rows out: 3061 | category total: 433779.55`; cancelled 26.538,30 · completed 433.779,55 · order not found 395,00.

**Razonamiento profesional:** la validación muestra **dónde** está cada dólar del total original, no solo que "da bien". La diferencia del join ingenuo cuantifica el costo de no sacar los duplicados. Error típico: validar solo que el código no tire error, o comparar el total final con el original y "ajustar" hasta que coincidan.

> 🟢 Everything is validated. Let's export the deliverables.

---

## H. 24:30–27:30 — Entregables y conclusiones

> 🟢 Section nine: deliverables and conclusions.

> 🖱️ I'm scrolling down below the output, and clicking the plus Code button in the toolbar at the top left, to add the sixteenth code cell.

> 🟢 This sixteenth code cell exports the clean dataset, and an exception report with every line that was corrected, has an exception, or is out of revenue.

> 🖱️ I'm typing the export in the sixteenth code cell.

**Celda 16:**

```python
# 9. Deliverables
clean.to_csv("clean_sales.csv", index=False)
report = clean[(clean["fix"] != "") | (clean["exception"] != "") | ~clean["in_revenue"]]
report.to_csv("exceptions_report.csv", index=False)
print(len(clean), "clean lines |", len(report), "lines in the exception report")
```

📘 **Qué hace cada línea** (para vos, no se lee):

- `# 9. Deliverables`: comentario de sección.
- `clean.to_csv("clean_sales.csv", index=False)`: guarda el dataset limpio.
- `report = clean[(clean["fix"] != "") | (clean["exception"] != "") | ~clean["in_revenue"]]`: líneas corregidas, con excepción o fuera del ingreso.
- `report.to_csv("exceptions_report.csv", index=False)`: guarda el reporte.
- `print(len(clean), "clean lines |", len(report), "lines in the exception report")`: cuántas filas tiene cada archivo.

> 🖱️ I'm clicking the Run cell button on the left of the sixteenth code cell, to export the files.

> 🖱️ I'm pointing at the output line.

> 🟢 3,061 clean lines, and 211 lines in the exception report: the 26 corrected lines, the 19 lines with an exception, and the other 166 lines of cancelled orders.

> 🖱️ I'm scrolling down to the end of the notebook, and clicking the plus Text button in the toolbar at the top left, to add the conclusions cell.

> 🟢 This last cell summarizes the data work, the business findings, and the recommendations.

> 🖱️ I'm typing the conclusions in the new text cell, at the bottom of the notebook.

```markdown
## 9. Conclusions and recommendations
- **Data:** 20 duplicate orders removed (a join would have added $4,911.90), 127 day-first dates converted, and 26 order lines corrected with evidence (12 prices in cents, 10 missing prices, 4 placeholder quantities). Unresolved: 6 line-total mismatches, 8 lines for the unknown product P025, and 5 lines without an order ($395).
- **Business:** completed revenue is $433,779.55 from 1,328 orders (AOV $326.64). Bedding leads with $112,125.95. June rose 50% because of three large B2B orders, and November is the seasonal peak (+45%).
- **Outliers:** 36 high-value orders, all B2B. They are a different customer segment, not errors.
- **Recommendations:** enforce one date format and prices in dollars in the export, block the 999 quantity, add P025 to the catalog, and report B2B separately.
- **Final notes:** the three input files are synthetic and were generated by Gemini before recording.
```

Ver "Pendientes": la nota final tiene que ser **cierta**.

> 🖱️ I'm clicking the empty area below the conclusions cell, to close the editor and show the formatted text.

> 🖱️ I'm pressing Command + S to save the notebook in Drive.

> 🖱️ I'm opening the File menu at the top left, choosing Download, then Download .ipynb, to keep the notebook for the deliverables.

> 🖱️ I'm clicking the Files icon in the left sidebar, then the three dots next to clean_sales.csv, and choosing Download.

> 🖱️ I'm clicking the three dots next to exceptions_report.csv, in the same panel, and choosing Download.

> 🖱️ I'm double-clicking exceptions_report.csv in the Files panel, to open it in Colab's file viewer.

Si Colab no abre un visor, agregá una celda con `report.head()` y mostrá la tabla.

> 🖱️ I'm scrolling right across the columns of the report, to the fix, exception, and in_revenue columns at the end.

> 🟢 Each line says why it's in the report, with its original price and quantity next to the corrected ones, so anyone can audit every change.

> 🖱️ I'm closing the file viewer tab at the top, and clicking the Downloads arrow at the top right of Firefox, to show the notebook and the two CSV files.

> 🖱️ I'm clicking an empty area of the page, to close the Downloads panel.

**Resultado esperado:** `3061 clean lines | 211 lines in the exception report`. En Descargas: `sales_analysis.ipynb`, `clean_sales.csv` y `exceptions_report.csv`.

---

## I. 27:30–30:30 — Epílogo

Dura **menos de 4 minutos**. No repitas los pasos: reflexioná.

> 🖱️ I'm scrolling up slowly through the notebook with the mouse wheel, in the center of the screen.

> 🟢 Let me reflect on this work. The most important finding is about the data itself: the export had 20 duplicate orders, and a simple join would have overstated revenue by almost 5,000 dollars. That's the kind of error that makes finance and sales disagree, and nobody sees it in a chart.

> 🟢 The key decision was to treat every anomaly as a question first. The same filter showed prices in cents, which were errors, and hotel orders of 100 units, which were real. The evidence decided, not the size of the number. And when there was no evidence, like the six totals that don't match, I didn't correct anything. I documented them.

> 🟢 For the business, the clean data changes the story. Bedding leads revenue, but Bath sells the most units. June's jump wasn't demand, it was three hotel orders. And B2B is a different segment, with orders more than ten times larger, so it should be reported and forecast separately.

> 🟢 There are limits. The data is synthetic and covers only one year, so I can't confirm that November is a repeating season. I can't resolve the six mismatches or identify product P025 without the source systems. And I don't have costs by line, so this is a revenue analysis, not a profit analysis.

> 🟢 The deliverables are the clean dataset, with original values and a label for every correction, the exception report, the two charts, and this reproducible notebook. As next steps, I'd send the exception report to the sales operations team, fix the export at the source, and add margin analysis using the catalog costs. Thanks for watching!

Si el reloj todavía no pasó los 15:00 (no debería pasar), no cortes: volvé a la celda 9 y compará categoría por categoría.

---

## Si algo sale mal (frases para corregir)

Siempre decí **qué** corregís y **en qué celda**:

| Error | Qué pasa | Qué decís y hacés |
| ----- | -------- | ----------------- |
| `MergeError` en la celda 7 | El `validate="m:1"` encontró duplicados: la celda 5 no se ejecutó | 🖱️ *"The validate check stopped the join, because the orders still have duplicates. That's the protection working. I'm running the fifth code cell again, and then this one."* |
| `KeyError` con una columna | Nombre mal escrito (por ejemplo `price_ration`) | 🖱️ *"There's a KeyError in this cell, because I misspelled price_ratio. I'm fixing the name and clicking Run again."* |
| `NameError` (`li`, `o`, `clean`, `rev`) | Una celda anterior no se ejecutó | 🖱️ *"There's a NameError, because an earlier cell didn't run. I'm opening the Runtime menu at the top and choosing Run before."* |
| `FileNotFoundError` en la celda 1 | Los CSV no se subieron o se borraron al reiniciar | 🖱️ *"The first code cell can't find the files. I'm opening the Files panel on the left, uploading the three CSV files again, and running the cell again."* |
| Error en `log_scale` (celda 14) | Seaborn antiguo | 🖱️ *"This Seaborn version doesn't support log_scale. I'm removing it and adding ax[1].set_yscale("log") on the next line."* |
| La celda 6 se ejecutó dos veces | Los precios en centavos se dividen otra vez por 100 | 🖱️ *"I ran the sixth code cell twice, so the cents prices were divided again. I'm opening the Runtime menu and choosing Run before, and then running this cell once."* |
| Un número distinto del guion | Otra versión de pandas o una celda corrida dos veces | Decí el número que ves. No digas números que no estén en pantalla. |

---

## Línea de tiempo estimada

| Sección | Tiempo | Duración |
| ------- | ------ | -------- |
| A. Apertura (intro de menos de 20 s + subir archivos + plan) | 0:00–2:00 | 2:00 |
| B. Carga y perfil (celdas 1–2) | 2:00–5:30 | 3:30 |
| C. Investigación de anomalías (celdas 3–4) | 5:30–9:30 | 4:00 |
| D. Transformación y conciliación (celdas 5–8) | 9:30–15:00 | 5:30 |
| E. Análisis de negocio y outliers (celdas 9–13) | 15:00–21:00 | 6:00 |
| F. Visualizaciones (celda 14) | 21:00–22:30 | 1:30 |
| G. Validación (celda 15) | 22:30–24:30 | 2:00 |
| H. Entregables y conclusiones (celda 16 + texto) | 24:30–27:30 | 3:00 |
| I. Epílogo | 27:30–30:30 | 3:00 |

Con mucho tipeo, la grabación probablemente pase de 30 minutos. Ver "Pendientes".

---

## Después de grabar

1. Abrí TaskRecorder **solo cuando terminó el epílogo**.
2. Ejecutá **Run full AutoQC**, no solo *Rerun failing*. Revisá que el porcentaje de acciones con What + Where pase el **70%** y mirá el porcentaje de tipeo.
3. Armá **Deliverables.zip** con el `.ipynb` descargado al final, `clean_sales.csv`, `exceptions_report.csv` y los **tres CSV originales** (sin modificar).
4. Subí los **cuatro archivos por separado**: el **MP4**, el **ZIP original de TaskRecorder**, **Deliverables.zip** y **Metadata.rtf**.
