from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class SiteUtils(models.Model):
    about_text = RichTextField()

class Bikes(models.Model):
    bike_name = models.CharField(max_length = 40, null=True)
    bike_brand = models.CharField(max_length = 100, null=True)
    bike_model = models.CharField(max_length = 100, null=True)
    bike_location = models.CharField(max_length = 100, null=True)
    bike_year = models.IntegerField()
    bike_type = models.CharField(max_length = 100, null=True)
    bike_picture = models.ImageField(upload_to = 'product_bike_image')
    bike_price = models.IntegerField()
    bike_location = models.CharField(max_length = 100, null=True)
    bike_description = RichTextField()
    bike_engine_type = models.CharField(max_length = 100, null=True)
    bike_engine_displacement = models.IntegerField()
    bike_max_power = models.CharField(max_length = 50, null=True)
    bike_emission_type = models.CharField(max_length = 50, null=True)
    bike_max_torque = models.CharField(max_length = 50, null=True)
    bike_stroke = models.IntegerField()
    bike_no_of_cylinders = models.IntegerField()
    bike_valve_per_cylinder = models.IntegerField()
    bike_fuel_type = models.CharField(max_length = 10, null=True)
    bike_compression_ratio = models.CharField(max_length = 10, null=True)
    bike_ignition = models.CharField(max_length = 20, null=True)
    bike_is_featured = models.BooleanField(default=False)
    bike_is_latest = models.BooleanField(default=False)

class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Bikes, on_delete=models.CASCADE)

    
