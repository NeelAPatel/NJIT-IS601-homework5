from decimal import Decimal, InvalidOperation, getcontext

from app.commands import Command

class SqrtCommand(Command):
    def execute(self, *args):
        # Set precision for Decimal operations if necessary
        getcontext().prec = 10  # Example precision setting

        # Check if the correct number of arguments is provided
        if len(args) != 1:
            return "Please use 'sqrt' command with one decimal number as a parameter."

        # Attempt to convert argument to Decimal and calculate the square root
        try:
            value = Decimal(args[0])
            return value.sqrt()
        except InvalidOperation:
            return "Invalid input. Please enter a valid decimal number."
