from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class HomeView(TemplateView):
    template_name = 'common/home.html'


#----UD8.3.a----
#Decorador de login_required - solo se puede acceder si el usuario está autenticado 
@method_decorator(login_required, name='dispatch')
class PanelView(TemplateView):
    template_name = 'common/panel.html'
