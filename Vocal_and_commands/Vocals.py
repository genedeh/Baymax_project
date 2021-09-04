import speech_recognition as sr
import pyttsx3


class Vocals:
    def speak(self, text):
        engine = pyttsx3.init()
        engine.setProperty('rate', 100.10)
        engine.setProperty('volume', 1.9)
        print(text)
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
            self.speak("RECOGNIZING...")
            query = recognizer.recognize_google(audio, language="en-us")
            print(f"{query.capitalize()}.\n")

        except Exception as e:
            self.speak("Sorry I did not here you, come again.")
            query = ''
        return query
