from django.db import models

# Create your models here.
#--------UD6.3.a--------
#Se crea el modelo Provincia con los campos codigo y nombre
class Provincia(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=255, unique=True)
    #--------UD6.3.b--------
    #El método __str__ devuelve una cadena con el código y el nombre de la provincia 100 caracteres
    def __str__(self):
        return f"{self.codigo}. {self.nombre[:100]}"
    
    #--------UD6.4.e-UD6.4.f--------
    #Nombre en singular y plural y ordenar por nombre
    class Meta:
        verbose_name = 'Provincia' # Nombre en singular
        verbose_name_plural = 'Provincias' # Nombre en plural
        ordering = ['nombre'] # Ordenar por nombre
        



#--------UD6.3.a--------
#Se crea el modelo Ciudad con los campos codigo, nombre y provincia
class Ciudad(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=256, unique=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT)

    #--------UD6.3.b--------
    #El método __str__ devuelve una cadena con el código y el nombre de la ciudad
    def __str__(self):
        return f"{self.provincia.codigo}.{self.nombre[:100]}"
    
    #--------UD6.4.e-UD6.4.f--------
    #Nombre en singular y plural y ordenar por nombre
    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        ordering = ['nombre']

#--------UD6.3.a--------
#Se crea el modelo Distrito con los campos nombre y ciudad
class Distrito(models.Model):
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=256)

    #--------UD6.3.b--------
    #El método __str__ devuelve el código de la provincia, el nombre de la ciudad y el nombre del distrito
    def __str__(self):
        return f"{self.ciudad.provincia.codigo}.{str(self.ciudad)}.{self.nombre[:100]}"

    #--------UD6.3.c-UD6.4.e-UD6.4.f--------
    #Restricción de distritos únicos por ciudad y nombre
    #Nombre en singular y plural y ordenar por ciudad y nombre 
    class Meta:
        verbose_name = 'Distrito'
        verbose_name_plural = 'Distritos'
        unique_together = ('ciudad', 'nombre')
        ordering = ['ciudad__codigo', 'nombre']