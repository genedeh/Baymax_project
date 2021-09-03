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


class PersonalAppOpening(AppOpening):
    def __set_up(self):
        self.apps = {'Alarms and clock': 'Microsoft.WindowsAlarms_8wekyb3d8bbwe!App',
                     'Calculator': 'Microsoft.WindowsCalculator_8wekyb3d8bbwe!App',
                     'Camera': 'Microsoft.WindowsCamera_8wekyb3d8bbwe!App',
                     'Contact Support': 'Windows.ContactSupport_cw5n1h2txyewy!App',
                     'Cortana': 'Microsoft.Windows.Cortana_cw5n1h2txyewy!CortanaUI',
                     'Facebook': 'Microsoft.MSFacebook_8wekyb3d8bbwe!x82a236355bd9df11a84400237de2db9e',
                     'File Explorer': 'c5e2524a-ea46-4f67-841f-6a9465d9d515_cw5n1h2txyewy!App',
                     'Groove Music': 'Microsoft.ZuneMusic_8wekyb3d8bbwe!Microsoft.ZuneMusic',
                     'Maps': 'Microsoft.WindowsMaps_8wekyb3d8bbwe!App',
                     'Movies and TV	': 'Microsoft.ZuneVideo_8wekyb3d8bbwe!Microsoft.ZuneVideo',
                     'News': 'Microsoft.BingNews_8wekyb3d8bbwe!AppexNews',
                     'Photos': 'Microsoft.Windows.Photos_8wekyb3d8bbwe!App',
                     'Settings': '2a4e62d8-8809-4787-89f8-69d0f01654fb_8wekyb3d8bbwe!App',
                     'Skype': 'Microsoft.SkypeApp_kzf8qxf38zg5c!Skype.AppId',
                     'Voice recorder': 'Microsoft.WindowsSoundRecorder_8wekyb3d8bbwe!App',
                     'Weather': 'Microsoft.BingWeather_8wekyb3d8bbwe!App',
                     'Xbox': 'Microsoft.XboxApp_8wekyb3d8bbwe!Microsoft.XboxApp'}
