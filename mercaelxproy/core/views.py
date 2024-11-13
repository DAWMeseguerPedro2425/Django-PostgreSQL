from django.shortcuts import render
from django.views.generic import ListView, DetailView
from core.models import Provincia, Ciudad, Distrito


class ProvinciaListView(ListView):
    model = Provincia
    template_name = 'core/provincia_list.html'
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['verbose_name_plural'] = self.model._meta.verbose_name_plural
        return context
    

class ProvinciaDetailView(DetailView):
    model = Provincia
    template_name = 'core/provincia_detail.html'


class CiudadListView(ListView):
    model = Ciudad
    template_name = 'core/ciudad_list.html'


class CiudadDetailView(DetailView):
    model = Ciudad
    template_name = 'core/ciudad_detail.html'


class DistritoListView(ListView):
    model = Distrito
    template_name = 'core/distrito_list.html'


class DistritoDetailView(DetailView):
    model = Distrito
    template_name = 'core/distrito_detail.html'
