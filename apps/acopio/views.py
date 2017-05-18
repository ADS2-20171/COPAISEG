from django.shortcuts import render
from django.views.generic import ListView
from .models import Socio


class AcopioListView(ListView):
    model = Socio
    template_name = "acopio/acopio_list.html"
