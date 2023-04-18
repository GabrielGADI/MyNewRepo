from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="servicii"),
    path("<int:service_id>", views.service_detail, name="service_detail")
]

app_name = "servicii"
