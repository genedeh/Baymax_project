import os
from abc import ABC, abstractmethod


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
        os.system(fr'{self.explore_apps_folder}\{self.apps.get("Google chrome")}')
        return f"alright i'll open 'Chrome'"

    def open_edge(self):
        self.__set_up()
        os.system(fr'{self.explore_apps_folder}\{self.apps.get("Microsoft Edge")}')


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
        os.system(fr'{self.explore_apps_folder}\{self.apps.get("Word")}')
        return f"alright i'll open 'Word'"

    def open_excel(self):
        self.__set_up()
        os.system(fr'{self.explore_apps_folder}\{self.apps.get("Excel")}')
        return f"alright i'll open 'Excel'"

    def open_outlook(self):
        self.__set_up()
        os.system(fr'{self.explore_apps_folder}\{self.apps.get("Outlook")}')
        return f"alright i'll open 'Outlook'"

    def open_power_point(self):
        self.__set_up()
        os.system(fr'{self.explore_apps_folder}\{self.apps.get("PowerPoint")}')
        return f"alright i'll open 'PowerPoint'"

    def open_publisher(self):
        self.__set_up()
        os.system(fr'{self.explore_apps_folder}\{self.apps.get("Publisher")}')
        return f"alright i'll open 'Publisher'"

    def open_access(self):
        self.__set_up()
        os.system(fr'{self.explore_apps_folder}\{self.apps.get("Access")}')
        return f"alright i'll open 'Access'"

    def open_windows_store(self):
        self.__set_up()
        os.system(fr'{self.explore_apps_folder}\{self.apps.get("Windows Store")}')
        return f"alright i'll open 'Windows Store'"


class PersonalAppOpening(AppOpening):
    def __set_up(self):
        self.apps = {'Alarms and clock': 'Microsoft.WindowsAlarms_8wekyb3d8bbwe!App',
                     'Calculator': 'Microsoft.WindowsCalculator_8wekyb3d8bbwe!App',
                     'Camera': 'Microsoft.WindowsCamera_8wekyb3d8bbwe!App',
                     'File Explorer': 'c5e2524a-ea46-4f67-841f-6a9465d9d515_cw5n1h2txyewy!App',
                     'Groove Music': 'Microsoft.ZuneMusic_8wekyb3d8bbwe!Microsoft.ZuneMusic',
                     'Maps': 'Microsoft.WindowsMaps_8wekyb3d8bbwe!App',
                     'Movies and TV': 'Microsoft.ZuneVideo_8wekyb3d8bbwe!Microsoft.ZuneVideo',
                     'News': 'Microsoft.BingNews_8wekyb3d8bbwe!AppexNews',
                     'Photos': 'Microsoft.Windows.Photos_8wekyb3d8bbwe!App',
                     'Calendar': 'Microsoft.WindowsCommunicationsApps_8wekyb3d8bbwe!Microsoft.WindowsLive.Calendar',
                     'Skype': 'Microsoft.SkypeApp_kzf8qxf38zg5c!App',
                     'Voice recorder': 'Microsoft.WindowsSoundRecorder_8wekyb3d8bbwe!App',
                     'Weather': 'Microsoft.BingWeather_8wekyb3d8bbwe!App',
                     'Paint 3D': 'Microsoft.MSPaint_8wekyb3d8bbwe!Microsoft.MSPaint',
                     'Xbox': 'Microsoft.XboxApp_8wekyb3d8bbwe!Microsoft.XboxApp'}

    def open_alarms_and_clock(self):
        self.__set_up()
        os.system(fr'{self.explore_apps_folder}\{self.apps.get("Alarms and clock")}')
        return "alright i'll open 'Alarms and clock"

    def open_calculator(self):
        self.__set_up()
        os.system(fr'{self.explore_apps_folder}\{self.apps.get("Calculator")}')
        return "alright i'll open 'Calculator"

    def open_camera(self):
        self.__set_up()
        os.system(fr'{self.explore_apps_folder}\{self.apps.get("Camera")}')
        return "alright i'll open 'Camera"

    def open_file_explorer(self):
        self.__set_up()
        os.system(fr'{self.explore_apps_folder}\{self.apps.get("File Explorer")}')
        return "alright i'll open 'File Explorer"

    def open_music(self):
        self.__set_up()
        os.system(fr'{self.explore_apps_folder}\{self.apps.get("Groove Music")}')
        return "alright i'll open 'Music"

    def open_map(self):
        self.__set_up()
        os.system(fr'{self.explore_apps_folder}\{self.apps.get("Maps")}')
        return "alright i'll open 'Map"

    def open_movies(self):
        self.__set_up()
        os.system(fr'{self.explore_apps_folder}\{self.apps.get("Movies and TV")}')
        return "alright i'll open 'Movies and TV"

    def open_news(self):
        self.__set_up()
        os.system(fr'{self.explore_apps_folder}\{self.apps.get("News")}')
        return "alright i'll open 'News"

    def open_photos(self):
        self.__set_up()
        os.system(fr'{self.explore_apps_folder}\{self.apps.get("Photos")}')
        return "alright i'll open 'Photos"

    def open_calendar(self):
        self.__set_up()
        os.system(fr'{self.explore_apps_folder}\{self.apps.get("Calendar")}')
        return "alright i'll open 'Calendar"

    def open_skype(self):
        self.__set_up()
        os.system(fr'{self.explore_apps_folder}\{self.apps.get("Skype")}')
        return "alright i'll open 'Skype"

    def open_voice_recorder(self):
        self.__set_up()
        os.system(fr'{self.explore_apps_folder}\{self.apps.get("Voice recorder")}')
        return "alright i'll open 'Voice recorder"

    def open_weather(self):
        self.__set_up()
        os.system(fr'{self.explore_apps_folder}\{self.apps.get("Weather")}')
        return "alright i'll open 'Weather"

    def open_paint_3D(self):
        self.__set_up()
        os.system(fr'{self.explore_apps_folder}\{self.apps.get("Paint 3D")}')
        return "alright i'll open 'Paint 3D"

    def open_xbox(self):
        self.__set_up()
        os.system(fr'{self.explore_apps_folder}\{self.apps.get("Xbox")}')
        return "alright i'll open 'Xbox"
