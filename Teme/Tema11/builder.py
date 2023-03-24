'''
a. La ce este folosit?

Builder este un model de design creațional care vă permite să construiți obiecte complexe pas cu pas.
Modelul vă permite să produceți diferite tipuri și reprezentări ale unui obiect folosind același cod de construcție.
Modelul Builder poate fi aplicat atunci când construirea diferitelor reprezentări ale produsului implică pași
similari care diferă doar în detalii.

'''

'''
b. PROS & CONS

    PROS:
    - puteți construi obiecte pas cu pas, puteți amâna pașii de construcție sau puteți rula pașii recursiv.
    - puteți reutiliza același cod de construcție atunci când construiți diferite reprezentări ale produselor.
    - principiul responsabilității unice. Puteți izola codul de construcție complex din logica de afaceri a produsului.
    
CONS:
    - complexitatea generală a codului crește, deoarece modelul necesită crearea mai multor clase noi.
'''

'''
c. Exemplu cod (template, nu neaparat exemplu din viata reala)
'''


class Product:
    def __init__(self):
        self.part_a = None
        self.part_b = None
        self.part_c = None


class Builder:
    def build_part_a(self):
        pass

    def build_part_b(self):
        pass

    def build_part_c(self):
        pass

    def get_product(self):
        pass


class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.part_a = "Part A"

    def build_part_b(self):
        self.product.part_b = "Part B"

    def build_part_c(self):
        self.product.part_c = "Part C"

    def get_product(self):
        return self.product


class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_part_a()
        self.builder.build_part_b()
        self.builder.build_part_c()


builder = ConcreteBuilder()
director = Director(builder)
director.construct()
product = builder.get_product()
print(product.part_a)
print(product.part_b)
print(product.part_c)