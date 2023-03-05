from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    @abstractmethod
    def arie(self):
        pass

    @abstractmethod
    def perimetru(self):
        pass


class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.latura = latura

    def arie(self):
        return self.latura ** 2

    def perimetru(self):
        return self.latura * 4


class Dreptunghi(FormaGeometrica):
    def __init__(self, lungime, latime):
        self.lungime = lungime
        self.latime = latime

    def arie(self):
        return self.lungime * self.latime

    def perimetru(self):
        return 2 * (self.lungime + self.latime)


class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.raza = raza

    def arie(self):
        return 3.14 * self.raza ** 2

    def perimetru(self):
        return 2 * 3.14 * self.raza
