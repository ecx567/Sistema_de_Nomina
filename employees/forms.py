from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['cedula', 'nombre', 'apellido','sexo', 'cargo', 'departamento', 'tipo_contrato', 'fecha_ingreso', 'salario']
        labels = {
            'cedula': 'Cédula',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'sexo': 'Sexo',
            'cargo': 'Cargo',
            'departamento': 'Departamento',
            'tipo_contrato': 'Tipo de Contrato',
            'fecha_ingreso': 'Fecha de Ingreso',
            'salario': 'Salario',
        }
        widgets = {
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'salario': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.Select(attrs={'class': 'form-control'}),
            'departamento': forms.Select(attrs={'class': 'form-control'}),
            'tipo_contrato': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def clean_cedula(self):
        cedula = self.cleaned_data['cedula']
        # Excluir el empleado actual al validar la cédula
        if Empleado.objects.filter(cedula=cedula).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Ya existe un empleado con esta cédula.")
        return cedula
