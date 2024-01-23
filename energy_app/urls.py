from django.urls import path
from . import views


urlpatterns = [
                path("", views.energy_main, name="energy"),
                path("meters/", views.return_energy_meters, name="meters")
               ]
