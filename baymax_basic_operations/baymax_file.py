from Vocal_and_commands.Vocals import Vocals


class FileManager:
    def create_file(self, filename: str):
        with open(f'{filename}', 'w') as file:
            file.write("This file was created by Baymax File Management system")
        vocal = Vocals()
        vocal.speak(f'{filename}, has been created')


fm = FileManager()
fm.create_file('test.txt')