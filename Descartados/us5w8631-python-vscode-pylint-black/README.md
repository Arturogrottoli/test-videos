# us5w8631 — Python: VS Code, venv, Pylint and Black

Recording script for setting up a small Python project in VS Code: create and fix `calculator.py`, set up a `.venv` virtual environment, configure Pylint and Black, and configure the workspace `settings.json`.

**Target length:** about 22 minutes, epilogue included. The recording must be **one continuous take between 15:00 and 50:59**.

## How to use this script

Each step has these parts:

- **On screen**: what you do.
- **Action (say it while you do it)**: one sentence for each click or typing action. It always names **what** you use, **where** it is on the screen, and **why**. AutoQC checks this in at least 70% of the interactions: *"I'm clicking [element] [location] to [reason]."*
- **Say**: the explanation. Values in `[brackets]` are read from the screen at that moment. Never say a number you have not seen on screen.
- **Check**: what must be visible before you move on.
- **Pause**: when to stop talking and let the screen speak. Pause about one second after every click, and **never stay silent for more than 45 seconds**.

If you do something that isn't in the script (for example, closing a pop-up), still say what it is, where it is, and why: *"I'm closing this notification with the X at its top right, so it doesn't cover the code."*

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

**Re-tested on the recording PC (Python 3.13.15, Pylint 4.1.3, Black 26.10.1), following this script step by step:**

| Step | Expected output |
| ---- | --------------- |
| 9 — Run the first version | `5`, then a traceback ending in `ZeroDivisionError: division by zero` |
| 10 — Pylint on the first version | 8 messages: W0311 bad-indentation (line 5), C0114 missing-module-docstring (line 1), C0116 missing-function-docstring (lines 2, 4, 6, 7), C0321 multiple-statements (line 6), W0611 unused-import `os` (line 1). **Score: 3.33/10** |
| 11 — Black | `--check`: "would reformat calculator.py … 1 file would be reformatted." Then: "reformatted calculator.py … 1 file reformatted." |
| 11 — (optional) Pylint again after Black | The indentation and one-line messages are gone. Only the docstrings and the unused import remain. **Score: 5.00/10** |
| 14 — Run the final version | `2 + 3 = 5`, `7 - 4 = 3`, `3 * 5 = 15`, `10 / 4 = 2.5`, `Error: Cannot divide by zero.` |
| 14 — Pylint on the final version | No messages. **Score: 10.00/10** |
| 14 — Black check on the final version | "1 file would be left unchanged." |

On this PC, PowerShell already allows scripts (`CurrentUser: Unrestricted`), so `.venv\Scripts\Activate.ps1` works without the `Set-ExecutionPolicy` command in Step 4.

Your versions may give different messages or scores. During the recording, always read what your own screen shows.

## Task information

**Goal (from Studio):** Configure a Python project in Visual Studio Code with a virtual environment, Pylint for linting, and Black for code formatting. Demonstrate how the tools identify and correct code-quality issues.

**Deliverable:** a VS Code project containing `calculator.py`, the `.venv` environment, and `.vscode/settings.json`, with Pylint and Black configured and demonstrated. The `.venv` folder can be large: check the rules to see if it must go into Deliverables.zip in full. `requirements.txt` (Step 5) is optional.

**Recording rules (from the AutoQC report and the Project Guide):**

- One continuous take between 15:00 and 50:59.
- Show the Goal document at the start, without narrating it for more than 30 seconds. Keep the introduction under 20 seconds.
- Say **where** each element is and **why** you use it, in at least 70% of the interactions.
- Pause about one second after each click. No silence longer than 45 seconds.
- Include a 3–4 minute epilogue (Step 16).
- Keep windows from overlapping: show one maximized window at a time.
- Typing should stay under about 30% (the code exception). Use the mouse for menus whenever possible.
- Never show Studio, Mercor, private information, or AI tools.
- After recording: run **Run full AutoQC** (not just *Rerun failing*) and upload four separate files: the **MP4**, the **original TaskRecorder ZIP**, **Deliverables.zip**, and **Metadata.rtf**.

If the task provides its own `calculator.py` with specific bugs, use that file instead of `calculator_initial.py` and fix what Pylint and the run actually report.

---

## Setup (before recording)

- VS Code and **Python 3.13.15 are already installed on this PC**, and `python` is on the PATH. **Close and reopen VS Code once before recording**, so its terminal picks up the new PATH. Confirm with `python --version` in the VS Code terminal: it must say `Python 3.13.15`. (`py --version` shows a different install, 3.14; always use `python` in this script.)
- Install three VS Code extensions: **Python** (`ms-python.python`), **Pylint** (`ms-python.pylint`) and **Black Formatter** (`ms-python.black-formatter`). If the task requires installing them on camera, do it in Step 2.
- Create an empty folder, for example `calculator-project` on the Desktop.
- Open the **Goal** document in the browser, ready for Step 0.
- Close unrelated tabs and turn off notifications. Close or minimize every window except the one you're showing.
- Increase the editor and terminal font size so code is readable in the video.
- Rehearse once, out loud, with a timer.

---

## Recording script

### Step 0 — Show the Goal (0:00–0:45)

- **On screen:** The Goal document in the browser.
- **Action:** "I'm on the Goal document in the browser, to show what this task asks for."
- **Say:** "As a Python developer, I'll set up a professional project in VS Code: a virtual environment, Pylint to find code-quality problems, and Black to format the code. Then I'll show both tools fixing a small calculator script."
- **Check:** The Goal is readable. Don't read it aloud for more than 30 seconds.
- **Pause:** Short.

### Step 1 — Open the project (0:45–1:30)

- **On screen:** VS Code → *File > Open Folder* → `calculator-project`.
- **Action:**
  - "I'm clicking the VS Code icon in the taskbar at the bottom of the screen, to open the code editor."
  - "I'm opening the File menu at the top left and choosing Open Folder, to open the project folder."
  - "I'm selecting the calculator-project folder on the Desktop and clicking the Select Folder button at the bottom right of the dialog."
  - If VS Code asks: "I'm clicking Yes, I trust the authors, in the center of the dialog, because this is my own folder."
- **Say:** "I'm starting with an empty project folder. The goal is to create a small calculator script, set up a virtual environment, and use Pylint and Black to clean up the code."
- **Check:** The Explorer shows the empty folder.
- **Pause:** Short, while the folder opens.

### Step 2 — Show the extensions (1:30–2:30)

- **On screen:** Open Extensions (Ctrl+Shift+X). Search "Pylint", then "Black Formatter".
- **Action:**
  - "I'm clicking the Extensions icon, the four squares in the left sidebar, to check the extensions this project needs."
  - "I'm typing Pylint in the search box at the top of the Extensions panel, to find the Pylint extension."
  - "I'm typing Black Formatter in the same search box, to check the formatter."
- **Say:** "I have the Python, Pylint, and Black Formatter extensions installed. The Python extension lets VS Code run and understand Python. Pylint will report code problems, and Black will handle formatting."
- **Check:** All three extensions show as installed or enabled.
- **Pause:** About two seconds on each extension.
- **Action (to go back):** "I'm clicking the Explorer icon, the two pages at the top of the left sidebar, to go back to the project files."

### Step 3 — Create the virtual environment (2:30–3:30)

- **On screen:** Open the terminal (*Terminal > New Terminal*) and run:
  ```
  python -m venv .venv
  ```
  (Use `py -m venv .venv` if `python` is not found on Windows.)
- **Action:**
  - "I'm opening the Terminal menu at the top and choosing New Terminal, to run commands inside the project folder."
  - "I'm typing the venv command in the terminal at the bottom of the window, to create the virtual environment."
- **Say:** "First, I'll create a virtual environment called dot venv. This keeps the project's packages separate from the global Python install, so each project can have its own versions."
- **Check:** A `.venv` folder appears in the Explorer.
- **Pause:** While it's being created.
- **Say (when it appears):** "The dot venv folder appeared in the Explorer on the left. It has its own copy of Python and its own packages."

### Step 4 — Activate the environment (3:30–4:30)

- **On screen:**
  - Windows PowerShell: `.venv\Scripts\Activate.ps1`
  - macOS/Linux: `source .venv/bin/activate`
  - If PowerShell blocks the script, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` and activate again.
- **Action:** "I'm typing the activation command in the terminal at the bottom, so the next commands use the virtual environment."
- **If PowerShell blocks it:** "PowerShell blocks scripts by default. I'm typing this command in the terminal to allow them only for this terminal session, and then activating again."
- **Say:** "Now I'll activate it. The prompt should show the environment name at the start."
- **Check:** The prompt starts with `(.venv)`.
- **Pause:** Yes. Point at `(.venv)` with the mouse.

### Step 5 — Install Pylint and Black (4:30–6:00)

- **On screen:**
  ```
  pip install pylint black
  pip list
  ```
- **Action:**
  - "I'm typing pip install in the terminal at the bottom, to install Pylint and Black inside the virtual environment."
  - "I'm typing pip list in the terminal, to confirm the packages are inside this environment."
- **Say:** "With the environment active, I'll install Pylint and Black. Then I'll list the packages to confirm they're inside this environment."
- **Say (while it installs, don't stay quiet):** "While it installs: Pylint is a linter. It reads the code without running it and reports errors, bad practices, and style problems. Black is a formatter. It rewrites the code in one consistent style, so nobody has to argue about spaces or line breaks."
- **Check:** `pylint` and `black` appear in `pip list`.
- **Pause:** Short, on the `pip list` output.
- *Optional, if the deliverables need it:* `pip freeze > requirements.txt`. **Action:** "I'm typing pip freeze in the terminal, to save the exact package versions to a requirements file." **Say:** "I'll also save the exact package versions to requirements dot txt."

### Step 6 — Select the interpreter (6:00–6:45)

- **On screen:** Ctrl+Shift+P → "Python: Select Interpreter" → pick the one inside `.venv`.
- **Action:**
  - "I'm opening the View menu at the top and choosing Command Palette, to tell VS Code which Python to use."
  - "I'm typing Python: Select Interpreter in the box at the top, and choosing the option inside dot venv, marked as Recommended."
- **Say:** "I'll point VS Code to the interpreter inside dot venv, so the editor uses the same packages as the terminal."
- **Check:** The status bar shows the Python version with `.venv`.
- **Action (to show it):** "I'm pointing at the status bar at the bottom right, where the Python version now shows dot venv."
- **Pause:** Short.

### Step 7 — Create `settings.json` (6:45–8:30)

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
- **Action:**
  - "I'm clicking the New Folder icon next to the project name, at the top of the Explorer panel on the left, and typing dot vscode, to create the folder for the workspace settings."
  - "I'm selecting the dot vscode folder in the Explorer, clicking the New File icon at the top of the panel, and typing settings dot json."
  - "I'm typing the settings in the editor, in the middle of the screen."
  - "I'm pressing Control and S to save the file."
- **Say:** "Next, the workspace settings. I'm setting the interpreter path, making Black the default formatter for Python, and enabling Pylint. I'm leaving format on save off for now, because I want to show the problems before Black fixes them. Since this file lives in the project, anyone who opens the folder gets the same setup."
- **Check:** No red error marks in the JSON. Save with Ctrl+S.
- **Pause:** Yes. Show the whole file for a few seconds.

### Step 8 — Write the first version of `calculator.py` (8:30–10:00)

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
- **Action:**
  - "I'm clicking the project name at the top of the Explorer, then the New File icon next to it, and typing calculator dot py, to create the script in the project root."
  - "I'm typing the first version of the calculator in the editor."
  - "I'm pressing Control and S to save it."
- **Say:** "Here's a quick first version of the calculator. I wrote it fast on purpose, so it has spacing problems, an unused import, no docstrings, and no check for division by zero. I'll let the tools find the style issues instead of fixing everything by hand."
- **Check:** The file is saved. Pylint may already underline some lines.
- **Pause:** While typing. Don't narrate each line, but don't stay silent for more than 45 seconds: mention each problem as you type it ("this import is never used", "this function is on one line").

### Step 9 — Run the script (10:00–11:00)

- **On screen:** `python calculator.py`
- **Action:** "I'm clicking in the terminal at the bottom and typing python calculator dot py, to run the script."
- **Say:** "Let me run it first to see how it behaves."
- **Check:** Read the real output. The first `print` should show `5`, followed by a traceback. Confirm it is a `ZeroDivisionError` before you mention it.
- **Say (after seeing it):** "The addition works, but dividing by zero crashes the script. I'll handle that case explicitly."
- **Pause:** Yes, on the traceback.

### Step 10 — Run Pylint on the first version (11:00–12:30)

- **On screen:** `pylint calculator.py`. Also open the *Problems* panel (Ctrl+Shift+M).
- **Action:**
  - "I'm typing pylint calculator dot py in the terminal at the bottom, to analyze the code."
  - "I'm opening the View menu at the top and choosing Problems, to see the same warnings in the Problems panel."
- **Say:** "Now Pylint. Let's see what it reports."
- **Check:** Read the real messages and the score at the bottom.
- **Say:** "It flags [message one] on line [n], and [message two] on line [n]. The score is [score] out of ten. Some of these, like the indentation and the one-line function, are formatting issues that Black can fix. The docstrings and the unused import I'll fix myself."
- **Action (while explaining):** "I'm clicking this warning in the Problems panel at the bottom, to jump to the line it refers to."
- **Pause:** Yes, long. Show the full output.

### Step 11 — Run Black (12:30–13:30)

- **On screen:**
  ```
  black --check calculator.py
  black calculator.py
  ```
- **Action:**
  - "I'm clicking the Terminal tab at the bottom and typing black dash dash check, to see if Black would change the file."
  - "I'm typing black calculator dot py in the terminal, to format the file."
- **Say:** "First I'll run Black in check mode, which only reports whether the file would change. Then I'll run it for real."
- **Check:** `--check` says the file would be reformatted. Then Black says it reformatted the file. In the editor, the spacing and line breaks are fixed.
- **Say:** "Black fixed the spacing, the indentation, and the one-line function."
- **Pause:** Yes. Show the formatted code.
- *Optional (adds time and shows the split between the tools):* run `pylint calculator.py` again. **Action:** "I'm running pylint again in the terminal at the bottom, to see what Black fixed and what's left." **Say:** "The score went up to [score]. The formatting messages are gone, but the docstrings and the unused import are still there, because Black only changes the format, not the content."

### Step 12 — Manual fixes (13:30–16:00)

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
- **Action:**
  - "I'm clicking settings dot json in the Explorer on the left, changing format on save to true, and pressing Control and S, so Black formats every save from now on."
  - "I'm clicking the calculator dot py tab at the top of the editor, to make the manual fixes."
  - "I'm selecting the import os line at the top of the file and deleting it, because it's never used."
  - "I'm typing the docstrings and the new divide and main functions in the editor."
  - "I'm pressing Control and S to save."
- **Say:** "Now that the problems are visible, I'll turn format on save back on. Then the manual fixes. I'm removing the unused import and adding a module docstring and a docstring for each function. For division, I'll raise a ValueError with a clear message instead of letting Python crash. I'm also moving the examples into a main function and catching the error there."
- **Check:** No syntax errors underlined.
- **Pause:** While typing. Explain decisions, not every line, and keep talking at least every 45 seconds.

### Step 13 — Test format on save (16:00–16:45)

- **On screen:** Break the spacing on purpose (for example, change `return a + b` to `return a+b`) and press Ctrl+S.
- **Action:**
  - "I'm clicking inside the add function, near the top of the editor, and removing the spaces around the plus sign, to test format on save."
  - "I'm pressing Control and S to save."
- **Say:** "Quick check that format on save works. I'll break the spacing on purpose and save."
- **Check:** After saving, the line goes back to `return a + b`.
- **Say (only if it worked):** "Black corrected it on save, so the settings file is working."
- **If it did not change:** "I'm opening the View menu, choosing Command Palette, and typing Format Document With, to check which formatter is the default." Confirm Black is the default. Don't say it works until you see it work.
- **Pause:** Yes, just before and after saving.

### Step 14 — Final verification (16:45–18:00)

- **On screen:**
  ```
  python calculator.py
  pylint calculator.py
  black --check calculator.py
  ```
- **Action:**
  - "I'm clicking in the terminal at the bottom and running the script again, to check it works."
  - "I'm running pylint in the terminal, to see the new score."
  - "I'm running black dash dash check in the terminal, to confirm the file is already formatted."
- **Say:** "Final checks. I'll run the script, then Pylint, then Black in check mode."
- **Check:**
  - The script prints four results and an error message, with no traceback.
  - Pylint shows a score. Read it as it appears.
  - Black reports that the file would be left unchanged.
- **Say:** "The script runs and handles division by zero cleanly. Pylint now gives [score] out of ten, and Black reports no changes."
- **If Pylint still shows warnings:** Fix them, or explain why you're leaving them.
- **Pause:** Yes, on each output.

### Step 15 — Wrap up (18:00–18:45)

- **On screen:** The Explorer showing `.venv`, `.vscode/settings.json`, `calculator.py` (and `requirements.txt` if created).
- **Action:** "I'm clicking each item in the Explorer panel on the left, the dot venv folder, settings dot json, and calculator dot py, to show the final project."
- **Say:** "To wrap up: the project has its own virtual environment, VS Code uses it, Pylint checks the code, and Black formats it on save. The calculator now handles division by zero with a clear error."
- **Pause:** About two seconds.

### Step 16 — Epilogue (18:45–22:15, 3–4 minutes)

Check the Odin rules for what the epilogue must include, and adjust this text if they ask for something different.

- **On screen:** Scroll slowly through `calculator.py`, then `settings.json`.
- **Action:** "I'm scrolling slowly through calculator dot py in the editor with the mouse wheel, to go over the decisions I made."
- **Say:** "In this epilogue, I want to go over my approach. I started with the environment: a virtual environment keeps the project's tools isolated, and selecting its interpreter in VS Code means the editor and the terminal always use the same packages."
- **Say:** "Then I wrote a quick first version on purpose and let the tools find the problems. Pylint and Black do different jobs. Black fixed the format in one command: spacing, indentation, and the one-line function. Pylint found the problems a formatter can't fix: the unused import and the missing docstrings."
- **Say:** "Running the script also mattered. Pylint didn't catch the division by zero; running the code did. So linting doesn't replace testing. I fixed it with a clear ValueError instead of letting the program crash."
- **Action:** "I'm clicking settings dot json in the Explorer on the left, to talk about the configuration."
- **Say:** "I kept format on save off at first, to show the problems before Black fixed them, and turned it on at the end. Because these settings live in the project, everyone who opens the folder gets the same interpreter, the same formatter, and the same checks."
- **Say:** "As next steps, I would add unit tests with pytest for the four functions, save the packages in requirements dot txt so anyone can recreate the environment with one command, and run Pylint and Black automatically before every commit. Thanks for watching!"
- **Check:** The epilogue lasts 3 to 4 minutes. If the clock hasn't passed 15:00 yet, don't stop: run Pylint again and explain each part of its output.
- **Pause:** About two seconds before stopping the recording.

---

## Task checklist

- [ ] Goal shown at the start, narrated for less than 30 seconds.
- [ ] `.venv` created and activated, with `(.venv)` visible in the video.
- [ ] Pylint and Black installed inside the venv, with `pip list` shown on screen.
- [ ] The `.venv` interpreter selected in VS Code.
- [ ] `.vscode/settings.json` shown in full and saved, with `formatOnSave` set to `true` at the end.
- [ ] Pylint run before and after the fixes.
- [ ] Black run from the terminal, and format on save tested.
- [ ] Final `calculator.py` runs with no unhandled errors.
- [ ] Every score and message read from the screen, not assumed.
- [ ] Every action narrated with **where** and **why**.
- [ ] Epilogue of 3–4 minutes, and total length between 15:00 and 50:59.

## General recording checklist

**Before recording**
- [ ] Read the original task instructions and compare them with this script.
- [ ] Notifications off. No personal tabs, emails or accounts visible. No Studio, Mercor, or AI tools on screen.
- [ ] Only one maximized window visible at a time.
- [ ] Font size large enough to read in the video.
- [ ] Microphone tested: volume and background noise.
- [ ] This script open on another screen or printed, outside the recorded area.

**While recording**
- [ ] Follow the steps in order. If something fails, show the error, explain it and fix it on screen.
- [ ] Say where each element is and why you use it.
- [ ] Read numbers from the screen. Never state a result before running the command.
- [ ] Pause about one second after each click, and never stay silent for more than 45 seconds.

**After recording**
- [ ] Watch the full video: audio is clear, code is readable, no sensitive information.
- [ ] Run **Run full AutoQC**, not just *Rerun failing*.
- [ ] Upload four separate files: the MP4, the original TaskRecorder ZIP, Deliverables.zip (with `calculator.py`, `.vscode/settings.json`, and `.venv` if required), and Metadata.rtf.
