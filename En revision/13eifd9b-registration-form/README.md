# 13eifd9b — Registration Form con extensiones de VS Code

Guion para grabar la tarea **13eifd9b**: en **VS Code**, escribís un formulario de registro en tres archivos y, con cada uno, instalás y probás una extensión: **Live Server** (HTML), **Prettier** (CSS) y **ESLint** (JavaScript). La página se ve en **Firefox**. Se graba en **una sola toma**, en una **Mac**. La grabación tiene que durar **entre 15:00 y 50:59**. Este guion apunta a unos **25 minutos**, epílogo incluido.

### Cambios en esta versión

| Problema de la versión anterior | Qué cambió |
| ------------------------------- | ---------- |
| La mayor parte de lo que se hacía en pantalla no estaba narrado | **Todas** las interacciones tienen su frase 🖱️ con **qué** hacés y **dónde** está: cada clic, archivo nuevo, tipeo, guardado, comando, prueba y corrección |
| Se explicaba el código línea por línea (24 líneas en `script.js` y 15 en `eslint.config.mjs`) | El código se escribe **por bloques** y cada bloque se explica con **una** frase 🟢 |
| Referencia a la documentación oficial de ESLint | **Eliminada.** No se abre ninguna documentación: todo pasa en VS Code y en la página |
| Atajos mezclados de Windows y Mac (`Ctrl`, `F12`, `F5`) | Solo atajos de **Mac** (`Cmd`, `Option`), dichos en voz alta |
| Introducción larga, con VS Code ya en pantalla | Menos de 20 segundos, con la **descripción de la tarea** en pantalla. Después abrís VS Code desde el **Dock** |
| El cierre era un saludo | **Epílogo** de 2 a 4 minutos con enfoque, **desafíos** y reflexiones |

### Las partes de la tarea y dónde están

| Parte | Dónde |
| ----- | ----- |
| 1. HTML (`index.html`) + **Live Server** | Pasos 1 a 4 |
| 2. CSS (`styles.css`) + **Prettier** | Pasos 5 a 7 |
| 3. JavaScript (`script.js`) + **ESLint** | Pasos 8 a 11 |
| 4. El proyecto funcionando (escritorio y celular) | Paso 12 |

**Cómo leer este guion:**

- 🖱️ = lo decís **mientras hacés** la acción. Siempre dice **qué** hacés y **dónde** está en la pantalla. Son las frases que cuenta AutoQC: **no te saltees ninguna**.
- 🟢 = explicación corta, entre una acción y otra.
- El texto en castellano es lo que hacés en pantalla. No se lee.
- Si usás un **atajo de teclado**, decí la tecla en voz alta: *"I'm pressing Command + S"*.
- **No expliques el código línea por línea.** Cada bloque tiene **una** frase 🟢 que dice para qué sirve, y la decís antes de escribirlo.
- Todo bloque de código sigue el mismo ciclo: **frase 🟢 → 🖱️ clic en el lugar del archivo donde va → 🖱️ escribir el bloque.** Al final de cada archivo: **🖱️ guardar con `Cmd + S` → señalar el resultado → explicarlo.**
- El título de cada paso **no se escribe en ningún lado**: lo decís en voz alta (*"Step two: Live Server"*).

> **Importante:** el Goal de Studio tiene prioridad sobre este guion. Si pide otros campos, otras extensiones u otros nombres de archivo, adaptá el guion.

---

## Archivos de la carpeta

```
13eifd9b-registration-form/
├── README.md     ← este guion
├── index.html    ← resultado final del paso 3
├── styles.css    ← resultado final del paso 6
└── script.js     ← resultado final del paso 8
```

Estos archivos son la **referencia** para comparar. En el video **no se usan**: se crea una carpeta nueva y vacía.

---

## Antes de grabar

1. Leé el Goal y comparalo con este guion.
2. **Node.js:** en la Terminal de la Mac, escribí `node -v`. Tiene que mostrar una versión, por ejemplo `v22.14.0`. Si da error, instalá la versión LTS desde https://nodejs.org. Se necesita para ESLint (paso 10).
3. **Extensiones:** si ya tenés instaladas Live Server, Prettier o ESLint, desinstalalas (engranaje → **Uninstall**) y reiniciá VS Code, así en el video aparecen con el botón **Install**.
4. **Prettier:** en VS Code, `Cmd + ,` → buscá `prettier require config` y dejá la casilla **desmarcada**. Si no, Prettier no formatea en el paso 7.
5. **Navegador:** **Firefox** tiene que ser el navegador predeterminado de la Mac (Live Server abre ese).
6. **Ventanas:** dejá **Firefox** abierto con la **descripción de la tarea** en pantalla, porque con ella arranca la grabación. Dejá **VS Code** abierto en la pestaña **Welcome**, sin ninguna carpeta, y con su ícono en el **Dock**. Borrá del Escritorio cualquier carpeta `registration-form` vieja.
7. Agrandá el zoom de VS Code (`Cmd + +`) para que el código se lea.
8. Practicá una vez entera en voz alta con cronómetro.
9. Nunca más de 45 segundos en silencio. Si Copilot u otra IA te sugiere código, ignoralo y seguí escribiendo vos.
10. Salvo la descripción de la tarea del principio, no muestres Studio, Mercor, datos personales ni herramientas de IA.

---

## 0:00–1:00 — Introducción y abrir VS Code

Empezás con la **descripción de la tarea** en Firefox. La introducción dura **menos de 20 segundos**:

> 🟢 I will be beginning my task soon. I'll build a registration form in VS Code with HTML, CSS, and JavaScript, and with each file I'll install and test one extension: Live Server, Prettier, and ESLint.

> 🖱️ I'm clicking the yellow minimize button at the top left of this Firefox window, to put the task description away.

> 🖱️ I'm clicking the VS Code icon in the Dock, on the right side of the screen, to open the editor.

> 🖱️ I'm pointing at the Welcome tab in the middle of VS Code. There's no folder open yet, because I'm starting from zero.

---

## 1:00–2:00 — Paso 1: abrir la carpeta del proyecto

> 🟢 Step one: the project folder. I open a whole folder, not a single file, so the Explorer shows all the files together and the extensions know which files belong to the project.

> 🖱️ I'm clicking the File menu at the top left of the screen, and choosing Open Folder.

> 🖱️ In the window, I'm clicking Desktop in the list on the left, and then the New Folder button at the bottom left, to create the project folder.

> 🖱️ I'm typing registration-form as the folder name, clicking Create, and then the Open button at the bottom right.

Si VS Code pregunta si confiás en los autores:

> 🖱️ I'm clicking "Yes, I trust the authors" in the dialog in the center of the screen. These are my own files, and without trust some extensions wouldn't work.

> 🖱️ I'm pointing at the Explorer on the left, under REGISTRATION-FORM. It's empty, because we start from zero.

---

## 2:00–3:30 — Paso 2: instalar Live Server

> 🟢 Step two: Live Server. Without it, I'd have to refresh the browser after every change. Live Server runs a small local web server and reloads the page every time I save.

> 🖱️ I'm clicking the Extensions icon, the four squares in the left sidebar, to open the Extensions view.

> 🖱️ I'm clicking the search box at the top of the Extensions panel and typing Live Server.

> 🖱️ I'm pointing at the author under the first result, Ritwick Dey. There are similar names, so I check it's the original one.

> 🖱️ I'm clicking the blue Install button next to Live Server, in the panel on the left.

> 🖱️ I'm pointing at the new Go Live button at the bottom right, in the blue status bar. We'll use it as soon as we have a page.

> 🖱️ I'm clicking the Explorer icon, the two pages at the top of the left sidebar, to go back to my files.

---

## 3:30–7:00 — Paso 3: `index.html`, la estructura

> 🟢 Step three: the HTML. index.html is the page a web server shows by default.

> 🖱️ I'm moving the mouse over REGISTRATION-FORM in the Explorer, and clicking the New File icon, the page with a plus, on the right of the folder name.

> 🖱️ I'm typing index.html as the file name and pressing Return. The file opens in the middle of the screen.

**Bloque 1 de 4 — esqueleto.** Escribí `!` y pulsá **Tab**: VS Code (Emmet) crea el esqueleto. Cambiá el `<title>` y agregá la línea `<link>`. El esqueleto puede verse un poco distinto (`<!DOCTYPE html>` en mayúsculas, 4 espacios de sangría); funciona igual.

> 🟢 Emmet, built into VS Code, writes the HTML skeleton when I type an exclamation mark and press Tab. I'll change the title and link the CSS file we'll create later.

> 🖱️ I'm typing an exclamation mark on the first line of index.html, and pressing Tab.

> 🖱️ I'm double-clicking the word Document inside the title tag, near the top of the file, and typing Registration Form.

> 🖱️ I'm clicking at the end of the title line and pressing Return, to add the link to styles.css below it.

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Registration Form</title>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
```

**Bloque 2 de 4 — el formulario y el campo Name.** Dentro del `<body>`:

> 🟢 This block opens the form and adds the first field. novalidate turns off the browser's own popups, because we'll show our own messages. Each field has a label, an input, and an empty small element for its error, named with the field id plus "-error".

> 🖱️ I'm clicking inside the body tag, in the middle of the file, to type the form there.

> 🖱️ I'm typing the form, the heading, and the name field.

```html
    <form id="form" novalidate>
      <h1>Create account</h1>

      <label for="name">Name</label>
      <input id="name" type="text" />
      <small id="name-error"></small>
```

**Bloque 3 de 4 — Email y Password:**

> 🟢 The email and password fields follow exactly the same pattern, so one piece of JavaScript can check all three. The email type shows the at sign on phone keyboards, and the password type hides what you type.

> 🖱️ I'm typing the email and password fields below the name field.

```html

      <label for="email">Email</label>
      <input id="email" type="email" />
      <small id="email-error"></small>

      <label for="password">Password</label>
      <input id="password" type="password" />
      <small id="password-error"></small>
```

**Bloque 4 de 4 — botón, mensaje y script.** Las etiquetas `</body>` y `</html>` ya las creó Emmet.

> 🟢 The submit button sends the form, the success message stays hidden until the data is valid, and the script goes at the end, so the whole form exists when JavaScript runs.

> 🖱️ I'm typing the button, the success message, and the script tag at the bottom of the body.

```html

      <button type="submit">Sign up</button>
      <p id="success" hidden>Registration successful!</p>
    </form>

    <script src="script.js"></script>
  </body>
</html>
```

> 🖱️ I'm pressing Command + S to save index.html.

> 🖱️ I'm pointing at the index.html tab at the top. The white dot is gone, so the file is saved.

---

## 7:00–8:00 — Paso 4: probar Live Server

> 🖱️ I'm clicking the Go Live button at the bottom right of VS Code, in the status bar, to open the page.

> 🖱️ I'm pointing at the address bar at the top of Firefox: 127.0.0.1, port 5500.

> 🟢 That's a local server on my own computer, only for development.

> 🖱️ I'm moving the mouse over the page, from the heading down to the button.

> 🟢 There's no CSS yet, so the page is plain, but the heading, the three fields, and the button are there. The success message is hidden. From now on, every time I save, this page reloads by itself.

> 🖱️ I'm clicking the VS Code icon in the Dock, on the right, to go back to the editor.

---

## 8:00–9:00 — Paso 5: instalar Prettier

> 🟢 Step five: Prettier, a code formatter. When we type fast, the code gets messy, and Prettier fixes spaces and indentation with one shortcut.

> 🖱️ I'm clicking the Extensions icon, the four squares in the left sidebar.

> 🖱️ I'm clicking the search box at the top of the panel, deleting the old text, and typing Prettier.

> 🖱️ I'm pointing at the first result, Prettier - Code formatter, by Prettier, the official one.

> 🖱️ I'm clicking the blue Install button next to it, in the panel on the left.

> 🖱️ I'm clicking the Explorer icon at the top of the left sidebar, to go back to my files.

---

## 9:00–11:00 — Paso 6: `styles.css`, el diseño

> 🟢 Step six: the CSS. The file name must match the link we wrote in the HTML.

> 🖱️ I'm clicking the New File icon, on the right of REGISTRATION-FORM in the Explorer, typing styles.css, and pressing Return.

**Bloque 1 de 2 — el formulario:**

> 🟢 This first rule puts the fields in one column with a small gap, keeps the form narrow and centered, and changes the font. Because it uses max-width, it also fits on a phone.

> 🖱️ I'm typing the form rule at the top of styles.css.

```css
form {
  display: grid;
  gap: 6px;
  max-width: 300px;
  margin: 40px auto;
  font-family: Arial, sans-serif;
}
```

**Bloque 2 de 2 — los errores:**

> 🟢 These two rules are for the errors: a red border on inputs with the class invalid, which JavaScript will add, and red text for the messages.

> 🖱️ I'm typing the two error rules below the form rule.

```css

input.invalid {
  border: 2px solid red;
}

small {
  color: red;
}
```

> 🖱️ I'm pressing Command + S to save styles.css.

> 🖱️ I'm clicking the Firefox icon in the Dock, on the right, and choosing the window with our page.

> 🟢 The page updated by itself, without refreshing: that's Live Server. Now the form is centered, narrow, and in Arial.

> 🖱️ I'm clicking the VS Code icon in the Dock, to go back to the editor.

---

## 11:00–12:30 — Paso 7: probar Prettier

> 🟢 Step seven: testing Prettier. I need messy code, so I'll make some on purpose.

> 🖱️ I'm selecting the input.invalid rule, lines 9 to 11 of styles.css, by dragging the mouse.

> 🖱️ I'm typing the same rule on one line, with no spaces.

```css
input.invalid{border:2px solid red}
```

> 🖱️ I'm right-clicking inside the code, and choosing Format Document With, in the menu.

> 🖱️ I'm choosing Configure Default Formatter, in the list at the top of the window, and then Prettier - Code formatter.

> 🟢 This only tells VS Code to use Prettier. It doesn't format anything yet.

> 🖱️ I'm pressing Shift + Option + F, the Format Document shortcut.

> 🖱️ I'm pointing at lines 9 to 11. The rule is back on three clean lines.

> 🖱️ I'm pressing Command + S to save the file.

Resultado esperado:

```css
input.invalid {
  border: 2px solid red;
}
```

---

## 12:30–16:00 — Paso 8: `script.js`, la funcionalidad

> 🟢 Step eight: the JavaScript, which makes the form work.

> 🖱️ I'm clicking the New File icon, on the right of REGISTRATION-FORM in the Explorer, typing script.js, and pressing Return.

**Ojo con el autocompletado:** cuando escribís `{`, `(` o `[`, VS Code agrega solo el cierre. No lo borres: seguí escribiendo adentro, y no escribas de nuevo un cierre que ya está.

**Bloque 1 de 4 — encontrar los elementos:**

> 🟢 These two lines find the form and the success message by their ids, and keep them in constants.

> 🖱️ I'm typing the two constants at the top of script.js.

```js
const form = document.getElementById("form");
const success = document.getElementById("success");
```

**Bloque 2 de 4 — las reglas:**

> 🟢 This object keeps all the rules in one place. Each key is a field id, and each value has a test that returns true or false, and the error message.

> 🖱️ I'm typing the rules object below the constants.

```js

const rules = {
  name: [(v) => v.trim().length >= 2, "Min. 2 characters."],
  email: [(v) => v.includes("@"), "Invalid email"],
  password: [(v) => v.length >= 8, "Min. 8 characters."],
};
```

**Bloque 3 de 4 — escuchar el envío:**

> 🟢 This listens for the submit event, and preventDefault stops the page from reloading, so we can check the data first.

> 🖱️ I'm typing the addEventListener call below the rules.

```js

form.addEventListener("submit", (event) => {
  event.preventDefault();
```

**Bloque 4 de 4 — validar y mostrar el resultado.** Escribilo dentro de la función, antes del `});` que puso VS Code.

> 🟢 For each rule, this runs the test, adds or removes the red border, and writes or clears the error. map checks every field, so all the errors show at once, and every says if all of them passed. If they did, the success message appears and the form is cleared.

> 🖱️ I'm clicking the empty line inside the function, above the closing brace, and typing the validation.

```js

  const ok = Object.entries(rules)
    .map(([id, [test, message]]) => {
      const valid = test(form.elements[id].value);
      form.elements[id].classList.toggle("invalid", !valid);
      document.getElementById(id + "-error").textContent = valid ? "" : message;
      return valid;
    })
    .every(Boolean);

  success.hidden = !ok;
  if (ok) form.reset();
});
```

> 🖱️ I'm pressing Command + S to save script.js.

> 🖱️ I'm pointing at the last line, 24, at the bottom of the file. The file is complete.

> 🟢 Before testing the form, let's add the last extension, to check this code for mistakes.

---

## 16:00–17:00 — Paso 9: instalar la extensión de ESLint

> 🟢 Step nine: ESLint, a linter. It reads the JavaScript without running it and finds real mistakes, like a misspelled variable.

> 🖱️ I'm clicking the Extensions icon in the left sidebar, then the search box at the top, and typing ESLint.

> 🖱️ I'm pointing at the first result, ESLint, by Microsoft.

> 🖱️ I'm clicking the blue Install button next to it, in the panel on the left.

> 🟢 This extension only connects VS Code to ESLint. ESLint itself and its rules are installed inside the project, so everyone uses the same version.

> 🖱️ I'm clicking the Explorer icon at the top of the left sidebar.

---

## 17:00–19:30 — Paso 10: instalar y configurar ESLint en el proyecto

> 🖱️ I'm clicking the Terminal menu at the top of the screen, and choosing New Terminal. The terminal opens at the bottom of VS Code.

> 🖱️ I'm typing pwd in the terminal and pressing Return, to check which folder I'm in.

> 🖱️ I'm pointing at the result in the terminal: it ends in registration-form, the right folder.

> 🟢 Now I'll install ESLint version 9 with npm. save-dev means it's a development tool, not part of the website.

> 🖱️ I'm typing the install command in the terminal and pressing Return.

```
npm install --save-dev eslint@9
```

> 🖱️ I'm pointing at the three new items in the Explorer, on the left: package.json, package-lock.json, and node_modules.

> 🟢 package.json lists the project's tools, package-lock.json saves the exact versions, and node_modules has ESLint's code.

> 🖱️ I'm typing npx eslint -v in the terminal and pressing Return, to check the installation.

> 🖱️ I'm pointing at the version in the terminal. It starts with 9, so it works.

> 🟢 ESLint still doesn't know which rules to use, so I'll create its configuration file, eslint.config.mjs, next to package.json.

> 🖱️ I'm clicking the New File icon, on the right of REGISTRATION-FORM in the Explorer, typing eslint.config.mjs, and pressing Return.

> 🟢 This file checks every .js file, says our script runs in the browser, where document already exists, and turns on two rules: an error for undefined variables, and a warning for unused ones.

> 🖱️ I'm typing the configuration in eslint.config.mjs, in the middle of the screen.

Ojo con el autocompletado: si VS Code ya cerró `}`, `]` o `)`, no los escribas de nuevo. Agregá a mano las comas y el `;` del final.

```js
import { defineConfig } from "eslint/config";

export default defineConfig([
  {
    files: ["**/*.js"],
    languageOptions: {
      sourceType: "script",
      globals: { document: "readonly" },
    },
    rules: {
      "no-undef": "error",
      "no-unused-vars": "warn",
    },
  },
]);
```

> 🖱️ I'm pressing Command + S to save eslint.config.mjs.

> 🟢 The extension started before this file existed, so I have to restart it.

> 🖱️ I'm pressing Command + Shift + P to open the Command Palette, at the top of VS Code.

> 🖱️ I'm typing ESLint: Restart ESLint Server in the Command Palette and pressing Return.

---

## 19:30–21:00 — Paso 11: probar ESLint

> 🟢 Step eleven: testing ESLint. First, I'll check the real code.

> 🖱️ I'm clicking inside the terminal, at the bottom, and typing npx eslint script.js, then Return.

> 🖱️ I'm pointing at the terminal: there's no output, so ESLint found no problems.

> 🟢 To see ESLint catch a mistake, I'll make a typical one on purpose.

> 🖱️ I'm clicking the script.js tab at the top, and then at the end of the file, below line 24.

> 🖱️ I'm typing nmae, a misspelled name, on line 25, and pressing Command + S to save.

```js
nmae;
```

> 🖱️ I'm moving the mouse over the red underline on line 25.

> 🟢 ESLint says "'nmae' is not defined": that's the no-undef rule we configured.

> 🖱️ I'm clicking inside the terminal and running npx eslint script.js again.

> 🖱️ I'm pointing at the error in the terminal: line 25, the message, and the rule name, no-undef.

> 🟢 Prettier didn't complain, because the line is well formatted, just wrong. Prettier checks how the code looks, and ESLint checks if it makes sense.

> 🖱️ I'm selecting line 25 in script.js, deleting it, and pressing Command + S to save.

> 🖱️ I'm running npx eslint script.js in the terminal one last time, and pointing at the empty output. The code is clean.

Salida esperada con `nmae;`:

```
  25:1  error  'nmae' is not defined  no-undef

✖ 1 problem (1 error, 0 warnings)
```

---

## 21:00–22:30 — Paso 12: el formulario funcionando

> 🟢 Step twelve: the whole project working. I'll test empty fields, wrong values, valid values, and a phone screen.

> 🖱️ I'm clicking the Firefox icon in the Dock, on the right, and choosing the window with our page.

> 🖱️ I'm pressing Command + R to reload the page, so it has the latest JavaScript.

> 🖱️ I'm clicking the Sign up button, at the bottom of the form, with all the fields empty.

> 🟢 Three red borders and three error messages. The page didn't reload, thanks to preventDefault.

> 🖱️ I'm clicking the Name field and typing J, then the Email field and typing jane, then the Password field and typing abc.

> 🖱️ I'm clicking the Sign up button again.

> 🟢 Still three errors, because none of the values follow the rules.

> 🖱️ I'm clearing each field and typing Jane, jane@example.com, and secret123.

> 🖱️ I'm clicking the Sign up button.

> 🖱️ I'm pointing at the message under the button: Registration successful!

> 🟢 The red borders and the errors are gone, and reset cleared the form.

> 🖱️ I'm pressing Command + Option + M to open Firefox's Responsive Design Mode, to simulate a phone.

> 🖱️ I'm clicking the device menu at the top of the page, and choosing a phone.

> 🟢 The form fits the phone width, thanks to max-width.

> 🖱️ I'm pressing Command + Option + M again to close Responsive Design Mode.

| Datos | Resultado |
| ----- | --------- |
| Campos vacíos | Bordes rojos y los mensajes _Min. 2 characters._, _Invalid email_, _Min. 8 characters._ |
| `J`, `jane`, `abc` | Los mismos tres errores |
| `Jane`, `jane@example.com`, `secret123` | Sin errores, campos vacíos y el mensaje _Registration successful!_ |
| Vista de celular | El formulario usa el ancho de la pantalla, hasta 300 píxeles |

---

## 22:30–25:00 — Epílogo

Dura **de 2 a 4 minutos**: enfoque, desafíos y reflexiones.

> 🖱️ I'm clicking the VS Code icon in the Dock, to go back to the editor.

> 🖱️ I'm clicking index.html in the Explorer, on the left.

> 🟢 Let me summarize. I split the form into three files, so each one has a single job: index.html for the structure, with the same id pattern for every field.

> 🖱️ I'm clicking styles.css in the Explorer.

> 🟢 styles.css for the design, with only three rules, and script.js for the validation.

> 🖱️ I'm clicking script.js in the Explorer.

> 🟢 About my decisions: I kept all the rules in one object, so adding a field means adding one line. And I used map before every, so every field shows its own error at the same time.

> 🖱️ I'm pointing at the extensions in the left sidebar, then at eslint.config.mjs in the Explorer.

> 🟢 And with each file, one extension: Live Server to see changes instantly, Prettier to keep the code clean, and ESLint to catch real mistakes before they reach the browser.

> 🟢 There were two challenges. Prettier didn't format the first time, because VS Code needs to be told which formatter to use. And ESLint needed more setup than the other two: installing it in the project, writing its configuration, telling it that document exists in the browser, and restarting its server.

> 🟢 One limit: the email check only looks for an at sign, and the validation runs only in the browser. As a next step, a real app would also validate on the server and confirm the email.

> 🟢 The takeaway: three short files and three extensions give a cleaner and faster workflow. Thanks for watching!

Si el reloj todavía no pasó los 15:00 (no debería pasar), no cortes: probá en la página otro caso inválido (por ejemplo, un nombre con solo espacios) y explicá por qué falla.

---

## Si algo sale mal (frases para corregir)

Siempre decí **qué** corregís y **dónde**:

| Error | Qué pasa | Qué decís y hacés |
| ----- | -------- | ----------------- |
| No aparece **Go Live** | La extensión no terminó de cargar | 🖱️ *"The Go Live button isn't in the status bar yet. I'm pressing Command + Shift + P and running Developer: Reload Window, to reload VS Code."* |
| Prettier no formatea | No está elegido como formateador | 🖱️ *"Prettier didn't format the file. I'm right-clicking in the code, choosing Format Document With, and picking Prettier - Code formatter directly."* |
| `npm: command not found` | Node.js no está instalado | Cortá la grabación: es un problema de preparación (punto 2 de "Antes de grabar"). |
| No aparece el subrayado rojo | La extensión no leyó la configuración | 🖱️ *"The red underline didn't appear. I'm pressing Command + Shift + P and running ESLint: Restart ESLint Server again."* |
| `TypeError: ... null` en la consola, o el formulario recarga la página | Un id mal escrito en `index.html` o en `script.js` | 🖱️ *"The form isn't working, because I misspelled the id in index.html, line 14. I'm fixing it, pressing Command + S, and testing again."* |
| Error de tipeo | Un paréntesis o una comilla de menos | 🖱️ *"I made a typo in script.js, a missing parenthesis on the line ESLint underlines. I'm adding it and saving again."* |
| Cualquier cosa fuera del guion | Un aviso, una ventana | 🖱️ *"I'm closing this notification at the bottom right of VS Code, to keep working."* |

---

## Después de grabar

1. Ejecutá **Run full AutoQC**, no solo *Rerun failing*. Revisá que el porcentaje de acciones con What + Where pase el **70%**.
2. Armá **Deliverables.zip** con la carpeta `registration-form` del video: `index.html`, `styles.css`, `script.js`, `eslint.config.mjs`, `package.json` y `package-lock.json`, **sin** `node_modules`.
3. Subí los **cuatro archivos por separado**: el **MP4**, el **ZIP original de TaskRecorder**, **Deliverables.zip** y **Metadata.rtf**.
