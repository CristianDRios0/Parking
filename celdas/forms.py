import django.forms as forms
from .models import Celda

class CeldaForm(forms.ModelForm):
    class Meta:
        model = Celda
        fields = ['codigo', 'tipo', 'estado']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control fuente_textos', 'placeholder': 'Ingrese el codigo para la nueva celda'}),
            'tipo': forms.Select(attrs={'class': 'form-control fuente_textos', 'placeholder': 'Seleccione un tipo de celda'}),
            'estado': forms.Select(attrs={'class': 'form-control fuente_textos'})
        }