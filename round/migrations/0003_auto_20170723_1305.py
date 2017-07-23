# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 13:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('round', '0002_auto_20170723_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scoreline',
            name='score',
        ),
        migrations.AddField(
            model_name='score',
            name='score_line',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='round.ScoreLine'),
            preserve_default=False,
        ),
    ]
