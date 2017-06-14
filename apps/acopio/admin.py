from django.contrib import admin
from .models import Acopio, Socio, DetalleAcopio, Parcela

admin.site.register(Acopio)
admin.site.register(Socio)
admin.site.register(Parcela)
admin.site.register(DetalleAcopio)
