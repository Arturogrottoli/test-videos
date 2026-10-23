# 6bbsb278 — Fitness Activity Analysis

Guion paso a paso para grabar la tarea **6bbsb278**: analizar 200 registros diarios de actividad física en **Google Colab** con **Python** y **pandas**. El trabajo incluye revisar la calidad de los datos, calcular estadísticas, comparar patrones por tipo de entrenamiento y por día de la semana, ver qué variables se relacionan y visualizar los resultados. La grabación tiene que durar **entre 15:00 y 50:59**. Este guion apunta a unos **22 minutos**, epílogo incluido.

**Cómo leer este guion:**

- Las frases que empiezan con 🖱️ las decís **en el momento de hacer clic, desplazarte o escribir**. Siempre dicen **qué** elemento usás, **dónde** está en la pantalla y **por qué** lo usás. Son las que revisa AutoQC.
- Las frases que empiezan con 🟢 son la explicación que **decís en inglés** entre una acción y otra.
- Debajo de cada bloque de código, la lista **What each line does** explica cada línea en inglés. La leés en voz alta mientras escribís esa línea.
- El resto, en castellano, es lo que hacés en pantalla. Las traducciones aparecen entre paréntesis después de cada frase.

> **Importante:** el Goal de Studio tiene prioridad sobre este guion. Antes de grabar, revisá el apartado **Starting materials**: si Studio trae su propio CSV, usá ese y adaptá los nombres de las columnas. Si no trae nada, usá `fitness_activity.csv` de esta carpeta. El Goal no dice qué herramienta usar: este guion usa Google Colab.

---

## Archivos de la carpeta

```
6bbsb278-fitness-activity-analysis/
├── GUION-V2.md                        ← este guion (versión nueva)
├── README.md                        ← guion anterior (sesión previa)
├── fitness_activity.csv             ← dataset de partida: 200 días, con errores para limpiar
└── fitness_activity_analysis.ipynb  ← notebook de referencia, completo y en orden
```

---

## El dataset

`fitness_activity.csv` tiene 200 días **ficticios**, del 1/1/2025 al 19/7/2025, con 6 columnas:

| Columna | Qué contiene |
| ------- | ------------ |
| `date` | Fecha |
| `steps` | Pasos del día |
| `active_minutes` | Minutos de actividad |
| `calories` | Calorías quemadas |
| `sleep_hours` | Horas de sueño |
| `workout_type` | Running, Cycling, Strength, Yoga o Rest |

**Errores puestos a propósito:** 2 días con pasos negativos (`-1`, un error del sensor), 4 días sin horas de sueño y 9 formas de escribir los 5 tipos de entrenamiento (`running`, `YOGA`, `Cycling ` con un espacio al final, etc.).

**Valores de referencia** (calculados del CSV):

| Paso | Resultado esperado |
| ---- | ------------------ |
| Inspección | 200 filas; `sleep_hours` con 196 valores; mínimo de `steps` −1; 9 tipos de entrenamiento |
| Limpieza | `(198, 7)`; mediana de sueño usada para completar: 7,15; 5 tipos |
| Resumen | Pasos: promedio ~7.703, mediana 7.240, mín. 1.500, máx. 18.157 · Minutos activos: promedio ~44 · Calorías: promedio ~2.388 · Sueño: promedio ~7,2 h |
| Por entrenamiento (pasos / minutos / calorías) | Running 11.679 / 57 / 2.636 · Cycling 8.098 / 65 / 2.562 · Strength 7.401 / 43 / 2.371 · Yoga 6.540 / 40 / 2.314 · Rest 4.593 / 15 / 2.047 |
| Por día (pasos) | Lunes ~8.082 · Martes ~7.028 · Miércoles ~7.275 · Jueves ~8.042 · Viernes ~6.533 · **Sábado ~11.198** · **Domingo ~5.793** |
| Sueño por día | Sábado ~7,6 h y domingo ~7,9 h; de lunes a viernes, entre ~6,8 y ~7,1 h |
| Correlaciones | Minutos activos y calorías **0,91** · Pasos y calorías **0,83** · Pasos y minutos activos **0,63** · Sueño con todo lo demás ~**−0,05** |

---

## Antes de grabar

1. Leé el Goal y compará este guion con el campo **Describe your idea** de Studio.
2. Practicá una vez entera en un notebook nuevo, leyendo en voz alta las frases 🖱️ y 🟢, y cronometrá.
3. Dejá dos pestañas abiertas en Firefox: el documento **Goal** y Colab (https://colab.research.google.com). Tené `fitness_activity.csv` en una carpeta fácil de encontrar. Agrandá el zoom (`Ctrl + +`).
4. Maximizá el navegador y cerrá o minimizá las demás ventanas, para que ninguna tape a otra.
5. Pausa de ~1 segundo después de cada clic y nunca más de 45 segundos en silencio.
6. No muestres Studio, Mercor, información privada ni herramientas de IA. Cerrá este guion si está en la misma pantalla.

---

## 0:00–0:45 — Mostrar el Goal

> 🖱️ I'm on the Goal document in the first browser tab, to show what this task asks for.
>
> (Estoy en el documento del Goal, en la primera pestaña del navegador, para mostrar qué pide esta tarea.)
>
> 🟢 As a data analyst, I'll analyze 200 days of fitness records with Python and pandas. I'll check the data quality, calculate summary statistics, compare activity patterns, look at relationships between variables, and visualize the results.
>
> (Como analista de datos, voy a analizar 200 días de registros de actividad física con Python y pandas. Voy a revisar la calidad de los datos, calcular estadísticas, comparar patrones de actividad, ver las relaciones entre variables y visualizar los resultados.)

---

## 0:45–4:00 — Colab y cargar los datos

> 🖱️ I'm clicking the second browser tab, at the top of the window, to open Google Colab.
>
> (Hago clic en la segunda pestaña del navegador, arriba de la ventana, para abrir Google Colab.)
>
> 🟢 Google Colab runs Python notebooks in the browser. pandas, for tables, and Matplotlib, for charts, are already installed.
>
> (Google Colab ejecuta notebooks de Python en el navegador. pandas, para tablas, y Matplotlib, para gráficos, ya vienen instalados.)
>
> 🖱️ I'm clicking the New notebook button at the bottom of the Open notebook dialog, to create a fresh notebook.
>
> (Hago clic en el botón New notebook, abajo del cuadro Open notebook, para crear un notebook nuevo.)
>
> 🖱️ I'm clicking the notebook title field at the top left, and typing fitness_activity_analysis.ipynb, to identify this analysis.
>
> (Hago clic en el campo del título del notebook, arriba a la izquierda, y escribo fitness_activity_analysis.ipynb, para identificar este análisis.)
>
> 🖱️ I'm clicking the Files icon, the folder in the left sidebar, and then the Upload to session storage icon at the top of the Files pane, and choosing fitness_activity.csv, so the notebook can read it.
>
> (Hago clic en el ícono Files, la carpeta de la barra lateral izquierda, y después en el ícono Upload to session storage, arriba del panel Files, y elijo fitness_activity.csv, para que el notebook pueda leerlo.)

Si aparece un aviso: *"I'm clicking OK on this warning, in the center of the screen, to continue the upload."*

> 🖱️ I'm clicking the plus Text button in the toolbar at the top left, to add a title and the goal.
>
> (Hago clic en el botón + Text de la barra de herramientas, arriba a la izquierda, para agregar un título y el objetivo.)

```markdown
# Fitness Activity Analysis
Dataset: 200 days of fitness records. Goal: check data quality, calculate summary statistics, compare activity patterns, examine relationships between variables, and visualize the results.
```

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that loads the libraries and the data.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que carga las librerías y los datos.)

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("fitness_activity.csv")
df.head()
```

**What each line does:**

- 🟢 `import pandas as pd`: this loads pandas, the library for tables of data.
- 🟢 `import matplotlib.pyplot as plt`: this loads pyplot, the part of Matplotlib that draws charts.
- 🟢 `df = pd.read_csv("fitness_activity.csv")`: this reads the uploaded file into a DataFrame called df.
- 🟢 `df.head()`: this shows the first five days.

> 🖱️ I'm clicking the Run cell button, the play icon to the left of this cell, to load the data.
>
> (Hago clic en el botón Run cell, el ícono de play a la izquierda de esta celda, para cargar los datos.)
>
> 🟢 Each row is one day: the date, the steps, the active minutes, the calories burned, the hours of sleep, and the type of workout.
>
> (Cada fila es un día: la fecha, los pasos, los minutos activos, las calorías quemadas, las horas de sueño y el tipo de entrenamiento.)

---

## 4:00–8:30 — Calidad de los datos y limpieza

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading called Inspect the data.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección llamado Inspect the data.)

Escribís `## 1. Inspect the data`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that checks the data quality.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que revisa la calidad de los datos.)

```python
df.info()
print(df.isna().sum())
print(df["workout_type"].unique())
df.describe()
```

**What each line does:**

- 🟢 `df.info()`: each column with its number of values and its data type.
- 🟢 `print(df.isna().sum())`: the number of missing values in each column.
- 🟢 `print(df["workout_type"].unique())`: every different workout name, to check they're consistent.
- 🟢 `df.describe()`: the count, mean, minimum, maximum, and percentiles of each number column. It helps spot impossible values.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to check the data.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para revisar los datos.)
>
> 🟢 I see three problems. First, sleep_hours has four missing values. Second, the workout names are inconsistent: running appears in lowercase, Yoga in capitals, and some have extra spaces. There are 9 spellings for 5 workouts.
>
> (Veo tres problemas. Primero, sleep_hours tiene cuatro valores faltantes. Segundo, los nombres de los entrenamientos son inconsistentes: running aparece en minúscula, Yoga en mayúsculas y algunos tienen espacios de más. Hay 9 formas de escribir 5 entrenamientos.)
>
> 🟢 And third, describe shows that the minimum of steps is minus one. You can't walk a negative number of steps, so those are sensor errors.
>
> (Y tercero, describe muestra que el mínimo de pasos es menos uno. No se puede caminar una cantidad negativa de pasos, así que son errores del sensor.)

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for cleaning.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para la limpieza.)

Escribís `## 2. Clean and prepare the data`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that fixes the problems.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que corrige los problemas.)

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

- 🟢 `df = df[df["steps"] >= 0].copy()`: this keeps only the days with zero or more steps, which removes the two sensor errors. copy makes a clean new table, so pandas doesn't warn when I change it.
- 🟢 `df["sleep_hours"] = df["sleep_hours"].fillna(df["sleep_hours"].median())`: fillna fills the four missing sleep values with the median. Here I fill instead of removing, because the steps and calories of those days are still useful.
- 🟢 `df["workout_type"] = df["workout_type"].str.strip().str.title()`: strip removes the extra spaces, and title gives every name a capital first letter.
- 🟢 `df["date"] = pd.to_datetime(df["date"])`: this converts the dates from text into real dates.
- 🟢 `df["day"] = df["date"].dt.day_name()`: a new column with the name of the day, like Monday, to compare the days of the week.
- 🟢 `print(df.shape)` and `print(df["workout_type"].unique())`: this checks the result.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to clean the data.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para limpiar los datos.)
>
> 🟢 Now we have 198 days and 7 columns, with 5 clean workout types.
>
> (Ahora tenemos 198 días y 7 columnas, con 5 tipos de entrenamiento limpios.)

---

## 8:30–13:00 — Estadísticas y comparaciones

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for summary statistics.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para las estadísticas.)

Escribís `## 3. Summary statistics`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell with the statistics of the activity measures.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código con las estadísticas de las medidas de actividad.)

```python
measures = ["steps", "active_minutes", "calories", "sleep_hours"]
df[measures].describe().round(1)
```

**What each line does:**

- 🟢 `measures = [...]`: a list with the four measures, so I don't have to write them again later.
- 🟢 `df[measures].describe().round(1)`: the statistics of those four columns, with one decimal.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to see the statistics.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para ver las estadísticas.)
>
> 🟢 An average day has about 7,700 steps, 44 active minutes, almost 2,400 calories, and 7.2 hours of sleep. Steps vary a lot, from 1,500 to over 18,000, while sleep is very stable, with a standard deviation under one hour.
>
> (Un día promedio tiene unos 7.700 pasos, 44 minutos activos, casi 2.400 calorías y 7,2 horas de sueño. Los pasos varían mucho, de 1.500 a más de 18.000, mientras que el sueño es muy estable, con una desviación estándar de menos de una hora.)

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for comparisons.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para las comparaciones.)

Escribís `## 4. Compare activity patterns`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that compares the workout types.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que compara los tipos de entrenamiento.)

```python
by_workout = df.groupby("workout_type")[["steps", "active_minutes", "calories"]].mean().round(0)
by_workout.sort_values("calories", ascending=False)
```

**What each line does:**

- 🟢 `by_workout = df.groupby("workout_type")[[...]].mean().round(0)`: groupby puts together the days of each workout type, and mean calculates the average steps, active minutes, and calories, rounded to whole numbers.
- 🟢 `by_workout.sort_values("calories", ascending=False)`: this shows the table from the most to the least calories.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to compare the workouts.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para comparar los entrenamientos.)
>
> 🟢 Running days burn the most calories, about 2,636, and rest days the least, about 2,047. Interesting detail: cycling has the most active minutes, about 65, but running burns more calories, because it adds many more steps.
>
> (Los días de running son los que más calorías queman, unas 2.636, y los de descanso los que menos, unas 2.047. Un detalle interesante: cycling tiene la mayor cantidad de minutos activos, unos 65, pero running quema más calorías, porque suma muchos más pasos.)
>
> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that compares the days of the week.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que compara los días de la semana.)

```python
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
by_day = df.groupby("day")[["steps", "sleep_hours"]].mean().reindex(days).round(1)
by_day
```

**What each line does:**

- 🟢 `days = [...]`: the days in calendar order. Without this, pandas would sort them alphabetically, starting with Friday.
- 🟢 `by_day = df.groupby("day")[["steps", "sleep_hours"]].mean().reindex(days).round(1)`: the average steps and sleep for each day of the week. reindex puts the rows in calendar order.
- 🟢 `by_day`: this shows the table.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to compare the days.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para comparar los días.)
>
> 🟢 Saturday is clearly the most active day, with about 11,200 steps, and Sunday the least, with about 5,800. It looks like a long workout on Saturday and rest on Sunday. Sleep is also longer on weekends, about 7.6 to 7.9 hours, against about 7 hours on weekdays.
>
> (El sábado es claramente el día más activo, con unos 11.200 pasos, y el domingo el menos activo, con unos 5.800. Parece un entrenamiento largo el sábado y descanso el domingo. El sueño también es más largo los fines de semana, de unas 7,6 a 7,9 horas, contra unas 7 horas en los días de semana.)

---

## 13:00–17:30 — Relaciones entre variables y gráficos

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for relationships.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para las relaciones.)

Escribís `## 5. Relationships between variables`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell with the correlation table.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código con la tabla de correlaciones.)

```python
df[measures].corr().round(2)
```

**What each line does:**

- 🟢 `df[measures].corr().round(2)`: corr calculates the correlation between every pair of measures. It goes from minus one to one. Close to one means they go up together, close to zero means no relationship.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to see the correlations.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para ver las correlaciones.)
>
> 🟢 Active minutes and calories have a very strong relationship, 0.91. Steps and calories are also strong, 0.83. But sleep is close to zero with everything, about minus 0.05, so in this data, more activity doesn't mean more or less sleep.
>
> (Los minutos activos y las calorías tienen una relación muy fuerte, 0,91. Los pasos y las calorías también, 0,83. Pero el sueño está cerca de cero con todo, unos menos 0,05, así que en estos datos más actividad no significa más ni menos sueño.)

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for the charts.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para los gráficos.)

Escribís `## 6. Visualizations`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell for a bar chart of steps by day.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código para un gráfico de barras de pasos por día.)

```python
by_day["steps"].plot(kind="bar", title="Average Steps by Day of the Week", xlabel="Day", ylabel="Steps", rot=45)
plt.show()
```

**What each line does:**

- 🟢 `by_day["steps"].plot(kind="bar", ...)`: a bar chart with the average steps of each day, with a title and both axis names. rot=45 tilts the day names so they don't overlap.
- 🟢 `plt.show()`: this displays the chart.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to draw the chart.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para dibujar el gráfico.)
>
> 🟢 The Saturday bar stands out, and Sunday is the lowest. The weekdays are in between.
>
> (La barra del sábado se destaca, y el domingo es la más baja. Los días de semana están en el medio.)
>
> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell for a scatter plot.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código para un gráfico de dispersión.)

```python
df.plot(kind="scatter", x="active_minutes", y="calories", title="Active Minutes vs Calories")
plt.show()
```

**What each line does:**

- 🟢 `df.plot(kind="scatter", x="active_minutes", y="calories", ...)`: a scatter plot with one dot per day: active minutes on the horizontal axis and calories on the vertical axis. pandas uses the column names as axis labels.
- 🟢 `plt.show()`: this displays the chart.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to draw the scatter plot.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para dibujar el gráfico de dispersión.)
>
> 🟢 The dots form a clear rising line: that's the 0.91 correlation. Each extra active minute adds calories in a very predictable way.
>
> (Los puntos forman una línea ascendente clara: esa es la correlación de 0,91. Cada minuto activo extra suma calorías de una forma muy predecible.)
>
> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell for a chart of calories by workout.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código para un gráfico de calorías por entrenamiento.)

```python
by_workout["calories"].sort_values().plot(kind="barh", title="Average Calories by Workout Type")
plt.xlabel("Calories")
plt.show()
```

**What each line does:**

- 🟢 `by_workout["calories"].sort_values().plot(kind="barh", ...)`: a horizontal bar chart with the average calories of each workout, sorted so the highest is at the top.
- 🟢 `plt.xlabel("Calories")`: this names the horizontal axis.
- 🟢 `plt.show()`: this displays the chart.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to draw the chart.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para dibujar el gráfico.)
>
> 🟢 Running is at the top and Rest at the bottom. Even on rest days, the body burns about 2,000 calories, which is the base energy we use just to live.
>
> (Running está arriba y Rest abajo. Incluso en los días de descanso el cuerpo quema unas 2.000 calorías, que es la energía base que usamos solo para vivir.)

---

## 17:30–19:00 — Conclusiones

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

---

## 19:00–22:30 — Epílogo (3–4 minutos)

Revisá en las reglas de Odin qué tiene que tener el epílogo y ajustá este texto si piden algo distinto.

> 🖱️ I'm opening the File menu at the top left of Colab and choosing Download, then Download .ipynb, to save the finished notebook for the deliverables.
>
> (Abro el menú File, arriba a la izquierda de Colab, y elijo Download y después Download .ipynb, para guardar el notebook terminado para los entregables.)
>
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
