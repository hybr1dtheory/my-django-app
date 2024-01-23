from django.urls import path
from . import views


urlpatterns = [
                path("", views.index, name="index"),
                path("child/", views.return_energy_html, name="child")
               ]
