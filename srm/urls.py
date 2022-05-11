from django.urls import path

from .views import *
from django.conf.urls import url
app_name = 'srm'

urlpatterns = [
   path('', srm_home, name='srm_home'),

   path('tasks/', TaskList.as_view(), name='task_list'),
   path('task/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
   path('task/add/', TaskAddAll.as_view(), name='task_add_all'),
   path('task/<deal_id>/add/', TaskAdd.as_view(), name='task_add'),
   path('task/<int:pk>/edit', TaskEdit.as_view(), name='task_edit'),
   path('task/<int:pk>/delete', TaskDelete.as_view(), name='task_delete'),

   path('costs/<int:deal_id>/add/', CostsAdd.as_view(), name='costs_add'),
   path('costs/<int:pk>/edit', CostsEdit.as_view(), name='costs_edit'),
   path('costs/<int:pk>/delete', CostsDelete.as_view(), name='costs_delete'),

   path('contacts/', ContactList.as_view(), name='contact_list'),
   path('contact/add/', ContactAdd.as_view(), name='contact_add'),
   path('contact/<int:pk>/', ContactDetail.as_view(), name='contact_detail'),
   path('contact/<int:pk>/edit', ContactEdit.as_view(), name='contact_edit'),
   path('contact/<int:pk>/delete', ContactDelete.as_view(), name='contact_delete'),

   path('orders/', OrderList.as_view(), name='order_list'),
   path('archive/orders', ArchiveOrderList.as_view(), name='archive_order_list'),
   path('<int:pk>/', OrderDetail.as_view(), name='order_detail'),
   path('add/', OrderAdd.as_view(), name='order_add'),
   path('<int:pk>/edit', OrderEdit.as_view(), name='order_edit'),
   path('<int:pk>/delete', OrderDelete.as_view(), name='order_delete'),
   path('filter/', order_filter, name='order_filter'),
]
