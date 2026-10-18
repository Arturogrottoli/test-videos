# Análisis de ventas con pandas — Guion de narración

Un video corto de programación en vivo. Lees un dataset de ventas de una cafetería con **pandas**, calculas totales y haces un gráfico de barras con **matplotlib**.

Cada paso tiene: **ACCIÓN** (lo que haces en pantalla), **DECIR** (lo que lees en voz alta, en inglés), **CÓDIGO** (lo que escribes) y **PRUEBA** (lo que deberías ver).

Los comandos cambian según el sistema. Donde dice **Windows** / **Mac**, usa el que corresponda. En Mac, donde dice `Ctrl` usa `Cmd`.

## Archivos del proyecto

| Archivo | Qué es |
| ------- | ------ |
| `sales.csv` | El dataset: ventas de 6 meses de una cafetería (café, té y jugo). Son datos de ejemplo. |
| `requirements.txt` | Las librerías que hay que instalar: pandas y matplotlib. |
| `analysis.py` | El código del análisis. Se escribe en el video. |
| `chart.png` | El gráfico. Lo crea `analysis.py` al ejecutarse. |

## Antes de grabar (no sale en el video)

1. **Python:** en una terminal, escribe el comando de tu sistema. Tiene que mostrar una versión, por ejemplo `Python 3.14.2`. Si da error, instala Python desde https://www.python.org/downloads/ y reinicia VS Code.
   - **Windows:** `py --version`
   - **Mac:** `python3 --version`
2. **Carpeta del video:** crea una carpeta nueva llamada `pandas` y copia adentro solo `sales.csv` y `requirements.txt`. `analysis.py` se escribe en el video.
3. **Extensión:** si ya tienes instalada la extensión **Python** de Microsoft, desinstálala y reinicia VS Code, así en el video aparece con el botón **Install**.

---

### Paso 1 — Introducción

**ACCIÓN:** VS Code está abierto en la pestaña de bienvenida (Welcome).

**DECIR:**

> Hi everyone! Today we'll analyze a small dataset with pandas, the most popular Python library for working with data. We'll read a CSV file, explore it, calculate some totals, and finish with a bar chart.
>
> Our dataset is the sales of a small coffee shop over six months. Let's get started.

**CÓDIGO:** Ninguno. **PRUEBA:** Ninguna.

---

### Paso 2 — Abrir la carpeta y mirar el dataset

**ACCIÓN:**

1. **File → Open Folder…** → elige la carpeta `pandas` → **Select Folder**. Si VS Code pregunta si confías en los autores, haz clic en **Yes, I trust the authors**.
2. Haz clic en `sales.csv` para abrirlo.

**DECIR:**

> I'll open my project folder, "pandas". It has two files. The first one is sales.csv, our dataset. A CSV file is just a table in plain text: each line is a row, and commas separate the columns.
>
> We have four columns: the month, the product, the number of units sold, and the revenue in dollars. There are three products, coffee, tea, and juice, from January to June. That's eighteen rows.
>
> The second file, requirements.txt, lists the libraries our project needs: pandas, and matplotlib for the chart.

**CÓDIGO:** Ninguno.

**PRUEBA:** El Explorer muestra `sales.csv` y `requirements.txt`. En `sales.csv` se ve la primera línea `month,product,units,revenue` y 18 filas de datos.

---

### Paso 3 — Instalar la extensión de Python

**ACCIÓN:** Abre **Extensions** (`Ctrl + Shift + X`), busca `Python`, elige **Python** de **Microsoft** y haz clic en **Install**.

**DECIR:**

> First, I'll install the Python extension, by Microsoft. It adds colors to our code, suggestions while we type, and helps VS Code work with Python. Install.

**CÓDIGO:** Ninguno.

**PRUEBA:** La extensión muestra un engranaje en vez de **Install**.

---

### Paso 4 — Instalar pandas y matplotlib

**ACCIÓN:**

1. Abre **Terminal → New Terminal** y escribe `pwd`. La ruta tiene que terminar en `pandas`.
2. Crea un entorno virtual:
   - **Windows:** `py -m venv .venv`
   - **Mac:** `python3 -m venv .venv`
3. Instala las librerías en el entorno:
   - **Windows:** `.venv\Scripts\python -m pip install -r requirements.txt`
   - **Mac:** `.venv/bin/python -m pip install -r requirements.txt`

**DECIR:**

> Now let's install pandas. I'll open the terminal and check that I'm in the project folder, with "pwd".
>
> First, I'll create a virtual environment, called ".venv". A virtual environment is a private folder for this project's libraries, so they don't mix with other projects. And we don't need administrator permissions.
>
> Then I'll install the libraries from requirements.txt with pip, Python's package installer. This takes a moment.

**CÓDIGO:** Ninguno.

**PRUEBA:** Aparece la carpeta `.venv` en el Explorer y la terminal termina con una línea que empieza con `Successfully installed`, que incluye `pandas` y `matplotlib`. Si VS Code pregunta si quieres usar el nuevo entorno, haz clic en **Yes**.

---

### Paso 5 — Leer y explorar el dataset

**ACCIÓN:**

1. En el Explorer, crea `analysis.py`.
2. Escribe estas líneas y guarda.
3. Ejecútalo en la terminal:
   - **Windows:** `.venv\Scripts\python analysis.py`
   - **Mac:** `.venv/bin/python analysis.py`

**CÓDIGO — `analysis.py` (parte 1):**

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")
print(df.head())
print(df.describe())
```

**DECIR:**

> Let's write our analysis in a new file, analysis.py. First, we import pandas. Everybody calls it "pd", it's a convention. We also import matplotlib, for the chart later.
>
> "pd.read_csv" reads our CSV file and turns it into a DataFrame. A DataFrame is like a spreadsheet inside Python: a table with rows and columns. We call it "df".
>
> "df.head()" shows the first five rows, so we can check that the data loaded correctly. And "df.describe()" gives us quick statistics for the number columns: how many values, the average, the minimum, the maximum, and more.
>
> Let's run it in the terminal. There's our table, and there are the statistics. For example, the average revenue per row is about 305 dollars, and the best row is 525.

**PRUEBA:** La terminal muestra las primeras 5 filas (de `Jan Coffee 120 360` a `Feb Tea 70 175`) y una tabla de estadísticas con `count 18`, `mean` de `revenue` cerca de `304.78` y `max` de `525`.

---

### Paso 6 — Calcular el total por producto

**ACCIÓN:** Agrega estas líneas al final de `analysis.py`, guarda y vuelve a ejecutarlo con el mismo comando.

**CÓDIGO — `analysis.py` (parte 2):**

```python

by_product = df.groupby("product")["revenue"].sum()
print(by_product)
```

**DECIR:**

> Now a real question: which product makes the most money? For that, we use "groupby". We group the rows by product, take the revenue column, and add it up with "sum".
>
> Let's run it again. Coffee is the winner with 2640 dollars, then juice with 1720, and tea with 1126.

**PRUEBA:** Al final de la salida aparece:

```
product
Coffee    2640
Juice     1720
Tea       1126
Name: revenue, dtype: int64
```

---

### Paso 7 — Hacer el gráfico

**ACCIÓN:** Agrega estas líneas al final de `analysis.py`, guarda y vuelve a ejecutarlo. Se abre una ventana con el gráfico. Ciérrala para que la terminal termine.

**CÓDIGO — `analysis.py` (parte 3):**

```python

by_product.plot(kind="bar", title="Revenue by product", rot=0)
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig("chart.png")
plt.show()
```

**DECIR:**

> Numbers are great, but a chart is easier to understand. pandas can draw charts directly. We call "plot" on our totals, with "kind" equal to "bar" for a bar chart, and a title. "rot=0" keeps the product names horizontal.
>
> Then we label the vertical axis, and "tight_layout" makes sure nothing gets cut off. "savefig" saves the chart as an image, chart.png, and "show" opens it in a window.
>
> Let's run it. And here's our chart! We can see right away that coffee sells the most, and tea the least. And in the Explorer, we also have chart.png, ready to use in a report or a presentation.

**PRUEBA:** Se abre una ventana con un gráfico de barras azules titulado **Revenue by product**: Coffee (cerca de 2600), Juice (cerca de 1700) y Tea (cerca de 1100), con los nombres horizontales. Al cerrar la ventana, aparece `chart.png` en el Explorer.

---

### Paso 8 — Cierre

**DECIR:**

> And that's it! In just a few lines, we read a CSV file with pandas, explored it with "head" and "describe", answered a question with "groupby", and created a chart with matplotlib.
>
> Try it with your own data: change the CSV, group by month instead of product, or try a line chart with "kind" equal to "line".
>
> Thanks for watching!

**ACCIÓN:** Detén la grabación.
