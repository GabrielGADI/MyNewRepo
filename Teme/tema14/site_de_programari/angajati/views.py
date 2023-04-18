from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee


# Create your views here.
def index(request):
    return HttpResponse("Aici vor fi angajatii!")


def angajati(request):
    angajati_list = Employee.objects.all()
    return render(request, "angajati.html", {"angajati": angajati_list})
