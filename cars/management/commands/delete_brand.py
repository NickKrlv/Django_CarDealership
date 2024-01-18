from django.core.management.base import BaseCommand
from cars.models import Car_brand


class Command(BaseCommand):
    help = 'Delete car brands in the database'

    def handle(self, *args, **options):

        brand_to_delete = Car_brand.objects.get(car_brand=...)

        brand_to_delete.delete()