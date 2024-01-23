from django.shortcuts import render


def energy_main(request):
    mess = {"message": "Hello, world! This is the index of my very first app:)"}
    return render(request, "energy.html", context=mess)


def return_energy_meters(request):
    some_data = {"meter_name": "Substation #1",
                 "phases": 3,
                 "kt": 1200
                 }
    return render(request, "energy_meters.html", context={"some_data": some_data})
