# Generated by Django 4.2 on 2024-01-23 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_version'),
        ('users', '0003_user_verification_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cars',
            field=models.ManyToManyField(blank=True, null=True, related_name='users', to='cars.car', verbose_name='Машины'),
        ),
    ]
