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

    def rename_dir(self, old_dir, new_dir):
        try:
            os.rename(old_dir, new_dir)
            self.vocal.speak("Source path renamed to destination was successfull.")
        except IsADirectoryError:
            self.vocal.speak("Source is a file but destination is a directory.")
        except NotADirectoryError:
            self.vocal.speak("Source is a directory but destination is a file.")
        except PermissionError:
            self.vocal.speak("Operation not permitted.")
        except OSError as error:
            self.vocal.speak(error)


dm = DirectoryManger()
dm.rename_dir('new_test', 'test')
