from django.db import models

class TipoContrato(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Contrato(models.Model):
    # Usamos 'employees.Empleado' en lugar de importarlo directamente
    empleado = models.ForeignKey('employees.Empleado', on_delete=models.CASCADE)
    tipo_contrato = models.ForeignKey(TipoContrato, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.empleado} - {self.tipo_contrato}"
