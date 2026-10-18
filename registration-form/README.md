# Formulario de registro — Guion de narración

Un video corto de programación en vivo. Escribes un formulario de registro en tres archivos y, en cada uno, instalas y pruebas una extensión de VS Code:

1. **HTML** (`index.html`) → **Live Server**
2. **CSS** (`styles.css`) → **Prettier**
3. **JavaScript** (`script.js`) → **ESLint**

Al final muestras el proyecto funcionando.

Cada paso tiene: **ACCIÓN** (lo que haces en pantalla), **DECIR** (lo que lees en voz alta, en inglés), **CÓDIGO** (lo que escribes) y **PRUEBA** (lo que deberías ver).

Los nombres de menús y botones están en inglés, tal como aparecen en VS Code en inglés.

**En Mac:** donde dice `Ctrl` usa `Cmd`, donde dice `Alt` usa `Option`, y en el navegador las herramientas de desarrollo se abren con `Cmd + Option + I` en vez de `F12`.

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
> We'll write three files: HTML for the structure, CSS for the design, and JavaScript for the functionality. And with each file, we'll add one VS Code extension that makes our work easier: Live Server, Prettier, and ESLint.

**CÓDIGO:** Ninguno. **PRUEBA:** Ninguna.

---

### Paso 2 — Abrir la carpeta del proyecto

**ACCIÓN:** **File → Open Folder…** → en el Escritorio, haz clic en **New folder** → llámala `registration-form` → **Select Folder**. Si VS Code pregunta si confías en los autores, haz clic en **Yes, I trust the authors**.

**DECIR:**

> I'll go to File, Open Folder, create a new folder called "registration-form" on my Desktop, and open it. The Explorer on the left is empty, because we start from zero.

**CÓDIGO:** Ninguno.

**PRUEBA:** El Explorer muestra **REGISTRATION-FORM** sin archivos.

---

### Paso 3 — Instalar Live Server

**ACCIÓN:** Abre **Extensions** (`Ctrl + Shift + X`), busca `Live Server`, elige **Live Server** de **Ritwick Dey** y haz clic en **Install**.

**DECIR:**

> Our first extension is Live Server. I'll open the Extensions view with this icon on the left and search for "Live Server", by Ritwick Dey.
>
> Live Server opens our page in the browser, and reloads it automatically every time we save a file. We don't have to switch windows and press refresh again and again. Install.

**CÓDIGO:** Ninguno.

**PRUEBA:** La extensión muestra un engranaje en vez de **Install**, y aparece un botón **Go Live** abajo a la derecha, en la barra de estado.

---

### Paso 4 — index.html: la estructura

**ACCIÓN:**

1. En el Explorer, haz clic en **New File…** y crea `index.html`.
2. Escribe `!` y pulsa **Tab**. VS Code (Emmet) crea el esqueleto básico de HTML.
3. Cambia el título a `Registration Form`, agrega la línea `<link>` y escribe el contenido del `<body>`. Guarda con `Ctrl + S`.

**CÓDIGO — `index.html`:**

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
    <form id="form" novalidate>
      <h1>Create account</h1>

      <label for="name">Name</label>
      <input id="name" type="text" />
      <small id="name-error"></small>

      <label for="email">Email</label>
      <input id="email" type="email" />
      <small id="email-error"></small>

      <label for="password">Password</label>
      <input id="password" type="password" />
      <small id="password-error"></small>

      <button type="submit">Sign up</button>
      <p id="success" hidden>Registration successful!</p>
    </form>

    <script src="script.js"></script>
  </body>
</html>
```

**DECIR:**

> Let's create index.html. A quick trick: I type an exclamation mark and press Tab, and VS Code writes the basic HTML skeleton for me. I'll change the title and link our stylesheet, styles.css.
>
> In the body, we add a form. The word "novalidate" turns off the browser's own validation, because our JavaScript will do it.
>
> Each field has three parts: a label, an input, and an empty "small" element for the error message. Notice the ids: "name" and "name-error", "email" and "email-error". Our JavaScript will use these names to find each error.
>
> Then a button, and a success message with the "hidden" attribute, so it's invisible for now. At the end, we load script.js.

**PRUEBA:** La pestaña `index.html` no muestra el punto blanco, o sea que está guardado.

---

### Paso 5 — Probar Live Server

**ACCIÓN:** Con `index.html` guardado, haz clic en **Go Live**, abajo a la derecha en la barra de estado.

**DECIR:**

> Now let's try Live Server. I'll click "Go Live" at the bottom of VS Code, and our page opens in the browser. It's very plain, because we don't have any CSS yet. From now on, every time I save a file, the browser will update by itself.

**CÓDIGO:** Ninguno.

**PRUEBA:** El navegador abre `http://127.0.0.1:5500/index.html` con la página sin estilos, y el botón de abajo ahora dice **Port : 5500**.

---

## Parte 2 — CSS y Prettier

### Paso 6 — Instalar Prettier

**ACCIÓN:** En **Extensions**, busca `Prettier`, elige **Prettier - Code formatter** de **Prettier** y haz clic en **Install**.

**DECIR:**

> Before we write the CSS, let's add our second extension: Prettier. I'll search for "Prettier" and choose "Prettier - Code formatter".
>
> Prettier is a code formatter. It fixes spaces, indentation, and quotes with one shortcut, so our code always looks clean and consistent. We'll see it in action in a moment. Install.

**CÓDIGO:** Ninguno.

**PRUEBA:** La extensión muestra un engranaje en vez de **Install**.

---

### Paso 7 — styles.css: el diseño

**ACCIÓN:** Crea `styles.css`, escribe el código de abajo y guarda. Mira el navegador.

**CÓDIGO — `styles.css`:**

```css
body {
  margin: 0;
  min-height: 100vh;
  display: grid;
  place-items: center;
  font-family: Arial, sans-serif;
  background: #eef2ff;
}

form {
  display: grid;
  gap: 6px;
  width: 90%;
  max-width: 360px;
  padding: 24px;
  background: white;
  border-radius: 10px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}

h1 {
  margin: 0 0 10px;
  text-align: center;
}

input {
  padding: 10px;
  border: 2px solid #ccc;
  border-radius: 6px;
}

input.invalid {
  border-color: #dc2626;
}

small {
  min-height: 16px;
  color: #dc2626;
}

button {
  padding: 12px;
  border: none;
  border-radius: 6px;
  color: white;
  background: #4f46e5;
  cursor: pointer;
}

#success {
  color: #16a34a;
  font-weight: bold;
  text-align: center;
}
```

**DECIR:**

> Now styles.css. For the body, "display: grid" and "place-items: center" put our form right in the middle of the screen.
>
> The form is a white card. Its width is 90 percent, but never more than 360 pixels. That makes it responsive: it fills a phone screen, and stays small on a big screen.
>
> The inputs get padding and a gray border. The class "invalid" turns the border red. JavaScript will add that class when a field is wrong. The error text is red, and the success message is green.
>
> I'll save, and look at the browser: it updated by itself. That's Live Server again.

**PRUEBA:** Sin recargar, el navegador muestra una tarjeta blanca centrada con un botón azul.

---

### Paso 8 — Probar Prettier

**ACCIÓN:**

1. En `styles.css`, selecciona la regla `input.invalid` (líneas 32 a 34) y escríbela de nuevo en una sola línea, así: `input.invalid{border-color:#dc2626}`.
2. Haz clic derecho en el código → **Format Document With…** → **Configure Default Formatter…** → **Prettier - Code formatter**. Esto se hace solo la primera vez.
3. Guarda con `Ctrl + S`. A partir de ahora, alcanza con pulsar `Shift + Alt + F`.

**DECIR:**

> Now let's try Prettier. I'll write this rule on one messy line, with no spaces. It still works, but it's hard to read.
>
> The first time, we tell VS Code to use Prettier: right-click, "Format Document With", "Configure Default Formatter", and Prettier. And there it is: Prettier puts the rule back on three clean lines. From now on, I just press Shift, Alt, and F.

**CÓDIGO:** Solo el cambio de la regla, que Prettier corrige.

**PRUEBA:** La regla vuelve a ocupar tres líneas:

```css
input.invalid {
  border-color: #dc2626;
}
```

---

## Parte 3 — JavaScript y ESLint

### Paso 9 — script.js: la funcionalidad

**ACCIÓN:** Crea `script.js`, escribe el código de abajo y guarda.

**CÓDIGO — `script.js`:**

```js
const form = document.getElementById("form");
const success = document.getElementById("success");

function check(id, isValid, message) {
  const input = document.getElementById(id);
  const error = document.getElementById(id + "-error");
  input.classList.toggle("invalid", !isValid);
  error.textContent = isValid ? "" : message;
  return isValid;
}

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const pass = document.getElementById("password").value;

  const okName = check("name", name.length >= 2, "Min. 2 characters.");
  const okEmail = check("email", email.includes("@"), "Invalid email");
  const okPass = check("password", pass.length >= 8, "Min. 8 characters.");

  success.hidden = !(okName && okEmail && okPass);
  if (!success.hidden) {
    form.reset();
  }
});
```

**DECIR:**

> Finally, script.js. First, we get the form and the success message from the page.
>
> Then one small function, "check", that we'll use for every field. It receives the field's id, whether the value is valid, and an error message. It finds the input and its error element, using the "-error" names from our HTML. If the value is not valid, it adds the red "invalid" class and shows the message. If it is valid, it removes the class and clears the message. And it returns the result.
>
> Next, we listen for the form's "submit" event. "preventDefault" stops the page from reloading. Then we read the three values. "trim" removes extra spaces.
>
> Now our three rules: the name needs at least 2 characters, the email must contain an at sign, and the password needs at least 8 characters.
>
> Last, the success message. It's visible only if all three checks are OK. And when everything is valid, we clear the form.

**PRUEBA:** El archivo está guardado. El formulario se prueba completo en el paso 13.

---

### Paso 10 — Instalar la extensión de ESLint

**ACCIÓN:** En **Extensions**, busca `ESLint`, elige **ESLint** de **Microsoft** y haz clic en **Install**.

**DECIR:**

> Our last extension is ESLint, by Microsoft. ESLint is a linter. It reads our JavaScript without running it and finds real mistakes, like a misspelled variable. Install.
>
> ESLint is different from Prettier. The extension only connects VS Code to ESLint. The ESLint program itself, and its rules, are installed in our project. Let's do that now.

**CÓDIGO:** Ninguno.

**PRUEBA:** La extensión muestra un engranaje en vez de **Install**.

---

### Paso 11 — Instalar ESLint en el proyecto

**ACCIÓN:**

1. Abre **Terminal → New Terminal** y escribe `pwd`. La ruta tiene que terminar en `registration-form`.
2. Instala ESLint en el proyecto:

   ```
   npm install --save-dev eslint@9
   ```

   Se crean `package.json`, `package-lock.json` y la carpeta `node_modules`.

3. Comprueba la versión:

   ```
   npx eslint -v
   ```

4. En el Explorer, crea `eslint.config.mjs` junto a `package.json`, escribe el código de abajo y guarda.
5. `Ctrl + Shift + P` → `ESLint: Restart ESLint Server` → Enter.

**CÓDIGO — `eslint.config.mjs`:**

```js
export default [
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
];
```

**DECIR:**

> I'll open the terminal and check that I'm in the project folder, with "pwd". Then I'll install ESLint in the project with "npm install --save-dev eslint@9". "Save-dev" means it's a tool for development, not part of the website.
>
> Let me check that it works with "npx eslint -v". It shows version 9.
>
> Now ESLint needs its rules. I'll create a file called "eslint.config.mjs". This is ESLint's configuration file. We turn on two rules: "no-undef" gives an error when we use a variable that doesn't exist, and "no-unused-vars" warns us about variables we never use. We also tell ESLint that our code runs in the browser, where "document" always exists.
>
> Finally, I'll restart the ESLint server, so the extension picks up the new configuration.

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

2. En `script.js`, agrega esta línea al final del archivo (línea 28) y guarda:

   ```js
   nmae;
   ```

3. Mira el subrayado rojo y pasa el mouse encima. Vuelve a ejecutar `npx eslint script.js`.
4. Borra la línea `nmae;`, guarda y ejecuta `npx eslint script.js` una última vez.

**DECIR:**

> Let's try ESLint. In the terminal, I'll run "npx eslint script.js". No output, which means ESLint didn't find any problems. Silence is good news.
>
> Now I'll make a typical mistake on purpose. At the end of the file, I'll write "nmae", a misspelled version of "name". Right away, ESLint underlines it in red, and when I hover over it, it says: "'nmae' is not defined". That variable doesn't exist.
>
> In the terminal, ESLint shows the same thing: line 28, an error, the message, and the rule name, "no-undef". ESLint found the bug without even running the code.
>
> Notice that Prettier didn't complain. The line is well formatted, just wrong. Prettier checks how the code looks, and ESLint checks if it makes sense.
>
> I'll delete the line, save, and run ESLint again. No output, so our code is clean.

**PRUEBA:**

- La primera vez, `npx eslint script.js` no muestra nada.
- Con `nmae;`, aparece un subrayado **rojo** que dice `'nmae' is not defined.`, y la terminal muestra:

  ```
  28:1  error  'nmae' is not defined  no-undef

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

> Now let's see the whole project working. First, I'll click Sign up with everything empty. Three red borders and three error messages.
>
> Now wrong values: one letter, an email without an at sign, and a short password. Still three errors, because none of them follow the rules.
>
> And now valid values: "Jane", "jane@example.com", and "secret123". The errors disappear, the form is cleared, and we see "Registration successful!" in green.
>
> Last, on a phone-sized screen, the form fills the width and still looks good.

**PRUEBA:**

| Datos | Resultado |
| ----- | --------- |
| Campos vacíos | Bordes rojos y los mensajes _Min. 2 characters._, _Invalid email_, _Min. 8 characters._ |
| `J`, `jane`, `abc` | Los mismos tres errores |
| `Jane`, `jane@example.com`, `secret123` | Sin errores, campos vacíos y el mensaje verde _Registration successful!_ |
| Vista de celular | La tarjeta ocupa cerca del 90% del ancho |

---

### Paso 14 — Cierre

**DECIR:**

> And that's it! With three short files, we built a working registration form: HTML for the structure, CSS for the design, and JavaScript for the validation.
>
> And with each file, we used one extension: Live Server to see our changes instantly, Prettier to keep the code clean, and ESLint to catch real mistakes before they reach the browser.
>
> Thanks for watching!

**ACCIÓN:** Detén la grabación.
