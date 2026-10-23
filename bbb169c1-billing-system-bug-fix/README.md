# bbb169c1 — Billing System Bug Fix

Guion paso a paso para grabar la tarea **bbb169c1**: diagnosticar y corregir un error en un script de facturación en **Python**. El script aplica el descuento porcentual mientras va sumando los artículos, en vez de aplicarlo una sola vez sobre el subtotal. En la grabación reproducís el total incorrecto, rastreás el orden del cálculo, lo corregís y creás **tres pruebas unitarias**. La grabación tiene que durar **entre 15:00 y 50:59**. Este guion apunta a unos **21 minutos**, epílogo incluido.

**Cómo leer este guion:**

- Las frases que empiezan con 🖱️ las decís **en el momento de hacer clic, desplazarte o escribir**. Siempre dicen **qué** elemento usás, **dónde** está en la pantalla y **por qué** lo usás. Son las que revisa AutoQC.
- Las frases que empiezan con 🟢 son la explicación que **decís en inglés** entre una acción y otra.
- Debajo de cada bloque de código, la lista **What each line does** explica cada línea en inglés. La leés en voz alta mientras escribís (o señalás) esa línea.
- El resto, en castellano, es lo que hacés en pantalla. Las traducciones aparecen entre paréntesis después de cada frase.

> **Importante:** el Goal de Studio tiene prioridad sobre este guion. Antes de grabar, comparalo con el campo **Describe your idea** de la tarea y confirmá qué apps están aprobadas. Este guion usa **Visual Studio Code** y su terminal.

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

## Antes de grabar

1. Leé el Goal y compará este guion con el campo **Describe your idea** de Studio.
2. **Instalá Python 3** en la computadora donde vas a grabar (https://www.python.org/downloads/; en el instalador marcá **Add python.exe to PATH**). En esta PC no hay Python instalado. Comprobá en una terminal que `python --version` funcione. Si no funciona, probá con `py`, y en ese caso usá `py` en lugar de `python` en todo el guion.
3. Copiá **solo** `billing.py` (el que tiene el error) a una carpeta nueva y limpia, por ejemplo `Escritorio\billing-system`. No copies la carpeta `solution`.
4. Practicá una vez entera, leyendo en voz alta las frases 🖱️ y 🟢, y cronometrá. Después volvé a copiar el `billing.py` con el error.
5. Dejá abiertos el documento **Goal** en Firefox y VS Code (sin ninguna carpeta abierta). Agrandá la letra de VS Code (`Ctrl + +`).
6. Maximizá la ventana que estés mostrando y cerrá o minimizá las demás, para que ninguna tape a otra.
7. Pausa de ~1 segundo después de cada clic y nunca más de 45 segundos en silencio.
8. No muestres Studio, Mercor, información privada ni herramientas de IA, ni la carpeta `solution`. Cerrá este guion si está en la misma pantalla.

---

## 0:00–0:45 — Mostrar el Goal

> 🖱️ I'm on the Goal document in the browser, to show what this task asks for.
>
> (Estoy en el documento del Goal, en el navegador, para mostrar qué pide esta tarea.)
>
> 🟢 As a developer maintaining a billing system, I'll fix a bug where the percentage discount is applied while the items are being added, instead of once on the subtotal. I'll reproduce it, trace it, fix it, and add three unit tests.
>
> (Como desarrollador que mantiene un sistema de facturación, voy a corregir un error en el que el descuento porcentual se aplica mientras se suman los artículos, en vez de una sola vez sobre el subtotal. Lo voy a reproducir, rastrear y corregir, y voy a agregar tres pruebas unitarias.)

---

## 0:45–5:00 — Abrir e inspeccionar el script

> 🖱️ I'm clicking the VS Code icon in the taskbar at the bottom of the screen, to open the code editor.
>
> (Hago clic en el ícono de VS Code en la barra de tareas, abajo de la pantalla, para abrir el editor de código.)
>
> 🖱️ I'm opening the File menu at the top left and choosing Open Folder, to open the billing project.
>
> (Abro el menú File, arriba a la izquierda, y elijo Open Folder, para abrir el proyecto de facturación.)
>
> 🖱️ I'm selecting the billing-system folder on the Desktop and clicking the Select Folder button at the bottom right of the dialog.
>
> (Selecciono la carpeta billing-system en el Escritorio y hago clic en el botón Select Folder, abajo a la derecha del cuadro.)

Si VS Code pregunta si confiás en los autores: *"I'm clicking Yes, I trust the authors, in the center of the dialog, because this is my own project folder."*

> 🖱️ I'm clicking billing.py in the Explorer panel on the left, to open the billing script.
>
> (Hago clic en billing.py en el panel Explorer de la izquierda, para abrir el script de facturación.)

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

> 🖱️ I'm opening the Terminal menu at the top of VS Code and choosing New Terminal, to run the script.
>
> (Abro el menú Terminal, arriba de VS Code, y elijo New Terminal, para ejecutar el script.)
>
> 🖱️ I'm typing python billing.py in the terminal at the bottom of the window, and pressing Enter, to reproduce the invoice total.
>
> (Escribo python billing.py en la terminal, abajo de la ventana, y presiono Enter, para reproducir el total de la factura.)

La terminal muestra `Invoice total: 273.15`.

> 🟢 The script says the total is 273.15. Let me calculate it by hand. Two keyboards at 50 dollars is 100, plus a 25-dollar mouse, plus a 200-dollar monitor. The subtotal is 325 dollars. Ten percent of 325 is 32.50, so the correct total is 292.50. The script charges 19.35 dollars less than it should. I've reproduced the bug.
>
> (El script dice que el total es 273,15. Lo calculo a mano. Dos teclados a 50 dólares son 100, más un mouse de 25, más un monitor de 200. El subtotal es 325 dólares. El 10 por ciento de 325 es 32,50, así que el total correcto es 292,50. El script cobra 19,35 dólares menos de lo que debería. Reproduje el error.)

Para rastrear el cálculo, agregás una línea temporal:

> 🖱️ I'm clicking at the end of the discount line, line 6 in the editor, and pressing Enter, to add a temporary print that shows the running total.
>
> (Hago clic al final de la línea del descuento, la línea 6 del editor, y presiono Enter, para agregar un print temporal que muestra el total parcial.)

Escribís, con la misma sangría que la línea de arriba:

```python
        print("After", item["name"], "running total:", round(total, 2))
```

**What each line does:**

- 🟢 `print("After", item["name"], "running total:", round(total, 2))`: this prints the total after each item, so I can see the order of the calculation step by step. It's temporary: I'll remove it after the fix.

> 🖱️ I'm pressing Control and S to save the file, and then clicking in the terminal at the bottom and running python billing.py again, to trace the calculation.
>
> (Presiono Control y S para guardar el archivo, y después hago clic en la terminal de abajo y ejecuto python billing.py otra vez, para rastrear el cálculo.)

La terminal muestra:

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

> 🖱️ I'm selecting the body of the function in the editor, from line 3 to line 8, to replace it with the corrected logic.
>
> (Selecciono el cuerpo de la función en el editor, de la línea 3 a la 8, para reemplazarlo con la lógica corregida.)

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

> 🖱️ I'm pressing Control and S to save, and running python billing.py again in the terminal at the bottom, to check the fix.
>
> (Presiono Control y S para guardar y ejecuto python billing.py otra vez en la terminal de abajo, para comprobar la corrección.)

La terminal muestra `Invoice total: 292.5`.

> 🟢 Now the total is 292.5, which is the 292.50 I calculated by hand. Python doesn't show the last zero, but the value is the same.
>
> (Ahora el total es 292,5, que es el 292,50 que calculé a mano. Python no muestra el último cero, pero el valor es el mismo.)

---

## 12:00–16:30 — Las tres pruebas unitarias

> 🟢 The fix works for this invoice, but I want to make sure the bug never comes back. For that, I'll write unit tests: small programs that check the function automatically, every time we run them.
>
> (La corrección funciona para esta factura, pero quiero asegurarme de que el error no vuelva. Para eso voy a escribir pruebas unitarias: pequeños programas que revisan la función automáticamente, cada vez que los ejecutamos.)
>
> 🖱️ I'm clicking the New File icon next to the folder name, at the top of the Explorer panel on the left, and typing test_billing.py, to create the test file.
>
> (Hago clic en el ícono New File al lado del nombre de la carpeta, arriba del panel Explorer de la izquierda, y escribo test_billing.py, para crear el archivo de pruebas.)
>
> 🖱️ I'm typing in the new test_billing.py tab in the editor, to write the tests.
>
> (Escribo en la pestaña nueva de test_billing.py del editor, para escribir las pruebas.)

Escribís el archivo de pruebas:

```python
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

- 🟢 `import unittest`: unittest is Python's built-in testing library, so there's nothing to install.
- 🟢 `from billing import calculate_invoice_total`: this imports the function I want to test from billing.py.
- 🟢 `class TestInvoiceTotal(unittest.TestCase):`: a test class groups the tests. Every method whose name starts with test is one test.
- 🟢 `def test_normal_invoice(self):`: the first test is a normal invoice: two keyboards at 50 dollars with a 10 percent discount. 100 minus 10 percent is 90.
- 🟢 `self.assertEqual(calculate_invoice_total(items, 10), 90.00)`: assertEqual checks that the function returns exactly the expected value. If it doesn't, the test fails.
- 🟢 `def test_zero_discount(self):`: the second test uses zero discount: three mice at 25 dollars must cost exactly 75. This checks that the function doesn't change the total when there's no discount.
- 🟢 `def test_multiple_items(self):`: the third test uses several items: the same invoice as the bug, which must cost 292.50. This is the test that catches this bug, because the error only appears with more than one item.
- 🟢 `if __name__ == "__main__": unittest.main()`: this lets me run the tests by running the file directly.

> 🖱️ I'm pressing Control and S to save the test file, and then clicking in the terminal at the bottom and typing python -m unittest -v, to run all the tests.
>
> (Presiono Control y S para guardar el archivo de pruebas, y después hago clic en la terminal de abajo y escribo python -m unittest -v, para ejecutar todas las pruebas.)

La terminal muestra las tres pruebas con `ok`, después `Ran 3 tests` y al final `OK`.

> 🟢 All three tests pass. The -v option, for verbose, shows each test by name: multiple items, normal invoice, and zero discount, all ok. "Ran 3 tests" and "OK" at the end confirm the corrected results.
>
> (Las tres pruebas pasan. La opción -v, de verbose, muestra cada prueba por su nombre: varios artículos, factura normal y descuento cero, todas ok. "Ran 3 tests" y "OK" al final confirman los resultados corregidos.)

---

## 16:30–17:30 — Verificación final

> 🖱️ I'm clicking the billing.py tab at the top of the editor, to review the final code once more.
>
> (Hago clic en la pestaña billing.py, arriba del editor, para revisar el código final una vez más.)
>
> 🟢 Let me verify: the temporary print is gone, the discount is outside the loop, the script prints 292.5, and the three tests pass. The deliverables are the corrected billing.py and the test file, test_billing.py.
>
> (Verifico: el print temporal ya no está, el descuento está afuera del loop, el script imprime 292,5 y las tres pruebas pasan. Los entregables son el billing.py corregido y el archivo de pruebas, test_billing.py.)

---

## 17:30–21:00 — Epílogo (3–4 minutos)

Revisá en las reglas de Odin qué tiene que tener el epílogo y ajustá este texto si piden algo distinto.

> 🖱️ I'm scrolling slowly through billing.py in the editor with the mouse wheel, to go over the fix.
>
> (Recorro despacio billing.py en el editor con la rueda del mouse, para repasar la corrección.)
>
> 🟢 In this epilogue, I want to go over my approach. First, I reproduced the bug and calculated the right answer by hand, so I knew exactly what "correct" meant before changing anything.
>
> (En este epílogo quiero repasar mi enfoque. Primero reproduje el error y calculé a mano la respuesta correcta, así sabía exactamente qué era "correcto" antes de cambiar nada.)
>
> 🟢 Then I traced the calculation with a temporary print. That showed the root cause: one line in the wrong place. The discount was inside the loop, so the first items were discounted several times. The fix was small, moving the discount out of the loop, but finding the exact cause is what makes a fix safe.
>
> (Después rastreé el cálculo con un print temporal. Eso mostró la causa de fondo: una línea en el lugar equivocado. El descuento estaba adentro del loop, así que los primeros artículos se descontaban varias veces. La corrección fue chica, sacar el descuento del loop, pero encontrar la causa exacta es lo que hace que una corrección sea segura.)
>
> 🖱️ I'm clicking the test_billing.py tab at the top of the editor, to talk about the tests.
>
> (Hago clic en la pestaña test_billing.py, arriba del editor, para hablar de las pruebas.)
>
> 🟢 An interesting detail: with one item, the old code gave the right answer, because the discount ran only once. So the normal invoice and zero discount tests would pass even with the bug. The multiple items test is the one that protects us. With the old code, it would get 273.15 instead of 292.50 and fail. That's why testing several items matters.
>
> (Un detalle interesante: con un solo artículo, el código viejo daba bien, porque el descuento se ejecutaba una sola vez. Entonces las pruebas de factura normal y de descuento cero pasarían incluso con el error. La prueba de varios artículos es la que nos protege. Con el código viejo obtendría 273,15 en vez de 292,50 y fallaría. Por eso importa probar varios artículos.)
>
> 🟢 As next steps, I would add tests for edge cases, like an empty invoice, a 100 percent discount, or an invalid negative discount, and decide how the function should handle them. For real money, I would also use Python's Decimal type instead of floats, to avoid small rounding errors. Thanks for watching!
>
> (Como próximos pasos, agregaría pruebas para casos límite, como una factura vacía, un descuento del 100 por ciento o un descuento negativo inválido, y definiría cómo tiene que manejarlos la función. Para dinero real, también usaría el tipo Decimal de Python en vez de floats, para evitar pequeños errores de redondeo. ¡Gracias por mirar!)

Si el reloj todavía no pasó los 15:00, no cortes: volvé a explicar el rastreo paso por paso con los números de la tabla de arriba.

---

## Después de grabar

1. Ejecutá **Run full AutoQC**, no solo *Rerun failing*.
2. Subí los **cuatro archivos por separado**: el **MP4**, el **ZIP original de TaskRecorder**, **Deliverables.zip** (con `billing.py` corregido y `test_billing.py`) y **Metadata.rtf**.
