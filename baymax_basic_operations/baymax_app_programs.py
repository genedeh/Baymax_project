# Import Required Library
from pprint import pprint
import sys

from Vocal_and_commands.Vocals import Vocals
from tkinter import *
import datetime
import time
import winsound
import googletrans
from googletrans import Translator
from threading import *

# Create Object
root = Tk()

# Set geometry
root.geometry("600x200")


# Use Threading
def Threading():
    t1 = Thread(target=alarm)
    t1.start()


vocals = Vocals()


def alarm():
    # Infinite Loop
    while True:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep(0.5)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"CURRENT TIME = {current_time} : ", f"TIME SET = {set_alarm_time}")

        if current_time == set_alarm_time:
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            vocals.speak(f"Times Up for {set_alarm_time}")
            break


# Add Labels, Frame, Button, Option's
Label(root, text="BayMax Alarm Clock", font="Saurabh 20 bold", fg="black").pack(pady=10)
Label(root, text="Set Time", font="Saurabh 25 bold", fg="red").pack()

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
         )
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(root, text="Set Alarm", font="Saurabh 15 bold", command=Threading, fg="blue").pack(pady=80)


# Execute Tkinter
def run():
    root.mainloop()


class Translator:
    def __init__(self, languages=googletrans.LANGUAGES):
        self.languages = languages

    def translate(self, sentence, to_language, from_language='en'):
        translator = Translator()
        print('translating stage 1')
        if from_language in self.languages and to_language in self.languages:
            sys.setrecursionlimit(10 ** 6)
            print('translating stage 2')
            translated_text = translator.translate(sentence, from_language=from_language, to_language=to_language)

            text = translated_text.text
            print(f'translating stage 1 {text} text')
            print(text)
        else:
            print("dose not exists")

    def get_languages(self):
        return pprint(self.languages, width=100)


class WebsiteDirector:
    def __init__(self, text: str):
        self.text = text
