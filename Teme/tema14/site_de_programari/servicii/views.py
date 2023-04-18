from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Service


# Create your views here.
def index(request):
    return HttpResponse("Aici vor fi serviciile")


def servicii(request):
    servicii_list = Service.objects.all()
    return render(request, "servicii.html", {"servicii": servicii_list})

def serviciu_detaliu(request, service_id):
    service = get_object_or_404(Service, pk=service_id)  # pk=primary key - cheia dupa care sa ne caute
    return render(request, "serviciu_detaliu.html", {"serviciu": service})