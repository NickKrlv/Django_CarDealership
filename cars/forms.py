from django import forms
from cars.models import Car, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CarForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Car
        fields = ['car_brand', 'model', 'year', 'photo', 'price', 'vin_number']

    def clean(self):
        cleaned_data = super().clean()
        vin_number = cleaned_data.get('vin_number')
        model = cleaned_data.get('model')

        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        if model is not None and any(word in model.lower() for word in words):
            raise forms.ValidationError('Модель не должна содержать ключевые слова')

        if vin_number is not None and len(vin_number) != 17:
            raise forms.ValidationError('VIN номер должен содержать 17 символов')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = ['car_version', 'version_number', 'version_name', 'is_current']
