# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-21 08:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Catalogo', '0005_auto_20170421_0225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='plazo_dias',
        ),
    ]