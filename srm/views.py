from django.shortcuts import render, reverse, HttpResponse ,HttpResponseRedirect, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import *
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from .forms import *
from urllib.request import Request, urlopen
from urllib.parse import quote
from datetime import datetime
from django.db.models import Count, Sum
# Create your views here.

# Create your views here.
@login_required
def srm_home(request):
    deal_count = Deal.objects.all().count()
    contact_count = Contact.objects.all().count()
    task_list = Task.objects.filter(finish=False)[:6]
    deal_list = Deal.objects.filter(stage__title='В процессе', archive=False)
    sum = Deal.objects.all().aggregate(total_sum=Sum('budget'))
    context = {
    'task_list':task_list, 'deal_list':deal_list, 'sum':sum, 'deal_count':deal_count,
    'contact_count':contact_count }
    return render(request, 'srm/index.html', context)


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Правильный пароль и пользователь "активен"
        login(request, user)
        # Перенаправление на "правильную" страницу
        return render(request,'masters/index.html')
    else:
        # Отображение страницы с ошибкой
        return HttpResponseRedirect("/account/invalid/")


def logout_view(request):
    logout(request)
    return redirect('home')


@method_decorator(login_required, name='dispatch')
class OrderList(ListView):
    model = Deal
    queryset = Deal.objects.filter(archive=False)

    def get_context_data(self, **kwargs):
        context = super(OrderList, self).get_context_data(**kwargs)
        sum = Deal.objects.all().aggregate(total_sum=Sum('budget'))
        costs = Deal.objects.all().aggregate(total_sum=Sum('costs__price'))
        context['sum'] = sum
        context['total_costs'] = sum['total_sum'] - costs['total_sum']
        return context


@method_decorator(login_required, name='dispatch')
class ArchiveOrderList(ListView):
    model = Deal
    queryset = Deal.objects.filter(archive=True)

@method_decorator(login_required, name='dispatch')
class OrderDetail(DetailView):
    model = Deal

    def get_context_data(self, **kwargs):
        context = super(OrderDetail, self).get_context_data(**kwargs)
        context['today'] = datetime.today().date()
        context['task_list'] = Task.objects.filter(deal=self.object)
        costs_list = Costs.objects.filter(deal=self.object)
        context['costs_list'] = costs_list
        costs_sum = 0
        for item in costs_list:
            costs_sum += item.price

        context['sum'] = self.object.budget - costs_sum
        return context


@method_decorator(login_required, name='dispatch')
class OrderAdd(CreateView):
    model = Deal
    form_class = OrderAddForm
    def get_success_url(self):
        return reverse('orders:order_list')

@method_decorator(login_required, name='dispatch')
class OrderEdit(UpdateView):
    model = Deal
    form_class = OrderEditForm
    template_name = 'srm/deal_edit.html'

    def get_success_url(self):
        return reverse('orders:order_list')


@method_decorator(login_required, name='dispatch')
class OrderDelete(DeleteView):
    model = Deal
    success_url = reverse_lazy('orders:order_list')


@method_decorator(login_required, name='dispatch')
class ContactList(ListView):
    model = Contact

@method_decorator(login_required, name='dispatch')
class ContactDetail(DetailView):
    model = Contact

    def get_context_data(self, **kwargs):
        context = super(ContactDetail, self).get_context_data(**kwargs)
        context['deal_list'] = Deal.objects.filter(contact=self.object)
        context['sum'] = Deal.objects.filter(contact=self.object).aggregate(total_sum=Sum('budget'))
        return context

@method_decorator(login_required, name='dispatch')
class ContactAdd(CreateView):
    model = Contact
    form_class = ContactAddForm
    def get_success_url(self):
        return reverse('orders:contact_list')

@method_decorator(login_required, name='dispatch')
class ContactEdit(UpdateView):
    model = Contact
    form_class = ContactEditForm
    template_name = 'srm/contact_edit.html'

    def get_success_url(self):
        return reverse('orders:contact_list')


@method_decorator(login_required, name='dispatch')
class ContactDelete(DeleteView):
    model = Contact
    success_url = reverse_lazy('orders:contact_list')

@login_required
def order_filter(request):
    """Фильтр заказов"""
    if 'select' in request.GET and request.GET['select']=='all':
        order_list = Deal.objects.all()
    else:
        order_list = Deal.objects.filter(stage__title = request.GET.get('select'))
    context = {'deal_list':order_list}
    return render(request, 'srm/deal_list.html', context)


@method_decorator(login_required, name='dispatch')
class TaskList(ListView):
    model = Task
    queryset = Task.objects.filter(finish=False)

    def get_context_data(self, **kwargs):
        context = super(TaskList, self).get_context_data(**kwargs)
        context['today'] = datetime.today().date()
        return context

@method_decorator(login_required, name='dispatch')
class TaskDetail(DetailView):
    model = Task


@method_decorator(login_required, name='dispatch')
class TaskAdd(CreateView):
    model = Task
    form_class = TaskAddForm
    template_name = 'srm/task_add.html'
    def get_success_url(self):
        return reverse('orders:order_detail', kwargs={'pk': self.object.deal.id})

    def form_valid(self, form):
        form.instance.deal = Deal.objects.get(id=self.kwargs['deal_id'])
        # form.instance.save()
        # self.user.teams.add(form.instance)
        form.save()
        return super(TaskAdd, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class TaskAddAll(CreateView):
    model = Task
    form_class = TaskAddAllForm
    template_name = 'srm/task_add.html'
    def get_success_url(self):
        return reverse('orders:task_list')

@method_decorator(login_required, name='dispatch')
class TaskEdit(UpdateView):
    model = Task
    form_class = TaskAddForm
    template_name = 'srm/task_edit.html'

    def get_success_url(self):
        return reverse('orders:order_detail', kwargs={'pk': self.object.deal.id})


@method_decorator(login_required, name='dispatch')
class TaskDelete(DeleteView):
    model = Task
    template_name = 'srm/task_delete.html'
    def get_success_url(self):
        return reverse('orders:order_detail', kwargs={'pk': self.object.deal.id})


@method_decorator(login_required, name='dispatch')
class CostsList(ListView):
    model = Costs

@method_decorator(login_required, name='dispatch')
class CostsAdd(CreateView):
    model = Costs
    form_class = CostsForm
    template_name = 'srm/task_add.html'
    def get_success_url(self):
        return reverse('orders:order_detail', kwargs={'pk': self.object.deal.id})

    def form_valid(self, form):
        form.instance.deal = Deal.objects.get(id=self.kwargs['deal_id'])
        # form.instance.save()
        # self.user.teams.add(form.instance)
        form.save()
        return super(CostsAdd, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class CostsEdit(UpdateView):
    model = Costs
    form_class = CostsForm
    template_name = 'srm/task_edit.html'

    def get_success_url(self):
        return reverse('orders:order_detail', kwargs={'pk': self.object.deal.id})


@method_decorator(login_required, name='dispatch')
class CostsDelete(DeleteView):
    model = Costs
    template_name = 'srm/task_delete.html'
    def get_success_url(self):
        return reverse('orders:order_detail', kwargs={'pk': self.object.deal.id})
