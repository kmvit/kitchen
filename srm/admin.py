from django.contrib import admin
from .models import *
# Register your models here.

class AdminDealFile(admin.TabularInline):
    model = DealFile
    extra = 0

class DealAdmin(admin.ModelAdmin):
    list_display=['title','contact','born', 'prepayment', 'budget']
    date_hierarchy = 'born'
    list_filter = ['stage','contact' ]
    inlines = [AdminDealFile]

admin.site.register(DealFile)
admin.site.register(Contact)
admin.site.register(KindofWork)
admin.site.register(City)
admin.site.register(Stage)
admin.site.register(Deal,DealAdmin)
admin.site.register(Task)
admin.site.register(Costs)
