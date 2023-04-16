from django.urls import path
from . import views

urlpatterns = [
    path("", views.servicii, name="servicii"),
    path("<int:serviciu_id>", views.serviciu_detaliu, name="serviciu_detaliu")
]

app_name = "servicii"
