# encoding=utf-8
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username', 'email', 'first_name', 'last_name', 'last_login',
            'date_joined'
        ]
        labels = {
            'username': 'Nombre de usuario ',
            'email': 'E-mail:',
        }


class UsuarioLogeoForm(forms.Form):

    username = forms.CharField(label='', max_length=50,
                               widget=forms.TextInput(attrs={
                                   'type': 'text',
                                   'placeholder': 'Usuario',
                                   'class': 'login-form_input'
                               }))
    password = forms.CharField(label='', max_length=50,
                               widget=forms.TextInput(attrs={
                                   'type': 'password',
                                   'placeholder': 'Contraseña',
                                   'class': 'login-form_input'
                               }))

    def clean(self):
        user_existe = User.objects.filter(
            username=self.cleaned_data['username'])
        if not user_existe:
            self.add_error('username', 'El nombre de usuario no existe')
        else:
            user = User.objects.get(username=self.cleaned_data['username'])
            if not user.check_password(self.cleaned_data['password']):
                self.add_error('password', 'El password no existe')
