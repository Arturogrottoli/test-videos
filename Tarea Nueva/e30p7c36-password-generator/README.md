# e30p7c36 — Password Generator & Strength Validator

Guion paso a paso para grabar la tarea **e30p7c36**: programar en **Google Colab**, con **Python**, un generador de contraseñas con opciones configurables y un validador de fortaleza. El validador evalúa la longitud, la variedad de caracteres, las secuencias repetidas y la entropía. Después generás 10 contraseñas, las mostrás en una tabla de **pandas**, encontrás la más débil y la más fuerte, y escribís conclusiones. La grabación tiene que durar **entre 15:00 y 50:59**. Este guion apunta a unos **25 minutos**, epílogo incluido.

**Cómo leer este guion:**

- Las frases que empiezan con 🖱️ las decís **en el momento de hacer clic, desplazarte o escribir**. Siempre dicen **qué** elemento usás, **dónde** está en la pantalla y **por qué** lo usás. Son las que revisa AutoQC.
- Las frases que empiezan con 🟢 son la explicación que **decís en inglés** entre una acción y otra.
- Debajo de cada bloque de código, la lista **What each line does** explica cada línea en inglés. La leés en voz alta mientras escribís esa línea.
- El resto, en castellano, es lo que hacés en pantalla. Las traducciones aparecen entre paréntesis después de cada frase.

> **Importante:** el Goal de Studio tiene prioridad sobre este guion. Si el Goal define otros nombres de funciones, otros criterios o otras etiquetas, seguí los del Goal. La tarea arranca desde cero, sin archivos externos.

---

## Archivos de la carpeta

```
e30p7c36-password-generator/
├── README.md             ← este guion
└── password_tool.ipynb   ← notebook de referencia, completo y en orden
```

Para probar el notebook de referencia: en https://colab.research.google.com elegís **File → Upload notebook**, seleccionás `password_tool.ipynb` y ejecutás **Runtime → Run all**. No hace falta subir ningún archivo.

---

## Cómo se calcula el puntaje

`check_strength()` da de **0 a 9 puntos**:

| Criterio | Puntos |
| -------- | ------ |
| Longitud: 8 o más, 12 o más, 16 o más caracteres | +1 por cada uno (hasta 3) |
| Variedad: minúsculas, mayúsculas, dígitos, símbolos | +1 por cada tipo presente (hasta 4) |
| Entropía: 60 bits o más, 80 bits o más | +1 por cada uno (hasta 2) |
| Secuencias repetidas (`aaa` o `abab`) | −1 |

**Etiqueta:** 8 o más = **Strong**, de 5 a 7 = **Medium**, 4 o menos = **Weak**.

**Entropía** = longitud × log₂(tamaño del conjunto de caracteres). El conjunto tiene 26 minúsculas, +26 mayúsculas, +10 dígitos y +32 símbolos (los de `string.punctuation`).

**Valores de referencia.** Las contraseñas cambian en cada ejecución, porque son aleatorias, pero los puntajes no, porque `generate_password` garantiza al menos un carácter de cada tipo elegido. Lo probé con 20.000 contraseñas por configuración:

| # | Longitud | Mayúsc. | Dígitos | Símbolos | Entropía | Puntaje | Etiqueta |
| -: | -: | :-: | :-: | :-: | -: | -: | -------- |
| 1 | 6 | – | – | – | 28,2 | 1 | Weak |
| 2 | 8 | – | – | – | 37,6 | 2 | Weak |
| 3 | 8 | ✓ | – | – | 45,6 | 3 | Weak |
| 4 | 8 | ✓ | ✓ | – | 47,6 | 4 | Weak |
| 5 | 10 | ✓ | ✓ | ✓ | 65,5 | 6 | Medium |
| 6 | 12 | ✓ | ✓ | – | 71,5 | 6 | Medium |
| 7 | 12 | ✓ | ✓ | ✓ | 78,7 | 7 | Medium |
| 8 | 16 | ✓ | ✓ | – | 95,3 | 8 | Strong |
| 9 | 16 | ✓ | ✓ | ✓ | 104,9 | 9 | Strong |
| 10 | 20 | ✓ | ✓ | ✓ | 131,1 | 9 | Strong |

La más débil es la #1. La más fuerte es la #10: empata en puntaje con la #9, pero tiene más entropía.

**La única excepción:** en más o menos **1 de cada 20 ejecuciones del lote**, alguna contraseña sale por azar con una secuencia repetida y pierde 1 punto. Si pasa, no lo escondas: es un ejemplo real de la penalización. Decí: *"This password lost one point, because by chance it has a repeated sequence. That's the repetition rule working."* Si la que pierde el punto es la #10 (pasa muy pocas veces), la más fuerte pasa a ser la #9.

---

## Antes de grabar

1. Leé el Goal y compará este guion con el campo **Describe your idea** de Studio.
2. Practicá una vez entera en un notebook nuevo, leyendo en voz alta todas las frases 🖱️ y 🟢, y cronometrá.
3. Pegá el Goal en un documento de **Google Docs** y borrá el **Approval ID** y cualquier dato personal. Agrandá el texto hasta que se lea completo.
4. Dejá tres pestañas abiertas en Firefox, en este orden: el documento del **Goal**, Colab (https://colab.research.google.com) y la documentación del módulo `secrets` (https://docs.python.org/3/library/secrets.html). En Colab dejá a la vista el cuadro **Open notebook**, sin crear todavía el notebook. Agrandá el zoom del navegador (`Ctrl + +`).
5. Maximizá el navegador y cerrá o minimizá las demás ventanas, para que ninguna tape a otra.
6. Pausa de ~1 segundo después de cada clic y nunca más de 45 segundos en silencio.
7. No muestres Studio, Mercor, información privada ni herramientas de IA. Si Colab muestra funciones de IA (Gemini), no las uses. Cerrá este guion si está en la misma pantalla.
8. **No uses contraseñas reales tuyas** en ningún momento. Para el ejemplo de la penalización usá `aaa123`.

---

## 0:00–1:30 — El Goal y el plan

Empezás en la primera pestaña, la del **Goal**, con el texto completo y legible. La introducción dura menos de 20 segundos: la frase de apertura y el objetivo.

> 🟢 I will be beginning my task soon. Here is the workflow I have in mind.
>
> (Voy a empezar mi tarea en breve. Este es el flujo de trabajo que tengo en mente.)
>
> 🖱️ I'm on the Goal document, in the first browser tab, to show what this task asks for.
>
> (Estoy en el documento del Goal, en la primera pestaña del navegador, para mostrar qué pide esta tarea.)
>
> 🟢 As a developer building a security utility, I'll create a password generator and a strength validator in Google Colab. I'll generate ten passwords with different settings, score them, show them in a table, and find the weakest and the strongest.
>
> (Como desarrollador que arma una herramienta de seguridad, voy a crear un generador de contraseñas y un validador de fortaleza en Google Colab. Voy a generar diez contraseñas con distintas configuraciones, ponerles un puntaje, mostrarlas en una tabla y encontrar la más débil y la más fuerte.)

Ajustá esta frase a lo que diga tu Goal. Después contás el plan, paso por paso:

> 🟢 Here's the plan. First, I'll write a function that generates passwords, with options for the length and for uppercase letters, digits, and symbols.
>
> (Este es el plan. Primero, voy a escribir una función que genera contraseñas, con opciones para la longitud y para las mayúsculas, los dígitos y los símbolos.)
>
> 🟢 Second, I'll write a function that scores how strong a password is. It will look at four things: the length, the variety of characters, repeated sequences, and the entropy, which is a mathematical measure of how hard a password is to guess.
>
> (Segundo, voy a escribir una función que le pone un puntaje a la fortaleza de una contraseña. Va a mirar cuatro cosas: la longitud, la variedad de caracteres, las secuencias repetidas y la entropía, que es una medida matemática de qué tan difícil es adivinar una contraseña.)
>
> 🟢 Third, I'll generate ten passwords, from weak settings to strong ones, and show them in a table with pandas. Then I'll find the weakest and the strongest.
>
> (Tercero, voy a generar diez contraseñas, desde configuraciones débiles hasta fuertes, y mostrarlas en una tabla con pandas. Después voy a encontrar la más débil y la más fuerte.)
>
> 🟢 Finally, I'll write down my conclusions and some recommendations for creating safe passwords.
>
> (Por último, voy a anotar mis conclusiones y algunas recomendaciones para crear contraseñas seguras.)

---

## 1:30–3:00 — Colab y el módulo secrets

> 🖱️ I'm clicking the second browser tab, at the top of the window, to open Google Colab.
>
> (Hago clic en la segunda pestaña del navegador, arriba de la ventana, para abrir Google Colab.)
>
> 🟢 Google Colab is a free tool from Google that runs Python notebooks in the browser. The code runs in Google's cloud, so there's nothing to install.
>
> (Google Colab es una herramienta gratuita de Google que ejecuta notebooks de Python en el navegador. El código se ejecuta en la nube de Google, así que no hay que instalar nada.)
>
> 🖱️ I'm clicking the third browser tab, at the top of the window, to show the documentation of Python's secrets module.
>
> (Hago clic en la tercera pestaña del navegador, arriba de la ventana, para mostrar la documentación del módulo secrets de Python.)
>
> 🟢 This is the official documentation of Python's secrets module. It generates random values that are safe for passwords. The regular random module is fine for games or simulations, but its numbers can be predicted, so it should never be used alone for security. secrets comes with Python, so there's nothing to install.
>
> (Esta es la documentación oficial del módulo secrets de Python. Genera valores aleatorios seguros para contraseñas. El módulo random común sirve para juegos o simulaciones, pero sus números se pueden predecir, así que nunca hay que usarlo solo para seguridad. secrets viene con Python, así que no hay que instalar nada.)
>
> 🖱️ I'm scrolling down the secrets page with the mouse wheel, to show the choice function.
>
> (Bajo por la página de secrets con la rueda del mouse, para mostrar la función choice.)
>
> 🟢 The function I'll use is secrets.choice. It picks one random element from a sequence, like one letter from the alphabet.
>
> (La función que voy a usar es secrets.choice. Elige un elemento al azar de una secuencia, como una letra del abecedario.)
>
> 🖱️ I'm clicking the second browser tab, at the top of the window, to go back to Google Colab.
>
> (Hago clic en la segunda pestaña del navegador, arriba de la ventana, para volver a Google Colab.)

---

## 3:00–5:00 — Notebook nuevo e imports

> 🖱️ I'm clicking the New notebook button at the bottom of the Open notebook dialog, to create a fresh notebook.
>
> (Hago clic en el botón New notebook, abajo del cuadro Open notebook, para crear un notebook nuevo.)
>
> 🖱️ I'm clicking the notebook title field at the top left, and typing password_tool.ipynb, to identify this project.
>
> (Hago clic en el campo del título del notebook, arriba a la izquierda, y escribo password_tool.ipynb, para identificar este proyecto.)
>
> 🖱️ I'm clicking the plus Text button in the toolbar at the top left, to add a title and the goal.
>
> (Hago clic en el botón + Text de la barra de herramientas, arriba a la izquierda, para agregar un título y el objetivo.)

```markdown
# Password Generator & Strength Validator
Goal: generate passwords with configurable options, score their strength with several criteria, and compare the results.
```

**What each line does:**

- 🟢 `# Password Generator & Strength Validator`: the hash sign makes this the main title of the notebook.
- 🟢 `Goal: ...`: this line says what the notebook does, so anyone who opens it understands it.

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add a code cell with the imports.
>
> (Hago clic en el botón + Code de la barra de herramientas, arriba a la izquierda, para agregar una celda de código con los imports.)

Escribís la **celda 1**:

```python
import random
import string
import secrets
import re
import math
import pandas as pd
```

**What each line does:**

- 🟢 `import random`: I'll use its SystemRandom class, which shuffles with the operating system's secure randomness, not the predictable one.
- 🟢 `import string`: it has ready-made sets of characters: lowercase, uppercase, digits, and symbols.
- 🟢 `import secrets`: it picks random characters in a way that is safe for passwords.
- 🟢 `import re`: re means regular expressions. They search for patterns in text, like digits or repeated characters.
- 🟢 `import math`: for the logarithm in the entropy formula.
- 🟢 `import pandas as pd`: pandas, the library for tables, with its usual short name, pd. I'll use it to show the results.

> 🖱️ I'm clicking the Run cell button, the play icon to the left of this cell, to load the libraries.
>
> (Hago clic en el botón Run cell, el ícono de play a la izquierda de esta celda, para cargar las librerías.)
>
> 🟢 The cell ran without errors, and there's no output, because imports only load the libraries. The first run takes a few seconds, because Colab connects to a computer in Google's cloud.
>
> (La celda se ejecutó sin errores, y no hay salida, porque los imports solo cargan las librerías. La primera ejecución tarda unos segundos, porque Colab se conecta a una computadora en la nube de Google.)

---

## 5:00–9:00 — generate_password()

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for the generator.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para el generador.)

Escribís `## 1. Password generator`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell for the generator function.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código para la función generadora.)

Escribís la **celda 2**:

```python
def generate_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):
    pools = [string.ascii_lowercase]
    if use_uppercase:
        pools.append(string.ascii_uppercase)
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append(string.punctuation)
    all_chars = "".join(pools)
    chars = [secrets.choice(pool) for pool in pools]
    chars += [secrets.choice(all_chars) for _ in range(length - len(chars))]
    random.SystemRandom().shuffle(chars)
    return "".join(chars)

print(generate_password(12))
```

**What each line does:**

- 🟢 `def generate_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):`: def creates a function. It takes the length and three options. The values after the equal signs are defaults: if I don't say anything, it makes a 12-character password with every type of character.
- 🟢 `pools = [string.ascii_lowercase]`: pools is a list of character sets. Lowercase letters are always included, so a password is never empty of letters.
- 🟢 `if use_uppercase: pools.append(string.ascii_uppercase)`: if uppercase is on, it adds the 26 uppercase letters to the list.
- 🟢 `if use_digits: pools.append(string.digits)`: the same for the 10 digits.
- 🟢 `if use_symbols: pools.append(string.punctuation)`: and the same for the 32 symbols, which come from string.punctuation.
- 🟢 `all_chars = "".join(pools)`: this joins all the chosen sets into one long string of allowed characters.
- 🟢 `chars = [secrets.choice(pool) for pool in pools]`: first, it picks one character from each chosen set. This guarantees that the password really contains every type I asked for.
- 🟢 `chars += [secrets.choice(all_chars) for _ in range(length - len(chars))]`: then it fills the rest of the length with random characters from all the allowed ones. The underscore means I don't need the loop counter.
- 🟢 `random.SystemRandom().shuffle(chars)`: it shuffles the characters with secure randomness, so the guaranteed characters aren't always at the start.
- 🟢 `return "".join(chars)`: it joins the list into one string and returns it.
- 🟢 `print(generate_password(12))`: a quick test with 12 characters.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to generate a test password.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para generar una contraseña de prueba.)
>
> 🟢 Here's a random 12-character password. I can see lowercase and uppercase letters, digits, and symbols, as I asked.
>
> (Acá hay una contraseña aleatoria de 12 caracteres. Veo minúsculas, mayúsculas, dígitos y símbolos, como pedí.)

Mirá la contraseña antes de decirlo: siempre tiene los cuatro tipos, pero nombralos señalándolos.

> 🖱️ I'm clicking the Run cell button again, to show that each password is different.
>
> (Hago clic en el botón Run cell otra vez, para mostrar que cada contraseña es distinta.)
>
> 🟢 A new password appeared, completely different from the first one. That's what we want: nobody can predict the next one.
>
> (Apareció una contraseña nueva, completamente distinta de la primera. Eso es lo que queremos: nadie puede predecir la siguiente.)

---

## 9:00–13:30 — check_strength()

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for the strength checker.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para el validador de fortaleza.)

Escribís `## 2. Strength checker`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell for the strength function.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código para la función de fortaleza.)

Escribís la **celda 3**:

```python
def check_strength(password):
    classes = [r"[a-z]", r"[A-Z]", r"[0-9]", r"[^A-Za-z0-9]"]
    sizes = [26, 26, 10, 32]
    present = [bool(re.search(c, password)) for c in classes]
    pool = sum(size for size, found in zip(sizes, present) if found)
    entropy = len(password) * math.log2(pool)
    score = (len(password) >= 8) + (len(password) >= 12) + (len(password) >= 16)
    score += sum(present)
    score += (entropy >= 60) + (entropy >= 80)
    if re.search(r"(.)\1\1|(.{2,})\2", password):
        score -= 1
    label = "Strong" if score >= 8 else "Medium" if score >= 5 else "Weak"
    return {"strength_score": score, "strength_label": label, "entropy": round(entropy, 1)}

print(check_strength("aaa123"))
print(check_strength(generate_password(16)))
```

**What each line does:**

- 🟢 `def check_strength(password):`: the function receives one password and returns its score.
- 🟢 `classes = [r"[a-z]", r"[A-Z]", r"[0-9]", r"[^A-Za-z0-9]"]`: four regular expressions, one per character type: lowercase, uppercase, digits, and anything that isn't a letter or a digit, which means symbols. The r before each string tells Python to read the backslashes and brackets as they are.
- 🟢 `sizes = [26, 26, 10, 32]`: how many characters each type has, in the same order.
- 🟢 `present = [bool(re.search(c, password)) for c in classes]`: re.search checks if each type appears in the password. The result is a list of four True or False values.
- 🟢 `pool = sum(size for size, found in zip(sizes, present) if found)`: zip pairs each size with its True or False. The pool is the number of possible characters, adding only the types that are present.
- 🟢 `entropy = len(password) * math.log2(pool)`: entropy measures how hard a password is to guess, in bits. It's the length times the base-2 logarithm of the pool. Each extra bit doubles the number of guesses an attacker needs.
- 🟢 `score = (len(password) >= 8) + (len(password) >= 12) + (len(password) >= 16)`: one point for each length level. In Python, True counts as 1 and False as 0, so I can add the comparisons.
- 🟢 `score += sum(present)`: one point for each type of character, so variety adds up to four points.
- 🟢 `score += (entropy >= 60) + (entropy >= 80)`: up to two more points for high entropy.
- 🟢 `if re.search(r"(.)\1\1|(.{2,})\2", password): score -= 1`: this regular expression finds repeated sequences. The first part finds the same character three times in a row, like "aaa". The second part finds a chunk of two or more characters repeated right after itself, like "abab". Repetition makes a password easier to guess, so it loses a point.
- 🟢 `label = "Strong" if score >= 8 else "Medium" if score >= 5 else "Weak"`: 8 or more is Strong, 5 to 7 is Medium, and 4 or less is Weak.
- 🟢 `return {...}`: it returns the score, the label, and the entropy, rounded to one decimal, as a dictionary.
- 🟢 `print(check_strength("aaa123"))`: a test with a weak example password that has a repetition. It's not a real password.
- 🟢 `print(check_strength(generate_password(16)))`: a test with a random 16-character password from my generator.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to test the strength checker.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para probar el validador.)

Señalás cada número mientras lo explicás:

> 🟢 "aaa123" scores 1, Weak, with 31 bits of entropy. Let me check it by hand. It has 6 characters, so no length points. It has lowercase letters and digits, so two variety points. The entropy is too low for extra points. And "aaa" is a repetition, so it loses one point. Two minus one is one, so the function works as I expected.
>
> ("aaa123" saca 1, Weak, con 31 bits de entropía. Lo compruebo a mano. Tiene 6 caracteres, así que no suma puntos por longitud. Tiene minúsculas y dígitos, así que suma dos puntos de variedad. La entropía es muy baja para sumar puntos. Y "aaa" es una repetición, así que pierde un punto. Dos menos uno es uno, así que la función funciona como esperaba.)
>
> 🟢 The random 16-character password scores 9, Strong, the maximum, with about 105 bits of entropy.
>
> (La contraseña aleatoria de 16 caracteres saca 9, Strong, el máximo, con unos 105 bits de entropía.)

Si la de 16 caracteres saca 8 (pasa muy pocas veces), decí que perdió un punto por una repetición al azar y volvé a ejecutar la celda.

---

## 13:30–18:00 — 10 contraseñas, la tabla y la más débil y la más fuerte

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for the batch.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para el lote.)

Escribís `## 3. Batch of 10 passwords`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that generates ten passwords with different settings.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que genera diez contraseñas con distintas configuraciones.)

Escribís la **celda 4**:

```python
configs = [
    (6, False, False, False), (8, False, False, False), (8, True, False, False),
    (8, True, True, False), (10, True, True, True), (12, True, True, False),
    (12, True, True, True), (16, True, True, False), (16, True, True, True),
    (20, True, True, True),
]
results = []
for length, upper, digits, symbols in configs:
    password = generate_password(length, upper, digits, symbols)
    config = f"upper={upper}, digits={digits}, symbols={symbols}"
    results.append({"password": password, "length": length, "configuration": config, **check_strength(password)})
len(results)
```

**What each line does:**

- 🟢 `configs = [...]`: ten configurations, ordered from weak to strong. Each one is a tuple with the length and whether to use uppercase, digits, and symbols. The first is 6 lowercase letters, and the last is 20 characters with everything.
- 🟢 `results = []`: an empty list to store the results.
- 🟢 `for length, upper, digits, symbols in configs:`: the loop takes one configuration at a time and unpacks its four values into these names.
- 🟢 `password = generate_password(length, upper, digits, symbols)`: it generates a password with those settings.
- 🟢 `config = f"upper={upper}, digits={digits}, symbols={symbols}"`: an f-string, which puts the values inside the text. It's a readable description of the settings.
- 🟢 `results.append({...})`: it adds a dictionary to the list, with the password, the length, the configuration, and the score from check_strength. The two asterisks unpack that dictionary into this one, so its three keys become columns too.
- 🟢 `len(results)`: this shows how many results are in the list.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to generate the batch.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para generar el lote.)
>
> 🟢 It shows 10, so the list has the ten results I expected. Now I'll show them in a table.
>
> (Muestra 10, así que la lista tiene los diez resultados que esperaba. Ahora los muestro en una tabla.)

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a heading for the results table.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título para la tabla de resultados.)

Escribís `## 4. Results table`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that shows the results as a formatted table.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que muestra los resultados como una tabla con formato.)

Escribís la **celda 5**:

```python
df = pd.DataFrame(results)
df.style.background_gradient(subset=["strength_score"], cmap="RdYlGn")
```

**What each line does:**

- 🟢 `df = pd.DataFrame(results)`: pandas turns the list of dictionaries into a table, called a DataFrame. Each dictionary is a row, and each key is a column.
- 🟢 `df.style.background_gradient(subset=["strength_score"], cmap="RdYlGn")`: this colors only the score column. RdYlGn means red, yellow, green: red for weak, yellow in the middle, and green for strong, so the result is easy to read at a glance.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to show the table.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para mostrar la tabla.)

Señalás las columnas de izquierda a derecha y después bajás por las filas:

> 🟢 The table has the password, the length, the configuration, the strength score, the label, and the entropy.
>
> (La tabla tiene la contraseña, la longitud, la configuración, el puntaje, la etiqueta y la entropía.)
>
> 🖱️ I'm moving the mouse down the strength_score column, in the table under the cell, to compare the rows.
>
> (Muevo el mouse por la columna strength_score, en la tabla debajo de la celda, para comparar las filas.)
>
> 🟢 The first four are red and Weak, from 1 to 4 points. The middle three are Medium, with 6, 6, and 7. And the last three are green and Strong, with 8, 9, and 9. The entropy also grows with the length and the variety, from about 28 bits to about 131.
>
> (Las primeras cuatro están en rojo y son Weak, de 1 a 4 puntos. Las tres del medio son Medium, con 6, 6 y 7. Y las últimas tres están en verde y son Strong, con 8, 9 y 9. La entropía también crece con la longitud y la variedad, de unos 28 bits a unos 131.)

Compará con la tabla de referencia antes de decirlo. Si alguna fila tiene un punto menos, usá la frase de la penalización de la sección **Cómo se calcula el puntaje**.

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a heading for the weakest and the strongest password.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título para la contraseña más débil y la más fuerte.)

Escribís `## 5. Weakest and strongest`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that finds the weakest and the strongest password.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que encuentra la contraseña más débil y la más fuerte.)

Escribís la **celda 6**:

```python
def find_weakest(results):
    return min(results, key=lambda r: (r["strength_score"], r["entropy"]))

def find_strongest(results):
    return max(results, key=lambda r: (r["strength_score"], r["entropy"]))

weakest = find_weakest(results)
strongest = find_strongest(results)
print("Weakest:", weakest["password"], "|", weakest["strength_score"], weakest["strength_label"], "|", weakest["configuration"])
print("Strongest:", strongest["password"], "|", strongest["strength_score"], strongest["strength_label"], "|", strongest["configuration"])
```

**What each line does:**

- 🟢 `def find_weakest(results): return min(results, key=lambda r: (r["strength_score"], r["entropy"]))`: min finds the result with the lowest value. The key says what to compare. lambda is a small function without a name: for each result, it returns the score and the entropy. Python compares the score first, and if two scores are equal, the entropy breaks the tie.
- 🟢 `def find_strongest(results): return max(...)`: the same idea with max, for the highest score.
- 🟢 `weakest = find_weakest(results)` and `strongest = find_strongest(results)`: I call both functions and save the results.
- 🟢 `print("Weakest:", ...)` and `print("Strongest:", ...)`: this shows each password with its score, label, and configuration.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to find the weakest and the strongest.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para encontrar la más débil y la más fuerte.)
>
> 🟢 The weakest is the 6-character lowercase password, with a score of 1. The strongest is the 20-character password with every type of character, with a score of 9.
>
> (La más débil es la de 6 caracteres en minúsculas, con puntaje 1. La más fuerte es la de 20 caracteres con todos los tipos, con puntaje 9.)
>
> 🟢 Two passwords scored 9, but the 20-character one has more entropy, about 131 bits against about 105, so it wins the tie. That's why I added the entropy to the key.
>
> (Dos contraseñas sacaron 9, pero la de 20 caracteres tiene más entropía, unos 131 bits contra unos 105, así que gana el desempate. Por eso agregué la entropía a la clave.)

---

## 18:00–20:00 — Conclusiones

> 🖱️ I'm clicking the plus Text button in the toolbar, to add the conclusions and recommendations.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar las conclusiones y recomendaciones.)

Mientras escribís, decí en voz alta lo que vas escribiendo:

```markdown
## 6. Conclusions and recommendations
- **Weakest:** 6 lowercase letters (score 1, Weak, about 28 bits of entropy). Short passwords with one character type can be guessed quickly.
- **Strongest:** 20 characters with uppercase, digits, and symbols (score 9, Strong, about 131 bits of entropy).
- **Length matters most:** 16 characters with letters and digits (score 8) is stronger than 12 characters with symbols (score 7).
- **Recommendations:** use at least 16 characters, mix uppercase, lowercase, digits, and symbols, avoid repeated characters or patterns, and use the `secrets` module (not `random`) to generate passwords.
```

> 🟢 The most interesting result is that length matters more than symbols. A 16-character password with letters and digits is stronger than a 12-character password with symbols, because each extra character multiplies the number of possible passwords.
>
> (El resultado más interesante es que la longitud importa más que los símbolos. Una contraseña de 16 caracteres con letras y dígitos es más fuerte que una de 12 con símbolos, porque cada carácter extra multiplica la cantidad de contraseñas posibles.)

---

## 20:00–25:00 — Epílogo (4–5 minutos)

Revisá en las reglas de Odin qué tiene que tener el epílogo y ajustá este texto si piden algo distinto.

> 🖱️ I'm opening the File menu at the top left of Colab and choosing Download, then Download .ipynb, to save the finished notebook for the deliverables.
>
> (Abro el menú File, arriba a la izquierda de Colab, y elijo Download y después Download .ipynb, para guardar el notebook terminado para los entregables.)

### Resumen paso a paso

Subís hasta el principio del notebook y vas bajando: cada frase va cuando la sección correspondiente está en pantalla. Señalá con el mouse lo que nombrás.

> 🖱️ I'm scrolling up to the top of the notebook with the mouse wheel, to go over everything we did, step by step.
>
> (Subo hasta el principio del notebook con la rueda del mouse, para repasar todo lo que hicimos, paso a paso.)
>
> 🟢 Let me summarize the whole project. We started with the title and the goal, and then imported six libraries: secrets and random for secure randomness, string for the character sets, re for patterns, math for the entropy, and pandas for the table.
>
> (Les resumo todo el proyecto. Empezamos con el título y el objetivo, y después importamos seis librerías: secrets y random para la aleatoriedad segura, string para los conjuntos de caracteres, re para los patrones, math para la entropía y pandas para la tabla.)
>
> 🖱️ I'm scrolling down to section 1, Password generator.
>
> (Bajo hasta la sección 1, Password generator.)
>
> 🟢 In section 1, we built the generator. It takes a length and three options, guarantees one character of each chosen type, fills the rest at random with secrets, and shuffles everything.
>
> (En la sección 1 armamos el generador. Recibe una longitud y tres opciones, garantiza un carácter de cada tipo elegido, completa el resto al azar con secrets y mezcla todo.)
>
> 🖱️ I'm scrolling down to section 2, Strength checker.
>
> (Bajo hasta la sección 2, Strength checker.)
>
> 🟢 In section 2, we built the checker. It gives up to three points for length, four for variety, and two for entropy, and takes one point away for repeated sequences. We checked it by hand with "aaa123", which scored 1.
>
> (En la sección 2 armamos el validador. Da hasta tres puntos por longitud, cuatro por variedad y dos por entropía, y resta un punto por secuencias repetidas. Lo comprobamos a mano con "aaa123", que sacó 1.)
>
> 🖱️ I'm scrolling down to sections 3 and 4, the batch and the results table.
>
> (Bajo hasta las secciones 3 y 4, el lote y la tabla de resultados.)
>
> 🟢 In sections 3 and 4, we generated ten passwords from weak to strong settings and showed them in a colored table: four Weak, three Medium, and three Strong.
>
> (En las secciones 3 y 4 generamos diez contraseñas, de configuraciones débiles a fuertes, y las mostramos en una tabla con colores: cuatro Weak, tres Medium y tres Strong.)
>
> 🖱️ I'm scrolling down to sections 5 and 6, Weakest and strongest, and the conclusions.
>
> (Bajo hasta las secciones 5 y 6, Weakest and strongest, y las conclusiones.)
>
> 🟢 In section 5, we found the weakest, 6 lowercase letters, and the strongest, 20 characters with everything, using the entropy to break the tie. And in section 6, we wrote the conclusions and the recommendations.
>
> (En la sección 5 encontramos la más débil, 6 letras minúsculas, y la más fuerte, 20 caracteres con todo, usando la entropía para desempatar. Y en la sección 6 escribimos las conclusiones y las recomendaciones.)

### Decisiones y próximos pasos

> 🖱️ I'm scrolling slowly up through the notebook with the mouse wheel, to go over the decisions I made.
>
> (Subo despacio por el notebook con la rueda del mouse, para repasar las decisiones que tomé.)
>
> 🟢 In this epilogue, I want to go over my approach. For the generator, I used the secrets module instead of plain random, because password randomness must be unpredictable. I also guaranteed at least one character of each chosen type, so the settings always mean what they say.
>
> (En este epílogo quiero repasar mi enfoque. Para el generador usé el módulo secrets en vez de random común, porque la aleatoriedad de una contraseña tiene que ser impredecible. También garanticé al menos un carácter de cada tipo elegido, así la configuración siempre cumple lo que dice.)
>
> 🟢 That guarantee also makes the results stable. The passwords change every time I run the notebook, but the scores stay the same, because they depend on the settings, not on luck.
>
> (Esa garantía también hace que los resultados sean estables. Las contraseñas cambian cada vez que ejecuto el notebook, pero los puntajes se mantienen, porque dependen de la configuración, no de la suerte.)
>
> 🟢 For the checker, I combined several criteria instead of just one. Length and variety are easy to understand, entropy gives a mathematical measure, and the repetition check catches patterns that the other rules miss.
>
> (Para el validador combiné varios criterios en vez de uno solo. La longitud y la variedad son fáciles de entender, la entropía da una medida matemática, y el chequeo de repeticiones detecta patrones que las otras reglas no ven.)
>
> 🟢 This scoring has limits. It doesn't know about dictionary words or common passwords: a long password like "Password1234567!" would score high, but it's easy to guess. Real tools also check lists of leaked passwords.
>
> (Este puntaje tiene límites. No conoce palabras del diccionario ni contraseñas comunes: una contraseña larga como "Password1234567!" sacaría un puntaje alto, pero es fácil de adivinar. Las herramientas reales también revisan listas de contraseñas filtradas.)
>
> 🟢 As next steps, I would add a check for common words, write unit tests for both functions, and turn this into a small app with a slider for the length. My recommendation is clear: use 16 or more random characters with every type, and let a password manager remember them. Thanks for watching!
>
> (Como próximos pasos, agregaría un chequeo de palabras comunes, escribiría pruebas unitarias para las dos funciones y lo convertiría en una pequeña app con un control deslizante para la longitud. Mi recomendación es clara: usar 16 caracteres aleatorios o más, con todos los tipos, y dejar que un gestor de contraseñas los recuerde. ¡Gracias por mirar!)

Si el reloj todavía no pasó los 15:00, no cortes: volvé a ejecutar la celda del lote y la de la tabla, y comentá cómo cambian las contraseñas pero no los puntajes.

---

## Después de grabar

1. Ejecutá **Run full AutoQC**, no solo *Rerun failing*.
2. Subí los **cuatro archivos por separado**: el **MP4**, el **ZIP original de TaskRecorder**, **Deliverables.zip** (con el `.ipynb` descargado) y **Metadata.rtf**.
