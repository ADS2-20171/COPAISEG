# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Firs Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('identity_type', models.CharField(choices=[('DNI', 'DNI'), ('FC', 'Canet de Extranjería'), ('OTROS', 'Otros')], default='DNI', max_length=15)),
                ('identity_num', models.CharField(error_messages={'unique': 'eeeee ee'}, max_length=20)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='persons')),
                ('email', models.EmailField(max_length=254)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
            },
        ),
    ]
