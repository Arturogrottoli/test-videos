# oyi436dd — E-commerce Financial Reconciliation

Guion para grabar la tarea **oyi436dd** alineada con el Goal oficial, con **Python y pandas** en **Google Colab** y **Firefox** como aplicación de apoyo. Se graba en una sola toma.

> **Goal:** *Reconstruct the financial position of a simulated e-commerce business by reconciling customer orders, payment transactions, processor settlements, refunds, and product costs. Deliver an auditable transaction-level ledger that explains revenue differences, settlement discrepancies, and unresolved financial movements.*

**Duración estimada: ~28 minutos** (máximo absoluto: 30).

**Archivos de entrada** (sintéticos, Q4 2025, con problemas reales):

| Archivo | Filas | Qué es | Problemas que tiene |
| ------- | ----- | ------ | ------------------- |
| `orders.csv` | 1.236 | Un pedido por fila: producto, cantidad, total, estado | 36 filas duplicadas por un error de exportación ($4.113 inflados) |
| `payments.csv` | 1.204 | Intentos de cobro: `captured` o `failed` | 79 intentos fallidos ($7.403 que no son caja), 6 pedidos cobrados dos veces, 8 cobros por un monto distinto al del pedido, 5 cobros de pedidos que no existen |
| `settlements.csv` | 1.182 | Líneas de liquidación del procesador: bruto, fee y neto por pago o reembolso | 26 cobros de fin de diciembre todavía no liquidados, 4 cobros sin liquidación, 5 liquidados por menos |
| `refunds.csv` | 87 | Reembolsos, ligados al `payment_id` (no al pedido) | Hay que mapearlos al pedido a través del pago |
| `products.csv` | 25 | Precio y costo unitario | 2 productos sin costo: 91 pedidos sin COGS |

**Cómo cubre cada parte del Goal:**

| Parte del Goal | Dónde se cumple |
| -------------- | --------------- |
| Customer orders | Celda 2: deduplicación y control de unicidad |
| Product costs | Celda 2: merge validado con `products.csv` y COGS por pedido |
| Payment transactions | Celda 3: solo cuenta la plata capturada, se detectan dobles cobros |
| Refunds y processor settlements | Celda 4 (armada): mapeados al pedido vía `payment_id` |
| Auditable transaction-level ledger | Celda 4: una fila por pedido, más cada cobro sin pedido, con los `payment_ids` de origen |
| Revenue differences | Celdas 4 y 5: `cash_diff` (caja neta − revenue neto), clasificada por causa |
| Settlement discrepancies | Celdas 4 y 5: `settle_diff` (neto esperado − neto liquidado), clasificada por causa |
| Financial position | Celda 6 (armada): ventas brutas, reembolsos, revenue neto, COGS, margen, caja, fees y liquidado |
| Validación contra las fuentes | Celdas 4 y 7: el ledger no pierde ni duplica plata, y los dos puentes cierran al centavo |
| Unresolved financial movements | Celda 8 (armada): `unresolved_items.csv` con causa y acción (`timing`, `refund_owed`, `collect`, `unexplained`) |

**Criterios de Slack que cubre:**

- Los archivos de entrada se modifican materialmente: `orders.csv` se reescribe sin duplicados y con costo, y `refunds.csv` y `settlements.csv` se reescriben con `order_id`.
- El impacto está en dólares.
- Cada regla se justifica con la alternativa incorrecta.
- Las explicaciones que no tienen evidencia quedan como `unexplained`: no se inventan.

---

## Cómo leer este guion

Cada fase tiene:

- **TIME:** cuándo empieza, cuándo termina y cuánto dura.
- **ON SCREEN:** qué tenés que hacer en pantalla, en orden.
- **SAY:** lo que decís, en inglés, intercalado con el código:
  - 🖱️ = lo decís **mientras hacés** la acción con el mouse: qué, dónde y por qué.
  - 🗣️⌨️ = lo decís **con las manos fuera del teclado**, y **después** tipeás el bloque de abajo **en silencio**.
  - 🟢 = lo decís con el mouse quieto: la decisión, o qué muestra el resultado.
- **WHY:** el razonamiento, para vos. **Ya está dentro de lo que decís**; no se lee aparte.
- **EXPECTED RESULT:** qué tiene que aparecer.
- 📘 = la explicación de cada línea, en inglés. Es para vos: **no se lee**.

---

## Estrategia de tiempo y tipeo

| | Cantidad | Tiempo |
| - | -------- | ------ |
| Tipeo en vivo (4 celdas + conclusiones) | 1.504 caracteres | ~8,6 min (~10 a 150 car./min) |
| Narración | ~1.880 palabras | ~14,5 min |
| Navegación y ejecución | 8 celdas + Files | ~3 min |
| **Total** | | **~27,5 min** (~29 a 150 car./min) |

**Tipeo: ~31% del video.** Si las guías piden menos, avisame y paso la celda 7 a armada (−205 caracteres, −1,3 min).

**Qué celdas van armadas y por qué:**

| Celda | Estado | Por qué |
| ----- | ------ | ------- |
| 1. Carga y perfil | **Armada** | Es mecánica: leer y contar. |
| 2. Pedidos y costos | Se tipea | Decisiones: qué es un pedido real y cómo unir costos sin multiplicar filas. |
| 3. Pagos | Se tipea | Decisión: qué cuenta como caja. |
| 4. Reembolsos, liquidaciones y ledger | **Armada** | Es el armado mecánico. Las reglas se explican señalando cada línea. |
| 5. Clasificación de diferencias | Se tipea | Es la decisión central: qué causa explica cada diferencia. |
| 6. Posición financiera | **Armada** | Son sumas estándar. |
| 7. Validación contra las fuentes | Se tipea | Es la prueba de que el ledger cierra. |
| 8. Exportación | **Armada** | Es mecánica: guardar archivos. |

**Reglas de tipeo:**

1. **Nunca hablar y tipear al mismo tiempo.** Frase 🗣️⌨️ con las manos quietas → bloque en silencio.
2. **Ningún tramo de tipeo pasa de 45 segundos.** El más largo tiene 109 caracteres (~37 s; ~44 s a 150 car./min). La línea larga de la celda 3 está partida en dos tramos, **sin Enter** en el medio.
3. **Nada de tipeo extra:** ni comentarios, ni `print` de prueba.
4. **No se usa autocompletado.** Si aparece una caja de sugerencias, Escape.

---

## Pendientes antes de grabar

| Tema | Qué hacer |
| ---- | --------- |
| **Descripción de TaskRecorder y Metadata** | No los tengo. Abajo, en "Textos para TaskRecorder y Metadata", hay una propuesta que coincide con este guion. Pegala o pasame los campos reales para ajustarla. |
| **Origen de los CSV** | Los generé yo, Claude, con un script de Python, **no con Gemini**. Decí "generated with AI", que es cierto, y marcá en Studio la opción de archivos generados con IA. Si las guías exigen otra herramienta, avisame. |
| **Límite de tipeo** | El guion da ~33%. Confirmá el límite. |
| **Nombre de la carpeta** | Sigue diciendo `customer-data-reconstruction`. No va en la entrega, pero si querés la renombro. |
| **Versiones anteriores** | La versión de clientes está en `_version_clientes/` y la primera idea en `_idea_anterior/`. No van en la entrega. |

---

## Textos para TaskRecorder y Metadata (propuesta)

**Descripción:**

> Reconstruct the Q4 2025 financial position of a simulated online store in Google Colab with pandas. I deduplicate orders, attach product costs, keep only captured payments, map refunds and processor settlements to orders through payment IDs, and build a transaction-level ledger. Each difference between revenue and cash, and between expected and settled cash, is classified by cause, validated against the source files, and exported with an unresolved-items report.

**Entregables:** `financial_reconciliation.ipynb`, `transaction_ledger.csv`, `unresolved_items.csv`, `financial_position.csv`, los tres CSV reescritos (`orders.csv`, `refunds.csv`, `settlements.csv`), `payments.csv`, `products.csv` y la carpeta `original/` con los cinco CSV sin tocar.

---

## La regla del mouse y del teclado

1. El mouse **solo se mueve con una frase 🖱️**. Mientras tipeás, soltalo.
2. Al terminar una acción, el cursor queda **quieto en el margen derecho**.
3. **Primero la frase, después el movimiento o el tipeo.**
4. **Repetí el número de celda al menos una vez por minuto.** Las frases ya lo hacen.
5. Frases comodín:
   - *"I'm scrolling right inside the table under cell N, to see the last columns."*
   - *"I'm clicking at the end of line N in cell N, to fix a typo."*
   - *"I'm pressing Escape to close the suggestion box, because I type everything by hand."*
   - *"I'm waiting for cell N to finish; the spinner on its left is still running."*

---

## Guion de grabación

### Fase 1. Opening

**TIME:** 0:00–2:00 (2 min)

**ON SCREEN:** Firefox, ventana 1, con la descripción de la tarea. Después: botón amarillo para minimizar → Firefox en el Dock → segunda ventana (Colab) → panel Files → cerrarlo.

**SAY:**

> 🟢 I will be beginning my task soon. The goal is to reconstruct the financial position of an online store for the last quarter of 2025, by reconciling its orders, payments, processor settlements, refunds, and product costs.

> 🟢 The deliverable is a transaction-level ledger, one row per order with its payment IDs, that explains every gap between revenue and cash, and between expected and settled cash. What I can't explain goes to an unresolved report.

> 🟢 My plan: clean orders and costs, keep only captured payments, map refunds and settlements to orders, classify each difference, compute the position, and validate it against the sources.

> 🖱️ I'm clicking the yellow minimize button at the top left of this window, to put the task description away.

> 🖱️ I'm clicking the Firefox icon in the Dock and choosing the second window: my Colab notebook.

> 🖱️ I'm clicking the folder icon in Colab's left sidebar, to open the Files panel and check the inputs.

> 🖱️ I'm pointing at the five CSV files. They're synthetic, generated with AI, and the originals stay on my Desktop, because this notebook rewrites three of these copies.

> 🖱️ I'm clicking the same folder icon to close the panel.

**WHY:** el revisor tiene que saber desde el principio qué significa "bien": cada diferencia explicada o documentada, y totales que cierran contra las fuentes.

**EXPECTED RESULT:** el notebook con las celdas 1, 4, 6 y 8 llenas y las 2, 3, 5 y 7 vacías. En Files, los cinco CSV.

---

### Fase 2. Perfil de las cinco fuentes

**TIME:** 2:00–3:45 (1,75 min)

**ON SCREEN:** Colab, celda 1 (armada). Señalar las líneas, Run, señalar la salida.

**Celda 1 (armada antes de grabar):**

```python
import pandas as pd
import numpy as np
o = pd.read_csv("orders.csv", parse_dates=["order_date"])
p = pd.read_csv("payments.csv", parse_dates=["created_at"])
r = pd.read_csv("refunds.csv", parse_dates=["refund_date"])
s = pd.read_csv("settlements.csv", parse_dates=["payout_date"])
pr = pd.read_csv("products.csv")
for n, d in {"orders": o, "payments": p, "refunds": r, "settlements": s, "products": pr}.items():
    print(n, d.shape, "duplicate rows:", d.duplicated().sum(), "nulls:", d.isna().sum().sum())
print(o.status.value_counts().to_dict(), p.status.value_counts().to_dict(), s.type.value_counts().to_dict())
print("unique orders:", o.order_id.nunique(), "| payments without order:", (~p.order_id.isin(o.order_id)).sum())
```

**SAY:**

> 🟢 Phase one: profiling the five sources.

> 🖱️ I'm pointing at cell one, at the top of the notebook. I prepared it before recording, because loading and counting are routine.

> 🖱️ I'm pointing at the five read_csv lines in cell one, with the dates parsed, because later I compare capture dates against payout dates.

> 🖱️ I'm clicking the Run button on the left of cell one.

> 🖱️ I'm pointing at the five profile lines under cell one.

> 🟢 Orders has 36 duplicate rows, and products has 2 missing values: two products without a cost.

> 🖱️ I'm pointing at the status line under cell one.

> 🟢 79 payments failed, so payments can't be summed as cash. And settlements mix charges and refunds.

> 🖱️ I'm pointing at the last line: 1,200 unique orders, and 5 payments without an order.

> 🟢 Those 5 are cash with no sale behind it. They'll stay in the ledger as their own rows.

**WHY:** cada problema del perfil anticipa una regla: deduplicar, contar solo lo capturado, separar cargos de reembolsos, conservar los cobros huérfanos.

**EXPECTED RESULT:**

- `orders (1236, 7) duplicate rows: 36 nulls: 0`
- `payments (1204, 5) duplicate rows: 0 nulls: 0`
- `refunds (87, 4) duplicate rows: 0 nulls: 0`
- `settlements (1182, 7) duplicate rows: 0 nulls: 0`
- `products (25, 5) duplicate rows: 0 nulls: 2`
- `{'completed': 1088, 'cancelled': 102, 'refunded': 46} {'captured': 1125, 'failed': 79} {'charge': 1095, 'refund': 87}`
- `unique orders: 1200 | payments without order: 5`

📘 **What each line does** (para vos, no se lee):

- `import pandas as pd` / `import numpy as np`: loads pandas and NumPy.
- The five `read_csv` lines: read each file, with the date columns parsed as real dates.
- `for n, d in {...}.items():`: loops over the five tables with their names.
- `print(n, d.shape, ..., d.duplicated().sum(), ..., d.isna().sum().sum())`: rows and columns, fully duplicated rows and missing values.
- `print(o.status.value_counts().to_dict(), ...)`: order statuses, payment statuses and settlement line types.
- `print("unique orders:", ..., (~p.order_id.isin(o.order_id)).sum())`: distinct orders, and payments whose `order_id` doesn't exist in orders.

---

### Fase 3. Pedidos y costo de producto

**TIME:** 3:45–7:30 (3,75 min)

**ON SCREEN:** Colab, celda 2 (vacía). Clic adentro, tipear 4 bloques, Run, señalar la salida.

**SAY:**

> 🖱️ I'm clicking inside cell two, the empty cell below the profile.

> 🟢 Phase two: orders and product costs.

> 🗣️⌨️ On the first lines of cell two, I save the raw order total, to measure the duplicates in dollars, and I drop the exact duplicate rows.

```python
raw = o.order_total.sum()
o = o.drop_duplicates()
```
*(49 caracteres · ~17 s)*

> 🗣️⌨️ Next line of cell two: I attach the unit cost. Validate m to 1 raises an error if a product appeared twice in products, which would multiply orders and inflate costs. And how left keeps orders without a cost, instead of dropping their revenue.

```python
o = o.merge(pr[["product_id", "unit_cost"]], on="product_id", how="left", validate="m:1")
```
*(89 caracteres · ~31 s)*

> 🗣️⌨️ Next line: the cost of goods sold of each order, quantity times unit cost.

```python
o["cogs"] = o.quantity * o.unit_cost
```
*(36 caracteres · ~12 s)*

> 🗣️⌨️ Last line of cell two: whether each order ID is now unique, the inflated dollars, and the orders without a cost.

```python
print(o.order_id.is_unique, round(raw - o.order_total.sum(), 2), o.cogs.isna().sum())
```
*(85 caracteres · ~29 s)*

> 🖱️ I'm clicking the Run button on the left of cell two.

> 🖱️ I'm pointing at the printed line under cell two: True, 4,113, and 91.

> 🟢 Each order is unique now, and the duplicates would have inflated gross sales by 4,113 dollars. 91 orders have no product cost. I don't invent a cost for them: I'll report their revenue separately, outside the margin.

**WHY:** `validate="m:1"` convierte el supuesto "un costo por producto" en un control. `how="left"` evita perder revenue de los pedidos sin costo, que se aíslan en vez de imputarse.

**EXPECTED RESULT:** `True 4113.0 91`

📘 **What each line does** (para vos, no se lee):

- `raw = o.order_total.sum()`: the total before cleaning, to measure the impact.
- `o = o.drop_duplicates()`: removes rows identical in every column.
- `o = o.merge(..., how="left", validate="m:1")`: adds `unit_cost` to each order; keeps orders without a match; fails if `product_id` repeats in products.
- `o["cogs"] = o.quantity * o.unit_cost`: cost of goods sold per order (`NaN` if the cost is missing).
- `print(...)`: unique order IDs, dollars removed, and orders without a cost.

---

### Fase 4. Pagos: qué cuenta como caja

**TIME:** 7:30–10:45 (3,25 min)

**ON SCREEN:** Colab, celda 3 (vacía). Clic adentro, tipear 4 bloques, Run, señalar la salida.

**SAY:**

> 🖱️ I'm clicking inside cell three, below the cost check.

> 🟢 Phase three: payments. Only captured payments are money; a failed attempt never reached the bank.

> 🗣️⌨️ On the first line of cell three: only the captured payments.

```python
cap = p[p.status == "captured"]
```
*(31 caracteres · ~11 s)*

> 🗣️⌨️ Next line of cell three, first half: per order, the captured amount and the number of captures.

```python
paid = cap.groupby("order_id").agg(captured=("amount", "sum"), n_cap=("amount", "size"), 
```
*(89 caracteres · ~31 s)*

> 🗣️⌨️ Same line, second half: the last capture time, and the payment IDs, so every row of the ledger traces back to its payments.

```python
last_cap=("created_at", "max"), payment_ids=("payment_id", ",".join))
```
*(69 caracteres · ~24 s)*

> 🗣️⌨️ Last line of cell three: the dollars in failed attempts, and the orders captured more than once.

```python
print(round(p.amount.sum() - cap.amount.sum(), 2), (paid.n_cap > 1).sum())
```
*(74 caracteres · ~25 s)*

> 🖱️ I'm clicking the Run button on the left of cell three.

> 🖱️ I'm pointing at the printed line under cell three: 7,403 and 6.

> 🟢 Summing every payment row would have overstated cash by 7,403 dollars. And 6 orders were captured twice: real money taken from customers that I'll check against revenue next.

**WHY:** la caja es solo lo capturado. Agregar por pedido antes de unir evita que un pedido con dos pagos duplique filas, y `payment_ids` deja la traza de auditoría.

**EXPECTED RESULT:** `7403.0 6`

📘 **What each line does** (para vos, no se lee):

- `cap = p[p.status == "captured"]`: keeps only successful payments.
- `paid = cap.groupby("order_id").agg(...)`: one row per order with the captured total, the number of captures, the last capture time and the comma-joined payment IDs. Se tipea en una sola línea, en dos tramos (no apretes Enter en el medio).
- `print(...)`: dollars in failed attempts, and orders with more than one capture.

---

### Fase 5. Reembolsos, liquidaciones y el ledger

**TIME:** 10:45–13:00 (2,25 min)

**ON SCREEN:** Colab, celda 4 (armada). Señalar las líneas, Run, señalar la salida.

**Celda 4 (armada antes de grabar):**

```python
pm = p.set_index("payment_id").order_id
r["order_id"] = r.payment_id.map(pm)
s["order_id"] = s.payment_id.map(pm)
refd = r.groupby("order_id").amount.sum().rename("refunded")
stl = s.groupby("order_id").agg(fee=("fee", "sum"), settled=("net", "sum"))
charge = s[s.type == "charge"]
lag = (charge.payout_date - charge.payment_id.map(p.set_index("payment_id").created_at).dt.normalize()).dt.days
L = o.set_index("order_id")[["status", "order_date", "order_total", "cogs"]].join([paid, refd, stl], how="outer")
L = L.fillna({"order_total": 0, "captured": 0, "n_cap": 0, "refunded": 0, "fee": 0})
L["net_revenue"] = np.where(L.status == "cancelled", 0, L.order_total - L.refunded)
L["cash_diff"] = (L.captured - L.refunded - L.net_revenue).round(2)
L["settle_diff"] = (L.captured - L.refunded - L.fee - L.settled.fillna(0)).round(2)
print("unmatched refunds:", r.order_id.isna().sum(), "| unmatched settlements:", s.order_id.isna().sum())
print("payout lag (days):", lag.value_counts().to_dict(), "| last payout:", s.payout_date.max().date())
print("ledger rows:", len(L), L.index.is_unique, "| lost cash:", round(L.captured.sum() - cap.amount.sum(), 2), "| lost sales:", round(L.order_total.sum() - o.order_total.sum(), 2))
print("cash_diff rows:", (L.cash_diff != 0).sum(), "| settle_diff rows:", (L.settle_diff != 0).sum())
```

**SAY:**

> 🟢 Phase four: refunds, settlements, and the ledger itself.

> 🖱️ I'm pointing at the first three lines of cell four, prepared before recording. Refunds and settlements only carry a payment ID, so I map them to their order through the payments table.

> 🖱️ I'm pointing at the two groupby lines: refunds, fees, and net settled, aggregated per order before joining, so no order repeats.

> 🖱️ I'm pointing at the join line in cell four: an outer join, so a payment without an order keeps its own row.

> 🖱️ I'm pointing at net_revenue: zero for cancelled orders, and the order total minus refunds otherwise.

> 🖱️ I'm pointing at the two difference columns. cash_diff is cash kept minus revenue earned; settle_diff is expected cash after refunds and fees, minus what was paid out. In a clean row, both are zero.

> 🖱️ I'm clicking the Run button on the left of cell four.

> 🖱️ I'm pointing at the first line under cell four: zero unmatched refunds and settlements.

> 🟢 Every refund and settlement line found its order, so nothing is lost in the mapping.

> 🖱️ I'm pointing at the payout lag line.

> 🟢 Every charge is paid out exactly two days after capture, and the last payout is December 31st. That's evidence for the timing rule I'll use next.

> 🖱️ I'm pointing at the ledger line: 1,205 unique rows, and zero cash or sales lost against the source tables.

> 🖱️ I'm pointing at the last line: 35 rows with a cash difference, and 35 with a settlement difference.

**WHY:** el ledger es una fila por transacción de venta con sus IDs de pago, más los cobros sin pedido. El lag fijo de dos días es la evidencia que justifica "en tránsito" sin suponerlo.

**EXPECTED RESULT:**

- `unmatched refunds: 0 | unmatched settlements: 0`
- `payout lag (days): {2: 1095} | last payout: 2025-12-31`
- `ledger rows: 1205 True | lost cash: 0.0 | lost sales: 0.0`
- `cash_diff rows: 35 | settle_diff rows: 35`

📘 **What each line does** (para vos, no se lee):

- `pm = p.set_index("payment_id").order_id`: a lookup from payment to order.
- `r["order_id"] = ...` / `s["order_id"] = ...`: the order of each refund and each settlement line.
- `refd = ...`: refunded dollars per order.
- `stl = ...`: processor fees and net settled cash per order (refund lines are negative).
- `charge` / `lag`: days between capture and payout for every charge line.
- `L = o.set_index(...).join([...], how="outer")`: the ledger, one row per order ID from any source.
- `L = L.fillna({...})`: no payment or refund means 0. `settled` stays `NaN` on purpose: "never settled" is not the same as "settled 0".
- `L["net_revenue"] = ...`: revenue after refunds; 0 for cancelled orders.
- `L["cash_diff"] = ...`: captured − refunded − net revenue.
- `L["settle_diff"] = ...`: captured − refunded − fees − settled net.
- The four `print` lines: mapping check, payout lag, ledger size with cash and sales lost against the sources (must be 0), and rows with differences.

---

### Fase 6. Clasificar cada diferencia

**TIME:** 13:00–19:00 (6 min)

**ON SCREEN:** Colab, celda 5 (vacía). Clic adentro, tipear 8 bloques, Run, señalar la tabla.

**SAY:**

> 🖱️ I'm clicking inside cell five, below the ledger check.

> 🟢 Phase five: explaining the differences. Each row gets the first rule it matches, most specific first.

> 🗣️⌨️ On the first lines of cell five: an empty dictionary of rules; payments with no order; and orders captured more than once.

```python
k = {}
k["unknown_order"] = L.status.isna()
k["double_charge"] = L.n_cap > 1
```
*(76 caracteres · ~26 s)*

> 🗣️⌨️ Next line of cell five: orders with revenue but no captured cash.

```python
k["unpaid"] = L.captured.eq(0) & L.cash_diff.ne(0)
```
*(50 caracteres · ~17 s)*

> 🗣️⌨️ Next: cancelled orders where the customer's money was kept.

```python
k["cancel_no_refund"] = L.status.eq("cancelled") & L.cash_diff.ne(0)
```
*(68 caracteres · ~23 s)*

> 🗣️⌨️ Any other cash difference is an amount mismatch: the data doesn't say why, so I don't guess.

```python
k["amount_mismatch"] = L.cash_diff.ne(0)
```
*(40 caracteres · ~14 s)*

> 🗣️⌨️ Now the settlement side, in cell five. Never settled and captured on December 30th or later: with a two-day lag, its payout falls after year end.

```python
k["in_transit"] = L.settled.isna() & L.last_cap.ge("2025-12-30")
```
*(64 caracteres · ~22 s)*

> 🗣️⌨️ Captured earlier but never settled, and settled for a different amount.

```python
k["no_settlement"] = L.settled.isna() & L.captured.gt(0)
k["short_settlement"] = L.settle_diff.ne(0)
```
*(100 caracteres · ~34 s)*

> 🗣️⌨️ Next line of cell five: np.select applies the rules in order; anything left is reconciled.

```python
L["recon"] = np.select(list(k.values()), list(k), "reconciled")
```
*(63 caracteres · ~22 s)*

> 🗣️⌨️ Last line of cell five: per category, the number of rows and the dollars of each difference.

```python
L.groupby("recon")[["cash_diff", "settle_diff"]].agg(["count", "sum"])
```
*(70 caracteres · ~24 s)*

> 🖱️ I'm clicking the Run button on the left of cell five. A table appears below it.

> 🖱️ I'm pointing at the reconciled row of the table under cell five.

> 🟢 1,135 rows are reconciled, and both differences there sum to exactly zero. Every other dollar has a named cause.

> 🖱️ I'm moving the mouse down the cash_diff sums.

> 🟢 Revenue side: 1,402 dollars from double charges and cancelled orders are owed back, 693 are unpaid, and the unknown orders and mismatches stay unexplained.

> 🖱️ I'm moving the mouse down the settle_diff sums.

> 🟢 Settlement side: 2,225 dollars are in transit, a timing difference; 696 never settled or settled short, and need a processor claim.

**WHY:** el orden de las reglas importa: lo más específico primero. Que la fila `reconciled` sume cero en las dos columnas prueba que no queda ninguna diferencia sin causa. "In transit" se apoya en el lag de 2 días medido en la celda 4.

**EXPECTED RESULT:**

| recon | cash count | cash sum | settle sum |
| ----- | ---------- | -------- | ---------- |
| amount_mismatch | 8 | -8.13 | 0.0 |
| cancel_no_refund | 7 | 730.00 | 0.0 |
| double_charge | 6 | 672.00 | 0.0 |
| in_transit | 26 | 0.00 | 2225.0 |
| no_settlement | 4 | 0.00 | 614.0 |
| reconciled | 1135 | 0.00 | 0.0 |
| short_settlement | 5 | 0.00 | 82.0 |
| unknown_order | 5 | 429.00 | 0.0 |
| unpaid | 9 | -693.00 | 0.0 |

📘 **What each line does** (para vos, no se lee):

- `k = {}`: an ordered dictionary of rules; `np.select` uses the first one that matches.
- `k["unknown_order"] = L.status.isna()`: rows with a payment but no order.
- `k["double_charge"] = L.n_cap > 1`: orders captured more than once.
- `k["unpaid"] = ...`: no captured cash, but revenue (a cash difference).
- `k["cancel_no_refund"] = ...`: cancelled, but cash kept.
- `k["amount_mismatch"] = L.cash_diff.ne(0)`: any remaining cash difference.
- `k["in_transit"] = ...`: never settled, captured on or after Dec 30 (T+2 lands after Dec 31).
- `k["no_settlement"] = ...`: captured before that, never settled.
- `k["short_settlement"] = ...`: settled, but not for the expected amount.
- `L["recon"] = np.select(...)`: the category of each row; `"reconciled"` if no rule matches.
- `L.groupby("recon")[...].agg(["count", "sum"])`: rows and dollars per category.

---

### Fase 7. Posición financiera

**TIME:** 19:00–20:45 (1,75 min)

**ON SCREEN:** Colab, celda 6 (armada). Señalar las líneas, Run, señalar la salida.

**Celda 6 (armada antes de grabar):**

```python
done = L.status.eq("completed")
fp = pd.Series({"gross_sales": L.order_total[L.status.ne("cancelled")].sum(),
                "refunds_on_sales": L.refunded[L.status.ne("cancelled")].sum(),
                "net_revenue": L.net_revenue.sum(),
                "revenue_without_cost": L.net_revenue[done & L.cogs.isna()].sum(),
                "cogs": L.cogs[done].sum(),
                "cash_captured": L.captured.sum(),
                "all_refunds": L.refunded.sum(),
                "processor_fees": L.fee.sum(),
                "settled_cash": L.settled.sum(),
                "unsettled_difference": L.settle_diff.sum()})
fp["gross_margin"] = fp.net_revenue - fp.revenue_without_cost - fp.cogs
fp.round(2)
```

**SAY:**

> 🟢 Phase six: the financial position, with revenue, cost, and cash kept apart.

> 🖱️ I'm pointing at the first lines of cell six: gross sales, refunds on those sales, and net revenue.

> 🖱️ I'm pointing at the cost lines: costs count only for completed orders, since fully refunded ones are treated as returned. Revenue without a known cost stays out of the margin instead of getting a zero cost.

> 🖱️ I'm pointing at the cash lines: captured, refunded, fees, and settled.

> 🖱️ I'm clicking the Run button on the left of cell six.

> 🖱️ I'm pointing at net_revenue and gross_margin under cell six.

> 🟢 Net revenue is 95,436 dollars, and the margin is 40,814 on the revenue with a known cost. 6,747 dollars of revenue have no cost, so the real margin is still open.

> 🖱️ I'm pointing at cash_captured and settled_cash.

> 🟢 The store captured 102,781 dollars but the processor paid out 90,419. The gap is refunds, fees, and the 2,921 dollars from cell five.

**WHY:** revenue (lo ganado), caja capturada (lo cobrado) y caja liquidada (lo depositado) son tres números distintos. Asignar costo cero a los productos sin costo inflaría el margen; por eso se aíslan.

**EXPECTED RESULT:** `gross_sales 100634.00`, `refunds_on_sales 5197.50`, `net_revenue 95436.50`, `revenue_without_cost 6746.75`, `cogs 47875.51`, `cash_captured 102780.87`, `all_refunds 6214.50`, `processor_fees 3226.26`, `settled_cash 90419.11`, `unsettled_difference 2921.00`, `gross_margin 40814.24`.

📘 **What each line does** (para vos, no se lee):

- `done = L.status.eq("completed")`: completed orders.
- `gross_sales` / `refunds_on_sales`: order value and refunds of non-cancelled orders.
- `net_revenue`: revenue after refunds.
- `revenue_without_cost`: net revenue of completed orders whose product has no cost.
- `cogs`: cost of goods of completed orders.
- `cash_captured` / `all_refunds` / `processor_fees` / `settled_cash`: the cash side.
- `unsettled_difference`: expected net cash not paid out.
- `fp["gross_margin"] = ...`: net revenue with a known cost, minus its cost.

---

### Fase 8. Validación contra las fuentes

**TIME:** 20:45–23:30 (2,75 min)

**ON SCREEN:** Colab, celda 7 (vacía). Clic adentro, tipear 2 bloques, Run, señalar la salida.

**SAY:**

> 🖱️ I'm clicking inside cell seven, below the financial position.

> 🟢 Phase seven: proving the ledger against the raw files, not against itself.

> 🗣️⌨️ On the first line of cell seven: the revenue bridge. Source cash minus source refunds minus net revenue, against the sum of the cash differences.

```python
print(round(cap.amount.sum() - r.amount.sum() - fp.net_revenue, 2), round(L.cash_diff.sum(), 2))
```
*(96 caracteres · ~33 s)*

> 🗣️⌨️ Last line: the settlement bridge. Source cash minus refunds, fees, and net payouts, against the sum of the settlement differences.

```python
print(round(cap.amount.sum() - r.amount.sum() - s.fee.sum() - s.net.sum(), 2), round(L.settle_diff.sum(), 2))
```
*(109 caracteres · ~37 s)*

> 🖱️ I'm clicking the Run button on the left of cell seven.

> 🖱️ I'm pointing at the two lines under cell seven: 1,129.87 twice, and 2,921 twice.

> 🟢 Both bridges close to the cent: the total gap computed from the raw files equals the sum of the categories in cell five. So every dollar of difference is explained or explicitly unresolved.

**WHY:** comparar el ledger contra las tablas de origen, y no contra sus propias columnas, es lo que lo hace auditable.

**EXPECTED RESULT:**

- `1129.87 1129.87`
- `2921.0 2921.0`

📘 **What each line does** (para vos, no se lee):

- Line 1: revenue bridge from sources vs. the sum of `cash_diff`.
- Line 2: settlement bridge from sources (`s.net` includes negative refund lines) vs. the sum of `settle_diff`.

---

### Fase 9. Exportación y reporte de pendientes

**TIME:** 23:30–25:15 (1,75 min)

**ON SCREEN:** Colab, celda 8 (armada). Señalar las líneas, Run, abrir Files, señalar los archivos, cerrar Files.

**Celda 8 (armada antes de grabar):**

```python
act = {"in_transit": "timing", "double_charge": "refund_owed", "cancel_no_refund": "refund_owed", "unpaid": "collect"}
L["resolution"] = L.recon.map(act).fillna("unexplained").where(L.recon != "reconciled", "none")
L.reset_index(names="order_id").to_csv("transaction_ledger.csv", index=False)
L[L.recon != "reconciled"].reset_index(names="order_id").to_csv("unresolved_items.csv", index=False)
fp.round(2).rename("amount").to_csv("financial_position.csv")
o.to_csv("orders.csv", index=False)
r.to_csv("refunds.csv", index=False)
s.to_csv("settlements.csv", index=False)
L.groupby("resolution")[["cash_diff", "settle_diff"]].sum()
```

**SAY:**

> 🟢 Phase eight: the exports.

> 🖱️ I'm pointing at the first two lines of cell eight: each category gets an action. Timing, refund owed, collect, or unexplained when the data has no cause.

> 🖱️ I'm pointing at the to_csv lines: the full ledger, the unresolved items, the financial position, and orders, refunds, and settlements rewritten with their costs and order IDs.

> 🖱️ I'm clicking the Run button on the left of cell eight.

> 🟢 Of the 70 open items, only 420 dollars of cash and 696 of settlements are truly unexplained; the rest have a clear action.

> 🖱️ I'm clicking the folder icon in the left sidebar, to open the Files panel.

> 🖱️ I'm pointing at transaction_ledger, unresolved_items, and financial_position, the three new files.

> 🖱️ I'm clicking the folder icon again to close the panel.

**WHY:** "unexplained" es una categoría explícita: no se borra ni se inventa una causa. Reescribir los archivos deja la corrección aplicada en la fuente (criterio de Slack); los originales quedan en el Escritorio y en `original/` del ZIP.

**EXPECTED RESULT:**

| resolution | cash_diff | settle_diff |
| ---------- | --------- | ----------- |
| collect | -693.00 | 0.0 |
| none | 0.00 | 0.0 |
| refund_owed | 1402.00 | 0.0 |
| timing | 0.00 | 2225.0 |
| unexplained | 420.87 | 696.0 |

En Files: `transaction_ledger.csv` (1.205 filas, 17 columnas), `unresolved_items.csv` (70 filas), `financial_position.csv` (11 filas), `orders.csv` (1.200 filas, con `unit_cost` y `cogs`), `refunds.csv` y `settlements.csv` (con `order_id`). Si no aparecen, tocá refresh y decí: *"I'm clicking refresh at the top of the Files panel, to show the new files."*

📘 **What each line does** (para vos, no se lee):

- `act = {...}`: the action for each explained category.
- `L["resolution"] = ...`: the action; `unexplained` for categories without a known cause, `none` for reconciled rows.
- `L.reset_index(names="order_id").to_csv(...)`: the ledger, with the order ID as a column.
- `L[L.recon != "reconciled"]...to_csv(...)`: only the open items.
- `fp...to_csv("financial_position.csv")`: the summary.
- `o / r / s .to_csv(...)`: the three input files rewritten.
- `L.groupby("resolution")[...].sum()`: dollars per action.

---

### Fase 10. Conclusiones

**TIME:** 25:15–27:15 (2 min)

**ON SCREEN:** Colab, + Text abajo de todo, tipear 4 bloques, clic afuera, Cmd + S.

**SAY:**

> 🖱️ I'm clicking plus Text at the top left, to add a text cell at the end of the notebook, for the conclusions.

> 🗣️⌨️ In the text cell: the title and the financial position.

```markdown
## Summary
- Net revenue $95,436.50; margin $40,814.24 ($6,746.75 without cost).
```
*(80 caracteres · ~27 s)*

> 🗣️⌨️ Second line of the text cell: the revenue difference and its causes.

```markdown
- Cash gap $1,129.87: $1,402 owed back, $693 unpaid, $420.87 unexplained.
```
*(73 caracteres · ~25 s)*

> 🗣️⌨️ Third line: the settlement difference.

```markdown
- Settlement gap $2,921: $2,225 in transit, $696 unexplained.
```
*(61 caracteres · ~21 s)*

> 🗣️⌨️ Last line: the AI declaration.

```markdown
- Input files generated with AI.
```
*(32 caracteres · ~11 s)*

> 🖱️ I'm clicking on the empty area below the text cell, to show it formatted.

> 🖱️ I'm pressing Command and S to save the notebook; the save message appears at the bottom left.

**EXPECTED RESULT:** la celda de texto con el título y cuatro viñetas, formateada.

---

### Fase 11. Epilogue

**TIME:** 27:15–28:15 (1 min)

**ON SCREEN:** Colab. Scroll lento hacia arriba. Sin tipear. Recién **después** del epilogue abrís TaskRecorder para detener la grabación.

**SAY:**

> 🖱️ I'm scrolling up slowly through the notebook, from the conclusions back to cell one.

> 🟢 The key decision was keeping revenue, captured cash, and settled cash as three numbers, linked per order through payment IDs, and aggregating before every join.

> 🟢 To verify, I turned assumptions into checks: validate m to 1, zero unmatched refunds and settlements, a measured two-day payout lag before calling anything in transit, and two bridges that close to the cent against the raw files.

> 🟢 The challenges: nothing in the data explains the 8 mismatched captures or the 5 orphan payments, so they're reported, not guessed, and two products have no cost. Next, I'd check them against discount codes and the processor's dispute report. Thanks for watching!

**WHY:** no repite los pasos: cuenta las decisiones, cómo se verificaron y qué queda abierto.

---

## Si algo sale mal

| Error | Qué decís y hacés |
| ----- | ----------------- |
| Un nombre mal escrito | 🖱️ *"There's a typo in cell N. I'm clicking on that line to fix it, and running the cell again."* |
| `MergeError` en la celda 2 | 🖱️ *"The validation caught a repeated product. I'm running cell one again, then cell two."* |
| `NameError` | 🖱️ *"An earlier cell didn't run. I'm opening the Runtime menu at the top and choosing Run before."* |
| La celda 2 se ejecutó dos veces | Aparecen `unit_cost_x` y `unit_cost_y`. Decí: *"I ran cell two twice, so I'm opening the Runtime menu and choosing Run before, to start again from cell one."* |
| Hay que repetir todo después de la celda 8 | 🖱️ *"The inputs were already rewritten, so I'm uploading the originals from my Desktop again in the Files panel."* |

---

## Resumen de tiempos

| Fase | Celda | TIME | Duración |
| ---- | ----- | ---- | -------- |
| 1. Opening | — | 0:00–2:00 | 2 min |
| 2. Perfil | 1 (armada) | 2:00–3:45 | 1,75 min |
| 3. Pedidos y costos | 2 | 3:45–7:30 | 3,75 min |
| 4. Pagos | 3 | 7:30–10:45 | 3,25 min |
| 5. Reembolsos, liquidaciones y ledger | 4 (armada) | 10:45–13:00 | 2,25 min |
| 6. Clasificación | 5 | 13:00–19:00 | 6 min |
| 7. Posición financiera | 6 (armada) | 19:00–20:45 | 1,75 min |
| 8. Validación | 7 | 20:45–23:30 | 2,75 min |
| 9. Exportación | 8 (armada) | 23:30–25:15 | 1,75 min |
| 10. Conclusiones | texto | 25:15–27:15 | 2 min |
| 11. Epilogue | — | 27:15–28:15 | 1 min |
| **Total** | | | **~28 min** |

**Margen:** ~2 minutos hasta 30 (la navegación está calculada con holgura). **Medilo:** hacé una práctica completa con cronómetro. Si pasa de 29 minutos, recortá **palabras** de las 🟢 (nunca las 🖱️ ni las 🗣️⌨️), o pasá la celda 7 a armada.

---

## Checklist

**Antes de grabar**

- [ ] Practicá dos veces con cronómetro. `financial_reconciliation.ipynb` tiene el código completo para comparar.
- [ ] En Colab, creá el notebook **financial_reconciliation** con **8 celdas de código**:
  - celdas **1, 4, 6 y 8**: pegá el código de la fase correspondiente;
  - celdas **2, 3, 5 y 7**: vacías;
  - **no ejecutes nada.**
- [ ] En **Files**, subí los cinco CSV del Escritorio (`orders`, `payments`, `refunds`, `settlements`, `products`). Los del Escritorio son los originales: no los toques.
- [ ] **Tools → Settings → AI assistance**: ocultá las funciones de IA.
- [ ] **Tools → Settings → Editor**: si está la opción, desactivá las sugerencias automáticas de código.
- [ ] Zoom (`Cmd + +`). Firefox con la ventana 1 en la descripción de la tarea y la ventana 2 en Colab.

**Durante**

- [ ] **Nunca hablar y tipear al mismo tiempo.** Ningún tramo de tipeo de más de 45 segundos.
- [ ] **Cada acción con qué + dónde** y, cuando no es obvio, **por qué**.
- [ ] **El número de celda se repite al menos una vez por minuto.**
- [ ] Ejecutá cada celda una vez, en orden.
- [ ] No termines antes de las conclusiones, **Cmd + S** y el epilogue. **TaskRecorder se abre recién después del epilogue.**

**Después**

- [ ] Detené TaskRecorder. Descargá el `.ipynb` y los 8 CSV de Colab.
- [ ] **Run full AutoQC**: revisá el porcentaje de tipeo y que What + Where pase el 70%.
- [ ] Armá **Deliverables.zip** con el `.ipynb`, los 8 CSV y la carpeta `original/` con los cinco CSV del Escritorio.
- [ ] Marcá en Studio la opción de archivos generados con IA.
- [ ] Subí por separado el **MP4**, el **ZIP de TaskRecorder**, **Deliverables.zip** y **Metadata.rtf**.
