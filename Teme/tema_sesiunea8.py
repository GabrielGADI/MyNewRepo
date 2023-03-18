from Teme.tema_sesiunea7 import FormaGeometrica, Patrat, Cerc
import unittest
from math import pi


# Alegeti 3 functii din cele implementate la tema anterior, si scrieti unit tests pentru ele folosind unittest.

class FormaGeometrica(unittest.TestCase):
    def test_cerc_perimetru(self):
        c = Cerc(5)
        self.assertAlmostEqual(c.perimetru(), 2 * pi * 5)

    def test_cerc_aria(self):
        c = Cerc(5)
        self.assertAlmostEqual(c.aria(), pi * 5 ** 2)

    def test_patrat_perimetru(self):
        p = Patrat(4)
        self.assertEqual(p.perimetru(), 4 * 4 )


# Alegeti 2 clase din cele implementate la tema anterior, si scrieti unit teste pentru toate metodele folosind unittest.


class TestCerc(unittest.TestCase):
    def test_perimetru(self):
        c = Cerc(6)
        self.assertAlmostEqual(c.perimetru(), 2 * pi * 6)

    def test_aria(self):
        c = Cerc(5)
        self.assertAlmostEqual(c.aria(), pi * 5 ** 2)


class TestPatrat(unittest.TestCase):
    def test_perimetru(self):
        p = Patrat(5)
        self.assertEqual(p.perimetru(), 20)

    def test_aria(self):
        p = Patrat(5)
        self.assertEqual(p.aria(), 25)


if __name__ == '__main__':
    unittest.main()


