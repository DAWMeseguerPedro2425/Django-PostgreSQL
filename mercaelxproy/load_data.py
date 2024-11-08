import os
import django

# Configuración del entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mercaelxproy.settings')
django.setup()

# Importar modelos
from core.models import Ciudad, Provincia, Distrito
from directorio_comercios.models import Asociacion, Categoria, Subcategoria, Comercio

def cargar_datos():
    # Crear provincias
    provincia1 = Provincia.objects.create(codigo="P001", nombre="Alicante")
    provincia2 = Provincia.objects.create(codigo="P002", nombre="Valencia")

    # Crear ciudades (5 ciudades distintas)
    ciudad1 = Ciudad.objects.create(codigo="C001", nombre="Orihuela", provincia=provincia1)
    ciudad2 = Ciudad.objects.create(codigo="C002", nombre="Alicante", provincia=provincia1)
    ciudad3 = Ciudad.objects.create(codigo="C003", nombre="Valencia", provincia=provincia2)
    ciudad4 = Ciudad.objects.create(codigo="C004", nombre="Torrent", provincia=provincia2)
    ciudad5 = Ciudad.objects.create(codigo="C005", nombre="Gandía", provincia=provincia2)

    # Crear distritos (1 distrito por ciudad)
    Distrito.objects.create(ciudad=ciudad1, nombre="Centro")
    Distrito.objects.create(ciudad=ciudad2, nombre="Santa Cruz")
    Distrito.objects.create(ciudad=ciudad3, nombre="Ciutat Vella")
    Distrito.objects.create(ciudad=ciudad4, nombre="El Pla")
    Distrito.objects.create(ciudad=ciudad5, nombre="Marquesado")

    # Crear asociaciones (1 asociación por ciudad)
    Asociacion.objects.create(nombre="Asociación Comerciantes Orihuela", ciudad=ciudad1)
    Asociacion.objects.create(nombre="Asociación Comerciantes Alicante", ciudad=ciudad2)
    Asociacion.objects.create(nombre="Asociación Comerciantes Valencia", ciudad=ciudad3)
    Asociacion.objects.create(nombre="Asociación Comerciantes Torrent", ciudad=ciudad4)
    Asociacion.objects.create(nombre="Asociación Comerciantes Gandía", ciudad=ciudad5)

    # Crear categorías (3 categorías distintas)
    categoria1 = Categoria.objects.create(codigo="CAT01", nombre="Alimentos")
    categoria2 = Categoria.objects.create(codigo="CAT02", nombre="Electrónica")
    categoria3 = Categoria.objects.create(codigo="CAT03", nombre="Ropa")

    # Crear subcategorías (2 subcategorías por categoría)
    Subcategoria.objects.create(codigo="SUB01", nombre="Verduras", categoria=categoria1)
    Subcategoria.objects.create(codigo="SUB02", nombre="Frutas", categoria=categoria1)
    Subcategoria.objects.create(codigo="SUB03", nombre="Móviles", categoria=categoria2)
    Subcategoria.objects.create(codigo="SUB04", nombre="Ordenadores", categoria=categoria2)
    Subcategoria.objects.create(codigo="SUB05", nombre="Camisetas", categoria=categoria3)
    Subcategoria.objects.create(codigo="SUB06", nombre="Pantalones", categoria=categoria3)

    # Crear comercios (2 comercios por ciudad, con diferentes categorías y subcategorías)
    Comercio.objects.create(nombre="Frutería La Huerta", ciudad=ciudad1, categoria=categoria1, subcategoria=Subcategoria.objects.get(nombre="Verduras"), direccion="Calle Falsa 123")
    Comercio.objects.create(nombre="Frutería La Fruta", ciudad=ciudad1, categoria=categoria1, subcategoria=Subcategoria.objects.get(nombre="Frutas"), direccion="Calle Verdadera 321")

    Comercio.objects.create(nombre="Electrónica Juan", ciudad=ciudad2, categoria=categoria2, subcategoria=Subcategoria.objects.get(nombre="Móviles"), direccion="Calle de la Tecnología 1")
    Comercio.objects.create(nombre="Informatics", ciudad=ciudad2, categoria=categoria2, subcategoria=Subcategoria.objects.get(nombre="Ordenadores"), direccion="Calle Ordenadores 2")

    Comercio.objects.create(nombre="Moda Joven", ciudad=ciudad3, categoria=categoria3, subcategoria=Subcategoria.objects.get(nombre="Camisetas"), direccion="Calle Juventud 3")
    Comercio.objects.create(nombre="Fashion City", ciudad=ciudad3, categoria=categoria3, subcategoria=Subcategoria.objects.get(nombre="Pantalones"), direccion="Calle Moda 4")

    Comercio.objects.create(nombre="Frutería La Natural", ciudad=ciudad4, categoria=categoria1, subcategoria=Subcategoria.objects.get(nombre="Verduras"), direccion="Calle Verde 56")
    Comercio.objects.create(nombre="Eco Market", ciudad=ciudad4, categoria=categoria1, subcategoria=Subcategoria.objects.get(nombre="Frutas"), direccion="Calle Eco 78")

    Comercio.objects.create(nombre="ElectroShop", ciudad=ciudad5, categoria=categoria2, subcategoria=Subcategoria.objects.get(nombre="Móviles"), direccion="Calle Gadgets 90")
    Comercio.objects.create(nombre="PC World", ciudad=ciudad5, categoria=categoria2, subcategoria=Subcategoria.objects.get(nombre="Ordenadores"), direccion="Avenida PC 12")

    print("Datos de ejemplo cargados con éxito.")

# Ejecutar la función de carga de datos
cargar_datos()
