from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class CommandHandler:
    def __init__(self):
        self.commands = {} # Stores Dictionary of commands that are registered

    def register_command(self, command_name: str, command: Command):
        ''' Any new Command_Name and Command-type command are passed in, 
        Register them into self.commands Dictonary such that key = command_name and command is the value'''
        self.commands[command_name] = command
        

    # def execute_command(self, command_name: str):
    #     """Easier to ask for forgiveness than permission (EAFP) - Use when its going to most likely work"""
    #     try:
    #         self.commands[command_name].execute()
    #     except KeyError:
    #         print(f"No such command: {command_name}")

    
    def execute_command(self, command_line):
        try:
            parts = command_line.split()
            command_name = parts[0]
        except IndexError:
            print("No command entered.")
            return
        
        command = self.commands.get(command_name)
        
        if command:
            args = parts[1:]
            try:
                result = command.execute(*args)
                print(result)
            except Exception as e:
                print(f"Error executing command '{command_name}': {e}")
        else:
            print(f"Command '{command_name}' not found.")