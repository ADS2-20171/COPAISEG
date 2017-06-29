# encoding: utf-8
from django import forms
from .models import Balance


class BalanceForm(forms.ModelForm):

    class Meta:
        model = Balance
        fields = ['balance', 'monto',
                  'cargo', 'acopio']
