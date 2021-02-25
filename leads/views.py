from django.shortcuts import render, reverse
from .models import Lead
from .forms import LeadForm
from django.views import generic

class LeadCreate(generic.CreateView):
	template_name = 'lead_create.html'
	form_class = LeadForm

	def get_success_url(self):
		return reverse('lead:success')

