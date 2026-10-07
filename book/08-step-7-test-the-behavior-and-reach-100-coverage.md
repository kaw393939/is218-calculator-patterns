# Step 7: Test the behavior and reach 100% coverage

A test gives your code a known input and checks the answer. Coverage shows which lines your tests ran. **Require 100% line coverage across the entire `calculator` package.** Branch coverage is not required for this assignment. A high coverage number alone does not prove the answers are correct: use assertions.

* Test all four operations with normal values, including decimals, negatives, and zero.
* Test division by zero.
* Test that the factory creates a concrete calculation with the supplied values and operation.
* Test that the abstract class cannot be instantiated.
* Test calculations using different operation functions.
* Test command results, successful history entries, no entry after a failure, empty history, and the returned history copy.
* Test CLI success, unknown commands, wrong operand counts, invalid numbers, division by zero, continuing after errors, exit, and EOF. Use pytest's `monkeypatch` to supply input and `capsys` to check output.

Here is one test to get started:

```python
from calculator.operations import Operations

def test_add():
    assert Operations.add(5, 3) == 8
```

Run the same command locally and in GitHub Actions:

```bash
python -m pytest --cov=calculator --cov-report=term-missing --cov-fail-under=100
```

The command fails if tests fail or coverage is below 100%. The report lists missed lines so you know what to test next.

**You may use `# pragma: no cover`.** Use it for small lines with no useful behavior to test, such as an abstract placeholder or the entry point that only calls `main()`. Explain each exclusion in a nearby comment and list it briefly in STUDENT_README.md. Keep arithmetic, factory construction, commands, history, input parsing, and error handling covered by tests. Do not exclude whole working modules or lower the threshold to make the report pass.
## Testing a short CLI conversation

Once you have written `calculator.cli.main()`, this shows how to supply input without typing during a test:

```python
from calculator.cli import main

def test_cli_add_then_exit(monkeypatch, capsys):
    answers = iter(["add 5 3", "exit"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(answers))
    main()
    lines = capsys.readouterr().out.splitlines()
    assert any(line in ("8", "8.0") for line in lines)
```

For an EOF test, replace input with a function that raises `EOFError`:

```python
def test_cli_eof(monkeypatch, capsys):
    def end_of_input(prompt=""):
        raise EOFError
    monkeypatch.setattr("builtins.input", end_of_input)
    main()  # Must return without an uncaught exception.
```

Do not let a fake-input iterator run out accidentally: that raises StopIteration, which is different from input's EOFError. Supply `exit` in normal conversation tests. If your program prints the result with a label, assert the exact labeled line instead. Avoid only checking that output contains a digit; a wrong answer might contain the same digit.

 Add separate assertions for error messages and verify a later valid command still works. Test decimals with `pytest.approx` when appropriate.

Next: [Step 8: Run tests automatically on GitHub](09-step-8-run-tests-automatically-on-github.md)

---

[Back to the contents](../README.md) · [Start with forking](00-fork-and-submit.md)
