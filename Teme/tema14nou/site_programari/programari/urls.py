from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="programari"),
    path("", views.clients, name="all_clients"),
    path("", views.employees, name="all_employees"),
    path("", views.services, name="all_services"),
    path("", views.appointments, name="all_appointments"),
    path("<int:client_id>", views.client_details, name="client_details"),
    path("<int:employee_id>", views.employee_detail, name="employee_details"),
    path("<int:service_id>", views.service_details, name="service_details"),
    path("<int:appointment_id>", views.appointment_details, name="appointment_details")

]
app_name = "programari"
