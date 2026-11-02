# 8xfo6301 — Gráfico interactivo con Plotly en Google Colab

Guion para grabar la tarea **8xfo6301**: aprendés a usar **Plotly**, una biblioteca nueva, en **Google Colab**, y creás un **gráfico interactivo** con el dataset de ejemplo **Gapminder**, que viene dentro de Plotly. Se graba en **Firefox**, en **una sola toma**. La grabación tiene que durar **entre 15:00 y 50:59**. Este guion apunta a unos **23 minutos**, epílogo incluido.

### Cambios en esta versión

| Problema de la versión anterior | Qué cambió |
| ------------------------------- | ---------- |
| Se explicaba el código línea por línea (listas *What each line does*) | El código es **mínimo** y se explica con **una** frase por celda |
| Celdas de texto para cada título de sección | **Todas las celdas son de código**, salvo la última (conclusiones). Los títulos se dicen en voz alta |
| Recorrido largo por la documentación (página principal, Bubble Charts, referencia de la API, búsquedas con `Ctrl + F`) | Una sola página, **Bubble Charts**, en menos de 2 minutos. Si el Goal no pide consultar la documentación, se saltea |
| Intro y plan de 2 minutos, con el Goal en Google Docs y el notebook creado durante la grabación | Menos de 20 segundos, con la **descripción de la tarea** en pantalla. Después, desde el Dock, abrís la ventana de Firefox con Colab y el notebook vacío ya creado |
| Atajos de Windows (`Ctrl`) | Atajos de **Mac** (`Cmd`), dichos en voz alta |
| El epílogo no tenía desafíos | El epílogo (2 a 4 minutos) resume el enfoque, los **desafíos** y las reflexiones |

### Las partes de la tarea y dónde están

| Paso | Dónde |
| ---- | ----- |
| 1. Comprobar Plotly y cargar Gapminder | Celdas 1 y 2 |
| 2. Explorar los datos y filtrar 2007 | Celdas 3 y 4 |
| 3. Primer gráfico, simple | Celda 5 |
| 4. Consultar la documentación de Plotly (**si el Goal lo pide**) | Pestaña nueva en Firefox |
| 5. Gráfico mejorado (burbujas, escala logarítmica, título, ejes) | Celda 6 |
| 6. Probar las interacciones: tooltip, leyenda, zoom, pan, reset, PNG | Sobre el gráfico de la celda 6 |
| 7. Gráfico animado de 1952 a 2007 (**opcional**) | Celda 7 |
| 8. Guardar como HTML, conclusiones y descargar | Celda 8 + última celda de texto |

**Cómo leer este guion:**

- 🖱️ = lo decís **mientras hacés** la acción. Siempre dice **qué** hacés y **dónde** está en la pantalla. Son las frases que cuenta AutoQC: **no te saltees ninguna**.
- 🟢 = explicación corta, entre una acción y otra.
- El texto en castellano es lo que hacés en pantalla. No se lee.
- Si usás un **atajo de teclado**, decí la tecla en voz alta: *"I'm pressing Command + T"*.
- **No expliques el código línea por línea.** Cada celda tiene **una** frase 🟢 que dice para qué sirve, y la decís antes de escribirla.
- **Todas las celdas son de código**, salvo la última (conclusiones), que es de texto. El título de cada paso **no se escribe**: lo decís en voz alta (*"Step two: explore the data"*).
- Toda celda sigue el mismo ciclo: **decir el título del paso → scroll hasta el final → clic en + Code → escribir el código → clic en Run → señalar el resultado → explicarlo.**

> **Importante:** el Goal de Studio tiene prioridad sobre este guion. **No tuve el texto del Goal**: revisá los pendientes de abajo antes de grabar.

---

## Pendientes antes de grabar

| Dato | Lo que supuse | Qué hacer |
| ---- | ------------- | --------- |
| **Goal aprobado** | *"Usar Plotly en Google Colab para crear un gráfico interactivo a partir de un dataset de ejemplo."* | Pasame el Goal (sin el Approval ID) y ajusto los pasos, la intro y el epílogo. |
| **Documentación (paso 4)** | Como es una tarea de aprender una biblioteca nueva, dejé **una** consulta corta a la página Bubble Charts. | Si el Goal no pide consultar la documentación, salteá el paso 4 y decí en el paso 5: *"Plotly Express has three options for this…"*. |
| **Dataset** | Gapminder, de `px.data.gapminder()`. No hay que subir nada. | Si el Goal nombra otro dataset, avisame. |
| **Gráfico animado (paso 7)** | Opcional. | Si el Goal pide un solo gráfico, saltealo. La grabación igual pasa de los 15:00. |
| **Versión de Plotly** | Probado con Plotly 5, 6 y 7. | Decí el número que muestre **tu** celda 1. |

---

## Archivos de la carpeta

```
8xfo6301-plotly-interactive-chart/
├── README.md               ← este guion
└── plotly_gapminder.ipynb  ← notebook de referencia, completo y en orden
```

Para probar el notebook de referencia: en Colab, **File → Upload notebook → Browse**, elegís `plotly_gapminder.ipynb` y ejecutás **Runtime → Run all**. No lo uses en la grabación: ahí el código se escribe.

---

## El dataset

**Gapminder**, la versión que trae Plotly con `px.data.gapminder()`: datos públicos por país, de la Fundación Gapminder. **1.704 filas y 8 columnas** (142 países × 12 años, de 1952 a 2007, cada 5 años), **sin valores faltantes**. Filtrado a **2007**: **142 filas**, una por país.

| Columna | Qué contiene | Dónde se usa |
| ------- | ------------ | ------------ |
| `country` | País | Nombre en negrita del tooltip (`hover_name`) |
| `continent` | Africa, Americas, Asia, Europe, Oceania | Color |
| `year` | Año | Filtro de 2007 y animación |
| `lifeExp` | Esperanza de vida, en años | Eje Y |
| `pop` | Población | Tamaño de la burbuja |
| `gdpPercap` | PIB per cápita, en dólares | Eje X |
| `iso_alpha`, `iso_num` | Códigos del país | No se usan |

**Valores de referencia de 2007**, para comprobar lo que ves en el tooltip:

| Dato | Valor |
| ---- | ----- |
| Países por continente | Africa 52, Asia 33, Europe 30, Americas 25, Oceania 2 |
| Mediana de esperanza de vida | Africa 52,9 · Asia 72,4 · Americas 72,9 · Europe 78,6 · Oceania 80,7 |
| Burbujas más grandes | China (1.319 millones; PIB 4.959; 73,0 años) e India (1.110 millones; PIB 2.452; 64,7 años) |
| PIB per cápita más alto | Norway 49.357 · Kuwait 47.307 · Singapore 47.143 |
| Esperanza de vida más baja | Swaziland 39,6 · Mozambique 42,1 · Zambia 42,4 |
| Excepciones (PIB alto, vida corta) | South Africa (9.270; 49,3), Botswana (12.570; 50,7), Equatorial Guinea (12.154; 51,6) |
| Mediana de Africa, 1952 → 2007 | 38,8 → 52,9 años |

---

## Antes de grabar

1. Leé el Goal y comparalo con este guion.
2. En **Firefox**, dejá **dos ventanas**: la primera con la **descripción de la tarea**, en pantalla, porque con ella arranca la grabación. La segunda con **Google Colab** (https://colab.research.google.com) y el notebook ya creado: **File → New notebook in Drive**, con el nombre `plotly_gapminder` y la **celda de código vacía** que Colab crea sola. Revisá que, al hacer clic en el ícono de Firefox en el **Dock (a la derecha)**, Colab aparezca en la **segunda línea** de la lista.
3. En Colab, **Tools → Settings → AI assistance**: ocultá las funciones de IA generativa, si está la opción.
4. Revisá que arriba a la derecha de Colab no se vea tu nombre ni tu correo.
5. Maximizá la ventana de Colab y agrandá el zoom (`Cmd + +`) para que el código se lea.
6. Practicá una vez entera en voz alta con cronómetro, y anotá la versión de Plotly que muestra la celda 1.
7. Ejecutá las celdas con el **botón Run** (mouse), no con el teclado, así cada ejecución tiene su frase.
8. Nunca más de 45 segundos en silencio. Si Colab te sugiere código (Gemini), ignoralo y seguí escribiendo vos.
9. Salvo la descripción de la tarea del principio, no muestres Studio, Mercor, datos personales ni herramientas de IA.

---

## 0:00–1:00 — Introducción y abrir Colab en Firefox

Empezás con la **descripción de la tarea** en pantalla. La introducción dura **menos de 20 segundos**:

> 🟢 I will be beginning my task soon. I'll learn Plotly, a new library for me, in Google Colab, and build an interactive chart with Gapminder, a sample dataset that comes with Plotly. Then I'll test every interaction and save the chart.

> 🖱️ I'm clicking the yellow minimize button at the top left of this Firefox window, to put the task description away.

> 🖱️ I'm clicking the Firefox icon in the Dock, on the right side of the screen, to see my open Firefox windows.

> 🖱️ I'm clicking the second line of the list, the Google Colab window, to open my notebook.

> 🖱️ I'm pointing at the notebook name, plotly_gapminder, at the top left next to the Colab logo. I created this empty notebook before starting.

> 🖱️ I'm pointing at the empty code cell at the top of the notebook, where I'll check Plotly.

---

## 1:00–3:30 — Paso 1: comprobar Plotly y cargar Gapminder

> 🟢 Step one: check Plotly and load the data.

> 🖱️ I'm clicking inside the empty code cell at the top of the notebook, to start typing in it.

> 🟢 This first code cell imports Plotly and prints its version, to check that it's installed in Colab.

> 🖱️ I'm typing the two lines in the first code cell, in the middle of the screen.

**Celda 1:**

```python
import plotly
print(plotly.__version__)
```

> 🖱️ I'm clicking the Run cell button, the play icon on the left edge of the first code cell, to run the check.

> 🖱️ I'm pointing at the status at the top right of Colab, which turns green when the runtime is connected.

> 🖱️ I'm pointing at the version number under the first code cell.

> 🟢 It shows version [leé tu número]. Plotly is already installed in Colab, so I don't need pip install.

> 🖱️ I'm scrolling down to the end of the first code cell, and clicking the plus Code button in the toolbar at the top left, to add the second code cell below it.

> 🟢 This second code cell imports Plotly Express, the simple part of Plotly, as px, loads the Gapminder sample data into a table called df, and shows the first five rows.

> 🖱️ I'm typing the code in the second code cell, in the middle of the screen.

**Celda 2:**

```python
import plotly.express as px
df = px.data.gapminder()
df.head()
```

> 🖱️ I'm clicking the Run cell button on the left of the second code cell, to load the data.

> 🖱️ I'm moving the mouse across the column headers of the table, below the second code cell, from left to right.

> 🟢 Each row is one country in one year: country, continent, year, lifeExp for life expectancy, pop for population, and gdpPercap for GDP per capita.

> 🖱️ I'm pointing at the first rows of the table, all for Afghanistan, on the left.

> 🟢 The first rows are Afghanistan, from 1952 on, every five years.

---

## 3:30–5:30 — Paso 2: explorar los datos y filtrar 2007

> 🟢 Step two: explore the data.

> 🖱️ I'm scrolling down below the table, and clicking the plus Code button in the toolbar at the top left, to add the third code cell.

> 🟢 This third code cell checks the size of the table with shape, and the columns and data types with info.

> 🖱️ I'm typing shape and info in the third code cell.

**Celda 3:**

```python
print(df.shape)
df.info()
```

> 🖱️ I'm clicking the Run cell button on the left of the third code cell, to see the structure.

> 🖱️ I'm pointing at the first line of the output, under the third code cell.

> 🟢 1,704 rows and 8 columns.

> 🖱️ I'm moving the mouse down the Non-Null Count column in the info output, in the middle of the screen.

> 🟢 Every column has 1,704 non-null values, so nothing is missing, and the numeric columns are already numbers, which Plotly needs for the axes.

> 🟢 Each country appears twelve times, once per year, so the chart would be crowded. For the main chart I'll keep only the most recent year, 2007.

> 🖱️ I'm scrolling down to the end of the info output, and clicking the plus Code button in the toolbar at the top left, to add the fourth code cell.

> 🟢 This fourth code cell keeps only the rows of 2007 in a new table, df_2007, and prints its size.

> 🖱️ I'm typing the filter in the fourth code cell.

**Celda 4:**

```python
df_2007 = df[df["year"] == 2007]
print(df_2007.shape)
```

> 🖱️ I'm clicking the Run cell button on the left of the fourth code cell, to filter the data.

> 🖱️ I'm pointing at the result under the fourth code cell.

> 🟢 142 rows: one per country, exactly as expected.

---

## 5:30–7:30 — Paso 3: primer gráfico, simple

> 🟢 Step three: a first, simple chart.

> 🖱️ I'm scrolling down to the end of the fourth code cell, and clicking the plus Code button in the toolbar at the top left, to add the fifth code cell.

> 🟢 This fifth code cell draws a scatter plot with px.scatter: GDP per capita on the x axis, life expectancy on the y axis, one color per continent, and the country name in the tooltip.

> 🖱️ I'm typing the scatter plot in the fifth code cell.

**Celda 5:**

```python
fig = px.scatter(df_2007, x="gdpPercap", y="lifeExp", color="continent", hover_name="country")
fig.show()
```

> 🖱️ I'm clicking the Run cell button on the left of the fifth code cell, to draw the first chart.

> 🖱️ I'm moving the mouse over one of the points on the right side of the chart, to see its tooltip.

> 🟢 The chart is already interactive, with no extra code: the tooltip shows the country in bold and its values.

> 🖱️ I'm pointing at the bottom left corner of the chart, where most points are crowded.

> 🟢 But there are problems. Most countries are squeezed on the left, under ten thousand dollars. All points have the same size, so I can't see population. And the axis titles are raw column names.

---

## 7:30–9:30 — Paso 4: consultar la documentación de Plotly

**Solo si el Goal pide consultar la documentación.** Si no, salteá este paso.

> 🟢 Step four: the documentation. I don't know yet which Plotly options fix this, so I'll check the official page for bubble charts, which are scatter plots where the size shows a third value.

> 🖱️ I'm pressing Command + T to open a new tab in this Firefox window.

> 🖱️ I'm typing plotly.com/python/bubble-charts in the address bar at the top, and pressing Return.

> 🖱️ I'm scrolling down to the first Plotly Express example, near the top of the page, to read its code.

> 🟢 This example uses the same Gapminder data for 2007. It adds what I need: size equals pop for the bubble size, log_x equals True for a logarithmic x axis, and size_max for the largest bubble.

> 🟢 A logarithmic axis multiplies by ten at each step: one thousand, ten thousand, a hundred thousand. That spreads out the countries squeezed on the left.

> 🖱️ I'm clicking the Colab tab at the top of the window, to go back to my notebook.

---

## 9:30–12:00 — Paso 5: gráfico mejorado

> 🟢 Step five: the improved chart.

> 🖱️ I'm scrolling down to the end of the first chart, and clicking the plus Code button in the toolbar at the top left, to add the sixth code cell.

> 🟢 This sixth code cell draws the same scatter plot, adding the bubble size by population, a logarithmic x axis, a title, and clear names for the two axes with labels.

> 🖱️ I'm typing the improved chart in the sixth code cell.

**Celda 6:**

```python
fig = px.scatter(df_2007, x="gdpPercap", y="lifeExp", color="continent", hover_name="country",
                 size="pop", size_max=60, log_x=True, title="Life Expectancy vs. GDP per Capita (2007)",
                 labels={"gdpPercap": "GDP per capita (USD)", "lifeExp": "Life expectancy (years)"})
fig.show()
```

> 🖱️ I'm clicking the Run cell button on the left of the sixth code cell, to draw the improved chart.

> 🖱️ I'm moving the mouse along the x axis, at the bottom of the chart, from one thousand to ten thousand.

> 🟢 Now the countries are spread out along the x axis.

> 🖱️ I'm pointing at the two largest bubbles, in the middle of the chart.

> 🟢 The bubble size shows population, so China and India are the biggest. And the title and the axis names are clear.

> 🖱️ I'm moving the mouse along the cloud of bubbles, from the bottom left to the top right.

> 🟢 The pattern is clear: richer countries tend to live longer, and on a log scale the bubbles form almost a straight line.

---

## 12:00–15:30 — Paso 6: probar las interacciones

> 🟢 Step six: testing the interactions.

> 🖱️ I'm moving the mouse over the largest bubble, in the middle of the chart, to see its tooltip.

> 🟢 China, Asia, about 4,959 dollars, 73 years, and 1.3 billion people. The tooltip uses my new axis names.

> 🖱️ I'm moving the mouse to the lowest bubbles, at the bottom of the chart.

> 🟢 This one is Swaziland, with about 40 years, the lowest in the data.

> 🖱️ I'm clicking Africa in the legend, on the right side of the chart, to hide that continent.

> 🟢 One click hides a group: the African bubbles disappeared, and Africa is greyed out in the legend.

> 🖱️ I'm clicking Africa in the legend again, to show it back.

> 🖱️ I'm double-clicking Europe in the legend, on the right, to show only Europe.

> 🟢 A double click isolates one group, to compare countries inside one continent.

> 🖱️ I'm double-clicking Europe in the legend again, to bring back all the continents.

> 🖱️ I'm moving the mouse to the top right corner of the chart, to show Plotly's toolbar, the modebar.

> 🖱️ I'm dragging a box with the mouse around the bubbles on the right side of the chart, to zoom in on the richest countries.

> 🟢 The axes adjust to that area, and the bubbles that overlapped are now separated.

> 🖱️ I'm clicking the Pan icon, the cross with four arrows in the modebar at the top right, and dragging the chart to move the view.

> 🖱️ I'm clicking the Reset axes icon, the house in the modebar at the top right, to go back to the full chart.

> 🖱️ I'm clicking the Zoom icon, the magnifying glass in the modebar, so dragging zooms again.

> 🖱️ I'm clicking the camera icon, the first one in the modebar at the top right, to download the chart as a PNG image.

> 🖱️ I'm clicking the Downloads arrow at the top right of Firefox, to check the file.

> 🟢 newplot.png is downloaded. A PNG is a static picture, so it loses the interactions.

> 🖱️ I'm clicking an empty area of the page, to close the Downloads panel.

---

## 15:30–17:30 — Paso 7 (opcional): gráfico animado de 1952 a 2007

> 🟢 Step seven: an animated chart, to see the change over time.

> 🖱️ I'm scrolling down to the end of the improved chart, and clicking the plus Code button in the toolbar at the top left, to add the seventh code cell.

> 🟢 This seventh code cell uses the full data, with every year. animation_frame turns each year into a frame, and the fixed ranges keep the axes still between years.

> 🖱️ I'm typing the animated chart in the seventh code cell.

**Celda 7:**

```python
fig_anim = px.scatter(df, x="gdpPercap", y="lifeExp", color="continent", hover_name="country",
                      size="pop", size_max=60, log_x=True,
                      animation_frame="year", range_x=[100, 150000], range_y=[20, 90])
fig_anim.show()
```

> 🖱️ I'm clicking the Run cell button on the left of the seventh code cell, to draw the animated chart.

> 🖱️ I'm clicking the play button, the triangle at the bottom left of the chart, to start the animation.

> 🟢 The bubbles move up and to the right: almost every country gets richer and lives longer. Africa's median goes from about 39 years in 1952 to about 53 in 2007.

> 🖱️ I'm dragging the year slider, below the chart, back to 1952, to compare the first and the last year.

---

## 17:30–19:30 — Paso 8: guardar el gráfico, conclusiones y descargar

> 🟢 Step eight: save the chart and write the conclusions.

> 🖱️ I'm scrolling down to the end of the last chart, and clicking the plus Code button in the toolbar at the top left, to add the eighth code cell.

> 🟢 This eighth code cell saves the 2007 chart as an HTML file, which, unlike the PNG, keeps every interaction and opens in any browser.

> 🖱️ I'm typing the save line in the eighth code cell.

**Celda 8:**

```python
fig.write_html("life_expectancy_2007.html")
```

> 🖱️ I'm clicking the Run cell button on the left of the eighth code cell, to save the file.

> 🖱️ I'm clicking the Files icon, the folder in the left sidebar, to check the file.

> 🖱️ I'm clicking the three dots next to life_expectancy_2007.html, in the left panel, and choosing Download.

> 🖱️ I'm clicking the Files icon in the left sidebar again, to close the panel.

> 🖱️ I'm scrolling down to the end of the notebook, and clicking the plus Text button in the toolbar at the top left, to add the conclusions cell.

> 🟢 This last cell sums up what the chart shows and the interactions I checked.

> 🖱️ I'm typing the conclusions in the new text cell, at the bottom of the notebook.

```markdown
## Conclusions
- In 2007, richer countries tend to live longer, but life expectancy rises fast at low incomes and flattens at high incomes.
- Africa has the lowest median life expectancy (about 53 years); Europe and Oceania the highest (about 79 and 81).
- Exceptions: South Africa, Botswana, and Equatorial Guinea have a GDP per capita above $9,000 but live around 50 years.
- Interactions checked: hover, legend (hide and isolate), zoom, pan, reset, and PNG download. The HTML file keeps them all.
```

> 🖱️ I'm clicking the empty area below the conclusions cell, to close the editor and show the formatted text.

> 🖱️ I'm pressing Command + S to save the notebook in Drive.

> 🖱️ I'm opening the File menu at the top left, choosing Download, then Download .ipynb, to keep the notebook for the deliverables.

> 🖱️ I'm clicking the Downloads arrow at the top right of Firefox, to show the notebook, the HTML, and the PNG.

---

## 19:30–22:30 — Epílogo

Dura **de 2 a 4 minutos**: enfoque, desafíos y reflexiones.

> 🖱️ I'm clicking an empty area of the page to close the Downloads panel, and scrolling up to the top of the notebook with the mouse wheel, to go over the whole analysis.

> 🟢 Let me summarize. I checked that Plotly was installed in Colab, loaded the Gapminder sample data, and confirmed it had 1,704 rows and no missing values. Then I kept only 2007, one row per country.

> 🖱️ I'm scrolling down to the fifth and sixth code cells, the two charts.

> 🟢 The first chart worked but was hard to read. With size, log_x, title, and labels, the improved chart shows the pattern clearly: richer countries tend to live longer.

> 🖱️ I'm scrolling down to the seventh and eighth code cells, the animation and the saved file.

> 🟢 I tested every interaction, animated the data from 1952 to 2007, and saved the chart as HTML, which keeps the interactions.

> 🖱️ I'm scrolling down to the conclusions cell, at the bottom of the notebook.

> 🟢 What I learned: with Plotly Express, one function call gives a full interactive chart, and each option is just a column name. I didn't write any code for hover, zoom, or the legend.

> 🟢 There were two challenges. The first chart squeezed most countries on the left, because a few are very rich, and a logarithmic x axis fixed it. And in the animation, the axes jumped every year, so I fixed their ranges with range_x and range_y.

> 🟢 One limit: this is a practice dataset that ends in 2007, and a scatter plot shows a relationship, not a cause. As a next step, I could also rename pop and continent in labels, so the whole tooltip is clean, or try a map with px.choropleth. Thanks for watching!

Si el reloj todavía no pasó los 15:00 (no debería pasar), no cortes: pasá el mouse por las tres excepciones (South Africa, Botswana, Equatorial Guinea) y leé sus tooltips.

---

## Si algo sale mal (frases para corregir)

Siempre decí **qué** corregís y **en qué celda**:

| Error | Qué pasa | Qué decís y hacés |
| ----- | -------- | ----------------- |
| `ValueError` con un nombre de columna | Escribiste mal `"gdpPercap"` o `"lifeExp"` (son sensibles a mayúsculas) | 🖱️ *"There's a ValueError in the sixth code cell, because I typed gdppercap in lowercase. I'm clicking on that line, fixing the capital P, and clicking Run again."* |
| `NameError: name 'px' is not defined` (o `df_2007`, `fig`) | Una celda anterior no se ejecutó | 🖱️ *"There's a NameError in this cell, because an earlier cell didn't run. I'm opening the Runtime menu at the top and choosing Run before, to run all the cells above it."* |
| El gráfico no aparece | La celda terminó sin error pero no se ve | 🖱️ *"The chart didn't show. I'm clicking Run again on the left of this cell."* |
| Error de sintaxis (paréntesis o comilla de menos) | `SyntaxError` | 🖱️ *"There's a syntax error in this cell, a missing parenthesis on the line Colab underlines. I'm adding it and running the cell again."* |
| Cualquier cosa fuera del guion | Un aviso, una ventana | 🖱️ *"I'm closing this notification at the bottom left, to keep working."* |

---

## Después de grabar

1. Ejecutá **Run full AutoQC**, no solo *Rerun failing*. Revisá que el porcentaje de acciones con What + Where pase el **70%**.
2. Armá **Deliverables.zip** con `plotly_gapminder.ipynb` (el que descargaste al final), `life_expectancy_2007.html` y, si las reglas lo permiten, `newplot.png`.
3. Subí los **cuatro archivos por separado**: el **MP4**, el **ZIP original de TaskRecorder**, **Deliverables.zip** y **Metadata.rtf**.
