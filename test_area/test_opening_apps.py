import unittest
from opening_apps.opening_of_apps import PersonalAppOpening, WebsiteAppOpening, WindowsAppOpening, AppOpening


class TestWebsiteOpeningApps(unittest.TestCase):
    def setUp(self) -> None:
        self.website_app_opening = WebsiteAppOpening()

    def test_website_return(self):
        self.assertEqual("alright i'll open 'Chrome'", self.website_app_opening.open_google())

    def test_website_class_instance(self):
        self.assertIsInstance(self.website_app_opening, AppOpening)


class TestWindowOpeningApps(unittest.TestCase):
    def setUp(self) -> None:
        self.window_app_opening = WindowsAppOpening()

    def test_window_return(self):
        self.assertEqual("alright i'll open 'Windows Store'", self.window_app_opening.open_windows_store())

    def test_window_class_instance(self):
        self.assertIsInstance(self.window_app_opening, AppOpening)


class TestPersonalOpeningApps(unittest.TestCase):
    def setUp(self) -> None:
        self.personal_app_opening = PersonalAppOpening()

    def test_personal_return(self):
        self.assertEqual("alright i'll open 'Movies and TV", self.personal_app_opening.open_movies())

    def test_personal_class_instance(self):
        self.assertIsInstance(self.personal_app_opening, AppOpening)
