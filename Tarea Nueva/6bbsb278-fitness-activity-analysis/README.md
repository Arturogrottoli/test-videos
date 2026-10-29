# 6bbsb278 — Fitness Activity Analysis

Guion paso a paso para grabar la tarea **6bbsb278**: analizar 200 registros diarios ficticios de actividad física en **Google Colab**, con **Python**, **pandas** y **Matplotlib**. El trabajo incluye revisar la calidad de los datos, calcular estadísticas, comparar patrones por tipo de entrenamiento y por día de la semana, ver qué variables se relacionan y visualizar los resultados. La grabación tiene que durar **entre 15:00 y 50:59**. Este guion apunta a unos **26 minutos**, epílogo incluido.

**Cómo leer este guion:**

- Las frases que empiezan con 🖱️ las decís **en el momento de hacer clic, desplazarte o escribir**. Siempre dicen **qué** elemento usás, **dónde** está en la pantalla y **por qué** lo usás. Son las que revisa AutoQC.
- Las frases que empiezan con 🟢 son la explicación que **decís en inglés** entre una acción y otra.
- Debajo de cada bloque de código, la lista **What each line does** explica cada línea en inglés. La leés en voz alta mientras escribís esa línea.
- El resto, en castellano, es lo que hacés en pantalla. Las traducciones aparecen entre paréntesis después de cada frase.

> **Importante:** el Goal de Studio tiene prioridad sobre este guion. Antes de grabar, revisá el apartado **Starting materials**: si Studio trae su propio CSV, usá ese y adaptá los nombres de las columnas. Si no trae nada, usá `fitness_activity.csv` de esta carpeta. El dataset lo armé yo: es ficticio y tiene errores puestos a propósito para limpiarlos. El Goal no dice qué herramienta usar: este guion usa Google Colab.

---

## Archivos de la carpeta

```
6bbsb278-fitness-activity-analysis/
├── README.md                        ← este guion
├── fitness_activity.csv             ← dataset de partida: 200 días, con errores para limpiar
└── fitness_activity_analysis.ipynb  ← notebook de referencia, completo y en orden
```

Para probar el notebook de referencia: en https://colab.research.google.com elegís **File → Upload notebook** y seleccionás `fitness_activity_analysis.ipynb`. Después subís `fitness_activity.csv` desde el panel **Files** y ejecutás **Runtime → Run all**.

---

## El dataset

`fitness_activity.csv` tiene 200 días **ficticios** de una sola persona, del 1/1/2025 al 19/7/2025, con 6 columnas:

| Columna | Qué contiene |
| ------- | ------------ |
| `date` | Fecha |
| `steps` | Pasos del día |
| `active_minutes` | Minutos de actividad |
| `calories` | Calorías quemadas en el día |
| `sleep_hours` | Horas de sueño |
| `workout_type` | Running, Cycling, Strength, Yoga o Rest |

**Errores puestos a propósito** (los encontrás y los limpiás durante la grabación):

| Problema | Dónde | Cómo se limpia |
| -------- | ----- | -------------- |
| Valor imposible | Pasos `-1` el 22/2 y el 30/4 (error del sensor) | Filtrar `steps >= 0` |
| Valores faltantes | Sin horas de sueño el 6/2, 29/3, 20/5 y 20/6 | `fillna()` con la mediana (7,15) |
| Nombres inconsistentes | 9 formas de escribir 5 entrenamientos (`running`, `YOGA`, `Cycling ` con espacio atrás, ` strength` con espacio adelante) | `str.strip().str.title()` |

---

## Antes de grabar

1. Leé el Goal y compará este guion con el campo **Describe your idea** de Studio.
2. Practicá una vez entera en un notebook nuevo, leyendo en voz alta todas las frases 🖱️ y 🟢, y cronometrá.
3. Pegá el Goal en un documento de **Google Docs** y borrá el **Approval ID** y cualquier dato personal. Agrandá el texto hasta que se lea completo.
4. Dejá cuatro pestañas abiertas en Firefox, en este orden: el documento del **Goal**, Colab (https://colab.research.google.com), el sitio de pandas (https://pandas.pydata.org) y el sitio de Matplotlib (https://matplotlib.org). En Colab dejá a la vista el cuadro **Open notebook**, sin crear todavía el notebook. Tené `fitness_activity.csv` en una carpeta fácil de encontrar, como el Escritorio. Agrandá el zoom del navegador (`Ctrl + +`).
5. Maximizá el navegador y cerrá o minimizá las demás ventanas, para que ninguna tape a otra.
6. Pausa de ~1 segundo después de cada clic y nunca más de 45 segundos en silencio.
7. No muestres Studio, Mercor, información privada ni herramientas de IA. Si Colab muestra funciones de IA (Gemini), no las uses. Cerrá este guion si está en la misma pantalla.

---

## 0:00–1:30 — El Goal y el plan

Empezás en la primera pestaña, la del **Goal**, con el texto completo y legible. La introducción dura menos de 20 segundos: la frase de apertura y el objetivo.

> 🟢 I will be beginning my task soon. Here is the workflow I have in mind.
>
> (Voy a empezar mi tarea en breve. Este es el flujo de trabajo que tengo en mente.)
>
> 🖱️ I'm on the Goal document, in the first browser tab, to show what this task asks for.
>
> (Estoy en el documento del Goal, en la primera pestaña del navegador, para mostrar qué pide esta tarea.)
>
> 🟢 As a data analyst, I'll analyze 200 days of fitness records with Python and pandas. I'll check the data quality, calculate summary statistics, compare activity patterns, look at relationships between variables, and visualize the results.
>
> (Como analista de datos, voy a analizar 200 días de registros de actividad física con Python y pandas. Voy a revisar la calidad de los datos, calcular estadísticas, comparar patrones de actividad, ver las relaciones entre variables y visualizar los resultados.)

Ajustá esta frase a lo que diga tu Goal. Después contás el plan, paso por paso:

> 🟢 Here's the plan. First, I'll load the CSV file in Google Colab and inspect it, to find any problems before calculating anything.
>
> (Este es el plan. Primero, voy a cargar el archivo CSV en Google Colab e inspeccionarlo, para encontrar los problemas antes de calcular nada.)
>
> 🟢 Second, I'll clean the data and add a column with the day of the week. Third, I'll calculate summary statistics for steps, active minutes, calories, and sleep.
>
> (Segundo, voy a limpiar los datos y agregar una columna con el día de la semana. Tercero, voy a calcular estadísticas de los pasos, los minutos activos, las calorías y el sueño.)
>
> 🟢 Fourth, I'll compare the activity by workout type and by day of the week, and use correlations to see which measures move together.
>
> (Cuarto, voy a comparar la actividad por tipo de entrenamiento y por día de la semana, y usar correlaciones para ver qué medidas se mueven juntas.)
>
> 🟢 Finally, I'll draw three charts with Matplotlib and write down my conclusions in the notebook.
>
> (Por último, voy a hacer tres gráficos con Matplotlib y anotar mis conclusiones en el notebook.)

---

## 1:30–3:00 — Colab, pandas y Matplotlib

> 🖱️ I'm clicking the second browser tab, at the top of the window, to open Google Colab.
>
> (Hago clic en la segunda pestaña del navegador, arriba de la ventana, para abrir Google Colab.)
>
> 🟢 Google Colab is a free tool from Google that runs Python notebooks in the browser. The code runs in Google's cloud, so there's nothing to install.
>
> (Google Colab es una herramienta gratuita de Google que ejecuta notebooks de Python en el navegador. El código se ejecuta en la nube de Google, así que no hay que instalar nada.)
>
> 🖱️ I'm clicking the third browser tab, at the top of the window, to show the official pandas website.
>
> (Hago clic en la tercera pestaña del navegador, arriba de la ventana, para mostrar el sitio oficial de pandas.)
>
> 🟢 This is pandas, a free Python library for tables of data. I'll use it to load the records, clean them, group them, and calculate the statistics and correlations.
>
> (Esto es pandas, una librería gratuita de Python para trabajar con tablas de datos. La voy a usar para cargar los registros, limpiarlos, agruparlos y calcular las estadísticas y las correlaciones.)
>
> 🖱️ I'm clicking the fourth browser tab, at the top of the window, to show the official Matplotlib website.
>
> (Hago clic en la cuarta pestaña del navegador, arriba de la ventana, para mostrar el sitio oficial de Matplotlib.)
>
> 🟢 This is Matplotlib, the most popular charting library in Python. pandas uses it behind the scenes when we call plot. Both libraries come already installed in Colab.
>
> (Esto es Matplotlib, la librería de gráficos más popular de Python. pandas la usa por detrás cuando llamamos a plot. Las dos librerías vienen instaladas en Colab.)
>
> 🖱️ I'm clicking the second browser tab, at the top of the window, to go back to Google Colab.
>
> (Hago clic en la segunda pestaña del navegador, arriba de la ventana, para volver a Google Colab.)

---

## 3:00–6:30 — Notebook nuevo y cargar los datos

> 🖱️ I'm clicking the New notebook button at the bottom of the Open notebook dialog, to create a fresh notebook.
>
> (Hago clic en el botón New notebook, abajo del cuadro Open notebook, para crear un notebook nuevo.)
>
> 🖱️ I'm clicking the notebook title field at the top left, and typing fitness_activity_analysis.ipynb, to identify this analysis.
>
> (Hago clic en el campo del título del notebook, arriba a la izquierda, y escribo fitness_activity_analysis.ipynb, para identificar este análisis.)

Subís el CSV:

> 🖱️ I'm clicking the Files icon, the folder in the left sidebar, to upload the dataset.
>
> (Hago clic en el ícono Files, la carpeta de la barra lateral izquierda, para subir el dataset.)
>
> 🖱️ I'm clicking the Upload to session storage icon, at the top of the Files pane, and choosing fitness_activity.csv from my computer, so the notebook can read it.
>
> (Hago clic en el ícono Upload to session storage, arriba del panel Files, y elijo fitness_activity.csv de mi computadora, para que el notebook pueda leerlo.)

Si aparece un aviso de que los archivos se borran al reiniciar el entorno: *"I'm clicking OK on this warning, in the center of the screen, to continue the upload."*

> 🖱️ I'm clicking the plus Text button in the toolbar at the top left, to add a title and the goal.
>
> (Hago clic en el botón + Text de la barra de herramientas, arriba a la izquierda, para agregar un título y el objetivo.)

```markdown
# Fitness Activity Analysis
Dataset: 200 days of fitness records. Goal: check data quality, calculate summary statistics, compare activity patterns, examine relationships between variables, and visualize the results.
```

**What each line does:**

- 🟢 `# Fitness Activity Analysis`: the hash sign makes this the main title of the notebook.
- 🟢 `Dataset: ... Goal: ...`: this line says what the data is and what I want to find out.

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add a code cell that loads the libraries and the data.
>
> (Hago clic en el botón + Code de la barra de herramientas, arriba a la izquierda, para agregar una celda de código que carga las librerías y los datos.)

Escribís la **celda 1**:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("fitness_activity.csv")
df.head()
```

**What each line does:**

- 🟢 `import pandas as pd`: this loads pandas, the library for tables of data, with its usual short name, pd.
- 🟢 `import matplotlib.pyplot as plt`: this loads pyplot, the part of Matplotlib that draws and shows charts, as plt.
- 🟢 `df = pd.read_csv("fitness_activity.csv")`: read_csv reads the file I uploaded and stores it in a DataFrame called df. A DataFrame is a table with rows and columns, like a spreadsheet.
- 🟢 `df.head()`: head shows the first five rows, to check that the data loaded correctly. I don't need print, because Colab always shows the result of the last line of a cell.

> 🖱️ I'm clicking the Run cell button, the play icon to the left of this cell, to load and show the data.
>
> (Hago clic en el botón Run cell, el ícono de play a la izquierda de esta celda, para cargar y mostrar los datos.)
>
> 🟢 This is a fictional dataset I prepared for this analysis: 200 days of records from one person's fitness tracker. Like most real data, it isn't perfectly clean, so after loading it, the first step will be to inspect it and fix any problems.
>
> (Este es un dataset ficticio que preparé para este análisis: 200 días de registros del reloj de actividad de una persona. Como pasa con casi todos los datos reales, no está perfectamente limpio, así que después de cargarlo, el primer paso va a ser inspeccionarlo y corregir los problemas.)

Señalás cada columna con el mouse, de izquierda a derecha, mientras la nombrás:

> 🟢 Each row is one day, and there are six columns. date is the day of the record, starting on January 1st, 2025. steps is how many steps the tracker counted that day. active_minutes is how many minutes the person was exercising or moving fast.
>
> (Cada fila es un día, y hay seis columnas. date es el día del registro, desde el 1 de enero de 2025. steps es cuántos pasos contó el reloj ese día. active_minutes es cuántos minutos la persona estuvo haciendo ejercicio o moviéndose rápido.)
>
> 🟢 calories is the total energy burned in the day, including the energy the body uses at rest. sleep_hours is how long the person slept. And workout_type is the kind of training that day: Running, Cycling, Strength, Yoga, or Rest, which means no workout.
>
> (calories es la energía total quemada en el día, incluida la que el cuerpo usa en reposo. sleep_hours es cuánto durmió la persona. Y workout_type es el tipo de entrenamiento de ese día: Running, Cycling, Strength, Yoga o Rest, que significa sin entrenamiento.)

---

## 6:30–10:30 — Calidad de los datos y limpieza

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading called Inspect the data.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección llamado Inspect the data.)

Escribís `## 1. Inspect the data`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that checks the data quality.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que revisa la calidad de los datos.)

Escribís la **celda 2**:

```python
df.info()
print(df.isna().sum())
print(df["workout_type"].unique())
df.describe()
```

**What each line does:**

- 🟢 `df.info()`: info lists every column with how many values it has and its data type. info prints by itself, so I don't need print.
- 🟢 `print(df.isna().sum())`: isna marks each empty cell as True, and sum counts them in each column. So this shows the number of missing values per column.
- 🟢 `print(df["workout_type"].unique())`: unique lists every different workout name, so I can see if they're written consistently.
- 🟢 `df.describe()`: describe gives a summary of each number column: count, mean, minimum, maximum, and percentiles. It helps me spot impossible values. Colab shows it because it's the last line.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to check the data.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para revisar los datos.)

Señalás cada problema con el mouse mientras lo nombrás:

> 🟢 I can see three problems. First, info shows 200 rows, but sleep_hours has only 196 values, and the missing-values count confirms it: four days have no sleep data.
>
> (Veo tres problemas. Primero, info muestra 200 filas, pero sleep_hours tiene solo 196 valores, y el conteo de faltantes lo confirma: cuatro días no tienen datos de sueño.)
>
> 🟢 Second, the workout names are inconsistent: running appears in lowercase, Yoga in capitals, and Cycling and strength have extra spaces. There are 9 spellings for only 5 workouts. If I don't fix this, pandas will treat Running and running as two different workouts.
>
> (Segundo, los nombres de los entrenamientos son inconsistentes: running aparece en minúscula, Yoga en mayúsculas, y Cycling y strength tienen espacios de más. Hay 9 formas de escribir solo 5 entrenamientos. Si no lo arreglo, pandas va a tratar Running y running como dos entrenamientos distintos.)
>
> 🟢 And third, describe shows that the minimum of steps is minus one. You can't walk a negative number of steps, so those are sensor errors.
>
> (Y tercero, describe muestra que el mínimo de pasos es menos uno. No se puede caminar una cantidad negativa de pasos, así que son errores del sensor.)
>
> 🟢 Also, the date column is stored as text, not as dates. I'll convert it, so I can get the day of the week.
>
> (Además, la columna date está guardada como texto, no como fechas. La voy a convertir, para poder sacar el día de la semana.)

Según la versión de pandas, el texto aparece como `object` o como `str`.

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for cleaning.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para la limpieza.)

Escribís `## 2. Clean and prepare the data`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that fixes the problems.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que corrige los problemas.)

Escribís la **celda 3**:

```python
df = df[df["steps"] >= 0].copy()
df["sleep_hours"] = df["sleep_hours"].fillna(df["sleep_hours"].median())
df["workout_type"] = df["workout_type"].str.strip().str.title()
df["date"] = pd.to_datetime(df["date"])
df["day"] = df["date"].dt.day_name()
print(df.shape)
print(df["workout_type"].unique())
```

**What each line does:**

- 🟢 `df = df[df["steps"] >= 0].copy()`: this keeps only the days with zero or more steps, which removes the two sensor errors. copy makes a clean new table, so pandas doesn't show a warning when I change it in the next lines.
- 🟢 `df["sleep_hours"] = df["sleep_hours"].fillna(df["sleep_hours"].median())`: fillna fills the four missing sleep values with the median, the middle value. Here I fill instead of removing, because the steps and calories of those days are still valid. I use the median instead of the mean, because it isn't affected by a few very short or very long nights.
- 🟢 `df["workout_type"] = df["workout_type"].str.strip().str.title()`: strip removes the extra spaces, and title writes each name with a capital first letter, so every workout has one spelling.
- 🟢 `df["date"] = pd.to_datetime(df["date"])`: to_datetime converts the dates from text into real dates.
- 🟢 `df["day"] = df["date"].dt.day_name()`: dt gives access to date functions, and day_name creates a new column with the name of the day, like Monday. This only works because I converted the dates in the line above.
- 🟢 `print(df.shape)`: this shows how many rows and columns are left.
- 🟢 `print(df["workout_type"].unique())`: this checks that the workout names are consistent now.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to clean the data.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para limpiar los datos.)
>
> 🟢 Now we have 198 days and 7 columns: the six original ones, plus day. And there are exactly 5 workout types. We removed the two days with negative steps and filled four sleep values.
>
> (Ahora tenemos 198 días y 7 columnas: las seis originales, más day. Y hay exactamente 5 tipos de entrenamiento. Quitamos los dos días con pasos negativos y completamos cuatro valores de sueño.)

---

## 10:30–15:30 — Estadísticas y comparaciones

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for summary statistics.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para las estadísticas.)

Escribís `## 3. Summary statistics`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell with the statistics of the activity measures.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código con las estadísticas de las medidas de actividad.)

Escribís la **celda 4**:

```python
measures = ["steps", "active_minutes", "calories", "sleep_hours"]
df[measures].describe().round(1)
```

**What each line does:**

- 🟢 `measures = [...]`: this saves the four measures in a list, so I don't have to write them again later. I'll reuse it for the correlations.
- 🟢 `df[measures].describe().round(1)`: describe calculates the statistics of those four columns, now with the clean data, and round(1) keeps one decimal.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to see the statistics.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para ver las estadísticas.)

Señalás cada columna de la tabla mientras la nombrás:

> 🟢 An average day has about 7,700 steps, 44 active minutes, almost 2,400 calories, and 7.2 hours of sleep.
>
> (Un día promedio tiene unos 7.700 pasos, 44 minutos activos, casi 2.400 calorías y 7,2 horas de sueño.)
>
> 🟢 Now the minimum of steps is 1,500, so the negative values are gone. Steps vary a lot, from 1,500 to over 18,000, with a standard deviation of about 3,000. Sleep is very stable: the standard deviation is under one hour, and half of the nights are between 6.7 and 7.6 hours.
>
> (Ahora el mínimo de pasos es 1.500, así que los valores negativos desaparecieron. Los pasos varían mucho, de 1.500 a más de 18.000, con una desviación estándar de unos 3.000. El sueño es muy estable: la desviación estándar es de menos de una hora, y la mitad de las noches están entre 6,7 y 7,6 horas.)

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for comparisons.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para las comparaciones.)

Escribís `## 4. Compare activity patterns`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that compares the workout types.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que compara los tipos de entrenamiento.)

Escribís la **celda 5**:

```python
by_workout = df.groupby("workout_type")[["steps", "active_minutes", "calories"]].mean().round(0)
by_workout.sort_values("calories", ascending=False)
```

**What each line does:**

- 🟢 `by_workout = df.groupby("workout_type")[[...]].mean().round(0)`: groupby puts together the days of each workout type, and mean calculates the average steps, active minutes, and calories, rounded to whole numbers. I store it in by_workout, to use it again for a chart.
- 🟢 `by_workout.sort_values("calories", ascending=False)`: this shows the table from the most to the least calories.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to compare the workouts.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para comparar los entrenamientos.)
>
> 🟢 Running days burn the most calories, about 2,636, and rest days the least, about 2,047. Running days also have the most steps, almost 11,700.
>
> (Los días de running son los que más calorías queman, unas 2.636, y los de descanso los que menos, unas 2.047. Los días de running también tienen la mayor cantidad de pasos, casi 11.700.)
>
> 🟢 Interesting detail: cycling has the most active minutes, about 65, but running burns more calories, because it adds many more steps. On a bike, you move a lot without walking.
>
> (Un detalle interesante: cycling tiene la mayor cantidad de minutos activos, unos 65, pero running quema más calorías, porque suma muchos más pasos. En bicicleta te movés mucho sin caminar.)

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that compares the days of the week.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que compara los días de la semana.)

Escribís la **celda 6**:

```python
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
by_day = df.groupby("day")[["steps", "sleep_hours"]].mean().reindex(days).round(1)
by_day
```

**What each line does:**

- 🟢 `days = [...]`: this is the list of days in calendar order. Without it, pandas would sort them alphabetically, starting with Friday.
- 🟢 `by_day = df.groupby("day")[["steps", "sleep_hours"]].mean().reindex(days).round(1)`: groupby puts together the days with the same name, and mean calculates the average steps and sleep for each one. reindex puts the rows in calendar order, using my list.
- 🟢 `by_day`: this shows the table.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to compare the days.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para comparar los días.)
>
> 🖱️ I'm moving the mouse down the steps column, in the table under the cell, to compare the days.
>
> (Muevo el mouse por la columna steps, en la tabla debajo de la celda, para comparar los días.)
>
> 🟢 Saturday is clearly the most active day, with about 11,200 steps, and Sunday the least, with about 5,800. It looks like a long workout on Saturday and rest on Sunday. From Monday to Friday, steps stay between about 6,500 and 8,100.
>
> (El sábado es claramente el día más activo, con unos 11.200 pasos, y el domingo el menos activo, con unos 5.800. Parece un entrenamiento largo el sábado y descanso el domingo. De lunes a viernes, los pasos se mantienen entre unos 6.500 y 8.100.)
>
> 🟢 Sleep is also longer on weekends, about 7.6 hours on Saturday and 7.9 on Sunday, against about 7 hours on weekdays.
>
> (El sueño también es más largo los fines de semana, unas 7,6 horas el sábado y 7,9 el domingo, contra unas 7 horas en los días de semana.)

---

## 15:30–20:00 — Relaciones entre variables y gráficos

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for relationships.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para las relaciones.)

Escribís `## 5. Relationships between variables`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell with the correlation table.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código con la tabla de correlaciones.)

Escribís la **celda 7**:

```python
df[measures].corr().round(2)
```

**What each line does:**

- 🟢 `df[measures].corr().round(2)`: corr calculates the correlation between every pair of the four measures. A correlation is a number between minus one and one. Close to one means they go up together, close to minus one means one goes up when the other goes down, and close to zero means there's no clear relationship.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to see the correlations.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para ver las correlaciones.)
>
> 🟢 The diagonal is always one, because each measure is perfectly related to itself. So I read the other cells.
>
> (La diagonal siempre es uno, porque cada medida está perfectamente relacionada consigo misma. Así que leo las otras celdas.)
>
> 🟢 Active minutes and calories have a very strong relationship, 0.91. Steps and calories are also strong, 0.83. Steps and active minutes are moderate, 0.63: cycling and strength add active minutes without many steps.
>
> (Los minutos activos y las calorías tienen una relación muy fuerte, 0,91. Los pasos y las calorías también, 0,83. Los pasos y los minutos activos tienen una relación moderada, 0,63: cycling y strength suman minutos activos sin muchos pasos.)
>
> 🟢 But sleep is close to zero with everything, about minus 0.05, so in this data, more activity doesn't mean more or less sleep.
>
> (Pero el sueño está cerca de cero con todo, unos menos 0,05, así que en estos datos más actividad no significa más ni menos sueño.)

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for the charts.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para los gráficos.)

Escribís `## 6. Visualizations`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell for a bar chart of steps by day.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código para un gráfico de barras de pasos por día.)

Escribís la **celda 8**:

```python
by_day["steps"].plot(kind="bar", title="Average Steps by Day of the Week", xlabel="Day", ylabel="Steps", rot=45)
plt.show()
```

**What each line does:**

- 🟢 `by_day["steps"].plot(kind="bar", ...)`: this draws a bar chart with the average steps of each day, using the table I made before. title, xlabel, and ylabel set the chart title and the names of both axes. rot equals 45 tilts the day names so they don't overlap.
- 🟢 `plt.show()`: this displays the chart below the cell.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to draw the chart.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para dibujar el gráfico.)
>
> 🟢 The Saturday bar stands out, almost twice as tall as Sunday, which is the lowest. The weekdays are in between. A bar chart is the right choice here, because I'm comparing separate groups.
>
> (La barra del sábado se destaca, casi el doble de alta que la del domingo, que es la más baja. Los días de semana están en el medio. Un gráfico de barras es la opción correcta acá, porque estoy comparando grupos separados.)

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell for a scatter plot.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código para un gráfico de dispersión.)

Escribís la **celda 9**:

```python
df.plot(kind="scatter", x="active_minutes", y="calories", title="Active Minutes vs Calories")
plt.show()
```

**What each line does:**

- 🟢 `df.plot(kind="scatter", x="active_minutes", y="calories", ...)`: a scatter plot draws one dot per day, with the active minutes on the horizontal axis and the calories on the vertical axis. It shows if two variables move together. pandas uses the column names as the axis labels.
- 🟢 `plt.show()`: this displays the chart.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to draw the scatter plot.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para dibujar el gráfico de dispersión.)
>
> 🟢 The dots form a clear rising line, from the bottom left to the top right: that's the 0.91 correlation. Each extra active minute adds calories in a very predictable way.
>
> (Los puntos forman una línea ascendente clara, de abajo a la izquierda hacia arriba a la derecha: esa es la correlación de 0,91. Cada minuto activo extra suma calorías de una forma muy predecible.)

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell for a chart of calories by workout.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código para un gráfico de calorías por entrenamiento.)

Escribís la **celda 10**:

```python
by_workout["calories"].sort_values().plot(kind="barh", title="Average Calories by Workout Type")
plt.xlabel("Calories")
plt.show()
```

**What each line does:**

- 🟢 `by_workout["calories"].sort_values().plot(kind="barh", ...)`: I take the calories column from the workout table, sort it, and draw a horizontal bar chart. barh means horizontal bars, and sorting from low to high puts the highest bar at the top.
- 🟢 `plt.xlabel("Calories")`: this names the horizontal axis.
- 🟢 `plt.show()`: this displays the chart.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to draw the chart.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para dibujar el gráfico.)
>
> 🟢 Running is at the top and Rest at the bottom. Even on rest days, the body burns about 2,000 calories, which is the base energy we use just to live. So the difference between a rest day and a running day is about 600 calories.
>
> (Running está arriba y Rest abajo. Incluso en los días de descanso el cuerpo quema unas 2.000 calorías, que es la energía base que usamos solo para vivir. Así que la diferencia entre un día de descanso y uno de running es de unas 600 calorías.)

---

## 20:00–21:30 — Conclusiones

**Valores de referencia** (los calculé directamente del CSV). Compará con tu resultado antes de decirlos:

| Paso | Resultado esperado |
| ---- | ------------------ |
| Inspección | 200 filas; `sleep_hours` con 196 valores; mínimo de `steps` −1; 9 tipos de entrenamiento |
| Limpieza | `(198, 7)`; mediana de sueño usada para completar: 7,15; 5 tipos: Running, Strength, Cycling, Rest, Yoga |
| Resumen | Pasos: promedio 7.703, mediana 7.240, desviación ~2.972, mín. 1.500, máx. 18.157 · Minutos activos: promedio 44,1 · Calorías: promedio 2.388 · Sueño: promedio 7,2 h, desviación 0,8, percentiles 25–75: 6,7–7,6 |
| Por entrenamiento (pasos / minutos / calorías) | Running 11.679 / 57 / 2.636 · Cycling 8.098 / 65 / 2.562 · Strength 7.401 / 43 / 2.371 · Yoga 6.540 / 40 / 2.314 · Rest 4.593 / 15 / 2.047 |
| Por día (pasos) | Lunes 8.082 · Martes 7.028 · Miércoles 7.275 · Jueves 8.042 · Viernes 6.533 · **Sábado 11.198** · **Domingo 5.793** |
| Sueño por día | Sábado 7,6 h y domingo 7,9 h; de lunes a viernes, entre 6,8 y 7,1 h |
| Correlaciones | Minutos activos y calorías **0,91** · Pasos y calorías **0,83** · Pasos y minutos activos **0,63** · Sueño con todo lo demás entre **−0,04 y −0,05** |
| Dato extra (no sale en pantalla) | De los 28 sábados, 14 son de cycling y 11 de running, y ninguno es de descanso. De los 28 domingos, 12 son de descanso |

> 🖱️ I'm clicking the plus Text button in the toolbar, to add the conclusions at the end of the notebook.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar las conclusiones al final del notebook.)

Mientras escribís, decí en voz alta lo que vas escribiendo:

```markdown
## 7. Conclusions
- **Data quality:** 200 rows became 198 days. We removed 2 days with negative steps (a sensor error), filled 4 missing sleep values with the median (7.15 hours), and fixed 9 workout spellings down to 5 types.
- **Summary:** an average day has about 7,700 steps, 44 active minutes, 2,390 calories, and 7.2 hours of sleep.
- **Weekly pattern:** Saturday is the most active day (about 11,200 steps) and Sunday the least active (about 5,800). Sleep is longer on weekends (about 7.6 to 7.9 hours).
- **Workouts:** running days burn the most calories (about 2,636) and rest days the least (about 2,047). Cycling has the most active minutes, but running has many more steps.
- **Relationships:** active minutes and calories are strongly related (0.91), and so are steps and calories (0.83). Sleep has almost no relationship with activity (about -0.05).
```

> 🟢 To sum up: this person is most active on Saturdays and rests on Sundays, running burns the most calories, and active minutes are the best sign of how many calories a day burns.
>
> (Para resumir: esta persona es más activa los sábados y descansa los domingos, running es lo que más calorías quema, y los minutos activos son el mejor indicador de cuántas calorías se queman en un día.)

---

## 21:30–26:00 — Epílogo (4–5 minutos)

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
> 🟢 Let me summarize the whole analysis. We started with the title and the goal: check the data quality, calculate statistics, compare patterns, look at relationships, and visualize the results.
>
> (Les resumo todo el análisis. Empezamos con el título y el objetivo: revisar la calidad de los datos, calcular estadísticas, comparar patrones, ver relaciones y visualizar los resultados.)
>
> 🟢 In the first cell, we imported pandas for the table and Matplotlib for the charts, and loaded the CSV: one row per day, with six columns.
>
> (En la primera celda importamos pandas para la tabla y Matplotlib para los gráficos, y cargamos el CSV: una fila por día, con seis columnas.)
>
> 🖱️ I'm scrolling down to section 1, Inspect the data, to show what we found.
>
> (Bajo hasta la sección 1, Inspect the data, para mostrar lo que encontramos.)
>
> 🟢 In section 1, we inspected the data before calculating anything, and we found three problems: four days with no sleep data, 9 spellings for only 5 workouts, and negative steps.
>
> (En la sección 1 inspeccionamos los datos antes de calcular nada, y encontramos tres problemas: cuatro días sin datos de sueño, 9 formas de escribir solo 5 entrenamientos y pasos negativos.)
>
> 🖱️ I'm scrolling down to section 2, Clean and prepare the data.
>
> (Bajo hasta la sección 2, Clean and prepare the data.)
>
> 🟢 In section 2, we fixed those problems, one line each. We also converted the dates and added the day of the week. We went from 200 rows to 198 clean days.
>
> (En la sección 2 arreglamos esos problemas, con una línea para cada uno. También convertimos las fechas y agregamos el día de la semana. Pasamos de 200 filas a 198 días limpios.)
>
> 🖱️ I'm scrolling down to sections 3 and 4, Summary statistics and Compare activity patterns.
>
> (Bajo hasta las secciones 3 y 4, Summary statistics y Compare activity patterns.)
>
> 🟢 In section 3, we described an average day: about 7,700 steps, 44 active minutes, 2,400 calories, and 7.2 hours of sleep. In section 4, we compared workouts and days: running burns the most, and Saturday is the most active day.
>
> (En la sección 3 describimos un día promedio: unos 7.700 pasos, 44 minutos activos, 2.400 calorías y 7,2 horas de sueño. En la sección 4 comparamos los entrenamientos y los días: running es lo que más quema, y el sábado es el día más activo.)
>
> 🖱️ I'm scrolling down to sections 5 and 6, Relationships and Visualizations.
>
> (Bajo hasta las secciones 5 y 6, Relationships y Visualizations.)
>
> 🟢 In section 5, the correlations showed that active minutes and calories go together, 0.91, while sleep isn't related to activity. In section 6, the three charts showed the same results visually: the Saturday peak, the rising line of minutes and calories, and the ranking of workouts.
>
> (En la sección 5, las correlaciones mostraron que los minutos activos y las calorías van juntos, 0,91, mientras que el sueño no se relaciona con la actividad. En la sección 6, los tres gráficos mostraron los mismos resultados de forma visual: el pico del sábado, la línea ascendente de minutos y calorías, y el ranking de entrenamientos.)
>
> 🖱️ I'm scrolling down to section 7, Conclusions, at the end of the notebook.
>
> (Bajo hasta la sección 7, Conclusions, al final del notebook.)
>
> 🟢 And finally, we wrote down the conclusions with the real numbers, so anyone who opens the notebook can read the results without running the code.
>
> (Y por último, anotamos las conclusiones con los números reales, así cualquiera que abra el notebook puede leer los resultados sin ejecutar el código.)

### Decisiones y próximos pasos

> 🖱️ I'm scrolling slowly up through the notebook with the mouse wheel, to go over the decisions I made.
>
> (Subo despacio por el notebook con la rueda del mouse, para repasar las decisiones que tomé.)
>
> 🟢 In this epilogue, I want to go over my approach. I treated each data problem differently. The negative steps were impossible, so I removed those days. The missing sleep values were only four, and the rest of those days was valid, so I filled them with the median instead of losing the whole day.
>
> (En este epílogo quiero repasar mi enfoque. Traté cada problema de los datos de forma distinta. Los pasos negativos eran imposibles, así que quité esos días. Los valores de sueño faltantes eran solo cuatro, y el resto de esos días era válido, así que los completé con la mediana en vez de perder el día entero.)
>
> 🟢 I compared the data in two ways, by workout and by day of the week, because each one answers a different question: what kind of training burns the most, and when this person is most active. Then the correlations showed which measures move together.
>
> (Comparé los datos de dos formas, por entrenamiento y por día de la semana, porque cada una responde una pregunta distinta: qué tipo de entrenamiento quema más y cuándo esta persona es más activa. Después las correlaciones mostraron qué medidas se mueven juntas.)
>
> 🟢 For each question, I chose a chart that fits it: bars to compare days and workouts, and a scatter plot to show the relationship between two measures.
>
> (Para cada pregunta elegí un gráfico que le corresponde: barras para comparar días y entrenamientos, y un gráfico de dispersión para mostrar la relación entre dos medidas.)
>
> 🟢 This analysis has limits. The data is fictional and comes from one person. A correlation doesn't prove a cause, and calories from a fitness tracker are an estimate, often calculated from the steps and active minutes themselves, which partly explains the strong correlations.
>
> (Este análisis tiene límites. Los datos son ficticios y son de una sola persona. Una correlación no prueba una causa, y las calorías de un reloj de actividad son una estimación, muchas veces calculada a partir de los mismos pasos y minutos activos, lo que explica en parte las correlaciones fuertes.)
>
> 🟢 As next steps, I could look at trends over the months, compare the day after a hard workout with the day after rest, or add heart rate data. For this person, a simple idea stands out: Sunday and Friday are the least active days, so a short walk on those days would balance the week. Thanks for watching!
>
> (Como próximos pasos, podría ver las tendencias a lo largo de los meses, comparar el día después de un entrenamiento fuerte con el día después de descansar o sumar datos de frecuencia cardíaca. Para esta persona se destaca una idea simple: el domingo y el viernes son los días menos activos, así que una caminata corta esos días equilibraría la semana. ¡Gracias por mirar!)

Si el reloj todavía no pasó los 15:00, no cortes: recorré la tabla de correlaciones par por par y explicá cada número.

---

## Después de grabar

1. Ejecutá **Run full AutoQC**, no solo *Rerun failing*.
2. Subí los **cuatro archivos por separado**: el **MP4**, el **ZIP original de TaskRecorder**, **Deliverables.zip** (con el `.ipynb` descargado y, si lo piden, el CSV) y **Metadata.rtf**.
