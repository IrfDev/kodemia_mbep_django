from app.models.psycologist import Psychologist
from django.db.models import OrderBy


def get_all_psychologists(order_by: str = "created_at", is_list: bool = True):
    psychologists = Psychologist.objects.all().order_by(order_by)

    if is_list:
        return [x for x in psychologists]
    else:
        return psychologists


def get_psychologist_by_id(psychology_id: str):
    psychologist = Psychologist.objects.get(pk=psychology_id)

    if isinstance(psychologist, Psychologist):
        return psychologist
    else:
        raise ValueError(
            "We couldn't find that psychologist. Please try again with a different id"
        )
