from django import forms
from .models import Parqueo, Vehiculo

class ParqueoForm(forms.ModelForm):
    class Meta:
        model = Parqueo
        fields = ['vehiculo', 'tarifa']
        widgets = {
            'vehiculo': forms.Select(attrs={'class': 'form-control'}),
            'tarifa': forms.Select(attrs={'class': 'form-control'}),
        }