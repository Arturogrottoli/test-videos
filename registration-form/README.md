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

**ACCIÓN:** En el Explorer, haz clic en **New File…** y crea `index.html`. Escribe cada bloque y lee el texto que está debajo. Al final, guarda con `Ctrl + S`.

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

> Let's create index.html. A quick trick: I type an exclamation mark and press Tab, and VS Code writes the basic HTML skeleton for me. In the head, I'll change the title to "Registration Form", and link our stylesheet, styles.css. We'll create that file later.

**Bloque 2 de 6** — dentro del `<body>`:

```html
    <form id="form" novalidate>
      <h1>Create account</h1>
```

> Inside the body, we add a form with the id "form", so JavaScript can find it. The word "novalidate" turns off the browser's own validation, because our JavaScript will do it. And a heading: "Create account".

**Bloque 3 de 6:**

```html
      <label for="name">Name</label>
      <input id="name" type="text" />
      <small id="name-error"></small>
```

> Each field has three parts. First, a label, the text the user sees. Its "for" attribute matches the input's id, so clicking the label puts the cursor in the field. Then the input itself. And an empty "small" element, where we'll show the error message. Notice its id: "name-error". Our JavaScript will use that name to find it.

**Bloque 4 de 6:**

```html
      <label for="email">Email</label>
      <input id="email" type="email" />
      <small id="email-error"></small>

      <label for="password">Password</label>
      <input id="password" type="password" />
      <small id="password-error"></small>
```

> The email and password fields follow exactly the same pattern: "email" and "email-error", "password" and "password-error". The type "password" hides what the user types with dots.

**Bloque 5 de 6:**

```html
      <button type="submit">Sign up</button>
      <p id="success" hidden>Registration successful!</p>
    </form>
```

> Then the button that sends the form, and the success message. It has the "hidden" attribute, so it's invisible for now. JavaScript will show it when everything is valid.

**Bloque 6 de 6** — antes de `</body>`. Las etiquetas `</body>` y `</html>` ya las creó Emmet en el bloque 1.

```html
    <script src="script.js"></script>
  </body>
</html>
```

> Finally, before closing the body, we load script.js. We put it at the end, so the whole form already exists when the script runs. I'll save the file.

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

**ACCIÓN:** Crea `styles.css`. Escribe cada bloque y lee el texto que está debajo. Al final, guarda y mira el navegador.

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

> Now styles.css. We only need three rules. First, the form. "display: grid" puts each label and field one below the other, with a small gap. "max-width" keeps it narrow, and "margin auto" centers it on the page. That also makes it responsive: on a phone, it simply uses the available width.

**Bloque 2 de 3:**

```css
input.invalid {
  border: 2px solid red;
}
```

> Second, the class "invalid" gives a field a red border. JavaScript will add that class when a field is wrong.

**Bloque 3 de 3:**

```css
small {
  color: red;
}
```

> And third, the error messages, in the "small" elements, are red.
>
> I'll save, and look at the browser: it updated by itself. That's Live Server again.

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

> Now let's try Prettier. I'll write this rule on one messy line, with no spaces. It still works, but it's hard to read.
>
> The first time, we tell VS Code to use Prettier: right-click, "Format Document With", "Configure Default Formatter", and Prettier. Now I'll press Shift, Option, and F, which is "Format Document". And there it is: Prettier puts the rule back on three clean lines. From now on, I just use that shortcut.

**CÓDIGO:** Solo el cambio de la regla, que Prettier corrige.

**PRUEBA:** La regla vuelve a ocupar tres líneas:

```css
input.invalid {
  border: 2px solid red;
}
```

---

## Parte 3 — JavaScript y ESLint

### Paso 9 — script.js: la funcionalidad

**ACCIÓN:** Crea `script.js`. Escribe cada bloque y lee el texto que está debajo. Al final, guarda con `Ctrl + S`.

**CÓDIGO Y DECIR:**

**Bloque 1 de 5:**

```js
const form = document.getElementById("form");
const success = document.getElementById("success");
```

> Finally, script.js. First, we get two elements from the page with "getElementById": the form, and the success message. We save them in constants, so we can use them later.

**Bloque 2 de 5:**

```js
const rules = {
  name: [(v) => v.trim().length >= 2, "Min. 2 characters."],
  email: [(v) => v.includes("@"), "Invalid email"],
  password: [(v) => v.length >= 8, "Min. 8 characters."],
};
```

> Then our rules, all in one place. For each field id, we have two things: a small function that tests the value, and the error message. The name needs at least 2 characters, and "trim" makes sure extra spaces don't count. The email must contain an at sign. And the password needs at least 8 characters. If we want a new field later, we just add one line here.

**Bloque 3 de 5** — VS Code agrega solo el cierre `});`, así que escribe el resto del código adentro.

```js
form.addEventListener("submit", (event) => {
  event.preventDefault();
```

> Next, we listen for the form's "submit" event, which happens when the user clicks Sign up. By default, the browser would reload the page. "preventDefault" stops that, so we can check the data first.

**Bloque 4 de 5:**

```js
  const ok = Object.entries(rules)
    .map(([id, [test, message]]) => {
      const valid = test(form.elements[id].value);
      form.elements[id].classList.toggle("invalid", !valid);
      document.getElementById(id + "-error").textContent = valid ? "" : message;
      return valid;
    })
```

> Now we go through our rules, one field at a time. "Object.entries" gives us each id with its test and its message. We find the input with "form.elements", and run the test on its value.
>
> Then "classList.toggle" adds the red "invalid" class when the value is not valid, and removes it when it is. We find the error element by adding "-error" to the id. That's the naming rule from our HTML. We show the message, or clear it. And we return true or false.

**Bloque 5 de 5:**

```js
    .every(Boolean);

  success.hidden = !ok;
  if (ok) form.reset();
});
```

> "every" checks that all the results are true. We use "map" first, so every field gets checked, even when the first one is wrong. Last, the success message stays hidden unless everything is OK. And when everything is valid, "reset" clears the form. I'll save the file.

**PRUEBA:** El archivo está guardado y tiene 24 líneas. El formulario se prueba completo en el paso 13.

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

**ACCIÓN Y DECIR:**

**1.** Abre **Terminal → New Terminal** y escribe:

```
pwd
```

> I'll open the terminal and check that I'm in the project folder, with "pwd".

**2.** Instala ESLint en el proyecto. Se crean `package.json`, `package-lock.json` y la carpeta `node_modules`.

```
npm install --save-dev eslint@9
```

> Then I'll install ESLint in the project with "npm install --save-dev eslint@9". "Save-dev" means it's a tool for development, not part of the website.

**3.** Comprueba la versión:

```
npx eslint -v
```

> Let me check that it works with "npx eslint -v". It shows version 9.

**4.** En el Explorer, crea `eslint.config.mjs` junto a `package.json`, escribe esto y guarda:

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

> Now ESLint needs its rules. I'll create a file called "eslint.config.mjs". This is ESLint's configuration file. We turn on two rules: "no-undef" gives an error when we use a variable that doesn't exist, and "no-unused-vars" warns us about variables we never use. We also tell ESLint that our code runs in the browser, where "document" always exists.

**5.** `Ctrl + Shift + P` → `ESLint: Restart ESLint Server` → Enter.

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

2. En `script.js`, agrega esta línea al final del archivo (línea 25) y guarda:

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
> In the terminal, ESLint shows the same thing: line 25, an error, the message, and the rule name, "no-undef". ESLint found the bug without even running the code.
>
> Notice that Prettier didn't complain. The line is well formatted, just wrong. Prettier checks how the code looks, and ESLint checks if it makes sense.
>
> I'll delete the line, save, and run ESLint again. No output, so our code is clean.

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

> Now let's see the whole project working. First, I'll click Sign up with everything empty. Three red borders and three error messages.
>
> Now wrong values: one letter, an email without an at sign, and a short password. Still three errors, because none of them follow the rules.
>
> And now valid values: "Jane", "jane@example.com", and "secret123". The errors disappear, the form is cleared, and we see "Registration successful!".
>
> Last, on a phone-sized screen, the form fills the width and still looks good.

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
