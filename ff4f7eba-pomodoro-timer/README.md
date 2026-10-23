# ff4f7eba — Pomodoro Timer

Guion paso a paso para grabar la tarea **ff4f7eba**: un temporizador Pomodoro en un único archivo HTML, con **HTML**, **CSS** y **JavaScript** puro, en **Visual Studio Code**, y probado en **Firefox**. Tiene sesiones de 25 minutos de trabajo y 5 de descanso, botones **Start**, **Pause** y **Reset**, el tiempo en formato **MM:SS** y un contador de sesiones. La grabación tiene que durar **entre 15:00 y 50:59**. Este guion apunta a unos **22 minutos**, epílogo incluido.

**Cómo leer este guion:**

- Las frases que empiezan con 🖱️ las decís **en el momento de hacer clic, desplazarte o escribir**. Siempre dicen **qué** elemento usás, **dónde** está en la pantalla y **por qué** lo usás. Son las que revisa AutoQC.
- Las frases que empiezan con 🟢 son la explicación que **decís en inglés** entre una acción y otra.
- Debajo de cada bloque de código, la lista **What each line does** explica cada línea (o cada grupo de líneas parecidas) en inglés. La leés en voz alta mientras escribís.
- El resto, en castellano, es lo que hacés en pantalla. Las traducciones aparecen entre paréntesis después de cada frase.

> **Importante:** el Goal de Studio tiene prioridad sobre este guion. El Goal que tengo dice "MM display". Este guion usa **MM:SS** (minutos y segundos), que es lo habitual en un Pomodoro. Confirmalo en Studio.

---

## Archivos de la carpeta

```
ff4f7eba-pomodoro-timer/
├── README.md
└── solution/
    └── index.html   ← el temporizador terminado, para probarlo y practicar (NO lo abras durante la grabación)
```

**Cómo se prueba sin esperar 25 minutos.** Para comprobar que el trabajo pasa al descanso y que el contador sube, cambiás por un momento las duraciones a segundos: `WORK_MINUTES = 0.1` (6 segundos) y `BREAK_MINUTES = 0.05` (3 segundos). Después de probar, las volvés a dejar en 25 y 5. Esto está incluido en el guion.

**Sobre el porcentaje de escritura:** son unas 80 líneas. Usá el atajo Emmet (`!` + `Enter`), escribí por partes y probá en Firefox después de cada una.

---

## Antes de grabar

1. Leé el Goal y compará este guion con el campo **Describe your idea** de Studio.
2. Abrí `solution/index.html` en Firefox y probalo, para conocer el comportamiento.
3. Creá una carpeta vacía `Escritorio\pomodoro-timer`.
4. Practicá una vez entera, leyendo en voz alta las frases 🖱️ y 🟢, y cronometrá. Después vaciá la carpeta.
5. Dejá abiertos el documento **Goal** en Firefox y VS Code (sin ninguna carpeta abierta). Agrandá la letra de VS Code (`Ctrl + +`).
6. Mostrá una sola ventana a la vez, maximizada, y pasá de una a otra con la barra de tareas. Cerrá o minimizá todo lo demás.
7. Pausa de ~1 segundo después de cada clic y nunca más de 45 segundos en silencio. Mientras el temporizador corre en las pruebas, seguí hablando.
8. No muestres Studio, Mercor, información privada ni herramientas de IA, ni la carpeta `solution`. Cerrá este guion si está en la misma pantalla.

---

## 0:00–0:45 — Mostrar el Goal

> 🖱️ I'm on the Goal document in Firefox, to show what this task asks for.
>
> (Estoy en el documento del Goal, en Firefox, para mostrar qué pide esta tarea.)
>
> 🟢 As a front-end developer, I'll build a Pomodoro timer in a single HTML file, with HTML, CSS, and plain JavaScript. It will have 25-minute work sessions, 5-minute breaks, Start, Pause, and Reset buttons, a minutes and seconds display, and a session counter.
>
> (Como desarrollador front-end, voy a crear un temporizador Pomodoro en un solo archivo HTML, con HTML, CSS y JavaScript puro. Va a tener sesiones de trabajo de 25 minutos, descansos de 5, botones Start, Pause y Reset, el tiempo en minutos y segundos y un contador de sesiones.)

---

## 0:45–5:00 — Crear el archivo y la estructura HTML

> 🖱️ I'm clicking the VS Code icon in the taskbar at the bottom of the screen, to open the code editor.
>
> (Hago clic en el ícono de VS Code en la barra de tareas, abajo de la pantalla, para abrir el editor de código.)
>
> 🖱️ I'm opening the File menu at the top left and choosing Open Folder, selecting the pomodoro-timer folder on the Desktop, and clicking Select Folder at the bottom right.
>
> (Abro el menú File, arriba a la izquierda, elijo Open Folder, selecciono la carpeta pomodoro-timer del Escritorio y hago clic en Select Folder, abajo a la derecha.)

Si VS Code pregunta si confiás en los autores: *"I'm clicking Yes, I trust the authors, in the center of the dialog, because this is my own folder."*

> 🖱️ I'm clicking the New File icon next to the folder name, at the top of the Explorer panel on the left, and typing index.html, to create the timer file.
>
> (Hago clic en el ícono New File al lado del nombre de la carpeta, arriba del panel Explorer de la izquierda, y escribo index.html, para crear el archivo del temporizador.)
>
> 🟢 The Pomodoro technique splits work into 25-minute focus sessions, with a 5-minute break after each one. This timer will switch between the two automatically.
>
> (La técnica Pomodoro divide el trabajo en sesiones de concentración de 25 minutos, con un descanso de 5 minutos después de cada una. Este temporizador va a pasar de una a otra automáticamente.)
>
> 🖱️ I'm typing an exclamation mark in the empty editor and pressing Enter, to let VS Code's Emmet shortcut create the basic HTML structure.
>
> (Escribo un signo de exclamación en el editor vacío y presiono Enter, para que el atajo Emmet de VS Code cree la estructura básica del HTML.)
>
> 🖱️ I'm double-clicking the word Document inside the title tag, near the top, and typing Pomodoro Timer, to name the browser tab.
>
> (Hago doble clic en la palabra Document adentro de la etiqueta title, cerca del principio, y escribo Pomodoro Timer, para ponerle nombre a la pestaña del navegador.)
>
> 🖱️ I'm clicking inside the body tag, in the middle of the file, to write the timer's structure.
>
> (Hago clic adentro de la etiqueta body, en el medio del archivo, para escribir la estructura del temporizador.)

```html
  <h1>Pomodoro Timer</h1>
  <div id="mode">Work</div>
  <div id="time">25:00</div>
  <button id="start">Start</button>
  <button id="pause">Pause</button>
  <button id="reset">Reset</button>
  <p>Sessions completed: <span id="sessions">0</span></p>
```

**What each line does:**

- 🟢 `<h1>Pomodoro Timer</h1>`: the title of the page.
- 🟢 `<div id="mode">Work</div>`: shows if we're in a work session or a break.
- 🟢 `<div id="time">25:00</div>`: the countdown, in minutes and seconds.
- 🟢 `<button id="start">`, `<button id="pause">`, `<button id="reset">`: the three controls. Each has an id, so JavaScript can react to its clicks.
- 🟢 `<p>Sessions completed: <span id="sessions">0</span></p>`: the session counter. The number is in a span, so JavaScript can update it.

> 🖱️ I'm pressing Control and S to save the file.
>
> (Presiono Control y S para guardar el archivo.)
>
> 🖱️ I'm clicking the Firefox icon in the taskbar, pressing Control and O, choosing index.html in the pomodoro-timer folder on the Desktop, and clicking the Open button at the bottom right, to see the page.
>
> (Hago clic en el ícono de Firefox en la barra de tareas, presiono Control y O, elijo index.html en la carpeta pomodoro-timer del Escritorio y hago clic en el botón Open, abajo a la derecha, para ver la página.)
>
> 🟢 The structure is there, but the buttons don't do anything yet.
>
> (La estructura está, pero los botones todavía no hacen nada.)

---

## 5:00–8:00 — CSS

> 🖱️ I'm clicking the VS Code icon in the taskbar, and clicking at the end of the title line, inside the head tag, to add the styles.
>
> (Hago clic en el ícono de VS Code en la barra de tareas y hago clic al final de la línea del title, adentro de la etiqueta head, para agregar los estilos.)

```html
  <style>
    body { font-family: Arial, sans-serif; text-align: center; background: #fee2e2; margin-top: 60px; }
    body.break { background: #dcfce7; }
    #mode { font-size: 28px; }
    #time { font-size: 96px; font-weight: bold; margin: 20px; }
    button { font-size: 18px; padding: 10px 24px; margin: 5px; cursor: pointer; }
  </style>
```

**What each line does:**

- 🟢 `body { ... background: #fee2e2; ... }`: everything centered, with a light red background for work time.
- 🟢 `body.break { background: #dcfce7; }`: when the body has the class break, the background turns light green, so you can see the mode from across the room.
- 🟢 `#mode { font-size: 28px; }`: a bigger label for the mode.
- 🟢 `#time { font-size: 96px; font-weight: bold; margin: 20px; }`: a very big, bold countdown, the most important thing on the page.
- 🟢 `button { ... }`: bigger buttons that are easy to click.

> 🖱️ I'm pressing Control and S to save, clicking the Firefox icon in the taskbar, and clicking the Reload button to the left of the address bar, to see the styles.
>
> (Presiono Control y S para guardar, hago clic en el ícono de Firefox en la barra de tareas y hago clic en el botón Reload a la izquierda de la barra de direcciones, para ver los estilos.)

---

## 8:00–13:00 — JavaScript: la cuenta regresiva, los modos y el contador

> 🖱️ I'm clicking the VS Code icon in the taskbar, and clicking after the last paragraph, just before the closing body tag, to add the script.
>
> (Hago clic en el ícono de VS Code en la barra de tareas y hago clic después del último párrafo, justo antes del cierre de body, para agregar el script.)

```html
  <script>
    const WORK_MINUTES = 25;
    const BREAK_MINUTES = 5;
    const timeText = document.getElementById("time");
    const modeText = document.getElementById("mode");
    const sessionsText = document.getElementById("sessions");
    let isWork = true;
    let secondsLeft = WORK_MINUTES * 60;
    let sessions = 0;
    let timer = null;

    function updateDisplay() {
      const minutes = String(Math.floor(secondsLeft / 60)).padStart(2, "0");
      const seconds = String(secondsLeft % 60).padStart(2, "0");
      timeText.textContent = `${minutes}:${seconds}`;
      modeText.textContent = isWork ? "Work" : "Break";
      document.body.classList.toggle("break", !isWork);
      document.title = `${minutes}:${seconds} - Pomodoro`;
    }

    function tick() {
      secondsLeft--;
      if (secondsLeft < 0) {
        if (isWork) {
          sessions++;
          sessionsText.textContent = sessions;
        }
        isWork = !isWork;
        secondsLeft = (isWork ? WORK_MINUTES : BREAK_MINUTES) * 60;
      }
      updateDisplay();
    }

    function start() {
      if (timer) return;
      timer = setInterval(tick, 1000);
    }

    function pause() {
      clearInterval(timer);
      timer = null;
    }

    function reset() {
      pause();
      isWork = true;
      secondsLeft = WORK_MINUTES * 60;
      updateDisplay();
    }

    document.getElementById("start").addEventListener("click", start);
    document.getElementById("pause").addEventListener("click", pause);
    document.getElementById("reset").addEventListener("click", reset);
    updateDisplay();
  </script>
```

**What each line does:**

- 🟢 `const WORK_MINUTES = 25; const BREAK_MINUTES = 5;`: the two durations, as constants at the top, so they're easy to find and change.
- 🟢 `const timeText = ...` and the next two lines: they find the countdown, the mode label, and the session number on the page.
- 🟢 `let isWork = true;`: true during a work session, false during a break.
- 🟢 `let secondsLeft = WORK_MINUTES * 60;`: the time left, in seconds. Counting in seconds makes the math simple.
- 🟢 `let sessions = 0; let timer = null;`: the completed sessions, and the running interval, which is null when the timer is stopped.
- 🟢 `function updateDisplay() {`: this draws the current state on the page.
- 🟢 `const minutes = String(Math.floor(secondsLeft / 60)).padStart(2, "0");`: the whole minutes. padStart adds a zero in front if needed, so 5 becomes 05.
- 🟢 `const seconds = String(secondsLeft % 60).padStart(2, "0");`: the percent sign is the remainder of the division: the seconds left after the whole minutes.
- 🟢 `` timeText.textContent = `${minutes}:${seconds}`; ``: this shows the time in MM:SS format.
- 🟢 `modeText.textContent = isWork ? "Work" : "Break";`: the label says Work or Break.
- 🟢 `document.body.classList.toggle("break", !isWork);`: during a break, the body gets the class break, so the background turns green.
- 🟢 `` document.title = ...; ``: the time also appears in the browser tab, so you can see it from another tab.
- 🟢 `function tick() { secondsLeft--;`: tick runs once per second and takes one second away.
- 🟢 `if (secondsLeft < 0) {`: when the time runs out, it switches mode.
- 🟢 `if (isWork) { sessions++; sessionsText.textContent = sessions; }`: if a work session just ended, the session counter goes up. Breaks don't count as sessions.
- 🟢 `isWork = !isWork;`: the exclamation mark flips true and false, so work becomes break and break becomes work.
- 🟢 `secondsLeft = (isWork ? WORK_MINUTES : BREAK_MINUTES) * 60;`: it loads the time for the new mode.
- 🟢 `updateDisplay();`: it shows the new time on the page.
- 🟢 `function start() { if (timer) return; timer = setInterval(tick, 1000); }`: setInterval runs tick every 1,000 milliseconds, one second. The check at the start avoids running two timers at once if someone clicks Start twice, which would make it go twice as fast.
- 🟢 `function pause() { clearInterval(timer); timer = null; }`: clearInterval stops the countdown. The time left is kept, so Start continues from the same point.
- 🟢 `function reset() { pause(); isWork = true; secondsLeft = WORK_MINUTES * 60; updateDisplay(); }`: Reset stops the timer and goes back to a fresh 25-minute work session. It keeps the session counter, because those sessions really happened.
- 🟢 `document.getElementById("start").addEventListener("click", start);` and the next two lines: each button calls its function when clicked.
- 🟢 `updateDisplay();`: it shows 25:00 when the page loads.

---

## 13:00–18:00 — Probar en Firefox

> 🖱️ I'm pressing Control and S to save, clicking the Firefox icon in the taskbar, and clicking the Reload button to the left of the address bar, to load the timer.
>
> (Presiono Control y S para guardar, hago clic en el ícono de Firefox en la barra de tareas y hago clic en el botón Reload a la izquierda de la barra de direcciones, para cargar el temporizador.)
>
> 🖱️ I'm clicking the Start button below the time, to start the countdown.
>
> (Hago clic en el botón Start, debajo del tiempo, para empezar la cuenta regresiva.)
>
> 🟢 It counts down from 25:00: 24:59, 24:58. The browser tab shows the time too.
>
> (Cuenta hacia atrás desde 25:00: 24:59, 24:58. La pestaña del navegador también muestra el tiempo.)
>
> 🖱️ I'm clicking the Start button again, to check that a second click doesn't make it run faster.
>
> (Hago clic otra vez en el botón Start, para comprobar que un segundo clic no lo hace ir más rápido.)
>
> 🟢 It still goes down one second at a time.
>
> (Sigue bajando de a un segundo.)
>
> 🖱️ I'm clicking the Pause button in the middle, to stop the countdown.
>
> (Hago clic en el botón Pause, en el medio, para frenar la cuenta regresiva.)
>
> 🟢 The time stops and stays where it was.
>
> (El tiempo se detiene y queda donde estaba.)
>
> 🖱️ I'm clicking Start again, to check that it continues from the same point.
>
> (Hago clic otra vez en Start, para comprobar que sigue desde el mismo punto.)
>
> 🖱️ I'm clicking the Reset button on the right, to go back to the beginning.
>
> (Hago clic en el botón Reset, a la derecha, para volver al principio.)
>
> 🟢 It stops and shows 25:00 again, in Work mode.
>
> (Se detiene y vuelve a mostrar 25:00, en modo Work.)

Probás el cambio de modo y el contador sin esperar 25 minutos:

> 🟢 I can't wait 25 minutes to test the switch to the break, so I'll make the durations shorter for a moment.
>
> (No puedo esperar 25 minutos para probar el paso al descanso, así que voy a acortar las duraciones por un momento.)
>
> 🖱️ I'm clicking the VS Code icon in the taskbar, and changing WORK_MINUTES to 0.1 and BREAK_MINUTES to 0.05 at the top of the script, which means 6 seconds and 3 seconds, only for testing.
>
> (Hago clic en el ícono de VS Code en la barra de tareas y cambio WORK_MINUTES a 0.1 y BREAK_MINUTES a 0.05, al principio del script, que son 6 segundos y 3 segundos, solo para probar.)
>
> 🖱️ I'm pressing Control and S, clicking the Firefox icon in the taskbar, clicking Reload to the left of the address bar, and clicking Start.
>
> (Presiono Control y S, hago clic en el ícono de Firefox en la barra de tareas, hago clic en Reload a la izquierda de la barra de direcciones y hago clic en Start.)
>
> 🟢 It counts down from 00:06. At the end, it switches to Break: the background turns green, the label says Break, and the counter shows 1 session. After 3 seconds, it goes back to Work, and after the next work session, the counter shows 2.
>
> (Cuenta hacia atrás desde 00:06. Al final pasa a Break: el fondo se pone verde, el cartel dice Break y el contador muestra 1 sesión. Después de 3 segundos vuelve a Work, y después de la siguiente sesión de trabajo, el contador muestra 2.)
>
> 🖱️ I'm clicking the Pause button, to stop the test.
>
> (Hago clic en el botón Pause, para frenar la prueba.)
>
> 🖱️ I'm clicking the VS Code icon in the taskbar, and changing WORK_MINUTES back to 25 and BREAK_MINUTES back to 5, so the timer uses the real durations.
>
> (Hago clic en el ícono de VS Code en la barra de tareas y vuelvo a poner WORK_MINUTES en 25 y BREAK_MINUTES en 5, para que el temporizador use las duraciones reales.)
>
> 🖱️ I'm pressing Control and S, clicking the Firefox icon, and clicking Reload, to confirm the timer shows 25:00 again.
>
> (Presiono Control y S, hago clic en el ícono de Firefox y hago clic en Reload, para confirmar que el temporizador vuelve a mostrar 25:00.)

---

## 18:00–21:30 — Epílogo (3–4 minutos)

Revisá en las reglas de Odin qué tiene que tener el epílogo y ajustá este texto si piden algo distinto.

> 🖱️ I'm clicking the VS Code icon in the taskbar, and scrolling slowly through index.html with the mouse wheel, to go over the code.
>
> (Hago clic en el ícono de VS Code en la barra de tareas y recorro despacio index.html con la rueda del mouse, para repasar el código.)
>
> 🟢 In this epilogue, I want to go over my approach. I store the time as a single number of seconds, and I only convert it to minutes and seconds when I show it. That keeps the logic simple: each tick just subtracts one.
>
> (En este epílogo quiero repasar mi enfoque. Guardo el tiempo como un solo número de segundos, y recién lo convierto a minutos y segundos cuando lo muestro. Eso mantiene la lógica simple: cada tick solo resta uno.)
>
> 🟢 One function, updateDisplay, is the only place that writes on the page. Start, Pause, Reset, and the tick change the state and then call it, so the screen always matches the state.
>
> (Una sola función, updateDisplay, es el único lugar que escribe en la página. Start, Pause, Reset y el tick cambian el estado y después la llaman, así la pantalla siempre coincide con el estado.)
>
> 🟢 I protected Start against double clicks, because two intervals would make the timer run twice as fast. And I put the durations in constants at the top, which made it easy to test the mode switch with a few seconds and then go back to 25 and 5.
>
> (Protegí Start contra el doble clic, porque dos intervalos harían que el temporizador vaya el doble de rápido. Y puse las duraciones en constantes al principio, lo que hizo fácil probar el cambio de modo con unos segundos y después volver a 25 y 5.)
>
> 🟢 One limitation: browsers can slow down timers in background tabs, so over a long session the countdown could drift a little. A more precise version would save the end time and calculate the difference with the clock on each tick.
>
> (Una limitación: los navegadores pueden hacer más lentos los temporizadores en pestañas de fondo, así que en una sesión larga la cuenta podría desfasarse un poco. Una versión más precisa guardaría la hora de fin y calcularía la diferencia con el reloj en cada tick.)
>
> 🟢 As next steps, I would add a sound when a session ends, a longer break after four sessions, like the classic Pomodoro technique, and settings so the user can choose the durations. Thanks for watching!
>
> (Como próximos pasos, agregaría un sonido al terminar cada sesión, un descanso más largo después de cuatro sesiones, como en la técnica Pomodoro clásica, y una configuración para que el usuario elija las duraciones. ¡Gracias por mirar!)

Si el reloj todavía no pasó los 15:00, no cortes: dejá correr la prueba corta unos ciclos más y explicá cada cambio de modo.

---

## Después de grabar

1. Comprobá que en el archivo final las duraciones quedaron en **25** y **5**.
2. Ejecutá **Run full AutoQC**, no solo *Rerun failing*.
3. Subí los **cuatro archivos por separado**: el **MP4**, el **ZIP original de TaskRecorder**, **Deliverables.zip** (con `index.html`) y **Metadata.rtf**.
