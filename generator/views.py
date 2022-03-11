from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import random

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    the_pass = ""

    characters = list('acdefghijklmnopqrstuvwxyz')

    if request.GET.get('upper'):
        characters.extend(list(('acdefghijklmnopqrstuvwxyz').upper()))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    lenght = int(request.GET.get('length',10))

    for x in range(lenght):
        the_pass += random.choice(characters)

    return render(request, 'generator/password.html', {'password': the_pass})

def about(request):

    return render(request, 'generator/about.html')