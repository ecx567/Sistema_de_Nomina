from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_empleados, name='listar_empleados'),
    path('nuevo/', views.crear_empleado, name='crear_empleado'),
    path('editar/<int:empleado_id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('eliminar/<int:empleado_id>/', views.eliminar_empleado, name='eliminar_empleado'),
    path('detalle/<int:empleado_id>/', views.detalle_empleado, name='detalle_empleado'),
]
