# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-12 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srm', '0016_auto_20180312_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='company',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]