# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-23 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutricion', '0003_auto_20170821_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='horarionut',
            name='duracion',
            field=models.PositiveSmallIntegerField(default=10),
        ),
    ]
