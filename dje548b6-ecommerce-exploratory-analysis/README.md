# dje548b6 — E-commerce Exploratory Data Analysis

Guion paso a paso para grabar la tarea **dje548b6**: un análisis exploratorio de un dataset público de e-commerce en **Google Colab**, con **Python**, **pandas** y **Matplotlib**, en unos **15 minutos**. El código es corto a propósito: son **6 celdas y 16 líneas**, para dedicar el tiempo a explicar.

**Cómo leer este guion:**

- Las frases que empiezan con 🟢 son lo que **decís en inglés** durante la grabación.
- Debajo de cada bloque de código, la lista **What each line does** explica cada línea en inglés. La leés en voz alta mientras escribís esa línea.
- El resto, en castellano, es lo que hacés en pantalla. Las traducciones aparecen entre paréntesis después de cada frase 🟢.

> **Importante:** el Goal oficial de Mercor y las reglas de grabación de Odin tienen prioridad sobre este guion. Antes de grabar, comparalos, sobre todo el dataset y los tres gráficos. Este guion no garantiza que la tarea se apruebe ni que 15 minutos alcancen.

---

## Archivos de la carpeta

```
dje548b6-ecommerce-exploratory-analysis/
├── README.md            ← este guion: qué hacer, qué explica cada línea y qué decir en inglés
├── ecommerce_eda.ipynb  ← el notebook completo, celda por celda, listo para abrir en Colab
└── retail-orders.csv    ← copia de respaldo del dataset (descargada el 21/10/2026)
```

`ecommerce_eda.ipynb` tiene el notebook completo, punto por punto, con las celdas de texto y de código ya separadas y en orden. Para abrirlo en Colab: en https://colab.research.google.com elegís **Archivo → Subir notebook** (*File → Upload notebook*) y seleccionás `ecommerce_eda.ipynb`. Para ejecutarlo entero: **Entorno de ejecución → Ejecutar todas** (*Runtime → Run all*). En VS Code también se abre con las celdas separadas.

El código del notebook es idéntico al de este guion. Si las reglas de Odin piden escribir el código en pantalla, escribilo durante la grabación y **no lo pegues**.

---

## El dataset

**Retail Orders**, de Datanemics.

- Página: https://datanemics.com/datasets/retail-orders/
- Enlace directo al CSV: https://datanemics.com/datasets/data/retail-orders.csv
- Licencia CC0 (dominio público). Los datos son **sintéticos**: no hay clientes reales.
- 7.000 filas (líneas de pedido) y 12 columnas, del 1/1/2023 al 30/12/2024. No tiene valores faltantes.

Comprobé en el CSV que existen las tres columnas que usamos:

| Columna | Qué contiene | Dónde se usa |
| ------- | ------------ | ------------ |
| `ordered_at` | Fecha y hora del pedido, guardada como texto | Gráfico de líneas |
| `category` | apparel, beauty, electronics, grocery, home, sports | Gráfico de barras |
| `revenue_usd` | Ingreso de la línea, en dólares, ya con descuento | Los tres gráficos |

---

## Antes de grabar

1. Leé el Goal oficial y las reglas de Odin para `dje548b6`.
2. Subí `ecommerce_eda.ipynb` a Colab, ejecutalo entero y anotá tus números reales. Después practicá una vez escribiendo las celdas vos, en un notebook nuevo.
3. Dejá dos pestañas abiertas: la página del dataset y Colab. Agrandá el zoom del navegador (`Ctrl + +`).

---

## 0:00–2:00 — El objetivo y la página del CSV

Empezás con la pestaña del dataset abierta en https://datanemics.com/datasets/retail-orders/. Saludás y presentás el objetivo:

> 🟢 Hi! In this video, I'll do an exploratory data analysis of a public e-commerce dataset, using Python, pandas, and Matplotlib in Google Colab.
>
> (¡Hola! En este video voy a hacer un análisis exploratorio de un dataset público de e-commerce, usando Python, pandas y Matplotlib en Google Colab.)

Bajás despacio por la página para mostrar la descripción del dataset:

> 🟢 This is the Retail Orders dataset. It's synthetic and in the public domain, and it has 7,000 order lines from 2023 and 2024.
>
> (Este es el dataset Retail Orders. Es sintético y de dominio público, y tiene 7.000 líneas de pedidos de 2023 y 2024.)

Señalás el enlace de descarga del CSV y explicás qué es un CSV:

> 🟢 The data comes as a CSV file. CSV means comma-separated values: it's a plain text table, where each line is a row and commas separate the columns. You can download it from this link.
>
> (Los datos vienen en un archivo CSV. CSV significa valores separados por comas: es una tabla en texto plano, donde cada línea es una fila y las comas separan las columnas. Se puede descargar desde este enlace.)

Mostrás la lista de columnas y contás qué vas a buscar:

> 🟢 I want to answer three questions: which categories bring in the most revenue, how revenue changes month by month, and how revenue is distributed across order lines.
>
> (Quiero responder tres preguntas: qué categorías generan más ingresos, cómo cambian los ingresos mes a mes y cómo se distribuyen los ingresos entre las líneas de pedido.)

---

## 2:00–4:00 — Abrir Colab, explicar pandas y cargar los datos

Pasás a la pestaña de Colab (https://colab.research.google.com) y hacés clic en **New notebook**. Hacés clic en el nombre de arriba a la izquierda y lo cambiás a `ecommerce_eda.ipynb`.

> 🟢 I'll create a new notebook. A notebook is made of cells. I write code in a cell, run it with Shift + Enter, and the result appears below.
>
> (Voy a crear un notebook nuevo. Un notebook está formado por celdas. Escribo código en una celda, la ejecuto con Shift + Enter y el resultado aparece debajo.)

Hacés clic en **+ Text** y escribís el título del notebook:

```markdown
# E-commerce Exploratory Data Analysis
Dataset: Retail Orders (Datanemics, CC0). Goal: explore revenue by category, by month, and per order line.
```

**What each line does:**

- 🟢 `# E-commerce Exploratory Data Analysis`: this is a text cell, not a code cell, so it doesn't run code. The hash sign at the start makes this line the main title. Later, lines that start with two hash signs create sections, which appear in the table of contents on the left.
- 🟢 `Dataset: ... Goal: ...`: this line says which dataset I'm using and what I want to find out, so the notebook is easy to follow.

Antes de escribir código, abrís una pestaña nueva con el sitio oficial de pandas, https://pandas.pydata.org, y lo mostrás unos 15 segundos:

> 🟢 This is the official pandas website. pandas is a free, open-source Python library for working with tables of data. It lets us load, explore, and summarize data with just a few lines of code. Colab already has it installed, so there's nothing to install.
>
> (Este es el sitio oficial de pandas. pandas es una librería de Python gratuita y de código abierto para trabajar con tablas de datos. Nos permite cargar, explorar y resumir datos con pocas líneas de código. Colab ya la tiene instalada, así que no hay que instalar nada.)

Volvés a Colab, hacés clic en **+ Code** y escribís la **celda 1**:

```python
import pandas as pd

df = pd.read_csv("https://datanemics.com/datasets/data/retail-orders.csv")
print(df.head())
```

**What each line does:**

- 🟢 `import pandas as pd`: import loads the pandas library so we can use it in the notebook. "as pd" gives it a short name, so I can write pd instead of pandas. Everyone uses pd.
- 🟢 `df = pd.read_csv(...)`: read_csv reads the CSV file straight from its link. The result is stored in a variable called df, short for DataFrame. A DataFrame is a pandas table with rows and columns, like a spreadsheet inside Python.
- 🟢 `print(df.head())`: head returns the first five rows, and print shows them. This lets me check that the data loaded correctly.

Ejecutás la celda con `Shift + Enter` y mostrás la tabla.

**Si el enlace falla:** descargás el CSV desde la página (o usás `retail-orders.csv` de esta carpeta). En Colab abrís el ícono de carpeta (**Files**) a la izquierda, hacés clic en **Upload to session storage**, elegís el archivo y cambiás la línea de lectura por `df = pd.read_csv("retail-orders.csv")`. Así lee el archivo subido, por su nombre.

> 🟢 If the link doesn't work, I can download the file and upload it from the Files panel on the left.
>
> (Si el enlace no funciona, puedo descargar el archivo y subirlo desde el panel de archivos de la izquierda.)

---

## 4:00–6:00 — Explorar los datos y convertir las fechas

Agregás una celda de texto con `## 1. Explore the data` y escribís la **celda 2**:

```python
print(df.shape)
df.info()
```

**What each line does:**

- 🟢 `print(df.shape)`: shape gives the number of rows and columns. We have 7,000 rows and 12 columns.
- 🟢 `df.info()`: info lists every column with its name, how many values it has, and its data type. I can see the three columns I need: ordered_at, category, and revenue_usd. Notice that ordered_at is stored as text, not as a date. I'll fix that next.

La ejecutás y señalás el resultado. Tiene que dar `(7000, 12)`, y `ordered_at` aparece como `object` o `str` (según la versión de pandas).

Agregás una celda de texto con `## 2. Dates and missing values` y escribís la **celda 3**:

```python
df["ordered_at"] = pd.to_datetime(df["ordered_at"])
print(df.isna().sum())
```

**What each line does:**

- 🟢 `df["ordered_at"] = pd.to_datetime(df["ordered_at"])`: to_datetime converts the ordered_at text into real dates and replaces the column. Now we can group the data by month.
- 🟢 `print(df.isna().sum())`: this checks for missing values. isna marks each empty cell as True, and sum counts them per column. This matters because missing or dirty data can give us wrong totals. Here, every column shows zero, so no cleaning is needed.

Decí "every column shows zero" solo si tu resultado muestra ceros.

---

## 6:00–11:30 — Matplotlib y los tres gráficos

Agregás una celda de texto:

```markdown
## 3. Charts
Matplotlib is Python's most widely used charting library. pandas uses it when we call `.plot()`.
```

Abrís una pestaña nueva con el sitio oficial de Matplotlib, https://matplotlib.org, y lo mostrás unos 15 segundos:

> 🟢 This is the official Matplotlib website. Matplotlib is the most popular charting library in Python. It draws bar charts, line charts, histograms, and much more. pandas uses it behind the scenes when we call plot. Colab already has it installed too.
>
> (Este es el sitio oficial de Matplotlib. Matplotlib es la librería de gráficos más popular de Python. Dibuja gráficos de barras, de líneas, histogramas y mucho más. pandas la usa por detrás cuando llamamos a plot. Colab también la tiene instalada.)

### Gráfico 1: barras, ingresos por categoría

Volvés a Colab y escribís la **celda 4**:

```python
import matplotlib.pyplot as plt

by_category = df.groupby("category")["revenue_usd"].sum().sort_values(ascending=False)
by_category.plot(kind="bar", title="Revenue by Category", xlabel="Category", ylabel="Revenue (USD)", rot=0)
plt.show()
```

**What each line does:**

- 🟢 `import matplotlib.pyplot as plt`: this imports pyplot, the part of Matplotlib that draws and shows charts, with its usual short name, plt. I only import it once, and the next cells can use it too.
- 🟢 `by_category = df.groupby("category")["revenue_usd"].sum().sort_values(ascending=False)`: groupby puts together the rows with the same category, sum adds up their revenue, and sort_values orders the result from highest to lowest. I store it in by_category.
- 🟢 `by_category.plot(kind="bar", ...)`: this draws a bar chart. title, xlabel, and ylabel set the chart title and the names of both axes, and rot equals zero keeps the category names horizontal.
- 🟢 `plt.show()`: this displays the chart below the cell.

Ejecutás la celda y te detenés un momento en el gráfico.

### Gráfico 2: líneas, ingresos mensuales

Escribís la **celda 5**:

```python
monthly = df.groupby(df["ordered_at"].dt.to_period("M"))["revenue_usd"].sum()
monthly.plot(marker="o", title="Monthly Revenue", xlabel="Month", ylabel="Revenue (USD)")
plt.show()
```

**What each line does:**

- 🟢 `monthly = df.groupby(df["ordered_at"].dt.to_period("M"))["revenue_usd"].sum()`: dt gives access to date functions, and to_period with "M" turns each date into its month, like 2023-01. This only works because we converted the column to dates. Then groupby groups the rows by month, sum adds up the revenue, and I store the 24 monthly totals in monthly.
- 🟢 `monthly.plot(marker="o", ...)`: this draws a line chart, which is the default type, so I don't need kind. A line chart is the right choice for data over time, and marker "o" puts a dot on each month. Again, title, xlabel, and ylabel set the title and the axis names.
- 🟢 `plt.show()`: this displays the chart.

Ejecutás la celda.

### Gráfico 3: histograma, ingresos por línea de pedido

Escribís la **celda 6**:

```python
df["revenue_usd"].plot(kind="hist", bins=50, title="Revenue per Order Line")
plt.xlabel("Revenue (USD)")
plt.show()
```

**What each line does:**

- 🟢 `df["revenue_usd"].plot(kind="hist", bins=50, ...)`: I take the revenue column on its own, without grouping, so each value is one order line. kind "hist" draws a histogram: it splits the revenue into fifty ranges, called bins, and the height of each bar is how many order lines fall in that range. So the vertical axis, Frequency, is a count, not money.
- 🟢 `plt.xlabel("Revenue (USD)")`: this sets the name of the horizontal axis. For the histogram I set it separately with plt, because pandas doesn't always apply it inside plot.
- 🟢 `plt.show()`: this displays the chart.

Ejecutás la celda.

---

## 11:30–14:00 — Interpretar los resultados y verificar los gráficos

Volvés a subir hasta cada gráfico. Revisás que tenga título y ejes con nombre, que el de barras tenga 6 categorías y que el de líneas tenga 24 meses.

**Valores de referencia.** Los calculé directamente del CSV el 21/10/2026, fuera de Colab. Compará con **tu** resultado antes de decirlos:

| Gráfico | Lo que muestran los datos |
| ------- | ------------------------- |
| Barras | Electronics lidera con unos $326.000 de $774.000 en total (~42%). Le siguen home (~$152.000) y apparel (~$126.000). Grocery es la más baja (~$37.000). |
| Líneas | La mayoría de los meses están entre $25.000 y $38.000. Hay un pico en diciembre en los dos años (~$48.000 en 2023 y ~$44.000 en 2024). El mes más bajo es enero de 2024 (~$18.600). |
| Histograma | Asimetría a la derecha: la mayoría de las líneas son de menos de ~$125 (la mediana ronda los $60). Hay una cola de pocas líneas grandes, hasta ~$2.300. |

Mientras recorrés el gráfico de barras:

> 🟢 In the bar chart, electronics is clearly the top category, with about 42 percent of all revenue. Grocery brings in the least.
>
> (En el gráfico de barras, electrónica es claramente la categoría principal, con cerca del 42 por ciento de los ingresos. Grocery es la que menos genera.)

Bajás al gráfico de líneas:

> 🟢 In the line chart, revenue is fairly stable most of the year, but it peaks in December in both years and drops in January. That looks like a holiday season effect.
>
> (En el gráfico de líneas, los ingresos son bastante estables la mayor parte del año, pero tienen un pico en diciembre en los dos años y bajan en enero. Parece un efecto de la temporada de fiestas.)

Bajás al histograma:

> 🟢 The histogram is right-skewed. Most order lines are small, but there's a long tail of a few large ones.
>
> (El histograma tiene asimetría a la derecha. La mayoría de las líneas de pedido son chicas, pero hay una cola larga de pocas líneas grandes.)

Verificás en voz alta:

> 🟢 Let me verify: each chart has a title and labeled axes, the bar chart shows all six categories, and the line chart covers all twenty-four months.
>
> (Verifico: cada gráfico tiene título y ejes con nombre, el de barras muestra las seis categorías y el de líneas cubre los veinticuatro meses.)

Agregás una celda de texto con las observaciones: una o dos frases por gráfico, con lo que se ve en él. Estas coinciden con los resultados del notebook ejecutado en Colab el 22/10/2026:

```markdown
## 4. Observations
- **Bar chart:** electronics is the top category, with about $326K of the $774K total (around 42%). Home and apparel follow, and grocery is the lowest (about $37K).
- **Line chart:** monthly revenue stays mostly between $25K and $38K. It peaks in December in both years (about $48K in 2023 and $44K in 2024) and drops in January, which suggests a holiday-season effect.
- **Histogram:** the distribution is right-skewed. Most order lines are under about $125, and a few large lines go up to about $2,300.
```

Mientras la escribís:

> 🟢 Now I'll write down what each chart shows, so the findings are saved in the notebook next to the charts.
>
> (Ahora anoto lo que muestra cada gráfico, así los hallazgos quedan guardados en el notebook junto a los gráficos.)

---

## 14:00–15:00 — Resumen y propósito

Agregás la última celda de texto:

```markdown
## 5. Conclusion
We loaded a public e-commerce CSV with pandas, checked its structure and missing values, converted dates,
and used Matplotlib to compare revenue by category, over time, and per order line.
Main findings: electronics leads revenue, revenue peaks in December, and most order lines are small.
```

Subís hasta el principio del notebook y cerrás:

> 🟢 To sum up, I loaded a public e-commerce CSV with pandas, explored its structure, converted the dates, checked for missing values, and created three charts with Matplotlib.
>
> (Para resumir, cargué un CSV público de e-commerce con pandas, exploré su estructura, convertí las fechas, revisé los valores faltantes y creé tres gráficos con Matplotlib.)
>
> 🟢 The main findings: electronics leads revenue, sales peak in December, and most order lines are small.
>
> (Los hallazgos principales: electrónica lidera los ingresos, las ventas tienen su pico en diciembre y la mayoría de las líneas de pedido son chicas.)
>
> 🟢 The purpose of exploratory analysis is to understand the data before making decisions or building anything more complex. Thanks for watching!
>
> (El propósito del análisis exploratorio es entender los datos antes de tomar decisiones o construir algo más complejo. ¡Gracias por mirar!)
