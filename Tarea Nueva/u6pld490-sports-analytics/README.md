# u6pld490 — Sports Analytics

Guion paso a paso para grabar la tarea **u6pld490**: analizar en **Google Colab**, con **pandas** y **NumPy**, los datos ficticios de rendimiento de un deportista. El trabajo incluye limpiar los datos, calcular estadísticas descriptivas, detectar valores atípicos con el **IQR** y crear un **histograma** y un **gráfico de dispersión**. La grabación tiene que durar **entre 15:00 y 50:59**. Este guion apunta a unos **25 minutos**, epílogo incluido.

**Cómo leer este guion:**

- Las frases que empiezan con 🖱️ las decís **en el momento de hacer clic, desplazarte o escribir**. Siempre dicen **qué** elemento usás, **dónde** está en la pantalla y **por qué** lo usás. Son las que revisa AutoQC.
- Las frases que empiezan con 🟢 son la explicación que **decís en inglés** entre una acción y otra.
- Debajo de cada bloque de código, la lista **What each line does** explica cada línea en inglés. La leés en voz alta mientras escribís esa línea.
- El resto, en castellano, es lo que hacés en pantalla. Las traducciones aparecen entre paréntesis después de cada frase.

> **Importante:** el Goal de Studio tiene prioridad sobre este guion. Antes de grabar, comparalo con el campo **Describe your idea** de la tarea. El dataset lo armé yo: es ficticio y tiene errores puestos a propósito para limpiarlos.

---

## Archivos de la carpeta

```
u6pld490-sports-analytics/
├── README.md                  ← este guion
├── athlete_games.csv          ← dataset de partida: 59 filas, con errores para limpiar
└── athlete_performance.ipynb  ← notebook de referencia, completo y en orden
```

Para probar el notebook de referencia: en https://colab.research.google.com elegís **File → Upload notebook** y seleccionás `athlete_performance.ipynb`. Después subís `athlete_games.csv` desde el panel **Files** y ejecutás **Runtime → Run all**.

---

## El dataset

`athlete_games.csv` tiene los partidos de una temporada de un jugador de básquet **ficticio**, contra equipos también ficticios. Tiene 59 filas y 7 columnas:

| Columna | Qué contiene |
| ------- | ------------ |
| `game` | Número de partido (1 a 58) |
| `date` | Fecha del partido |
| `opponent` | Equipo rival |
| `minutes` | Minutos jugados |
| `points` | Puntos anotados |
| `rebounds` | Rebotes |
| `assists` | Asistencias |

**Errores puestos a propósito** (los encontrás y los limpiás durante la grabación):

| Problema | Dónde | Cómo se limpia |
| -------- | ----- | -------------- |
| Fila duplicada | El partido 12 aparece dos veces | `drop_duplicates()` |
| Valores faltantes | Sin puntos en los partidos 7 y 33, sin minutos en el 41 | `dropna()` |
| Valor imposible | 340 minutos en el partido 22 (un partido dura 48) | Filtrar `minutes <= 48` |
| Nombres inconsistentes | 15 formas de escribir 8 equipos (`tigers`, `WOLVES`, `Sharks ` con espacio) | `str.strip().str.title()` |

---

## Antes de grabar

1. Leé el Goal y compará este guion con el campo **Describe your idea** de Studio.
2. Practicá una vez entera en un notebook nuevo, leyendo en voz alta todas las frases 🖱️ y 🟢, y cronometrá.
3. Dejá tres pestañas abiertas en Firefox, en este orden: Colab (https://colab.research.google.com), el sitio de pandas (https://pandas.pydata.org) y el sitio de NumPy (https://numpy.org). En Colab dejá a la vista el cuadro **Open notebook**, sin crear todavía el notebook. Tené `athlete_games.csv` en una carpeta fácil de encontrar, como el Escritorio. Agrandá el zoom del navegador (`Ctrl + +`).
4. Maximizá el navegador y cerrá o minimizá las demás ventanas, para que ninguna tape a otra.
5. Pausa de ~1 segundo después de cada clic y nunca más de 45 segundos en silencio.
6. No muestres Studio, Mercor, información privada ni herramientas de IA. Cerrá este guion si está en la misma pantalla.

---

## 0:00–1:15 — Colab, pandas y NumPy

Empezás en la primera pestaña, la de **Colab**, con el cuadro **Open notebook** a la vista. La introducción dura menos de 20 segundos: decís el objetivo y enseguida pasás a la primera acción.

> 🖱️ I'm on Google Colab, in the first browser tab, where I'll do this whole analysis.
>
> (Estoy en Google Colab, en la primera pestaña del navegador, donde voy a hacer todo el análisis.)
>
> 🟢 As a data analyst for a sports performance team, I'll analyze a fictional athlete's game data in Google Colab. I'll clean it, calculate descriptive statistics, find outliers with the IQR method, and create a histogram and a scatter plot.
>
> (Como analista de datos de un equipo de rendimiento deportivo, voy a analizar en Google Colab los datos de partidos de un deportista ficticio. Los voy a limpiar, calcular estadísticas descriptivas, encontrar valores atípicos con el método IQR y crear un histograma y un gráfico de dispersión.)
>
> 🟢 Google Colab is a free tool from Google that runs Python notebooks in the browser. The code runs in Google's cloud, so there's nothing to install.
>
> (Google Colab es una herramienta gratuita de Google que ejecuta notebooks de Python en el navegador. El código se ejecuta en la nube de Google, así que no hay que instalar nada.)
>
> 🖱️ I'm clicking the second browser tab, at the top of the window, to show the official pandas website.
>
> (Hago clic en la segunda pestaña del navegador, arriba de la ventana, para mostrar el sitio oficial de pandas.)
>
> 🟢 This is pandas, a free Python library for tables of data. I'll use it to load the games, clean them, and calculate the statistics.
>
> (Esto es pandas, una librería gratuita de Python para trabajar con tablas de datos. La voy a usar para cargar los partidos, limpiarlos y calcular las estadísticas.)
>
> 🖱️ I'm clicking the third browser tab, at the top of the window, to show the official NumPy website.
>
> (Hago clic en la tercera pestaña del navegador, arriba de la ventana, para mostrar el sitio oficial de NumPy.)
>
> 🟢 This is NumPy, a free Python library for fast math with numbers and arrays. pandas is built on top of NumPy, and I'll use NumPy for percentiles and for the IQR method. Both libraries come already installed in Colab.
>
> (Esto es NumPy, una librería gratuita de Python para hacer cálculos rápidos con números y arreglos. pandas está construida sobre NumPy, y voy a usar NumPy para los percentiles y para el método IQR. Las dos librerías vienen instaladas en Colab.)
>
> 🖱️ I'm clicking the first browser tab, at the top left of the window, to go back to Google Colab.
>
> (Hago clic en la primera pestaña del navegador, arriba a la izquierda de la ventana, para volver a Google Colab.)

---

## 1:15–5:30 — Notebook nuevo y cargar los datos

> 🖱️ I'm clicking the New notebook button at the bottom of the Open notebook dialog, to create a fresh notebook.
>
> (Hago clic en el botón New notebook, abajo del cuadro Open notebook, para crear un notebook nuevo.)
>
> 🖱️ I'm clicking the notebook title field at the top left, and typing athlete_performance.ipynb, to identify this analysis.
>
> (Hago clic en el campo del título del notebook, arriba a la izquierda, y escribo athlete_performance.ipynb, para identificar este análisis.)

Subís el CSV:

> 🖱️ I'm clicking the Files icon, the folder in the left sidebar, to upload the dataset.
>
> (Hago clic en el ícono Files, la carpeta de la barra lateral izquierda, para subir el dataset.)
>
> 🖱️ I'm clicking the Upload to session storage icon, at the top of the Files pane, and choosing athlete_games.csv from my computer, so the notebook can read it.
>
> (Hago clic en el ícono Upload to session storage, arriba del panel Files, y elijo athlete_games.csv de mi computadora, para que el notebook pueda leerlo.)

Si aparece un aviso de que los archivos se borran al reiniciar el entorno: *"I'm clicking OK on this warning, in the center of the screen, to continue the upload."*

> 🖱️ I'm clicking the plus Text button in the toolbar at the top left, to add a title and the goal.
>
> (Hago clic en el botón + Text de la barra de herramientas, arriba a la izquierda, para agregar un título y el objetivo.)

```markdown
# Athlete Performance Analysis
Dataset: fictional game log of one basketball player. Goal: clean the data, describe scoring with statistics, find outliers with the IQR method, and explore patterns with charts.
```

**What each line does:**

- 🟢 `# Athlete Performance Analysis`: the hash sign makes this the main title of the notebook.
- 🟢 `Dataset: ... Goal: ...`: this line says what the data is and what I want to find out.

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add a code cell that loads the libraries and the data.
>
> (Hago clic en el botón + Code de la barra de herramientas, arriba a la izquierda, para agregar una celda de código que carga las librerías y los datos.)

Escribís la **celda 1**:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("athlete_games.csv")
df
```

**What each line does:**

- 🟢 `import pandas as pd`: this loads pandas, the library for tables of data, with its usual short name, pd.
- 🟢 `import numpy as np`: this loads NumPy with its usual short name, np. I'll use it for percentiles.
- 🟢 `import matplotlib.pyplot as plt`: this loads pyplot, the part of Matplotlib that draws charts, as plt.
- 🟢 `df = pd.read_csv("athlete_games.csv")`: read_csv reads the file I uploaded and stores it in a DataFrame called df. A DataFrame is a table with rows and columns, like a spreadsheet.
- 🟢 `df`: writing df alone, as the last line of the cell, shows the table. This file is small, so pandas shows every row, and I can check the whole dataset right here in the notebook.

> 🖱️ I'm clicking the Run cell button, the play icon to the left of this cell, to load and show the data.
>
> (Hago clic en el botón Run cell, el ícono de play a la izquierda de esta celda, para cargar y mostrar los datos.)
>
> 🟢 This is a fictional dataset I prepared for this analysis: one season of games for one basketball player. Like most real data, it isn't perfectly clean, so after loading it, the first step will be to inspect it and fix any problems.
>
> (Este es un dataset ficticio que preparé para este análisis: una temporada de partidos de un jugador de básquet. Como pasa con casi todos los datos reales, no está perfectamente limpio, así que después de cargarlo, el primer paso va a ser inspeccionarlo y corregir los problemas.)

Señalás cada columna con el mouse, de izquierda a derecha, mientras la nombrás:

> 🟢 Each row is one game, and there are seven columns. game is the game number, in order. date is the day of the game. opponent is the rival team. minutes is how long the player was on the court. A basketball game lasts 48 minutes, so no value should be higher than that.
>
> (Cada fila es un partido, y hay siete columnas. game es el número de partido, en orden. date es el día del partido. opponent es el equipo rival. minutes es cuánto tiempo estuvo el jugador en la cancha. Un partido de básquet dura 48 minutos, así que ningún valor debería ser mayor.)
>
> 🟢 points is how many points he scored. This is the main column of the analysis: I'll use it for the statistics, the outliers, and the histogram. rebounds counts the balls he caught after a missed shot, and assists counts the passes that led directly to a teammate's basket.
>
> (points es cuántos puntos anotó. Es la columna principal del análisis: la uso para las estadísticas, los valores atípicos y el histograma. rebounds cuenta las pelotas que agarró después de un tiro fallado, y assists cuenta los pases que terminaron directamente en un punto de un compañero.)

🖱️ Bajás despacio por la tabla con la rueda del mouse hasta la última fila:

> 🖱️ I'm scrolling down through the table, in the output under the cell, to show every game.
>
> (Bajo por la tabla, en la salida debajo de la celda, para mostrar todos los partidos.)
>
> 🟢 At the bottom, pandas shows the size: 59 rows and 7 columns. And here in row 4, notice tigers is written in lowercase. I'll come back to that when I inspect the data.
>
> (Abajo, pandas muestra el tamaño: 59 filas y 7 columnas. Y acá, en la fila 4, fíjense que tigers está escrito en minúscula. Vuelvo a eso cuando inspeccione los datos.)

Si Colab corta la tabla con `...` en el medio, agregás `pd.set_option("display.max_rows", 100)` antes de `df` y decís: *"This line tells pandas to show up to 100 rows, so we see the whole table."* Probalo antes de grabar.

---

## 5:30–10:00 — Inspeccionar y limpiar los datos

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
print(df["opponent"].unique())
df.describe()
```

**What each line does:**

- 🟢 `df.info()`: info lists every column with how many values it has and its data type. If a column has fewer values than the number of rows, it has missing values.
- 🟢 `print("Duplicate rows:", df.duplicated().sum())`: duplicated marks each row that is an exact copy of an earlier row, and sum counts them.
- 🟢 `print(df["opponent"].unique())`: unique lists every different value in the opponent column, so I can see if the team names are written consistently.
- 🟢 `df.describe()`: describe gives a summary of each number column: count, mean, minimum, maximum, and percentiles. It helps me spot impossible values. I don't need print for info, because it prints by itself, or for describe, because Colab always shows the result of the last line of a cell.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to inspect the data.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para inspeccionar los datos.)

Señalás cada problema con el mouse mientras lo nombrás:

> 🟢 I can see four problems. First, info shows 59 rows, but minutes has only 58 values and points has only 57, so there are missing values.
>
> (Veo cuatro problemas. Primero, info muestra 59 filas, pero minutes tiene solo 58 valores y points solo 57, así que hay valores faltantes.)
>
> 🟢 Second, there is one duplicate row. Third, the opponent names are inconsistent: for example, Tigers appears with a capital letter and in lowercase, and some names have extra spaces. There are 15 spellings for only 8 teams.
>
> (Segundo, hay una fila duplicada. Tercero, los nombres de los rivales son inconsistentes: por ejemplo, Tigers aparece con mayúscula y en minúscula, y algunos nombres tienen espacios de más. Hay 15 formas de escribir solo 8 equipos.)
>
> 🟢 And fourth, describe shows a maximum of 340 minutes. A basketball game lasts 48 minutes, so that value is impossible. It's probably a typing error.
>
> (Y cuarto, describe muestra un máximo de 340 minutos. Un partido de básquet dura 48 minutos, así que ese valor es imposible. Probablemente es un error de tipeo.)

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for cleaning.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para la limpieza.)

Escribís `## 2. Clean and prepare the data`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that fixes these four problems.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que arregla estos cuatro problemas.)

Escribís la **celda 3**:

```python
df = df.drop_duplicates()
df = df.dropna(subset=["minutes", "points"])
df = df[df["minutes"] <= 48].copy()
df["opponent"] = df["opponent"].str.strip().str.title()
print(df.shape)
print(df["opponent"].unique())
```

**What each line does:**

- 🟢 `df = df.drop_duplicates()`: this removes the duplicate row, so the same game isn't counted twice.
- 🟢 `df = df.dropna(subset=["minutes", "points"])`: dropna removes the rows with missing minutes or points. I remove them instead of filling them, because guessing a score would change the statistics.
- 🟢 `df = df[df["minutes"] <= 48].copy()`: this keeps only the games with 48 minutes or less, which removes the impossible 340. copy makes a clean new table, so pandas doesn't show a warning when I change it in the next line.
- 🟢 `df["opponent"] = df["opponent"].str.strip().str.title()`: strip removes the extra spaces, and title writes each name with a capital first letter, so every team has one spelling.
- 🟢 `print(df.shape)`: this shows how many rows and columns are left.
- 🟢 `print(df["opponent"].unique())`: this checks that the team names are consistent now.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to clean the data.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para limpiar los datos.)
>
> 🟢 Now we have 54 games and 7 columns, and only 8 team names. We removed one duplicate, three rows with missing values, and one impossible value.
>
> (Ahora tenemos 54 partidos y 7 columnas, y solo 8 nombres de equipos. Quitamos un duplicado, tres filas con valores faltantes y un valor imposible.)

---

## 10:00–14:00 — Estadísticas descriptivas y valores atípicos

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for the statistics.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para las estadísticas.)

Escribís `## 3. Descriptive statistics`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that describes the points per game.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que describe los puntos por partido.)

Escribís la **celda 4**:

```python
points = df["points"]
print(points.agg(["mean", "median", "std"]).round(2))
print("Percentiles 25, 50, 75, 90:", np.percentile(points, [25, 50, 75, 90]))
```

**What each line does:**

- 🟢 `points = df["points"]`: this saves the points column in a short variable, so the next lines are easier to read.
- 🟢 `print(points.agg(["mean", "median", "std"]).round(2))`: agg calculates several statistics at once with pandas. The mean is the average. The median is the middle value when the games are sorted. The standard deviation, std, measures how far the games usually are from the average. round(2) keeps two decimals.
- 🟢 `print("Percentiles 25, 50, 75, 90:", np.percentile(points, [25, 50, 75, 90]))`: NumPy's percentile function finds the value below which a percentage of the games fall. For example, the 90th percentile means 90 percent of the games are at or below that number.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to calculate the statistics.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para calcular las estadísticas.)
>
> 🟢 The player averages about 20.9 points per game, and the median is 20.5. They're very close, so a typical game is around 20 points. The standard deviation is about 6.4 points.
>
> (El jugador promedia unos 20,9 puntos por partido, y la mediana es 20,5. Están muy cerca, así que un partido típico ronda los 20 puntos. La desviación estándar es de unos 6,4 puntos.)
>
> 🟢 The 25th percentile is 17.25 and the 75th is 23, so half of the games are between those two values. And 90 percent of the games are at or below 26.7 points.
>
> (El percentil 25 es 17,25 y el 75 es 23, así que la mitad de los partidos están entre esos dos valores. Y el 90 por ciento de los partidos están en 26,7 puntos o menos.)

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for the outliers.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para los valores atípicos.)

Escribís `## 4. Outliers with the IQR method`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that finds the unusual games.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que encuentra los partidos inusuales.)

Escribís la **celda 5**:

```python
q1, q3 = np.percentile(points, [25, 75])
iqr = q3 - q1
lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
print("IQR:", iqr, "| Lower bound:", lower, "| Upper bound:", upper)
df[(points < lower) | (points > upper)]
```

**What each line does:**

- 🟢 `q1, q3 = np.percentile(points, [25, 75])`: this calculates the first quartile, Q1, the 25th percentile, and the third quartile, Q3, the 75th percentile.
- 🟢 `iqr = q3 - q1`: the interquartile range, or IQR, is the distance between Q3 and Q1. It's the range of the middle half of the games.
- 🟢 `lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr`: this is the standard IQR rule. Any value more than one and a half IQRs below Q1 or above Q3 is an outlier.
- 🟢 `print("IQR:", ...)`: this shows the IQR and the two limits.
- 🟢 `df[(points < lower) | (points > upper)]`: this keeps only the games below the lower limit or above the upper limit. The vertical bar means "or".

> 🖱️ I'm clicking the Run cell button to the left of this cell, to find the outliers.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para encontrar los valores atípicos.)
>
> 🟢 The IQR is 5.75 points, so any game under about 8.6 or over about 31.6 points is an outlier. There are three: 46 points in game 15 and 41 points in game 38, both with around 40 minutes, and only 3 points in game 49, where the player played just 11 minutes.
>
> (El IQR es de 5,75 puntos, así que cualquier partido por debajo de unos 8,6 o por encima de unos 31,6 puntos es atípico. Hay tres: 46 puntos en el partido 15 y 41 en el 38, los dos con unos 40 minutos, y solo 3 puntos en el partido 49, donde el jugador jugó apenas 11 minutos.)
>
> 🟢 I don't remove these outliers, because they are real games, not errors. They are exactly the games the team should look at.
>
> (No quito estos valores atípicos, porque son partidos reales, no errores. Son justamente los partidos que el equipo tendría que mirar.)

---

## 14:00–17:30 — Histograma y gráfico de dispersión

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for the charts.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para los gráficos.)

Escribís `## 5. Charts`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell for the histogram.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código para el histograma.)

Escribís la **celda 6**:

```python
points.plot(kind="hist", bins=15, title="Points per Game")
plt.xlabel("Points")
plt.show()
```

**What each line does:**

- 🟢 `points.plot(kind="hist", bins=15, title="Points per Game")`: this draws a histogram. It splits the points into 15 ranges, called bins, and each bar shows how many games fall in that range. The vertical axis, Frequency, is a number of games.
- 🟢 `plt.xlabel("Points")`: this names the horizontal axis.
- 🟢 `plt.show()`: this displays the chart.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to draw the histogram.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para dibujar el histograma.)
>
> 🟢 Most games are grouped between 15 and 25 points: that's 40 of the 54 games. The bars far to the right are the two big games, and the bar far to the left is the 3-point game.
>
> (La mayoría de los partidos se agrupan entre 15 y 25 puntos: son 40 de los 54. Las barras bien a la derecha son los dos partidos grandes, y la barra bien a la izquierda es el partido de 3 puntos.)

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell for the scatter plot.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código para el gráfico de dispersión.)

Escribís la **celda 7**:

```python
df.plot(kind="scatter", x="minutes", y="points", title="Minutes vs Points")
plt.show()
print("Correlation:", round(df["minutes"].corr(df["points"]), 2))
```

**What each line does:**

- 🟢 `df.plot(kind="scatter", x="minutes", y="points", ...)`: a scatter plot draws one dot per game, with the minutes on the horizontal axis and the points on the vertical axis. It shows if two variables move together. pandas uses the column names as the axis labels.
- 🟢 `plt.show()`: this displays the chart.
- 🟢 `print("Correlation:", round(df["minutes"].corr(df["points"]), 2))`: corr calculates the correlation, a number between minus one and one. Close to one means that when one variable goes up, the other one goes up too.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to draw the scatter plot.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para dibujar el gráfico de dispersión.)
>
> 🟢 The dots go up from left to right: more minutes usually means more points. The correlation is about 0.63, a moderate positive relationship. The two big games are at the top right, and the 3-point game is alone at the bottom left, with very few minutes.
>
> (Los puntos suben de izquierda a derecha: más minutos suele significar más puntos. La correlación es de unos 0,63, una relación positiva moderada. Los dos partidos grandes están arriba a la derecha, y el partido de 3 puntos está solo abajo a la izquierda, con muy pocos minutos.)

---

## 17:30–19:30 — Observaciones y conclusión

**Valores de referencia** (los calculé directamente del CSV). Compará con tu resultado antes de decirlos:

| Paso | Resultado esperado |
| ---- | ------------------ |
| Inspección | 59 filas; `minutes` 58 valores, `points` 57; 1 duplicado; 15 nombres de rival; máximo de minutos 340 |
| Limpieza | `(54, 7)` y 8 equipos: Falcons, Tigers, Wolves, Eagles, Bears, Hawks, Lions, Sharks |
| Estadísticas | Promedio 20,89; mediana 20,5; desviación estándar 6,44; percentiles 17,25 / 20,5 / 23 / 26,7 |
| IQR | IQR 5,75; límites 8,625 y 31,625; atípicos: partidos 15 (46 pts), 38 (41 pts) y 49 (3 pts) |
| Gráficos | 40 de 54 partidos entre 15 y 25 puntos; correlación 0,63 |

> 🖱️ I'm clicking the plus Text button in the toolbar, to add my observations below the charts.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar mis observaciones debajo de los gráficos.)

Mientras escribís, decí en voz alta lo que vas escribiendo:

```markdown
## 6. Observations
- **Cleaning:** 59 rows became 54 games. We removed 1 duplicate row, 3 rows with missing minutes or points, and 1 impossible value (340 minutes in a 48-minute game). Opponent names had 15 different spellings for 8 teams, and now they are consistent.
- **Statistics:** the player averages about 20.9 points per game, with a median of 20.5 and a standard deviation of about 6.4. Half of the games are between 17.25 and 23 points, and 90% are at or below 26.7.
- **Outliers:** the IQR is 5.75, so games below 8.6 or above 31.6 points are outliers. There are three: 46 points (game 15) and 41 points (game 38), both with about 40 minutes, and 3 points in only 11 minutes (game 49).
- **Histogram:** most games (40 of 54) are between 15 and 25 points, with a few extreme games on both sides.
- **Scatter plot:** more minutes usually means more points (correlation about 0.63). The 3-point game is low because the player only played 11 minutes.
```

> 🖱️ I'm clicking the plus Text button in the toolbar, to add the conclusion at the end of the notebook.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar la conclusión al final del notebook.)

```markdown
## 7. Conclusion
The player is a consistent scorer of about 20 points per game. The two 40+ point games are exceptional performances, and the 3-point game is explained by very few minutes on the court, so playing time is a key factor in scoring.
```

> 🟢 To sum up: the player scores about 20 points in a typical game, the IQR method found two exceptional games and one very low game, and the scatter plot shows that playing time is a key factor in scoring.
>
> (Para resumir: el jugador anota unos 20 puntos en un partido típico, el método IQR encontró dos partidos excepcionales y uno muy bajo, y el gráfico de dispersión muestra que el tiempo de juego es un factor clave para anotar.)

---

## 19:30–25:00 — Epílogo (5–6 minutos)

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
> 🟢 Let me summarize the whole analysis. We started with the title and the goal: clean the data, describe the scoring, find outliers, and explore patterns with charts.
>
> (Les resumo todo el análisis. Empezamos con el título y el objetivo: limpiar los datos, describir los puntos, encontrar valores atípicos y explorar patrones con gráficos.)
>
> 🟢 In the first cell, we imported three libraries: pandas for the table, NumPy for the percentiles, and Matplotlib for the charts. Then we loaded the CSV and looked at the whole table: 59 rows, one per game, and 7 columns.
>
> (En la primera celda importamos tres librerías: pandas para la tabla, NumPy para los percentiles y Matplotlib para los gráficos. Después cargamos el CSV y miramos la tabla completa: 59 filas, una por partido, y 7 columnas.)
>
> 🖱️ I'm scrolling down to section 1, Inspect the data, to show what we found.
>
> (Bajo hasta la sección 1, Inspect the data, para mostrar lo que encontramos.)
>
> 🟢 In section 1, we inspected the data before calculating anything, and we found four problems: missing minutes and points, one duplicate game, 15 spellings for only 8 teams, and an impossible value of 340 minutes.
>
> (En la sección 1 inspeccionamos los datos antes de calcular nada, y encontramos cuatro problemas: minutos y puntos faltantes, un partido duplicado, 15 formas de escribir solo 8 equipos y un valor imposible de 340 minutos.)
>
> 🖱️ I'm scrolling down to section 2, Clean and prepare the data.
>
> (Bajo hasta la sección 2, Clean and prepare the data.)
>
> 🟢 In section 2, we fixed those four problems, one line each. We removed the duplicate, the three rows with missing values, and the impossible game, and we fixed the team names. We went from 59 rows to 54 clean games.
>
> (En la sección 2 arreglamos esos cuatro problemas, con una línea para cada uno. Quitamos el duplicado, las tres filas con valores faltantes y el partido imposible, y corregimos los nombres de los equipos. Pasamos de 59 filas a 54 partidos limpios.)
>
> 🖱️ I'm scrolling down to section 3, Descriptive statistics.
>
> (Bajo hasta la sección 3, Descriptive statistics.)
>
> 🟢 In section 3, we described the points. The mean is about 20.9 and the median is 20.5. They are very close, so the scoring is balanced. The standard deviation, about 6.4, tells us how much the points usually move away from the average. And the percentiles showed that half of the games are between 17 and 23 points.
>
> (En la sección 3 describimos los puntos. El promedio es unos 20,9 y la mediana 20,5. Están muy cerca, así que los puntos están equilibrados. La desviación estándar, unos 6,4, nos dice cuánto se alejan normalmente los puntos del promedio. Y los percentiles mostraron que la mitad de los partidos está entre 17 y 23 puntos.)
>
> 🖱️ I'm scrolling down to section 4, Outliers with the IQR method.
>
> (Bajo hasta la sección 4, Outliers with the IQR method.)
>
> 🟢 In section 4, we used the IQR method. The IQR is the distance between the first and third quartiles, 5.75 points. Any game below 8.6 or above 31.6 points is an outlier. We found three: 46 and 41 points, two great games, and 3 points, in a game where the player only played 11 minutes.
>
> (En la sección 4 usamos el método IQR. El IQR es la distancia entre el primer y el tercer cuartil, 5,75 puntos. Cualquier partido por debajo de 8,6 o por encima de 31,6 puntos es atípico. Encontramos tres: 46 y 41 puntos, dos partidos excelentes, y 3 puntos, en un partido donde el jugador solo jugó 11 minutos.)
>
> 🖱️ I'm scrolling down to section 5, Charts, to show the two charts again.
>
> (Bajo hasta la sección 5, Charts, para mostrar otra vez los dos gráficos.)
>
> 🟢 In section 5, we drew two charts. The histogram shows that most games, 40 of 54, are between 15 and 25 points. The scatter plot shows that more minutes usually means more points, with a correlation of 0.63, which is a moderate to strong positive relationship.
>
> (En la sección 5 hicimos dos gráficos. El histograma muestra que la mayoría de los partidos, 40 de 54, está entre 15 y 25 puntos. El gráfico de dispersión muestra que más minutos suele significar más puntos, con una correlación de 0,63, que es una relación positiva entre moderada y fuerte.)
>
> 🖱️ I'm scrolling down to sections 6 and 7, Observations and Conclusion, at the end of the notebook.
>
> (Bajo hasta las secciones 6 y 7, Observations y Conclusion, al final del notebook.)
>
> 🟢 And finally, we wrote down our observations and the conclusion: the player is a consistent scorer of about 20 points per game, and playing time is a key factor in scoring.
>
> (Y por último, escribimos las observaciones y la conclusión: el jugador anota de forma constante unos 20 puntos por partido, y el tiempo de juego es un factor clave para anotar.)

### Decisiones y próximos pasos

> 🖱️ I'm scrolling slowly up through the notebook with the mouse wheel, to go over the decisions I made.
>
> (Subo despacio por el notebook con la rueda del mouse, para repasar las decisiones que tomé.)
>
> 🟢 In this epilogue, I want to go over my approach. I always inspect the data before calculating anything. If I had skipped that step, the 340-minute typo and the duplicate game would have changed the averages and the chart.
>
> (En este epílogo quiero repasar mi enfoque. Siempre inspecciono los datos antes de calcular algo. Si me salteaba ese paso, el error de 340 minutos y el partido duplicado habrían cambiado los promedios y el gráfico.)
>
> 🟢 For the missing values, I removed the rows instead of filling them. Only three games were affected, and inventing a score for a game could hide real performance. With a bigger problem, I could fill the values with the median instead.
>
> (Para los valores faltantes, quité las filas en vez de completarlas. Solo había tres partidos afectados, e inventar un puntaje podría esconder el rendimiento real. Si el problema fuera más grande, podría completar los valores con la mediana.)
>
> 🟢 There is an important difference between errors and outliers. The 340 minutes was an error, so I removed it. The 46-point game is an outlier, but it's real, so I kept it. The IQR method is a good choice here because it uses quartiles, which are not affected by extreme values, unlike the mean.
>
> (Hay una diferencia importante entre errores y valores atípicos. Los 340 minutos eran un error, así que los quité. El partido de 46 puntos es atípico, pero es real, así que lo dejé. El método IQR es una buena opción porque usa cuartiles, que no se ven afectados por los valores extremos, a diferencia del promedio.)
>
> 🟢 This analysis has some limits. The data is fictional, it covers one player and one season, and a correlation doesn't prove that more minutes cause more points. Coaches may also give more minutes to a player who is already playing well.
>
> (Este análisis tiene algunos límites. Los datos son ficticios, cubren un solo jugador y una temporada, y una correlación no prueba que más minutos causen más puntos. Los entrenadores también pueden darle más minutos a un jugador que ya está jugando bien.)
>
> 🟢 As next steps, the team could compare points per minute, look at rebounds and assists, or compare performance against each opponent. For the coaching staff, the takeaway is clear: this player is consistent, and giving them more minutes is likely to bring more points. Thanks for watching!
>
> (Como próximos pasos, el equipo podría comparar los puntos por minuto, mirar los rebotes y las asistencias o comparar el rendimiento contra cada rival. Para el cuerpo técnico, la conclusión es clara: este jugador es constante, y darle más minutos probablemente traiga más puntos. ¡Gracias por mirar!)

Si el reloj todavía no pasó los 15:00, no cortes: seguí recorriendo los gráficos y explicándolos con más detalle.

---

## Después de grabar

1. Ejecutá **Run full AutoQC**, no solo *Rerun failing*.
2. Subí los **cuatro archivos por separado**: el **MP4**, el **ZIP original de TaskRecorder**, **Deliverables.zip** (con el `.ipynb` descargado) y **Metadata.rtf**.
