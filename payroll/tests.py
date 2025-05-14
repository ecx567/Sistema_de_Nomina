from django.test import TestCase
from .models import Rol, Empleado

class RolModelTest(TestCase):
    def setUp(self):
        self.empleado = Empleado.objects.create(nombre="Juan Pérez", apellido="García", salario=5000)
        self.rol = Rol.objects.create(empleado=self.empleado, mes="Enero", anio=2023, salario_base=5000)

    def test_calcular_tot_ing(self):
        self.rol.horas_extra = 10
        self.rol.bono = 500
        self.rol.calcular_tot_ing()
        self.assertEqual(self.rol.tot_ing, 5500)  # 5000 + (10 * 0) + 500

    def test_calcular_iess(self):
        self.rol.calcular_iess()
        self.assertEqual(self.rol.iess, 472.5)  # 9.45% de 5000

    def test_calcular_tot_des(self):
        self.rol.deducciones = self.rol.iess
        self.rol.calcular_tot_des()
        self.assertEqual(self.rol.tot_des, 472.5)

    def test_calcular_neto(self):
        self.rol.deducciones = self.rol.iess
        self.rol.calcular_neto()
        self.assertEqual(self.rol.neto, 4527.5)  # 5000 - 472.5

    def test_string_representation(self):
        self.assertEqual(str(self.rol), 'Rol de Juan Pérez para Enero/2023')