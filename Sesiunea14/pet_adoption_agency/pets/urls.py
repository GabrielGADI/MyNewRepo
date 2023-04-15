from django.urls import path
from . import views # importam fisierul views

# definim lista pentru toate rutele care le accepta aplicatia noastra
urlpatterns = [
    path("", views.pets, name="all_pets"),  #prima pagina contine ruta, functia si numele rutei
    path("<int:pet_id>", views.pet_details, name="pet_details")
]
app_name = "pets" # ca aplicatia sa ruleze e necesar sa creeam obiect