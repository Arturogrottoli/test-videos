# us5w8631 — Python Environment Setup

Guion paso a paso para grabar la tarea **us5w8631**: configurar un proyecto Python en **Visual Studio Code** con un entorno virtual (**.venv**), **Pylint** para el análisis estático y **Black** para el formateo. En la grabación mostrás cómo las dos herramientas encuentran y corrigen problemas en un `calculator.py` y dejás todo configurado en `settings.json`. La grabación tiene que durar **entre 15:00 y 50:59**. Este guion apunta a unos **22 minutos**, epílogo incluido.

**Cómo leer este guion:**

- Las frases que empiezan con 🖱️ las decís **en el momento de hacer clic, desplazarte o escribir**. Siempre dicen **qué** elemento usás, **dónde** está en la pantalla y **por qué** lo usás. Son las que revisa AutoQC.
- Las frases que empiezan con 🟢 son la explicación que **decís en inglés** entre una acción y otra.
- Debajo de cada bloque de código, la lista **What each line does** explica cada línea en inglés. La leés en voz alta mientras escribís esa línea.
- El resto, en castellano, es lo que hacés en pantalla. Las traducciones aparecen entre paréntesis después de cada frase.

> **Importante:** el Goal de Studio tiene prioridad sobre este guion. La tarea arranca desde cero, sin archivos externos. **Esta tarea no se puede hacer en Colab**: necesita Python instalado en la computadora donde grabás.

---

## Archivos de la carpeta

```
us5w8631-python-environment/
├── README.md
└── solution/                 ← resultado final de referencia (NO lo abras durante la grabación)
    ├── calculator.py         ← el archivo ya corregido
    └── .vscode/settings.json ← la configuración del proyecto
```

---

## Antes de grabar

1. Leé el Goal y compará este guion con el campo **Describe your idea** de Studio.
2. **Instalá Python 3** (https://www.python.org/downloads/; en el instalador marcá **Add python.exe to PATH**). En esta PC no está instalado. Comprobá en una terminal que `python --version` funcione.
3. En VS Code, instalá **antes de grabar** la extensión **Python** de Microsoft. Es la que permite elegir el intérprete. Las extensiones **Pylint** y **Black Formatter** las instalás durante la grabación.
4. **Ensayá una vez entera** y anotá lo que te devuelve Pylint la primera vez: los mensajes y la nota sobre 10. Los voy a necesitar en la sección 9:00. Pylint no está instalado en esta PC, así que no pude ejecutarlo para darte la salida exacta. Después borrá la carpeta de práctica.
5. Si al abrir una terminal aparece en rojo un error de **execution policy** (PowerShell no deja ejecutar scripts), no pasa nada: este guion llama siempre a `.venv\Scripts\python` directamente, sin activar el entorno. Igual, conviene evitarlo en la grabación: practicá antes para ver si te aparece.
6. Dejá abiertos el documento **Goal** en el navegador y VS Code (sin ninguna carpeta abierta). Agrandá la letra (`Ctrl + +`).
7. Mostrá una sola ventana a la vez, maximizada. Cerrá o minimizá todo lo demás, para que ninguna ventana tape a otra.
8. Pausa de ~1 segundo después de cada clic y nunca más de 45 segundos en silencio. Mientras se instala algo, seguí explicando.
9. No muestres Studio, Mercor, información privada ni herramientas de IA, ni la carpeta `solution`. Cerrá este guion si está en la misma pantalla.

---

## 0:00–0:45 — Mostrar el Goal

> 🖱️ I'm on the Goal document in the browser, to show what this task asks for.
>
> (Estoy en el documento del Goal, en el navegador, para mostrar qué pide esta tarea.)
>
> 🟢 As a Python developer, I'll set up a professional project in VS Code: a virtual environment, Pylint to find code-quality problems, and Black to format the code. Then I'll show both tools working on a small calculator file.
>
> (Como desarrollador Python, voy a configurar un proyecto profesional en VS Code: un entorno virtual, Pylint para encontrar problemas de calidad de código y Black para formatear el código. Después voy a mostrar las dos herramientas funcionando en un archivo chico de calculadora.)

---

## 0:45–4:30 — Carpeta del proyecto y entorno virtual

> 🖱️ I'm clicking the VS Code icon in the taskbar at the bottom of the screen, to open the code editor.
>
> (Hago clic en el ícono de VS Code en la barra de tareas, abajo de la pantalla, para abrir el editor de código.)
>
> 🖱️ I'm opening the File menu at the top left and choosing Open Folder, to create and open the project folder.
>
> (Abro el menú File, arriba a la izquierda, y elijo Open Folder, para crear y abrir la carpeta del proyecto.)
>
> 🖱️ In the dialog, I'm going to the Desktop, clicking the New folder button at the top, and typing calculator-project, to create the project folder.
>
> (En el cuadro voy al Escritorio, hago clic en el botón New folder de arriba y escribo calculator-project, para crear la carpeta del proyecto.)
>
> 🖱️ I'm selecting the calculator-project folder and clicking the Select Folder button at the bottom right, to open it in VS Code.
>
> (Selecciono la carpeta calculator-project y hago clic en el botón Select Folder, abajo a la derecha, para abrirla en VS Code.)

Si VS Code pregunta si confiás en los autores: *"I'm clicking Yes, I trust the authors, in the center of the dialog, because this is my own folder."*

> 🖱️ I'm opening the Terminal menu at the top and choosing New Terminal, to run commands inside the project folder.
>
> (Abro el menú Terminal de arriba y elijo New Terminal, para ejecutar comandos dentro de la carpeta del proyecto.)
>
> 🟢 First, a virtual environment. It's a private copy of Python just for this project, with its own packages. That way, the tools I install here don't mix with other projects, and anyone can recreate the same setup.
>
> (Primero, un entorno virtual. Es una copia privada de Python solo para este proyecto, con sus propios paquetes. Así, las herramientas que instalo acá no se mezclan con otros proyectos, y cualquiera puede recrear la misma configuración.)
>
> 🖱️ I'm typing the venv command in the terminal at the bottom and pressing Enter, to create the virtual environment.
>
> (Escribo el comando venv en la terminal de abajo y presiono Enter, para crear el entorno virtual.)

```
python -m venv .venv
```

**What each line does:**

- 🟢 `python -m venv .venv`: -m runs a module that comes with Python, venv, which creates a virtual environment. .venv is the folder name. The dot at the start is the usual convention, and VS Code recognizes it automatically.

> 🟢 The .venv folder appeared in the Explorer panel on the left. It contains its own Python and its own packages.
>
> (La carpeta .venv apareció en el panel Explorer de la izquierda. Tiene su propio Python y sus propios paquetes.)

---

## 4:30–8:00 — Elegir el intérprete e instalar Pylint y Black

> 🖱️ I'm opening the View menu at the top and choosing Command Palette, to tell VS Code which Python to use.
>
> (Abro el menú View de arriba y elijo Command Palette, para indicarle a VS Code qué Python usar.)
>
> 🖱️ I'm typing Python: Select Interpreter in the box at the top, and choosing the option that says .venv, marked as Recommended, so this project uses the virtual environment.
>
> (Escribo Python: Select Interpreter en el cuadro de arriba y elijo la opción que dice .venv, marcada como Recommended, para que este proyecto use el entorno virtual.)
>
> 🟢 Now the status bar at the bottom right shows the Python version with .venv. VS Code will run, check, and format this project's code with the virtual environment.
>
> (Ahora la barra de estado, abajo a la derecha, muestra la versión de Python con .venv. VS Code va a ejecutar, revisar y formatear el código de este proyecto con el entorno virtual.)
>
> 🖱️ I'm clicking in the terminal at the bottom, and typing the pip install command, to install Pylint and Black inside the virtual environment.
>
> (Hago clic en la terminal de abajo y escribo el comando pip install, para instalar Pylint y Black dentro del entorno virtual.)

```
.venv\Scripts\python -m pip install pylint black
```

**What each line does:**

- 🟢 `.venv\Scripts\python`: I call the Python inside the virtual environment directly, so the packages go into .venv and not into the global Python.
- 🟢 `-m pip install pylint black`: pip is Python's package installer. It downloads and installs Pylint and Black.

> 🟢 While it installs: Pylint is a linter. It reads the code without running it and reports errors, bad practices, and style problems. Black is a formatter. It rewrites the code with a single consistent style, so nobody has to argue about spaces or line breaks.
>
> (Mientras se instala: Pylint es un linter. Lee el código sin ejecutarlo e informa errores, malas prácticas y problemas de estilo. Black es un formateador. Reescribe el código con un único estilo consistente, así nadie tiene que discutir sobre espacios o saltos de línea.)
>
> 🖱️ I'm clicking the Extensions icon, the four squares in the left sidebar, typing Pylint in the search box, and clicking Install on the Pylint extension by Microsoft, so VS Code shows Pylint's warnings in the editor.
>
> (Hago clic en el ícono Extensions, los cuatro cuadrados de la barra lateral izquierda, escribo Pylint en el buscador y hago clic en Install en la extensión Pylint de Microsoft, para que VS Code muestre las advertencias de Pylint en el editor.)
>
> 🖱️ I'm typing Black Formatter in the same search box, and clicking Install on the Black Formatter extension by Microsoft, so VS Code can format with Black.
>
> (Escribo Black Formatter en el mismo buscador y hago clic en Install en la extensión Black Formatter de Microsoft, para que VS Code pueda formatear con Black.)
>
> 🖱️ I'm clicking the Explorer icon, the two pages at the top of the left sidebar, to go back to the project files.
>
> (Hago clic en el ícono Explorer, las dos hojas arriba de la barra lateral izquierda, para volver a los archivos del proyecto.)

---

## 8:00–11:30 — calculator.py con problemas a propósito y Pylint

> 🖱️ I'm clicking the New File icon next to the folder name, at the top of the Explorer panel, and typing calculator.py, to create the calculator file.
>
> (Hago clic en el ícono New File al lado del nombre de la carpeta, arriba del panel Explorer, y escribo calculator.py, para crear el archivo de la calculadora.)
>
> 🟢 I'll write basic calculator functions, but I'll include some problems on purpose, so we can see what each tool finds.
>
> (Voy a escribir funciones básicas de calculadora, pero con algunos problemas a propósito, para ver qué encuentra cada herramienta.)

Escribís el archivo **tal cual**, con los problemas:

```python
import os
def Add(a,b):
    return a+b
def subtract( a, b ):
    return a-b
def multiply(a,b): return a*b
def divide(a,b):
    if b==0:
        return None
    return a/b
result=divide(10,0)
if result == None:
    print("Cannot divide by zero")
```

**What each line does:**

- 🟢 `import os`: problem one: I import a module that I never use.
- 🟢 `def Add(a,b): return a+b`: the add function. Problem two: the name starts with a capital letter, but Python functions should use lowercase. There are also no spaces around the plus sign or after the comma.
- 🟢 `def subtract( a, b ): return a-b`: subtract, with extra spaces inside the parentheses.
- 🟢 `def multiply(a,b): return a*b`: multiply, with the whole function on one line.
- 🟢 `def divide(a,b): if b==0: return None ... return a/b`: divide returns None when b is zero, to avoid a division by zero error.
- 🟢 `result=divide(10,0)`: it divides 10 by zero as an example.
- 🟢 `if result == None:`: problem three: in Python, you should compare with None using "is", not two equal signs.
- 🟢 And none of the functions has a docstring, a short description of what it does.

> 🖱️ I'm pressing Control and S to save the file.
>
> (Presiono Control y S para guardar el archivo.)
>
> 🟢 The Pylint extension already underlines some lines in the editor. Let me run Pylint in the terminal to see the full report.
>
> (La extensión de Pylint ya subraya algunas líneas en el editor. Ejecuto Pylint en la terminal para ver el informe completo.)
>
> 🖱️ I'm clicking in the terminal at the bottom and typing the pylint command, to analyze the file.
>
> (Hago clic en la terminal de abajo y escribo el comando pylint, para analizar el archivo.)

```
.venv\Scripts\python -m pylint calculator.py
```

**What each line does:**

- 🟢 `.venv\Scripts\python -m pylint calculator.py`: this runs Pylint from the virtual environment on calculator.py.

Leés los mensajes **que te aparezcan**. Lo esperable es algo así (confirmalo en el ensayo):

| Código | Mensaje | Qué significa |
| ------ | ------- | ------------- |
| C0114 | missing-module-docstring | Al archivo le falta una descripción al principio |
| C0116 | missing-function-docstring | A las funciones les falta descripción |
| C0103 | invalid-name | `Add` no está en snake_case (y quizás `result`, por estar al nivel del módulo) |
| C0321 | multiple-statements | `multiply` tiene dos instrucciones en una línea |
| C0121 | singleton-comparison | `== None` debería ser `is None` |
| W0611 | unused-import | `os` se importa y no se usa |

> 🟢 Pylint lists each problem with the line number, a code, and a short name. The letters mean the type: C is convention, about style and naming. W is a warning, like the unused import. At the end, it gives the code a score out of 10: [YOUR SCORE].
>
> (Pylint lista cada problema con el número de línea, un código y un nombre corto. Las letras indican el tipo: C es convención, sobre estilo y nombres. W es una advertencia, como el import sin usar. Al final le da al código una nota sobre 10: [TU NOTA].)
>
> 🟢 Notice that Pylint doesn't complain about the missing spaces. Modern Pylint leaves formatting to tools like Black. That's why we use both: Pylint for code quality, and Black for formatting.
>
> (Fíjense que Pylint no se queja de los espacios que faltan. Pylint moderno deja el formato a herramientas como Black. Por eso usamos las dos: Pylint para la calidad del código y Black para el formato.)

---

## 11:30–15:30 — Black y corregir lo que encontró Pylint

> 🖱️ I'm typing the black command in the terminal at the bottom, to format the file.
>
> (Escribo el comando black en la terminal de abajo, para formatear el archivo.)

```
.venv\Scripts\python -m black calculator.py
```

**What each line does:**

- 🟢 `.venv\Scripts\python -m black calculator.py`: this runs Black on calculator.py. It rewrites the file in place.

> 🟢 Black says "reformatted calculator.py". In the editor, the spaces are fixed, multiply is split into two lines, and there are two blank lines between functions, as Python's style guide recommends. But Black only changes the format. It didn't fix the names, the docstrings, or the unused import. Those I fix myself.
>
> (Black dice "reformatted calculator.py". En el editor, los espacios están corregidos, multiply quedó en dos líneas y hay dos líneas en blanco entre funciones, como recomienda la guía de estilo de Python. Pero Black solo cambia el formato. No corrigió los nombres, los docstrings ni el import sin usar. Eso lo corrijo yo.)
>
> 🖱️ I'm editing calculator.py in the editor, to fix each problem that Pylint reported.
>
> (Edito calculator.py en el editor, para corregir cada problema que informó Pylint.)

El archivo queda así:

```python
"""Basic calculator functions."""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b, or None if b is zero."""
    if b == 0:
        return None
    return a / b


def main():
    """Run a quick example of the calculator."""
    result = divide(10, 0)
    if result is None:
        print("Cannot divide by zero")
    print(add(2, 3), subtract(5, 1), multiply(4, 2), divide(9, 3))


if __name__ == "__main__":
    main()
```

**What each line does:**

- 🟢 `"""Basic calculator functions."""`: the module docstring, a description of the whole file. I also removed import os, because it wasn't used.
- 🟢 `def add(a, b):`: I renamed Add to add, in lowercase, following Python's naming style.
- 🟢 `"""Return the sum of a and b."""`: each function now has a one-line docstring that says what it returns.
- 🟢 `def main():`: I moved the example into a main function, so it doesn't run at the module level.
- 🟢 `if result is None:`: now it compares with "is None", the correct way.
- 🟢 `print(add(2, 3), subtract(5, 1), multiply(4, 2), divide(9, 3))`: a quick check of the four functions.
- 🟢 `if __name__ == "__main__": main()`: main only runs when I run the file directly, not when another file imports it.

> 🖱️ I'm pressing Control and S to save, and running the pylint command again in the terminal at the bottom, to check the fixes.
>
> (Presiono Control y S para guardar y vuelvo a ejecutar el comando pylint en la terminal de abajo, para comprobar las correcciones.)
>
> 🟢 Now Pylint rates the code 10 out of 10, with no messages. The underlines in the editor are gone too.
>
> (Ahora Pylint le pone 10 sobre 10 al código, sin mensajes. Los subrayados del editor también desaparecieron.)
>
> 🖱️ I'm typing python calculator.py with the venv path in the terminal, to check that the code still works.
>
> (Escribo python calculator.py con la ruta del venv en la terminal, para comprobar que el código sigue funcionando.)

```
.venv\Scripts\python calculator.py
```

> 🟢 It prints "Cannot divide by zero", and then 5, 4, 8, and 3.0. The code works the same as before, but it's cleaner.
>
> (Imprime "Cannot divide by zero" y después 5, 4, 8 y 3.0. El código funciona igual que antes, pero está más limpio.)

---

## 15:30–19:00 — settings.json y verificar el entorno

> 🖱️ I'm opening the View menu and choosing Command Palette, to create the workspace settings.
>
> (Abro el menú View y elijo Command Palette, para crear la configuración del espacio de trabajo.)
>
> 🖱️ I'm typing Preferences: Open Workspace Settings (JSON) in the box at the top and pressing Enter, so VS Code creates a settings.json file just for this project.
>
> (Escribo Preferences: Open Workspace Settings (JSON) en el cuadro de arriba y presiono Enter, para que VS Code cree un settings.json solo para este proyecto.)
>
> 🟢 VS Code created a .vscode folder with settings.json inside. These settings only apply to this project, and they can be shared with the team.
>
> (VS Code creó una carpeta .vscode con settings.json adentro. Esta configuración solo se aplica a este proyecto y se puede compartir con el equipo.)

Escribís dentro de las llaves:

```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}\\.venv\\Scripts\\python.exe",
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "editor.formatOnSave": true
    },
    "pylint.args": ["--max-line-length=88"]
}
```

**What each line does:**

- 🟢 `"python.defaultInterpreterPath": "...\\.venv\\Scripts\\python.exe"`: the project always uses the Python inside .venv. workspaceFolder means this project folder, and the backslashes are doubled because JSON needs them escaped.
- 🟢 `"[python]": {`: the next settings only apply to Python files.
- 🟢 `"editor.defaultFormatter": "ms-python.black-formatter"`: Black is the formatter for Python files.
- 🟢 `"editor.formatOnSave": true`: every time I save a Python file, Black formats it automatically.
- 🟢 `"pylint.args": ["--max-line-length=88"]`: Black uses lines of up to 88 characters, so I tell Pylint to use the same limit. That way, the two tools never disagree.

> 🖱️ I'm pressing Control and S to save settings.json.
>
> (Presiono Control y S para guardar settings.json.)

Verificás que todo funcione junto:

> 🖱️ I'm clicking the calculator.py tab at the top of the editor, and removing the spaces around the plus sign in the add function, to test format on save.
>
> (Hago clic en la pestaña calculator.py, arriba del editor, y borro los espacios alrededor del signo más en la función add, para probar el formateo al guardar.)
>
> 🖱️ I'm pressing Control and S to save.
>
> (Presiono Control y S para guardar.)
>
> 🟢 As soon as I save, Black puts the spaces back. Format on save works.
>
> (Apenas guardo, Black vuelve a poner los espacios. El formateo al guardar funciona.)
>
> 🖱️ I'm adding import sys at the top of the file, below the docstring, and saving, to test that Pylint still reports problems in the editor.
>
> (Agrego import sys al principio del archivo, debajo del docstring, y guardo, para probar que Pylint sigue informando problemas en el editor.)
>
> 🖱️ I'm opening the View menu and choosing Problems, to see the Problems panel at the bottom.
>
> (Abro el menú View y elijo Problems, para ver el panel Problems abajo.)
>
> 🟢 Pylint marks sys as an unused import, right in the editor and in the Problems panel. Both tools work automatically now.
>
> (Pylint marca sys como un import sin usar, en el editor y en el panel Problems. Las dos herramientas funcionan solas ahora.)
>
> 🖱️ I'm deleting the import sys line and saving, so the file is clean again.
>
> (Borro la línea import sys y guardo, para que el archivo vuelva a quedar limpio.)

---

## 19:00–22:30 — Epílogo (3–4 minutos)

Revisá en las reglas de Odin qué tiene que tener el epílogo y ajustá este texto si piden algo distinto.

> 🖱️ I'm clicking each file in the Explorer panel on the left, calculator.py, settings.json, and the .venv folder, to go over the final project.
>
> (Hago clic en cada archivo del panel Explorer de la izquierda, calculator.py, settings.json y la carpeta .venv, para repasar el proyecto final.)
>
> 🟢 In this epilogue, I want to go over the setup. The virtual environment keeps the project's tools isolated. Pylint and Black are installed inside it, and settings.json tells VS Code to use it, so the project behaves the same for everyone who opens it.
>
> (En este epílogo quiero repasar la configuración. El entorno virtual mantiene aisladas las herramientas del proyecto. Pylint y Black están instalados adentro, y settings.json le dice a VS Code que lo use, así el proyecto se comporta igual para cualquiera que lo abra.)
>
> 🟢 The two tools do different jobs. Black fixed the format in one command: spaces, line breaks, and blank lines. Pylint found the problems that a formatter can't fix: the unused import, the function name, the comparison with None, and the missing docstrings. I fixed those by hand, and the score went up to 10 out of 10.
>
> (Las dos herramientas hacen trabajos distintos. Black corrigió el formato con un solo comando: espacios, saltos de línea y líneas en blanco. Pylint encontró los problemas que un formateador no puede corregir: el import sin usar, el nombre de la función, la comparación con None y los docstrings faltantes. Eso lo corregí a mano, y la nota subió a 10 sobre 10.)
>
> 🟢 One detail I like is matching the line length: Black uses 88 characters, so I set Pylint to 88 too. Without that, the tools could disagree about long lines.
>
> (Un detalle que me gusta es igualar el largo de línea: Black usa 88 caracteres, así que configuré Pylint en 88 también. Sin eso, las herramientas podrían no ponerse de acuerdo sobre las líneas largas.)
>
> 🟢 As next steps, I would save the installed packages in a requirements.txt file, so others can recreate the environment with one command, add unit tests, and run Pylint and Black automatically before every commit. Thanks for watching!
>
> (Como próximos pasos, guardaría los paquetes instalados en un archivo requirements.txt, para que otros puedan recrear el entorno con un solo comando, agregaría pruebas unitarias y ejecutaría Pylint y Black automáticamente antes de cada commit. ¡Gracias por mirar!)

Si el reloj todavía no pasó los 15:00, no cortes: mostrá otra vez el formateo al guardar con otro cambio de espacios y explicá la salida de Pylint línea por línea.

---

## Después de grabar

1. Ejecutá **Run full AutoQC**, no solo *Rerun failing*.
2. Subí los **cuatro archivos por separado**: el **MP4**, el **ZIP original de TaskRecorder**, **Deliverables.zip** y **Metadata.rtf**. En Deliverables.zip va la carpeta del proyecto con `calculator.py` y `.vscode/settings.json`. La carpeta `.venv` puede pesar mucho; revisá en las reglas si hay que incluirla entera.
