from decimal import Decimal, ROUND_HALF_UP
from django import forms
from .models import Rol

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['empleado', 'mes', 'anio', 'salario_base', 'horas_extra', 'bono', 'tot_ing', 'iess', 'tot_des', 'neto']
        widgets = {
            'mes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mes'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Año'}),
            'salario_base': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salario Base'}),
            'horas_extra': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Horas Extra'}),
            'bono': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Bono'}),
            'tot_ing': forms.NumberInput(attrs={'class': 'form-control'}), 
            'iess': forms.NumberInput(attrs={'class': 'form-control'}),     
            'tot_des': forms.NumberInput(attrs={'class': 'form-control'}),  
            'neto': forms.NumberInput(attrs={'class': 'form-control'}),     
        }

    def clean(self):
        cleaned_data = super().clean()
        salario_base = cleaned_data.get('salario_base') or Decimal(0)
        horas_extra = cleaned_data.get('horas_extra') or Decimal(0)
        bono = cleaned_data.get('bono') or Decimal(0)

        # Calcular los valores
        total_ingresos = salario_base + horas_extra + bono
        iess = salario_base * Decimal('0.0945')  # 9.45% del salario base
        total_deducciones = iess
        neto = total_ingresos - total_deducciones

        # Redondear los valores a 2 decimales
        cleaned_data['tot_ing'] = total_ingresos.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        cleaned_data['iess'] = iess.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        cleaned_data['tot_des'] = total_deducciones.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        cleaned_data['neto'] = neto.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

        return cleaned_data
