from django.shortcuts import render
from django.views import generic
from .models import Work

class WorklistView(generic.ListView):
	template_name = 'work_list.html'
	queryset = Work.objects.all()

	def get_context_data(self, **kwargs):
		context = super(WorklistView, self).get_context_data(**kwargs)
		context['my_title'] = 'Портфолио'
		return context



class WorkDetailView(generic.DetailView):
	template_name = 'work_detail.html'
	queryset = Work.objects.all()


