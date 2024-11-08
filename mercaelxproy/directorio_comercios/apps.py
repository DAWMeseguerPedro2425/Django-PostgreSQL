from django.apps import AppConfig


class DirectorioComerciosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'directorio_comercios'
    #--------UD6.3.d--------
    #Se cambia el nombre de la aplicación en el panel de administración
    verbose_name = 'Directorio de Comercios'
