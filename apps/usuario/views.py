from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.views.generic import CreateView, FormView, TemplateView
from django.core.urlresolvers import reverse_lazy, reverse

from .forms import RegistroForm, UsuarioLogeoForm


def LogOut(request):
    logout(request)
    return redirect(reverse('usuario:login'))


class Inicio(TemplateView):
    template_name = 'index.html'


class RegistroUsuario(CreateView):
    model = User
    template_name = "usuario/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('account:persona_list')


class Logeo(FormView):

    template_name = 'login.html'
    form_class = UsuarioLogeoForm
    success_url = reverse_lazy('usuario:index')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        if user.is_active:
            login(self.request, user)
            return super(Logeo, self).form_valid(form)
        else:
            return redirect(reverse('usuario:login'))
