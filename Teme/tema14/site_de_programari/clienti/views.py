from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Client


# Create your views here.
def index(request):
    return HttpResponse("Aici vor fi clientii!")


def clients(request):
    clients_list = Client.objects.all()
    return render(request, "clients.html", {"clients": clients_list})


def client_details(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    return render(request, "client_detail.html", {"client": client})
