from django.core.management.base import BaseCommand
from cars.models import Car_brand


class Command(BaseCommand):
    help = 'Initialize car brands in the database'

    def handle(self, *args, **options):
        car_brands = ['Toyota', 'Ford', 'Chevrolet', 'Honda', 'Hyundai', 'Nissan', 'Volkswagen', 'Audi',
                      'Mercedes-Benz', 'BMW', 'Subaru', 'Mazda', 'Lexus', 'Jeep', 'Tesla', 'Volvo', 'Porsche', 'KIA']

        for brand in car_brands:
            Car_brand.objects.get_or_create(car_brand=brand)
            self.stdout.write(self.style.SUCCESS(f'Successfully created brand: {brand}'))
