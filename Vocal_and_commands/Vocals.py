import speech_recognition as sr
import pyttsx3


class Vocals:
    def speak(self, text):
        engine = pyttsx3.init()
        engine.setProperty('rate', 160)
        engine.setProperty('volume', 10.9)
        print(text)
        engine.say(text)
        engine.runAndWait()
        return text

    def take_command(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("||\/||\/||....")
            audio = recognizer.listen(source)

        try:
            print("RECOGNIZING...")
            query = recognizer.recognize_google(audio, language="en-uk")
            print(f"{query.capitalize()}.\n")

        except Exception as e:
            self.speak("Sorry I did not here you, come again.")
            query = None
        return query
