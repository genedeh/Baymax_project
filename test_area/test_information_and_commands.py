import unittest
from infomation_and_commands.infomation_abstraction import TestInformation


class InfoTest(unittest.TestCase):
    def setUp(self) -> None:
        self.test_info = TestInformation({"name": "Genesis", "age": "12"})

    def test_get_info(self):
        test_get_info = self.test_info.get_information('age')
        self.assertEqual("12", test_get_info)

    def test_set_info(self):
        test_set_info = self.test_info.set_information('gender', 'male')
        self.assertIn(test_set_info, self.test_info.information)

    def test_changed_info(self):
        test_changed_info = self.test_info.change_information('age', '13')
        print(self.test_info.information)
