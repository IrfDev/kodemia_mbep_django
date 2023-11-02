from django.shortcuts import render
from app.usecases.psycologist import get_all_psychologists, get_psychologist_by_id
from app.usecases.patient import get_all_patients, get_patient_by_id
from app.usecases.appointments import get_all_appointments, get_appointment_by_id

# Create your views here.


def list_psychologists(req):
    psychologists = get_all_psychologists(is_list=True)
    return render(req, "psychologists.html", context={"psychologists": psychologists})


def get_psychologist(req, id):
    psychologists = get_psychologist_by_id(id)
    return render(req, "psychologists.html", context={"psychologists": [psychologists]})


def list_patients(req):
    patients = get_all_patients(is_list=True)
    return render(req, "patients.html", context={"patients": patients})


def get_patient(req, id):
    patient = get_patient_by_id(id)
    return render(req, "patients.html", context={"patients": [patient]})


def list_appointments(req):
    appointments = get_all_appointments(is_list=True)
    return render(req, "appointments.html", context={"appointments": appointments})


def get_appointment(req, id):
    appointment = get_appointment_by_id(id)
    return render(req, "appointments.html", context={"appointments": [appointment]})
