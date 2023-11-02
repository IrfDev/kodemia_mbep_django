from django.db import models


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=27)
    biography = models.TextField(max_length=255)
    address = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True, auto_created=True)
    updated_at = models.DateField(auto_now=True, auto_created=True)
