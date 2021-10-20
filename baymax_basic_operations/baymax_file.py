from Vocal_and_commands.Vocals import Vocals


class FileManager:
    def create_file(self, filename: str):
        with open(f'{filename}', 'w') as file:
            file.write("This file was created by Baymax File Management system")
        vocal = Vocals()
        vocal.speak(f'{filename}, has been created')

    def read_file(self, filename: str):
        with open(f'{filename}', 'r') as file:
            content = file.read()
        vocal = Vocals()
        vocal.speak(f'{filename}, has been read')
        return content


fm = FileManager()
print(fm.read_file('test.txt'))
