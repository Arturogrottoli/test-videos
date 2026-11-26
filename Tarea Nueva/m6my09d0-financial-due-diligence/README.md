# m6my09d0 — Financial Due Diligence

Guion para grabar la tarea **m6my09d0** en **Google Colab** (app principal), con **Firefox** como app de apoyo, en una sola toma.

> **Goal:** *I will perform a focused financial due diligence assessment of a simulated acquisition target, investigating revenue recognition discrepancies, accounts receivable recoverability, and the validity of management-proposed EBITDA adjustments. I will use cross-source reconciliations and historical transaction analysis to quantify material earnings and working capital risks, producing a reproducible financial analysis and an evidence-based findings report to support the acquiring company's investment decision.*

**Duración estimada: ~25:59, con 35% de tipeo** (tipeando a 135 car./min; ya cuenta los números leídos en palabras). Objetivo 20–25 min; límite absoluto 30:00. Si tipeás a 120 car./min da ~27:07 y 38%: practicá hasta tipear cada tramo en el tiempo indicado.

**Punto de partida al grabar:**

- El notebook **financial_due_diligence** tiene la **celda 1 ya escrita**.
- Los cuatro CSV ya están subidos en el panel **Files** de Colab.
- La celda 1 es solo preparación: librerías, lectura de los CSV, la huella (hash) de cada archivo, dos columnas auxiliares, el mapa de cuentas y la plantilla del PDF, `report()`.
- **Todo lo demás se tipea en vivo** (celdas 2 a 12).
- En el video se dice que la celda 1 estaba escrita y por qué.

**Reglas que cumple (iguales a las otras tareas):**

- **Ningún CSV de entrada se modifica.** La última celda lo demuestra comparando la huella de cada archivo con la del principio.
- La apertura sobre la descripción dura menos de 20 s y empieza con la frase exacta: *"I will be beginning my task soon. Here is the workflow I have in mind."*
- Cada acción del mouse tiene su frase 🖱️ con qué, dónde y por qué.
- Nunca se habla y se tipea a la vez; ningún tramo de tipeo pasa de 45 s.
- Objetivo ~25 min, máximo 30. Tipeo ≤35%.
- Los números se leen en palabras (entre paréntesis), y con "about" cuando están redondeados.

---

## Cronograma

| # | Bloque | Fase | Celda | TIME | Duración |
| - | ------ | ---- | ----- | ---- | -------- |
| 0 | Opening | — | — | 0:00–1:04 | 1:04 |
| 1 | Celda 1: carga e inspección | 1. Opening and data inspection | 1 | 1:04–2:38 | 1:34 |
| 2 | Phase 1: qué contiene el libro mayor | 1. Opening and data inspection | 2 | 2:38–3:57 | 1:19 |
| 3 | Phase 2: conciliación entre fuentes | 2. Revenue reconciliation | 3 | 3:57–5:59 | 2:02 |
| 4 | Phase 2: rastreo del corte de ingresos | 2. Revenue reconciliation | 4 | 5:59–7:19 | 1:20 |
| 5 | Phase 2: transacciones duplicadas | 2. Revenue reconciliation | 5 | 7:19–8:54 | 1:35 |
| 6 | Phase 3: respaldo de cada ajuste | 3. Quality of earnings | 6 | 8:54–10:27 | 1:33 |
| 7 | Phase 3: evidencia de reestructuración y consultoría | 3. Quality of earnings | 7 | 10:27–12:03 | 1:37 |
| 8 | Phase 3: veredictos y EBITDA normalizado | 3. Quality of earnings | 8 | 12:03–16:12 | 4:09 |
| 9 | Phase 3: cuentas por cobrar vencidas | 3. Receivables | 9 | 16:12–17:54 | 1:41 |
| 10 | Phase 3: facturación a IronBridge después de la administración | 3. Receivables | 10 | 17:54–19:13 | 1:20 |
| 11 | Phase 4: los cinco hallazgos | 4. Findings and reporting | 11 | 19:13–22:20 | 3:07 |
| 12 | Phase 4: informe PDF y validación | 4. Findings and reporting | 12 | 22:20–24:39 | 2:19 |
| 13 | Epilogue | — | — | 24:39–25:59 | 1:20 |
| | **Total** | | | | **~25:59** |

*(Calculado con 130 palabras/min de narración, 135 caracteres/min de tipeo en silencio, todo sumado, más ~20 s de navegación y ejecución por bloque.)*

---

## Archivos

**Input files** (data room de Northstar Industrial Components, ene-2024 a dic-2025):

| Archivo | Filas | Qué tiene |
| ------- | ----- | --------- |
| `general_ledger.csv` | 622 | Asientos con fecha de transacción y de registro, cuenta, débito, crédito, contraparte y documento. Cuadra (débitos = créditos). **No tiene cobros de clientes**: Accounts Receivable solo tiene débitos |
| `monthly_financials.csv` | 24 | Estado de resultados mensual. El EBITDA es antes de la depreciación (EBITDA − D&A = EBIT en los 24 meses) |
| `accounts_receivable_aging.csv` | 9 | Facturas abiertas por $1,196,200. Ninguno de esos números de factura aparece en el libro mayor |
| `management_adjustments.csv` | 9 | Ajustes de EBITDA de la gerencia: 3 de 2024 y 6 de 2025, con su documento de respaldo |

**Corrección hecha antes de grabar:** el generador de datos tenía un bug. Al inyectar el duplicado PO-2024-0892, pisó dos líneas de compra de octubre de 2024. Por eso faltaban $721,745 de COGS en el libro mayor. Se subió la línea `PO-2024-2034` (TXN10247 y TXN10248) de 250,811 a 972,556. Ahora el libro mayor cuadra con los estados mensuales en todas las líneas, salvo las dos diferencias reales (corte de ingresos y $55,000 de consultoría). El original quedó guardado fuera del repo. En el video no se modifica nada.

**Output files:**

| Archivo | Cómo se genera |
| ------- | -------------- |
| `due_diligence_findings_report.pdf` | `report()` en la celda 12. Se descarga desde Files y se abre en Firefox |
| `financial_due_diligence.ipynb` | Cmd + S y File → Download → Download .ipynb, en el epílogo |

---

## Los números que tenés que tener claros

| Concepto | Valor | Celda |
| -------- | ----- | ----- |
| Ingresos 2024 / 2025 (estados mensuales) | $18,979,748 / $21,068,722 | 1 |
| EBITDA reportado 2025 | $3,157,374 | 1 y 8 |
| EBITDA de la gerencia 2025 (con sus 6 ajustes) | $3,546,874 | 8 |
| **EBITDA defendible 2025** (reportado − $55,000 de consultoría no registrada) | **$3,102,374** | 8 |
| Si se documentan los ajustes calificados (+$174,500) | $3,276,874 | PDF |
| Brecha con la gerencia | $444,500 = rechazados $215,000 + calificados $174,500 + consultoría $55,000 | PDF |
| Cuentas por cobrar → después de la previsión de IronBridge | $1,196,200 → **$883,400** | 9 |
| Más de 90 días sin evidencia suficiente (Keystone + Cascade) | $110,600 | 9 |
| Facturado a IronBridge después de entrar en administración | $668,197 (pregunta abierta) | 10 |

**Veredicto de cada ajuste:**

| Ajuste | Año | Monto | Veredicto | Por qué |
| ------ | --- | ----- | --------- | ------- |
| ADJ-001 Legal settlement | 2024 | 185,000 | Rechazado | `LEGAL-SET-2024` no está en el libro mayor |
| ADJ-002 Restructuring | 2024 | 95,000 | Rechazado | Se repite en feb-2025: no es único |
| ADJ-003 Restructuring | 2025 | 78,000 | Rechazado | Segunda reestructuración en 4 meses: recurrente |
| ADJ-004 Owner comp | 2025 | 120,000 | Calificado | Ajuste pro forma: necesita contrato del CEO y benchmark |
| ADJ-005 ERP consulting | 2025 | 95,000 | Rechazado | `CONS-ERP-2025` no existe; la única consultoría es `CONS-2025-Q4` ($55,000) |
| ADJ-006 Depreciation | 2025 | 42,000 | Rechazado | El EBITDA ya excluye la depreciación: se contaría dos veces |
| ADJ-007 Above-market rent | 2025 | 36,000 | Calificado | Necesita estudio de mercado y que el alquiler cambie al cierre |
| ADJ-008 Duplicate PO-2024-0892 | 2024 | 42,300 | Aceptado | El duplicado está en el libro mayor |
| ADJ-009 FX loss | 2025 | 18,500 | Calificado | `FX-REVAL-2025` no está; el SG&A está en totales mensuales |

**Los cinco hallazgos (celda 11):**

| # | Hallazgo | Monto | Tipo de exposición |
| - | -------- | ----- | ------------------ |
| F1 | Corte de ingresos: INV2024-12-C002 (Cascade), fecha 28-dic-2024, registrada 08-ene-2025 | $148,500 | Timing entre años; neto cero en dos años |
| F2 | Duplicado PO-2024-0892 (TechServ): $84,600 debitados por un servicio de $42,300 | $42,300 | Costo de 2024; no toca 2025 |
| F3 | Consultoría: ADJ-005 sin respaldo + $55,000 en el libro mayor que faltan en los estados mensuales | $150,000 | EBITDA 2025 |
| F4 | Reestructuración recurrente (nov-2024 y feb-2025) | $78,000 | EBITDA 2025 |
| F5 | IronBridge Works: 407 días, en administración | $312,800 | Capital de trabajo |

Los cinco montos **no se suman**: son exposiciones de distinto tipo. Así se evita la doble contabilización.

**Diferencias con la guía del instructor** (`reference/INSTRUCTOR_SOLUTION_GUIDE.md`):

- La guía acepta ADJ-004, ADJ-007 y ADJ-009 y llega a $3,331,874. Acá se califican, porque no hay evidencia en el libro mayor. ADJ-009 se rechazaría por el mismo motivo que ADJ-005.
- La guía no ve que los $55,000 de consultoría no están en los estados mensuales.
- La guía no ve que a IronBridge se le siguió facturando después de entrar en administración.
- Elegiste el criterio estricto. La guía queda solo como referencia y no se muestra en el video.

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
- **WHY:** el criterio profesional, para vos. **Ya está dentro de lo que decís**; no se lee aparte.
- **EXPECTED RESULT:** qué tiene que aparecer.
- **VERIFY BEFORE CONTINUING:** qué controlar antes de pasar al bloque siguiente.
- 📘 = qué hace cada línea, en inglés. Es para vos: **no se lee**.

---

## Estrategia de tiempo y tipeo

| | Cantidad | Tiempo |
| - | -------- | ------ |
| Tipeo en vivo (celdas 2 a 12) | 1.226 caracteres | ~9,1 min a 135 car./min (~10,2 a 120) |
| Narración | ~1.591 palabras | ~12,2 min |
| Navegación y ejecución | 14 bloques | ~4,7 min |
| **Total** | | **~25:59** (~27:07 si tipeás a 120 car./min) |

**Tipeo: ~35% del video a 135 car./min** (~38% a 120).

**Reglas de tipeo:**

1. **Nunca hablar y tipear al mismo tiempo.** Frase 🗣️⌨️ con las manos quietas → bloque en silencio.
2. **Ningún tramo pasa de 45 segundos.** Las líneas largas de las celdas 8 y 11 se tipean en dos tramos, **sin Enter** entre ellos.
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
6. Las tablas anchas del libro mayor tienen barra de scroll horizontal debajo. Si una columna que nombrás no se ve, decí la frase comodín y movete.
7. Frases comodín:
   - *"I'm scrolling right inside the output of cell N, to see the last columns."*
   - *"I'm clicking at the end of line N in cell N, to fix a typo."*
   - *"I'm pressing Escape to close the suggestion box, because I type everything by hand."*
   - *"I'm waiting for cell N to finish; the spinner on its left is still running."*

---

## Guion de grabación

### Bloque 0. Opening

**TIME:** 0:00–1:04 (1:04)

**WHAT I DO:** hablar con la descripción de la tarea en pantalla (menos de 20 s) → minimizar → abrir Colab desde el Dock → abrir el panel Files.

**WHERE:** Firefox ventana 1 (descripción). Botón amarillo arriba a la izquierda. Ícono de Firefox en el Dock (Mac); segunda ventana de la lista. Ícono de carpeta en la barra lateral izquierda de Colab.

**SAY:**

> 🟢 I will be beginning my task soon. Here is the workflow I have in mind. I'll reconcile the target's revenue, trace duplicates, test management's EBITDA add-backs and the receivables, and deliver a notebook and a PDF with five findings.

> 🖱️ I'm minimizing the task description with the yellow button at the top left.

> 🖱️ I'm clicking Firefox in the Dock and choosing the second window: my Colab notebook, financial due diligence.

> 🖱️ I'm clicking the folder icon on Colab's left sidebar, to show the four data room files. They're synthetic, generated with AI, and I never modify them.

**WHY:** la apertura sobre la descripción dura menos de 20 s (pedido explícito del prompt). El resto del bloque ya es Colab.

**EXPECTED RESULT:** el notebook con la celda 1 escrita (sin ejecutar) y el panel Files abierto con los cuatro CSV.

**VERIFY BEFORE CONTINUING:** están los cuatro archivos y no hay ningún PDF ni otro CSV en Files.

---

### Bloque 1. Celda 1: carga e inspección

**TIME:** 1:04–2:38 (1:34)

**WHAT I DO:** señalar cada grupo de líneas de la celda 1 (ya escrita) → Run → señalar las salidas.

**WHERE:** celda 1, la única del notebook, a la derecha del panel Files. Botón Run (triángulo) a la izquierda de la celda.

**Celda 1 (ya escrita antes de grabar, no se tipea):**

```python
import pandas as pd
import numpy as np
import hashlib, textwrap
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

FILES = ["general_ledger.csv", "monthly_financials.csv", "accounts_receivable_aging.csv", "management_adjustments.csv"]
h = lambda: [hashlib.md5(open(f, "rb").read()).hexdigest() for f in FILES]
H = h()
g = pd.read_csv(FILES[0], parse_dates=["Transaction_Date", "Posting_Date"])
m = pd.read_csv(FILES[1])
ar = pd.read_csv(FILES[2])
a = pd.read_csv(FILES[3])
m["Year"] = m.Month.str[:4].astype(int)
g["Year"] = g.Posting_Date.dt.year
g["Amount"] = (g.Debit - g.Credit).abs()
COA = {4010: "Revenue", 5010: "COGS", 6010: "Payroll_Expenses", 6020: "Rent", 6030: "SGA_Expenses", 6040: "Depreciation_Amortization", 6100: "Restructuring"}

def report(path="due_diligence_findings_report.pdf"):
    f = "${:,.0f}".format
    wr = lambda s: textwrap.fill(s, 104, initial_indent="  ", subsequent_indent="     ")
    why = {"ADJ-001": "LEGAL-SET-2024 not in GL; no matching SG&A spike in 2024",
           "ADJ-002": "Restructuring repeats in Feb-2025: not one-time",
           "ADJ-003": "Restructuring also charged in Nov-2024: recurring",
           "ADJ-004": "Pro forma: needs CEO contract and $280k market benchmark",
           "ADJ-005": "CONS-ERP-2025 not in GL; only consulting is CONS-2025-Q4",
           "ADJ-006": "EBITDA already excludes D&A: add-back double counts",
           "ADJ-007": "Pro forma: needs market lease study; lease must reset at close",
           "ADJ-008": "Duplicate confirmed in GL (PO-2024-0892)",
           "ADJ-009": "FX-REVAL-2025 not in GL; SG&A posted as monthly totals"}
    rs = g[g.Account_Code.eq(6100)]
    rv = ib[ib.Credit.gt(0)]
    rest = w.Outstanding_Amount.drop("IronBridge Works")
    adj_ar = ar.Outstanding_Amount.sum() - F.iloc[4]
    up = E.defensible + b.get("qualify", 0)
    e24 = m.EBITDA[m.Year.eq(2024)].sum()
    L = ["NORTHSTAR INDUSTRIAL COMPONENTS LTD. - FINANCIAL DUE DILIGENCE FINDINGS REPORT",
         "Sources: general_ledger, monthly_financials, accounts_receivable_aging, management_adjustments (Jan-2024 to Dec-2025)", "",
         "1. EXECUTIVE SUMMARY",
         wr(f"Management presents 2025 adjusted EBITDA of {f(E.management)}. The evidence supports {f(E.defensible)}: reported EBITDA of "
            f"{f(E.reported)} less {f(x)} of consulting cost that is in the general ledger but missing from the management accounts. "
            f"Qualified adjustments of {f(b.get('qualify', 0))} would lift it to {f(up)} only if documented. Receivables of "
            f"{f(ar.Outstanding_Amount.sum())} fall to {f(adj_ar)} after a full provision for IronBridge Works, which is in administration. "
            f"The ledger shifts {f(F.iloc[0])} of revenue from 2024 to 2025: a timing difference with no two-year impact."), "",
         "2. KEY FINANCIAL DISCREPANCIES (general ledger by posting year minus management accounts)",
         *rec.T.map(f).to_string().split("\n"), "",
         "3. QUANTIFIED EARNINGS AND WORKING CAPITAL RISKS (each amount counted once)",
         f"  EBITDA 2025: management claim vs defensible          {f(E.management - E.defensible):>12}",
         f"     rejected {f(b.get('reject', 0))} + qualified {f(b.get('qualify', 0))} + unrecorded consulting {f(x)}",
         f"  Receivables: IronBridge full provision                {f(F.iloc[4]):>12}",
         f"  Receivables: over 90 days, evidence insufficient      {f(rest.sum()):>12}   ({', '.join(rest.index)})",
         f"  Revenue timing 2024 to 2025 (no EBITDA effect)        {f(F.iloc[0]):>12}",
         f"  2024 duplicate cost (2024 EBITDA understated)         {f(F.iloc[1]):>12}   no 2025 effect", "",
         "4. MANAGEMENT EBITDA ADJUSTMENTS (accepted / rejected / qualified)",
         *[f"  {i} {r.Period}  {f(r.Amount):>9}  {r.verdict:<8} {why[i]}" for i, r in a.set_index("Adjustment_ID").iterrows()],
         f"  2025: reported {f(E.reported)} | management {f(E.management)} | defensible {f(E.defensible)} | if qualified supported {f(up)}",
         f"  2024: reported {f(e24)} + accepted ADJ-008 {f(A['ADJ-008'])} = {f(e24 + A['ADJ-008'])}", "",
         "5. RECEIVABLES ASSESSMENT (over 90 days)",
         *[f"  {n:<22}{f(r.Outstanding_Amount):>10}  {r.Days_Overdue:>4} days  {r.Collection_Notes}" for n, r in w.iterrows()],
         wr(f"IronBridge was invoiced {f(rv.Credit.sum())} after August 2025 ({', '.join(rv.Document_Reference)}). These invoices are not in "
            "the aging and the ledger records no cash receipts, so collection cannot be confirmed."), "",
         "6. FIVE FINDINGS"]
    info = [
        (f"{c.Document_Reference.iloc[0]}, {c.Counterparty.iloc[0]}: dated {c.Transaction_Date.iloc[0]:%Y-%m-%d}, posted {c.Posting_Date.iloc[0]:%Y-%m-%d}",
         f"Revenue by posting year, GL minus management accounts: 2024 = {f(rec.Revenue[2024])}; 2025 = {f(rec.Revenue[2025])}; two-year net = {f(rec.Revenue.sum())}",
         "GL understates 2024 and overstates 2025 revenue; management accounts are correct (accrual). Cut-off control weakness",
         "Reclassify to 2024; test cut-off at both year ends", "High - confirmed timing difference"),
        (f"{d.Document_Reference.iloc[0]}, {d.Counterparty.iloc[0]}: {' and '.join(d.Transaction_ID)}, posted {', '.join(d.Posting_Date.dt.strftime('%d-%b-%Y'))}",
         f"Total debited {f(d.Debit.sum())}; one posting is valid, so overstatement = {f(F.iloc[1])}",
         "2024 COGS overstated and EBITDA understated; payable overstated if unpaid. Supports ADJ-008 (2024 only)",
         "Obtain TechServ credit note or vendor statement", "High on duplicate; medium on recovery"),
        ("ADJ-005 (CONS-ERP-2025): 0 GL rows. CONS-2025-Q4, Consulting Partners LLC, 2025-12-15",
         f"Add-back rejected {f(A['ADJ-005'])} + GL SG&A 2025 above management accounts by {f(x)}",
         "Management EBITDA overstated by both amounts", "Request ERP advisory invoices; book the missing consulting cost", "High - referenced document absent from the ledger"),
        (f"{', '.join(rs.Document_Reference)}: {f(rs.Debit.iloc[0])} ({rs.Posting_Date.iloc[0]:%b-%Y}) and {f(rs.Debit.iloc[1])} ({rs.Posting_Date.iloc[1]:%b-%Y})",
         f"Restructuring in consecutive years; ADJ-003 add-back rejected = {f(F.iloc[3])} (ADJ-002 rejected for 2024)",
         "Restructuring behaves as a recurring cost of the operating model", "Request 2026 restructuring plan", "Medium-high - recurrence is a judgment"),
        ("INV2024-0845, IronBridge Works (C008): 407 days overdue, administration proceedings, legal counsel engaged 2025-08",
         f"Full provision {f(F.iloc[4])}; adjusted receivables {f(ar.Outstanding_Amount.sum())} - {f(F.iloc[4])} = {f(adj_ar)}",
         f"Working capital overstated; plus {f(rv.Credit.sum())} billed after administration with no evidence of collection",
         "Obtain administrator's report and post-close receipts", "High on provision; post-administration billing unresolved")]
    for (t, amt), (src, calc, imp, act, conf) in zip(F.items(), info):
        L += [f"  {t} - {f(amt)}", wr(f"Records: {src}"), wr(f"Calculation: {calc}"), wr(f"Impact: {imp}"),
              wr(f"Follow-up: {act}"), wr(f"Confidence: {conf}"), ""]
    L += ["7. LIMITATIONS AND RECOMMENDED FOLLOW-UP",
          wr(f"No cash receipts in the ledger: Accounts Receivable only has debits ({f(g.Debit[g.Account_Code.eq(1200)].sum())}) and none of "
             "the 9 aging invoices appear in the ledger, so the aging cannot be reconciled to the books."),
          wr("Payroll and SG&A are posted as single monthly totals, so ADJ-004 and ADJ-009 cannot be tested at transaction level."),
          wr(f"{', '.join(rest.index)}: {f(rest.sum())} over 90 days with no dispute flag; evidence is insufficient to provide or to clear."),
          wr("Open requests: IronBridge administrator's report; ERP advisory invoices; TechServ credit note; 2026 restructuring plan; "
             "CEO contract and pay benchmark; market lease study; FX revaluation schedule; bank statements to tie receivables.")]
    txt = "\n".join(L).split("\n")
    with PdfPages(path) as pdf:
        for i in range(0, len(txt), 80):
            fig = plt.figure(figsize=(8.5, 11))
            fig.text(0.05, 0.96, "\n".join(txt[i:i + 80]), family="monospace", size=7, va="top", parse_math=False)
            pdf.savefig(fig)
            plt.close(fig)
    print("saved", path)

for n, d in zip(FILES, [g, m, ar, a]):
    print(n, d.shape, "| nulls:", d.isna().sum().sum(), "| duplicate rows:", d.duplicated().sum())
print("GL debits - credits:", g.Debit.sum() - g.Credit.sum(), "| duplicate transaction IDs:", g.Transaction_ID.duplicated().sum())
print("AR aging total:", ar.Outstanding_Amount.sum(), "| aging invoices found in GL:", ar.Invoice_Number.isin(g.Document_Reference).sum())
m.groupby("Year")[["Revenue", "EBITDA", "Depreciation_Amortization", "EBIT", "Net_Income"]].sum()
```

**SAY:**

> 🖱️ I'm pointing at cell one. I wrote it before recording because it's only setup. Every analysis after it, I type live.

> 🖱️ I'm pointing at H: a fingerprint of each file, so at the end I can prove the evidence never changed.

> 🖱️ I'm pointing at COA, which maps ledger accounts to the monthly financial lines, and at the report function: the PDF template, fed only by variables I calculate live.

> 🖱️ I'm clicking the Run button on the left of cell one.

> 🖱️ I'm pointing at the checks under cell one: no nulls, no duplicate rows, debits equal credits, and unique transaction IDs.

> 🖱️ I'm pointing at the receivables line: none of the 9 (nine) aging invoices exists in the ledger.

> 🟢 So I can't tie the aging to the books. That's a limitation for the report.

> 🖱️ I'm pointing at the yearly table: EBITDA minus depreciation equals EBIT in both years.

> 🟢 So this EBITDA is already before depreciation. I'll need that for one of the add-backs.

**WHY:** la fase 1 del prompt (carga, estructura, validación de campos y calidad de datos) queda a la vista en una sola ejecución. Las dos limitaciones se detectan antes de analizar: no hay cobros en el libro mayor, y el EBITDA es antes de D&A.

**EXPECTED RESULT:**

- `general_ledger.csv (622, 13)`, `monthly_financials.csv (24, 15)`, `accounts_receivable_aging.csv (9, 10)`, `management_adjustments.csv (9, 9)`, todos con `nulls: 0 | duplicate rows: 0`.
- `GL debits - credits: 0.0 | duplicate transaction IDs: 0`.
- `AR aging total: 1196200 | aging invoices found in GL: 0`.
- Tabla: 2024 → `18979748.0 / 2713401.0 / 815403.0 / 1897998.0 / 1269478.0`; 2025 → `21068722.0 / 3157374.0 / 910249.0 / 2247125.0 / 1512265.0`.

**VERIFY BEFORE CONTINUING:** cuatro líneas de archivos, dos líneas de control y la tabla de dos años.

📘 **What each line does** (para vos, no se lee):

- `import ...`: pandas, numpy, hashing, text wrapping and matplotlib's PDF writer (all preinstalled in Colab).
- `FILES = [...]` / `h = lambda: ...` / `H = h()`: MD5 fingerprint of each input file at load time.
- `g`, `m`, `ar`, `a`: ledger (dates parsed), monthly financials, receivables aging, management adjustments.
- `m["Year"]`, `g["Year"]`: calendar year (posting year for the ledger).
- `g["Amount"] = (g.Debit - g.Credit).abs()`: line amount without sign (each P&L account sits on one side only).
- `COA = {...}`: ledger account code → monthly financials column.
- `def report(): ...`: builds the PDF from `rec`, `c`, `d`, `a`, `b`, `E`, `x`, `w`, `ib`, `A` and `F`; runs only when cell 12 calls it.
- `for n, d in zip(...)`: shape, nulls and exact duplicate rows of each file.
- The two `print` lines: ledger balance, unique IDs, AR total and how many aging invoices exist in the ledger.
- `m.groupby("Year")[...].sum()`: two-year P&L summary.

---

### Bloque 2. Phase 1: qué contiene el libro mayor

**TIME:** 2:38–3:57 (1:19)

**WHAT I DO:** + Code → tipear 1 tramo → Run → señalar dos cuentas.

**WHERE:** botón **+ Code** arriba a la izquierda; la celda 2 aparece debajo de la salida de la celda 1.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell two below cell one.

> 🗣️⌨️ Cell two: total debits and credits for each ledger account.

```python
g.groupby("Account_Name")[["Debit", "Credit"]].sum()
```
*(52 caracteres · ~23 s)*

> 🖱️ I'm clicking Run on cell two, and pointing at Accounts Receivable: debits only, no credits.

> 🟢 The ledger records invoices but no customer receipts. It shows what was billed, not what was collected.

> 🖱️ I'm pointing at Restructuring Charges: 173 (one hundred seventy-three) thousand, booked against Accrued Liabilities. I'll come back to it in cell seven.

**WHY:** valida la estructura contable antes de usarla. Muestra que no hay cobros en el libro mayor, el límite principal de la evidencia sobre cuentas por cobrar.

**EXPECTED RESULT:** 12 cuentas. `Accounts Receivable 40048470.0 / 0.0`; `Restructuring Charges 173000.0`; `Accrued Liabilities 0.0 / 173000.0`; `Cost of Goods Sold 24238854.0`.

**VERIFY BEFORE CONTINUING:** `Cost of Goods Sold` da 24,238,854 (si da 23,517,109, el CSV no tiene la corrección de octubre de 2024).

📘 **What each line does** (para vos, no se lee):

- `g.groupby("Account_Name")[["Debit", "Credit"]].sum()`: total debits and credits per ledger account.

---

### Bloque 3. Phase 2: conciliación entre fuentes

**TIME:** 3:57–5:59 (2:02)

**WHAT I DO:** + Code → tipear 2 tramos → Run → señalar Revenue y SGA_Expenses.

**WHERE:** **+ Code** arriba a la izquierda; la celda 3 aparece debajo de la celda 2.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell three.

> 🗣️⌨️ First line of cell three: ledger amounts by posting year and statement line, using the account map.

```python
y = g.groupby(["Year", g.Account_Code.map(COA)]).Amount.sum().unstack()
```
*(71 caracteres · ~32 s)*

> 🗣️⌨️ Then I subtract the monthly financials. Anything that isn't zero is a discrepancy.

```python
rec = y - m.groupby("Year")[y.columns].sum()
rec
```
*(48 caracteres · ~21 s)*

> 🖱️ I'm clicking Run on cell three, and pointing at Revenue: minus 148,500 (one hundred forty-eight thousand five hundred) in 2024 (twenty twenty-four), plus the same in 2025 (twenty twenty-five).

> 🟢 Opposite signs, zero over two years: that looks like timing, not a lost sale.

> 🖱️ I'm pointing at SGA_Expenses: in 2025 (twenty twenty-five) the ledger has 55,000 (fifty-five thousand) more than the management accounts. Every other line ties to the dollar.

**WHY:** una sola conciliación compara todas las líneas del estado de resultados, no solo ingresos. Encuentra el corte de $148,500 y, además, el gasto de $55,000 que falta en los estados mensuales.

**EXPECTED RESULT:** dos filas (2024 y 2025). `Revenue -148500.0 / 148500.0`; `SGA_Expenses 0.0 / 55000.0`; el resto `0.0`.

**VERIFY BEFORE CONTINUING:** COGS da 0.0 en los dos años.

📘 **What each line does** (para vos, no se lee):

- `y = g.groupby(["Year", g.Account_Code.map(COA)]).Amount.sum().unstack()`: ledger P&L by posting year and statement line (balance sheet accounts drop out because they are not in `COA`).
- `rec = y - m.groupby("Year")[y.columns].sum()`: ledger minus monthly financials, same year and line.
- `rec`: shows the reconciliation.

---

### Bloque 4. Phase 2: rastreo del corte de ingresos

**TIME:** 5:59–7:19 (1:20)

**WHAT I DO:** + Code → tipear 1 tramo → Run → señalar las dos filas.

**WHERE:** **+ Code** arriba a la izquierda; la celda 4 aparece debajo de la celda 3.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell four.

> 🗣️⌨️ Cell four: lines posted in a later year than their transaction date.

```python
c = g[g.Transaction_Date.dt.year < g.Year]
c
```
*(44 caracteres · ~20 s)*

> 🖱️ I'm clicking Run on cell four, and pointing at the invoice: Cascade Engineering, dated December 28 (twenty-eight), posted January 8 (eight).

> 🟢 The monthly financials put it in December, which is correct on an accrual basis. The ledger booked it eleven days late, so 2024 (twenty twenty-four) ledger revenue is understated and 2025 (twenty twenty-five) is overstated. It's a cutoff error: a reclassification between years, not an EBITDA adjustment.

**WHY:** separa error de timing: es la única línea que cruza de año, y el monto coincide exacto con la diferencia de la celda 3.

**EXPECTED RESULT:** 2 filas: TXN10293 (Accounts Receivable, débito 148500.0) y TXN10294 (Revenue, crédito 148500.0), `Transaction_Date 2024-12-28`, `Posting_Date 2025-01-08`, `Document_Reference INV2024-12-C002`.

**VERIFY BEFORE CONTINUING:** son exactamente dos filas.

📘 **What each line does** (para vos, no se lee):

- `c = g[g.Transaction_Date.dt.year < g.Year]`: lines posted in a later year than the transaction.
- `c`: shows them.

---

### Bloque 5. Phase 2: transacciones duplicadas

**TIME:** 7:19–8:54 (1:35)

**WHAT I DO:** + Code → tipear 1 tramo → Run → señalar las dos filas.

**WHERE:** **+ Code** arriba a la izquierda; la celda 5 aparece debajo de la celda 4.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell five.

> 🗣️⌨️ Cell five: debit lines with the same document and the same amount. keep False shows every copy.

```python
d = g[g.Debit.gt(0) & g.duplicated(["Document_Reference", "Debit"], keep=False)]
d
```
*(82 caracteres · ~36 s)*

> 🖱️ I'm clicking Run on cell five, and pointing at PO-2024-0892: TechServ, 42,300 (forty-two thousand three hundred) twice, three days apart, in two journals.

> 🟢 One posting is real, so the overstatement is 42,300 (forty-two thousand three hundred), not the 84,600 (eighty-four thousand six hundred) debited. And it's a 2024 (twenty twenty-four) cost, so it doesn't touch 2025 (twenty twenty-five) EBITDA.

**WHY:** cuantifica sin doble conteo: el exceso es una sola de las dos copias. También se ubica el año, para no mezclarlo con el EBITDA de 2025.

**EXPECTED RESULT:** 2 filas, TXN10243 (2024-10-05, JNL5122) y TXN10245 (2024-10-08, JNL5123), ambas `Cost of Goods Sold 42300.0`, `TechServ Maintenance`, `PO-2024-0892`.

**VERIFY BEFORE CONTINUING:** son exactamente dos filas.

📘 **What each line does** (para vos, no se lee):

- `d = g[g.Debit.gt(0) & g.duplicated(["Document_Reference", "Debit"], keep=False)]`: debit lines repeated with the same document and amount, all copies.
- `d`: shows them.

---

### Bloque 6. Phase 3: respaldo de cada ajuste

**TIME:** 8:54–10:27 (1:33)

**WHAT I DO:** + Code → tipear 1 tramo → Run → scroll a la derecha de la salida → señalar la columna `in_gl`.

**WHERE:** **+ Code** arriba a la izquierda; la celda 6 aparece debajo de la celda 5. La columna `in_gl` es la última de la tabla.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell six.

> 🗣️⌨️ Cell six: does each adjustment's supporting document exist in the ledger?

```python
a["in_gl"] = a.Supporting_Document_Reference.isin(g.Document_Reference)
a
```
*(73 caracteres · ~32 s)*

> 🖱️ I'm clicking Run on cell six, and scrolling right to the in_gl column at the end.

> 🖱️ I'm pointing at in_gl: only the two restructuring adjustments and the duplicate are True.

> 🟢 The 95,000 (ninety-five thousand) ERP consulting add-back, the legal settlement and the FX loss cite documents that aren't in the books. Owner pay, rent and depreciation are normalizations: they need outside evidence, not a ledger entry.

**WHY:** cada ajuste se contrasta con el libro mayor antes de opinar. Se distingue un ajuste sin respaldo (debería tener asiento) de una normalización pro forma (necesita evidencia externa).

**EXPECTED RESULT:** 9 filas; `in_gl` True solo en ADJ-002, ADJ-003 y ADJ-008.

**VERIFY BEFORE CONTINUING:** tres True.

📘 **What each line does** (para vos, no se lee):

- `a["in_gl"] = a.Supporting_Document_Reference.isin(g.Document_Reference)`: True when the supporting document appears in the ledger (adds a column in memory only; the CSV is untouched).
- `a`: shows all nine adjustments.

---

### Bloque 7. Phase 3: evidencia de reestructuración y consultoría

**TIME:** 10:27–12:03 (1:37)

**WHAT I DO:** + Code → tipear 1 tramo → Run → señalar las filas de reestructuración y de consultoría.

**WHERE:** **+ Code** arriba a la izquierda; la celda 7 aparece debajo de la celda 6.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell seven.

> 🗣️⌨️ Cell seven: the restructuring account, and anything paid to a consulting firm.

```python
g[g.Account_Code.eq(6100) | g.Counterparty.str.contains("Consult")]
```
*(67 caracteres · ~30 s)*

> 🖱️ I'm clicking Run on cell seven, and pointing at restructuring: 95,000 (ninety-five thousand) in November 2024 (twenty twenty-four) and 78,000 (seventy-eight thousand) in February 2025 (twenty twenty-five).

> 🟢 Two restructurings in four months aren't one-time. I reject both add-backs.

> 🖱️ I'm pointing at the consulting rows: 55,000 (fifty-five thousand), reference CONS-2025-Q4.

> 🟢 That's the only consulting cost in the ledger, and it's the 55,000 (fifty-five thousand) missing from the management accounts. So the ERP add-back has no support, and the real cost isn't even in reported EBITDA.

**WHY:** las dos decisiones más discutibles se apoyan en asientos concretos: la recurrencia (dos cargos en meses consecutivos de dos años) y la consultoría (un documento distinto, por otro monto, y fuera de los estados mensuales).

**EXPECTED RESULT:** 4 filas: TXN10285 (2024-11-30, 95000.0, RESTR-2024-11), TXN10361 (2025-02-28, 78000.0, RESTR-2025-02), TXN10621 (SGA Expenses 55000.0) y TXN10622 (Cash, crédito 55000.0), las dos de `CONS-2025-Q4`.

**VERIFY BEFORE CONTINUING:** cuatro filas.

📘 **What each line does** (para vos, no se lee):

- `g[g.Account_Code.eq(6100) | g.Counterparty.str.contains("Consult")]`: restructuring lines plus every line with a consulting counterparty.

---

### Bloque 8. Phase 3: veredictos y EBITDA normalizado

**TIME:** 12:03–16:12 (4:09)

**WHAT I DO:** + Code → tipear 5 tramos → Run → señalar los tres valores.

**WHERE:** **+ Code** arriba a la izquierda; la celda 8 aparece debajo de la celda 7.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell eight.

> 🗣️⌨️ First line of cell eight: my verdicts. IDs ending in 1 (one), 2 (two), 3 (three), 5 (five) and 6 (six) are rejected...

```python
a["verdict"] = np.where(a.Adjustment_ID.str[-1].isin(list("12356")), "reject", 
```
*(79 caracteres · ~35 s)*

> 🗣️⌨️ Same line, continuing: the rest are accepted if the ledger supports them, otherwise qualified.

*(sigue en la misma línea, sin Enter)*

```python
np.where(a.in_gl, "accept", "qualify"))
```
*(39 caracteres · ~17 s)*

> 🗣️⌨️ Next line: the 2025 (twenty twenty-five) adjustments, by verdict.

```python
b = a[a.Period.eq(2025)].groupby("verdict").Amount.sum()
```
*(56 caracteres · ~25 s)*

> 🗣️⌨️ Next line: reported 2025 (twenty twenty-five) EBITDA, and x, the unrecorded consulting.

```python
e, x = m.EBITDA[m.Year.eq(2025)].sum(), rec.SGA_Expenses[2025]
```
*(62 caracteres · ~28 s)*

> 🗣️⌨️ Last lines: reported, management's figure, and my defensible EBITDA.

```python
E = pd.Series([e, e + b.sum(), e - x], ["reported", "management", "defensible"])
E
```
*(82 caracteres · ~36 s)*

> 🖱️ I'm clicking Run on cell eight, and pointing at the three values: about 3.16 (three point one six) million reported, about 3.55 (three point five five) million for management, and about 3.1 (three point one) million defensible.

> 🟢 Defensible is reported minus the missing consulting. Rejected: restructuring, ERP consulting, and depreciation, which this EBITDA already excludes, so adding it back counts it twice.

> 🟢 Qualified: owner pay, rent and the FX loss, 174,500 (one hundred seventy-four thousand five hundred) in total. Payroll and SG&A are monthly totals, so I'd need the CEO contract, a lease study and the FX schedule. The only accepted one is the 2024 (twenty twenty-four) duplicate.

> 🟢 So the gap between management's EBITDA and mine is 444,500 (four hundred forty-four thousand five hundred).

**WHY:** cada ajuste recibe aceptar, rechazar o calificar con un criterio explícito. El EBITDA defendible solo incluye lo que tiene evidencia. Lo calificado se muestra aparte, como potencial, no como dato.

**EXPECTED RESULT:** `reported 3157374.0`, `management 3546874.0`, `defensible 3102374.0`.

**VERIFY BEFORE CONTINUING:** `defensible` = `reported` − 55,000.

📘 **What each line does** (para vos, no se lee):

- `a["verdict"] = np.where(...isin(list("12356")), "reject", np.where(a.in_gl, "accept", "qualify"))`: ADJ-001/002/003/005/006 rejected; of the rest, ledger-supported → accept (ADJ-008), otherwise qualify (ADJ-004/007/009).
- `b = a[a.Period.eq(2025)].groupby("verdict").Amount.sum()`: 2025 amounts by verdict (reject 215,000, qualify 174,500).
- `e, x = ...`: reported 2025 EBITDA and the 55,000 SG&A gap from cell 3.
- `E = pd.Series([...])`: reported, management-adjusted and defensible EBITDA.
- `E`: shows them.

---

### Bloque 9. Phase 3: cuentas por cobrar vencidas

**TIME:** 16:12–17:54 (1:41)

**WHAT I DO:** + Code → tipear 1 tramo → Run → señalar los tres clientes.

**WHERE:** **+ Code** arriba a la izquierda; la celda 9 aparece debajo de la celda 8.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell nine.

> 🗣️⌨️ Cell nine: receivables more than 90 (ninety) days overdue, by customer.

```python
w = ar[ar.Days_Overdue.gt(90)].set_index("Customer_Name")
w
```
*(59 caracteres · ~26 s)*

> 🖱️ I'm clicking Run on cell nine, and pointing at IronBridge Works: 312,800 (three hundred twelve thousand eight hundred), 407 (four hundred seven) days overdue, in administration. The note says legal counsel was engaged in August 2025 (twenty twenty-five).

> 🟢 That's insolvency, not slow payment. A full provision takes receivables from 1,196,200 (one million one hundred ninety-six thousand two hundred) to 883,400 (eight hundred eighty-three thousand four hundred).

> 🖱️ I'm pointing at Keystone and Cascade: 110,600 (one hundred ten thousand six hundred) together, and neither is disputed.

> 🟢 With no receipts in the ledger, the evidence is insufficient. I flag them, but I don't provide for them.

**WHY:** se distingue riesgo de cobro (insolvencia documentada) de demora común. Donde la evidencia no alcanza, se dice explícitamente y no se inventa una previsión.

**EXPECTED RESULT:** 3 filas: IronBridge Works `312800 / 407`, Keystone Assembly `67400 / 144`, Cascade Engineering `43200 / 183`.

**VERIFY BEFORE CONTINUING:** tres clientes.

📘 **What each line does** (para vos, no se lee):

- `w = ar[ar.Days_Overdue.gt(90)].set_index("Customer_Name")`: invoices over 90 days, indexed by customer.
- `w`: shows them.

---

### Bloque 10. Phase 3: facturación a IronBridge después de la administración

**TIME:** 17:54–19:13 (1:20)

**WHAT I DO:** + Code → tipear 1 tramo → Run → señalar fechas y montos.

**WHERE:** **+ Code** arriba a la izquierda; la celda 10 aparece debajo de la celda 9.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell ten.

> 🗣️⌨️ Cell ten: IronBridge's last ledger lines. Did billing continue after the administration?

```python
ib = g[g.Counterparty.eq("IronBridge Works")].tail(6)
ib
```
*(56 caracteres · ~25 s)*

> 🖱️ I'm clicking Run on cell ten, and pointing at the dates: November and December 2025 (twenty twenty-five), about 668 (six hundred sixty-eight) thousand billed.

> 🟢 None of it is in the aging, and the ledger can't show whether it was collected. That's an open question for the report, not a number in my findings.

**WHY:** es un riesgo de reconocimiento de ingresos (facturar a un cliente insolvente). Como la evidencia no permite concluir, se reporta como pregunta abierta, sin inventar un monto.

**EXPECTED RESULT:** 6 filas (factura y cuenta por cobrar de cada una): INV2025-11-005 `8787.0`, INV2025-11-004 `518709.0`, INV2025-12-005 `140701.0`.

**VERIFY BEFORE CONTINUING:** las tres fechas son posteriores a agosto de 2025.

📘 **What each line does** (para vos, no se lee):

- `ib = g[g.Counterparty.eq("IronBridge Works")].tail(6)`: IronBridge's last three invoices (two ledger lines each).
- `ib`: shows them.

---

### Bloque 11. Phase 4: los cinco hallazgos

**TIME:** 19:13–22:20 (3:07)

**WHAT I DO:** + Code → tipear 4 tramos → Run → señalar los cinco montos.

**WHERE:** **+ Code** arriba a la izquierda; la celda 11 aparece debajo de la celda 10.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell eleven.

> 🗣️⌨️ First line of cell eleven: adjustment amounts by ID.

```python
A = a.set_index("Adjustment_ID").Amount
```
*(39 caracteres · ~17 s)*

> 🗣️⌨️ Next line: the five finding amounts, each from an earlier cell. The cutoff, half the duplicated debit, and ERP plus the unrecorded consulting...

```python
F = pd.Series([rec.Revenue[2025], d.Debit.sum() / 2, A["ADJ-005"] + x, 
```
*(71 caracteres · ~32 s)*

> 🗣️⌨️ Same line, continuing: the restructuring add-back, and IronBridge.

*(sigue en la misma línea, sin Enter)*

```python
A["ADJ-003"], w.Outstanding_Amount["IronBridge Works"]])
```
*(56 caracteres · ~25 s)*

> 🗣️⌨️ Last lines: their names, and show them.

```python
F.index = ["F1 cutoff", "F2 duplicate", "F3 consulting", "F4 restructuring", "F5 IronBridge"]
F
```
*(95 caracteres · ~42 s)*

> 🖱️ I'm clicking Run on cell eleven, and pointing at the five amounts.

> 🟢 I never add them up. The cutoff is timing, the duplicate is 2024 (twenty twenty-four), consulting and restructuring hit 2025 (twenty twenty-five) EBITDA, and IronBridge hits working capital.

> 🟢 The largest earnings issue is F3: 150,000 (one hundred fifty thousand) against management's EBITDA.

**WHY:** cada hallazgo sale de una celda anterior (nada se tipea a mano). La clasificación por tipo evita la doble contabilización: el corte no cambia el EBITDA, el duplicado es de 2024 y IronBridge es balance.

**EXPECTED RESULT:** `F1 cutoff 148500.0`, `F2 duplicate 42300.0`, `F3 consulting 150000.0`, `F4 restructuring 78000.0`, `F5 IronBridge 312800.0`.

**VERIFY BEFORE CONTINUING:** cinco filas con esos montos.

📘 **What each line does** (para vos, no se lee):

- `A = a.set_index("Adjustment_ID").Amount`: adjustment amount by ID.
- `F = pd.Series([...])`: cutoff (cell 3), duplicate overstatement = half of the two debits (cell 5), ADJ-005 + unrecorded consulting (cells 6–8), ADJ-003 (cell 7), IronBridge balance (cell 9).
- `F.index = [...]`: finding names.
- `F`: shows them.

---

### Bloque 12. Phase 4: informe PDF y validación

**TIME:** 22:20–24:39 (2:19)

**WHAT I DO:** + Code → tipear 1 tramo → Run → señalar la salida → Files: refrescar, descargar el PDF → abrirlo en Firefox y recorrerlo → volver a la pestaña de Colab.

**WHERE:** **+ Code** arriba a la izquierda. Panel Files a la izquierda: botón de refrescar (flecha circular) arriba; tres puntos a la derecha del nombre del PDF. Panel de descargas de Firefox: flecha arriba a la derecha.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell twelve.

> 🗣️⌨️ Cell twelve: build the PDF, then check that revenue nets to zero, the duplicate leaves one posting, every adjustment has a verdict, and the inputs are unchanged.

```python
report()
print(rec.Revenue.sum(), d.Debit.sum() - F.iloc[1], a.verdict.notna().all(), h() == H)
```
*(95 caracteres · ~42 s)*

> 🖱️ I'm clicking Run on cell twelve, and pointing at the output: zero, 42,300 (forty-two thousand three hundred), True and True.

> 🟢 The last True means the four files still match their fingerprints: the evidence was never modified.

> 🖱️ I'm clicking refresh at the top of the Files panel, then the three dots next to the PDF, and Download.

> 🖱️ I'm clicking the PDF in Firefox's downloads panel, at the top right, to open it in a new tab.

> 🖱️ I'm pointing at the executive summary: the same EBITDA and receivables as cells eight and nine.

> 🖱️ I'm scrolling down through the nine adjustment verdicts, the five findings with records, calculation, impact, follow-up and confidence, and the limitations.

> 🖱️ I'm clicking the Colab tab at the top of Firefox, to go back to the notebook.

**WHY:** valida en código lo que pide el prompt (conciliación consistente, duplicado sin doble conteo, ajustes trazables, entradas sin cambios). Después se muestra que el PDF dice lo mismo que el notebook.

**EXPECTED RESULT:** `saved due_diligence_findings_report.pdf` y `0.0 42300.0 True True`. El PDF tiene dos páginas, con las secciones 1 a 7.

**VERIFY BEFORE CONTINUING:** el último valor es `True`. Si Firefox guarda el PDF sin mostrar el panel de descargas: 🖱️ *"I'm clicking the downloads arrow at the top right of Firefox, to open the PDF."*

📘 **What each line does** (para vos, no se lee):

- `report()`: writes `due_diligence_findings_report.pdf` from the notebook variables (function from cell 1).
- `print(...)`: two-year revenue gap (0), valid TechServ posting after removing the duplicate (42,300), every adjustment has a verdict (True), input fingerprints unchanged (True).

---

### Bloque 13. Epilogue

**TIME:** 24:39–25:59 (1:20)

**WHAT I DO:** Cmd + S → File → Download → Download .ipynb → scroll lento hacia arriba, sin tipear. Recién **después** abrís TaskRecorder para detener la grabación.

**WHERE:** menú **File** arriba a la izquierda de Colab. Notebook, desde la celda 12 hasta la celda 1.

**SAY:**

> 🖱️ I'm pressing Command S to save, then choosing File, Download, Download .ipynb, so the notebook sits next to the PDF.

> 🖱️ I'm scrolling up slowly from cell twelve to cell one, to recap.

> 🟢 Defensible 2025 (twenty twenty-five) EBITDA is about 3.1 (three point one) million, not 3.55 (three point five five). The gap is 215,000 (two hundred fifteen thousand) rejected, 174,500 (one hundred seventy-four thousand five hundred) qualified, and 55,000 (fifty-five thousand) of cost left out.

> 🟢 IronBridge needs a 312,800 (three hundred twelve thousand eight hundred) provision, and another 110,600 (one hundred ten thousand six hundred) needs evidence.

> 🟢 The hardest part was separating timing from real errors: neither the cutoff nor the duplicate changes 2025 (twenty twenty-five).

> 🟢 Before signing, I'd request IronBridge's administration report, the ERP invoices, TechServ's credit note, the 2026 (twenty twenty-six) restructuring plan and bank statements. Thanks for watching!

**WHY:** es el resumen ejecutivo: número defendible, riesgos de capital de trabajo, la decisión más difícil y los pedidos de información antes de cerrar.

---

## Si algo sale mal

| Error | Qué decís y hacés |
| ----- | ----------------- |
| Un nombre mal escrito | 🖱️ *"There's a typo in cell N. I'm clicking on that line to fix it, and running the cell again."* |
| `NameError` | 🖱️ *"An earlier cell didn't run. I'm opening the Runtime menu at the top and choosing Run before."* |
| `NameError` dentro de `report()` | Falta correr alguna celda de la 3 a la 11: `report()` usa sus variables. Runtime → Run before. |
| La celda 3 muestra COGS distinto de 0 en 2024 | El CSV subido no es el corregido. Subí el `general_ledger.csv` de `inputs/`. |
| La celda 8 da `KeyError: 2025` | Revisá `rec.SGA_Expenses[2025]`: el año es número, sin comillas. |
| `h() == H` da False | Algún CSV se modificó después de correr la celda 1. No sigas: volvé a subir los cuatro CSV y Runtime → Run all. |
| El PDF no se abre en Firefox | Firefox lo abre con su visor propio. Si lo guarda sin abrir: flecha de descargas arriba a la derecha → clic en el archivo. |
| Hay que volver a correr todo | Los CSV nunca se modifican: alcanza con Runtime → Run all. |

---

## Checklist de archivos y preparación previa

- [ ] Practicá dos veces con cronómetro. [financial_due_diligence.ipynb](financial_due_diligence.ipynb) tiene el código completo para comparar. No lo abras en la grabación.
- [ ] En Colab, creá el notebook **financial_due_diligence** con **la celda 1 escrita** (copiala del bloque 1) y nada más. **No ejecutes nada.**
- [ ] En **Files**, subí los cuatro CSV de [inputs/](inputs/) (los corregidos). Revisá que los nombres no tengan `(1)` y que no quede ningún PDF de una prueba anterior.
- [ ] Cerrá el panel Files antes de empezar: se abre en el bloque 0.
- [ ] **Tools → Settings → AI assistance**: ocultá las funciones de IA.
- [ ] **Tools → Settings → Editor**: si está la opción, desactivá las sugerencias automáticas de código.
- [ ] Firefox: que los PDF se abran en Firefox (Settings → Applications → PDF → Open in Firefox) y que se vea el panel de descargas. Vaciá la lista de descargas.
- [ ] Zoom (`Cmd + +`). Firefox con la ventana 1 en la descripción de la tarea y la ventana 2 en Colab.
- [ ] La carpeta [reference/](reference/) tiene la guía del instructor: **no la abras en el video**.

## Checklist de resultados que deben quedar generados

- [ ] `aging invoices found in GL: 0` y la tabla de dos años (celda 1).
- [ ] `Accounts Receivable 40048470.0 / 0.0` (celda 2).
- [ ] `Revenue -148500 / 148500` y `SGA_Expenses 0 / 55000` (celda 3).
- [ ] INV2024-12-C002 (celda 4) y PO-2024-0892 dos veces (celda 5).
- [ ] `in_gl` True solo en ADJ-002, 003 y 008 (celda 6).
- [ ] `defensible 3102374.0` (celda 8).
- [ ] IronBridge 312,800 / 407 días (celda 9) y tres facturas después de agosto de 2025 (celda 10).
- [ ] Los cinco hallazgos (celda 11) y `0.0 42300.0 True True` (celda 12).
- [ ] Descargados: `due_diligence_findings_report.pdf` y `financial_due_diligence.ipynb`. Armá **Deliverables.zip** con los dos y los cuatro CSV de entrada. Marcá en Studio la opción de archivos generados con IA.

## Checklist de decisiones que debo explicar

- [ ] **Corte de ingresos** = timing: neto cero en dos años; es reclasificación, no ajuste de EBITDA.
- [ ] **Duplicado** = $42,300 (no $84,600), y es de 2024.
- [ ] **Consultoría**: ADJ-005 sin respaldo y $55,000 que faltan en los estados mensuales.
- [ ] **Reestructuración recurrente**: dos cargos en cuatro meses.
- [ ] **Depreciación**: el EBITDA ya la excluye (EBITDA − D&A = EBIT).
- [ ] **Calificados** (ADJ-004, 007, 009): qué evidencia falta.
- [ ] **IronBridge**: previsión total; Keystone y Cascade sin evidencia suficiente.
- [ ] **Limitaciones**: no hay cobros en el libro mayor; el aging no se puede conciliar.
- [ ] **Sin doble conteo**: los cinco montos son de tipos distintos.
- [ ] **Entradas intactas**: `h() == H`.
