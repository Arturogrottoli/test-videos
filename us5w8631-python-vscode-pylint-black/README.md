# us5w8631 — Python: VS Code, venv, Pylint and Black

Recording script for setting up a small Python project in VS Code: create and fix `calculator.py`, set up a `.venv` virtual environment, configure Pylint and Black, and configure the workspace `settings.json`.

## How to use this script

Each step has four parts:

- **On screen**: what you do.
- **Say**: the exact narration. Values in `[brackets]` are read from the screen at that moment. Never say a number you have not seen on screen.
- **Check**: what must be visible before you move on.
- **Pause**: when to stop talking and let the screen speak.

## Files in this folder

| File | Purpose |
| ---- | ------- |
| `README.md` | This script |
| `reference/calculator_initial.py` | First version with style problems and a division-by-zero bug (typed in Step 8) |
| `reference/calculator_final.py` | Corrected version (reached in Step 12) |
| `reference/settings.json` | Workspace settings (typed in Step 7) |

These are **reference files only**. Do not open this folder in VS Code for the recording. Pylint would also lint the `reference` files. Record in a separate, empty folder (for example `Desktop/calculator-project`).

### Pre-test results (not for narration)

I tested the reference files with Pylint 4.1.3 and Black 26.10.1 on Python 3.14:

- `calculator_initial.py` crashes with `ZeroDivisionError`. Pylint reports bad indentation, missing docstrings, multiple statements on one line and an unused import. Black reports that it would reformat the file.
- `calculator_final.py` runs without errors, gets 10.00/10 from Pylint, and Black leaves it unchanged.

Your versions may give different messages or scores. During the recording, always read what your own screen shows.

## Missing information (check the original task before recording)

- Required video length: not confirmed.
- Recording rules (camera, microphone, resolution, single take, edits allowed): not confirmed.
- AutoQC requirements: not confirmed.
- **Deliverables for this task: not confirmed.** Possibly the video, `calculator.py`, `.vscode/settings.json` and `requirements.txt`. Confirm before recording.
- If the task provides its own `calculator.py` with specific bugs, use that file instead of `calculator_initial.py` and fix what Pylint and the run actually report.

---

## Setup (before recording)

- Install VS Code and Python 3. Confirm with `python --version` (or `py --version` on Windows).
- Install three VS Code extensions: **Python** (`ms-python.python`), **Pylint** (`ms-python.pylint`) and **Black Formatter** (`ms-python.black-formatter`). If the task requires installing them on camera, do it in Step 2.
- Create an empty folder, for example `calculator-project`.
- Close unrelated tabs and turn off notifications.
- Increase the editor and terminal font size so code is readable in the video.

---

## Recording script

### Step 1 — Open the project

- **On screen:** VS Code → *File > Open Folder* → `calculator-project`.
- **Say:** "I'm starting with an empty project folder. The goal is to create a small calculator script, set up a virtual environment, and use Pylint and Black to clean up the code."
- **Check:** The Explorer shows the empty folder.
- **Pause:** Short, while the folder opens.

### Step 2 — Show the extensions

- **On screen:** Open Extensions (Ctrl+Shift+X). Search "Pylint", then "Black Formatter".
- **Say:** "I have the Python, Pylint, and Black Formatter extensions installed. Pylint will report code problems, and Black will handle formatting."
- **Check:** All three extensions show as installed or enabled.
- **Pause:** About two seconds on each extension.

### Step 3 — Create the virtual environment

- **On screen:** Open the terminal (*Terminal > New Terminal*) and run:
  ```
  python -m venv .venv
  ```
  (Use `py -m venv .venv` if `python` is not found on Windows.)
- **Say:** "First, I'll create a virtual environment called dot venv. This keeps the project's packages separate from the global Python install."
- **Check:** A `.venv` folder appears in the Explorer.
- **Pause:** While it's being created.

### Step 4 — Activate the environment

- **On screen:**
  - Windows PowerShell: `.venv\Scripts\Activate.ps1`
  - macOS/Linux: `source .venv/bin/activate`
  - If PowerShell blocks the script, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` and activate again.
- **Say:** "Now I'll activate it. The prompt should show the environment name at the start."
- **Check:** The prompt starts with `(.venv)`.
- **Pause:** Yes. Point at `(.venv)`.

### Step 5 — Install Pylint and Black

- **On screen:**
  ```
  pip install pylint black
  pip list
  ```
- **Say:** "With the environment active, I'll install Pylint and Black. Then I'll list the packages to confirm they're inside this environment."
- **Check:** `pylint` and `black` appear in `pip list`.
- **Pause:** During the installation. Stay quiet if it takes a while.
- *Optional, if the deliverables need it:* `pip freeze > requirements.txt`. **Say:** "I'll also save the exact package versions to requirements dot txt."

### Step 6 — Select the interpreter

- **On screen:** Ctrl+Shift+P → "Python: Select Interpreter" → pick the one inside `.venv`.
- **Say:** "I'll point VS Code to the interpreter inside dot venv, so the editor uses the same packages as the terminal."
- **Check:** The status bar shows the Python version with `.venv`.
- **Pause:** Short.

### Step 7 — Create `settings.json`

- **On screen:** Create a `.vscode` folder and inside it a `settings.json` file. Type the content from `reference/settings.json`. For now, write `"editor.formatOnSave": false` so Black doesn't fix the first version on save. You'll turn it on in Step 12.
  ```json
  {
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
    "[python]": {
      "editor.defaultFormatter": "ms-python.black-formatter",
      "editor.formatOnSave": false
    },
    "pylint.enabled": true
  }
  ```
  On macOS/Linux, the interpreter path is `${workspaceFolder}/.venv/bin/python`.
- **Say:** "Next, the workspace settings. I'm setting the interpreter path, making Black the default formatter for Python, and enabling Pylint. I'm leaving format on save off for now, because I want to show the problems before Black fixes them. Since this file lives in the project, anyone who opens the folder gets the same setup."
- **Check:** No red error marks in the JSON. Save with Ctrl+S.
- **Pause:** Yes. Show the whole file for a few seconds.

### Step 8 — Write the first version of `calculator.py`

- **On screen:** Create `calculator.py` and type the content of `reference/calculator_initial.py`:
  ```python
  import os
  def add(a,b):
      return a+b
  def subtract(a,b):
    return a-b
  def multiply(a,b): return a*b
  def divide(a,b):
      return a/b
  if __name__=="__main__":
      print(add(2,3))
      print(divide(10,0))
  ```
- **Say:** "Here's a quick first version of the calculator. I wrote it fast, so it has spacing problems, an unused import, no docstrings, and no check for division by zero. I'll let the tools find the style issues instead of fixing everything by hand."
- **Check:** The file is saved. Pylint may already underline some lines.
- **Pause:** While typing. Don't narrate each line.

### Step 9 — Run the script

- **On screen:** `python calculator.py`
- **Say:** "Let me run it first to see how it behaves."
- **Check:** Read the real output. The first `print` should show `5`, followed by a traceback. Confirm it is a `ZeroDivisionError` before you mention it.
- **Say (after seeing it):** "The addition works, but dividing by zero crashes the script. I'll handle that case explicitly."
- **Pause:** Yes, on the traceback.

### Step 10 — Run Pylint on the first version

- **On screen:** `pylint calculator.py`. Also open the *Problems* panel (Ctrl+Shift+M).
- **Say:** "Now Pylint. Let's see what it reports."
- **Check:** Read the real messages and the score at the bottom.
- **Say:** "It flags [message one] on line [n], and [message two] on line [n]. The score is [score] out of ten. Some of these, like the indentation and the one-line function, are formatting issues that Black can fix. The docstrings and the unused import I'll fix myself."
- **Pause:** Yes, long. Show the full output.

### Step 11 — Run Black

- **On screen:**
  ```
  black --check calculator.py
  black calculator.py
  ```
- **Say:** "First I'll run Black in check mode, which only reports whether the file would change. Then I'll run it for real."
- **Check:** `--check` says the file would be reformatted. Then Black says it reformatted the file. In the editor, the spacing and line breaks are fixed.
- **Say:** "Black fixed the spacing, the indentation, and the one-line function."
- **Pause:** Yes. Show the formatted code.

### Step 12 — Manual fixes

- **On screen:**
  1. In `.vscode/settings.json`, change `"editor.formatOnSave"` to `true` and save.
  2. Edit `calculator.py` until it matches `reference/calculator_final.py`:
  ```python
  """Simple calculator with basic arithmetic operations."""


  def add(a, b):
      """Return the sum of a and b."""
      return a + b


  def subtract(a, b):
      """Return a minus b."""
      return a - b


  def multiply(a, b):
      """Return the product of a and b."""
      return a * b


  def divide(a, b):
      """Return a divided by b. Raise ValueError if b is zero."""
      if b == 0:
          raise ValueError("Cannot divide by zero.")
      return a / b


  def main():
      """Run a few example calculations."""
      print(f"2 + 3 = {add(2, 3)}")
      print(f"7 - 4 = {subtract(7, 4)}")
      print(f"3 * 5 = {multiply(3, 5)}")
      print(f"10 / 4 = {divide(10, 4)}")
      try:
          divide(10, 0)
      except ValueError as error:
          print(f"Error: {error}")


  if __name__ == "__main__":
      main()
  ```
- **Say:** "Now that the problems are visible, I'll turn format on save back on. Then the manual fixes. I'm removing the unused import and adding a module docstring and a docstring for each function. For division, I'll raise a ValueError with a clear message instead of letting Python crash. I'm also moving the examples into a main function and catching the error there."
- **Check:** No syntax errors underlined.
- **Pause:** While typing. Explain decisions, not every line.

### Step 13 — Test format on save

- **On screen:** Break the spacing on purpose (for example, change `return a + b` to `return a+b`) and press Ctrl+S.
- **Say:** "Quick check that format on save works. I'll break the spacing on purpose and save."
- **Check:** After saving, the line goes back to `return a + b`.
- **Say (only if it worked):** "Black corrected it on save, so the settings file is working."
- **If it did not change:** Run Ctrl+Shift+P → "Format Document With…" and confirm Black is the default. Don't say it works until you see it work.
- **Pause:** Yes, just before and after saving.

### Step 14 — Final verification

- **On screen:**
  ```
  python calculator.py
  pylint calculator.py
  black --check calculator.py
  ```
- **Say:** "Final checks. I'll run the script, then Pylint, then Black in check mode."
- **Check:**
  - The script prints four results and an error message, with no traceback.
  - Pylint shows a score. Read it as it appears.
  - Black reports that the file would be left unchanged.
- **Say:** "The script runs and handles division by zero cleanly. Pylint now gives [score] out of ten, and Black reports no changes."
- **If Pylint still shows warnings:** Fix them, or explain why you're leaving them.
- **Pause:** Yes, on each output.

### Step 15 — Wrap up

- **On screen:** The Explorer showing `.venv`, `.vscode/settings.json`, `calculator.py` (and `requirements.txt` if created).
- **Say:** "To wrap up: the project has its own virtual environment, VS Code uses it, Pylint checks the code, and Black formats it on save. The calculator now handles division by zero with a clear error."
- **Pause:** About two seconds before stopping the recording.

---

## Task checklist

- [ ] `.venv` created and activated, with `(.venv)` visible in the video.
- [ ] Pylint and Black installed inside the venv, with `pip list` shown on screen.
- [ ] The `.venv` interpreter selected in VS Code.
- [ ] `.vscode/settings.json` shown in full and saved, with `formatOnSave` set to `true` at the end.
- [ ] Pylint run before and after the fixes.
- [ ] Black run from the terminal, and format on save tested.
- [ ] Final `calculator.py` runs with no unhandled errors.
- [ ] Every score and message read from the screen, not assumed.
- [ ] **Deliverable list confirmed** against the original task.

## General recording checklist

**Before recording**
- [ ] Read the original task instructions and resolve the missing information above.
- [ ] Notifications off. No personal tabs, emails or accounts visible.
- [ ] Font size large enough to read in the video.
- [ ] Microphone tested: volume and background noise.
- [ ] This script open on another screen or printed, outside the recorded area.

**While recording**
- [ ] Follow the steps in order. If something fails, show the error, explain it and fix it on screen.
- [ ] Read numbers from the screen. Never state a result before running the command.
- [ ] Pause on important outputs.

**After recording**
- [ ] Watch the full video: audio is clear, code is readable, no sensitive information.
- [ ] Final files saved and named as the original task requires.
