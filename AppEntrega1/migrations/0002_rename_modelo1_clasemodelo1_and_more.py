# Generated by Django 4.1 on 2022-09-03 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppEntrega1', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Modelo1',
            new_name='ClaseModelo1',
        ),
        migrations.RenameModel(
            old_name='Modelo2',
            new_name='ClaseModelo2',
        ),
        migrations.RenameModel(
            old_name='Modelo3',
            new_name='ClaseModelo3',
        ),
        migrations.RenameField(
            model_name='clasemodelo2',
            old_name='Apellido',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='clasemodelo3',
            old_name='Apellido',
            new_name='apellido',
        ),
    ]