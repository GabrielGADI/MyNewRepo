from Sesiunea8.testing_examples.app.func import is_div_3_5, NotInException, only_ints
import unittest
from parameterized import parameterized


class TestFunc(unittest.TestCase): # pentru a testa trebuie intotdeauna sa creeam o clasa
    def test_is_div_3_5_35(self):
        self.assertEqual(35, is_div_3_5(15))  # ruleaza test cu return ok

    def test_is_div_3_5_3(self):
        self.assertEqual(3, is_div_3_5(9))

    def test_is_div_3_5_5(self):
        self.assertEqual(5, is_div_3_5(25))

    def test_is_div_3_5_not_div(self):
        self.assertEqual(None, is_div_3_5(4))

    @parameterized.expand([ # o singura functie pentru toate instantele
        (15, 35),
        (9, 3),
        (25, 5),
        (4, None)
    ])
    def test_is_div_3_5(self, n, expected):
        self.assertEqual(expected, is_div_3_5(n))

    def test_only_ints_exceptions(self):
        self.assertRaises(NotInException, only_ints,[1,2,3,"s"])
