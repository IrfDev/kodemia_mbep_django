from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


KODERS = [
    {
        "id": 0,
        "name": "Juan",
    },
    {
        "id": 1,
        "name": "Pedro",
    },
    {
        "id": 2,
        "name": "José",
    },
    {
        "id": 3,
        "name": "Cristian",
    },
    {
        "id": 4,
        "name": "John Doe",
    },
    {
        "id": 4,
        "name": "Johane Doe",
    },
]


def get_koder(request, id):
    founded_koder = next((koder for koder in KODERS if koder["id"] == id), None)

    if isinstance(founded_koder, dict):
        return render(request, "koders.html", context={"koders": [founded_koder]})
    else:
        return HttpResponse("Koder not found")


def list_koders(req):
    li_koders = "".join([f"<li> {koder['name']} </li>" for koder in KODERS])
    koders_html = f"<h1>Koders</h1><ol>{li_koders}</ol>"
    return render(req, "koders.html", context={"koders": KODERS})


def get_koder_type(req, name, type):
    return render(req, "type.html", context={"name": name, "type": type})
