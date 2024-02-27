import importlib
import os
import pkgutil

from app.commands import CommandHandler, Command

class App: 
    def __init__(self):
        self.command_handler = CommandHandler()


    def pluginRegistration(self): 
        # Dynamically load all plugins in the plugins directory
        pluginPath = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([pluginPath.replace('.', '/')]):
            #For each item, item's name, and pkgFlag in path's list... 

            if is_pkg:  # Ensure it's a package
                
                #Grabs module aka the plugin package folder
                plugin_module = importlib.import_module(f'{pluginPath}.{plugin_name}')

                # for each item in folder, check if theres a subclass and register it as a command
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):  # Assuming a BaseCommand class exists
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore
            else: 
                continue
    


    def start(self):


        self.pluginRegistration()

        print("Type 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Print, Loop
            # register plugins
            self.command_handler.execute_command(input(">>> ").strip())

    
    # def startX(self): 
    #     #Looped Command Registration 
    #     # self.command_handler.register

    #     commands_path = os.path.join(os.path.dirname(__file__), 'commands')
    #     folderIgnore = ['__pycache__']
    #     for item in os.listdir(commands_path):
    #         try:
    #             # Check if the item is a directory and construct the path to it
    #             item_path = os.path.join(commands_path, item)
    #             if not os.path.isdir(item_path):
    #                 continue
                
    #             # ignore pycache and other extraneous folders
    #             if item in folderIgnore: 
    #                 continue
                
    #             #== Everything is good --> Build the registry
    #             # Assume the class is named with the format: CommandnameCommand (e.g., AddCommand)
    #             command_class_name = f'{item.capitalize()}Command' # generating command name 
    #             command_module = importlib.import_module(f'.commands.{item}', 'app')
    #             command_class = getattr(command_module, command_class_name) #pairing module and class together

    #             # Instantiate the command class
    #             command_instance = command_class()

    #             # Register the command with the command handler
    #             self.command_handler.register_command(item, command_instance)

    #         except Exception as e:
    #             # Handle any errors in command registration
    #             print(f'An error occurred while registering the command {item}: {e}')

    #     print("Type 'exit y' to exit.")
    #     while True:  #REPL Read, Evaluate, Print, Loop
    #         result = self.command_handler.execute_command(input(">>> ").strip()) 
            
    #         if result is not None:
    #             print(result)
