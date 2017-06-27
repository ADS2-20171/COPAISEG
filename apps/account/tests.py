from django.test import TestCase

from .models import Persona


class PersonaTestCase(TestCase):

    def setUp(self):
        Persona.objects.create(first_name="juan", last_name="juarez")
        Persona.objects.create(first_name="pedro", last_name="lasalle")

    def test_personas_have_apell(self):
        """Personas that can speak are correctly identified"""
        juan = Persona.objects.get(first_name="juan")
        pedro = Persona.objects.get(first_name="pedro")
        self.assertEqual(juan.have(), 'Yo juan y mi apellido es "juarez"')
        self.assertEqual(pedro.have(), 'Yo pedro y mi apellido es "lasalle"')
