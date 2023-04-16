from django.db import models

from angajati.models import Employee
from clienti.models import Client
from servicii.models import Service


# Create your models here.

class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.client} - {self.service} - {self.date}"
