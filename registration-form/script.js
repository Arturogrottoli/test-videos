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
