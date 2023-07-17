from django.shortcuts import render, HttpResponse

# Create your views here.

def about(request):
    return render (request, 'Ai/about.html')


def home(request ):
    return render (request, 'Ai/base.html')