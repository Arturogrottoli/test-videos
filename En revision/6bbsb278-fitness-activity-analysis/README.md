# 6bbsb278 — Fitness Activity Analysis

Guion paso a paso para grabar la tarea **6bbsb278**: analizar 200 registros diarios ficticios de actividad física en **Google Colab**, con **Python**, **pandas** y **Matplotlib**. El trabajo incluye revisar la calidad de los datos, calcular estadísticas, comparar patrones por tipo de entrenamiento y por día de la semana, ver qué variables se relacionan y visualizar los resultados. La grabación tiene que durar **entre 15:00 y 50:59**. Este guion apunta a unos **28 minutos**, epílogo incluido.

**Cómo leer este guion:**

- Las frases que empiezan con 🖱️ las decís **en el momento de hacer clic, desplazarte o escribir**. Siempre dicen **qué** elemento usás, **dónde** está en la pantalla y **por qué** lo usás. Son las que revisa AutoQC.
- Las frases que empiezan con 🟢 son la explicación que **decís en inglés** entre una acción y otra.
- Debajo de cada bloque de código, la lista **What each line does** explica **cada renglón por separado**, en inglés. Leés la explicación de un renglón **mientras lo escribís**, y recién después pasás al siguiente. Así nunca estás escribiendo en silencio.
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

Para probar el notebook de referencia: en https://colab.research.google.com elegís **File → Upload notebook**, hacés clic en **Browse** (no lo arrastres desde VS Code) y seleccionás `fitness_activity_analysis.ipynb`. Después subís `fitness_activity.csv` desde el panel **Files** y ejecutás **Runtime → Run all**.

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
4. Dejá **cuatro pestañas** abiertas en Firefox, en este orden:
   1. el documento del **Goal**;
   2. Colab (https://colab.research.google.com), con el cuadro **Open notebook** a la vista, sin crear todavía el notebook;
   3. el sitio oficial de pandas (https://pandas.pydata.org);
   4. el sitio oficial de Matplotlib (https://matplotlib.org).

   Tené `fitness_activity.csv` en una carpeta fácil de encontrar, como el Escritorio. Agrandá el zoom del navegador (`Ctrl + +`).
5. Maximizá el navegador y cerrá o minimizá las demás ventanas, para que ninguna tape a otra.
6. Pausa de ~1 segundo después de cada clic y nunca más de 45 segundos en silencio.
7. Escribí el código **un renglón por vez**, a tu ritmo normal (no más lento a propósito: el tiempo tipeando cuenta para el **porcentaje de escritura**, que tiene que quedar por debajo de ~30%). Decí la explicación de ese renglón mientras lo escribís, y si terminás de escribir antes, terminá la frase antes de pasar al siguiente renglón. Ejecutá las celdas siempre con el **botón Run** (mouse), no con el teclado.
8. No muestres Studio, Mercor, información privada ni herramientas de IA. Si Colab muestra funciones de IA (Gemini) o te sugiere código mientras escribís, ignorá la sugerencia y seguí escribiendo vos. Cerrá este guion si está en la misma pantalla.

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

## 1:30–3:30 — Colab, pandas y Matplotlib

> 🖱️ I'm clicking the second browser tab, at the top of the window, to open Google Colab.
>
> (Hago clic en la segunda pestaña del navegador, arriba de la ventana, para abrir Google Colab.)
>
> 🟢 Google Colab is a free tool from Google that runs Python notebooks in the browser. A notebook mixes text cells, for explanations, and code cells, that I can run one at a time and see the result right below. The code runs on a computer in Google's cloud, so there's nothing to install on my machine.
>
> (Google Colab es una herramienta gratuita de Google que ejecuta notebooks de Python en el navegador. Un notebook mezcla celdas de texto, para las explicaciones, y celdas de código, que puedo ejecutar de a una y ver el resultado justo abajo. El código se ejecuta en una computadora en la nube de Google, así que no hay que instalar nada en mi máquina.)
>
> 🟢 For this analysis I'll use two libraries. Neither of them is part of Python itself: they're external, open source libraries. I'll show where each one comes from.
>
> (Para este análisis voy a usar dos librerías. Ninguna de las dos es parte de Python: son librerías externas, de código abierto. Les muestro de dónde sale cada una.)
>
> 🖱️ I'm clicking the third browser tab, at the top of the window, to show the official pandas website.
>
> (Hago clic en la tercera pestaña del navegador, arriba de la ventana, para mostrar el sitio oficial de pandas.)
>
> 🟢 This is pandas, at pandas.pydata.org. pandas is a free, open source Python library for working with tables of data, like a spreadsheet inside Python. Its main object is the DataFrame, a table with rows and columns. I'll use it to load the records, clean them, group them, and calculate the statistics and correlations.
>
> (Esto es pandas, en pandas.pydata.org. pandas es una librería de Python gratuita y de código abierto para trabajar con tablas de datos, como una hoja de cálculo dentro de Python. Su objeto principal es el DataFrame, una tabla con filas y columnas. La voy a usar para cargar los registros, limpiarlos, agruparlos y calcular las estadísticas y las correlaciones.)
>
> 🖱️ I'm scrolling down the pandas homepage, in the center of the window, with the mouse wheel, to show what the project offers.
>
> (Bajo por la página principal de pandas, en el centro de la ventana, con la rueda del mouse, para mostrar lo que ofrece el proyecto.)
>
> 🟢 On a normal computer, you install pandas first, with the command pip install pandas. pip is Python's package installer, and it downloads libraries from the Python Package Index, called PyPI.
>
> (En una computadora normal, primero hay que instalar pandas, con el comando pip install pandas. pip es el instalador de paquetes de Python, y descarga las librerías del Python Package Index, que se llama PyPI.)
>
> 🖱️ I'm clicking the fourth browser tab, at the top of the window, to show the official Matplotlib website.
>
> (Hago clic en la cuarta pestaña del navegador, arriba de la ventana, para mostrar el sitio oficial de Matplotlib.)
>
> 🟢 This is Matplotlib, at matplotlib.org, the most popular charting library in Python. It draws bar charts, line charts, scatter plots, and many more. pandas uses it behind the scenes when we call plot, so I'll draw the charts from pandas, and use Matplotlib to show them and to name the axes.
>
> (Esto es Matplotlib, en matplotlib.org, la librería de gráficos más popular de Python. Dibuja gráficos de barras, de líneas, de dispersión y muchos más. pandas la usa por detrás cuando llamamos a plot, así que voy a dibujar los gráficos desde pandas y usar Matplotlib para mostrarlos y ponerles nombre a los ejes.)
>
> 🟢 Both libraries are installed with pip on a normal computer, but Colab already comes with both installed, so I can import them directly.
>
> (Las dos librerías se instalan con pip en una computadora normal, pero Colab ya trae las dos instaladas, así que las puedo importar directamente.)
>
> 🖱️ I'm clicking the second browser tab, at the top of the window, to go back to Google Colab.
>
> (Hago clic en la segunda pestaña del navegador, arriba de la ventana, para volver a Google Colab.)

---

## 3:30–7:00 — Notebook nuevo y cargar los datos

> 🖱️ I'm clicking the New notebook button at the bottom of the Open notebook dialog, to create a fresh notebook.
>
> (Hago clic en el botón New notebook, abajo del cuadro Open notebook, para crear un notebook nuevo.)
>
> 🖱️ I'm clicking the notebook title field at the top left, and typing fitness_activity_analysis.ipynb, to identify this analysis. ipynb is the file extension of notebooks.
>
> (Hago clic en el campo del título del notebook, arriba a la izquierda, y escribo fitness_activity_analysis.ipynb, para identificar este análisis. ipynb es la extensión de los notebooks.)

Subís el CSV:

> 🖱️ I'm clicking the Files icon, the folder in the left sidebar, to upload the dataset.
>
> (Hago clic en el ícono Files, la carpeta de la barra lateral izquierda, para subir el dataset.)
>
> 🖱️ I'm clicking the Upload to session storage icon, at the top of the Files pane, and choosing fitness_activity.csv from my computer, so the notebook can read it.
>
> (Hago clic en el ícono Upload to session storage, arriba del panel Files, y elijo fitness_activity.csv de mi computadora, para que el notebook pueda leerlo.)

Si aparece un aviso de que los archivos se borran al reiniciar el entorno: *"I'm clicking OK on this warning, in the center of the screen, to continue the upload."*

> 🟢 A CSV file is a simple text file where each line is a row, and the values are separated by commas. It's one of the most common formats for sharing data.
>
> (Un archivo CSV es un archivo de texto simple donde cada línea es una fila, y los valores están separados por comas. Es uno de los formatos más comunes para compartir datos.)
>
> 🖱️ I'm clicking the plus Text button in the toolbar at the top left, to add a title and the goal.
>
> (Hago clic en el botón + Text de la barra de herramientas, arriba a la izquierda, para agregar un título y el objetivo.)

```markdown
# Fitness Activity Analysis
Goal: check data quality, calculate statistics, compare activity patterns, find relationships, and visualize the results.
```

**What each line does:**

- 🟢 `# Fitness Activity Analysis`: text cells use a format called Markdown. One hash sign at the start of a line makes it the main title of the notebook, in big letters.

  (Las celdas de texto usan un formato que se llama Markdown. Un numeral al principio de la línea la convierte en el título principal del notebook, en letras grandes.)

- 🟢 `Goal: ...`: this line says what I want to do with the data: check its quality, calculate statistics, compare patterns, find relationships, and visualize the results. That way, anyone who opens the notebook understands it right away.

  (Esta línea dice qué quiero hacer con los datos: revisar su calidad, calcular estadísticas, comparar patrones, encontrar relaciones y visualizar los resultados. Así, cualquiera que abra el notebook lo entiende enseguida.)

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

- 🟢 `import pandas as pd`: import tells Python to load a library, so I can use its functions. This loads pandas, the library from the website I showed, already installed in Colab. The words "as pd" give it a short name, so I can write pd instead of pandas every time. pd is the name almost everyone uses, so other analysts recognize it right away.

  (import le dice a Python que cargue una librería, para poder usar sus funciones. Esto carga pandas, la librería del sitio que mostré, que ya viene instalada en Colab. Las palabras "as pd" le dan un nombre corto, así puedo escribir pd en vez de pandas cada vez. pd es el nombre que usa casi todo el mundo, así otros analistas lo reconocen enseguida.)

- 🟢 `import matplotlib.pyplot as plt`: Matplotlib is big, so I only load the part I need: pyplot, the module that draws and shows charts. The dot means that pyplot is inside matplotlib. I give it its usual short name, plt.

  (Matplotlib es grande, así que cargo solo la parte que necesito: pyplot, el módulo que dibuja y muestra los gráficos. El punto quiere decir que pyplot está adentro de matplotlib. Le doy su nombre corto habitual, plt.)

- 🟢 `df = pd.read_csv("fitness_activity.csv")`: I leave an empty line to separate the imports from the code. read_csv is a pandas function that reads a CSV file. It reads the file I uploaded, with its name in quotes, and stores the table in a variable called df, short for DataFrame. A DataFrame is a table with rows and columns, like a spreadsheet.

  (Dejo una línea vacía para separar los imports del código. read_csv es una función de pandas que lee un archivo CSV. Lee el archivo que subí, con su nombre entre comillas, y guarda la tabla en una variable que se llama df, abreviatura de DataFrame. Un DataFrame es una tabla con filas y columnas, como una hoja de cálculo.)

- 🟢 `df.head()`: head shows the first five rows of the table, to check that the data loaded correctly. I don't need print, because Colab always shows the result of the last line of a cell.

  (head muestra las primeras cinco filas de la tabla, para comprobar que los datos se cargaron bien. No necesito print, porque Colab siempre muestra el resultado de la última línea de una celda.)

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
>
> 🟢 The numbers on the left, starting at 0, are the index: pandas numbers the rows automatically, starting from zero.
>
> (Los números de la izquierda, que empiezan en 0, son el índice: pandas numera las filas automáticamente, empezando desde cero.)

---

## 7:00–11:30 — Calidad de los datos y limpieza

> 🖱️ I'm clicking the plus Text button in the toolbar at the top left, to add a section heading called Inspect the data.
>
> (Hago clic en el botón + Text de la barra de herramientas, arriba a la izquierda, para agregar un título de sección llamado Inspect the data.)

Escribís `## 1. Inspect the data`, y mientras escribís:

> 🟢 Two hash signs make a section heading, smaller than the main title. I'll number every section, so the notebook is easy to follow.
>
> (Dos numerales hacen un título de sección, más chico que el título principal. Voy a numerar cada sección, así el notebook es fácil de seguir.)
>
> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add a code cell that checks the data quality.
>
> (Hago clic en el botón + Code de la barra de herramientas, arriba a la izquierda, para agregar una celda de código que revisa la calidad de los datos.)
>
> 🟢 Before calculating anything, I check the data for three common problems: missing values, inconsistent text, and impossible numbers. If I skip this step, every result after it could be wrong.
>
> (Antes de calcular nada, reviso los datos buscando tres problemas comunes: valores faltantes, texto inconsistente y números imposibles. Si me salteo este paso, todos los resultados que vengan después podrían estar mal.)

Escribís la **celda 2**:

```python
df.info()
print(df.isna().sum())
print(df["workout_type"].unique())
df.describe()
```

**What each line does:**

- 🟢 `df.info()`: info lists every column of the table, with how many values are not empty and the data type. int64 means whole numbers, float64 means decimal numbers, and object or str means text. info prints by itself, so I don't need print.

  (info lista todas las columnas de la tabla, con cuántos valores no están vacíos y el tipo de dato. int64 son números enteros, float64 son números con decimales, y object o str es texto. info imprime solo, así que no necesito print.)

- 🟢 `print(df.isna().sum())`: isna checks every cell of the table and marks the empty ones as True. Then sum counts the True values in each column. So this shows how many missing values each column has. I need print here, because this isn't the last line of the cell.

  (isna revisa cada celda de la tabla y marca las vacías como True. Después sum cuenta los True de cada columna. Así que esto muestra cuántos valores faltantes tiene cada columna. Acá necesito print, porque esta no es la última línea de la celda.)

- 🟢 `print(df["workout_type"].unique())`: square brackets with a column name in quotes select one column of the table. unique lists every different value in that column, without repeating any. This lets me see if the workout names are written consistently.

  (Los corchetes con el nombre de una columna entre comillas seleccionan una columna de la tabla. unique lista todos los valores distintos de esa columna, sin repetir ninguno. Esto me deja ver si los nombres de los entrenamientos están escritos de forma consistente.)

- 🟢 `df.describe()`: describe gives a summary of each number column: how many values, the mean, the standard deviation, the minimum, the percentiles, and the maximum. It's a quick way to spot impossible values, like a negative number of steps. Colab shows it because it's the last line.

  (describe da un resumen de cada columna numérica: cuántos valores hay, la media, la desviación estándar, el mínimo, los percentiles y el máximo. Es una forma rápida de encontrar valores imposibles, como una cantidad negativa de pasos. Colab lo muestra porque es la última línea.)

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

> 🖱️ I'm clicking the plus Text button in the toolbar at the top left, to add a section heading for cleaning.
>
> (Hago clic en el botón + Text de la barra de herramientas, arriba a la izquierda, para agregar un título de sección para la limpieza.)

Escribís `## 2. Clean and prepare the data`.

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add a code cell that fixes the problems.
>
> (Hago clic en el botón + Code de la barra de herramientas, arriba a la izquierda, para agregar una celda de código que corrige los problemas.)

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

- 🟢 `df = df[df["steps"] >= 0].copy()`: this line removes the impossible values. The part inside, df["steps"] >= 0, checks every row and gives True when the steps are zero or more. Putting that check inside df and square brackets keeps only the True rows, so the two days with minus one steps are removed. copy makes an independent new table, so pandas doesn't show a warning when I change it in the next lines.

  (Esta línea quita los valores imposibles. La parte de adentro, df["steps"] >= 0, revisa cada fila y da True cuando los pasos son cero o más. Poner esa comprobación adentro de df y corchetes deja solo las filas True, así que se quitan los dos días con menos uno pasos. copy crea una tabla nueva e independiente, así pandas no muestra una advertencia cuando la cambio en las líneas siguientes.)

- 🟢 `df["sleep_hours"] = df["sleep_hours"].fillna(df["sleep_hours"].median())`: now the missing sleep values. At the end of the line, median calculates the median of the sleep column, the middle value when they're sorted, which is 7.15 hours. fillna fills every empty cell with that value, and I save the result back in the same column. I fill instead of removing, because the steps and calories of those four days are still valid. And I use the median instead of the mean, because it isn't affected by a few very short or very long nights.

  (Ahora los valores de sueño faltantes. Al final de la línea, median calcula la mediana de la columna de sueño, el valor del medio cuando están ordenados, que es 7,15 horas. fillna completa cada celda vacía con ese valor, y guardo el resultado en la misma columna. Completo en vez de quitar, porque los pasos y las calorías de esos cuatro días siguen siendo válidos. Y uso la mediana en vez de la media, porque no le afectan unas pocas noches muy cortas o muy largas.)

- 🟢 `df["workout_type"] = df["workout_type"].str.strip().str.title()`: .str gives access to text functions for the whole column at once. strip removes the spaces at the start and at the end, like in "Cycling" with a space. title writes each word with a capital first letter and the rest in lowercase, so running and YOGA become Running and Yoga. Now every workout has only one spelling.

  (.str da acceso a funciones de texto para toda la columna a la vez. strip quita los espacios del principio y del final, como en "Cycling" con un espacio. title escribe cada palabra con la primera letra en mayúscula y el resto en minúscula, así running y YOGA pasan a ser Running y Yoga. Ahora cada entrenamiento se escribe de una sola forma.)

- 🟢 `df["date"] = pd.to_datetime(df["date"])`: the dates were stored as text. pd.to_datetime converts them into real dates, so pandas knows the year, the month, the day, and the day of the week of each one.

  (Las fechas estaban guardadas como texto. pd.to_datetime las convierte en fechas de verdad, así pandas conoce el año, el mes, el día y el día de la semana de cada una.)

- 🟢 `df["day"] = df["date"].dt.day_name()`: .dt gives access to date functions for the whole column. day_name returns the name of the day, like Monday or Saturday. I save it in a new column called day. This only works because I converted the dates in the line above.

  (.dt da acceso a funciones de fecha para toda la columna. day_name devuelve el nombre del día, como Monday o Saturday. Lo guardo en una columna nueva que se llama day. Esto solo funciona porque convertí las fechas en la línea de arriba.)

- 🟢 `print(df.shape)`: shape gives the size of the table: the number of rows and the number of columns. I expect 198 rows, because I removed two.

  (shape da el tamaño de la tabla: la cantidad de filas y la cantidad de columnas. Espero 198 filas, porque quité dos.)

- 🟢 `print(df["workout_type"].unique())`: and unique again, to confirm that now there are only five workout names.

  (Y unique otra vez, para confirmar que ahora hay solo cinco nombres de entrenamiento.)

> 🖱️ I'm clicking the Run cell button to the left of this cell, to clean the data.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para limpiar los datos.)
>
> 🟢 Now we have 198 days and 7 columns: the six original ones, plus day. And there are exactly 5 workout types. We removed the two days with negative steps and filled four sleep values.
>
> (Ahora tenemos 198 días y 7 columnas: las seis originales, más day. Y hay exactamente 5 tipos de entrenamiento. Quitamos los dos días con pasos negativos y completamos cuatro valores de sueño.)

---

## 11:30–17:00 — Estadísticas y comparaciones

> 🖱️ I'm clicking the plus Text button in the toolbar at the top left, to add a section heading for summary statistics.
>
> (Hago clic en el botón + Text de la barra de herramientas, arriba a la izquierda, para agregar un título de sección para las estadísticas.)

Escribís `## 3. Summary statistics`.

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add a code cell with the statistics of the activity measures.
>
> (Hago clic en el botón + Code de la barra de herramientas, arriba a la izquierda, para agregar una celda de código con las estadísticas de las medidas de actividad.)

Escribís la **celda 4**:

```python
measures = ["steps", "active_minutes", "calories", "sleep_hours"]
df[measures].describe().round(1)
```

**What each line does:**

- 🟢 `measures = ["steps", "active_minutes", "calories", "sleep_hours"]`: measures is a Python list, written with square brackets, with the names of the four number columns I want to study: steps, active minutes, calories, and sleep hours. I save it in a variable so I don't have to write the four names again. I'll reuse it later for the correlations.

  (measures es una lista de Python, escrita con corchetes, con los nombres de las cuatro columnas numéricas que quiero estudiar: pasos, minutos activos, calorías y horas de sueño. La guardo en una variable para no tener que escribir los cuatro nombres otra vez. La voy a reutilizar después para las correlaciones.)

- 🟢 `df[measures].describe().round(1)`: putting the list inside the square brackets selects those four columns. describe calculates their statistics, now with the clean data. round with a 1 rounds every number to one decimal, so the table is easier to read. Each dot adds one more step to the result of the step before.

  (Poner la lista adentro de los corchetes selecciona esas cuatro columnas. describe calcula sus estadísticas, ahora con los datos limpios. round con un 1 redondea cada número a un decimal, así la tabla es más fácil de leer. Cada punto agrega un paso más sobre el resultado del paso anterior.)

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

> 🖱️ I'm clicking the plus Text button in the toolbar at the top left, to add a section heading for comparisons.
>
> (Hago clic en el botón + Text de la barra de herramientas, arriba a la izquierda, para agregar un título de sección para las comparaciones.)

Escribís `## 4. Compare activity patterns`.

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add a code cell that compares the workout types.
>
> (Hago clic en el botón + Code de la barra de herramientas, arriba a la izquierda, para agregar una celda de código que compara los tipos de entrenamiento.)

Escribís la **celda 5**:

```python
by_workout = df.groupby("workout_type")[["steps", "active_minutes", "calories"]].mean().round(0)
by_workout.sort_values("calories", ascending=False)
```

**What each line does:**

- 🟢 `by_workout = df.groupby("workout_type")[["steps", "active_minutes", "calories"]].mean().round(0)`: this line has several steps, chained with dots. First, groupby with workout_type puts together all the days of each workout: all the Running days in one group, all the Yoga days in another, and so on. Then the double square brackets select three columns: steps, active minutes, and calories. The outer brackets select columns, and the inner ones are the list of names. mean calculates the average of each column for each group, and round with a 0 rounds to whole numbers. I save the result in by_workout, because I'll use it again for a chart.

  (Esta línea tiene varios pasos, encadenados con puntos. Primero, groupby con workout_type junta todos los días de cada entrenamiento: todos los días de Running en un grupo, todos los de Yoga en otro, y así. Después, los corchetes dobles seleccionan tres columnas: pasos, minutos activos y calorías. Los corchetes de afuera seleccionan columnas, y los de adentro son la lista de nombres. mean calcula el promedio de cada columna para cada grupo, y round con un 0 redondea a números enteros. Guardo el resultado en by_workout, porque lo voy a usar otra vez para un gráfico.)

- 🟢 `by_workout.sort_values("calories", ascending=False)`: sort_values orders the rows by the calories column. ascending equals False means from highest to lowest, so the workout that burns the most calories is at the top. It's the last line, so Colab shows the table.

  (sort_values ordena las filas por la columna de calorías. ascending igual a False quiere decir de mayor a menor, así el entrenamiento que más calorías quema queda arriba. Es la última línea, así que Colab muestra la tabla.)

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

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add a code cell that compares the days of the week.
>
> (Hago clic en el botón + Code de la barra de herramientas, arriba a la izquierda, para agregar una celda de código que compara los días de la semana.)

Escribís la **celda 6**:

```python
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
by_day = df.groupby("day")[["steps", "sleep_hours"]].mean().reindex(days).round(1)
by_day
```

**What each line does:**

- 🟢 `days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]`: a list with the seven days in calendar order, from Monday to Sunday. I need it because pandas sorts text alphabetically, so it would start with Friday, which is confusing to read.

  (Una lista con los siete días en orden de calendario, de lunes a domingo. La necesito porque pandas ordena el texto alfabéticamente, así que empezaría por Friday, y eso es confuso de leer.)

- 🟢 `by_day = df.groupby("day")[["steps", "sleep_hours"]].mean().reindex(days).round(1)`: the same idea as before, now by day of the week. groupby with day puts together all the Mondays, all the Tuesdays, and so on. I select two columns, steps and sleep hours, and mean calculates the average for each day. reindex with my list reorders the rows, so they follow the calendar. round with a 1 keeps one decimal. I save it in by_day, for the bar chart later.

  (La misma idea que antes, ahora por día de la semana. groupby con day junta todos los lunes, todos los martes, y así. Selecciono dos columnas, pasos y horas de sueño, y mean calcula el promedio de cada día. reindex con mi lista reordena las filas, así siguen el calendario. round con un 1 deja un decimal. Lo guardo en by_day, para el gráfico de barras de después.)

- 🟢 `by_day`: writing the name of a variable alone on the last line shows it. So this displays the table.

  (Escribir el nombre de una variable sola en la última línea la muestra. Así que esto muestra la tabla.)

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

## 17:00–22:00 — Relaciones entre variables y gráficos

> 🖱️ I'm clicking the plus Text button in the toolbar at the top left, to add a section heading for relationships.
>
> (Hago clic en el botón + Text de la barra de herramientas, arriba a la izquierda, para agregar un título de sección para las relaciones.)

Escribís `## 5. Relationships between variables`.

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add a code cell with the correlation table.
>
> (Hago clic en el botón + Code de la barra de herramientas, arriba a la izquierda, para agregar una celda de código con la tabla de correlaciones.)

Escribís la **celda 7**:

```python
df[measures].corr().round(2)
```

**What each line does:**

- 🟢 `df[measures].corr().round(2)`: first, I select the four columns with the measures list I saved before. corr calculates the correlation between every pair of them, and round with a 2 keeps two decimals. A correlation is a number between minus one and one. Close to one means the two measures go up together. Close to minus one means one goes up when the other goes down. And close to zero means there's no clear relationship.

  (Primero, selecciono las cuatro columnas con la lista measures que guardé antes. corr calcula la correlación entre cada par de ellas, y round con un 2 deja dos decimales. Una correlación es un número entre menos uno y uno. Cerca de uno quiere decir que las dos medidas suben juntas. Cerca de menos uno quiere decir que una sube cuando la otra baja. Y cerca de cero quiere decir que no hay una relación clara.)

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

> 🖱️ I'm clicking the plus Text button in the toolbar at the top left, to add a section heading for the charts.
>
> (Hago clic en el botón + Text de la barra de herramientas, arriba a la izquierda, para agregar un título de sección para los gráficos.)

Escribís `## 6. Visualizations`.

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add a code cell for a bar chart of steps by day.
>
> (Hago clic en el botón + Code de la barra de herramientas, arriba a la izquierda, para agregar una celda de código para un gráfico de barras de pasos por día.)

Escribís la **celda 8**:

```python
by_day["steps"].plot(kind="bar", title="Average Steps by Day of the Week", xlabel="Day", ylabel="Steps", rot=45)
plt.show()
```

**What each line does:**

- 🟢 `by_day["steps"].plot(kind="bar", title="Average Steps by Day of the Week", xlabel="Day", ylabel="Steps", rot=45)`: by_day and steps in square brackets takes the steps column of the table by day. plot draws it, and kind equals bar makes it a bar chart, with one bar per day. title is the text at the top of the chart. xlabel and ylabel are the names of the horizontal and the vertical axes. rot equals 45 rotates the day names 45 degrees, so they don't overlap. pandas uses Matplotlib behind the scenes to draw it.

  (by_day con steps entre corchetes toma la columna de pasos de la tabla por día. plot la dibuja, y kind igual a bar la convierte en un gráfico de barras, con una barra por día. title es el texto de arriba del gráfico. xlabel e ylabel son los nombres del eje horizontal y del vertical. rot igual a 45 gira los nombres de los días 45 grados, así no se pisan. pandas usa Matplotlib por detrás para dibujarlo.)

- 🟢 `plt.show()`: plt is pyplot, from my imports. show displays the finished chart below the cell, without extra text above it.

  (plt es pyplot, de mis imports. show muestra el gráfico terminado debajo de la celda, sin texto de más arriba.)

> 🖱️ I'm clicking the Run cell button to the left of this cell, to draw the chart.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para dibujar el gráfico.)
>
> 🟢 The Saturday bar stands out, almost twice as tall as Sunday, which is the lowest. The weekdays are in between. A bar chart is the right choice here, because I'm comparing separate groups.
>
> (La barra del sábado se destaca, casi el doble de alta que la del domingo, que es la más baja. Los días de semana están en el medio. Un gráfico de barras es la opción correcta acá, porque estoy comparando grupos separados.)

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add a code cell for a scatter plot.
>
> (Hago clic en el botón + Code de la barra de herramientas, arriba a la izquierda, para agregar una celda de código para un gráfico de dispersión.)

Escribís la **celda 9**:

```python
df.plot(kind="scatter", x="active_minutes", y="calories", title="Active Minutes vs Calories")
plt.show()
```

**What each line does:**

- 🟢 `df.plot(kind="scatter", x="active_minutes", y="calories", title="Active Minutes vs Calories")`: now I call plot on the whole table, with kind equals scatter, which makes a scatter plot. It draws one dot for each day. x is the column for the horizontal axis, the active minutes, and y is the column for the vertical axis, the calories. A scatter plot shows if two measures move together. pandas uses the column names as the axis labels.

  (Ahora llamo a plot sobre toda la tabla, con kind igual a scatter, que hace un gráfico de dispersión. Dibuja un punto por cada día. x es la columna del eje horizontal, los minutos activos, e y es la columna del eje vertical, las calorías. Un gráfico de dispersión muestra si dos medidas se mueven juntas. pandas usa los nombres de las columnas como nombres de los ejes.)

- 🟢 `plt.show()`: and show displays the chart below the cell.

  (Y show muestra el gráfico debajo de la celda.)

> 🖱️ I'm clicking the Run cell button to the left of this cell, to draw the scatter plot.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para dibujar el gráfico de dispersión.)
>
> 🟢 The dots form a clear rising line, from the bottom left to the top right: that's the 0.91 correlation. Each extra active minute adds calories in a very predictable way.
>
> (Los puntos forman una línea ascendente clara, de abajo a la izquierda hacia arriba a la derecha: esa es la correlación de 0,91. Cada minuto activo extra suma calorías de una forma muy predecible.)

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add a code cell for a chart of calories by workout.
>
> (Hago clic en el botón + Code de la barra de herramientas, arriba a la izquierda, para agregar una celda de código para un gráfico de calorías por entrenamiento.)

Escribís la **celda 10**:

```python
by_workout["calories"].sort_values().plot(kind="barh", title="Average Calories by Workout Type")
plt.xlabel("Calories")
plt.show()
```

**What each line does:**

- 🟢 `by_workout["calories"].sort_values().plot(kind="barh", title="Average Calories by Workout Type")`: by_workout and calories in square brackets takes the calories column from the workout table I saved before. sort_values orders it from low to high. kind equals barh means horizontal bars. Matplotlib draws the first value at the bottom, so sorting from low to high puts the highest bar at the top, like a ranking.

  (by_workout con calories entre corchetes toma la columna de calorías de la tabla de entrenamientos que guardé antes. sort_values la ordena de menor a mayor. kind igual a barh quiere decir barras horizontales. Matplotlib dibuja el primer valor abajo, así que ordenar de menor a mayor deja la barra más alta arriba, como un ranking.)

- 🟢 `plt.xlabel("Calories")`: xlabel sets the name of the horizontal axis, where the calories are.

  (xlabel pone el nombre del eje horizontal, donde están las calorías.)

- 🟢 `plt.show()`: and show displays the chart.

  (Y show muestra el gráfico.)

> 🖱️ I'm clicking the Run cell button to the left of this cell, to draw the chart.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para dibujar el gráfico.)
>
> 🟢 Running is at the top and Rest at the bottom. Even on rest days, the body burns about 2,000 calories, which is the base energy we use just to live. So the difference between a rest day and a running day is about 600 calories.
>
> (Running está arriba y Rest abajo. Incluso en los días de descanso el cuerpo quema unas 2.000 calorías, que es la energía base que usamos solo para vivir. Así que la diferencia entre un día de descanso y uno de running es de unas 600 calorías.)

---

## 22:00–23:30 — Conclusiones

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

> 🖱️ I'm clicking the plus Text button in the toolbar at the top left, to add the conclusions at the end of the notebook.
>
> (Hago clic en el botón + Text de la barra de herramientas, arriba a la izquierda, para agregar las conclusiones al final del notebook.)

Escribís la celda de texto:

```markdown
## 7. Conclusions
- Data quality: 200 rows became 198 days (2 negative steps removed, 4 sleep values filled, 5 workout names).
- Average day: about 7,700 steps, 44 active minutes, 2,390 calories, and 7.2 hours of sleep.
- Saturday is the most active day (about 11,200 steps) and Sunday the least (about 5,800).
- Running burns the most calories (about 2,636) and rest days the least (about 2,047).
- Active minutes and calories are strongly related (0.91). Sleep is not related to activity.
```

**What each line does:**

- 🟢 `## 7. Conclusions`: the last section heading. Each line below starts with a dash, which makes a bullet point.

  (El último título de sección. Cada línea de abajo empieza con un guion, que hace una viñeta.)

- 🟢 `- Data quality: ...`: the data went from 200 rows to 198 clean days. We removed 2 days with negative steps, a sensor error, filled 4 missing sleep values with the median, and fixed 9 workout spellings down to 5 names.

  (Los datos pasaron de 200 filas a 198 días limpios. Quitamos 2 días con pasos negativos, un error del sensor, completamos 4 valores de sueño faltantes con la mediana y redujimos 9 formas de escribir los entrenamientos a 5 nombres.)

- 🟢 `- Average day: ...`: an average day has about 7,700 steps, 44 active minutes, 2,390 calories, and 7.2 hours of sleep.

  (Un día promedio tiene unos 7.700 pasos, 44 minutos activos, 2.390 calorías y 7,2 horas de sueño.)

- 🟢 `- Saturday is the most active day ...`: the weekly pattern: Saturday is the most active day, with about 11,200 steps, and Sunday the least active, with about 5,800. Sleep is also longer on weekends.

  (El patrón semanal: el sábado es el día más activo, con unos 11.200 pasos, y el domingo el menos activo, con unos 5.800. El sueño también es más largo los fines de semana.)

- 🟢 `- Running burns the most calories ...`: running days burn the most calories, about 2,636, and rest days the least, about 2,047. Cycling has the most active minutes, but running has many more steps.

  (Los días de running queman más calorías, unas 2.636, y los de descanso menos, unas 2.047. Cycling tiene más minutos activos, pero running tiene muchos más pasos.)

- 🟢 `- Active minutes and calories ...`: the relationships: active minutes and calories are strongly related, 0.91, and steps and calories too, 0.83. Sleep has almost no relationship with activity, about minus 0.05.

  (Las relaciones: los minutos activos y las calorías están muy relacionados, 0,91, y los pasos y las calorías también, 0,83. El sueño casi no tiene relación con la actividad, unos menos 0,05.)

> 🟢 To sum up: this person is most active on Saturdays and rests on Sundays, running burns the most calories, and active minutes are the best sign of how many calories a day burns.
>
> (Para resumir: esta persona es más activa los sábados y descansa los domingos, running es lo que más calorías quema, y los minutos activos son el mejor indicador de cuántas calorías se queman en un día.)

---

## 23:30–28:00 — Epílogo (4–5 minutos)

Revisá en las reglas de Odin qué tiene que tener el epílogo y ajustá este texto si piden algo distinto.

> 🖱️ I'm opening the File menu at the top left of Colab and choosing Download, then Download .ipynb, to save the finished notebook for the deliverables.
>
> (Abro el menú File, arriba a la izquierda de Colab, y elijo Download y después Download .ipynb, para guardar el notebook terminado para los entregables.)

### Resumen paso a paso

Subís hasta el principio del notebook y vas bajando: cada frase va cuando la sección correspondiente está en pantalla. Señalá con el mouse lo que nombrás.

> 🖱️ I'm scrolling up to the top of the notebook, in the center of the screen, with the mouse wheel, to go over everything we did, step by step.
>
> (Subo hasta el principio del notebook, en el centro de la pantalla, con la rueda del mouse, para repasar todo lo que hicimos, paso a paso.)
>
> 🟢 Let me summarize the whole analysis. We started with the title and the goal: check the data quality, calculate statistics, compare patterns, look at relationships, and visualize the results.
>
> (Les resumo todo el análisis. Empezamos con el título y el objetivo: revisar la calidad de los datos, calcular estadísticas, comparar patrones, ver relaciones y visualizar los resultados.)
>
> 🟢 In the first cell, we imported two external libraries, already installed in Colab: pandas for the table and Matplotlib for the charts. Then we loaded the CSV: one row per day, with six columns.
>
> (En la primera celda importamos dos librerías externas, que ya vienen instaladas en Colab: pandas para la tabla y Matplotlib para los gráficos. Después cargamos el CSV: una fila por día, con seis columnas.)
>
> 🖱️ I'm scrolling down the notebook, in the center of the screen, to section 1, Inspect the data, to show what we found.
>
> (Bajo por el notebook, en el centro de la pantalla, hasta la sección 1, Inspect the data, para mostrar lo que encontramos.)
>
> 🟢 In section 1, we inspected the data before calculating anything, and we found three problems: four days with no sleep data, 9 spellings for only 5 workouts, and negative steps.
>
> (En la sección 1 inspeccionamos los datos antes de calcular nada, y encontramos tres problemas: cuatro días sin datos de sueño, 9 formas de escribir solo 5 entrenamientos y pasos negativos.)
>
> 🖱️ I'm scrolling down the notebook, in the center of the screen, to section 2, Clean and prepare the data, to review the cleaning.
>
> (Bajo por el notebook, en el centro de la pantalla, hasta la sección 2, Clean and prepare the data, para repasar la limpieza.)
>
> 🟢 In section 2, we fixed those problems, one line each. We also converted the dates and added the day of the week. We went from 200 rows to 198 clean days.
>
> (En la sección 2 arreglamos esos problemas, con una línea para cada uno. También convertimos las fechas y agregamos el día de la semana. Pasamos de 200 filas a 198 días limpios.)
>
> 🖱️ I'm scrolling down the notebook, in the center of the screen, to sections 3 and 4, to review the statistics and the comparisons.
>
> (Bajo por el notebook, en el centro de la pantalla, hasta las secciones 3 y 4, para repasar las estadísticas y las comparaciones.)
>
> 🟢 In section 3, we described an average day: about 7,700 steps, 44 active minutes, 2,400 calories, and 7.2 hours of sleep. In section 4, we compared workouts and days: running burns the most, and Saturday is the most active day.
>
> (En la sección 3 describimos un día promedio: unos 7.700 pasos, 44 minutos activos, 2.400 calorías y 7,2 horas de sueño. En la sección 4 comparamos los entrenamientos y los días: running es lo que más quema, y el sábado es el día más activo.)
>
> 🖱️ I'm scrolling down the notebook, in the center of the screen, to sections 5 and 6, to review the relationships and the charts.
>
> (Bajo por el notebook, en el centro de la pantalla, hasta las secciones 5 y 6, para repasar las relaciones y los gráficos.)
>
> 🟢 In section 5, the correlations showed that active minutes and calories go together, 0.91, while sleep isn't related to activity. In section 6, the three charts showed the same results visually: the Saturday peak, the rising line of minutes and calories, and the ranking of workouts.
>
> (En la sección 5, las correlaciones mostraron que los minutos activos y las calorías van juntos, 0,91, mientras que el sueño no se relaciona con la actividad. En la sección 6, los tres gráficos mostraron los mismos resultados de forma visual: el pico del sábado, la línea ascendente de minutos y calorías, y el ranking de entrenamientos.)
>
> 🖱️ I'm scrolling down the notebook, in the center of the screen, to section 7, Conclusions, at the end, to review the results.
>
> (Bajo por el notebook, en el centro de la pantalla, hasta la sección 7, Conclusions, al final, para repasar los resultados.)
>
> 🟢 And finally, we wrote down the conclusions with the real numbers, so anyone who opens the notebook can read the results without running the code.
>
> (Y por último, anotamos las conclusiones con los números reales, así cualquiera que abra el notebook puede leer los resultados sin ejecutar el código.)

### Decisiones y próximos pasos

> 🖱️ I'm scrolling slowly up through the notebook, in the center of the screen, with the mouse wheel, to go over the decisions I made.
>
> (Subo despacio por el notebook, en el centro de la pantalla, con la rueda del mouse, para repasar las decisiones que tomé.)
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
2. Subí los **cuatro archivos por separado**: el **MP4**, el **ZIP original de TaskRecorder**, **Deliverables.zip** (con el `.ipynb` descargado **y** `fitness_activity.csv`: en bookstore lo marcaron porque faltaba el CSV) y **Metadata.rtf**.
