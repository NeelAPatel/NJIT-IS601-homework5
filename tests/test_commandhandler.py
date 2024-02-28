'''Tests Command Handler'''
from app.commands import Command, CommandHandler

# Create a concrete subclass of Command for testing purposes
class TestCommand(Command):
    ''' Concrete subclass for testing '''
    def execute(self):
        ''' executes concrete subclass'''
        return "Test command executed"

# Define the test function for the concrete implementation
def test_command_execute():
    ''' tests the Command Class's instaniation'''
    command_instance = TestCommand()
    result = command_instance.execute()
    assert result == "Test command executed", "The execute method should return 'Test command executed'"

def test_handler_index_error(capsys):
    ''' tests index error occurance'''
    CommandHandler().execute_command(command_line="")
    captured = capsys.readouterr()

    assert captured.out == "No command entered.\n"
