# yfmhc0c0 — 13-Week Liquidity Assessment

Guion para grabar la tarea **yfmhc0c0** en **Google Colab** (app principal), con **Firefox** como app de apoyo, en una sola toma.

> **Goal:** *Reconstruct and stress-test the 13-week liquidity position of a simulated mid-sized company facing tightening cash availability, customer payment delays, and upcoming debt obligations. Deliver an auditable weekly liquidity model, scenario comparisons, and a justified financing action plan that maintains minimum cash requirements while respecting contractual borrowing limits.*

**Duración estimada: ~29:29, con 35% de tipeo** (tipeando a 135 car./min; ya cuenta los números leídos en palabras). Límite absoluto: 30:00. Si tipeás a 120 car./min da ~30:45 y 37%: practicá hasta tipear cada tramo en el tiempo indicado.

**Punto de partida al grabar:** el notebook **liquidity_assessment** tiene la **celda 1 ya escrita** y los cinco CSV ya están subidos en el panel **Files** de Colab. La celda 1 es solo preparación: librerías, lectura de los CSV, la fecha de la semana 1, la fila del revolver, dos fórmulas auxiliares (semana y caja de cierre) y la función `export()`. **Todo lo demás se tipea en vivo** (celdas 2 a 7). En el video se dice que la celda 1 estaba escrita y por qué.

**Reglas que cumple (iguales a las otras tareas):**

- **Ningún CSV de entrada se sobrescribe.** Los cinco entregables tienen nombres nuevos.
- Cada acción del mouse tiene su frase 🖱️ con qué, dónde y por qué.
- Nunca se habla y se tipea a la vez; ningún tramo de tipeo pasa de 45 s.
- Máximo 30 min y tipeo ≤35%.

---

## Cronograma

| # | Bloque | Fase | Celda | TIME | Duración |
| - | ------ | ---- | ----- | ---- | -------- |
| 0 | Opening | — | — | 0:00–1:39 | 1:39 |
| 1 | Celda 1: carga y contratos | 1. Data reconstruction | 1 | 1:39–4:06 | 2:26 |
| 2 | Phase 1: caja libre real | 1. Data reconstruction | 2 | 4:06–6:38 | 2:32 |
| 3 | Phase 2: confiabilidad de los cobros | 2. Cash flow reliability | 3 | 6:38–9:13 | 2:35 |
| 4 | Phase 3: forecast de 13 semanas | 3. 13-week forecast | 4 | 9:13–14:37 | 5:24 |
| 5 | Phase 4: capacidad real de endeudamiento | 4. Financing alternatives | 5 | 14:37–19:03 | 4:26 |
| 6 | Phase 4–5: estrategias y estrés | 4–5. Strategies and stress | 6 | 19:03–24:24 | 5:20 |
| 7 | Phase 5: validación, exportación y archivos | 5. Validation | 7 | 24:24–28:01 | 3:38 |
| 8 | Epilogue | — | — | 28:01–29:29 | 1:27 |
| | **Total** | | | | **~29:29** |

*(Calculado con 130 palabras/min de narración, 135 caracteres/min de tipeo en silencio, todo sumado, más ~20 s de navegación y ejecución por bloque.)*

---

## Archivos

**Input files** (sintéticos, generados con IA antes de grabar; fecha de corte viernes 2026-11-20, semana 1 = lunes 2026-11-23):

| Archivo | Filas | Columnas clave | Qué tiene |
| ------- | ----- | -------------- | --------- |
| `bank_transactions.csv` | 163 | `txn_id, date, account_id, account_type, description, reference, amount, status` | 5 filas duplicadas ($202,453 de caja inflada); 3 cheques emitidos sin compensar (−$64,150); una cuenta restringida (reserva de deuda, $381,900) |
| `accounts_receivable.csv` | 456 | `invoice_id, customer, invoice_date, due_date, amount, status, paid_date` | Historial pagado desde marzo, 69 facturas abiertas ($2,025,511) y 2 en disputa ($47,767). Northwind es el 46% de lo abierto y paga con 26,5 días de mora |
| `accounts_payable.csv` | 46 | `bill_id, vendor, category, bill_date, due_date, amount, critical, max_extension_days` | El 62% es con proveedores críticos (0 días de extensión); el resto acepta 21 o 28 días |
| `debt_facilities.csv` | 3 | `facility_id, commitment, drawn, interest_rate, …, advance_rate, reserve, min_unrestricted_cash, max_leverage, ltm_ebitda` | Revolver de $1,200,000 (usado $750,000), term loan y préstamo de equipos. Caja mínima $500,000, apalancamiento máximo 3.5x |
| `operating_forecast.csv` | 65 | `week, week_start, category, customer, amount, discretionary` | La gerencia proyecta los cobros de ventas nuevas sin mora; $179,000 de gasto discrecional; servicio de deuda de las tres líneas |

**Output files** (los genera el notebook con `export()` en la celda 7):

| Archivo | Qué contiene | Se calcula en |
| ------- | ------------ | ------------- |
| `reconciled_cash_position.csv` | Caja por tipo de cuenta y estado, sin duplicados | Celda 2 |
| `13_week_liquidity_forecast.csv` | Por semana: salidas, entradas y caja de cierre | Celda 4 |
| `borrowing_base_analysis.csv` | AR elegible, base de préstamo, margen del compromiso y del covenant | Celda 5 |
| `scenario_comparison.csv` | Caja de cierre semanal de los seis escenarios | Celda 6 |
| `liquidity_risk_report.csv` | Giro recomendado y apalancamiento resultante | Celda 7 |

Y el notebook: **`liquidity_assessment.ipynb`**.

**Dónde está cada restricción del Goal:** todas en la fila `RCF-01` de `debt_facilities.csv`: `min_unrestricted_cash` (500,000), `commitment` (1,200,000), `max_leverage` (3.5) con `ltm_ebitda`, y `advance_rate`, `reserve` y `drawn` para la base de préstamo.

**Supuesto documentado:** el archivo no trae límite de concentración. Northwind es el 46% del AR abierto, así que se aplica un **tope de 25% por cliente**, un criterio estándar de los préstamos respaldados por cuentas a cobrar. Se dice en voz alta. No cambia la capacidad final, porque el límite que manda es el del apalancamiento.

**Cómo cubre cada fase del prompt:**

| Fase | Celdas | Qué produce |
| ---- | ------ | ----------- |
| 1. Financial data reconstruction | 1, 2 | Duplicados detectados; caja libre de $525,938 (sin duplicados, con cheques pendientes, sin la cuenta restringida) |
| 2. Cash flow reliability | 3 | Mora mediana de los últimos 90 días por cliente: Northwind 26,5 días |
| 3. 13-week forecast | 4 | Entradas, salidas y cierre por semana. Debajo del mínimo desde la semana 1; piso de $301,347 en la semana 9 (déficit de $198,653) |
| 4. Financing alternatives | 5, 6 | Capacidad real $235,000 (manda el covenant). Seis escenarios comparados |
| 5. Mitigation and validation | 6, 7 | Plan combinado: postergar, estirar y girar $225,000. Mínimo $710,707; con estrés $518,909; apalancamiento 3.49x. Los cinco CSV exportados |

**Los números que tenés que tener claros:**

| Escenario | Caja mínima en 13 semanas | ¿Cumple $500k? | Decisión |
| --------- | ------------------------- | -------------- | -------- |
| `base` (no hacer nada) | $301,347 | No | Hay que actuar |
| `credit` (girar toda la capacidad, $235k) | $536,347 | Sí | Rechazado: no aguanta el estrés |
| `credit_stress` (lo mismo con Northwind 2 semanas más tarde) | $348,449 | No | Prueba del rechazo |
| `levers` (postergar discrecional + estirar proveedores no críticos) | $485,707 | No | Rechazado: no alcanza solo |
| `combined` (palancas + giro de $225k) | $710,707 | Sí | **Elegido** |
| `stress` (combinado con Northwind 2 semanas más tarde) | $518,909 | Sí | El plan aguanta |

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
- **VERIFY BEFORE CONTINUING:** qué controlar antes de pasar al bloque siguiente.
- 📘 = qué hace cada línea, en inglés. Es para vos: **no se lee**.

---

## Estrategia de tiempo y tipeo

| | Cantidad | Tiempo |
| - | -------- | ------ |
| Tipeo en vivo (celdas 2 a 7) | 1.380 caracteres | ~10,2 min a 135 car./min (~11,5 a 120) |
| Narración | ~2.113 palabras | ~16,3 min |
| Navegación y ejecución | 9 bloques | ~3,0 min |
| **Total** | | **~29:29** (~30:45 si tipeás a 120 car./min) |

**Tipeo: ~35% del video a 135 car./min** (~37% a 120).

**Reglas de tipeo:**

1. **Nunca hablar y tipear al mismo tiempo.** Frase 🗣️⌨️ con las manos quietas → bloque en silencio.
2. **Ningún tramo pasa de 45 segundos.** Las líneas largas de las celdas 4, 5 y 6 se tipean en dos tramos, **sin Enter** entre ellos.
3. **Nada de tipeo extra:** ni comentarios ni `print` de prueba.
4. **Sin autocompletado.** Si aparece una caja de sugerencias, Escape.
5. **Comillas y corchetes:** si Colab cierra solo `"`, `(`, `[` o `{`, seguí tipeando igual: al escribir el de cierre, Colab lo salta.

---

## La regla del mouse y del teclado

1. El mouse **solo se mueve con una frase 🖱️**. Mientras tipeás, soltalo.
2. Al terminar una acción, el cursor queda **quieto en el margen derecho**.
3. **Primero la frase, después el movimiento o el tipeo.**
4. **Repetí el número de celda al menos una vez por minuto.** Las frases ya lo hacen.
5. Para agregar una celda: **+ Code**, arriba a la izquierda de la barra de Colab, debajo del menú.
6. Frases comodín:
   - *"I'm scrolling down inside the output of cell N, to see the last rows."*
   - *"I'm clicking at the end of line N in cell N, to fix a typo."*
   - *"I'm pressing Escape to close the suggestion box, because I type everything by hand."*
   - *"I'm waiting for cell N to finish; the spinner on its left is still running."*

---

## Guion de grabación

### Bloque 0. Opening

**TIME:** 0:00–1:39 (1:39)

**WHAT I DO:** hablar con la descripción de la tarea en pantalla → minimizar → abrir Colab desde el Dock → abrir el panel Files.

**WHERE:** Firefox ventana 1 (descripción). Botón amarillo arriba a la izquierda. Ícono de Firefox en el Dock, a la derecha (Mac); segunda ventana de la lista. Ícono de carpeta en la barra lateral izquierda de Colab.

**SAY:**

> 🟢 I will be beginning my task soon. A mid-sized company is running short of cash: customers pay late, and debt payments are coming. I'm building its 13-week (thirteen-week) liquidity forecast, and a financing plan that keeps 500 (five hundred) thousand dollars of free cash without breaking its loan limits.

> 🟢 The constraints: a 1.2 (one point two) million dollar revolver, but only what the borrowing base and a 3.5 (three point five) times leverage covenant allow. I'll deliver five CSV files: cash position, forecast, borrowing base, scenarios, and a risk report.

> 🖱️ I'm clicking the yellow minimize button at the top left, to hide the task description.

> 🖱️ I'm clicking the Firefox icon in the Dock on the right, and choosing the second window: my Colab notebook, liquidity assessment.

> 🖱️ I'm clicking the folder icon in Colab's left sidebar, to open the Files panel and show my inputs.

> 🖱️ I'm pointing at the five CSV files in the Files panel: bank transactions, receivables, payables, debt facilities and the operating forecast. They're synthetic, generated with AI, and I never overwrite them.

**WHY:** en menos de un minuto y medio el revisor ve el objetivo, las restricciones del contrato, los cinco inputs y los cinco entregables.

**EXPECTED RESULT:** el notebook con la celda 1 escrita (sin ejecutar) y el panel Files abierto con los cinco CSV.

**VERIFY BEFORE CONTINUING:** están los cinco archivos y no hay ningún otro CSV en Files.

---

### Bloque 1. Celda 1: carga y contratos

**TIME:** 1:39–4:06 (2:26)

**WHAT I DO:** señalar cada grupo de líneas de la celda 1 (ya escrita) → Run → señalar la salida.

**WHERE:** celda 1, la única del notebook, a la derecha del panel Files. Botón Run (triángulo) a la izquierda de la celda.

**Celda 1 (ya escrita antes de grabar, no se tipea):**

```python
import pandas as pd
import numpy as np
b = pd.read_csv("bank_transactions.csv", parse_dates=["date"])
ar = pd.read_csv("accounts_receivable.csv", parse_dates=["invoice_date", "due_date", "paid_date"])
ap = pd.read_csv("accounts_payable.csv", parse_dates=["bill_date", "due_date"])
debt = pd.read_csv("debt_facilities.csv")
op = pd.read_csv("operating_forecast.csv")
W1 = pd.Timestamp("2026-11-23")
r = debt.iloc[0]
W = lambda s: (s - W1).dt.days.clip(0) // 7 + 1
c = lambda x: cash0 + x.groupby("week").amount.sum().loc[:13].cumsum()

def export():
    pos.round(2).to_csv("reconciled_cash_position.csv")
    fc.rename(int).round(2).to_csv("13_week_liquidity_forecast.csv")
    bba.round(2).rename("amount").to_csv("borrowing_base_analysis.csv")
    t.rename(int).round(2).to_csv("scenario_comparison.csv")
    k.round(4).rename("value").to_csv("liquidity_risk_report.csv")

for n, d in {"bank": b, "ar": ar, "ap": ap, "debt": debt, "op": op}.items():
    print(n, d.shape, "| duplicate rows:", d.duplicated().sum())
debt.set_index("facility_id").T
```

**SAY:**

> 🖱️ I'm pointing at cell one, at the top of the notebook. I wrote it before recording because it's only setup: libraries, the five files, and two small helpers. Every financial decision after it I type live.

> 🖱️ I'm pointing at the five read_csv lines: bank, receivables, payables, debt and the operating forecast, with their dates parsed.

> 🖱️ I'm pointing at W1 (W one), the Monday of week one, and r, the revolver's row in the debt file.

> 🖱️ I'm pointing at the two helpers below. W turns a date into a forecast week; past-due items fall into week one. c turns any set of flows into weekly closing cash, starting from the opening cash I'll calculate in cell two.

> 🖱️ I'm pointing at the export function. It writes my five deliverables at the end, all with new names, so the inputs stay untouched.

> 🖱️ I'm clicking the Run button on the left of cell one.

> 🖱️ I'm pointing at the bank line under cell one: 163 (one hundred sixty-three) rows and 5 (five) duplicate rows.

> 🖱️ I'm pointing at the other four lines: receivables, payables, debt and the operating forecast have no duplicate rows.

> 🖱️ I'm pointing at the RCF-01 (R C F zero one) column of the debt table, below the counts.

> 🟢 The revolver has a 1.2 (one point two) million commitment, 750 (seven hundred fifty) thousand already drawn, an 80 (eighty) percent advance rate and a 150 (one hundred fifty) thousand reserve. The covenant is 3.5 (three point five) times leverage on 1.07 (one point zero seven) million of EBITDA, and the minimum cash is 500 (five hundred) thousand.

> 🖱️ I'm pointing at the term loan column: a 168 (one hundred sixty-eight) thousand dollar payment in January, inside my 13 (thirteen) weeks.

**WHY:** el revisor ve de dónde sale cada restricción: todas están en `debt_facilities.csv`, no inventadas.

**EXPECTED RESULT:**

- `bank (163, 8) | duplicate rows: 5`; los otros cuatro con `duplicate rows: 0`.
- La tabla de deuda: `RCF-01` con `commitment 1200000`, `drawn 750000`, `advance_rate 0.8`, `reserve 150000.0`, `min_unrestricted_cash 500000.0`, `max_leverage 3.5`, `ltm_ebitda 1070000.0`. `TL-01` con `scheduled_payment 168000` y `next_payment_date 2027-01-15`.

**VERIFY BEFORE CONTINUING:** los cinco archivos cargaron (cinco líneas impresas) y aparece la tabla de deuda.

📘 **What each line does** (para vos, no se lee):

- `import pandas as pd` / `import numpy as np`: libraries.
- `b = ...`, `ar = ...`, `ap = ...`, `debt = ...`, `op = ...`: the five inputs, with dates parsed.
- `W1 = pd.Timestamp("2026-11-23")`: Monday of forecast week 1.
- `r = debt.iloc[0]`: the revolver row (RCF-01).
- `W = lambda s: (s - W1).dt.days.clip(0) // 7 + 1`: date → week number; anything already due lands in week 1.
- `c = lambda x: cash0 + x.groupby("week").amount.sum().loc[:13].cumsum()`: weekly closing cash for weeks 1–13 from opening cash `cash0` (defined in cell 2).
- `def export(): ...`: writes the five deliverables; it runs only when cell 7 calls it.
- `for n, d in {...}.items(): print(...)`: shape and exact duplicate rows of each file.
- `debt.set_index("facility_id").T`: debt facilities, one column per facility.

---

### Bloque 2. Phase 1: caja libre real

**TIME:** 4:06–6:38 (2:32)

**WHAT I DO:** + Code → tipear 2 tramos → Run → señalar las tres filas.

**WHERE:** botón **+ Code** arriba a la izquierda; la celda 2 aparece debajo de la salida de la celda 1.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell two below the output of cell one.

> 🗣️⌨️ First line of cell two: the reconciled cash position. I drop the duplicated transaction IDs, then add up by account type and status.

```python
pos = b.drop_duplicates("txn_id").groupby(["account_type", "status"]).amount.sum()
```
*(82 caracteres · ~36 s)*

> 🗣️⌨️ Next lines of cell two: opening cash is the operating accounts only, cleared and pending. Then I show the position.

```python
cash0 = pos["operating"].sum()
pos
```
*(34 caracteres · ~15 s)*

> 🖱️ I'm clicking the Run button on the left of cell two.

> 🖱️ I'm pointing at operating cleared under cell two: about 590 (five hundred ninety) thousand dollars.

> 🟢 The raw bank file says about 793 (seven hundred ninety-three) thousand. The about 202 (two hundred two) thousand difference was the duplicated transactions.

> 🖱️ I'm pointing at operating pending: minus about 64 (sixty-four) thousand.

> 🟢 Those are checks I already issued. The money is gone even if the bank hasn't cleared them, so I subtract them. Free cash is about 526 (five hundred twenty-six) thousand dollars.

> 🖱️ I'm pointing at restricted: about 382 (three hundred eighty-two) thousand.

> 🟢 That's the debt service reserve. The lender controls it, so it doesn't count toward the 500 (five hundred) thousand minimum.

**WHY:** tres decisiones de tesorería en una tabla: duplicados fuera, cheques pendientes restados (criterio conservador) y caja restringida excluida.

**EXPECTED RESULT:** `operating cleared 590088.2`, `operating pending -64150.0`, `restricted cleared 381900.0`.

**VERIFY BEFORE CONTINUING:** tres filas. `cash0` vale 525,938.20 (590,088.20 − 64,150).

📘 **What each line does** (para vos, no se lee):

- `pos = b.drop_duplicates("txn_id").groupby(["account_type", "status"]).amount.sum()`: bank balance by account type and status, each transaction counted once.
- `cash0 = pos["operating"].sum()`: opening unrestricted cash, cleared plus pending.
- `pos`: shows the reconciled position.

---

### Bloque 3. Phase 2: confiabilidad de los cobros

**TIME:** 6:38–9:13 (2:35)

**WHAT I DO:** + Code → tipear 2 tramos → Run → señalar tres clientes.

**WHERE:** **+ Code** arriba a la izquierda; la celda 3 aparece debajo de la salida de la celda 2.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell three below cell two.

> 🗣️⌨️ First line of cell three: days late for every paid invoice, paid date minus due date.

```python
ar["late"] = (ar.paid_date - ar.due_date).dt.days
```
*(49 caracteres · ~22 s)*

> 🗣️⌨️ Next lines of cell three: the median delay per customer, only for payments in the last 90 (ninety) days. The median ignores one-off outliers, and recent behavior predicts the next weeks better than all of history.

```python
d = ar[ar.paid_date > "2026-08-22"].groupby("customer").late.median()
d
```
*(71 caracteres · ~32 s)*

> 🖱️ I'm clicking the Run button on the left of cell three.

> 🖱️ I'm pointing at Northwind Retail at the bottom of the list under cell three: 26.5 (twenty-six point five) days late.

> 🟢 Northwind is 46 (forty-six) percent of what customers owe us. A delay that big, on that much money, is the biggest risk in this forecast.

> 🖱️ I'm pointing at Harbor Cafe Group and Keystone Office: 17 (seventeen) days each.

> 🖱️ I'm pointing at Lakeside Clinics: half a day. Most customers pay on time.

> 🟢 Management's forecast assumes everyone pays on the due date. I'll replace that with each customer's real delay. And there's no evidence anyone pays early, so I reject accelerating collections as a lever.

**WHY:** el forecast de la gerencia supone cobro en plazo; la evidencia del archivo dice otra cosa. Ajustar con la mora real es el cambio que más mueve la caja.

**EXPECTED RESULT:** 12 clientes; `Northwind Retail 26.5`, `Harbor Cafe Group 17.0`, `Keystone Office 17.0`, `Lakeside Clinics 0.5`.

**VERIFY BEFORE CONTINUING:** Northwind tiene el número más alto.

📘 **What each line does** (para vos, no se lee):

- `ar["late"] = (ar.paid_date - ar.due_date).dt.days`: days late per invoice (in memory only; the file isn't touched).
- `d = ar[ar.paid_date > "2026-08-22"].groupby("customer").late.median()`: median delay per customer over the last 90 days.
- `d`: shows it.

---

### Bloque 4. Phase 3: forecast de 13 semanas

**TIME:** 9:13–14:37 (5:24)

**WHAT I DO:** + Code → tipear 6 tramos → Run → recorrer la tabla.

**WHERE:** **+ Code** arriba a la izquierda; la celda 4 aparece debajo de la salida de la celda 3.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell four below cell three.

> 🗣️⌨️ First line of cell four: o is the open invoices, not the disputed ones. Each one goes in the week of its due date plus that customer's delay.

```python
o = ar[ar.status.eq("open")].assign(week=W(ar.due_date + 
```
*(57 caracteres · ~25 s)*

> 🗣️⌨️ Same line, continuing: the delay in days, from cell three.

*(sigue en la misma línea, sin Enter)*

```python
pd.to_timedelta(ar.customer.map(d), "D")))
```
*(42 caracteres · ~19 s)*

> 🗣️⌨️ Next line of cell four: f is every cash flow. The receivables, plus the payables as negative amounts in the week they're due.

```python
f = pd.concat([o, ap.assign(week=W(ap.due_date), amount=-ap.amount), 
```
*(69 caracteres · ~31 s)*

> 🗣️⌨️ Same line, continuing: plus the operating forecast, with new-sales collections pushed back by the same customer delay, in weeks.

*(sigue en la misma línea, sin Enter)*

```python
op.assign(week=op.week + op.customer.map(d).fillna(0) // 7)])
```
*(61 caracteres · ~27 s)*

> 🗣️⌨️ Next line of cell four: the forecast table. Outflows and inflows per week.

```python
fc = f.groupby(["week", f.amount > 0]).amount.sum().unstack()
```
*(61 caracteres · ~27 s)*

> 🗣️⌨️ Same line, continuing: name the two columns, keep weeks one to thirteen, and add the closing cash. Then show it.

*(sigue en la misma línea, sin Enter)*

```python
.set_axis(["outflow", "inflow"], axis=1).loc[:13].assign(close=c(f))
fc
```
*(71 caracteres · ~32 s)*

> 🖱️ I'm clicking the Run button on the left of cell four.

> 🖱️ I'm pointing at week 1 (one) under cell four: about 502 (five hundred two) thousand going out and closing cash of about 371 (three hundred seventy-one) thousand.

> 🟢 We're below the 500 (five hundred) thousand minimum in the very first week, because overdue bills and payroll all land at once.

> 🖱️ I'm pointing at week 5 (five) in the inflow column: about 453 (four hundred fifty-three) thousand, the best collection week, which is why cash briefly recovers.

> 🖱️ I'm pointing at week 9 (nine) in the close column: about 301 (three hundred one) thousand, the lowest point.

> 🟢 That's a deficit of about 199 (one hundred ninety-nine) thousand dollars. Cash only gets back above the minimum in weeks 4 (four) to 6 (six) and week 12 (twelve).

> 🖱️ I'm pointing at week 8 (eight) in the outflow column: 376 (three hundred seventy-six) thousand, which includes the 168 (one hundred sixty-eight) thousand term loan payment from the debt file.

> 🖱️ I'm pointing at week 13 (thirteen) at the bottom: about 498 (four hundred ninety-eight) thousand.

> 🟢 Even at the end we're still short. So this isn't just timing that fixes itself: it's a funding gap that needs action.

**WHY:** la tabla muestra la primera semana bajo el mínimo (semana 1), el déficit (piso de la semana 9) y que el problema no se cierra solo (semana 13 todavía abajo): es estructural, no solo de timing.

**EXPECTED RESULT:** 13 filas. Semana 1: `-501612.21 346698.69 371024.68`. Semana 9: `close 301347.18`. Semana 13: `close 497982.59`.

**VERIFY BEFORE CONTINUING:** la columna `close` de la semana 9 es 301,347.18.

📘 **What each line does** (para vos, no se lee):

- `o = ar[ar.status.eq("open")].assign(week=W(ar.due_date + pd.to_timedelta(ar.customer.map(d), "D")))`: open invoices in the week of their expected payment.
- `f = pd.concat([o, ap.assign(...), op.assign(...)])`: all flows: receivables (+), payables (−) and the operating forecast with customer delays.
- `fc = f.groupby(["week", f.amount > 0]).amount.sum().unstack().set_axis(["outflow", "inflow"], axis=1).loc[:13].assign(close=c(f))`: weekly outflows, inflows and closing cash.
- `fc`: shows the forecast.

---

### Bloque 5. Phase 4: capacidad real de endeudamiento

**TIME:** 14:37–19:03 (4:26)

**WHAT I DO:** + Code → tipear 5 tramos → Run → señalar las cuatro filas.

**WHERE:** **+ Code** arriba a la izquierda; la celda 5 aparece debajo de la salida de la celda 4.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell five below cell four.

> 🟢 The revolver says 1.2 (one point two) million, but that's never what you can really draw. Cell five calculates the real number.

> 🗣️⌨️ First line of cell five: eligible receivables. Open invoices only, so the disputed ones are out, and each customer capped at 25 (twenty-five) percent of the total. The file has no concentration limit, so that cap is my documented assumption.

```python
e = o.groupby("customer").amount.sum().clip(upper=o.amount.sum() / 4).sum()
```
*(75 caracteres · ~33 s)*

> 🗣️⌨️ Next line of cell five: the borrowing base, 80 (eighty) percent of eligible receivables, minus the reserve, minus what's already drawn.

```python
bba = pd.Series({"eligible": e, "base": r.advance_rate * e - r.reserve - r.drawn, 
```
*(82 caracteres · ~36 s)*

> 🗣️⌨️ Same line, continuing: room left under the commitment.

*(sigue en la misma línea, sin Enter)*

```python
"commitment": r.commitment - r.drawn, 
```
*(38 caracteres · ~17 s)*

> 🗣️⌨️ Same line, continuing: room left under the leverage covenant, 3.5 (three point five) times EBITDA minus all the debt.

*(sigue en la misma línea, sin Enter)*

```python
"leverage": r.max_leverage * r.ltm_ebitda - debt.drawn.sum()})
```
*(62 caracteres · ~28 s)*

> 🗣️⌨️ Last lines of cell five: the real capacity is the smallest of the three limits.

```python
cap = bba.iloc[1:].min()
bba
```
*(28 caracteres · ~12 s)*

> 🖱️ I'm clicking the Run button on the left of cell five.

> 🖱️ I'm pointing at eligible under cell five: about 1.6 (one point six) million.

> 🟢 The 25 (twenty-five) percent cap removed about 426 (four hundred twenty-six) thousand of Northwind's invoices. Lending against one customer that pays a month late isn't safe.

> 🖱️ I'm pointing at base and commitment, in the middle of the output under cell five.

> 🟢 There's 450 (four hundred fifty) thousand left under the commitment, but the borrowing base only supports about 380 (three hundred eighty) thousand.

> 🖱️ I'm pointing at leverage: 235 (two hundred thirty-five) thousand, the smallest.

> 🟢 The covenant is the binding limit. Of the 1.2 (one point two) million revolver, I can really draw 235 (two hundred thirty-five) thousand. Drawing more would break the 3.5 (three point five) times leverage.

**WHY:** la capacidad es el mínimo de tres límites. Se demuestra que el compromiso nominal no está disponible: manda el covenant de apalancamiento.

**EXPECTED RESULT:** `eligible 1599898.56`, `base 379918.848`, `commitment 450000.0`, `leverage 235000.0`.

**VERIFY BEFORE CONTINUING:** `leverage` es el menor de los tres; `cap` = 235,000.

📘 **What each line does** (para vos, no se lee):

- `e = o.groupby("customer").amount.sum().clip(upper=o.amount.sum() / 4).sum()`: open AR per customer, capped at 25% of total open AR, then summed.
- `bba = pd.Series({...})`: eligible AR; borrowing base (advance rate × eligible − reserve − drawn); room under the commitment; room under the leverage covenant.
- `cap = bba.iloc[1:].min()`: real availability, the lowest of the three limits.
- `bba`: shows the analysis.

---

### Bloque 6. Phase 4–5: estrategias y estrés

**TIME:** 19:03–24:24 (5:20)

**WHAT I DO:** + Code → tipear 7 tramos → Run → señalar el gráfico.

**WHERE:** **+ Code** arriba a la izquierda; la celda 6 aparece debajo de la salida de la celda 5.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell six below cell five.

> 🗣️⌨️ First line of cell six: the first lever, defer the discretionary spending, marketing and capex, beyond the 13 (thirteen) weeks.

```python
p = f[f.discretionary.ne("Y")]
```
*(30 caracteres · ~13 s)*

> 🗣️⌨️ Next line of cell six: the second lever, pay suppliers later, but only by the days each one accepts. Critical suppliers accept zero, so they're never delayed.

```python
q = p.assign(week=p.week + p.max_extension_days.fillna(0) // 7)
```
*(63 caracteres · ~28 s)*

> 🗣️⌨️ Next line: the downside. N pushes the customer with the longest delay, Northwind, two more weeks.

```python
N = lambda x: x.assign(week=x.week + 2 * x.customer.eq(d.idxmax()))
```
*(67 caracteres · ~30 s)*

> 🗣️⌨️ Next line of cell six: the draw I need so the stressed plan stays above 500 (five hundred) thousand, rounded up to 25 (twenty-five) thousand.

```python
x = np.ceil((500000 - c(N(q)).min()) / 25000) * 25000
```
*(53 caracteres · ~24 s)*

> 🗣️⌨️ Next line: the scenario table. Base, credit only, and credit only under stress.

```python
t = pd.DataFrame({"base": c(f), "credit": c(f) + cap, "credit_stress": c(N(f)) + cap, 
```
*(86 caracteres · ~38 s)*

> 🗣️⌨️ Same line, continuing: levers only, the combined plan, and the combined plan under stress.

*(sigue en la misma línea, sin Enter)*

```python
"levers": c(q), "combined": c(q) + x, "stress": c(N(q)) + x})
```
*(61 caracteres · ~27 s)*

> 🗣️⌨️ Last line of cell six: a chart of all six, with the 500 (five hundred) thousand minimum as a black line.

```python
t.plot().axhline(500000, color="k");
```
*(36 caracteres · ~16 s)*

> 🖱️ I'm clicking the Run button on the left of cell six.

> 🖱️ I'm pointing at the black horizontal line in the chart under cell six: the 500 (five hundred) thousand minimum.

> 🖱️ I'm pointing at the blue line, base: below the minimum in 9 (nine) of the 13 (thirteen) weeks.

> 🖱️ I'm pointing at the orange line, credit only: above. The green one, credit under stress, drops well below.

> 🟢 Drawing all 235 (two hundred thirty-five) thousand uses the whole capacity and still fails if Northwind slips. That's why I reject credit only.

> 🖱️ I'm pointing at the red line, levers: it dips under the minimum. Cutting costs alone isn't enough.

> 🖱️ I'm pointing at the purple line, combined, and the brown one, stress: both stay above the black line every week.

**WHY:** el giro `x` se dimensiona sobre el caso estresado, no sobre el base: así el plan aguanta el riesgo de concentración. Estirar a proveedores críticos se descarta por la consecuencia operativa (cortan el suministro).

**EXPECTED RESULT:** un gráfico con seis líneas y una horizontal negra en 500,000. Colores: `base` azul, `credit` naranja, `credit_stress` verde, `levers` rojo, `combined` violeta (la de más arriba), `stress` marrón. Debajo del mínimo: `base` en 9 semanas, `credit_stress` en 7, `levers` en las semanas 1 y 9; `credit`, `combined` y `stress` nunca.

**VERIFY BEFORE CONTINUING:** aparece el gráfico sin error. Si aparece una línea de texto tipo `<matplotlib.lines.Line2D…>`, falta el `;` al final.

📘 **What each line does** (para vos, no se lee):

- `p = f[f.discretionary.ne("Y")]`: flows without discretionary spending (deferred beyond week 13).
- `q = p.assign(week=p.week + p.max_extension_days.fillna(0) // 7)`: payables moved by their allowed extension, in whole weeks; critical suppliers have 0.
- `N = lambda x: x.assign(week=x.week + 2 * x.customer.eq(d.idxmax()))`: stress: the slowest payer's collections two weeks later.
- `x = np.ceil((500000 - c(N(q)).min()) / 25000) * 25000`: draw needed to keep the stressed plan at the minimum, rounded up to 25,000.
- `t = pd.DataFrame({...})`: weekly closing cash for six scenarios.
- `t.plot().axhline(500000, color="k");`: chart with the minimum cash line in black, so it doesn't share the blue of `base`.

---

### Bloque 7. Phase 5: validación, exportación y archivos

**TIME:** 24:24–28:01 (3:38)

**WHAT I DO:** + Code → tipear 2 tramos → Run → señalar el reporte y los mínimos → Files: refrescar, señalar los cinco entregables y abrir el forecast → cerrar el visor.

**WHERE:** **+ Code** arriba a la izquierda; la celda 7 aparece debajo del gráfico. Panel Files a la izquierda: botón de refrescar (flecha circular) arriba del panel.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell seven below the chart.

> 🗣️⌨️ First line of cell seven: the risk report. The draw, and leverage after drawing it: all debt plus the draw, over EBITDA.

```python
k = pd.Series({"draw": x, "leverage": (debt.drawn.sum() + x) / r.ltm_ebitda})
```
*(77 caracteres · ~34 s)*

> 🗣️⌨️ Last lines of cell seven: export the five files, show the risk report, and the minimum cash of each scenario.

```python
export()
print(k)
t.min()
```
*(25 caracteres · ~11 s)*

> 🖱️ I'm clicking the Run button on the left of cell seven.

> 🖱️ I'm pointing at draw under cell seven: 225 (two hundred twenty-five) thousand. That's below the 235 (two hundred thirty-five) thousand capacity.

> 🖱️ I'm pointing at leverage: 3.49 (three point four nine) times, just under the 3.5 (three point five) covenant.

> 🟢 The plan is legal, but tight: there's almost no covenant room left. That's the main remaining risk.

> 🖱️ I'm pointing at the minimum for base and levers: about 301 (three hundred one) thousand and about 486 (four hundred eighty-six) thousand, both below 500 (five hundred) thousand. Rejected.

> 🖱️ I'm pointing at credit and credit_stress: about 536 (five hundred thirty-six) thousand, but about 348 (three hundred forty-eight) thousand under stress. Rejected.

> 🖱️ I'm pointing at combined and stress: about 711 (seven hundred eleven) thousand and about 519 (five hundred nineteen) thousand. Both above the minimum.

> 🟢 So my recommendation is the combined plan: defer 179 (one hundred seventy-nine) thousand of discretionary spend, stretch only the non-critical suppliers, and draw 225 (two hundred twenty-five) thousand on the revolver. It holds even if Northwind pays two weeks later.

> 🖱️ I'm clicking the refresh button at the top of the Files panel, to see the new files.

> 🖱️ I'm pointing at the five new files in the Files panel: cash position, 13-week (thirteen-week) forecast, borrowing base, scenario comparison and risk report, next to the five untouched inputs.

> 🖱️ I'm double-clicking 13_week_liquidity_forecast.csv (thirteen week liquidity forecast) in the Files panel, to open it on the right and check it saved correctly.

> 🖱️ I'm pointing at the columns in the viewer: week, outflow, inflow and close, the same 13 (thirteen) rows as cell four.

> 🖱️ I'm closing the file viewer with the X on its tab, to go back to the notebook.

**WHY:** se verifican las tres restricciones a la vez: caja mínima (los dos escenarios elegidos ≥ 500,000), límite de giro (225,000 ≤ 235,000) y covenant (3.49x ≤ 3.5x). Las alternativas rechazadas quedan con su número.

**EXPECTED RESULT:**

- `draw 225000.0`, `leverage 3.490654`.
- `base 301347.18`, `credit 536347.18`, `credit_stress 348448.52`, `levers 485706.85`, `combined 710706.85`, `stress 518909.18`.
- En Files: los cinco CSV de entrada y los cinco nuevos.

**VERIFY BEFORE CONTINUING:** los cinco archivos nuevos aparecen en Files. Si el doble clic no abre el visor, no insistas: 🖱️ *"The viewer didn't open, so I'm pointing at the file in the Files panel instead."* y seguí.

📘 **What each line does** (para vos, no se lee):

- `k = pd.Series({"draw": x, "leverage": (debt.drawn.sum() + x) / r.ltm_ebitda})`: recommended draw and resulting leverage.
- `export()`: writes the five deliverables (function from cell 1).
- `print(k)`: shows the risk report.
- `t.min()`: lowest weekly cash per scenario.

---

### Bloque 8. Epilogue

**TIME:** 28:01–29:29 (1:27)

**WHAT I DO:** Cmd + S → scroll lento hacia arriba, sin tipear. Recién **después** abrís TaskRecorder para detener la grabación.

**WHERE:** Colab, desde la celda 7 hasta la celda 1.

**SAY:**

> 🖱️ I'm pressing Command and S to save the notebook; the save message appears at the bottom left.

> 🖱️ I'm scrolling up slowly through the notebook, from cell seven back to cell one, to recap.

> 🟢 My approach: rebuild free cash from the bank, replace management's on-time assumption with real customer delays, then size the financing against the real limits, not the headline commitment.

> 🟢 The key decisions: pending checks reduce cash, restricted cash doesn't count, Northwind is capped at 25 (twenty-five) percent, and critical suppliers are never stretched.

> 🟢 The hardest part was Northwind: almost half of receivables, paying a month late. The draw is sized so the plan survives if it slips even more.

> 🟢 Remaining risks: leverage ends at 3.49 (three point four nine) times, so there's no room for another draw, and stretching suppliers costs some goodwill. With more time, I'd negotiate covenant headroom with the bank. Thanks for watching!

**WHY:** es el resumen ejecutivo: enfoque, decisiones, desafío, recomendación y riesgos que quedan.

---

## Si algo sale mal

| Error | Qué decís y hacés |
| ----- | ----------------- |
| Un nombre mal escrito | 🖱️ *"There's a typo in cell N. I'm clicking on that line to fix it, and running the cell again."* |
| `NameError` | 🖱️ *"An earlier cell didn't run. I'm opening the Runtime menu at the top and choosing Run before."* |
| `NameError: cash0` en la celda 4 | La celda 2 no corrió: `c` usa `cash0`. Corré la celda 2 y después la 4. |
| La celda 4 no da 301,347 en la semana 9 | Revisá `"2026-08-22"` en la celda 3 y el `// 7` de la celda 4. |
| La celda 5 no da 235,000 en `leverage` | Revisá `debt.drawn.sum()` (suma las tres líneas de deuda, no solo el revolver). |
| El gráfico muestra texto debajo | Falta el `;` al final de `t.plot().axhline(500000, color="k");`. No es un error: seguí. |
| Hay que volver a correr todo | Los CSV de entrada nunca se reescriben: alcanza con Runtime → Run all. |

---

## Checklist de archivos y preparación previa

- [ ] Practicá dos veces con cronómetro. [liquidity_assessment.ipynb](liquidity_assessment.ipynb) tiene el código completo para comparar. No lo abras en la grabación.
- [ ] En Colab, creá el notebook **liquidity_assessment** con **la celda 1 escrita** (copiala del bloque 1) y nada más. **No ejecutes nada.**
- [ ] En **Files**, subí los cinco CSV de esta carpeta. Revisá que los nombres no tengan `(1)`.
- [ ] Cerrá el panel Files antes de empezar: se abre en el bloque 0.
- [ ] **Tools → Settings → AI assistance**: ocultá las funciones de IA.
- [ ] **Tools → Settings → Editor**: si está la opción, desactivá las sugerencias automáticas de código.
- [ ] Zoom (`Cmd + +`). Firefox con la ventana 1 en la descripción de la tarea y la ventana 2 en Colab.

## Checklist de resultados que deben quedar generados

- [ ] `bank (163, 8) | duplicate rows: 5` y la tabla de deuda (celda 1).
- [ ] `590088.2 / -64150.0 / 381900.0` (celda 2).
- [ ] Northwind 26.5 (celda 3).
- [ ] Semana 9 = 301,347.18 (celda 4).
- [ ] `leverage 235000.0` como mínimo (celda 5).
- [ ] El gráfico con seis líneas y la línea de 500,000 (celda 6).
- [ ] `draw 225000`, `leverage 3.49` y los seis mínimos (celda 7).
- [ ] En Files: `reconciled_cash_position.csv`, `13_week_liquidity_forecast.csv`, `borrowing_base_analysis.csv`, `scenario_comparison.csv` y `liquidity_risk_report.csv`.
- [ ] Después: descargá `liquidity_assessment.ipynb` y los cinco CSV generados. Armá **Deliverables.zip** con eso y los cinco CSV de entrada sin tocar. Marcá en Studio la opción de archivos generados con IA.

## Checklist de decisiones que debo explicar

- [ ] **Duplicados del banco** fuera ($202,453).
- [ ] **Cheques pendientes** restan; **caja restringida** no cuenta.
- [ ] **Mora mediana de 90 días** en vez del supuesto de cobro en plazo; no se aceleran cobranzas (no hay evidencia).
- [ ] **AR elegible:** sin disputadas y con tope de 25% por cliente (supuesto documentado).
- [ ] **Capacidad real** = mínimo de tres límites; manda el covenant ($235,000).
- [ ] **Proveedores críticos** nunca se estiran.
- [ ] **El giro se dimensiona con estrés**, no con el caso base.
- [ ] **Alternativas rechazadas** con su número: base, solo crédito, solo palancas.
- [ ] **Riesgos que quedan:** covenant al límite (3.49x), Northwind, relación con proveedores.
