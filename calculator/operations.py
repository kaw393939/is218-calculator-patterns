"""Arithmetic strategies: each static method uses only its arguments."""


class Operations:
    @staticmethod
    def add(a: float, b: float) -> float:
        # No self or cls is needed because the answer depends only on a and b.
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
