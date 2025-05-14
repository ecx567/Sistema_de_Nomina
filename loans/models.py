from django.db import models

# Create your models here.
from django.db import models
from employees.models import Empleado
from decimal import Decimal  


class TipoPrestamo(models.Model):
    descripcion = models.CharField(max_length=100)
    tasa = models.IntegerField(default=0)  

    def __str__(self):
        return self.descripcion

class Prestamo(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    tipo_prestamo = models.ForeignKey(TipoPrestamo, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    interes = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    monto_pagar = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    numero_cuotas = models.PositiveIntegerField(default=1)
    cuota_mensual = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        tasa_decimal = Decimal(self.tipo_prestamo.tasa) / Decimal(100)
        self.interes = self.monto * tasa_decimal
        self.monto_pagar = self.monto + self.interes
        self.cuota_mensual = self.monto_pagar / self.numero_cuotas
        self.saldo = self.monto_pagar
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Préstamo de {self.empleado.nombre} - {self.tipo_prestamo.descripcion}"
