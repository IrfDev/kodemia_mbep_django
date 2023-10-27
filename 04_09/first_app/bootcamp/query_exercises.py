# Get one bootcamp filtered by koders whose last names contains "ez"

from bootcamp.models import Bootcamp, Generation, Koder, Mentor
from django.db.models import OrderBy


def get_bootcamp_by_koder_last_name(last_name, unique_values: bool = False):
    bootcamps = Bootcamp.objects.filter(
        generations__koders__last_name__endswith=last_name
    )

    if unique_values:
        bootcamps = bootcamps.distinct()

    return [x for x in bootcamps]


def get_mentor_koders_by_id(mentor_id: int):
    mentor_koders = Koder.objects.filter(
        generation__mentors__pk__exact=mentor_id
    ).values(
        "first_name",
        "last_name",
        "status",
        # We use the underscore mentors to get the associated mentors and
        # The associated fields
        "generation__mentors__first_name",
        "generation__mentors__last_name",
    )

    first_koder = mentor_koders[0]

    mentor = {
        "first_name": first_koder["generation__mentors__first_name"],
        "last_name": first_koder["generation__mentors__last_name"],
    }

    return [mentor_koders, mentor]


def get_koders_excluding_last_bootcamp():
    latest_bootcamp = Bootcamp.objects.order_by("created_at").first()
    koders = Koder.objects.exclude(generation__bootcamp__pk__exact=latest_bootcamp.pk)

    return koders
