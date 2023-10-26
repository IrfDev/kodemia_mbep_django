from django.db import models

# Create your models here.


class Koder(models.Model):
    """
    Koder Model
    """

    STATUS = [
        ("active", "Active"),
        ("inactive", "In-active"),
        ("finished", "Finished"),
    ]
    SIZES = [
        ("s", "Small"),
        ("m", "Medium"),
        ("l", "Large"),
    ]

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=350)
    generation = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=8, choices=STATUS, default="active")
    status = models.CharField(choices=SIZES, default="m", max_length=8)
    created_at = models.DateField(auto_now=True, auto_created=True)
    birthdate = models.DateField(blank=True, null=True)
    updated_at = models.DateField(
        auto_created=True,
    )

    def __str__(self):
        return f"first_name => {self.first_name} {self.last_name}"
