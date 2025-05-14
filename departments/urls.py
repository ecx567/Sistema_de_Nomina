from django.urls import path
from .views import listar_departamentos, crear_departamento, actualizar_departamento, eliminar_departamento, detalle_departamento

urlpatterns = [
    path('', listar_departamentos, name='listar_departamentos'),
    path('nuevo/', crear_departamento, name='crear_departamento'),
    path('editar/<int:id>/', actualizar_departamento, name='actualizar_departamento'),
    path('eliminar/<int:id>/', eliminar_departamento, name='eliminar_departamento'),
    path('detalle/<int:id>/', detalle_departamento, name='detalle_departamento'),
]