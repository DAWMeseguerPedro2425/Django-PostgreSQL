from django.shortcuts import render
from django.views.generic import ListView, DetailView
from directorio_comercios.models import Categoria, Subcategoria, Asociacion, Comercio
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from common.mixins import CreateUpdateMixin, DeleteMixin, OrderedListMixin
from .forms import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

#--------UD6.7.a--------
#Crear las vistas de la aplicación directorio_comercios para mostrar las categorías, subcategorías, asociaciones y comercios
# según la tabla 1 de anexo 2
#----UD7.2.g----
#Llamada a la clase de OrderedListMixin para ordering por query de la list
#----UD8.3.a----
#Decorador de login_required - solo se puede acceder si el usuario está autenticado
@method_decorator(login_required, name='dispatch')
class CategoriaListView(OrderedListMixin, ListView): # ListView es una clase de Django que muestra una lista de objetos de un modelo
    model = Categoria
    template_name = 'directorio_comercios/categoria_list.html'
    #----UD6.8.b----
    #pagina_by que sirve para paginar los resultados usando pagination.html
    paginate_by = 3

#----UD8.3.a----
#Decorador de login_required - solo se puede acceder si el usuario está autenticado
@method_decorator(login_required, name='dispatch')
class CategoriaDetailView(DetailView): # DetailView es una clase de Django que muestra los detalles de un objeto de un modelo
    model = Categoria
    template_name = 'directorio_comercios/categoria_detail.html'
    #----UD6.8.b----
    #pagina_by que sirve para paginar los resultados usando pagination.html
    paginate_by = 3

#----UD7.2.a----
#Vista de crear, actualizar y eliminar una categoría
#----UD8.3.a----
#Decorador de login_required - solo se puede acceder si el usuario está autenticado
@method_decorator(login_required, name='dispatch')
class CategoriaCreateView(CreateUpdateMixin, CreateView):
    model = Categoria
    #template_name = 'common/base_create_udpate.html'
    #fields = '__all__'
    success_url = 'categoria_update'
    #----UD7.3.a-----
    # implementacion de form
    form_class = CategoriaForm
    #----UD7.4.a----
    # Mensaje de creacion
    success_message = 'Categoría creada con éxito.'

#----UD8.3.a----
#Decorador de login_required - solo se puede acceder si el usuario está autenticado
@method_decorator(login_required, name='dispatch')
class CategoriaUpdateView(CreateUpdateMixin, UpdateView):
    model = Categoria
    #template_name = 'common/base_create_udpate.html'
    #fields = '__all__'
    success_url = 'categoria_update'
    url_borrado = 'categoria_delete'
    #----UD7.3.a-----
    # implementacion de form
    form_class = CategoriaForm
    #----UD7.4.a----
    # Mensaje de actualización
    success_message = 'Categoría actualizada con éxito.'

#--UD7.2.b----
#Vista de eliminar una categoría
#----UD8.3.a----
#Decorador de login_required - solo se puede acceder si el usuario está autenticado
@method_decorator(login_required, name='dispatch')
class CategoriaDeleteView(DeleteMixin, DeleteView):
    model = Categoria
    #template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('categoria_list')
    success_message = "Categoría eliminada correctamente"
    error_message = "No se puede eliminar la categoría porque tiene subcategorías asociadas"
    mensaje_confirmacion = "¿Está seguro de que desea eliminar esta categoría?"

#----UD7.2.g----
#Llamada a la clase de OrderedListMixin para ordering por query de la list
@method_decorator(login_required, name='dispatch')
class SubCategoriaListView(OrderedListMixin, ListView):
    model = Subcategoria
    template_name = 'directorio_comercios/subcategoria_list.html'
    #----UD6.8.b----
    #pagina_by que sirve para paginar los resultados usando pagination.html
    paginate_by = 3

#----UD8.3.a----
#Decorador de login_required - solo se puede acceder si el usuario está autenticado
@method_decorator(login_required, name='dispatch')
class SubCategoriaDetailView(DetailView):
    model = Subcategoria
    template_name = 'directorio_comercios/subcategoria_detail.html'
    #----UD6.8.b----
    #pagina_by que sirve para paginar los resultados usando pagination.html
    paginate_by = 3

#----UD7.2.a----
#Vista de crear, actualizar y eliminar una subcategoría
#----UD8.3.a----
#Decorador de login_required - solo se puede acceder si el usuario está autenticado
@method_decorator(login_required, name='dispatch')
class SubcategoriaCreateView(CreateUpdateMixin, CreateView):
    model = Subcategoria
    #template_name = 'common/base_create_udpate.html'
    #fields = '__all__'
    success_url = 'subcategoria_update'
    #----UD7.3.a-----
    # implementacion de form
    form_class = SubcategoriaForm
    #----UD7.4.a----
    # Mensaje de creacion
    success_message = 'Subcategoría creada con éxito.'

#----UD8.3.a----
#Decorador de login_required - solo se puede acceder si el usuario está autenticado
@method_decorator(login_required, name='dispatch')
class SubcategoriaUpdateView(CreateUpdateMixin, UpdateView):
    model = Subcategoria
    #template_name = 'common/base_create_udpate.html'
    #fields = '__all__'
    success_url = 'subcategoria_update'
    url_borrado = 'subcategoria_delete'
    #----UD7.3.a-----
    # implementacion de form
    form_class = SubcategoriaForm
    #----UD7.4.a----
    # Mensaje de actualización
    success_message = 'Subcategoría actualizada con éxito.'

#--UD7.2.b----
#Vista de eliminar una subcategoría
#----UD8.3.a----
#Decorador de login_required - solo se puede acceder si el usuario está autenticado
@method_decorator(login_required, name='dispatch')
class SubcategoriaDeleteView(DeleteMixin, DeleteView):
    model = Subcategoria
    #template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('subcategoria_list')
    success_message = "La subcategoría ha sido eliminada con éxito."
    mensaje_confirmacion = "¿Está seguro que quiere eliminar esta Subcategoría?"

#----UD7.2.g----
#Llamada a la clase de OrderedListMixin para ordering por query de la list
@method_decorator(login_required, name='dispatch')
class AsociacionListView(OrderedListMixin, ListView):
    model = Asociacion
    template_name = 'directorio_comercios/asociacion_list.html'
    #----UD6.8.b----
    #pagina_by que sirve para paginar los resultados usando pagination.html
    paginate_by = 3

#----UD8.3.a----
#Decorador de login_required - solo se puede acceder si el usuario está autenticado
@method_decorator(login_required, name='dispatch')
class AsociacionDetailView(DetailView):
    model = Asociacion
    template_name = 'directorio_comercios/asociacion_detail.html'
    #----UD6.8.b----
    #pagina_by que sirve para paginar los resultados usando pagination.html
    paginate_by = 3

#----UD7.2.a----
#Vista de crear, actualizar y eliminar una asociación
#----UD8.3.a----
#Decorador de login_required - solo se puede acceder si el usuario está autenticado
@method_decorator(login_required, name='dispatch')
class AsoCreateView(CreateUpdateMixin, CreateView):
    model = Asociacion
    #template_name = 'common/base_create_udpate.html'
    #fields = '__all__'
    success_url = 'asociacion_update'
    #----UD7.3.a-----
    # implementacion de form
    form_class = AsociacionForm
    #----UD7.4.a----
    # Mensaje de creacion
    success_message = 'Asociación creada con éxito.'

#----UD8.3.a----
#Decorador de login_required - solo se puede acceder si el usuario está autenticado 
@method_decorator(login_required, name='dispatch')
class AsopdateView(CreateUpdateMixin, UpdateView):
    model = Asociacion
      # Permite la especificación del formulario en las vistas
    #template_name = 'common/base_create_udpate.html'
    #fields = '__all__'
    success_url = 'asociacion_update'
    url_borrado = 'asociacion_delete'
    #----UD7.3.a-----
    # implementacion de form
    form_class = AsociacionForm
    #----UD7.4.a----
    # Mensaje de actualización
    success_message = 'Asociación actualizada con éxito.'

#--UD7.2.b----
#Vista de eliminar una asociación
#----UD8.3.a----
#Decorador de login_required - solo se puede acceder si el usuario está autenticado 
@method_decorator(login_required, name='dispatch')
class AsoDeleteView(DeleteMixin, DeleteView):
    model = Asociacion
    #template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('asociacion_list')
    success_message = "La asociación ha sido eliminada con éxito."
    error_message = "No se puede eliminar la asociación porque tiene comercios asociados."
    mensaje_confirmacion = "¿Está seguro que quiere eliminar esta Asociación?"


#----UD7.2.g----
#Llamada a la clase de OrderedListMixin para ordering por query de la list
@method_decorator(login_required, name='dispatch')
class ComercioListView(OrderedListMixin, ListView):
    model = Comercio
    template_name = 'directorio_comercios/comercio_list.html'
    #----UD6.8.b----
    #pagina_by que sirve para paginar los resultados usando pagination.html
    paginate_by = 3

#----UD8.3.a----
#Decorador de login_required - solo se puede acceder si el usuario está autenticado 
@method_decorator(login_required, name='dispatch')
class ComercioDetailView(DetailView):
    model = Comercio
    template_name = 'directorio_comercios/comercio_detail.html'
    #----UD6.8.b----
    #pagina_by que sirve para paginar los resultados usando pagination.html
    paginate_by = 3

#----UD7.2.a----
#Vista de crear, actualizar y eliminar un comercio
#----UD8.3.a----
#Decorador de login_required - solo se puede acceder si el usuario está autenticado 
@method_decorator(login_required, name='dispatch')
class ComercioCreateView(CreateUpdateMixin, CreateView):
    model = Comercio
    #template_name = 'common/base_create_udpate.html'
    #fields = '__all__'
    success_url = 'comercio_update'
    #----UD7.3.a-----
    # implementacion de form
    form_class = ComercioForm
    #----UD7.4.a----
    # Mensaje de creacion
    success_message = 'Comercio creado con éxito.'

#----UD8.3.a----
#Decorador de login_required - solo se puede acceder si el usuario está autenticado 
@method_decorator(login_required, name='dispatch')
class ComercioUpdateView(CreateUpdateMixin, UpdateView):
    model = Comercio
    #template_name = 'common/base_create_udpate.html'
    #fields = '__all__'
    url_borrado = 'comercio_delete'
    success_url = 'comercio_update'
    #----UD7.3.a-----
    # implementacion de form
    form_class = ComercioForm
    #----UD7.4.a----
    # Mensaje de actualización
    success_message = 'Comercio actualizado con éxito.'

#--UD7.2.b----
#Vista de eliminar un comercio
#----UD8.3.a----
#Decorador de login_required - solo se puede acceder si el usuario está autenticado 
@method_decorator(login_required, name='dispatch')
class ComercioDeleteView(DeleteMixin, DeleteView):
    model = Comercio
    #template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('comercio_list')
    success_message = "El comercio ha sido eliminado con éxito."
    mensaje_confirmacion = "¿Está seguro que quiere eliminar este Comercio?"
