

import os
from app.commands import Command


class MenuCommand(Command): 
    def execute(self): 

        print("Command Menu: ")
        commands_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'commands', '..', '..', ))
        # print (commands_path)
        folderIgnore = ['__pycache__', '__init__.py']
        for item in os.listdir(commands_path):
            # ignore pycache and other extraneous folders
            if item in folderIgnore: 
                continue
            print(item)
        print()