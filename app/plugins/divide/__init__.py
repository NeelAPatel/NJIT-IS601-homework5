from decimal import Decimal, InvalidOperation

from app.commands import Command


class DivideCommand(Command):

    def execute(self, *args):
        # Check if the correct number of arguments is provided
        if len(args) != 2:
            return "Please use 'divide' command with two decimal numbers as parameters."

        # Attempt to convert arguments to Decimal and divide them
        try:
            a = Decimal(args[0])
            b = Decimal(args[1])
            if (b == 0): 
                raise ZeroDivisionError("Cannot divide by zero.")
            
            return a / b
        except InvalidOperation:
            return "Invalid input. Please enter two decimal numbers."
        except ZeroDivisionError as e:
            return "Cannot divide by zero."
