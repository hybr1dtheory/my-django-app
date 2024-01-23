from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world! This is the index of my very first app:)")


def return_energy_html(request):
    some_data = {"username": "some user",
                 "email": "xxx@gmail.com",
                 "name": "Panteleymon"
                 }
    return render(request, "energy_child.html", context={"some_data": some_data})
