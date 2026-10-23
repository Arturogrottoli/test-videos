# dje548b6 — E-commerce Exploratory Data Analysis

Guion paso a paso para grabar la tarea **dje548b6**: un análisis exploratorio de un dataset público de e-commerce en **Google Colab**, con **Python**, **pandas** y **Matplotlib**. La grabación tiene que durar **entre 15:00 y 50:59**. Este guion apunta a unos **22–24 minutos**, epílogo incluido, para no quedar cerca del mínimo. El código es corto a propósito: son **6 celdas y 16 líneas**, para dedicar el tiempo a explicar.

**Cómo leer este guion:**

- Las frases que empiezan con 🖱️ las decís **en el momento de hacer clic, desplazarte o escribir**. Siempre dicen **qué** elemento usás, **dónde** está en la pantalla y **por qué** lo usás. Son las que revisa AutoQC.
- Las frases que empiezan con 🟢 son la explicación que **decís en inglés** entre una acción y otra.
- Debajo de cada bloque de código, la lista **What each line does** explica cada línea en inglés. La leés en voz alta mientras escribís esa línea.
- El resto, en castellano, es lo que hacés en pantalla. Las traducciones aparecen entre paréntesis después de cada frase.

> **Importante:** el Goal oficial de Mercor y las reglas de grabación de Odin tienen prioridad sobre este guion. Antes de grabar, comparalos, sobre todo el dataset, los tres gráficos y el epílogo. Este guion no garantiza que la tarea se apruebe.

---

## Lo que pidió AutoQC en la grabación anterior

| Control | Qué pasó | Qué hacer ahora |
| ------- | -------- | --------------- |
| **Narración: dónde (bloquea el envío)** | En 0 de 59 interacciones dijiste dónde estaba el elemento. | Leé **todas** las frases 🖱️. Al menos el 70% de las interacciones tiene que decir **dónde** y **por qué**. Fórmula: *I'm clicking **[elemento]** **[ubicación]** to **[motivo]**.* |
| Ventanas superpuestas | Una ventana tapó otra durante 17 segundos (01:11–01:27). | Antes de grabar, dejá **solo el navegador** maximizado. Cerrá o minimizá todo lo demás, también este guion si está en la misma pantalla. |
| Porcentaje de escritura | 23,5% (para programación se acepta hasta ~30%). | Ejecutá las celdas con el **botón Run** (mouse), no con el teclado. Escribí solo el código y los títulos cortos. |
| Duración | Tiene que ser una sola grabación continua de 15:00 a 50:59. | Seguí los tiempos de este guion. No dejes silencios de más de 45 segundos y hacé una pausa de ~1 segundo después de cada clic. |
| Goal y epílogo | Hay que mostrar el Goal al principio y, en esta tarea, incluir un epílogo de 3–4 minutos (aprobado el 22/10). | El Goal está en la sección 0:00–0:45 (máximo 30 segundos de narración). El epílogo está al final. |

Si en un momento hacés algo que no está en el guion (por ejemplo, cerrar un aviso), decí igual qué es, dónde está y por qué lo tocás: *"I'm closing this pop-up with the X button at its top right, so it doesn't cover the notebook."*

---

## Archivos de la carpeta

```
dje548b6-ecommerce-exploratory-analysis/
├── README.md            ← este guion: qué hacer, qué decir en inglés y dónde está cada botón
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
2. Subí `ecommerce_eda.ipynb` a Colab, ejecutalo entero y anotá tus números reales. Después practicá una vez escribiendo las celdas vos, en un notebook nuevo, **leyendo en voz alta todas las frases 🖱️ y 🟢** y cronometrando.
3. Dejá tres pestañas abiertas en el navegador, en este orden: el documento **Goal**, la página del dataset y Colab (https://colab.research.google.com). Agrandá el zoom del navegador (`Ctrl + +`).
4. Maximizá el navegador y cerrá o minimizá las demás ventanas, para que ninguna tape a otra durante la grabación.
5. Recordá: pausa de ~1 segundo después de cada clic, y nunca más de 45 segundos en silencio.
6. No muestres Studio, Mercor, información privada ni herramientas de IA en ningún momento de la grabación. Usá solo las apps permitidas (Google Colab en Firefox). Cerrá también este guion si está en la misma pantalla.

---

## 0:00–0:45 — Mostrar el Goal

Empezás con la pestaña del **Goal** abierta. Lo mostrás y no lo narrás más de 30 segundos:

> 🖱️ I'm on the Goal document in the first browser tab, to show what this task asks for.
>
> (Estoy en el documento del Goal, en la primera pestaña del navegador, para mostrar qué pide esta tarea.)
>
> 🟢 The goal is to do an exploratory data analysis of a public e-commerce dataset in Google Colab, using Python, pandas, and Matplotlib, and to create and explain three charts.
>
> (El objetivo es hacer un análisis exploratorio de un dataset público de e-commerce en Google Colab, con Python, pandas y Matplotlib, y crear y explicar tres gráficos.)

Ajustá esta frase a lo que diga tu Goal.

---

## 0:45–4:00 — La página del CSV y el plan

La introducción tiene que durar **menos de 20 segundos**: una sola frase y enseguida la primera acción. Las explicaciones largas (qué es EDA, Colab y Python) van después, mientras hacés algo en pantalla.

> 🟢 Hi! In this video, I'll do an exploratory data analysis of a public e-commerce dataset, using Python, pandas, and Matplotlib in Google Colab.
>
> (¡Hola! En este video voy a hacer un análisis exploratorio de un dataset público de e-commerce, usando Python, pandas y Matplotlib en Google Colab.)
>
> 🖱️ I'm clicking the second browser tab, at the top of the window, to open the dataset page.
>
> (Hago clic en la segunda pestaña del navegador, arriba de la ventana, para abrir la página del dataset.)

Bajás despacio por la página mientras explicás qué es un análisis exploratorio:

> 🖱️ I'm scrolling down the dataset page with the mouse wheel to show the description of the data.
>
> (Bajo por la página del dataset con la rueda del mouse para mostrar la descripción de los datos.)
>
> 🟢 Exploratory data analysis, or EDA, is the first step when we get a new dataset. Before building models or making decisions, we look at the data to understand what it contains: how big it is, what each column means, whether there are missing or wrong values, and what patterns stand out. Charts are a big part of it, because a chart shows in seconds what a table of thousands of rows can't.
>
> (El análisis exploratorio de datos, o EDA, es el primer paso cuando recibimos un dataset nuevo. Antes de construir modelos o tomar decisiones, miramos los datos para entender qué contienen: qué tamaño tienen, qué significa cada columna, si hay valores faltantes o incorrectos y qué patrones se destacan. Los gráficos son una parte importante, porque un gráfico muestra en segundos lo que una tabla de miles de filas no puede.)
>
> 🟢 This is the Retail Orders dataset. It's synthetic and in the public domain, and it has 7,000 order lines from 2023 and 2024.
>
> (Este es el dataset Retail Orders. Es sintético y de dominio público, y tiene 7.000 líneas de pedidos de 2023 y 2024.)

Señalás el botón de descarga y explicás qué es un CSV:

> 🟢 The data comes as a CSV file. CSV means comma-separated values: it's a plain text table, where each line is a row and commas separate the columns.
>
> (Los datos vienen en un archivo CSV. CSV significa valores separados por comas: es una tabla en texto plano, donde cada línea es una fila y las comas separan las columnas.)
>
> 🖱️ I'm clicking the Download CSV button on this page to save a copy of the dataset, as a backup in case the direct link doesn't work in Colab.
>
> (Hago clic en el botón Download CSV de esta página para guardar una copia del dataset, como respaldo por si el enlace directo no funciona en Colab.)

Bajás hasta la lista de columnas y contás qué vas a buscar:

> 🖱️ I'm scrolling down to the column list in the middle of the page, to see which fields the dataset has.
>
> (Bajo hasta la lista de columnas, en el medio de la página, para ver qué campos tiene el dataset.)
>
> 🟢 I want to answer three questions: which categories bring in the most revenue, how revenue changes month by month, and how revenue is distributed across order lines.
>
> (Quiero responder tres preguntas: qué categorías generan más ingresos, cómo cambian los ingresos mes a mes y cómo se distribuyen los ingresos entre las líneas de pedido.)

Contás el plan, paso por paso:

> 🟢 Here's the plan. First, I'll read the CSV with pandas and look at the first rows. Second, I'll check its structure: how many rows and columns it has, and the data type of each column.
>
> (Este es el plan. Primero, voy a leer el CSV con pandas y mirar las primeras filas. Segundo, voy a revisar su estructura: cuántas filas y columnas tiene y el tipo de dato de cada columna.)
>
> 🟢 Third, I'll clean the data. I'll convert the order dates from text to real dates, and check for missing values, because dirty data gives wrong results.
>
> (Tercero, voy a limpiar los datos. Voy a convertir las fechas de los pedidos de texto a fechas reales y revisar los valores faltantes, porque los datos sucios dan resultados incorrectos.)
>
> 🟢 Finally, I'll build three charts with Matplotlib, one for each question: a bar chart, a line chart, and a histogram. Then I'll explain what each chart tells us.
>
> (Por último, voy a armar tres gráficos con Matplotlib, uno para cada pregunta: un gráfico de barras, uno de líneas y un histograma. Después voy a explicar qué nos dice cada gráfico.)

---

## 4:00–7:00 — Abrir Colab, explicar pandas y cargar los datos

> 🖱️ I'm clicking the third browser tab, at the top of the window, to open Google Colab.
>
> (Hago clic en la tercera pestaña del navegador, arriba de la ventana, para abrir Google Colab.)
>
> 🟢 This is Google Colab. Colab is a free tool from Google that runs Python notebooks in the browser. There's nothing to install: the code runs on a computer in Google's cloud, and popular data libraries like pandas and Matplotlib are already installed.
>
> (Esto es Google Colab. Colab es una herramienta gratuita de Google que ejecuta notebooks de Python en el navegador. No hay que instalar nada: el código se ejecuta en una computadora en la nube de Google, y las librerías de datos más populares, como pandas y Matplotlib, ya vienen instaladas.)
>
> 🟢 Python is the programming language we'll use. It's the most popular language for data analysis, because its code is short and easy to read.
>
> (Python es el lenguaje de programación que vamos a usar. Es el lenguaje más popular para análisis de datos, porque su código es corto y fácil de leer.)
>
> 🖱️ I'm clicking the New notebook button at the bottom of the Open notebook dialog, to create a fresh Colab notebook.
>
> (Hago clic en el botón New notebook, abajo del cuadro Open notebook, para crear un notebook de Colab nuevo.)

Si no aparece el cuadro, usás el menú: *"I'm opening the File menu at the top left and choosing New notebook, to create a fresh notebook."*

> 🟢 A notebook is made of cells. I write Python in a cell, run it, and the result appears right below the cell, so I can explore the data step by step.
>
> (Un notebook está formado por celdas. Escribo Python en una celda, la ejecuto y el resultado aparece justo debajo de la celda, así que puedo explorar los datos paso a paso.)
>
> 🖱️ I'm clicking the notebook title field at the top left, and typing ecommerce_eda.ipynb, to identify this analysis.
>
> (Hago clic en el campo del título del notebook, arriba a la izquierda, y escribo ecommerce_eda.ipynb, para identificar este análisis.)
>
> 🖱️ I'm clicking the plus Text button in the toolbar at the top left, to add a text cell with the title and the goal.
>
> (Hago clic en el botón + Text de la barra de herramientas, arriba a la izquierda, para agregar una celda de texto con el título y el objetivo.)

Escribís el título del notebook:

```markdown
# E-commerce Exploratory Data Analysis
Dataset: Retail Orders (Datanemics, CC0). Goal: explore revenue by category, by month, and per order line.
```

**What each line does:**

- 🟢 `# E-commerce Exploratory Data Analysis`: this is a text cell, not a code cell, so it doesn't run code. The hash sign at the start makes this line the main title. Later, lines that start with two hash signs create sections, which appear in the table of contents on the left.
- 🟢 `Dataset: ... Goal: ...`: this line says which dataset I'm using and what I want to find out, so the notebook is easy to follow.

Antes de escribir código, mostrás el sitio oficial de pandas unos 15 segundos:

> 🖱️ I'm clicking the plus button next to the browser tabs at the top, and typing pandas.pydata.org in the address bar, to show the official pandas website.
>
> (Hago clic en el botón + al lado de las pestañas del navegador, arriba, y escribo pandas.pydata.org en la barra de direcciones, para mostrar el sitio oficial de pandas.)
>
> 🟢 This is the official pandas website. pandas is a free, open-source Python library for working with tables of data. It lets us load, explore, and summarize data with just a few lines of code. Colab already has it installed, so there's nothing to install.
>
> (Este es el sitio oficial de pandas. pandas es una librería de Python gratuita y de código abierto para trabajar con tablas de datos. Nos permite cargar, explorar y resumir datos con pocas líneas de código. Colab ya la tiene instalada, así que no hay que instalar nada.)
>
> 🖱️ I'm clicking the Colab tab at the top of the browser, to go back to my notebook.
>
> (Hago clic en la pestaña de Colab, arriba del navegador, para volver a mi notebook.)
>
> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add a code cell below the title.
>
> (Hago clic en el botón + Code de la barra de herramientas, arriba a la izquierda, para agregar una celda de código debajo del título.)
>
> 🖱️ I'm typing in this new code cell to import pandas and load the data.
>
> (Escribo en esta celda de código nueva para importar pandas y cargar los datos.)

Escribís la **celda 1**:

```python
import pandas as pd

df = pd.read_csv("https://datanemics.com/datasets/data/retail-orders.csv")
print(df.head())
```

**What each line does:**

- 🟢 `import pandas as pd`: import loads the pandas library so we can use it in the notebook. "as pd" gives it a short name, so I can write pd instead of pandas. Everyone uses pd.
- 🟢 `df = pd.read_csv(...)`: read_csv reads the CSV file straight from its link. The result is stored in a variable called df, short for DataFrame. A DataFrame is a pandas table with rows and columns, like a spreadsheet inside Python.
- 🟢 `print(df.head())`: head returns the first five rows, and print shows them. This lets me check that the data loaded correctly.

> 🖱️ I'm clicking the Run cell button, the play icon to the left of this code cell, to load the data.
>
> (Hago clic en el botón Run cell, el ícono de play a la izquierda de esta celda de código, para cargar los datos.)
>
> 🟢 Here are the first five rows. The data loaded correctly.
>
> (Acá están las primeras cinco filas. Los datos se cargaron bien.)

La primera vez, Colab tarda unos segundos en conectarse: seguí hablando mientras tanto.

**Si el enlace falla:** usás el CSV que descargaste (o `retail-orders.csv` de esta carpeta) y decís:

> 🖱️ I'm opening the Files icon, the folder in the left sidebar, to manage the dataset.
>
> (Abro el ícono Files, la carpeta de la barra lateral izquierda, para manejar el dataset.)
>
> 🖱️ I'm clicking Upload to session storage, at the top of the Files pane on the left, to load the CSV I downloaded.
>
> (Hago clic en Upload to session storage, arriba del panel Files de la izquierda, para cargar el CSV que descargué.)
>
> 🖱️ I'm editing the read_csv line in this code cell, to read the uploaded file by its name.
>
> (Edito la línea de read_csv en esta celda de código, para leer el archivo subido por su nombre.)

La línea queda `df = pd.read_csv("retail-orders.csv")`. Después ejecutás la celda con el botón Run, como arriba.

---

## 7:00–10:00 — Explorar los datos y convertir las fechas

> 🖱️ I'm clicking the plus Text button in the toolbar at the top left, to add a section heading called Explore the data.
>
> (Hago clic en el botón + Text de la barra de herramientas, arriba a la izquierda, para agregar un título de sección llamado Explore the data.)

Escribís `## 1. Explore the data`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell under this heading and check the structure of the data.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código debajo de este título y revisar la estructura de los datos.)

Escribís la **celda 2**:

```python
print(df.shape)
df.info()
```

**What each line does:**

- 🟢 `print(df.shape)`: shape gives the number of rows and columns.
- 🟢 `df.info()`: info lists every column with its name, how many values it has, and its data type.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to see the size and the columns of the data.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para ver el tamaño y las columnas de los datos.)
>
> 🟢 We have 7,000 rows and 12 columns. In the info table, I can see the three columns I need: ordered_at, category, and revenue_usd. Notice that ordered_at is stored as text, not as a date. I'll fix that next.
>
> (Tenemos 7.000 filas y 12 columnas. En la tabla de info veo las tres columnas que necesito: ordered_at, category y revenue_usd. Fíjense que ordered_at está guardada como texto, no como fecha. Eso lo arreglo ahora.)

Tiene que dar `(7000, 12)`, y `ordered_at` aparece como `object` o `str` (según la versión de pandas).

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for dates and missing values.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección sobre fechas y valores faltantes.)

Escribís `## 2. Dates and missing values`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that cleans the dates and checks for missing values.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que limpia las fechas y revisa los valores faltantes.)

Escribís la **celda 3**:

```python
df["ordered_at"] = pd.to_datetime(df["ordered_at"])
print(df.isna().sum())
```

**What each line does:**

- 🟢 `df["ordered_at"] = pd.to_datetime(df["ordered_at"])`: to_datetime converts the ordered_at text into real dates and replaces the column. Now we can group the data by month.
- 🟢 `print(df.isna().sum())`: this checks for missing values. isna marks each empty cell as True, and sum counts them per column. This matters because missing or dirty data can give us wrong totals.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to convert the dates and count the missing values.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para convertir las fechas y contar los valores faltantes.)
>
> 🟢 Every column shows zero, so there are no missing values and no more cleaning is needed.
>
> (Todas las columnas muestran cero, así que no hay valores faltantes y no hace falta limpiar más.)

Decí "every column shows zero" solo si tu resultado muestra ceros.

---

## 10:00–15:30 — Matplotlib y los tres gráficos

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for the charts.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para los gráficos.)

Escribís:

```markdown
## 3. Charts
Matplotlib is Python's most widely used charting library. pandas uses it when we call `.plot()`.
```

Mostrás el sitio oficial de Matplotlib unos 15 segundos:

> 🖱️ I'm clicking the plus button next to the browser tabs at the top, and typing matplotlib.org in the address bar, to show the official Matplotlib website.
>
> (Hago clic en el botón + al lado de las pestañas del navegador, arriba, y escribo matplotlib.org en la barra de direcciones, para mostrar el sitio oficial de Matplotlib.)
>
> 🟢 This is the official Matplotlib website. Matplotlib is the most popular charting library in Python. It draws bar charts, line charts, histograms, and much more. pandas uses it behind the scenes when we call plot. Colab already has it installed too.
>
> (Este es el sitio oficial de Matplotlib. Matplotlib es la librería de gráficos más popular de Python. Dibuja gráficos de barras, de líneas, histogramas y mucho más. pandas la usa por detrás cuando llamamos a plot. Colab también la tiene instalada.)
>
> 🖱️ I'm clicking the Colab tab at the top of the browser, to go back to my notebook.
>
> (Hago clic en la pestaña de Colab, arriba del navegador, para volver a mi notebook.)

### Gráfico 1: barras, ingresos por categoría

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell for the first chart, revenue by category.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código para el primer gráfico, ingresos por categoría.)

Escribís la **celda 4**:

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

> 🖱️ I'm clicking the Run cell button to the left of this cell, to draw the bar chart.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para dibujar el gráfico de barras.)

Te detenés un momento en el gráfico.

### Gráfico 2: líneas, ingresos mensuales

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell for the second chart, monthly revenue.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código para el segundo gráfico, ingresos mensuales.)

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

> 🖱️ I'm clicking the Run cell button to the left of this cell, to draw the line chart.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para dibujar el gráfico de líneas.)

### Gráfico 3: histograma, ingresos por línea de pedido

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell for the third chart, a histogram of revenue per order line.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código para el tercer gráfico, un histograma de ingresos por línea de pedido.)

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

> 🖱️ I'm clicking the Run cell button to the left of this cell, to draw the histogram.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para dibujar el histograma.)

---

## 15:30–18:30 — Interpretar los resultados y verificar los gráficos

**Valores de referencia.** Los calculé directamente del CSV, fuera de Colab (21/10/2026 y 23/10/2026). Compará con **tu** resultado antes de decirlos:

| Gráfico | Lo que muestran los datos |
| ------- | ------------------------- |
| Barras | Total: ~$774.000. Electronics ~$326.000 (42%), home ~$152.000 (20%), apparel ~$126.000 (16%), sports ~$81.000 (11%), beauty ~$51.000 (7%), grocery ~$37.000 (5%). Las tres primeras suman ~78%. Electronics sola (~$326.000) supera a las cuatro últimas juntas (~$295.000). |
| Líneas | Promedio ~$32.000 por mes; la mayoría entre $25.000 y $38.000. Pico en diciembre en los dos años (~$48.000 en 2023 y ~$44.000 en 2024). El mes más bajo es enero de 2024 (~$18.600), justo después del pico. Septiembre es flojo en los dos años (~$27.000 y ~$25.000). Total anual: 2023 ~$403.000 y 2024 ~$371.000 (~8% menos). |
| Histograma | Asimetría a la derecha. Mediana ~$60 y promedio ~$111. 3 de cada 4 líneas son de menos de ~$125 y 9 de cada 10, de menos de $250. Máximo ~$2.300. El 10% de líneas más grandes aporta ~41% de los ingresos. |

> 🖱️ I'm scrolling up in the notebook with the mouse wheel to the bar chart, to explain what it shows.
>
> (Subo por el notebook con la rueda del mouse hasta el gráfico de barras, para explicar qué muestra.)
>
> 🟢 In the bar chart, electronics is clearly the top category, with about 42 percent of all revenue. Grocery brings in the least, about 5 percent.
>
> (En el gráfico de barras, electrónica es claramente la categoría principal, con cerca del 42 por ciento de los ingresos. Grocery es la que menos genera, cerca del 5 por ciento.)
>
> 🟢 The top three categories, electronics, home, and apparel, bring in almost 80 percent of the revenue. In fact, electronics alone earns more than the four smallest categories combined.
>
> (Las tres primeras categorías, electrónica, hogar e indumentaria, generan casi el 80 por ciento de los ingresos. De hecho, electrónica sola gana más que las cuatro categorías más chicas juntas.)
>
> 🟢 For the business, this means electronics is the most important category to protect, for example by keeping it in stock. But depending so much on one category is also a risk.
>
> (Para el negocio, esto significa que electrónica es la categoría más importante para cuidar, por ejemplo manteniendo stock. Pero depender tanto de una categoría también es un riesgo.)
>
> 🖱️ I'm scrolling down to the line chart, below the bar chart, to explain the monthly trend.
>
> (Bajo hasta el gráfico de líneas, debajo del de barras, para explicar la tendencia mensual.)
>
> 🟢 In the line chart, revenue is fairly stable most of the year, around 32 thousand dollars a month, but it peaks in December in both years and drops in January. That looks like a holiday season effect.
>
> (En el gráfico de líneas, los ingresos son bastante estables la mayor parte del año, alrededor de 32 mil dólares por mes, pero tienen un pico en diciembre en los dos años y bajan en enero. Parece un efecto de la temporada de fiestas.)
>
> 🟢 January 2024 is the lowest month in the whole dataset, right after the December peak. September is also weak in both years.
>
> (Enero de 2024 es el mes más bajo de todo el dataset, justo después del pico de diciembre. Septiembre también es flojo en los dos años.)
>
> 🟢 Comparing the two years, 2024 brought in about 8 percent less than 2023. That's worth investigating, but with only two years of data we can't call it a trend yet.
>
> (Comparando los dos años, 2024 generó cerca de un 8 por ciento menos que 2023. Vale la pena investigarlo, pero con solo dos años de datos todavía no podemos decir que sea una tendencia.)
>
> 🖱️ I'm scrolling down to the histogram, at the bottom of the notebook, to explain how revenue is distributed.
>
> (Bajo hasta el histograma, al final del notebook, para explicar cómo se distribuyen los ingresos.)
>
> 🟢 The histogram is right-skewed. Most order lines are small, but there's a long tail of a few large ones.
>
> (El histograma tiene asimetría a la derecha. La mayoría de las líneas de pedido son chicas, pero hay una cola larga de pocas líneas grandes.)
>
> 🟢 About three out of four order lines are under 125 dollars, and nine out of ten are under 250. The largest one is about 2,300 dollars.
>
> (Cerca de tres de cada cuatro líneas de pedido son de menos de 125 dólares, y nueve de cada diez, de menos de 250. La más grande es de unos 2.300 dólares.)
>
> 🟢 Because of that tail, the average line, about 110 dollars, is almost double the median, about 60. So the median describes a typical order line better. And the largest 10 percent of lines bring in about 40 percent of the revenue.
>
> (Por esa cola, el promedio por línea, unos 110 dólares, es casi el doble de la mediana, unos 60. Así que la mediana describe mejor una línea de pedido típica. Y el 10 por ciento de líneas más grandes aporta cerca del 40 por ciento de los ingresos.)

Verificás en voz alta:

> 🟢 Let me verify: each chart has a title and labeled axes, the bar chart shows all six categories, and the line chart covers all twenty-four months.
>
> (Verifico: cada gráfico tiene título y ejes con nombre, el de barras muestra las seis categorías y el de líneas cubre los veinticuatro meses.)

Agregás la celda de observaciones. Coincide con los valores de referencia de arriba:

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a text cell with my observations, so the findings are saved next to the charts.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar una celda de texto con mis observaciones, así los hallazgos quedan guardados juntolo  a los gráficos.)

```markdown
## 4. Observations
- **Bar chart:** electronics is the top category, with about $326K of the $774K total (around 42%). Home and apparel follow, and grocery is the lowest (about $37K, around 5%).
  The top three categories bring in almost 80% of revenue, and electronics alone earns more than the four smallest categories combined.
- **Line chart:** monthly revenue averages about $32K and stays mostly between $25K and $38K. It peaks in December in both years (about $48K in 2023 and $44K in 2024) and drops in January, which suggests a holiday-season effect.
  January 2024 is the lowest month (about $18.6K), September is weak in both years, and 2024 brought in about 8% less than 2023.
- **Histogram:** the distribution is right-skewed. About 3 in 4 order lines are under $125, 9 in 10 are under $250, and the largest is about $2,300.
  The mean (about $111) is almost double the median (about $60), and the largest 10% of lines bring in about 41% of revenue.
```

Mientras escribís, decí en voz alta lo que vas escribiendo, para no quedarte en silencio.

---

## 18:30–19:30 — Resumen y propósito

> 🖱️ I'm clicking the plus Text button in the toolbar, to add the last text cell with the conclusion.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar la última celda de texto con la conclusión.)

```markdown
## 5. Conclusion
We loaded a public e-commerce CSV with pandas, checked its structure and missing values, converted dates,
and used Matplotlib to compare revenue by category, over time, and per order line.
Main findings: electronics leads revenue, revenue peaks in December, and most order lines are small.
```

> 🖱️ I'm scrolling up to the top of the notebook with the mouse wheel, to go over the whole analysis.
>
> (Subo hasta el principio del notebook con la rueda del mouse, para repasar todo el análisis.)
>
> 🟢 To sum up, I loaded a public e-commerce CSV with pandas, explored its structure, converted the dates, checked for missing values, and created three charts with Matplotlib.
>
> (Para resumir, cargué un CSV público de e-commerce con pandas, exploré su estructura, convertí las fechas, revisé los valores faltantes y creé tres gráficos con Matplotlib.)
>
> 🟢 The main findings: electronics leads revenue, sales peak in December, and most order lines are small.
>
> (Los hallazgos principales: electrónica lidera los ingresos, las ventas tienen su pico en diciembre y la mayoría de las líneas de pedido son chicas.)
>
> 🟢 The purpose of exploratory analysis is to understand the data before making decisions or building anything more complex.
>
> (El propósito del análisis exploratorio es entender los datos antes de tomar decisiones o construir algo más complejo.)

---

## 19:30–23:00 — Epílogo (3–4 minutos)

Revisá en las reglas de Odin qué tiene que tener el epílogo y ajustá este texto si piden algo distinto. Primero guardás el notebook:

> 🖱️ I'm opening the File menu at the top left of Colab and choosing Download, then Download .ipynb, to save the finished notebook for the deliverables.
>
> (Abro el menú File, arriba a la izquierda de Colab, y elijo Download y después Download .ipynb, para guardar el notebook terminado para los entregables.)

Después hablás mientras recorrés el notebook despacio:

> 🖱️ I'm scrolling slowly through the notebook with the mouse wheel, to go over the decisions I made.
>
> (Recorro despacio el notebook con la rueda del mouse, para repasar las decisiones que tomé.)
>
> 🟢 In this epilogue, I want to go over why I made each decision. I chose one chart for each question. A bar chart compares categories, a line chart shows change over time, and a histogram shows how values are distributed. Using the right chart for each question makes the answer easy to see.
>
> (En este epílogo quiero repasar por qué tomé cada decisión. Elegí un gráfico para cada pregunta. Un gráfico de barras compara categorías, uno de líneas muestra cambios en el tiempo y un histograma muestra cómo se distribuyen los valores. Usar el gráfico adecuado para cada pregunta hace que la respuesta sea fácil de ver.)
>
> 🟢 I kept the code short on purpose. pandas does the heavy work, like grouping and summing, in one line, and its plot function calls Matplotlib for us. That way, each step is easy to read and to check.
>
> (Mantuve el código corto a propósito. pandas hace el trabajo pesado, como agrupar y sumar, en una línea, y su función plot llama a Matplotlib por nosotros. Así cada paso es fácil de leer y de verificar.)
>
> 🟢 The most important step was converting the dates. Without it, I couldn't group the orders by month, and the line chart wouldn't work. This is a common problem: CSV files store everything as text, so we always need to check the data types first.
>
> (El paso más importante fue convertir las fechas. Sin eso no podía agrupar los pedidos por mes y el gráfico de líneas no funcionaría. Es un problema común: los CSV guardan todo como texto, así que siempre hay que revisar primero los tipos de datos.)
>
> 🟢 This analysis also has some limits. The data is synthetic, so the patterns don't come from a real store. We only have two years, which is not enough to confirm a long-term trend. And the dataset has a column called returned, which I didn't use, so these totals include orders that were later returned.
>
> (Este análisis también tiene algunos límites. Los datos son sintéticos, así que los patrones no vienen de una tienda real. Solo tenemos dos años, lo que no alcanza para confirmar una tendencia a largo plazo. Y el dataset tiene una columna llamada returned, que no usé, así que estos totales incluyen pedidos que después se devolvieron.)
>
> 🟢 As next steps, I could remove the returned orders, compare revenue by sales channel or by country, or look at which categories sell more in December. Each of these is just one more groupby and one more chart, with the same tools.
>
> (Como próximos pasos, podría quitar los pedidos devueltos, comparar los ingresos por canal de venta o por país, o ver qué categorías venden más en diciembre. Cada uno es solo un groupby más y un gráfico más, con las mismas herramientas.)
>
> 🟢 For a business, these findings could guide decisions like planning stock and marketing before December, and protecting the electronics category. That's the value of exploratory analysis: a few lines of code turn seven thousand rows into clear answers. Thanks for watching!
>
> (Para un negocio, estos hallazgos pueden orientar decisiones como planificar el stock y el marketing antes de diciembre, y cuidar la categoría de electrónica. Ese es el valor del análisis exploratorio: unas pocas líneas de código convierten siete mil filas en respuestas claras. ¡Gracias por mirar!)

Si al terminar el epílogo el reloj todavía no pasó los 15:00, no cortes. Seguí recorriendo los gráficos y explicándolos con más detalle hasta pasar cómodamente ese mínimo.

---

## Después de grabar

1. Ejecutá **Run full AutoQC**, no solo *Rerun failing*, para revisar los dos controles de narración.
2. Subí los **cuatro archivos por separado**: el **MP4**, el **ZIP original de TaskRecorder**, **Deliverables.zip** y **Metadata.rtf**.
