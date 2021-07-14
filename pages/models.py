from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

from portfolio.models import WORK_CATEGORY

TEMPLATES = (
	('page.html', 'page.html'),
	('home.html', 'home.html'),
	('reklama.html', 'reklama.html'),
	('seo.html', 'seo.html'),
	('develop.html', 'develop.html'),
	('just-text.html', 'just-text.html'),
)


class BasePage(models.Model):
	title = models.CharField(max_length=200, verbose_name='Название')
	slug = models.SlugField(unique=True, verbose_name='Дружественный URL')
	meta_title = models.TextField(blank=True, null=True, verbose_name='Meta Title')
	meta_description = models.TextField(blank=True, null=True, verbose_name='Meta Description')
	preview_image = models.FileField(upload_to='preview', blank=True, null=True)
	is_home_page = models.BooleanField(default=False, verbose_name='Назначить главной страницей')



class Page(BasePage):
	html = models.TextField(blank=True, null=True, verbose_name='Html код')
	content_one = RichTextField(blank=True, null=True, verbose_name='Для кого подойдет')
	content_two = RichTextField(blank=True, null=True, verbose_name='Что получаете при заказе')
	portfolio = models.CharField(max_length=50, choices=WORK_CATEGORY, default=1, verbose_name='Какую категорию работ выводить')
	price_base = models.CharField(max_length=100, default='10000', verbose_name='Базовая цена')
	price_pro = models.CharField(max_length=100, default='30000', verbose_name='Индивидуальная цена')
	template = models.CharField(max_length=50, choices=TEMPLATES, default=1, verbose_name='Использовать шаблон')

	class Meta:
		verbose_name = 'Страницу'
		verbose_name_plural = 'Страницы'

	def save(self, *args, **kwargs):
		if self.is_home_page == True:
			Page.objects.filter(is_home_page=True).update(is_home_page=False)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('pages:page', kwargs={'slug': self.slug})


class ContactInformation(models.Model):
	phone = models.CharField(max_length=20, verbose_name='Телефон')
	mobile_phone = models.CharField(max_length=20, verbose_name='Мобильный')
	email = models.EmailField(verbose_name='Почта')
	address = models.TextField(verbose_name='Адрес')
	instagram= models.CharField(max_length=100, blank=True, null=True, verbose_name='Инстаграмм')
	vk = models.CharField(max_length=100, blank=True, null=True, verbose_name='Вконтакте')

	class Meta:
		verbose_name = 'Контактная информация'
		verbose_name_plural = 'Информация'

	def __str__(self):
		return 'Контактная информация для отображения на сайте'



