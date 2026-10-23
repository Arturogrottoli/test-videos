# Password Generator & Strength Validator — notebook cells for Google Colab.
# Each "# %%" block is one Colab code cell. Paste them in order.
# Markdown cells (title and conclusions) are described in README.md.

# %% Cell 1 — Imports
import secrets
import string
import pandas as pd


# %% Cell 2 — generator
def generator(length=12, use_upper=True, use_digits=True, use_symbols=True):
    """Generate a random password with the selected character types."""
    pools = [string.ascii_lowercase]
    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append(string.punctuation)

    if length < len(pools):
        raise ValueError(f"Length must be at least {len(pools)} for the selected options.")

    # One character from each selected pool, so every type is included
    chars = [secrets.choice(pool) for pool in pools]
    all_chars = "".join(pools)
    chars += [secrets.choice(all_chars) for _ in range(length - len(chars))]
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


# %% Cell 3 — Test generator
print(generator())
print(generator(8, use_symbols=False))
print(len(generator(20)))
try:
    generator(2)
except ValueError as e:
    print("Error:", e)


# %% Cell 4 — check_strength
def check_strength(password):
    """Score a password from 0 to 6 and return the score and a label."""
    score = 0
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        label = "Weak"
    elif score <= 4:
        label = "Medium"
    else:
        label = "Strong"
    return score, label


# %% Cell 5 — Test check_strength on fixed examples
for pw in ["abc", "abcdefgh", "Abcdefgh12", "Abcdef12!xyz"]:
    print(pw, "->", check_strength(pw))

# %% Cell 6 — Generate a batch of 10 passwords
configs = [
    {"length": 6, "use_upper": False, "use_digits": False, "use_symbols": False},
    {"length": 8, "use_upper": False, "use_digits": True, "use_symbols": False},
    {"length": 8, "use_upper": True, "use_digits": True, "use_symbols": False},
    {"length": 10, "use_upper": True, "use_digits": False, "use_symbols": True},
    {"length": 10, "use_upper": True, "use_digits": True, "use_symbols": True},
    {"length": 12, "use_upper": False, "use_digits": True, "use_symbols": True},
    {"length": 12, "use_upper": True, "use_digits": True, "use_symbols": True},
    {"length": 14, "use_upper": True, "use_digits": True, "use_symbols": False},
    {"length": 16, "use_upper": True, "use_digits": True, "use_symbols": True},
    {"length": 20, "use_upper": True, "use_digits": True, "use_symbols": True},
]

rows = []
for cfg in configs:
    pw = generator(**cfg)
    score, label = check_strength(pw)
    rows.append({"password": pw, **cfg, "score": score, "strength": label})

passwords_df = pd.DataFrame(rows)
passwords_df

# %% Cell 7 — Strongest and weakest
ranked = passwords_df.sort_values(["score", "length"], ascending=False).reset_index(drop=True)
strongest = ranked.iloc[0]
weakest = ranked.iloc[-1]
print(f"Strongest: {strongest['password']} | score: {strongest['score']} | length: {strongest['length']}")
print(f"Weakest:   {weakest['password']} | score: {weakest['score']} | length: {weakest['length']}")
print("\nStrength counts:\n", passwords_df["strength"].value_counts())
