''' This module tests the functions of launching the application itself '''
import pytest
from unittest.mock import patch, MagicMock
from app import App

# from app.commands import Command


# class ValidCommand(Command):
#     '''# Mock plugin structure'''
#     def execute(self):
#         pass

# invalid_item = "I should be ignored"
# AnotherClass = object  # Not subclassing Command

# # Test function
# def test_plugin_registration_skips_invalid_items():
#     with patch('pkgutil.iter_modules') as mock_iter_modules, \
#          patch('importlib.import_module') as mock_import_module:

#         # Mock iter_modules to return a single plugin
#         mock_iter_modules.return_value = [(None, 'mock_plugin', True)]

#         # Mock import_module to return a module with both valid and invalid items
#         mock_plugin_module = MagicMock()
#         mock_plugin_module.ValidCommand = ValidCommand
#         mock_plugin_module.invalid_item = invalid_item
#         mock_plugin_module.AnotherClass = AnotherClass
#         mock_import_module.return_value = mock_plugin_module

#         # Instantiate App and call pluginRegistration
#         app_instance = App()
#         app_instance.pluginRegistration()

#         # Verify that the CommandHandler registered only the ValidCommand
#         # This assumes your CommandHandler has a way to check registered commands, adjust accordingly
#         assert 'mock_plugin' in app_instance.command_handler.commands
#         assert isinstance(app_instance.command_handler.commands['mock_plugin'], ValidCommand)
#         assert 'invalid_item' not in app_instance.command_handler.commands
#         assert 'AnotherClass' not in app_instance.command_handler.commands

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    #with pytest.raises(SystemExit) as excinfo:
    with pytest.raises(SystemExit):
        app.start()

    # Optionally, check for specific exit code or message
    # assert excinfo.value.code == expected_exit_code

    # Verify that the unknown command was handled as expected
    captured = capfd.readouterr()
    assert "Command 'unknown_command' not found." in captured.out
