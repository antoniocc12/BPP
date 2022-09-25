import unittest
from funciones import exp_cuadrado

class TestExp(unittest.TestCase):

    def test_1(self):
        resultado = exp_cuadrado(2)
        self.assertEqual(resultado, 4)

    def test_2(self):
        resultado = exp_cuadrado(10)
        self.assertIn(resultado, [3, 43, 20, 1000])

    def test_3(self):
        resultado = exp_cuadrado(10)
        self.assertIn(resultado, [3, 43, 20, 100])

    def test_4(self):
        resultado = exp_cuadrado(10)
        self.assertGreater(resultado, 200)

    def test_excepcion(self):
        with self.assertRaises(TypeError):
            resultado = exp_cuadrado('10')
