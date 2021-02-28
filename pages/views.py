from django.shortcuts import render
from django.views import generic
from .models import Page
from portfolio.models import Work
from blog.models import Blog
from django.contrib.sitemaps import Sitemap


class HomePage(generic.DetailView):
	template_name = 'pages/home.html'
	queryset = Page.objects.all()

	def get_object(self, queryset=None):
		return self.queryset.get(is_home_page=True)


	def get_context_data(self, **kwargs):
		context = super(HomePage, self).get_context_data(**kwargs)
		context['work_list'] = Work.objects.all()[:6]
		context['blog_list'] =Blog.objects.all()
		return context


class PageView(generic.DetailView):
	queryset = Page.objects.all()

	def get_template_names(self):
		return 'pages/' + self.object.template

	def get_context_data(self, **kwargs):
		context = super(PageView, self).get_context_data(**kwargs)
		context['work_list'] = Work.objects.filter(category=self.object.portfolio)[:3]
		return context


class ContactView(generic.DetailView):
	template_name = 'pages/contact.html'

	def get_object(self, queryset=None):
		return Page.objects.get(slug='contact')



class PageSiteMap(Sitemap):
	changefreq = "never"
	priority = 0.5

	def items(self):
		return Page.objects.all()
