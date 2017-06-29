from django.test import TestCase

from .models import unidadesmedida


class ProductoTestCase(TestCase):

    def setUp(self):
        unidadesmedida.objects.create(unidadMedida="kilos", prefijo="kg")
        unidadesmedida.objects.create(unidadMedida="libras", prefijo="lb")

    def test_product_pays_product(self):
        """Personas that can speak are correctly identified"""
        kilos = unidadesmedida.objects.get(unidadMedida="kilos")
        libras = unidadesmedida.objects.get(unidadMedida="libras")
        self.assertEqual(kilos.have(), 'Los kilos su prefijo es "kg"')
        self.assertEqual(libras.have(), 'Los libras su prefijo es "lb"')