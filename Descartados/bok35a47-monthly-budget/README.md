# bok35a47 — Monthly Budget

Guion paso a paso para grabar la tarea **bok35a47**: armar en **Google Sheets** un control de presupuesto mensual. Calcula el gasto por categoría con **SUMIF** y el porcentaje que representa sobre el ingreso. Con **IF** marca las categorías que pasan el **80%** de su presupuesto, y con un **gráfico de barras** compara lo presupuestado con lo gastado. La grabación tiene que durar **entre 15:00 y 50:59**. Este guion apunta a unos **21 minutos**, epílogo incluido.

**Cómo leer este guion:**

- Las frases que empiezan con 🖱️ las decís **en el momento de hacer clic, desplazarte o escribir**. Siempre dicen **qué** elemento usás, **dónde** está en la pantalla y **por qué** lo usás. Son las que revisa AutoQC.
- Las frases que empiezan con 🟢 son la explicación que **decís en inglés** entre una acción y otra.
- Debajo de cada fórmula, la lista **What each part does** explica cada parte en inglés. La leés en voz alta mientras la escribís.
- El resto, en castellano, es lo que hacés en pantalla. Las traducciones aparecen entre paréntesis después de cada frase.

> **Importante:** el Goal de Studio tiene prioridad sobre este guion. Antes de grabar, comparalo con el campo **Describe your idea** de la tarea. Los datos los armé yo: son ficticios.

---

## Archivos de la carpeta

```
bok35a47-monthly-budget/
├── README.md         ← este guion
├── transactions.csv  ← material de partida: 24 gastos de octubre de 2026
└── budget.csv        ← material de partida: ingreso mensual y presupuesto por categoría
```

---

## Los datos

**`transactions.csv`**: 24 gastos con 4 columnas, `Date`, `Description`, `Category` y `Amount`.

**`budget.csv`**: cuando lo importás, la hoja **Budget** queda así:

| | A | B | C | D | E | F |
| - | - | - | - | - | - | - |
| 1 | Monthly income | 4500 | | | | |
| 2 | | | | | | |
| 3 | Category | Budget | Actual | % of income | % of budget used | Alert |
| 4 | Rent | 1400 | | | | |
| 5 | Groceries | 500 | | | | |
| 6 | Utilities | 200 | | | | |
| 7 | Transportation | 250 | | | | |
| 8 | Dining Out | 200 | | | | |
| 9 | Entertainment | 150 | | | | |
| 10 | Health | 100 | | | | |
| 11 | Total | | | | | |

Las columnas C a F (y la fila 11) las completás con fórmulas durante la grabación.

**Valores de referencia.** Los calculé directamente de los CSV. Compará con lo que te da la hoja:

| Categoría | Budget | Actual | % of income | % of budget used | Alert |
| --------- | -----: | -----: | ----------: | ---------------: | ----- |
| Rent | 1.400,00 | 1.400,00 | 31,11% | 100,00% | Over 80% |
| Groceries | 500,00 | 432,60 | 9,61% | 86,52% | Over 80% |
| Utilities | 200,00 | 150,00 | 3,33% | 75,00% | OK |
| Transportation | 250,00 | 160,30 | 3,56% | 64,12% | OK |
| Dining Out | 200,00 | 235,90 | 5,24% | 117,95% | Over 80% |
| Entertainment | 150,00 | 94,99 | 2,11% | 63,33% | OK |
| Health | 100,00 | 85,25 | 1,89% | 85,25% | Over 80% |
| **Total** | **2.800,00** | **2.559,04** | **56,87%** | **91,39%** | Over 80% |

El ingreso es de 4.500, así que quedan **1.940,96** sin gastar.

---

## Antes de grabar

1. Leé el Goal y compará este guion con el campo **Describe your idea** de Studio.
2. **Idioma y configuración regional.** Este guion usa los menús en **inglés** y fórmulas con **coma** (`,`). Si tu Google está en castellano, los menús van a aparecer en castellano, y con la configuración de Argentina las fórmulas usan punto y coma (`;`) y los decimales, coma. Para que todo coincida con el guion:
   - Poné tu cuenta de Google en inglés (https://myaccount.google.com → *Datos personales* → *Idioma*), o adaptá los nombres de los menús.
   - En la grabación cambiás la configuración regional de la hoja a **United States** (está incluido en el guion). Sin ese paso, los CSV pueden importarse mal.
3. Practicá una vez entera, leyendo en voz alta las frases 🖱️ y 🟢, y cronometrá. Después borrá la hoja de práctica.
4. Dejá dos pestañas abiertas en Firefox: el documento **Goal** y Google Sheets (https://sheets.google.com). Tené los dos CSV en una carpeta fácil de encontrar. Agrandá el zoom (`Ctrl + +`).
5. Maximizá el navegador y cerrá o minimizá las demás ventanas, para que ninguna tape a otra.
6. Pausa de ~1 segundo después de cada clic y nunca más de 45 segundos en silencio.
7. No muestres Studio, Mercor, información privada ni herramientas de IA. Cerrá este guion si está en la misma pantalla.

---

## 0:00–0:45 — Mostrar el Goal

> 🖱️ I'm on the Goal document in the first browser tab, to show what this task asks for.
>
> (Estoy en el documento del Goal, en la primera pestaña del navegador, para mostrar qué pide esta tarea.)
>
> 🟢 As a financial analyst, I'll build a monthly budget tracker in Google Sheets. It will total the expenses by category with SUMIF, calculate each category's share of income, flag categories over 80 percent of their budget with IF, and compare budget and actual spending in a bar chart.
>
> (Como analista financiero, voy a armar un control de presupuesto mensual en Google Sheets. Va a sumar los gastos por categoría con SUMIF, calcular qué parte del ingreso representa cada categoría, marcar con IF las categorías que pasan el 80 por ciento de su presupuesto y comparar en un gráfico de barras lo presupuestado con lo gastado.)

---

## 0:45–5:00 — Crear la hoja e importar los datos

> 🖱️ I'm clicking the second browser tab, at the top of the window, to open Google Sheets.
>
> (Hago clic en la segunda pestaña del navegador, arriba de la ventana, para abrir Google Sheets.)
>
> 🟢 Google Sheets is Google's free online spreadsheet. It works in the browser and saves automatically.
>
> (Google Sheets es la hoja de cálculo online y gratuita de Google. Funciona en el navegador y guarda automáticamente.)
>
> 🖱️ I'm clicking the Blank spreadsheet tile, at the top left under "Start a new spreadsheet", to create a new file.
>
> (Hago clic en el recuadro Blank spreadsheet, arriba a la izquierda debajo de "Start a new spreadsheet", para crear un archivo nuevo.)
>
> 🖱️ I'm clicking the "Untitled spreadsheet" title at the top left, and typing Monthly Budget Tracker, to name the file.
>
> (Hago clic en el título "Untitled spreadsheet", arriba a la izquierda, y escribo Monthly Budget Tracker, para ponerle nombre al archivo.)
>
> 🖱️ I'm opening the File menu at the top left and choosing Settings, to check the locale.
>
> (Abro el menú File, arriba a la izquierda, y elijo Settings, para revisar la configuración regional.)
>
> 🖱️ I'm choosing United States in the Locale list, in the middle of the Settings dialog, and clicking the Save settings button at the bottom right, so decimals use a dot and the numbers in my files are read correctly.
>
> (Elijo United States en la lista Locale, en el medio del cuadro Settings, y hago clic en el botón Save settings, abajo a la derecha, para que los decimales usen punto y los números de mis archivos se lean bien.)

Importás los gastos:

> 🖱️ I'm opening the File menu at the top left and choosing Import, to load the expense transactions.
>
> (Abro el menú File, arriba a la izquierda, y elijo Import, para cargar los gastos.)
>
> 🖱️ I'm clicking the Upload tab at the top of the Import dialog, then the Browse button in the middle, and choosing transactions.csv from my computer.
>
> (Hago clic en la pestaña Upload, arriba del cuadro Import, después en el botón Browse del medio, y elijo transactions.csv de mi computadora.)
>
> 🖱️ I'm choosing Replace current sheet in the Import location list, and clicking the Import data button at the bottom, to put the transactions in this first sheet.
>
> (Elijo Replace current sheet en la lista Import location y hago clic en el botón Import data, abajo, para poner los gastos en esta primera hoja.)
>
> 🟢 Each row is one expense from October: the date, a description, the category, and the amount in dollars. There are 24 expenses in 7 categories.
>
> (Cada fila es un gasto de octubre: la fecha, una descripción, la categoría y el importe en dólares. Hay 24 gastos en 7 categorías.)
>
> 🖱️ I'm double-clicking the sheet tab at the bottom left, and typing Transactions, to give the sheet a clear name that I'll use in my formulas.
>
> (Hago doble clic en la pestaña de la hoja, abajo a la izquierda, y escribo Transactions, para darle a la hoja un nombre claro que voy a usar en mis fórmulas.)

Importás el presupuesto:

> 🖱️ I'm opening the File menu again and choosing Import, to load the income and the budget.
>
> (Abro de nuevo el menú File y elijo Import, para cargar el ingreso y el presupuesto.)
>
> 🖱️ I'm clicking the Upload tab, then Browse, and choosing budget.csv.
>
> (Hago clic en la pestaña Upload, después en Browse, y elijo budget.csv.)
>
> 🖱️ I'm choosing Insert new sheet in the Import location list, and clicking Import data at the bottom, to keep the budget in its own sheet.
>
> (Elijo Insert new sheet en la lista Import location y hago clic en Import data, abajo, para tener el presupuesto en su propia hoja.)
>
> 🖱️ I'm double-clicking the new sheet tab at the bottom, next to Transactions, and typing Budget, to name it.
>
> (Hago doble clic en la pestaña de la hoja nueva, abajo, al lado de Transactions, y escribo Budget, para ponerle nombre.)
>
> 🟢 This sheet has the monthly income, 4,500 dollars, in cell B1, and the budget for each category in column B. Columns C to F are empty: I'll fill them with formulas. Keeping the raw transactions and the summary in separate sheets keeps the data organized.
>
> (Esta hoja tiene el ingreso mensual, 4.500 dólares, en la celda B1, y el presupuesto de cada categoría en la columna B. Las columnas C a F están vacías: las voy a completar con fórmulas. Tener los gastos y el resumen en hojas separadas mantiene los datos ordenados.)

---

## 5:00–9:00 — SUMIF: gasto real por categoría

> 🖱️ I'm clicking cell C4, in the Actual column next to Rent, to calculate how much was spent on rent.
>
> (Hago clic en la celda C4, en la columna Actual al lado de Rent, para calcular cuánto se gastó en alquiler.)

Escribís la fórmula y presionás Enter:

```
=SUMIF(Transactions!C:C, A4, Transactions!D:D)
```

**What each part does:**

- 🟢 `=SUMIF(`: SUMIF adds up only the values that meet a condition.
- 🟢 `Transactions!C:C`: the first part is where to look: the Category column in the Transactions sheet. The exclamation mark separates the sheet name from the column.
- 🟢 `A4`: the second part is what to look for: the category in cell A4, Rent.
- 🟢 `Transactions!D:D`: the third part is what to add: the Amount column. So the formula adds the amounts of every row whose category is Rent.

> 🟢 Rent is 1,400 dollars, one single payment.
>
> (El alquiler es de 1.400 dólares, un solo pago.)
>
> 🖱️ I'm dragging the small blue square at the bottom right of cell C4 down to C10, to copy the formula to the other categories.
>
> (Arrastro el cuadradito azul de la esquina inferior derecha de la celda C4 hasta C10, para copiar la fórmula a las otras categorías.)
>
> 🟢 When I copy the formula down, A4 changes to A5, A6, and so on, so each row looks for its own category. That's called a relative reference.
>
> (Cuando copio la fórmula hacia abajo, A4 cambia a A5, A6 y así, así que cada fila busca su propia categoría. Eso se llama referencia relativa.)

Totales de la fila 11:

> 🖱️ I'm clicking cell B11, in the Total row, and typing a SUM formula, to add up the whole budget.
>
> (Hago clic en la celda B11, en la fila Total, y escribo una fórmula SUM, para sumar todo el presupuesto.)

```
=SUM(B4:B10)
```

**What each part does:**

- 🟢 `=SUM(B4:B10)`: SUM adds every value from B4 to B10, the budgets of the seven categories.

> 🖱️ I'm dragging the small blue square at the bottom right of B11 one cell to the right, to C11, to total the actual spending too.
>
> (Arrastro el cuadradito azul de la esquina inferior derecha de B11 una celda a la derecha, hasta C11, para sumar también el gasto real.)
>
> 🟢 The total budget is 2,800 dollars and the actual spending is 2,559.04.
>
> (El presupuesto total es de 2.800 dólares y el gasto real es de 2.559,04.)
>
> 🖱️ I'm selecting cells B1 to C11 with the mouse, and clicking the Format as currency button, the dollar sign in the toolbar at the top, to show the amounts as money.
>
> (Selecciono con el mouse las celdas B1 a C11 y hago clic en el botón Format as currency, el signo de dólar de la barra de herramientas de arriba, para mostrar los importes como dinero.)

---

## 9:00–13:30 — Porcentajes e IF

> 🖱️ I'm clicking cell D4, in the "% of income" column, to calculate rent as a share of income.
>
> (Hago clic en la celda D4, en la columna "% of income", para calcular el alquiler como parte del ingreso.)

```
=C4/$B$1
```

**What each part does:**

- 🟢 `C4`: the actual spending on rent.
- 🟢 `/$B$1`: divided by the monthly income in B1. The dollar signs lock the reference: it's an absolute reference, so when I copy the formula down, every row still divides by B1.

> 🖱️ I'm clicking cell E4, in the "% of budget used" column, to compare rent with its budget.
>
> (Hago clic en la celda E4, en la columna "% of budget used", para comparar el alquiler con su presupuesto.)

```
=C4/B4
```

**What each part does:**

- 🟢 `=C4/B4`: the actual spending divided by the budget of the same category. Here I want relative references, because each row has its own budget.

> 🖱️ I'm clicking cell F4, in the Alert column, to flag the category if it goes over 80 percent of its budget.
>
> (Hago clic en la celda F4, en la columna Alert, para marcar la categoría si pasa el 80 por ciento de su presupuesto.)

```
=IF(C4>0.8*B4, "Over 80%", "OK")
```

**What each part does:**

- 🟢 `=IF(`: IF checks a condition and shows one result if it's true and another if it's false.
- 🟢 `C4>0.8*B4`: the condition: is the actual spending greater than 80 percent of the budget?
- 🟢 `"Over 80%"`: if it's true, the cell shows "Over 80%".
- 🟢 `"OK"`: if it's false, it shows "OK".

> 🖱️ I'm selecting cells D4 to F4 and dragging the small blue square at the bottom right down to row 10, to copy the three formulas to every category.
>
> (Selecciono las celdas D4 a F4 y arrastro el cuadradito azul de la esquina inferior derecha hasta la fila 10, para copiar las tres fórmulas a todas las categorías.)
>
> 🖱️ I'm selecting cells D10 to F10 and dragging the small blue square down one more row, to row 11, to get the same calculations for the totals.
>
> (Selecciono las celdas D10 a F10 y arrastro el cuadradito azul una fila más, hasta la fila 11, para tener los mismos cálculos en los totales.)
>
> 🖱️ I'm selecting cells D4 to E11 and clicking the Format as percent button, the percent sign in the toolbar at the top, to show the results as percentages.
>
> (Selecciono las celdas D4 a E11 y hago clic en el botón Format as percent, el signo de porcentaje de la barra de herramientas de arriba, para mostrar los resultados como porcentajes.)

Para que las alertas se vean de un vistazo:

> 🖱️ I'm selecting cells F4 to F11, and opening the Format menu at the top and choosing Conditional formatting, to color the alerts.
>
> (Selecciono las celdas F4 a F11, abro el menú Format de arriba y elijo Conditional formatting, para colorear las alertas.)
>
> 🖱️ In the panel on the right, I'm choosing "Text is exactly" in the Format rules list, typing Over 80%, choosing a red fill color, and clicking the Done button at the bottom of the panel.
>
> (En el panel de la derecha, elijo "Text is exactly" en la lista Format rules, escribo Over 80%, elijo un color de relleno rojo y hago clic en el botón Done, abajo del panel.)
>
> 🟢 Now the four categories over 80 percent are red: Rent, Groceries, Dining Out, and Health. Utilities, Transportation, and Entertainment are OK.
>
> (Ahora las cuatro categorías que pasan el 80 por ciento están en rojo: Rent, Groceries, Dining Out y Health. Utilities, Transportation y Entertainment están OK.)

---

## 13:30–16:00 — Gráfico de barras

> 🖱️ I'm selecting cells A3 to C10 with the mouse, the categories with their budget and actual spending, to use them in the chart.
>
> (Selecciono con el mouse las celdas A3 a C10, las categorías con su presupuesto y su gasto real, para usarlas en el gráfico.)
>
> 🖱️ I'm opening the Insert menu at the top and choosing Chart, to create the chart.
>
> (Abro el menú Insert de arriba y elijo Chart, para crear el gráfico.)
>
> 🖱️ In the Chart editor on the right, I'm opening the Chart type list and choosing Column chart, the vertical bar chart, to compare budget and actual side by side for each category.
>
> (En el Chart editor de la derecha, abro la lista Chart type y elijo Column chart, el gráfico de barras verticales, para comparar lado a lado el presupuesto y el gasto real de cada categoría.)

Si preferís barras horizontales, elegí **Bar chart**. Las dos opciones son gráficos de barras.

> 🖱️ I'm clicking the Customize tab at the top of the Chart editor, opening Chart and axis titles, and typing Budget vs Actual Spending as the chart title.
>
> (Hago clic en la pestaña Customize, arriba del Chart editor, abro Chart and axis titles y escribo Budget vs Actual Spending como título del gráfico.)
>
> 🖱️ In the same section, I'm choosing Horizontal axis title and typing Category, then Vertical axis title and typing Amount (USD), so both axes have names.
>
> (En la misma sección elijo Horizontal axis title y escribo Category, después Vertical axis title y escribo Amount (USD), para que los dos ejes tengan nombre.)
>
> 🖱️ I'm dragging the chart by its border to the right of the table, so it doesn't cover the data.
>
> (Arrastro el gráfico desde su borde hacia la derecha de la tabla, para que no tape los datos.)
>
> 🟢 Each category has two bars: the budget and the actual spending. Where the actual bar is taller, we overspent. Dining Out is the only category above its budget. Rent is exactly on budget, and the other categories are below.
>
> (Cada categoría tiene dos barras: el presupuesto y el gasto real. Donde la barra del gasto real es más alta, gastamos de más. Dining Out es la única categoría por encima de su presupuesto. Rent está justo en el presupuesto y las demás categorías están por debajo.)

---

## 16:00–17:30 — Revisar las fórmulas y verificar

> 🖱️ I'm opening the View menu at the top, choosing Show, and clicking Formulas, to review all the formulas at once.
>
> (Abro el menú View de arriba, elijo Show y hago clic en Formulas, para revisar todas las fórmulas a la vez.)
>
> 🟢 Every row uses the same formulas, only the row number changes, and every percentage of income divides by B1. That's what I expected.
>
> (Cada fila usa las mismas fórmulas, solo cambia el número de fila, y cada porcentaje del ingreso divide por B1. Es lo que esperaba.)
>
> 🖱️ I'm opening View, Show, Formulas again, to go back to the results.
>
> (Abro de nuevo View, Show, Formulas, para volver a los resultados.)
>
> 🖱️ I'm clicking the Transactions tab at the bottom left, and selecting the Amount column from D2 to D25, to check the total.
>
> (Hago clic en la pestaña Transactions, abajo a la izquierda, y selecciono la columna Amount de D2 a D25, para comprobar el total.)
>
> 🟢 The sum at the bottom right of the screen is 2,559.04, the same as the actual total in the Budget sheet. So SUMIF counted every transaction exactly once.
>
> (La suma de abajo a la derecha de la pantalla es 2.559,04, igual que el total real de la hoja Budget. Así que SUMIF contó cada gasto exactamente una vez.)
>
> 🖱️ I'm clicking the Budget tab at the bottom, to go back to the summary.
>
> (Hago clic en la pestaña Budget, abajo, para volver al resumen.)

---

## 17:30–18:30 — Resumen de los hallazgos

> 🖱️ I'm clicking cell A13, below the table, and typing a short summary of the findings.
>
> (Hago clic en la celda A13, debajo de la tabla, y escribo un resumen corto de los hallazgos.)

Escribís una línea por celda, de A13 a A16:

```
Summary
Total spending: $2,559.04, 56.9% of income. $1,940.96 left this month.
Dining Out is over budget (117.95%). Groceries (86.5%) and Health (85.3%) are close to the limit.
Rent is a fixed cost, so it always uses 100% of its budget.
```

> 🟢 To sum up: this month we spent about 57 percent of our income, so 1,940.96 dollars are left. Rent is the biggest expense, 31 percent of income. Dining Out went almost 18 percent over its budget, and Groceries and Health are close to their limits. Rent is flagged too, but that's expected, because it's a fixed cost.
>
> (Para resumir: este mes gastamos cerca del 57 por ciento del ingreso, así que quedan 1.940,96 dólares. El alquiler es el mayor gasto, el 31 por ciento del ingreso. Dining Out se pasó casi un 18 por ciento de su presupuesto, y Groceries y Health están cerca de su límite. Rent también aparece marcado, pero es lo esperable, porque es un costo fijo.)

---

## 18:30–22:00 — Epílogo (3–4 minutos)

Revisá en las reglas de Odin qué tiene que tener el epílogo y ajustá este texto si piden algo distinto.

> 🖱️ I'm scrolling slowly through the Budget sheet with the mouse wheel, to go over the decisions I made.
>
> (Recorro despacio la hoja Budget con la rueda del mouse, para repasar las decisiones que tomé.)
>
> 🟢 In this epilogue, I want to go over my approach. I kept the raw transactions in one sheet and the summary in another. The summary never has typed numbers, only formulas, so if a new expense is added to Transactions, every total, percentage, alert, and the chart update automatically.
>
> (En este epílogo quiero repasar mi enfoque. Dejé los gastos en una hoja y el resumen en otra. El resumen nunca tiene números escritos a mano, solo fórmulas, así que si se agrega un gasto nuevo en Transactions, todos los totales, porcentajes, alertas y el gráfico se actualizan solos.)
>
> 🟢 I used SUMIF with whole columns, C and D, so new rows are included without changing the formula. I used an absolute reference for the income in B1, and relative references for everything else, so one formula works for every row.
>
> (Usé SUMIF con columnas completas, C y D, así las filas nuevas se incluyen sin cambiar la fórmula. Usé una referencia absoluta para el ingreso en B1 y referencias relativas para todo lo demás, así una sola fórmula sirve para todas las filas.)
>
> 🟢 The 80 percent alert is a warning, not a problem. It tells us to watch a category before it goes over budget. Dining Out is the real problem this month, and Groceries and Health need attention. Rent is flagged too, which shows a limit of a single rule: fixed costs always reach 100 percent.
>
> (La alerta del 80 por ciento es un aviso, no un problema. Nos dice que vigilemos una categoría antes de que se pase del presupuesto. Dining Out es el problema real de este mes, y Groceries y Health necesitan atención. Rent también aparece marcado, lo que muestra un límite de usar una sola regla: los costos fijos siempre llegan al 100 por ciento.)
>
> 🟢 As next steps, I could add a separate rule for fixed costs, track several months to see trends, or add a Savings category for the 1,940 dollars left. For the person managing this budget, the clear action is to reduce dining out next month. Thanks for watching!
>
> (Como próximos pasos, podría agregar una regla aparte para los costos fijos, seguir varios meses para ver tendencias o agregar una categoría de ahorro para los 1.940 dólares que sobran. Para quien maneja este presupuesto, la acción clara es reducir las comidas afuera el mes que viene. ¡Gracias por mirar!)

Si el reloj todavía no pasó los 15:00, no cortes: recorré otra vez las fórmulas celda por celda, haciendo clic en cada una para que se vea en la barra de fórmulas.

---

## Después de grabar

1. Para los entregables: abrí el menú **File → Download → Microsoft Excel (.xlsx)** y, si lo piden, compartí el enlace de la hoja.
2. Ejecutá **Run full AutoQC**, no solo *Rerun failing*.
3. Subí los **cuatro archivos por separado**: el **MP4**, el **ZIP original de TaskRecorder**, **Deliverables.zip** y **Metadata.rtf**.
