from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import CustomAuthenticationForm

from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import TemplateView

# Clase para el inicio de sesión
class CustomLoginView(SuccessMessageMixin, LoginView):
    template_name = 'common/login.html'  # Asegúrate de que esta plantilla exista
    authentication_form = CustomAuthenticationForm  # Usa tu formulario personalizado
    success_message = 'Has iniciado sesión correctamente.'

# Clase para el cierre de sesión
class CustomLogoutView(LogoutView):
    
    success_message = 'Has cerrado sesión correctamente.'

    def dispatch(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().dispatch(request, *args, **kwargs)
