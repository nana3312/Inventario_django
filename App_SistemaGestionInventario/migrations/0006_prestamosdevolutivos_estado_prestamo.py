# Generated by Django 3.0.3 on 2023-12-03 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_SistemaGestionInventario', '0005_materiales_observaciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamosdevolutivos',
            name='estado_prestamo',
            field=models.BooleanField(default=False),
        ),
    ]
