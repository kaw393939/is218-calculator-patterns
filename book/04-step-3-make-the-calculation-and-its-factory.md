# Step 3: Make the calculation and its factory

A calculation holds two numbers and the operation to use. `self` means this particular object. `cls` means the class we called. The class method `create()` is our factory: it builds a calculation.

An abstract class is a shared promise. Every concrete calculation must provide `execute()`. Use `execute()` instead of `get_result()`. Put this starting code in `calculation.py` and keep comments explaining the method types.

```python
from abc import ABC, abstractmethod
from collections.abc import Callable

class Calculation(ABC):
    def __init__(self, a: float, b: float,
                 operation: Callable[[float, float], float]):
        # Each calculation owns its two numbers and chosen operation.
        self.a = a
        self.b = b
        self.operation = operation

    @classmethod
    def create(cls, a, b, operation):
        # cls is the concrete class that called create().
        # The factory builds a new object of that class.
        return cls(a, b, operation)

    @abstractmethod
    def execute(self) -> float:  # pragma: no cover
        # This is the promise; concrete classes supply the real work.
        # execute() replaces get_result() and returns the answer.
        pass

class ArithmeticCalculation(Calculation):
    def execute(self) -> float:
        # An instance method uses this calculation's stored values.
        return self.operation(self.a, self.b)
```

Call `ArithmeticCalculation.create(...)`, not `Calculation.create(...)`. The abstract class cannot be created directly. This is a simple factory method using `cls`; it does not choose between subclasses.

---

[Back to the contents](../README.md) · [Start with forking](00-fork-and-submit.md)

Next: [Step 4: Select the strategy from user input](05-step-4-select-the-strategy-from-user-input.md)
