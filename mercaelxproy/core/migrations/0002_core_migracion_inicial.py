from django.db import migrations
#-----UD9.3.a-----
#Archivo de migración que carga datos iniciales en la base de datos de core
def create_initial_data(apps, schema_editor):
    Provincia = apps.get_model('core', 'Provincia')
    Ciudad = apps.get_model('core', 'Ciudad')
    Distrito = apps.get_model('core', 'Distrito')

    provincia1 = Provincia.objects.create(codigo="ALC", nombre="Alicante")
    provincia2 = Provincia.objects.create(codigo="VAL", nombre="Valencia")

    ciudad1 = Ciudad.objects.create(codigo="ORI", nombre="Orihuela", provincia=provincia1)
    ciudad2 = Ciudad.objects.create(codigo="ALC", nombre="Alicante", provincia=provincia1)
    ciudad3 = Ciudad.objects.create(codigo="VAL", nombre="Valencia", provincia=provincia2)
    ciudad4 = Ciudad.objects.create(codigo="TOR", nombre="Torrent", provincia=provincia2)
    ciudad5 = Ciudad.objects.create(codigo="GAN", nombre="Gandía", provincia=provincia2)

    Distrito.objects.create(ciudad=ciudad1, nombre="Centro")
    Distrito.objects.create(ciudad=ciudad2, nombre="Santa Cruz")
    Distrito.objects.create(ciudad=ciudad3, nombre="Ciutat Vella")
    Distrito.objects.create(ciudad=ciudad3, nombre="Carrus")
    Distrito.objects.create(ciudad=ciudad4, nombre="El Pla")
    Distrito.objects.create(ciudad=ciudad5, nombre="Marquesado")

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_data),
    ]