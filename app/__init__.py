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
                        if issubclass(item, (Command)):
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue  # Ignore if not class
            else: 
                continue

    def start(self):

        self.pluginRegistration()

        print("Type 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Print, Loop
            # register plugins
            self.command_handler.execute_command(input(">>> ").strip())
