from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import ProtectedError





#----UD7.2.d----
#Clase de mixin para pasar los campos de plantilla de Update y Create
class CreateUpdateMixin(SuccessMessageMixin):
    url_borrado = None
    success_url = None
    #fields = '__all__'#campos que se van a mostrar en el formulario, __all__ significa que se van a mostrar todos los campos
    template_name = 'common/base_create_update.html'
    success_message = None
    form_class = None  # Permite la especificación del formulario en las vistas

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['verbose_name'] = self.model._meta.verbose_name #nombre de la clase en singular especificado en la clase Meta del modelo
        context['url_borrado'] = self.url_borrado
        return context
    
    def get_success_url(self):
        return reverse_lazy(self.success_url, kwargs={'pk': self.object.pk})


#----UD7.2.f----
#Clase de mixin para elimnar un projecot y verificar las dependencias
class DeleteMixin(SuccessMessageMixin):
    template_name = 'common/base_confirm_delete.html' # ruta plantilla
    success_url = None
    success_message = None
    error_message = None
    mensaje_confirmacion = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = self.model._meta.verbose_name # titulo en la plantilla
        context['mensaje_confirmacion'] = self.mensaje_confirmacion # mensaje de eleimincaion especificado
        context['cancel_url'] = self.success_url # ur en el bonton de cancel
        return context

    def get_success_url(self):
        return self.success_url


    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ProtectedError:
            messages.error(
                self.request,
                self.error_message
            )
            return HttpResponseRedirect(self.success_url)

#----UD7.2.g----
#Clase de mixin para ordenancion con query_set
class OrderedListMixin:
    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.GET.get('ordering', 'asc')
        if ordering == 'desc':
            return queryset.order_by('-id')
        return queryset.order_by('id')