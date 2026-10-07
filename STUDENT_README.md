# My calculator submission — instructor student walkthrough

This completed example was built by following the assignment from Canvas. It is a simulation, not a submission by a real student. See WALKTHROUGH_NOTES.md for the issues found and resolved.

## Setup, run, and test

Use Python 3.12 or newer. Run these commands from the repository folder:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m calculator
python -m pytest --cov=calculator --cov-report=term-missing --cov-fail-under=100
```

In Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`. If activation is unavailable, run `.venv\Scripts\python.exe` directly in place of python. On macOS/Linux, `.venv/bin/python` also works directly.

## Example conversation

```text
> add 5 3
8.0
> divide 6 0
Error: Cannot divide by zero
> multiply -2 4
-8.0
> history
add 5 3 = 8.0
multiply -2 4 = -8.0
> exit
Goodbye!
```

Commands take exactly two numbers, except history and exit, which take none. Whitespace and uppercase command names are accepted. Blank lines are skipped. EOF also ends the program. The assignment requires ordinary numeric operands; this example does not add a special policy for NaN/infinity or Ctrl-C.

## Static, class, and instance methods

- Static: Operations.add(a, b) only needs a and b, so it has no self or cls. The other arithmetic methods work the same way.
- Class: Calculation.create(cls, a, b, operation) creates the class that called it. ArithmeticCalculation.create(...) therefore builds ArithmeticCalculation; Calculation itself stays abstract.
- Instance: ArithmeticCalculation.execute(self) uses the numbers and operation stored on that particular calculation. A different object can have different numbers and an operation.

## Factory, Command, and Strategy

For `add 5 3`, main splits and validates input, chooses Operations.add from the operation dictionary (Strategy), then calls ArithmeticCalculation.create(5.0, 3.0, Operations.add) (factory method). It gives the resulting calculation and shared history to CalculateCommand. The command's execute method calls calculation.execute, records the success, and returns 8.0. The CLI prints 8.0. HistoryCommand returns a copy of recorded entries.

The factory is a simple class construction method, not a subclass-selection factory. Strategies here are functions, not strategy subclasses. Commands coordinate actions; calculation execution performs the math.

## OOP

- Encapsulation: a Calculation groups its numbers and operation with execution. HistoryCommand returns a list copy, protecting the stored history from the caller's changes. Calculation attributes are public; Python does not make them private automatically.
- Abstraction: Calculation declares execute as abstract. A concrete calculation has to supply that method.
- Inheritance: ArithmeticCalculation reuses Calculation's initializer and create method.
- Polymorphism: CalculateCommand calls execute without choosing a concrete calculation implementation. The tests pass both ArithmeticCalculation and OtherCalculation to it and get valid numeric answers.
- Composition: CalculateCommand has a calculation, and a calculation has an operation function. Passing these pieces in makes them easy to replace.

## SOLID

- Single responsibility: Operations handles arithmetic, Calculation stores/delegates a calculation, commands coordinate execution/history, and the CLI reads and prints.
- Open/closed: another operation needs a method and a name in the CLI dictionary. Calculation.execute and CalculateCommand.execute do not need to change.
- Liskov substitution: OtherCalculation in the tests keeps the same promise as ArithmeticCalculation: execute returns the numeric result or lets an appropriate calculation error propagate.
- Interface segregation: Calculation requires only execute. It does not require printing, reading input, or history management.
- Dependency inversion: CalculateCommand receives a Calculation abstraction. Calculation receives a callable operation instead of hard-coding addition. The CLI builds the concrete pieces.

## Tests and GitHub Actions

54 tests pass locally, and all 89 measured application statements are covered. Tests assert arithmetic answers, factory construction, interchangeable calculations, command results, history copying/order, failed history, CLI errors followed by success, history display, exit, and EOF. Importing the entry point is also checked to make sure it does not start input.

The committed workflow uses Python 3.12 and runs on pushes, pull requests, and manual dispatch. It fails below 100% line coverage. The [successful branch run](https://github.com/kaw393939/is218-calculator-patterns/actions/runs/37670378046) passed on Python 3.12.

## Coverage exclusions

- Calculation.execute is an abstract placeholder: it defines a promise without implementing behavior.
- The `if __name__ == "__main__"` block is thin startup code that only calls the main function. Tests exercise main directly, and an actual subprocess smoke test checks the command-line entry point.

No arithmetic, factory, command, history, parsing, or error-handling behavior is excluded.

## Rubric review

| Category | Evidence | Review |
| --- | --- | --- |
| Working CLI (30) | cli.py, operation tests, CLI conversation tests, subprocess smoke test | All requested behaviors implemented. |
| OOP and patterns (30) | operations.py, calculation.py, commands.py; interchangeable calculation test | All required roles and method types implemented. |
| Tests and coverage (20) | 54 passing tests, 100% of calculator package | Full code requirement met with two small explained exclusions. |
| GitHub Actions (10) | tests.yml with 100% threshold | Passed on GitHub for the completed implementation. |
| Explanations and submission (10) | This file and useful source comments | Explanations complete; actual student fork/access and Canvas submission are not simulated. |

This is a self-review of the instructor's audit branch, not a posted Canvas grade. No fabricated student submission was made.
