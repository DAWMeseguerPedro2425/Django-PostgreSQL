"""
URL configuration for mercaelxproy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from common import views as common_views
from core import views as core_views
#--------UD7.b--------
#Importar las vistas de la aplicación directorio_comercios con
#  el nombre comercios_views
from directorio_comercios import views as comercios_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', common_views.HomeView.as_view(), name='home'),
    path('panel/', common_views.PanelView.as_view(), name='panel'),
    path('provincia_list/', core_views.ProvinciaListView.as_view(), name='provincia_list'),
    path('provincia_detail/<int:pk>/', core_views.ProvinciaDetailView.as_view(), name='provincia_detail'),
    path('ciudad_list/', core_views.CiudadListView.as_view(), name='ciudad_list'),
    path('ciudad_detail/<int:pk>/', core_views.CiudadDetailView.as_view(), name='ciudad_detail'),
    path('distrito_list/', core_views.DistritoListView.as_view(), name='distrito_list'),
    path('distrito_detail/<int:pk>/', core_views.DistritoDetailView.as_view(), name='distrito_detail'),
    
    #--------UD7.b--------
    #URLs de la aplicación directorio_comercios
    path('categoria_list/', comercios_views.CategoriaListView.as_view(), name='categoria_list'),
    path('categoria_detail/<int:pk>/', comercios_views.CategoriaDetailView.as_view(), name='categoria_detail'),
    path('subcategoria_list/', comercios_views.SubCategoriaListView.as_view(), name='subcategoria_list'),
    path('subcategoria_detail/<int:pk>/', comercios_views.SubCategoriaDetailView.as_view(), name='subcategoria_detail'),
    path('asociacion_list/', comercios_views.AsociacionListView.as_view(), name='asociacion_list'),
    path('asociacion_detail/<int:pk>/', comercios_views.AsociacionDetailView.as_view(), name='asociacion_detail'),
    path('comercio_list/', comercios_views.ComercioListView.as_view(), name='comercio_list'),
    path('comercio_detail/<int:pk>/', comercios_views.ComercioDetailView.as_view(), name='comercio_detail'),
]

#-----UD6.2.e-----
#Referenciar imagenes en el proyecto
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)