# Generated by Django 4.2 on 2024-11-13 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ciudad',
            options={'ordering': ['nombre'], 'verbose_name': 'Ciudad', 'verbose_name_plural': 'Ciudades'},
        ),
        migrations.AlterModelOptions(
            name='distrito',
            options={'ordering': ['ciudad__codigo', 'nombre'], 'verbose_name': 'Distrito', 'verbose_name_plural': 'Distritos'},
        ),
        migrations.AlterModelOptions(
            name='provincia',
            options={'ordering': ['nombre'], 'verbose_name': 'Provincia', 'verbose_name_plural': 'Provincias'},
        ),
        migrations.AlterField(
            model_name='provincia',
            name='nombre',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
