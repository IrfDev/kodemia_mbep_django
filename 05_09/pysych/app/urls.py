from django.urls import path

from app.views import (
    list_psychologists,
    get_psychologist,
    list_appointments,
    list_patients,
    get_patient,
    get_appointment,
)

urlpatterns = [
    path("psychologists/<int:id>", get_psychologist),
    path("psychologists/", list_psychologists),
    path("patients/<int:id>", get_patient),
    path("patients/", list_patients),
    path("appointments/<int:id>", get_appointment),
    path("appointments/", list_appointments),
]
