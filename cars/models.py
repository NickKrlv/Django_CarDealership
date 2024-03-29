from django.db import models
from django.shortcuts import redirect, render

NULLABLE = {'null': True, 'blank': True}


class Car(models.Model):
    car_brand = models.ForeignKey('Car_brand', on_delete=models.CASCADE, verbose_name='Марка автомобиля')
    model = models.CharField(max_length=100, verbose_name='Модель автомобиля')
    year = models.IntegerField(verbose_name='Год выпуска')
    photo = models.ImageField(upload_to='cars/', **NULLABLE, verbose_name='Фото автомобиля')
    price = models.IntegerField(verbose_name='Цена автомобиля', **NULLABLE)

    vin_number = models.CharField(max_length=17, unique=True, verbose_name='Номер VIN', **NULLABLE)

    def __str__(self):
        return f'{self.car_brand} {self.model}'

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class Car_brand(models.Model):
    car_brand = models.CharField(max_length=100, verbose_name='Марка автомобиля')

    def __str__(self):
        return self.car_brand

    class Meta:
        verbose_name = 'Марка автомобиля'
        verbose_name_plural = 'Марки автомобилей'


class Version(models.Model):
    car_version = models.ForeignKey('Car', on_delete=models.CASCADE, verbose_name='Автомобиль')
    version_number = models.IntegerField(verbose_name='Номер версии')
    version_name = models.CharField(max_length=100, verbose_name='Название версии')
    is_current = models.BooleanField(default=False, verbose_name='Текущая версия')

    def __str__(self):
        return self.version_name

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'


