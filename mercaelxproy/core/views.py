from django.shortcuts import render
from django.views.generic import ListView, DetailView
from core.models import Provincia, Ciudad, Distrito


class ProvinciaListView(ListView):
    model = Provincia
    template_name = 'core/provincia_list.html'
    #----UD6.8.b----
    #pagina_by que sirve para paginar los resultados usando pagination.html
    paginate_by = 3
    

class ProvinciaDetailView(DetailView):
    model = Provincia
    template_name = 'core/provincia_detail.html'
    #----UD6.8.b----
    #pagina_by que sirve para paginar los resultados usando pagination.html
    paginate_by = 3


class CiudadListView(ListView):
    model = Ciudad
    template_name = 'core/ciudad_list.html'
    #----UD6.8.b----
    #pagina_by que sirve para paginar los resultados usando pagination.html
    paginate_by = 3


class CiudadDetailView(DetailView):
    model = Ciudad
    template_name = 'core/ciudad_detail.html'
    #----UD6.8.b----
    #pagina_by que sirve para paginar los resultados usando pagination.html
    paginate_by = 3


class DistritoListView(ListView):
    model = Distrito
    template_name = 'core/distrito_list.html'
    #----UD6.8.b----
    #pagina_by que sirve para paginar los resultados usando pagination.html
    paginate_by = 3


class DistritoDetailView(DetailView):
    model = Distrito
    template_name = 'core/distrito_detail.html'
    #----UD6.8.b----
    #pagina_by que sirve para paginar los resultados usando pagination.html
    paginate_by = 3
