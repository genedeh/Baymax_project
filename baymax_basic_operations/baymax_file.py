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

    def update_file(self, filename: str, content: str):
        with open(f'{filename}', '+a') as file:
            file.write(f" {content}")
        vocal = Vocals()
        vocal.speak(f'{filename}, has been updated')


fm = FileManager()
fm.update_file('test.txt', 'Added an update method')
