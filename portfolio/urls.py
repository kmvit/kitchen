from django.urls import path
from .views import WorklistView, WorkDetailView


app_name='portfolio'

urlpatterns = [
    path('', WorklistView.as_view(), name='work_list'),
    path('<slug>/', WorkDetailView.as_view(), name='work_detail'),
    ]
