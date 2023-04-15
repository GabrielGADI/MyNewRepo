from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Pet


# Create your views here.

def index(request):
    return HttpResponse("Hello World")


def pets(request):
    pets_list = Pet.objects.all()  # returneaza toate obiectele de tip Pet
    return render(request, "all_pets.html", {"pets": pets_list})


def pet_details(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)  # pk=primary key - cheia dupa care sa ne caute
    return render(request, "pet_details.html", {"pet": pet}) # pet_details.html fisier creat in templates
