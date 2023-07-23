from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import openai
# Create your views here.

from django.utils import timezone

openai_api_key = ''
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
    return render (request, 'Ai/about.html')


def register(request ):

    return render (request, 'Ai/registration.html')

def login(request ):
    return render (request, 'Ai/login.html')

def logout(request):
    return render (request, 'Ai/logout.html')