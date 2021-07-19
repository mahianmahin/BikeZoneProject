from django.contrib import admin
from django.urls import path, include
from bike_zone import views as main
from auth_app import views as authentication

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.home, name="home"),
    path('about/', main.about, name="about"),
    path('bike_details/', main.bike_details, name="bike_details"),
    path('bikes/', main.bikes, name="bikes"),
    path('contact/', main.contact, name="contact"),
    path('dashboard/', main.dashboard, name="dashboard"),
    path('search/', main.search, name="search"),
    path('services/', main.services, name="services"),
    path('login/', authentication.app_login, name="login"),
    path('logout/', authentication.app_logout, name="logout"),
    path('signup/', authentication.app_signup, name="signup"),

    # Social accounts login url
    path('socialaccounts/', include('allauth.urls'))
]
