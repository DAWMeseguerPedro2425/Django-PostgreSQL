from django.db import models
#-----UD9.4-----
# Modelo abstracto Persona
class Persona(models.Model):
    nombre = models.CharField(max_length=128)
    apellidos = models.CharField(max_length=256)

    class Meta:
        abstract = True

        
#-----UD9.4-----
# Modelo abstracto Localizacion
class Localizacion(models.Model):
    direccion = models.CharField(max_length=256)
    codigo_postal = models.CharField(max_length=5)
    ciudad = models.CharField(max_length=256)

    class Meta:
        abstract = True
