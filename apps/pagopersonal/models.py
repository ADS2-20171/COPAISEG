from django.db import models
from apps.account.models import Persona


class RegistroAsistencia(models.Model):


    fecha_acceso = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "RegistroAsistencia"
        verbose_name_plural = "RegistroAsistencias"

    def __str__(self):
        return self.fecha_acceso


class PagoPersonal(models.Model):

    cargo = models.CharField(max_length=20)
    monto = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = "PagoPersonal"
        verbose_name_plural = "PagoPersonales"

    def __str__(self):
        return self.cargo

    def pays(self):
        return 'Yo como %s gano "%s"' % (self.cargo, self.monto)


class PersonalRegistro(models.Model):

    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    pagopersonal = models.ForeignKey(PagoPersonal, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    RUC = models.CharField(max_length=20)

    class Meta:
        verbose_name = "PersonalRegistro"
        verbose_name_plural = "PersonalRegistros"

    def __str__(self):
        return self.persona.first_name


class Personal(models.Model):

    #persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    #RUC = models.CharField(max_length=15)
    registro_asistencia = models.ForeignKey(
        RegistroAsistencia, on_delete=models.CASCADE)
    personal_registro = models.ForeignKey(
        PersonalRegistro, on_delete=models.CASCADE)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    mes_correspondiente = models.CharField(max_length=20)
    pago_total = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, null=True)
    #socio = models.ForeignKey(Socio, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Personal"
        verbose_name_plural = "Personales"

    def __str__(self):
        return self.personal_registro.persona.first_name


class DetalleReciboHonorario(models.Model):

    #persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    #RUC = models.CharField(max_length=15)
    personal = models.ForeignKey(
        Personal, on_delete=models.CASCADE)
    concepto = models.CharField(max_length=20)
    suma_de = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, null=True)
    total_neto_recibido = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, null=True)
    #socio = models.ForeignKey(Socio, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "DetalleReciboHonorario"
        verbose_name_plural = "DetalleReciboHonorarios"

    def __str__(self):
        return self.concepto


class ReciboHonorario(models.Model):

    #persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    #RUC = models.CharField(max_length=15)
    detalle_recibo_honorarios = models.ForeignKey(
        DetalleReciboHonorario, on_delete=models.CASCADE)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    num_recibo_honorarios = models.CharField(max_length=20)
    #socio = models.ForeignKey(Socio, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "ReciboHonorario"
        verbose_name_plural = "ReciboHonorarios"

    def __str__(self):
        return self.ReciboHonorario
# return "%s %s %s" % (self.acopio.socio.persona.first_name,
        # self.acopio.socio.persona.last_name,
        # self.parcela.codigo)
