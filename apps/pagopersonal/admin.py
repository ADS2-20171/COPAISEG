from django.contrib import admin
from .models import RegistroAsistencia, Personal, PagoPersonal

admin.site.register(RegistroAsistencia)
admin.site.register(Personal)
admin.site.register(PagoPersonal)
