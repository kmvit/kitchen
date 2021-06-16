from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from .models import Lead
from .forms import LeadForm
from django.views import generic
from django.core.mail import send_mail

class LeadCreate(generic.CreateView):
	template_name = 'lead_create.html'
	form_class = LeadForm
	model = Lead

	def form_valid(self, form):
		send_mail(
			'Заявка с сайта',
			'Зайдите в админку и проверьте лиды!',
			'info@kmv-it.ru',
			['manager@kmv-it.ru'],
			fail_silently=False
		)



		return super(LeadCreate, self).form_valid(form)

	def get_success_url(self):
		return reverse('lead:success')

