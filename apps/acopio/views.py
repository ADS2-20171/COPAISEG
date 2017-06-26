from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView

from .models import Socio
from .forms import SocioForm, PersonaForm


class SocioListView(ListView):
    model = Socio
    template_name = 'acopio/socio_list.html'


class SocioCreateView(CreateView):
    model = Socio
    template_name = 'acopio/socio_form.html'
    form_class = SocioForm
    second_forms_class = PersonaForm
    success_url = reverse_lazy('acopio:socio_list')

    def get_context_data(self, **kwargs):
        context = super(SocioCreateView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_forms_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_forms_class(request.POST)
        if form.is_valid() and form2.is_valid():
            socio = form.save(commit=False)
            socio.persona = form2.save()
            socio.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form,
                                                                 form2=form2))
