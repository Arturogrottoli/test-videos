# oyi436dd — E-commerce Financial Reconstruction

Guion para volver a grabar la tarea **oyi436dd** respetando la idea aprobada. Se graba en **Google Colab** (app principal), con **Firefox** como app de apoyo, en una sola toma.

> **Goal:** *Reconstruct the financial position of a simulated e-commerce business by reconciling customer orders, payment transactions, processor settlements, refunds, and product costs. Deliver an auditable transaction-level ledger that explains revenue differences, settlement discrepancies, and unresolved financial movements.*

**Duración estimada: ~29:27, con 35% de tipeo** (tipeando a 135 car./min). Límite absoluto: 30:00. Si tipeás más lento (120 car./min), da ~30:44 y 38%: practicá hasta tipear cada tramo en el tiempo indicado.

**Punto de partida al grabar:** la **celda 1 ya está escrita** (imports, lectura de los cinco CSV, la función `export()` e `info`) y los cinco CSV ya están subidos en el panel **Files** de Colab. **Todo lo demás se tipea en vivo** (celdas 2 a 9). No hay celda de conclusiones: se dicen en el epílogo. En el video se dice por qué: la celda 1 es preparación, no análisis, y el tiempo ahorrado va a explicar la conciliación.

**Por qué se rechazó la grabación anterior y qué cambia:** la versión anterior deduplicaba identidades de clientes y armaba perfiles de comportamiento: eso no estaba en la idea aprobada. Esta versión hace solamente reconstrucción financiera:

- No se deduplican clientes ni se normalizan teléfonos. `customer_id` se deja tal como viene.
- No hay perfiles, ni segmentación, ni marketing.
- **No se sobrescribe ningún CSV de entrada.** Los tres archivos que se generan tienen nombres nuevos.

---

## Cronograma

| # | Bloque | Fase | Celda | TIME | Duración |
| - | ------ | ---- | ----- | ---- | -------- |
| 0 | Opening | — | — | 0:00–1:23 | 1:23 |
| 1 | Celda 1: carga e inspección de los cinco archivos | 1. Input inspection | 1 | 1:23–3:42 | 2:19 |
| 2 | Validación de datos | 2. Data validation | 2 | 3:42–6:03 | 2:21 |
| 3 | Conciliación de pagos | 3. Payment reconciliation | 3 | 6:03–9:18 | 3:15 |
| 4 | Conciliación con las liquidaciones del procesador | 4. Processor settlement | 4 | 9:18–11:49 | 2:31 |
| 5 | Conciliación de reembolsos | 5. Refund reconciliation | 5 | 11:49–14:00 | 2:10 |
| 6 | Costos de productos y margen | 6. Product cost | 6 | 14:00–16:04 | 2:04 |
| 7 | Registro de excepciones | 7. Exception register | 7 | 16:04–22:11 | 6:07 |
| 8 | Resumen de control y exportación | 7. Deliverables | 8 | 22:11–25:24 | 3:13 |
| 9 | Validación contra las fuentes y revisión de los archivos | 7. Validation | 9 | 25:24–28:13 | 2:49 |
| 10 | Epilogue | — | — | 28:13–29:27 | 1:14 |
| | **Total** | | | | **~29:27** |

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
| Tipeo en vivo (celdas 2 a 9) | 1.392 caracteres | ~10,3 min a 135 car./min (~11,6 a 120) |
| Narración | ~2.011 palabras | ~15,5 min |
| Navegación y ejecución | 11 bloques | ~3,7 min |
| **Total** | | **~29:27** (~30:44 si tipeás a 120 car./min) |

**Tipeo: ~35% del video a 135 car./min** (~38% a 120).

**Qué se hizo para que todo entre tipeado:**

- Nombres cortos: `o` pedidos, `p` pagos, `r` reembolsos, `k` productos, `t` condiciones del procesador, `c` cobros capturados, `L` ledger, `x` excepciones, `s` resumen.
- La celda 1 (imports, lectura de los CSV, la función `export()` e `info`) va escrita antes de grabar: es preparación, no análisis.
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

**TIME:** 0:00–1:23 (1:23)

**WHAT I DO:** hablar con la descripción de la tarea en pantalla → minimizar → abrir Colab desde el Dock → abrir el panel Files.

**WHERE:** Firefox ventana 1 (descripción). Botón amarillo arriba a la izquierda. Ícono de Firefox en el Dock, a la derecha (Mac); segunda ventana de la lista. Ícono de carpeta en la barra lateral izquierda de Colab.

**SAY:**

> 🟢 I will be beginning my task soon. I'm rebuilding the financial position of an online store for the last quarter of 2025, from five sources that don't agree: orders, payments, refunds, product costs, and the processor's fee terms.

> 🟢 The result is three files: a transaction-level ledger, an exception register, and a control summary that ties back to the sources.

> 🖱️ I'm clicking the yellow minimize button at the top left, to hide the task description.

> 🖱️ I'm clicking the Firefox icon in the Dock on the right, and choosing the second window: my Colab notebook.

> 🖱️ I'm clicking the folder icon in Colab's left sidebar, to open the Files panel and show my inputs.

> 🖱️ I'm pointing at the five CSV files in the Files panel. I uploaded them before recording. They're synthetic, generated with AI, and I never overwrite them.

**WHY:** en menos de un minuto y medio el revisor ve el objetivo, los cinco archivos de la idea aprobada y los tres entregables.

**EXPECTED RESULT:** el notebook con la celda 1 escrita (sin ejecutar) y el panel Files abierto con los cinco CSV.

**VERIFY BEFORE CONTINUING:** están los cinco archivos y no hay ningún otro CSV en Files.

---

### Bloque 1. Celda 1: carga e inspección de los cinco archivos

**TIME:** 1:23–3:42 (2:19)

**WHAT I DO:** señalar cada grupo de líneas de la celda 1 (ya escrita) → Run → recorrer la salida con scroll.

**WHERE:** celda 1, la única del notebook, a la derecha del panel Files. Botón Run (triángulo) a la izquierda de la celda.

**Celda 1 (ya escrita antes de grabar, no se tipea):**

```python
import pandas as pd
import numpy as np

o = pd.read_csv("orders.csv")
p = pd.read_csv("payments.csv")
r = pd.read_csv("refunds.csv")
k = pd.read_csv("products.csv")
t = pd.read_csv("processor_terms.csv")

def export():
    L.to_csv("transaction_reconciliation_ledger.csv", index=False)
    x.to_csv("exception_register.csv", index=False)
    s.to_csv("financial_control_summary.csv")

for d in [o, p, r, k, t]:
    d.info()
t
```

**SAY:**

> 🖱️ I'm pointing at cell one, at the top of the notebook. I wrote it before recording because it's only setup: imports, loading the five files, and the export. Everything after it I type live.

> 🖱️ I'm pointing at the five read_csv lines in the middle of cell one: o is orders, p payments, r refunds, k products, and t the processor terms.

> 🖱️ I'm pointing at the export function below them. It saves my three deliverables at the end, all with new names, so the inputs stay untouched.

> 🖱️ I'm clicking the Run button on the left of cell one, to load and describe the five files.

> 🖱️ I'm pointing at the orders block under cell one: 1,180 rows and no missing values.

> 🟢 There's no discount, tax or shipping column: order_total is quantity times price. customer_id stays as it is; this task is about money, not customers.

> 🖱️ I'm scrolling down inside the output of cell one, to the payments block, to check the payout columns.

> 🖱️ I'm pointing at payout_id and settled: 1,113 values out of 1,243. Failed attempts and unsettled captures have none.

> 🖱️ I'm scrolling down to the products block, to check the costs.

> 🖱️ I'm pointing at unit_cost: 23 values out of 25. There's one cost per product and no cost history, so cost of goods uses that cost.

> 🖱️ I'm scrolling down to the terms table at the bottom of cell one, to read the processor's rates.

> 🟢 Card is 2.9 percent plus 30 cents, wallet 3.49 percent plus 49 cents, bank transfer 0.8 percent. Payouts arrive one to three days later.

**WHY:** antes de unir nada hay que ver las claves y los vacíos. Los vacíos en `settled` y `unit_cost` anticipan dos excepciones. Las dos frases sobre descuentos/impuestos/envíos y costos históricos dejan dicho que no existen en los datos, en vez de inventarlos.

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
- `o = pd.read_csv("orders.csv")` … `t = pd.read_csv("processor_terms.csv")`: reads each input into a short name.
- `def export():`: defines the export of the three deliverables; it only runs when cell 8 calls it, so it uses the final `L`, `x` and `s`.
- `L.to_csv(..., index=False)` / `x.to_csv(..., index=False)` / `s.to_csv(...)`: ledger, exception register and summary, with new file names.
- `for d in [o, p, r, k, t]:` + `d.info()`: prints rows, columns, non-null counts and types for each table.
- `t`: shows the processor terms.

---

### Bloque 2. Validación de datos

**TIME:** 3:42–6:03 (2:21)

**WHAT I DO:** + Code → tipear 2 tramos → Run → señalar la salida.

**WHERE:** botón **+ Code** arriba a la izquierda; la celda 2 aparece debajo de la salida de la celda 1.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell two below the output of cell one.

> 🗣️⌨️ Cell two is validation. First two lines: I set aside the exact duplicate rows for the exceptions, and drop them from my working copy. The file itself doesn't change.

```python
dup = o[o.duplicated()]
o = o.drop_duplicates()
```
*(47 caracteres · ~21 s)*

> 🗣️⌨️ Last line of cell two: how many duplicates, their dollars, and whether order IDs and payment IDs are now unique.

```python
print(len(dup), dup.order_total.sum(), o.order_id.is_unique, p.payment_id.is_unique)
```
*(84 caracteres · ~37 s)*

> 🖱️ I'm clicking the Run button on the left of cell two.

> 🖱️ I'm pointing at the output under cell two: 30 rows, 3,235 dollars, and two Trues.

> 🟢 30 orders were exported twice. Without them, every order ID and payment ID is unique, so my joins can't double count.

> 🟢 I only drop rows that are identical in every column. If two rows shared an ID with different data, I'd investigate them instead.

**WHY:** se borran solo filas idénticas en todas las columnas: no hay riesgo de perder un pedido real.

**EXPECTED RESULT:** `30 3235.0 True True`

**VERIFY BEFORE CONTINUING:** los dos `True`. Si `o.order_id.is_unique` diera `False`, la unión de la celda 3 fallaría.

📘 **What each line does** (para vos, no se lee):

- `dup = o[o.duplicated()]`: rows that repeat an earlier row in every column.
- `o = o.drop_duplicates()`: working copy without those rows; `orders.csv` is not touched.
- `print(len(dup), dup.order_total.sum(), o.order_id.is_unique, p.payment_id.is_unique)`: count and dollars of duplicates, and two uniqueness checks.

---

### Bloque 3. Conciliación de pagos

**TIME:** 6:03–9:18 (3:15)

**WHAT I DO:** + Code → tipear 3 tramos → Run → señalar el monto y los tres grupos.

**WHERE:** **+ Code** arriba a la izquierda; la celda 3 aparece debajo de la salida de la celda 2.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell three below cell two.

> 🗣️⌨️ First line of cell three: c keeps only captured payments, because an attempt isn't revenue, and joins the fee terms by payment method.

```python
c = p[p.status.eq("captured")].merge(t, on="method")
```
*(52 caracteres · ~23 s)*

> 🗣️⌨️ Next line of cell three: L is my ledger. The outer join keeps orders with no payment and payments with no order. Validate one-to-one stops the cell if any order was captured twice.

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

> 🖱️ I'm pointing at the first number under cell three: 12,501 dollars of failed attempts, which never count as revenue.

> 🖱️ I'm pointing at both, just below: 1,134 orders matched to exactly one capture.

> 🖱️ I'm pointing at left only: 16 orders with no capture. Billed, but never collected.

> 🟢 Ten of them only had failed attempts, and six never had any attempt at all.

> 🖱️ I'm pointing at right only: 5 captures whose order doesn't exist. Cash with nothing behind it, so I keep it and flag it.

> 🟢 An inner join would hide both groups, and the totals would still look clean.

**WHY:** el `outer` muestra las dos diferencias que hay que explicar; `validate="1:1"` prueba que no hay doble cobro.

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

**TIME:** 9:18–11:49 (2:31)

**WHAT I DO:** + Code → tipear 2 tramos → Run → señalar los ceros y los seis faltantes.

**WHERE:** **+ Code** arriba a la izquierda; la celda 4 aparece debajo de la salida de la celda 3.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell four below cell three.

> 🗣️⌨️ First line of cell four: the expected fee, the amount times the rate plus the fixed fee, rounded to cents like the processor does.

```python
L["fee"] = (L.amount * L.fee_pct + L.fee_fixed).round(2)
```
*(56 caracteres · ~25 s)*

> 🗣️⌨️ Next lines of cell four: the gap, expected net minus what was actually settled, and a count of the gaps.

```python
L["gap"] = (L.amount - L.fee - L.settled).round(2)
L.gap.value_counts()
```
*(71 caracteres · ~32 s)*

> 🖱️ I'm clicking the Run button on the left of cell four.

> 🖱️ I'm pointing at the first row under cell four: a gap of zero for 1,107 captures.

> 🟢 My formula reproduces the processor's payouts to the cent, so the terms are applied correctly.

> 🟢 That's why I round the fee: the processor charges whole cents, and without rounding almost every gap would be a fraction of a cent.

> 🖱️ I'm pointing at the six rows below it: gaps from 7.80 to 30 dollars.

> 🟢 Six payouts came in 108.70 dollars short. The fees already match, so these are unexplained processor adjustments, and they go to the exceptions.

**WHY:** primero se prueba la fórmula de comisión; recién después las diferencias son creíbles.

**EXPECTED RESULT:** `0.0 1107`, y seis filas con `1` cada una: `7.8`, `12.5`, `15.0`, `18.4`, `25.0`, `30.0` (en cualquier orden).

**VERIFY BEFORE CONTINUING:** 1.107 ceros. Si aparecen cientos de valores chicos distintos, revisá que diga `L.fee_pct` y `L.fee_fixed`.

📘 **What each line does** (para vos, no se lee):

- `L["fee"] = (L.amount * L.fee_pct + L.fee_fixed).round(2)`: expected processor fee per capture.
- `L["gap"] = (L.amount - L.fee - L.settled).round(2)`: expected net minus settled net; empty when not settled.
- `L.gap.value_counts()`: how many captures have each gap.

---

### Bloque 5. Conciliación de reembolsos

**TIME:** 11:49–14:00 (2:10)

**WHAT I DO:** + Code → tipear 2 tramos → Run → señalar el número.

**WHERE:** **+ Code** arriba a la izquierda; la celda 5 aparece debajo de la salida de la celda 4.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell five below cell four.

> 🗣️⌨️ First line of cell five: the total refunded per payment, partial and full together, mapped onto the ledger. Map can't add rows, so each refund is subtracted only once.

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

> 🟢 Two refunds point to failed attempts, and two to payment IDs that don't exist. I don't force them onto an order; they're exceptions.

> 🟢 Everything else matched: 5,020.65 dollars of refunds now sit on the payment they belong to. The processor keeps its fee on a refund, so the fee stays as a cost.

**WHY:** los reembolsos se suman por pago antes de unir: si se unieran fila por fila, un pago con dos reembolsos duplicaría la fila del ledger.

**EXPECTED RESULT:** `488.0`

**VERIFY BEFORE CONTINUING:** el resultado es exactamente `488.0`.

📘 **What each line does** (para vos, no se lee):

- `L["refund"] = L.payment_id.map(r.groupby("payment_id").amount.sum()).fillna(0)`: total refunded for each captured payment; zero if none.
- `r.amount.sum() - L.refund.sum()`: refund dollars that didn't match a captured payment.

---

### Bloque 6. Costos de productos y margen

**TIME:** 14:00–16:04 (2:04)

**WHAT I DO:** + Code → tipear 2 tramos → Run (no muestra salida).

**WHERE:** **+ Code** arriba a la izquierda; la celda 6 aparece debajo de la salida de la celda 5.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell six below cell five.

> 🗣️⌨️ First line of cell six: cost of goods, the quantity times the product's unit cost, again with map so no rows are added.

```python
L["cogs"] = L.quantity * L.product_id.map(k.set_index("product_id").unit_cost)
```
*(78 caracteres · ~35 s)*

> 🗣️⌨️ Last line of cell six: the margin, cash captured minus refunds, fees and cost.

```python
L["margin"] = L.amount - L.refund - L.fee - L.cogs
```
*(50 caracteres · ~22 s)*

> 🖱️ I'm clicking the Run button on the left of cell six. There's no output: it only adds two columns, and I check them in cells seven and eight.

> 🟢 Where a product has no cost, the margin stays blank. I don't fill it with an average; that would be an invented number.

**WHY:** sin costo, el margen se deja vacío (NaN) a propósito. Los 90 casos aparecen como `no_cost` en la celda 7 y en blanco en la celda 8.

**EXPECTED RESULT:** la celda corre sin salida y sin error (aparece el tilde verde a la izquierda).

**VERIFY BEFORE CONTINUING:** no hay `KeyError`. Si lo hay, revisá `"product_id"` y `unit_cost`.

📘 **What each line does** (para vos, no se lee):

- `L["cogs"] = L.quantity * L.product_id.map(k.set_index("product_id").unit_cost)`: cost of goods sold per transaction.
- `L["margin"] = L.amount - L.refund - L.fee - L.cogs`: cash margin; empty if any part is missing.

---

### Bloque 7. Registro de excepciones

**TIME:** 16:04–22:11 (6:07)

**WHAT I DO:** + Code → tipear 6 tramos → Run → señalar los tipos de excepción.

**WHERE:** **+ Code** arriba a la izquierda; la celda 7 aparece debajo de la celda 6.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell seven below cell six.

> 🗣️⌨️ Cell seven labels every ledger row. First line: a dictionary of rules, starting with an order with no payment, and a payment with no order.

```python
e = {"no_payment": L.payment_id.isna(), "no_order": L.order_total.isna(),
```
*(73 caracteres · ~32 s)*

> 🗣️⌨️ Second line of cell seven, inside the dictionary: charged a different amount than billed, and refunded more than captured.

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

> 🗣️⌨️ Next line: the exception register. The flagged ledger rows, plus the duplicate rows from cell two.

```python
x = pd.concat([L[L.issue.ne("ok")], dup.assign(issue="duplicate"), 
```
*(67 caracteres · ~30 s)*

> 🗣️⌨️ Same line, continuing: plus the refunds with no captured payment. Then the count per issue.

*(sigue en la misma línea, sin Enter)*

```python
r[~r.payment_id.isin(c.payment_id)].assign(issue="bad_refund")])
x.issue.value_counts()
```
*(87 caracteres · ~39 s)*

> 🖱️ I'm clicking the Run button on the left of cell seven.

> 🖱️ I'm pointing at the first row under cell seven: no_cost, 90 sales of P017 and P022, the two products with no cost.

> 🖱️ I'm pointing at duplicate, 30, in the second row: the export copies from cell two.

> 🖱️ I'm pointing at pending, 26, in the third row.

> 🟢 They're all from December 29 to 31. With one to three payout days in the terms, they just hadn't settled at year end. That's timing, not a loss.

> 🖱️ I'm pointing at no_payment, 16, the orders never collected from cell three.

> 🖱️ I'm pointing at amount_diff, 8: orders charged a different amount than billed, 865 dollars billed against 883 captured.

> 🖱️ I'm pointing at short_paid 6, no_order 5 and bad_refund 4: the short payouts, orphan captures and bad refunds I found in cells four, three and five.

> 🖱️ I'm pointing at the last row, over_refund, 2: payments refunded twice, 217 dollars to recover.

> 🟢 187 rows in total, each explained by one rule. The order matters: an order with no payment also has no settlement, so no_payment comes before pending.

**WHY:** cada tipo de excepción es una regla explícita y auditable. Los duplicados y los reembolsos mal referenciados no están en el ledger, así que se suman aparte.

**EXPECTED RESULT:** `no_cost 90`, `duplicate 30`, `pending 26`, `no_payment 16`, `amount_diff 8`, `short_paid 6`, `no_order 5`, `bad_refund 4`, `over_refund 2`.

**VERIFY BEFORE CONTINUING:** la suma da 187 y no aparece `ok` en la lista.

📘 **What each line does** (para vos, no se lee):

- `e = {"no_payment": L.payment_id.isna(), "no_order": L.order_total.isna(),`: rules for orders without a capture and captures without an order.
- `"amount_diff": L.amount.ne(L.order_total), "over_refund": L.refund.gt(L.amount),`: captured amount different from the order total; refunds above the captured amount.
- `"short_paid": L.gap.gt(0), "pending": L.settled.isna(), "no_cost": L.cogs.isna()}`: short payout; not settled yet; no product cost.
- `L["issue"] = np.select(list(e.values()), list(e), "ok")`: first matching rule per row, or `ok`.
- `x = pd.concat([...])`: flagged ledger rows, duplicate order rows and unmatched refunds in one register.
- `x.issue.value_counts()`: rows per issue type.

---

### Bloque 8. Resumen de control y exportación

**TIME:** 22:11–25:24 (3:13)

**WHAT I DO:** + Code → tipear 4 tramos → Run → recorrer la tabla.

**WHERE:** **+ Code** arriba a la izquierda; la celda 8 aparece debajo de la salida de la celda 7.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell eight below cell seven.

> 🗣️⌨️ First line of cell eight: group the ledger by issue, and pick the eight money columns, from billed to margin.

```python
s = L.groupby("issue")["order_total amount refund fee settled gap cogs margin"
```
*(78 caracteres · ~35 s)*

> 🗣️⌨️ Same line, continuing: add them up. Min count one leaves a blank where nothing could be computed, instead of a fake zero.

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

> 🗣️⌨️ Last lines of cell eight: export, the function from cell one, writes the three deliverables. Then the summary, rounded to cents.

```python
export()
s.round(2)
```
*(19 caracteres · ~8 s)*

> 🖱️ I'm clicking the Run button on the left of cell eight.

> 🖱️ I'm pointing at the total row at the bottom of cell eight: 114,484 dollars billed and 112,613 captured.

> 🟢 The difference: 2,300 never collected, plus 411 with no order, plus 18 dollars of amount differences.

> 🖱️ I'm pointing at the fee and settled columns of the total row: 3,488.53 in fees, 107,100.21 settled.

> 🟢 What's left between captured and settled is the 108.70 short and the 26 pending payouts.

> 🖱️ I'm pointing at the pending row: 1,966 dollars captured, and settled is blank. Correct: nothing has been paid out for those yet.

> 🖱️ I'm pointing at the over_refund row: a margin of minus 351 dollars, because of the double refunds.

> 🖱️ I'm pointing at the ok row: 100,494 dollars clean, with a margin of 38,930, about 39 percent.

> 🖱️ I'm pointing at the blanks in the no_cost row: unknown, not zero.

**WHY:** agrupar por `issue` hace que cada dólar del resumen se pueda rastrear hasta un tipo de excepción, y de ahí a las filas del ledger.

**EXPECTED RESULT:** tabla de 9 filas (8 tipos + `total`). Fila `total`: `114484.0 112613.0 5020.65 3488.53 107100.21 108.7 56860.23 40096.93`. Fila `ok`: `100494.0 100494.0 4586.65 3132.45 97361.55 0.0 53844.69 38930.21`.

**VERIFY BEFORE CONTINUING:** la fila `total` coincide con la de arriba, y en `no_cost` las columnas `cogs` y `margin` dicen `NaN`.

📘 **What each line does** (para vos, no se lee):

- `s = L.groupby("issue")[...].sum(min_count=1)`: money columns per issue; blank if no value exists.
- `s.loc["total"] = s.sum()`: total row.
- `export()`: runs the function from cell 1: ledger (1,155 rows), exception register (187 rows) and summary (9 rows).
- `s.round(2)`: shows the summary in cents.

---

### Bloque 9. Validación contra las fuentes y revisión de los archivos

**TIME:** 25:24–28:13 (2:49)

**WHAT I DO:** + Code → tipear 2 tramos → Run → señalar los ceros → Files: refrescar → abrir `exception_register.csv` → cerrar el visor.

**WHERE:** **+ Code** arriba a la izquierda; la celda 9 aparece debajo de la salida de la celda 8. Panel Files a la izquierda: botón de refrescar (flecha circular) arriba del panel.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell nine below cell eight.

> 🗣️⌨️ Cell nine checks the ledger against the sources. First part: billed, captured and settled from the total row of the summary.

```python
s.loc["total", ["order_total", "amount", "settled"]] - 
```
*(55 caracteres · ~24 s)*

> 🗣️⌨️ Same line, continuing: minus the same three totals, straight from the original tables.

*(sigue en la misma línea, sin Enter)*

```python
[o.order_total.sum(), c.amount.sum(), p.settled.sum()]
```
*(54 caracteres · ~24 s)*

> 🖱️ I'm clicking the Run button on the left of cell nine.

> 🖱️ I'm pointing at the three zeros under cell nine.

> 🟢 Nothing lost and nothing counted twice. Refunds differ only by the 488 dollars already in the register.

> 🖱️ I'm clicking the refresh button at the top of the Files panel, to see the new files.

> 🖱️ I'm pointing at the three deliverables in the Files panel, next to the five untouched inputs.

> 🖱️ I'm double-clicking exception_register.csv in the Files panel, to open it on the right.

> 🖱️ I'm scrolling right inside the file viewer, to the issue column near the end.

> 🖱️ I'm pointing at the first rows: O80003 is no_cost, settled correctly but with no margin, and O80040 is no_payment.

> 🖱️ I'm scrolling down to the last rows of the viewer, to the bad refunds, like RF6056 pointing to PAY399120, which doesn't exist.

> 🟢 In these bad_refund rows, amount is the refund amount, because there's no valid payment.

> 🖱️ I'm closing the file viewer with the X on its tab, to go back to the notebook.

**WHY:** la validación compara contra las tablas de origen, no contra el ledger: así prueba que la unión no perdió ni duplicó plata. Abrir un entregable muestra que existe y que es legible.

**EXPECTED RESULT:** `order_total 0.0`, `amount 0.0`, `settled 0.0`. En Files: los cinco CSV originales y los tres nuevos.

**VERIFY BEFORE CONTINUING:** los tres ceros. Si el doble clic no abre el visor, no insistas: 🖱️ *"The viewer didn't open, so I'm pointing at the file in the Files panel instead."* y seguí.

📘 **What each line does** (para vos, no se lee):

- `s.loc["total", ["order_total", "amount", "settled"]] - [o.order_total.sum(), c.amount.sum(), p.settled.sum()]`: difference between the summary totals and the source totals.

---

### Bloque 10. Epilogue

**TIME:** 28:13–29:27 (1:14)

**WHAT I DO:** scroll lento hacia arriba, sin tipear. Recién **después** abrís TaskRecorder para detener la grabación.

**WHERE:** Colab, desde la celda 9 hasta la celda 1.

**SAY:**

> 🖱️ I'm scrolling up slowly through the notebook, from cell nine back to cell one, to recap.

> 🟢 My approach was one ledger, one row per order or capture, with each step adding a column: fee, gap, refund, cost and margin.

> 🟢 The key decisions: only captures count as revenue, the outer join keeps both kinds of orphans, and blanks stay blank instead of being estimated.

> 🟢 The hardest part was telling timing from loss: the pending payouts are timing, while the bad refunds and double refunds are real money.

> 🟢 Open items: 217 dollars of double refunds, 108.70 in short payouts, 2,300 uncollected, and two missing product costs. One limitation: each row keeps only its first issue. Thanks for watching!

**WHY:** no repite los pasos: cuenta el enfoque, las decisiones, el desafío y lo que queda abierto. La declaración de IA ya se dijo en el opening.

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
| La celda 9 no da ceros | Si ves un número diminuto como `1e-11` o `-0.0`, es redondeo de decimales: decí *"That's floating-point noise, effectively zero."* Si es un número real, revisá en la celda 3 el `how="outer"`. |
| Hay que volver a correr todo | Los CSV de entrada nunca se reescriben: alcanza con Runtime → Run all. |

---

## Checklist de archivos y preparación previa

- [ ] Practicá dos veces con cronómetro. [financial_reconstruction.ipynb](financial_reconstruction.ipynb) tiene el código completo para comparar. No lo abras en la grabación.
- [ ] En Colab, creá el notebook **financial_reconstruction** con **la celda 1 escrita** (copiala del bloque 1) y nada más. **No ejecutes nada.**
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
- [ ] La celda 6 corre sin salida y sin error.
- [ ] 187 excepciones en 9 tipos (celda 7).
- [ ] La tabla resumen con la fila `total` (celda 8).
- [ ] Tres ceros (celda 9).
- [ ] En Files: `transaction_reconciliation_ledger.csv` (1.155 filas), `exception_register.csv` (187 filas) y `financial_control_summary.csv` (9 filas).
- [ ] El notebook guardado (Cmd + S) después de terminar la grabación.
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

*(Es la versión larga del epilogue. No la uses en la grabación: alargaría el video. Sirve si te preguntan.)*

---

## Pendientes antes de grabar

| Tema | Qué hacer |
| ---- | --------- |
| **Goal en TaskRecorder** | Confirmá que la descripción de TaskRecorder es la de la idea aprobada (el Goal de arriba). |
| **Origen de los CSV** | Sintéticos, generados con IA. Decí "generated with AI" y marcá en Studio la opción de archivos generados con IA. |
