# 5yd86428 — Bookstore Sales Analysis

Guion paso a paso para grabar la tarea **5yd86428**: analizar 200 transacciones de una librería en **Google Colab** con **Python** y **pandas**. El trabajo incluye limpiar los datos, resumir las ventas por categoría y por mes, calcular estadísticas descriptivas y detectar posibles valores atípicos con el **IQR**. La grabación tiene que durar **entre 15:00 y 50:59**. Este guion apunta a unos **21 minutos**, epílogo incluido.

**Cómo leer este guion:**

- Las frases que empiezan con 🖱️ las decís **en el momento de hacer clic, desplazarte o escribir**. Siempre dicen **qué** elemento usás, **dónde** está en la pantalla y **por qué** lo usás. Son las que revisa AutoQC.
- Las frases que empiezan con 🟢 son la explicación que **decís en inglés** entre una acción y otra.
- Debajo de cada bloque de código, la lista **What each line does** explica cada línea en inglés. La leés en voz alta mientras escribís esa línea.
- El resto, en castellano, es lo que hacés en pantalla. Las traducciones aparecen entre paréntesis después de cada frase.

> **Importante:** el Goal de Studio tiene prioridad sobre este guion. Antes de grabar, revisá el apartado **Starting materials**: si Studio trae su propio CSV, usá ese y adaptá los nombres de las columnas. Si no trae nada, usá `bookstore_sales.csv` de esta carpeta. El Goal no dice qué herramienta usar: este guion usa Google Colab.

---

## Archivos de la carpeta

```
5yd86428-bookstore-sales-analysis/
├── GUION-V2.md                       ← este guion (versión nueva)
├── README.md                       ← guion anterior (sesión previa)
├── bookstore_sales.csv             ← dataset de partida: 200 transacciones (201 filas, con errores para limpiar)
└── bookstore_sales_analysis.ipynb  ← notebook de referencia, completo y en orden
```

---

## El dataset

`bookstore_sales.csv` tiene 200 transacciones **ficticias** de 2025, con 5 columnas:

| Columna | Qué contiene |
| ------- | ------------ |
| `transaction_id` | Identificador (T001 a T200) |
| `date` | Fecha de la venta |
| `category` | Fiction, Non-Fiction, Children, Science, History, Comics |
| `quantity` | Cantidad de libros |
| `unit_price` | Precio por libro, en dólares |

**Errores puestos a propósito:** 1 fila duplicada (T074), 3 transacciones sin cantidad (T023, T097, T151) y 11 formas de escribir las 6 categorías (`fiction`, `SCIENCE`, ` Comics` con un espacio adelante, etc.).

**Valores de referencia** (calculados del CSV):

| Paso | Resultado esperado |
| ---- | ------------------ |
| Inspección | 201 filas; `quantity` con 198 valores; 1 duplicado; 11 categorías distintas |
| Limpieza | `(197, 7)` y 6 categorías |
| Por categoría | Fiction 62 transacciones / 120 libros / $1.823,05 · Children 48 / 105 / $1.467,88 · Non-Fiction 39 / 58 / $1.355,93 · Science 16 / 36 / $984,53 · History 14 / 20 / $510,87 · Comics 18 / 33 / $489,58 |
| Total | $6.631,84 |
| Por mes | Máximo: diciembre ($1.071,82, 25 transacciones). Le siguen junio ($926,01) y septiembre ($896,62). Los más bajos son mayo ($182,62) y febrero ($192,80) |
| Estadísticas de `total` | count 197 · mean 33,66 · std 43,47 · min 6,86 · 25% 15,36 · 50% 22,71 · 75% 38,80 · max 507,50 |
| IQR | IQR 23,44; límites −19,80 y 73,96; **11** posibles atípicos, todos por arriba. Los 3 más grandes: T061 (25 libros infantiles, $507,50), T132 (12 de ciencia, $218,16) y T178 (15 de ficción, $178,65) |

---

## Antes de grabar

1. Leé el Goal y compará este guion con el campo **Describe your idea** de Studio.
2. Practicá una vez entera en un notebook nuevo, leyendo en voz alta las frases 🖱️ y 🟢, y cronometrá.
3. Dejá tres pestañas abiertas en Firefox, en este orden: el documento **Goal**, el sitio de pandas (https://pandas.pydata.org) y Colab (https://colab.research.google.com). Tené `bookstore_sales.csv` en una carpeta fácil de encontrar. Agrandá el zoom (`Ctrl + +`).
4. Maximizá el navegador y cerrá o minimizá las demás ventanas, para que ninguna tape a otra.
5. Pausa de ~1 segundo después de cada clic y nunca más de 45 segundos en silencio.
6. No muestres Studio, Mercor, información privada ni herramientas de IA. Cerrá este guion si está en la misma pantalla.

---

## 0:00–0:45 — Mostrar el Goal

> 🖱️ I'm on the Goal document in the first browser tab, to show what this task asks for.
>
> (Estoy en el documento del Goal, en la primera pestaña del navegador, para mostrar qué pide esta tarea.)
>
> 🟢 As a data analyst, I'll analyze 200 bookstore transactions with Python and pandas. I'll clean the data, summarize sales by category and by month, calculate descriptive statistics, and find potential outliers with the IQR method.
>
> (Como analista de datos, voy a analizar 200 transacciones de una librería con Python y pandas. Voy a limpiar los datos, resumir las ventas por categoría y por mes, calcular estadísticas descriptivas y encontrar posibles valores atípicos con el método IQR.)

---

## 0:45–4:00 — pandas, Colab y cargar los datos

> 🖱️ I'm clicking the second browser tab, at the top of the window, to show the official pandas website.
>
> (Hago clic en la segunda pestaña del navegador, arriba de la ventana, para mostrar el sitio oficial de pandas.)
>
> 🟢 pandas is the most popular Python library for working with tables of data. It can group, summarize, and clean thousands of rows with a few lines of code.
>
> (pandas es la librería de Python más popular para trabajar con tablas de datos. Puede agrupar, resumir y limpiar miles de filas con pocas líneas de código.)
>
> 🖱️ I'm clicking the third browser tab, at the top of the window, to open Google Colab.
>
> (Hago clic en la tercera pestaña del navegador, arriba de la ventana, para abrir Google Colab.)
>
> 🟢 Google Colab runs Python notebooks in the browser, and pandas is already installed.
>
> (Google Colab ejecuta notebooks de Python en el navegador, y pandas ya viene instalado.)
>
> 🖱️ I'm clicking the New notebook button at the bottom of the Open notebook dialog, to create a fresh notebook.
>
> (Hago clic en el botón New notebook, abajo del cuadro Open notebook, para crear un notebook nuevo.)
>
> 🖱️ I'm clicking the notebook title field at the top left, and typing bookstore_sales_analysis.ipynb, to identify this analysis.
>
> (Hago clic en el campo del título del notebook, arriba a la izquierda, y escribo bookstore_sales_analysis.ipynb, para identificar este análisis.)
>
> 🖱️ I'm clicking the Files icon, the folder in the left sidebar, and then the Upload to session storage icon at the top of the Files pane, and choosing bookstore_sales.csv, so the notebook can read it.
>
> (Hago clic en el ícono Files, la carpeta de la barra lateral izquierda, y después en el ícono Upload to session storage, arriba del panel Files, y elijo bookstore_sales.csv, para que el notebook pueda leerlo.)

Si aparece un aviso: *"I'm clicking OK on this warning, in the center of the screen, to continue the upload."*

> 🖱️ I'm clicking the plus Text button in the toolbar at the top left, to add a title and the goal.
>
> (Hago clic en el botón + Text de la barra de herramientas, arriba a la izquierda, para agregar un título y el objetivo.)

```markdown
# Bookstore Sales Analysis
Dataset: 200 bookstore transactions from 2025. Goal: clean the data, summarize sales by category and month, describe transaction values, and find potential outliers with the IQR method.
```

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that loads the data.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que carga los datos.)

```python
import pandas as pd

df = pd.read_csv("bookstore_sales.csv")
df.head()
```

**What each line does:**

- 🟢 `import pandas as pd`: this loads pandas with its usual short name, pd.
- 🟢 `df = pd.read_csv("bookstore_sales.csv")`: this reads the uploaded file into a DataFrame, a table called df.
- 🟢 `df.head()`: this shows the first five rows, to check the data loaded correctly.

> 🖱️ I'm clicking the Run cell button, the play icon to the left of this cell, to load the data.
>
> (Hago clic en el botón Run cell, el ícono de play a la izquierda de esta celda, para cargar los datos.)
>
> 🟢 Each row is one sale: an ID, the date, the book category, how many books, and the price of each book.
>
> (Cada fila es una venta: un ID, la fecha, la categoría del libro, cuántos libros y el precio de cada libro.)

---

## 4:00–8:30 — Inspeccionar y limpiar

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading called Inspect the data.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección llamado Inspect the data.)

Escribís `## 1. Inspect the data`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that looks for problems.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que busca problemas.)

```python
df.info()
print("Duplicate rows:", df.duplicated().sum())
print(df["category"].unique())
```

**What each line does:**

- 🟢 `df.info()`: this lists each column with its number of values and its data type. A column with fewer values than rows has missing values.
- 🟢 `print("Duplicate rows:", df.duplicated().sum())`: this counts rows that are exact copies of an earlier row.
- 🟢 `print(df["category"].unique())`: this lists every different category, to check that they're written consistently.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to inspect the data.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para inspeccionar los datos.)
>
> 🟢 There are three problems. We have 201 rows, but the quantity column has only 198 values, so three sales have no quantity. There's one duplicate row. And the categories are inconsistent: Fiction also appears in lowercase, Science in capitals, and some names have extra spaces. There are 11 spellings for only 6 categories.
>
> (Hay tres problemas. Tenemos 201 filas, pero la columna quantity tiene solo 198 valores, así que tres ventas no tienen cantidad. Hay una fila duplicada. Y las categorías son inconsistentes: Fiction también aparece en minúscula, Science en mayúsculas y algunos nombres tienen espacios de más. Hay 11 formas de escribir solo 6 categorías.)

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for cleaning.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para la limpieza.)

Escribís `## 2. Clean and prepare the data`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that cleans the data and adds new columns.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que limpia los datos y agrega columnas nuevas.)

```python
df = df.drop_duplicates()
df = df.dropna(subset=["quantity"])
df["category"] = df["category"].str.strip().str.title()
df["date"] = pd.to_datetime(df["date"])
df["total"] = df["quantity"] * df["unit_price"]
df["month"] = df["date"].dt.to_period("M")
print(df.shape)
print(df["category"].unique())
```

**What each line does:**

- 🟢 `df = df.drop_duplicates()`: this removes the duplicate row, so a sale isn't counted twice.
- 🟢 `df = df.dropna(subset=["quantity"])`: this removes the three sales with no quantity. Without the quantity, I can't know the amount of the sale, and guessing it would change the totals.
- 🟢 `df["category"] = df["category"].str.strip().str.title()`: strip removes extra spaces, and title writes each word with a capital first letter, so each category has one spelling.
- 🟢 `df["date"] = pd.to_datetime(df["date"])`: this converts the dates from text into real dates.
- 🟢 `df["total"] = df["quantity"] * df["unit_price"]`: a new column with the amount of each sale: quantity times unit price.
- 🟢 `df["month"] = df["date"].dt.to_period("M")`: a new column with the month of each sale, to group by month later.
- 🟢 `print(df.shape)` and `print(df["category"].unique())`: this checks how many rows are left and that the categories are clean.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to clean the data.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para limpiar los datos.)
>
> 🟢 Now we have 197 clean transactions and 7 columns, and exactly 6 categories.
>
> (Ahora tenemos 197 transacciones limpias y 7 columnas, y exactamente 6 categorías.)

---

## 8:30–12:30 — Ventas por categoría y por mes

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for sales by category.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para las ventas por categoría.)

Escribís `## 3. Sales by category`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that summarizes each category.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que resume cada categoría.)

```python
by_category = df.groupby("category").agg(
    transactions=("transaction_id", "count"),
    units=("quantity", "sum"),
    revenue=("total", "sum"),
).sort_values("revenue", ascending=False).round(2)
by_category
```

**What each line does:**

- 🟢 `df.groupby("category").agg(`: groupby puts together the sales of each category, and agg calculates several summaries at once.
- 🟢 `transactions=("transaction_id", "count"),`: the number of sales per category.
- 🟢 `units=("quantity", "sum"),`: the number of books sold.
- 🟢 `revenue=("total", "sum"),`: the money each category brought in.
- 🟢 `).sort_values("revenue", ascending=False).round(2)`: it sorts from highest to lowest revenue and rounds to cents.
- 🟢 `by_category`: this shows the table.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to see the categories.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para ver las categorías.)
>
> 🟢 Fiction leads, with 62 sales and about 1,823 dollars. Children is second, with about 1,468, and Non-Fiction third. Science has only 16 sales, but almost 985 dollars, because science books are expensive. Comics brings in the least.
>
> (Fiction lidera, con 62 ventas y unos 1.823 dólares. Children está segunda, con unos 1.468, y Non-Fiction tercera. Science tiene solo 16 ventas, pero casi 985 dólares, porque los libros de ciencia son caros. Comics es la que menos genera.)

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for sales by month.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para las ventas por mes.)

Escribís `## 4. Sales by month`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that summarizes each month.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que resume cada mes.)

```python
by_month = df.groupby("month").agg(
    transactions=("transaction_id", "count"),
    revenue=("total", "sum"),
).round(2)
by_month
```

**What each line does:**

- 🟢 `df.groupby("month").agg(`: this time I group the sales by month.
- 🟢 `transactions=("transaction_id", "count"), revenue=("total", "sum"),`: the number of sales and the revenue for each month.
- 🟢 `).round(2)` and `by_month`: it rounds to cents and shows the table, already in date order.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to see the monthly trend.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para ver la tendencia mensual.)
>
> 🟢 December is the best month, with 25 sales and about 1,072 dollars: the holiday season. June and September are also high, but that's mostly because of a few very large orders. February and May are the weakest months, under 200 dollars each.
>
> (Diciembre es el mejor mes, con 25 ventas y unos 1.072 dólares: la temporada de fiestas. Junio y septiembre también son altos, pero sobre todo por unos pocos pedidos muy grandes. Febrero y mayo son los meses más flojos, con menos de 200 dólares cada uno.)

---

## 12:30–16:30 — Estadísticas descriptivas y valores atípicos

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for descriptive statistics.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para las estadísticas descriptivas.)

Escribís `## 5. Descriptive statistics`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that describes the sale amounts.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que describe los montos de las ventas.)

```python
df["total"].describe().round(2)
```

**What each line does:**

- 🟢 `df["total"].describe().round(2)`: describe gives the count, the mean, the standard deviation, the minimum, the 25th, 50th, and 75th percentiles, and the maximum of the sale amounts, rounded to cents.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to see the statistics.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para ver las estadísticas.)
>
> 🟢 The average sale is about 33.66 dollars, but the median, the 50 percent line, is only 22.71. When the mean is much higher than the median, a few large values are pulling it up. The maximum, 507.50, confirms it. The standard deviation, about 43, is also large compared with the mean.
>
> (La venta promedio es de unos 33,66 dólares, pero la mediana, la línea del 50 por ciento, es de solo 22,71. Cuando el promedio es mucho más alto que la mediana, unos pocos valores grandes lo están tirando para arriba. El máximo, 507,50, lo confirma. La desviación estándar, de unos 43, también es grande comparada con el promedio.)

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for the outliers.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para los valores atípicos.)

Escribís `## 6. Outliers with the IQR method`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that finds the unusual sales.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que encuentra las ventas inusuales.)

```python
q1, q3 = df["total"].quantile([0.25, 0.75])
iqr = q3 - q1
lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
print("IQR:", round(iqr, 2), "| Lower bound:", round(lower, 2), "| Upper bound:", round(upper, 2))
outliers = df[(df["total"] < lower) | (df["total"] > upper)]
print("Potential outliers:", len(outliers))
outliers.sort_values("total", ascending=False)
```

**What each line does:**

- 🟢 `q1, q3 = df["total"].quantile([0.25, 0.75])`: the first quartile, Q1, and the third quartile, Q3: the 25th and 75th percentiles of the sale amounts.
- 🟢 `iqr = q3 - q1`: the interquartile range, the spread of the middle half of the sales.
- 🟢 `lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr`: the standard IQR rule: values more than one and a half IQRs outside the quartiles are potential outliers.
- 🟢 `print("IQR:", ...)`: this shows the IQR and the limits.
- 🟢 `outliers = df[(df["total"] < lower) | (df["total"] > upper)]`: this keeps only the sales outside the limits. The vertical bar means "or".
- 🟢 `print("Potential outliers:", len(outliers))`: how many there are.
- 🟢 `outliers.sort_values("total", ascending=False)`: this shows them from largest to smallest.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to find the outliers.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para encontrar los valores atípicos.)
>
> 🟢 The IQR is about 23.44 dollars. The lower limit is negative, so no sale can be too small. The upper limit is about 73.96 dollars, and 11 sales are above it.
>
> (El IQR es de unos 23,44 dólares. El límite inferior es negativo, así que ninguna venta puede ser demasiado chica. El límite superior es de unos 73,96 dólares, y hay 11 ventas por encima.)
>
> 🟢 The three biggest are bulk orders: 25 children's books for 507.50 dollars, 12 science books for 218.16, and 15 fiction books for 178.65. They look like orders from a school or a library. The other eight are smaller: purchases of two to four copies, many of them expensive science books.
>
> (Las tres más grandes son pedidos al por mayor: 25 libros infantiles por 507,50 dólares, 12 de ciencia por 218,16 y 15 de ficción por 178,65. Parecen pedidos de una escuela o una biblioteca. Las otras ocho son más chicas: compras de dos a cuatro ejemplares, muchas de libros de ciencia caros.)
>
> 🟢 That's why I call them potential outliers. The IQR method flags unusual values, but a person has to decide what they mean. These are real sales, not errors, so I keep them in the totals.
>
> (Por eso los llamo posibles valores atípicos. El método IQR marca los valores inusuales, pero una persona tiene que decidir qué significan. Son ventas reales, no errores, así que las dejo en los totales.)

---

## 16:30–18:00 — Hallazgos

> 🖱️ I'm clicking the plus Text button in the toolbar, to add the findings at the end of the notebook.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar los hallazgos al final del notebook.)

Mientras escribís, decí en voz alta lo que vas escribiendo:

```markdown
## 7. Findings
- **Cleaning:** 201 rows became 197 transactions. We removed 1 duplicate row and 3 rows with no quantity, and fixed 11 category spellings down to 6 categories.
- **Categories:** Fiction leads revenue (about $1,823 from 62 transactions), followed by Children (about $1,468) and Non-Fiction (about $1,356). Comics brings in the least (about $490).
- **Months:** December is the best month (about $1,072). June and September are high because of large bulk orders. February and May are the weakest months (under $200).
- **Statistics:** the average transaction is about $33.66, but the median is only $22.71, so a few large orders pull the average up.
- **Outliers:** the IQR rule flags 11 transactions above $73.96. The three biggest are bulk orders: 25 children's books ($507.50), 12 science books ($218.16), and 15 fiction books ($178.65). They are real sales, not errors, so we keep them.
```

---

## 18:00–21:30 — Epílogo (3–4 minutos)

Revisá en las reglas de Odin qué tiene que tener el epílogo y ajustá este texto si piden algo distinto.

> 🖱️ I'm opening the File menu at the top left of Colab and choosing Download, then Download .ipynb, to save the finished notebook for the deliverables.
>
> (Abro el menú File, arriba a la izquierda de Colab, y elijo Download y después Download .ipynb, para guardar el notebook terminado para los entregables.)
>
> 🖱️ I'm scrolling slowly up through the notebook with the mouse wheel, to go over the decisions I made.
>
> (Subo despacio por el notebook con la rueda del mouse, para repasar las decisiones que tomé.)
>
> 🟢 In this epilogue, I want to go over my approach. Cleaning came first, because each problem would have changed the results. The duplicate would have counted a sale twice, and the inconsistent categories would have split Fiction into two separate groups in the summary.
>
> (En este epílogo quiero repasar mi enfoque. La limpieza fue primero, porque cada problema habría cambiado los resultados. El duplicado habría contado una venta dos veces, y las categorías inconsistentes habrían dividido Fiction en dos grupos separados en el resumen.)
>
> 🟢 I calculated a total column instead of looking only at quantities, because the business cares about revenue. That showed something the quantities hide: Science sells few books, but brings in a lot of money.
>
> (Calculé una columna de total en vez de mirar solo las cantidades, porque al negocio le importan los ingresos. Eso mostró algo que las cantidades esconden: Science vende pocos libros, pero genera mucho dinero.)
>
> 🟢 The statistics and the outliers tell the same story: most sales are small, around 20 dollars, and a few bulk orders make a big difference. A single order of 507 dollars is almost half of the best month's revenue. For a small bookstore, those customers matter a lot.
>
> (Las estadísticas y los valores atípicos cuentan la misma historia: la mayoría de las ventas son chicas, de unos 20 dólares, y unos pocos pedidos grandes hacen una gran diferencia. Un solo pedido de 507 dólares es casi la mitad de los ingresos del mejor mes. Para una librería chica, esos clientes importan mucho.)
>
> 🟢 This analysis has limits: the data is fictional and covers only one year, so I can't confirm seasonal patterns. As next steps, I would compare several years, add charts for the monthly trend, and analyze bulk orders separately. For the store, two ideas stand out: prepare stock for December, and offer special deals to schools and libraries. Thanks for watching!
>
> (Este análisis tiene límites: los datos son ficticios y cubren un solo año, así que no puedo confirmar patrones de temporada. Como próximos pasos, compararía varios años, agregaría gráficos de la tendencia mensual y analizaría los pedidos al por mayor por separado. Para la tienda se destacan dos ideas: preparar el stock para diciembre y ofrecer promociones especiales a escuelas y bibliotecas. ¡Gracias por mirar!)

Si el reloj todavía no pasó los 15:00, no cortes: recorré la tabla mensual mes por mes y comentá cada valor.

---

## Después de grabar

1. Ejecutá **Run full AutoQC**, no solo *Rerun failing*.
2. Subí los **cuatro archivos por separado**: el **MP4**, el **ZIP original de TaskRecorder**, **Deliverables.zip** (con el `.ipynb` descargado) y **Metadata.rtf**.
