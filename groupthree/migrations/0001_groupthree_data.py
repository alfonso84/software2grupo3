# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from groupthree import models

def insert_data_default(apps, schema_editor):
    Juego = apps.get_model('groupthree', 'Juego')
    Juego.objects.create(
        juego_id=1,
        juego='Polla'
    )
    Sala = apps.get_model('groupthree', 'Sala')
    Sala.objects.create(
        sala_id = 1,
        juego_id=1,
        capacidad_maxima=10,
        cantidad_usuarios = 0,
        es_publica = True
    )

def delete_data_default(apps, schema_editor):
    Juego = apps.get_model('groupthree', 'Juego')
    Juego = Juego.objects.get(
        juego_id=1
    )
    Juego.delete()
    Sala = apps.get_model('groupthree', 'Sala')
    Sala = Sala.objects.get(
        sala_id=1
    )
    Sala.delete()


class Migration(migrations.Migration):
    dependencies = [
        ('groupthree', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(insert_data_default, delete_data_default)
    ]
