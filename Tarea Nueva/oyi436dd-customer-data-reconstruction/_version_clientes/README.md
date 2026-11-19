# oyi436dd — Customer Data Reconstruction

Guion para grabar la tarea **oyi436dd** con la idea nueva: **reconstruir y validar una base de clientes** con **Python y pandas** en **Google Colab**, con **Firefox** como aplicación de apoyo. Se graba en una sola toma.

**Duración estimada: ~27 minutos** (máximo absoluto: 30).

**Archivos de entrada** (sintéticos, con problemas reales):

| Archivo | Filas | Problemas que tiene |
| ------- | ----- | ------------------- |
| `customers.csv` | 542 | 42 registros duplicados de 500 personas, con emails en mayúsculas o con espacios, teléfonos en 4 formatos, 30 emails vacíos y 11 personas con ciudades en conflicto |
| `orders.csv` | 2.419 | 57 filas exactamente duplicadas, 48 pedidos con una versión vieja (`pending`) y una nueva, y 14 pedidos de clientes que no existen |
| `customer_activity.csv` | 5.420 | 114 eventos duplicados, 31 de clientes que no existen y eventos anteriores a la fecha de alta |

**Los 6 pasos de la idea aprobada y dónde se cumplen:**

| Paso aprobado | Fase | Celda |
| ------------- | ---- | ----- |
| 1. Inspeccionar y perfilar los tres datasets | 2 | 1 (armada) |
| 2. Resolver identidades duplicadas y conflictos entre clientes | 3 | 2 (se tipea) |
| 3. Reconciliar transacciones duplicadas | 4 | 3 (se tipea) |
| 4. Crear variables de comportamiento histórico | 6 | 5 (armada) |
| 5. Validar relaciones y cardinalidad de los joins | 5 y 7 | 4 y 6 (se tipean) |
| 6. Exportar el dataset consolidado y el reporte de excepciones | 8 | 7 (armada) |

**Criterios de Slack que cubre:** los archivos de entrada se modifican materialmente (los tres se reescriben, sin perder los valores originales del archivo de clientes), el impacto se mide en dólares (11.580 inflados por duplicados, 1.316 sin cliente) y cada decisión se justifica comparándola con la alternativa incorrecta.

---

## Cómo leer este guion

Cada fase tiene:

- **TIME:** cuándo empieza, cuándo termina y cuánto dura.
- **ON SCREEN:** qué tenés que hacer en pantalla, en orden.
- **SAY:** lo que decís, en inglés, intercalado con el código:
  - 🖱️ = lo decís **mientras hacés** la acción con el mouse: qué, dónde y por qué.
  - 🗣️⌨️ = lo decís **con las manos fuera del teclado**, y **después** tipeás el bloque de abajo **en silencio**. Cada bloque marca sus caracteres y su tiempo.
  - 🟢 = lo decís con el mouse quieto: la decisión, o qué muestra el resultado.
- **WHY:** el razonamiento técnico, para vos. **Ya está dentro de lo que decís**; no se lee aparte.
- **EXPECTED RESULT:** qué tiene que aparecer y cómo saber que salió bien.
- 📘 = la explicación de cada línea, en inglés. Es para vos: **no se lee**.

---

## Estrategia de tiempo y tipeo

**Por qué 27 minutos son reales y no tiempo de lectura:** la estimación suma la narración (130 palabras por minuto), el tipeo en silencio (175 caracteres por minuto) y unos 20 segundos de navegación por celda. Con ese mismo método, la tarea k3a13c10 dio 75 minutos estimados y vos mediste 75.

| | Cantidad | Tiempo |
| - | -------- | ------ |
| Tipeo en vivo (4 celdas + conclusiones) | 1.440 caracteres | ~8,2 min (~9,6 a 150 car./min) |
| Narración | ~2.120 palabras | ~16,3 min |
| Navegación y ejecución | 8 celdas + Files | ~2,5 min |
| **Total** | | **~27 min** (~28,5 a 150 car./min) |

**Tipeo: ~30% del video.**

**Qué celdas van armadas y por qué:**

| Celda | Estado | Por qué |
| ----- | ------ | ------- |
| 1. Carga y perfil | **Armada** | Es mecánica: leer y contar. Lo que importa es interpretar el perfil. |
| 2. Identidades | Se tipea | Es la decisión central: qué clave identifica a una persona. |
| 3. Pedidos duplicados | Se tipea | Decisión: qué versión de un pedido es la verdadera. |
| 4. Joins y cardinalidad | Se tipea | Decisión: cómo unir sin multiplicar filas. |
| 5. Variables de comportamiento | **Armada** | Son agregaciones estándar. Se explican señalando cada línea. |
| 6. Validación de totales | Se tipea | Es la prueba de que nada se perdió. |
| 7. Excepciones y exportación | **Armada** | Es mecánica: juntar tablas y guardar archivos. |

**Reglas de tipeo (las mismas que en k3a13c10):**

1. **Nunca hablar y tipear al mismo tiempo.** Frase 🗣️⌨️ con las manos quietas → bloque en silencio.
2. **Ningún tramo de tipeo pasa de 45 segundos.** El bloque más largo tiene 101 caracteres (~35 s; ~40 s a 150 car./min). La línea más larga está partida en dos tramos, con una frase en el medio y **sin Enter**.
3. **Nada de tipeo extra:** ni comentarios, ni `print` de prueba.
4. **No se usa autocompletado.** Si aparece una caja de sugerencias, Escape.

---

## Pendientes antes de grabar

| Tema | Qué hacer |
| ---- | --------- |
| **Origen de los CSV** | Los generé yo, Claude, con un script de Python, **no con Gemini**. Decí "generated with AI", que es cierto, y marcá en Studio la opción de archivos generados con IA. Si preferís generarlos con Gemini, pasámelos: todos los números del guion cambian y hay que recalcularlos. |
| **Límite de tipeo** | No sé el límite de esta tarea. En k3a13c10 era 35%. El guion da ~30%. Si las guías dicen menos, avisame. |
| **Notebook** | Armalo antes de grabar como dice la checklist: celdas 1, 5 y 7 con el código; celdas 2, 3, 4 y 6 vacías. |
| **Archivos de la idea vieja** | Los moví a `_idea_anterior/` (orders, order_items, products, el notebook y el README viejo). No van en la entrega. |

---

## La regla del mouse y del teclado

1. El mouse **solo se mueve con una frase 🖱️**. Mientras tipeás, soltalo.
2. Al terminar una acción, el cursor queda **quieto en el margen derecho**.
3. **Primero la frase, después el movimiento o el tipeo.**
4. **Repetí el número de celda al menos una vez por minuto.** Las frases ya lo hacen.
5. Frases comodín para lo que no está en el guion:
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

> 🟢 I will be beginning my task soon. The goal is to rebuild a reliable customer base from three messy sources, so that each real person appears once, with their full order and activity history, and every record I can't resolve is documented instead of silently dropped.

> 🟢 The inputs are customers, with one row per customer record; orders, with one row per order version; and customer_activity, with logins, page views, cart adds, and support tickets.

> 🟢 My plan: profile the three files, resolve duplicate identities, reconcile duplicate orders, validate the join cardinality, build behavioral features, reconcile the totals, and export a consolidated dataset with an exception report. I expect one row per real customer, totals that match to the cent, and a short list of exceptions with their reasons.

> 🖱️ I'm clicking the yellow minimize button at the top left of this window, to put the task description away.

> 🖱️ I'm clicking the Firefox icon in the Dock, on the right of the screen, and choosing the second window: my Colab notebook.

> 🖱️ I'm clicking the folder icon in Colab's left sidebar, to open the Files panel and check the inputs.

> 🖱️ I'm pointing at the three CSV files in the panel. They're synthetic, generated with AI, and the originals stay on my Desktop, because at the end this notebook rewrites these copies.

> 🖱️ I'm clicking the same folder icon to close the panel, so the notebook gets the full width.

**WHY:** el revisor tiene que saber desde el principio qué significa "bien": una fila por persona, totales que cierran y excepciones documentadas.

**EXPECTED RESULT:** el notebook con las celdas 1, 5 y 7 llenas y las 2, 3, 4 y 6 vacías. En Files, los tres CSV.

---

### Fase 2. Inspección y perfil

**TIME:** 2:00–5:00 (3 min)

**ON SCREEN:** Colab, celda 1 (armada). Señalar las líneas, Run, señalar la salida.

**Celda 1 (armada antes de grabar, no se tipea):**

```python
import pandas as pd
c = pd.read_csv("customers.csv", parse_dates=["signup_date"])
o = pd.read_csv("orders.csv", parse_dates=["order_date", "updated_at"])
a = pd.read_csv("customer_activity.csv", parse_dates=["event_date"])
for name, d in {"customers": c, "orders": o, "activity": a}.items():
    print(name, d.shape, "duplicate rows:", d.duplicated().sum(), "nulls:", d.isna().sum().sum())
print("unique order_id:", o.order_id.nunique(), "| orders without customer:", (~o.customer_id.isin(c.customer_id)).sum())
c.head()
```

**SAY:**

> 🟢 Phase one: profiling the three files.

> 🖱️ I'm pointing at cell one, at the top of the notebook. I prepared this cell before recording, because loading and counting are routine, and I'd rather spend the time on the decisions.

> 🖱️ I'm pointing at lines two to four of cell one: the three read_csv calls, with the date columns parsed as real dates, because later I compare orders and events against signup dates.

> 🖱️ I'm pointing at the loop in cell one: for each file, the shape, the fully duplicated rows, and the missing values. Then I compare row count with unique order IDs, and check orders whose customer doesn't exist.

> 🖱️ I'm clicking the Run button on the left of cell one. The profile prints right below it.

> 🖱️ I'm pointing at the three profile lines under cell one.

> 🟢 Customers has 542 records and 30 missing values, all in email. Orders has 57 exact duplicate rows, and activity has 114.

> 🖱️ I'm pointing at the next line: 2,314 unique order IDs.

> 🟢 Orders has 2,419 rows but only 2,314 IDs. 57 extra rows are exact copies, so 48 more are different versions of the same order. That's a reconciliation problem, not just duplicates. And 14 orders point to customers that don't exist.

> 🖱️ I'm moving the mouse down the phone and email columns of the table under cell one.

> 🟢 Phones come in at least three formats, and one email is empty. So exact matching on raw values would miss duplicates; I need to normalize first.

**WHY:** comparar filas con IDs únicos separa "copias exactas" de "versiones distintas del mismo pedido", que se resuelven de forma distinta. Ver los formatos antes de buscar duplicados evita una clave de matching que falle en silencio.

**EXPECTED RESULT:**

- `customers (542, 7) duplicate rows: 0 nulls: 30`
- `orders (2419, 6) duplicate rows: 57 nulls: 0`
- `activity (5420, 3) duplicate rows: 114 nulls: 0`
- `unique order_id: 2314 | orders without customer: 14`
- Tabla: `C0002` con `(513) 390-6167`, `C0003` con `584.091.8461` y el email con espacios, `C0005` con email `NaN`.

📘 **What each line does** (para vos, no se lee):

- `import pandas as pd`: loads pandas as `pd`.
- `c = pd.read_csv("customers.csv", parse_dates=["signup_date"])`: reads the customers, with `signup_date` as a real date.
- `o = pd.read_csv("orders.csv", parse_dates=["order_date", "updated_at"])`: reads the orders, with both dates parsed.
- `a = pd.read_csv("customer_activity.csv", parse_dates=["event_date"])`: reads the activity events.
- `for name, d in {...}.items():`: loops over the three tables with their names.
- `print(name, d.shape, "duplicate rows:", d.duplicated().sum(), "nulls:", d.isna().sum().sum())`: rows and columns, fully duplicated rows and total missing values.
- `print("unique order_id:", o.order_id.nunique(), "| orders without customer:", (~o.customer_id.isin(c.customer_id)).sum())`: distinct order IDs, and orders whose `customer_id` isn't in customers (`~` means "not").
- `c.head()`: the first 5 customers, to see the formats.

---

### Fase 3. Resolver identidades duplicadas

**TIME:** 5:00–10:00 (5 min)

**ON SCREEN:** Colab, celda 2 (vacía). Clic adentro, tipear 7 bloques, Run, señalar la salida.

**SAY:**

> 🖱️ I'm clicking inside cell two, the empty cell below the profile.

> 🟢 Phase two: identity resolution. The question is which key identifies a real person.

> 🗣️⌨️ On the first line of cell two, I'll normalize the email: strip the spaces and lowercase it.

```python
c["email_n"] = c.email.str.strip().str.lower()
```
*(46 caracteres · ~16 s)*

> 🗣️⌨️ Next line of cell two: the phone with only its digits, so all formats become the same.

```python
c["phone_n"] = c.phone.str.replace(r"\D", "", regex=True)
```
*(57 caracteres · ~20 s)*

> 🗣️⌨️ Now, still in cell two: I sort by signup date and give each phone the oldest customer ID as master ID. The oldest record survives, because it holds the real signup date.

```python
c = c.sort_values("signup_date")
c["master_id"] = c.groupby("phone_n").customer_id.transform("first")
```
*(101 caracteres · ~35 s)*

> 🗣️⌨️ Next line of cell two: I compare three keys. First half: duplicates found with the raw email, and with the normalized email.

```python
print(c.email.dropna().duplicated().sum(), c.email_n.dropna().duplicated().sum(), 
```
*(82 caracteres · ~28 s)*

> 🗣️⌨️ Same line, second half: the records merged by phone.

```python
len(c) - c.master_id.nunique())
```
*(31 caracteres · ~11 s)*

> 🗣️⌨️ Still in cell two: a group per master ID, and the records whose group has more than one city.

```python
g = c.groupby("master_id")
conf = c[g.city.transform("nunique") > 1]
```
*(68 caracteres · ~23 s)*

> 🗣️⌨️ Last two lines of cell two: I check that no phone group has two different emails, count the conflicts, and show two of them.

```python
print(g.email_n.nunique().max(), conf.master_id.nunique())
conf.sort_values("master_id").head(4)
```
*(96 caracteres · ~33 s)*

> 🖱️ I'm clicking the Run button on the left of cell two. Two printed lines and a table appear below it.

> 🖱️ I'm pointing at the first printed line under cell two: 0, 31, and 42.

> 🟢 The raw email finds zero duplicates, so exact matching would have missed every single one. The normalized email finds 31, but it can't see the records with an empty email. The phone finds all 42, because it's never empty.

> 🖱️ I'm pointing at the second line: 1 and 11.

> 🟢 The 1 is my safety check: no phone group has two different emails, so the phone isn't merging different people. And 11 people have records with different cities.

> 🖱️ I'm pointing at the two Maria Molina rows in the table, at the city column.

> 🟢 Same person, same email and phone, but Miami in one record and Boston in the other. I can't know which is current, so I keep the master record's city and send these to the exception report, instead of guessing.

**WHY:**

- El email crudo da 0: es la prueba de que normalizar era necesario.
- El email normalizado da 31 y no 42: muestra por qué el email solo no alcanza.
- El `1` demuestra que el teléfono no fusiona personas distintas.
- Elegir el registro más viejo como master es una regla de supervivencia explícita y reproducible.

**EXPECTED RESULT:**

- Primera línea: `0 31 42`.
- Segunda línea: `1 11`.
- Tabla de 4 filas: `C0180` y `C0061` (Maria Molina, Miami / Boston, master `C0061`); `C0016` y `C0145` (James Lopez, Austin / Miami, master `C0145`).

📘 **What each line does** (para vos, no se lee):

- `c["email_n"] = c.email.str.strip().str.lower()`: the email without surrounding spaces and in lowercase. Missing emails stay missing.
- `c["phone_n"] = c.phone.str.replace(r"\D", "", regex=True)`: removes every non-digit (`\D`), so all phone formats match.
- `c = c.sort_values("signup_date")`: oldest records first.
- `c["master_id"] = c.groupby("phone_n").customer_id.transform("first")`: every record gets the ID of the oldest record with the same phone.
- `print(c.email.dropna().duplicated().sum(), c.email_n.dropna().duplicated().sum(), len(c) - c.master_id.nunique())`: duplicates found by raw email, by normalized email, and records merged by phone. Se tipea en una sola línea, en dos tramos (no apretes Enter en el medio).
- `g = c.groupby("master_id")`: the records grouped by person.
- `conf = c[g.city.transform("nunique") > 1]`: the records of people with more than one city.
- `print(g.email_n.nunique().max(), conf.master_id.nunique())`: the most distinct emails in one person (must be 1) and the number of people with a city conflict.
- `conf.sort_values("master_id").head(4)`: shows two conflicts, with both records of each.

---

### Fase 4. Reconciliar pedidos duplicados

**TIME:** 10:00–13:00 (3 min)

**ON SCREEN:** Colab, celda 3 (vacía). Clic adentro, tipear 3 bloques, Run, señalar la salida.

**SAY:**

> 🖱️ I'm clicking inside cell three, below the identity table.

> 🟢 Phase three: duplicate orders. There are two different problems: exact copies, and several versions of the same order.

> 🗣️⌨️ On the first line of cell three, I save the total amount, to measure the impact in dollars. Then I drop the exact copies and count what's left.

```python
total = o.amount.sum()
o = o.drop_duplicates()
n = len(o)
```
*(57 caracteres · ~20 s)*

> 🗣️⌨️ Next line of cell three: for orders with several versions, I keep the latest updated_at. Keeping the first row would keep stale statuses.

```python
o = o.sort_values("updated_at").drop_duplicates("order_id", keep="last")
```
*(72 caracteres · ~25 s)*

> 🗣️⌨️ Last two lines of cell three: the row counts and the inflated dollars, and the status of the surviving orders.

```python
print(n, len(o), round(total - o.amount.sum(), 2))
o.status.value_counts()
```
*(74 caracteres · ~25 s)*

> 🖱️ I'm clicking the Run button on the left of cell three. A printed line and the status counts appear below it.

> 🖱️ I'm pointing at the printed line under cell three: 2,362, 2,314, and 11,580.09.

> 🟢 Dropping copies leaves 2,362 rows; keeping the latest version leaves 2,314, exactly the number of unique IDs from cell one. And the duplicates inflated revenue by 11,580 dollars.

> 🖱️ I'm moving the mouse down the status counts below.

> 🟢 Completed, cancelled, and refunded, and no pending. That confirms the old versions were the pending snapshots: every order that survived has its final status.

**WHY:** las copias exactas y las versiones son problemas distintos. `updated_at` es la evidencia de cuál versión es la vigente. Que no quede ningún `pending` valida la regla: con `keep="first"` habrían sobrevivido los 48 estados viejos.

**EXPECTED RESULT:**

- `2362 2314 11580.09`
- `completed 2097`, `cancelled 165`, `refunded 52`. **No aparece `pending`.**

📘 **What each line does** (para vos, no se lee):

- `total = o.amount.sum()`: the total amount before cleaning, to measure the impact.
- `o = o.drop_duplicates()`: removes rows identical in every column.
- `n = len(o)`: the rows left after removing copies.
- `o = o.sort_values("updated_at").drop_duplicates("order_id", keep="last")`: sorts by last update and keeps the latest version of each order.
- `print(n, len(o), round(total - o.amount.sum(), 2))`: rows after each step and the dollars removed.
- `o.status.value_counts()`: how many orders have each final status.

---

### Fase 5. Validar relaciones y cardinalidad de los joins

**TIME:** 13:00–17:00 (4 min)

**ON SCREEN:** Colab, celda 4 (vacía). Clic adentro, tipear 5 bloques, Run, señalar la salida.

**SAY:**

> 🖱️ I'm clicking inside cell four, below the status counts.

> 🟢 Phase four: connecting orders and activity to the resolved customers, and proving that the joins don't multiply rows.

> 🗣️⌨️ On the first lines of cell four: a lookup from each customer ID to its master ID, applied to the orders.

```python
m = c.set_index("customer_id").master_id
o["master_id"] = o.customer_id.map(m)
```
*(78 caracteres · ~27 s)*

> 🗣️⌨️ Next, still in cell four: the activity without its duplicate events, mapped to master IDs too.

```python
a = a.drop_duplicates()
a["master_id"] = a.customer_id.map(m)
```
*(61 caracteres · ~21 s)*

> 🗣️⌨️ Next line of cell four: one row per real person, the master records, indexed by master ID.

```python
cust = c[c.customer_id == c.master_id].set_index("master_id")
```
*(61 caracteres · ~21 s)*

> 🗣️⌨️ Now the validated join: validate m to 1 makes pandas raise an error if a master ID appeared twice. And the wrong alternative, joining orders directly with activity, for comparison.

```python
j = o.join(cust.city, on="master_id", validate="m:1")
bad = o.merge(a, on="master_id")
```
*(86 caracteres · ~29 s)*

> 🗣️⌨️ Last line of cell four: the row counts, plus the orders and events with no customer.

```python
print(len(o), len(j), len(bad), o.master_id.isna().sum(), a.master_id.isna().sum())
```
*(83 caracteres · ~28 s)*

> 🖱️ I'm clicking the Run button on the left of cell four. One line prints below it.

> 🖱️ I'm pointing at the first two numbers under cell four: 2,314 and 2,314.

> 🟢 The validated join keeps exactly 2,314 orders, and it didn't raise an error, so each master ID is unique on the customer side.

> 🖱️ I'm pointing at the third number: 26,047.

> 🟢 Joining orders and activity row by row gives 26,047 rows, about eleven times the orders. Any revenue summed after that join would be wrong. That's why I'll aggregate each table per customer first, and join the aggregates.

> 🖱️ I'm pointing at the last two numbers: 14 and 31.

> 🟢 14 orders and 31 events belong to customer IDs that don't exist. I keep them out of the customer features, but I don't delete them: they go to the exception report.

**WHY:** `validate="m:1"` convierte un supuesto ("cada cliente aparece una vez") en un control que falla si no se cumple. El join directo de 26.047 filas es la alternativa incorrecta más común: muestra en números por qué se agrega antes de unir.

**EXPECTED RESULT:** `2314 2314 26047 14 31`. Si aparece `MergeError`, la celda 2 no generó un master único: volvé a ejecutar las celdas 2 a 4 en orden.

📘 **What each line does** (para vos, no se lee):

- `m = c.set_index("customer_id").master_id`: a lookup from every customer ID to its master ID.
- `o["master_id"] = o.customer_id.map(m)`: the master ID of each order. Unknown IDs get `NaN`.
- `a = a.drop_duplicates()`: removes duplicate events.
- `a["master_id"] = a.customer_id.map(m)`: the master ID of each event.
- `cust = c[c.customer_id == c.master_id].set_index("master_id")`: only the surviving record of each person, one row per master ID.
- `j = o.join(cust.city, on="master_id", validate="m:1")`: joins each order with its customer's city. `validate="m:1"` raises an error if a master ID repeats on the right side.
- `bad = o.merge(a, on="master_id")`: the wrong join, orders × events, to show the fan-out.
- `print(len(o), len(j), len(bad), o.master_id.isna().sum(), a.master_id.isna().sum())`: orders, rows after the valid join, rows after the wrong join, orphan orders and orphan events.

---

### Fase 6. Variables de comportamiento histórico

**TIME:** 17:00–19:30 (2,5 min)

**ON SCREEN:** Colab, celda 5 (armada). Señalar las líneas, Run, señalar la tabla.

**Celda 5 (armada antes de grabar, no se tipea):**

```python
early = a.event_date < a.master_id.map(cust.signup_date)
done = o[(o.status == "completed") & o.master_id.notna()]
f = done.groupby("master_id").agg(orders=("order_id", "size"), spent=("amount", "sum"), last_order=("order_date", "max"))
act = a[~early].groupby("master_id").agg(events=("event_type", "size"), last_seen=("event_date", "max"))
d = cust.join([f, act]).fillna({"orders": 0, "spent": 0, "events": 0})
ref = pd.Timestamp("2025-12-31")
d["aov"] = (d.spent / d.orders).round(2)
d["recency_days"] = (ref - d.last_order).dt.days
d["inactive_90"] = (ref - d.last_seen).dt.days > 90
print("events before signup:", early.sum())
d[["orders", "spent", "aov", "events", "recency_days"]].describe().round(1)
```

**SAY:**

> 🟢 Phase five: behavioral features, one row per real customer.

> 🖱️ I'm pointing at cell five. I prepared it before recording, because these are standard aggregations; what matters is the rules inside them.

> 🖱️ I'm pointing at the first line of cell five: an event before the master's signup date is impossible, so I flag it instead of counting it as activity.

> 🖱️ I'm pointing at the second line: only completed orders count as spending, because cancelled and refunded orders aren't revenue.

> 🖱️ I'm moving the mouse over the two agg lines: orders, spending and last order per customer, and events and last activity per customer. Each table is aggregated first, as cell four showed.

> 🖱️ I'm pointing at the join line: customers with no orders get zero, not missing, because zero orders is a real value.

> 🖱️ I'm clicking the Run button on the left of cell five. The summary table appears below it.

> 🖱️ I'm pointing at the printed line under cell five: 20 events before signup.

> 🟢 20 events are dated before their customer existed, so they're excluded and reported.

> 🖱️ I'm pointing at the count row of the table: 500 in orders, but 483 in aov and recency_days.

> 🟢 500 customers, one per real person. 17 have no completed order, so they have no average order value and no recency. That's correct, not a gap.

> 🖱️ I'm pointing at the 50% row: 4 orders, about 406 dollars, and 58 days since the last order.

> 🟢 The typical customer bought four times, spent about 400 dollars, and last ordered two months before year end.

**WHY:** las reglas (eventos antes del alta, solo pedidos completados, cero en lugar de vacío) son decisiones de negocio y se explican aunque el código esté armado. El `count` de 483 confirma que el `fillna` solo rellenó lo que debía.

**EXPECTED RESULT:**

- `events before signup: 20`
- `count`: 500 en `orders`, `spent` y `events`; 483 en `aov` y `recency_days`.
- Fila `50%`: orders 4,0 · spent 406,4 · aov 104,6 · events 10,0 · recency_days 58,0.

📘 **What each line does** (para vos, no se lee):

- `early = a.event_date < a.master_id.map(cust.signup_date)`: True for events dated before their customer's signup.
- `done = o[(o.status == "completed") & o.master_id.notna()]`: completed orders with a known customer.
- `f = done.groupby("master_id").agg(...)`: per customer, the number of orders, total spent and last order date.
- `act = a[~early].groupby("master_id").agg(...)`: per customer, the valid events and the last activity date.
- `d = cust.join([f, act]).fillna({...})`: one row per customer with both feature sets. No orders or events means 0.
- `ref = pd.Timestamp("2025-12-31")`: the reference date, the end of the data period.
- `d["aov"] = (d.spent / d.orders).round(2)`: average order value.
- `d["recency_days"] = (ref - d.last_order).dt.days`: days since the last completed order.
- `d["inactive_90"] = (ref - d.last_seen).dt.days > 90`: no activity in the last 90 days.
- `print("events before signup:", early.sum())`: how many events were excluded.
- `d[[...]].describe().round(1)`: count, mean, quartiles and max of the main features.

---

### Fase 7. Validación de totales

**TIME:** 19:30–21:30 (2 min)

**ON SCREEN:** Colab, celda 6 (vacía). Clic adentro, tipear 2 bloques, Run, señalar la salida.

**SAY:**

> 🖱️ I'm clicking inside cell six, below the feature summary.

> 🟢 Phase six: proving that the consolidated table didn't lose or double any money.

> 🗣️⌨️ On the first line of cell six: one row per customer, and the spending in my table against the completed orders it comes from.

```python
print(d.index.is_unique, round(d.spent.sum(), 2), round(done.amount.sum(), 2))
```
*(78 caracteres · ~27 s)*

> 🗣️⌨️ Second line of cell six: the dollars in orphan orders, the inactive customers, and the customers with no completed order.

```python
print(round(o[o.master_id.isna()].amount.sum(), 2), d.inactive_90.sum(), (d.orders == 0).sum())
```
*(95 caracteres · ~33 s)*

> 🖱️ I'm clicking the Run button on the left of cell six. Two lines print below it.

> 🖱️ I'm pointing at the first line under cell six: True, 227,115.94, and 227,115.94.

> 🟢 Each customer appears once, and the two totals match to the cent, so the joins kept every completed dollar.

> 🖱️ I'm pointing at the second line: 1,315.58, 64, and 17.

> 🟢 1,316 dollars sit in the 14 orphan orders and can't be attributed to anyone. 64 customers have been inactive for more than 90 days, and 17 never completed an order.

**WHY:** cuadrar al centavo es la prueba de que la agregación y los joins no perdieron ni duplicaron dinero. El dinero huérfano se cuantifica para que el negocio decida si vale la pena investigarlo.

**EXPECTED RESULT:**

- `True 227115.94 227115.94`
- `1315.58 64 17`

📘 **What each line does** (para vos, no se lee):

- `print(d.index.is_unique, round(d.spent.sum(), 2), round(done.amount.sum(), 2))`: one row per customer, and the spending total in the final table vs. in the source orders.
- `print(round(o[o.master_id.isna()].amount.sum(), 2), d.inactive_90.sum(), (d.orders == 0).sum())`: the dollars of orphan orders, inactive customers, and customers with no completed orders.

---

### Fase 8. Reporte de excepciones y exportación

**TIME:** 21:30–23:30 (2 min)

**ON SCREEN:** Colab, celda 7 (armada). Señalar las líneas, Run, abrir Files, señalar los archivos, cerrar Files.

**Celda 7 (armada antes de grabar, no se tipea):**

```python
x = pd.concat([conf[["customer_id", "master_id"]].assign(issue="city_conflict"),
               o[o.master_id.isna()][["customer_id", "order_id"]].assign(issue="orphan_order"),
               a[a.master_id.isna()][["customer_id", "event_date"]].assign(issue="orphan_event"),
               a[early][["customer_id", "event_date"]].assign(issue="event_before_signup")])
x.to_csv("exceptions_report.csv", index=False)
d.to_csv("customers_consolidated.csv")
c.to_csv("customers.csv", index=False)
o.to_csv("orders.csv", index=False)
a.to_csv("customer_activity.csv", index=False)
x.issue.value_counts()
```

**SAY:**

> 🟢 Phase seven: the exception report and the exports.

> 🖱️ I'm pointing at the concat in cell seven, prepared before recording: one table with every unresolved record, its ID, and its reason, so nothing disappears without a trace.

> 🖱️ I'm pointing at the to_csv lines of cell seven: the consolidated customers, and the three input files rewritten. Customers keeps the original email and phone next to the normalized ones and the master ID, so every merge can be audited. Orders and activity are saved without duplicates and with their master ID.

> 🖱️ I'm clicking the Run button on the left of cell seven. The exception counts appear below it.

> 🖱️ I'm moving the mouse down the counts under cell seven.

> 🟢 31 orphan events, 22 records with a city conflict, 20 events before signup, and 14 orphan orders: 87 exceptions, each with its reason.

> 🖱️ I'm clicking the folder icon in the left sidebar, to open the Files panel.

> 🖱️ I'm pointing at customers_consolidated and exceptions_report, the two new files.

> 🖱️ I'm pointing at customers, orders, and customer_activity: the same names, but now cleaned and linked by master ID.

> 🖱️ I'm clicking the folder icon again to close the panel.

**WHY:** las excepciones se documentan con su motivo en vez de borrarse. Así cada fila descartada se puede rastrear. Reescribir los archivos de entrada deja la corrección aplicada en la fuente (criterio de Slack), y los originales quedan en el Escritorio y en `original/` del ZIP.

**EXPECTED RESULT:**

- `orphan_event 31`, `city_conflict 22`, `event_before_signup 20`, `orphan_order 14`.
- En Files, 5 archivos: `customer_activity.csv` (5.306 filas), `customers.csv` (542 filas, 10 columnas), `customers_consolidated.csv` (500 filas), `exceptions_report.csv` (87 filas) y `orders.csv` (2.314 filas). Si no aparecen, tocá refresh y decí: *"I'm clicking refresh at the top of the Files panel, to show the new files."*

📘 **What each line does** (para vos, no se lee):

- `x = pd.concat([...])`: stacks four exception lists, each with an `issue` label: city conflicts, orphan orders, orphan events and events before signup.
- `x.to_csv("exceptions_report.csv", index=False)`: saves the exception report.
- `d.to_csv("customers_consolidated.csv")`: saves one row per customer with all features. The index is the master ID, so it's kept.
- `c.to_csv("customers.csv", index=False)`: rewrites customers with `email_n`, `phone_n` and `master_id`. The original email and phone stay.
- `o.to_csv("orders.csv", index=False)`: rewrites orders, deduplicated, with `master_id`.
- `a.to_csv("customer_activity.csv", index=False)`: rewrites activity, deduplicated, with `master_id`.
- `x.issue.value_counts()`: the number of exceptions per reason.

---

### Fase 9. Conclusiones

**TIME:** 23:30–25:00 (1,5 min)

**ON SCREEN:** Colab, + Text abajo de todo, tipear 4 bloques, clic afuera, Cmd + S.

**SAY:**

> 🖱️ I'm clicking plus Text at the top left, to add a text cell at the end of the notebook, for the conclusions.

> 🗣️⌨️ In the text cell, the title and the identity result.

```markdown
## Summary
- 542 records are 500 customers; 11 have conflicting cities.
```
*(71 caracteres · ~24 s)*

> 🗣️⌨️ Second line of the text cell: the order reconciliation in dollars.

```markdown
- Duplicate orders inflated revenue by $11,580.
```
*(47 caracteres · ~16 s)*

> 🗣️⌨️ Third line: the validation and what remains unresolved.

```markdown
- Totals match to the cent; $1,316 in 14 orders has no customer.
```
*(64 caracteres · ~22 s)*

> 🗣️⌨️ Last line: the AI declaration.

```markdown
- Input files generated with AI.
```
*(32 caracteres · ~11 s)*

> 🖱️ I'm clicking on the empty area below the text cell, to show it formatted.

> 🖱️ I'm pressing Command and S to save the notebook; the save message appears at the bottom left.

**EXPECTED RESULT:** la celda de texto con el título y cuatro viñetas, formateada.

---

### Fase 10. Epilogue

**TIME:** 25:00–27:00 (2 min)

**ON SCREEN:** Colab. Scroll lento hacia arriba. Sin tipear. Recién **después** del epilogue abrís TaskRecorder para detener la grabación.

**SAY:**

> 🖱️ I'm scrolling up slowly through the notebook, from the conclusions back to cell one.

> 🟢 The key decision was the identity key. Raw email found nothing, normalized email missed the records without one, and the phone found all 42 duplicates. I only trusted it after checking that no phone group had two different emails. For orders, I used updated_at as the evidence of the current version, and the absence of pending statuses confirmed it.

> 🟢 To verify quality, I turned assumptions into checks: validate m to 1 on the join, a comparison against the 26,000-row wrong join, one row per customer, and totals that match to the cent. And every record I couldn't resolve is in the exception report with its reason, not deleted.

> 🟢 The limitations: matching by phone assumes people don't share phones, which would need a fuzzy name check in a real system. The city conflicts need a source of truth, like the latest shipping address. And the data is synthetic and covers one year. Thanks for watching!

**WHY:** no repite los pasos: cuenta las decisiones, cómo se verificaron y qué falta.

---

## Si algo sale mal

| Error | Qué decís y hacés |
| ----- | ----------------- |
| Un nombre mal escrito | 🖱️ *"There's a typo in cell N. I'm clicking on that line to fix it, and running the cell again."* |
| `MergeError` en la celda 4 | 🖱️ *"The validation caught a repeated master ID, so cell two didn't run as expected. I'm running cells two to four again in order."* |
| `NameError` | 🖱️ *"An earlier cell didn't run. I'm opening the Runtime menu at the top and choosing Run before."* |
| Hay que repetir todo después de la celda 7 | 🖱️ *"The inputs were already rewritten, so I'm uploading the originals from my Desktop again in the Files panel."* |
| La celda 3 se ejecutó dos veces | No pasa nada: el resultado no cambia, pero el `print` muestra `2314 2314 0.0`. Decí: *"I ran cell three twice; the second run finds nothing left to remove."* |

---

## Resumen de tiempos

| Fase | Celda | TIME | Duración |
| ---- | ----- | ---- | -------- |
| 1. Opening | — | 0:00–2:00 | 2 min |
| 2. Inspección y perfil | 1 (armada) | 2:00–5:00 | 3 min |
| 3. Identidades | 2 | 5:00–10:00 | 5 min |
| 4. Pedidos duplicados | 3 | 10:00–13:00 | 3 min |
| 5. Joins y cardinalidad | 4 | 13:00–17:00 | 4 min |
| 6. Variables de comportamiento | 5 (armada) | 17:00–19:30 | 2,5 min |
| 7. Validación de totales | 6 | 19:30–21:30 | 2 min |
| 8. Excepciones y exportación | 7 (armada) | 21:30–23:30 | 2 min |
| 9. Conclusiones | texto | 23:30–25:00 | 1,5 min |
| 10. Epilogue | — | 25:00–27:00 | 2 min |
| **Total** | | | **~27 min** |

**Margen:** 3 minutos hasta 30. **Medilo:** hacé una práctica completa con cronómetro. Si pasa de 28 minutos, recortá **palabras** de las 🟢 (nunca las 🖱️ ni las 🗣️⌨️).

---

## Checklist

**Antes de grabar**

- [ ] Practicá dos veces con cronómetro. `customer_reconstruction.ipynb` tiene el código completo para comparar.
- [ ] En Colab, creá el notebook **customer_reconstruction** con **7 celdas de código**:
  - celdas **1, 5 y 7**: pegá el código de la fase correspondiente;
  - celdas **2, 3, 4 y 6**: vacías;
  - **no ejecutes nada.**
- [ ] En **Files**, subí los tres CSV del Escritorio. Los del Escritorio son los originales: no los toques.
- [ ] **Tools → Settings → AI assistance**: ocultá las funciones de IA.
- [ ] **Tools → Settings → Editor**: si está la opción, desactivá las sugerencias automáticas de código. Todo lo que se tipea, se tipea a mano.
- [ ] Zoom (`Cmd + +`). Firefox con la ventana 1 en la descripción de la tarea y la ventana 2 en Colab (segunda línea del Dock).

**Durante**

- [ ] **Nunca hablar y tipear al mismo tiempo.** Ningún tramo de tipeo de más de 45 segundos.
- [ ] **Cada acción con qué + dónde** (número de celda, línea, columna, botón) y, cuando no es obvio, **por qué**.
- [ ] **El número de celda se repite al menos una vez por minuto.**
- [ ] Ejecutá cada celda una vez, en orden. **No repitas la celda 1 después de la celda 7.**
- [ ] No termines antes de las conclusiones, **Cmd + S** y el epilogue. **TaskRecorder se abre recién después del epilogue.**

**Después**

- [ ] Detené TaskRecorder. Descargá el `.ipynb` y los 5 CSV de Colab.
- [ ] **Run full AutoQC**: revisá el porcentaje de tipeo y que What + Where pase el 70%.
- [ ] Armá **Deliverables.zip** con el `.ipynb`, los 5 CSV y la carpeta `original/` con los tres CSV del Escritorio.
- [ ] Marcá en Studio la opción de archivos generados con IA.
- [ ] Subí por separado el **MP4**, el **ZIP de TaskRecorder**, **Deliverables.zip** y **Metadata.rtf**.
