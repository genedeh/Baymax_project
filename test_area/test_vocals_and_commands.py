from Vocal_and_commands.Vocals import Vocals
import unittest


class VocalsTest(unittest.TestCase):
    def setUp(self):
        self.vocal = Vocals()

    def test_speak_type(self):
        speech = self.vocal.speak('')
        self.assertIsInstance(speech, str)
