from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Balance
from .forms import BalanceForm


class MonedaListView(ListView):
    model = Balance
    template_name = 'caja/moneda_list.html'


class MonedaCreateView(CreateView):
    model = Balance
    form_class = BalanceForm
    template_name = 'caja/moneda_form.html'
    success_url = reverse_lazy('kaja:moneda_list')


class MonedaUpdateView(UpdateView):
    model = Balance
    form_class = BalanceForm
    template_name = 'caja/moneda_form.html'
    success_url = reverse_lazy('kaja:moneda_list')

    def dispatch(self, *args, **kwargs):
        self.autor_id = kwargs['pk']
        return super(MonedaUpdateView, self).dispatch(*args, **kwargs)


class MonedaDeleteView(DeleteView):
    model = Balance
    template_name = 'caja/persona_delete.html'
    success_url = reverse_lazy('kaja:moneda_list')
