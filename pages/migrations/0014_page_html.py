# Generated by Django 3.1.6 on 2021-07-14 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_auto_20210228_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='html',
            field=models.TextField(blank=True, null=True, verbose_name='Html код'),
        ),
    ]
