# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srm', '0009_auto_20170727_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='phone',
            field=models.CharField(default='1', max_length=13, verbose_name='Телефон'),
        ),
    ]