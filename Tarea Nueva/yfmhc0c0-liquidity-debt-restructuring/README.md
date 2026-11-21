# yfmhc0c0 — 13-Week Liquidity & Debt Restructuring Analysis

Guion para grabar la tarea **yfmhc0c0** en **Google Colab** (app principal), con **Firefox** como app de apoyo, en una sola toma.

> **Goal:** *Reconstruct and stress-test the 13-week liquidity position of a simulated mid-sized company facing tightening cash availability, customer payment delays, and upcoming debt obligations. (…) Deliver an auditable weekly liquidity model, scenario comparisons, and a justified financing action plan that maintains minimum cash requirements while respecting contractual borrowing limits.*

**Duración estimada: ~24:00** (máximo 25).

**Punto de partida al grabar:** la celda 1 ya está escrita y los cinco CSV ya están cargados en el panel **Files** de Colab. No se sube nada ni se tipea la carga: ese tiempo se usa para explicar.

---

## Cronograma

| # | Bloque | Fase de Dawn | Celda | TIME | Duración |
| - | ------ | ------------ | ----- | ---- | -------- |
| 0 | Opening | — | — | 0:00–1:10 | 1:10 |
| 1 | Carga y contratos | Phase 1 | 1 (ya escrita) | 1:10–3:10 | 2:00 |
| 2 | Posición de caja real | Phase 1 | 2 (se tipea) | 3:10–6:05 | 2:55 |
| 3 | Confiabilidad de los flujos | Phase 2 | 3 (armada) | 6:05–8:20 | 2:15 |
| 4 | Proyección de 13 semanas | Phase 3 | 4 (armada) | 8:20–10:10 | 1:50 |
| 5 | Capacidad real de endeudamiento | Phase 4 | 5 (se tipea) | 10:10–13:40 | 3:30 |
| 6 | Comparación de alternativas | Phase 4 | 6 (armada) | 13:40–15:35 | 1:55 |
| 7 | Plan elegido y estrés | Phase 5 | 7 (se tipea) | 15:35–19:10 | 3:35 |
| 8 | Exportación y registro de decisiones | Phase 5 | 8 (armada) | 19:10–20:45 | 1:35 |
| 9 | Conclusiones | Phase 5 | texto (se tipea) | 20:45–23:05 | 2:20 |
| 10 | Epilogue | — | — | 23:05–24:00 | 0:55 |
| | **Total** | | | | **~24:00** |

*(Calculado con 130 palabras/min de narración, 135 caracteres/min de tipeo en silencio, todo sumado, más ~20 s de navegación y ejecución por bloque.)*

**Margen:** 1:00 hasta 25:00. Si en la práctica pasás de 24:30, recortá **palabras de las 🟢** (nunca las 🖱️ ni las 🗣️⌨️).

---

## Verificación de los archivos de entrada

Los cinco CSV los generé yo (Claude) con [_generador/generate_data.py](_generador/generate_data.py) (semilla fija, reproducible). Cada valor contractual del Goal **está en los archivos**:

| Restricción del Goal | Dónde está |
| -------------------- | ---------- |
| Minimum unrestricted cash USD 500,000 | `debt_facilities.csv` → `min_unrestricted_cash` (fila RCF-01) |
| Revolver commitment USD 1,200,000 | `debt_facilities.csv` → `commitment` (fila RCF-01) |
| Max leverage 3.5x | `debt_facilities.csv` → `max_leverage` + `ltm_ebitda` (fila RCF-01) |
| Advance rate, reserves, deuda usada | `advance_rate`, `reserve`, `drawn`, `eligibility_days`, `concentration_limit` |

**Contradicción resuelta:** el apalancamiento necesita EBITDA, que no venía en ninguno de los cinco archivos. Lo agregué como `ltm_ebitda` en la fila del revolver, porque es el EBITDA del último *compliance certificate* del contrato. Así sale del archivo y no se inventa.

**Archivos** (sintéticos, fecha de corte viernes 2026-11-20, semana 1 = lunes 2026-11-23):

| Archivo | Filas | Columnas clave | Problemas que tiene |
| ------- | ----- | -------------- | ------------------- |
| `bank_transactions.csv` | 164 | `txn_id, date, account_id, account_type, description, reference, amount, status` | 5 filas duplicadas ($202,453 de caja inflada); 3 cheques emitidos sin compensar ($64,150); una cuenta restringida (reserva de deuda, $381,900); un cobro devuelto por falta de fondos |
| `accounts_receivable.csv` | 456 | `invoice_id, customer, invoice_date, due_date, amount, status, paid_date` | Historial pagado desde marzo + facturas abiertas. Northwind (45% del AR abierto) pasó de 6 a 26,5 días de mora; 2 facturas en disputa; 2 vencidas hace más de 90 días; 1 marcada `paid` cuyo cobro el banco devolvió |
| `accounts_payable.csv` | 46 | `bill_id, vendor, category, bill_date, due_date, amount, critical, max_extension_days` | El 62% es con proveedores críticos que no aceptan prórroga |
| `debt_facilities.csv` | 3 | `facility_id, facility_type, commitment, drawn, interest_rate, next_payment_date, payment_months, scheduled_payment` + términos del revolver | Revolver, term loan (cuota de $168,000 en la semana 8) y préstamo de equipos |
| `operating_forecast.csv` | 58 | `week, week_start, category, customer, amount, discretionary` | La gerencia proyecta cobros de ventas nuevas **en plazo**, sin mora; $179,000 de gasto discrecional (capex y marketing) |

**Cómo cubre cada fase:**

| Fase de Dawn | Celdas | Qué produce para la siguiente |
| ------------ | ------ | ----------------------------- |
| 1. Reconstruct the financial position | 1, 2, inicio de 3 | `cash0` = $716,256 de caja libre real; la factura NSF reabierta |
| 2. Reliability of cash flows | 3 | `o` (AR cobrable con fecha esperada), `delay`, `op` ajustado, `el` (AR elegible) |
| 3. 13-week forecast | 4 | `forecast()` y `base`: 7 semanas bajo el mínimo, piso de $289,365 en la semana 9 |
| 4. Financing alternatives | 5, 6 | `cap` = $235,000 de capacidad real; tabla `cmp` con las cinco alternativas y el estrés |
| 5. Mitigation strategy | 7, 8, texto | `plan` y `stress`, giro de $225,000, `financing_plan.csv`, gráfico |

**Criterios de Slack que cubre:**

- Los cinco CSV se reescriben en Colab con los mismos nombres: el banco con la marca `dup`, el AR con `status_raw`, `days_late`, `expected_date` e `in_forecast`, el AP con `due_date_raw` y el forecast operativo con `week_raw` y `deferred`. Los originales quedan en el Escritorio.
- Todo el impacto está en dólares.
- Cada alternativa descartada tiene su número y su razón.
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
| Tipeo en vivo (celdas 2, 5 y 7 + conclusiones) | 911 caracteres | ~6,7 min a 135 car./min (~6 a 150; ~7,6 a 120) |
| Narración | ~1.800 palabras | ~13,9 min |
| Navegación, ejecución y Files | 11 bloques | ~3,5 min |
| **Total** | | **~24:00** (~25:00 si tipeás a 120 car./min) |

**Tipeo: ~28% del video** (~30% a 120 car./min; máximo 35%). La celda 1 y la carga de archivos no suman tipeo: ya están hechas antes de grabar.

**Qué celdas van armadas y por qué:**

| Celda | Estado | Por qué |
| ----- | ------ | ------- |
| 1. Carga y contratos | **Ya escrita** | Es mecánica: leer y perfilar. Se explica línea por línea en lugar de tipearla. |
| 2. Posición de caja | Se tipea | Decisión: qué cuenta como caja disponible. |
| 3. Confiabilidad | **Armada** | Son muchas reglas cortas; se explican señalando cada grupo de líneas. |
| 4. Motor de proyección | **Armada** | Es el armado mecánico de la tabla semanal. |
| 5. Capacidad real | Se tipea | Es la restricción contractual central. |
| 6. Alternativas | **Armada** | Es repetir el motor con cada palanca. |
| 7. Plan y estrés | Se tipea | Es la decisión final: cuánto girar y cuándo. |
| 8. Exportación | **Armada** | Es mecánica: guardar y graficar. |

**Reglas de tipeo:**

1. **Nunca hablar y tipear al mismo tiempo.** Frase 🗣️⌨️ con las manos quietas → bloque en silencio.
2. **Ningún tramo pasa de 45 segundos.** El más largo tiene 83 caracteres (~37 s a 135 car./min).
3. **Nada de tipeo extra:** ni comentarios ni `print` de prueba.
4. **Sin autocompletado.** Si aparece una caja de sugerencias, Escape.

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

> 🟢 I will be beginning my task soon. A mid-sized company is short on cash: its biggest customer pays later and a loan payment is due. Over 13 weeks, I'll find a plan that keeps 500,000 of free cash within its loan limits.

> 🟢 I'll reconcile the bank, test the cash flows, build the weekly forecast, measure real borrowing capacity, and stress-test my plan.

> 🖱️ I'm clicking the yellow minimize button at the top left, to hide the task description.

> 🖱️ I'm clicking the Firefox icon in the Dock and choosing the second window: my Colab notebook.

> 🟢 The five input CSVs are already uploaded to this notebook's Files panel. They're synthetic, generated with AI; the notebook rewrites them, and the originals stay on my Desktop.

**WHY:** el revisor tiene que saber desde el minuto uno qué es "éxito": $500,000 libres todas las semanas, sin pasar ningún límite del contrato.

**EXPECTED RESULT:** el notebook con las celdas 1, 3, 4, 6 y 8 llenas y las 2, 5 y 7 vacías. El panel Files queda cerrado: se abre recién en el bloque 8, cuando ya están los ocho CSV.

---

### Bloque 1. Phase 1 — Carga y contratos

**TIME:** 1:10–3:10 (2:00)

**WHAT I DO:** señalar cada grupo de líneas de la celda 1 (ya escrita) → Run → señalar la salida.

**WHERE:** celda 1, arriba de todo. Botón Run (triángulo) a la izquierda de la celda.

**Celda 1 (ya escrita antes de grabar):**

```python
import pandas as pd
import numpy as np
b = pd.read_csv("bank_transactions.csv", parse_dates=["date"])
ar = pd.read_csv("accounts_receivable.csv", parse_dates=["invoice_date", "due_date", "paid_date"])
ap = pd.read_csv("accounts_payable.csv", parse_dates=["bill_date", "due_date"])
debt = pd.read_csv("debt_facilities.csv", parse_dates=["next_payment_date"])
op = pd.read_csv("operating_forecast.csv", parse_dates=["week_start"])
for n, d in {"bank": b, "ar": ar, "ap": ap, "debt": debt, "op": op}.items():
    print(n, d.shape, "| duplicate rows:", d.duplicated().sum())
print(b.groupby(["account_id", "account_type", "status"]).amount.sum().round(0).to_dict())
debt.set_index("facility_id").T
```

**SAY:**

> 🟢 Phase one: reconstructing the real financial position.

> 🖱️ I'm pointing at cell one, which I wrote before recording, because loading files is routine. I'll use the time to explain it instead.

> 🖱️ I'm pointing at the first two read_csv lines in cell one: the bank movements and the customer invoices. Dates are parsed because every collection depends on a due date.

> 🖱️ I'm pointing at the next three lines: supplier bills, the three debt facilities with the revolver's terms, and management's weekly forecast.

> 🖱️ I'm pointing at the loop in cell one: for each file, its size and its fully duplicated rows. That's my first data-quality check.

> 🖱️ I'm pointing at the next print line: the bank balance by account and status, before any cleaning, so I can compare it with the cleaned one in cell two.

> 🖱️ I'm pointing at the last line of cell one: the debt table turned sideways, one column per facility, to read the contract terms.

> 🖱️ I'm clicking the Run button on the left of cell one.

> 🖱️ I'm pointing at the bank line under cell one: 5 fully duplicated rows.

> 🟢 That's an export error that inflates cash.

> 🖱️ I'm pointing at the balances: three accounts, one restricted, plus pending checks.

> 🟢 So the bank's total is not my available cash.

> 🖱️ I'm pointing at the RCF-01 column of the debt table, under cell one.

> 🟢 These are my limits: 1.2 million committed, 750,000 drawn, an 80% advance rate, a 150,000 reserve, 500,000 minimum unrestricted cash, and leverage up to 3.5 times EBITDA of 1.07 million.

**WHY:** las restricciones del Goal tienen que salir del contrato (el archivo), no de supuestos. Mostrarlas al principio deja claro de dónde sale cada límite.

**EXPECTED RESULT:**

- `bank (164, 8) | duplicate rows: 5`; `ar (456, 7)`, `ap (46, 8)`, `debt (3, 17)`, `op (58, 6)`, todas con `duplicate rows: 0`.
- `{('DSR-03', 'restricted', 'cleared'): 381900.0, ('OPR-01', 'operating', 'cleared'): 957859.0, ('OPR-01', 'operating', 'pending'): -64150.0, ('PAY-02', 'operating', 'cleared'): 25000.0}`
- La tabla del contrato: RCF-01 con `commitment 1200000`, `drawn 750000`, `advance_rate 0.8`, `reserve 150000`, `min_unrestricted_cash 500000`, `max_leverage 3.5`, `ltm_ebitda 1070000`; TL-01 con `scheduled_payment 168000` y `next_payment_date 2027-01-15`.

📘 **What each line does** (para vos, no se lee):

- `import pandas as pd` / `import numpy as np`: loads pandas and NumPy.
- `b = pd.read_csv("bank_transactions.csv", ...)`: bank movements, with `date` as a real date.
- `ar = pd.read_csv("accounts_receivable.csv", ...)`: customer invoices, with invoice, due and paid dates parsed.
- `ap = pd.read_csv("accounts_payable.csv", ...)`: open supplier bills.
- `debt = pd.read_csv("debt_facilities.csv", ...)`: the three facilities and the revolver's terms.
- `op = pd.read_csv("operating_forecast.csv", ...)`: management's weekly operating forecast.
- `for n, d in {...}.items():`: loops over the five tables with their names.
- `print(n, d.shape, ..., d.duplicated().sum())`: rows, columns and fully duplicated rows.
- `print(b.groupby(["account_id", "account_type", "status"]).amount.sum()...)`: raw balance per account, type and status.
- `debt.set_index("facility_id").T`: the debt table turned sideways, one column per facility.

---

### Bloque 2. Phase 1 — Posición de caja real

**TIME:** 2:50–5:45 (2:55)

**WHAT I DO:** clic en la celda 2 → tipear 4 tramos → Run → señalar la salida.

**WHERE:** celda 2, vacía, debajo de la tabla del contrato.

**SAY:**

> 🖱️ I'm clicking inside cell two, the empty cell below the contract table.

> 🗣️⌨️ First line of cell two: I flag repeated transaction IDs instead of deleting them, so the bank file stays auditable.

```python
b["dup"] = b.duplicated("txn_id")
```
*(33 caracteres · ~15 s)*

> 🗣️⌨️ Next line of cell two: without duplicates, the balance by account type and status.

```python
pos = b[~b.dup].groupby(["account_type", "status"]).amount.sum()
```
*(64 caracteres · ~28 s)*

> 🗣️⌨️ Next line: opening cash is only the operating side, net of pending checks, which are already written. The restricted reserve is the lender's, so it's out.

```python
cash0 = pos["operating"].sum()
```
*(30 caracteres · ~13 s)*

> 🗣️⌨️ Last lines of cell two: the dollars in duplicates, my opening cash, and the position table.

```python
print(b[b.dup].amount.sum().round(), cash0.round())
pos
```
*(55 caracteres · ~24 s)*

> 🖱️ I'm clicking the Run button on the left of cell two.

> 🖱️ I'm pointing at the first printed number under cell two: 202,453.

> 🟢 The duplicated rows would have overstated cash by 202,453 dollars.

> 🖱️ I'm pointing at the second number: 716,256.

> 🟢 That's my real opening cash, not the 1.36 million the export suggests: duplicates, written checks and the restricted reserve come out. I start just 216,000 above the minimum.

**WHY:** la posición inicial tiene que ser caja **libre y disponible**: sin duplicados, neta de cheques emitidos (ya comprometidos) y sin la reserva restringida, que no se puede usar para pagar operaciones.

**EXPECTED RESULT:**

- `202453.0 716256.0`
- Tabla `pos`: `operating cleared 780405.82`, `operating pending -64150.00`, `restricted cleared 381900.00`.

**DECISION:** ¿los cheques pendientes cuentan? **Sí, se restan**: ya salieron de los libros y van a compensarse. Contarlos como caja sobreestimaría $64,150. ¿La reserva restringida cuenta? **No**: el covenant habla de *unrestricted cash*.

📘 **What each line does** (para vos, no se lee):

- `b["dup"] = b.duplicated("txn_id")`: `True` for the second and later copies of a transaction ID.
- `pos = b[~b.dup].groupby(...).amount.sum()`: balance by account type and status, without duplicates.
- `cash0 = pos["operating"].sum()`: operating cleared plus pending (the pending checks are negative).
- `print(b[b.dup].amount.sum().round(), cash0.round())`: duplicated dollars and opening cash.
- `pos`: shows the position table.

---

### Bloque 3. Phase 2 — Confiabilidad de los flujos

**TIME:** 5:45–8:00 (2:15)

**WHAT I DO:** señalar los grupos de líneas de la celda 3 → Run → señalar cada línea de la salida.

**WHERE:** celda 3 (armada), debajo de la tabla de posición.

**Celda 3 (armada antes de grabar):**

```python
net = b[~b.dup].groupby("reference").amount.sum()
nsf = ar.status.eq("paid") & ar.invoice_id.map(net).eq(0)
ar["status_raw"] = ar.status
ar.loc[nsf, "status"] = "returned"
print("NSF:", ar.loc[nsf, ["invoice_id", "customer", "amount"]].values.tolist())
ASOF = pd.Timestamp("2026-11-20")
ar["days_late"] = (ar.paid_date - ar.due_date).dt.days
recent = ar[ar.paid_date > ASOF - pd.Timedelta(days=90)]
delay = recent.groupby("customer").days_late.median().clip(lower=0)
o = ar[ar.status.eq("open")].copy()
o["expected"] = o.due_date + pd.to_timedelta(o.customer.map(delay), "D")
o["collect"] = (ASOF - o.due_date).dt.days.le(90)
share = o.groupby("customer").amount.sum().sort_values(ascending=False) / o.amount.sum()
top = share.index[0]
print(top, "share of open AR:", round(share.iloc[0], 2), "| median days late, all history:", ar[ar.customer.eq(top)].days_late.median(), "| last 90 days:", delay[top])
print("excluded from forecast $:", ar[ar.status.isin(["disputed", "returned"])].amount.sum().round(0), "disputed/NSF +", o[~o.collect].amount.sum().round(0), "over 90 days past due")
print("AP share with critical suppliers:", round(ap[ap.critical.eq("Y")].amount.sum() / ap.amount.sum(), 2), "| discretionary spend:", op[op.discretionary.eq("Y")].amount.sum())
delay["Other customers"] = recent[recent.customer.ne(top)].days_late.median()
op["week_raw"] = op.week
op["week"] += (op.customer.map(delay) / 7).round().fillna(0).astype(int)
print("new-sales collection lag (weeks):", (op.week - op.week_raw).groupby(op.customer).max().to_dict(), "| $ pushed past week 13:", op[op.week > 13].amount.sum())
el = o[(ASOF - o.invoice_date).dt.days.le(debt.eligibility_days[0])].groupby("customer").amount.sum()
```

**SAY:**

> 🖱️ I'm pointing at the first lines of cell three, prepared before recording, closing phase one: a paid invoice whose bank receipts net to zero bounced, so I reopen it.

> 🟢 Phase two: how reliable are these cash flows?

> 🖱️ I'm pointing at the delay lines in cell three: each customer's median days late over the last 90 days, not the whole history.

> 🖱️ I'm pointing at the expected line: due date plus that delay. Invoices over 90 days past due stay out.

> 🖱️ I'm pointing at the op lines at the bottom: management's new-sales collections get the same delays.

> 🖱️ I'm clicking the Run button on the left of cell three.

> 🖱️ I'm pointing at the NSF line under cell three: invoice 10300, Harbor Cafe, 9,682 dollars.

> 🟢 Receivables said paid, but the bank returned it.

> 🖱️ I'm pointing at the Northwind line: 45% of open receivables, 6 days late on the full history, 26.5 in the last 90 days.

> 🟢 The full history would hide the slowdown, so I use the recent window.

> 🖱️ I'm pointing at the excluded line: 57,449 dollars disputed or returned, and 25,553 over 90 days past due.

> 🟢 No evidence they'll be paid, so they're out.

> 🖱️ I'm pointing at the AP line: 62% of payables are with critical suppliers.

> 🟢 Those can't be stretched. And 179,000 of discretionary spend could be deferred.

> 🖱️ I'm pointing at the last line: Northwind's new sales arrive 4 weeks later than management assumed, others 1 week; 589,000 moves past week 13.

**WHY:** proyectar con el promedio histórico sobreestimaría los cobros, porque Northwind cambió de comportamiento en agosto. Lo disputado, lo devuelto y lo muy vencido no es caja confiable. El ajuste del forecast de la gerencia se apoya en la mora medida, no en un supuesto.

**EXPECTED RESULT:**

- `NSF: [['INV-10300', 'Harbor Cafe Group', 9682.38]]`
- `Northwind Retail share of open AR: 0.45 | median days late, all history: 6.0 | last 90 days: 26.5`
- `excluded from forecast $: 57449.0 disputed/NSF + 25553.0 over 90 days past due`
- `AP share with critical suppliers: 0.62 | discretionary spend: -179000.0`
- `new-sales collection lag (weeks): {'Northwind Retail': 4, 'Other customers': 1} | $ pushed past week 13: 589000.0`

**DECISION:** ¿historial completo o últimos 90 días? **Últimos 90**: la mora de Northwind pasó de 6 a 26,5 días; usar el historial completo adelantaría cobros que la evidencia no respalda.

📘 **What each line does** (para vos, no se lee):

- `net = b[~b.dup].groupby("reference").amount.sum()`: net bank amount per reference (invoice ID for customer receipts).
- `nsf = ar.status.eq("paid") & ar.invoice_id.map(net).eq(0)`: invoices marked paid whose receipt was reversed (net zero).
- `ar["status_raw"] = ar.status`: keeps the original status.
- `ar.loc[nsf, "status"] = "returned"`: reopens the NSF invoice with its own status.
- `print("NSF:", ...)`: shows the reopened invoice.
- `ASOF = pd.Timestamp("2026-11-20")`: the cut-off date.
- `ar["days_late"] = ...`: paid date minus due date, per paid invoice.
- `recent = ar[ar.paid_date > ASOF - pd.Timedelta(days=90)]`: payments of the last 90 days.
- `delay = recent.groupby("customer").days_late.median().clip(lower=0)`: each customer's recent median delay; early payers count as 0.
- `o = ar[ar.status.eq("open")].copy()`: open invoices only (not disputed or returned).
- `o["expected"] = ...`: expected collection date = due date + customer delay.
- `o["collect"] = ...`: `False` for invoices more than 90 days past due.
- `share = ...`: each customer's share of open receivables, largest first.
- `top = share.index[0]`: the largest customer.
- `print(top, ...)`: its share and its full-history vs. recent median delay.
- `print("excluded from forecast $:", ...)`: dollars left out of the forecast.
- `print("AP share with critical suppliers:", ...)`: share of payables that can't be stretched, and the discretionary total.
- `delay["Other customers"] = ...`: one recent delay for all customers other than the top one.
- `op["week_raw"] = op.week`: keeps management's original week.
- `op["week"] += ...`: shifts each collection row by its customer's delay, in weeks; other rows don't move.
- `print("new-sales collection lag (weeks):", ...)`: the shift and the dollars pushed beyond week 13.
- `el = ...`: open receivables invoiced within the eligibility window, per customer (input for the borrowing base).

---

### Bloque 4. Phase 3 — Proyección de 13 semanas

**TIME:** 8:00–9:50 (1:50)

**WHAT I DO:** señalar las líneas de la celda 4 → Run → señalar la línea impresa y la columna `close`.

**WHERE:** celda 4 (armada), debajo de la salida de la celda 3.

**Celda 4 (armada antes de grabar):**

```python
W1 = pd.Timestamp("2026-11-23")
MIN = debt.min_unrestricted_cash[0]
wk = lambda d: ((d - W1).dt.days // 7 + 1).clip(lower=1)
ds = pd.concat([pd.DataFrame({"date": pd.date_range(r.next_payment_date, "2027-02-21", freq=pd.DateOffset(months=r.payment_months)), "amount": r.scheduled_payment}) for r in debt.itertuples()])
def forecast(o, ap, op, draw={}):
    f = pd.DataFrame(index=range(1, 14))
    f["ar_in"] = o[o.collect].groupby(wk(o.expected)).amount.sum()
    f["operating"] = op.groupby("week").amount.sum()
    f["ap_out"] = -ap.groupby(wk(ap.due_date)).amount.sum()
    f["debt_out"] = -ds.groupby(wk(ds.date)).amount.sum()
    f["rcf_draw"] = pd.Series(draw, dtype=float)
    f = f.fillna(0)
    f["close"] = cash0 + f.sum(axis=1).cumsum()
    return f
base = forecast(o, ap, op)
low = base.index[base.close < MIN]
print("weeks below", MIN, ":", list(low), "| trough:", round(base.close.min()), "in week", base.close.idxmin(), "| week 13:", round(base.close.iloc[-1]), "| net flow weeks 12-13:", round(base.close.diff().tail(2).mean()))
base.round(0)
```

**SAY:**

> 🟢 Phase three: the 13-week forecast.

> 🖱️ I'm pointing at the top of cell four: week one, and the minimum read from the contract file.

> 🖱️ I'm pointing at the ds line: debt service from each facility's payment dates.

> 🖱️ I'm pointing at the forecast function in cell four: each week adds collections, operating items, bills, debt service and any draw; closing cash is the running total.

> 🟢 It's a function so phases four and five reuse the same engine.

> 🖱️ I'm clicking the Run button on the left of cell four.

> 🖱️ I'm pointing at the printed line under cell four: below the minimum from week 7 to week 13, with a trough of 289,365 in week 9.

> 🖱️ I'm moving the mouse down the close column of the table, from week 6 to week 9.

> 🟢 That's the year-end bonus, insurance, and the 168,000 loan payment in week 8, while Northwind pays later.

> 🖱️ I'm pointing at the end of the printed line: week 13 closes at 385,100, but the last two weeks average plus 43,000.

> 🟢 So it's not an operating loss; it's a working-capital hole from Northwind's delay that outlasts the 13 weeks. A one-week bridge won't fix it; I need committed funding.

**WHY:** separar el déficit **temporal** (timing y pagos únicos) del **estructural** (pérdida operativa) decide el tipo de financiación. Como el flujo semanal vuelve a ser positivo pero la caja no recupera el mínimo antes de la semana 13, el déficit es de capital de trabajo y dura más que la ventana.

**EXPECTED RESULT:**

`weeks below 500000.0 : [7, 8, 9, 10, 11, 12, 13] | trough: 289365 in week 9 | week 13: 385100 | net flow weeks 12-13: 43000`

| week | ar_in | operating | ap_out | debt_out | close |
| ---- | ----- | --------- | ------ | -------- | ----- |
| 1 | 346,699 | -124,000 | -377,612 | 0 | 561,342 |
| 4 | 289,660 | -23,000 | -179,373 | 0 | 708,760 |
| 6 | 135,606 | -193,100 | -24,919 | -21,438 | 517,662 |
| 7 | 102,404 | -193,900 | 0 | 0 | 426,166 |
| 8 | 86,245 | -8,600 | 0 | -168,000 | 335,811 |
| 9 | 101,654 | -148,100 | 0 | 0 | **289,365** |
| 11 | 0 | -51,900 | 0 | -15,500 | 299,100 |
| 13 | 0 | -6,000 | 0 | 0 | 385,100 |

**DECISION:** ¿temporal o estructural? **Capital de trabajo, más largo que la ventana**: el flujo de las semanas 12–13 es +$43,000 por semana (no hay pérdida operativa), pero $589,000 de cobros de Northwind quedan después de la semana 13. Por eso se necesita financiación comprometida, no un puente de una semana.

📘 **What each line does** (para vos, no se lee):

- `W1 = pd.Timestamp("2026-11-23")`: Monday of week 1.
- `MIN = debt.min_unrestricted_cash[0]`: the 500,000 minimum, read from the revolver row.
- `wk = lambda d: ...`: turns a date column into a week number 1–13; anything already overdue lands in week 1.
- `ds = pd.concat([...])`: every scheduled debt payment inside the window (monthly or quarterly, from `payment_months`).
- `def forecast(o, ap, op, draw={}):`: the weekly engine; its inputs are receivables, payables, the operating forecast and any revolver draws.
- `f = pd.DataFrame(index=range(1, 14))`: one row per week.
- `f["ar_in"] = ...`: collectible invoices by expected week.
- `f["operating"] = ...`: operating forecast by (adjusted) week.
- `f["ap_out"] = ...`: supplier bills by due week, negative.
- `f["debt_out"] = ...`: debt service by week, negative.
- `f["rcf_draw"] = pd.Series(draw, dtype=float)`: revolver draws, if any, by week.
- `f = f.fillna(0)`: weeks with no flow are 0.
- `f["close"] = cash0 + f.sum(axis=1).cumsum()`: closing cash each week.
- `return f`: returns the table.
- `base = forecast(o, ap, op)`: the adjusted base case.
- `low = base.index[base.close < MIN]`: weeks below the minimum.
- `print(...)`: breach weeks, trough, week 13 and the average weekly flow of the last two weeks.
- `base.round(0)`: shows the weekly model.

---

### Bloque 5. Phase 4 — Capacidad real de endeudamiento

**TIME:** 9:50–13:20 (3:30)

**WHAT I DO:** clic en la celda 5 → tipear 5 tramos → Run → señalar los cuatro números.

**WHERE:** celda 5, vacía, debajo de la tabla semanal.

**SAY:**

> 🖱️ I'm clicking inside cell five, the empty cell below the weekly table.

> 🟢 Phase four: how much can I really borrow?

> 🗣️⌨️ First lines of cell five: the revolver row, and the concentration limit, so no customer counts for more than 25% of eligible receivables.

```python
r = debt.iloc[0]
e = el.clip(upper=r.concentration_limit * el.sum())
```
*(68 caracteres · ~30 s)*

> 🗣️⌨️ Next line of cell five: the borrowing base. Eighty percent of eligible receivables, minus the reserve, minus what's already drawn.

```python
bb = r.advance_rate * e.sum() - r.reserve - r.drawn
```
*(51 caracteres · ~23 s)*

> 🗣️⌨️ Next line: leverage room. 3.5 times EBITDA, minus all the debt of the three facilities.

```python
lev = r.max_leverage * r.ltm_ebitda - debt.drawn.sum()
```
*(54 caracteres · ~24 s)*

> 🗣️⌨️ Next line of cell five: the real capacity is the tightest of the three limits.

```python
cap = min(r.commitment - r.drawn, bb, lev)
```
*(42 caracteres · ~19 s)*

> 🗣️⌨️ Last line of cell five: print the three limits and the capacity.

```python
print(r.commitment - r.drawn, round(bb), lev, cap)
```
*(50 caracteres · ~22 s)*

> 🖱️ I'm clicking the Run button on the left of cell five.

> 🖱️ I'm pointing at the four numbers under cell five: 450,000, 379,919, 235,000 and 235,000.

> 🟢 The line has 450,000 unused and the borrowing base allows 379,919, but the leverage covenant allows only 235,000. That's my real capacity: about half the unused line.

**WHY:** la disponibilidad real de un revolver basado en activos es el **mínimo** entre lo no usado del compromiso, el borrowing base (AR elegible × advance rate − reserves − lo ya girado) y lo que permite el covenant de apalancamiento. Suponer que todo lo no usado está disponible es el error que el Goal prohíbe.

**EXPECTED RESULT:** `450000 379919 235000.0 235000.0`

**DECISION:** el límite que manda es el **apalancamiento** ($235,000), no el compromiso ($450,000) ni el borrowing base ($379,919). Cualquier giro mayor a $235,000 queda descartado.

📘 **What each line does** (para vos, no se lee):

- `r = debt.iloc[0]`: the revolver row (RCF-01).
- `e = el.clip(upper=r.concentration_limit * el.sum())`: eligible receivables per customer, capped at 25% of the total.
- `bb = r.advance_rate * e.sum() - r.reserve - r.drawn`: borrowing base availability after the reserve and the current draw.
- `lev = r.max_leverage * r.ltm_ebitda - debt.drawn.sum()`: extra debt allowed before leverage hits 3.5x.
- `cap = min(r.commitment - r.drawn, bb, lev)`: the real capacity, the tightest limit.
- `print(...)`: the three limits and the capacity.

---

### Bloque 6. Phase 4 — Comparación de alternativas

**TIME:** 13:20–15:15 (1:55)

**WHAT I DO:** señalar los grupos de líneas de la celda 6 → Run → señalar la línea del estrés y las filas de la tabla.

**WHERE:** celda 6 (armada), debajo de la salida de la celda 5.

**Celda 6 (armada antes de grabar):**

```python
ap2 = ap.assign(due_date=ap.due_date + pd.to_timedelta(ap.max_extension_days, "D"))
op2 = op[op.discretionary.eq("N")]
o2 = o.assign(expected=o.expected.where(o.customer.ne(top), o.due_date))
op3 = op.assign(week=op.week.where(op.customer.ne(top), op.week_raw))
alts = {"base": base,
        "revolver": forecast(o, ap, op, {low[0]: cap}),
        "accelerate": forecast(o2, ap, op3),
        "defer": forecast(o, ap, op2),
        "stretch": forecast(o, ap2, op),
        "defer+stretch": forecast(o, ap2, op2)}
cmp = pd.DataFrame({k: {"trough": f.close.min(), "weeks_below_min": (f.close < MIN).sum(), "week13": f.close.iloc[-1]} for k, f in alts.items()}).T
cmp["gain_at_trough"] = cmp.trough - cmp.trough["base"]
cmp["cost"] = 0.0
cmp.loc["revolver", "cost"] = cap * r.interest_rate * (14 - low[0]) / 52
ost = o.assign(expected=o.expected + pd.to_timedelta(14 * o.customer.eq(top), "D"))
ops = op2.assign(week=op2.week + 2 * op2.customer.eq(top))
spre = forecast(ost, ap2, ops)
print("stress: Northwind 14 more days late, with defer + stretch | trough:", round(spre.close.min()), "in week", spre.close.idxmin(), "| without stretch:", round(forecast(ost, ap, ops).close.min()))
cmp.round(0)
```

**SAY:**

> 🖱️ I'm pointing at the first lines of cell six, prepared before recording: suppliers stretched within their contracts, discretionary spend removed, and Northwind paid on time.

> 🖱️ I'm pointing at the alts dictionary: the same engine run once per alternative, so they're comparable.

> 🖱️ I'm pointing at the ost and ops lines: a stress case where Northwind pays two more weeks late, continuing its trend.

> 🖱️ I'm clicking the Run button on the left of cell six.

> 🖱️ I'm pointing at the revolver row of the table under cell six: trough 517,662, at about 3,000 dollars of interest.

> 🟢 It barely clears the minimum and uses all the capacity, with nothing left for a bad week.

> 🖱️ I'm pointing at the accelerate row: the biggest gain, 381,173.

> 🟢 But it assumes Northwind pays on time again, and the last 90 days say otherwise. It stays out of the plan.

> 🖱️ I'm pointing at the defer and stretch rows.

> 🟢 Deferring capex and marketing adds 161,000 at the trough at no cost. Stretching adds only 9,735, because 62% of payables are with critical suppliers.

> 🖱️ I'm pointing at the stress line above the table: with defer and stretch, the stressed trough is 281,527; without stretch, 262,466.

> 🟢 That small stretch matters: it's 19,000 dollars less I'd have to borrow.

**WHY:** cada palanca se mide con el mismo motor y la misma métrica (el piso y las semanas bajo el mínimo). Una alternativa vale por su efecto en el **peor momento**, no en el total. Acelerar cobros es la más grande en papel, pero depende de la conducta del cliente, que la evidencia contradice.

**EXPECTED RESULT:**

`stress: Northwind 14 more days late, with defer + stretch | trough: 281527 in week 11 | without stretch: 262466`

| alternativa | trough | weeks_below_min | week13 | gain_at_trough | cost |
| ----------- | ------ | --------------- | ------ | -------------- | ---- |
| base | 289,365 | 7 | 385,100 | 0 | 0 |
| revolver | 517,662 | 0 | 620,100 | 228,297 | 3,005 |
| accelerate | 670,538 | 0 | 769,400 | 381,173 | 0 |
| defer | 450,365 | 3 | 564,100 | 161,000 | 0 |
| stretch | 299,100 | 6 | 385,100 | 9,735 | 0 |
| defer+stretch | 469,100 | 2 | 564,100 | 179,735 | 0 |

**DECISION:**

- **Revolver solo:** descartado. Pasa el caso base por $17,662, pero usa toda la capacidad y no deja margen para el estrés.
- **Acelerar a Northwind:** descartado como base del plan. No hay evidencia: su mora subió a 26,5 días. Queda como acción de cobranza (upside).
- **Postergar discrecionales:** aceptado. Gratis, +$161,000 en el piso.
- **Estirar proveedores no críticos:** aceptado. Chico en la base, pero baja $19,061 lo que hay que girar bajo estrés, y respeta `max_extension_days`.

📘 **What each line does** (para vos, no se lee):

- `ap2 = ap.assign(due_date=... + max_extension_days)`: bills moved by the extension each supplier allows (0 for critical ones).
- `op2 = op[op.discretionary.eq("N")]`: the forecast without discretionary spend (deferred past week 13).
- `o2 = o.assign(expected=...)`: Northwind's open invoices collected on their due dates.
- `op3 = op.assign(week=...)`: Northwind's new-sales collections back at management's original weeks.
- `alts = {...}`: one forecast per alternative; the revolver one draws the full capacity in the first breach week.
- `cmp = pd.DataFrame({...}).T`: trough, weeks below the minimum and week 13 per alternative.
- `cmp["gain_at_trough"] = ...`: improvement at the trough vs. base.
- `cmp["cost"] = 0.0` / `cmp.loc["revolver", "cost"] = ...`: interest on the draw until week 13.
- `ost = o.assign(expected=... + 14 days for the top customer)`: stress on open invoices.
- `ops = op2.assign(week=... + 2 weeks for the top customer)`: stress on new-sales collections.
- `spre = forecast(ost, ap2, ops)`: stressed case with defer + stretch, before any draw.
- `print("stress: ...")`: stressed trough with and without the stretch.
- `cmp.round(0)`: shows the comparison.

---

### Bloque 7. Phase 5 — Plan elegido y estrés

**TIME:** 15:15–18:50 (3:35)

**WHAT I DO:** clic en la celda 7 → tipear 4 tramos → Run → señalar los cinco valores.

**WHERE:** celda 7, vacía, debajo de la tabla de alternativas.

**SAY:**

> 🖱️ I'm clicking inside cell seven, the empty cell below the comparison table.

> 🟢 Phase five: free levers first; the revolver covers the rest, sized to the stress case, because the base case got us here.

> 🗣️⌨️ First line of cell seven: the first week the stressed case drops below the minimum. That's when I draw.

```python
w = (spre.close < MIN).idxmax()
```
*(31 caracteres · ~14 s)*

> 🗣️⌨️ Next line: the draw closes the stressed gap, rounded up to 25,000, the way draws are requested.

```python
draw = np.ceil((MIN - spre.close.min()) / 25000) * 25000
```
*(56 caracteres · ~25 s)*

> 🗣️⌨️ Next two lines of cell seven: the plan with that draw, and the same plan under stress.

```python
plan = forecast(o, ap2, op2, {w: draw})
stress = forecast(ost, ap2, ops, {w: draw})
```
*(83 caracteres · ~37 s)*

> 🗣️⌨️ Last line: the week, the draw, whether it fits the real capacity, and the plan and stress troughs.

```python
print(w, draw, draw <= cap, plan.close.min().round(), stress.close.min().round())
```
*(81 caracteres · ~36 s)*

> 🖱️ I'm clicking the Run button on the left of cell seven.

> 🖱️ I'm pointing at the printed line under cell seven: week 7, 225,000, True.

> 🟢 A 225,000 draw in week 7 fits inside the 235,000 of real capacity. Without the supplier stretch, it would be 250,000, and that breaks the leverage limit.

> 🖱️ I'm pointing at the last two numbers: 676,024 and 506,527.

> 🟢 The plan never drops below 676,000, and under stress cash stays above 500,000 every week.

**WHY:** las palancas sin costo van primero; la deuda cubre solo el resto. Dimensionar el giro con el caso estresado da colchón real, y el chequeo `draw <= cap` prueba que el plan cumple compromiso, borrowing base y covenant al mismo tiempo.

**EXPECTED RESULT:** `7 225000.0 True 676024.0 506527.0`

**DECISION:** ¿girar lo justo para la base o para el estrés? **Para el estrés**: $225,000 en la semana 7. Es viable porque está debajo de $235,000. Sin el estiramiento de proveedores harían falta $250,000, que no es viable.

📘 **What each line does** (para vos, no se lee):

- `w = (spre.close < MIN).idxmax()`: first week the stressed case is below the minimum (`idxmax` returns the first `True`).
- `draw = np.ceil((MIN - spre.close.min()) / 25000) * 25000`: the stressed shortfall, rounded up to 25,000.
- `plan = forecast(o, ap2, op2, {w: draw})`: base inputs with defer, stretch and the draw.
- `stress = forecast(ost, ap2, ops, {w: draw})`: the same plan under the Northwind stress.
- `print(...)`: draw week, amount, whether it fits the capacity, and both troughs.

---

### Bloque 8. Phase 5 — Exportación y registro de decisiones

**TIME:** 18:50–20:25 (1:35)

**WHAT I DO:** señalar las líneas de la celda 8 → Run → señalar el registro y el gráfico → abrir Files → cerrar Files.

**WHERE:** celda 8 (armada), debajo de la salida de la celda 7. Ícono de carpeta en la barra lateral izquierda.

**Celda 8 (armada antes de grabar):**

```python
ar["expected_date"] = o.expected
ar["in_forecast"] = ar.index.isin(o[o.collect].index)
b.to_csv("bank_transactions.csv", index=False)
ar.to_csv("accounts_receivable.csv", index=False)
ap.assign(due_date_raw=ap.due_date, due_date=ap2.due_date).to_csv("accounts_payable.csv", index=False)
op.assign(deferred=op.discretionary.eq("Y")).to_csv("operating_forecast.csv", index=False)
pd.concat({"base": base, "plan": plan, "stress": stress}, names=["scenario", "week"]).round(2).to_csv("liquidity_forecast_13w.csv")
cmp.round(2).to_csv("scenario_comparison.csv")
log = pd.DataFrame({"action": ["defer discretionary spend", "stretch non-critical suppliers", f"revolver draw in week {w}", f"accelerate {top}", "revolver alone"],
                    "decision": ["accepted", "accepted", "accepted", "rejected", "rejected"],
                    "usd": [-op[op.discretionary.eq("Y")].amount.sum(), ap.amount[ap.max_extension_days > 0].sum(), draw, cmp.gain_at_trough["accelerate"], cap],
                    "basis": ["capex and marketing moved past week 13, no cost", "only non-critical bills, within agreed max_extension_days", f"sized to the stress case, below real capacity {cap:,.0f}",
                              f"recent delay {delay[top]} days, no evidence it reverses", "uses all capacity, no buffer for stress"]})
log.to_csv("financing_plan.csv", index=False)
print(log, "\nleverage after draw:", round((debt.drawn.sum() + draw) / r.ltm_ebitda, 2), "| unused capacity:", cap - draw, "| interest cost:", round(draw * r.interest_rate * (14 - w) / 52))
ax = pd.DataFrame({"base": base.close, "plan": plan.close, "stress": stress.close}).plot(marker="o", title="Unrestricted cash, 13 weeks")
ax.axhline(MIN, color="red", ls="--")
```

**SAY:**

> 🖱️ I'm pointing at the to_csv lines of cell eight, prepared before recording: the five inputs rewritten with original values kept, plus the outputs.

> 🖱️ I'm pointing at the log table in cell eight: each action, accepted or rejected, with its dollars and the reason.

> 🖱️ I'm clicking the Run button on the left of cell eight.

> 🖱️ I'm pointing at the line under the log: leverage 3.49, 10,000 of capacity left, about 2,900 of interest.

> 🟢 Every limit holds, with a thin margin.

> 🖱️ I'm pointing at the chart under cell eight: the blue base falls below the red minimum; the orange plan and green stress stay above.

> 🖱️ I'm clicking the folder icon in the left sidebar, to open the Files panel.

> 🖱️ I'm pointing at liquidity_forecast_13w, scenario_comparison and financing_plan, the three new files.

> 🖱️ I'm clicking the folder icon again to close the panel.

**WHY:** el modelo tiene que ser auditable: cada ajuste queda en el archivo junto a su valor original, y cada decisión con su número y su razón. Reescribir los archivos de entrada cumple el criterio de Slack; los originales quedan en el Escritorio y en `original/` del ZIP.

**EXPECTED RESULT:**

| action | decision | usd | basis |
| ------ | -------- | --- | ----- |
| defer discretionary spend | accepted | 179,000.00 | capex and marketing moved past week 13, no cost |
| stretch non-critical suppliers | accepted | 332,025.46 | only non-critical bills, within agreed max_extension_days |
| revolver draw in week 7 | accepted | 225,000.00 | sized to the stress case, below real capacity 235,000 |
| accelerate Northwind Retail | rejected | 381,173.41 | recent delay 26.5 days, no evidence it reverses |
| revolver alone | rejected | 235,000.00 | uses all capacity, no buffer for stress |

`leverage after draw: 3.49 | unused capacity: 10000.0 | interest cost: 2877`

El gráfico: la línea azul (base) por debajo de la roja punteada (500,000) de la semana 7 a la 13; la naranja (plan) y la verde (estrés) siempre por encima. El piso verde está en la semana 11.

En Files: los cinco CSV reescritos, más `liquidity_forecast_13w.csv` (39 filas), `scenario_comparison.csv` (6 filas) y `financing_plan.csv` (5 filas). Si no aparecen, decí: *"I'm clicking refresh at the top of the Files panel, to show the new files."*

📘 **What each line does** (para vos, no se lee):

- `ar["expected_date"] = o.expected`: expected collection date on each open invoice.
- `ar["in_forecast"] = ...`: whether the invoice is counted in the forecast.
- `b.to_csv(...)`: bank file with the `dup` flag.
- `ar.to_csv(...)`: receivables with `status_raw`, `days_late`, `expected_date` and `in_forecast`.
- `ap.assign(due_date_raw=..., due_date=ap2.due_date).to_csv(...)`: payables with the stretched date and the original one.
- `op.assign(deferred=...).to_csv(...)`: the operating forecast with `week_raw` and the deferred flag.
- `pd.concat({...}).to_csv("liquidity_forecast_13w.csv")`: the weekly model for base, plan and stress.
- `cmp.round(2).to_csv("scenario_comparison.csv")`: the alternatives table.
- `log = pd.DataFrame({...})`: the decision log, with action, decision, dollars and basis.
- `log.to_csv("financing_plan.csv", index=False)`: saves it.
- `print(log, ...)`: the log, leverage after the draw, capacity left and interest cost.
- `ax = pd.DataFrame({...}).plot(...)`: closing cash per week for the three scenarios.
- `ax.axhline(MIN, ...)`: the 500,000 minimum as a red dashed line.

---

### Bloque 9. Conclusiones

**TIME:** 20:25–22:45 (2:20)

**WHAT I DO:** + Text → tipear 3 tramos → clic afuera → Cmd + S.

**WHERE:** botón **+ Text** arriba a la izquierda de la barra de Colab (agrega la celda al final, porque la celda 8 está seleccionada).

**SAY:**

> 🖱️ I'm clicking plus Text at the top left, to add a text cell at the end of the notebook for the conclusions.

> 🗣️⌨️ In the text cell: the title, and the problem with the real capacity.

```markdown
## Financing plan
- Free cash $716,256; trough $289,365 in week 9; real capacity $235,000.
```
*(91 caracteres · en dos tramos: el título + Enter (~8 s), y la viñeta (~33 s))*

> 🗣️⌨️ Next line of the text cell: the plan and its stress result.

```markdown
- Defer $179,000, stretch, draw $225,000 in week 7: stress trough $506,527.
```
*(75 caracteres · ~33 s)*

> 🗣️⌨️ Last line: the AI declaration.

```markdown
- Input files generated with AI.
```
*(32 caracteres · ~14 s)*

> 🖱️ I'm clicking on the empty area below the text cell, to show it formatted.

> 🖱️ I'm pressing Command and S to save the notebook; the save message appears at the bottom left.

**EXPECTED RESULT:** la celda de texto con el título y tres viñetas, formateada.

---

### Bloque 10. Epilogue

**TIME:** 22:45–23:40 (0:55)

**WHAT I DO:** scroll lento hacia arriba, sin tipear. Recién **después** abrís TaskRecorder para detener la grabación.

**WHERE:** Colab, desde las conclusiones hasta la celda 1.

**SAY:**

> 🖱️ I'm scrolling up slowly through the notebook, from the conclusions back to cell one.

> 🟢 The key decisions: free cash, not the bank total; Northwind's recent behavior, not its history; and credit as the tightest of three limits.

> 🟢 The plan defers 179,000, stretches non-critical suppliers and draws 225,000 in week 7, and it survives the stress.

> 🟢 Open risks: 10,000 of capacity left, Northwind at 45% of receivables, and capex returning after week 13. Next, I'd escalate Northwind's collections. Thanks for watching!

**WHY:** no repite los pasos: cuenta las decisiones, cómo se validaron y qué queda abierto.

---

## Si algo sale mal

| Error | Qué decís y hacés |
| ----- | ----------------- |
| Un nombre mal escrito | 🖱️ *"There's a typo in cell N. I'm clicking on that line to fix it, and running the cell again."* |
| `NameError` | 🖱️ *"An earlier cell didn't run. I'm opening the Runtime menu at the top and choosing Run before."* |
| **La celda 3 se ejecutó dos veces** | Corre las semanas de cobro dos veces. Decí: *"I ran cell three twice, which shifts the collections again. I'm opening the Runtime menu and choosing Run before, to reload the files from cell one."* |
| Hay que repetir algo después de la celda 8 | 🖱️ *"The inputs were already rewritten, so I'm uploading the originals from my Desktop again in the Files panel."* |
| Los números de la celda 7 no coinciden | Revisá que en la celda 7 diga `ap2` y `op2` (no `ap` y `op`). |

---

## Checklist de archivos y preparación previa

- [ ] Practicá dos veces con cronómetro. [liquidity_forecast.ipynb](liquidity_forecast.ipynb) tiene el código completo para comparar.
- [ ] En Colab, creá el notebook **liquidity_forecast** con **8 celdas de código**:
  - celda **1**: ya escrita (carga y contratos);
  - celdas **3, 4, 6 y 8**: pegá el código de cada bloque;
  - celdas **2, 5 y 7**: vacías;
  - **no ejecutes nada.**
- [ ] En **Files**, subí los cinco CSV de esta carpeta: `bank_transactions`, `accounts_receivable`, `accounts_payable`, `debt_facilities` y `operating_forecast`. Los de la carpeta son los originales: no los toques.
- [ ] **Tools → Settings → AI assistance**: ocultá las funciones de IA.
- [ ] **Tools → Settings → Editor**: si está la opción, desactivá las sugerencias automáticas de código.
- [ ] Zoom (`Cmd + +`). Firefox con la ventana 1 en la descripción de la tarea y la ventana 2 en Colab.

## Checklist de resultados que deben quedar generados

- [ ] `cash0` = 716,256 (celda 2).
- [ ] La factura INV-10300 reabierta como `returned` (celda 3).
- [ ] La tabla semanal `base`, con el piso de 289,365 en la semana 9 (celda 4).
- [ ] La capacidad real `cap` = 235,000 (celda 5).
- [ ] La tabla `cmp` de seis escenarios (celda 6).
- [ ] `plan` y `stress`: giro de 225,000 en la semana 7, pisos de 676,024 y 506,527 (celda 7).
- [ ] Ocho CSV en Files: los cinco reescritos, `liquidity_forecast_13w.csv`, `scenario_comparison.csv` y `financing_plan.csv`, más el gráfico (celda 8).
- [ ] La celda de conclusiones y el notebook guardado.
- [ ] Después: descargá el `.ipynb` y los 8 CSV. Armá **Deliverables.zip** con todo eso y la carpeta `original/` con los cinco CSV de esta carpeta. Marcá en Studio la opción de archivos generados con IA.

## Checklist de decisiones financieras que debo explicar

- [ ] **Caja de partida:** sin duplicados, neta de cheques emitidos, sin la reserva restringida ($716,256, no $1.36M).
- [ ] **El cobro devuelto:** el AR decía `paid`, el banco lo devolvió; se reabre y no se proyecta.
- [ ] **Mora reciente vs. histórica:** 26,5 vs. 6 días para Northwind; se usa la reciente.
- [ ] **Exclusiones:** lo disputado, lo devuelto y lo vencido hace más de 90 días no se proyecta ($83,002).
- [ ] **Temporal vs. estructural:** es capital de trabajo, no pérdida operativa (+$43,000 por semana al final), pero dura más que la ventana → financiación comprometida.
- [ ] **Capacidad real:** el mínimo de tres límites; manda el apalancamiento ($235,000 de $450,000).
- [ ] **Por qué no el revolver solo:** usa toda la capacidad y no deja margen para el estrés.
- [ ] **Por qué no acelerar a Northwind:** la evidencia muestra lo contrario.
- [ ] **Por qué estirar proveedores aunque gane poco:** baja el giro bajo estrés de $250,000 (no viable) a $225,000 (viable).
- [ ] **Por qué dimensionar con el estrés:** la base es lo que llevó a la empresa a esta situación.
- [ ] **Riesgos pendientes:** $10,000 de capacidad libre, concentración del 45% en Northwind, el capex vuelve después de la semana 13.

---

## Conclusión para cerrar la grabación (en inglés)

> The company looked like it had 1.36 million dollars in the bank, but only 716,000 is free cash. With Northwind paying later, it drops below the 500,000 minimum from week 7 and bottoms out at 289,000 in week 9. The revolver can't fix that alone: the leverage covenant caps new debt at 235,000. So the plan defers 179,000 of discretionary spend, stretches only non-critical suppliers within their agreed terms, and draws 225,000 in week 7. Cash stays above the minimum every week, even if Northwind pays two more weeks late. What's left to watch is the thin 10,000 of capacity and Northwind's concentration.

*(Es la versión larga del epilogue. Si te sobra tiempo, podés decirla en lugar de las tres 🟢 del bloque 10; si no, las 🟢 alcanzan.)*

---

## Pendientes antes de grabar

| Tema | Qué hacer |
| ---- | --------- |
| **Descripción de TaskRecorder y Metadata** | Abajo hay una propuesta que coincide con este guion. Pegala o pasame los campos reales para ajustarla. |
| **Origen de los CSV** | Los generé yo, Claude, con [_generador/generate_data.py](_generador/generate_data.py). Decí "generated with AI" y marcá en Studio la opción de archivos generados con IA. |
| **Carpeta `_generador/`** | Tiene el generador, el código de las celdas y el script que lo ejecuta. No va en la entrega. |

**Descripción (propuesta):**

> Rebuild the 13-week liquidity position of a simulated mid-sized company in Google Colab with pandas. I reconcile bank transactions to find free cash, reopen a returned customer payment, adjust collections to each customer's recent payment delays, and build a weekly forecast that shows when cash drops below the 500,000 minimum. I calculate real revolver capacity from the borrowing base and the leverage covenant, compare four funding levers, choose a combination sized to a stress case, and export the rewritten inputs, the weekly model, the scenario comparison and a decision log.
