from django.urls import path

from .views import welcome, greetings_with_name, greetings_koder

urlpatterns = [
    path("welcome/", welcome),
    path("greetings/<str:name>", greetings_with_name),
    path("greetings-kodemia/<str:type>", greetings_koder),
]
