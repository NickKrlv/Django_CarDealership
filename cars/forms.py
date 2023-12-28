from django import forms
from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['car_brand', 'model', 'year', 'photo', 'price']
