from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def name(request):
    return render(request, 'generator/name.html', {'name': str(input('Enter name:'))})

def password(request):
    pwd = ''
    character = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'))
    uppercase = request.GET.get('uppercase')
    number = request.GET.get('number')
    special_char = request.GET.get('special character')

    if uppercase:
        character.extend(list('JKLMNOPQRSTUVWXYZ'))
    if number:
        character.extend(list('1234567890'))
    if special_char:
        character.extend(list('!@#$%&*-_^&'))
    for x in range(length):
        pwd += random.choice(character)
    return render(request, 'generator/pwd.html', {'password': pwd})
