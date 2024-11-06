from django.test import TestCase
from .models import MiModelo

class MiModeloTestCase(TestCase):
    def setUp(self):
        MiModelo.objects.create(nombre="Test 1")

    def test_nombre(self):
        modelo = MiModelo.objects.get(nombre="Test 1")
        self.assertEqual(modelo.nombre, "Test 1")