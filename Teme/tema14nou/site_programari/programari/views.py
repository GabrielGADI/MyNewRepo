from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Client, Employee, Service, Appointment


# Create your views here.
def index(request):
    return HttpResponse("Aici vom avea programarile!!!!!")


# def clients(request):
#     clients_list = Client.objects.all()
#     return render(request, 'all_clients.html', {'clients': clients_list})
#
#
# def client_details(request, client_id):
#     client = get_object_or_404(Client, pk=client_id)
#     return render(request, "client_detail.html", {"client": client})
#
#
# def client_add(request):
#     client_details = request.POST.dict()
#     client = Client(first_name=client_details["first_name"], last_name = client_details["last_name"], email = client_details["email"], phone = client_details["phone"], address = client_details["address"])
#     client.save()
#     return HttpResponseRedirect(reverse("clients:all_clients"))
#
#
# def employees(request):
#     employees_list = Employee.objects.all()
#     return render(request, 'all_employees.html', {'employees': employees_list})
#
#
# def employee_detail(request, employee_id):
#     employee = get_object_or_404(Employee, pk=employee_id)
#     return render(request, "employee_detail.html", {"employee": employee})
#
#
# def employee_add(request):
#     employee_detail = request.POST.dict()
#     employee = Employee(first_name=employee_detail["first_name"], last_name=employee_detail["last_name"], email=employee_detail["email"], phone=employee_detail["phone"], speciality=employee_detail["speciality"])
#     employee.save()
#     return HttpResponseRedirect(reverse("employees:all_employees"))
#
#
# def services(request):
#     services_list = Service.objects.all()
#     return render(request, 'all_services.html', {'services': services_list})
#
#
# def service_details(request, service_id):
#     service = get_object_or_404(Service, pk=service_id)
#     return render(request, "service_detail.html", {"service": service})
#
#
# def service_add(request):
#     service_details = request.POST.dict()
#     service = Service(name=service_details["name"], description=service_details["description"],price=service_details["price"])
#     service.save()
#     return HttpResponseRedirect(reverse("service:all_services"))
#
#
# def appointments(request):
#     appointments_list = Appointment.objects.all()
#     return render(request, 'all_appointment.html', {'appointments': appointments_list})
#
#
# def appointment_details(request, appointment_id):
#     appointment = get_object_or_404(Appointment, pk=appointment_id)
#     return render(request, "appointment_detail.html", {"appointment": appointment})
#
#
# def appointment_add(request):
#     appointment_details = request.POST.dict()
#     appointment = Appointment(client=appointment_details["client"], employee=appointment_details["last_name"],service=appointment_details["service"], date=appointment_details["date"])
#     appointment.save()
#     return HttpResponseRedirect(reverse("appointments:all_appointments"))


class AppointmentsView(generic.ListView):
    template_name = "all_appointments.html"
    context_object_name = "appointments"

    def get_queryset(self):
        return Appointment.objects.all()


class AppointmentDetailView(generic.DetailView):
    template_name = "appointment_detail.html"
    model = Appointment


class AppointmentCreateView(generic.CreateView):
    model = Appointment
    fields = ["client", "employee", "service", "date"]
    success_url = reverse_lazy("appointments:all_appointments")


class ClientsView(generic.ListView):
    template_name = "all_clients.html"
    context_object_name = "clients"

    def get_queryset(self):
        return Client.objects.all()


class ClientDetailView(generic.DetailView):
    template_name = "client_detail.html"
    model = Client


class ClientCreateView(generic.CreateView):
    model = Client
    fields = ["first_name", "last_name", "email", "phone", "address"]
    success_url = reverse_lazy("clients:all_clients")

class EmployeesView(generic.ListView):
    template_name = "all_employees.html"
    context_object_name = "employees"

    def get_queryset(self):
        return Employee.objects.all()


class EmployeeDetailView(generic.DetailView):
    template_name = "employee_detail.html"
    model = Employee


class EmployeeCreateView(generic.CreateView):
    model = Employee
    fields = ["first_name", "last_name", "email", "phone", "speciality"]
    success_url = reverse_lazy("employees:all_employees")

class ServicesView(generic.ListView):
    template_name = "all_services.html"
    context_object_name = "services"

    def get_queryset(self):
        return Service.objects.all()


class ServiceDetailView(generic.DetailView):
    template_name = "service_detail.html"
    model = Service


class ServiceCreateView(generic.CreateView):
    model = Service
    fields = ["name", "description", "price"]
    success_url = reverse_lazy("services:all_services")