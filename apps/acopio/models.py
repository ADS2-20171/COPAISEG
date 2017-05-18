from django.db import models
from apps.account.models import Person


class Socio(models.Model):

    persona = models.OneToOneField(Person, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=8)

    class Meta:
        verbose_name = "Socio"
        verbose_name_plural = "Socios"

    def __str__(self):
        return self.persona.first_name


class Parcela(models.Model):

    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=8)
    ubicacion = models.CharField(max_length=20)
    area_cultivo = models.DecimalField(max_digits=4, decimal_places=2)
    area_desarrollo = models.DecimalField(max_digits=4, decimal_places=2)
    prod_estimado_tn = models.DecimalField(max_digits=4, decimal_places=2)
    prod_estimado_kg = models.DecimalField(max_digits=4, decimal_places=2)
    certificacion_propuesta = models.CharField(max_length=5)
    total_parcelas = models.IntegerField()

    class Meta:
        verbose_name = "Parcela"
        verbose_name_plural = "Parcelas"

    def __str__(self):
        return self.codigo


class Acopio(models.Model):

    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    fech_acopio = models.DateTimeField(auto_now_add=True)
    parcela = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    precio_uni = models.DecimalField(max_digits=6, decimal_places=2)
    pago = models.IntegerField()
    estado = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Acopio"
        verbose_name_plural = "Acopios"

    def __str__(self):
        return self.parcela
