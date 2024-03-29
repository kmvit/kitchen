# Generated by Django 3.1.6 on 2022-05-11 18:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('srm', '0030_deal_archive'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterModelOptions(
            name='kindofwork',
            options={'verbose_name': 'Вид работы', 'verbose_name_plural': 'Выди работы'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='srm.city', verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='company',
            field=models.CharField(blank=True, max_length=200, verbose_name='Компания'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=11, validators=[django.core.validators.RegexValidator(message='Номер клиента в формате 7XXXXXXXXXX (X - номер от 0 до 9)', regex='^7\\d{10}$')], verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='site',
            field=models.CharField(blank=True, max_length=200, verbose_name='Сайт'),
        ),
        migrations.AlterField(
            model_name='deal',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='srm.contact', verbose_name='Контакт'),
        ),
        migrations.AlterField(
            model_name='deal',
            name='kindofwork',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='srm.kindofwork', verbose_name='Что делаем?'),
        ),
        migrations.AlterField(
            model_name='task',
            name='deal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='srm.deal', verbose_name='Сделка'),
        ),
    ]
