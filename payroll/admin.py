from django.contrib import admin
from .models import Rol

class RolAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'mes', 'anio', 'salario_base', 'get_deducciones', 'get_total_a_pagar')  # Actualizado
    search_fields = ('empleado__nombre', 'mes', 'anio')
    list_filter = ('mes', 'anio')

    def get_deducciones(self, obj):
        return obj.iess  # Usa el campo `iess` del modelo
    get_deducciones.short_description = 'Deducciones'

    def get_total_a_pagar(self, obj):
        return obj.neto  # Usa el campo `neto` del modelo
    get_total_a_pagar.short_description = 'Total a Pagar'

admin.site.register(Rol, RolAdmin)
