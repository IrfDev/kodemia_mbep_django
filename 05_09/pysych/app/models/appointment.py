from django.db import models
from .patient import Patient
from .psycologist import Psychologist


class Appointment(models.Model):
    title = models.CharField(max_length=20)
    date = models.DateField()
    patient_id = models.ForeignKey(Patient, models.PROTECT, related_name="appointments")
    psychologist_id = models.ForeignKey(
        Psychologist, models.PROTECT, related_name="appointments"
    )
    created_at = models.DateField(auto_now_add=True, auto_created=True)
    updated_at = models.DateField(auto_now=True, auto_created=True)
