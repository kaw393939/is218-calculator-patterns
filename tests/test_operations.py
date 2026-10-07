import pytest
from calculator.operations import Operations


@pytest.mark.parametrize("operation,a,b,expected", [
    (Operations.add, 5, 3, 8),
    (Operations.add, -5, 3, -2),
    (Operations.add, 0, 0, 0),
    (Operations.add, 1.5, 2.25, 3.75),
    (Operations.subtract, 5, 3, 2),
    (Operations.subtract, -5, -3, -2),
    (Operations.subtract, 0, 0, 0),
    (Operations.subtract, 1.5, 0.25, 1.25),
    (Operations.multiply, 5, 3, 15),
    (Operations.multiply, -5, 3, -15),
    (Operations.multiply, 0, 7, 0),
    (Operations.multiply, 1.5, 2.5, 3.75),
    (Operations.divide, 6, 3, 2),
    (Operations.divide, -6, 3, -2),
    (Operations.divide, 0, 3, 0),
    (Operations.divide, 1, 3, 1 / 3),
    (Operations.divide, 1.5, 0.5, 3),
])
def test_arithmetic(operation, a, b, expected):
    assert operation(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("zero", [0, 0.0, -0.0])
def test_division_by_zero(zero):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Operations.divide(6, zero)
