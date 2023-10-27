from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from bootcamp.models import Koder
from bootcamp.query_exercises import (
    get_bootcamp_by_koder_last_name,
    get_mentor_koders_by_id,
    get_koders_excluding_last_bootcamp,
)


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


def get_ez_bootcamps(req):
    bootcamps = get_bootcamp_by_koder_last_name("ez")
    return render(req, "bootcamps.html", context={"bootcamps": bootcamps})


def get_ez_unique_bootcamps(req):
    bootcamps = get_bootcamp_by_koder_last_name("ez", True)
    return render(
        req, "bootcamps.html", context={"bootcamps": bootcamps, "are_unique": True}
    )


def get_generation_koders_by_mentor(req, mentor_id=1):
    [koders, mentor] = get_mentor_koders_by_id(mentor_id=mentor_id)
    return render(req, "koders.html", context={"koders": koders, "mentor": mentor})


def get_recent_koders(req):
    koders = get_koders_excluding_last_bootcamp()
    return render(req, "koders.html", context={"koders": koders})
