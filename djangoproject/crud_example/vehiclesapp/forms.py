from django import forms
from .models import vehiculos

class VehicleForm (forms.ModelForm):
    
    class Meta:

        model = vehiculos

        fields = [
            "placa",
            "marca",
            "modelo",
            "color"
        ]

        labels = {
            'placa':'Numero de placa', 
            'marca' : 'Marcha del vehiculo',
            'modelo' : 'Modelo del vehiculo',
            'color' : 'Color del vehiculo'
        }

        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.Select(attrs={'class': 'form-control'})
        }

