# encoding: utf-8
from django import forms

from .models import Persona


class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = ['first_name', 'last_name', 'identity_type',
                  'identity_num', 'photo', 'email', 'birth_date']


# class UsuarioForm(forms.ModelForm):

#     class Meta:
#         model = User
#         fields = ['username', 'password', 'groups', 'user_permissions',
#                   'is_staff', 'is_active', 'is_superuser', 'last_login',
#                   'date_joined', 'persona']
