# Step 2: Make operations with static methods

A static method needs only the values you give it. It does not need `self` or `cls`. Put the four arithmetic methods in `Operations`. Here is addition; write the other three.

```python
class Operations:
    @staticmethod
    def add(a: float, b: float) -> float:
        # This method uses only a and b. No object state is needed.
        return a + b
```

For division, raise `ValueError("Cannot divide by zero")` when the second number is zero. The CLI will catch that error and show its message.
Next: [Step 3: Make the calculation and its factory](04-step-3-make-the-calculation-and-its-factory.md)

---

[Back to the contents](../README.md) · [Start with forking](00-fork-and-submit.md)
