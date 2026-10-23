# Formulario de registro — Guion de narración

Un video corto de programación en vivo. Escribes un formulario de registro en tres archivos y, en cada uno, instalas y pruebas una extensión de VS Code:

1. **HTML** (`index.html`) → **Live Server**
2. **CSS** (`styles.css`) → **Prettier**
3. **JavaScript** (`script.js`) → **ESLint**

Al final muestras el proyecto funcionando.

Cada paso tiene: **ACCIÓN** (lo que haces en pantalla), **DECIR** (lo que lees en voz alta, en inglés), **CÓDIGO** (lo que escribes) y **PRUEBA** (lo que deberías ver).

Los nombres de menús y botones están en inglés, tal como aparecen en VS Code en inglés.

**En Mac:** donde dice `Ctrl` usa `Cmd`, donde dice `Alt` usa `Option`, y en el navegador las herramientas de desarrollo se abren con `Cmd + Option + I` en vez de `F12`.

## Regla de oro: nada sin explicar

En la revisión anterior, la mayor parte de lo que hacías en pantalla no estaba explicado. Por eso, en este guion **cada acción tiene su "para qué" dentro del DECIR**. Cada clic, cada comando y cada línea de código.

- **Di la frase mientras haces la acción**, no antes ni mucho después. Si escribes una línea de código, la frase de esa línea va justo ahí.
- **Si haces algo que no está en el guion** (corregir un error de tipeo, cerrar un aviso, mover una ventana), dilo en una frase corta: _"I made a typo, let me fix it."_ / _"I'll close this notification."_
- **En `script.js` y en `eslint.config.mjs` hay una explicación por cada línea de código.** Escribe una línea y di su frase. No escribas varias líneas en silencio.
- Si necesitas tiempo para escribir, puedes quedarte callado mientras tipeas, pero **antes de pasar a la siguiente línea** di la frase de la que acabas de escribir.

## Antes de grabar (no sale en el video)

1. **Node.js:** en VS Code, abre **Terminal → New Terminal** y escribe `node -v`. Tiene que mostrar una versión, por ejemplo `v22.14.0`. Si da error, instala la versión LTS desde https://nodejs.org y reinicia VS Code. Se necesita para instalar ESLint en el paso 11.
2. **Extensiones:** si ya tienes instaladas Live Server, Prettier o ESLint, desinstálalas (engranaje → **Uninstall**) y reinicia VS Code, así en el video aparecen con el botón **Install**.
3. **Carpeta:** no uses la copia de este proyecto que bajaste de GitHub, porque ya tiene los archivos terminados. En el video se crea una carpeta nueva y vacía.

---

## Parte 1 — HTML y Live Server

### Paso 1 — Introducción

**ACCIÓN:** VS Code está abierto en la pestaña de bienvenida (Welcome).

**DECIR:**

> Hi everyone! Today we'll build a registration form from scratch with HTML, CSS, and JavaScript. It will have three fields: name, email, and password. If something is wrong, we'll show an error under the field. If everything is right, we'll show a success message.
>
> We'll write three files: HTML for the structure, CSS for the design, and JavaScript for the functionality. We split them into three files so each one has a single job, and the code is easier to read and change.
>
> And with each file, we'll add one VS Code extension that makes our work easier: Live Server, Prettier, and ESLint. I'll explain each one when we install it.

**CÓDIGO:** Ninguno. **PRUEBA:** Ninguna.

---

### Paso 2 — Abrir la carpeta del proyecto

**ACCIÓN:** **File → Open Folder…** → en el Escritorio, haz clic en **New folder** → llámala `registration-form` → **Select Folder**. Si VS Code pregunta si confías en los autores, haz clic en **Yes, I trust the authors**.

**DECIR:**

> First, I'll go to File, Open Folder, and create a new folder called "registration-form" on my Desktop. I open a whole folder, not a single file, because VS Code treats the folder as our project. That way the Explorer shows all our files together, and the extensions know which files belong to the project.
>
> VS Code asks if I trust the authors. These are my own files, so I'll say yes. If I didn't, VS Code would open in Restricted Mode, and some extensions wouldn't work.
>
> The Explorer on the left is empty, because we start from zero.

**CÓDIGO:** Ninguno.

**PRUEBA:** El Explorer muestra **REGISTRATION-FORM** sin archivos.

---

### Paso 3 — Instalar Live Server

**ACCIÓN:** Abre **Extensions** (`Ctrl + Shift + X`), busca `Live Server`, elige **Live Server** de **Ritwick Dey** y haz clic en **Install**.

**DECIR:**

> Our first extension is Live Server. I'll open the Extensions view with this icon on the left, or with Control, Shift, X, and search for "Live Server".
>
> There are several extensions with similar names, so I'll check the author: Ritwick Dey. That's the original one, with millions of downloads.
>
> Why do we need it? Without it, we would open the HTML file in the browser and press refresh every time we change something. Live Server runs a small web server on our computer, opens the page, and reloads it automatically every time we save a file. Install.

**CÓDIGO:** Ninguno.

**PRUEBA:** La extensión muestra un engranaje en vez de **Install**, y aparece un botón **Go Live** abajo a la derecha, en la barra de estado.

**DECIR (al ver el botón):**

> The extension is installed, and we have a new "Go Live" button at the bottom. We'll use it as soon as we have a page to show.

---

### Paso 4 — index.html: la estructura

**ACCIÓN:** En el Explorer, haz clic en **New File…** y crea `index.html`. Escribe cada bloque y lee el texto que está debajo. Al final, guarda con `Ctrl + S`.

**DECIR (al crear el archivo):**

> Let's create our first file, index.html. The name "index" is a convention: it's the page a web server shows by default.

**CÓDIGO Y DECIR:**

**Bloque 1 de 6** — escribe `!` y pulsa **Tab**: VS Code (Emmet) crea el esqueleto. Después cambia el título y agrega la línea `<link>`. El esqueleto de Emmet puede verse un poco distinto (por ejemplo `<!DOCTYPE html>` en mayúsculas o 4 espacios de sangría); funciona igual.

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

> A quick trick: I type an exclamation mark and press Tab. This is Emmet, a tool built into VS Code, and it writes the basic HTML skeleton for me, so I don't have to type it every time. Let me go through it.
>
> "doctype html" tells the browser this is a modern HTML page. "lang en" says the page is in English, which helps screen readers and search engines. Inside the head, we put information about the page that isn't shown in it. "charset UTF-8" lets the page display any character correctly, like accents. The "viewport" line makes the page fit the width of a phone, instead of showing a tiny desktop version.
>
> I'll change the title to "Registration Form". That's the text on the browser tab. And I'll add a "link" to styles.css, so the page uses our CSS. We'll create that file in a moment.
>
> Everything visible goes inside the body.

**Bloque 2 de 6** — dentro del `<body>`:

```html
    <form id="form" novalidate>
      <h1>Create account</h1>
```

> Inside the body, we add a form. A form element groups the fields and the button, and lets us react when it's submitted. I give it the id "form", so JavaScript can find it later.
>
> "novalidate" turns off the browser's own validation. Each browser shows its own popup messages, and they look different everywhere. We want our own messages, under each field, so our JavaScript will do the checking.
>
> And a heading, "h1", so the user knows what this form is for: "Create account".

**Bloque 3 de 6:**

```html
      <label for="name">Name</label>
      <input id="name" type="text" />
      <small id="name-error"></small>
```

> Each field has three parts. First, a label, the text the user sees. Its "for" attribute matches the input's id. That connects them: clicking the label puts the cursor in the field, and screen readers read the label aloud.
>
> Then the input itself, type "text", where the user writes the name. Its id, "name", is how JavaScript will find it.
>
> And an empty "small" element. It's empty on purpose: that's where we'll show the error message. Notice its id: "name-error", the field's id plus "-error". JavaScript will use that naming rule to find it.

**Bloque 4 de 6:**

```html
      <label for="email">Email</label>
      <input id="email" type="email" />
      <small id="email-error"></small>

      <label for="password">Password</label>
      <input id="password" type="password" />
      <small id="password-error"></small>
```

> The email and password fields follow exactly the same pattern: "email" and "email-error", "password" and "password-error". Keeping the same pattern is what lets one piece of JavaScript handle all three fields.
>
> The type "email" shows the at sign key on phone keyboards. The type "password" hides what the user types with dots, so nobody can read it over their shoulder.

**Bloque 5 de 6:**

```html
      <button type="submit">Sign up</button>
      <p id="success" hidden>Registration successful!</p>
    </form>
```

> Then the button. Type "submit" means that clicking it submits the form. That's the event our JavaScript will listen for.
>
> And the success message, with the id "success" so JavaScript can find it. It has the "hidden" attribute, so it's invisible for now. We only want to show it after a valid registration.
>
> Then we close the form.

**Bloque 6 de 6** — antes de `</body>`. Las etiquetas `</body>` y `</html>` ya las creó Emmet en el bloque 1.

```html
    <script src="script.js"></script>
  </body>
</html>
```

> Finally, before closing the body, we load script.js. We put it at the end on purpose. The browser reads the page from top to bottom, so by the time it reaches the script, the whole form already exists, and JavaScript can find every element.
>
> I'll save with Control S. The white dot on the tab disappears, which means the file is saved.

**PRUEBA:** La pestaña `index.html` no muestra el punto blanco, o sea que está guardado.

---

### Paso 5 — Probar Live Server

**ACCIÓN:** Con `index.html` guardado, haz clic en **Go Live**, abajo a la derecha en la barra de estado.

**DECIR:**

> Now let's try Live Server, to check our HTML. I'll click "Go Live" at the bottom of VS Code, and our page opens in the browser.
>
> Look at the address: 127.0.0.1, port 5500. That's a local server running on my own computer. Nobody else can see it, it's just for development.
>
> The page is very plain, because we don't have any CSS yet. But all the parts are there: the heading, three fields, and the button. The success message doesn't show, because it's hidden. From now on, every time I save a file, the browser will update by itself.

**CÓDIGO:** Ninguno.

**PRUEBA:** El navegador abre `http://127.0.0.1:5500/index.html` con la página sin estilos, y el botón de abajo ahora dice **Port : 5500**.

---

## Parte 2 — CSS y Prettier

### Paso 6 — Instalar Prettier

**ACCIÓN:** Vuelve a VS Code. En **Extensions**, busca `Prettier`, elige **Prettier - Code formatter** de **Prettier** y haz clic en **Install**.

**DECIR:**

> Back in VS Code. Before we write the CSS, let's add our second extension: Prettier. I'll install it now, before writing the code, so I can use it on the CSS right away. I'll search for "Prettier" and choose "Prettier - Code formatter". The author is Prettier itself, the official one.
>
> Prettier is a code formatter. When we write fast, the code gets messy: missing spaces, wrong indentation, everything on one line. Prettier fixes all of that with one shortcut, so our code always looks clean and consistent, and we don't waste time fixing spaces by hand. Install.

**CÓDIGO:** Ninguno.

**PRUEBA:** La extensión muestra un engranaje en vez de **Install**.

---

### Paso 7 — styles.css: el diseño

**ACCIÓN:** Crea `styles.css`. Escribe cada bloque y lee el texto que está debajo. Al final, guarda y mira el navegador.

**DECIR (al crear el archivo):**

> Now I'll create styles.css. The name must match the "link" we wrote in the HTML head, or the page won't find it.

**CÓDIGO Y DECIR:**

**Bloque 1 de 3:**

```css
form {
  display: grid;
  gap: 6px;
  max-width: 300px;
  margin: 40px auto;
  font-family: Arial, sans-serif;
}
```

> We only need three rules. The first one styles the form.
>
> "display: grid" puts each label, field, and message one below the other, in a single column. "gap: 6px" adds a small space between them, so they don't touch.
>
> "max-width: 300px" keeps the form narrow, because a very wide form is hard to read. "margin: 40px auto" adds 40 pixels of space on top and bottom, and "auto" on the sides centers the form on the page.
>
> Because we use max-width instead of a fixed width, the form is also responsive: on a phone, it simply uses the available width.
>
> Last, "font-family" changes the default font to Arial, which is cleaner. "sans-serif" is a backup, in case Arial isn't installed.

**Bloque 2 de 3:**

```css
input.invalid {
  border: 2px solid red;
}
```

> The second rule is for inputs with the class "invalid". It gives them a red border, two pixels thick, so the user sees right away which field has a problem. No field has this class yet. JavaScript will add it when a field is wrong, and remove it when it's fixed.

**Bloque 3 de 3:**

```css
small {
  color: red;
}
```

> The third rule makes the error messages red. They live in the "small" elements we created under each field, so the color matches the red border.
>
> I'll save, and look at the browser: it updated by itself, without pressing refresh. That's Live Server working. Now the form is centered, narrow, and in Arial.

**PRUEBA:** Sin recargar, el navegador muestra el formulario centrado, con cada campo debajo de su etiqueta y la letra Arial.

---

### Paso 8 — Probar Prettier

**ACCIÓN:**

1. En `styles.css`, selecciona la regla `input.invalid` (líneas 9 a 11) y escríbela de nuevo en una sola línea, así: `input.invalid{border:2px solid red}`.
2. **Elige Prettier como formateador (solo la primera vez):** clic derecho dentro del código → **Format Document With…** → en la lista de arriba, **Configure Default Formatter…** → **Prettier - Code formatter**. Este paso solo elige Prettier: **todavía no formatea**.
3. **Formatea:** pulsa `Shift + Option + F` (en Windows, `Shift + Alt + F`). Ahora sí la regla vuelve a ocupar 3 líneas.
4. Guarda con `Cmd + S`.

**Si no funciona (revísalo antes de grabar, en Mac):**

- **Prettier está activado:** abajo a la derecha, en la barra de estado, tiene que aparecer **{ } Prettier** con una tilde (✓). Si tiene una ✗ o un aviso, haz clic ahí para ver el error.
- **La extensión no está desactivada:** `Cmd + Shift + X` → **Prettier - Code formatter**. Si hay un botón **Enable**, haz clic en él.
- **Formatear directo con Prettier:** clic derecho → **Format Document With…** → elige **Prettier - Code formatter**, no la opción "Configure…". Esto formatea aunque Prettier no esté elegido por defecto.
- **Revisa los ajustes:** `Cmd + ,` para abrir **Settings**.
  - Busca `default formatter` y elige **Prettier - Code formatter**.
  - Busca `prettier require config`: la casilla tiene que estar **desmarcada**. Si está marcada, Prettier no formatea porque el proyecto no tiene archivo de configuración.
- **Recarga VS Code:** `Cmd + Shift + P` → `Developer: Reload Window`.

**DECIR:**

> Now let's try Prettier. To test it, I need messy code, so I'll make some on purpose. I'll write this rule on one line, with no spaces. The browser still understands it, but it's hard for a person to read.
>
> VS Code can have more than one formatter installed, so the first time, we have to tell it which one to use. Right-click, "Format Document With", "Configure Default Formatter", and Prettier. This only chooses Prettier. It doesn't format anything yet.
>
> Now I'll press Shift, Option, and F, which is "Format Document". And there it is: Prettier puts the rule back on three clean lines, with the right spaces and indentation. From now on, I just use that shortcut. I'll save.

**CÓDIGO:** Solo el cambio de la regla, que Prettier corrige.

**PRUEBA:** La regla vuelve a ocupar tres líneas:

```css
input.invalid {
  border: 2px solid red;
}
```

---

## Parte 3 — JavaScript y ESLint

### Paso 9 — script.js: la funcionalidad, línea por línea

**ACCIÓN:** Crea `script.js`. **Escribe una línea, di su frase, y recién entonces pasa a la siguiente.** Las líneas vacías no se explican; solo pulsa Enter. Al final, guarda con `Ctrl + S`.

**Ojo con el autocompletado:** cuando escribes `{`, `(` o `[`, VS Code agrega solo el cierre (`}`, `)`, `]`). No lo borres: sigue escribiendo adentro. Cuando llegues a una línea de cierre que VS Code ya escribió (por ejemplo, la línea 24), **no la escribas de nuevo**: pon el cursor ahí y di su frase.

**DECIR (al crear el archivo):**

> Finally, script.js, the same name we used in the script tag in the HTML. This file makes the form work. I'll explain every line as I write it.

**CÓDIGO Y DECIR (una frase por línea):**

---

**Línea 1**

```js
const form = document.getElementById("form");
```

> First, we need to find the form on the page. "document" is the whole page, and "getElementById" finds the element with the id "form", the one we wrote in the HTML. We save it in a constant called "form", so we don't have to search for it again.

**Línea 2**

```js
const success = document.getElementById("success");
```

> Same thing for the success message: we find the element with the id "success" and save it, because we'll show or hide it later.

**Línea 3** — vacía. Solo pulsa Enter.

**Línea 4**

```js
const rules = {
```

> Now our validation rules. I'll put them all together in one object called "rules", so they're easy to find and change in one place.

**Línea 5**

```js
  name: [(v) => v.trim().length >= 2, "Min. 2 characters."],
```

> The first rule is for the name field. The key "name" matches the input's id. The value is a list with two things. First, a small function that receives the value, "v", and returns true if it's valid. Here, "trim" removes spaces at the start and the end, so a name made of only spaces doesn't count, and then we check it has at least 2 characters. Second, the error message to show if the test fails.

**Línea 6**

```js
  email: [(v) => v.includes("@"), "Invalid email"],
```

> The rule for email: the value must include an at sign. It's a simple check, just enough to catch obvious mistakes. A real app would also confirm the email by sending a message to it.

**Línea 7**

```js
  password: [(v) => v.length >= 8, "Min. 8 characters."],
```

> And the rule for the password: at least 8 characters. Here we don't use "trim", because spaces can be part of a password.

**Línea 8**

```js
};
```

> And we close the rules object. If we want a new field later, we just add one line inside it.

**Línea 9** — vacía. Solo pulsa Enter.

**Línea 10** — VS Code agrega solo `});` (será la línea 24). Sigue escribiendo adentro.

```js
form.addEventListener("submit", (event) => {
```

> Now we tell the form what to do when it's submitted. "addEventListener" means: when this event happens, run this function. The event is "submit", which happens when the user clicks Sign up or presses Enter. The function receives an "event" object with information about what happened.

**Línea 11**

```js
  event.preventDefault();
```

> By default, submitting a form sends the data and reloads the page. We don't want that, because we would lose our error messages. "preventDefault" stops it, so we can check the data first.

**Línea 12** — vacía. Solo pulsa Enter.

**Línea 13**

```js
  const ok = Object.entries(rules)
```

> Now we check all the fields. The final result, true or false, will go in a constant called "ok". "Object.entries" turns our rules object into a list of pairs: the field id, and its test with its message. That way we can go through them one by one.

**Línea 14**

```js
    .map(([id, [test, message]]) => {
```

> "map" runs a function for each pair, and collects the results in a new list. In the parentheses, we unpack each pair into three names: the "id", the "test" function, and the error "message". That makes the next lines easier to read.

**Línea 15**

```js
      const valid = test(form.elements[id].value);
```

> "form.elements" lets us find any field of the form by its id. We take what the user typed, its "value", and run the test on it. The answer, true or false, goes in "valid".

**Línea 16**

```js
      form.elements[id].classList.toggle("invalid", !valid);
```

> Now we update the red border. "classList.toggle" adds or removes a CSS class. The second part decides which: "not valid". If the field is not valid, it adds the "invalid" class, and our CSS paints the border red. If it's valid, it removes the class, so the red border goes away after the user fixes it.

**Línea 17**

```js
      document.getElementById(id + "-error").textContent = valid ? "" : message;
```

> Next, the error message. We find the error element by adding "-error" to the id. That's the naming rule from our HTML, like "name-error". Then we set its text. The question mark is a short "if": if the field is valid, an empty text, so the old error disappears; if not, the error message.

**Línea 18**

```js
      return valid;
```

> We return true or false for this field, so "map" can add it to its list of results.

**Línea 19**

```js
    })
```

> And we close the function that checks one field. At this point, "map" gives us a list like true, false, true.

**Línea 20**

```js
    .every(Boolean);
```

> "every" checks if all the values in that list are true. If even one field failed, "ok" is false.
>
> Why "map" first, and not "every" directly? Because "every" stops at the first false. With "map", every field gets checked and shows its own error, even when the first one is wrong.

**Línea 21** — vacía. Solo pulsa Enter.

**Línea 22**

```js
  success.hidden = !ok;
```

> Now the success message. Its "hidden" property is the opposite of "ok". If everything is OK, hidden becomes false, so the message appears. If there are errors, it stays hidden.

**Línea 23**

```js
  if (ok) form.reset();
```

> And if everything is OK, "reset" empties all the fields, so the form is ready for the next person.

**Línea 24** — ya la escribió VS Code. Pon el cursor ahí y di:

```js
});
```

> This last line, which VS Code wrote for us, closes the submit function and the "addEventListener" call. I'll save the file.

---

**PRUEBA:** El archivo está guardado y tiene 24 líneas. El formulario se prueba completo en el paso 13.

**DECIR (después de guardar):**

> The JavaScript is done. Before testing the form, let's add our last extension, to check this code for mistakes.

---

### Paso 10 — Instalar la extensión de ESLint

**ACCIÓN:** En **Extensions**, busca `ESLint`, elige **ESLint** de **Microsoft** y haz clic en **Install**.

**DECIR:**

> Our last extension is ESLint, by Microsoft. ESLint is a linter. It reads our JavaScript without running it and finds real mistakes, like a misspelled variable or a variable we created and never used. It's better to find those mistakes now, in the editor, than later, when a user finds them in the browser. Install.
>
> ESLint works differently from Prettier. This extension only connects VS Code to ESLint. The ESLint program itself, and its rules, are installed inside our project. That way, everyone who works on the project uses the same version and the same rules. Let's do that now.

**CÓDIGO:** Ninguno.

**PRUEBA:** La extensión muestra un engranaje en vez de **Install**.

---

### Paso 11 — Instalar ESLint en el proyecto

**ACCIÓN Y DECIR:**

**1.** Abre **Terminal → New Terminal** y escribe:

```
pwd
```

> I'll open a terminal inside VS Code, with Terminal, New Terminal. The next command installs ESLint in the current folder, so first I'll check where I am with "pwd", which means "print working directory". It ends in registration-form, so we're in the right place.

**2.** Instala ESLint en el proyecto. Se crean `package.json`, `package-lock.json` y la carpeta `node_modules`.

```
npm install --save-dev eslint@9
```

> Now I'll install ESLint with npm, the package manager that comes with Node.js. "eslint@9" asks for version 9, because our configuration file uses the version 9 format. "save-dev" means it's a tool for development, not part of the website. Users never download it.
>
> Three new things appear in the Explorer. "package.json" lists the tools our project uses. "package-lock.json" records the exact versions, so everyone gets the same ones. And "node_modules" holds the actual code of ESLint.

**3.** Comprueba la versión:

```
npx eslint -v
```

> Let me check that it works. "npx" runs the ESLint we just installed in this project, not a global one. It shows version [read the version on screen], so the installation worked.

**4.** En el Explorer, crea `eslint.config.mjs` junto a `package.json` (no dentro de `node_modules`). El formato es el de la documentación oficial de ESLint: https://eslint.org/docs/latest/use/configure/configuration-files

**Igual que en `script.js`: escribe una línea, di su frase, y recién entonces pasa a la siguiente.** Las líneas vacías no se explican; solo pulsa Enter.

**Ojo con el autocompletado:** cuando escribes `{`, `(` o `[`, VS Code agrega solo el cierre. Al pulsar Enter, el cierre baja a la línea de abajo. Cuando llegues a una línea de cierre que ya está escrita (líneas 9, 13, 14 y 15), **no la escribas de nuevo**: pon el cursor al final, **agrega la coma si la línea la lleva** (VS Code no la pone) y di su frase.

El archivo completo, para que lo compares al final:

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

**DECIR (al crear el archivo):**

> Right now ESLint is installed, but it doesn't know which rules to use. So I'll create its configuration file, "eslint.config.mjs", next to package.json. This is the file name ESLint looks for. The "mjs" ending means this file is a JavaScript module, so we can use "import" and "export" in it. I'll follow the format from the official ESLint docs, and explain every line.

**CÓDIGO Y DECIR (una frase por línea):**

---

**Línea 1**

```js
import { defineConfig } from "eslint/config";
```

> First, we import "defineConfig" from ESLint, the package we just installed. It's a helper that wraps our configuration. It doesn't change any rules, but it lets VS Code suggest the right options and catch typos while we write this file.

**Línea 2** — vacía. Solo pulsa Enter.

**Línea 3** — VS Code agrega solo `])`. Sigue escribiendo adentro.

```js
export default defineConfig([
```

> "export default" is how this file hands its configuration to ESLint. When ESLint starts, it reads whatever we export here. Inside defineConfig we open a list, with square brackets, because a configuration can have several blocks, for example different rules for different files. We only need one.

**Línea 4** — VS Code agrega solo `}`.

```js
  {
```

> The curly brace opens our only configuration block. Everything inside applies to the same group of files.

**Línea 5**

```js
    files: ["**/*.js"],
```

> "files" says which files this block checks. The two stars mean "any folder", and star dot js means "any file that ends in dot js". So it checks our script.js, and any JavaScript file we add later.

**Línea 6** — VS Code agrega solo `}`.

```js
    languageOptions: {
```

> "languageOptions" describes how our JavaScript runs, so ESLint understands it correctly.

**Línea 7**

```js
      sourceType: "script",
```

> "sourceType script" says our script.js is a normal browser script, because we load it with a plain script tag in the HTML, not as a module. This matters because scripts and modules follow slightly different rules.

**Línea 8**

```js
      globals: { document: "readonly" },
```

> "globals" lists variables that exist without us creating them. In the browser, "document" always exists, but ESLint doesn't know that. Without this line, the "no-undef" rule would report "document" as a mistake. "readonly" means we only read it, we never replace it.

**Línea 9** — ya está escrita. Agrega la coma al final y di:

```js
    },
```

> This closes the language options. The comma is there because another option comes next.

**Línea 10** — VS Code agrega solo `}`.

```js
    rules: {
```

> Now the most important part: "rules", the list of problems we want ESLint to look for.

**Línea 11**

```js
      "no-undef": "error",
```

> "no-undef" means "no undefined variables". It reports any variable that doesn't exist, which usually means a typo. We set it to "error", because that code would break in the browser.

**Línea 12**

```js
      "no-unused-vars": "warn",
```

> "no-unused-vars" reports variables we create but never use. That's not a bug, just leftover code, so a warning is enough. Errors show up in red, warnings in yellow.

**Línea 13** — ya está escrita. Agrega la coma al final y di:

```js
    },
```

> This closes the rules.

**Línea 14** — ya está escrita. Agrega la coma al final y di:

```js
  },
```

> This closes our configuration block.

**Línea 15** — ya está escrita. Agrega el punto y coma al final y di:

```js
]);
```

> And this closes the list and the defineConfig call. I'll save the file. If I want more rules later, I just add more lines inside "rules".

**5.** `Ctrl + Shift + P` → `ESLint: Restart ESLint Server` → Enter.

> The extension started before this file existed, so it doesn't know about it yet. I'll open the Command Palette with Control, Shift, P, and run "ESLint: Restart ESLint Server", so it reads the new configuration.

**PRUEBA:**

- `pwd` termina en `registration-form`.
- `npx eslint -v` muestra una versión que empieza con `v9`, por ejemplo `v9.39.5`.
- El Explorer muestra `eslint.config.mjs` junto a `package.json`.
- Si el comando **ESLint: Restart ESLint Server** no aparece, la extensión no está instalada o está desactivada: vuelve al paso 10.

---

### Paso 12 — Probar ESLint

**ACCIÓN:**

1. En la terminal, revisa el archivo:

   ```
   npx eslint script.js
   ```

2. En `script.js`, agrega esta línea al final del archivo (línea 25) y guarda:

   ```js
   nmae;
   ```

3. Mira el subrayado rojo y pasa el mouse encima. Vuelve a ejecutar `npx eslint script.js`.
4. Borra la línea `nmae;`, guarda y ejecuta `npx eslint script.js` una última vez.

**DECIR:**

> Let's try ESLint. First, I'll check our real code, to make sure it's clean before we break anything. In the terminal, I'll run "npx eslint script.js". No output, which means ESLint didn't find any problems. Silence is good news.
>
> To see ESLint catch a problem, I need a mistake, so I'll make a typical one on purpose. At the end of the file, I'll write "nmae", a misspelled version of "name", and save. Right away, ESLint underlines it in red. When I hover over it, it says: "'nmae' is not defined". That variable doesn't exist, and this is the "no-undef" rule we configured.
>
> I'll run ESLint in the terminal again. It shows the same thing: line 25, an error, the message, and the rule name, "no-undef". The editor and the terminal agree. ESLint found the bug without even running the code.
>
> Notice that Prettier didn't complain. The line is well formatted, just wrong. That's the difference: Prettier checks how the code looks, and ESLint checks if it makes sense.
>
> The test is done, so I'll delete the line, save, and run ESLint one last time, to confirm we left the code clean. No output, so our code is clean.

**PRUEBA:**

- La primera vez, `npx eslint script.js` no muestra nada.
- Con `nmae;`, aparece un subrayado **rojo** que dice `'nmae' is not defined.`, y la terminal muestra:

  ```
  25:1  error  'nmae' is not defined  no-undef

  ✖ 1 problem (1 error, 0 warnings)
  ```

- Después de borrar la línea, `npx eslint script.js` vuelve a no mostrar nada.
- Si no aparece el subrayado en el editor, ejecuta otra vez **ESLint: Restart ESLint Server** y revisa **View → Output → ESLint**.

---

## Parte 4 — El proyecto funcionando

### Paso 13 — Probar el formulario

**ACCIÓN:**

1. En el navegador, recarga la página con `F5`.
2. Haz clic en **Sign up** con todos los campos vacíos.
3. Escribe `J`, `jane` y `abc`, y haz clic en **Sign up**.
4. Escribe `Jane`, `jane@example.com` y `secret123`, y haz clic en **Sign up**.
5. Pulsa `F12`, luego `Ctrl + Shift + M`, y elige un tamaño de celular. Después cierra las herramientas de desarrollo.

**DECIR:**

> Now let's see the whole project working. I'll press F5 to reload the page once, so we start from a clean state with the latest JavaScript.
>
> I'll test three cases: empty fields, wrong values, and valid values. That way we see every path in our code.
>
> First, I'll click Sign up with everything empty. Three red borders and three error messages. The page didn't reload, thanks to "preventDefault", and every field shows its error, thanks to "map".
>
> Now wrong values: one letter for the name, an email without an at sign, and a short password. Still three errors, because none of them follow the rules.
>
> And now valid values: "Jane", "jane@example.com", and "secret123". The red borders and the errors disappear, the form is cleared by "reset", and we see "Registration successful!".
>
> Last, many people will fill in this form on a phone, so I'll check that too. I'll open the developer tools with F12, and turn on the device toolbar with Control, Shift, M, to simulate a phone screen. The form fills the width and still looks good, thanks to "max-width" in our CSS. I'll close the developer tools.

**PRUEBA:**

| Datos | Resultado |
| ----- | --------- |
| Campos vacíos | Bordes rojos y los mensajes _Min. 2 characters._, _Invalid email_, _Min. 8 characters._ |
| `J`, `jane`, `abc` | Los mismos tres errores |
| `Jane`, `jane@example.com`, `secret123` | Sin errores, campos vacíos y el mensaje _Registration successful!_ |
| Vista de celular | El formulario usa el ancho de la pantalla, hasta 300 píxeles |

---

### Paso 14 — Cierre

**DECIR:**

> And that's it! With three short files, we built a working registration form: HTML for the structure, CSS for the design, and JavaScript for the validation.
>
> And with each file, we used one extension: Live Server to see our changes instantly, Prettier to keep the code clean, and ESLint to catch real mistakes before they reach the browser.
>
> Thanks for watching!

**ACCIÓN:** Detén la grabación.
