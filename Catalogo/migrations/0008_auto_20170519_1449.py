# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 12:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Catalogo', '0007_categoria_plazo_dias'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrera', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='copialibro',
            name='prestado',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perfil',
            name='carrera',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Catalogo.Carrera'),
            preserve_default=False,
        ),
    ]