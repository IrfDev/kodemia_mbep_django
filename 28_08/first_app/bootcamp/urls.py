from django.urls import path

from .views import get_koder, list_koders, get_koder_type

urlpatterns = [
    path("get_koder/<int:id>", get_koder),
    path("list_koders", list_koders),
    path("user/<str:name>/<str:type>", get_koder_type),
]
