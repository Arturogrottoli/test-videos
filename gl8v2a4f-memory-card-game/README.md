# gl8v2a4f — Memory Card Game

Guion paso a paso para grabar la tarea **gl8v2a4f**: un juego de memoria hecho desde cero en un único `index.html`, con **HTML**, **CSS** y **JavaScript** puro, en **Visual Studio Code**, y probado en **Firefox**. El juego tiene una grilla de 4×4 con 8 pares, una animación de volteo en 3D y un contador de intentos. Además, las parejas encontradas quedan fijas, aparece un mensaje al ganar y hay un botón para reiniciar. La grabación tiene que durar **entre 15:00 y 50:59**. Este guion apunta a unos **25 minutos**, epílogo incluido.

**Cómo leer este guion:**

- Las frases que empiezan con 🖱️ las decís **en el momento de hacer clic, desplazarte o escribir**. Siempre dicen **qué** elemento usás, **dónde** está en la pantalla y **por qué** lo usás. Son las que revisa AutoQC.
- Las frases que empiezan con 🟢 son la explicación que **decís en inglés** entre una acción y otra.
- Debajo de cada bloque de código, la lista **What each line does** explica cada línea (o cada grupo de líneas parecidas) en inglés. La leés en voz alta mientras escribís.
- El resto, en castellano, es lo que hacés en pantalla. Las traducciones aparecen entre paréntesis después de cada frase.

> **Importante:** el Goal de Studio tiene prioridad sobre este guion. Antes de grabar, revisá el apartado **Starting materials**. Según las notas, la tarea arranca desde cero.

---

## Archivos de la carpeta

```
gl8v2a4f-memory-card-game/
├── README.md
└── solution/
    └── index.html   ← el juego terminado, para probarlo y practicar (NO lo abras durante la grabación)
```

**Sobre el porcentaje de escritura.** Este es el guion con más código para escribir: unas 100 líneas. Para no pasar del ~30% de escritura:

- Usá el atajo **Emmet** de VS Code: escribís `!` y presionás `Enter`, y VS Code crea solo la estructura básica del HTML.
- Escribí por partes y **probá en Firefox después de cada parte**. Probar es todo mouse y baja el porcentaje.
- Jugá una partida completa en la prueba final: son varios minutos de clics.
- No apures la explicación: el guion apunta a 25 minutos para que la escritura sea una parte menor del video.

En el juego las cartas usan **letras de la A a la H**, porque escribir emojis en VS Code es lento. Si querés, en el epílogo mencionás que se pueden cambiar por emojis o imágenes.

---

## Antes de grabar

1. Leé el Goal y compará este guion con el campo **Describe your idea** de Studio.
2. Abrí `solution/index.html` en Firefox y jugá una partida, para conocer el comportamiento.
3. Creá una carpeta vacía `Escritorio\memory-game`.
4. Practicá una vez entera, leyendo en voz alta las frases 🖱️ y 🟢, y cronometrá. Después vaciá la carpeta `memory-game`.
5. Dejá abiertos el documento **Goal** en Firefox y VS Code (sin ninguna carpeta abierta). Agrandá la letra de VS Code (`Ctrl + +`).
6. Mostrá una sola ventana a la vez, maximizada, y pasá de una a otra con la barra de tareas. Cerrá o minimizá todo lo demás, para que ninguna ventana tape a otra.
7. Pausa de ~1 segundo después de cada clic y nunca más de 45 segundos en silencio.
8. No muestres Studio, Mercor, información privada ni herramientas de IA, ni la carpeta `solution`. Cerrá este guion si está en la misma pantalla.

---

## 0:00–0:45 — Mostrar el Goal

> 🖱️ I'm on the Goal document in Firefox, to show what this task asks for.
>
> (Estoy en el documento del Goal, en Firefox, para mostrar qué pide esta tarea.)
>
> 🟢 As a front-end developer, I'll build a memory card game from scratch in a single HTML file, with HTML, CSS, and plain JavaScript. It will have a 4 by 4 grid with eight pairs, a flip animation, an attempts counter, a win message, and a restart button.
>
> (Como desarrollador front-end, voy a crear desde cero un juego de memoria en un solo archivo HTML, con HTML, CSS y JavaScript puro. Va a tener una grilla de 4 por 4 con ocho pares, una animación de volteo, un contador de intentos, un mensaje de victoria y un botón para reiniciar.)

---

## 0:45–5:30 — Crear el archivo y la estructura HTML

> 🖱️ I'm clicking the VS Code icon in the taskbar at the bottom of the screen, to open the code editor.
>
> (Hago clic en el ícono de VS Code en la barra de tareas, abajo de la pantalla, para abrir el editor de código.)
>
> 🖱️ I'm opening the File menu at the top left and choosing Open Folder, selecting the memory-game folder on the Desktop, and clicking Select Folder at the bottom right.
>
> (Abro el menú File, arriba a la izquierda, elijo Open Folder, selecciono la carpeta memory-game del Escritorio y hago clic en Select Folder, abajo a la derecha.)

Si VS Code pregunta si confiás en los autores: *"I'm clicking Yes, I trust the authors, in the center of the dialog, because this is my own folder."*

> 🖱️ I'm clicking the New File icon next to the folder name, at the top of the Explorer panel on the left, and typing index.html, to create the game file.
>
> (Hago clic en el ícono New File al lado del nombre de la carpeta, arriba del panel Explorer de la izquierda, y escribo index.html, para crear el archivo del juego.)
>
> 🟢 The whole game will live in this one file. HTML gives the structure, CSS the look and the animation, and JavaScript the game logic.
>
> (Todo el juego va a estar en este único archivo. HTML da la estructura, CSS el aspecto y la animación, y JavaScript la lógica del juego.)
>
> 🖱️ I'm typing an exclamation mark in the empty editor and pressing Enter, to let VS Code's Emmet shortcut create the basic HTML structure.
>
> (Escribo un signo de exclamación en el editor vacío y presiono Enter, para que el atajo Emmet de VS Code cree la estructura básica del HTML.)
>
> 🟢 Emmet wrote the standard skeleton for me: the doctype, the html, head, and body tags, the character set, and the viewport for mobile screens.
>
> (Emmet me escribió el esqueleto estándar: el doctype, las etiquetas html, head y body, el juego de caracteres y el viewport para pantallas de celular.)
>
> 🖱️ I'm double-clicking the word Document inside the title tag, near the top of the file, and typing Memory Card Game, to name the browser tab.
>
> (Hago doble clic en la palabra Document adentro de la etiqueta title, cerca del principio del archivo, y escribo Memory Card Game, para ponerle nombre a la pestaña del navegador.)
>
> 🖱️ I'm clicking inside the body tag, in the middle of the file, to write the page structure.
>
> (Hago clic adentro de la etiqueta body, en el medio del archivo, para escribir la estructura de la página.)

Escribís dentro de `<body>`:

```html
  <h1>Memory Card Game</h1>
  <p>Attempts: <span id="attempts">0</span></p>
  <div class="grid" id="grid"></div>
  <p id="message"></p>
  <button id="restart">Restart</button>
```

**What each line does:**

- 🟢 `<h1>Memory Card Game</h1>`: the main title of the page.
- 🟢 `<p>Attempts: <span id="attempts">0</span></p>`: the attempts counter. The number is inside a span with an id, so JavaScript can find it and update it.
- 🟢 `<div class="grid" id="grid"></div>`: an empty container for the 16 cards. JavaScript will create the cards inside it, in a random order.
- 🟢 `<p id="message"></p>`: an empty paragraph for the win message.
- 🟢 `<button id="restart">Restart</button>`: the button to start a new game.

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
> 🟢 The title, the counter, and the button are there. The grid is still empty, because the cards come from JavaScript.
>
> (Están el título, el contador y el botón. La grilla todavía está vacía, porque las cartas las crea JavaScript.)

---

## 5:30–10:00 — CSS: la grilla y la animación de volteo

> 🖱️ I'm clicking the VS Code icon in the taskbar, and clicking at the end of the title line, inside the head tag near the top, to add the styles.
>
> (Hago clic en el ícono de VS Code en la barra de tareas, y hago clic al final de la línea del title, adentro de la etiqueta head cerca del principio, para agregar los estilos.)

Escribís debajo de `<title>`:

```html
  <style>
    body { font-family: Arial, sans-serif; text-align: center; background: #1e293b; color: white; }
    .grid { display: grid; grid-template-columns: repeat(4, 90px); gap: 12px; justify-content: center; margin: 20px; }
    .card { width: 90px; height: 90px; perspective: 600px; cursor: pointer; }
    .inner { position: relative; width: 100%; height: 100%; transition: transform 0.5s; transform-style: preserve-3d; }
    .card.flipped .inner { transform: rotateY(180deg); }
    .front, .back { position: absolute; inset: 0; border-radius: 10px; backface-visibility: hidden;
      display: flex; align-items: center; justify-content: center; font-size: 40px; font-weight: bold; }
    .back { background: #3b82f6; }
    .front { background: white; color: #1e293b; transform: rotateY(180deg); }
    .card.matched .front { background: #86efac; }
    button { padding: 10px 20px; font-size: 16px; cursor: pointer; }
  </style>
```

**What each line does:**

- 🟢 `body { ... }`: a dark background, white text, and everything centered.
- 🟢 `.grid { display: grid; grid-template-columns: repeat(4, 90px); gap: 12px; ... }`: CSS Grid makes the 4 by 4 board: four columns of 90 pixels, with 12 pixels between cards. Sixteen cards fill four rows automatically.
- 🟢 `.card { ... perspective: 600px; cursor: pointer; }`: each card is a 90-pixel square. Perspective gives depth to the 3D flip, and the cursor turns into a hand.
- 🟢 `.inner { ... transition: transform 0.5s; transform-style: preserve-3d; }`: the inner part is what actually rotates. The transition makes the rotation take half a second, and preserve-3d keeps the two faces in 3D space.
- 🟢 `.card.flipped .inner { transform: rotateY(180deg); }`: when a card has the class flipped, its inner part turns 180 degrees around the vertical axis. That's the flip animation.
- 🟢 `.front, .back { position: absolute; inset: 0; ... backface-visibility: hidden; ... }`: both faces sit on top of each other and fill the card. backface-visibility hidden hides a face when it's turned away, so we only see one side at a time.
- 🟢 `.back { background: #3b82f6; }`: the back of the card is blue.
- 🟢 `.front { ... transform: rotateY(180deg); }`: the front is white and starts already turned around, so it's hidden until the card flips.
- 🟢 `.card.matched .front { background: #86efac; }`: when a pair is found, its front turns green.
- 🟢 `button { ... }`: a bigger, clickable button.

> 🖱️ I'm pressing Control and S to save, clicking the Firefox icon in the taskbar, and clicking the Reload button to the left of the address bar, to see the styles.
>
> (Presiono Control y S para guardar, hago clic en el ícono de Firefox en la barra de tareas y hago clic en el botón Reload a la izquierda de la barra de direcciones, para ver los estilos.)
>
> 🟢 The page is dark and centered now. The cards will appear when we add the JavaScript.
>
> (Ahora la página es oscura y está centrada. Las cartas van a aparecer cuando agreguemos el JavaScript.)

---

## 10:00–14:00 — JavaScript, parte 1: mezclar y crear las cartas

> 🖱️ I'm clicking the VS Code icon in the taskbar, and clicking after the button line, just before the closing body tag, to add the script.
>
> (Hago clic en el ícono de VS Code en la barra de tareas, y hago clic después de la línea del botón, justo antes del cierre de body, para agregar el script.)

Escribís:

```html
  <script>
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

    function shuffle(array) {
      for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
      }
      return array;
    }

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
  </script>
```

**What each line does:**

- 🟢 `const symbols = ["A", ... "H"];`: the eight symbols. Each one will appear twice, so we get eight pairs.
- 🟢 `const grid = document.getElementById("grid");` and the next two lines: these find the grid, the attempts number, and the message on the page, so the code can change them.
- 🟢 `let firstCard = null; let secondCard = null;`: the two cards the player has turned over in the current turn.
- 🟢 `let lockBoard = false;`: when this is true, the board ignores clicks, while two wrong cards are turning back.
- 🟢 `let attempts = 0; let matches = 0;`: the number of attempts and the number of pairs found.
- 🟢 `let flipBackTimer = null;`: it remembers the timer that turns wrong cards back, so a restart can cancel it.
- 🟢 `function shuffle(array) { ... }`: this is the Fisher-Yates shuffle. It goes from the last position to the first and swaps each card with a random earlier one. It's the standard way to give every order the same chance.
- 🟢 `[array[i], array[j]] = [array[j], array[i]];`: this swaps two values in one line.
- 🟢 `function startGame() {`: this prepares a new game.
- 🟢 `clearTimeout(flipBackTimer); grid.innerHTML = ""; resetTurn();`: it cancels any pending timer, empties the board, and clears the current turn.
- 🟢 `attempts = 0; matches = 0; ... message.textContent = "";`: it resets the counters, the number on screen, and the message.
- 🟢 `shuffle([...symbols, ...symbols]).forEach(symbol => {`: the three dots copy the symbols twice into one list of 16, which is shuffled. Then, for each symbol, it creates a card.
- 🟢 `const card = document.createElement("div"); card.className = "card";`: it creates a new div with the class card.
- 🟢 `card.dataset.symbol = symbol;`: it saves the symbol in the card, so we can compare two cards later.
- 🟢 `card.innerHTML = ...`: inside the card, it puts the inner part with the back and the front, which shows the symbol.
- 🟢 `card.addEventListener("click", () => flipCard(card));`: when the card is clicked, it calls flipCard. I'll write that function next.
- 🟢 `grid.appendChild(card);`: it adds the card to the board.

> 🖱️ I'm pressing Control and S to save. I won't test yet, because startGame needs the functions from the next part.
>
> (Presiono Control y S para guardar. Todavía no lo pruebo, porque startGame necesita las funciones de la parte siguiente.)

---

## 14:00–18:00 — JavaScript, parte 2: voltear, comparar, ganar y reiniciar

> 🖱️ I'm clicking at the end of the startGame function, before the closing script tag, to add the game logic.
>
> (Hago clic al final de la función startGame, antes del cierre de script, para agregar la lógica del juego.)

Escribís:

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

    function resetTurn() {
      firstCard = null;
      secondCard = null;
      lockBoard = false;
    }

    document.getElementById("restart").addEventListener("click", startGame);
    startGame();
```

**What each line does:**

- 🟢 `if (lockBoard || card === firstCard || card.classList.contains("matched")) return;`: this ignores the click in three cases: while wrong cards are turning back, if the player clicks the same card twice, or if the card is already part of a found pair. This is what locks the matched pairs.
- 🟢 `card.classList.add("flipped");`: it adds the flipped class, and the CSS turns the card over.
- 🟢 `if (!firstCard) { firstCard = card; return; }`: if this is the first card of the turn, it saves it and waits for the second one.
- 🟢 `secondCard = card; attempts++; attemptsText.textContent = attempts;`: on the second card, one attempt is complete, so the counter goes up on screen.
- 🟢 `checkMatch();`: then it compares the two cards.
- 🟢 `if (firstCard.dataset.symbol === secondCard.dataset.symbol) {`: if both cards have the same symbol, it's a match.
- 🟢 `firstCard.classList.add("matched"); secondCard.classList.add("matched");`: both cards get the matched class: they stay face up and turn green.
- 🟢 `matches++; resetTurn();`: one more pair found, and a new turn starts.
- 🟢 `if (matches === symbols.length) { message.textContent = ...; }`: when the pairs found equal eight, the player won, and the message shows the number of attempts.
- 🟢 `else { lockBoard = true; flipBackTimer = setTimeout(() => { ... }, 800); }`: if the cards are different, the board is locked, and after 800 milliseconds both cards turn back. The pause gives the player time to see them.
- 🟢 `function resetTurn() { ... }`: it forgets the two cards and unlocks the board.
- 🟢 `document.getElementById("restart").addEventListener("click", startGame);`: the Restart button starts a new game.
- 🟢 `startGame();`: this starts the first game when the page loads.

---

## 18:00–22:00 — Probar el juego en Firefox

> 🖱️ I'm pressing Control and S to save, clicking the Firefox icon in the taskbar, and clicking the Reload button to the left of the address bar, to load the game.
>
> (Presiono Control y S para guardar, hago clic en el ícono de Firefox en la barra de tareas y hago clic en el botón Reload a la izquierda de la barra de direcciones, para cargar el juego.)
>
> 🟢 Now we have 16 blue cards in a 4 by 4 grid.
>
> (Ahora tenemos 16 cartas azules en una grilla de 4 por 4.)

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

## 22:00–25:30 — Epílogo (3–4 minutos)

Revisá en las reglas de Odin qué tiene que tener el epílogo y ajustá este texto si piden algo distinto.

> 🖱️ I'm clicking the VS Code icon in the taskbar, and scrolling slowly through index.html with the mouse wheel, to go over the code.
>
> (Hago clic en el ícono de VS Code en la barra de tareas y recorro despacio index.html con la rueda del mouse, para repasar el código.)
>
> 🟢 In this epilogue, I want to go over my approach. I kept everything in one file, as the task asks, but separated it into three clear parts: the HTML structure, the CSS styles, and the JavaScript logic.
>
> (En este epílogo quiero repasar mi enfoque. Dejé todo en un solo archivo, como pide la tarea, pero separado en tres partes claras: la estructura HTML, los estilos CSS y la lógica de JavaScript.)
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
2. Subí los **cuatro archivos por separado**: el **MP4**, el **ZIP original de TaskRecorder**, **Deliverables.zip** (con `index.html`) y **Metadata.rtf**.
