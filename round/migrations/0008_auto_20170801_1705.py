# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('round', '0007_auto_20170727_1416'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='round',
            options={'verbose_name': 'Runda'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': 'Lag'},
        ),
        migrations.AlterField(
            model_name='scoreline',
            name='hole',
            field=models.IntegerField(verbose_name='Hål'),
        ),
        migrations.AlterField(
            model_name='scoreline',
            name='strokes',
            field=models.IntegerField(blank=True, null=True, verbose_name='Antal slag'),
        ),
    ]
