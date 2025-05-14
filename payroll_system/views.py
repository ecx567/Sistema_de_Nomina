from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect

@method_decorator([login_required, never_cache], name='dispatch')
class IndexView(TemplateView):
    template_name = 'index.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario registrado exitosamente. Ahora puedes iniciar sesión.")
            return redirect('login')  # Redirigir al login después del registro
        else:
            messages.error(request, "Hubo un error al registrar el usuario. Revisa los datos ingresados.")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
