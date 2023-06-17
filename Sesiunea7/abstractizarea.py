'''
O clasa abstracta este o clasa care are cel putin o metoda abstracta
O metoda abstracta este o metoda fara corp (implementare)
abc - abstract base class
'''

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod  # functie abstract ca decorator
    def sound(self):  # functie fara corp
        pass

    @abstractmethod
    def sleep(self):  # functie fara corp specificand @abstractmethod
        raise NotImplementedError


class Dog(Animal):  # ca o clasa sa fie clasa concret, trebuie sa implementeze toate functiile din clasa abstracta
    def sound(self):
        print("Woof")

    def sleep(self):
        print("zzz")


class Cat(Animal):
    def sound(self):
        print("miow")

    def sleep(self):
        print("prrr")
