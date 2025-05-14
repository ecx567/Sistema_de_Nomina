from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Rol
from .forms import RolForm
from employees.models import Empleado
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def listar_roles_pago(request):
    query = request.GET.get('q', '')
    roles = Rol.objects.all()

    if query:
        roles = roles.filter(
            Q(empleado__nombre__icontains=query) |
            Q(empleado__apellido__icontains=query) |
            Q(mes__icontains=query) |
            Q(anio__icontains=query)
        )

    # Paginación
    paginator = Paginator(roles, 10)  # Mostrar 10 roles por página
    page_number = request.GET.get('page')
    roles_paginated = paginator.get_page(page_number)

    return render(request, 'payroll/payroll_list.html', {
        'roles': roles_paginated,
        'query': query
    })

@login_required
def crear_rol_pago(request):
    if request.method == 'POST':
        form = RolForm(request.POST)
        if form.is_valid():
            rol = form.save(commit=False)  # No guardar aún
            rol.calcular_totales()        # Calcular los valores en el modelo
            rol.save()                    # Guardar con los valores calculados
            messages.success(request, "Rol de pago creado correctamente.")
            return redirect('listar_roles_pago')
        else:
            messages.error(request, "Hubo un error al crear el rol de pago. Revisa los datos ingresados.")
    else:
        form = RolForm()

    return render(request, 'payroll/payroll_form.html', {'form': form})


@login_required
def actualizar_rol_pago(request, pk):
    rol = get_object_or_404(Rol, pk=pk)
    if request.method == 'POST':
        form = RolForm(request.POST, instance=rol)
        if form.is_valid():
            form.save()  # Los cálculos se realizan automáticamente en el método save
            return redirect('listar_roles_pago')
    else:
        form = RolForm(instance=rol)
    empleados = Empleado.objects.all()
    return render(request, 'payroll/payroll_form.html', {
        'form': form,
        'empleados': empleados,
        'payroll': rol  # para saber que es "actualizar"
    })

@login_required
def confirmar_eliminar_rol_pago(request, pk):
    rol = get_object_or_404(Rol, pk=pk)
    if request.method == 'POST':
        rol.delete()
        return redirect('listar_roles_pago')
    return render(request, 'payroll/payroll_confirm_delete.html', {'rol': rol})

@login_required
def detalle_rol_pago(request, pk):
    rol = get_object_or_404(Rol, pk=pk)
    return render(request, 'payroll/payroll_detail.html', {'rol': rol})
