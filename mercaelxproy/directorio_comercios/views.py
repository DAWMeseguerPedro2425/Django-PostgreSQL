from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from directorio_comercios.models import Categoria, Subcategoria, Asociacion, Comercio

#--------UD7.a--------
#Crear las vistas de la aplicación directorio_comercios 
# según la tabla 1 de aneño 2
class CategoriaListView(ListView): # ListView es una clase de Django que muestra una lista de objetos de un modelo
    model = Categoria
    template_name = 'directorio_comercios/categoria_list.html'

class CategoriaDetailView(DetailView): # DetailView es una clase de Django que muestra los detalles de un objeto de un modelo
    model = Categoria
    template_name = 'directorio_comercios/categoria_detail.html'

class SubCategoriaListView(ListView):
    model = Subcategoria
    template_name = 'directorio_comercios/subcategoria_list.html'

class SubCategoriaDetailView(DetailView):
    model = Subcategoria
    template_name = 'directorio_comercios/subcategoria_detail.html'

class AsociacionListView(ListView):
    model = Asociacion
    template_name = 'directorio_comercios/asociacion_list.html'

class AsociacionDetailView(DetailView):
    model = Asociacion
    template_name = 'directorio_comercios/asociacion_detail.html'

class ComercioListView(ListView):
    model = Comercio
    template_name = 'directorio_comercios/comercio_list.html'

class ComercioDetailView(DetailView):
    model = Comercio
    template_name = 'directorio_comercios/comercio_detail.html'