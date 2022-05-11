from django import template
from srm.models import Task
from datetime import datetime

register = template.Library()
@register.inclusion_tag('srm/task_notification.html', takes_context=True)
def task_notification(context):
    request = context['request']
    task_note =  Task.objects.filter(finish=False, born__lte=datetime.today().date())
    task_count =  task_note.count()

    context_dict = { 'task_note':task_note, 'task_count':task_count}
    return context_dict
