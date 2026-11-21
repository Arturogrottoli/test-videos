# oyi436dd — E-commerce Financial Reconstruction

Guion para volver a grabar la tarea **oyi436dd** respetando la idea aprobada. Se graba en **Google Colab** (app principal), con **Firefox** como app de apoyo, en una sola toma.

> **Goal:** *Reconstruct the financial position of a simulated e-commerce business by reconciling customer orders, payment transactions, processor settlements, refunds, and product costs. Deliver an auditable transaction-level ledger that explains revenue differences, settlement discrepancies, and unresolved financial movements.*

**Duración estimada: ~38:45** (tipeo ≤35%). Es más que el objetivo de 25 min, pero vos elegiste priorizar el límite de tipeo; Odin acepta hasta 50:59.

**Punto de partida al grabar:** el notebook está **vacío** (una celda de código sin nada) y los cinco CSV ya están subidos en el panel **Files** de Colab. **Todo el código se tipea en vivo**, incluida la celda 1.

**Por qué se rechazó la grabación anterior y qué cambia:** la versión anterior deduplicaba identidades de clientes y armaba perfiles de comportamiento: eso no estaba en la idea aprobada. Esta versión hace solamente reconstrucción financiera:

- No se deduplican clientes ni se normalizan teléfonos. `customer_id` se deja tal como viene.
- No hay perfiles, ni segmentación, ni marketing.
- **No se sobrescribe ningún CSV de entrada.** Los tres archivos que se generan tienen nombres nuevos.

---

## Cronograma

| # | Bloque | Fase | Celda | TIME | Duración |
| - | ------ | ---- | ----- | ---- | -------- |
| 0 | Opening | — | — | 0:00–1:42 | 1:42 |
| 1 | Carga e inspección de los cinco archivos | 1. Input inspection | 1 | 1:42–5:54 | 4:12 |
| 2 | Validación de datos | 2. Data validation | 2 | 5:54–8:30 | 2:36 |
| 3 | Conciliación de pagos | 3. Payment reconciliation | 3 | 8:30–12:22 | 3:53 |
| 4 | Conciliación con las liquidaciones del procesador | 4. Processor settlement | 4 | 12:22–15:22 | 3:00 |
| 5 | Conciliación de reembolsos | 5. Refund reconciliation | 5 | 15:22–18:01 | 2:38 |
| 6 | Costos de productos y margen | 6. Product cost | 6 | 18:01–20:38 | 2:38 |
| 7 | Registro de excepciones | 7. Exception register | 7 | 20:38–26:44 | 6:06 |
| 8 | Entregables y resumen de control | 7. Deliverables | 8 | 26:44–31:57 | 5:13 |
| 9 | Validación contra las fuentes y revisión de los archivos | 7. Validation | 9 | 31:57–35:40 | 3:43 |
| 10 | Conclusiones | — | texto | 35:40–37:01 | 1:22 |
| 11 | Epilogue | — | — | 37:01–38:45 | 1:44 |
| | **Total** | | | | **~38:45** |

*(Calculado con 130 palabras/min de narración, 135 caracteres/min de tipeo en silencio, todo sumado, más ~20 s de navegación y ejecución por bloque.)*

---

## Archivos de entrada

Sintéticos, generados con IA antes de grabar. Período: Q4 2025 (del 2025-10-01 al 2025-12-31).

| Archivo | Filas | Columnas | Qué es |
| ------- | ----- | -------- | ------ |
| `orders.csv` | 1.180 | `order_id, customer_id, order_date, product_id, quantity, order_total` | Un pedido por fila |
| `payments.csv` | 1.243 | `payment_id, order_id, method, amount, status, created_at, payout_id, settled` | Cada intento de cobro (`captured` o `failed`). Si el procesador ya lo liquidó, trae el lote (`payout_id`) y el neto recibido (`settled`) |
| `refunds.csv` | 76 | `refund_id, payment_id, amount, refund_date` | Reembolsos parciales y totales, ligados al pago |
| `products.csv` | 25 | `product_id, product_name, category, unit_price, unit_cost` | Precio y costo unitario |
| `processor_terms.csv` | 3 | `method, fee_pct, fee_fixed, payout_days` | Comisión del procesador por medio de pago y días hasta la liquidación |

**Claves de relación:** `orders.order_id` ↔ `payments.order_id`; `payments.payment_id` ↔ `refunds.payment_id`; `orders.product_id` ↔ `products.product_id`; `payments.method` ↔ `processor_terms.method`.

**Problemas que tienen los datos** (los encuentra el código; no hace falta saberlos antes):

| Problema | Cantidad | Dólares | Dónde se detecta |
| -------- | -------- | ------- | ---------------- |
| Filas de pedidos duplicadas por la exportación | 30 | $3,235.00 | Celda 2 |
| Intentos de cobro fallidos (no son ingreso) | 104 | $12,501.00 | Celda 3 |
| Pedidos sin cobro capturado (10 solo con intentos fallidos, 6 sin ningún intento) | 16 | $2,300.00 | Celda 3 |
| Cobros de pedidos que no existen | 5 | $411.00 | Celda 3 |
| Cobros por un monto distinto al del pedido | 8 | $865.00 facturados, $883.00 cobrados | Celda 7 |
| Liquidaciones con menos plata que el neto esperado | 6 | $108.70 | Celda 4 |
| Cobros todavía no liquidados al cierre (29 al 31 de diciembre) | 26 | $1,966.00 | Celda 7 |
| Reembolsos sin un cobro válido (2 a intentos fallidos, 2 a IDs inexistentes) | 4 | $488.00 | Celda 5 |
| Pagos reembolsados dos veces | 2 | $217.00 de más | Celda 7 |
| Productos sin costo (P017, P022): no se puede calcular el margen | 90 líneas | $8,162.00 de ventas | Celda 6 |

**Cómo cubre cada fase del prompt:**

| Fase | Celda | Qué produce |
| ---- | ----- | ----------- |
| 1. Input inspection | 1 | Carga de los cinco archivos; filas, columnas, tipos y vacíos de cada uno |
| 2. Data validation | 2 | 30 filas duplicadas ($3,235) fuera; IDs de pedidos y pagos únicos |
| 3. Payment reconciliation | 3 | Solo cuentan los cobros capturados; pedidos sin cobro y cobros sin pedido |
| 4. Processor settlement | 4 | Comisión según `processor_terms.csv`; diferencia entre el neto esperado y el liquidado |
| 5. Refund reconciliation | 5 | Reembolsos ligados al cobro; $488 sin cobro válido |
| 6. Product cost | 6 | Costo y margen por transacción; 2 productos sin costo |
| 7. Final deliverables | 7, 8, 9 | `exception_register.csv` (187 filas), `transaction_reconciliation_ledger.csv` (1.155 filas), `financial_control_summary.csv` y la validación contra las fuentes |

**Los puentes que cierran** (para el epílogo y por si te preguntan):

- **Ingresos:** facturado $114,484.00 − pedidos sin cobro $2,300.00 + diferencia de montos $18.00 + cobros sin pedido $411.00 = **capturado $112,613.00**.
- **Liquidaciones:** capturado $112,613.00 − comisiones $3,488.53 − liquidado $107,100.21 − faltante $108.70 = **$1,915.56**, que es el neto pendiente de los 26 cobros de fin de año ($1,966.00 − $50.44 de comisión).

---

## Cómo leer este guion

Cada bloque tiene:

- **TIME:** inicio, fin y duración.
- **WHAT I DO:** la acción, en orden.
- **WHERE:** dónde está en pantalla.
- **SAY:** lo que decís, en inglés, intercalado con el código:
  - 🖱️ = lo decís **mientras hacés** la acción con el mouse: qué, dónde y por qué.
  - 🗣️⌨️ = lo decís **con las manos fuera del teclado**, y **después** tipeás el bloque de abajo **en silencio**.
  - 🟢 = lo decís con el mouse quieto: qué muestra el resultado y qué decidís.
- **WHY:** el criterio técnico, para vos. **Ya está dentro de lo que decís**; no se lee aparte.
- **EXPECTED RESULT:** qué tiene que aparecer.
- **VERIFY BEFORE CONTINUING:** qué controlar antes de pasar al bloque siguiente. Si no da, mirá "Si algo sale mal".
- 📘 = qué hace cada línea, en inglés. Es para vos: **no se lee**.

---

## Estrategia de tiempo y tipeo

| | Cantidad | Tiempo |
| - | -------- | ------ |
| Tipeo en vivo (celdas 1 a 9 + conclusiones) | 1.826 caracteres | ~13,5 min a 135 car./min (~15,2 a 120) |
| Narración | ~2.759 palabras | ~21,2 min |
| Navegación y ejecución | 12 bloques | ~4,0 min |
| **Total** | | **~38:45** (~40:26 si tipeás a 120 car./min) |

**Tipeo: ~35% del video a 135 car./min** (~38% a 120).

**Qué se hizo para que todo entre tipeado:**

- Nombres cortos: `o` pedidos, `p` pagos, `r` reembolsos, `k` productos, `t` condiciones del procesador, `c` cobros capturados, `L` ledger, `x` excepciones, `s` resumen.
- Los cinco archivos se cargan con una sola línea.
- Un único ledger `L` al que cada fase le agrega columnas. Las excepciones salen de una sola regla por tipo.

**Reglas de tipeo:**

1. **Nunca hablar y tipear al mismo tiempo.** Frase 🗣️⌨️ con las manos quietas → bloque en silencio.
2. **Ningún tramo pasa de 45 segundos.** Las líneas largas de las celdas 7, 8 y 9 se tipean en dos tramos, **sin Enter** entre ellos.
3. **Nada de tipeo extra:** ni comentarios ni `print` de prueba.
4. **Sin autocompletado.** Si aparece una caja de sugerencias, Escape.
5. **`~` en Mac** (celda 7): **Option + ñ** y después **espacio**.
6. **Celda 7, líneas 2 y 3:** van dentro de las llaves del diccionario. Si Colab ya pone la sangría solo, no agregues espacios: dentro de `{ }` la sangría no cambia nada.
7. **Comillas y corchetes:** si Colab cierra solo `"`, `(` o `[`, seguí tipeando igual: al escribir el de cierre, Colab lo salta.

---

## La regla del mouse y del teclado

1. El mouse **solo se mueve con una frase 🖱️**. Mientras tipeás, soltalo.
2. Al terminar una acción, el cursor queda **quieto en el margen derecho**.
3. **Primero la frase, después el movimiento o el tipeo.**
4. **Repetí el número de celda al menos una vez por minuto.** Las frases ya lo hacen.
5. Para agregar una celda: **+ Code**, arriba a la izquierda de la barra de Colab, debajo del menú. Agrega la celda debajo de la seleccionada.
6. Frases comodín:
   - *"I'm scrolling down inside the output of cell N, to see the last rows."*
   - *"I'm clicking at the end of line N in cell N, to fix a typo."*
   - *"I'm pressing Escape to close the suggestion box, because I type everything by hand."*
   - *"I'm waiting for cell N to finish; the spinner on its left is still running."*

---

## Guion de grabación

### Bloque 0. Opening

**TIME:** 0:00–1:42 (1:42)

**WHAT I DO:** hablar con la descripción de la tarea en pantalla → minimizar → abrir Colab desde el Dock → abrir el panel Files.

**WHERE:** Firefox ventana 1 (descripción). Botón amarillo arriba a la izquierda. Ícono de Firefox en el Dock, a la derecha (Mac); segunda ventana de la lista. Ícono de carpeta en la barra lateral izquierda de Colab.

**SAY:**

> 🟢 I will be beginning my task soon. The task is to rebuild the financial position of an online store for the last quarter of 2025.

> 🟢 I have five sources: orders, payment attempts, refunds, product costs, and the payment processor's fee terms. They don't agree with each other, and my job is to explain every difference.

> 🟢 By the end I'll have three files: a transaction-level ledger, an exception register, and a financial control summary that ties back to the sources.

> 🖱️ I'm clicking the yellow minimize button at the top left, to hide the task description.

> 🖱️ I'm clicking the Firefox icon in the Dock on the right, and choosing the second window: my empty Colab notebook.

> 🖱️ I'm clicking the folder icon in the left sidebar of Colab, to open the Files panel.

> 🖱️ I'm pointing at the five CSV files in the Files panel: orders, payments, refunds, products and processor terms. I uploaded them before recording. They're synthetic, generated with AI.

> 🟢 One rule for the whole session: I never overwrite these five files. Everything I produce gets a new file name.

**WHY:** el revisor tiene que ver desde el principio el objetivo, los cinco archivos de la idea aprobada y los tres entregables. Así puede comparar cada paso con la descripción.

**EXPECTED RESULT:** el notebook vacío con una celda de código, y el panel Files abierto con los cinco CSV.

**VERIFY BEFORE CONTINUING:** están los cinco archivos y no hay ningún otro CSV en Files.

---

### Bloque 1. Carga e inspección de los cinco archivos

**TIME:** 1:42–5:54 (4:12)

**WHAT I DO:** clic en la celda 1 → tipear 4 tramos → Run → recorrer la salida con scroll.

**WHERE:** celda 1, la única del notebook, a la derecha del panel Files.

**SAY:**

> 🖱️ I'm clicking inside cell one, the empty code cell at the top of the notebook.

> 🗣️⌨️ First two lines of cell one: pandas for the tables, and numpy for one labeling step later.

```python
import pandas as pd
import numpy as np
```
*(38 caracteres · ~17 s)*

> 🗣️⌨️ Next line of cell one: the five file names, in one string that I split into a list.

```python
n = "orders payments refunds products processor_terms".split()
```
*(62 caracteres · ~28 s)*

> 🗣️⌨️ Next line: read the five files, in that order, into five short names: o for orders, p for payments, r for refunds, k for products, and t for terms.

```python
o, p, r, k, t = [pd.read_csv(f + ".csv") for f in n]
```
*(52 caracteres · ~23 s)*

> 🗣️⌨️ Last lines of cell one: info for each table, which shows rows, columns, types and missing values. Then the terms table itself, because it's only three rows.

```python
for d in [o, p, r, k, t]: d.info()
t
```
*(36 caracteres · ~16 s)*

> 🖱️ I'm clicking the Run button on the left of cell one.

> 🖱️ I'm pointing at the first block under cell one, orders: 1,180 rows and six columns, with no missing values.

> 🟢 order_id links to payments, product_id links to products, and order_total is what the customer was billed.

> 🟢 customer_id is there too, but I leave it exactly as it is. This task is about money, not about who the customers are.

> 🖱️ I'm scrolling down inside the output of cell one, to the payments block: 1,243 rows.

> 🖱️ I'm pointing at payout_id and settled: only 1,113 non-null out of 1,243.

> 🟢 So 130 payments have no settlement. Some are failed attempts, which are never settled. The rest I'll have to explain.

> 🟢 The dates are text here. I don't need date math: they're in year-month-day format, so they also sort correctly as text.

> 🖱️ I'm scrolling down to refunds: 76 rows, linked by payment_id, not by order. So refunds attach to the payment first.

> 🖱️ I'm pointing at products: 25 rows, but unit_cost has only 23 values. Two products have no cost.

> 🖱️ I'm scrolling down to the terms table at the bottom of cell one.

> 🟢 Card costs 2.9 percent plus 30 cents and settles in two days. Wallet is 3.49 percent plus 49 cents, one day. Bank transfer is 0.8 percent, three days.

**WHY:** antes de unir nada hay que ver las claves y los vacíos. Los vacíos en `settled` y `unit_cost` anticipan dos excepciones: pagos sin liquidar y márgenes que no se pueden calcular.

**EXPECTED RESULT:**

- `orders`: `RangeIndex: 1180 entries`, 6 columnas, todas `1180 non-null`.
- `payments`: `1243 entries`, 8 columnas; `payout_id` y `settled` con `1113 non-null`.
- `refunds`: `76 entries`, 4 columnas.
- `products`: `25 entries`; `unit_cost` con `23 non-null`.
- `processor_terms`: `3 entries`.
- La tabla `t` al final: `card 0.0290 0.30 2`, `wallet 0.0349 0.49 1`, `bank_transfer 0.0080 0.00 3`.

**VERIFY BEFORE CONTINUING:** aparecen los cinco bloques de `info` y la tabla de condiciones. En Colab los tipos de texto aparecen como `object`; está bien.

📘 **What each line does** (para vos, no se lee):

- `import pandas as pd`: loads pandas.
- `import numpy as np`: loads numpy, used for `np.select` in cell 7.
- `n = "orders payments refunds products processor_terms".split()`: the five file names as a list.
- `o, p, r, k, t = [pd.read_csv(f + ".csv") for f in n]`: reads each file and unpacks the five tables.
- `for d in [o, p, r, k, t]: d.info()`: prints rows, columns, non-null counts and types for each table.
- `t`: shows the processor terms.

---

### Bloque 2. Validación de datos

**TIME:** 5:54–8:30 (2:36)

**WHAT I DO:** + Code → tipear 2 tramos → Run → señalar los cuatro valores.

**WHERE:** botón **+ Code** arriba a la izquierda; la celda 2 aparece debajo de la salida de la celda 1.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell two below the output of cell one.

> 🟢 Cell two is validation. Before matching anything, the keys have to be unique, or every join will double count.

> 🗣️⌨️ First two lines of cell two: keep the exact duplicate rows aside, so they go to the exceptions, then drop them from my working copy. The file on disk doesn't change.

```python
dup = o[o.duplicated()]
o = o.drop_duplicates()
```
*(47 caracteres · ~21 s)*

> 🗣️⌨️ Last line of cell two: how many duplicates, how many dollars they add, and whether order IDs and payment IDs are now unique.

```python
print(len(dup), dup.order_total.sum(), o.order_id.is_unique, p.payment_id.is_unique)
```
*(84 caracteres · ~37 s)*

> 🖱️ I'm clicking the Run button on the left of cell two.

> 🖱️ I'm pointing at the first two numbers under cell two: 30 rows and 3,235 dollars.

> 🟢 30 orders were exported twice. Kept in, they would inflate billed revenue by 3,235 dollars.

> 🖱️ I'm pointing at the two True values.

> 🟢 After removing them, every order ID is unique, so the duplicates were full copies, not two different orders with the same ID. And every payment ID is unique too.

**WHY:** se borran solo filas idénticas en todas las columnas: no hay riesgo de perder un pedido real. Si quedaran IDs repetidos con datos distintos, habría que investigarlos y no borrarlos.

**EXPECTED RESULT:** `30 3235.0 True True`

**VERIFY BEFORE CONTINUING:** los dos `True`. Si `o.order_id.is_unique` diera `False`, la unión de la celda 3 fallaría.

📘 **What each line does** (para vos, no se lee):

- `dup = o[o.duplicated()]`: rows that repeat an earlier row in every column.
- `o = o.drop_duplicates()`: working copy without those rows; `orders.csv` is not touched.
- `print(len(dup), dup.order_total.sum(), o.order_id.is_unique, p.payment_id.is_unique)`: count and dollars of duplicates, and two uniqueness checks.

---

### Bloque 3. Conciliación de pagos

**TIME:** 8:30–12:22 (3:53)

**WHAT I DO:** + Code → tipear 3 tramos → Run → señalar el monto y los tres grupos.

**WHERE:** **+ Code** arriba a la izquierda; la celda 3 aparece debajo de la salida de la celda 2.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell three below cell two.

> 🟢 Cell three matches orders with payments. A payment attempt isn't revenue: only a captured payment is money.

> 🗣️⌨️ First line of cell three: c is the captured payments only, joined with the terms by payment method, so each one carries its fee rate.

```python
c = p[p.status.eq("captured")].merge(t, on="method")
```
*(52 caracteres · ~23 s)*

> 🗣️⌨️ Next line of cell three: L is my ledger. An outer join keeps orders without a payment and payments without an order. The indicator marks which side each row came from, and validate one-to-one stops the cell if any order had two captures.

```python
L = o.merge(c, on="order_id", how="outer", indicator=True, validate="1:1")
```
*(74 caracteres · ~33 s)*

> 🗣️⌨️ Last lines of cell three: the dollars in failed attempts, and how many rows came from each side.

```python
print(p.amount.sum() - c.amount.sum())
L._merge.value_counts()
```
*(62 caracteres · ~28 s)*

> 🖱️ I'm clicking the Run button on the left of cell three.

> 🖱️ I'm pointing at the first number under cell three: 12,501 dollars.

> 🟢 That's 104 failed attempts. If I had summed every payment, revenue would be overstated by 12,501 dollars.

> 🟢 And the validate check passed: no order has two captures, so the join can't duplicate money.

> 🖱️ I'm pointing at both: 1,134 orders with exactly one capture.

> 🖱️ I'm pointing at left only: 16 orders with no captured payment.

> 🟢 Ten of them only had failed attempts, and six never had any attempt. That's billed revenue that was never collected.

> 🖱️ I'm pointing at right only: 5 captures whose order ID doesn't exist in the orders file.

> 🟢 That's cash I received with no order behind it. I keep it in the ledger and flag it; I don't drop it.

> 🟢 With an inner join, those 16 orders and 5 captures would silently disappear, and the totals would still look clean. That's exactly what an audit has to avoid.

**WHY:** el `outer` es la decisión clave: un `inner` escondería justo las dos diferencias que hay que explicar (pedidos sin cobro y cobros sin pedido). `validate="1:1"` prueba que no hay doble cobro.

**EXPECTED RESULT:**

- `12501.0`
- `both 1134`, `left_only 16`, `right_only 5`

**VERIFY BEFORE CONTINUING:** no hay `MergeError`. 1.134 + 16 + 5 = 1.155 filas en el ledger.

📘 **What each line does** (para vos, no se lee):

- `c = p[p.status.eq("captured")].merge(t, on="method")`: captured payments with their fee terms.
- `L = o.merge(c, on="order_id", how="outer", indicator=True, validate="1:1")`: the ledger; every order and every capture, one row per order, with a `_merge` column saying where each row came from.
- `print(p.amount.sum() - c.amount.sum())`: dollars in failed attempts.
- `L._merge.value_counts()`: rows matched on both sides, orders only, captures only.

---

### Bloque 4. Conciliación con las liquidaciones del procesador

**TIME:** 12:22–15:22 (3:00)

**WHAT I DO:** + Code → tipear 2 tramos → Run → señalar el conteo de ceros y los seis faltantes.

**WHERE:** **+ Code** arriba a la izquierda; la celda 4 aparece debajo de la salida de la celda 3.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell four below cell three.

> 🟢 Cell four goes from gross to net: what the processor should have paid me, against what it actually paid.

> 🗣️⌨️ First line of cell four: the fee for each capture, the amount times the percentage plus the fixed fee, rounded to cents.

```python
L["fee"] = (L.amount * L.fee_pct + L.fee_fixed).round(2)
```
*(56 caracteres · ~25 s)*

> 🗣️⌨️ Next lines of cell four: the gap is the expected net minus what was settled. Zero means the payout is exactly right. Then I count the gaps.

```python
L["gap"] = (L.amount - L.fee - L.settled).round(2)
L.gap.value_counts()
```
*(71 caracteres · ~32 s)*

> 🖱️ I'm clicking the Run button on the left of cell four.

> 🖱️ I'm pointing at the first row under cell four: a gap of zero for 1,107 captures.

> 🟢 So my fee formula reproduces the processor's payouts to the cent. That proves I'm applying the terms correctly.

> 🟢 The rounding matters here. The processor charges whole cents, so without rounding the fee, almost every gap would be a fraction of a cent, and I couldn't tell real differences from noise.

> 🖱️ I'm pointing at the six rows below: gaps from 7.80 to 30 dollars.

> 🟢 Six payouts came in short, 108.70 dollars in total. They aren't fees, because the fees already match. They're processor adjustments I can't explain from the data, so they go to the exceptions.

> 🟢 Captures with no payout yet have no gap at all: they aren't settled. I'll handle them in cell seven.

**WHY:** si los ceros no fueran mayoría, la fórmula de comisión estaría mal y todas las diferencias serían falsas. Primero se prueba la fórmula; después se buscan las excepciones.

**EXPECTED RESULT:** `0.0 1107`, y seis filas con `1` cada una: `7.8`, `12.5`, `15.0`, `18.4`, `25.0`, `30.0` (en cualquier orden).

**VERIFY BEFORE CONTINUING:** 1.107 ceros. Si aparecen cientos de valores chicos distintos, revisá que diga `L.fee_pct` y `L.fee_fixed`.

📘 **What each line does** (para vos, no se lee):

- `L["fee"] = (L.amount * L.fee_pct + L.fee_fixed).round(2)`: expected processor fee per capture.
- `L["gap"] = (L.amount - L.fee - L.settled).round(2)`: expected net minus settled net; empty when not settled.
- `L.gap.value_counts()`: how many captures have each gap.

---

### Bloque 5. Conciliación de reembolsos

**TIME:** 15:22–18:01 (2:38)

**WHAT I DO:** + Code → tipear 2 tramos → Run → señalar el número.

**WHERE:** **+ Code** arriba a la izquierda; la celda 5 aparece debajo de la salida de la celda 4.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell five below cell four.

> 🟢 Cell five brings in refunds. A payment can have more than one refund, partial or full, so I add them up per payment first.

> 🗣️⌨️ First line of cell five: total refunded per payment ID, mapped onto the ledger. Map can't add rows, so the ledger stays one row per transaction. No refund means zero.

```python
L["refund"] = L.payment_id.map(r.groupby("payment_id").amount.sum()).fillna(0)
```
*(78 caracteres · ~35 s)*

> 🗣️⌨️ Last line of cell five: refunds in the file minus refunds that found a captured payment.

```python
r.amount.sum() - L.refund.sum()
```
*(31 caracteres · ~14 s)*

> 🖱️ I'm clicking the Run button on the left of cell five.

> 🖱️ I'm pointing at the result under cell five: 488 dollars.

> 🟢 488 dollars of refunds don't match any captured payment. Two point to failed attempts, so money went back on a charge that never happened. Two point to payment IDs that don't exist.

> 🟢 I don't force them onto an order. They go to the exceptions as bad references.

> 🟢 Everything else matched: 5,020.65 dollars of refunds, partial and full, now sit on the payment they belong to.

> 🟢 One assumption: the processor keeps its fee when a payment is refunded, so the fee stays as a cost even on a full refund.

**WHY:** los reembolsos se suman por pago antes de unir: si se unieran fila por fila, un pago con dos reembolsos duplicaría la fila del ledger.

**EXPECTED RESULT:** `488.0`

**VERIFY BEFORE CONTINUING:** el resultado es exactamente `488.0`.

📘 **What each line does** (para vos, no se lee):

- `L["refund"] = L.payment_id.map(r.groupby("payment_id").amount.sum()).fillna(0)`: total refunded for each captured payment; zero if none.
- `r.amount.sum() - L.refund.sum()`: refund dollars that didn't match a captured payment.

---

### Bloque 6. Costos de productos y margen

**TIME:** 18:01–20:38 (2:38)

**WHAT I DO:** + Code → tipear 2 tramos → Run → señalar los dos productos.

**WHERE:** **+ Code** arriba a la izquierda; la celda 6 aparece debajo de la salida de la celda 5.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell six below cell five.

> 🟢 Cell six adds product costs, so each transaction gets a margin.

> 🗣️⌨️ First line of cell six: cost of goods is the quantity times the unit cost of the product. Again I use map, so no rows are added.

```python
L["cogs"] = L.quantity * L.product_id.map(k.set_index("product_id").unit_cost)
```
*(78 caracteres · ~35 s)*

> 🗣️⌨️ Next lines of cell six: the margin is cash captured minus refunds, minus processor fees, minus cost. Then the products with no cost.

```python
L["margin"] = L.amount - L.refund - L.fee - L.cogs
k[k.unit_cost.isna()]
```
*(72 caracteres · ~32 s)*

> 🖱️ I'm clicking the Run button on the left of cell six.

> 🖱️ I'm pointing at the two rows under cell six: P017, the USB-C Hub, and P022, the Resistance Bands.

> 🟢 Neither has a unit cost, so their margin stays empty. I don't fill it with an average: that would be an invented number. It's a limitation, and it goes to the exceptions.

> 🟢 The margin is on cash, not on billed amounts, because that's the money the business actually kept.

**WHY:** sin costo, el margen se deja vacío (NaN) a propósito: un margen inventado haría que la posición financiera parezca más completa de lo que es.

**EXPECTED RESULT:** dos filas: `P017 USB-C Hub Tech 79.0 NaN` y `P022 Resistance Bands Fitness 24.0 NaN`.

**VERIFY BEFORE CONTINUING:** aparecen solo esas dos filas.

📘 **What each line does** (para vos, no se lee):

- `L["cogs"] = L.quantity * L.product_id.map(k.set_index("product_id").unit_cost)`: cost of goods sold per transaction.
- `L["margin"] = L.amount - L.refund - L.fee - L.cogs`: cash margin; empty if any part is missing.
- `k[k.unit_cost.isna()]`: products with no cost.

---

### Bloque 7. Registro de excepciones

**TIME:** 20:38–26:44 (6:06)

**WHAT I DO:** + Code → tipear 6 tramos → Run → señalar cada tipo de excepción.

**WHERE:** **+ Code** arriba a la izquierda; la celda 7 aparece debajo de la salida de la celda 6.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell seven below cell six.

> 🟢 Cell seven labels every ledger row. Each exception type is one explicit rule, so anyone can audit why a row was flagged.

> 🗣️⌨️ First line of cell seven: a dictionary of rules. An order with no payment, and a payment with no order.

```python
e = {"no_payment": L.payment_id.isna(), "no_order": L.order_total.isna(),
```
*(73 caracteres · ~32 s)*

> 🗣️⌨️ Second line of cell seven, still inside the dictionary: charged a different amount than billed, and refunded more than was charged.

```python
     "amount_diff": L.amount.ne(L.order_total), "over_refund": L.refund.gt(L.amount),
```
*(85 caracteres · ~38 s)*

> 🗣️⌨️ Third line, closing the dictionary: a short payout, a capture not settled yet, and a product with no cost.

```python
     "short_paid": L.gap.gt(0), "pending": L.settled.isna(), "no_cost": L.cogs.isna()}
```
*(86 caracteres · ~38 s)*

> 🗣️⌨️ Next line of cell seven: the issue column. numpy select takes the first rule that is true, in that order; everything else is ok.

```python
L["issue"] = np.select(list(e.values()), list(e), "ok")
```
*(55 caracteres · ~24 s)*

> 🗣️⌨️ Next line: the exception register. First, the flagged ledger rows and the duplicate order rows from cell two.

```python
x = pd.concat([L[L.issue.ne("ok")], dup.assign(issue="duplicate"), 
```
*(67 caracteres · ~30 s)*

> 🗣️⌨️ Same line, continuing: the refunds that don't match a captured payment. Then the count per issue.

*(sigue en la misma línea, sin Enter)*

```python
r[~r.payment_id.isin(c.payment_id)].assign(issue="bad_refund")])
x.issue.value_counts()
```
*(87 caracteres · ~39 s)*

> 🖱️ I'm clicking the Run button on the left of cell seven.

> 🖱️ I'm pointing at the first row under cell seven: no_cost, 90 rows.

> 🟢 90 sales of the two products with no cost. The money is fine; only the margin is missing.

> 🖱️ I'm pointing at duplicate, 30, and pending, 26.

> 🟢 The 26 pending captures are all from December 29 to 31. With one to three days to settle, they simply hadn't been paid out at year end. That's timing, not a loss.

> 🖱️ I'm pointing at no_payment, 16, and amount_diff, 8.

> 🟢 Eight orders were charged a different amount than billed, some more, some less: 865 dollars billed against 883 captured.

> 🖱️ I'm pointing at the last four rows: short_paid 6, no_order 5, bad_refund 4, and over_refund 2.

> 🟢 Over-refund means a payment was refunded twice: 217 dollars went back that shouldn't have. That one needs to be recovered.

> 🟢 That's 187 rows in total, and each one has a rule that explains it.

**WHY:** el orden de las reglas importa: un pedido sin pago también tiene `settled` vacío, y por eso `no_payment` va antes que `pending`. Así, cada fila queda con su causa real. Los duplicados y los reembolsos mal referenciados no están en el ledger, así que se suman aparte.

**EXPECTED RESULT:** `no_cost 90`, `duplicate 30`, `pending 26`, `no_payment 16`, `amount_diff 8`, `short_paid 6`, `no_order 5`, `bad_refund 4`, `over_refund 2`.

**VERIFY BEFORE CONTINUING:** la suma da 187 y no aparece `ok` en la lista.

📘 **What each line does** (para vos, no se lee):

- `e = {"no_payment": L.payment_id.isna(), "no_order": L.order_total.isna(),`: rules for orders without a capture and captures without an order.
- `"amount_diff": L.amount.ne(L.order_total), "over_refund": L.refund.gt(L.amount),`: captured amount different from the order total; refunds above the captured amount.
- `"short_paid": L.gap.gt(0), "pending": L.settled.isna(), "no_cost": L.cogs.isna()}`: short payout; not settled yet; no product cost.
- `L["issue"] = np.select(list(e.values()), list(e), "ok")`: first matching rule per row, or `ok`.
- `x = pd.concat([L[L.issue.ne("ok")], dup.assign(issue="duplicate"), r[~r.payment_id.isin(c.payment_id)].assign(issue="bad_refund")])`: flagged ledger rows, duplicate order rows and unmatched refunds in one register.
- `x.issue.value_counts()`: rows per issue type.

---

### Bloque 8. Entregables y resumen de control

**TIME:** 26:44–31:57 (5:13)

**WHAT I DO:** + Code → tipear 6 tramos → Run → recorrer la tabla fila por fila.

**WHERE:** **+ Code** arriba a la izquierda; la celda 8 aparece debajo de la salida de la celda 7.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell eight below cell seven.

> 🟢 Cell eight builds the financial control summary and exports the three deliverables.

> 🗣️⌨️ First line of cell eight: group the ledger by issue, and pick the eight money columns, from billed to margin.

```python
s = L.groupby("issue")["order_total amount refund fee settled gap cogs margin"
```
*(78 caracteres · ~35 s)*

> 🗣️⌨️ Same line, continuing: add them up. min count one keeps a blank where nothing could be computed, instead of a fake zero.

*(sigue en la misma línea, sin Enter)*

```python
.split()].sum(min_count=1)
```
*(26 caracteres · ~12 s)*

> 🗣️⌨️ Next line of cell eight: a total row at the bottom.

```python
s.loc["total"] = s.sum()
```
*(24 caracteres · ~11 s)*

> 🗣️⌨️ Next line of cell eight: export the ledger with a new file name, so the five inputs stay untouched. No index, because order and payment IDs already identify each row.

```python
L.to_csv("transaction_reconciliation_ledger.csv", index=False)
```
*(62 caracteres · ~28 s)*

> 🗣️⌨️ Next line of cell eight: export the exception register, also with a new name.

```python
x.to_csv("exception_register.csv", index=False)
```
*(47 caracteres · ~21 s)*

> 🗣️⌨️ Last lines of cell eight: export the summary, and show it rounded to cents.

```python
s.to_csv("financial_control_summary.csv")
s.round(2)
```
*(52 caracteres · ~23 s)*

> 🖱️ I'm clicking the Run button on the left of cell eight.

> 🖱️ I'm pointing at the total row at the bottom of cell eight: 114,484 dollars billed and 112,613 captured.

> 🟢 The difference is the revenue bridge: 2,300 dollars never collected, plus 18 dollars of amount differences, plus 411 dollars of captures with no order.

> 🖱️ I'm pointing at the fee and settled columns of the total row: 3,488.53 in fees and 107,100.21 settled.

> 🟢 Captured minus fees minus settled leaves about two thousand dollars: 108.70 short payouts, and the net of the 26 pending captures.

> 🖱️ I'm pointing at the ok row: 100,494 dollars clean, with a margin of 38,930.

> 🟢 That's about a 39 percent cash margin on clean transactions.

> 🖱️ I'm pointing at the pending row: 1,966 dollars captured, and settled is blank.

> 🟢 That's correct: nothing has been paid out for those yet. The money is real, it's just in transit at year end.

> 🖱️ I'm pointing at the short_paid row: the gap column shows the same 108.70 from cell four.

> 🖱️ I'm pointing at the over_refund row: a margin of minus 351 dollars, because of the double refunds.

> 🖱️ I'm pointing at the blanks in the no_cost and no_payment rows.

> 🟢 Blank means unknown, not zero. The total margin of 40,097 dollars leaves out the 90 sales with no cost, and the summary shows it.

**WHY:** agrupar por `issue` hace que cada dólar del resumen se pueda rastrear hasta un tipo de excepción, y de ahí a las filas del ledger. `min_count=1` evita que un margen no calculable aparezca como 0.

**EXPECTED RESULT:** tabla de 9 filas (8 tipos + `total`). Fila `total`: `114484.0 112613.0 5020.65 3488.53 107100.21 108.7 56860.23 40096.93`. Fila `ok`: `100494.0 100494.0 4586.65 3132.45 97361.55 0.0 53844.69 38930.21`.

**VERIFY BEFORE CONTINUING:** la fila `total` coincide con la de arriba, y en `no_cost` las columnas `cogs` y `margin` dicen `NaN`.

📘 **What each line does** (para vos, no se lee):

- `s = L.groupby("issue")[...].sum(min_count=1)`: money columns per issue; blank if no value exists.
- `s.loc["total"] = s.sum()`: total row.
- `L.to_csv("transaction_reconciliation_ledger.csv", index=False)`: transaction-level ledger, 1,155 rows.
- `x.to_csv("exception_register.csv", index=False)`: exception register, 187 rows.
- `s.to_csv("financial_control_summary.csv")`: summary with the issue as first column.
- `s.round(2)`: shows the summary in cents.

---

### Bloque 9. Validación contra las fuentes y revisión de los archivos

**TIME:** 31:57–35:40 (3:43)

**WHAT I DO:** + Code → tipear 2 tramos → Run → señalar los ceros → Files: refrescar y abrir los tres entregables.

**WHERE:** **+ Code** arriba a la izquierda; la celda 9 aparece debajo de la salida de la celda 8. Panel Files a la izquierda: botón de refrescar (flecha circular) arriba del panel.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell nine below cell eight.

> 🟢 Cell nine proves the ledger didn't lose or invent money. I compare its totals with the original sources.

> 🗣️⌨️ First part of cell nine: billed, captured and settled from the total row of the summary.

```python
(s.loc["total", ["order_total", "amount", "settled"]] - 
```
*(56 caracteres · ~25 s)*

> 🗣️⌨️ Same line, continuing: minus the same three totals taken directly from the source tables, as absolute differences in cents.

*(sigue en la misma línea, sin Enter)*

```python
[o.order_total.sum(), c.amount.sum(), p.settled.sum()]).abs().round(2)
```
*(70 caracteres · ~31 s)*

> 🖱️ I'm clicking the Run button on the left of cell nine.

> 🖱️ I'm pointing at the three zeros under cell nine.

> 🟢 Billed, captured and settled all match the sources to the cent. The outer join kept every order and every capture, and the one-to-one check guarantees nothing was counted twice.

> 🟢 Refunds are the one total that doesn't match, by design: the 488 dollars from cell five, which are in the register as bad refunds.

> 🖱️ I'm clicking the refresh button at the top of the Files panel on the left.

> 🖱️ I'm pointing at the three new files: transaction reconciliation ledger, exception register, and financial control summary. The five inputs are still there with their original names.

> 🖱️ I'm double-clicking exception_register.csv in the Files panel, to open it on the right.

> 🖱️ I'm scrolling right inside the file viewer, to the issue column near the end.

> 🖱️ I'm pointing at the first rows: order O80003 is no_cost, captured and settled correctly, but its margin is blank. Order O80040 is no_payment: billed 38 dollars, with no payment at all.

> 🖱️ I'm scrolling down to the last rows of the register: the bad refunds, like RF6056, pointing to payment PAY399120, which doesn't exist.

> 🟢 Every row keeps its original order, payment or refund fields next to the issue, so anyone can trace it back to the source file.

> 🖱️ I'm double-clicking financial_control_summary.csv, to check it saved with the issue labels as the first column.

> 🖱️ I'm closing the file viewers with the X on their tabs, to go back to the notebook.

**WHY:** la validación compara contra las tablas de origen, no contra el ledger: así prueba que la unión no perdió ni duplicó plata. Abrir los archivos muestra que los entregables existen y que los originales siguen intactos.

**EXPECTED RESULT:** `order_total 0.0`, `amount 0.0`, `settled 0.0`. En Files: los cinco CSV originales y los tres nuevos.

**VERIFY BEFORE CONTINUING:** los tres ceros. Si alguno no da cero, revisá en la celda 3 el `how="outer"`.

📘 **What each line does** (para vos, no se lee):

- `(s.loc["total", ["order_total", "amount", "settled"]] - [o.order_total.sum(), c.amount.sum(), p.settled.sum()]).abs().round(2)`: absolute difference between the summary totals and the source totals, in cents.

---

### Bloque 10. Conclusiones

**TIME:** 35:40–37:01 (1:22)

**WHAT I DO:** + Text → tipear 2 tramos → clic afuera → Cmd + S.

**WHERE:** botón **+ Text** arriba a la izquierda de la barra de Colab, al lado de **+ Code**.

**SAY:**

> 🖱️ I'm clicking plus Text at the top left, to add a text cell at the end of the notebook for the conclusions.

> 🗣️⌨️ In the text cell: the title.

```markdown
## Summary
```
*(10 caracteres · ~4 s)*

> 🗣️⌨️ Next line of the text cell: the result, and the AI declaration.

```markdown
- Ledger ties to the sources; inputs generated with AI.
```
*(55 caracteres · ~24 s)*

> 🖱️ I'm clicking on the empty area below the text cell, to show it formatted.

> 🖱️ I'm pressing Command and S to save the notebook; the save message appears at the bottom left.

**EXPECTED RESULT:** la celda de texto con el título y una viñeta, formateada.

---

### Bloque 11. Epilogue

**TIME:** 37:01–38:45 (1:44)

**WHAT I DO:** scroll lento hacia arriba, sin tipear. Recién **después** abrís TaskRecorder para detener la grabación.

**WHERE:** Colab, desde las conclusiones hasta la celda 1.

**SAY:**

> 🖱️ I'm scrolling up slowly through the notebook, from the conclusions back to cell one.

> 🟢 My approach was one ledger, with one row per order or capture, and each phase adding columns: fee, gap, refund, cost and margin.

> 🟢 The key decisions: only captured payments count as revenue, the outer join keeps both kinds of orphans, and blanks stay blank instead of being estimated.

> 🟢 The hardest part was the refunds and the pending payouts. Both looked like missing money, but the pending ones are just timing, and some refunds point to payments that never happened.

> 🟢 The checks: the fee formula reproduces 1,107 payouts to the cent, and the ledger ties to the sources.

> 🟢 One limitation: each ledger row gets only its first issue. In this data no row had two, but with real data I'd keep a list of issues per row.

> 🟢 Open items: 217 dollars of double refunds to recover, 108.70 in short payouts to claim from the processor, 2,300 dollars uncollected, and two product costs to find. With more time, I'd confirm the pending payouts in early January. Thanks for watching!

**WHY:** no repite los pasos: cuenta el enfoque, las decisiones, el desafío, cómo se validó y qué queda abierto.

---

## Si algo sale mal

| Error | Qué decís y hacés |
| ----- | ----------------- |
| Un nombre mal escrito | 🖱️ *"There's a typo in cell N. I'm clicking on that line to fix it, and running the cell again."* |
| `NameError` | 🖱️ *"An earlier cell didn't run. I'm opening the Runtime menu at the top and choosing Run before."* |
| `FileNotFoundError` en la celda 1 | Algún CSV no está en Files o tiene otro nombre (por ejemplo `orders (1).csv`). 🖱️ *"One file name doesn't match. I'm checking the Files panel on the left."* |
| `MergeError` en la celda 3 | La celda 2 no corrió o no se borraron los duplicados. Corré de nuevo la celda 2 y después la 3. |
| La celda 4 no da 1.107 ceros | Revisá `L.amount * L.fee_pct + L.fee_fixed` y el `.round(2)` de las dos líneas. |
| La celda 5 no da `488.0` | Revisá `.fillna(0)` y que agrupe por `"payment_id"`. |
| La celda 7 da otros números | Revisá el orden de las reglas: `no_payment` y `no_order` tienen que ir primero, y `pending` antes que `no_cost`. |
| La celda 9 no da ceros | Revisá en la celda 3 el `how="outer"`, y en la celda 8 el `min_count=1`. |
| Hay que volver a correr todo | Los CSV de entrada nunca se reescriben: alcanza con Runtime → Run all. |

---

## Checklist de archivos y preparación previa

- [ ] Practicá dos veces con cronómetro. [financial_reconstruction.ipynb](financial_reconstruction.ipynb) tiene el código completo para comparar. No lo abras en la grabación.
- [ ] En Colab, creá el notebook **financial_reconstruction** **vacío**: una sola celda de código sin nada. **No ejecutes nada.**
- [ ] En **Files**, subí los cinco CSV de esta carpeta: `orders`, `payments`, `refunds`, `products` y `processor_terms`. Revisá que los nombres no tengan `(1)`.
- [ ] Cerrá el panel Files antes de empezar: se abre en el bloque 0.
- [ ] **Tools → Settings → AI assistance**: ocultá las funciones de IA.
- [ ] **Tools → Settings → Editor**: si está la opción, desactivá las sugerencias automáticas de código.
- [ ] Probá el `~` en Colab antes de grabar (**Option + ñ** y espacio).
- [ ] Zoom (`Cmd + +`). Firefox con la ventana 1 en la descripción de la tarea y la ventana 2 en Colab.

## Checklist de resultados que deben quedar generados

- [ ] Los cinco bloques de `info` y la tabla `t` (celda 1).
- [ ] `30 3235.0 True True` (celda 2).
- [ ] `12501.0` y `1134 / 16 / 5` (celda 3).
- [ ] `0.0 1107` y seis faltantes (celda 4).
- [ ] `488.0` (celda 5).
- [ ] P017 y P022 sin costo (celda 6).
- [ ] 187 excepciones en 9 tipos (celda 7).
- [ ] La tabla resumen con la fila `total` (celda 8).
- [ ] Tres ceros (celda 9).
- [ ] En Files: `transaction_reconciliation_ledger.csv` (1.155 filas), `exception_register.csv` (187 filas) y `financial_control_summary.csv` (9 filas).
- [ ] La celda de conclusiones y el notebook guardado.
- [ ] Después: descargá el `.ipynb` y los tres CSV generados. Armá **Deliverables.zip** con eso y los cinco CSV de entrada sin tocar. Marcá en Studio la opción de archivos generados con IA.

## Checklist de decisiones que debo explicar

- [ ] **Duplicados:** solo filas idénticas en todo; IDs únicos después.
- [ ] **Ingreso = cobro capturado**, no intento ($12,501 fallidos fuera).
- [ ] **`outer` + `validate="1:1"`:** se ven los dos tipos de huérfanos y no hay doble conteo.
- [ ] **Comisiones** según `processor_terms.csv`: la fórmula reproduce 1.107 liquidaciones al centavo.
- [ ] **Reembolsos** sumados por pago antes de unir; $488 sin cobro válido.
- [ ] **Sin costo = margen vacío**, no estimado.
- [ ] **Pendientes = timing** (29 al 31 de diciembre), no pérdida.
- [ ] **Validación** contra las fuentes, no contra el ledger.
- [ ] **Originales intactos:** los tres entregables tienen nombres nuevos.

---

## Conclusión para cerrar la grabación (en inglés)

> Billed revenue was 114,484 dollars, but only 112,613 was captured: 2,300 was never collected, 411 came in with no order, and eight orders were charged a different amount. Failed attempts, 12,501 dollars, were never counted as revenue. The processor fee terms reproduce 1,107 payouts to the cent; six payouts came in 108.70 short, and 26 year-end captures are simply waiting to settle. Refunds were matched by payment: 488 dollars point to no valid payment, and two payments were refunded twice. Every difference is in the exception register, and the ledger ties to the sources.

*(Es la versión larga del epilogue. Si te sobra tiempo, podés decirla en lugar de las 🟢 del bloque 11.)*

---

## Pendientes antes de grabar

| Tema | Qué hacer |
| ---- | --------- |
| **Goal en TaskRecorder** | Confirmá que la descripción de TaskRecorder es la de la idea aprobada (el Goal de arriba). |
| **Origen de los CSV** | Sintéticos, generados con IA. Decí "generated with AI" y marcá en Studio la opción de archivos generados con IA. |
| **Generador** | Los CSV salen de [_generador/generate_data.py](_generador/generate_data.py). No lo subas ni lo muestres en la grabación. |
