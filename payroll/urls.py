from django.urls import path, include
from .views import (
    listar_roles_pago,
    crear_rol_pago,
    actualizar_rol_pago,
    confirmar_eliminar_rol_pago,
    detalle_rol_pago,
)

urlpatterns = [
    path('crear/', crear_rol_pago, name='crear_rol_pago'),
    path('', listar_roles_pago, name='listar_roles_pago'),
    path('editar/<int:pk>/', actualizar_rol_pago, name='actualizar_rol_pago'),
    path('eliminar/<int:pk>/', confirmar_eliminar_rol_pago, name='confirmar_eliminar_rol_pago'),
    path('detalle/<int:pk>/', detalle_rol_pago, name='detalle_rol_pago'),
]
