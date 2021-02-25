from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
	title = models.CharField(max_length=150, verbose_name='Название')
	slug = models.SlugField(unique=True, verbose_name='Дружественный URL')

	class Meta:
		verbose_name = 'Категорию'
		verbose_name_plural = 'Категории статей'

	def __str__(self):
		return self.title

class Blog(models.Model):
	title = models.CharField(max_length=150, verbose_name='Название')
	meta_title = models.TextField(blank=True, null=True, verbose_name='Meta Title')
	meta_description = models.TextField(blank=True, null=True, verbose_name='Meta Description')
	slug = models.SlugField(unique=True, verbose_name='Дружественный URL')
	preview_image = models.FileField(upload_to='blog_preview', verbose_name='Изображение превью')
	image = models.FileField(upload_to='blog', verbose_name='Изображение в статье')
	date_born = models.DateField(verbose_name='Дата создания')
	description = models.TextField(blank=True, null=True, verbose_name='Краткое описание')
	content = RichTextField(verbose_name='Текст статьи')
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Категория статьи')

	class Meta:
		verbose_name = 'Статью'
		verbose_name_plural = 'Статьи'

	def __str__(self):
		return self.title


