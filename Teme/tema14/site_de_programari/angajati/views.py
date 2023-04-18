from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Employee


# Create your views here.
def index(request):
    return HttpResponse("Aici vor fi angajatii!")


def employees(request):
    employees_list = Employee.objects.all()
    return render(request, "employees.html", {"employees": employees_list})


def employee_details(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, "employee_detail.html", {"employee": employee})
