from django.db import models
from apps.acopio.models import Acopio
# Create your models here.


class Cargo(models.Model):

    monto_ingreso = models.DecimalField(max_digits=20, decimal_places=2)
    tipo_cargo = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

    def __str__(self):
        return self.tipo_cargo


class Balance(models.Model):

    #persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=20, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=20, decimal_places=2)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    acopio = models.ForeignKey(Acopio, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Balance"
        verbose_name_plural = "Balance"

    def __str__(self):
        return self.balance


class CajaEgreso(models.Model):

    fecha = models.DateTimeField(auto_now_add=True)
    num_comprobante = models.CharField(max_length=50, blank=True)
    acopio = models.ForeignKey(Acopio, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "CajaEgreso"
        verbose_name_plural = "CajaEgresos"

    def __str__(self):
        return self.acopio.socio.persona.first_name


class DetalleCaja(models.Model):

    cantidad = models.DecimalField(max_digits=20, decimal_places=2)
    descripcion = models.CharField(max_length=50, blank=True)
    precio_uni = models.DecimalField(
        'Precio Unitario', max_digits=20, decimal_places=2)
    total_egreso = models.DecimalField(
        'Precio a Pagar', max_digits=20, decimal_places=2)

    class Meta:
        verbose_name = "DetalleCaja"
        verbose_name_plural = "Detalles Caja"

    def __unicode__(self):
        return self.cantidad
