import pytest
from app import App
from decimal import Decimal
from app import App

from app.commands.subtract import SubtractCommand

def test_subtract_command_with_two_decimals():
    subtract_command = SubtractCommand()
    result = subtract_command.execute('10.5', '20.3')
    assert result == Decimal('-9.8'), "Should return the difference of two decimals"

def test_subtract_command_with_incorrect_args():
    subtract_command = SubtractCommand()
    result = subtract_command.execute('10.5')
    assert result == "Please use 'subtract' command with two decimal numbers as parameters."

def test_subtract_command_with_non_decimal_input():
    subtract_command = SubtractCommand()
    result = subtract_command.execute('abc', 'xyz')
    assert result == "Invalid input. Please enter two decimal numbers."
