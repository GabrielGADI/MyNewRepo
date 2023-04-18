from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Service


# Create your views here.
def index(request):
    return HttpResponse("Aici vor fi serviciile!")


def services(request):
    services_list = Service.objects.all()
    return render(request, "services.html", {"services": services_list})


def service_detaliu(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    return render(request, "service_detail.html", {"service": service})
