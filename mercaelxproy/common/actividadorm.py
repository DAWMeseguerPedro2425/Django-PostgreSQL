from core.models import Ciudad, Provincia, Distrito
from directorio_comercios.models import Asociacion, Categoria, Subcategoria, Comercio

#--------UD6.6--------
#Funciones sobre los modelos del proyecto

#Devuelve todos los comercios
def get_comercios_all():
    return Comercio.objects.all()

#Devuelve las 3 primeras categorías
#[:3] para limitar a 3
def get_cat_3():
    return Categoria.objects.all()[:3]#[:3] para limitar a 3

#Devuelve todos la comercios cuyo codigo poastal sea 033
def get_ra_not_0612():
    return Comercio.objects.filter(codigo_postal="033")

#Devuelve un queryset de los comercios cuyo id sea menor a 2, ordénalos por código, descendente.
#lt = less than / menor que
def get_com_id_lt_2_cod_des():
    return Comercio.objects.filter(id__lt=2).order_by('-codigo')

#Devuelve un queryset de las asociaciones cuyo id sea mayor a 2.
#gt = greater than / mayor que
def get_asoc_id_gt_2():
    return Asociacion.objects.filter(id__gt=2)

#Devuelve un queryset con los distritos que contienen la palabra "Carrús" en su nombre, ordenados por nombre ascendente.
#icontains = contiene la cadena
def get_dist_carrus_nom_des():
    return Distrito.objects.filter(nombre__icontains="Carrús").order_by('nombre')

#Devuelve un queryset con todas las ciudades, excluyendo aquellas cuyo código postal acabe en "01".
#No existe el elemento codigo_postal en la clase Ciudad actualmente 
def get_ciudad_post_not_01():
    return Ciudad.objects.exclude(codigo_postal__endswith="01")

#Devuelve un objeto de la clase Subcategoria cuya categoría contenga "Hostelería" y cuyo código acabe en "S".
#endswith = termina con
def get_sub_host_ends_S():
    return Subcategoria.objects.filter(categoria__nombre__icontains="Hostelería", codigo__endswith="S").first()

#Crea una categoría código CAT10, nombre "Comestibles", y la descripción igual al nombre.
def create_cat10():
    return Categoria.objects.create(codigo="CAT10", nombre="Comestibles", descripcion="Comestibles")

#Crea una nueva subcategoria SCAT15, con nombre "Supermercados", Categoría con código CAT10.
def create_sub10():
    categoria = Categoria.objects.get(codigo="CAT10")
    return Subcategoria.objects.create(codigo="SCAT15", nombre="Supermercados", categoria=categoria)

#Modifica el nombre de la última provincia para concatenar el texto "(última)".
#last = último elemento
def update_last_provincia():
    provincia = Provincia.objects.last()
    provincia.nombre += " (última)"
    provincia.save()
    return provincia

#Eliminar los comercios cuya dirección contenga la palabra "Avenida", independientemente de que aparezca en minúsculas o mayúsculas.
def delete_com_avenida():
    return Comercio.objects.filter(direccion__icontains="avenida").delete()

