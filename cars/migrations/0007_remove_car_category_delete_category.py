# Generated by Django 5.0 on 2023-12-28 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_alter_car_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]