# 5yd86428 — Bookstore Sales Analysis

Guion paso a paso para grabar la tarea **5yd86428**: analizar 200 transacciones ficticias de una librería en **Google Colab**, con **Python** y **pandas**. El trabajo incluye limpiar los datos, resumir las ventas por categoría y por mes, calcular estadísticas descriptivas y detectar posibles valores atípicos con el **IQR**. La grabación tiene que durar **entre 15:00 y 50:59**. Este guion apunta a unos **24 minutos**, epílogo incluido.

**Cómo leer este guion:**

- Las frases que empiezan con 🖱️ las decís **en el momento de hacer clic, desplazarte o escribir**. Siempre dicen **qué** elemento usás, **dónde** está en la pantalla y **por qué** lo usás. Son las que revisa AutoQC.
- Las frases que empiezan con 🟢 son la explicación que **decís en inglés** entre una acción y otra.
- Debajo de cada bloque de código, la lista **What each line does** explica cada línea en inglés. La leés en voz alta mientras escribís esa línea.
- El resto, en castellano, es lo que hacés en pantalla. Las traducciones aparecen entre paréntesis después de cada frase.

> **Importante:** el Goal de Studio tiene prioridad sobre este guion. Antes de grabar, revisá el apartado **Starting materials**: si Studio trae su propio CSV, usá ese y adaptá los nombres de las columnas. Si no trae nada, usá `bookstore_sales.csv` de esta carpeta. El dataset lo armé yo: es ficticio y tiene errores puestos a propósito para limpiarlos. El Goal no dice qué herramienta usar: este guion usa Google Colab.

---

## Archivos de la carpeta

```
5yd86428-bookstore-sales-analysis/
├── README.md                       ← este guion
├── bookstore_sales.csv             ← dataset de partida: 200 transacciones (201 filas, con errores para limpiar)
└── bookstore_sales_analysis.ipynb  ← notebook de referencia, completo y en orden
```

Para probar el notebook de referencia: en https://colab.research.google.com elegís **File → Upload notebook** y seleccionás `bookstore_sales_analysis.ipynb`. Después subís `bookstore_sales.csv` desde el panel **Files** y ejecutás **Runtime → Run all**.

---

## El dataset

`bookstore_sales.csv` tiene 200 transacciones **ficticias** de una librería, del 9 de enero al 27 de diciembre de 2025. Tiene 201 filas (una está duplicada) y 5 columnas:

| Columna | Qué contiene |
| ------- | ------------ |
| `transaction_id` | Identificador de la venta (T001 a T200) |
| `date` | Fecha de la venta |
| `category` | Fiction, Non-Fiction, Children, Science, History, Comics |
| `quantity` | Cantidad de libros de la venta |
| `unit_price` | Precio de cada libro, en dólares |

**Errores puestos a propósito** (los encontrás y los limpiás durante la grabación):

| Problema | Dónde | Cómo se limpia |
| -------- | ----- | -------------- |
| Fila duplicada | La venta T074 aparece dos veces | `drop_duplicates()` |
| Valores faltantes | Sin cantidad en T023, T097 y T151 | `dropna(subset=["quantity"])` |
| Nombres inconsistentes | 11 formas de escribir 6 categorías (`fiction`, `SCIENCE`, `children`, `Non-fiction ` con espacio atrás, ` Comics` con espacio adelante) | `str.strip().str.title()` |

---

## Antes de grabar

1. Leé el Goal y compará este guion con el campo **Describe your idea** de Studio.
2. Practicá una vez entera en un notebook nuevo, leyendo en voz alta todas las frases 🖱️ y 🟢, y cronometrá.
3. Pegá el Goal en un documento de **Google Docs** y borrá el **Approval ID** y cualquier dato personal. Agrandá el texto hasta que se lea completo.
4. Dejá tres pestañas abiertas en Firefox, en este orden: el documento del **Goal**, Colab (https://colab.research.google.com) y el sitio de pandas (https://pandas.pydata.org). En Colab dejá a la vista el cuadro **Open notebook**, sin crear todavía el notebook. Tené `bookstore_sales.csv` en una carpeta fácil de encontrar, como el Escritorio. Agrandá el zoom del navegador (`Ctrl + +`).
5. Maximizá el navegador y cerrá o minimizá las demás ventanas, para que ninguna tape a otra.
6. Pausa de ~1 segundo después de cada clic y nunca más de 45 segundos en silencio.
7. No muestres Studio, Mercor, información privada ni herramientas de IA. Si Colab muestra funciones de IA (Gemini), no las uses. Cerrá este guion si está en la misma pantalla.

---

## 0:00–1:30 — El Goal y el plan

Empezás en la primera pestaña, la del **Goal**, con el texto completo y legible. La introducción dura menos de 20 segundos: la frase de apertura y el objetivo.

> 🟢 I will be beginning my task soon. Here is the workflow I have in mind.
>
> (Voy a empezar mi tarea en breve. Este es el flujo de trabajo que tengo en mente.)
>
> 🖱️ I'm on the Goal document, in the first browser tab, to show what this task asks for.
>
> (Estoy en el documento del Goal, en la primera pestaña del navegador, para mostrar qué pide esta tarea.)
>
> 🟢 As a data analyst, I'll analyze 200 bookstore transactions with Python and pandas. I'll clean the data, summarize sales by category and by month, calculate descriptive statistics, and find potential outliers with the IQR method.
>
> (Como analista de datos, voy a analizar 200 transacciones de una librería con Python y pandas. Voy a limpiar los datos, resumir las ventas por categoría y por mes, calcular estadísticas descriptivas y encontrar posibles valores atípicos con el método IQR.)

Ajustá esta frase a lo que diga tu Goal. Después contás el plan, paso por paso:

> 🟢 Here's the plan. First, I'll load the CSV file in Google Colab and inspect it, to find any problems before calculating anything.
>
> (Este es el plan. Primero, voy a cargar el archivo CSV en Google Colab e inspeccionarlo, para encontrar los problemas antes de calcular nada.)
>
> 🟢 Second, I'll clean the data and add two new columns: the total amount of each sale, and its month.
>
> (Segundo, voy a limpiar los datos y agregar dos columnas nuevas: el monto total de cada venta y su mes.)
>
> 🟢 Third, I'll summarize the sales by category and by month. Fourth, I'll describe the sale amounts with statistics, and use the IQR method to find the unusual sales.
>
> (Tercero, voy a resumir las ventas por categoría y por mes. Cuarto, voy a describir los montos de las ventas con estadísticas y usar el método IQR para encontrar las ventas inusuales.)
>
> 🟢 Finally, I'll write down my findings in the notebook, so the results are saved next to the code.
>
> (Por último, voy a anotar mis hallazgos en el notebook, así los resultados quedan guardados junto al código.)

---

## 1:30–2:30 — Colab y pandas

> 🖱️ I'm clicking the second browser tab, at the top of the window, to open Google Colab.
>
> (Hago clic en la segunda pestaña del navegador, arriba de la ventana, para abrir Google Colab.)
>
> 🟢 Google Colab is a free tool from Google that runs Python notebooks in the browser. The code runs in Google's cloud, so there's nothing to install.
>
> (Google Colab es una herramienta gratuita de Google que ejecuta notebooks de Python en el navegador. El código se ejecuta en la nube de Google, así que no hay que instalar nada.)
>
> 🖱️ I'm clicking the third browser tab, at the top of the window, to show the official pandas website.
>
> (Hago clic en la tercera pestaña del navegador, arriba de la ventana, para mostrar el sitio oficial de pandas.)
>
> 🟢 This is pandas, a free Python library for tables of data. I'll use it to load the sales, clean them, group them by category and month, and calculate the statistics. It comes already installed in Colab.
>
> (Esto es pandas, una librería gratuita de Python para trabajar con tablas de datos. La voy a usar para cargar las ventas, limpiarlas, agruparlas por categoría y por mes y calcular las estadísticas. Viene ya instalada en Colab.)
>
> 🖱️ I'm clicking the second browser tab, at the top of the window, to go back to Google Colab.
>
> (Hago clic en la segunda pestaña del navegador, arriba de la ventana, para volver a Google Colab.)

---

## 2:30–6:00 — Notebook nuevo y cargar los datos

> 🖱️ I'm clicking the New notebook button at the bottom of the Open notebook dialog, to create a fresh notebook.
>
> (Hago clic en el botón New notebook, abajo del cuadro Open notebook, para crear un notebook nuevo.)
>
> 🖱️ I'm clicking the notebook title field at the top left, and typing bookstore_sales_analysis.ipynb, to identify this analysis.
>
> (Hago clic en el campo del título del notebook, arriba a la izquierda, y escribo bookstore_sales_analysis.ipynb, para identificar este análisis.)

Subís el CSV:

> 🖱️ I'm clicking the Files icon, the folder in the left sidebar, to upload the dataset.
>
> (Hago clic en el ícono Files, la carpeta de la barra lateral izquierda, para subir el dataset.)
>
> 🖱️ I'm clicking the Upload to session storage icon, at the top of the Files pane, and choosing bookstore_sales.csv from my computer, so the notebook can read it.
>
> (Hago clic en el ícono Upload to session storage, arriba del panel Files, y elijo bookstore_sales.csv de mi computadora, para que el notebook pueda leerlo.)

Si aparece un aviso de que los archivos se borran al reiniciar el entorno: *"I'm clicking OK on this warning, in the center of the screen, to continue the upload."*

> 🖱️ I'm clicking the plus Text button in the toolbar at the top left, to add a title and the goal.
>
> (Hago clic en el botón + Text de la barra de herramientas, arriba a la izquierda, para agregar un título y el objetivo.)

```markdown
# Bookstore Sales Analysis
Dataset: 200 bookstore transactions from 2025. Goal: clean the data, summarize sales by category and month, describe transaction values, and find potential outliers with the IQR method.
```

**What each line does:**

- 🟢 `# Bookstore Sales Analysis`: the hash sign makes this the main title of the notebook.
- 🟢 `Dataset: ... Goal: ...`: this line says what the data is and what I want to find out.

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add a code cell that loads pandas and the data.
>
> (Hago clic en el botón + Code de la barra de herramientas, arriba a la izquierda, para agregar una celda de código que carga pandas y los datos.)

Escribís la **celda 1**:

```python
import pandas as pd

df = pd.read_csv("bookstore_sales.csv")
df.head()
```

**What each line does:**

- 🟢 `import pandas as pd`: this loads pandas, the library for tables of data, with its usual short name, pd.
- 🟢 `df = pd.read_csv("bookstore_sales.csv")`: read_csv reads the file I uploaded and stores it in a DataFrame called df. A DataFrame is a table with rows and columns, like a spreadsheet.
- 🟢 `df.head()`: head shows the first five rows, to check that the data loaded correctly. I don't need print, because Colab always shows the result of the last line of a cell.

> 🖱️ I'm clicking the Run cell button, the play icon to the left of this cell, to load and show the data.
>
> (Hago clic en el botón Run cell, el ícono de play a la izquierda de esta celda, para cargar y mostrar los datos.)
>
> 🟢 This is a fictional dataset I prepared for this analysis: one year of sales from a small bookstore. Like most real data, it isn't perfectly clean, so after loading it, the first step will be to inspect it and fix any problems.
>
> (Este es un dataset ficticio que preparé para este análisis: un año de ventas de una librería chica. Como pasa con casi todos los datos reales, no está perfectamente limpio, así que después de cargarlo, el primer paso va a ser inspeccionarlo y corregir los problemas.)

Señalás cada columna con el mouse, de izquierda a derecha, mientras la nombrás:

> 🟢 Each row is one sale, and there are five columns. transaction_id is the code of the sale, from T001 to T200. date is the day of the sale. category is the type of book, like Fiction or Children.
>
> (Cada fila es una venta, y hay cinco columnas. transaction_id es el código de la venta, de T001 a T200. date es el día de la venta. category es el tipo de libro, como Fiction o Children.)
>
> 🟢 quantity is how many books were sold, and unit_price is the price of each book, in dollars. There's no column with the total amount of the sale, so I'll calculate it: quantity times unit price.
>
> (quantity es cuántos libros se vendieron, y unit_price es el precio de cada libro, en dólares. No hay una columna con el monto total de la venta, así que la voy a calcular: cantidad por precio unitario.)
>
> 🟢 Notice that quantity shows 1.0 instead of 1. That's a hint: pandas uses decimal numbers when a column has empty values. I'll check that next.
>
> (Fíjense que quantity muestra 1.0 en vez de 1. Es una pista: pandas usa números decimales cuando una columna tiene valores vacíos. Lo reviso ahora.)

---

## 6:00–10:00 — Inspeccionar y limpiar los datos

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading called Inspect the data.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección llamado Inspect the data.)

Escribís `## 1. Inspect the data`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that looks for problems in the data.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que busca problemas en los datos.)

Escribís la **celda 2**:

```python
df.info()
print("Duplicate rows:", df.duplicated().sum())
print(df["category"].unique())
```

**What each line does:**

- 🟢 `df.info()`: info lists every column with how many values it has and its data type. If a column has fewer values than the number of rows, it has missing values. info prints by itself, so I don't need print.
- 🟢 `print("Duplicate rows:", df.duplicated().sum())`: duplicated marks each row that is an exact copy of an earlier row, and sum counts them.
- 🟢 `print(df["category"].unique())`: unique lists every different value in the category column, so I can see if the names are written consistently.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to inspect the data.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para inspeccionar los datos.)

Señalás cada problema con el mouse mientras lo nombrás:

> 🟢 I can see three problems. First, info shows 201 rows, but quantity has only 198 values, so three sales have no quantity. That's why the column has decimals.
>
> (Veo tres problemas. Primero, info muestra 201 filas, pero quantity tiene solo 198 valores, así que tres ventas no tienen cantidad. Por eso la columna tiene decimales.)
>
> 🟢 Second, there is one duplicate row. The file should have 200 sales, and the duplicate explains the extra row.
>
> (Segundo, hay una fila duplicada. El archivo debería tener 200 ventas, y el duplicado explica la fila de más.)
>
> 🟢 Third, the categories are inconsistent: Fiction also appears in lowercase, Science in capitals, and Comics and Non-fiction have extra spaces. There are 11 spellings for only 6 categories. If I don't fix this, pandas will count Fiction and lowercase fiction as two different groups.
>
> (Tercero, las categorías son inconsistentes: Fiction también aparece en minúscula, Science en mayúsculas, y Comics y Non-fiction tienen espacios de más. Hay 11 formas de escribir solo 6 categorías. Si no lo arreglo, pandas va a contar Fiction y fiction en minúscula como dos grupos distintos.)
>
> 🟢 Also, the date column is stored as text, not as dates. I'll convert it, so I can group by month.
>
> (Además, la columna date está guardada como texto, no como fechas. La voy a convertir, para poder agrupar por mes.)

Según la versión de pandas, el texto aparece como `object` o como `str`.

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for cleaning.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para la limpieza.)

Escribís `## 2. Clean and prepare the data`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that cleans the data and adds new columns.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que limpia los datos y agrega columnas nuevas.)

Escribís la **celda 3**:

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

- 🟢 `df = df.drop_duplicates()`: this removes the duplicate row, so the same sale isn't counted twice.
- 🟢 `df = df.dropna(subset=["quantity"])`: dropna removes the three sales with no quantity. I remove them instead of filling them, because without the quantity I can't know the amount of the sale, and guessing it would change the totals.
- 🟢 `df["category"] = df["category"].str.strip().str.title()`: strip removes the extra spaces, and title writes each word with a capital first letter, so every category has one spelling.
- 🟢 `df["date"] = pd.to_datetime(df["date"])`: to_datetime converts the dates from text into real dates.
- 🟢 `df["total"] = df["quantity"] * df["unit_price"]`: this creates a new column with the amount of each sale: quantity times unit price.
- 🟢 `df["month"] = df["date"].dt.to_period("M")`: dt gives access to date functions, and to_period with "M" turns each date into its month, like 2025-01. This only works because I converted the dates in the line above.
- 🟢 `print(df.shape)`: this shows how many rows and columns are left.
- 🟢 `print(df["category"].unique())`: this checks that the categories are consistent now.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to clean the data.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para limpiar los datos.)
>
> 🟢 Now we have 197 transactions and 7 columns: the five original ones, plus total and month. And there are exactly 6 categories. We removed one duplicate and three sales with no quantity.
>
> (Ahora tenemos 197 transacciones y 7 columnas: las cinco originales, más total y month. Y hay exactamente 6 categorías. Quitamos un duplicado y tres ventas sin cantidad.)

---

## 10:00–14:00 — Ventas por categoría y por mes

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for sales by category.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para las ventas por categoría.)

Escribís `## 3. Sales by category`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that summarizes each category.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que resume cada categoría.)

Escribís la **celda 4**:

```python
by_category = df.groupby("category").agg(
    transactions=("transaction_id", "count"),
    units=("quantity", "sum"),
    revenue=("total", "sum"),
).sort_values("revenue", ascending=False).round(2)
by_category
```

**What each line does:**

- 🟢 `by_category = df.groupby("category").agg(`: groupby puts together the sales of each category, and agg calculates several summaries at once. I store the result in by_category.
- 🟢 `transactions=("transaction_id", "count"),`: this counts the number of sales in each category.
- 🟢 `units=("quantity", "sum"),`: this adds up the number of books sold.
- 🟢 `revenue=("total", "sum"),`: this adds up the money each category brought in.
- 🟢 `).sort_values("revenue", ascending=False).round(2)`: this sorts the categories from highest to lowest revenue, and rounds to cents.
- 🟢 `by_category`: this shows the table.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to see the categories.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para ver las categorías.)
>
> 🟢 Fiction leads, with 62 sales, 120 books, and about 1,823 dollars. Children is second, with about 1,468, and Non-Fiction third, with about 1,356.
>
> (Fiction lidera, con 62 ventas, 120 libros y unos 1.823 dólares. Children está segunda, con unos 1.468, y Non-Fiction tercera, con unos 1.356.)
>
> 🟢 Science is interesting: it has only 16 sales and 36 books, but almost 985 dollars. That's because science books are expensive, about 27 dollars each, compared with about 15 for fiction. Comics brings in the least, about 490 dollars.
>
> (Science es interesante: tiene solo 16 ventas y 36 libros, pero casi 985 dólares. Es porque los libros de ciencia son caros, unos 27 dólares cada uno, contra unos 15 los de ficción. Comics es la que menos genera, unos 490 dólares.)

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for sales by month.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para las ventas por mes.)

Escribís `## 4. Sales by month`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that summarizes each month.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que resume cada mes.)

Escribís la **celda 5**:

```python
by_month = df.groupby("month").agg(
    transactions=("transaction_id", "count"),
    revenue=("total", "sum"),
).round(2)
by_month
```

**What each line does:**

- 🟢 `by_month = df.groupby("month").agg(`: this time I group the sales by the month column I created during cleaning.
- 🟢 `transactions=("transaction_id", "count"),`: the number of sales in each month.
- 🟢 `revenue=("total", "sum"),`: the revenue of each month.
- 🟢 `).round(2)`: this rounds to cents. I don't sort it, because the months are already in date order, and that's the order I want to read.
- 🟢 `by_month`: this shows the table.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to see the monthly trend.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para ver la tendencia mensual.)
>
> 🖱️ I'm moving the mouse down the revenue column, in the table under the cell, to compare the months.
>
> (Muevo el mouse por la columna revenue, en la tabla debajo de la celda, para comparar los meses.)
>
> 🟢 December is the best month, with 25 sales and about 1,072 dollars: that's the holiday season. November also has 25 sales, but less money, about 662 dollars.
>
> (Diciembre es el mejor mes, con 25 ventas y unos 1.072 dólares: es la temporada de fiestas. Noviembre también tiene 25 ventas, pero menos dinero, unos 662 dólares.)
>
> 🟢 June and September are also high, about 926 and 897 dollars, but partly because of one very large order in each month. I'll see those orders in the outlier section. February and May are the weakest months, under 200 dollars each.
>
> (Junio y septiembre también son altos, unos 926 y 897 dólares, pero en parte por un pedido muy grande en cada mes. Esos pedidos los voy a ver en la sección de valores atípicos. Febrero y mayo son los meses más flojos, con menos de 200 dólares cada uno.)

---

## 14:00–18:00 — Estadísticas descriptivas y valores atípicos

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for the statistics.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para las estadísticas.)

Escribís `## 5. Descriptive statistics`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that describes the sale amounts.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que describe los montos de las ventas.)

Escribís la **celda 6**:

```python
df["total"].describe().round(2)
```

**What each line does:**

- 🟢 `df["total"].describe().round(2)`: describe gives a summary of the sale amounts: the count, the mean, the standard deviation, the minimum, the 25th, 50th, and 75th percentiles, and the maximum. round(2) keeps two decimals, like cents.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to calculate the statistics.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para calcular las estadísticas.)

Señalás cada valor con el mouse mientras lo nombrás:

> 🟢 There are 197 sales. The mean, or average, is about 33.66 dollars. But the median, the 50 percent line, is only 22.71. The median is the middle value when the sales are sorted.
>
> (Hay 197 ventas. La media, o promedio, es de unos 33,66 dólares. Pero la mediana, la línea del 50 por ciento, es de solo 22,71. La mediana es el valor del medio cuando se ordenan las ventas.)
>
> 🟢 When the mean is much higher than the median, a few large values are pulling it up. The maximum, 507.50 dollars, confirms it. The standard deviation, which measures how far the sales usually are from the average, is about 43, which is large compared with the mean.
>
> (Cuando el promedio es mucho más alto que la mediana, unos pocos valores grandes lo están tirando para arriba. El máximo, 507,50 dólares, lo confirma. La desviación estándar, que mide cuánto se alejan normalmente las ventas del promedio, es de unos 43, que es grande comparada con el promedio.)
>
> 🟢 The 25th percentile is about 15 dollars and the 75th is about 39, so half of the sales are between those two values.
>
> (El percentil 25 es de unos 15 dólares y el 75 de unos 39, así que la mitad de las ventas están entre esos dos valores.)

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for the outliers.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para los valores atípicos.)

Escribís `## 6. Outliers with the IQR method`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that finds the unusual sales.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que encuentra las ventas inusuales.)

Escribís la **celda 7**:

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

- 🟢 `q1, q3 = df["total"].quantile([0.25, 0.75])`: this calculates the first quartile, Q1, the 25th percentile, and the third quartile, Q3, the 75th percentile.
- 🟢 `iqr = q3 - q1`: the interquartile range, or IQR, is the distance between Q3 and Q1. It's the range of the middle half of the sales.
- 🟢 `lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr`: this is the standard IQR rule. Any value more than one and a half IQRs below Q1 or above Q3 is a potential outlier.
- 🟢 `print("IQR:", ...)`: this shows the IQR and the two limits, rounded to cents.
- 🟢 `outliers = df[(df["total"] < lower) | (df["total"] > upper)]`: this keeps only the sales below the lower limit or above the upper limit. The vertical bar means "or".
- 🟢 `print("Potential outliers:", len(outliers))`: len counts how many there are.
- 🟢 `outliers.sort_values("total", ascending=False)`: this shows them from the largest to the smallest.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to find the outliers.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para encontrar los valores atípicos.)
>
> 🟢 The IQR is about 23.44 dollars. The lower limit is negative, minus 19.80, and a sale can't be negative, so no sale can be too small. The upper limit is about 73.96 dollars, and 11 sales are above it.
>
> (El IQR es de unos 23,44 dólares. El límite inferior es negativo, menos 19,80, y una venta no puede ser negativa, así que ninguna venta puede ser demasiado chica. El límite superior es de unos 73,96 dólares, y hay 11 ventas por encima.)
>
> 🖱️ I'm scrolling down through the outliers table, under the cell, to read each row.
>
> (Bajo por la tabla de valores atípicos, debajo de la celda, para leer cada fila.)
>
> 🟢 The three biggest are bulk orders: 25 children's books for 507.50 dollars in June, 12 science books for 218.16 in September, and 15 fiction books for 178.65 in December. They look like orders from a school or a library. These are the large orders that pushed June and September up.
>
> (Las tres más grandes son pedidos al por mayor: 25 libros infantiles por 507,50 dólares en junio, 12 de ciencia por 218,16 en septiembre y 15 de ficción por 178,65 en diciembre. Parecen pedidos de una escuela o una biblioteca. Son los pedidos grandes que hicieron subir junio y septiembre.)
>
> 🟢 The other eight are smaller: purchases of two to four copies, half of them expensive science books.
>
> (Las otras ocho son más chicas: compras de dos a cuatro ejemplares, la mitad de libros de ciencia caros.)
>
> 🟢 That's why I call them potential outliers. The IQR method flags unusual values, but a person has to decide what they mean. These are real sales, not errors, so I keep them in the totals.
>
> (Por eso los llamo posibles valores atípicos. El método IQR marca los valores inusuales, pero una persona tiene que decidir qué significan. Son ventas reales, no errores, así que las dejo en los totales.)

---

## 18:00–19:30 — Hallazgos

**Valores de referencia** (los calculé directamente del CSV). Compará con tu resultado antes de decirlos:

| Paso | Resultado esperado |
| ---- | ------------------ |
| Inspección | 201 filas; `quantity` con 198 valores; 1 duplicado; 11 categorías distintas |
| Limpieza | `(197, 7)` y 6 categorías: Fiction, Children, Non-Fiction, History, Comics, Science |
| Por categoría | Fiction 62 ventas / 120 libros / $1.823,05 · Children 48 / 105 / $1.467,88 · Non-Fiction 39 / 58 / $1.355,93 · Science 16 / 36 / $984,53 · History 14 / 20 / $510,87 · Comics 18 / 33 / $489,58. Total: $6.631,84 |
| Por mes | Diciembre $1.071,82 (25 ventas) · junio $926,01 · septiembre $896,62 · noviembre $662,29 (25 ventas) · mayo $182,62 y febrero $192,80 (los más bajos) |
| Estadísticas de `total` | count 197 · mean 33,66 · std 43,47 · min 6,86 · 25% 15,36 · 50% 22,71 · 75% 38,80 · max 507,50 |
| IQR | IQR 23,44; límites −19,80 y 73,96; **11** posibles atípicos, todos por arriba. Los 3 más grandes: T061 (25 libros infantiles, $507,50), T132 (12 de ciencia, $218,16) y T178 (15 de ficción, $178,65) |

En la tabla por categoría, la columna `units` aparece con decimales (`120.0`), por la misma razón que `quantity`. Es normal.

> 🖱️ I'm clicking the plus Text button in the toolbar, to add my findings at the end of the notebook.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar mis hallazgos al final del notebook.)

Mientras escribís, decí en voz alta lo que vas escribiendo:

```markdown
## 7. Findings
- **Cleaning:** 201 rows became 197 transactions. We removed 1 duplicate row and 3 rows with no quantity, and fixed 11 category spellings down to 6 categories.
- **Categories:** Fiction leads revenue (about $1,823 from 62 transactions), followed by Children (about $1,468) and Non-Fiction (about $1,356). Comics brings in the least (about $490).
- **Months:** December is the best month (about $1,072). June and September are high because of large bulk orders. February and May are the weakest months (under $200).
- **Statistics:** the average transaction is about $33.66, but the median is only $22.71, so a few large orders pull the average up.
- **Outliers:** the IQR rule flags 11 transactions above $73.96. The three biggest are bulk orders: 25 children's books ($507.50), 12 science books ($218.16), and 15 fiction books ($178.65). They are real sales, not errors, so we keep them.
```

> 🟢 To sum up: Fiction and Children bring in the most money, December is the best month, and a few bulk orders make a big difference in the totals.
>
> (Para resumir: Fiction y Children son las que más dinero generan, diciembre es el mejor mes y unos pocos pedidos al por mayor hacen una gran diferencia en los totales.)

---

## 19:30–24:00 — Epílogo (4–5 minutos)

Revisá en las reglas de Odin qué tiene que tener el epílogo y ajustá este texto si piden algo distinto.

> 🖱️ I'm opening the File menu at the top left of Colab and choosing Download, then Download .ipynb, to save the finished notebook for the deliverables.
>
> (Abro el menú File, arriba a la izquierda de Colab, y elijo Download y después Download .ipynb, para guardar el notebook terminado para los entregables.)

### Resumen paso a paso

Subís hasta el principio del notebook y vas bajando: cada frase va cuando la sección correspondiente está en pantalla. Señalá con el mouse lo que nombrás.

> 🖱️ I'm scrolling up to the top of the notebook with the mouse wheel, to go over everything we did, step by step.
>
> (Subo hasta el principio del notebook con la rueda del mouse, para repasar todo lo que hicimos, paso a paso.)
>
> 🟢 Let me summarize the whole analysis. We started with the title and the goal: clean the data, summarize sales by category and month, describe the sale amounts, and find potential outliers.
>
> (Les resumo todo el análisis. Empezamos con el título y el objetivo: limpiar los datos, resumir las ventas por categoría y por mes, describir los montos de las ventas y encontrar posibles valores atípicos.)
>
> 🟢 In the first cell, we imported pandas and loaded the CSV: one row per sale, with five columns.
>
> (En la primera celda importamos pandas y cargamos el CSV: una fila por venta, con cinco columnas.)
>
> 🖱️ I'm scrolling down to section 1, Inspect the data, to show what we found.
>
> (Bajo hasta la sección 1, Inspect the data, para mostrar lo que encontramos.)
>
> 🟢 In section 1, we inspected the data before calculating anything, and we found three problems: three sales with no quantity, one duplicate row, and 11 spellings for only 6 categories.
>
> (En la sección 1 inspeccionamos los datos antes de calcular nada, y encontramos tres problemas: tres ventas sin cantidad, una fila duplicada y 11 formas de escribir solo 6 categorías.)
>
> 🖱️ I'm scrolling down to section 2, Clean and prepare the data.
>
> (Bajo hasta la sección 2, Clean and prepare the data.)
>
> 🟢 In section 2, we fixed those problems, one line each. We also converted the dates, and added two columns: the total of each sale and its month. We went from 201 rows to 197 clean transactions.
>
> (En la sección 2 arreglamos esos problemas, con una línea para cada uno. También convertimos las fechas y agregamos dos columnas: el total de cada venta y su mes. Pasamos de 201 filas a 197 transacciones limpias.)
>
> 🖱️ I'm scrolling down to sections 3 and 4, Sales by category and Sales by month.
>
> (Bajo hasta las secciones 3 y 4, Sales by category y Sales by month.)
>
> 🟢 In sections 3 and 4, we grouped the sales. Fiction leads revenue, and Science earns a lot from few books because of its high prices. December is the best month, and February and May are the weakest.
>
> (En las secciones 3 y 4 agrupamos las ventas. Fiction lidera los ingresos, y Science gana mucho con pocos libros por sus precios altos. Diciembre es el mejor mes, y febrero y mayo son los más flojos.)
>
> 🖱️ I'm scrolling down to sections 5 and 6, Descriptive statistics and Outliers.
>
> (Bajo hasta las secciones 5 y 6, Descriptive statistics y Outliers.)
>
> 🟢 In section 5, the mean of about 34 dollars was much higher than the median of about 23, a sign of a few large sales. In section 6, the IQR method confirmed it: 11 potential outliers, all above about 74 dollars, and the three biggest are bulk orders.
>
> (En la sección 5, el promedio de unos 34 dólares fue mucho más alto que la mediana de unos 23, una señal de unas pocas ventas grandes. En la sección 6, el método IQR lo confirmó: 11 posibles atípicos, todos por encima de unos 74 dólares, y los tres más grandes son pedidos al por mayor.)
>
> 🖱️ I'm scrolling down to section 7, Findings, at the end of the notebook.
>
> (Bajo hasta la sección 7, Findings, al final del notebook.)
>
> 🟢 And finally, we wrote down the findings with the real numbers, so anyone who opens the notebook can read the results without running the code.
>
> (Y por último, anotamos los hallazgos con los números reales, así cualquiera que abra el notebook puede leer los resultados sin ejecutar el código.)

### Decisiones y próximos pasos

> 🖱️ I'm scrolling slowly up through the notebook with the mouse wheel, to go over the decisions I made.
>
> (Subo despacio por el notebook con la rueda del mouse, para repasar las decisiones que tomé.)
>
> 🟢 In this epilogue, I want to go over my approach. Cleaning came first, because each problem would have changed the results. The duplicate would have counted a sale twice, and the inconsistent categories would have split Fiction into two separate groups in the summary.
>
> (En este epílogo quiero repasar mi enfoque. La limpieza fue primero, porque cada problema habría cambiado los resultados. El duplicado habría contado una venta dos veces, y las categorías inconsistentes habrían dividido Fiction en dos grupos separados en el resumen.)
>
> 🟢 For the missing quantities, I removed the rows instead of filling them. Only three sales were affected, and inventing a quantity would invent revenue. With a bigger problem, I could fill them with the median quantity instead.
>
> (Para las cantidades faltantes, quité las filas en vez de completarlas. Solo había tres ventas afectadas, e inventar una cantidad sería inventar ingresos. Si el problema fuera más grande, podría completarlas con la cantidad mediana.)
>
> 🟢 I calculated a total column instead of looking only at quantities, because the business cares about revenue. That showed something the quantities hide: Science sells few books, but brings in a lot of money.
>
> (Calculé una columna de total en vez de mirar solo las cantidades, porque al negocio le importan los ingresos. Eso mostró algo que las cantidades esconden: Science vende pocos libros, pero genera mucho dinero.)
>
> 🟢 The statistics and the outliers tell the same story: most sales are small, around 20 dollars, and a few bulk orders make a big difference. A single order of 507 dollars is almost half of the best month's revenue. For a small bookstore, those customers matter a lot. The IQR method is a good choice here, because it uses quartiles, which aren't affected by extreme values, unlike the mean.
>
> (Las estadísticas y los valores atípicos cuentan la misma historia: la mayoría de las ventas son chicas, de unos 20 dólares, y unos pocos pedidos grandes hacen una gran diferencia. Un solo pedido de 507 dólares es casi la mitad de los ingresos del mejor mes. Para una librería chica, esos clientes importan mucho. El método IQR es una buena opción acá, porque usa cuartiles, que no se ven afectados por los valores extremos, a diferencia del promedio.)
>
> 🟢 This analysis has limits: the data is fictional and covers only one year, so I can't confirm seasonal patterns. As next steps, I would compare several years, add charts for the monthly trend, and analyze bulk orders separately. For the store, two ideas stand out: prepare stock for December, and offer special deals to schools and libraries. Thanks for watching!
>
> (Este análisis tiene límites: los datos son ficticios y cubren un solo año, así que no puedo confirmar patrones de temporada. Como próximos pasos, compararía varios años, agregaría gráficos de la tendencia mensual y analizaría los pedidos al por mayor por separado. Para la tienda se destacan dos ideas: preparar el stock para diciembre y ofrecer promociones especiales a escuelas y bibliotecas. ¡Gracias por mirar!)

Si el reloj todavía no pasó los 15:00, no cortes: recorré la tabla mensual mes por mes y comentá cada valor.

---

## Después de grabar

1. Ejecutá **Run full AutoQC**, no solo *Rerun failing*.
2. Subí los **cuatro archivos por separado**: el **MP4**, el **ZIP original de TaskRecorder**, **Deliverables.zip** (con el `.ipynb` descargado) y **Metadata.rtf**.
