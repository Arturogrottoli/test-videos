# e30p7c36 — Password Generator & Strength Validator

Guion paso a paso para grabar la tarea **e30p7c36**: programar en **Google Colab**, con **Python**, un generador de contraseñas con opciones configurables y un validador de fortaleza. El validador evalúa la longitud, la variedad de caracteres, las secuencias repetidas y la entropía. Después generás 10 contraseñas, las mostrás en una tabla de **pandas**, encontrás la más débil y la más fuerte, y escribís conclusiones. La grabación tiene que durar **entre 15:00 y 50:59**. Este guion apunta a unos **28–30 minutos**, epílogo incluido.

**Cómo leer este guion:**

- Las frases que empiezan con 🖱️ las decís **en el momento de hacer clic, desplazarte o escribir**. Siempre dicen **qué** elemento usás, **dónde** está en la pantalla y **por qué** lo usás. Son las que revisa AutoQC.
- Las frases que empiezan con 🟢 son la explicación que **decís en inglés** entre una acción y otra.
- Debajo de cada bloque de código, la lista **What each line does** explica **cada renglón por separado**, en inglés. Leés la explicación de un renglón **mientras lo escribís**, y recién después pasás al siguiente. Así nunca estás escribiendo en silencio.
- El resto, en castellano, es lo que hacés en pantalla. Las traducciones aparecen entre paréntesis después de cada frase.

> **Importante:** el Goal de Studio tiene prioridad sobre este guion. Si el Goal define otros nombres de funciones, otros criterios o otras etiquetas, seguí los del Goal. La tarea arranca desde cero, sin archivos externos.

---

## Archivos de la carpeta

```
e30p7c36-password-generator/
├── README.md             ← este guion
└── password_tool.ipynb   ← notebook de referencia, completo y en orden
```

Para probar el notebook de referencia: en https://colab.research.google.com elegís **File → Upload notebook**, hacés clic en **Browse** (no lo arrastres desde VS Code), seleccionás `password_tool.ipynb` y ejecutás **Runtime → Run all**. No hace falta subir ningún archivo.

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

**La única excepción:** en más o menos **1 de cada 20 ejecuciones del lote**, alguna contraseña sale por azar con una secuencia repetida y pierde 1 punto. Si pasa, no lo escondas: es un ejemplo real de la penalización. Decí: *"This password lost one point, because by chance it has a repeated sequence. That's the repetition rule working. I'll run the batch again, so the table matches the typical result."* (Esta contraseña perdió un punto porque, por azar, tiene una secuencia repetida. Es la regla de repetición funcionando. Vuelvo a ejecutar el lote, para que la tabla coincida con el resultado típico.) Después volvés a ejecutar la **celda 4** (el lote) y la **celda 5** (la tabla) hasta que los puntajes coincidan con la tabla de referencia. Así las frases fijas de la tabla, de las conclusiones y del epílogo siguen siendo ciertas.

---

## Antes de grabar

1. Leé el Goal y compará este guion con el campo **Describe your idea** de Studio.
2. Practicá una vez entera en un notebook nuevo, leyendo en voz alta todas las frases 🖱️ y 🟢, y cronometrá.
3. Pegá el Goal en un documento de **Google Docs** y borrá el **Approval ID** y cualquier dato personal. Agrandá el texto hasta que se lea completo.
4. Dejá **cuatro pestañas** abiertas en Firefox, en este orden:
   1. el documento del **Goal**;
   2. Colab (https://colab.research.google.com), con el cuadro **Open notebook** a la vista, sin crear todavía el notebook;
   3. la documentación del módulo `secrets` (https://docs.python.org/3/library/secrets.html);
   4. el sitio oficial de pandas (https://pandas.pydata.org).

   Agrandá el zoom del navegador (`Ctrl + +`).
5. Maximizá el navegador y cerrá o minimizá las demás ventanas, para que ninguna tape a otra.
6. Pausa de ~1 segundo después de cada clic y nunca más de 45 segundos en silencio.
7. Escribí el código **un renglón por vez**, a tu ritmo normal (no más lento a propósito: el tiempo tipeando cuenta para el **porcentaje de escritura**, que tiene que quedar por debajo de ~30%). Decí la explicación de ese renglón mientras lo escribís, y si terminás de escribir antes, terminá la frase antes de pasar al siguiente renglón. Ejecutá las celdas siempre con el **botón Run** (mouse), no con el teclado.
8. No muestres Studio, Mercor, información privada ni herramientas de IA. Si Colab muestra funciones de IA (Gemini) o te sugiere código mientras escribís, ignorá la sugerencia y seguí escribiendo vos. Cerrá este guion si está en la misma pantalla.
9. **No uses contraseñas reales tuyas** en ningún momento. Para el ejemplo de la penalización usá `aaa123`.

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

## 1:30–4:30 — Colab, la librería estándar, secrets y pandas

> 🖱️ I'm clicking the second browser tab, at the top of the window, to open Google Colab.
>
> (Hago clic en la segunda pestaña del navegador, arriba de la ventana, para abrir Google Colab.)
>
> 🟢 Google Colab is a free tool from Google that runs Python notebooks in the browser. A notebook mixes text cells, for explanations, and code cells, that I can run one at a time and see the result right below. The code runs on a computer in Google's cloud, so there's nothing to install on my machine.
>
> (Google Colab es una herramienta gratuita de Google que ejecuta notebooks de Python en el navegador. Un notebook mezcla celdas de texto, para las explicaciones, y celdas de código, que puedo ejecutar de a una y ver el resultado justo abajo. El código se ejecuta en una computadora en la nube de Google, así que no hay que instalar nada en mi máquina.)
>
> 🟢 Before I start coding, let me explain where my tools come from. Python comes with a big collection of ready-made modules, called the standard library. Four of the five things I'll import come from there: random, string, secrets, and math. They're part of Python itself, so they work anywhere Python is installed, with no extra installation.
>
> (Antes de empezar a programar, quiero explicar de dónde salen mis herramientas. Python viene con una gran colección de módulos ya hechos, que se llama la librería estándar. Cuatro de las cinco cosas que voy a importar salen de ahí: random, string, secrets y math. Son parte de Python, así que funcionan en cualquier lugar donde esté instalado Python, sin instalar nada más.)
>
> 🟢 The fifth one, pandas, is different: it's not part of Python. It's an external library, made by an open source community. I'll show both.
>
> (La quinta, pandas, es distinta: no es parte de Python. Es una librería externa, hecha por una comunidad de código abierto. Les muestro las dos.)
>
> 🖱️ I'm clicking the third browser tab, at the top of the window, to show the documentation of Python's secrets module.
>
> (Hago clic en la tercera pestaña del navegador, arriba de la ventana, para mostrar la documentación del módulo secrets de Python.)
>
> 🟢 This is the official Python documentation, at docs.python.org, on the page of the secrets module. secrets is part of the standard library since Python 3.6, and it was created exactly for passwords, security tokens, and similar secrets. It generates random values using the most secure source of randomness the operating system has.
>
> (Esta es la documentación oficial de Python, en docs.python.org, en la página del módulo secrets. secrets es parte de la librería estándar desde Python 3.6, y se creó justamente para contraseñas, tokens de seguridad y secretos parecidos. Genera valores aleatorios usando la fuente de aleatoriedad más segura que tiene el sistema operativo.)
>
> 🟢 Why not the regular random module? random is fine for games or simulations, but its numbers come from a formula. If someone sees enough of its output, they can predict the next numbers. For a password, that's unacceptable, so I'll use secrets to pick every character.
>
> (¿Por qué no el módulo random común? random sirve para juegos o simulaciones, pero sus números salen de una fórmula. Si alguien ve suficientes resultados, puede predecir los siguientes. Para una contraseña eso es inaceptable, así que voy a usar secrets para elegir cada carácter.)
>
> 🖱️ I'm scrolling down the secrets page, in the center of the window, with the mouse wheel, to show the choice function.
>
> (Bajo por la página de secrets, en el centro de la ventana, con la rueda del mouse, para mostrar la función choice.)
>
> 🟢 The function I'll use is secrets.choice. It picks one random element from a sequence, like one letter from the alphabet. I'll call it once for every character of the password.
>
> (La función que voy a usar es secrets.choice. Elige un elemento al azar de una secuencia, como una letra del abecedario. La voy a llamar una vez por cada carácter de la contraseña.)
>
> 🖱️ I'm clicking the fourth browser tab, at the top of the window, to show the official pandas website.
>
> (Hago clic en la cuarta pestaña del navegador, arriba de la ventana, para mostrar el sitio oficial de pandas.)
>
> 🟢 This is pandas, at pandas.pydata.org. pandas is a free, open source Python library for working with tables of data, like a spreadsheet inside Python. Its main object is the DataFrame, a table with rows and columns. It's one of the most used libraries in data analysis.
>
> (Esto es pandas, en pandas.pydata.org. pandas es una librería de Python gratuita y de código abierto para trabajar con tablas de datos, como una hoja de cálculo dentro de Python. Su objeto principal es el DataFrame, una tabla con filas y columnas. Es una de las librerías más usadas en análisis de datos.)
>
> 🖱️ I'm scrolling down the pandas homepage, in the center of the window, with the mouse wheel, to show what the project offers.
>
> (Bajo por la página principal de pandas, en el centro de la ventana, con la rueda del mouse, para mostrar lo que ofrece el proyecto.)
>
> 🟢 Because pandas is not part of Python, on a normal computer you install it first, with the command pip install pandas. pip is Python's package installer, and it downloads libraries from the Python Package Index, called PyPI. But Colab already comes with pandas installed, so I can import it directly.
>
> (Como pandas no es parte de Python, en una computadora normal primero hay que instalarla, con el comando pip install pandas. pip es el instalador de paquetes de Python, y descarga las librerías del Python Package Index, que se llama PyPI. Pero Colab ya trae pandas instalada, así que la puedo importar directamente.)
>
> 🟢 In this project, I'll use pandas at the end, to show the ten passwords and their scores in a clean table, with colors.
>
> (En este proyecto voy a usar pandas al final, para mostrar las diez contraseñas y sus puntajes en una tabla prolija, con colores.)
>
> 🖱️ I'm clicking the second browser tab, at the top of the window, to go back to Google Colab.
>
> (Hago clic en la segunda pestaña del navegador, arriba de la ventana, para volver a Google Colab.)

---

## 4:30–7:30 — Notebook nuevo e imports

> 🖱️ I'm clicking the New notebook button at the bottom of the Open notebook dialog, to create a fresh notebook.
>
> (Hago clic en el botón New notebook, abajo del cuadro Open notebook, para crear un notebook nuevo.)
>
> 🖱️ I'm clicking the notebook title field at the top left, and typing password_tool.ipynb, to identify this project. ipynb is the file extension of notebooks.
>
> (Hago clic en el campo del título del notebook, arriba a la izquierda, y escribo password_tool.ipynb, para identificar este proyecto. ipynb es la extensión de los notebooks.)
>
> 🖱️ I'm clicking the plus Text button in the toolbar at the top left, to add a title and the goal.
>
> (Hago clic en el botón + Text de la barra de herramientas, arriba a la izquierda, para agregar un título y el objetivo.)

```markdown
# Password Generator & Strength Validator
Goal: generate passwords with configurable options, score their strength with several criteria, and compare the results.
```

**What each line does:**

- 🟢 `# Password Generator & Strength Validator`: text cells use a format called Markdown. One hash sign at the start of a line makes it the main title of the notebook, in big letters.

  (Las celdas de texto usan un formato que se llama Markdown. Un numeral al principio de la línea la convierte en el título principal del notebook, en letras grandes.)

- 🟢 `Goal: ...`: this line says what the notebook does: generate passwords, score them, and compare them. That way, anyone who opens the notebook understands it right away.

  (Esta línea dice qué hace el notebook: generar contraseñas, ponerles puntaje y compararlas. Así, cualquiera que abra el notebook lo entiende enseguida.)

> 🖱️ I'm clicking the plus Code button in the toolbar at the top left, to add a code cell with the imports.
>
> (Hago clic en el botón + Code de la barra de herramientas, arriba a la izquierda, para agregar una celda de código con los imports.)
>
> 🟢 An import tells Python to load a module, so I can use its functions in my code. I'll write one import per line, and explain each one.
>
> (Un import le dice a Python que cargue un módulo, para poder usar sus funciones en mi código. Voy a escribir un import por línea y explicar cada uno.)

Escribís la **celda 1**:

```python
import random
import string
import secrets
import math
import pandas as pd
```

**What each line does:**

- 🟢 `import random`: random comes with Python, in the standard library. It generates random numbers. As I said, its normal functions are predictable, so I won't use them to pick characters. I'll only use one part of it, the SystemRandom class, which takes its randomness from the operating system, the same secure source that secrets uses. I need it to shuffle the characters, because secrets doesn't have a shuffle function.

  (random viene con Python, en la librería estándar. Genera números aleatorios. Como dije, sus funciones normales son predecibles, así que no las voy a usar para elegir caracteres. Solo voy a usar una parte, la clase SystemRandom, que toma la aleatoriedad del sistema operativo, la misma fuente segura que usa secrets. La necesito para mezclar los caracteres, porque secrets no tiene una función para mezclar.)

- 🟢 `import string`: string also comes with Python. It has ready-made sets of characters, so I don't have to type the alphabet by hand. I'll use four of them: ascii_lowercase, the 26 lowercase letters; ascii_uppercase, the 26 uppercase letters; digits, the 10 digits; and punctuation, the 32 symbols of the keyboard.

  (string también viene con Python. Tiene conjuntos de caracteres ya armados, así no tengo que escribir el abecedario a mano. Voy a usar cuatro: ascii_lowercase, las 26 minúsculas; ascii_uppercase, las 26 mayúsculas; digits, los 10 dígitos; y punctuation, los 32 símbolos del teclado.)

- 🟢 `import secrets`: secrets is the standard library module I just showed in the documentation. It picks random characters in a way that is safe for passwords, and nobody can predict them.

  (secrets es el módulo de la librería estándar que acabo de mostrar en la documentación. Elige caracteres al azar de una forma segura para contraseñas, y nadie los puede predecir.)

- 🟢 `import math`: math is the standard library module for mathematical functions, like square roots and logarithms. I need the base-2 logarithm, log2, for the entropy formula.

  (math es el módulo de la librería estándar para funciones matemáticas, como raíces cuadradas y logaritmos. Necesito el logaritmo en base 2, log2, para la fórmula de la entropía.)

- 🟢 `import pandas as pd`: and this is pandas, the external library from the website I showed, already installed in Colab. The words "as pd" give it a short name, so I can write pd instead of pandas every time. pd is the name almost everyone uses, so other developers recognize it right away.

  (Y esta es pandas, la librería externa del sitio que mostré, que ya viene instalada en Colab. Las palabras "as pd" le dan un nombre corto, así puedo escribir pd en vez de pandas cada vez. pd es el nombre que usa casi todo el mundo, así otros programadores lo reconocen enseguida.)

> 🖱️ I'm clicking the Run cell button, the play icon to the left of this cell, to load the libraries.
>
> (Hago clic en el botón Run cell, el ícono de play a la izquierda de esta celda, para cargar las librerías.)
>
> 🟢 The cell ran without errors, and there's no output, because imports only load the libraries. If any name were wrong, Python would show an error here. The first run takes a few seconds, because Colab connects to a computer in Google's cloud.
>
> (La celda se ejecutó sin errores, y no hay salida, porque los imports solo cargan las librerías. Si algún nombre estuviera mal, Python mostraría un error acá. La primera ejecución tarda unos segundos, porque Colab se conecta a una computadora en la nube de Google.)

---

## 7:30–12:30 — generate_password()

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for the generator.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para el generador.)

Escribís `## 1. Password generator`, y mientras escribís:

> 🟢 Two hash signs make a section heading, smaller than the main title. I'll number every section, so the notebook is easy to follow.
>
> (Dos numerales hacen un título de sección, más chico que el título principal. Voy a numerar cada sección, así el notebook es fácil de seguir.)
>
> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell for the generator function.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código para la función generadora.)
>
> 🟢 This function is the heart of the generator. The idea is simple: collect the allowed characters, pick one of each type I asked for, fill the rest at random, and shuffle everything. I'll explain each line as I type it.
>
> (Esta función es el corazón del generador. La idea es simple: juntar los caracteres permitidos, elegir uno de cada tipo que pedí, completar el resto al azar y mezclar todo. Voy a explicar cada línea mientras la escribo.)

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

- 🟢 `def generate_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):`: def is the Python keyword that creates a function, a block of code with a name that I can reuse. This one is called generate_password, and it takes four parameters inside the parentheses. length is how many characters the password will have. use_uppercase, use_digits, and use_symbols are switches, True or False, that turn each type of character on or off. The values after the equal signs are defaults: if I call the function without options, it makes a 12-character password with every type of character. The colon at the end opens the body of the function, and everything indented below it belongs to the function.

  (def es la palabra clave de Python que crea una función, un bloque de código con nombre que puedo reutilizar. Esta se llama generate_password y recibe cuatro parámetros entre los paréntesis. length es cuántos caracteres va a tener la contraseña. use_uppercase, use_digits y use_symbols son interruptores, True o False, que activan o desactivan cada tipo de carácter. Los valores después de los signos igual son valores por defecto: si llamo a la función sin opciones, arma una contraseña de 12 caracteres con todos los tipos. Los dos puntos del final abren el cuerpo de la función, y todo lo que está con sangría abajo pertenece a la función.)

- 🟢 `pools = [string.ascii_lowercase]`: pools is a list, written with square brackets, that will hold the groups of characters I'm allowed to use. I call each group a pool. It starts with string.ascii_lowercase, the 26 lowercase letters from a to z. Lowercase letters are always included, so every password has a base of letters.

  (pools es una lista, escrita con corchetes, que va a guardar los grupos de caracteres que puedo usar. A cada grupo lo llamo pool. Empieza con string.ascii_lowercase, las 26 minúsculas de la a a la z. Las minúsculas siempre se incluyen, así toda contraseña tiene una base de letras.)

- 🟢 `if use_uppercase:`: if checks a condition. If the use_uppercase switch is True, Python runs the indented line below. If it's False, it skips it.

  (if comprueba una condición. Si el interruptor use_uppercase es True, Python ejecuta la línea con sangría de abajo. Si es False, la saltea.)

- 🟢 `pools.append(string.ascii_uppercase)`: append adds an element at the end of a list. Here it adds string.ascii_uppercase, the 26 uppercase letters from A to Z.

  (append agrega un elemento al final de una lista. Acá agrega string.ascii_uppercase, las 26 mayúsculas de la A a la Z.)

- 🟢 `if use_digits:`: the same check, now for the digits switch.

  (La misma comprobación, ahora para el interruptor de los dígitos.)

- 🟢 `pools.append(string.digits)`: if it's on, it adds string.digits, the ten digits from 0 to 9.

  (Si está activado, agrega string.digits, los diez dígitos del 0 al 9.)

- 🟢 `if use_symbols:`: and the same check for the symbols switch.

  (Y la misma comprobación para el interruptor de los símbolos.)

- 🟢 `pools.append(string.punctuation)`: string.punctuation has the 32 symbols of a standard keyboard, like the exclamation mark, the at sign, the hash, and the brackets.

  (string.punctuation tiene los 32 símbolos de un teclado estándar, como el signo de exclamación, la arroba, el numeral y los corchetes.)

- 🟢 `all_chars = "".join(pools)`: join glues the elements of a list into one string. The empty quotes before the dot mean I put nothing between them. So all_chars is one long string with every allowed character. With everything on, that's 26 plus 26 plus 10 plus 32, which is 94 characters.

  (join pega los elementos de una lista en un solo texto. Las comillas vacías antes del punto quieren decir que no pongo nada entre ellos. Así, all_chars es un texto largo con todos los caracteres permitidos. Con todo activado, son 26 más 26 más 10 más 32, o sea 94 caracteres.)

- 🟢 `chars = [secrets.choice(pool) for pool in pools]`: this is a list comprehension, a short way to build a list with a loop inside square brackets. For each pool in my list, secrets.choice picks one random character from it. So if I chose four types, chars starts with four characters, one of each type. This guarantees that the password really contains every type I asked for. Without this step, a random password could, by bad luck, have no digits at all.

  (Esto es una list comprehension, una forma corta de armar una lista con un bucle adentro de los corchetes. Por cada pool de mi lista, secrets.choice elige un carácter al azar de ese grupo. Entonces, si elegí cuatro tipos, chars empieza con cuatro caracteres, uno de cada tipo. Esto garantiza que la contraseña de verdad tenga todos los tipos que pedí. Sin este paso, una contraseña aleatoria podría, por mala suerte, no tener ningún dígito.)

- 🟢 `chars += [secrets.choice(all_chars) for _ in range(length - len(chars))]`: now I fill in the rest. len(chars) is how many characters I already have, so length minus len(chars) is how many are missing. range repeats the loop that many times. Each time, secrets.choice picks a random character from all the allowed ones. The underscore is a variable name that means "I don't need the loop counter, I only want to repeat". The plus-equals adds these new characters at the end of the list.

  (Ahora completo el resto. len(chars) es cuántos caracteres ya tengo, así que length menos len(chars) es cuántos faltan. range repite el bucle esa cantidad de veces. Cada vez, secrets.choice elige un carácter al azar entre todos los permitidos. El guion bajo es un nombre de variable que quiere decir "no necesito el contador del bucle, solo quiero repetir". El más-igual agrega estos caracteres nuevos al final de la lista.)

- 🟢 `random.SystemRandom().shuffle(chars)`: at this point, the guaranteed characters are always at the start, in the same order: lowercase first, then uppercase, and so on. That's a pattern, and patterns are bad for passwords. So I shuffle the list. SystemRandom uses the operating system's secure randomness, the same source as secrets, and shuffle mixes the list in place.

  (En este punto, los caracteres garantizados están siempre al principio, en el mismo orden: primero la minúscula, después la mayúscula, y así. Eso es un patrón, y los patrones son malos para las contraseñas. Entonces mezclo la lista. SystemRandom usa la aleatoriedad segura del sistema operativo, la misma fuente que secrets, y shuffle mezcla la lista ahí mismo.)

- 🟢 `return "".join(chars)`: finally, join glues the list of characters back into one string, and return sends it back as the result of the function.

  (Por último, join vuelve a pegar la lista de caracteres en un solo texto, y return lo devuelve como resultado de la función.)

- 🟢 `print(generate_password(12))`: this line has no indentation, so it's outside the function. It calls the function with a length of 12, and print shows the result. It's a quick test to check that everything works.

  (Esta línea no tiene sangría, así que está fuera de la función. Llama a la función con una longitud de 12, y print muestra el resultado. Es una prueba rápida para comprobar que todo funciona.)

> 🖱️ I'm clicking the Run cell button to the left of this cell, to generate a test password.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para generar una contraseña de prueba.)
>
> 🟢 Here's a random 12-character password. I can see lowercase and uppercase letters, digits, and symbols, as I asked.
>
> (Acá hay una contraseña aleatoria de 12 caracteres. Veo minúsculas, mayúsculas, dígitos y símbolos, como pedí.)

Mirá la contraseña antes de decirlo: siempre tiene los cuatro tipos, pero nombralos señalándolos con el mouse.

> 🖱️ I'm clicking the Run cell button again, to the left of the same cell, to show that each password is different.
>
> (Hago clic en el botón Run cell otra vez, a la izquierda de la misma celda, para mostrar que cada contraseña es distinta.)
>
> 🟢 A new password appeared, completely different from the first one. That's what we want: nobody can predict the next one.
>
> (Apareció una contraseña nueva, completamente distinta de la primera. Eso es lo que queremos: nadie puede predecir la siguiente.)

---

## 12:30–18:00 — check_strength()

> 🖱️ I'm clicking the plus Text button in the toolbar, to add a section heading for the strength checker.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar un título de sección para el validador de fortaleza.)

Escribís `## 2. Strength checker`.

> 🖱️ I'm clicking the plus Code button in the toolbar, to add a code cell for the strength function.
>
> (Hago clic en el botón + Code de la barra de herramientas, para agregar una celda de código para la función de fortaleza.)
>
> 🟢 This cell has two functions. The first one, has_repetition, is a small helper that finds repeated sequences. The second one, check_strength, gives a password a score from 0 to 9: up to three points for length, up to four for variety, up to two for entropy, and minus one for repeated sequences. Then it turns the score into a label: Strong, Medium, or Weak.
>
> (Esta celda tiene dos funciones. La primera, has_repetition, es una función auxiliar chiquita que encuentra secuencias repetidas. La segunda, check_strength, le da a una contraseña un puntaje de 0 a 9: hasta tres puntos por longitud, hasta cuatro por variedad, hasta dos por entropía y menos uno por secuencias repetidas. Después convierte el puntaje en una etiqueta: Strong, Medium o Weak.)

Escribís la **celda 3**:

```python
def has_repetition(password):
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return True
    for size in range(2, len(password) // 2 + 1):
        for i in range(len(password) - 2 * size + 1):
            if password[i:i + size] == password[i + size:i + 2 * size]:
                return True
    return False

def check_strength(password):
    present = [
        any(c.islower() for c in password),
        any(c.isupper() for c in password),
        any(c.isdigit() for c in password),
        any(not c.isalnum() for c in password),
    ]
    sizes = [26, 26, 10, 32]
    pool = sum(size for size, found in zip(sizes, present) if found)
    entropy = len(password) * math.log2(pool)
    score = (len(password) >= 8) + (len(password) >= 12) + (len(password) >= 16)
    score += sum(present)
    score += (entropy >= 60) + (entropy >= 80)
    if has_repetition(password):
        score -= 1
    label = "Strong" if score >= 8 else "Medium" if score >= 5 else "Weak"
    return {"strength_score": score, "strength_label": label, "entropy": round(entropy, 1)}

print(check_strength("aaa123"))
print(check_strength(generate_password(16)))
```

**What each line does:**

- 🟢 `def has_repetition(password):`: first, a small helper function. It checks if a password has a repeated sequence, and it returns True or False. I write it apart, so check_strength stays short and easy to read.

  (Primero, una función auxiliar chiquita. Revisa si una contraseña tiene una secuencia repetida, y devuelve True o False. La escribo aparte, así check_strength queda corta y fácil de leer.)

- 🟢 `for i in range(len(password) - 2):`: the first check looks for the same character three times in a row. This loop goes through the positions of the password, one by one. i is the position, starting at 0. I stop two positions before the end, because at each position I'll look at three characters: this one and the next two.

  (La primera comprobación busca el mismo carácter tres veces seguidas. Este bucle recorre las posiciones de la contraseña, una por una. i es la posición, empezando en 0. Freno dos posiciones antes del final, porque en cada posición voy a mirar tres caracteres: este y los dos siguientes.)

- 🟢 `if password[i] == password[i + 1] == password[i + 2]:`: square brackets with a number read the character at that position. The double equal sign compares. So this asks: is the character at i equal to the next one, and to the one after that? If yes, it's the same character three times in a row, like "aaa".

  (Los corchetes con un número leen el carácter que está en esa posición. El doble signo igual compara. Entonces esto pregunta: ¿el carácter en i es igual al siguiente, y al que viene después? Si es así, es el mismo carácter tres veces seguidas, como "aaa".)

- 🟢 `return True`: then I already know there's a repetition, so the function answers True and stops right there.

  (Entonces ya sé que hay una repetición, así que la función responde True y termina ahí mismo.)

- 🟢 `for size in range(2, len(password) // 2 + 1):`: the second check looks for a chunk that repeats right after itself, like "abab", where "ab" appears twice. size is the size of the chunk: from 2 characters up to half of the password, because a chunk and its copy have to fit inside the password. The double slash divides and drops the decimals, so half of 7 is 3.

  (La segunda comprobación busca un pedazo que se repite justo después de sí mismo, como "abab", donde "ab" aparece dos veces. size es el tamaño del pedazo: de 2 caracteres hasta la mitad de la contraseña, porque el pedazo y su copia tienen que entrar en la contraseña. La doble barra divide y descarta los decimales, así que la mitad de 7 es 3.)

- 🟢 `for i in range(len(password) - 2 * size + 1):`: a loop inside the other loop. For each size, i goes through every position where a chunk and its copy still fit inside the password.

  (Un bucle adentro del otro bucle. Para cada tamaño, i recorre todas las posiciones donde todavía entran un pedazo y su copia dentro de la contraseña.)

- 🟢 `if password[i:i + size] == password[i + size:i + 2 * size]:`: a colon inside the square brackets cuts a slice of the text, from the first position up to the second one. The left side is the chunk that starts at i. The right side is the chunk that comes right after it, with the same size. If they're equal, like "ab" and "ab" in "abab", it's a repetition.

  (Los dos puntos adentro de los corchetes cortan un pedazo del texto, desde la primera posición hasta la segunda. El lado izquierdo es el pedazo que empieza en i. El lado derecho es el pedazo que viene justo después, del mismo tamaño. Si son iguales, como "ab" y "ab" en "abab", es una repetición.)

- 🟢 `return True`: again, if I find one, the answer is True.

  (Otra vez, si encuentro una, la respuesta es True.)

- 🟢 `return False`: this line is at the same level as the for loops, not inside them, so it only runs if both loops finish without finding anything. That means there's no repetition, so the answer is False.

  (Esta línea está al mismo nivel que los bucles for, no adentro, así que solo se ejecuta si los dos bucles terminan sin encontrar nada. Eso quiere decir que no hay repetición, así que la respuesta es False.)

- 🟢 `def check_strength(password):`: now the main function, called check_strength. It receives one password, as text, and it will return its score, its label, and its entropy.

  (Ahora la función principal, que se llama check_strength. Recibe una contraseña, como texto, y va a devolver su puntaje, su etiqueta y su entropía.)

- 🟢 `present = [`: present will be a list of four True or False values, one for each type of character: lowercase, uppercase, digits, and symbols. I write each check on its own line, so it's easy to read.

  (present va a ser una lista de cuatro valores True o False, uno por cada tipo de carácter: minúsculas, mayúsculas, dígitos y símbolos. Escribo cada comprobación en su propia línea, así es fácil de leer.)

- 🟢 `any(c.islower() for c in password),`: c goes through each character of the password, one by one. islower is a text method that says if a character is a lowercase letter. any returns True if at least one of them is True. So this is True if the password has at least one lowercase letter.

  (c recorre cada carácter de la contraseña, uno por uno. islower es un método de texto que dice si un carácter es una letra minúscula. any devuelve True si al menos uno es True. Entonces esto es True si la contraseña tiene al menos una minúscula.)

- 🟢 `any(c.isupper() for c in password),`: the same idea with isupper, which checks for uppercase letters.

  (La misma idea con isupper, que revisa si hay mayúsculas.)

- 🟢 `any(c.isdigit() for c in password),`: and with isdigit, which checks for digits, from 0 to 9.

  (Y con isdigit, que revisa si hay dígitos, del 0 al 9.)

- 🟢 `any(not c.isalnum() for c in password),`: isalnum means alphanumeric: a letter or a digit. The word not flips it, so this is True for any character that is not a letter or a digit, which means a symbol.

  (isalnum quiere decir alfanumérico: una letra o un dígito. La palabra not lo invierte, así que esto es True para cualquier carácter que no sea letra ni dígito, o sea un símbolo.)

- 🟢 `]`: the closing bracket ends the list. For example, for "aaa123" the list is True, False, True, False: it has lowercase letters and digits, but no uppercase letters and no symbols.

  (El corchete de cierre termina la lista. Por ejemplo, para "aaa123" la lista es True, False, True, False: tiene minúsculas y dígitos, pero no mayúsculas ni símbolos.)

- 🟢 `sizes = [26, 26, 10, 32]`: sizes is how many characters each type has, in the same order as the checks: 26 lowercase letters, 26 uppercase letters, 10 digits, and 32 symbols.

  (sizes es cuántos caracteres tiene cada tipo, en el mismo orden que las comprobaciones: 26 minúsculas, 26 mayúsculas, 10 dígitos y 32 símbolos.)

- 🟢 `pool = sum(size for size, found in zip(sizes, present) if found)`: zip pairs the two lists element by element: the first size with the first True or False, the second with the second, and so on. Then sum adds only the sizes whose type is present. The result, pool, is how many different characters an attacker would have to try in each position. For "aaa123", that's 26 plus 10, which is 36.

  (zip empareja las dos listas elemento por elemento: el primer tamaño con el primer True o False, el segundo con el segundo, y así. Después sum suma solo los tamaños de los tipos que están presentes. El resultado, pool, es cuántos caracteres distintos tendría que probar un atacante en cada posición. Para "aaa123" son 26 más 10, o sea 36.)

- 🟢 `entropy = len(password) * math.log2(pool)`: this is the entropy formula, measured in bits. math.log2 is the base-2 logarithm, from the math module: it says how many bits one character from the pool is worth. Multiplying by the length gives the total for the password. Each extra bit doubles the number of guesses an attacker needs. For "aaa123", it's 6 times log2 of 36, about 31 bits.

  (Esta es la fórmula de la entropía, medida en bits. math.log2 es el logaritmo en base 2, del módulo math: dice cuántos bits vale un carácter del pool. Al multiplicarlo por la longitud da el total de la contraseña. Cada bit extra duplica la cantidad de intentos que necesita un atacante. Para "aaa123" es 6 por log2 de 36, unos 31 bits.)

- 🟢 `score = (len(password) >= 8) + (len(password) >= 12) + (len(password) >= 16)`: now the score. len gives the length of the password. Each comparison, like len(password) >= 8, gives True or False. In Python, True counts as 1 and False as 0, so I can add them. A password gets one point for reaching 8 characters, another for 12, and another for 16: up to three points for length.

  (Ahora el puntaje. len da la longitud de la contraseña. Cada comparación, como len(password) >= 8, da True o False. En Python, True vale 1 y False vale 0, así que los puedo sumar. Una contraseña suma un punto por llegar a 8 caracteres, otro por 12 y otro por 16: hasta tres puntos por longitud.)

- 🟢 `score += sum(present)`: plus-equals adds to the score. sum(present) counts the True values, so the password gets one point for each type of character it has: up to four points for variety.

  (El más-igual suma al puntaje. sum(present) cuenta los valores True, así que la contraseña suma un punto por cada tipo de carácter que tiene: hasta cuatro puntos por variedad.)

- 🟢 `score += (entropy >= 60) + (entropy >= 80)`: the same trick with the entropy: one more point for 60 bits or more, and another for 80 bits or more. Up to two points.

  (El mismo truco con la entropía: un punto más por 60 bits o más, y otro por 80 bits o más. Hasta dos puntos.)

- 🟢 `if has_repetition(password):`: here I use my helper function from the top of the cell. It answers True if the password has the same character three times in a row, like "aaa", or a chunk repeated right after itself, like "abab".

  (Acá uso mi función auxiliar del principio de la celda. Responde True si la contraseña tiene el mismo carácter tres veces seguidas, como "aaa", o un pedazo repetido justo después de sí mismo, como "abab".)

- 🟢 `score -= 1`: if a repetition is found, minus-equals takes one point away, because repeated patterns make a password easier to guess.

  (Si encuentra una repetición, el menos-igual resta un punto, porque los patrones repetidos hacen que una contraseña sea más fácil de adivinar.)

- 🟢 `label = "Strong" if score >= 8 else "Medium" if score >= 5 else "Weak"`: this is a conditional expression, an if and else written in one line. If the score is 8 or more, the label is Strong. Otherwise, if it's 5 or more, it's Medium. Otherwise, it's Weak.

  (Esto es una expresión condicional, un if y un else escritos en una sola línea. Si el puntaje es 8 o más, la etiqueta es Strong. Si no, si es 5 o más, es Medium. Si no, es Weak.)

- 🟢 `return {"strength_score": score, "strength_label": label, "entropy": round(entropy, 1)}`: the function returns a dictionary, written with curly braces. A dictionary stores pairs of a key and a value. Here there are three keys: strength_score, strength_label, and entropy. round with a 1 keeps one decimal, so the number is easy to read.

  (La función devuelve un diccionario, escrito con llaves. Un diccionario guarda pares de clave y valor. Acá hay tres claves: strength_score, strength_label y entropy. round con un 1 deja un decimal, así el número es fácil de leer.)

- 🟢 `print(check_strength("aaa123"))`: outside the function, a test with "aaa123", an example of a weak password with a repetition. It's not a real password.

  (Fuera de la función, una prueba con "aaa123", un ejemplo de contraseña débil con una repetición. No es una contraseña real.)

- 🟢 `print(check_strength(generate_password(16)))`: and a second test that connects both functions: generate_password makes a random 16-character password, and check_strength scores it right away.

  (Y una segunda prueba que conecta las dos funciones: generate_password arma una contraseña aleatoria de 16 caracteres, y check_strength le pone el puntaje enseguida.)

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

## 18:00–24:00 — 10 contraseñas, la tabla y la más débil y la más fuerte

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

- 🟢 `configs = [`: configs is a list of ten configurations, ordered from weak to strong. Each one is a tuple, a group of values in parentheses. Each tuple has four values, in the same order as my function's parameters: the length, and then True or False for uppercase, digits, and symbols.

  (configs es una lista de diez configuraciones, ordenadas de débil a fuerte. Cada una es una tupla, un grupo de valores entre paréntesis. Cada tupla tiene cuatro valores, en el mismo orden que los parámetros de mi función: la longitud, y después True o False para mayúsculas, dígitos y símbolos.)

- 🟢 `(6, False, False, False), (8, False, False, False), (8, True, False, False),`: the first three: 6 lowercase letters only; 8 lowercase letters only; and 8 characters with lowercase and uppercase letters.

  (Las primeras tres: solo 6 minúsculas; solo 8 minúsculas; y 8 caracteres con minúsculas y mayúsculas.)

- 🟢 `(8, True, True, False), (10, True, True, True), (12, True, True, False),`: the next three: 8 characters with letters and digits; 10 characters with everything; and 12 characters with letters and digits, but no symbols.

  (Las tres siguientes: 8 caracteres con letras y dígitos; 10 caracteres con todo; y 12 caracteres con letras y dígitos, pero sin símbolos.)

- 🟢 `(12, True, True, True), (16, True, True, False), (16, True, True, True),`: then 12 characters with everything; 16 characters with letters and digits; and 16 characters with everything.

  (Después, 12 caracteres con todo; 16 caracteres con letras y dígitos; y 16 caracteres con todo.)

- 🟢 `(20, True, True, True),`: and the last one, the strongest: 20 characters with every type.

  (Y la última, la más fuerte: 20 caracteres con todos los tipos.)

- 🟢 `]`: the closing bracket ends the list. I wrote it on several lines only to make it easier to read.

  (El corchete de cierre termina la lista. La escribí en varias líneas solo para que sea más fácil de leer.)

- 🟢 `results = []`: an empty list, where I'll store one result for each password.

  (Una lista vacía, donde voy a guardar un resultado por cada contraseña.)

- 🟢 `for length, upper, digits, symbols in configs:`: the for loop takes one configuration at a time. Because each tuple has four values, Python unpacks them directly into four names: length, upper, digits, and symbols. The indented lines below run once for each configuration, so ten times.

  (El bucle for toma una configuración por vez. Como cada tupla tiene cuatro valores, Python los desempaqueta directamente en cuatro nombres: length, upper, digits y symbols. Las líneas con sangría de abajo se ejecutan una vez por cada configuración, o sea diez veces.)

- 🟢 `password = generate_password(length, upper, digits, symbols)`: inside the loop, I call my generator with those four settings, and save the password.

  (Adentro del bucle, llamo a mi generador con esas cuatro opciones y guardo la contraseña.)

- 🟢 `config = f"upper={upper}, digits={digits}, symbols={symbols}"`: this is an f-string: the letter f before the quotes lets me put variables inside the text, wherever there are curly braces. It builds a readable description of the settings, like "upper=True, digits=True, symbols=False", to show in the table.

  (Esto es un f-string: la letra f antes de las comillas me deja poner variables adentro del texto, donde haya llaves. Arma una descripción legible de las opciones, como "upper=True, digits=True, symbols=False", para mostrarla en la tabla.)

- 🟢 `results.append({"password": password, "length": length, "configuration": config, **check_strength(password)})`: I add a dictionary to the list, with the password, the length, and the configuration. The two asterisks unpack the dictionary that check_strength returns, so its three keys, the score, the label, and the entropy, are added to this same dictionary. Each of these dictionaries will become one row of the table.

  (Agrego un diccionario a la lista, con la contraseña, la longitud y la configuración. Los dos asteriscos desempaquetan el diccionario que devuelve check_strength, así sus tres claves, el puntaje, la etiqueta y la entropía, se suman a este mismo diccionario. Cada uno de estos diccionarios va a ser una fila de la tabla.)

- 🟢 `len(results)`: this line is outside the loop. len counts the elements of the list. Because it's the last line of the cell, Colab shows its value, even without print. It should be 10.

  (Esta línea está fuera del bucle. len cuenta los elementos de la lista. Como es la última línea de la celda, Colab muestra su valor, aunque no tenga print. Debería dar 10.)

> 🖱️ I'm clicking the Run cell button to the left of this cell, to generate the batch.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para generar el lote.)
>
> 🟢 It shows 10, so the list has the ten results I expected. Now I'll show them in a table with pandas.
>
> (Muestra 10, así que la lista tiene los diez resultados que esperaba. Ahora los muestro en una tabla con pandas.)

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

- 🟢 `df = pd.DataFrame(results)`: pd is pandas, with the short name I gave it in the imports. DataFrame is the pandas table I showed on the website. It turns my list of dictionaries into a table: each dictionary becomes a row, and each key becomes a column name. I call it df, short for DataFrame, which is the usual name.

  (pd es pandas, con el nombre corto que le di en los imports. DataFrame es la tabla de pandas que mostré en el sitio. Convierte mi lista de diccionarios en una tabla: cada diccionario se vuelve una fila, y cada clave, el nombre de una columna. La llamo df, abreviatura de DataFrame, que es el nombre habitual.)

- 🟢 `df.style.background_gradient(subset=["strength_score"], cmap="RdYlGn")`: style lets me change how the table looks, without changing the data. background_gradient colors each cell by its value. subset says which columns to color: only strength_score. cmap is the color map: RdYlGn means red, yellow, green, so low scores are red, middle ones yellow, and high ones green. Because it's the last line of the cell, Colab shows the table.

  (style me deja cambiar cómo se ve la tabla, sin cambiar los datos. background_gradient pinta cada celda según su valor. subset dice qué columnas pintar: solo strength_score. cmap es el mapa de colores: RdYlGn significa rojo, amarillo, verde, así los puntajes bajos quedan en rojo, los del medio en amarillo y los altos en verde. Como es la última línea de la celda, Colab muestra la tabla.)

> 🖱️ I'm clicking the Run cell button to the left of this cell, to show the table.
>
> (Hago clic en el botón Run cell a la izquierda de esta celda, para mostrar la tabla.)

**Compará con la tabla de referencia antes de hablar.** Si alguna fila tiene un punto menos, usá la frase de la penalización de la sección **Cómo se calcula el puntaje** y volvé a ejecutar la celda 4 y la celda 5. Después señalás las columnas de izquierda a derecha y bajás por las filas:

> 🟢 The table has the password, the length, the configuration, the strength score, the label, and the entropy. The numbers on the left, from 0 to 9, are the row numbers that pandas adds.
>
> (La tabla tiene la contraseña, la longitud, la configuración, el puntaje, la etiqueta y la entropía. Los números de la izquierda, del 0 al 9, son los números de fila que agrega pandas.)
>
> 🖱️ I'm moving the mouse down the strength_score column, in the table under the cell, to compare the rows.
>
> (Muevo el mouse por la columna strength_score, en la tabla debajo de la celda, para comparar las filas.)
>
> 🟢 The first four are red and Weak, from 1 to 4 points. The middle three are Medium, with 6, 6, and 7. And the last three are green and Strong, with 8, 9, and 9. The entropy also grows with the length and the variety, from about 28 bits to about 131.
>
> (Las primeras cuatro están en rojo y son Weak, de 1 a 4 puntos. Las tres del medio son Medium, con 6, 6 y 7. Y las últimas tres están en verde y son Strong, con 8, 9 y 9. La entropía también crece con la longitud y la variedad, de unos 28 bits a unos 131.)

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

print("Weakest:", find_weakest(results))
print("Strongest:", find_strongest(results))
```

**What each line does:**

- 🟢 `def find_weakest(results):`: a function that receives the list of results and returns the weakest password.

  (Una función que recibe la lista de resultados y devuelve la contraseña más débil.)

- 🟢 `return min(results, key=lambda r: (r["strength_score"], r["entropy"]))`: min returns the smallest element of a list. But my elements are dictionaries, so I have to tell min what to compare, and that's the key. lambda creates a small function without a name, in one line. For each result r, it returns a pair: the score and the entropy. Python compares pairs from left to right: first the score, and only if two scores are equal, the entropy breaks the tie.

  (min devuelve el elemento más chico de una lista. Pero mis elementos son diccionarios, así que le tengo que decir a min qué comparar, y eso es el key. lambda crea una función chiquita sin nombre, en una línea. Para cada resultado r, devuelve un par: el puntaje y la entropía. Python compara los pares de izquierda a derecha: primero el puntaje, y solo si dos puntajes son iguales, la entropía desempata.)

- 🟢 `def find_strongest(results):`: the same idea, a function for the strongest password.

  (La misma idea, una función para la contraseña más fuerte.)

- 🟢 `return max(results, key=lambda r: (r["strength_score"], r["entropy"]))`: max returns the largest element, with the same key: the highest score first, and the highest entropy if there's a tie.

  (max devuelve el elemento más grande, con el mismo key: primero el puntaje más alto, y la entropía más alta si hay empate.)

- 🟢 `print("Weakest:", find_weakest(results))`: I call find_weakest with my ten results, and print shows the answer. print can show several values separated by commas: first the word Weakest, and then the whole dictionary of the weakest password, with its password, length, configuration, score, label, and entropy.

  (Llamo a find_weakest con mis diez resultados, y print muestra la respuesta. print puede mostrar varios valores separados por comas: primero la palabra Weakest, y después el diccionario completo de la contraseña más débil, con su contraseña, longitud, configuración, puntaje, etiqueta y entropía.)

- 🟢 `print("Strongest:", find_strongest(results))`: the same line for the strongest password, using find_strongest.

  (La misma línea para la contraseña más fuerte, usando find_strongest.)

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

## 24:00–26:00 — Conclusiones

> 🖱️ I'm clicking the plus Text button in the toolbar at the top left, to add the conclusions and recommendations.
>
> (Hago clic en el botón + Text de la barra de herramientas, para agregar las conclusiones y recomendaciones.)

Mientras escribís, decí en voz alta lo que vas escribiendo:

```markdown
## 6. Conclusions
- Weakest: 6 lowercase letters (score 1, about 28 bits).
- Strongest: 20 characters with every type (score 9, about 131 bits).
- Length matters most: 16 characters without symbols (score 8) beats 12 with symbols (score 7).
- Use 16+ characters, every type, no repeated patterns, and the secrets module.
```

**What each line does:**

- 🟢 `## 6. Conclusions`: the last section heading. Each line below starts with a dash, which makes a bullet point.

  (El último título de sección. Cada línea de abajo empieza con un guion, que hace una viñeta.)

- 🟢 `- Weakest: ...`: the weakest was 6 lowercase letters, with a score of 1, Weak, and about 28 bits of entropy. Short passwords with only one type of character can be guessed very quickly.

  (La más débil fue la de 6 minúsculas, con puntaje 1, Weak, y unos 28 bits de entropía. Las contraseñas cortas con un solo tipo de carácter se pueden adivinar muy rápido.)

- 🟢 `- Strongest: ...`: the strongest was 20 characters with uppercase and lowercase letters, digits, and symbols, with a score of 9, Strong, and about 131 bits.

  (La más fuerte fue la de 20 caracteres con mayúsculas, minúsculas, dígitos y símbolos, con puntaje 9, Strong, y unos 131 bits.)

- 🟢 `- Length matters most: ...`: a 16-character password with letters and digits, but no symbols, scored 8. That's more than a 12-character password with symbols, which scored 7.

  (Una contraseña de 16 caracteres con letras y dígitos, pero sin símbolos, sacó 8. Eso es más que una de 12 caracteres con símbolos, que sacó 7.)

- 🟢 `- Use 16+ characters, ...`: my recommendations: at least 16 characters, every type of character, no repeated characters or patterns, and always the secrets module, not plain random, to generate them.

  (Mis recomendaciones: al menos 16 caracteres, todos los tipos de carácter, nada de caracteres ni patrones repetidos, y siempre el módulo secrets, no random común, para generarlas.)

> 🟢 The most interesting result is that length matters more than symbols. A 16-character password with letters and digits is stronger than a 12-character password with symbols, because each extra character multiplies the number of possible passwords.
>
> (El resultado más interesante es que la longitud importa más que los símbolos. Una contraseña de 16 caracteres con letras y dígitos es más fuerte que una de 12 con símbolos, porque cada carácter extra multiplica la cantidad de contraseñas posibles.)

---

## 26:00–30:00 — Epílogo (4 minutos)

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
> 🟢 Let me summarize the whole project. We started with the title and the goal, and then imported five libraries. Four come with Python, in the standard library: secrets and random for secure randomness, string for the character sets, and math for the entropy. And pandas, an external library already installed in Colab, for the table.
>
> (Les resumo todo el proyecto. Empezamos con el título y el objetivo, y después importamos cinco librerías. Cuatro vienen con Python, en la librería estándar: secrets y random para la aleatoriedad segura, string para los conjuntos de caracteres y math para la entropía. Y pandas, una librería externa que ya viene instalada en Colab, para la tabla.)
>
> 🖱️ I'm scrolling down the notebook, in the center of the screen, to section 1, Password generator, to review the generator.
>
> (Bajo por el notebook, en el centro de la pantalla, hasta la sección 1, Password generator, para repasar el generador.)
>
> 🟢 In section 1, we built the generator. It takes a length and three options, guarantees one character of each chosen type, fills the rest at random with secrets, and shuffles everything.
>
> (En la sección 1 armamos el generador. Recibe una longitud y tres opciones, garantiza un carácter de cada tipo elegido, completa el resto al azar con secrets y mezcla todo.)
>
> 🖱️ I'm scrolling down the notebook, in the center of the screen, to section 2, Strength checker, to review the scoring.
>
> (Bajo por el notebook, en el centro de la pantalla, hasta la sección 2, Strength checker, para repasar el puntaje.)
>
> 🟢 In section 2, we built the checker, with a helper function that finds repeated sequences. It gives up to three points for length, four for variety, and two for entropy, and takes one point away for repeated sequences. We checked it by hand with "aaa123", which scored 1.
>
> (En la sección 2 armamos el validador, con una función auxiliar que encuentra secuencias repetidas. Da hasta tres puntos por longitud, cuatro por variedad y dos por entropía, y resta un punto por secuencias repetidas. Lo comprobamos a mano con "aaa123", que sacó 1.)
>
> 🖱️ I'm scrolling down the notebook, in the center of the screen, to sections 3 and 4, to review the batch and the results table.
>
> (Bajo por el notebook, en el centro de la pantalla, hasta las secciones 3 y 4, para repasar el lote y la tabla de resultados.)
>
> 🟢 In sections 3 and 4, we generated ten passwords from weak to strong settings and showed them in a colored table: four Weak, three Medium, and three Strong.
>
> (En las secciones 3 y 4 generamos diez contraseñas, de configuraciones débiles a fuertes, y las mostramos en una tabla con colores: cuatro Weak, tres Medium y tres Strong.)
>
> 🖱️ I'm scrolling down the notebook, in the center of the screen, to sections 5 and 6, to review the weakest and strongest passwords and the conclusions.
>
> (Bajo por el notebook, en el centro de la pantalla, hasta las secciones 5 y 6, para repasar la contraseña más débil y la más fuerte, y las conclusiones.)
>
> 🟢 In section 5, we found the weakest, 6 lowercase letters, and the strongest, 20 characters with everything, using the entropy to break the tie. And in section 6, we wrote the conclusions and the recommendations.
>
> (En la sección 5 encontramos la más débil, 6 letras minúsculas, y la más fuerte, 20 caracteres con todo, usando la entropía para desempatar. Y en la sección 6 escribimos las conclusiones y las recomendaciones.)

### Decisiones y próximos pasos

> 🖱️ I'm scrolling slowly up through the notebook, in the center of the screen, with the mouse wheel, to go over the decisions I made.
>
> (Subo despacio por el notebook, en el centro de la pantalla, con la rueda del mouse, para repasar las decisiones que tomé.)
>
> 🟢 In this epilogue, I want to go over my approach. For the generator, I used the secrets module instead of plain random, because password randomness must be unpredictable. I also guaranteed at least one character of each chosen type, so the settings always mean what they say.
>
> (En este epílogo quiero repasar mi enfoque. Para el generador usé el módulo secrets en vez de random común, porque la aleatoriedad de una contraseña tiene que ser impredecible. También garanticé al menos un carácter de cada tipo elegido, así la configuración siempre cumple lo que dice.)
>
> 🟢 That guarantee also makes the results stable. The passwords change every time I run the notebook, but the scores almost always stay the same, because they depend on the settings. The only exception is a rare random repetition, which costs one point.
>
> (Esa garantía también hace que los resultados sean estables. Las contraseñas cambian cada vez que ejecuto el notebook, pero los puntajes casi siempre se mantienen, porque dependen de la configuración. La única excepción es una repetición al azar, que pasa pocas veces y resta un punto.)
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
