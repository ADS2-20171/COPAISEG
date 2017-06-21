from django.contrib import admin
from .models import Balance, Cargo, CajaEgreso, DetalleCaja

admin.site.register(Balance)
admin.site.register(Cargo)
admin.site.register(CajaEgreso)
admin.site.register(DetalleCaja)
# Register your models here.
