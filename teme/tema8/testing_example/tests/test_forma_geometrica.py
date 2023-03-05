'''
Folosind TDD, rezolvati urmatoarea problema: Sa se scrie o ierarhie de clase pentru forme geometrice: FormaGeometrica, Patrat, Dreptunghi, Cerc.
FormaGeometrica este interfata, adica clasa abstracta cu doar metode astracte. Metode: arie(), perimetru().
Sa se mosteneasca interfata, si sa se implementeze cele 2 metode pentru fiecare din cele 3 forme geometrice.
R: test_forma_geomerica
'''
from teme.tema8.testing_example.app.forma_geometrica import Patrat, Dreptunghi, Cerc
import unittest


class TestFormeGeometrice(unittest.TestCase):
    def test_patrat(self):
        patrat = Patrat(5)
        self.assertEqual(patrat.arie(), 25)
        self.assertEqual(patrat.perimetru(), 20)

    def test_dreptunghi(self):
        dreptunghi = Dreptunghi(4, 6)
        self.assertEqual(dreptunghi.arie(), 24)
        self.assertEqual(dreptunghi.perimetru(), 20)

    def test_cerc(self):
        cerc = Cerc(3)
        self.assertAlmostEqual(cerc.arie(), 28.26, delta=0.01)
        self.assertAlmostEqual(cerc.perimetru(), 18.84, delta=0.01)
