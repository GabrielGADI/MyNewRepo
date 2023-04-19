from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="angajati"),
    path("", views.employees, name="employees")
]
