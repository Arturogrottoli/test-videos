# dje548b6 — E-commerce Exploratory Data Analysis

Guion paso a paso para grabar la tarea **dje548b6**: un análisis exploratorio de un dataset público de e-commerce en **Google Colab**, con **Python**, **pandas** y **Matplotlib**, en unos **15 minutos**. El código es corto a propósito: son **6 celdas y 16 líneas**, para dedicar el tiempo a explicar.

**Cómo leer este guion:**

- El texto en <span style="color:#3fb950">**verde**</span> es lo que **decís en inglés** durante la grabación.
- El resto, en castellano, es lo que hacés en pantalla y la explicación de cada línea de código. Las traducciones aparecen entre paréntesis después de cada frase.
- Los colores se ven en la vista previa de VS Code (`Ctrl + Shift + V`). GitHub no muestra colores.

> **Importante:** el Goal oficial de Mercor y las reglas de grabación de Odin tienen prioridad sobre este guion. Antes de grabar, comparalos, sobre todo el dataset y los tres gráficos. Este guion no garantiza que la tarea se apruebe ni que 15 minutos alcancen.

---

## Archivos de la carpeta

```
dje548b6-ecommerce-exploratory-analysis/
├── README.md            ← este guion
├── ecommerce_eda.ipynb  ← el notebook completo, listo para abrir en Colab
├── notebook_cells.py    ← el mismo código como script de Python
└── retail-orders.csv    ← copia de respaldo del dataset (descargada el 21/10/2026)
```

`ecommerce_eda.ipynb` ya hace todo el análisis, punto por punto, con las mismas celdas de texto y de código que este guion. Para abrirlo en Colab: en https://colab.research.google.com elegís **Archivo → Subir notebook** (*File → Upload notebook*), seleccionás `ecommerce_eda.ipynb` y después **Entorno de ejecución → Ejecutar todas** (*Runtime → Run all*). Colab solo abre archivos `.ipynb`: el `.py` no se puede subir como notebook.

`notebook_cells.py` tiene el mismo código, para ejecutarlo fuera de Colab con `python notebook_cells.py`. Si las reglas de Odin piden escribir el código en pantalla, usá estos archivos solo para practicar y **no los pegues** durante la grabación.

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
2. Abrí `ecommerce_eda.ipynb` en Colab, ejecutalo entero y anotá tus números reales.
3. Dejá dos pestañas abiertas: la página del dataset y Colab. Agrandá el zoom del navegador (`Ctrl + +`).

---

## 0:00–2:00 — El objetivo y la página del CSV

Empezás con la pestaña del dataset abierta en https://datanemics.com/datasets/retail-orders/. Saludás y presentás el objetivo:

> <span style="color:#3fb950">Hi! In this video, I'll do an exploratory data analysis of a public e-commerce dataset, using Python, pandas, and Matplotlib in Google Colab.</span>
>
> (¡Hola! En este video voy a hacer un análisis exploratorio de un dataset público de e-commerce, usando Python, pandas y Matplotlib en Google Colab.)

Bajás despacio por la página para mostrar la descripción del dataset:

> <span style="color:#3fb950">This is the Retail Orders dataset. It's synthetic and in the public domain, and it has 7,000 order lines from 2023 and 2024.</span>
>
> (Este es el dataset Retail Orders. Es sintético y de dominio público, y tiene 7.000 líneas de pedidos de 2023 y 2024.)

Señalás el enlace de descarga del CSV y explicás qué es un CSV:

> <span style="color:#3fb950">The data comes as a CSV file. CSV means comma-separated values: it's a plain text table, where each line is a row and commas separate the columns. You can download it from this link.</span>
>
> (Los datos vienen en un archivo CSV. CSV significa valores separados por comas: es una tabla en texto plano, donde cada línea es una fila y las comas separan las columnas. Se puede descargar desde este enlace.)

Mostrás la lista de columnas y contás qué vas a buscar:

> <span style="color:#3fb950">I want to answer three questions: which categories bring in the most revenue, how revenue changes month by month, and how revenue is distributed across order lines.</span>
>
> (Quiero responder tres preguntas: qué categorías generan más ingresos, cómo cambian los ingresos mes a mes y cómo se distribuyen los ingresos entre las líneas de pedido.)

---

## 2:00–4:00 — Abrir Colab, explicar pandas y cargar los datos

Pasás a la pestaña de Colab (https://colab.research.google.com) y hacés clic en **New notebook**. Hacés clic en el nombre de arriba a la izquierda y lo cambiás a `ecommerce_eda.ipynb`.

> <span style="color:#3fb950">I'll create a new notebook. A notebook is made of cells. I write code in a cell, run it with Shift + Enter, and the result appears below.</span>
>
> (Voy a crear un notebook nuevo. Un notebook está formado por celdas. Escribo código en una celda, la ejecuto con Shift + Enter y el resultado aparece debajo.)

Hacés clic en **+ Text** y escribís el título del notebook:

```markdown
# E-commerce Exploratory Data Analysis
Dataset: Retail Orders (Datanemics, CC0). Goal: explore revenue by category, by month, and per order line.
```

Antes de escribir código, explicás qué es pandas:

> <span style="color:#3fb950">pandas is a Python library for working with tables of data. It lets us load, explore, and summarize data with just a few lines of code. Colab already has it installed, so there's nothing to install.</span>
>
> (pandas es una librería de Python para trabajar con tablas de datos. Nos permite cargar, explorar y resumir datos con pocas líneas de código. Colab ya la tiene instalada, así que no hay que instalar nada.)

Hacés clic en **+ Code** y escribís la **celda 1**:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://datanemics.com/datasets/data/retail-orders.csv")
df.head()
```

Qué hace cada línea:

- `import pandas as pd`: carga pandas con su alias habitual, `pd`.
- `import matplotlib.pyplot as plt`: carga el módulo de gráficos de Matplotlib con el alias `plt`.
- `df = pd.read_csv(...)`: lee el CSV directamente desde el enlace y lo guarda en un DataFrame llamado `df`.
- `df.head()`: muestra las primeras 5 filas, para comprobar que los datos se cargaron bien.

Mientras la escribís, lo contás:

> <span style="color:#3fb950">I import pandas as "pd", and Matplotlib's pyplot as "plt". Those are the usual short names.</span>
>
> (Importo pandas como "pd" y el pyplot de Matplotlib como "plt". Son los alias habituales.)
>
> <span style="color:#3fb950">read_csv loads the file straight from its link into a DataFrame. A DataFrame is like a spreadsheet inside Python. head shows the first five rows.</span>
>
> (read_csv carga el archivo directamente desde su enlace en un DataFrame. Un DataFrame es como una hoja de cálculo dentro de Python. head muestra las primeras cinco filas.)

Ejecutás la celda con `Shift + Enter` y mostrás la tabla.

**Si el enlace falla:** descargás el CSV desde la página (o usás `retail-orders.csv` de esta carpeta). En Colab abrís el ícono de carpeta (**Files**) a la izquierda, hacés clic en **Upload to session storage**, elegís el archivo y cambiás la línea de lectura por `df = pd.read_csv("retail-orders.csv")`. Así lee el archivo subido, por su nombre.

> <span style="color:#3fb950">If the link doesn't work, I can download the file and upload it from the Files panel on the left.</span>
>
> (Si el enlace no funciona, puedo descargar el archivo y subirlo desde el panel de archivos de la izquierda.)

---

## 4:00–6:00 — Explorar los datos y convertir las fechas

Agregás una celda de texto con `## 1. Explore the data` y escribís la **celda 2**:

```python
print(df.shape)
df.info()
```

Qué hace cada línea:

- `print(df.shape)`: muestra (filas, columnas). Tiene que dar `(7000, 12)`.
- `df.info()`: en una sola tabla muestra cada columna con su nombre, cuántos valores no vacíos tiene y su tipo de dato (`Dtype`). Ahí comprobás que existen `ordered_at`, `category` y `revenue_usd`, y que `ordered_at` es texto (`object` o `str`, según la versión de pandas), no fecha.

La ejecutás y lo explicás:

> <span style="color:#3fb950">shape tells us we have 7,000 rows and 12 columns. info lists every column with its data type, and I can see the three I need: ordered_at, category, and revenue_usd.</span>
>
> (shape nos dice que tenemos 7.000 filas y 12 columnas. info lista cada columna con su tipo de dato, y veo las tres que necesito: ordered_at, category y revenue_usd.)
>
> <span style="color:#3fb950">Notice that ordered_at is stored as text, not as a date. I'll fix that next.</span>
>
> (Fíjense que ordered_at está guardada como texto, no como fecha. Eso lo arreglo ahora.)

Agregás una celda de texto con `## 2. Dates and missing values` y escribís la **celda 3**:

```python
df["ordered_at"] = pd.to_datetime(df["ordered_at"])
df.isna().sum()
```

Qué hace cada línea:

- `pd.to_datetime(df["ordered_at"])`: convierte el texto en fechas reales y reemplaza la columna. Ahora se puede agrupar por mes.
- `df.isna().sum()`: `isna()` marca cada celda vacía como `True`, y `sum()` las cuenta por columna.

La ejecutás y lo explicás:

> <span style="color:#3fb950">I convert ordered_at with pd.to_datetime, so now it's a real date and we can group it by month.</span>
>
> (Convierto ordered_at con pd.to_datetime, así que ahora es una fecha real y la podemos agrupar por mes.)
>
> <span style="color:#3fb950">Next, I check for missing values. isna marks each empty cell, and sum counts them per column. This matters because missing or dirty data can give us wrong totals. Here, every column shows zero, so no cleaning is needed.</span>
>
> (Después reviso los valores faltantes. isna marca cada celda vacía, y sum las cuenta por columna. Esto importa porque los datos faltantes o sucios pueden darnos totales incorrectos. Acá todas las columnas muestran cero, así que no hace falta limpiar.)

Decí "zero" solo si tu resultado muestra ceros.

---

## 6:00–11:30 — Matplotlib y los tres gráficos

Agregás una celda de texto:

```markdown
## 3. Charts
Matplotlib is Python's most widely used charting library. pandas uses it when we call `.plot()`.
```

Y presentás la librería:

> <span style="color:#3fb950">Matplotlib is the most popular charting library in Python. pandas uses it behind the scenes when we call plot, so I can set the title and the axis labels right inside plot. plt.show displays the chart.</span>
>
> (Matplotlib es la librería de gráficos más popular de Python. pandas la usa por detrás cuando llamamos a plot, así que puedo poner el título y los nombres de los ejes directamente dentro de plot. plt.show muestra el gráfico.)

### Gráfico 1: barras, ingresos por categoría

Escribís la **celda 4**:

```python
by_category = df.groupby("category")["revenue_usd"].sum().sort_values(ascending=False)
by_category.plot(kind="bar", title="Revenue by Category", xlabel="Category", ylabel="Revenue (USD)", rot=0)
plt.show()
```

Qué hace cada línea:

- Línea 1: `groupby("category")` agrupa las filas por categoría, `["revenue_usd"].sum()` suma los ingresos de cada grupo y `sort_values(ascending=False)` ordena de mayor a menor.
- Línea 2: `plot(kind="bar", ...)` dibuja un gráfico de barras. `title`, `xlabel` y `ylabel` ponen el título y los nombres de los ejes. `rot=0` deja los nombres de las categorías horizontales.
- Línea 3: `plt.show()` muestra el gráfico debajo de la celda.

Mientras la escribís, lo contás:

> <span style="color:#3fb950">groupby puts together the rows with the same category, sum adds up their revenue, and I sort the result from highest to lowest.</span>
>
> (groupby junta las filas con la misma categoría, sum suma sus ingresos, y ordeno el resultado de mayor a menor.)
>
> <span style="color:#3fb950">Then I plot it as a bar chart, with a title and labels for both axes.</span>
>
> (Después lo grafico como barras, con un título y nombres para los dos ejes.)

Ejecutás la celda y te detenés un momento en el gráfico.

### Gráfico 2: líneas, ingresos mensuales

Escribís la **celda 5**:

```python
monthly = df.groupby(df["ordered_at"].dt.to_period("M"))["revenue_usd"].sum()
monthly.plot(marker="o", title="Monthly Revenue", xlabel="Month", ylabel="Revenue (USD)")
plt.show()
```

Qué hace cada línea:

- Línea 1: `dt.to_period("M")` convierte cada fecha en su mes (por ejemplo `2023-01`). Funciona solo porque antes convertimos la columna a fechas. Después agrupa por mes y suma los ingresos.
- Línea 2: `plot(...)` dibuja un gráfico de líneas, que es el tipo por defecto. `marker="o"` pone un punto en cada mes. `title`, `xlabel` y `ylabel` ponen el título y los nombres de los ejes.
- Línea 3: `plt.show()` muestra el gráfico.

Mientras la escribís, lo contás:

> <span style="color:#3fb950">to_period with "M" turns each date into its month. This only works because we converted the column to dates. Then I group by month and add up the revenue.</span>
>
> (to_period con "M" convierte cada fecha en su mes. Esto funciona solo porque convertimos la columna a fechas. Después agrupo por mes y sumo los ingresos.)
>
> <span style="color:#3fb950">A line chart is the right choice for data over time, and the markers show each month.</span>
>
> (Un gráfico de líneas es la opción adecuada para datos en el tiempo, y los marcadores muestran cada mes.)

Ejecutás la celda.

### Gráfico 3: histograma, ingresos por línea de pedido

Escribís la **celda 6**:

```python
df["revenue_usd"].plot(kind="hist", bins=50, title="Revenue per Order Line")
plt.xlabel("Revenue (USD)")
plt.show()
```

Qué hace cada línea:

- Línea 1: `plot(kind="hist", bins=50, ...)` dibuja un histograma. Divide los ingresos en 50 rangos (bins) y cuenta cuántas líneas caen en cada uno. El eje vertical sale solo con el nombre `Frequency`: es una **cantidad de líneas**, no dinero.
- Línea 2: `plt.xlabel(...)` pone el nombre del eje horizontal. En los histogramas se pone con `plt` porque pandas no siempre lo toma dentro de `plot`.
- Línea 3: `plt.show()` muestra el gráfico.

Mientras la escribís, lo contás:

> <span style="color:#3fb950">A histogram splits the revenue into ranges, called bins. Here I use fifty. The height of each bar is how many order lines fall in that range, so the vertical axis is a count, not money.</span>
>
> (Un histograma divide los ingresos en rangos, llamados bins. Acá uso cincuenta. La altura de cada barra es cuántas líneas de pedido caen en ese rango, así que el eje vertical es una cantidad, no dinero.)

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

> <span style="color:#3fb950">In the bar chart, electronics is clearly the top category, with about 42 percent of all revenue. Grocery brings in the least.</span>
>
> (En el gráfico de barras, electrónica es claramente la categoría principal, con cerca del 42 por ciento de los ingresos. Grocery es la que menos genera.)

Bajás al gráfico de líneas:

> <span style="color:#3fb950">In the line chart, revenue is fairly stable most of the year, but it peaks in December in both years and drops in January. That looks like a holiday season effect.</span>
>
> (En el gráfico de líneas, los ingresos son bastante estables la mayor parte del año, pero tienen un pico en diciembre en los dos años y bajan en enero. Parece un efecto de la temporada de fiestas.)

Bajás al histograma:

> <span style="color:#3fb950">The histogram is right-skewed. Most order lines are small, but there's a long tail of a few large ones.</span>
>
> (El histograma tiene asimetría a la derecha. La mayoría de las líneas de pedido son chicas, pero hay una cola larga de pocas líneas grandes.)

Verificás en voz alta:

> <span style="color:#3fb950">Let me verify: each chart has a title and labeled axes, the bar chart shows all six categories, and the line chart covers all twenty-four months.</span>
>
> (Verifico: cada gráfico tiene título y ejes con nombre, el de barras muestra las seis categorías y el de líneas cubre los veinticuatro meses.)

Agregás una celda de texto con tus observaciones reales:

```markdown
## 4. Observations
- Bar chart: ...
- Line chart: ...
- Histogram: ...
```

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

> <span style="color:#3fb950">To sum up, I loaded a public e-commerce CSV with pandas, explored its structure, converted the dates, checked for missing values, and created three charts with Matplotlib.</span>
>
> (Para resumir, cargué un CSV público de e-commerce con pandas, exploré su estructura, convertí las fechas, revisé los valores faltantes y creé tres gráficos con Matplotlib.)
>
> <span style="color:#3fb950">The main findings: electronics leads revenue, sales peak in December, and most order lines are small.</span>
>
> (Los hallazgos principales: electrónica lidera los ingresos, las ventas tienen su pico en diciembre y la mayoría de las líneas de pedido son chicas.)
>
> <span style="color:#3fb950">The purpose of exploratory analysis is to understand the data before making decisions or building anything more complex. Thanks for watching!</span>
>
> (El propósito del análisis exploratorio es entender los datos antes de tomar decisiones o construir algo más complejo. ¡Gracias por mirar!)
