import os
from abc import ABC


class AppOpening(ABC):
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



