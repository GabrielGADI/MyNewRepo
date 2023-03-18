'''
ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
probabil am colturi’
'''
from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        print("Cel mai probabil am colturi.")


print(40 * "*")

'''
INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură
'''


class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.latura = latura


print(40 * "*")

'''
ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
implementezi metoda abstractă aria)

Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI
mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
abstractă aria)
'''


class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura
        print(f'In initul clasei patrat, pi = {self.PI}')

    @property
    def latura(self):
        print("Setting as property")
        return self.__latura

    @latura.getter
    def latura(self):
        print("Getting value")
        return self.__latura

    @latura.setter
    def latura(self, value):
        print("Setting new value")
        self.__latura = value

    @latura.deleter
    def latura(self):
        print("Deleting value")
        self.__latura = None


class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    def aria(self):
        return self.PI * (self.__raza ** 2)

    @property
    def raza(self):
        print("Setting as property")
        return self.__raza

    @raza.getter
    def raza(self):
        print("Getting value")
        return self.__raza

    @raza.setter
    def raza(self, value):
        print("Setting new value")
        self.__raza = value

    @raza.deleter
    def raza(self):
        print("Deleting value")
        self.__raza = None


def descrie():
    print("Eu nu am colturi.")


print(40 * "*")

'''
POLYMORPHISM
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
Creează un obiect de tip Pătrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui
'''


class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.latura = latura

    def aria(self):
        return self.latura * self.latura

    def perimetru(self):
        return 4 * self.latura


p = Patrat(7)


def print_patrat_info(p):
    print("Aria patratului este:", p.aria())
    print("Perimetrul patratutlui este:", p.perimetru())


print_patrat_info(p)

import math


class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.raza = raza

    def aria(self):
        return math.pi * self.raza ** 2

    def perimetru(self):
        return 2 * math.pi * self.raza


c = Cerc(5)


def print_cerc_info(c):  # apelam c obiectul, atributul trebuie cu litera mica
    print("Aria cercului este:", c.aria())
    print("Perimetrul cercului este:", c.perimetru())

def descriere_interfata(obj):
    obj.descriere()

print_cerc_info(c)

print(40 * "*")
