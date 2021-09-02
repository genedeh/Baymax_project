from abc import ABC, abstractmethod


class InformationAbstraction(ABC):

    def __init__(self, info=None):
        if info is None and info is not dict:
            info = {}
        self.information = info

    @abstractmethod
    def get_information(self, info_name):
        pass

    @abstractmethod
    def set_information(self, info_name, info_value):
        pass

    @abstractmethod
    def change_information(self, info_name, new_info_value):
        pass
