# Step 1: Give each part a home

Use this small structure. Keep all application code inside `calculator/` so coverage measures the whole application.

```
calculator/
    __init__.py
    __main__.py
    operations.py
    calculation.py
    commands.py
    cli.py
tests/
requirements.txt
README.md              # keep the assignment book contents
STUDENT_README.md      # write your own explanations here
.github/workflows/tests.yml
```

First open a terminal in the cloned project folder (the folder containing requirements.txt). You need Git and Python 3.12 or newer. Check with `git --version` and `python --version`. On macOS/Linux, use `python3` if `python` is not available; on Windows you can use `py -3`. Use that same interpreter to create your virtual environment. After activation, `python` refers to the environment.

Use Python 3.12 or newer. Create a virtual environment and put these test tools in `requirements.txt`:

```
pytest>=8,<10
pytest-cov>=7,<8
```

```bash
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows PowerShell instead:
# .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Add `.venv/`, `__pycache__/`, `.pytest_cache/`, `.coverage`, and `htmlcov/` to `.gitignore`. Commit your source and tests, not your virtual environment.
The starter already contains addition, the calculation classes, a few example tests, and the workflow. You must add the remaining operations, commands, CLI, and tests. A green starter check does **not** mean the assignment is complete.


## If activation does not work

You can use the environment's Python directly instead of changing PowerShell permissions:

```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m pytest --cov=calculator --cov-report=term-missing --cov-fail-under=100
```

On macOS/Linux the equivalent executable is `.venv/bin/python`.

The starter has no CLI entry point yet. `python -m calculator` will fail until you complete Step 6. Run the starter tests first; that failure does not mean your clone is broken.

---

[Back to the contents](../README.md) · [Start with forking](00-fork-and-submit.md)

Next: [Step 2: Make operations with static methods](03-step-2-make-operations-with-static-methods.md)
