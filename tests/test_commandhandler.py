'''Tests divide command'''
from app.commands import Command, CommandHandler


def test_Command_class():
    pass

def test_Handler_IndexError(capsys):
    CommandHandler().execute_command(command_line="")
    captured = capsys.readouterr();

    assert captured.out == "No command entered.\n"


def test_Handler_IndexError(capsys):
    CommandHandler().execute_command(command_line="")
    captured = capsys.readouterr();

    assert captured.out == "No command entered.\n"

    