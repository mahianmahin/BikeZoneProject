from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
from .models import SiteUtils, Bikes

# Create your views here.

def home(request):
    bikes = Bikes.objects.all()
    
    brand = []
    model = []
    location = []
    year = []
    type_of_bike = []

    for item in bikes:
        if item.bike_brand in brand:
            continue
        else:
            brand.append(item.bike_brand)

        if item.bike_model in model:
            continue
        else:
            model.append(item.bike_model)

        if item.bike_location in location:
            continue
        else:
            location.append(item.bike_location)

        if item.bike_year in year:
            continue
        else:
            year.append(item.bike_year)

        if item.bike_type in type_of_bike:
            continue
        else:
            type_of_bike.append(item.bike_type)

    data = {
        'bikes': bikes,
        'brand': brand,
        'model': model,
        'location': location,
        'year': year,
        'type': type_of_bike
    }

    # print("\n=======\n", year, "\n=======\n")
    # print("\n=======\n", type_of_bike, "\n=======\n")

    return render(request, 'bike_zone/index.html', data)

def about(request):
    site_utils = SiteUtils.objects.all()
    
    data = {
        'site_utils' : site_utils,
    }

    return render(request, 'bike_zone/about.html', data)

def bike_details(request, id):
    bikes = Bikes.objects.get(pk=id)
    data = {
        'bikes' : bikes
    }
    return render(request, 'bike_zone/bike-details.html', data)

def bikes(request):
    return render(request, 'bike_zone/bikes.html')

def contact(request):
    return render(request, 'bike_zone/contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'bike_zone/dashboard.html')

    else:
        messages.warning(request, 'Login first to enter to the dashboard')
        return redirect('/login/')

def search(request):
    bikes = Bikes.objects.all()
    
    brand = []
    model = []
    location = []
    year = []
    type_of_bike = []

    for item in bikes:
        if item.bike_brand in brand:
            continue
        else:
            brand.append(item.bike_brand)

        if item.bike_model in model:
            continue
        else:
            model.append(item.bike_model)

        if item.bike_location in location:
            continue
        else:
            location.append(item.bike_location)

        if item.bike_year in year:
            continue
        else:
            year.append(item.bike_year)

        if item.bike_type in type_of_bike:
            continue
        else:
            type_of_bike.append(item.bike_type)

    data = {
        'bikes': bikes,
        'brand': brand,
        'model': model,
        'location': location,
        'year': year,
        'type': type_of_bike
    }

    return render(request, 'bike_zone/search.html', data)

def services(request):
    return render(request, 'bike_zone/services.html')