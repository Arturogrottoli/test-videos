# 6bbsb278 — Fitness Activity Data Analysis

Guion para grabar la tarea **6bbsb278**: como data analyst de una empresa ficticia de fitness, analizás en **Google Colab** un dataset sintético de 200 días de actividad física, con **pandas** y **Matplotlib**. La grabación tiene que durar **entre 15:00 y 50:59**. Este guion apunta a unos **28 minutos**, epílogo incluido (la grabación anterior duró ~35).

### Cambios en esta versión

| Problema de la versión anterior | Qué cambió |
| ------------------------------- | ---------- |
| Solo 43,4% de acciones con What + Where (mínimo 70%) | Cada clic, scroll, celda nueva, ejecución y corrección tiene su frase 🖱️ con **qué** hacés y **dónde** está |
| Se explicaba el código línea por línea | Una frase corta por **bloque** de código, que dice para qué sirve |
| Consulta a la documentación de pandas y Matplotlib en Firefox | **Eliminada.** Todo pasa en Colab |
| El dataset no seguía los pasos aprobados (`fitness_activity.csv`, sin `day_of_week`, `calories_burned` ni `exercise_minutes`) | El paso 1 **crea** `fitness_data.csv` en Colab, con las 6 columnas aprobadas |
| Faltaba el análisis de outliers con IQR | Nueva sección 7, IQR sobre `steps` |
| El scatter era `active_minutes` vs `calories` | Ahora es exactamente `steps` vs `calories_burned` |

### Los 8 pasos aprobados y dónde están

| Paso | Dónde |
| ---- | ----- |
| 1. Crear `fitness_data.csv` (`date`, `day_of_week`, `steps`, `calories_burned`, `exercise_minutes`, `active_hours`) | Celda 1 |
| 2. `pd.read_csv()`, `head()`, `info()`, `shape` | Celdas 2 y 3 |
| 3. mean, median, std, min, max de steps, calories y exercise_minutes | Celda 4 |
| 4. `groupby()` por `day_of_week` | Celda 5 |
| 5. Correlación de Pearson con `corr()` y la matriz | Celda 6 |
| 6. Bar chart de average steps by day + scatter `steps` vs `calories_burned` | Celdas 7 y 8 |
| 7. Outliers en `steps` con IQR, imprimiendo los registros | Celda 9 |
| 8. Conclusiones: día más activo, fuerza de la correlación, outliers | Última celda de texto |

**Cómo leer este guion:**

- 🖱️ = lo decís **mientras hacés** la acción. Siempre dice **qué** hacés y **dónde** está en la pantalla. Son las frases que cuenta AutoQC.
- 🟢 = explicación corta, entre una acción y otra.
- El texto en castellano es lo que hacés en pantalla. No se lee.
- **No expliques el código línea por línea.** Antes de escribir una celda decís para qué sirve. Si la celda es larga, decís la frase del bloque cuando llegás a ese bloque.

> **Importante:** el Goal de Studio tiene prioridad sobre este guion. Si Studio trae un CSV propio en **Starting materials**, usalo y adaptá los nombres de las columnas.

---

## Archivos de la carpeta

```
6bbsb278-fitness-activity-analysis/
├── README.md                    ← este guion
├── fitness_data.csv             ← el CSV que crea la celda 1 (referencia, para comparar)
└── fitness_data_analysis.ipynb  ← notebook de referencia, completo y en orden
```

Para probar el notebook de referencia: en Colab, **File → Upload notebook → Browse**, elegís `fitness_data_analysis.ipynb` y ejecutás **Runtime → Run all**. No hace falta subir el CSV: la celda 1 lo crea.

---

## El dataset

La celda 1 genera 200 días **sintéticos** (del 1/1/2025 al 19/7/2025) con una semilla fija (`42`), así que los números salen **siempre iguales** y coinciden con las tablas de este guion.

| Columna | Qué contiene |
| ------- | ------------ |
| `date` | Fecha |
| `day_of_week` | Nombre del día (Monday … Sunday) |
| `steps` | Pasos del día. Los sábados son más altos y los domingos más bajos |
| `calories_burned` | Calorías quemadas, que dependen de los pasos y los minutos de ejercicio |
| `exercise_minutes` | Minutos de ejercicio |
| `active_hours` | Horas activas |

Tres días tienen valores fuera de lo común **a propósito**, para que el IQR tenga algo que encontrar: 21.500 pasos (fila 45), 19.800 (fila 118) y 600 (fila 160).

---

## Antes de grabar

1. Leé el Goal y comparalo con este guion.
2. Abrí **solo** Colab (https://colab.research.google.com), con el cuadro **Open notebook** a la vista. Ninguna otra pestaña.
3. Maximizá el navegador y agrandá el zoom (`Ctrl + +`) para que el código se lea.
4. Practicá una vez entera en voz alta con cronómetro.
5. Ejecutá las celdas con el **botón Run** (mouse), no con el teclado, así cada ejecución tiene su frase.
6. Nunca más de 45 segundos en silencio. Si Colab te sugiere código (Gemini), ignoralo y seguí escribiendo vos.
7. No muestres Studio, Mercor, datos personales ni herramientas de IA.

---

## 0:00–1:30 — Introducción y notebook nuevo

La introducción dura **menos de 20 segundos**:

> 🟢 I will be beginning my task soon. As a data analyst for a fitness company, I'll analyze 200 days of synthetic activity data in Google Colab with pandas and Matplotlib.

> 🟢 The plan: create the CSV, load and inspect it, calculate statistics, compare the days of the week, check the correlation between steps and calories, draw two charts, find outliers with the IQR method, and write my conclusions.

> 🖱️ I'm clicking the New notebook button at the bottom of the Open notebook dialog, in the center of the screen, to start a blank notebook.

> 🖱️ I'm clicking the notebook name at the top left, next to the Colab logo, and typing fitness_data_analysis, so the file has a clear name.

> 🖱️ I'm clicking the plus Text button in the toolbar at the top left, to add a title cell above the code.

Escribís:

```markdown
# Fitness Activity Data Analysis
Goal: analyze 200 days of synthetic fitness data: statistics, activity by day of week, the correlation between steps and calories, charts, and outliers in steps.
```

> 🟢 This text cell holds the title and the goal, so anyone who opens the notebook knows what it's about.

Si Colab dejó una celda de código vacía arriba de todo:

> 🖱️ I'm clicking the trash icon on the right side of the empty code cell at the top, to delete it, because I don't need it.

---

## 1:30–5:00 — Paso 1: crear `fitness_data.csv`

> 🖱️ I'm clicking the plus Text button in the toolbar at the top left, to add the heading for step one under the title.

Escribís `## 1. Create the dataset`.

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add the first code cell under that heading.

> 🟢 In this first code cell I'll import the libraries and build the dataset: 200 days, with the six columns the task asks for, saved as fitness_data.csv.

Escribís la **celda 1**. Decí cada frase 🟢 cuando llegás a ese bloque:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
fitness = pd.DataFrame({"date": pd.date_range("2025-01-01", periods=200)})
fitness["day_of_week"] = fitness["date"].dt.day_name()

avg_steps = {"Monday": 8000, "Tuesday": 7500, "Wednesday": 8000, "Thursday": 7500,
             "Friday": 7000, "Saturday": 10500, "Sunday": 5500}
steps = fitness["day_of_week"].map(avg_steps) + rng.normal(0, 1500, 200)
steps[[45, 118, 160]] = [21500, 19800, 600]
minutes = steps / 200 + rng.normal(0, 8, 200)

fitness["steps"] = steps.round().astype(int)
fitness["calories_burned"] = (1600 + steps * 0.07 + minutes * 3 + rng.normal(0, 120, 200)).round().astype(int)
fitness["exercise_minutes"] = minutes.clip(0).round().astype(int)
fitness["active_hours"] = (steps / 4000 + rng.normal(0, 0.4, 200)).clip(0.2).round(1)

fitness.to_csv("fitness_data.csv", index=False)
print("Saved fitness_data.csv:", fitness.shape)
```

- Al escribir los imports y la semilla:

  > 🟢 First, the imports: NumPy for random numbers, pandas for the table, and Matplotlib for the charts. The seed, 42, makes the random numbers the same every time, so the results are reproducible.

- Al escribir `date` y `day_of_week`:

  > 🟢 Next, 200 dates starting on January 1st, 2025, and the name of each day, which I'll need to compare the days of the week.

- Al escribir `avg_steps` y `steps`:

  > 🟢 Each day of the week gets a typical number of steps, with Saturday the highest and Sunday the lowest, plus random variation. I'm also adding three unusual days on purpose, a very long walk, a race, and a day the tracker was barely worn, so the outlier check has something real to find.

- Al escribir las cuatro columnas `fitness[...]`:

  > 🟢 Calories and exercise minutes grow with the steps, plus some noise, like real tracker data. I round every value, so the CSV looks like a real export.

- Al escribir `to_csv`:

  > 🟢 And finally, I save the table as fitness_data.csv, without the index, and print its size.

> 🖱️ I'm clicking the Run cell button, the play icon on the left edge of this cell, to create the CSV.

> 🟢 The first run takes a few seconds, because Colab is connecting to a runtime. The status at the top right turns green when it's ready.

Salida esperada: `Saved fitness_data.csv: (200, 6)`.

> 🖱️ I'm clicking the Files icon, the folder in the left sidebar, to check that the file was created.

> 🟢 Here it is: fitness_data.csv, in the session storage. 200 rows and 6 columns, as the output says.

> 🖱️ I'm clicking the Files icon in the left sidebar again, to close the panel and get the space back.

---

## 5:00–8:30 — Paso 2: cargar e inspeccionar

> 🖱️ I'm scrolling down to the bottom of the notebook, below the output of the first cell, and clicking the plus Text button in the toolbar at the top left, to add the heading for step two.

Escribís `## 2. Load and inspect the data`.

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add a code cell that loads the CSV.

> 🟢 In this second code cell I read the CSV with read_csv, like any analyst would with a file they received, and show the first rows with head.

Escribís la **celda 2**:

```python
df = pd.read_csv("fitness_data.csv")
df.head()
```

> 🖱️ I'm clicking the Run cell button on the left of the second code cell, to load the data.

Señalás las columnas con el mouse, de izquierda a derecha:

> 🖱️ I'm moving the mouse across the column headers of the table, below the cell, to show the six columns.

> 🟢 Each row is one day: the date, the day of the week, steps, calories burned, exercise minutes, and active hours. The first day, January 1st, was a Wednesday with 8,457 steps.

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

> 🟢 All six columns have 200 non-null values, so nothing is missing. steps, calories_burned, and exercise_minutes are whole numbers, active_hours has decimals, and date and day_of_week are text. The shape confirms 200 rows and 6 columns.

Según la versión de pandas, el texto aparece como `object` o como `str`. Si dice `object`, decí *"object means text"*.

---

## 8:30–11:00 — Paso 3: estadísticas descriptivas

> 🖱️ I'm scrolling down below the info output, and clicking the plus Text button in the toolbar at the top left, to add the heading for step three.

Escribís `## 3. Descriptive statistics`.

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add the fourth code cell.

> 🟢 Here I calculate the five statistics the task asks for, mean, median, standard deviation, minimum, and maximum, for steps, calories, and exercise minutes. I save the three column names in a list, because I'll reuse it.

Escribís la **celda 4**:

```python
metrics = ["steps", "calories_burned", "exercise_minutes"]
df[metrics].agg(["mean", "median", "std", "min", "max"]).round(1)
```

> 🖱️ I'm clicking the Run cell button on the left of the fourth code cell, to calculate the statistics.

> 🖱️ I'm moving the mouse down the steps column of the result table, below the cell.

> 🟢 An average day has about 7,755 steps, and the median is close, 7,570. The standard deviation is about 2,417, so steps vary a lot from day to day. The minimum, 600, and the maximum, 21,500, are far from the rest. I'll check them later with the IQR method.

> 🖱️ I'm moving the mouse to the calories_burned and exercise_minutes columns, on the right of the table.

> 🟢 Calories average about 2,251, between 1,639 and 3,414. Exercise averages 39 minutes, with a maximum of 107.

| Valores esperados | steps | calories_burned | exercise_minutes |
| ----------------- | ----- | --------------- | ---------------- |
| mean | 7754.9 | 2251.5 | 39.0 |
| median | 7570.0 | 2236.0 | 38.0 |
| std | 2417.4 | 234.9 | 14.2 |
| min | 600.0 | 1639.0 | 0.0 |
| max | 21500.0 | 3414.0 | 107.0 |

---

## 11:00–13:30 — Paso 4: `groupby()` por día de la semana

> 🖱️ I'm scrolling down below the statistics table, and clicking the plus Text button in the toolbar at the top left, to add the heading for step four.

Escribís `## 4. Average activity by day of week`.

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add the fifth code cell.

> 🟢 Now I group the days with groupby on day_of_week and calculate the average of the three metrics for each day. I add a list with the days in calendar order, because pandas would sort them alphabetically, starting with Friday.

Escribís la **celda 5**:

```python
day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
by_day = df.groupby("day_of_week")[metrics].mean().reindex(day_order).round(1)
by_day
```

> 🖱️ I'm clicking the Run cell button on the left of the fifth code cell, to compare the days.

> 🖱️ I'm moving the mouse down the steps column of the result, from Monday to Sunday.

> 🟢 Saturday is clearly the most active day: about 10,988 steps, 2,553 calories, and 56 exercise minutes on average. Sunday is the least active, with about 5,210 steps. From Monday to Friday, steps stay between about 6,755 and 8,032.

| Valores esperados (steps) | Mon 7837.0 · Tue 7727.2 · Wed 8031.8 · Thu 7648.4 · Fri 6755.4 · **Sat 10988.3** · **Sun 5210.4** |
| --- | --- |

---

## 13:30–16:00 — Paso 5: correlación de Pearson

> 🖱️ I'm scrolling down below the day table, and clicking the plus Text button in the toolbar at the top left, to add the heading for step five.

Escribís `## 5. Correlation`.

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add the sixth code cell.

> 🟢 This cell calculates the Pearson correlation between steps and calories_burned with corr, and then shows the full correlation matrix of the four number columns. Pearson is the default method of corr.

Escribís la **celda 6**:

```python
pearson = df["steps"].corr(df["calories_burned"])
print("Pearson correlation (steps vs calories_burned):", round(pearson, 2))
df[["steps", "calories_burned", "exercise_minutes", "active_hours"]].corr().round(2)
```

> 🖱️ I'm clicking the Run cell button on the left of the sixth code cell, to calculate the correlation.

> 🖱️ I'm pointing at the printed line above the matrix, under the cell.

> 🟢 The Pearson correlation between steps and calories burned is 0.85. A correlation goes from minus one to one, and anything above 0.7 is strong, so this is a strong positive relationship: more steps, more calories.

> 🖱️ I'm moving the mouse across the correlation matrix, below the printed line.

> 🟢 The diagonal is always one, because each column matches itself. All the other values are positive, from 0.66 to 0.85, so all four measures go up together.

---

## 16:00–20:00 — Paso 6: gráficos con Matplotlib

> 🖱️ I'm scrolling down below the correlation matrix, and clicking the plus Text button in the toolbar at the top left, to add the heading for step six.

Escribís `## 6. Charts`.

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add the seventh code cell, for the bar chart.

> 🟢 The first chart is a bar chart of average steps by day of week, with Matplotlib. It uses the by_day table from step four, with one bar per day, a title, and labels on both axes.

Escribís la **celda 7**:

```python
plt.figure(figsize=(8, 4))
plt.bar(by_day.index, by_day["steps"], color="steelblue")
plt.title("Average Steps by Day of Week")
plt.xlabel("Day of week")
plt.ylabel("Average steps")
plt.show()
```

> 🖱️ I'm clicking the Run cell button on the left of the seventh code cell, to draw the bar chart.

> 🖱️ I'm pointing at the Saturday bar, the tallest one, near the right side of the chart.

> 🟢 The Saturday bar stands out, about twice as tall as Sunday, the shortest bar right next to it. A bar chart fits here, because I'm comparing separate groups.

> 🖱️ I'm scrolling down below the bar chart, and clicking the plus Code button in the toolbar at the top left, to add the eighth code cell, for the scatter plot.

> 🟢 The second chart is a scatter plot of steps against calories_burned, one dot per day, to see the correlation from step five.

Escribís la **celda 8**:

```python
plt.figure(figsize=(6, 4))
plt.scatter(df["steps"], df["calories_burned"], alpha=0.6)
plt.title("Steps vs Calories Burned")
plt.xlabel("steps")
plt.ylabel("calories_burned")
plt.show()
```

> 🟢 alpha makes the dots a bit transparent, so the overlapping ones are easier to see.

> 🖱️ I'm clicking the Run cell button on the left of the eighth code cell, to draw the scatter plot.

> 🖱️ I'm moving the mouse along the cloud of dots, from the bottom left to the top right of the chart.

> 🟢 The dots rise from the bottom left to the top right: that's the 0.85 correlation. Steps are on the horizontal axis and calories burned on the vertical axis.

> 🖱️ I'm pointing at the two dots on the far right, and the one alone on the far left.

> 🟢 Two dots sit far to the right, with about 20,000 steps, and one sits alone on the left, with only 600. They're the unusual days. Next, I'll check them with the IQR method.

---

## 20:00–23:30 — Paso 7: outliers con el método IQR

> 🖱️ I'm scrolling down below the scatter plot, and clicking the plus Text button in the toolbar at the top left, to add the heading for step seven.

Escribís `## 7. Outliers in steps (IQR method)`.

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add the ninth code cell.

> 🟢 The IQR method finds outliers in steps. Q1 is the value below which a quarter of the days fall, and Q3 is the value below which three quarters fall. The IQR is the distance between them.

> 🟢 Any day below Q1 minus 1.5 times the IQR, or above Q3 plus 1.5 times the IQR, is an outlier. I use the IQR instead of the mean because the extreme days themselves don't move it much.

Escribís la **celda 9**:

```python
q1 = df["steps"].quantile(0.25)
q3 = df["steps"].quantile(0.75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
print(f"Q1: {q1:,.0f} | Q3: {q3:,.0f} | IQR: {iqr:,.0f}")
print(f"Normal range: {lower:,.0f} to {upper:,.0f} steps")

outliers = df[(df["steps"] < lower) | (df["steps"] > upper)]
print("Outliers found:", len(outliers))
outliers
```

- Al llegar a la línea `outliers = ...`:

  > 🟢 This filter keeps only the rows below the lower bound or above the upper bound. The vertical bar means "or".

> 🖱️ I'm clicking the Run cell button on the left of the ninth code cell, to find the outliers.

> 🖱️ I'm pointing at the printed lines under the cell.

> 🟢 Q1 is 6,163 steps and Q3 is 8,983, so the IQR is 2,820. The normal range goes from 1,933 to 13,213 steps.

> 🖱️ I'm moving the mouse over the three rows of the outlier table, at the bottom of the output.

> 🟢 The method found 3 outlier days. February 15th, a Saturday, with 21,500 steps, and April 29th with 19,800, both with almost 100 minutes of exercise. And June 10th with only 600 steps and 2 minutes of exercise, probably a day the tracker wasn't worn.

> 🟢 The two high days look like real long workouts, so I keep them. The 600-step day looks like a tracking problem, but it's only one day, so it barely changes the averages.

| Valores esperados | Q1 6,163 · Q3 8,983 · IQR 2,820 · rango 1,933 a 13,213 · **3 outliers**: fila 45 (2025-02-15, Saturday, 21500) · fila 118 (2025-04-29, Tuesday, 19800) · fila 160 (2025-06-10, Tuesday, 600) |
| --- | --- |

---

## 23:30–25:00 — Paso 8: conclusiones y guardar

> 🖱️ I'm scrolling down to the bottom of the notebook, below the outlier table, and clicking the plus Text button in the toolbar at the top left, to add the conclusions cell.

> 🟢 The last cell answers the three questions of the task: the most active day, the strength of the correlation, and the outliers.

Escribís:

```markdown
## 8. Conclusions
- **Most active day:** Saturday, with about 10,988 steps on average. Sunday is the least active, with about 5,210.
- **Correlation:** steps and calories_burned have a strong positive Pearson correlation of 0.85. More steps usually means more calories burned.
- **Outliers:** the IQR method (normal range 1,933 to 13,213 steps) found 3 outlier days: 21,500 steps on 2025-02-15, 19,800 on 2025-04-29, and only 600 on 2025-06-10.
```

> 🖱️ I'm clicking the File menu at the top left of Colab and choosing Save, to save the notebook.

> 🖱️ I'm opening the File menu at the top left again, choosing Download, then Download .ipynb, to keep the notebook for the deliverables.

> 🖱️ I'm clicking the Files icon in the left sidebar, then the three dots next to fitness_data.csv, and choosing Download, to keep the CSV too.

---

## 25:00–28:00 — Epílogo

> 🖱️ I'm scrolling up to the top of the notebook with the mouse wheel, in the center of the screen, to go over the whole analysis.

> 🟢 Let me summarize. In step one, I created a synthetic dataset of 200 days with the six columns the task asks for, and saved it as fitness_data.csv.

> 🖱️ I'm scrolling down to sections 2 and 3, in the middle of the notebook.

> 🟢 Then I loaded it with read_csv and checked it with head, info, and shape: 200 rows, 6 columns, no missing values. The statistics showed an average of about 7,755 steps, with a wide spread.

> 🖱️ I'm scrolling down to sections 4 and 5.

> 🟢 groupby showed that Saturday is the most active day and Sunday the least. And the Pearson correlation between steps and calories burned is 0.85, a strong positive relationship.

> 🖱️ I'm scrolling down to sections 6 and 7, the charts and the outliers.

> 🟢 The bar chart shows the Saturday peak, and the scatter plot shows the rising pattern of steps and calories. The IQR method found 3 outlier days, two very active ones and one with almost no activity.

> 🟢 About my decisions: I used a fixed seed so the results are reproducible. I used the median next to the mean because of the extreme days. And I chose IQR for outliers because it isn't pulled by the outliers themselves, the way the mean and standard deviation are.

> 🟢 One limit: the data is synthetic and comes from one person, and a correlation doesn't prove that steps cause the calories. As a next step, the company could use real tracker data, compare months, or flag days like June 10th automatically as possible tracking problems.

> 🟢 For the fitness company, the takeaway is simple: Saturday is the peak, Sunday is the low point, and steps are a good predictor of calories burned. Thanks for watching!

Si el reloj todavía no pasó los 15:00 (no debería pasar), no cortes: recorré la matriz de correlación par por par.

---

## Si algo sale mal (frases para corregir)

Siempre decí **qué** corregís y **en qué celda**:

| Error | Qué pasa | Qué decís y hacés |
| ----- | -------- | ----------------- |
| Error de tipeo en el nombre de una columna (`KeyError`) | Escribiste mal `"calories_burned"` u otra | 🖱️ *"There's a KeyError in the sixth code cell, because I misspelled calories_burned. I'm clicking on that line, fixing the name, and clicking Run again."* |
| `NameError: name 'pd' is not defined` (o `by_day`, `metrics`) | Una celda anterior no se ejecutó | 🖱️ *"There's a NameError in this cell, because an earlier cell didn't run. I'm opening the Runtime menu at the top and choosing Run before, to run all the cells above it."* |
| `FileNotFoundError` en la celda 2 | No se ejecutó la celda 1 | 🖱️ *"The second code cell can't find the CSV, because the first cell didn't run. I'm scrolling up and clicking Run on the first code cell, then running this one again."* |
| Error de sintaxis (paréntesis o comilla de menos) | `SyntaxError` | 🖱️ *"There's a syntax error in this cell, a missing parenthesis on the line Colab underlines. I'm adding it and running the cell again."* |
| Cualquier cosa fuera del guion | Un aviso, una ventana | 🖱️ *"I'm closing this notification at the bottom left, to keep working."* |

---

## Después de grabar

1. Ejecutá **Run full AutoQC**, no solo *Rerun failing*. Revisá que el porcentaje de acciones con What + Where pase el **70%**.
2. Subí los **cuatro archivos por separado**: el **MP4**, el **ZIP original de TaskRecorder**, **Deliverables.zip** (con el `.ipynb` descargado **y** `fitness_data.csv`) y **Metadata.rtf**.
