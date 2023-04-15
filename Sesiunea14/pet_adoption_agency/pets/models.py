from django.db import models


# Create your models here.

class Pet(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=False)
    gender = models.CharField(max_length=1, choices=[("F", "Female"), ("M", "Male")])  # lista cu tupluri
    species = models.CharField(max_length=6, choices=[("dog", "Dog"), ("cat", "Cat"), ("rabbit", "Rabbit")])

    def __str__(self):
        return f"{self.name} - {self.age} - {self.gender} - {self.species}"
