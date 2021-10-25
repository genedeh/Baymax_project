import os
from pprint import pprint

from Vocal_and_commands.Vocals import Vocals


class FileManager:
    def __init__(self):
        self.vocal = Vocals()

    def create_file(self, filename: str):
        with open(f'{filename}', 'w') as file:
            file.write("This file was created by Baymax File Management system")
        self.vocal.speak(f'{filename}, has been created')

    def read_file(self, filename: str):
        with open(f'{filename}', 'r') as file:
            content = file.read()
        self.vocal.speak(f'{filename}, has been read')
        return content

    def update_file(self, filename: str, content: str):
        with open(f'{filename}', '+a') as file:
            file.write(f" {content}")
        self.vocal.speak(f'{filename}, has been updated')

    def delete_file(self, filename: str):
        os.remove(filename)
        self.vocal.speak(f'{filename}, has been deleted')


class DirectoryManger:
    def __init__(self):
        self.vocal = Vocals()

    def create_dir(self, dir_name):
        os.mkdir(f'{dir_name}')
        self.vocal.speak(f"{dir_name} directory has been created")

    def list_files_in_dir(self, dir_name):
        dir_list = os.listdir(dir_name)
        self.vocal.speak(f"This are the files in {dir_name} directory")
        pprint(dir_list, width=10)


dm = DirectoryManger()
dm.list_files_in_dir('test')
