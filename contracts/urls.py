from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_contratos, name='listar_contratos'),  # Cambiado
    path('nuevo/', views.crear_contrato, name='crear_contrato'),
    path('editar/<int:contrato_id>/', views.actualizar_contrato, name='actualizar_contrato'),
    path('eliminar/<int:contrato_id>/', views.eliminar_contrato, name='eliminar_contrato'),
    path('detalle/<int:contrato_id>/', views.detalle_contrato, name='detalle_contrato'),  # Agregado
]
