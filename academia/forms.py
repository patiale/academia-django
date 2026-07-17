from django import forms
from .models import RegistroPago

class RegistroPagoForm(forms.ModelForm):
    class Meta:
        model = RegistroPago
        fields = ['monto', 'referencia_transaccion']
        widgets = {
            'monto': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 25.00'}),
            'referencia_transaccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de referencia'}),
        }
        