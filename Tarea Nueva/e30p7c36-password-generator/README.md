# e30p7c36 — Password Generator & Strength Validator

Recording script for building a password generator and a strength checker in Python on **Google Colab**: implement `generator` and `check_strength`, generate a batch of 10 passwords, show them in a DataFrame, find the strongest and the weakest according to the validator, and write conclusions.

**Registered deliverable:** the notebook (`.ipynb`) only. No external files are required.

## How to use this script

Each step has four parts:

- **On screen**: what you do.
- **Say**: the exact narration. Values in `[brackets]` are read from the screen at that moment. Never say a value you have not seen on screen.
- **Check**: what must be visible before you move on.
- **Pause**: when to stop talking and let the screen speak.

## Files in this folder

| File | Purpose |
| ---- | ------- |
| `README.md` | This script |
| `notebook_cells.py` | Every code cell, in order (`# %% Cell N`). Paste each block into its own Colab cell. |

### Pre-test (not for narration)

I ran all the cells locally on Python 3.14 and they finished without errors. Things to know before recording:

- **The passwords change on every run** (they come from `secrets`). Never read a password from this file. Read it from your own screen.
- Each configuration in Cell 6 guarantees at least one character of every selected type, so **the score of each row depends only on its settings, not on luck**. That makes the strongest/weakest result stable across runs, while the actual password strings change.
- The expected results for the fixed examples in Cell 5 can be worked out by hand from the rules (see Step 5). Confirm them on screen anyway.

## Missing information (check the original task before recording)

- Required video length: not confirmed.
- Recording rules (camera, microphone, resolution, single take, edits allowed): not confirmed.
- AutoQC requirements: not confirmed.
- **Exact signatures of `generator` and `check_strength`.** The ones below are a proposal. If the task defines parameters, return values or names, follow those.
- **Strength criteria and labels.** The 0–6 score and the Weak / Medium / Strong thresholds are a proposal. If the task defines its own rules, use those and update Step 5's expected results.
- Whether the DataFrame needs specific columns: not confirmed.
- Required notebook file name: not confirmed.

---

## Setup (before recording)

- Open a new notebook in Google Colab and rename it, for example `password_generator.ipynb`.
- Have `notebook_cells.py` open outside the recorded area so you can copy each cell.
- Browser zoom around 110–125% so the code and the table are readable.

---

## Recording script

### Step 1 — Title and imports

- **On screen:** Add a **text cell** with `# Password Generator & Strength Validator`. Paste and run **Cell 1**:
  ```python
  import secrets
  import string
  import pandas as pd
  ```
- **Say:** "I'm building a password generator and a strength checker. I'm using the secrets module instead of random, because secrets is designed for security-sensitive values like passwords. The string module gives me the character sets, and pandas is for the results table."
- **Check:** The cell runs without errors.
- **Pause:** Short.

### Step 2 — Implement `generator`

- **On screen:** Paste and run **Cell 2**:
  ```python
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
  ```
- **Say:** "The generator takes a length and three options: uppercase, digits, and symbols. Lowercase is always included. First I pick one character from each selected group, so the password really contains every type it promises. Then I fill the rest from all the groups combined and shuffle, so the guaranteed characters aren't always at the start. If the length is too short to fit one of each type, it raises an error."
- **Check:** The cell runs without errors.
- **Pause:** While typing or pasting.

### Step 3 — Test `generator`

- **On screen:** Paste and run **Cell 3**:
  ```python
  print(generator())
  print(generator(8, use_symbols=False))
  print(len(generator(20)))
  try:
      generator(2)
  except ValueError as e:
      print("Error:", e)
  ```
- **Say:** "A few quick tests: the default settings, a shorter one without symbols, a length check, and a length that's too short."
- **Check:**
  - Line 1: a 12-character password.
  - Line 2: 8 characters with no symbols.
  - Line 3: `20`.
  - Line 4: the error message.
- **Say:** "The default one has a mix of all four types. The second one has no symbols, the length check prints [value], and the invalid case raises the error as intended."
- **Pause:** Yes.

### Step 4 — Implement `check_strength`

- **On screen:** Paste and run **Cell 4**:
  ```python
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
  ```
- **Say:** "The strength checker gives one point for each rule: at least 8 characters, at least 12 characters, and one point each for lowercase, uppercase, digits, and symbols. That's six points at most. Two or fewer is weak, three or four is medium, and five or six is strong. It's a simple rule-based check, not a full security audit."
- **Check:** The cell runs without errors.
- **Pause:** While typing or pasting.

### Step 5 — Test `check_strength` on fixed examples

- **On screen:** Paste and run **Cell 5**:
  ```python
  for pw in ["abc", "abcdefgh", "Abcdefgh12", "Abcdef12!xyz"]:
      print(pw, "->", check_strength(pw))
  ```
- **Say:** "Before using it on random passwords, I'll test it on fixed examples where I can work out the score by hand."
- **Check:** By the rules, the expected results are:

  | Password | Expected score | Expected label |
  | -------- | -------------- | -------------- |
  | `abc` | 1 | Weak |
  | `abcdefgh` | 2 | Weak |
  | `Abcdefgh12` | 4 | Medium |
  | `Abcdef12!xyz` | 6 | Strong |

  Compare them with the output. Only say they match if they do.
- **Say:** "The short lowercase one gets one point. Adding length gets two. Adding uppercase and digits gets four. The last one has everything and gets six. All four match what I expected."
- **Pause:** Yes.

### Step 6 — Generate the batch of 10

- **On screen:** Paste and run **Cell 6**:
  ```python
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
  ```
- **Say:** "Now a batch of ten passwords. I'm using different settings on purpose, from six lowercase letters up to twenty characters with every type, so the validator has a real range to judge. Each password goes into a DataFrame with its settings, its score, and its label."
- **Check:** 10 rows. Each password's length matches the `length` column, and the settings match the characters you see.
- **Say:** "Ten rows. The labels go from [lowest label] to [highest label], and the scores rise with length and variety."
- **Pause:** Yes, long, on the table.

### Step 7 — Strongest and weakest

- **On screen:** Paste and run **Cell 7**:
  ```python
  ranked = passwords_df.sort_values(["score", "length"], ascending=False).reset_index(drop=True)
  strongest = ranked.iloc[0]
  weakest = ranked.iloc[-1]
  print(f"Strongest: {strongest['password']} | score: {strongest['score']} | length: {strongest['length']}")
  print(f"Weakest:   {weakest['password']} | score: {weakest['score']} | length: {weakest['length']}")
  print("\nStrength counts:\n", passwords_df["strength"].value_counts())
  ```
- **Say:** "To find the strongest and weakest, I sort by score and use length to break ties, because several passwords share the top score."
- **Check:** Read both lines and the label counts.
- **Say:** "The strongest is the [length]-character password with a score of [score]. The weakest is the [length]-character one, with a score of [score]. Overall there are [n] strong, [n] medium, and [n] weak."
- **Pause:** Yes.

### Step 8 — Conclusions (text cell)

- **On screen:** Add a **text cell** and fill it in from your outputs:
  ```
  ## Conclusions
  - `generator` uses the `secrets` module and guarantees at least one character from each selected type.
  - `check_strength` scores passwords from 0 to 6, based on length and character variety.
  - In this batch: [n] Strong, [n] Medium, [n] Weak.
  - Strongest: length [x], score [y]. Weakest: length [x], score [y].
  - Length and character variety together drive the score; [observation from your table, e.g. which settings first reached "Strong"].
  - Limitations: the checker doesn't detect dictionary words or common patterns, and once a password reaches 12 characters, extra length adds no points.
  - These passwords are demo output and shouldn't be used for real accounts.
  ```
- **Say:** "Here are the findings from this run. The exact passwords will change if the notebook runs again, but each row's score comes from its settings, so the ranking stays the same."
- **Check:** The conclusions match the table on screen.
- **Pause:** While typing.

### Step 9 — Run everything and save

- **On screen:**
  1. *Runtime > Restart session and run all*.
  2. The password strings will change. If the conclusions quote a specific password, update it. The scores and counts should stay the same; confirm it on screen.
  3. *File > Download > Download .ipynb*.
- **Say:** "I'll run everything from a clean runtime to make sure the notebook works in order. The passwords are new, but the scores and counts [are the same / changed, so I'll update the conclusions]. Then I'll download the notebook."
- **Check:** No errors, the conclusions match the outputs, and the `.ipynb` is downloaded.
- **Pause:** During the run.

---

## Task checklist

- [ ] `generator` and `check_strength` implemented and tested separately.
- [ ] Fixed `check_strength` examples checked against the real output.
- [ ] Batch of 10 passwords shown in a DataFrame.
- [ ] Strongest and weakest identified, with the tie-break explained.
- [ ] Conclusions match the **last** run.
- [ ] Only the `.ipynb` delivered; no external files.
- [ ] **Signatures and criteria confirmed** against the original task.

## General recording checklist

**Before recording**
- [ ] Read the original task instructions and resolve the missing information above.
- [ ] Notifications off. No personal tabs, emails or accounts visible.
- [ ] Browser zoom large enough to read code and the table.
- [ ] Microphone tested: volume and background noise.
- [ ] This script open on another screen or printed, outside the recorded area.

**While recording**
- [ ] Follow the steps in order. If something fails, show the error, explain it and fix it on screen.
- [ ] Read values from the screen. Never state a result before running the cell.
- [ ] Pause on tables and key outputs.

**After recording**
- [ ] Watch the full video: audio is clear, code is readable, no sensitive information.
- [ ] Notebook named as the original task requires.
