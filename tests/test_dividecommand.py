'''Tests divide command'''
from decimal import Decimal

from app.commands.divide import DivideCommand

def test_divide_command_with_two_decimals():
    ''' Tests for 2-number args '''
    divide_command = DivideCommand()
    result = divide_command.execute('20', '5')
    assert result == Decimal('4'), "Should return the sum of two decimals"

def test_divide_command_with_incorrect_args():
    ''' Tests for incorrect args '''
    divide_command = DivideCommand()
    result = divide_command.execute('10.5')
    assert result == "Please use 'divide' command with two decimal numbers as parameters."

def test_divide_command_with_non_decimal_input():
    ''' Tests for wrong type args '''
    divide_command = DivideCommand()
    result = divide_command.execute('abc', 'xyz')
    assert result == "Invalid input. Please enter two decimal numbers."
