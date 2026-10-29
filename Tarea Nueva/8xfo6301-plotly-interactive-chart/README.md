# 8xfo6301 — Gráfico interactivo con Plotly en Google Colab

Guion paso a paso para grabar la tarea **8xfo6301**: aprender a usar **Plotly**, una biblioteca nueva, en **Google Colab**, y crear un **gráfico interactivo** a partir de un dataset de ejemplo. Cuando hace falta, se consulta la **documentación oficial de Plotly** desde **Firefox**. La grabación tiene que ser **continua** y durar **entre 15:00 y 50:59**. Este guion apunta a unos **27 minutos**, con un epílogo de unos 3 minutos.

**Cómo leer este guion:**

- Cada sección tiene tres partes: **Acción en pantalla**, **Narración exacta en inglés** y **Resultado esperado**. No pases a la sección siguiente hasta ver el resultado esperado.
- Las frases que empiezan con 🖱️ las decís **en el momento de hacer clic, desplazarte o escribir**. Siempre dicen **qué** elemento usás, **dónde** está en la pantalla y **por qué**. Son las que revisa AutoQC.
- Las frases que empiezan con 🟢 son la explicación que decís entre una acción y otra.
- Debajo de cada bloque de código, la lista **What each line does** explica cada línea en inglés. La leés en voz alta mientras escribís esa línea.
- Las traducciones al castellano van entre paréntesis y **no se leen**.
- Hacé una pausa de **~1 segundo después de cada clic**, y nunca te quedes **más de 45 segundos en silencio**. Si Colab tarda, seguí explicando lo que acabás de escribir.

> **Importante:** el Goal aprobado y las reglas vigentes de Odin tienen prioridad sobre este guion. **No tuve el texto del Goal**, así que este guion es un **borrador**: revisá los pendientes de abajo antes de grabar.

---

## Pendientes antes de grabar (datos que faltan en la consigna)

| Dato | Lo que supuse | Qué hacer |
| ---- | ------------- | --------- |
| **Texto del Goal aprobado** | No lo tengo. Lo resumí como *"usar Plotly en Google Colab para crear un gráfico interactivo a partir de un dataset de ejemplo"*. | Pasame el Goal (sin el Approval ID) y ajusto la frase del Goal, el plan y el epílogo a lo que dice. |
| **Dataset** | Uso **Gapminder**, que viene dentro de Plotly (`px.data.gapminder()`). No hay que descargar ni subir nada, y no tiene datos personales. | Si el Goal nombra otro dataset (por ejemplo, un CSV o `iris`/`tips`), avisame y cambio las celdas de carga y los números. |
| **Tipo de gráfico** | Un gráfico de dispersión con burbujas (*bubble chart*): PIB per cápita contra esperanza de vida en 2007. | Si el Goal pide otro tipo (barras, líneas, mapa), avisame. |
| **Gráfico animado (sección 21:00)** | Lo marqué como **opcional**. Suma un segundo gráfico, con un solo parámetro nuevo. | Si el Goal pide un solo gráfico, saltealo. La grabación igual pasa de los 15:00. |
| **Entregables** | El notebook `.ipynb` y el gráfico como `.html` interactivo. | Confirmá en las reglas de Odin qué archivos van en Deliverables.zip. |
| **Epílogo** | Menos de 4 minutos: decisiones, verificación, límites y próximos pasos. | Si las reglas de Odin piden otro contenido, ajustá ese texto. |
| **Versión de Plotly en Colab** | Probé el código con Plotly 7.1 y pandas 3.1, y es compatible con Plotly 5 y 6. | Decí el número que muestre **tu** celda, no el de este guion. |

---

## Archivos de la carpeta

```
8xfo6301-plotly-interactive-chart/
├── README.md               ← este guion
└── plotly_gapminder.ipynb  ← notebook de referencia, completo y en orden (sin ejecutar)
```

Para ensayar: en https://colab.research.google.com elegís **File → Upload notebook**, seleccionás `plotly_gapminder.ipynb` y ejecutás **Runtime → Run all**. **No lo uses en la grabación**: en el video el notebook se crea desde cero y el código se escribe, no se pega.

---

## El dataset (verificado)

**Gapminder**, la versión que trae Plotly con `px.data.gapminder()`. Plotly la usa en los ejemplos de su documentación. Son datos públicos de la Fundación Gapminder, por país.

- **1.704 filas y 8 columnas**: 142 países, 5 continentes y 12 años (de 1952 a 2007, cada 5 años).
- **No tiene valores faltantes.**
- Filtrado a **2007**: **142 filas**, una por país.

| Columna | Qué contiene | Dónde se usa |
| ------- | ------------ | ------------ |
| `country` | País | Nombre en negrita del tooltip (`hover_name`) |
| `continent` | Africa, Americas, Asia, Europe, Oceania | Color de cada punto |
| `year` | Año, de 1952 a 2007 | Filtro de 2007 y animación |
| `lifeExp` | Esperanza de vida, en años | Eje Y |
| `pop` | Población | Tamaño de la burbuja |
| `gdpPercap` | PIB per cápita, en dólares ajustados por inflación | Eje X |
| `iso_alpha`, `iso_num` | Códigos del país | No se usan |

**Valores de referencia de 2007** (calculados con el dataset, el 29/10/2026). Usalos para comprobar lo que ves en el tooltip:

| Dato | Valor |
| ---- | ----- |
| Países por continente | Africa 52, Asia 33, Europe 30, Americas 25, Oceania 2 (Australia y New Zealand) |
| Mediana de esperanza de vida | Africa 52,9 · Asia 72,4 · Americas 72,9 · Europe 78,6 · Oceania 80,7 |
| Burbujas más grandes | China (1.319 millones; PIB 4.959; 73,0 años) e India (1.110 millones; PIB 2.452; 64,7 años) |
| PIB per cápita más alto | Norway 49.357 · Kuwait 47.307 · Singapore 47.143 |
| PIB per cápita más bajo | Congo, Dem. Rep. 278 (46,5 años) |
| Esperanza de vida más alta | Japan 82,6 · Hong Kong, China 82,2 · Iceland 81,8 |
| Esperanza de vida más baja | Swaziland 39,6 · Mozambique 42,1 · Zambia 42,4 |
| Excepciones (PIB alto, vida corta) | South Africa (9.270; 49,3), Botswana (12.570; 50,7), Equatorial Guinea (12.154; 51,6) |
| United States | PIB 42.952; 78,2 años |
| Mediana de Africa, 1952 → 2007 | 38,8 → 52,9 años (Europe: 65,9 → 78,6) |

---

## Antes de grabar

1. **Goal en Google Docs.** Pegá el Goal aprobado en un documento de Google Docs. **Borrá el Approval ID** y cualquier nombre, correo o dato personal. Ponele un título neutro, por ejemplo `8xfo6301 – Goal`. Agrandá el texto o el zoom (`Ctrl + +`) hasta que se lea completo **sin desplazarte**, o con un solo desplazamiento.
2. **Datos personales en pantalla.** Arriba a la derecha de Google Docs y de Colab aparece la foto o la inicial de tu cuenta de Google. Revisá que no se vea tu nombre ni tu correo. **No hagas clic** en ese ícono durante la grabación.
3. **IA de Colab.** Colab trae funciones de IA (Gemini y el texto *"Start coding or generate with AI"* en las celdas vacías). Antes de grabar, entrá a **Tools → Settings → AI assistance** y activá la opción para ocultar las funciones de IA generativa, si está disponible. Durante la grabación **no uses ninguna herramienta de IA**.
4. **Firefox, con dos pestañas en este orden:**
   1. el documento de Google Docs con el Goal;
   2. Google Colab (https://colab.research.google.com), con el cuadro **Open notebook** a la vista y sin crear todavía el notebook.

   La documentación de Plotly **no** la dejes abierta: la abrís durante la grabación, cuando surge la duda. Maximizá Firefox y dejá seleccionada la **primera pestaña** (el Goal).
5. Iniciá sesión en Google en Firefox antes de grabar, porque Colab la necesita para ejecutar código.
6. Cerrá las demás ventanas, también este guion si está en la misma pantalla, para que ninguna ventana tape a otra. Usá solo Firefox (Google Docs, Colab y plotly.com).
7. Ensayá una vez entera en un notebook nuevo, leyendo en voz alta todas las frases 🖱️ y 🟢, y cronometrá. Anotá la versión de Plotly que te muestra Colab.
8. Para que no suba el porcentaje de escritura, ejecutá las celdas con el **botón Run** (mouse) y escribí solo el código y los títulos cortos. Las celdas de texto largas son pocas y las vas diciendo en voz alta mientras escribís.
9. Antes de afirmar algo en voz alta (*"it works"*, *"it was saved"*), **miralo en pantalla**. Si algo falla, decilo y arreglalo frente a la cámara: eso también es parte del flujo real.

---

## 0:00–0:20 — Introducción con el Goal en pantalla

**Acción en pantalla:**

1. La grabación arranca con Firefox maximizado en la **primera pestaña**: el Goal en Google Docs, completo y legible.
2. No hagas clic en nada. Dejá el mouse quieto, a un costado del texto.

**Narración exacta en inglés (menos de 20 segundos):**

> 🟢 I will be beginning my task soon. Here is the workflow I have in mind.
>
> (Voy a empezar mi tarea en breve. Este es el flujo de trabajo que tengo en mente.)
>
> 🟢 On screen is the approved Goal, in Google Docs in Firefox: use Plotly in Google Colab to create an interactive chart from a sample dataset.
>
> (En pantalla está el Goal aprobado, en Google Docs en Firefox: usar Plotly en Google Colab para crear un gráfico interactivo a partir de un dataset de ejemplo.)

Ajustá la segunda frase al texto exacto de tu Goal.

**Resultado esperado:** el Goal se leyó completo y no aparece ningún Approval ID ni dato personal.

---

## 0:20–2:00 — El plan de trabajo

**Acción en pantalla:** seguís en el Goal. Si el texto no entra entero, bajás despacio con la rueda del mouse.

**Narración exacta en inglés:**

> 🖱️ I'm scrolling down the Goal document with the mouse wheel, to show the rest of the text.
>
> (Bajo por el documento del Goal con la rueda del mouse, para mostrar el resto del texto.)
>
> 🟢 Plotly is a library I'm learning for this task, so I'll work step by step and check the official documentation when I need it.
>
> (Plotly es una librería que estoy aprendiendo para esta tarea, así que voy a trabajar paso a paso y consultar la documentación oficial cuando la necesite.)
>
> 🟢 Here's the plan. First, in Google Colab, I'll create a new notebook and check that Plotly is available. If it isn't, I'll install it.
>
> (Este es el plan. Primero, en Google Colab, voy a crear un notebook nuevo y comprobar que Plotly está disponible. Si no está, lo instalo.)
>
> 🟢 Second, I'll load a sample dataset. Plotly comes with a few small datasets for practice. I'll use Gapminder, which has life expectancy, population, and GDP per capita for 142 countries, from 1952 to 2007.
>
> (Segundo, voy a cargar un dataset de ejemplo. Plotly trae algunos datasets chicos para practicar. Voy a usar Gapminder, que tiene esperanza de vida, población y PIB per cápita de 142 países, de 1952 a 2007.)
>
> 🟢 Third, I'll make a first, simple chart, and see what needs to improve. Then I'll go to the Plotly documentation in Firefox, to learn the options that fix it.
>
> (Tercero, voy a hacer un primer gráfico simple y ver qué hay que mejorar. Después voy a ir a la documentación de Plotly en Firefox, para aprender las opciones que lo arreglan.)
>
> 🟢 Fourth, I'll build the improved chart and test every interaction: the hover tooltip, the legend, zoom, pan, reset, and downloading the chart as an image.
>
> (Cuarto, voy a armar el gráfico mejorado y probar cada interacción: el tooltip al pasar el mouse, la leyenda, el zoom, el desplazamiento, el reinicio y la descarga del gráfico como imagen.)
>
> 🟢 Finally, I'll save the chart as an interactive HTML file, download the notebook, and sum up what I learned.
>
> (Por último, voy a guardar el gráfico como un archivo HTML interactivo, descargar el notebook y resumir lo que aprendí.)

**Resultado esperado:** el plan quedó dicho y seguís en la pestaña del Goal.

---

## 2:00–4:30 — Abrir Colab y crear el notebook

**Acción en pantalla:**

1. Hacés clic en la **segunda pestaña** (Colab).
2. Hacés clic en **New notebook**, abajo del cuadro **Open notebook**.
3. Cambiás el título del notebook.
4. Agregás una celda de texto con el título.

**Narración exacta en inglés:**

> 🖱️ I'm clicking the second browser tab, at the top of the window, to open Google Colab.
>
> (Hago clic en la segunda pestaña del navegador, arriba de la ventana, para abrir Google Colab.)
>
> 🟢 Google Colab is a free Google tool that runs Python notebooks in the browser. The code runs on a computer in Google's cloud, so I don't need to install Python on my laptop.
>
> (Google Colab es una herramienta gratuita de Google que ejecuta notebooks de Python en el navegador. El código corre en una computadora en la nube de Google, así que no necesito instalar Python en mi laptop.)
>
> 🖱️ I'm clicking the New notebook button, at the bottom of the Open notebook dialog, to start a fresh notebook.
>
> (Hago clic en el botón New notebook, abajo del cuadro Open notebook, para empezar un notebook nuevo.)

Si no aparece el cuadro: *"I'm opening the File menu at the top left and choosing New notebook, to start a fresh notebook."*

> 🟢 A notebook is a list of cells. Code cells run Python, and text cells hold titles and notes. The result of each code cell appears right below it, so I can check every step before moving on.
>
> (Un notebook es una lista de celdas. Las celdas de código ejecutan Python y las de texto tienen títulos y notas. El resultado de cada celda de código aparece justo debajo, así puedo comprobar cada paso antes de seguir.)
>
> 🖱️ I'm pointing at the plus Code and plus Text buttons in the toolbar at the top left, which add each kind of cell.
>
> (Señalo los botones + Code y + Text de la barra de herramientas, arriba a la izquierda, que agregan cada tipo de celda.)
>
> 🖱️ I'm pointing at the play icon on the left side of the empty cell, which runs the cell.
>
> (Señalo el ícono de play a la izquierda de la celda vacía, que ejecuta la celda.)
>
> 🖱️ I'm clicking the notebook title at the top left, Untitled0, and typing plotly_gapminder, to give the notebook a clear name.
>
> (Hago clic en el título del notebook, arriba a la izquierda, Untitled0, y escribo plotly_gapminder, para darle un nombre claro al notebook.)
>
> 🖱️ I'm clicking the plus Text button in the toolbar at the top left, to add a text cell with the title and the goal.
>
> (Hago clic en el botón + Text de la barra de herramientas, arriba a la izquierda, para agregar una celda de texto con el título y el objetivo.)

Escribís:

```markdown
# Interactive Chart with Plotly
Dataset: Gapminder, built into Plotly. Goal: build an interactive chart of life expectancy vs. GDP per capita and test its interactions.
```

**What each line does:**

- 🟢 `# Interactive Chart with Plotly`: the hash sign makes this line the main title of the notebook.
- 🟢 `Dataset: ... Goal: ...`: this line says which data I'm using and what I want to build, so anyone who opens the notebook understands it.

> 🖱️ I'm clicking outside the text cell, on the empty area below it, to close the editor and see the formatted title.
>
> (Hago clic fuera de la celda de texto, en el área vacía de abajo, para cerrar el editor y ver el título con formato.)

Un notebook nuevo trae una celda de código vacía, así que el título queda debajo de ella. Lo subís:

> 🖱️ I'm clicking the Move cell up arrow, in the small toolbar at the top right of the text cell, to put the title at the very top of the notebook.
>
> (Hago clic en la flecha Move cell up, en la barra chica arriba a la derecha de la celda de texto, para poner el título al principio del notebook.)

La celda de código vacía queda debajo del título: la usás para la celda 1 (hacés clic adentro en vez de usar **+ Code**, y decís *"I'm clicking inside the empty code cell below the title, to check whether Plotly is installed."*).

**Resultado esperado:** notebook llamado `plotly_gapminder.ipynb`, con el título en negrita.

---

## 4:30–7:00 — Comprobar Plotly y cargar el dataset

**Acción en pantalla:** dos celdas de código. Ejecutás cada una con su botón de play.

**Narración exacta en inglés:**

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell below the title and check whether Plotly is installed.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código debajo del título y comprobar si Plotly está instalado.)

Escribís la **celda 1**:

```python
import plotly
print(plotly.__version__)
```

**What each line does:**

- 🟢 `import plotly`: this loads the Plotly library. If it isn't installed, this line gives an error called ModuleNotFoundError.
- 🟢 `print(plotly.__version__)`: this prints the installed version, so I know which documentation to follow.

> 🖱️ I'm clicking the Run cell button, the play icon to the left of this cell, to run the check.
>
> (Hago clic en el botón Run cell, el ícono de play a la izquierda de esta celda, para ejecutar la comprobación.)
>
> 🟢 The first run takes a few seconds, because Colab is connecting to the computer in Google's cloud, called the runtime. You can see the indicator at the top right changing.
>
> (La primera ejecución tarda unos segundos, porque Colab se está conectando a la computadora en la nube de Google, llamada runtime. Se ve cómo cambia el indicador arriba a la derecha.)
>
> 🟢 The cell printed version [tu número]. So Plotly is already installed in Colab, and I don't need to install anything. If this had failed, I would add a cell with exclamation mark pip install plotly. The exclamation mark runs a terminal command from the notebook.
>
> (La celda mostró la versión [tu número]. O sea que Plotly ya está instalado en Colab y no necesito instalar nada. Si hubiera fallado, agregaría una celda con signo de exclamación pip install plotly. El signo de exclamación ejecuta un comando de terminal desde el notebook.)

Si de verdad aparece `ModuleNotFoundError`: agregás una celda con `!pip install plotly`, la ejecutás, decís qué ves y volvés a ejecutar la celda 1.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a new code cell and load the sample dataset.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código nueva y cargar el dataset de ejemplo.)

Escribís la **celda 2**:

```python
import plotly.express as px

df = px.data.gapminder()
df.head()
```

**What each line does:**

- 🟢 `import plotly.express as px`: Plotly Express is the simple part of Plotly. It makes a full chart with one function call. px is the short name everyone uses, also in the official docs.
- 🟢 `df = px.data.gapminder()`: px.data has small sample datasets for practice. gapminder returns the data as a pandas DataFrame, which is a table with rows and columns. I store it in df.
- 🟢 `df.head()`: head shows the first five rows. Because it's the last line of the cell, Colab displays it as a table, without print.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to load the data and show the first rows.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para cargar los datos y mostrar las primeras filas.)
>
> 🟢 Here are the first five rows, all for Afghanistan, from 1952 onward. Each row is one country in one year. I can see the columns country, continent, year, lifeExp for life expectancy, pop for population, and gdpPercap for GDP per capita.
>
> (Acá están las primeras cinco filas, todas de Afganistán, desde 1952. Cada fila es un país en un año. Veo las columnas country, continent, year, lifeExp para la esperanza de vida, pop para la población y gdpPercap para el PIB per cápita.)

**Resultado esperado:** una tabla con 5 filas de Afghanistan y 8 columnas.

---

## 7:00–9:30 — Explorar los datos y filtrar 2007

**Acción en pantalla:** un título de sección y dos celdas de código.

**Narración exacta en inglés:**

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading called Explore the data.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección llamado Explore the data.)

Escribís `## 1. Explore the data`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that checks the size and the types of the data.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que revisa el tamaño y los tipos de los datos.)

Escribís la **celda 3**:

```python
print(df.shape)
df.info()
```

**What each line does:**

- 🟢 `print(df.shape)`: shape gives the number of rows and columns.
- 🟢 `df.info()`: info lists every column, how many non-empty values it has, and its data type.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to see the structure of the data.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para ver la estructura de los datos.)
>
> 🟢 We have 1,704 rows and 8 columns. Every column shows 1,704 non-null values, so there are no missing values, and no cleaning is needed. The numeric columns, like lifeExp and gdpPercap, are already numbers, which Plotly needs for the axes.
>
> (Tenemos 1.704 filas y 8 columnas. Todas las columnas muestran 1.704 valores no nulos, así que no hay valores faltantes y no hace falta limpiar. Las columnas numéricas, como lifeExp y gdpPercap, ya son números, que es lo que Plotly necesita para los ejes.)

Decí *"no missing values"* solo si todas las columnas muestran `1704 non-null`.

> 🟢 The data has twelve years for each country. If I plot all of them at once, each country appears twelve times, and the chart gets crowded. So for the main chart I'll keep only the most recent year, 2007.
>
> (Los datos tienen doce años para cada país. Si grafico todos juntos, cada país aparece doce veces y el gráfico se satura. Así que para el gráfico principal me quedo solo con el año más reciente, 2007.)
>
> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that filters the year 2007.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que filtra el año 2007.)

Escribís la **celda 4**:

```python
df_2007 = df[df["year"] == 2007]
print(df_2007.shape)
```

**What each line does:**

- 🟢 `df_2007 = df[df["year"] == 2007]`: the condition inside the brackets is True for the rows where year is 2007, and the brackets keep only those rows. I store them in a new table, df_2007, so the full data stays unchanged for later.
- 🟢 `print(df_2007.shape)`: this checks how many rows are left.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to filter the data.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para filtrar los datos.)
>
> 🟢 It shows 142 rows and 8 columns: one row per country, which is exactly what I expected.
>
> (Muestra 142 filas y 8 columnas: una fila por país, que es justo lo que esperaba.)

**Resultado esperado:** `(1704, 8)` en la celda 3 y `(142, 8)` en la celda 4.

---

## 9:30–11:30 — Primer gráfico, simple

**Acción en pantalla:** un título de sección y una celda de código. Mirás el gráfico y señalás el problema con el mouse.

**Narración exacta en inglés:**

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for the first chart.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para el primer gráfico.)

Escribís `## 2. First chart`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell for a first, simple scatter plot.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código para un primer gráfico de dispersión simple.)

Escribís la **celda 5**:

```python
fig = px.scatter(df_2007, x="gdpPercap", y="lifeExp", color="continent", hover_name="country")
fig.show()
```

**What each line does:**

- 🟢 `fig = px.scatter(...)`: px.scatter makes a scatter plot, where each country is one point. I pass the table and the column names: GDP per capita on the x axis, life expectancy on the y axis, a different color for each continent, and the country name as the title of the tooltip. The chart is stored in a variable called fig, short for figure.
- 🟢 `fig.show()`: this displays the chart below the cell.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to draw the first chart.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para dibujar el primer gráfico.)
>
> 🟢 The chart is already interactive, without any extra code. Let me hover over one point.
>
> (El gráfico ya es interactivo, sin código extra. Paso el mouse por un punto.)
>
> 🖱️ I'm moving the mouse over one of the points on the right side of the chart, to see its tooltip.
>
> (Muevo el mouse sobre uno de los puntos del lado derecho del gráfico, para ver su tooltip.)
>
> 🟢 The tooltip shows the country name in bold, and its values. That's what hover_name does.
>
> (El tooltip muestra el nombre del país en negrita y sus valores. Eso es lo que hace hover_name.)
>
> 🖱️ I'm pointing at the bottom left corner of the chart, where most points are crowded.
>
> (Señalo la esquina inferior izquierda del gráfico, donde se amontonan la mayoría de los puntos.)
>
> 🟢 But there's a problem. Most countries are squeezed on the left, under ten thousand dollars, while a few rich countries go up to almost fifty thousand. So it's hard to compare the poorer countries. Also, all points have the same size, so I can't see which countries have more people. And the axis titles are the raw column names, like gdpPercap.
>
> (Pero hay un problema. La mayoría de los países están apretados a la izquierda, por debajo de diez mil dólares, mientras que unos pocos países ricos llegan a casi cincuenta mil. Así es difícil comparar los países más pobres. Además, todos los puntos tienen el mismo tamaño, así que no veo qué países tienen más habitantes. Y los títulos de los ejes son los nombres crudos de las columnas, como gdpPercap.)
>
> 🟢 I don't know yet which Plotly options fix this, so I'll check the official documentation.
>
> (Todavía no sé qué opciones de Plotly arreglan esto, así que voy a consultar la documentación oficial.)

**Resultado esperado:** un gráfico de puntos de 5 colores, con la leyenda **continent** a la derecha y casi todos los puntos amontonados a la izquierda.

---

## 11:30–14:30 — Consultar la documentación oficial de Plotly en Firefox

**Acción en pantalla:**

1. Abrís una pestaña nueva con `Ctrl + T`.
2. Escribís `plotly.com/python` y apretás `Enter`.
3. Buscás **Bubble Charts** (en la sección *Basic Charts*) y entrás.
4. Mostrás el primer ejemplo de Plotly Express.
5. Abrís la referencia de `px.scatter` y buscás `log_x` y `labels`.
6. Volvés a la pestaña de Colab.

**Narración exacta en inglés:**

> 🖱️ I'm pressing Control and T, to open a new browser tab for the Plotly documentation.
>
> (Aprieto Control y T, para abrir una pestaña nueva del navegador para la documentación de Plotly.)
>
> 🖱️ I'm typing plotly dot com slash python in the address bar at the top, and pressing Enter, to open the official Plotly documentation for Python.
>
> (Escribo plotly punto com barra python en la barra de direcciones, arriba, y aprieto Enter, para abrir la documentación oficial de Plotly para Python.)
>
> 🟢 This is the official Plotly Python documentation. It's organized by chart type, and each page has short examples I can adapt.
>
> (Esta es la documentación oficial de Plotly para Python. Está organizada por tipo de gráfico, y cada página tiene ejemplos cortos que puedo adaptar.)
>
> 🟢 A scatter plot where the size of each point shows a third value is called a bubble chart. So I'll look for that page.
>
> (Un gráfico de dispersión donde el tamaño de cada punto muestra un tercer valor se llama gráfico de burbujas. Así que voy a buscar esa página.)
>
> 🖱️ I'm scrolling down to the Basic Charts section, in the middle of the page, and clicking Bubble Charts, to see how to size the points.
>
> (Bajo hasta la sección Basic Charts, en el medio de la página, y hago clic en Bubble Charts, para ver cómo darles tamaño a los puntos.)

Si no lo encontrás rápido: *"I'm pressing Control and F and typing bubble, to find the link on this page."*

> 🖱️ I'm scrolling down to the first Plotly Express example, at the top of the Bubble charts page, to read its code.
>
> (Bajo hasta el primer ejemplo de Plotly Express, al principio de la página Bubble charts, para leer su código.)
>
> 🟢 This example uses the same Gapminder data for 2007. It adds three options I need. size equals pop makes each bubble as big as the country's population. log_x equals True puts the x axis on a logarithmic scale. And size_max equals 60 sets how big the largest bubble can be.
>
> (Este ejemplo usa los mismos datos de Gapminder de 2007. Agrega tres opciones que necesito. size igual a pop hace que cada burbuja sea tan grande como la población del país. log_x igual a True pone el eje x en escala logarítmica. Y size_max igual a 60 define qué tan grande puede ser la burbuja más grande.)
>
> 🟢 A logarithmic scale means each step on the axis multiplies the value by ten: one thousand, ten thousand, a hundred thousand. That spreads out the poorer countries that were squeezed on the left.
>
> (Una escala logarítmica significa que cada paso del eje multiplica el valor por diez: mil, diez mil, cien mil. Eso separa los países más pobres que estaban apretados a la izquierda.)
>
> 🟢 I also want to confirm exactly what log_x does, and find out how to rename the axes. For that, the best place is the API reference, which lists every parameter of px.scatter.
>
> (También quiero confirmar exactamente qué hace log_x y averiguar cómo renombrar los ejes. Para eso, el mejor lugar es la referencia de la API, que lista cada parámetro de px.scatter.)
>
> 🖱️ I'm clicking the address bar at the top, typing plotly dot com slash python dash api dash reference, and pressing Enter, to open the API reference.
>
> (Hago clic en la barra de direcciones, arriba, escribo plotly punto com barra python guion api guion reference y aprieto Enter, para abrir la referencia de la API.)
>
> 🖱️ I'm clicking plotly dot express in the list, and then scatter, to open the page for the px.scatter function.
>
> (Hago clic en plotly.express en la lista y después en scatter, para abrir la página de la función px.scatter.)

Si te perdés en la lista, escribís la dirección completa: `plotly.com/python-api-reference/generated/plotly.express.scatter.html`.

> 🖱️ I'm pressing Control and F and typing log_x, to find that parameter on this long page.
>
> (Aprieto Control y F y escribo log_x, para encontrar ese parámetro en esta página larga.)
>
> 🟢 The reference says: if True, the x-axis is log-scaled. That confirms what I saw in the example.
>
> (La referencia dice: si es True, el eje x tiene escala logarítmica. Eso confirma lo que vi en el ejemplo.)
>
> 🖱️ I'm scrolling down a little with the mouse wheel, to show the parameters below log_x.
>
> (Bajo un poco con la rueda del mouse, para mostrar los parámetros que están debajo de log_x.)
>
> 🟢 A few parameters below, there's title, which sets the chart title.
>
> (Unos parámetros más abajo está title, que define el título del gráfico.)
>
> 🖱️ I'm changing the search text in the find bar at the bottom to labels, to find the parameter that renames the axes.
>
> (Cambio el texto de búsqueda en la barra de búsqueda, abajo, por labels, para encontrar el parámetro que renombra los ejes.)

Si `labels` aparece varias veces, apretás `Enter` en la barra de búsqueda hasta llegar a la entrada **labels (dict with str keys and str values)**.

> 🟢 labels takes a dictionary. By default, Plotly uses the column names for the axis titles, the legend, and the tooltip, and this parameter lets me replace them with clear names.
>
> (labels recibe un diccionario. Por defecto, Plotly usa los nombres de las columnas para los títulos de los ejes, la leyenda y el tooltip, y este parámetro me deja reemplazarlos por nombres claros.)
>
> 🖱️ I'm scrolling up a little with the mouse wheel, to show the parameters just above labels.
>
> (Subo un poco con la rueda del mouse, para mostrar los parámetros que están justo arriba de labels.)
>
> 🟢 Just above labels, there's animation_frame, which turns a column into the frames of an animation. I may try that at the end. Now I know everything I need.
>
> (Justo arriba de labels está animation_frame, que convierte una columna en los cuadros de una animación. Quizás lo pruebe al final. Ahora ya sé todo lo que necesito.)

Si salteás la sección opcional del gráfico animado, no digas la frase de `animation_frame`: decí solo *"Now I know everything I need."*

> 🖱️ I'm pressing Escape to close the find bar, and clicking the Colab tab, the second tab at the top, to go back to my notebook.
>
> (Aprieto Escape para cerrar la barra de búsqueda y hago clic en la pestaña de Colab, la segunda arriba, para volver a mi notebook.)

**Resultado esperado:** viste el ejemplo de Bubble charts y las entradas `log_x` y `labels` en la referencia. Estás de vuelta en Colab.

---

## 14:30–17:00 — Gráfico mejorado

**Acción en pantalla:** un título de sección y una celda de código.

**Narración exacta en inglés:**

> 🖱️ I'm scrolling down to the bottom of the notebook, and clicking the plus Text button in the toolbar, to add a heading for the improved chart.
>
> (Bajo hasta el final del notebook y hago clic en el botón + Text de la barra de herramientas, para agregar un título para el gráfico mejorado.)

Escribís:

```markdown
## 3. Improved chart
After checking the Plotly docs: `log_x=True` spreads out the GDP values, and `size="pop"` turns the points into bubbles.
```

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell with the improved chart.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código con el gráfico mejorado.)

Escribís la **celda 6**:

```python
fig = px.scatter(
    df_2007, x="gdpPercap", y="lifeExp",
    color="continent", size="pop", hover_name="country",
    log_x=True, size_max=60,
    title="Life Expectancy vs. GDP per Capita (2007)",
    labels={"gdpPercap": "GDP per capita (USD)", "lifeExp": "Life expectancy (years)"},
)
fig.show()
```

**What each line does:**

- 🟢 `fig = px.scatter(`: the same function as before. I split the options over several lines so they're easy to read. Python allows that inside parentheses.
- 🟢 `df_2007, x="gdpPercap", y="lifeExp",`: the same data and the same axes as the first chart.
- 🟢 `color="continent", size="pop", hover_name="country",`: color and hover_name stay the same, and size equals pop is new: bigger countries get bigger bubbles.
- 🟢 `log_x=True, size_max=60,`: the two options from the docs: a logarithmic x axis, and a maximum bubble size of 60.
- 🟢 `title="..."`: the title that appears above the chart.
- 🟢 `labels={...}`: a dictionary that maps each column name to a clear name. The axis titles and the tooltip will use these names.
- 🟢 `)`: closes the function call.
- 🟢 `fig.show()`: displays the new chart. I reuse the name fig, so it replaces the first chart in memory.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to draw the improved chart.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para dibujar el gráfico mejorado.)

Si sale `SyntaxError`, mirá las comas al final de cada línea y las comillas; decí qué encontraste, corregilo y volvé a ejecutar.

> 🟢 Now the chart is much easier to read. The countries are spread out across the x axis, which shows one thousand, ten thousand, and so on. Bubble size shows population, so China and India are the two largest bubbles. And the title and the axis names are clear.
>
> (Ahora el gráfico se lee mucho mejor. Los países están repartidos a lo largo del eje x, que muestra mil, diez mil, etcétera. El tamaño de la burbuja muestra la población, así que China e India son las dos burbujas más grandes. Y el título y los nombres de los ejes son claros.)
>
> 🟢 Now I can see the pattern: richer countries tend to live longer. And on a log scale, the points form almost a straight line going up. That means each time income multiplies, life expectancy goes up by a similar number of years.
>
> (Ahora se ve el patrón: los países más ricos tienden a vivir más. Y en escala logarítmica, los puntos forman casi una línea recta que sube. Eso significa que cada vez que el ingreso se multiplica, la esperanza de vida sube una cantidad de años parecida.)

**Resultado esperado:** gráfico de burbujas con título, ejes **GDP per capita (USD)** y **Life expectancy (years)**, eje X con marcas tipo `1000`, `10k`, y dos burbujas grandes (China e India).

---

## 17:00–21:00 — Probar las interacciones

Probás cada interacción **una por una** y decís lo que ves. Si alguna no responde como dice el guion, describí lo que pasa de verdad.

**Acción en pantalla y narración exacta en inglés:**

### Tooltip (hover)

> 🖱️ I'm moving the mouse over the largest bubble, in the middle of the chart, to check its tooltip.
>
> (Muevo el mouse sobre la burbuja más grande, en el medio del gráfico, para comprobar su tooltip.)
>
> 🟢 The tooltip says China in bold, continent Asia, GDP per capita about 4,959 dollars, life expectancy about 73 years, and a population of about 1.3 billion. So the hover shows the right data, and it uses my new labels.
>
> (El tooltip dice China en negrita, continente Asia, PIB per cápita de unos 4.959 dólares, esperanza de vida de unos 73 años y una población de unos 1.300 millones. O sea que el hover muestra los datos correctos y usa mis nombres nuevos.)
>
> 🟢 Population and continent still show their column names, pop and continent, because I only renamed the two axes. That's fine for now, and I could add them to labels later.
>
> (La población y el continente siguen mostrando los nombres de columna, pop y continent, porque solo renombré los dos ejes. Por ahora está bien, y podría agregarlos a labels más adelante.)
>
> 🖱️ I'm moving the mouse to the bubbles at the bottom of the chart, to find the country with the lowest life expectancy.
>
> (Muevo el mouse a las burbujas de la parte de abajo del gráfico, para encontrar el país con la esperanza de vida más baja.)
>
> 🟢 This one is Swaziland, in Africa, with about 40 years of life expectancy, the lowest in the data.
>
> (Esta es Swaziland, en África, con unos 40 años de esperanza de vida, la más baja de los datos.)

### Leyenda

> 🖱️ I'm clicking Africa in the legend, on the right side of the chart, to hide that continent.
>
> (Hago clic en Africa en la leyenda, del lado derecho del gráfico, para ocultar ese continente.)
>
> 🟢 The African bubbles disappeared, and Africa looks greyed out in the legend. One click hides a group.
>
> (Las burbujas de África desaparecieron y Africa se ve en gris en la leyenda. Un clic oculta un grupo.)
>
> 🖱️ I'm clicking Africa in the legend again, to show it back.
>
> (Hago clic de nuevo en Africa en la leyenda, para volver a mostrarla.)
>
> 🖱️ I'm double-clicking Europe in the legend, to show only the European countries.
>
> (Hago doble clic en Europe en la leyenda, para mostrar solo los países europeos.)
>
> 🟢 Now only Europe is visible. A double click isolates one group, which is useful to compare countries inside one continent.
>
> (Ahora solo se ve Europa. Un doble clic aísla un grupo, lo que sirve para comparar países dentro de un continente.)
>
> 🖱️ I'm double-clicking Europe in the legend again, to bring back all the continents.
>
> (Hago doble clic de nuevo en Europe en la leyenda, para volver a mostrar todos los continentes.)

### Zoom, desplazamiento y reinicio

> 🖱️ I'm moving the mouse to the top right of the chart, to show the toolbar that Plotly adds, called the modebar.
>
> (Muevo el mouse arriba a la derecha del gráfico, para mostrar la barra de herramientas que agrega Plotly, llamada modebar.)
>
> 🟢 The modebar has a camera to download the chart, zoom, pan, selection tools, zoom in and out, autoscale, and reset axes. If I hover over each icon, a small label shows its name.
>
> (La modebar tiene una cámara para descargar el gráfico, zoom, desplazamiento, herramientas de selección, acercar y alejar, autoescala y reiniciar los ejes. Si paso el mouse por cada ícono, aparece una etiqueta chica con su nombre.)
>
> 🖱️ I'm dragging a box with the mouse around the group of bubbles on the right side of the chart, to zoom in on the richest countries.
>
> (Arrastro un recuadro con el mouse alrededor del grupo de burbujas del lado derecho del gráfico, para acercarme a los países más ricos.)
>
> 🟢 The chart zoomed in, and the axes changed to fit that area. Now the bubbles that were on top of each other are separated.
>
> (El gráfico se acercó y los ejes cambiaron para ajustarse a esa zona. Ahora las burbujas que estaban encimadas se separan.)
>
> 🖱️ I'm clicking the Pan icon, the four-arrow cross in the modebar at the top right, and dragging the chart, to move the view.
>
> (Hago clic en el ícono Pan, la cruz de cuatro flechas en la modebar, arriba a la derecha, y arrastro el gráfico, para mover la vista.)
>
> 🖱️ I'm clicking the Reset axes icon, the house in the modebar at the top right, to go back to the full chart.
>
> (Hago clic en el ícono Reset axes, la casita en la modebar, arriba a la derecha, para volver al gráfico completo.)
>
> 🟢 The chart is back to its original view. A double click on the chart area does the same.
>
> (El gráfico volvió a su vista original. Un doble clic en el área del gráfico hace lo mismo.)
>
> 🖱️ I'm clicking the Zoom icon, the magnifying glass in the modebar, so dragging zooms again instead of panning.
>
> (Hago clic en el ícono Zoom, la lupa de la modebar, para que arrastrar vuelva a hacer zoom en vez de mover.)

### Descargar como imagen

> 🖱️ I'm clicking the camera icon, the first one in the modebar at the top right, to download the chart as a PNG image.
>
> (Hago clic en el ícono de la cámara, el primero de la modebar, arriba a la derecha, para descargar el gráfico como imagen PNG.)
>
> 🖱️ I'm clicking the Downloads arrow at the top right of Firefox, to check that the image was saved.
>
> (Hago clic en la flecha de Descargas, arriba a la derecha de Firefox, para comprobar que se guardó la imagen.)
>
> 🟢 The file newplot.png is in the downloads list, so the export works. A PNG is a static picture: it's useful for a report, but it loses the interactions.
>
> (El archivo newplot.png está en la lista de descargas, así que la exportación funciona. Un PNG es una imagen fija: sirve para un informe, pero pierde las interacciones.)

Decí el nombre que aparezca de verdad en la lista. Si no aparece, decilo y probá otra vez.

> 🖱️ I'm clicking an empty area of the page, to close the Downloads panel.
>
> (Hago clic en un área vacía de la página, para cerrar el panel de Descargas.)

### Anotar lo comprobado

> 🖱️ I'm clicking the plus Text button in the toolbar, to write down the interactions I just checked.
>
> (Hago clic en el botón + Text de la barra de herramientas, para anotar las interacciones que acabo de comprobar.)

Escribís (decís cada punto en voz alta mientras lo escribís):

```markdown
## 4. Interactions checked
- **Hover:** shows the country name in bold, plus its GDP per capita, life expectancy, population, and continent.
- **Legend:** one click hides a continent, a double click shows only that continent, and another double click brings all of them back.
- **Zoom and pan:** dragging a box zooms in, the Pan tool moves the view, and Reset axes goes back to the start.
- **Download:** the camera icon saves the chart as a PNG file.
```

**Resultado esperado:** probaste las cinco interacciones y quedaron escritas en el notebook.

---

## 21:00–23:00 — (Opcional) Gráfico animado de 1952 a 2007

Hacelo solo si el Goal no limita la tarea a un único gráfico.

**Narración exacta en inglés:**

> 🟢 In the API reference, just above labels, I saw a parameter called animation_frame. With it, Plotly can animate a chart over time. I'll try it with the full data, with all twelve years.
>
> (En la referencia de la API, justo arriba de labels, vi un parámetro llamado animation_frame. Con él, Plotly puede animar un gráfico en el tiempo. Lo voy a probar con los datos completos, con los doce años.)

> 🖱️ I'm clicking the plus Text button and then the plus Code button in the toolbar, to add a heading and a code cell for the animated chart.
>
> (Hago clic en el botón + Text y después en el botón + Code de la barra de herramientas, para agregar un título y una celda de código para el gráfico animado.)

Título: `## 5. Animated chart (1952–2007)`. Después escribís la **celda 7**:

```python
fig_anim = px.scatter(
    df, x="gdpPercap", y="lifeExp",
    color="continent", size="pop", hover_name="country",
    log_x=True, size_max=60,
    animation_frame="year", range_x=[100, 150000], range_y=[20, 90],
)
fig_anim.show()
```

**What each line does:**

- 🟢 `fig_anim = px.scatter(`: the same function, stored in a new variable, so my 2007 chart stays in fig.
- 🟢 `df, x=..., y=...,`: this time I use df, the full data with every year, not df_2007.
- 🟢 `color=..., size=..., hover_name=...,` and `log_x=True, size_max=60,`: the same options as the improved chart.
- 🟢 `animation_frame="year"`: each year becomes one frame of the animation, and Plotly adds a play button and a slider.
- 🟢 `range_x=[100, 150000], range_y=[20, 90]`: these fix the axes, so they don't jump from one year to the next. The data goes from about 240 to 113,000 dollars, and from about 24 to 83 years, so these ranges cover everything.
- 🟢 `fig_anim.show()`: displays the animated chart.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to draw the animated chart.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para dibujar el gráfico animado.)
>
> 🖱️ I'm clicking the play button, the triangle at the bottom left of the chart, to start the animation.
>
> (Hago clic en el botón de play, el triángulo abajo a la izquierda del gráfico, para empezar la animación.)
>
> 🟢 The bubbles move up and to the right over time: almost every country gets richer and lives longer. For example, the median life expectancy in Africa goes from about 39 years in 1952 to about 53 in 2007.
>
> (Las burbujas se mueven hacia arriba y a la derecha con el tiempo: casi todos los países se vuelven más ricos y viven más. Por ejemplo, la mediana de esperanza de vida en África pasa de unos 39 años en 1952 a unos 53 en 2007.)
>
> 🖱️ I'm dragging the year slider, below the chart, back to 1952, to compare the first and the last year.
>
> (Arrastro el deslizador de años, debajo del gráfico, de vuelta a 1952, para comparar el primer año con el último.)

**Resultado esperado:** gráfico con botón de play y deslizador de **year** de 1952 a 2007; los ejes no cambian entre años.

---

## 23:00–24:30 — Guardar el gráfico, el notebook y conclusiones

**Narración exacta en inglés:**

> 🖱️ I'm clicking the plus Text button and then the plus Code button, to add a heading and a code cell that saves the chart.
>
> (Hago clic en el botón + Text y después en el botón + Code, para agregar un título y una celda de código que guarda el gráfico.)

Título: `## 6. Save and conclusions` (si saltaste la sección opcional, usá `## 5. Save and conclusions`). Después escribís la **celda 8**:

```python
fig.write_html("life_expectancy_2007.html")
```

- 🟢 `fig.write_html(...)`: this saves the 2007 chart as an HTML file. Unlike the PNG, the HTML keeps every interaction, and it opens in any browser, without Python.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to save the file.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para guardar el archivo.)
>
> 🖱️ I'm clicking the Files icon, the folder in the left sidebar of Colab, to check that the file was created.
>
> (Hago clic en el ícono Files, la carpeta de la barra lateral izquierda de Colab, para comprobar que se creó el archivo.)
>
> 🟢 life_expectancy_2007.html is in the list, so it was saved.
>
> (life_expectancy_2007.html está en la lista, así que se guardó.)

Si no aparece, hacé clic en el ícono de **Refresh** arriba del panel Files y decilo: *"I'm clicking the Refresh icon at the top of the Files panel, to update the list."*

> 🖱️ I'm clicking the three dots next to the file name, and choosing Download, to save the interactive chart on my computer.
>
> (Hago clic en los tres puntos junto al nombre del archivo y elijo Download, para guardar el gráfico interactivo en mi computadora.)
>
> 🖱️ I'm clicking the plus Text button, to add the conclusions at the end of the notebook.
>
> (Hago clic en el botón + Text, para agregar las conclusiones al final del notebook.)

Escribís (diciéndolo en voz alta). Si saltaste el gráfico animado, borrá el último punto:

```markdown
- In 2007, richer countries tend to live longer, but the relationship is not a straight line: life expectancy rises fast at low incomes and flattens at high incomes.
- Africa has the lowest median life expectancy (about 53 years), and Europe and Oceania the highest (about 79 and 81).
- South Africa, Botswana, and Equatorial Guinea are exceptions: their GDP per capita is above 9,000 dollars, but life expectancy is around 50 years.
- The animation shows life expectancy rising on every continent between 1952 and 2007.
```

> 🖱️ I'm opening the File menu at the top left of Colab, and choosing Download, then Download .ipynb, to save the finished notebook.
>
> (Abro el menú File, arriba a la izquierda de Colab, y elijo Download y después Download .ipynb, para guardar el notebook terminado.)
>
> 🖱️ I'm clicking the Downloads arrow at the top right of Firefox, to check that both files were downloaded.
>
> (Hago clic en la flecha de Descargas, arriba a la derecha de Firefox, para comprobar que se descargaron los dos archivos.)
>
> 🟢 plotly_gapminder.ipynb and life_expectancy_2007.html are in the downloads list, together with the PNG.
>
> (plotly_gapminder.ipynb y life_expectancy_2007.html están en la lista de descargas, junto con el PNG.)

**Resultado esperado:** en Descargas están `plotly_gapminder.ipynb`, `life_expectancy_2007.html` y `newplot.png`.

---

## 24:30–27:30 — Epílogo (menos de 4 minutos)

**Acción en pantalla:** cerrás el panel de Descargas y recorrés despacio el notebook con la rueda del mouse, desde arriba.

**Narración exacta en inglés:**

> 🖱️ I'm clicking an empty area of the page to close the Downloads panel, and scrolling up to the top of the notebook, to go over the whole workflow.
>
> (Hago clic en un área vacía de la página para cerrar el panel de Descargas y subo hasta el principio del notebook, para repasar todo el flujo de trabajo.)
>
> 🟢 To sum up: I checked that Plotly was installed in Colab, loaded the Gapminder sample dataset, explored it, and filtered the year 2007. Then I made a first scatter plot, found its problems, and used the official documentation to fix them with a log scale, bubble sizes, a title, and clear labels.
>
> (Para resumir: comprobé que Plotly estaba instalado en Colab, cargué el dataset de ejemplo Gapminder, lo exploré y filtré el año 2007. Después hice un primer gráfico de dispersión, encontré sus problemas y usé la documentación oficial para arreglarlos con una escala logarítmica, tamaños de burbuja, un título y nombres claros.)
>
> 🟢 I tested every interaction on screen: the tooltip shows the right data, the legend hides and isolates continents, zoom, pan, and reset work, and the chart downloads as a PNG. I also saved it as an HTML file, which keeps the interactions.
>
> (Probé cada interacción en pantalla: el tooltip muestra los datos correctos, la leyenda oculta y aísla continentes, el zoom, el desplazamiento y el reinicio funcionan, y el gráfico se descarga como PNG. También lo guardé como archivo HTML, que conserva las interacciones.)
>
> 🟢 What I learned about Plotly: with Plotly Express, one function call gives a full interactive chart, and each option is just a column name. The interactions come for free; I didn't write any code for hover or zoom. That's the main difference from a static chart library like Matplotlib.
>
> (Lo que aprendí de Plotly: con Plotly Express, una sola llamada a una función da un gráfico interactivo completo, y cada opción es solo el nombre de una columna. Las interacciones vienen incluidas: no escribí código para el hover ni para el zoom. Esa es la diferencia principal con una librería de gráficos estáticos como Matplotlib.)
>
> 🟢 Checking the documentation was a key step. The Bubble charts page gave me a working example, and the API reference confirmed what each parameter does and showed me options I didn't know, like animation_frame. That's a good way to learn any new library: start simple, see what's wrong, and look up only what you need.
>
> (Consultar la documentación fue un paso clave. La página Bubble charts me dio un ejemplo que funciona, y la referencia de la API confirmó qué hace cada parámetro y me mostró opciones que no conocía, como animation_frame. Es una buena forma de aprender cualquier librería nueva: empezar simple, ver qué está mal y buscar solo lo que hace falta.)
>
> 🟢 About the data: interactivity helps to find exceptions. By hovering, I found that South Africa, Botswana, and Equatorial Guinea have a GDP per capita above nine thousand dollars, but a life expectancy around fifty years. The chart shows that, but the data alone doesn't explain why.
>
> (Sobre los datos: la interactividad ayuda a encontrar excepciones. Pasando el mouse encontré que South Africa, Botswana y Equatorial Guinea tienen un PIB per cápita de más de nueve mil dólares, pero una esperanza de vida de unos cincuenta años. El gráfico lo muestra, pero los datos solos no explican por qué.)
>
> 🟢 There are some limits. This is a small practice dataset that ends in 2007, so it isn't current. And a scatter plot shows a relationship, not a cause: being richer is linked to living longer, but this chart can't prove one causes the other.
>
> (Hay algunos límites. Es un dataset chico de práctica que termina en 2007, así que no está actualizado. Y un gráfico de dispersión muestra una relación, no una causa: ser más rico está asociado a vivir más, pero este gráfico no puede probar que una cosa cause la otra.)
>
> 🟢 As next steps, I could add population and continent to the labels, so the whole tooltip is clean, or try other Plotly Express charts from the same documentation, like a map with px.choropleth. Thanks for watching!
>
> (Como próximos pasos, podría agregar la población y el continente a labels, para que todo el tooltip quede prolijo, o probar otros gráficos de Plotly Express de la misma documentación, como un mapa con px.choropleth. ¡Gracias por mirar!)

Si al terminar el reloj no pasó los 15:00, no cortes: volvé al gráfico de 2007 y seguí explorándolo con el hover y el zoom, explicando lo que ves (por ejemplo, Japan arriba a la derecha y Congo, Dem. Rep. abajo a la izquierda).

---

## Después de grabar

1. Ejecutá **Run full AutoQC**, no solo *Rerun failing*.
2. Revisá que en ningún momento se vean el Approval ID, tu correo ni otros datos personales.
3. Subí los archivos que pidan las reglas de Odin (en tareas anteriores: el **MP4**, el **ZIP original de TaskRecorder**, **Deliverables.zip** y **Metadata.rtf**). En Deliverables.zip, si las reglas lo permiten: `plotly_gapminder.ipynb`, `life_expectancy_2007.html` y `newplot.png`.
