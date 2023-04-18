from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Appointment


# Create your views here.
def index(request):
    return HttpResponse("Aici vor fi programarile active")


def programari(request):
    programari_list = Appointment.objects.all()
    return render(request, "appointment.html", {"programari": programari_list})

def appointment_details(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    return render(request, "appointment_detail.html", {"appointment": appointment})

