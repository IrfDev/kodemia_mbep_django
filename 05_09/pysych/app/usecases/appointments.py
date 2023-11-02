from app.models.appointment import Appointment


def get_all_appointments(order_by: str = "created_at", is_list=True):
    appointments = (
        Appointment.objects.all()
        .values("patient_id__first_name", "id", "title", "psychologist_id__first_name")
        .order_by(order_by)
    )

    if is_list:
        return [x for x in appointments]
    else:
        return appointments


def get_appointment_by_id(psychology_id: str):
    appointment = Appointment.objects.values(
        "patient_id__first_name", "id", "pk", "title", "psychologist_id__first_name"
    ).get(id=psychology_id)

    return appointment
