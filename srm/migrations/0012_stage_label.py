# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-19 01:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srm', '0011_auto_20170727_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='label',
            field=models.CharField(default='label-default', max_length=300, verbose_name='Цвет'),
        ),
    ]
