# Generated by Django 3.1.6 on 2021-02-12 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name': 'Страницу', 'verbose_name_plural': 'Страницы'},
        ),
        migrations.AlterField(
            model_name='basepage',
            name='preview_image',
            field=models.FileField(blank=True, null=True, upload_to='preview'),
        ),
    ]
