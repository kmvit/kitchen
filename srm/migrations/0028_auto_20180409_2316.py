# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-09 20:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srm', '0027_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='born',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Срок завершения'),
        ),
    ]