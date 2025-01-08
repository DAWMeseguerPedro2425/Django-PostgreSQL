from django.shortcuts import render
from django.views.generic import ListView, DetailView
from core.models import Provincia, Ciudad, Distrito
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from common.mixins import CreateUpdateMixin, DeleteMixin, OrderedListMixin, LoginRequiredMixin
from .forms import *

#----UD7.2.g----
#Llamada a la clase de OrderedListMixin para ordering por query de la list
#----UD8.3----
#Vistas de provincias con login_required para acceder a las vistas
class ProvinciaListView(LoginRequiredMixin, OrderedListMixin, ListView):
    model = Provincia
    template_name = 'core/provincia_list.html'
    #----UD6.8.b----
    #pagina_by que sirve para paginar los resultados usando pagination.html
    paginate_by = 3

#----UD8.3----
class ProvinciaDetailView(LoginRequiredMixin, DetailView):
    model = Provincia
    template_name = 'core/provincia_detail.html'
    #----UD6.8.b----
    #pagina_by que sirve para paginar los resultados usando pagination.html
    paginate_by = 3

#----UD7.2.a-UD7.2.d-----
#Vista de crear, actualizar y eliminar una provincia
#version con mixin
#----UD8.3----
class ProvCreateView(LoginRequiredMixin, CreateUpdateMixin,CreateView):
    model = Provincia
    #template_name = 'common/base_create_update.html'
    #fields = '__all__' #campos que se van a mostrar en el formulario, __all__ significa que se van a mostrar todos los campos
    #----UD7.2.d-----
    #url de redirección del mixin
    success_url = 'provincia_update'
    #----UD7.3.a-----
    # implementacion de form
    form_class = ProvinciaForm
    #----UD7.4.a----
    # Mensaje de creación
    success_message = 'Provincia creada con éxito.'
    
    #----UD7.2.c-UD7.2.d-----
    #contexto que se pasa a la plantilla y url de redirección
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['verbose_name'] = self.model._meta.verbose_name
    #     return context
    # def get_success_url(self):
    #     return reverse_lazy('provincia_update', kwargs={'pk': self.object.pk})

#----UD8.3----
class ProvUpdateView(LoginRequiredMixin, CreateUpdateMixin,UpdateView):
    model = Provincia
    #template_name = 'common/base_create_update.html'
    #fields = '__all__'
    #----UD7.2.d-----
    #url de redirección del mixin
    success_url = 'provincia_update'
    #----UD7.2.c----
    #url_borrado que se pasa a la plantilla para que se pueda borrar la provincia
    url_borrado = 'provincia_delete'
    #----UD7.3.a-----
    # implementacion de form
    form_class = ProvinciaForm
    #----UD7.4.a----
    # Mensaje de actualización
    success_message = 'Provincia actualizada con éxito.'
    


    #----UD7.2.c-----
    #contexto que se pasa a la plantilla y url de redirección
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['url_borrado'] = self.url_borrado
    #     context['verbose_name'] = self.model._meta.verbose_name
    #     return context

    # def get_success_url(self):
    #     return reverse_lazy('provincia_update', kwargs={'pk': self.object.pk})


#----UD7.2.f-----
#version delete mixin provincia
#----UD8.3----
class ProvDeleteView(LoginRequiredMixin, DeleteMixin, DeleteView):
    model = Provincia
    #template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('provincia_list')
    success_message = "La provincia ha sido eliminada con éxito." #Mesaje de eleiminacion exitoso
    error_message = "No se puede eliminar la provincia porque tiene ciudades asociadas."#Mensaje de fallo por dependencias de delete
    mensaje_confirmacion = "¿Está seguro que quiere eliminar esta Provincia?" #Mensaje de la pantalla de delete


    
#----UD7.2.g----
#Llamada a la clase de OrderedListMixin para ordering por query de la list
#----UD8.3----
#Vistas de ciudades con login_required para acceder a las vistas
class CiudadListView(LoginRequiredMixin, OrderedListMixin, ListView):
    model = Ciudad
    template_name = 'core/ciudad_list.html'
    #----UD6.8.b----
    #pagina_by que sirve para paginar los resultados usando pagination.html
    paginate_by = 3

#----UD8.3----
class CiudadDetailView(LoginRequiredMixin, DetailView):
    model = Ciudad
    template_name = 'core/ciudad_detail.html'
    #----UD6.8.b----
    #pagina_by que sirve para paginar los resultados usando pagination.html
    paginate_by = 3

#----UD7.2.a----
#Vista de crear, actualizar y eliminar una ciudad
#----UD8.3----
class CiudadCreateView(LoginRequiredMixin, CreateUpdateMixin, CreateView):
    model = Ciudad
    #template_name = 'common/base_create_update.html'
    #fields = '__all__'
    success_url = 'ciudad_update'
    #----UD7.3.a-----
    # implementacion de form
    form_class = CiudadForm
    #----UD7.4.a----
    # Mensaje de creación
    success_message = 'Ciudad creada con éxito.'
    #----UD7.2.c-----
    #contexto que se pasa a la plantilla y url de redirección
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['verbose_name'] = self.model._meta.verbose_name
    #     return context
    # def get_success_url(self):
    #     return reverse_lazy('ciudad_update', kwargs={'pk': self.object.pk})

#----UD8.3----
class CiudadUpdateView(LoginRequiredMixin, CreateUpdateMixin, UpdateView):
    model = Ciudad
    #template_name = 'common/base_create_update.html'
    #fields = '__all__'
    success_url = 'ciudad_update'
    #----UD7.2.c----
    #url_borrado que se pasa a la plantilla para que se pueda borrar la ciudad
    url_borrado = 'ciudad_delete'
    #----UD7.3.a-----
    # implementacion de form
    form_class = CiudadForm
    #----UD7.4.a----
    # Mensaje de actualización
    success_message = 'Ciudad actualizada con éxito.'
    #----UD7.2.c-----
    #contexto que se pasa a la plantilla y url de redirección
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['url_borrado'] = self.url_borrado
    #     context['verbose_name'] = self.model._meta.verbose_name
    #     return context
    # def get_success_url(self):
    #     return reverse_lazy('ciudad_update', kwargs={'pk': self.object.pk})


#----UD7.2.f-----
# version delete mixin ciudad
#----UD8.3----
class CiudadDeleteView(LoginRequiredMixin, DeleteMixin, DeleteView):
    model = Ciudad
    #template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('ciudad_list')
    success_message = "La ciudad ha sido eliminada con éxito."
    error_message = "No se puede eliminar la ciudad porque tiene distritos asociados." 
    mensaje_confirmacion = "¿Está seguro que quiere eliminar esta Ciudad?"


#----UD7.2.g----
#Llamada a la clase de OrderedListMixin para ordering por query de la list
#----UD8.3----
#Vistas de distritos con login_required para acceder a las vistas
class DistritoListView(LoginRequiredMixin, OrderedListMixin, ListView):
    model = Distrito
    template_name = 'core/distrito_list.html'
    #----UD6.8.b----
    #pagina_by que sirve para paginar los resultados usando pagination.html
    paginate_by = 3

#----UD8.3----
class DistritoDetailView(LoginRequiredMixin, DetailView):
    model = Distrito
    template_name = 'core/distrito_detail.html'
    #----UD6.8.b----
    #pagina_by que sirve para paginar los resultados usando pagination.html
    paginate_by = 3

#----UD7.2.a----
#Vista de crear, actualizar y eliminar un distrito
#----UD8.3----
class DistCreateView(LoginRequiredMixin, CreateUpdateMixin, CreateView):
    model = Distrito
    #template_name = 'common/base_create_update.html'
    #fields = '__all__'
    success_url = 'distrito_update'
    #----UD7.3.a-----
    # implementacion de form
    form_class = DistritoForm
    #----UD7.4.a----
    # Mensaje de creación
    success_message = 'Distrito creado con éxito.'

    #----UD7.2.c-----
    #contexto que se pasa a la plantilla y url de redirección
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['verbose_name'] = self.model._meta.verbose_name
    #     return context
    # def get_success_url(self):
    #     return reverse_lazy('distrito_update', kwargs={'pk': self.object.pk})

#----UD8.3----
class DistUpdateView(LoginRequiredMixin, CreateUpdateMixin, UpdateView):
    model = Distrito
    #template_name = 'common/base_create_udpate.html'
    fields = '__all__'
    #success_url = 'distrito_update'
    #----UD7.2.c----
    #url_borrado que se pasa a la plantilla para que se pueda borrar el distrito
    url_borrado = 'distrito_delete'
    #----UD7.3.a-----
    # implementacion de form
    form_class = DistritoForm
    #----UD7.4.a----
    # Mensaje de actualización
    success_message = 'Distrito actualizado con éxito.'

    #----UD7.2.c-----
    #contexto que se pasa a la plantilla y url de redirección
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['url_borrado'] = self.url_borrado
    #     context['verbose_name'] = self.model._meta.verbose_name
    #     return context
    # def get_success_url(self):
    #     return reverse_lazy('distrito_update', kwargs={'pk': self.object.pk})

#----UD7.2.f-----
# version delete mixin distrito
#----UD8.3----
class DistDeleteView(LoginRequiredMixin, DeleteMixin, DeleteView):
    model = Distrito
    #template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('distrito_list')
    success_message = "El distrito ha sido eliminado con éxito."
    error_message = "No se puede eliminar el distrito porque tiene comercios asociados."
    mensaje_confirmacion = "¿Está seguro que quiere eliminar este Distrito?"

