import importlib
import pytest
from calculator.cli import main


def conversation(monkeypatch, capsys, commands):
    answers = iter(commands)

    def read(prompt=""):
        try:
            return next(answers)
        except StopIteration:
            # Real input raises EOFError when the stream ends.
            raise EOFError from None

    monkeypatch.setattr("builtins.input", read)
    main()
    return capsys.readouterr().out.splitlines()


@pytest.mark.parametrize("command,answer", [
    ("add 5 3", "8.0"),
    ("subtract 5 3", "2.0"),
    ("multiply -5 3", "-15.0"),
    ("divide 6 3", "2.0"),
    ("add 1.5 2.25", "3.75"),
    ("  ADD   5  3  ", "8.0"),
])
def test_success(monkeypatch, capsys, command, answer):
    assert conversation(monkeypatch, capsys, [command, "exit"]) == [answer, "Goodbye!"]


@pytest.mark.parametrize("bad_command,message", [
    ("power 5 3", "Error: unknown command; use add, subtract, multiply, divide, history, or exit"),
    ("add", "Error: use add followed by two numbers"),
    ("add 5", "Error: use add followed by two numbers"),
    ("add 5 3 2", "Error: use add followed by two numbers"),
    ("add x 3", "Error: enter valid numbers"),
    ("add 5 x", "Error: enter valid numbers"),
    ("divide 6 0", "Error: Cannot divide by zero"),
    ("history 5", "Error: history does not take numbers"),
    ("exit 5", "Error: exit does not take numbers"),
])
def test_error_then_valid_command(monkeypatch, capsys, bad_command, message):
    lines = conversation(monkeypatch, capsys, [bad_command, "add 5 3", "history", "exit"])
    assert lines == [message, "8.0", "add 5 3 = 8.0", "Goodbye!"]


def test_history_lists_successes_in_order(monkeypatch, capsys):
    assert conversation(monkeypatch, capsys, ["add 5 3", "multiply 4 6", "history", "exit"]) == [
        "8.0", "24.0", "add 5 3 = 8.0", "multiply 4 6 = 24.0", "Goodbye!"
    ]


def test_empty_history(monkeypatch, capsys):
    assert conversation(monkeypatch, capsys, ["history", "exit"]) == ["History is empty", "Goodbye!"]


def test_blank_line_does_not_create_history(monkeypatch, capsys):
    assert conversation(monkeypatch, capsys, ["   ", "history", "exit"]) == ["History is empty", "Goodbye!"]


def test_eof_without_commands(monkeypatch, capsys):
    assert conversation(monkeypatch, capsys, []) == ["Goodbye!"]


def test_eof_after_success(monkeypatch, capsys):
    assert conversation(monkeypatch, capsys, ["add 5 3"]) == ["8.0", "Goodbye!"]


def test_importing_entrypoint_does_not_start_input(monkeypatch):
    def unexpected_input(prompt=""):
        raise AssertionError("Importing the package must not start the CLI")
    monkeypatch.setattr("builtins.input", unexpected_input)
    assert importlib.import_module("calculator.__main__").main is main
