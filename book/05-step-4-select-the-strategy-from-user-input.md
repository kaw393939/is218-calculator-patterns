# Step 4: Select the strategy from user input

Before using the four-operation dictionary below, finish the other three methods in Step 2. This dictionary and the final two lines are fragments for your CLI, not a complete program.

A strategy is a way to do a job. Here, the operation functions are the strategies. The CLI selects one from a dictionary; the selected function does the arithmetic.

Try the already-working addition strategy first:

```python
from calculator.operations import Operations
from calculator.calculation import ArithmeticCalculation

calculation = ArithmeticCalculation.create(5, 3, Operations.add)
print(calculation.execute())  # 8
```

```python
from calculator.operations import Operations
from calculator.calculation import ArithmeticCalculation

operations = {
    "add": Operations.add,
    "subtract": Operations.subtract,
    "multiply": Operations.multiply,
    "divide": Operations.divide,
}

# After checking the command and converting the two numbers:
operation = operations[command_name]
calculation = ArithmeticCalculation.create(a, b, operation)
```

Check that the command exists before looking it up. Convert operands with `float()` and catch invalid input. No separate strategy class is required.
Next: [Step 5: Let a command run the calculation](06-step-5-let-a-command-run-the-calculation.md)

---

[Back to the contents](../README.md) · [Start with forking](00-fork-and-submit.md)
