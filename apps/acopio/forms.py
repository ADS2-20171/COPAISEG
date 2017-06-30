# encoding: utf-8
from django import forms

from apps.account.models import Persona
from .models import Socio, Parcela, Acopio, DetalleAcopio


class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = ['first_name', 'last_name', 'identity_type',
                  'identity_num', 'photo', 'email', 'birth_date']
        labels = {
            'first_name': 'Nombre: ',
            'last_name': 'Apellidos: ',
            'identity_type': 'Tipo de Identidad: ',
            'identity_num': 'Número: ',
            'photo': 'Fotografía: ',
            'email': 'E-mail: ',
            'birth_date': 'Fecha de Nacimiento: ',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'identity_num': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SocioForm(forms.ModelForm):

    class Meta:
        model = Socio
        fields = ['cod_socio', 'direccion', 'ciudad',
                  'estado']
        labels = {
            'cod_socio': 'Codigo de Socio: ',
            'direccion': 'Dirección: ',
            'ciudad': 'Distrito: ',
            'estado': 'Estado: ',
        }
        # widgets = {
        #     'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'identity_num': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email': forms.TextInput(attrs={'class': 'form-control'}),
        # }


class ParcelaForm(forms.ModelForm):

    class Meta:
        model = Parcela
        fields = ['codigo', 'ubicacion', 'area_cultivo', 'area_desarrollo',
                  'prod_estimado_tn', 'prod_estimado_kg', 'total_parcelas',
                  'socio']


class AcopioForm(forms.ModelForm):

    class Meta:
        model = Acopio
        fields = ['socio', 'estado', 'n_ticket']
        labels = {
            'socio': 'Proveedor ',
            'estado': 'Pagado?: ',
            'n_ticket': 'N° Ticket: ',
        }


class DetalleAcopioForm(forms.ModelForm):

    class Meta:
        model = DetalleAcopio
        fields = ['parcela', 'acopio', 'kilos', 'precio_uni', 'total_pagar']
        labels = {
            'parcela': 'Parcela: ',
            'acopio': 'Acopio:',
            'kilos': 'Cantidad en Kg.: ',
            'precio_uni': 'Acopiado a: ',
            'total_pagar': 'Total a pagar: ',
        }
