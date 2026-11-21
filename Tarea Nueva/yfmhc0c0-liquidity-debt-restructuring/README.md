# yfmhc0c0 — 13-Week Liquidity & Debt Restructuring Analysis

Guion para grabar la tarea **yfmhc0c0** en **Google Colab** (app principal), con **Firefox** como app de apoyo, en una sola toma.

> **Goal:** *Reconstruct and stress-test the 13-week liquidity position of a simulated mid-sized company facing tightening cash availability, customer payment delays, and upcoming debt obligations. (…) Deliver an auditable weekly liquidity model, scenario comparisons, and a justified financing action plan that maintains minimum cash requirements while respecting contractual borrowing limits.*

**Duración estimada: ~24:15** (máximo 25; ~25:20 si tipeás a 120 car./min).

**Punto de partida al grabar:** la **celda 1 ya está escrita** y los cinco CSV ya están cargados en el panel **Files** de Colab. **Todo lo demás se tipea en vivo** (celdas 2 a 6 y la celda de conclusiones).

---

## Cronograma

| # | Bloque | Fase de Dawn | Celda | TIME | Duración |
| - | ------ | ------------ | ----- | ---- | -------- |
| 0 | Opening | — | — | 0:00–1:10 | 1:10 |
| 1 | Carga y contratos | Phase 1 | 1 (ya escrita) | 1:10–3:00 | 1:50 |
| 2 | Caja libre real | Phase 1 | 2 (se tipea) | 3:00–5:00 | 2:00 |
| 3 | Mora reciente por cliente | Phase 2 | 3 (se tipea) | 5:00–8:35 | 3:35 |
| 4 | Proyección de 13 semanas | Phase 3 | 4 (se tipea) | 8:35–13:15 | 4:40 |
| 5 | Capacidad real de endeudamiento | Phase 4 | 5 (se tipea) | 13:15–16:15 | 3:00 |
| 6 | Alternativas, plan y estrés | Phase 4–5 | 6 (se tipea) | 16:15–21:15 | 5:00 |
| 7 | Conclusiones | Phase 5 | texto (se tipea) | 21:15–23:05 | 1:50 |
| 8 | Epilogue | — | — | 23:05–24:15 | 1:10 |
| | **Total** | | | | **~24:15** |

*(Calculado con 130 palabras/min de narración, 135 caracteres/min de tipeo en silencio, todo sumado, más ~20 s de navegación y ejecución por bloque.)*

**Margen:** 0:45 hasta 25:00. Si en el ensayo pasás de 25:00, recortá **palabras de las 🟢** (nunca las 🖱️ ni las 🗣️⌨️).

---

## Verificación de los archivos de entrada

Los cinco CSV los generé yo (Claude) con [_generador/generate_data.py](_generador/generate_data.py) (semilla fija, reproducible). Cada valor contractual del Goal **está en los archivos**:

| Restricción del Goal | Dónde está |
| -------------------- | ---------- |
| Minimum unrestricted cash USD 500,000 | `debt_facilities.csv` → `min_unrestricted_cash` (fila RCF-01) |
| Revolver commitment USD 1,200,000 | `debt_facilities.csv` → `commitment` (fila RCF-01) |
| Max leverage 3.5x | `debt_facilities.csv` → `max_leverage` + `ltm_ebitda` (fila RCF-01) |
| Advance rate, reserves, deuda usada | `advance_rate`, `reserve`, `drawn` (fila RCF-01) |

**Contradicción resuelta:** el apalancamiento necesita EBITDA, que no venía en ninguno de los cinco archivos. Lo agregué como `ltm_ebitda` en la fila del revolver, porque es el EBITDA del último *compliance certificate* del contrato. Así sale del archivo y no se inventa.

**Base de préstamo:** el contrato no fija límite de concentración ni ventana de elegibilidad, así que el AR elegible es **todo el AR abierto no disputado**. No hay en el archivo ningún límite que el código no aplique.

**Archivos** (sintéticos, fecha de corte viernes 2026-11-20, semana 1 = lunes 2026-11-23):

| Archivo | Filas | Columnas clave | Problemas que tiene |
| ------- | ----- | -------------- | ------------------- |
| `bank_transactions.csv` | 163 | `txn_id, date, account_id, account_type, description, reference, amount, status` | 5 filas duplicadas ($202,453 de caja inflada); 3 cheques emitidos sin compensar ($64,150); una cuenta restringida (reserva de deuda, $381,900). El banco suma $1,110,291; la caja libre es $525,938 |
| `accounts_receivable.csv` | 456 | `invoice_id, customer, invoice_date, due_date, amount, status, paid_date` | Historial pagado desde marzo + 69 facturas abiertas. Northwind (46% del AR abierto) paga con 26,5 días de mora en los últimos 90 días; 2 facturas en disputa ($47,767) |
| `accounts_payable.csv` | 46 | `bill_id, vendor, category, bill_date, due_date, amount, critical, max_extension_days` | El 62% es con proveedores críticos (`max_extension_days` = 0); el resto acepta 21 o 28 días |
| `debt_facilities.csv` | 3 | `facility_id, facility_type, commitment, drawn, interest_rate, …, advance_rate, reserve, min_unrestricted_cash, max_leverage, ltm_ebitda` | Revolver (750k usados de 1,2M), term loan (2,4M; cuota de $168,000 en enero) y préstamo de equipos |
| `operating_forecast.csv` | 65 | `week, week_start, category, customer, amount, discretionary` | La gerencia proyecta los cobros de ventas nuevas **en plazo**, sin mora; $179,000 de gasto discrecional (capex y marketing); incluye el servicio de deuda de las tres líneas |

**Cómo cubre cada fase:**

| Fase de Dawn | Celdas | Qué produce para la siguiente |
| ------------ | ------ | ----------------------------- |
| 1. Reconstruct the financial position | 1, 2 | `cash0` = $525,938 de caja libre real |
| 2. Reliability of cash flows | 3 | `d` (mora reciente por cliente) y `ar.exp` (fecha esperada de cobro); el AR reescrito |
| 3. 13-week forecast | 4 | `f` (todos los flujos con su semana), `c()` (caja de cierre) y el caso base: piso de $301,347 en la semana 9 |
| 4. Financing alternatives | 5, 6 | `cap` = $235,000 de capacidad real; postergar y estirar (`levers`) no alcanza |
| 5. Mitigation strategy | 6, texto | giro de $225,000 dentro de la capacidad; `plan` y `stress` sobre el mínimo |

**Criterios de Slack que cubre:**

- `accounts_receivable.csv` se reescribe en Colab con el mismo nombre: conserva todas las columnas originales y suma `late` (días de mora) y `exp` (fecha esperada de cobro). El original queda en el Escritorio.
- Todo el impacto está en dólares.
- Cada alternativa tiene su número y su razón.
- No se leen tablas: se señalan dos o tres valores y se decide.

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
- **WHY:** el criterio financiero, para vos. **Ya está dentro de lo que decís**; no se lee aparte.
- **EXPECTED RESULT:** qué tiene que aparecer.
- **DECISION:** las alternativas y cómo se elige con el resultado.
- 📘 = qué hace cada línea, en inglés. Es para vos: **no se lee**.

---

## Estrategia de tiempo y tipeo

| | Cantidad | Tiempo |
| - | -------- | ------ |
| Tipeo en vivo (celdas 2 a 6 + conclusiones) | 1.189 caracteres | ~8,8 min a 135 car./min (~9,9 a 120) |
| Narración | ~1.620 palabras | ~12,5 min |
| Navegación y ejecución | 9 bloques | ~3 min |
| **Total** | | **~24:15** (~25:20 si tipeás a 120 car./min) |

**Tipeo: ~36% del video a 135 car./min** (~39% a 120). Es lo mínimo con todo tipeado salvo la celda 1: el código ya está reducido a lo indispensable. Para quedar en 35% o menos hay que tipear a ~140 car./min. Practicá los tramos largos.

**Qué se simplificó para que todo entre tipeado:**

- Una sola función de caja (`c`) en lugar de un motor con cinco columnas.
- Todos los flujos (cobros, proveedores, forecast operativo con el servicio de deuda) en una sola tabla `f`, con su semana.
- Las palancas se aplican filtrando o moviendo semanas en esa tabla (`p`, `q`, `s`).
- La fecha de la semana 1 (`W1`) está en la celda 1, que ya está escrita.

**Reglas de tipeo:**

1. **Nunca hablar y tipear al mismo tiempo.** Frase 🗣️⌨️ con las manos quietas → bloque en silencio.
2. **Ningún tramo pasa de 45 segundos.** El más largo tiene 86 caracteres (~38 s a 135 car./min). La línea larga de la celda 4 se tipea en dos tramos, **sin Enter** en el medio.
3. **Nada de tipeo extra:** ni comentarios ni `print` de prueba.
4. **Sin autocompletado.** Si aparece una caja de sugerencias, Escape.
5. **`~` en Mac:** con teclado español, **Option + ñ** y después **espacio**; con teclado US, **Shift + `**. Se usa una vez, en la celda 2.

---

## La regla del mouse y del teclado

1. El mouse **solo se mueve con una frase 🖱️**. Mientras tipeás, soltalo.
2. Al terminar una acción, el cursor queda **quieto en el margen derecho**.
3. **Primero la frase, después el movimiento o el tipeo.**
4. **Repetí el número de celda al menos una vez por minuto.** Las frases ya lo hacen.
5. Frases comodín:
   - *"I'm scrolling down inside the output of cell N, to see the last rows."*
   - *"I'm clicking at the end of line N in cell N, to fix a typo."*
   - *"I'm pressing Escape to close the suggestion box, because I type everything by hand."*
   - *"I'm waiting for cell N to finish; the spinner on its left is still running."*

---

## Guion de grabación

### Bloque 0. Opening

**TIME:** 0:00–1:10 (1:10)

**WHAT I DO:** hablar con la descripción de la tarea en pantalla → minimizar → abrir Colab desde el Dock.

**WHERE:** Firefox ventana 1 (descripción). Botón amarillo arriba a la izquierda. Ícono de Firefox en el Dock, a la derecha (Mac); segunda ventana de la lista.

**SAY:**

> 🟢 I will be beginning my task soon. A mid-sized company is short on cash: its biggest customer pays later and loan payments are due. Over 13 weeks, I'll find a plan that keeps 500,000 of free cash within its loan limits.

> 🟢 I'll reconcile the bank, measure customer delays, build the weekly forecast, measure real borrowing capacity, and stress-test the plan.

> 🖱️ I'm clicking the yellow minimize button at the top left, to hide the task description.

> 🖱️ I'm clicking the Firefox icon in the Dock and choosing the second window: my Colab notebook.

> 🟢 The five input CSVs are already uploaded to the Files panel. They're synthetic, generated with AI; the originals stay on my Desktop.

**WHY:** el revisor tiene que saber desde el minuto uno qué es "éxito": $500,000 libres todas las semanas, sin pasar ningún límite del contrato.

**EXPECTED RESULT:** el notebook con la celda 1 escrita y la celda 2 vacía debajo.

---

### Bloque 1. Phase 1 — Carga y contratos

**TIME:** 1:10–3:00 (1:50)

**WHAT I DO:** señalar cada grupo de líneas de la celda 1 (ya escrita) → Run → señalar la salida.

**WHERE:** celda 1, arriba de todo. Botón Run (triángulo) a la izquierda de la celda.

**Celda 1 (ya escrita antes de grabar):**

```python
import pandas as pd
import numpy as np
b = pd.read_csv("bank_transactions.csv", parse_dates=["date"])
ar = pd.read_csv("accounts_receivable.csv", parse_dates=["invoice_date", "due_date", "paid_date"])
ap = pd.read_csv("accounts_payable.csv", parse_dates=["bill_date", "due_date"])
debt = pd.read_csv("debt_facilities.csv")
op = pd.read_csv("operating_forecast.csv")
W1 = pd.Timestamp("2026-11-23")
for n, d in {"bank": b, "ar": ar, "ap": ap, "debt": debt, "op": op}.items():
    print(n, d.shape, "| duplicate rows:", d.duplicated().sum())
print(b.groupby(["account_type", "status"]).amount.sum().round(0).to_dict())
debt.set_index("facility_id").T
```

**SAY:**

> 🟢 Phase one: reconstructing the real financial position.

> 🖱️ I'm pointing at cell one, which I wrote before recording, because loading files is routine. Everything after it I'll type live.

> 🖱️ I'm pointing at the first read_csv lines in cell one: bank movements and customer invoices. Dates are parsed because every collection depends on a due date.

> 🖱️ I'm pointing at the next three: supplier bills, the debt contracts, and management's weekly forecast.

> 🖱️ I'm pointing at W1: Monday, November 23rd, the first week of the forecast.

> 🖱️ I'm pointing at the loop: for each file, its size and its fully duplicated rows.

> 🖱️ I'm clicking the Run button on the left of cell one.

> 🖱️ I'm pointing at the bank line under cell one: 5 duplicated rows.

> 🟢 That's an export error that inflates cash.

> 🖱️ I'm pointing at the balances: operating cash, 64,150 of pending checks, and 381,900 restricted.

> 🟢 So the bank's total is not my available cash.

> 🖱️ I'm pointing at the RCF-01 column of the debt table, under cell one.

> 🟢 These are my limits: 1.2 million committed, 750,000 drawn, an 80% advance rate, a 150,000 reserve, 500,000 minimum cash, and leverage up to 3.5 times EBITDA of 1.07 million.

**WHY:** las restricciones del Goal tienen que salir del contrato (el archivo), no de supuestos. Mostrarlas al principio deja claro de dónde sale cada límite.

**EXPECTED RESULT:**

- `bank (163, 8) | duplicate rows: 5`; `ar (456, 7)`, `ap (46, 8)`, `debt (3, 15)`, `op (65, 6)`, todas con `duplicate rows: 0`.
- `{('operating', 'cleared'): 792541.0, ('operating', 'pending'): -64150.0, ('restricted', 'cleared'): 381900.0}`
- La tabla del contrato: RCF-01 con `commitment 1200000`, `drawn 750000`, `advance_rate 0.8`, `reserve 150000.0`, `min_unrestricted_cash 500000.0`, `max_leverage 3.5`, `ltm_ebitda 1070000.0`; TL-01 con `drawn 2400000` y `scheduled_payment 168000`; EQ-01 con `drawn 360000`.

📘 **What each line does** (para vos, no se lee):

- `import pandas as pd` / `import numpy as np`: loads pandas and NumPy.
- `b = pd.read_csv("bank_transactions.csv", ...)`: bank movements, with `date` as a real date.
- `ar = pd.read_csv("accounts_receivable.csv", ...)`: customer invoices, with invoice, due and paid dates parsed.
- `ap = pd.read_csv("accounts_payable.csv", ...)`: open supplier bills, with due dates parsed.
- `debt = pd.read_csv("debt_facilities.csv")`: the three facilities and the revolver's terms.
- `op = pd.read_csv("operating_forecast.csv")`: management's weekly operating forecast, including debt service.
- `W1 = pd.Timestamp("2026-11-23")`: Monday of week 1.
- `for n, d in {...}.items():`: loops over the five tables with their names.
- `print(n, d.shape, ..., d.duplicated().sum())`: rows, columns and fully duplicated rows.
- `print(b.groupby(["account_type", "status"]).amount.sum()...)`: raw balance by account type and status.
- `debt.set_index("facility_id").T`: the debt table turned sideways, one column per facility.

---

### Bloque 2. Phase 1 — Caja libre real

**TIME:** 3:00–5:00 (2:00)

**WHAT I DO:** clic en la celda 2 → tipear 2 tramos → Run → señalar el número.

**WHERE:** celda 2, vacía, debajo de la tabla del contrato.

**SAY:**

> 🖱️ I'm clicking inside cell two, the empty cell below the contract table.

> 🗣️⌨️ In cell two, opening cash: I drop repeated transaction IDs and keep only operating accounts. Pending checks stay in, as negatives, because they're already written. The restricted reserve belongs to the lender, so it's out.

```python
cash0 = b[~b.duplicated("txn_id") & b.account_type.eq("operating")].amount.sum()
```
*(80 caracteres · ~36 s)*

> 🗣️⌨️ Last line of cell two: show it rounded.

```python
round(cash0)
```
*(12 caracteres · ~5 s)*

> 🖱️ I'm clicking the Run button on the left of cell two.

> 🖱️ I'm pointing at the number under cell two: 525,938.

> 🟢 That's my real opening cash, not the 1.11 million the bank file adds up to. Duplicates were 202,000 of it, the restricted reserve 381,900, and pending checks take away another 64,150.

> 🟢 So I start only 26,000 above the minimum. Any delay in collections pushes the company below it.

**WHY:** la posición inicial tiene que ser caja **libre y disponible**: sin duplicados, neta de cheques emitidos (ya comprometidos) y sin la reserva restringida, que no se puede usar para pagar operaciones.

**EXPECTED RESULT:** `525938`

**DECISION:** ¿los cheques pendientes cuentan? **Sí, se restan**: ya salieron de los libros y van a compensarse. ¿La reserva restringida cuenta? **No**: el covenant habla de *unrestricted cash*. ¿Borrar o marcar duplicados? Se excluyen en el cálculo sin tocar el archivo del banco.

📘 **What each line does** (para vos, no se lee):

- `cash0 = b[~b.duplicated("txn_id") & b.account_type.eq("operating")].amount.sum()`: sum of operating rows (cleared and pending), skipping the second copy of any transaction ID.
- `round(cash0)`: shows opening cash without cents.

---

### Bloque 3. Phase 2 — Mora reciente por cliente

**TIME:** 5:00–8:35 (3:35)

**WHAT I DO:** + Code → tipear 4 tramos → Run → señalar dos filas de la salida.

**WHERE:** botón **+ Code** arriba a la izquierda de la barra de Colab (agrega la celda 3 debajo de la celda 2).

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell three below cell two.

> 🟢 Phase two: how reliable are these cash flows? Customers don't pay on the due date, so I measure how late each one pays.

> 🗣️⌨️ First line of cell three: days late on every paid invoice, paid date minus due date.

```python
ar["late"] = (ar.paid_date - ar.due_date).dt.days
```
*(50 caracteres · ~22 s)*

> 🗣️⌨️ Next line of cell three: each customer's median delay, only on payments of the last 90 days, because recent behavior is what predicts the next weeks. The median ignores one-off outliers.

```python
d = ar[ar.paid_date > "2026-08-22"].groupby("customer").late.median()
```
*(69 caracteres · ~31 s)*

> 🗣️⌨️ Next line: the expected collection date, the due date plus that customer's delay.

```python
ar["exp"] = ar.due_date + pd.to_timedelta(ar.customer.map(d), "D")
```
*(67 caracteres · ~30 s)*

> 🗣️⌨️ Last lines of cell three: I rewrite the receivables file with the two new columns, keeping every original one, and show the delays.

```python
ar.to_csv("accounts_receivable.csv")
d
```
*(38 caracteres · ~17 s)*

> 🖱️ I'm clicking the Run button on the left of cell three.

> 🖱️ I'm pointing at the last row under cell three: Northwind Retail, 26.5 days late.

> 🟢 Northwind is the biggest customer, 46% of open receivables, and the slowest payer. Its cash arrives almost four weeks after the due date.

> 🖱️ I'm pointing at the other rows: from half a day to 17 days.

> 🟢 So a forecast on due dates would overstate early collections. I'll use these expected dates instead.

> 🟢 Ninety days is about one quarter: long enough for a stable median, short enough to catch Northwind's recent slowdown.

**WHY:** proyectar en la fecha de vencimiento sobreestima los cobros. La ventana de 90 días capta la conducta actual de Northwind, que es la que importa para las próximas 13 semanas.

**EXPECTED RESULT:** la serie `d` con 12 clientes: `Northwind Retail 26.5` (la más alta), `Harbor Cafe Group 17.0`, `Keystone Office 17.0`, `Foxglove Pharmacy 11.0`, y el resto entre `0.5` y `7.5`. En Files, `accounts_receivable.csv` reescrito.

**DECISION:** ¿mora histórica o reciente? **Reciente (90 días)**: es la que va a repetirse en la ventana. ¿Promedio o mediana? **Mediana**: un pago atípico no mueve la fecha esperada.

📘 **What each line does** (para vos, no se lee):

- `ar["late"] = (ar.paid_date - ar.due_date).dt.days`: days between due date and payment; empty for open invoices.
- `d = ar[ar.paid_date > "2026-08-22"].groupby("customer").late.median()`: median days late per customer, payments of the last 90 days before the November 20 cut-off.
- `ar["exp"] = ar.due_date + pd.to_timedelta(ar.customer.map(d), "D")`: expected collection date = due date + the customer's delay.
- `ar.to_csv("accounts_receivable.csv")`: rewrites the input with `late` and `exp` added; original columns unchanged.
- `d`: shows the delays.

---

### Bloque 4. Phase 3 — Proyección de 13 semanas

**TIME:** 8:35–13:15 (4:40)

**WHAT I DO:** + Code → tipear 6 tramos (la línea de `f` en dos tramos, sin Enter) → Run → señalar tres semanas.

**WHERE:** botón **+ Code** arriba a la izquierda (agrega la celda 4 debajo de la salida de la celda 3).

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell four below the delays.

> 🟢 Phase three: the 13-week forecast. I'll put every cash flow in one table, each with its week.

> 🗣️⌨️ First line of cell four: a small function that turns a date into a week number. Anything already overdue lands in week one.

```python
W = lambda s: (s - W1).dt.days.clip(0) // 7 + 1
```
*(46 caracteres · ~20 s)*

> 🗣️⌨️ Next line of cell four: only open invoices, in the week of their expected date. Disputed invoices, 47,767 dollars, stay out: no evidence they'll be paid.

```python
o = ar[ar.status.eq("open")].assign(week=W(ar.exp))
```
*(51 caracteres · ~23 s)*

> 🗣️⌨️ Next line, in two parts: all flows together. Supplier bills go negative, in the week they're due.

```python
f = pd.concat([o, ap.assign(week=W(ap.due_date), amount=-ap.amount),
```
*(69 caracteres · ~31 s · sin Enter al final)*

> 🗣️⌨️ Second part, same line: management's forecast, with the new-sales collections moved by each customer's delay, in whole weeks.

```python
 op.assign(week=op.week + op.customer.map(d).fillna(0) // 7)])
```
*(57 caracteres · ~25 s)*

> 🗣️⌨️ Next line of cell four: closing cash each week is opening cash plus the running total of net flows, for weeks one to thirteen. It's a function so the alternatives reuse it.

```python
c = lambda x: cash0 + x.groupby("week").amount.sum().loc[:13].cumsum()
```
*(70 caracteres · ~31 s)*

> 🗣️⌨️ Last line of cell four: the base case.

```python
c(f)
```
*(4 caracteres · ~2 s)*

> 🖱️ I'm clicking the Run button on the left of cell four.

> 🖱️ I'm pointing at week 1 under cell four: 371,025.

> 🟢 Cash is below the 500,000 minimum in the very first week, because overdue supplier bills fall there.

> 🖱️ I'm moving the mouse down to week 9: 301,347, the trough.

> 🟢 That's the year-end bonus, insurance and the loan payments, while Northwind pays almost four weeks late.

> 🖱️ I'm pointing at weeks 12 and 13: about 500,000.

> 🟢 Cash recovers but never builds a cushion. It's a working-capital gap, not an operating loss: cash comes in, just late.

> 🟢 And it's not one bad week: weeks 6 to 9 all lose cash, so a one-week bridge wouldn't fix it.

**WHY:** separar el déficit **temporal** (timing y pagos únicos) del **estructural** (pérdida operativa) decide el tipo de financiación. Acá el flujo vuelve a ser positivo en las semanas 10 y 12, pero la caja no se aleja del mínimo: hace falta financiación comprometida, no solo recortes.

**EXPECTED RESULT:** la serie `c(f)` con las semanas `1.0` a `13.0`. Valores clave: semana 1 `371024.68`, semana 4 `518442.01`, semana 5 `640994.96`, semana 9 `301347.18` (piso), semana 12 `501082.59`, semana 13 `497982.59`. Debajo del mínimo en las semanas 1–3, 7–11 y 13.

**DECISION:** ¿temporal o estructural? **Capital de trabajo**: hay cobros, pero llegan tarde; $285,800 de cobros de Northwind quedan después de la semana 13. Por eso se combina recortar egresos con un giro comprometido del revolver.

📘 **What each line does** (para vos, no se lee):

- `W = lambda s: (s - W1).dt.days.clip(0) // 7 + 1`: date → week number (1 = week of Nov 23); dates before W1 count as week 1.
- `o = ar[ar.status.eq("open")].assign(week=W(ar.exp))`: open invoices only (disputed are out), with their expected week.
- `f = pd.concat([o, ap.assign(week=W(ap.due_date), amount=-ap.amount), op.assign(...)])`: one table of flows: collections (+), supplier bills (−) by due week, and the operating forecast.
- `op.assign(week=op.week + op.customer.map(d).fillna(0) // 7)`: shifts each new-sales collection by its customer's delay in whole weeks (Northwind: 3); rows without a measured customer don't move.
- `c = lambda x: cash0 + x.groupby("week").amount.sum().loc[:13].cumsum()`: closing cash for weeks 1 to 13 of any set of flows.
- `c(f)`: the base case.

---

### Bloque 5. Phase 4 — Capacidad real de endeudamiento

**TIME:** 13:15–16:15 (3:00)

**WHAT I DO:** + Code → tipear 4 tramos → Run → señalar los dos números.

**WHERE:** botón **+ Code** arriba a la izquierda (agrega la celda 5 debajo de la proyección).

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell five below the forecast.

> 🟢 Phase four: the revolver has 450,000 unused, but how much can I really borrow?

> 🗣️⌨️ First line of cell five: the revolver's row of the contract.

```python
r = debt.iloc[0]
```
*(16 caracteres · ~7 s)*

> 🗣️⌨️ Next line of cell five: the borrowing base. Eighty percent of open, undisputed receivables, minus the reserve, minus what's already drawn.

```python
bb = r.advance_rate * o.amount.sum() - r.reserve - r.drawn
```
*(57 caracteres · ~25 s)*

> 🗣️⌨️ Next line: the real capacity is the tightest of three limits: the unused commitment, the borrowing base, and the leverage room, 3.5 times EBITDA minus all three facilities.

```python
cap = min(r.commitment - r.drawn, bb, r.max_leverage * r.ltm_ebitda - debt.drawn.sum())
```
*(86 caracteres · ~38 s)*

> 🗣️⌨️ Last line of cell five: print the borrowing base and the capacity.

```python
print(bb, cap)
```
*(14 caracteres · ~6 s)*

> 🖱️ I'm clicking the Run button on the left of cell five.

> 🖱️ I'm pointing at the two numbers under cell five: 720,409 and 235,000.

> 🟢 The borrowing base would allow 720,000 and the line has 450,000 unused, but the leverage covenant allows only 235,000 more debt. That's my real capacity: about half of the unused line.

> 🟢 Today the company carries 3.51 million of debt on 1.07 million of EBITDA, 3.28 times. There's little room before 3.5.

**WHY:** la disponibilidad real de un revolver basado en activos es el **mínimo** entre lo no usado del compromiso, el borrowing base (AR elegible × advance rate − reserves − lo ya girado) y lo que permite el covenant de apalancamiento. Suponer que todo lo no usado está disponible es el error que el Goal prohíbe.

**EXPECTED RESULT:** `720408.608 235000.0`

**DECISION:** el límite que manda es el **apalancamiento**: 3,5 × 1.070.000 − 3.510.000 = $235,000. Cualquier giro mayor queda descartado.

📘 **What each line does** (para vos, no se lee):

- `r = debt.iloc[0]`: the revolver row (RCF-01).
- `bb = r.advance_rate * o.amount.sum() - r.reserve - r.drawn`: borrowing base availability: 80% of open undisputed AR, minus the 150,000 reserve and the 750,000 already drawn.
- `cap = min(r.commitment - r.drawn, bb, r.max_leverage * r.ltm_ebitda - debt.drawn.sum())`: the tightest of unused commitment (450,000), borrowing base and leverage room.
- `print(bb, cap)`: borrowing base availability and real capacity.

---

### Bloque 6. Phase 4–5 — Alternativas, plan y estrés

**TIME:** 16:15–21:15 (5:00)

**WHAT I DO:** + Code → tipear 6 tramos → Run → señalar el giro y las cuatro filas.

**WHERE:** botón **+ Code** arriba a la izquierda (agrega la celda 6 debajo de la capacidad).

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell six below the capacity.

> 🟢 Now the alternatives. Free levers first; the revolver only covers what's left.

> 🗣️⌨️ First line of cell six: lever one, defer discretionary spend. I drop the capex and marketing rows, 179,000 dollars, to after week 13.

```python
p = f[f.discretionary.ne("Y")]
```
*(30 caracteres · ~13 s)*

> 🗣️⌨️ Next line of cell six: lever two, stretch suppliers, only as far as each contract allows. Critical suppliers, 62% of payables, have zero days, so they don't move.

```python
q = p.assign(week=p.week + p.max_extension_days.fillna(0) // 7)
```
*(63 caracteres · ~28 s)*

> 🗣️⌨️ Next line: the stress case. On top of both levers, the slowest payer, Northwind, pays two more weeks late, continuing its trend.

```python
s = q.assign(week=q.week + 2 * q.customer.eq(d.idxmax()))
```
*(57 caracteres · ~25 s)*

> 🗣️⌨️ Next line of cell six: the draw closes the gap in the stressed case, rounded up to 25,000, the way draws are requested.

```python
x = np.ceil((500000 - c(s).min()) / 25000) * 25000
```
*(50 caracteres · ~22 s)*

> 🗣️⌨️ Next line: one table to compare the base, the two levers, the plan with the draw, and the plan under stress.

```python
t = pd.DataFrame({"base": c(f), "levers": c(q), "plan": c(q) + x, "stress": c(s) + x})
```
*(86 caracteres · ~38 s)*

> 🗣️⌨️ Last lines of cell six: the draw, whether it fits the real capacity, and the lowest week of each scenario.

```python
print(x, x <= cap)
t.min()
```
*(26 caracteres · ~12 s)*

> 🖱️ I'm clicking the Run button on the left of cell six.

> 🖱️ I'm pointing at the levers row under cell six: 485,707.

> 🟢 Deferring and stretching lift the trough by 184,000 at no cost, but cash is still below 500,000. Cuts alone are not enough.

> 🖱️ I'm pointing at the first line: 225,000, True.

> 🟢 A 225,000 draw, now, fits inside the 235,000 of real capacity. Leverage goes to 3.49 times, just under the 3.5 limit.

> 🖱️ I'm pointing at the plan and stress rows: 710,707 and 518,909.

> 🟢 The plan never drops below 710,000, and even if Northwind pays two weeks later, cash stays above 500,000 every week.

> 🟢 I size the draw to the stress case, not the base, because the base is what got the company here.

> 🟢 The cost is small: 225,000 at 9.5% for 13 weeks is about 5,300 dollars of interest, to stay compliant every week.

**WHY:** las palancas sin costo van primero; la deuda cubre solo el resto. Dimensionar el giro con el caso estresado da colchón real, y el chequeo `x <= cap` prueba que el plan cumple compromiso, borrowing base y covenant a la vez.

**EXPECTED RESULT:**

- `225000.0 True`
- `base 301347.18`, `levers 485706.85`, `plan 710706.85`, `stress 518909.18`

**DECISION:**

- **Solo recortes (postergar + estirar):** descartado como solución completa. Gratis, +$184,360 en el piso, pero sigue debajo del mínimo.
- **Acelerar a Northwind:** no entra en el plan. Su mora reciente es la más alta (26,5 días); no hay evidencia de que mejore. Queda como acción de cobranza.
- **Plan:** postergar $179,000 + estirar solo proveedores no críticos + girar $225,000 ahora. Es viable: $225,000 ≤ $235,000.
- **¿Girar para la base o para el estrés?** Para el estrés: el piso estresado sin giro es $293,909, y hacen falta $206,091, redondeados a $225,000.

📘 **What each line does** (para vos, no se lee):

- `p = f[f.discretionary.ne("Y")]`: flows without discretionary spend (capex and marketing deferred past week 13).
- `q = p.assign(week=p.week + p.max_extension_days.fillna(0) // 7)`: supplier bills moved by the extension each contract allows (0 for critical suppliers); other rows don't move.
- `s = q.assign(week=q.week + 2 * q.customer.eq(d.idxmax()))`: stress: Northwind's collections (the customer with the largest delay) two weeks later.
- `x = np.ceil((500000 - c(s).min()) / 25000) * 25000`: the stressed shortfall, rounded up to 25,000.
- `t = pd.DataFrame({...})`: closing cash per week for base, levers, plan (levers + draw) and stress (stress + draw).
- `print(x, x <= cap)`: the draw and whether it fits the real capacity.
- `t.min()`: the lowest week of each scenario.

---

### Bloque 7. Conclusiones

**TIME:** 21:15–23:05 (1:50)

**WHAT I DO:** + Text → tipear 3 tramos → clic afuera → Cmd + S → abrir y cerrar Files.

**WHERE:** botón **+ Text** arriba a la izquierda de la barra de Colab (agrega la celda al final). Ícono de carpeta en la barra lateral izquierda.

**SAY:**

> 🖱️ I'm clicking plus Text at the top left, to add a text cell at the end of the notebook for the conclusions.

> 🗣️⌨️ In the text cell: the title.

```markdown
## Plan
```
*(7 caracteres · ~3 s)*

> 🗣️⌨️ Next line of the text cell: the plan and the limit it respects.

```markdown
- Defer, stretch, draw $225,000 (cap $235,000).
```
*(47 caracteres · ~21 s)*

> 🗣️⌨️ Last line: the AI declaration.

```markdown
- Input files generated with AI.
```
*(32 caracteres · ~14 s)*

> 🖱️ I'm clicking on the empty area below the text cell, to show it formatted.

> 🖱️ I'm pressing Command and S to save the notebook; the save message appears at the bottom left.

> 🖱️ I'm clicking the folder icon in the left sidebar, to open the Files panel.

> 🖱️ I'm pointing at accounts_receivable.csv: rewritten with the delay and the expected date for each invoice.

> 🖱️ I'm clicking the folder icon again to close the panel.

**EXPECTED RESULT:** la celda de texto con el título y dos viñetas, formateada. En Files, los cinco CSV; `accounts_receivable.csv` con fecha de modificación nueva. Si no se ve, decí: *"I'm clicking refresh at the top of the Files panel, to show the updated file."*

---

### Bloque 8. Epilogue

**TIME:** 23:05–24:15 (1:10)

**WHAT I DO:** scroll lento hacia arriba, sin tipear. Recién **después** abrís TaskRecorder para detener la grabación.

**WHERE:** Colab, desde las conclusiones hasta la celda 1.

**SAY:**

> 🖱️ I'm scrolling up slowly through the notebook, from the conclusions back to cell one.

> 🟢 The key decisions: free cash, not the bank total; each customer's recent delay, not the due date; and credit as the tightest of three limits.

> 🟢 The plan defers 179,000, stretches only non-critical suppliers and draws 225,000 now. It survives the stress, with leverage at 3.49.

> 🟢 The hardest part was the capacity: the line looked like 450,000, but the covenant allows only about half.

> 🟢 Open risks: only 10,000 of capacity left, Northwind at 46% of receivables, and the other customers' new sales still on management's dates. Next, I'd escalate Northwind's collections. Thanks for watching!

**WHY:** no repite los pasos: cuenta las decisiones, cómo se validaron y qué queda abierto.

---

## Si algo sale mal

| Error | Qué decís y hacés |
| ----- | ----------------- |
| Un nombre mal escrito | 🖱️ *"There's a typo in cell N. I'm clicking on that line to fix it, and running the cell again."* |
| `NameError` | 🖱️ *"An earlier cell didn't run. I'm opening the Runtime menu at the top and choosing Run before."* |
| `KeyError: 'week'` o resultados en `NaN` en la celda 6 | Falta `.fillna(0)` en la línea de `q`. 🖱️ *"I'm clicking at the end of the q line in cell six, to add fillna."* |
| Hay que volver a correr la celda 1 después de la celda 3 | El AR ya está reescrito y trae una columna `Unnamed: 0`. No cambia ningún resultado: decí *"The receivables file was already rewritten; the extra index column doesn't affect the analysis."* |
| La celda 6 da otros números | Revisá que `s` salga de `q` (no de `p`) y que `plan` sea `c(q) + x`. |

---

## Checklist de archivos y preparación previa

- [ ] Practicá dos veces con cronómetro. [liquidity_forecast.ipynb](liquidity_forecast.ipynb) tiene el código completo para comparar.
- [ ] En Colab, creá el notebook **liquidity_forecast** con **la celda 1 escrita** (copiala del bloque 1) y **la celda 2 vacía** debajo. **No ejecutes nada.**
- [ ] En **Files**, subí los cinco CSV de esta carpeta: `bank_transactions`, `accounts_receivable`, `accounts_payable`, `debt_facilities` y `operating_forecast`. Los de la carpeta son los originales: no los toques.
- [ ] **Tools → Settings → AI assistance**: ocultá las funciones de IA.
- [ ] **Tools → Settings → Editor**: si está la opción, desactivá las sugerencias automáticas de código.
- [ ] Probá el `~` en Colab (Option + ñ y espacio, o Shift + ` en teclado US).
- [ ] Zoom (`Cmd + +`). Firefox con la ventana 1 en la descripción de la tarea y la ventana 2 en Colab.

## Checklist de resultados que deben quedar generados

- [ ] `cash0` = 525,938 (celda 2).
- [ ] La mora reciente `d`, con Northwind en 26,5 días (celda 3).
- [ ] `accounts_receivable.csv` reescrito con `late` y `exp` (celda 3).
- [ ] El caso base, con el piso de 301,347 en la semana 9 (celda 4).
- [ ] La capacidad real `cap` = 235,000 (celda 5).
- [ ] Giro de 225,000 (`True`), plan 710,707 y estrés 518,909 (celda 6).
- [ ] La celda de conclusiones y el notebook guardado.
- [ ] Después: descargá el `.ipynb` y el `accounts_receivable.csv` reescrito. Armá **Deliverables.zip** con eso y la carpeta `original/` con los cinco CSV de esta carpeta. Marcá en Studio la opción de archivos generados con IA.

## Checklist de decisiones financieras que debo explicar

- [ ] **Caja de partida:** sin duplicados, neta de cheques emitidos, sin la reserva restringida ($525,938, no $1.11M).
- [ ] **Mora reciente:** mediana de los últimos 90 días; Northwind 26,5 días.
- [ ] **Exclusiones:** las facturas en disputa ($47,767) no se proyectan.
- [ ] **Forecast de la gerencia:** los cobros de ventas nuevas de Northwind se corren 3 semanas; $285,800 quedan después de la semana 13.
- [ ] **Temporal vs. estructural:** capital de trabajo, no pérdida operativa.
- [ ] **Capacidad real:** el mínimo de tres límites; manda el apalancamiento ($235,000 de $450,000 no usados).
- [ ] **Por qué no solo recortes:** el piso queda en $485,707, debajo del mínimo.
- [ ] **Por qué no acelerar a Northwind:** la evidencia muestra lo contrario.
- [ ] **Por qué dimensionar con el estrés:** la base es lo que llevó a la empresa a esta situación.
- [ ] **Riesgos pendientes:** $10,000 de capacidad libre, concentración del 46% en Northwind, cobros de los demás clientes en fechas de la gerencia, el capex vuelve después de la semana 13.

---

## Conclusión para cerrar la grabación (en inglés)

> The company's bank file adds up to 1.11 million dollars, but only 526,000 is free cash. With Northwind paying almost four weeks late, cash is below the 500,000 minimum from the first week and bottoms out at 301,000 in week 9. Deferring discretionary spend and stretching non-critical suppliers help, but not enough. The revolver can't fix it alone either: the leverage covenant caps new debt at 235,000. So the plan combines both levers with a 225,000 draw now. Cash stays above the minimum every week, even if Northwind pays two more weeks late. What's left to watch is the thin 10,000 of capacity and Northwind's concentration.

*(Es la versión larga del epilogue. Si te sobra tiempo, podés decirla en lugar de las tres 🟢 del bloque 8; si no, las 🟢 alcanzan.)*

---

## Pendientes antes de grabar

| Tema | Qué hacer |
| ---- | --------- |
| **Descripción de TaskRecorder y Metadata** | Abajo hay una propuesta que coincide con este guion. Pegala o pasame los campos reales para ajustarla. |
| **Origen de los CSV** | Los generé yo, Claude, con [_generador/generate_data.py](_generador/generate_data.py). Decí "generated with AI" y marcá en Studio la opción de archivos generados con IA. |
| **Carpeta `_generador/`** | Tiene el generador, el código de las celdas y el script que lo ejecuta. No va en la entrega. |

**Descripción (propuesta):**

> Rebuild the 13-week liquidity position of a simulated mid-sized company in Google Colab with pandas. I reconcile bank transactions to find free cash, measure each customer's recent payment delay, and build a weekly forecast that shows when cash drops below the 500,000 minimum. I calculate real revolver capacity from the borrowing base and the leverage covenant, compare cost-free levers with a revolver draw, size the draw to a stress case, and rewrite the receivables file with expected collection dates.
