from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
from .models import SiteUtils, Bikes, Cart
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.mail import EmailMessage
from django.conf import settings
from django.db.models import Q
from django.urls import reverse

# for payment

from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
import socket
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def checkout(request):
    mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id='bikez611019424042b', sslc_store_pass='bikez611019424042b@ssl')

    status_url = request.build_absolute_uri(reverse('complete'))
    
    mypayment.set_urls(success_url=status_url, fail_url=status_url, cancel_url=status_url, ipn_url=status_url)
    mypayment.set_product_integration(total_amount=Decimal('20.20'), currency='BDT', product_category='Bike', product_name='demo-product', num_of_item=1, shipping_method='YES', product_profile='None')

    mypayment.set_customer_info(name='John Doe', email='johndoe@email.com', address1='demo address', address2='demo address 2', city='Dhaka', postcode='1207', country='Bangladesh', phone='01711111111')
    mypayment.set_shipping_info(shipping_to='demo customer', address='demo address', city='Dhaka', postcode='1209', country='Bangladesh')

    response_data = mypayment.init_payment()

    return redirect(response_data['GatewayPageURL'])

def complete(request):
    return render(request, 'bike_zone/checkout.html')

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

    if request.method == "GET":
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
    bikes = Bikes.objects.all()
    
    paginator = Paginator(bikes, 6)
    page = request.GET.get('page')
    paged_bikes = paginator.get_page(page)
    
    data = {
        'bikes': paged_bikes
    }
    return render(request, 'bike_zone/bikes.html', data)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        message_body = "Name: " + name + "\n" + "Phone: " + phone + "\n" + "E-mail: " + email + "\n\n" + message

        mail = EmailMessage(
            subject,
            message_body,
            settings.EMAIL_HOST_USER,
            ['mahianmahin@yahoo.com']
        )

        mail.send()

        messages.success(request, 'Mail sent successfully. We will contact you shortly')
        return redirect('/contact/')

    return render(request, 'bike_zone/contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user_id = request.user)

        data = {
            'cart': cart
        }

        return render(request, 'bike_zone/dashboard.html', data)

    else:
        messages.warning(request, 'Login first to enter to the dashboard')
        return redirect('/login/')

def add_to_cart(request, id):
    cart_ins = Cart(
        user_id = request.user,
        products = Bikes.objects.get(pk=id)
    )

    cart_ins.save()
    messages.success(request, 'Bike added to cart successfully!')

    return redirect('/dashboard/')

def delete_cart_item(request, id):
    cart_ins = Cart.objects.filter( Q(user_id = request.user) & Q(products = Bikes.objects.get(pk=id)) )
    cart_ins.delete()

    messages.success(request, 'Item removed from your cart successfully!')
    return redirect('/dashboard/')

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

    if request.method == "GET":
        data = {
        'bikes': bikes,
        'brand': brand,
        'model': model,
        'location': location,
        'year': year,
        'type': type_of_bike
    }

    if request.method == "POST":
        search_brand = request.POST.get('brand')
        search_model = request.POST.get('model')
        search_location = request.POST.get('location')
        search_year = request.POST.get('year')
        search_type = request.POST.get('type')
        search_min_price = request.POST.get('price-min')
        search_max_price = request.POST.get('price-max')

        searched_bikes = Bikes.objects.filter(
            Q(bike_brand = search_brand) |
            Q(bike_model = search_model) |
            Q(bike_location = search_location) |
            Q(bike_year = search_year) |
            Q(bike_type = search_type) |
            Q(bike_price__gte = search_min_price) &
            Q(bike_price__lte = search_max_price)
        )

        data = {
            'searched_bikes': searched_bikes,
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


