# 1. Sa se creeze o clasa Student cu atributele nume, universitate si an (toate la constructor)
'''
2. Sa se creeze functiile specifice astfel incat la printarea unui student sa se
afiseze toate atributele acestui
'''

'''
3. Fie lista de studenti
students = [
         Student(name="Alex", university="Babes", year=3),
         Student(name="Cristina", university="Yale", year=4),
         Student(name="Meredith", university="Chicago", year=3),
         Student(name="George", university="Harvard", year=1),
         Student(name="Mark", university="NYU", year=4),
         Student(name="Owen", university="NYU", year=4),
         Student(name="Derek", university="Columbia", year=4)
         ]
a) Sa se creeze clasa StudentsDB in care sa se adauge ca si atribut de clasa lista de studenti
b) Sa se creeze o functie care primeste ca parametru numele unui student si verifica daca acel student 
este inregistrat la vreo universitate
c) Sa se creeze o functie care adauga un nou student in lista de studenti

'''


# 1.
class Student:
    def __init__(self, name, university, year):
        self.name = name
        self.university = university
        self.year = year

    # 2.
    def __str__(self):
        return f"name = {self.name} universiy = {self.university} year = {self.year}"

    def __repr__(self):  # cand nu avem liste vom aplica metoda pentru apelare str
        return str(self)  # apelam functia str


s = Student("Mike", 'UMC', 2010)
print(s)


# 3. a)
class StudentsDB:
    students = [
        Student(name="Alex", university="Babes", year=3),
        Student(name="Cristina", university="Yale", year=4),
        Student(name="Meredith", university="Chicago", year=3),
        Student(name="George", university="Harvard", year=1),
        Student(name="Mark", university="NYU", year=4),
        Student(name="Owen", university="NYU", year=4),
        Student(name="Derek", university="Columbia", year=4)
    ]

    # 3. b)
    def check_enrolled_student(self, name):
        for student in self.students:
            if name == student.name and student.university:
                return True
        return False

    # 3. c)
    def add_student(self, student):
        self.students.append(student)


db = StudentsDB()
print(db.check_enrolled_student("Mark"))
db.add_student(Student("Mike", "UMC", 2010))
print(db.students)
