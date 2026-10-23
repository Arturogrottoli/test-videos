# e30p7c36 — Password Generator & Strength Validator

Guion paso a paso para grabar la tarea **e30p7c36** en **Google Colab**: un generador de contraseñas con opciones configurables y un validador de fortaleza. El validador evalúa la longitud, la variedad de caracteres, las secuencias repetidas y la entropía. Después generás 10 contraseñas, las mostrás en una tabla de pandas, encontrás la más débil y la más fuerte, y escribís conclusiones. La grabación tiene que durar **entre 15:00 y 50:59**. Este guion apunta a unos **22 minutos**, epílogo incluido.

**Cómo leer este guion:**

- Las frases que empiezan con 🖱️ las decís **en el momento de hacer clic, desplazarte o escribir**. Siempre dicen **qué** elemento usás, **dónde** está en la pantalla y **por qué** lo usás. Son las que revisa AutoQC.
- Las frases que empiezan con 🟢 son la explicación que **decís en inglés** entre una acción y otra.
- Debajo de cada bloque de código, la lista **What each line does** explica cada línea en inglés. La leés en voz alta mientras escribís esa línea.
- El resto, en castellano, es lo que hacés en pantalla. Las traducciones aparecen entre paréntesis después de cada frase.

> **Importante:** el Goal de Studio tiene prioridad sobre este guion. La tarea arranca desde cero, sin archivos externos.

---

## Archivos de la carpeta

```
e30p7c36-password-generator/
├── GUION-V2.md             ← este guion (versión nueva)
├── README.md             ← guion anterior (sesión previa)
└── password_tool.ipynb   ← notebook de referencia, completo y en orden
```

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

**Entropía** = longitud × log₂(tamaño del conjunto de caracteres). El conjunto tiene 26 minúsculas, +26 mayúsculas, +10 dígitos y +32 símbolos.

**Valores de referencia.** Las contraseñas cambian en cada ejecución, porque son aleatorias, pero los puntajes no, porque `generate_password` garantiza al menos un carácter de cada tipo elegido. La única excepción: si por azar sale una secuencia repetida, esa contraseña pierde 1 punto. Es raro; si pasa, explicalo como un ejemplo de la penalización.

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

---

## Antes de grabar

1. Leé el Goal y compará este guion con el campo **Describe your idea** de Studio.
2. Practicá una vez entera en un notebook nuevo, leyendo en voz alta las frases 🖱️ y 🟢, y cronometrá.
3. Dejá tres pestañas abiertas en Firefox, en este orden: el documento **Goal**, la documentación del módulo `secrets` (https://docs.python.org/3/library/secrets.html) y Colab (https://colab.research.google.com). Agrandá el zoom (`Ctrl + +`).
4. Maximizá el navegador y cerrá o minimizá las demás ventanas, para que ninguna tape a otra.
5. Pausa de ~1 segundo después de cada clic y nunca más de 45 segundos en silencio.
6. No muestres Studio, Mercor, información privada ni herramientas de IA. Cerrá este guion si está en la misma pantalla.
7. **No uses contraseñas reales tuyas** en ningún momento. Para el ejemplo de la penalización usá `aaa123`.

---

## 0:00–0:45 — Mostrar el Goal

> 🖱️ I'm on the Goal document in the first browser tab, to show what this task asks for.
>
> (Estoy en el documento del Goal, en la primera pestaña del navegador, para mostrar qué pide esta tarea.)
>
> 🟢 As a developer building a security utility, I'll create a password generator and a strength validator in Google Colab. I'll generate ten passwords with different settings, score them, show them in a table, and find the weakest and the strongest.
>
> (Como desarrollador que arma una herramienta de seguridad, voy a crear un generador de contraseñas y un validador de fortaleza en Google Colab. Voy a generar diez contraseñas con distintas configuraciones, ponerles un puntaje, mostrarlas en una tabla y encontrar la más débil y la más fuerte.)

---

## 0:45–4:00 — El módulo secrets, Colab e imports

> 🖱️ I'm clicking the second browser tab, at the top of the window, to show the documentation of Python's secrets module.
>
> (Hago clic en la segunda pestaña del navegador, arriba de la ventana, para mostrar la documentación del módulo secrets de Python.)
>
> 🟢 This is the official documentation of Python's secrets module. It generates random values that are safe for passwords. The regular random module is fine for games, but its numbers can be predicted, so it should never be used alone for security.
>
> (Esta es la documentación oficial del módulo secrets de Python. Genera valores aleatorios seguros para contraseñas. El módulo random común sirve para juegos, pero sus números se pueden predecir, así que nunca hay que usarlo solo para seguridad.)
>
> 🖱️ I'm clicking the third browser tab, at the top of the window, to open Google Colab.
>
> (Hago clic en la tercera pestaña del navegador, arriba de la ventana, para abrir Google Colab.)
>
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

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell with the imports.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código con los imports.)

```python
import random
import string
import secrets
import re
import math
import pandas as pd
```

**What each line does:**

- 🟢 `import random`: I'll use its SystemRandom class to shuffle characters with the operating system's secure randomness.
- 🟢 `import string`: it has ready-made sets of characters: lowercase, uppercase, digits, and symbols.
- 🟢 `import secrets`: it picks random characters in a way that is safe for passwords.
- 🟢 `import re`: regular expressions, to search for patterns, like digits or repeated characters.
- 🟢 `import math`: for the logarithm in the entropy formula.
- 🟢 `import pandas as pd`: to show the results as a table.

> 🖱️ I'm clicking the Run cell button, the play icon to the left of this cell, to load the libraries.
>
> (Hago clic en el botón Run cell, el ícono de play a la izquierda de esta celda, para cargar las librerías.)

---

## 4:00–8:00 — generate_password()

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for the generator.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para el generador.)

Escribís `## 1. Password generator`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell for the generator function.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código para la función generadora.)

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

- 🟢 `def generate_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):`: the function takes the length and three options. By default it makes a 12-character password with every type of character.
- 🟢 `pools = [string.ascii_lowercase]`: pools is a list of character sets. Lowercase letters are always included.
- 🟢 `if use_uppercase: pools.append(string.ascii_uppercase)`: if uppercase is on, it adds the uppercase letters. The next two ifs do the same for digits and for symbols, which come from string.punctuation.
- 🟢 `all_chars = "".join(pools)`: this joins all the chosen sets into one long string of allowed characters.
- 🟢 `chars = [secrets.choice(pool) for pool in pools]`: first, it picks one character from each chosen set. This guarantees that the password really contains every type I asked for.
- 🟢 `chars += [secrets.choice(all_chars) for _ in range(length - len(chars))]`: then it fills the rest of the length with random characters from all the allowed ones.
- 🟢 `random.SystemRandom().shuffle(chars)`: it shuffles the characters with secure randomness, so the guaranteed characters aren't always at the start.
- 🟢 `return "".join(chars)`: it joins the list into one string and returns it.
- 🟢 `print(generate_password(12))`: a quick test with 12 characters.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to generate a test password.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para generar una contraseña de prueba.)
>
> 🟢 Here's a random 12-character password with lowercase, uppercase, digits, and symbols. If I run it again, I get a different one.
>
> (Acá hay una contraseña aleatoria de 12 caracteres con minúsculas, mayúsculas, dígitos y símbolos. Si la ejecuto de nuevo, sale otra distinta.)
>
> 🖱️ I'm clicking the Run cell button again, to show that each password is different.
>
> (Hago clic en el botón Run cell otra vez, para mostrar que cada contraseña es distinta.)

---

## 8:00–12:30 — check_strength()

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for the strength checker.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para el validador de fortaleza.)

Escribís `## 2. Strength checker`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell for the strength function.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código para la función de fortaleza.)

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

- 🟢 `classes = [r"[a-z]", r"[A-Z]", r"[0-9]", r"[^A-Za-z0-9]"]`: four regular expressions, one per character type: lowercase, uppercase, digits, and anything else, which means symbols.
- 🟢 `sizes = [26, 26, 10, 32]`: how many characters each type has.
- 🟢 `present = [bool(re.search(c, password)) for c in classes]`: re.search checks if each type appears in the password. The result is a list of True or False.
- 🟢 `pool = sum(size for size, found in zip(sizes, present) if found)`: the pool is the number of possible characters, adding only the types that are present.
- 🟢 `entropy = len(password) * math.log2(pool)`: entropy measures how hard a password is to guess, in bits. Each extra bit doubles the number of guesses an attacker needs.
- 🟢 `score = (len(password) >= 8) + (len(password) >= 12) + (len(password) >= 16)`: one point for each length level. In Python, True counts as 1, so I can add the comparisons.
- 🟢 `score += sum(present)`: one point for each type of character, so variety adds up to four points.
- 🟢 `score += (entropy >= 60) + (entropy >= 80)`: up to two more points for high entropy.
- 🟢 `if re.search(r"(.)\1\1|(.{2,})\2", password): score -= 1`: this regular expression finds repeated sequences: the same character three times in a row, like "aaa", or a chunk repeated twice, like "abab". Repetition makes a password easier to guess, so it loses a point.
- 🟢 `label = "Strong" if score >= 8 else "Medium" if score >= 5 else "Weak"`: 8 or more is Strong, 5 to 7 is Medium, and 4 or less is Weak.
- 🟢 `return {...}`: it returns the score, the label, and the entropy as a dictionary.
- 🟢 `print(check_strength("aaa123"))`: a test with a weak password that has a repetition.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to test the strength checker.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para probar el validador.)
>
> 🟢 "aaa123" scores 1, Weak. It's short, it only has letters and digits, and "aaa" is a repetition, so it lost a point. The random 16-character password scores 9, Strong, with about 105 bits of entropy.
>
> (“aaa123” saca 1, Weak. Es corta, solo tiene letras y dígitos, y "aaa" es una repetición, así que perdió un punto. La contraseña aleatoria de 16 caracteres saca 9, Strong, con unos 105 bits de entropía.)

---

## 12:30–16:00 — 10 contraseñas, la tabla y la más débil y la más fuerte

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for the batch.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para el lote.)

Escribís `## 3. Batch of 10 passwords`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that generates ten passwords with different settings.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que genera diez contraseñas con distintas configuraciones.)

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

- 🟢 `configs = [...]`: ten configurations, from weak to strong. Each one has the length and whether to use uppercase, digits, and symbols.
- 🟢 `results = []`: an empty list to store the results.
- 🟢 `for length, upper, digits, symbols in configs:`: the loop takes one configuration at a time.
- 🟢 `password = generate_password(length, upper, digits, symbols)`: it generates a password with those settings.
- 🟢 `config = f"upper={upper}, digits={digits}, symbols={symbols}"`: an f-string, a readable description of the settings.
- 🟢 `results.append({...})`: it adds a dictionary to the list, with the password, the length, the configuration, and the score from check_strength. The two asterisks unpack that dictionary into this one.
- 🟢 `len(results)`: this shows that the list has ten results.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to generate the batch.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para generar el lote.)

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a heading for the results table.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título para la tabla de resultados.)

Escribís `## 4. Results table`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that shows the results as a formatted table.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que muestra los resultados como una tabla con formato.)

```python
df = pd.DataFrame(results)
df.style.background_gradient(subset=["strength_score"], cmap="RdYlGn")
```

**What each line does:**

- 🟢 `df = pd.DataFrame(results)`: pandas turns the list of dictionaries into a table. Each dictionary is a row, and each key is a column.
- 🟢 `df.style.background_gradient(subset=["strength_score"], cmap="RdYlGn")`: this colors the score column from red, for weak, through yellow, to green, for strong, so the result is easy to read at a glance.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to show the table.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para mostrar la tabla.)
>
> 🟢 The table has the password, the length, the configuration, the strength score, the label, and the entropy. The first four are red and Weak, the middle three are Medium, and the last three are green and Strong.
>
> (La tabla tiene la contraseña, la longitud, la configuración, el puntaje, la etiqueta y la entropía. Las primeras cuatro están en rojo y son Weak, las tres del medio son Medium, y las últimas tres están en verde y son Strong.)

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell that finds the weakest and the strongest password.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código que encuentra la contraseña más débil y la más fuerte.)

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

- 🟢 `def find_weakest(results): return min(results, key=lambda r: (r["strength_score"], r["entropy"]))`: min finds the result with the lowest value. The key says what to compare: first the score, and if two scores are equal, the entropy breaks the tie.
- 🟢 `def find_strongest(results): return max(...)`: the same idea with max, for the highest score.
- 🟢 `weakest = ...` and `strongest = ...`: I call both functions and save the results.
- 🟢 `print("Weakest:", ...)` and `print("Strongest:", ...)`: this shows each password with its score, label, and configuration.

> 🖱️ I'm clicking the Run cell button to the left of this cell, to find the weakest and the strongest.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para encontrar la más débil y la más fuerte.)
>
> 🟢 The weakest is the 6-character lowercase password, with a score of 1. The strongest is the 20-character password with every type of character, with a score of 9. Two passwords scored 9, but the 20-character one has more entropy, about 131 bits, so it wins the tie.
>
> (La más débil es la de 6 caracteres en minúsculas, con puntaje 1. La más fuerte es la de 20 caracteres con todos los tipos, con puntaje 9. Dos contraseñas sacaron 9, pero la de 20 caracteres tiene más entropía, unos 131 bits, así que gana el desempate.)

---

## 16:00–18:30 — Conclusiones

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

## 18:30–22:00 — Epílogo (3–4 minutos)

Revisá en las reglas de Odin qué tiene que tener el epílogo y ajustá este texto si piden algo distinto.

> 🖱️ I'm opening the File menu at the top left of Colab and choosing Download, then Download .ipynb, to save the finished notebook for the deliverables.
>
> (Abro el menú File, arriba a la izquierda de Colab, y elijo Download y después Download .ipynb, para guardar el notebook terminado para los entregables.)
>
> 🖱️ I'm scrolling slowly up through the notebook with the mouse wheel, to go over the decisions I made.
>
> (Subo despacio por el notebook con la rueda del mouse, para repasar las decisiones que tomé.)
>
> 🟢 In this epilogue, I want to go over my approach. For the generator, I used the secrets module instead of plain random, because password randomness must be unpredictable. I also guaranteed at least one character of each chosen type, so the settings always mean what they say.
>
> (En este epílogo quiero repasar mi enfoque. Para el generador usé el módulo secrets en vez de random común, porque la aleatoriedad de una contraseña tiene que ser impredecible. También garanticé al menos un carácter de cada tipo elegido, así la configuración siempre cumple lo que dice.)
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

Si el reloj todavía no pasó los 15:00, no cortes: volvé a ejecutar la celda del lote y comentá cómo cambian las contraseñas pero no los puntajes.

---

## Después de grabar

1. Ejecutá **Run full AutoQC**, no solo *Rerun failing*.
2. Subí los **cuatro archivos por separado**: el **MP4**, el **ZIP original de TaskRecorder**, **Deliverables.zip** (con el `.ipynb` descargado) y **Metadata.rtf**.
