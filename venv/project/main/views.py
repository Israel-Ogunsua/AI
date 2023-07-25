from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import openai
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyttsx3
import pyaudio

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
# Create your views here.

from django.utils import timezone

openai_api_key = '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'
openai.api_key = openai_api_key

def ask_openai(message):
    # Use the input 'message' parameter as the user's input
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message},  # Use the 'message' parameter here
        ]
    )
    
    print( response)
    # Retrieve and return the assistant's response
    answer = response.choices[0].message['content'].strip()
    return answer


def home(request ):
    if request.method == 'POST':
        message = request.POST.get('message')
        print(message)
        response = ask_openai(message) 
        return JsonResponse({'message': message, 'response': response})
    return render (request, 'Ai/home.html')

def setting(request ):
    return render (request, 'Ai/setting.html')




def about(request):
    engine.say("I am Israel your voice assistance")
    engine.say("What can I do for you today?")
    #engine.runAndWait()

    #say_someting()
    return render (request, 'Ai/about.html')

def talk(text):
    engine.say(text)
    engine.runAndWait()


def say_someting():
        with sr.Microphone() as source:
            print("Speaking...")
            voice = listener.listen(source)
            try:
               action = listener.recognize_google(voice,language='en-USA')
               
            except:
                print("Couldn't hear you")
                action = listener.recognize_google(voice,language='en-USA')
            #action = action.lower()
           
            talk(action)

            if 'david' in action:
                action = action.replace("david","")
                print(action)

            elif "play" in action:
                song = action.replace("play","")
                print("playing.....")
                talk("playing" + song)
                pywhatkit.playonyt(song)

            elif "play me" in action:
                song = action.replace("play me","")
                print("playing.....")
                talk("playing" + song)
                pywhatkit.playonyt(song)

            elif "time" in action:
                time = datetime.datetime.now().strftime("%I:%M %p")
                print(time)
                talk("The current time is" + time)

            elif 'who' in action:
                discription = action.replace("who", "")
                information = wikipedia.summary(discription, 8)
                print(information)
                talk(information)

            else:
                talk('Can you say that again') 

        return action



def register(request ):

    return render (request, 'Ai/registration.html')

def login(request ):
    return render (request, 'Ai/login.html')

def logout(request):
    return render (request, 'Ai/logout.html')