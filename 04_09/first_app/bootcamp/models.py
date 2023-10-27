from django.db import models

# Create your models here.


class Bootcamp(models.Model):
    """
    Bootcamp Model
    """

    name = models.CharField(unique=True, max_length=100)
    created_at = models.DateField(auto_now=True, auto_created=True)
    updated_at = models.DateField(
        auto_created=True,
        auto_now_add=True,
    )


class Generation(models.Model):
    """
    Generation Model
    """

    number = models.IntegerField()
    created_at = models.DateField(auto_now=True, auto_created=True)
    updated_at = models.DateField(
        auto_created=True,
        auto_now_add=True,
    )
    bootcamp = models.ForeignKey(Bootcamp, models.PROTECT, related_name="generations")


# Koders: Pertenece a 1 generacion=> 1 generacion - n koder
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
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=8, choices=STATUS, default="active")
    size = models.CharField(choices=SIZES, default="m", max_length=8)
    birthdate = models.DateField(blank=True, null=True)
    created_at = models.DateField(auto_now=True, auto_created=True)
    updated_at = models.DateField(auto_created=True, auto_now_add=True)

    # Foreign key

    generation = models.ForeignKey(Generation, models.PROTECT, related_name="koders")

    def __str__(self):
        return f"first_name => {self.first_name} {self.last_name}"


# Mentores: Pertenece a varias generacion => n generacion - n mentor
class Mentor(models.Model):
    """
    Mentor Model
    """

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=350)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    created_at = models.DateField(auto_now=True, auto_created=True)
    updated_at = models.DateField(
        auto_created=True,
        auto_now_add=True,
    )

    generations = models.ManyToManyField(Generation, related_name="mentors")

    def __str__(self):
        return f"first_name => {self.first_name} {self.last_name}"
