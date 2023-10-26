from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from bootcamp.models import Koder

KODERS = [
    {"id": 0, "name": "Juan", "is_active": True},
    {"id": 1, "name": "Pedro", "is_active": False},
    {"id": 2, "name": "José", "is_active": True},
    {"id": 3, "name": "Cristian", "is_active": False},
    {"id": 4, "name": "John Doe", "is_active": True},
    {"id": 4, "name": "Johane Doe", "is_active": False},
]


def get_koder(request, id):
    founded_koder = Koder.objects.filter(pk=id).first()

    if isinstance(founded_koder, Koder):
        return render(request, "koders.html", context={"koders": [founded_koder]})
    else:
        return render(
            request,
            "error.html",
            context={"message": "Koder not found, please retry with a new id"},
        )


def list_koders(req):
    all_koders = Koder.objects.all()
    return render(req, "koders.html", context={"koders": all_koders})


def get_koder_type(req, name, type):
    return render(req, "type.html", context={"name": name, "type": type})
