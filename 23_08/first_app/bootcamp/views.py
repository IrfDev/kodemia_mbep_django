from django.shortcuts import render


from django.http import HttpResponse


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


def get_koder(req, id):
    founded_koder = next((koder for koder in KODERS if koder["id"] == id), None)

    if isinstance(founded_koder, dict):
        return HttpResponse(f"Koder founded: {founded_koder['name']}")
    else:
        return HttpResponse("Koder not found")


def list_koders(req):
    li_koders = "".join([f"<li> {koder['name']} </li>" for koder in KODERS])
    return HttpResponse(f"<h1>Koders</h1><ol>{li_koders}</ol>")
