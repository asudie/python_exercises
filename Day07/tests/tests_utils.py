import pytest
from ex00.utils import get_user_input

def test_get_user_input_valid(monkeypatch):
    # Simulate valid user input (answering 1)
    monkeypatch.setattr('builtins.input', lambda _: "1")
    answers = ["Answer 1", "Answer 2", "Answer 3"]
    assert get_user_input(answers) == 1

def test_get_user_input_invalid_out_of_range(monkeypatch):
    # Simulate invalid user input (answering 0, then 4, then a valid 2)
    inputs = iter(["0", "4", "2"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    answers = ["Answer 1", "Answer 2", "Answer 3"]
    assert get_user_input(answers) == 2

def test_get_user_input_invalid_non_integer(monkeypatch):
    # Simulate invalid non-integer input ("abc", then a valid "3")
    inputs = iter(["abc", "3"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    answers = ["Answer 1", "Answer 2", "Answer 3"]
    assert get_user_input(answers) == 3
