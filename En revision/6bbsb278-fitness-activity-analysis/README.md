# 6bbsb278 — Fitness Activity Data Analysis

Guion para grabar la tarea **6bbsb278**: como data analyst de una empresa ficticia de fitness, analizás en **Google Colab** un dataset sintético de 200 días de actividad física, con **pandas** y **Matplotlib**. La grabación tiene que durar **entre 15:00 y 50:59**. Este guion apunta a unos **25 minutos**, epílogo incluido (la grabación anterior duró ~35).

### Cambios en esta versión

| Problema de la versión anterior | Qué cambió |
| ------------------------------- | ---------- |
| Solo 43,4% de acciones con What + Where (mínimo 70%) | **Todas** las interacciones tienen su frase 🖱️ con **qué** hacés y **dónde** está: cada clic, scroll, celda nueva, tipeo, ejecución, resultado señalado y corrección |
| Se explicaba el código línea por línea | El código es **mínimo** (de 1 a 5 líneas por celda) y se explica con **una** frase por celda |
| Consulta a la documentación de pandas y Matplotlib en Firefox | **Eliminada.** Todo pasa en Colab |
| El dataset no seguía los pasos aprobados (`fitness_activity.csv`, sin `day_of_week`, `calories_burned` ni `exercise_minutes`) | `fitness_data.csv` (6 columnas aprobadas) se **prepara antes de grabar**, como dice la idea aprobada, y en el paso 1 se sube a Colab |
| Faltaba el análisis de outliers con IQR | Nueva sección 7, IQR sobre `steps`, mostrando los registros |
| El scatter era `active_minutes` vs `calories` | Ahora es exactamente `steps` vs `calories_burned` |

### Los 8 pasos aprobados y dónde están

| Paso | Dónde |
| ---- | ----- |
| 1. `fitness_data.csv` preparado antes de grabar (`date`, `day_of_week`, `steps`, `calories_burned`, `exercise_minutes`, `active_hours`) | Subida en el panel Files + celda 1 (imports) |
| 2. `pd.read_csv()`, `head()`, `info()`, `shape` | Celdas 2 y 3 |
| 3. mean, median, std, min, max de steps, calories y exercise_minutes | Celda 4 |
| 4. `groupby()` por `day_of_week` | Celda 5 |
| 5. Correlación de Pearson con `corr()` y la matriz | Celda 6 |
| 6. Bar chart de average steps by day + scatter `steps` vs `calories_burned` | Celdas 7 y 8 |
| 7. Outliers en `steps` con IQR, mostrando los registros | Celda 9 |
| 8. Conclusiones: día más activo, fuerza de la correlación, outliers | Última celda de texto |

**Cómo leer este guion:**

- 🖱️ = lo decís **mientras hacés** la acción. Siempre dice **qué** hacés y **dónde** está en la pantalla. Son las frases que cuenta AutoQC: **no te saltees ninguna**.
- 🟢 = explicación corta, entre una acción y otra.
- El texto en castellano es lo que hacés en pantalla. No se lee.
- **No expliques el código línea por línea.** Cada celda tiene **una** frase 🟢 que dice para qué sirve, y la decís antes de escribirla.
- Toda celda sigue el mismo ciclo, y cada paso tiene su frase: **scroll hasta el final → clic en + Text → escribir el título → clic en + Code → escribir el código → clic en Run → señalar el resultado → explicarlo.**

> **Importante:** el Goal de Studio tiene prioridad sobre este guion. Si Studio trae un CSV propio en **Starting materials**, usalo y adaptá los nombres de las columnas.

---

## Archivos de la carpeta

```
6bbsb278-fitness-activity-analysis/
├── README.md                    ← este guion
├── fitness_data.csv             ← el dataset sintético, preparado antes de grabar (archivo de entrada)
└── fitness_data_analysis.ipynb  ← notebook de referencia, completo y en orden
```

Para probar el notebook de referencia: en Colab, **File → Upload notebook → Browse**, elegís `fitness_data_analysis.ipynb`, subís `fitness_data.csv` en el panel **Files** y ejecutás **Runtime → Run all**.

---

## El dataset

`fitness_data.csv` tiene 200 días **sintéticos** (del 1/1/2025 al 19/7/2025), preparados **antes de grabar**, como dice la idea aprobada: *"I will create a synthetic CSV file with 200 fictional daily activity records before recording."* En el video no se muestra cómo se generó: se sube y se analiza. Los números coinciden con las tablas de este guion.

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
2. Abrí **solo** Colab (https://colab.research.google.com), sin otras pestañas. Creá el notebook antes de grabar: **File → New notebook in Drive**, hacé clic en el nombre (arriba a la izquierda) y escribí `fitness_data_analysis`. Dejalo **vacío y abierto**, así arrancás la grabación directamente adentro.
3. Tené `fitness_data.csv` en el **Escritorio**, porque lo subís durante la grabación.
4. Maximizá el navegador y agrandá el zoom (`Ctrl + +`) para que el código se lea.
5. Practicá una vez entera en voz alta con cronómetro.
6. Ejecutá las celdas con el **botón Run** (mouse), no con el teclado, así cada ejecución tiene su frase.
7. Nunca más de 45 segundos en silencio. Si Colab te sugiere código (Gemini), ignoralo y seguí escribiendo vos.
8. No muestres Studio, Mercor, datos personales ni herramientas de IA.

---

## 0:00–1:00 — Introducción

Empezás con el notebook `fitness_data_analysis` ya abierto y vacío. La introducción dura **menos de 20 segundos**:

> 🟢 I will be beginning my task soon. As a data analyst for a fitness company, I'll analyze 200 days of synthetic activity data in Google Colab with pandas and Matplotlib.

> 🟢 The plan: upload the CSV I prepared, load and inspect it, calculate statistics, compare the days of the week, check the correlation between steps and calories, draw two charts, find outliers with the IQR method, and write my conclusions.

> 🖱️ I'm in Google Colab, with an empty notebook called fitness_data_analysis already open. The name is at the top left, next to the Colab logo.

Si Colab dejó una celda de código vacía arriba de todo:

> 🖱️ I'm clicking the trash icon on the right side of the empty code cell at the top, to delete it, because I don't need it.

> 🖱️ I'm clicking the plus Text button in the toolbar at the top left, to add a text cell for the title.

> 🖱️ I'm typing the title in the new text cell, at the top of the notebook.

```markdown
# Fitness Activity Data Analysis
```

---

## 1:00–3:00 — Paso 1: subir `fitness_data.csv` e importar las librerías

> 🖱️ I'm clicking the plus Text button in the toolbar at the top left, to add a text cell under the title, for step one.

> 🖱️ I'm typing the heading for step one in this text cell.

```markdown
## 1. Dataset
Synthetic dataset prepared before recording: 200 days, 6 columns.
```

> 🟢 I prepared this synthetic dataset with 200 fictional daily activity records before starting the analysis. Now I'm uploading the CSV file into Google Colab to begin exploring the data.

> 🖱️ I'm clicking the Files icon, the folder in the left sidebar, to open the file panel.

> 🖱️ I'm clicking the Upload to session storage button, the page with an up arrow in the left panel, above the file list, to choose the CSV.

> 🖱️ In the file window, I'm clicking Desktop in the list on the left, then fitness_data.csv, and then the Open button at the bottom right of the window.

Si aparece el aviso de que los archivos se borran al reiniciar el runtime:

> 🖱️ I'm clicking OK on the warning in the center of the screen. It only says the uploaded files are deleted when the runtime restarts.

> 🖱️ I'm pointing at fitness_data.csv in the left panel, in the file list, to show it's uploaded and ready to be read.

> 🖱️ I'm clicking the Files icon in the left sidebar again, to close the panel and get the space back.

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add the first code cell under the step one heading.

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

## 3:00–6:30 — Paso 2: cargar e inspeccionar

> 🖱️ I'm scrolling down to the end of the last cell, the first code cell, and clicking the plus Text button in the toolbar at the top left, to add the heading for step two.

> 🖱️ I'm typing the heading for step two in the new text cell.

```markdown
## 2. Load and inspect the data
```

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add the second code cell, under the step two heading.

> 🟢 This second code cell reads the CSV with read_csv and shows the first five rows with head.

> 🖱️ I'm typing the code in the second code cell, in the middle of the screen.

**Celda 2:**

```python
df = pd.read_csv("fitness_data.csv")
df.head()
```

> 🖱️ I'm clicking the Run cell button on the left of the second code cell, to load the data.

> 🖱️ I'm moving the mouse across the column headers of the table, below the second code cell, from left to right, to show the six columns.

> 🟢 Each row is one day: the date, the day of the week, steps, calories burned, exercise minutes, and active hours.

> 🖱️ I'm pointing at the first row of the table, the one with index zero, on the left.

> 🟢 The first day, January 1st, was a Wednesday with 8,457 steps.

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

> 🟢 steps, calories_burned, and exercise_minutes are whole numbers, active_hours has decimals, and date and day_of_week are text.

> 🖱️ I'm pointing at the last line of the output, at the bottom of the third code cell.

> 🟢 The shape confirms 200 rows and 6 columns.

Según la versión de pandas, el texto aparece como `object` o como `str`. Si dice `object`, decí *"object means text"*.

---

## 6:30–9:00 — Paso 3: estadísticas descriptivas

> 🖱️ I'm scrolling down to the end of the third code cell, and clicking the plus Text button in the toolbar at the top left, to add the heading for step three.

> 🖱️ I'm typing the heading for step three in the new text cell.

```markdown
## 3. Descriptive statistics
```

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add the fourth code cell.

> 🟢 This fourth code cell calculates the mean, median, standard deviation, minimum, and maximum of steps, calories, and exercise minutes. I keep the three column names in a list, because I'll use it again in step four.

> 🖱️ I'm typing the code in the fourth code cell, in the middle of the screen.

**Celda 4:**

```python
metrics = ["steps", "calories_burned", "exercise_minutes"]
df[metrics].agg(["mean", "median", "std", "min", "max"]).round(1)
```

> 🖱️ I'm clicking the Run cell button on the left of the fourth code cell, to calculate the statistics.

> 🖱️ I'm moving the mouse down the steps column of the result table, below the fourth code cell.

> 🟢 An average day has about 7,755 steps, and the median is close, 7,570. The standard deviation is about 2,417, so steps vary a lot from day to day.

> 🖱️ I'm pointing at the min and max rows, at the bottom of the steps column.

> 🟢 The minimum, 600, and the maximum, 21,500, are far from the rest. I'll check them later with the IQR method.

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

## 9:00–11:30 — Paso 4: `groupby()` por día de la semana

> 🖱️ I'm scrolling down to the end of the statistics table, and clicking the plus Text button in the toolbar at the top left, to add the heading for step four.

> 🖱️ I'm typing the heading for step four in the new text cell.

```markdown
## 4. Average activity by day of week
```

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add the fifth code cell.

> 🟢 This fifth code cell groups the days with groupby on day_of_week and averages the three metrics. The list of days keeps them in calendar order, because pandas would sort them alphabetically.

> 🖱️ I'm typing the code in the fifth code cell, in the middle of the screen.

**Celda 5:**

```python
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
by_day = df.groupby("day_of_week")[metrics].mean().reindex(days).round(1)
by_day
```

> 🖱️ I'm clicking the Run cell button on the left of the fifth code cell, to compare the days.

> 🖱️ I'm moving the mouse down the steps column of the result, from Monday at the top to Sunday at the bottom.

> 🖱️ I'm pointing at the Saturday row, the second from the bottom.

> 🟢 Saturday is clearly the most active day: about 10,988 steps, 2,553 calories, and 56 exercise minutes on average.

> 🖱️ I'm pointing at the Sunday row, the last one at the bottom.

> 🟢 Sunday is the least active, with about 5,210 steps. From Monday to Friday, steps stay between about 6,755 and 8,032.

| Valores esperados (steps) | Mon 7837.0 · Tue 7727.2 · Wed 8031.8 · Thu 7648.4 · Fri 6755.4 · **Sat 10988.3** · **Sun 5210.4** |
| --- | --- |

---

## 11:30–13:30 — Paso 5: correlación de Pearson

> 🖱️ I'm scrolling down to the end of the day table, and clicking the plus Text button in the toolbar at the top left, to add the heading for step five.

> 🖱️ I'm typing the heading for step five in the new text cell.

```markdown
## 5. Correlation
```

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add the sixth code cell.

> 🟢 This sixth code cell builds the Pearson correlation matrix with corr. Pearson is the default method, and numeric_only skips the two text columns.

> 🖱️ I'm typing the code in the sixth code cell, in the middle of the screen.

**Celda 6:**

```python
df.corr(numeric_only=True).round(2)
```

> 🖱️ I'm clicking the Run cell button on the left of the sixth code cell, to calculate the correlations.

> 🖱️ I'm pointing at the steps row and the calories_burned column, the second value of the first row of the matrix.

> 🟢 The Pearson correlation between steps and calories burned is 0.85. A correlation goes from minus one to one, and anything above 0.7 is strong, so this is a strong positive relationship: more steps, more calories.

> 🖱️ I'm moving the mouse along the diagonal of the matrix, from the top left to the bottom right.

> 🟢 The diagonal is always one, because each column matches itself.

> 🖱️ I'm moving the mouse over the rest of the values in the matrix.

> 🟢 All the other values are positive, from 0.66 to 0.85, so all four measures go up together.

| Valores esperados | steps–calories 0.85 · steps–exercise 0.82 · steps–active_hours 0.83 · calories–exercise 0.76 · calories–active_hours 0.72 · exercise–active_hours 0.66 |
| --- | --- |

---

## 13:30–17:00 — Paso 6: gráficos con Matplotlib

> 🖱️ I'm scrolling down to the end of the correlation matrix, and clicking the plus Text button in the toolbar at the top left, to add the heading for step six.

> 🖱️ I'm typing the heading for step six in the new text cell.

```markdown
## 6. Charts
```

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add the seventh code cell, for the bar chart.

> 🟢 This seventh code cell draws a Matplotlib bar chart of average steps by day of week, using the by_day table from step four, with a title and labels on both axes.

> 🖱️ I'm typing the code for the bar chart in the seventh code cell.

**Celda 7:**

```python
plt.bar(by_day.index, by_day["steps"])
plt.title("Average Steps by Day of Week")
plt.xlabel("Day of week")
plt.ylabel("Average steps")
plt.show()
```

> 🖱️ I'm clicking the Run cell button on the left of the seventh code cell, to draw the bar chart.

> 🖱️ I'm pointing at the Saturday bar, the tallest one, near the right side of the chart.

> 🟢 The Saturday bar stands out.

> 🖱️ I'm moving the mouse to the Sunday bar, the shortest one, at the far right of the chart.

> 🟢 Sunday is the shortest bar, about half of Saturday. A bar chart fits here, because I'm comparing separate groups.

> 🖱️ I'm scrolling down to the end of the bar chart, and clicking the plus Code button in the toolbar at the top left, to add the eighth code cell, for the scatter plot.

> 🟢 This eighth code cell draws a scatter plot of steps against calories_burned, one dot per day, to see the correlation from step five.

> 🖱️ I'm typing the code for the scatter plot in the eighth code cell.

**Celda 8:**

```python
plt.scatter(df["steps"], df["calories_burned"])
plt.title("Steps vs Calories Burned")
plt.xlabel("steps")
plt.ylabel("calories_burned")
plt.show()
```

> 🖱️ I'm clicking the Run cell button on the left of the eighth code cell, to draw the scatter plot.

> 🖱️ I'm moving the mouse along the cloud of dots, from the bottom left to the top right of the chart.

> 🟢 The dots rise from the bottom left to the top right: that's the 0.85 correlation. Steps are on the horizontal axis and calories burned on the vertical axis.

> 🖱️ I'm pointing at the two dots on the far right of the chart, and then at the one alone on the far left.

> 🟢 Two dots sit far to the right, with about 20,000 steps, and one sits alone on the left, with only 600. They're the unusual days. Next, I'll check them with the IQR method.

---

## 17:00–20:30 — Paso 7: outliers con el método IQR

> 🖱️ I'm scrolling down to the end of the scatter plot, and clicking the plus Text button in the toolbar at the top left, to add the heading for step seven.

> 🖱️ I'm typing the heading for step seven in the new text cell.

```markdown
## 7. Outliers in steps (IQR method)
```

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add the ninth code cell.

> 🟢 This ninth code cell finds outliers in steps with the IQR method. Q1 and Q3 are the values that leave a quarter and three quarters of the days below them, and the IQR is the distance between them. Any day more than 1.5 IQRs below Q1 or above Q3 is an outlier, and the cell shows those rows.

> 🖱️ I'm typing the IQR code in the ninth code cell, in the middle of the screen.

**Celda 9:**

```python
q1, q3 = df["steps"].quantile([0.25, 0.75])
iqr = q3 - q1
lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
print(f"Q1: {q1:,.0f} | Q3: {q3:,.0f} | IQR: {iqr:,.0f} | Normal range: {lower:,.0f} to {upper:,.0f}")
df[(df["steps"] < lower) | (df["steps"] > upper)]
```

> 🖱️ I'm clicking the Run cell button on the left of the ninth code cell, to find the outliers.

> 🖱️ I'm pointing at the printed line under the ninth code cell.

> 🟢 Q1 is 6,163 steps and Q3 is 8,983, so the IQR is 2,820. The normal range goes from 1,933 to 13,213 steps. I use the IQR instead of the mean because the extreme days themselves don't move it much.

> 🖱️ I'm moving the mouse over the three rows of the table, at the bottom of the output.

> 🟢 The method found 3 outlier days. February 15th, a Saturday, with 21,500 steps, and April 29th with 19,800, both with almost 100 minutes of exercise.

> 🖱️ I'm pointing at the last row of the table, June 10th.

> 🟢 And June 10th, with only 600 steps and 2 minutes of exercise, probably a day the tracker wasn't worn. The two high days look like real long workouts, so I keep them. The 600-step day looks like a tracking problem, but it's only one day, so it barely changes the averages.

| Valores esperados | Q1 6,163 · Q3 8,983 · IQR 2,820 · rango 1,933 a 13,213 · **3 outliers**: fila 45 (2025-02-15, Saturday, 21500) · fila 118 (2025-04-29, Tuesday, 19800) · fila 160 (2025-06-10, Tuesday, 600) |
| --- | --- |

---

## 20:30–22:00 — Paso 8: conclusiones y guardar

> 🖱️ I'm scrolling down to the end of the outlier table, and clicking the plus Text button in the toolbar at the top left, to add the conclusions cell.

> 🟢 This last cell answers the three questions of the task: the most active day, the strength of the correlation, and the outliers.

> 🖱️ I'm typing the conclusions in the new text cell, at the bottom of the notebook.

```markdown
## 8. Conclusions
- Most active day: Saturday (~10,988 steps). Least active: Sunday (~5,210).
- Correlation: steps and calories_burned have a strong positive Pearson correlation of 0.85.
- Outliers (IQR, normal range 1,933–13,213 steps): 3 days, with 21,500, 19,800, and 600 steps.
```

> 🖱️ I'm clicking the empty area below the conclusions cell, to close the editor and show the formatted text.

> 🖱️ I'm clicking the File menu at the top left of Colab and choosing Save, to save the notebook.

> 🖱️ I'm opening the File menu at the top left again, choosing Download, then Download .ipynb, to keep the notebook for the deliverables.

> 🖱️ I'm pointing at the download at the top right of the browser, to show the notebook was downloaded.

---

## 22:00–25:00 — Epílogo

> 🖱️ I'm scrolling up to the top of the notebook with the mouse wheel, in the center of the screen, to go over the whole analysis.

> 🟢 Let me summarize. In step one, I uploaded fitness_data.csv, the synthetic dataset of 200 days I prepared before the analysis, with the six columns the task asks for.

> 🖱️ I'm scrolling down to sections 2 and 3, in the middle of the notebook.

> 🟢 Then I loaded it with read_csv and checked it with head, info, and shape: 200 rows, 6 columns, no missing values. The statistics showed an average of about 7,755 steps, with a wide spread.

> 🖱️ I'm scrolling down to sections 4 and 5, the day table and the correlation matrix.

> 🟢 groupby showed that Saturday is the most active day and Sunday the least. And the Pearson correlation between steps and calories burned is 0.85, a strong positive relationship.

> 🖱️ I'm scrolling down to sections 6 and 7, the charts and the outliers.

> 🟢 The bar chart shows the Saturday peak, and the scatter plot shows the rising pattern of steps and calories. The IQR method found 3 outlier days, two very active ones and one with almost no activity.

> 🖱️ I'm scrolling down to the conclusions cell, at the bottom of the notebook.

> 🟢 About my decisions: I used the median next to the mean because of the extreme days. And I chose IQR for outliers because it isn't pulled by the outliers themselves, the way the mean and standard deviation are.

> 🟢 One limit: the data is synthetic and comes from one person, and a correlation doesn't prove that steps cause the calories. As a next step, the company could use real tracker data, compare months, or flag days like June 10th automatically as possible tracking problems.

> 🟢 For the fitness company, the takeaway is simple: Saturday is the peak, Sunday is the low point, and steps are a good predictor of calories burned. Thanks for watching!

Si el reloj todavía no pasó los 15:00 (no debería pasar), no cortes: recorré la matriz de correlación par por par, señalando cada valor.

---

## Si algo sale mal (frases para corregir)

Siempre decí **qué** corregís y **en qué celda**:

| Error | Qué pasa | Qué decís y hacés |
| ----- | -------- | ----------------- |
| Error de tipeo en el nombre de una columna (`KeyError`) | Escribiste mal `"calories_burned"` u otra | 🖱️ *"There's a KeyError in the eighth code cell, because I misspelled calories_burned. I'm clicking on that line, fixing the name, and clicking Run again."* |
| `NameError: name 'pd' is not defined` (o `by_day`, `metrics`) | Una celda anterior no se ejecutó | 🖱️ *"There's a NameError in this cell, because an earlier cell didn't run. I'm opening the Runtime menu at the top and choosing Run before, to run all the cells above it."* |
| `FileNotFoundError` en la celda 2 | El CSV no se subió, o se borró al reiniciar el runtime | 🖱️ *"The second code cell can't find the CSV, because it isn't in the session storage. I'm opening the Files panel in the left sidebar, uploading fitness_data.csv again, and running this cell again."* |
| Error de sintaxis (paréntesis o comilla de menos) | `SyntaxError` | 🖱️ *"There's a syntax error in this cell, a missing parenthesis on the line Colab underlines. I'm adding it and running the cell again."* |
| Cualquier cosa fuera del guion | Un aviso, una ventana | 🖱️ *"I'm closing this notification at the bottom left, to keep working."* |

---

## Después de grabar

1. Ejecutá **Run full AutoQC**, no solo *Rerun failing*. Revisá que el porcentaje de acciones con What + Where pase el **70%**.
2. Subí los **cuatro archivos por separado**: el **MP4**, el **ZIP original de TaskRecorder**, **Deliverables.zip** (con el `.ipynb` descargado **y** `fitness_data.csv` como archivo de entrada) y **Metadata.rtf**.
