import speech_recognition as sr
import os
import time

r= sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)

try:
    print("You said " + r.recognize_google(audio))
    time.sleep(5)
    os.system("shutdown /s /t 1")
except LookupError:
    print("Could no understand audio")