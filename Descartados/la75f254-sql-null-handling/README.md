# la75f254 — SQL NULL Handling

Guion paso a paso para grabar la tarea **la75f254** en **DBeaver**. Una consulta de precios devuelve NULL en el precio final cuando falta el descuento, y no avisa. En la grabación inspeccionás la tabla `products` y reproducís el error. Rastreás cómo se propaga el NULL, definís una política explícita y lo corregís con **COALESCE**. Después creás pruebas reutilizables y exportás un reporte de antes y después. La grabación tiene que durar **entre 15:00 y 50:59**. Este guion apunta a unos **22 minutos**, epílogo incluido.

**Cómo leer este guion:**

- Las frases que empiezan con 🖱️ las decís **en el momento de hacer clic, desplazarte o escribir**. Siempre dicen **qué** elemento usás, **dónde** está en la pantalla y **por qué** lo usás. Son las que revisa AutoQC.
- Las frases que empiezan con 🟢 son la explicación que **decís en inglés** entre una acción y otra.
- Debajo de cada consulta, la lista **What each line does** explica cada parte en inglés. La leés en voz alta mientras la escribís.
- El resto, en castellano, es lo que hacés en pantalla. Las traducciones aparecen entre paréntesis después de cada frase.

> **Importante:** el Goal de Studio tiene prioridad sobre este guion. Antes de grabar, revisá el apartado **Starting materials** de la tarea: si Studio trae su propia base de datos, usá esa y adaptá los nombres de tabla y columnas. Si no trae nada, usá `pricing.db` de esta carpeta.

---

## Archivos de la carpeta

```
la75f254-sql-null-handling/
├── README.md                  ← este guion
├── pricing.db                 ← material de partida: base SQLite con la tabla products
├── setup.sql                  ← el script que crea la misma tabla, por si necesitás recrearla
└── solution/                  ← solución de referencia (NO la abras durante la grabación)
    ├── fixed_price_query.sql  ← la consulta corregida
    └── edge_case_tests.sql    ← las pruebas
```

---

## La tabla `products`

12 productos ficticios de un equipo de precios. **4 no tienen descuento cargado** (`discount_pct` es NULL):

| id | name | price | discount_pct | Precio final hoy | Precio final corregido |
| -: | ---- | ----: | -----------: | ---------------: | ---------------------: |
| 1 | Wireless Mouse | 25.00 | 10 | 22.50 | 22.50 |
| **2** | **USB-C Cable** | 12.50 | **NULL** | **NULL** | **12.50** |
| 3 | Desk Lamp | 40.00 | 15 | 34.00 | 34.00 |
| 4 | Coffee Mug | 9.99 | 0 | 9.99 | 9.99 |
| **5** | **Board Game** | 34.90 | **NULL** | **NULL** | **34.90** |
| 6 | Puzzle 1000 pcs | 18.00 | 20 | 14.40 | 14.40 |
| 7 | Notebook Pack | 7.50 | 5 | 7.13 | 7.13 |
| **8** | **Cookbook** | 29.00 | **NULL** | **NULL** | **29.00** |
| 9 | Bluetooth Speaker | 59.99 | 25 | 44.99 | 44.99 |
| 10 | Throw Pillow | 22.00 | 10 | 19.80 | 19.80 |
| 11 | Action Figure | 15.00 | 0 | 15.00 | 15.00 |
| **12** | **Mystery Novel** | 14.99 | **NULL** | **NULL** | **14.99** |

**Política que vas a aplicar:** si falta el descuento, se toma como **0%** (se vende a precio completo). La suma de los precios finales pasa de 167,81 (sin contar los 4 NULL) a **259,20**.

Todas las consultas de este guion las probé sobre `pricing.db` y dan estos resultados.

---

## Antes de grabar

1. Leé el Goal y compará este guion con el campo **Describe your idea** de Studio.
2. Instalá DBeaver Community si no lo tenés (https://dbeaver.io). **Conectate una vez a `pricing.db` antes de grabar**: la primera vez, DBeaver pide descargar el driver de SQLite. Así no aparece ese aviso en la grabación. Después borrá esa conexión.
3. Copiá `pricing.db` a una carpeta fácil de encontrar, por ejemplo `Escritorio\pricing`. Creá también una carpeta vacía `Escritorio\pricing\deliverables` para los archivos que vas a guardar.
4. Practicá una vez entera, leyendo en voz alta las frases 🖱️ y 🟢, y cronometrá. Comprobá cómo se ven en tu DBeaver los menús **File → Save As** y **Export data**.
5. Dejá abiertos el documento **Goal** en el navegador y DBeaver. Agrandá la letra del editor (`Ctrl + +` o *Window → Preferences*).
6. Maximizá la ventana que estés mostrando y cerrá o minimizá las demás, para que ninguna tape a otra.
7. Pausa de ~1 segundo después de cada clic y nunca más de 45 segundos en silencio.
8. No muestres Studio, Mercor, información privada ni herramientas de IA, ni la carpeta `solution`. Cerrá este guion si está en la misma pantalla.

---

## 0:00–0:45 — Mostrar el Goal

> 🖱️ I'm on the Goal document in the browser, to show what this task asks for.
>
> (Estoy en el documento del Goal, en el navegador, para mostrar qué pide esta tarea.)
>
> 🟢 As a software engineer supporting a pricing team, I'll fix a discount query that silently returns NULL for the final price when the discount is missing. I'll reproduce it, trace it, fix it with COALESCE, write test queries, and export a before and after report.
>
> (Como ingeniero de software que da soporte a un equipo de precios, voy a corregir una consulta de descuentos que devuelve NULL en el precio final, sin avisar, cuando falta el descuento. La voy a reproducir, rastrear y corregir con COALESCE, voy a escribir consultas de prueba y voy a exportar un reporte de antes y después.)

---

## 0:45–4:00 — Conectarse a la base e inspeccionar la tabla

> 🖱️ I'm clicking the DBeaver icon in the taskbar at the bottom of the screen, to open the database tool.
>
> (Hago clic en el ícono de DBeaver en la barra de tareas, abajo de la pantalla, para abrir la herramienta de bases de datos.)
>
> 🟢 DBeaver is a free database tool. It lets me connect to a database, browse its tables, and run SQL queries. This database is SQLite, a small database stored in a single file.
>
> (DBeaver es una herramienta gratuita de bases de datos. Me permite conectarme a una base, recorrer sus tablas y ejecutar consultas SQL. Esta base es SQLite, una base de datos chica guardada en un solo archivo.)
>
> 🖱️ I'm opening the Database menu at the top and choosing New Database Connection, to connect to the pricing database.
>
> (Abro el menú Database de arriba y elijo New Database Connection, para conectarme a la base de precios.)
>
> 🖱️ I'm clicking SQLite in the list of databases, in the middle of the dialog, and then the Next button at the bottom.
>
> (Hago clic en SQLite en la lista de bases de datos, en el medio del cuadro, y después en el botón Next, abajo.)
>
> 🖱️ I'm clicking the Open button next to the Path field, and choosing pricing.db in the pricing folder on the Desktop, to point the connection to the file.
>
> (Hago clic en el botón Open al lado del campo Path y elijo pricing.db en la carpeta pricing del Escritorio, para que la conexión apunte al archivo.)
>
> 🖱️ I'm clicking the Finish button at the bottom right, to create the connection.
>
> (Hago clic en el botón Finish, abajo a la derecha, para crear la conexión.)
>
> 🖱️ In the Database Navigator on the left, I'm expanding pricing.db, then Tables, and double-clicking products, to see the table.
>
> (En el Database Navigator de la izquierda, despliego pricing.db, después Tables, y hago doble clic en products, para ver la tabla.)
>
> 🖱️ I'm clicking the Data tab at the top of the table panel, to see the rows.
>
> (Hago clic en la pestaña Data, arriba del panel de la tabla, para ver las filas.)
>
> 🟢 The products table has 12 products, with an id, a name, a category, a price, and a discount percentage. Notice that some rows show NULL in the discount column. NULL in SQL means "unknown" or "missing". It's not the same as zero.
>
> (La tabla products tiene 12 productos, con un id, un nombre, una categoría, un precio y un porcentaje de descuento. Fíjense que algunas filas muestran NULL en la columna de descuento. NULL en SQL significa "desconocido" o "faltante". No es lo mismo que cero.)

---

## 4:00–9:30 — Encontrar los NULL, reproducir el error y rastrearlo

> 🖱️ I'm right-clicking pricing.db in the Database Navigator on the left, and choosing SQL Editor, then Open SQL script, to write queries.
>
> (Hago clic derecho en pricing.db en el Database Navigator de la izquierda y elijo SQL Editor y después Open SQL script, para escribir consultas.)

Escribís la **consulta 1**:

```sql
SELECT id, name, price, discount_pct
FROM products
WHERE discount_pct IS NULL;
```

**What each line does:**

- 🟢 `SELECT id, name, price, discount_pct`: these are the columns I want to see.
- 🟢 `FROM products`: from the products table.
- 🟢 `WHERE discount_pct IS NULL;`: only the rows where the discount is missing. In SQL, I must write IS NULL. If I write equals NULL, it finds nothing, because NULL is never equal to anything, not even to another NULL.

> 🖱️ I'm placing the cursor on the query and clicking the Execute SQL statement button, the orange play icon on the left side of the editor, to run it.
>
> (Pongo el cursor en la consulta y hago clic en el botón Execute SQL statement, el ícono naranja de play del costado izquierdo del editor, para ejecutarla.)
>
> 🟢 Four products have no discount: the USB-C Cable, the Board Game, the Cookbook, and the Mystery Novel.
>
> (Cuatro productos no tienen descuento: USB-C Cable, Board Game, Cookbook y Mystery Novel.)

Debajo escribís la **consulta 2**, la original con el error:

```sql
SELECT id, name, price, discount_pct,
       ROUND(price - price * discount_pct / 100, 2) AS final_price
FROM products;
```

**What each line does:**

- 🟢 `SELECT id, name, price, discount_pct,`: the product and its discount.
- 🟢 `ROUND(price - price * discount_pct / 100, 2) AS final_price`: this is the original formula. It takes the price, subtracts the price times the discount divided by 100, and rounds to two decimals. AS gives the result the name final_price.
- 🟢 `FROM products;`: for every product.

> 🖱️ I'm clicking on this second query and pressing the Execute SQL statement button on the left of the editor, to reproduce the problem.
>
> (Hago clic en esta segunda consulta y presiono el botón Execute SQL statement, a la izquierda del editor, para reproducir el problema.)
>
> 🟢 Here's the bug. For the four products without a discount, the final price is NULL. The query doesn't show any error. It just returns an empty price, so a store could show no price, or a report could ignore these products. That's why it's called a silent error.
>
> (Acá está el error. En los cuatro productos sin descuento, el precio final es NULL. La consulta no muestra ningún error. Solo devuelve un precio vacío, así que una tienda podría no mostrar el precio, o un reporte podría ignorar estos productos. Por eso se lo llama error silencioso.)

Para rastrear cómo se propaga el NULL, escribís la **consulta 3**:

```sql
SELECT name, price, discount_pct,
       discount_pct / 100 AS discount_rate,
       price * discount_pct / 100 AS discount_amount,
       price - price * discount_pct / 100 AS final_price
FROM products
WHERE id = 2;
```

**What each line does:**

- 🟢 `SELECT name, price, discount_pct,`: the USB-C Cable, which has no discount.
- 🟢 `discount_pct / 100 AS discount_rate,`: step one of the formula: the discount divided by 100.
- 🟢 `price * discount_pct / 100 AS discount_amount,`: step two: the price times that rate, the money we take off.
- 🟢 `price - price * discount_pct / 100 AS final_price`: step three: the price minus the discount amount.
- 🟢 `WHERE id = 2;`: only for product 2, so I can follow one row step by step.

> 🖱️ I'm clicking on the third query and pressing the Execute SQL statement button, to trace the calculation step by step.
>
> (Hago clic en la tercera consulta y presiono el botón Execute SQL statement, para rastrear el cálculo paso a paso.)
>
> 🟢 Every step is NULL. That's how NULL works in SQL arithmetic: any math with NULL gives NULL. NULL divided by 100 is NULL, the price times NULL is NULL, and 12.50 minus NULL is also NULL. So one missing value in the discount spreads through the whole expression to the final price.
>
> (Todos los pasos dan NULL. Así funciona NULL en la aritmética de SQL: cualquier cuenta con NULL da NULL. NULL dividido 100 es NULL, el precio por NULL es NULL, y 12,50 menos NULL también es NULL. Entonces un solo valor faltante en el descuento se propaga por toda la expresión hasta el precio final.)

---

## 9:30–12:30 — La política y la corrección con COALESCE

> 🟢 Before fixing it, I need an explicit policy: what should a missing discount mean? I'll treat it as no discount, zero percent, so the product is sold at full price. It's the safest choice: we never give a discount that nobody approved, and every product gets a price.
>
> (Antes de corregirlo necesito una política explícita: ¿qué tiene que significar un descuento faltante? Lo voy a tomar como sin descuento, cero por ciento, así el producto se vende a precio completo. Es la opción más segura: nunca damos un descuento que nadie aprobó, y todos los productos tienen precio.)

Escribís la **consulta 4**, la corregida:

```sql
-- Policy: a NULL discount means "no discount", so the product is sold at full price.
SELECT id, name, price, discount_pct,
       ROUND(price - price * COALESCE(discount_pct, 0) / 100, 2) AS final_price
FROM products;
```

**What each line does:**

- 🟢 `-- Policy: ...`: two dashes start a comment. I write the policy right in the query, so anyone who reads it knows the decision.
- 🟢 `SELECT id, name, price, discount_pct,`: the same columns as before.
- 🟢 `COALESCE(discount_pct, 0)`: COALESCE returns the first value that is not NULL. If the discount exists, it uses it. If it's NULL, it uses zero. Everything else in the formula stays the same.
- 🟢 `FROM products;`: for every product.

> 🖱️ I'm clicking on the corrected query and pressing the Execute SQL statement button on the left of the editor, to check the fix.
>
> (Hago clic en la consulta corregida y presiono el botón Execute SQL statement, a la izquierda del editor, para comprobar la corrección.)
>
> 🟢 Now every product has a final price. The four products without a discount show their full price, for example 12.50 for the USB-C Cable. And the products that had a discount didn't change: the Wireless Mouse is still 22.50.
>
> (Ahora todos los productos tienen precio final. Los cuatro productos sin descuento muestran su precio completo, por ejemplo 12,50 el USB-C Cable. Y los productos que tenían descuento no cambiaron: el Wireless Mouse sigue en 22,50.)
>
> 🟢 Notice I fixed the query, not the data. I didn't change the NULLs in the table to zero, because the missing values are information too: the pricing team may want to fill them later.
>
> (Fíjense que corregí la consulta, no los datos. No cambié los NULL de la tabla por cero, porque los valores faltantes también son información: el equipo de precios quizás quiera completarlos después.)

Guardás la consulta corregida como entregable. Borrás del editor las consultas 1 a 3 (o las dejás en otro script) y dejás solo la 4:

> 🖱️ I'm opening the File menu at the top left and choosing Save As, and saving the script as fixed_price_query.sql in the deliverables folder, to keep the corrected query.
>
> (Abro el menú File, arriba a la izquierda, elijo Save As y guardo el script como fixed_price_query.sql en la carpeta deliverables, para conservar la consulta corregida.)

---

## 12:30–16:30 — Pruebas reutilizables

> 🖱️ I'm right-clicking pricing.db in the Database Navigator, and choosing SQL Editor, then Open SQL script, to write the tests in a new script.
>
> (Hago clic derecho en pricing.db en el Database Navigator y elijo SQL Editor y después Open SQL script, para escribir las pruebas en un script nuevo.)

Escribís la **prueba 1**:

```sql
-- Test 1: edge cases for the final price formula (every row must say PASS).
WITH test_cases (test_name, price, discount_pct, expected) AS (
    VALUES ('NULL discount', 100.0, NULL, 100.0),
           ('Zero discount', 100.0, 0, 100.0),
           ('Normal discount', 80.0, 25, 60.0),
           ('Full discount', 50.0, 100, 0.0),
           ('Zero price', 0.0, 10, 0.0)
)
SELECT test_name, price, discount_pct, expected,
       ROUND(price - price * COALESCE(discount_pct, 0) / 100, 2) AS actual,
       CASE WHEN ROUND(price - price * COALESCE(discount_pct, 0) / 100, 2) = expected
            THEN 'PASS' ELSE 'FAIL' END AS result
FROM test_cases;
```

**What each line does:**

- 🟢 `WITH test_cases (...) AS (VALUES ...)`: WITH creates a small temporary table called test_cases, only for this query. Each row is one test: a name, a price, a discount, and the expected final price. It doesn't touch the real table, so I can run it any time.
- 🟢 `'NULL discount', 100.0, NULL, 100.0`: the main case. With no discount, 100 must stay 100.
- 🟢 `'Zero discount'`, `'Normal discount'`, `'Full discount'`, `'Zero price'`: the other edge cases: zero percent, a normal 25 percent, a full 100 percent discount that must give zero, and a free product.
- 🟢 `ROUND(price - price * COALESCE(discount_pct, 0) / 100, 2) AS actual`: the corrected formula, applied to each test case.
- 🟢 `CASE WHEN ... = expected THEN 'PASS' ELSE 'FAIL' END AS result`: CASE compares the actual result with the expected one and writes PASS or FAIL.

> 🖱️ I'm clicking on the test query and pressing the Execute SQL statement button on the left of the editor, to run the tests.
>
> (Hago clic en la consulta de prueba y presiono el botón Execute SQL statement, a la izquierda del editor, para ejecutar las pruebas.)
>
> 🟢 All five edge cases say PASS.
>
> (Los cinco casos límite dicen PASS.)

Escribís debajo las **pruebas 2 y 3**, que revisan la tabla real:

```sql
-- Test 2: no product may have a NULL final price (expected: 0).
SELECT COUNT(*) AS null_final_prices
FROM products
WHERE ROUND(price - price * COALESCE(discount_pct, 0) / 100, 2) IS NULL;

-- Test 3: every final price must be between 0 and the original price (expected: 0).
SELECT COUNT(*) AS out_of_range
FROM products
WHERE ROUND(price - price * COALESCE(discount_pct, 0) / 100, 2) NOT BETWEEN 0 AND price;
```

**What each line does:**

- 🟢 `SELECT COUNT(*) AS null_final_prices`: test 2 counts how many products still have a NULL final price. The answer must be zero.
- 🟢 `WHERE ... IS NULL;`: it looks for NULL results of the corrected formula.
- 🟢 `SELECT COUNT(*) AS out_of_range`: test 3 counts final prices that make no sense.
- 🟢 `WHERE ... NOT BETWEEN 0 AND price;`: a final price below zero or above the original price would be wrong. The answer must be zero too.

> 🖱️ I'm clicking the Execute SQL script button, the icon with a play sign and lines on the left of the editor, to run all the tests together.
>
> (Hago clic en el botón Execute SQL script, el ícono con un play y unas líneas a la izquierda del editor, para ejecutar todas las pruebas juntas.)
>
> 🖱️ I'm clicking each result tab at the bottom of the screen, to check the result of each test.
>
> (Hago clic en cada pestaña de resultados, abajo de la pantalla, para revisar el resultado de cada prueba.)
>
> 🟢 Test 1 has five PASS rows, and tests 2 and 3 both return zero. These tests are reusable: if someone changes the query later, they can run this script again and see right away if something broke.
>
> (La prueba 1 tiene cinco filas PASS, y las pruebas 2 y 3 devuelven cero. Estas pruebas son reutilizables: si alguien cambia la consulta más adelante, puede ejecutar este script de nuevo y ver enseguida si algo se rompió.)
>
> 🖱️ I'm opening the File menu and choosing Save As, and saving this script as edge_case_tests.sql in the deliverables folder.
>
> (Abro el menú File, elijo Save As y guardo este script como edge_case_tests.sql en la carpeta deliverables.)

---

## 16:30–19:00 — Reporte de antes y después

> 🖱️ I'm right-clicking pricing.db in the Database Navigator, and choosing SQL Editor, then Open SQL script, to write the comparison report.
>
> (Hago clic derecho en pricing.db en el Database Navigator y elijo SQL Editor y después Open SQL script, para escribir el reporte comparativo.)

```sql
SELECT id, name, price, discount_pct,
       ROUND(price - price * discount_pct / 100, 2) AS final_price_before,
       ROUND(price - price * COALESCE(discount_pct, 0) / 100, 2) AS final_price_after,
       CASE WHEN discount_pct IS NULL THEN 'Fixed: no discount applied' ELSE 'Unchanged' END AS status
FROM products
ORDER BY id;
```

**What each line does:**

- 🟢 `SELECT id, name, price, discount_pct,`: the product data.
- 🟢 `... AS final_price_before,`: the old formula, so the report shows the NULL results.
- 🟢 `... AS final_price_after,`: the corrected formula, next to it.
- 🟢 `CASE WHEN discount_pct IS NULL THEN 'Fixed: no discount applied' ELSE 'Unchanged' END AS status`: a status column that tells the finance team which rows changed and why.
- 🟢 `ORDER BY id;`: sorts the products by id.

> 🖱️ I'm clicking the Execute SQL statement button on the left of the editor, to build the report.
>
> (Hago clic en el botón Execute SQL statement, a la izquierda del editor, para armar el reporte.)
>
> 🟢 Now the before and after are side by side. Eight products are unchanged, and the four products without a discount now have a price instead of NULL.
>
> (Ahora el antes y el después están lado a lado. Ocho productos no cambian, y los cuatro productos sin descuento ahora tienen precio en vez de NULL.)
>
> 🖱️ I'm right-clicking the results grid at the bottom, and choosing Export data, to save the report as a file.
>
> (Hago clic derecho en la grilla de resultados de abajo y elijo Export data, para guardar el reporte como archivo.)
>
> 🖱️ I'm choosing CSV in the list of formats, in the middle of the export wizard, and clicking Next at the bottom, to create a file the finance team can open in Excel.
>
> (Elijo CSV en la lista de formatos, en el medio del asistente de exportación, y hago clic en Next, abajo, para crear un archivo que el equipo de finanzas pueda abrir en Excel.)
>
> 🖱️ I'm clicking Next on the settings pages, and in the Output page I'm choosing the deliverables folder as the directory and typing price_fix_report as the file name.
>
> (Hago clic en Next en las páginas de configuración, y en la página Output elijo la carpeta deliverables como directorio y escribo price_fix_report como nombre del archivo.)
>
> 🖱️ I'm clicking the Proceed button at the bottom right, to export the report.
>
> (Hago clic en el botón Proceed, abajo a la derecha, para exportar el reporte.)

Si DBeaver muestra un aviso de exportación terminada: *"I'm closing this notification at the bottom right, because the export finished."*

---

## 19:00–22:30 — Epílogo (3–4 minutos)

Revisá en las reglas de Odin qué tiene que tener el epílogo y ajustá este texto si piden algo distinto.

> 🖱️ I'm clicking the fixed_price_query.sql tab at the top of the editor, to go over the fix.
>
> (Hago clic en la pestaña fixed_price_query.sql, arriba del editor, para repasar la corrección.)
>
> 🟢 In this epilogue, I want to go over my approach. I started by finding the affected rows and reproducing the NULL results, so I knew exactly which products were broken: four of twelve.
>
> (En este epílogo quiero repasar mi enfoque. Empecé por encontrar las filas afectadas y reproducir los resultados NULL, así sabía exactamente qué productos estaban mal: cuatro de doce.)
>
> 🟢 Then I traced the expression step by step. The root cause is how SQL treats NULL: any arithmetic with NULL returns NULL, and SQL doesn't warn you. That's what makes this kind of bug dangerous: totals and reports quietly ignore the missing rows.
>
> (Después rastreé la expresión paso a paso. La causa de fondo es cómo trata SQL a NULL: cualquier cuenta con NULL devuelve NULL, y SQL no avisa. Eso es lo que hace peligroso a este tipo de error: los totales y los reportes ignoran en silencio las filas faltantes.)
>
> 🟢 The fix was COALESCE with an explicit policy: a missing discount means zero discount. I wrote the policy as a comment in the query, because the most important part of this fix is the decision, not the function. Another team might prefer to flag those products instead, and that should be a conscious choice.
>
> (La corrección fue COALESCE con una política explícita: un descuento faltante significa descuento cero. Escribí la política como comentario en la consulta, porque lo más importante de esta corrección es la decisión, no la función. Otro equipo podría preferir marcar esos productos, y eso tendría que ser una elección consciente.)
>
> 🖱️ I'm clicking the edge_case_tests.sql tab at the top of the editor, to talk about the tests.
>
> (Hago clic en la pestaña edge_case_tests.sql, arriba del editor, para hablar de las pruebas.)
>
> 🟢 The tests don't depend on the current data. The edge cases live inside the query, so they always check the same situations, including a full discount and a free product. The table checks make sure no NULL or impossible price ever reaches the store.
>
> (Las pruebas no dependen de los datos actuales. Los casos límite están adentro de la consulta, así que siempre revisan las mismas situaciones, incluidos un descuento total y un producto gratis. Los chequeos sobre la tabla aseguran que ningún precio NULL o imposible llegue a la tienda.)
>
> 🟢 As next steps, I would add a NOT NULL constraint with a default of zero on the discount column, or a check that discounts stay between 0 and 100, so bad data can't enter in the first place. I would also ask the pricing team to fill in the four missing discounts. Thanks for watching!
>
> (Como próximos pasos, agregaría una restricción NOT NULL con un valor por defecto de cero en la columna de descuento, o un chequeo para que los descuentos estén entre 0 y 100, así los datos incorrectos no pueden entrar desde el principio. También le pediría al equipo de precios que complete los cuatro descuentos faltantes. ¡Gracias por mirar!)

Si el reloj todavía no pasó los 15:00, no cortes: volvé a ejecutar las pruebas y explicá cada caso límite.

---

## Después de grabar

1. Ejecutá **Run full AutoQC**, no solo *Rerun failing*.
2. Subí los **cuatro archivos por separado**: el **MP4**, el **ZIP original de TaskRecorder**, **Deliverables.zip** (con `fixed_price_query.sql`, `edge_case_tests.sql` y `price_fix_report.csv`) y **Metadata.rtf**.
