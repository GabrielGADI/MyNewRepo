'''
Alegeti una din temele de mai sus, si convertiti testele din unittest in pytest.
R: test_func_pytest
'''
from Teme.tema8.testing_example.app.func import FormaGeometrica, Patrat, Cerc
from math import pi


def test_patrat_aria():
    p = Patrat(5)
    assert p.aria() == 25


def test_patrat_perimetru():
    p = Patrat(5)
    assert p.perimetru() == 20


def test_cerc_aria():
    c = Cerc(5)
    assert c.aria() == pi * 5 ** 2


def test_cerc_perimetru():
    c = Cerc(5)
    assert c.perimetru() == 2 * pi * 5
