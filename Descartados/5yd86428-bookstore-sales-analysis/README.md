# 5yd86428 — Bookstore Sales Analysis

Guion para grabar la tarea **5yd86428**: como data analyst de una librería online ficticia, analizás en **Google Colab** un dataset sintético de 200 ventas, con **pandas** y **Matplotlib**, para encontrar las categorías que más facturan, la tendencia mensual y las transacciones inusuales. Se graba en **Firefox**, en **una sola toma**. La grabación tiene que durar **entre 15:00 y 50:59**. Este guion apunta a unos **24 minutos**, epílogo incluido (la grabación anterior duró ~35).

### Cambios en esta versión

| Problema de la versión anterior | Qué cambió |
| ------------------------------- | ---------- |
| Solo 40,9% de acciones con What + Where (mínimo 70%) | **Todas** las interacciones tienen su frase 🖱️ con **qué** hacés y **dónde** está: cada clic, scroll, celda nueva, tipeo, ejecución, resultado señalado, guardado y corrección |
| 04:06: al abrir el CSV no se dijo dónde estaba | *"…in the left panel, above the file list"* |
| 09:08: al agregar una celda no se describió el scroll ni el botón | Cada celda nueva arranca con *"I'm scrolling down to the end of… and clicking the plus Code button in the toolbar at the top left…"* |
| Se explicaba el código línea por línea (11 bloques *What each line does*) | El código es **mínimo** (de 1 a 5 líneas por celda) y se explica con **una** frase por celda |
| Consulta a la documentación de pandas y Matplotlib en Firefox | **Eliminada.** Todo pasa en Colab |
| El dataset no seguía los pasos aprobados (`bookstore_sales.csv`, con `category`, `quantity`, `unit_price`; sin `title` ni `total revenue`) | `sales_data.csv` (6 columnas aprobadas) se **prepara antes de grabar** y en el paso 1 se sube a Colab |
| Etapa de limpieza (duplicados, faltantes, categorías mal escritas) que no está en los pasos aprobados | **Eliminada** |
| Las estadísticas eran solo del total | Ahora son de `total revenue` **y** `units sold` |
| Introducción de más de un minuto, empezando en 00:51 | Menos de 20 segundos, desde el inicio |
| El notebook entregado no estaba actualizado | Se guarda y se descarga **al final de la grabación**, después de las conclusiones |

Además, según el prompt de grabación:

- La **introducción** dura menos de 20 segundos y se dice con la **descripción de la tarea en pantalla**. Después minimizás esa ventana y, desde el Dock, abrís la ventana de Firefox con Colab y el notebook vacío ya creado.
- Cada **atajo de teclado** se dice en voz alta (`Cmd + S`).
- El **epílogo** (2 a 4 minutos) resume el enfoque, los **desafíos** y las reflexiones.

### Los 7 pasos aprobados y dónde están

| Paso | Dónde |
| ---- | ----- |
| 1. `sales_data.csv` preparado antes de grabar (`date`, `book category`, `title`, `units sold`, `unit price`, `total revenue`) | Subida en el panel Files + celda 1 (imports) |
| 2. `pd.read_csv()`, `head()`, `info()`, `shape` | Celdas 2 y 3 |
| 3. mean, median, std, min, max de revenue y units sold | Celda 4 |
| 4. `groupby()` por categoría y por mes | Celdas 5 y 6 |
| 5. Bar chart de revenue by category + histogram de transaction amounts | Celdas 7 y 8 |
| 6. Outliers en `total revenue` con IQR, mostrando las transacciones | Celda 9 |
| 7. Conclusiones: categoría principal, mejor mes, outliers | Última celda de texto |

**Cómo leer este guion:**

- 🖱️ = lo decís **mientras hacés** la acción. Siempre dice **qué** hacés y **dónde** está en la pantalla. Son las frases que cuenta AutoQC: **no te saltees ninguna**.
- 🟢 = explicación corta, entre una acción y otra.
- El texto en castellano es lo que hacés en pantalla. No se lee.
- Si usás un **atajo de teclado**, decí la tecla en voz alta: *"I'm pressing Command + S"*.
- **No expliques el código línea por línea.** Cada celda tiene **una** frase 🟢 que dice para qué sirve, y la decís antes de escribirla.
- **Todas las celdas son de código**, salvo la última (conclusiones), que es de texto. El título de cada paso **no se escribe**: lo decís en voz alta (*"Step two: load and inspect the data"*).
- Toda celda sigue el mismo ciclo, y cada paso tiene su frase: **decir el título del paso → scroll hasta el final → clic en + Code → escribir el código → clic en Run → señalar el resultado → explicarlo.**

> **Importante:** el Goal de Studio tiene prioridad sobre este guion. Si Studio trae un CSV propio en **Starting materials**, usalo y adaptá los nombres de las columnas.

---

## Archivos de la carpeta

```
5yd86428-bookstore-sales-analysis/
├── README.md                       ← este guion
├── sales_data.csv                  ← el dataset sintético, preparado antes de grabar (archivo de entrada)
└── bookstore_sales_analysis.ipynb  ← notebook de referencia, completo y en orden
```

Para probar el notebook de referencia: en Colab, **File → Upload notebook → Browse**, elegís `bookstore_sales_analysis.ipynb`, subís `sales_data.csv` en el panel **Files** y ejecutás **Runtime → Run all**.

---

## El dataset

`sales_data.csv` tiene 200 ventas **sintéticas** de 2025, preparadas **antes de grabar**, como dice la idea aprobada. En el video no se muestra cómo se generó: se sube y se analiza. Los números coinciden con las tablas de este guion.

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
2. En **Firefox**, dejá **dos ventanas**: la primera con la **descripción de la tarea**, en pantalla, porque con ella arranca la grabación. La segunda con **Google Colab** (https://colab.research.google.com) y el notebook ya creado: **File → New notebook in Drive**, con el nombre `bookstore_sales_analysis` y la **celda de código vacía** que Colab crea sola. Revisá que, al hacer clic en el ícono de Firefox en el **Dock (a la derecha)**, Colab aparezca en la **segunda línea** de la lista.
3. Tené `sales_data.csv` en el **Escritorio**, porque lo subís durante la grabación.
4. Maximizá la ventana de Colab y agrandá el zoom (`Cmd + +`) para que el código se lea.
5. Practicá una vez entera en voz alta con cronómetro.
6. Ejecutá las celdas con el **botón Run** (mouse), no con el teclado, así cada ejecución tiene su frase.
7. Nunca más de 45 segundos en silencio. Si Colab te sugiere código (Gemini), ignoralo y seguí escribiendo vos.
8. Salvo la descripción de la tarea del principio, no muestres Studio, Mercor, datos personales ni herramientas de IA.

---

## 0:00–1:00 — Introducción y abrir Colab en Firefox

Empezás con la **descripción de la tarea** en pantalla. La introducción dura **menos de 20 segundos**:

> 🟢 I will be beginning my task soon. As a data analyst for an online bookstore, I'll analyze 200 synthetic sales in Google Colab with pandas and Matplotlib: statistics, categories, months, two charts, outliers, and conclusions.

> 🖱️ I'm clicking the yellow minimize button at the top left of this Firefox window, to put the task description away.

> 🖱️ I'm clicking the Firefox icon in the Dock, on the right side of the screen, to see my open Firefox windows.

> 🖱️ I'm clicking the second line of the list, the Google Colab window, to open my notebook.

> 🖱️ I'm pointing at the notebook name, bookstore_sales_analysis, at the top left next to the Colab logo. I created this empty notebook before starting.

> 🖱️ I'm pointing at the empty code cell at the top of the notebook, where I'll type the imports.

---

## 1:00–3:30 — Paso 1: subir `sales_data.csv` e importar las librerías

> 🟢 Step one: the dataset. I prepared this synthetic dataset with 200 fictional bookstore sales before starting the analysis. Now I'm uploading the CSV file into Google Colab to begin exploring the data.

> 🖱️ I'm clicking the Files icon, the folder in the left sidebar, to open the file panel.

> 🖱️ I'm clicking the Upload to session storage button, the page with an up arrow in the left panel, above the file list, to choose the CSV.

> 🖱️ In the file window, I'm clicking Desktop in the list on the left, then sales_data.csv, and then the Open button at the bottom right of the window.

Si aparece el aviso de que los archivos se borran al reiniciar el runtime:

> 🖱️ I'm clicking OK on the warning in the center of the screen. It only says the uploaded files are deleted when the runtime restarts.

> 🖱️ I'm pointing at sales_data.csv in the left panel, in the file list, to show it's uploaded and ready to be read.

> 🖱️ I'm clicking the Files icon in the left sidebar again, to close the panel and get the space back.

> 🖱️ I'm clicking inside the empty code cell at the top of the notebook, to start typing in it.

> 🟢 This first code cell imports pandas, for the table, and Matplotlib, for the charts.

> 🖱️ I'm typing the two imports in the first code cell, in the middle of the screen.

**Celda 1:**

```python
import pandas as pd
import matplotlib.pyplot as plt
```

> 🖱️ I'm clicking the Run cell button, the play icon on the left edge of the first code cell, to import the libraries.

> 🖱️ I'm pointing at the status at the top right of Colab, which turns green when the runtime is connected.

> 🟢 The first run takes a few seconds, because Colab is connecting to a runtime. There's no output under the cell, which means the imports worked.

---

## 3:30–6:30 — Paso 2: cargar e inspeccionar

> 🟢 Step two: load and inspect the data.

> 🖱️ I'm scrolling down to the end of the first code cell, and clicking the plus Code button in the toolbar at the top left, to add the second code cell below it.

> 🟢 This second code cell reads the CSV with read_csv and shows the first five rows with head.

> 🖱️ I'm typing the code in the second code cell, in the middle of the screen.

**Celda 2:**

```python
df = pd.read_csv("sales_data.csv")
df.head()
```

> 🖱️ I'm clicking the Run cell button on the left of the second code cell, to load the data.

> 🖱️ I'm moving the mouse across the column headers of the table, below the second code cell, from left to right, to show the six columns.

> 🟢 Each row is one sale: the date, the book category, the title, units sold, unit price, and total revenue.

> 🖱️ I'm pointing at the first row of the table, the one with index zero, on the left.

> 🟢 The first sale, on January 1st, is two copies of The Money Mind at $20.15, so $40.30.

> 🖱️ I'm scrolling down below the table, and clicking the plus Code button in the toolbar at the top left, to add the third code cell.

> 🟢 This third code cell checks the structure of the table: info lists the columns, the non-empty values, and the data types, and shape gives the number of rows and columns.

> 🖱️ I'm typing info and shape in the third code cell.

**Celda 3:**

```python
df.info()
df.shape
```

> 🖱️ I'm clicking the Run cell button on the left of the third code cell, to see the structure.

> 🖱️ I'm pointing at the Non-Null Count column in the info output, in the middle of the screen.

> 🟢 All six columns have 200 non-null values, so nothing is missing.

> 🖱️ I'm moving the mouse down the Dtype column, on the right of the info output.

> 🟢 units sold is a whole number, unit price and total revenue have decimals, and date, book category, and title are text.

> 🖱️ I'm pointing at the last line of the output, at the bottom of the third code cell.

> 🟢 The shape confirms 200 rows and 6 columns.

Según la versión de pandas, el texto aparece como `object` o como `str`. Si dice `object`, decí *"object means text"*.

---

## 6:30–8:30 — Paso 3: estadísticas descriptivas

> 🟢 Step three: descriptive statistics.

> 🖱️ I'm scrolling down to the end of the third code cell, and clicking the plus Code button in the toolbar at the top left, to add the fourth code cell.

> 🟢 This fourth code cell calculates the mean, median, standard deviation, minimum, and maximum of total revenue and units sold.

> 🖱️ I'm typing the code in the fourth code cell, in the middle of the screen.

**Celda 4:**

```python
df[["total revenue", "units sold"]].agg(["mean", "median", "std", "min", "max"]).round(2)
```

> 🖱️ I'm clicking the Run cell button on the left of the fourth code cell, to calculate the statistics.

> 🖱️ I'm moving the mouse down the total revenue column of the result table, below the fourth code cell.

> 🟢 The average sale is $36.25, and the median is $32.

> 🖱️ I'm pointing at the max row, at the bottom of the total revenue column.

> 🟢 The maximum, $294.15, is far above the rest, so a few large orders pull the average above the median.

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

## 8:30–12:00 — Paso 4: `groupby()` por categoría y por mes

> 🟢 Step four: sales by category and by month.

> 🖱️ I'm scrolling down to the end of the statistics table, and clicking the plus Code button in the toolbar at the top left, to add the fifth code cell, for the categories.

> 🟢 This fifth code cell groups the sales with groupby on book category, adds up the revenue of each one, and sorts them from highest to lowest.

> 🖱️ I'm typing the code in the fifth code cell, in the middle of the screen.

**Celda 5:**

```python
by_category = df.groupby("book category")["total revenue"].sum().sort_values(ascending=False).round(2)
by_category
```

> 🖱️ I'm clicking the Run cell button on the left of the fifth code cell, to compare the categories.

> 🖱️ I'm pointing at the first two rows of the result, Fiction and Non-Fiction, at the top.

> 🟢 Fiction leads, with $2,217.60, followed by Non-Fiction, with $1,705.65.

> 🖱️ I'm pointing at the last row, Children, at the bottom of the result.

> 🟢 Children has the lowest revenue, $695.74, because children's books are the cheapest.

> 🖱️ I'm scrolling down to the end of the category result, and clicking the plus Code button in the toolbar at the top left, to add the sixth code cell, for the months.

> 🟢 This sixth code cell takes the year and month from the first seven characters of the date, and adds up the revenue of each month with groupby.

> 🖱️ I'm typing the code in the sixth code cell, in the middle of the screen.

**Celda 6:**

```python
df["month"] = df["date"].str[:7]
by_month = df.groupby("month")["total revenue"].sum().round(2)
by_month
```

> 🖱️ I'm clicking the Run cell button on the left of the sixth code cell, to compare the months.

> 🖱️ I'm moving the mouse down the revenue values, to the last two rows, 2025-11 and 2025-12, at the bottom of the result.

> 🟢 December is the best month by far, with $1,772.37, and November is second, with $898.34. That's the holiday season.

> 🖱️ I'm pointing at the rows for 2025-02 and 2025-10, near the top and near the bottom of the list.

> 🟢 The weakest months are February and October, with about $210 each.

| Valores esperados | |
| --- | --- |
| Por categoría (ingresos) | Fiction 2217.60 · Non-Fiction 1705.65 · History 968.31 · Comics 941.97 · Science 720.31 · Children 695.74 |
| Por mes (ingresos) | **2025-12 1772.37** · 2025-11 898.34 · 2025-07 797.89 · 2025-01 698.50 · … · 2025-10 210.72 · 2025-02 209.52 |

---

## 12:00–15:30 — Paso 5: gráficos con Matplotlib

> 🟢 Step five: charts.

> 🖱️ I'm scrolling down to the end of the month result, and clicking the plus Code button in the toolbar at the top left, to add the seventh code cell, for the bar chart.

> 🟢 This seventh code cell draws a Matplotlib bar chart of revenue by category, using the sorted result from step four, with a title and labels on both axes.

> 🖱️ I'm typing the code for the bar chart in the seventh code cell.

**Celda 7:**

```python
plt.bar(by_category.index, by_category)
plt.title("Revenue by Category")
plt.xlabel("Book category")
plt.ylabel("Total revenue ($)")
plt.show()
```

> 🖱️ I'm clicking the Run cell button on the left of the seventh code cell, to draw the bar chart.

> 🖱️ I'm pointing at the first bar, Fiction, on the left side of the chart.

> 🟢 Fiction is the tallest bar, and Non-Fiction, next to it, is clearly second.

> 🖱️ I'm moving the mouse over the other four bars, on the right side of the chart.

> 🟢 The other four categories are much lower, all under $1,000. A bar chart fits here, because I'm comparing separate groups.

> 🖱️ I'm scrolling down to the end of the bar chart, and clicking the plus Code button in the toolbar at the top left, to add the eighth code cell, for the histogram.

> 🟢 This eighth code cell draws a histogram of the transaction amounts: it splits total revenue into 20 ranges and counts the sales in each one.

> 🖱️ I'm typing the code for the histogram in the eighth code cell.

**Celda 8:**

```python
plt.hist(df["total revenue"], bins=20)
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

## 15:30–19:00 — Paso 6: outliers con el método IQR

> 🟢 Step six: outliers in total revenue, with the IQR method.

> 🖱️ I'm scrolling down to the end of the histogram, and clicking the plus Code button in the toolbar at the top left, to add the ninth code cell.

> 🟢 This ninth code cell finds outliers in total revenue with the IQR method. Q1 and Q3 are the amounts that leave a quarter and three quarters of the sales below them, and the IQR is the distance between them. Any sale more than 1.5 IQRs below Q1 or above Q3 is an outlier, and the cell shows those rows.

> 🖱️ I'm typing the IQR code in the ninth code cell, in the middle of the screen.

**Celda 9:**

```python
q1, q3 = df["total revenue"].quantile([0.25, 0.75])
iqr = q3 - q1
lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
print(f"Q1: ${q1:.2f} | Q3: ${q3:.2f} | IQR: ${iqr:.2f} | Normal range: ${lower:.2f} to ${upper:.2f}")
df[(df["total revenue"] < lower) | (df["total revenue"] > upper)]
```

> 🖱️ I'm clicking the Run cell button on the left of the ninth code cell, to find the outliers.

> 🖱️ I'm pointing at the printed line under the ninth code cell.

> 🟢 Q1 is $18.30 and Q3 is $43.99, so the IQR is $25.68. The upper limit is $82.51. The lower limit is negative, and no sale can be negative, so only very large sales can be outliers here.

> 🖱️ I'm moving the mouse over the three rows of the table, at the bottom of the output.

> 🟢 The method found 3 outlier transactions, all bulk orders. 20 copies of Captain Comet in July, for $273.40. 12 copies of The Silent River on December 10th, for $161.04.

> 🖱️ I'm pointing at the last row of the table, December 25th.

> 🟢 And 15 copies of Small Habits on December 25th, for $294.15, the largest sale of the year. They are real sales, not errors, so I keep them. Two of them are in December, but even without them December would still be the best month.

| Valores esperados | Q1 $18.30 · Q3 $43.99 · IQR $25.68 · rango $-20.22 a $82.51 · **3 outliers**: fila 90 (2025-07-24, Comics, Captain Comet, 20 × 13.67 = 273.40) · fila 174 (2025-12-10, Fiction, The Silent River, 12 × 13.42 = 161.04) · fila 194 (2025-12-25, Non-Fiction, Small Habits, 15 × 19.61 = 294.15) |
| --- | --- |

La tabla también muestra la columna `month`, que agregaste en la celda 6. Es normal.

Dato para vos (no hace falta decirlo): diciembre sin esos dos pedidos suma unos $1.317, que igual le gana a noviembre ($898).

---

## 19:00–20:30 — Paso 7: conclusiones y guardar

> 🖱️ I'm scrolling down to the end of the outlier table, and clicking the plus Text button in the toolbar at the top left, to add the conclusions cell.

> 🟢 This last cell answers the three questions of the task: the top category, the best month, and the outliers.

> 🖱️ I'm typing the conclusions in the new text cell, at the bottom of the notebook.

```markdown
## 7. Conclusions
- Top category: Fiction ($2,217.60). Second: Non-Fiction ($1,705.65).
- Best month: December 2025 ($1,772.37). Second: November ($898.34), so the holidays drive sales.
- Outliers (IQR, normal range up to $82.51): 3 bulk orders of $294.15, $273.40, and $161.04. They are real sales, so I keep them.
```

> 🖱️ I'm clicking the empty area below the conclusions cell, to close the editor and show the formatted text.

Guardás **ahora**, con todo el notebook terminado, para que el archivo entregado esté actualizado:

> 🖱️ I'm pressing Command + S to save the final version of the notebook in Drive.

> 🖱️ I'm opening the File menu at the top left of Colab, choosing Download, then Download .ipynb, to keep this final notebook for the deliverables.

> 🖱️ I'm pointing at the download at the top right of the browser, to show the notebook was downloaded.

---

## 20:30–24:00 — Epílogo

Dura **de 2 a 4 minutos**: enfoque, desafíos y reflexiones.

> 🖱️ I'm scrolling up to the top of the notebook with the mouse wheel, in the center of the screen, to go over the whole analysis.

> 🟢 Let me summarize. In step one, I uploaded sales_data.csv, the synthetic dataset of 200 bookstore sales I prepared before the analysis, with the six columns the task asks for.

> 🖱️ I'm scrolling down to the second, third, and fourth code cells, in the middle of the notebook.

> 🟢 Then I loaded it with read_csv and checked it with head, info, and shape: 200 rows, 6 columns, no missing values. The statistics showed an average sale of $36.25, with a median of $32.

> 🖱️ I'm scrolling down to the fifth and sixth code cells, the category and month results.

> 🟢 groupby showed that Fiction brings in the most revenue, and that December is the best month, with November second.

> 🖱️ I'm scrolling down to the seventh, eighth, and ninth code cells, the charts and the outliers.

> 🟢 The bar chart shows Fiction on top, and the histogram shows that most sales are small, with three lonely bars on the right. The IQR method confirmed them: 3 bulk orders.

> 🖱️ I'm scrolling down to the conclusions cell, at the bottom of the notebook.

> 🟢 About my decisions: I looked at the median next to the mean because of the large orders. And I chose IQR for outliers because it isn't pulled by the outliers themselves, the way the mean and standard deviation are.

> 🟢 There were two challenges. The column names have spaces, like total revenue, so I always had to write them in brackets and quotes, exactly as in the file. And I had to decide what to do with the bulk orders: they are real sales, not mistakes, so I kept them, and I checked that December is still the best month even without the two December orders.

> 🟢 One limit: the data is synthetic and covers only one year, so I can't tell whether the December peak repeats every year. As a next step, the bookstore could compare several years, or look at bulk orders separately, since three orders can change a whole month.

> 🟢 For the bookstore, the takeaway is simple: invest in Fiction, prepare stock for November and December, and treat bulk orders as a separate kind of customer. Thanks for watching!

Si el reloj todavía no pasó los 15:00 (no debería pasar), no cortes: recorré el resultado por mes, señalando mes por mes.

---

## Si algo sale mal (frases para corregir)

Siempre decí **qué** corregís y **en qué celda**:

| Error | Qué pasa | Qué decís y hacés |
| ----- | -------- | ----------------- |
| `KeyError` con un nombre de columna | Escribiste mal `"total revenue"` o `"units sold"` (por ejemplo, con guion bajo en vez de espacio) | 🖱️ *"There's a KeyError in the fourth code cell, because I typed total_revenue with an underscore, and the column name has a space. I'm clicking on that line, fixing the name, and clicking Run again."* |
| `NameError: name 'pd' is not defined` (o `by_category`) | Una celda anterior no se ejecutó | 🖱️ *"There's a NameError in this cell, because an earlier cell didn't run. I'm opening the Runtime menu at the top and choosing Run before, to run all the cells above it."* |
| `FileNotFoundError` en la celda 2 | El CSV no se subió, o se borró al reiniciar el runtime | 🖱️ *"The second code cell can't find the CSV, because it isn't in the session storage. I'm opening the Files panel in the left sidebar, uploading sales_data.csv again, and running this cell again."* |
| Error de sintaxis (paréntesis o comilla de menos) | `SyntaxError` | 🖱️ *"There's a syntax error in this cell, a missing parenthesis on the line Colab underlines. I'm adding it and running the cell again."* |
| Cualquier cosa fuera del guion | Un aviso, una ventana | 🖱️ *"I'm closing this notification at the bottom left, to keep working."* |

---

## Después de grabar

1. Ejecutá **Run full AutoQC**, no solo *Rerun failing*. Revisá que el porcentaje de acciones con What + Where pase el **70%**.
2. Armá **Deliverables.zip** con el `.ipynb` que descargaste **al final de esta grabación** (no uno anterior) **y** `sales_data.csv` (archivo de entrada). Antes de comprimir, abrí el `.ipynb` y confirmá que tiene la celda **7. Conclusions**.
3. Subí los **cuatro archivos por separado**: el **MP4**, el **ZIP original de TaskRecorder**, **Deliverables.zip** y **Metadata.rtf**.
