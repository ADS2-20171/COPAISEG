from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .forms import PersonaForm
from .models import Persona


# class IndexView(ListView):
#     model = Person
#     template_name = "index.html"


# VIEW Persona
class PersonaListView(ListView):
    model = Persona
    template_name = "account/persona_list.html"
    context_object_name = 'persons'  # Default: object_list
    paginate_by = 7
    queryset = Persona.objects.all()  # Default: Model.objects.all()

    def get_queryset(self):
        return Persona.objects.all()


class PersonaCreateView(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'account/persona_form.html'
    success_url = reverse_lazy('account:persona_list')


class PersonaUpdateView(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'account/persona_form.html'
    success_url = reverse_lazy('account:persona_list')

    def dispatch(self, *args, **kwargs):
        self.autor_id = kwargs['pk']
        return super(PersonaUpdateView, self).dispatch(*args, **kwargs)


class PersonaDeleteView(DeleteView):
    model = Persona
    template_name = 'account/persona_delete.html'
    success_url = reverse_lazy('account:persona_list')


# VIEW Usuario
class UsuarioListView(ListView):
    model = User
    template_name = "account/usuario_list.html"
    context_object_name = 'users'  # Default: object_list
    paginate_by = 7
    queryset = User.objects.all()  # Default: Model.objects.all()

    def get_queryset(self):
        return User.objects.all()


class UsuarioCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'account/usuario_form.html'
    success_url = reverse_lazy('account:usuario_list')


class UsuarioUpdateView(UpdateView):
    model = User
    form_class = UserCreationForm
    template_name = 'account/usuario_form.html'
    success_url = reverse_lazy('account:usuario_list')

    def dispatch(self, *args, **kwargs):
        self.autor_id = kwargs['pk']
        return super(UsuarioUpdateView, self).dispatch(*args, **kwargs)


class UsuarioDeleteView(DeleteView):
    model = User
    template_name = 'account/usuario_delete.html'
    success_url = reverse_lazy('account:usuario_list')
