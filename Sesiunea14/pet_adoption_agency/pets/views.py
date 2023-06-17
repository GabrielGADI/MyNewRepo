from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Pet


# Create your views here.

# def index(request):
#     return HttpResponse("Hello World")
#
#
# def pets(request):
#     pets_list = Pet.objects.all()  # returneaza toate obiectele de tip Pet
#     return render(request, "all_pets.html", {"pets": pets_list})
#
#
# def pet_details(request, pet_id):
#     pet = get_object_or_404(Pet, pk=pet_id)  # pk=primary key - cheia dupa care sa ne caute
#     return render(request, "pet_details.html", {"pet": pet}) # pet_details.html fisier creat in templates
#
# def pet_add(request):
#     pet_details = request.POST.dict()
#     pet = Pet(name=pet_details["name"], age = pet_details["age"], gender = pet_details["gender"], species = pet_details["species"])
#     pet.save()
#     return HttpResponseRedirect(reverse("pets:all_pets"))

class PetsView(generic.ListView):
    template_name = "all_pets.html"
    context_object_name = "pets"

    def get_queryset(self):
        return Pet.objects.all()


class PetDetailView(generic.DetailView):
    template_name = "pet_details.html"
    model = Pet


class PetCreateView(generic.CreateView):
    model = Pet
    fields = ["name", "age", "gender", "species"]
    success_url = reverse_lazy("pets:all_pets")
