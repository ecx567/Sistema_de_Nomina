from django.urls import path
from . import views


urlpatterns = [
    path('', views.listar_prestamos, name='listar_prestamos'),
    path('nuevo/', views.crear_prestamo, name='crear_prestamo'),
    path('editar/<int:pk>/', views.actualizar_prestamo, name='actualizar_prestamo'),
    path('eliminar/<int:pk>/', views.eliminar_prestamo, name='eliminar_prestamo'),
    path('detalle/<int:pk>/', views.detalle_prestamo, name='detalle_prestamo'), 
]
