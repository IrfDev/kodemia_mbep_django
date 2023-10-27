from django.urls import path

from .views import (
    get_koder,
    list_koders,
    get_koder_type,
    get_ez_bootcamps,
    get_ez_unique_bootcamps,
    get_generation_koders_by_mentor,
    get_recent_koders,
)

urlpatterns = [
    path("get_koder/<int:id>", get_koder),
    path("list_koders", list_koders),
    path("user/<str:name>/<str:type>", get_koder_type),
    path("ejercicios/1", get_ez_bootcamps),
    path("ejercicios/2", get_ez_unique_bootcamps),
    path("ejercicios/3/<int:mentor_id>", get_generation_koders_by_mentor),
    path("ejercicios/3", get_generation_koders_by_mentor),
    path("ejercicios/4", get_recent_koders),
]
