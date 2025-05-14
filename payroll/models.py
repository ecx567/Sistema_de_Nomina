from decimal import Decimal
from django.db import models
from employees.models import Empleado

class Rol(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    mes = models.CharField(max_length=20)
    anio = models.IntegerField()
    salario_base = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    horas_extra = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bono = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tot_ing = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    iess = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tot_des = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    neto = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        unique_together = ('empleado', 'mes', 'anio')  # Evitar duplicados

    def calcular_totales(self):
        # Calcular el total de ingresos
        self.tot_ing = self.salario_base + self.horas_extra + self.bono
        # Calcular el IESS (9.45% del salario base)
        self.iess = round(self.salario_base * Decimal('0.0945'), 2)
        # Calcular el total de deducciones
        self.tot_des = self.iess
        # Calcular el neto (total ingresos - total deducciones)
        self.neto = self.tot_ing - self.tot_des

    def save(self, *args, **kwargs):
        # Calcular los totales antes de guardar
        self.calcular_totales()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Rol de {self.empleado} para {self.mes}/{self.anio}'
