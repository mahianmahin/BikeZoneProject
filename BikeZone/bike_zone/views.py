from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'bike_zone/index.html')

def about(request):
    return render(request, 'bike_zone/about.html')

def bike_details(request):
    return render(request, 'bike_zone/bike-details.html')

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
    return render(request, 'bike_zone/search.html')

def services(request):
    return render(request, 'bike_zone/services.html')