from django.contrib import admin
from .models import RegistroAsistencia, Personal, PagoPersonal, PersonalRegistro, DetalleReciboHonorario, ReciboHonorario

admin.site.register(RegistroAsistencia)
admin.site.register(Personal)
admin.site.register(PagoPersonal)
admin.site.register(PersonalRegistro)
admin.site.register(DetalleReciboHonorario)
admin.site.register(ReciboHonorario)
