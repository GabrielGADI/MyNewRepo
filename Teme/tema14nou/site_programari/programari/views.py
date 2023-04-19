from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Client, Employee, Service, Appointment


# Create your views here.
def index(request):
    return HttpResponse("Aici vom avea programarile!")


def clients(request):
    clients_list = Client.objects.all()
    return render(request, 'all_clients.html', {'clients': clients_list})


def client_details(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    return render(request, "client_detail.html", {"client": client})


def employees(request):
    employees_list = Employee.objects.all()
    return render(request, 'all_employees.html', {'employees': employees_list})


def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, "employee_detail.html", {"employee": employee})


def services(request):
    services_list = Service.objects.all()
    return render(request, 'all_services.html', {'services': services_list})


def service_details(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    return render(request, "service_detail.html", {"service": service})


def appointments(request):
    appointments_list = Appointment.objects.all()
    return render(request, 'all_appointment.html', {'appointments': appointments_list})


def appointment_details(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    return render(request, "appointment_detail.html", {"appointment": appointment})
