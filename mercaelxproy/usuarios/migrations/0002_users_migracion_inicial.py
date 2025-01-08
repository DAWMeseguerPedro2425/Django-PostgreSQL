from django.db import migrations
#-----UD9.3.c-----
#Archivo de migración que crea un usuario administrador en la base de datos de usuarios
def create_admin_user(apps, schema_editor):
    MyUser = apps.get_model('usuarios', 'MyUser')
    MyUser.objects.create(
        username='admin',
        email='admin@example.com',
        password='admin',
        is_superuser=True,
        is_staff=True,
        is_active=True
    )

class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_admin_user),
    ]