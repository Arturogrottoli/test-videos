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
