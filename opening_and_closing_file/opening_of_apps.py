import os
from abc import ABC


class AppOpening(ABC):
    def __set_up(self):
        pass

    def __init__(self):
        self.explore_apps_folder = r"start explorer shell:appsfolder"
        self.apps = {}


class WebsiteAppOpening(AppOpening):
    def __set_up(self):
        self.apps = {'Google chrome': 'Chrome', 'Microsoft Edge': 'MSEdge'}

    def open_google(self):
        self.__set_up()
        os.system(f'{self.explore_apps_folder}\{self.apps.get("Google chrome")}')
        return f"alright i'll open 'Chrome'"

    def open_edge(self):
        self.__set_up()
        os.system(f'{self.explore_apps_folder}\{self.apps.get("Microsoft Edge")}')


class WindowsAppOpening(AppOpening):
    def __set_up(self):
        self.apps = {'Windows Store': 'Microsoft.WindowsStore_8wekyb3d8bbwe!App',
                     'Word': 'Microsoft.Office.Word_8wekyb3d8bbwe!microsoft.word',
                     'Excel': 'Microsoft.Office.Excel_8wekyb3d8bbwe!microsoft.excel',
                     'Outlook': 'Microsoft.Office.OUTLOOK.EXE.15',
                     'PowerPoint': 'Microsoft.Office.POWERPNT.EXE.15',
                     'Publisher': 'Microsoft.Office.MSPUB.EXE.15',
                     'Access': 'Microsoft.Office.MSACCESS.EXE.15'}

    def open_word(self):
        self.__set_up()
        os.system(f'{self.explore_apps_folder}\{self.apps.get("Word")}')
        return f"alright i'll open 'Word'"

    def open_excel(self):
        self.__set_up()
        os.system(f'{self.explore_apps_folder}\{self.apps.get("Excel")}')
        return f"alright i'll open 'Excel'"

    def open_outlook(self):
        self.__set_up()
        os.system(f'{self.explore_apps_folder}\{self.apps.get("Outlook")}')
        return f"alright i'll open 'Outlook'"

    def open_power_point(self):
        self.__set_up()
        os.system(f'{self.explore_apps_folder}\{self.apps.get("PowerPoint")}')
        return f"alright i'll open 'PowerPoint'"

    def open_publisher(self):
        self.__set_up()
        os.system(f'{self.explore_apps_folder}\{self.apps.get("Publisher")}')
        return f"alright i'll open 'Publisher'"

    def open_access(self):
        self.__set_up()
        os.system(f'{self.explore_apps_folder}\{self.apps.get("Access")}')
        return f"alright i'll open 'Access'"

    def open_windows_store(self):
        self.__set_up()
        os.system(f'{self.explore_apps_folder}\{self.apps.get("Windows Store")}')
        return f"alright i'll open 'Windows Store'"


