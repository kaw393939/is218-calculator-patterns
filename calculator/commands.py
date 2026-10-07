"""Commands coordinate actions; the CLI is responsible for printing."""
from calculator.calculation import Calculation


class CalculateCommand:
    def __init__(self, calculation: Calculation, history: list[str],
                 label: str = "calculation"):
        # Receive a Calculation rather than hard-code how to do its math.
        self.calculation = calculation
        self.history = history
        self.label = label

    def execute(self) -> float:
        result = self.calculation.execute()
        # Append after execution: an exception cannot create a false success.
        self.history.append(f"{self.label} = {result}")
        return result


class HistoryCommand:
    def __init__(self, history: list[str]):
        self.history = history

    def execute(self) -> list[str]:
        # Copy the list so callers cannot append/remove from stored history.
        return self.history.copy()
