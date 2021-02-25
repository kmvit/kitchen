from django.db import models
from ckeditor.fields import RichTextField



class Status(models.Model):
	title = models.CharField(max_length=50, verbose_name='Название')
	class Meta:
		verbose_name = 'Статус'
		verbose_name_plural = 'Статусы для лидов'

	def __str__(self):
		return self.title

class Lead(models.Model):
	name = models.CharField(max_length=100, blank=True, verbose_name='Имя')
	email = models.EmailField(verbose_name='Почта', blank=True)
	phone = models.CharField(max_length=15, blank=True, verbose_name='Телефон')
	status = models.ForeignKey(Status, default=1, on_delete=models.SET_NULL, null=True, verbose_name='Статус')
	description = RichTextField(verbose_name='Описание', blank=True)

	class Meta:
		verbose_name = 'Лид'
		verbose_name_plural = 'Лиды'

	def __str__(self):
		return self.name + ' ' + self.status.title



