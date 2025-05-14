from django import forms
from .models import Prestamo

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['empleado', 'tipo_prestamo', 'fecha_prestamo', 'monto', 'numero_cuotas']
        labels = {
            'empleado': 'Empleado',
            'tipo_prestamo': 'Tipo de Préstamo',
            'fecha_prestamo': 'Fecha del Préstamo',
            'monto': 'Monto',
            'numero_cuotas': 'Número de Cuotas',
        }
        widgets = {
            'fecha_prestamo': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control'}),
            'numero_cuotas': forms.NumberInput(attrs={'class': 'form-control'}),
        }
