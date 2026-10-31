# 5yd86428 — Bookstore Sales Analysis

Guion para grabar la tarea **5yd86428**: como data analyst de una librería online ficticia, analizás en **Google Colab** un dataset sintético de 200 ventas, con **pandas** y **Matplotlib**, para encontrar las categorías que más facturan, la tendencia mensual y las transacciones inusuales. La grabación tiene que durar **entre 15:00 y 50:59**. Este guion apunta a unos **28 minutos**, epílogo incluido (la grabación anterior duró ~35).

### Cambios en esta versión

| Problema de la versión anterior | Qué cambió |
| ------------------------------- | ---------- |
| Solo 40,9% de acciones con What + Where (mínimo 70%) | Cada clic, scroll, celda nueva, ejecución, corrección y guardado tiene su frase 🖱️ con **qué** hacés y **dónde** está |
| Se explicaba el código línea por línea (11 bloques *What each line does*) | Una frase corta por **bloque** de código, que dice para qué sirve |
| Consulta a la documentación de pandas y Matplotlib en Firefox | **Eliminada.** Solo la pestaña del Goal (para la introducción) y Colab |
| El dataset no seguía los pasos aprobados (`bookstore_sales.csv`, con `category`, `quantity`, `unit_price`; sin `title` ni `total revenue`) | El paso 1 **crea** `sales_data.csv` en Colab, con las 6 columnas aprobadas |
| Etapa de limpieza (duplicados, faltantes, categorías mal escritas) que no está en los pasos aprobados | **Eliminada.** Ahorra unos 4 minutos |
| Las estadísticas eran solo del total | Ahora son de `total revenue` **y** `units sold` |
| El notebook entregado no estaba actualizado | Se guarda y se descarga **al final de la grabación**, después de las conclusiones |

### Los 7 pasos aprobados y dónde están

| Paso | Dónde |
| ---- | ----- |
| 1. Crear `sales_data.csv` (`date`, `book category`, `title`, `units sold`, `unit price`, `total revenue`) | Celda 1 |
| 2. `pd.read_csv()`, `head()`, `info()`, `shape` | Celdas 2 y 3 |
| 3. mean, median, std, min, max de revenue y units sold | Celda 4 |
| 4. `groupby()` por categoría y por mes | Celdas 5 y 6 |
| 5. Bar chart de revenue by category + histogram de transaction amounts | Celdas 7 y 8 |
| 6. Outliers en `total revenue` con IQR, imprimiendo las transacciones | Celda 9 |
| 7. Conclusiones: categoría principal, mejor mes, outliers | Última celda de texto |

**Cómo leer este guion:**

- 🖱️ = lo decís **mientras hacés** la acción. Siempre dice **qué** hacés y **dónde** está en la pantalla. Son las frases que cuenta AutoQC.
- 🟢 = explicación corta, entre una acción y otra.
- El texto en castellano es lo que hacés en pantalla. No se lee.
- **No expliques el código línea por línea.** Antes de escribir una celda decís para qué sirve. Si la celda es larga, decís la frase del bloque cuando llegás a ese bloque.

> **Importante:** el Goal de Studio tiene prioridad sobre este guion. Si Studio trae un CSV propio en **Starting materials**, usalo y adaptá los nombres de las columnas.

---

## Archivos de la carpeta

```
5yd86428-bookstore-sales-analysis/
├── README.md                       ← este guion
├── sales_data.csv                  ← el CSV que crea la celda 1 (referencia, para comparar)
└── bookstore_sales_analysis.ipynb  ← notebook de referencia, completo y en orden
```

Para probar el notebook de referencia: en Colab, **File → Upload notebook → Browse**, elegís `bookstore_sales_analysis.ipynb` y ejecutás **Runtime → Run all**. No hace falta subir el CSV: la celda 1 lo crea.

---

## El dataset

La celda 1 genera 200 ventas **sintéticas** de 2025 con una semilla fija (`5`), así que los números salen **siempre iguales** y coinciden con las tablas de este guion.

| Columna | Qué contiene |
| ------- | ------------ |
| `date` | Fecha de la venta. Noviembre y diciembre tienen más ventas, por las fiestas |
| `book category` | Fiction, Non-Fiction, Children, Science, History, Comics |
| `title` | Título del libro (2 títulos inventados por categoría) |
| `units sold` | Libros de la venta: de 1 a 3, salvo 3 pedidos grandes |
| `unit price` | Precio de cada libro, en dólares |
| `total revenue` | `units sold` × `unit price` |

Tres ventas son pedidos grandes **a propósito**, para que el IQR tenga algo que encontrar: 20, 12 y 15 libros.

Los nombres de columna tienen **espacios**, como pide la tarea. Por eso en el código siempre van entre corchetes y comillas: `df["total revenue"]`.

---

## Antes de grabar

1. Leé el Goal y comparalo con este guion.
2. Pegá el Goal en un documento de **Google Docs**, borrá el **Approval ID** y cualquier dato personal, y agrandá el texto hasta que se lea completo.
3. Dejá **solo dos pestañas** en el navegador: **1)** el documento del Goal y **2)** Colab (https://colab.research.google.com), con el cuadro **Open notebook** a la vista. Nada de documentación.
4. Maximizá el navegador y agrandá el zoom (`Ctrl + +`) para que el código se lea.
5. Practicá una vez entera en voz alta con cronómetro.
6. Ejecutá las celdas con el **botón Run** (mouse), no con el teclado, así cada ejecución tiene su frase.
7. Nunca más de 45 segundos en silencio. Si Colab te sugiere código (Gemini), ignoralo y seguí escribiendo vos.
8. No muestres Studio, Mercor, datos personales ni herramientas de IA.

---

## 0:00–1:30 — Introducción y notebook nuevo

Empezás en la **pestaña 1**, con el Goal a la vista. La introducción dura **menos de 20 segundos**:

> 🟢 I will be beginning my task soon. As a data analyst for an online bookstore, I'll analyze 200 synthetic sales in Google Colab, to find the top categories, the monthly trend, and unusual transactions.

> 🖱️ I'm pointing at the task description in the first browser tab, at the top of the window, to show the seven steps of the task.

> 🟢 The plan: create the CSV, load and inspect it, calculate statistics, group by category and month, draw two charts, find outliers with the IQR method, and write my conclusions.

> 🖱️ I'm clicking the second browser tab, at the top of the window, to switch to Google Colab.

> 🖱️ I'm clicking the New notebook button at the bottom of the Open notebook dialog, in the center of the screen, to start a blank notebook.

> 🖱️ I'm clicking the notebook name at the top left, next to the Colab logo, and typing bookstore_sales_analysis, so the file has a clear name.

> 🖱️ I'm clicking the plus Text button in the toolbar at the top left, to add a title cell above the code.

Escribís:

```markdown
# Bookstore Sales Analysis
Goal: analyze 200 synthetic sales of an online bookstore to find the top categories, the monthly trend, and unusual transactions.
```

> 🟢 This text cell holds the title and the goal, so anyone who opens the notebook knows what it's about.

Si Colab dejó una celda de código vacía arriba de todo:

> 🖱️ I'm clicking the trash icon on the right side of the empty code cell at the top, to delete it, because I don't need it.

---

## 1:30–5:30 — Paso 1: crear `sales_data.csv`

> 🖱️ I'm clicking the plus Text button in the toolbar at the top left, to add the heading for step one under the title.

Escribís `## 1. Create the dataset`.

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add the first code cell under that heading.

> 🟢 In this first code cell I'll import the libraries and build the dataset: 200 sales with the six columns the task asks for, saved as sales_data.csv.

Escribís la **celda 1**. Decí cada frase 🟢 cuando llegás a ese bloque:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rng = np.random.default_rng(5)
prices = {"Fiction": 14.99, "Non-Fiction": 18.99, "Children": 9.99,
          "Science": 24.99, "History": 21.99, "Comics": 12.99}
titles = {"Fiction": ["The Silent River", "Midnight Garden"],
          "Non-Fiction": ["Small Habits", "The Money Mind"],
          "Children": ["Leo the Brave Lion", "Stars for Mia"],
          "Science": ["Tiny Atoms", "The Living Planet"],
          "History": ["Roads of Rome", "The Long War"],
          "Comics": ["Captain Comet", "Night Patrol"]}

days = pd.date_range("2025-01-01", "2025-12-31")
weights = np.where(days.month == 12, 3, np.where(days.month == 11, 2, 1))
sales = pd.DataFrame({"date": rng.choice(days, 200, p=weights / weights.sum())})
sales["book category"] = rng.choice(list(prices), 200, p=[0.3, 0.2, 0.2, 0.1, 0.1, 0.1])
sales["title"] = [rng.choice(titles[c]) for c in sales["book category"]]
sales["units sold"] = rng.integers(1, 4, 200)
sales.loc[[40, 120, 175], "units sold"] = [20, 12, 15]
sales["unit price"] = (sales["book category"].map(prices) + rng.normal(0, 1.5, 200)).round(2)
sales["total revenue"] = (sales["units sold"] * sales["unit price"]).round(2)

sales = sales.sort_values("date")
sales.to_csv("sales_data.csv", index=False)
print("Saved sales_data.csv:", sales.shape)
```

- Al escribir los imports y la semilla:

  > 🟢 First, the imports: NumPy for random numbers, pandas for the table, and Matplotlib for the charts. The seed, 5, makes the random numbers the same every time, so the results are reproducible.

- Al escribir `prices` y `titles`:

  > 🟢 Next, the six book categories with a typical price, and two made-up titles for each one.

- Al escribir `days`, `weights` y la columna `date`:

  > 🟢 Here I pick 200 dates in 2025. December gets three times the weight and November twice, because bookstores sell more before the holidays.

- Al escribir `book category`, `title` y `units sold`:

  > 🟢 Each sale gets a category, with Fiction the most common, a title from that category, and one to three books. I'm also turning three sales into bulk orders on purpose, of 20, 12, and 15 books, so the outlier check has something real to find.

- Al escribir `unit price` y `total revenue`:

  > 🟢 The unit price varies a little around the category price, and total revenue is units sold times unit price.

- Al escribir `to_csv`:

  > 🟢 Finally, I sort the sales by date, save them as sales_data.csv without the index, and print the size.

> 🖱️ I'm clicking the Run cell button, the play icon on the left edge of this cell, to create the CSV.

> 🟢 The first run takes a few seconds, because Colab is connecting to a runtime. The status at the top right turns green when it's ready.

Salida esperada: `Saved sales_data.csv: (200, 6)`.

> 🖱️ I'm clicking the Files icon, the folder in the left sidebar, to check that the file was created.

> 🟢 Here it is: sales_data.csv, in the session storage, with 200 rows and 6 columns.

> 🖱️ I'm clicking the Files icon in the left sidebar again, to close the panel and get the space back.

---

## 5:30–9:00 — Paso 2: cargar e inspeccionar

> 🖱️ I'm scrolling down to the bottom of the notebook, below the output of the first cell, and clicking the plus Text button in the toolbar at the top left, to add the heading for step two.

Escribís `## 2. Load and inspect the data`.

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add a code cell that loads the CSV.

> 🟢 In this second code cell I read the CSV with read_csv, like any analyst would with a file they received, and show the first rows with head.

Escribís la **celda 2**:

```python
df = pd.read_csv("sales_data.csv")
df.head()
```

> 🖱️ I'm clicking the Run cell button on the left of the second code cell, to load the data.

> 🖱️ I'm moving the mouse across the column headers of the table, below the cell, to show the six columns.

> 🟢 Each row is one sale: the date, the book category, the title, units sold, unit price, and total revenue. The first sale, on January 1st, is two copies of The Money Mind at $20.15, so $40.30.

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add a third code cell for the structure of the table.

> 🟢 Now I check the structure: info lists the columns, the non-empty values, and the data types, and shape gives the number of rows and columns.

Escribís la **celda 3**:

```python
df.info()
print("Shape:", df.shape)
```

> 🟢 shape has no parentheses, because it's an attribute of the table, not a method.

> 🖱️ I'm clicking the Run cell button on the left of the third code cell, to see the structure.

> 🖱️ I'm pointing at the Non-Null Count column in the info output, in the middle of the screen.

> 🟢 All six columns have 200 non-null values, so nothing is missing. units sold is a whole number, unit price and total revenue have decimals, and date, book category, and title are text. The shape confirms 200 rows and 6 columns.

Según la versión de pandas, el texto aparece como `object` o como `str`. Si dice `object`, decí *"object means text"*.

---

## 9:00–11:30 — Paso 3: estadísticas descriptivas

> 🖱️ I'm scrolling down below the info output, and clicking the plus Text button in the toolbar at the top left, to add the heading for step three.

Escribís `## 3. Descriptive statistics`.

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add the fourth code cell.

> 🟢 Here I calculate the five statistics the task asks for, mean, median, standard deviation, minimum, and maximum, for total revenue and units sold.

Escribís la **celda 4**:

```python
df[["total revenue", "units sold"]].agg(["mean", "median", "std", "min", "max"]).round(2)
```

> 🖱️ I'm clicking the Run cell button on the left of the fourth code cell, to calculate the statistics.

> 🖱️ I'm moving the mouse down the total revenue column of the result table, below the cell.

> 🟢 The average sale is $36.25, and the median is $32. The mean is higher than the median, and the maximum, $294.15, is far above the rest, so a few large orders pull the average up.

> 🖱️ I'm moving the mouse to the units sold column, on the right of the table.

> 🟢 A typical sale is about two books, but the maximum is 20, so there are bulk orders. I'll check them later with the IQR method.

| Valores esperados | total revenue | units sold |
| ----------------- | ------------- | ---------- |
| mean | 36.25 | 2.24 |
| median | 32.00 | 2.00 |
| std | 31.34 | 1.88 |
| min | 6.90 | 1.00 |
| max | 294.15 | 20.00 |

---

## 11:30–15:30 — Paso 4: `groupby()` por categoría y por mes

> 🖱️ I'm scrolling down below the statistics table, and clicking the plus Text button in the toolbar at the top left, to add the heading for step four.

Escribís `## 4. Sales by category and by month`.

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add the fifth code cell, for the categories.

> 🟢 Now I group the sales with groupby on book category, and for each category I count the transactions, add up the units, and add up the revenue. Then I sort from the highest revenue to the lowest.

Escribís la **celda 5**:

```python
by_category = df.groupby("book category").agg(
    transactions=("title", "count"),
    units=("units sold", "sum"),
    revenue=("total revenue", "sum"),
).sort_values("revenue", ascending=False).round(2)
by_category
```

> 🖱️ I'm clicking the Run cell button on the left of the fifth code cell, to compare the categories.

> 🖱️ I'm moving the mouse down the revenue column of the result, from top to bottom.

> 🟢 Fiction leads, with $2,217.60 from 68 sales, followed by Non-Fiction, with $1,705.65. Children has as many sales as Non-Fiction, 38, but the lowest revenue, $695.74, because children's books are cheaper.

> 🖱️ I'm scrolling down below the category table, and clicking the plus Code button in the toolbar at the top left, to add the sixth code cell, for the months.

> 🟢 For the months, I first turn the date into a month column, and then group by it the same way: number of sales and total revenue.

Escribís la **celda 6**:

```python
df["month"] = pd.to_datetime(df["date"]).dt.to_period("M")
by_month = df.groupby("month").agg(
    transactions=("title", "count"),
    revenue=("total revenue", "sum"),
).round(2)
by_month
```

> 🖱️ I'm clicking the Run cell button on the left of the sixth code cell, to compare the months.

> 🖱️ I'm moving the mouse down the revenue column, to the last two rows at the bottom of the table.

> 🟢 December is the best month by far, with $1,772.37 from 43 sales, and November is second, with $898.34. That's the holiday season. The weakest months are February and October, with about $210 each.

| Valores esperados | |
| --- | --- |
| Por categoría (ventas / libros / ingresos) | Fiction 68 / 149 / 2217.60 · Non-Fiction 38 / 90 / 1705.65 · History 19 / 44 / 968.31 · Comics 23 / 69 / 941.97 · Science 14 / 29 / 720.31 · Children 38 / 68 / 695.74 |
| Por mes (ingresos) | **Dic 1772.37 (43 ventas)** · Nov 898.34 · Jul 797.89 · Ene 698.50 · … · Oct 210.72 · Feb 209.52 |

---

## 15:30–19:30 — Paso 5: gráficos con Matplotlib

> 🖱️ I'm scrolling down below the month table, and clicking the plus Text button in the toolbar at the top left, to add the heading for step five.

Escribís `## 5. Charts`.

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add the seventh code cell, for the bar chart.

> 🟢 The first chart is a bar chart of revenue by category, with Matplotlib. It uses the category table from step four, which is already sorted, so the bars go from highest to lowest.

Escribís la **celda 7**:

```python
plt.figure(figsize=(8, 4))
plt.bar(by_category.index, by_category["revenue"], color="steelblue")
plt.title("Revenue by Category")
plt.xlabel("Book category")
plt.ylabel("Total revenue ($)")
plt.show()
```

> 🖱️ I'm clicking the Run cell button on the left of the seventh code cell, to draw the bar chart.

> 🖱️ I'm pointing at the first bar, Fiction, on the left side of the chart.

> 🟢 Fiction is the tallest bar, and Non-Fiction is clearly second. The other four categories are much lower, all under $1,000. A bar chart fits here, because I'm comparing separate groups.

> 🖱️ I'm scrolling down below the bar chart, and clicking the plus Code button in the toolbar at the top left, to add the eighth code cell, for the histogram.

> 🟢 The second chart is a histogram of the transaction amounts. It splits the total revenue into 20 ranges and counts how many sales fall in each one.

Escribís la **celda 8**:

```python
plt.figure(figsize=(8, 4))
plt.hist(df["total revenue"], bins=20, color="darkorange", edgecolor="black")
plt.title("Distribution of Transaction Amounts")
plt.xlabel("Total revenue per transaction ($)")
plt.ylabel("Number of transactions")
plt.show()
```

> 🖱️ I'm clicking the Run cell button on the left of the eighth code cell, to draw the histogram.

> 🖱️ I'm pointing at the tall bars on the left side of the histogram.

> 🟢 Most sales are on the left, under about $80: the first three bars alone hold more than 160 sales.

> 🖱️ I'm moving the mouse to the right side of the chart, to the three small bars standing alone.

> 🟢 Far to the right there are three lonely bars, around $160, $270, and $290. Those are the bulk orders. Next, I'll check them with the IQR method.

---

## 19:30–23:00 — Paso 6: outliers con el método IQR

> 🖱️ I'm scrolling down below the histogram, and clicking the plus Text button in the toolbar at the top left, to add the heading for step six.

Escribís `## 6. Outliers in total revenue (IQR method)`.

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add the ninth code cell.

> 🟢 The IQR method finds outliers in total revenue. Q1 is the amount below which a quarter of the sales fall, and Q3 is the amount below which three quarters fall. The IQR is the distance between them.

> 🟢 Any sale below Q1 minus 1.5 times the IQR, or above Q3 plus 1.5 times the IQR, is an outlier. I use the IQR because the extreme sales themselves don't move it much, unlike the mean.

Escribís la **celda 9**:

```python
q1 = df["total revenue"].quantile(0.25)
q3 = df["total revenue"].quantile(0.75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
print(f"Q1: ${q1:.2f} | Q3: ${q3:.2f} | IQR: ${iqr:.2f}")
print(f"Normal range: ${lower:.2f} to ${upper:.2f}")

outliers = df[(df["total revenue"] < lower) | (df["total revenue"] > upper)]
print("Outliers found:", len(outliers))
outliers
```

- Al llegar a la línea `outliers = ...`:

  > 🟢 This filter keeps only the sales below the lower bound or above the upper bound. The vertical bar means "or".

> 🖱️ I'm clicking the Run cell button on the left of the ninth code cell, to find the outliers.

> 🖱️ I'm pointing at the printed lines under the cell.

> 🟢 Q1 is $18.30 and Q3 is $43.99, so the IQR is $25.68. The upper limit is $82.51. The lower limit is negative, and no sale can be negative, so only very large sales can be outliers here.

> 🖱️ I'm moving the mouse over the three rows of the outlier table, at the bottom of the output.

> 🟢 The method found 3 outlier transactions, all bulk orders. 20 copies of Captain Comet in July, for $273.40. 12 copies of The Silent River on December 10th, for $161.04. And 15 copies of Small Habits on December 25th, for $294.15, the largest sale of the year.

> 🟢 They are real sales, not errors, so I keep them. But they matter: two of them are in December. Even without them, December would still be the best month.

| Valores esperados | Q1 $18.30 · Q3 $43.99 · IQR $25.68 · rango $-20.22 a $82.51 · **3 outliers**: fila 90 (2025-07-24, Comics, Captain Comet, 20 × 13.67 = 273.40) · fila 174 (2025-12-10, Fiction, The Silent River, 12 × 13.42 = 161.04) · fila 194 (2025-12-25, Non-Fiction, Small Habits, 15 × 19.61 = 294.15) |
| --- | --- |

Dato para vos (no hace falta decirlo): diciembre sin esos dos pedidos suma unos $1.317, que igual le gana a noviembre ($898).

---

## 23:00–25:00 — Paso 7: conclusiones y guardar

> 🖱️ I'm scrolling down to the bottom of the notebook, below the outlier table, and clicking the plus Text button in the toolbar at the top left, to add the conclusions cell.

> 🟢 The last cell answers the three questions of the task: the top category, the best month, and the outliers.

Escribís:

```markdown
## 7. Conclusions
- **Top category:** Fiction, with $2,217.60 in revenue from 68 transactions. Non-Fiction is second, with $1,705.65.
- **Best month:** December 2025, with $1,772.37 from 43 transactions. November is second, with $898.34, so the holiday season drives sales.
- **Outliers:** the IQR method (normal range up to $82.51) found 3 bulk orders: 15 copies of Small Habits ($294.15), 20 of Captain Comet ($273.40), and 12 of The Silent River ($161.04). They are real sales, so I keep them.
```

Guardás **ahora**, con todo el notebook terminado, para que el archivo entregado esté actualizado:

> 🖱️ I'm clicking the File menu at the top left of Colab and choosing Save, to save the final version of the notebook.

> 🖱️ I'm opening the File menu at the top left again, choosing Download, then Download .ipynb, to keep this final notebook for the deliverables.

> 🖱️ I'm clicking the Files icon in the left sidebar, then the three dots next to sales_data.csv, and choosing Download, to keep the CSV too.

---

## 25:00–28:00 — Epílogo

> 🖱️ I'm scrolling up to the top of the notebook with the mouse wheel, in the center of the screen, to go over the whole analysis.

> 🟢 Let me summarize. In step one, I created a synthetic dataset of 200 bookstore sales with the six columns the task asks for, and saved it as sales_data.csv.

> 🖱️ I'm scrolling down to sections 2 and 3, in the middle of the notebook.

> 🟢 Then I loaded it with read_csv and checked it with head, info, and shape: 200 rows, 6 columns, no missing values. The statistics showed an average sale of $36.25, with a median of $32.

> 🖱️ I'm scrolling down to section 4, the category and month tables.

> 🟢 groupby showed that Fiction brings in the most revenue, and that December is the best month, with November second.

> 🖱️ I'm scrolling down to sections 5 and 6, the charts and the outliers.

> 🟢 The bar chart shows Fiction on top, and the histogram shows that most sales are small, with three lonely bars on the right. The IQR method confirmed them: 3 bulk orders.

> 🟢 About my decisions: I used a fixed seed so the results are reproducible. I looked at the median next to the mean because of the large orders. And I kept the outliers, because they are real sales, not mistakes.

> 🟢 One limit: the data is synthetic and covers only one year, so I can't tell whether the December peak repeats every year. As a next step, the bookstore could compare several years, or look at bulk orders separately, since three orders can change a whole month.

> 🟢 For the bookstore, the takeaway is simple: invest in Fiction, prepare stock for November and December, and treat bulk orders as a separate kind of customer. Thanks for watching!

Si el reloj todavía no pasó los 15:00 (no debería pasar), no cortes: recorré la tabla por mes, mes por mes.

---

## Si algo sale mal (frases para corregir)

Siempre decí **qué** corregís y **en qué celda**:

| Error | Qué pasa | Qué decís y hacés |
| ----- | -------- | ----------------- |
| `KeyError` con un nombre de columna | Escribiste mal `"total revenue"` o `"units sold"` (por ejemplo, con guion bajo en vez de espacio) | 🖱️ *"There's a KeyError in the fourth code cell, because I typed total_revenue with an underscore, and the column name has a space. I'm clicking on that line, fixing the name, and clicking Run again."* |
| `NameError: name 'pd' is not defined` (o `by_category`) | Una celda anterior no se ejecutó | 🖱️ *"There's a NameError in this cell, because an earlier cell didn't run. I'm opening the Runtime menu at the top and choosing Run before, to run all the cells above it."* |
| `FileNotFoundError` en la celda 2 | No se ejecutó la celda 1 | 🖱️ *"The second code cell can't find the CSV, because the first cell didn't run. I'm scrolling up and clicking Run on the first code cell, then running this one again."* |
| Error de sintaxis (paréntesis o comilla de menos) | `SyntaxError` | 🖱️ *"There's a syntax error in this cell, a missing parenthesis on the line Colab underlines. I'm adding it and running the cell again."* |
| Cualquier cosa fuera del guion | Un aviso, una ventana | 🖱️ *"I'm closing this notification at the bottom left, to keep working."* |

---

## Después de grabar

1. Ejecutá **Run full AutoQC**, no solo *Rerun failing*. Revisá que el porcentaje de acciones con What + Where pase el **70%**.
2. Armá **Deliverables.zip** con el `.ipynb` que descargaste **al final de esta grabación** (no uno anterior) **y** `sales_data.csv`. Antes de comprimir, abrí el `.ipynb` y confirmá que tiene la celda **7. Conclusions**.
3. Subí los **cuatro archivos por separado**: el **MP4**, el **ZIP original de TaskRecorder**, **Deliverables.zip** y **Metadata.rtf**.
