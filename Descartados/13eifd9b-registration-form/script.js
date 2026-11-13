const form = document.getElementById("form");
const success = document.getElementById("success");

const rules = {
  name: [(v) => v.trim().length >= 2, "Min. 2 characters."],
  email: [(v) => v.includes("@"), "Invalid email"],
  password: [(v) => v.length >= 8, "Min. 8 characters."],
};

form.addEventListener("submit", (event) => {
  event.preventDefault();

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
