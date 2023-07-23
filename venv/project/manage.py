#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


# import speech_recognition as sr
# import pywhatkit
# import datetime
# import wikipedia
# import pyttsx3

# #Start by creating a listiner 
# listener = sr.Recognizer()
# engine = pyttsx3.init()
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[1].id)
# engine.say("I am Israel your voice assistance")
# engine.say("What can I do for you today?")
# engine.runAndWait()

# def talk(text):
#     engine.say(text)
#     engine.runAndWait()


# def say_someting():
#         with sr.Microphone() as source:
#             print("Speaking...")
#             voice = listener.listen(source)
#             action = listener.recognize_google(voice)
#             #action = action.lower()
#             talk(action)

#             if 'david' in action:
#                 action = action.replace("david","")
#                 print(action)

#             elif "play" in action:
#                 song = action.replace("play","")
#                 print("playing.....")
#                 talk("playing" + song)
#                 pywhatkit.playonyt(song)

#             elif "play me" in action:
#                 song = action.replace("play me","")
#                 print("playing.....")
#                 talk("playing" + song)
#                 pywhatkit.playonyt(song)

#             elif "time" in action:
#                 time = datetime.datetime.now().strftime("%I:%M %p")
#                 print(time)
#                 talk("The current time is" + time)

#             elif 'who' in action:
#                 discription = action.replace("who", "")
#                 information = wikipedia.summary(discription, 8)
#                 print(information)
#                 talk(information)

#             else:
#                 talk('Can you say that again') 

#         return action

# def run():
#         command = say_someting()
#         return command

  

if __name__ == '__main__':
    main()
    # run() 
