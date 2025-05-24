from django.shortcuts import render, redirect, get_object_or_404
from .models import Departamento
from .forms import DepartamentoForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required
def listar_departamentos(request):
    query = request.GET.get('q', '')
    departamentos_list = Departamento.objects.all()
    if query:
        departamentos_list = departamentos_list.filter(nombre__icontains=query)
    paginator = Paginator(departamentos_list, 2)  # 10 por página
    page_number = request.GET.get('page')
    departamentos = paginator.get_page(page_number)
    return render(request, 'departments/department_list.html', {
        'departamentos': departamentos,
        'query': query,
    })

@login_required
def detalle_departamento(request, id):
    departamento = get_object_or_404(Departamento, id=id)
    return render(request, 'departments/department_detail.html', {'departamento': departamento})

@login_required
def crear_departamento(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_departamentos')
    else:
        form = DepartamentoForm()
    return render(request, 'departments/department_form.html', {'form': form})

@login_required
def actualizar_departamento(request, id):
    departamento = get_object_or_404(Departamento, id=id)
    if request.method == 'POST':
        form = DepartamentoForm(request.POST, instance=departamento)
        if form.is_valid():
            form.save()
            return redirect('listar_departamentos')
    else:
        form = DepartamentoForm(instance=departamento)
    return render(request, 'departments/department_form.html', {'form': form})

@login_required
def eliminar_departamento(request, id):
    departamento = get_object_or_404(Departamento, id=id)
    if request.method == 'POST':
        departamento.delete()
        return redirect('listar_departamentos')
    return render(request, 'departments/department_confirm_delete.html', {'departamento': departamento})
