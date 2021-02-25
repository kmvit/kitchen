from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

WORK_CATEGORY = (
	('visitka','Сайт визитка'),
	('coop','Корпоративный сайт'),
	('shop','Интернет-магазин'),
	('landing','Лэндинг'),
)

class Work(models.Model):
	title = models.CharField(max_length=100, verbose_name='Название')
	slug = models.SlugField(unique=True, verbose_name='Дружественный URL')
	meta_description = models.TextField(verbose_name='Мета описание')
	preview_image = models.FileField(upload_to='preview', verbose_name='Превью')
	image = models.FileField(upload_to='portfolio', verbose_name='Изображение большое')
	content = RichTextField(verbose_name='Описание')
	link_to_site = models.CharField(max_length=100, blank=True, verbose_name='Ссылка на сайт')
	category = models.CharField(max_length=50, choices=WORK_CATEGORY, default=1, blank=True, verbose_name='Категория сайта')

	class Meta:
		verbose_name = 'Работу'
		verbose_name_plural = 'Портфолио'


	def __str__(self):
		return self.title


