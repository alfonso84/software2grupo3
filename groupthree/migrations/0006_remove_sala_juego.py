# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-30 06:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groupthree', '0005_auto_20180130_0609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sala',
            name='juego',
        ),
    ]
