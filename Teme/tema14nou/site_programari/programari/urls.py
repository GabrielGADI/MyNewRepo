from django.urls import path
from . import views

# urlpatterns = [
#     # path("", views.index, name="programari"),
#     path("<int:client_id>", views.client_details, name="client_details"),
#     path("client", views.client_add, name="add"),
#     path("", views.employees, name="all_employees"),
#     path("<int:employee_id>", views.employee_detail, name="employee_details"),
#     path("employee", views.employee_add, name="add"),
#     path("", views.services, name="all_services_"),
#     path("<int:service_id>", views.service_details, name="service_details"),
#     path("service", views.service_add, name="add"),
#     path("", views.appointments, name="all_appointments"),
#     path("<int:appointment_id>", views.appointment_details, name="appointment_details"),
#     path("appointment", views.appointment_add, name="add")
#
 # ]



urlpatterns = [
     path("", views.index, name="programari"),
     path("", views.ClientsView.as_view(), name="all_clients"),
     path("<int:pk>", views.ClientDetailView.as_view(), name="client_detail"),
     path("client", views.ClientCreateView.as_view(), name="add"),
     path("", views.AppointmentsView.as_view(), name="all_appointments"),
     path("<int:pk>", views.AppointmentDetailView.as_view(), name="appointment_detail"),
     path("appointment", views.AppointmentCreateView.as_view(), name="add"),
     path("", views.ServicesView.as_view(), name="all_services"),
     path("<int:pk>", views.ServiceDetailView.as_view(), name="service_detail"),
     path("pet", views.ServiceCreateView.as_view(), name="add"),
     path("", views.EmployeesView.as_view(), name="all_employees"),
     path("<int:pk>", views.EmployeeDetailView.as_view(), name="employee_detail"),
     path("pet", views.EmployeeCreateView.as_view(), name="add")
]

app_name = "programari"
