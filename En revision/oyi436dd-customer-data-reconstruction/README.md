# oyi436dd — Customer Data Reconstruction

Guion para grabar la tarea **oyi436dd** en **Google Colab** (app principal), con **Firefox** como app de apoyo, en una sola toma.

> **Goal:** *Reconstruct and validate customer-level data by resolving identity inconsistencies, reconciling duplicate transactions, engineering historical behavioral features, and producing an auditable consolidated dataset with clearly documented exceptions.*

**Duración estimada: ~24:50** (objetivo 25, máximo 30).

**Punto de partida al grabar:** la **celda 1 ya está escrita** y los tres CSV ya están cargados en el panel **Files** de Colab. **Todo lo demás se tipea en vivo** (celdas 2 a 7 y la celda de conclusiones).

---

## Cronograma

| # | Bloque | Parte del Goal | Celda | TIME | Duración |
| - | ------ | -------------- | ----- | ---- | -------- |
| 0 | Opening | — | — | 0:00–1:10 | 1:10 |
| 1 | Perfil de los tres archivos | Inspección | 1 (ya escrita) | 1:10–3:00 | 1:50 |
| 2 | Identidades | Identity inconsistencies | 2 (se tipea) | 3:00–7:00 | 4:00 |
| 3 | Pedidos duplicados | Duplicate transactions | 3 (se tipea) | 7:00–9:40 | 2:40 |
| 4 | Vincular pedidos y actividad | Duplicate transactions | 4 (se tipea) | 9:40–12:05 | 2:25 |
| 5 | Variables de comportamiento | Behavioral features | 5 (se tipea) | 12:05–16:00 | 3:55 |
| 6 | Validación | Validate | 6 (se tipea) | 16:00–17:55 | 1:55 |
| 7 | Excepciones y exportación | Auditable dataset + exceptions | 7 (se tipea) | 17:55–21:55 | 4:00 |
| 8 | Conclusiones | — | texto (se tipea) | 21:55–23:35 | 1:40 |
| 9 | Epilogue | — | — | 23:35–24:50 | 1:15 |
| | **Total** | | | | **~24:50** |

*(Calculado con 130 palabras/min de narración, 135 caracteres/min de tipeo en silencio, todo sumado, más ~20 s de navegación y ejecución por bloque.)*

---

## Archivos de entrada

Sintéticos, generados con IA. Fecha de corte de los datos: 2025-12-31.

| Archivo | Filas | Columnas | Problemas que tiene |
| ------- | ----- | -------- | ------------------- |
| `customers.csv` | 542 | `customer_id, first_name, last_name, email, phone, city, signup_date` | 42 registros duplicados de 500 personas; teléfonos en 4 formatos; 30 emails vacíos y 32 con mayúsculas o espacios; 11 personas con ciudades en conflicto |
| `orders.csv` | 2.419 | `order_id, customer_id, order_date, amount, status, updated_at` | 57 filas exactamente duplicadas; 48 pedidos con una versión vieja y una nueva; 14 pedidos de clientes que no existen ($1,315.58) |
| `customer_activity.csv` | 5.400 | `customer_id, event_date, event_type` | 114 eventos duplicados; 31 de clientes que no existen |

**Cómo cubre cada parte del Goal:**

| Parte del Goal | Celda | Qué produce |
| -------------- | ----- | ----------- |
| Identity inconsistencies | 2 | `master_id` por teléfono normalizado: 542 registros → 500 personas; `conf`, 11 personas con ciudades en conflicto |
| Reconciling duplicate transactions | 3, 4 | 2.314 pedidos únicos ($11,580.09 menos); actividad sin duplicados; todo vinculado al `master_id` |
| Historical behavioral features | 5 | `d`: una fila por persona con pedidos, gasto, último pedido y eventos |
| Validate | 6 | El gasto de `d` cierra al centavo con los pedidos completados ($227,115.94) |
| Auditable dataset + documented exceptions | 7 | `customers_consolidated.csv`, `exceptions_report.csv` (67 filas) y `customers.csv` reescrito |

**Criterios de Slack que cubre:**

- `customers.csv` se reescribe con el mismo nombre: conserva todas las columnas originales y suma `phone_n` y `master_id`. El original queda en el Escritorio.
- El impacto está en dólares: $11,580.09 inflados por duplicados y $1,315.58 en pedidos sin cliente.
- Cada decisión se justifica contra la alternativa incorrecta.

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
- **DECISION:** las alternativas y cómo se elige con el resultado.
- 📘 = qué hace cada línea, en inglés. Es para vos: **no se lee**.

---

## Estrategia de tiempo y tipeo

| | Cantidad | Tiempo |
| - | -------- | ------ |
| Tipeo en vivo (celdas 2 a 7 + conclusiones) | 1.281 caracteres | ~9,5 min a 135 car./min (~10,7 a 120) |
| Narración | ~1.562 palabras | ~12,0 min |
| Navegación y ejecución | 10 bloques | ~3,3 min |
| **Total** | | **~24:50** (~26:00 si tipeás a 120 car./min) |

**Tipeo: ~38% del video a 135 car./min** (~41% a 120). Es lo mínimo con todo tipeado salvo la celda 1: el código ya está reducido a lo indispensable.

**Qué se simplificó para que todo entre tipeado:**

- Los duplicados exactos y las versiones viejas de pedidos se resuelven en **una sola línea** (ordenar por `updated_at` y quedarse con la última).
- Los pedidos y la actividad se vinculan con `map` sobre una serie de clave única: no puede multiplicar filas, así que no hace falta un control de cardinalidad aparte.
- Una sola tabla `d` con la ficha del cliente y sus variables.
- Saqué del CSV de actividad 20 eventos anteriores a la fecha de alta, que el código simple ya no trata.

**Reglas de tipeo:**

1. **Nunca hablar y tipear al mismo tiempo.** Frase 🗣️⌨️ con las manos quietas → bloque en silencio.
2. **Ningún tramo pasa de 45 segundos.** El más largo tiene 85 caracteres (~38 s a 135 car./min). Las líneas largas de las celdas 5, 6 y 7 se tipean en varios tramos, **sin Enter** entre ellos.
3. **Nada de tipeo extra:** ni comentarios ni `print` de prueba.
4. **Sin autocompletado.** Si aparece una caja de sugerencias, Escape.
5. **`\` en Mac** (celda 2): con teclado español, **Option + º** (la tecla a la izquierda del 1); con teclado US, la tecla arriba de Enter.

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

> 🟢 I will be beginning my task soon. A company's customer data is messy: the same person appears more than once, orders are duplicated, and some records point to customers that don't exist.

> 🟢 I'll resolve identities, remove duplicate orders, build one behavioral profile per customer, check the totals, and document every exception.

> 🖱️ I'm clicking the yellow minimize button at the top left, to hide the task description.

> 🖱️ I'm clicking the Firefox icon in the Dock and choosing the second window: my Colab notebook.

> 🟢 The three input CSVs are already uploaded to the Files panel. They're synthetic, generated with AI; the originals stay on my Desktop.

**WHY:** el revisor tiene que saber desde el principio qué es "éxito": una fila por persona, sin importes duplicados, con totales que cierran y excepciones documentadas.

**EXPECTED RESULT:** el notebook con la celda 1 escrita y la celda 2 vacía debajo.

---

### Bloque 1. Perfil de los tres archivos

**TIME:** 1:10–3:00 (1:50)

**WHAT I DO:** señalar cada grupo de líneas de la celda 1 (ya escrita) → Run → señalar la salida.

**WHERE:** celda 1, arriba de todo. Botón Run (triángulo) a la izquierda de la celda.

**Celda 1 (ya escrita antes de grabar):**

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

> 🖱️ I'm pointing at cell one, which I wrote before recording, because loading files is routine. Everything after it I'll type live.

> 🖱️ I'm pointing at the three read_csv lines: customers, orders and activity. Dates are parsed because I'll sort and compare them.

> 🖱️ I'm pointing at the loop: for each file, its size, exact duplicate rows and missing values.

> 🖱️ I'm pointing at the last print: unique order IDs, and orders whose customer doesn't exist.

> 🖱️ I'm clicking the Run button on the left of cell one.

> 🖱️ I'm pointing at the customers line under cell one: 542 rows and 30 missing values, all in email.

> 🟢 So email can't be my identity key: it's missing for some people.

> 🖱️ I'm pointing at the orders line: 57 exact duplicate rows, and only 2,314 unique order IDs out of 2,419.

> 🟢 So there are more duplicates than the exact copies: some orders have two versions.

> 🟢 The orders also have an updated_at column, which will tell me which version is current.

> 🖱️ I'm pointing at the activity line: 114 duplicate events. And 14 orders point to customers that don't exist.

> 🖱️ I'm pointing at the phone column of the table: four different formats for the same kind of number.

**WHY:** el perfil decide la estrategia: el email tiene vacíos, el teléfono está completo pero con formatos distintos, y en pedidos hay más IDs repetidos que filas idénticas.

**EXPECTED RESULT:**

- `customers (542, 7) duplicate rows: 0 nulls: 30`
- `orders (2419, 6) duplicate rows: 57 nulls: 0`
- `activity (5400, 3) duplicate rows: 114 nulls: 0`
- `unique order_id: 2314 | orders without customer: 14`
- Las 5 primeras filas de `customers`: teléfonos como `5989504447` y `(513) 390-6167`; la fila de C0005 con el email vacío (`NaN`).

📘 **What each line does** (para vos, no se lee):

- `import pandas as pd`: loads pandas.
- `c = pd.read_csv("customers.csv", parse_dates=["signup_date"])`: customer records, with the signup date as a date.
- `o = pd.read_csv("orders.csv", parse_dates=["order_date", "updated_at"])`: orders, with order and last-update timestamps.
- `a = pd.read_csv("customer_activity.csv", parse_dates=["event_date"])`: activity events.
- `for name, d in {...}.items():`: loops over the three tables with their names.
- `print(name, d.shape, ..., d.duplicated().sum(), ..., d.isna().sum().sum())`: rows, columns, exact duplicate rows and missing values.
- `print("unique order_id:", ..., (~o.customer_id.isin(c.customer_id)).sum())`: distinct order IDs and orders with an unknown customer.
- `c.head()`: first five customer records.

---

### Bloque 2. Identidades

**TIME:** 3:00–7:00 (4:00)

**WHAT I DO:** clic en la celda 2 → tipear 5 tramos → Run → señalar los dos números.

**WHERE:** celda 2, vacía, debajo de la tabla de clientes.

**SAY:**

> 🖱️ I'm clicking inside cell two, the empty cell below the customers table.

> 🟢 First, identity: which records are the same person?

> 🗣️⌨️ First line of cell two: a normalized phone, digits only, so the four formats become one key.

```python
c["phone_n"] = c.phone.str.replace(r"\D", "", regex=True)
```
*(56 caracteres · ~25 s)*

> 🗣️⌨️ Next line of cell two: sort by signup date, so the oldest record of each person comes first.

```python
c = c.sort_values("signup_date")
```
*(32 caracteres · ~14 s)*

> 🗣️⌨️ Next line: the master ID is the oldest record's ID for each phone. That's my survivorship rule: the first registration wins.

```python
c["master_id"] = c.groupby("phone_n").customer_id.transform("first")
```
*(68 caracteres · ~30 s)*

> 🗣️⌨️ Next line of cell two: records of the same person with different cities. I don't overwrite them; they go to the exceptions.

```python
conf = c[c.groupby("master_id").city.transform("nunique") > 1]
```
*(63 caracteres · ~28 s)*

> 🗣️⌨️ Last line of cell two: how many people, and how many with a city conflict.

```python
print(c.master_id.nunique(), conf.master_id.nunique())
```
*(54 caracteres · ~24 s)*

> 🖱️ I'm clicking the Run button on the left of cell two.

> 🖱️ I'm pointing at the first number under cell two: 500.

> 🟢 542 records are 500 real people: 42 were duplicates in different formats.

> 🟢 If I had matched on email, the 30 empty emails would each look like a new person, and the ones in uppercase or with spaces wouldn't match.

> 🟢 And the oldest-record rule is stable: running it again gives the same masters.

> 🖱️ I'm pointing at the second number: 11.

> 🟢 Eleven people have two cities. A newer record doesn't prove a move, so I keep the master's city and report the conflict.

**WHY:** el teléfono está completo y, normalizado, identifica a la persona; el email tiene 30 vacíos y 32 con mayúsculas o espacios. La regla de supervivencia (el registro más viejo) es explícita y reproducible.

**EXPECTED RESULT:** `500 11`

**DECISION:** ¿clave por email o por teléfono? **Teléfono normalizado**: completo en los 542 registros. ¿Pisar la ciudad con la del registro más nuevo? **No**: sin evidencia de mudanza, se documenta como excepción.

📘 **What each line does** (para vos, no se lee):

- `c["phone_n"] = c.phone.str.replace(r"\D", "", regex=True)`: removes every non-digit from the phone.
- `c = c.sort_values("signup_date")`: oldest records first.
- `c["master_id"] = c.groupby("phone_n").customer_id.transform("first")`: each record gets the ID of the oldest record with the same phone.
- `conf = c[c.groupby("master_id").city.transform("nunique") > 1]`: records of people who appear with more than one city.
- `print(c.master_id.nunique(), conf.master_id.nunique())`: number of people and people with a city conflict.

---

### Bloque 3. Pedidos duplicados

**TIME:** 7:00–9:40 (2:40)

**WHAT I DO:** + Code → tipear 3 tramos → Run → señalar los dos números.

**WHERE:** botón **+ Code** arriba a la izquierda de la barra de Colab (agrega la celda 3 debajo de la celda 2).

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell three below cell two.

> 🟢 Now the duplicate transactions.

> 🗣️⌨️ First line of cell three: the order total before cleaning, to measure the impact in dollars.

```python
t = o.amount.sum()
```
*(18 caracteres · ~8 s)*

> 🗣️⌨️ Next line of cell three: sort by last update and keep the latest version of each order ID. That removes exact copies and old versions in one step.

```python
o = o.sort_values("updated_at").drop_duplicates("order_id", keep="last")
```
*(72 caracteres · ~32 s)*

> 🗣️⌨️ Last line of cell three: orders left, and the dollars removed.

```python
print(len(o), round(t - o.amount.sum(), 2))
```
*(43 caracteres · ~19 s)*

> 🖱️ I'm clicking the Run button on the left of cell three.

> 🖱️ I'm pointing at the two numbers under cell three: 2,314 and 11,580.09.

> 🟢 One row per order ID now. 57 exact copies and 48 old versions inflated revenue by 11,580 dollars.

> 🟢 Keeping the first version instead would keep a pending status that was later updated. The latest update is the true state.

> 🟢 I measure the total before and after, so the impact is in dollars, not just rows. Without this step, every customer's spending would be overstated.

> 🟢 Cancelled and refunded orders stay in the table for now; I'll leave them out of spending in cell five.

**WHY:** un pedido con dos versiones (por ejemplo, `pending` y después `completed`) no son dos ventas. Quedarse con la última actualización refleja el estado real y elimina las copias exactas a la vez.

**EXPECTED RESULT:** `2314 11580.09`

**DECISION:** ¿primera o última versión? **Última** (`keep="last"` sobre `updated_at`): es el estado vigente del pedido.

📘 **What each line does** (para vos, no se lee):

- `t = o.amount.sum()`: order total before deduplication.
- `o = o.sort_values("updated_at").drop_duplicates("order_id", keep="last")`: one row per order ID, the most recently updated.
- `print(len(o), round(t - o.amount.sum(), 2))`: orders left and dollars removed.

---

### Bloque 4. Vincular pedidos y actividad

**TIME:** 9:40–12:05 (2:25)

**WHAT I DO:** + Code → tipear 3 tramos → Run (sin salida).

**WHERE:** botón **+ Code** arriba a la izquierda (agrega la celda 4 debajo de la salida de la celda 3).

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell four below the order counts.

> 🗣️⌨️ First line of cell four: a lookup from every customer ID to its master ID.

```python
m = c.set_index("customer_id").master_id
```
*(40 caracteres · ~18 s)*

> 🗣️⌨️ Next line of cell four: each order gets its master ID. I use map, not merge: the lookup has one row per customer ID, so it can't multiply orders.

```python
o["master_id"] = o.customer_id.map(m)
```
*(37 caracteres · ~16 s)*

> 🗣️⌨️ Last lines of cell four: drop the duplicate events, and link each event to its master ID the same way.

```python
a = a.drop_duplicates()
a["master_id"] = a.customer_id.map(m)
```
*(61 caracteres · ~27 s)*

> 🖱️ I'm clicking the Run button on the left of cell four.

> 🟢 No output here. Orders and events with an unknown customer get an empty master ID; I'll report them, not guess.

> 🟢 A merge against a table with repeated keys is the classic way amounts get duplicated. Map avoids it by design, and cell six will prove it.

**WHY:** un `merge` contra una tabla con claves repetidas multiplica filas e infla importes. `map` sobre una serie indexada por `customer_id` (única) devuelve exactamente una fila por pedido.

**EXPECTED RESULT:** sin salida. (`o` sigue con 2.314 filas; `a` queda con 5.286.)

**DECISION:** ¿asignar los pedidos huérfanos a un cliente parecido? **No**: no hay evidencia; se documentan como excepción.

📘 **What each line does** (para vos, no se lee):

- `m = c.set_index("customer_id").master_id`: Series from customer ID to master ID (unique index).
- `o["master_id"] = o.customer_id.map(m)`: master ID on each order; empty for unknown customers.
- `a = a.drop_duplicates()`: removes the 114 exact duplicate events.
- `a["master_id"] = a.customer_id.map(m)`: master ID on each event; empty for unknown customers.

---

### Bloque 5. Variables de comportamiento

**TIME:** 12:05–16:00 (3:55)

**WHAT I DO:** + Code → tipear 5 tramos (la primera línea en tres tramos, sin Enter) → Run → señalar tres columnas.

**WHERE:** botón **+ Code** arriba a la izquierda (agrega la celda 5 debajo de la celda 4).

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell five below cell four.

> 🟢 Now one row per person, with their history.

> 🗣️⌨️ First line of cell five, in three parts. First part: the master record of each person, the oldest one, as the base row.

```python
d = c.drop_duplicates("master_id").set_index("master_id")
```
*(57 caracteres · ~25 s · sin Enter al final)*

> 🗣️⌨️ Second part, same line: join only completed orders, grouped by person. Cancelled and refunded orders aren't revenue.

```python
.join(o[o.status.eq("completed")].groupby("master_id")
```
*(54 caracteres · ~24 s · sin Enter al final)*

> 🗣️⌨️ Third part: number of orders, total spent, and the date of the last order.

```python
.agg(orders=("order_id", "size"), spent=("amount", "sum"), last=("order_date", "max")))
```
*(85 caracteres · ~38 s)*

> 🗣️⌨️ Next line of cell five: number of activity events per person.

```python
d["events"] = a.groupby("master_id").size()
```
*(43 caracteres · ~19 s)*

> 🗣️⌨️ Last line of cell five: a summary of the new columns.

```python
d.describe().round(1)
```
*(21 caracteres · ~9 s)*

> 🖱️ I'm clicking the Run button on the left of cell five.

> 🖱️ I'm pointing at the count row under cell five: 500 people, 483 with orders, 497 with events.

> 🟢 Every person is kept, even the 17 who never completed an order. That's a behavior too.

> 🖱️ I'm pointing at the median row: 4 orders, 413 dollars spent, 10 events.

> 🟢 Events per person show engagement, even for people who don't buy.

> 🖱️ I'm pointing at the last column's max date: December 19, 2025.

> 🟢 Nothing after the December 31 cut-off, so these features only use history.

> 🟢 And the median last order is November 3rd: that's the recency of a typical customer, about two months before the cut-off.

**WHY:** la base es la ficha del cliente (500 filas), no los pedidos: un `join` desde los clientes conserva a quienes no compraron. Solo los pedidos completados cuentan como gasto.

**EXPECTED RESULT:** `describe` con `count`: `signup_date 500`, `orders 483.0`, `spent 483.0`, `last 483`, `events 497.0`. Medianas (`50%`): `orders 4.0`, `spent 413.5`, `events 10.0`. `max` de `last`: `2025-12-19`.

**DECISION:** ¿contar cancelados y reembolsados? **No**: el gasto es lo que efectivamente se cobró.

📘 **What each line does** (para vos, no se lee):

- `d = c.drop_duplicates("master_id").set_index("master_id")`: one row per person, the oldest record (the table is sorted by signup date).
- `.join(o[o.status.eq("completed")].groupby("master_id")`: adds completed orders grouped by person; people with none keep empty values.
- `.agg(orders=..., spent=..., last=...)`: order count, total amount and last order date.
- `d["events"] = a.groupby("master_id").size()`: events per person.
- `d.describe().round(1)`: count, mean, quartiles and max of each column.

---

### Bloque 6. Validación

**TIME:** 16:00–17:55 (1:55)

**WHAT I DO:** + Code → tipear 2 tramos (sin Enter entre ellos) → Run → señalar los dos totales.

**WHERE:** botón **+ Code** arriba a la izquierda (agrega la celda 6 debajo del resumen).

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell six below the summary.

> 🟢 Now I prove that consolidating didn't lose or duplicate money.

> 🗣️⌨️ In cell six, first part: the total spent in my customer table.

```python
print(d.spent.sum().round(2),
```
*(30 caracteres · ~13 s · sin Enter al final)*

> 🗣️⌨️ Second part, same line: the completed orders with a known customer, straight from the deduplicated orders.

```python
 o.dropna().query("status == 'completed'").amount.sum().round(2))
```
*(64 caracteres · ~28 s)*

> 🖱️ I'm clicking the Run button on the left of cell six.

> 🖱️ I'm pointing at the two numbers under cell six: 227,115.94 and 227,115.94.

> 🟢 They match to the cent. The join didn't multiply any order, and no completed order with a known customer was lost.

> 🟢 If the join had multiplied rows, the first number would be bigger; if I had lost orders, it would be smaller.

**WHY:** si el `join` hubiera multiplicado filas, el total de `d` sería mayor; si se hubiera perdido algún pedido, menor. Que coincidan al centavo es la prueba.

**EXPECTED RESULT:** `227115.94 227115.94`

📘 **What each line does** (para vos, no se lee):

- `print(d.spent.sum().round(2),`: total spent in the consolidated table.
- `o.dropna().query("status == 'completed'").amount.sum().round(2))`: completed orders with a master ID (orphans have an empty one and drop out).

---

### Bloque 7. Excepciones y exportación

**TIME:** 17:55–21:55 (4:00)

**WHAT I DO:** + Code → tipear 5 tramos (la primera línea en tres tramos, sin Enter) → Run → señalar el conteo → abrir y cerrar Files.

**WHERE:** botón **+ Code** arriba a la izquierda (agrega la celda 7). Ícono de carpeta en la barra lateral izquierda.

**SAY:**

> 🖱️ I'm clicking plus Code at the top left, to add cell seven below the validation.

> 🟢 Last step: everything I didn't resolve goes into one exceptions report, with a reason.

> 🗣️⌨️ First line of cell seven, in three parts. First: the city conflicts.

```python
x = pd.concat([conf.assign(issue="city_conflict"),
```
*(50 caracteres · ~22 s · sin Enter al final)*

> 🗣️⌨️ Second part: orders with no customer.

```python
 o[o.master_id.isna()].assign(issue="orphan_order"),
```
*(52 caracteres · ~23 s · sin Enter al final)*

> 🗣️⌨️ Third part: events with no customer.

```python
 a[a.master_id.isna()].assign(issue="orphan_event")])
```
*(53 caracteres · ~24 s)*

> 🗣️⌨️ Next lines of cell seven: save the exceptions report and the consolidated customers.

```python
x.to_csv("exceptions_report.csv")
d.to_csv("customers_consolidated.csv")
```
*(72 caracteres · ~32 s)*

> 🗣️⌨️ Last lines: rewrite the customers file with the normalized phone and the master ID next to the original columns, and count the exceptions.

```python
c.to_csv("customers.csv")
x.issue.value_counts()
```
*(48 caracteres · ~21 s)*

> 🖱️ I'm clicking the Run button on the left of cell seven.

> 🖱️ I'm pointing at the counts under cell seven: 31 orphan events, 22 city-conflict records, 14 orphan orders.

> 🟢 The 14 orphan orders are 1,316 dollars with no customer to assign them to. They stay out of the profiles, but they're documented.

> 🟢 The city conflicts are 22 rows because each of the 11 people has two records. Every row keeps its original customer ID, so anyone can trace it back to the source file.

> 🖱️ I'm clicking the folder icon in the left sidebar, to open the Files panel.

> 🖱️ I'm pointing at exceptions_report and customers_consolidated, the two new files, and customers, rewritten.

> 🖱️ I'm clicking the folder icon again to close the panel.

**WHY:** auditable significa que cada fila excluida o no resuelta tiene un motivo y se puede rastrear hasta su registro original.

**EXPECTED RESULT:** `orphan_event 31`, `city_conflict 22`, `orphan_order 14`. En Files: `exceptions_report.csv` (67 filas), `customers_consolidated.csv` (500 filas) y `customers.csv` reescrito. Si no se ven, decí: *"I'm clicking refresh at the top of the Files panel, to show the new files."*

📘 **What each line does** (para vos, no se lee):

- `x = pd.concat([conf.assign(issue="city_conflict"),`: city-conflict records, tagged.
- `o[o.master_id.isna()].assign(issue="orphan_order"),`: orders with an unknown customer, tagged.
- `a[a.master_id.isna()].assign(issue="orphan_event")])`: events with an unknown customer, tagged.
- `x.to_csv("exceptions_report.csv")`: saves the exceptions report.
- `d.to_csv("customers_consolidated.csv")`: saves one row per person with the features.
- `c.to_csv("customers.csv")`: rewrites the input with `phone_n` and `master_id`; original columns unchanged.
- `x.issue.value_counts()`: rows per reason.

---

### Bloque 8. Conclusiones

**TIME:** 21:55–23:35 (1:40)

**WHAT I DO:** + Text → tipear 3 tramos → clic afuera → Cmd + S.

**WHERE:** botón **+ Text** arriba a la izquierda de la barra de Colab (agrega la celda al final).

**SAY:**

> 🖱️ I'm clicking plus Text at the top left, to add a text cell at the end of the notebook for the conclusions.

> 🗣️⌨️ In the text cell: the title.

```markdown
## Summary
```
*(10 caracteres · ~4 s)*

> 🗣️⌨️ Next line of the text cell: the main result in numbers.

```markdown
- 500 customers from 542 records; $11,580 of duplicates removed.
```
*(64 caracteres · ~28 s)*

> 🗣️⌨️ Last line: the AI declaration.

```markdown
- Input files generated with AI.
```
*(32 caracteres · ~14 s)*

> 🖱️ I'm clicking on the empty area below the text cell, to show it formatted.

> 🖱️ I'm pressing Command and S to save the notebook; the save message appears at the bottom left.

**EXPECTED RESULT:** la celda de texto con el título y dos viñetas, formateada.

---

### Bloque 9. Epilogue

**TIME:** 23:35–24:50 (1:15)

**WHAT I DO:** scroll lento hacia arriba, sin tipear. Recién **después** abrís TaskRecorder para detener la grabación.

**WHERE:** Colab, desde las conclusiones hasta la celda 1.

**SAY:**

> 🖱️ I'm scrolling up slowly through the notebook, from the conclusions back to cell one.

> 🟢 The key decisions: the normalized phone as identity key, because email was incomplete; the oldest record as master; and the latest version of each order.

> 🟢 The check: total spent matches the completed orders to the cent.

> 🟢 The hardest part was the orders: there were more repeated IDs than exact copies, so I had to find the old versions too.

> 🟢 Open items: 11 city conflicts and 1,316 dollars of orders without a customer, all in the exceptions report.

> 🟢 With more time, I'd confirm the city conflicts with the customers, and look for the missing customer records behind the orphan orders. Thanks for watching!

**WHY:** no repite los pasos: cuenta las decisiones, cómo se validaron, el desafío y qué queda abierto.

---

## Si algo sale mal

| Error | Qué decís y hacés |
| ----- | ----------------- |
| Un nombre mal escrito | 🖱️ *"There's a typo in cell N. I'm clicking on that line to fix it, and running the cell again."* |
| `NameError` | 🖱️ *"An earlier cell didn't run. I'm opening the Runtime menu at the top and choosing Run before."* |
| Los totales de la celda 6 no coinciden | Revisá que en la celda 5 diga `o.status.eq("completed")` y en la celda 6 `'completed'` entre comillas simples. |
| Hay que volver a correr la celda 1 después de la celda 7 | `customers.csv` ya está reescrito. 🖱️ *"The customers file was already rewritten, so I'm uploading the original from my Desktop again in the Files panel."* |

---

## Checklist de archivos y preparación previa

- [ ] Practicá dos veces con cronómetro. [customer_reconstruction.ipynb](customer_reconstruction.ipynb) tiene el código completo para comparar.
- [ ] En Colab, creá el notebook **customer_reconstruction** con **la celda 1 escrita** (copiala del bloque 1) y **la celda 2 vacía** debajo. **No ejecutes nada.**
- [ ] En **Files**, subí los tres CSV de esta carpeta: `customers`, `orders` y `customer_activity`. Los de la carpeta son los originales: no los toques.
- [ ] **Tools → Settings → AI assistance**: ocultá las funciones de IA.
- [ ] **Tools → Settings → Editor**: si está la opción, desactivá las sugerencias automáticas de código.
- [ ] Probá el `\` en Colab antes de grabar.
- [ ] Zoom (`Cmd + +`). Firefox con la ventana 1 en la descripción de la tarea y la ventana 2 en Colab.

## Checklist de resultados que deben quedar generados

- [ ] `500 11` (celda 2).
- [ ] `2314 11580.09` (celda 3).
- [ ] El resumen de `d` con 500 personas (celda 5).
- [ ] `227115.94 227115.94` (celda 6).
- [ ] `exceptions_report.csv` (67 filas), `customers_consolidated.csv` (500 filas) y `customers.csv` reescrito (celda 7).
- [ ] La celda de conclusiones y el notebook guardado.
- [ ] Después: descargá el `.ipynb` y los tres CSV generados. Armá **Deliverables.zip** con eso y la carpeta `original/` con los tres CSV de esta carpeta. Marcá en Studio la opción de archivos generados con IA.

## Checklist de decisiones que debo explicar

- [ ] **Clave de identidad:** teléfono normalizado, no email (30 vacíos).
- [ ] **Supervivencia:** el registro más viejo es el master.
- [ ] **Ciudades en conflicto:** no se pisan; van a excepciones (11 personas).
- [ ] **Pedidos:** última versión por `updated_at`; $11,580.09 menos.
- [ ] **`map` y no `merge`:** no puede multiplicar filas.
- [ ] **Solo pedidos completados** como gasto.
- [ ] **Validación:** el total cierra al centavo.
- [ ] **Huérfanos:** no se asignan; se documentan ($1,315.58 en 14 pedidos, 31 eventos).

---

## Conclusión para cerrar la grabación (en inglés)

> The customer file had 542 records, but they're 500 people: I matched them by a normalized phone, because email was incomplete, and kept the oldest record as the master. Orders had exact copies and older versions that inflated revenue by 11,580 dollars; keeping the latest update fixed both. Every person now has one row with orders, spending, last order and activity, and the total matches the completed orders to the cent. What I couldn't resolve, 11 city conflicts and 1,316 dollars of orders with no customer, is in the exceptions report.

*(Es la versión larga del epilogue. Si te sobra tiempo, podés decirla en lugar de las 🟢 del bloque 9.)*

---

## Pendientes antes de grabar

| Tema | Qué hacer |
| ---- | --------- |
| **Goal en TaskRecorder** | Confirmá que la descripción de TaskRecorder corresponde a este Goal. Abajo hay una propuesta. |
| **Origen de los CSV** | Sintéticos, generados con IA. Decí "generated with AI" y marcá en Studio la opción de archivos generados con IA. |

**Descripción (propuesta):**

> Reconstruct customer-level data in Google Colab with pandas. I resolve duplicate customer identities with a normalized phone key and a survivorship rule, remove duplicate and outdated order versions, link orders and activity to each person without multiplying rows, build behavioral features, validate totals against the source, and export a consolidated customer dataset with an exceptions report.
