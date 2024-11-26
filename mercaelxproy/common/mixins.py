from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

#----UD7.2.d----
#Clase de mixin para pasar la url de borrado a la plantilla
class CreateUpdateMixin:
    url_borrado = None
    success_url = None
    fields = '__all__'#campos que se van a mostrar en el formulario, __all__ significa que se van a mostrar todos los campos
    template_name = 'common/base_create_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['verbose_name'] = self.model._meta.verbose_name
        context['url_borrado'] = self.url_borrado
        return context
    
    def get_success_url(self):
        return reverse_lazy(self.success_url, kwargs={'pk': self.object.pk})