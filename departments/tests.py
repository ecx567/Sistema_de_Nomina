from django.test import TestCase
from .models import Departamento

class DepartamentoModelTest(TestCase):

    def setUp(self):
        Departamento.objects.create(nombre="Recursos Humanos", descripcion="Gestión de personal")
        Departamento.objects.create(nombre="Finanzas", descripcion="Gestión financiera")

    def test_departamento_str(self):
        departamento = Departamento.objects.get(nombre="Recursos Humanos")
        self.assertEqual(str(departamento), "Recursos Humanos")

    def test_departamento_count(self):
        count = Departamento.objects.count()
        self.assertEqual(count, 2)

    def test_departamento_creation(self):
        departamento = Departamento.objects.create(nombre="IT", descripcion="Soporte técnico")
        self.assertEqual(departamento.nombre, "IT")
        self.assertEqual(departamento.descripcion, "Soporte técnico")