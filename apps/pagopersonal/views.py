from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .forms import PagoPersonalForm
from .models import PagoPersonal


# class IndexView(ListView):
#     model = Person
#     template_name = "index.html"


# VIEW Persona
class PagoPersonalListView(ListView):
    model = PagoPersonal
    template_name = "pagopersonal/pago_personal_list.html"
    context_object_name = 'pagopersonales'  # Default: object_list
    paginate_by = 7
    queryset = PagoPersonal.objects.all()  # Default: Model.objects.all()

    def get_queryset(self):
        return PagoPersonal.objects.all()


class PagoPersonalCreateView(CreateView):
    model = PagoPersonal
    form_class = PagoPersonalForm
    template_name = 'pagopersonal/pago_personal_form.html'
    success_url = reverse_lazy('pagopersonal:pagopersonal_list')


class PagoPersonalUpdateView(UpdateView):
    model = PagoPersonal
    form_class = PagoPersonalForm
    template_name = 'pagopersonal/pago_personal_form.html'
    success_url = reverse_lazy('pagopersonal:pagopersonal_list')

    def dispatch(self, *args, **kwargs):
        self.autor_id = kwargs['pk']
        return super(PagoPersonalUpdateView, self).dispatch(*args, **kwargs)


class PagoPersonalDeleteView(DeleteView):
    model = PagoPersonal
    template_name = 'pagopersonal/pago_personal_delete.html'
    success_url = reverse_lazy('pagopersonal:pagopersonal_list')
