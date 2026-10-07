"""Read a command, choose the pieces, and display the outcome."""
from calculator.calculation import ArithmeticCalculation
from calculator.commands import CalculateCommand, HistoryCommand
from calculator.operations import Operations


def main() -> None:
    operations = {
        "add": Operations.add,
        "subtract": Operations.subtract,
        "multiply": Operations.multiply,
        "divide": Operations.divide,
    }
    history: list[str] = []

    while True:
        try:
            parts = input("> ").split()
        except EOFError:
            print("Goodbye!")
            break

        if not parts:
            continue
        name = parts[0].lower()

        if name in ("exit", "history"):
            if len(parts) != 1:
                print(f"Error: {name} does not take numbers")
                continue
            if name == "exit":
                print("Goodbye!")
                break
            entries = HistoryCommand(history).execute()
            if entries:
                for entry in entries:
                    print(entry)
            else:
                print("History is empty")
            continue

        if name not in operations:
            print("Error: unknown command; use add, subtract, multiply, divide, history, or exit")
            continue
        if len(parts) != 3:
            print(f"Error: use {name} followed by two numbers")
            continue

        try:
            a, b = float(parts[1]), float(parts[2])
        except ValueError:
            print("Error: enter valid numbers")
            continue

        # Input selects the strategy; the factory builds the calculation.
        # The command executes it and records success; the CLI prints its result.
        calculation = ArithmeticCalculation.create(a, b, operations[name])
        command = CalculateCommand(calculation, history,
                                   f"{name} {parts[1]} {parts[2]}")
        try:
            print(command.execute())
        except ValueError as error:
            print(f"Error: {error}")
