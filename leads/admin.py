from django.contrib import admin
from .models import *

class LeadAdmin(admin.ModelAdmin):
	list_display = ('name', 'date_born', 'status', 'date_update')

admin.site.register(Status)
admin.site.register(Lead, LeadAdmin)


