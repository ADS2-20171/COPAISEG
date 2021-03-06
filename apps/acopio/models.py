from django.db import models
from apps.account.models import Persona


class Socio(models.Model):

    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    cod_socio = models.CharField(max_length=6)
    direccion = models.CharField(max_length=50, blank=True)
    ciudad = models.CharField(max_length=50, blank=True)
    estado = models.BooleanField(default=True)

    updated_at = models.DateTimeField("Updated at", auto_now=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        verbose_name = "Socio"
        verbose_name_plural = "Socios"

    def __str__(self):
        return self.persona.first_name


class Parcela(models.Model):

    codigo = models.CharField(max_length=8)
    ubicacion = models.CharField(max_length=20)
    area_cultivo = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, null=True)
    area_desarrollo = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, null=True)
    prod_estimado_tn = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, null=True)
    prod_estimado_kg = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, null=True)
    total_parcelas = models.IntegerField(blank=True, null=True)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Parcela"
        verbose_name_plural = "Parcelas"

    def __str__(self):
        return self.codigo


class Acopio(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    fech_acopio = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=False)
    n_ticket = models.IntegerField()

    class Meta:
        verbose_name = "Acopio"
        verbose_name_plural = "Acopios"

    def __str__(self):
        return self.socio.persona.first_name


class DetalleAcopio(models.Model):
    parcela = models.ForeignKey(Parcela, on_delete=models.CASCADE)
    acopio = models.ForeignKey(Acopio)
    kilos = models.DecimalField(max_digits=20, decimal_places=2)
    precio_uni = models.DecimalField(
        'Precio Unitario', max_digits=20, decimal_places=2)
    total_pagar = models.DecimalField(
        'Precio a Pagar', max_digits=20, decimal_places=2, blank=True, null=True)
    # total_importe = models.aggregate(Sum('importe'))

    class Meta:
        verbose_name = "Detalle  Acopio"
        verbose_name_plural = "Detalles Acopio"

    def __str__(self):
        return "%s %s %s" % (self.acopio.socio.persona.first_name,
                             self.acopio.socio.persona.last_name,
                             self.parcela.codigo)

    def _get_importe(self):
        return self.precio_uni * self.total_pagar
    importe = property(_get_importe)
