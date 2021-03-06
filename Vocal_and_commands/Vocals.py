from pprint import pprint

import speech_recognition as sr
import pyttsx3


class Vocals:
    def speak(self, text):
        engine = pyttsx3.init()
        engine.setProperty('rate', 197)
        engine.setProperty('volume', 2.7)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        pprint(text)
        engine.say(text)
        engine.runAndWait()
        return text

    def take_command(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print(f'==========\n"INITIALIZING"\n==========')
            self.speak(r",I AM LISTENING....")
            audio = recognizer.record(source, duration=4.10)

        try:
            query = recognizer.recognize_google(audio, language="en-us")
            print(f"{query.capitalize()}.\n")

        except Exception as e:
            self.speak("Sorry I did not hear you, come again.")
            query = ''
        return query