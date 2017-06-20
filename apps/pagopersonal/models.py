from django.db import models


class RegistroAsistencia(models.Model):

    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "RegistroAsistencia"
        verbose_name_plural = "RegistroAsistencias"

    def __str__(self):
        return self.updated_at


class Personal(models.Model):

    RUC = models.CharField(max_length=8)
    pago_total = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, null=True)
    #socio = models.ForeignKey(Socio, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Personal"
        verbose_name_plural = "Personals"

    def __str__(self):
        return self.RUC


class PagoPersonal(models.Model):

    cargo = models.CharField(max_length=10)
    monto = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = "PagoPersonal"
        verbose_name_plural = "PagoPersonals"

    def __str__(self):
        return self.cargo
