from django.http import HttpResponse
from django.shortcuts import render
from .models import Appointment


# Create your views here.
def index(request):
    return HttpResponse("Aici vor fi programarile active")


def programari(request):
    programari_list = Appointment.objects.all()
    return render(request, "programari.html", {"programari": programari_list})
