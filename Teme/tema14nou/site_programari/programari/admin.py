from django.contrib import admin
from .models import Client, Appointment, Employee, Service

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Service)

