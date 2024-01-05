"""views"""

from random import choice
from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

#! no olvidar ingresar la app dentro del setings


def about(request):
    """this_is_about"""
    #! debe ir con comillas simples ''
    return render(request, 'about.html')


def home(request):
    """this_is_home"""
    return render(request, 'home.html')


def password(request):
    """ruta_generator"""
    characters = list("abcdefghijklmnñopqrstuvwxyz")
    generated_password = ""

    length = int(request.GET.get("length"))
    uppercase = request.GET.get("uppercase")
    numbers = request.GET.get("numbers")
    specials = request.GET.get("specials")

    if uppercase:
        characters.extend(list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"))

    if numbers:
        characters.extend(list("0123456789"))

    if specials:
        characters.extend(list("*/@#$%^&+=-_.?!|<>"))

    for _ in range(length):
        generated_password += choice(characters)

    return render(request, 'password.html', {"password": generated_password})
