# Generated by Django 3.1.6 on 2021-11-02 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_page_html'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='portfolio',
            field=models.CharField(choices=[('visitka', 'Многостраничник'), ('shop', 'Интернет-магазин'), ('landing', 'Лэндинг')], default=1, max_length=50, verbose_name='Какую категорию работ выводить'),
        ),
    ]
