from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')

    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users_avatars/', verbose_name='Аватар', **NULLABLE)
    county = models.CharField(max_length=35, verbose_name='Страна', **NULLABLE)
    cars = models.ManyToManyField('cars.Car', verbose_name='Машины', related_name='users', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=100, blank=True)
