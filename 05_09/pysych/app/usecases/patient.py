from app.models.patient import Patient
from django.db.models import OrderBy


def get_all_patients(order_by: str = "created_at", is_list=True):
    patients = Patient.objects.all().order_by(order_by)

    if is_list:
        return [x for x in patients]
    else:
        return patients


def get_patient_by_id(psychology_id: str):
    patient = Patient.objects.get(pk=psychology_id)

    if isinstance(patient, Patient):
        return patient
    else:
        raise ValueError(
            "We couldn't find that Patient. Please try again with a different id"
        )
