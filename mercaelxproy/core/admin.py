from django.contrib import admin

# Register your models here.
from .models import Provincia, Ciudad, Distrito

#--------UD6.4.a-UD6.4.b--------
#Registro los moodelos en la administración de Django(Provincia)
class ProvinciaAdmin(admin.ModelAdmin): # Defino la clase ProvinciaAdmin para personalizar la administración del modelo de Provincia
    list_display = ('id', 'codigo', 'nombre')  # Mostrar estos campos en la vista de lista
    list_display_links = ('codigo', 'nombre')  # Hacer codigo y nombre clicables
    search_fields = ('codigo', 'nombre')  # Añadir capacidad de búsqueda para codigo y nombre
    readonly_fields = ('id',)  # Hacer id de solo lectura

admin.site.register(Provincia, ProvinciaAdmin) # Registro Provincia con la clase ProvinciaAdmin

#--------UD6.4.a-UD6.4.b--------
#Registro los moodelos en la administración de Django(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    list_display = ('codigo_provincia', 'codigo', 'nombre')
    list_display_links = ('codigo_provincia', 'codigo', 'nombre')
    list_filter = ('provincia',) # Añadir filtro por provincia
    search_fields = ('codigo', 'nombre', 'provincia__nombre')
    preserve_filters = True # Preservar los filtros

    def codigo_provincia(self, obj): # Método para mostrar el código de la provincia
        return obj.provincia.codigo
    
admin.site.register(Ciudad, CiudadAdmin)

#--------UD6.4.b--------
#Registro los moodelos en la administración de Django(Distrito)
class DistritoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo_ciudad')
    list_display_links = ('nombre', 'codigo_ciudad')
    list_filter = ('ciudad',)
    search_fields = ('nombre', 'ciudad__nombre') 
    preserve_filters = True 

    def codigo_ciudad(self, obj):
        return obj.ciudad.codigo

admin.site.register(Distrito, DistritoAdmin)