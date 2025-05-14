from django.test import TestCase
from .models import TipoContrato, Contrato
from employees.models import Empleado

class TipoContratoModelTest(TestCase):

    def setUp(self):
        self.tipo_contrato = TipoContrato.objects.create(nombre="Contrato a Tiempo Completo", descripcion="Contrato para empleados a tiempo completo")

    def test_tipo_contrato_creation(self):
        contrato = TipoContrato.objects.get(nombre="Contrato a Tiempo Completo")
        self.assertEqual(contrato.descripcion, "Contrato para empleados a tiempo completo")

    def test_tipo_contrato_str(self):
        self.assertEqual(str(self.tipo_contrato), "Contrato a Tiempo Completo")

class ContratoModelTest(TestCase):

    def setUp(self):
        self.empleado = Empleado.objects.create(nombre="Juan Pérez", apellido="Gómez", salario=5000)
        self.tipo_contrato = TipoContrato.objects.create(nombre="Contrato a Tiempo Completo", descripcion="Contrato para empleados a tiempo completo")
        self.contrato = Contrato.objects.create(empleado=self.empleado, tipo_contrato=self.tipo_contrato, fecha_inicio="2023-01-01")

    def test_contrato_creation(self):
        self.assertEqual(self.contrato.empleado.nombre, "Juan Pérez")
        self.assertEqual(self.contrato.tipo_contrato.nombre, "Contrato a Tiempo Completo")

    def test_contrato_str(self):
        self.assertEqual(str(self.contrato), "Juan Pérez - Contrato a Tiempo Completo")