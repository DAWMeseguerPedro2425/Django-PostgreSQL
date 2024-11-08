from django.db import models

# Create your models here.
from django.core.validators import RegexValidator

#--------UD6.3.a--------
#Se crea el modelo Asociacion con los campos nombre, dirección, ciudad, correo electrónico y teléfono
class Asociacion(models.Model):
    nombre = models.CharField(max_length=256, unique=True)
    direccion = models.TextField(blank=True, null=True)
    ciudad = models.ForeignKey('core.Ciudad', on_delete=models.PROTECT)
    correo_electronico = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=15,blank=True,null=True,
        validators=[RegexValidator(regex=r'^\+?\d{9,15}$')] # Expresion regular para validar el teléfono
    )

    #--------UD6.3.b--------
    # el metodo __str__ devuelve una cadena de texto con el nombre de la asociación
    def __str__(self):
        return f"{self.ciudad.provincia.codigo}. {self.nombre}"

    #--------UD6.3.c-UD6.4.e-UD6.4.f--------
    #Restricción de asociaciones únicas por ciudad y nombre
    #Nombre en singular y plural y ordenar por ciudad y nombre
    class Meta:
        unique_together = ('ciudad', 'nombre')
        verbose_name = 'Asociación'
        verbose_name_plural = 'Asociaciones'
        ordering = ['ciudad__codigo', 'nombre']

#--------UD6.3.a--------
#Se crea el modelo Categoria con los campos código y nombre
class Categoria(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=256, unique=True)

    #--------UD6.3.b--------
    # el metodo __str__ devuelve una cadena de texto con el código y el nombre de la categoría
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

#--------UD6.3.a--------
#Se crea el modelo Subcategoria con los campos código, nombre y categoría
class Subcategoria(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=256)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    #--------UD6.3.b--------
    # el metodo __str__ devuelve una cadena de texto con el código, el nombre y la categoría
    def __str__(self):
        return f"{self.categoria.codigo}.{self.codigo}. {self.nombre}"

    #--------UD6.3.c-UD6.4.e-UD6.4.f--------
    #Restricción de categoria única por nombre
    #Nombre en singular y plural y orden por codigo
    class Meta:
        unique_together = ('categoria', 'nombre')
        verbose_name = 'Subcategoría'
        verbose_name_plural = 'Subcategorías'
        ordering = ['codigo']

#--------UD6.3.a--------
#Se crea el modelo Comercio con los campos nombre, código postal, dirección, 
# ciudad, categoría, subcategoría, asociación, correo electrónico y teléfono
class Comercio(models.Model):
    nombre = models.CharField(max_length=256, unique=True)
    codigo_postal = models.CharField(max_length=5)
    direccion = models.TextField()
    ciudad = models.ForeignKey('core.Ciudad', on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.PROTECT, blank=True, null=True)
    asociacion = models.ForeignKey(Asociacion, on_delete=models.PROTECT, blank=True, null=True)
    correo_electronico = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True,
        validators=[RegexValidator(regex=r'^\+?\d{9,15}$')]# Expresion regular para validar el teléfono copilot
    )

    #--------UD6.3.b--------
    # el metodo __str__ devuelve una cadena de texto con el código, el nombre y la categoría y si tiene subcategoría la añade
    def __str__(self):
        if self.subcategoria:
            return f"{self.categoria.codigo}.{self.subcategoria.codigo} - {self.nombre}"
        return f"{self.categoria.codigo} - {self.nombre}"

    #--------UD6.3.c-UD6.4.e-UD6.4.f--------
    #Restricción de comercios únicos por ciudad
    class Meta:
        unique_together = ('ciudad', 'nombre')
        verbose_name = 'Comercio'
        verbose_name_plural = 'Comercios'
        ordering = ['ciudad__codigo', 'nombre']