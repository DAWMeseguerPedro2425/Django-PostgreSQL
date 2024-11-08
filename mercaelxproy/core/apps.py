from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    #--------UD6.3.d--------
    #Se cambia el nombre de la aplicación en el panel de administración
    verbose_name = 'Core'