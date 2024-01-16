from django.contrib import admin

from blog.models import BlogPost
from cars.models import Car, Car_brand, Version


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('car_brand', 'model', 'year', 'price', 'vin_number')
    list_filter = ('car_brand', 'year')


@admin.register(Car_brand)
class CarBrandAdmin(admin.ModelAdmin):
    list_display = ('pk', 'car_brand')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('car_version', 'version_number', 'version_name', 'is_current')


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published')
