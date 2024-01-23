from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("energy/", include("energy_app.urls")),
    path('admin/', admin.site.urls),
]
