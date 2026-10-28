from django import forms
from .models import AnalyticsReport

class AnalyticsFilterForm(forms.Form):
    date_from = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label="Від дати"
    )
    date_to = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label="До дати"
    )

class AnalyticsReportForm(forms.ModelForm):
    class Meta:
        model = AnalyticsReport
        fields = [
            'title', 
            'average_temperature', 
            'average_humidity', 
            'avg_soil_moisture', 
            'avg_light_level', 
            'plant_health_status', 
            'notes'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'average_temperature': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'average_humidity': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'avg_soil_moisture': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'avg_light_level': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'plant_health_status': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
