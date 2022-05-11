from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div
from django.forms import ModelForm
from django import forms
from .models import *

class OrderAddForm(ModelForm):
    class Meta:
        model = Deal
        fields='__all__'
        exclude = ['status', 'start']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                'title',
                'kindofwork',
                'born',
                'contact',
                'stage',
                css_class='col-md-6 form-group'

            ),
            Div(
                'description',
                'prepayment',
                'budget',
                'archive',
                css_class='col-md-6 form-group'
            ),

            ButtonHolder(
                Submit('submit', 'обавить', css_class='button white')
            )
        )

class OrderEditForm(ModelForm):
    class Meta:
        model = Deal
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                'title',
                'kindofwork',
                'born',
                'contact',
                'stage',
                css_class='col-md-6 form-group'

            ),
            Div(
                'description',
                'prepayment',
                'budget',
                'archive',
                css_class='col-md-6 form-group'
            ),

            ButtonHolder(
                Submit('submit', 'Изменить', css_class='button white')
            )
        )


class OrderFile(ModelForm):
    class Meta:
        model = DealFile
        fields='__all__'
        exclude=['deal']

class ContactAddForm(ModelForm):
    class Meta:
        model = Contact
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Сначала добавляем контакт потом сделку',
                'name',
                'phone',
                'city',
                'email',
                'company',
                'site',

            ),

            ButtonHolder(
                Submit('submit', 'Добавить', css_class='button white')
            )
        )

class ContactEditForm(ModelForm):
    class Meta:
        model = Contact
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                'name',
                'phone',
                'city',
                css_class='col-md-6 form-group'

            ),
            Div(
                'email',
                'company',
                'site',
                css_class='col-md-6 form-group'
            ),

            ButtonHolder(
                Submit('submit', 'Изменить', css_class='button white')
            )
        )

class TaskAddForm(ModelForm):
    class Meta:
        model = Task
        fields='__all__'
        exclude = ['status','deal']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                'title',
                'deal',
                'born',
                css_class='col-md-6 form-group'

            ),
            Div(
                'content',
                'finish',
                css_class='col-md-6 form-group'
            ),

            ButtonHolder(
                Submit('submit', 'Добавить', css_class='button white')
            )
        )

class TaskAddAllForm(ModelForm):
    class Meta:
        model = Task
        fields='__all__'
        exclude = ['status']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['deal'].queryset = Deal.objects.filter(archive=False)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                'title',
                'deal',
                'born',
                css_class='col-md-6 form-group'

            ),
            Div(
                'content',
                'finish',
                css_class='col-md-6 form-group'
            ),

            ButtonHolder(
                Submit('submit', 'Добавить', css_class='button white')
            )
        )


class CostsForm(ModelForm):
    class Meta:
        model = Costs
        fields='__all__'
        exclude = ['deal']
