from django.core.validators import RegexValidator
from django.db import models
from django.db.models import Sum
from datetime import datetime
import os

# Create your models here.

class Stage(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    label = models.CharField(max_length=300, verbose_name='Цвет', default='label-default')
    class Meta:
        verbose_name = 'Этап'
        verbose_name_plural = 'Этапы'
    def __str__(self):
        return self.title

class City(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    regex = RegexValidator(regex=r'^7\d{10}$',
                           message="Номер клиента в формате 7XXXXXXXXXX (X - номер от 0 до 9)")
    phone = models.CharField(max_length=11, blank=True, validators=[regex], verbose_name='Номер телефона')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')
    email = models.EmailField(blank=True, verbose_name='Почта')
    company = models.CharField(max_length=200, blank=True, verbose_name='Компания')
    site = models.CharField(max_length=200, blank=True, verbose_name='Сайт')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.name

class KindofWork(models.Model):
    title = models.CharField(max_length=300)

    class Meta:
        verbose_name = 'Вид работы'
        verbose_name_plural = 'Выди работы'

    def __str__(self):
        return self.title



class Deal(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    kindofwork = models.ForeignKey(KindofWork, on_delete=models.CASCADE, verbose_name='Что делаем?')
    born = models.DateField(verbose_name='Дата', default=datetime.now)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, verbose_name='Контакт')
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, verbose_name='Этап')
    prepayment = models.IntegerField(verbose_name='Предоплата', blank=True, null=True)
    budget = models.IntegerField(verbose_name='Бюджет')
    description = models.TextField(verbose_name='Примечания', blank=True)
    archive = models.BooleanField(default=False, verbose_name="В архив")


    class Meta:
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'
        ordering = ['-born']
    def __str__(self):
        return self.title

    def remainder(self):
        try:
            return self.budget - self.prepayment
        except:
            return self.budget
    remainder.short_description = 'Остаток'


class DealFile(models.Model):
    file = models.FileField(upload_to='deal_file')
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE, blank=True)

    def __str__(self):
       return self.file.name

class Task(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE, verbose_name='Сделка')
    born = models.DateField(verbose_name='Срок завершения', default=datetime.now)
    content = models.TextField(verbose_name='Содержание', blank=True)
    finish = models.BooleanField(verbose_name='Завершено', default=False)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['born']
    def __str__(self):
        return self.title

class Costs(models.Model):
    title = models.CharField(max_length=300, verbose_name='Статья расхода')
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE, verbose_name="Сделка")
    born = models.DateField(verbose_name='Когда', default=datetime.now)
    price = models.IntegerField(verbose_name="Сумма")
    class Meta:
        verbose_name = 'Расходы'
        verbose_name_plural = 'Расходы'
    def __str__(self):
        return self.title
