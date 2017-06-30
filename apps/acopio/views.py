from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Socio, Parcela, Acopio, DetalleAcopio
from apps.account.models import Persona
from .forms import SocioForm, PersonaForm, ParcelaForm, AcopioForm, DetalleAcopioForm


class SocioListView(ListView):
    model = Socio
    template_name = 'socio/socio_list.html'
    context_object_name = 'socio'  # Default: object_list
    paginate_by = 7
    queryset = Socio.objects.all()  # Default: Model.objects.all()

    def get_queryset(self):
        return Socio.objects.all()


class SocioCreateView(CreateView):
    model = Socio
    template_name = 'socio/socio_form.html'
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


class SocioUpdateView(UpdateView):
    model = Socio
    second_model = Persona
    template_name = 'socio/socio_form.html'
    form_class = SocioForm
    second_form_class = PersonaForm
    success_url = reverse_lazy('acopio:socio_list')

    def get_context_data(self, **kwargs):
        context = super(SocioUpdateView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        socio = self.model.objects.get(id=pk)
        persona = self.second_model.objects.get(id=socio.persona_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=persona)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_socio = kwargs['pk']
        socio = self.model.objects.get(id=id_socio)
        persona = self.second_model.objects.get(id=socio.persona_id)
        form = self.form_class(request.POST, instance=socio)
        form2 = self.second_form_class(request.POST, instance=persona)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())


class SocioDeleteView(DeleteView):
    model = Socio
    template_name = 'socio/socio_delete.html'
    success_url = reverse_lazy('acopio:socio_list')


# PARCELA
class ParcelaListView(ListView):
    model = Parcela
    template_name = 'parcela/parcela_list.html'
    context_object_name = 'parcela'  # Default: object_list
    paginate_by = 7
    queryset = Parcela.objects.all()  # Default: Model.objects.all()

    def get_queryset(self):
        return Parcela.objects.all()


class ParcelaCreateView(CreateView):
    model = Parcela
    form_class = ParcelaForm
    template_name = 'parcela/parcela_form.html'
    success_url = reverse_lazy('acopio:parcela_list')


class ParcelaUpdateView(UpdateView):
    model = Parcela
    form_class = ParcelaForm
    template_name = 'parcela/parcela_form.html'
    success_url = reverse_lazy('acopio:parcela_list')

    def dispatch(self, *args, **kwargs):
        self.autor_id = kwargs['pk']
        return super(ParcelaUpdateView, self).dispatch(*args, **kwargs)


class ParcelaDeleteView(DeleteView):
    model = Parcela
    template_name = 'parcela/parcela_delete.html'
    success_url = reverse_lazy('acopio:parcela_list')


# ACOPIO
class AcopioDetalleListView(ListView):
    model = DetalleAcopio
    template_name = 'acopio/acopio_list.html'
    context_object_name = 'acopio'  # Default: object_list
    paginate_by = 7
    queryset = DetalleAcopio.objects.all()  # Default: Model.objects.all()

    def get_queryset(self):
        return DetalleAcopio.objects.all()


class AcopioDetalleCreateView(CreateView):
    model = DetalleAcopio
    template_name = 'acopio/acopio_form.html'
    form_class = AcopioForm
    second_forms_class = DetalleAcopioForm
    success_url = reverse_lazy('acopio:acopio_list')

    def get_context_data(self, **kwargs):
        context = super(AcopioDetalleCreateView, self).get_context_data(**kwargs)
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
            detalleacopio = form.save(commit=False)
            detalleacopio.acopio = form2.save()
            detalleacopio.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form,
                                                                 form2=form2))

# class AcopioDetalleUpdateView(UpdateView):
#     model = Socio
#     second_model = DetalleAcopio
#     template_name = 'socio/socio_form.html'
#     form_class = SocioForm
#     second_form_class = PersonaForm
#     success_url = reverse_lazy('acopio:socio_list')

#     def get_context_data(self, **kwargs):
#         context = super(SocioUpdateView, self).get_context_data(**kwargs)
#         pk = self.kwargs.get('pk', 0)
#         socio = self.model.objects.get(id=pk)
#         persona = self.second_model.objects.get(id=socio.persona_id)
#         if 'form' not in context:
#             context['form'] = self.form_class()
#         if 'form2' not in context:
#             context['form2'] = self.second_form_class(instance=persona)
#         context['id'] = pk
#         return context

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object
#         id_socio = kwargs['pk']
#         socio = self.model.objects.get(id=id_socio)
#         persona = self.second_model.objects.get(id=socio.persona_id)
#         form = self.form_class(request.POST, instance=socio)
#         form2 = self.second_form_class(request.POST, instance=persona)
#         if form.is_valid() and form2.is_valid():
#             form.save()
#             form2.save()
#             return HttpResponseRedirect(self.get_success_url())
#         else:
#             return HttpResponseRedirect(self.get_success_url())
