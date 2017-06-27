from django.db import models
from apps.account.models import Persona


class Almacen(models.Model):

    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=8)

    class Meta:
        verbose_name = "Almacen"
        verbose_name_plural = "Almacenes"

    def __str__(self):
        return self.persona.first_name


class Categoria(models.Model):

    categoria = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.categoria


class unidadesmedida(models.Model):

    unidadMedida = models.CharField(max_length=100)
    prefijo = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Unidade de medida"
        verbose_name_plural = "Unidades de medida"

    def __str__(self):
        return self.unidadMedida

    def have(self):
        return 'Los %s su prefijo es "%s"' % (self.unidadMedida, self.prefijo)


class Producto(models.Model):

    nombre = models.CharField(max_length=100)
    precioCompra = models.DecimalField(max_digits=20, decimal_places=2)
    precioVenta = models.DecimalField(max_digits=20, decimal_places=2)
    igv = models.DecimalField(max_digits=20, decimal_places=2)
    unidadMedida = models.ForeignKey(unidadesmedida, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    detalle = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.unidadMedida.prefijo

