from django.contrib import admin
from .models import Almacen, Categoria, unidadesmedida, Producto


admin.site.register(Almacen)
admin.site.register(Categoria)
admin.site.register(unidadesmedida)
admin.site.register(Producto)
