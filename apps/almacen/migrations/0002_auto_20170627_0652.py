# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 11:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='Igv',
            new_name='igv',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='PecioVenta',
            new_name='precioVenta',
        ),
    ]
