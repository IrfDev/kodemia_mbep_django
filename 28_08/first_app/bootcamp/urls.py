from django.urls import path

from .views import get_koder, list_koders

urlpatterns = [
    path("get_koder/<int:id>", get_koder),
    path("list_koders", list_koders),
]
