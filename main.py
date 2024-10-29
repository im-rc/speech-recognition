# This is a sample Python script.

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            text = text.lower()

            print(f"Recognized text: {text}")
    except:
        print("you are trying to be funny")
        r = sr.Recognizer()
        continue
