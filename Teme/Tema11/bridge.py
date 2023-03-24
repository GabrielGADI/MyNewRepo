'''
a. La ce este folosit?

Bridge - un model de proiectare structurală care vă permite să împărțiți o clasă mare sau un set de clase strâns
legate în două ierarhii separate - abstracție și implementare - care pot fi dezvoltate independent una de cealaltă.
'''

'''
b. PROS & CONS

PROS:
    - puteți crea clase și aplicații independente de platformă.
    - codul client funcționează cu abstracții de nivel înalt. Nu este expus detaliilor platformei.
    - rincipiul deschis/închis. Puteți introduce noi abstracții și implementări independent unele de altele.
    - principiul responsabilității unice. Vă puteți concentra pe logica de nivel înalt în abstractizare și pe 
    detaliile platformei în implementare.
    
    CONS:
    - ați putea face codul mai complicat prin aplicarea modelului unei clase foarte coezive.
'''

'''
c. Exemplu cod (template, nu neaparat exemplu din viata reala)
'''


class Abstraction:
    def __init__(self, implementation):
        self.implementation = implementation

    def operation(self):
        self.implementation.operation_implementation()


class Implementation:
    def operation_implementation(self):
        pass


class ConcreteImplementationA(Implementation):
    def operation_implementation(self):
        print("ConcreteImplementationA operation implementation")


class ConcreteImplementationB(Implementation):
    def operation_implementation(self):
        print("ConcreteImplementationB operation implementation")


implementation_a = ConcreteImplementationA()
implementation_b = ConcreteImplementationB()

abstraction_a = Abstraction(implementation_a)
abstraction_a.operation()

abstraction_b = Abstraction(implementation_b)
abstraction_b.operation()

'''

d. (Optionala) O descriere a unde ar putea fi folosit in viata reala (nu neaparat exemplu legat de IT)

  Se poate folosi intr-o fabrica de productie masini, creeandu-se un model de masina care implica toate procesele 
de productie si pe de alta parte logistica pentru achizitionarea de materiale, comunicare eficienta cu 
furnizorii si termene limita de livrare si tot ce implica furnizarea de materiale necesare pentru productie si 
vanzarea produsului(model - masina).
   Fabrica de productie de masini poate fi considerat Bridge
   
'''
