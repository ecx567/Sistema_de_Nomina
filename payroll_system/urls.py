from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from payroll_system.views import IndexView ,register  # Ajusta si la vista está en otra app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register, name='register'),
    path('index/', IndexView.as_view(), name='index'),
    path('employees/', include('employees.urls')),
    path('departments/', include('departments.urls')),
    path('contracts/', include('contracts.urls')),
    path('payroll/', include('payroll.urls')),
    path('loans/', include('loans.urls')),
]
