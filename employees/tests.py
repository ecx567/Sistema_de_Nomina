from django.test import TestCase
from .models import Empleado, Cargo, Departamento, TipoContrato

class EmpleadoModelTest(TestCase):

    def setUp(self):
        self.departamento = Departamento.objects.create(nombre='Recursos Humanos', descripcion='Gestión de personal')
        self.cargo = Cargo.objects.create(nombre='Gerente', descripcion='Responsable de la gestión')
        self.tipo_contrato = TipoContrato.objects.create(nombre='Indefinido', descripcion='Contrato sin fecha de finalización')
        self.empleado = Empleado.objects.create(
            nombre='Juan',
            apellido='Pérez',
            cargo=self.cargo,
            departamento=self.departamento,
            tipo_contrato=self.tipo_contrato,
            fecha_ingreso='2023-01-01',
            salario=5000
        )

    def test_empleado_creation(self):
        self.assertEqual(self.empleado.nombre, 'Juan')
        self.assertEqual(self.empleado.apellido, 'Pérez')
        self.assertEqual(self.empleado.cargo.nombre, 'Gerente')
        self.assertEqual(self.empleado.departamento.nombre, 'Recursos Humanos')
        self.assertEqual(self.empleado.tipo_contrato.nombre, 'Indefinido')
        self.assertEqual(self.empleado.salario, 5000)

    def test_string_representation(self):
        self.assertEqual(str(self.empleado), 'Juan Pérez')