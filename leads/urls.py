from django.views.generic import TemplateView
from django.urls import path, include
from .views import LeadCreate

app_name="lead"

urlpatterns = [
    path('create/', LeadCreate.as_view(), name='lead_create'),
    path('success/', TemplateView.as_view(template_name='success.html'),name='success' ),

]
