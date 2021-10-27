import pyttsx3
import speech_recognition as s
import os
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
while True:

    r=s.Recognizer()
    with s.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("say something")
        audio=r.listen(source)
        spoken_text=r.recognize_google(audio)

    if (spoken_text=="hello"):
        speak("hello sir")
    if (spoken_text=="introduce yourself"):
        speak("hi sir iam friday")
    if (spoken_text=="what is my hobby"):
        speak("drawings sir")
    if (spoken_text=="tell my name"):
        speak("Mr.Abhinav venkataramani")
    if ('open' in spoken_text):
        os.system('explorer C:\\{}'.format(spoken_text.replace("open ","")))
    if (spoken_text=="bye"):
        speak("bye sir")
        break
