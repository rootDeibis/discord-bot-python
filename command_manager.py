from importlib.machinery import SourceFileLoader
from os import listdir, path

class CommandManager():
    commands = []

    def load(self,commands_dir: str):
        files = listdir(commands_dir)

        for file in files:
            filepath = path.join(commands_dir, file)

        
            if path.isfile(filepath):
                command_file = SourceFileLoader(file, filepath).load_module()
                command = command_file.command()
                self.commands.append(command)
    def find_command(self,name: str):
        cmd = None

        for command in self.commands:
            if command.name == name:
                cmd = command
                break;
        
        return cmd
