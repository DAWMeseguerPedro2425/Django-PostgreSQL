# Generated by Django 5.1.3 on 2024-12-02 16:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Asociacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256, unique=True)),
                ('direccion', models.TextField(blank=True, null=True)),
                ('correo_electronico', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.ciudad')),
            ],
            options={
                'verbose_name': 'Asociación',
                'verbose_name_plural': 'Asociaciones',
                'ordering': ['ciudad__codigo', 'nombre'],
                'unique_together': {('ciudad', 'nombre')},
            },
        ),
        migrations.CreateModel(
            name='Subcategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=256)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='directorio_comercios.categoria')),
            ],
            options={
                'verbose_name': 'Subcategoría',
                'verbose_name_plural': 'Subcategorías',
                'ordering': ['codigo'],
                'unique_together': {('categoria', 'nombre')},
            },
        ),
        migrations.CreateModel(
            name='Comercio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256, unique=True)),
                ('codigo_postal', models.CharField(max_length=5)),
                ('direccion', models.TextField()),
                ('correo_electronico', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('asociacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='directorio_comercios.asociacion')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='directorio_comercios.categoria')),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.ciudad')),
                ('subcategoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='directorio_comercios.subcategoria')),
            ],
            options={
                'verbose_name': 'Comercio',
                'verbose_name_plural': 'Comercios',
                'ordering': ['ciudad__codigo', 'nombre'],
                'unique_together': {('ciudad', 'nombre')},
            },
        ),
    ]
