'''
Folosind TDD, rezolvati urmatoarea problema: Sa se scrie o ierarhie de clase pentru forme geometrice: FormaGeometrica,
Patrat, Dreptunghi, Cerc.
FormaGeometrica este interfata, adica clasa abstracta cu doar metode astracte. Metode: arie(), perimetru().
Sa se mosteneasca interfata, si sa se implementeze cele 2 metode pentru fiecare din cele 3 forme geometrice.
R: test_forma_geomerica
'''
from Teme.tema8.testing_example.app.forma_geometrica import Patrat, Dreptunghi, Cerc
import unittest
from parameterized import parameterized


class TestCerc(unittest.TestCase):
    @parameterized.expand([
        [Cerc(5), 78.5],
        [Cerc(0), 0],
        [Cerc(10), 314.000000000000002]
    ])
    def test_arie(self, cerc, expected):
        self.assertEqual(cerc.arie(), expected)

    @parameterized.expand([
        [Cerc(5), 31.400000000000002],
        [Cerc(0), 0],
        [Cerc(10), 62.800000000000004]
    ])
    def test_perimetru(self, cerc, expected):
        self.assertEqual(cerc.perimetru(), expected)


class TestPatrat(unittest.TestCase):

    @parameterized.expand([
        [Patrat(10), 100],
        [Patrat(0), 0],
        [Patrat(1), 1],
        [Patrat(5), 25]
    ])
    def test_arie(self, patrat, expected):
        self.assertEqual(patrat.arie(), expected)

    @parameterized.expand([
        [Patrat(10), 40],
        [Patrat(0), 0],
        [Patrat(1), 4],
        [Patrat(5), 20]
    ])
    def test_perimetru(self, patrat, expected):
        self.assertEqual(patrat.perimetru(), expected)


class TestDreptunghi(unittest.TestCase):
    @parameterized.expand([
        [Dreptunghi(5,7),35],
        [Dreptunghi(0,2), 0],
        [Dreptunghi(10,12), 120]
    ])
    def test_arie(self, dreptunghi, expected):
        self.assertEqual(dreptunghi.arie(), expected)

    @parameterized.expand([
        [Dreptunghi(5,7), 24],
        [Dreptunghi(0,2), 4],
        [Dreptunghi(10,12), 44]
    ])
    def test_perimetru(self, dreptunghi, expected):
        self.assertEqual(dreptunghi.perimetru(), expected)

