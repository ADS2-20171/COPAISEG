from django.test import TestCase
from .models import Cargo


class CargoTestCase(TestCase):

    def setUp(self):
        Cargo.objects.create(tipo_cargo="pago", monto_ingreso=4000)
        Cargo.objects.create(tipo_cargo="deposito", monto_ingreso=20000)

    def test_Cargos_do_depos(self):
        """Cargos that can speak are correctly identified"""
        pago = Cargo.objects.get(tipo_cargo="pago")
        deposito = Cargo.objects.get(tipo_cargo="deposito")
        self.assertEqual(pago.depos(), 'Por concepto de pago entro la suma de "4000.00"')
        self.assertEqual(deposito.depos(), 'Por concepto de deposito entro la suma de "20000.00"')
