# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-16 10:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
        ('personal', '0001_initial'),
        ('fisioterapia', '0009_remove_ficha_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='creado')),
                ('actualizado', models.DateTimeField(auto_now=True, verbose_name='actualizado')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('detalle', models.CharField(max_length=200)),
                ('estado', models.CharField(choices=[('1', 'No tomada'), ('2', 'Finalizada')], default='1', max_length=200)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='paciente.Paciente')),
                ('personal', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='personal.Personal')),
            ],
            options={
                'db_table': 'horario_fis',
            },
        ),
    ]
