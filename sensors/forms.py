from django import forms
from .models import Sensor

class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ['name', 'sensor_type', 'pin', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Наприклад: DHT22'}),
            'sensor_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Наприклад: Температура'}),
            'pin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Наприклад: GPIO 4'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }