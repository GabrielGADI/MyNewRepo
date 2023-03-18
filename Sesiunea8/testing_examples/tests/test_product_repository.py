# testare product_repository
from Sesiunea8.testing_examples.app.product import Product
from Sesiunea8.testing_examples.app.product_repository import ProductRepository
import unittest
from parameterized import parameterized


class TestProductRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = ProductRepository()

    def test_get_all(self):
        # repo = ProductRepository()
        self.assertEqual(self.repo.products, self.repo.get_all())

    @parameterized.expand([
        ("Orez", Product(name="Orez", price=4.5, discount=10, category="Alimente de baza")),
        ("Vin", None)
    ])
    def test_get_by_name(self, name, expected):
        # repo = ProductRepository()
        self.assertEqual(expected, self.repo.get_by_name(name))