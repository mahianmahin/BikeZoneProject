# Generated by Django 3.2 on 2021-07-25 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_zone', '0015_bikes_bike_fuel_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikes',
            name='bike_compression_ratio',
            field=models.CharField(max_length=10, null=True),
        ),
    ]