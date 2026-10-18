# Análisis de ventas con pandas en Google Colab — Guion de narración

Un video corto de programación en vivo en **Google Colab**. Subes un dataset de ventas de una cafetería, lo exploras con **pandas** y haces un gráfico de barras con **matplotlib**. No hay que instalar nada: Colab ya trae pandas y matplotlib.

Cada paso tiene: **ACCIÓN** (lo que haces en pantalla), **DECIR** (lo que lees en voz alta, en inglés), **CÓDIGO** (lo que escribes) y **PRUEBA** (lo que deberías ver).

Los nombres de menús y botones están en inglés, tal como aparecen en Colab en inglés. En Mac, donde dice `Ctrl` usa `Cmd`.

## Archivos del proyecto

| Archivo | Qué es |
| ------- | ------ |
| `sales.csv` | El dataset: ventas de 6 meses de una cafetería (café, té y jugo). Son datos de ejemplo. |
| `analysis.ipynb` | El notebook terminado, como referencia. Para verlo en Colab: **File → Upload notebook** y elige este archivo. |

## Antes de grabar (no sale en el video)

1. Inicia sesión en tu cuenta de Google en el navegador.
2. Ten `sales.csv` en una carpeta fácil de encontrar, por ejemplo el Escritorio.
3. Abre https://colab.research.google.com una vez para confirmar que carga.

---

### Paso 1 — Introducción

**ACCIÓN:** El navegador está abierto en https://colab.research.google.com.

**DECIR:**

> Hi everyone! Today we'll analyze a small dataset with pandas, the most popular Python library for working with data. We'll read a CSV file, explore it, calculate some totals, and finish with a bar chart.
>
> We'll use Google Colab. Colab runs Python in the browser, for free, and pandas is already installed. So there's nothing to set up. Let's get started.

**CÓDIGO:** Ninguno. **PRUEBA:** Ninguna.

---

### Paso 2 — Crear el notebook

**ACCIÓN:**

1. Haz clic en **New notebook**, o ve a **File → New notebook in Drive**.
2. Haz clic en el nombre de arriba a la izquierda (`Untitled0.ipynb`) y cámbialo a `sales_analysis.ipynb`.

**DECIR:**

> I'll create a new notebook and call it "sales_analysis". A notebook is made of cells. We write code in a cell, run it, and the result appears right below. That makes it perfect for exploring data step by step.

**CÓDIGO:** Ninguno.

**PRUEBA:** Se abre un notebook vacío con una celda de código, y el nombre de arriba dice `sales_analysis.ipynb`.

---

### Paso 3 — Subir el dataset

**ACCIÓN:**

1. En la barra de la izquierda, haz clic en el ícono de carpeta (**Files**).
2. Haz clic en el ícono **Upload to session storage** (una hoja con una flecha hacia arriba) y elige `sales.csv`.
3. Si aparece un aviso de que los archivos se borran al terminar la sesión, haz clic en **OK**.

**DECIR:**

> Now we need our data. I'll open the Files panel on the left and upload sales.csv.
>
> Colab warns us that uploaded files are deleted when the session ends. That's fine for today. We just need to upload the file again next time.
>
> Our dataset is the sales of a small coffee shop. It has four columns: the month, the product, the number of units sold, and the revenue in dollars. There are three products, coffee, tea, and juice, from January to June.

**CÓDIGO:** Ninguno.

**PRUEBA:** `sales.csv` aparece en el panel **Files**, junto a la carpeta `sample_data`.

---

### Paso 4 — Leer el dataset

**ACCIÓN:** En la primera celda, escribe el código de abajo y pulsa `Shift + Enter` para ejecutarla. La primera vez tarda unos segundos, mientras Colab se conecta.

**CÓDIGO — celda 1:**

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")
df.head()
```

**DECIR:**

> Let's write our first cell. First, we import pandas. Everybody calls it "pd", it's a convention. We also import matplotlib, for the chart later.
>
> "pd.read_csv" reads our CSV file and turns it into a DataFrame. A DataFrame is like a spreadsheet inside Python: a table with rows and columns. We call it "df".
>
> "df.head()" shows the first five rows. I'll press Shift and Enter to run the cell. There's our data, in a clean table.

**PRUEBA:** Debajo de la celda aparece una tabla con las columnas `month`, `product`, `units` y `revenue`, y 5 filas, de `Jan Coffee 120 360` a `Feb Tea 70 175`. Colab crea una celda nueva abajo.

Si aparece `FileNotFoundError`, el archivo no se subió: vuelve al paso 3.

---

### Paso 5 — Explorar los números

**ACCIÓN:** En la celda nueva, escribe el código y pulsa `Shift + Enter`.

**CÓDIGO — celda 2:**

```python
df.describe()
```

**DECIR:**

> Next, "describe" gives us quick statistics for the number columns: how many values, the average, the minimum, the maximum, and more. For example, the average revenue per row is about 305 dollars, and the best row is 525.

**PRUEBA:** Aparece una tabla de estadísticas con `count 18`, `mean` de `revenue` cerca de `304.78` y `max` de `525`.

---

### Paso 6 — Calcular el total por producto

**ACCIÓN:** En la celda nueva, escribe el código y pulsa `Shift + Enter`.

**CÓDIGO — celda 3:**

```python
by_product = df.groupby("product")["revenue"].sum()
by_product
```

**DECIR:**

> Now a real question: which product makes the most money? For that, we use "groupby". We group the rows by product, take the revenue column, and add it up with "sum".
>
> Coffee is the winner with 2640 dollars, then juice with 1720, and tea with 1126.

**PRUEBA:** Aparece:

```
product
Coffee    2640
Juice     1720
Tea       1126
Name: revenue, dtype: int64
```

---

### Paso 7 — Hacer el gráfico

**ACCIÓN:** En la celda nueva, escribe el código y pulsa `Shift + Enter`.

**CÓDIGO — celda 4:**

```python
by_product.plot(kind="bar", title="Revenue by product", rot=0)
plt.ylabel("Revenue ($)")
plt.show()
```

**DECIR:**

> Numbers are great, but a chart is easier to understand. pandas can draw charts directly. We call "plot" on our totals, with "kind" equal to "bar" for a bar chart, and a title. "rot=0" keeps the product names horizontal. Then we label the vertical axis, and "show" displays the chart.
>
> And here's our chart, right inside the notebook! We can see right away that coffee sells the most, and tea the least.

**PRUEBA:** Debajo de la celda aparece un gráfico de barras azules titulado **Revenue by product**: Coffee (cerca de 2600), Juice (cerca de 1700) y Tea (cerca de 1100), con los nombres horizontales.

---

### Paso 8 — Cierre

**DECIR:**

> And that's it! In just four cells, we read a CSV file with pandas, explored it with "head" and "describe", answered a question with "groupby", and created a chart with matplotlib. All in the browser, without installing anything.
>
> Try it with your own data: change the CSV, group by month instead of product, or try a line chart with "kind" equal to "line".
>
> Thanks for watching!

**ACCIÓN:** Detén la grabación.
