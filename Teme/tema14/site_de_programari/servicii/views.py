from django.http import HttpResponse
from django.shortcuts import render
from .models import Service


# Create your views here.
def index(request):
    return HttpResponse("Hello  World")


def servicii(request):
    servicii_list = Service.objects.all()
    return render(request, "servicii.html", {"servicii": servicii_list})
