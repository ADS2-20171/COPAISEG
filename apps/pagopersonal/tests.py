from django.test import TestCase

from .models import PagoPersonal


class PagoPersonalTestCase(TestCase):

    def setUp(self):
        PagoPersonal.objects.create(cargo="administrador", monto=50)
        PagoPersonal.objects.create(cargo="contadora", monto=35)

    def test_pago_pay_money(self):
        """Personas that can speak are correctly identified"""
        administrador = PagoPersonal.objects.get(cargo="administrador")
        contadora = PagoPersonal.objects.get(cargo="contadora")
        self.assertEqual(administrador.pays(), 'Yo como administrador gano "50.00"')
        self.assertEqual(contadora.pays(), 'Yo como contadora gano "35.00"')
