# Generated by Django 3.1.6 on 2021-11-11 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20211102_2213'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='work',
            options={'ordering': ['-pk'], 'verbose_name': 'Работу', 'verbose_name_plural': 'Портфолио'},
        ),
    ]