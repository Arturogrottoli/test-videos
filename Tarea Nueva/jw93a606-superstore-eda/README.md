# jw93a606 — Superstore Sales: análisis exploratorio con seaborn

Guion paso a paso para grabar la tarea **jw93a606**: importar el dataset público **Sample - Superstore** en **Google Colab** desde **Firefox**, limpiarlo y explorarlo con **pandas**, y crear **cinco gráficos con seaborn**, cada uno guardado como PNG. Los gráficos son: barras de ventas por categoría, línea de ingresos mensuales, histograma del valor de los pedidos, dispersión de precio contra cantidad y heatmap de correlaciones. La grabación tiene que durar **entre 15:00 y 50:59**. Este guion apunta a unos **27 minutos**, epílogo incluido.

**Cómo leer este guion:**

- Cada sección tiene tres partes: **Acción en pantalla**, **Narración exacta en inglés** y **Resultado esperado**.
- Las frases que empiezan con 🖱️ las decís **en el momento de hacer clic, desplazarte o escribir**. Siempre dicen **qué** elemento usás, **dónde** está en la pantalla y **por qué** lo usás. Son las que revisa AutoQC.
- Las frases que empiezan con 🟢 son la explicación que decís entre una acción y otra.
- Debajo de cada bloque de código, la lista **What each line does** explica cada línea en inglés. La leés en voz alta mientras escribís esa línea.
- Las traducciones al castellano van entre paréntesis y **no se leen**.
- Hacé una pausa de **~1 segundo después de cada clic**, y nunca te quedes **más de 45 segundos en silencio**.

> **Importante:** el Goal aprobado y las reglas vigentes de Odin tienen prioridad sobre este guion. Antes de grabar, comparalos.

---

## Pendientes antes de grabar (no los pude verificar yo)

| Dato | Estado | Qué hacer |
| ---- | ------ | --------- |
| Licencia **CC0** del dataset | **Sin verificar**: Kaggle no se pudo abrir desde acá. | Confirmá en la página de Kaggle, en el campo **License**, que dice *CC0: Public Domain*. Si dice otra cosa, avisá antes de grabar, porque el Goal dice CC0. |
| Link de Kaggle para **Final Notes** | Link probable: https://www.kaggle.com/datasets/vivek468/superstore-dataset-final | Confirmá que es la página desde donde descargaste el archivo y copiá ese link en Final Notes. |
| Nombres dentro de **Deliverables.zip** | En el repo no hay reglas de Odin sobre nombres. | Los nombres de abajo son una propuesta. Revisalos contra las reglas de Odin. |
| **Epílogo** | Las otras tareas tenían un epílogo de 3–4 minutos. | Revisá en las reglas de Odin si esta tarea lo pide y ajustá ese texto si piden algo distinto. |
| Versión de pandas en Colab | Probé el código con pandas 3.1, seaborn 0.13 y matplotlib 3.11. | Si Colab tiene otra versión, `df.info()` puede mostrar `object` en vez de `str` para el texto. La narración no depende de eso. |

---

## Archivos de la carpeta

```
jw93a606-superstore-eda/
├── README.md                 ← este guion
├── Sample - Superstore.csv   ← dataset descargado de Kaggle (9.994 filas, 21 columnas)
└── superstore_eda.ipynb      ← notebook de referencia, completo y en orden (sin ejecutar)
```

Para probar el notebook de referencia: en https://colab.research.google.com elegís **File → Upload notebook** y seleccionás `superstore_eda.ipynb`. Después subís `Sample - Superstore.csv` desde el panel **Files** y ejecutás **Runtime → Run all**. Ensayalo con esto, pero **no lo uses en la grabación**: en el video el notebook se crea desde cero.

---

## El dataset (verificado con el archivo)

`Sample - Superstore.csv`: pedidos de una tienda ficticia de Estados Unidos, de enero de 2014 a diciembre de 2017. Tiene 9.994 filas y 21 columnas, y **cada fila es una línea de un pedido** (un producto dentro de un pedido).

| Columna | Qué contiene | Dónde se usa |
| ------- | ------------ | ------------ |
| `Row ID` | Número de fila | Se excluye al buscar duplicados |
| `Order ID` | Identificador del pedido (un pedido puede tener varias filas) | Histograma (valor por pedido) |
| `Order Date` | Fecha del pedido, como **texto** `M/D/YYYY` | Gráfico de líneas |
| `Ship Date` | Fecha de envío, como **texto** `M/D/YYYY` | Limpieza |
| `Postal Code` | Código postal, leído como **número** | Limpieza |
| `Category` | Furniture, Office Supplies, Technology | Gráfico de barras |
| `Sales` | Venta de la línea, en dólares (ya con descuento) | Barras, líneas, histograma, heatmap |
| `Quantity` | Unidades (de 1 a 14) | Dispersión, heatmap |
| `Discount` | Descuento (de 0 a 0,8) | Heatmap |
| `Profit` | Ganancia, puede ser negativa | Heatmap |

El resto de las columnas son `Ship Mode`, `Customer ID`, `Customer Name`, `Segment`, `Country`, `City`, `State`, `Region`, `Product ID`, `Sub-Category` y `Product Name`.

**Problemas reales del archivo** (los encontrás y los arreglás en la grabación):

| Problema | Detalle | Cómo se arregla |
| -------- | ------- | --------------- |
| Codificación | No está en UTF-8: `pd.read_csv` sin opciones da `UnicodeDecodeError` | `encoding="latin-1"` |
| Fechas como texto | `Order Date` y `Ship Date` son texto, no fechas | `pd.to_datetime(..., format="%m/%d/%Y")` |
| Código postal como número | 449 códigos perdieron el cero inicial (01040 quedó como 1040) | `astype(str).str.zfill(5)` |
| Fila duplicada | 1 fila repetida si no se cuenta `Row ID` (pedido US-2014-150119) | `drop_duplicates(subset=...)` |
| No hay columna de precio | El Goal pide precio contra cantidad | Nueva columna `Unit Price = Sales / Quantity` |
| Valores faltantes | **No hay** (0 en todo el archivo) | Se revisa y se dice en voz alta |

---

## Antes de grabar

1. Leé el Goal aprobado y completá los **Pendientes** de arriba.
2. Copiá `Sample - Superstore.csv` al **Escritorio**, para encontrarlo rápido al subirlo.
3. Iniciá sesión en Google en Firefox antes de grabar, porque Colab la necesita para ejecutar código. No muestres tu correo ni datos privados.
4. Practicá una vez entera en un notebook nuevo, leyendo en voz alta todas las frases 🖱️ y 🟢, y cronometrá.
5. Prepará las cuatro pestañas de Firefox, en este orden:
   1. Colab (https://colab.research.google.com), con el cuadro **Open notebook** a la vista y sin crear todavía el notebook.
   2. pandas (https://pandas.pydata.org).
   3. matplotlib (https://matplotlib.org).
   4. seaborn (https://seaborn.pydata.org).
6. En Firefox, entrá a **Settings → General** y activá **Open previous windows and tabs**. Así, al abrirlo en la grabación, aparecen las cuatro pestañas. Maximizá la ventana, agrandá el zoom con `Ctrl + +` en cada pestaña y **cerrá Firefox**. Tiene que estar cerrado al empezar, porque el paso 1 del Goal es abrirlo. Probá cerrarlo y abrirlo una vez para confirmar que vuelven las cuatro pestañas.
7. Cerrá o minimizá las demás ventanas para que ninguna tape a otra, y también este guion si está en la misma pantalla.
8. En la grabación de dje548b6, AutoQC midió 23,5% de escritura. Para no subir ese porcentaje, ejecutá las celdas con el **botón Run** (mouse) y escribí solo el código y los títulos cortos. Revisá el límite vigente en las reglas de Odin.
9. Si las reglas piden escribir el código en pantalla, escribilo en la grabación y **no lo pegues**.
10. No uses herramientas de IA durante la grabación.
11. Sobre el dataset, en el video decís **de dónde** viene (Kaggle, licencia CC0), pero **no** mostrás ni explicás cómo se descarga. La descarga se hizo antes de grabar.

---

## 0:00–2:00 — Apertura: Firefox, Colab, pandas, matplotlib y seaborn

**Acción en pantalla:**

1. Empezás en el Escritorio, con Firefox cerrado.
2. Hacés clic en el ícono de **Firefox** en la barra de tareas, abajo de la pantalla. Se abre con las cuatro pestañas, en la primera (Colab).
3. Hacés clic en la segunda pestaña (pandas), arriba de la ventana.
4. Hacés clic en la tercera pestaña (matplotlib).
5. Hacés clic en la cuarta pestaña (seaborn).
6. Volvés a la primera pestaña (Colab).

Si Firefox no abre las pestañas, apretás `Ctrl + L`, escribís `colab.research.google.com` y apretás `Enter`, y seguís sin mostrar las otras páginas.

**Narración exacta en inglés:**

> 🟢 As a data analyst supporting an e-commerce team, I'll import a public sales dataset into Google Colab, clean and explore it with pandas, and create five charts with seaborn. The goal is to give the e-commerce manager a visual summary of the data.
>
> (Como analista de datos de un equipo de e-commerce, voy a importar un dataset público de ventas en Google Colab, limpiarlo y explorarlo con pandas, y crear cinco gráficos con seaborn. El objetivo es darle al gerente de e-commerce un resumen visual de los datos.)
>
> 🖱️ I'm clicking the Firefox icon in the taskbar, at the bottom of the screen, to open the browser.
>
> (Hago clic en el ícono de Firefox en la barra de tareas, abajo de la pantalla, para abrir el navegador.)
>
> 🟢 Firefox opens on Google Colab, in the first tab. Google Colab is a free Google tool that runs Python notebooks in the browser. The code runs in Google's cloud, so there's nothing to install. This is where I'll do the whole analysis.
>
> (Firefox se abre en Google Colab, en la primera pestaña. Google Colab es una herramienta gratuita de Google que ejecuta notebooks de Python en el navegador. El código corre en la nube de Google, así que no hay nada que instalar. Acá voy a hacer todo el análisis.)
>
> 🖱️ I'm clicking the second browser tab, at the top of the window, to show the official pandas website.
>
> (Hago clic en la segunda pestaña del navegador, arriba de la ventana, para mostrar el sitio oficial de pandas.)
>
> 🟢 This is pandas, a free Python library for tables of data. I'll use it to load the CSV file, find problems in the data, clean them, and group the sales by category, month, and order.
>
> (Esto es pandas, una librería gratuita de Python para tablas de datos. La voy a usar para cargar el archivo CSV, encontrar problemas en los datos, limpiarlos y agrupar las ventas por categoría, mes y pedido.)
>
> 🖱️ I'm clicking the third browser tab, at the top of the window, to show the official matplotlib website.
>
> (Hago clic en la tercera pestaña del navegador, arriba de la ventana, para mostrar el sitio oficial de matplotlib.)
>
> 🟢 This is matplotlib, the basic chart library for Python. I'll use it to set the size of each chart and to save each one as a PNG file.
>
> (Esto es matplotlib, la librería básica de gráficos de Python. La voy a usar para definir el tamaño de cada gráfico y para guardar cada uno como archivo PNG.)
>
> 🖱️ I'm clicking the fourth browser tab, at the top of the window, to show the official seaborn website.
>
> (Hago clic en la cuarta pestaña del navegador, arriba de la ventana, para mostrar el sitio oficial de seaborn.)
>
> 🟢 This is seaborn, a library built on top of matplotlib. It makes clear statistical charts with very little code. I'll use it to draw the five charts: a bar plot, a line plot, a histogram, a scatter plot, and a heatmap. pandas, matplotlib, and seaborn all come already installed in Colab.
>
> (Esto es seaborn, una librería construida sobre matplotlib. Hace gráficos estadísticos claros con muy poco código. La voy a usar para dibujar los cinco gráficos: barras, líneas, histograma, dispersión y heatmap. pandas, matplotlib y seaborn vienen ya instaladas en Colab.)
>
> 🖱️ I'm clicking the first browser tab, at the top left of the window, to go back to Google Colab.
>
> (Hago clic en la primera pestaña del navegador, arriba a la izquierda de la ventana, para volver a Google Colab.)

**Resultado esperado:** Firefox maximizado en la pestaña de Colab, con el cuadro **Open notebook** en el centro, después de mostrar las tres páginas oficiales.

---

## 2:00–3:45 — Notebook nuevo y subir el CSV

**Acción en pantalla:**

1. Hacés clic en **New notebook**, abajo del cuadro **Open notebook**. Si no aparece el cuadro, usás **File → New notebook in Drive**, arriba a la izquierda.
2. Hacés clic en el título (`Untitled0.ipynb`), arriba a la izquierda, escribís `superstore_eda.ipynb` y apretás `Enter`.
3. Hacés clic en el ícono **Files** (la carpeta), en la barra lateral izquierda.
4. Hacés clic en el ícono **Upload to session storage** (la hoja con una flecha hacia arriba), arriba del panel Files.
5. En la ventana de Firefox para elegir archivos, vas al **Escritorio**, seleccionás `Sample - Superstore.csv` y hacés clic en **Open**.
6. Si aparece el aviso de que los archivos se borran cuando se reinicia el entorno, hacés clic en **OK**.

**Narración exacta en inglés:**

> 🖱️ I'm clicking the New notebook button, at the bottom of the Open notebook dialog, to create a fresh notebook for this analysis.
>
> (Hago clic en el botón New notebook, abajo del cuadro Open notebook, para crear un notebook nuevo para este análisis.)
>
> 🖱️ I'm clicking the notebook title at the top left, and typing superstore underscore EDA dot ipynb, to give the notebook a clear name.
>
> (Hago clic en el título del notebook, arriba a la izquierda, y escribo superstore_eda.ipynb, para darle un nombre claro.)
>
> 🟢 EDA stands for exploratory data analysis: we look at the data, clean it, and use charts to understand it before drawing any conclusions.
>
> (EDA significa análisis exploratorio de datos: miramos los datos, los limpiamos y usamos gráficos para entenderlos antes de sacar conclusiones.)
>
> 🖱️ I'm clicking the Files icon, the folder in the left sidebar, to open the file panel.
>
> (Hago clic en el ícono Files, la carpeta de la barra lateral izquierda, para abrir el panel de archivos.)
>
> 🖱️ I'm clicking the Upload to session storage icon, at the top of the Files panel, to upload the dataset.
>
> (Hago clic en el ícono Upload to session storage, arriba del panel Files, para subir el dataset.)
>
> 🖱️ I'm selecting Sample dash Superstore dot csv on my Desktop and clicking Open, at the bottom right of the window, so the notebook can read it.
>
> (Selecciono Sample - Superstore.csv en el Escritorio y hago clic en Open, abajo a la derecha de la ventana, para que el notebook pueda leerlo.)
>
> 🟢 This is the Sample Superstore dataset. I downloaded it from Kaggle before recording, and it has a CC0 public domain license. It has the orders of a fictional US store from 2014 to 2017.
>
> (Este es el dataset Sample Superstore. Lo descargué de Kaggle antes de grabar y tiene licencia CC0 de dominio público. Tiene los pedidos de una tienda ficticia de Estados Unidos de 2014 a 2017.)

Si aparece el aviso: *"I'm clicking OK on this warning, in the center of the screen, to continue the upload. It only says that uploaded files are deleted when the session ends."*

**Resultado esperado:** notebook llamado `superstore_eda.ipynb` y `Sample - Superstore.csv` visible en el panel Files.

---

## 3:45–6:30 — Título y carga de los datos con pandas

**Acción en pantalla:**

1. Hacés clic en **+ Text**, en la barra de herramientas arriba a la izquierda, y escribís el título y el objetivo.
2. Hacés clic en **+ Code** y escribís la celda 1 **sin** `encoding="latin-1"`, es decir, terminando la línea en `pd.read_csv("Sample - Superstore.csv")`.
3. Hacés clic en **Run cell** (el ícono de play, a la izquierda de la celda).
4. Aparece un `UnicodeDecodeError`. Lo señalás con el mouse.
5. Hacés clic dentro de la celda, justo antes del paréntesis de cierre de `read_csv`, y agregás `, encoding="latin-1"`.
6. Hacés clic de nuevo en **Run cell**.
7. Señalás las columnas de la tabla con el mouse y te desplazás hacia la derecha en la salida.

Celda de texto:

```markdown
# Superstore Sales: Exploratory Data Analysis
Dataset: Sample - Superstore (Kaggle, CC0). Goal: clean and explore the orders with pandas, and create five seaborn charts that give the e-commerce manager a visual summary.
```

**Celda 1** (versión final, después de agregar el encoding):

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")
df = pd.read_csv("Sample - Superstore.csv", encoding="latin-1")
df.head()
```

**What each line does:**

- 🟢 `import pandas as pd`: this loads pandas, the Python library for tables of data, with its usual short name, pd.
- 🟢 `import seaborn as sns`: this loads seaborn, a chart library built on matplotlib. It makes clear, good-looking statistical charts with very little code.
- 🟢 `import matplotlib.pyplot as plt`: this loads pyplot from matplotlib. I'll use it to set the size of each chart, save it as a PNG file, and show it.
- 🟢 `sns.set_theme(style="whitegrid")`: this gives all the charts the same clean style, with a light grid that makes values easier to read.
- 🟢 `df = pd.read_csv(..., encoding="latin-1")`: read_csv reads the uploaded file into a DataFrame called df, which is a table with rows and columns. The encoding tells pandas how the text in the file is stored.
- 🟢 `df.head()`: this shows the first five rows, to check that the data loaded correctly.

**Narración exacta en inglés:**

> 🖱️ I'm clicking the plus Text button in the toolbar at the top left, to add a title and the goal of the notebook.
>
> (Hago clic en el botón + Text de la barra de herramientas, arriba a la izquierda, para agregar el título y el objetivo del notebook.)
>
> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that loads the libraries and the data.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que carga las librerías y los datos.)
>
> 🖱️ I'm clicking the Run cell button, the play icon to the left of the cell, to load the file.
>
> (Hago clic en el botón Run cell, el ícono de play a la izquierda de la celda, para cargar el archivo.)
>
> 🟢 We get a Unicode decode error. By default, pandas expects the file to be in UTF-8, but this file uses a different text encoding, so some special characters can't be read. This is the first sign that the data is not perfectly clean.
>
> (Aparece un error de decodificación Unicode. Por defecto, pandas espera que el archivo esté en UTF-8, pero este archivo usa otra codificación de texto, así que algunos caracteres especiales no se pueden leer. Es la primera señal de que los datos no están perfectamente limpios.)
>
> 🖱️ I'm clicking inside the cell, at the end of the read CSV line, and adding encoding equals latin one, to tell pandas how this file is stored.
>
> (Hago clic dentro de la celda, al final de la línea de read_csv, y agrego encoding="latin-1", para decirle a pandas cómo está guardado el archivo.)
>
> 🖱️ I'm clicking the Run cell button again, to the left of the cell, to load the data.
>
> (Hago clic otra vez en el botón Run cell, a la izquierda de la celda, para cargar los datos.)
>
> 🟢 Now it works. Each row is one product inside an order. For example, the first row is order CA 2016 152156, from November 8, 2016: a bookcase from the Furniture category, two units, sold for about 262 dollars, with a profit of about 42 dollars.
>
> (Ahora funciona. Cada fila es un producto dentro de un pedido. Por ejemplo, la primera fila es el pedido CA-2016-152156, del 8 de noviembre de 2016: una biblioteca de la categoría Furniture, dos unidades, vendida por unos 262 dólares, con una ganancia de unos 42 dólares.)
>
> 🖱️ I'm scrolling to the right in the table output, under the cell, to show the last columns.
>
> (Me desplazo a la derecha en la tabla de salida, debajo de la celda, para mostrar las últimas columnas.)
>
> 🟢 The columns I'll use most are Order Date, Category, Sales, Quantity, Discount, and Profit. Notice row four: it has a 45 percent discount and a negative profit of about 383 dollars. I'll come back to discounts and profit in the heatmap.
>
> (Las columnas que más voy a usar son Order Date, Category, Sales, Quantity, Discount y Profit. Fíjense en la fila cuatro: tiene un descuento del 45 por ciento y una ganancia negativa de unos 383 dólares. Vuelvo a los descuentos y la ganancia en el heatmap.)

**Resultado esperado:** primero el `UnicodeDecodeError`. Después, la tabla con las primeras 5 filas y 21 columnas. Como hay muchas columnas, Colab puede mostrar `...` en el medio.

---

## 6:30–9:30 — Inspeccionar los datos

**Acción en pantalla:**

1. **+ Text** → escribís `## 1. Inspect the data`.
2. **+ Code** → escribís la celda 2.
3. **Run cell**.
4. Bajás con la rueda del mouse por la salida y señalás cada parte mientras la nombrás.

**Celda 2:**

```python
print(df.shape)
df.info()
print("Missing values:", df.isna().sum().sum())
print("Duplicate rows:", df.drop(columns="Row ID").duplicated().sum())
print("Postal codes with 4 digits:", (df["Postal Code"] < 10000).sum())
```

**What each line does:**

- 🟢 `print(df.shape)`: shape gives the number of rows and columns.
- 🟢 `df.info()`: info lists every column with how many values it has and its data type. It prints by itself.
- 🟢 `print("Missing values:", df.isna().sum().sum())`: isna marks each empty cell. The first sum counts them per column, and the second sum adds them up for the whole table.
- 🟢 `print("Duplicate rows:", df.drop(columns="Row ID").duplicated().sum())`: I ignore Row ID, because it's different in every row even when the rest is identical. Then duplicated marks each row that repeats an earlier one, and sum counts them.
- 🟢 `print("Postal codes with 4 digits:", ...)`: US postal codes have five digits. If a code is lower than 10,000, it lost its leading zero when pandas read it as a number.

**Narración exacta en inglés:**

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading called Inspect the data.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección llamado Inspect the data.)
>
> 🟢 Before I make any chart, I want to check the quality of the data. A chart built on dirty data can give the manager the wrong message.
>
> (Antes de hacer cualquier gráfico, quiero revisar la calidad de los datos. Un gráfico hecho con datos sucios le puede dar al gerente un mensaje equivocado.)
>
> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that looks for problems.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que busca problemas.)
>
> 🖱️ I'm clicking the Run cell button to the left of this cell, to inspect the data.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para inspeccionar los datos.)
>
> 🖱️ I'm scrolling down through the output with the mouse wheel, to go over each result.
>
> (Bajo por la salida con la rueda del mouse, para repasar cada resultado.)
>
> 🟢 We have 9,994 rows and 21 columns. In info, every column has 9,994 non-null values, and the missing values count confirms it: zero. So there are no missing values to fix.
>
> (Tenemos 9.994 filas y 21 columnas. En info, cada columna tiene 9.994 valores no nulos, y el conteo de faltantes lo confirma: cero. Así que no hay valores faltantes para arreglar.)
>
> 🟢 But there are other problems. First, look at the data types: Order Date and Ship Date are stored as text, not as dates. With text, pandas can't group the sales by month, so I need to convert them.
>
> (Pero hay otros problemas. Primero, miren los tipos de datos: Order Date y Ship Date están guardadas como texto, no como fechas. Con texto, pandas no puede agrupar las ventas por mes, así que tengo que convertirlas.)
>
> 🟢 Second, Postal Code is stored as a number, int64. A postal code is a label, not a quantity, and 449 codes lost their leading zero. For example, a code like 01040 became 1040.
>
> (Segundo, Postal Code está guardado como número, int64. Un código postal es una etiqueta, no una cantidad, y 449 códigos perdieron el cero inicial. Por ejemplo, un código como 01040 quedó como 1040.)
>
> 🟢 And third, there is one duplicate row. The same product appears twice in the same order, with the same values, so it would count that sale twice.
>
> (Y tercero, hay una fila duplicada. El mismo producto aparece dos veces en el mismo pedido, con los mismos valores, así que esa venta se contaría dos veces.)

**Resultado esperado:** `(9994, 21)`, la tabla de `info` con 9.994 no nulos en todas las columnas, `Missing values: 0`, `Duplicate rows: 1` y `Postal codes with 4 digits: 449`.

---

## 9:30–12:30 — Limpiar los datos y resumen numérico

**Acción en pantalla:**

1. **+ Text** → escribís `## 2. Clean the data`.
2. **+ Code** → escribís la celda 3 → **Run cell**.
3. **+ Code** → escribís la celda 4 → **Run cell**.
4. Señalás con el mouse las filas `min`, `50%` y `max` de la tabla.

**Celda 3:**

```python
df = df.drop_duplicates(subset=df.columns.drop("Row ID"))
df["Order Date"] = pd.to_datetime(df["Order Date"], format="%m/%d/%Y")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%m/%d/%Y")
df["Postal Code"] = df["Postal Code"].astype(str).str.zfill(5)
df["Unit Price"] = df["Sales"] / df["Quantity"]
print(df.shape)
print(df["Order Date"].min(), "to", df["Order Date"].max())
df[["Order Date", "Ship Date", "Postal Code", "Unit Price"]].dtypes
```

**What each line does:**

- 🟢 `df = df.drop_duplicates(subset=df.columns.drop("Row ID"))`: this removes the duplicate row. subset tells pandas to compare every column except Row ID.
- 🟢 `df["Order Date"] = pd.to_datetime(..., format="%m/%d/%Y")`: to_datetime turns the text into real dates. The format says the text is month, day, and a four-digit year, so pandas doesn't confuse the day and the month.
- 🟢 `df["Ship Date"] = ...`: the same conversion for the ship date.
- 🟢 `df["Postal Code"] = df["Postal Code"].astype(str).str.zfill(5)`: astype(str) turns the codes into text, and zfill(5) adds zeros on the left until each code has five digits.
- 🟢 `df["Unit Price"] = df["Sales"] / df["Quantity"]`: the dataset has no price column, so I calculate the price per unit by dividing the sales of each line by its quantity. Sales already includes the discount, so this is the price the customer actually paid per unit.
- 🟢 `print(df.shape)`: this shows the new size of the table.
- 🟢 `print(df["Order Date"].min(), "to", df["Order Date"].max())`: now that the dates are real dates, I can find the first and the last order.
- 🟢 `df[[...]].dtypes`: this shows the new data types of the columns I changed.

**Celda 4:**

```python
df[["Sales", "Quantity", "Discount", "Profit", "Unit Price"]].describe().round(2)
```

- 🟢 `describe().round(2)`: describe gives a summary of each number column: count, mean, standard deviation, minimum, quartiles, and maximum. round(2) keeps two decimals.

**Narración exacta en inglés:**

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for cleaning.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para la limpieza.)
>
> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that fixes these problems.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que arregla estos problemas.)
>
> 🖱️ I'm clicking the Run cell button to the left of this cell, to clean the data.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para limpiar los datos.)
>
> 🟢 Now we have 9,993 rows, one less because of the duplicate, and 22 columns, because I added Unit Price. The orders go from January 3, 2014, to December 30, 2017: four full years. Order Date and Ship Date are now datetime, Postal Code is text, and Unit Price is a decimal number.
>
> (Ahora tenemos 9.993 filas, una menos por el duplicado, y 22 columnas, porque agregué Unit Price. Los pedidos van del 3 de enero de 2014 al 30 de diciembre de 2017: cuatro años completos. Order Date y Ship Date ahora son fechas, Postal Code es texto y Unit Price es un número decimal.)
>
> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell with a summary of the number columns.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código con un resumen de las columnas numéricas.)
>
> 🖱️ I'm clicking the Run cell button to the left of this cell, to see the summary.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para ver el resumen.)
>
> 🟢 The median sale per line is about 54 dollars, but the mean is about 230, and the maximum is more than 22,000. When the mean is much higher than the median, a few very large sales pull the average up. That's important for the histogram.
>
> (La venta mediana por línea es de unos 54 dólares, pero el promedio es de unos 230, y el máximo pasa los 22.000. Cuando el promedio es mucho más alto que la mediana, unas pocas ventas muy grandes tiran el promedio para arriba. Eso es importante para el histograma.)
>
> 🟢 Quantity goes from 1 to 14 units, with a median of 3. Discount goes from 0 to 80 percent. Profit goes from a loss of about 6,600 dollars to a gain of about 8,400. And the unit price goes from 34 cents to about 3,773 dollars, with a median of about 16 dollars.
>
> (Quantity va de 1 a 14 unidades, con una mediana de 3. Discount va de 0 a 80 por ciento. Profit va de una pérdida de unos 6.600 dólares a una ganancia de unos 8.400. Y el precio unitario va de 34 centavos a unos 3.773 dólares, con una mediana de unos 16 dólares.)
>
> 🟢 The data is clean now, so I can start with the five charts.
>
> (Los datos ya están limpios, así que puedo empezar con los cinco gráficos.)

**Resultado esperado:** `(9993, 22)`, `2014-01-03 00:00:00 to 2017-12-30 00:00:00`, los tipos `datetime64`, `str` (u `object`), `str` (u `object`) y `float64`, y después la tabla de `describe` con los valores de la sección **Valores de referencia**.

---

## 12:30–14:00 — Gráfico 1: barras de ventas por categoría

**Acción en pantalla:**

1. **+ Text** → escribís `## 3. Visualizations`.
2. **+ Code** → escribís la celda 5 → **Run cell**.
3. Señalás cada barra de izquierda a derecha.

**Celda 5:**

```python
plt.figure(figsize=(8, 5))
ax = sns.barplot(data=df, x="Category", y="Sales", estimator="sum", errorbar=None)
ax.set(title="Total Sales by Category", xlabel="Category", ylabel="Total sales (USD)")
plt.savefig("01_bar_sales_by_category.png", dpi=150, bbox_inches="tight")
plt.show()
```

**What each line does:**

- 🟢 `plt.figure(figsize=(8, 5))`: this creates a new chart, 8 units wide and 5 tall, so each chart starts clean.
- 🟢 `sns.barplot(..., estimator="sum", errorbar=None)`: barplot draws one bar per category. estimator="sum" makes each bar the total sales of that category, instead of the average. errorbar=None removes the error lines, because I want totals, not estimates.
- 🟢 `ax.set(title=..., xlabel=..., ylabel=...)`: this adds the title and the labels of both axes, so the chart is clear on its own.
- 🟢 `plt.savefig("01_bar_sales_by_category.png", dpi=150, bbox_inches="tight")`: this saves the chart as a PNG file. dpi=150 gives a sharp image, and bbox_inches="tight" keeps the labels from being cut off. I save it before show, because show clears the chart.
- 🟢 `plt.show()`: this displays the chart in the notebook.

**Narración exacta en inglés:**

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for the visualizations.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para las visualizaciones.)
>
> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell for the first chart, a bar plot of sales by category.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código para el primer gráfico, un gráfico de barras de ventas por categoría.)
>
> 🖱️ I'm clicking the Run cell button to the left of this cell, to draw and save the bar plot.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para dibujar y guardar el gráfico de barras.)
>
> 🟢 Technology has the highest total sales, about 836,000 dollars. Furniture follows with about 742,000, and Office Supplies has about 719,000. The three categories are close, but Technology leads.
>
> (Technology tiene las ventas totales más altas, unos 836.000 dólares. Le sigue Furniture con unos 742.000, y Office Supplies tiene unos 719.000. Las tres categorías están cerca, pero Technology va primera.)
>
> 🟢 Something interesting: Office Supplies has about 6,000 of the almost 10,000 lines, the most by far, but the lowest sales. Those products are cheap, so they sell often but bring less money.
>
> (Algo interesante: Office Supplies tiene unas 6.000 de las casi 10.000 líneas, por lejos la mayor cantidad, pero las ventas más bajas. Son productos baratos: se venden seguido pero traen menos dinero.)

**Resultado esperado:** tres barras con título y etiquetas en los dos ejes, en este orden: Furniture ≈ 742K, Office Supplies ≈ 719K y Technology ≈ 836K. El archivo `01_bar_sales_by_category.png` queda guardado en la sesión.

---

## 14:00–15:45 — Gráfico 2: línea de ingresos mensuales

**Acción en pantalla:**

1. **+ Code** → escribís la celda 6 → **Run cell**.
2. Seguís la línea con el mouse de izquierda a derecha y señalás los picos de fin de año.

**Celda 6:**

```python
monthly = df.resample("MS", on="Order Date")["Sales"].sum().reset_index()
plt.figure(figsize=(12, 5))
ax = sns.lineplot(data=monthly, x="Order Date", y="Sales", marker="o")
ax.set(title="Monthly Revenue, 2014 to 2017", xlabel="Month", ylabel="Revenue (USD)")
plt.savefig("02_line_monthly_revenue.png", dpi=150, bbox_inches="tight")
plt.show()
```

**What each line does:**

- 🟢 `monthly = df.resample("MS", on="Order Date")["Sales"].sum().reset_index()`: resample groups the orders by month, using the dates I converted. MS means month start, so each month is labeled with its first day. sum adds the sales of each month, and reset_index turns the result back into a table with two columns.
- 🟢 `plt.figure(figsize=(12, 5))`: this chart is wider, because it shows 48 months.
- 🟢 `sns.lineplot(..., marker="o")`: lineplot connects the months with a line, and the markers show a dot for each month.
- 🟢 `ax.set(...)`: the title and the axis labels.
- 🟢 `plt.savefig("02_line_monthly_revenue.png", ...)`: this saves the second PNG.
- 🟢 `plt.show()`: this displays the chart.

**Narración exacta en inglés:**

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell for the second chart, the monthly revenue trend.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código para el segundo gráfico, la tendencia de ingresos mensuales.)
>
> 🟢 This chart only works because I converted Order Date to real dates. With text, pandas couldn't group the orders by month.
>
> (Este gráfico solo funciona porque convertí Order Date en fechas reales. Con texto, pandas no podría agrupar los pedidos por mes.)
>
> 🖱️ I'm clicking the Run cell button to the left of this cell, to draw and save the line plot.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para dibujar y guardar el gráfico de líneas.)
>
> 🟢 There are two clear patterns. First, growth: yearly revenue goes from about 484,000 dollars in 2014 to about 733,000 in 2017. 2015 was a little lower than 2014, and then it grew strongly in 2016 and 2017.
>
> (Hay dos patrones claros. Primero, crecimiento: los ingresos anuales van de unos 484.000 dólares en 2014 a unos 733.000 en 2017. 2015 fue un poco más bajo que 2014, y después creció fuerte en 2016 y 2017.)
>
> 🟢 Second, seasonality: every year, revenue peaks in September, November, and December, and drops in January and February. The best month is November 2017, with about 118,000 dollars, and the lowest is February 2014, with about 4,500.
>
> (Segundo, estacionalidad: todos los años, los ingresos tienen picos en septiembre, noviembre y diciembre, y bajan en enero y febrero. El mejor mes es noviembre de 2017, con unos 118.000 dólares, y el más bajo es febrero de 2014, con unos 4.500.)

**Resultado esperado:** una línea de 48 puntos, de enero de 2014 a diciembre de 2017, con picos a fin de cada año y el máximo en noviembre de 2017. El archivo `02_line_monthly_revenue.png` queda guardado.

---

## 15:45–17:30 — Gráfico 3: histograma del valor de los pedidos

**Acción en pantalla:**

1. **+ Code** → escribís la celda 7 → **Run cell**.
2. Señalás el eje horizontal (10, 100, 1.000, 10.000) y la zona más alta del histograma.

**Celda 7:**

```python
order_values = df.groupby("Order ID")["Sales"].sum()
plt.figure(figsize=(8, 5))
ax = sns.histplot(order_values, bins=40, log_scale=True)
ax.set(title="Distribution of Order Values", xlabel="Order value (USD, log scale)", ylabel="Number of orders")
plt.savefig("03_hist_order_values.png", dpi=150, bbox_inches="tight")
plt.show()
```

**What each line does:**

- 🟢 `order_values = df.groupby("Order ID")["Sales"].sum()`: each row is one product, but an order can have several products. groupby adds up the sales of each Order ID, so I get the total value of each order.
- 🟢 `plt.figure(figsize=(8, 5))`: a new chart.
- 🟢 `sns.histplot(order_values, bins=40, log_scale=True)`: a histogram splits the order values into 40 ranges, called bins, and each bar counts how many orders fall in that range. log_scale=True uses a logarithmic axis: each step is ten times bigger, 10, 100, 1,000. Without it, almost all orders would be squeezed into the first bar, because a few orders are huge.
- 🟢 `ax.set(...)`: the title and the labels. The x label says log scale, so nobody misreads it.
- 🟢 `plt.savefig("03_hist_order_values.png", ...)`: this saves the third PNG.
- 🟢 `plt.show()`: this displays the chart.

**Narración exacta en inglés:**

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell for the third chart, a histogram of order values.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código para el tercer gráfico, un histograma del valor de los pedidos.)
>
> 🖱️ I'm clicking the Run cell button to the left of this cell, to draw and save the histogram.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para dibujar y guardar el histograma.)
>
> 🟢 There are 5,009 orders. Notice the horizontal axis: 10, 100, 1,000, 10,000. Each step is ten times bigger, because I used a log scale.
>
> (Hay 5.009 pedidos. Fíjense en el eje horizontal: 10, 100, 1.000, 10.000. Cada paso es diez veces más grande, porque usé una escala logarítmica.)
>
> 🟢 Most orders are between about 10 and 1,000 dollars, and the median order is about 152 dollars. About 42 percent of the orders are under 100 dollars. On the right, there's a long tail: 27 orders are over 5,000 dollars, and the biggest is about 23,700.
>
> (La mayoría de los pedidos están entre unos 10 y 1.000 dólares, y el pedido mediano es de unos 152 dólares. Cerca del 42 por ciento de los pedidos son de menos de 100 dólares. A la derecha hay una cola larga: 27 pedidos pasan los 5.000 dólares, y el más grande es de unos 23.700.)
>
> 🟢 For the manager, this means the typical customer spends around 150 dollars, but a small group of very large orders brings a lot of revenue.
>
> (Para el gerente, esto significa que el cliente típico gasta unos 150 dólares, pero un grupo chico de pedidos muy grandes trae muchos ingresos.)

**Resultado esperado:** un histograma con forma de campana sobre el eje logarítmico, con el pico entre 100 y 1.000 USD, título y etiquetas en los dos ejes. El archivo `03_hist_order_values.png` queda guardado.

---

## 17:30–19:00 — Gráfico 4: dispersión de precio contra cantidad

**Acción en pantalla:**

1. **+ Code** → escribís la celda 8 → **Run cell**.
2. Señalás las franjas horizontales de puntos (una por cada cantidad) y recorrés el eje de precios.

**Celda 8:**

```python
plt.figure(figsize=(8, 5))
ax = sns.scatterplot(data=df, x="Unit Price", y="Quantity", alpha=0.3)
ax.set(xscale="log", title="Unit Price vs. Quantity", xlabel="Unit price (USD, log scale)", ylabel="Quantity per order line")
plt.savefig("04_scatter_price_vs_quantity.png", dpi=150, bbox_inches="tight")
plt.show()
```

**What each line does:**

- 🟢 `plt.figure(figsize=(8, 5))`: a new chart.
- 🟢 `sns.scatterplot(data=df, x="Unit Price", y="Quantity", alpha=0.3)`: a scatter plot draws one dot per order line, with the unit price I calculated on the horizontal axis and the quantity on the vertical axis. alpha=0.3 makes the dots partly transparent, so darker areas show where many dots overlap.
- 🟢 `ax.set(xscale="log", ...)`: the prices go from 34 cents to more than 3,000 dollars, so I use a log scale on the price axis again. Then come the title and the labels.
- 🟢 `plt.savefig("04_scatter_price_vs_quantity.png", ...)`: this saves the fourth PNG.
- 🟢 `plt.show()`: this displays the chart.

**Narración exacta en inglés:**

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell for the fourth chart, a scatter plot of price versus quantity.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código para el cuarto gráfico, un gráfico de dispersión de precio contra cantidad.)
>
> 🟢 The question here is: do customers buy fewer units when the price is higher?
>
> (La pregunta acá es: ¿los clientes compran menos unidades cuando el precio es más alto?)
>
> 🖱️ I'm clicking the Run cell button to the left of this cell, to draw and save the scatter plot.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para dibujar y guardar el gráfico de dispersión.)
>
> 🟢 The dots form horizontal lines, because quantity is always a whole number, from 1 to 14. And each line covers the whole range of prices, from under 1 dollar to more than 1,000.
>
> (Los puntos forman líneas horizontales, porque la cantidad siempre es un número entero, de 1 a 14. Y cada línea cubre todo el rango de precios, desde menos de 1 dólar hasta más de 1.000.)
>
> 🟢 So the answer is no: in this dataset, price and quantity are not related. Customers buy about 3 or 4 units on average, whether the product costs 5 dollars or 500. I'll confirm this with a number in the heatmap.
>
> (Así que la respuesta es no: en este dataset, el precio y la cantidad no están relacionados. Los clientes compran en promedio unas 3 o 4 unidades, ya sea que el producto cueste 5 dólares o 500. Lo voy a confirmar con un número en el heatmap.)

**Resultado esperado:** franjas horizontales de puntos en las cantidades 1 a 14, repartidas sobre todo el eje de precios (log), con título y etiquetas en los dos ejes. El archivo `04_scatter_price_vs_quantity.png` queda guardado.

---

## 19:00–20:30 — Gráfico 5: heatmap de correlaciones

**Acción en pantalla:**

1. **+ Code** → escribís la celda 9 → **Run cell**.
2. Señalás cada casillero mientras lo nombrás.

**Celda 9:**

```python
numeric = ["Sales", "Quantity", "Discount", "Profit", "Unit Price"]
plt.figure(figsize=(7, 5))
ax = sns.heatmap(df[numeric].corr(), annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1)
ax.set_title("Correlation Between Numeric Variables")
plt.savefig("05_heatmap_correlations.png", dpi=150, bbox_inches="tight")
plt.show()
```

**What each line does:**

- 🟢 `numeric = [...]`: this is the list of number columns I want to compare. I leave out Row ID and Postal Code, because they are labels, not measurements.
- 🟢 `plt.figure(figsize=(7, 5))`: a new chart.
- 🟢 `sns.heatmap(df[numeric].corr(), ...)`: corr calculates the correlation between every pair of columns, a number from minus 1 to 1. Close to 1 means they go up together, close to minus 1 means one goes up when the other goes down, and close to 0 means no relationship. heatmap colors each value: annot=True writes the number in each box, fmt=".2f" uses two decimals, coolwarm uses red for positive and blue for negative, and vmin and vmax fix the scale from minus 1 to 1.
- 🟢 `ax.set_title(...)`: the title. The variable names already label both axes.
- 🟢 `plt.savefig("05_heatmap_correlations.png", ...)`: this saves the fifth PNG.
- 🟢 `plt.show()`: this displays the chart.

**Narración exacta en inglés:**

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell for the last chart, a heatmap of correlations.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código para el último gráfico, un heatmap de correlaciones.)
>
> 🖱️ I'm clicking the Run cell button to the left of this cell, to draw and save the heatmap.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para dibujar y guardar el heatmap.)
>
> 🟢 The diagonal is always 1, because each variable is perfectly related to itself. The strongest value is Sales and Unit Price, 0.89. That's expected, because I calculated Unit Price from Sales.
>
> (La diagonal siempre es 1, porque cada variable está perfectamente relacionada consigo misma. El valor más fuerte es Sales con Unit Price, 0,89. Es esperable, porque calculé Unit Price a partir de Sales.)
>
> 🟢 Sales and Profit have 0.48, a moderate positive relationship: bigger sales usually bring more profit. And Quantity and Unit Price have zero, which confirms what we saw in the scatter plot.
>
> (Sales y Profit tienen 0,48, una relación positiva moderada: las ventas más grandes suelen traer más ganancia. Y Quantity con Unit Price da cero, lo que confirma lo que vimos en el gráfico de dispersión.)
>
> 🟢 The most useful number for the manager is Discount and Profit: minus 0.22, the only blue box. Higher discounts go with lower profit. Remember row four, with a 45 percent discount and a loss. That doesn't prove the discounts cause the losses, but it's worth reviewing.
>
> (El número más útil para el gerente es Discount con Profit: menos 0,22, el único casillero azul. Los descuentos más altos van con menos ganancia. Acuérdense de la fila cuatro, con un descuento del 45 por ciento y una pérdida. Eso no prueba que los descuentos causen las pérdidas, pero vale la pena revisarlo.)

**Resultado esperado:** una matriz de 5 × 5 con números de dos decimales, título y escala de color de −1 a 1. El archivo `05_heatmap_correlations.png` queda guardado.

---

## 20:30–22:00 — Observaciones en el notebook

**Acción en pantalla:**

1. **+ Text** → escribís las observaciones mientras las decís en voz alta.

```markdown
## 4. Observations
- **Data:** 9,994 rows and no missing values. We removed 1 duplicate, fixed the dates and the postal codes, and added Unit Price.
- **Category:** Technology has the highest sales, about $836K.
- **Trend:** revenue grows from about $484K in 2014 to $733K in 2017, with peaks at the end of each year.
- **Orders:** the median order is about $152, but a few orders are over $5,000.
- **Price vs. quantity:** no relationship (correlation 0.00).
- **Discount:** higher discounts go with lower profit (-0.22).
```

**Narración exacta en inglés:**

> 🖱️ I'm clicking the plus Text button in the toolbar, to write my observations below the charts.
>
> (Hago clic en el botón + Text de la barra de herramientas, para escribir mis observaciones debajo de los gráficos.)
>
> 🟢 I'm writing down the six main findings, so the manager can read the summary without running any code.
>
> (Escribo los seis hallazgos principales, para que el gerente pueda leer el resumen sin ejecutar código.)

Mientras escribís cada punto, decilo en voz alta en inglés tal como está escrito.

**Resultado esperado:** una celda de texto con el título `4. Observations` y seis puntos.

---

## 22:00–23:45 — Descargar el notebook y los cinco PNG

**Acción en pantalla:**

1. En el panel **Files** de la izquierda, hacés clic en el ícono **Refresh** (la flecha circular) si todavía no ves los cinco PNG.
2. Para cada PNG, en orden del 01 al 05: pasás el mouse sobre el archivo, hacés clic en los **tres puntos** (⋮) a la derecha del nombre y elegís **Download**.
3. Si Firefox pregunta qué hacer con el archivo, elegís **Save File** y **OK**.
4. Abrís el menú **File**, arriba a la izquierda de Colab → **Download** → **Download .ipynb**.
5. Hacés clic en el ícono de **descargas** de Firefox (la flecha hacia abajo, arriba a la derecha) para mostrar los seis archivos descargados.

**Narración exacta en inglés:**

> 🖱️ I'm clicking the Refresh icon at the top of the Files panel, on the left, to show the PNG files the notebook just saved.
>
> (Hago clic en el ícono Refresh, arriba del panel Files, a la izquierda, para mostrar los archivos PNG que el notebook acaba de guardar.)
>
> 🟢 Here are the five charts, saved as PNG files, numbered in the same order as the notebook.
>
> (Acá están los cinco gráficos, guardados como archivos PNG y numerados en el mismo orden que en el notebook.)
>
> 🖱️ I'm clicking the three dots next to the first file, 01 bar sales by category, in the Files panel, and choosing Download, to save it to my computer.
>
> (Hago clic en los tres puntos al lado del primer archivo, 01_bar_sales_by_category, en el panel Files, y elijo Download, para guardarlo en mi computadora.)
>
> 🖱️ I'm doing the same for the second file, the monthly revenue line plot.
>
> (Hago lo mismo con el segundo archivo, el gráfico de líneas de ingresos mensuales.)
>
> 🖱️ Now the third file, the histogram of order values.
>
> (Ahora el tercer archivo, el histograma del valor de los pedidos.)
>
> 🖱️ The fourth file, the price versus quantity scatter plot.
>
> (El cuarto archivo, el gráfico de dispersión de precio contra cantidad.)
>
> 🖱️ And the fifth file, the correlation heatmap.
>
> (Y el quinto archivo, el heatmap de correlaciones.)
>
> 🖱️ I'm opening the File menu at the top left of Colab, choosing Download, and then Download dot ipynb, to save the executed notebook with all its outputs.
>
> (Abro el menú File, arriba a la izquierda de Colab, elijo Download y después Download .ipynb, para guardar el notebook ejecutado con todas sus salidas.)
>
> 🖱️ I'm clicking the Downloads arrow at the top right of Firefox, to check that all six files were downloaded.
>
> (Hago clic en la flecha de descargas, arriba a la derecha de Firefox, para comprobar que se descargaron los seis archivos.)
>
> 🟢 The notebook and the five PNG files are downloaded. These are the deliverables for this task.
>
> (El notebook y los cinco archivos PNG están descargados. Son los entregables de esta tarea.)

Decí la última frase **solo después** de ver los seis archivos en la lista de descargas.

**Resultado esperado:** seis archivos en la lista de descargas de Firefox: `superstore_eda.ipynb` y los cinco PNG con los nombres del 01 al 05.

---

## 23:45–26:45 — Epílogo: resumen para el gerente (3 minutos)

Revisá en las reglas de Odin qué tiene que tener el epílogo y ajustá este texto si piden algo distinto.

**Acción en pantalla:**

1. Cerrás el panel de descargas con `Esc`.
2. Subís con la rueda del mouse hasta el principio del notebook y vas bajando: cada frase va cuando la sección correspondiente está en pantalla.

**Narración exacta en inglés:**

> 🖱️ I'm pressing Escape to close the downloads panel, and scrolling up to the top of the notebook with the mouse wheel, to go over the whole analysis.
>
> (Aprieto Escape para cerrar el panel de descargas y subo con la rueda del mouse hasta el principio del notebook, para repasar todo el análisis.)
>
> 🟢 Let me summarize. I loaded the Superstore dataset with pandas. The first problem was the text encoding, which I fixed with latin one.
>
> (Les resumo. Cargué el dataset Superstore con pandas. El primer problema fue la codificación del texto, que arreglé con latin-1.)
>
> 🖱️ I'm scrolling down to sections 1 and 2, Inspect and Clean the data.
>
> (Bajo hasta las secciones 1 y 2, Inspect y Clean the data.)
>
> 🟢 There were no missing values, but the data still needed cleaning: the dates were text, 449 postal codes had lost their leading zero, and there was one duplicate row. I also added a Unit Price column, because the dataset has no price.
>
> (No había valores faltantes, pero los datos igual necesitaban limpieza: las fechas eran texto, 449 códigos postales habían perdido el cero inicial y había una fila duplicada. También agregué la columna Unit Price, porque el dataset no tiene precio.)
>
> 🖱️ I'm scrolling down to section 3, Visualizations, to show the five charts again.
>
> (Bajo hasta la sección 3, Visualizations, para mostrar otra vez los cinco gráficos.)
>
> 🟢 The bar plot shows that Technology sells the most. The line plot shows that revenue grows every year after 2015, with peaks at the end of each year. The histogram shows that the typical order is about 150 dollars, with a few very large ones. The scatter plot and the heatmap show that price doesn't change how many units people buy, and that higher discounts go with lower profit.
>
> (El gráfico de barras muestra que Technology es lo que más vende. El de líneas muestra que los ingresos crecen todos los años desde 2015, con picos a fin de cada año. El histograma muestra que el pedido típico es de unos 150 dólares, con algunos muy grandes. El de dispersión y el heatmap muestran que el precio no cambia cuántas unidades se compran, y que los descuentos más altos van con menos ganancia.)
>
> 🟢 A few decisions I made: I checked the data before plotting anything, because the duplicate would have counted a sale twice, and text dates make a monthly chart impossible. I used a log scale for order values and prices, because a few huge values would hide everything else. And I saved each chart before showing it, so the PNG files are complete.
>
> (Algunas decisiones que tomé: revisé los datos antes de graficar nada, porque el duplicado habría contado una venta dos veces, y con fechas como texto no se puede hacer un gráfico mensual. Usé escala logarítmica para el valor de los pedidos y los precios, porque unos pocos valores enormes taparían todo lo demás. Y guardé cada gráfico antes de mostrarlo, para que los PNG queden completos.)
>
> 🟢 This analysis has some limits. The store is fictional, and a correlation shows a relationship, not a cause. As next steps, the team could look at profit by sub-category and region, and check which discounts lead to losses.
>
> (Este análisis tiene algunos límites. La tienda es ficticia, y una correlación muestra una relación, no una causa. Como próximos pasos, el equipo podría mirar la ganancia por subcategoría y región, y revisar qué descuentos llevan a pérdidas.)
>
> 🟢 For the e-commerce manager, the key messages are: Technology leads sales, the business is growing with strong year-end seasons, and discounts should be reviewed because they go with lower profit. Thanks for watching!
>
> (Para el gerente de e-commerce, los mensajes clave son: Technology lidera las ventas, el negocio crece con temporadas fuertes a fin de año, y conviene revisar los descuentos porque van con menos ganancia. ¡Gracias por mirar!)

Si el reloj todavía no pasó los 15:00, no cortes: seguí recorriendo los gráficos y explicándolos con más detalle.

**Resultado esperado:** el notebook recorrido de arriba a abajo y la grabación cerrada después de los 15:00.

---

## Valores de referencia

Los calculé ejecutando este mismo código sobre el CSV. Compará con lo que ves en pantalla antes de decirlos.

| Paso | Resultado esperado |
| ---- | ------------------ |
| Carga sin encoding | `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf6 ...` |
| Inspección | `(9994, 21)`; 0 valores faltantes; 1 duplicado; 449 códigos postales de 4 dígitos |
| Limpieza | `(9993, 22)`; fechas de `2014-01-03` a `2017-12-30` |
| `describe` | Sales: mediana 54,48, promedio 229,85, máximo 22.638,48. Quantity: 1 a 14, mediana 3. Discount: 0 a 0,8. Profit: −6.599,98 a 8.399,98. Unit Price: 0,34 a 3.773,08, mediana 16,27 |
| Barras | Technology 836.154; Furniture 741.718; Office Supplies 719.047 |
| Líneas | Por año: 2014 ≈ 483.966; 2015 ≈ 470.533; 2016 ≈ 609.206; 2017 ≈ 733.215. Máximo: nov. 2017 ≈ 118.448. Mínimo: feb. 2014 ≈ 4.520 |
| Histograma | 5.009 pedidos; mediana 151,96; promedio 458,56; 42% de menos de 100 USD; 27 pedidos de más de 5.000 USD; máximo 23.661,23 |
| Dispersión | Correlación precio–cantidad 0,00; ≈3,8 unidades de promedio en todos los rangos de precio |
| Heatmap | Sales–Unit Price 0,89; Sales–Profit 0,48; Profit–Unit Price 0,47; Sales–Quantity 0,20; Discount–Profit −0,22; los demás ≈ 0 |

---

## 1. Lista de verificación de los cinco gráficos

| # | Gráfico | Título | Eje X | Eje Y | Archivo PNG | ✔ |
| - | ------- | ------ | ----- | ----- | ----------- | - |
| 1 | Barras: ventas por categoría | Total Sales by Category | Category | Total sales (USD) | `01_bar_sales_by_category.png` | ☐ |
| 2 | Línea: ingresos mensuales | Monthly Revenue, 2014 to 2017 | Month | Revenue (USD) | `02_line_monthly_revenue.png` | ☐ |
| 3 | Histograma: valor de los pedidos | Distribution of Order Values | Order value (USD, log scale) | Number of orders | `03_hist_order_values.png` | ☐ |
| 4 | Dispersión: precio contra cantidad | Unit Price vs. Quantity | Unit price (USD, log scale) | Quantity per order line | `04_scatter_price_vs_quantity.png` | ☐ |
| 5 | Heatmap: correlaciones | Correlation Between Numeric Variables | Variables | Variables | `05_heatmap_correlations.png` | ☐ |

Para cada uno, confirmá que:

- está hecho con **seaborn**;
- tiene título y etiquetas legibles;
- se guardó con `plt.savefig` **antes** de `plt.show()`;
- el PNG descargado se abre y no tiene etiquetas cortadas.

---

## 2. Entregables finales (6 archivos)

1. `superstore_eda.ipynb`: el notebook **ejecutado**, descargado con File → Download → Download .ipynb.
2. `01_bar_sales_by_category.png`
3. `02_line_monthly_revenue.png`
4. `03_hist_order_values.png`
5. `04_scatter_price_vs_quantity.png`
6. `05_heatmap_correlations.png`

---

## 3. Estructura recomendada de Deliverables.zip

```
Deliverables.zip
├── superstore_eda.ipynb
├── 01_bar_sales_by_category.png
├── 02_line_monthly_revenue.png
├── 03_hist_order_values.png
├── 04_scatter_price_vs_quantity.png
└── 05_heatmap_correlations.png
```

- Los seis archivos van en la raíz del ZIP, sin subcarpetas. Es una propuesta: revisala contra las reglas de Odin.
- No incluyas el CSV, porque no figura como entregable en el Goal, salvo que las reglas lo pidan.
- Si Firefox renombró algún archivo al descargarlo (por ejemplo, `superstore_eda (1).ipynb`), devolvele el nombre correcto antes de comprimir.
- Armá el ZIP **después** de grabar. No es parte del video.

---

## 4. Duración estimada

| Sección | Tiempo |
| ------- | ------ |
| Apertura: Firefox, Colab y las tres librerías | 0:00–2:00 |
| Notebook nuevo y subir el CSV | 2:00–3:45 |
| Título y carga con pandas | 3:45–6:30 |
| Inspeccionar | 6:30–9:30 |
| Limpiar y resumen numérico | 9:30–12:30 |
| Gráfico 1: barras | 12:30–14:00 |
| Gráfico 2: líneas | 14:00–15:45 |
| Gráfico 3: histograma | 15:45–17:30 |
| Gráfico 4: dispersión | 17:30–19:00 |
| Gráfico 5: heatmap | 19:00–20:30 |
| Observaciones | 20:30–22:00 |
| Descargas | 22:00–23:45 |
| Epílogo | 23:45–26:45 |
| **Total** | **≈ 27 minutos** (sin epílogo, ≈ 24) |

Hay margen de sobra sobre el mínimo de 15:00 y queda lejos del máximo de 50:59.

---

## Después de grabar

1. Ejecutá **Run full AutoQC**, no solo *Rerun failing*.
2. Armá `Deliverables.zip` con los seis archivos.
3. Completá `Metadata.rtf` y Final Notes, con el link de Kaggle del dataset. Esto se hace **fuera** de la grabación.
4. Subí los **cuatro archivos por separado**: el **MP4**, el **ZIP original de TaskRecorder**, **Deliverables.zip** y **Metadata.rtf**.
