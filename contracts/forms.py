from django import forms
from django.db.models import Q
from .models import Contrato

class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ['empleado', 'tipo_contrato', 'fecha_inicio', 'fecha_fin']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        empleado = cleaned_data.get('empleado')
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')

        if not all([empleado, fecha_inicio, fecha_fin]):
            return cleaned_data  # Si falta algún dato, no valida más

        # Filtrar contratos del mismo empleado, excluyendo el actual si se está editando
        contratos_existentes = Contrato.objects.filter(empleado=empleado)

        # Excluir el contrato actual si se está editando (esto ya está bien)
        if self.instance.pk:
            contratos_existentes = contratos_existentes.exclude(pk=self.instance.pk)

        # Verificar solapamiento de fechas de manera eficiente
        conflicto = contratos_existentes.filter(
            Q(fecha_inicio__lte=fecha_fin) & Q(fecha_fin__gte=fecha_inicio)
        ).exists()

        if conflicto:
            raise forms.ValidationError("Este empleado ya tiene un contrato establecido en el rango de fechas proporcionado.")

        return cleaned_data
