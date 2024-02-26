import os
from importlib import import_module

from app.commands import CommandHandler
from app.commands.add import AddCommand
from app.commands.exit import ExitCommand
from app.commands.hello import HelloCommand
from app.commands.subtract import SubtractCommand

class App: 
    def __init__(self) -> None:
        self.command_handler = CommandHandler()

    def start(self):
        # Register commands here
        self.command_handler.register_command("hello", HelloCommand())
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        
        # self.command_handler.register_command("menu", MenuCommand())
        # self.command_handler.register_command("discord", DiscordCommand())

        print("Type 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Print, Loop
            self.command_handler.execute_command(input(">>> ").strip())





    # def start(self): 
    #     #Looped Command Registration 
    #     # self.command_handler.register

    #     commands_path = os.path.join(os.path.dirname(__file__), 'commands')
    #     for item in os.listdir(commands_path):
    #         try:
    #             # Check if the item is a directory and construct the path to it
    #             item_path = os.path.join(commands_path, item)
    #             if not os.path.isdir(item_path):
    #                 continue

    #             # Dynamically import the command module
    #             command_module = import_module(f'.commands.{item}', 'app')

    #             # Assume the class is named with the format: CommandnameCommand (e.g., AddCommand)
    #             command_class_name = f'{item.capitalize()}Command'
    #             command_class = getattr(command_module, command_class_name)

    #             # Instantiate the command class
    #             command_instance = command_class()

    #             # Register the command with the command handler
    #             self.command_handler.register_command(item, command_instance)

    #         except Exception as e:
    #             # Handle any errors in command registration
    #             print(f'An error occurred while registering the command {item}: {e}')
