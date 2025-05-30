from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Contrato
from .forms import ContratoForm
from employees.models import Empleado
from .models import Contrato, TipoContrato

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator

@login_required
def listar_contratos(request):
    query = request.GET.get('q', '')
    contratos = Contrato.objects.all()

    if query:
        contratos = contratos.filter(
            Q(empleado__nombre__icontains=query) |
            Q(empleado__apellido__icontains=query) |
            Q(tipo_contrato__nombre__icontains=query)
        )

    # Paginación
    paginator = Paginator(contratos, 2)  
    page_number = request.GET.get('page')
    contratos_paginated = paginator.get_page(page_number)

    return render(request, 'contracts/contract_list.html', {
        'contratos': contratos_paginated,
        'query': query
    })


@login_required
def crear_contrato(request):
    if request.method == 'POST':
        form = ContratoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_contratos')
    else:
        form = ContratoForm()

    empleados = Empleado.objects.all()
    tipos_contrato = TipoContrato.objects.all()

    return render(request, 'contracts/contract_form.html', {
        'form': form,
        'empleados': empleados,
        'tipos_contrato': tipos_contrato
    })

@login_required
def actualizar_contrato(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)
    if request.method == 'POST':
        form = ContratoForm(request.POST, instance=contrato)
        if form.is_valid():
            form.save()
            return redirect('listar_contratos')
    else:
        form = ContratoForm(instance=contrato)

    empleados = Empleado.objects.all()
    tipos_contrato = TipoContrato.objects.all()

    return render(request, 'contracts/contract_form.html', {
        'form': form,
        'empleados': empleados,
        'tipos_contrato': tipos_contrato,
        'contract': contrato
    })

@login_required
def eliminar_contrato(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)
    if request.method == 'POST':
        contrato.delete()
        return redirect('listar_contratos')
    return render(request, 'contracts/contract_confirm_delete.html', {'contrato': contrato})

@login_required
def detalle_contrato(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)
    return render(request, 'contracts/contract_detail.html', {'contrato': contrato})
