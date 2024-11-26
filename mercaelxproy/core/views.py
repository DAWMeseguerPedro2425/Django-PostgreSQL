from django.shortcuts import render
from django.views.generic import ListView, DetailView
from core.models import Provincia, Ciudad, Distrito
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from common.mixins import CreateUpdateMixin
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models.deletion import ProtectedError
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.messages import constants as messages


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

#----UD7.2.a-UD7.2.d-----
#Vista de crear, actualizar y eliminar una provincia
#version con mixin
class ProvCreateView(CreateUpdateMixin,CreateView):
    model = Provincia
    #template_name = 'common/base_create_update.html'
    #fields = '__all__' #campos que se van a mostrar en el formulario, __all__ significa que se van a mostrar todos los campos
    #----UD7.2.d-----
    #url de redirección del mixin
    success_url = 'provincia_update'

    
    #----UD7.2.c-UD7.2.d-----
    #contexto que se pasa a la plantilla y url de redirección
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['verbose_name'] = self.model._meta.verbose_name
    #     return context
    # def get_success_url(self):
    #     return reverse_lazy('provincia_update', kwargs={'pk': self.object.pk})

class ProvUpdateView(CreateUpdateMixin,UpdateView):
    model = Provincia
    #template_name = 'common/base_create_update.html'
    #fields = '__all__'
    #----UD7.2.d-----
    #url de redirección del mixin
    success_url = 'provincia_update'
    #----UD7.2.c----
    #url_borrado que se pasa a la plantilla para que se pueda borrar la provincia
    url_borrado = 'provincia_delete'
    #----UD7.2.c-----
    #contexto que se pasa a la plantilla y url de redirección
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['url_borrado'] = self.url_borrado
    #     context['verbose_name'] = self.model._meta.verbose_name
    #     return context

    # def get_success_url(self):
    #     return reverse_lazy('provincia_update', kwargs={'pk': self.object.pk})



class ProvDeleteView(SuccessMessageMixin, DeleteView):
    model = Provincia
    template_name = 'common/base_confirm_delete.html'
    titulo = "Eliminar una Provincia"
    success_url = reverse_lazy('provincia_list')

    success_message = "La provincia ha sido eliminada con éxito."
    error_message = "No se puede eliminar la provincia porque tiene ciudades asociadas."
    mensaje_confirmacion = "¿Está seguro que quiere eliminar esta Provincia?"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = self.titulo
        context['mensaje_confirmacion'] = self.mensaje_confirmacion
        context['cancel_url'] = reverse_lazy('provincia_list')
        return context

    def get_success_url(self):
        return self.success_url
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
            messages.success(request, self.success_message)
        except ProtectedError:
            messages.error(request, self.error_message)
        return redirect(self.success_url)

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

#----UD7.2.a----
#Vista de crear, actualizar y eliminar una ciudad
class CiudadCreateView(CreateUpdateMixin, CreateView):
    model = Ciudad
    #template_name = 'common/base_create_update.html'
    #fields = '__all__'
    success_url = 'ciudad_update'

    #----UD7.2.c-----
    #contexto que se pasa a la plantilla y url de redirección
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['verbose_name'] = self.model._meta.verbose_name
    #     return context
    # def get_success_url(self):
    #     return reverse_lazy('ciudad_update', kwargs={'pk': self.object.pk})

class CiudadUpdateView(CreateUpdateMixin, UpdateView):
    model = Ciudad
    #template_name = 'common/base_create_update.html'
    #fields = '__all__'
    success_url = 'ciudad_update'
    #----UD7.2.c----
    #url_borrado que se pasa a la plantilla para que se pueda borrar la ciudad
    url_borrado = 'ciudad_delete'

    #----UD7.2.c-----
    #contexto que se pasa a la plantilla y url de redirección
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['url_borrado'] = self.url_borrado
    #     context['verbose_name'] = self.model._meta.verbose_name
    #     return context
    # def get_success_url(self):
    #     return reverse_lazy('ciudad_update', kwargs={'pk': self.object.pk})


class CiudadDeleteView(DeleteView):
    model = Ciudad
    template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('ciudad_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['verbose_name'] = self.model._meta.verbose_name
        return context
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Verificar si hay Distritos relacionados
        if self.object.distrito_set.exists():
            messages.error(request, "No se puede eliminar la ciudad porque tiene distritos asociados.")
            return redirect('ciudad_list')
        return super().delete(request, *args, **kwargs)


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

#----UD7.2.a----
#Vista de crear, actualizar y eliminar un distrito
class DistCreateView(CreateUpdateMixin, CreateView):
    model = Distrito
    #template_name = 'common/base_create_update.html'
    #fields = '__all__'
    success_url = 'distrito_update'

    #----UD7.2.c-----
    #contexto que se pasa a la plantilla y url de redirección
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['verbose_name'] = self.model._meta.verbose_name
    #     return context
    # def get_success_url(self):
    #     return reverse_lazy('distrito_update', kwargs={'pk': self.object.pk})

class DistUpdateView(CreateUpdateMixin, UpdateView):
    model = Distrito
    #template_name = 'common/base_create_udpate.html'
    fields = '__all__'
    #success_url = 'distrito_update'
    #----UD7.2.c----
    #url_borrado que se pasa a la plantilla para que se pueda borrar el distrito
    url_borrado = 'distrito_delete'

    #----UD7.2.c-----
    #contexto que se pasa a la plantilla y url de redirección
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['url_borrado'] = self.url_borrado
    #     context['verbose_name'] = self.model._meta.verbose_name
    #     return context
    # def get_success_url(self):
    #     return reverse_lazy('distrito_update', kwargs={'pk': self.object.pk})

class DistDeleteView(DeleteView):
    model = Distrito
    template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('distrito_list')
    
    titulo = "Eliminar un Distrito"
    mensaje_confirmación = "¿Está seguro que quiere eliminar este Distrito?"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = self.titulo
        context['mensaje_confirmación'] = self.mensaje_confirmación
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.comercio_set.exists():
            messages.error(request, "No se puede eliminar el distrito porque tiene comercios asociados.")
            return redirect('distrito_list')
        return super().delete(request, *args, **kwargs)