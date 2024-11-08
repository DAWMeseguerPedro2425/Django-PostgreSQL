from core.models import Ciudad, Provincia, Distrito
from directorio_comercios.models import Asociacion, Categoria, Subcategoria, Comercio

#--------UD6.6--------
#Funciones sobre los modelos del proyecto

#Devuelve todos los comercios
def get_comercios_all():
    return Comercio.objects.all()

#Devuelve las 3 primeras categorías
def get_cat_3():
    return Categoria.objects.all()[:3]#[:3] para limitar a 3

#Devuelve todas la ciduades cuyo codigo poastal sea 033
def get_ra_not_0612():
    return Ciudad.objects.filter(codigo="033")