# Step 5: Let a command run the calculation

A command is an object that represents an action. Write `CalculateCommand`. Give it a calculation and a shared history list. Its `execute()` must run the calculation, add a successful entry to history, and return the answer. If calculation fails, do not add an entry.

Write `HistoryCommand` with its own `execute()`. Return a copy of the history list so the caller cannot change the stored list by appending or removing entries. Simple strings are fine for entries. For example, `add 5 3 = 8.0` is readable; equivalent readable formats are accepted. Create the shared history list once in `main()`, outside the input loop. Give that same list to both command classes. A new list on each loop would forget earlier work. The CLI prints them or says that history is empty.

The calculation does the math. The command coordinates the action and history. Both use the name `execute()`, but they have different jobs. Keep printing and input in the CLI.
## A small starting shape

```python
from calculator.calculation import Calculation

class CalculateCommand:
    def __init__(self, calculation: Calculation, history: list[str]):
        # The command receives its pieces instead of building them.
        self.calculation = calculation
        self.history = history

    def execute(self) -> float:
        # TODO: execute the calculation, then record a successful entry.
        # Return the result. A failure must leave history unchanged.
        raise NotImplementedError("Complete this method")
```

Do not use `pragma: no cover` on this working method. Add a test that checks the returned answer and the new history entry. Then write `HistoryCommand`.


You may give CalculateCommand an optional label such as `add 5 3` so it can build a readable history string without printing or parsing input. The required jobs stay the same: execute, record success, return the result.

---

[Back to the contents](../README.md) · [Start with forking](00-fork-and-submit.md)

Next: [Step 6: Connect the CLI](07-step-6-connect-the-cli.md)
