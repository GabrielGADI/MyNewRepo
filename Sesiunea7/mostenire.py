'''
 mostenirea - luarea tuturor atributelor si functiilor din clasa care mosteneste
 mostenirea ne ajuta sa nu mai scriem cod duplicat daca vrem sa avem obiecte care fac acelasi lucru
 mostenirea - relatie de tip "is"
'''
class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def print_name(self):
        print(f"My name is {self.name}")


class Student(Person): # Student mosteneste tot ce este in clasa Person
    pass


class Worker(Person): # Worker mosteneste tot ce este in clasa Person
    def __init__(self, age, name, job): # suprascriere constructor pentru adaugare noi atribute
        # Person.__init__(self, age, name) # apelarea constructorului clasei parinte (person)
        super().__init__(age, name) # o alta metoda de apelare a constructorului clasei parinte (Person)
        self.job = job


p = Person(18, "Mike")
p.print_name()

st = Student(20, "John")
st.print_name()

wk1 = Worker(21, "Leti", "Bancher")
wk1.print_name()
print(wk1.job)
print(wk1.age)

print(type(p))
print(type(st))
print(type(wk1))