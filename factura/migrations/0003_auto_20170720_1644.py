# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-20 21:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0002_auto_20170720_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturas',
            name='serie',
            field=models.CharField(default='', max_length=25, unique=True),
        ),
    ]
