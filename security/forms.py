from django import forms
from .models import SecurityMeasure

class SecurityMeasureForm(forms.ModelForm):
    class Meta:
        model = SecurityMeasure
        fields = ['title', 'category', 'description', 'responsible', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'responsible': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }