from django.shortcuts import render
from django.http import HttpResponse
from .models import Client


# Create your views here.
def index(request):
    return HttpResponse("Hello  World")


def clienti(request):
    clienti_list = Client.objects.all()
    return render(request, "clienti.html", {"clienti": clienti_list})
