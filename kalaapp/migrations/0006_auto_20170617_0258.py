# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-17 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalaapp', '0005_auto_20170614_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(blank=True, default='usuario/noimagen.jpeg', help_text='Foto', null=True, upload_to='usuario/'),
        ),
    ]
