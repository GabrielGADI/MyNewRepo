from dataclasses import dataclass

@dataclass # decorator
class Product:
    name: str
    price: int
    discount: float
    category: str
    def get_final_price(self):
        return self.price - self.price * self.discount / 100
