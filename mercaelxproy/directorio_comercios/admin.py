from django.contrib import admin

# Register your models here.
from .models import Asociacion, Categoria, Subcategoria, Comercio

#--------UD6.3.a-DU6.3.c--------
#Registro los modelos en la administración de Django(Asociacion)

class AsociacionAdmin(admin.ModelAdmin):# Defino la clase AsociacionAdmin para personalizar la administración del modelo de Asociacion
    list_display = ('codigo_ciudad', 'nombre')  # Mostrar codigo_ciudad y nombre en la vista de lista
    list_display_links = ('codigo_ciudad', 'nombre')  # Hacer estos campos clicables
    search_fields = ('nombre', 'ciudad__nombre', 'direccion')  # Buscar por nombre, ciudad__nombre y direccion

    def codigo_ciudad(self, obj):  # Método para mostrar el codigo de la ciudad
        return obj.ciudad.codigo
    codigo_ciudad.short_description = 'Código Ciudad'

admin.site.register(Asociacion, AsociacionAdmin) # Registro de Asociacion con la clase AsociacionAdmin

#--------UD6.3.a-DU6.3.c--------
#Registro los modelos en la administración de Django(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    list_display_links = ('codigo', 'nombre')
    search_fields = ('codigo', 'nombre')

admin.site.register(Categoria, CategoriaAdmin)

#--------UD6.3.a-DU6.3.c--------
#Registro los modelos en la administración de Django(Subcategoria)
class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ('codigo_categoria', 'codigo', 'nombre')
    list_display_links = ('codigo_categoria', 'codigo', 'nombre')
    list_filter = ('categoria',) #Añadir filtro por categoria
    search_fields = ('categoria__codigo', 'codigo', 'nombre', 'categoria__nombre')
    preserve_filters = True #Preservar los filtros

    def codigo_categoria(self, obj):
        return obj.categoria.codigo
    codigo_categoria.short_description = 'Código Categoria'

admin.site.register(Subcategoria, SubcategoriaAdmin)

#--------UD6.3.a-DU6.3.c--------
#Registro los modelos en la administración de Django(Comercio)
class ComercioAdmin(admin.ModelAdmin):
    list_display = ('codigo_ciudad', 'codigo_categoria', 'codigo_subcategoria', 'nombre', 'codigo_postal')
    list_display_links = ('codigo_ciudad', 'codigo_categoria', 'codigo_subcategoria', 'nombre', 'codigo_postal')
    list_filter = ('ciudad', 'categoria', 'subcategoria', 'asociacion')
    search_fields = (
        'nombre', 'codigo_postal', 'direccion',
        'ciudad__nombre', 'categoria__codigo', 'categoria__nombre',
        'subcategoria__codigo', 'subcategoria__nombre',
        'asociacion__nombre'
    )
    preserve_filters = True

    def codigo_ciudad(self, obj):
        return obj.ciudad.codigo
    codigo_ciudad.short_description = 'Código Ciudad'

    def codigo_categoria(self, obj):
        return obj.categoria.codigo
    codigo_categoria.short_description = 'Código Categoria'

    def codigo_subcategoria(self, obj):
        return obj.subcategoria.codigo if obj.subcategoria else 'N/A'
    codigo_subcategoria.short_description = 'Código Subcategoria'

admin.site.register(Comercio, ComercioAdmin)