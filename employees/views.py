from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Empleado
from .forms import EmpleadoForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q  # Solo si vas a usar búsqueda


@login_required
def listar_empleados(request):
    query = request.GET.get('q', '')  # Captura el término de búsqueda si existe
    sexo = request.GET.get('sexo', '')
    empleados_list = Empleado.objects.all().select_related('departamento')

    if query:
        empleados_list = empleados_list.filter(
            Q(nombre__icontains=query) |
            Q(apellido__icontains=query) |
            Q(cedula__icontains=query)
        )
    if sexo in ['M', 'F']:
        empleados_list = empleados_list.filter(sexo=sexo)

    paginator = Paginator(empleados_list, 2)  
    page_number = request.GET.get('page')
    empleados = paginator.get_page(page_number)

    return render(request, 'employees/employee_list.html', {
        'empleados': empleados,
        'query': query,
        'sexo': sexo,
    })


@login_required
def detalle_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    return render(request, 'employees/employee_detail.html', {'empleado': empleado})

@login_required
def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'employees/employee_form.html', {'form': form})

@login_required
def actualizar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('listar_empleados')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'employees/employee_form.html', {'form': form})

@login_required
def eliminar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('listar_empleados')
    return render(request, 'employees/employee_confirm_delete.html', {'empleado': empleado})
