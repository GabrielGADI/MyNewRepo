from abc import ABC, abstractmethod
import math



class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.latura = latura

    def aria(self):
        return self.latura * self.latura

    def perimetru(self):
        return 4 * self.latura

class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.raza = raza

    def aria(self):
        return math.pi * self.raza ** 2

    def perimetru(self):
        return 2 * math.pi * self.raza

