# bbb169c1 — Billing System Bug Fix

Guion paso a paso para grabar la tarea **bbb169c1** en **Google Colab**: diagnosticar y corregir un error en un script de facturación en **Python**. El script aplica el descuento porcentual mientras va sumando los artículos, en vez de aplicarlo una sola vez sobre el subtotal. En la grabación reproducís el total incorrecto, rastreás el orden del cálculo, lo corregís y creás **tres pruebas unitarias**. La grabación tiene que durar **entre 15:00 y 50:59**. Este guion apunta a unos **21 minutos**, epílogo incluido.

**Cómo leer este guion:**

- Las frases que empiezan con 🖱️ las decís **en el momento de hacer clic, desplazarte o escribir**. Siempre dicen **qué** elemento usás, **dónde** está en la pantalla y **por qué** lo usás. Son las que revisa AutoQC.
- Las frases que empiezan con 🟢 son la explicación que **decís en inglés** entre una acción y otra.
- Debajo de cada bloque de código, la lista **What each line does** explica cada línea en inglés. La leés en voz alta mientras escribís (o señalás) esa línea.
- El resto, en castellano, es lo que hacés en pantalla. Las traducciones aparecen entre paréntesis después de cada frase.

> **Importante:** el Goal de Studio tiene prioridad sobre este guion. Antes de grabar, comparalo con el campo **Describe your idea** de la tarea y **confirmá que Google Colab es una app aprobada para esta tarea**.

---

## Archivos de la carpeta

```
bbb169c1-billing-system-bug-fix/
├── README.md              ← este guion
├── billing.py             ← material de partida: el script CON el error
└── solution/              ← solución de referencia (NO la abras durante la grabación)
    ├── billing.py         ← script corregido
    └── test_billing.py    ← las tres pruebas unitarias
```

---

## El error

`calculate_invoice_total` recibe una lista de artículos (precio y cantidad) y un porcentaje de descuento. El descuento está **adentro** del `for`, así que se aplica después de sumar cada artículo, y los primeros artículos se descuentan varias veces.

Factura de ejemplo, con 10% de descuento:

| Artículo | Precio | Cantidad | Importe |
| -------- | ------ | -------- | ------- |
| Keyboard | 50,00 | 2 | 100,00 |
| Mouse | 25,00 | 1 | 25,00 |
| Monitor | 200,00 | 1 | 200,00 |
| **Subtotal** | | | **325,00** |
| **Total correcto** (325 − 10%) | | | **292,50** |
| **Total que da el script** | | | **273,15** (19,35 de menos) |

Cómo llega el script a 273,15: 100 − 10% = 90 → 90 + 25 = 115 − 10% = 103,50 → 103,50 + 200 = 303,50 − 10% = **273,15**.

**Las pruebas.** Con un solo artículo, el error no se nota, porque el descuento se aplica una sola vez. Por eso las pruebas de "factura normal" (un artículo) y "descuento cero" dan bien con el código viejo y con el nuevo. **La prueba de varios artículos es la que detecta el error**: con el código viejo daría 273,15 en vez de 292,50. Esto lo explicás en el epílogo.

---

## Cómo se trabaja con un script en Colab

Colab es un notebook, pero también puede trabajar con archivos `.py` comunes:

- **Subir y editar:** subís `billing.py` desde el panel **Files**. Con **doble clic** se abre en un **editor de archivos**, en un panel a la derecha. Ahí lo leés y lo modificás.
- **Ejecutar:** en una celda de código, `!python billing.py` ejecuta el script. El `!` le dice a Colab que ejecute un comando de terminal.
- **Crear un archivo:** una celda que empieza con `%%writefile test_billing.py` guarda el resto de la celda como un archivo nuevo con ese nombre.

**Plan B**, por si el editor de archivos no guarda los cambios: en una celda nueva escribís `%%writefile billing.py` en la primera línea, debajo el código corregido completo (el de la sección 9:00–12:00) y la ejecutás. Eso reemplaza el archivo.

---

## Antes de grabar

1. Leé el Goal y compará este guion con el campo **Describe your idea** de Studio.
2. Practicá una vez entera en Colab, leyendo en voz alta las frases 🖱️ y 🟢, y cronometrá. Comprobá que el doble clic abre `billing.py` en el editor y que `Ctrl + S` guarda los cambios. Si no funciona, usá el plan B.
3. Tené **solo** el `billing.py` con el error en una carpeta fácil de encontrar, como el Escritorio. No dejes a mano la carpeta `solution`.
4. Dejá dos pestañas abiertas en Firefox: el documento **Goal** y Colab (https://colab.research.google.com). Agrandá el zoom (`Ctrl + +`).
5. Maximizá el navegador y cerrá o minimizá las demás ventanas, para que ninguna tape a otra.
6. Pausa de ~1 segundo después de cada clic y nunca más de 45 segundos en silencio.
7. No muestres Studio, Mercor, información privada ni herramientas de IA, ni la carpeta `solution`. Cerrá este guion si está en la misma pantalla.

---

## 0:00–0:45 — Mostrar el Goal

> 🖱️ I'm on the Goal document in the first browser tab, to show what this task asks for.
>
> (Estoy en el documento del Goal, en la primera pestaña del navegador, para mostrar qué pide esta tarea.)
>
> 🟢 As a developer maintaining a billing system, I'll fix a bug where the percentage discount is applied while the items are being added, instead of once on the subtotal. I'll reproduce it, trace it, fix it, and add three unit tests.
>
> (Como desarrollador que mantiene un sistema de facturación, voy a corregir un error en el que el descuento porcentual se aplica mientras se suman los artículos, en vez de una sola vez sobre el subtotal. Lo voy a reproducir, rastrear y corregir, y voy a agregar tres pruebas unitarias.)

---

## 0:45–5:00 — Abrir Colab, subir e inspeccionar el script

> 🖱️ I'm clicking the second browser tab, at the top of the window, to open Google Colab.
>
> (Hago clic en la segunda pestaña del navegador, arriba de la ventana, para abrir Google Colab.)
>
> 🟢 I'll work in Google Colab. It runs Python in the browser, so I can open the script, run it, and test it without installing anything.
>
> (Voy a trabajar en Google Colab. Ejecuta Python en el navegador, así que puedo abrir el script, ejecutarlo y probarlo sin instalar nada.)
>
> 🖱️ I'm clicking the New notebook button at the bottom of the Open notebook dialog, to create a fresh notebook.
>
> (Hago clic en el botón New notebook, abajo del cuadro Open notebook, para crear un notebook nuevo.)
>
> 🖱️ I'm clicking the notebook title field at the top left, and typing billing_bug_fix.ipynb, to identify this work.
>
> (Hago clic en el campo del título del notebook, arriba a la izquierda, y escribo billing_bug_fix.ipynb, para identificar este trabajo.)
>
> 🖱️ I'm clicking the Files icon, the folder in the left sidebar, to upload the billing script.
>
> (Hago clic en el ícono Files, la carpeta de la barra lateral izquierda, para subir el script de facturación.)
>
> 🖱️ I'm clicking the Upload to session storage icon, at the top of the Files pane, and choosing billing.py from my computer.
>
> (Hago clic en el ícono Upload to session storage, arriba del panel Files, y elijo billing.py de mi computadora.)

Si aparece un aviso: *"I'm clicking OK on this warning, in the center of the screen, to continue the upload."*

> 🖱️ I'm double-clicking billing.py in the Files pane on the left, to open it in Colab's file editor on the right.
>
> (Hago doble clic en billing.py en el panel Files de la izquierda, para abrirlo en el editor de archivos de Colab, a la derecha.)

Recorrés el código con el mouse, señalando cada línea mientras la explicás:

```python
def calculate_invoice_total(items, discount_percent):
    """Return the invoice total after applying a percentage discount."""
    total = 0.0
    for item in items:
        total += item["price"] * item["quantity"]
        total -= total * discount_percent / 100
    return round(total, 2)


if __name__ == "__main__":
    invoice_items = [
        {"name": "Keyboard", "price": 50.00, "quantity": 2},
        {"name": "Mouse", "price": 25.00, "quantity": 1},
        {"name": "Monitor", "price": 200.00, "quantity": 1},
    ]
    print("Invoice total:", calculate_invoice_total(invoice_items, 10))
```

**What each line does:**

- 🟢 `def calculate_invoice_total(items, discount_percent):`: this function receives the invoice items and the discount percentage, and returns the total.
- 🟢 `"""Return the invoice total..."""`: this docstring describes what the function should do: apply a percentage discount to the invoice.
- 🟢 `total = 0.0`: the total starts at zero.
- 🟢 `for item in items:`: the loop goes through the items one by one.
- 🟢 `total += item["price"] * item["quantity"]`: for each item, it adds the price times the quantity to the total.
- 🟢 `total -= total * discount_percent / 100`: then it subtracts the discount from the total. Notice this line is indented inside the loop, so it runs once for every item. I'll come back to this.
- 🟢 `return round(total, 2)`: it returns the total rounded to two decimals, like money.
- 🟢 `if __name__ == "__main__":`: this block only runs when I run the file directly. It creates a sample invoice with three items and prints its total with a 10 percent discount.

---

## 5:00–9:00 — Reproducir el error y rastrear el cálculo

> 🖱️ I'm clicking the plus Text button in the toolbar at the top left, to add a heading for this step.
>
> (Hago clic en el botón + Text de la barra de herramientas, arriba a la izquierda, para agregar un título para este paso.)

Escribís `## 1. Reproduce the bug`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that runs the script.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que ejecuta el script.)

```python
!python billing.py
```

**What each line does:**

- 🟢 `!python billing.py`: the exclamation mark tells Colab to run a terminal command. This command runs billing.py with Python, just like on a normal computer.

> 🖱️ I'm clicking the Run cell button, the play icon to the left of this cell, to reproduce the invoice total.
>
> (Hago clic en el botón Run cell, el ícono de play a la izquierda de esta celda, para reproducir el total de la factura.)

Debajo aparece `Invoice total: 273.15`.

> 🟢 The script says the total is 273.15. Let me calculate it by hand. Two keyboards at 50 dollars is 100, plus a 25-dollar mouse, plus a 200-dollar monitor. The subtotal is 325 dollars. Ten percent of 325 is 32.50, so the correct total is 292.50. The script charges 19.35 dollars less than it should. I've reproduced the bug.
>
> (El script dice que el total es 273,15. Lo calculo a mano. Dos teclados a 50 dólares son 100, más un mouse de 25, más un monitor de 200. El subtotal es 325 dólares. El 10 por ciento de 325 es 32,50, así que el total correcto es 292,50. El script cobra 19,35 dólares menos de lo que debería. Reproduje el error.)

Para rastrear el cálculo, agregás una línea temporal en el editor:

> 🖱️ I'm clicking at the end of the discount line in the file editor on the right, and pressing Enter, to add a temporary print that shows the running total.
>
> (Hago clic al final de la línea del descuento en el editor de archivos de la derecha, y presiono Enter, para agregar un print temporal que muestra el total parcial.)

Escribís, con la misma sangría que la línea de arriba:

```python
        print("After", item["name"], "running total:", round(total, 2))
```

**What each line does:**

- 🟢 `print("After", item["name"], "running total:", round(total, 2))`: this prints the total after each item, so I can see the order of the calculation step by step. It's temporary: I'll remove it after the fix.

> 🖱️ I'm pressing Control and S to save the file, and clicking the Run cell button to the left of the same cell, to run the script again and trace the calculation.
>
> (Presiono Control y S para guardar el archivo, y hago clic en el botón Run cell a la izquierda de la misma celda, para ejecutar el script de nuevo y rastrear el cálculo.)

Debajo aparece:

```
After Keyboard running total: 90.0
After Mouse running total: 103.5
After Monitor running total: 273.15
Invoice total: 273.15
```

> 🟢 Now I can see the problem. After the keyboards, the total is 90: the 10 percent discount was already applied. Then the mouse is added, and the discount is applied again to everything, including the keyboards. And again after the monitor.
>
> (Ahora veo el problema. Después de los teclados, el total es 90: ya se aplicó el 10 por ciento de descuento. Después se suma el mouse y el descuento se aplica de nuevo a todo, incluidos los teclados. Y otra vez después del monitor.)
>
> 🟢 So the keyboards got the discount three times, the mouse twice, and the monitor once. The root cause is the order of operations: the discount is inside the loop, so it runs for every item. It should run once, after the loop, on the subtotal.
>
> (Entonces los teclados tuvieron el descuento tres veces, el mouse dos y el monitor una. La causa de fondo es el orden de las operaciones: el descuento está adentro del loop, así que se ejecuta con cada artículo. Tendría que ejecutarse una sola vez, después del loop, sobre el subtotal.)

---

## 9:00–12:00 — Corregir el cálculo

> 🖱️ I'm selecting the body of the function in the file editor on the right, from the total line down to the return line, to replace it with the corrected logic.
>
> (Selecciono el cuerpo de la función en el editor de archivos de la derecha, desde la línea de total hasta la del return, para reemplazarlo con la lógica corregida.)

Escribís el cuerpo nuevo. La función queda así:

```python
def calculate_invoice_total(items, discount_percent):
    """Return the invoice total after applying a percentage discount."""
    subtotal = 0.0
    for item in items:
        subtotal += item["price"] * item["quantity"]
    discount = subtotal * discount_percent / 100
    return round(subtotal - discount, 2)
```

**What each line does:**

- 🟢 `subtotal = 0.0`: I renamed total to subtotal, so the name says what the variable really holds before the discount.
- 🟢 `for item in items:`: the loop still goes through every item.
- 🟢 `subtotal += item["price"] * item["quantity"]`: now the loop only adds the items. There's no discount inside it.
- 🟢 `discount = subtotal * discount_percent / 100`: this line is outside the loop, so the discount is calculated only once, on the full subtotal.
- 🟢 `return round(subtotal - discount, 2)`: the total is the subtotal minus the discount, rounded to two decimals.

Con el cambio también desaparece el `print` temporal.

> 🖱️ I'm pressing Control and S to save, and clicking the Run cell button to the left of the same cell, to check the fix.
>
> (Presiono Control y S para guardar, y hago clic en el botón Run cell a la izquierda de la misma celda, para comprobar la corrección.)

Debajo aparece `Invoice total: 292.5`.

> 🟢 Now the total is 292.5, which is the 292.50 I calculated by hand. Python doesn't show the last zero, but the value is the same.
>
> (Ahora el total es 292,5, que es el 292,50 que calculé a mano. Python no muestra el último cero, pero el valor es el mismo.)

---

## 12:00–16:30 — Las tres pruebas unitarias

> 🟢 The fix works for this invoice, but I want to make sure the bug never comes back. For that, I'll write unit tests: small programs that check the function automatically, every time we run them.
>
> (La corrección funciona para esta factura, pero quiero asegurarme de que el error no vuelva. Para eso voy a escribir pruebas unitarias: pequeños programas que revisan la función automáticamente, cada vez que los ejecutamos.)
>
> 🖱️ I'm clicking the plus Text button in the toolbar, to add a heading for the tests.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título para las pruebas.)

Escribís `## 2. Unit tests`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that creates the test file.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que crea el archivo de pruebas.)

Escribís la celda:

```python
%%writefile test_billing.py
import unittest

from billing import calculate_invoice_total


class TestInvoiceTotal(unittest.TestCase):
    def test_normal_invoice(self):
        items = [{"name": "Keyboard", "price": 50.00, "quantity": 2}]
        self.assertEqual(calculate_invoice_total(items, 10), 90.00)

    def test_zero_discount(self):
        items = [{"name": "Mouse", "price": 25.00, "quantity": 3}]
        self.assertEqual(calculate_invoice_total(items, 0), 75.00)

    def test_multiple_items(self):
        items = [
            {"name": "Keyboard", "price": 50.00, "quantity": 2},
            {"name": "Mouse", "price": 25.00, "quantity": 1},
            {"name": "Monitor", "price": 200.00, "quantity": 1},
        ]
        self.assertEqual(calculate_invoice_total(items, 10), 292.50)


if __name__ == "__main__":
    unittest.main()
```

**What each line does:**

- 🟢 `%%writefile test_billing.py`: this first line tells Colab to save the rest of the cell as a file called test_billing.py, instead of running it. This way, the tests live in their own file, next to billing.py.
- 🟢 `import unittest`: unittest is Python's built-in testing library, so there's nothing to install.
- 🟢 `from billing import calculate_invoice_total`: this imports the function I want to test from billing.py.
- 🟢 `class TestInvoiceTotal(unittest.TestCase):`: a test class groups the tests. Every method whose name starts with test is one test.
- 🟢 `def test_normal_invoice(self):`: the first test is a normal invoice: two keyboards at 50 dollars with a 10 percent discount. 100 minus 10 percent is 90.
- 🟢 `self.assertEqual(calculate_invoice_total(items, 10), 90.00)`: assertEqual checks that the function returns exactly the expected value. If it doesn't, the test fails.
- 🟢 `def test_zero_discount(self):`: the second test uses zero discount: three mice at 25 dollars must cost exactly 75. This checks that the function doesn't change the total when there's no discount.
- 🟢 `def test_multiple_items(self):`: the third test uses several items: the same invoice as the bug, which must cost 292.50. This is the test that catches this bug, because the error only appears with more than one item.
- 🟢 `if __name__ == "__main__": unittest.main()`: this lets me run the tests by running the file directly.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to save the test file.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para guardar el archivo de pruebas.)
>
> 🟢 Colab says "Writing test_billing.py", and the new file appears in the Files pane on the left, next to billing.py.
>
> (Colab dice "Writing test_billing.py", y el archivo nuevo aparece en el panel Files de la izquierda, al lado de billing.py.)
>
> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that runs all the tests.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que ejecuta todas las pruebas.)

```python
!python -m unittest -v
```

**What each line does:**

- 🟢 `!python -m unittest -v`: this runs unittest from the terminal. It finds every file whose name starts with test, runs all its tests, and the -v option, for verbose, shows each test by name.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to run the tests.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para ejecutar las pruebas.)

Debajo aparecen las tres pruebas con `ok`, después `Ran 3 tests` y al final `OK`.

> 🟢 All three tests pass: multiple items, normal invoice, and zero discount, all ok. "Ran 3 tests" and "OK" at the end confirm the corrected results.
>
> (Las tres pruebas pasan: varios artículos, factura normal y descuento cero, todas ok. "Ran 3 tests" y "OK" al final confirman los resultados corregidos.)

---

## 16:30–17:30 — Verificación final y descarga

> 🖱️ I'm scrolling through billing.py in the file editor on the right, to review the final code once more.
>
> (Recorro billing.py en el editor de archivos de la derecha, para revisar el código final una vez más.)
>
> 🟢 Let me verify: the temporary print is gone, the discount is outside the loop, the script prints 292.5, and the three tests pass.
>
> (Verifico: el print temporal ya no está, el descuento está afuera del loop, el script imprime 292,5 y las tres pruebas pasan.)
>
> 🖱️ I'm right-clicking billing.py in the Files pane on the left and choosing Download, and doing the same with test_billing.py, to save the two deliverables.
>
> (Hago clic derecho en billing.py en el panel Files de la izquierda y elijo Download, y hago lo mismo con test_billing.py, para guardar los dos entregables.)

Los archivos subidos a Colab se borran cuando se cierra la sesión, así que **descargalos antes de cerrar**.

---

## 17:30–21:00 — Epílogo (3–4 minutos)

Revisá en las reglas de Odin qué tiene que tener el epílogo y ajustá este texto si piden algo distinto.

> 🖱️ I'm scrolling slowly up through the notebook with the mouse wheel, to go over the steps.
>
> (Subo despacio por el notebook con la rueda del mouse, para repasar los pasos.)
>
> 🟢 In this epilogue, I want to go over my approach. First, I reproduced the bug and calculated the right answer by hand, so I knew exactly what "correct" meant before changing anything.
>
> (En este epílogo quiero repasar mi enfoque. Primero reproduje el error y calculé a mano la respuesta correcta, así sabía exactamente qué era "correcto" antes de cambiar nada.)
>
> 🟢 Then I traced the calculation with a temporary print. That showed the root cause: one line in the wrong place. The discount was inside the loop, so the first items were discounted several times. The fix was small, moving the discount out of the loop, but finding the exact cause is what makes a fix safe.
>
> (Después rastreé el cálculo con un print temporal. Eso mostró la causa de fondo: una línea en el lugar equivocado. El descuento estaba adentro del loop, así que los primeros artículos se descontaban varias veces. La corrección fue chica, sacar el descuento del loop, pero encontrar la causa exacta es lo que hace que una corrección sea segura.)
>
> 🟢 An interesting detail: with one item, the old code gave the right answer, because the discount ran only once. So the normal invoice and zero discount tests would pass even with the bug. The multiple items test is the one that protects us. With the old code, it would get 273.15 instead of 292.50 and fail. That's why testing several items matters.
>
> (Un detalle interesante: con un solo artículo, el código viejo daba bien, porque el descuento se ejecutaba una sola vez. Entonces las pruebas de factura normal y de descuento cero pasarían incluso con el error. La prueba de varios artículos es la que nos protege. Con el código viejo obtendría 273,15 en vez de 292,50 y fallaría. Por eso importa probar varios artículos.)
>
> 🟢 I kept the code and the tests as separate .py files, not just notebook cells, because in a real billing system they would live in the project and run automatically before every change.
>
> (Dejé el código y las pruebas como archivos .py separados, no solo como celdas del notebook, porque en un sistema de facturación real estarían en el proyecto y se ejecutarían automáticamente antes de cada cambio.)
>
> 🟢 As next steps, I would add tests for edge cases, like an empty invoice, a 100 percent discount, or an invalid negative discount, and decide how the function should handle them. For real money, I would also use Python's Decimal type instead of floats, to avoid small rounding errors. Thanks for watching!
>
> (Como próximos pasos, agregaría pruebas para casos límite, como una factura vacía, un descuento del 100 por ciento o un descuento negativo inválido, y definiría cómo tiene que manejarlos la función. Para dinero real, también usaría el tipo Decimal de Python en vez de floats, para evitar pequeños errores de redondeo. ¡Gracias por mirar!)

Si el reloj todavía no pasó los 15:00, no cortes: volvé a explicar el rastreo paso por paso con los números de la tabla de arriba.

---

## Después de grabar

1. Ejecutá **Run full AutoQC**, no solo *Rerun failing*.
2. Subí los **cuatro archivos por separado**: el **MP4**, el **ZIP original de TaskRecorder**, **Deliverables.zip** (con `billing.py` corregido y `test_billing.py`; si querés, también el notebook desde **File → Download → Download .ipynb**) y **Metadata.rtf**.
