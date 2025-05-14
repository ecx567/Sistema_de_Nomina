from django.db import models
from departments.models import Departamento 
from contracts.models import TipoContrato
from django.apps import apps

class Cargo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Empleado(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    cedula = models.CharField(max_length=10, unique=True, null=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default='M')  # Campo agregado
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    tipo_contrato = models.ForeignKey(TipoContrato, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def get_tipo_contrato(self):
        try:
            TipoContrato = apps.get_model('contracts', 'TipoContrato')
            return TipoContrato.objects.get(id=self.tipo_contrato_id)
        except TipoContrato.DoesNotExist:
            return None  # Retornar None si el contrato no se encuentra
