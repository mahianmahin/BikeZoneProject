from django.contrib import admin
from .models import SiteUtils, Bikes, Cart

@admin.register(SiteUtils)
class SiteUtilsAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(Bikes)
class BikesAdmin(admin.ModelAdmin):
    list_display = ('id', 'bike_name', 'bike_price', 'bike_is_featured', 'bike_is_latest')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'products')