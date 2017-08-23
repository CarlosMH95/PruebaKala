# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutricion', '0002_horarionut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha_nutricion',
            name='carnes_input',
            field=models.CharField(choices=[('1', '4-5 veces'), ('2', '2-3 veces'), ('3', '1 vez'), ('4', 'Rara vez'), ('5', 'Nunca')], default='3', max_length=20),
        ),
        migrations.AlterField(
            model_name='ficha_nutricion',
            name='cho_input',
            field=models.CharField(choices=[('1', '4-5 veces'), ('2', '2-3 veces'), ('3', '1 vez'), ('4', 'Rara vez'), ('5', 'Nunca')], default='3', max_length=20),
        ),
        migrations.AlterField(
            model_name='ficha_nutricion',
            name='comidas_rapidas_input',
            field=models.CharField(choices=[('1', '4-5 veces'), ('2', '2-3 veces'), ('3', '1 vez'), ('4', 'Rara vez'), ('5', 'Nunca')], default='3', max_length=20),
        ),
        migrations.AlterField(
            model_name='ficha_nutricion',
            name='energizantes_input',
            field=models.CharField(choices=[('1', '4-5 veces'), ('2', '2-3 veces'), ('3', '1 vez'), ('4', 'Rara vez'), ('5', 'Nunca')], default='3', max_length=20),
        ),
        migrations.AlterField(
            model_name='ficha_nutricion',
            name='enlatados_input',
            field=models.CharField(choices=[('1', '4-5 veces'), ('2', '2-3 veces'), ('3', '1 vez'), ('4', 'Rara vez'), ('5', 'Nunca')], default='3', max_length=20),
        ),
        migrations.AlterField(
            model_name='ficha_nutricion',
            name='frituras_input',
            field=models.CharField(choices=[('1', '4-5 veces'), ('2', '2-3 veces'), ('3', '1 vez'), ('4', 'Rara vez'), ('5', 'Nunca')], default='3', max_length=20),
        ),
        migrations.AlterField(
            model_name='ficha_nutricion',
            name='frutas_input',
            field=models.CharField(choices=[('1', '4-5 veces'), ('2', '2-3 veces'), ('3', '1 vez'), ('4', 'Rara vez'), ('5', 'Nunca')], default='3', max_length=20),
        ),
        migrations.AlterField(
            model_name='ficha_nutricion',
            name='gaseosas_input',
            field=models.CharField(choices=[('1', '4-5 veces'), ('2', '2-3 veces'), ('3', '1 vez'), ('4', 'Rara vez'), ('5', 'Nunca')], default='3', max_length=20),
        ),
        migrations.AlterField(
            model_name='ficha_nutricion',
            name='infusiones_input',
            field=models.CharField(choices=[('1', '4-5 veces'), ('2', '2-3 veces'), ('3', '1 vez'), ('4', 'Rara vez'), ('5', 'Nunca')], default='3', max_length=20),
        ),
        migrations.AlterField(
            model_name='ficha_nutricion',
            name='lacteos_input',
            field=models.CharField(choices=[('1', '4-5 veces'), ('2', '2-3 veces'), ('3', '1 vez'), ('4', 'Rara vez'), ('5', 'Nunca')], default='3', max_length=20),
        ),
        migrations.AlterField(
            model_name='ficha_nutricion',
            name='vegetales_input',
            field=models.CharField(choices=[('1', '4-5 veces'), ('2', '2-3 veces'), ('3', '1 vez'), ('4', 'Rara vez'), ('5', 'Nunca')], default='3', max_length=20),
        ),
    ]
