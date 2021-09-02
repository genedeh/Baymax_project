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


class TestInformation(InformationAbstraction):
    def get_information(self, info_name):
        if info_name in self.information:
            return  self.information.get(info_name)
        else:
            return "not found"

    def set_information(self, info_name, info_value):
        if info_name not in self.information:
            self.information[info_name] = info_value
            return info_name
        else:
            return "found"

    def change_information(self, info_name, new_info_value):
        if info_name in self.information:
            self.information[info_name] = new_info_value
            return new_info_value
        else:
            return "not found"