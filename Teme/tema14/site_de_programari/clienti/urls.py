from django.urls import path
from .import views

urlpatterns = [
    path("", views.clienti, name="clienti")
]
