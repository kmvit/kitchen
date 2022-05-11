from django.forms import ModelForm
from django import forms
from .models import *

class OrderAddForm(ModelForm):
    class Meta:
        model = Deal
        fields='__all__'
        exclude = ['status', 'start']

class OrderEditForm(ModelForm):
    class Meta:
        model = Deal
        fields='__all__'


class OrderFile(ModelForm):
    class Meta:
        model = DealFile
        fields='__all__'
        exclude=['deal']

class ContactAddForm(ModelForm):
    class Meta:
        model = Contact
        fields='__all__'

class ContactEditForm(ModelForm):
    class Meta:
        model = Contact
        fields='__all__'

class TaskAddForm(ModelForm):
    class Meta:
        model = Task
        fields='__all__'
        exclude = ['status','deal']

class TaskAddAllForm(ModelForm):
    class Meta:
        model = Task
        fields='__all__'
        exclude = ['status']

    def __init__(self, *args, **kwargs):
        super(TaskAddAllForm, self).__init__(*args, **kwargs)
        self.fields['deal'].queryset = Deal.objects.filter(archive=False)


class CostsForm(ModelForm):
    class Meta:
        model = Costs
        fields='__all__'
        exclude = ['deal']
