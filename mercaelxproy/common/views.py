from django.shortcuts import render
from django.views.generic import TemplateView
from common.mixins import LoginRequiredMixin

# Create your views here.
class HomeView(TemplateView):
    template_name = 'common/home.html'


#----UD8.3----
#Vista de panel para acceder a las vistas de las aplicaciones con login_required
class PanelView(LoginRequiredMixin, TemplateView):
    template_name = 'common/panel.html'
