# Step 6: Connect the CLI

Put the loop in `cli.py`. Put only the code that starts it in `__main__.py`. Run it with `python -m calculator`.

For `add 5 3`, the path is: read input → choose `Operations.add` → create a calculation → create and execute a command → print the answer. Add a comment near this code explaining that path.
## Build the loop in small steps

1. Import Operations, ArithmeticCalculation, CalculateCommand, and HistoryCommand into `cli.py`. Write `def main():`.
2. Inside main, create the operation dictionary and one empty history list.
3. Start `while True`. Read `input("> ")` and split it into words. If input raises EOFError, stop. An empty line can simply start the next loop.
4. If the first word is `exit`, stop. If it is `history`, execute HistoryCommand and print its entries (or an empty-history message). These commands take no operands.
5. Otherwise, check that the name exists in the operation dictionary and that exactly two operands follow it. Show a helpful error and continue if either check fails.
6. Convert the operands with float(). Catch ValueError for invalid numbers, show a message, and continue.
7. Select the strategy, use the class factory, and build CalculateCommand. Execute it, print the answer, and catch ValueError for division by zero.
8. Let the loop ask for the next command. Do not catch every Exception: catch the expected input and math errors.

Here is a skeleton to fill in. The comments describe what you need to write; they are not a finished solution.

```python
from calculator.operations import Operations
from calculator.calculation import ArithmeticCalculation
from calculator.commands import CalculateCommand, HistoryCommand

def main():
    history = []
    # Create the operation dictionary here.
    while True:
        try:
            words = input("> ").split()
        except EOFError:
            break
        # Handle blank input, exit, and history.
        # Check the operation and operand count.
        # Convert the numbers, select the strategy, and build the pieces.
        # Execute the command and show its result or a helpful error.
```

Start by supporting one command, then add the others and errors. Save as you go.

## Make the entry point

Put this small file in `calculator/__main__.py`:

```python
from calculator.cli import main

# This only starts main(); test the behavior of main() directly.
if __name__ == "__main__":  # pragma: no cover
    main()
```

Run `python -m calculator` from the repository root. Type `add 5 3`, then `history`, then `exit`. For EOF in a real terminal use Ctrl-D on macOS/Linux, or Ctrl-Z then Enter on Windows.

Case-insensitive commands and skipping blank lines are useful choices, but are not extra grading requirements. The assignment covers ordinary numeric operands; extra handling of NaN/infinity is optional.


---

[Back to the contents](../README.md) · [Start with forking](00-fork-and-submit.md)

Next: [Step 7: Test the behavior and reach 100% coverage](08-step-7-test-the-behavior-and-reach-100-coverage.md)
