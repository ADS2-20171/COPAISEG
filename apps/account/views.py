from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import PersonaForm, UsuarioForm
from .models import Person, User


class AccountListView(ListView):
    model = Person
    template_name = "account/index.html"


# VIEW Persona
class PersonaListView(ListView):
    model = Person
    template_name = "account/persona_list.html"

    def get_queryset(self):
        return Person.objects.all()


class PersonaCreateView(CreateView):
    model = Person
    form_class = PersonaForm
    template_name = 'account/persona_form.html'
    success_url = reverse_lazy('account:persona_list')


class PersonaUpdateView(UpdateView):
    model = Person
    form_class = PersonaForm
    template_name = 'account/persona_form.html'
    success_url = reverse_lazy('account:persona_list')

    def dispatch(self, *args, **kwargs):
        self.autor_id = kwargs['pk']
        return super(PersonaUpdateView, self).dispatch(*args, **kwargs)


class PersonaDeleteView(DeleteView):
    model = Person
    template_name = 'account/persona_delete.html'
    success_url = reverse_lazy('account:persona_list')


# VIEW Usuario
class UsuarioListView(ListView):
    model = User
    template_name = "account/usuario_list.html"

    def get_queryset(self):
        return User.objects.all()


class UsuarioCreateView(CreateView):
    model = User
    form_class = UsuarioForm
    template_name = 'account/usuario_form.html'
    success_url = reverse_lazy('account:usuario_list')


class UsuarioUpdateView(UpdateView):
    model = User
    form_class = UsuarioForm
    template_name = 'account/usuario_form.html'
    success_url = reverse_lazy('account:usuario_list')

    def dispatch(self, *args, **kwargs):
        self.autor_id = kwargs['pk']
        return super(UsuarioUpdateView, self).dispatch(*args, **kwargs)


class UsuarioDeleteView(DeleteView):
    model = User
    template_name = 'account/usuario_delete.html'
    success_url = reverse_lazy('account:usuario_list')
