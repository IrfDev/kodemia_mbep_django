from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def welcome(request):
    "Welcome view"
    return HttpResponse("Bienvenido")


def greetings_with_name(req, name):
    return HttpResponse(f"<h1>Hallo {name}</h1>")


def greetings_koder(req, type):
    global GREETING_MESSAGE
    GREETING_MESSAGE = ""

    match type:
        case "mentor":
            GREETING_MESSAGE = f"Hello {type} here are your classes"
        case "koder":
            GREETING_MESSAGE = f"Hello {type} welcome to kodemia"
        case _:
            GREETING_MESSAGE = f"You're not welcome here"

    return HttpResponse(GREETING_MESSAGE)
