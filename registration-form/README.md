# Formulario de registro — Guion de narración

Un video corto de programación en vivo. Instalas tres extensiones de VS Code y después escribes un formulario de registro en tres archivos: `index.html` (estructura), `styles.css` (diseño) y `script.js` (funcionalidad).

Cada paso tiene: **ACCIÓN** (lo que haces en pantalla), **DECIR** (lo que lees en voz alta, en inglés), **CÓDIGO** (lo que escribes) y **PRUEBA** (lo que deberías ver).

Los nombres de menús y botones están en inglés, tal como aparecen en VS Code en inglés.

## Antes de grabar (no sale en el video)

ESLint no trae reglas por defecto, así que se deja listo antes de grabar. Live Server y Prettier no necesitan nada.

1. **Node.js:** en la terminal de VS Code (**Terminal → New Terminal**), escribe `node -v`. Si da error, instala la versión LTS desde https://nodejs.org y reinicia VS Code.
2. **Instalar ESLint:** en la misma terminal, ejecuta `npm install -g eslint@9`.
3. **Reglas de ESLint:** `Ctrl + Shift + P` → `Preferences: Open User Settings (JSON)`. Pega esta línea justo después de la primera `{` y guarda:

   ```json
   "eslint.options": { "overrideConfigFile": true, "overrideConfig": { "languageOptions": { "globals": { "document": "readonly" } }, "rules": { "no-undef": "error", "no-unused-vars": "warn" } } },
   ```

4. **Prettier como formateador:** abre cualquier archivo CSS, pulsa `Shift + Alt + F`, haz clic en **Configure…** y elige **Prettier - Code formatter**.

Si en el video ESLint no subraya nada, ejecuta `Ctrl + Shift + P` → `ESLint: Restart ESLint Server`.

---

### Paso 1 — Introducción

**ACCIÓN:** VS Code está abierto en la pestaña de bienvenida (Welcome).

**DECIR:**

> Hi everyone! Today we'll build a registration form from scratch with HTML, CSS, and JavaScript. It will have three fields: name, email, and password. If something is wrong, we'll show an error under the field. If everything is right, we'll show a success message.
>
> First, we'll add three VS Code extensions that make our work easier: Live Server, Prettier, and ESLint. Then we'll write three files: HTML for the structure, CSS for the design, and JavaScript for the functionality.

**CÓDIGO:** Ninguno. **PRUEBA:** Ninguna.

---

### Paso 2 — Abrir la carpeta del proyecto

**ACCIÓN:** **File → Open Folder…** → en el Escritorio, haz clic en **New folder** → llámala `registration-form` → **Select Folder**. Si VS Code pregunta si confías en los autores, haz clic en **Yes, I trust the authors**.

**DECIR:**

> I'll go to File, Open Folder, create a new folder called "registration-form" on my Desktop, and open it. The Explorer on the left is empty, because we start from zero.

**CÓDIGO:** Ninguno.

**PRUEBA:** El Explorer muestra **REGISTRATION-FORM** sin archivos.

---

### Paso 3 — Instalar las extensiones

**ACCIÓN:** Abre la vista de **Extensions** (`Ctrl + Shift + X`) e instala:

1. **Live Server**, de Ritwick Dey
2. **Prettier - Code formatter**, de Prettier
3. **ESLint**, de Microsoft

Si ya las instalaste al preparar, solo muéstralas en la lista y no digas "Install".

**DECIR:**

> I'll open the Extensions view with this icon on the left.
>
> First, Live Server. It opens our page in the browser and reloads it automatically every time we save. Install.
>
> Second, Prettier. It's a code formatter. It fixes spaces, indentation, and quotes with one shortcut, so our code always looks clean. Install.
>
> Third, ESLint. It's a linter. It reads our JavaScript and underlines real mistakes while we type, like a misspelled variable. ESLint needs a list of rules, and I already set them up before this video. Install.
>
> In short: Live Server shows our work, Prettier keeps it clean, and ESLint keeps it correct.

**CÓDIGO:** Ninguno.

**PRUEBA:** Las tres extensiones muestran **Uninstall** o un ícono de engranaje. Aparece un botón **Go Live** abajo a la derecha, en la barra de estado.

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

### Paso 5 — Ejemplo de Live Server

**ACCIÓN:**

Con `index.html` guardado, haz clic en **Go Live**, en la barra de estado de abajo a la derecha.

**DECIR:**

> Let's see our first extension. I'll click "Go Live" at the bottom of VS Code. Live Server opens our page in the browser. It's very plain, because we don't have any CSS yet. From now on, every time I save a file, the browser will update by itself.

**CÓDIGO:** Ninguno.

**PRUEBA:** El navegador abre `http://127.0.0.1:5500/index.html` con la página sin estilos, y el botón de abajo ahora dice **Port : 5500**.

---

### Paso 6 — styles.css: el diseño

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
> I'll save, and look at the browser: it updated by itself again. That's Live Server.

**PRUEBA:** Sin recargar, el navegador muestra una tarjeta blanca centrada con un botón azul.

---

### Paso 7 — Ejemplo de Prettier

**ACCIÓN:** En `styles.css`, selecciona la regla `input.invalid` (líneas 32 a 34) y escríbela de nuevo en una sola línea, así: `input.invalid{border-color:#dc2626}`. Pulsa `Shift + Alt + F` y guarda.

**DECIR:**

> Now let's see Prettier. I'll write this rule on one messy line, with no spaces. It still works, but it's hard to read. I'll press Shift, Alt, and F, and Prettier puts it back on three clean lines.

**CÓDIGO:** Solo el cambio de la regla, que Prettier corrige.

**PRUEBA:** Al pulsar `Shift + Alt + F`, la regla vuelve a ocupar tres líneas:

```css
input.invalid {
  border-color: #dc2626;
}
```

---

### Paso 8 — script.js: la funcionalidad

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

  const okName = check("name", name.length >= 2, "Min. 2 characters");
  const okEmail = check("email", /^\S+@\S+\.\S+$/.test(email), "Invalid email");
  const okPass = check("password", pass.length >= 8, "Min. 8 characters");

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
> Now our three rules: the name needs at least 2 characters, the email must match a simple pattern, something, at sign, something, dot, something, and the password needs at least 8 characters.
>
> Last, the success message. It's visible only if all three checks are OK. And when everything is valid, we clear the form.

**PRUEBA:** En el navegador, haz clic en **Sign up** con los campos vacíos: aparecen tres bordes rojos y tres mensajes en rojo.

---

### Paso 9 — Ejemplo de ESLint

**ACCIÓN:**

1. En la **línea 19**, cambia `name.length` por `nmae.length`.
2. Pasa el mouse sobre la línea **roja** debajo de `nmae`, y después sobre la línea **amarilla** debajo de `name` en la línea 15.
3. Guarda. En el navegador, haz clic en **Sign up**. Pulsa `F12` y abre la pestaña **Console**.
4. Vuelve a cambiar `nmae` por `name` y guarda. Cierra las herramientas de desarrollo.

**DECIR:**

> Now let's see ESLint. I'll make a typical typo: on line 19, I'll write "nmae" instead of "name".
>
> ESLint underlines it in red right away: "'nmae' is not defined". That variable doesn't exist. And there's also a yellow warning on line 15: "'name' is assigned a value but never used", because now we never use the real variable.
>
> Is it really a bug? I'll save and try the form. I click Sign up, and nothing happens. In the browser console, there it is: "ReferenceError: nmae is not defined". The form is broken, and ESLint told us before we even opened the browser.
>
> Notice that Prettier didn't complain. The code was well formatted, just wrong. Prettier checks how the code looks, and ESLint checks if it makes sense.
>
> I'll fix the typo, and both lines disappear.

**PRUEBA:**

- **Con el error:** subrayado rojo `'nmae' is not defined.` (regla `no-undef`) y aviso amarillo `'name' is assigned a value but never used.` (regla `no-unused-vars`). La consola muestra `Uncaught ReferenceError: nmae is not defined`.
- **Después de corregirlo:** no queda ningún subrayado.
- **Si no aparece ningún subrayado:** ejecuta **ESLint: Restart ESLint Server** y revisa **View → Output → ESLint**.

---

### Paso 10 — Probar el formulario

**ACCIÓN:**

1. Escribe `J`, `jane@` y `abc`, y haz clic en **Sign up**.
2. Escribe `Jane`, `jane@example.com` y `secret123`, y haz clic en **Sign up**.
3. Pulsa `F12`, luego `Ctrl + Shift + M`, y elige un tamaño de celular. Después cierra las herramientas de desarrollo.

**DECIR:**

> Let's test it. Wrong values first: one letter, an email without a domain, and a short password. Three red errors.
>
> Now valid values: "Jane", "jane@example.com", and "secret123". The errors disappear, the form is cleared, and we see "Registration successful!" in green.
>
> And on a phone-sized screen, the form fills the width and still looks good.

**PRUEBA:**

| Datos | Resultado |
| ----- | --------- |
| `J`, `jane@`, `abc` | Bordes rojos y los mensajes _Min. 2 characters_, _Invalid email_, _Min. 8 characters_ |
| `Jane`, `jane@example.com`, `secret123` | Sin errores, campos vacíos y el mensaje verde _Registration successful!_ |
| Vista de celular | La tarjeta ocupa cerca del 90% del ancho |

---

### Paso 11 — Cierre

**DECIR:**

> And that's it! With three short files, we built a working registration form: HTML for the structure, CSS for the design, and JavaScript for the validation.
>
> And we used three extensions: Live Server to see changes instantly, Prettier to keep the code clean, and ESLint to catch real mistakes before they reach the browser.
>
> Thanks for watching!

**ACCIÓN:** Detén la grabación.

---

> **Después de grabar:** el ajuste `eslint.options` de "Antes de grabar" se aplica a todos tus proyectos. Para quitarlo, abre **Preferences: Open User Settings (JSON)** y borra el bloque `"eslint.options"`.
