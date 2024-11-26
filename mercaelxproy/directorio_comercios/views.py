from django.shortcuts import render
from django.views.generic import ListView, DetailView
from directorio_comercios.models import Categoria, Subcategoria, Asociacion, Comercio
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from common.mixins import CreateUpdateMixin

#--------UD6.7.a--------
#Crear las vistas de la aplicación directorio_comercios para mostrar las categorías, subcategorías, asociaciones y comercios
# según la tabla 1 de anexo 2

class CategoriaListView(ListView): # ListView es una clase de Django que muestra una lista de objetos de un modelo
    model = Categoria
    template_name = 'directorio_comercios/categoria_list.html'
    #----UD6.8.b----
    #pagina_by que sirve para paginar los resultados usando pagination.html
    paginate_by = 3

class CategoriaDetailView(DetailView): # DetailView es una clase de Django que muestra los detalles de un objeto de un modelo
    model = Categoria
    template_name = 'directorio_comercios/categoria_detail.html'
    #----UD6.8.b----
    #pagina_by que sirve para paginar los resultados usando pagination.html
    paginate_by = 3

#----UD7.2.a----
#Vista de crear, actualizar y eliminar una categoría
class CategoriaCreateView(CreateUpdateMixin, CreateView):
    model = Categoria
    #template_name = 'common/base_create_udpate.html'
    #fields = '__all__'
    success_url = 'categoria_update'


    #----UD7.2.c-----
    #contexto que se pasa a la plantilla y url de redirección
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['verbose_name'] = self.model._meta.verbose_name
    #     return context
    # def get_success_url(self):
    #     return reverse_lazy('categoria_update', kwargs={'pk': self.object.pk})

class CategoriaUpdateView(CreateUpdateMixin, UpdateView):
    model = Categoria
    #template_name = 'common/base_create_udpate.html'
    #fields = '__all__'
    success_url = 'categoria_update'
    url_borrado = 'categoria_delete'

    #----UD7.2.c-----
    #contexto que se pasa a la plantilla y url de redirección
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['url_borrado'] = self.url_borrado
    #     context['verbose_name'] = self.model._meta.verbose_name
    #     return context
    # def get_success_url(self):
    #     return reverse_lazy('categoria_update', kwargs={'pk': self.object.pk})


class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('categoria_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['verbose_name'] = self.model._meta.verbose_name
        return context
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Verificar si hay Subcategorías relacionadas
        if self.object.subcategoria_set.exists():
            messages.error(request, "No se puede eliminar la categoría porque tiene subcategorías asociadas.")
            return redirect('categoria_list')
        return super().delete(request, *args, **kwargs)

class SubCategoriaListView(ListView):
    model = Subcategoria
    template_name = 'directorio_comercios/subcategoria_list.html'
    #----UD6.8.b----
    #pagina_by que sirve para paginar los resultados usando pagination.html
    paginate_by = 3

class SubCategoriaDetailView(DetailView):
    model = Subcategoria
    template_name = 'directorio_comercios/subcategoria_detail.html'
    #----UD6.8.b----
    #pagina_by que sirve para paginar los resultados usando pagination.html
    paginate_by = 3

#----UD7.2.a----
#Vista de crear, actualizar y eliminar una subcategoría
class SubcategoriaCreateView(CreateUpdateMixin, CreateView):
    model = Subcategoria
    #template_name = 'common/base_create_udpate.html'
    #fields = '__all__'
    success_url = 'subcategoria_update'


    #----UD7.2.c-----
    #contexto que se pasa a la plantilla y url de redirección
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['verbose_name'] = self.model._meta.verbose_name
    #     return context
    # def get_success_url(self):
    #     return reverse_lazy('subcategoria_update', kwargs={'pk': self.object.pk})

class SubcategoriaUpdateView(CreateUpdateMixin, UpdateView):
    model = Subcategoria
    #template_name = 'common/base_create_udpate.html'
    #fields = '__all__'
    success_url = 'subcategoria_update'

    url_borrado = 'subcategoria_delete'

    #----UD7.2.c-----
    #contexto que se pasa a la plantilla y url de redirección
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['url_borrado'] = self.url_borrado
    #     context['verbose_name'] = self.model._meta.verbose_name
    #     return context
    # def get_success_url(self):
    #     return reverse_lazy('subcategoria_update', kwargs={'pk': self.object.pk})

class SubcategoriaDeleteView(DeleteView):
    model = Subcategoria
    template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('subcategoria_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['verbose_name'] = self.model._meta.verbose_name
        return context
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Verificar si hay Comercios relacionados
        if self.object.comercio_set.exists():
            messages.error(request, "No se puede eliminar la subcategoría porque tiene comercios asociados.")
            return redirect('subcategoria_list')
        return super().delete(request, *args, **kwargs)

class AsociacionListView(ListView):
    model = Asociacion
    template_name = 'directorio_comercios/asociacion_list.html'
    #----UD6.8.b----
    #pagina_by que sirve para paginar los resultados usando pagination.html
    paginate_by = 3

class AsociacionDetailView(DetailView):
    model = Asociacion
    template_name = 'directorio_comercios/asociacion_detail.html'
    #----UD6.8.b----
    #pagina_by que sirve para paginar los resultados usando pagination.html
    paginate_by = 3

#----UD7.2.a----
#Vista de crear, actualizar y eliminar una asociación
class AsoCreateView(CreateUpdateMixin, CreateView):
    model = Asociacion
    #template_name = 'common/base_create_udpate.html'
    #fields = '__all__'
    success_url = 'asociacion_update'

    #----UD7.2.c-----
    #contexto que se pasa a la plantilla y url de redirección
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['url_borrado'] = self.url_borrado
    #     context['verbose_name'] = self.model._meta.verbose_name
    #     return context
    # def get_success_url(self):
    #     return reverse_lazy('asociacion_update', kwargs={'pk': self.object.pk})

class AsopdateView(CreateUpdateMixin, UpdateView):
    model = Asociacion
    #template_name = 'common/base_create_udpate.html'
    #fields = '__all__'
    success_url = 'asociacion_update'

    url_borrado = 'asociacion_delete'

    #----UD7.2.c-----
    #contexto que se pasa a la plantilla y url de redirección
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['url_borrado'] = self.url_borrado
    #     context['verbose_name'] = self.model._meta.verbose_name
    #     return context
    # def get_success_url(self):
    #     return reverse_lazy('asociacion_update', kwargs={'pk': self.object.pk})

class AsoDeleteView(DeleteView):
    model = Asociacion
    template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('asociacion_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['verbose_name'] = self.model._meta.verbose_name
        return context
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Verificar si hay Comercios relacionados
        if self.object.comercio_set.exists():
            messages.error(request, "No se puede eliminar la asociación porque tiene comercios asociados.")
            return redirect('asociacion_list')
        return super().delete(request, *args, **kwargs)


class ComercioListView(ListView):
    model = Comercio
    template_name = 'directorio_comercios/comercio_list.html'
    #----UD6.8.b----
    #pagina_by que sirve para paginar los resultados usando pagination.html
    paginate_by = 3

class ComercioDetailView(DetailView):
    model = Comercio
    template_name = 'directorio_comercios/comercio_detail.html'
    #----UD6.8.b----
    #pagina_by que sirve para paginar los resultados usando pagination.html
    paginate_by = 3

#----UD7.2.a----
#Vista de crear, actualizar y eliminar un comercio
class ComercioCreateView(CreateUpdateMixin, CreateView):
    model = Comercio
    #template_name = 'common/base_create_udpate.html'
    #fields = '__all__'
    success_url = 'comercio_update'

    #----UD7.2.c-----
    #contexto que se pasa a la plantilla y url de redirección
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['verbose_name'] = self.model._meta.verbose_name
    #     return context
    # def get_success_url(self):
    #     return reverse_lazy('comercio_update', kwargs={'pk': self.object.pk})

class ComercioUpdateView(CreateUpdateMixin, UpdateView):
    model = Comercio
    #template_name = 'common/base_create_udpate.html'
    #fields = '__all__'
    url_borrado = 'comercio_delete'
    success_url = 'comercio_update'


    #----UD7.2.c-----
    #contexto que se pasa a la plantilla y url de redirección
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['url_borrado'] = self.url_borrado
    #     context['verbose_name'] = self.model._meta.verbose_name
    #     return context
    # def get_success_url(self):
    #     return reverse_lazy('comercio_update', kwargs={'pk': self.object.pk})

class ComercioDeleteView(DeleteView):
    model = Comercio
    template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('comercio_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['verbose_name'] = self.model._meta.verbose_name
        return context
    def delete(self, request, *args, **kwargs):
        # Si Comercio no tiene dependencias, se puede eliminar directamente
        return super().delete(request, *args, **kwargs)