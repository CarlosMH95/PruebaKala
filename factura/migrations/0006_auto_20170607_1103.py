# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0005_auto_20170606_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturas',
            name='subtotal',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='facturas',
            name='total',
            field=models.FloatField(),
        ),
    ]
