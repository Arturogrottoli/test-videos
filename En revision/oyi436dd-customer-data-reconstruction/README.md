# oyi436dd — Customer Data Reconstruction

Guion para grabar la tarea **oyi436dd** en **Google Colab** con **Python y pandas**, con **Firefox** como aplicación de apoyo. Se graba en una sola toma.

> **Goal:** *Reconstruct and validate customer-level data by resolving identity inconsistencies, reconciling duplicate transactions, engineering historical behavioral features, and producing an auditable consolidated dataset with clearly documented exceptions.*

**Duración estimada: ~24,5–25,5 minutos** (máximo absoluto: 30).

**Archivos de entrada** (sintéticos, con problemas reales):

| Archivo | Filas | Problemas que tiene |
| ------- | ----- | ------------------- |
| `customers.csv` | 542 | 42 registros duplicados de 500 personas, con emails en mayúsculas o con espacios, teléfonos en 4 formatos, 30 emails vacíos, 11 personas con ciudades en conflicto, y 61 personas distintas que comparten nombre y ciudad con otra |
| `orders.csv` | 2.419 | 57 filas exactamente duplicadas, 48 pedidos con una versión vieja (`pending`) y una nueva, y 14 pedidos de clientes que no existen |
| `customer_activity.csv` | 5.420 | 114 eventos duplicados, 31 de clientes que no existen y 20 eventos anteriores a la fecha de alta |

**Cómo cubre cada parte del Goal:**

| Parte del Goal | Fase | Celda |
| -------------- | ---- | ----- |
| Inspección y perfil de los tres archivos | 2 | 1 (armada) |
| Identity inconsistencies: duplicados resueltos **y** ambiguos que no se fusionan | 3 | 2 (se tipea) |
| Reconciling duplicate transactions | 4 | 3 (se tipea) |
| Cardinalidad de los joins y prevención de importes duplicados | 5 | 4 (armada) |
| Historical behavioral features, con fecha de corte validada | 6 | 5 (armada) |
| Validación contra las fuentes | 7 | 6 (armada) |
| Auditable consolidated dataset + documented exceptions | 8 | 7 (armada) |

**Criterios de Slack que cubre:** los tres archivos de entrada se reescriben (customers con los valores originales al lado de los normalizados y el `master_id`). El impacto se mide en dólares: $11,580 inflados por duplicados y $1,316 sin cliente. Cada decisión se justifica comparándola con la alternativa incorrecta.

---

## Cambios respecto de la versión anterior (auditoría del 2026-11-20)

| # | Cambio | Por qué |
| - | ------ | ------- |
| 1 | Celda 2: nueva línea `amb` (mismo nombre y ciudad, distinta persona) y su conteo en el `print`: `1 11 61` | El Goal pide identidades ambiguas que **no** se fusionan; antes no había ninguna acción que lo mostrara. |
| 2 | Fase 3: justificación de por qué no se pisa la ciudad del master | En los 11 conflictos el master es el registro más viejo; el revisor iba a preguntar. |
| 3 | Celda 5: `inactive_90` corregido (los clientes **sin** eventos ahora cuentan como inactivos: 67, no 64) | Era un error: `NaT > 90` da `False`. |
| 4 | Celda 5: `email_n` toma el primer email no vacío del grupo | El master de 1 persona tenía el email vacío y el duplicado no; se perdía. |
| 5 | Celda 5: control de fecha de corte (`0 0` pedidos y eventos posteriores al 31/12/2025) | La consistencia temporal tiene que demostrarse, no suponerse. |
| 6 | Celda 7: motivo `ambiguous_name` en el reporte (151 filas, antes 87) | Las ambiguas quedan documentadas. |
| 7 | Celdas 4 y 6 pasan a **armadas**; opening, conclusiones y epilogue más cortos | La versión anterior daba 29–32 min reales y ~35–38% de tipeo. |
| 8 | Carpeta: la versión financiera pasó a `_version_financiera/` | La raíz tenía archivos de otra tarea con otro Goal. |

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

**Cómo se calcula:** narración a 130 palabras por minuto, tipeo en silencio a **135 caracteres por minuto** (todo sumado, sin superposición) y ~20 s de navegación y ejecución por fase. La medición real de k3a13c10 se calibró con 120 car./min; por eso también se muestra ese caso.

| | Cantidad | Tiempo |
| - | -------- | ------ |
| Tipeo en vivo (celdas 2 y 3 + conclusiones) | 1.011 caracteres | ~7,5 min (~8,4 a 120 car./min) |
| Narración | ~1.793 palabras | ~13,8 min |
| Navegación y ejecución | 10 fases | ~3,3 min |
| **Total** | | **~24,6 min** (~25,6 a 120 car./min) |

**Tipeo: ~30% del video** (~33% a 120 car./min; máximo 35%).

**Qué celdas van armadas y por qué:**

| Celda | Estado | Por qué |
| ----- | ------ | ------- |
| 1. Carga y perfil | **Armada** | Es mecánica: leer y contar. Lo que importa es interpretar el perfil. |
| 2. Identidades | Se tipea | Es la decisión central: qué clave identifica a una persona y a quién no fusionar. |
| 3. Pedidos duplicados | Se tipea | Decisión: qué versión de un pedido es la verdadera. |
| 4. Joins y cardinalidad | **Armada** | El control (`validate="m:1"`) y el join incorrecto se explican señalando cada línea. |
| 5. Variables de comportamiento | **Armada** | Son agregaciones estándar. Las reglas de negocio se explican señalando cada línea. |
| 6. Validación de totales | **Armada** | Son dos `print` de control; lo que importa es leer que cierran al centavo. |
| 7. Excepciones y exportación | **Armada** | Es mecánica: juntar tablas y guardar archivos. |

**Reglas de tipeo:**

1. **Nunca hablar y tipear al mismo tiempo.** Frase 🗣️⌨️ con las manos quietas → bloque en silencio.
2. **Ningún tramo de tipeo pasa de 45 segundos.** El más largo tiene 84 caracteres (~37 s a 135 car./min; ~42 s a 120). Las líneas largas están partidas en dos tramos, con una frase en el medio y **sin Enter**.
3. **Nada de tipeo extra:** ni comentarios, ni `print` de prueba.
4. **No se usa autocompletado.** Si aparece una caja de sugerencias, Escape.

---

## Pendientes antes de grabar

| Tema | Qué hacer |
| ---- | --------- |
| **Goal en TaskRecorder** | Confirmá que la descripción de TaskRecorder corresponde a este Goal (clientes), no a la versión financiera de `_version_financiera/`. Abajo hay una propuesta de descripción. |
| **Origen de los CSV** | Los generé yo, Claude, con un script de Python. Decí "generated with AI" y marcá en Studio la opción de archivos generados con IA. |
| **Límite de tipeo** | El guion da ~30–33% según tu velocidad (máximo 35%). |
| **Versiones anteriores** | `_version_financiera/` y `_idea_anterior/` no van en la entrega. |

**Descripción para TaskRecorder (propuesta):**

> Reconstruct a reliable customer base in Google Colab with pandas from three messy sources: customers, orders and customer activity. I resolve duplicate identities with a normalized phone key, keep look-alike customers apart, reconcile exact and versioned duplicate orders, validate join cardinality, build historical behavioral features with a validated cut-off date, check totals to the cent, and export a consolidated customer dataset with an exception report.

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

**TIME:** 0:00–1:15 (1:15)

**ON SCREEN:** Firefox, ventana 1, con la descripción de la tarea. Después: botón amarillo para minimizar → Firefox en el Dock → segunda ventana (Colab) → panel Files → cerrarlo.

**SAY:**

> 🟢 I will be beginning my task soon. The goal is to rebuild a reliable customer base from three messy files, so each real person appears once with their full history, and every record I can't resolve is documented instead of dropped.

> 🟢 My plan: profile the files, resolve identities, reconcile duplicate orders, validate the joins, build behavioral features, check the totals, and export the dataset with an exception report.

> 🖱️ I'm clicking the yellow minimize button at the top left, to hide the task description.

> 🖱️ I'm clicking the Firefox icon in the Dock and choosing the second window: my Colab notebook.

> 🖱️ I'm clicking the folder icon in Colab's left sidebar, to open the Files panel.

> 🖱️ I'm pointing at the three CSV files: customers, orders and customer_activity. They're synthetic, generated with AI; the notebook rewrites them, and the originals stay on my Desktop.

> 🖱️ I'm clicking the same folder icon to close the panel.

**WHY:** el revisor tiene que saber desde el principio qué significa "bien": una fila por persona, totales que cierran y excepciones documentadas.

**EXPECTED RESULT:** el notebook con las celdas 1, 4, 5, 6 y 7 llenas y las 2 y 3 vacías. En Files, los tres CSV.

---

### Fase 2. Inspección y perfil

**TIME:** 1:15–3:45 (2:30)

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

> 🖱️ I'm pointing at cell one, prepared before recording, because loading and counting are routine.

> 🖱️ I'm pointing at the three read_csv lines in cell one, with dates parsed, because later I compare orders and events against signup dates.

> 🖱️ I'm pointing at the loop: shape, duplicates and missing values per file, then unique order IDs and orphan orders.

> 🖱️ I'm clicking the Run button on the left of cell one.

> 🖱️ I'm pointing at the three profile lines under cell one.

> 🟢 Customers has 542 records and 30 missing emails. Orders has 57 exact duplicate rows, and activity has 114.

> 🖱️ I'm pointing at the next line: 2,314 unique order IDs.

> 🟢 2,419 rows but 2,314 IDs: 57 exact copies, and 48 more are versions of the same order. And 14 orders have no customer.

> 🖱️ I'm moving the mouse down the phone and email columns of the table under cell one.

> 🟢 Phones come in several formats, and one email is empty. Exact matching on raw values would miss duplicates, so I normalize first.

**WHY:** comparar filas con IDs únicos separa "copias exactas" de "versiones distintas del mismo pedido", que se resuelven de forma distinta. Ver los formatos antes de buscar duplicados evita una clave de matching que falle en silencio.

**EXPECTED RESULT:**

- `customers (542, 7) duplicate rows: 0 nulls: 30`
- `orders (2419, 6) duplicate rows: 57 nulls: 0`
- `activity (5420, 3) duplicate rows: 114 nulls: 0`
- `unique order_id: 2314 | orders without customer: 14`
- Tabla: `C0002` con `(513) 390-6167`, `C0003` con `584.091.8461`, `C0005` con email `NaN`.

📘 **What each line does** (para vos, no se lee):

- `import pandas as pd`: loads pandas as `pd`.
- `c = pd.read_csv("customers.csv", parse_dates=["signup_date"])`: reads the customers, with `signup_date` as a real date.
- `o = pd.read_csv("orders.csv", parse_dates=["order_date", "updated_at"])`: reads the orders, with both dates parsed.
- `a = pd.read_csv("customer_activity.csv", parse_dates=["event_date"])`: reads the activity events.
- `for name, d in {...}.items():`: loops over the three tables with their names.
- `print(name, d.shape, ..., d.duplicated().sum(), ..., d.isna().sum().sum())`: rows and columns, fully duplicated rows and total missing values.
- `print("unique order_id:", ..., (~o.customer_id.isin(c.customer_id)).sum())`: distinct order IDs, and orders whose `customer_id` isn't in customers (`~` means "not").
- `c.head()`: the first 5 customers, to see the formats.

---

### Fase 3. Resolver identidades

**TIME:** 3:45–10:15 (6:30)

**ON SCREEN:** Colab, celda 2 (vacía). Clic adentro, tipear 10 tramos, Run, señalar la salida.

**SAY:**

> 🖱️ I'm clicking inside cell two, the empty cell below the profile.

> 🟢 Phase two: identity resolution. Two questions: which key identifies a real person, and who looks similar but must not be merged.

> 🗣️⌨️ On the first line of cell two, I normalize the email: strip the spaces and lowercase it.

```python
c["email_n"] = c.email.str.strip().str.lower()
```
*(46 caracteres · ~20 s)*

> 🗣️⌨️ Next line of cell two: the phone with only its digits, so all formats become the same.

```python
c["phone_n"] = c.phone.str.replace(r"\D", "", regex=True)
```
*(57 caracteres · ~25 s)*

> 🗣️⌨️ Still in cell two: I sort by signup date, oldest first.

```python
c = c.sort_values("signup_date")
```
*(31 caracteres · ~14 s)*

> 🗣️⌨️ Next line of cell two: each phone gets the oldest customer ID as master ID. The oldest record survives, because it holds the real signup date.

```python
c["master_id"] = c.groupby("phone_n").customer_id.transform("first")
```
*(69 caracteres · ~31 s)*

> 🗣️⌨️ Next line of cell two: I compare three keys. First half: duplicates found with the raw email, and with the normalized email.

```python
print(c.email.dropna().duplicated().sum(), c.email_n.dropna().duplicated().sum(), 
```
*(82 caracteres · ~36 s)*

> 🗣️⌨️ Same line, second half: the records merged by phone.

```python
len(c) - c.master_id.nunique())
```
*(31 caracteres · ~14 s)*

> 🗣️⌨️ Still in cell two: a group per master ID, and the records whose person has more than one city.

```python
g = c.groupby("master_id")
conf = c[g.city.transform("nunique") > 1]
```
*(68 caracteres · ~30 s)*

> 🗣️⌨️ Now the opposite risk, in cell two: records with the same first name, last name and city, but different master IDs. First half: group by name and city.

```python
amb = c[c.groupby(["first_name", "last_name", "city"])
```
*(52 caracteres · ~23 s)*

> 🗣️⌨️ Same line, second half: keep the groups that hold more than one master ID.

```python
.master_id.transform("nunique") > 1]
```
*(36 caracteres · ~16 s)*

> 🗣️⌨️ Last lines of cell two: whether any phone group has two different emails, the people with a city conflict, and the look-alike people. Then two conflicts on screen.

```python
print(g.email_n.nunique().max(), conf.master_id.nunique(), amb.master_id.nunique())
conf.sort_values("master_id").head(4)
```
*(122 caracteres · en dos tramos: el `print` + Enter (~38 s), y la última línea (~16 s))*

> 🖱️ I'm clicking the Run button on the left of cell two. Two printed lines and a table appear below it.

> 🖱️ I'm pointing at the first printed line under cell two: 0, 31 and 42.

> 🟢 Raw email finds zero; normalized email finds 31 but misses the empty ones; the phone finds all 42, because it's never empty.

> 🖱️ I'm pointing at the second line: 1, 11 and 61.

> 🟢 The 1 is my safety check: no phone has two different emails, so it isn't merging different people. 11 people have two cities.

> 🟢 And 61 people share a name and city with someone else, but not a phone or email. A name match would merge them; I keep them apart and report them as ambiguous.

> 🖱️ I'm pointing at the two Maria Molina rows in the table, at the city column.

> 🟢 Same email and phone, Miami and Boston. A newer record isn't proof of a move, so I keep the master's city and flag it.

**WHY:**

- El email crudo da 0: es la prueba de que normalizar era necesario.
- El email normalizado da 31 y no 42: muestra por qué el email solo no alcanza.
- El `1` demuestra que el teléfono no fusiona personas distintas.
- El `61` es el riesgo contrario: nombre + ciudad parece una clave razonable, pero fusionaría 61 personas distintas.
- Elegir el registro más viejo como master es una regla de supervivencia explícita y reproducible. Los conflictos de ciudad no se resuelven sin evidencia: se documentan.

**EXPECTED RESULT:**

- Primera línea: `0 31 42`.
- Segunda línea: `1 11 61`.
- Tabla de 4 filas: `C0180` y `C0061` (Maria Molina, Miami / Boston, master `C0061`); `C0016` y `C0145` (James Lopez, Austin / Miami, master `C0145`).

📘 **What each line does** (para vos, no se lee):

- `c["email_n"] = c.email.str.strip().str.lower()`: the email without surrounding spaces and in lowercase. Missing emails stay missing.
- `c["phone_n"] = c.phone.str.replace(r"\D", "", regex=True)`: removes every non-digit (`\D`), so all phone formats match.
- `c = c.sort_values("signup_date")`: oldest records first.
- `c["master_id"] = c.groupby("phone_n").customer_id.transform("first")`: every record gets the ID of the oldest record with the same phone.
- `print(c.email.dropna().duplicated().sum(), c.email_n.dropna().duplicated().sum(), len(c) - c.master_id.nunique())`: duplicates found by raw email, by normalized email, and records merged by phone. Se tipea en una sola línea, en dos tramos (no apretes Enter en el medio).
- `g = c.groupby("master_id")`: the records grouped by person.
- `conf = c[g.city.transform("nunique") > 1]`: the records of people with more than one city.
- `amb = c[c.groupby(["first_name", "last_name", "city"]).master_id.transform("nunique") > 1]`: records whose name and city are shared with a different person (different master ID). Se tipea en una sola línea, en dos tramos.
- `print(g.email_n.nunique().max(), conf.master_id.nunique(), amb.master_id.nunique())`: the most distinct emails in one person (must be 1), people with a city conflict, and look-alike people.
- `conf.sort_values("master_id").head(4)`: shows two conflicts, with both records of each.

---

### Fase 4. Reconciliar pedidos duplicados

**TIME:** 10:15–13:15 (3:00)

**ON SCREEN:** Colab, celda 3 (vacía). Clic adentro, tipear 3 tramos, Run, señalar la salida.

**SAY:**

> 🖱️ I'm clicking inside cell three, below the identity table.

> 🟢 Phase three: duplicate orders. Two different problems: exact copies, and several versions of the same order.

> 🗣️⌨️ On the first lines of cell three, I save the total amount, to measure the impact in dollars. Then I drop the exact copies and count what's left.

```python
total = o.amount.sum()
o = o.drop_duplicates()
n = len(o)
```
*(57 caracteres · ~25 s)*

> 🗣️⌨️ Next line of cell three: for orders with several versions, I keep the latest updated_at. Keeping the first row would keep stale statuses.

```python
o = o.sort_values("updated_at").drop_duplicates("order_id", keep="last")
```
*(72 caracteres · ~32 s)*

> 🗣️⌨️ Last two lines of cell three: the row counts and the inflated dollars, and the status of the surviving orders.

```python
print(n, len(o), round(total - o.amount.sum(), 2))
o.status.value_counts()
```
*(74 caracteres · ~33 s)*

> 🖱️ I'm clicking the Run button on the left of cell three.

> 🖱️ I'm pointing at the printed line under cell three: 2,362, 2,314, and 11,580.09.

> 🟢 Dropping copies leaves 2,362 rows; keeping the latest version leaves 2,314, exactly the unique IDs from cell one. The duplicates inflated revenue by 11,580 dollars.

> 🖱️ I'm moving the mouse down the status counts below.

> 🟢 No pending left: the old versions were the pending snapshots, so every order kept its final status.

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

**TIME:** 13:15–15:30 (2:15)

**ON SCREEN:** Colab, celda 4 (armada). Señalar las líneas, Run, señalar los cinco números.

**Celda 4 (armada antes de grabar, no se tipea):**

```python
m = c.set_index("customer_id").master_id
o["master_id"] = o.customer_id.map(m)
a = a.drop_duplicates()
a["master_id"] = a.customer_id.map(m)
cust = c[c.customer_id == c.master_id].set_index("master_id")
j = o.join(cust.city, on="master_id", validate="m:1")
bad = o.merge(a, on="master_id")
print(len(o), len(j), len(bad), o.master_id.isna().sum(), a.master_id.isna().sum())
```

**SAY:**

> 🟢 Phase four: connecting orders and activity to the resolved customers, and proving the joins don't multiply rows.

> 🖱️ I'm pointing at the first lines of cell four, prepared before recording: every customer ID mapped to its master ID, in orders and deduplicated activity.

> 🖱️ I'm pointing at the cust line: one row per real person, the master records.

> 🖱️ I'm pointing at the join line in cell four: validate m to 1 makes pandas raise an error if a master ID appeared twice on the customer side.

> 🖱️ I'm pointing at the bad line: the wrong alternative, orders joined directly with activity, kept only for comparison.

> 🖱️ I'm clicking the Run button on the left of cell four.

> 🖱️ I'm pointing at the first two numbers under cell four: 2,314 and 2,314.

> 🟢 The validated join keeps exactly 2,314 orders and raised no error, so each master ID is unique.

> 🖱️ I'm pointing at the third number: 26,047.

> 🟢 The direct join gives 26,047 rows, eleven times the orders; any revenue summed there would be wrong. So I aggregate per customer first.

> 🖱️ I'm pointing at the last two numbers: 14 and 31.

> 🟢 14 orders and 31 events belong to customer IDs that don't exist. They stay out of the features, but they go to the exception report.

**WHY:** `validate="m:1"` convierte un supuesto ("cada cliente aparece una vez") en un control que falla si no se cumple. El join directo de 26.047 filas es la alternativa incorrecta más común: muestra en números por qué se agrega antes de unir.

**EXPECTED RESULT:** `2314 2314 26047 14 31`. Si aparece `MergeError`, la celda 2 no generó un master único: volvé a ejecutar las celdas 2 a 4 en orden.

📘 **What each line does** (para vos, no se lee):

- `m = c.set_index("customer_id").master_id`: a lookup from every customer ID to its master ID.
- `o["master_id"] = o.customer_id.map(m)`: the master ID of each order. Unknown IDs get `NaN`.
- `a = a.drop_duplicates()`: removes duplicate events.
- `a["master_id"] = a.customer_id.map(m)`: the master ID of each event.
- `cust = c[c.customer_id == c.master_id].set_index("master_id")`: only the surviving record of each person, one row per master ID.
- `j = o.join(cust.city, on="master_id", validate="m:1")`: joins each order with its customer's city; raises an error if a master ID repeats on the right side.
- `bad = o.merge(a, on="master_id")`: the wrong join, orders × events, to show the fan-out.
- `print(...)`: orders, rows after the valid join, rows after the wrong join, orphan orders and orphan events.

---

### Fase 6. Variables de comportamiento histórico

**TIME:** 15:30–18:15 (2:45)

**ON SCREEN:** Colab, celda 5 (armada). Señalar las líneas, Run, señalar la línea impresa y la tabla.

**Celda 5 (armada antes de grabar, no se tipea):**

```python
early = a.event_date < a.master_id.map(cust.signup_date)
done = o[(o.status == "completed") & o.master_id.notna()]
f = done.groupby("master_id").agg(orders=("order_id", "size"), spent=("amount", "sum"), last_order=("order_date", "max"))
act = a[~early].groupby("master_id").agg(events=("event_type", "size"), last_seen=("event_date", "max"))
d = cust.join([f, act]).fillna({"orders": 0, "spent": 0, "events": 0})
d["email_n"] = g.email_n.first()
ref = pd.Timestamp("2025-12-31")
d["aov"] = (d.spent / d.orders).round(2)
d["recency_days"] = (ref - d.last_order).dt.days
d["inactive_90"] = ~((ref - d.last_seen).dt.days <= 90)
print("events before signup:", early.sum(), "| orders and events after cutoff:", (o.order_date > ref).sum(), (a.event_date > ref).sum())
d[["orders", "spent", "aov", "events", "recency_days"]].describe().round(1)
```

**SAY:**

> 🟢 Phase five: behavioral features, one row per real customer.

> 🖱️ I'm pointing at cell five, prepared before recording; what matters is the rules inside it.

> 🖱️ I'm pointing at the first line of cell five: an event before the customer's signup is impossible, so I flag it instead of counting it.

> 🖱️ I'm pointing at the second line: only completed orders count as spending, because cancelled and refunded orders aren't revenue.

> 🖱️ I'm moving the mouse over the two agg lines: orders, spending and last order per customer, and events and last activity, each aggregated before the join.

> 🖱️ I'm pointing at the join and email lines: no orders means zero, and the email comes from the first non-empty record, so merging doesn't lose it.

> 🖱️ I'm pointing at the ref line: the cut-off is the end of 2025, and inactive_90 also counts customers with no activity at all.

> 🖱️ I'm clicking the Run button on the left of cell five.

> 🖱️ I'm pointing at the printed line under cell five: 20 events before signup, and zero orders or events after the cut-off.

> 🟢 The 20 are excluded and reported, and nothing is dated after the cut-off.

> 🖱️ I'm pointing at the count row of the table: 500 in orders, but 483 in aov and recency_days.

> 🟢 500 customers; the 17 without a completed order have no order value or recency. That's correct, not a gap.

> 🖱️ I'm pointing at the 50% row: 4 orders, about 406 dollars, and 58 days since the last order.

**WHY:** las reglas (eventos antes del alta, solo pedidos completados, cero en lugar de vacío, email del primer registro no vacío, sin actividad = inactivo) son decisiones de negocio y se explican aunque el código esté armado. El `0 0` demuestra la fecha de corte. El `count` de 483 confirma que el `fillna` solo rellenó lo que debía.

**EXPECTED RESULT:**

- `events before signup: 20 | orders and events after cutoff: 0 0`
- `count`: 500 en `orders`, `spent` y `events`; 483 en `aov` y `recency_days`.
- Fila `50%`: orders 4,0 · spent 406,4 · aov 104,6 · events 10,0 · recency_days 58,0.

📘 **What each line does** (para vos, no se lee):

- `early = a.event_date < a.master_id.map(cust.signup_date)`: True for events dated before their customer's signup.
- `done = o[(o.status == "completed") & o.master_id.notna()]`: completed orders with a known customer.
- `f = done.groupby("master_id").agg(...)`: per customer, the number of orders, total spent and last order date.
- `act = a[~early].groupby("master_id").agg(...)`: per customer, the valid events and the last activity date.
- `d = cust.join([f, act]).fillna({...})`: one row per customer with both feature sets. No orders or events means 0.
- `d["email_n"] = g.email_n.first()`: the first non-empty normalized email of each person (recovers 1 email that the master record lacked).
- `ref = pd.Timestamp("2025-12-31")`: the cut-off date, the end of the data period.
- `d["aov"] = (d.spent / d.orders).round(2)`: average order value.
- `d["recency_days"] = (ref - d.last_order).dt.days`: days since the last completed order.
- `d["inactive_90"] = ~((ref - d.last_seen).dt.days <= 90)`: no activity in the last 90 days; customers with no events at all (`NaT`) also count as inactive.
- `print(...)`: excluded events, and orders and events dated after the cut-off (must be 0).
- `d[[...]].describe().round(1)`: count, mean, quartiles and max of the main features.

---

### Fase 7. Validación de totales

**TIME:** 18:15–19:45 (1:30)

**ON SCREEN:** Colab, celda 6 (armada). Señalar las dos líneas, Run, señalar la salida.

**Celda 6 (armada antes de grabar, no se tipea):**

```python
print(d.index.is_unique, round(d.spent.sum(), 2), round(done.amount.sum(), 2))
print(round(o[o.master_id.isna()].amount.sum(), 2), d.inactive_90.sum(), (d.orders == 0).sum())
```

**SAY:**

> 🟢 Phase six: proving that the consolidated table didn't lose or double any money.

> 🖱️ I'm pointing at the first line of cell six: one row per customer, and the spending in my table against the completed orders it comes from.

> 🖱️ I'm pointing at the second line: the dollars in orphan orders, the inactive customers, and the customers with no completed order.

> 🖱️ I'm clicking the Run button on the left of cell six.

> 🖱️ I'm pointing at the first line under cell six: True, 227,115.94, and 227,115.94.

> 🟢 Each customer appears once, and the two totals match to the cent, so the joins kept every completed dollar.

> 🖱️ I'm pointing at the second line: 1,315.58, 67, and 17.

> 🟢 1,316 dollars sit in orphan orders. 67 customers are inactive, including those with no activity at all, and 17 never completed an order.

**WHY:** cuadrar al centavo es la prueba de que la agregación y los joins no perdieron ni duplicaron dinero. El dinero huérfano se cuantifica para que el negocio decida si vale la pena investigarlo.

**EXPECTED RESULT:**

- `True 227115.94 227115.94`
- `1315.58 67 17`

📘 **What each line does** (para vos, no se lee):

- `print(d.index.is_unique, round(d.spent.sum(), 2), round(done.amount.sum(), 2))`: one row per customer, and the spending total in the final table vs. in the source orders.
- `print(round(o[o.master_id.isna()].amount.sum(), 2), d.inactive_90.sum(), (d.orders == 0).sum())`: the dollars of orphan orders, inactive customers, and customers with no completed orders.

---

### Fase 8. Reporte de excepciones y exportación

**TIME:** 19:45–21:45 (2:00)

**ON SCREEN:** Colab, celda 7 (armada). Señalar las líneas, Run, abrir Files, señalar los archivos, cerrar Files.

**Celda 7 (armada antes de grabar, no se tipea):**

```python
x = pd.concat([conf[["customer_id", "master_id"]].assign(issue="city_conflict"),
               amb[["customer_id", "master_id"]].assign(issue="ambiguous_name"),
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

> 🖱️ I'm pointing at the concat in cell seven, prepared before recording: one table with every unresolved record, its ID and its reason, so nothing disappears without a trace.

> 🖱️ I'm pointing at the to_csv lines: the consolidated customers and the three inputs rewritten, keeping the original email and phone next to the master ID.

> 🖱️ I'm clicking the Run button on the left of cell seven.

> 🖱️ I'm moving the mouse down the counts under cell seven.

> 🟢 64 look-alike records, 31 orphan events, 22 records with a city conflict, 20 events before signup and 14 orphan orders: 151 exceptions, each with its reason.

> 🖱️ I'm clicking the folder icon in the left sidebar, to open the Files panel.

> 🖱️ I'm pointing at customers_consolidated and exceptions_report, the two new files, and at the three inputs, now cleaned and linked by master ID.

> 🖱️ I'm clicking the folder icon again to close the panel.

**WHY:** las excepciones se documentan con su motivo en vez de borrarse. Así cada fila descartada o no fusionada se puede rastrear. Reescribir los archivos de entrada deja la corrección aplicada en la fuente (criterio de Slack); los originales quedan en el Escritorio y en `original/` del ZIP.

**EXPECTED RESULT:**

- `ambiguous_name 64`, `orphan_event 31`, `city_conflict 22`, `event_before_signup 20`, `orphan_order 14`.
- En Files, 5 archivos: `customer_activity.csv` (5.306 filas), `customers.csv` (542 filas, 10 columnas), `customers_consolidated.csv` (500 filas), `exceptions_report.csv` (151 filas) y `orders.csv` (2.314 filas). Si no aparecen, tocá refresh y decí: *"I'm clicking refresh at the top of the Files panel, to show the new files."*

📘 **What each line does** (para vos, no se lee):

- `x = pd.concat([...])`: stacks five exception lists, each with an `issue` label: city conflicts, look-alike people, orphan orders, orphan events and events before signup.
- `x.to_csv("exceptions_report.csv", index=False)`: saves the exception report.
- `d.to_csv("customers_consolidated.csv")`: saves one row per customer with all features. The index is the master ID, so it's kept.
- `c.to_csv("customers.csv", index=False)`: rewrites customers with `email_n`, `phone_n` and `master_id`. The original email and phone stay.
- `o.to_csv("orders.csv", index=False)`: rewrites orders, deduplicated, with `master_id`.
- `a.to_csv("customer_activity.csv", index=False)`: rewrites activity, deduplicated, with `master_id`.
- `x.issue.value_counts()`: the number of exceptions per reason.

---

### Fase 9. Conclusiones

**TIME:** 21:45–23:30 (1:45)

**ON SCREEN:** Colab, + Text abajo de todo, tipear 3 tramos, clic afuera, Cmd + S.

**SAY:**

> 🖱️ I'm clicking plus Text at the top left, to add a text cell at the end of the notebook for the conclusions.

> 🗣️⌨️ In the text cell: the title and the identity result.

```markdown
## Summary
- 542 records are 500 customers; 61 look-alikes kept apart.
```
*(71 caracteres · ~32 s)*

> 🗣️⌨️ Next line of the text cell: the order reconciliation and the validation.

```markdown
- Duplicate orders inflated revenue by $11,580; totals match to the cent.
```
*(73 caracteres · ~32 s)*

> 🗣️⌨️ Last line: what remains unresolved, and the AI declaration.

```markdown
- $1,316 in 14 orders has no customer. Input files generated with AI.
```
*(69 caracteres · ~31 s)*

> 🖱️ I'm clicking on the empty area below the text cell, to show it formatted.

> 🖱️ I'm pressing Command and S to save the notebook; the save message appears at the bottom left.

**EXPECTED RESULT:** la celda de texto con el título y tres viñetas, formateada.

---

### Fase 10. Epilogue

**TIME:** 23:30–24:30 (1:00)

**ON SCREEN:** Colab. Scroll lento hacia arriba. Sin tipear. Recién **después** del epilogue abrís TaskRecorder para detener la grabación.

**SAY:**

> 🖱️ I'm scrolling up slowly through the notebook, from the conclusions back to cell one.

> 🟢 The key decision was the identity key: the phone found all 42 duplicates, I only trusted it after checking that no phone had two emails, and I kept 61 look-alikes apart instead of merging by name.

> 🟢 Every assumption became a check: validate m to 1, a cut-off with nothing after it, and totals that match to the cent. The limitation: shared phones would need a fuzzy name check in a real system, and the city conflicts need a source of truth. Thanks for watching!

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

| Etapa | Fase | Celda | TIME | Duración |
| ----- | ---- | ----- | ---- | -------- |
| Introducción y objetivo | 1 | — | 0:00–1:15 | 1:15 |
| Inspección de archivos (y diagnóstico) | 2 | 1 (armada) | 1:15–3:45 | 2:30 |
| Resolución de identidades (limpieza incluida) | 3 | 2 | 3:45–10:15 | 6:30 |
| Reconciliación de transacciones | 4 | 3 | 10:15–13:15 | 3:00 |
| Consolidación y JOINs | 5 | 4 (armada) | 13:15–15:30 | 2:15 |
| Ingeniería de features | 6 | 5 (armada) | 15:30–18:15 | 2:45 |
| Validaciones | 7 | 6 (armada) | 18:15–19:45 | 1:30 |
| Entregables y cierre | 8, 9, 10 | 7 (armada) + texto | 19:45–24:30 | 4:45 |
| **Total** | | | | **~24,5 min** |

**Margen:** 5,5 minutos hasta 30. **Medilo:** hacé una práctica completa con cronómetro. Si pasa de 27 minutos, recortá **palabras** de las 🟢 (nunca las 🖱️ ni las 🗣️⌨️).

---

## Checklist

**Antes de grabar**

- [ ] Practicá dos veces con cronómetro. `customer_reconstruction.ipynb` tiene el código completo para comparar.
- [ ] En Colab, creá el notebook **customer_reconstruction** con **7 celdas de código**:
  - celdas **1, 4, 5, 6 y 7**: pegá el código de la fase correspondiente;
  - celdas **2 y 3**: vacías;
  - **no ejecutes nada.**
- [ ] En **Files**, subí los tres CSV de esta carpeta (`customers`, `orders`, `customer_activity`). **No los de `_version_financiera/`.** Los de la carpeta son los originales: no los toques.
- [ ] **Tools → Settings → AI assistance**: ocultá las funciones de IA.
- [ ] **Tools → Settings → Editor**: si está la opción, desactivá las sugerencias automáticas de código.
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
- [ ] Armá **Deliverables.zip** con el `.ipynb`, los 5 CSV y la carpeta `original/` con los tres CSV de esta carpeta.
- [ ] Marcá en Studio la opción de archivos generados con IA.
- [ ] Subí por separado el **MP4**, el **ZIP de TaskRecorder**, **Deliverables.zip** y **Metadata.rtf**.
