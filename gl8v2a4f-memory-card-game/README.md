# gl8v2a4f — Memory Card Game

Guion paso a paso para grabar la tarea **gl8v2a4f**: un juego de memoria hecho desde cero con **HTML**, **CSS** y **JavaScript** puro, en **tres archivos** (`index.html`, `style.css` y `script.js`), en **Visual Studio Code**, y probado en **Firefox**. El juego tiene una grilla de 4×4 con 8 pares, una animación de volteo en 3D y un contador de intentos. Además, las parejas encontradas quedan fijas, aparece un mensaje al ganar y hay un botón para reiniciar. La grabación tiene que durar **entre 15:00 y 50:59**. Este guion apunta a unos **30 minutos**, epílogo incluido, para que escribir código ocupe **menos de un tercio** del video.

**Cómo leer este guion:**

- Las frases que empiezan con 🖱️ las decís **en el momento de hacer clic, desplazarte o escribir**. Siempre dicen **qué** elemento usás, **dónde** está en la pantalla y **por qué** lo usás. Son las que revisa AutoQC.
- Las frases que empiezan con 🟢 son la explicación que **decís en inglés** entre una acción y otra.
- Debajo de cada bloque de código, la lista **What each line does** explica cada línea (o cada grupo de líneas parecidas) en inglés. La leés en voz alta mientras escribís.
- El resto, en castellano, es lo que hacés en pantalla. Las traducciones aparecen entre paréntesis después de cada frase.

> **Importante:** el Goal de Studio tiene prioridad sobre este guion. El Goal que tengo dice **"a single index.html file"**, pero este guion usa **tres archivos** separados. Confirmá en Studio cuál de las dos versiones vale antes de grabar. Si es un solo archivo, la versión anterior está en el historial de git.

---

## Archivos de la carpeta

```
gl8v2a4f-memory-card-game/
├── README.md
└── solution/        ← el juego terminado, para probarlo y practicar (NO lo abras durante la grabación)
    ├── index.html   ← la estructura de la página
    ├── style.css    ← el diseño y la animación
    └── script.js    ← la lógica del juego
```

**Sobre el porcentaje de escritura.** Este es el guion con más código para escribir: unas 100 líneas entre los tres archivos, unos 7–8 minutos tecleando. Para que eso quede en menos de un tercio del video:

- **Planificación de ~6 minutos antes de escribir código** (sección 0:45–7:00). Es todo con el mouse: creás los tres archivos vacíos y recorrés páginas de documentación mientras explicás el juego y las técnicas.
  - **No es una introducción.** La regla dice que la introducción dure **menos de 20 segundos**: si hablás varios minutos al principio sin hacer nada en pantalla, AutoQC puede marcarlo. Por eso la planificación siempre va acompañada de clics y desplazamientos, cada uno con su frase 🖱️.
- Usá el atajo **Emmet** de VS Code: escribís `!` y presionás `Enter`, y VS Code crea solo la estructura básica del HTML.
- Escribí un archivo por vez y **probá en Firefox después de cada uno**. Probar es todo mouse y baja el porcentaje.
- Jugá una partida completa en la prueba final: son varios minutos de clics.
- No apures la explicación: el guion apunta a 25 minutos para que la escritura sea una parte menor del video.

En el juego las cartas usan **letras de la A a la H**, porque escribir emojis en VS Code es lento. Si querés, en el epílogo mencionás que se pueden cambiar por emojis o imágenes.

---

## Antes de grabar

1. Leé el Goal y compará este guion con el campo **Describe your idea** de Studio.
2. Abrí `solution/index.html` en Firefox y jugá una partida, para conocer el comportamiento.
3. Creá una carpeta vacía `Escritorio\memory-game`.
4. Practicá una vez entera, leyendo en voz alta las frases 🖱️ y 🟢, y cronometrá. Después vaciá la carpeta `memory-game`.
5. Dejá abiertas en Firefox **cinco pestañas**, en este orden (comprobá antes que cada enlace abra bien, porque MDN a veces cambia sus direcciones):
   1. El documento **Goal**.
   2. MDN, CSS Grid: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout
   3. MDN, backface-visibility: https://developer.mozilla.org/en-US/docs/Web/CSS/backface-visibility
   4. MDN, setTimeout: https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout
   5. Wikipedia, Fisher–Yates shuffle: https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle

   Dejá abierto también VS Code, sin ninguna carpeta abierta. Agrandá la letra de VS Code (`Ctrl + +`).
6. Mostrá una sola ventana a la vez, maximizada, y pasá de una a otra con la barra de tareas. Cerrá o minimizá todo lo demás, para que ninguna ventana tape a otra.
7. Pausa de ~1 segundo después de cada clic y nunca más de 45 segundos en silencio.
8. No muestres Studio, Mercor, información privada ni herramientas de IA, ni la carpeta `solution`. Cerrá este guion si está en la misma pantalla.

---

## 0:00–0:45 — Mostrar el Goal

> 🖱️ I'm on the Goal document in Firefox, to show what this task asks for.
>
> (Estoy en el documento del Goal, en Firefox, para mostrar qué pide esta tarea.)
>
> 🟢 As a front-end developer, I'll build a memory card game from scratch with HTML, CSS, and plain JavaScript, in three separate files. It will have a 4 by 4 grid with eight pairs, a flip animation, an attempts counter, a win message, and a restart button.
>
> (Como desarrollador front-end, voy a crear desde cero un juego de memoria con HTML, CSS y JavaScript puro, en tres archivos separados. Va a tener una grilla de 4 por 4 con ocho pares, una animación de volteo, un contador de intentos, un mensaje de victoria y un botón para reiniciar.)

---

## 0:45–7:00 — Planificación: los archivos, las reglas y las técnicas

Esta sección no tiene código. Sirve para estirar el video con explicaciones útiles, siempre haciendo algo con el mouse. Hablá tranquilo, sin apurarte.

### Crear el proyecto y los tres archivos vacíos

> 🖱️ I'm clicking the VS Code icon in the taskbar at the bottom of the screen, to open the code editor.
>
> (Hago clic en el ícono de VS Code en la barra de tareas, abajo de la pantalla, para abrir el editor de código.)
>
> 🖱️ I'm opening the File menu at the top left and choosing Open Folder, selecting the memory-game folder on the Desktop, and clicking Select Folder at the bottom right.
>
> (Abro el menú File, arriba a la izquierda, elijo Open Folder, selecciono la carpeta memory-game del Escritorio y hago clic en Select Folder, abajo a la derecha.)

Si VS Code pregunta si confiás en los autores: *"I'm clicking Yes, I trust the authors, in the center of the dialog, because this is my own folder."*

> 🟢 Before writing any code, I'll plan the project. I'll split the game into three files, each with one job: index.html for the structure, style.css for the look and the animation, and script.js for the game logic. This is called separation of concerns. Keeping them separate makes the code easier to read, to test, and to change. For example, a designer could change the colors in style.css without touching the game logic.
>
> (Antes de escribir código, voy a planificar el proyecto. Voy a dividir el juego en tres archivos, cada uno con una tarea: index.html para la estructura, style.css para el aspecto y la animación, y script.js para la lógica del juego. Esto se llama separación de responsabilidades. Tenerlos separados hace que el código sea más fácil de leer, de probar y de cambiar. Por ejemplo, un diseñador podría cambiar los colores en style.css sin tocar la lógica del juego.)
>
> 🖱️ I'm clicking the New File icon next to the folder name, at the top of the Explorer panel on the left, and typing index.html, to create the page.
>
> (Hago clic en el ícono New File al lado del nombre de la carpeta, arriba del panel Explorer de la izquierda, y escribo index.html, para crear la página.)
>
> 🖱️ I'm clicking the New File icon again and typing style.css, to create the style sheet.
>
> (Hago clic otra vez en el ícono New File y escribo style.css, para crear la hoja de estilos.)
>
> 🖱️ I'm clicking the New File icon once more and typing script.js, to create the JavaScript file.
>
> (Hago clic una vez más en el ícono New File y escribo script.js, para crear el archivo de JavaScript.)
>
> 🖱️ I'm pointing at the three files in the Explorer panel on the left, to show the structure of the project.
>
> (Señalo los tres archivos en el panel Explorer de la izquierda, para mostrar la estructura del proyecto.)

Explicás las reglas mientras señalás cada archivo con el mouse:

> 🟢 Let me explain the rules of the game. There are 16 cards face down, in a 4 by 4 grid. Each letter appears on exactly two cards, so there are eight pairs. The player turns over two cards per turn. If they match, they stay face up. If not, they turn back after a moment, and the player has to remember where they were.
>
> (Les explico las reglas del juego. Hay 16 cartas boca abajo, en una grilla de 4 por 4. Cada letra aparece en exactamente dos cartas, así que hay ocho pares. El jugador da vuelta dos cartas por turno. Si coinciden, quedan boca arriba. Si no, se dan vuelta después de un momento, y el jugador tiene que recordar dónde estaban.)
>
> 🟢 Each pair of cards counts as one attempt, and the game shows the number of attempts. When all eight pairs are found, a win message appears, and a Restart button shuffles the cards for a new game.
>
> (Cada par de cartas cuenta como un intento, y el juego muestra la cantidad de intentos. Cuando se encuentran los ocho pares, aparece un mensaje de victoria, y un botón Restart mezcla las cartas para una partida nueva.)
>
> 🖱️ I'm clicking script.js in the Explorer panel, to talk about the logic I'll write there.
>
> (Hago clic en script.js en el panel Explorer, para hablar de la lógica que voy a escribir ahí.)
>
> 🟢 The logic needs to remember a few things, which we call the state of the game: the first and second card of the current turn, whether the board is locked while two wrong cards turn back, the number of attempts, and the number of pairs found. Most bugs in this kind of game come from the state, so I'll keep it small and clear.
>
> (La lógica necesita recordar algunas cosas, que llamamos el estado del juego: la primera y la segunda carta del turno actual, si el tablero está bloqueado mientras dos cartas incorrectas se dan vuelta, la cantidad de intentos y la cantidad de pares encontrados. La mayoría de los errores en este tipo de juego vienen del estado, así que lo voy a mantener chico y claro.)

### Las técnicas, en la documentación

> 🖱️ I'm clicking the Firefox icon in the taskbar, and then the second tab at the top, to show the MDN page about CSS Grid.
>
> (Hago clic en el ícono de Firefox en la barra de tareas y después en la segunda pestaña de arriba, para mostrar la página de MDN sobre CSS Grid.)
>
> 🟢 MDN, the Mozilla Developer Network, is the reference documentation for web technologies. For the board, I'll use CSS Grid. It lets me define rows and columns, and the browser places the items in the cells automatically.
>
> (MDN, la Mozilla Developer Network, es la documentación de referencia de las tecnologías web. Para el tablero voy a usar CSS Grid. Me permite definir filas y columnas, y el navegador ubica los elementos en las celdas automáticamente.)
>
> 🖱️ I'm scrolling down the page with the mouse wheel, to show an example of a grid.
>
> (Bajo por la página con la rueda del mouse, para mostrar un ejemplo de grilla.)
>
> 🟢 With one line, grid-template-columns, I'll ask for four columns of the same width. Then I just add 16 cards, and they fill four rows by themselves. I don't need to calculate any positions.
>
> (Con una línea, grid-template-columns, voy a pedir cuatro columnas del mismo ancho. Después solo agrego 16 cartas, y llenan cuatro filas solas. No necesito calcular ninguna posición.)
>
> 🖱️ I'm clicking the third tab at the top, to show the MDN page about backface-visibility.
>
> (Hago clic en la tercera pestaña de arriba, para mostrar la página de MDN sobre backface-visibility.)
>
> 🟢 For the flip animation, each card will have two faces, a back and a front, on top of each other. I'll rotate the card 180 degrees around the vertical axis, like turning a real card. backface-visibility hidden hides the face that is turned away, so we only see one side at a time.
>
> (Para la animación de volteo, cada carta va a tener dos caras, un dorso y un frente, una encima de la otra. Voy a rotar la carta 180 grados sobre el eje vertical, como dar vuelta una carta real. backface-visibility hidden oculta la cara que queda de espaldas, así vemos un solo lado a la vez.)
>
> 🖱️ I'm scrolling down to the example on this page, to show how a hidden back face looks.
>
> (Bajo hasta el ejemplo de esta página, para mostrar cómo se ve una cara trasera oculta.)
>
> 🟢 The nice thing is that the animation is pure CSS. JavaScript will only add or remove a class called flipped, and CSS will do the rotation, with a transition of half a second.
>
> (Lo bueno es que la animación es CSS puro. JavaScript solo va a agregar o quitar una clase llamada flipped, y CSS va a hacer la rotación, con una transición de medio segundo.)
>
> 🖱️ I'm clicking the fourth tab at the top, to show the MDN page about setTimeout.
>
> (Hago clic en la cuarta pestaña de arriba, para mostrar la página de MDN sobre setTimeout.)
>
> 🟢 When two cards don't match, the player needs a moment to see them before they turn back. setTimeout runs a function after a delay in milliseconds. I'll use 800 milliseconds, and while we wait, the board will be locked so the player can't open a third card.
>
> (Cuando dos cartas no coinciden, el jugador necesita un momento para verlas antes de que se den vuelta. setTimeout ejecuta una función después de una demora en milisegundos. Voy a usar 800 milisegundos, y mientras esperamos, el tablero va a estar bloqueado para que el jugador no pueda abrir una tercera carta.)
>
> 🖱️ I'm clicking the fifth tab at the top, to show the Wikipedia page about the Fisher-Yates shuffle.
>
> (Hago clic en la quinta pestaña de arriba, para mostrar la página de Wikipedia sobre la mezcla de Fisher-Yates.)
>
> 🟢 To shuffle the cards, I'll use the Fisher-Yates algorithm. It goes from the last card to the first, and swaps each one with a random card before it. It's short, fast, and gives every possible order the same chance. A common shortcut, sorting with a random number, looks simpler but doesn't shuffle fairly.
>
> (Para mezclar las cartas voy a usar el algoritmo de Fisher-Yates. Va de la última carta a la primera y cambia cada una por una carta al azar anterior. Es corto, rápido y le da a cada orden posible la misma probabilidad. Un atajo común, ordenar con un número aleatorio, parece más simple, pero no mezcla de forma justa.)
>
> 🖱️ I'm scrolling down the page to the steps of the algorithm, to show how it works.
>
> (Bajo por la página hasta los pasos del algoritmo, para mostrar cómo funciona.)
>
> 🟢 So the plan is: first the HTML structure, then the CSS for the grid and the flip, and then the JavaScript in two parts: creating and shuffling the cards, and then the game rules. I'll test in Firefox after each file.
>
> (Entonces el plan es: primero la estructura HTML, después el CSS para la grilla y el volteo, y después el JavaScript en dos partes: crear y mezclar las cartas, y después las reglas del juego. Voy a probar en Firefox después de cada archivo.)

---

## 7:00–10:30 — index.html: la estructura

En cada bloque de código: **primero** decís qué hace el bloque completo (🟢 **What this block does**) y **después** explicás cada línea mientras la escribís (**What each line does**).

> 🖱️ I'm clicking the VS Code icon in the taskbar, and then index.html in the Explorer panel on the left, to start with the structure.
>
> (Hago clic en el ícono de VS Code en la barra de tareas y después en index.html, en el panel Explorer de la izquierda, para empezar por la estructura.)

### Bloque 1 — El esqueleto de la página

> 🟢 **What this block does:** every HTML page needs the same basic skeleton, so I'll let VS Code write it for me, and then give the page its name.
>
> (**Qué hace este bloque:** toda página HTML necesita el mismo esqueleto básico, así que voy a dejar que VS Code lo escriba por mí, y después le pongo nombre a la página.)
>
> 🖱️ I'm typing an exclamation mark in the empty editor and pressing Enter, to let VS Code's Emmet shortcut create the basic HTML structure.
>
> (Escribo un signo de exclamación en el editor vacío y presiono Enter, para que el atajo Emmet de VS Code cree la estructura básica del HTML.)
>
> 🖱️ I'm double-clicking the word Document inside the title tag, near the top of the file, and typing Memory Card Game.
>
> (Hago doble clic en la palabra Document adentro de la etiqueta title, cerca del principio del archivo, y escribo Memory Card Game.)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Memory Card Game</title>
</head>
<body>
</body>
</html>
```

**What each line does** (señalá cada línea con el mouse):

- 🟢 `<!DOCTYPE html>`: it tells the browser this is a modern HTML5 page.
- 🟢 `<html lang="en">`: the root of the page. lang says the content is in English, which helps screen readers.
- 🟢 `<head>`: information about the page that isn't shown in the page itself.
- 🟢 `<meta charset="UTF-8">`: the character encoding, so any letter or symbol displays correctly.
- 🟢 `<meta name="viewport" ...>`: it makes the page fit the width of phone screens.
- 🟢 `<title>Memory Card Game</title>`: the name in the browser tab.
- 🟢 `<body>`: everything visible goes inside the body.

### Bloque 2 — Conectar la hoja de estilos

> 🟢 **What this block does:** it connects this page to style.css, so the browser applies the design.
>
> (**Qué hace este bloque:** conecta esta página con style.css, para que el navegador aplique el diseño.)
>
> 🖱️ I'm clicking at the end of the title line, inside the head tag, and pressing Enter, to add the link.
>
> (Hago clic al final de la línea del title, adentro de la etiqueta head, y presiono Enter, para agregar el vínculo.)

```html
  <link rel="stylesheet" href="style.css">
```

**What each line does:**

- 🟢 `<link rel="stylesheet" href="style.css">`: rel says the file is a style sheet, and href is the file name. It goes in the head, so the styles load before the page is shown.

### Bloque 3 — El contenido visible

> 🟢 **What this block does:** it creates everything the player sees: the title, the attempts counter, an empty board for the cards, a place for the win message, and the restart button. At the end, it loads the JavaScript file.
>
> (**Qué hace este bloque:** crea todo lo que ve el jugador: el título, el contador de intentos, un tablero vacío para las cartas, un lugar para el mensaje de victoria y el botón de reinicio. Al final, carga el archivo de JavaScript.)
>
> 🖱️ I'm clicking inside the body tag, in the middle of the file, to write the page content.
>
> (Hago clic adentro de la etiqueta body, en el medio del archivo, para escribir el contenido de la página.)

```html
  <h1>Memory Card Game</h1>
  <p>Attempts: <span id="attempts">0</span></p>
  <div class="grid" id="grid"></div>
  <p id="message"></p>
  <button id="restart">Restart</button>
  <script src="script.js"></script>
```

**What each line does:**

- 🟢 `<h1>Memory Card Game</h1>`: the main title of the page.
- 🟢 `<p>Attempts: <span id="attempts">0</span></p>`: the attempts counter. The number is inside a span with an id, so JavaScript can find it and update it.
- 🟢 `<div class="grid" id="grid"></div>`: an empty container for the 16 cards. JavaScript will create the cards inside it, in a random order.
- 🟢 `<p id="message"></p>`: an empty paragraph for the win message.
- 🟢 `<button id="restart">Restart</button>`: the button to start a new game.
- 🟢 `<script src="script.js"></script>`: this loads the JavaScript file. I put it at the end of the body, so the board and the buttons already exist when the script runs.

### Probar index.html

> 🖱️ I'm pressing Control and S to save the file.
>
> (Presiono Control y S para guardar el archivo.)
>
> 🖱️ I'm clicking the Firefox icon in the taskbar at the bottom, and pressing Control and O, to open the file dialog.
>
> (Hago clic en el ícono de Firefox en la barra de tareas, abajo, y presiono Control y O, para abrir el cuadro de abrir archivo.)
>
> 🖱️ I'm choosing index.html in the memory-game folder on the Desktop, and clicking the Open button at the bottom right, to see the page in Firefox.
>
> (Elijo index.html en la carpeta memory-game del Escritorio y hago clic en el botón Open, abajo a la derecha, para ver la página en Firefox.)
>
> 🟢 The title, the counter, and the button are there, with no style yet, because style.css is still empty. The board is empty too, because the cards come from JavaScript.
>
> (Están el título, el contador y el botón, todavía sin estilo, porque style.css sigue vacío. El tablero también está vacío, porque las cartas las crea JavaScript.)

---

## 10:30–14:30 — style.css: la grilla y la animación de volteo

> 🖱️ I'm clicking the VS Code icon in the taskbar, and then style.css in the Explorer panel on the left, to write the styles.
>
> (Hago clic en el ícono de VS Code en la barra de tareas y después en style.css, en el panel Explorer de la izquierda, para escribir los estilos.)

### Bloque 4 — La página y el tablero

> 🟢 **What this block does:** it centers the page and builds the 4 by 4 board with CSS Grid.
>
> (**Qué hace este bloque:** centra la página y arma el tablero de 4 por 4 con CSS Grid.)

```css
body { font-family: Arial; text-align: center; }
.grid { display: grid; grid-template-columns: repeat(4, 80px); gap: 10px; justify-content: center; }
```

**What each line does:**

- 🟢 `body { font-family: Arial; text-align: center; }`: a simple font, and all the text centered.
- 🟢 `.grid { ... }`: display grid turns the board into a grid. grid-template-columns repeat 4, 80 pixels makes four columns of 80 pixels, so each card is 80 pixels wide. gap leaves 10 pixels between cards, and justify-content center puts the board in the middle of the page. Sixteen cards will fill four rows automatically.

### Bloque 5 — La carta y su giro

> 🟢 **What this block does:** it defines the height of each card and the 3D flip animation. The card has an inner part that rotates when the card gets the class flipped.
>
> (**Qué hace este bloque:** define la altura de cada carta y la animación de volteo en 3D. La carta tiene una parte interna que gira cuando la carta recibe la clase flipped.)

```css
.card { height: 80px; perspective: 600px; cursor: pointer; }
.inner { position: relative; height: 100%; transition: transform 0.5s; transform-style: preserve-3d; }
.flipped .inner { transform: rotateY(180deg); }
```

**What each line does:**

- 🟢 `.card { height: 80px; perspective: 600px; cursor: pointer; }`: each card is 80 pixels high, so with the grid column it's a square. perspective gives depth to the rotation, so it looks 3D, and cursor pointer shows a hand over the card.
- 🟢 `.inner { ... }`: the inner part fills the card and is what actually rotates. transition makes the rotation last half a second, and preserve-3d keeps its two faces in 3D space.
- 🟢 `.flipped .inner { transform: rotateY(180deg); }`: when the card has the class flipped, the inner part turns 180 degrees around the vertical axis. That's the flip.

### Bloque 6 — Las dos caras

> 🟢 **What this block does:** it styles the two faces of each card: the blue back, and the white front with the letter, which starts hidden. It also colors the found pairs in green.
>
> (**Qué hace este bloque:** les da estilo a las dos caras de cada carta: el dorso azul y el frente blanco con la letra, que empieza oculto. También pinta de verde los pares encontrados.)

```css
.front, .back { position: absolute; inset: 0; backface-visibility: hidden; display: flex; align-items: center; justify-content: center; font-size: 36px; }
.back { background: steelblue; }
.front { background: white; border: 2px solid steelblue; transform: rotateY(180deg); }
.matched .front { background: lightgreen; }
```

**What each line does:**

- 🟢 `.front, .back { ... }`: both faces sit on top of each other and fill the card: position absolute and inset zero do that. backface-visibility hidden hides each face when it's turned away. The flex properties center the letter, and font-size makes it big.
- 🟢 `.back { background: steelblue; }`: the back of the card is blue.
- 🟢 `.front { background: white; border: 2px solid steelblue; transform: rotateY(180deg); }`: the front is white with a blue border, and it starts already turned around, so it's hidden until the card flips.
- 🟢 `.matched .front { background: lightgreen; }`: when a pair is found, its front turns green.

### Probar style.css

> 🖱️ I'm pressing Control and S to save, clicking the Firefox icon in the taskbar, and clicking the Reload button to the left of the address bar, to see the styles.
>
> (Presiono Control y S para guardar, hago clic en el ícono de Firefox en la barra de tareas y hago clic en el botón Reload a la izquierda de la barra de direcciones, para ver los estilos.)
>
> 🟢 The text is centered and uses the new font now, so the link to style.css works. The cards will appear when we add the JavaScript.
>
> (Ahora el texto está centrado y usa la nueva fuente, así que el vínculo con style.css funciona. Las cartas van a aparecer cuando agreguemos el JavaScript.)

---

## 14:30–18:30 — script.js, parte 1: el estado, la mezcla y las cartas

> 🖱️ I'm clicking the VS Code icon in the taskbar, and then script.js in the Explorer panel on the left, to write the game logic.
>
> (Hago clic en el ícono de VS Code en la barra de tareas y después en script.js, en el panel Explorer de la izquierda, para escribir la lógica del juego.)

### Bloque 7 — Los datos y el estado del juego

> 🟢 **What this block does:** it defines the eight letters of the game, finds the page elements that the code will change, and creates the variables that remember the state of the game.
>
> (**Qué hace este bloque:** define las ocho letras del juego, busca los elementos de la página que el código va a cambiar y crea las variables que recuerdan el estado del juego.)

```javascript
const symbols = ["A", "B", "C", "D", "E", "F", "G", "H"];
const grid = document.getElementById("grid");
const attemptsText = document.getElementById("attempts");
const message = document.getElementById("message");
let firstCard = null;
let secondCard = null;
let lockBoard = false;
let attempts = 0;
let matches = 0;
let flipBackTimer = null;
```

**What each line does:**

- 🟢 `const symbols = ["A", ... "H"];`: the eight letters. Each one will appear on two cards, so we get eight pairs. const means this value won't change.
- 🟢 `const grid = document.getElementById("grid");`: it finds the empty board in index.html by its id.
- 🟢 `const attemptsText = document.getElementById("attempts");`: it finds the number of attempts on the page.
- 🟢 `const message = document.getElementById("message");`: it finds the paragraph for the win message.
- 🟢 `let firstCard = null;`: the first card turned over in this turn. let means the value will change. null means there's no card yet.
- 🟢 `let secondCard = null;`: the second card of the turn.
- 🟢 `let lockBoard = false;`: when it's true, the board ignores clicks, while two wrong cards are turning back.
- 🟢 `let attempts = 0;`: how many attempts the player has made.
- 🟢 `let matches = 0;`: how many pairs the player has found.
- 🟢 `let flipBackTimer = null;`: it remembers the timer that turns wrong cards back, so Restart can cancel it.

### Bloque 8 — Mezclar las cartas

> 🟢 **What this block does:** it shuffles a list with the Fisher-Yates algorithm, the one we saw on Wikipedia, so every game has the cards in a different random order.
>
> (**Qué hace este bloque:** mezcla una lista con el algoritmo de Fisher-Yates, el que vimos en Wikipedia, para que cada partida tenga las cartas en un orden aleatorio distinto.)

```javascript
function shuffle(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
}
```

**What each line does:**

- 🟢 `function shuffle(array) {`: a function that receives a list and returns it shuffled.
- 🟢 `for (let i = array.length - 1; i > 0; i--) {`: the loop goes from the last position down to the second one.
- 🟢 `const j = Math.floor(Math.random() * (i + 1));`: it picks a random position j, from zero up to i.
- 🟢 `[array[i], array[j]] = [array[j], array[i]];`: it swaps the two cards in one line.
- 🟢 `return array;`: it returns the shuffled list.

### Bloque 9 — Empezar una partida

> 🟢 **What this block does:** it prepares a new game. It clears the board and the counters, and then creates the 16 cards in a random order, each one ready to react to a click.
>
> (**Qué hace este bloque:** prepara una partida nueva. Limpia el tablero y los contadores, y después crea las 16 cartas en un orden aleatorio, cada una lista para reaccionar a un clic.)

```javascript
function startGame() {
  clearTimeout(flipBackTimer);
  grid.innerHTML = "";
  resetTurn();
  attempts = 0;
  matches = 0;
  attemptsText.textContent = attempts;
  message.textContent = "";
  shuffle([...symbols, ...symbols]).forEach(symbol => {
    const card = document.createElement("div");
    card.className = "card";
    card.dataset.symbol = symbol;
    card.innerHTML = `<div class="inner"><div class="back"></div><div class="front">${symbol}</div></div>`;
    card.addEventListener("click", () => flipCard(card));
    grid.appendChild(card);
  });
}
```

**What each line does:**

- 🟢 `function startGame() {`: the function that starts a new game.
- 🟢 `clearTimeout(flipBackTimer);`: it cancels a pending flip-back, in case the player restarts in the middle of one.
- 🟢 `grid.innerHTML = "";`: it removes all the old cards from the board.
- 🟢 `resetTurn();`: it clears the current turn. I'll write this function in the next part.
- 🟢 `attempts = 0; matches = 0;`: both counters go back to zero.
- 🟢 `attemptsText.textContent = attempts;`: the page shows zero attempts.
- 🟢 `message.textContent = "";`: it removes the win message.
- 🟢 `shuffle([...symbols, ...symbols]).forEach(symbol => {`: the three dots copy the letters twice into one list of 16. shuffle mixes it, and forEach creates one card for each letter.
- 🟢 `const card = document.createElement("div");`: it creates a new, empty div.
- 🟢 `card.className = "card";`: it gives it the class card, so it gets the size and the 3D style from style.css.
- 🟢 `card.dataset.symbol = symbol;`: it saves the letter inside the card, to compare two cards later.
- 🟢 `` card.innerHTML = `<div class="inner">...</div>`; ``: inside the card, it puts the inner part with the back and the front, and the front shows the letter.
- 🟢 `card.addEventListener("click", () => flipCard(card));`: when the player clicks the card, it calls flipCard.
- 🟢 `grid.appendChild(card);`: it adds the card to the board.

> 🖱️ I'm pressing Control and S to save. I won't test yet, because startGame needs the functions from the next part.
>
> (Presiono Control y S para guardar. Todavía no lo pruebo, porque startGame necesita las funciones de la parte siguiente.)

---

## 18:30–22:30 — script.js, parte 2: las reglas del juego

> 🖱️ I'm clicking at the end of script.js, below the startGame function, to add the game rules.
>
> (Hago clic al final de script.js, debajo de la función startGame, para agregar las reglas del juego.)

### Bloque 10 — Dar vuelta una carta

> 🟢 **What this block does:** it runs every time the player clicks a card. It ignores the clicks that aren't allowed, turns the card over, and when two cards are open, counts the attempt and compares them.
>
> (**Qué hace este bloque:** se ejecuta cada vez que el jugador hace clic en una carta. Ignora los clics que no están permitidos, da vuelta la carta y, cuando hay dos cartas abiertas, cuenta el intento y las compara.)

```javascript
function flipCard(card) {
  if (lockBoard || card === firstCard || card.classList.contains("matched")) return;
  card.classList.add("flipped");
  if (!firstCard) {
    firstCard = card;
    return;
  }
  secondCard = card;
  attempts++;
  attemptsText.textContent = attempts;
  checkMatch();
}
```

**What each line does:**

- 🟢 `function flipCard(card) {`: it receives the card that was clicked.
- 🟢 `if (lockBoard || card === firstCard || card.classList.contains("matched")) return;`: it ignores the click in three cases: the board is locked, the player clicked the same card twice, or the card is already part of a found pair. The two vertical bars mean "or", and return stops the function.
- 🟢 `card.classList.add("flipped");`: it adds the class flipped, and the CSS turns the card over.
- 🟢 `if (!firstCard) {`: if there's no first card yet in this turn...
- 🟢 `firstCard = card; return;`: ...this card becomes the first one, and we wait for the second.
- 🟢 `secondCard = card;`: otherwise, this is the second card.
- 🟢 `attempts++;`: two cards make one attempt, so the counter goes up by one.
- 🟢 `attemptsText.textContent = attempts;`: the new number appears on the page.
- 🟢 `checkMatch();`: it compares the two cards.

### Bloque 11 — Comparar las dos cartas

> 🟢 **What this block does:** it decides what happens with the two open cards. If the letters match, they stay face up in green, and if that was the last pair, the player wins. If not, the board locks and the cards turn back after a short pause.
>
> (**Qué hace este bloque:** decide qué pasa con las dos cartas abiertas. Si las letras coinciden, quedan boca arriba en verde, y si era el último par, el jugador gana. Si no, el tablero se bloquea y las cartas se dan vuelta después de una pausa corta.)

```javascript
function checkMatch() {
  if (firstCard.dataset.symbol === secondCard.dataset.symbol) {
    firstCard.classList.add("matched");
    secondCard.classList.add("matched");
    matches++;
    resetTurn();
    if (matches === symbols.length) {
      message.textContent = `You won in ${attempts} attempts!`;
    }
  } else {
    lockBoard = true;
    flipBackTimer = setTimeout(() => {
      firstCard.classList.remove("flipped");
      secondCard.classList.remove("flipped");
      resetTurn();
    }, 800);
  }
}
```

**What each line does:**

- 🟢 `if (firstCard.dataset.symbol === secondCard.dataset.symbol) {`: if both cards have the same letter, it's a match. Three equal signs compare the values exactly.
- 🟢 `firstCard.classList.add("matched"); secondCard.classList.add("matched");`: both cards get the class matched: they stay face up, turn green, and can't be clicked again.
- 🟢 `matches++;`: one more pair found.
- 🟢 `resetTurn();`: a new turn starts.
- 🟢 `if (matches === symbols.length) {`: if the pairs found are eight, the same as the number of letters, the game is over.
- 🟢 `` message.textContent = `You won in ${attempts} attempts!`; ``: the win message, with the number of attempts inside the text.
- 🟢 `} else {`: if the letters are different...
- 🟢 `lockBoard = true;`: ...the board locks, so the player can't open a third card.
- 🟢 `flipBackTimer = setTimeout(() => {`: setTimeout waits before running the code inside, and I save the timer so Restart can cancel it.
- 🟢 `firstCard.classList.remove("flipped"); secondCard.classList.remove("flipped");`: both cards turn back face down.
- 🟢 `resetTurn();`: a new turn starts, and the board unlocks.
- 🟢 `}, 800);`: the wait is 800 milliseconds, enough to see the cards.

### Bloque 12 — Terminar el turno y arrancar el juego

> 🟢 **What this block does:** it has a small helper that clears the current turn, connects the Restart button, and starts the first game when the page loads.
>
> (**Qué hace este bloque:** tiene una función chica que limpia el turno actual, conecta el botón Restart y empieza la primera partida cuando se carga la página.)

```javascript
function resetTurn() {
  firstCard = null;
  secondCard = null;
  lockBoard = false;
}

document.getElementById("restart").addEventListener("click", startGame);
startGame();
```

**What each line does:**

- 🟢 `function resetTurn() {`: the helper that ends a turn.
- 🟢 `firstCard = null; secondCard = null;`: it forgets the two cards of the turn.
- 🟢 `lockBoard = false;`: it unlocks the board.
- 🟢 `document.getElementById("restart").addEventListener("click", startGame);`: when the player clicks Restart, it calls startGame.
- 🟢 `startGame();`: this starts the first game as soon as the page loads.

---

## 22:30–27:00 — Probar el juego en Firefox

> 🖱️ I'm pressing Control and S to save, clicking the Firefox icon in the taskbar, and clicking the Reload button to the left of the address bar, to load the game.
>
> (Presiono Control y S para guardar, hago clic en el ícono de Firefox en la barra de tareas y hago clic en el botón Reload a la izquierda de la barra de direcciones, para cargar el juego.)
>
> 🟢 Now we have 16 blue cards in a 4 by 4 grid, so the three files are working together.
>
> (Ahora tenemos 16 cartas azules en una grilla de 4 por 4, así que los tres archivos funcionan juntos.)

Probás cada requisito, narrando cada clic:

> 🖱️ I'm clicking the first card at the top left of the grid, to test the flip animation.
>
> (Hago clic en la primera carta, arriba a la izquierda de la grilla, para probar la animación de volteo.)
>
> 🟢 The card turns over in 3D and shows its letter.
>
> (La carta se da vuelta en 3D y muestra su letra.)
>
> 🖱️ I'm clicking the same card again, to check that clicking a card twice doesn't count as a pair.
>
> (Hago clic otra vez en la misma carta, para comprobar que hacer clic dos veces en una carta no cuenta como pareja.)
>
> 🖱️ I'm clicking a second card in the grid, to test what happens with two different cards.
>
> (Hago clic en una segunda carta de la grilla, para probar qué pasa con dos cartas distintas.)
>
> 🟢 They're different, so after a moment both turn back, and the attempts counter at the top shows 1.
>
> (Son distintas, así que después de un momento las dos se dan vuelta, y el contador de intentos de arriba muestra 1.)

Cuando encontrás un par:

> 🖱️ I'm clicking the card with the matching letter, to complete a pair.
>
> (Hago clic en la carta con la letra que coincide, para completar un par.)
>
> 🟢 It's a match: both cards stay face up and turn green.
>
> (Es una pareja: las dos cartas quedan boca arriba y se ponen verdes.)
>
> 🖱️ I'm clicking one of the green cards, to check that matched pairs stay locked.
>
> (Hago clic en una de las cartas verdes, para comprobar que las parejas encontradas quedan bloqueadas.)
>
> 🟢 Nothing happens, so matched pairs can't be turned back.
>
> (No pasa nada, así que las parejas encontradas no se pueden dar vuelta.)
>
> 🖱️ I'm quickly clicking a third card while two wrong cards are still turning, to check that the board is locked.
>
> (Hago clic rápido en una tercera carta mientras dos cartas incorrectas todavía se están dando vuelta, para comprobar que el tablero está bloqueado.)
>
> 🟢 The third card doesn't flip, so the player can only have two cards open at a time.
>
> (La tercera carta no se da vuelta, así que el jugador solo puede tener dos cartas abiertas a la vez.)

Seguís jugando hasta ganar, narrando los pares que encontrás ("I'm clicking the card in the second row, third column, to find the pair for B"):

> 🟢 That's the last pair. The message says I won, with the number of attempts.
>
> (Ese es el último par. El mensaje dice que gané, con la cantidad de intentos.)
>
> 🖱️ I'm clicking the Restart button below the grid, to start a new game.
>
> (Hago clic en el botón Restart, debajo de la grilla, para empezar una partida nueva.)
>
> 🟢 All cards are face down again, the counter is back to zero, the message is gone, and the cards are in a new random order.
>
> (Todas las cartas están boca abajo otra vez, el contador volvió a cero, el mensaje desapareció y las cartas están en un orden aleatorio nuevo.)
>
> 🖱️ I'm clicking two cards to show that the letters are in different positions than before.
>
> (Hago clic en dos cartas para mostrar que las letras están en posiciones distintas que antes.)

---

## 27:00–30:30 — Epílogo (3–4 minutos)

Revisá en las reglas de Odin qué tiene que tener el epílogo y ajustá este texto si piden algo distinto.

> 🖱️ I'm clicking the VS Code icon in the taskbar, and clicking each file in the Explorer panel on the left, index.html, style.css, and script.js, to go over the code.
>
> (Hago clic en el ícono de VS Code en la barra de tareas y hago clic en cada archivo del panel Explorer de la izquierda, index.html, style.css y script.js, para repasar el código.)
>
> 🟢 In this epilogue, I want to go over my approach. I split the game into three files, one for each job: index.html for the structure, style.css for the look, and script.js for the behavior. The HTML only needs two lines to connect them: the link in the head and the script tag at the end of the body.
>
> (En este epílogo quiero repasar mi enfoque. Dividí el juego en tres archivos, uno para cada tarea: index.html para la estructura, style.css para el aspecto y script.js para el comportamiento. El HTML solo necesita dos líneas para conectarlos: el link en el head y la etiqueta script al final del body.)
>
> 🟢 The flip animation is pure CSS. JavaScript only adds or removes the flipped class, and CSS does the 3D rotation. That keeps the logic simple and the animation smooth.
>
> (La animación de volteo es CSS puro. JavaScript solo agrega o quita la clase flipped, y CSS hace la rotación en 3D. Eso mantiene la lógica simple y la animación fluida.)
>
> 🟢 The hardest part of a memory game is the state: which cards are open, and when the player is allowed to click. The lockBoard flag and the checks at the start of flipCard prevent the common bugs: opening three cards at once, matching a card with itself, or turning back a found pair. I tested each of those cases in Firefox.
>
> (Lo más difícil de un juego de memoria es el estado: qué cartas están abiertas y cuándo puede hacer clic el jugador. La variable lockBoard y los chequeos al principio de flipCard evitan los errores comunes: abrir tres cartas a la vez, emparejar una carta consigo misma o dar vuelta un par ya encontrado. Probé cada uno de esos casos en Firefox.)
>
> 🟢 I used the Fisher-Yates shuffle because simpler tricks, like sorting with a random number, don't give every order the same chance.
>
> (Usé la mezcla de Fisher-Yates porque los trucos más simples, como ordenar con un número aleatorio, no le dan la misma probabilidad a todos los órdenes.)
>
> 🟢 As next steps, I could replace the letters with emojis or images, add a timer and a best score saved in the browser, and add levels with bigger grids. Thanks for watching!
>
> (Como próximos pasos, podría reemplazar las letras por emojis o imágenes, agregar un cronómetro y un mejor puntaje guardado en el navegador, y sumar niveles con grillas más grandes. ¡Gracias por mirar!)

Si el reloj todavía no pasó los 15:00, no cortes: jugá otra partida completa explicando cada jugada.

---

## Después de grabar

1. Ejecutá **Run full AutoQC**, no solo *Rerun failing*.
2. Subí los **cuatro archivos por separado**: el **MP4**, el **ZIP original de TaskRecorder**, **Deliverables.zip** (con `index.html`, `style.css` y `script.js`) y **Metadata.rtf**.
