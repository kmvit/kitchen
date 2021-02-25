from django.shortcuts import render
from django.views import generic
from .models import Work

class WorklistView(generic.ListView):
	template_name = 'work_list.html'
	queryset = Work.objects.all()


class WorkDetailView(generic.DetailView):
	template_name = 'work_detail.html'
	queryset = Work.objects.all()


