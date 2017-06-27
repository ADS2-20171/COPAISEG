# encoding: utf-8
from django import forms

from .models import PagoPersonal


class PagoPersonalForm(forms.ModelForm):

    class Meta:
        model = PagoPersonal
        fields = ['cargo', 'monto']


# class UsuarioForm(forms.ModelForm):

#     class Meta:
#         model = User
#         fields = ['username', 'password', 'groups', 'user_permissions',
#                   'is_staff', 'is_active', 'is_superuser', 'last_login',
#                   'date_joined', 'persona']
