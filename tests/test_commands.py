import pytest
from calculator.calculation import Calculation, ArithmeticCalculation
from calculator.commands import CalculateCommand, HistoryCommand
from calculator.operations import Operations


class OtherCalculation(Calculation):
    """A second implementation that keeps the same numeric-result promise."""
    def execute(self):
        return self.operation(self.a, self.b)


@pytest.mark.parametrize("concrete", [ArithmeticCalculation, OtherCalculation])
def test_factory_and_command_accept_different_calculations(concrete):
    history = []
    calculation = concrete.create(5, 3, Operations.add)
    assert type(calculation) is concrete  # create uses cls, not a hard-coded class.
    assert CalculateCommand(calculation, history, "add 5 3").execute() == 8
    assert history == ["add 5 3 = 8"]


def test_successful_commands_share_ordered_history():
    history = []
    first = ArithmeticCalculation.create(5, 3, Operations.add)
    second = ArithmeticCalculation.create(6, 3, Operations.divide)
    assert CalculateCommand(first, history).execute() == 8
    assert CalculateCommand(second, history, "divide 6 3").execute() == 2
    assert HistoryCommand(history).execute() == ["calculation = 8", "divide 6 3 = 2.0"]


def test_failed_command_does_not_add_history():
    history = ["previous success"]
    calculation = ArithmeticCalculation.create(6, 0, Operations.divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        CalculateCommand(calculation, history).execute()
    assert history == ["previous success"]


def test_history_returns_a_copy():
    history = ["first", "second"]
    returned = HistoryCommand(history).execute()
    returned.pop()
    returned.append("changed")
    assert history == ["first", "second"]
    assert returned == ["first", "changed"]


def test_empty_history():
    assert HistoryCommand([]).execute() == []
