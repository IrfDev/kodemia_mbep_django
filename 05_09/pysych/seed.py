from app.models import Appointment, Patient, Psychologist
from datetime import date

LOREM_STRING = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sed euismod nisi porta lorem mollis aliquam ut porttitor. Eget duis at tellus at urna condimentum mattis pellentesque id. Odio euismod lacinia at quis risus sed vulputate odio ut. Lectus urna duis convallis convallis tellus id. Orci ac auctor augue mauris augue neque gravida in fermentum. Diam volutpat commodo sed egestas egestas fringilla phasellus faucibus. Et egestas quis ipsum suspendisse. Et malesuada fames ac turpis egestas. Pretium viverra suspendisse potenti nullam ac. Lectus mauris ultrices eros in cursus. Amet consectetur adipiscing elit ut aliquam purus sit. Urna molestie at elementum eu. Ultricies mi eget mauris pharetra et ultrices neque ornare. Enim tortor at auctor urna. Consequat interdum varius sit amet mattis vulputate. Cras semper auctor neque vitae tempus quam pellentesque. Mi bibendum neque egestas congue quisque.
"""


# Psychologists
psy_1 = Psychologist.objects.create(
    first_name="Juancho",
    last_name="Perez",
    birthdate=date(1994, 10, 10),
    email="juancho@juancho.com",
)
psy_2 = Psychologist.objects.create(
    first_name="Luis",
    last_name="Lopez",
    birthdate=date(1994, 10, 10),
    email="luis@luis.com",
)
psy_3 = Psychologist.objects.create(
    first_name="Lizbeth",
    last_name="Rodriguez",
    birthdate=date(1994, 10, 10),
    email="lizbeth@lizbeth.com",
)


# Patients

pat_1 = Patient.objects.create(
    first_name="Marco",
    last_name="Marin",
    birthdate=date(1994, 10, 10),
    email="marco@marco.com",
    biography=LOREM_STRING,
    address="Av. Siempre viva 5050, Springfield",
)
pat_2 = Patient.objects.create(
    first_name="Alfredo",
    last_name="Martinez",
    birthdate=date(1994, 10, 10),
    email="alfredo@alfredo.com",
    biography=LOREM_STRING,
    address="Av. Siempre viva 5050, Springfield",
)
pat_3 = Patient.objects.create(
    first_name="Ricardo",
    last_name="Reynosa",
    birthdate=date(1994, 10, 10),
    email="ricardo@ricardo.com",
    biography=LOREM_STRING,
    address="Av. Siempre viva 5050, Springfield",
)


apt_1 = Appointment.objects.create(
    title="Initial appointment",
    date=date(2023, 11, 11),
    patient_id=pat_1,
    psychologist_id=psy_2,
)
apt_2 = Appointment.objects.create(
    title="Follow up appointment",
    date=date(2023, 1, 11),
    patient_id=pat_2,
    psychologist_id=psy_1,
)
apt_3 = Appointment.objects.create(
    title="Diagnostic appointment",
    date=date(2023, 5, 11),
    patient_id=pat_3,
    psychologist_id=psy_3,
)
