import os
import django

#Metodo creado por IA para cargar datos de ejemplo en la base de datos despues de eliminar las migraciones

# Configuración del entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mercaelxproy.settings')
django.setup()

# Importar modelos
from core.models import Ciudad, Provincia, Distrito
from directorio_comercios.models import Asociacion, Categoria, Subcategoria, Comercio

def cargar_datos():
    # Crear provincias
    provincia1 = Provincia.objects.create(codigo="ALC", nombre="Alicante")
    provincia2 = Provincia.objects.create(codigo="VAL", nombre="Valencia")

    # Crear ciudades (5 ciudades distintas)
    ciudad1 = Ciudad.objects.create(codigo="ORI", nombre="Orihuela", provincia=provincia1)
    ciudad2 = Ciudad.objects.create(codigo="ALC", nombre="Alicante", provincia=provincia1)
    ciudad3 = Ciudad.objects.create(codigo="VAL", nombre="Valencia", provincia=provincia2)
    ciudad4 = Ciudad.objects.create(codigo="TOR", nombre="Torrent", provincia=provincia2)
    ciudad5 = Ciudad.objects.create(codigo="GAN", nombre="Gandía", provincia=provincia2)

    # Crear distritos (1 distrito por ciudad)
    Distrito.objects.create(ciudad=ciudad1, nombre="Centro")
    Distrito.objects.create(ciudad=ciudad2, nombre="Santa Cruz")
    Distrito.objects.create(ciudad=ciudad3, nombre="Ciutat Vella")
    Distrito.objects.create(ciudad=ciudad3, nombre="Carrus")
    Distrito.objects.create(ciudad=ciudad4, nombre="El Pla")
    Distrito.objects.create(ciudad=ciudad5, nombre="Marquesado")

    # Crear asociaciones (1 asociación por ciudad)
    Asociacion.objects.create(
        nombre="Asociación Comerciantes Orihuela",
        ciudad=ciudad1,
        correo_electronico="contacto@asociacionorihuela.com",
        telefono="965123456"
    )
    Asociacion.objects.create(
        nombre="Asociación Comerciantes Alicante",
        ciudad=ciudad2,
        correo_electronico="info@asociacionalicante.com",
        telefono="965654321"
    )
    Asociacion.objects.create(
        nombre="Asociación Comerciantes Valencia",
        ciudad=ciudad3,
        correo_electronico="contacto@asociacionvalencia.com",
        telefono="960987654"
    )
    Asociacion.objects.create(
        nombre="Asociación Comerciantes Torrent",
        ciudad=ciudad4,
        correo_electronico="info@asociaciontorrent.com",
        telefono="962123789"
    )
    Asociacion.objects.create(
        nombre="Asociación Comerciantes Gandía",
        ciudad=ciudad5,
        correo_electronico="contacto@asociaciongandia.com",
        telefono="962456123"
    )

    # Crear categorías (3 categorías distintas)
    categoria1 = Categoria.objects.create(codigo="ALI", nombre="Alimentos")
    categoria2 = Categoria.objects.create(codigo="ELE", nombre="Electrónica")
    categoria3 = Categoria.objects.create(codigo="ROP", nombre="Ropa")

    # Crear subcategorías (2 subcategorías por categoría)
    Subcategoria.objects.create(codigo="VER", nombre="Verduras", categoria=categoria1)
    Subcategoria.objects.create(codigo="FRU", nombre="Frutas", categoria=categoria1)
    Subcategoria.objects.create(codigo="MOV", nombre="Móviles", categoria=categoria2)
    Subcategoria.objects.create(codigo="ORD", nombre="Ordenadores", categoria=categoria2)
    Subcategoria.objects.create(codigo="CAM", nombre="Camisetas", categoria=categoria3)
    Subcategoria.objects.create(codigo="PAN", nombre="Pantalones", categoria=categoria3)

    # Crear comercios (2 comercios por ciudad, con diferentes categorías y subcategorías)
    Comercio.objects.create(nombre="Frutería La Huerta", ciudad=ciudad1, categoria=categoria1, subcategoria=Subcategoria.objects.get(nombre="Verduras"), direccion="Calle Falsa 123", codigo_postal="03300")
    Comercio.objects.create(nombre="Frutería Juan Carlos", ciudad=ciudad1, categoria=categoria1, subcategoria=Subcategoria.objects.get(nombre="Frutas"), direccion="Calle Verdadera 321", codigo_postal="03300")

    Comercio.objects.create(nombre="Electrónica Juan", ciudad=ciudad2, categoria=categoria2, subcategoria=Subcategoria.objects.get(nombre="Móviles"), direccion="Calle de la Tecnología 1", codigo_postal="03001")
    Comercio.objects.create(nombre="PC Componentes", ciudad=ciudad2, categoria=categoria2, subcategoria=Subcategoria.objects.get(nombre="Ordenadores"), direccion="Calle Ordenadores 2", codigo_postal="03002")

    Comercio.objects.create(nombre="ZARA", ciudad=ciudad3, categoria=categoria3, subcategoria=Subcategoria.objects.get(nombre="Camisetas"), direccion="Calle Juventud 3", codigo_postal="46002")
    Comercio.objects.create(nombre="Berska", ciudad=ciudad3, categoria=categoria3, subcategoria=Subcategoria.objects.get(nombre="Pantalones"), direccion="Calle Moda 4", codigo_postal="46003")

    Comercio.objects.create(nombre="Frutería La Natural", ciudad=ciudad4, categoria=categoria1, subcategoria=Subcategoria.objects.get(nombre="Verduras"), direccion="Calle Verde 56", codigo_postal="46950")
    Comercio.objects.create(nombre="Eco Market", ciudad=ciudad4, categoria=categoria1, subcategoria=Subcategoria.objects.get(nombre="Frutas"), direccion="Calle Eco 78", codigo_postal="46951")

    Comercio.objects.create(nombre="Móvil libre", ciudad=ciudad5, categoria=categoria2, subcategoria=Subcategoria.objects.get(nombre="Móviles"), direccion="Calle Gadgets 90", codigo_postal="46700")
    Comercio.objects.create(nombre="PC World", ciudad=ciudad5, categoria=categoria2, subcategoria=Subcategoria.objects.get(nombre="Ordenadores"), direccion="Avenida PC 12", codigo_postal="46701")

    print("Datos de ejemplo cargados con éxito.")

# Ejecutar la función de carga de datos
cargar_datos()
