# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 11:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('acopio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=20)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=20)),
                ('acopio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acopio.Acopio')),
            ],
            options={
                'verbose_name': 'Balance',
                'verbose_name_plural': 'Balance',
            },
        ),
        migrations.CreateModel(
            name='CajaEgreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('num_comprobante', models.CharField(blank=True, max_length=50)),
                ('acopio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acopio.Acopio')),
            ],
            options={
                'verbose_name': 'CajaEgreso',
                'verbose_name_plural': 'CajaEgresos',
            },
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto_ingreso', models.DecimalField(decimal_places=2, max_digits=20)),
                ('tipo_cargo', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='DetalleCaja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=20)),
                ('descripcion', models.CharField(blank=True, max_length=50)),
                ('precio_uni', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Precio Unitario')),
                ('total_egreso', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Precio a Pagar')),
            ],
            options={
                'verbose_name': 'DetalleCaja',
                'verbose_name_plural': 'Detalles Caja',
            },
        ),
        migrations.AddField(
            model_name='balance',
            name='cargo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kaja.Cargo'),
        ),
    ]
