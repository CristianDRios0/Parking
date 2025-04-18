from django import forms
from .models import Vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['placa', 'cliente']
        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la placa'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
        }