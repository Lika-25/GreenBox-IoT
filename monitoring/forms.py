from django import forms
from .models import GreenhouseInfo

class GreenhouseInfoForm(forms.ModelForm):
    class Meta:
        model = GreenhouseInfo
        fields = '__all__'