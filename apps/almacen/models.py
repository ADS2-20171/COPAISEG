from django.db import models
from apps.account.models import Persona


class Almacen(models.Model):

    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=8)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Producto"

    def __str__(self):
        return self.persona.first_name


class Categoria(models.Model):

    categoria = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categoria"

    def __str__(self):
        return self.categoria


class unidadesmedida(models.Model):

    unidadM = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Unidades de medida"
        verbose_name_plural = "CUnidades de medida"

    def __str__(self):
        return self.unidaM
