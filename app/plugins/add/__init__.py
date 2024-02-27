from decimal import Decimal, InvalidOperation

from app.commands import Command


class AddCommand(Command):

    def execute(self, *args):
        # Check if the correct number of arguments is provided
        if len(args) != 2:
            return "Please use 'add' command with two decimal numbers as parameters."

        # Attempt to convert arguments to Decimal and add them
        try:
            a = Decimal(args[0])
            b = Decimal(args[1])
            return a + b
        except InvalidOperation:
            return "Invalid input. Please enter two decimal numbers."
