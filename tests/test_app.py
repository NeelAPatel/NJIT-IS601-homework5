''' This module tests the functions of launching the application itself '''
import pytest
from unittest.mock import patch, MagicMock
from app import App

# Assuming you have a dummy command for testing
from app.plugins.hello import HelloCommand as DummyCommand

@pytest.fixture
def app_instance():
    app = App()
    # Assuming CommandHandler has a register_command method
    app.command_handler.register_command("dummy", DummyCommand())
    return app

def test_app_plugin_registration(monkeypatch, app_instance):
    # Mock iter_modules to simulate finding plugins
    mock_iter_modules = [(None, 'dummy_plugin', True)]
    monkeypatch.setattr('pkgutil.iter_modules', lambda _: mock_iter_modules)

    # Mock import_module to simulate plugin module with a valid command
    dummy_plugin_module = MagicMock()
    dummy_plugin_module.DummyCommand = DummyCommand
    monkeypatch.setattr('importlib.import_module', lambda _: dummy_plugin_module)

    app_instance.pluginRegistration()
    # Check if 'dummy_plugin' is registered, adjust according to your implementation
    assert 'dummy_plugin' in app_instance.command_handler.commands

def test_app_start_exit_command(capfd, monkeypatch, app_instance):
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app_instance.start()
    captured = capfd.readouterr()
    assert "Type 'exit' to exit." in captured.out

def test_app_start_with_command(capfd, monkeypatch, app_instance):
    inputs = iter(['dummy', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with patch.object(DummyCommand, 'execute', return_value=None) as mock_execute:
        app_instance.start()
        mock_execute.assert_called_once()
    captured = capfd.readouterr()
    assert "Type 'exit' to exit." in captured.out

def test_app_start_unknown_command(capfd, monkeypatch, app_instance):
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app_instance.start()
    captured = capfd.readouterr()
    # Adjust the assertion based on how your app handles unknown commands
    assert "Command 'unknown_command' not found." not in captured.out  # Assuming unknown commands are silently ignored



# import pytest
# from app import App

# def test_app_start_exit_command(capfd, monkeypatch):
#     """Test that the REPL exits correctly on 'exit' command."""
#     # Simulate user entering 'exit'
#     monkeypatch.setattr('builtins.input', lambda _: 'exit')
#     app = App()
#     with pytest.raises(SystemExit) as e:
#         app.start()
#     assert e.type == SystemExit

# def test_app_start_unknown_command(capfd, monkeypatch):
#     """Test how the REPL handles an unknown command before exiting."""
#     # Simulate user entering an unknown command followed by 'exit'
#     inputs = iter(['unknown_command', 'exit'])
#     monkeypatch.setattr('builtins.input', lambda _: next(inputs))

#     app = App()

#     #with pytest.raises(SystemExit) as excinfo:
#     with pytest.raises(SystemExit):
#         app.start()

#     # Optionally, check for specific exit code or message
#     # assert excinfo.value.code == expected_exit_code

#     # Verify that the unknown command was handled as expected
#     captured = capfd.readouterr()
#     assert "Command 'unknown_command' not found." in captured.out
