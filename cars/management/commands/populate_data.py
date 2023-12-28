from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from cars.models import Car, Car_brand


class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        # Очистка данных
        self.stdout.write(self.style.SUCCESS('Clearing existing data...'))
        Car.objects.all().delete()
        Car_brand.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Populating database with sample data...'))

        car_brand = Car_brand.objects.create(car_brand='BMW')
        car = Car.objects.create(car_brand=car_brand, model='X5', year=2018, price=4000000)

        self.stdout.write(self.style.SUCCESS('Sample data populated successfully!'))
