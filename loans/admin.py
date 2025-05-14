from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TipoPrestamo, Prestamo

@admin.register(TipoPrestamo)
class TipoPrestamoAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'tasa')
    search_fields = ('descripcion',)

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'tipo_prestamo', 'fecha_prestamo', 'monto', 'saldo')
    search_fields = ('empleado__nombre', 'tipo_prestamo__descripcion')
    list_filter = ('tipo_prestamo', 'fecha_prestamo')
