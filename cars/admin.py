from django.contrib import admin

from cars.models import Car, Car_brand


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('car_brand', 'model', 'year', 'price')
    list_filter = ('car_brand', 'year')


@admin.register(Car_brand)
class CarBrandAdmin(admin.ModelAdmin):
    list_display = ('pk', 'car_brand')
