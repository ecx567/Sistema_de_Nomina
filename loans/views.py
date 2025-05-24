from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Prestamo
from .forms import PrestamoForm
from django.core.paginator import Paginator


@login_required
def listar_prestamos(request):
    query = request.GET.get('q', '')
    prestamos_list = Prestamo.objects.all()

    if query:
        prestamos_list = prestamos_list.filter(
            Q(empleado__nombre__icontains=query) |
            Q(tipo_prestamo__descripcion__icontains=query)
        )

    paginator = Paginator(prestamos_list, 2)  
    page_number = request.GET.get('page')
    prestamos = paginator.get_page(page_number)

    return render(request, 'loans/prestamo_list.html', {
        'prestamos': prestamos,
        'query': query,
    })


@login_required
def crear_prestamo(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_prestamos')
    else:
        form = PrestamoForm()
    return render(request, 'loans/prestamo_form.html', {'form': form})

@login_required
def actualizar_prestamo(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    if request.method == 'POST':
        form = PrestamoForm(request.POST, instance=prestamo)
        if form.is_valid():
            form.save()
            return redirect('listar_prestamos')
    else:
        form = PrestamoForm(instance=prestamo)
    return render(request, 'loans/prestamo_form.html', {'form': form})

@login_required
def eliminar_prestamo(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    if request.method == 'POST':
        prestamo.delete()
        return redirect('listar_prestamos')
    return render(request, 'loans/prestamo_confirm_delete.html', {'prestamo': prestamo})

@login_required
def detalle_prestamo(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    return render(request, 'loans/prestamo_detail.html', {'prestamo': prestamo})
